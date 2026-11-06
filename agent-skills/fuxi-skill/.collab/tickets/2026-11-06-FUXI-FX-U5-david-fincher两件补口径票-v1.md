# FUXI-FX-U5 · david-fincher 两件三件套补口径票（BW-3 红账清偿首笔·入池前补口径工序入册本体侧落地）

> 票号＝FX-U5｜起草＝架构席（arch-fuxi-u5）｜日期＝2026-11-06｜被派＝**工程师席**（FUXI 线）
> 起草时点 HEAD 实测＝`20e1141`（FX-U4 收口登记笔·`git rev-parse HEAD` 实跑；status 照登 untracked 若干〔`.collab/ledger/`、`.scratch/FX-U2~U4-qa/`、`.scratch/FX-U3/`、`.scratch/FX-U4/`、`.scratch/qa-gwprev/`、`.scratch/qa-rpubrev/`、`.scratch_wbdocs.html`〕与本案无关禁带入；他案 TK-GWP 在途零触碰）；开工 ANCHOR＝开工当轮 HEAD 实测读数，回执开端必附；开工前置对账＝assert-tool 汇总读数＝FX-U4 收口态 `PASS=25 FAIL=1 PENDING_STAGE=1 总数=27`·exit 1＋BW-3 明细含 david-fincher 两处命中在册（开工读数不符＝停手上报，禁带差开工）。
> 账权＝FUXI 项目（拍板㊠）：本票及其回执／QA 件落 FUXI 账域（`agent-skills/fuxi-skill/.collab/`）；百工 bundle 账域与 SWB 仓其他账不入本票射程。
> 来历（自包含，禁指针依赖）：BW-3（裸数字三件套检出：统计口径＋样本量＋一致性系数）已于 FX-U4 离桩转实装（收口登记＝`.collab/receipts/2026-11-06-FUXI-FX-U4-收口登记-v1.md`，落账 `20e1141`），收口态携 8 处真实存量违例红在册（FX-U4 回执 `219c63b` 件内逐字清单：david-fincher 两件〔SKILL.md line61＋registration.md line36，均缺一致性系数〕＋miyazaki-hayao 三处＋mrbeast 三处）。FX-U4 收口登记 §三在册口径＝「红不清账，账在 FX 账线随入池票清」；产品席 PM-U1 判定件（`.collab/research/2026-11-04-FUXI-PM-U1-下一段优先级产品判定-v1.md`）§二第5行尾在册＝「BW-3 红处置随入池批＝入池前补口径工序入册」；§三排期第三段＝「首单入池实跑（david-fincher-perspective）＋SKILL.md/references 换代」。PM §二第4行钉首单＝david-fincher（EG-6 一手占比过门槛、无受限行）。**本票＝第三段首票＝入池前补口径工序本体侧落地＝BW-3 红账清偿首笔（david 两件归零）；miyazaki/mrbeast 两产物红账留池不入本段射程（§四）。**
> **产品签核行（PM §五口径：发布数字口径相关处置须签）**：产品席判词已在册＝PM-U1 §二第5行尾「BW-3 红处置随入池批＝入池前补口径工序入册」＋§二第4行「首单＝david-fincher-perspective」＋§三第三段排期（路径＝`agent-skills/fuxi-skill/.collab/research/2026-11-04-FUXI-PM-U1-下一段优先级产品判定-v1.md`）＝**本票获产品签核（判词形态，非弃权）**。

---

## 〇、复核结论（架构席 2026-11-06 实读实跑实查，票内定稿依据）

1. **门禁现势实跑取证**（本席仓根现盘实跑，非转述）：assert-tool 汇总＝`PASS=25 FAIL=1 PENDING_STAGE=1 总数=27`·exit 1（FAIL 恰＝BW-3）；BW-3 明细行逐字在册＝8 命中清单（与 FX-U4 回执清单全等）：
   - `david-fincher-perspective/SKILL.md line61 缺一致性系数`
   - `david-fincher-perspective/registration.md line36 缺一致性系数`
   - `miyazaki-hayao-perspective/SKILL.md line6 缺统计口径、样本量、一致性系数`／`…SKILL.md line59 缺一致性系数`／`…registration.md line36 缺一致性系数`
   - `mrbeast-perspective/SKILL.md line34 缺统计口径、样本量、一致性系数`／`…SKILL.md line62 缺一致性系数`／`…registration.md line36 缺一致性系数`
   selftest 四件＝155／40／22／19（反常全 0）；run-gates 现盘＝`GATE PASS（发现 9503 条，均按路由表走②不拦提交）`exit 0（存量较 FX-U3/U4 起草基线 9479 的漂移属他案在途项，回执照登归因不修不动）。
