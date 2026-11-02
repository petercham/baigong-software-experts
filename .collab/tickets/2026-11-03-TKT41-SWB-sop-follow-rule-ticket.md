# TKT41 · SOP 域随动规则票（§20.1⑦ 落盘票·V13 口径·quick-mode/bugfix-path 两卷收编＋lead 卡豁免句删除＋§20.1①–⑥ 同票处置·规则票·L2·架构席起草）

- 起草实测 HEAD：`d3ca3ad`（MERGE-V13 收口链上·QA-MERGE-V13 回执誊录登记笔；开工须实测 HEAD 为其后，读数入回执）。起草时实盘未见 TKT40 票体入库（`ls .collab/tickets/ | grep TKT40`＝0）与其余并行起草笔入库；仅两份 2026-11-01 TKT qa 汇编件仍 untracked（候处置池·零触碰）。
- 票型＝**规则票**（§12 L2 变更通道四类之一·V13 L177；修票权＝提案席位修）。本票止于票面起草落盘，**不开工执行**——执行＝工程师席经当票租约 path_globs。
- 编号注记：40 号留与并行换锚票（TKT40·V12→V13·另一架构席），本票取 41；两票无依赖（见§六票间关系）。

## 〇、依据（逐字摘录·python 实跑取值·V13 行号口径）

- 现行基线件＝`.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md`（260 物理行·头块 28 行·恒等式 **V13 n＝物理 n−28**·贴文正文 232 行；三哈希：全文（物理 L29–260）`3f335333e0fe4bc2a3532688588a6fde5a313981ef8bf04fc05ff8a1934ccb9b`／产品件本体（V13 L1–56）`7214ad14259b175fd6912806e2b3a7bb3655ff35053098f9ed5df66c2d9691f3`／架构件本体（V13 L57–232）`efb4f7658c1e5555fcf310cdf4ae91ecbf6ce5cfe19c420c293e0e62cc1078c4`；起草复算三值与头块落定值逐字相等）。
- **§20.1⑦ 条款原文（V13 L227＝物理 L255·逐字）**：
  > ⑦**快速模式/BugFix 两档及 lead 卡“快捷路径除外”豁免句→维护票（§3⑧/表2-3）为唯一合法轻量形态**：无 API 变更之轻量工作由维护票承接（准入四判据），涉 API 变更之轻量工作回归标准流（设计裁定：触接口变更不设轻量通道）。quick-mode/bugfix-path 两卷就地收编（退役头注＋指向替代形态，不物理删除）、lead MD:34 豁免句删除——**执行载体＝SOP 域随动规则票一张（随收口批、施工首票放行前落盘；票面：起草＝架构席（规则票→提案席位修）、执行＝工程师席经当票租约 path_globs）**，①–⑥ 所涉卷内条款同票处置。
- 程序去向登记（`.collab/qa/2026-11-03-R13-双席会师-三方收口登记-v1.md` 物理 L35·逐字）：
  > MERGE-V13 剥壳落盘（正式登记件＋三锚随本批 commit 号回填＋壳面编号随批轻注＋K-1/K-3/QA-1 清单定稿注记随批）→ TKT40 换锚（V12→V13）→ SOP 域随动规则票落盘（§20.1⑦·施工首票放行前）→ T01 放行恢复 → T02–T06 串行。
- 维护词条与判据（V13 L202 §17 维护票词条·逐字节引）：`**维护票**——节点 1–3 合并为轻签点（产品＋架构合签）、节点 4–6 全保的轻量票型；准入四判据：无 API 变更／无数据迁移／单域文件集／可逆回滚。`；轻签点表注（V13 L110）：`未达准入判据（§17 维护票词条）而走维护票→转流程变更票重审`。§3 票型八类清单见 V13 L113（维护＝第⑧类）；表2-3 维护行见 V13 L108。
- **落点文件实测结论（起草实测）**：①交付树 SOP 域（`deliverables/` 全域 md/json）基线引用串 `v2\.9|V13 L|V12 L|交接件v2` grep -o 命中＝**0**——SOP 域现盘不承载「引用基线版本」条款，本票落点与 TKT40 换锚面零交集，**规则文本不候 TKT40，本票无硬前置**；②「票包引用基线版本」条款承载面＝`.collab/tickets/README.md` L5/L17（现载 V12/11-02 件三哈希 f25a89ee/14605e18/17f4843a）＋票包七件各 L4 锚行——该面＝TKT40 职权面，本票禁动。
- 前验核证（起草盘上直读实测·开工复测相等方可落笔）：两卷现态＝`quick-mode.md` 29 行／`bugfix-path.md` 20 行（两卷 L3 均为「本件承载…逐字下沉件」声明行·锚文本见 S-A）；lead 卡 L34 实物＝`- ❌ 禁止跳过前序阶段直接进入后续阶段（快速模式/BugFix 快捷路径除外）`（待删串 `（快速模式/BugFix 快捷路径除外）` 实测 20 字符含全角括号、该行唯一命中）；plugin.json L3＝bundle.lock L5＝`"version": "0.1.13"`；SKILL.md frontmatter `version: 1.1.2`。

