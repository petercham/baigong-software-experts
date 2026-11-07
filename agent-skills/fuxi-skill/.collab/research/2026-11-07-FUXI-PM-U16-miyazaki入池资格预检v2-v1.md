# FUXI · PM-U16 miyazaki 入池资格预检 v2

> 产品席（pm-fuxi-u16·fresh eyes）亲笔｜日期＝2026-11-07｜性质＝产品判定件（FUXI 账域·research 面）·FX-U15 收口后重跑 PM-U5 的消费侧入池资格预检，非入池确认——人工闸仍归皮总；只读调查产物，除本件外零写入。
> 开工 ANCHOR 实测＝HEAD `fc18b63`（`git log --oneline -1` 现盘实跑＝FX-U15 收口登记笔；FX-U15 链五笔 `3fb8413` 票面→`5a434a4` 封印→`8bddb75` 修订→`6b15688` 回执→`c9791b6` QA→`fc18b63` 收口照登；untracked `.collab/ledger/`、`.scratch/FX-U*` 照登与本案无关禁带入）。
> 射程＝`agent-skills/fuxi-skill/products/pending/miyazaki-hayao-perspective/` 单产物（SKILL.md＋registration.md＋test-prompts.md 三件）；`elements-of-style-technique/` 不入本件射程（本令限定 miyazaki）。
> 预检框架与判据口径＝沿 v1（`agent-skills/fuxi-skill/.collab/research/2026-11-06-FUXI-PM-U5-待审区两产物入池资格预检-v1.md`·落账 `bbed4f0`）：六维资格读数表＋语料落盘侧对拍＋受限面核查＋κ 校准链核查；判据全部取在册口径（`agent-skills/fuxi-skill/gates/assertion-catalog.md`／`agent-skills/fuxi-skill/contracts/evidence-grading.md` EG-6 现版〔补批采纳面五子款＋新鲜度参考评分条款在册〕／`agent-skills/fuxi-skill/contracts/failure-modes.md` FM-S-01 现版〔受限行随撤条件句在册〕／`agent-skills/fuxi-skill/contracts/artifact-contract.md` AC-5／products 两级 README＋先例链），不另造判据。
> 全部读数＝本席现盘实读实跑，不采信任何转述；在册值仅作对拍目标，非读数来源。

---

## 〇、开工基线读数（现盘实跑取证）

1. **assert-tool 汇总**（现盘连跑两次）＝`PASS=27 FAIL=0 PENDING_STAGE=0 总数=27`·**exit 0**·两跑输出逐字节 cmp 全等（留存＝仓根 `.scratch/PM-U16/assert_run1.txt`／`assert_run2.txt`）＝全仓门禁全绿态在本席独立复现（FX-U15 在册声明 27/0/0/27 对拍成立）。BW-3 明细行逐字＝`BW-3 PASS 产物正文实跑命中=0（扫描 12 件·实扫描判绿）`——v1 §〇-1 六命中清单中 miyazaki 三命中全部出清。
2. **池态**＝FC-6 PASS `active 池条目 2·无人工确认来源条目数=0（实条目确认引用行判绿）`（david-fincher-perspective＋mrbeast-perspective 在位·各带 confirmation.md）；pending 条目＝2（miyazaki-hayao-perspective＋elements-of-style-technique；本件预检前者）。miyazaki 目录三件＝SKILL.md／registration.md／test-prompts.md，confirmation.md 不在位＝待审区形态正常（confirmation 属入池闸后动作件）。
3. **产物级结构门禁全绿**（本席跑①同输出内读数）＝ST-3 PASS 4 条目·节 diff=∅／ST-4 PASS 回归条目 24（miyazaki=6）／ST-9 PASS registration 四节 diff=∅／ST-10 PASS 批次 eos-b1、t9 逐路 18/18 在场／FC-3 PASS 要素行 55 行成对判绿／BW-1、BW-2、BW-5 命中 0／GS-4 PASS 元组 2 在场·κ 报告与 calibration_state 逐元组对账全一致。
4. **产物本体 sha256＋行数留档**（预检时点·供入池批版本审计对拍）＝SKILL.md `731331e26c4f3de3…`（63 行）／registration.md `d6826b4ea94fff7a…`（38 行）；全值＋两跑 assert 输出居仓根 `.scratch/PM-U16/`。对开工 ANCHOR 无并发笔触及本体（本席开工起零写入·推翻④前置对账零触发）。

