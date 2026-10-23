# Skill 构建（D/T/M/F 四型）

> **状态**：草稿 v0.1（从 `object-audit/references/10-skill.md` 拆出的构建规范·待审计器交叉验证）。
> **出处**：四型＝**实践者一手**（obra/superpowers 的 meta-skill `writing-skills`：Discipline-Enforcing／Technique／Pattern／Reference，并规定**按型分别测**）；边界四道＝**官方一手**（agentskills.io spec ＋ Claude Code 团队博客 ＋ 官方帮助中心）。
> **关于 Diátaxis／ISO：只作类比，不是其原生适用范围**——Diátaxis 作者原话是类型混装「at the heart of a vast number of problems in documentation」（**不是**"最常见的失败模式"），且从未把框架推广到非文档对象；ISO 9001:2015 本身不规定文件层级，四层金字塔源出 ISO/TR 10013:2001 附录 A 的**资料性**示例，ISO 10013:2021 已不再规定任何层级。

## 第 0 步：定类型（定不出＝先别写）

官方原话："The best skills fit cleanly into one; the ones that try to do too much straddle several and confuse the agent."（Claude Code 团队博客·内部 skill 编目后的观察）——**这句话同时是分类标准和反粒度警告**：判不出主类型，说明它已经在 straddle。

| 型 | 是什么 | 一句话判据 | 一手定义（superpowers `writing-skills`） |
|---|---|---|---|
| **D 纪律强制型** | 一条不许越的线，违反要被咬住 | **删掉步骤它仍是完整纪律；一加步骤就变成了别的型** | Discipline-Enforcing |
| **T 技术步骤型** | 一个带顺序的做法 | **有明确的「做完了」，输入→产物可对账** | Technique：concrete method with steps to follow |
| **M 思维模式型** | 一类判断的框法，无固定顺序 | **换对象仍用同一套判据；没有「一次做完」** | Pattern：way of thinking about problems |
| **F 参考查表型** | 只有「是什么」 | **删掉所有祈使句，内容仍完整** | Reference：API docs, syntax guides, tool documentation |

**一处必须承认的业界空缺**：官方九类（Library and API reference … Infrastructure operations）与 superpowers 四型里**都没有「角色定义／岗位说明」这一类**。"某个角色该干什么"在业界不是 skill 的型，而是**纪律（D）或思维模式（M）的内容**。所以要造角色 → 走 D 型，见 `20-expert-role.md`；**不要新立第五型**（单列"角色型"是我们的发明，不是业界范式）。

## 第 1 步：按型填字段（缺一即写不完）

| 型 | 必填 | 不该有（出现了就是混装） |
|---|---|---|
| D | 红线句／**违反的负样本**／被咬的机制（机检或人工）／升级路径 | 步骤编号、单一对象的专属判据 |
| T | 入口条件／步骤（含**停手条件**）／出口判据／产出件 | 无负样本的"应该"、角色利益论述 |
| M | 判据集／每判据的「判法」／反模式／判定分级 | 固定步骤编号、具体产物路径 |
| F | 每条目＋出处＋版本或生效日 | 祈使句、职责、流程 |

## 第 2 步：按型自测（型别不是标签，是测试用例的分组依据）

superpowers 值得整段抄的一条：**按型分别规定测法**——

| 型 | 测法（写完就跑一遍） |
|---|---|
| D | 造一个**违反**，看有没有被咬住。不咬＝防线不存在 |
| T | 照着跑一遍，看能不能到出口、产出件是否对得上 |
| M | 换一个对象，看这套判据还成不成立 |
| F | 抽 3 条，对一遍现行真源（版本/日期） |

## 第 3 步：查混装（一件只有一个主类型）

其余内容进 `references/` 并按各自类型标注。

