#!/usr/bin/env bash
# P5 事件并发时序（架构设计 v2.9 §10 L196 词条原句摘录·SWB-T01 T01-A）
# 标的：多席位并发工具事件下，hook 事件（PreToolUse 等）的到达顺序/隔离性是否可依赖。
# 退出码约定：0＝探针完整跑完且产出合法状态行；非0＝探针执行失败。
set -u
EVID_DIR="${EVID_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/swb-t01-p5-XXXXXX")}"
OUT="$EVID_DIR/p5.out"

find_bundle() {
  local c
  for c in "$HOME/AppData/Local/Programs/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs" \
           "$HOME/AppData/Roaming/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs"; do
    [ -f "$c" ] && { printf '%s' "$c"; return 0; }
  done
  return 1
}

{
  echo "P5 事件并发时序 实测 $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  MJS=$(find_bundle) || { echo "OBSERVATION: 平台 CLI 打包件未找到（无运行环境）"; echo "STATUS: inconclusive"; exit 0; }
  echo "bundle=$MJS"
  echo "--- 并发隔离相关代码面读数（call_id 作用域缓存/per-session 状态）---"
  python3 - "$MJS" <<'PY'
import sys,re
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
for pat in ['preToolUseHookResults','toolPermissionDecisionSnapshots','_toolStartTimes','cachePreToolUseResult']:
    print(pat, '=', len(re.findall(pat,src)))
m=re.search(r'cacheKeys=\$\{Array\.from\(I\.preToolUseHookResults.{0,120}',src,re.S)
print('SESSION-SCOPED-CACHE:',m.group(0)[:180] if m else 'NOT FOUND')
print('NOTE: 代码面显示 hook 结果按 session+call_id 键控缓存＝事件按调用隔离；跨席位事件的全局到达顺序无任何串行化承诺可 grep 到。')
PY
  echo "OBSERVATION: 跨席位并发事件的时序保证属运行期性质，脚本侧无法构造两席同刻工具事件（需活跃团队运行态）；代码面仅有 per-session/per-call 隔离键，无全局排序闸。时序不可依赖性未被证实也未被证伪。"
  echo "STATUS: inconclusive"
} > "$OUT" 2>&1
cat "$OUT"
echo "STATUS: $(grep '^STATUS:' "$OUT" | tail -1 | cut -d' ' -f2)"
exit 0
