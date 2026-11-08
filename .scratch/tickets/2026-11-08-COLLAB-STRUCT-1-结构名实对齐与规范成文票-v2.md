# COLLAB-STRUCT-1 .collab 结构名实对齐与规范成文票（架构席·过程件规格票·纯规格零施工）v2

- **票号**：COLLAB-STRUCT-1｜**版本**：v2（append-only 序链 v1→v2；v1＝f5f1222dfdb9／24,590B／4e5b630 落链，本件取代其为施工依据）｜**起草席**：架构席（arch-struct1c）
- **开工读数（实测）**：`date`＝`Sun Nov 8 22:22:26 2026`（本机时钟）／HEAD＝`67a3462`（＝派工令预期钉值，对钉成立）／`git status --porcelain --untracked-files=no`＝空（tracked 面净；他案 untracked 取证面照登不碰：`.scratch/FX-U1x*`、`.collab/ledger/`〔本票射程内补链对象〕、`.collab/tmp-w7-msg.txt`〔候裁②对象〕、research 散件等）。
- **裁定真源（条款依据·已完整直读）**：
  1. `.collab/decisions/2026-11-08-皮总裁定-collab结构规范重定义与缺陷清单并案.md`＝`b8bdadc` 落链（blob 5,056B／`ea8061101341`）——结构裁定七条。
  2. `.collab/decisions/2026-11-08-皮总裁定-ADR工序写入权与drafts治理.md`＝`67a3462` 落链（blob 3,339B／`16fe47f5d145`）——**v2 追加输入**：ADR 统一主理人写／会签＝状态闸／人类闸按产品设计层分级／会签＝讨论流程任意席位可发起·主理人组织／时序＝收口→呈报人类→正式 ADR 件／ADR drafts 交接件一题一文档禁多版本存活。
- **修单来源（v2 唯一修订条款面）**：
  - `.collab/qa/2026-11-08-COLLAB-STRUCT-双席审票会师对拍与裁定-v1.md`（`agent-experts/baigong-software-team/.collab/qa/`，commit `36dfb78`，blob 5,373B／`7843fb3bf7f9`）＝红三黄七合并清单＋裁定「两票非废票级、主票出 v2、修单只是输入作者席亲笔、候裁六项继续单列不重审、红-1/红-3 钉值终态挂候裁①」。
  - 皮总 ADR 裁定件（上 2.）随动面＝其 §三 连带影响清单（seat-permissions adr 写域改判／ADR 工序真源 `b0b449d` 链改写／一题一文档细则）。
  - **修单之外零自扩射程**；工具归属/shareds 自包含议题＝另票 TOOLHOME（已径裁，不入本票）。
- **v1 双席审票基准**：A 席 `559f2a8`（红2黄5绿11）＋B 席 `93434e0`（红2黄6绿13）——已会师对拍，本票不重审只落位。
- **两笔封顶兑现**：本票＝主票第二笔（v1＋v2 恰封顶）；v2 回来后双席窄复核（改哪段复验哪段），不开新面、不再出 v3。
- **v1 处置行（ADR 裁定⑥「一题一文档、禁一题多版本存活」落笔）**：v2 落链起，同题施工依据存活态唯一＝本件 v2；v1 链上件照登不动（append-only 史实锚，PROJINIT v1/v2、SEMGV-T1 v1-v5 多版链先例同构），v1 自此**不再是施工依据**——B2 实例化、工程师施工票、双席窄复核一律指向本 v2。
- **门禁基线（本席开工时点实跑）**：`bash agent-skills/object-audit/scripts/run-gates.sh --no-write` ＝ **GATE PASS exit 0／发现 31,885**（主盘形态；较 v1 起草时点 31,875 漂移 +10＝`b8bdadc..67a3462` 区间新增链件路径型 advisory，照登；跨形态比数禁令见 §5 判据1）。

## 0 已入账裁定转录（忠实执行，不复议）

**结构裁定（`b8bdadc`）七条——同 v1 §0：**
1. drafts 分子包＝**错误定义废止**：交接件草稿直接落 `drafts/` 顶层，无子包（归档子包除外）；每交接件只留一件存活态最新版，过期版本入归档子包。
2. **adr 单立 `.collab/adr/`**（不在 architect/ 下）——条件问「adr 可否涉产品需求变更」裁定取证＝是（ADR 工序链 `b0b449d` 三方会签含产品席＋ADR-0001 产品席保留项 R-PM-1 `b2150c5`；业界锚见 A4 依据行〔黄-7〕）。交付面 `docs/adr/` 终写位不动；过程面 `drafts/adr/` 四件迁入。
3. `architect/`＝架构席非交接件写权域——规格有域无实体，须补建。
4. `audits/`＝名实对齐：实体 `qa/` 改 `audits/`（仓根＋包内），席位卡／seat-permissions.json／hooks-map 同批随动。
5. `ledger/`＝两处 untracked 补 commit 入链。
6. 未列子包（board/dispatch/evidence/inbox/process/receipts/refs/research/returns 等）存续不禁，按项目阶段取用。
7. 六目录定位＝需求最终确认前阶段的标准界定，非全生命周期闭集（目标态表头注必带该限定）。

**ADR 工序裁定（`67a3462`）六条——v2 新增：**
8. **写权改判：ADR 统一由主理人写**（推翻甲案架构席终写／乙案会签补件区两候裁＝销账）；seat-permissions 现值须随此改判重排。
9. 会签＝状态闸：相关席位会签收口＝通过判定；收口结果呈报人类（知悉/授权放行）。
10. 人类闸分级：涉产品设计层→必须人类授权放行；不涉→会签收口可自决。
11. 会签＝讨论流程（同构）：任意席位可发起；主理人组织相关席位参与讨论和会签。
12. 时序：讨论/会签→收口→呈报人类知悉/授权放行→形成执行交接的正式 ADR 件。
13. drafts 治理随大盘：讨论过程中的 ADR 交接件＝drafts 成员，与其他 drafts 同治理原则；一题一文档，禁止一题多版本存活。

