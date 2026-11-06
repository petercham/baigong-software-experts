# FUXI-FX-U10 · mrbeast-perspective 补口径与内容微动票（BW-3 mrbeast 三处出清·入池批前置小施工）

> 票号＝FX-U10｜起草＝架构席（software-team-architect-u10）｜日期＝2026-11-07｜被派＝**工程师席**（FUXI 线）
> 起草时点 HEAD 实测＝`5d6c7a8`（`git log -1` 现盘实跑＝TK-PROJINIT 工程师回执v1 笔；status 照登 untracked 若干〔`.collab/ledger/`、`.scratch/FX-U*`、`.scratch/PM-U5/`〕与本案无关禁带入；他案 PROJINIT 在途零触碰）；开工 ANCHOR＝开工当轮 HEAD 实测读数，回执开端必附。
> 开工前置对账＝assert-tool 汇总＝`PASS=26 FAIL=1 PENDING_STAGE=0 总数=27`·exit 1（FAIL 恰＝BW-3 六命中：miyazaki 三〔SKILL.md L6/L59、registration.md L36〕＋mrbeast 三〔SKILL.md L34/L62、registration.md L36〕，明细逐字见 §三-1）；selftest 四件＝161/40/22/19 反常 0；FC-6 active 池条目 1（david-fincher-perspective 在位）·pending 条目 3。开工读数不符＝停手上报，禁带差开工。
> 账权＝FUXI 项目（拍板㊠）：本票及其回执／QA 件落 FUXI 账域（agent-skills/fuxi-skill/.collab/）；百工 bundle 账域与 SWB 仓其他账不入本票射程。
> 来历（自包含，禁指针依赖）：BW-3（裸数字三件套检出＝统计口径＋样本量＋一致性系数·行粒度缺任一即咬）FX-U4 离桩转实装后存量红六命中在册（收口登记＝agent-skills/fuxi-skill/.collab/receipts/2026-11-06-FUXI-FX-U4-收口登记-v1.md·U9 收口态复核＝全仓门禁唯一存续红）；红账随各自入池批出清为在册口径（FX-U4 §三＋decisions david 誊录件裁定附带登记第三行同款重述）。产品席判定件 agent-skills/fuxi-skill/.collab/research/2026-11-06-FUXI-PM-U5-待审区两产物入池资格预检-v1.md（落账 bbed4f0）§二裁 mrbeast＝够格（EG-6 一手占比 57.1≥50 过线·新鲜度窗口 10/14 过·无 EG-6 受限行）、§2.3 给前置施工清单 B1-B4、§三-3 批序建议「先 mrbeast 后 miyazaki」。**本票＝mrbeast 入池批第一票＝前置小施工（B1-B4 四处行内原地）；BW-3 六命中→三命中，余三处＝miyazaki 红存续属其自身入池批射程。**
> **产品签核行（PM §五口径：发布数字口径与统计三件套定义＝产品签核面）**：随票登记输入＝PM-U5 判定件（路径如上·落账 bbed4f0·FUXI 账域在册件合规指针），其中 §二 mrbeast 资格判「够格」、§2.1 BW-3 三处逐处定性、§2.3 前置清单 B1-B4、§三-3 批序＝**本票获产品签核（判词形态，非弃权）**。
> 指针纪律注：本票面反引号路径＝起草时点目标已在盘者；回执／收口登记等尚未生成件的路径一律裸文写（避免 OA-D6 起草态悬空假报）；落笔前对票面跑 check-pointers --target 自查零 BLOCK。

---

## 〇、复核结论（架构席 2026-11-07 实读实跑实查，票内定稿依据）