## 一、声明闭集（12 件·本票唯一可写执行面）

- deliverables/experts/baigong-software-team/skills/software-orchestration/references/quick-mode.md
- deliverables/experts/baigong-software-team/skills/software-orchestration/references/bugfix-path.md
- deliverables/experts/baigong-software-team/agents/software-company-team-lead.md
- deliverables/experts/baigong-software-team/agents/software-qa-engineer.md
- deliverables/experts/baigong-software-team/agents/software-engineer.md
- deliverables/experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md
- deliverables/experts/baigong-software-team/skills/software-orchestration/references/deploy-gate.md
- deliverables/experts/baigong-software-team/skills/software-orchestration/references/dev-discipline.md
- deliverables/experts/baigong-software-team/skills/software-orchestration/SKILL.md
- deliverables/experts/baigong-software-team/.codebuddy-plugin/plugin.json
- deliverables/experts/baigong-software-team/bundle.lock
- deliverables/experts/baigong-software-team/README.md

## 二、逐目施工规格（行位＝起草实测现盘行·落位一律以「落点」列逐字文本锚为准；同文件多落点按行号降序落笔·先深后浅）

### S-A 两卷就地收编（§20.1⑦ 主面·加性头注·不物理删除）

- **quick-mode.md**：L3 承载声明行（锚文本起段 `> 本件承载 \`software-company-team-lead.md\`（fork v1.2.0）§⚡ 快速模式`）之后插两行（空行＋头注）：
  ```
  > **退役声明（v2.9 §20.1⑦）**：本档「快速模式」工作流档位已被**维护票**替代（架构 §3 票型八类⑧／表2-3 维护行／§17 维护票词条·准入四判据：无 API 变更／无数据迁移／单域文件集／可逆回滚）。无 API 变更之轻量工作由维护票承接；涉 API 变更之轻量工作回归标准流（触接口变更不设轻量通道）。本档保留为技法参考，不作跳阶段依据。
  ```
- **bugfix-path.md**：L3 之后插同款两行，档位名换「BugFix 快捷路径」其余逐字同。
- 两卷正文其余逐字节零触碰。

### S-B lead 卡豁免句删除（§20.1⑦ 指名面）

- `agents/software-company-team-lead.md` L34：整串删除 `（快速模式/BugFix 快捷路径除外）`（20 字符含全角括号），删后该行＝`- ❌ 禁止跳过前序阶段直接进入后续阶段`，行首 `- ❌ ` 及其余逐字保留。
- L45–59 路由四档表与 L94「首先判断工作流类型（快速模式/BugFix/标准 SOP/部分工作流）」＝**本票不动**（路由档位描述面随退役声明读法降级为技法参考；档位表整表重构属席位卡装填面＝T05 闭集，不在此扩面）。

### S-C §20.1①–⑥ 所涉卷内条款同票处置（过渡口径标注·20.2④ 体例·加性不删原文）

统一模板行（各落点插于指名行/节之后一行）：`> **过渡口径（v2.9 §20.1·X）**：<替代形态句>（旧条款保留为技法面，验收结论一律以 SWB v2.9 基线为准）`。逐落点（X＝条款号·锚文本均起草实测在盘）：

