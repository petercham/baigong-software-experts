#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S3 施工测试实体 · 注入构造与派发闸（B3：dispatch-spec/dispatch-builder/serial-gate）——三段式（表2-2）。

本件居交付树 tests（项目根字面 tests/**＝施工与验收测试实体·判据真源双层双址条款·SWB-B4 两级锚换代）。
argv 面：额外文件路径参数＝待一并机械执行的兄弟测试件（票面判据 5 调用形制
`python test_dispatch_gate.py test_decision_pack.py`）。

覆盖：串行闸（活跃≠0 拒派发＋呈报恰一条＝票面判据3 形态）；白名单超集检测 exit≠0 回显差异集
（票面判据4 形态）；Agent ID 互验双向比对（§8）；注入包哈希入账「注入包哈希」记录类（§3 六类）；
dispatch-spec 八行结构（六节点＋维护行＋ADR·落盘行·签字集合非空）。运行落盘一律 Temp 重定向，仓内零残留。
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
CONFIG = os.path.join(PACK, "config")


def load_script(name: str):
    path = os.path.join(SCRIPTS, name)
    spec = importlib.util.spec_from_file_location(name.replace("-", "_").replace(".py", ""), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


builder = load_script("dispatch-builder.py")
gate = load_script("serial-gate.py")

SPEC_PATH = os.path.join(CONFIG, "dispatch-spec.json")


def read_ledger(path: str) -> list[dict]:
    out = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    out.append(json.loads(line))
    return out


def seed_states(states_file: str, mapping: dict) -> None:
    with open(states_file, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False)


def t01_spec_eight_rows_signoffs_nonempty(tmp: str) -> None:
    with open(SPEC_PATH, encoding="utf-8") as f:
        spec = json.load(f)
    assert len(spec["nodes"]) == 8, f"dispatch-spec 行数={len(spec['nodes'])} ≠ 8（六节点＋维护行＋ADR·落盘行）"
    assert all(len(n["signoffs"]) > 0 for n in spec["nodes"]), "存在签字集合为空的行"
    assert spec.get("derived_from") == "表2-3"
    maint = [n for n in spec["nodes"] if str(n["node"]).startswith("维护")]
    assert len(maint) == 1 and set(maint[0]["signoffs"]) == {"产品席", "架构席（合签）"}


def t02_serial_gate_active_nonzero_rejects_with_exactly_one_report(tmp: str) -> None:
    """票面判据3 形态：账本预置 1 张活跃票后调 dispatch → exit≠0 且「呈报」记录恰 1 条。"""
    led, st = os.path.join(tmp, "ledger.jsonl"), os.path.join(tmp, "states.json")
    seed_states(st, {"SWB-T99": {"state": 4, "ticket_type": "开发"}})
    rc = builder.dispatch({"ticket_id": "SWB-T03X", "node": 4, "seat_id": "engineer",
                           "agent_id": "engineer-x1"},
                          builder.load_spec(SPEC_PATH), led, st,
                          os.path.join(tmp, "agents.jsonl"), os.path.join(tmp, "inj"))
    assert rc != 0, "活跃票非零时派发未被串行闸拒绝"
    reports = [r for r in read_ledger(led) if r["type"] == "呈报"]
    assert len(reports) == 1, f"呈报记录数={len(reports)} ≠ 恰1条"
    assert reports[0]["payload"]["event"] == "serial_gate_reject"


def t03_dispatch_ok_writes_package_hash_record(tmp: str) -> None:
    """无活跃票→机械展开成功；注入包哈希写账本「注入包哈希」记录类（§3 六类）。"""
    led, st = os.path.join(tmp, "ledger.jsonl"), os.path.join(tmp, "states.json")
    seed_states(st, {})
    rc = builder.dispatch({"ticket_id": "SWB-T04", "node": 4, "seat_id": "engineer",
                           "agent_id": "engineer-fresh1"},
                          builder.load_spec(SPEC_PATH), led, st,
                          os.path.join(tmp, "agents.jsonl"), os.path.join(tmp, "inj"))
    assert rc == 0, "无活跃票时派发应放行"
    recs = [r for r in read_ledger(led) if r["type"] == "注入包哈希"]
    assert len(recs) == 1 and len(recs[0]["payload"]["package_hash"]) == 64


def t04_superset_rejected_with_diff_set(tmp: str) -> None:
    """票面判据4 形态：样例票注入面超出 spec 声明面 → exit≠0，回显差异集。"""
    led, st = os.path.join(tmp, "ledger.jsonl"), os.path.join(tmp, "states.json")
    seed_states(st, {})
    rc = builder.dispatch({"ticket_id": "SWB-T05", "node": 4, "seat_id": "engineer",
                           "agent_id": "engineer-fresh2",
                           "requested_items": ["本票票面副本", "上游内容副本", "他票票体副本"]},
                          builder.load_spec(SPEC_PATH), led, st,
                          os.path.join(tmp, "agents.jsonl"), os.path.join(tmp, "inj"))
    assert rc == builder.EXIT_SUPERSET, f"超集请求应 exit=EXIT_SUPERSET，实得 {rc}"
    reports = [r for r in read_ledger(led) if r["payload"].get("event") == "injection_superset_reject"]
    assert len(reports) == 1
    assert reports[0]["payload"]["superset_items"] == ["他票票体副本"], "回显差异集不符"


def t05_agent_id_crosscheck_bidirectional(tmp: str) -> None:
    """§8 互验键双向比对：中文名拒；席位前缀正向不符拒；账本反向映射不符拒。"""
    agents = os.path.join(tmp, "agents.jsonl")
    assert builder.agent_id_crosscheck("工程师一号", "engineer", agents) != []   # 中文名禁
    assert builder.agent_id_crosscheck("qa-x1", "engineer", agents) != []       # 正向前缀不符
    with open(agents, "w", encoding="utf-8") as f:
        f.write(json.dumps({"agent_id": "engineer-a1", "seat_id": "engineer", "ticket_id": "T1"}) + "\n")
    assert builder.agent_id_crosscheck("engineer-a1", "engineer", agents) == []  # 双向一致
    assert builder.agent_id_crosscheck("engineer-a1", "qa", agents) != []       # 反向比对不符
    # 闸面：互验不符→exit≠0 且差异计入 §13 分子口径记录
    led, st = os.path.join(tmp, "led5.jsonl"), os.path.join(tmp, "st5.json")
    seed_states(st, {})
    rc = builder.dispatch({"ticket_id": "SWB-T06", "node": 4, "seat_id": "engineer",
                           "agent_id": "qa-imp1"},
                          builder.load_spec(SPEC_PATH), led, st,
                          os.path.join(tmp, "ag5.jsonl"), os.path.join(tmp, "inj5"))
    assert rc == builder.EXIT_AGENT_MISMATCH
    rej = [r for r in read_ledger(led) if r["payload"].get("event") == "dispatch_rejected_agent_mismatch"]
    assert len(rej) == 1 and "差异率分子" in rej[0]["payload"]["counted_in"]


def t06_purity_construction_assertion(tmp: str) -> None:
    """构造断言：成品命中过程痕迹词族→拒出（表2-3 表注源头即纯款）。"""
    pkg = {"ticket_id": "T", "node": 4, "seat_id": "engineer",
           "items": [{"name": "本票票面副本", "kind": "literal", "path": "x"}]}
    assert builder.purity_assertion(pkg) == []  # 词族零命中（条目名不含禁词时）
    dirty = {"ticket_id": "T", "node": 4, "seat_id": "engineer",
             "items": [{"name": "轮次叙事段落", "kind": "literal", "path": "x"}]}
    assert builder.purity_assertion(dirty) == ["轮次叙事"], "构造断言应命中禁词"


def t07_serial_gate_cli_smoke(tmp: str) -> None:
    """serial-gate 独立 CLI 冒烟：活跃=0 → exit0；活跃≠0 → exit≠0。"""
    led, st = os.path.join(tmp, "led7.jsonl"), os.path.join(tmp, "st7.json")
    seed_states(st, {})
    r1 = subprocess.run([sys.executable, os.path.join(SCRIPTS, "serial-gate.py"),
                         "--ticket", "T-A", "--ledger", led, "--states", st],
                        capture_output=True, text=True)
    assert r1.returncode == 0
    seed_states(st, {"T-BUSY": {"state": 3}})
    r2 = subprocess.run([sys.executable, os.path.join(SCRIPTS, "serial-gate.py"),
                         "--ticket", "T-A", "--ledger", led, "--states", st],
                        capture_output=True, text=True)
    assert r2.returncode != 0
    assert len([r for r in read_ledger(led) if r["type"] == "呈报"]) == 1


def run_self() -> int:
    tests = [t01_spec_eight_rows_signoffs_nonempty,
             t02_serial_gate_active_nonzero_rejects_with_exactly_one_report,
             t03_dispatch_ok_writes_package_hash_record,
             t04_superset_rejected_with_diff_set,
             t05_agent_id_crosscheck_bidirectional,
             t06_purity_construction_assertion,
             t07_serial_gate_cli_smoke]
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
