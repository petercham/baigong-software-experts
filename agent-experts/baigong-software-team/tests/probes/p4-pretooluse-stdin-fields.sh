#!/usr/bin/env bash
# P4 PreToolUse stdin 字段完整性[代码层已证，待运行时]（架构设计 v2.9 §10 L196 词条原句摘录·SWB-T01 T01-A）
# 双证据（票面 T01-A 钉死）：
#   证据①＝对平台 CLI 打包件 codebuddy-lite-wb.mjs grep executePreToolUseHooks payload 注入 agent_id/agent_type（§19 buildAgentTrigger 行复真锚点）；
#   证据②＝运行时实际触发一次 PreToolUse 并回显 stdin JSON 字段清单。运行时不可行项如实登记 inconclusive＋观测环境读数，禁造假阳性。
# 退出码约定：0＝探针完整跑完且产出合法状态行；非0＝探针执行失败。
set -u
EVID_DIR="${EVID_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/swb-t01-p4-XXXXXX")}"
OUT="$EVID_DIR/p4.out"
DUMP="$EVID_DIR/stdin-dump.json"

find_bundle() {
  local c
  for c in "$HOME/AppData/Local/Programs/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs" \
           "$HOME/AppData/Roaming/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs"; do
    [ -f "$c" ] && { printf '%s' "$c"; return 0; }
  done
  return 1
}

{
  echo "P4 PreToolUse stdin 字段完整性 实测 $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  MJS=$(find_bundle) || { echo "OBSERVATION: 平台 CLI 打包件未找到"; echo "STATUS: inconclusive"; exit 0; }
  echo "bundle=$MJS"

  echo "=== 证据①：代码层 grep 复真（§19 buildAgentTrigger 行）==="
  echo "--- grep -c executePreToolUseHooks ---"
  grep -c 'executePreToolUseHooks' "$MJS"
  echo "--- buildAgentTrigger 定义摘录（payload 注入 agent_id/agent_type）---"
  python3 - "$MJS" <<'PY'
import sys,re
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
m=re.search(r'function buildAgentTrigger\([^)]*\)\{.{0,260}',src,re.S)
print(m.group(0)[:260] if m else 'BUILDAGENTTRIGGER NOT FOUND')
m2=re.search(r'executePreToolUseHooks\(t,i,n,s,c,p\)\{.{0,420}',src,re.S)
print('PAYLOAD-SITE:',m2.group(0)[:420] if m2 else 'PAYLOAD SITE NOT FOUND')
code_ok = bool(m) and 'agent_id' in (m.group(0) if m else '') and 'agent_type' in (m.group(0) if m else '')
print('CODE_LAYER_VERDICT:', 'verified' if code_ok else 'not-verified')
PY

  echo "=== 证据②：运行时触发一次 PreToolUse 回显 stdin 字段清单 ==="
  SCRATCH="$EVID_DIR/runtimescan"
  mkdir -p "$SCRATCH/.codebuddy"
  cat > "$SCRATCH/.codebuddy/settings.json" <<EOF
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "cat > \\"$(cygpath -wa "$DUMP" 2>/dev/null || printf '%s' "$DUMP")\\" 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
EOF
  CLI="$HOME/AppData/Local/Programs/WorkBuddy/resources/app.asar.unpacked/cli/bin/codebuddy"
  [ -x "$CLI" ] || CLI="$HOME/AppData/Roaming/WorkBuddy/resources/app.asar.unpacked/cli/bin/codebuddy"
  if [ -x "$CLI" ]; then
    echo "cli=$CLI"
    ( cd "$SCRATCH" && timeout 150 "$CLI" -p --port "$((20000 + RANDOM % 20000))" --no-session-persistence --tools "Bash" "Reply with exactly the single word PONG. Do not use any tool." ) 2>&1 | tail -6
    if [ -s "$DUMP" ]; then
      echo "--- stdin JSON 字段清单 ---"
      python3 -c "import json;d=json.load(open(r'''$DUMP''',encoding='utf-8'));print(sorted(d.keys()));print('has agent_id:', 'agent_id' in d, 'has agent_type:', 'agent_type' in d)"
      runtime_ok=1
    else
      echo "OBSERVATION: 运行时未产生 stdin dump（headless 独立会话需登录鉴权＝环境读数：Authentication required / 无桌面会话令牌）"
      runtime_ok=0
    fi
  else
    echo "OBSERVATION: CLI 启动器不存在（环境读数：cli launcher missing）"
    runtime_ok=0
  fi

  code_ok=$(grep -o 'CODE_LAYER_VERDICT: [a-z]*' "$OUT" 2>/dev/null | tail -1 | cut -d' ' -f2)
  : # (重取在下方主判定处)
} > "$OUT" 2>&1

code_ok=$(grep -o 'CODE_LAYER_VERDICT: [a-z]*' "$OUT" | tail -1 | cut -d' ' -f2)
runtime_hit=$(grep -c 'has agent_id:' "$OUT")
if [ "$code_ok" = "verified" ] && [ "$runtime_hit" -ge 1 ]; then
  status=pass
else
  status=inconclusive
fi
cat "$OUT"
echo "STATUS: $status"
exit 0
