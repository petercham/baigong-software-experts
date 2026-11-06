# FUXI-FX-U8 · technique 首单生产票（elements-of-style-technique·B-6 封闭语料人工停点＋ST-10 跨轨咬合候裁停点＋pending 三件套落地）

> 票号＝FX-U8｜起草＝架构席（software-team-architect-u8）｜日期＝2026-11-06｜被派＝**工程师席**（FUXI 线）＋**语料交付停点＝用户**（S2·B-6 人工动作位）＋**候裁裁决停点＝产品席经主理人**（S4·HR-1）
> 起草时点 HEAD 实测＝`d3bc512`（`git rev-parse HEAD` 实跑）；开工 ANCHOR＝开工当轮 HEAD 实测读数，回执开端必附；开工前置对账＝①FX-U7 收口登记已入账（第四段首票·串行令 §七）；②`agent-skills/fuxi-skill/gates/assert-tool.py` 汇总现读＝`PASS=25 FAIL=1 PENDING_STAGE=1 总数=27`·exit 1 且 BW-3 明细＝6 命中全部属 `agent-skills/fuxi-skill/products/pending/miyazaki-hayao-perspective/`（3 处）＋`agent-skills/fuxi-skill/products/pending/mrbeast-perspective/`（3 处）、BW-4 现读＝PENDING_STAGE S1 桩；③selftest 四件基线＝assert-tool 155／s0b-kappa 40／validator-public-anchor 22／validator-source-anchor 19（起草时点实跑反常全 0）；开工读数不符＝停手上报，禁带差开工。status 照登 untracked（`.collab/ledger/`、`.scratch/` 各案目录、`agent-experts/baigong-software-team/.collab/ledger/` 等）与本案无关禁带入；他案 TK-PROJINIT 在途零触碰。
> 账权＝FUXI 项目（拍板㊠）：本票及其封印登记／回执／裁决誊录全部落 FUXI 账域（`agent-skills/fuxi-skill/.collab/`）；百工 bundle 账域与 SWB 仓其他账不入本票射程。
> 来历（自包含，禁指针依赖）：PM-U1 判定件（`agent-skills/fuxi-skill/.collab/research/2026-11-04-FUXI-PM-U1-下一段优先级产品判定-v1.md`）§二第8行「f3 technique 首单·选小对象控范围」＋§三「第四段＝technique 首单＋BW-4 转正」排期在册。产品席 PM-U2 判定件已落账＝`agent-skills/fuxi-skill/.collab/research/2026-11-06-FUXI-PM-U2-technique首单选对象判定与BW4转正签核-v1.md`（commit `65ccedb`·FUXI 账域在册件＝合规指针）：§二判定一＝首单对象《The Elements of Style》（Strunk & White），对象 id＝`elements-of-style`，产物目录名＝`elements-of-style-technique`（1918 初版公有领域全文＝封闭语料默认建议·J-4 方法工具书案型·source-anchor 可锚线过）；落位＝`agent-skills/fuxi-skill/products/pending/elements-of-style-technique/` 三件套（`SKILL.md`＋`test-prompts.md`＋`registration.md`），pending 条目清单行随批增行·轨别列值＝`method`；§2.3 选对象不另设人工闸（判否）——B-6 语料封闭给定本身已把对象确认固化为人类动作点（用户交付/指定封闭文本＝对象的事实确认位）。BW-4 转正随批消费侧口径签核＝同件 §三（随 FX-U9 票面全文登记，本票不重复）；PM-U2 §一在册约束「technique 首单产物不得复制 BW-3 红形态：registration/SKILL.md 内占比类数字必带三件套」。**本票＝第四段首票＝technique 首单产物生产段**；BW-4 离桩转正＝FX-U9 另票（拆分裁定＝§〇-8）。
> **产品签核行（PM §五口径：产物轨首单落地＋扫描面消费形态相关须签）**：产品判定件已在册＝PM-U2 §二判定一（首单对象定名＋落位闭集＋registration 轨别字段＝method＋EG-6 受限口径如实登记不凑档）＋§2.3（不另设选对象闸＋首单完成定义＝产物侧结构检实扫＋source-anchor L1 机械层实跑，VA-S 三臂/诱饵/留出/泄漏/边缘层随 harness 工件到位前一律记未验）（路径＝`agent-skills/fuxi-skill/.collab/research/2026-11-06-FUXI-PM-U2-technique首单选对象判定与BW4转正签核-v1.md`）＝**本票获产品签核（判定形态，非弃权）**。

