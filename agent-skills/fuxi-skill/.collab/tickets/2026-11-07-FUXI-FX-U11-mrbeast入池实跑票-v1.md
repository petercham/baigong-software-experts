# FUXI-FX-U11 · mrbeast-perspective 入池实跑票（pending→active 人工闸全流程·U6 模板第二单照抄）

> 票号＝FX-U11｜起草＝架构席（software-team-architect-u10）｜日期＝2026-11-07｜被派＝**工程师席**（FUXI 线）＋**人工闸＝皮总**（S4 停点，非工程师射程）
> 起草时点 HEAD 实测＝`5d6c7a8`（`git log -1` 现盘实跑）；开工 ANCHOR＝开工当轮 HEAD 实测读数，回执开端必附；开工前置对账＝①FX-U10 收口登记已入账（串行令 §七）；②assert-tool 汇总＝`PASS=26 FAIL=1 PENDING_STAGE=0 总数=27`·exit 1 且 BW-3 明细＝3 命中（mrbeast 三处归零实证·余三处＝miyazaki）；③FC-6 active 池条目 1（david 在位）·pending 条目 3；开工读数不符＝停手上报，禁带差开工。status 照登 untracked 若干与本案无关禁带入；他案 PROJINIT 在途零触碰。
> 账权＝FUXI 项目（拍板㊠）：本票及其提案／审计／确认包／确认誊录／回执／QA 件全部落 FUXI 账域（agent-skills/fuxi-skill/.collab/）。
> 来历（自包含，禁指针依赖）：入池规程真源＝agent-skills/fuxi-skill/products/README.md §一在册措辞「入池前置：写入本池必须经**人工确认＋独立提案＋版本审计**；确认前产物落待确认暂存区（pending/）」；§三确认引用行格式钉死（确认件约定名 confirmation.md，四字段＝产物id／人工确认引用／提案件引用／版本审计引用；产物id 与目录名逐字全等；缺件或任一字段空＝该条目计「无人工确认来源」，FC-6 咬）。首单模板已在册＝FX-U6 david-fincher 全流程（票面＝本目录 2026-11-06-FUXI-FX-U6-首单入池实跑票-v1.md·确认誊录件＝agent-skills/fuxi-skill/.collab/decisions/2026-11-06-FUXI-入池确认-david-fincher-perspective-v1.md）。产品席判定件 agent-skills/fuxi-skill/.collab/research/2026-11-06-FUXI-PM-U5-待审区两产物入池资格预检-v1.md（落账 bbed4f0）§二裁 mrbeast＝**够格**：EG-6 一手占比 57.1（样本 14）≥50 过线无受限行；新鲜度窗口 10/14 过（补注依据经 U10 B4 显形）；三缺位如实态与 david 入池时同款。**本票＝mrbeast 入池批第二票＝入池实跑全流程（S0-S6·人工闸·FC-6 池 1→2）。**
> **产品签核行（PM §五口径：active 池入池规程执行＋发布数字口径相关须签）**：随票登记输入＝PM-U5 判定件（路径如上·FUXI 账域在册件合规指针）——§二「够格（无 EG-6 受限行）」＋§三-3 批序「先 mrbeast 后 miyazaki」＋§三-1「入池最终裁＝皮总人工闸」＝**本票获产品签核（判词形态，非弃权）**。
> 指针纪律注：本票面反引号路径＝起草时点目标已在盘者；回执／提案／审计／确认包／誊录等尚未生成件的路径一律裸文写（避免 OA-D6 起草态悬空假报）；落笔前对票面跑 check-pointers --target 自查零 BLOCK。

---

## 〇、复核结论（架构席 2026-11-07 实读实跑实查，票内定稿依据）

