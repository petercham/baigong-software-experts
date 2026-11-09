# COLLAB-STRUCT-1 .collab 结构名实对齐与规范成文票（架构席·过程件规格票·纯规格零施工）

- **票号**：COLLAB-STRUCT-1｜**版本**：v1（append-only 序链起点）｜**起草席**：架构席（arch-commitment-design）
- **开工读数（实测）**：`2026-11-08 19:18:02 +0800`／HEAD＝`b8bdadc`（≥派工令下限 `b8bdadc` 对钉）／`git status --porcelain --untracked-files=no`＝空（tracked 面净；他案 untracked 取证面照登不碰：`.scratch/FX-U1x*`、`.collab/ledger/`〔本票射程内补链对象〕、research 散件等）。
- **裁定真源（唯一条款依据·已完整直读）**：`.collab/decisions/2026-11-08-皮总裁定-collab结构规范重定义与缺陷清单并案.md`＝`b8bdadc` 落链（blob 5,056B／sha256 前 12 `ea8061101341`）。
- **审计取证基准**：`.collab/decisions/2026-11-08-呈皮总-collab目录结构审计如实报告与优化方案候拍-v1.md`＝`c848a78` 落链（blob 8,772B／`cea90e88afa9`）。
- **并案清单基准**：`.collab/2026-11-08-百工团队层问题复盘清单-v1.md`＝`0259cd6` 落链（blob 6,272B／`9dc187945f91`）——其中 B3/B4/B5 三项归并案票 `COLLAB-STRUCT-B345`（见 §8 票间关系）。
- **两笔封顶**：本票 v1＋（如需）v2 一笔封顶；审后修票按会师裁定另计。
- **门禁基线（开工时点实跑）**：`bash agent-skills/object-audit/scripts/run-gates.sh --no-write` ＝ **GATE PASS exit 0／发现 31,875 条均 advisory**（FX-U21 后 `--no-write` 只读开关已上线，真盘禁跑闸体例自此退役——50164c9 收口登记在册）。

## 0 已入账裁定转录（本票忠实执行，不复议）

1. drafts 分子包＝**错误定义废止**：交接件草稿直接落 `drafts/` 顶层，无子包（归档子包除外）；每交接件只留一件存活态最新版，过期版本入归档子包。
2. **adr 单立 `.collab/adr/`**（不在 architect/ 下）——条件问「adr 可否涉产品需求变更」裁定取证＝是（ADR 工序链 `b0b449d` 三方会签含产品席＋ADR-0001 产品席保留项 R-PM-1 `b2150c5`）；交付面 `docs/adr/` 终写位不动；过程面 `drafts/adr/` 四件迁入。
3. `architect/`＝架构席非交接件写权域（派单排期、函件套件、接口矩阵类）——规格有域无实体，须补建。
4. `audits/`＝名实对齐：实体 `qa/` 改 `audits/`（仓根＋包内），席位卡／seat-permissions.json／hooks-map 同批随动。
5. `ledger/`＝两处 untracked 补 commit 入链。
6. 未列子包（board/dispatch/evidence/inbox/process/receipts/refs/research/returns 等）存续不禁，按项目阶段取用。
7. **六目录定位＝需求最终确认前阶段的标准界定**，非全生命周期闭集——本票全部措辞按此口径（目标态表头注必带该限定）。

## 1 现态基线钉值（落笔前实测，2026-11-08）

### 1.1 配置与规范面（逐件行数／字节／sha256 前 12）

