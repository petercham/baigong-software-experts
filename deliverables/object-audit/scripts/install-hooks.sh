#!/usr/bin/env bash
# --- spec-provenance v1 ---
# spec_id: MC-HOOK-1
# spec_file: deliverables/multi-collab/references/60-gates.md
# spec_anchor: - 安装器**幂等**
# spec_clause_sha256: 9e568722577b7ca9b2d6cb5dae54f6115c468bfc102157e9e5d04efc0f74f797
# spec_version: 3.9
# spec_effective: 2026-10-23
# provider: multi-collab
# --- /spec-provenance ---
#
# 钩子安装器（幂等装 .git/hooks/pre-commit）。规范来源：设计 v2 §2.5/60-gates。
#
# 三条照抄规范的行为约束（不复写正文，只指路径）：
#   幂等／不覆盖已有钩子 → deliverables/multi-collab/references/60-gates.md「七、接入」
#   钩子文件本身不入仓（入仓的是本安装器） → 同上「一、三个出口」段末
#   钩子内用显式解释器调用（不依赖可执行位） → 同上「七、接入」第 2 条
#
# 退出码（本件是安装器，不是检查器；语义与检查脚本的闭集对齐但不含 3）：
#   0 已安装／本来就是最新  1 已存在他人钩子，未覆盖，需人工合并
#   2 用法错  4 基础设施错（找不到 git 仓／找不到 bash／找不到门禁入口）

set -u

# 显式解释器：本文件自身用 `bash` 调起，写进钩子的命令也一律带解释器名。
SELF_DIR="$(cd "$(dirname "$0")" && pwd)"
RUNNER="$SELF_DIR/run-gates.sh"

say() { printf '%s\n' "$*"; }
die_usage() { printf 'usage error: %s\n' "$*" >&2; exit 2; }
die_infra() { printf 'infra error: %s\n' "$*" >&2; exit 4; }

# --- 参数：只接受 --root（其余一律用法错，不猜） ---
ROOT_ARG=""
while [ $# -gt 0 ]; do
  case "$1" in
    --root) [ $# -ge 2 ] || die_usage "--root 需要一个目录参数"; ROOT_ARG="$2"; shift 2 ;;
    -h|--help)
      say "用法：bash install-hooks.sh [--root <仓根>]"
      say "幂等安装 .git/hooks/pre-commit；已存在非本器生成的钩子时不覆盖，提示人工合并。"
      exit 0 ;;
    *) die_usage "未知参数：$1" ;;
  esac
done

# --- 定位 git 仓根 ---
if [ -n "$ROOT_ARG" ]; then
  [ -d "$ROOT_ARG" ] || die_usage "--root 不存在：$ROOT_ARG"
  REPO_ROOT="$(cd "$ROOT_ARG" && pwd)"
elif command -v git >/dev/null 2>&1; then
  REPO_ROOT="$(git -C "$SELF_DIR" rev-parse --show-toplevel 2>/dev/null)" \
    || die_infra "当前目录不在 git 仓内，无法定位 .git/hooks"
  [ -n "$REPO_ROOT" ] || die_infra "git rev-parse 未返回仓根"
else
  die_infra "找不到 git，且未给 --root"
fi

HOOKS_DIR="$REPO_ROOT/.git/hooks"
HOOK="$HOOKS_DIR/pre-commit"
[ -d "$HOOKS_DIR" ] || die_infra "钩子目录不存在：$HOOKS_DIR"
[ -f "$RUNNER" ] || die_infra "找不到门禁入口脚本：$RUNNER"

# 本器生成的钩子内容。标记行用于区分"本器装的"与"别人装的"。
MARKER="generated-by: object-audit/scripts/install-hooks.sh"
GATE_HOOK_BODY="#!/usr/bin/env bash
# ${MARKER}
# 提交前门禁（出口①）。规范来源：设计 v2 §2.5/60-gates。
# 改判据请改 deliverables/multi-collab/references/60-gates.md 的路由表，不要改本文件。
set -u
exec bash \"$RUNNER\" --root \"$REPO_ROOT\"
"

write_hook() {
  printf '%s\n' "$GATE_HOOK_BODY" > "$HOOK" || die_infra "写入钩子失败：$HOOK"
  # 权限位尽力而为：规范明写钩子内用显式解释器调用，**不依赖可执行位**
  # （部分文件系统权限位不具区分力，靠它会把"装不上"伪装成"已装好"）。
  chmod +x "$HOOK" 2>/dev/null || true
}

if [ -e "$HOOK" ]; then
  if grep -qF "$MARKER" "$HOOK" 2>/dev/null; then
    # 是本器装的：内容一致＝零差异（幂等判据），不一致＝刷新到当前版本。
    CURRENT="$(cat "$HOOK")"
    WANT="$(printf '%s\n' "$GATE_HOOK_BODY")"
    if [ "$CURRENT" = "$WANT" ]; then
      say "已是最新，未改动：$HOOK"
      exit 0
    fi
    write_hook
    say "本器钩子已刷新到当前版本：$HOOK"
    exit 0
  fi
  # 别人装的（或手工写的）：**不覆盖**，提示人工合并。
  say "已存在非本器生成的 pre-commit，未覆盖：$HOOK"
  say "请人工把下面这段并进去（覆盖＝悄悄删掉别人装的东西）："
  say "-----8<-----"
  printf '%s\n' "$GATE_HOOK_BODY"
  say "-----8<-----"
  exit 1
fi

write_hook
say "已安装 pre-commit 钩子：$HOOK"
say "入口：bash $RUNNER"
exit 0
