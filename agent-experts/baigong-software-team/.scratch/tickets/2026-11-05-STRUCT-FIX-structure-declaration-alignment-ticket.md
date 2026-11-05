# STRUCT-FIX STRUCTURE 声明面↔实态对位修正批施工票（架构席起草·落改按 S 节分席）

- 开端读数：devkits HEAD 以本票 commit 实测为准；开票侧实测 `git rev-parse --short HEAD`＝`f199c30`（main），`git status --porcelain` 本席名下净（他席在途 untracked 件不入本票）。
- 背景（决策依据·自包含）：皮总（2026-11-05 16:55）拍②＝STRUCTURE.md 一次性存量人工清查，架构席清查报告已落盘（`.collab/research/2026-11-05-STRUCTURE存量清查-架构席-v1.md`＝f199c30）：七份实物逐份双验，漂移总账＝必修 4（fuxi 双向脱节 2＋EAC `sources/` 未宣＋object-build `scripts/` 未宣）／随正 5（COPY.state×3＋bundle 顶层四件）／观察 3（不入本票，见禁动面）。本票依据＝清查报告必修 4＋随正 5；随正处置采报告最实质三条之 3 的设计判断＝「生成物/装配元数据不列举」惯例句成文豁免，不逐件枚举；惯例句同时作将来 C-3 结构一致性机检的豁免依据（豁免面机读化）。观察 3 不入票：`docs/adr/` 候 ADR-L0 批后自动消解、仓根无 STRUCTURE 属既成设计（报告 §〇 定性）、softwares/ 壳无锚属登记级。
- HOLD：**排程依赖＝本票交付排 ADR-L0 批之后**。理由：两票写面交叠件＝bundle `README.md`（版本账尾行追加位置）＋三同源（ADR-L0 S5 定 0.1.25→0.1.26，本票随动 0.1.26→0.1.27 依 ADR-L0 落地后现值）；ADR-L0 触碰 object-audit `scripts/`（新挂 check-adr.py）而本票触碰 object-audit STRUCTURE——ADR-L0 票面 S 节已自注「object-audit scripts/ 声明面已覆盖新脚本落位，零随动需求」，故本票对 object-audit STRUCTURE 仅落惯例句零条目随动，不冲突。若 ADR-L0 未先行落地即执行本票＝README 版本账尾行与三同源现值双双失步，A 判据不可达。执行序＝ADR-L0（含 S4 终写）全部落笔后，本票按施工时实测现值随动（票面版本号只声明相对值，绝对值按现值登记）。
- 改动面闭集＝11 件：（闭集外零触碰；写入席位按 S 节标注，混席件＝无；八声明面件＋三版本随动件）
- 声明闭集：
  - agent-skills/fuxi-skill/docs/STRUCTURE.md
  - agent-skills/external-advisor-collab/docs/STRUCTURE.md
  - agent-skills/object-build/docs/STRUCTURE.md
  - agent-skills/multi-collab/docs/STRUCTURE.md
  - agent-skills/object-audit/docs/STRUCTURE.md
  - agent-skills/bundle-assembly-registration/docs/STRUCTURE.md
  - agent-experts/baigong-software-team/docs/STRUCTURE.md
  - agent-experts/baigong-software-team/README.md
  - agent-experts/baigong-software-team/plugin.json
  - agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json
  - agent-experts/baigong-software-team/bundle.lock

开票侧实体核验：闭集 8 件全部 `git ls-files` 实测在位（f199c30 态，读数 `.scratch/structfix/readings-*.txt`，票批后清）。前态钉值实测（f199c30 态）：条目行／yaml 行计数＝fuxi 3/3、EAC 2/2、object-build 2/2、multi-collab 2/2、object-audit 4/4、bundle-assembly-registration 2/2、bundle 7/6；「非枚举面」六份 STRUCTURE 现时命中＝0（`git grep -c "非枚举面" -- "*STRUCTURE.md"` exit 1＝零命中）。bundle README 版本账尾行＝v0.1.25（L67，f199c30 态）；三同源现值实测＝plugin.json L3／.codebuddy-plugin/plugin.json L3／bundle.lock L5 均 `0.1.25`——**注意：ADR-L0 交付后三值变 `0.1.26`，本票执行时按彼时现值 +1 随动并附前后读数（H6 实测口径）**。

