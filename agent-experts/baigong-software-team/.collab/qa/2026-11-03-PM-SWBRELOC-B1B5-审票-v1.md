# PM-SWBRELOC-B1B5 审票 v1——产品席独立审票（B1–B5 迁移施工票全套五票）

## 〇、读数与手续

- 审票轮 HEAD 实测读数＝`232bcfb`（≥ 开工门槛 `232bcfb` ✓）。
- 被审五票 commit 读数（`git log --oneline` 实测）：
  | 票 | 文件 | commit |
  |---|---|---|
  | B1 骨架票 | `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-SWB-B1-收口登记-v1.md`（票面 `b5fd2b4`·已退役·寻回见 SWB-RET 退役名录） | `b5fd2b4` |
  | B2 交付面搬家票 | `...-B2-delivery-tree-migration-ticket.md` | `f017a51` |
  | B3 过程域搬家票 | `...-B3-process-domain-migration-ticket.md` | `d584d7b` |
  | B4 门禁票面锚定随动票 | `...-B4-gate-ticket-anchor-sync-ticket.md` | `9ae0b8a` ＋ 勘正微笔 `232bcfb` |
  | B5 收尾票 | `...-B5-closure-gitignore-readme-ticket.md` | `8f5efa9` |
- 审票人＝产品席（pm-relocrev）；性质＝只读独立审票（fresh eyes），除本报告件外零触碰任何文件。
- 审票依据（本席全部直读原文，非转述）：施工基线＝`.collab/design/2026-11-03-restructure-proposal-draft-v3.md`（B0 冻结件）；B0 冻结登记 `.collab/2026-11-03-SWB-B0冻结-仓目录重整方案v3基线登记-v1.md`；裁定件 `f135855`（票面落位＋T07/T08R 放行）、`f5a0d96`（迁移禁用誊写）、裁定三（项目自由分层×`.collab` 固定结构×docs 约定 md·含 §二点五/二点六/二点七/二点八/二点九）、裁定「ADR 正件落位 docs」；T08R＋A1 收口登记 `.collab/2026-11-03-SWB-T08R-A1-收口登记-v1.md`（R①–R⑨ 路由·R⑧ (i) 向定案）。
- 现盘实测对账（本席亲跑·对票面基线读数复核）：
  - `git ls-files deliverables/` ＝ **198** ✓（B2 票面基线全等；v3 §三写「203 件」＝起草时点漂移）；
  - `git ls-files .collab` ＝ **597** ✓（分桶：tickets 85／qa 159／receipts 51／board 1／design 24／decisions 16／research 242／**evidence 2（tracked！）**／根散件 17）；
  - untracked 文件系统面：refs **8835** ✓／evidence find **3857**（票面 3827·见 S6）／inbox＋dispatch **19** ✓；
  - 两支 untracked `2026-11-01-TKT-*` 件现盘 `.collab/qa/` 在位 ✓；
  - `git ls-files docs`（旧仓根）＝ **8 件**（`docs/README.md`＋`docs/process/` 1 件＋`docs/research/` 6 件·见 R-1）。

---

## 一、总则核验（五票共性·审①③⑤面）

1. **三附注照载齐全**（审③）：誊写禁令（`f5a0d96`·仓内 `git mv`／跨仓字节级复制＋删源·判据「新位与原位 diff 仅申报剥壳段／字节一致」）、票面落位 `.scratch/tickets`（`f135855`）、era 跨仓口径（字节复制两笔对账）——**五票票头全部照载齐全**，且各票按自身辖域做了自察声明（B1「新建创作类辖域外自察」、B4「原位代码文本随动批非搬家批·照注自察」、B5「gitignore/README 重写＝创作类辖域外」）。此自察分层与裁定 `f5a0d96` §二.3「新建创作类件不属辖域」口径一致，未借自察规避搬家目。✓
2. **票面落位合规**：五票本体均在 `.scratch/tickets/` ✓；B1-F 建 `.scratch/tickets/README.md`；B3 含 `.collab/tickets`→`.scratch/tickets/` 搬家目＋E-ARC-1′ 换锚先行硬线（B3a 跑绿前 B3b 禁启动）——B0 附注②照位。✓
3. **B 批判据四目对位**（审②）：
   - 目①（tickets 搬家 git mv＋换锚先行＋落位形态）→ B3a/B3b ✓；
   - 目②（check-ticket-reconcile 缺省票目录按 `.scratch/tickets` 实装＋扫描面非空正断言防假绿）→ B4-A1/A2（枚举为空 `SystemExit(4)`）✓；
   - 目③（era 跨仓字节复制两笔对账）→ **五票内均未实装**，一致指向 ESC1 独立微批（B5 票间关系「随 B4/B5 后」在册）——v3 §六清残注记二允许「B 批随移动作**或**独立微批」，路径合规，但 **ESC1 票至今未出**（见 S1）；
   - 目④（两支 2026-11-01 TKT untracked 旧件随批入库）→ B3 判据7（`git ls-files | grep -c "2026-11-01-TKT"`＝2）✓。
