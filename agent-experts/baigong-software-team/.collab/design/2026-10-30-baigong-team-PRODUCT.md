# 百工软件团队 · 产品设计说明书

> 文档性质：产品设计说明书（描述件）。被描述对象＝`baigong-software-team` 专家团包（Team 型多角色专家团）。
> 本件所述机制一律以包内相对路径指向真源（如 `skills/software-orchestration/references/dev-discipline.md`），条款细则以包内各卷为准，本文只做产品视角表述、不复述条文。

## 1. 产品定位

**一句话**：交付总监统筹产品、架构、工程、QA 四席，按固定 SOP 把需求推到可验收交付，每步留证据与判定级别的可审计多角色软件交付专家团。

**类型**：Team 型（多角色协作团队）。主对话入口为主理人席位（交付总监·齐活林），其余四席由主理人按需编排，用户无需直连任何成员席。

**出身背景**：本包为市场包 fork 自维护——基线＝WorkBuddy 专家中心市场包 `software-company` v1.1.0，fork 后经历本地形态适配、改名与版本升迁，后与旧血脉做身份切割、版本号自 0.1.0 重新起算，现行版本态 0.1.10。完整版本账（沿革全链）见包内 `README.md`「出身」节；本说明书不重复逐版记录。fork 的意义在于：市场版给协作骨架，本包在其上叠加了本地纪律层（写权边界、交接收口、部署硬门等），纪律卷皆在 `skills/software-orchestration/references/` 包内自包含。

## 2. 目标用户与使用场景

**谁在用**：需要在 WorkBuddy 内把"想法→可用软件"走完一段有质量关卡的交付过程的用户；需要有人替他把需求拆成可验收任务、把交付审出缺口的人。

**拿来干什么**（从席位定义与包门面路由表归纳）：

| 场景 | 典型请求 | 承接形态 |
|---|---|---|
| 需求拆解 | "把这个需求拆成可验收的开发任务，标出依赖、验收判据和预估改动面" | 产品席 PRD／架构席任务分解 |
| 中大型开发 | 多页面/多模块应用、前后端 combined | 🏗️ 标准 SOP 五席全链 |
| 小型开发 | 单页应用、小游戏、工具脚本 | ⚡ 快速模式（工程+QA 两席） |
| Bug 修复 | 明确 Bug 报告（非新功能） | 🔧 BugFix 快捷路径 |
| 审计验收 | "审这份交付或治理报告，按四态判定给结论，列出必须补的缺口" | QA 席独立核验出判词 |
| 市场调研 | 行业/竞品/定价分析 | 产品席研究模式出报告 |
| 讨论会主持 | 组织／主持／收口外部顾问讨论会、编制议题包与决议件 | 主理人席临时兼任主持人，加载 `external-advisor-collab` 技能按该技能程序执行 |

## 3. 能力地图（工作流路由）

主理人收到请求后**首先判档**，判档表内置于主理人席位 MD（`agents/software-company-team-lead.md`「工作流路由」节），各档细则下沉在 `skills/software-orchestration/references/` 对应分件，判定命中后第一件事读对应分件。五档：

| 档位 | 适用判定（一句话） | 细则卷 |
|---|---|---|
| ⚡ 快速模式 | 单页应用/小游戏/工具脚本等 ≤10 源文件的明确功能实现——跳过 PRD 与架构设计，工程直接实现、QA 验证；这是默认倾向档（"宁选快速模式，不选过重流程"） | `references/quick-mode.md` |
| 🔧 BugFix 快捷路径 | 用户报告的是明确 Bug 而非新功能——工程师定位修复、QA 回归测试两步走完 | `references/bugfix-path.md` |
| 🏗️ 标准 SOP | 多页面/多模块、涉及后端+前端、>10 源文件的中大型需求——产品→架构→工程→QA 五席逐步派单，每步带质量关卡 | `references/standard-sop.md` |
| 📋 部分工作流 | 只需要链条中的一段（仅 PRD／架构评审／代码实现／仅测试／市场调研等六子模式）——按需单派席位，不跑全链 | `references/partial-workflows.md` |
| 增量开发 | 已有项目上的变更需求（新功能或修复）——四席各自基于旧产物做增量：增量 PRD→增量设计+任务列表→最小变更实现→全量回归+新测试 | `references/incremental-dev.md` |

