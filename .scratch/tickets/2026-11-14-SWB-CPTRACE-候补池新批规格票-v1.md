# SWB-CPTRACE · 候补池新批规格票（v1·纯规格·零施工）

- 票号：**SWB-CPTRACE**
- 票名：**回执留痕引用体例条款与 SCRATCHCFG 黄-1 存量处置规格票**
- 票型：维护（轻量工作分支·体例四查全列＋引用面必查按射程申报）
- 起草席：架构席 arch-cpool2（fresh 实例·前任架构席未落产出·本票从零起草）
- 票面落点：`.scratch/tickets/2026-11-14-SWB-CPTRACE-候补池新批规格票-v1.md`
- 来源：SWB-SCRATCHCFG 收口登记（`5801e42`）事故照登黄-1 挂候补池＋QA 判词（`838f982`）§六建议方向 (a)
- 候裁点：§七（本票预期零枚·闭集收紧口径见彼节）

> **票面自注**：本票正文对一切 scratch 取证族留痕仅叙述性提及、裸文写（全角斜杠）、不落可达全径＝本票自采新条款体例·防自咬。正文反引号路径形态引用者均已实测在场。

---

## 〇、开工读数（起草轮现跑·禁抄旧数）

- `date`＝`Sat Nov 14 02:22:27 2026`
- `git rev-parse --short HEAD`＝`5801e42`（＝SWB-SCRATCHCFG 收口登记笔＝链顶·与派工预期起点全等）
- `git status --porcelain`＝tracked 脏面一枚他案照登零碰零带入＝M agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl；仓根 untracked 散件群照登不入（仓根 .collab／ 案卷散件十四枚＋散件 .py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt＋仓根 .collab／research／ 散件五枚）
- 开工窗 index.lock＝free（未撞锁）
- 缺省面 BLOCK 基线现跑＝`python share/check-pointers.py 2>/dev/null | grep -c "BLOCK"` ＝ **22827**（与 SCRATCHCFG 链上 V0／V5 读数全等；留痕裸文落本席 scratch 票号族 v0-cp-default.txt＝完工随族自删）

## 一、议题与根因链（人话版）＋实证读数

**互搏机理**：仓内两条纪律同席同日互搏——

1. **纪律①（临时工作物完工自删）**：dev-discipline §八＝一切临时工作物唯一落点各项目仓根 scratch 票号族，收口登记票必含清理判据，收口态＝零残留（scratch 取证族批毕删除）。
2. **纪律②（回执正文引用本族留痕全径）**：工程师回执体例惯态＝V 读数逐条附留痕文件全径（反引号路径指针形态）。

时序：回执落笔当时 scratch 族在场→当时靶检绿；完工自删后指针必悬空→事后对回执件跑靶检必出 BLOCK。**落笔当时绿≠永久绿**——非施工面责任，是两纪律的时序互搏＝设计缝隙，属治理面体例修法。

**实证读数（起草轮现跑复现·回执件指 SCRATCHCFG 票附回执）**：

- 靶检该回执件现跑 → **exit 1**·三枚 BLOCK（行 24／25／73·悬空目标均指已自删的工程师 scratch 取证族＝裸文写 .scratch／SWB-SCRATCHCFG／v0-s4-before.txt、.scratch／SWB-SCRATCHCFG／v0-block-before.txt、.scratch／SWB-SCRATCHCFG／v7-rungates-before-build.txt 三枚；另 NOTE-FXU28 短式归位注记一枚不进 findings）
- 同件在**缺省扫描面读数＝不在场**：缺省域＝三分类目录（agent-experts／agent-skills／softwares），仓根 tickets 桶不在域内→本回执三枚悬空**不入缺省 BLOCK 基线 22827**（此点决定 §四处置选型与 A14 先例零碰撞·见彼节坐实）
- QA 判词（`838f982`）在册同判：黄-1＝票面两要求互搏之设计缝隙，非施工面新增悬空；建议归治理面另账＝回执引用 scratch 留痕宜用叙述性描述或留痕改落票附件内。

## 二、净影响面（grep 实证盘点·修法射程）

盘点口径写死两面：

