# SWB-T04 强制机制群：B5＋B7＋B8＋B10＋B11（写侧校验与提交审计等）（施工票·L3·架构席起草）

- 开端读数：ANCHOR＝08fc5ee（见总览件）；开工时实测 HEAD 附回执。
- 设计真源：`.collab/refs/external/SWB-交接件v2.8-产品设计与架构设计-2026-11-02.md`（现行基线＝v2.8 三方收口（PM-R10 `cd5d959`＋QA-R10 `5e30e50`）·MERGE-V11 正式登记回执 `3fb8c47`；V11 行号前缀（V11 n＝落盘物理 n−27）；产品本体 V11 L26–80 sha256=20a96da5…；架构本体 V11 L81–253 sha256=66aab921…；纯 LF）。
- 背景（自包含）：承接消费面声明第②项「写侧校验规则←表2-1 不可写列＋提交审计」（V11 L233；不可写列 V11 L95–104）。覆盖构件：B5 写侧校验与提交审计、B7 签名、B8 影子重放、B10 停刀、B11 记忆中立化（§9 V11 L178–191）。违纪模式表拦截面承接：行 2「越租约路径写入→U2＋B5 deny」、行 5「绕过脚本直改账本→U5＋B2 日志互验」（B5 面）、行 6「检索自救→U7＋B11 读侧扫描（P3 能力面未验证，只作辅助面不作假设）」、行 7「无票提交/amend/rebase→B5 提交审计＋日终对账」、行 11「过程件被用作引用目标→B8 引用可达性扫描＋B11 下游件引用扫描」、行 14「停刀延迟超阈→B10＋deny−freeze≤60s」。**票面纪律镜像 §10：B5 主路以 P4 读数为准，P4 运行时未过前不得把 stdin 完整性当已成立闸前提——主路/退路双形并列，择路由候裁 Q-04。**
- 前置票：T01（P4/P5/P6 读数）、T02（租约台账＋`deny_globs` 数据源＋账本记录类）。

## 声明闭集（10 件·本票唯一可写面）
- 声明闭集：
- deliverables/experts/baigong-software-team/hooks/hooks.json
- deliverables/experts/baigong-software-team/skills/sop/scripts/write-guard.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/commit-audit.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/liveness-selfcheck.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/freeze-unfreeze.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/memory-neutralize.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/shadow-replay.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/sign-verify.py
- deliverables/experts/baigong-software-team/config/seat-permissions-hooks-map.json
- deliverables/experts/baigong-software-team/tests/s4/test_enforcement.py

## 逐条施工规格

### T04-A hooks.json（平台事件强制·§5 工件矩阵 V11 L143–151）
- PreToolUse matcher：写类工具 → `write-guard.py`；Read/Grep matcher → `memory-neutralize.py`（§9 B11 行）。
- PostToolUse：记账 → `commit-audit.py`（§9 B5 行「PostToolUse 记账＋对账＋活性自检」）。
- 拦截规则不装业务逻辑（§5「不装什么」列）。
- 决策词表锚点（§19 V11 L244）：`permissionDecision` 取 deny/ask；exit 2→blocking；本文件只用该词表既有值，不自造。

### T04-B write-guard.py（B5 写侧校验·消费面②落点）
- 主路（P4 运行时 pass）：PreToolUse stdin 直读 `agent_id`/`agent_type` → 查租约台账（T02 lease 记录）→ 路径 ∉ 租约 path_globs ∨ 路径 ∈ `seat-permissions-hooks-map.json` 的 deny_globs（源＝表2-1「明确不可写」列逐席位转录）→ `permissionDecision: deny`（U2/G1）。
- 退路（P4 运行时 negative）：SubagentStart 状态文件形态（§9 B5 行「P4 阴性→SubagentStart 状态文件，人类拍板启用」）——实现同判据、身份源换为状态文件；启用与否候裁 Q-04，票面两形同交付、缺省不启用退路。
- 每次 deny 写「写入」记录＋触发「租约越界 deny」呈报码（§4 触发源六闭集第一项）。

### T04-C commit-audit.py（B5 提交审计）
- 拦三形态：amend／rebase／orphan 提交（无票 ID trailer，§17 词条）→ exit 2 blocking；
- B0 退路补位：P7 阴性时拦 force-push（§9 B0 退路「PreToolUse 拦 force-push/amend」）；
- PostToolUse 记账：提交哈希/票 ID/席位归因入「写入」记录类。

### T04-D liveness-selfcheck.py（B5 活性自检）
- 形态＝§17「先注入必中事件再读统计」：注入一条哨兵 deny 请求→断言统计计数+1→失败写「活性自检失败」呈报码（§13 指标异常闭集第二项）。