| 条款 | 落点（路径:行·起草实测·锚文本） | 替代形态句（逐字） |
|---|---|---|
| ① | `agents/software-qa-engineer.md` L71 节头 `## Test Round Control (STRICT — MAX 2 ROUNDS)` 后 | QA 两轮上限→三段式机械判绿＋缺陷票回流 |
| ② | `agents/software-engineer.md` L87 `- No duplicate implementations across files` 之后一行（＝L88 前） | IS_PASS 自审出口→制度③＋三段式 |
| ② | `skills/.../references/standard-sop.md` L33 `   - 全部文件完成后执行 **全局一致性审查**（IS_PASS: YES/NO）` 后 | 同② |
| ④ | `agents/software-qa-engineer.md` L57 节头 `#### Smart Routing Decision (CRITICAL):` 后 | 智能路由三态分派→回流四型＋B2 状态机迁移 |
| ④ | `agents/software-company-team-lead.md` L90 `   - QA 每轮测试后必须做出智能路由判定（Engineer/QA/NoOne）` 后 | 同④ |
| ⑤ | `skills/.../references/deploy-gate.md` L32 节头 `## 五、四段部署流程（2026-10-28 皮总定口径：装配 → 预览 → 人类闸 → 部署）` 后 | 独立 deploy-gate 四段卷→发布硬门禁二＋灰度机械门禁＋转正代写（四段流程保留为装配运维面） |
| ⑥ | `skills/.../references/dev-discipline.md` L42 `2. 对账口径＝\`git show --name-only <commit>\` 与回执清单**全等**；缺项/多项＝违例（回执失真）。` 后 | 人工回执全等对账→B2/B5 账本（回执保留为申报载体） |
| ①④ 汇总 | `skills/software-orchestration/references/standard-sop.md` L43 `   - **最多 2 轮测试**：第 1 轮发现问题反馈修复，第 2 轮回归验证。2 轮仍不过则输出报告标注遗留问题` 后 | （①＋④合并一行） |

- **③ 落点说明（起草裁量·登记不候裁·承 SOP-R1 既有裁量）**：③「QA 自写自判测试链」在两卷/席位 MD 无直接成文句——处置面＝qa MD `## Test Writing Standards` 节头（实测 L90）后插③句：`工程师写脚本/CI 机械执行/QA 出结论（存量测试资产保留为技术面，不作验收结论源）`。

### S-D SKILL.md 索引随动

- L16/L17 两行「何时必读」列行内改：`判定走 ⚡ 快速模式后` → `技法参考（档位已退役 v2.9 §20.1⑦·轻工作量走维护票）`；`判定走 🔧 BugFix 快捷路径后` → 同款。description（L3）触发词**不动**（退役为语义层，触发词保留无害）。
- frontmatter `version: 1.1.2` → `1.1.3`（组件版本与 SKILL.md 同源纪律·README v0.1.13 先例）。

### S-E 版本账随动（纪律①每变必 bump·三处同源）

- `.codebuddy-plugin/plugin.json` L3：`"version": "0.1.13"` → `"0.1.14"`。
- `bundle.lock` L5：`"version": "0.1.13"` → `"0.1.14"`（bundle 本体行；components 行零触碰）。
- `README.md` 版本账区 v0.1.13 行（实测 L39·锚文本起段 `- **版本账 v0.1.13**（2026-10-31·纪律落点批·SOP-B1）`）之前**新增一行**：`- **版本账 v0.1.14**（2026-11-03·TKT41 SOP 域随动规则票收编批）：quick-mode/bugfix-path 两卷退役头注收编＋lead 卡豁免句删除＋§20.1①–⑥ 过渡口径标注九落点＋SKILL.md 索引两行随动 1.1.2→1.1.3；plugin.json＋bundle.lock 双 0.1.14。依据＝SWB v2.9 基线 §20.1⑦（V13 L227·全文 sha256 3f335333…）。`

## 三、验收判据（全部机械可判·回执附逐项读数·计数口径＝occurrence `grep -o | wc -l`）

0. 开工前验：`grep -roE 'v2\.9|V13 L|交接件v2' deliverables/ | wc -l`＝**0**（与§〇实测一致方可落笔）；两卷行数 29/20；lead L34 实物串在位；plugin/lock 双 `0.1.13`；SKILL `version: 1.1.2`。
1. `grep -c '快捷路径除外' deliverables/experts/baigong-software-team/agents/software-company-team-lead.md`＝**0**。
2. 退役头注命中各＝1（`grep -c '退役声明（v2.9 §20.1⑦）'`）；两卷行数＝**29→31／20→22**（各＋2·加性）。
3. 过渡口径标注行全落：`grep -rc '过渡口径（v2.9 §20.1'` 逐文件 qa MD／engineer MD／standard-sop／deploy-gate／dev-discipline／lead 卡＝**3/1/2/1/1/1**（qa MD＝①L71＋④L57＋③节头后三行；合计＝**9 落点**；具名对账表九行含③行入回执）。
4. SKILL 随动：`grep -c '技法参考（档位已退役 v2.9 §20.1⑦' SKILL.md`＝**2**；`判定走 ⚡ 快速模式后`／`判定走 🔧 BugFix 快捷路径后` 各＝**0**；`version: 1.1.3`＝1。
5. 版本三同源：plugin.json L3＝bundle.lock L5＝`0.1.14`（各 grep 命中 1）；SKILL.md `version: 1.1.3` 命中 1；README `版本账 v0.1.14` 行在位命中 1。
6. 基线引用面断言：执行后 `grep -rc 'v2\.9'` 逐文件＝quick 1／bugfix 1／lead 1／qa 3／engineer 1／standard-sop 2／deploy-gate 1／dev-discipline 1／SKILL 2／README 1／PRODUCT 0／ARCHITECTURE 0（合计 **14**）；`grep -ro 'V13 L' deliverables/ | wc -l`＝**1**（README 版本账行内）。
7. 闭集对账：`git show --name-only <执行笔>` 与声明闭集 12 件＋回执全等（dev-discipline §三 回执口径）；闭集外 `git status deliverables/` 零改动。
8. 禁动面复核：§五所列各面 git 状态零改动。

