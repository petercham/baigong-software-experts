# FUXI-FX-U12 · D-13 `value_decl_diff` 逐点位修正票（并集口径→逐点位口径·契约措辞一字不动·单点缺值必咬）

> 票号＝FX-U12｜起草＝架构席（arch-fuxi-u12）｜日期＝2026-11-07｜被派＝**工程师席**（FUXI 线·一人一实例）
> 起草／开工 ANCHOR＝`d94ed63ba1005c266598aa4d2b5f7bbebc4fc572`（short `d94ed63`，开工当轮 `git -C agent-skills/fuxi-skill rev-parse HEAD` 实测＝起草时点同值；tracked 面净实锤＝`git status --porcelain` 仅 untracked 若干〔`.collab/ledger/`、`.scratch/*` 存量、`.scratch_wbdocs.html`、`agent-experts/baigong-software-team/.collab/ledger/`〕与本案无关禁带入；他案 PROJINIT 在途零触碰）。开工 ANCHOR 与 `d94ed63` 不符＝停手上报，禁带差开工。
> 开工前置对账（四读数当轮实读相符方可动码）：①TR4 缺陷台账落账笔 `d94ed63` 在链（`git log --oneline -3` 首位即该笔）；②assert 汇总＝`PASS=26 FAIL=1 PENDING_STAGE=0 总数=27`·exit 1，唯一 FAIL＝BW-3 三命中全属 miyazaki（明细逐字见 §三-1）；③selftest 四件＝assert-tool 用例 **161**／s0b-kappa 40／validator-public-anchor 22／validator-source-anchor 19，反常全 0；④run-gates＝`GATE PASS（发现 9822 条，均按路由表走②不拦提交）`exit 0（起草当轮现盘实跑值，开工照登对拍，漂移 FX2-1 口径归因照登）。
> 账权＝FUXI 项目（拍板㊠）：本票及其回执／QA 件落 FUXI 账域（`agent-skills/fuxi-skill/.collab/`）；百工 bundle 账域与 SWB 仓其他账不入本票射程。
> 来历（自包含，禁指针依赖）：TR4 缺陷台账归因复盘件 `agent-skills/fuxi-skill/.collab/defects/2026-11-07-FUXI-缺陷台账归因复盘-v1.md`（落账 `d94ed63`）§二乙组 L48 D-13 行在册＝「`value_decl_diff` 跨块并集口径掩盖单点位缺值（单缺不咬·双缺才咬）」，状态＝候补挂账，③阻断判＝**阻断**（该行原文：「契约 AC-2 明文『逐字全等』而机械面并集＝声明↔机检不对齐＝任何场景下单点位缺值声明恒漏检；同族『每声明闭集配机械位』先例＝D-34/T11 均出票修」），④去向＝该件 §三-1；§四 L138 标题句自陈「候补挂账 25 项中除阻断级 D-13 外 24 项」＝全台账唯一阻断级未修项；§五备注① L153 在册＝BW-3 余三处红账全属 miyazaki（fail-closed 真红存续随 miyazaki 入池批清账）。§三-1（L132）修法原文：「修法＝并集改逐点位 diff＋selftest 单缺/双缺配对夹具＋catalog 口径行随动（材料＝qa/S1 P5/P16 两探针已备好夹具形态）」；同段可降级条件原文：「**可降级条件（如实登记）**：若产品/主理人裁『§五口径本义＝并集语义』并把 AC-2 措辞随正为并集，则本项降为加固类入候补池——降级＝契约措辞裁量权在产品段，不在本席；裁前按现契约文字＝阻断」。**决策现状＝拍板「先修 D-13」＝不采降级路径：契约措辞一字不动、机械面补强到逐点位**（本票按此写死；降级路径的裁量权在产品段、本票不启动也不预设）。同族先例出票形态照收＝TR2 #4 → T11 修 D-34（`008fa07` ST-9 四节闭集断言·基数 25→26 三同源随动）与 FX-U3 修六路落盘（`0fa7ea7` ST-10）。
> 指针纪律注：本票面反引号路径＝起草时点目标已在盘者；回执／收口登记等尚未生成件的路径一律裸文写（避免 OA-D6 起草态悬空假报）；落笔前对票面跑 check-pointers --target 自查零 BLOCK。

---

## 〇、复核结论（架构席 2026-11-07 实读实跑实查，票内定稿依据）