---

## 〇、复核结论（架构席 2026-11-06 实读实跑实查，票内定稿依据）

1. **断言工具现读实跑**：`agent-skills/fuxi-skill/gates/assert-tool.py` 汇总＝`PASS=25 FAIL=1 PENDING_STAGE=1 总数=27`·exit 1（BW-3 六命中逐处与 FX-U4 收口态在册清单一致，对象＝miyazaki/mrbeast 两产物）；BW-4 挂接位 L1125-1127＝桩行 `return (READ_PENDING, "S1")`；产物级扫描面枚举 `_product_scan_entries()`（L809）现盘条目＝3（david 已入 active 池根＋pending 两条目），本票增 technique 条目后扫描面＝4 条目·正文件 12 件。断言编号闭集 27 三同源面（ASSERTIONS／`GS5_BASELINE`／docstring 计数）本票零碰（无新断言）。
2. **ST-10 跨轨咬合预演实证（架构席 import 现盘代码内存干跑取证，非交付面改动）**：现实现 `six_route_problems()`（L1488）对产物级扫描面**逐条目不分轨**消费 registration「六路采集」声明行（`_SIX_ROUTE_ROW_RE`），声明行缺位＝问题行「缺六路采集声明行」。method 轨采集纪律真源＝`agent-skills/fuxi-skill/adapters/method.md` L10「五路＝定义term路／关键句路／论证链路／实例路／边界条件路，五路各自落盘」——technique 条目 registration 无义务亦不可能写「六路采集」行（写＝不实声明违 FM-S-01）。内存干跑两式均证：①method 案型 registration 文本＋现盘批次基面 → 问题行 `elements-of-style-technique 缺六路采集声明行`；②该对象语料批次假想落盘后 → 同咬（咬合与落盘无关，声明行形态即咬）。**结论＝首单产物入扫描面必触 ST-10 FAIL（汇总变 `PASS=24 FAIL=2 PENDING_STAGE=1 总数=27`）——此红属 ST-10 判据面未区分轨别的越界咬（断言条款本体＝adapters/person.md 六路条款＋FM-S-01 落盘核对，PM-U1 原判词对象＝person 案型），非产物缺陷真红；处置＝断言判据面变更＝产品签核面（PM §五「扫描面枚举变更须签」），PM-U2 签核未覆盖此项——架构席不预裁，列候裁 HR-1（§六），票内设裁决停点（S4）。**
3. **随动读数预演（首单落地后现读变化面逐项）**：
   - ST-3：`产物实例 3 条目·文件 3·节结构 diff=∅` → `产物实例 4 条目·文件 4·节结构 diff=∅`（technique 本体件六段卡头按段名前缀归一化实扫，产物合规前提；`_SEG_HEAD_RE`／`technique_segment_normalize()` L685 复用面现盘已含 technique 分支）；
   - ST-4：`产物条目 3·回归条目 18（逐条目 …=6 三组）` → `产物条目 4·回归条目 24（逐条目 …=6 四组）`（首单 test-prompts 取 6 条与先例同档；`所属轨`＝`method` ∈ `SIDE_TRACKS` L106 在册三值）；
   - ST-9：`registration 随件 3 条目` → `4 条目`（四节闭集 `REGISTRATION_SECTION_CLOSEDSET` L128 轨无关，method 案型同四节名，先例 `agent-skills/fuxi-skill/products/pending/miyazaki-hayao-perspective/registration.md` 同构）；
   - BW-1／BW-2／BW-5(b)：PASS 态读数含扫描计数，`扫描 9 件` → `扫描 12 件`，命中增量必＝0；BW-3＝FAIL 态读数无计数段（明细六命中含行号逐字节不变，扫描面扩面不扰其命中清单）——新三件套零新增硬约束：任何含占比/通过率/% 数字的行必三件套关键词随行（先例绿形态＝`agent-skills/fuxi-skill/products/david-fincher-perspective/registration.md` L36；EG-6 行「一致性系数」关键词以如实措辞随行，method 轨无 κ 元组不造数，见 §二 S3）；
   - FC-3：`产物要素侧要素行 55 行成对判绿` → **55 零变**（要素行判定＝行内同时含 `` `证据等级` ``＋`` `来源态` `` 两反引号 token；technique 卡五字段＝出处/触发/步骤/边界/验证状态不含两 token——产物本体禁写 `证据等级`／`来源态` 两字段名 token，除非行级成对，S3 规格钉入）；卡侧出处成对归 validator L1 管辖非 FC-3 markdown 判据；
   - GS-2／GS-3（S5 validator L1 实跑随动）：GS-2 `method 记录 0 条·空扫描合法态` → `method 记录 7 条·越白名单命中=0（实记录判绿）`（`run_batch()` 每批写 6 层记录 V01-V06＋×5 报告行 V07＝7 条，`validator-source-anchor.py` L365-402 实读）；GS-3 `全量记录 36 条` → `全量记录 43 条·双向不匹配数=0（实记录硬验收判绿）`（36＋7 定值钉值）；GS-1／GS-4／GS-5／FC-6 零变（method 记录 calibration_state＝待校准缺省不入 GS-4 元组面；pending 条目不计 active 池）；
   - ST-10：裁决前必红（§〇-2）；裁决后读数形态随裁决选项（§〇-6），判定列＝PASS 回位为 S6 验收判据。