### T04-E freeze-unfreeze.py（B10 停刀）
- 动作链＝§9 B10 行逐字：freeze 清租约 → 全写 matcher 置 deny → 终止实例；解冻/吊销仅人类直通触点触发（表2-2 V11 L123「脚本不得自触发」——脚本无自动触发路径，入口带人类令牌校验）。
- 成值时限（§13 V11 L208）：deny−freeze ≤ **60s**（缺省，可配但缺省即 60）；P6 阴性时按退路「逐席显式 deny 列表」实现配置面（启用候裁 Q-05 随 P6 读数）。
- 一键冻结＝紧急直通三通道之首（§4/§17）。

### T04-F memory-neutralize.py（B11 记忆中立化）
- 两面扫描（§9 B11 行）：①Read/Grep matcher 扫描记忆文件读取→引用记忆作流程状态即拦/标；②下游件引用扫描：新增/修改件文本出现记忆文件路径引用→报「引用扫描命中」呈报码（§4 触发源第四项）。
- 对应 U6/G1-G2、违纪行 1（B11 面）。诚实边界：U7 保证＝「P3[未验证]＋G5 辅助面」（§7 V11 L164）——本脚本只实现读侧检出面，不声明阻断性能力面保证。

### T04-G shadow-replay.py（B8 影子重放）
- 输入＝`.collab/ledger/`＋`.collab/archive/`＋注入存档（§9 B8 行·v2.8 布局）；输出＝差异三分类记录＋引用可达性扫描结论（过程件被引用即命中，违纪行 11）。
- 失效＝重实现（不涉平台依赖）。

### T04-H sign-verify.py（B7 签名·fail-closed）
- gpg 验签封装：签名件（`.collab/human/reviews/` 形态·v2.8 表2-1 人类行）验签＋身份锚比对；**刻意无降级**（§9 B7 行）：gpg 不可用→exit≠0 硬失败，禁 fallback。
- 密钥生成/保管＝人类离线自持动作（§11 密钥根行），不在票内；票内只交付验证侧脚本与验签记录入账。

### T04-I seat-permissions-hooks-map.json
- 由 T02 `seat-permissions.json` 派生 `deny_globs` 的 hooks 消费形态（表2-1「明确不可写」列）；头部注 `derived_from: seat-permissions.json (表2-1)`；与源件一致性断言在测试内。

## 验收判据（全部机械可判）
1. `python -c "import json;h=json.load(open('deliverables/experts/baigong-software-team/hooks/hooks.json'));assert h"` 退出 0 且文件含 PreToolUse/PostToolUse 两键（grep 读数）；
2. deny 冒烟：无租约状态下样例写请求经 write-guard → 输出含 `"permissionDecision":"deny"`（读数入回执）；
3. orphan 提交冒烟：构造无票 trailer 样例提交描述 → commit-audit exit＝2；amend/rebase 样例各 exit＝2（三读数）；
4. `python deliverables/experts/baigong-software-team/skills/sop/scripts/liveness-selfcheck.py` 退出 0 且账本「呈报」类无「活性自检失败」新增；停用 hooks 后重跑 → exit≠0 且新增该呈报码恰 1 条（双向读数，§17 活性自检定义的正反两态）；
5. freeze 冒烟：触发 freeze → 断言链「租约清空→全写 deny→实例终止」三步读数齐且耗时 ≤60s（脚本自计时回显）；
6. B11 冒烟：样例下游件含记忆路径引用 → memory-neutralize 命中码回显；
7. sign-verify 对伪造签名 exit≠0、对 gpg 缺失环境 exit≠0（fail-closed 两读数）；
8. `python deliverables/experts/baigong-software-team/tests/s4/test_enforcement.py` 退出 0；
9. 派生一致性断言：seat-permissions-hooks-map.json 的 deny_globs 席位集 ⊆ seat-permissions.json 席位集且每席位非空（测试内断言，读数入回执）。

## 票间关系
- 前置：T01、T02。后置：T05（席位卡脚本调用清单引用本票实体名；六条演练「写侧拦截／停刀-恢复／重放对账」三链消费本票产物）。

## 禁动面（零触碰）
- 两基线登记件本体、`.collab/` 全域（回执除外）、`docs/`、T01/T02/T03/T05 声明闭集全部文件。
- B0 账本历史 append-only 不回改；工程师不得改本票票体四字段。

## 候裁点（单列·不自行拍）
- Q-04：P4 运行时读数阴性 → SubagentStart 状态文件退路是否启用（§9 B5 行明示「人类拍板启用」）。
- Q-05：P6 读数阴性 → B10 退路「逐席显式 deny 列表」启用（§9 B10 行）。
- B7 密钥根生成/轮换属人类侧密钥自持动作，票面不代拍（§11）。

## 回执
落 `.collab/receipts/2026-11-01-SWB-T04-receipt.md`：开端 HEAD＋完整文件清单＋判据 1–9 实测读数。commit 单独笔，`collab:` 前缀只含本票闭集件。
