# 判词 · T-fuxi-pres8-fix-01（S8 前置修复·fresh eyes 独立证伪）

判席＝qa-pres8（QA 席·独立复算＋自造反例，不采信回执）·2026-10-29。被判件＝工程师回执 `.collab/evidence/2026-10-29-回执-pres8-fix-01.md`（已读）＋skills `dbce846`＋devkits `e422ca2`。修复对象判词＝`.collab/evidence/2026-10-29-判词-T-fuxi-srcexempt-01.md` 黄项段（已读·黄-2/黄-4 为整改输入）。

## 开端三仓 HEAD 读数（复核时实测）

- skills 仓 HEAD＝`dbce84681283fbecc92433efe383d006876dcc16`（与回执一致）；`git status --porcelain`＝空。
- devkits 仓 HEAD＝`e422ca216d16764f9a8d561c7a9ec1735bac7e26`（与回执一致）；tracked 面 porcelain＝空。
- experts 仓 HEAD＝`20daf8ed61785bca8dc957e983231870d14b8ae1`；porcelain 仅历史 untracked（`.collab/`/`.workbuddy/`）＝本票零触碰确认。

---

## 一、结论

**IS_PASS · 红 0／黄 3（＋挂账黄-1 在位确认）**

- 黄-2 互斥机检两闸同判据落地、口径一致；黄-4 中文/英文路由双向实测进检；N 系级联/占比/分账全部独立复算对位；sha 链、479 门禁、帽检、F-06 对拍、黄-1 未动全部复算吻合。
- 黄 3 均不拦收口（见四节）：互斥＝纯形态信号判定，藏形态/挪注记位仍可得注记豁免（探针实测＝**互斥机检可再伪造**，但残面与条款文本所定判定面同界）；基名闭集主判定优先之下「基名＋frontmatter 伪装镜片」件整件豁免（行为如实登记）；K-B5 断言列四引语 vs 级联 17 处靠行末包句（枚举不全·候补另票）。

**互斥机检可否再伪造一句话＝可（形态规避路）：件名去 lens/镜片＋不挂镜片类注记＋frontmatter 无「镜片」三信号全隐时，镜片正文挂【类型：料源存档】仍获 V8＋帽双豁免（探针 h 实测 EXEMPT）；镜片注记挪到第四行亦绕过互斥（探针 i 实测 EXEMPT）。惟此即条款文本自身所定判定面（件名/首三行注记/frontmatter）之极限，实现与文本一致，非实现缺陷。**

---

## 二、复算读数（全部独立重跑／重算，与回执对表）

### 2.1 commit 存在性与 diff 面

| 项 | 回执申报 | 实测 | 判定 |
|---|---|---|---|
| skills `dbce846` | contract-anchors 1 文件 1 行 | 1 file, +1/−1（MC-FX-V8-1 豁免句行）；frontmatter 未 bump（1.4.1）、无新 tag | 吻合·只动声明文件 |
| devkits `e422ca2` | tools 两脚本＋测试区 packs/gates＋证据十件 | `6bdcc96..e422ca2`＝tools/check-truename.py(+46面)＋check-pack-structure.py(+34面)＋测试区 packs 五件＋gates.md＋qa-probe 读数 4 件＋v8-f06 读数 6 件＋回执 1 件＝18 文件 | 吻合·三包 SKILL.md 与其他真源零入 diff |
| 判定面单实现 | skills 仓无 scripts/ | skills 仓 find 无 check-truename/check-pack-structure 副本＝两闸仅 devkits tools/ 一处，无双实现漂移 | 属实 |

### 2.2 provenance sha 独立重算（同款口径：锚行 strip→连续空白压单空格→sha256）

| 块 | 申报 sha | 重算 | 判定 |
|---|---|---|---|
| V8-1（v1.2） | `8f64e1a1664291f1…` | `8f64e1a1664291f150159a4dcaaf08c4b45d791e8ed099ef461d63062de30e03` 锚命中恰 1 | MATCH |
| STRUCT-1（v1.0） | `1b0b2748…` | 现算 `1b0b27485847b91b…` | 未动确认 |
| STRUCT-2（v1.1） | `b9ee0641…` | 现算 `b9ee064140339c1e…`（帽面豁免句文本未动·互斥随 V8-1 联动经「判定同 V8-1 豁免面②」引用生效） | 未动确认 |