2. **补口径目标行实读**（两件现文）：david SKILL.md L61＝「外部请求计数=`3`（本对象六路检索批）；语料 12 要素条目，一手占比读数 58.3（统计口径：本人原文态条目数/要素条目总数；样本量 12）过 EG-6 门槛 50。」——行内已有「统计口径」「样本量」两关键词，缺「一致性系数」；david registration.md L36＝「`一手占比门槛`=`50`；`新鲜度窗口月数`=`12`；`一手占比`=`58.3`（统计口径：本人原文态要素条目数/要素条目总数；样本量=`12`）＝门槛过。」——同款缺一致性系数。检出器口径实读（assert-tool `bare_number_hits` L425 区＋`NUMBER_CONTEXT_KEYS`＝三关键词行内在场检，缺任一即咬）＝补一行内第三关键词、且该关键词须携带可回查真值，非关键词贴皮。
3. **一致性系数真值回查位实读**：david SKILL.md L15 `calibration_state`=`校准态` 注「元组 2 在场（s0c-anchors-b1 软/硬两元组·κ 点值 0.801887/1.0）」；软门 κ 封印锚值＝FX-U2 证据哈希封印登记件（`.collab/receipts/2026-11-06-FUXI-FX-U2-证据哈希封印登记-v1.md`）＋GS-4 现读 `PASS 元组 2 个在场·κ 报告与 calibration_state 逐元组对账全一致`——补口径句所携 κ 值取软门锚点 0.801887，与产物元数据行、封印件、GS-4 读数三处可交叉对账＝语义活性（QA 抽查面，§七）。
4. **零碰面预演**：补口径为两文件行内原地改写（禁增删行）→同文件其余行行号不变（miyazaki/mrbeast 六命中行号零漂移）；david L61/L36 非 FC-3 要素行（不含 `证据等级`＋`来源态` 双 token，补口径句禁引入该两 token）；BW-1/BW-2/BW-5 词表对补口径句零命中（补口径措辞已按现词表预检）；ST-3/ST-9 节结构零触（节内行改）；GS-4 只消费 `calibration_state` 声明行（L15 零触）。＝**除 BW-3 外 26 项读数预期零变化，BW-3 明细 8→6、三态计数与 exit 码不变**（预演取证＝§三-1/2 钉值）。
5. **拆分裁定（U5／U6／U7 三票，理由入票）**：①U5（补口径）＝产物本体面两文件小笔、判据零新增；U6（入池实跑）＝池盘面移池＋规程四件套＋人工闸停点；U7（入口换代）＝包根 SKILL.md/references 新建＋STRUCTURE 声明随动——三面**盘面对象零交集**（U5 产物文件内容／U6 池结构与过程件／U7 入口件面），唯一共享＝run-gates 存量基线可能互漂。②U5→U6 强序＝「入池前补口径」在册条款（PM §二第5行尾），david 红账不清则入池动作携红入场＝再造漂亮读数（PM §四风险句同型）；③U7 与 U5/U6 零盘耦合且不含人工闸，并行以免 U6 停点期间全线空等。**结论＝三票；开工序＝U5 先、U6 随（前置＝U5 收口登记入账）、U7 与两票并行可随时开工（互不越面各如 §四）。** 基数三同源 27／断言闭集零碰贯穿三票（本段无新断言设计）。

---

## 一、声明闭集（本票交付笔唯一改动面，共 2 件）

1. `agent-skills/fuxi-skill/products/pending/david-fincher-perspective/SKILL.md`（§二 S1 一目）
2. `agent-skills/fuxi-skill/products/pending/david-fincher-perspective/registration.md`（§二 S2 一目）

