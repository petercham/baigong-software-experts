# COLLAB-STRUCT-1 .collab 结构名实对齐与规范成文 · 施工分票 v1.1（纯规格·零施工）

- **票号**：COLLAB-STRUCT-1｜**版本**：施工分票 v1.1｜**性质**：施工执行规格件（本件本身零施工）
- **存活态声明**：自本件落链起，同题施工依据存活态唯一＝本件 v1.1；v1 链上件照登不动（append-only 史实锚），不再作为工程师席施工依据。本件正文逐字自包含成文，工程师席照本件条款直接执行，不得回取带出处钉的规格来源原文替换。
- **仓根**：`D:\multi-agent-collab-devkits\`
- **本件落点**：`D:\multi-agent-collab-devkits\agent-experts\baigong-software-team\.scratch\tickets\2026-11-09-COLLAB-STRUCT-1-施工分票-v1.1.md`（按本票 §2 A4 住址成文行，落在 bundle 项目根 `.scratch/tickets/` 体例目录；目录已在位）
- **依据（规格来源·仓内绝对路径点名）**：
  1. `D:\multi-agent-collab-devkits\.scratch\tickets\2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v2.md`（251 行／46,944B／链笔 `5eeeb3a`）
  2. `D:\multi-agent-collab-devkits\.collab\decisions\2026-11-09-皮总裁定-STRUCT-v2放行与六项候裁取态.md`（92 行／9,397B／sha256 前 12 `7ded3258a84c`／链笔 `6c495d4`；append-only 史实锚，本批零改）
- **开工读数（落笔前实跑·实测）**：`date`＝`Mon Nov  9 04:30:04 2026`（本机时钟）／`git rev-parse HEAD`＝`a378642d0ddd521d2c8fe0c23e76d0ee58ab2f3c`（短 `a378642`）／`git status --short --untracked-files=no`（tracked 面）＝空（净）。
- **落笔前复点（实测·链漂移照登）**：`date`＝`Mon Nov  9 04:44:16 2026`／HEAD＝`4692857dd263621df1bee65633a765dd5b583190`（短 `4692857`）。自派工来件开端 `f9b5403` 起，链上新增 `d41326e`／`6c0c91b`／`a378642`／`4692857` 四笔全属他案在制品，照登不碰；tracked 面他案 staged 一件＝`agent-skills/fuxi-skill/.collab/receipts/2026-11-08-FUXI-FX-U24-收束调查-v1.md`（A 状态），照登不碰；本件双侧 pathspec 单件落账，防污染笔。上述漂移不改本票射程与任何钉值口径。
- **五张 agent 卡现态复点（逐件行数／字节／sha256 前 12·实测）**：`software-team-product.md` 46／3,227／`a1c6a4f8ecce`；`software-team-architect.md` 47／3,825／`1c51935d3ca6`；`software-team-qa.md` 49／3,848／`0bcda097f0f7`；`software-team-engineer.md` 49／3,951／`b4331d7422c4`；`software-team-lead.md` 77／5,298／`c2287132f1e8`。五卡 sha 钉与基线全等；五卡 `T3` 挂载句现值 `grep -c`＝0／0／0／0／0，链上无 SEMGV-T3 施工笔，基线钉继续有效。若施工开工时链上已现 SEMGV-T3 施工笔，即以其为基线，五卡 sha 钉作废并按实测重取；一切行号锚按内容锚定位、不锁死行号。
- **其它开工复点实测（逐项·现盘）**：三同源 `plugin.json`／`.codebuddy-plugin/plugin.json`／`bundle.lock` 现均 `0.1.30`（本批零 bump）；仓根 `.collab/qa/` tracked 10、包内 `agent-experts/baigong-software-team/.collab/qa/` tracked 234、`agent-skills/fuxi-skill/.collab/qa/` tracked 48、`agent-skills/external-advisor-collab/.collab/qa/` tracked 2（全仓 `git ls-files | grep -c "/\.collab/qa/\|\.collab/qa/"`＝294）；**两包不并入本批迁移，两包 qa 现值以施工开工复点为准、不锁死本数（现盘 48＋2＝50；登记基线 46＋2 系史实登记值、非实质意图，现值漂移 +2 照登不碰）**；包内 `.collab/audits/` tracked 现值 6 件、仓根 `.collab/audits/` tracked 现值 0 件（目标桶既有件照登不碰，名实对齐后并存），包内 `.collab/audits/` 内 `/qa/` 命中＝0（防嵌套断言现值）；仓根 `.collab/` 根面 tracked 散件恰 20 件，`decisions/` 直系 tracked 56 件，两者 `comm -12` 实测空＝零同名冲突；`.collab/tmp-w7-msg.txt` 留痕实测＝23 行／2,270B／sha256 `037a83b30b08741c9bf476496284ce7357b5f164388f4f1a697e5627a9a50056`，被 `.gitignore:36 /.collab/tmp-*.txt` 忽略（`git check-ignore -v` 命中该行）；ledger untracked 恰三文件；包内 `.collab/drafts/adr/` 恰四件；仓根 `.scratch/tickets/` 内 COLLAB-STRUCT 票族三件 tracked、bundle 项目根 `.scratch/tickets/` 内票族专名 0 件（本件 v1.1 与 v1 施工分票按住址成文行亦落此面，含 `COLLAB-STRUCT` 字样但不属票族专名，不计入 §5 判据 9 落位核对）；历史文内旧字样现值随盘漂移、以施工开工复点为准、不锁死本数（`git grep -l "\.collab/qa/" -- '*.md'`＝218 文件、`git grep "\.collab/qa/" -- '*.md' | wc -l`＝355 行、`drafts/adr`＝72 行、「十一桶」＝81 occurrence）。

---

## §1 施工总纲（先读本节再执行）

1. **同批一 commit**：§2 A 组（配置与规范成文）与 §3 B 组（目录实体迁移）**必须同批一个 commit** 落账。配置指新名／实体已就位，两态不并存；不得拆成「先改配置、后搬目录」两笔，也不得只做其中一组。
2. **施工序**：先 SEMGV-T3、后 COLLAB-STRUCT-1。本票施工须待 SEMGV-T3 施工笔落链后派出；本票不预写 T3 挂载句、不触碰 SEMGV-T3 写集，两案条款互不污染。
3. **开工复点**：施工开工读数须复点五张 agent 卡现态（行数／字节／sha256 前 12）与 §5 各判据的现值钉；**一切行号锚按内容锚定位、不锁死行号**；一切数值钉（qa 两包现值、ls-files 终值、历史文内归因基数、门禁参考读数、mv 计数）**以施工开工复点为准、不锁死本数**，R 行计数按「复点两桶之和＋adr 4＋票族 3＋散件 20」公式对钉。
4. **射程边界**：本分票为纯规格件，起草落盘阶段不 mv 目录、不改 config／席位卡／规范一字、不补链 ledger、不删 tmp、不 bump 版本、不建目录、不跑装配。工具归属／shareds 自包含议题不入本批射程。
5. **历史案卷口径**：新名生效点起按新名落；旧文不追改。四件套处置＝① 件位按 §3 B 组逐件 `git mv` 全量归位；② 历史文内旧路径字面按 append-only 史实锚照登，不改一字；③ 去歧义由两份 README 各加一行承担（§2 A5）；④ 增量面由 §3 B7 过渡期向前进纪律封口。

## §2 A 组：配置与规范成文（逐件行级，替换文本逐字入票）

### A1 `agent-experts/baigong-software-team/config/seat-permissions.json`（十处行级替换）

1. product 行 `write_globs`：`[".collab/drafts/prd/", ".collab/product/", ".collab/drafts/proposals/"]` → `[".collab/drafts/", ".collab/product/"]`
2. product 行 `deny_globs`：删 `".collab/drafts/design/"`、`".collab/drafts/adr/"` 二项，原位并入 `".collab/adr/"` 一项（`".collab/audits/"` 已在位保留）。
3. architect 行 `write_globs`：头四段 `".collab/drafts/design/", ".collab/drafts/adr/", ".collab/architect/", ".collab/drafts/proposals/"` → `".collab/drafts/", ".collab/architect/"`；**同时删 `"docs/adr/"` 一项**（ADR 文书执笔权归 host）。其余元素（含 `"docs/STRUCTURE.md"`）一字不动。
4. qa 行 `write_globs` 尾段：`".collab/drafts/proposals/"` → `".collab/drafts/"`（`.collab/audits/` 已在位不动）。
5. qa 行 `deny_globs`：删 `".collab/drafts/prd/"`、`".collab/drafts/design/"`、`".collab/drafts/adr/"` 三项 → 并入一项 `".collab/adr/"`（会签意见落各席既有写域＝零新开写域；`adr/` 对 product/qa 维持 deny）。
6. engineer 行 `write_globs` 尾段：`".collab/drafts/deploy/"` → `".collab/drafts/"`。
7. engineer 行 `deny_globs`：`".collab/qa/**"` → `".collab/audits/**"`（恰一处）。
8. engineer 行 **`deny_globs_note`（实在 `:59`；`:54` 的 `write_globs_note` 内无 drafts 字样）** 同句三处随动：① `".collab/drafts/deploy/"` 字样 → `".collab/drafts/"`；② 「十一桶闭集内 board/decisions/design/dispatch/evidence/process/**qa**/receipts/research/refs」段 → 「十七桶闭集内 board/decisions/design/dispatch/evidence/process/**audits**/receipts/research/refs」（桶名换代＋计数换代）；③ 本行另 1 处「十一桶闭集」（首句先决真源指针）→「十七桶闭集」。注记其余语义一字不动（让出父桶对表句、双兜底句、design 桶维持格句照旧）。
9. 顶层 `table_notes.枚举款六类`（`:7`）：「（B1-D·十一桶）」→「（B1-D·十七桶）」。
10. host 行：`write_globs` 尾追加两项 `".collab/adr/", "docs/adr/"`；`deny_globs` 内 `"docs/*（除转正代写通道）"` → `"docs/*（除转正代写通道与docs/adr/）"`（终写面开口显式化，与 write_globs 行同源）。

**纵深减层如实申报（机械后果，照登不改判）**：drafts 子包废止后四个配置行 `write_globs` 同含 `.collab/drafts/`＝drafts 成共写域，席位互防从路径粒度降为租约粒度（当票租约 path_globs 点名具体文件＋声明闭集对账＋纯净核验承载）；deny 面对 drafts 不再可枚举子路径。adr 面换代后防护改移＝`adr/` 单桶归 host 写域＋其余席位 deny／非授权双兜底（签发面写域子集校验＋写侧『路径∉当席租约』）。

### A2 `agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json`（与 A1 同源派生·同批同值）

- product／qa／engineer 三行 `deny_globs` 改动＝A1 对应行**逐字同值**（两文件五席数组全等约束）。
- host 行 `deny_globs`：`"docs/*（除转正代写通道）"` 同值替换为 A1 第 10 处新值（两文件 host 行同源对账）。
- engineer 行 `deny_globs_note`（`:29`，同源缩略版）：「十一桶闭集」→「十七桶闭集」一处。
- architect 行零动（deny 面本无 adr 条目）。

### A3 五张 agent 卡＋lead 卡（逐行，现值→新值）

文件均在 `agent-experts/baigong-software-team/agents/`。**本节一切行号锚按内容锚定位、不锁死行号**：下述 `:NN` 仅为现值辅助定位，施工按「现值串」逐字匹配定位，行号漂移不改射程；architect 卡三行按内容锚＝写域行／明确不可写行／可写内容行区分，不依赖行号次序或标号。

- `software-team-product.md` 写域行：现值 → `- 写域：\`.collab/drafts/\`、\`.collab/product/\``
- `software-team-architect.md` 写域行：现值（含 `.collab/drafts/{design,adr}/`、`docs/adr/` ADR 落盘写权尾段）→ `- 写域：\`.collab/drafts/\`、\`.collab/architect/\`、\`.collab/tickets/\` 票面文档（起草与按修票权修订）、开发票四字段、\`tests/\` 共写（增删改走 C1）、租约段签注与灰度判据（票内）`（adr 两面写权句全删）。
- `software-team-architect.md` 明确不可写行：现值含「**写域行已授权之 `docs/adr/` 除外**——其防护＝…」例外子句 → `- 明确不可写：\`docs/\`（三件套及 STRUCTURE 等 docs 子面）、\`.archive/\`、代码域、\`.collab/\` 未授权子域、\`audits/\``（例外子句随写权撤销而删；`docs/adr/` 防护移交 host 租约面＝A1 第 10 处）。
- `software-team-architect.md` 可写内容行：`- 可写内容：设计、ADR、开发票、边界约束` → `- 可写内容：设计、开发票、边界约束`。
- `software-team-qa.md` 写域行：尾段 `\`.collab/drafts/proposals/\`` → `\`.collab/drafts/\``（余一字不动；该行 `\`.collab/audits/\`` 经 B 组迁移由悬空变实存）。
- `software-team-engineer.md` 写域行：`\`.collab/drafts/deploy/\`` → `\`.collab/drafts/\``（余一字不动）。
- `software-team-lead.md` 席位派发路由行：现值单行 `| 系统设计、ADR、开发票、边界约束 | software-team-architect |` → 拆两行：`| 系统设计、开发票、边界约束 | software-team-architect |`＋`| ADR 文书（起草与 docs/adr 落盘＝主理人自写，不派发） | software-team-lead（本席） |`（卡行数 77→78 登记）。