1. **被修函数现盘实读**：`value_decl_diff()`＝`agent-skills/fuxi-skill/gates/assert-tool.py` L312-330。docstring L313 逐字自陈并集口径：「契约声明值 ↔ 工具注册值 diff：逐字段并集与注册元组逐字全等才算过。」函数体机制＝先把各 json 块的「值注册」按字段名 **update 进一个 merged 集合**（L315-322：`merged.setdefault(str(field), set()).update(str(v) for v in allowed)`），再对注册表逐字段比对并集（L323-329）。＝声明点位间互掩：任一点位缺值，只要别处存在同值即被并集补齐＝恒漏检放行（D-13 判定成立）。
2. **全部调用点实查（两条消费断言，逐一实查列出·非推演）**：
   - **FC-1** `fc_1_two_field_closedset()`（L1175-1190）→ 调用行 L1187 `problems = value_decl_diff(blocks, fc1_only)`，`fc1_only`＝两字段（`evidence_grade`／`calibration_state`，注册常量 L93-94）。读数行 L1190＝`两字段名在注册面·两值闭集与契约声明逐字全等`。
   - **FC-2** `fc_2_kernel_fields_diff()`（L1193-1230）→ 调用行 L1226 `problems.extend(value_decl_diff(blocks, VALUE_REGISTRIES))`，`VALUE_REGISTRIES`＝九对照字段注册表（L235-245：`evidence_grade`／`calibration_state`／`证据等级`／`来源态`／`control_arm`／`leakage_check`／`abstain_tier`／`编译形态`／`所属轨`）。读数行 L1229-1230＝`注册表 %d 字段·双向 diff=∅·实例⊆注册·FM条目纪律·值互洽全等`。
   - 除上述两处仓内调用外，`value_decl_diff` 仅被 selftest 直调三例消费：L1985 `FC1V_pass`／L1986 `FC1V_bite_extra_value`／L1987 `FC1V_bite_missing_decl`（`_selftest_cases()` L1791 起）。**无第三消费点**（grep `value_decl_diff` 命中恰六处＝定义 1＋仓内调用 2＋selftest 直调 3，已实查）。
   - 块来源装配面（点位容器）：FC-1 经 `_all_blocks(_contract_texts())`（L1181）、FC-2 经同函数（L1204）；`_contract_texts()`（L650-660）＝三契约件（`KERNEL_THREE_FILES` L223＝evidence-grading／failure-modes／artifact-contract）＋`agent-skills/fuxi-skill/rejected/README.md`（键 `rejected-README`）；`_all_blocks()`（L663-670）按 `texts.values()` 插入序（实读＝evidence-grading→failure-modes→artifact-contract→rejected-README）extend 各件 fenced json 块＝**确定性序，可钉死点位号**。（第三处 `_all_blocks` 调用 L1300＝FC-5 bundle 命名空间检，**不消费** `value_decl_diff`，本票零碰。）
3. **契约声明强度实读（禁改基面·引用附行号）**：`agent-skills/fuxi-skill/contracts/artifact-contract.md`
   - L24 节头 `## AC-2 状态字段`；L26 原文：「两字段两闭集（逐字与断言工具 FC-1 注册位全等；声明位＝机读值注册表，工具做双向 diff）：」；L29 值注册块原文：`{"值注册": {"evidence_grade": ["人工验证", "机械断言", "LLM 判定"], "calibration_state": ["校准态", "待校准"]}}`；**L34 原文：「- 两字段名显式写入本契约（两轴正交）；字段名与取值两闭集与断言工具注册位逐字全等。」**
   - 卷头 L3 双纪律原文：「> 性质＝交付件本体（自包含成文·双纪律＝节闭集〔恰五节，多节/缺节/改名＝diff 非空即 fail〕＋字段名闭集〔本文件声明字段名与断言工具注册位双向 diff＝∅，未注册字段零容忍〕）。」
   - 契约文本内「并集」字样 grep 命中＝**0**：契约从未声明并集语义＝「声明强度＞机械强度」缺口成文依据，故修法＝机械面补强、契约零字不动（＝TR4 §三-1 不降级路径的文本面事实）。
4. **声明点位实查枚举（含「值注册」键的 json 块＝逐点位比对的作用域；扁平块序取 `_all_blocks` 确定性序）**：现盘 json 块总数 **12**（解析失败 0），其中「值注册」块恰 **5** 个：
   | 扁平块号 | 件与落位 | 节 | 该点位在册字段数 |
   |---|---|---|---|
   | #2 | `agent-skills/fuxi-skill/contracts/evidence-grading.md` L45 | EG-5 候选单元记录 | 14（含 6 在册字段＋8 类型占位/非在册字段） |
   | #6 | `agent-skills/fuxi-skill/contracts/artifact-contract.md` L17 | AC-1 元数据 | 3（`编译形态`／`所属轨`／`abstain_tier`） |
   | #7 | `agent-skills/fuxi-skill/contracts/artifact-contract.md` L29 | AC-2 状态字段 | 2（`evidence_grade`／`calibration_state`） |
   | #8 | `agent-skills/fuxi-skill/contracts/artifact-contract.md` L49 | AC-3 准入证据卡 | 2（`control_arm`／`leakage_check`） |
   | #10 | `agent-skills/fuxi-skill/rejected/README.md` L27 | 二、条目文件字段（淘汰条目） | 7（含 `所属轨`／`证据等级`／`control_arm`／`leakage_check`） |
   - 其余 7 块＝「字段注册」块（#1/#4/#5/#9/#12）与实例记录块（#3 EG-5 示例、#11 rejected 示例条目）——不属值注册面，逐点位口径对其零动作（实读确认）。
