#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FUXI-S1 QA 对抗复探探针（fresh eyes·证伪导向）。

纪律：全部坏样本在 %TEMP% 副本树内生成与销毁，仓内零写入。
手段＝整树复制 deliverables/skills/fuxi-skill/ 到临时目录，施加突变后
以该副本为基面跑 assert-tool.py（工具路径自文件位置静态定位，副本自洽）。
每探针期望＝工具咬（exit 1 且指定断言 FAIL）；工具放过＝探针红。
"""
import os
import shutil
import subprocess
import sys
import tempfile

REPO = r"D:\multi-agent-collab-devkits"
SKILL = os.path.join(REPO, "deliverables", "skills", "fuxi-skill")
TOOL = os.path.join("gates", "assert-tool.py")

results = []


def make_tree(with_board=False):
    tmp = tempfile.mkdtemp(prefix="fuxi-s1-probe-")
    dst = os.path.join(tmp, "deliverables", "skills", "fuxi-skill")
    shutil.copytree(SKILL, dst)
    if with_board:
        bdir = os.path.join(tmp, ".collab", "board")
        os.makedirs(bdir)
        shutil.copy(os.path.join(REPO, ".collab", "board", "board-2026-10-30.md"), bdir)
    return tmp, dst


def run_tool(root):
    p = subprocess.run([sys.executable, os.path.join(root, "deliverables", "skills", "fuxi-skill", "gates", "assert-tool.py")],
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def probe(name, mutate, expect_exit, expect_fail_ids, expect_pass_ids=()):
    tmp, dst = make_tree(with_board=True)
    try:
        mutate(dst)
        root = tmp
        code, out = run_tool(root)
        ok = code == expect_exit
        lines = {ln.split()[0]: ln for ln in out.splitlines() if ln.startswith(("ST-", "BW-", "FC-", "GS-"))}
        for fid in expect_fail_ids:
            if not lines.get(fid, "").startswith(fid + " FAIL"):
                ok = False
                out += "\n[probe %s] 期望 %s FAIL，实际读数行：%r" % (name, fid, lines.get(fid))
        for fid in expect_pass_ids:
            if not lines.get(fid, "").startswith(fid + " PASS"):
                ok = False
                out += "\n[probe %s] 期望 %s PASS，实际读数行：%r" % (name, fid, lines.get(fid))
        if code != expect_exit:
            out += "\n[probe %s] 期望 exit=%d 实际 exit=%d" % (name, expect_exit, code)
        results.append((name, ok, code))
        print(("BITE-OK " if ok else "MISSED  ") + name + " exit=%d" % code)
        if not ok:
            print(out[-800:])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _patch(path, old, new):
    with open(path, "r", encoding="utf-8") as f:
        t = f.read()
    assert old in t, "patch anchor missing in %s" % path
    with open(path, "w", encoding="utf-8") as f:
        f.write(t.replace(old, new, 1))


# --- 探针 1：契约文件外字段注入（声明侧）→ FC-2 应咬 ---
def m1(dst):
    _patch(os.path.join(dst, "contracts", "artifact-contract.md"),
           '{"字段注册": ["产物id"', '{"字段注册": ["自造字段X", "产物id"')

probe("P1_声明侧外字段注入", m1, 1, ("FC-2",))


# --- 探针 2：实例记录外字段注入（EG-5 示例行）→ FC-2 应咬 ---
def m2(dst):
    _patch(os.path.join(dst, "contracts", "evidence-grading.md"),
           '"abstain_tier": "有限定"}', '"abstain_tier": "有限定", "自造字段Y": "x"}')

probe("P2_实例外字段注入", m2, 1, ("FC-2",))


# --- 探针 3：evidence_grade 声明值闭集外值 → FC-1/FC-2 应咬 ---
def m3(dst):
    _patch(os.path.join(dst, "contracts", "artifact-contract.md"),
           '"evidence_grade": ["人工验证", "机械断言", "LLM 判定"]',
           '"evidence_grade": ["人工验证", "机械断言", "LLM 判定", "直觉认定"]')

probe("P3_evidence_grade闭集外值", m3, 1, ("FC-1", "FC-2"))


# --- 探针 4：calibration_state 声明与模拟 κ 不一致（κ 弱却声明校准态）→ fail-closed 应咬 ---
def m4(dst):
    _patch(os.path.join(dst, "gates", "assert-tool.py"),
           'cases.append(("GS4_bite_inconsistent", calibration_consistent("校准态", weak_kappa), False))',
           'cases.append(("GS4_bite_inconsistent", calibration_consistent("校准态", weak_kappa), True))')
    # 翻转期望值：若判据真咬（返回 False≠True）→ selftest 应红 exit 1

# （P4 突变只作用于 selftest 用例区，selftest 模式单跑见下方 P4b）


# selftest 期望翻转探针（P4 实跑 selftest 模式）
tmp, dst = make_tree()
try:
    m4(dst)
    p = subprocess.run([sys.executable, os.path.join(dst, "gates", "assert-tool.py"), "selftest"],
                       capture_output=True, text=True)
    ok = p.returncode == 1 and "GS4_bite_inconsistent" in (p.stdout + p.stderr)
    results.append(("P4b_selftest期望翻转应红", ok, p.returncode))
    print(("BITE-OK " if ok else "MISSED  ") + "P4b_selftest期望翻转应红 exit=%d" % p.returncode)
    if not ok:
        print((p.stdout + p.stderr)[-500:])
finally:
    shutil.rmtree(tmp, ignore_errors=True)


# --- 探针 5：calibration_state 值注册缺声明（缺「待校准」）→ FC-1/FC-2 应咬（fail-closed） ---
def m5(dst):
    _patch(os.path.join(dst, "contracts", "artifact-contract.md"),
           '"calibration_state": ["校准态", "待校准"]', '"calibration_state": ["校准态"]')

probe("P5_calibration_state缺值声明", m5, 1, ("FC-1", "FC-2"))


# --- 探针 6：FM 条目处置列写「视情况」→ FC-2（纪律子检查）应咬 ---
def m6(dst):
    _patch(os.path.join(dst, "contracts", "failure-modes.md"),
           "| FM-S-03 | 共享 | 成本失控（标注/蒸算开销越出预注册预算） | 开销台账越线读数 | 阻断当前批次，转人工闸复核预算 |",
           "| FM-S-03 | 共享 | 成本失控（标注/蒸算开销越出预注册预算） | 开销台账越线读数 | 视情况处理 |")

probe("P6_FM处置列视情况注入", m6, 1, ("FC-2",))


# --- 探针 7：FM 条目缺基线（删 FM-M-03 行）→ 数量基线应咬 ---
def m7(dst):
    _patch(os.path.join(dst, "contracts", "failure-modes.md"),
           "| FM-M-03 | method | 跨技能混淆（与近邻卡不可区分） | decoy 对照命中率 fail | 阻断：修订 A2 触发段重测 decoy，未过不晋级 |\n", "")

probe("P7_FM条目低于数量基线", m7, 1, ("FC-2",))


# --- 探针 8：契约节改名（EG-6 改名）→ ST-2 节闭集应咬 ---
def m8(dst):
    _patch(os.path.join(dst, "contracts", "evidence-grading.md"),
           "## EG-6 语料门槛登记", "## EG-6 语料库登记")

probe("P8_EG-6节改名", m8, 1, ("ST-2",))


# --- 探针 9：rejected/ 批次缺 coverage-audit＋条目三问缺位 → ST-5 应咬 ---
def m9(dst):
    bdir = os.path.join(dst, "rejected", "2026-11-01-b01")
    os.makedirs(bdir)
    with open(os.path.join(bdir, "c-9001.md"), "w", encoding="utf-8") as f:
        f.write('# 淘汰条目\n\n```json\n{"candidate_id": "c-9001", "所属轨": "person", '
                '"淘汰维度": "排他性", "淘汰理由": "无排他性证据", "证据等级": "跨文本推断"}\n```\n')
    # 缺 coverage-audit.md ＋ 条目缺 control_arm/leakage_check 三问 → 双咬

probe("P9_ST5缺审计件＋条目三问缺位", m9, 1, ("ST-5",))


# --- 探针 10：coverage-audit 三问缺一 → ST-5 应咬 ---
def m10(dst):
    bdir = os.path.join(dst, "rejected", "2026-11-01-b02")
    os.makedirs(bdir)
    with open(os.path.join(bdir, "coverage-audit.md"), "w", encoding="utf-8") as f:
        f.write('# coverage-audit\n\n```json\n{"哪些留下": "8 条", "哪些扔了": "5 条"}\n```\n')

probe("P10_coverage-audit缺第三问", m10, 1, ("ST-5",))


# --- 探针 11：看板件删性质声明行 → FC-4 应咬 ---
def m11(dst):
    root = os.path.dirname(os.path.dirname(os.path.dirname(dst)))
    _patch(os.path.join(root, ".collab", "board", "board-2026-10-30.md"),
           "性质＝记录件·人工触发填写·非控制器", "性质＝记录件")

probe("P11_看板缺性质声明行", m11, 1, ("FC-4",))


# --- 探针 12：看板缺三栏之一 → FC-4 应咬 ---
def m12(dst):
    root = os.path.dirname(os.path.dirname(os.path.dirname(dst)))
    _patch(os.path.join(root, ".collab", "board", "board-2026-10-30.md"),
           "## 人工闸结论", "## 人工结论")

probe("P12_看板栏名越闭集", m12, 1, ("FC-4",))


# --- 探针 13：状态词表私扩「已核」等纯函数直调取证 ---
import importlib.util
spec = importlib.util.spec_from_file_location("assert_tool_probe", os.path.join(SKILL, "gates", "assert-tool.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
checks = []
checks.append(("P13a_词表越界已核", mod.state_vocab_closed_ok(("已核",), mod.BOARD_COLUMNS) is False))
checks.append(("P13b_κ缺失仍校准态", mod.calibration_consistent("校准态", None) is False))
checks.append(("P13c_κ弱仍校准态", mod.calibration_consistent("校准态", {"点值": 0.65, "区间下界": 0.55}) is False))
checks.append(("P13d_三问缺对照臂", mod.three_question_ok({"证据等级": "原文可证实", "evidence_grade": "机械断言", "leakage_check": "未检"}) is False))
for name, ok in checks:
    results.append((name, ok, None))
    print(("BITE-OK " if ok else "MISSED  ") + name)


# --- 探针 14：实例记录取值越闭集（证据等级示例行取值改非法值）→ 工具是否实咬？（取证探针，允许放过＝记发现） ---
def m14(dst):
    _patch(os.path.join(dst, "contracts", "evidence-grading.md"),
           '"证据等级": "跨文本推断"', '"证据等级": "铁证如山"')

tmp, dst = make_tree(with_board=True)
try:
    m14(dst)
    code, out = run_tool(tmp)
    fc2 = [ln for ln in out.splitlines() if ln.startswith("FC-2")]
    print("FORENSIC P14_实例取值越闭集: exit=%d %s" % (code, fc2))
    results.append(("P14_实例取值越闭集实咬取证(期望咬)", code == 1, code))
finally:
    shutil.rmtree(tmp, ignore_errors=True)


print("\n==== 汇总 ====")
missed = [n for n, ok, _ in results if not ok]
print("探针 %d／咬中 %d／放过 %d" % (len(results), len(results) - len(missed), len(missed)))
for n in missed:
    print("MISSED:", n)