4. **validator-source-anchor L1 实跑预演**：harness 批次工件目录最小集＝`artifact.json`（产物卡集＋时间切分核对行）；L1 `layer_l1_mechanical()`（L117）＝卡级六段齐备＋五字段非空＋B 段非空＋触发在场＋source_id/位置成对——首单合规卡集 → L1 PASS `卡 N 张·六段＋五字段＋B 段＋触发断言＋出处成对全判绿`；L2-L6 与 ×5 工件缺位 → 记未验（fail-closed 不推定绿，PM-U2 §2.3 首单完成定义在册）；批次汇总＝`PASS=1 FAIL=0 未验=6`·exit 0；`verification-records.jsonl`＋`report.json` 落 harness 注册路径（gitignored 桶）＝GS-2/GS-3 随动消费源。N＝蒸馏卡数，开工实跑照登，禁回执外推。
5. **语料与批次落位设计**：封闭语料批次＝`agent-skills/fuxi-skill/.collab/evidence/corpus/eos-b1/elements-of-style/`（evidence 桶受 `.gitignore` `/**/.collab/evidence/` 制排除，不入 git；FX-U3 归位案同制）；validator 批次工件＝`agent-skills/fuxi-skill/.collab/evidence/harness/eos-b1/`（`_HARNESS_SUBPATH` L216 注册路径内，GS 消费面）；史实锚＝S7 封印登记件（tracked·哈希逐文件·三段分列表形防观察-FX2-1 噪音自增，FX-U3 §〇-7 口径沿用——起草时点 run-gates 实跑现读 `GATE PASS（发现 9708 条）`，开工现读照登对拍，漂移逐数照登＋归因行）。
6. **HR-1 裁决两案形态（供产品席裁，架构席不预裁；推荐案乙，理由＝改动最小＋轨界如实）**：
   - **案甲（判据面豁免）**：`six_route_problems()` 挂接层按目录后缀过滤——`-technique`／`-bundle` 条目不入六路判据面（person 轨条款对象不变）；`agent-skills/fuxi-skill/gates/assertion-catalog.md` ST-10 条目断言内容行加轨界限定句；selftest 增两配（technique 条目豁免放／person 条目存续咬对）＝155→157；ST-10 读数行加豁免注记；**method 轨声明↔落盘一致性机检位空白＝登记观察项随收口（防「料没采齐」在 method 轨重现 T9 黄-1 案型＝届时呈产品段补判）**。
   - **案乙（五路对应检）**：新增 `FIVE_ROUTE_CLOSEDSET`（注册常量单源＝`agent-skills/fuxi-skill/adapters/method.md` L10 五值逐字）＋五路声明行正则；`-technique` 条目按五路口径跑同一「声明↔落盘」骨架（语料批次对象目录逐路 `.md` 在场检）；selftest 增约六配＝155→161；施工面大（新判据面），且五路落盘件形态（提取件 vs 原文分块）无先例钉值。