- **A 面＝原始字样面**（正文含反引号起手的 scratch 族路径字样·过含·checker 未必当路径解析）：起草轮现跑 git grep 对模式「反引号字符＋转义点 scratch 斜杠＋票号字符族＋斜杠」限定文件名含「回执」或 receipt 的 tracked 件 → **295 枚字样／102 枚文件**（含大量 checker 不当路径形态：命令段含空格、通配段、jsonl 等非判据扩展名·及目标仍在场者——A 面≫真射程，只作体量参考）。
- **B 面＝机检语义真悬空面（修法射程真值）**：起草轮程序化复跑＝复用 check-pointers 自身 looks_like_path／resolve／后缀归位三层函数逐 token 判（留痕裸文落本席 scratch 票号族·完工自删）＝**7 枚悬空 token／4 枚 tracked 回执类件**：
  1. SCRATCHCFG 票附回执（仓根 tickets 桶）行 24／25／73＝**3 枚**（本票必修·§四）
  2. `agent-experts/baigong-software-team/.collab/receipts/2026-11-05-ADR-L0-工程师回执-v1.md` 行 4／48＝2 枚（指向已删 eng-adrl0 取证族·在缺省扫描域内）
  3. `agent-experts/baigong-software-team/.collab/receipts/2026-11-05-AV-FIX-工程师回执v1.md` 行 12＝1 枚（指向已删 AV-FIX 取证族）
  4. `agent-experts/baigong-software-team/.collab/receipts/2026-11-06-TK-PROJINIT-工程师回执-v1.md` 行 21＝1 枚（指向已删 projinit 取证族）
- **不入射程面（写死）**：tickets 桶退役票面悬空引用（SWB-RET 退役批删票面所致·另一根因·由票面寻回体例承载）与 fuxi 案 scratch 内 worktree 副本树行（缺省面内数千枚·他案取证噪声·FUXI 面零碰照登）。缺省面全部 scratch 指向 BLOCK 行现跑 14833 枚、其中文件名含回执／receipt 者 3481 枚、剔 fuxi 副本树后非票面类 58 枚——大头＝退役票面指向与副本树，均不入本票射程。
- 他案脏面口径：仓根 untracked 散件群未 tracked 未入扫描·照登不入。

**射程结论**：条款面（S1）防增量＝一切未来回执／判词／收口登记／commit message；存量必修（S2）＝本批 3 枚；上述 2–4 共 4 枚存量挂新候补行（§六）。

## 三、逐字落位规格（体例条款成文·采纳值写死）

**采纳修法＝(a) 回执类工件正文对 scratch 取证族仅叙述性提及、不落可达全径**——采纳值由架构席写死（候裁面不收此枚·§七）。理由：

1. (b)（留痕改落票附件内）与 **sources 洁净纪律**张力＝scratch 留痕多为机检原始输出（过程物），升格入登记附件＝过程物混入登记面，违 dev-discipline §二「开发叙事不入」「过程物不混入」同族口径；
2. (b) 与 **scratch 轻量纪律**张力＝留痕升格 tracked 常驻件＝取证物永久仓存＋§八 自删纪律失效；
3. (a) 实践口径已在册：SCRATCHCFG QA 判词 §六纪律自证行对工程师席 scratch 取证族「仅叙述性提及不落可达全径」已同型运转；FX-U48 修法①拆写／裸文先例体例在册；
4. (a) 零机检扩装＝与 check-pointers 现行语义（反引号才解析）天然咬合，不扩豁免、不加新 checker。

### S1 条款成文（落点写死·逐字照录）

**落点文件**＝`agent-experts/baigong-software-team/skills/software-orchestration/references/dev-discipline.md`（§八「临时工作物落位与清理纪律」真源·现文第 80–85 行·第 4 项止于第 85 行）。

**S1-a**：§八 第 4 项之后新增第 5 项（插入位置＝现文第 85 行之后、原空行之前；插入文本逐字如下·围栏标记仅标界不入正文）：

```
5. scratch 取证族可达路径不入留存工件：回执、判词、收口登记、commit message 等一切在 scratch 取证族完工自删后仍留存的工件，正文对任何席位的 scratch 取证族（各项目 `.scratch/<票号>/` 族及其内工件）仅准叙述性提及＝族名或工件基名裸文写、不以反引号路径形态落指针；判据＝指针机检可解析的指向 scratch 取证族之路径 token 零出现。取证需长存者，先升格为登记常驻件（归档面或票附件案面）再让指针只指常驻位。根因＝本节第 3 项完工自删与正文引用留痕全径的时序互搏：落笔当时在场故当时绿，自删后卫检必悬空（SWB-SCRATCHCFG 案 QA 判词黄-1 同构）。
```

（条款文本内反引号 token 带尖括号＝checker 形态判定天然不当路径·条款自身不自咬；条款不写 SWB-CPTRACE 字样＝防机检对账混淆，溯源由本票与 commit 链承载。）

