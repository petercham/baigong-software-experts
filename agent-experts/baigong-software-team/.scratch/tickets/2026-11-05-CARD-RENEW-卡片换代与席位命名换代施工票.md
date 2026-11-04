# CARD-RENEW 百工团卡片换代＋席位命名换代施工票（架构席·票面起草；交付面写入＝工程师席执行）

<!-- 已撤HOLD（主理人·2026-11-05）：双席独立审票清账完毕——产品席 红0黄2绿12（a4144c9/7f8f39f）＋QA席 红1黄5绿8（78ffa5b/4e4731f）；红项R1＋黄项Y1/Y2/Y3/Y4 已由起草席修票落链 31cef54 机检自证（对账1/SKIP0）；A席黄2（tags行话）与QA席Y5（displayDescription截尾）留②预览挂卡段。工程师可开工。 -->

- 开端读数：devkits HEAD 以本票 commit 实测为准（起草时实测 `4d52e88`；审票清账修正轮开工实测 `4e4731f`，双席审票在链 a4144c9/7f8f39f/78ffa5b）。
- 背景（决策依据·自包含）：卡片名字表态轮实锤五席花名／职业标签／头像引用文件名与市场参照产品 software-company v1.1.0 注册卡逐字全撞（五席意见件在链：341fcb6／dd14821／c3dde2f+db99a6b／ddf0755+6d4610b／4fa464b+ce6b060+20d7aea；卡片审查提案件在链 0678816）。皮总终裁（裁定登记件 `.collab/decisions/2026-11-05-皮总裁定-席位职业标签与花名换代.md`，commit 4d52e88）：职业标签 zh 换代＝交付总监→项目负责人、产品经理不变、架构师→架构工程师、工程师→开发工程师、QA工程师→质量审计师；花名换代＝齐活林→包好用、许清楚→姜通透、高见远→顾长远、寇豆码→柯会码、严过关→沈得严；en 默认随动＝Bao/Jiang/Gu/Ke/Shen＋Project Lead/Product Manager 不变/Architect Engineer/Development Engineer/QA Auditor；头像文件名换代随票、图像不重制；席位 id 与席位卡文件名不动；历史链不改写。卡片文案同票换代（提案 §三 候选＋五席意见定稿，定稿文本见本票 T 节，工程师逐字照录）。
- 换代映射总表（本票一切替换的唯一真源）：

  | 席位 | 花名 zh | 花名 en | 职业 zh | 职业 en | 头像新引用 |
  |---|---|---|---|---|---|
  | software-team-lead | 齐活林→包好用 | Qi→Bao | 交付总监→项目负责人 | Delivery Director→Project Lead | avatars/software-team-lead.png |
  | software-team-product | 许清楚→姜通透 | Xu→Jiang | 产品经理（不变） | Product Manager（不变） | avatars/software-team-product.png |
  | software-team-architect | 高见远→顾长远 | Gao→Gu | 架构师→架构工程师 | Architect→Architect Engineer | avatars/software-team-architect.png |
  | software-team-engineer | 寇豆码→柯会码 | Kou→Ke | 工程师→开发工程师 | Software Engineer→Development Engineer | avatars/software-team-engineer.png |
  | software-team-qa | 严过关→沈得严 | Yan→Shen | QA工程师→质量审计师 | QA Engineer→QA Auditor | avatars/software-team-qa.png |

  裁定登记件注记①在册：裁定原文「高远见」系「高见远」笔误，映射对象＝架构席花名→顾长远。
