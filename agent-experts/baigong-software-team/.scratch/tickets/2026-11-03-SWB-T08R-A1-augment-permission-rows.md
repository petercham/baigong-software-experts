# SWB-T08R-A1 · 施工输入增补件：权限表补行（host `.collab/decisions/` ＋ architect `docs/adr/` 写域与 deny 开口三件套）——与 T08R 同票同批施工

- 起草实测 HEAD：`f135855`（票面落位＋T07/T08R 放行裁定笔）。开工 ANCHOR 义务＝开工时实测 HEAD 为 `f135855` 或其后可达后继，读数附回执开端。
- 件型＝**增补施工输入件（A1）**，体例裁量登记：取「新建 A1 件」案、弃「T08R 票面原地 append」案——放行主体＝T08R（`4082ff3`）票面已过双席审票与皮总放行，append 会破坏被核对象对位；取新建保版本链完整（同 ES v3.1 新建先例，`4eb6e55`）。**T08R 票面本体零改动**；本件与 T08R **同票同批施工**（一次 commit 落两件规格全部行位），读数冲突处以本件合账读数为准（见「合账」节）。
- 上游依据（全部现盘直读）：
  - 放行裁定＝`.collab/decisions/2026-11-03-皮总裁定-票面落位scratch与T07T08R放行.md`（`f135855`）§二.3：「补行系 ES 收口后新增设计，T08R 起草在先不含此内容＝须架构席（作者席）出 T08R 施工输入增补后工程师方可施工 T08R」；
  - ES 终态收口登记（`28381a6`）§四-3：seat-permissions 两 config 补行＝与 T08R 同票＋**两行必须同批**；
  - ES v3（`e1de307`）§三随动目＋v3.1（`4eb6e55`）§二归口表；PM 注记③原文＝`.collab/qa/2026-11-03-PM-ES-v3-快验销账-v1.md` L36（deny `docs/**` 改**显式枚举三件套**＝`docs/PRODUCT.md`/`docs/ARCHITECTURE.md`/`docs/STRUCTURE.md`，裁定三§二点九根名录闭集恰好可枚举；闭集扩员时 deny 枚举同批随动）；
  - QA N-1（v3.1 §二 L61）：枚举式 deny 开口对 docs 未来新子面 fail-open 向→**docs 面枚举闭集断言随同票登记**（本件 A1-J4 落实轻量守卫版）。
- 计数口径：occurrence 口径；判据命令自带落盘重定向；负例一律 exit≠0；行号＝起草实测现盘物理行号（锚 `f135855`），开工复测位移则以逐字文本锚定位。
- Temp 条款（承 T08R）：仓外 Temp＝`T08R_A1_TMP` 由调用方注入，**必须 Windows 盘符形态**（例 `D:/…`）；禁 `/tmp` 与挂载形态。

## 声明闭集（1 件·本笔唯一可写面）
- 声明闭集：
- .collab/tickets/2026-11-03-SWB-T08R-A1-augment-permission-rows.md

（注：本闭集＝本**起草笔**可写面；**施工笔**可写面＝T08R 票面声明闭集 6 件原样不变——A1 补行全部落在其中两 config 内，无新增文件，闭集零扩员。）

## 逐条施工规格（Aug 系列·与 T08R-A/B/B2/C/D/E 合并按 config 文件一次落笔）

### Aug1 host 行补 `.collab/decisions/`（裁定登记族誊录权落盘面）

`config/seat-permissions.json` host 行 `write_globs`（物理 L13）＝在 T08R-B 账一②拆行后的 14 行序列尾追加一行：
`".collab/decisions/"`
- 语义账＝ES v3 §三.3「不变目」＋T-A 三族分权：裁定登记族落盘权＝主理人（誊录），本行为其数据面授权；判词族（verdicts.md）与 ADR 正件族不在本行（后者见 Aug2）。
- 写侧无拦截：host 现 `deny_globs`（L16）＝`["deliverables/**", "tests/**", "docs/*（除转正代写通道）"]` 不含 `.collab/` 任何行——decisions 域签发（Aug 后）＋租约在册即 allow（探针 Q-e exit 0 佐证签发面；写侧经既有 decide 链无 deny 命中）。
- hooks-map host 行 `deny_globs` 零动（同源断言 t13 天然绿）。

