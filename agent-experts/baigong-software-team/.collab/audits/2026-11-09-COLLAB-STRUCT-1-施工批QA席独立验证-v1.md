# COLLAB-STRUCT-1 施工批 QA 席独立验证判词 v1（fresh eyes·九判据独立实跑）

- 席位：QA（qa-struct-c1v）｜性质：施工批独立验证判词（票级验收结论面）
- 开工开端实测：date＝`Mon Nov  9 13:07:09 2026`／`git rev-parse HEAD`＝`11d5fc0`（开工时点）／tracked 面净（untracked 全为各案取证面照登不碰）
- 被核链段（is-ancestor 逐笔实查全 exit 0）：开工锚 `0a4249a` → 施工笔 `e49977a`（251 R100＋14 M＋25 A）→ 补齐续笔 `d616b77`（恰 20 件旧路径 D 面）→ 回执笔 `9f265fe`（恰回执一件）。链上夹他案笔 `9db7f92`/`a9908e5`/`5ee503a`/`c0b0d86`（FUXI 线）照登不碰；QA 验证期间链上新增他案笔 `c38fccd`（FUXI-FX-U28 A 面条款笔·M＝agent-skills/fuxi-skill/.collab/README.md）照登——判词落笔时 HEAD＝`c38fccd`，被核面读数以 `9f265fe` 终点复跑为准。
- 唯一依据票面：`agent-experts/baigong-software-team/.scratch/tickets/2026-11-09-COLLAB-STRUCT-1-施工分票-v1.1.md`——blob 复算＝`58b52f0ab08f…`（303dcec 树值与盘上件 hash-object 全等）；sha256 前 12＝`8005e7f6…` 与回执申报全等；全文直读完毕。
- 工程师取证区 `agent-experts/baigong-software-team/.scratch/COLLAB-STRUCT-1/` 全程禁读；回执件读数只作对照禁采信；一切判据独立实跑（含 `0a4249a`/`d616b77` 两个干净 worktree 对拍，居仓根 `.scratch/COLLAB-STRUCT-1-qa/` 不 commit）。

## 总判：绿（九判据全绿·红 0·黄 1）＝建议放行

## 九判据逐项读数（全部独立实跑）

