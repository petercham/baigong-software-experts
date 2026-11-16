# SWB-RCTPATH-R2 · 留档件正文路径写法甲案条款修订票 · fresh eyes 快审判词（QA席 qa-rctrev · v1）

- 审对象＝票面 .scratch／tickets／2026-11-16-SWB-RCTPATH-R2-留档件正文路径写法甲案条款修订票-v1.md（落链 89f796d）
- 判词落点＝.collab／audits／2026-11-16-SWB-RCTPATH-R2-快审判词-QA席-v1.md（本件）
- 审法＝只读实测取证·逐项现跑复现·不读不引用产品席任何产出
- 总裁决＝**需 rev**（红 2 黄 2 绿 8）

> 本席体例自注：正文路径一律裸文＋全角斜杠（／U+FF0F）＝防自咬；引文块内反引号内容以 ⟦⟧ 替换。

## 〇、开工读数（本席当轮现跑）

- git rev-parse --short HEAD ＝ **89f796d**（＝票面落链＝派工预期值·即链顶）。
- 89f796d 链段恰一件（票面本身·112 行插入）·git show --stat 复现；其父＝4ea0d58（＝归裁登记落链·与票 §〇 起草读数自洽）。
- git status --porcelain 照登零带入零清理＝ledger 一枚 M 态（agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl）＋仓根散件群（.collab 根散 md 十二枚／.collab／research 散 md 六枚／.py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt）——与票 §〇 他案脏面清单逐类对拍一致。
- 本席 scratch＝.scratch／rctrev-qa／（完工自删·commit 留证保留）。

## 一、红项（2）

### 红-1｜V4 对落点件的「--target exit 0」口径现盘即不可机械满足（前车之鉴同型）

- 票面位置＝§四 V4：「python share／check-pointers.py --root . --target 落点件实路径 → exit 0」。
- 失实点＝落点件现文自带一枚**在册既有 BLOCK**，与插入段无关、且按票面自身禁动面不可修复——该判据按字面现盘即不可满足，亦不可经合规施工变为满足。
- 实测取证（本席当轮现跑）：
  1. python share/check-pointers.py --root . --target agent-skills/multi-collab/references/20-handoff.md → **exit 1**，输出恰一条：agent-skills/multi-collab/references/20-handoff.md:24: BLOCK OA-D6 指针悬空 ⟦deliverables/experts/baigong-software-team/skills/software-orchestration/references/handoff-discipline.md⟧ → 目标不存在（该行现文在册＝§二「决策/设计类交接件」段迁移指针，SWB-B2 搬家史产物）。
  2. 该 token 不在豁免快照：share／baseline-pointer-exempt.json 现数恰 5 键，逐键扫描无含 handoff-discipline／deliverables/experts 者。
  3. 修复该悬空行＝改既有字句，直接违反票 §3.2「全部五十九行现文一字不动」与 §五 禁动面、V6「施工笔＝恰一件且零触其余」口径——即 V4 与票自身约束**互斥闭环**：要么 V4 必红，要么破禁动面。
- 与 V5 自相矛盾：V5 预设缺省 BLOCK 钉值「零扰动如实登记」＝默认该既有 BLOCK 计入基线照旧存续；V4 却同时要求同件 --target exit 0。两判据不能同真。
- 修单建议（供 rev·非本席裁量）：V4 落点件侧改「与开工基线读数对拍零新增 BLOCK（差量口径）」，同轮本票面／回执 --target exit 0 照旧；既有悬空一枚另归 check-pointers 自身悬空处置在册线（A14H1 同族）呈排，不入本票射程。

### 红-2｜落点件现文行数失实（五十九→实测五十八）·V2 计数判据照字面必不符

- 票面位置＝§3.2「现文五节·五十九行」；§3.2 约束行「全部五十九行现文一字不动」；§四 V2「现文五十九行逐行仍在（git show HEAD 该件行数＝59＋新增行数」）。三处同错。
- 实测取证：
  1. wc -l agent-skills/multi-collab/references/20-handoff.md ＝ **58**；grep -c '' 同件 ＝ 58（文件以换行收尾·末字节 0a 已 xxd 坐实＝58 行读法无歧义）。
  2. git show HEAD:agent-skills/multi-collab/references/20-handoff.md | wc -l ＝ **58**。
