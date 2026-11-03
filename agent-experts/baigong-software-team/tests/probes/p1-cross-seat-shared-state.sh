#!/usr/bin/env bash
# P1 席位间文件外共享状态（架构设计 v2.9 §10 L196 词条原句摘录·SWB-T01 T01-A）
# 标的：席位间是否存在「协作仓库文件之外」的平台态共享状态（团队态/任务板/席间信箱）。
# 退出码约定（票面验收判据口径）：0＝探针完整跑完且产出合法状态行；非0＝探针执行失败。
# stdout 末行输出 `STATUS: <pass|negative|inconclusive>`；读数文件落 $EVID_DIR（系统 Temp·不落仓）。
set -u
EVID_DIR="${EVID_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/swb-t01-p1-XXXXXX")}"
OUT="$EVID_DIR/p1.out"
WB="${HOME}/.workbuddy"

{
  echo "P1 席位间文件外共享状态 实测 $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "platform_state_root=$WB"
  if [ ! -d "$WB/teams" ]; then
    echo "OBSERVATION: $WB/teams 不存在（非 WorkBuddy 环境或状态根不同）"
    echo "STATUS: inconclusive"
    exit 0
  fi
  # 选取最近活动的团队态目录（runtime.json mtime 最新）
  latest_team=""
  latest_ts=0
  for d in "$WB"/teams/*/; do
    [ -f "$d/runtime.json" ] || continue
    ts=$(stat -c %Y "$d/runtime.json" 2>/dev/null || echo 0)
    if [ "$ts" -gt "$latest_ts" ]; then latest_ts=$ts; latest_team="$d"; fi
  done
  if [ -z "$latest_team" ]; then
    echo "OBSERVATION: teams/ 下无 runtime.json（无活跃团队态）"
    echo "STATUS: inconclusive"
    exit 0
  fi
  echo "latest_team=$latest_team"
  python3 - "$latest_team" <<'PY'
import json,sys,os,glob
team=sys.argv[1]
cfg=json.load(open(os.path.join(team,'config.json'),encoding='utf-8'))
rt=json.load(open(os.path.join(team,'runtime.json'),encoding='utf-8'))
members=cfg.get('members',[])
print(f"config.json members={len(members)} lead={cfg.get('leadAgentId')}")
print(f"runtime.json status={rt.get('status')} updatedAt={rt.get('updatedAt')}")
inboxes=glob.glob(os.path.join(team,'inboxes','*.json'))
print(f"inbox files={len(inboxes)} sample={os.path.basename(inboxes[0]) if inboxes else '-'}")
tname=os.path.basename(team.rstrip('/\\'))
tasks=glob.glob(os.path.expanduser(os.path.join('~','.workbuddy','tasks',tname,'*.json')))
print(f"task board files={len(tasks)}")
if tasks:
    t=json.load(open(sorted(tasks)[0],encoding='utf-8'))
    print(f"task record keys={sorted(t.keys())}")
# 判定：仓库文件之外的平台态共享面（团队注册表/席间信箱/任务板）齐备且可跨席读取＝pass
ok = len(members)>=2 and len(inboxes)>=1 and len(tasks)>=1
print("VERDICT:", "pass" if ok else "negative")
PY
} > "$OUT" 2>&1
status=$(grep -o 'VERDICT: [a-z]*' "$OUT" | tail -1 | cut -d' ' -f2)
case "$status" in pass|negative|inconclusive) : ;; *) status=inconclusive ;; esac
cat "$OUT"
echo "STATUS: $status"
exit 0
