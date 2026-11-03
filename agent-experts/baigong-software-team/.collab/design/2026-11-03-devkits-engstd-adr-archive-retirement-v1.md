# ENGSTD · devkits 工程规范定标设计件（ADR/归档/退役三题）v1 · 架构席定标

- 起草实测 HEAD：`b003a0e`（`git rev-parse --short HEAD`·工作仓 `D:\multi-agent-collab-devkits`·main）；开工 ANCHOR 读数即此。
- 件型＝**定标设计件**（架构席职权域·皮总明示三题属工程问题不上呈拍板；完工走产品席/QA席双席独立审票，收口即生效）。本件给结论与可机械判定条款草案，不落改任何交付面/既有票面/席位卡。
- 兼容基线（只读直读）＝`.collab/decisions/2026-11-03-皮总裁定-项目自由分层与collab固定结构及docs约定md.md`（裁定三·§一~§二点九）：`.collab` 固定结构闭集、docs＝当前存活干净交接件（PRODUCT/ARCHITECTURE/STRUCTURE）、票面落 `.collab/tickets` 或 `.scratch/tickets` 二候、仓根白名单闭集。本件三题结论全部在该框架内落位，不新增固定结构桶（新增桶＝规范分叉，违裁定三§二点五.1）。
- 既有决策机理基线：「后生效覆盖先前·原件不删只作注记」（append-only·史实锚）——本件与其同轨。
- 计数口径：occurrence 口径；行号锚 HEAD=`b003a0e`；判据命令自带落盘重定向；负例 exit≠0 断言。
- 业界引用四件套体例＝来源文件名／日期／条款位置／URL，集中登记于 §四引用账。

## 声明闭集（1 件·本笔唯一可写面）
- 声明闭集：
- .collab/design/2026-11-03-devkits-engstd-adr-archive-retirement-v1.md

---

# T-A · ADR／决策记录机制

## A.1 业界最佳实践对照

1. **Nygard 格式与状态机**（2011 定式）：一条决策一件短文档，五段＝Title/Status/Context/Decision/Consequences；Status 合法取值 proposed／accepted／rejected／deprecated／superseded；**编号单调递增永不复用；被推翻的决策留在日志中标 superseded，因为「知道它曾经是决策」本身有价值**。〔来源：Architecture Decision Records Written by Your Coding Agent／2026-11-03 检索／§"What an architecture decision record is"引 adr.github.io 与 Nygard 2011／https://nimbalyst.com/blog/architecture-decision-records-written-by-your-coding-agent〕
2. **supersede 不改写纪律**：「Treat accepted records as immutable. If a decision changes, write a new ADR instead of editing the old one. Then mark the old record as superseded and link both documents together.（accepted 件视为不可变；决策变了写新件，旧件标 superseded 并双向互链）」＋常见错误清单点名「Editing accepted records — rewriting history destroys the value of the log」。〔来源：Architecture Decision Records (ADR) Explained: A Complete Guide／2026-11-03 检索／§Status Lifecycle of Architecture Decision Records＋§Common Mistakes with Architecture Decision Records／https://vickybytes.com/blog/architecture-decision-records-explained〕
3. **MADR 状态与替代流程**：Status 取值闭集 `proposed | accepted | rejected | deprecated | superseded by <adr>`；supersession 程序＝新建 ADR→旧件 Status 改 `Superseded by new-adr`→新件反向链接 `Supersedes old-adr`（双向）。〔来源：MADR 模板实战指南／2026-11-03 检索／§元数据头 Status 取值＋§八 supersession 流程／https://blog.csdn.net/gitblog_00602/article/details/161209131；模板真源 adr.github.io/madr〕
4. **落位惯例与「ADR 长存 vs 过程物归档」之分**：业界惯例 `docs/adr/` 或 `docs/decisions/`，编号＋slug（`0007-use-postgresql.md`），理由＝与代码同库经 PR 审、版本控制自动跟踪；ADR 工具链（adr-tools/Log4brains）以**编号件不删**为前提。〔来源：ADR Explained／§Where to Store Architecture Decision Records／同上 URL；ADR (Architecture Decision Record) glossary／2026-11-03 检索／§"A superseded ADR is never deleted; the history is the value"／https://www.getlockstep.dev/glossary/adr〕

