#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S3 施工测试实体 · 决策包装配（B4：decision-pack.py）。

覆盖：触发源六闭集逐码呈报（§4 V13 L115）；闭集外触发码拒；呈报面含缺陷定级字段（§18⑩·
severity＋severity_confirmed 呈现，不判级）；灰度→全量机械门禁＝票内声明判据比对读数，
不符拒出 full-rollout（表2-2 V13 L97）。argv 面无兄弟件时仅自跑（被 test_dispatch_gate.py 带动）。
运行落盘一律 Temp 重定向，仓内零残留。
"""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.dirname(os.path.dirname(HERE))
SCRIPTS = os.path.join(PACK, "skills", "sop", "scripts")


def load_script(name: str):
    path = os.path.join(SCRIPTS, name)
    spec = importlib.util.spec_from_file_location(name.replace("-", "_").replace(".py", ""), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


dp = load_script("decision-pack.py")


def read_ledger(path: str) -> list[dict]:
    out = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    out.append(json.loads(line))
    return out


def t01_six_trigger_codes_all_reportable(tmp: str) -> None:
    """六闭集逐码实现为呈报触发枚举：逐码出呈报决策包成功＋入账恰一。"""
    led = os.path.join(tmp, "led1.jsonl")
    codes = sorted(dp.TRIGGER_CODES)
    assert len(codes) == 6
    for i, code in enumerate(codes):
        dp.build_report_pack(code, f"TK-{i}", {"detail": "x"}, None, False, led, None)
    recs = [r for r in read_ledger(led) if r["type"] == "呈报"]
    assert len(recs) == 6
    assert sorted(r["payload"]["trigger_source"] for r in recs) == codes


def t02_trigger_outside_closure_rejected(tmp: str) -> None:
    led = os.path.join(tmp, "led2.jsonl")
    try:
        dp.build_report_pack("自造触发码", "TK-X", {}, None, False, led, None)
        raise AssertionError("闭集外触发码未被拒")
    except SystemExit as e:
        assert e.code == dp.EXIT_TRIGGER_NOT_IN_CLOSURE
    assert read_ledger(led) == []  # 闭集外不落入账


def t03_report_pack_contains_grading_fields(tmp: str) -> None:
    """§18⑩：呈报面含缺陷定级字段（定级与定级确认状态呈现；本脚本不判级）。"""
    led, out = os.path.join(tmp, "led3.jsonl"), os.path.join(tmp, "pack3.json")
    pack = dp.build_report_pack("对账差≠0", "TK-G", {"diff": 2}, "P0", False, led, out)
    g = pack["defect_grading"]
    assert g["severity"] == "P0" and g["severity_confirmed"] is False
    assert "QA 双复核＋人类终裁" in g["grading_authority"]
    assert pack["pack_type"] == "呈报"
    assert os.path.exists(out)


def t04_full_rollout_criteria_mismatch_rejected(tmp: str) -> None:
    """票内声明判据 vs 读数不符→拒出 full-rollout＋呈报留痕（机械门禁，不裁量）。"""
    led = os.path.join(tmp, "led4.jsonl")
    crit = [{"criterion": "差异率", "expect": "<=2%"}, {"criterion": "熔断", "expect": "无"}]
    rc = dp.build_full_rollout_pack("TK-R", crit, {"差异率": "3.5%", "熔断": "无"}, led, None)
    assert rc == dp.EXIT_ROLLOUT_CRITERIA_MISMATCH
    rej = [r for r in read_ledger(led) if r["payload"].get("event") == "full_rollout_reject"]
    assert len(rej) == 1 and rej[0]["payload"]["mismatches"][0]["criterion"] == "差异率"


def t05_full_rollout_criteria_match_produces_pack(tmp: str) -> None:
    led, out = os.path.join(tmp, "led5.jsonl"), os.path.join(tmp, "rollout5.json")
    crit = [{"criterion": "差异率", "expect": "<=2%"}, {"criterion": "熔断", "expect": "无"}]
    rc = dp.build_full_rollout_pack("TK-R2", crit, {"差异率": "<=2%", "熔断": "无"}, led, out)
    assert rc == 0
    with open(out, encoding="utf-8") as f:
        pack = json.load(f)
    assert pack["pack_type"] == "full-rollout" and len(pack["pack_hash"]) == 64


def t06_missing_declared_criteria_not_discretionary(tmp: str) -> None:
    """票内声明判据缺席→拒出（不得现场裁量）。"""
    led = os.path.join(tmp, "led6.jsonl")
    rc = dp.build_full_rollout_pack("TK-R3", [], {"差异率": "0%"}, led, None)
    assert rc == dp.EXIT_ROLLOUT_CRITERIA_MISMATCH
    assert len([r for r in read_ledger(led) if r["type"] == "呈报"]) == 1


def t07_cli_smoke_report_and_readings_file(tmp: str) -> None:
    """CLI 冒烟：report 子命令＋判据/读数 JSON 文件形态，落盘重定向 Temp。"""
    led = os.path.join(tmp, "led7.jsonl")
    r1 = subprocess.run([sys.executable, os.path.join(SCRIPTS, "decision-pack.py"), "report",
                         "--trigger", "活性自检失败", "--ticket", "TK-C",
                         "--ledger", led, "--out", os.path.join(tmp, "p7.json")],
                        capture_output=True, text=True)
    assert r1.returncode == 0, r1.stderr
    crit_f, read_f = os.path.join(tmp, "crit.json"), os.path.join(tmp, "read.json")
    with open(crit_f, "w", encoding="utf-8") as f:
        json.dump([{"criterion": "退回率", "expect": "<=30%"}], f)
    with open(read_f, "w", encoding="utf-8") as f:
        json.dump({"退回率": "31%"}, f, ensure_ascii=False)
    r2 = subprocess.run([sys.executable, os.path.join(SCRIPTS, "decision-pack.py"), "full-rollout",
                         "--ticket", "TK-C2", "--criteria", crit_f, "--readings", read_f,
                         "--ledger", led], capture_output=True, text=True)
    assert r2.returncode != 0, "读数与声明判据不符应拒出 full-rollout"


def run_self() -> int:
    tests = [t01_six_trigger_codes_all_reportable, t02_trigger_outside_closure_rejected,
             t03_report_pack_contains_grading_fields, t04_full_rollout_criteria_mismatch_rejected,
             t05_full_rollout_criteria_match_produces_pack, t06_missing_declared_criteria_not_discretionary,
             t07_cli_smoke_report_and_readings_file]
    for t in tests:
        with tempfile.TemporaryDirectory() as tmp:
            t(tmp)
        print(f"PASS {t.__name__}")
    return 0


def main() -> int:
    return run_self()


if __name__ == "__main__":
    sys.exit(main())
