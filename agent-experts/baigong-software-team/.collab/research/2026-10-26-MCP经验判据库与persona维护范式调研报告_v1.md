# MCP 经验判据库与 persona 维护范式调研报告 v1

## 【来源】帽

- 本席：产品经理席（pm-mcp-persona，Team: _auto_15e90588-7dd0-436b-9d06-de2f2118f90f）
- 当轮仓 HEAD 读数：`D:\multi-agent-collab-skillpack` @ `1ee7014`（`git rev-parse --short HEAD` 实测）
- 调研日期 / 全部出处访问日期：2026-10-26
- 取证方式：WebSearch / WebFetch；每条结论附 URL＋标题＋访问日期。查不到先例处已明标「未找到先例」。
- 前序报告（不重复取证，直接引用）：`2026-10-26-跨平台维度耦合与装配部署补证调研报告_v1.md`（下称【跨平台】）、`2026-10-26-仓拓扑维度分仓最佳实践调研报告_v1.md`（下称【仓拓扑】）、`2026-10-25-第二轮外部锚点核验_v1.md`（下称【锚点核验】，其 A07/A08/A10/A11/A14 已核验条目直接引用）。
- 性质：仅供决策者（皮总）对 G-8（persona 是否与专家包解耦）及「MCP 收窄为拟人化决策库」定位供料，不代拍板；只新建本文件，不改任何既有文件。

---

## TL;DR

- **A（MCP 经验判据库）一行**：**可行且已有近形先例**——「把品味/审美/编辑规则类人类经验做成 MCP server、以带 ID 的检索 tool 供 agent 按需查询」有直接先例（content-knowledge-mcp：纯 markdown 判据库＋词法检索＋规则 ID 审计，无向量库），MCP 官方语义（resources＝给模型提供上下文的数据）与社区判据（「检索依赖用户问题→做成 tool」）均支持该用法；最小实现＝FastMCP＋md 库＋1 个 search tool，WorkBuddy/Claude Code/Codex/Cursor 均支持；**但社区一致判据是「小体量判据仍宜做 skill references/，MCP 只在需要跨消费者共享单一事实源＋按需检索省 context＋独立更新节奏时才划算」**——收窄定位成立，边界在此。
- **B（persona 维护范式）一行**：业界三档并存——①同文件耦合（Claude Code subagent/CrewAI/AutoGen/Coze/GPTs instructions/The Agency，与 WorkBuddy 专家包同构，是主流）；②同仓（workspace）分文件（OpenClaw SOUL.md＋模板继承、Hermes SOUL.md slot、Letta persona memory block、Relato workspace 级 voice＋per-agent 指令两层）；③独立资产被多方引用（Letta 共享 block 官方明示可 attach 多 agent、角色卡/共享 lorebook、中央 Brand Constitution 注入/RAG）——**「同一 persona 被多个 agent 复用」有实装先例，但先例形态全部是「独立文件/平台资源被引用」，git 仓拓扑级的「persona 独立仓」仍未找到先例**（维持【仓拓扑】启示#8）。

---

## A. MCP 收窄为「人类经验判据/拟人化决策库」

### A-1 实况：有无「人类经验判据 MCP server」先例？——有，且形态多样

