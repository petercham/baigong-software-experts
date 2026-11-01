# SWB-T01 平台能力实测包 P1–P10（施工票·L3·架构席起草）

- 开端读数：ANCHOR＝08fc5ee（分票包基线化实测，见总览件）；本票开工时实测 `git rev-parse --short HEAD` 附回执。
- 设计真源：`.collab/refs/external/SWB-交接件v2.4-产品设计与架构设计-2026-11-01.md`（行号前缀 V7；产品本体 L25–79 sha256=664ef6b2…；架构本体 L80–237 sha256=e0801956…）。逐字引用以该件为准，票面转述仅作路由。
- 背景（自包含）：多席位协作系统两份基线（产品设计 v2.4＋架构设计 v2.4）已三方收口生效。架构 §10 登记平台验证清单 P1–P10，并令「P3/P4/P7 由实测票先行落盘；P4/P7 阻塞 B5/B0 定型；未验证能力不得被任何闸引为前提」。本票＝消费面声明第⑥项「实测清单←§10」的承接票，也是全包唯一前置数据票：其读数决定 T02 主路形态、T05 主路形态、T05 候裁面处置。**§10 规则镜像到票面纪律：本包任何票面不得以 [未验证:P槽] 能力作闸前提。**
- 前置票：无（基线生效＝开工前提，架构 §18 基线化时序：B0 开工在基线生效之后；本票先于 B0 属 §10「实测先行」授权）。
- 逻辑并行性：可与任何票并行；实际派工在 B3 串行闸（T03 产物）上线前由人类侧纪律保证一票活跃，建议按 DAG 序首位施工。

## 声明闭集（13 件·本票唯一可写面）
- 声明闭集：
- software-team/tests/probes/run-probes.sh
- software-team/tests/probes/p1-cross-seat-shared-state.sh
- software-team/tests/probes/p2-lead-md-injection.sh
- software-team/tests/probes/p3-tools-declaration-scope.sh
- software-team/tests/probes/p4-pretooluse-stdin-fields.sh
- software-team/tests/probes/p5-event-concurrency-timing.sh
- software-team/tests/probes/p6-deny-cross-seat-consistency.sh
- software-team/tests/probes/p7-git-standalone-service.sh
- software-team/tests/probes/p8-mcp-auth-shape.sh
- software-team/tests/probes/p9-dispatch-record-export.sh
- software-team/tests/probes/p10-thirdparty-hooks-parity.sh
- software-team/tests/probes/results/probe-results.json
- software-team/tests/probes/results/probe-report.md

## 逐条施工规格

### T01-A 十个实测脚本（P1–P10 逐号一件·V7 L183 词条逐号对应）
每个脚本头部注 `# P<n> <§10 原句摘录>`，落点路径见闭集行。逐号标的（§10 原文口径，不得扩义）：
- p1＝席位间文件外共享状态；p2＝主理人 md 注入恒常性与上限；p3＝工具声明生效范围；p4＝PreToolUse stdin 字段完整性（代码层已证、待运行时——运行时部分为本票增量）；p5＝事件并发时序；p6＝deny 跨席位一致性；p7＝git 独立服务可建性；p8＝MCP auth 形态（**问句，无预设**：只登记观测，不得预填结论）；p9＝派发记录导出；p10＝第三方插件 hooks 同权性。
- p4 代码层复真锚点（§19 buildAgentTrigger 行）：对平台 CLI 打包件 `codebuddy-lite-wb.mjs` grep `executePreToolUseHooks` payload 注入 `agent_id`/`agent_type`，脚本须复现该 grep 并附读数；运行时核验＝实际触发一次 PreToolUse 并回显 stdin JSON 字段清单。
- p7 核验方式＝按 §19「git 原生能力」行：仅验**可建性**（本地建裸仓＋保护分支/拒非快进配置可达），不验远端服务运维（属 §11 人类侧外置物）。

### T01-B 读数落盘（机检源）
- `probe-results.json`：顶层对象，键＝P1–P10 恰十个；每键值＝`{"status":"pass|negative|inconclusive","evidence":"<读数文件路径或命令>","ts":"<ISO8601>"}`。status 三态闭集，禁他值。
- `run-probes.sh`：依序调用十脚本→汇总写 probe-results.json→退出码：全十键齐且值合法＝0，否则≠0。
- `probe-report.md`：十节（每 P 一节），每节含实测命令、读数摘录、QA 复核结论栏（QA 席填写，工程师只留空栏——§14 行2「装配工程师实测＋QA 复核」）。

## 验收判据（全部机械可判）
1. `bash software-team/tests/probes/run-probes.sh; echo $?` ＝0；
2. `python -c "import json;d=json.load(open('software-team/tests/probes/results/probe-results.json'));assert sorted(d)==['P'+str(i) for i in range(1,11)];assert all(v['status'] in ('pass','negative','inconclusive') for v in d.values())"` 退出 0；
3. `ls software-team/tests/probes/*.sh | wc -l` ＝11（十实测＋runner）；
4. p4 脚本回执含 `executePreToolUseHooks` grep 命中读数与 stdin 字段回显两块证据（回执内嵌原文，grep 可定位）；
5. probe-report.md 节数：`grep -c '^## P' software-team/tests/probes/results/probe-report.md` ＝10；
6. P8 节结论栏只含观测不含预设：人工抽检项移交 QA（不机械化，因 §10「问句，无预设」）。

## 票间关系
- 后置消费：T02 读 P7 定主路；T05 读 P4/P5 定主路；T05 读 P3 定 disallowedTools 候裁；P8 读数供候裁单列 Q-03。
- 本票不依赖任何票。

## 禁动面（零触碰）
- 两基线登记件（V7 文件本体）、`.collab/` 全域（回执除外）、`docs/`、其余各票声明闭集文件、`software-team/` 下非本票闭集路径（目录首建者以先开工票为准，见总览 Q-01）。
- 工程师不得改本票票体四字段（§7 工程师席位纪律）。

## 候裁点（单列·不自行拍）
- 无（本票只产读数；读数触发的拍点列于 T02/T05 票面与总览候裁清单）。

## 回执
落 `.collab/receipts/2026-11-01-SWB-T01-receipt.md`：开端 HEAD＋完整文件清单（与 commit name-only 全等）＋全部机制断言附实测载体。commit 单独笔，`collab:` 前缀只含本票闭集件。