**判据 1＝绿**：两 config `python -m json.tool` 均 exit 0；两文件五席（host/product/architect/qa/engineer）`deny_globs` 数组逐席全等（程序化逐项对比，非目测）。A1 十处行级替换逐处独立断言：A1-1 product 写域＝「.collab/drafts/」＋「.collab/product/」恰两值 PASS；A1-2 product deny 删二并入一（新面 `.collab/adr/**` 恰一处、「.collab/audits/**」在位）PASS；A1-3 architect 写域头两段换代＋「docs/adr/」删净＋「docs/STRUCTURE.md」保留 PASS；A1-4/A1-5 qa 写域尾段换代＋deny 删三并入一 PASS；A1-6/A1-7 engineer 写域尾段＋deny「.collab/audits/**」恰一处且「.collab/qa/**」删净 PASS；A1-8 note 三处随动（十七桶在两处、十一桶零、drafts/deploy 零）PASS；A1-9 枚举款「B1-D·十七桶」PASS；A1-10 host 写域尾追加恰〔.collab/adr/、docs/adr/〕＋deny 新短语逐字 PASS。注：deny 新项实装为 `.collab/adr/**` 带星形双星，票面成文为 `.collab/adr/` 简写——与本行既有 deny 项风格（全带 `/**`）一致，判读作忠实实现随注不判偏。

**判据 2＝绿**：三面 drafts 子包废止零命中（grep exit 1＝0 行，基线 13 行清零）；config 面旧字样「collab/qa」零命中（exit 1）；「十一桶」在用面零——config＋包内 README＋collab-fixed-structure＋五卡四锚现值全 0（对照 `0a4249a` 同锚恰为票面所载现值 4 行）；残余「十一桶」全部在历史案卷与六外包面＝禁动面照登。

**判据 3＝绿**：全仓 qa 终值公式两读数相等——`git ls-files | grep -c` qa 面＝**53** ＝ fuxi 51＋EAC 2（两桶 `wc -l` 和）；主理人独立复跑读数 53 与本部全咬。audits 两桶＝仓根 **10**／包内 **244**（244＝迁入 234＋开工既有 10；开工既有现值 10 与票面登记钉 6 的差为链上向前进落件漂移，票面「开工复点为准不锁死」覆盖照登）；adr tracked＝**4**；architect tracked＝**1**（≥1）；ledger 三文件 tracked 在册；仓根 `.collab/` 根面旧散件＝**0**（根面唯一直系文件＝新建 README 本体，属 add 面非散件）；decisions 直系＝**79**＝58（开工锚实数）＋20（归位）＋他案 1（`9db7f92` 移交工单 v2 照登）。开工锚五桶实数独立复得：仓根 qa 10／包内 qa 234／仓根 audits 0／包内 audits 10／fuxi 51／EAC 2／decisions 58——全部与公式咬合。

**判据 4＝绿**：`git show --name-status e49977a`＝**251 R 全 R100**（非 R100 零条）＋14 M＋25 A；R 行按源桶分解＝仓根 qa 10＋包内 qa 234＋drafts/adr 4＋票族 3＝251＝开工复点两桶和（10＋234）＋4＋3 对钉。**跨笔检测＝本判据核心实跑**：`d616b77` 20 件旧路径 D 面与 `e49977a` 新路径 A 面逐 20 件 blob sha 程序化配对（`d616b77^:旧路径` vs `e49977a:新路径`）＝**20/20 全等·零失配**＝mv 全程内容等价坐实；链合计 `0a4249a..9f265fe` R 行＝**271**＝244＋4＋3＋20 对钉。防嵌套两式 `grep -c "/qa/"`＝**0/0**。adr 四件 blob 双点（`0a4249a:旧` vs `e49977a:新`）四件全等。

**判据 5＝绿（差值全归因·唯一新增 BLOCK 复核属实）**：形制＝干净 worktree 同形态两读数对拍（本部自建 `0a4249a` 与 `d616b77` 两 worktree，非采信工程师读数）——基线 6,899 条 vs 施工后 7,016 条＝**净差 +117**，与工程师申报 worktree 差 +117 恰等（对照咬合，非采信）。两态 run-gates 均 GATE BLOCK 唯一原因＝check-source-of-truth exit 2「包目录不存在：../multi-agent-collab-experts/workbuddy/baigong-video-team」——基线态同因存在＝环境邻仓缺失非本批产物、两态同型不翻红；主盘 HEAD 实跑 run-gates **GATE PASS exit 0**（发现 151,180 条·主盘形制含 agent-skills 在途取证副本，与工程师申报主盘 32,442→33,429 形制射程不同量级属形制差非盘面差，照登不比数）。差值逐条归因（源路径换代归一后新增 151／消解 34／净 +117；其中新增 BLOCK 96 条逐条归类零漏网）：三族旧字样悬空 49（`.collab/qa/` 旧字面 21＋drafts/adr 旧字面 3＋仓根散件旧路径 24＋tmp-w7-msg.txt 1）＋票族三件 B8 迁移后历史审票件短式指针解析落空 42（mv 机械后果·旧文不追改射程）＋**新 BLOCK 恰 1 枚**（下述）；新增 WATCH 55 条全为 mv 后源路径随动再发；消解 34 条含仓根 README 新建消解旧悬空 18 枚＋architect 卡旧句悬空消解 1 枚。工程师回执「新文案面 19 条」目测数与本部逐条分解口径不可精确复现（见黄-1）。**新 BLOCK 独立复核属实**：`agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md:31` 住址行 `agent-experts/baigong-software-team/docs/STRUCTURE.md` 短式「docs/STRUCTURE.md」解析悬空 BLOCK——`--target` 靶检实跑复现、目标实体实存（盘上件在位）＝解析射程缺口非真悬空；**唯一性坐实**＝对 13 个 A/B 面改件逐一 `--target` 靶检仅命中此 1 枚（开工锚同面靶检＝旧 architect 卡 1 枚已消解）。与 FUXI-U28（链上票 `5ee503a`）修法同题确认＝短式指针候选层缺口同族；随注一点＝全仓「docs/STRUCTURE.md」后缀命中 7 份（七包各一），U28 后缀唯一命中归位层对本枚亦多义不消解，与票面住址行「逐字不得改写」条款构成条款内冲突，从逐字登记在册处置正确（该枚走 OA-D6 advisory 路由不拦提交＝主盘 GATE PASS 实证）。

**判据 6＝绿**：注入形制 `T06_TMP=<仓外Temp> bash` 两态实跑——drill-05 基线 exit 1 红因「RED: deny 原因非 freeze 联动」vs 施工后 exit 1 同文案红因＝同型不恶化；drill-06 基线 exit 1 红因「负扫面命中读数缺位＋replay-dirty.json FileNotFoundError」vs 施工后 exit 1 同型；s2 夹具两态均 exit 0 不变。B6 三件路径随动读检：三文件 drafts 旧子包字样现值 0（grep exit 1）、新文案全部 `.collab/drafts/` 顶层形制在册。缺陷台账在册面（`.collab/defects/2026-11-08-drill夹具回读编码失配与缺件引用缺陷-v1.md`）禁动面 diff 空。

**判据 7＝绿**：`python agent-skills/object-audit/scripts/check-adr.py --bundle-root agent-experts/baigong-software-team` 独立实跑 exit **0**／读数 `docs/adr 盘上件=1｜桶1=1 桶2=20 桶3=1` 与钉值同值；裸跑形态不入判据照登。

**判据 8＝绿**：standard-sop「架构席终写」现值 **0**（开工锚现值 1→0）；architect 卡「docs/adr」现值 **0**（开工现值 2→0·写权句删净）；「可写内容：设计、ADR」行现值 **0**（新行「可写内容：设计、开发票、边界约束」逐字在位）；lead 卡旧路由行现值 **0**＋新行「ADR 文书…software-team-lead（本席）」命中 **1**；config host 行含〔.collab/adr/、docs/adr/〕命中 1、architect 行含 docs/adr 命中 0。第 5-6 款一字不动＝与 `0a4249a` 版本程序化逐行对比全等（该文件 diff 仅单一 hunk 辖第 1-4 款）。A3 全部替换文本＝票面逐字串逐条在位断言 9/9 PASS；lead 卡行数与开工基线差恰 +1（票面登记口径 77→78 对应票面基线值，开工实际基线已含 T3 挂载句随动，内容差恰拆行一处，见偏离 3）。

**判据 9＝绿**：仓根 `git ls-files ".scratch/tickets/" | grep -c "COLLAB-STRUCT"`＝**0**（开工现值 3）；bundle 面票族专名 `-E` 口径＝**3**（开工现值 0）；向前进核对＝`0a4249a..d616b77` 区间两 qa 旧桶 name-status A 状态命中＝**0**。

## §6 禁动面复点＝全绿

`agent-experts/baigong-software-team/docs/adr/` diff `0a4249a..HEAD` 空（一字不动）；三同源 diff 空且现值三处均 0.1.30（零 bump）；两包 qa diff 空（未并入迁移）；SEMGV-T3 案写集（bundle.lock／注册面 plugin.json／sop SKILL.md／claim-commitment-governance 七件）diff 空零触碰；六外包 README／defects 台账／门禁机件本体 diff 空照登。**写集闭集对钉**：链合计 10 A＋14 M＋271 R——M14＝声明 15 面减新建仓根 README（转 A）恰余全部；A 面 STRUCT 本批＝add 面 5 件闭集全中（ledger 三＋仓根 README＋architect 占位 README）＋回执笔恰一件＋20 散件在新路径侧（链合计并入 R）；其余 A/M＝他案四笔剔除照登——**零越集**。

## 纯净性（拍板㊻）＝绿

对 `e49977a` A/B 在用面（两 config＋五卡＋两规范真源＋两 README＋.gitignore）全部新增行 85 行做过程字样扫描（链笔号／sha 串／出处钉／案卷指针／故障编号／候裁·拍板字样）＝**零命中**；A4/A5 逐字条款（17 桶行·drafts 顶层条款·依据注记两行·住址成文行·去歧义句）在三件真源＋两 README 中逐字在位且三处 17 桶行逐字同值；architect 占位件 4 行≤5 行限；仓根 README 含仓根性质注。净化对照表申报 18 处＝其面即上述零命中扫描面，交付面纯净独立坐实。

## 三偏离独立裁定素材

**偏离 1（施工拆两笔）＝无实害坐实、半态在链照登**：`e49977a` 单独 checkout 态独立实测＝旧根面 20 件＋新 decisions 路径 20 件**双路径共存**（旧 20＋该面 74 直系含新 20 实数在链）——该半态下对旧路径的引用**仍可解析**（旧路径未删＝不新增悬空），对新路径引用亦解析正常＝**窗口内仓内引用零实害**；唯一异常＝`e49977a` 单点不满足判据 3「根面散件 0」读数（该判据在链终点 `d616b77` 满足）。§1.1「同批一 commit」辖 A＋B 不拆配置先/目录后——本次拆点在 B9 内部（目录级 pathspec 未覆盖仓根散件旧路径），A＋B 主体仍在 `e49977a` 同批；20 件跨笔 blob 全等＝补齐不缺损属实。

**偏离 2（新 BLOCK 一枚）＝唯一性＋同题性双确认**：见判据 5——存在性、唯一性（13 件 A/B 面靶检恰 1）、目标实存（射程缺口非真悬空）、与 U28 同族同题均坐实；随注 U28 后缀唯一层对 7 后缀多义不消解之差别，收口归 U28 线或住址行逐字条款的既有处置（advisory 不拦），本批无整改义务。

**偏离 3（开工复点漂移）＝与票面条款自洽**：五卡 sha 钉作废重取条款（票头复点行明文）适用属实——开工锚五卡各含 T3 挂载句 1 行实查（claim-commitment-governance 各恰 1 命中），票面基线钉值（46/47/49/49/77）与 `0a4249a` 实值（47/48/50/50/78）差＝T3 挂载句＋既有落件，一切按内容锚定位条款承载；fuxi qa 48→51、decisions 56→58 漂移均在「以开工复点为准、不锁死本数」条款射程，公式两读数相等不受害＝漂移合法。

## 黄项台账

**黄-1（归因颗粒·不阻断·不构成放行障碍）**：判据 5 差值归因中工程师回执「新文案面 19 条」分类数与本部逐条独立分解（BLOCK 侧 42 枚 B8 短式＋1 枚住址行＋tmp 1 枚等）口径不可精确复现；差值总数（+117）恰等、全部 151 新增/34 消解均可归因于本批 mv／新建文本、零无归属残留、零糊账——判黄为归因表分类颗粒度差，修正＝回执口径随注补列 B8 短式与 tmp 两类目即可（预授权闭合路径＝回执 append 一行级，无盘面改动）。

## 放行建议

**绿建议放行**：九判据独立实跑全绿、禁动面全封、写集闭集零越集、交付面纯净坐实、三偏离均无实害或已在册同题；黄-1 为回执文书面随注级，不阻断收口。会师收口按 `0a4249a` 放行登记声明「QA fresh eyes 会师收口中间不再回裁」口径执行。

- 取证居仓根 `.scratch/COLLAB-STRUCT-1-qa/` 不 commit（含两 worktree 用后移除）；本判词单独落账恰一件；落笔前本件 check-pointers 靶检零 BLOCK exit 0；message 零 at 符号字符用「at符号」字样；双侧 pathspec 限判词一件。