## A.2 本仓采纳口径（定标结论）

1. **落位＝维持 `.collab/decisions/`，不迁 `docs/`**。理由三条：①裁定三§二点八定义 docs＝「当前存活的干净交接件」，决策记录＝史实锚族（append-only·后生效覆盖先前机理），性质归 `.collab` 侧，迁 docs 违该定义；②门禁现状＝spec-provenance 锚已 6 处指 `.collab/decisions/`（实测 grep：bundle-assembly-registration/SKILL.md:11、multi-collab/SKILL.md:10、object-audit/SKILL.md:10、check-provenance.py:14、object-build/SKILL.md:11、tools/check-source-of-truth.py 指 research 侧），落位一动全链换锚；③业界「与受治对象同库近邻」精神在本报中由「与各项目自己 `.collab` 同域」承接（裁定三§二点六.4：治理记录归各项目自己 `.collab`）。ADR 正件与裁定登记**同桶分族**，不新增子目录（固定结构闭集不扩）。
2. **件体格式＝Nygard 最小骨架＋状态行闭集＋双向互链**（现盘裁定登记件已含「开端 HEAD＋后生效覆盖注记」，天然兼容，只补三字段）：
   - 命名定式：决策登记现式（日期＋标题）保留；架构决策正件加族前缀 `ADR-NNN`（NNN＝三位零填充·项目内单调递增不复用）→ `YYYY-MM-DD-ADR-NNN-<slug>.md`；
   - 头部块必含四行：`- Status：`（闭集＝`Proposed`／`Accepted`／`Rejected`／`Deprecated`／`Superseded by <件路径或ADR号>`）、`- Deciders：`、`- Date：`、`- Author：`＋`- Registrar：`（登记人）两字段分列＝**誊录权与判决作者分离的机读形态**；
   - supersede 程序：新件落盘＋旧件**只改 Status 行一处**＋双向互链（旧件 Status 指新件、新件增 `Supersedes：` 行）；旧件正文其余零触碰（＝本仓「原件不删只作注记」与业界 accepted-immutable 同款，互认不冲突）。
3. **三族分权落盘（定标）**：
   - **决策者裁定登记族**＝登记权＝主理人（誊录权明文；限定「非判决作者」：Registrar≠Deciders 中的决策者时合法，Author 字段记决策者原话出处）——与代笔禁令自洽：禁令禁的是「主理人自造裁决」，誊录登记本就是主理人职权，缺的是**条款明文**（现状＝事实代笔无条款＝本次补上）。
   - **架构决策正件族（ADR）**＝落盘权＝架构席，从 `.collab/drafts/{design,adr}/` 草稿域延伸到 `.collab/decisions/ADR-*` 正式域（席位卡写域与 seat-permissions 数据面随动＝列入后续施工票，本设计件不落改）。草稿→正件语义：draft ADR 无 Status  Accepted 不生效；正件落盘即生效（后生效覆盖先前机理自动接管）。
   - **判词族**＝verdicts.md 既有规范（裁-25/28 五段式＋独立审计席出品）**一字不动**（盘点账⑤确认已规范）。
   - 三族共桶 `.collab/decisions/` 的机械分族判据＝文件名族前缀闭集：裁定登记＝无 ADR 前缀的「皮总裁定/主理人裁定/裁决记录/拍板」系；ADR＝`*ADR-*`；判词＝verdicts.md 单件。
4. **SOP 增节点＝「裁决到达→对应席位落盘→commit」闭环**：handoff-discipline §十一（候裁面闭集＝向上准入）之后补配对条款「§十一之一 裁决落地：裁决队列出列件（皮总裁定/主理人裁定）＝对应席位（裁定登记＝主理人／ADR＝架构席／判词＝独立审计席）在**到达后首笔可写窗口内**落盘 decisions 并单独 commit；落盘前该裁决不具执行效力（票面引用未落盘裁决＝引用方违例）」。此节点同时封掉「拍板后无落盘节点」缺口（盘点账③）。
5. **`.collab/human/deliberations/` 与 `.collab/decisions/` 分工（定标）**：deliberations＝人类席**审议过程面**（讨论稿、 deliberation 记录、质询与答辩——形成裁决前的材料，人类席自有写权，现条款保留）；decisions＝**裁决生效登记面**（闭集三族）。裁决性内容在 deliberations 内出现不具效力，须经上述 §十一之一 程序落 decisions 方生效；反向：decisions 内不写讨论过程（史实锚只收结果＋原话要点）。