| 件 | 现态 |
|---|---|
| `agent-experts/baigong-software-team/config/seat-permissions.json` | 73 行／8,655B／`2e92c7b97af2` |
| `agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json` | 40 行／4,003B／`0d25b6057c93` |
| `agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md` | 27 行／1,719B／`403db8e0e0f5` |
| `agent-experts/baigong-software-team/.collab/README.md` | 12 行／635B／`9e9397c74902` |
| 仓根 `.collab/README.md` | **不存在**（审计实锤：仓根缺 README） |
| `agents/software-team-product.md` | 46 行／3,227B／`a1c6a4f8ecce`（`:22` 写域行含 `.collab/drafts/prd/`） |
| `agents/software-team-architect.md` | 47 行／3,825B／`1c51935d3ca6`（`:22` 含 `.collab/drafts/{design,adr}/`） |
| `agents/software-team-qa.md` | 49 行／3,848B／`0bcda097f0f7`（`:22` 已写 `.collab/audits/`＝悬空指空现状实锤；含 `.collab/drafts/proposals/`） |
| `agents/software-team-engineer.md` | 49 行／3,951B／`b4331d7422c4`（`:22` 含 `.collab/drafts/deploy/`） |
| `agents/software-team-lead.md` | 77 行／5,298B／`c2287132f1e8`（grep 无 drafts/qa/audits 命中＝本票零触碰） |
| `.gitignore` | `:13` 注释行含 `.collab/{decisions,qa,receipts,board,research}/` 字样（注释面，行为零关） |

### 1.2 目录实体与 tracked 计数

- 仓根 `.collab/`：实体子目录 13（board/decisions/design/dispatch/evidence/inbox/ledger/process/qa/receipts/refs/research/returns）＋根面散件 20 件 md＋`tmp-w7-msg.txt`（untracked）；**无 drafts/product/architect/adr/audits 实体**。tracked 计数：`.collab/` 全部 84 件，其中 `.collab/qa/` 8 件、根面散件 20 件全 tracked。
- 包内 `agent-experts/baigong-software-team/.collab/`：实体子目录 13（含 drafts/product，无 architect/adr/audits/tickets）＋根面散件 3 件（2 件登记／呈拍＋README）；tracked 593 件，其中 `.collab/qa/` **230 件**、`.collab/drafts/` 4 件（全部住 `drafts/adr/` 子包，drafts 顶层散件＝0）。
- 其余包 qa 面（对照，本票不迁·见 §7 候裁①）：`agent-skills/fuxi-skill/.collab/qa/` tracked 46 件；`agent-skills/external-advisor-collab/.collab/qa/` 2 件。
- ledger untracked 恰三文件：`.collab/ledger/ledger.jsonl`、`agent-experts/baigong-software-team/.collab/ledger/leases.jsonl`、`…/ledger.jsonl`。
- 历史文内旧路径引用存量（迁移射程测算基数）：tracked `*.md` 内 `.collab/qa/` 字面命中＝**205 文件／290 行**（不含 evidence 排除面）；`drafts/adr` 字面命中＝**26 行**。
- 目录字面机械消费者（随动取证）：`tests/acceptance/drills/drill-05-freeze-recover.sh`（`:17/:22/:27/:49` 用 `.collab/drafts/prd/` 租约样例）、`drill-06-replay-reconcile.sh`（`:20` 同款）、`tests/s2/test_lease_instantiation.py`（`:95/:96` 断言 `.collab/drafts/prd/`）——`lease-issuer.py:127-130` 子集校验按 write_globs 行逐字命中，drafts 子包废止后三件样例必须随动。seat-permissions 其余消费者＝`write-guard.py:321`／`lease-issuer.py:160`／`freeze-unfreeze.py`／`dispatch-builder.py`（读 config 非硬编码目录字面＝零随动）；`check-adr.py` 只锚 `docs/adr`＝零随动；`.gitignore` 排除面不含 qa/audits（默认入库）＝改名零 ignore 行为变化。

## 2 施工规格 A 组：配置与规范成文（逐件行级，规格文本逐字入票）

> 施工序约束：A 组与 B 组迁移**必须同批一 commit**（配置指新名／实体已就位，两态不并存）。

### A1 `config/seat-permissions.json`（七处行级替换）

