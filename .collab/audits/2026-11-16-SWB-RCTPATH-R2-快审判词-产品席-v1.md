# SWB-RCTPATH-R2 · 快审判词 · 产品席（pm-rctrev·v1）

- 收件人：主理人（team-lead）
- 目的：SWB-RCTPATH-R2 修订轮票面双席快审之产品席独立判词（fresh eyes·只读零改·逐项实测取证）
- 正文：自包含——本件含全部实测读数，接收方不必回查他件即可裁决
- 来源：【来源】pm-rctrev（产品席）· 派工令「RCTPATH-R2 票面 fresh eyes 快审」
- 状态：待处理

> 体例自注：本件正文对一切路径仅叙述性提及＝裸文写＋全角斜杠（／U+FF0F），不落反引号路径指针＝防自咬体例；引文块承载原文时反引号内容以 ⟦⟧ 标记替换。

## 〇、开工读数（本席现跑）

- git rev-parse --short HEAD ＝ **89f796d**（＝R2 票面落链＝派工预期值·即链顶·如实登记）。
- 审对象＝.scratch／tickets／2026-11-16-SWB-RCTPATH-R2-留档件正文路径写法甲案条款修订票-v1.md（89f796d 落链，git show --stat 坐实恰一件 112 行新增·票名尾标 [SWB-RCTPATH-R2-TICKET]）。
- git status --porcelain 照登零带入零清理＝ledger 一枚 M 态＋仓根散件群（与本席开工读数同构：.collab 根散 md 十二枚／.collab／research 散 md 六枚／.py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt＝他案脏面，本席零带入）。
- 本席 scratch 工作区＝.scratch／rctrev-pm／（完工自删·commit 留证保留）。
- 独立性申报：本席未读未引用同票 QA 席任何产出；全部读数为自家现跑。

## 一、总裁决

**红 1 · 黄 2 · 绿 9 → 需 rev（一条 V 系判据硬伤必改；两处读数级勘正随 rev 顺改）**

条款文本本体忠实、落点论证成立、取证可复现——案件实体面全绿。红项集中在验收判据 V4：票面要求「落点件自靶 exit 0」，而落点件现文自带一枚在册悬空指针（现跑坐实 exit 1），该判据与 V2「既有字句零改」＋§五 门禁零触互斥，按票面现文施工笔必绿不了 V4。此项属验收判据规格缺陷（非新决策项），rev 改判据口径即可闭合，不动摇甲案落地。

## 二、红项（附实测取证）

### 红-1 ｜ V4「落点件自靶 exit 0」不可机械满足·与 V2 及禁动面互锁成死结

- 票面位置：§四 V4——「python share/check-pointers.py --root . --target 落点件实路径 → exit 0；同轮对施工回执／本票面各跑 --target 亦 exit 0」。
- 失实点：落点件现文**开工前即不满足**该判据。现跑读数：
  - ⟦python share/check-pointers.py --root . --target agent-skills/multi-collab/references/20-handoff.md ⟧ → **exit 1**，输出 ⟦agent-skills/multi-collab/references/20-handoff.md:24: BLOCK OA-D6 指针悬空 deliverables/experts/baigong-software-team/skills/software-orchestration/references/handoff-discipline.md → 目标不存在⟧。
  - 悬空根因在册＝20-handoff.md §二「决策/设计类交接件的附加判据」段（现文行 24）内半角反引号指针仍指 B2 搬家前旧径 deliverables／experts／…（真源现位＝agent-experts／baigong-software-team／skills／software-orchestration／references／handoff-discipline.md，git ls-files 恰一实存坐实）；该旧径未列 share／baseline-pointer-exempt.json 豁免清单（现读八枚 items 逐项核过，无此 token）。
  - 死结构成：V4 要落点件 --target exit 0 ⇒ 须消行 24 悬空 ⇒ 消悬空只有两路——改行 24 字句（违 V2「全部五十九行现文一字不动」＋§五「另一落点候选件…引用只指不搬」同理的既有真源零改面）或进豁免清单（违 §五「门禁配置零触」）。纯 append 施工笔对行 24 无能为力。
  - 缺省门禁态能过（89f796d 等笔均过钩）不构成豁免：钩面走 run-gates 缺省域发现数对账口径，V5 已按该口径写「零扰动如实登读数」；V4 是对该件单文件的 exit 0 硬判据，两者口径不同，V4 现文独立看必挂。