## 1 现态基线钉值（v2 落笔前 67a3462 时点实测）

### 1.1 配置与规范面（逐件行数／字节／sha256 前 12）

| 件 | 现态（v2 复点，与 v1 §1.1 全等＝本区间零扰动） |
|---|---|
| `agent-experts/baigong-software-team/config/seat-permissions.json` | 73 行／8,655B／`2e92c7b97af2` |
| `agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json` | 40 行／4,003B／`0d25b6057c93` |
| `agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md` | 27 行／1,719B／`403db8e0e0f5` |
| `agent-experts/baigong-software-team/.collab/README.md` | 12 行／635B／`9e9397c74902` |
| 仓根 `.collab/README.md` | **不存在**（审计实锤） |
| `agents/software-team-product.md` | 46 行／3,227B／`a1c6a4f8ecce`（`:22` 含 `.collab/drafts/prd/`） |
| `agents/software-team-architect.md` | 47 行／3,825B／`1c51935d3ca6`（`:22` 含 `.collab/drafts/{design,adr}/`＋`docs/adr/`；`:23` 含「`docs/adr/` 除外」例外子句；`:24` 可写内容含「ADR」） |
| `agents/software-team-qa.md` | 49 行／3,848B／`0bcda097f0f7`（`:22` 含 `.collab/drafts/proposals/`；`.collab/audits/`＝悬空指空） |
| `agents/software-team-engineer.md` | 49 行／3,951B／`b4331d7422c4`（`:22` 含 `.collab/drafts/deploy/`） |
| `agents/software-team-lead.md` | 77 行／5,298B／`c2287132f1e8`（**v2 改判：非零触碰**——`:50` 席位派发路由行含「系统设计、ADR、开发票、边界约束 → software-team-architect」＝ADR 裁定随动面） |
| `skills/software-orchestration/references/standard-sop.md` | `:50` 起「ADR 工序（决策记录链）」节六款——`:52` 链序款＝`b0b449d` 工序链成文面（「…四方收口草案→架构席终写入 `docs/adr/`」）＝ADR 裁定⑧改写对象 |
| `.gitignore` | `:13` 注释行含 `.collab/{decisions,qa,receipts,board,research}/` 字样（注释面，行为零关） |

### 1.2 目录实体与 tracked 计数（67a3462 复点）

- 仓根 `.collab/`：根面散件 20 件 md（＝`.collab/defects/` 桶建立后计数，与 v1「20 件」同值）＋`tmp-w7-msg.txt`（untracked）；实体子目录含 `qa/`（tracked **10**＝v1 基线 8＋本票包双席审票件 2（`559f2a8`/`93434e0` 落链）〔N-3 勘正：v1 钉 8 系 `b8bdadc` 时点真值，现态 10 与合计 93 闭合〕）＋`defects/`（tracked 1＝drill 夹具缺陷台账 `1324B`，`36dfb78` 落链）。**无 drafts/product/architect/adr/audits 实体**。仓根 `.collab/` tracked 合计 93 件（含 defects 桶与双席审票件新增；其中根面散件 20 件全 tracked）。
- 包内 `agent-experts/baigong-software-team/.collab/`：tracked 594 件（＝v1 593＋会师裁定件 1）；其中 `.collab/qa/` **231 件**（＝v1 230＋会师裁定件）；`.collab/drafts/` 4 件全部住 `drafts/adr/` 子包（drafts 顶层散件＝0）；`returns/` tracked 2（仓根另 2＝在用实体桶，黄-2 取证）。
- 其余包 qa 面（候裁①射程对象）：`agent-skills/fuxi-skill/.collab/qa/` tracked **46**；`agent-skills/external-advisor-collab/.collab/qa/` tracked **2**；合计 **48**（与 §5.3 两态钉值一致）。
- ledger untracked 恰三文件（复点）：`.collab/ledger/ledger.jsonl`、`agent-experts/baigong-software-team/.collab/ledger/leases.jsonl`、`…/ledger.jsonl`。
- 历史文内旧路径引用存量（v1 起草时点 `b8bdadc`→`67a3462` 已漂移，照登〔N-2 勘正：原误引不存在的 `67a3362`〕）：tracked `*.md` 内 `.collab/qa/` 字面＝**209 文件／308 行**（v1 时点 205/290＋本区间审票/会师链件自带引用）；`drafts/adr` 字面＝**46 行**（v1 26＋同区间增量）。迁移射程测算按 §7 候裁①两态口径。
- 「十一桶」字样存量（黄-1 取证〔N-4 勘正复跑钉值〕）：全仓 occurrence＝**42**（`git grep -o "十一桶" | wc -l`）；baigong 包内＝**20 occurrence／19 行**（窄复核 `49f9448` 时点实测口径＝N-4 席值复现），其中**在用规范/配置面＝5 occurrence／4 行**（`seat-permissions.json:7`〔1〕＋`:59`〔2 同行〕、`seat-permissions-hooks-map.json:29`〔1〕、包内 `.collab/README.md:5`〔1〕），其余 **15 occurrence／15 行＝历史案卷**（qa//receipts/research/版本账 v0.1.18 行）＝append-only 不追改；六外包 `.collab/README.md` 各 1＝跨包面（＝§2 黄-1 条款点名随动只及 baigong 在用面；六外包 README 入 §6 禁动面登记，本批不动）。补全笔时点（HEAD 含 `49f9448` 窄复核件后）包内复跑＝23 occurrence／22 行，差值 3＝窄复核件自身命中＝同族计数漂移照登，在用面锚值不受影响。
- 键名错位钉证（红-2）：`drafts/deploy` 字样实在 `seat-permissions.json:59`＝engineer 行 **deny_globs_note**（非 v1 A1.6 所称 write_globs_note `:54`）；`:54` write_globs_note 内无 drafts 字样。配置/席位卡/规范真源三范围 drafts 子包字面现值＝**13 行**（本席 `-E` 实测）。
- 夹具/消费面随动取证：`drill-05-freeze-recover.sh`（`:17/:22/:27/:49` 用 `.collab/drafts/prd/` 样例）、`drill-06-replay-reconcile.sh` 同款 `:20`、`test_lease_instantiation.py:95/:96`；`lease-issuer.py:127-130` 子集校验按 write_globs 行逐字命中；`check-adr.py` 只锚 `docs/adr`＝零随动（命令形制钉值见 §5 判据7）；`.gitignore` 对 `.collab/audits/x.md` 两态均不 ignore（`git check-ignore` exit 1 实测）。
- **基线读数钉（本席 67a3462 实跑）**：`drill-05` exit **1**／`drill-06` exit **1**（红基线，红因＝缺陷台账 `.collab/defects/2026-11-08-drill夹具回读编码失配与缺件引用缺陷-v1.md`〔`36dfb78` 链〕＝黄-5 判据改差值口径的对象）；`python agent-experts/baigong-software-team/tests/s2/test_lease_instantiation.py` exit **0**；`check-adr.py` 裸跑 exit **4**（infra error，非用态）；`check-adr.py --bundle-root agent-experts/baigong-software-team` exit **0**／`docs/adr 盘上件=1｜桶1=1 桶2=20 桶3=1`。

