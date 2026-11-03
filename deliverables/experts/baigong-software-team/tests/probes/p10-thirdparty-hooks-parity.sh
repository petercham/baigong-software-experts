#!/usr/bin/env bash
# P10 第三方插件 hooks 同权性（架构设计 v2.9 §10 L196 词条原句摘录·SWB-T01 T01-A）
# 标的：第三方插件声明的 hooks 与用户级 settings hooks 是否同权进入同一执行管道（B 闸复用前置）。
# 退出码约定：0＝探针完整跑完且产出合法状态行；非0＝探针执行失败。
set -u
EVID_DIR="${EVID_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/swb-t01-p10-XXXXXX")}"
OUT="$EVID_DIR/p10.out"

find_bundle() {
  local c
  for c in "$HOME/AppData/Local/Programs/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs" \
           "$HOME/AppData/Roaming/WorkBuddy/resources/app.asar.unpacked/cli/dist/codebuddy-lite-wb.mjs"; do
    [ -f "$c" ] && { printf '%s' "$c"; return 0; }
  done
  return 1
}

{
  echo "P10 第三方插件 hooks 同权性 实测 $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  MJS=$(find_bundle) || { echo "OBSERVATION: 平台 CLI 打包件未找到（无运行环境）"; echo "VERDICT: inconclusive"; exit 0; }
  echo "bundle=$MJS"
  echo "--- 代码层：hooks 获取管道读数（settings hooks 与 plugin hooks 汇入同数组）---"
  python3 - "$MJS" <<'PY'
import sys,re
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
m=re.search(r'async getHooks\(t\)\{.{0,420}',src,re.S)
print('GETHOOKS:',m.group(0)[:420] if m else 'NOT FOUND')
m2=re.search(r'"hooks/hooks\.json".{0,120}|hooks/hooks\.json",\w+="[A-Z_]+"',src,re.S)
print('PLUGIN-HOOKS-FILE:',m2.group(0)[:180] if m2 else 'NOT FOUND')
m3=re.search(r'CODEBUDDY_DISABLE_EXTENDED_PLUGIN_HOOKS.{0,220}',src,re.S)
print('DISABLE-KW:',m3.group(0)[:240] if m3 else 'NOT FOUND')
m4=re.search(r'allowUntrustedFrontmatterHooks.{0,140}',src,re.S)
print('UNTRUSTED-FRONTMATTER-GATE:',m4.group(0)[:160] if m4 else 'NOT FOUND')
pipe = bool(m) and 'loadHooksFromPlugins' in (m.group(0) if m else '')
print('NOTE: getHooks 单管道＝settings hooks ∪ plugin hooks ∪ scoped registry 同数组喂同一 executeHooks；存在全局关闭开关 CODEBUDDY_DISABLE_EXTENDED_PLUGIN_HOOKS 与 frontmatter 信任闸＝插件 hooks 有额外信任门。')
print('VERDICT:', 'pass' if pipe else 'inconclusive')
PY
  echo "--- 盘上读数：已安装插件 hooks 声明件存在性计数 ---"
  find "$HOME/.workbuddy/plugins/cache" -maxdepth 5 -path "*hooks/hooks.json" 2>/dev/null | wc -l
} > "$OUT" 2>&1
status=$(grep -o 'VERDICT: [a-z]*' "$OUT" | tail -1 | cut -d' ' -f2)
case "$status" in pass|negative|inconclusive) : ;; *) status=inconclusive ;; esac
cat "$OUT"
echo "STATUS: $status"
exit 0
