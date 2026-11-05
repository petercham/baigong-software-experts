#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B4 决策包装配（机械计算＋异常强制呈报·架构 v2.9 §9 B4 行）

规范锚点：架构 v2.9 §4 异常五类强制呈报，触发源六闭集
｛租约越界 deny／对账差≠0／活性自检失败／引用扫描命中／超期／熔断｝逐码实现为呈报触发枚举；
表2-2「决策包装配与呈报：状态机脚本；主理人仅投递」；
表2-2「灰度→全量＝QA 按声明判据机械门禁，不得现场裁量」→ 判据读取＝票内声明字段，
脚本比对读数，不符拒出 full-rollout 决策包；
§18⑩（次级承接）呈报面含缺陷定级字段：P0/P1 定级＝QA 双复核＋人类终裁，
决策包呈报面呈现定级（severity）与定级确认状态（severity_confirmed）。

运行落盘一律可重定向：--ledger/--out 与 SWB_LEDGER_ROOT；验证运行请重定向至所属项目仓根 .scratch/<票号>/（批毕即删）。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

def _load_sibling(name: str):
    """按文件路径加载同目录件（serial-gate.py 含连字符不可直接 import）。"""
    import importlib.util
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name)
    spec = importlib.util.spec_from_file_location(name.replace("-", "_").replace(".py", ""), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_gate = _load_sibling("serial-gate.py")
append_record = _gate.append_record
canonical_json = _gate.canonical_json
default_ledger_root = _gate.default_ledger_root

# ---- 触发源六闭集（§4）逐码枚举·六码名与 §4 六项一一对应 ----
TRIG_LEASE_DENY = "租约越界deny"        # ①租约越界 deny
TRIG_RECONCILE_DIFF = "对账差≠0"        # ②对账差≠0
TRIG_LIVENESS_FAIL = "活性自检失败"     # ③活性自检失败
TRIG_REF_SCAN_HIT = "引用扫描命中"      # ④引用扫描命中
TRIG_OVERDUE = "超期"                   # ⑤超期
TRIG_CIRCUIT_BREAK = "熔断"             # ⑥熔断
TRIGGER_CODES = {
    TRIG_LEASE_DENY, TRIG_RECONCILE_DIFF, TRIG_LIVENESS_FAIL,
    TRIG_REF_SCAN_HIT, TRIG_OVERDUE, TRIG_CIRCUIT_BREAK,
}

# 缺陷定级面（§18⑩）：定级权＝QA 双复核＋人类终裁（表2-2），本脚本只呈现、不判级
GRADES_REQUIRING_CONFIRM = {"P0", "P1"}

EXIT_TRIGGER_NOT_IN_CLOSURE = 2   # 触发码越出六闭集
EXIT_ROLLOUT_CRITERIA_MISMATCH = 3  # 灰度→全量机械门禁不符→拒出 full-rollout


def pack_root() -> str:
    d = os.path.abspath(__file__)
    for _ in range(4):
        d = os.path.dirname(d)
    return d


def build_report_pack(trigger: str, ticket_id: str, evidence: dict,
                      severity: str | None, severity_confirmed: bool,
                      ledger_file: str, out_path: str | None) -> dict:
    """异常强制呈报：触发码∈六闭集否则拒；呈报面含缺陷定级字段；呈报入账本「呈报」记录类。"""
    if trigger not in TRIGGER_CODES:
        print(f"REJECT: 触发码 {trigger!r} 越出触发源六闭集 {sorted(TRIGGER_CODES)}（§4）", file=sys.stderr)
        raise SystemExit(EXIT_TRIGGER_NOT_IN_CLOSURE)
    pack = {
        "pack_type": "呈报",
        "trigger_source": trigger,
        "ticket_id": ticket_id,
        "evidence": evidence,
        "defect_grading": {                      # 呈报面缺陷定级字段（§18⑩）
            "severity": severity,
            "severity_confirmed": severity_confirmed,
            "grading_authority": "QA 双复核＋人类终裁（表2-2）——本脚本呈现定级与定级确认状态，不判级",
        },
        "delivery": "主理人仅投递（表2-2）；装配与呈报＝状态机脚本（B4）",
        "built_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    pack["pack_hash"] = hashlib.sha256(canonical_json(
        {k: pack[k] for k in ("pack_type", "trigger_source", "ticket_id", "evidence", "defect_grading")}
    ).encode("utf-8")).hexdigest()
    rec = append_record(ledger_file, "呈报", "decision-pack.py",
                        {"event": "decision_pack_report", "ticket_id": ticket_id,
                         "trigger_source": trigger, "pack_hash": pack["pack_hash"]})
    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(pack, f, ensure_ascii=False, indent=2)
    print(f"OK report-pack ticket={ticket_id} trigger={trigger} pack_hash={pack['pack_hash']} ledger_hash={rec['hash']}")
    print(json.dumps(pack, ensure_ascii=False))
    return pack