1. product 行 `write_globs`：`[".collab/drafts/prd/", ".collab/product/", ".collab/drafts/proposals/"]` → `[".collab/drafts/", ".collab/product/"]`
2. product 行 `deny_globs`：删 `".collab/drafts/design/**"`、`".collab/drafts/adr/**"` 二项，原位并入 `".collab/audits/**"` 保留（即该二项替换为一项 `".collab/adr/**"`）。
3. architect 行 `write_globs` 头两段：`".collab/drafts/design/", ".collab/drafts/adr/", ".collab/architect/", ".collab/drafts/proposals/"` → `".collab/drafts/", ".collab/adr/", ".collab/architect/"`（其余元素与 `docs/adr/` 等一字不动）。
4. qa 行 `write_globs` 尾段：`".collab/drafts/proposals/"` → `".collab/drafts/"`（`.collab/audits/` 已在位不动）。
5. qa 行 `deny_globs`：删 `".collab/drafts/prd/**"、".collab/drafts/design/**"、".collab/drafts/adr/**"` 三项 → 并入一项 `".collab/adr/**"`。
6. engineer 行 `write_globs` 尾段：`".collab/drafts/deploy/"` → `".collab/drafts/"`（`write_globs_note` 内三子域对表句随之改：`returns/inbox/drafts 父桶下 engineer 行` 语义不变、`drafts/deploy` 字样改 `drafts`——注记文本随动登记）。
7. engineer 行 `deny_globs`：`".collab/qa/**"` → `".collab/audits/**"`（恰一处）。

**纵深减层如实申报（裁定后果，非复议）**：drafts 子包废止后四席 write_globs 同含 `.collab/drafts/`＝drafts 成共写域，席位互防从路径粒度降为**租约粒度**（当票租约 path_globs 点名具体文件＋声明闭集对账＋QA 纯净核验承载）；deny 面对 drafts 不再可枚举子路径。此为裁定①的机械后果，票面如实登记不改判。

### A2 `config/seat-permissions-hooks-map.json`（与 A1 同源派生·同批同值）

- product／qa／engineer 三席 `deny_globs` 改动＝A1 对应席**逐字同值**（SRC4Z 两文件五席数组全等约束在册）；architect／host 行零动。

### A3 四席位卡（各一行，`:22` 写域行，内容锚非行号锚——见 §7 候裁⑤票间序）

- product `:22`：`- 写域：` → 新值：`- 写域：\`.collab/drafts/\`、\`.collab/product/\``
- architect `:22`：现值 `- 写域：\`.collab/drafts/{design,adr}/\`、\`.collab/architect/\`、\`.collab/drafts/proposals/\`、\`.collab/tickets/\` 票面文档（起草与按修票权修订）、开发票四字段、\`tests/\` 共写（增删改走 C1）、租约段签注与灰度判据（票内）、\`docs/adr/\` ADR 落盘写权（编号四位形态随 ES 定标）` → 新值：`- 写域：\`.collab/drafts/\`、\`.collab/adr/\`、\`.collab/architect/\`、\`.collab/tickets/\` 票面文档（起草与按修票权修订）、开发票四字段、\`tests/\` 共写（增删改走 C1）、租约段签注与灰度判据（票内）、\`docs/adr/\` ADR 落盘写权（编号四位形态随 ES 定标）`
- qa `:22`：尾段 `\`.collab/drafts/proposals/\`` → `\`.collab/drafts/\``（余一字不动；该行 `\`.collab/audits/\`` 经本次迁移由悬空变实存）
- engineer `:22`：`\`.collab/drafts/deploy/\`` → `\`.collab/drafts/\``（余一字不动）
- lead 卡零触碰（无相关字面）。

### A4 规范真源 `skills/sop/references/collab-fixed-structure.md`