---

## 一、miyazaki-hayao-perspective 资格读数表（v2·现盘）

| 维 | 读数（现盘实读附路径行号） | 判 |
|---|---|---|
| 1 BW-3 | 现盘命中＝0（§〇-1 明细行逐字）；v1 三处（SKILL.md L6／L59＋registration.md L36）已由 FX-U15 修订笔 `8bddb75` 出清：L59／L36 两发布数字行原地补齐三件套（统计口径＋样本量 25＋一致性系数 κ=0.801887），L6 措辞微动出清误咬（观察-FX4-1 案型·非贴皮＝门禁断言名误咬型随在册口径消解） | **出清坐实**（v1 前置施工清单 M1/M2/M3 全部落地，本席门禁实跑独立复现） |
| 2 EG-6 一手占比 | registration.md L36 登记 `一手占比`=`56.0`（样本量=`25`）≥门槛 `50`＝**过线**；语料落盘侧本席复算对拍＝首批 `agent-skills/fuxi-skill/.collab/evidence/corpus/t9/miyazaki-hayao/` 条目行 17（本人原文 8／第三方转述 9）＋补批 `…/t9/miyazaki-hayao-suppl/` 条目行 8（本人原文 6：C-MH-18/19/22/23/24/25／第三方转述 2：C-MH-20/21）→ 一手 8+6=`14`／分母 17+8=`25`＝**56.0 逐值咬合**；分母形态合规＝甲案全件入样（EG-6 补批采纳面条款：第三方转述 2 条亦入分母·禁按后果选择性采纳），采纳生效点＝封印登记件落账（`agent-skills/fuxi-skill/.collab/receipts/2026-11-07-FUXI-FX-U15-语料批次哈希封印登记-v1.md`·本席独立复算六文件 sha256＋字节数与 §一表六值逐字全等）；闸序＝`git merge-base --is-ancestor 5a434a4 8bddb75` 本席实跑 exit0＝封印在先、修订在后坐实 | **过门槛**（v1 呈裁项 A「EG-6 受限入池与否」随读数随正消解——不再是受限案，无需首案裁） |
| 3 新鲜度窗口 | registration.md L37＋SKILL.md L60 登记落窗（≥2025-10-31）内条目=`7`/`25`；语料侧本席对点＝补批窗内标记逐条 7（C-MH-18/19/20/21/22/23/24）＋窗外如实不计 1（C-MH-25·发布锚 2025-01-01）＋首批 17 条行内发布锚落窗内＝0（grep 2025-10 以后锚＝0 命中）→ 7/8/17 三值咬合、7/25 与登记逐值吻合；条款口径＝EG-6 现版（`agent-skills/fuxi-skill/contracts/evidence-grading.md` L78 参考评分类：读数照登照产、不构成入池资格、不作门禁判据、不触发 FM-S-01、不产生受限行〔裁定源＝皮总新鲜度降参考评分裁定·誊录在册〕）；双案敏感性在册随注（若另裁内容创作日锚＝5/25＝H-3 候补面，登记行内已带） | **参考评分照登**＝非门槛、非受限项（v1 呈裁项 B 随契约落地消解——同型裁已过时，不再呈「受限接受」） |
| 4 κ 校准态 | SKILL.md L16 `calibration_state`=`校准态`（工具现读＝GS-4 PASS·元组 2 在场·软/硬 κ 0.801887/1.0）；对象级校准在册三证（本席实查）＝①`agent-skills/fuxi-skill/.collab/evidence/harness/s0c-anchors-b1/prereg-s0c.json` 预注册四对象集含 `miyazaki-hayao`（语料库哈希＝首批快照 `80d1005beb…`）②`anchor-labels-soft.json` 含 mh- 系列标注单元＝mh-s01..s14 唯一 id 14 个／occurrence 34（硬面 mh- 命中=0 如实）③κ 值 0.801887 三回查位全对＝`anchor-tuple-soft.json` 在册＋SKILL.md L16/L59＋registration.md L36 发布行＋FX-U2 封印件在册；挂账如实＝当期 s0c 标注面未随补批扩批（扩批与否候补挂账在册·L59/L36 句内随行＋封印件 §四在册） | **校准锚链在位**（对象级覆盖＋发布行三件套齐；mrbeast 候裁项 C 先例〔批级锚接受〕本案不需引用——miyazaki 自始对象级在位） |
| 5 版本账 | SKILL.md L13-L15：快照 `2026-10-31`／版本 `v0.2`／复审到期 `2027-01-29`＝快照＋90 自然日（AC-5 规则，`agent-skills/fuxi-skill/contracts/artifact-contract.md` L21）逐字对 | 在场且规则吻合；**快照是否须随语料变更重算＝候皮总 H-2**（台账 D-75＝无在册判据·见 §二事实段，本件不裁） |
| 6 三件套＋test-prompts | 三件齐在；test-prompts 条目 6·字段 ⊆ 注册闭集·期望档位 ∈ 四档词表（ST-4 消费读数绿）；registration 四节 diff=∅（ST-9 绿）；六路 t9 逐路在场（ST-10 18/18）；要素行 55 行成对（FC-3 绿） | FC/ST 面在册判据全绿 |
| 附 三缺位如实 | control_arm=未测／leakage_check=未检／judge 层参考位缺位（SKILL.md L17＋诚实边界节 L63）——同 david／mrbeast 已接受缺位如实态 | 不因批准转绿，如实呈报面（mrbeast 入池确认件附带登记口径在册先例） |