版本随动面自查（派工要点 3）：本票触碰面＝七份 STRUCTURE（均非 SKILL 版本面）＋bundle README（版本账载体）。不触任何包 SKILL.md——fuxi 无 SKILL.md（`ls`＋`git log --all --follow` 双验零落笔＝从未存在，非删除）；EAC `sources/` 补声明不触 90-changelog（非条款语义改动，沿革行随 ref 换代才有，本票不换代）；multi-collab/object-audit STRUCTURE 仅惯例句零条目动，不触其 SKILL/changelog。唯 bundle 顶层版本账触 README＝随动登记走三同源既有体例（纪律①每变必 bump·三同源，真源＝bundle README 版本账行体例＋bundle-assembly-registration `20-register.md` L18）。三同源 bump 属交叠面随 ADR-L0 后置（HOLD 段）。

回执落点＝`.collab/receipts/2026-11-05-STRUCT-FIX-工程师回执-v1.md`（文件名级回执指针行）。

## §口径（判据定义·票内自包含）

1. **惯例句（逐字，七份 STRUCTURE 各落一处）**：
   `非枚举面＝生成物与装配元数据（COPY.state、bundle.lock、plugin.json、settings.json、仓侧 README.md）不逐件枚举，声明面对其零覆盖属既成惯例（STRUCT-FIX 成文·C-3 机检据此豁免）。`
   落位＝「交付面＝…不属于交付路径。」行之后、yaml 围栏块之前，空行分隔；七份逐字同一（同文机检＝A4）。惯例句含裸词 `COPY.state` 等＝无日期裸写、不在 OA-T1 判据射程（扫描面内已核：现盘六份 STRUCTURE 零日期）。
2. **条目行↔yaml 行对偶不变式**：每份 STRUCTURE 的 `delivery_paths` yaml 行必须逐条命中声明节 `- \`…\`` 条目行（除 bundle `docs/adr/` 条目——既有条目注「不属于交付路径」yaml 不含＝既成形态零动）；惯例句行不入 yaml（非枚举面无交付射程）。
3. **fuxi 重写口径**：声明面按实态重写＝`README.md`＋`adapters/`＋`contracts/`＋`gates/`＋`products/`＋`rejected/`＋`specs/` 七条；yaml 随动同七条；「交付面＝」句随重写。旧三条（SKILL.md/references/）全删——git 全史零落笔（`git log --all --follow -- agent-skills/fuxi-skill/SKILL.md` 空返回）＝声明系 B1 壳批模板先行态（建立笔 c7f87e7），非规划领先：包已解冻续推（FUXI 解冻拍板在 decisions），冻结态 SKILL.md 不补建、待 FUXI 技能本体批再立（登记候裁 Q-1）。
4. **OA-T1 日期纪律**（TMP-DISC 教训前置）：定稿落交付面文本日期一律①全角括注②反引号段③`YYYY-MM-DD` 模板三载体之一；惯例句与本票全部定稿文本零裸日期。
5. 行号锚＝f199c30 读数；施工以 pattern 命中为准，实测与票面预期冲突按实测登记上报（H6）。

## S1 fuxi-skill STRUCTURE 重写（工程师·逐字）

`agent-skills/fuxi-skill/docs/STRUCTURE.md` 整件替换为（定稿全文·外栏四反引号因内嵌 yaml 围栏）：

````
# 项目分层目录方案 · fuxi-skill

本项目＝伏羲（fuxi-skill）perspective-pack-builder 技能。分层如下：

- `README.md` — 包级详细件（性质自注＝交付件本体·相近工具对照表置顶）
- `adapters/` — 对象分类适配件（person/method/classifier 三型）
- `contracts/` — 契约真源（artifact-contract／evidence-grading／failure-modes）
- `gates/` — 机检闸面（assert-tool／harness／validator 族）
- `products/` — 视角包成品（按契约炼成的 perspective pack 产物）
- `rejected/` — 淘汰候选留档面
- `specs/` — 对象规范件（perspective-spec／technique-spec）