- `:10` 桶名闭集行：`decisions/ qa/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/`＋README 索引件 → **`decisions/ audits/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/ drafts/ adr/ architect/ product/ ledger/`＋README 索引件**（16 桶；＋`drafts/ archive 子包条款`新行：「`drafts/` 顶层直接落交接件草稿、无分子包；唯一例外子包＝`drafts/archive/`（过期版本归档，见裁定③）；每交接件在 drafts 顶层只存一件存活态最新版」）。
- `:16` 入库面行：`decisions/`、`qa/`、`receipts/`… → `qa`→`audits`，并补 `drafts/`、`adr/`、`architect/`、`product/`、`ledger/` 入入库面（ledger 补链＝裁定⑤）。
- 依据注记段 append 一行：「六目录＝需求最终确认前阶段标准界定（裁定 2026-11-08 `b8bdadc`）；桶闭集换代 11→16＝同裁定结构落改」。

### A5 README 成文两件

- 新建仓根 `.collab/README.md`：内容＝桶总表（六标准目录逐行「目录·放什么·谁法定写」照裁定 §三 目标态表誊入＋表头注「六目录＝需求最终确认前阶段的标准界定，非全生命周期闭集」＋未列子包存续条款＋仓根性质注：仓根 `.collab/`＝本仓治理史面，无席位写权机检（seat-permissions 只辖软开团包内席位），落件按惯例＋decisions 归口）。
- 包内 `.collab/README.md`：桶名录行改与 A4 新闭集逐字同值；入库/排除两制行随动；首行「现行在途案卷暂在仓根」注保留（事实态）。

### A6 `.gitignore` 注释随动（行为零变款）

- `:13` 注释行 `qa` → `audits` 一处；正文排除面无 qa 字样＝零行为改动（回执附 `git check-ignore -v` 前后同值读数对拍：`agent-experts/baigong-software-team/.collab/audits/x.md` 两态均不 ignore）。

## 3 施工规格 B 组：目录实体（迁移与补链）

1. **audits 改名两处**（git mv 保 blob sha 逐件零变）：`git mv .collab/qa .collab/audits`（恰 8 tracked）；`git mv agent-experts/baigong-software-team/.collab/qa agent-experts/baigong-software-team/.collab/audits`（恰 230 tracked）。
2. **adr 单立＋四件迁入**：包内 `.collab/drafts/adr/` 四 tracked 件 `git mv` → 包内 `.collab/adr/`（drafts/adr 子包目录随 mv 清空消失）；仓根 `.collab/adr/` 本批不建空目录（见 B4 注）。
3. **ledger 补链**：`git add` 恰三 untracked 文件（§1.2 点名），入账即链态＝记账面脱链异常消除（裁定⑤）。
4. **architect 补建（包内）**：`mkdir` 包内 `.collab/architect/`＋落一件 5 行内索引占位 README（桶用途一句话＋「实体随首件架构过程件落位」）——空目录不入 git，占位件＝机械断言 `git ls-files` ≥1 可验。**仓根六子集从简条款**：仓根＝治理史面无写权机检，本批只落有实物对象者（audits mv＋ledger 链＋README），drafts/architect 空仓不建，首件届时自然落位（理由：空目录不入链＝断言不可验＋YAGNI）。
5. **drafts 顶层化＋归档子包（我定形态＋理由，候裁③可推翻）**：归档子包落位＝**`drafts/archive/`**（包内）。理由：①归档对象＝drafts 过期版本，与 drafts 同域同主（起草席自身换版＝旧版 mv 进 `drafts/archive/`＋新版落顶层，一次租约闭环，无需 host 搬件——若复用 `.collab/archive/` 则该面归 host 写域，每次换版跨席搬件违反最小授权）；②`drafts/archive/` 天然被四席 write_globs 行 `.collab/drafts/` 前缀命中（lease-issuer `:130` startswith 校验实测语义），零新增配置行；③与 host `.collab/archive/`（退役定稿落位）语义分域不混。现 drafts 顶层零散件＝无需存量归位动作；条款为前向纪律。
6. **tests 三件样例随动**（drafts/prd 废止的机械必然）：`drill-05` `:22/:27/:49` 三处 `.collab/drafts/prd/tmp-drill05.md` → `.collab/drafts/tmp-drill05.md`（`:17` 注释行 `drafts/prd` 字样随改）；`drill-06` `:20` 同款一处；`test_lease_instantiation.py` `:95/:96` 两处 `.collab/drafts/prd/` → `.collab/drafts/`。

