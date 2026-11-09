#!/usr/bin/env bash
# SWB-T06-D · 演练六＝重放对账（§17 六名逐字·名6）
# 判据：B8 重放→差异三分类＋引用扫描结论→日终对账差=0。
# 落盘一律仓外 Temp；仓内零运行残留。
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PKG="$(cd "$DIR/../../.." && pwd)"
SCRIPTS="$PKG/skills/sop/scripts"
ROOT="$(cd "$PKG/../../.." && pwd)"
TMP="${T06_TMP:?T06_TMP 须由调用方注入（仓外 Temp·件内不落盘符）}/drill06"
rm -rf "$TMP"; mkdir -p "$TMP/inject"
LED="$TMP/ledger.jsonl"; LEASES="$TMP/leases.jsonl"; ST="$TMP/states.json"
say(){ echo "[drill-06] $*"; }
fail(){ say "RED: $*"; exit 1; }

# 0) 预置在册票据＋租约（对账交叉核两侧同源，避免 orphan 租约假差）
python "$SCRIPTS/state-transition.py" --ticket DRILL06 --from 1 --to 1 --ticket-type 开发 \
  --ledger "$LED" --states "$ST" >/dev/null 2>&1 || fail "票据建立 exit≠0"
python "$SCRIPTS/lease-issuer.py" --ticket DRILL06 --seat product --countersign architect:drill06 \
  --path-glob ".collab/drafts/tmp-drill06.md" \
  --config "$PKG/config/seat-permissions.json" --leases "$LEASES" >/dev/null 2>&1 \
  || fail "租约签发 exit≠0"

# 1) B8 重放（正扫面：注入存档＋转正候选件＝纯件 → 零命中 exit 0）
printf '# 候选件（演练构造·纯）\n\n依据 V13 L202 设计锚与 .collab/ledger/ 治理域路径引用。\n' > "$TMP/candidate.md"
printf '# 注入存档件（演练构造·纯）\n\n本件仅含指针三形态引用。\n' > "$TMP/inject/item.md"
python "$SCRIPTS/shadow-replay.py" --ledger "$LED" --repo "$ROOT" --inject "$TMP/inject" \
  --candidate "$TMP/candidate.md" --out "$TMP/replay.json" >"$TMP/rp.txt" 2>&1 \
  || fail "B8 正扫面 exit≠0（纯件应零命中）: $(tail -2 "$TMP/rp.txt")"
python - "$TMP/replay.json" <<'PY' || fail "差异三分类结构断言失败"
import json, sys
r = json.load(open(sys.argv[1], encoding="utf-8"))
d = r["diffs"]
for k in ("missing_in_replay", "missing_in_ledger", "mismatch"):
    assert k in d, f"三分类键缺席 {k}"
print(f"三分类读数: missing_in_replay={len(d['missing_in_replay'])} "
      f"missing_in_ledger={len(d['missing_in_ledger'])} mismatch={len(d['mismatch'])}")
print(f"引用扫描结论: 词族命中={len(r['scan']['word_hits'])} 引用命中={len(r['scan']['ref_hits'])}（正扫面零命中 exit 0）")
PY
[ $? -eq 0 ] || fail "三分类读数未过"

# 2) 负扫面：过程痕迹词族＋过程件引用 → 命中 exit≠0（违纪行 11 拦截面在位）
printf '# 脏件\n\n本段为修订史述过程记录，并引用 .collab/archive/old-note.md 作引用目标。\n' > "$TMP/dirty.md"
if python "$SCRIPTS/shadow-replay.py" --ledger "$LED" --repo "$ROOT" --candidate "$TMP/dirty.md" \
   --out "$TMP/replay-dirty.json" --report-ledger "$TMP/report-ledger.jsonl" >/dev/null 2>&1; then
  fail "脏件扫描未命中（应 exit≠0）"
fi
python -c "
import json
r=json.load(open('$TMP/replay-dirty.json',encoding='utf-8'))
assert r['scan']['word_hits'] and r['scan']['ref_hits']
print('负扫面读数: 词族命中=%d 过程件引用命中=%d exit≠0 在位' % (len(r['scan']['word_hits']), len(r['scan']['ref_hits'])))" || fail "负扫面命中读数缺位"

# 3) 日终对账差=0（本演练 Temp 域：无 cleared 行的干净租约台账面）
python "$SCRIPTS/reconcile-daily.py" --ledger "$LED" --leases "$LEASES" --states "$ST" \
  --repo-root "$ROOT" >"$TMP/rc.txt" 2>&1 || fail "reconcile-daily exit≠0: $(cat "$TMP/rc.txt")"
python -c "
import json
r=json.load(open(0,encoding='utf-8'))" < /dev/null 2>/dev/null
RC_DIFF=$(python -c "import json,sys; r=json.loads(open('$TMP/rc.txt',encoding='utf-8').read()); print(r['diff'])")
[ "$RC_DIFF" = "0" ] || { say "对账读数: $(cat "$TMP/rc.txt")"; fail "日终对账差=$RC_DIFF ≠0"; }
say "日终对账读数: diff=0（counts 见 $TMP/rc.txt）"

# 已知差口实测探针（呈核用·不修他票文件）：对含 freeze cleared 行的租约台账跑对账→KeyError 复现
printf '{"ts":"t","cleared": true, "by":"probe"}\n' > "$TMP/leases-cleared.jsonl"
cat "$LEASES" >> "$TMP/leases-cleared.jsonl"
python "$SCRIPTS/reconcile-daily.py" --ledger "$LED" --leases "$TMP/leases-cleared.jsonl" \
  --states "$ST" --repo-root "$ROOT" >"$TMP/rc2.txt" 2>&1
PRC=$?
say "差口探针读数: reconcile-daily 对 cleared 行台账 exit=$PRC（详情 $TMP/rc2.txt 尾行：$(tail -1 "$TMP/rc2.txt")）"

say "GREEN 重放对账链：B8 三分类＋引用扫描结论（正扫零命中/负扫 exit≠0）→日终对账差=0（clean 面）"
echo "DRILL06_GREEN"