## A.3 可机械判定条款草案（供后续施工票引用·本件不落改）

```
E-ADR-1 头块断言（正例 exit 0／负例 exit≠0）：
  `.collab/decisions/` 内文件名匹配 `*ADR-*` 的件，头 12 行内必含
  `^- Status：(Proposed|Accepted|Rejected|Deprecated|Superseded by .+)$`
  且含 `^- Deciders：` `^- Date：YYYY-MM-DD` `^- Author：` `^- Registrar：` 四行。
  python 逐件校验，缺任一行 exit 1。
E-ADR-2 编号唯一与不复用：仓内 `ADR-(\d{3})` 提取集，重复 occurrence>1 exit 1；
  新落盘 ADR 编号必＝既有最大＋1（跳号/复用 exit 1）。
E-ADR-3 supersede 双向：对每个 Status 含 `Superseded by X` 的件，X 件内必含
  `^- Supersedes：` 回链；缺边 exit 1（python 双向图校验）。
E-ADR-4 accepted 不可变（门禁侧）：对 Status∈{Accepted,Rejected,Deprecated,Superseded by *}
  的件，commit diff 白名单＝仅 Status 行＋Supersedes 行＋文末追加注记行；
  其余行入 diff＝BLOCK（git show --name-only＋行级 diff 过滤）。
E-ADR-5 三族分族计数对账：`git ls-files .collab/decisions/` 按族前缀正则分桶
  （ADR／裁定登记／verdicts），三桶和＝总数（桶外件出现＝登记违例读数）。
```

---

# T-B · 归档策略

## B.1 核心争点与业界对照

- **A 案（工作树零归档面，git 承担归档）业界主流依据**：「Since the history is preserved in version control, there is absolutely no reason not to remove code you don't need」＋删除侧推荐「delete and **tag the revisions** where they were deleted（删除时打 tag，死件可原位寻回）」＋归档目录固有弊病「links or relative references will no longer apply」。〔来源：Delete unused source code from the repository or keep an archive folder?／2026-11-03 检索／问题正文＋Thomas Owens 答＋Sergio Velasquez 答／https://softwareengineering.stackexchange.com/questions/289904/delete-unused-source-code-from-the-repository-or-keep-an-archive-folder〕
- **B 案（自建归档面）依据**：删除＝「out of sight out of mind」＋solo/低熟悉度场景 git mv 到 `_archive/`＋归档目录放 README 登记退役日期与替代物，「心理安全网」论。〔来源：Don't Delete, Archive: How I Safely "Retired" Zombie Code with git mv and _archive/／2026-11-03 检索／§The Solution: A Code Graveyard＋§Lessons Learned／https://dev.to/masaoshimadaopen/dont-delete-archive-how-i-safely-retired-zombie-code-with-git-mv-and-archive-53a0〕

## B.2 本仓约束实测（决定性证据）

1. **引用在册依赖重**：票面互引 26 处（`.scratch/tickets/` 内对票文件路径引用 occurrence）；交付面→票面活引用 15 处；**spec-provenance 锚直接指票面件**＝check-collab-lint.py L5/L14/L23 三处 `spec_file: agent-skills/external-advisor-collab/.scratch/tickets/2026-10-30-EAC-SK5-机检票.md`——票面被删＝门禁头块断链（check-provenance 族 BLOCK）。
2. **check-ticket-reconcile 缺省扫描面＝票目录在册件**（现仓 L317；重组后＝`.collab/tickets` 或 `.scratch/tickets` 按裁项②）——票面消失即对账链断（已登记「假绿」危险形态见 T09 输入件 G5）。
3. **git 寻回成本实测**：`git log --follow` 定点查已迁件（DIRRELOC 票）＝**0.15 秒**返回；本仓体量（tracked ~800 件）下寻回零门槛。
4. **裁定三框架约束**：`.collab` 固定结构闭集不含归档桶；仓根白名单不含归档目录——**自建归档面＝规范分叉／白名单违例**，除非皮总临时裁定（§二点六.2「其他公共需要临时决定」）。