| # | 先例 | 内容形态 | 与本案「经验判据库」的距离 | 出处（访问 2026-10-26） |
|---|---|---|---|---|
| A1 | **content-knowledge-mcp**（Glama 目录） | 公司编辑知识＝品牌规则（R# ID）、视觉模板目录（T#）、过往帖子与成效，全部**纯 markdown 文件**；3 个 tool（search_guidelines / list_visual_templates / get_post_examples）；**刻意不用向量库**——「规则带 ID、agent 引用 ID、人审 `rules_used: ["R920","R903"]` 可秒级审计；embedding 返回段落，不返回论证」；词法检索、查不到返回 NO_MATCH；stdio 跑 Claude Desktop/Claude Code，KNOWLEDGE_PATH 换目录即换公司 | **最近形先例**：品味/规则/成效经验＝带 ID 的 md 判据库＋检索 tool＋审计闭环，与「让内容生产更有品味」的定位几乎同构 | https://glama.ai/mcp/servers/alessandro-martelli/content-knowledge-mcp |
| A2 | RAG MCP Server（LobeHub 目录） | .md/.txt 知识文件→ChromaDB 向量库；tool＝search_knowledge/list_sources，resource＝rag://info 统计；任何 MCP 客户端可查 | 先例（RAG-over-MCP 模式），但走向量检索，与 A1 的「小体量判据词法检索＋ID 审计」构成两条技术路线对照 | https://lobehub.com/mcp/lluiscv99-rag-mcp-server |
| A3 | rag-mcp（Postgres+pgvector） | 五 tool（ingest/search/list/delete/reindex）；「只负责检索链路，生成交回调用方大模型」；可 stdio 本地跑给 Claude Desktop | 先例（检索与生成分离的 MCP 边界纪律） | https://www.jxxy.net/ai/articles/a-gh-2026-10-15-3365-rag-mcp-pgvector-retrieval-server |
| A4 | Microsoft Foundry Local「Agentic Retrieval」内置 MCP server | 平台把 RAG 检索能力（search_hybrid/search_vector/search_text…）暴露为 MCP tools，任何 MCP 客户端连接查询已摄入集合 | 厂商级先例：知识检索作为 MCP tool 面是微软产品线的一等形态 | https://learn.microsoft.com/en-ca/azure/azure-arc/agents-tools-foundry-local/mcp-server-overview |
| A5 | OpenAI Docs MCP（官方托管） | OpenAI 官方托管公开 MCP server（streamable HTTP），只读检索/阅读官方文档；官方建议配 AGENTS.md 片段＋OpenAI Docs **Skill** 引导 agent 优先走该 MCP | 一手平台先例：**知识供给走 MCP＋使用引导走 Skill 的组合**正是「判据 MCP＋纪律 skill」的现成搭配 | https://developers.openai.com/learn/docs-mcp |
| A6 | 反例对照：品味类内容也大量以 Skill 形态交付 | samber `copywriting-prose-creator` skill：品牌语气/句式/节奏/词汇判据全部写在 SKILL.md＋references/（含 SOUL.md/TONE.md 读取约定）；Google Gemini `curation` skill：品味档案（interests.json）＋选择与排名判据写成 skill | 「品味/审美判据」并非 MCP 独占场景，Skill references/ 同样承载且更轻量 | https://mcpservers.org/th/agent-skills/samber/copywriting-prose-creator ；https://mcpservers.org/zh-CN/agent-skills/google-gemini/curation |

**与「做成 Agent Skills 的 references/」对比（社区一致判据）**：

| 维度 | MCP 判据库 | Skill references/ | 出处 |
|---|---|---|---|
| 定位口诀 | 「MCP＝访问层（能触达什么），Skill＝程序层（该怎么做）」；「写指令→skill，写远端系统客户端→MCP」 | 同左 | https://ruleskill.com/learn/mcp-vs-agent-skills |
| context 成本 | 多数客户端连接时**前置加载全部 tool 定义**，每次调用再叠加结果；tool 数超过约 40 个（Cursor）开始劣化，平均每 server ~12 tool | 渐进披露：未激活只占 name＋description，正文与 bundled files 按需加载——**大体量指令集做成 skill 比做成 tool 描述省 context** | https://www.descope.com/blog/post/mcp-vs-skills ；https://mcptrove.com/blog/best-mcp-servers-for-writing ；https://ruleskill.com/learn/mcp-vs-agent-skills |
| 何时选 MCP | 「公司知识库带结构化资源→MCP（资源发现是核心）」「需要跨客户端单一事实源、集中更新」 | 「agent 已能触达一切但做得不一致→skill」「Markdown 比 server 便宜迭代」 | https://dockup.ai/blog/agent-skills-vs-mcp ；https://www.mdskills.ai/ja/docs/skills-vs-mcp |
| 运维成本 | 需要进程/部署/版本/信任边界（server 可在稳定 tool 名后改行为） | 零进程，文件即资产；风险＝指令陈旧 | https://www.descope.com/blog/post/mcp-vs-skills ；https://dockup.ai/blog/agent-skills-vs-mcp |