5. **逐点位口径内存干跑取证（架构席 importlib 加载现盘代码＋内存复刻判定函数，非交付面改动；留档 `agent-skills/fuxi-skill/.scratch/FX-U12/perm1-dryrun-perpoint-diff.py` 与 `agent-skills/fuxi-skill/.scratch/FX-U12/perpoint-dryrun-evidence.txt`）**：
   - **FC-1 现盘逐点位＝绿**（两点位 #7＋#2 各字段与注册元组逐字全等）＝§三-3「在册产物与在册声明零新增误咬」的 FC-1 侧干跑确证。
   - **FC-2 现盘逐点位＝恰一处新咬**：`点位#10 所属轨 多出∅ 缺失['bundle']`——`agent-skills/fuxi-skill/rejected/README.md` L27 声明 `"所属轨": ["person", "method"]`（实读），而工具注册 `SIDE_TRACKS = ("person", "method", "bundle")`（L106）。定性注＝该点位是**留档区条目字段声明面**（同文件 L31 在册口径「判定维度分轨」＋示例条目 L37 `"所属轨": "person"`），留档条目是否存在 bundle 形态属产品/主理人语义裁量＝**本席不现场改判**，列 §六 候裁 H-1（该新咬落在 FC-2＝全仓新增第二红，处置分支写死 §六）。
   - **夹具形态对拍（并集 vs 逐点位）**：P5 型（两点位、一处缺 `待校准`）＝并集**绿**／逐点位**咬**（`点位#2 calibration_state 多出∅ 缺失['待校准']`）；P16 型（两点同缺）＝两口径皆咬；全齐＝两口径皆绿；单点替换越界值＝两口径皆咬（替换非 D-13 漏检面）；空块列表＝两口径皆全域缺声明咬。
   - **既有 selftest 三例保真**：`FC1V_pass`／`FC1V_bite_extra_value`／`FC1V_bite_missing_decl` 在逐点位语义下三例判据值不变（True/True/True，逐例验算在册）。