7. **EG-6／受限口径登记面实读**：EG-6 门槛行先例绿形态＝david L36（三件套齐＋κ 锚）；miyazaki L36 红形态＝缺「一致性系数」关键词随行（BW-3 在册咬）。首单 EG-6 行＝`一手占比门槛`=`50`；`新鲜度窗口月数`=`12`；`一手占比`=`100`（统计口径：封闭语料原文态要素条目数/要素条目总数；样本量=`<实数>`；一致性系数：无——method 轨无软判据层，`calibration_state` 登记缺省值不造 κ）＝门槛过；新鲜度窗口读数＝成书文本按 EG-6 现文照判、受限口径如实登记不凑档（PM-U2 §2.3 钉死）。
8. **拆分裁定（FX-U8／FX-U9 两票串行，理由入票）**：①判据逻辑零重叠（产物生产＋语料＋裁决停点 vs 断言挂接位实装）；②盘面依赖不同（本票双人工停点＝语料交付＋HR-1 裁决，长节奏；U9 零盘面对象依赖、仅验收读数依赖本票产物在扫描面）；③**收口态红性**：两票收口均预期全净（本票收口＝HR-1 裁决落地消除假咬后汇总三态计数与开工基线全等；U9 收口＝BW-4 PENDING→PASS）——拆一票若合一，双人工停点将拖住门禁代码小改的收口节奏，且 QA 独立核验面（产物侧内容检 vs 断言实装配对检）异质；④唯一耦合＝验收读数依赖（U9 验收必须「实扫 N≥1」＝PM-U2 签核「转正批次与首单产物同批」条件本身，以串行令＋U9 开工前置对账消解）＋HR-1 裁决实施落点（实施归 U9 门禁面，断言面改动集中一票）。**结论＝拆两票：FX-U8（产物生产段）先开工，FX-U9（BW-4 离桩转正＋HR-1 随裁）随后；两票票面互引为合规指针（FUXI 账域在册件）。**

---

## 一、声明闭集（本票交付面，git 面恰 6 件＝产物三件套 3＋约定面随动 1＋封印登记 1＋回执 1）

1. 产物本体（新建·能力卡集六段＋卡体五字段）＝目录 `agent-skills/fuxi-skill/products/pending/elements-of-style-technique/`（随批新建）内件 `SKILL.md`
2. 注册随件（新建·四节闭集·轨别字段＝`method`）＝同目录内件 `registration.md`
3. 回归随件（新建·条目 6）＝同目录内件 `test-prompts.md`
4. `agent-skills/fuxi-skill/products/pending/README.md`（条目清单表随批增一行：`elements-of-style-technique/`／`method`／登记快照日；其余文本零动）
5. 封印登记件（新建·史实锚制封印件·FX-U3 封印案同制）＝FUXI 账域 receipts 子域（目录 `agent-skills/fuxi-skill/.collab/receipts/`）内件 `2026-11-06-FUXI-FX-U8-语料批次哈希封印登记-v1.md`
6. 工程师回执（新建·§五规格）＝同 receipts 子域内件 `2026-11-06-FUXI-FX-U8-工程师回执-v1.md`

