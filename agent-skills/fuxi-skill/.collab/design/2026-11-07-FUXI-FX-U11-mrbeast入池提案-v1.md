# FUXI-FX-U11 · mrbeast-perspective 入池提案 v1

> 票号＝FX-U11｜工序＝S1 独立提案件（票面 §二 S1·闭集第 6 件）｜日期＝2026-11-07｜提案席＝工程师席（FUXI 线·FX-U11 票内新鲜实例）
> 性质＝入池前置三件套之「独立提案」件（池规程真源＝`agent-skills/fuxi-skill/products/README.md` §一「入池前置：写入本池必须经人工确认＋独立提案＋版本审计」）。本件不是确认件；确认权在皮总（S4 人工闸）。
> 模板先例＝FX-U6 david-fincher 首单提案（`agent-skills/fuxi-skill/.collab/design/2026-11-06-FUXI-FX-U6-david-fincher入池提案-v1.md`）·第二单照抄件形。

## ① 提案头（独立性声明）

- 提案席＝工程师席；确认人＝皮总（主理人呈）——**提案人≠确认人**，独立性声明成立。
- 本席职责边界＝把资格读数、缺位面、候裁项如实备齐到「一句话可批」强度；不代签、不预填任何人工确认引用（票面 §四「人工闸不可代位」条款遵守声明）。
- 开工 ANCHOR＝`874d0be`（全哈希 `874d0bea28398c139c1a28e8e85983cb215c9a1a`＝开工当轮 `git log -1` 现盘实跑）。
- 开工前置对账四行全绿（不符＝停手条款未触发）：①FX-U10 收口登记 `d86b34d` 在 HEAD 链＋放行登记 `874d0be` 在场（串行令硬前置满足）；②assert-tool 汇总＝`PASS=26 FAIL=1 PENDING_STAGE=0 总数=27`·exit 1 且 BW-3 明细＝恰 3 命中全部属 miyazaki-hayao-perspective（mrbeast 三处归零实证＝明细中 mrbeast 零命中）；③本体 sha 对拍＝改后态 SKILL.md `8869c8cf7a4a492d6dc7154a774838e77a04abd95c94fc47c36aa88c03d1b787`／registration.md `0f3c0ebcfb817fd1b27f34c2c38141022e3b861c2070dc1527eb8322f2b270f6` 与 U10 回执（`agent-skills/fuxi-skill/.collab/receipts/2026-11-07-FUXI-FX-U10-工程师回执-v1.md` L96-97）逐值全等；④FC-6 现读 active 池条目 1（david 在位）·pending 条目 3（含 mrbeast 原位三件）。
- 本件写作时点门禁读数＝ANCHOR 态实跑（`.scratch/FX-U11/assert-run1.txt` 留档，run 内逐字节对账）。

## ② 入池对象与轨别

| 字段 | 值 | 出处 |
|---|---|---|
| 产物id | `mrbeast-perspective`（与目录名逐字全等） | 产物 SKILL.md 元数据节 L9 |
| 所属轨 | `person` | 同上 L10 |
| 编译形态 | `single` | 同上 L11 |
| 版本号 | `v0.2` | 同上 L13 |
| 快照时戳 | `2026-10-31` | 同上 L12 |
| 复审到期日 | `2027-01-29` | 同上 L14（＝快照＋90 日，本席实算 `datetime.date(2026,10,31)+timedelta(days=90)＝2027-01-29` 逐字对上） |
| 当前落位 | `agent-skills/fuxi-skill/products/pending/mrbeast-perspective/`（待确认暂存区） | 现盘实查 |
| 拟入落位 | `agent-skills/fuxi-skill/products/mrbeast-perspective/`（active 生效池根） | 池规程 §一 |

## ③ 门禁现读全文引用（assert-tool 27 项明细·当期读数照录）

开工 ANCHOR `874d0be` 态实跑（exit 1），逐行照录：

