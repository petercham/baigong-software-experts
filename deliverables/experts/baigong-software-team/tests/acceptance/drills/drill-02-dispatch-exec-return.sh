#!/usr/bin/env bash
# SWB-T06-D · 演练二＝派发-执行-回流（§17 六名逐字·名2）
# 判据：B3 展开→一票活跃→回流四型之一入账；串行闸对第二派发 exit≠0 亦属全绿条件。
# 落盘一律仓外 Temp；仓内零运行残留。
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PKG="$(cd "$DIR/../../.." && pwd)"
SCRIPTS="$PKG/skills/sop/scripts"
TMP="${T06_TMP:?T06_TMP 须由调用方注入（仓外 Temp·件内不落盘符）}/drill02"
rm -rf "$TMP"; mkdir -p "$TMP"
LED="$TMP/ledger.jsonl"; ST="$TMP/states.json"; AG="$TMP/agents.jsonl"
say(){ echo "[drill-02] $*"; }
fail(){ say "RED: $*"; exit 1; }

# 1) B3 展开（无活跃票状态下首派发：串行闸放行→机械展开→哈希入账）
python "$SCRIPTS/dispatch-builder.py" --ticket DRILL02 --node 4 --seat engineer \
  --agent-id engineer-drill02 --ledger "$LED" --states "$ST" --agents "$AG" --out "$TMP/injections" \
  >"$TMP/d1.txt" 2>&1 || fail "首派发 exit≠0: $(cat "$TMP/d1.txt")"
say "B3 展开读数: $(head -1 "$TMP/d1.txt")"
grep -q 'package_hash=' "$TMP/d1.txt" || fail "注入包哈希读数缺席"

# 2) 票建立（B2 建立于节点 1）→ 一票活跃
python "$SCRIPTS/state-transition.py" --ticket DRILL02 --from 1 --to 1 --ticket-type 开发 \
  --ledger "$LED" --states "$ST" >"$TMP/e1.txt" 2>&1 || fail "票据建立 exit≠0: $(cat "$TMP/e1.txt")"
say "一票活跃读数: $(cat "$TMP/e1.txt")"

# 3) 第二派发请求 → 串行闸 exit≠0（全绿条件之一）
if python "$SCRIPTS/dispatch-builder.py" --ticket DRILL02B --node 4 --seat engineer \
   --agent-id engineer-drill02b --ledger "$LED" --states "$ST" --agents "$AG" --out "$TMP/injections" \
   >"$TMP/d2.txt" 2>&1; then
  fail "串行闸未拦第二派发（应 exit≠0）"
fi
say "串行闸读数(exit≠0 预期): $(head -1 "$TMP/d2.txt")"
grep -q 'serial_gate_reject\|REJECT serial-gate' "$TMP/d2.txt" || fail "串行闸呈报读数缺席"

# 4) 执行推进＋回流入账（完成型＝4→5 迁移经 B2 签字集合校验入账）
python "$SCRIPTS/state-transition.py" --ticket DRILL02 --from 1 --to 2 --ticket-type 开发 \
  --sign 产品交付签 --sign 架构PRD接收签 --sign QA可验收性签 --ledger "$LED" --states "$ST" >/dev/null 2>&1 || fail "1→2 迁移被拒"
python "$SCRIPTS/state-transition.py" --ticket DRILL02 --from 2 --to 3 --ticket-type 开发 \
  --sign 架构交付签 --sign QA质量属性审计签 --ledger "$LED" --states "$ST" >/dev/null 2>&1 || fail "2→3 迁移被拒"
python "$SCRIPTS/state-transition.py" --ticket DRILL02 --from 3 --to 4 --ticket-type 开发 \
  --sign 架构生成签 --sign 产品范围签 --sign QA充分性签 --ledger "$LED" --states "$ST" >/dev/null 2>&1 || fail "3→4 迁移被拒"
python "$SCRIPTS/state-transition.py" --ticket DRILL02 --from 4 --to 5 --kind signoff --ticket-type 开发 \
  --sign 工程师交付签 --sign QA审计签 --return-type 完成 --ledger "$LED" --states "$ST" >"$TMP/r1.txt" 2>&1 \
  || fail "4→5 回流迁移入账 exit≠0: $(cat "$TMP/r1.txt")"
say "回流入账读数(完成型经 4→5 迁移登记): $(cat "$TMP/r1.txt")"

# 5) 账本回读：派发/呈报(串行拒)/签字(回流) 记录在位＋哈希链
python - "$LED" <<'PY' || fail "账本回读断言失败"
import json, sys
recs = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
def cnt(t, ev):
    return sum(1 for r in recs if r["type"] == t and r["payload"].get("event") == ev)
assert cnt("派发", "dispatch_built") == 1, "完成派发计数≠1"
assert cnt("呈报", "serial_gate_reject") >= 1, "串行闸呈报缺席"
assert cnt("签字", "transition") >= 1, "回流（4→5 签字类迁移）入账缺席"
prev = "GENESIS"
for r in recs:
    assert r["prev_hash"] == prev, f"哈希链断点 seq={r['seq']}"
    prev = r["hash"]
print(f"账本回读: 总记录={len(recs)} 哈希链连续 派发=1 串行拒>=1 回流签字>=1")
PY
[ $? -eq 0 ] || fail "账本回读未过"

# 呈核注记（不修他票文件）：回流四型（完成/部分完成/受阻/异常）之「型」字段在全部机制实体
# 落盘面未机械化——入账载体＝B2 迁移记录（G2），四型标签字段缺席＝缺陷呈核项（回执单列）。
say "NOTE: 回流四型标签字段未见机制实体机械化，载体＝B2 迁移记录（缺陷呈核·回执单列）"

say "GREEN 派发-执行-回流链：B3 展开→一票活跃→串行闸拒二派发(exit≠0)→回流四型之一(完成)入账"
echo "DRILL02_GREEN"