> 盘面对象（gitignored 桶·不进 commit·哈希入封印件与回执）：`agent-skills/fuxi-skill/.collab/evidence/corpus/eos-b1/elements-of-style/`（封闭语料收讫落位，S1）＋`agent-skills/fuxi-skill/.collab/evidence/harness/eos-b1/`（validator 批次工件＋验证记录＋报表，S5）。
> **`agent-skills/fuxi-skill/gates/` 全树＝零触碰**（断言面零碰：无新断言、基数三同源 27 零动、BW-4 桩零动、ST-10 判据零动——HR-1 实施归 FX-U9）。miyazaki/mrbeast/david 三产物零触；池约定件本体（`agent-skills/fuxi-skill/products/` 内 README 件）零改；adapters／specs／contracts／docs 四子域（均在 `agent-skills/fuxi-skill/` 下）／宿主装载面零触。回执另笔（§五）。

## 二、施工规格（工序序含两停点，落位钉死）

**S0 · 开工前置对账**（§卷头三读数）：U7 收口登记在账＋assert 汇总/BW-4 桩态/selftest 四件基线。不符＝停手上报。

**S1 · 语料封闭收讫停点（B-6 人工动作位·工程师席在此可停手候料）**：封闭语料由用户提供（经主理人转交），默认建议＝《The Elements of Style》1918 初版公有领域全文；用户指定其他版次则以该版封闭收讫。**收讫动作＝语料文本落位语料批次目录（批次名 `eos-b1`／对象目录名 `elements-of-style`，基面＝`agent-skills/fuxi-skill/.collab/evidence/corpus/` 下随批新建）内单一文本件（文件名 kebab·建议 `original-full-text.md`）＋封存时戳登记（hold-out 时间轴 T＝收讫时戳，`agent-skills/fuxi-skill/adapters/method.md` Air-gapped 条款口径）**。语料未收讫＝停手呈主理人（FM-S-01 转人工闸索取语料），**禁凭基座记忆蒸馏开工**。收讫后实算语料 sha256＋字节数，为 S7 封印件对拍基准。

**S2 · 五路提取＋蒸馏工序（method adapter 规程，过程件不落 git）**：先分析阅读产出全书结构总览（过程件落仓根 `.scratch/FX-U8/`），再五路（定义term路／关键句路／论证链路／实例路／边界条件路）并行提取；提取判据＝跨段落佐证（≥2 独立段落，每处 `source_id`＋位置成对回查封闭语料）＋可执行性＋任务效用；能力卡数 N 由蒸馏实况定（N≥1；PM-U1「小对象控范围」纪律，回执照登 N 与逐卡卡名）。

**S3 · 产物三件套落笔（闭集第 1-3 件）**——内容纪律四条（全部对应既有断言口径，逐条可在 §三验收复核）：
- **六段＋五字段形态**：每张卡 H2 节头＝`R 原文`／`I 诠释`／`A1 案例`／`A2 触发场景`／`E 执行步骤`／`B 边界`（裸段名「R」形态亦合法——段名前缀归一化两写法同判，`agent-skills/fuxi-skill/specs/technique-spec.md` 节闭集表口径）；描述名若写须与注册描述名逐字全等；卡体 json 块五字段＝`出处／触发／步骤／边界／验证状态`（`验证状态`＝`未验`，AC-3 未验不进取门禁位）；B 段非空显式适用／不适用边界（B-7 铁律）。
- **BW-3 零新增硬约束**：三件套内任何含 `%` 或「占比／通过率／一致率」形态数字的行，同一行必带「统计口径／样本量／一致性系数」三关键词随行（先例绿形态＝`agent-skills/fuxi-skill/products/david-fincher-perspective/registration.md` L36）。
- **FC-3 要素行零增量硬约束**：产物本体禁写 `` `证据等级` ``＋`` `来源态` `` 双反引号 token 要素标注行（technique 卡形态不含该两字段名；如写则行级 `source_id`＋`位置` 必成对）；卡侧 R 段出处成对纪律随卡体 `出处` 字段＋validator L1 检（§〇-4），非 FC-3 markdown 判据面。
- **词表零命中**：BW-1 角色扮演词表／BW-2 无据斩钉截铁触发词／BW-5(b) 平滑句式词表零命中（产物正文实扫，`agent-skills/fuxi-skill/gates/assert-tool.py` 注册词表）。
- registration 四节＝`注册三元组／分类器四问决策记录／采集与蒸馏声明／语料门槛登记`（节名照 ST-9 注册闭集逐字，先例 `agent-skills/fuxi-skill/products/pending/miyazaki-hayao-perspective/registration.md` 同构）；分类器四问记录＝J-4 方法工具书案型判定轨迹（Q2 否＋Q4 有→分类器输出 `method`；产物轨别字段＝`method`——两词表不同层不互推，PM-U2 注记）；EG-6 行照 §〇-7 钉形（一手占比 100＝封闭语料原文态口径、新鲜度窗口按 EG-6 现文照判受限口径如实登记不凑档）；**「六路采集」声明行禁写**（method 轨无六路义务，写＝不实声明；ST-10 咬合走 HR-1 候裁面，§六）。
- test-prompts.md：条目恰 6（先例同档）；字段 ⊆ `用例id／题面／期望档位／所属轨／是否锚点题`；`期望档位` ∈ 弃权四档；`所属轨`=`method`。

