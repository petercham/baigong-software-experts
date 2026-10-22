# R1 · skill 切分的官方事实（对象轴 vs 阶段轴）

调查日 2026-10-22。只列可回链出处；打不开的原页登记在末节，不用记忆补。

## 结论（条件式）

**官方从未把"对象类型"当作拆分依据。** 唯一的拆分判据是**上下文共现关系**：互斥/很少一起用 → 分开；否则合并为"一个入口 + 按域分件"。

对 12 格的含义：

- **(b)/(c) 有直接官方范式**：Pattern 2「多域一 skill，按域分 reference」＋ `theme-factory`（10 个同类对象→1 skill+10 分件）＋ `skill-creator`（造+评+改+量测在 1 skill，审计角色落到 `agents/grader.md`）。
- **(a) 不被禁止，但撞"太窄"判据**：官方点名 Too narrow 为病。只有 6 个对象的知识**互斥**时才符合官方判据。
- **阶段轴（造/审）官方仓库基本没拆**：四处官方实例都是造+验同居。要把 2 阶段做成 2 个顶层 skill，官方**无先例**，社区仅 1 例。

一句话：**按"上下文互斥度"分顶层 skill，不按对象分；对象和阶段都下沉为 references 分件。** 12 格直接铺成 12 个 skill 是最缺依据的做法。

---

## 证据

**E1 [A] 唯一可操作的分拆判据是共现度，不是对象身份**
> "**Structure for scale:** When the `SKILL.md` file becomes unwieldy, split its content into separate files and reference them. **If certain contexts are mutually exclusive or rarely used together, keeping the paths separate will reduce the token usage.**"
— Anthropic Engineering《Equipping agents for the real world with Agent Skills》
https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

**E2 [A] 顶层按 workflow 拆；并明确多专注 skill 优于大 skill**

> "**Keep it focused:** Create separate skills for different workflows. **Multiple focused skills compose better than one large skill.**"
> "**Skills can build on each other:** While skills can't explicitly reference other skills, Claude can use multiple skills together automatically. This composability is one of the most powerful parts of the skills feature."
— Claude Help Center《How to create custom skills》 https://support.claude.com/en/articles/12512198-how-to-create-custom-skills （已直连抓正文核验）
注：这是最接近"何时拆两个 skill"的官方回答——拆的单位是 **workflow**。且 compose 发生在**顶层 skill 之间**；合进 1 个 skill 后跨格组合退化为分件引用，不再享有此待遇。

**E3 [A-] 官方明文范式：一个 skill 含多域 → 按域分 reference**
> "#### Pattern 2: Domain-specific organization
> For Skills with multiple domains, organize content by domain to avoid loading irrelevant context. When a user asks about sales metrics, the agent only needs to read sales-related schemas, not finance or marketing data. This keeps token usage low and context focused."
> `bigquery-skill/ ├── SKILL.md (overview and navigation) └── reference/{finance,sales,product,marketing}.md`
— Anthropic《Skill authoring best practices》→「Skill structure → Progressive disclosure patterns → Pattern 2」
等级：**内容 A、载体 B**。`platform.claude.com` 原页 SSL 直达失败（见末节），我取 `obra/superpowers` 仓库内的逐字副本 `skills/writing-skills/references/anthropic-best-practices.md`（1151 行，保留指向 `platform.claude.com/.../agent-skills/overview` 的链接与 `mintcdn.com/.../agent-skills-*.png` 官方图床地址，可判为官方 MDX 导出件）。https://github.com/obra/superpowers/blob/main/skills/writing-skills/references/anthropic-best-practices.md

**这是本题最直接的范式：把 6 个对象填进 `reference/` 是官方示范动作；升格成 6 个顶层 skill 无对应示范。**
**E4 [A] 规范对"范围"无规定，只规定尺寸与命名绑定；但对成本有三级规格值**
- 「Keep your main `SKILL.md` under 500 lines.」「Keep individual [reference files] focused.」「There are no format restrictions.」（正文）
- **分件链深上限（反向约束，易被忽略）**：「Keep file references **one level deep** from `SKILL.md`. **Avoid deeply nested reference chains.**」→ 官方允许"多分件"，但**禁止套娃**。"对象下沉为分件"必须落成**一层平铺**，不能是 `入口 → 对象目录 → 阶段文件` 的两层。
- **三级成本口径**（spec「Progressive disclosure」，本人直连核验）：Metadata「~100 tokens」启动时对**所有**已装 skill 常驻／Instructions「< 5000 tokens recommended」触发时整体加载／Resources「loaded only when required」。→ 官方等于给出了单个 skill 正文的**容差带 5k**：这是"合太粗"的官方上界，与 `SKILL.md<500 行` 互为表里。
- `name`「Must match the parent directory name」。常驻代价另有一句官方定性（`code.claude.com/docs/en/skills`「Find unused skills」，直连核验）：「Every skill in the skill listing adds to your context on every turn, whether or not Claude ever uses it.」
— https://agentskills.io/specification
成本实测（B，见 R4）：124 skill ≈13,800 tokens/轮（≈111/个）、40 skill ≈3,060/轮 → 12 个顶层 skill ≈1.3k tokens 常驻。且 SkillRouter（arXiv 2603.22455，8 万 skill 尺度）实测：藏起 body 只给 name+description，最强管线 Hit@1 由 68.0%→24.0%——**拆得越细越依赖 description 独立可辨识，而它恰恰最不耐压缩**（作者自述 not a universal law，5–30 skill 场景未测）。