### A4 规范真源 `agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md`

- `:10` 桶名闭集行：`decisions/ qa/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/`＋README 索引件 → **`decisions/ audits/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/ drafts/ adr/ architect/ product/ ledger/ returns/`＋README 索引件**（**17 桶**；`returns/` 为在用实体桶补录，仓根＋包内 tracked 实体各 2 件已钉证）。并新增一行 `drafts/` 顶层条款（逐字）：「`drafts/` 顶层直接落交接件草稿、无分子包；唯一例外子包＝`drafts/archive/`（过期版本归档）；每交接件在 drafts 顶层只存一件存活态最新版」。
- `:16` 入库面行：`qa`→`audits`，并补 `drafts/`、`adr/`、`architect/`、`product/`、`ledger/`、`returns/` 入入库面（`ledger` 补链＝账本三文件入链后入名录；`returns` 在用面本已入库＝名录补全非新开）。
- 依据注记段 append 两行（逐字）：①「六目录＝需求最终确认前阶段标准界定；桶闭集换代 11→17＝结构落改＋returns 补录」；②「adr 单立之业界实践锚＝Michael Nygard《Documenting Architecture Decisions》(2016)：ADR 记录难以逆转的架构决策，其 Consequences 常直接驱动或否定产品需求（取证口径＝人类工程实践通例优先）」。
- **住址成文行 append 一行（逐字，不得改写）**：
  > 票面与临时工作物的唯一落点＝所属项目仓根（项目根＝含 `docs/STRUCTURE.md` 之探针锚目录）下的 `.scratch/<票号>/`；本仓百工项目锚＝`agent-experts/baigong-software-team/docs/STRUCTURE.md`；现行体例目录名 `.scratch/tickets/` 入表，规格名 `tickets/` 不再使用。

  规范表据此承认现行 `.scratch/tickets/` 体例，规格名 `tickets/` 作废。