## 4 声明闭集（OA-D6-5 机检源·逐行完整路径）

- agent-experts/baigong-software-team/config/seat-permissions.json
- agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json
- agent-experts/baigong-software-team/agents/software-team-product.md
- agent-experts/baigong-software-team/agents/software-team-architect.md
- agent-experts/baigong-software-team/agents/software-team-qa.md
- agent-experts/baigong-software-team/agents/software-team-engineer.md
- agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md
- agent-experts/baigong-software-team/.collab/README.md
- .collab/README.md
- .gitignore
- agent-experts/baigong-software-team/tests/acceptance/drills/drill-05-freeze-recover.sh
- agent-experts/baigong-software-team/tests/acceptance/drills/drill-06-replay-reconcile.sh
- agent-experts/baigong-software-team/tests/s2/test_lease_instantiation.py
- （mv 面 242 件＝8＋230＋4，由 mv 命令整目录承载，逐件新路径＝旧路径名改，回执附 `git show --name-status` 全量 R 行计数对钉 242）
- （add 面 3 件＝§1.2 ledger 三文件点名）

## 5 机械可验判据（施工回执必附实测）

1. **JSON 合法**：两 config `python -m json.tool` exit 0；两文件五席 deny_globs 数组逐席全等（SRC4Z 同批同值约束复用）。
2. **grep 钉值**：`git grep -c "drafts/prd\|drafts/design\|drafts/adr\|drafts/proposals\|drafts/deploy" -- agent-experts/baigong-software-team/config agent-experts/baigong-software-team/agents agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md` ＝ **0**（配置/席位卡/规范真源三面新名齐）；`git grep -c "collab/qa" -- "agent-experts/baigong-software-team/config"` ＝ 0。
3. **ls-files 断言**：`git ls-files | grep -c "/\.collab/qa/\|\.collab/qa/"` 路径面＝0；`.collab/audits/` tracked 计数＝8＋230＝238；`.collab/adr/` tracked＝4；`.collab/architect/` tracked≥1；ledger 三文件 tracked 态。
4. **mv 保真**：`git show --name-status` R 行＝恰 242（8＋230＋4），全 R100（内容零变·`-M` 检测）；抽验四件 adr 新旧 blob sha 全等（`git cat-file blob` 双点对拍）。
5. **门禁零回归对拍**：run-gates `--no-write` 现开工基线＝GATE PASS exit 0／发现 31,875（本票开工时点实跑）——施工后复跑须 **GATE PASS 不翻红**；发现计数按窄口径（GATE PASS 行「发现 N 条」单一真源，参并案票 B3 条款）如实登记前后两值＋差值归因（mv 面 242 件文件名变→路径型 advisory 行改名不减不增＝预期差值≈0，非零差值须逐条归因，不得「基本通过」式糊账）。
6. **drill/s2 三件复跑**：`bash drill-05-freeze-recover.sh`、`bash drill-06-replay-reconcile.sh` exit 0（演练面自夹具，仓内跑前确认租约夹具路径随 A6 改后自洽）；`python tests/s2/test_lease_instantiation.py` 直跑 exit 0（S2 夹具自跑形制在册）。
7. **check-adr 零扰**：`agent-skills/object-audit/scripts/check-adr.py` 现态 exit 0／docs/adr 盘上件=1／桶1=1 桶2=20 桶3=1——本票不动 `docs/adr/` 一字，复跑读数须同值。

## 6 禁动面闭集（点名）