## 2 施工规格 A 组：配置与规范成文（逐件行级，规格文本逐字入票）

> 施工序约束：A 组与 B 组迁移**必须同批一 commit**（配置指新名／实体已就位，两态不并存）。
> 行号锚＝67a3462 现态读数；施工票开工读数须复点，行号漂移按内容锚定位。

### A1 `config/seat-permissions.json`（十处行级替换＝v1 七处＋红-2 勘正落键＋ADR 裁定⑧随动三处）

1. product 行 `write_globs`：`[".collab/drafts/prd/", ".collab/product/", ".collab/drafts/proposals/"]` → `[".collab/drafts/", ".collab/product/"]`
2. product 行 `deny_globs`：删 `".collab/drafts/design/"`、`".collab/drafts/adr/"` 二项，原位并入 `".collab/adr/"` 一项（`".collab/audits/"` 已在位保留）。
3. architect 行 `write_globs`〔ADR 裁定⑧改判〕：头四段 `".collab/drafts/design/", ".collab/drafts/adr/", ".collab/architect/", ".collab/drafts/proposals/"` → `".collab/drafts/", ".collab/architect/"`；**同时删 `"docs/adr/"` 一项**（ADR 文书执笔权归主理人，架构席 adr 两面写权全清）。其余元素（含 `"docs/STRUCTURE.md"`）一字不动。
4. qa 行 `write_globs` 尾段：`".collab/drafts/proposals/"` → `".collab/drafts/"`（`.collab/audits/` 已在位不动）。
5. qa 行 `deny_globs`：删 `".collab/drafts/prd/"`、`".collab/drafts/design/"`、`".collab/drafts/adr/"` 三项 → 并入一项 `".collab/adr/"`（会签补件合法落点安排见 A7 第 2 款：会签意见落各席既有写域＝零新开写域，`adr/` 面对 product/qa 维持 deny）。
6. engineer 行 `write_globs` 尾段：`".collab/drafts/deploy/"` → `".collab/drafts/"`。
7. engineer 行 `deny_globs`：`".collab/qa/**"` → `".collab/audits/**"`（恰一处）。
8. engineer 行 **`deny_globs_note`（实在 `:59`**——〔红-2 勘正：v1 A1.6 误称 write_globs_note `:54`，`:54` 内无 drafts 字样，§1.2 已钉证〕）同句三处随动：① `".collab/drafts/deploy/"` 字样 → `".collab/drafts/"`；② 「十一桶闭集内 board/decisions/design/dispatch/evidence/process/**qa**/receipts/research/refs」段 → 「十七桶闭集内 board/decisions/design/dispatch/evidence/process/**audits**/receipts/research/refs」（桶名换代＋计数换代）；③ 本行另 1 处「十一桶闭集」（首句先决真源指针）→ 「十七桶闭集」。注记其余语义一字不动（让出父桶对表句、双兜底句、design 桶维持格句照旧）。
9. 顶层 `table_notes.枚举款六类`（`:7`）：「（B1-D·十一桶）」→「（B1-D·十七桶）」〔黄-1 在用锚点名随动①〕。
10. host 行〔ADR 裁定⑧写权改判落点〕：`write_globs` 尾追加两项 `".collab/adr/", "docs/adr/"`；`deny_globs` 内 `"docs/*（除转正代写通道）"` → `"docs/*（除转正代写通道与docs/adr/）"`（终写面开口显式化，与 write_globs 行同源）。

**纵深减层如实申报（裁定后果，非复议，承 v1）**：drafts 子包废止后四席 write_globs 同含 `.collab/drafts/`＝drafts 成共写域，席位互防从路径粒度降为租约粒度（当票租约 path_globs 点名具体文件＋声明闭集对账＋QA 纯净核验承载）；deny 面对 drafts 不再可枚举子路径。adr 面换代后防护改移＝`adr/` 单桶归 host 写域＋其余席位 deny/非授权双兜底（签发面写域子集校验＋写侧『路径∉当席租约』）。此为裁定的机械后果，票面如实登记不改判。

