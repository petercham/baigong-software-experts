#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: MC-SOT-1
# spec_file: .collab/research/2026-10-25-专家层与技能层架构决议-执行交接件_v1.md
# spec_anchor: 2. **三守门**：①单真源
# spec_clause_sha256: e00ce57d764932edc0bb8a010046cad977bf9e35d02c5485370e59128b9b1a18
# spec_version: 1.0
# spec_effective: 2026-10-25
# provider: multi-collab
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: MC-SOT-2
# spec_file: .collab/research/2026-10-25-专家层与技能层架构决议-执行交接件_v1.md
# spec_anchor: 2. **三守门**：①单真源
# spec_clause_sha256: e00ce57d764932edc0bb8a010046cad977bf9e35d02c5485370e59128b9b1a18
# spec_version: 1.0
# spec_effective: 2026-10-25
# provider: multi-collab
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: MC-SKILL-LINE
# spec_file: .collab/research/2026-10-25-专家层与技能层架构决议-执行交接件_v1.md
# spec_anchor: ### 2.1 N1 三层拆解案（定稿形态·第四轮三方已认可）
# spec_clause_sha256: 51fccbbc3d42fbb0756eb698ea12f984dd63f558269df84d0ed74600f6aec882
# spec_version: 1.0
# spec_effective: 2026-10-25
# provider: multi-collab
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: MC-SOT-EXEMPT
# spec_file: .collab/decisions/2026-10-25-皮总拍板.md
# spec_anchor: - **① 基线豁免＝转正式豁免，豁免键＝「文本＋出现文件集合」（选项 c）**
# spec_clause_sha256: adb675e9429b2a1bce4d2876241fc50c328b1d6ea80230163f00a8747d47c2f8
# spec_version: 1.0
# spec_effective: 2026-10-26
# provider: multi-collab
# --- /spec-provenance ---
#
# 规范来源（皮总 Q4 令·两问之一）：
#   MC-SOT-1／MC-SOT-2 ＝ 三守门①「单真源」（同一内容只一处全文、MD 只留骨架行、
#     细则只在 skill、互引不双写）＋ 2.1 三层拆解案细则 1（骨架/细则切分线）。
#   MC-SKILL-LINE ＝ 2500 分轨口径（交接件 §二 #4 已决升格：SKILL.md 技能层
#     ≤5000 token 级）。
#   MC-SOT-EXEMPT ＝ 皮总拍板 decisions §九·①（2026-10-26）：基线豁免＝转正式豁免，
#     豁免键＝「行文本＋出现文件集合」；仅当两者皆匹配才豁免，同文本出现在集合外的
#     新文件仍照 BLOCK（不取纯文本键，堵住同文本搬家盲区）。
#   出处：MC-SOT-1／2／MC-SKILL-LINE ＝交接件 §一/§二；MC-SOT-EXEMPT ＝ .collab/decisions
#   裁决条目。二者规范实体均在 .collab（不在 deliverables/ 下），此处如实注明。
#
#   **前缀取 MC- 而非 ADR-（批 5-② 拍定，理由＝机检实测）**：check-provenance 的
#   SPEC_ID_RE 收 ADR-，但 run-gates.sh 的 SPEC_ID_HOME **无 ADR 映射**
#   （只有 OA／OB／MC／PUB），实测 ADR-* 进 per_spec → 读表规则 5 判「解析不到」
#   → **exit 3 门禁自锁（逐笔提交全拦）**；MC- 与 provider＝multi-collab 同族，是
#   唯一与挂载目标（decisions §九·②）相容的前缀。**注**：前缀合规是必要条件不是
#   充分条件——MC- 要真正「条款级」可解析，仍需三条正文落进 multi-collab 规范件
#   （当前为自指式满足，归 W6，见下方「挂载状态」）。
#
# 出口路由（皮总 Q4 令·两问之二）：
#   退出码照 60-gates.md §六闭集：0 通过／1 违规／2 用法错／4 基础设施错。
#   发现行照 run-gates.sh FINDING_RE 一行一封格式输出；严重度一律取自路由表
#   on_severity 已有取值域（BLOCK／WATCH）——基线豁免项转 WATCH，不新造 SEV 词
#   （新造词在挂入 run-gates 后会撞「未知 SEV」exit 4，属自埋雷，故不取）。
#   **挂载状态（批 5-② 甲案已挂·此处如实记态，不夸大不缩小）**：本脚本已挂入
#   run-gates.sh 的 SCRIPTS 清单，清单项＝`ROOT/tools/check-source-of-truth`
#   （甲案＝给清单加「显式前缀 ROOT/ ＝仓根相对路径」的解析语义，判据一字未动；
#   `../../..` 相对段写法实测 exit 4，故不取）。60-gates.md 的 per_spec 已补
#   本件四条 → 一律 advisory：出提示、**不拦提交**（§九·②「先 advisory 取信号」）。
#   **遗留（不本单治·归 W6）**：读表规则 5 要求 spec_id 在 provider 包规范件里
#   解析得到，本件四条现为「id 串出现在 60-gates.md 自身 json 围栏」的**自指式
#   满足**（实测 `grep -rn SOT deliverables/skills/multi-collab/` 在本件加表前零
#   命中）；条款正文仍住 .collab（交接件／decisions），待 W6 把三条正文落进
#   multi-collab 规范件后转真满足。已在 60-gates.md §四 表下同步留痕。
#   前缀若改 ADR-：run-gates 的 SPEC_ID_HOME 无 ADR 映射 → 逐笔提交 exit 3 自锁
#   （实测），故维持 MC-（详见 decisions §九·② 与批 5-② 回报）。
#
# token 口径（MC-SKILL-LINE 用）：script-v1（tools/count_agent_tokens.py 同款实现：
#   CJK 区段正则≈1 token/字、非 CJK≈4 字符/token、ceil 上取整）。
#   **emoji 归属约定＝script-v1 现状：非 CJK 池**（区段正则不含 U+2600–27BF 等
#   W 属性符号，emoji 按 4 字符≈1 token 计）——约定出处＝批 4 W5a 勘察报告 B3.2
#   （.collab/research/2026-10-25-批4-W5a-2500分轨复算与技能层口径勘察报告_v1.md）。
#
# 本件只读：不写任何文件（基线快照由外部程序化生成，见 load_baseline 注释）。
"""W2 真源对账：A 骨架-本体对账（单真源守护）＋ B 技能层线检。

用法：
    python tools/check-source-of-truth.py [--root <仓根>] [--pkg <相对包路径>]

默认包＝deliverables/experts/aigc-video-team/。

检查项：
    A1（MC-SOT-1）agents/ 七席 MD 之间、MD 与 skills/ 之间 ≥12 CJK 连续段行级重合
       ——重合＝第二真源嫌疑。**豁免键＝「行文本＋出现文件集合」**（decisions §九·①）：
       文本匹配且出现文件 ∈ 该文本既定文件集合 → 转 WATCH 并标「｜基线豁免（文本＋
       文件集合）」，不计 BLOCK；文本不在基线、或文本在基线但出现在集合外的新文件
       → 照 BLOCK 并标「｜新命中」（同文本搬家必被抓）。
    A2（MC-SOT-2）agents/ 与 skills/ 内反引号 .md 路径指针可达性——悬空＝BLOCK。
    B （MC-SKILL-LINE）五域 SKILL.md token ≤5000（script-v1/ceil/emoji 非 CJK 池）。

退出码（闭集，见 60-gates.md §六）：0 通过／1 违规／2 用法错／4 基础设施错。
"""