- `docs/adr/`（终写位＝裁定②明文不动）；`docs/**` 全部；`.archive/**`。
- 历史案卷**内文**一切旧路径引用（`.collab/qa/` 290 行／`drafts/adr` 26 行存量措辞）——append-only 不回改（新名生效点起按新名落；全量追改与否＝候裁①）。
- `agent-skills/fuxi-skill/.collab/qa/`、`agent-skills/external-advisor-collab/.collab/qa/`（技能包自有案卷面）——是否同批改名＝候裁①射程，本票默认不动。
- 仓根 `.collab/` 根面散件 20 件＋`tmp-w7-msg.txt`＝候裁②，本票不搬不删。
- `run-gates.sh`／各 check-*.py／`write-guard.py`／`lease-issuer.py`／`publish.py` 等门禁与机件本体＝零触碰（本票改其消费的配置面，不改机件）。
- 三同源版本号（`plugin.json`／`bundle.lock`／`.codebuddy-plugin/plugin.json` 现均 0.1.30）＝本票零 bump（候裁④）。
- SEMGV-T3 案写集（五卡各一行的 T3 挂载句／bundle.lock／注册面 plugin.json／sop SKILL.md／claim-commitment-governance 七件）＝本票不预写 T3 挂载句；A3 席位卡改动与 T3 挂载句的交叠处置＝候裁⑤票间序，两案条款互不污染。
- `.collab/tickets/` vs `.scratch/tickets/` 票面住址裁定（审计件 §四.2 遗留子选项）＝候裁⑥，本票票面仍按近期体例落 `.scratch/tickets/`。

## 7 候裁面单列（本票不自行拍，逐条给规格供裁）

**候裁① 存量历史案卷迁移射程**：两案供裁——
- 案甲＝全量 `git mv` 之外再追改史文内文引用（290 行 qa＋26 行 drafts/adr＋其余包 48 件 qa 面）：指针全实但违 append-only 先例、且 24,193 级 pointers 存量噪声面重排成本高；
- 案乙＝**新名生效点起按新名、旧文不追改**（主理人倾向·append-only 先例同构）：悬空旧路径按存量噪声照登（既有 BLOCK 存量 2.4 万同族），check-pointers 对旧文命中不新增处置成本。
- 本席规格建议＝案乙＋补充件：仓根/包内两份 README 各加一行「历史案卷内 `.collab/qa/` 字样＝改名前旧路径，读作 `.collab/audits/`」去歧义句（一行级，不改史文）。其余技能包（fuxi 46＋EAC 2）qa 面是否同名实对齐并入本裁：建议**并入案乙同批 mv**（名实对齐判据同源），或单列下一批——供裁。

**候裁② 仓根 .collab 治理史散件 20 件＋tmp-w7-msg.txt 处置**：规格＝20 件按性质归 `decisions/`（收口登记／呈拍／裁定／清单类逐件点名清单见附页 A〔起草时可补〕）＋`tmp-w7-msg.txt` 删除（untracked 临时物，非链上对象，rm 即可）；或全部照旧＋README 注明散件惯例。归裁。

**候裁③ 归档子包精确落位**：本票 §3.B5 已给方案（`drafts/archive/` 包内＋三条理由）；替代案＝复用 host `.collab/archive/`（跨席搬件代价在册）。归裁。

**候裁④ 版本号三同源是否随批 bump**：本票默认**零 bump**——理由＝配置面随动批不改变包对外行为面（席位写域路径属内部工序面）；且升号排期归 PROJINIT 合并批（裁定②③④在册）＋SEMGV 系列放行后的合并升号窗口，另起 bump 会撞排期。若裁定要求随批 bump，三同源＋changelog 同批条款另出。归裁。

