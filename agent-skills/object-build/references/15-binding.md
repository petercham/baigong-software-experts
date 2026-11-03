# 装订与期别（造之前必须定的第二根轴）

> **状态**：草稿 v0.1（从 `object-audit/references/15-binding.md` 拆出的**设计规范**部分；审计侧的**期别判据**留在审计器）。
> **出处**：思想前身＝知识工程「知识库＋推理机」二分（Feigenbaum 1977【A 学术一手·PDF 已核】）；机制命名＝早期绑定 vs 晚期绑定／静态链接 vs 动态链接（JLS §15.5、Ousterhout CS140【A】）；架构规范＝OCP＋DIP＋依赖注入（Martin 1996【B 一手】）；调度先例＝产生式系统三分＋冲突消解＋TEIRESIAS 元规则【A】；经验层＝Soar 的 episodic memory【A 官方】＋CBR 的 case base（Aamodt & Plaza 1994【A】）＋RAG 的 non-parametric memory（Lewis 2020【A】）；工业成品＝VS Code 的 `contributes.chatAgents`／`chatSkills`【A 官方】。

## 为什么造之前先定期

D/T/M/F 四型分的是**内容形态**；这根轴分的是**何时确定**。两者正交——同一个 T 型 skill 可以写死在节点契约里（编译期），也可以按输入检索注入（运行时）。

Feigenbaum 一句话管期：**"The interesting action arises from the knowledge base, not the inference engine."**——可变性预算花在知识侧，引擎侧求稳定。造的时候把不该变的东西烧进可变层（或反之）是最贵的错，改起来等于重造。

## 三层两态模型（判期的靶子）

| 层 | 是什么 | 期 | 学名 | 我方对象 | 业界对应 |
|---|---|---|---|---|---|
| **角色层** | 拟人专家：使命／边界／权限 | **编译期** | procedural memory（Soar）／productions（ACT-R） | 专家角色 | VS Code `contributes.chatAgents`："pre-configured AI personas with specific instructions and tool restrictions" |
| **岗位层** | 拟岗位节点：入口／出口／契约 | **编译期** | 推理机／contribution point 宿主 | 节点 | LangGraph node："Functions that encode the logic of your agents" |
| **技能层** | D/T/M/F 四型 | **声明在编译期，挂载在运行时** | 依赖注入（DI）／service registry | skill | VS Code `chatSkills`："folders of instructions… that Copilot can load **when relevant**"；MCP `tools/list` |
| **经验层** | 案例库：过去做得怎么样 | **运行时** | **episodic memory**／case base／non-parametric memory | 案例库（待建） | CBR 4R 的 RETRIEVE＋RETAIN；Voyager 的 vector-DB skill library |
| **路由层** | 无命中时怎么办 | **运行时** | 冲突消解（conflict resolution）／元规则（metarule） | 路由决策（待建） | **业界空白，见下** |

**工业成品级证据（最强的一条）**：VS Code 官方已把这套结构做成产品——`contributes` 字段做**静态声明**（contribution points），`activationEvents` 做**运行时激活**，且官方把两类分开命名：chat**Agents**＝"pre-configured AI personas"（编译期角色），chat**Skills**＝"load when relevant to perform specialized tasks"（运行时技能）。**「专家／节点／技能」三个词与 VS Code 官方命名逐一对上。**

**挂载的触发条件（Soar 官方原话）**：

> "Semantic and episodic knowledge usually come into play only when procedural knowledge is **in some way incomplete or inadequate for the current situation**."

即：procedural（角色＋岗位＋技能）**不足时**才检索 episodic（经验）。这正是「某个特定专家在特定岗位上处理特定输入」的精确语义——**挂载不是常态，是能力缺口出现时的补救**。造的时候不要为了"灵活"把常态能力也做成检索态。

**引擎复用、知识替换的 1977 年原型（Feigenbaum，PDF 已核）**：斯坦福把 MYCIN 的规则抽掉、保留其推理机，作为 PUFF 的诊断引擎——**引擎（岗位）原样复用，知识（经验）整体替换**。这是「岗位卡固化、经验运行时挂载」的原始工程实践。

## 装订链（两级装订＋一级运行时注入）

**合并不是文档耦合，是编译期装订。**

```
节点（岗位）──装订──▶ 专家（角色）──装订──▶ 技能（能力）──运行时检索注入──▶ 经验（案例库）
```

| 环节 | 时机 | 业界对应 | 装订后可换吗 |
|---|---|---|---|
| 节点×专家 | **编译期末** | LangGraph `compile()`；constructor injection；VS Code manifest 解析；OSGi install/start 解析 | **不可换**（换＝重新编译） |
| 专家×技能 | **编译期末** | 同上 | 不可换 |
| 技能×经验 | **运行时** | setter/interface injection；CBR RETRIEVE；RAG retriever | **可换**（每次按输入检索） |

**DI 三型给出装订时机的谱系**（Fowler：Constructor Injection／Setter Injection／Interface Injection）：**constructor＝装订时定死，setter/interface＝装订后可换**。两级装订＋一级运行时注入，正是这个谱系的两端。

**框架圈那句话的正确读法**（避免照抄出错）：

- OpenAI 指南 "Multi-agent systems can be modeled as graphs, **with agents represented as nodes**"——角色**装订进**节点，不是角色与节点合成一个对象；
- Swarm README "…it can also be used to represent a very specific workflow or step… **all represented by the same primitive**"——说的是**同一原语可承担两种语义**，不是说不必区分两种语义；
- LangGraph "You MUST **compile** your graph before you can use it"——**compile 就是装订时刻**，编译后不可变，运行时跑的是编译产物。

即：框架统一的是**原语与装订产物**，不是**对象模型**。

## 内容分工（造节点 vs 造专家时别写串）

