# Skill 对象审计（技能/规范/技法库）

> **本件只持审计判据（问句式）。构建规范在 `object-build/references/10-skill.md`，此处只留指针。**
>
> 出处：干净度五测＝本地约定；契约闭环＝`skill-contract-audit` 收敛（以其真源为准）；description 触发＝业界范式（Agent Skills 开放标准 spec：`description`「Should describe both what the skill does and when to use it」）；**四型＝实践者一手**（obra/superpowers 的 meta-skill `writing-skills`：Discipline-Enforcing／Technique／Pattern／Reference）；**边界四道＝官方一手**（agentskills.io spec＋Claude Code 团队博客＋官方帮助中心）。**Diátaxis／ISO 只作类比**——Diátaxis 原话是类型混装「at the heart of a vast number of problems in documentation」（**不是**"最常见的失败模式"），从未推广到非文档对象；ISO 9001:2015 不规定文件层级，四层金字塔源出 ISO/TR 10013:2001 附录 A 的**资料性**示例，ISO 10013:2021 已不再规定。

## S0 前置：先判型（判错型＝后面全部测项打偏）

**为什么要判型**：官方原话——"The best skills fit cleanly into one; the ones that try to do too much straddle several and confuse the agent."（Claude Code 团队博客·内部 skill 编目后的观察）。这句话**同时是分类标准和反粒度警告**：判不出主类型，就说明它已经在 straddle。

| 型 | 是什么 | 一句话判据 | 一手定义（superpowers `writing-skills`） |
|---|---|---|---|
| **D 纪律强制型** | 一条不许越的线，违反要被咬住 | **删掉步骤它仍是完整纪律；一加步骤就变成了别的型** | Discipline-Enforcing |
| **T 技术步骤型** | 一个带顺序的做法 | **有明确的「做完了」，输入→产物可对账** | Technique：concrete method with steps to follow |
| **M 思维模式型** | 一类判断的框法，无固定顺序 | **换对象仍用同一套判据；没有「一次做完」** | Pattern：way of thinking about problems |
| **F 参考查表型** | 只有「是什么」 | **删掉所有祈使句，内容仍完整** | Reference：API docs, syntax guides, tool documentation |

**一处必须承认的业界空缺**：官方九类与 superpowers 四型里**都没有「角色定义／岗位说明」这一类**。"某个角色该干什么"在业界不是 skill 的型，而是**纪律（D）或思维模式（M）的内容**。若被审件自称"角色型 skill"，按 D 型审；把它单列一型是我们的发明，不是业界范式。

## S0-b 字段齐备（判型之后立刻查·否则后面全空转）

**审**：该型的必填字段是否逐项落实？

判据清单在 `object-build/references/10-skill.md` 第 1 步（本器不复写——复写＝第二真源）。核法：打开构建侧清单，逐项在该件里找落点，**指不出行号即缺**。

**审**：是否混装（一件出现两个主类型）？

拆法在 `object-build/references/10-skill.md` 第 3 步。本器只判结论：**找到第二个主类型的完整证据链（该型的必填项自成一组）＝混装**，判关注（可延后至下版拆）；若混装已导致必填项互相挤占（如纪律件里长出步骤表）＝阻断。

**型别漂移的识别信号（本器自己的 grep 判据）**：D 件出现「第一步／然后／流程」＝在往 T 漂；T 件出现「一般来说／视情况」＝在往 M 漂；M 件出现具体产物路径＝在往 T 漂。

**类型决定审计轴（本器最大的一个省事）**：**D 型 skill 直接走专家角色那套测项**（`20-expert-role.md` 的 E 系列）——D 型要的「边界三栏／权限／升级路径／负样本」与专家角色审计是同一组要求，不必两套都跑。T 型加查入口/出口/产出件，M 型加查判据可测性，F 型只查出处与时效。S1–S11 是四型共用的底座。

**判型之后还有第二根正交轴**：**期**（编译期固化 vs 运行时挂载）。型别管"内容是什么形态"，期别管"何时确定"——同一个 T 型 skill 可以写死在节点契约里（编译期），也可以按输入检索注入（运行时）。**判据与出处见 `15-binding.md`；不先定期，就会用编译期的尺子（干净度/穷尽性/机检）去审运行时对象（案例库/经验库），那是用错尺子。**

## S1–S5 干净度五测（同总则 T1–T5·此处给 Skill 专用判法）