```
ST-1 PASS 主契约面在场·json 可解析·AC 节闭集 diff=∅
ST-2 PASS 三件在 contracts/ 实体·节闭集 diff=∅（EG6/FM5/AC5）
ST-3 PASS 产物实例 4 条目·文件 4·节结构 diff=∅（实产物判绿）
ST-4 PASS 产物条目 4·回归条目 24（逐条目 david-fincher-perspective=6／elements-of-style-technique=6／miyazaki-hayao-perspective=6／mrbeast-perspective=6）·字段闭集＋档位/轨取值判绿（实产物判绿）
ST-5 PASS 批次 0·审计件 0·条目 0（空 listing 合法）
ST-6 PASS person 面无「执行步骤」段字样·命中=0
ST-7 PASS method 面无「表达 DNA」段字样·命中=0
ST-8 PASS 两规范表在场·四节闭集 diff=∅·关键引用行（AC-1/总则声明行/AC-2/VA-S-01）在场
ST-9 PASS 产物实例 registration 随件 4 条目·节闭集 diff=∅
ST-10 PASS 产物实例 3 条目·批次 eos-b1、t9 逐路存在性检 18/18 在场（实扫描判绿）·method 轨豁免 1 条目（-technique）
BW-1 PASS 词表条目 5·产物正文实跑命中=0（扫描 12 件）
BW-2 PASS 触发词 5·档位 4·产物正文实跑命中=0（扫描 12 件）
BW-3 FAIL 产物报告裸数字 3 处（三件套=统计口径＋样本量＋一致性系数·缺任一即裸）：miyazaki-hayao-perspective/SKILL.md line6 缺统计口径、样本量、一致性系数；miyazaki-hayao-perspective/SKILL.md line59 缺一致性系数；miyazaki-hayao-perspective/registration.md line36 缺一致性系数
BW-4 PASS technique 条目 1·扫描 7 卡·B段检出=0（实扫描判绿）
BW-5 PASS (a) 声明行两行在场·(b) 词表 4 值本体在场·产物面命中=0（扫描 9 件·实扫描判绿）
BW-6 PASS 对照表先于首个二级标题·两工具名＋本线列名命中·声明行命中=1·三维度行名齐备
FC-1 PASS 两字段名在注册面·两值闭集与契约声明逐字全等
FC-2 PASS 注册表 26 字段·双向 diff=∅·实例⊆注册·FM条目纪律·值互洽全等
FC-3 PASS 契约 json 实例 2 条成对判绿·产物要素侧要素行 55 行成对判绿（实要素行判绿）
FC-4 PASS 词表六值·三栏名声明 AC-5·词表声明句逐字全等·看板目录空（合法）·看板状态token扫描判绿
FC-5 PASS bundle 实例 0 条·命名空间互借检出=0（配对咬放实证见 selftest）
FC-6 PASS active 池条目 1·无人工确认来源条目数=0（实条目确认引用行判绿）
GS-1 PASS person 记录 36 条·越白名单命中=0（实记录判绿）
GS-2 PASS method 记录 7 条·越白名单命中=0（实记录判绿）
GS-3 PASS 全量记录 43 条·双向不匹配数=0（实记录硬验收判绿）
GS-4 PASS 元组 2 个在场·κ 报告与 calibration_state 逐元组对账全一致（判据本体零改动）
GS-5 PASS 层名11·白名单6+6·断言基数27·机械层名两白名单在场·层名声明↔代码 diff=∅（只增不减）
汇总 PASS=26 FAIL=1 PENDING_STAGE=0 总数=27
```

**BW-3 余 3 对象如实**：全部落在 `miyazaki-hayao-perspective`（3 处：SKILL.md line6／line59、registration.md line36），**本对象 mrbeast 三处（SKILL.md L34／L62＋registration.md L36）已由 FX-U10（commit `f0998bb`）出清**——本件开工实跑 BW-3 明细中 mrbeast 零命中＝归零实证（六→三）。红账存续非本对象账，不入本票射程（票面 §四：miyazaki 红账出清归 miyazaki 自身入池批工序）。

**FC-6 当期读数如实**：`active 池条目 1·无人工确认来源条目数=0（实条目确认引用行判绿）`＝david 首单产物级实证在位；本单＝该判据产物级实证第二单到位对象。

selftest 四件当期读数：`selftest 用例 161／反常 0`（assert-tool）、`s0b-kappa selftest 用例 40／反常 0`、`validator-public-anchor selftest 用例 22／反常 0`、`validator-source-anchor selftest 用例 19／反常 0`——四件全过、反常零。

## ④ EG-6 与窗口陈述（含校准态对账链·批级锚口径）