### A2 `config/seat-permissions-hooks-map.json`（与 A1 同源派生·同批同值）

- product／qa／engineer 三席 `deny_globs` 改动＝A1 对应席**逐字同值**（SRC4Z 两文件五席数组全等约束在册）。
- host 行 `deny_globs`〔v2 新增随动，v1 A2「host 行零动」作废〕：`"docs/*（除转正代写通道）"` 同值替换为 A1-10 新值（两文件 host 行同源对账）。
- engineer 行 `deny_globs_note`（`:29`，同源缩略版）：「十一桶闭集」→「十七桶闭集」一处〔黄-1 在用锚点名随动②〕。
- architect 行零动（deny 面本无 adr 条目）。

### A3 五席位卡（承 v1 四卡＋lead 卡随 ADR 裁定⑧入射）

- product `:22`：现值 → 新值：`- 写域：\`.collab/drafts/\`、\`.collab/product/\``
- architect `:22`〔ADR 裁定⑧〕：现值（含 `.collab/drafts/{design,adr}/`、`docs/adr/` ADR 落盘写权尾段）→ 新值：`- 写域：\`.collab/drafts/\`、\`.collab/architect/\`、\`.collab/tickets/\` 票面文档（起草与按修票权修订）、开发票四字段、\`tests/\` 共写（增删改走 C1）、租约段签注与灰度判据（票内）`（adr 两面写权句全删）。
- architect `:23`〔随 :22 换代回滚〕：现值含「**写域行已授权之 `docs/adr/` 除外**——其防护＝…」例外子句 → 新值：`- 明确不可写：\`docs/\`（三件套及 STRUCTURE 等 docs 子面）、\`.archive/\`、代码域、\`.collab/\` 未授权子域、\`audits/\``（例外子句随写权撤销而删＝ES2 批前形态回滚；`docs/adr/` 防护移交 host 租约面＝A1-10）。
- architect `:24`〔ADR 裁定⑧〕：`- 可写内容：设计、ADR、开发票、边界约束` → `- 可写内容：设计、开发票、边界约束`。
- qa `:22`：尾段 `\`.collab/drafts/proposals/\`` → `\`.collab/drafts/\``（余一字不动；该行 `\`.collab/audits/\`` 经 B 组迁移由悬空变实存）。
- engineer `:22`：`\`.collab/drafts/deploy/\`` → `\`.collab/drafts/\``（余一字不动）。
- lead `:50`〔ADR 裁定⑧路由随动〕：现值单行 `| 系统设计、ADR、开发票、边界约束 | software-team-architect |` → 拆两行：`| 系统设计、开发票、边界约束 | software-team-architect |`＋`| ADR 文书（起草与 docs/adr 落盘＝主理人自写，不派发，裁定 67a3462） | software-team-lead（本席） |`（卡行数 77→78 登记）。

### A4 规范真源 `skills/sop/references/collab-fixed-structure.md`

- `:10` 桶名闭集行：`decisions/ qa/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/`＋README 索引件 → **`decisions/ audits/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/ drafts/ adr/ architect/ product/ ledger/ returns/`＋README 索引件**（**17 桶**——〔黄-2 修：v1 拟 16 桶漏 `returns/`，仓根＋包内 tracked 实体在用桶各 2 件已钉证，补桶入闭集〕；＋`drafts/ archive 子包条款`新行：「`drafts/` 顶层直接落交接件草稿、无分子包；唯一例外子包＝`drafts/archive/`（过期版本归档）；每交接件在 drafts 顶层只存一件存活态最新版」）。
- `:16` 入库面行：`qa`→`audits`，并补 `drafts/`、`adr/`、`architect/`、`product/`、`ledger/`、`returns/` 入入库面（ledger 补链＝裁定⑤；returns 在用面本已入库＝名录补全非新开）。
- 依据注记段 append 两行：①「六目录＝需求最终确认前阶段标准界定（裁定 2026-11-08 `b8bdadc`）；桶闭集换代 11→17＝同裁定结构落改＋returns 补录」；②〔黄-7 业界锚〕「adr 单立之业界实践锚＝Michael Nygard《Documenting Architecture Decisions》(2016)：ADR 记录难以逆转的架构决策，其 Consequences 常直接驱动或否定产品需求（取证口径＝人类工程实践通例优先）；本仓两证 `b0b449d`／`b2150c5` 位次旁证」。

### A5 README 成文两件（承 v1，桶名录随 17 桶换代）

- 新建仓根 `.collab/README.md`：内容＝桶总表（六标准目录逐行「目录·放什么·谁法定写」照裁定目标态表誊入，**adr 行法定写席＝主理人**〔ADR 裁定⑧〕＋表头注「六目录＝需求最终确认前阶段的标准界定，非全生命周期闭集」＋未列子包存续条款＋仓根性质注：仓根 `.collab/`＝本仓治理史面，无席位写权机检（seat-permissions 只辖软开团包内席位），落件按惯例＋decisions 归口）。
- 包内 `.collab/README.md`：桶名录行改与 A4 新 17 桶闭集**逐字同值**；「十一桶」字样随动清零〔黄-1 在用锚点名随动③〕；入库/排除两制行随动；首行「现行在途案卷暂在仓根」注保留（事实态）。

### A6 `.gitignore` 注释随动（行为零变款，承 v1）

- `:13` 注释行 `qa` → `audits` 一处；正文排除面无 qa 字样＝零行为改动（回执附 `git check-ignore -v` 前后同值读数对拍：`agent-experts/baigong-software-team/.collab/audits/x.md` 两态均不 ignore＝本席已实测 exit 1 基线在册）。

