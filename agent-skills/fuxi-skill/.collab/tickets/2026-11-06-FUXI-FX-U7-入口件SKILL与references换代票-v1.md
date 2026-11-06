# FUXI-FX-U7 · 入口件换代票（包根 SKILL.md 新建·按包 README 使用口径＋旧代 references 九卷七式闭集处置表落交付面＋STRUCTURE 声明面随动）

> 票号＝FX-U7｜起草＝架构席（arch-fuxi-u7）｜日期＝2026-11-06｜被派＝**工程师席**（FUXI 线）
> 起草时点 HEAD 实测＝`20e1141`（FX-U4 收口登记笔）；开工 ANCHOR＝开工当轮 HEAD 实测读数，回执开端必附；开工基线对账＝assert-tool 汇总 `PASS=25 FAIL=1 PENDING_STAGE=1 总数=27`·exit 1＋selftest 155/40/22/19＋run-gates `GATE PASS`（开工当轮实读数为准，与本票起草读数不符＝按开工态照登不归因本票）。status 照登 untracked 若干与本案无关禁带入；他案 TK-GWP 在途零触碰。
> 账权＝FUXI 项目（拍板㊠）：本票交付面＝FUXI 包内交付面＋docs 声明面；**宿主装载面（`C:\Users\peter\.workbuddy\skills\fuxi-skill\`）零触碰**（只读实读完毕，其换代部署归注册面另工序，非本票射程，§四）。
> 来历（自包含，禁指针依赖）：产品席 PM-U1 判定件（`.collab/research/2026-11-04-FUXI-PM-U1-下一段优先级产品判定-v1.md`）U1-3（黄级·消费入口分裂）在册＝「仓内包无技能入口，宿主装载的是旧代技能，两套 fuxi-skill 并存」——宿主已装载副本（v1.1.0）内容＝旧 V3 代工序（镜片/化名制/盲评五维卡/导入七式），与仓内重建的双轨工具链完全脱节；§二第7行判词在册＝「**菜单外(f2)＝技能入口件 SKILL.md＋references 换代：STRUCTURE.md 声明的交付面缺两件，宿主装载旧代同名技能＝消费入口分裂。不做，则入池产物『可装载』是空话。最小笔＝按包 README 使用口径重写 SKILL.md 入口＋迁移/重写 references（旧代九卷与新双轨工序的映射处置走七式闭集口径逐卷判定，登记处置表）**，应做·入池段同批或紧随」；§三第三段排期在册＝「第三段＝首单入池实跑＋SKILL.md/references 换代」。**本票＝第三段第三票＝入口件换代（与 U5/U6 并行，§〇-7）。**
> **产品签核行（PM §五口径：交付面/消费入口取舍须签）**：产品席判词已在册＝PM-U1 §二第7行（f2 应做判定＋最小笔规格＋七式闭集逐卷处置口径）＋§三第三段排期（路径＝`agent-skills/fuxi-skill/.collab/research/2026-11-04-FUXI-PM-U1-下一段优先级产品判定-v1.md`）＝**本票获产品签核（判词形态，非弃权）**。

---

## 〇、复核结论（架构席 2026-11-06 实读实跑实查，票内定稿依据）

1. **仓内入口面零存在实证**：`git ls-files` 对 fuxi 包 `SKILL.md`/`references` 零命中（products/ 下产物本体 SKILL.md 六件除外）；包根现盘无 `SKILL.md`、无 `references/` 目录——与 PM U1-3「git ls-files 零命中，无删除史」一致。
2. **STRUCTURE 声明面实读（判词转述差如实登记，非回流候裁）**：`docs/STRUCTURE.md` 现 delivery_paths 七行＝`README.md`/`adapters/`/`contracts/`/`gates/`/`products/`/`rejected/`/`specs/`——**不含** `SKILL.md` 与 `references/` 两行（PM §二第7行「STRUCTURE.md 声明的交付面缺两件」按 U1-3 上下文读＝「声明交付面中 SKILL.md＋references 两实体缺件」，实读显示声明行亦缺）。处置＝本票交付实体两件＋声明面补两行同源随动，一次闭合，不重呈 PM 判词本身。
3. **宿主旧代件只读实读**（禁动面实查基线）：宿主面＝`README.md`＋`SKILL.md`＋`references/` 九卷（卷目清单实读在册：`persona-lens-fields`／`import-mapping`／`technique-lens-card`／`pack-boundary`／`acceptance-blind-eval`／`alias-naming`／`token-cap-splitting`／`contract-anchors`／`self-distillation`）；宿主 SKILL.md frontmatter＝`version: 1.1.0`·旧 V3 工序主线（S0-S8：原料判定/候核账/字段闭集/导入七式/透镜化/补齐降级/盲评五维卡/化名命名/帽拆/落包 tag）。本票 §二 S2 处置表逐卷判定以此九卷清单为对象。
4. **新 SKILL.md 落包根即入仓级门禁扫描域（预检取证）**：`check-skill-meta.py`（run-gates SCRIPTS 在列）扫三分类目录一层包 SKILL.md——OA-S5 体量披露＝主件常驻红线 ≤200 行、OA-S2 触发描述＝description 须含 when 标记（`Use when` 等六词任一），严重度 BLOCK 族（S1–S5 问净不合格＝阻断）。新件不合规＝run-gates 新增 BLOCK＝整批退回，故 §二 S1 规格钉入该两判据＋§三验收钉零新增红。其余仓级检查（check-pointers 指针闭合／check-entity 实体名）对新增两件的读数漂移＝回执逐数照登＋归因行（FX2-1 口径，不修不动仓级面）。
5. **FUXI 断言面零涉实读**：包根 `SKILL.md` 不入产物级扫描面（`_product_scan_entries()` 只枚举 products/ 池根条目＋pending 一层）；BW-6 只消费包 `README.md`；ST-8 只消费 specs/ 两规范表——**新入口件对 assert-tool 27 项读数预期零变化**（§三-1 钉值）。`references/` 新卷不在任何 FUXI 断言基面。断言闭集 27 零碰（本票无新断言设计）。
6. **旧九卷↔仓内真源映射实读**（处置预判依据，逐卷对仓内在册真源）：`specs/perspective-spec.md`（四节闭集）／`specs/technique-spec.md`／`adapters/classifier.md`（四值闭集＋决策序）／`adapters/person.md`（六路 C1）／`adapters/method.md`／`contracts/` 三契约／`gates/` validator 族＋validator-catalog／池约定件（`products/README.md` kebab 命名纪律）——各卷职能仓内真源在场性逐卷核实入 §二 S2 预判表，工程师复核实改判须在处置表内注明改判理由（判据活性面，§三-3）。
7. **拆分裁定（U5/U6/U7 三票，理由全量入 U5 票 §〇-5）**：本票与 U5（产物文件内容面）／U6（池结构＋规程过程件＋人工闸）盘面对象零交集＝**与两票并行合法**；互不越面＝本票禁碰 `products/` 全树与 `.collab/decisions|design|research` U6 件面；U6 禁碰本票三件（§各票 §四互文）。基数三同源 27 贯穿三票零碰。

---

## 一、声明闭集（本票交付笔唯一改动面，共 3 件）

1. `agent-skills/fuxi-skill/SKILL.md`（新建·入口主件·§二 S1）
2. `agent-skills/fuxi-skill/references/legacy-disposition.md`（新建·旧九卷处置表卷·§二 S2）
3. `agent-skills/fuxi-skill/docs/STRUCTURE.md`（delivery_paths 补两行随动·§二 S3）

> `README.md`（包级详细件）零触碰（使用口径真源不变，SKILL.md 指向它）；`products/` 全树零触（U6 面）；`specs/contracts/adapters/gates/rejected/docs/STRUCTURE.md 以外` 零触；宿主面零触。回执另笔（§五）。

## 二、施工规格（逐件，落位钉死）

**S1 · 包根 SKILL.md（入口主件）**
- frontmatter 四键：`name: fuxi-skill`；`description:`＝双轨定位一句话＋装载口径＋「Use when」子句（含中英 when 标记任一命中 OA-S2）＋触发词段（蒸馏视角／perspective 产物／technique 能力卡／对象分类四问／入池规程等）；`version:` 入口件当期值（宿主换代部署时的 bump 归注册面另工序）；`agent_created: true`。
- 正文按包 README「使用口径」段（L38 六步链）重写为工序主线表（骨架在表、细则指向仓内真源路径，不复写细则正文）：①对象登记→②`adapters/classifier.md` 分类（四值闭集＋决策序）→③`adapters/person.md`／`adapters/method.md` 蒸馏→④validator 门禁（method 硬门 `gates/validator-source-anchor.py`／person 软门 `gates/validator-public-anchor.py`；结构层 `gates/assert-tool.py`）→⑤入池 `products/`（人工确认＋独立提案＋版本审计前置，池约定件 `products/README.md`）→⑥装载口径（宿主显式注册制，分卷注册期预编译）——每行「细则真源」列＝仓内路径逐字。
- 必含声明三句：①「与前序同名旧物（旧 V3 代工序件）无继承关系」（与 README L11 同款口径）；②防误用一句（builder≠产物库本体、不在运行时扮演任何人）；③references 索引一行指向 `references/legacy-disposition.md`（旧代读者定位卷）。
- 体量硬红线：全文 ≤200 行（OA-S5 取值，run-gates BLOCK 族）；正文禁泛指过程词表（validator-catalog v2 体例注入纪律）；禁实体名泛指违例（check-entity 预检）。

**S2 · references/legacy-disposition.md（旧九卷处置表卷）**
- 性质＝交付面卷（自包含成文）：旧 V3 代同名技能 references 九卷 → 仓内新双轨真源的逐卷处置表，供旧代消费方定位新真源；本卷＝新交付件，非旧卷搬运。
- 七式闭集口径（处置取值域钉死）：直接随迁／适配／合并／拆分／降级／裁撤／不随迁。
- 表列＝旧卷名｜旧职能一句话｜七式判定｜仓内承接真源路径（裁撤/不随迁亦须给出「该职能现由谁承载或为何不出仓」）｜判定依据一句话。
- 架构席预判九行（工程师逐卷复核，改判须注明依据）：`persona-lens-fields`＝裁撤（承接 `specs/perspective-spec.md` 四节闭集）；`technique-lens-card`＝裁撤（`specs/technique-spec.md`）；`pack-boundary`＝裁撤（`adapters/classifier.md` 四值闭集＋归包判定归池约定件）；`contract-anchors`＝裁撤（真源＝仓内 `contracts/` 三契约，V3 外部静态锚不随迁）；`self-distillation`＝裁撤（`adapters/person.md` 六路 C1＋`contracts/evidence-grading.md`）；`alias-naming`＝裁撤（新链实名 kebab 命名纪律＝池约定件 §一，化名制废止）；`acceptance-blind-eval`＝裁撤（新链 person 软门＝格式检查表门禁位＋judge 层参考位，五维卡不入闸；独立复跑原则承接 `gates/validator-catalog.md`）；`token-cap-splitting`＝降级（分卷预编译＝条款级在册，拆件细则不随迁，登记候补观察随回执）；`import-mapping`＝不随迁（七式＝本次换代处置技法，其结果即本表本身，新链无导入工序）。
- 卷尾登记行：宿主旧代件原位不触碰指针一行（换代部署＝注册面另工序）。

**S3 · docs/STRUCTURE.md 声明面随动（恰两目）**
- delivery_paths yaml 块补两行：`  - SKILL.md`＋`  - references/`（插在 `README.md` 行后，其余七行零动）。
- 正文分层清单补对应两行（`SKILL.md — 技能入口主件`／`references/ — 旧代处置映射卷`），格式同款；惯例句与 schema_version 零动。

**工序序＝S2（处置表先定，逐卷复核）→S1（入口件引用处置表与真源路径）→S3（实体实存后声明随动）→§三验收全跑→回执笔。git 面交付笔＝S1/S2/S3 恰三件＋回执笔可两笔。**

## 三、验收判据（三态禁假绿，全部可机械验证）

1. **FUXI 断言面零涉钉值**：`python agent-skills/fuxi-skill/gates/assert-tool.py` 汇总行逐字 `PASS=25 FAIL=1 PENDING_STAGE=1 总数=27`·exit 1；27 项明细逐字节与开工基线全等（含 BW-3 六命中明细、FC-6 读数按开工时点态——U6 若先行收口则 FC-6 以 U6 收口态为开工基线照登）；连跑两次全等；selftest 四件 155/40/22/19 零回归。
2. **声明面实存对拍钉值**：delivery_paths 八行逐行对盘上实存 ＝8/8 在场（SKILL.md 文件＋references/ 目录新建实证）；`git ls-files` 对包根 `SKILL.md`＋`references/` 命中数＝2（换代前零命中的随动实证）；STRUCTURE diff 行数＝正文两行＋yaml 两行。
3. **处置表闭集活性**：legacy-disposition.md 行数＝旧九卷清单逐卷恰一行（9/9，卷名与宿主面实读清单逐字对拍，§〇-3）；「七式判定」列取值 ∈ 七式闭集（机械可 grep 对表）；裁撤/不随迁行「承接真源路径」列逐路径盘上实存（可开可解析）。
4. **仓级门禁零新增红钉值**：`bash agent-skills/object-audit/scripts/run-gates.sh` exit 0·`GATE PASS`；OA-S5 实证＝SKILL.md 行数 ≤200（回执照录实测行数）；OA-S2 实证＝description when 标记命中；check-pointers／check-entity／check-collab-lint 对新增两件＝零 BLOCK；存量逐数照登＋新增 WATCH 归因行（FX2-1 口径）。
5. **宿主面零触碰实证**：`git diff`／盘面对账＝仓外零写入；回执登记宿主件路径＋「原位原状未触碰」一行＋「换代部署归注册面另工序」指针行。
6. **碰面闭合**：交付笔 `git show --name-only` ≡ §一 三件；`git diff` 对 `products/` 全树／`README.md`／`specs/`／`contracts/`／`adapters/`／`gates/`／`rejected/`／U6 过程件面／他案 TK-GWP 在途面＝零改动。

## 四、禁动面（违任一＝整批退回）

- **宿主装载面零触碰**：`C:\Users\peter\.workbuddy\skills\fuxi-skill\` 全树只读；禁复制旧卷正文入仓（处置表＝判定＋指针，非搬运）；禁代做注册面部署。
- **`products/` 全树零触**（U6 面互不越面）；池约定件零触；U6 过程件（decisions/design/research）零触。
- **包 `README.md` 零触**（使用口径真源；SKILL.md 只指不搬）；specs/contracts/adapters/gates＝零触（真源面）。
- **门禁面／断言闭集 27 零碰**；基数三同源＝FX-U4 收口态原样；evidence 桶不入 git；史账不随正；已裁项不回流（PM f2 判定在册不重呈）。
- **STRUCTURE 只补两行制**：除 §二 S3 四行外该件零动（惯例句/schema/其余声明行）。

## 五、回执要求

`.collab/receipts/2026-11-06-FUXI-FX-U7-工程师回执-v1.md`：开工 ANCHOR＋开工三读数；§六判据逐条实跑读数全文（27 项零变化对拍＋8/8 声明对拍表＋处置表九行全文＋七式取值对表＋承接路径实存清单＋SKILL.md 实测行数＋run-gates 照登归因＋宿主零触碰登记行）；预判九行如有改判逐行改判理由；`git show --name-only` 清单。一票一批一 commit（交付＋回执可两笔）。

## 六、候裁单列

- **候裁无**。发现一登记项非对立分歧如实呈报：PM §二第7行「STRUCTURE 声明缺两件」转述与实读（声明行亦缺）之差＝转述精度差，本票 §〇-2 已按实读同源闭合（实体＋声明一次补齐），不构成回流候裁。`token-cap-splitting` 降级登记的「分卷细则欠账」入候补观察（随收口登记候补池，不起票）。

## 七、纪律

一票一批一 commit（交付＋回执可两笔）；**并行令＝本票与 U5/U6 并行合法**，开工无前置（各以开工当轮实读数为基线）；互不越面＝禁碰 `products/` 全树与 U6 过程件面（U6/U5 票 §四互文）。QA 席独立核验另票另件，fresh eyes 全实跑：§三判据逐条复现＋对抗例钉死——**对抗一（入口件超限咬合）**：scratch 复制 SKILL.md 追加至 >200 行→check-skill-meta 必 BLOCK 形态发现（OA-S5 活性实证）→复原；**对抗二（处置表虚报承接）**：任选一裁撤行承接路径改名注入→路径实存检必咬；**对抗三（旧卷搬运检出）**：对宿主九卷逐卷抽 20 字连续串对仓内新两件 grep＝零命中（证「判定＋指针非搬运」）。临时工作物只落本仓根 `.scratch/FX-U7/`；复现门禁基线禁用只读 worktree（教训在册），用仓根现盘态。

——架构席 arch-fuxi-u7 起草·2026-11-06·除本票面外零写入。