1. **FC-6 代码实读**（agent-skills/fuxi-skill/gates/assert-tool.py L1690 起判据体＋L155 CONFIRM_FILE_NAME）：池计数口径＝`_product_entries()` 仅枚举 products 池根直接条目（pending 条目不计池）；条目确认判据＝confirmation.md 内 fenced json 块**恰备四键**全部非空＋产物id 与目录名逐字全等，任一块满足即放行该条目；缺件／json 解析失败／字段缺位或空＝计「无人工确认来源」FAIL。PASS 读数构造式（非空池态）＝`active 池条目 %d·无人工确认来源条目数=0（实条目确认引用行判绿）`——**本票入池后 FC-6 明细钉值预演＝`FC-6 PASS active 池条目 2·无人工确认来源条目数=0（实条目确认引用行判绿）`**。
2. **移池扫描面守恒实读**：产物级扫描面枚举＝池根直接条目＋pending 一层下产物目录——mrbeast 移到池根后仍在同一并集（条目名不变）：ST-3（4 条目）／ST-4（回归条目 24）／ST-9／ST-10／FC-3 产物侧／BW-1／BW-2／BW-3／BW-5(b) 逐条目消费读数预期零变化；`_product_md_texts()` 排除 confirmation.md（确认件属入池规程面非产物正文）＝确认件落位对词表／裸数字／节结构扫描面零扰动。BW-3 余 3 命中＝miyazaki 三处，mrbeast 文件字节零改（git mv）行号零漂移＝明细行逐字节不变。
3. **门禁开工基线（U10 收口态预期）**：汇总 `PASS=26 FAIL=1 PENDING_STAGE=0 总数=27`·exit 1（FAIL＝BW-3 三处＝miyazaki 红账留池，不入本票射程）；selftest 四件 161/40/22/19；run-gates 起草时点现盘 `GATE PASS（发现 9743 条）`exit 0。
4. **mrbeast 入池资格对账**：EG-6 门槛过（57.1≥50；U10 补口径后三件套齐·批级锚措辞）；新鲜度窗口过（10/14·B4 依据显形）；**新候裁项 C＝对象级校准覆盖缺位**（PM-U5 §2.2 首案型）——在册 GS-4 元组级判据不咬＝不阻入池，但确认包 S3 如实呈报面必须专列该缺位与「批级锚非对象级读数」陈述，供皮总裁补标与否（见 §六）。三缺位如实（control_arm 未测／leakage_check 未检／judge 层参考位缺位）与 david 案同款呈报。
5. **确认引用可达性设计**：confirmation.md 三引用字段取**包根相对路径**指针形态（池约定件 §三「确认记录件路径（指针形态允许）」，与 david confirmation.md 在盘实例同制——其引用路径含 `-` 转义形态系首单 json 内 `\u002d` 写法，本单取直写路径即可，FC-6 只判非空与产物id 全等）；run-gates 指针族对新增引用路径的读数漂移＝回执逐数照登＋归因行（FX2-1 口径），不在 FUXI 票内处置仓级门禁面。
6. **拆票位置（U10／U11 两票序中本票位置，理由全量入 U10 票 §〇-6）**：本票＝人工闸票，停点独占（S4）；U10（补口径）＝本票开工前置；无并行第三票（本批闭集＝两票串行）。基数三同源 27／断言闭集零碰贯穿本票（FC-6 判据早已实装，本票＝其产物级实证第二单到位，判据本体零动）。

---

## 一、声明闭集（本票交付面，git 面恰 9 件＝移池 3＋确认件 1＋约定面随动 1＋过程件 4）

1. agent-skills/fuxi-skill/products/mrbeast-perspective/SKILL.md（移池，git mv 字节零改）
2. agent-skills/fuxi-skill/products/mrbeast-perspective/registration.md（同上）
3. agent-skills/fuxi-skill/products/mrbeast-perspective/test-prompts.md（同上）
4. agent-skills/fuxi-skill/products/mrbeast-perspective/confirmation.md（新建·第二单实例·四字段规格 §二 S5）
5. agent-skills/fuxi-skill/products/pending/README.md（§二 S6 条目清单随动目）
6. agent-skills/fuxi-skill/.collab/design/2026-11-07-FUXI-FX-U11-mrbeast入池提案-v1.md（独立提案件·新建）
7. agent-skills/fuxi-skill/.collab/design/2026-11-07-FUXI-FX-U11-mrbeast版本审计-v1.md（版本审计件·新建）
8. agent-skills/fuxi-skill/.collab/research/2026-11-07-FUXI-FX-U11-入池确认包-mrbeast-v1.md（确认包件·新建·呈皮总本体）
9. agent-skills/fuxi-skill/.collab/decisions/2026-11-07-FUXI-入池确认-mrbeast-perspective-v1.md（皮总确认文本誊录·新建·人工闸产物·誊录人＝主理人）

