#!/usr/bin/env bash
# SWB-T06-D · 演练一＝誊录路由（§17 六条演练词条 V13 L202 六名逐字·名1）
# 判据：人类输入→B1 登记→路由读数链全绿。
# 运行落盘一律置仓外 Temp（T06_TMP 由调用方注入·件内不落具体盘符）；仓内零运行残留。
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PKG="$(cd "$DIR/../../.." && pwd)"
SCRIPTS="$PKG/skills/sop/scripts"
TMP="${T06_TMP:?T06_TMP 须由调用方注入（仓外 Temp·件内不落盘符）}/drill01"
rm -rf "$TMP"; mkdir -p "$TMP"
LED="$TMP/ledger.jsonl"
say(){ echo "[drill-01] $*"; }
fail(){ say "RED: $*"; exit 1; }

# 1) 人类输入原文件（Temp）
IN="$TMP/human-input.txt"
printf '指令：按 SWB-T06 票面执行誊录路由演练。\n' > "$IN"

# 2) B1 登记（六类誊录闭集成员＝指令）
python "$SCRIPTS/intake-register.py" "$IN" --class 指令 --ledger "$LED" >"$TMP/out1.txt" 2>&1 \
  || fail "intake-register 正常类登记 exit≠0: $(cat "$TMP/out1.txt")"
say "登记读数: $(cat "$TMP/out1.txt")"
grep -q 'REGISTERED reg_no=INTK-' "$TMP/out1.txt" || fail "登记号读数缺席"

# 3) 负例：誊录类越出六闭集 → exit≠0（B1 零裁量拒收面）
if python "$SCRIPTS/intake-register.py" "$IN" --class 自造类别 --ledger "$LED" >"$TMP/out2.txt" 2>&1; then
  fail "越出六类闭集的誊录类未被拒（应 exit≠0）"
fi
say "负例读数(exit≠0 预期): $(head -1 "$TMP/out2.txt")"

# 4) 路由读数链：账本「intake 登记」记录恰 1＋四字段/登记号/哈希链在位
python - "$LED" <<'PY' || fail "账本回读断言失败"
import json, sys
recs = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
ints = [r for r in recs if r["type"] == "intake 登记"]
assert len(ints) == 1, f"intake 登记计数={len(ints)} ≠ 1"
p = ints[0]["payload"]
for k in ("reg_no", "class", "input_path", "sha256", "source_role", "declaration_tier", "purity_scan_ref"):
    assert k in p, f"字段缺席 {k}"
assert p["class"] == "指令"
print("路由读数链: intake登记=1 class=指令 reg_no=%s sha256=%s… hash=%s…" %
      (p["reg_no"], p["sha256"][:12], ints[0]["hash"][:12]))
PY
[ $? -eq 0 ] || fail "路由读数链断言未过"

say "GREEN 誊录路由链：人类输入→B1 登记→路由读数链全绿（负例闭集拒收在位）"
echo "DRILL01_GREEN"