4. **候裁回流检查**（审④）：五票候裁点全「无」，逐项对账裁定面——拼写 `agent-experts`（清残注记一）→ 五票目录名一律照用 ✓；票面落位（`f135855`）→ 无回流 ✓；era（清残注记二降执行项）→ B3 按 ESC1 候选留置、票面明示「不上呈皮总＝执行层」✓；D7 落 docs → B5-C 执行 ✓；R⑤ 约定 md 定名 STRUCTURE.md → B1-C 执行 ✓；R⑧ (i) 向 → B1-D 先决＋B4-C 精化 ✓；R⑨ 表2-1 追认 → B4-D 执行 ✓。**无已决事项被列为候裁** ✓。B4 把「门禁路由加挂 `--scope docs/adr`」明确推出本票（＝另票另裁）——ADR 落 docs 裁定的随动义务属 ES v3 作者席议程，B4 不吞并，边界干净 ✓。
5. **票面与冻结基线 v3 符合性**（审②主面）：批次切分＝v3 §五逐批对位；§三归宿表逐行有承接票（交付面行→B2；过程域各桶行→B3；gitignore/README/D7 行→B5；tools 行→B2-C/B4）；§四三技术点 D5（不换锚）/D6（git mv＋tag＋fuxi 预演）/D7（入库落 docs）分别在 B2-A0/B2 判据7/B5-C 落目；§五判据（每批单独 commit＋机械判据＋对账清零＋门禁零回归对拍）五票均自带。除 §二专项一处基线内部不自洽外，**未见票面越权改动冻结基线语义**。✓
6. **最佳实践对标**（审①·时效优先近 3 月、权威优先行业一致标准）：`.scratch/tickets` 高频迭代件落位＋一票一文件＋Status/Blocked-by（Matt Pocock 式）＝当代 agent 工程社区主流实践，与「票＝架构到施工间的迭代交接件、非持久分发对象」的皮总定性一致 ✓；`docs/` 只放当前存活干净交接件＋STRUCTURE/PRODUCT/ARCHITECTURE 三件套命名（去 collab 前缀）＝对齐通用文档约定 ✓；仓根白名单闭集＋项目物理隔离自包含＝对齐 monorepo「可整体拷走」与 package-per-project 惯例 ✓；`.collab` 固定结构由规范件单一定义、用户 md 覆写不认＝对齐「约定优于配置＋规范真源唯一」惯例 ✓。B3 票面选择**不做** Matt Pocock 式头部转换（Status/Blocked-by）＝v3 明示「与否随裁」＝未决项由票面裁定＋回执登记，非已决回流，产品席认可该裁定（保持史实票面字节一致优先，与誊写禁令同轨），建议主理人核销一行确认。

---

## 二、专项判定：B3「勘误注记」（v3 L70 两支 TKT 件归宿＝登记争议）

