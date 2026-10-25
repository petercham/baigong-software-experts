#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: N1-SOT-1
# spec_file: .collab/research/2026-10-25-专家层与技能层架构决议-执行交接件_v1.md
# spec_anchor: 2. **三守门**：①单真源
# spec_clause_sha256: e00ce57d764932edc0bb8a010046cad977bf9e35d02c5485370e59128b9b1a18
# spec_version: 1
# spec_effective: 2026-10-25
# provider: multi-collab
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: N1-SOT-2
# spec_file: .collab/research/2026-10-25-专家层与技能层架构决议-执行交接件_v1.md
# spec_anchor: 2. **三守门**：①单真源
# spec_clause_sha256: e00ce57d764932edc0bb8a010046cad977bf9e35d02c5485370e59128b9b1a18
# spec_version: 1
# spec_effective: 2026-10-25
# provider: multi-collab
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: N1-SKILL-LINE
# spec_file: .collab/research/2026-10-25-专家层与技能层架构决议-执行交接件_v1.md
# spec_anchor: ### 2.1 N1 三层拆解案（定稿形态·第四轮三方已认可）
# spec_clause_sha256: 51fccbbc3d42fbb0756eb698ea12f984dd63f558269df84d0ed74600f6aec882
# spec_version: 1
# spec_effective: 2026-10-25
# provider: multi-collab
# --- /spec-provenance ---
#
# 规范来源（皮总 Q4 令·两问之一）：
#   N1-SOT-1／N1-SOT-2 ＝ 三守门①「单真源」（同一内容只一处全文、MD 只留骨架行、
#     细则只在 skill、互引不双写）＋ 2.1 三层拆解案细则 1（骨架/细则切分线）。
#   N1-SKILL-LINE ＝ 2500 分轨口径（交接件 §二 #4 已决升格：SKILL.md 技能层
#     ≤5000 token 级）。
#   出处均＝交接件 §一/§二（provider 填 multi-collab 系因 check-provenance 要求
#   provider＝deliverables/ 下现存包名；本件规范实体在 .collab 交接件，如实注明）。
#
# 出口路由（皮总 Q4 令·两问之二）：
#   退出码照 60-gates.md §六闭集：0 通过／1 违规／2 用法错／4 基础设施错。
#   发现行照 run-gates.sh FINDING_RE 一行一封格式输出。
#   **路由缺口如实报告（不自造路由）**：本脚本未挂 run-gates.sh 的 SCRIPTS 清单，
#   且 60-gates.md 路由表 per_spec 无 N1-* 条目——若未来挂入，按读表规则 2 走
#   on_severity 默认（BLOCK→block／WATCH→advisory）；§四 配套规则 1 要求 block
#   必须有条款级依据，N1-* 的 per_spec 配置候主理人/皮总治理决定，本件不预设。
#
# token 口径（N1-SKILL-LINE 用）：script-v1（tools/count_agent_tokens.py 同款实现：
#   CJK 区段正则≈1 token/字、非 CJK≈4 字符/token、ceil 上取整）。
#   **emoji 归属约定＝script-v1 现状：非 CJK 池**（区段正则不含 U+2600–27BF 等
#   W 属性符号，emoji 按 4 字符≈1 token 计）——约定出处＝批 4 W5a 勘察报告 B3.2
#   （.collab/research/2026-10-25-批4-W5a-2500分轨复算与技能层口径勘察报告_v1.md）。
#
# 本件只读：不写任何文件。
"""W2 真源对账：A 骨架-本体对账（单真源守护）＋ B 技能层线检。

用法：
    python tools/check-source-of-truth.py [--root <仓根>] [--pkg <相对包路径>]

默认包＝deliverables/profiles/aigc-video-team/。

检查项：
    A1（N1-SOT-1）agents/ 七席 MD 之间、MD 与 skills/ 之间 ≥12 CJK 连续段行级重合
       ——重合＝第二真源嫌疑，BLOCK 候选；首跑基线既有项以「｜基线既有」标注区分
       （标注不改 SEV 不改退出码——判据不放宽，红就是红）。
    A2（N1-SOT-2）agents/ 与 skills/ 内反引号 .md 路径指针可达性——悬空＝BLOCK。
    B （N1-SKILL-LINE）五域 SKILL.md token ≤5000（script-v1/ceil/emoji 非 CJK 池）。

退出码（闭集，见 60-gates.md §六）：0 通过／1 违规／2 用法错／4 基础设施错。
"""