### A-2 「很难固化的判据」收窄定位是否成立？——成立，且属 MCP 惯用场景，但入口应是 tool

- **官方语义**：MCP 官网把 MCP 定位为连接「data sources（本地文件、数据库）、tools、workflows（specialized prompts）」的开放标准——**知识/上下文供给本就是 MCP 官方三用途之一**（https://modelcontextprotocol.io/ ，访问 2026-10-26）。
- **resources 规范原文**（spec 2025-06-18）：resources＝「servers 用来分享 *data that provides context to language models*（文件、数据库 schema、应用信息）」，**application-driven**（由宿主应用决定如何注入上下文，可 UI 选择/搜索/自动纳入），只读、URI 寻址，带 `audience`/`priority`/`lastModified` 注解供宿主排布优先级（https://modelcontextprotocol.io/specification/2025-06-18/server/resources ，访问 2026-10-26）。
- **判据类内容的正确落位**（社区三源一致）：「Does the AI need to KNOW something → Resource；DO something → Tool」（https://webmcpguide.com/articles/mcp-tools-vs-resources-vs-prompts ）；但**「检索依赖用户问题（如搜索知识库）的内容必须是 tool，不是 resource」**（https://exotechnologies.xyz/research/mcp-tools-resources-prompts ）；resource 适合「相对静态、跨对话普遍有用」的小体量内容，「只在偶尔需要时按需取」的内容用 tool 更省 context（https://skillful.sh/blog/the-real-difference-between-mcp-resources-and-tools-1 ）。
- **判定**：把「品味/审美/决策启发式」做成 MCP 供给**属惯用场景**（A1-A5 先例支撑）；规范上的正确装配＝**检索入口做 tool（模型按需决定查什么），少量全局基线判据可做 resource（宿主注入）**。「收窄」方向本身与官方/社区对 MCP 的用法一致；唯一保留：MCP 官方叙事的重心在「连接外部系统/实时数据」，纯静态小体量判据放 MCP 会被社区判据质疑「skill 更便宜」——收窄到「**很难固化＝体量大、更新频繁、需跨消费者共享**」的判据时，MCP 路线才占优。

### A-3 本地智能体机制下 MCP server 的运行形态

- **stdio 本地进程是主流**：「约 90% 的 MCP server 经 stdio 跑在你自己机器上，对个人写作场景是正确默认（笔记不出本机）」（https://mcptrove.com/blog/best-mcp-servers-for-writing ）；content-knowledge-mcp 即 stdio＋KNOWLEDGE_PATH 指向本地 md 目录（A1）。
- **各平台配置面**：Codex＝`~/.codex/config.toml [mcp_servers.*]`＋`codex mcp add`（stdio 与 streamable HTTP 皆支持，0.46.0+ 原生 HTTP）（https://developers.openai.com/learn/docs-mcp ；https://glama.ai/mcp/servers/@hanlulong/stata-mcp/score ）；Claude Code＝`claude mcp add --transport http|stdio`＋`/mcp` 查看（同 docs-mcp 页）；WorkBuddy＝设置→MCP 添加服务器＋OAuth 管理（https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide ），开放平台侧 Connector 走「MCP＋Skill」标准路径（connector-meta.json＋mcp.json＋skills/），**Expert 的 plugin.json 可声明 MCP/Connector 依赖**（https://aistacknav.com/tencent-workbuddy-open-platform-skill-expert-connector-mcp/ ）。
- **对用户暴露面**：安装/信任确认（WorkBuddy 连接器市场「搜索→连接→信任」三步，见执中 MCP 接入实录 http://mp.weixin.qq.com/s?__biz=MzU2Njc2MzcwMg==&mid=2247540141&idx=1&sn=e3862dc3ed4cf171c657c880b932186c ）；stdio 形态＝本地进程＋配置文件，远程形态＝URL＋OAuth。
- **与「本地包编译部署」的互补切分**（实况归纳，非先例）：本地包（bundle/skills/AGENTS.md）承载**随包版本锁定的东西**——编排图、席位 persona、流程纪律 skill；MCP 承载**跨包共享、集中更新、按需检索的东西**——经验判据库、外部系统访问。OpenAI Docs MCP＋Docs Skill 的组合（A5）就是这个分工的官方示范：判据/资料在 server，「何时查、怎么引用」在 skill。