**候裁⑤ 票间互斥（SEMGV-T3 × COLLAB-STRUCT-1 席位卡写集交叠）**：实测交叠面＝四席位卡 `:22` 写域行——T3 v2（`b4a75d5`·候皮总放行未施工）写集含五卡各**追加一行挂载指针**；本案 A3 改四卡 `:22` 写域行本身。两笔落同文件相邻行＝git 可串接（不同行零冲突），**真风险＝语义序**：T3 先行则 STRUCT 按新卡现态重算锚；STRUCT 先行则 T3 票面钉的五卡 sha 基线（77/46/47/49/49＋sha 前 12）全部作废须 rev。本席分析＝**先 T3 后 STRUCT**（T3 已候放行＝在途末笔；STRUCT 开工基线按 T3 落链后五卡终态重取，改动小一侧承担序差）。条款＝STRUCT 施工票开工读数须复点五卡现态，若链上出现 T3 施工笔即以其为基线。归裁确认序。

**候裁⑥ 票面住址成文**（审计件遗留）：`.collab/tickets/`（规格名）vs `.scratch/tickets/`（实际体例）二选一入 README/规范表。本票按近期体例走 `.scratch/tickets/`；成文归裁。

## 8 票间关系（票包全景）

- `COLLAB-STRUCT-1`（本票）＝结构落改主票：§2 A 组成文＋§3 B 组实体，同批一施工 commit（两笔封顶内工程师落施工票另计）。
- `COLLAB-STRUCT-B345`（并案维护票·落 software-orchestration 随包技能域）＝B3 BLOCK 计数宽窄口径单一真源钉死＋B4 scratch 取证清理规程行＋B5 任务清单对账条款化（轻档已行，重档入席位 MD 给建议）。写集＝`skills/software-orchestration/references/` 三件＋SKILL.md 索引行，与 STRUCT-1 写集**零交叠**（除 `collab-fixed-structure.md` 归 STRUCT-1 独占）——两票可并行起草、串行施工亦可。
- 与 `SEMGV-T3`＝候裁⑤票间序约束，条款互不污染（两案面各自引用真源）。

## 9 完工定义与三态明示（逐条分开写）

1. **做了但没落盘**：本票起草期三真源全文直读（`git cat-file blob`）、配置/席位卡/规范/夹具/tests 消费面只读实测（wc/sha/grep/mv 计数/run-gates 基线）——均仓内只读命令，仓内零临时脚本零中间文件。
2. **落盘了但没提交**：本件写入 `.scratch/tickets/` 后至 `git add` 前为工作区新文件态。
3. **提交了但没对账**：commit 后至完工回报给出「status 他案照登＋`git show --name-only` 恰本件」实测前此态存在；由完工回报补齐，不预标「已完成」。

- **完工定义**：票面单笔 `collab:` commit 落账＋回报附 sha／行数／字节／sha256＋落笔前自查勘正登记＋三态明示。
- **纪律**：双侧 pathspec 限定本件；禁 `git add -A`／`--amend`／`reset`／`--no-verify`；他案在制品照登不碰；门禁 advisory 照常；纯规格零施工——本票不 mv 一件、不改 config 一字、不补链 ledger、不建目录。
- **本件 commit sha 与提交后态**由完工回报实测给出，正文不预写自指值。

---

## 租约段（架构席签注 · 由 B2 实例化）

```
lease:
  ticket: COLLAB-STRUCT-1-v1
  seat: architect
  author_seat: arch-commitment-design
  path_globs:
    - .scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v1.md
  deny_globs:
    - docs/**
    - .archive/**
    - agent-skills/**
    - agent-experts/**
    - softwares/**
    - tests/**
    - "*.py"
  note: 本票只出 COLLAB-STRUCT-1 结构名实对齐与规范成文规格票面 v1 一件，零施工；不 mv 目录、不改 seat-permissions/席位卡/config/gitignore 一字、不补链 ledger、不建目录、不 bump 版本。依据＝皮总裁定 b8bdadc（drafts 子包废止／adr 单立／architect 补建／audits 名实对齐／ledger 补链／未列子包存续／六目录＝需求最终确认前阶段界定）。候裁六项单列不自行拍（存量迁移射程／散件处置／归档落位／版本 bump／与 SEMGV-T3 票间序／票面住址）。两笔封顶；落链即停候双席审。
```