6. **QA 探针实证在册（夹具形态素材·引用附行号）**：`agent-skills/fuxi-skill/.collab/qa/2026-10-30-FUXI-S1-QA验证报告-v1.md` L54（「放过（记黄-3／注甲，见下）：P5 单点位 `calibration_state` 缺值声明被并集掩盖」）＋L94 黄-3 原文（「**黄-3（值闭集 diff 并集口径掩盖单点缺值）**：`value_decl_diff` 按跨块并集对账——EG-5 与 AC-2 两点位仅**一处**缺「待校准」时不咬（P5 实证；两点同缺则咬，P16 实证）。§五口径未明文逐点位 diff，故不构成违例，但 AC-2「与注册位逐字全等」的强度未逐点位机械保证。建议列工具随动候补」）。两探源码在册＝`agent-skills/fuxi-skill/.collab/qa/2026-10-30-FUXI-S1-QA-probe.py` L124-129（P5：把 AC-2 `"calibration_state": ["校准态", "待校准"]` 改成 `["校准态"]` 单点缺值→期望咬，实测放）与 `agent-skills/fuxi-skill/.collab/qa/2026-10-30-FUXI-S1-QA-probe2.py` L75-83（P16：EG-5 与 AC-2 两点同缺→实测咬）。
7. **候补池登记位实读**：`agent-skills/fuxi-skill/.collab/research/2026-10-30-FUXI-S0a-S4-施工链收口报告-v1.md` L41（§四「未绿项」第 5 行「黄账候补池（不顺手改）」行原文含「黄-3 value_decl_diff 跨块并集口径」；出池条件原文＝「出池条件＝对应工序实际暴露同类问题」——实际暴露已发生：TR4 按交付视角复判判阻断＋拍板先修＝本票出池起工）。出处偏差如实注＝TR4 §三-1 称「§五候补池行」，本席现读该行落位＝**§四第 5 行（L41）**，属引用节号转写偏差、不影响登记事实，照登不重裁。
8. **catalog 口径行实查（随动对象钉死）**：`agent-skills/fuxi-skill/gates/assertion-catalog.md` 现盘「并集」字样 grep 命中＝**0 occ**；涉该函数值比对语义的口径行＝**恰两条条目行**（FC-1 断言内容行 L118 含「取值 ∈ {人工验证, 机械断言, LLM 判定}；calibration_state 取值 ∈ {校准态, 待校准}」；FC-2 分期行 L123 含「机检口径三条＝声明⊆注册、实例⊆注册、注册⊆声明双向 diff＝∅」）＋§五 selftest 枚举行 L193（含「契约字段闭集外值咬放〔配对〕」族名位）。＝本票随动面恰这两条目行＋§五枚举行＋修订注记 append v12，不扩面。
9. **基数三同源现读（本票零碰·钉死当期读数）**：①`GS5_BASELINE`（L161）＝`GS5_BASELINE = {"层名基数": 11, "person白名单基数": 6, "method白名单基数": 6, "断言编号基数": 27}`；②`ASSERTIONS` 注册表（L1756-1784）＝27 个二元组（ST-1..10／BW-1..6／FC-1..6／GS-1..5）；③docstring 计数处＝L5（「断言目录＝同目录 `assertion-catalog.md`（27 项：ST-1..10／BW-1..6／FC-1..6／GS-1..5）。」）／L42（「跑 27 项」）／L858（「# 27 项目录断言（FX-U3 实装：ST-10）…」）／L1720（GS-5 docstring「断言编号基数（27 项）」）。本票无新断言号＝三同源三处全部零动，GS-5 明细行现读「…断言基数27…」逐字不变。旁注如实登＝`run_assertions()` docstring（L2288）存史前措辞「20 项逐项读数」，属交付面文案存量（同族＝TR4 D-18/D-24 类文字账），**本票不动**（禁顺手清扫扩面，YAGNI）。
10. **版本账／changelog 实查结论（写集依据）**：`git ls-files` 全枚举＋`grep -iE "changelog|version|版本|history"` 双查＝fuxi-skill 包内**无独立版本账／changelog 文件**。包内版本受控形态＝件内「修订注记」节两处在册（`agent-skills/fuxi-skill/README.md` §修订注记 v2 一行＋`agent-skills/fuxi-skill/gates/assertion-catalog.md` L197 修订注记 v1..v11 段＝断言目录版本账本体，历史批 v7/v9/v10/v11 均在此 append）。＝本票版本面落点＝**assertion-catalog.md 修订注记 append v12（已在写集第 2 件内，不新增文件）**；README 修订注记零碰（本票不改 README 所载断言计数／使用口径／目录地图，且断言计数 27 零动＝无随动触发条件）。

---

## 一、声明闭集（本票交付笔唯一改动面，共 2 件）

1. `agent-skills/fuxi-skill/gates/assert-tool.py`（§二 S1 四目＝函数体改逐点位＋docstring 随正＋selftest 三配对夹具＋调用点随动判定）
2. `agent-skills/fuxi-skill/gates/assertion-catalog.md`（§二 S2 三目＝FC-1/FC-2 口径行随正＋§五 selftest 枚举行随动＋修订注记 append v12）

> 写集依据逐件＝§〇-1/-2（被修函数与调用点在此件）、§〇-8（口径行在此件）、§〇-10（版本账＝本件修订注记节，包内无独立版本账文件故不造）。
> **写集外零面**：`contracts/` 三契约件＝**一字不动**（含 AC-2 全部条文与五个值注册块）；`agent-skills/fuxi-skill/rejected/README.md` 零触（候裁 H-1 射程，禁现场改判）；`products/` 全树零触（在册产物 active 池 david＋mrbeast、pending 三件套 elements-of-style-technique＋miyazaki-hayao、archive 三件免检面）；`validator-catalog.md` §二 层名值注册块零碰（`层名`／`判定`／`裁判家族` 不在 `VALUE_REGISTRIES` 九字段射程，GS-5 声明↔代码 diff 走独立面，见 §四）；基数三同源三处零碰；其余断言函数体零碰；README／SKILL／specs／adapters／docs／validator 三件／s0b-kappa／`.gitignore`／`agent-experts/baigong-software-team/` 全树零触。回执另笔（§五）。

## 二、施工规格（逐件逐落位，语义写死）

**S1 · assert-tool.py**