### 1.1 v1 受限项→现态变化表（逐项对照 `bbed4f0` 结论）

| v1 项（2026-11-06） | 现盘态（2026-11-07） | 变化依据（本席实跑坐实） |
|---|---|---|
| BW-3 三处待随批出清（M1/M2 补口径＋M3 措辞微动） | 命中=0·BW-3 PASS | FX-U15 修订笔 `8bddb75` 三处落地＋本席门禁两跑复现 |
| EG-6 47.1（样本 17）＜50＝不过→走 FM-S-01 受限路径 | **56.0（样本 25）≥50＝过线** | 甲案全件入样裁定→suppl 八条封印入分母（采纳生效）→修订改登；语料侧复算 14/25 咬合 |
| 呈裁项 A：EG-6 受限入池与否（首案型） | **消解**——不再是受限案，无需该裁 | 同上（FM-S-01 受限行随撤条件＝「修订后 `一手占比` 读数越过门槛」已成立，`agent-skills/fuxi-skill/contracts/failure-modes.md` L34 现版在册） |
| 新鲜度 0/17＝窗口不过→受限如实（呈裁项 B 先例同型） | **7/25 参考评分照登＝非门槛非受限**（补批 2025-12..2026-09 批入样后读数随正） | EG-6 参考评分条款落地（`agent-skills/fuxi-skill/contracts/evidence-grading.md` L78/L86）＋修订改登；呈裁项 B **消解** |
| 受限态在册（registration L36 受限行＋SKILL L6 受限声明行等五处） | **五处随撤坐实**：现盘「受限」字样 SKILL 3 处／registration 3 处＝全部为随撤语义引用句（L6/L59/L36「受限行随撤」「受限路径随撤」＋L32「随撤`受限`」字样）或质量陈述（SKILL L61「引语措辞精度受限」），grep「受限声明／不达标／走 FM-S-01 受限路径／47.1／0/17」＝**零命中**＝无现受限断言残留 | FX-U15 修订笔＋W-1 措辞纪律在册；本席 grep 实跑 |
| κ 校准＝在位（v1 已判非缺） | 在位不变＋**发布行补登 κ=0.801887**（L59/L36 三件套第三件）＋对象级同锚句按 H-3 david 形判动在册；挂账＝标注面未随补批扩批候补 | 三回查位＋prereg＋mh- 单元本席实查（§一表第 4 行） |
| 门禁汇总 26/1 exit1（BW-3 红） | **27/0/0/27 exit0 全绿** | 本席两跑 cmp 全等独立复现 |
| 版本账 快照 2026-10-31／v0.2／2027-01-29 | 零变更存续；语料已变更而快照未重算＝**H-2 候裁事实**（§二） | SKILL L13-L16 现盘实读；FX-U15 收口「元数据 L13-L16 零触（H-2 未裁禁预动）」在册 |

