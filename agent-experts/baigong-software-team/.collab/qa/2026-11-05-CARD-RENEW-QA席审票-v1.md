# CARD-RENEW 票面 QA 席独立审票 v1（B 席·证伪导向·fresh eyes）

> 【来源】QA席·双席独立审票（B 席）＋ 2026-11-05。A 席＝产品席并发独立审，本席未读其任何产出（fresh eyes）。
> 性质：审票件（只读审查，零施工，唯一写入＝本件）。
> 开工读数：`git rev-parse --short HEAD` 实测 `da25666`（CARD-RENEW 挂 HOLD 笔）。
> 被核件：`agent-experts/baigong-software-team/.scratch/tickets/2026-11-05-CARD-RENEW-卡片换代与席位命名换代施工票.md`（实测 357 行；派工书称 356 行，差一行为末行换行计数口径差，不构成判项）。
> 裁定真源：`.collab/decisions/2026-11-05-皮总裁定-席位职业标签与花名换代.md`（4d52e88）＋ `.collab/decisions/2026-11-05-主理人裁定-CARD-RENEW候裁八条.md`（bda4fec）。
> 计数口径：本件全部 grep 计数为 occurrence 口径（`grep -ro/-rn`），逐项就地附命令与读数原文。
> **总裁决：红 1 ／ 黄 5 ／ 绿 8——票面可施工性＝有条件通过：R1 一行修（声明块头去括注）清账前，工程师对 A7 必然无法绿，HOLD 不宜撤。**

---

## 必做① T 节六个 JSON 块独立语法校验＋两卡同值断言

**PASS。** 实测：`re.findall(r'```json\n(.*?)```')` 从票面抽块＝6 块；逐块值形态包壳解析（补外层 `{}`、去尾逗号）全过——block1 `displayDescription`／block2 `defaultInitPrompt`／block3 `tags`／block4 `quickPrompts` len=6／block5 `members` len=5（lead,product,architect,engineer,qa）／block6 `members` len=5（lead,product,architect,qa,engineer）。block6 顺序与包装卡现行 L55–96 实态顺序一致（票面 L232 顺序保持注 ✓）；block6 每项 `name`＋`displayName` 两键同值＝与包装卡现行两键结构（plugin.json L58–59 等）吻合 ✓。
两卡同值断言可机械复现：T2.2–2.5＝「替换为 T1.2/T1.3/T1.5/T1.6 同一块（逐字）」＝指针式同值，机械判据＝施工后 `diff <(jq .displayDescription 两卡)` 类比对可执行；候裁③已裁两卡 description 统一 ✓。
行号锚核对（现盘直读）：T1 七目锚 L3/L4/L42–45/L48–51/L53–57/L58–71/L72–108 与 `.codebuddy-plugin/plugin.json` 现行块界全对齐 ✓；T2 六目锚 L3/L4/L39–42/L45–49/L50–54/L55–96 与 `plugin.json` 现行块界全对齐 ✓；T3 bundle.lock L5＝`"version": "0.1.22"` 实测在位 ✓（bundle.lock 内 `"version"` 键仅此一处，A4 的 `grep -n '"version"'` 三读数口径干净）。

## 必做② A1–A8 逐条可机械性审查（旧名归零扫描实跑＋白名单封闭性）