### A7 ADR 工序真源随动 `skills/software-orchestration/references/standard-sop.md`〔ADR 裁定⑧-⑬ 成文落点〕

- `:50` 「ADR 工序（决策记录链）」节**第 1-4 款重写**（第 5-6 款 supersede/立项触发判据一字不动）：
  1. **链序（换代）**：任意席位可发起（会签＝讨论流程同构）→主理人誊录登记（`.collab/decisions/`·append-only·逐字）→相关席位会签＝**状态闸**（收口＝通过判定）→收口草案落 `.collab/adr/`（过程面＝drafts 治理成员：**一题一文档、禁一题多版本存活**，过期版本入归档子包）→呈报人类知悉/授权放行（**涉产品设计层＝必须人类授权放行；不涉＝会签收口可自决**）→**主理人统一起草形成执行交接的正式 ADR 件落 `docs/adr/`**（编号四位·Status 闭集·头块五行照 ES E-ADR-1″）。
  2. **会签语义（换代）**：会签＝对收口草案的签署认可；会签席可出保留项——保留项未闭合前正式件起草段禁启动（收口未成）。保留项闭合归位不变：经主理人呈人类裁定，裁定落 decisions 后草案修订＝**主理人照新裁定登记件重誊草案**（誊聚权不含裁量、执笔权归主理人＝裁定⑧；落位 `.collab/adr/`＝零新开写域）；会签席永不改草案（deny 语义不变）。**会签补件合法落点＝各席既有写域**（product→`.collab/product/`、qa→`.collab/audits/`、architect→`.collab/architect/` 或当票票面）＝零新开写域，`.collab/adr/**` 对 product/qa 维持 deny（A1-2/A1-5 承接）。重誊后全链重走会签（同序同判据），旧会签随重誊作废不入账本终态。
  3. **正式件段＝条款甲语义承（执笔席换代）**：正式 ADR 件＝主理人逐字照录四方会签收口草案，零文风裁量——终写件与收口草案正文哈希对等方可落 `docs/adr/`；主理人职责＝执笔＋落盘担责（R10/R11/R21 语义随写权移主理人）。会签签署＝账本签字记录（经 state-transition.py 既有通道）。
  4. **条款乙（承）**：ADR 记的是多方已收敛决策，非主理人单方草案；主理人组织会签又执笔终写不构成自审——记录链≠正文链，防自审条款（转正代写通道·制度③）辖架构正文链（docs/ARCHITECTURE.md 族），两条路各自成文互不管辖。
- 旧文「架构席终写」字样在本节第 1-4 款清零（判据 8 钉）；`b0b449d` decisions 登记件本体＝append-only 史实锚不改，其「被改写」效力由本节换代承接（后生效覆盖先前，既有口径）。
- 写权射程申报：本件属 software-orchestration 随包技能域（B345 同域先例＝架构席随包技能维护权射程）；与 B345 票写集（handoff/dev/dispatch-discipline 三件＋SKILL.md）**零交叠**——standard-sop.md 不在 B345 声明闭集内。

## 3 施工规格 B 组：目录实体（迁移与补链）

1. **audits 改名两处（仓根＋包内）**（git mv 保 blob sha 逐件零变）：`git mv .collab/qa .collab/audits`（现值 tracked **10** 件）；`git mv agent-experts/baigong-software-team/.collab/qa agent-experts/baigong-software-team/.collab/audits`（现值 tracked **233** 件）。两值系本笔补全时点 `737fc0b` 复点（＝67a3462 时点 8/231＋双席窄复核件四枚落链随增，照登）——**施工票开工读数复点现值为准**，R 行计数按「复点两桶之和＋adr 4」公式对钉，不锁死本数。其余包 qa 面（fuxi 46＋EAC 2）迁否＝候裁①，默认射程不动。
2. **adr 单立＋四件迁入**：包内 `.collab/drafts/adr/` 四 tracked 件 `git mv` → 包内 `.collab/adr/`（drafts/adr 子包目录随 mv 清空消失）；仓根 `.collab/adr/` 本批不建空目录（B4 从简条款）。**历史态照登行（一题一文档前向条款）**：0001 题 draft/final＋两份会签件四件并存＝旧工序（架构席终写态）历史事实，append-only 不并删不追改；ADR 裁定⑬「一题一文档、禁一题多版本存活」自新名生效点起对 `.collab/adr/` 过程面前向适用（在途题唯一存活文档，换版走归档子包）。
3. **ledger 补链**：`git add` 恰三 untracked 文件（§1.2 点名），入账即链态＝记账面脱链异常消除（裁定⑤）。
4. **architect 补建（包内）**：`mkdir` 包内 `.collab/architect/`＋落一件 5 行内索引占位 README（桶用途一句话＋「实体随首件架构过程件落位」）——空目录不入 git，占位件＝机械断言 `git ls-files` ≥1 可验。**仓根六子集从简条款（承 v1）**：仓根＝治理史面无写权机检，本批只落有实物对象者（audits mv＋ledger 链＋README），drafts/architect 空仓不建，首件届时自然落位（理由：空目录不入链＝断言不可验＋YAGNI）。
5. **drafts 顶层化＋归档子包（承 v1 我定形态，候裁③可推翻）**：归档子包落位＝**`drafts/archive/`**（包内）。理由三条照 v1：①归档对象与 drafts 同域同主（起草席换版＝旧版 mv 进 `drafts/archive/`＋新版落顶层，一次租约闭环，无需跨席搬件）；②`drafts/archive/` 天然被 write_globs 行 `.collab/drafts/` 前缀命中（lease-issuer `:130` startswith 校验语义），零新增配置行；③与 host `.collab/archive/`（退役定稿落位）语义分域不混。现 drafts 顶层零散件＝无需存量归位动作；条款为前向纪律。**ADR 面同规（裁定⑬）**：`.collab/adr/` 在途交接件一题一文档，过期版本去向＝`.collab/adr/` 面归档随 drafts 治理同则（届时若需机检行，随批 config 随动另笔，本票不预开）。
6. **tests 三件样例随动（drafts/prd 废止的机械必然，承 v1）**：`drill-05` `:22/:27/:49` 三处 `.collab/drafts/prd/tmp-drill05.md` → `.collab/drafts/tmp-drill05.md`（`:17` 注释行 `drafts/prd` 字样随改）；`drill-06` `:20` 同款一处；`test_lease_instantiation.py` `:95/:96` 两处 `.collab/drafts/prd/` → `.collab/drafts/`。