### Aug2 architect 行补 `docs/adr/` write_globs＋deny 开口显式枚举三件套（PM 注记③形态）

`config/seat-permissions.json` architect 行（物理 L29–36），两改**必须同批同 commit**：
1. `write_globs`（L31）＝T08R-B 账一③拆行后的 8 行序列尾追加一行：
   `"docs/adr/"`
2. `deny_globs`（L34）现值（逐字）：
   `"deny_globs": ["docs/**", ".archive/**", "deliverables/**", ".collab/audits/**"]`
   替换为（`docs/**` 出列→三件套显式枚举直书，其余三行零动）：
   `"deny_globs": ["docs/PRODUCT.md", "docs/ARCHITECTURE.md", "docs/STRUCTURE.md", ".archive/**", "deliverables/**", ".collab/audits/**"]`
3. 该行增注记键 `deny_globs_note`（新键，t13 不断注记键＝无害）：
   `"deny_globs_note": "docs deny 开口＝PM 注记③显式枚举三件套（裁定三§二点九根名录闭集）；闭集扩员＝deny 枚举同批随动（注册/配置面同批清零纪律）；三件套外 docs 子面（含 docs/adr/）不入 deny，其防护＝签发面写域子集校验＋写侧『路径∉当席租约』双兜底——起草探针 Q-b/Q-c/R-i 实证无 fail-open 窗口（QA N-1 处置，A1-J4 在位断言）。"`
4. `config/seat-permissions-hooks-map.json` architect 行 `deny_globs`（L20）＝与源件同值同批更新（s4 t13 派生同源断言随两文件一致而绿）。
- 语义账＝ES v3 §三.2「architect 补 `docs/adr/` write_globs＋deny 同步开口」＋裁定 `5358ea4` ADR 正件族落位＋§二点九三件套定名；`.collab/drafts/adr/`（设计草稿面）与 `docs/adr/`（ADR 正件族）两族并存＝ES 三族分权既定，不构成重复授权。
- **三件套在现盘 docs 不存在**（现盘 docs 顶层＝README.md/process/research·B 批迁移落位）：三行 deny 对现盘零命中＝无害前置在位；现盘 docs 子面（process/research/README.md）不在 architect 写域→签发面 REJECT＋写侧 ∉租约兜底（探针 Q-c/Q-d 实证），无过渡期敞口。

### Aug3 E-ADR-4 基名引用式钉锚（QA 注记 b·登记式条款）

ES 判据 E-ADR-4‴ 落任何门禁/校验票时，其 adr 基名引用式**一律钉**：
`\b\d{4}-[A-Za-z0-9._-]+\.md`
（钉锚源＝ES 终态收口登记 §三 QA 注记 b；本件＝T08R 同票批的引用权威面——门禁挂载属 60-gates 路由裁量面（QA N-2 归口），不在 T08R＋A1 闭集，本条为字面钉死登记，后续票引用不得改写。）

### Aug4 docs 面枚举闭集断言（QA N-1 同票登记·A1-J4 实体）

见判据节 A1-J4——「docs 前缀机械写行集合闭集」在位断言，随本批验收跑，防枚举式 deny 开口对未来 docs 子面的 fail-open 向。

## 两行同批的机理实证（起草探针落盘＝`D:/arch-swbfix-t08raug-probe/probe.out`＋`probe2.out`·Windows 盘符形态）

write-guard decide 顺序＝deny 先行（write-guard.py L204–208）→租约兜底（L210–215）；lease-issuer 零裁量子集校验（lease-issuer.py L70–71）。据此：
- **半批 Y（只开 deny 不补 write_globs）**＝签发面 REJECT：`docs/adr/0001-t.md` → **exit 2**「越出席位 architect 写域行」（Q-g 实测）——写权落空；
- **半批 X（只补 write_globs 不开 deny）**＝写侧被 `docs/**` 吞：喂 architect 身份＋`docs/adr/` 租约 → **deny**，原因行 `glob='docs/**'`（R-i 实测）——ES「新立残留窗口」预言在机械层复现；
- **全批（两行同改）**＝签发 `docs/adr/0001-test.md` **exit 0**（Q-a）／写侧同路径 allow（P-e·stdout 无 permissionDecision）／`docs/PRODUCT.md` 签发 exit 2（Q-b）＋写侧 deny `glob='docs/PRODUCT.md'`（P-f）＝正负双侧对位。
- 对照基线：现盘（未增补）architect `docs/adr/` 签发 **exit 2**（Q-h）＝缺陷在基线存在、A1 批修复；host `.collab/decisions/…` 签发 exit 0（Q-e 增补构型）。
- 探针注记：`lease-issuer` 的 countersign 校验先于子集校验——判据签发命令必带 `--countersign architect:<sig>`，否则 exit 2 语义错位（T08R c3 同形制）。

