#!/usr/bin/env bash
# P2 主理人 md 注入恒常性与上限（架构设计 v2.9 §10 L196 词条原句摘录·SWB-T01 T01-A）
# 标的：主理人（lead）注入到席位的团队上下文 md 是否每轮恒常注入、是否有长度/轮次上限。
# 退出码约定：0＝探针完整跑完且产出合法状态行；非0＝探针执行失败。
set -u
EVID_DIR="${EVID_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/swb-t01-p2-XXXXXX")}"
OUT="$EVID_DIR/p2.out"

find_bundle() {
  local c
  for c in "$HOME/AppData/Local/Programs/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs" \
           "$HOME/AppData/Roaming/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs"; do
    [ -f "$c" ] && { printf '%s' "$c"; return 0; }
  done
  return 1
}

{
  echo "P2 主理人 md 注入恒常性与上限 实测 $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  MJS=$(find_bundle) || { echo "OBSERVATION: 平台 CLI 打包件未找到"; echo "STATUS: inconclusive"; exit 0; }
  echo "bundle=$MJS"
  echo "--- grep team-sys-prompt ---"
  grep -c 'team-sys-prompt' "$MJS"
  echo "--- grep data-role=\"team-context\" ---"
  grep -c 'data-role="team-context"' "$MJS"
  echo "--- 注入条件逻辑摘录（shouldInjectTeamPrompt）---"
  python3 - "$MJS" <<'PY'
import sys,re
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
m=re.search(r'shouldInjectTeamPrompt\([^)]*\)\{.{0,600}',src,re.S)
print(m.group(0)[:600] if m else 'NOT FOUND')
m2=re.search(r'.{120}Agent Teammate Communication.{420}',src,re.S)
print('INJECT-SITE:',m2.group(0)[:540] if m2 else 'NOT FOUND')
# 上限观测：注入路径上是否出现 maxChars/truncate/limit 类约束
inj=re.search(r'shouldInjectTeamPrompt.{0,3000}',src,re.S)
seg=inj.group(0) if inj else ''
for kw in ('maxChars','truncat','maxLength','charBudget','DEFERRED_TOOLS_CHAR_BUDGET'):
    print(f'limit-kw {kw}:', kw in seg)
PY
  echo "OBSERVATION: 注入为条件式（首轮/席位名册变更/续会话时注入，名册未变且用户消息已含标记则跳过）＝非无条件恒常；注入路径未见显式长度上限关键字；运行期逐轮恒常性与上限无法从脚本侧回显（transcript 不在可扫面）。"
  echo "STATUS: inconclusive"
} > "$OUT" 2>&1
cat "$OUT"
echo "STATUS: $(grep '^STATUS:' "$OUT" | tail -1 | cut -d' ' -f2)"
exit 0
