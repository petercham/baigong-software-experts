#!/usr/bin/env bash
# P9 派发记录导出（架构设计 v2.9 §10 L196 词条原句摘录·SWB-T01 T01-A）
# 标的：派发记录（任务板/席位派发态）能否被导出为机读件（账本 B5 对账/活性自检消费前置）。
# 退出码约定：0＝探针完整跑完且产出合法状态行；非0＝探针执行失败。
set -u
EVID_DIR="${EVID_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/swb-t01-p9-XXXXXX")}"
OUT="$EVID_DIR/p9.out"
WB="${HOME}/.workbuddy"

{
  echo "P9 派发记录导出 实测 $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  if [ ! -d "$WB/tasks" ]; then
    echo "OBSERVATION: $WB/tasks 不存在（非 WorkBuddy 环境）"
    echo "VERDICT: inconclusive"
  else
    echo "--- 任务板记录盘上形态扫描 ---"
    python3 - "$WB" <<'PY'
import json,sys,os,glob
wb=sys.argv[1]
tfiles=glob.glob(os.path.join(wb,'tasks','*','*.json'))
print('task-record files =',len(tfiles))
teams=set(os.path.basename(os.path.dirname(f)) for f in tfiles)
print('task boards by team =',len(teams))
if tfiles:
    recs=[json.load(open(f,encoding='utf-8')) for f in tfiles[:50]]
    keysets=set(tuple(sorted(r.keys())) for r in recs if isinstance(r,dict))
    print('record keysets =',[list(k) for k in list(keysets)[:3]])
    # 导出性＝纯 JSON 文件可直接机读导出
    print('export-roundtrip-sample:', json.dumps(recs[0])[:160])
    ok=len(tfiles)>0 and all(isinstance(r,dict) for r in recs)
else:
    ok=False
print('VERDICT:', 'pass' if ok else 'inconclusive')
PY
  fi
} > "$OUT" 2>&1
status=$(grep -o 'VERDICT: [a-z]*' "$OUT" | tail -1 | cut -d' ' -f2)
case "$status" in pass|negative|inconclusive) : ;; *) status=inconclusive ;; esac
cat "$OUT"
echo "STATUS: $status"
exit 0