交付面＝上述七目录/件；`docs/` 为项目文档面，不属于交付路径。

非枚举面＝生成物与装配元数据（COPY.state、bundle.lock、plugin.json、settings.json、仓侧 README.md）不逐件枚举，声明面对其零覆盖属既成惯例（STRUCT-FIX 成文·C-3 机检据此豁免）。

```yaml
schema_version: 1
project_root: "."
delivery_paths:
  - README.md
  - adapters/
  - contracts/
  - gates/
  - products/
  - rejected/
  - specs/
```
````

注：fuxi 顶层唯一例外自注＝本包 `README.md` 入交付面（性质自注「交付件本体」置顶于件内），惯例句「仓侧 README.md」豁免指非交付定性者，两件不冲突（票内裁定）。验收＝A1。

## S2 EAC sources/ 补声明（工程师·逐字）

`agent-skills/external-advisor-collab/docs/STRUCTURE.md`：
1. 声明节 `- \`references/\` — 技能参考件（规程、模板、裁决引文等）` 行后追加一行：
   `- \`sources/\` — 自包含料源面（dev-discipline §二.5 唯一允许进交付物的料源·spec-anchors 实体居此）`
2. 「交付面＝」句改为：`交付面＝\`SKILL.md\`＋\`references/\`＋\`sources/\`；\`docs/\` 为项目文档面，不属于交付路径。`
3. 「交付面＝」行后落惯例句（§口径 1 逐字，空行分隔）。
4. yaml `delivery_paths` 末项后追加：`  - sources/`
验收＝A2。理据＝`sources/spec-anchors.md` git 面在位（readings-A）；不声明＝装配/授权射程少一条。

## S3 object-build scripts/ 补声明（工程师·逐字）

`agent-skills/object-build/docs/STRUCTURE.md`：
1. 声明节 `- \`references/\` — 技能参考件（装配工序、规范件模板等）` 行后追加一行：
   `- \`scripts/\` — 装配工序执行件（publish.py 装配器本体）`
2. 「交付面＝」句改为：`交付面＝\`SKILL.md\`＋\`references/\`＋\`scripts/\`；\`docs/\` 为项目文档面，不属于交付路径。`
3. 「交付面＝」行后落惯例句（§口径 1 逐字，空行分隔）。
4. yaml `delivery_paths` 末项后追加：`  - scripts/`
验收＝A2。理据＝`scripts/publish.py` git 面在位＝run-gates 外挂与 CLN-PURE assembly_exclude 执行主体；object-audit 已宣 `scripts/` 同族先例。

## S4 随正四处＝惯例句落位（工程师·逐字）

以下四份各两处动（「交付面＝」行后落惯例句＋空行），零条目动、零 yaml 动：
- `agent-skills/multi-collab/docs/STRUCTURE.md`（COPY.state 豁免）
- `agent-skills/object-audit/docs/STRUCTURE.md`（COPY.state 豁免；scripts/tests 已宣零动＝ADR-L0 check-adr 落位已被覆盖，HOLD 段注）
- `agent-skills/bundle-assembly-registration/docs/STRUCTURE.md`（零漂移样板随批落惯例句＝样板面亦入豁免统一措辞；其余零动）
- `agent-experts/baigong-software-team/docs/STRUCTURE.md`（顶层 README/plugin.json/bundle.lock/settings.json 四件豁免；`docs/adr/` 条目 L11 零动——ADR-L0 落地后自动咬合，本票不判不补）
验收＝A3。

## S5 bundle 版本账随动（工程师·随 ADR-L0 后置）

