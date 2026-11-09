# CARD-RENEW 产品席独立审票 v1（A 席）

> 【来源】产品席·独立审票轮·2026-11-05。只读审票，禁施工，件居 `.collab/qa/`。
> 开工读数：`git rev-parse --short HEAD` 实测 `da25666`（CARD-RENEW 票面 HOLD 挂位笔；被核票面 commit＝起笔 `94ed2ec`）。
> 被核件＝`agent-experts/baigong-software-team/.scratch/tickets/2026-11-05-CARD-RENEW-卡片换代与席位命名换代施工票.md`（下称「票面」，356 行完整直读；票面 commit＝起笔 `94ed2ec`＋HOLD 挂位笔 `da25666`）。
> 裁定真源＝`.collab/decisions/2026-11-05-皮总裁定-席位职业标签与花名换代.md`（4d52e88，下称「裁定」）＋`.collab/decisions/2026-11-05-主理人裁定-CARD-RENEW候裁八条.md`（bda4fec，下称「八裁」）。
> fresh eyes 纪律：QA 席（B 席）审票件零读取；本席对照用己席意见件（commit 88df907 终态）已计入输入。
> 口径声明：本件 occurrence 计数均为 `grep -rn` 行:列实测；判定逐项 PASS/FAIL＋文件行号。
> 总裁决：**红 0 ／ 黄 2 ／ 绿 12**。黄＝随动位一漏＋文案口味项，皆不阻塞施工；无红项＝本席无停手上报项。

---

## 一、审① T 节定稿文案对皮总裁定的忠实性（映射总表逐字对照，含 en 面）

### 1.1 映射总表（票面 L9–15）逐格对照裁定

| 格 | 票面值 | 裁定真源 | 判定 |
|---|---|---|---|
| 花名 zh 五格 | 齐活林→包好用／许清楚→姜通透／高见远→顾长远／寇豆码→柯会码／严过关→沈得严 | 裁定原文 L15–19 逐字等值 | PASS 🟢 |
| 「高远见」笔误处置 | 票面 L17 注记①搬运：映射对象＝架构席花名→顾长远 | 裁定 L23 注记 1 同口径 | PASS 🟢 |
| 职业 zh 五格 | 交付总监→项目负责人／产品经理不变／架构师→架构工程师／工程师→开发工程师／QA工程师→质量审计师 | 裁定原文 L9–13；「QA ->质量审计师」→票面按盘上现值「QA工程师」为映射左值，处置正确（盘上实态 `agents/software-team-qa.md` L9 `zh: "QA工程师"`） | PASS 🟢 |
| 花名 en 五格 | Bao/Jiang/Gu/Ke/Shen | 裁定 L25 注记 2 默认随动值逐字等值 | PASS 🟢 |
| 职业 en 五格 | Project Lead／Product Manager 不变／Architect Engineer／Development Engineer／QA Auditor | 裁定 L26 逐字等值 | PASS 🟢 |
| 头像新引用五格 | `avatars/software-team-*.png` 与席位 id 同族 | 裁定 L27 注记 3（旧血统名→id 同族形态、图像不重制） | PASS 🟢 |
| 席位 id／席位卡文件名不动 | 票面禁动面 L332 钉死 | 裁定 L28 注记 4 | PASS 🟢 |
| 历史链不改写 | 票面白名单＋禁动面 L334（旧名不顺手清／新名不回补） | 裁定 L29 注记 5 | PASS 🟢 |

### 1.2 T 节落地块对映射总表的忠实性（抽查到行）

