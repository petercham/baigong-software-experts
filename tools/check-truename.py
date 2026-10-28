#!/usr/bin/env python3
# tools/check-truename.py · 闸门一 V8 真名残留机检（audit-h08·2026-10-28·设计稿 §⑤-4 口径）
# --- spec-provenance v1 ---
# spec_id: MC-FX-V8-1
# spec_file: ../multi-agent-collab-skills/skills/fuxi-skill/references/contract-anchors.md
# spec_anchor: > **MC-FX-V8-1**（闸门一 check-truename）：V8 真名残留扫描——扫描面＝perspective 类产物包全部真源（SKILL.md＋references/*.md＋frontmatter 全字段）＋content 域 genre-library 挂载列＋条目表注记区＋消费壳 ⛓ 挂载注记行；豁免面＝①各件 `## meta`…含「来源标注」的节（节名定位闭集）＋②料源登记件整件（文件类型面判定＝基名 `sources-ledger*.md`（主判定·基名闭集）或首三行含【类型：料源存档】注记（注记式·带互斥机检：凡件挂镜片类类型注记〔【类型：人格镜片】【类型：persona 镜片】【类型：技法镜片】含后缀形态〕或呈镜片形态〔件名含 lens/镜片 或 frontmatter description 含「镜片」〕的，注记式豁免不生效＝豁免伪造防线·T-fuxi-pres8-fix-01）；sources＝skill 料源、不进程序运行时，蒸馏全程真名作锚＝三节真名纪律所定，真名豁免·皮总拍板⑧ sources 双豁免）；无「来源标注」要求的料源登记件内真名不视为镜片显示面残留。词典＝工具侧 names（真名面）＋pseudonyms（化名包裹面）两件事前分段；旧化名留注释段不算命中面。命中三态＝EXEMPT（豁免面·绿）／SUBSTR（化名包裹子串误触·预分账）／VIOLATION（扫描面真名直书→BLOCK）。判绿＝零 VIOLATION ⛓ V3:225-228、235。
# spec_clause_sha256: 8f64e1a1664291f150159a4dcaaf08c4b45d791e8ed099ef461d63062de30e03
# spec_version: 1.2
# spec_effective: 2026-10-29
# provider: multi-collab
# --- /spec-provenance ---
# 泛化改造（T-zhulong-02·Z04·结构案 §四-1）：新增 --pack/--pseudonyms/--root，**默认行为不变**
#   （默认扫描面与 audit-h08 版逐字一致：perspective 包全真源＋genre-library/条目表＋两壳 ⛓ 注记行；
#    化名词典从硬编码闭集外置为 check-truename-pseudonyms.txt，词典内容与旧硬编码等值）。
# 扫描面闭集：perspective 类产物包全部真源（含 frontmatter）＋genre-library 挂载列（主件注记行＋配方条目表挂载列及其注记＝genre-recipe-entries.md 四节区）＋两壳 ⛓ 挂载指针注记行。
# 豁免面（T-fuxi-srcexempt-01·皮总拍板⑧ sources 真名豁免）：
#   ①各件含「来源标注」关键词的 meta 节（节名定位：从「## meta」或「## meta（来源标注…）」标题到下一同级标题或文件尾；节内须含「来源标注」四字）——行为不变；
#   ②料源登记件整件豁免（按**文件类型面**判定，不靠段落名硬撑：基名匹配 sources-ledger*.md＝主判定闭集，
#     或首三行出现【类型：料源存档】注记——注记式带互斥机检：同时挂镜片类注记/呈镜片形态的注记豁免不生效，
#     T-fuxi-pres8-fix-01 黄-2）——料源台账整件命中记 EXEMPT(料源登记件)。
# 词典：真名＝check-truename-names.txt（同目录）；化名包裹＝check-truename-pseudonyms.txt（同目录）。
#   CJK 词＝子串匹配；拉丁词＝词边界匹配；`#` 注释段不算词典命中面（旧化名留注释段·E3）。
# 命中三态分账（spec 条款正文＝skills 仓 fuxi-skill 包 references/contract-anchors MC-FX-V8-1·自指式初挂）：
#   EXEMPT   ＝命中落于豁免面节内（判绿）
#   SUBSTR   ＝命中被已知化名包裹（子串误触·人工复核口径自动预分账，如「李安」⊂「李安全」）
#   VIOLATION＝扫描面真名直书（未绿）→ 另输出 FINDING_RE 行（BLOCK MC-FX-V8-1）
# 退出码闭集（60-gates §六）：0＝扫描面零 VIOLATION／1＝有 VIOLATION／2＝用法错／4＝基础设施错。
import argparse
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)