1. **门禁现势实跑取证**（本席仓根现盘实跑，非转述）：assert-tool 汇总＝`PASS=26 FAIL=1 PENDING_STAGE=0 总数=27`·exit 1；BW-3 明细行逐字与 PM-U5 §〇-1 及 FX-U5 票面 §三-1 六命中清单全等（见 §三-1 改前对照）。selftest 四件＝assert-tool 用例 161／s0b-kappa 40／validator-public-anchor 22／validator-source-anchor 19，反常全 0；run-gates 现盘＝`GATE PASS（发现 9743 条，均按路由表走②不拦提交）`exit 0。
2. **mrbeast 本体行号复核**（PM-U5 给值 L62/L36/L34/L37 → 本席现盘实读逐一咬合，无漂移）：SKILL.md＝66 行、registration.md＝38 行；四处落位现文与 PM-U5 §2.1/§2.3 引用逐字相符（全文见 §二 S1-S4 现文行）。本体 sha256 留档对拍＝SKILL.md `1da5d619…`／registration.md `8a987a11…` 与 PM-U5 §〇-4 预检时点留档前缀逐字咬合＝开工前置对账第四行（PM-U5 推翻④条款：本体与他案并发笔不符即停手）。
3. **检出器口径实读**（agent-skills/fuxi-skill/gates/assert-tool.py）：`bare_number_hits()` L436-448＝逐行枚举，行内 `_PERCENT_RE`（L265＝`\d+(?:\.\d+)?\s*%`）或 `_NUMBER_METRIC_RE`（L266＝`(通过率|一致率|占比)[^\d]{0,8}\d+…`）命中→查 NUMBER_CONTEXT_KEYS 三关键词（L90）行内在场，缺任一即咬；＝补第三关键词且携可回查真值方为真补（关键词贴皮＝语义活性对账不通过，§三-5）。四处触发定性：SKILL.md L34＝`+1%` 走 _PERCENT_RE；L62／registration.md L36＝「占比读数/一手占比=57.1」走 _NUMBER_METRIC_RE 缺一致性系数。
4. **κ 真值回查位实读**：mrbeast SKILL.md L15 `calibration_state`=`校准态` 注（s0c-anchors-b1 软/硬两元组·κ 点值 0.801887/1.0）；软门 κ 封印锚值＝agent-skills/fuxi-skill/.collab/receipts/2026-11-06-FUXI-FX-U2-证据哈希封印登记-v1.md＋GS-4 现读 `PASS 元组 2 个在场·κ 报告与 calibration_state 逐元组对账全一致`（anchor-tuple-soft.json 实读 κ点值 0.801887）。**对象级覆盖缺位复核属实**：agent-skills/fuxi-skill/.collab/evidence/harness/s0c-anchors-b1/prereg-s0c.json 预注册对象集＝david-fincher／miyazaki-hayao／eac-30-discipline／mc-70-charter 四对象（mrbeast 不在册）；anchor-labels-soft.json／anchor-labels-hard.json grep「mb-」＝命中 0。＝补口径句**只能取批级元组锚措辞＋缺位如实注随行**，禁 david 先例的「与本产物 calibration_state 同锚」对象级归属句（PM-U5 §2.1 措辞约束）。GS-4 判据实读（gs_4_calibration_kappa() L1431-1465）＝逐 anchor-tuple*.json 元组级对账、无对象级要求＝PM-U5 推翻①不成立，在册口径不阻入池。
5. **措辞前向兼容设计注**（候裁项 C 两态读数基线）：B1/B2 补口径句写「该对象不在 s0c-anchors-b1 批次预注册对象集」——b1 批次预注册＝封印在册历史事实，后续若裁对象级补标（扩新 s0c 批次）此句仍真、不须回改；补标与否归皮总裁（U11 确认闸呈），本票按「已裁不补标」基线施工，缺位如实注随行＝PM-U5 在册口径。
6. **拆票裁定（U10／U11 两票，理由入票）**：①U10（本票）＝产物本体面两文件四行小笔、判据零新增；U11＝入池实跑票＝移池＋规程四件套＋人工闸停点（U6 模板）。两面**盘面对象零交集**（U10 产物文件内容／U11 池结构与过程件），唯一共享＝run-gates 存量基线可能互漂。②U10→U11 强序＝「入池前补口径」在册条款（PM-U5 §2.3 前置清单＋FX-U4 收口态红账随入池批口径）：mrbeast 红账不清则入池动作携红入场。③不合单自证＝若一票合单，BW-3 出清读数（6→3）与 FC-6 移池读数（1→2）混于一笔验收、且人工闸停点会把本体改动笔卡在闸前——收口钉值不混原则下两票分立为最小拆法。基数三同源 27／断言闭集零碰贯穿两票（本批无新断言设计）。