## B.3 定标结论＝③分族处置（工作树不建归档目录，git 历史＋tag 承担归档；分族定义移除资格）

1. **永不归档/永不删除族**：`.collab/decisions/` 全部（三族）＋`verdicts.md`——史实锚＋spec 出处（实测 6 处锚），任何批不得删。
2. **docs 族**：不归档——docs＝当前存活面（裁定三§二点八），历史版本被现行件取代时**直接出 docs**；其历史态已由 `.collab` 案卷／git 历史承载（§二点八.2 原文「历史版本/沿革态不进 docs（归 .collab 过程域或归档）」中「归档」一支由本条定标＝归 git 历史，不建物理归档面）。
3. **票面族＝收口后条件式移除**（本仓高频件族，采纳「移除＋tag」而非归档目录）：
   - 票收口（回执被 QA 独立验证收讫）→ 票首行状态标记 `已结案`（现仓 occurrence＝0，即此机制缺位，随后续施工票补）；
   - **移除前置＝引用闭合机械判据**（下 E-ARC-1）：该票路径串在活扫描面（交付面＋decisions＋在册票＋门禁 spec_file 头块）出现＝0 方可 `git rm`；被 spec_file 锚定的票（如 EAC-SK5 机检票）＝**实质不可删**，除非 spec_file 换锚先行；
   - 移除程序：单独 commit `retire:` 前缀＋消息体含 `RETIRE <票ID>`＋移除批打 tag（`archive-<YYYYMMDD>`，SE 主流推荐形态）；寻回程序写一行进票目录 README：`git log --diff-filter=D --grep "RETIRE <票ID>"` 定位删除笔→`git show <笔>^:<旧路径>` 取全文。
4. **出口条件**（对 B.1-B 案的让步口）：若将来单项目未入库过程块（refs/evidence 系）需留存，走仓外归档（先例＝2026-10-27 移出 `D:\multi-agent-collab-archive\`）＝**仓外即归档面**，工作树与 git 皆不背。

```
E-ARC-1 移除资格判据（负例 exit≠0）：
  对待移除票路径 P：grep -rno "$P" deliverables/ .collab/decisions/ .scratch/tickets/ tools/ | grep -v "^$P" | wc -l == 0
  且 grep -rn "spec_file: $P" deliverables/ tools/ == 0；任一非 0 → 移除被拒。
E-ARC-2 移除笔三要素：commit 前缀 `retire:`＋消息含 `RETIRE <票ID>`＋该批 HEAD 有 tag `archive-*`；
  git log --grep 与 git tag --contains 双查，缺项 exit 1。
E-ARC-3 史实锚永存断言：check-provenance 对全部 spec_file∈{decisions,verdicts} 锚件存在性校验
  ＝门禁既有能力，重组/移除批后 GATE PASS 即等价断言（零新构件）。