**S4 · HR-1 候裁呈报停点（不阻塞收口）**：ST-10 跨轨咬合（§〇-2 预演实证）随回执附呈候裁单全文（两案形态 §〇-6＋架构席推荐案乙与理由），经主理人转产品席裁；**工程师席／架构席不得自行实施豁免或改判据**（裁决权＝产品席，PM §五扫描面变更须签口径）。裁决前本票可收口，收口登记件含「ST-10 假咬红在册·处置随 FX-U9 随裁」指针行（FX-U4 §三-6 红账随批先例体例）。

**S5 · validator-source-anchor L1 实跑（机械断言层产物级实证）**：生成段将卡集落 harness 注册路径下批次目录 eos-b1（目录 `agent-skills/fuxi-skill/.collab/evidence/harness/eos-b1/`，随批新建）内工件件 `artifact.json`（`cards` 卡集＋时间切分核对行含收讫时戳 T）；判分段实跑 `python agent-skills/fuxi-skill/gates/validator-source-anchor.py` 对批次目录 `agent-skills/fuxi-skill/.collab/evidence/harness/eos-b1/`（其余七工件缺位＝对应层记未验，fail-closed 不造工件凑绿——PM-U2 首单完成定义在册）。预期批次读数＝`PASS=1 FAIL=0 未验=6`·exit 0；L1 明细＝`卡 N 张·六段＋五字段＋B 段＋触发断言＋出处成对全判绿`；验证记录件 `verification-records.jsonl`（7 条 method 记录 V01-V07）＋报表件 `report.json` 落同批次目录＝GS-2/GS-3 随动消费源（§〇-3）。

**S6 · 验收全跑**（§三逐条实跑，连跑两次对拍）。

**S7 · 封印登记件**（闭集第 5 件）：五节＝①登记头（开工 ANCHOR／落账 HEAD 由回执承载）；②语料落位逐件表**三段分列**（批次列 `eos-b1`／对象目录列 `elements-of-style`／文件名列＋sha256＋字节数——FX-U3 §〇-7 观察-FX2-1 噪音规避条款沿用）；③封印复验命令（sha256 逐件重算对拍口径逐字入册）；④validator 批次工件哈希指针（`_dir_artifact_hashes` 口径工件集哈希值照登，gitignored 侧锚）；⑤修订注记行。

**工序序＝S0→S1（语料停点）→S2→S3→S5→S7→S6→S4 呈报并入回执→回执笔。commit 计划＝三笔（闭集）：①封印件笔；②产物三件套＋pending README 行笔（恰 4 件）；③回执笔。此外零 commit。**

## 三、验收判据（三态禁假绿，全部可机械验证；钉值守恒＝PASS+FAIL+PENDING=总数自查入回执）

