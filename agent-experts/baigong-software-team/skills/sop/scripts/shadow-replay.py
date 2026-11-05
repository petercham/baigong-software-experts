#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""T04-G · B8 影子重放（失效＝重实现·不涉平台依赖）

规范锚点：架构 v2.9 §9 B8 行「读 .collab/ledger/＋.collab/archive/＋注入存档→差异三分类＋
过程痕迹扫描（引用可达性＋正文过程痕迹词族机检，命中 exit≠0；白名单＝指针三形态：
设计锚·哈希·治理域路径；扫描范围显式排除治理面；转正候选件入扫）」；
违纪模式表行 11「过程件被用作引用目标→B8 引用可达性扫描＋B11 下游件引用扫描」。

输入＝账本目录（ledger.jsonl/leases.jsonl/states.json）＋存档目录（.collab/archive/ 形态）
＋注入存档目录（dispatch-builder 注入包落盘形态）＋git 提交链（重放参照面）。
输出＝差异三分类记录：
  ①missing_in_replay＝账本声称的提交在 git 链缺席；
  ②missing_in_ledger＝git 链提交在账本「写入」记录无归属；
  ③mismatch＝两侧均在但字段比对不符（票 ID 缺席/提交哈希对不上）。
引用可达性扫描：被扫件内路径引用 → 目标不存在＝不可达命中；引用目标落过程库存档面
（archive/dlq 等＝过程件）＝「过程件被用作引用目标」命中（违纪行 11）。
白名单＝指针三形态（§9 B8 行）：设计锚（版本号＋行号段形态）·哈希（64/40 位 hex）·治理域路径（.collab/ 真源引用）。
扫描范围显式排除治理面（.collab/ 内文件不作词族扫描对象）；转正候选件（--candidate）入扫。
命中 exit≠0。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

# 过程痕迹词族（真源锚＝§17 正文纯度款 P-Ⅰ 禁项枚举：修订史述/评审审计表态叙述/辩解注/开工读数/轮次票号叙事）
PROCESS_TRACE_WORDS = ["修订史", "评审表态", "审计表态", "辩解", "开工读数", "轮次叙事", "表态叙述"]

WHITELIST_PATTERNS = [
    re.compile(r"\bV\d+\s*L\d+"),                        # 设计锚形态
    re.compile(r"\b[0-9a-f]{40,64}\b"),                  # 哈希形态
    re.compile(r"\.collab/(ledger|decisions|tickets|receipts|refs|manifest|human)/"),  # 治理域路径形态
]

PATH_REF_RE = re.compile(r"(?:\.collab|docs|\.archive|deliverables|tests)/[A-Za-z0-9_./\-{}\u4e00-\u9fff]+")
PROCESS_ARCHIVE_DIRS = (".collab/archive/", ".collab/dlq/", ".collab/process/", ".collab/evidence/")

EXIT_HIT = 1  # 过程痕迹/引用命中 → exit≠0（§9 B8 行）


def default_ledger_root() -> str:
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(os.getcwd(), ".collab", "ledger"))


def read_records(path: str) -> list[dict]:
    out = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    out.append(json.loads(line))
    return out