| # | 测项 | Skill 专用判法 |
|---|---|---|
| S1 | 项目实体 | 扫：项目名／各类号段（纪律号·台账号·判词号·票号）／日期／人名／项目路径（临时目录名·盘符路径）。**豁免（裁-21）：协议强制日期不算实体**——`spec-provenance` 块 `spec_effective` 行、changelog 文件（文件名含 `changelog`）全部日期、全角括注内的版本/决策注日期（如「（2026-10-22·决策者拍）」「v3.0（2026-10-23）」「（2026-10-22 建）」）；**正文裸叙述日期仍算**（裸写于句中、不在全角括注内者）。**改名/沿革史实句豁免（裁-23）**：史实锚句中的项目名不算实体——句式如「改名（YYYY-MM-DD…）」「由 X 改名」「旧名作废」；史实锚不删不改写，正文裸项目名（非史实句式）仍算。**账本日期豁免（裁-25）**：`COPY.state`（文件名精确匹配）全部日期豁免——账本＝机器生成同步流水，与 changelog 同性质（协议强制时间戳）；路径不豁免（`copy:` 键记 `${SKILLS_ROOT}/` 变量式消灭实体） |
| S2 | 触发描述 | description 只写「什么时候用」不写「给哪个项目用」；when 条件＋触发词齐；换个项目读仍成立 |
| S3 | 出处 | 每条规则三档标注：业界出处（URL/标准号）／命名范式（ADR·Diátaxis·SSOT·INVEST）／本地约定（显式写「本地约定」而不是默认成共识） |
| S4 | 真源方向 | 方法论真源在 skill 层；项目值（真源文件·机检清单·临时目录）由项目 profile 注入，且 profile 必须真实存在（禁悬空引用） |
| S5 | 体量披露 | 主文件＜200 行（**严于官方 500 行的本地约定**：主文件常驻的是已激活会话的每一轮）；细则进 references/；references 按对象或阶段分件，主文件只留路由与骨架 |

## S6–S9 契约闭环（能力能不能落地）

| # | 测项 | 判法 |
|---|---|---|
| S6 | 主张—产物对 | 每条声明的能力能指到一个产物：脚本／命令／检查器／判据 |
| S7 | 悬空指针 | 引用的文件/工具/字段真实存在（含「由项目 profile 注入」的 profile 本身） |
| S8 | 负样本 | 抽 1–2 条约束故意违反，防线必须咬（不咬＝防线不存在） |
| S9 | 能力边界诚实 | 不声称别的 skill 负责的事；跨 skill 只写指针（「票制见 X」「身份见 Y」），不代写细则 |

## S10–S11 结构与加载

| # | 测项 | 判法 |
|---|---|---|
| S10 | 渐进披露 | 主文件给骨架与路由；长清单进 references/；无 references 而主文件超 200 行＝不合格 |
| S11 | 触发覆盖 | description 含主要同义词与场景词（用户不会按你的术语提问）；缺触发词＝该用法永远不加载 |

## 判定要点

- **S0 判不出主类型＝阻断**：型别不明就没法选尺子；硬审下去往往逼出「给纪律件补步骤」「给步骤件补判据」这类假件。
- **S0-b 字段缺必填项＝阻断**：该型不合格（不是"待完善"，是这一型还没成立）。
- 四问里「问净」不合格是**阻断**级：脏 skill 会污染所有使用它的会话。
- 「问实」不合格为**阻断**：「声明的能力落不了地」比没有更坏——它会把假能力当既有能力规划。
- 「问测」「问界」不合格可判**关注**，须带核验动作。

## 来源清单（2026-10-22 四研究席并行取证·全部实抓核到）

| 来源 | 等级 | 用于本件哪一条 |
|---|---|---|
| https://agentskills.io/specification | A 开放标准 | 体量边界、description 规范 |
| https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills/ | A Claude Code 团队 | "fit cleanly into one"、九类、description＝触发描述、常驻上下文 |
| https://code.claude.com/docs/en/skills | A 官方文档 | reference/task 两类内容、成本边界 |
| https://support.claude.com/en/articles/12512198-creating-custom-skills | A 官方帮助中心 | 职责边界（separate skills compose better） |
| https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md | B 实践者一手 | **四型（D/T/M/F）＋按型分别测** |
| https://diataxis.fr/start-here/ 与 /map/ | A 作者一手 | 类型混装论断（原话 at the heart of a vast number of problems in documentation） |
| https://docs.divio.com/documentation-system/ | A 作者一手 | 同上原帖版 |

**取证时明确打不开、未据记忆补的**：platform.claude.com（区域拦截）；en.wikipedia.org 全系（本环境不可达，凡涉 Wikipedia 处均以二手转引并降级）；ISO 9001/9000 标准正文（付费墙，仅以 TÜV IRCA 教材与 WMO 指南佐证）。