### A5 README 成文两件

- **新建仓根 `.collab/README.md`**：内容＝桶总表（六标准目录逐行「目录·放什么·谁法定写」，adr 行法定写席＝主理人；逐行名录以本票 §2 A4 的 17 桶闭集行与 `config/seat-permissions.json` 各席 `write_globs` 为据就地成文）＋表头注「六目录＝需求最终确认前阶段的标准界定，非全生命周期闭集」＋未列子包存续条款＋17 桶名录行（与 §2 A4 新 17 桶闭集**逐字同值**）＋仓根性质注：仓根 `.collab/`＝本仓治理史面，无席位写权机检（seat-permissions 只辖软开团包内席位），落件按惯例＋decisions 归口。
- **包内 `agent-experts/baigong-software-team/.collab/README.md`**：桶名录行改与 A4 新 17 桶闭集**逐字同值**；「十一桶」字样随动清零；入库／排除两制行随动；首行「现行在途案卷暂在仓根」注保留（事实态）。
- **两份 README 各加一行去歧义句（逐字，仓根 README 新建时随带、包内 README 追加）**：
  > 历史案卷内 .collab/qa/ 字样＝改名前旧路径，读作 .collab/audits/

- **两份 README 桶名录段各 append 住址成文行一行（逐字，与 A4 全等）**：
  > 票面与临时工作物的唯一落点＝所属项目仓根（项目根＝含 `docs/STRUCTURE.md` 之探针锚目录）下的 `.scratch/<票号>/`；本仓百工项目锚＝`agent-experts/baigong-software-team/docs/STRUCTURE.md`；现行体例目录名 `.scratch/tickets/` 入表，规格名 `tickets/` 不再使用。

### A6 `.gitignore` 注释随动（行为零变款）

- `:13` 注释行 `qa` → `audits` 一处；正文排除面无 qa 字样＝零行为改动。回执附 `git check-ignore -v` 前后同值读数对拍：`agent-experts/baigong-software-team/.collab/audits/x.md` 两态均不 ignore（开工基线实测 exit 1 在册）。

### A7 `agent-experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md` ADR 工序真源 `:50` 节第 1-4 款重写（第 5-6 款一字不动）

1. **链序（换代）**：任意席位可发起（会签＝讨论流程同构）→主理人誊录登记（`.collab/decisions/`·append-only·逐字）→相关席位会签＝**状态闸**（收口＝通过判定）→收口草案落 `.collab/adr/`（过程面＝drafts 治理成员：**一题一文档、禁一题多版本存活**，过期版本入归档子包）→呈报人类知悉／授权放行（**涉产品设计层＝必须人类授权放行；不涉＝会签收口可自决**）→**主理人统一起草形成执行交接的正式 ADR 件落 `docs/adr/`**（编号四位·Status 闭集·头块五行）。
2. **会签语义（换代）**：会签＝对收口草案的签署认可；会签席可出保留项——保留项未闭合前正式件起草段禁启动（收口未成）。保留项闭合归位不变：经主理人呈人类裁定，裁定落 decisions 后草案修订＝**主理人照新裁定登记件重誊草案**（誊聚权不含裁量、执笔权归主理人；落位 `.collab/adr/`＝零新开写域）；会签席永不改草案（deny 语义不变）。**会签补件合法落点＝各席既有写域**（product→`.collab/product/`、qa→`.collab/audits/`、architect→`.collab/architect/` 或当票票面）＝零新开写域，`.collab/adr/**` 对 product/qa 维持 deny。重誊后全链重走会签（同序同判据），旧会签随重誊作废不入账本终态。
3. **正式件段＝条款甲语义承（执笔席换代）**：正式 ADR 件＝主理人逐字照录四方会签收口草案，零文风裁量——终写件与收口草案正文哈希对等方可落 `docs/adr/`；主理人职责＝执笔＋落盘担责。会签签署＝账本签字记录（经 state-transition.py 既有通道）。
4. **条款乙（承）**：ADR 记的是多方已收敛决策，非主理人单方草案；主理人组织会签又执笔终写不构成自审——记录链≠正文链，防自审条款（转正代写通道）辖架构正文链（docs/ARCHITECTURE.md 族），两条路各自成文互不管辖。
- 旧字样 `架构席终写` 在本节第 1-4 款清零（判据 8 钉）；decisions 登记件本体＝append-only 史实锚不改，其「被改写」效力由本节换代承接（后生效覆盖先前）。
- 写权射程申报：本件属随包技能域；`standard-sop.md` 不在并案维护票声明闭集内，两写集零交叠。