def _find_root():
    cur = HERE
    while True:
        if os.path.isdir(os.path.join(cur, 'deliverables')):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return PARENT
        cur = parent


def load_words(path):
    """词典件读取：每行一词，`#` 注释段不算词典内容（闭集断言：空文件＝用法错在调用方处理）。"""
    cjk, lat = [], []
    try:
        with io.open(path, encoding='utf-8') as f:
            for line in f:
                w = line.split('#', 1)[0].strip()
                if not w:
                    continue
                (cjk if re.search(r'[\u4e00-\u9fff]', w) else lat).append(w)
    except (OSError, UnicodeDecodeError) as exc:
        sys.stderr.write('infra error: 词典读取失败 %s: %s\n' % (path, exc))
        raise SystemExit(4)
    return cjk, lat


SRC_LEDGER_NAME_RE = re.compile(r'^sources-ledger.*\.md$')
SRC_LEDGER_TAG = '【类型：料源存档】'
# 豁免伪造防线（T-fuxi-pres8-fix-01·黄-2）：注记式豁免与镜片形态互斥。
# 镜片类类型注记（含后缀形态如「persona 镜片·理论透镜」）：
LENS_TAG_MARKS = ('人格镜片', 'persona 镜片', '技法镜片')
TYPE_TAG_RE = re.compile(r'【类型：([^】]+)】')
LENS_FORM_RE = re.compile(r'lens|镜片', re.I)


def is_lens_piece(path, text):
    """镜片形态判定（互斥机检面）：件名含 lens/镜片／首三行挂镜片类类型注记／
    frontmatter 块内出现「镜片」字样（description 自述）。"""
    if LENS_FORM_RE.search(os.path.basename(path)):
        return True
    lines = text.splitlines()
    if lines and lines[0].strip() == '---':
        for ln in lines[1:20]:
            s = ln.strip()
            if s == '---':
                break
            if '镜片' in s:
                return True
    for tg in TYPE_TAG_RE.findall('\n'.join(lines[:3])):
        if any(m in tg for m in LENS_TAG_MARKS):
            return True
    return False


def is_source_ledger(path, text):
    """料源登记件判定（文件类型面·基名闭集为主判定）：
    ①基名＝sources-ledger*.md（主判定·闭集）→ 豁免；
    ②首三行出现【类型：料源存档】注记（注记式）→ 豁免，但带互斥机检：
      凡同时挂镜片类类型注记或呈镜片形态（件名 lens/镜片、frontmatter 自述镜片）的，
      注记豁免不生效＝防镜片件挂注记伪造豁免（黄-2）。"""
    if SRC_LEDGER_NAME_RE.match(os.path.basename(path)):
        return True
    head = '\n'.join(text.splitlines()[:3])
    if SRC_LEDGER_TAG not in head:
        return False
    return not is_lens_piece(path, text)


def exempt_spans(text):
    """豁免面①＝含「来源标注」的 meta 节（## meta 标题起，至下一 ## 标题或 EOF）。"""
    spans = []
    lines = text.splitlines(keepends=True)
    pos = [0]
    for ln in lines:
        pos.append(pos[-1] + len(ln))
    for i, ln in enumerate(lines):
        if re.match(r'^## meta', ln):
            j = i + 1
            while j < len(lines) and not re.match(r'^## ', lines[j]):
                j += 1
            body = ''.join(lines[i:j])
            if '来源标注' in body:
                spans.append((pos[i], pos[j]))
    return spans


