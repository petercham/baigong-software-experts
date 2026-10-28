#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: MC-ZL-STRUCT-1
# spec_file: ../multi-agent-collab-skills/skills/zhulong/references/R8-契约锚与改判账.md
# spec_anchor: > **MC-ZL-STRUCT-1**（闸门二 check-pack-structure·结构面）：①persona 镜片件必填节在位（identity/stance/traits/taboos/audience_contract/performance/exemplars〔含按需半〕/meta）＋件内禁项反查（词汇清单/强制勾选框/传记/名场面口号）→缺＝BLOCK ⛓ V3:29-42；②技法镜片节序闭集 I/R/A1/A2/E/B＋挂接＋meta，A2＋B 缺任一＝BLOCK ⛓ V3:117；④索引完备＝SKILL.md 逐件登记＋"何时必读"列＋"按需装载·默认不读"注记，缺登记＝BLOCK、裸基名互指＝WATCH ⛓ V3:255、262；⑤类型注记闭集＝【类型：方法论】【类型：判据】【类型：技法镜片】【类型：persona 镜片】，注记缺失＝WATCH、闭集外造词＝BLOCK ⛓ V3:113。
# spec_clause_sha256: c87d3e493a33bddd5e59c85510c4a64fab19f7afa7cb472c3f217ad3004e590f
# spec_version: 1.0
# spec_effective: 2026-10-28
# provider: multi-collab
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: MC-ZL-STRUCT-2
# spec_file: ../multi-agent-collab-skills/skills/zhulong/references/R8-契约锚与改判账.md
# spec_anchor: > **MC-ZL-STRUCT-2**（闸门二·帽面）：包内逐件（SKILL.md＋references 全部）≤2500（script-v1/ceil）→超限＝BLOCK；本帽补 MC-SKILL-LINE（≤5000 只覆 SKILL.md）覆盖不到的 V3⑥-1 逐件帽 ⛓ V3:243、260。zhulong 自身包同纳入帽检面（自身吃自家狗粮）。
# spec_clause_sha256: 9f16bfaa0254146c089532f7fd85be3cc15538029b1b6d5334abb79230b4cc73
# spec_version: 1.0
# spec_effective: 2026-10-28
# provider: multi-collab
# --- /spec-provenance ---
#
# 闸门二 · 六维/字段结构＋体量帽机检（T-zhulong-02·Z04·结构案 §四-2）。
# 条款正文＝skills 仓 zhulong 包 R8 卷（MC-ZL-* 自指式初挂·E1）；挂载初期按 MC-SOT-* 先例如实登记。
# 输入面：--pack <path>（绝对或相对仓根）指定产物包；缺省＝默认双包面
#   {skills仓 skills/aigc-video-perspective（产物示例）, skills仓 skills/zhulong（builder 自身·E5）}。
# 判据闭集（MC-ZL-STRUCT-1 结构面＋MC-ZL-STRUCT-2 帽面）：见上 spec_anchor。
# 通用口径：只读；--root 由 run-gates 注入；发现行照 FINDING_RE 一行一封；
#   严重度闭集＝BLOCK／WATCH（不新造词）；退出码闭集 0/1/2/4（60-gates §六）。
#   "绿"＝零 BLOCK（WATCH 计数如实出）。
"""check-pack-structure：perspective 类产物包＋zhulong 自身包的字段/节序闭集与逐件 2500 帽机检。

用法：
    python check-pack-structure.py [--root <devkits仓根>] [--pack <包目录>]...

退出码（闭集，见 60-gates.md §六）：0 通过／1 违规／2 用法错／4 基础设施错。
"""

from __future__ import annotations

import argparse
import os
import re
import sys

CJK_RE = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')
CAP = 2500  # script-v1 帽（tools/count_agent_tokens.py 同款口径）

# persona 镜片主件必填节（按 ## 标题定位；exemplars 允许落按需半＝同基名 *-deep*.md）
PERSONA_SECTIONS = ('identity', 'stance', 'traits', 'taboos',
                    'audience_contract', 'performance', 'meta')
PERSONA_DEEP_OK = ('exemplars',)
# 件内禁项反查（V3:42）
PERSONA_FORBIDDEN = (('词汇清单', '件内禁项违例：词汇清单'),
                     ('名场面口号', '件内禁项违例：名场面口号'),
                     ('- [ ]', '件内禁项违例：强制勾选框'))
# 技法镜片节序闭集（V3:113/117）：I/R/A1/A2/E/B＋挂接＋meta
TECH_SECTIONS = (('I 技法定义', False), ('R 出处引证', False), ('A1 ', False),
                 ('A2 ', True), ('E 怎么做', False), ('B 何时别用', True),
                 ('挂接', False), ('meta', False))
TYPE_TAG_RE = re.compile(r'【类型：([^】]+)】')
TYPE_CLOSE = ('方法论', '判据', '技法镜片', 'persona 镜片')