---

## 一、声明闭集（本票交付笔唯一改动面，共 2 件）

1. agent-skills/fuxi-skill/products/pending/mrbeast-perspective/SKILL.md（§二 S1/S3 两目·L62＋L34）
2. agent-skills/fuxi-skill/products/pending/mrbeast-perspective/registration.md（§二 S2/S4 两目·L36＋L37）

> 门禁面／断言面／池盘面＝零触碰；test-prompts.md 零触；miyazaki-hayao-perspective / elements-of-style-technique / david-fincher-perspective 三产物全树零触；assert-tool／assertion-catalog 零触（判据零新增，selftest 161 零增）。回执另笔（§五）。

## 二、施工规格（逐处整行替换，落位钉死；四处皆行内原地——禁增删行）

**S1 · B1＝SKILL.md L62 原地补 κ 口径（批级锚措辞＋缺位如实注随行）**
- L62 整行替换（前后行零动、行数零增减）：
  - 现文：`- 外部请求计数=`3`（本对象六路检索批）；语料 14 要素条目，一手占比读数 57.1（统计口径：本人原文态条目数/要素条目总数；样本量 14）过 EG-6 门槛 50；新鲜度窗口内条目占多数＝窗口过。`
  - 改后：`- 外部请求计数=`3`（本对象六路检索批）；语料 14 要素条目，一手占比读数 57.1（统计口径：本人原文态条目数/要素条目总数；样本量 14；一致性系数 κ=0.801887＝s0c-anchors-b1 软门锚点元组读数（封印在册；本对象不在该批次预注册对象集＝对象级锚覆盖缺位，此值为批级元组读数非对象级读数））过 EG-6 门槛 50；新鲜度窗口内条目占多数＝窗口过。`

**S2 · B2＝registration.md L36 原地补 κ 口径（同 S1 措辞约束）**
- L36 整行替换（前后行零动、行数零增减）：
  - 现文：``- `一手占比门槛`=`50`；`新鲜度窗口月数`=`12`；`一手占比`=`57.1`（统计口径：本人原文态要素条目数/要素条目总数；样本量=`14`）＝门槛过。``
  - 改后：``- `一手占比门槛`=`50`；`新鲜度窗口月数`=`12`；`一手占比`=`57.1`（统计口径：本人原文态要素条目数/要素条目总数；样本量=`14`；一致性系数 κ=0.801887＝s0c-anchors-b1 软门锚点元组读数（封印在册；本对象不在该批次预注册对象集＝对象级锚覆盖缺位，此值为批级元组读数非对象级读数））＝门槛过。``

**S3 · B3＝SKILL.md L34 内容微动出清（脱裸 % 形态·语义零变·禁贴皮）**
- L34 整行替换（前后行零动、行数零增减；行内要素标注段 source_id 等逐字零动）：
  - 现文：`- **留存是一票否决的裁判**：任何变现/包装动作不得杀死留存；连 AI 配音这种「质量略降」的替换也要用留存读数裁决（+1% 即采用）。`证据等级`=`原文可证实`·`来源态`=`本人原文`·source_id=`https://www.creatorspotlight.com/p/minimizing-media`·位置＝「AI dubs retention 引语段」·`abstain_tier`=`有支持``
  - 改后：`- **留存是一票否决的裁判**：任何变现/包装动作不得杀死留存；连 AI 配音这种「质量略降」的替换也要用留存读数裁决（转述态：留存只要上升即采用·该实验增益幅度与三件套随转述源未得＝按转述引用标注不补口径）。`证据等级`=`原文可证实`·`来源态`=`本人原文`·source_id=`https://www.creatorspotlight.com/p/minimizing-media`·位置＝「AI dubs retention 引语段」·`abstain_tier`=`有支持``