任何档位推进中都受协作规则卷（顺序流转/信息传递/反馈回路/语言一致性/结构化输出）约束，收尾受交付总结规范约束（TL;DR＋交付概览＋文件清单＋下一步建议）。

## 4. 五席价值主张

| 席位 | 职责一句话 | 对用户的核心价值 |
|---|---|---|
| 主理人（齐活林·交付总监） | 编排者而非执行者：建团队、判档路由、中转所有跨席信息、汇编交付；可临时兼任外部顾问讨论会主持人 | 用户只面对一个入口，换来的是"谁接、什么顺序、每步怎么验收"的持续在线统筹 |
| 产品经理（许清楚） | 把模糊需求写成可施工的 PRD（简单 PRD 默认／完整 PRD 含竞品象限分析），或以研究模式出市场调研报告 | 需求先被界定再被实现——目标、用户故事、P0/P1/P2 需求池、待澄清项一目了然 |
| 架构师（高见远） | 基于 PRD 一次性输出系统设计（方案选型/文件列表/类图/时序图）＋按依赖排序的任务分解（≤5 任务硬上限、首任务必为项目基础设施） | 设计与排期一次成型：工程拿到的是可直接执行的任务列表，不是需要二次翻译的蓝图 |
| 工程师（寇豆码） | 按设计批量实现全部代码（一次性写完、禁止占位符/TODO），完工前做全局跨文件一致性自查（IS_PASS 判定）；交付面唯一有写权限的席位 | 交付是完整可用的代码而非骨架；改动有回执清单可逐项对账 |
| QA 工程师（严过关） | 编写并运行测试，每轮做智能路由判定（源码 Bug 回工程/测试 Bug 自修/全过收工），测试最多 2 轮、遗留问题如实入报告；对回执清单逐件核对交付面纯净性 | 质量结论出自独立判定方：不自己生产所以不给自己放行，2 轮上限换交付节奏、遗留问题不藏 |

## 5. 质量与可审计承诺

产品视角的四组承诺（条款细则以 `references/dev-discipline.md`、`references/handoff-discipline.md` 两卷为准）：

- **每步留证据**：SOP 每一步产出带验收判据与判定级别；关键输出要求结构化（表格/Mermaid/JSON），交接件按六字段骨架自包含成文——接手人只拿该件即可行动。
- **判定分级、禁糊账**：工程完工有 IS_PASS 二值判定；QA 每轮有路由判定；收口声明前须跑收口自检五件套（判据清单/逐条证据/三态计数/未绿项/移出项），任一缺项只能报"部分完成"；验收读数按三分账分列，不出"基本通过"式结论。
- **独立核验（fresh eyes）**：交付面纯净性由 QA 席逐件核验，生产方不兼判定方——工程师自证不算绿，QA 漏检才算 QA 未绿项；核验者以空会话接手人视角对终态复核，不沿用生产方的过程假设。
- **写权闭集与拒写权**：交付面（`.collab/` 过程域以外的一切产物）只有工程师席有写权限；其余席位产出＝过程件只落过程域，受命向交付面写入时有权且应当拒绝并报主理人改派。工程师写入集＝票面声明的文件闭集，完工回执逐项列出写入清单并与版本库实写面全等对账。

## 6. 非目标与边界

- **不做单代理全能模拟**：主理人严禁跳过正式团队流程、严禁代写任何成员席的专业产出；所有跨席信息流经主理人中转，席位间不得直连。
- **不自行动外部系统**：装配／注册／覆盖插件缓存三类动作一律属部署任务——须独立部署票＋用户明确批准，且走「装配→预览→人类闸→部署」四段闸口链，禁止跳段、禁止人类闸由代理代跑（`references/deploy-gate.md`）。开发收口不自动附带部署。
- **不设研究席**：调研是各席通用技能而非编制，取证按问题适配席位派执行（`references/dev-discipline.md` §一）。
- **装配组件闭集外不属本团**：本包装配的外部技能组件锁版本闭集目前为两件——`external-advisor-collab`（讨论会程序真源）与 `deep-research`（证据型调研技能），均锁不可变 tag（见 `bundle.lock` components）；其他外部协作类技能包（如通用多席协作盘件）不属本包范围。
- **不越内容本体判断**：本包交付的是过程质量保障（拆解、设计、实现、质检、审计判定），不对业务内容本体作最终裁决；市场研究产出为带来源的分析建议，决策权保留给用户。

## 7. 交付形态