> 门禁面／断言面／池约定面／STRUCTURE 面＝零触碰（补口径＝FX-U4 §三-6「补口径后重报」的产品段工序本体侧落地，非门禁票射程）；`test-prompts.md` 零触；miyazaki/mrbeast 两产物全件零触；assert-tool／assertion-catalog 零触（判据零新增，selftest 155 零增）。

## 二、施工规格（逐件逐行，落位钉死）

**S1 · david SKILL.md（L61 原地补第三件套）**
- L61 整行替换（前后行零动、行数零增减）：
  - 现文：`- 外部请求计数=`3`（本对象六路检索批）；语料 12 要素条目，一手占比读数 58.3（统计口径：本人原文态条目数/要素条目总数；样本量 12）过 EG-6 门槛 50。`
  - 改后：`- 外部请求计数=`3`（本对象六路检索批）；语料 12 要素条目，一手占比读数 58.3（统计口径：本人原文态条目数/要素条目总数；样本量 12；一致性系数 κ=0.801887＝软门锚点元组读数（s0c-anchors-b1 封印在册，与本产物 `calibration_state`=`校准态` 同锚））过 EG-6 门槛 50。`

**S2 · david registration.md（L36 原地补第三件套）**
- L36 整行替换（前后行零动、行数零增减）：
  - 现文：`- `一手占比门槛`=`50`；`新鲜度窗口月数`=`12`；`一手占比`=`58.3`（统计口径：本人原文态要素条目数/要素条目总数；样本量=`12`）＝门槛过。`
  - 改后：`- `一手占比门槛`=`50`；`新鲜度窗口月数`=`12`；`一手占比`=`58.3`（统计口径：本人原文态要素条目数/要素条目总数；样本量=`12`；一致性系数 κ=0.801887＝软门锚点元组读数（s0c-anchors-b1 封印在册，与本产物元数据 `calibration_state`=`校准态` 同锚））＝门槛过。`
- 措辞纪律：两行改后须仍为单行（禁换行拆行）；禁引入 `证据等级`／`来源态` 反引号 token（防误入 FC-3 要素行面）；禁触碰其余任何行含 L15 元数据行。

**工序序＝S1→S2→§三验收全跑→回执笔。git 面交付笔＝S1/S2 恰两件＋回执笔可两笔。**

## 三、验收判据（三态禁假绿，全部可机械验证）

1. **BW-3 明细行钉值（8→6）**：`python agent-skills/fuxi-skill/gates/assert-tool.py` BW-3 明细行逐字＝`FAIL 产物报告裸数字 6 处（三件套=统计口径＋样本量＋一致性系数·缺任一即裸）：miyazaki-hayao-perspective/SKILL.md line6 缺统计口径、样本量、一致性系数；miyazaki-hayao-perspective/SKILL.md line59 缺一致性系数；miyazaki-hayao-perspective/registration.md line36 缺一致性系数；mrbeast-perspective/SKILL.md line34 缺统计口径、样本量、一致性系数；mrbeast-perspective/SKILL.md line62 缺一致性系数；mrbeast-perspective/registration.md line36 缺一致性系数`（＝开工清单剥 david 两项、余六项逐字含行号零漂移）；连跑两次逐字节全等。**david 两件命中归零＝红账清偿首笔实证。**
2. **汇总读数钉值（守恒不变）**：汇总行逐字 `PASS=25 FAIL=1 PENDING_STAGE=1 总数=27`·exit 1——三态计数与开工基线全等（BW-3 仍 FAIL＝余六处他产物红存续如实，**禁为凑绿触 miyazaki/mrbeast 本体**；FAIL=1 项性不变＝红账随入池批条款续行至 U6/U7 收口）。
3. **零碰面读数对账**：与开工基线逐行 diff＝判定列零变化，读数列变化仅 BW-3 一行；其余 26 项读数逐字节零变化（含 ST-3／ST-4／FC-3／BW-1／BW-2／BW-5／GS-4 对 david 文件消费位改后复扫读数）；selftest 四件＝155／40／22／19 零回归。
4. **语义活性对账（非贴皮实证）**：两处补口径句 κ 值 0.801887 与三处回查位对账全一致——①david SKILL.md L15 元数据行 κ 点值；②FX-U2 证据哈希封印登记件所载软门 κ；③assert-tool GS-4 明细行「逐元组对账全一致」现读；回执附三处读数引文。
5. **run-gates 基线零新增红**：`bash agent-skills/object-audit/scripts/run-gates.sh` exit 0·`GATE PASS`；与开工基线（起草时点 9503 条上下）对拍＝无 BLOCK 新增、无红新增；存量逐数照登＋漂移归因行。
6. **碰面闭合**：交付笔 `git show --name-only` ≡ §一 两件；`git diff` 对 miyazaki/mrbeast 两产物全树／`products/README.md`／`products/pending/README.md`／`gates/` 全树／`docs/`／`contracts/`／`adapters/`／`specs/`／仓级面／他案 TK-GWP 在途面＝零改动；两件文件 diff 仅各一行（行数零增减实证）。