def tokens(text: str) -> int:
    """script-v1：CJK≈1/字、非 CJK≈4 字符/token、ceil；emoji＝非 CJK 池。"""
    cjk = len(CJK_RE.findall(text))
    return cjk + -(-(len(text) - cjk) // 4)


def read(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as handle:
            return handle.read()
    except (OSError, UnicodeDecodeError) as exc:
        sys.stderr.write('infra error: 读不到 %s: %s\n' % (path, exc))
        raise SystemExit(4)


def section_titles(text: str):
    return [ln for ln in text.splitlines() if ln.startswith('## ')]


def check_lens_piece(rel: str, text: str, pack_abs: str, base_name: str, tags):
    """按类型注记路由结构检（tags＝件标题注记∪索引行注记）。返回 findings [(rel,line,SEV,spec,msg)]。"""
    findings = []
    tagstr = ''.join(tags)
    if 'persona 镜片' in tagstr:
        titles = section_titles(text)
        joined = '\n'.join(titles)
        for sec in PERSONA_SECTIONS:
            if not re.search(r'^## .*' + re.escape(sec), joined, re.M):
                findings.append((rel, 1, 'BLOCK', 'MC-ZL-STRUCT-1',
                                 'persona 镜片必填节缺 `## %s`' % sec))
        # exemplars 允许落按需半（同基名 -deep）
        deep_ok = False
        for sec in PERSONA_DEEP_OK:
            if re.search(r'^## .*' + re.escape(sec), joined, re.M):
                continue
            for cur, _d, fs in os.walk(pack_abs):
                for f in fs:
                    if f.startswith(base_name) and f.endswith('.md') and 'deep' in f:
                        if re.search(r'^## .*' + re.escape(sec),
                                     '\n'.join(section_titles(read(os.path.join(cur, f)))), re.M):
                            deep_ok = True
            if not deep_ok:
                findings.append((rel, 1, 'BLOCK', 'MC-ZL-STRUCT-1',
                                 '必填节 `%s` 主件与同基名按需半均未见' % sec))
        body_wo_meta = re.split(r'^## meta', text, flags=re.M)[0]
        for pat, why in PERSONA_FORBIDDEN:
            if pat in body_wo_meta:
                line = next((i for i, ln in enumerate(text.splitlines(), 1)
                             if pat in ln and not ln.startswith('## meta')), 1)
                findings.append((rel, line, 'BLOCK', 'MC-ZL-STRUCT-1', why))
    elif '技法镜片' in ''.join(tags):
        titles = '\n'.join(section_titles(text))
        for sec, hard in TECH_SECTIONS:
            if not re.search(r'^## ' + re.escape(sec), titles, re.M):
                sev = 'BLOCK' if hard else 'WATCH'
                findings.append((rel, 1, sev, 'MC-ZL-STRUCT-1',
                                 '技法镜片节序缺 `## %s`%s'
                                 % (sec, '（A2/B 缺＝未绿·②-1）' if hard else '（沿编缺节·候裁）')))
    return findings


def norm_rel(p: str) -> str:
    return p.replace(os.sep, '/')


def index_registers(skill_text: str, rel_in_pack: str, base: str) -> bool:
    """SKILL.md 是否登记该件：字面基名/包内相对路径命中，或花括号分组形态（`x-{a,b}.md` 展开）命中。"""
    if base in skill_text or rel_in_pack in skill_text:
        return True
    for m in re.finditer(r'`([^`]*\{[^}]*\}[^`]*\.md)`', skill_text):
        pat = m.group(1)
        bm = re.match(r'^(.*)\{([^}]*)\}(.*)$', pat)
        if not bm:
            continue
        for alt in bm.group(2).split(','):
            cand = bm.group(1) + alt.strip() + bm.group(3)
            if cand == rel_in_pack or os.path.basename(cand) == base:
                return True
    return False


def check_pack(pack_abs: str):
    """单包六维/结构＋帽检。返回 findings（相对盘根路径标识）。"""
    findings = []
    if not os.path.isdir(pack_abs):
        sys.stderr.write('usage error: 包目录不存在：%s\n' % pack_abs)
        raise SystemExit(2)
    skill_md = os.path.join(pack_abs, 'SKILL.md')
    if not os.path.isfile(skill_md):
        findings.append((os.path.relpath(pack_abs, 'D:/'), 1, 'BLOCK', 'MC-ZL-STRUCT-1',
                         '包缺 SKILL.md 主件（索引完备无从检起）'))
        skill_text = ''
    else:
        skill_text = read(skill_md)
    ref_files = []
    refs_dir = os.path.join(pack_abs, 'references')
    if os.path.isdir(refs_dir):
        for cur, _d, fs in os.walk(refs_dir):
            for f in fs:
                if f.endswith('.md'):
                    ref_files.append(os.path.join(cur, f))
    # --- 帽面 MC-ZL-STRUCT-2：逐件 ≤2500（SKILL.md＋references 全部·README 不入装载面不检）---
    for p in ([skill_md] if skill_text else []) + ref_files:
        t = tokens(read(p))
        rel = os.path.relpath(p, 'D:/')
        if t > CAP:
            findings.append((rel, 1, 'BLOCK', 'MC-ZL-STRUCT-2',
                             '件 token %d > %d（script-v1/ceil·⑥-1 逐件帽）' % (t, CAP)))
    # --- 索引完备：references 逐件在 SKILL.md 登记 ---
    if skill_text:
        for p in ref_files:
            base = os.path.basename(p)
            rel_in_pack = norm_rel(os.path.relpath(p, pack_abs))
            if not index_registers(skill_text, rel_in_pack, base):
                findings.append((os.path.relpath(skill_md, 'D:/'), 1, 'BLOCK', 'MC-ZL-STRUCT-1',
                                 'references 件 `%s` 未在 SKILL.md 索引登记（缺登记）' % base))
        if '何时必读' not in skill_text:
            findings.append((os.path.relpath(skill_md, 'D:/'), 1, 'BLOCK', 'MC-ZL-STRUCT-1',
                             'SKILL.md 索引缺"何时必读"列'))
        if '按需装载' not in skill_text:
            findings.append((os.path.relpath(skill_md, 'D:/'), 1, 'WATCH', 'MC-ZL-STRUCT-1',
                             'SKILL.md 索引未见"按需装载·默认不读"注记'))
    # --- 镜片件判定：类型注记＝件标题行∪SKILL 索引行并集（在位体例：有的件注记在索引行）---
    ref_texts = {p: read(p) for p in ref_files}

    def piece_tags(base: str, text: str):
        tags = TYPE_TAG_RE.findall('\n'.join(text.splitlines()[:3]))
        if skill_text:
            for ln in skill_text.splitlines():
                if base in ln:
                    tags.extend(TYPE_TAG_RE.findall(ln))
        return tags

    is_lens_pack = any('-deep' not in os.path.basename(p)
                       and any('镜片' in t for t in piece_tags(os.path.basename(p), ref_texts[p]))
                       for p in ref_files)
    for p in ref_files:
        base = os.path.basename(p)
        if '-deep' in base:
            continue  # 按需半＝主件条款的延伸载体，不独立判类型
        text = ref_texts[p]
        rel = os.path.relpath(p, 'D:/')
        tags = piece_tags(base, text)
        if is_lens_pack:
            findings.extend(check_lens_piece(rel, text, pack_abs, os.path.splitext(base)[0], tags))
        for tg in tags:
            core = tg.split('·')[0].strip()
            if core not in TYPE_CLOSE:
                findings.append((rel, 1, 'BLOCK', 'MC-ZL-STRUCT-1',
                                 '类型注记闭集外造词【类型：%s】' % tg))
        if is_lens_pack and not tags:
            findings.append((rel, 1, 'WATCH', 'MC-ZL-STRUCT-1',
                             '镜片包件缺类型注记（`%s`）' % base))
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description='闸门二 六维/字段结构＋体量帽机检（MC-ZL-STRUCT-1/2）')
    ap.add_argument('--root', default='', help='devkits 仓根（run-gates 注入；用于姊妹仓相对定位）')
    ap.add_argument('--pack', action='append', default=[],
                    help='产物包目录（绝对或相对仓根），可重复；缺省＝默认双包面 perspective＋zhulong')
    args = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    if args.root:
        root = os.path.abspath(args.root)
    else:
        cur = here
        while True:
            if os.path.isdir(os.path.join(cur, 'deliverables')):
                root = cur
                break
            parent = os.path.dirname(cur)
            if parent == cur:
                sys.stderr.write('infra error: 未能定位仓根；请用 --root 指定\n')
                return 4
            cur = parent
    skl = os.path.join(root, '..', 'multi-agent-collab-skills')

    if args.pack:
        packs = [p if os.path.isabs(p) else os.path.join(root, p) for p in args.pack]
    else:
        packs = [os.path.join(skl, 'skills', 'aigc-video-perspective'),
                 os.path.join(skl, 'skills', 'zhulong')]

    n_block = n_watch = 0
    for pack in packs:
        if not os.path.isdir(pack):
            sys.stderr.write('usage error: 包目录不存在：%s\n' % pack)
            return 2
        for rel, line, sev, spec, msg in check_pack(pack):
            print('%s:%d: %s %s %s' % (rel, line, sev, spec, msg))
            if sev == 'BLOCK':
                n_block += 1
            else:
                n_watch += 1
    print('—— check-pack-structure 计数：BLOCK=%d WATCH=%d（绿＝零 BLOCK）' % (n_block, n_watch))
    return 1 if n_block or n_watch else 0


if __name__ == '__main__':
    sys.exit(main())