> 门禁面／断言面／产物本体内容面＝零触碰（移池只动位置不动字节）；assert-tool／assertion-catalog／STRUCTURE／SKILL.md／references＝零触；miyazaki-hayao-perspective／elements-of-style-technique／david-fincher-perspective 三产物零触。回执另笔（§五）。

## 二、施工规格（工序序含人工闸停点，落位钉死）

**S0 · 开工前置对账**（§卷头）：U10 收口登记在账＋门禁三读数对账＋BW-3 明细 3 命中在场＋本体 sha 与 U10 收口态对拍。不符＝停手上报。

**S1 · 独立提案件**（闭集第 6 件）：落位 .collab/design/2026-11-07-FUXI-FX-U11-mrbeast入池提案-v1.md（裸文写路径）。内容六节＝①提案头（提案席≠确认人，独立性声明）；②入池对象与轨别（mrbeast-perspective／person／编译形态 single／版本 v0.2／快照 2026-10-31／复审到期 2027-01-29）；③门禁现读全文引用（assert-tool 27 项明细当期读数照录，BW-3 余 3 对象如实＝miyazaki 非本对象）；④EG-6 与窗口陈述（一手占比 57.1≥50 门槛过＋新鲜度 10/14 窗口过＋U10 B4 补注后依据显形陈述＋calibration_state 校准态对账链：κ=0.801887 三处锚＝**批级元组锚**）；⑤风险与缺位如实（**对象级校准覆盖缺位＝候裁项 C 专列陈述**／control_arm 未测／leakage_check 未检／judge 层参考位——四缺位不得读作质量绿）；⑥提案结论（建议入池＋一句话可批的批准话术草案＋若皮总裁「须补标」则本提案转阻塞呈报的分支声明）。

**S2 · 版本审计件**（闭集第 7 件）：落位 .collab/design/2026-11-07-FUXI-FX-U11-mrbeast版本审计-v1.md（裸文写路径）。内容＝①审计对象版本账（v0.2／快照时戳／T9 复跑批次指针）；②随件三文件 sha256 审计基线表（移池前实算，与 S5 移池后对拍基准）；③入池前变更史一行（U10 四处行内改动 commit 指针照登）；④复审到期日核对（AC-5 规则：快照＋90 日＝2027-01-29 逐字对）；⑤审计结论行。

**S3 · 确认包件**（闭集第 8 件·「一句话可批」强度）：落位 .collab/research/2026-11-07-FUXI-FX-U11-入池确认包-mrbeast-v1.md（裸文写路径）。五节＝①一句话请求（「批准 mrbeast-perspective v0.2 入 active 生效池？是／否」）；②资格读数表（门禁 27 项三态汇总＋EG-6 门槛过＋新鲜度窗口过＋U10 补口径 BW-3 mrbeast 归零实证）；③如实呈报面（**候裁项 C 对象级校准覆盖缺位＝随确认一并呈裁：批准入池＝按批级锚接受；须补标＝另开 s0c 扩批工程票**／三缺位如实／BW-3 红账留池对象非本对象）；④引用链（提案件／审计件／PM-U5 判定件路径）；⑤批准话术草案（＝誊录模板：确认人＋日期＋确认文本＋四字段引用行预填值＋对候裁项 C 的裁定一行）。

**S4 · 人工闸停点（工序序显式停点·工程师席在此停手）**：确认包经主理人呈皮总；**皮总确认前，工程师席禁执行 S5 及之后任何动作（禁自行移池、禁预建 confirmation.md）**。皮总确认文本由主理人誊录落闭集第 9 件（.collab/decisions/ 子域·david 誊录件同制）；誊录件含确认原话、确认人、日期、批准范围（限本对象本版本）、候裁项 C 裁定行。回执附誊录件路径与确认日期。