## 四、禁动面（违任一＝整批退回）

- **miyazaki/mrbeast 两产物本体零触碰**（红账留池不入本段射程＝PM §三第三段射程＋§〇-5 拆分裁定）；禁顺手补其口径凑绿。
- **门禁面零碰**：assert-tool／assertion-catalog／validator 三件／s0b-kappa／基数三同源＝FX-U4 收口态原样；断言闭集 27 零碰（本票无新断言）。
- **补口径≠改读数**：κ／58.3／12／50 等既登数值零改动；禁改 `calibration_state` 行；禁改 EG-6 判定结论（门槛过／窗口不过受限行原样）。
- **evidence 桶不入 git；史账不随正；已裁项不回流**（FX-U4 收口态、PM 排期判定均在册）。
- **宿主装载面（`~/.workbuddy/skills/fuxi-skill/`）零触碰**；仓外零写入。

## 五、回执要求

`.collab/receipts/2026-11-06-FUXI-FX-U5-工程师回执-v1.md`：开工 ANCHOR 实测 HEAD＋开工基线读数对账行（＝FX-U4 收口态三读数＋BW-3 八命中清单在场）；§三六判据逐条实跑读数全文（BW-3 六命中明细全文＋汇总行＋exit code＋26 项零变化对拍表＋κ 三处回查引文＋run-gates 照登归因）；两件改前改后 sha256 对照（红账清偿证据链）；`git show --name-only` 清单；§〇 复核不一致处如实申报。一票一批一 commit（交付＋回执可两笔）。

## 六、候裁单列

- **候裁无**。补口径去向＝PM §二第5行尾在册条款本体侧执行；κ 取值面＝三处在册锚值对账，无新对立主张；观察-FX4-1（转述引用行三件套随行口径细化）在册候补池，本票不预裁不扩面（david 两处非转述引用行型）。

## 七、纪律

一票一批一 commit（交付＋回执可两笔）；**串行令＝U5 为第三段首票**：U6 开工前置＝U5 收口登记入账（U6 票面 §七同款写明）；U7 与 U5 并行合法（盘面对象零交集，§〇-5），但 U7 回执不得引用 U5 在途读数作基线（各以开工当轮实读为准）。QA 席独立核验另票另件，fresh eyes 全实跑：§三判据逐条复现＋对抗例钉死——**对抗一（假补检出）**：scratch 复制 david 条目，对 L61/L36 做「只贴关键词不改语义」式假补（如行尾裸加「一致性系数」四字无 κ 值）→BW-3 机械层必放（行粒度口径本义），但语义活性抽查（§三-4 三处回查对账）必判假补不合规＝登记「机械绿＋语义不达标」双态实证，真补必须 κ 值随行；**对抗二（行号漂移防护）**：在 L61 前插入空行→其余六命中行号必漂移（复现 BW-3 行粒度对行数敏感）→复原→六命中明细与 §三-1 钉值全等；**对抗三（越面防护）**：确认 miyazaki/mrbeast 两件 registration L36 未被同款顺补（`git diff` 白名单对拍）。临时工作物只落本仓根 `.scratch/FX-U5/`；复现门禁基线禁用只读 worktree（FX-U2 回执教训在册），用仓根现盘态。

——架构席 arch-fuxi-u5 起草·2026-11-06·除本票面外零写入。