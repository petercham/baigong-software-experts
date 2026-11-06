# FUXI-FX-U6 · david-fincher-perspective 入池提案 v1

> 票号＝FX-U6｜工序＝S1 独立提案件（票面 §二 S1·闭集第 6 件）｜日期＝2026-11-06｜提案席＝工程师席（FUXI 线·FX-U6 票内新鲜实例）
> 性质＝入池前置三件套之「独立提案」件（池规程真源＝`products/README.md` §一「入池前置：写入本池必须经人工确认＋独立提案＋版本审计」）。本件不是确认件；确认权在皮总（S4 人工闸）。

## ① 提案头（独立性声明）

- 提案席＝工程师席；确认人＝皮总（主理人呈）——**提案人≠确认人**，独立性声明成立。
- 本席职责边界＝把资格读数、受限态、缺位面如实备齐到「一句话可批」强度；不代签、不预填任何人工确认引用（票面 §四「人工闸不可代位」条款遵守声明）。
- 开工 ANCHOR＝`b813207`；本件写作时点门禁读数＝ANCHOR 态实跑（`.scratch/FX-U6/assert-run-HEADb813207.txt` 留档，run 内逐字节对账）。

## ② 入池对象与轨别

| 字段 | 值 | 出处 |
|---|---|---|
| 产物id | `david-fincher-perspective`（与目录名逐字全等） | 产物 SKILL.md 元数据节 L9 |
| 所属轨 | `person` | 同上 L10 |
| 编译形态 | `single` | 同上 L11 |
| 版本号 | `v0.2` | 同上 L13 |
| 快照时戳 | `2026-10-31` | 同上 L12 |
| 复审到期日 | `2027-01-29` | 同上 L14（＝快照＋90 日，本席实算 `datetime(2026,10,31)+90d＝2027-01-29` 逐字对上） |
| 当前落位 | `products/pending/david-fincher-perspective/`（待确认暂存区） | 现盘实查 |
| 拟入落位 | `products/david-fincher-perspective/`（active 生效池根） | 池规程 §一 |

## ③ 门禁现读全文引用（assert-tool 27 项明细·当期读数照录）

开工 ANCHOR 态实跑（exit 1），逐行照录：

```
ST-1 PASS 主契约面在场·json 可解析·AC 节闭集 diff=∅
ST-2 PASS 三件在 contracts/ 实体·节闭集 diff=∅（EG6/FM5/AC5）
ST-3 PASS 产物实例 3 条目·文件 3·节结构 diff=∅（实产物判绿）
ST-4 PASS 产物条目 3·回归条目 18（逐条目 david-fincher-perspective=6／miyazaki-hayao-perspective=6／mrbeast-perspective=6）·字段闭集＋档位/轨取值判绿（实产物判绿）
ST-5 PASS 批次 0·审计件 0·条目 0（空 listing 合法）
ST-6 PASS person 面无「执行步骤」段字样·命中=0
ST-7 PASS method 面无「表达 DNA」段字样·命中=0
ST-8 PASS 两规范表在场·四节闭集 diff=∅·关键引用行（AC-1/总则声明行/AC-2/VA-S-01）在场
ST-9 PASS 产物实例 registration 随件 3 条目·节闭集 diff=∅
ST-10 PASS 产物实例 3 条目·批次 t9 逐路存在性检 18/18 在场（实扫描判绿）
BW-1 PASS 词表条目 5·产物正文实跑命中=0（扫描 9 件）
BW-2 PASS 触发词 5·档位 4·产物正文实跑命中=0（扫描 9 件）
BW-3 FAIL 产物报告裸数字 6 处（三件套=统计口径＋样本量＋一致性系数·缺任一即裸）：miyazaki-hayao-perspective/SKILL.md line6 缺统计口径、样本量、一致性系数；miyazaki-hayao-perspective/SKILL.md line59 缺一致性系数；miyazaki-hayao-perspective/registration.md line36 缺一致性系数；mrbeast-perspective/SKILL.md line34 缺统计口径、样本量、一致性系数；mrbeast-perspective/SKILL.md line62 缺一致性系数；mrbeast-perspective/registration.md line36 缺一致性系数
BW-4 PENDING_STAGE S1
BW-5 PASS (a) 声明行两行在场·(b) 词表 4 值本体在场·产物面命中=0（扫描 9 件·实扫描判绿）
BW-6 PASS 对照表先于首个二级标题·两工具名＋本线列名命中·声明行命中=1·三维度行名齐备
FC-1 PASS 两字段名在注册面·两值闭集与契约声明逐字全等
FC-2 PASS 注册表 26 字段·双向 diff=∅·实例⊆注册·FM条目纪律·值互洽全等
FC-3 PASS 契约 json 实例 2 条成对判绿·产物要素侧要素行 55 行成对判绿（实要素行判绿）
FC-4 PASS 词表六值·三栏名声明 AC-5·词表声明句逐字全等·看板目录空（合法）·看板状态token扫描判绿
FC-5 PASS bundle 实例 0 条·命名空间互借检出=0（配对咬放实证见 selftest）
FC-6 PASS active 池条目 0·无人工确认来源条目数=0（空池平凡真·规程级实证非产物级）
GS-1 PASS person 记录 36 条·越白名单命中=0（实记录判绿）
GS-2 PASS method 记录 0 条·越白名单命中=0（空扫描合法态·配对咬放见 selftest）
GS-3 PASS 全量记录 36 条·双向不匹配数=0（实记录硬验收判绿）
GS-4 PASS 元组 2 个在场·κ 报告与 calibration_state 逐元组对账全一致（判据本体零改动）
GS-5 PASS 层名11·白名单6+6·断言基数27·机械层名两白名单在场·层名声明↔代码 diff=∅（只增不减）
汇总 PASS=25 FAIL=1 PENDING_STAGE=1 总数=27
```