**S5 · confirmation.md 第二单实例＋移池**（闭集第 1-4 件，同一 commit）：
- confirmation.md 全文规格（json 块恰四键·包根相对路径指针形态·直写路径）：
  ```json
  {"产物id": "mrbeast-perspective", "人工确认引用": ".collab/decisions/2026-11-07-FUXI-入池确认-mrbeast-perspective-v1.md", "提案件引用": ".collab/design/2026-11-07-FUXI-FX-U11-mrbeast入池提案-v1.md", "版本审计引用": ".collab/design/2026-11-07-FUXI-FX-U11-mrbeast版本审计-v1.md"}
  ```
  （产物id 与目录名逐字全等；四字段非空；`_product_md_texts()` 排除机制在册＝正文扫描零扰动）
- 移池＝`git mv agent-skills/fuxi-skill/products/pending/mrbeast-perspective → agent-skills/fuxi-skill/products/mrbeast-perspective`（R100 rename 实证，字节零改）；confirmation.md 落移后条目根部。

**S6 · pending/README 条目清单随动**（闭集第 5 件）：条目清单表删除 mrbeast 行（余两行原样＝miyazaki/elements-of-style）；其余约定文本零动（池规程本体零改＝FC-6 判据基面零动）。

**工序序＝S0→S1→S2→S3→**S4 停点呈皮总**→（获确认）誊录落盘→S5→S6→§三验收全跑→回执笔。commit 计划＝四笔：①S1+S2+S3 过程件笔（停点笔）；②誊录件笔（decisions）；③S5+S6 移池笔（恰 5 件）；④回执笔。闸序钉值＝誊录笔（②）早于移池笔（③），git 链序即闸序实证。**

## 三、验收判据（三态禁假绿，全部可机械验证）

1. **FC-6 明细行钉值（池 1→2 产物级实证）**：`python agent-skills/fuxi-skill/gates/assert-tool.py` FC-6 明细行逐字＝`FC-6 PASS active 池条目 2·无人工确认来源条目数=0（实条目确认引用行判绿）`（＝§〇-1 预演钉值）；连跑两次逐字节全等。
2. **汇总守恒钉值（四元守恒自查防 U4 式笔误）**：汇总行逐字 `PASS=26 FAIL=1 PENDING_STAGE=0 总数=27`·exit 1——与开工基线三态计数与基数全等＝入池不新增绿不新增红（FAIL=1＝BW-3 三处 miyazaki 红账存续如实）。
3. **扫描面守恒对账**：除 FC-6 一行外 26 项明细逐字节零变化——BW-3 明细行三命中清单含行号逐字不变（mrbeast 移池字节零改）；ST-3 4 条目／ST-4 回归条目 24／ST-9 4 条目／ST-10 3 条目 18/18／FC-3 要素行 55 行／BW-1、BW-2 扫描 12 件／BW-5 扫描 9 件——confirmation.md 被 `_product_md_texts()` 排除实证；selftest 四件 161/40/22/19 零回归。
4. **移池碰面钉值**：移池笔 `git show --name-status` ≡ 3 条 `R100`＋confirmation.md `A`＋pending README `M`＝恰 5 行；三文件移池后 sha256 ≡ S2 审计基线表逐值全等；products/pending 现盘条目＝2（miyazaki／elements-of-style）；池根条目＝2（david／mrbeast）。
5. **确认链四件套闭合**：提案／审计／确认包／decisions 誊录四件在 git 在场＋confirmation.md 三引用路径逐文件实存在（指针解析可开）；誊录件含确认人＋日期＋批准范围行＋候裁项 C 裁定行。
6. **run-gates 基线零新增红**：exit 0·`GATE PASS`；与开工基线对拍无 BLOCK 新增无红新增；新增引用路径／decisions 件引发的指针族 WATCH 漂移＝逐数照登＋归因行（FX2-1 口径不修不动）。
7. **碰面闭合**：四笔 `git show --name-only` 并集 ≡ §一 9 件＋回执；git diff 对 miyazaki／elements-of-style／david 三产物、gates 全树、docs／contracts／adapters／specs 四面、agent-skills/fuxi-skill/products/README.md（池约定件本体）、宿主装载面、他案面＝零改动。