- 改动面闭集＝21 件（16 改＋5 改名）：

  改（16）：
  1. `agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json`
  2. `agent-experts/baigong-software-team/plugin.json`
  3. `agent-experts/baigong-software-team/bundle.lock`
  4. `agent-experts/baigong-software-team/agents/software-team-lead.md`
  5. `agent-experts/baigong-software-team/agents/software-team-product.md`
  6. `agent-experts/baigong-software-team/agents/software-team-architect.md`
  7. `agent-experts/baigong-software-team/agents/software-team-engineer.md`
  8. `agent-experts/baigong-software-team/agents/software-team-qa.md`
  9. `agent-experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md`
  10. `agent-experts/baigong-software-team/skills/software-orchestration/references/quick-mode.md`
  11. `agent-experts/baigong-software-team/skills/software-orchestration/references/bugfix-path.md`
  12. `agent-experts/baigong-software-team/skills/software-orchestration/references/collab-rules.md`
  13. `agent-experts/baigong-software-team/skills/software-orchestration/references/partial-workflows.md`
  14. `agent-experts/baigong-software-team/docs/PRODUCT.md`
  15. `agent-experts/baigong-software-team/docs/ARCHITECTURE.md`
  16. `agent-experts/baigong-software-team/README.md`

  改名（5，git mv，图像本体零动）：
  17. `agent-experts/baigong-software-team/avatars/software-company-team-lead.png` → `avatars/software-team-lead.png`
  18. `agent-experts/baigong-software-team/avatars/software-product-manager.png` → `avatars/software-team-product.png`
  19. `agent-experts/baigong-software-team/avatars/software-architect.png` → `avatars/software-team-architect.png`
  20. `agent-experts/baigong-software-team/avatars/software-engineer.png` → `avatars/software-team-engineer.png`
  21. `agent-experts/baigong-software-team/avatars/software-qa-engineer.png` → `avatars/software-team-qa.png`

<!-- 声明闭集＝OA-D6-5 机检源，逐行（括注移出声明行本体，R1 修正：DECL_LINE_RE 要求「声明闭集」紧邻冒号） -->
- 声明闭集：
  - agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json
  - agent-experts/baigong-software-team/plugin.json
  - agent-experts/baigong-software-team/bundle.lock
  - agent-experts/baigong-software-team/agents/software-team-lead.md
  - agent-experts/baigong-software-team/agents/software-team-product.md
  - agent-experts/baigong-software-team/agents/software-team-architect.md
  - agent-experts/baigong-software-team/agents/software-team-engineer.md
  - agent-experts/baigong-software-team/agents/software-team-qa.md
  - agent-experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md
  - agent-experts/baigong-software-team/skills/software-orchestration/references/quick-mode.md
  - agent-experts/baigong-software-team/skills/software-orchestration/references/bugfix-path.md
  - agent-experts/baigong-software-team/skills/software-orchestration/references/collab-rules.md
  - agent-experts/baigong-software-team/skills/software-orchestration/references/partial-workflows.md
  - agent-experts/baigong-software-team/docs/PRODUCT.md
  - agent-experts/baigong-software-team/docs/ARCHITECTURE.md
  - agent-experts/baigong-software-team/README.md
  - agent-experts/baigong-software-team/avatars/software-team-lead.png
  - agent-experts/baigong-software-team/avatars/software-team-product.png
  - agent-experts/baigong-software-team/avatars/software-team-architect.png
  - agent-experts/baigong-software-team/avatars/software-team-engineer.png
  - agent-experts/baigong-software-team/avatars/software-team-qa.png

- 口径约束（全票通用）：①「标签位」＝卡片字段值、流程图行、`席位名（花名）`括注位、docs 名录行——一律按映射总表换代；②正文泛指席位简称（「工程师席」「架构席」「分派给架构师」「工程师完工回执」等组合词）＝席位名用语，**不换**（席位 id 不动的同一口径）；③裸「架构师」「工程师」不入归零断言串（见验收 A2），裸「QA工程师／QA 工程师」「交付总监」「Software Engineer」「Software Architect」「Delivery Director」「QA Engineer」入归零断言串，出现即须换代。

## T1 `.codebuddy-plugin/plugin.json`（注册卡·展示面真源）

1. L3 `"version": "0.1.22",` → `"version": "0.1.23",`
2. L4 `description` 整值替换（逐字）：
   `"description": "Baigong Software Team: five-seat SOP-driven software delivery — six-node flow with ledger-as-truth state machine, lease-gated writes, dual-seat independent review, built-in advisor-meeting and deep-research skills, four-stage deploy chain.",`
3. L42–45 `displayDescription` 整块替换（逐字）：

```json
  "displayDescription": {
    "en": "Auditable five-seat software delivery team: a Project Lead orchestrates Product, Architect Engineer, Development Engineer and QA Auditor. Work starts from requirements and acceptance criteria and runs the six-node flow (requirement, design, ticket breakdown, execution, release, grayscale) serially. Ledger as single source of truth, lease-gated writes and mechanical gates; Product and QA seats review every output independently — the producer never self-verdicts, the human keeps final call. Built-in advisor-meeting facilitation and evidence-based deep research; releases go through the four-stage gate chain: assemble, preview, human verification, deploy.",
    "zh": "五席协作的可审计软件交付专家团：项目负责人统筹产品、架构、工程、质量审计四席，从需求与验收标准出发，沿六节点流程（需求→设计→拆票→执行→发布→灰度）串行推进；账本为唯一真相、租约写侧校验与机械门禁执法；产品席＋QA席对产出做独立复审（生成方不自判，人类保留终裁）；内置外部顾问讨论会主持与证据型深度调研能力，上线走『装配→预览→人工验证→部署』四段闸口链。"
  },
```