`agent-experts/baigong-software-team/README.md`：版本账块追加一行（插彼时尾行后），体例：
`- **版本账 v0.1.27**（2026-11-05·STRUCT-FIX 声明面对位修正批）：七份 STRUCTURE 声明面↔实态对位——fuxi 声明按实态重写（七条目，旧 SKILL/references 虚宣删·git 全史零落笔实证）＋EAC sources/ 补声明＋object-build scripts/ 补声明＋「非枚举面」统一惯例句七份落位（COPY.state×3 与 bundle 顶层元数据豁免成文·C-3 机检豁免依据）；依据＝架构席清查 v1（f199c30）；纯声明面批零代码零 SKILL 动。三同源 0.1.26→0.1.27（纪律①每变必 bump·三同源）。`
（版本号绝对值按执行现值＝ADR-L0 落地后 +1；若 ADR-L0 未落地即执行本票＝HOLD 违反，不得先行。）
随动件＝三同源三件（plugin.json L3／.codebuddy-plugin/plugin.json L3／bundle.lock L5，已在声明闭集内＝版本随动件体例同 TMP-DISC/ADR-L0），值＝彼时现值 +1。

## 验收判据（逐票机械·A 判据前后读数钉值）

- **A1 fuxi 重写咬合**：后态 `grep -c '^- \`' agent-skills/fuxi-skill/docs/STRUCTURE.md`＝7、`grep -c '^  - ' …`＝7（前态 3/3）；声明条目逐条 `test -e agent-skills/fuxi-skill/<条目>` 全真；实态↔声明双向＝`git ls-files agent-skills/fuxi-skill/ | cut -d/ -f3 | sort -u | grep -v '^\.'` 输出八行（前态实测：README.md adapters contracts docs gates products rejected specs＝readings-N），其中七行全在声明、剩余一行＝`docs`（项目文档面＝声明句既载排除项）。
- **A2 两补声明咬合**：EAC 后态条目/yaml＝3/3（前态 2/2）、`test -d agent-skills/external-advisor-collab/sources` 真；object-build 后态条目/yaml＝3/3（前态 2/2）、`test -d agent-skills/object-build/scripts` 真。
- **A3 惯例句七份落位**：`git grep -l "非枚举面" -- "*STRUCTURE.md"`＝7 文件命中（前态 exit 1 零命中）；每份内恰 1（`git grep -c "非枚举面" -- "*STRUCTURE.md"` 七行均＝1）。
- **A4 惯例句逐字同一**：惯例句定稿串 `grep -c` 逐字命中＝7（七份各 1）；同串与票面 §口径 1 逐字节对等（回执附 diff 读数）。
- **A5 对偶不变式**（§口径 2）：七份逐份 yaml 行⊆条目行集合断言全真（回执附逐份对读表）；bundle `docs/adr/` 条目列既成例外。
- **A6 版本随动**：三同源读值＝ADR-L0 落地后现值 +1（前后各附·F7）；README 版本账新行＝1 且版本号与三同源一致；README v0.1.26 行（ADR-L0）在位先于本票行（链序读数）。
- **A7 OA-T1 预跑**：七份 STRUCTURE＋README 新行过 check-entity 真判据链＝裸日期 0（惯例句零日期；版本账行日期在括注内＝既有豁免口径）。
- **A8 零漂移样板零破坏**：bundle-assembly-registration 后态条目/yaml 仍 2/2（惯例句不入 yaml），仅惯例句 +1。

## 禁动面

- 六包 SKILL.md／各 90-changelog.md／seat-permissions config／bundle.lock `assembly_exclude` 与 components 钉 ref（本票零换代零换钉）；
- 代码域全部（`scripts/*.py` 本体、run-gates、check-* 全体）；
- `agent-skills/fuxi-skill/` 实体面（本票只改其 docs/STRUCTURE.md 声明面，零建零删实体）；
- softwares/、仓根（观察 3 不入票）；`docs/adr/` 目录本体（ADR-L0 点火件）；
- ADR-L0 票面/TMP-DISC 票面及其在途件；`.collab/ledger/`（他席在途）。

## 候裁单列

