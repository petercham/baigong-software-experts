#!/usr/bin/env bash
# SWB-T06-D · 演练四＝决策包呈拍（§17 六名逐字·名4）
# 判据：触发源六码之一→B4 包→呈拍记录。
# 落盘一律仓外 Temp；仓内零运行残留。
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PKG="$(cd "$DIR/../../.." && pwd)"
SCRIPTS="$PKG/skills/sop/scripts"
TMP="${T06_TMP:?T06_TMP 须由调用方注入（仓外 Temp·件内不落盘符）}/drill04"
rm -rf "$TMP"; mkdir -p "$TMP"
LED="$TMP/ledger.jsonl"
say(){ echo "[drill-04] $*"; }
fail(){ say "RED: $*"; exit 1; }

# 1) 触发源六闭集逐码枚举面在位（真源＝decision-pack.py 六码）＋越码拒收
if python "$SCRIPTS/decision-pack.py" report --trigger 自造触发码 --ticket DRILL04 --ledger "$LED" >/dev/null 2>&1; then
  fail "越出六闭集的触发码未被拒（应 exit≠0）"
fi
say "负例读数(exit≠0 预期): 触发码越闭集拒收在位"

# 2) 六码之一（引用扫描命中）→ B4 呈报决策包装配落盘
python "$SCRIPTS/decision-pack.py" report --trigger 引用扫描命中 --ticket DRILL04 \
  --evidence '{"source":"drill-04","note":"演练构造证据：引用扫描命中样例"}' \
  --severity P2 --ledger "$LED" --out "$TMP/pack-report.json" >"$TMP/dp.txt" 2>&1 \
  || fail "呈报决策包装配 exit≠0: $(cat "$TMP/dp.txt")"
say "B4 包读数: $(head -1 "$TMP/dp.txt")"
grep -q 'pack_hash=' "$TMP/dp.txt" || fail "决策包哈希读数缺席"
python -c "import json,sys; p=json.load(open(sys.argv[1],encoding='utf-8')); assert p['pack_type']=='呈报' and p['trigger_source']=='引用扫描命中' and 'defect_grading' in p; print('包体字段核: pack_type/trigger_source/defect_grading 在位')" "$TMP/pack-report.json" \
  || fail "决策包字段核验失败"

# 3) 呈拍记录入账（呈报记录类恰配）
python - "$LED" <<'PY' || fail "呈拍记录断言失败"
import json, sys
recs = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
pk = [r for r in recs if r["type"] == "呈报" and r["payload"].get("event") == "decision_pack_report"]
assert len(pk) == 1, f"呈报决策包记录={len(pk)} ≠1"
assert pk[0]["payload"]["trigger_source"] == "引用扫描命中"
print(f"呈拍记录读数: decision_pack_report=1 trigger=引用扫描命中 pack_hash={pk[0]['payload']['pack_hash'][:12]}…")
PY
[ $? -eq 0 ] || fail "呈拍记录链未过"

# 4) 灰度→全量门禁负例（表2-2 机械门禁不得现场裁量）：无声明判据→拒出包
if python "$SCRIPTS/decision-pack.py" full-rollout --ticket DRILL04 --criteria "$TMP/no.json" \
   --readings "$TMP/no.json" --ledger "$LED" >/dev/null 2>&1; then
  fail "无声明判据的 full-rollout 未被拒"
fi
say "灰度门禁负例读数(exit≠0 预期): 声明判据缺席拒出包在位"

say "GREEN 决策包呈拍链：六码之一→B4 包装配落盘→呈拍记录入账（六闭集拒收＋灰度门禁负例在位）"
echo "DRILL04_GREEN"
