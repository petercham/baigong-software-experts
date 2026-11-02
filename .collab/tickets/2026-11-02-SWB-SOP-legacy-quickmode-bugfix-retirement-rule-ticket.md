# SWB-SOP-R1 · SOP 域随动规则票：quick-mode/bugfix-path 两卷收编＋lead 卡豁免句删除＋§20.1①–⑥ 同票处置（规则票·L2·架构席起草）

- 起草实测 HEAD：`7ba8db5`（开工须实测 HEAD 为其后，读数入回执）。
- 票型＝**规则票**（v2.8 §12 L2 通道四类之一；修票权＝提案席位修）。设计依据＝v2.8 §20.1 末段（登记件 `.collab/refs/external/SWB-交接件v2.8-产品设计与架构设计-2026-11-02.md` 物理 L275·只读）：「quick-mode/bugfix-path 两卷就地收编（退役头注＋指向替代形态，不物理删除）、lead MD:34 豁免句删除——**执行载体＝SOP 域随动规则票一张（随收口批、T01 放行前落盘；票面：起草＝架构席（规则票→提案席位修）、执行＝工程师席经当票租约 path_globs）**，①–⑥ 所涉卷内条款同票处置」＋主笔席全票复核报告（`7ba8db5`）§五放行门②。
- **本票只起草落盘，不开工执行**——执行候皮总放行指令后经当票租约 path_globs 派工程师席；落盘时点纪律＝**T01 放行前**。
- 前验核证（起草已盘上直读实测·开工复测后方可落笔）：两卷现态＝`quick-mode.md` 29 行／`bugfix-path.md` 20 行（两卷 L3 均为「本件承载…逐字下沉件」声明行）；lead 卡 L34 实物＝`- ❌ 禁止跳过前序阶段直接进入后续阶段（快速模式/BugFix 快捷路径除外）`（待删串 `（快速模式/BugFix 快捷路径除外）` 实测 20 字符含全角括号，该行唯一命中）。

## 声明闭集（12 件·本票唯一可写面）

- 声明闭集：
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

## 逐条施工规格（行位＝起草实测现盘行号·逐字文本）

### S-A 两卷就地收编（§20.1⑦ 主面·不物理删除）

- **quick-mode.md**：L3（承载声明行）之后插两行（空行＋头注）：
  ```
  > **退役声明（v2.8 §20.1⑦）**：本档「快速模式」工作流档位已被**维护票**替代（架构 §3 票型八类之⑧／表2-3 维护行／§17 词条 36 准入四判据：无 API 变更／无数据迁移／单域文件集／可逆回滚）。无 API 变更之轻量工作由维护票承接；涉 API 变更之轻量工作回归标准流（触接口变更不设轻量通道）。本档保留为技法参考，不作跳阶段依据。
  ```
- **bugfix-path.md**：L3 之后插同款两行，档位名换「BugFix 快捷路径」其余逐字同。
- 两卷正文其余逐字节零触碰（收编＝加性头注，非改写）。

### S-B lead 卡豁免句删除（§20.1⑦ 指名面）

- `software-company-team-lead.md` L34：整串删除 `（快速模式/BugFix 快捷路径除外）`（20 字符含全角括号），删后该行＝`- ❌ 禁止跳过前序阶段直接进入后续阶段`，行首 `- ❌ ` 及其余逐字保留。
- L45–59 路由四档表与 L94「首先判断工作流类型（快速模式/BugFix/标准 SOP/部分工作流）」＝**本票不动**（路由档位描述面随退役声明读法降级为技法参考；档位表整表重构属席位卡装填面＝T05 闭集，不在此扩面）。

### S-C §20.1①–⑥ 所涉卷内条款同票处置（过渡口径标注·20.2④ 体例·加性不删原文）

统一模板行（各落点插于指名行/节之后一行）：`> **过渡口径（v2.8 §20.1·X）**：<替代形态句>（旧条款保留为技法面，验收结论一律以 SWB v2.8 基线为准）`。逐落点（X＝条款号）：

| 条款 | 落点（路径:行·起草实测） | 替代形态句（逐字） |
|---|---|---|
| ① | `agents/software-qa-engineer.md` L71 节头后 | QA 两轮上限→三段式机械判绿＋缺陷票回流 |
| ② | `agents/software-engineer.md` L88「Output a verdict:」前 | IS_PASS 自审出口→制度③＋三段式 |
| ② | `skills/.../references/standard-sop.md` L33 后 | 同② |
| ④ | `agents/software-qa-engineer.md` L57 节头后 | 智能路由三态分派→回流四型＋B2 状态机迁移 |
| ④ | `agents/software-company-team-lead.md` L90 后 | 同④ |
| ⑤ | `skills/.../references/deploy-gate.md` L32 节头后 | 独立 deploy-gate 四段卷→发布硬门禁二＋灰度机械门禁＋转正代写（四段流程保留为装配运维面） |
| ⑥ | `skills/.../references/dev-discipline.md` L42 后 | 人工回执全等对账→B2/B5 账本（回执保留为申报载体） |
| ①④⑤⑥ 汇总 | `skills/software-orchestration/references/standard-sop.md` L43 后 | ①＋④（同①④句合并一行） |