### 1.2 结论＝够格（入池形态资格达成），候裁项仅 H-2 一项并呈

机械面（27/0/0/27 全绿·BW-3 出清）＋结构面（ST-3/4/9/10·FC-3/6 全绿）＋门槛面（EG-6 56.0 过线·语料侧逐值咬合）＋校准锚链面（对象级在位·κ 三件套发布行齐）四维无任一阻入池项；v1 两受限呈裁项（A/B）已分别随裁定与契约落地消解，v1 前置施工清单（M1/M2/M3）已全部出清——**本席判词＝miyazaki-hayao-perspective 已达入池形态资格，无新候裁项、无受限呈报面**。

- 呈闸内容随之收窄为两项：①入池与否本体裁（人工闸＝皮总，products/README.md §一「人工确认＋独立提案＋版本审计」三前置不变，本席不越权）；②H-2 快照重算与否并案呈（§二事实段供呈，本席不表态）。
- 如实呈报面（不阻资格）＝三缺位如实（control_arm／leakage_check／judge 层）＋新鲜度 7/25 参考读数照呈＋s0c 标注面扩批挂账——三者皆在册如实态，不得读作质量绿，亦不得读作资格红。
- 本席只出预检判词；入池动作（移池／confirmation.md／版本审计）与 H-2/H-3 裁归皮总人工闸＋主理人排期。

---

## 二、H-2 事实段（候皮总裁事项·本席只列事实与两态影响面，不表态）

**事实描述**（现盘实读实跑）：

- 快照四行现盘内容＝SKILL.md L13-L16：`快照时戳`=`2026-10-31`／`版本号`=`v0.2`／`复审到期日`=`2027-01-29`（＋L16 calibration_state 行）；本席 sha256 对拍 FX-U15 修订前后该面零触（修订笔 `8bddb75` numstat＝两文件各 3 增 3 删·写集＝SKILL L6/L59/L60＋registration L32/L36/L37·L13-L16 不在写集）。位置注＝指令文句作「registration.md 元数据面 L13-L16」，现盘实测该四行为 **SKILL.md** L13-L16（registration.md 无快照字段行）；FX-U15 收口与 QA 件「元数据 L13-L16 零触」「SKILL L13-L16 cmp 全等」所指同面，本件按实测位置登记。
- 语料已变更事实＝suppl 补批八条（C-MH-18..25）已经哈希封印入样（封印件落账 `5a434a4`＝采纳生效点·本席六文件 sha 复算全等）；样本集 17→25、两读数随之改登。
- 快照未重算事实＝SKILL.md L13-L15 仍为首批蒸馏快照态；s0c prereg 语料库哈希仍钉首批快照哈希 `80d1005beb…`（补批未随扩批在册）；AC-5 仅有「复审到期＝快照＋90 日」规则，**「语料批次变更是否强制重拍快照/推版本号/重算复审到期」无在册判据**＝台账 D-75 在册（`agent-skills/fuxi-skill/.collab/defects/2026-11-07-FUXI-缺陷台账归因复盘-v1.md` L130·出处 research/R1 §四-3·契约 grep「语料变更|语料批次」零命中实证随账）。

**两态影响面**（照列不裁）：

