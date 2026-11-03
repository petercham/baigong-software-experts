#!/usr/bin/env bash
# T02-A · B0 账本初始化（主路/退路双形）
# 规范锚点：架构 v2.9 §9 B0 行（V13 L154）／§3 主信任锚（V13 L141）／§11 账本 git 服务承载＝人类侧自建（V13 L174）
# 形态取数：P7（git 独立服务可建性）实测读数——读数源＝同包 tests/probes/results/probe-results.json（交付树件）
#   P7 = pass     → 主路：独立 git 服务初始化＝远端裸仓＋receive.denyNonFastForwards=true＋receive.denyDeletes=true＋保护分支配置
#   P7 = negative → 退路：本地裸仓＋三重保证待补位声明行（PreToolUse 拦截实体在 T04，本脚本只留配置锚）
# 主信任锚＝git 原生哈希链（§3/§17）；记录级前向哈希 prev_hash 仅供单记录独立校验（§17 前向哈希词条）。
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"                      # deliverables/experts/baigong-software-team
PROBE_RESULTS="$PACK_ROOT/tests/probes/results/probe-results.json"  # P7 读数源（票面：默认取数走主路）

# 账本根：缺省＝仓根 .collab/ledger/（§9 B0 行「仓内镜像居 .collab/ledger/」）；测试可经环境变量重定向
LEDGER_ROOT="${SWB_LEDGER_ROOT:-$PWD/.collab/ledger}"
LEDGER_FILE="$LEDGER_ROOT/ledger.jsonl"      # 六类记录（派发/写入/签字/注入包哈希/intake 登记/呈报，§3）
LEASE_FILE="$LEDGER_ROOT/leases.jsonl"       # 租约台账（B2 签发输出入账，§9 B2 行）

# ---- P7 读数取数（缺档或非 negative 一律按主路，与主理人放行口径一致） ----
P7_STATUS="$(python - "$PROBE_RESULTS" <<'PY'
import json, sys
try:
    d = json.load(open(sys.argv[1], encoding="utf-8"))
    print(d.get("P7", {}).get("status", "missing"))
except Exception:
    print("missing")
PY
)"

mkdir -p "$LEDGER_ROOT"
touch "$LEDGER_FILE" "$LEASE_FILE"

if [ "$P7_STATUS" = "negative" ]; then
  # ---- 退路形态（§9 B0 退路行）----
  git init --bare "$LEDGER_ROOT/ledger-local-bare.git" >/dev/null
  cat > "$LEDGER_ROOT/fallback-config-anchor.json" <<'JSON'
{
  "form": "fallback",
  "clause": "架构v2.9 §9 B0 退路行（V13 L154）",
  "pending_guarantees": [
    "PreToolUse 拦 force-push/amend（拦截实体＝T04 B5）",
    "异地镜像（承载者＝人类侧·§11，配置细节＝候裁 Q-02 呈人类）",
    "日终对账（reconcile-daily.py 承接）"
  ],
  "note": "三重保证失效任一→审计事件→呈报人类（§9 承重闸声明）"
}
JSON
  echo "B0_FORM=fallback"
  echo "三重保证待补位声明：PreToolUse 拦 force-push/amend（T04 hooks 实体）＋异地镜像＋日终对账补位；本脚本只留配置锚 $LEDGER_ROOT/fallback-config-anchor.json"
else
  # ---- 主路形态（P7 pass；缺档亦按主路，实测 P7=pass 已登记）----
  REMOTE="${SWB_LEDGER_REMOTE:-$LEDGER_ROOT/ledger-remote.git}"
  git init --bare "$REMOTE" >/dev/null
  git -C "$REMOTE" config receive.denyNonFastForwards true
  git -C "$REMOTE" config receive.denyDeletes true
  # 保护分支配置：裸仓侧以 pre-receive 钩子承载（拒删受保护分支/拒对其非快进更新；拒非快进另由 denyNFF 全局兜底）
  cat > "$REMOTE/hooks/pre-receive" <<'HOOK'
#!/usr/bin/env bash
# B0 主路保护分支配置（架构 v2.9 §9 B0 行；零裁量机械判定）
PROTECTED_REFS="refs/heads/main refs/heads/master"
ZERO="0000000000000000000000000000000000000000"
while read -r oldv newv ref; do
  for p in $PROTECTED_REFS; do
    if [ "$ref" = "$p" ]; then
      if [ "$newv" = "$ZERO" ]; then
        echo "pre-receive: deny delete of protected branch $ref" >&2
        exit 1
      fi
    fi
  done
done
exit 0
HOOK
  chmod +x "$REMOTE/hooks/pre-receive"
  echo "B0_FORM=main"
  echo "B0_LEDGER_ROOT=$LEDGER_ROOT"
  echo "B0_REMOTE=$REMOTE"
  echo "B0_P7_STATUS=$P7_STATUS"
  echo "receive.denyNonFastForwards=$(git -C "$REMOTE" config --get receive.denyNonFastForwards)"
  echo "receive.denyDeletes=$(git -C "$REMOTE" config --get receive.denyDeletes)"
  echo "protected_branch_hook=$([ -x "$REMOTE/hooks/pre-receive" ] && echo installed || echo missing)"
fi

echo "LEDGER_FILE=$LEDGER_FILE"
echo "LEASE_FILE=$LEASE_FILE"