- 前车之鉴同型：上一批票「全仓 grep 零命中」判据不可机械满足被 QA 席判红——同属「判据写给了一个开工即不成立的终态」。
- 修法建议（供 rev·不属候裁）：V4 改为「落点件 --target 输出对比开工基线＝除行 24 既有悬空一枚外零新增 BLOCK／WATCH；该既有悬空如实登记基线读数」，或等价「差量零新增」口径；同时把行 24 悬空本身转入候补池/另案（它是一枚真在册悬空，与本条款案无关，不该由本票顺手背）。

## 三、黄项（附实测取证）

### 黄-1 ｜ 落点件行数「五十九行」失实＝实测 58 行·V2 核验等式必差一

- 票面位置：§3.2「现文五节·五十九行」；§3.2 末条「全部五十九行现文一字不动」；§四 V2「现文五十九行逐行仍在（git show HEAD 该件行数＝59＋新增行数）」。
- 实测：wc -l 该件＝**58**；git show HEAD 该件 | wc -l＝**58**；文件以单一换行收尾（python 读全文 endswith 单 \n 坐实）。「59」仅在 split 计数含尾空串口径下成立，票面未声明口径。
- 危害面：V2 是验收等式判据，工程师若按 wc -l 现读对拍将得 58＋新增≠59＋新增，触发核验失配轮。rev 时统一为「58 行」或写明计数口径。

### 黄-2 ｜ §3.1 择点理由一对 dev-discipline 卷首自注引文省略未标注

- 票面位置：§3.1 理由 1——「dev-discipline 卷首自注＝『本地约定（跨项目·全专家/技能开发通用）』」。
- 实测：原文＝⟦本地约定（跨项目·全专家/技能开发通用·四件一体成文）⟧——引文截尾省「·四件一体成文」未加省略号。论断方向不受影响（技法面定性仍真），属引文不逐字，rev 顺补即可。

## 四、绿项（逐项实测）