## 4 声明闭集（OA-D6-5 机检源·逐行完整路径）

- agent-experts/baigong-software-team/config/seat-permissions.json
- agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json
- agent-experts/baigong-software-team/agents/software-team-product.md
- agent-experts/baigong-software-team/agents/software-team-architect.md
- agent-experts/baigong-software-team/agents/software-team-qa.md
- agent-experts/baigong-software-team/agents/software-team-engineer.md
- agent-experts/baigong-software-team/agents/software-team-lead.md〔v2 新增：ADR 路由行 `:50`〕
- agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md
- agent-experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md〔v2 新增：ADR 工序节 1-4 款〕
- agent-experts/baigong-software-team/.collab/README.md
- .collab/README.md（新建）
- .gitignore
- agent-experts/baigong-software-team/tests/acceptance/drills/drill-05-freeze-recover.sh
- agent-experts/baigong-software-team/tests/acceptance/drills/drill-06-replay-reconcile.sh
- agent-experts/baigong-software-team/tests/s2/test_lease_instantiation.py
- （mv 面＝仓根 qa 10＋包内 qa 233＋adr 4＝**247**〔737fc0b 复点值；施工票开工复点为准＝「两桶复点＋4」公式〕；候裁①并入态另加 48＝295；逐件新路径＝旧路径名改，回执附 `git show --name-status` 全量 R 行计数对钉）
- （add 面 3 件＝§1.2 ledger 三文件点名＋新建 `.collab/README.md`＋占位 `agent-experts/baigong-software-team/.collab/architect/README.md`＝共 5 新链件）

## 5 机械可验判据（施工回执必附实测）

1. **JSON 合法＋同源全等**：两 config `python -m json.tool` exit 0；两文件五席 deny_globs 数组逐席全等（SRC4Z 同批同值约束复用，host 行随 A1-10/A2 同步改后仍逐席全等）。**门禁对拍形制（黄-6 钉）**：run-gates 计数一律**同形态两读数对拍**（主盘对主盘、worktree 对 worktree），**禁跨形态比数**（worktree 形态 6,582/6,586 与主盘差一量级＝形制差非盘面差）。
2. **grep 钉值（现值→新值 0）**：`git grep -c "drafts/prd\|drafts/design\|drafts/adr\|drafts/proposals\|drafts/deploy" -- agent-experts/baigong-software-team/config agent-experts/baigong-software-team/agents agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md` ＝ **0**（现值基线＝**13 行**〔§1.2 钉〕）；`git grep -c "collab/qa" -- "agent-experts/baigong-software-team/config"` ＝ 0；「十一桶」在用面清零（黄-1 点名四处逐锚复跑）：`git grep -c "十一桶" -- agent-experts/baigong-software-team/config agent-experts/baigong-software-team/.collab/README.md` ＝ **0**（现值＝5 occurrence／4 行；历史案卷＋六外包面不在射程，禁动面登记）。
3. **ls-files 断言（红-1 两态条件化钉·终态挂候裁①）**：`git ls-files | grep -c "/\.collab/qa/\|\.collab/qa/"` 现值＝**291**（本笔补全时点 `737fc0b` 复点＝仓根 10＋包内 233＋fuxi 46＋EAC 2；67a3462 时点口径＝8＋231＋46＋2＝287，两时点差＝窄复核两件落链随增，照登）。施工后按候裁①两态各自钉死、机械可判：**态甲（候裁①不并入＝默认射程）**钉值＝**48**（fuxi 46＋EAC 2 照登，非 FAIL）；**态乙（候裁①并入同批 mv）**钉值＝**0**。〔勘正本体＝会师红-1：v1 钉「路径面 0」把未裁选项当既成事实，默认射程下必 FAIL，废止〕。其余钉值：`.collab/audits/` tracked＝复点两桶和（67a3462 口径 8＋230＝238；737fc0b 口径 10＋233＝243；按施工开工复点钉）；`.collab/adr/` tracked＝4；`.collab/architect/` tracked≥1；ledger 三文件 tracked 态。
4. **mv 保真**：`git show --name-status` 默认射程 R 行＝复点两桶和＋4（＝247 口径），**全 R100**（内容零变·`-M` 检测）；候裁①并入态另加 48 全 R100；抽验四件 adr 新旧 blob sha 全等（`git cat-file blob` 双点对拍）。
5. **门禁零回归对拍（红-3 两态改钉＋黄-6 形制）**：基线＝本票开工主盘实跑（开工时点登记，本笔补全时点参考读数＝**GATE PASS exit 0／发现 31,901**〔`737fc0b` 后主盘，含窄复核链件漂移照登；67a3462 时点 31,885〕）。判据＝**GATE PASS 不翻红**＋前后两读数**同形态**＋差值按窄口径（GATE PASS 行「发现 N 条」单一真源，参并案票 B3 条款）逐条归因。**〔红-3 勘正〕废止 v1「预期差值≈0」钉**：mv 后历史文内旧路径引用按案乙转悬空，check-pointers 类必增（QA 席隔离 worktree 模拟对拍实测 **＋12**＝pointers +20／reconcile +21／closure −8），与「≈0」互斥——改钉两态：**态甲（案乙不追改）**差值非零合法，钉「每条新增悬空命中可归因＝旧文 `.collab/qa/`／`drafts/adr` 字样（存量 209 文件/308 行＋26→46 行同族）」，禁「基本通过」式糊账；**态乙（案甲并入＋追改）**方可钉差值≈0。
6. **drill/s2 差值口径（黄-5 改钉）**：开工基线两读数照登＝`drill-05` exit **1**／`drill-06` exit **1**（红基线＝既有缺陷〔write-guard deny 输出 ensure_ascii 转义 vs 夹具中文明文／夹具引用目标缺件〕，台账 `.collab/defects/2026-11-08-drill夹具回读编码失配与缺件引用缺陷-v1.md`〔`36dfb78`〕在册，修路另票候排＝禁动面锁死）。验收＝改差值口径：三件随 B6 改后复跑，drill 两笔仍 exit 1 且**红因读数与基线同型**（缺陷面不因本票恶化）＝PASS；`python agent-experts/baigong-software-team/tests/s2/test_lease_instantiation.py` exit **0** 不变（夹具租约路径随 B6 自洽）。
7. **check-adr 命令形制一行级钉死（黄-3）**：验收命令＝`python agent-skills/object-audit/scripts/check-adr.py --bundle-root agent-experts/baigong-software-team`，钉 exit **0**／`docs/adr 盘上件=1｜桶1=1 桶2=20 桶3=1`（本票不动 `docs/adr/` 一字，复跑读数同值）。裸跑 exit **4**（infra error）＝非用态，不入判据（形制在册防复现误读）。
8. **ADR 随动面 grep 钉值（v2 新增）**：`git grep -c "架构席终写" -- agent-experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md` ＝ **0**（现值 1）；`git grep -c "docs/adr" -- agent-experts/baigong-software-team/agents/software-team-architect.md` ＝ **0**（现值 3＝`:22`/`:23`×2）；architect 卡「可写内容」行不含「ADR」＝`git grep -c "可写内容：设计、ADR" -- …architect.md` 现值 1→**0**；lead 卡 `ADR … software-team-architect` 路由行现值 1→**0**（新行含「ADR 文书…software-team-lead（本席）」命中 1）；seat-permissions.json host 行含 `".collab/adr/", "docs/adr/"`＝命中 1、architect 行含 `"docs/adr/"`＝**0**。