```

---

# T-C · 组件退役规则

## C.1 业界对照

- **SemVer 退役双拍程序**：deprecation 属正常演化；两动作＝更新文档＋以 **minor** 发布携带弃用标记；**移除前至少有一个携带弃用标记的 minor 版本**，移除落在后续 **major**。〔来源：Semantic Versioning 2.0.0 FAQ＋§7（minor MUST bump when deprecated／major MUST bump for removal）／2026-11-03 检索／https://www.semver.org/；解读件 How should a library deprecate an API? What SemVer says／§The rule／https://safeguard.sh/resources/blog/how-should-a-library-deprecate-an-api-what-semver-says〕
- **弃用通知五要素**：受影响对象名／原因（含安全原因）／替代物及示例／弃用发生版本＋计划移除版本／独立 changelog 分类目（Deprecated/Removed）。〔来源：同上 safeguard 解读＋How do I retire an insecure API…／§"What a good deprecation notice contains"／https://safeguard.sh/resources/blog/deprecate-then-remove-how-to-retire-an-insecure-api-under-semver〕
- **窗口与审计**：弃用与移除两事件分离（RFC 9745 Deprecation header＝「在走」／RFC 8594 Sunset header＝「何时停」）；「deprecation nobody notices is no deprecation」；移除前静态 grep＋运行时观察双半审计找齐调用方。〔来源：API Versioning Best Practices／§Set a Clear Deprecation Timeline＋§Deprecating and Sunsetting Old API Versions／2026-11-03 检索／https://wso2.com/api-platform/learn/api-versioning-best-practices/；内部工具 90 天合同实践／§audit 两半／https://chagdev.com/?p=736〕

## C.2 本仓采纳口径＝退役手续最小闭集（五目）

组件（席位卡／bundle 注册面／废技能／废配置行）退役手续闭集，缺一即退役未完备：

1. **弃用宣告（先行）**：裁定/审票件内点名对象＋原因＋替代物＋移除批指向＝deprecation notice（五要素去「版本号」换「批次/HEAD 锚」）。宣告批与移除批之间**至少间隔一个可写批次**（本仓版 SemVer「至少一个 minor」等价款；紧急安全族除外：fail-closed 即拆＋宣告补记）。
2. **版本账 append-only 追加行**（README 版本账先例形态）：内容含「退役：<对象> 依 <裁定/票ID>」。
3. **注册/配置面同批随动清零**：plugin.json `agents[]`/`members[]`、hooks-map 身份映射、bundle.lock、ARCHITECTURE/PRODUCT 反引号路径——全部在移除批内改毕（跨批残留＝悬空注册窗口，违「static grep 找齐调用方」审计款）。
4. **物理移除＋清零断言**：`git rm`＋引用清零断言（`grep -rno <旧路径族> <活面> == 0`·T07 判据 9 先例形态）。
5. **bump 三同源**（纪律①）：移除批 version bump＋门禁 GATE PASS 对拍。

## C.3 T07 旧五卡退役按此口径复核（只评估不施工）

| 目 | T07 现面 | 判定 |
|---|---|---|
| 1 宣告先行 | 宣告链两段：§20.2③ 退役已生效裁定（史述面先例登记见 T07-B 节头）＋T07 票面（执行票含原因/替代物=新五卡） | **满足**（宣告批→票批有间隔） |
| 2 版本账追加行 | README「出身」节 append-only 追加 v0.1.15 行（T07 甲账.4 规格在案） | **满足**（票面已含规格，施工后核） |
| 3 注册/配置面同批清零 | `.codebuddy-plugin/plugin.json` 注册面＋ARCHITECTURE/PRODUCT 反引号路径随动在 T07 闭集；**hooks-map `agent_type_to_seat` 五行旧卡名移出 T07、归 T08（丙账）** | **缺口点名**：新口径下「配置面随动清零」应同批完成；T07 拆到 T08＝注册残留跨批（T07 候裁③已自觉登记，且现盘实测旧五卡未删、version 仍 0.1.14＝T07 未施工，缺口未成真）。**处置建议**：T07/T08 若同窗施工则并批核销（视同同批）；若分窗，T07 回执须登记残留窗口读数＋T08 回执核销，两笔闭环即符合本目 |
| 4 物理移除＋清零断言 | 判据 6（agents 目录五件清零）＋判据 9（旧卡路径引用 11→0） | **满足** |
| 5 bump 三同源 | 判据 10（三处 0.1.14→0.1.15） | **满足** |

**结论**：T07 手续 5/5 齐备，唯第 3 目跨批残留一项——按 C.2 第 3 目处置建议闭环即可，不需改票。

```
E-RET-1 退役手续核表（机械侧）：对每个退役对象，四查——
  (a) 宣告件存在（grep `退役|清退` +对象名 in .collab/decisions|tickets）；
  (b) 版本账行存在（README grep `退役：<对象>`）；
  (c) 旧路径族引用清零（活面 grep occurrence==0）；
  (d) version bump 读数三同源。
  任一缺→退役未完备读数入回执（advisory 起步，转 BLOCK 属门禁路由表裁量）。
