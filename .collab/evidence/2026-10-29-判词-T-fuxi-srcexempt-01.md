# 判词 · T-fuxi-srcexempt-01（sources 双豁免实施·fresh eyes 独立复核）

判席＝qa-srcex（QA 席·独立复算，不采信回执）·2026-10-29。被判件＝工程师回执 `.collab/evidence/2026-10-29-回执-srcexempt-01.md`＋skills commit `95bb1e8`＋devkits commit `d52e873`。真源依据＝devkits 拍板⑧「sources 单立（Q6-续）」双豁免条（已核原文在位：①长度豁免②真名豁免＋配套 STRUCT-2 帽面豁免＋V8 豁免面扩 sources/）。

## 开端三仓 HEAD 读数（复核时实测）

- skills 仓 HEAD＝`95bb1e89ba747dd2f94eae0394b7d298f7a665ff`（与回执一致）；`git status --porcelain`＝空。
- devkits 仓 HEAD＝`d52e8736cc71f0bc3857d707dbb1abdb45628dd3`（与回执一致）；tools/ 面 porcelain＝空。
- experts 仓 HEAD＝`20daf8e`（本票零修改确认）。

---

## 一、结论

**IS_PASS（有条件）·红 0／黄 4**

- 双豁免实施与已决口径一致、豁免面宽度未漏罩镜片正文/deep 件/SKILL 主件（反例实测拦截有效）；sha 链、F-06 对拍读数、run-gates 基线、帽检读数全部独立复算吻合。
- 黄 4 均不拦收口：豁免判定面注记式可伪造（呈报候裁）、证据件未入库沿先例缺口、既有 gate 路由缺口旁注、测试区包 SKILL 索引真名基名残留（另票既定）。

**豁免面宽度一句话判定＝两路实测均守住已决边界：非料源基名＋伪造料源注记的普通件/真镜片件真名照拦（V8 VIOLATION）、超帽照拦（STRUCT-2 BLOCK），豁免只落料源登记件判定面内；但判定面第二式（首三行注记）机械上不排斥镜片件挂注记伪造豁免＝登记候裁。**

---

## 二、复算读数（全部独立重跑／重算，与回执对表）

### 2.1 commit 存在性与 diff 面

| 项 | 回执申报 | 实测 | 判定 |
|---|---|---|---|
| skills `95bb1e8` | 5 files, +23/−18 | 5 files, +23 insertions/−18 deletions（contract-anchors／alias-naming／self-distillation／SKILL.md／.dev 修订账） | 吻合·只动声明文件 |
| devkits `d52e873` | tools/ 两脚本 +30/−9、+22/−6 | `9b07d42..d52e873` 仅 tools/check-truename.py(+30/−9)＋tools/check-pack-structure.py(+22/−6)，零其他文件 | 吻合·词典件零残留 |
| 词典 `check-truename-names.txt` | 对拍临时追加已还原 | 现版无 S8sim 段（大卫芬奇/MrBeast/宫崎骏系 13 词不在盘上词典）·tools/ porcelain 空 | 吻合·还原属实 |

### 2.2 provenance sha 独立重算（按 check-provenance 同款口径：锚行 strip→连续空白压单空格→sha256）

| 块 | 申报 sha | 重算 | 判定 |
|---|---|---|---|
| V8-1（v1.1） | `ae667fa1…` | `ae667fa18c2c88a5…` 锚命中恰 1 | MATCH |
| STRUCT-2（v1.1） | `b9ee0641…` | `b9ee064140339c1e…` 锚命中恰 1 | MATCH |
| STRUCT-1／FACT-1／NAME-1（未触） | 1b0b2748／799061d5／2d459a2b | 三块全 MATCH | 未动确认 |

### 2.3 F-06 对拍读数独立复算

方法＝不采信回执读数，用 QA 自造的词典副本（库工具词典＋S8sim 段合并，落 `qa-probe/tools/` 副本跑，用后删除）重跑现行 HEAD 脚本：

| 面 | 回执申报（改后） | QA 复算 | 判定 |
|---|---|---|---|
| v8-f06/ledger-only | EXEMPT=45·VIOLATION=0·exit0 | EXEMPT=45（全 `EXEMPT(料源登记件·豁免面②)`）·VIOLATION=0·exit0 | 吻合 |
| packs/david-fincher | VIOLATION=2·exit1 | VIOLATION=2·exit1 | 吻合 |
| packs/mrbeast | VIOLATION=1·exit1 | VIOLATION=1·exit1 | 吻合 |
| packs/miyazaki | VIOLATION=2·exit1 | VIOLATION=2·exit1 | 吻合 |

三包残留 VIOLATION 全部落 `SKILL.md:9` 索引标题（`fvx-david-fincher`/`fvx-mrbeast`/`fvx-miyazaki` 拉丁真名基名 fincher/mrbeast/miyazaki，词边界命中）——定位与回执申报一致，非料区非镜片正文。

### 2.4 run-gates 与帽检

- devkits run-gates 全跑：`GATE PASS（发现 479 条）` exit=0·各面 BLOCK=0（check-pack-structure 计数 BLOCK=0 WATCH=52 与回执同集）——479 持平确认，零新增红。（run-gates 自动写 `.collab/evidence/gates/` 快照＝工具既定行为·该目录 gitignore·非真源触碰。）
- skills 包帽检逐件独立重算（script-v1 同款口径）：SKILL 2455／contract-anchors 2216／**alias-naming 2497**／self-distillation 2472＋余六件读数与回执全等，全部 ≤2500。第四式压缩归帽 2497 读数复算属实。
- D-01：SKILL.md frontmatter＝`version: 1.4.1` ✓；tag 链实测：`fuxi-skill@v1.4.0` points-at `5d4d38e`（开工基线读数属实）、`95bb1e8` 上无 tag、盘上无 `fuxi-skill@1.4.1` 半截 tag——「只 commit·tag 随 S8 落包批」口径核实成立。

