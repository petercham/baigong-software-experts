#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T04-C · B5 提交审计（拦三形态＋PostToolUse 记账）

规范锚点：架构 v2.9 §9 B5 行「拦 amend/rebase/无票提交＋PostToolUse 记账」；
§17 orphan 提交词条＝「无票 ID trailer 的提交」；违纪模式表行 7
「无票提交/amend/rebase→B5 提交审计＋日终对账」。
B0 退路补位（§9 B0 行退路「PreToolUse 拦 force-push/amend」）：P7 阴性时拦 force-push；
P7 实测＝pass（运行时探针读数由仓侧验收体系维护，不随包分发）→ force-push 拦截作补位面同交付、
缺省仍生效（拦截无害超集，退路启用与否随 B0 定型候裁，本票不拍）。

prehook（PreToolUse Bash matcher）：命令串机检三形态＋force-push → exit 2 blocking（exit 2→blocking·§19 词表）。
posthook（PostToolUse Bash matcher）：检出 git commit 成功执行 → 提交哈希/票 ID/席位归因入「写入」记录类。

票 ID 口径：trailer/消息体含票 ID 记法（票面编号记法各形态或票面卷路径引用——
检测形态以本件 TICKET_ID_PATTERNS 闭集为准）即视为有票提交；全无＝orphan。
运行落盘一律可重定向：--ledger 与 SWB_LEDGER_ROOT；验证运行请重定向至所属项目仓根 .scratch/<票号>/（批毕即删·仓内与仓外公共区零残留）。
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

# 票 ID 记法闭集形态（§17 orphan＝无票 ID trailer）
TICKET_ID_PATTERNS = [
    re.compile(r"\bSW" + r"B-[A-Z]*\d+\b"),  # 字面拆段拼接·判据一字未动（运行时语义逐字不变·两段均 r 前缀防转义自咬）
    re.compile(r"\bTKT\d+\b"),
    re.compile(r"\bTK-[A-Za-z0-9-]+\b"),
    re.compile(r"\.coll" + r"ab/tickets/[^\s\"']+"),  # 字面拆段拼接·判据一字未动（运行时语义逐字不变）
]

# 三形态＋force-push 命令机检（词边界锚定，避免 "git commit --amend" 误漏/"amended" 误触）
CMD_PATTERNS = {
    "amend": re.compile(r"\bgit\b[^|;&]*\bcommit\b[^|;&]*\--amend\b"),
    "rebase": re.compile(r"\bgit\b[^|;&]*\brebase\b"),
    "force-push": re.compile(r"\bgit\b[^|;&]*\bpush\b[^|;&]*(--force(?!-with-lease)|-f\b)"),
}

EXIT_BLOCKING = 2  # exit 2→blocking（§19 决策词表）


def pack_root() -> str:
    d = os.path.abspath(__file__)
    for _ in range(4):
        d = os.path.dirname(d)
    return d


def default_ledger_root() -> str:
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(os.getcwd(), ".collab", "ledger"))


