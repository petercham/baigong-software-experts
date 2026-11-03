# FUXI-T11 · assert-tool ST-9 registration 随件节闭集断言票

> 票号＝FUXI-T11｜起草＝架构席（arch-fuxi-tr1）｜日期＝2026-10-31｜被派＝**工程师席**
> ANCHOR＝开工前取当轮 HEAD 实测读数（回执开端必附；**开工须在 FUXI-T10 收口之后**——两票串行令）；起草时点 HEAD 实测＝`551317c` 后继面（起草不执行，锚以开工读数为准）
> 来历（自包含）：T9 端到端复跑 QA 对抗实证（候补 O2→TR2 §一-4 分诊为修票）：classifier.md §二 末行声明「注册记录实体落点＝产物条目目录根 `registration.md`：内容闭集四节（节头逐字）＝`注册三元组`／`分类器四问决策记录`／`采集与蒸馏声明（六节规程逐节执行读数）`／`语料门槛登记（EG-6）`」（T7 修正后口径），但**交付面门禁无机械消费点**——ST-3 只 diff `SKILL.md` 本体件；QA 实测 registration 任一节头改名 → assert-tool 不咬（PASS=23 不变）。＝声明面有闭集、机检面无咬合位，违反本项目「每声明闭集配机械位」硬验收惯例；T9 判据⑨现为 grep 人工读数位。**本票＝补缺口，不改四节口径本身。**

## 〇、执行裁定（票内定稿，非候裁）

1. **断言编号＝ST-9**（结构类现列 ST-1..8，ST-9 为下一空号；「只增不减」纪律方向合法）。基数三处同源随动 25→**26**：assert-tool `GS5_BASELINE["断言编号基数"]`＝26＋ASSERTIONS 列表 append 一项＋`assertion-catalog.md` 编号闭集行「25 项」→「26 项」与结构类计数「结构 8」→「结构 9」＋assert-tool 头 docstring 计数行（L5/L40 两处「25 项」）随动。
2. **判据本体规格（钉死）**：
   - 实装基面＝`_product_scan_entries()` 既有产物级扫描面枚举（生效池根直接条目＋pending/ 一层；archive 免检自动继承）；每条目消费 `registration.md` 随件。
   - 判定＝该文件 H2 节名集（沿用 ST-3 perspective 侧既有归一化 `_norm_perspective_headers()` 同款去空白归一，防连写/带空格两形态误咬）对四节注册闭集 diff＝∅：`注册三元组`／`分类器四问决策记录`／`采集与蒸馏声明（六节规程逐节执行读数）`／`语料门槛登记（EG-6）`（节头逐字＝classifier 声明行四值，注册常量单源不复制第二份词表——直接从本断言注册常量出，catalog 侧引用同文本）。
   - 三态：扫描面空＝空扫描合法态判绿（FC-5/GS/ST-3 同款口径）；条目缺 `registration.md`＝**fail**（classifier 声明随件必在场，缺＝结构违例——pending/README 条目清单行亦声明随件三件套）；节 diff 非空＝fail 列明细；全等＝PASS（读数含条目数）。
   - 多节处置＝多出节即咬（四节＝内容闭集，非「至少四节」）。
3. **GS-5 活性自证**：GS-5 既有「断言编号基数 ≥ 基线」分支自动随动（基线改 26）；selftest 增配对用例＝四节全等放／改名咬／缺文件咬／空扫描放（≥4 例，总数 139→≥143 如实入回执）。

## 一、声明闭集（本票交付笔唯一改动面）

- `deliverables/skills/fuxi-skill/gates/assert-tool.py`（ST-9 函数＋ASSERTIONS append＋GS5_BASELINE 26＋注册常量＋docstring 计数行两处随动＋selftest 配对用例）
- `deliverables/skills/fuxi-skill/gates/assertion-catalog.md`（结构类 append ST-9 条目〔分期＝〔S4 建／T11 实装〕·断言内容/失败语义/条款行（条款＝classifier §二 注册落点行＋T7 口径）〕＋「25 项」→「26 项」两处＋修订注记 append）

回执（另笔）：`.collab/receipts/2026-10-31-ENG-T11-工程师回执v1.md`。

## 二、施工规格

S1 · assert-tool：注册常量 `REGISTRATION_SECTION_CLOSEDSET`（四值逐字）；函数 `st_9_registration_section_diff()`（消费 `_product_scan_entries()`，逐条目读 `registration.md`，H2 抽取复用既有归一化层）；ASSERTIONS append `("ST-9", "st_9_registration_section_diff")`；GS5_BASELINE 断言编号基数 26；docstring L5「25 项」与 L40「跑 25 项」随动 26。
S2 · selftest：四配对（正样本＝四节全等内存串放／改名咬／缺文件咬／空列表放）＋基数例随动（既有 `GS5_assert基数` 例期望自动＝26）。
S3 · catalog：ST-9 条目文本照 §〇-2 规格成文；基数措辞两处随动；修订注记 append 一行（v 序随现文件体例）。
S4 · 判分段实跑读数入回执（§三）。

## 三、验收判据（三态禁假绿）

1. **现盘实产物判绿**：assert-tool 全量仓内模式 ST-9＝`PASS 产物实例 registration 随件 3 条目·节闭集 diff=∅` 型读数（T9 复跑批三 registration 四节现盘全过）；连跑两次逐字节全等；汇总 FAIL=0、PENDING_STAGE=2（BW-3/BW-4）零动。
2. **总数随动对账**：汇总 总数=**26**；GS-5 读数含基数 26 且判绿（只增不减分支活）；catalog/assert-tool/GS-5 三处基数全等（grep 对拍读数入回执）。
3. **对抗三例（真咬实证·测毕复位 blob 对拍）**：①任一 registration 节头改名→ST-9 FAIL 真咬；②删除任一 registration.md→FAIL 真咬；③（可选负样本＝pending/ 临时清空）空扫描合法态判绿。复位三件 hash-object 对 `HEAD:` blob 全等。
4. **零回归**：assert-tool selftest 例数 139→≥143·反常 0；四工具 selftest 其余三件（40/22/19）零动；validator 两件/run-gates 性质零动（run-gates 计数与 T10 收口后基线全等——ST-9 不入 run-gates 检查器集，仅 assert-tool 内部断言，如 run-gates 消费 assert-tool 汇总行则总数行差 25→26 如实解释）。
5. 禁动面：四节节头口径本体零改（classifier.md 零触碰——它已是真源）；产物九件零触碰（只读消费）；`products/` 面零动；validator-catalog/§四 预注册表零动；s0b/s0c 工件零触碰。`git show --name-only`≡声明闭集（交付笔恰 2 件）。

## 四、纪律

- 交付单笔（前缀 `ENG-T11:`）＋回执笔另 commit；回执开端附开工 ANCHOR（须在 T10 收口后取数）。
- 禁 --no-verify、禁 amend、禁 push；候补池不动；新缺口只登记走 ㊵。

## 五、候裁点

无。ST-9 编号/缺随件即咬/多节即咬三项均为 classifier 既有声明文本（「内容闭集四节」「随件」）的直接机械化的程序内定稿，无对立分歧；基数只增不减走既有 GS-5 纪律。