## 6 禁动面闭集（点名）

- `docs/adr/`（终写位＝裁定②明文不动；写权席换主理人＝配置面改，盘上件零动）；`docs/**` 全部；`.archive/**`。
- 历史案卷**内文**一切旧路径引用与旧字样（`.collab/qa/` 209 文件/308 行／`drafts/adr` 46 行／「十一桶」历史 15 行）——append-only 不回改（新名生效点起按新名落；全量追改与否＝候裁①射程）。
- `agent-skills/fuxi-skill/.collab/qa/`（46）、`agent-skills/external-advisor-collab/.collab/qa/`（2）＝候裁①射程，本票默认不动。
- 六外包 `.collab/README.md`（bundle-assembly-registration／external-advisor-collab／fuxi-skill／multi-collab／object-audit／object-build 各 1 处「十一桶」）＝跨包面本批不动（黄-1 随动只点名 baigong 在用四锚）。
- 仓根 `.collab/` 根面散件 20 件＋`tmp-w7-msg.txt`＝候裁②，本票不搬不删。
- `.collab/defects/` 台账本体（drill 缺陷登记件）＝只读引用，修路另票候排。
- `run-gates.sh`／各 check-*.py／`write-guard.py`／`lease-issuer.py`／`publish.py` 等门禁与机件本体＝零触碰（本票改其消费的配置面，不改机件）。
- 三同源版本号（`plugin.json`／`bundle.lock`／`.codebuddy-plugin/plugin.json` 现均 0.1.30）＝本票零 bump（候裁④）。
- SEMGV-T3 案写集（五卡各一行的 T3 挂载句／bundle.lock／注册面 plugin.json／sop SKILL.md／claim-commitment-governance 七件）＝本票不预写 T3 挂载句；A3 席位卡改动与 T3 挂载句的交叠处置＝候裁⑤票间序，两案条款互不污染。
- `standard-sop.md` ADR 工序节**第 5-6 款**（supersede 归道／立项触发判据）＝本票零动（ADR 裁定未涉）。
- 工具归属／shareds 自包含议题＝**另票 TOOLHOME**（已径裁），严禁入本票射程。
- `skills/software-orchestration/` 其余三 references 件＋SKILL.md＝B345 票写集，本票零触碰（零交叠自证＝两闭集互不含）。

## 7 候裁面单列（本票不自行拍，逐条给规格供裁；承 v1 六项，会师裁定＝继续单列不重审）

**候裁① 存量历史案卷迁移射程（红-1/红-3 钉值终态挂此，两态钉保持不替皮总择定）**：两案供裁——
- 案甲＝全量 `git mv`（含 fuxi 46＋EAC 2 并入）之外再追改史文内文引用（308 行 qa＋46 行 drafts/adr）：指针全实但违 append-only 先例、24,193 级 pointers 存量噪声面重排成本高；
- 案乙＝**新名生效点起按新名、旧文不追改**（主理人倾向·append-only 先例同构）：悬空旧路径按存量噪声照登。
- 本席规格建议＝案乙＋补充件（两份 README 各加一行「历史案卷内 `.collab/qa/` 字样＝改名前旧路径，读作 `.collab/audits/`」去歧义句）。**两态钉＝§5.3（48｜0）与 §5.5（差值归因｜≈0），裁后自动取态，票面不预择。**