## §3 B 组：目录实体（迁移与补链，与 A 组同批一 commit）

- **B1 audits 改名两处（逐件 `git mv`·禁目录级 mv）**：
  - **包内笔**：目标桶 `agent-experts/baigong-software-team/.collab/audits/` **已存在且非空**（开工复点现值以施工开工复点为准、不锁死本数；现盘 6 件＝向前进纪律落件的既有复核／裁定类件，照登不碰，名实对齐后并存）。**禁目录级 `git mv agent-experts/baigong-software-team/.collab/qa agent-experts/baigong-software-team/.collab/audits`**（目标桶非空时 git 语义＝把源目录移入目标成为 `audits/qa/` 子目录，产生嵌套）；一律**逐文件** `git mv <旧路径>/<文件名> <新路径>/<同名>` 平级迁入，逐件 R100、blob sha 零变。源桶 `agent-experts/baigong-software-team/.collab/qa/` 现值 tracked 234 件（登记钉 233＋复核件落链随增 +1 照登），以施工开工复点现值为准、不锁死本数。
  - **仓根笔**：目标桶 `D:\multi-agent-collab-devkits\.collab\audits\` 开工复点现值 **0 件**、目录未立（目录级 `git mv .collab/qa .collab/audits` 平级改名本正确）；为与包内共用 R100 计数公式及防嵌套断言，本面亦一律**逐文件** `git mv`，逐件 R100、blob sha 零变。源桶 `D:\multi-agent-collab-devkits\.collab\qa\` 现值 tracked 10 件，以施工开工复点现值为准、不锁死本数。
  - **反向机械断言（判据 4 随附）**：`git ls-files "agent-experts/baigong-software-team/.collab/audits/" | grep -c "/qa/"` ＝ **0**；仓根同式 `git ls-files ".collab/audits/" | grep -c "/qa/"` ＝ **0**（两式现值均 0 实测）。若任一式非 0＝发生目录级嵌套，判 FAIL 并停手。
  - R 行计数按「复点两桶之和＋adr 4＋票族 3＋散件 20」公式对钉，不锁死本数（逐件 mv 展开后的 R 行数与目录级 mv 相同，公式不变）。
  - 其余两包 qa 面＝**不并入本批迁移，维持默认射程不动**；两包 qa 现值以施工开工复点为准、不锁死本数（现盘 fuxi 48＋EAC 2＝50；登记基线 46＋2 系史实登记值、非实质意图）。新名生效点起按新名、旧文不追改。
- **B2 adr 单立＋四件迁入**：包内 `.collab/drafts/adr/` 四 tracked 件 `git mv` → 包内 `.collab/adr/`（drafts/adr 子包目录随 mv 清空消失）；仓根 `.collab/adr/` 本批不建空目录。**历史态照登行（一题一文档前向条款）**：0001 题 draft／final＋两份会签件四件并存＝旧工序历史事实，append-only 不并删不追改；「一题一文档、禁一题多版本存活」自新名生效点起对 `.collab/adr/` 过程面前向适用（在途题唯一存活文档，换版走归档子包）。
- **B3 ledger 补链**：`git add` 恰三 untracked 文件＝`.collab/ledger/ledger.jsonl`、`agent-experts/baigong-software-team/.collab/ledger/leases.jsonl`、`agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl`，入账即链态＝记账面脱链异常消除。
- **B4 architect 补建（包内）**：`mkdir` 包内 `.collab/architect/`＋落一件 5 行内索引占位 README（桶用途一句话＋「实体随首件架构过程件落位」）——空目录不入 git，占位件＝机械断言 `git ls-files` ≥1 可验。**仓根六子集从简**：仓根＝治理史面无写权机检，本批只落有实物对象者（audits mv＋ledger 链＋README），drafts／architect 空仓不建，首件届时自然落位（空目录不入链＝断言不可验）。
- **B5 drafts 顶层化＋归档子包**：归档子包落位＝**`drafts/archive/`（包内 `agent-experts/baigong-software-team/.collab/drafts/archive/`）**，**不复用仓根 `.collab/archive/`**。三条理由：①归档对象与 drafts 同域同主（起草席换版＝旧版 mv 进 `drafts/archive/`＋新版落顶层，一次租约闭环，无需跨席搬件）；②`drafts/archive/` 天然被 `write_globs` 行 `.collab/drafts/` 前缀命中（lease-issuer `:130` startswith 校验语义），零新增配置行；③与仓根 `.collab/archive/`（退役定稿落位）语义分域不混。现 drafts 顶层零散件＝无需存量归位动作；条款为前向纪律。**ADR 面同规**：`.collab/adr/` 在途交接件一题一文档，过期版本去向随 drafts 治理同则（届时若需机检行，随批 config 随动另笔，本票不预开）。
- **B6 tests 三件样例随动**：`drill-05-freeze-recover.sh` `:22/:27/:49` 三处 `.collab/drafts/prd/tmp-drill05.md` → `.collab/drafts/tmp-drill05.md`（`:17` 注释行 `drafts/prd` 字样随改）；`drill-06-replay-reconcile.sh` `:20` 同款一处；`test_lease_instantiation.py` `:95/:96` 两处 `.collab/drafts/prd/` → `.collab/drafts/`。
- **B7 过渡期向前进纪律**：自本票放行起至 B 组迁移收口，**一切新增记账／审票／复核／登记类件直接落目标名桶**（`audits/` 等法定新名桶，不存在则先建后落；仓根与包内两面同规）——**存量迁移归 B1 逐件 `git mv`，新增面禁落旧名桶**（`qa/` 等）。过渡期每笔后向落旧桶会令迁移射程持续增大；本条款封住增量面，B1 mv 计数公式承担残余窗口漂移。条款效力＝前向纪律（放行即生效，先于 B 组施工收口），与历史案卷存量射程正交。
- **B8 票族三件随批 mv 归位 bundle 项目根**：工序真源＝`skills/software-orchestration/references/dev-discipline.md:83`「唯一落点＝所属项目仓根（项目根＝含 docs/STRUCTURE.md 之探针锚目录）`.scratch/<票号>/`」——百工项目锚＝`agent-experts/baigong-software-team/docs/STRUCTURE.md`（在位实存），历史票全住 bundle `agent-experts/baigong-software-team/.scratch/tickets/`（体例实证）。三件现落仓根 `.scratch/tickets/`＝落点违规，随批 `git mv` 归位：仓根 `.scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v1.md`／`…-v2.md`／`…COLLAB-STRUCT-B345-工序纪律并案维护票-v1.md` 三件 → `agent-experts/baigong-software-team/.scratch/tickets/` 同名（三件均 tracked，R 行随 §5 判据 4 计数公式另加 3）。**落位条款按 dev-discipline:83 成文承（票面＋临时工作物同规）**：本票族自归位后，后续一切本工序族票面／回执／临时工作物按 :83 落 bundle 项目根 `.scratch/` 面。
- **B9 仓根 `.collab\` 根面 tracked 散件 20 件归位＋删除 tmp 临时件**：
  - `D:\multi-agent-collab-devkits\.collab\` 根面 tracked 散件恰 20 件（逐件清单＝本票 §4 声明闭集所列的 20 行旧路径），与 `D:\multi-agent-collab-devkits\.collab\decisions\` 现有件**零同名冲突**（`comm -12` 实测空）→ 20 件**全量逐件 `git mv` 同名归位** `D:\multi-agent-collab-devkits\.collab\decisions\`，**R100 保真**（逐件旧路径＝`.collab/<文件名>`，新路径＝`.collab/decisions/<同名>`）。
  - 删除 `D:\multi-agent-collab-devkits\.collab\tmp-w7-msg.txt`（untracked，已被 `.gitignore:36 /.collab/tmp-*.txt` 忽略）。**删除前留痕（实测钉）＝23 行／2,270B／sha256 `037a83b30b08741c9bf476496284ce7357b5f164388f4f1a697e5627a9a50056`，须逐字写入施工回执**；施工时先复算该三值，与钉不符即停手呈报，不自行改钉。
  - 本条为本批执行对象，不属禁动面（§6 已相应改判）。

## §4 声明闭集（机检源·逐行完整路径）

配置／席位卡／规范／README／.gitignore／tests 面：

- agent-experts/baigong-software-team/config/seat-permissions.json
- agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json
- agent-experts/baigong-software-team/agents/software-team-product.md
- agent-experts/baigong-software-team/agents/software-team-architect.md
- agent-experts/baigong-software-team/agents/software-team-qa.md
- agent-experts/baigong-software-team/agents/software-team-engineer.md
- agent-experts/baigong-software-team/agents/software-team-lead.md
- agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md
- agent-experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md
- agent-experts/baigong-software-team/.collab/README.md
- .collab/README.md（新建）
- .gitignore
- agent-experts/baigong-software-team/tests/acceptance/drills/drill-05-freeze-recover.sh
- agent-experts/baigong-software-team/tests/acceptance/drills/drill-06-replay-reconcile.sh
- agent-experts/baigong-software-team/tests/s2/test_lease_instantiation.py

20 件治理史散件 **旧路径（mv 源）**：

- .collab/2026-11-03-SWB-B3-收口登记-v1.md
- .collab/2026-11-04-SWB-ADR审票链-主理人串行违例登记-v1.md
- .collab/2026-11-04-SWB-ADR工序票-呈拍简报-v1.md
- .collab/2026-11-04-SWB-ADR工序票-收口登记-v1.md
- .collab/2026-11-04-SWB-ADR调研双件-互相吞笔事故登记-v1.md
- .collab/2026-11-04-SWB-B4-收口登记-v1.md
- .collab/2026-11-04-SWB-B5-收口登记-v1.md
- .collab/2026-11-04-SWB-B批总收口登记-v1.md
- .collab/2026-11-04-SWB-CD1-收口登记-v1.md
- .collab/2026-11-04-SWB-ES2-收口登记-v1.md
- .collab/2026-11-04-SWB-RET-事故登记-v1.md
- .collab/2026-11-04-SWB-RET-收口登记-v1.md
- .collab/2026-11-05-ADR-L0-收口登记-v1.md
- .collab/2026-11-05-STRUCT-FIX-收口登记-v1.md
- .collab/2026-11-05-TMP-DISC-收口登记-v1.md
- .collab/2026-11-05-主理人候拍面清点更正登记-v1.md
- .collab/2026-11-06-PROJINIT-final-放行呈拍与H8待裁-v1.md
- .collab/2026-11-06-PROJINIT-放行呈拍与四条待裁-v1.md
- .collab/2026-11-07-FUXI-miyazaki入池闸与快照两态-呈拍简报-v1.md
- .collab/2026-11-08-百工团队层问题复盘清单-v1.md

20 件治理史散件 **新路径（mv 目标）**：

- .collab/decisions/2026-11-03-SWB-B3-收口登记-v1.md
- .collab/decisions/2026-11-04-SWB-ADR审票链-主理人串行违例登记-v1.md
- .collab/decisions/2026-11-04-SWB-ADR工序票-呈拍简报-v1.md
- .collab/decisions/2026-11-04-SWB-ADR工序票-收口登记-v1.md
- .collab/decisions/2026-11-04-SWB-ADR调研双件-互相吞笔事故登记-v1.md
- .collab/decisions/2026-11-04-SWB-B4-收口登记-v1.md
- .collab/decisions/2026-11-04-SWB-B5-收口登记-v1.md
- .collab/decisions/2026-11-04-SWB-B批总收口登记-v1.md
- .collab/decisions/2026-11-04-SWB-CD1-收口登记-v1.md
- .collab/decisions/2026-11-04-SWB-ES2-收口登记-v1.md
- .collab/decisions/2026-11-04-SWB-RET-事故登记-v1.md
- .collab/decisions/2026-11-04-SWB-RET-收口登记-v1.md
- .collab/decisions/2026-11-05-ADR-L0-收口登记-v1.md
- .collab/decisions/2026-11-05-STRUCT-FIX-收口登记-v1.md
- .collab/decisions/2026-11-05-TMP-DISC-收口登记-v1.md
- .collab/decisions/2026-11-05-主理人候拍面清点更正登记-v1.md
- .collab/decisions/2026-11-06-PROJINIT-final-放行呈拍与H8待裁-v1.md
- .collab/decisions/2026-11-06-PROJINIT-放行呈拍与四条待裁-v1.md
- .collab/decisions/2026-11-07-FUXI-miyazaki入池闸与快照两态-呈拍简报-v1.md
- .collab/decisions/2026-11-08-百工团队层问题复盘清单-v1.md

票族三件随批 mv 的旧／新路径：

- .scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v1.md〔mv 源〕
- .scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v2.md〔mv 源〕
- .scratch/tickets/2026-11-08-COLLAB-STRUCT-B345-工序纪律并案维护票-v1.md〔mv 源〕
- agent-experts/baigong-software-team/.scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v1.md〔mv 目标〕
- agent-experts/baigong-software-team/.scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v2.md〔mv 目标〕
- agent-experts/baigong-software-team/.scratch/tickets/2026-11-08-COLLAB-STRUCT-B345-工序纪律并案维护票-v1.md〔mv 目标〕

- **mv 面计数公式**：`git show --name-status` 的 R 行＝复点两桶和＋4（adr 四件迁入）＋3（票族三件归位）＋20（治理史散件归位），**全部 R100**；逐件新路径＝旧路径同名改，回执附全量 R 行计数对钉。目标桶既有件（包内 `.collab/audits/` 开工复点现值 6 件、仓根 `.collab/audits/` 0 件）照登不碰、不计入 R 行数，名实对齐后与迁入件并存。
- **add 面 5 件**：`.collab/ledger/ledger.jsonl`、`agent-experts/baigong-software-team/.collab/ledger/leases.jsonl`、`agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl`、新建 `.collab/README.md`、占位 `agent-experts/baigong-software-team/.collab/architect/README.md`。
- **delete 面 1 件（untracked·不入 commit）**：`.collab/tmp-w7-msg.txt`，留痕见 §3 B9。

## §5 九条机械可验判据（施工回执必附逐条实测）

1. **JSON 合法＋同源全等**：两 config `python -m json.tool` exit 0；两文件五席 `deny_globs` 数组逐席全等（同源派生约束；host 行随 A1 第 10 处／A2 同步改后仍逐席全等）。**门禁对拍形制**：run-gates 计数一律**同形态两读数对拍**（主盘对主盘、worktree 对 worktree），**禁跨形态比数**（worktree 形态与主盘差一量级＝形制差非盘面差）。
2. **grep 钉值（现值→新值 0）**：`git grep -c "drafts/prd\|drafts/design\|drafts/adr\|drafts/proposals\|drafts/deploy" -- agent-experts/baigong-software-team/config agent-experts/baigong-software-team/agents agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md` ＝ **0**（现值基线＝**13 行**）；`git grep -c "collab/qa" -- "agent-experts/baigong-software-team/config"` ＝ 0；「十一桶」在用面清零（点名四处逐锚复跑）：`git grep -c "十一桶" -- agent-experts/baigong-software-team/config agent-experts/baigong-software-team/.collab/README.md` ＝ **0**（现值＝5 occurrence／4 行；历史案卷＋六外包面不在射程，禁动面登记）。
3. **ls-files 断言（终值公式钉）**：`git ls-files | grep -c "/\.collab/qa/\|\.collab/qa/"` **施工后终值＝施工开工复点两包 qa 现值之和**（＝`git ls-files "agent-skills/fuxi-skill/.collab/qa/" | wc -l` ＋ `git ls-files "agent-skills/external-advisor-collab/.collab/qa/" | wc -l`；现盘复点＝48＋2＝**50** 照登，**非 FAIL**；两包不并入本批迁移，终值以施工开工复点为准、不锁死常数；登记基线 `48` 系史实登记值、非实质意图）。**机械验收形制**：施工回执附「施工后该 grep 读数」与「开工复点两包 `wc -l` 之和」两读数，相等即 PASS（差值 0 可机检）；**禁与常数 48 直接比数**。其余钉值：`.collab/audits/` tracked **迁入件数**＝复点两桶和（目标桶开工复点既有件照登不碰、并存另计）；`.collab/adr/` tracked＝4；`.collab/architect/` tracked≥1；ledger 三文件 tracked 态；仓根 `.collab/` 根面 tracked 散件＝0（20 件全量归位 `decisions/`）；`.collab/decisions/` 直系 tracked＝现值 56＋20＝76（以施工开工复点为准）。
4. **mv 保真＋防嵌套**：`git show --name-status` 的 R 行＝复点两桶和＋4＋票族 3＋归位散件 20，**全 R100**（内容零变·`-M` 检测）；两处 audits 改名一律逐文件平级 mv（禁目录级）；抽验四件 adr 新旧 blob sha 全等（`git cat-file blob` 双点对拍）；20 件归位逐件 R100 与「复点两桶和＋4＋票族 3」累加对钉。**防嵌套机械断言**：`git ls-files "agent-experts/baigong-software-team/.collab/audits/" | grep -c "/qa/"` ＝ **0**、`git ls-files ".collab/audits/" | grep -c "/qa/"` ＝ **0**（两式现值均 0 实测）；若任一式非 0＝发生目录级 `audits/qa/` 嵌套，判 FAIL 并停手。
5. **门禁零回归对拍**：基线＝施工开工主盘实跑（开工时点登记；参考读数＝`GATE PASS exit 0／发现 N`，N 随盘波动、以施工开工复点为准、不锁死本数）。判据＝**GATE PASS 不翻红**＋前后两读数**同形态**（主盘对主盘、worktree 对 worktree，禁跨形态比数）＋**差值非零合法**：差值按窄口径（GATE PASS 行「发现 N 条」单一真源）**每条新增悬空命中须逐条归因于旧文 `.collab/qa/`／`drafts/adr` 字面存量**；归因基数＝`git grep` 现值、**以施工开工复点为准、不锁死本数**（现盘 `git grep -l "\.collab/qa/" -- '*.md'`＝218 文件／`git grep "\.collab/qa/" -- '*.md' | wc -l`＝355 行／`drafts/adr`＝72 行，随盘漂移照登；旧登记 209 文件／308 行／46 行系同族史实基线值）；**禁「基本通过」式糊账**；迁移后历史文内旧路径引用转悬空（旧文不追改），check-pointers 类命中必增，差值非零不构成翻红。
6. **drill／s2 差值口径**：开工基线两读数照登＝`drill-05` exit **1**／`drill-06` exit **1**（既有缺陷：write-guard deny 输出 ensure_ascii 转义 vs 夹具中文明文／夹具引用目标缺件，缺陷台账 `.collab/defects/2026-11-08-drill夹具回读编码失配与缺件引用缺陷-v1.md` 在册，修路另案处理＝禁动面锁死）。**调用形制一行钉**：drill 两件基线与复跑一律用 **`T06_TMP` 注入形制**（drill-05 `:10` `T06_TMP:?` 契约＝仓外 Temp 由调用方注入，`T06_TMP=<仓外Temp目录> bash drill-05…`）——裸跑 exit 1 同值不同因（变量未设即中止，非夹具红因），读数只在注入形制下有效。验收＝改差值口径：三件随 B6 改后复跑（注入形制），drill 两笔仍 exit 1 且**红因读数与基线同型**（缺陷面不因本票恶化）＝PASS；`python agent-experts/baigong-software-team/tests/s2/test_lease_instantiation.py` exit **0** 不变（夹具租约路径随 B6 自洽）。
7. **check-adr 命令形制一行级钉死**：验收命令＝`python agent-skills/object-audit/scripts/check-adr.py --bundle-root agent-experts/baigong-software-team`，钉 exit **0**／`docs/adr 盘上件=1｜桶1=1 桶2=20 桶3=1`（本票不动 `docs/adr/` 一字，复跑读数同值）。裸跑 exit **4**（infra error）＝非用态，不入判据（形制在册防复现误读）。锚面措辞按实：check-adr 主锚＝`docs/adr/`＋另锚两面＝①`.collab/decisions/`（ADR_DECISIONS_SUBDIR，三面对账 diff 面）②adr 件内 `.collab/…` 案卷活引用补偿断言（WATCH advisory 正则）——三面均不落本票 mv 射程（`docs/adr/` 禁动、`decisions/` 只进不迁、advisory 引用面＝历史文内字面照登不随动）＝**零随动结论不变**。
8. **ADR 随动面 grep 钉值**：`git grep -c "架构席终写" -- agent-experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md` ＝ **0**（现值 1）；`git grep -c "docs/adr" -- agent-experts/baigong-software-team/agents/software-team-architect.md` ＝ **0**（**现值 2**＝写域行＋明确不可写行各 1；可写内容行不含该字面；**按内容锚定位、不锁死行号**，现值以施工开工复点为准）；architect 卡「可写内容」行不含「ADR」＝`git grep -c "可写内容：设计、ADR" -- …architect.md` 现值 1→**0**；lead 卡 `ADR … software-team-architect` 路由行现值 1→**0**（新行含「ADR 文书…software-team-lead（本席）」命中 1）；`seat-permissions.json` host 行含 `".collab/adr/", "docs/adr/"`＝命中 1、architect 行含 `"docs/adr/"`＝**0**。
9. **过渡期向前进＋票面落位核对**：
   - **落位核对（票族专名口径）**：施工后 `git ls-files ".scratch/tickets/" | grep -c "COLLAB-STRUCT"` ＝ **0**（现值 3）；`git -c core.quotepath=false ls-files "agent-experts/baigong-software-team/.scratch/tickets/" | grep -cE "COLLAB-STRUCT-1-结构名实对齐与规范成文票|COLLAB-STRUCT-B345-工序纪律并案维护票"` ＝ **3**（现值 **0**）——三件票族归位 bundle 项目根 `.scratch/tickets/`＝dev-discipline `:83` 唯一落点复现；**票族专名过滤排除本工序族施工分票（v1 链上件与本件 v1.1）及一切回执件**（其名含 `COLLAB-STRUCT` 但不含票族专名），故现值 0／施工后 3 对自指计数免疫；调用形制＝宽 grep `COLLAB-STRUCT` 仅用于仓根半式，bundle 半式一律用票族专名 `-E` 口径。mv 三件 R100 随判据 4 计数（复点两桶和＋4＋3＋20）对钉。
   - **向前进核对**：放行后至 B1 收口区间内，`git log --name-only <放行笔>..<B1收口笔> -- ".collab/qa/" "agent-experts/baigong-software-team/.collab/qa/"` 命中新增件（A 状态）＝**0**（该区间一切新增记账／审票／复核／登记类件一律落 `audits/` 目标名桶）；若区间内出现 qa/ 旧桶 A 笔＝违例照登并 B1 前整改（mv 进桶后计 R），B1 mv 计数公式随之承「开工复点」吸收窗口漂移。

## §6 禁动面闭集（点名）

- `docs/adr/`（终写位不动；写权变更只落配置面，盘上件零动）；`docs/**` 全部；`.archive/**`。
- 历史案卷**内文**一切旧路径引用与旧字样＝**新名生效点起按新名、旧文不追改，append-only 不回改**；归因基数（`.collab/qa/`／`drafts/adr`／「十一桶」字面存量）**以施工开工复点现值为准、不锁死本数**（现盘 218 文件／355 行／72 行／81 occurrence；旧登记 209 文件／308 行／46 行／15 行系同族史实基线值、漂移照登）。
- `agent-skills/fuxi-skill/.collab/qa/`、`agent-skills/external-advisor-collab/.collab/qa/` 两包 qa 存量＝**不并入本批迁移，维持默认射程不动**；两包 qa 现值以施工开工复点为准、不锁死本数（现盘 fuxi 48＋EAC 2＝50；登记基线 46＋2 系史实登记值、非实质意图）。
- 六外包 `.collab/README.md`（bundle-assembly-registration／external-advisor-collab／fuxi-skill／multi-collab／object-audit／object-build 各 1 处「十一桶」）＝跨包面本批不动（在用面随动只点名 baigong 在用四锚）。
- `.collab/defects/` 台账本体（drill 缺陷登记件）＝只读引用，本批不动。
- `run-gates.sh`／各 `check-*.py`／`write-guard.py`／`lease-issuer.py`／`publish.py` 等门禁与机件本体＝本批零触碰（本批改其消费的配置面，不改机件）。
- 三同源版本号（`plugin.json`／`bundle.lock`／`.codebuddy-plugin/plugin.json` 现均 `0.1.30`）＝**本批零 bump**；升号并入 PROJINIT 合并批＋SEMGV 系列放行后的合并升号窗口。
- SEMGV-T3 案写集（五卡各一行的 T3 挂载句／`bundle.lock`／注册面 `plugin.json`／`sop SKILL.md`／`claim-commitment-governance` 七件）＝本批零触碰、不预写 T3 挂载句；施工序＝先 SEMGV-T3 后 COLLAB-STRUCT-1，两案条款互不污染。
- `standard-sop.md` ADR 工序节**第 5-6 款**（supersede 归道／立项触发判据）＝本批零动。
- 工具归属／shareds 自包含议题＝不入本批射程，严禁塞入。
- `skills/software-orchestration/` 其余三 references 件＋`SKILL.md`＝本批零触碰（零交叠自证＝两闭集互不含）。
- **规格来源件** `D:\multi-agent-collab-devkits\.scratch\tickets\2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v2.md` 与 `D:\multi-agent-collab-devkits\.collab\decisions\2026-11-09-皮总裁定-STRUCT-v2放行与六项候裁取态.md`＝append-only 史实锚，本批零改；终值一律以施工开工复点为准、不锁死常数。**v1 链上件** `D:\multi-agent-collab-devkits\agent-experts\baigong-software-team\.scratch\tickets\2026-11-09-COLLAB-STRUCT-1-施工分票-v1.md`＝append-only 史实锚，照登不动、不再作为施工依据。
- 仓根 `.collab/` 根面 tracked 散件 20 件与 `.collab/tmp-w7-msg.txt` **不属禁动面**：两者为本批 §3 B9 处置对象（全量逐件 `git mv` 同名归位 `decisions/`、删除 tmp 并留痕）。

## §7 完工定义、施工回执与三态明示

- **完工定义**：§2 A 组与 §3 B 组**同批一个 `collab:` commit** 落账；施工回执另落 bundle 项目根 `.scratch/` 面（按 dev-discipline `:83`）。
- **施工回执必附**：commit sha；`git show --name-only`／`--name-status` 全量清单与 §4 闭集逐件对钉；§5 九条判据逐条实测读数；20 件归位逐件 R100 读数；两处 audits 改名防嵌套断言两条 `grep -c "/qa/"`＝0 实测；终值公式钉两读数相等（施工后 `ls-files grep -c` 与开工复点两包 `wc -l` 之和）；`.collab/tmp-w7-msg.txt` 删除前留痕三值（23 行／2,270B／sha256 `037a83b30b08741c9bf476496284ce7357b5f164388f4f1a697e5627a9a50056`）；`git check-ignore -v` 前后同值对拍；门禁同形态两读数；A／B 同批一 commit 自证；**净化对照表**（逐处列明本票 §2 各替换文本相对规格来源的删除串／替换串／定位串／所在行，供 QA 逐件核交付面纯净性——替换文本内不得含链笔号、出处钉、过程编号、案卷指针等治理史字样）。
- **纪律**：双侧 pathspec 限定；禁 `git add -A`／`--amend`／`reset`／`--no-verify`；他案在制品照登不碰；门禁 advisory 照常；本仓 commit 一律带 ≥7 分钟 timeout 或后台跑（pre-commit 钩子输出约 8MB，会撞前台 2 分钟超时）。
- **三态明示（逐条分开写）**：
  1. **做了但没落盘**：两规格来源全文直读、配置／席位卡／规范／夹具／tests 消费面只读实测（wc／sha／grep／mv 计数／门禁基线／drill 形制）——均仓内只读命令，仓内零临时脚本零中间文件。
  2. **落盘了但没提交**：本件写入 `agent-experts/baigong-software-team/.scratch/tickets/` 后至 `git add` 前为工作区改动态。
  3. **提交了但没对账**：commit 后至完工回报给出「status 他案照登＋`git show --name-only` 恰本件」实测前此态存在；由完工回报补齐，不预标「已完成」。
- **本件 commit sha 与提交后态**由完工回报实测给出，正文不预写自指值。

---

## 租约段（架构签注 · 由 B2 实例化）

```
lease:
  ticket: COLLAB-STRUCT-1-施工分票-v1.1
  seat: architect
  countersign: "architect: 租约段签注（唯一生产权）由 B2 实例化"
  path_globs:
    - agent-experts/baigong-software-team/.scratch/tickets/2026-11-09-COLLAB-STRUCT-1-施工分票-v1.1.md
  deny_globs:
    - docs/**
    - .archive/**
    - agent-skills/**
    - agent-experts/baigong-software-team/.collab/**
    - softwares/**
    - tests/**
    - "*.py"
  note: 本件只出 COLLAB-STRUCT-1 施工执行规格分票 v1.1 一件（同题唯一施工依据·逐字自包含成文·纯规格零施工）；v1 链上件照登不动（append-only 史实锚）。A 组成文与 B 组迁移同批一 commit 为后续施工执行规格，本件起草阶段不 mv 目录、不改 config／席位卡／规范一字、不补链 ledger、不建目录、不删 tmp、不 bump 版本、不预写 T3 挂载句、不跑装配。deny 面已由 `agent-experts/**` 收窄为 `agent-experts/baigong-software-team/.collab/**`（保治理面禁写、放开 `.scratch/tickets/` 住址，使 path_globs 不被自身 deny 覆盖）；B2 实例化时以 `lease-issuer.py` 验本件 path 可签发。依据＝施工规格票 v2（251 行／46,944B／5eeeb3a）＋STRUCT v2 放行裁定件（6c495d4，绝对路径见票头依据行）。工具归属／shareds 自包含议题不入射程。
```