- **D＋T 混（最常见）**：纪律里塞做法 → 做法抽成 T 件，D 只留红线＋负样本。**D 型超重的典型症状＝行数膨胀＋出现「第一步／然后／流程」。**
- **T＋M 混**：步骤与判断框绑在一起 → 拆两件（方法可复用，流程绑一次交付）。
- **M＋F 混＝合法**：判据集自带查表（出处／词表），分栏标注即可。
- **D＋F 混＝合法**：纪律带自己的词表与权限表。

**型别漂移信号（自查用 grep）**：D 件出现「第一步／然后／流程」＝在往 T 漂；T 件出现「一般来说／视情况」＝在往 M 漂；M 件出现具体产物路径＝在往 T 漂。发现漂移先判「它主要产出的是**约束**还是**方法**」，再决定拆还是留。

## 第 4 步：定边界四道尺（官方一手·与型别正交，四型共用）

| 尺 | 要求 | 出处 |
|---|---|---|
| **触发边界** | description 写「**何时用**」，不写「是什么」。官方原话："the description field is not a summary, it's a description of when to trigger this skill" | Claude Code 团队博客 |
| **职责边界** | 一个 skill 一个 workflow；"Multiple focused skills compose better than one large skill" | 官方帮助中心 |
| **体量边界** | ① 正文**官方建议上界 "< 5,000 tokens recommended"**（agentskills.io spec 直连核到；**是 recommended，不是硬上限——写成"官方硬上限"会被打回**）。**注意：`skill-creator` 同一约束写的是 "<5k words"——words≠tokens，两个量纲，不要混引**（5k words≈6.5k tokens）② 官方另给 **＜500 行**（启发式，无实验）③ **description＋when_to_use 在 listing 中截断于 1,536 字符**（这是**描述层**硬上限，不是正文）④ 细则进 references/，引用保持一层深（"Avoid deeply nested reference chains"）⑤ 本地更严：主文件 ＜200 行 | ①②③ 官方（agentskills.io spec ／ code.claude.com）；④ 同上 spec；⑤ 本地约定 |
| **成本边界** | 官方三级加载成本：**Level 1 metadata "~100 tokens"（startup 时对全部 skill 加载）／Level 2 instructions "< 5,000 tokens recommended"（触发时）／Level 3 resources "loaded only when required"（不占这 5k）**。→ N 个 skill 每轮固定税 ≈ **N×100**（做预算用 100 官方规格值，做上界论证用实测 111，两者不能混）。**若引官方 "install many Skills without context penalty"，必须与「Every skill … adds to your context on every turn」成对读**：单个便宜，但**线性且无条件**；"without penalty" 是相对于"把全文塞进 CLAUDE.md"，不是零成本 | 官方三级规格值（agentskills.io spec 直连可复核）＋第三方 o200k_base 实测（仅作量级） |
| **「入口少、分件多」的三条限定** | ① **分件不套娃**：官方 "Keep file references **one level deep** from `SKILL.md`. **Avoid deeply nested reference chains**." → 分件只从主文件挂一层，不得再嵌套；"下沉为分件"不等于可以无限递归，**"入口→对象目录→阶段文件"这种树形直接违规** ② **「夹逼」是方向上的双侧，不是强度上的对等**：**5k 侧**＝**规范自己给的数**（recommended），**外推距离近**；**SkillRouter 侧**＝~8 万 skill／75 查询、作者自认 "not a universal law"，**在 10–30 个模块规模上未被测量**，**外推距离远（跨 3 个数量级）**。**Context Rot 不为 "5k" 这个数值背书，只支持"正文不宜变长"这个方向**——拿它给 5k 作证，正是我们在 SkillRouter 那边要避免的错 ③ **reference 侧不是免费，是「按需付费」**：读的时候照样进上下文，Context Rot 对它同样适用。"挪到分件侧"省的是**每轮**的钱，**不是省掉读的钱** | ①②③ 官方 spec；② Context Rot（Chroma）／SkillRouter（标注外推边界） |

**成本边界的直接推论（拆不拆 skill 的最终判据）**

**拆分的成本由「边界是否等于加载边界」决定，不由「拆成几个」决定。**

