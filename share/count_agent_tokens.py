#!/usr/bin/env python3
# share/count_agent_tokens.py · 口径 v1（CJK≈1 token/字、非 CJK≈4 字符/token）
# 口径具名：script-v1；取整方式：ceil（上取整）。
# 引用本脚本读数时必须申报四要素：口径版本 script-v1 ＋ 被测 commit SHA ＋ 实测人 ＋ 取整方式 ceil。
import os, re, sys, glob
CJK = r'[\u3400-\u4dbf\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]'
RED_LINE = 2500
def tokens(text: str) -> int:
    cjk = len(re.findall(CJK, text))
    return cjk + -(-(len(text) - cjk) // 4)      # ceil(非CJK/4)
if __name__ == '__main__':
    # 拆仓（2026-10-26）＋ T2 三仓口径：默认扫三仓 agents——
    #   experts 仓（video bundle）＋ devkits 仓（deliverables/experts/ 下软开 bundle）；
    #   skills 仓无 agents，不入 glob。三仓须并列同一父目录（D:\）。
    # 显式传 argv[1] 时按单 glob 覆盖（旧行为不变）。
    # DEBTCLN-R5 红线参数化：--limit 整数值运行时覆盖红线；默认＝行 7 RED_LINE＝2500（皮总 10-25 拍板值不变）。
    if '--limit' in sys.argv:
        _i = sys.argv.index('--limit')
        if _i + 1 >= len(sys.argv):
            sys.exit('count_agent_tokens: --limit 后须整数值')
        RED_LINE = int(sys.argv[_i + 1])
        del sys.argv[_i:_i + 2]
    if len(sys.argv) > 1:
        pats = [sys.argv[1]]
    else:
        pats = ['../multi-agent-collab-experts/workbuddy/*/agents/*.md',
                'deliverables/experts/*/agents/*.md']
    bad = 0
    seen = set()
    for pat in pats:
        for p in sorted(glob.glob(pat, recursive=True)):
            ap = os.path.abspath(p)
            if ap in seen:
                continue
            seen.add(ap)
            t = tokens(open(p, encoding='utf-8').read())
            flag = 'OK ' if t <= RED_LINE else 'OVER'
            bad += t > RED_LINE
            print(f'{flag} {t:6d}  {p}')
    sys.exit(1 if bad else 0)