4. L48–51 `defaultInitPrompt` 整块替换（逐字）：

```json
  "defaultInitPrompt": {
    "zh": "我是项目负责人包好用，带产品、架构、工程、QA 四席。告诉我你要落地的目标——我先把目标落成可验收的需求，再判档路由（标准 SOP／维护票／部分工作流／增量开发），执行期一票活跃、跨席信息经我中转，每步收口有独立复审与账本留痕，终裁归你。",
    "en": "I am Bao, Project Lead, with Product, Architect Engineer, Development Engineer and QA Auditor on my team. Tell me the goal — I first turn it into an acceptable requirement, then route it (standard SOP / maintenance ticket / partial workflow / incremental development). One ticket is active during execution, cross-seat information flows through me, every step closes with independent review and a ledger trail, and the final call stays with you."
  },
```

5. L53–57 `tags` 整块替换（逐字）：

```json
  "tags": [
    { "en": "Software Delivery (SOP)", "zh": "软件交付（SOP）" },
    { "en": "Ledger & Write Gates", "zh": "账本与写侧门禁" },
    { "en": "Independent Review & Audit", "zh": "独立复审与审计" }
  ],
```

6. L58–71 `quickPrompts` 整块替换（5＋1＝6 条，逐字；宿主字段若限 5 槽则删第 6 条，见候裁⑦）：

```json
  "quickPrompts": [
    {
      "en": "I have a development requirement — run the standard flow: PRD, system design, ticket breakdown, serial execution, independent acceptance, with verdict evidence at every step.",
      "zh": "我有一个开发需求，请按标准流程走一遍：出 PRD、出设计、拆票、串行执行、独立验收，每步留判定证据。"
    },
    {
      "en": "Independently review this design or delivery against a three-state coverage matrix item by item, list the must-fill gaps — the producer never self-verdicts, and the final call stays with me.",
      "zh": "这份设计／交付请做独立复审：按三态覆盖矩阵逐项给结论，列出必补项——生成方不自判，终裁归我。"
    },
    {
      "en": "Host an external advisor meeting: prepare the topic pack, run multiple rounds of written exchange, and converge into a resolution document.",
      "zh": "组织一场外部顾问讨论会：帮我编制议题包，多轮书面交流后收敛出决议件。"
    },
    {
      "en": "Research this tech choice, competitor or market: multi-source with citations and falsifiable conditions — lock the question before acting.",
      "zh": "调研这个技术选型／竞品／市场：要多源带引用、给出可推翻条件，先锁问题再动手。"
    },
    {
      "en": "When changes to this team's own package or system go live: take the four-stage chain — assemble first, mount a preview card, and after my manual verification approve the formal deploy.",
      "zh": "本专家团自身的包／系统改动要上线时：按四段链上到预览——先装配、挂预览卡，我人工验证通过后再批准正式部署。"
    },
    {
      "en": "Make one interface-preserving lightweight change to this existing project via a maintenance ticket: requirements, design and ticket breakdown merge into a light sign-off, while acceptance, release and grayscale stay intact — reconcile the change list item by item.",
      "zh": "给这个已有项目做一处不改接口的轻量变更，走维护票：需求／设计／拆票合轻签，验收、发布、灰度不减免，改动清单逐项对账。"
    }
  ],
```

7. L72–108 `members` 整块替换（逐字；`displayName`/`profession`/`avatar` 按映射总表，`id`/`role` 不动）：

