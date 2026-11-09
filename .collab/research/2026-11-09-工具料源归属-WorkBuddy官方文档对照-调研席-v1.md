# 工具料源归属 · WorkBuddy 官方文档对照调研 v1（调研席）

- 当轮开工 HEAD 实测读数：`4179986ffcb7cb1ba45380ee6b4726c95f6cbe06`（首次取证时点）；落笔时点 HEAD 复测读数＝`0812beca7fe3216ac15d1156e46d386fec172957`（他席在途提交致 HEAD 随动，非本席改动；本席开工时暂存面实测＝空，落笔前复测＝空）。
- 票面背景：候裁点＝仓内通用脚本工具（散在 `tools/` 桶与 `agent-skills/*/scripts/`）的归属落位三取一：甲＝仓根新目录料源／乙＝`tools/` 升格为料源／丙＝独立组件仓。既定裁定＝「通用工具归 shareds 料源，且必须装配时自包含嵌入使用方包后才可挂载」。决策者指令＝查 WorkBuddy 官方文档取官方口径作决策依据。
- 本文＝只读调研产出，不改任何既有源码文件。

## 一、官方文档取证（逐条附来源）

### 1.1 技能（Skill）包结构规范

- 官方口径 A（WorkBuddy IDE / CodeBuddy 文档）：Skill 是「模块化的、自包含的能力包」（原文如此）。结构＝必需的 `SKILL.md`（YAML frontmatter：name、description 必填＋Markdown 指令）＋可选打包资源三目录：`scripts/`（可执行代码，Python/Bash 等）、`references/`（按需加载进上下文的文档）、`assets/`（用在输出中的文件）。来源：https://www.workbuddy.cn/docs/ide/Features/Skills
- 官方口径 B（WorkBuddy 开放平台·技能上架规范）：zip 包基础结构＝技能名目录根层的 `SKILL.md`（必须）＋`references/`＋`scripts/`＋`templates/`（皆可选）。scripts 定位原文：「存放技能执行中需要调用的脚本，AI 通过 Bash 工具执行」「使用方式：在 SKILL.md 中声明调用命令和参数」。来源：https://open.workbuddy.cn/docs/skill （英文同页 https://open.workbuddy.cn/en/docs/skill）
- 要点：两页一致——脚本随技能包**目录内嵌**分发，SKILL.md 内声明调用命令；无任何「脚本放在包外共享目录、运行时从外部取」的口径。

### 1.2 专家包 / 专家团 bundle 结构与装配语义

- 官方（开放平台·专家）：专家包基础结构＝隐藏目录 codebuddy-plugin 下的 `plugin.json`＋`avatars/`＋`agents/`＋`README.md`；`plugin.json` 有可选字段 `skills`（string[]，「技能目录路径列表（如 ["./skills/my-skill"]）」）——即技能以**包内相对路径**随专家包声明。专家团＝`expertType: "team"`＋`teamInfo {leadAgent, memberAgents}`。跨包外部能力只经 `dependencies.mcpServers`（.mcp.json）与 `dependencies.connectors`（连接器 ID 列表）声明，无任何「共享脚本/共享文件」依赖字段。来源：https://open.workbuddy.cn/docs/expert
- 官方（WorkBuddy 客户端·专家中心）：「专家本身不主动获取系统权限……当配备了 Skill / MCP 时才会在您的授权下间接访问文件或外部服务」；Skill=工具能力、专家=角色、专家团=多专家协作。来源：https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Expert-Center

### 1.3 插件（plugin）体系·自包含语义（本次最硬的一条）

- 官方（CodeBuddy 插件参考文档，https://www.workbuddy.cn/docs/cli/plugins-reference ）：
  - 插件定义原文＝「一个**自包含**的组件目录」。组件含 Skills（`skills/<name>/SKILL.md`，可带 `scripts/`，原文「技能可以包含辅助文件和脚本」）、Agents、Hooks、MCP、LSP、`bin/`（可执行文件，启用插件时加入 Bash 工具 PATH，可裸命令调用）、插件根 `scripts/`（用于钩子和实用脚本）等。
  - 自包含硬语义原文：「已安装的插件无法引用其目录之外的文件」「遍历到插件根目录之外的路径（如 `../shared-utils`）在安装后不会工作，因为那些外部文件不会被复制到缓存中」。marketplace 安装把插件整体复制到版本化缓存 `~/.codebuddy/plugins/cache/<marketplace>/<plugin>/<version>`，不原地使用。
  - 共享资源的官方口子只有两个：①同一 marketplace 内**符号链接**，缓存复制时「解引用并复制目标内容」进插件缓存（＝最终仍自包含，不是运行时跨目录读取）；②插件级 `dependencies`（整插件为依赖单元，自动装传递依赖，跨 marketplace 默认阻止、需 allowlist）。
