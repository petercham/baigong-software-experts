#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S2 施工测试实体 · 账本核心（B0/B1/B2/对账）——工程师写、CI 机械执行、QA 出结论（三段式·表2-2）。

本件居交付树 tests（项目根字面 tests/**＝施工与验收测试实体·判据真源双层双址条款·SWB-B4 两级锚换代）。
argv 面：额外文件路径参数＝待一并机械执行的兄弟测试件（票面判据 5 调用形制
`python test_ledger_core.py test_lease_instantiation.py`）。
"""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.dirname(os.path.dirname(HERE))                       # baigong-software-team
SCRIPTS = os.path.join(PACK, "skills", "sop", "scripts")


def load_script(name: str):
    path = os.path.join(SCRIPTS, name)
    spec = importlib.util.spec_from_file_location(name.replace("-", "_").replace(".py", ""), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


intake = load_script("intake-register.py")
state = load_script("state-transition.py")
reconcile_mod = load_script("reconcile-daily.py")


def read_ledger(path: str) -> list[dict]:
    out = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    out.append(json.loads(line))
    return out


def t01_intake_registers_and_echoes(tmp: str) -> None:
    src = os.path.join(tmp, "input.md")
    with open(src, "w", encoding="utf-8") as f:
        f.write("人类输入原件内容\n")
    led = os.path.join(tmp, "ledger.jsonl")
    rec = intake.register_intake(src, "指令", led)
    assert rec["type"] == "intake 登记"
    assert rec["payload"]["reg_no"].startswith("INTK-")
    assert len(rec["payload"]["sha256"]) == 64
    # 四字段在位（外部输入件登记四字段·表2-2 B1 行）
    for k in ("source_role", "declaration_tier", "sha256", "purity_scan_ref"):
        assert k in rec["payload"]
    assert read_ledger(led)[-1]["hash"] == rec["hash"]


def t02_intake_class_closed_set(tmp: str) -> None:
    src = os.path.join(tmp, "input2.md")
    with open(src, "w", encoding="utf-8") as f:
        f.write("x\n")
    led = os.path.join(tmp, "ledger2.jsonl")
    for cls in intake.TRANSCRIPTION_CLASSES:
        assert len(intake.TRANSCRIPTION_CLASSES) == 6
        intake.register_intake(src, cls, led)
    try:
        intake.register_intake(src, "业务解析", led)  # 闭集外→拒
        raise AssertionError("闭集外誊录类型未被拒")
    except SystemExit:
        pass


def t03_legal_transition_chain(tmp: str) -> None:
    led = os.path.join(tmp, "led3.jsonl")
    st = os.path.join(tmp, "states3.json")
    assert state.transition("TKT-X", 1, 1, kind="dispatch", signs=[], ticket_type="开发",
                            severity=None, severity_confirmed=False, human_direct=False,
                            ledger_file=led, states_file=st) == 0
    assert state.transition("TKT-X", 1, 2, kind="signoff",
                            signs=intake_s1_signs(), ticket_type="开发",
                            severity=None, severity_confirmed=False, human_direct=False,
                            ledger_file=led, states_file=st) == 0
    types = [r["type"] for r in read_ledger(led)]
    assert "派发" in types and "签字" in types  # 每次迁移写对应记录类


def intake_s1_signs() -> list[str]:
    return ["产品交付签", "架构PRD接收签", "QA可验收性签"]


def t04_illegal_transition_4_to_1_rejected_with_report(tmp: str) -> None:
    led = os.path.join(tmp, "led4.jsonl")
    st = os.path.join(tmp, "states4.json")
    state.transition("TKT-Y", 1, 1, kind="dispatch", signs=[], ticket_type="开发",
                     severity=None, severity_confirmed=False, human_direct=False,
                     ledger_file=led, states_file=st)
    for i in range(1, 4):  # 推到节点 4 执行
        state.transition("TKT-Y", i, i + 1, kind="signoff", signs=state.SIGNSETS[i],
                         ticket_type="开发", severity=None, severity_confirmed=False,
                         human_direct=False, ledger_file=led, states_file=st)
    rc = state.transition("TKT-Y", 4, 1, kind="dispatch", signs=[], ticket_type="开发",
                          severity=None, severity_confirmed=False, human_direct=False,
                          ledger_file=led, states_file=st)
    assert rc != 0, "非法迁移 4→1 须 exit≠0"
    reports = [r for r in read_ledger(led) if r["type"] == "呈报"]
    assert len(reports) == 1, "非法迁移须恰产生一条「呈报」类记录"
    assert reports[0]["payload"]["event"] == "audit_transition_rejected"


def t05_severity_gate_p0_defect(tmp: str) -> None:
    led = os.path.join(tmp, "led5.jsonl")
    st = os.path.join(tmp, "states5.json")
    state.transition("BUG-1", 1, 1, kind="dispatch", signs=[], ticket_type="缺陷",
                     severity=None, severity_confirmed=False, human_direct=False,
                     ledger_file=led, states_file=st)
    for i in range(1, 3):
        state.transition("BUG-1", i, i + 1, kind="signoff", signs=state.SIGNSETS[i],
                         ticket_type="缺陷", severity=None, severity_confirmed=False,
                         human_direct=False, ledger_file=led, states_file=st)
    # 定级未确认的 P0 缺陷票链迁移（进入 4 执行）→ exit≠0＋呈报一条
    rc = state.transition("BUG-1", 3, 4, kind="dispatch", signs=[], ticket_type="缺陷",
                          severity="P0", severity_confirmed=False, human_direct=False,
                          ledger_file=led, states_file=st)
    assert rc != 0
    reports = [r for r in read_ledger(led) if r["type"] == "呈报"]
    assert len(reports) == 1
    # 定级确认签收在位后放行（脚本只校验签收字段在位、不判级）；离开节点 3 仍须表2-3 签字集合
    rc2 = state.transition("BUG-1", 3, 4, kind="signoff", signs=state.SIGNSETS[3], ticket_type="缺陷",
                           severity="P0", severity_confirmed=True, human_direct=False,
                           ledger_file=led, states_file=st)
    assert rc2 == 0


def t06_hold_requires_human_direct(tmp: str) -> None:
    led = os.path.join(tmp, "led6.jsonl")
    st = os.path.join(tmp, "states6.json")
    state.transition("TKT-H", 1, 1, kind="dispatch", signs=[], ticket_type="开发",
                     severity=None, severity_confirmed=False, human_direct=False,
                     ledger_file=led, states_file=st)
    rc = state.transition("TKT-H", 1, "挂起", kind="dispatch", signs=[], ticket_type="开发",
                          severity=None, severity_confirmed=False, human_direct=False,
                          ledger_file=led, states_file=st)
    assert rc != 0, "脚本不得自触发挂起"
    rc2 = state.transition("TKT-H", 1, "挂起", kind="dispatch", signs=[], ticket_type="开发",
                           severity=None, severity_confirmed=False, human_direct=True,
                           ledger_file=led, states_file=st)
    assert rc2 == 0
    holds = [r for r in read_ledger(led) if r["payload"].get("event") == "emergency_hold"]
    assert len(holds) == 1  # 紧急停票写「呈报」类记录留痕


def t07_timeouts_defaults(tmp: str) -> None:
    cfg = state.load_timeouts(None)
    assert cfg["工程师票"] == 48.0 and cfg["呈报"] == 24.0  # §13 缺省
    assert set(state.TRIGGER_SOURCES) == {"租约越界deny", "对账差≠0", "活性自检失败", "引用扫描命中", "超期", "熔断"}


def t08_reconcile_diff_writes_report(tmp: str) -> None:
    led = os.path.join(tmp, "led8.jsonl")
    leases = os.path.join(tmp, "leases8.jsonl")
    st = os.path.join(tmp, "states8.json")
    # 租约台账有一张无在册票据的租约 → 对账差≠0 → 呈报
    with open(leases, "w", encoding="utf-8") as f:
        f.write(json.dumps({"lease": {"ticket_id": "GHOST-1", "path_globs": [], "seat_id": "engineer", "hash": "x"}}, ensure_ascii=False) + "\n")
    res = reconcile_mod.reconcile(led, leases, st, PACK)
    assert res["diff"] >= 1
    reports = [r for r in read_ledger(led) if r["type"] == "呈报"]
    assert len(reports) == 1
    assert reports[0]["payload"]["trigger_source"] == "对账差≠0"  # 触发源六闭集成员


def run_self() -> int:
    tests = [t01_intake_registers_and_echoes, t02_intake_class_closed_set,
             t03_legal_transition_chain, t04_illegal_transition_4_to_1_rejected_with_report,
             t05_severity_gate_p0_defect, t06_hold_requires_human_direct,
             t07_timeouts_defaults, t08_reconcile_diff_writes_report]
    for t in tests:
        with tempfile.TemporaryDirectory() as tmp:
            t(tmp)
        print(f"PASS {t.__name__}")
    return 0


def main() -> int:
    rc = run_self()
    if rc != 0:
        return rc
    # argv 兄弟测试件机械执行（票面判据 5 调用形制）
    for p in sys.argv[1:]:
        if os.path.isfile(p):
            r = subprocess.run([sys.executable, p])
            if r.returncode != 0:
                return r.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