---

## 三、反例实测结果（豁免面宽度·核心风险项）

探针面＝`qa-probe/probe-pack/`（自造临时包·用后已删除，读数快照留 `qa-probe/probe-v8-reading.txt`、`probe-struct-reading.txt`）：

| 探针件 | 构造 | V8 真名闸预期/实测 | STRUCT-2 帽闸预期/实测（件 token） |
|---|---|---|---|
| `sources-ledger-probe.md` | 料源基名＋【类型：料源存档】·超帽·含真名 | EXEMPT(料源登记件·豁免面②) ✓（基名路） | 3384 不拦 ✓ |
| `forged-tag-lens.md` | **非料源基名**·仅首三行【类型：料源存档】注记·含真名 | EXEMPT(豁免面②)（注记路命中·见四节候裁） | 3393 不拦（同缺口） |
| `method-notes.md` | 【类型：方法论】正文直书真名·超帽·无注记 | **VIOLATION×2→BLOCK** ✓ | 3388>**BLOCK** ✓ |
| `real-lens-lens.md` | 【类型：人格镜片】完整必填节镜片主件·正文直书真名 | **VIOLATION×2→BLOCK** ✓ | 帽内 |
| `dual-tag-lens.md` | 镜片注记＋料源存档注记双挂·超帽·含真名 | EXEMPT（双挂即豁免·见四节候裁） | 不拦（同缺口） |
| 三包 `SKILL.md`（现物） | 索引标题真名基名 | **仍 VIOLATION** ✓（SKILL 主件不被豁免罩住） | — |
| 三包镜片正文/deep 件（现物） | 改闸前有 31/7/12 命中 | 现全清零＝因料件豁免而非扫描面漏扫（EXEMPT 分账逐条可溯） | — |

**判定＝豁免面宽度按已决口径守边成功**：真名豁免只罩判定为料源登记件的件，镜片正文、deep 件、SKILL 主件、方法论卷全部仍在拦截面内；帽豁免同理（非料源件超帽照拦）。**但判定面可被注记伪造**＝任何文件（含镜片件、双标注记）首三行加一行【类型：料源存档】即获真名＋帽双豁免，机械面无缝隙互斥检查（STRUCT-1 对双挂注记不 BLOCK）——按票面要求不自行改，呈报候裁（见四节）。

---

## 四、对工程师遗留登记的确认／推翻＋呈报候裁项

1. **确认**·三包测试区 SKILL.md 索引标题真名基名残留（fincher/mrbeast/miyazaki×2/×1/×2）：独立复现，定位准确，属测试区假想包命名问题，S8 正式落包改名联动处置＝另票合理，不在本票豁免口径内（豁免按文件类型面不扩 SKILL 主件）。**黄-1（挂账性质·非本票缺陷）**。
2. **确认**·判定面两式（基名/首三行注记）存在豁免伪造面：注记式对任意文件生效且不排斥镜片件挂用。已决原文＝「V8 豁免面扩 sources/」；「扩 sources/」是否涵容「首三行注记式」作为第二判定路，或应收窄至基名闭集＋增「镜片注记与料源存档注记互斥」机检——**呈候裁，不自行改**。**黄-2**。
3. **确认**·tag 随 S8 批、D-01 修平（1.4.1）成立（见 2.4）；无遗留。
4. **黄-3（流程缺口·沿先例）**：回执件落 gitignore 区 `.collab/evidence/` 未显式 `-f` 入库（先例 `0931450`＝回执显式 add -f 入仓），`v8-f06/` 对拍读数 14 件＋前后证据未 tracked——回执自述「证据面新增」但仓内不可见（d52e873 diff 只含 tools/）。证据不丢（盘上在位·本次复核已独立复算全部读数），但违仓内回执入仓先例。
5. **黄-4（旁注·超出本票范围·另票）**：复核中发现既有 gate 路由缺口——STRUCT-1 必填节机检只路由 `'persona 镜片'` 注记，中文新注记【类型：人格镜片】件不进必填节检查（条款①文义覆盖「人格镜片件」）。该缺口先于本票存在（不在 d52e873 diff 内），与本票豁免实施无关，登记另票。

---

## 五、红线自查与局限

**红线＝三仓真源零修改**：本席全程只读；写入＝判词（本件·evidence 区）＋`qa-probe/` 反例读数快照（票面指定探针区）；probe-pack 与工具词典副本已删除（`qa-probe/` 仅存 5 个读数件）。run-gates 自动写 `.collab/evidence/gates/` 快照＝门禁既定写面（gitignore·非真源）。skills porcelain 复核后仍空 ✓。

**局限**：
- F-06「改闸前」45×VIOLATION 读数未复跑旧版脚本重验（复算＝改闸后现物全量＋改前读数与回执对表＋脚本 diff 逻辑审读确认豁免面②为唯一新增豁免路，旧行为分支未触）；如需旧版现物重跑＝另议。
- 「首三行注记」伪造面只验了 V8/STRUCT 两闸行为，未验对 FACT-1 豁免面（料源存档件免三态标注）的连带影响——该豁免先于本票存在（fix-01 条款既有），非本票新增面。
- 词典副本合并法（names＋S8sim 段）与工程师「--names 注入/临时并入」两法读词逻辑同路径（load_words 同函数），等效性判断基于脚本审读，非逐字节等同其当时操作。