- **B3 语义零变约束写死**：裁决规则语义等同性判据＝改后行仍表达「留存读数上升（哪怕质量略降）即采用替换」同一规则；原括注数值门槛（+1%＝百分之一点）属转述源实验幅度读数，脱形后以「上升即采用」保留方向语义＋明示转述源性质——**禁**改为补 κ／补三件套（张冠李戴贴皮＝PM-U5 §2.1 禁形态）；**禁**改 `证据等级`/`来源态`/source_id/位置/`abstain_tier` 五要素段任何字节。QA 可机械核两则：①改后 L34 不含 _PERCENT_RE 命中形态（全行无「%」字符）且不含 _NUMBER_METRIC_RE 命中形态；②语义注记行（本行＋票面 §二 S3 登记）在场。

**S4 · B4＝registration.md L37 新鲜度窗口行补注判定依据显形（非改数）**
- L37 整行替换（前后行零动、行数零增减；既登读数 `10`/`14`＝窗口过 逐字保留禁改）：
  - 现文：`- 新鲜度窗口读数：源件集中于 2025-03~2026-10 发布，落 12 个月窗口内条目=`10`/`14`＝窗口过（如实读数）。`
  - 改后：`- 新鲜度窗口读数：源件集中于 2025-03~2026-10 发布，落 12 个月窗口内条目=`10`/`14`＝窗口过（如实读数；窗内计数逐条判定依据：行内发布锚确证在窗 8 条＝C-MB-01/02/05/07/08/09/10/14＋无行内日锚按源件发布批时推定计入在窗 2 条（推定形态＝依据强度低于确证层、归属未逐条登记＝如实注）＝合计 10；窗外确证 2 条＝C-MB-03（2025-03）、C-MB-04（2025-03-27）；无行内日锚共 4 条＝C-MB-06/11/12/13 其中未计入 2 条；最保守读数＝仅确证层 8/14 仍占多数，窗口过结论稳）。`
- 补注依据对拍源（回执须引用）：agent-skills/fuxi-skill/.collab/evidence/corpus/t9/mrbeast/ 六路条目登记行（C-MB-01..14 逐条 source_id＋位置＋日锚形态现盘实读）＋PM-U5 §二表第 3 行逐条对点读数。禁改既登读数 `10`/`14`；禁改「窗口过」结论；补注只增透明度不减确定性表述（「最保守 8/14 仍占多数」随行）。
- L37 命中态注（回执须实证）：L37 含「条目=`10`/`14`」但**不含**「占比/通过率/一致率」邻近数字形态亦无「%」→**改前改后皆非 BW-3 命中行**＝B4 属登记透明度补注非出清笔；此读数须在回执以改前后 BW-3 明细行逐字对照实证（六→三命中清单中无 L37 项）。

**工序序＝S1→S2→S3→S4→§三验收全跑→回执笔。git 面交付笔＝恰两件（SKILL.md＋registration.md）＋回执笔，可两笔。**

## 三、验收判据（三态禁假绿，全部可机械验证）

1. **BW-3 明细行钉值（6→3）**：`python agent-skills/fuxi-skill/gates/assert-tool.py` BW-3 明细行逐字＝`FAIL 产物报告裸数字 3 处（三件套=统计口径＋样本量＋一致性系数·缺任一即裸）：miyazaki-hayao-perspective/SKILL.md line6 缺统计口径、样本量、一致性系数；miyazaki-hayao-perspective/SKILL.md line59 缺一致性系数；miyazaki-hayao-perspective/registration.md line36 缺一致性系数`（＝开工六命中清单剥 mrbeast 三项、余 miyazaki 三项**逐字含行号零漂移**）；连跑两次逐字节全等。**mrbeast 三处命中归零＝本票出清实证。**
2. **汇总读数钉值（四元守恒）**：汇总行逐字 `PASS=26 FAIL=1 PENDING_STAGE=0 总数=27`·exit 1——与开工基线三态计数与基数全等（BW-3 仍 FAIL＝miyazaki 三处红存续如实，**禁为凑绿触 miyazaki 本体**；FAIL=1 项性不变＝红账随入池批条款续行至 miyazaki 入池批）。
3. **涉门禁断言消费面零碰**：断言编号闭集 27 两票零动（本票零新增零删）；assert-tool selftest 用例 161／s0b-kappa 40／validator-public-anchor 22／validator-source-anchor 19 四件零回归·反常 0；ST-3 条目 4·ST-4 回归条目 24·ST-9 四条目·ST-10 三条目 18/18·FC-3 要素行 55 行·FC-6 池条目 1·GS-4 元组 2·BW-1/BW-2/BW-5 命中 0——除 BW-3 一行外 26 项明细逐字节零变化。
4. **BW-3 命中行号前后对照表（入票·回执照登实跑复核）**：
   - 改前六处：`miyazaki-hayao-perspective/SKILL.md line6`／`miyazaki-hayao-perspective/SKILL.md line59`／`miyazaki-hayao-perspective/registration.md line36`／`mrbeast-perspective/SKILL.md line34`／`mrbeast-perspective/SKILL.md line62`／`mrbeast-perspective/registration.md line36`
   - 改后三处：miyazaki 三项逐字同上（行号零漂移实证＝四处改动皆行内原地、行数零增减：SKILL.md 66→66 行、registration.md 38→38 行）；mrbeast 三项归零。
