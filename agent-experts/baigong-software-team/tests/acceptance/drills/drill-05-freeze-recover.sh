#!/usr/bin/env bash
# SWB-T06-D · 演练五＝停刀-恢复（§17 六名逐字·名5）
# 判据：freeze→清租约→全写 deny→解冻（人类令牌）→自计时 ≤60s。
# 落盘一律仓外 Temp；仓内零运行残留。人类令牌/校验锚＝演练面构造（Temp），不代表真实密钥根。
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PKG="$(cd "$DIR/../../.." && pwd)"
SCRIPTS="$PKG/skills/sop/scripts"
CFG="$PKG/config"
TMP="${T06_TMP:?T06_TMP 须由调用方注入（仓外 Temp·件内不落盘符）}/drill05"
rm -rf "$TMP"; mkdir -p "$TMP"
LED="$TMP/ledger.jsonl"; LEASES="$TMP/leases.jsonl"; FS="$TMP/freeze-state.json"
say(){ echo "[drill-05] $*"; }
fail(){ say "RED: $*"; exit 1; }

# 0) 预置活跃租约（架构签注经 lease-issuer 正常签发），供 freeze 清租约读数。
#    席位取 product（写域行含机械 glob `.collab/drafts/`，可经 lease-issuer 零裁量子集校验；
#    该路径亦不在 product deny_globs 行内）。呈核注记（不修他票文件）：engineer 写域首行
#    「（工作空间根∪部署路径）−受保护区」＝非机械描述行，lease-issuer 无法对交付面旧字面 deliverables/**
#    类请求经子集校验实例化（实测读数入回执呈核段）。
python "$SCRIPTS/lease-issuer.py" --ticket DRILL05 --seat product --countersign architect:drill05 \
  --path-glob ".collab/drafts/tmp-drill05.md" \
  --config "$CFG/seat-permissions.json" --leases "$LEASES" >"$TMP/l1.txt" 2>&1 \
  || fail "租约签发 exit≠0: $(cat "$TMP/l1.txt")"
say "预置租约读数: $(cat "$TMP/l1.txt")"
# 冻结前：租约内写＝放行（无决策输出＝不干预）
python "$SCRIPTS/write-guard.py" --path ".collab/drafts/tmp-drill05.md" \
  --ledger "$LED" --leases "$LEASES" --freeze-state "$FS" \
  <<'JSON' >"$TMP/w0.txt" 2>&1
{"agent_type": "software-team-product", "agent_id": "product-drill05"}
JSON
grep -q '"permissionDecision"' "$TMP/w0.txt" && fail "冻结前租约内写被误拦（应放行）"
say "冻结前租约内写＝放行（ALLOW 读数在 stderr）"

# 1) freeze（一键冻结＝紧急直通三通道之首；人类直通发起演练面）
python "$SCRIPTS/freeze-unfreeze.py" freeze --ledger "$LED" --leases "$LEASES" \
  --freeze-state "$FS" --map "$CFG/seat-permissions-hooks-map.json" >"$TMP/fz.txt" 2>&1 \
  || fail "freeze exit≠0（含超时限读数如实呈现）: $(cat "$TMP/fz.txt")"
say "freeze 链读数:"; sed 's/^/  /' "$TMP/fz.txt"
ELAPSED=$(grep -o 'elapsed=[0-9.]*s' "$TMP/fz.txt" | head -1 | sed 's/elapsed=//;s/s//')
grep -q 'OK ≤时限' "$TMP/fz.txt" || fail "自计时读数缺位或超阈"
python -c "import sys; e=float('$ELAPSED'); assert e<=60.0, e; print(f'自计时读数 elapsed={e}s ≤60s OK')" || fail "自计时 >60s"

# 2) 清租约读数：leases.jsonl 出现 cleared 行
grep -q '"cleared": true' "$LEASES" || fail "freeze 清租约 cleared 行缺席"
say "清租约读数: leases.jsonl cleared 行在册"

# 3) 全写 deny：原租约内写也必 deny（freeze-state 联动）
python "$SCRIPTS/write-guard.py" --path ".collab/drafts/tmp-drill05.md" \
  --ledger "$LED" --leases "$LEASES" --freeze-state "$FS" \
  <<'JSON' >"$TMP/w1.txt" 2>&1
{"agent_type": "software-team-product", "agent_id": "product-drill05"}
JSON
grep -q '"permissionDecision":"deny"' "$TMP/w1.txt" || fail "freeze 态全写 deny 未生效"
grep -q 'B10 freeze 态全写 deny' "$TMP/w1.txt" || fail "deny 原因非 freeze 联动"
say "全写 deny 读数: 原租约内写亦 deny（B10 freeze 联动）"

# 4) 解冻（人类令牌）：无令牌→拒（fail-closed）；有令牌→解除
if python "$SCRIPTS/freeze-unfreeze.py" unfreeze --ledger "$LED" --leases "$LEASES" \
   --freeze-state "$FS" --token-anchor "$TMP/anchor" >/dev/null 2>&1; then
  fail "无人类令牌解冻未被拒（fail-closed 未成立）"
fi
say "令牌负例读数(exit≠0 预期): 无令牌解冻拒收在位"
TOKEN="drill05-human-token-$RANDOM"
python - "$TMP/anchor" "$TOKEN" <<'PY' || fail "锚写入失败"
import hashlib, sys
open(sys.argv[1], "w", encoding="utf-8").write(hashlib.sha256(sys.argv[2].encode("utf-8")).hexdigest() + "\n")
PY
python "$SCRIPTS/freeze-unfreeze.py" unfreeze --human-token "$TOKEN" --token-anchor "$TMP/anchor" \
  --ledger "$LED" --leases "$LEASES" --freeze-state "$FS" >"$TMP/uf.txt" 2>&1 \
  || fail "人类令牌解冻 exit≠0: $(cat "$TMP/uf.txt")"
say "解冻读数: $(cat "$TMP/uf.txt")"
python -c "import json; s=json.load(open('$FS',encoding='utf-8')); assert s['deny_all_writes']==False; print('解冻后 deny_all_writes=False 确认')" || fail "解冻状态未复位"

# 呈核注记（不修他票文件）：解冻后租约已被 freeze 链清除——恢复后若走日终对账，
# reconcile-daily.py:95 对 cleared 行（无 lease 键）KeyError＝已知差口，实测读数见回执单列（本演练不修）。

say "GREEN 停刀-恢复链：freeze→清租约→全写deny→人类令牌解冻→自计时 elapsed=${ELAPSED}s ≤60s"
echo "DRILL05_GREEN"