**S1-b**：同文件 §三「工程师完工回执」第 3 项（现文第 44 行）句尾追加随动短句，逐字：

```
正文对 scratch 取证族的引用形态受 §八 第 5 项约束。
```

（同文件两处改动＝同一根因同批一笔；§八＝体例真源、§三＝回执消费位单点指针，不复写条款本体。）

### 禁动面（明确列出）

- share／ 全域零改（含 check-pointers.py、baseline-pointer-exempt.json、check-pointer-closure.py、run-gates.sh——本票**不扩豁免 items**·机械否决理由见 §四选型段）；
- FUXI 面（agent-skills／fuxi-skill／ 全树·含其 scratch 副本群）零碰；
- 史件 append-only 不回改：仓根与两包 .collab／ 案卷既有件（audits／qa／receipts 中除 S2 点名件外一切件）、ADR 落盘面（包根 docs／adr／ 及链上 ADR-L0 群）、ledger／leases／config 两件、SCRATCHCFG 票面真源本体与 QA 判词本体——一字不碰；**唯一例外＝S2 对 SCRATCHCFG 票附回执的三行定向复原**（该件＝tickets 桶票附回执·非案卷三件套史件·不在缺省扫描域·定性坐实见 §四）；
- 他案脏面（ledger 一枚＋仓根 untracked 散件群）照登零带入；
- tests／ 面只跑未改。

## 四、存量处置规格（三枚悬空 BLOCK·逐枚可机械判定）

**处置选型＝改字复原（narrative 化），不扩豁免层**。与「历史件不改字豁免」先例口径**不冲突**的机械坐实：A14 先例采豁免层是为**缺省扫描域**历史件避免基线碰撞（先例基线 17398→17404 型碰撞）；本回执件在仓根 tickets 桶＝**不在缺省域**（§一已坐实），改字对缺省基线 22827 扰动＝**0**，无碰撞面。反向机械否决豁免方案：豁免命中仍出 WATCH 行进 findings→该回执靶检 exit 恒 1＝黄-1 不可闭＝豁免方案对「单件靶检须绿」诉求机械不可用（不采）。改字＝S1 条款对存量的溯及复原＝体例自洽。

**落点文件**＝`.scratch/tickets/2026-11-11-SWB-SCRATCHCFG-工程师回执-v1.md`（tracked·票附回执·(h) 体例）。

**处置指令（逐枚·施工轮机械执行·除点名三行外全文件逐字节零动）**：

1. **行 24**：行内反引号包裹的 scratch 族全径 token（半角反引号原形·指向已自删留痕 v0-s4-before.txt）→ 改裸文形态：去反引号＋半角斜杠换全角斜杠＋随注「裸文写·已随完工自删」；
2. **行 25**：同式（基名 v0-block-before.txt）；
3. **行 73**：同式（基名 v7-rungates-before-build.txt）。

**处置轮禁触行（写死·现跑均不 BLOCK）**：同文件行 37（命令段含空格）、行 43（含空格＋jsonl 双豁免形态）、行 55（jsonl 非判据扩展名）、行 85／86（尾斜杠族根 token·现跑解析命中 tickets 桶不 BLOCK）——一律零动。施工轮若处置后靶检仍现指 scratch 取证族 BLOCK，对命中行同式复原后复跑（收敛判据＝V3）。

**处置前后读数对照（可机械验证）**：

- 处置前（本票开工基线）：靶检 exit **1**·BLOCK 计数 **3**
- 处置后：靶检 exit **0**·BLOCK 计数 **0**（NOTE-FXU28 注记行允许在场·不进 findings 不影响 exit）
- 缺省面：处置前后 BLOCK 计数差＝**0**（该件不在缺省域·V4 坐实）

## 五、V 系机械验收判据（每条＝可照跑命令＋预期·仓级基线占位以验收轮现跑为准）

- **V0 开工基线（施工／验收轮现跑·禁抄本票钉值）**：
  - 靶检 SCRATCHCFG 票附回执（命令同 §一）→ exit 1·BLOCK 计数 3
  - 缺省面 BLOCK 计数现跑＝占位钉 22827·**以验收轮现跑为准**（前后差判据见 V4）
  - 靶检 dev-discipline 落点文件 → exit **1**·BLOCK 恰 **2**（既存基线＝两处对 STRUCTURE 结构件裸引悬空＝docs／STRUCTURE.md 字样拆写防自咬·S1 改动前既有·V2 对照面）