## 合账（单一账·T08R 原账与 A1 增补合并复算·勿两套账）

起草探针 python 复算（机械化判定标准 v2 正则＝T08R 定义）：

| 口径 | 总行 | 非机械 | 逐席（总行/非机械） |
|---|---|---|---|
| 现盘基线（`f135855`） | 34 | 14 | host 13/4·product 3/0·architect 7/5·qa 4/2·engineer 5/2·human 2/1 |
| T08R 原账一后（票面 P-regex 申报） | 34 | 10 | host 14/3·product 3/0·architect 8/4·qa 4/2·engineer 3/0·human 2/1 |
| **T08R＋A1 合并后（权威读数·覆盖 T08R 判据 2 申报值）** | **36** | **10** | host **15**/3·product 3/0·architect **9**/4·qa 4/2·engineer 3/0·human 2/1 |

即：A1 增两行机械行（host＋`.collab/decisions/`、architect＋`docs/adr/`），非机械数不变＝10。T08R 判据 2 的「账一后 34/10」读数由本表第三行取代（判据 A1-J5 实体）；T08R 判据 2 的开工基线读数（34/14）不变。

## 判据增补（A1-J 系列·全部机械可判·命令自带落盘·负例 exit≠0）

- **A1-J1 数据面补行断言**：python 内联读两 config：host `write_globs` 含 `.collab/decisions/`（occurrence＝1）且 host 总行数＝15；architect `write_globs` 集＝{拆行后 8 行}∪{`docs/adr/`}（恰 9 行）；architect `deny_globs` 六行**全等**上列新值；`docs/**` 串在 architect 行（两 config）occurrence＝0；map architect `deny_globs` 与源件全等 → 全断言 exit 0 → `$T08R_A1_TMP/j-a1-1.out`。
- **A1-J2 签发面正负例**：`lease-issuer --seat architect --countersign architect:probe --path-glob "docs/adr/0001-probe.md"` → exit 0；同形制 `docs/PRODUCT.md`→exit≠0；`docs/process/probe.md`→exit≠0；`--seat host --path-glob ".collab/decisions/2026-11-03-probe.md"` → exit 0（四条逐条 exit 码 echo 落 `$T08R_A1_TMP/j-a1-2.out`；开工基线同式＝第一条 exit≠0/第三条 exit≠0/第四条 exit≠0，施工后不得反向）。
- **A1-J3 写侧两读数**：Temp 直写租约行（`{"ts":"t","lease":{"ticket_id":"A1J3","seat_id":"architect","path_globs":["docs/adr/"],"hash":"h"}}`）＋`write-guard --path "docs/adr/0002-probe.md"` 喂 `{"agent_type":"software-architect","agent_id":"software-architect-a1"}` → stdout 无 `"permissionDecision"`（allow·不自造词）；`--path "docs/PRODUCT.md"` → deny 且原因行含 `glob='docs/PRODUCT.md'` occurrence＝1 → `$T08R_A1_TMP/j-a1-3.out`。
- **A1-J4 docs fail-open 守卫断言（N-1 实体）**：python 断言三件：(a) 全席位机械 `write_globs` 中以 `docs/` 起始的行集 ⊆ {`docs/adr/`}（任何新 docs 子面写行＝exit 1，除非随批入枚举＝闭集扩员纪律的机检面）；(b) architect `deny_globs` 三件套字面 occurrence 各＝1；(c) 现盘 `git ls-files docs/` 顶层子目录（`adr` 除外）逐名拼探针路径喂各席机械写行，任何命中 → exit 1 → `$T08R_A1_TMP/j-a1-4.out`（现盘预期全绿：process/research/README.md 对 architect 写域无命中）。
- **A1-J5 合账复算断言**：按机械化判定标准 v2 正则复算＝总行 **36**、非机械 **10**、逐席分布＝合账表第三行逐值 → exit 0 → `$T08R_A1_TMP/j-a1-5.out`（开工基线同式 34/14 先跑先落盘对照）。