- T1.7 注册卡 members 定稿块（票面 L137–173）：五席 displayName/profession/avatar 与映射总表逐格等值，id/role 不动——PASS 🟢。
- T2.6 包装卡 members 定稿块（票面 L187–229）：`name`/`displayName` 两键同值换代＝包装卡现行结构实态（现卡 `plugin.json` L58–61 实测双键），顺序 lead/product/architect/qa/engineer 照现状保持（现卡实测同序）——PASS。
- T4 五席位卡（票面 L242–246）：逐卡四行 frontmatter＋标题行花名位，与五卡实态行位全对上（实测：lead `agents/software-team-lead.md` L6 齐活林/L13 `# 主理人 - 齐活林`；architect L6/L16；engineer L6 `zh: "寇豆码"`/L8 `en: "Software Engineer"`/L16；qa L6/L8 `en: "QA Engineer"`/L16；product L6/L16）；T4.2 product profession 两行不动＝映射「不变」——PASS。
- T1.4 defaultInitPrompt zh 开场「我是项目负责人包好用」＋en「I am Bao, Project Lead」＝裁定新值入文案——PASS。
- T6/T7 docs/README 各处新值（项目负责人/姜通透/顾长远/柯会码/沈得严）与映射等值——PASS。

**审①小结：全 PASS（绿 1 总账＋上表 8 细分）。**

## 二、审② 卡片文案产品面质量（人话／黑话／退役档名／自造标签）

- **退役档名检查**：T 节全部定稿文案 grep「快速模式／BugFix」——展示文案零入文（T1.4 判档四名目＝标准 SOP／维护票／部分工作流／增量开发，与现行盘上一致：`skills/software-orchestration/SKILL.md` L16–21）；唯 T7.4 版本账新行含「旧『快速模式』档位…随此退役」＝登记行史实陈述（append-only 版本账体例），非退役名上展示面——PASS 🟢。
- **自造标签检查**：quickPrompt 2「三态覆盖矩阵」＝盘上词条原文（`skills/sop/references/architecture-v2.9-copy.md` L142「产出一律三态覆盖矩阵」），且本席意见轮所反对的自拟括注「（覆盖／部分／缺口）」未入定稿——意见已被吸收，PASS 🟢。
- **六节点口径**：T1.3 zh「需求→设计→拆票→执行→发布→灰度」＝architecture copy L60 骨架，无五段旧链残留（旧链 README L13 由 T7.2 换掉）——PASS。
- **「一票活跃」入 defaultInitPrompt**：登记词条（architecture copy L60）＋主理人意见轮已裁保留（4fa464b 要点在案）——PASS。
- **黑话残留（黄-2）**：T1.5 tags zh 槽二「账本与写侧门禁」/en「Ledger & Write Gates」——「写侧门禁」对宿主用户（是否选购本团队的决策者）仍是内部执法面行话，不透明；本席意见轮建议收益面措辞（锚＝本人意见件 88df907 §二 2.2 槽二条），票面未采且候裁八条未裁此点。文案口味项＝不阻塞施工，登记呈报供主理人②预览段随卡片实感一并定夺——**FAIL→黄** 🟡（判据＝皮总口径「面向宿主用户人话」，此项半达：zh 可猜、en 生硬）。

**审②小结：绿 4 ＋黄 1（黄-2）。**

## 三、审③ 改动面闭集 vs 独立实扫（多漏＝红）

本席独立实扫（命令口径同票面 A1/A2，白名单外）：

### 3.1 旧五花名 occurrence 全命中对照（`grep -roEn "齐活林|许清楚|高见远|寇豆码|严过关" --include="*.md" --include="*.json"`，排除 `.collab/`、`.scratch/`）

实测命中 64 处，分布逐面对账票面点名面：