## 四、禁动面（违任一＝整批退回）

- **人工闸不可代位**：工程师席／产品席／架构席任何一席不得代签确认或预填「人工确认引用」指向非皮总件；S4 前移池＝整批退回＋呈拍。
- **mrbeast 三文件字节零改**（移池只动位置；U10 已改过内容，本票起封字节）；confirmation.md 四字段禁含空值／禁多键（恰备四键＝判据）。
- **miyazaki 红账不入本票**：BW-3 余 3 处不清账不收尾（出清归 miyazaki 自身入池批工序）；elements-of-style-technique／david-fincher-perspective 两产物全树零触。
- **门禁面／断言闭集 27 零碰**；池约定件 agent-skills/fuxi-skill/products/README.md 本体零改（规程变更须另呈产品签核）；evidence 桶不入 git；史账不随正；已裁项不回流。
- **模板复用不扩面**：david 四件套即在册模板（FX-U6），照抄件形；**禁**在本票为模板化改池约定件或新建约定面文件；观察-FX4-1 机械判据面调整不在本票射程（引注不实施）。

## 五、回执要求

裸文写路径＝agent-skills/fuxi-skill/.collab/receipts/2026-11-07-FUXI-FX-U11-工程师回执-v1.md：开工 ANCHOR＋前置对账行（U10 收口在账＋三读数＋本体 sha 对拍）；§三七判据逐条实跑读数全文（FC-6 明细＋汇总＋26 项零变化对拍表＋R100 清单＋sha 对拍表＋确认链四件路径＋run-gates 照登归因）；S4 停点执行陈述（呈报时间／获确认时间／誊录件路径／候裁项 C 裁定读数照登）；四笔 commit 清单＋闸序实证（②早于③）；§〇 复核不一致处如实申报。

## 六、候裁单列

- **候裁项 C（首案型·U10 票 §六同款·随 S3/S4 一并呈皮总）**：对象级校准覆盖缺位——批准入池＝按批级锚接受（缺位如实注随行＝在册口径）；须补标＝本提案转阻塞、另开 s0c 扩批工程票（对象级补标＝新工程射程，不在本两票闭集）。票面读数以「已裁不补标」为基线（U10 措辞前向兼容设计注同款）。
- **新鲜度窗口与 EG-6＝无呈裁项**（mrbeast 两维皆过，与 david 案受限呈裁面不同＝账面最贴 david 模板；david 誊录件裁定附带登记第三行同款重述：BW-3 余三处属 miyazaki 不入本单射程）。
- 观察-FX4-1 在册候补池不重呈（PM-U5 §三-2 判词方向已在册；机械判据面调整须另票＋产品会签走门禁面重交付程序）。

## 七、纪律

一票一批四 commit（§二 commit 计划，人闸切分天然多笔）；**串行令＝U11 开工前置＝U10 收口登记入账**（U10 票 §七同款写明）。QA 席独立核验另票另件，fresh eyes 全实跑：§三判据逐条复现＋对抗例钉死——**对抗一（缺字段拒移池）**：scratch 复制条目构 confirmation.md 缺「提案件引用」字段→FC-6 必计该条目无人工确认来源 FAIL（注入实跑复现后复原，交付面零触）；**对抗二（产物id 不符检出）**：scratch 把产物id 写成 david-fincher-perspective→FC-6 必咬（与目录名逐字全等判据）；**对抗三（提前移池检出）**：对账 commit ③时间戳晚于 commit ②（decisions 誊录笔）——移池笔必在誊录笔之后，git 链序即闸序实证。临时工作物只落本仓根 `.scratch/FX-U11/`；复现门禁基线禁用只读 worktree（教训在册），用仓根现盘态。

——架构席 software-team-architect-u10 起草·2026-11-07·除本票面外零写入。