### T08R 原判据随动改（读数取代清单·判据编号不动）

| T08R 判据 | 随动 |
|---|---|
| 判据 1（数据面断言） | engineer 断言零动；**增** A1-J1 断言并入同跑（或并跑两文件，读数并呈） |
| 判据 2（机械审查） | 施工后读数 34/10 → **36/10**（合账表）；开工基线 34/14 零动 |
| 判据 8（s2/s4 回归） | 零改（s4 t13 随两 config 一致更新绿；s2 六席位行断言与 engineer deny len 断言零触及） |
| 判据 10（版本三同源） | 零改——**A1 不独立 bump**：补行与 T08R 同批一次 bump（0.1.14→0.1.15，或 T07 先落则 0.1.15→0.1.16，前后值各附实测） |
| README 版本账 append 行 | T08R 原句扩为：「权限表数据面机械化（SWB-T08R＋A1）：engineer 写域参数化＋deny 唯二落实＋hooks-map 新五身份补行＋host 裁定登记誊录权＋architect ADR 写域与 docs 三件套枚举开口，依据＝皮总裁定 ff72b92/18bf840/5358ea4＋ES 终态收口 28381a6」 |

## 施工合并说明（给工程师席）

- 一次施工 commit 落 T08R＋A1 全部行位于闭集 6 件内：seat-permissions.json（engineer 行 A 段＋B 账一 host/architect 拆行＋Aug1＋Aug2）、hooks-map（B2＋C＋Aug2.4）、三版本件＋README（D 段合并句）。T08R 判据 0–11＋本件 A1-J1–J5 全绿＝批次验收。
- 建议行位施工序：先 T08R 账一拆行（host/architect），再 Aug1 尾追加，再 Aug2 两改——避免锚串二次位移。

## 禁动面（零触碰）
- ES 设计真源四件（v1/v2/v3/v3.1）零改动（ES 版本链纪律）；`docs/` 全域（三件套实体＝B 批落位，本批不造文件）；席位卡五新件（ES §四-1 卡面誊录权/写权明文＝卡面随动票，与 T08R 候裁 R⑥ 同域，**不在本批**，候裁呈报见下）；`write-guard.py`/`lease-issuer.py` 机制代码零触碰；T08R 票面本体零改动；`table_notes`/`explicitly_not_writable`/其余四席 write_globs 零动（architect `explicitly_not_writable` 含 `"docs/"` 字符串列＝表2-1 转录面，与机械 deny 面分层，随 B4 再锚对表＝既有候裁 R⑨ 同型，不自行消解）。
- 不自判合格（制度③）；工程师不得改本件票体四字段与验收行。

## 候裁点（单列·不自行拍）
- **A1①** ES 终态收口 §四-1 席位卡面（主理人卡誊录权明文＋架构席卡 `docs/adr/` 写权句）＝卡面执行规范随动票归属——与 T08R 候裁 R⑥ 同域合并呈裁（数据面 A1 已先行，卡面句未裁前卡零触碰）。
- **A1②** architect `explicitly_not_writable` 列含 `"docs/"` 与 Aug2 枚举开口的设计基线偏差——随 R⑨ 同笔呈 B4 票包再锚追认（本批不自行改表2-1 转录面）。
- **A1③** 三件套实体缺位过渡期（docs 现盘＝README/process/research）：deny 三行无害前置＋双兜底在位（探针实证），B 批三件套落位后自然全活——是否需过渡期 README 索引注记＝主理人裁。

## 回执
落 `.collab/receipts/2026-11-03-SWB-T08R-A1-receipt.md`（随 T08R 回执同批或随后单独笔）：开端 HEAD 实测＋A1-J1–J5 逐条命令与读数（含开工基线 j-a1-2 前值对照）＋合账表三行复算读数＋候裁 A1①–③逐条呈裁原文引用。本起草笔单独 commit `collab:` 前缀只含声明闭集 1 件；禁 `--no-verify`、禁 amend；pre-commit 门禁真拦时如实报告拦点并在闭集内修正重过，不得绕闸。