- 危害＝V2 为计数判据，按票面所载「59＋新增行数」现跑必差一＝验收轮必翻红；属票面读数失实＋V 系口径不可机械满足双失。
- 修单建议＝三处 59→58（或改「行数＝58＋新增行数」口径）。

## 二、黄项（2）

### 黄-1｜条款第 1 目锚的「交接件体例三律②」在交付面无规范真源句

- 票面位置＝§3.3 条款第 1 目「仍照交接件体例三律②＝附含盘符完整本地绝对路径——该律不变」；§3.1 理由 2／3 同引。
- 实测＝全仓检索（排除 .scratch／与 .collab／过程域）：「含盘符」在 agent-skills／multi-collab／ 七件 references 与 handoff-discipline.md 内**零命中**；「体例三律」成句仅在册 .workbuddy／memory／MEMORY.md 行 26「交接件体例三律：md 落盘；提及文件附完整盘符绝对路径；来件开端附当轮 HEAD 实测」＝主理人记忆面；工具面随动先例＝share／check-ticket-reconcile.py 行 375 注释（该注释只**引用**三律②字样，非律文真源）。
- 定性＝对归裁登记措辞的忠实誊写（归裁 §二 亦用该字样）＝不判红；但条款若按稿落进交接真源，将出现「真源件内一条律引用交付面无真源的律」＝语义锚悬空，与「引用只指不搬」的引用前提（所指须在册）有隙。
- 建议＝rev 时条款第 1 目括注补三律②真源出处，或另呈微票先把体例三律成句誊入交接侧真源族（不在本票射程·本票禁动面自洽）。

### 黄-2｜§3.3 块自注与块实态不符（自述含半角径，块内实零半角路径 token）

- 票面位置＝§3.3 引子「（块内＝落笔实文本＝仓根相对半角径为条款实质·非本票叙述面）」与票面自注（行 12）「§三 条款文本块内的仓根相对半角径＝未来落笔实文本」。
- 实测＝§3.3 围栏块全文（票行 68-74）逐行扫描：无任何半角斜杠仓根相对路径 token；块内路径性字样仅 dev-discipline 裸文节号引用（第 3／4 目）与「／U+FF0F」全角说明。自述所称「半角径为条款实质」在块内无对应物。
- 定性＝纯自述失准·不伤条款实质与 V3 逐字对等判据＝黄。建议＝自注改为「块内引用形态＝裸文节号引用＋全角叙述形态」。

## 三、绿项（8）