5. **语义活性对账（非贴皮实证）**：S1/S2 补口径句 κ 值 0.801887 与三处回查位对账全一致——①mrbeast SKILL.md L15 元数据行 κ 点值；②FX-U2 证据哈希封印登记件所载软门 κ；③assert-tool GS-4 明细行「逐元组对账全一致」现读；回执附三处读数引文。**对象级缺位如实注两行在场实证**＝改后 L62／L36 各含「对象级锚覆盖缺位」字样（禁对象级归属句实证）。
6. **B3 出清机械核**：改后 SKILL.md L34 全行不含「%」字符（`grep -c '%'` 对 L34＝0）、不含「占比/通过率/一致率＋数字」邻近形态；语义注记随行在场（「转述态」字样）；行内五要素段（证据等级／来源态／source_id／位置／abstain_tier）与现文逐字节全等。
7. **B4 非改数机械核**：改后 registration.md L37 含子串「条目=`10`/`14`＝窗口过」逐字在场；既登数 10/14/12/50/57.1 五值零改动（改动前后 diff 仅括注追加段）。
8. **run-gates 基线零新增红**：`bash agent-skills/object-audit/scripts/run-gates.sh` exit 0·`GATE PASS`；与开工基线 9743 条对拍＝无 BLOCK 新增、无红新增；存量逐数照登＋漂移归因行（FX2-1 口径，不在 FUXI 票内处置仓级门禁面）。
9. **碰面闭合**：交付笔 `git show --name-only` ≡ §一 两件；git diff 对 miyazaki-hayao-perspective／elements-of-style-technique／david-fincher-perspective 三产物全树、mrbeast test-prompts.md、gates 全树、docs／contracts／adapters／specs 四面、池约定件两件（agent-skills/fuxi-skill/products/README.md、agent-skills/fuxi-skill/products/pending/README.md）、仓级面／他案在途面＝零改动；两件文件 diff 各仅两行（SKILL.md 两行／registration.md 两行·行数零增减实证）。

## 四、禁动面（违任一＝整批退回）

- **三产物全树零触碰**：miyazaki-hayao-perspective（红账归其自身入池批）／elements-of-style-technique／david-fincher-perspective（已入池生效件，改动＝判别口径双证据违例）；禁顺手补 miyazaki 口径凑绿。
- **mrbeast test-prompts.md 零触**；mrbeast 本体除 §二 四行外任何行零触（含 L12-L16 元数据行、L15 `calibration_state` 声明行、L58-L66 诚实边界节余行）。
- **门禁面零碰**：assert-tool／assertion-catalog／validator 三件／s0b-kappa／基数三同源＝U9 收口态原样；断言闭集 27 零碰（本票无新断言）。
- **补口径≠改读数**：κ=0.801887 取在册封印锚值、57.1／14／50／12／10／窗口过结论等既登数值与结论零改动；禁改 `calibration_state` 行；禁改 EG-6 判定结论；禁把 L37 补注写成改数或改判。
- **候裁项 C 不入施工闭集**：本票不建对象级标注、不改 prereg-s0c.json、不扩 s0c 批次、不新增 anchor 文件（evidence 桶不入 git 且封印面不可追改）。
- **史账不随正；已裁项不回流；宿主装载面（`~/.workbuddy/skills/fuxi-skill/`）零触碰；仓外零写入**；临时工作物只落仓根 `.scratch/FX-U10/`。