def build_full_rollout_pack(ticket_id: str, declared_criteria: list[dict], readings: dict,
                            ledger_file: str, out_path: str | None) -> int:
    """灰度→全量机械门禁（表2-2）：判据读取＝票内声明字段，脚本逐项比对读数；
    任一不符→拒出 full-rollout 决策包（exit≠0）并写「呈报」类审计事件；全符→出包。"""
    if not declared_criteria:
        print("REJECT rollout: 票内无声明判据字段——灰度→全量判据读取＝票内声明字段，无声明不裁量（表2-2）", file=sys.stderr)
        append_record(ledger_file, "呈报", "decision-pack.py", {
            "event": "full_rollout_reject", "ticket_id": ticket_id,
            "reason": "票内声明判据缺席（不得现场裁量）",
        })
        return EXIT_ROLLOUT_CRITERIA_MISMATCH
    mismatches = []
    for crit in declared_criteria:
        key = crit["criterion"]
        if key not in readings:
            mismatches.append({"criterion": key, "declared": crit.get("expect"), "actual": None,
                               "note": "读数缺席"})
        elif str(readings[key]) != str(crit.get("expect")):
            mismatches.append({"criterion": key, "declared": crit.get("expect"),
                               "actual": readings[key], "note": "读数与声明判据不符"})
    if mismatches:
        append_record(ledger_file, "呈报", "decision-pack.py", {
            "event": "full_rollout_reject", "ticket_id": ticket_id,
            "mismatches": mismatches,
            "clause": "表2-2 QA 按声明判据机械门禁，不得现场裁量（B4）",
        })
        print(f"REJECT rollout ticket={ticket_id}: 声明判据比对不符，差异={mismatches}", file=sys.stderr)
        return EXIT_ROLLOUT_CRITERIA_MISMATCH
    pack = {
        "pack_type": "full-rollout",
        "ticket_id": ticket_id,
        "criteria_checked": declared_criteria,
        "readings": readings,
        "gate": "QA 按声明判据机械门禁通过（表2-2）；单签＝full-rollout（QA按声明判据单签·表2-3 节点6）",
        "built_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    pack["pack_hash"] = hashlib.sha256(canonical_json(
        {k: pack[k] for k in ("pack_type", "ticket_id", "criteria_checked", "readings")}
    ).encode("utf-8")).hexdigest()
    rec = append_record(ledger_file, "呈报", "decision-pack.py",
                        {"event": "decision_pack_full_rollout", "ticket_id": ticket_id,
                         "pack_hash": pack["pack_hash"]})
    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(pack, f, ensure_ascii=False, indent=2)
    print(f"OK full-rollout ticket={ticket_id} pack_hash={pack['pack_hash']} ledger_hash={rec['hash']}")
    print(json.dumps(pack, ensure_ascii=False))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B4 决策包装配（触发源六闭集呈报＋灰度→全量机械门禁·§9/§4）")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("report", help="异常强制呈报决策包（触发码∈六闭集）")
    p1.add_argument("--trigger", required=True, help=f"触发码（闭集：{sorted(TRIGGER_CODES)}）")
    p1.add_argument("--ticket", required=True)
    p1.add_argument("--evidence", default="{}", help="证据 JSON（JSON 字面或 JSON 文件路径）")
    p1.add_argument("--severity", default=None, help="缺陷定级（P0/P1/P2…·只呈现不判级·§18⑩）")
    p1.add_argument("--severity-confirmed", action="store_true", help="定级确认状态字段")
    p1.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    p1.add_argument("--out", default=None, help="决策包落盘路径（可重定向）")

    p2 = sub.add_parser("full-rollout", help="灰度→全量决策包（票内声明判据机械比对）")
    p2.add_argument("--ticket", required=True)
    p2.add_argument("--criteria", required=True, help="票内声明判据 JSON 文件（[{criterion,expect},…]）")
    p2.add_argument("--readings", required=True, help="实测读数 JSON 文件（{criterion: value}）")
    p2.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    p2.add_argument("--out", default=None, help="决策包落盘路径（可重定向）")

    a = ap.parse_args(argv)

    def load_json_arg(v: str) -> object:
        if os.path.exists(v):
            with open(v, encoding="utf-8") as f:
                return json.load(f)
        return json.loads(v)

    if a.cmd == "report":
        build_report_pack(a.trigger, a.ticket, load_json_arg(a.evidence),
                          a.severity, a.severity_confirmed, a.ledger, a.out)
        return 0
    criteria = load_json_arg(a.criteria)
    readings = load_json_arg(a.readings)
    return build_full_rollout_pack(a.ticket, criteria, readings, a.ledger, a.out)


if __name__ == "__main__":
    sys.exit(main())