- **S1-a（L312-330 函数体＝并集→逐点位，判定语义写死）**：函数签名保持不变
  ```python
  def value_decl_diff(blocks: "list[dict]", registries: "dict[str, tuple[str, ...]]") -> "list[str]":
  ```
  （签名零改＝两处调用点 L1187/L1226 调用形态零动＝「调用点随动」在本票语义下＝**零调用改动**，仅读数随语义自然随动；实查依据 §〇-2。）
  新判定语义（逐点位）＝对 `blocks` 逐个 json 块独立对账，块间零并集、零互补：
  ```text
  对每个块（序号 bi 取 blocks 扁平序，自 1）：
      vals = 块.get("值注册")；非 dict → 该块跳过（非声明点位）
      对 vals 的每个 (field, allowed)：
          allowed 非 list → 跳过（沿用现口径）
          field 不在 registries → 跳过（未在册字段由 FC-2 字段面「声明⊆注册」判，禁在此一号两判）
          got = set(allowed 元素逐个 str 化)；want = set(registries[field])
          extra = got - want；missing = want - got
          extra 或 missing 非空 → 追加问题行「点位#{bi} {field} 多出{sorted(extra) or '∅'} 缺失{sorted(missing) or '∅'}」
  收尾（在册字段零声明守卫）：registries 中任一 field 从未在任何点位出现 → 追加问题行「{field} 全点位均未声明 缺失{sorted(want)}」
      （＝并集口径 L323-329 的「字段整体缺席仍咬」能力不回退，配 selftest FC1V_bite_missing_decl 单块变体保真）
  返回 problems（空＝放）
  ```
  **判定要点三条写死**：①**任一点位独立比对**——同一字段在多点声明时逐点各自全等，任一缺值/替换＝咬（消除单点掩蔽）；②**类型占位记法自然放**——`["string"]`／`["number"]` 形态点位（EG-5 块内 `candidate_id`／`一手占比门槛` 等）因字段名不在两注册表内被跳过（现盘 EG-5 L45 同体现象＝并集口径下亦不入比对，零新咬面来源），**禁新建类型占位豁免词表/豁免常量**（现盘跳过机制已覆盖，YAGNI）；③**读数禁跨点平滑**——问题行必带 `点位#{bi}` 定位前缀（禁「至少一点绿」形态）。
- **S1-b（docstring L313 随正）**：「契约声明值 ↔ 工具注册值 diff：逐字段并集与注册元组逐字全等才算过。」→「契约声明值 ↔ 工具注册值 diff：逐声明点位与注册元组逐字全等才算过（每点位独立对账·任一点位缺值/替换即咬·跨点位互补不算过；在册字段全点位未声明亦咬）。」除该行外函数注释零动。
- **S1-c（selftest `_selftest_cases()` 内 L1985-1987 之后新增配对三例；既有 `FC1V_*` 三例本体零动）**（夹具形态直接取自 qa/S1 P5/P16 两探针，§〇-6）：
  ```python
  # D-13 逐点位配对（夹具＝qa/S1 P5 放型／P16 咬型两探针形态）：单点缺值必咬·两点缺咬·全齐绿
  full_pair = [{"值注册": {"evidence_grade": list(EVIDENCE_GRADES),
                           "calibration_state": list(CALIBRATION_STATES)}},
               {"值注册": {"evidence_grade": list(EVIDENCE_GRADES),
                           "calibration_state": list(CALIBRATION_STATES)}}]
  one_missing = [{"值注册": {"evidence_grade": list(EVIDENCE_GRADES),
                             "calibration_state": list(CALIBRATION_STATES)}},
                 {"值注册": {"evidence_grade": list(EVIDENCE_GRADES),
                             "calibration_state": ["校准态"]}}]   # P5 型：单点缺「待校准」，别处有同值
  both_missing = [{"值注册": {"evidence_grade": list(EVIDENCE_GRADES),
                              "calibration_state": ["校准态"]}},
                  {"值注册": {"evidence_grade": list(EVIDENCE_GRADES),
                              "calibration_state": ["校准态"]}}]  # P16 型：两点同缺
  cases.append(("D13V_all齐_pass", value_decl_diff(full_pair, fc1_pair) == [], True))
  cases.append(("D13V_单点缺值咬", value_decl_diff(one_missing, fc1_pair) != [], True))
  cases.append(("D13V_两点缺值咬", value_decl_diff(both_missing, fc1_pair) != [], True))
  ```
  三例语义标语（放/咬对）如上钉；用例名以 `D13V_` 族前缀入 §五 selftest 枚举。**用例数 161→164**（开工实读数≠161 时按开工实基数＋3 为准并申报）。禁删禁改既有 `FC1V_*` 三例（§〇-5 保真验算在册：三例逐点位下判据值不变）。
- **S1-d（调用点零改动实证目）**：L1187／L1226 两行逐字节零变化＝回执必附 diff 零证（防「顺手给 FC-2 加豁免参数」形态私扩）。
- 纪律注：新增注释禁含过程域词（票号/候裁/主理人字样禁入 `gates/` 注释——D-18 存量教训）；`declared_field_names()`（L299-309，字段名面）／`kernel_field_diff()`／FM 条目纪律／实例侧判据／三态词表／退出码闭集／`GS5_BASELINE`／`ASSERTIONS`／validator-catalog 声明↔代码 diff 面＝全部零动。

**S2 · assertion-catalog.md（真源随动三目）**