1. **ST-10 假咬钉值（如实红在册，裁决前收口态）**：明细行逐字 `ST-10 FAIL 六路声明↔落盘违例：elements-of-style-technique 缺六路采集声明行`（＝§〇-2 内存干跑预演取证值）；连跑两次逐字节全等。
2. **汇总读数钉值（U8 收口态）**：汇总行逐字 `PASS=24 FAIL=2 PENDING_STAGE=1 总数=27`·exit 1（开工基线 `PASS=25 FAIL=1 PENDING_STAGE=1 总数=27` 的 delta 仅 ST-10 一项 PASS→FAIL；四元守恒自查 24+2+1=27 ✓；FAIL=2＝BW-3 六处红账存续＋ST-10 假咬，两红账处置分别随入池批／FX-U9 随裁）；**禁为凑绿给 registration 写六路行**（不实声明违 FM-S-01＝整批退回）。
3. **产物侧随动钉值**：ST-3 明细 `产物实例 4 条目·文件 4·节结构 diff=∅（实产物判绿）`；ST-4 明细 `产物条目 4·回归条目 24（逐条目 …=6 四组）`（新增组名＝`elements-of-style-technique=6`）；ST-9 明细 `registration 随件 4 条目·节闭集 diff=∅`；BW-1／BW-2／BW-5(b) 扫描计数 `扫描 12 件` 且命中增量=0；BW-3 明细六命中清单含行号逐字节不变（FAIL 态读数无计数段，扩面不扰）；FC-3 明细 `产物要素侧要素行 55 行成对判绿` **零变**（§〇-3）。
4. **validator L1 实跑钉值**：批次汇总 `PASS=1 FAIL=0 未验=6`·exit 0；L1 明细行卡数 N ≡ SKILL.md 实卡数 ≡ artifact.json 卡集条数三处对拍全等；`verification-records.jsonl` 恰 7 条全部 `所属轨`=`method`；连跑两次逐项读数全等（判分段确定性）。
5. **GS 随动钉值**：GS-2 明细 `method 记录 7 条·越白名单命中=0（实记录判绿）`（空扫描合法态字样消失＝method 轨验证记录产物级实证首例）；GS-3 明细 `全量记录 43 条·双向不匹配数=0（实记录硬验收判绿）`（36+7 定值对拍）；GS-1 `person 记录 36 条`／GS-4 `元组 2 个在场`／GS-5 基数 27／FC-6 `active 池条目 1`＝四行逐字节零变化。
6. **语料锚线抽查实证**：回执抽三张卡 R 段引文，逐字在封印语料件内命中（grep 逐字回查读数照登）＋卡 `出处` 字段位置指向收讫版实际位置（source-anchor 可锚线过＝PM-U2 资格线产物级复核）。
7. **其余断言零碰对账**：除判据 1/3/4/5 列明项外，其余明细行与开工基线逐字节零变化（含 ST-1/2/5/6/7/8、BW-4 PENDING 桩行原文、BW-6、FC-1/2/4/5、ST-10 之外的产物级断言）。
8. **run-gates 基线零新增红**：exit 0·`GATE PASS`；与开工基线对拍无 BLOCK 无新增红；指针族 WATCH 漂移逐数照登＋归因行（FX2-1 口径；起草时点实跑现读 `GATE PASS（发现 9708 条）` 照登备对）。
9. **碰面闭合**：三笔 `git show --name-only` 并集 ≡ §一 6 件；`git diff` 对 `agent-skills/fuxi-skill/gates/` 全树／三产物全树／`agent-skills/fuxi-skill/products/README.md`／`agent-skills/fuxi-skill/contracts/`／`agent-skills/fuxi-skill/adapters/`／`agent-skills/fuxi-skill/specs/`／`agent-skills/fuxi-skill/docs/`／`.gitignore`＝零改动；evidence 两桶零 tracked。

## 四、禁动面（违任一＝整批退回）

- **B-6 铁律**：语料未收讫禁开工蒸馏；基座记忆补全＝泄漏面整批退回；语料中途换版＝回 S1 重封印＋回执申报。
- **gates/ 全树零触碰**：ST-10 豁免／BW-4 装桩／任何判据调整不入本票（HR-1 实施归 FX-U9）；断言闭集 27／基数三同源零碰。
- **registration 禁写「六路采集」行**（不实声明凑绿）；四节节名逐字照注册闭集。
- **既有三产物本体零触**；miyazaki/mrbeast BW-3 红账不清（随入池批）；david 入池态零扰动（FC-6 `active 池条目 1` 读数零变）。
- **凑绿三禁**：禁写六路行凑 ST-10 绿（不实声明）；禁造 harness 缺位工件凑 L2-L6 绿（未验如实＝PM-U2 首单完成定义）；禁给 EG-6 新鲜度窗口造数凑档（受限口径如实）。
- **evidence 两桶不入 git**：`git add -f` 任何 evidence 桶文件＝违治理原则整批退回；`.gitignore` 零改动。
- **两账域史账不随正**；已裁项不回流；宿主装载面／他案面（TK-PROJINIT 等）零触碰。