from __future__ import annotations

import argparse
import os
import re
import sys

CJK_RE = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')
MIN_CJK = 12                 # 重合判定阈值：行内 ≥12 个 CJK 字符
SKILL_LINE = 5000            # N1-SKILL-LINE：技能层 ≤5000 token 级
DEFAULT_PKG = 'deliverables/profiles/aigc-video-team'

# 首跑基线快照（外置 JSON＝tools/baseline-sot-dup.json·程序化生成以免手抄漂移）：
# 首跑（d23a374＋T2/T3 落地态）实测的七席 MD 结构性模板重合行（三栏/权限/⛓ 节
# 骨架、共用指针行）。脚本仍按 BLOCK 候选输出，仅加「｜基线既有」标注区分——
# 标注不改 SEV 不改退出码（判据不放宽）；转正式豁免属治理决定，本件不自行放宽。
BASELINE_SNAPSHOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'baseline-sot-dup.json')

def load_baseline() -> frozenset:
    if not os.path.isfile(BASELINE_SNAPSHOT):
        return frozenset()   # 快照缺失＝全部按新命中输出（更严不更松）
    import json
    try:
        with open(BASELINE_SNAPSHOT, 'r', encoding='utf-8') as handle:
            return frozenset(json.load(handle)['lines'])
    except (OSError, ValueError, KeyError) as exc:
        raise SystemExit('infra error: 基线快照损坏 %s: %s' % (BASELINE_SNAPSHOT, exc))