| 命中面（实测行号） | 票面点名位 | 判定 |
|---|---|---|
| `.codebuddy-plugin/plugin.json` L49/61/75/82/89/96/103＋L44/50/60/76（zh 文案位） | T1.3/T1.4/T1.6/T1.7 整块替换全覆盖 | PASS |
| `plugin.json` L58/59/66/67/74/75/82/83/90/91 | T2.6 整块替换全覆盖 | PASS |
| 五席位卡各 L6＋L16（共 10 处） | T4.1–4.5 | PASS |
| `README.md` L11（五名同线） | T7.2 | PASS；L61（v1.2.3 史实行五名）＝A1 白名单豁免样例，票面 L321 点名豁免 ✓ |
| `docs/PRODUCT.md` L10/L48–52 | T6.1 | PASS |
| `docs/ARCHITECTURE.md` L15–19/L74–78 | T6.2 | PASS |
| `skills/software-orchestration/references/` standard-sop L15×2/L20×2/L31×2/L38×2/L41、quick-mode L18、bugfix-path L17/L20 | T5.1–5.3 逐行点名，行号逐一对上实扫 | PASS |

→ 旧花名面：**零漏**（闭集外白名单外命中＝0）。

### 3.2 A2 断言串 occurrence 对照（同口径扫「交付总监|Delivery Director|QA工程师|QA 工程师|QA Engineer|Software Architect|Software Engineer」）

实测命中 39 处：注册卡 L44/49/50/60/61/76/90/97/104（含 en）→T1 块替换 ✓；包装卡 L60/84/92→T2 ✓；席位卡 engineer L8/lead L8,L9/qa L8,L9→T4 ✓；README L3/L11→T7 ✓；PRODUCT L8/L10/L48/L52→T6.1 ✓（T6.1 含 L8 换 README 同文＝八裁④）；ARCHITECTURE L15/L19/L78→T6.2 ✓；standard-sop L8/L38×2、quick-mode L12、bugfix-path L12/L20、collab-rules L10、partial-workflows L13→T5 逐行点名 ✓。全部命中入块。

断言串外命中复实（变体与相邻面，本席补扫）：
- `config/seat-permissions-hooks-map.json` L35–37 `"software-architect"/"software-qa-engineer"/"software-engineer"`＝席位 id legacy 别名映射（寻址键），裁定注记 4 钉死不动＋A2 精确串不入——**正确不动**，PASS 🟢。
- 全包 `*.py/*.lock` 等非 md/json 旧花名命中＝0（实测）——A1 的 --include 面即全覆盖，PASS。
- 包外 `.workbuddy/memory/*.md` 旧名命中 4 文件＝宿主运行域记忆文件，非仓内真源、无流程效力（memory-neutralize 纪律口径）——票面 A1 射程限包内，**射程正确**，PASS 🟢（登记说明，非缺陷）。

→ 断言串面：**零漏**。

### 3.3 随动位一漏（黄-1）

`README.md` L68「替换规格」行现文点名六个旧头像文件名（`software-company-team-lead.png / software-product-manager.png / …`），且该行「盘上无头像素材，`avatars/` 仅 `.gitkeep` 占位」本身已失真（实测 `avatars/` 六 PNG 在盘）。票面 T8 改名五件后，该行枚举的旧文件名将与盘上实态错位——README 属展示面真源，T7 未点名此线、A1/A2 断言口径不覆盖头像文件名（归零射程＝花名/职业标签），故此漏**不触任何验收判据**，但属改名动作的相邻随动位漏网，与本次「消除旧血统残留」案旨相悖——建议主理人处置：追加 T7.5 一行随动（旧文件名枚举→新五名）或明列白名单豁免注记。**黄** 🟡（不阻塞：不违任何裁定、不触归零断言）。

**审③小结：闭集 21 件对实扫＝点名面全覆盖（绿）；随动位一漏（黄-1）。**

## 四、审④ 双卡口径分裂是否真消除