- **V1 条款落位**：
  - grep 计数「scratch 取证族可达路径不入留存工件」于 dev-discipline ＝ **1**
  - grep 计数「受 §八 第 5 项约束」于 dev-discipline ＝ **1**
  - 条款本体逐字＝本票 §三 S1-a 围栏内容（去围栏行）原始文本级 in 判据 True（QA 程序化提取比对）
- **V2 条款面零回归**：靶检 dev-discipline → exit 1·BLOCK 恰 2＝V0 同值（S1 新增行零新指针＝尖括号形态坐实）
- **V3 回执复原兑现**：靶检 SCRATCHCFG 票附回执 → exit **0** 且输出 grep BLOCK 计数 **0**
- **V4 缺省面零扰动**：验收轮缺省 BLOCK 计数 − 开工窗现跑值 ＝ **0**
- **V5 门禁零回归**：`bash share/run-gates.sh` → **GATE PASS exit 0**·发现数占位（开工窗链上读数 151457 系 SCRATCHCFG 链态·**以验收轮现跑为准**·判据＝零回归不升新红栏）
- **V6 声明闭集与零动自证**：施工两笔链上 `git diff --name-only` 面＝恰两件＝dev-discipline＋SCRATCHCFG 票附回执（多一无少＝违例）；blob 级对拍＝dev-discipline 除 S1-a 插入段与 S1-b 追加短句外逐字零动（前像为后像分段严格前缀判据）、回执件除三行外逐字节零动。
- **V7 本票面与施工面防自咬**：落笔前各笔面件靶检 exit 0（本票面现跑见 §八读数）。

## 六、②③并批排程判断（自决＋理由）

- **②A14 黄-1（check-pointers.py 自身 target 面两枚既存存量 BLOCK＝悬空指 references／20-handoff.md 与 docs／INDEX.md 两式）＝维持候另票，不并批。** 理由：根因异＝两枚系脚本注释区内对包文档／索引的叙述性示例引用悬空（文档迁移遗留），与 scratch 取证族自删互搏非同根因；修法落点＝share／ 交付面注释行＝工程师席施工范畴，并入将迫使本票声明闭集跨域（架构席规格票不得携 share 改动）；且 A14 收口登记已裁「候另票」口径在册，无新事实不翻案。本票 S1 条款亦不触及该两枚（其非回执类工件正文·禁动面零碰）。
- **③A14 候②（桶名闭集机检）＝维持候补池候排，不并批。** 理由：属新机检扩面（新 checker 或既有 checker 扩规则＋豁免二段消费面已成文零引用的在册半成品），与「豁免 items 九条」不同量级，需独立规格与排程；并入将稀释本票单根因最小票形态（轻量档）；A14 收口登记「候②两行成文消费面零引用桶名闭集机检维持候补池」口径在册。
- **新候补行呈报（本票盘点产出·候补池新增一行）**：§二 B 面第 2–4 项共 **4 枚**存量回执悬空（ADR-L0 回执 2＋AV-FIX 回执 1＋TK-PROJINIT 回执 1·均在缺省扫描域内·根因与黄-1 同构＝取证族自删）＝S1 条款生效后可按 §四同式（narrative 复原＋豁免选型复评）处置；因在缺省域内，处置涉基线扰动（−4 或转 WATCH），需独立排程评估与 A14 豁免口径的交互，不塞本票（本票声明闭集＝两件封顶）。

## 七、候裁面（闭集收紧·预期近零）

**候裁枚数＝0。** 逐面自查：修法取态 (a)／(b) 属体例条款选型＝架构席职权内（非「改真源口径且未收敛对立」——(a) 与现行 check-pointers 语义零冲突、与 QA 判词建议方向一致＝已收敛）；存量处置选型（改字 vs 豁免）＝机械判据可决（豁免方案对单件靶检机械不可用·§四坐实）＝非真决策者范畴；②③并批判断＝排程职权内；条款溯及既往仅一枚（SCRATCHCFG 票附回执·该件处置＝修复其自身被在册判词点名的黄-1 黄项，属裁决兑现非扩面）。无保留闸触发项。

## 八、起草轮纪律自证与本票面读数

- 起草席临时工作物居本席 scratch 票号族（SWB-CPTRACE·v0-cp-default.txt／v0-cp-three-receipts.txt 等留痕）＝完工自删（本票自身＝交付件保留于 tickets 桶）。
- 本票面防自咬：正文对悬空字样一律拆写／裸文写／全角斜杠；落笔前本票面靶检 exit 0 才 commit（commit 面留痕）。
- 盘点程序化读数留痕＝本席 scratch 票号族·引用处仅叙述性提及（新条款体例自证首件）。