- Q-1 fuxi `SKILL.md` 补建：本票删虚宣不补建（解冻续推中，入口件归 FUXI 技能本体批）——若决策者裁「应即刻补建」＝另批，本票声明面届时再随动。
- Q-2 惯例句是否升为 STRUCTURE 样板模板要件（新包出生即带）：本票只落存量七份，模板面（object-build `references/50-directory.md` 等）未触——升模板与否候裁。
- Q-3 COPY.state 身份表述复核：清查报告称三包 COPY.state，实测 git 面三包在位（multi-collab/object-audit/object-build），EAC/fuxi 无——与报告一致；惯例句措辞以件名列举不依赖计数，若将来 COPY.state 增减零随动需求（刻意设计）。

## 自检（开票侧）

- 临时读数区＝`.scratch/structfix/`（readings-A..M 十三件）：票批后随票清理义务＝收口登记时 `rm -r .scratch/structfix` 附读数（§八.2）；
- 声明闭集自对账：闭集列出 8 路径行＋S5 补正三同源三件＝11 件，S 节落点覆盖 11/11（fuxi=S1、EAC=S2、object-build=S3、四份随正=S4 中三份＋bundle=S4 第四份、README=S5、三同源=S5），逐一对应无孤儿；
- 惯例句含全角括号内逗号枚举＋裸词零日期，过 §口径 4；票内日期均括注内；
- OA-T1 预跑读数（本票成文前已跑·check-entity 真判据链 mask_non_narrative＋in_fullwidth_paren·四样本）：惯例句行＝裸 0／版本账行（括注日期）＝裸 0／开票侧读数行（反引号段）＝裸 0／裸日期对照样本＝命中 1（证判据链有效）；
- 与 ADR-L0 写面交叠核表：README（交叠→HOLD 排后）／三同源（交叠→HOLD 排后）／object-audit STRUCTURE（不交叠，ADR-L0 不触）／multi-collab 60-gates 等（本票不触）＝交叠二面全入 HOLD 排程依赖，票开端已注明。

## 修订记录

（append-only，修票笔此后追加）

## 修订笔 v1（双席审票清账后·作者席亲笔·append-only 修订段）

开工 HEAD 实测＝`0312d35`（修订笔落链前链顶；链上双席审票件＝产品席 `28f0021`（红0黄3绿10）＋QA席 `0312d35`（红0黄2绿5·路由＝双黄 append-only 修票笔后按 HOLD 放行））。本段逐项**覆盖**原笔对应文本；原笔体例零改写。作者席对修单全部断言已独立复现（复现代数＝`.scratch/structfix/rev-readings-1/2.txt`，读数随收口清理）。

### R-1（QA 黄-1·必落）A1/A2/A8 条目计数式换代＝方括号形态

原笔 A1 中 ``grep -c '^- \`'`` 式：单引号内 `\`` ＝字面反斜杠＋反引号，逐字实跑 fuxi 现盘返回 0（exit 1）＝前态钉值 3 按原式不可达（作者复现：rev-readings-1 V1＝0/exit 1）。**覆盖为统一方括号形态**：

- 条目行计数式＝`grep -c '^- [`]' <文件>`；yaml 行计数式＝`grep -c '^  - ' <文件>`（原式无转义问题零动）。
- 换代后现盘复跑（rev-readings-1 V2）＝fuxi 3／EAC 2／object-build 2／multi-collab 2／object-audit 4／bundle-assembly-registration 2／bundle 7——**票面全部前态钉值可达零改动**（fuxi 3/3、EAC 2/2、object-build 2/2、multi-collab 2/2、object-audit 4/4、样板 2/2、bundle 7/6）。
- A2/A8 原笔以「条目/yaml＝N/N」计数口径表述，无内嵌命令式；本目覆盖＝A1/A2/A8 三判据的执行命令一律取方括号形态（回执须附换代式读数）。
- 原笔 A1 行字面依 append-only 体例零动（同 ADR-L0 修订笔先例＝覆盖段为唯一施工依据）；数值面零改动，纯命令式修正。

### R-2（QA 黄-2·必落）A4 逐字基准钉死＝去包裹内串＋sha 钉值

原笔 A4「与 §口径 1 逐字节对等」存在包裹态歧义（§口径 1 定稿句带反引号包裹 vs S1 落位句无包裹）。**覆盖 A4 为**：