1. **条款忠实性＝绿**：§3.3 五目逐目对照归裁登记 §二（落链 4ea0d58·30 行件·git show 复现）：仓根相对纯路径（正斜杠）✓／叙述面裸文＋全角斜杠豁免✓／嵌套包仓根相对全径✓／消息面照旧含盘符＝两域两制域界定写入✓——甲案四要素齐载。第 2 目「自包根相对形态不在允许集」＝甲案「亦按仓根相对全径」的收敛展开＋本案案名本义（包根相对写法预防），非偷渡；第 5 目「仓外不在射程维持现状」＝射程闭合句，甲案原文即只辖「仓内文件」，无新决策。**乙案要素零夹带**（通块无「含盘符入正文」口径）。
2. **落点插入锚点真实＝绿**：现文行 26 ＝ ⟦**append-only**：交接件落定后只追加勘误注，不改原文（史实锚）；**不改他人文档**——要驳就另立一件回投。⟧ 与票 §3.2 锚点句**逐字全等**；行 27 空行；行 28 ＝ ⟦## 三、两盘区分（写权＝路径前缀，可机检）⟧——插入位「该段与其后空行之后、§三 节题行之前」如述真实；插入节题「### 二之二、…」三级小节居二级节间，不破坏五节结构与编号。
3. **落点论证可核＝绿**：§3.1 所据可复现——20-handoff.md 五节节题如票所述（一 成文理由／二 规格／三 两盘／四 落盘分发／五 消息方向律）；dev-discipline §三节题＝「工程师完工回执」（行 38 在册·三目结构属实）；§一-2「其他席位一切产出＝过程件」在册；卷首自注「本地约定（跨项目·全专家/技能开发通用·四件一体成文）」在册；候选二零采用列入 §五 一致。
4. **取证复现（抽查≥3 项）＝绿**：①share／check-ticket-reconcile.py 行 375 注释句现读逐字＝「# 回执指针两形态（ENG-S7 扩认·工具向票面体例三律②『含盘符完整路径』对齐）：」，三认态①②③在册（375-386 区段），**包根相对确不在三认态**；②CPRC5 回执例证：.collab／receipts／2026-11-14-SWB-CPRC5-工程师回执-v1.md 行 26／27 现读＝「件一（ADR-L0 回执）行 3·乙-1：包根相对 token 改字补全为仓根相对全径」「件二…错径旧域前缀 token 修正桶路径」逐字在册；③ADR-L0 回执 ⟦.scratch/eng-adrl0/⟧ 包根相对 token 现读在册（该件行 3 反引号 token）；④dev-discipline §八-5 scratch 取证族只准叙述性提及＋时序互搏根因在册（行 80 节·第 5 项全文）。行 374-391 段引用属实（374 为空行、389 起为 abs_ptr_to_rel 函数头，段界宽松不失实）。
5. **票面读数对拍＝绿**：票面行数＝112（wc -l 现跑＝112＝commit stat 112 insertions 全等）；票链段恰一件（git show --name-only 89f796d＝票面一枚）；§〇 HEAD 4ea0d58 与票链父笔实测吻合；他案脏面清单与当轮 git status 对拍一致。
6. **票面自靶＝绿**：python share/check-pointers.py --root . --target .scratch/tickets/2026-11-16-SWB-RCTPATH-R2-留档件正文路径写法甲案条款修订票-v1.md → **exit 0** 现跑复现（票 §八 声称成立）。
7. **V 系其余可判＝绿（红项除外）**：V0 开工读数可复现；V1 diff 仅 append 段口径可执行（name-only 恰一件＋「零其他 hunk」闭合歧义）；V3 逐字节对等可执行（从 §3.3 围栏块提取 vs 落笔新增段 diff）；V5 基线差量登记口径可执行；V6 两笔恰各一件可执行；防自咬判据（自靶 exit 0）可复跑。
8. **§五 §六 自洽与零新候裁＝绿**：§五 禁动面六条与归裁登记「不回改票面」「机检加严段不预装」逐条对上；§六 判据成立——取态已裁（4ea0d58）、落点择一系归裁明示「执行分解归架构席自决不上楼」、施工规格属执行细节；本席全审未发现真分歧，零新候裁属实（红-1 属判据缺陷非候裁项——修法属票内自纠，不涉决策者保留范畴）。

## 四、总判

**需 rev**。红二项均为窄修可闭：红-1 V4 落点件侧改基线差量口径（既有悬空另线呈排）、红-2 三处行数 59→58。黄-1 建议 rev 时补三律②真源出处或另线成文；黄-2 自注勘正。条款文本本体（§3.3）忠实甲案、落点锚点真实、论证成立——修 V 系与读数后即可放行。

## 五、纪律笔（本席起草笔自证）

- 只写判词件一件；单件 pathspec 两端齐带·add 紧邻 commit 零窗口·commit 前 git diff --cached --name-only 坐实仅自件·FX_COMMIT_DECLARE 挂 commit 命令侧·禁 add -A／amend／no-verify·message collab: 起头零 at 零反引号·尾标 [SWB-RCTPATH-R2-QA-REV] 置最末位·commit 输出重定向 .scratch／rctrev-qa／·撞锁有界等待零删锁。
- 落链前自靶：python share/check-pointers.py --root . --target .collab/audits/2026-11-16-SWB-RCTPATH-R2-快审判词-QA席-v1.md 须 exit 0（读数见完工回报）。
- 只读评审零触碰真源／票面／落点件；他案脏面照登零带入零清理；链上 FUXI 笔群零碰；产品席产出零读零引用。