- **③ 落点说明（起草裁量·登记不候裁）**：③「QA 自写自判测试链」在两卷/席位 MD 无直接成文句（qa MD L53–90 为写测试跑测试技法，非结论权条款）——处置面选 qa MD「## Test Writing Standards」节头（实测 L90）后插③句：`工程师写脚本/CI 机械执行/QA 出结论（存量测试资产保留为技术面，不作验收结论源）`。

### S-D SKILL.md 索引随动

- L16/L17 两行「何时必读」列行内改：`判定走 ⚡ 快速模式后` → `技法参考（档位已退役 v2.8 §20.1⑦·轻工作量走维护票）`；`判定走 🔧 BugFix 快捷路径后` → 同款。description（L3）触发词**不动**（退役为语义层，触发词保留无害，避免 description 长串重写）。
- frontmatter `version: 1.1.2` → `1.1.3`（组件版本与 SKILL.md 同源纪律·README v0.1.13 先例）。

### S-E 版本账随动（纪律①每变必 bump·三处同源）

- `.codebuddy-plugin/plugin.json` L3：`"version": "0.1.13"` → `"0.1.14"`。
- `bundle.lock` L5：`"version": "0.1.13"` → `"0.1.14"`（bundle 本体行；components 两行零触碰）。
- `README.md` 版本账区 L39（v0.1.13 行）之前**新增一行**：`- **版本账 v0.1.14**（2026-11-0x·SOP-R1 规则票·v2.8 §20.1 收编批）：quick-mode/bugfix-path 两卷退役头注收编＋lead 卡豁免句删除＋§20.1①–⑥ 过渡口径标注八落点＋SKILL.md 索引两行随动 1.1.2→1.1.3；plugin.json＋bundle.lock 双 0.1.14。依据＝SWB v2.8 基线 §20.1⑦（三方收口 3fb8c47）。`（日期落笔时实填）。

## 验收判据（全部机械可判·回执附逐项读数）

1. `grep -c '快捷路径除外' deliverables/experts/baigong-software-team/agents/software-company-team-lead.md` ＝**0**。
2. 两卷退役头注命中各＝1（`grep -c '退役声明（v2.8 §20.1⑦）'`）；两卷行数＝**29→31／20→22**（各＋2·加性）。
3. 过渡口径标注行全落：`grep -rc '过渡口径（v2.8 §20.1' <qa MD／engineer MD／standard-sop／deploy-gate／dev-discipline／lead 卡>` 逐文件＝**1/1/2/1/1/1**（合计 7＋③ 落 qa MD＝qa MD 计 2 行，总 8 落点具名对账表入回执）。
4. 版本三同源：plugin.json L3＝bundle.lock L5＝`0.1.14`；SKILL.md `version: 1.1.3`；README `版本账 v0.1.14` 行在位——四 grep 各命中 1。
5. 闭集对账：`git show --name-only <执行笔>` 与声明闭集 12 件＋回执全等（dev-discipline §三 回执口径）；闭集外 `git status deliverables/` 零改动。
6. 禁动面复核：software-orchestration 其余五卷（collab-rules/delivery-summary/handoff-discipline/incremental-dev/partial-workflows）＋PRODUCT.md/ARCHITECTURE.md/avatars／`deliverables/skills/` 三包／票包七件／`.collab/` 全域（回执除外）——git 状态零改动。

## 票间关系

- 前置：无（§20.1⑦ 随 v2.8 收口即生效）。后置：T01 放行须在本票**落盘**后（§20.1⑦ 明文「T01 放行前落盘」——落盘＝本票面在盘；**执行**可在放行前后由皮总排程，但须先于 T05 落盘前完成 lead 卡面处置或按候裁 R1 定点顺位）。
- 与 T05 关系：20.2③ 旧席位卡五件于 T05 落盘即退役（替换非并存）——本票 S-B/S-C(lead 卡④) 动的是**旧名族**卡文件；见候裁点。

## 禁动面（零触碰）

- 上判据 6 所列其余卷与文件；`deliverables/skills/` 三包（external-advisor-collab/deep-research/multi-collab 域）；票包七件；两基线登记面；`.collab/` 全域（回执除外）。
- 执行席不得改本票票体四字段；不得顺手改写路由四档表（L45–59）——属 T05 装填面。

## 候裁点（单列·不自行拍）

- **R1（与 CR-7 同源）**：本票 lead 卡落点按现盘名 `software-company-team-lead.md`；若 T05 先执行落新名族 `software-team-*.md`，则 S-B/S-C 落点应随新名族卡（新卡按 v2.8 §8 本就无豁免句，S-B 自动免执）。两族顺位＝决策者定点（随 CR-7 一并呈）；本票规格按现盘面落，顺位裁定不影响其余面。
- 无新增候裁（③ 落点选择属起草裁量已具名 S-C 说明，不候裁）。

## 回执

落 `.collab/receipts/2026-11-02-SWB-SOP-R1-receipt.md`：开端 HEAD＋前验读数（两卷行数/L3 内容＋lead L34 实物串）＋判据 1–6 逐项实测读数＋八落点对账表（条款号×路径×行位×标注句）。commit 单独笔，`collab:` 前缀只含本票闭集件＋回执。