- FC-1 条目（L116-120）断言内容行随正＝句末追加「（逐声明点位独立对账＝该字段在契约每个值注册点位均须与注册位逐字全等，跨点位互补不算过）」；失败语义／条款两行本体零动。
- FC-2 条目（L122-126）分期行（L123）「机检口径三条」括注后随正＝补「值互洽子检查＝逐声明点位（非跨点位并集）与注册元组逐字全等」一句；断言内容／失败语义／条款三行本体零动。
- §五 selftest 枚举行（L193）补族名「契约声明值逐点位对账全齐放／单点位缺值咬／两点位缺值咬〔D13V 配对族〕」；§五计数句其余零动（工具桩仍余 0 项）。
- 修订注记（L197 段）append v12 一行：「v12（2026-11-07·D-13 值注册逐点位口径批）：`value_decl_diff` 并集口径改逐声明点位口径（函数签名零改·调用点 L1187/L1226 零改·docstring 口径行随正·类型占位记法沿用字段名未在册跳过机制零新词表）；编号闭集 27 零动、无新断号、基数三同源零碰；§五计数句零动；selftest 枚举补 D13V 族（用例 161→164）；FC-1/FC-2 口径行随正补逐点位句；契约三件零字未动。」
- **catalog 内禁现「并集」字样**（§三-5 判据：现盘 0 occ→收口仍 0 occ；口径行随正只用「逐点位／逐声明点位」措辞，防把缺陷口径固化成交付文案）。

**工序序＝S1（码面）→ §三验收全跑（含 FC-2 逐点位新咬态如实处置＝见 §六 H-1 分支，禁先码后裁）→ S2（真源随动，读数实测定稿后写）→ 回执笔。git 面交付笔＝S1+S2 恰两件＋回执笔可两笔。**

## 三、验收判据（三态禁假绿，全部可机械验证）

1. **BW-3 唯一红读数不变（在册产物零误咬总判据之一）**：`python agent-skills/fuxi-skill/gates/assert-tool.py` BW-3 明细行逐字＝`FAIL 产物报告裸数字 3 处（三件套=统计口径＋样本量＋一致性系数·缺任一即裸）：miyazaki-hayao-perspective/SKILL.md line6 缺统计口径、样本量、一致性系数；miyazaki-hayao-perspective/SKILL.md line59 缺一致性系数；miyazaki-hayao-perspective/registration.md line36 缺一致性系数`（与开工基线逐字节全等·行号零漂移）；连跑两次逐字节全等。
2. **汇总四元守恒钉值（两态写死，禁现场凑）**：开工基线态＝`PASS=26 FAIL=1 PENDING_STAGE=0 总数=27`·exit 1。收口态两分支钉死——
   - 分支 A（§六 H-1 经主理人裁「补 `bundle` 到留档点位」并经随正通道挂本票后实施）：收口汇总行逐字 `PASS=26 FAIL=1 PENDING_STAGE=0 总数=27`·exit 1（唯一 FAIL 仍＝BW-3；FC-2 回绿；四元守恒 26+1+0=27 ✓）；
   - 分支 B（H-1 未裁＝默认态）：收口汇总行逐字 `PASS=25 FAIL=2 PENDING_STAGE=0 总数=27`·exit 1（**第二红＝FC-2**，明细行必含 `点位#10 所属轨 多出∅ 缺失['bundle']` 定位串；四元守恒 25+2+0=27 ✓）。
   - 两态均 exit 1 存续＝fail-closed 本义，禁吞 0；除 FC-1/FC-2 两行与汇总行外，其余 25 项明细逐字节零变化（含 ST-3 产物实例 4 条目、ST-4 回归条目 24、ST-9 四条目、ST-10 三条目 18/18＋豁免注记、FC-3 要素行 55 行、FC-6 池条目 2、GS-4 元组 2、GS-5 基数 27）。