def in_exempt(off, spans):
    return any(a <= off < b for a, b in spans)


def wrapped_pseudonym(text, start, end, pseudonyms):
    for p in pseudonyms:
        if start + len(p) <= len(text) and text[start:start + len(p)] == p:
            return p
        if start - len(p) >= 0 and text[start - len(p):start + (end - start) + (len(p) - (end - start))] == p:
            return p
    for p in pseudonyms:
        i = 0
        while True:
            i = text.find(p, i)
            if i < 0:
                break
            if i <= start < i + len(p):
                return p
            i += 1
    return None


def scan_file(path, cjk, lat, label, pseudonyms):
    text = io.open(path, encoding='utf-8').read()
    spans = exempt_spans(text)
    whole_exempt = is_source_ledger(path, text)  # 豁免面②＝料源登记件整件（拍板⑧真名豁免）
    hits = []
    for w in cjk:
        i = 0
        while True:
            i = text.find(w, i)
            if i < 0:
                break
            line = text.count('\n', 0, i) + 1
            if whole_exempt:
                st = 'EXEMPT(料源登记件·豁免面②)'
            elif in_exempt(i, spans):
                st = 'EXEMPT'
            else:
                p = wrapped_pseudonym(text, i, i + len(w), pseudonyms)
                st = f'SUBSTR(包裹化名:{p})' if p else 'VIOLATION'
            hits.append((line, w, st))
            i += len(w)
    for w in lat:
        pat = re.compile(r'(?<![A-Za-z])' + re.escape(w) + r'(?![A-Za-z])', re.IGNORECASE)
        for m in pat.finditer(text):
            line = text.count('\n', 0, m.start()) + 1
            if whole_exempt:
                st = 'EXEMPT(料源登记件·豁免面②)'
            elif in_exempt(m.start(), spans):
                st = 'EXEMPT'
            else:
                st = 'VIOLATION'
            hits.append((line, m.group(0), st))
    return label, hits