**E5 [A] Claude Code 文档同样没有"范围"条款，拆分维度是"调用方式"**
已逐词检索：**不存在** "coherent unit" / "one skill per" / "single responsibility" / "compose"，也**无**"何时拆"章节。最接近的是三个 frontmatter 开关：
> "`disable-model-invocation: true` … Use this for **workflows with side effects** or that you want to control timing, like `/commit`, `/deploy`…"
> "`user-invocable: false` … Use this for **background knowledge** that isn't actionable as a command."
— https://code.claude.com/docs/en/skills ｜即官方切分维＝「知识型 vs 操作型／有无副作用／是否需隔离」，**对象类型不在其中**。

**E6 [A] 命名规范是活动名，不是对象名**
> "We recommend using **gerund form** (verb + -ing) for Skill names, **as this clearly describes the activity or capability** the Skill provides."
— 同 E3（「Naming conventions」）。顶层 skill 的语义单位被官方定义为 **activity**，轻偏阶段轴（活动）而非对象轴（名词）。

**E7 [A] 官方仓库 anthropics/skills：19 个 skill，内部是"入口+分件"**
顶层 19 个：`academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx`
https://github.com/anthropics/skills/tree/main/skills

| skill | 结构 | 意义 |
|---|---|---|
| `theme-factory` | `SKILL.md`＋`themes/*.md`（10 个主题）＋1 个 showcase pdf | **A 级"多同类对象合并进 1 skill"实例**：10 个对象各自不成 skill，因选择发生在同一流程（showcase→选一个→应用） |
| `mcp-builder` | `SKILL.md`＋`reference/{node,python}_mcp_server.md`＋`reference/evaluation.md` | **变体分件、阶段不切**：造（两平台）与评（evaluation）同居 |
| `skill-creator` | `SKILL.md`＋`agents/{analyzer,comparator,grader}.md`＋`references/schemas.md`＋8 脚本 | **造+审同居 1 skill**，审计角色下沉为 `agents/grader.md`——正是 (c) 的"阶段合并、角色分件" |

`skill-creator` description 自述范围，可证"一个 skill 可以很宽"：
> "Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, **run evals to test a skill, benchmark skill performance with variance analysis**, or optimize a skill's description…"
`docx/pdf/pptx/xlsx` 是 4 对象→4 skill，像支持 (a)；但其成立靠 E1 判据（做 xlsx 完全不需要 pptx 的模板与脚本＝**互斥**），且体量极大（`skills/` 下 439 个文件中这四个占多数）。是"互斥→拆"，非"异类→拆"。

**E8 [B] superpowers（15 skill）：按活动切；造+验合并；同一对象按站位拆**
`brainstorming, diagnosing-superpowers, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills` https://github.com/obra/superpowers/tree/main/skills
- `writing-skills` description：「Use when **creating** new skills, **editing** existing skills, or **verifying** skills work before deployment」→ 造+改+验一个对象合成一个 skill。
- `requesting-code-review`（作者侧派 reviewer）／`receiving-code-review`（收侧处置反馈）＝**同一对象按站位拆**。这才是该库拆分的真实理由。

**E9 [B] wshobson/agents（92 plugin，每 plugin 1–16 skill）：反向的极细粒度**
`plugins/python-development/skills` = 16 个（`python-async-patterns / python-anti-patterns / python-testing-patterns / python-type-safety / uv-package-manager …`）；`plugins/api-scaffolding/skills` = 1 个。https://github.com/wshobson/agents/tree/main/plugins
方向与 (b) 相反，但切的维度是**子话题**（async/testing/type-safety），仍不是"对象 × 阶段"；两种形态都跑得通。

**E10 [B] ratacat/claude-skills（97 skill）：唯一找到的"造/审分家"实例**
`agent-native-architecture`（"Build applications where agents are first-class citizens…"）／`agent-native-audit`（"Run comprehensive architecture review with **scored principles**"）／`agent-native-reviewer`（供子代理的评审角色）；另有 `heal-skill`（修 SKILL.md）与 `creating-agent-skills`、`create-agent-skill` 并存。https://github.com/ratacat/claude-skills/tree/main/skills
它拆的仍是三种不同 workflow（设计／打分审计／代码评审），与 E2 相容。