```

---

## 候裁/呈报节（真无法收敛项·仅一项）

- **固定结构闭集与 ADR 同桶假设**：本件按「decisions 桶内文件名分族」实现三族分权，未新增 `.collab/decisions/adr/` 子目录（保守兼容裁定三闭集）。若 `.collab` 固定结构闭集定义（架构席另持有规范实施权）最终名录含 adr 子桶，本件落位条款只需把「同桶分族」换「子桶」，其余（状态机/分权/落盘程序/判据）零动。此为规范实施细节自裁范围，列此仅备双席审票知悉，不属上呈。

## 四、引用账（四件套·集中登记）

| # | 来源文件 | 日期 | 条款位置 | URL |
|---|---|---|---|---|
| 1 | Architecture Decision Records (ADR) Explained: A Complete Guide | 2026-11-03 检索 | §Status Lifecycle／§Common Mistakes（accepted immutable）／§Where to Store（docs/adr＋编号惯例） | https://vickybytes.com/blog/architecture-decision-records-explained |
| 2 | MADR 模板实战指南（译介＋adr.github.io/madr 真源指向） | 2026-11-03 检索 | §元数据头 Status 闭集／§八 supersession 双向流程 | https://blog.csdn.net/gitblog_00602/article/details/161209131 |
| 3 | Architecture Decision Records Written by Your Coding Agent（引 Nygard 2011＋adr.github.io 定义） | 2026-11-03 检索 | §What an architecture decision record is（编号不复用／superseded 留档语义） | https://nimbalyst.com/blog/architecture-decision-records-written-by-your-coding-agent |
| 4 | ADR (Architecture Decision Record) — Lockstep glossary | 2026-11-03 检索 | §The standard format（"superseded ADR is never deleted"） | https://www.getlockstep.dev/glossary/adr |
| 5 | Delete unused source code… or keep an archive folder? — Software Engineering SE | 2026-11-03 检索 | 问题正文＋Thomas Owens 答（delete＋tag）＋Sergio Velasquez 答（archive 断链弊病） | https://softwareengineering.stackexchange.com/questions/289904/delete-unused-source-code-from-the-repository-or-keep-an-archive-folder |
| 6 | Don't Delete, Archive: …git mv and _archive/ — DEV Community | 2026-11-03 检索 | §Code Graveyard 程序＋README 登记款 | https://dev.to/masaoshimadaopen/dont-delete-archive-how-i-safely-retired-zombie-code-with-git-mv-and-archive-53a0 |
| 7 | Semantic Versioning 2.0.0 | 2026-11-03 检索 | §7（deprecation→minor bump）＋FAQ（移除前至少一 minor 携带弃用） | https://www.semver.org/ |
| 8 | How should a library deprecate an API? What SemVer says — Safeguard | 2026-11-03 检索 | §The rule／§What a good deprecation notice contains（五要素） | https://safeguard.sh/resources/blog/how-should-a-library-deprecate-an-api-what-semver-says |
| 9 | API Versioning Best Practices — WSO2 | 2026-11-03 检索 | §Set a Clear Deprecation Timeline（RFC 9745/8594 两信号分立） | https://wso2.com/api-platform/learn/api-versioning-best-practices/ |
| 10 | Sunset Banners Beat Surprise Breakage（90-day contract·内部工具审计两半） | 2026-11-03 检索 | §Audit: find every callers（静态＋运行时双半） | https://chagdev.com/?p=736 |

## 五、回执（起草笔）

- 开端 HEAD 实测＝`b003a0e`；起草前 `git status --porcelain` 读数登记；本笔单独 commit（`collab:` 前缀·只含声明闭集 1 件）；禁 `--no-verify`、禁 amend；门禁拦截如实报告不绕闸。
- 三题结论一句话：T-A＝decisions 桶内三族分权（裁定登记誊录权主理人明文＋ADR 正件架构席落盘＋判词不动），Nygard 状态行＋编号＋supersede 双向不改写，SOP 补「裁决到达→席位落盘→commit」闭环；T-B＝不建归档目录，git 历史＋retire commit＋tag 承担归档，分族定移除资格（decisions 永不删、票面收口后引用闭合机械判据放行移除）；T-C＝退役手续五目闭集，T07 复核 5/5 齐备唯 hooks-map 跨批残留一项按并批/两笔闭环处置。