check-provenance 实跑：--target 两件 exit=0；默认域全量 exit=0 ✓。

### 2.3 门禁回归

- devkits run-gates 全跑（QA 现跑）：**GATE PASS（发现 479 条）exit=0**·各面 BLOCK=0 持平（check-truename 默认面 EXEMPT=39 SUBSTR=8 VIOLATION=0；check-pack-structure BLOCK=0 WATCH=52 同集）✓
- skills 仓薄启动器 `tools/run-gates.sh`：exit=0（SOT=0 V8=0 STRUCT=0）✓
- check-blind-eval 接口模式（N-02 依据独立复跑）：BLOCK=0 WATCH=1 **exit=1** ✓＝gates.md §六 勘误（exit=0→1）成立；run-gates 路由②advisory 不拦＝两读数不矛盾属实。
- V8 对三包现物（现行词典）：三包 exit 全=0·全零命中 ✓（基名词典外词现词典不命中口径不变）。

### 2.4 帽检级联后读数独立复算（script-v1 同款口径）

12 件全 OK：fincher `325/1292/1647/1998`｜miyazaki `318/1332/1701/2395`｜mrbeast `323/1559/1193/1601`——与回执 `caps-pres8fix-after.txt` 逐件全等；主件微增＝级联注记字数、全部 ≤2500 ✓。

### 2.5 F-06 对拍独立复跑（QA 自造词典副本＝库工具词典＋S8sim 段合并，跑现行 HEAD 脚本）

- ledger-only 三台账：EXEMPT=45·VIOLATION=0·exit=0 ✓（互斥机检未伤真料源件）
- 三包 S8sim 词典下：fincher VIOLATION=2／mrbeast=1／miyazaki=2·exit=1，VIOLATION 全部落 `SKILL.md:9`（fincher/mrbeast/miyazaki 基名词边界命中）＝黄-1 残留定位复现 ✓

---

## 三、探针实测结果（QA 自造九件·`qa-probe/fix02-probe-pack/`·用后已删，读数快照留 `qa-probe/fix02-reading-{v8,struct,ledgeronly}.txt`）

词典＝现行真词典（斯皮尔伯格在册），填体＝超帽真名复读体（每件 ~400 次真名命中）。