本包的产品形态＝一条"真源→装配→部署"链条加一条版本账纪律：

- **包面真源**：仓内 `workbuddy/baigong-software-team/` 目录是席位定义与流程域的唯一真源；改席位定义只改真源。
- **装配面派生**：`bundle.lock` 声明组件与版本锁，装配器把包本体＋锁定的外部组件拼成注册态 bundle；装配产物不入任何版本库，缺省输出为与源仓同级的 `<仓名>-build/<bundle名>` 预览面——派生产物，非第二真源。
- **部署四段闸**：装配→预览→人类闸→部署，段段须上游收口；预览态抓手＝本地市场注册挂预览卡，人类真实验证明示通过后部署面才转正（`skills/software-orchestration/references/deploy-gate.md` §五）。
- **版本账纪律**：包版本号在 `.codebuddy-plugin/plugin.json` 与 `bundle.lock` 同源镜像、每变必 bump；组件一律锁不可变 tag；历次变更逐版记账于 `README.md`「出身」节版本账——版本号同时是宿主刷新运行缓存的载体。

---

## 取证（誊入交付包时删除本节；正文自包含）

路径基准＝仓根。包＝`workbuddy/baigong-software-team/`（下省略此前缀）。

- 现行版本 0.1.10：`bundle.lock:5`、`.codebuddy-plugin/plugin.json:3`。
- 出身基线 software-company v1.1.0：`README.md:24`；Team 型：`README.md:7`、`.codebuddy-plugin/plugin.json:22`（`"expertType": "team"`）。
- 五席位：`agents/` 目录 listing（5 件 MD）；`.codebuddy-plugin/plugin.json:10-14`（agents 数组 5 行）。
- 路由档位：`agents/software-company-team-lead.md:49-54`（四档判定表）＋`:79`（增量开发⛓ 必读行）；五档各卷＝`skills/software-orchestration/references/quick-mode.md:5-7`、`bugfix-path.md:9-10`、`standard-sop.md:7-8`、`partial-workflows.md:9-14`、`incremental-dev.md:7-12`。
- references 卷数实测＝10 卷（非任务书所称十一卷）：`skills/software-orchestration/references/` listing（10 个 .md）＋`skills/software-orchestration/SKILL.md:14-25`（索引表 10 行）；SKILL.md 版本 1.1.0＝`SKILL.md:5`。
- 装配组件两件与锁 tag：`bundle.lock:15`（`external-advisor-collab@v1.1.1`）、`bundle.lock:25`（`deep-research@v1.0.2`）；组件行闭集＝`bundle.lock:10-30`（仅两元素）。
- 每变必 bump／同源镜像纪律：`bundle.lock:8`（bundle note 纪律①④）、`bundle.lock:33-38`（conventions）。
- 质量关卡：IS_PASS 判定＝`agents/software-company-team-lead.md:89`、`agents/software-engineer.md:78-92`；QA 智能路由与 2 轮上限＝`agents/software-qa-engineer.md:53-69`、`:71-88`；QA 回执核对行＝`agents/software-qa-engineer.md:145`。
- 收口五件套：`skills/software-orchestration/references/handoff-discipline.md:30-32`；交接件骨架与自包含判据＝同卷 `:15-19`。
- 写权闭集与拒写权：`references/dev-discipline.md:6-15`（§一；拒写权 `:14`）；不新设研究席＝`:16`（§一.5）；生产方不兼判定方＝`:48`（§四.2）；回执与 commit 全等对账＝`:40-42`（§三）。
- 席位写权声明（五席各一节）：`agents/software-company-team-lead.md:109-112`、`software-product-manager.md:95-97`、`software-architect.md:144-146`、`software-engineer.md:152-154`、`software-qa-engineer.md:139-141`。
- 部署硬门与四段闸：`references/deploy-gate.md:7-13`（闭集三动作）、`:15-18`（两前置）、`:32-36`（四段链）。
- 讨论会兼任：`agents/software-company-team-lead.md:63-66`。
- 使用示例/quickPrompts：`README.md:17-18`、`.codebuddy-plugin/plugin.json:58-71`。
- 团队协作铁律（不代写/不直连/不跳段）：`agents/software-company-team-lead.md:22-35`。
- 头像 6 件：`avatars/` listing（team＋五席位 PNG 共 6 件）。
- 维护规则（真源只改仓内、部署面只准复制生成）：`README.md:79`。