def main():
    ap = argparse.ArgumentParser(description='V8 真名残留机检（闸门一·MC-FX-V8-1）')
    ap.add_argument('--root', default='', help='devkits 仓根（缺省自脚本位置向上找 deliverables/；用于姊妹仓相对定位）')
    ap.add_argument('--pack', default='', help='产物包目录（绝对或相对仓根）。给出＝只扫该包真源（新产物包票用）；缺省＝audit-h08 全默认扫描面（行为不变）')
    ap.add_argument('--pseudonyms', default='', help='化名词典路径（缺省＝同目录 check-truename-pseudonyms.txt）')
    args = ap.parse_args()

    root = os.path.abspath(args.root) if args.root else _find_root()
    skl = os.path.join(root, '..', 'multi-agent-collab-skills')
    exp = os.path.join(root, '..', 'multi-agent-collab-experts')
    per = os.path.join(skl, 'skills', 'aigc-video-perspective')

    pseudo_file = args.pseudonyms or os.path.join(HERE, 'check-truename-pseudonyms.txt')
    cjk, lat = load_words(os.path.join(HERE, 'check-truename-names.txt'))
    pseudo_cjk, pseudo_lat = load_words(pseudo_file)  # 化名词典＝CJK＋拉丁两段均入包裹分账
    pseudonyms = pseudo_cjk + pseudo_lat

    files = []
    if args.pack:
        pack = args.pack if os.path.isabs(args.pack) else os.path.join(root, args.pack)
        if not os.path.isdir(pack):
            sys.stderr.write('usage error: 包目录不存在：%s\n' % pack)
            return 2
        for r, _d, fs in os.walk(pack):
            for f in fs:
                if f.endswith('.md'):
                    files.append((os.path.join(r, f), '产物包真源'))
    else:
        for r, _d, fs in os.walk(per):
            for f in fs:
                if f.endswith('.md'):
                    files.append((os.path.join(r, f), 'perspective真源'))
        # genre-library 挂载列区（主件注记行＋条目表所在四节区）
        files.append((os.path.join(skl, 'skills', 'aigc-video-content', 'references', 'genre-library.md'), '挂载列·主件(全文·词典仅指挂载列语义区,真名词典在通识文本天然零命中,如实全扫)'))
        files.append((os.path.join(skl, 'skills', 'aigc-video-content', 'references', 'genre-recipe-entries.md'), '挂载列·条目表+注记(全文全扫)'))

    # 两壳 ⛓ 注记行（仅注记行入扫描面·默认面专属）
    shell_marks = {} if args.pack else {
        os.path.join(exp, 'workbuddy', 'hjh-aigc-video-team', 'agents', 'aigc-screenwriter.md'): '挂载',
        os.path.join(exp, 'workbuddy', 'hjh-aigc-video-team', 'agents', 'aigc-operations.md'): '挂载',
    }
    total_v = total_s = total_e = 0
    finding_lines = []
    print(f'词典：CJK {len(cjk)} 词／拉丁 {len(lat)} 词（词边界）')
    for path, label in sorted(files):
        try:
            lab, hits = scan_file(path, cjk, lat, label, pseudonyms)
        except (OSError, UnicodeDecodeError) as exc:
            sys.stderr.write('infra error: 读不到 %s: %s\n' % (path, exc))
            return 4
        rel = os.path.relpath(path, 'D:/')
        if not hits:
            continue
        for line, w, st in sorted(hits):
            tag = 'E' if st.startswith('EXEMPT') else ('S' if st.startswith('SUBSTR') else 'V')
            if tag == 'E':
                total_e += 1
            elif tag == 'S':
                total_s += 1
            else:
                total_v += 1
                finding_lines.append('%s:%d: BLOCK MC-FX-V8-1 扫描面真名直书「%s」(%s)' % (rel, line, w, label))
            print(f'[{tag}] {rel}:{line}  「{w}」  {st}')
    # 两壳注记行
    for path, kw in shell_marks.items():
        try:
            text = io.open(path, encoding='utf-8').read()
        except (OSError, UnicodeDecodeError) as exc:
            sys.stderr.write('infra error: 读不到壳件 %s: %s\n' % (path, exc))
            return 4
        rel = os.path.relpath(path, 'D:/')
        for n, ln in enumerate(text.splitlines(), 1):
            if kw in ln and '⛓' in ln or ('视角镜片' in ln):
                body = ln
                hits = [w for w in cjk if w in body] + [w for w in lat if re.search(r'(?<![A-Za-z])' + re.escape(w) + r'(?![A-Za-z])', body, re.I)]
                for w in hits:
                    p = wrapped_pseudonym(body, body.find(w), 0, pseudonyms) if re.search(r'[\u4e00-\u9fff]', w) else None
                    st = f'SUBSTR(包裹化名:{p})' if p else 'VIOLATION'
                    print(f'[{"S" if st.startswith("SUBSTR") else "V"}] {rel}:{n}  「{w}」  {st} (壳⛓注记行)')
                    if st == 'VIOLATION':
                        total_v += 1
                        finding_lines.append('%s:%d: BLOCK MC-FX-V8-1 壳⛓注记行真名直书「%s」' % (rel, n, w))
                    else:
                        total_s += 1
    print(f'—— 分账：EXEMPT(豁免面命中·绿)={total_e}  SUBSTR(子串误触·判非残留)={total_s}  VIOLATION(扫描面真名直书)={total_v}')
    for fl in finding_lines:
        print(fl)
    return 1 if total_v else 0


if __name__ == '__main__':
    sys.exit(main())
