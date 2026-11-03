# SWB-T01 平台能力实测报告（P1–P10·工程师实测件·QA 复核栏留空）

- 实测环境读数（运行时平台版本与环境）：WorkBuddy 5.9.3（env `WORKBUDDY_APP_VERSION=5.9.3`）；平台 CLI 打包件 `@genie/agent-cli` version 2.165.0（`…/WorkBuddy/resources/app.asar.unpacked/cli/package.json`），打包件本体 `…/cli/dist/codebuddy-lite-wb.mjs`（9,880,062 字节·mtime 2026-10-27 17:31）；git 2.55.0.windows.3；bash 5.3.15(1)-release (x86_64-pc-cygwin)；Python 3.13.14；node v22.22.2；OS=Windows_NT AMD64。
- 实测时刻：`2026-11-03`（UTC·反引号段＝仓闸 OA-T1 遮除区随动）·runner＝`run-probes.sh`（十脚本串行汇总）·`probe-results.json` 的 `ts` 用 ISO 8601 基本格式（同闸随动）。
- 状态三态口径（票面 T01-B）：pass／negative／inconclusive。P8 按票面纪律＝问句无预设，固定 inconclusive（仅观测）。
- 机检源＝`probe-results.json`（同目录）。读数证据文件落系统 Temp（`%TMPDIR%/swb-t01-evid-*`），不落仓。

## P1 席位间文件外共享状态
- 状态：**pass**
- 实测命令：`bash p1-cross-seat-shared-state.sh`
- 读数摘录：平台状态根 `~/.workbuddy/teams/<team>/` 下 `config.json`（members=119·leadAgentId 在册）、`runtime.json`（status=active·updatedAt 读数）、`inboxes/*.json`（119 个席间信箱文件）；任务板 `~/.workbuddy/tasks/<team>/*.json`（88 条记录·键集 activeForm/createdAt/description/id/status/subject/updatedAt）。＝席位间存在仓库文件之外的平台态共享面（团队注册表＋席间信箱＋任务板），三面对全部席位可读。
- QA 复核结论栏：（待 QA 席填写）

## P2 主理人 md 注入恒常性与上限
- 状态：**inconclusive**
- 实测命令：`bash p2-lead-md-injection.sh`
- 读数摘录：打包件 grep `team-sys-prompt`=1、`data-role="team-context"`=2；注入站点＝TeamContextInterceptor（`shouldInjectTeamPrompt` 条件式：首轮用户消息/续会话/名册指纹变更时注入，名册未变且消息已含标记则跳过）；注入路径未见 `maxChars/truncat/maxLength` 类上限关键字；运行期逐轮恒常性与注入上限无法从脚本侧回显（transcript 不在可扫面·sessions 目录扫描 team-context 命中=0）。恒常性与上限两问均未证实未证伪。
- QA 复核结论栏：（待 QA 席填写）

## P3 工具声明生效范围
- 状态：**pass**
- 实测命令：`bash p3-tools-declaration-scope.sh`
- 读数摘录：打包件 token 计数 `--tools`=4、`allowedTools`=19、`disallowedTools`=15。子席位继承逻辑读数：`this.mainSession.options.disallowedTools ?? []` 与 agent 配置 `disallowedTools` 取并集后注入子席位 options（继承并集语义坐实）；`--tools` 为进程级内置工具限制；agent md frontmatter 支持 `tools`/`disallowedTools` 声明。生效范围＝进程级（CLI 旗标）＋agent 声明级＋子席位继承并集，代码层坐实。
- QA 复核结论栏：（待 QA 席填写）

## P4 PreToolUse stdin 字段完整性
- 状态：**inconclusive**（代码层已证＝verified；运行时增量未行＝如实登记，禁造假阳性）
- 实测命令：`bash p4-pretooluse-stdin-fields.sh`
- 证据①（代码层 grep 复真·§19 buildAgentTrigger 行）读数：`grep -c executePreToolUseHooks` = **3**；`buildAgentTrigger` 定义摘录：`function buildAgentTrigger(t){…i.agent_type=n…t.storeId&&(i.agent_id=t.storeId)…}`（payload 注入 agent_id/agent_type 坐实）；payload 组装点摘录：`executePreToolUseHooks(t,i,n,s,c,p){let h={session_id:…,transcript_path:s,cwd:…,hook_event_name:"PreToolUse",tool_name:t,tool_input:i,call_id:p,tool_use_id:p,…buildAgentTrigger(n)}…}`（stdin 字段清单代码层形态＝session_id/transcript_path/cwd/hook_event_name/tool_name/tool_input/call_id/tool_use_id/agent_id/agent_type）。
- 证据②（运行时触发回显）读数：scratch 项目 `.codebuddy/settings.json` 挂 PreToolUse dump 钩子后起 headless 会话，CLI 回显 `Authentication required. Please use /login command to sign in to your account`＝独立 headless 会话需登录鉴权，无桌面会话令牌可复用；stdin dump 未产生。运行时字段回显项 INCONCLUSIVE。
- 票面验收判据 4 状态说明：`executePreToolUseHooks` grep 命中读数块在场（本报告与 p4 回执均有）；「stdin 字段回显」块以代码层 payload 字段清单＋运行时受阻环境读数形态在场（票面 T01-A 明令运行时不可行项如实登记 inconclusive）。
- QA 复核结论栏：（待 QA 席填写）