```json
  "members": [
    {
      "id": "software-team-lead",
      "displayName": { "en": "Bao", "zh": "包好用" },
      "profession": { "en": "Project Lead", "zh": "项目负责人" },
      "avatar": "avatars/software-team-lead.png",
      "role": "lead"
    },
    {
      "id": "software-team-product",
      "displayName": { "en": "Jiang", "zh": "姜通透" },
      "profession": { "en": "Product Manager", "zh": "产品经理" },
      "avatar": "avatars/software-team-product.png",
      "role": "member"
    },
    {
      "id": "software-team-architect",
      "displayName": { "en": "Gu", "zh": "顾长远" },
      "profession": { "en": "Architect Engineer", "zh": "架构工程师" },
      "avatar": "avatars/software-team-architect.png",
      "role": "member"
    },
    {
      "id": "software-team-engineer",
      "displayName": { "en": "Ke", "zh": "柯会码" },
      "profession": { "en": "Development Engineer", "zh": "开发工程师" },
      "avatar": "avatars/software-team-engineer.png",
      "role": "member"
    },
    {
      "id": "software-team-qa",
      "displayName": { "en": "Shen", "zh": "沈得严" },
      "profession": { "en": "QA Auditor", "zh": "质量审计师" },
      "avatar": "avatars/software-team-qa.png",
      "role": "member"
    }
  ]
```

（L1–2 其余键、L9–41 团队级 displayName/profession/avatar/team.png、agents[]/skills[]/teamInfo 零动。）

## T2 `plugin.json`（包装卡·与注册卡消除口径分裂）

1. L3 `"version": "0.1.22",` → `"version": "0.1.23",`
2. L4 `description` 整值替换为 T1.2 同一串（逐字）。
3. L39–42 `displayDescription` 整块替换为 T1.3 同一块（逐字）。
4. L45–49 `tags` 整块替换为 T1.5 同一块（逐字）。
5. L50–54 `quickPrompts` 整块替换为 T1.6 同一块（逐字）。
6. L55–96 `members` 整块替换（逐字；本卡 members 每项含 `name` 与 `displayName` 两键，两键同值换代，其余结构不动）：

```json
  "members": [
    {
      "id": "software-team-lead",
      "name": { "en": "Bao", "zh": "包好用" },
      "displayName": { "en": "Bao", "zh": "包好用" },
      "profession": { "en": "Project Lead", "zh": "项目负责人" },
      "avatar": "avatars/software-team-lead.png",
      "role": "lead"
    },
    {
      "id": "software-team-product",
      "name": { "en": "Jiang", "zh": "姜通透" },
      "displayName": { "en": "Jiang", "zh": "姜通透" },
      "profession": { "en": "Product Manager", "zh": "产品经理" },
      "avatar": "avatars/software-team-product.png",
      "role": "member"
    },
    {
      "id": "software-team-architect",
      "name": { "en": "Gu", "zh": "顾长远" },
      "displayName": { "en": "Gu", "zh": "顾长远" },
      "profession": { "en": "Architect Engineer", "zh": "架构工程师" },
      "avatar": "avatars/software-team-architect.png",
      "role": "member"
    },
    {
      "id": "software-team-qa",
      "name": { "en": "Shen", "zh": "沈得严" },
      "displayName": { "en": "Shen", "zh": "沈得严" },
      "profession": { "en": "QA Auditor", "zh": "质量审计师" },
      "avatar": "avatars/software-team-qa.png",
      "role": "member"
    },
    {
      "id": "software-team-engineer",
      "name": { "en": "Ke", "zh": "柯会码" },
      "displayName": { "en": "Ke", "zh": "柯会码" },
      "profession": { "en": "Development Engineer", "zh": "开发工程师" },
      "avatar": "avatars/software-team-engineer.png",
      "role": "member"
    }
  ]
```

（注意本卡 members 顺序为 lead/product/architect/qa/engineer，照此保持，不随注册卡重排。）

## T3 `bundle.lock`

L5 `"version": "0.1.22",` → `"version": "0.1.23",`（其余行零动；三同源＝T1.1/T2.1/T3.1 同值）。

## T4 五席位卡（`agents/software-team-*.md`·仅 frontmatter 姓名职业四行＋正文标题行花名位）

标题行格式 `# <席位名> - <花名>`：席位名不动、只换花名（席位名≠职业标签，口径②）。