### A-4 可行性判定：最小实现路径与平台支持面

- **技术上完全可行，最小实现极小**：参照 content-knowledge-mcp——FastMCP（Python）或 MCP TypeScript SDK＋一个 md 目录＋1-3 个检索 tool（词法检索＋条目 ID 即可起步，无需向量库）＋stdio 传输；该先例含 12/12 smoke test 与 8 例 agent 级评测（含对抗例），证明「判据 MCP」是可测试、可审计的资产形态（A1 出处）。
- **平台支持面**：MCP 为开放标准，Claude/ChatGPT、VS Code、Cursor 等广泛支持（https://modelcontextprotocol.io/ ）；本案三平台逐一证实——WorkBuddy（官方 MCP 文档＋Connector MCP+Skill 路径＋企业版「全面兼容 MCP 协议」https://www.workbuddy.cn/docs/enterprise/215846215905308672 ）；Claude Code（claude mcp add）；Codex CLI（config.toml/codex mcp）。**未见任何主流平台缺 MCP 支持**（Gemini CLI 亦在 RAG MCP 先例的支持列表内，A2）。
- **真实成本不在技术在部署**：①每平台各自配置（本地 stdio 每机装一次；远程 HTTP 需托管＋HTTPS＋30 秒内返回等 WorkBuddy 连接器要求，见 aistacknav 页）；②WorkBuddy 上架走连接器审核/市场流程；③tool 数量预算（客户端 ~40 tool 劣化线，判据 server 应只暴露 1-3 个 tool）；④信任与审计（server 可在稳定 tool 名后改行为——判据库版本化应配 digest/tag，呼应【仓拓扑】问 3 的 Helm/npm 纪律）。
- **一行判定**：**「经验判据 MCP server」可行、有近形先例、最小实现一个脚本级；建议边界＝只把「跨包共享＋需集中更新＋体量大到不宜全量入 context」的判据放 MCP，其余品味/规范类内容留在 skill references/ 与席位文件内。**

---

## B. persona 维护范式盘点（G-8 决策依据）

### B-1 主流平台/框架 persona 维护形态三档归类（2025-2026 实况）

**第一档：persona 与角色职责同文件/同字段（耦合）**

| 平台 | persona 落点 | 出处 |
|---|---|---|
| Claude Code subagent | `.claude/agents/*.md` frontmatter＋正文＝system prompt（人格语气与职责同文）；另有个人级 `~/.claude/agents/` 与项目级两层（作用域分层，非 persona 分离） | 【跨平台】问1#1（访问 2026-10-26）；The Agency 用法＝把 55 个角色 MD 直接 `cp` 进 `~/.claude/agents/`（https://mintlify.wiki/msitarzewski/agency-agents ） |
| CrewAI | agents.yaml 内 role/goal/backstory 同条配置 | 【跨平台】问1#5 |
| AutoGen | agent 组件 JSON 的 system_message 字段 | 【跨平台】问1#6 |
| Coze | 「人设与回复逻辑」单一面板 | 【跨平台】问1#7 |
| GPTs | Instructions 一个字段承载角色＋语气＋规则；但 instructions/knowledge/capabilities 三配置项分离（A10 已核验） | 【跨平台】问1#8 |
| The Agency（agency-agents，6800+ stars） | 每个角色＝一个 MD：identity＋personality＋mission＋workflow＋deliverables＋success metrics 全在内；**整个文件被多平台复用**（Claude Code 目录 / 通用 prompt 模板 / OpenClaw 模板 kit 的灵感源） | https://faycalazib.com/blog/agency-agents-complete-guide ；https://www.besthub.dev/articles/explore-the-agency-55-ai-agent-roles-organized-into-9-departments-612a9f39c647 ；https://github.com/codevjs/openclaw-multi-agent-kit （访问 2026-10-26） |