**候裁② 仓根 .collab 治理史散件 20 件＋tmp-w7-msg.txt 处置**：承 v1 规格（20 件按性质归 `decisions/`＋tmp 删除；或照旧＋README 注散件惯例）。归裁。

**候裁③ 归档子包精确落位**：本票 §3.B5 已给方案（`drafts/archive/` 包内＋三条理由）；替代案＝复用 host `.collab/archive/`（跨席搬件代价在册）。归裁。

**候裁④ 版本号三同源是否随批 bump**：本票默认**零 bump**——理由承 v1（配置面随动批不改变包对外行为面；升号排期归 PROJINIT 合并批＋SEMGV 系列放行后的合并升号窗口）。若裁定要求随批 bump，三同源＋changelog 同批条款另出。归裁。

**候裁⑤ 票间互斥（SEMGV-T3 × COLLAB-STRUCT-1 席位卡写集交叠）**：承 v1 条款——实测交叠面＝席位卡写域行；T3 v2（`b4a75d5`·候皮总放行未施工）写集含五卡各追加一行挂载指针；本案 A3 改五卡写域/路由行本身。两笔落同文件相邻行＝git 可串接（不同行零冲突），真风险＝语义序。本席分析＝**先 T3 后 STRUCT**；条款＝STRUCT 施工票开工读数须复点五卡现态，若链上出现 T3 施工笔即以其为基线（v1 钉的五卡 sha 基线随之作废重取，本 v2 §1.1 钉值同承受此条款）。归裁确认序。

**候裁⑥ 票面住址成文**（审计件遗留）：`.collab/tickets/`（规格名）vs `.scratch/tickets/`（实际体例）二选一入 README/规范表。本票按近期体例走 `.scratch/tickets/`；成文归裁。

（候裁六项之外无新增候裁；ADR 裁定⑧-⑬＝已裁既成条款不入候裁；此前「ADR 甲/乙案候裁」随 `67a3462` 销账。）

## 8 票间关系（票包全景）

- `COLLAB-STRUCT-1`（本票 v2）＝结构落改主票：§2 A 组成文（含 A7 ADR 随动）＋§3 B 组实体，同批一施工 commit；施工票＝工程师落，另计于本票两笔封顶之外。
- `COLLAB-STRUCT-B345`（并案维护票）＝绿票本体，仅「§1 三律首句行锚 `:45`→`:40` 一行锚勘」随批顺手（会师裁定 3·不单出 rev）——**该锚勘落笔属 B345 票面自身，主票 v2 不代改**（本行＝随批登记，射程归 B345）。写集与 STRUCT-1 零交叠（standard-sop.md 归 STRUCT-1 A7 新入射，不在 B345 闭集）。
- 与 `SEMGV-T3`＝候裁⑤票间序约束，条款互不污染。
- `TOOLHOME`（工具归属/shareds 自包含议题）＝已径裁另票，与本票零关系，仅作禁动登记防塞入。

## 9 完工定义与三态明示（逐条分开写）

1. **做了但没落盘**：起草与本笔补全期真源五件全文直读（皮总两裁定＋会师裁定＋双席审票＋B345 票面）、配置/席位卡/规范/夹具/tests 消费面只读实测（wc/sha/grep/mv 计数/run-gates 主盘基线 31,885→31,901 两读数、drill/s2/check-adr 基线形制）——均仓内只读命令，仓内零临时脚本零中间文件。
2. **落盘了但没提交**：本件写入 `.scratch/tickets/` 后至 `git add` 前为工作区改动态（本笔＝链上 a56ad4d 截断件 71 行之上补全，工作区→新链笔）。
3. **提交了但没对账**：commit 后至完工回报给出「status 他案照登＋`git show --name-only` 恰本件」实测前此态存在；由完工回报补齐，不预标「已完成」。

- **完工定义**：票面单笔 `collab:` commit 落账＋回报附 sha／行数／字节／sha256＋修单条目对照表＋三态明示。
- **纪律**：双侧 pathspec 限定本件；禁 `git add -A`／`--amend`／`reset`／`--no-verify`；他案在制品照登不碰；门禁 advisory 照常；纯规格零施工——本票不 mv 一件、不改 config 一字、不补链 ledger、不建目录。
- **本件 commit sha 与提交后态**由完工回报实测给出，正文不预写自指值。

---

## 租约段（架构席签注 · 由 B2 实例化）

```
lease:
  ticket: COLLAB-STRUCT-1-v2
  seat: architect
  author_seat: arch-struct1c
  path_globs:
    - .scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v2.md
  deny_globs:
    - docs/**
    - .archive/**
    - agent-skills/**
    - agent-experts/**
    - softwares/**
    - tests/**
    - "*.py"
  note: 本票只出 COLLAB-STRUCT-1 结构名实对齐与规范成文规格票面 v2 一件（含 N-1 截断补全＋N-2/3/4 勘正），零施工；不 mv 目录、不改 seat-permissions/席位卡/config/gitignore/standard-sop 一字、不补链 ledger、不建目录、不 bump 版本。依据＝皮总裁定 b8bdadc（结构七条）＋皮总 ADR 裁定 67a3462（写权统一主理人／会签＝状态闸／人类闸分级／任意席位可发起／时序／drafts 一题一文档）＋会师裁定 36dfb78 红三黄七修单（红-1/红-3 两态钉挂候裁①、红-2 deny_globs_note 键名勘正、黄六收口）。候裁六项继续单列不自行拍。两笔封顶已兑现（v1＋v2）；落链即停候双席窄复核（改哪段复验哪段，不开新面）。TOOLHOME 另票不入射程。
```