**A1/A2 归零扫描实跑（换代前基线）＝PASS（口径成立、白名单封闭、无必然拦截／无漏网）：**
- 命令原文：`grep -roE "齐活林|许清楚|高见远|寇豆码|严过关" agent-experts/baigong-software-team/ --include="*.md" --include="*.json"`（A1）；同口径断言串 `交付总监|Delivery Director|QA工程师|QA 工程师|QA Engineer|Software Architect|Software Engineer`（A2）。两串在现盘均可跑通、非空转。
- **白名单外全部命中逐行点名核对**（A1∪A2）：README L3/L11（T7.1/T7.2 覆盖）；README L61（＝版本账 v1.2.3 行，实测在位＝白名单豁免样例 ✓）；docs/PRODUCT.md L8/L10/L48–52（T6.1 覆盖）；docs/ARCHITECTURE.md L15–19/L74–78（T6.2 覆盖）；plugin.json L58–91 段（T2.6 整块覆盖）；.codebuddy-plugin/plugin.json L44/L49/L50/L60–61/L75–76/L82/L89/L96/L97/L103–104 段（T1.3/T1.4/T1.6/T1.7 覆盖）；五席位卡各 2 处（frontmatter＋标题行，T4 覆盖）；五技法卷命中全部落在 T5 逐行点名内（standard-sop L8/15/20/31/38/41、quick-mode L12/18、bugfix-path L12/17/20、collab-rules L10、partial-workflows L13）。**无一命中落在 21 件闭集外＝工程师不会因漏覆盖被 A1/A2 必然拦死；无一旧名命中在闭集内而 T 节无替换动作＝无漏网。**
- 白名单外文件类型补充扫描：`grep -rlE <A1∪A2 词族>` 排除 *.md/*.json 后包内命中＝**0**（含 SKILL.md、模板、脚本全扫）——A1/A2 的 `--include` 两型口径无漏型。
- 起草席「其余技法卷/sop 副本/SWB 交接件零命中」断言复测：`skills/`（排除 T5 五卷）旧名∪A2 词族命中＝0 ✓；`docs/SWB-交接件v2.9-*.md` 旧名∪QA 词族命中＝0 ✓（禁碰面成立且无 A1/A2 违例风险）。
- **A2 三分账注记成立**：新串「架构工程师/开发工程师」内含裸「架构师/工程师」，裸词不入断言串（候裁①已裁）→ 无自撞；`Software Architect` 换代后无残留载体（架构卡现行 en＝"Architect"，见 G8 注）。
- A3：**≥1 断言可跑，括注数目失准＝黄 Y3**（见分账）。
- A4：PASS（F7 前后值均可实测：前值 0.1.22 三读数实取）。
- A5：实体读数＝`agent-skills/object-audit/scripts/run-gates.sh` 在盘 ✓。
- A6：实体读数＝`agent-skills/object-audit/scripts/check-pointer-closure.py` 在盘 ✓；本席现跑（只读）＝exit 0、WATCH 存量若干（multi-collab refs 旧账，与本案无关）——「不新增」对比口径可执行 ✓，但见 Y2 漏网路径注。
- A7：**FAIL＝红 R1**（见分账）。
- A8：三哈希前值 `3f335333…/7214ad14…/efb4f765…` 与 README v0.1.19 行（L44）所载逐字同 ✓；name-only 对账口径（改名 old/new 双列）可执行 ✓。

## 必做③ 声明闭集 21 件 vs 改动面闭集对账＋头像引用成对

**声明闭集 21＝改动面闭集 21 逐条全等 ✓**（python 集合对账：声明 21 条＝16 改＋5 改名新位；改动面 16＋5 改名对＝同名同数；声明集无多无漏）。
**头像引用成对核＝两处引用面成立、第三面漏网＝黄 Y2**：旧头像文件名全仓（排除 .collab/.scratch）命中＝两卡各 5 处（.codebuddy L77/84/91/98/105＋plugin.json L61/69/77/85/93＝T1.7/T2.6 整块随替换，成对 ✓）＋**README L68 一处（不在 T7 改动目内）**——git mv 后该行五旧文件名＝死引用；且 check-pointer-closure 现跑不抓该处（L68 文件名列表无反引号包裹，非指针解析射程）→ A6 「不新增」判据对其失明。另 README L68 整段「盘上无头像素材，avatars/ 仅 .gitkeep 占位」与实测（avatars/ 六 png 在盘、无 .gitkeep）已不符＝旧债，随票不随动则留第二口径。`avatars/team.png` 两引用（两卡 L46/L43）零动断言 ✓。席位卡内无 png 引用（grep png agents/ ＝0）→「两卡＋席位卡内引用？」疑虑实测＝席位卡无引用面，票面引用面认定完整。
改名旧位 5 路径不入声明闭集（只列新位）：A8 双列对账口径可覆盖，check-ticket-reconcile 对 mv 旧位的实际消化行为未验证＝观察项（随 R1 修复后施工回执可检）。

## 必做④ run-gates 实体路径读数

**PASS。** 票面 A5 所引 `agent-skills/object-audit/scripts/run-gates.sh` ＝ `ls` 实测在位；其 SCRIPTS 行（L136）含 check-pointer-closure/check-ticket-reconcile＝A6/A7 所引器同盘 ✓。

## 必做⑤ 映射总表 vs 裁定原文逐字一致性

**PASS。** 五席 zh/en/职业/avatar 映射逐项对照裁定原文（4d52e88 照录段）：交付总监→项目负责人✓／产品经理不变✓／架构师→架构工程师✓／工程师→开发工程师✓／QA→质量审计师（票面记「QA工程师→质量审计师」＝对裁定字面「QA」的合理解释，无歧义席）✓；花名五项逐字✓；**「高远见→顾长远」笔误注记忠实**：票面 L17 注记↔裁定注记①全同（映射对象＝架构席花名，裁定择「顾长远」弃自拟「顾远鉴」，票照裁）✓；en 随动五项＋职业 en 五值与裁定注记②逐项同✓；候裁八条在票面全部落位（①裸泛指不换→口径②③＋各 T 注✓；②项目负责人照原文✓；③两卡 description 统一新串＝T1.2/T2.2✓；④PRODUCT L8 同新文＝T6.1.7（文本缺位见 Y1）；⑤动词不动＝T5 各行动词保留✓；⑥图像登记零动＝T8.4✓；⑦quickPrompts 6 条＋预览实测截断＝T1.6/T7 候裁⑦保留✓；⑧头像回退预案＝候裁⑧保留✓）。
注记一条（非违例）：裁定注记②写「Software Architect→Architect Engineer」，而架构卡现行 en＝"Architect"——**票面 T4.3 按盘面实值 `en: "Architect"` 起手替换＝票从盘、正确**；措辞差在裁定注记侧，不属本案违例。

---

## 红黄绿分账

**红 1**
- **R1（A7 机械拦截，票面一行修）**：票面声明块头＝`- 声明闭集（OA-D6-5 机检源，逐行）：`（L45），「声明闭集」与「：」之间插了括注——解析器 `check-ticket-reconcile.py` 的 `DECL_LINE_RE＝^...声明闭集[：:]`（L72）要求紧邻冒号，实测跑票 `python agent-skills/object-audit/scripts/check-ticket-reconcile.py --root . --ticket <本票>` 读数＝**「票 1（对账 0／SKIP 缺声明 1）」＝SKIP 不算绿**→ A7「21 件全认」在现票面下必然做不出来。修法＝块头改裸形态 `- 声明闭集：`（解析器两形态约定注释 L23–26 明文）。责任在起草席票面格式，非工具问题。

**黄 5**
- **Y1**：T6.1.7 PRODUCT L8 只说「替换为 README L3 同文」未给逐字定稿（L8 现行句式与 README L3 不同构、含 `**一句话**：`前缀），与票自设「T 节＝唯一施工依据、逐字照录」纪律冲突——工程师有两条推导路径，恐生第二口径。补逐字目标行即消。
- **Y2**：README L66–68 头像节未入改动面：mv 后五旧文件名成死引用、check-pointer-closure 不抓（A6 漏网路径实测）、L68「无头像素材/.gitkeep」陈述与盘面六 png 实态早已不符。建议随 T7 追加一目随动刷新该节（或明示豁免并登记）。
- **Y3**：A3 括注「架构席 4 处…实测 4 处为满」与命中拓扑不符：每新花名＝注册卡 1＋包装卡 2（name/displayName 两键同值）＋席位卡 frontmatter 1＋标题 1＝5，加 T5/T6/T7 各面命中远超 4。≥1 断言可跑不毁判据，但「为满」表述会误导回执对账，应改口径（如「≥5＋T5/T6/T7 点名面」）。
- **Y4**：票面 F11 自检「预期零命中」与实测冲突：F11 终式行自身（票 L352）含「轮次戳」，本席实跑 `grep -oE "见?第\s*\d+\s*轮|轮次戳|〔[^〕]*·轮〕|轮次号[：:]" <票>` ＝ 1 命中（L352 自指）。H6 会强制登记非零，票面应在预期段自登记该自指命中，免得回执环节读数推翻票面断言。
- **Y5**：displayDescription 新块（zh≈190 字＋en 更长）无宿主字段限长实测安排（候裁⑦只测 quickPrompts 槽数）；提案 §3.3 的「超限截尾」条款未随迁入票——②预览段存在展示截断风险，建议预览段一并实测登记。

**绿 8**
- G1：六 JSON 块值形态全部解析通过（①读数在案），两卡 members 顺序/两键结构各随其卡现行实态。
- G2：T1/T2/T3 全部行号锚与现盘块界逐一核对无漂。
- G3：A1∪A2 现盘全量命中逐行点名，白名单外命中 100% 被 T1–T7 覆盖、白名单内旧名不被顺手清（README L61 实测即豁免样例）——无必然拦截、无漏网；非 md/json 型命中＝0。
- G4：A4/A5/A6/A8 实体与读数全验（run-gates.sh／check-pointer-closure.py 在盘、bundle.lock L5 前值 0.1.22、三哈希与 README v0.1.19 行逐字同）。
- G5：映射总表↔裁定原文↔候裁八条三方逐字一致，含「高远见」笔误注记忠实性。
- G6：「五卡正文无旧名」断言复测成立（五卡命中＝仅 frontmatter＋标题行）。
- G7：sop 副本/SWB 交接件/其余技法卷零命中断言复测成立（禁碰面自洽）。
- G8：T4 五卡前值逐项现盘核对成立（lead L13 标题、其余 L16 标题；architect profession.en 现行 "Architect" 票从盘正确）。

---

## 会师建议（供主理人撤/续 HOLD 裁量）

R1 一行修（声明块头）＋Y1 补逐字句＝建议清账后再撤 HOLD 交工程师；Y2/Y3/Y4 可回执期处理；Y5 并入②预览段实测项。本席无条款语义异议：文案定稿面（displayDescription/defaultInitPrompt/quickPrompts/tags/README 三节）与本席前轮意见口径相容（「人类终裁」已入、「快速通道」措辞已修、三态覆盖矩阵已入）——无保留项。