**BW-3 余 6 对象如实**：全部落在 `miyazaki-hayao-perspective`（3 处）与 `mrbeast-perspective`（3 处），**本对象 david-fincher 两处已由 FX-U5（commit `5826b40`）补口径清零**——本件开工实跑 BW-3 明细中 david 零命中＝归零实证。红账存续非本对象账，不入本票射程（票面 §四）。

selftest 四件当期读数：`selftest 用例 155／反常 0`（assert-tool）、`s0b-kappa selftest 用例 40／反常 0`、`validator-public-anchor selftest 用例 22／反常 0`、`validator-source-anchor selftest 用例 19／反常 0`——四件全过、反常零。

## ④ EG-6 与受限路径陈述

- **EG-6 门槛过读数**：`一手占比`=`58.3` ≥ 门槛 `50`（出处＝registration.md §语料门槛登记 L36：「`一手占比门槛`=`50`；`新鲜度窗口月数`=`12`；`一手占比`=`58.3`（统计口径：本人原文态要素条目数/要素条目总数；样本量=`12`；一致性系数 κ=0.801887＝软门锚点元组读数（s0c-anchors-b1 封印在册，与本产物元数据 `calibration_state`=`校准态` 同锚））＝门槛过」；SKILL.md 诚实边界节 L61 同源行）。三件套（统计口径＋样本量＋一致性系数）齐＝U5 补口径后 BW-3 david 归零的构造性实证。
- **新鲜度窗口受限行如实**：窗口内条目=`4`/`12`＝窗口判据按字面不过，走 FM-S-01 受限路径如实登记（registration.md L37；SKILL.md 诚实边界 L62）——受限行＝`受限`，诚实边界节加厚降期望，禁凑档。按票面 §〇-4 口径：PM 判词「无受限行」指无 EG-6 受限档位行，窗口受限登记行为在册如实态，**不阻入池、由人工闸当场裁**；本件如实呈报不加工。
- **calibration_state 校准态对账链（κ=0.801887 三处锚）**：
  1. 封印锚＝`.collab/evidence/harness/s0c-anchors-b1/anchor-tuple-soft.json`：`"κ点值": 0.801887`、`"calibration_state": "校准态"`（实读在场）；
  2. 产物锚＝david SKILL.md L15：`calibration_state`=`校准态`（工具现读＝assert-tool GS-4 PASS·元组 2 在场·κ 点值 0.801887/1.0；非手写声明）；
  3. 门禁锚＝assert-tool GS-4 当期读数 `PASS 元组 2 个在场·κ 报告与 calibration_state 逐元组对账全一致`。
  三锚逐字一致＝校准态非自declare，工具对账在册。

## ⑤ 风险与缺位如实（三缺位不得读作质量绿）

- `control_arm`=`未测`：old/new/without_skill 三臂对照读数缺位（准入证据卡 L16）。
- `leakage_check`=`未检`：test-prompts 题面未对照语料——对照需判分段批次工件，当期该输入面缺位＝未验如实（准入证据卡 L16）。
- judge 层（盲评 rubric／绝对线／decoy）＝参考位读数缺位（SKILL.md 诚实边界 L64）。
- 上三读数均为**缺位如实态**，本提案不将其折算为任何质量绿；对照臂/泄漏/judge 的后续出账归各自后续工序，不入本入池票射程。
- 其余在册如实面：矛盾条目（200-take 传说 vs 本人均值自述）按原样入档不平滑；外部视角路低密度未造数补平；归因差未平滑（SKILL.md 诚实边界节）。

## ⑥ 提案结论

**建议入池**：david-fincher-perspective v0.2 具备入 active 生效池的规程资格——EG-6 门槛过（三件套齐）、结构/防编/要素/校准门禁面全绿（27 项中本对象零红）、受限态与三缺位均如实登记在产物本体；「最后一步从未发生」的空池平凡真状态（FC-6 现读）需由本单产物级实证替代。

一句话可批的批准话术草案（与 S3 确认包 §五同文）：

> 批准 david-fincher-perspective v0.2 入 active 生效池？是／否

——工程师席（FX-U6 票内新鲜实例）提案·2026-11-06·除本件外零写入。
