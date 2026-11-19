#!/usr/bin/env bash
# 用途＝tests 桶 run-all 入口：python 回归五枚与验收演练执行器一枚串跑→全绿末行 RUN_ALL_GREEN。
# 「纯标准库零第三方依赖」声明一行（声明本体＝计划 v2 行 123 逐字）＝入口件本体只调 python3／bash／coreutils。
# 运行窗＝worktree 根或包根两态皆可执行（经 BASH_SOURCE 自定位件目录·不依 cwd）。
# 族名＝ITER-W2-T2e 交付。
# probes 段处置申明（票级放行登记黄-6 采乙写死）＝本入口默认跳跑 run-probes.sh。原因＝该 runner 以
# cp 重写 tests 桶同域 tracked 件 probe-results.json（ts 字段必变）＝违本票 tests 既有 28 枚零改禁动面
# 与施工面单核验；探针结果消费面＝只读既有 probe-results.json 与 probe-report.md 两件；
# run-probes.sh 单跑归显式接受该重写副作用的席位自跑＝不入本入口串跑序（跳跑原因随此注释申明）。
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
n_green=0
n_total=0
run_step() {
  target="$1"
  runner="$2"
  n_total=$((n_total + 1))
  echo "==== run-all: $target ===="
  if "$runner" "$DIR/$target"; then
    n_green=$((n_green + 1))
    echo "==== run-all: $target -> GREEN ===="
  else
    echo "==== run-all: $target -> RED（红链具名：$target）====" >&2
    echo "RUN_ALL_RED red_chain=$target green=$n_green/$n_total" >&2
    exit 1
  fi
}
# 执行序第一段＝python 回归五枚依序（s2／s3／s4 全部 test 前缀 py·逐件 exit 码即时打印）
run_step "s2/test_lease_instantiation.py" python3
run_step "s2/test_ledger_core.py" python3
run_step "s3/test_decision_pack.py" python3
run_step "s3/test_dispatch_gate.py" python3
run_step "s4/test_enforcement.py" python3
# 执行序第二段＝验收演练执行器（六演练串跑·落盘仓外 Temp 零仓内残留＝先例形制；红链指名形制沿 drill-runner 先例）
run_step "acceptance/drill-runner.sh" bash
# 执行序第三段＝probes 段＝默认跳跑（黄-6 乙案·申明见头注）
if [ "$n_green" -eq "$n_total" ] && [ "$n_total" -eq 6 ]; then
  echo "probes 段跳跑申明在册（黄-6 乙案＝原因见头注）"
  echo "RUN_ALL_GREEN"
  exit 0
fi
echo "RUN_ALL_RED green=$n_green/$n_total" >&2
exit 1
