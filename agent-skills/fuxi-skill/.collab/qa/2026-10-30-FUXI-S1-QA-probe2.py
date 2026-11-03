#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FUXI-S1 QA 对抗复探第二轮（补齐第一轮盲区取证）。临时副本树内作业，仓内零写入。"""
import os
import shutil
import subprocess
import sys
import tempfile

REPO = r"D:\multi-agent-collab-devkits"
SKILL = os.path.join(REPO, "deliverables", "skills", "fuxi-skill")
results = []


def make_tree(with_board=True):
    tmp = tempfile.mkdtemp(prefix="fuxi-s1-probe2-")
    dst = os.path.join(tmp, "deliverables", "skills", "fuxi-skill")
    shutil.copytree(SKILL, dst)
    if with_board:
        bdir = os.path.join(tmp, ".collab", "board")
        os.makedirs(bdir)
        shutil.copy(os.path.join(REPO, ".collab", "board", "board-2026-10-30.md"), bdir)
    return tmp, dst


def run_tool(root):
    p = subprocess.run([sys.executable, os.path.join(root, "deliverables", "skills",
                       "fuxi-skill", "gates", "assert-tool.py")], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def probe(name, mutate, expect_exit, expect_ids_state):
    """expect_ids_state: {断言id: "PASS"|"FAIL"}"""
    tmp, dst = make_tree()
    try:
        mutate(dst)
        code, out = run_tool(tmp)
        lines = {ln.split()[0]: ln for ln in out.splitlines() if ln.startswith(("ST-", "BW-", "FC-", "GS-"))}
        ok = code == expect_exit
        notes = []
        for fid, want in expect_ids_state.items():
            got = lines.get(fid, "<absent>")
            if not got.startswith(fid + " " + want):
                ok = False
                notes.append("期望 %s %s 实际 %r" % (fid, want, got))
        if code != expect_exit:
            notes.append("期望 exit=%d 实际 exit=%d" % (expect_exit, code))
        results.append((name, ok))
        print(("BITE-OK " if ok else "MISSED  ") + name + " exit=%d" % code)
        for n in notes:
            print("   " + n)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def patch_file(path, old, new, count=1):
    with open(path, "r", encoding="utf-8") as f:
        t = f.read()
    assert old in t, "anchor missing: %s" % path
    with open(path, "w", encoding="utf-8") as f:
        f.write(t.replace(old, new, count))


# P15：看板实例正文私扩状态词表外 token「彻底完成」→ 规格 §六 J4 要求「状态 token∈词表闭集」扫描，是否实咬？
def m15(dst):
    root = os.path.dirname(os.path.dirname(os.path.dirname(dst)))
    patch_file(os.path.join(root, ".collab", "board", "board-2026-10-30.md"),
               "## 人工闸结论\n",
               "## 人工闸结论\n\n- 主理人裁定：S1 产物面全部 `彻底完成`，状态迁移到 `已核`。\n")


probe("P15_看板实例状态token越词表(J4口径)", m15, 1, {"FC-4": "FAIL"})


# P16：calibration_state 声明值在 EG-5 与 AC-2 两点位同时缺「待校准」→ 值 diff 应咬（确认工具能力，非并集盲区外）
def m16(dst):
    patch_file(os.path.join(dst, "contracts", "artifact-contract.md"),
               '"calibration_state": ["校准态", "待校准"]', '"calibration_state": ["校准态"]')
    patch_file(os.path.join(dst, "contracts", "evidence-grading.md"),
               '"calibration_state": ["校准态", "待校准"]', '"calibration_state": ["校准态"]')


probe("P16_两点位同时缺值声明应咬", m16, 1, {"FC-1": "FAIL", "FC-2": "FAIL"})


# P17：ST-5 正样本（临时批次，三问齐备）→ 应 PASS 批次1（跑通后随副本销毁，不落仓）
def m17(dst):
    bdir = os.path.join(dst, "rejected", "2026-10-30-b01")
    os.makedirs(bdir)
    with open(os.path.join(bdir, "c-0107.md"), "w", encoding="utf-8") as f:
        f.write('# 淘汰条目 c-0107\n\n```json\n'
                '{"candidate_id": "c-0107", "所属轨": "person", "淘汰维度": "排他性", '
                '"淘汰理由": "相邻三例均可由更简假设替代", "证据等级": "跨文本推断", '
                '"control_arm": "无臂", "leakage_check": "未检"}\n```\n')
    with open(os.path.join(bdir, "coverage-audit.md"), "w", encoding="utf-8") as f:
        f.write('# coverage-audit 2026-10-30-b01\n\n```json\n'
                '{"哪些留下": "8 条（统计口径：三判据全过；样本量 13；一致性系数见 κ 报告）", '
                '"哪些扔了": "5 条（统计口径：任一判据 fail；样本量 13；一致性系数见 κ 报告）", '
                '"为什么": "排他性与预测力不足", "一手占比": "62%（统计口径：一手源条数/总条数；样本量 13；一致性系数见 κ 报告）"}\n```\n')


probe("P17_ST5正样本临时批次跑通", m17, 0, {"ST-5": "PASS"})


# P18：相邻板日期间隔 >14 天 → FC-4 应咬（周期兜底隔离线）
def m18(dst):
    root = os.path.dirname(os.path.dirname(os.path.dirname(dst)))
    bdir = os.path.join(root, ".collab", "board")
    src = os.path.join(bdir, "board-2026-10-30.md")
    with open(src, "r", encoding="utf-8") as f:
        t = f.read()
    with open(os.path.join(bdir, "board-2026-11-25.md"), "w", encoding="utf-8") as f:
        f.write(t)


probe("P18_相邻板间隔超限", m18, 1, {"FC-4": "FAIL"})


# P19：AC-5 契约正文私扩状态词「已核」入词表声明句 → FC-4 词表侧是否咬（词表本体在工具侧，契约文本侧扫描？）
def m19(dst):
    patch_file(os.path.join(dst, "contracts", "artifact-contract.md"),
               "基线闭集（与 FC-4 注册位逐字全等，不扩）：`needs_review`／`active`／`归档区`／`待校准`／`未验`。",
               "基线闭集（与 FC-4 注册位逐字全等，不扩）：`needs_review`／`active`／`归档区`／`待校准`／`未验`／`已核`。")


probe("P19_AC-5正文私扩已核(J4/FC-4口径)", m19, 1, {"FC-4": "FAIL"})


# P20：FM 条目的轨别与所在节不匹配（FM-P-01 轨别改 method）→ FC-2 纪律子检查应咬
def m20(dst):
    patch_file(os.path.join(dst, "contracts", "failure-modes.md"),
               "| FM-P-01 | person | 幻觉填充", "| FM-P-01 | method | 幻觉填充")


probe("P20_FM轨别与前缀不匹配", m20, 1, {"FC-2": "FAIL"})


# P21：契约三件缺件之一（删 failure-modes.md）→ ST-2/FC-2 应咬
def m21(dst):
    os.remove(os.path.join(dst, "contracts", "failure-modes.md"))


probe("P21_契约缺件", m21, 1, {"ST-2": "FAIL", "FC-2": "FAIL"})


# P22：FC-3 实例记录 source_id 有而位置空 → FC-3 应咬
def m22(dst):
    patch_file(os.path.join(dst, "contracts", "evidence-grading.md"),
               '"source_id": "src-03", "位置": "第三章·第二节"', '"source_id": "src-03", "位置": ""')


probe("P22_FC3成对字段单侧空", m22, 1, {"FC-3": "FAIL"})


# P23：工具侧注册表私扩一字段（契约侧无声明）→ 「注册表未声明缺失」应咬（防私扩双向闭合）
def m23(dst):
    patch_file(os.path.join(dst, "gates", "assert-tool.py"),
               '    "编号", "轨别", "触发", "检出", "处置",', '    "编号", "轨别", "触发", "检出", "处置", "自造注册字段Z",')


probe("P23_注册表私扩应咬", m23, 1, {"FC-2": "FAIL"})


# P24：PENDING_STAGE 项被误计为 fail 的对照——确认 ST-3/ST-4/BW-3/BW-4 PENDING 不拉码（正例基线）
def m24(dst):
    pass


probe("P24_基线连跑PENDING不拉码", m24, 0, {"ST-3": "PENDING_STAGE", "GS-4": "PENDING_STAGE", "FC-4": "PASS", "ST-5": "PASS"})

print("\n==== 汇总 ====")
missed = [n for n, ok in results if not ok]
print("探针 %d／符合预期 %d／放过(盲区) %d" % (len(results), len(results) - len(missed), len(missed)))
for n in missed:
    print("BLIND/MISS:", n)
