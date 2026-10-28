#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: MC-ZL-BLIND-1
# spec_file: ../multi-agent-collab-skills/skills/zhulong/references/R8-契约锚与改判账.md
# spec_anchor: > **MC-ZL-BLIND-1**（闸门三 check-blind-eval·只验台账不跑评）：台账落 devkits .collab/evidence/blind-eval/<pack>@<tag>-<date>.json；schema 闭集字段＝pack/tag/piece/type(persona|technique)/dim_scores（persona {30,20,20,15,15}／技法 {30,25,25,20}）/answer_agent_id≠score_agent_id/decoy_result（技法必填）/grade(A|B|C|D)/notes。判据：每镜片件必有台账条目（未执行不得计绿）＝缺→BLOCK；grade<B→BLOCK；答题＝评分同 agent→BLOCK；技法缺 decoy 或诱饵失败→BLOCK；persona 引库内自评分替代复跑→BLOCK；红线题得分 0 记录缺失→WATCH ⛓ V3:159-183。取数形态（成片段落＝分镜文本＋镜头参数 vs 真成片帧）不在本票定死，按当期在产项目实取 ⛓ V3:272。
# spec_clause_sha256: 92216556f7cac94d68bfae8cc0a155d65edc8d47174aaabfc2a5a9f360e280c6
# spec_version: 1.0
# spec_effective: 2026-10-28
# provider: multi-collab
# --- /spec-provenance ---
#
# 闸门三 · 双 agent 盲评台账机检（T-zhulong-02·Z04·结构案 §四-3）。
# **只验台账不跑评**：评分须双 agent 真人/真席分离执行（R5 卷跑批规程），脚本不代办（防自评自证）。
# 跑批规程本体＝skills 仓 zhulong 包 references/R5 卷；本脚本＝台账机检接口。
# E4（主理人裁定）：盲评取数形态不在本票定死——本件只留接口与规程文本，不验取数形态。
# 台账落点：devkits .collab/evidence/blind-eval/<pack>@<tag>-<date>.json（证据面·不入 git）。
# 输入面：--pack <pack>@<tag> 产物包 tag 名（判"每镜片件必有台账条目"）；缺省＝接口模式
#   （只校在盘台账 schema＋无台账出 WATCH——未执行判据不得计绿，但缺判据面本身按接口模式分账）。
# 通用口径：只读；--root 由 run-gates 注入；发现行照 FINDING_RE；SEV 闭集 BLOCK/WATCH；
#   退出码闭集 0/1/2/4（60-gates §六）；"绿"＝零 BLOCK。
"""check-blind-eval：盲评台账 schema/反作弊/等级闸机检（MC-ZL-BLIND-1）。

用法：
    python check-blind-eval.py [--root <devkits仓根>] [--pack <pack>@<tag>]

退出码（闭集，见 60-gates.md §六）：0 通过／1 违规（≥1 发现）／2 用法错／4 基础设施错。
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

LEDGER_SCHEMA = ('pack', 'tag', 'piece', 'type', 'dim_scores',
                 'answer_agent_id', 'score_agent_id', 'decoy_result', 'grade', 'notes')
DIM_CLOSE = {'persona': [30, 20, 20, 15, 15], 'technique': [30, 25, 25, 20]}
GRADE_CLOSE = ('A', 'B', 'C', 'D')
GRADE_FAIL = ('C', 'D')
TYPE_CLOSE = ('persona', 'technique')


def load_ledgers(evidence_dir: str):
    """读全部台账件：返回 [(文件名, doc 或 None（损坏）)]。损坏台账不删不猜（史实留盘）。"""
    out = []
    if not os.path.isdir(evidence_dir):
        return out
    for name in sorted(os.listdir(evidence_dir)):
        if not name.endswith('.json'):
            continue
        try:
            with open(os.path.join(evidence_dir, name), 'r', encoding='utf-8') as handle:
                doc = json.load(handle)
            out.append((name, doc))
        except (OSError, ValueError) as exc:
            sys.stderr.write('infra warn: 台账损坏 %s: %s\n' % (name, exc))
            out.append((name, None))
    return out


def check_entry(fname: str, entry: dict):
    """单条目 schema＋反作弊＋等级闸。返回 findings [(标识,SEV,spec,msg)]。"""
    findings = []
    missing = [k for k in LEDGER_SCHEMA if k not in entry]
    if missing:
        findings.append((fname, 'BLOCK', 'MC-ZL-BLIND-1',
                         '台账条目缺 schema 字段 %s' % ','.join(missing)))
        return findings
    typ = entry['type']
    if typ not in TYPE_CLOSE:
        findings.append((fname, 'BLOCK', 'MC-ZL-BLIND-1',
                         'type 闭集外取值 %r（persona|technique）' % typ))
        return findings
    ds = entry['dim_scores']
    if not isinstance(ds, list) or sorted(ds, reverse=True) != DIM_CLOSE[typ]:
        findings.append((fname, 'BLOCK', 'MC-ZL-BLIND-1',
                         'dim_scores 不等于 %s 型闭集分值 %s' % (typ, DIM_CLOSE[typ])))
    if entry['grade'] not in GRADE_CLOSE:
        findings.append((fname, 'BLOCK', 'MC-ZL-BLIND-1',
                         'grade 闭集外取值 %r' % entry['grade']))
    elif entry['grade'] in GRADE_FAIL:
        findings.append((fname, 'BLOCK', 'MC-ZL-BLIND-1',
                         'grade=%s <B → 回炉件不得入库（④-1/④-2）' % entry['grade']))
    if entry['answer_agent_id'] == entry['score_agent_id']:
        findings.append((fname, 'BLOCK', 'MC-ZL-BLIND-1',
                         '答题 agent＝评分 agent（反作弊②违例）'))
    if typ == 'technique':
        if entry['decoy_result'] in (None, '', 'fail', 'FAIL', False):
            findings.append((fname, 'BLOCK', 'MC-ZL-BLIND-1',
                             '技法件缺 decoy_result 或诱饵未通过（②-2/④-2）'))
    else:
        notes = str(entry.get('notes', ''))
        if '库内' in notes and ('替代' in notes or 'FIDELITY' in notes.upper()):
            findings.append((fname, 'BLOCK', 'MC-ZL-BLIND-1',
                             'persona 件引库内自评分替代复跑（④-3 违例）'))
        if '红线' not in notes and '伪装成本人断言' not in notes:
            findings.append((fname, 'WATCH', 'MC-ZL-BLIND-1',
                             '红线题"伪装成本人断言"得分记录未见（notes 应含红线读数）'))
    return findings


def lens_pieces_of_pack(root: str, pack_name: str):
    """从 skills 仓产物包 SKILL.md 索引行提取镜片主件基名（类型注记路由）。"""
    skl = os.path.join(root, '..', 'multi-agent-collab-skills')
    skill_md = os.path.join(skl, 'skills', pack_name, 'SKILL.md')
    if not os.path.isfile(skill_md):
        sys.stderr.write('usage error: 产物包 SKILL.md 不存在：%s\n' % skill_md)
        raise SystemExit(2)
    pieces = []
    with open(skill_md, 'r', encoding='utf-8') as handle:
        for line in handle:
            m = re.search(r'`(references/[^`]+\.md)`', line)
            if not m or '-deep' in m.group(1):
                continue
            if 'persona 镜片' in line:
                pieces.append((m.group(1), 'persona'))
            elif '技法镜片' in line:
                pieces.append((m.group(1), 'technique'))
    return pieces


def main() -> int:
    ap = argparse.ArgumentParser(description='闸门三 盲评台账机检（MC-ZL-BLIND-1·只验不跑）')
    ap.add_argument('--root', default='', help='devkits 仓根（run-gates 注入）')
    ap.add_argument('--pack', default='', help='产物包 tag 名（如 aigc-video-perspective@v1.2.0）：判每镜片件必有台账条目；缺省＝接口模式')
    args = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    if args.root:
        root = os.path.abspath(args.root)
    else:
        cur = here
        while True:
            if os.path.isdir(os.path.join(cur, '.collab')) or os.path.isdir(os.path.join(cur, 'tools')):
                root = cur
                break
            parent = os.path.dirname(cur)
            if parent == cur:
                sys.stderr.write('infra error: 未能定位仓根；请用 --root 指定\n')
                return 4
            cur = parent
    evidence_dir = os.path.join(root, '.collab', 'evidence', 'blind-eval')

    ledgers = load_ledgers(evidence_dir)
    n_block = n_watch = 0

    def emit(rel, sev, spec, msg):
        nonlocal n_block, n_watch
        print('%s:1: %s %s %s' % (rel, sev, spec, msg))
        if sev == 'BLOCK':
            n_block += 1
        else:
            n_watch += 1

    # 1) 在盘台账逐条 schema/反作弊/等级闸
    entries_by_pack = {}
    for fname, doc in ledgers:
        if doc is None:
            emit(fname, 'BLOCK', 'MC-ZL-BLIND-1', '台账件 JSON 损坏（不删不猜·须重跑落盘）')
            continue
        entries = doc.get('entries') if isinstance(doc, dict) else None
        if not isinstance(entries, list):
            emit(fname, 'BLOCK', 'MC-ZL-BLIND-1', '台账顶层缺 entries[]')
            continue
        for i, entry in enumerate(entries):
            if not isinstance(entry, dict):
                emit(fname, 'BLOCK', 'MC-ZL-BLIND-1', 'entries[%d] 非对象' % i)
                continue
            for rel, sev, spec, msg in check_entry(fname, entry):
                emit(rel, sev, spec, msg)
            key = (entry.get('pack', ''), entry.get('tag', ''))
            entries_by_pack.setdefault(key, set()).add(entry.get('piece', ''))

    # 2) 判据①：--pack 给定＝逐镜片件必有台账条目（未执行不得计绿）
    if args.pack:
        if '@' not in args.pack:
            sys.stderr.write('usage error: --pack 需 <pack>@<tag> 形态：%s\n' % args.pack)
            return 2
        pack_name, tag = args.pack.split('@', 1)
        have = entries_by_pack.get((pack_name, tag), set())
        for piece, _typ in lens_pieces_of_pack(root, pack_name):
            if piece not in have:
                emit(args.pack, 'BLOCK', 'MC-ZL-BLIND-1',
                     '镜片件 `%s` 无盲评台账条目（未执行不得计绿·R5 跑批四步）' % piece)
    elif not ledgers:
        emit('.collab/evidence/blind-eval/', 'WATCH', 'MC-ZL-BLIND-1',
             '盲评台账零在盘＝接口模式（产物票 --pack 判定"缺台账＝BLOCK"；规程见 R5 卷）')

    print('—— check-blind-eval 计数：BLOCK=%d WATCH=%d（绿＝零 BLOCK）' % (n_block, n_watch))
    return 1 if n_block or n_watch else 0


if __name__ == '__main__':
    sys.exit(main())