## 五、回执要求

裸文写路径＝agent-skills/fuxi-skill/.collab/receipts/2026-11-07-FUXI-FX-U10-工程师回执-v1.md：开工 ANCHOR 实测 HEAD＋开工基线四读数对账行（assert 汇总＋BW-3 六命中在场＋selftest 四件＋本体 sha 对拍 PM-U5 留档）；§三九判据逐条实跑读数全文（BW-3 三命中明细全文＋汇总行＋exit code＋26 项零变化对拍表＋κ 三处回查引文＋缺位注两行在场实证＋B3/B4 机械核引文＋run-gates 照登归因）；两件改前改后 sha256 对照＋行数对照（66/38 不变）；`git show --name-only` 清单；§〇 复核不一致处如实申报。一票一批一 commit（交付＋回执可两笔）。

## 六、候裁单列

- **候裁项 C（首案型·不入施工闭集·裁决归皮总·U11 确认闸时呈）**：mrbeast `calibration_state`=`校准态` 的**对象级校准覆盖缺位**——mrbeast 不在 s0c-anchors-b1 预注册四对象集、封印标注面无 mb- 条目；在册 GS-4 判据（元组级对账·assert-tool L1431-1465 实读无对象级要求）不咬＝**不阻入池**；补口径句已按批级锚措辞＋缺位如实注随行（§二 S1/S2）。是否补齐对象级支撑（扩 s0c 批次补标＝新工程票射程）或按批级锚接受入池＝皮总裁；本票对「已裁不补标」与「已裁补标」两态的读数**以不补标为基线**，缺位如实注随行＝PM-U5 在册口径（§〇-5 前向兼容设计注）。
- **观察-FX4-1 兑现表态引注不实施**：PM-U5 §三-2 产品段正式表态（BW-3 三件套随行义务限「发布统计数字」；门禁断言编号与转述源内未补齐口径的引用数字不属发布统计）——其**涉机械判据面调整须架构另票＋产品会签走门禁面重交付程序，不在本批射程**，本票只引注不实施；本票 B3 按 PM-U5 §2.1 逐处定性以内容微动出清，＝口径未改前提下的合规路径。

## 七、纪律

一票一批一 commit（交付＋回执两笔）；**串行令＝U10 收口登记入账为 U11 开工前置**（U11 票面 §七同款写明）。QA 席独立核验另票另件，fresh eyes 全实跑：§三判据逐条复现＋对抗例钉死——**对抗一（假补检出）**：scratch 复制 mrbeast 条目，对 L62/L36 做「只贴关键词不携 κ 真值」式假补→BW-3 机械层必放（行粒度口径本义），但语义活性抽查（§三-5 三处回查对账）必判假补不合规＝「机械绿＋语义不达标」双态实证，真补须 κ 值随行；**对抗二（对象级归属句越界检出）**：scratch 对 L62 贴 david 先例措辞「与本产物 calibration_state 同锚」→§三-5 缺位注在场核必判违例（mrbeast 非四对象集成员＝该句为假陈述）；**对抗三（行号漂移防护）**：在 SKILL.md L62 前插入空行→miyazaki 三命中行号必漂移（复现行粒度对行数敏感）→复原→三命中明细与 §三-1 钉值全等；**对抗四（改数防护）**：scratch 把 L37 `10`/`14` 改为 `8`/`14`→§三-7 子串在场核必判违例（B4＝补注非改数）→复原。复现门禁基线禁用只读 worktree（FX-U2 教训在册），用仓根现盘态。

——架构席 software-team-architect-u10 起草·2026-11-07·除本票面外零写入。