| 探针件 | 构造 | V8 实测 | STRUCT 实测 | 判定 |
|---|---|---|---|---|
| a `fix02-forged-note-lens.md` | 非基名＋仅【类型：料源存档】注记＋件名含 lens＋超帽含真名 | **VIOLATION×401→BLOCK** ✓ | **STRUCT-2 BLOCK 4830>2500** ✓ | 双拦 ✓（票项 1a） |
| b `fix02-forged-fm.md` | 非基名·件名无 lens·frontmatter description 含「镜片」＋料源注记 | **VIOLATION×401→BLOCK** ✓ | **STRUCT-2 BLOCK 4839** ✓ | frontmatter 形态路互斥生效 ✓ |
| c `fix02-dual-tag.md` | 人格镜片＋料源存档双挂·超帽·缺必填节 | **VIOLATION×401→BLOCK** ✓ | **STRUCT-2 BLOCK＋STRUCT-1 必填节 BLOCK×8**（含 exemplars） ✓ | 双挂件互斥生效＋进结构检 ✓（票项 1b） |
| d `fix02-cn-lens-missing.md` | 中文【类型：人格镜片】首三行·缺必填节（帽内） | VIOLATION=0（无真名·不进豁免争议） | **STRUCT-1 必填节 BLOCK×7**（stance/traits/taboos/audience_contract/performance/meta＋exemplars 均未见） | 黄-4 修复达成·复跑读数在位 ✓（票项 2） |
| e `fix02-en-lens-missing.md` | 英文【类型：persona 镜片】首三行·缺必填节 | — | **STRUCT-1 BLOCK×7** 同款 | 英文路由不回归 ✓（票项 2） |
| f `sources-ledger-fix02.md` | 纯基名料源件·超帽·含真名 | **EXEMPT×400 不变** | 帽面豁免（无帽 BLOCK；仅 WATCH 缺类型注记·沿例） | 基名闭集豁免未回归 ✓（票项 1c） |
| g `sources-ledger-disguise.md` | **边界**：基名命中＋frontmatter 伪装镜片（description 含「人格镜片」） | **EXEMPT×401**（基名闭集主判定优先＝互斥不触基名路） | 帽面仍豁免（仅 WATCH） | **现行为登记＝基名路优先豁免**·与条款「主判定·基名闭集」字面一致；不判对错 ✓（票项 1d） |
| h `fix02-hidden-piece.md` | **自造反例**：镜片正文内容·三形态信号全隐（件名无 lens/镜片、无 frontmatter、注记仅料源存档） | **EXEMPT×401**＝豁免到手 | 帽面豁免（WATCH 缺类型注记 advisory·不拦） | **互斥可再伪造＝形态隐藏路**（见四节黄-A） |
| i `fix02-tagline4.md` | **自造反例**：料源注记落第 1 行＋persona 镜片注记落第 4 行（首三行外）＋件名无 lens | **EXEMPT×401** | 帽面豁免 | **互斥可再伪造＝注记落位路**（同根·黄-A） |

分账总读数：V8＝EXEMPT 1604（4 件）／VIOLATION 1203（3 件）·exit=1；STRUCT＝BLOCK=25 WATCH=5·exit=1（含探针外历史区 FACT-1 WATCH×3 常驻）。

**文本口径 vs 实实现一致性**：条款互斥句〔件名含 lens/镜片 或 frontmatter description 含「镜片」或挂镜片类类型注记〕与两闸实现逐路对照——①注记扫描面＝首三行（条款「挂注记」未写位置＝按注记体例首三行实施，探针 i 证位置可避）；②frontmatter 检查实现比文本宽（扫块内任意行含「镜片」，止于前 20 行，非仅 description＝实现严于文本，无害登记）；③两闸 is_lens_piece/is_lens_piece_form 代码同款＝口径一致 ✓。互斥只对注记式生效、基名闭集不受影响——与条款「主判定·基名闭集」一致（g 件实证）。

---

## 四、遗留登记与候裁（黄项）

1. **黄-A（互斥残面·候裁）**：互斥机检＝纯形态信号三件套（件名/首三行注记/frontmatter），探针 h（全隐形态）与 i（注记挪第四行）实测均获双豁免。条款文本自身即以此三信号为判定面＝实现与文本零偏差，残面属口径边界非实现缺陷；若要更严（全篇扫【类型：…】注记／扫正文镜片自述语）须先改条款再改脚本。**呈候裁，不自行改。**
2. **黄-B（基名路边界·登记不判）**：基名闭集主判定优先→`sources-ledger-disguise.md`（基名＋frontmatter 伪装镜片）V8 全 EXEMPT＋帽面豁免＝现行为如票面所问「基名闭集主判定优先＝豁免」属实。残余伪造面＝改基名即可获豁免——但改基名即失闭集＝料源纪律问题（料源件按命名体例恒基名），机械面不再叠加判定，登记行为。
3. **黄-C（K-B5 覆盖面·候补另票）**：级联 17 处旗全部指向台账 K-B5 行（行真在位、三态〔存疑待核-降级〕与旗语义一致）；但 K-B5 断言列只枚四引语（algorithm→audience／10M>100×100k／comment section 烂／coachable），其中 coachable 正文无对应（未用·无害），而「做尽可能好的视频」「100 条改进法」「倒推物流」「头脑风暴」等正文级联处不在四引语枚举内——覆盖面靠行末「正文该批 B04 引语旗已按本行级联改旗」包句支撑。语义成立但枚举不全，建议另票补全 K-B5 断言列或改行末为显式清单。**不判错。**
4. **挂账确认（黄-1·按票禁动）**：三包 `SKILL.md:9` 真名基名残留（fvx-david-fincher/fvx-mrbeast/fvx-miyazaki）在位未动＝S8 落包改名联动另票 ✓；现词典下三包 V8 exit=0 不变、S8sim 词典下 2/1/2 定位不变（见 2.5）✓。
5. **回执证据小疵（登记）**：`v8-f06/provenance-pres8fix-after.txt`＝0 字节——check-provenance exit=0 时零输出，空文件＝无发现行的通过记录，逻辑成立但读数未注记；不影响判定。