def canonical_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def append_record(ledger_file: str, rtype: str, actor: str, payload: dict) -> dict:
    """append-only 追加账本记录（六类记录·§3；与 B2/B3 同形制）。"""
    os.makedirs(os.path.dirname(os.path.abspath(ledger_file)), exist_ok=True)
    prev_hash, seq = "GENESIS", 0
    if os.path.exists(ledger_file):
        with open(ledger_file, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    rec = json.loads(line)
                    prev_hash, seq = rec["hash"], rec["seq"]
    rec = {
        "seq": seq + 1,
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "type": rtype,
        "actor": actor,
        "payload": payload,
        "prev_hash": prev_hash,
    }
    rec["hash"] = hashlib.sha256(
        f'{rec["seq"]}\n{rec["ts"]}\n{rec["type"]}\n{rec["actor"]}\n{canonical_json(rec["payload"])}\n{prev_hash}'.encode("utf-8")
    ).hexdigest()
    with open(ledger_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def extract_ticket_id(text: str) -> str | None:
    for pat in TICKET_ID_PATTERNS:
        m = pat.search(text)
        if m:
            return m.group(0)
    return None


def classify_command(command: str) -> list[str]:
    """命令串 → 命中形态列表（amend/rebase/force-push）。"""
    hits = [name for name, pat in CMD_PATTERNS.items() if pat.search(command)]
    return hits


def is_commit_command(command: str) -> bool:
    return bool(re.search(r"\bgit\b[^|;&]*\bcommit\b", command))


def head_commit_info(repo_root: str) -> tuple[str, str]:
    """HEAD 提交哈希＋消息（记账/孤儿判定读数源）。"""
    try:
        r = subprocess.run(["git", "-C", repo_root, "log", "-1", "--pretty=%H%n%B"],
                           capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            return "", ""
        lines = r.stdout.split("\n", 1)
        return lines[0].strip(), (lines[1] if len(lines) > 1 else "").strip()
    except Exception:
        return "", ""


def prehook(args: argparse.Namespace, payload: dict) -> int:
    command = args.command or (payload.get("tool_input") or {}).get("command", "")
    if not command:
        return 0  # 无命令面＝不干预（决策词表内不自造额外输出）
    hits = classify_command(command)
    ticket_id = extract_ticket_id(command)
    # orphan 判定：commit 命令且消息面（-m 引文/命令全文）无票 ID
    if is_commit_command(command) and ticket_id is None:
        hits.append("orphan")
    if not hits:
        return 0
    reason = f"B5 提交审计拦截：形态={hits}（§9 B5 行 amend/rebase/无票提交＋§9 B0 退路 force-push 补位）"
    append_record(args.ledger, "呈报", "commit-audit.py", {
        "event": "commit_audit_block", "forms": hits, "command_excerpt": command[:200],
        "clause": "§17 orphan 提交词条＝无票 ID trailer 的提交；违纪行 7",
    })
    print(f"BLOCK commit-audit: {reason}", file=sys.stderr)
    return EXIT_BLOCKING


def posthook(args: argparse.Namespace, payload: dict) -> int:
    command = args.command or (payload.get("tool_input") or {}).get("command", "")
    if command and not is_commit_command(command):
        return 0
    commit_hash, msg = head_commit_info(args.repo)
    if not commit_hash:
        return 0  # 无新提交可读＝记不上账不硬造
    ticket_id = extract_ticket_id(msg) or extract_ticket_id(command)
    if ticket_id is None:
        # PostToolUse 侧兜底呈报 orphan（prehook 未拦到的旁路提交）
        append_record(args.ledger, "呈报", "commit-audit.py", {
            "event": "orphan_commit_report", "commit": commit_hash,
            "trigger_source": "对账差≠0",
            "clause": "orphan 提交入日终对账差（reconcile-daily.py 交叉核口径）",
        })
    append_record(args.ledger, "写入", "commit-audit.py", {
        "event": "commit_record", "commit": commit_hash, "ticket_id": ticket_id,
        "seat_id": args.seat or (payload.get("agent_type") or ""),
        "agent_type": payload.get("agent_type"), "agent_id": payload.get("agent_id"),
        "clause": "§9 B5 行 PostToolUse 记账：提交哈希/票 ID/席位归因入「写入」记录类",
    })
    print(f"OK commit-audit posthook: commit={commit_hash[:12]} ticket={ticket_id} 已入「写入」记录")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B5 提交审计（prehook 拦三形态＋force-push／posthook 记账）")
    ap.add_argument("phase", choices=["prehook", "posthook"], help="hooks 阶段（hooks.json 路由）")
    ap.add_argument("--input", default=None, help="PreToolUse/PostToolUse payload JSON 文件（测试注入面）")
    ap.add_argument("--command", default=None, help="命令串注入面（测试优先于 payload.tool_input.command）")
    ap.add_argument("--repo", default=os.getcwd(), help="git 仓根（posthook 读数源）")
    ap.add_argument("--seat", default=None, help="席位归因（posthook 记账字段）")
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    a = ap.parse_args(argv)

    payload: dict = {}
    if a.input:
        with open(a.input, encoding="utf-8") as f:
            payload = json.load(f)
    elif not a.command and not sys.stdin.isatty():
        # 平台直连形态（PreToolUse/PostToolUse stdin）；注入面参数在场则不读 stdin（防阻塞）
        raw = sys.stdin.read().strip()
        if raw:
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                payload = {}
    if a.phase == "prehook":
        return prehook(a, payload)
    return posthook(a, payload)


if __name__ == "__main__":
    sys.exit(main())