3. **在册产物与在册声明零新增误咬（当场是红＝停笔呈报，禁顺手修产物）**：新口径下 27 项判定列的变化**只允许**落在 FC-1/FC-2 两行，且 FC-2 的新咬点位必逐字符于 §〇-5 干跑预演清单（恰一处＝`agent-skills/fuxi-skill/rejected/README.md` 值注册点位 #10 之 `所属轨`）。**若出现任何其他新咬点（含 active 池 david-fincher-perspective／mrbeast-perspective、pending 三件套 elements-of-style-technique／miyazaki-hayao-perspective、archive 三件、specs／adapters 面任一），或 FC-1 由绿转咬＝当场是红**：立即停笔呈报主理人（回执/回流件如实登记咬合明细＋点位定位串），禁改产物、禁改契约、禁给判据加豁免凑绿——按 §六 H-2 处置分支走。预演依据＝§〇-5 逐点位干跑（FC-1 全绿／FC-2 恰一处）＋回执必附「27 项逐行 diff 白名单对拍表」（白名单＝FC-1 行〔判定可绿不变、明细含读数变化时逐字申报〕、FC-2 行、汇总行三行，余 24 行逐字节全等）。
4. **selftest 钉值＋零回归**：assert-tool selftest＝用例 **164**／反常 0／exit 0（161＋D13V 三配对；开工基数非 161 按开工实读＋3 申报）；既有 `FC1V_pass`／`FC1V_bite_extra_value`／`FC1V_bite_missing_decl` 三例在场且判绿（保真实证）；s0b-kappa 40／validator-public-anchor 22／validator-source-anchor 19 三件零回归·反常 0。仓内模式红与 selftest 全绿并存＝合法态（FX-U4 两模式语义分离在册）。
5. **catalog 文案 grep 判据（限域写死，防自指）**：`grep -c "并集" agent-skills/fuxi-skill/gates/assertion-catalog.md`＝**0**（现盘实查 0 → 收口仍 0）；`grep -c "并集" agent-skills/fuxi-skill/gates/assert-tool.py`＝**0**（现盘实查 1＝L313 docstring 自陈行，随正后清零＝本票口径文案收口实证）；两值回执逐字附读数。
6. **run-gates 基线零新增红**：`bash agent-skills/object-audit/scripts/run-gates.sh` exit 0·`GATE PASS`；与开工基线 9822 条对拍＝无 BLOCK 新增、无红新增；存量逐数照登＋漂移归因行（FX2-1 口径，仓级门禁面不在 FUXI 票内处置）。
7. **碰面闭合**：交付笔 `git show --name-only` ≡ §一 两件；`git diff` 对 `contracts/` 三件／`rejected/`／`products/` 全树／`validator-catalog.md`／`specs/`／`adapters/`／`docs/`／README／SKILL／validator 三件／s0b-kappa／`.gitignore`／`agent-experts/baigong-software-team/` 全树＝零改动；基数三同源三处（`GS5_BASELINE`／`ASSERTIONS`／docstring 计数）逐字零变化；断言编号闭集 27 原样（GS-5 明细行逐字不变）。

## 四、禁动面（违任一＝整批退回）

- **契约一字禁改**：`agent-skills/fuxi-skill/contracts/artifact-contract.md`（含 AC-2 条文 L24-L34 与 L17/L29/L49 三值注册块）／`evidence-grading.md`（含 L45 EG-5 值注册块）／`failure-modes.md`＝任何字节零改动；「把 AC-2 措辞随正为并集」的降级路径**不在本票射程**（裁量权在产品段，TR4 §三-1 原文在册；本票前提＝已拍不降级）。
- **其余断言语义禁改**：除 `value_decl_diff` 函数体＋其 docstring＋FC1V 三例之外的任何判据函数体／读数行／注册常量零动；`VALUE_REGISTRIES` 九字段表零动（禁加删字段、禁改元组值）；`SIDE_TRACKS`／`EVIDENCE_GRADES`／`CALIBRATION_STATES` 等注册位零动；`declared_field_names()` 字段名面零动；`kernel_field_diff()`／FM 纪律／实例侧判据零动（禁一号两判）。
- **禁加豁免面**：禁为 `agent-skills/fuxi-skill/rejected/README.md` 点位新增豁免常量／后缀过滤／字段名白名单（留档点位缺 `bundle` 属语义裁量＝§六 H-1，非机械面可自行关闭）；禁新建类型占位豁免词表（§二 S1-a-②）。
- **在册产物零触碰**：active 池 david-fincher-perspective／mrbeast-perspective（已入池生效件，改动＝判别口径双证据违例）、pending 三件套 elements-of-style-technique／miyazaki-hayao-perspective、archive 三件全树零触；禁改产物任何行凑绿（新咬处置唯一路径＝停笔呈报，§三-3/§六 H-2）。
- **基数三同源零碰**（断言编号 27 原样，无新断言号）；`validator-catalog.md` 零碰（其层名值注册块字段不在九字段射程＝逐点位口径零涉，GS-5 声明↔代码 diff 读数必逐字不变）。
- **exit 1 不得吞**；史账不随正；已裁项不回流；evidence 桶不入 git；宿主装载面（`~/.workbuddy/skills/fuxi-skill/`）零触碰；仓外零写入；临时工作物只落仓根 `.scratch/FX-U12/`。

## 五、回执要求

裸文写路径＝agent-skills/fuxi-skill/.collab/receipts/2026-11-07-FUXI-FX-U12-工程师回执-v1.md：开工 ANCHOR 实测 HEAD（≡`d94ed63` 或如实申报差异）＋前置四读数对账行（assert 汇总＋BW-3 三命中在场＋selftest 四件＋run-gates 条数）；§三七判据逐条实跑读数全文（BW-3 明细钉值＋汇总收口态两态之一定值＋27 项逐行 diff 白名单对拍表＋FC-2 新咬定位串原文＋selftest 用例数钉值＋三件回归＋grep 两值＋run-gates 照登归因）；函数体改前改后全文对照＋sha256 对照；L1187/L1226 零改动 diff 证；交付笔 `git show --name-only` 清单；§〇 复核不一致处如实申报。一票一批一 commit（交付＋回执可两笔）。

