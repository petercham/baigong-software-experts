#!/usr/bin/env bash
# SWB-T06-D · 六条演练执行器：依序执行六脚本→全绿 exit 0 输出 SIX_DRILLS_GREEN；
# 任一红→exit≠0 并指名红链。落盘一律仓外 Temp（T06_TMP，全域一致路径·Git Bash 与
# Windows python 同域可读；禁 /tmp）。
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# T06_TMP 由调用方注入（全域一致路径要求＝Git Bash 与 Windows python 同域可读·禁 /tmp，
# 例＝仓外同级 Temp 目录）。件内不落具体盘符（OA-T1 项目实体款）；未注入时缺省取系统
# 临时目录（运行时经 python tempfile 计算）。
if [ -z "${T06_TMP:-}" ]; then
  T06_TMP="$(python -c 'import tempfile;print(tempfile.gettempdir().replace(chr(92),"/"))')"
fi
export T06_TMP
echo "drill-runner T06_TMP=$T06_TMP"
DRILLS=(
  "drills/drill-01-transcription-routing.sh"
  "drills/drill-02-dispatch-exec-return.sh"
  "drills/drill-03-write-side-intercept.sh"
  "drills/drill-04-decision-pack-escalation.sh"
  "drills/drill-05-freeze-recover.sh"
  "drills/drill-06-replay-reconcile.sh"
)
n_green=0
for d in "${DRILLS[@]}"; do
  echo "==== drill-runner: $d ===="
  if bash "$DIR/$d"; then
    n_green=$((n_green + 1))
    echo "==== $d -> GREEN ===="
  else
    echo "==== $d -> RED（红链指名：$d）====" >&2
    echo "DRILL_RUNNER_RED red_chain=$d green=$n_green/6" >&2
    exit 1
  fi
done
if [ "$n_green" -eq 6 ]; then
  echo "SIX_DRILLS_GREEN"
  exit 0
fi
echo "DRILL_RUNNER_RED green=$n_green/6" >&2
exit 1