- T2.2＝T1.2 同 description 串（八裁③两卡统一）；T2.3＝T1.3 同 displayDescription 块；T2.4＝T1.5 同 tags 块；T2.5＝T1.6 同 quickPrompts 块；T2.6 members 两键同值换代——五面同值断言链在票面内闭合，PASS。
- 票面 T2 行号与包装卡实态对位实测：L4 description ✓、L39–42 displayDescription ✓、L45–49 tags ✓、L50–54 quickPrompts ✓、L55–96 members ✓（逐位 sed 实测）；包装卡无 `defaultInitPrompt` 字段（实测 grep 零命中）→票面未强补该字段＝结构零动口径正确，PASS。
- 残余差异面＝包装卡 members 多 `name` 键＋缺 defaultInitPrompt＝结构性差异非口径差异，卡片可读文案五面全同值——分裂消除成立，PASS 🟢。

## 五、审⑤ 验收判据与程序面（抽验）

- A1/A2 grep 口径与本席实扫口径等值、白名单逐路径封闭（史实行 L61 豁免样例与实测命中吻合）——PASS。
- A3 计数口径复核：architect 新名盘上 4 处（两卡 members 各 1＋席位卡 frontmatter＋标题行）＝本席实扫同构读数（五席位卡正文旧花名各仅 L6+L16 两处命中，佐证「正文无花名」断言）——PASS。
- A4 三同源：现值实测 0.1.22 三处（`bundle.lock` L5、`plugin.json` L3、`.codebuddy-plugin/plugin.json` L3）＝票面 F7 前值一致——PASS。
- A5/A6 脚本实体在盘：`agent-skills/object-audit/scripts/run-gates.sh`、`check-pointer-closure.py` 实测存在（ls）——PASS。
- A7 声明闭集 21 行（票面 L46–66）＝改动面闭集 21 件逐行等值（16 改＋5 改名新路径）——PASS。
- T5 豁免面白名单抽查：collab-rules L11–12（架构师/产品经理/工程师裸泛指）、partial-workflows L10–12/L14、ARCHITECTURE L28——行号与实态逐一对上，且八裁①已裁「裸泛指不换」——豁免有据，PASS。
- 候裁八条在票面均有对应落点（票面 L339–346 vs 八裁①–⑧逐条方向一致），票面 L3 已注「候裁八条已由主理人裁定在册 bda4fec」——程序闭合，PASS。

**审⑤小结：全 PASS（绿）。**

---

## 六、红黄绿分账（终态）

**红 0。**（无停手上报项；定稿文本无对裁定失真、闭集无触断言口径漏位、双卡分裂确消。）

**黄 2：**
1. **黄-1 随动位漏**：`README.md` L68 头像规格行枚举旧头像文件名六名（行本身「无头像素材」已失真）——T8 改名后错位残留；不触 A1/A2 射程故不违票面判据，建议追加 T7.5 随动一行或明列豁免注记。
2. **黄-2 文案口味**：tags zh 槽二「账本与写侧门禁」/en「Ledger & Write Gates」仍系执法面行话，宿主用户不透明（本席 88df907 意见建议收益面措辞未被吸收，候裁未裁此点）——呈主理人②预览段随卡片实感一并定夺，不阻塞。

**绿 12：**①映射总表对裁定（zh/en/头像/不动面，细分 8 全 PASS）；②笔误注记①搬运正确；③T1–T3 块替换与行号实态对位；④T4 五席位卡行位实态对位；⑤T5 技法卷点名行逐一对上＋豁免面白名单有据（八裁①）；⑥T6 docs 点名行对位（含八裁④ L8 同新文）；⑦T7 三节＋版本账 append-only 体例＋退役名不入展示文案；⑧T8 改名与引用成对（10 处引用＝两卡各五处，实测现值对位）；⑨A1/A2 实扫零漏＋断言串外命中（id 别名/包外 memory）处置正确；⑩A3–A7 验收口径与脚本实体在盘可机械验证；⑪候裁八条落点闭合；⑫双卡口径分裂真消除（五面同值断言链闭合）。

## 七、裁定建议

本席裁定：**票面可放行**（黄二项建议主理人在撤 HOLD 前顺手处置黄-1 一行级；黄-2 留②预览段人类闸实感裁）。产品职权面无异议项。
