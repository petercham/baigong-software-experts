#!/usr/bin/env bash
# P6 deny 跨席位一致性（架构设计 v2.9 §10 L196 词条原句摘录·SWB-T01 T01-A）
# 标的：PreToolUse hook 返回 deny 时，该拒绝是否对所有席位一致生效（同一 hook 源、同决策词表）。
# 退出码约定：0＝探针完整跑完且产出合法状态行；非0＝探针执行失败。
set -u
EVID_DIR="${EVID_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/swb-t01-p6-XXXXXX")}"
OUT="$EVID_DIR/p6.out"

find_bundle() {
  local c
  for c in "$HOME/AppData/Local/Programs/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs" \
           "$HOME/AppData/Roaming/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs"; do
    [ -f "$c" ] && { printf '%s' "$c"; return 0; }
  done
  return 1
}

{
  echo "P6 deny 跨席位一致性 实测 $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  MJS=$(find_bundle) || { echo "OBSERVATION: 平台 CLI 打包件未找到（无运行环境）"; echo "STATUS: inconclusive"; exit 0; }
  echo "bundle=$MJS"
  echo "--- deny 决策词表＋调用点读数（§19 PreToolUse 决策词表行）---"
  python3 - "$MJS" <<'PY'
import sys,re
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
print('permissionDecision count =',len(re.findall('permissionDecision',src)))
sites=[m.start() for m in re.finditer(r'executePreToolUseHooks\(',src)]
print('executePreToolUseHooks call/def sites =',len(sites))
m=re.search(r'"deny"===ev\.permissionDecision.{0,200}',src,re.S)
print('DENY-SITE-MCP:',m.group(0)[:200] if m else 'NOT FOUND')
m2=re.search(r'if\(!N\.allowed\)\{.{0,180}',src,re.S)
print('DENY-SITE-MAIN:',m2.group(0)[:180] if m2 else 'NOT FOUND')
m3=re.search(r'allowUntrustedFrontmatterHooks.{0,120}',src,re.S)
print('UNTRUSTED-GATE:',m3.group(0)[:150] if m3 else 'NOT FOUND')
print('NOTE: 主工具路径与 MCP 工具路径共用同一 executePreToolUseHooks 决策管道＝单管道同词表（代码面）；跨席位（多 in-process 会话）是否同获同一 deny 需运行期双席实测，脚本侧无法触发。')
PY
  echo "OBSERVATION: 代码面＝deny 词表与决策管道单源；跨席位一致性运行期未验证（无法在探针内并行起两席并触发同 matcher）。"
  echo "STATUS: inconclusive"
} > "$OUT" 2>&1
cat "$OUT"
echo "STATUS: $(grep '^STATUS:' "$OUT" | tail -1 | cut -d' ' -f2)"
exit 0