- 结论性转述：官方模型里「共享」＝**装配/安装期复制进包**或**以完整插件为依赖单位**，不存在「多包运行时共读一个脚本料源目录」的机制。

### 1.4 共享资源 / 料源（shareds）机制有无官方定义

- 查无：workbuddy.cn / open.workbuddy.cn 官方文档中无「shareds」「料源」「共享资源目录」「跨技能共享脚本」任何命名机制。官方文档未覆盖此概念。
- 最近似的官方承载面（非脚本用途）：①项目级 `.codebuddy/skills/` 目录随项目仓库版本控制、团队共享（来源：https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Project ，该页同时列 `.codebuddy/rules|agents|commands|CODEBUDDY.md`）；②「资料库」＝文档/CSV/HTML 团队资料协作面，非代码执行面（来源：https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Library ）。

### 1.5 脚本工具随技能分发的官方口径

- 汇总 1.1/1.3：脚本随技能走 `scripts/` 内嵌；技能随专家包走 `plugin.json skills:["./skills/..."]` 内嵌；插件整体入缓存。全链路皆「复制进包」语义。另有插件级 `bin/`（可执行入 PATH）作为插件自带工具的第二形态——同样是**包内**目录。来源同 1.1、1.3 两页。

### 1.6 MCP / 连接器与技能内脚本的边界

- 官方（开放平台·连接器）：连接器＝外部服务桥，形态二选一（MCP 或 CLI），包结构固定＝connector-meta 清单＋mcp 或 cli 连接配置＋icon 图标＋skills 指引目录；连接器包**不含可执行脚本**，实际服务能力由外部 MCP Server 或外部已发布 CLI 提供（cli 配置的 init 命令装外部 CLI）。Skill 在连接器体系里只作「AI 使用指引」层。来源：https://open.workbuddy.cn/docs/connector
- 边界转述：本地确定性脚本逻辑归 skill `scripts/`（Bash 执行）；需外部服务/鉴权/进程的能力归 MCP/Connector 声明。仓内通用脚本属前者。

## 二、仓内现状对照（现读，未改）

- `tools/` 桶受版本控制面（`git ls-files tools/`）：`check-source-of-truth.py`、`check-truename.py`、`check-truename-names.txt`、`count_agent_tokens.py`、`baseline-seat-decl.json`、`baseline-sot-dup.json`、`sot-external-provenance.txt`（共 7 件）。
- 技能内嵌脚本先例（`git ls-files "agent-skills/*/scripts/*"`）：`agent-skills/object-audit/scripts/` 下 11 件（含 `check-pointers.py`、`check-skill-meta.py`、`run-gates.sh` 等）＋`agent-skills/object-build/scripts/publish.py`。专家包内另有 `agent-experts/baigong-software-team/skills/sop/scripts/` 18 件、`tests/` 探针若干——脚本已普遍按「随技能包内嵌」形态存在。
- 仓内对 `tools/` 的消费方式（grep 实测）：`agent-skills/bundle-assembly-registration/references/20-register.md`、`agent-skills/multi-collab/references/70-charter.md` 等以**仓根相对指针**引用 `tools/check-source-of-truth.py`；`agent-skills/object-audit/scripts/run-gates.sh` 以 `ROOT/tools/check-source-of-truth` 前缀跨域调用；`check-skill-meta.py` 定位仓根即认「tools/＋三分类目录」。即 `tools/` 现态＝仓级开发期工具桶，消费点全在仓内，且门禁链已硬编码 `tools/` 路径名。
- 装配语义（agent-experts/baigong-software-team/bundle.lock 现读）：components[] 锁不可变 tag（纪律②），`target` 指装配面 bundle 内相对路径（如 `skills/external-advisor-collab`），note 多处明文「装配产物＝仓外 -build 预览面＝派生非第二真源」「部署态自包含」「产物不入任何仓版本库（纪律④）」。装配器先例 agent-skills/object-build/scripts/publish.py 以 copy＋sha256 对账做包内副本。`tools/` 桶**不在**任何 bundle.lock 组件行内——它从未被装配进包。
- 仓内「料源」一词既有语义（grep 实测）：`sources/` 子包＝「唯一允许进交付物的自包含料源」（agent-skills/object-audit/references/50-document.md D6-3 行、agent-experts/baigong-software-team/skills/software-orchestration/references/dev-discipline.md）。即仓内「料源」＝进交付包的自包含素材面，与「装配期嵌入」裁定语义一致。