**E11 [C+] 官方博客的"太宽/太窄"双向判据**
> "Aim for **single-purpose skills**. 'SEO optimization for blog posts' is focused enough for specific instructions while broad enough for reusability. **Too broad: 'Content marketing helper.' Too narrow: 'Add meta descriptions.'**"
— Claude 官方博客《How to create Skills: Key steps, limitations, and examples》 https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples
降为 C+：`claude.com` SSL 直连失败（curl error 35，WebFetch 亦失败）；该段经**两次独立检索**返回完全一致原文，另有中文二手转述整理为三列表（太宽 `content-marketing-helper`／太窄 `add-meta-descriptions`／合适 `seo-optimization-for-blog-posts`，https://www.iceyao.com.cn/2026/05/07/claude-skills-creation-guide ）。**未开原页故不算 A，但方向与 E2 一致。** 对本题：**"一种对象 × 一个阶段"（12 格最细格）极可能落在 "Too narrow" 侧**——官方举的"太窄"反例正是"一个动作＋一个对象特性"的粒度。

## 反例（不符合上列结论的真实案例）

1. **顶层确有"一对象一 skill"官方实例**：`docx/pdf/pptx/xlsx`（E7）。故 (a) 不是错，只是**成立条件**＝上下文互斥＋单格体量已超 500 行。
2. **确存在"造/审分家"实例**：ratacat `agent-native-architecture/-audit/-reviewer`（E10）。但它与 E2 相容；若据此说"官方不许阶段合并"就错了——官方**自己在合并**（skill-creator 含 evals/grader）。
3. **确存在"细粒度优于分件"大库**：wshobson `python-development` 16 skill（E9）。故 (b) 非唯一正确形态。另：**未找到**任何官方材料称"面向不同对象应拆成不同 skill"，也无任何材料把"对象类型"列为拆分理由（此为负空间证据，非漏查）。

## 查不到的清单

| 目标 | 结果 |
|---|---|
| `platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices` 原页 | **打不开**。`docs.claude.com` 301 至 `platform.claude.com`，随后 curl SSL error 35、WebFetch fetch failed。改用 E3 仓库内逐字副本 |
| `claude.com/blog/how-to-create-skills-...` 原页 | **打不开**（SSL error 35；r.jina.ai 代理同样失败）。仅得检索逐字摘要（E11，C+） |
| agentskills.io 有 "coherent unit"/"one skill per"/"multiple skills compose"；docs/claude-code 有"何时拆两 skill"专章 | **均不存在**，已逐词检索整页；code 侧仅有三个调用方式开关（E5） |
| 官方"每 skill token"口径 | **有规格值**（~100 / <5k / 0，E4，本人直连 agentskills.io 核验）；`platform.claude.com/.../overview` 同表「~100 tokens per Skill / Under 5k tokens / None until accessed」我**打不开**，由 R4 经检索取得，两处数字一致。缺口是**实测分布**：无分位数、无最坏值、"~"的离散度未知 |
| 官方"skill 数量上限／触发面竞争"的定量说法 | **未找到**。另有一句官方定性「install many Skills without context penalty」（仅见于未直连的 overview 页，由 R4 转述），与 E4 常驻代价句并不矛盾（前者讲"轻"，后者讲"每人每轮都占"），但我不把它当 A 级引用。社区说法「Every one you install adds invocation triggers…」（C，未采信） |
| 社区流传启发式「If you're writing 'and also' in your description, you need two skills」 | **无法溯源**：出现在 `claudeskills.info` 镜像页，但原仓库 `ratacat/claude-skills` 的 `create-agent-skill`/`creating-agent-skills` 与 `obra/superpowers` 的 `writing-skills` 均检索不到。**判为镜像改写，不引用** |

## 对本题的适用边界

**官方事实能覆盖到的**：
1. 顶层拆分判据＝上下文互斥/共现＋复用价值（E1/E2/E11），**不是对象类型**。
2. "一 skill 装多域、域落 `reference/*.md`"是官方明文范式（E3），有 `theme-factory`（10 同类对象→1 skill）实物（E7）。
3. "造+评同居一 skill"是官方自己在做的形态（`skill-creator`、`mcp-builder`）（E7）。
4. skill 名应是活动名（E6）；metadata ≈100 tokens/skill 常驻（E4）。

**覆盖不到、仍须本项目自决的**：
1. **"6 种对象的知识是否互斥"是领域判断，不是文档问题。** 若"造节点"与"造 skill"共享同一套骨架/判据语言（本项目 v2 似共享），按 E1 **不该**拆成 6 个顶层 skill；若判据/模板/检查项几乎零交集，则**该**拆。官方给了尺子，没给读数。
2. **12 格落成 2 个顶层 skill 还是 1 个入口**，无先例可对号：官方最大合并案例是 `theme-factory`（10 同类、单一选择流程）与 `skill-creator`（4 类活动、同一迭代循环）；12 格是否同属"一个循环"，是设计判断。**但 E4 的"一层平铺"是硬约束**：`入口→对象目录→阶段文件` 的两层嵌套违规，可行形只有 (b) 1 入口×12 平铺分件，或 (c) 2 入口×各 6 平铺分件。
3. **"审计"是否天然该独立成 skill**：只能援引"知识型 vs 操作型／有无副作用"（E5）。审计无副作用、宜被模型自触发反复自查 → 更像 `user-invocable: false` 的知识型，**这支持并入而非另立 skill**；但这是从开关语义外推，非原文直述。
4. **12 个 description 的触发面竞争，官方零定量指引**。任何"12 个 skill 会误触发"的论断目前只有 C 级社区说法，不能当事实。