## 六、候裁单列（禁现场改判，全部呈主理人）

- **H-1｜「合法并集场景」发现位（本席直读已发现一处，非「未发现」）**：`agent-skills/fuxi-skill/rejected/README.md` L27 淘汰条目值注册点位声明 `"所属轨": ["person", "method"]`，工具注册 `SIDE_TRACKS = ("person", "method", "bundle")`（L106）含 `bundle`——并集口径下 EG-5（L45）／AC-1（L17）两点位补 `bundle` 使该缺值不咬；逐点位口径下该点位必咬＝FC-2 新增红（预演定位串 `点位#10 所属轨 多出∅ 缺失['bundle']`）。**争议本体＝「留档区淘汰条目是否应含 bundle 形态」是语义问题**（该文件 L31 在册口径「判定维度分轨，框架共用」＋示例条目仅 person 例，契约侧 AC-1 L8 在册口径＝bundle＝混合形态编译产物、两层命名空间隔离判据 FC-5，非淘汰候选形态）——本席**不现场改判**，两案呈主理人／产品段：
  - 案一（补声明）：`agent-skills/fuxi-skill/rejected/README.md` L27 补 `"bundle"`＝声明面跟注册面对齐；涉交付件文案改动，须经主理人裁＋随正通道挂本票或另笔（本票 §一写集不含该件，禁工程师席自行改）。收口落 §三-2 分支 A。
  - 案二（收注册）：`SIDE_TRACKS` 去 `bundle`＝注册面跟留档语义对齐——**违 GS-5 只增不减纪律射程需另评**（该常量不属 GS5_BASELINE 三组基线，但缩值属门禁面重交付程序族），本席不建议、只列案备裁。
  - 未裁（默认）＝落 §三-2 分支 B（FC-2 红存续如实收口，H-1 随收口登记入候补池在册，红账清账路径归裁后随动笔）。
- **H-2｜「在册产物/在册声明新咬」处置分支（写死）**：实跑出现 §三-3 白名单外任一新增咬（含 FC-1 转咬、任何产物面/契约面新咬）＝**当场是红**：工程师席立即停笔（禁继续码、禁改产物/契约/判据凑绿），回流件如实登记咬合明细＋点位定位串＋复现命令，呈主理人裁拆分/另案；本票按异常销账路径收口。此分支与 H-1 分列＝H-1 属预演已知点位，H-2 属预演外实跑发现。
- 既有候补池项（观察-FX2-1 族／D-18 交付面过程词存量／D-66 设计态双态等）＝在册不重呈；TR4 §三-1 降级路径已拍不采＝不回流。

## 七、纪律

一票一批一 commit（交付＋回执可两笔）；**串行令＝本票单实例**（工程师席一人一实例；发现同席多实例并发＝立即停手向上报告）；前置＝TR4 台账落账 `d94ed63` 在链（§卷头①）；与在途他案（PROJINIT 线）零交集＝commit 一律 pathspec 限定本票写集（FX-U10 收口教训条款在册），rename 不涉及。跨席交互经主理人：H-1 裁决权在主理人/产品段，工程师席/QA 席不得自行改判据或改文案（禁门禁面自行扩判据＝TR4 在册口径）。QA 席独立核验另票另件，fresh eyes 全实跑：§三判据逐条复现＋对抗例钉死——**对抗一（D-13 主形态活性）**：scratch 复制契约面，对 AC-2 点位单独删 `待校准`（EG-5 保持全值）→FC-1 与 FC-2 必咬且读数含点位定位→复原复跑读数全等；**对抗二（P16 型两点缺）**：AC-2＋EG-5 两点同缺→两判皆咬（既有能力不回退实证）；**对抗三（禁跨点平滑实证）**：构造两点位互补形态（点 A 缺值 X、点 B 缺值 Y、并集恰全）→逐点位口径必两点皆咬（并集口径旧态放＝修前后对照登记）；**对抗四（在册面零误咬复算）**：现盘全树复跑 27 项，新咬集合 ≡ §〇-5 预演清单（FC-1 绿／FC-2 恰一处 #10）逐值对拍。复现门禁基线禁用只读 worktree（FX-U2/D-36 教训在册），用仓根现盘态。

——架构席 arch-fuxi-u12 起草·2026-11-07·ANCHOR `d94ed63`·除本票面外零写入（临时取证落 `.scratch/FX-U12/`）。
