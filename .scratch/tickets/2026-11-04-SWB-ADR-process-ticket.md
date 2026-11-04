# SWB-ADR · 施工票：ADR 工序票（工序节点成文＋会签承载＋票型归道＋席位卡文法随动）（施工票·L2·架构席起草·已确认链执行类）

- 起草实测 HEAD＝`d85ddc7`（吞笔事故登记笔）；开工 ANCHOR＝开工实测 HEAD ≥ `d85ddc7`，读数附回执开端。
- 决策真源＝决策者已确认 ADR 工序链（主理人派工在案）：**人类输入决策 → 主理人誊录登记 → 产品席＋QA席＋架构席会签 → 架构席对四方收口草案做终写（写入 docs/adr/）**；两条已声明执行条款（甲/乙）见 §条款区。本票＝该已确认链的工序成文执行，**决策本身不再审**。
- 裁定登记核对：盘上直读 `.collab/decisions/` 现无「ADR 工序链确认」登记件（grep 实测＝免拍板裁定 L19 仅点名「ADR 工序票候皮总拍板」）——**皮总「确认」誊录登记＝本票开工前置**（誊录权＝主理人·lead 卡 L76），登记笔未落前禁开工（候裁④在册）。
- 缺口真源＝架构席对照评估件 `.collab/design/2026-11-04-SWB-ADR出口节点归属-架构席对照评估-v1.md`（缺位 G-1～G-7 全表）；外部证据＝`.collab/research/2026-11-04-ADR归属范式调研-产品席-v1.md`（R1–R13）＋`.collab/research/2026-11-04-ADR归属范式调研-补核席位节点绑定-产品席-v1.md`（R14–R21：MArc 先批准后记录／MAD-Arch approval gate 问责决策人——终写＝owner/champion 认领担责语义，非执笔权）。
- 体例先例＝B 批票面族（声明闭集/逐条落位/机检判据/禁动面/候裁区五段齐）；纯誊写条款先例＝`f5a0d96` 誊写禁令链。
- 计数口径＝occurrence（occ）；判据自带落盘重定向（Temp·仓内零运行残留）；负例 exit≠0。

## 现盘落位实测（起草取证·回执附开工复测）