1. `agents/software-team-lead.md`：frontmatter `en: "Qi"`→`en: "Bao"`；`zh: "齐活林"`→`zh: "包好用"`；`en: "Delivery Director"`→`en: "Project Lead"`；`zh: "交付总监"`→`zh: "项目负责人"`；L13 标题 `# 主理人 - 齐活林`→`# 主理人 - 包好用`。
2. `agents/software-team-product.md`：`en: "Xu"`→`en: "Jiang"`；`zh: "许清楚"`→`zh: "姜通透"`； profession 两行不动；L16 标题→`# 产品 - 姜通透`。
3. `agents/software-team-architect.md`：`en: "Gao"`→`en: "Gu"`；`zh: "高见远"`→`zh: "顾长远"`；`en: "Architect"`→`en: "Architect Engineer"`；`zh: "架构师"`→`zh: "架构工程师"`；L16 标题→`# 架构 - 顾长远`。
4. `agents/software-team-engineer.md`：`en: "Kou"`→`en: "Ke"`；`zh: "寇豆码"`→`zh: "柯会码"`；`en: "Software Engineer"`→`en: "Development Engineer"`；`zh: "工程师"`→`zh: "开发工程师"`；L16 标题→`# 工程师 - 柯会码`。
5. `agents/software-team-qa.md`：`en: "Yan"`→`en: "Shen"`；`zh: "严过关"`→`zh: "沈得严"`；`en: "QA Engineer"`→`en: "QA Auditor"`；`zh: "QA工程师"`→`zh: "质量审计师"`；L16 标题→`# QA - 沈得严`。

（席位卡其余正文零动——实测五卡正文无旧花名/旧职业标签命中，grep 取证在起草回执。）

## T5 技法卷正文句随动（`skills/software-orchestration/references/`·occurrence 口径逐行点名）

1. `standard-sop.md`：
   - L8 流程行（逐字替换）：`用户需求 → 产品经理(PRD) → 架构工程师(系统设计+任务分解) → 开发工程师(代码实现) → 质量审计师(测试验证)`
   - L15：`**分派给产品经理（姜通透）**：将需求转发给姜通透创建 PRD 文档。`
   - L20：`**分派给架构工程师（顾长远）**：PRD 完成后，转发给顾长远进行系统架构设计 **+ 任务分解**。架构师一次性输出：`（句尾「架构师一次性输出」＝泛指主语，照口径②不动）
   - L31：`**分派给开发工程师（柯会码）**：任务列表就绪后，转发给柯会码编写代码。工程师将：`（「工程师将」泛指主语不动）
   - L38：`**分派给质量审计师（沈得严）**：代码编写完成后，转发给沈得严进行测试。QA 工程师将：`——本行句尾「QA 工程师将」入归零断言串，替换为「质量审计师将」。全行定稿：`5. **分派给质量审计师（沈得严）**：代码编写完成后，转发给沈得严进行测试。质量审计师将：`
   - L41：`     - 源码有Bug → 反馈给开发工程师（柯会码）修复`
2. `quick-mode.md`：L12 流程行→`用户需求 → TeamCreate → 开发工程师(直接实现全部代码) → 质量审计师(验证)`；L18→`3. 分派给开发工程师（柯会码），附带：`
3. `bugfix-path.md`：L12 流程行→`用户Bug报告 → TeamCreate → 开发工程师(定位+修复) → 质量审计师(回归测试)`；L17→`2. 分派给开发工程师（柯会码）：`；L20→`3. 分派给质量审计师（沈得严）仅运行回归测试确认修复`
4. `collab-rules.md`：L10→`   - 如果质量审计师发现源码 Bug → 分派回工程师修复（附带具体错误信息和失败测试）`（「分派回工程师」泛指席位简称不动；L11–12 裸架构师／产品经理／工程师＝席位简称，入豁免白名单，见候裁①）
5. `partial-workflows.md`：L13→`- **仅测试**：仅分派给质量审计师创建测试`（L10–12、L14 裸职业简称不动，候裁①）

（`skills/sop/references/` 两基线副本、SKILL.md、dev-discipline/handoff/deploy-gate/dispatch 等其余技法卷实测零命中旧花名与断言串——`grep -rn` 取证在起草回执，不入闭集。）

## T6 docs 活文档两件套

1. `docs/PRODUCT.md`：
   - L10：`**类型**：Team 型（多角色协作团队）。主对话入口为主理人席位（项目负责人·包好用），其余四席由主理人按需编排，用户无需直连任何成员席。`
   - L48 行首格：`| 主理人（包好用·项目负责人） |`（行其余格不动）
   - L49 行首格：`| 产品经理（姜通透） |`
   - L50 行首格：`| 架构工程师（顾长远） |`
   - L51 行首格：`| 开发工程师（柯会码） |`
   - L52 行首格：`| 质量审计师（沈得严） |`
   - L8「一句话」行整行替换（逐字定稿＝本票 T7.1 新句全文内联，Y1 修正；同值注记：两处一句口径统一）：`**一句话**：百工软件团队专家团：项目负责人统筹产品经理、架构工程师、开发工程师、质量审计师四席，按固定 SOP 把需求推到可验收交付，每步留证据与判定级别。`