- 态一＝重算：快照时戳推至补批入样时点→版本号随推（v0.2→随裁值）→复审到期日按 AC-5 随新快照重算；连带＝s0c prereg 语料库哈希与「对象级同锚」句的锚语义（现锚＝首批快照哈希·扩批与否另属 H-3/s0c 扩批票射程 D-69 域）、版本审计链与入池确认版本限定句形态（先例口径＝「限本对象、限本版本」）、本件 §〇-4 本体 sha 留档对拍基线随新笔随正。
- 态二＝保留：快照语义定格＝首批蒸馏快照，补批定性为快照后样本补充动作，全部史实由封印链＋修订链＋登记行承载（现盘即此态）；连带＝复审到期仍＝2027-01-29（基于 2026-10-31）、元数据面不反映语料版次、透明度依赖登记面与封印件对账。

---

## 三、计数口径声明＋关键计数双验

- **口径声明**：occurrence 口径＝字符串出现次数（`grep -o | wc -l`）；行计数口径＝含该串的行数（`grep -c`）；唯一 id 口径＝去重后的 id 集基数；条目行口径＝以 `- C-MH-NN｜` 起的要素立目行。四类口径在本件分别标注、不混用。
- **双验清单**（两独立取法互证）：
  1. 首批条目 17＝逐文件条目行求和（3+4+0+4+2+4）↔ 唯一 id 集 C-MH-01..17 基数 17＝两口径全等。
  2. 补批条目 8＝逐文件条目行求和（0+2+0+4+2+0）↔ 立目唯一 id C-MH-18..25 基数 8＝全等。口径注＝补批目录 grep `C-MH-` 唯一 id 表面＝10，多出两值（C-MH-01/06）居**随行回查注记**非条目立目行，不入分母（与封印件「要素条目数=8」咬合）——此即 occurrence/行计数口径差之实例，如实显形。
  3. 一手 14＝首批本人原文条目行 8＋补批 6（逐条 id 列举复核）；14/25＝56.0＝登记值咬合。
  4. 窗内 7＝suppl 条目行「窗内标记＝窗内」grep 7 ↔ 逐条列举 C-MH-18..24 基数 7；窗外 1（C-MH-25）；首批窗内 0（两取法：条目行 2025-10 后锚 grep＝0 与登记行「首批 17 条无一行内发布锚落窗内」）；7+1＝8＝补批条数闭合。
  5. mh- 标注单元＝occurrence 34／唯一 id 14（两口径并呈；与 QA 件「soft 34 occ」对拍＝occurrence 口径全等）；硬面 mh-＝0（两制同值）。
  6. 「受限」occurrence＝SKILL 3／registration 3（行计数＝SKILL 3 行／registration 2 行——registration L36 行内 2 处，口径差显形）；「随撤」occurrence＝SKILL 2／registration 3。
  7. 门禁基数 27＝汇总总数 ↔ GS-5 断言基数 27 读数行＝两源同值（基数三同源之两源面）。

---

## 四、可推翻项预登记

- 推翻①：若本席 §一-2 语料侧复算与封印件/登记值在**入池开工时点**不再逐值咬合（补批条目被经注记路径剔除/改登＝合法但读数随变），EG-6 判定随读数随正，本表 §1.1 第 2/3 行重出。
- 推翻②：若皮总对 H-2 裁「重算」，SKILL.md L13-L15 将经产物票改登，本件 §〇-4 sha 留档即成历史对拍点，入池批版本审计须对「预检时点本体＝v0.2 快照未重算态」与「闸后本体」两态分别认领。
- 推翻③：若 H-3（新鲜度锚语义）另裁内容创作日锚，新鲜度参考读数 7/25→5/25 随注态转主登态——参考评分非门槛定性不变，不翻转本件资格判定。
- 推翻④：本件开工起若他案并发笔触及两本体件（§〇-4 sha 与入池开工时点不符＝违规情形），开工前置对账即停手上报，本件读数作废重出。
- 推翻⑤：若 s0c 标注面扩批批（D-69 域他票）改动 κ 锚值，发布行三件套 κ 随新锚随正——calibration_state 与 GS-4 对账机制不变，不翻转本件资格判定。

——产品席 pm-fuxi-u16·2026-11-07·除本件外零写入（products/、gates/、contracts/、adapters/、evidence 桶全零触·取证留仓根 `.scratch/PM-U16/` 不 commit·untracked `.collab/ledger/` 零带入）。