def append_record(ledger_file: str, rtype: str, actor: str, payload: dict) -> dict:
    os.makedirs(os.path.dirname(os.path.abspath(ledger_file)), exist_ok=True)
    prev_hash, seq = "GENESIS", 0
    for rec in read_records(ledger_file):
        prev_hash, seq = rec["hash"], rec["seq"]
    rec = {
        "seq": seq + 1,
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "type": rtype, "actor": actor, "payload": payload, "prev_hash": prev_hash,
    }
    rec["hash"] = hashlib.sha256(
        f'{rec["seq"]}\n{rec["ts"]}\n{rec["type"]}\n{rec["actor"]}\n'
        f'{json.dumps(rec["payload"], ensure_ascii=False, sort_keys=True, separators=(",", ":"))}\n{prev_hash}'.encode("utf-8")
    ).hexdigest()
    with open(ledger_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def git_commits(repo_root: str) -> dict[str, str]:
    """重放参照面：git 链 {hash: 消息首行}。"""
    out: dict[str, str] = {}
    try:
        r = subprocess.run(["git", "-C", repo_root, "log", "--pretty=%H%x09%s"],
                           capture_output=True, text=True, timeout=60)
        if r.returncode == 0:
            for line in r.stdout.splitlines():
                if "\t" in line:
                    h, s = line.split("\t", 1)
                    out[h.strip()] = s.strip()
    except Exception:
        pass
    return out


def classify_diffs(ledger_file: str, repo_root: str) -> dict:
    """差异三分类（§9 B8 行）。"""
    commits = git_commits(repo_root)
    write_recs = [r for r in read_records(ledger_file)
                  if r["type"] == "写入" and r["payload"].get("event") == "commit_record"]
    claimed = {str(r["payload"].get("commit", "")): r for r in write_recs}
    missing_in_replay = [c for c in claimed if c and c not in commits]
    missing_in_ledger = [h for h in commits if h not in claimed]
    mismatch: list[dict] = []
    for c, rec in claimed.items():
        if c in commits and rec["payload"].get("ticket_id") is None:
            mismatch.append({"commit": c, "note": "账本有归属但票 ID 缺席（orphan 应入对账差）"})
    return {"missing_in_replay": missing_in_replay, "missing_in_ledger": missing_in_ledger,
            "mismatch": mismatch}


def whitelisted(line: str) -> bool:
    return any(p.search(line) for p in WHITELIST_PATTERNS)


def scan_files(files: list[str], repo_root: str) -> dict:
    """过程痕迹扫描：词族机检＋引用可达性（扫描面显式排除治理面＝调用侧不入 .collab/ 文件；
    此处对每个被扫件防御性再排一次）。"""
    word_hits: list[dict] = []
    ref_hits: list[dict] = []
    for path in files:
        norm = path.replace("\\", "/")
        if "/.collab/" in f"/{norm}" or norm.startswith(".collab/") or "/.collab/" in norm:
            continue  # 扫描范围显式排除治理面（§9 B8 行）
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
        for i, line in enumerate(lines, 1):
            if whitelisted(line):
                continue
            for w in PROCESS_TRACE_WORDS:
                if w in line:
                    word_hits.append({"file": norm, "line": i, "word": w})
            for m in PATH_REF_RE.finditer(line):
                ref = m.group(0)
                abs_ref = ref if os.path.isabs(ref) else os.path.join(repo_root, ref)
                if any(ref.startswith(d) for d in PROCESS_ARCHIVE_DIRS):
                    ref_hits.append({"file": norm, "line": i, "ref": ref,
                                     "kind": "过程件被用作引用目标（违纪行 11）"})
                elif not os.path.exists(abs_ref):
                    ref_hits.append({"file": norm, "line": i, "ref": ref, "kind": "引用不可达"})
    return {"word_hits": word_hits, "ref_hits": ref_hits}


def collect_scan_files(archive_dir: str, inject_dir: str, candidates: list[str]) -> list[str]:
    files: list[str] = []
    for root_dir in (archive_dir, inject_dir):
        if root_dir and os.path.isdir(root_dir):
            for dirpath, _dirs, names in os.walk(root_dir):
                for n in names:
                    if n.endswith(".md"):
                        files.append(os.path.join(dirpath, n))
    files.extend(candidates)  # 转正候选件入扫（§9 B8 行）
    return files


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B8 影子重放（差异三分类＋过程痕迹/引用可达性扫描·命中 exit≠0）")
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    ap.add_argument("--repo", default=os.getcwd(), help="git 链读取仓根（重放参照面）")
    ap.add_argument("--archive", default=None, help="存档目录（.collab/archive/ 形态）")
    ap.add_argument("--inject", default=None, help="注入存档目录（dispatch 注入包落盘形态）")
    ap.add_argument("--candidate", action="append", default=[], help="转正候选件（可重复·入扫）")
    ap.add_argument("--out", default=None, help="差异三分类记录落盘 JSON（可重定向）")
    ap.add_argument("--report-ledger", default=None, help="命中呈报落账文件（缺省不写，避免误入仓账本）")
    a = ap.parse_args(argv)

    diffs = classify_diffs(a.ledger, a.repo)
    files = collect_scan_files(a.archive or "", a.inject or "", a.candidate)
    scan = scan_files(files, a.repo)
    result = {"diffs": diffs, "scan": scan,
              "clause": "§9 B8 行：差异三分类＋过程痕迹扫描（白名单＝指针三形态·治理面排除·候选件入扫）"}
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
    print(json.dumps(result, ensure_ascii=False))
    hit = bool(scan["word_hits"]) or bool(scan["ref_hits"])
    if hit and a.report_ledger:
        append_record(a.report_ledger, "呈报", "shadow-replay.py", {
            "event": "trigger_report", "trigger_source": "引用扫描命中",
            "word_hits": scan["word_hits"], "ref_hits": scan["ref_hits"],
            "clause": "违纪行 11 过程件被用作引用目标→B8 引用可达性扫描",
        })
    if hit:
        print(f"HIT shadow-replay: 词族命中={len(scan['word_hits'])} 引用命中={len(scan['ref_hits'])} -> exit≠0", file=sys.stderr)
        return EXIT_HIT
    return 0


if __name__ == "__main__":
    sys.exit(main())