2. `docs/ARCHITECTURE.md`：
   - L15：`    U[用户] <--> L["主理人 · 包好用（项目负责人）<br/>software-team-lead"]`
   - L16：`    L -->|派工| PM["产品经理 · 姜通透<br/>software-team-product"]`
   - L17：`    L -->|派工| AR["架构工程师 · 顾长远<br/>software-team-architect"]`
   - L18：`    L -->|派工| EN["开发工程师 · 柯会码<br/>software-team-engineer"]`
   - L19：`    L -->|派工| QA["质量审计师 · 沈得严<br/>software-team-qa"]`
   - L74 行首格：`| 主理人 包好用 |`；L75：`| 产品经理 姜通透 |`；L76：`| 架构工程师 顾长远 |`；L77：`| 开发工程师 柯会码 |`；L78：`| 质量审计师 沈得严 |`（各行其余格不动；L28「PRD→架构师、任务列表→工程师」＝席位简称，候裁①不动）

（`docs/SWB-交接件v2.9-*.md` 登记件实测旧花名命中＝0（grep 取证起草回执），零触碰——三哈希登记件禁扰动。）

## T7 `README.md`

1. L3 替换：`百工软件团队专家团：项目负责人统筹产品经理、架构工程师、开发工程师、质量审计师四席，按固定 SOP 把需求推到可验收交付，每步留证据与判定级别。`
2. L11–13「功能」三行换代（逐字）：

```
- **5 席位 SOP 协作**：主理人（项目负责人·包好用）＋产品经理（姜通透）＋架构工程师（顾长远）＋开发工程师（柯会码）＋质量审计师（沈得严）
- **工作流路由**：主理人收到请求先判断档位（标准 SOP／维护票／部分工作流／增量开发），再定席位编排与推进顺序
- **可审计交付**：需求→设计→拆票→执行→发布→灰度六节点全程留痕；账本为唯一真相，租约写侧校验与机械门禁执法，产品席＋QA席独立复审（生成方不自判），执行期一票活跃
```

3. L17–18「使用示例」两行换代（逐字，＝T1.6 定稿 1、2 两条）：

```
- 我有一个开发需求，请按标准流程走一遍：出 PRD、出设计、拆票、串行执行、独立验收，每步留判定证据。
- 这份设计／交付请做独立复审：按三态覆盖矩阵逐项给结论，列出必补项——生成方不自判，终裁归我。
```

4. 「头像」节（现 L68 段，产品席审票黄-1 补位）整段替换（逐字）：

```
`avatars/` 六件 PNG 在位（team＝团队图，五席各一；v1.3.1 版本账在册补齐批）。替换规格：PNG/JPG、512×512 px、单张 ≤500KB，文件名对应 plugin.json members[].avatar（team.png / software-team-lead.png / software-team-product.png / software-team-architect.png / software-team-engineer.png / software-team-qa.png）。
```

（旧句「盘上无头像素材，`avatars/` 仅 `.gitkeep` 占位」与盘面实态不符（六 png 实测在位）——本票随动改正；五席文件名按映射总表换新名，team.png 不动。该节旧头像文件名不在 A1/A2 归零断言串内（断言串＝花名/职业标签，不含文件名），无判据冲突。）

5. 出身节版本账**追加一行**（append-only，既有史实行含旧花名者不回改——L61 v1.2.3 行即豁免样例）：

```
- **版本账 v0.1.23**（2026-11-05·CARD-RENEW 卡片文案＋席位命名换代批）：依皮总裁定（`.collab/decisions/2026-11-05-皮总裁定-席位职业标签与花名换代.md`）五席花名换代（包好用/姜通透/顾长远/柯会码/沈得严）＋职业标签换代（项目负责人/产品经理不变/架构工程师/开发工程师/质量审计师）＋en 随动；头像五件改名与席位 id 同族（图像本体不重制）；卡片文案换代＝displayDescription/defaultInitPrompt/quickPrompts(5+1)/tags/description 对齐提案＋五席意见定稿，注册卡与包装卡口径分裂消除；README 功能/使用示例两节换代（旧「快速模式」档位与五段旧链口径随此退役）。三同源 0.1.22→0.1.23。
```

