# SWB-T08 · 规则票：权限表（表2-1）数据面机械化——engineer 写域行机械形态＋全表逐行机械化审查（规则票·L2·架构席起草）

- 起草实测 HEAD：`8af5711`（SWB-T07 票面笔之后；起票链＝`6d40ece` 裁定笔→`8af5711` T07 票面笔）。开工 ANCHOR 义务＝开工时实测 HEAD 为 `8af5711` 或其后可达后继，读数附回执开端。
- 票型＝**规则票**（§12 L2 通道；修票权＝提案席位修＝架构席起草、经质量链后派工程师施工）。裁定依据（盘上直读）＝`.collab/decisions/2026-11-03-皮总裁定-SWB票包遗留三件.md`（`6d40ece`）第③项：采**选项 A**——出「权限表（表2-1）数据面机械化」规则票，把工程师行「（工作空间根∪部署路径）−受保护区」改写为机械可判形态并逐行审查全表机械化；**排在真实试运行前完成，不插队**。
- 缺陷证据（只读·判定出处）：`.collab/qa/2026-11-03-QA-T06-独立验证-v1.md` 第九节分账③＋`.collab/receipts/2026-11-01-SWB-T06-receipt.md` 呈核③：`lease-issuer.py --seat engineer --path-glob deliverables/**` → **exit=2** `REJECT: 请求路径 … 越出席位 engineer 写域行`（起草复测属实＝exit 2）；drill-05 曾改走 product 席机械声明行完成（drill-05 L16–20 注记逐字在盘）。
- 设计真源对照（登记面·只读禁写）＝`.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md`：表2-1 节＝物理 L98–107（V13 L70–79·V13 n＝物理 n−28）；工程师行＝物理 L105 逐字；「受保护区」词条＝物理 L230 §17 逐字「`docs/` 全域＋`.archive/` 全域＋`.collab/` 根中未被表2-1授权的子域」；顶层枚举款＝物理 L107「交付树（`deliverables/`）＋`docs/`＋`.archive/`＋`.collab/`＋`.git/`＋`tests/`」；路径锚定款＝物理 L106。逐字引文与真源串对位义务（T05 U7 先例教训）：施工前直读上述物理行原文，附回执。
- 计数口径声明：occurrence 口径（`grep -o | wc -l` 或 python 逐项）；判据命令一律自带落盘重定向；负例一律 exit≠0 断言。行号口径＝起草实测现盘物理行号（锚 HEAD=8af5711），开工复测若位移，以逐字文本锚定位为准。

## 机械化判定标准（本票自定机械口径·审查与判据共用）
- 机械行＝纯 ASCII 路径字面，匹配正则 `^[A-Za-z0-9][A-Za-z0-9._/*{}-]*$`（允许通配 `*`/`**`）；含 CJK、全角括注、`∪`、`−` 或花括号占位符（`{id}`/`{seat}` 类非路径语义）＝非机械行。write-guard.py `glob_match` L98–105 既有惯例同款（CJK/∪/− 检测→不参与机械匹配；全角括注剥离）。
- 行为事实基线（起草实测）：现盘非机械行在 lease-issuer L70–73 子集校验与 write-guard 匹配中**恒不命中**（字符串包含判定对 CJK 描述行永假）——故「描述行移入注记键」＝行为零变化；唯 engineer 首行替换＝真实行为变化（REJECT→放行），属裁定授权面。

## 声明闭集（6 件·本票唯一可写面）
- 声明闭集：
- deliverables/experts/baigong-software-team/config/seat-permissions.json
- deliverables/experts/baigong-software-team/config/seat-permissions-hooks-map.json
- deliverables/experts/baigong-software-team/.codebuddy-plugin/plugin.json
- deliverables/experts/baigong-software-team/bundle.lock
- deliverables/experts/baigong-software-team/plugin.json
- deliverables/experts/baigong-software-team/README.md

## 逐条施工规格

### T08-A engineer 写域行机械化（裁定核心·表2-1 物理 L105 设计语义忠实实例化）