- 绿-1 条款文本忠实性：§3.3 五条与归裁登记 §二 甲案四要素逐一对位——域界定句（不约束消息面域＝体例三律②照旧）↔裁定「消息面照旧含盘符全路径＝两域两制，条款内写清域界」；「一律仓根相对纯路径（正斜杠）」↔裁定同句；「叙述性提及允许裸文＋全角斜杠」↔裁定同句；「嵌套包内文件亦按仓根相对全径写」↔裁定同句并加严「自包根相对形态不在允许集」＝原票 §三 甲案本义。第 5 条「只辖仓内文件」＝裁定「提及仓内文件」射程的自然澄清非新口径。零乙案要素偷渡（乙案＝正文含盘符制，条款明拒并两域分立）。归裁三要素誊写展开属实。
- 绿-2 落点锚点真实：插入锚点现文在册——行 26 ⟦**append-only**：交接件落定后只追加勘误注，不改原文（史实锚）；**不改他人文档**——要驳就另立一件回投。⟧ 与票面引文逐字吻合（含星号加粗标记）；行 27 空行；行 28 ⟦## 三、两盘区分（写权＝路径前缀，可机检）⟧ 节题紧随＝「§二 末段之后、§三 节题之前」位置如述。「### 二之二、…」节题形态插入不触节序一～五。
- 绿-3 落点论证可驳性核查（三条理由均无失实）：①候选二 dev-discipline §三 节题实测＝「三 工程师完工回执」三目，节射程确窄于条款全体席位射程；§一-2「其他席位…一切产出＝过程件」在册；卷首自注定性属实（引文瑕疵见黄-2）。②三律②随动先例 check-ticket-reconcile.py 行 375 注释「工具向票面体例三律②『含盘符完整路径』对齐」现读逐字对上；归裁登记 §二 亦径称候选一为「交接真源」。③落点件现文对同卷件反引号引用先例在册（行 22 对 30-formats.md 的引用句）。
- 绿-4 取证可复现（抽查≥3 项）：①8792a97（原票面·80 行）git show exit 0；②4ea0d58（归裁登记·30 行）git show exit 0 且为 89f796d 之父笔（git log %p 坐实）＝§〇「HEAD＝4ea0d58 即链顶」属实；③check-ticket-reconcile.py 行 374-391 现读＝注释起于行 375＋ABS_RECEIPT_PTR_RE 行 380＋RECEIPT_TAIL_PTR_RE 行 383-384＋abs_ptr_to_rel docstring，三认态①②③对号、仓外绝对不算、包根相对不在三认态＝票面 §二-4 全相合；④CPRC5 回执行 26／27 引文（包根相对 token 改字补全／错径旧域前缀 token 修正）现读吻合。
- 绿-5 §〇 脏面清单实数对拍：ledger M 一枚＋?? 计 23 枚＝.collab 根散 md 12＋research 散 md 6＋.py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt＋本笔 scratch 目录前未含 rctrev-pm——与票面列举逐项吻合。
- 绿-6 本票面自靶现跑：python share/check-pointers.py --root . --target 本票面实路径 → **exit 0**（防自咬体例成立；§3.3 条款文本块内零反引号 token，dev-discipline 字样均裸文节号引用＝不入指针射程，与票面 §3.3 随附说明一致）。
- 绿-7 V0／V1／V3／V5／V6 机械可判：V0 读数复现（见绿-4②）；V1 单件 diff 面判据可执行；V3 逐字节对等可 diff 比对 exit 码判定；V5 已预写「dev-discipline 引用句若被计提及→如实登记差量＋基线」对冲口径（本席现读缺省扫描该件新增面预计零 BLOCK——条款块无反引号——V5 兜底足够）；V6 两笔各恰一件可 git show --name-only 判定。唯 V2 差一（黄-1）、V4 死结（红-1）。
- 绿-8 §五 禁动面自洽：候选二件零触／原票面零回改／候补池与 MEMORY 面零写／机检加严段不预装（归裁登记 §二 末条在册同口径）／share／全域零触＝与 V 系无冲突面（share／ 只读调用不在写入触面）。
- 绿-9 §六「零新候裁」属实：条款取态已归裁在册（4ea0d58 §二）；落点择一＝归裁登记明示执行分解归架构席自决＝本票已论证自决不呈裁，层级正确；本席快审未发现真分歧——红-1 属判据规格缺陷，修法在票面文字内（改 V4 口径＋悬空另案），不涉新决策项，不构成候裁。
- 绿-10 命名说明成立：R2＝票号后缀与原票面 v1 文件名并存不冲突；归裁登记「不回改票面」与「修订另立本件」一致（4ea0d58 §二 在册句）。

## 五、总判与 rev 修单

**需 rev**（修订轮票面出 v2·append-only 随例另笔或票面勘正注按主理人定例）。修单三条：

1. N-1（红-1）：V4 改差量口径——「落点件 --target 除行 24 既有悬空一枚（基线读数随票附登）外零新增 BLOCK／WATCH」；该枚在册悬空另案处置（候补池或工具票），不由本票顺手改字句或进豁免。
2. N-2（黄-1）：「五十九行」三处改「58 行」或写明行数口径；V2 等式随动。
3. N-3（黄-2）：§3.1 dev-discipline 卷首引文补全或加省略标注。

条款文本 §3.3 本体零修单——忠实在册裁定，放行面仅卡在验收判据。

## 六、纪律笔

- 本席只写本判词件一件；只读评审零触碰真源；单件 pathspec 两端齐带·add 紧邻 commit 零窗口·commit 前 git diff --cached --name-only 坐实仅自件·FX_COMMIT_DECLARE＝仓根相对纯路径挂 commit 命令侧·禁 add -A／amend／no-verify·message collab: 起头零 at 零反引号·尾标置最末位·commit 输出重定向 .scratch／rctrev-pm／（完工自删·留证在链）·撞锁有界等待零删锁。
- 防自咬体例＝路径裸文＋全角斜杠·引文块反引号内容以 ⟦⟧ 替换；落链前自靶 python share/check-pointers.py --root . --target 本判词件实路径 须 exit 0（读数见完工回报）。
- 他案脏面照登零带入零清理；链上 FUXI 笔群零碰；未读未引用同票 QA 席任何产出。