from __future__ import annotations

import argparse
import os
import re
import sys

CJK_RE = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')
MIN_CJK = 12                 # 重合判定阈值：行内 ≥12 个 CJK 字符
SKILL_LINE = 5000            # MC-SKILL-LINE：技能层 ≤5000 token 级
DEFAULT_PKG = 'deliverables/experts/aigc-video-team'

# 基线快照（外置 JSON＝tools/baseline-sot-dup.json·程序化生成以免手抄漂移）：
#   形态＝ items[]：{text＝行文本, files＝该文本既定出现的文件集合}。
#   **豁免键＝「文本＋文件集合」**（皮总拍板 decisions §九·①，规范来源见文件头
#   MC-SOT-EXEMPT 块）——不取纯文本键，以堵住「同文本搬家被误标基线」的盲区。
#   判定：仅当「行文本匹配」且「出现文件 ∈ 该文件集合」才豁免（转 WATCH·不计 BLOCK）；
#   文本不在基线、或出现在集合外的新文件 → 照 BLOCK（标「｜新命中」）。
#   判据强度（MIN_CJK／SKILL_LINE／OA-D6 裁-21 裸基名→WATCH 划界）不因豁免而变。
BASELINE_SNAPSHOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'baseline-sot-dup.json')


def load_baseline() -> dict:
    """读基线快照：返回 {行文本 -> 既定出现文件集合(frozenset)}。

    快照缺失＝无基线（全部按新命中输出，更严不更松）；形态不符或损坏＝exit 4
    （不猜语义，与 60-gates §六「基础设施错」一致）。
    """
    if not os.path.isfile(BASELINE_SNAPSHOT):
        return {}
    import json
    try:
        with open(BASELINE_SNAPSHOT, 'r', encoding='utf-8') as handle:
            data = json.load(handle)
        items = data['items']
        return dict((item['text'], frozenset(item['files'])) for item in items)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        raise SystemExit('infra error: 基线快照损坏或形态不符 %s: %s'
                         % (BASELINE_SNAPSHOT, exc))


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
                    findings.append((rel, i, 'WATCH', 'MC-SOT-2',
                                     '指针裸基名 `%s`（不 BLOCK，按 D6 裁-21 划界）' % target))
                    continue
                cand_root = os.path.normpath(os.path.join(pkg_abs, target))
                cand_dir = os.path.normpath(os.path.join(os.path.dirname(abs_path), target))
                if not (os.path.isfile(cand_root) or os.path.isfile(cand_dir)):
                    findings.append((rel, i, 'BLOCK', 'MC-SOT-2',
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
    # 豁免键＝「行文本＋出现文件集合」：逐「出现处」判定，同一行文本的不同出现处
    # 各自判——集合内的豁免，集合外的（搬家/新增载体）照 BLOCK。
    baseline = load_baseline()
    n_exempt = 0
    index = {}   # 行文本 -> [(rel, 行号)]
    for rel in agents + skills:
        for i, line in big_lines(os.path.join(pkg_abs, rel)):
            index.setdefault(line, []).append((rel, i))
    for line, occ in index.items():
        files = sorted({rel for rel, _ in occ})
        if len(files) > 1 and any(f.startswith('agents/') for f in files):
            allowed = baseline.get(line)
            for rel, i in occ:
                if allowed is not None and rel in allowed:
                    n_exempt += 1
                    findings.append((rel, i, 'WATCH', 'MC-SOT-1',
                                     '≥%d CJK 行级重合（基线结构性模板·共 %d 处：%s）'
                                     '｜基线豁免（文本＋文件集合）'
                                     % (MIN_CJK, len(files), ' + '.join(files))))
                else:
                    if allowed is None:
                        reason = '行文本不在基线'
                    else:
                        reason = '行文本在基线但出现文件不在既定集合（搬家／新增载体）'
                    findings.append((rel, i, 'BLOCK', 'MC-SOT-1',
                                     '≥%d CJK 行级重合（第二真源嫌疑·共 %d 处：%s）'
                                     '｜新命中（豁免键未命中·%s）'
                                     % (MIN_CJK, len(files), ' + '.join(files), reason)))

    # --- A2 ⛓/反引号指针可达性 ---
    findings.extend(check_pointers(pkg_abs, agents + skills))

    # --- B 技能层线检：SKILL.md ≤5000（script-v1/ceil/emoji 非 CJK 池） ---
    for rel in skills:
        if norm(rel).endswith('SKILL.md'):
            with open(os.path.join(pkg_abs, rel), 'r', encoding='utf-8') as handle:
                t = tokens(handle.read())
            if t > SKILL_LINE:
                findings.append((rel, 1, 'BLOCK', 'MC-SKILL-LINE',
                                 'SKILL.md token %d > %d（script-v1/ceil/emoji 非 CJK 池）'
                                 % (t, SKILL_LINE)))

    # --- 输出一行一封（run-gates FINDING_RE 兼容）＋计数行 ---
    violations = 0
    for rel, i, sev, spec, msg in sorted(findings):
        print('%s:%d: %s %s %s' % (rel, i, sev, spec, msg))
        if sev == 'BLOCK':
            violations += 1
    n_watch_ptr = sum(1 for f in findings if f[2] == 'WATCH' and f[3] != 'MC-SOT-1')
    exit_code = 1 if violations else 0
    print('check-source-of-truth: 文件 %d（agents %d＋skills %d）｜BLOCK %d（新命中 %d）'
          '｜基线豁免 %d（WATCH·键＝文本＋文件集合）｜指针 WATCH %d｜exit %d'
          % (len(agents) + len(skills), len(agents), len(skills),
             violations, violations, n_exempt, n_watch_ptr, exit_code))
    return exit_code


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按 4（60-gates §六）
        sys.stderr.write('infra error: %s\n' % exc)
        sys.exit(4)