（追加位置＝「出身」节版本账现末行之后、下一节标题之前，照该件现行登记行体例。）

## T8 头像改名与引用成对

1. 五件 `git mv`（映射见改动面闭集 17–21），图像字节零动。
2. 引用成对＝T1.7/T2.6 新 avatar 值（两卡各五处，共 10 处引用随改名同步换代）。
3. `avatars/team.png` 及其两处引用零动。
4. 图像内容注记（不施工）：现六图画面文字＝旧姓大字（v1.3.1 版本账在册样式）——裁定明示图像不重制，画面文字与新人设错位登记候裁⑥。

## 验收判据（可机械验证·工程师回执逐项附实测读数）

- **A1 旧花名归零**：`grep -roE "齐活林|许清楚|高见远|寇豆码|严过关" agent-experts/baigong-software-team/ --include="*.md" --include="*.json"` 在**豁免白名单外**命中＝0。白名单（史实/登记豁免，逐路径封闭）：`README.md` 出身节版本账行（L61 v1.2.3 行等既有史实行）、`docs/SWB-交接件v2.9-*.md`（登记件零触碰）、`.collab/**`、`.scratch/tickets/**`（本票面与历史票引用裁定原文）、git 历史面（不属盘上 grep 射程）。
- **A2 旧职业标签归零（断言串口径）**：断言串闭集＝`交付总监`、`Delivery Director`、`QA工程师`、`QA 工程师`、`QA Engineer`、`Software Architect`、`Software Engineer`——同 grep 口径白名单外命中＝0。裸「架构师」「工程师」「产品经理」不入断言串（席位简称豁免，口径②/③）；「架构工程师」「开发工程师」「质量审计师」内部含「架构师/工程师」子串，对撞时按 SUBSTR 三分账登记不判违例。
- **A3 新名成对在位（结构式判据，Y3 修正）**：每个新花名须同时命中以下**结构位**即绿，不以固定总数判——①注册卡 members 条目 `displayName` 恰 1；②包装卡 members 条目 `name`＋`displayName` 双键各 1（合计 2）；③对应席位卡 frontmatter `zh:` 恰 1＋正文标题行恰 1（合计 2）。逐席命令形如 `grep -c "顾长远" .codebuddy-plugin/plugin.json plugin.json agents/software-team-architect.md`，按文件读数为 1/2/2 即绿（回执附三文件逐文件读数；总数随正文命中浮动不作判据）。profession：五新职业 zh/en 按映射表在两卡 members＋席位卡 frontmatter 成对出现（每文件逐字段读数入回执）；avatar：五新引用名在两卡各 1（计 10）＋改名后文件在位各 1（`ls avatars/` 读数）。
- **A4 三同源同值**：`grep -n '"version"' bundle.lock plugin.json .codebuddy-plugin/plugin.json` 三读数全等＝`0.1.23`（F7：前后值各附实测，前值 0.1.22）。
- **A5 门禁**：`bash agent-skills/object-audit/scripts/run-gates.sh`（仓内在册实体，开票侧 `find` 实测换代后路径＝`agent-skills/object-audit/scripts/run-gates.sh`）GATE PASS，输出存证入回执。
- **A6 引用闭环**：`check-pointer-closure` 缺省两包面读数与前值对比不新增（附前后读数）。
- **A7 声明闭集对账**：check-ticket-reconcile 对本票声明闭集读数＝21 件全认（缺声明＝SKIP 不算绿）。
- **A8 禁动面零扰动**：`docs/SWB-交接件v2.9-*.md` 三哈希不变（3f335333…/7214ad14…/efb4f765…，登记见 README v0.1.19 行）；commit name-only 清单与声明闭集 21 件全等（改名件按 old/new 双列对齐）。

## 禁动面（红线细化）

- 席位 id／`agents/software-team-*.md` 文件名／`agents[]`/`teamInfo` 零动（裁定钉死）。
- `docs/SWB-交接件v2.9-*.md` 登记件零触碰；`.collab/**` 交付性内容零触碰；`.archive/**` 零触碰。
- 旧名在豁免白名单内**不得顺手清**（历史链不改写＝裁定注记⑤）；新名在史实行**不得回补**（append-only 不回改既有行）。
- 装配面/部署面/市场条目（`~/.workbuddy/plugins/` 全系）非仓内真源，本票零触碰，随四段链装配步传导。

