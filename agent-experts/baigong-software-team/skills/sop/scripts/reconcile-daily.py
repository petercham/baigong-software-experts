#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T02-E · 日终对账（B0 退路三重保证之一／主路常态对账）

规范锚点：架构 v2.9 §9 B0 行（日终对账）／§4 触发源六闭集之「对账差≠0」。
对账对象＝账本六类记录 vs git 提交／租约台账交叉核；差≠0 → 写「呈报」类审计事件
（触发源＝对账差≠0，六闭集成员）。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

RECORD_TYPES = ["派发", "写入", "签字", "注入包哈希", "intake 登记", "呈报"]  # 账本六类（§3）

# —— SWB-B16-f 修一（纯增·消费侧净化标注＝台账消费工序对内容外部字段按不可信输入处理＝红六破法向丙在册） ——
EXTERNAL_CONTENT_TYPES = ("呈报", "intake 登记")  # 外部内容面条目类闭集（同件具名＝RECORD_TYPES 六类本体不动）
EXTERNAL_CONTENT_FIELD_KEYS = frozenset({  # 外部内容字段键枚举闭集＝逐键标注不重写（不清洗不覆盖＝史实锚存续）
    "command_excerpt", "diff_items", "note", "reason", "path", "input_path", "text", "title",
})


def default_ledger_root() -> str:
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(os.getcwd(), ".collab", "ledger"))


def canonical_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def read_records(ledger_file: str) -> list[dict]:
    recs = []
    if os.path.exists(ledger_file):
        with open(ledger_file, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    recs.append(json.loads(line))
    return recs


def annotate_untrusted(records: list[dict]) -> int:
    """SWB-B16-f 修一（消费侧净化标注）＝读台账后、对账判定前＝外部内容面条目入不可信输入标注态：
    条目级逐键枚举命中面（EXTERNAL_CONTENT_FIELD_KEYS 闭集）＝内存标注＝不清洗不覆盖＝账本数据面零触；
    对账判定取径只取「写入」类记账字段＝外部内容字段永不参与判定＝标注态处置具名（污染台账亦防＝向丙在册）。"""
    annotated = 0
    for r in records:
        if r.get("type") in EXTERNAL_CONTENT_TYPES:
            payload = r.get("payload") or {}
            r["_untrusted_input"] = sorted(k for k in payload if k in EXTERNAL_CONTENT_FIELD_KEYS)
            annotated += 1
    return annotated


def append_report(ledger_file: str, payload: dict) -> dict:
    recs = read_records(ledger_file)
    prev_hash = recs[-1]["hash"] if recs else "GENESIS"
    rec = {
        "seq": len(recs) + 1,
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "type": "呈报",
        "actor": "reconcile-daily.py",
        "payload": payload,
        "prev_hash": prev_hash,
    }
    rec["hash"] = hashlib.sha256(
        f'{rec["seq"]}\n{rec["ts"]}\n{rec["type"]}\n{rec["actor"]}\n{canonical_json(rec["payload"])}\n{prev_hash}'.encode("utf-8")
    ).hexdigest()
    os.makedirs(os.path.dirname(ledger_file), exist_ok=True)
    with open(ledger_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def reconcile(ledger_file: str, leases_file: str, states_file: str, repo_root: str) -> dict:
    """交叉核：①「写入」类记录 vs git 提交数（写入记录不应超可归属提交面）；
    ②租约台账票ID vs 状态机票据登记（租约须有在册票据）。差≠0 →「呈报」类审计事件。"""
    records = read_records(ledger_file)
    untrusted_annotated = annotate_untrusted(records)  # 修一＝对账前净化标注（内存态·账本零触）
    by_type = {t: 0 for t in RECORD_TYPES}
    for r in records:
        if r["type"] in by_type:
            by_type[r["type"]] += 1

    diffs: list[str] = []

    # ① 写入记录 vs git 提交交叉核
    write_recs = [r for r in records if r["type"] == "写入"]
    git_commits: list[str] = []
    try:
        out = subprocess.run(["git", "-C", repo_root, "log", "--pretty=%H"],
                             capture_output=True, text=True, timeout=30)
        if out.returncode == 0:
            git_commits = [l.strip() for l in out.stdout.splitlines() if l.strip()]
    except Exception:
        diffs.append("git 提读取数失败")
    tagged = [r for r in write_recs if str(r["payload"].get("commit", "")).lower() != "unattributed"]
    if len(tagged) > len(git_commits):
        diffs.append(f"写入类记录(可归属)={len(tagged)} > git 提交={len(git_commits)}")

    # SWB-B16-f 修二（判定变更·A2 台账条目绑 commit 对象）＝「写入」类条目经前向哈希主信任锚（git 原生链面＝本段已取 git_commits 复用零新读）
    # 交叉核绑定态＝未绑定条目（commit 字段缺席／空值／unattributed／链面对象不存在）入标注态＝不列 diffs＝零回填零追炸（生效日＝放行落链笔起算）。
    # schema 面＝RECORD_TYPES 六类闭集不动（J-1 终裁采甲在册）＝绑定态＝条目字段级扩展具名申明。
    commit_set = set(git_commits)
    bound_recs, unbound_annotated, unbound_seq = 0, 0, []
    for r in write_recs:
        c = str(r["payload"].get("commit", "")).strip().lower()
        if c and c != "unattributed" and c in commit_set:
            bound_recs += 1
        else:
            unbound_annotated += 1
            unbound_seq.append(r.get("seq"))

    # ② 租约台账 vs 票据登记交叉核
    tickets_in_states: set[str] = set()
    if os.path.exists(states_file):
        with open(states_file, encoding="utf-8") as f:
            tickets_in_states = set(json.load(f).keys())
    lease_ticket_ids: set[str] = set()
    if os.path.exists(leases_file):
        with open(leases_file, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    e = json.loads(line)
                    if e.get("cleared") or not isinstance(e.get("lease"), dict):
                        continue  # freeze cleared 行（无 lease 键）跳过租约字段（方案甲·读侧容行）
                    lease_ticket_ids.add(e["lease"]["ticket_id"])
    orphan_leases = sorted(lease_ticket_ids - tickets_in_states)
    if orphan_leases:
        diffs.append(f"租约台账存在无在册票据票ID: {orphan_leases}")

    result = {"counts_by_type": by_type, "git_commits": len(git_commits),
              "leases": len(lease_ticket_ids), "tickets": len(tickets_in_states),
              "write_binding": {"bound": bound_recs, "unbound_annotated": unbound_annotated,
                                "unbound_seq": unbound_seq},  # 修二绑定核验标注态入消费读数（标注不判红＝零追炸）
              "untrusted_annotated": untrusted_annotated,  # 修一净化标注态入消费读数
              "diff": len(diffs), "diff_items": diffs}
    if diffs:
        rec = append_report(ledger_file, {"event": "audit_reconcile_diff",
                                          "trigger_source": "对账差≠0",  # 触发源六闭集成员（§4/§13）
                                          "diff_items": diffs})
        result["report_ledger_hash"] = rec["hash"]
    return result


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="日终对账（六类记录 vs git 提交/租约台账交叉核）")
    root = default_ledger_root()
    ap.add_argument("--ledger", default=os.path.join(root, "ledger.jsonl"))
    ap.add_argument("--leases", default=os.path.join(root, "leases.jsonl"))
    ap.add_argument("--states", default=os.path.join(root, "states.json"))
    ap.add_argument("--repo-root", default=os.getcwd())
    a = ap.parse_args(argv)
    result = reconcile(a.ledger, a.leases, a.states, a.repo_root)
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