## P5 事件并发时序
- 状态：**inconclusive**
- 实测命令：`bash p5-event-concurrency-timing.sh`
- 读数摘录：代码面隔离键计数 `preToolUseHookResults`=28、`toolPermissionDecisionSnapshots`=10、`_toolStartTimes`=9、`cachePreToolUseResult`=13＝hook 结果按 session＋call_id 键控缓存（按调用隔离坐实）；跨席位事件全局到达顺序无任何串行化承诺可 grep。两席同刻工具事件需活跃团队运行态，脚本侧无法构造——时序可依赖性未证实未证伪。
- QA 复核结论栏：（待 QA 席填写）

## P6 deny 跨席位一致性
- 状态：**inconclusive**
- 实测命令：`bash p6-deny-cross-seat-consistency.sh`
- 读数摘录：`permissionDecision` 计数=114；`executePreToolUseHooks` call/def 站点=4；主工具路径与 MCP 工具路径共用同一决策管道读数在场（`"deny"===ev.permissionDecision`→decision outcome rejected；主路径 `if(!N.allowed)`→block）；`allowUntrustedFrontmatterHooks` 信任闸在场。deny 词表与管道单源＝代码层坐实；跨席位（多 in-process 会话）同获同 deny 需运行期双席实测，脚本侧无法触发。
- QA 复核结论栏：（待 QA 席填写）

## P7 git 独立服务可建性
- 状态：**pass**
- 实测命令：`bash p7-git-standalone-service.sh`
- 读数摘录：`bare-init=OK`（本地裸仓可建）；`push-loop=OK`（file:// 协议推送闭环）；`non-ff-rejection=OK (push rc=1)`（拒非快进原生可达）；`denyNFF-config=OK`＋回读 `true`（`receive.denyNonFastforwards`）；`pre-receive-branch-guard=OK (push rc=1)`（保护分支＝服务端 pre-receive 分支级拒绝最小原生实现可达）。仅验可建性；远端服务运维不验（§11 人类侧外置物）。
- QA 复核结论栏：（待 QA 席填写）

## P8 MCP auth 形态（问句·无预设·只登记观测）
- 状态：**inconclusive**（票面纪律：问句无预设，探针内无判定逻辑，固定登记态）
- 实测命令：`bash p8-mcp-auth-shape.sh`
- 观测读数（不含结论预设）：
  - 盘上 `~/.workbuddy/mcp.json`（132 字节）：server 名 `comfy-roundabout-mcp`；每 server 键形态＝`type`/`url`；凭据字段在场计数=0（无内嵌 key/token/secret/authorization 样例）。
  - 盘上 `~/.workbuddy/mcp-approvals.json`（109 字节·条目 1）：键形态＝`<64位hex>::<serverName>` → 数值（时间戳）。
  - 打包件词面计数（不判义）：`oauth`(大小写变体)=255、`authorization`=180、`headers`=594、`mcp*auth`=72、`api_key`=68、`bearer`=33；`mcp-approvals.json` 文件名字面量在打包件中 NOT FOUND（该文件属 WorkBuddy 壳层非 CLI 打包件）。
- 结论栏＝无预设（P8 答案由消费面票据观测读数裁定·候裁单列 Q-03）。
- QA 复核结论栏：（待 QA 席填写·票面验收判据 6＝人工抽检项移交 QA）

## P9 派发记录导出
- 状态：**pass**
- 实测命令：`bash p9-dispatch-record-export.sh`
- 读数摘录：`~/.workbuddy/tasks/*/*.json`＝115 条任务记录·6 个任务板（按团队分目录）；记录键集（纯 JSON·可机读导出）＝activeForm/blockedBy?/createdAt/description/id/owner?/status/subject/updatedAt；导出往返样例在场（json.dumps 直接可导）。
- QA 复核结论栏：（待 QA 席填写）

## P10 第三方插件 hooks 同权性
- 状态：**pass**
- 实测命令：`bash p10-thirdparty-hooks-parity.sh`
- 读数摘录：`getHooks` 单管道读数＝settings hooks ∪ `loadHooksFromPlugins` ∪ scopedHookRegistry 同数组喂同一 `executeHooks`（同权进同一执行管道坐实）；插件 hooks 声明件路径字面量 `"hooks/hooks.json"` 在场；差异化读数＝全局关闭开关 `CODEBUDDY_DISABLE_EXTENDED_PLUGIN_HOOKS`＋`allowUntrustedFrontmatterHooks` 信任闸＝插件 hooks 同管道但有额外信任门；盘上已安装插件 `hooks/hooks.json` 计数=16。
- QA 复核结论栏：（待 QA 席填写）
