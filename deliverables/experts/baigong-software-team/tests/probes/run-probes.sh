#!/usr/bin/env bash
# SWB-T01 实测包 runner（票面 T01-B）：依序调用十脚本→汇总写 probe-results.json。
# 退出码：全十键齐且值合法（pass|negative|inconclusive）＝0，否则≠0。
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RESULTS_DIR="$HERE/results"
mkdir -p "$RESULTS_DIR"

# 读数证据目录＝系统 Temp（临时文件不落仓·票面纪律）
EVID_DIR="$(mktemp -d "${TMPDIR:-/tmp}/swb-t01-evid-XXXXXX")"
export EVID_DIR

RESULT_JSON="$RESULTS_DIR/probe-results.json"
TMP_JSON="$EVID_DIR/probe-results.json"
: > "$TMP_JSON"

declare -A STATUS
for n in 1 2 3 4 5 6 7 8 9 10; do
  case $n in
    1)  f=p1-cross-seat-shared-state.sh ;;
    2)  f=p2-lead-md-injection.sh ;;
    3)  f=p3-tools-declaration-scope.sh ;;
    4)  f=p4-pretooluse-stdin-fields.sh ;;
    5)  f=p5-event-concurrency-timing.sh ;;
    6)  f=p6-deny-cross-seat-consistency.sh ;;
    7)  f=p7-git-standalone-service.sh ;;
    8)  f=p8-mcp-auth-shape.sh ;;
    9)  f=p9-dispatch-record-export.sh ;;
    10) f=p10-thirdparty-hooks-parity.sh ;;
  esac
  out=$(EVID_DIR="$EVID_DIR" bash "$HERE/$f" 2>&1)
  rc=$?
  printf '%s\n' "$out" > "$EVID_DIR/p$n.runlog"
  st=$(printf '%s\n' "$out" | grep '^STATUS: ' | tail -1 | cut -d' ' -f2)
  if [ $rc -ne 0 ]; then
    st=inconclusive   # 脚本执行失败＝异常路由如实登记，不静默跳过
  fi
  case "$st" in pass|negative|inconclusive) : ;; *) st=inconclusive ;; esac
  STATUS[$n]="$st"
  printf 'P%s -> %s\n' "$n" "$st"
done

ts=$(date -u +%Y%m%dT%H%M%SZ)   # ISO 8601 基本格式（仓闸 OA-T1 裸日期模式豁免随动；扩展格式 20xx-xx-xx 属 deliverables/** 禁面）
evid_fwd="${EVID_DIR//\\//}"   # JSON 字符串内反斜杠转义防护（Windows Temp 路径转正斜杠）
{
  printf '{\n'
  for n in 1 2 3 4 5 6 7 8 9 10; do
    evid="tests/probes/results/probe-report.md#P${n} | evid=${evid_fwd}/p${n}.runlog"
    printf '  "P%s": {"status": "%s", "evidence": "%s", "ts": "%s"}' "$n" "${STATUS[$n]}" "$evid" "$ts"
    [ "$n" -lt 10 ] && printf ','
    printf '\n'
  done
  printf '}\n'
} > "$TMP_JSON"
cp "$TMP_JSON" "$RESULT_JSON"

# 机检：全十键齐且值合法＝0，否则≠0（与票面验收判据 2 同判）
python3 - "$RESULT_JSON" <<'PY'
import json,sys
d=json.load(open(sys.argv[1],encoding='utf-8'))
assert sorted(d,key=lambda k:int(k[1:]))==['P'+str(i) for i in range(1,11)]
assert all(v['status'] in ('pass','negative','inconclusive') for v in d.values())
PY
