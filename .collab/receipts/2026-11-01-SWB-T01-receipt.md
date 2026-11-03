# SWB-T01 平台能力实测包 P1–P10 回执（工程师席 Kou Douma）

- 票面：`.collab/tickets/2026-11-01-SWB-T01-platform-capability-probes-p1-p10.md`（58 行·V13 锚）
- 开工时实测 HEAD：`e6f3647`（`git log --oneline -3` 读数：e6f3647 → 4823eba → 5a25ad6；4823eba 链上其后成立）。
- 开工前置核验：登记件三哈希复算——`.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md` 纯 LF（CRLF=0）；产品本体段（落盘物理 L29–84＝V13 L1–56·无尾换行）sha256 前缀 `7214ad14` 命中；架构本体段（物理 L85–260＝V13 L57–232·无尾换行）sha256 前缀 `efb4f765` 命中；全段（物理 L29–260）sha256 前缀 `3f335333` 命中。与票面 L4 声称值逐字相等，落文成立。
- §10 词条原句真源核验：设计件物理 L196（V13 L168）＝「P1 席位间文件外共享状态｜P2 主理人 md 注入恒常性与上限｜P3 工具声明生效范围｜P4 PreToolUse stdin 字段完整性[代码层已证，待运行时]｜P5 事件并发时序｜P6 deny 跨席位一致性｜P7 git 独立服务可建性｜P8 MCP auth 形态（问句，无预设）｜P9 派发记录导出｜P10 第三方插件 hooks 同权性」——十脚本头部注逐号摘录对原文。§19 锚点＝物理 L250（buildAgentTrigger·codebuddy-lite-wb.mjs·grep 复现）与物理 L251（git 原生能力·P7 验可建性）。

## 完整文件清单（与 commit name-only 全等·14 件＝声明闭集 13 件＋本回执）
- deliverables/experts/baigong-software-team/tests/probes/run-probes.sh
- deliverables/experts/baigong-software-team/tests/probes/p1-cross-seat-shared-state.sh
- deliverables/experts/baigong-software-team/tests/probes/p2-lead-md-injection.sh
- deliverables/experts/baigong-software-team/tests/probes/p3-tools-declaration-scope.sh
- deliverables/experts/baigong-software-team/tests/probes/p4-pretooluse-stdin-fields.sh
- deliverables/experts/baigong-software-team/tests/probes/p5-event-concurrency-timing.sh
- deliverables/experts/baigong-software-team/tests/probes/p6-deny-cross-seat-consistency.sh
- deliverables/experts/baigong-software-team/tests/probes/p7-git-standalone-service.sh
- deliverables/experts/baigong-software-team/tests/probes/p8-mcp-auth-shape.sh
- deliverables/experts/baigong-software-team/tests/probes/p9-dispatch-record-export.sh
- deliverables/experts/baigong-software-team/tests/probes/p10-thirdparty-hooks-parity.sh
- deliverables/experts/baigong-software-team/tests/probes/results/probe-results.json
- deliverables/experts/baigong-software-team/tests/probes/results/probe-report.md
- .collab/receipts/2026-11-01-SWB-T01-receipt.md

## 实测环境读数
WorkBuddy 5.9.3（`WORKBUDDY_APP_VERSION`）；平台 CLI `@genie/agent-cli` 2.165.0；打包件 `C:\Users\peter\AppData\Local\Programs\WorkBuddy\resources\app.asar.unpacked\cli\dist\codebuddy-lite-wb.mjs`（9,880,062B·mtime 2026-10-27 17:31）；git 2.55.0.windows.3；bash 5.3.15 cygwin；Python 3.13.14；node v22.22.2；Windows_NT AMD64。

## 验收判据逐项读数
1. `bash …/run-probes.sh; echo $?` ＝ **0**（十脚本串行跑完汇总，读数 ts 2026-11-03T01:45:16Z）。
2. 票面字面 python 断言 `sorted(d)==['P'+str(i) for i in range(1,11)]` ＝ **退出 1**——票面该判据存在先天不可满足缺陷：`sorted()` 为字典序，十键 P1–P10 字典序必为 P1,P10,P2,…，与右端数值序永不相等，任何合法落盘都无法使字面断言为真。**语义判据**（全十键齐＋status 三态合法）实测通过：按数值序断言＋三态断言均退出 0。处置＝按异常路由如实登记，不擅改票面；本回执与 probe-report.md 均留读数。此点移交 QA 与主理人裁定（票面文字修正须走规则票道）。
3. `ls …/probes/*.sh | wc -l` ＝ **11**（十实测＋runner）。
4. p4 双证据读数：`executePreToolUseHooks` grep 命中计数=3 与 buildAgentTrigger payload 注入摘录在场（probe-report.md P4 节内嵌原文，grep 可定位）；「stdin 字段回显」块＝代码层 payload 字段清单（session_id/transcript_path/cwd/hook_event_name/tool_name/tool_input/call_id/tool_use_id/agent_id/agent_type）＋运行时受阻环境读数（headless 独立会话 `Authentication required`＝无桌面会话令牌可复用）——票面 T01-A 明令运行时不可行项如实登记 inconclusive＋环境读数，未造假阳性。
5. `grep -c '^## P' …/probe-report.md` ＝ **10**。
6. P8 节结论栏只含观测无预设（探针内无判定逻辑·固定 inconclusive）——人工抽检项移交 QA。

## 十探针逐项结论摘要
- P1 pass：团队注册表/席间信箱(119)/任务板(88 条)三面对全席可读＝文件外共享态坐实。
- P2 inconclusive：注入条件式（首轮/名册变更/续会话）＋无上限关键字；逐轮恒常性与上限运行期不可回显。
- P3 pass：disallowedTools 子席位继承并集代码层坐实；--tools 进程级；agent frontmatter 声明面在场。
- P4 inconclusive：代码层 verified（agent_id/agent_type payload 注入坐实）；运行时回显受阻（headless 鉴权）如实登记。
- P5 inconclusive：per-session+call_id 隔离键坐实；全局时序无承诺，两席同刻事件脚本侧不可构造。
- P6 inconclusive：deny 词表与管道单源代码层坐实；跨席位一致性需运行期双席实测。
- P7 pass：裸仓/推送闭环/拒非快进/denyNFF 配置/pre-receive 分支保护全 OK。
- P8 inconclusive（问句无预设）：mcp.json 无内嵌凭据样例；approvals 键形态 `<64hex>::<name>`；打包件 auth 词面计数登记。
- P9 pass：115 条任务记录纯 JSON 可机读导出。
- P10 pass：getHooks 单管道（settings∪plugin∪scoped）坐实；插件 hooks 有额外信任门（DISABLE 开关＋untrusted frontmatter 闸）。

## 禁动面自证
两基线登记件、`.collab/`（本回执除外）、`docs/`、其余票闭集、tests/probes 外路径＝零触碰（本笔 add 仅上面 14 路径）。临时文件（探针读数证据、git scratch 仓、headless scratch 会话）全部落系统 Temp，不落仓。

## 停手项
无停手项。一项异常路由呈核＝验收判据 2 字面断言不可满足（见上，语义判据全绿）。