def tokens(text: str) -> int:
    """script-v1 口径：CJK≈1 token/字、非 CJK≈4 字符/token、ceil；emoji＝非 CJK 池。"""
    cjk = len(CJK_RE.findall(text))
    return cjk + -(-(len(text) - cjk) // 4)


def norm(p: str) -> str:
    return p.replace(os.sep, '/')


def collect_md(pkg_abs: str):
    """返回包内 md 相对路径列表（统一正斜杠），分 agents/ 与 skills/ 两组。"""
    agents, skills = [], []
    for root, dirs, files in os.walk(pkg_abs):
        dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__')]
        for f in sorted(files):
            if not f.endswith('.md'):
                continue
            rel = norm(os.path.relpath(os.path.join(root, f), pkg_abs))
            (agents if rel.startswith('agents/') else
             skills if rel.startswith('skills/') else []).append(rel)
    return sorted(agents), sorted(skills)


def big_lines(path_abs: str):
    """行内 ≥12 CJK 的行：返回 [(行号, 规范化行文本)]。"""
    out = []
    try:
        with open(path_abs, 'r', encoding='utf-8') as handle:
            for i, line in enumerate(handle, 1):
                stripped = line.strip()
                if len(CJK_RE.findall(stripped)) >= MIN_CJK:
                    out.append((i, stripped))
    except (OSError, UnicodeDecodeError) as exc:
        raise SystemExit('infra error: 读不到 %s: %s' % (path_abs, exc))
    return out


POINTER_RE = re.compile(r'`([A-Za-z0-9][A-Za-z0-9./_-]*\.md)`')


def check_pointers(pkg_abs: str, rel_files):
    """A2：反引号 .md 路径可达性。含 / 的按「相对包根」与「相对所在目录」双探；
    裸基名（不含 /）＝WATCH（OA-D6 裁-21 同款划界：裸基名不 BLOCK）。"""
    findings = []
    for rel in rel_files:
        abs_path = os.path.join(pkg_abs, rel)
        try:
            with open(abs_path, 'r', encoding='utf-8') as handle:
                body = handle.read()
        except (OSError, UnicodeDecodeError) as exc:
            raise SystemExit('infra error: 读不到 %s: %s' % (abs_path, exc))
        for i, line in enumerate(body.splitlines(), 1):
            for m in POINTER_RE.finditer(line):
                target = m.group(1)
                if target.startswith('http'):
                    continue
                if '/' not in target:
                    findings.append((rel, i, 'WATCH', 'N1-SOT-2',
                                     '指针裸基名 `%s`（不 BLOCK，按 D6 裁-21 划界）' % target))
                    continue
                cand_root = os.path.normpath(os.path.join(pkg_abs, target))
                cand_dir = os.path.normpath(os.path.join(os.path.dirname(abs_path), target))
                if not (os.path.isfile(cand_root) or os.path.isfile(cand_dir)):
                    findings.append((rel, i, 'BLOCK', 'N1-SOT-2',
                                     '指针悬空 `%s` → 包根与所在目录双探均不存在' % target))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description='W2 真源对账（骨架-本体＋技能层线检）')
    parser.add_argument('--root', default='', help='仓根（默认自脚本位置向上找 deliverables/）')
    parser.add_argument('--pkg', default=DEFAULT_PKG, help='被测专家包（相对仓根）')
    args = parser.parse_args()

    # 定位仓根
    root = args.root
    if not root:
        cur = os.path.dirname(os.path.abspath(__file__))
        while True:
            if os.path.isdir(os.path.join(cur, 'deliverables')):
                root = cur
                break
            parent = os.path.dirname(cur)
            if parent == cur:
                sys.stderr.write('infra error: 未能定位仓根；请用 --root 指定\n')
                return 4
            cur = parent
    pkg_abs = os.path.join(root, args.pkg)
    if not os.path.isdir(pkg_abs):
        sys.stderr.write('usage error: 包目录不存在：%s\n' % args.pkg)
        return 2

    agents, skills = collect_md(pkg_abs)
    if not agents:
        sys.stderr.write('usage error: %s 下无 agents/*.md\n' % args.pkg)
        return 2

    findings = []

    # --- A1 骨架-本体对账：≥12 CJK 行级重合（scope＝至少一侧为 agents/） ---
    baseline = load_baseline()
    index = {}   # 行文本 -> [(rel, 行号)]
    for rel in agents + skills:
        for i, line in big_lines(os.path.join(pkg_abs, rel)):
            index.setdefault(line, []).append((rel, i))
    for line, occ in index.items():
        files = sorted({rel for rel, _ in occ})
        if len(files) > 1 and any(f.startswith('agents/') for f in files):
            tag = '｜基线既有' if line in baseline else ''
            for rel, i in occ:
                findings.append((rel, i, 'BLOCK', 'N1-SOT-1',
                                 '≥%d CJK 行级重合（第二真源嫌疑·共 %d 处：%s）%s'
                                 % (MIN_CJK, len(files), ' + '.join(files), tag)))

    # --- A2 ⛓/反引号指针可达性 ---
    findings.extend(check_pointers(pkg_abs, agents + skills))

    # --- B 技能层线检：SKILL.md ≤5000（script-v1/ceil/emoji 非 CJK 池） ---
    for rel in skills:
        if norm(rel).endswith('SKILL.md'):
            with open(os.path.join(pkg_abs, rel), 'r', encoding='utf-8') as handle:
                t = tokens(handle.read())
            if t > SKILL_LINE:
                findings.append((rel, 1, 'BLOCK', 'N1-SKILL-LINE',
                                 'SKILL.md token %d > %d（script-v1/ceil/emoji 非 CJK 池）'
                                 % (t, SKILL_LINE)))

    # --- 输出一行一封（run-gates FINDING_RE 兼容）＋计数行 ---
    violations = 0
    for rel, i, sev, spec, msg in sorted(findings):
        print('%s:%d: %s %s %s' % (rel, i, sev, spec, msg))
        if sev == 'BLOCK':
            violations += 1
    n_watch = sum(1 for f in findings if f[2] == 'WATCH')
    print('check-source-of-truth: 文件 %d（agents %d＋skills %d）｜BLOCK 候选 %d｜WATCH %d'
          % (len(agents) + len(skills), len(agents), len(skills),
             sum(1 for f in findings if f[2] == 'BLOCK'), n_watch))
    return 1 if violations else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按 4（60-gates §六）
        sys.stderr.write('infra error: %s\n' % exc)
        sys.exit(4)