## 五、回执要求

工程师回执件（新建）＝FUXI 账域 receipts 子域（目录 `agent-skills/fuxi-skill/.collab/receipts/`）内件 `2026-11-06-FUXI-FX-U8-工程师回执-v1.md`：开工 ANCHOR 实测 HEAD＋§卷头前置对账行；语料收讫陈述（交付人／收讫时戳／版次声明／sha256）；卡集清单（N 张逐卡卡名）；§三九判据逐条实跑读数全文（ST-10 假咬明细＋汇总三态＋四元守恒自查表 `24+2+1=27`＋随动钉值对拍表＋validator L1 批次读数与三处卡数对拍＋GS 随动钉值＋锚线抽查三卡 grep 读数＋零碰对拍白名单表＋run-gates 照登归因）；S4 候裁呈报陈述（呈报时间／候裁单全文随附）；三笔 commit 清单；§〇 复核不一致处如实申报。

## 六、候裁单列

- **候裁 HR-1（本票唯一候裁·真·未裁对立分歧）**：ST-10 六路声明↔落盘判据现实现不分轨，technique 条目入扫描面必咬「缺六路采集声明行」（§〇-2 内存干跑两式实证）——对立＝「产物合规但断言越轨界咬合」vs「断言面改动属产品签核面」（PM §五扫描面枚举变更须签口径）。两案形态＝§〇-6 案甲（后缀豁免＋观察登记）／案乙（`FIVE_ROUTE_CLOSEDSET` 五路对应检）；架构席推荐案乙（method 轨声明↔落盘机检位不留空白，防空池式盲区），**裁决权＝产品席（经主理人），实施落点＝FX-U9**（门禁面集中随裁＋随 BW-4 同文件链）。裁决前本票带假咬红收口（红账指针行体例＝FX-U4 §三-6）。
- 除此无候裁：首单对象定名／落位／EG-6 受限口径均 PM-U2 判定件在册已决；选对象不另设闸＝PM-U2 §2.3 判否在册。

## 七、纪律

一票一批三 commit（§二 commit 计划闭集）；**串行令＝FX-U8 开工前置＝FX-U7 收口登记入账**；FX-U9 开工前置＝FX-U8 产物落地在扫描面（U9 验收「实扫 N≥1」依赖）＋HR-1 已裁或未裁均可（U9 票面按裁决落地／带豁免实施两态自适）；互不越面＝本票零碰 `agent-skills/fuxi-skill/gates/` 全树（断言面归 U9），U9 零碰 `products/` 全树。QA 席独立核验另票另件，fresh eyes 全实跑：§三判据逐条复现＋对抗例钉死——**对抗一（假咬非虚报）**：scratch 复制产物条目并补「六路采集」声明行→ST-10 对复制条目转放（证咬合确由声明行形态触发，注入面复原零残留）；**对抗二（凑绿检出）**：registration 补写六路行→复跑必现该条目批次落盘不在场二次咬（不实声明双咬面＝禁凑绿实证）；**对抗三（validator 确定性）**：判分段连跑两次逐字节全等＋删 artifact.json→L1 未验汇总 `PASS=0 FAIL=0 未验=7`·exit 0（fail-closed 不推定绿）；**对抗四（BW-3 零新增复核）**：三件套逐行 grep 占比/通过率/% 形态行，逐行核三关键词随行。临时工作物只落本仓根 `.scratch/FX-U8/`；复现门禁基线禁用只读 worktree（教训在册），用仓根现盘态。

——架构席 software-team-architect-u8 起草·2026-11-06·除本票面外零写入。