- **EG-6 门槛过读数**：`一手占比`=`57.1` ≥ 门槛 `50`（出处＝registration.md §语料门槛登记 L36：「`一手占比门槛`=`50`；`新鲜度窗口月数`=`12`；`一手占比`=`57.1`（统计口径：本人原文态要素条目数/要素条目总数；样本量=`14`；一致性系数 κ=0.801887＝s0c-anchors-b1 软门锚点元组读数（封印在册；本对象不在该批次预注册对象集＝对象级锚覆盖缺位，此值为批级元组读数非对象级读数））＝门槛过」；SKILL.md 诚实边界节 L62 同源行）。三件套（统计口径＋样本量＋一致性系数）齐＝FX-U10 B1/B2 补口径后 BW-3 mrbeast 归零的构造性实证。语料落盘侧对拍（PM-U5 判定件 §二第 2 行在册）＝六路 C- 条目 14（本人原文 8／第三方转述 6／模型推断 0）→ 8/14≈57.1 逐值咬合。**无 EG-6 受限行**。
- **新鲜度窗口过读数**：落 12 个月窗口内条目=`10`/`14`＝窗口过（registration.md L37；FX-U10 B4 补注后判定依据显形：行内发布锚确证在窗 8 条＝C-MB-01/02/05/07/08/09/10/14＋无行内日锚按源件发布批时推定计入在窗 2 条（推定形态＝依据强度低于确证层＝如实注）＝合计 10；窗外确证 2 条＝C-MB-03（2025-03）、C-MB-04（2025-03-27）；最保守读数＝仅确证层 8/14 仍占多数，窗口过结论稳）。与 david 案不同：david 为窗口受限行走 FM-S-01 受限路径，**mrbeast 两维（EG-6＋新鲜度）皆过＝无受限呈裁项**（PM-U5 判定件 §二结论「够格（无 EG-6 受限行）」在册）。
- **calibration_state 校准态对账链（κ=0.801887 三处锚＝批级元组锚）**：
  1. 封印锚＝`agent-skills/fuxi-skill/.collab/evidence/harness/s0c-anchors-b1/anchor-tuple-soft.json` L4：`"κ点值": 0.801887`（实读在场）；
  2. 产物锚＝mrbeast SKILL.md L15：`calibration_state`=`校准态`（工具现读＝assert-tool GS-4 PASS·元组 2 在场（s0c-anchors-b1 软/硬两元组·κ 点值 0.801887/1.0）；非手写声明）；
  3. 门禁锚＝assert-tool GS-4 当期读数 `PASS 元组 2 个在场·κ 报告与 calibration_state 逐元组对账全一致`。
  三锚逐字一致＝校准态非自declare，工具对账在册。**措辞口径注**：本对象产物面两处 κ 引值行（SKILL.md L62／registration.md L36）均为 FX-U10 批级锚措辞（「s0c-anchors-b1 软门锚点元组读数（封印在册…此值为批级元组读数非对象级读数）」）＋对象级锚覆盖缺位如实注随行——**禁**写「与本产物 calibration_state 同锚」类对象级归属句（PM-U5 §2.2 措辞约束·U10 已按此落笔）。

## ⑤ 风险与缺位如实（四缺位不得读作质量绿）

- **候裁项 C 专列陈述＝对象级校准覆盖缺位（首案型）**：`prereg-s0c.json` 预注册对象集＝david-fincher／miyazaki-hayao／eac-30-discipline／mc-70-charter 四对象，**mrbeast 不在册**；`anchor-labels-soft.json`／`anchor-labels-hard.json` 全封印标注面 grep「mb-」＝0 命中（本席开工现查复证两文件计数 0）。在册 GS-4 判据＝元组级对账无对象级要求＝机械位不咬、按 specs/池规程在册口径**不阻入池**；但校准态支撑＝批级元组锚非对象级读数——补标与否＝皮总 S4 随确认一并裁（见 §⑥ 分支声明与确认包 §③ 候裁项 C 呈裁段）。
- `control_arm`=`未测`：old/new/without 三臂对照读数缺位（准入证据卡 L16）。
- `leakage_check`=`未检`：test-prompts 题面未对照语料——判分段批次泄漏检输入面缺位＝未验如实（准入证据卡 L16）。
- judge 层（盲评 rubric／绝对线／decoy）＝参考位读数缺位（SKILL.md 诚实边界 L66）。
- 上四读数均为**缺位如实态**，本提案不将其折算为任何质量绿；对照臂/泄漏/judge 的后续出账归各自后续工序，不入本入池票射程。
- 其余在册如实面：矛盾条目（数据裁决 vs 故事转向）按原样入档不平滑（SKILL.md 反模式节＋诚实边界节）；部分转写源无原始视频回查＝证据等级降为跨文本推断逐条标注；商业数字＝第三方转述态引用不补全（SKILL.md 诚实边界节）。

## ⑥ 提案结论

**建议入池**：mrbeast-perspective v0.2 具备入 active 生效池的规程资格——EG-6 门槛过（57.1≥50·三件套齐·批级锚措辞）、新鲜度窗口过（10/14·B4 依据显形）、结构/防编/要素/校准门禁面全绿（27 项中本对象零红·BW-3 三处已由 U10 出清）、缺位与候裁项 C 均如实登记在册；FC-6 判据产物级实证第二单由本单到位（池 1→2）。

一句话可批的批准话术草案（与 S3 确认包 §五同文）：

> 批准 mrbeast-perspective v0.2 入 active 生效池？是／否

分支声明（票面 §六候裁项 C 口径）：若皮总裁「**按批级锚接受**」＝本提案结论照常执行（缺位如实注随行＝在册口径）；若皮总裁「**须补标**」＝对象级补标（扩 s0c 批次）＝新工程射程不在本两票闭集，**本提案即转阻塞呈报**，另开 s0c 扩批工程票，本入池票按阻塞收口上报。票面读数以「不补标」为基线（U10 措辞前向兼容设计注同款）。

——工程师席（FX-U11 票内新鲜实例）提案·2026-11-07·除本件外零写入。