1. **基线锚行**（`agent-experts/baigong-software-team/docs/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md`·登记件哈希自锁件·L5 全文 sha256 声明在案）：§3 票型八类句＝物理 L141；表2-3 节点 2 行＝L131、维护行＝L136；§12 通道四类句＝L205、基线技术落实修订生效制＝L206。**该件为哈希自锁登记件——任何追加使 L5 声明哈希失配＝文法事件须处置（候裁①）。**
2. **数据面现状**：`config/ticket-types.json` types＝八类无 ADR（L3–12）；`config/ticket-authors.json` authors 键集＝同八类（同源断言＝T03 验收判据 2）；`config/dispatch-spec.json` nodes＝6 节点＋维护行（实测 keys：node1–6/维护·节点1-3），无 ADR 行；`docs/STRUCTURE.md` 无 ADR 条目（grep 零命中）；五席位卡现态＝architect L22 写域含 `docs/adr/`、L24「明确不可写：`docs/`」（G-7 文法张力在案）；`skills/software-orchestration/references/standard-sop.md` 无 ADR 工序节（grep 零命中）。
3. **写通道实核（谁能在施工期写哪）**：config/**、agents/**、skills/** ∈ engineer write_globs（租约 path_globs 授权下可写）；`docs/STRUCTURE.md` ∈ architect deny 枚举（seat-permissions L36）且不入任何席 write_globs——**基线件与 STRUCTURE 的追加笔当前授权面无路**（转正代写通道＝manifest 状态机专用，与本票无 manifest 在案）＝候裁②登记，不自行开权。
4. **docs/adr/ 在盘态**：项目 docs/adr 目录未建（find 全仓仅外部快照残留＝RET 已处置面）；版本面 `git ls-tree -r HEAD | grep "docs/adr/"`＝0；ES2 收口登记 §三双前置在册（①首支 ADR 实际落 docs/adr/②触发批同批实装 60-gates 挂载与 E-ADR-3″）——**目录初始化与门禁挂载不入本票正文，候裁③单列**。
5. **token 基线**（`tools/count_agent_tokens.py`·ES2 后五值）：1533/942/1115/1044/860（lead/product/architect? 序按工具输出面回执复测钉值）——本票涉三卡（architect/product/qa），判据 7 设增量界。

## 声明闭集（10 件·本批唯一可写 git 面）

- 声明闭集：
- agent-experts/baigong-software-team/config/ticket-types.json
- agent-experts/baigong-software-team/config/ticket-authors.json
- agent-experts/baigong-software-team/config/dispatch-spec.json
- agent-experts/baigong-software-team/skills/sop/scripts/dispatch-builder.py（**修订笔之二扩员·红-1 选型②＝行数钉值随动件**）
- agent-experts/baigong-software-team/tests/s3/test_dispatch_gate.py（**同上·t01 钉值随笔件**）
- agent-experts/baigong-software-team/agents/software-team-architect.md
- agent-experts/baigong-software-team/agents/software-team-product.md
- agent-experts/baigong-software-team/agents/software-team-qa.md
- agent-experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md
- agent-experts/baigong-software-team/docs/adr/（**条件件·仅候裁③获准随首支 ADR 批开目录时启用；本票单独施工批禁触**）

（候裁①②获准后另行追加：交接件基线追加行、docs/STRUCTURE.md 条目——追加行文本已在本票 §规格四/五给出，落位批另起，闭集届时扩员随裁定笔。）

## 条款区（已声明执行条款·入 SOP 与卡面）

- **条款甲（终写＝纯机械誊写）**：架构师终写段逐字照录四方会签收口草案，**零文风裁量**——终写件与收口草案正文 diff 必空（哈希对等），架构席职责＝owner/champion 认领担责（R10/R11/R21 语义），不是执笔权，不是内容复审权。
- **条款乙（既会签又终写不构成自审）**：ADR 记的是四方已收敛决策，非架构单方设计稿；防自审条款（转正代写通道·制度③）辖架构正文链（docs/ARCHITECTURE.md 族），ADR 记录链与其两条路各自成文、互不管辖。

## 逐条施工规格（G-1～G-7 处置·到落位）

### G-1 票型闭集增 ADR 类（采增类案·挂靠案列候裁⑤）

- `config/ticket-types.json`：types 数组 append `"ADR"`（八类→九类）；`derived_from` 行尾追加注记「＋ADR 类（已确认链执行类·2026-11-04 决策者确认链）」——types 顺序 append，既有八类行零动。
- `config/ticket-authors.json`：authors 增键 `"ADR": "架构席（终写段＝纯誊写·条款甲）"`；`table_six_mappings_verbatim` 零动；`same_origin_closure_note` 尾追注「ADR＝九类增员·作者权直列架构席（非表注六映射来源）」。
- `config/dispatch-spec.json`：`ticket_types_note` 零动（引用式随 type 集自动同源）。
- 基线 §3 L141「票型八类」句随动＝候裁①②获准后经追加条款行落实，文本见 §规格五-2。

### G-2 会签承载位（dispatch-spec 增 ADR 节点行＝数据面承载）

- `config/dispatch-spec.json` nodes 数组 append 一节点行（形态沿维护行先例）：
```json
{"node": "ADR·落盘", "name": "ADR 工序（人类决策→誊录登记→会签→终写）",
 "signoffs": ["产品会签签", "QA 会签签", "架构会签签＋终写签（终写＝条款甲纯誊写）"],
 "human_role": "输入决策＋（登记件誊录经主理人）",
 "injection_faces": [
   {"seat": "product", "entries": [{"name": "裁决登记件（誊录态只读）", "kind": "pointer"}, {"name": "收口草案（四方会签中）", "kind": "literal"}]},
   {"seat": "qa", "entries": [{"name": "裁决登记件（誊录态只读）", "kind": "pointer"}, {"name": "收口草案（四方会签中）", "kind": "literal"}]},
   {"seat": "architect", "entries": [{"name": "裁决登记件（誊录态只读）", "kind": "pointer"}, {"name": "收口草案（会签终稿）", "kind": "literal"}]}]}
```
- 表2-3 基线随行（「ADR·落盘｜签字集合＝产品席＋QA席＋架构席（会签）＋架构终写签｜人类＝输入决策」）＝候裁①②落位；**「新设签字面」是否触发 §12 L206 门/保险丝＝候裁①单列，本票不自行豁免**。
- **行数钉值机械随动（修订笔之二补·红-1 销项·选型②）**——B 席拦红实证：`skills/sop/scripts/dispatch-builder.py` L65–66 `load_spec` 硬断言 `len(nodes)!=7→SystemExit FATAL`（L161 REJECT 文案「七行」同款字面）＋`tests/s3/test_dispatch_gate.py` L60 t01 同钉＝节点行 append 后 8 nodes 全派发 fail-closed 停摆。施工规格（三点同笔·config 笔同批或前后脚均可，机件笔先落则过渡态零窗口）：
  1. dispatch-builder.py L65 `!= 7`→`!= 8`；L66 FATAL 文案「表2-3 七行（六节点＋维护行）」→「表2-3 八行（六节点＋维护行＋ADR·落盘行）」；L161 REJECT 文案「七行内」→「声明行集内」（展示串去行数依赖）。
  2. test_dispatch_gate.py L60 断言 `== 7`→`== 8`＋f-string 文案同款换代；t01 函数名 `t01_spec_seven_rows_signoffs_nonempty`→`t01_spec_eight_rows_signoffs_nonempty`（L157 run_self 引用行同笔换代·防文法债）。
  3. dispatch-spec.json `source` 行 append 注记「＋ADR·落盘行（2026-11-04 已确认链执行类新增·基线表2-3 随行候裁①②落位）」——消「七行逐行转录」自述与八行现态的断言面破口；`derived_from: "表2-3"` 值零动（t01 L62 断言依赖）。
- **选型②理由（如实入账）**：行数钉值＝dispatch-spec 行集的**机械镜像**（不变量随数据面随动），非新设计决策——新增节点行是已确认链成文（G-2 本体），钉值 7→8 是其机械必要随动，与 spec 本体同票闭合方为零过渡态（选型①候裁单列会造「spec 已八行而机件仍钉七」的禁派发窗口，引入不必要过渡态）；写权路在盘＝config/**、skills/**、tests/** ∈ engineer write_globs（租约 path_globs 授权下可写·seat-permissions L53）。**层界厘清（顺候裁①关系）**：机件镜像层（本随动·行数事实）≠ L2 条款层（表2-3 基线行/§3 八类句＝候裁①②）——机件文案换代预对齐基线终态；若候裁①②最终否基线追加，L66 文案回落形态「dispatch-spec 八行（表2-3 七行＋ADR·落盘扩行）」随裁定笔，钉值 8 不随候裁摆动（事实源＝spec 现态）。

### G-3 ADR 修订/supersede 归道（归「同一工序链重跑」·不开第五通道）

- 归道方案：ADR 之修订/废止＝**新 ADR 走同一工序链重跑＋supersede 双向互链**（E-ADR 族机理：supersede 双向、accepted 不可变、编号四位唯一不复用·ES v3.1 在册）；**不改 §12 通道四类闭集**——L2 条款/TCB/阈值/seat-permissions 的**改权**仍归 C1 四通道射程，ADR 是其**记录面**不是变更通道（两线各自成文：内容改权走 C1，决策记录走 ADR 工序）。
- 数据面承载＝`standard-sop.md` ADR 工序节内成文（见 G-5 节文本第五段）＋基线 §12 追加注记行（文本见 §规格五-3·落位候裁①②）。

### G-5 工序节点本体＝standard-sop.md 增「ADR 工序」节

- `skills/software-orchestration/references/standard-sop.md` 尾部 append 一节（节名「ADR 工序（决策记录链）」），五段全文：
  1. 链序：人类输入决策→主理人誊录登记（`.collab/decisions/`·append-only·逐字）→产品席＋QA席＋架构席会签→四方收口草案→架构席终写入 `docs/adr/`（编号四位·Status 闭集·头块五行照 ES E-ADR-1″）。
  2. 会签语义：会签＝对收口草案的签署认可；会签席可出保留项——保留项未闭合前终写段禁启动（收口未成）。**保留项闭合归位**：保留项经主理人呈人类裁定（输入决策权恒在人类侧，三席会签不替代决策）；裁定落 decisions 登记后，草案修订＝**架构席照新裁定登记件重誊草案**（誊聚权不含裁量·条款甲语义延伸及重誊；落位仍在 `.collab/drafts/adr/` 既有写域＝零新开写域）；会签席永不改草案（deny 语义不变）。重誊后全链重走会签（同序同判据），旧会签随重誊作废不入账本终态。
  3. 终写段＝条款甲全文（逐字照录·diff 空判据）。
  4. 条款乙全文（不构成自审·两链互不管辖）。
  5. 修订/supersede 归道句（G-3 方案成文）。
- 三席位卡随动纪律行（各一行·append 于各卡纪律区）：
  - architect 卡：「ADR 终写＝纯机械誊写：逐字照录四方会签收口草案，零文风裁量；终写与草案哈希对等方可落盘；既会签又终写不构成自审（记录链≠正文链）【条款甲/乙·已确认链】」
  - product 卡：「ADR 会签权：对四方收口草案签署认可或出保留项；保留项未闭合禁终写【ADR 工序·SOP 节】」
  - qa 卡：同 product 句式（换席位名）。
- **收口草案落位与签署通道（工序面配套·零新写域）**：草案本体＝`.collab/drafts/adr/`（architect write_globs 既有桶·草案誊聚＝架构席誊录不裁量）；会签签署＝账本签字记录（账本六类·经 state-transition.py 既有通道）；会签保留项落各席既有写域（product→`.collab/product/`、qa→`.collab/audits/`）；product/qa deny 列既含 `.collab/drafts/adr/**`（hooks-map 实测在册）＝会签席不可改草案，与「签署不执笔」语义天然对齐——**两 config 零改动**。
- architect 卡 G-7 文法澄清（同卡内 L24 行**原位换代**·非纪律区 append）：「明确不可写：`docs/`（三件套及 STRUCTURE 等 docs 子面；**写域行已授权之 `docs/adr/` 除外**——其防护＝签发面写域子集校验＋写侧租约双兜底·seat-permissions architect 行注记同文）】」——机制面零改动（deny_globs/write_globs 两 config 零染），仅卡面文法与数据面对齐（消 G-7 张力）。

### G-6 STRUCTURE 增补条目（文本给出·落位候裁②）

- `docs/STRUCTURE.md` 分层列表追加条目文本：「`docs/adr/` — ADR 正件族（架构席终写落位·编号四位·永存面不入退役流程；不属于交付路径）」。
- 落位批＝候裁②（STRUCTURE ∈ architect deny 枚举＝授权面先开：C1 或裁定点名写入通道）获准后另笔；本票施工批 STRUCTURE 零触碰。

### 规格五 基线追加三行文本（落位候裁①②·哈希处置随①）

1. 表2-3 随航行（接维护行 L136 形制）：`| ADR·落盘 | 签字集合＝产品席＋QA席＋架构席（会签）＋架构终写签（终写＝纯誊写条款） | 输入决策 |`
2. §3 票型随航行：`票型九类（原八类＋ADR）——ADR 类作者权＝架构席（终写段纯誊写）；已确认链 2026-11-04。`
3. §12 归道注记行：`ADR 记录面＝工序链重跑＋supersede 互链承载，不入 L2 变更四类闭集；L2 条款改权仍归 C1 等四通道，记录与改权两线各自成文。`

### G-4 门禁/机件挂载（只登记不设计·候裁③）

- 涉脚本改动面全部候裁③单列：60-gates 挂载 `check-pointers --scope docs/adr` 类路由、E-ADR-1″/2‴/3″/4″/5‴ 校验器实装、docs/adr 目录初始化时机——全部＝ES2 双前置②射程，触发批同批实装；本票闭集内**无任何 scripts/ 与 60-gates 文件**。

## 验收判据（occurrence 口径·开工复测随回执）

1. **闭集全等**：本批 `git show --name-status <笔>` 文件集 ⊆ 声明闭集 10 件（条件件 docs/adr 在单独批未触＝零出现；交接件/STRUCTURE/两权限 config/60-gates 交集＝空——scripts 仅 dispatch-builder.py 一员·tests 仅 test_dispatch_gate.py 一员，逐笔 name-status 对账）。
2. **同源断言绿**：python 断言 `set(ticket-authors.authors.keys()) == set(ticket-types.types)` 真；三 config `json.load` exit 0；`dispatch-spec.nodes` 含 node=="ADR·落盘" 恰 1。
3. **票型钉值**：`grep -c '"ADR"' config/ticket-types.json`＝1；ticket-authors `"ADR"` occ＝1；types 长度 8→9。
4. **SOP/卡面钉值**：standard-sop.md `grep -c "ADR 工序"` ≥1 且条款甲/乙关键句（「纯机械誊写」「不构成自审」）各 occ ≥1；三卡各新增纪律行恰 1 行；architect 卡 L24 换代行含「docs/adr/ 除外」occ＝1、原「明确不可写：`docs/`」裸行 occ＝0。
5. **config 零染**：seat-permissions.json、seat-permissions-hooks-map.json 两笔零出现（`git log -1 --name-only` 对账）。
6. **基线/STRUCTURE 零染**：交接件与 STRUCTURE.md 本批 diff 零行（候裁未落）；`git ls-files agent-experts/baigong-software-team/docs/adr/`＝0（全路径口径·与声明闭集条目对齐；单独批前）。
7. **token 界**：三卡 `count_agent_tokens.py` 复测各 ≤2500 且增量（architect/product/qa）合计 **≤210**（修订笔之二上修·原 ≤180 与判据 4 锁死文本互斥＝B 席黄-1：script-v1 口径 dry-run 实测 Δ192＝arch 114＋prod 39＋qa 39 必炸）；各卡 ≤2500 无虞（architect 942→1056／product 860→899／qa 1044→1083）；五值读数随回执。
8. **负例**：构造「终写件与收口草案 diff 非空」样态跑判据 4 哈希对等断言 exit≠0（Temp 面）。
9. **纪律**：单笔单件族 `collab:` 前缀；禁 --no-verify/禁 amend；pre-commit 门禁真跑；提交前 `git diff --cached --name-only` 自证＋提交后立即 `git show --name-status HEAD` 载体对账（双闸·防吞笔·d85ddc7 事故条款）。
10. **机件兼容硬验（修订笔之二新增·补 B 席所指判据族漏检）**：施工批收笔前 `python agent-experts/baigong-software-team/tests/s3/test_dispatch_gate.py`（self-run 全 PASS·exit 0）＋`python -c "import json;d=json.load(open('agent-experts/baigong-software-team/config/dispatch-spec.json',encoding='utf-8'));assert len(d['nodes'])==8"` exit 0＋`grep -c "!= 8" skills/sop/scripts/dispatch-builder.py`＝1／`grep -c "== 8" tests/s3/test_dispatch_gate.py`≥1／REJECT 文案「七行内」occ＝0——五读数齐绿方收笔（负例＝Temp 面还原 `!= 7` 跑 t01 exit≠0 复现）。

## 禁动面

- 交接件基线件＝**哈希自锁登记件**：本批零触碰；后续追加只许 append-only 只增不改史行，且须随候裁①哈希处置裁定。
- `docs/ARCHITECTURE.md` 及转正代写通道零触碰；状态机/promote-manifest 零触碰。
- seat-permissions.json / hooks-map / scripts（**唯一例外＝dispatch-builder.py 行数钉值随动三点·见 G-2 机械随动规格**）/ 60-gates / dispatch 卷零触碰；tests 面唯一例外＝test_dispatch_gate.py t01 随笔。
- `.collab/decisions/` 誊录面＝主理人权，架构席零触碰。
- 皮总确认登记笔未落前（候裁④）整批禁开工。

## 候裁区（超出已确认链·只登记不判定）

1. **候裁①**：交接件基线追加行＝全文 sha256 声明失配的文法处置——采「勘定追记」节（文末追加三行＋重算全文哈希回填追记节·原件零动）还是另立修订登记件？**先例注记（B 席裁据补入）**＝「勘定追记」与盘上 **B4-D 先例**同构：交接件物理 L262 追认注记（SWB-B4 B4-D·2026-11-04·「尾追加不入 V13 段·append-only」）自声明＝追加区在 L261 之后、**L1–260 行号与三基线哈希不扰动**（全文 `3f3353…` 等三哈希零动）——即「文末追加区」形态在盘上已有既成先例，采此案则本票三行（§规格五）沿该形态、原件哈希零触＝失配议题自消；另立登记件案＝双件对读成本。＋会签行＝新设签字面是否触发 §12 L206 门/保险丝（皮总「确认」登记可否代签该触发）——归决策者/产品席裁。行数钉值随动与本候裁的层界关系见 G-2 节「层界厘清」段（机件镜像层已随票闭合，不候本裁）。
2. **候裁②**：交接件与 `docs/STRUCTURE.md` 的写入授权通道（现 architect deny 枚举在列、无 write_globs 路）＝需 C1 或裁定点名，先开权后落笔。
3. **候裁③**：docs/adr 目录初始化时机＋门禁常驻挂载＋E-ADR-3″ 等校验器实装（涉脚本）＝ES2 双前置②射程，触发批同批实装。
4. **候裁④（开工前置）**：皮总 ADR 工序链「确认」的 decisions 誊录登记笔＝主理人义务；登记笔哈希即本票开工 ANCHOR 随动。**状态注记（修订笔随动）＝已闭合随 `b0b449d`（拍板登记笔已落链·`.collab/decisions/2026-11-04-皮总拍板-ADR工序链确认.md`）；开工 ANCHOR＝`b0b449d` 之后**（票面 L5 起草读数行＝起草时点 d85ddc7 史实如实，不改）。
5. **候裁⑤（备选案）**：G-1 若决策者否增类案，挂靠替代＝复用「开发」票类＋票内 ADR 子型字段（authors/dispatch 零扩，基线八类句零触）——两案机检判据随案换，不夹带本票正文。

——arch-swbreloc 起草·只票面零施工·开工读数 HEAD `d85ddc7`。