> **A4 惯例句逐字同一**：基准态＝去反引号包裹内串；基准钉值＝UTF-8 字节数 **228**＋sha256 前 12 位 **`15b98b5a1653`**。判据＝七份落位各取该整行（去行首尾空白）对基准内串逐字节比对全真（`grep -c` 定稿串命中＝7 辅证）；回执附逐份 sha 对读表。

作者复现（rev-readings-1 V3＋python 对拍）：§口径 1 行去包裹内串 vs 惯例句设计内串＝逐字节对等 True，字节 228、sha12 `15b98b5a1653`。**H6 登记**：修单转述作「229 字节」，作者实测＝228 字节（sha 前 12 两位一致＝`15b98b5a1653`）；按实测口径取 228，若 QA 席 229 系含行尾字符另报，判据以行内串去首尾空白态为准不受影响。

### R-3（PM Y-1·随正）HOLD 段引用出处更正

原笔 HOLD 段将「object-audit scripts/ 声明面已覆盖新脚本落位，零随动需求」标源＝ADR-L0 票面 S 节。复现（rev-readings-2 V4）：ADR-L0 票面 grep「声明面已覆盖」＝0 命中（exit 1）＝错置坐实；**实源＝清查报告 §一.6 附注（`2026-11-05-STRUCTURE存量清查-架构席-v1.md` L69 逐字吻合，V5）**。覆盖＝HOLD 段该句出处改标「清查报告 §一.6 附注」。实质结论零动（object-audit STRUCTURE 现盘已宣 `scripts/`＝条目行 L7＋交付面句 L10＋yaml L18 三处实测，V6）。

### R-4（PM Y-2·口径级）§口径 1 补点号目录豁免句

原笔 §口径 1 惯例句按件名列举五件，未覆盖点号名顶层面（`.codebuddy-plugin/`——内件 plugin.json git 面在位，V7；`.collab/`／`.scratch/`——.gitignore 既载治理/临时域）。C-3 将来按包顶层对账时点号目录成常驻误报。A1 判据虽已用 `grep -v '^\.'` 排除，但只在命令层未成文。**覆盖＝§口径 1 增补第二句（逐字，随惯例句同落七份）**：

> 点号名顶层面（`.collab/`、`.scratch/`、`.codebuddy-plugin/` 等）不入声明射程，机检对账对其零覆盖属既成惯例。

落位＝惯例句行之后同段（两句间无空行）；A3/A4 判据射程同步＝`git grep -c "非枚举面"` 仍＝7 文件各 1（增补句不含锚词「非枚举面」不扰动钉值）；A4 基准内串钉值只辖惯例句首句，增补句另立同文对读（回执附七份增补句逐字命中＝7）。OA-T1 面：增补句零日期零新增风险。

### R-5（PM Y-3·登记）「随正 5 条」计数口径注记

原笔背景行「随正 5（COPY.state×3＋bundle 顶层四件）」枚举实为 4 件次；清查报告 §二「随正 5 条」第五项系「（COPY.state×3＋bundle 顶层四件一句＋软性）」中未定义之「软性」。覆盖口径＝**本票覆盖面无缺**（报告表级随正行实测 4 行全入 S4 四落点）；工程师回执按枚举 4 走；「随正 5」计数沿报告原账不改引，票内以本目注记为闭合。

### 不修登记（两席共判）

候裁 Q-1/Q-2/Q-3 边界清楚零动；HOLD 排程两席互洽确认零动（三同源 0.1.25 现值如钉、ADR-L0→0.1.26、本票相对 +1 无环）。

### 修订笔后闭合读数义务（工程师段同步·CR 系列）

- CR-1：修订笔后票面原转义式零残留＝`grep -c '\\`' <本票面>` 于计数式语境零命中（换代全量核对）；条目计数式换代形态命中 ≥4（A1 两处＋本段两处）；
- CR-2：修订笔先于工程师开工（链序＝审票双席→修订笔→HOLD 押 ADR-L0 放行→工程师开工）；修票笔只动票面不受 HOLD 辖，HOLD 排程依赖本身不变。