**第二档：同仓/同 workspace 内分文件（persona 独立成文件，与操作指令/技能并列）**

| 平台 | 分工 | 出处 |
|---|---|---|
| OpenClaw | SOUL.md（人格/规则）＋IDENTITY.md（name/vibe）与 AGENTS.md（路由/操作）、TOOLS.md、USER.md、skills/ 并列；**模板继承**：`~/.openclaw/templates/base-agent.md` 定义共享规则/语气，子 agent `extends:` 继承——「base-writer.md 定 tone＋formatting，seo-writer/email-writer 扩展专属技能」 | 【跨平台】问1#3；https://crewclaw.com/blog/openclaw-advanced-setup-tips ；https://clawhub.ai/neal-collab/skills/multi-agent-blueprint （访问 2026-10-26） |
| Hermes Agent | `~/.hermes/SOUL.md`＝系统提示 slot #1 持久 persona；「SOUL.md 只管你是谁，不管你要做什么」 | 【跨平台】问1#4 |
| Letta/MemGPT | `persona` memory block 与 `human`/自定义 block 分立，block 常驻 context、agent 可自编辑 | http://docs.letta.com/guides/agents/memory-blocks （访问 2026-10-26） |
| Relato（内容 agent 平台） | **workspace 级指令**（品牌 voice/tone/禁忌，所有 agent 继承）与 **per-agent 指令**（岗位专属）两层：「跨全部内容成立的放 workspace 层，单 agent 任务行为放 agent 层」 | https://help.relato.com/en/articles/15901047-give-your-agents-a-brand-voice （访问 2026-10-26） |
| A07 论文（Persona-Execution Separation） | persona（instructions/tone/self-presentation）与 execution 分离为命名架构模式——注意分离轴＝persona vs execution（信任域），**不是** persona vs 角色职责，引用不得混同 | 【锚点核验】A07（arXiv:2608.27427） |

**第三档：独立资产被多方引用（跨应用/跨仓资源级）**

| 先例 | 形态 | 出处 |
|---|---|---|
| 角色卡生态（Tavern v2/V3） | persona＝可移植独立文件资产（PNG 内嵌 JSON），跨 SillyTavern/Agnai/RisuAI 三前端无损互载；**Shared lorebooks：一个 lorebook 嵌入多张卡并链接，逐卡显示 up-to-date/out-of-date**；独立 Personas mode（persona 存为卡供转换复用） | https://promptquorum.com/power-local-llm/sillytavern-vs-agnai-vs-risuai-roleplay ；https://github.com/DevCardmaker/SillyTavern-Charactercard-Editor-and-Maker （访问 2026-10-26） |
| Letta 共享 memory block | 官方明示「create blocks that are **shared between multiple agents**」：一个 block 经 `block_ids` attach 到多个 agent，改一处全同步；示例即 persona/organization block | http://docs.letta.com/guides/agents/memory-blocks （访问 2026-10-26） |
| Brand Constitution 中央化模式 | 品牌宪法＝中央托管的单一事实源（master_constitution.json/md），数十个 agent 经 build/run-time 注入、系统级 RAG 或框架全局配置引用——「不能把品牌规则硬编码进每个 agent 的 prompt」 | https://publishing-project.rivendellweb.net/brand-constitutions-for-ai （访问 2026-10-26） |
| Coze/Dify 知识库 | 平台资源库级独立资产被多个 Bot/工作流引用（persona 本体仍耦合在 Bot 内，仅知识侧分离） | 【跨平台】问 2 矩阵 |
| persona 独立 **git 仓** | **未找到先例**（维持【仓拓扑】启示#8；本轮检索「voice.md single source of truth」等实践均为「共享目录/git 仓内共享路径」而非独立仓，见 B-2） | —— |