## 三、比较陈述：官方口径对三案的支持度

1. 「工具脚本必须随包自包含」有无明文支撑：**有，且强硬**。官方插件文档明文＝「插件是自包含的组件目录」「已安装插件无法引用目录外文件」「`../shared-utils` 安装后不工作」；技能文档把 scripts/ 定义为技能目录内资源。任何「多包运行时共读一个仓级 tools/ 目录」的方案在官方分发模型（整体复制进版本化缓存）下直接失效。
2. 甲案（仓根新目录料源）／乙案（tools/ 升格料源）：两案在**开发仓真源面**层面无官方差异——官方不管开发仓内部怎么摆目录（`.codebuddy/skills/` 项目级共享语义只覆盖技能，未覆盖脚本桶）。差别在既有链成本：乙案零改链（run-gates.sh/check-skill-meta.py/门禁基线现认 `tools/` 名），甲案需随动全部硬编码点＋24 件门禁锚面风险。两案都**必须**补「装配时复制进包」工序才可挂载——官方口径不禁止仓内共享目录作真源，禁止的是**部署态**引用包外路径。
3. 丙案（独立组件仓）：官方有相邻机制＝插件级 `dependencies`（整插件依赖单位）与 marketplace 符号链接「解引用复制」语义；但开放平台专家包文档**无**插件 dependencies 字段（仅 MCP/连接器依赖），故丙案若走「专家包依赖一个工具插件」在开放平台口径下无明文承载；走「bundle.lock 组件行＋装配期复制」则与现行 deep-research 跨仓组件先例同构（agent-experts/baigong-software-team/bundle.lock 第二组件行即跨仓取源先例），成本＝多仓版本/tag 管理。
4. 官方口径不足的部分（如实标注）：官方文档未定义「shareds/料源」命名机制；未裁决「开发仓内工具目录放哪」；插件级 dependencies 是否被 WorkBuddy 客户端专家包运行时消费无明文。故「官方文档不足以完全裁决甲乙丙」成立——官方能裁决的是**必要条件**（挂载形态必须自包含嵌入），不能裁决的是**真源摆放位置**（甲 vs 乙 vs 丙属仓内维护维度决策）。

## 四、口径结论（一句话）

官方明文支撑「自包含嵌入」这一半裁定（插件自包含＋安装即复制＋禁包外引用，来源 plugins-reference/Skills/expert 三页），对真源放甲/乙/丙无明文——三案只要都走「装配时复制进包」皆合规，差异纯在仓内维护成本，其中乙案（tools/ 升格、保留现名）改链成本最低、丙案有 bundle.lock 跨仓组件先例可依托但无官方插件依赖承载明文。

## 五、来源清单

- https://www.workbuddy.cn/docs/ide/Features/Skills （Skill 自包含能力包·scripts/references/assets 结构）
- https://open.workbuddy.cn/docs/skill （技能 zip 基础结构·scripts 子资源目录口径）
- https://open.workbuddy.cn/docs/expert （专家/专家团结构·plugin.json skills 字段·依赖仅 MCP/连接器）
- https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Expert-Center （专家/Skill/专家团分工·权限语义）
- https://www.workbuddy.cn/docs/cli/plugins-reference （插件自包含定义·bin/·禁 ../ 外引·版本化缓存·dependencies 与符号链接复制）
- https://open.workbuddy.cn/docs/connector （连接器包不含可执行脚本·MCP/CLI 二选一·Skill 仅作指引层）
- https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Project （项目级 .codebuddy/skills 随仓库共享）
- 官方文档未覆盖项：shareds/料源命名机制；开发仓内脚本目录位置裁决；专家包运行时插件级 dependencies。

（完·调研席 research-toolhome·2026-11-09）