`config/seat-permissions.json` engineer 行 L49 现值（逐字）：
`"write_globs": ["（工作空间根∪部署路径）−受保护区", ".collab/inbox/engineer/", ".collab/returns/engineer/", ".collab/drafts/deploy/", "限定当票租约路径集"],`
替换为：
`"write_globs": ["deliverables/**", ".collab/inbox/engineer/", ".collab/returns/engineer/", ".collab/drafts/deploy/"],`
并同席增一键（描述行入注记·行为零变化款）：
`"write_globs_note": "首行＝（工作空间根∪部署路径）−受保护区 的仓内机械实例化：顶层枚举款六类中，受保护区（docs/.archive/.collab未授权子域）与『明确不可写』列（仓根 tests/ 真源域）已除；交付树 deliverables/** 经当票租约 path_globs 授权（表注路径锚定＋双层双址款）；『限定当票租约路径集』＝B2 租约面行为约束（lease-issuer 子集校验承载），非路径行。",`

- 语义忠实性论证（对照物理 L105＋L107＋L230 三串）：仓顶层闭集枚举六类中，工程师「（工作空间根∪部署路径）−受保护区」在仓内的可写余集＝`deliverables/`（交付树）；`docs/`/`.archive/`＝受保护区全域、仓根 `tests/`＝该行「明确不可写」列指名、`.collab/` 其余＝受保护区——三条逐一对位该行既有 `explicitly_not_writable`/`deny_globs` 行，零新域释放。**「部署路径」＝仓外运行态位置，仓顶层枚举内无对应路径可 instantiate，不建行**（登记候裁⑤呈明，不自行拍）。
- 起草探针（仓外 Temp）：改后配置跑 lease-issuer——`--path-glob "deliverables/**"`→exit 0（四字段入账）；`--path-glob "deliverables/experts/baigong-software-team/skills/sop/scripts/x.py"`→exit 0；`--path-glob "docs/foo.md"`→exit 2；`--path-glob ".collab/ledger/x"`→exit 2。写侧 end-to-end（lease deliverables/** ＋ write-guard engineer 身份写 deliverables 路径）＝无 deny 决策输出（放行）。

### T08-B 全表逐行机械化审查（裁定「逐行机械化审查」落点·两分账）

起草实测全表 30 行 write_globs（host 13／product 3／architect 7／qa 4／engineer 5／human 2），非机械行 14 行（host 4／product 0／architect 5／qa 2／engineer 2／human 1）。**账一（本票闭集内机械修正·语义零变化或纯通配展开）**：

| 席位 | 现行（逐字） | 机械形态 | 语义账 |
|---|---|---|---|
| engineer | 「（工作空间根∪部署路径）−受保护区」＋「限定当票租约路径集」 | 见 T08-A | 裁定授权面 |
| host | `.collab/human/{intake,reviews}/` | 拆两行 `.collab/human/intake/`、`.collab/human/reviews/` | 花括号枚举＝精确展开零变化 |
| architect | `.collab/drafts/{design,adr}/` | 拆两行 `.collab/drafts/design/`、`.collab/drafts/adr/` | 同上 |

**账二（语义拿不准处＝候裁单列·不自行拍·见候裁①–④）**：host `.collab/tickets/{id}/仅生命周期字段`·architect `.collab/tickets/票面文档（起草与按修票权修订）`·qa `.collab/tickets/缺陷票（修票权）`（三席同路径不同字段级约束，路径通配表达不了字段约束）；host `docs/转正代写`·`.archive/退役定稿落位`（代写/落位＝promote-manifest 脚本机械通道非席位租约写）；architect `开发票四字段`·`租约段签注与灰度判据（票内）`（票内字段面）；architect/qa `tests/共写（增删改走 C1）`（机械化＝新放行能力，现恒不命中，扩权需双席对表）；human 行「签名经主理人落…」（人类席不在 hooks 强制面）；engineer 新卡声明文本行随动与否（候裁⑥）。账二各行本票**零动**（现恒不命中＝无害滞留），回执附全表 30 行逐行审查读数表。

### T08-C hooks-map 身份映射补行（T07 丙账归口·实测结构缺口）

`config/seat-permissions-hooks-map.json` `agent_type_to_seat`（L32–38）现仅旧五名键。实测结构事实：新五卡 frontmatter `name:`＝`software-team-{lead,product,architect,qa,engineer}`（五卡 L2 逐字），现行身份投用后 write-guard `seat_of`（精确匹配→agent_id 前缀近似，L144–152）对五新名**全不命中**→席位不可归因→fail-closed 全 deny（写侧对五席全灭）。**加性修法（不动旧五行·演练身份零破坏）**：追加五行——
```json
    "software-team-lead": "host",
    "software-team-product": "product",
    "software-team-architect": "architect",
    "software-team-qa": "qa",
    "software-team-engineer": "engineer"
```
旧五行保留为 legacy 别名（drill-03/drill-05/tests/s4 现用旧身份串＝`software-engineer`/`software-product-manager`，改键则演练破坏；加行零破坏，T07 已登记旧名清退随 T08 后另议）。`_spec`「席位覆盖说明」行尾注补一句 legacy＋新名双载说明（该件内注记行随动）。

### T08-D 版本账随动（纪律①·三同源）

`.codebuddy-plugin/plugin.json` L3、`bundle.lock` L5、根 `plugin.json` L3 三处 version 现值同源（若 SWB-T07 先行施工则现值＝0.1.15，本票 bump →0.1.16；若 T08 先行则 0.1.14→0.1.15）。前后值各附实测 grep 读数（F7 口径）。`README.md`「出身」节版本账 append-only 追加一行（内容＝权限表数据面机械化：engineer 写域行机械形态＋全表审查账一＋hooks-map 身份补行，依据＝皮总裁定③·SWB-T08），既有行零回改。

## 验收判据（全部机械可判·命令自带落盘·负例一律 exit≠0）

0. 调用方注入仓外 Temp＝`T08_TMP`（Git Bash 与 Windows python 同域可读·禁 /tmp）。
1. **正例·engineer 交付面租约实例化 exit 0**：`python deliverables/experts/baigong-software-team/skills/sop/scripts/lease-issuer.py --ticket T08P1 --seat engineer --countersign architect:t08 --path-glob "deliverables/**" --config deliverables/experts/baigong-software-team/config/seat-permissions.json --leases "$T08_TMP/l1.jsonl" > "$T08_TMP/c1.out" 2>&1` → exit 0 且 c1.out 含 `"seat_id": "engineer"` 与 `hash` 四字段读数（对照开工前基线＝exit 2 REJECT，开工首跑基线读数亦落盘 `$T08_TMP/c1-base.out` 如实登记）。
2. **正例·具体路径租约 exit 0**：同式 `--path-glob "deliverables/experts/baigong-software-team/tests/t08sample/x.py"` → exit 0（读数落 `$T08_TMP/c2.out`）。
3. **负例·三越域请求各 exit≠0**：`docs/x.md`、`.collab/ledger/x`、`tests/x.py` 三请求逐条跑，落盘 `$T08_TMP/c3.out`（三 exit 码逐条 echo）→ 三条均 exit≠0（现行为回归保持：现配置下三请求本已 exit 2，机械化后不得放开）。
4. **机械审查断言**：python 内联读 `seat-permissions.json`，对 engineer `write_globs` 逐行匹配本票机械正则 → 非机械行数＝**0**；对 host/architect 账一展开行断言在位（`.collab/human/intake/`／`.collab/human/reviews/`／`.collab/drafts/design/`／`.collab/drafts/adr/` 四串各 occurrence＝1）；全表非机械行数读数落盘 `$T08_TMP/c4.out`（起草基线＝**14**（host 4／product 0／architect 5／qa 2／engineer 2／human 1），账一 4 非机械行动工清零（engineer 2＋host 花括号 1＋architect 花括号 1）→ 本批后读数＝**10**（host 3／architect 4／qa 2／human 1＝账二候裁滞留行，回执逐行登记）。
5. **hooks-map 身份补行断言**：`python -c "import json;m=json.load(open('deliverables/experts/baigong-software-team/config/seat-permissions-hooks-map.json'));a=m['agent_type_to_seat'];assert all(a.get(k) is not None for k in ('software-team-lead','software-team-product','software-team-architect','software-team-qa','software-team-engineer'))" > "$T08_TMP/c5.out" 2>&1` → exit 0；写侧端到端：lease engineer deliverables/** 入账后 `write-guard.py --path "deliverables/experts/baigong-software-team/tests/t08sample/x.py"` 喂 `{"agent_type":"software-team-engineer","agent_id":"software-team-engineer-x"}` → 输出无 `"permissionDecision"`（放行）落 `$T08_TMP/c6.out`。
6. **写域回归·旧身份仍通（加性零破坏）**：drill-03 现用旧身份 `software-engineer` 语义保持——`bash deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-03-write-side-intercept.sh > "$T08_TMP/c7.out" 2>&1` → exit 0。
7. **测试实体回归**：`python deliverables/experts/baigong-software-team/tests/s2/test_ledger_core.py deliverables/experts/baigong-software-team/tests/s2/test_lease_instantiation.py > "$T08_TMP/c8.out" 2>&1` → exit 0；`python deliverables/experts/baigong-software-team/tests/s4/test_enforcement.py > "$T08_TMP/c9.out" 2>&1` → exit 0（t13 deny_globs 同源断言＝本票未动 deny_globs 各数组，必须仍绿）。
8. **六演练回归**：`T06_TMP="$T08_TMP" bash deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-runner.sh > "$T08_TMP/c10.out" 2>&1` → exit 0 且 `SIX_DRILLS_GREEN` occurrence＝1（drill-05 走位随动＝候裁⑦未裁前零触碰，product 席走位保持）。
9. **版本三同源读数**：`grep -n '"version"' deliverables/experts/baigong-software-team/.codebuddy-plugin/plugin.json deliverables/experts/baigong-software-team/bundle.lock deliverables/experts/baigong-software-team/plugin.json > "$T08_TMP/c11.out"` → 三处同值＝本批后值（前后值各附实测·F7）。
10. **门禁零回归**：`bash deliverables/skills/object-audit/scripts/run-gates.sh --root . > "$T08_TMP/c12.out" 2>&1` → GATE PASS exit 0（开工基线同式读数并呈）。

## 票间关系
- 前置：SWB-T07（版本链＋旧卡清退后数据面身份面收敛更净；T07 候裁③丙账点名归本票）；T02（seat-permissions/hooks-map 实体）、T04（write-guard 消费面）收口件。
- 后置：真实试运行呈拍（裁定③「排在真实试运行前完成」）。质量链＝产品席＋QA 席双席独立审计→三方收口→呈皮总放行后派工程师施工。

## 禁动面（零触碰）
- 设计真源登记件与 `.collab/refs/external/` 全域；`.collab/` 其余（回执除外）；`docs/`、`tools/`。
- **T06 六演练除 drill-05 走位随动外零触碰**（drill-05 是否改走 engineer 席＝候裁⑦，未裁前零触碰）；`write-guard.py`、`lease-issuer.py` 及其余 scripts 零触碰（本票＝数据面规则票，不改机制代码）；**席位卡五新件零触碰**（engineer 新卡 L22 声明文本行随动与否＝候裁⑥，本票不拍）；`seat-permissions.json`／hooks-map 的 `deny_globs` 各数组零动（s4 t13 同源断言锚）；`explicitly_not_writable`/`carrier`/`table_notes` 各键零动（table_notes 如需注记随动限候裁裁定后）。
- 工程师不得改本票票体四字段与验收行；不自判合格（制度③）。

## 候裁点（单列·不自行拍）
1. **`.collab/tickets/` 三席字段级约束机械化**：host「仅生命周期字段」／architect「票面文档（起草与按修票权修订）」／qa「缺陷票（修票权）」——路径面可统一展开 `.collab/tickets/`，但字段级/票型级约束超出 path_glob 表达力（票体四字段纪律在 B2/票面机制层）。展开＋注记 vs 维持现样，呈裁。
2. **host `docs/转正代写`／`.archive/退役定稿落位`**：载体＝promote-manifest 脚本机械执行（物理 L106 表注转正代写款），非席位租约写；且 host deny 行 `docs/*（除转正代写通道）` 的括注豁免同样不可 path 机械判。是否建行/删行/改注记，呈裁。
3. **architect/qa `tests/共写（增删改走 C1）` 机械化为 `tests/` 行＝扩权**（现恒不命中→改后可签发仓根真源域租约；C1 流程约束不可 path 判）。设计原文确赋共写（物理 L101–102），但放开＝真实行为变化，呈双席对表。
4. **human 行「签名经主理人落 .collab/human/reviews/」**：人类席不入 hooks 强制面（hooks-map 不收人类行·设计语义），机械化与否呈裁。
5. **「部署路径」仓外域**：T08-A 不建行；真实投产若需部署域租约，届时按枚举补行（呈报件事项七旧账池同款登记），呈知悉。
6. **engineer 新卡（`agents/software-team-engineer.md` L22）声明文本行随动**：该句＝表2-1 工程师行设计散文转录；数据面已机械化而卡面仍散文，两读并呈。裁定前**零触碰**（本票闭集不含席位卡），随动两案（卡面改机械串 vs 保持设计散文＋注「机械实例化见 config」）呈裁。
7. **drill-05 走位是否改 engineer 席**：机械化后 engineer 对 deliverables 可签发租约，drill-05 现走 product 席（L16–20 注记）。改走＝演练面改写（T06 闭集件），不改＝注记成旧史。呈裁。
8. **`.collab/returns/engineer/` 等三行与 deny_globs `.collab/**` 的现行冲突（起草新证·实测读数）**：现盘构造 engineer 租约 `.collab/returns/engineer/PR02.md` 签发成功（exit 0），write-guard 对同路径喂 engineer 身份→**deny**（原因行逐字＝`路径∈deny_globs（表2-1 明确不可写·seat=engineer glob='.collab/**' …）`）——表2-1 授权的三个 `.collab` 子域被 deny 行 `.collab/**`（设计原文＝「`.collab/` 其余」）全域吞没，回流件落盘路径（return-template 指名 `.collab/returns/engineer/`）在现行数据面**写不进去**。修法涉 deny 表达（排除式 glob 超出表达力）或 write-guard 判定顺序（机制代码＝T04 闭集），均超本票数据面闭集，**呈裁**（候选案：deny 行拆 `.collab/*` 显式减授权三行的不可表达性／write-guard 增写域豁免（另出施工票）／回流件改道 host 域（改设计语义））。

## 候补优化池登记句（不入本票议程·仅登记）
旧身份 legacy 别名行（hooks-map 旧五行）的最终清退、`agents/*.md` 裸基名 WATCH 族、tools 两份基线快照再生（走 `--regen-*` 开关）、s2 t05 断言对 engineer 行新注记键的随动补强，均登记候补池。

## 回执
落 `.collab/receipts/2026-11-03-SWB-T08-receipt.md`：开端 HEAD 实测＋完整文件清单（与 commit name-only 全等）＋判据 0–10 逐条命令与实测读数（含开工前基线负例读数 c1-base 对照）＋全表 30 行逐行审查读数表＋候裁①–⑧逐条呈裁原文引用。交付笔单独 commit `collab:` 前缀只含闭集 6 件；回执笔随后单独笔。禁 `--no-verify`、禁 amend；pre-commit 门禁真拦时如实报告拦点并在闭集内修正重过，不得绕闸。