- **skill 边界 ＝ 每轮付费的加载边界**（~100 tokens/个/轮，无条件、不看用不用）
- **reference 边界 ＝ 按需付费**（不读不花，Level 3 "loaded only when required"）
- 所以判据是「**这个东西需不需要每轮参与选择**」——不是「内容多不多」，也不是「面向哪个对象」。

**官方唯一可操作的分开判据是共现度**："If certain contexts are **mutually exclusive or rarely used together**, keeping the paths separate will reduce the token usage."
（**注意：官方 spec／文档里并没有 "coherent unit of work" 这个说法，流传甚广但查证为零——不要引用。**）

**拆成独立 skill 的正当条件（工程侧实证）**：该对象带**独立运行时/解析器/外部工具**、**独立版本与发版节奏**、**可单独卸载**、或共享昂贵中间产物的代价不可接受。四条一条都不满足时，拆只是把内容从「按需付费」挪到「每轮付费」。

**反例警示（成熟体系的正确落位）**：对象类型之间的差别，业界落点是**触发条件**而不是模块边界——Checkstyle「A visit to a node triggers all Checks configured for **its token**」；buf lint 规则**绝大多数按对象命名**（`ENUM_*`/`FIELD_*`/`MESSAGE_*`…，**有例外**：`PROTOVALIDATE` 不守前缀、`STABLE_PACKAGE_NO_IMPORT_UNSTABLE` 不属于任何类别），但**按严格度组织**（MINIMAL⊂BASIC⊂STANDARD）、交付单包。**按对象命名 ≠ 按对象分模块。**

## 第 5 步：写的时候就别带历史债（否则后面只能删）

| 债型 | 造的时候怎么做 |
|---|---|
| 违反流水（「我们曾错过 X」「某次被纠」的过程记录） | 不写；只留「为什么立这条」一句决策血缘（不带编号） |
| 项目号段引用（纪律号·台账号·判词号） | 不写编号；写规则语义（「署名纪律」而非具体编号），编号留项目侧真源 |
| 项目值（路径、成员名、目录名） | 不写实值；留占位与注入说明（由项目 profile 注入） |

## 第 6 步：升版先减后加

剥离历史债 → 补出处 → **最后**才加新规则。顺序反了＝一边减一边增，棘轮失效（只增不减）。

## 来源清单（2026-10-22 四研究席并行取证·全部实抓核到）

| 来源 | 等级 | 用于 |
|---|---|---|
| https://agentskills.io/specification | A 开放标准 | 体量边界（＜500 行/＜5000 tokens/一层深）、description 规范 |
| https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills/ | A Claude Code 团队 | "fit cleanly into one"、九类、description＝触发描述、常驻上下文 |
| https://code.claude.com/docs/en/skills | A 官方文档 | reference/task 两类内容、user-invocable 与 disable-model-invocation、成本边界 |
| https://support.claude.com/en/articles/12512198-creating-custom-skills | A 官方帮助中心 | 职责边界（separate skills compose better） |
| https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md | B 实践者一手 | **四型（D/T/M/F）＋按型分别测＋字数上限＋description 只写 when** |
| https://diataxis.fr/start-here/ 与 /map/ | A 作者一手 | 类型混装论断（原话 at the heart of a vast number of problems in documentation） |
| https://docs.divio.com/documentation-system/ | A 作者一手 | 同上原帖版 |

**取证时明确打不开、未据记忆补的**：platform.claude.com（区域拦截）；en.wikipedia.org 全系（本环境不可达，凡涉 Wikipedia 处均以二手转引并降级）；ISO 9001/9000 标准正文（付费墙，仅以 TÜV IRCA 教材与 WMO 指南佐证）。

## 交接口（写完交审计器时提供什么）

1. 本件的**主类型**（D/T/M/F 之一，一句话理由）。
2. 该型必填字段的**逐项落点**（在文件第几行）。
3. 该型的**自测结果**（第 2 步那张表跑没跑、结果）。
4. 边界四道尺的**实测值**（行数／tokens／references 层深／description 字数）。