## 五、N 系级联/分账独立复算明细

- **N-01 mrbeast 17 处级联**：改前基线（`6bdcc96` 版）〔已核实·B04〕＝主件 8 行＋混合 M4 行（B03/B04）＋deep 8 行；改后〔已核实·B04〕残留 grep＝0 ✓。抽 5 处核：main:18（algorithm→audience＝K-B5 枚举引语 ✓）、main:36（comment section 烂 ✓）、deep:32（10M>100×100k ✓）、deep:42（引语形态标签〔存疑待核-降级·K-B5 引语「标题必须配得上时长」〕与 deep 侧语义自洽 ✓）、main:21（M4 行 B03 侧〔已核实·B03〕保留＋B04 侧降级注 ✓）。B03 侧未误伤：main:20/33/34/39、deep:20/22/27、main:21 B03 侧全部〔已核实〕原旗在位 ✓；〔存疑待核〕B08→料降级行未动 ✓（覆盖面见黄-C）。
- **N-04 fincher**：meta「在盘一手 1/13≈8%（含候补 3/15≈20%；一手在盘＝C04，候补＝C05/C13）」与台账一节末行逐字对位；分母复算＝C01–C14 共 14 occurrence − C11 线索图＝13 ✓；候补口径 3/15＝(1+2)/(13+2) 自洽 ✓；指针「五节」对位（三件套住五节）✓。
- **N-05 miyazaki**：meta「1/11≈9%（一手在盘＝C-M2 AWN 问答全文）」与台账一节末行对位；分母复算＝C-M1–C-M12 共 12 occurrence − 1＝11（C-M7 链计 1 口径·台账一末行自洽）✓；C-M2 行三态＝一手在盘真在位 ✓。
- **N-06 分账拆分独立逐行复算（每行取首标）**：fincher 总 14＝已核实 3＋双值 1（K12）＋存疑 3＋降级 7（我的脚本把 K12 计入已核实＝纯核实 3＋双值 1 合并读法一致）✓；mrbeast 总 8＝已核实 2＋存疑 4＋降级 1＋料降级 1（K-B8）＝加和 8 ✓；miyazaki 总 21＝已核实 10＋存疑 8＋降级 3（K-M2/M19/M21 三行枚举补全实见）✓。总数 14/8/21 不变 ✓。
- **N-02/N-03**：gates.md §六 exit=1 实跑复现（2.3）✓；K-B5 交叉引用 F-02 指向 report.md 摩擦表 F-02 真在位（A3 灰区条）✓。

## 六、红线自查与局限

**红线＝三仓真源与 packs 零修改**：本席全程只读＋判词（本件）＋探针区写入（`qa-probe/fix02-probe-pack/`＋`fix02-tools/` 词典副本·用后已删，只留三份读数快照 fix02-reading-*.txt）；复核后 skills porcelain 仍空、devkits tracked 面 porcelain 空、experts 仅历史 untracked。run-gates 自动写 `.collab/evidence/gates/`＝门禁既定写面（非真源）。✓

**局限**：
- 「改前」读数未重跑旧版脚本（与回执对表＋`6bdcc96` 版文件 git show 对读确认级联前后旗数变化＝8+8+1 形态一致）；
- 探针填体＝复读体真名，token 形态与真文有差（帽闸只数 token，不影响判定）；
- 词典副本合并法与工程师操作等效性同前票局限（load_words 同函数路径）。