## 四、执行与程序

- 起草笔＝本票面一件单独 commit（`collab:` 前缀）；执行笔＝单独 commit 只含闭集 12 件＋回执。执行席＝工程师席（当票租约 path_globs 限§一闭集）；起草＝架构席（本票）。**起草席禁施工**。
- 回执落 `.collab/receipts/2026-11-03-TKT41-sop-follow-rule-receipt.md`：开端 HEAD＋判据 0 复测读数＋判据 1–8 逐项实测读数＋九落点对账表（条款号×路径×行位×锚文本×标注句）。

## 五、票间关系与禁动面

- 前置＝V13 正式登记件在盘（已在盘·`d3ca3ad` 链上）；**TKT40 非本票前置**（§〇实测①：交付树基线引用零命中，两票闭集无交集）。后置＝T01（施工首票）放行须在本票**落盘**后（§20.1⑦ 明文「施工首票放行前落盘」——落盘＝本票面在盘；**执行**可经放行前后由决策者排程，但 lead 卡面处置须先于 T05 落盘前完成或按候裁 R1 定点顺位）。
- 与 **SOP-R1**（`.collab/tickets/2026-11-02-SWB-SOP-legacy-quickmode-bugfix-retirement-rule-ticket.md`·94 行·候执行）关系：本票＝§20.1⑦ 随 V13 基线的**换锚执行面**——本票落盘后 SOP-R1 转历史票面（append-only 留存原位·不再具执行授权），§20.1⑦「规则票一张」载体读本票；tickets/README L22 状态行随动（「SWB SOP 退役规则（候执行）」改指本票）＝架构席索引轻修或随主理人登记，**不在本票闭集**。SOP-R1 规格中 `v2.8 §20.1⑦`／`词条 36` 系旧基线读数，本票已按 V13 实物全部转制（`v2.9 §20.1⑦`／`§17 维护票词条`）。
- 与 **TKT40** 关系：并行零交集（TKT40 面＝票包七件＋tickets/README 基线行；本票面＝交付树 SOP 域 12 件）。
- 与 **T05** 关系：20.2③（V13 L228）旧席位卡五件于 T05 落盘即退役（替换非并存）——本票 S-B/S-C(lead 卡④) 动的是**旧名族**卡文件；见候裁点 R1。
- **禁动面（零触碰）**：software-orchestration 其余五卷（collab-rules/delivery-summary/handoff-discipline/incremental-dev/partial-workflows）＋PRODUCT.md/ARCHITECTURE.md/avatars／`deliverables/skills/` 三包／票包七件＋tickets/README.md／TKT40 票面与 SOP-R1 票面／三件登记面（两登记件＋交接件本体）／`.collab/` 全域（回执除外）。执行席不得改本票票体四字段；不得顺手改写路由四档表（L45–59）——属 T05 装填面。

## 六、候裁点（单列·不自行拍·㊵闭集纪律：无真分歧不滥设）

- **R1（承 SOP-R1·与 CR-7 同源·非新设）**：本票 lead 卡落点按现盘名 `software-company-team-lead.md`；若 T05 先执行落新名族 `software-team-*.md`，则 S-B/S-C 落点随新名族卡（新卡按 v2.9 §8 本就无豁免句，S-B 自动免执）。两族顺位＝决策者定点（已随 CR-7 呈）；本票规格按现盘面落，顺位裁定不影响其余面。
- **新增候裁＝0**（③ 落点选择＝起草裁量已具名 S-C 说明，承 SOP-R1 既有裁量不候裁；换锚承继关系＝§20.1⑦「随收口批」条款的机械随动，无真分歧不立目）。
