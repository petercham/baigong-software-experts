#!/usr/bin/env bash
# SWB-T06-D · 演练三＝写侧拦截（§17 六名逐字·名3）
# 判据：无租约写→deny 读数＋呈报码。
# 落盘一律仓外 Temp；仓内零运行残留。
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PKG="$(cd "$DIR/../../.." && pwd)"
SCRIPTS="$PKG/skills/sop/scripts"
TMP="${T06_TMP:?T06_TMP 须由调用方注入（仓外 Temp·件内不落盘符）}/drill03"
rm -rf "$TMP"; mkdir -p "$TMP"
LED="$TMP/ledger.jsonl"; LEASES="$TMP/leases.jsonl"
say(){ echo "[drill-03] $*"; }
fail(){ say "RED: $*"; exit 1; }

# 0) 签核环节（裁定现行态＝签名验核体系保留并继续执行）：sign-verify 正常调用；
#    密钥缺位时按其 fail-closed 形态如实呈现（exit≠0 即预期读数，不造假通过）。
printf 'DRILL03 签核环节样例件\n' > "$TMP/signed.md"
printf 'placeholder\n' > "$TMP/signed.md.sig"
python "$SCRIPTS/sign-verify.py" --signed "$TMP/signed.md" --signature "$TMP/signed.md.sig" \
  --keyring "$TMP/keyring" --identity-anchor "$TMP/identity-anchors" --ledger "$LED" \
  >"$TMP/sv.txt" 2>&1
SV_RC=$?
say "sign-verify 调用 exit=$SV_RC（密钥缺位＝fail-closed 硬失败为预期形态）"
[ $SV_RC -ne 0 ] || fail "sign-verify 在无密钥环状态返回 0（fail-closed 未成立？）"
grep -q 'verify_fail' "$LED" || fail "验签失败记录未入账（签字记录类）"

# 1) 无租约状态样例写请求 → deny 读数
#（SWB-B4 补丁五：探针路径随两级锚换代＝项目根相对新字面，仓根字面 deliverables/** 已随 B2 灭）
python "$SCRIPTS/write-guard.py" --path "agents/x.md" \
  --ledger "$LED" --leases "$LEASES" --freeze-state "$TMP/freeze-state.json" \
  <<'JSON' >"$TMP/wg.txt" 2>&1
{"agent_type": "software-engineer", "agent_id": "engineer-drill03",
 "tool_input": {"file_path": "agents/x.md"}}
JSON
say "write-guard 输出: $(cat "$TMP/wg.txt")"
grep -q '"permissionDecision":"deny"' "$TMP/wg.txt" || fail "deny 读数缺席"

# 2) 呈报码：deny 留痕＋触发源六闭集①租约越界deny 各恰一
python - "$LED" <<'PY' || fail "呈报码断言失败"
import json, sys
recs = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
deny = [r for r in recs if r["type"] == "写入" and r["payload"].get("event") == "write_deny"]
rep = [r for r in recs if r["type"] == "呈报" and r["payload"].get("trigger_source") == "租约越界deny"]
assert len(deny) == 1, f"write_deny 留痕={len(deny)} ≠1"
assert len(rep) == 1, f"租约越界deny 呈报码={len(rep)} ≠1"
print(f"呈报码读数: write_deny=1 呈报(租约越界deny)=1 呈报hash={rep[0]['hash'][:12]}…")
PY
[ $? -eq 0 ] || fail "呈报码链未过"

say "GREEN 写侧拦截链：无租约写→deny 读数＋「租约越界deny」呈报码（签核环节 sign-verify fail-closed 如实呈现）"
echo "DRILL03_GREEN"
