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
# 写动作边界（T2 三仓接线批更新）：默认只读、不写任何文件；唯一例外＝显式
#   `--regen-baseline` 开关（程序化重生成基线快照，禁手抄的机械化实现）。
#   不显式带开关时行为与旧版一致（只读）。
"""W2 真源对账：A 骨架-本体对账（单真源守护）＋ B 技能层线检。

T2 三仓口径（拆仓执行批·拍板六⑥）：
    默认＝**双根对账**（dual）：
      根① bundle 根＝`--pkg`（默认 ../multi-agent-collab-experts/workbuddy/baigong-video-team，
        experts 仓 video bundle·skills/ 已出池后其 agents/ 为唯一成员）；
      根② 技能真源根＝`--skills-root`（默认 ../multi-agent-collab-skills/skills，
        skills 仓五域·含 references/）。
      agents（根①的 agents/ 子树）vs skills（根① skills/ 子树＋根②全部 .md）
      的 A1 重合检测**跨仓跑**；A2 指针解析加「技能真源根」探针（见 check_pointers）。
    单根口径（single）＝旧行为：只扫 `--pkg` 一个根（包内自包含）。
      软开 bundle（devkits 仓 workbuddy/baigong-software-team·拍板五①自包含豁免）
      用第二调项：`--mode single --pkg workbuddy/baigong-software-team --tag softdev`。

    **豁免键 files 维度＝跨仓两段式路径口径（T2 定·稳定可机检）**：
      文件标识＝`<roottag>:<root 内相对路径（正斜杠）>`；
      roottag 闭集＝{experts（video bundle 根）, skills（技能真源根）, softdev（软开
      bundle 单根调项·--tag 可覆盖缺省 pkg）}。
      例：`experts:agents/aigc-director.md` ＋ `skills:aigc-video-content/SKILL.md`。
      豁免键仍＝「行文本＋出现文件集合」（MC-SOT-EXEMPT 一字未动），只是集合元素
      换成本口径的两段式标识——跨仓搬家（同文本从 experts 挪进 skills 仓新文件）
      照样被「集合外新文件→BLOCK」条款咬住。

用法：
    python tools/check-source-of-truth.py [--root <devkits 仓根>]
        [--mode dual|single] [--pkg <相对仓根的包路径>] [--skills-root <相对仓根的技能真源根>]
        [--tag <roottag>] [--regen-baseline]

    --regen-baseline：对**本次扫描面**全对账一次，程序化重生成 tools/baseline-sot-dup.json。
      合并规则（两扫描面共一份基线文件）：本次扫描 roottag 集合内的旧 items 整体替换，
      集合外的 items 原样保留（dual 面＝{experts,skills}，single 面＝{<tag>}）。
      基线快照由本开关生成，禁手抄（旧基线由 git 史留痕）。

检查项：
    A1（MC-SOT-1）agents 席 MD 之间、MD 与 skills 之间 ≥12 CJK 连续段行级重合
       ——重合＝第二真源嫌疑。**豁免键＝「行文本＋出现文件集合」**（decisions §九·①）：
       文本匹配且出现文件 ∈ 该文本既定文件集合 → 转 WATCH 并标「｜基线豁免（文本＋
       文件集合）」，不计 BLOCK；文本不在基线、或文本在基线但出现在集合外的新文件
       → 照 BLOCK 并标「｜新命中」（同文本搬家必被抓）。
    A2（MC-SOT-2）agents/ 与 skills/ 内反引号 .md 路径指针可达性——悬空＝BLOCK。
       dual 模式解析探针（依序）：① 相对 bundle 根；② 相对所在目录；
       ③ 相对技能真源根；④ 剥去 `skills/` 前缀后相对技能真源根
       （出池指针 `skills/<域>/…` 在 skills 仓的落点＝`<域>/…`）。
    B （MC-SKILL-LINE）SKILL.md token ≤5000（script-v1/ceil/emoji 非 CJK 池）。

退出码（闭集，见 60-gates.md §六）：0 通过／1 违规／2 用法错／4 基础设施错。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

CJK_RE = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')
MIN_CJK = 12                 # 重合判定阈值：行内 ≥12 个 CJK 字符
SKILL_LINE = 5000            # MC-SKILL-LINE：技能层 ≤5000 token 级
# 拆仓（2026-10-26 皮总拍定）：专家包本体在姊妹仓，默认包＝跨仓相对路径。
# 前提＝三仓并列于同一父目录（D:\）；不满足时用 --pkg / --skills-root 显式指定。
DEFAULT_PKG = '../multi-agent-collab-experts/workbuddy/baigong-video-team'
DEFAULT_SKILLS_ROOT = '../multi-agent-collab-skills/skills'
DEFAULT_TAG_DUAL_BUNDLE = 'experts'    # 双根口径：bundle 根 roottag
DEFAULT_TAG_DUAL_SKILLS = 'skills'     # 双根口径：技能真源根 roottag
DEFAULT_TAG_SINGLE = 'pkg'             # 单根口径缺省 roottag（软开调项传 softdev）

# 基线快照（外置 JSON＝tools/baseline-sot-dup.json·程序化生成以免手抄漂移）：
#   形态＝ items[]：{text＝行文本, files＝该文本既定出现的文件集合（两段式标识）}。
#   **豁免键＝「文本＋文件集合」**（皮总拍板 decisions §九·①，规范来源见文件头
#   MC-SOT-EXEMPT 块）——不取纯文本键，以堵住「同文本搬家被误标基线」的盲区。
#   判定：仅当「行文本匹配」且「出现文件 ∈ 该文件集合」才豁免（转 WATCH·不计 BLOCK）；
#   文本不在基线、或出现在集合外的新文件 → 照 BLOCK（标「｜新命中」）。
#   判据强度（MIN_CJK／SKILL_LINE／OA-D6 裁-21 裸基名→WATCH 划界）不因豁免而变。
BASELINE_SNAPSHOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'baseline-sot-dup.json')

# MC-SOT-2 外部产地注记白名单（V8 批 BLOCK 7 裁定 a·audit-h08b·2026-10-28）：
#   content 域 V1/V2 五件件头「来源标注：源＝drama-script-team 包 …」中的反引号路径
#   ＝外部市场包产地注记（非我方消费指针），多探针天然不可达。仅当「目标命中白名单」
#   且「该行含『来源标注』或『源＝』」才降级 WATCH；白名单外悬空照 BLOCK。
EXTERNAL_PROVENANCE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'sot-external-provenance.txt')


def load_external_provenance() -> set:
    if not os.path.isfile(EXTERNAL_PROVENANCE):
        return set()
    try:
        with open(EXTERNAL_PROVENANCE, 'r', encoding='utf-8') as handle:
            return {ln.split('#', 1)[0].strip() for ln in handle
                    if ln.split('#', 1)[0].strip()}
    except (OSError, UnicodeDecodeError) as exc:
        raise SystemExit('infra error: 白名单读取失败 %s: %s' % (EXTERNAL_PROVENANCE, exc))


def load_baseline() -> dict:
    """读基线快照：返回 {行文本 -> 既定出现文件集合(frozenset)}。

    快照缺失＝无基线（全部按新命中输出，更严不更松）；形态不符或损坏＝exit 4
    （不猜语义，与 60-gates §六「基础设施错」一致）。
    """
    if not os.path.isfile(BASELINE_SNAPSHOT):
        return {}
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


def collect_md(root_abs: str, tag: str, include_all_non_agents: bool):
    """一个根的 md 收集：返回 (agents, skills) 两段式标识列表（正斜杠·排序）。

    agents＝`agents/` 子树；skills＝`skills/` 子树（include_all_non_agents＝True 时
    该根下所有非 agents/ 的 md 都算 skills——技能真源根无 agents/ 子树，五域目录
    直接为顶层）。根内其余 md（如 bundle README）不入对账面（与旧口径一致）。
    """
    agents, skills = [], []
    for cur, dirs, files in os.walk(root_abs):
        dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__')]
        for f in sorted(files):
            if not f.endswith('.md'):
                continue
            rel = norm(os.path.relpath(os.path.join(cur, f), root_abs))
            if rel.startswith('agents/'):
                agents.append('%s:%s' % (tag, rel))
            elif rel.startswith('skills/') or include_all_non_agents:
                skills.append('%s:%s' % (tag, rel))
    return sorted(agents), sorted(skills)


def big_lines(abs_path: str):
    """行内 ≥12 CJK 的行：返回 [(行号, 规范化行文本)]。"""
    out = []
    try:
        with open(abs_path, 'r', encoding='utf-8') as handle:
            for i, line in enumerate(handle, 1):
                stripped = line.strip()
                if len(CJK_RE.findall(stripped)) >= MIN_CJK:
                    out.append((i, stripped))
    except (OSError, UnicodeDecodeError) as exc:
        raise SystemExit('infra error: 读不到 %s: %s' % (abs_path, exc))
    return out


POINTER_RE = re.compile(r'`([A-Za-z0-9][A-Za-z0-9./_-]*\.md)`')


def check_pointers(abs_of: dict, skills_abs: str | None, rel_files, provenance: set):
    """A2：反引号 .md 路径可达性。含 / 的按多探针解析（口径见模块 docstring）：
    ①相对 bundle 根 ②相对所在目录 ③相对技能真源根（dual）④剥 `skills/` 前缀后
    相对技能真源根（dual）。裸基名（不含 /）＝WATCH（OA-D6 裁-21 同款划界）。
    外部产地注记白名单（V8 BLOCK 7 裁定 a）：目标命中白名单且该行含产地标志＝WATCH。"""
    findings = []
    for rel in rel_files:
        abs_path = abs_of[rel]
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
                # 多探针：所在目录＋所属根＋（dual）技能真源根两式
                candidates = [os.path.normpath(os.path.join(os.path.dirname(abs_path), target))]
                # 所属根探针：tag 段剥掉后还原该文件所属根
                owner_root = abs_of.get(rel + '#root')
                if owner_root:
                    candidates.append(os.path.normpath(os.path.join(owner_root, target)))
                if skills_abs:
                    candidates.append(os.path.normpath(os.path.join(skills_abs, target)))
                    if target.startswith('skills/'):
                        candidates.append(os.path.normpath(
                            os.path.join(skills_abs, target[len('skills/'):]))
                        )
                if not any(os.path.isfile(c) for c in candidates):
                    if target in provenance and ('来源标注' in line or '源＝' in line):
                        findings.append((rel, i, 'WATCH', 'MC-SOT-2',
                                         '外部产地注记 `%s` → 白名单豁免（外部包路径·非我方消费指针）' % target))
                        continue
                    findings.append((rel, i, 'BLOCK', 'MC-SOT-2',
                                     '指针悬空 `%s` → 包根/所在目录/技能真源根多探均不存在' % target))
    return findings


def scan(agents: list, skills: list, abs_of: dict, skills_abs: str | None,
         baseline: dict):
    """跑 A1＋A2＋B 三项，返回 (findings, dup_items, n_exempt, n_watch_ptr)。

    dup_items＝本次扫描面全部 A1 重合文本的基线形态 items（供 --regen-baseline）。
    """
    findings = []
    n_exempt = 0

    # --- A1 骨架-本体对账：≥12 CJK 行级重合（scope＝至少一侧为 agents） ---
    index = {}   # 行文本 -> [(标识, 行号)]
    for rel in agents + skills:
        for i, line in big_lines(abs_of[rel]):
            index.setdefault(line, []).append((rel, i))
    dup_items = []
    for line, occ in index.items():
        files = sorted({rel for rel, _ in occ})
        if len(files) > 1 and any(f in agents for f in files):
            dup_items.append({'text': line, 'files': files})
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

    # --- A2 反引号指针可达性 ---
    findings.extend(check_pointers(abs_of, skills_abs, agents + skills, load_external_provenance()))

    # --- B 技能层线检：SKILL.md ≤5000（script-v1/ceil/emoji 非 CJK 池） ---
    for rel in skills:
        if rel.endswith('SKILL.md'):
            with open(abs_of[rel], 'r', encoding='utf-8') as handle:
                t = tokens(handle.read())
            if t > SKILL_LINE:
                findings.append((rel, 1, 'BLOCK', 'MC-SKILL-LINE',
                                 'SKILL.md token %d > %d（script-v1/ceil/emoji 非 CJK 池）'
                                 % (t, SKILL_LINE)))
    n_watch_ptr = sum(1 for f in findings if f[2] == 'WATCH' and f[3] != 'MC-SOT-1')
    return findings, dup_items, n_exempt, n_watch_ptr


def regen_baseline(dup_items: list, tags: set) -> None:
    """--regen-baseline：程序化重生成基线快照（禁手抄的机械化实现）。

    合并规则＝本次扫描 roottag 集合内的旧 items 整体替换、集合外原样保留
    （dual 面＝{experts, skills}，single 面＝{<tag>}），两扫描面共一份基线文件。
    旧格式 items（files 无两段式 `:` 标识＝T2 前口径）一律视为被替换对象——
    两段式口径生效后它们永不命中（files 集合对不上），留着只造噪音；
    其史实由 git 史留痕（拆仓 T2 票面明示）。
    """
    kept = []
    if os.path.isfile(BASELINE_SNAPSHOT):
        try:
            with open(BASELINE_SNAPSHOT, 'r', encoding='utf-8') as handle:
                old = json.load(handle)
            for item in old.get('items', []):
                files = item.get('files', [])
                if not all(':' in f for f in files):
                    continue            # 旧格式（无两段式标识）→ 替换
                item_tags = {f.split(':', 1)[0] for f in files}
                if not item_tags.issubset(tags):
                    kept.append(item)   # 本次面之外（另一扫描面）的 items 保留
        except (OSError, ValueError) as exc:
            raise SystemExit('infra error: 读旧基线失败（拒绝盲写覆盖）%s: %s'
                             % (BASELINE_SNAPSHOT, exc))
    doc = {
        'note': ('W2 真源对账脚本 A1 基线快照（**豁免键＝行文本＋该文本既定出现的文件集合**）。'
                 '每条 item＝一条基线行文本＋其既定出现文件集合；仅当「文本匹配」且「出现文件 '
                 '∈ files」才豁免（转 WATCH），同文本出现在集合外的新文件照 BLOCK（皮总拍板 '
                 'decisions §九·①，规范来源见脚本头 MC-SOT-EXEMPT 块）。本件由脚本 '
                 '--regen-baseline 程序化生成，禁手抄。文件标识＝两段式 `<roottag>:<根内相对路径>`'
                 '（roottag 闭集见脚本 docstring·T2 三仓口径）。'),
        'exemption_key': '文本＋出现文件集合（不是纯文本键）',
        'path_key_format': 'roottag:root内相对路径（正斜杠）；roottag∈{experts,skills,softdev}',
        'items': sorted(kept + dup_items, key=lambda it: (it['files'][0] if it['files'] else '', it['text'])),
    }
    try:
        with open(BASELINE_SNAPSHOT, 'w', encoding='utf-8') as handle:
            json.dump(doc, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
    except OSError as exc:
        raise SystemExit('infra error: 基线快照写入失败 %s: %s' % (BASELINE_SNAPSHOT, exc))
    print('regen-baseline: 写入 %d 条 items（本次面 tags=%s·替换旧面 items·其余保留）'
          % (len(doc['items']), '+'.join(sorted(tags))))


def main() -> int:
    parser = argparse.ArgumentParser(description='W2 真源对账（骨架-本体＋技能层线检·T2 三仓口径）')
    parser.add_argument('--root', default='', help='devkits 仓根（默认自脚本位置向上找 deliverables/）')
    parser.add_argument('--mode', default='dual', choices=('dual', 'single'),
                        help='dual＝bundle 根＋技能真源根双根对账（缺省）；single＝旧包内单根口径')
    parser.add_argument('--pkg', default=DEFAULT_PKG, help='被测专家包（相对仓根）')
    parser.add_argument('--skills-root', default=DEFAULT_SKILLS_ROOT,
                        help='技能真源根（相对仓根·仅 dual 模式用）')
    parser.add_argument('--tag', default='', help='single 模式 roottag（缺省 pkg；软开调项用 softdev）')
    parser.add_argument('--regen-baseline', action='store_true',
                        help='对本次扫描面全对账并重生成基线快照（程序化·禁手抄）')
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
    pkg_abs = os.path.abspath(os.path.join(root, args.pkg))
    if not os.path.isdir(pkg_abs):
        sys.stderr.write('usage error: 包目录不存在：%s\n' % args.pkg)
        return 2

    agents, skills = [], []
    abs_of = {}
    skills_abs = None
    tags = set()
    if args.mode == 'dual':
        skills_abs = os.path.abspath(os.path.join(root, args.skills_root))
        if not os.path.isdir(skills_abs):
            sys.stderr.write('usage error: 技能真源根不存在：%s\n' % args.skills_root)
            return 2
        tag_b, tag_s = DEFAULT_TAG_DUAL_BUNDLE, DEFAULT_TAG_DUAL_SKILLS
        a1, s1 = collect_md(pkg_abs, tag_b, include_all_non_agents=False)
        a2, s2 = collect_md(skills_abs, tag_s, include_all_non_agents=True)
        agents, skills = a1 + a2, s1 + s2
        tags = {tag_b, tag_s}
        # 指针探针①「相对 bundle 根」的根目录登记（仅 bundle 根成员适用）
        for rel in a1 + s1:
            abs_of[rel + '#root'] = pkg_abs
        abs_of.update({rel: os.path.join(pkg_abs, rel.split(':', 1)[1]) for rel in a1 + s1})
        abs_of.update({rel: os.path.join(skills_abs, rel.split(':', 1)[1]) for rel in a2 + s2})
    else:
        tag = args.tag or DEFAULT_TAG_SINGLE
        a, s = collect_md(pkg_abs, tag, include_all_non_agents=False)
        agents, skills = a, s
        tags = {tag}
        abs_of.update({rel: os.path.join(pkg_abs, rel.split(':', 1)[1]) for rel in a + s})
        abs_of.update({rel + '#root': pkg_abs for rel in a + s})

    if not agents:
        sys.stderr.write('usage error: %s 下无 agents/ 内 md\n' % args.pkg)
        return 2

    baseline = load_baseline()
    findings, dup_items, n_exempt, n_watch_ptr = scan(agents, skills, abs_of, skills_abs, baseline)

    if args.regen_baseline:
        regen_baseline(dup_items, tags)
        # 重生成后基线即本次面 → 复跑一次 A1 判定以输出「零新 BLOCK」的验收读数
        baseline = load_baseline()
        findings, _dup, n_exempt, n_watch_ptr = scan(agents, skills, abs_of, skills_abs, baseline)

    # --- 输出一行一封（run-gates FINDING_RE 兼容）＋计数行 ---
    violations = 0
    for rel, i, sev, spec, msg in sorted(findings):
        print('%s:%d: %s %s %s' % (rel, i, sev, spec, msg))
        if sev == 'BLOCK':
            violations += 1
    exit_code = 1 if violations else 0
    print('check-source-of-truth: 模式 %s｜文件 %d（agents %d＋skills %d）'
          '｜BLOCK %d（新命中 %d）｜基线豁免 %d（WATCH·键＝文本＋文件集合）'
          '｜指针 WATCH %d｜exit %d'
          % (args.mode, len(agents) + len(skills), len(agents), len(skills),
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