### B-2 耦合 vs 独立：两方案的业界证据与反例

**「persona 与专家包耦合维护」的强项证据**

1. 与消费平台同构：WorkBuddy 专家包（plugin.json＋agents/*.md）与 Claude Code subagent/CrewAI/GPTs 同构，persona 在席位文件内是这些机制的**原生形状**，拆开反而偏离平台惯例（【跨平台】问 1 结论，多源）。
2. 零部署成本、无引用失效面：文件即全部，无「引用文件缺失/版本错配」故障模式（dockup/descope 对 skill-vs-MCP 成本分析同理适用：https://dockup.ai/blog/agent-skills-vs-mcp ）。
3. 单一消费者场景无拆分收益：monorepo 实证判据——无独立发布节奏/独立归属/独立访问边界就不拆（【仓拓扑】问 1，reveneau/monorepo.tools 多源）。

**「persona 独立维护」的强项证据**

1. **复用需求有实装先例（独立维护最强理由，本轮重点核实）**：
   - Letta：一个 persona/共享 block attach 多 agent，官方文档级支持（B-1 第三档）；
   - OpenClaw：base template＋`extends:` 继承，「更新自动传播到所有子 agent」，防「五个 agent 只是五个化名」的同质化失败模式（https://crewclaw.com/blog/openclaw-advanced-setup-tips ；https://blog.csdn.net/weixin_27028523/article/details/160607304 ）；
   - The Agency：55+ 人格库被 Claude Code 目录、通用 prompt、OpenClaw kit 多形态复用（6,800+ stars 的需求信号）；
   - SillyTavern：persona 独立成卡＋shared lorebook 嵌多卡并带新鲜度状态；
   - Relato：workspace 级 voice 一次设置全体 agent 继承。
2. **复制式耦合的漂移失效模式被明确记录**：「把 voice 文件 copy-paste 进四个 agent，六个月后得到五个略有不同的版本……修复是架构性的，不是纪律性的：voice 文件只住一处，每个 agent 引用它」（https://www.goaspi.com/blog/ai-brand-voice-train-agents-write-like-you ）；「no agent works from a private version of the brand」＝共享记忆层而非各 agent 私藏 persona（https://jam7.com/blog/brand-consistency-ai-agents-one-voice ）（均访问 2026-10-26）。
3. 独立更新节奏收益：中央宪法「marketing 更新语气规则，全体 agent 即时继承，无需代码部署」（rivendellweb，B-1 第三档）。

**反例与限定**

- Hermes 社区铁律反对的是「persona 文件混入项目指令/剧本」，支持的是**文件内/文件间分工**，不等于支持跨仓分离（【跨平台】问1#4）。
- A07 的分离轴是 persona vs execution（审计信任域），不能直接引为「persona 应脱离角色包」的依据（【锚点核验】A07 注意事项）。
- 独立维护的代价：引用失效与版本错配（goaspi 的「which version is it reading」诊断；dockup「server 可在稳定名字后改行为」）；跨仓 persona 无任何仓拓扑先例（【仓拓扑】启示#8）。
- 多平台复用先例（The Agency、角色卡）的复用机制＝**整文件复制/导入**＋版本号标注（goaspi `voice-v2026-09.md`），不是运行时引用——即「复用」与「独立仓」仍是两回事。

### B-3 决策参照表（不代拍板）

| 判别条件（成立→倾向） | 耦合（persona 在席位文件内） | 独立（persona 成独立资产） | 业界依据 |
|---|---|---|---|
| 同一 persona 是否被 ≥2 个专家包/席位/平台消费 | 否（单消费者） | **是**（复用需求＝最强理由） | Letta shared blocks、OpenClaw extends、The Agency、Relato workspace 层 |
| persona 是否与所属包同节奏演进、同一维护者 | 是 | 否（独立维护者/独立更新节奏，如「品味库」由内容负责人季度更新） | 【仓拓扑】问 1 三判据；goaspi 季度更新实践 |
| persona 内容体量与注入方式 | 小体量、每次全量注入无害 | 大体量、需按需检索省 context（→可与 A 的判据 MCP 合并考虑） | descope/ruleskill context 成本对比；A1 content-knowledge-mcp |
| 目标平台机制 | 平台只认单文件 persona（WorkBuddy 席位 MD、Claude Code subagent、GPTs） | 平台原生支持引用/共享（Letta block、OpenClaw extends、Coze 资源库） | 【跨平台】问 1 矩阵；B-1 三档 |
| 是否出现复制漂移事实/风险 | 无（1-2 个包） | 已出现或可预期多副本（多包共享同一「公司腔」） | goaspi 五版本漂移案例；jam7 |
| 审计/信任要求 | 无特殊 | 需「persona 可漂移、execution 可审计」分离时 | A07（限定：persona vs execution 轴） |
| **折中形态（两档证据都支持）** | **同仓独立文件＋席位 MD 引用/分节**：persona 独立成 `personas/*.md`，席位 MD 内引用或编译期注入——先满足复用与防漂移，不升格独立仓 | | OpenClaw/Hermes 同 workspace 分文件先例；goaspi /shared-context/voice.md；Backstage「元数据贴近描述对象」（【仓拓扑】#4） |
| 升格独立仓的门槛 | —— | 仅当出现「独立归属方＋独立发布节奏＋独立访问边界」任一（如判据/persona 库对外服务其他团队的产品） | 【仓拓扑】问 1 实证三理由；persona 独立仓先例＝未找到 |

**与 A 的联动提示**：若决策者把「品味/经验判据」走 MCP（A 结论），则 persona 中「个性/语气」与「经验判据」天然分家——前者仍宜随席位（平台机制决定），后者可入 MCP 判据库；这实际上是一种「按内容性质解耦」而非「按资产维度解耦」，与三档先例全部兼容。

---

## 附：本报告新增出处清单（均访问 2026-10-26）

1. content-knowledge-mcp — https://glama.ai/mcp/servers/alessandro-martelli/content-knowledge-mcp
2. RAG MCP Server — https://lobehub.com/mcp/lluiscv99-rag-mcp-server
3. rag-mcp（pgvector） — https://www.jxxy.net/ai/articles/a-gh-2026-10-15-3365-rag-mcp-pgvector-retrieval-server
4. Microsoft Foundry Local Agentic Retrieval MCP — https://learn.microsoft.com/en-ca/azure/azure-arc/agents-tools-foundry-local/mcp-server-overview
5. OpenAI Docs MCP — https://developers.openai.com/learn/docs-mcp
6. samber copywriting-prose-creator（skill 形态品味判据） — https://mcpservers.org/th/agent-skills/samber/copywriting-prose-creator
7. Google Gemini curation skill（品味档案判据 skill） — https://mcpservers.org/zh-CN/agent-skills/google-gemini/curation
8. MCP 官网 — https://modelcontextprotocol.io/
9. MCP spec 2025-06-18 Resources — https://modelcontextprotocol.io/specification/2025-06-18/server/resources
10. MCP Client Best Practices（progressive discovery） — https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices
11. MCP vs Agent Skills（RuleSkill） — https://ruleskill.com/learn/mcp-vs-agent-skills
12. MCP vs Skills（Descope） — https://www.descope.com/blog/post/mcp-vs-skills
13. Skills vs MCP（mdskills.ai） — https://www.mdskills.ai/ja/docs/skills-vs-mcp
14. Agent Skills vs MCP（Dockup） — https://dockup.ai/blog/agent-skills-vs-mcp
15. Best MCP Servers for Writing（stdio ~90%、tool 数上限） — https://mcptrove.com/blog/best-mcp-servers-for-writing
16. MCP Tools vs Resources vs Prompts — https://webmcpguide.com/articles/mcp-tools-vs-resources-vs-prompts ；https://exotechnologies.xyz/research/mcp-tools-resources-prompts ；https://skillful.sh/blog/the-real-difference-between-mcp-resources-and-tools-1 ；https://mcporbit.com/blog/mcp-tools-vs-resources-vs-prompts
17. WorkBuddy MCP 集成文档 — https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide
18. WorkBuddy 企业版产品优势（全面兼容 MCP） — https://www.workbuddy.cn/docs/enterprise/215846215905308672
19. WorkBuddy 开放平台 Skill/Expert/Connector/MCP 教程 — https://aistacknav.com/tencent-workbuddy-open-platform-skill-expert-connector-mcp/
20. 执中 MCP 上线 WorkBuddy（连接器接入三步实录） — http://mp.weixin.qq.com/s?__biz=MzU2Njc2MzcwMg==&mid=2247540141&idx=1&sn=e3862dc3ed4cf171c657c880b932186c
21. Codex CLI MCP 参考 — https://github.com/alirezarezvani/claude-code-skill-factory/blob/dev/documentation/references/openai-codex-cli-instructions.md ；https://glama.ai/mcp/servers/@hanlulong/stata-mcp/score
22. Letta Memory blocks（共享 block 多 agent） — http://docs.letta.com/guides/agents/memory-blocks ；https://forum.letta.com/t/agent-memory-solutions-letta-vs-mem0-vs-zep-vs-cognee/85
23. OpenClaw 模板继承 — https://crewclaw.com/blog/openclaw-advanced-setup-tips
24. OpenClaw Multi-Agent Blueprint / multi-agent-kit — https://clawhub.ai/neal-collab/skills/multi-agent-blueprint ；https://github.com/codevjs/openclaw-multi-agent-kit
25. OpenClaw 多 Agent 人格矩阵（中文实践） — https://blog.csdn.net/wu560130911/article/details/160954341 ；https://blog.csdn.net/weixin_27028523/article/details/160607304
26. The Agency（agency-agents） — https://mintlify.wiki/msitarzewski/agency-agents ；https://faycalazib.com/blog/agency-agents-complete-guide ；https://www.besthub.dev/articles/explore-the-agency-55-ai-agent-roles-organized-into-9-departments-612a9f39c647 ；https://tmdm.cn/ai-expert-team-agents/
27. SillyTavern 角色卡 V2/共享 lorebook — https://sillytavern.wiki/for-contributors/writing-extensions/ ；https://promptquorum.com/power-local-llm/sillytavern-vs-agnai-vs-risuai-roleplay ；https://github.com/DevCardmaker/SillyTavern-Charactercard-Editor-and-Maker
28. Brand Constitutions for AI Agents — https://publishing-project.rivendellweb.net/brand-constitutions-for-ai
29. AI Brand Voice（voice 单一事实源＋漂移案例） — https://www.goaspi.com/blog/ai-brand-voice-train-agents-write-like-you
30. One Voice at 10× Output（共享记忆层） — https://jam7.com/blog/brand-consistency-ai-agents-one-voice
31. Relato brand voice（workspace/per-agent 两层） — https://help.relato.com/en/articles/15901047-give-your-agents-a-brand-voice
32. Brand Guidelines for AI Agents（RAG＋引用规则） — https://www.pedowitzgroup.com/how-do-i-ensure-ai-agents-follow-brand-guidelines