## 候裁单列（票面不预设裁决，工程师见未裁候裁项对应落点照票面现案执行、呈报不擅改）

1. **裸职业简称随不随**：collab-rules L11–12、partial-workflows L10–12/L14、ARCHITECTURE L28、standard-sop 句尾主语等「架构师／工程师／产品经理／QA」泛指席位简称——本票现案＝**不换**（席位 id 不动同口径）。候皮总改判全换。
2. **lead profession.zh「项目负责人」**：与体系内席位名「主理人」并存两称——本票照裁定原文逐字「项目负责人」，不改「主理人」。
3. **包装卡 description 英文旧长句**（"SWB v2.9 assembly…ledger-as-truth…"）：本票现案＝两卡 description 统一为提案 §3.2 新串（消口径分裂）；若裁两卡 description 允许各保持异构，回退本卡旧串即可。
4. **README「一句话」L3 与 PRODUCT L8**：本票现案＝两处同新文；PRODUCT L8 若裁定保留旧句式仅换五词，按映射表替换该行五处标签词即可（该行含「交付总监」＝A2 断言串，故至少须换词，不可整行不动）。
5. **「测试」动词位**：standard-sop L38/quick-mode/bugfix-path 流程行内「测试验证／进行测试／回归测试」动词——质量审计师名下动词是否随「审计」语义改词（如「审计验证」）＝文案口味候裁；本票现案＝动词不动（最小改动）。
6. **头像图像画面文字错位**：图内旧姓大字与新人设名不符（裁定＝图像不重制），登记候裁——若日后重制另开票，本票零动。
7. **quickPrompts 槽数**：本票备 6 条；宿主字段限 5 槽时删第 6 条（维护票条）——槽数上限由工程师在②预览段实测宿主读数为准，回执登记实删数。
8. **头像改名可行性（宿主侧引用查证结论）**：起草侧实测＝宿主缓存/部署面引用皆随装配产物走（`~/.workbuddy/plugins/cache|marketplaces/…/plugin.json` 为装配面拷贝，非手改真源，已 grep 实扫），仓内真源改名无外部硬引用阻塞；若②预览段宿主读数显异常则头像回退旧名成对（文件＋两卡引用同回退），卡片其余换代不受影响。

## 自检与回执（F 系列惯例）

- 开工读数＝本票 commit 后 HEAD（票面起草读数 4d52e88）；
- run-gates GATE PASS（附输出载体路径）；check-pointer-closure 前后对比（附读数）；version 前后值各附实测 grep 读数（F7）；A1/A2 归零断言附命令与读数原文；
- 禁列过程痕迹自检 grep 用 F11 终式 `见?第\s*\d+\s*轮|轮次戳|〔[^〕]*·轮〕|轮次号[：:]`——**票面自登记自指命中（Y4 修正）**：本行自身含该终式字面＝自指命中，F11 读数预期＝1（即本行）；回执期 H6 读数按此对账，读数>1 才按三分账升级登记（H6：票面预期与实测冲突时按实测登记，不得改文凑数）；
- 回执落 `.collab/receipts/`（落点更正登记：起草时票面原写 `.collab/research/`，工程师实落＝`.collab/receipts/2026-11-05-CARD-RENEW-工程师回执v1.md`，主理人已追认该落位——更正缘由＝回执族件居 receipts 桶为新树体例，起草时误写 research 桶）：回执指针行＝`agent-experts/baigong-software-team/.collab/receipts/2026-11-05-CARD-RENEW-工程师回执v1.md`。回执内容＝开端 HEAD＋完整写入/修改/改名文件清单（与 commit name-only 全等）＋全部机制断言附实测载体（N4）。
- 传导链（四段，禁跳段）：本票收口→①装配（publish.py --assemble 产物三件套对账）→②预览（本地市场源注册挂预览卡＋quickPrompts 槽数宿主实测）→③人类闸（皮总验卡片展示＋新名实感，明示通过）→④转正（marketplace.json 条目 description 随装配产物更新）。

## 红线

- 声明闭集外零触碰；定稿文本有异议停手上报不擅改（本票 T 节＝唯一施工依据，工程师逐字照录）；append-only 不回改既有行；HOLD 位：票面送产品席＋QA席双席独立审票，审票意见清账前本票首行标「**HOLD：审票意见处置中——工程师见 HOLD 不开工**」由主理人挂/撤（F12 闸位制，起草席不自撤）。