| 对象 | 该写什么 | 出处 |
|---|---|---|
| **节点** | **工序流程、出口结构等标准规范**——入口／出口／判据／门禁 | ISO 9000 对 procedure 的定义："specified way to carry out an activity or a process" |
| **专家** | **工序和结构无关的方法论**——一套以人扮演的角色为参照的理论科学知识的**激活提示词** | CrewAI 的 backstory："Provides context and personality to the agent" |

**运行时节点与专家已合并好**——合并的是**可运行单元**，不是文档；真源层两个对象仍各自独立、各自演进。这正是 PUFF 的结构：引擎（岗位）原样复用，知识（经验）整体替换。

**分层的正确说法**：对象模型层分专家／节点（存储解耦）→ 装订层合成可运行单元（编译期合并）→ 检索层注入经验（运行时）。**"解耦"与"合并"发生在不同层，不矛盾。**

## 无命中三态（路由层怎么设计）

**先看负空间**：Anthropic《Building effective agents》全文只有 routing「分类并转发」，**没有 no-match 分支**；OpenAI《A Practical Guide to Building Agents》34 页全文 **0 处 "routing"**，最接近的只有"失败阈值→升级人类"。两大厂商唯一内建的"无合适工具"语义是 `tool_choice` 的 `auto`/`none`。**「能力库层面没有匹配能力时该怎么办」没有任何权威来源把它当一等模式写过。**

> **状态**：`auto` / `required` 两档有标准正文级先例；`no-match` 仍属业界空白（我方显式化即贡献）。整组未入正式协议，落协议前不得作为验收判据引用。

| 态 | 语义 | 出处 |
|---|---|---|
| `auto` | 允许专家以通用能力直接作答（降级） | OpenAI/Anthropic：`tool_choice: auto`＝"Call zero, one, or multiple functions"；JSON Schema `$vocabulary: false` → "**SHOULD** proceed" |
| `required` | 必须命中某技能，否则**显式报错**（强约束节点用） | `tool_choice: required`；**JSON Schema 2020-12 §8.1.2 正文级**：`$vocabulary: true` → "implementations that do not recognize the vocabulary **MUST refuse to process**"；链接器未解析符号＝硬错误（`--unresolved-symbols=report-all` 为默认） |
| `no-match` | 返回「能力库无匹配」＋建议（新建技能 or 升级人类） | OpenAI human intervention："gracefully transfer control when it can't complete a task"；**此态未找到任何权威来源，显式化即我方贡献** |

**硬语义的粒度（三档表＝正文级；「硬语义只能在模块层」＝推论·非原文）**：`$vocabulary` 正文规定 "**It MUST NOT appear in subschemas**"，且强度在层级上不对称——**以下三档均为正文级原文**（JSON Schema 2020-12 §4.3.1／§6.5／§8.1.2）：

| 层级 | 未识别时语义 | 强度 |
|---|---|---|
| 模块（vocabulary）标必需 | "MUST refuse to process" | **硬拒绝** |
| 模块（vocabulary）标可选 | "SHOULD proceed" | 软继续 |
| 单条规则（keyword） | "SHOULD be treated as annotations" | **只有软降级** |

→ **【推论·非原文】**（提出：res-sw-eng-analog；逻辑复核：res-standard-axis）：既然 §4.3.3 明说 "there is no analogous mechanism to indicate individual keyword usage"，单条规则层**连"必需"都声明不出来**，则**硬语义只有划在模块／用途粒度上才成立**。搬到本体系：`required` 只能声明在节点契约（元层），不得由每个技能自己声明"我是必需的"——写在技能层只能得到"建议"，得不到"必须"。

**引用时不可把两者混为一谈**：三档表是原文，可作硬引证；「只能划在模块层」是推论，须带标签，且可被推翻。

回退链：技能未命中 → 通用推理（`auto`）→ 仍不行 → 升级人类；技能运行时失效/被撤 → 熔断＋降级响应（circuit breaker）；技能依赖缺失 → 分 mandatory（停）与 optional（降级运行）两级（OSGi Declarative Services 策略：未解析依赖则不启动 bundle＝fail fast）。

## 三处必须修正的引用（照错会失分）

1. **ACT-R 没有 episodic memory**。ACT-R 官方只有 declarative＋procedural 两种记忆模块；procedural/semantic/episodic **三分是 Soar 的划分**（Soar 官方："Soar distinguishes three different types of LTM: procedural, semantic, and episodic"）。
2. **CBR 的起源是 Schank 1982《Dynamic Memory》**（Aamodt & Plaza 原文 `[Schank-82]`）；Schank & Abelson 1977《Scripts, Plans, Goals and Understanding》是脚本理论出处、CBR 的前史。两者都属实，引错年代失分。
3. **「挂载」不是学界标准词**。标准表述是「**运行时检索注入**（retrieve-time injection）」：RAG 的 non-parametric memory／CBR 的 RETRIEVE／in-context learning／episodic memory retrieval。对外文本用后者并援引出处。

## 自检（造之前跑一遍）

| # | 自测 | 判法 |
|---|---|---|
| 1 | 期别已定 | 能一句话答「这东西何时确定？」—编译期 / 运行时（技能层是"声明编译期、挂载运行时"，须说明是哪一段） |
| 2 | 装订点已定 | 若涉及多个对象，写明哪个环节装订、装订后可不可换 |
| 3 | 内容没写串 | 节点件里没有"方法论"；专家件里没有"工序步骤／出口结构" |
| 4 | 运行时不烧编译期预算 | 没为"以后可能要变"把编译期对象做成可配项（配置项存在即会被打开） |
| 5 | 路由有出口 | 若设计了检索/调度，必须答"查不到时怎么办"（三态至少选一态，缺席＝黑洞） |
