#!/usr/bin/env bash
# P3 工具声明生效范围（架构设计 v2.9 §10 L196 词条原句摘录·SWB-T01 T01-A）
# 标的：tools/disallowedTools 声明的生效范围（进程级/会话级/子席位继承）。
# 退出码约定：0＝探针完整跑完且产出合法状态行；非0＝探针执行失败。
set -u
EVID_DIR="${EVID_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/swb-t01-p3-XXXXXX")}"
OUT="$EVID_DIR/p3.out"

find_bundle() {
  local c
  for c in "$HOME/AppData/Local/Programs/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs" \
           "$HOME/AppData/Roaming/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs"; do
    [ -f "$c" ] && { printf '%s' "$c"; return 0; }
  done
  return 1
}

{
  echo "P3 工具声明生效范围 实测 $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  MJS=$(find_bundle) || { echo "OBSERVATION: 平台 CLI 打包件未找到"; echo "STATUS: inconclusive"; exit 0; }
  echo "bundle=$MJS"
  echo "--- token 计数 ---"
  for t in '\-\-tools' 'allowedTools' 'disallowedTools'; do printf '%s=' "$t"; grep -c "$t" "$MJS"; done
  echo "--- 子席位继承逻辑摘录（主会话∪agent配置 disallowedTools 并集）---"
  python3 - "$MJS" <<'PY'
import sys,re
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
m=re.search(r'this\.mainSession\.options\.disallowedTools\?\?.{0,220}',src,re.S)
print('INHERIT:',m.group(0)[:240] if m else 'NOT FOUND')
m2=re.search(r'--tools.{0,200}',src,re.S)
print('--tools-scope:',m2.group(0)[:200] if m2 else 'NOT FOUND')
m3=re.search(r'Optional frontmatter: `tools` / `disallowedTools`[^\\]*',src,re.S)
print('AGENT-FRONTMATTER:',m3.group(0)[:240] if m3 else 'NOT FOUND')
ok = bool(m)
print('VERDICT:', 'pass' if ok else 'inconclusive')
PY
} > "$OUT" 2>&1
status=$(grep -o 'VERDICT: [a-z]*' "$OUT" | tail -1 | cut -d' ' -f2)
case "$status" in pass|negative|inconclusive) : ;; *) status=inconclusive ;; esac
cat "$OUT"
echo "STATUS: $status"
exit 0
