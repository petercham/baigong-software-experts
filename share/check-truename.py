#!/usr/bin/env python3
# share/check-truename.py · V8 真名残留机检（audit-h08·2026-10-28·设计稿 §⑤-4 口径）
# 扫描面闭集：perspective 包全部真源（含 frontmatter）＋genre-library 挂载列（主件注记行＋配方条目表挂载列及其注记＝genre-recipe-entries.md 四节区）＋两壳 ⛓ 挂载指针注记行。
# 豁免面（唯一）：各件含「来源标注」关键词的 meta 节（节名定位：从「## meta」或「## meta（来源标注…）」标题到下一同级标题或文件尾；节内须含「来源标注」四字）。
# 词典：check-truename-names.txt（同目录）。CJK 词＝子串匹配；拉丁词＝词边界匹配。
# 命中两态分账：
#   EXEMPT   ＝命中落于豁免面节内（判绿）
#   SUBSTR   ＝命中被已知化名包裹（子串误触·人工复核口径自动预分账，如「李安」⊂「李安全」）
#   VIOLATION＝扫描面真名直书（未绿）
# 退出码：0＝扫描面零 VIOLATION。
import os, re, sys, io

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = r'D:\multi-agent-collab-experts'
SKL = r'D:\multi-agent-collab-skills'
PER = os.path.join(SKL, 'skills', 'aigc-video-perspective')

PSEUDONYMS = ['周星星', '斯皮尔饱嗝', '黑择名字', '姑不理客', '徐磕巴', '李安全', '皮亚睫', '喂鸽茨基']

def load_dict():
    cjk, lat = [], []
    with io.open(os.path.join(HERE, 'check-truename-names.txt'), encoding='utf-8') as f:
        for line in f:
            w = line.split('#', 1)[0].strip()
            if not w:
                continue
            (cjk if re.search(r'[\u4e00-\u9fff]', w) else lat).append(w)
    return cjk, lat

def exempt_spans(text):
    """豁免面＝含「来源标注」的 meta 节（## meta 标题起，至下一 ## 标题或 EOF）。"""
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

def wrapped_pseudonym(text, start, end):
    for p in PSEUDONYMS:
        if start + len(p) <= len(text) and text[start:start + len(p)] == p:
            return p
        if start - len(p) >= 0 and text[start - len(p):start + (end - start) + (len(p) - (end - start))] == p:
            return p
    for p in PSEUDONYMS:
        i = 0
        while True:
            i = text.find(p, i)
            if i < 0:
                break
            if i <= start < i + len(p):
                return p
            i += 1
    return None

def scan_file(path, cjk, lat, label):
    text = io.open(path, encoding='utf-8').read()
    spans = exempt_spans(text)
    hits = []
    for w in cjk:
        i = 0
        while True:
            i = text.find(w, i)
            if i < 0:
                break
            line = text.count('\n', 0, i) + 1
            if in_exempt(i, spans):
                st = 'EXEMPT'
            else:
                p = wrapped_pseudonym(text, i, i + len(w))
                st = f'SUBSTR(包裹化名:{p})' if p else 'VIOLATION'
            hits.append((line, w, st))
            i += len(w)
    for w in lat:
        pat = re.compile(r'(?<![A-Za-z])' + re.escape(w) + r'(?![A-Za-z])', re.IGNORECASE)
        for m in pat.finditer(text):
            line = text.count('\n', 0, m.start()) + 1
            if in_exempt(m.start(), spans):
                st = 'EXEMPT'
            else:
                st = 'VIOLATION'
            hits.append((line, m.group(0), st))
    return label, hits

def main():
    cjk, lat = load_dict()
    files = []
    for root, _, fs in os.walk(PER):
        for f in fs:
            if f.endswith('.md'):
                files.append((os.path.join(root, f), 'perspective真源'))
    # genre-library 挂载列区（主件注记行＋条目表所在四节区）
    files.append((os.path.join(SKL, 'skills', 'aigc-video-content', 'references', 'genre-library.md'), '挂载列·主件(全文·词典仅指挂载列语义区,真名词典在通识文本天然零命中,如实全扫)'))
    files.append((os.path.join(SKL, 'skills', 'aigc-video-content', 'references', 'genre-recipe-entries.md'), '挂载列·条目表+注记(全文全扫)'))
    # 两壳 ⛓ 注记行（仅注记行入扫描面）
    shell_marks = {
        os.path.join(EXP, 'workbuddy', 'baigong-video-team', 'agents', 'aigc-screenwriter.md'): '挂载',
        os.path.join(EXP, 'workbuddy', 'baigong-video-team', 'agents', 'aigc-operations.md'): '挂载',
    }
    total_v = total_s = total_e = 0
    print(f'词典：CJK {len(cjk)} 词／拉丁 {len(lat)} 词（词边界）')
    for path, label in sorted(files):
        lab, hits = scan_file(path, cjk, lat, label)
        rel = os.path.relpath(path, 'D:/')
        if not hits:
            continue
        for line, w, st in sorted(hits):
            tag = 'E' if st == 'EXEMPT' else ('S' if st.startswith('SUBSTR') else 'V')
            if tag == 'E':
                total_e += 1
            elif tag == 'S':
                total_s += 1
            else:
                total_v += 1
            print(f'[{tag}] {rel}:{line}  「{w}」  {st}')
    # 两壳注记行
    for path, kw in shell_marks.items():
        text = io.open(path, encoding='utf-8').read()
        rel = os.path.relpath(path, 'D:/')
        for n, ln in enumerate(text.splitlines(), 1):
            if kw in ln and '⛓' in ln or ('视角镜片' in ln):
                body = ln
                hits = [w for w in cjk if w in body] + [w for w in lat if re.search(r'(?<![A-Za-z])' + re.escape(w) + r'(?![A-Za-z])', body, re.I)]
                for w in hits:
                    p = wrapped_pseudonym(body, body.find(w), 0) if re.search(r'[\u4e00-\u9fff]', w) else None
                    st = f'SUBSTR(包裹化名:{p})' if p else 'VIOLATION'
                    print(f'[{"S" if st.startswith("SUBSTR") else "V"}] {rel}:{n}  「{w}」  {st} (壳⛓注记行)')
                    if st == 'VIOLATION':
                        total_v += 1
                    else:
                        total_s += 1
    print(f'—— 分账：EXEMPT(豁免面命中·绿)={total_e}  SUBSTR(子串误触·判非残留)={total_s}  VIOLATION(扫描面真名直书)={total_v}')
    sys.exit(1 if total_v else 0)

if __name__ == '__main__':
    main()
