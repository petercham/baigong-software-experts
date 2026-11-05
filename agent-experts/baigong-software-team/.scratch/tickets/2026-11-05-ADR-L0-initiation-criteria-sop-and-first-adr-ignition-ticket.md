# ADR-L0 ADR 立项触发判据入 SOP＋首支 ADR 同批点火施工票（架构席起草·落改按 S 节分席）

- 开端读数：devkits HEAD 以本票 commit 实测为准；开票侧实测 `git rev-parse --short HEAD`＝`138e39a`（main），`git status --porcelain` 本席名下净（他席在途 untracked 件不入本票）。
- 背景（决策依据·自包含）：ADR 工序链已成文生效（工序五段节在位 `skills/software-orchestration/references/standard-sop.md` L50-60），但工序只有「怎么写」无「何时写」——ADR 工序票全文 grep「触发」5 处全为挂载时序语义，零立项线（架构席调研取证 `.collab/research/2026-11-05-ADR触发判据与首支死结-架构席调研-v2.md`＝c4ae3e3）。同时首支 ADR 与触发批互为前提成死结：ES2 收口双前置①「首支 ADR 实际落 docs/adr」②「触发批同批实装挂载与校验器」（`.scratch/tickets/2026-11-04-SWB-ADR-process-ticket.md` L15/L127），无判据则无触发批，无首支则双前置永不触发，docs/adr 永不存在。决策者（2026-11-05 16:55）已裁＝**案 a：判据成文批＝触发批**——判据本体命中工序链改动信号，按判据自身立首支 ADR（拟号 0001），同批完成 docs/adr 初始化＋60-gates 挂载＋E-ADR 校验器实装＝双前置①②合法闭合。E-ADR 族机理条款真源＝ES 定标面 v2/v3/v3.1 终态（`.collab/design/2026-11-03-devkits-engstd-adr-archive-retirement-v2.md` A.3＋v3.1 三修点：E-ADR-2 升 ‴ 四位正断言／E-ADR-5 升 ‴ 桶互斥＋和式／E-ADR-4 注记引用式三式闭集）；编号形态定案＝**四位 NNNN**（`^(\d{4})-` 文件名正断言，v3.1 黄-1/黄-3 已消历史三位制不自洽；架构卡/STRUCTURE/SOP「编号四位」与之一致）。
- HOLD：无。
- 改动面闭集＝15 件：（闭集外零触碰；写入席位按 S 节标注，混席件＝无）
- 声明闭集：
  - agent-experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md
  - agent-experts/baigong-software-team/skills/software-orchestration/SKILL.md
  - agent-experts/baigong-software-team/docs/adr/0001-adr-initiation-trigger-criteria.md
  - agent-skills/object-audit/references/50-document.md
  - agent-skills/object-audit/scripts/check-adr.py
  - agent-skills/object-audit/scripts/run-gates.sh
  - agent-skills/object-audit/SKILL.md
  - agent-skills/object-audit/references/90-changelog.md
  - agent-skills/multi-collab/references/60-gates.md
  - agent-skills/multi-collab/SKILL.md
  - agent-skills/multi-collab/references/90-changelog.md
  - agent-experts/baigong-software-team/README.md
  - agent-experts/baigong-software-team/plugin.json
  - agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json
  - agent-experts/baigong-software-team/bundle.lock

开票侧实体核验：闭集内除 `docs/adr/0001-…`（本票新建＝点火件）外 14 件 `git ls-files` 实测在位（138e39a）。三同源现值实测：plugin.json L3／.codebuddy-plugin/plugin.json L3／bundle.lock L5 均＝`0.1.25`；software-orchestration SKILL.md L5＝`1.1.5`；object-audit SKILL.md L6＝`0.8`；multi-collab SKILL.md L5＝`4.10`。E-ADR-5‴ 对账现盘基线（bundle 根锚）：桶1（docs/adr）＝0／桶2（bundle `.collab/decisions/` 排除 verdicts.md）＝19／桶3（verdicts.md）＝1／和式＝`git ls-files docs/adr/ .collab/decisions/`＝20 ✓（0+19+1＝20）。

回执落点＝`.collab/receipts/2026-11-05-ADR-L0-工程师回执-v1.md`（文件名级回执指针行）。

## §口径（判据定义·票内自包含）

