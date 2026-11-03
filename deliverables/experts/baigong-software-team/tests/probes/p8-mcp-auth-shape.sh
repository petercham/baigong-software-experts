#!/usr/bin/env bash
# P8 MCP auth 形态（问句，无预设）（架构设计 v2.9 §10 L196 词条原句摘录·SWB-T01 T01-A）
# 纪律（票面钉死）：本探针只登记观测，不得预填结论；任何 [未验证:P8] 能力不得作脚本内闸前提。
# 探针内不设置 pass/negative 判定逻辑——状态固定为 inconclusive（问句无预设），全部信息以观测读数形态落盘。
# 退出码约定：0＝探针完整跑完且产出合法状态行；非0＝探针执行失败。
set -u
EVID_DIR="${EVID_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/swb-t01-p8-XXXXXX")}"
OUT="$EVID_DIR/p8.out"

find_bundle() {
  local c
  for c in "$HOME/AppData/Local/Programs/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs" \
           "$HOME/AppData/Roaming/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs"; do
    [ -f "$c" ] && { printf '%s' "$c"; return 0; }
  done
  return 1
}

{
  echo "P8 MCP auth 形态 观测登记 $(date -u +%Y-%m-%dT%H:%M:%SZ)（问句无预设·只登记观测）"

  echo "--- 观测①：盘上 MCP 配置形态（用户级 mcp.json·键形态，不抄凭据值）---"
  MCPJ="$HOME/.workbuddy/mcp.json"
  if [ -f "$MCPJ" ]; then
    echo "mcp.json exists size=$(wc -c < "$MCPJ")"
    echo "top-keys:"; grep -o '"[A-Za-z]*"[[:space:]]*:' "$MCPJ" | sort -u
    echo "server-names:"; grep -o '"[a-z0-9-]*-mcp"\|"[a-z0-9-]*":' "$MCPJ" | head -10
    echo "credential-field-presence-scan:"; grep -c -i 'key\|token\|secret\|authorization' "$MCPJ" || true
  else
    echo "mcp.json 不存在"
  fi

  echo "--- 观测②：审批留痕文件形态（mcp-approvals.json·仅键形态）---"
  APJ="$HOME/.workbuddy/mcp-approvals.json"
  if [ -f "$APJ" ]; then
    echo "mcp-approvals.json exists size=$(wc -c < "$APJ") entries=$(grep -o '::' "$APJ" | wc -l)"
    echo "key-shape-sample:"; grep -o '"[0-9a-f]\{16\}' "$APJ" | head -2
  else
    echo "mcp-approvals.json 不存在"
  fi

  echo "--- 观测③：打包件内 auth 相关词面计数（不判义）---"
  MJS=$(find_bundle) || { echo "bundle 未找到（观测缺项）"; echo "STATUS: inconclusive"; exit 0; }
  echo "bundle=$MJS"
  python3 - "$MJS" <<'PY'
import sys,re
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
for pat in [r'[Oo][Aa]uth', r'authorization', r'headers', r'mcp[_A-Za-z]*[Aa]uth', r'api[_Kk]ey', r'bearer', r'apiVersion|env\.(MCP|API)']:
    print(pat, '=', len(re.findall(pat,src)))
m=re.search(r'".{0,60}mcp-approvals\.json"',src,re.S)
print('approvals-file-literal:', m.group(0) if m else 'NOT FOUND')
PY
  echo "OBSERVATION-ONLY: 以上为形态观测读数，不含结论预设。P8 问句答案由消费面票（候裁单列 Q-03）据读数裁定。"
  echo "STATUS: inconclusive"
} > "$OUT" 2>&1
cat "$OUT"
echo "STATUS: $(grep '^STATUS:' "$OUT" | tail -1 | cut -d' ' -f2)"
exit 0
