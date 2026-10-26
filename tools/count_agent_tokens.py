#!/usr/bin/env python3
# tools/count_agent_tokens.py · 口径 v1（CJK≈1 token/字、非 CJK≈4 字符/token）
# 口径具名：script-v1；取整方式：ceil（上取整）。
# 引用本脚本读数时必须申报四要素：口径版本 script-v1 ＋ 被测 commit SHA ＋ 实测人 ＋ 取整方式 ceil。
import re, sys, glob
CJK = r'[\u3400-\u4dbf\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]'
RED_LINE = 2500
def tokens(text: str) -> int:
    cjk = len(re.findall(CJK, text))
    return cjk + -(-(len(text) - cjk) // 4)      # ceil(非CJK/4)
if __name__ == '__main__':
    # 拆仓（2026-10-26）：专家包在姊妹仓 multi-collab-agent-experts（须并列同一父目录）
    pat = sys.argv[1] if len(sys.argv) > 1 else '../multi-collab-agent-experts/workbuddy/*/agents/*.md'
    bad = 0
    for p in sorted(glob.glob(pat, recursive=True)):
        t = tokens(open(p, encoding='utf-8').read())
        flag = 'OK ' if t <= RED_LINE else 'OVER'
        bad += t > RED_LINE
        print(f'{flag} {t:6d}  {p}')
    sys.exit(1 if bad else 0)