**争议**：v3 §三 L70 行把「工作区 2 支 2026-11-01 TKT untracked 旧件」归宿标为 **fuxi-skill** `.collab\qa\` 入库；B3 归项目分账函数规则 1（名含 `TKT`→baigong）与之冲突。B3 票处理＝**分账函数为准归百工**，v3 该行按 erratum **登记回执**，不静默改冻结基线。

**产品席口径：处理路径合规，实质判定成立；须补一步程序闭环（不构成红项）。** 四条依据：

1. **实质判定正确**：TKT 系即 SWB 票包分票案卷线。现盘 14 支 TKT 票（票名如「TKT28-SWB票包v2.7基线再锚定」「TKT36-SWB-ticket-pack-V11-re-anchoring」「TKT40-SWB-ticket-pack-V13-re-anchoring」）＋30 余支 TKT 案卷件全部属 SWB/百工案线；两支争议件（`2026-11-01-TKT-双席审计过程件汇总-v1.md`／`2026-11-01-TKT-最终分票件全文汇编-v1.md`）即该案线过程案卷，归百工无疑。v3 L70 标 fuxi 系笔误。
2. **冻结纪律未被破坏**：B0 冻结令＝「B1–B5 出票一律以 v3 为准，方案文本改动须走修票/增补程序，不得顺手改」。B3 对 v3 文本零触碰，改以回执 erratum 登记＝正是「不静默改基线」的合规形态，优于直接改表行。
3. **上位判据留有可据缝隙**：B0 冻结登记 B 批判据四目④对这两支件只锁定「随批入库路径」，**未锁定归属项目**；冲突仅存于 v3 §三表行一处，属基线内部不自洽（表行 vs 四目＋同票函数）。票面择「四目＋全票统一分账函数」口径，优于择单行表笔误——若反取 fuxi，反而破坏分账函数全票统一性与案卷同桶守恒。
4. **须补完**：erratum 现仅「回执登记」级。按 B0 冻结纪律的完整闭环，应由主理人在 **B 批收口登记**中落一行「v3 §三 L70 erratum 增补登记（照引原行＋判定依据＝分账函数规则1＋四目④未锁归属）」＝增补程序实体落笔；B3 回执须照引 v3 L70 原文以供对账。补完此步则登记链条无懈可击。

---

## 三、逐票三态判定

### B1 骨架票（`b5fd2b4`）——**认可**（附黄项 B1-Y1）

认可面：
- 三分类目录＋项目名录＝v3 §一白名单＋清残注记一（拼写已决）照载；`softwares` 空名录＋「届时再入」＝v3「届时再入」口径 ✓。
- 7 项目固定 `.collab` 桶名录＋两制入库声明＝裁定三§一.1① 固定结构；「用户 STRUCTURE.md 内 `.collab` 段落不认」＝裁定三§一.3 照录 ✓；B1-D 规范件＝R⑧ (i) 向精化先决闭集真源（收口登记 `ed5d3c0` §三对位），且明示「引用指针不复写 B4 行文本」＝真源唯一纪律 ✓。
- STRUCTURE.md 定名＋YAML 围栏＋`schema_version`＋delivery_paths 拒 `docs/` 前缀行机检款＝裁定三§二点九＋T08R 提案字段冻结 ✓；拒 docs 前缀与「docs＝人读交接件、交付路径不得落 docs」的语义自洽 ✓。
- gitignore 只增不删（B5 全重写前过渡防御）＋禁动面自声明＋`.scratch/` 不 ignore（票面入库面）＝与 `f135855` 语义一致 ✓。
- 声明闭集逐行点数复核＝**20 件** ✓；判据 1–7 全部机械可判（含负例 exit≠0、过渡态顶层白名单含 `deliverables/docs` 并注明 B2/B5 灭）✓。
- B1-C「已知数据面缺陷登记不改数据面·随 B4 修」＝缺陷在册不顺手改＝冻结纪律正确形态 ✓。

**B1-Y1（黄）**：B1-D 规范件落 bundle 交付面内新建（`skills/sop/references/collab-fixed-structure.md`），票面自察「本批不入交付包体·零 bump」——与纪律①「bundle 本体每变必 bump」存在张力（该文件是 bundle 组件内容）。票面已自察申报、且 B2 随即 bump 0.1.17 实质覆盖，风险可控。修法＝B 批收口登记追认此格免 bump，或将 bump 前移至 B1（一行）。

### B2 交付面搬家票（`f017a51`）——**有条件认可**（须修 B2-Y1、B2-Y2）

认可面：
- 全部搬家＝`git mv`、剥壳段申报＝恒 0、判据 2 R100 占比＋抽样 10 件 `git diff` ＝0 双断言＝誊写禁令判据实装到位 ✓。
- D6 既裁三件套齐全：开工打 `archive-pre-B2-*` tag（判据7）＋fuxi 线小规模预演先行（B2-A0 单独一笔·不成即 revert 呈核不硬推）＋rename 保历史 ✓。
- **壳位防撞规则（内容注入式逐 `git mv` 入壳·禁整目录替换）**＝本票最亮处：识别出 B1 已建 `agent-experts/baigong-software-team/{.collab,docs}` 壳会与整目录 mv 相撞，主动改形并逐笔回执——跨票依赖处理正确 ✓。
- PRODUCT/ARCHITECTURE→`docs/`＝v3 §三 L57＋裁定三§二点八；并核「plugin.json 未声明此两件＝纯人读文档·包内迁移平台面安全」＝迁移安全性核验到位 ✓。
- 门禁扫描根**同批**随动（缺则本批 GATE 必红＝同批硬随动判定正确）：check-pointers DEFAULT_SCOPE/根探针/候选层三层分类、check-pointer-closure DEFAULT_PKG_FACES、run-gates GATES_MD 候选序＋根探针、bundle.lock `path`、tools/check-source-of-truth spec 锚与用法注释、钩子再生（不手改·前后两读数）——覆盖面完整且逐项可验 ✓。
- check-ticket-reconcile / check-collab-lint spec 锚 / 60-gates 叙述面明确「不在本批」并指向 B3a/B4＝批次边界干净、无越批 ✓。
- 版本 bump 0.1.16→0.1.17＋README append-only＝纪律① ✓；实测基线 198 件分桶与本席现盘全等 ✓。

**B2-Y1（黄·须修）**：判据 1 计数算式自缠——同一条款内并存「＝197」「含 STRUCTURE.md 1→**110**」「判据式＝Σ新桶−B1 壳件＝197」多口径。本席按现盘推演：mv 后新桶总量＝197（mv 件）＋16（B1 壳件＝7 STRUCTURE＋7 项目 `.collab/README`＋2 分类 README）＝**213**；`agent-skills` 侧亦与票面 109/110 不合。票面以「回执逐桶表为准」兜底，但判据式必须写死一条可跑断言，否则执行席自行择算式＝判据失去机械性。修法＝改为双式 `git ls-files agent-experts/ agent-skills/ | wc -l` ＝ 197＋壳件数（票面算出壳件数明文）＋`git ls-files deliverables/` ＝ 0。

**B2-Y2（黄·须修）**：判据 3「活引用清零」grep 面只含 `*.py/*.sh/*.json`，包内 **md** 对 `deliverables/` 的活引用（spec_file 头块注释、SOP/席位卡引用串，如 run-gates.sh L4/L13/L22/L34 与同型 md 锚）只靠门禁 check-pointers 兜底；而禁动面同时规定「六包与 bundle 内**非随动清单文件**内容零触碰」。若门禁在本批因 md/注释锚悬空指红，可写面与禁动面互斥无解。修法＝开工前在票面或回执口径明确：随动清单是否涵盖「spec_file 头块与文档锚路径行」；若不涵盖则这些旧路径须以史述豁免清单逐处登记＋门禁零回归读数佐证。附带：v3 §三「203 件」vs 实测 198 之差按实测立账＝做法正确，回执登记一行漂移说明即可。

### B3 过程域搬家票（`d584d7b`）——**有条件认可**（须修 B3-Y1、B3-Y3；B3-Y2 建议项；专项 erratum＝合规见§二）

认可面：
- **B3a 换锚先行（单独 commit·跑绿前 B3b 禁启动硬线）→ B3b mv** 的序＝B0 附注②＋批判据四目①全照，且判据1 给出可跑未 0 即禁启动的前置断言 ✓；裸票 ID 基名族零改＝非路径语义豁免口径合理 ✓。
- 归项目分账函数＝六序正则（首中即停），FUXI 先于 `QA-`/`ARCH` 等泛词、era 族单列候选、其余人工分账面缺省归百工（v3 L62「纯仓级归百工」口径）——机械可跑、顺序设计正确、兜底不吞争议件 ✓；配套要求回执逐件分桶表 ✓。
- 根 17 散件归桶定标：以「固定结构闭集无 `cases/` 桶＝不新增桶」为红线，按内容形态归同名桶（登记件＝质量链过程账归 receipts、裁决本体只在 decisions）＝对 B1-D 规范与裁定三§一.1① 的忠实执行 ✓（本席实测根散件 17 件与票面全等）。
- era 候选留置原位＋列 ESC1 移交清单附件＝清残注记二执行项口径；票内不搬＝跨仓两笔对账另批，符合附注③ ✓。
- 判据 5「旧域清零」＋判据3 R100 100%（改锚笔单走不混 mv 笔）＋判据6 过渡态在册（如实登记 check-ticket-reconcile 旧缺省扫描面变空的危险窗口读数＝非绿不判红）＝诚实过渡态登记，无假绿设计 ✓。
- 两支 untracked TKT 入库＝四目④；`2026-11-01-TKT` 计数断言＝2 ✓。

**B3-Y1（黄·必补·开工前一行级）**：`.collab/evidence/` 桶下有 **2 件 tracked 史实锚**——`2026-10-29-判词-T-team-rename-01.md`、`2026-10-29-回执-team-rename-01.md`（本席 `git ls-files .collab/evidence` 亲验）。票面把 evidence 整桶归入 B3e「文件系统 mv·untracked 面」。若照此走文件系统 mv：旧位从工作区消失＝索引残留悬空，新位被 B1 过渡块 `/**/.collab/evidence/` 吞掉不被 add，而判据2 用的是 `git ls-files` 计数＝**索引未动仍计数→假绿**，两件史实锚有脱出版本库风险。修法＝此 2 件改列 `git mv` 面（`git mv` 不受目标 ignore 规则影响），并在判据2 增补 `git status --porcelain` 为空断言。

**B3-Y3（黄·必补）**：判据2 守恒式基线口径与断言口径不同域——票面 597 是 `git ls-files .collab` 单域，判据2 断言用 `git ls-files | grep "\.collab/\|\.scratch/"` 双域，会把 B 批五票面＋B1 `.scratch/tickets/README.md`（现盘 `.scratch` tracked 已 5 件，B1 收口后 6 件）计入迁后侧；照式跑「597＋2」必然短 6～7 件＝假红。修法＝写明双侧同域口径（建议：`git ls-files .collab .scratch | wc -l` 迁前实测 vs 迁后实测＋2）。

**B3-Y2（黄·轻·建议）**：era 正则「视频|video|短剧|导演|编剧」按**名**命中，会把 devkits 自产件误留置入 ESC1 候选（如 `2026-10-23-视频团队本体审计_v1.md` 系本仓自产审计，非外部快照）。留置＋主理人核销机制可兜住不外流，但 ESC1 移交清单应标注「按出处（自产 vs 第三方外部快照）二次分账」，避免把自产判词依据件搬到 experts 仓造成真源离仓。

### B4 门禁票面锚定随动票（`9ae0b8a`＋勘正 `232bcfb`）——**有条件认可**（须修 B4-Y2；B4-Y1、B4-Y3 处置项）

认可面：
- 批判据四目②实装完整：缺省票目录**按项目双候选**枚举（`{agent-experts,agent-skills,softwares}/<project>/.scratch/tickets/`）＋无则跳过**不再回落旧域**（旧域 B3b 已灭）＋**扫描面为空 → `SystemExit(4)` infra error 防假绿**＝本席认为这是全套票里对「门禁哑火」危险形态最关键的一处正面设计 ✓；判据1 正例（exit 0）＋负例构造（仓外 Temp 无票目录 exit 4）双向闭合 ✓。
- R⑧ 精化＝按收口定案 (i) 向：保留 `.collab/**` 基线 deny＋按 B1-D 规范闭集逐桶枚举减授权（除 host 租约授权桶），并明示「桶名以 B1-D 规范件为唯一真源·grep 引用不复写名录」＝定案忠实＋真源唯一 ✓；过渡态 (III) 显性化冲突在册消账路径清晰 ✓。
- R⑨ 追认＝**不改正文·文末追加一行注记**＋V13 恒等式保护声明（尾追加不扰动 L1–260 行号、追加行不入 V13 段）＋判据5 三哈希（全文/产品段/架构段）逐字复算不变＝append-only 与恒等式纪律的标准形态 ✓。
- write-guard/lease-issuer 两级锚（项目根＝上溯首个含 `docs/STRUCTURE.md` 目录；仓根仅用于交付 listing 与 git 子命令；权限字面读作项目根相对）＝裁定三 席位执行规范③＋§二点九 承载面的正确落地；lease 账本根随项目根＋覆写语义零动 ✓。
- B4-E engineer 枚举行按 D1 名录填充＋判据6「STRUCTURE delivery_paths ↔ seat-permissions engineer 机械行逐行相等」＝把 B1 约定 md 与权限数据面锁成同源对账，是全套票里最有价值的机检设计 ✓。
- 勘正微笔 `232bcfb` 亲验 diff＝仅「12 件→16 件展开口径」两处计数字样，非语义改动，且单独 commit、`collab:` 前缀＝手续合规 ✓。

**B4-Y2（黄·必补·跨票承诺悬空）**：B1-C 白纸黑字登记「seat-permissions `project_domain_md`＝`docs/collab-project-structure.md` 系作废名残留（裁定三§二点九定名 STRUCTURE.md）——**B4 闭集内修值**」；本席 grep 亲验 B4 票面全文无 `project_domain_md`／修值目。跨票承诺无承接＝作废名残留会活到 B4 之后。修法＝B4 闭集（已含 `seat-permissions.json`）补一行修值目（改 `docs/STRUCTURE.md`）＋并入判据6 相等断言面。

**B4-Y1（黄·处置项）**：收口登记 §三把 **R①（票面字段级约束随落位再核）／R②（host docs 转正代写·promote-manifest 通道对表）／R③（tests/ 共写双席对表）** 三项路由入「B4 议程」，B4 票面仅在票头引用了路由行（grep 亲验：`R①②③` 仅出现于 L4 出处引用），施工规格 B4-A–F 无处置目。三项均「账二维持」非阻塞，但路由会在 B4 收口后断链。修法＝B4 回执设「R①②③ 处置/在册」一节逐条落一行（处置或续在册）。

**B4-Y3（黄·轻）**：勘正后闭集口径仍差一——票注自称「16 件展开」，按其自述展开＝11 行具名（含 run-gates／check-collab-lint）＋版本三同源（bundle.lock＋plugin.json＋`.codebuddy-plugin/plugin.json`）＋README ＝ **15 件**；回执 name-only 全等会按 15 跑。修法＝再勘计数或补出漏列件。另：判据6 把 engineer 写域锁成 delivery_paths 六目录相等，则 `plugin.json`/`settings.json` 等 bundle 根文件不在 engineer 可写面内——本票不改其现面即安全，但回执应附「engineer 现面读值 vs 相等断言」读数，确认该断言不会与现存写权行冲突致红。

### B5 收尾票（`8f5efa9`）——**有条件认可**（须修 B5-Y1、B5-Y2）

认可面：
- gitignore 全量重写＝v3 L71 两制（史实锚入库／外部快照＋运行流水排除），路径随新树＋旧仓根条款退役＋**回执附新旧条款映射表**（本席认可映射表为必要件：gitignore 重写是全票包唯一「不可 diff 对账」面，映射表即其审计面）✓；负向防御条款 `!/**/.collab/research/`＋era 留置面显式注记行＝沿用现行 L13/L42–44 先例形态 ✓。
- 仓根 README 四节＝v3 §一照态＋§三 L58「deliverables/README 表并入仓根 README」＋跨项目案卷「只指不搬」索引（B0 前主理人口径＋裁定三§二点六.4）✓；判据5 名录行数＝7＋索引行数 ≥ B3c2 回执表行数＝可跑 ✓。
- D7 入库＝**字节级复制＋删源**（refs 暂住位→docs），判据＝sha256＋三哈希逐字不变＝`f5a0d96` 跨域搬运判据正确套用（同仓跨域但 git 视角＝增删两笔，故不用 git mv 的判定合理）✓；引用随动活引用清零＋bundle 来源注两处刷新→三同源 bump 0.1.19＋README append＝纪律① ✓。
- 判据1 顶层终态白名单＋判据2 check-ignore ≥8 形态矩阵（入库面/排除面双向）＝收尾票判据设计强 ✓。

**B5-Y1（黄·必补·安全面）**：B5-A 排除面清单**丢了三方外部快照条款**——现行 gitignore 对 `.collab/research/reference-2026-10-24/{video-teams,official-cos,summoned-2026-10-24}/` 的显式排除（判据 B「真源混淆」纪律·该三桶 75 件现处 ignore 态）未在重写清单中给出新树对应行；而 B3d 又把 era 候选**留置在仓根 `.collab/research/`**（ESC1 未执行）。两者叠加＝B5 重写落地后这些外部快照件从 ignore 变 untracked-not-ignored，任何 `git add -A`/门禁 add 都可能把第三方快照整批纳入我仓版本库，违「外部参照件不入我仓」既有裁决。修法＝B5-A 排除面补「外部快照桶按新树路径全量重立」一行（＋era 留置面期间维持其 ignore），并以判据2 矩阵含该形态。

**B5-Y2（黄·处置项）**：仓根 `.collab/` 残留面与终态白名单断言存在盲区——判据1 用 `ls -d */`（shell glob 不出点目录），故仓根 `.collab/`（含 era 留置 research 件＋ESC1 未搬面）不会出现在断言面；票面亦无「仓根 `.collab`＝ESC1 前唯一允许残留」的显式声明行。修法＝补一行「仓根 `.collab` 残留＝era 留置面·ESC1 域·非违例」注记，或以 `find .collab -type f | wc -l` ＝ era 留置数断言（与 B3 判据5 同式）纳入 B5 判据。

**B5 关联红项见 §四 S2/R-1**（旧仓根 `docs/` 8 件归宿悬空——B5-D 声称「B3 已分流」与 B3 票面禁动面相冲突）。

---

## 四、跨票系统性发现

- **S1（须处置·非阻塞）＝ESC1 无票面**。批判据四目③（era 跨仓字节复制两笔对账）＋附注③ 全链一致指向 ESC1，五票均「不在本票」，B5 票间关系仅写「后置＝ESC1（独立微批随 B4/B5 后）」，但 **ESC1 票至今未出**，且 experts 仓侧接收仓 `D:\multi-agent-collab-experts` 侧的接收面（目录落位/命名/对账脚本）无任何票面承载。四目③目前处于「有据无票」态。建议＝B 批收口登记前由架构席补出 ESC1 微批票（含 era 清单附件＋两仓两笔 sha256 对账＋experts 侧 gitignore 承接），否则 B 批收口判据四目③无法销账。
- **S2（红项 R-1）＝旧仓根 `docs/` 8 件 tracked 内容归宿悬空**。v3 §三 L68 明定「`docs/` 8 件（process/research 子桶）＝空壳横切，内容归各项目 docs 或 `.collab`」＝**要求迁移**。但：B3 声明闭集不含 `docs/`、禁动面明示「`docs/`（旧仓根·B5）」；B5 声明闭集仅「docs/ 残壳清灭：process/research 内容 **B3 已分流**，README 索引件删除」。**两票互相指认、无人承接**＝`docs/README.md`＋`docs/process/2026-10-22-建包过程记录.md`＋`docs/research/R1..R6`（6 件）共 8 件 tracked 件在五票可写面无归属；B5-D 若按「残壳确认空」跑则判据红，若顺手删＝违 v3「内容归位」口径且丢史实面。这是全套票唯一确定的跨票断链＝**须修票面**（建议归 B3：`docs/` 8 件按分账函数入项目 `.collab/research|receipts/`，B5 只灭壳）。
- **S3（黄·版本账跨票链）＝纪律① bump 链有空格**。票面 bump 链＝B2 0.1.16→0.1.17、B4 0.1.17→0.1.18、B5 0.1.18→0.1.19；B1（新建 bundle 交付面内规范件）、B3（B3a 改锚**触及交付面文件内容**——check-collab-lint spec_file 头块三处锚即在 deliverables 内，票面禁动面亦承认「除 B3a 改锚文本行」）均自声明零 bump。B3a 属交付面内容变更，纪律①未追认＝与 B1-Y1 同型。建议＝B 批收口登记统一追认「迁移期交付面随动改锚免 bump」一格，或把 B3a bump 并入 B4 同笔。
- **S4（黄·工具锚随动目无落笔）**：v3 §三 L69 明定「run-gates.sh 在 object-audit 包内，其 `ROOT/tools/` 锚＝**B4 改上溯/参数注入**」。B2-C 已改 run-gates 仓根探针＋GATES_MD 候选序（功能上新树可跑：tools 仍留仓根），但 B4 闭集含 `run-gates.sh` 却无对应施工规格行（B4-A–F 未提 run-gates 目）；现行脚本内 spec_file 注释锚 `deliverables/multi-collab/references/60-gates.md`（L4/L13/L22/L34）系旧路径残留。＝v3 该行落在两票缝隙。建议＝B4 补一行（改 spec_file 注释锚）或在回执登记「v3 L69 由 B2-C 根探针随动覆盖·读数附」。
- **S5（认可·设计强项）**：跨票真源单一链设计成立——B1-D 规范件（桶名闭集唯一真源）→ B4-C deny 枚举 grep 引用不复写 → B4-E engineer 写域 ↔ B1-C STRUCTURE delivery_paths 逐行相等断言。三处锁成一条同源对账，是本次迁移在权限面上的最佳实践落点，产品席明确认可。
- **S6（黄·基线读数漂移防护）**：票面 untracked 面基线 evidence＝3827 vs 本席实测 find＝3857（refs 8835／inbox＋dispatch 19 全等）。evidence 桶由门禁运行持续写入（`EVIDENCE_DIR=$ROOT/.collab/evidence/gates`），票面锚定 `f017a51` 时点读数到 B3 开工时必然增长＝B3 判据4「迁后 Σ 项目同名桶＝基线」会假红。建议＝B3 开工首步**重落盘基线**（票面已对 tracked 面要求开工实测，untracked 面未同要求），并在回执区分「票面起草读数／开工实测读数」两栏。
- **S7（认可·过渡态诚实）**：B1（顶层白名单过渡集含待灭目录）、B2（B2-A0 预演不成即 revert 呈核）、B3（判据6 危险窗口读数非绿不判红）、B4（R⑧ 过渡态 (III) 在册）四处均主动登记过渡态而非以豁免掩盖——符合本仓「假绿即缺陷」既有纪律，产品席认可。
- **S8（程序面提示）**：五票回执落位统一指向 `agent-experts/baigong-software-team/.collab/receipts/`（B1 例外＝仓根 `.collab/receipts/`）——B1 回执落旧域、B2–B5 落新域，两者相差一个 B3 搬家目。B1 回执件本身会被 B3 按分账函数（名含 SWB→baigong）搬入新桶，无矛盾，但回执落位口径应在 B 批收口登记说明一行，免得收口对账时误判「B1 回执脱域」。

---

## 五、结论表态

**有条件认可。** 五票整体质量高：三附注照载齐全、批次切分与 v3 §五/§三逐项对位、B 批判据四目①②④实装到位、候裁面零已决回流、誊写禁令判据（R100/字节一致/两笔对账）与冻结纪律（不静默改基线·缺陷在册随批修·append-only）执行忠实；§二专项 erratum 处理路径判定为**合规**（须补 B 批收口登记增补一步）。

**红项（1·须修后方可开工对应票）**
- **R-1**：旧仓根 `docs/` 8 件 tracked 内容归宿悬空（B3 禁动 vs B5 声称「B3 已分流」互指），v3 §三 L68 迁移要求无人承接＝跨票断链。修＝B3 承接 8 件按分账函数入项目桶，B5 只灭壳；或另出微批票。

**黄项（10·开工前一行级或回执级修补）**
- B1-Y1：B1-D 交付面内新建件零 bump 与纪律①张力（收口追认或 bump 前移）。
- B2-Y1：判据1 计数算式多口径自缠（现盘推演终值 213），须写死单一可跑双式。
- B2-Y2：判据3 活引用面只扫 py/sh/json，md/spec 锚与「非随动清单零触碰」互斥风险＋203 vs 198 漂移登记。
- B3-Y1：`.collab/evidence/` 2 件 **tracked** 史实锚被当 untracked 面文件系统 mv→脱库风险＋`git ls-files` 口径假绿（改 `git mv`＋`git status` 空断言）。
- B3-Y2：era 按名正则误留置自产研究件（ESC1 清单按出处二次分账）。
- B3-Y3：判据2 守恒式基线域（`.collab` 单域 597）与断言域（`.collab`＋`.scratch` 双域）不同→必然短 6～7 件假红。
- B4-Y1：R①②③ 路由入 B4 议程但票面无处置目（回执逐条落一行在册）。
- B4-Y2：B1 承诺「`project_domain_md` 作废名 B4 闭集内修值」在 B4 无承接＝悬空（必补）。
- B4-Y3：闭集展开自称 16 件实为 15 件；判据6 相等断言需附 engineer 现面读数确认不撞。
- B5-Y1：gitignore 重写清单丢第三方外部快照排除条款＋era 留置仍在仓根→外部快照漏入库真源混淆风险（必补）。
- B5-Y2：仓根 `.collab` 残留落在 `ls -d */` 断言盲区（补注记或补 find 计数断言）。
- S1：批判据四目③ era 跨仓「有据无票」，ESC1 票未出（收口前补出）。
- S3：B1/B3a 交付面变更免 bump 未追认（收口统一追认）。
- S4：v3 L69 run-gates `ROOT/tools` 锚随动目落两票缝隙。
- S6：untracked 面基线读数漂移（evidence 3827→3857）未要求开工重落盘。
- S8：B1 回执落旧域 vs B2–B5 落新域，收口对账需一行口径说明。

**判定细分**：B1＝认可（附黄）；B2＝有条件认可；B3＝有条件认可（R-1 承接修在 B3）；B4＝有条件认可；B5＝有条件认可。§二专项登记争议＝**产品席口径＝B3 处理合规、归属判定正确（归百工）、须补 B 批收口登记 erratum 增补一行**。

（本报告件＝产品席独立审票产出；除本件外全程零触碰。）