1. **OA-T1 日期纪律（上次 TMP-DISC 教训前置）**：凡落交付面的定稿文本，日期一律①全角括注内②反引号段内③`YYYY-MM-DD` 模板形态三种载体之一；开票侧已按 check-entity 真判据链（mask_non_narrative＋in_fullwidth_paren）对七类样本行预跑＝裸日期全零（读数见自检节）。ADR 头块 `Date：` 行**必须反引号包裹日期**（`- Date：\`YYYY-MM-DD\``）——理由＝docs/adr 在 check-entity 扫描面（agent-experts/**）且 OA-T1 per_spec=block，裸日期必拦；反引号遮除＝check-entity 既有口径（「反引号段内日期不算裸写」），E-ADR-1″ 校验器实现须在遮反引号后匹配 Date 行（匹配语义不变＝协议强制日期载体合法）。
2. **工序链归位**：ADR-0001 正文终稿＝四方收口草案（`.collab/drafts/adr/`＝架构席既有写域）→产品席＋QA席＋架构席会签→架构席终写＝逐字照录收口草案（条款甲·哈希对等）。**本票只定 ADR-0001 草案骨架（S4），终稿文本＝会签后收口草案，不由本票钉死**；会签路由归主理人，起草席不自行会签。
3. **「同批」解释**：ES2 双前置②「触发批同批实装」＝同票不同 commit 合法——机部件先过门（check-adr 对空 docs/adr 全断言真空真＝不炸门），终写笔随后（S4→S5 链序见执行序节）。
4. 行号锚＝138e39a 读数；施工以 pattern 命中为准，实测与票面预期冲突按实测登记上报（H6）。

## S1 standard-sop ADR 工序节增判据款（工程师·逐字）

`agent-experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md`：「## ADR 工序（决策记录链）」节第 5 款（supersede 归道段）之后追加第 6 款，逐字照录：

```
6. **立项触发判据（ADR 工序入口闸）**：
   入线（命中任一＝该决策应立 ADR，走决策记录链）：
   - T1 真源形态改动：改变任一纪律/配置/条款的「唯一真源」载体或形态（哪卷哪桶哪 config 承载何规则）。
   - T2 文件域结构改动：改变目录布局、写域结构、落位规则或三层文件域边界（含 `.scratch` 落位、docs/adr 落位、仓根分层）。
   - T3 席位职权改动：改变「谁有权动什么」（写权/拒权/会签设计/工序签核面的新增或换代）。
   - T4 工序链本体改动：新增/退役/换代工序环节、票型、门禁挂载机制或签字面。
   不入线（命中且入线零命中＝留 decisions 级，不立 ADR）：
   - N1 案内程序裁定：单票射程内的放行/候裁落拍/豁免注记/审票修单处置。
   - N2 一次性执行处置：换钉、装配、迁移、清理、解冻等随批耗尽的批处置。
   - N3 口径数字微调：阈值数值、排程、估算界差等无结构语义的调整。
   混合件＝拆分处理：一件决策同时含入线与不入线要素时，ADR 只誊入线句（附 decisions 原件路径引用，不复写正文），原件 append-only 不动。
   覆盖链：新口径覆盖旧口径＝终态案立 ADR、旧案留 decisions 史实不回改，ADR 头块标取代关系（E-ADR supersede 双向互链机理）。
   申诉线：席位对初筛结果有异议＝候裁呈报，不现场改判据；初筛可机械＝对 decisions 登记件按入线四词 grep 出候选清单，终判归会签三席。
```

- 验收＝A1。

## S2 SKILL.md 索引随动（工程师）

`skills/software-orchestration/SKILL.md`：
1. L5 `version: 1.1.5` → `version: 1.1.6`；
2. description 触发词尾部「…清理判据、零残留。」→「…清理判据、零残留、ADR立项、触发判据。」；
3. references 索引表 standard-sop 行内容列「标准 SOP 逐步流程全节（五席逐步派单细则·PRD 两型·IS_PASS 与智能路由流转）」→「标准 SOP 逐步流程全节（五席逐步派单细则·PRD 两型·IS_PASS 与智能路由流转·ADR 工序与立项触发判据）」；「何时必读」列零动。
- 验收＝A5。

## S3 E-ADR 校验器实装＋条款落交付面＋门禁挂载（工程师·涉脚本面全规格）

### S3a 条款文本落交付面（spec_file 锚目标）

`agent-skills/object-audit/references/50-document.md` 文末（「## 判定要点」节之前）新增一节「## E-ADR ADR 族机检断言（docs/adr 面）」，正文＝ES 定标终态五款逐字迁入：E-ADR-1″（头块断言·适用面 `docs/adr/*.md`·头 12 行必含 Status/Deciders/Date/Author/Registrar 五行·Status 闭集；Date 行匹配口径注＝日期可反引号包裹载体，校验器遮反引号后匹配·§口径1 同旨）、E-ADR-2‴（文件名正断言 `^(\d{4})-[A-Za-z0-9._-]+\.md$`＋提取集唯一＋新号＝最大＋1，v3.1 黄-1 全文）、E-ADR-3″（双向 supersede 全向校验＋adr 内 `.collab/…` 活引用存在性补偿断言 advisory 起步，v3 文本）、E-ADR-4″（适用域 docs/adr 族限定＋diff 白名单＝Status 行＋Supersedes 行＋文末追加注记行＋注记引用式三式闭集 `^\d{4}-`∪`ADR-\d{3}`∪案件路径，v3.1 黄-3 全文）、E-ADR-5‴（三面对账：桶1 `git ls-files docs/adr/` 逐名在盘／桶2 bundle `.collab/decisions/` 逐名排除 `decisions/verdicts\.md$`／桶3 verdicts.md 单件／和式断言＋`D docs/adr/`∪`D .collab/decisions/` 删除行 BLOCK，v3.1 黄-2 全文）。文本内日期只准 `YYYY-MM-DD` 模板形态（OA-T1 安全）。逐字真源＝`.collab/design/…v2.md` A.3＋v3.md §一-B＋v3.1.md 三修点（施工侧按该三件终态段逐字誊入，冲突以 v3.1> v3 > v2 后生效序）。

### S3b 校验器新件

`agent-skills/object-audit/scripts/check-adr.py`（新建）：
- 项目根锚＝自脚本位置上溯首个含 `docs/STRUCTURE.md` 目录（write-guard.py L49-58 同款探针）；缺省＝baigong bundle 根；`--root` 覆写面在册；
- 实现 E-ADR-1″/2‴/3″/4″/5‴ 五断言，输出格式循族件惯例（`<file>:<line>: <SEV> <spec_id> <msg>`），缺边/缺行/跳号/复用/和式不符＝exit 1；
- **E-ADR-5‴ 和式扫描根声明**＝bundle 根；仓根 `.collab/decisions/`（治理层搬家批所设七件面）**不在 E-ADR-5‴ 射程**——ES 文本先于该面出现而生，射程漂移开票侧已上报（红-1），本票按原文射程实装不扩面，漂移处置候裁（见候裁3）；
- E-ADR-4″ diff 白名单实现＝pre-commit 上下文取 `git diff --cached -- docs/adr/`（非提交上下文跳过并在 coverage 行申报「E-ADR-4″ 本次未执行」＝族件「未执行判据不得计绿」口径）；
- 头块必带 spec-provenance 五行块（spec_file 指 S3a 新节·spec_anchor 按五断言各条）；
- 只读铁律：本件不写任何文件。

### S3c 门禁挂载

1. `agent-skills/object-audit/scripts/run-gates.sh` L136 `SCRIPTS=` 行尾追加 ` check-adr`（行级一行改，其余零动）；
2. `agent-skills/multi-collab/references/60-gates.md` 路由表两处：①`per_spec` JSON 块 `"OA-D6-5": {"commit": "advisory"}` 行后补五行（`E-ADR-1″`…`E-ADR-5‴` 全部 `{"commit": "advisory"}`，注意前一行补逗号＝JSON 合法）；②路由表说明段（L104-105 式例行）尾追加五行（spec 名｜advisory｜条款真源＝`object-audit/references/50-document.md` E-ADR 节 X 行｜**足**（首挂 advisory＝放行裁定候裁③既有射程；升 block 候实跑零误报读数入 evidence 后另拍））。挂载严重度授权＝ADR 工序放行裁定候裁③既批射程，不新触发 L0 闸。

### S3d 版本账随动（跨包两件）

- `agent-skills/object-audit/SKILL.md` L6 `version: 0.8` → `0.9`；`agent-skills/object-audit/references/90-changelog.md` 文末追加一行（v0.9（2026-11-05·ADR-L0 批）＝E-ADR 五断言落 50-document 新节＋check-adr.py 实装＋run-gates 挂名；日期括注内）；
- `agent-skills/multi-collab/SKILL.md` L5 `version: 4.10` → `4.11`；`agent-skills/multi-collab/references/90-changelog.md` 文末追加一行（v4.11（2026-11-05·ADR-L0 批·60-gates 五行进表首挂 advisory）；先例＝v4.10 两 spec 进表同形制）。
- 验收＝A2＋A3＋A4。

## S4 ADR-0001 首支（草案→会签→终写·分席）

1. **草案**（架构席·`.collab/drafts/adr/0001-adr-initiation-trigger-criteria-draft.md`＝既有写域零新开）：骨架定稿约束——
   - 文件名/终写落位＝`docs/adr/0001-adr-initiation-trigger-criteria.md`（NNNN 四位制）；
   - 头块五行（前 12 行内·逐字形态）：`- Status：Accepted`／`- Deciders：皮总（案 a 裁定）＋产品席＋QA席＋架构席会签`／``- Date：`2026-11-05```（反引号包裹＝§口径1）／`- Author：架构席（起草）`／`- Registrar：主理人（誊录）`；＋`- Supersedes：` 行**缺省不设**（首支无取代对象，E-ADR-3″ 真空真）；
   - 正文骨架四段（Nygard）：背景（死结链＝本票背景节可引 `.collab/research/…v2.md` 与工序票 L15/L127 锚）／决策（案 a＋判据四款 T1-T4/N1-N3＋三辅线全文＝S1 同款文本）／后果（工序入口闸生效／ES2 双前置闭合／历史件处置案乙若签则随附）／自指合法性注记段（本 ADR 记录对象＝立项判据自身＝按判据 T4 命中而立，自证点＝判据辖运行时决策不辖记录件自身形态，会签三席对此段逐席表态）；
   - 文本内日期一律括注/反引号载体（§口径1）。
2. **会签**：草案成笔后 SendMessage 主理人→主理人路由产品席＋QA席独立会签（各席保留项走工序链 §2 归位）→四方收口草案固化（哈希登记）。
3. **终写**（架构席·独立 commit·租约经 B2 按本票签发 path_globs＝docs/adr/）：逐字照录收口草案入 `docs/adr/0001-adr-initiation-trigger-criteria.md`；终写件与收口草案正文哈希对等方可落盘（条款甲）。
- 验收＝A4＋A6。

## S5 bundle 版本随动（工程师）

- 三同源 `0.1.25` → `0.1.26`（plugin.json L3／.codebuddy-plugin/plugin.json L3／bundle.lock L5，现值实测 0.1.25 如开票侧读数）；
- `agent-experts/baigong-software-team/README.md` 版本账块追加一行（插 v0.1.25 行后）：`- **版本账 v0.1.26**（2026-11-05·ADR-L0 判据成文＋首支点火批）：standard-sop ADR 工序节增第 6 款立项触发判据（T1-T4 入线/N1-N3 不入线＋混合拆分/覆盖链/申诉线）＋SKILL 索引触发词随动 1.1.5→1.1.6＋ADR-0001 首支落 docs/adr/（案 a 自指点火·ES2 双前置①②闭合）＋跨包随动（object-audit 0.8→0.9 E-ADR 五断言实装挂线／multi-collab 4.10→4.11 五 spec 进路由表）。三同源 0.1.25→0.1.26（纪律①每变必 bump·三同源）。`
- 验收＝A5。

## 执行序（防炸门·链内固定）

①工程师 S1＋S2＋S3a-d（机件与条款面·此笔时 docs/adr 尚未存在＝check-adr 真空真过门）→②架构席 S4 草案笔→③主理人路由会签链→④架构席 S4 终写笔（独立 commit·租约）→⑤工程师 S5 bundle 版本笔→⑥回执笔。②-④不入工程师闭集执行段；S5 可在④前后但终态读数含 ADR-0001。

## 禁动面

- 五席位卡全部（ADR 工序纪律行 L24/L25 等 ES 批所设＝已在本位，零动）；`config/seat-permissions*.json`（architect docs/adr 写权行 ES 批已在位）；
- 两基线副本（product/architecture-v2.9-copy.md）一字不碰；交接件 v2.9 原件（文末追加区零新增）；
- `.collab/decisions/` 全部史实件（含案 a 裁定登记件＝主理人誊录权面，本票不代笔）；`verdicts.md`；
- `docs/STRUCTURE.md`（docs/adr 条目 L11 ES 批已在位＝本票后声明与实态对齐，无需改）；
- E-ADR 族既有 design 三件（v1/v2/v3/v3.1 原件 append-only 不动）；`check-entity.py`（§口径1 用既有遮除口径，不扩豁免不触该件）；
- 各脚本功能逻辑（除 S3b 新建件与 S3c run-gates 一行）。

## 验收判据（可机械·occurrence 钉值·前后读数附回执·F7）

- **A0**：开工 HEAD＋`git status` 净读数；run-gates 基线 GATE PASS＋发现数读数；check-adr 不存时缺件不拦（挂线前基线）；
- **A1 判据款在位**：`grep -c "^6\. \*\*立项触发判据" standard-sop.md`＝**1**；四入线锚句（T1 真源形态改动／T2 文件域结构改动／T3 席位职权改动／T4 工序链本体改动）各＝1；三不入线锚句各＝1；三辅线（混合件＝拆分处理／覆盖链／申诉线）各＝1；
- **A2 校验器行为**：`python agent-skills/object-audit/scripts/check-adr.py --root <bundle根>` 对终态 docs/adr＝exit 0；**负例族（.scratch 内临时构型·批毕即删·附读数）**＝(a) 文件名 `01-three-digit.md`→E-ADR-2‴ exit1；(b) 头块缺 Registrar 行→E-ADR-1″ exit1；(c) Status 行裸日期未包反引号→对 check-entity 单独跑＝OA-T1 BLOCK 命中（证 §口径1 必要性）；(d) 造 Status＝`Superseded by 不存在的件`→E-ADR-3″ exit1；(e) 桶2 塞 `verdicts.md` 入和式双计复算＝排除式生效（grep -v 命中 0）；
- **A3 门禁挂载**：run-gates 重跑 GATE PASS exit 0（发现数不新增 BLOCK/WATCH 族＝对拍读数）；`grep -c '"E-ADR' 60-gates.md`＝**5**；路由说明段 E-ADR 行＝5；60-gates JSON 块 `python -c "json.load"` 合法性 exit 0；
- **A4 ADR-0001 在位与哈希对等**：`git ls-files docs/adr/`＝1 件·文件名匹配 `^0001-`；终写件正文 sha256＝收口草案登记哈希（回执附两值）；头 12 行 grep 五行各＝1；
- **A5 版本随动**：三同源＝`0.1.26`（前后各附）；SKILL 1.1.6／object-audit 0.9／multi-collab 4.11（前后各附）；README 版本账 v0.1.26 行＝1；两包 changelog 新行各＝1；
- **A6 OA-T1 零新增**：check-entity 终面跑＝OA-T1 命中不新增（施工前后各附·docs/adr 新件零命中＝反引号/括注载体全生效）；
- **A7 E-ADR-5‴ 和式**：终态桶1＝1·桶2＝19·桶3＝1·和式＝21（前后读数各附；若会签链致 decisions 增件则按实测登记）。

## 自检与回执（N4 附载体）

- 开票侧预跑读数（本票成文前已跑·check-entity 真判据链七样本）：SOP 第 6 款行（无日期）＝裸 0／ADR 头块反引号 Date＝裸 0／括注日期行＝裸 0／裸日期对照样本＝命中 1（证判据链有效）／README 版本账行（括注）＝裸 0／`YYYY-MM-DD` 模板行＝裸 0／changelog 括注行＝裸 0；
- 声明闭集 15 件＝改动闭集上限（工程师段 13 件＋架构席终写段 2 件：ADR-0001＋其草稿不落闭集＝草稿域既有写域过程件）；闭集外零触碰；
- F11 终式禁列过程痕迹自检照跑，三分账登记；
- 回执落 `.collab/receipts/2026-11-05-ADR-L0-工程师回执-v1.md`（工程师段）＋终写段读数由架构席回执随终写笔或独立微笔（前缀 collab:）；
- 清理判据（TMP-DISC §八 自示范）：负例构型与任何预跑模拟面＝`.scratch/adr-l0/` 内作业，批毕删除＋读数；收口 `git status` 净＋盘根/系统 Temp 零新建抽查（A8 同款）。

## 候裁单列

1. **历史 decisions 处置案乙**（adr-candidate 标记行＋ADR-CANDIDATES.md 名册件）：架构席建议案（调研 v1 §1.3）——是否随本批/另批落，候决策者拍＋会签确认；本票**不径行**。
2. **TMP-DISC 四款口径＝拟第二支 ADR**（ADR-0002·T2 命中·原件＝TMP-DISC 票面背景节＋收口件）：立项走 S1 判据＋工序链，落位候会签与决策者示意确认；本票不启动。
3. **E-ADR-5‴ 射程漂移**（红-1 随票处置向）：仓根 `.collab/decisions/`（七件治理层）不在 ES 原文射程（ES 先于该面而生）——选项＝维持原文射程（本票现案）／扩两桶对账（另微票）；候裁不现场扩。
4. **check-adr 升 block 时点**：五 spec 首挂 advisory（族例＝零误报读数入 evidence 后另拍）；不在本票。

## 红线

- 只动声明闭集 15 件；混席段（S4）按席位归属执行，工程师不入终写段、架构席不入机件段；
- 定稿句有异议＝停手上报（判据四款＋三辅线文本＝决策者裁案 a 所定调研 v2 成文，不得改写）；
- ADR-0001 会签实体不经本席自签——草案成笔即交主理人路由；
- append-only：不改本票既有行；实测与预期冲突按实测登记（H6）。
