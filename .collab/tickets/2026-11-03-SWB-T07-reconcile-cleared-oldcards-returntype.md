# SWB-T07 · 微修票：reconcile 读侧容 cleared 行＋旧五席位卡物理清退＋回流四型标签机械化（施工票·L3·架构席起草）

- 起草实测 HEAD：`6d40ece`（`git rev-parse --short HEAD`·工作仓 `D:\multi-agent-collab-devkits`·main）；开工 ANCHOR 义务＝开工时实测 HEAD 应为 `6d40ece` 或其后可达后继，读数附回执开端（缺读数＝程序违例）。
- 票型＝微修票（缺陷修复·三目全部为**已实测发现问题**，YAGNI 议程闭集，推演优化项一律不入票）。
- 裁定依据（盘上直读·只读）＝`.collab/decisions/2026-11-03-皮总裁定-SWB票包遗留三件.md`（`6d40ece`）第①②④项：①对账崩溃缺陷采**方案甲**（改读侧容 cleared 行，不动台账格式/不改写侧）；②旧五席位卡物理清退与①**合并为同一张微票**；④回流四型标签**顺带**并入本票修（落点由架构席起草时定——本票落点＝`state-transition.py` 4→5 迁移记录增 `return_type` 字段＋四闭集校验，见 T07-C）。
- 证据件（只读·判定出处）：
  - 工程师实测复现＝`.collab/receipts/2026-11-01-SWB-T06-receipt.md`（呈核项①）；
  - QA 独立复现＝`.collab/qa/2026-11-03-QA-T06-独立验证-v1.md` 第六节（exit=1＋尾行 `KeyError: 'lease'`＋源码定位 reconcile-daily.py:95）与第九节（呈核五项分账：缺陷两件＝KeyError、回流四型标签；清退面呈核见 `.collab/qa/2026-11-03-QA-T05-独立验证-v1.md` 呈核①）。
- 计数口径声明：本票全部计数＝occurrence 口径（`grep -o … | wc -l` 或逐项 python 计数），非 `grep -c` 行数口径；判据命令一律自带落盘重定向（票面文字缺陷族先例教训）。
- 行号口径：本票引用行号＝起草实测现盘物理行号（锚行 `HEAD=6d40ece`）；开工复测行号若因前序笔位移，以本票逐字文本锚定位为准（SWB-SOP-R1 落位程序条款同款）。

## 声明闭集（15 件·本票唯一可写面）
- 声明闭集：
- deliverables/experts/baigong-software-team/skills/sop/scripts/reconcile-daily.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/state-transition.py
- deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-02-dispatch-exec-return.sh
- deliverables/experts/baigong-software-team/agents/software-company-team-lead.md
- deliverables/experts/baigong-software-team/agents/software-product-manager.md
- deliverables/experts/baigong-software-team/agents/software-architect.md
- deliverables/experts/baigong-software-team/agents/software-engineer.md
- deliverables/experts/baigong-software-team/agents/software-qa-engineer.md
- deliverables/experts/baigong-software-team/.codebuddy-plugin/plugin.json
- deliverables/experts/baigong-software-team/bundle.lock
- deliverables/experts/baigong-software-team/plugin.json
- deliverables/experts/baigong-software-team/README.md
- deliverables/experts/baigong-software-team/ARCHITECTURE.md
- deliverables/experts/baigong-software-team/PRODUCT.md
- deliverables/experts/baigong-software-team/skills/sop/templates/return-template.md

## 逐条施工规格

### T07-A reconcile-daily.py 读侧容 cleared 行（方案甲·缺陷＝已两次独立实测复现）

- 缺陷现盘：`reconcile-daily.py` L95＝`lease_ticket_ids.add(json.loads(line)["lease"]["ticket_id"])`，对 freeze 清租约 cleared 行（`freeze-unfreeze.py` L121–125 落盘形态＝`{"ts":…,"cleared": true,"cleared_count_prior":…,"by":"freeze-unfreeze.py freeze"}`，无 `lease` 键）无键防护→exit=1 `KeyError: 'lease'`（工程师与 QA 各自独立复现，QA 件第六节）。
- 修法（读侧单点·写侧与台账格式零动）：L95 单行替换为四行——
  ```python
                    e = json.loads(line)
                    if e.get("cleared") or not isinstance(e.get("lease"), dict):
                        continue  # freeze cleared 行（无 lease 键）跳过租约字段（SWB-T07 方案甲·读侧容行）
                    lease_ticket_ids.add(e["lease"]["ticket_id"])
  ```
  语义对位 write-guard.py `load_leases`（L155–170）既有 cleared 识别惯例（`e.get("cleared")` 判据同款）；台账格式约定、freeze 写侧、`leases` 计数语义（在册租约行数，cleared 行不计）零动。起草探针（仓外 Temp＝`D:/qa-swbfix-tmp`）：修改后语义跑含 cleared 行台账→exit 0、读数 `"leases": 1, "diff": 0`（cleared 行不 crash 不计数）。

### T07-B 旧五席位卡物理清退（§20.2③ 退役已生效·本目补物理删除＋引用面随动）

- 删除对象＝`deliverables/experts/baigong-software-team/agents/` 下旧五件（闭集列名五件·物理删除）。现盘该目录十件＝旧五＋新五（`software-team-{lead,product,architect,qa,engineer}.md` 零触碰）。范围红线：`workbuddy/` 与 experts 市场侧同名旧件不在本仓交付面者**不属本票**。
- 引用面排查结论（起草实测·occurrence 口径·锚 HEAD=6d40ece）——**处置三分账**：

  **甲账：现行注册/指针引用（随票逐件点名进闭集并随动）**
  1. `.codebuddy-plugin/plugin.json`：`agents[]` L10–14 五行指旧卡路径；`agentName` L23／`teamInfo` L25–30 四＋一名／`members[].id` L74/L81/L88/L95/L102 五行指旧卡名＝注册面现行引用。随动规格：`agents[]` 五行逐行替换为 `"./agents/software-team-lead.md"／"./agents/software-team-product.md"／"./agents/software-team-architect.md"／"./agents/software-team-qa.md"／"./agents/software-team-engineer.md"`；`agentName`/`leadAgent`→`software-team-lead`；`memberAgents`→新四员；`members[].id` 五行→新五 ID；`displayName/profession/avatar/role` 行零动（头像文件名行保留＝`avatars/software-*.png` 六件在盘指向存在，非悬空，QA-T05 呈核①同款判定）。
  2. `ARCHITECTURE.md` L15–19（编制图五节点名）＋L74–78（五席一览五反引号路径 `agents/software-*.md`）：删除后该五反引号带目录路径＝check-pointers OA-D6 悬空 BLOCK 族（工具真判据实测机理＝`check_pointers` 多探针皆不中→BLOCK）。随动规格：五节点名/五路径逐处替换为新五卡对应名与路径（`software-team-lead`／`agents/software-team-lead.md` 等五对），行文其余零动。
  3. `PRODUCT.md` L32 反引号路径 `agents/software-company-team-lead.md`：同上悬空面，随动替换为 `agents/software-team-lead.md`；该句其余零动（「工作流路由」节名与 L34–38 五档表＝旧叙事面，整段随 §20.1⑦ 的收编不在本票议程，列候补池）。
  4. 版本账随动（纪律①每变必 bump·TKT41 批先例三同源）：`.codebuddy-plugin/plugin.json` L3 `0.1.14`→`0.1.15`、`bundle.lock` L5 `0.1.14`→`0.1.15`、根 `plugin.json` L3 `0.1.14`→`0.1.15`（三处现值同 0.1.14，随批同步 bump，前后值各附实测 grep 读数入回执·F7 口径）；`README.md`「出身」节版本账**append-only 追加一行** v0.1.15（内容＝旧五卡物理清退＋.codebuddy-plugin 注册面随动指向新五卡，依据＝皮总裁定②·SWB-T07），既有行零回改。

  **乙账：历史叙事/产地注记引用（判「零触碰」·回执登记分账）**
  - `README.md` L27（fork 改名沿革）、L60（头像替换规格列举）、L72–76（旧 bundle token 账表五行）＝史述面；
  - `skills/software-orchestration/references/{quick-mode,bugfix-path,collab-rules,delivery-summary,incremental-dev,partial-workflows,standard-sop}.md` 各 L3「本件承载 `software-company-team-lead.md`（fork v1.2.0）…」＝产地注记（裸基名反引号＝WATCH 面，且所指＝市场 fork 源非仓内文件，删除不改变其真值）；
  - `tools/baseline-seat-decl.json`／`tools/baseline-sot-dup.json` 内旧卡路径键＝程序化基线（禁手抄；如需再生走 `--regen-*` 开关，本票不再生，回执登记读数）。
  - 乙账全部不在闭集，零触碰；回执附逐文件 occurrence 读数分账表（起草基线：README=11、references 七件各 1、hooks-map=5、根 plugin.json 头像行=5、.codebuddy-plugin 头像行=5、drill-03=1、drill-05=2、tests/s4=4、tools 基线若干）。

  **丙账：运行时身份映射残留（本票零触碰·登记候补池）**
  - `config/seat-permissions-hooks-map.json` L33–37 `agent_type_to_seat` 五行旧卡名：＝agent_type 身份映射非文件引用；新五卡 frontmatter `name:`＝`software-team-*`（实测五卡 L2），投用后现行身份将不命中该映射→写侧 fail-closed。该面＝表2-1 数据面职权，**归 SWB-T08 票**，本票禁动。

### T07-C 回流四型标签机械化（顺带目·缺陷实证＝QA 件 grep 全 scripts「回流」occurrence=0＋drill-02 L65–67 呈核注记＋T06 回执呈核②）

- 落点（起草裁量·裁定件④授权架构席定）＝`state-transition.py` 前进迁移 4→5（离开节点 4 执行＝回流登记面）增 `return_type` 字段＋四闭集校验：
  1. 常量区（L44 `TRIGGER_SOURCES` 之后）增一行：`RETURN_TYPES = ["完成", "部分完成", "受阻", "异常"]  # §3 回流件四型闭集（V13 物理 L141）`。
  2. `main()` 增参数：`ap.add_argument("--return-type", default=None, choices=RETURN_TYPES, help="回流四型标签（4→5 必填·§3 闭集）")`（argparse `choices` 即非法值机械拒：非法值 exit=2，系统级负例）。
  3. `transition()` 签名增 `return_type: str | None = None`；前进迁移段（L163 起）插入校验：`(src, dst) == (4, 5)` 且 `return_type` 缺席 → `return _reject(..., "4→5 回流迁移缺 return_type（回流四型闭集 {完成,部分完成,受阻,异常}·§3）", trigger_source)`；`(src, dst) != (4, 5)` 而 `return_type` 在位 → 同式拒（型标签只许挂回流迁移，防误挂）。
  4. L174–178 前进迁移入账 payload 增键：`"return_type": return_type if (src, dst) == (4, 5) else None`。
  5. 既有负/正路径零动：非法迁移（如 4→1）先于 return_type 校验命中既有 `_reject`（L164–165 顺序在前）；挂起/解冻/定级签收路径零触碰；账本记录格式只增键不改既有键。
- 语义真源对位（逐字引文对位款·T05 U7 教训）：`return-template.md` L3 现行句「态必从四型取一：**完成／部分完成／受阻／异常**（§3 回流四型闭集，其他措辞状态机拒绝登记）」——本目即把该句「状态机拒绝登记」机械化实装；四型取值串与该逐字串对位（全角分隔符两侧名逐一＝RETURN_TYPES 四值）。
- 随动两件（闭集内）：
  - `drill-02-dispatch-exec-return.sh` L43–44 该次 4→5 调用行追加参数 `--return-type 完成`（仅此一处加参，六名判据/断言零动——必填校验下不加该参则 drill-02 必红，随动属必填裁量的必然面，回执逐笔登记）；
  - `return-template.md`「回流头」节（L11「回流态」行之后）插一行：`- 迁移登记：state-transition.py --return-type 取同一型值（完成→"完成"，四值逐字同；4→5 缺值状态机拒）`（申报面↔机械面贯通，模板其余零动）。

## 验收判据（全部机械可判·命令自带落盘·负例一律 exit≠0 断言）

1. **正例·cleared 行台账对账 exit 0**（仓外 Temp＝`T07_TMP` 由调用方注入，不落仓内）：构造含一在册票据＋一条 product 席租约＋一条 cleared 行的台账跑对账，落盘 `$T07_TMP/c1.out`：
   `python deliverables/experts/baigong-software-team/skills/sop/scripts/reconcile-daily.py --ledger "$T07_TMP/l.jsonl" --leases "$T07_TMP/leases.jsonl" --states "$T07_TMP/states.json" --repo-root . > "$T07_TMP/c1.out" 2>&1` → exit 0 且 `$T07_TMP/c1.out` JSON 读数 `"diff": 0` 且 `"leases": 1`（cleared 行不计数不 crash；台账构造形制＝本票 T07-A 引 freeze-unfreeze.py L123–125 逐字段）。
2. **回归·既有对账形态不破坏**：`python deliverables/experts/baigong-software-team/tests/s2/test_ledger_core.py deliverables/experts/baigong-software-team/tests/s2/test_lease_instantiation.py > "$T07_TMP/c2.out" 2>&1` → exit 0（t08 orphan 租约呈报形态＝diff≥1＋呈报恰 1 仍在位，读数入回执）。
3. **正例·四型入账读数**：drill-02 单跑（注入 `T07_TMP`）exit 0；账本回读落盘 `$T07_TMP/c3.out`：
   `python - "$T07_TMP/drill02/ledger.jsonl" > "$T07_TMP/c3.out" 2>&1 <<'PY'` …回读断言脚本体（回执内联亦可）：`import json,sys; recs=[json.loads(l) for l in open(sys.argv[1],encoding="utf-8") if l.strip()]; n=sum(1 for r in recs if r["payload"].get("event")=="transition" and r["payload"].get("return_type")=="完成" and r["payload"].get("from")==4 and r["payload"].get("to")==5); assert n==1, n; print("return_type=完成 occurrence=1 OK")` → exit 0 且 `$T07_TMP/c3.out` 含 `occurrence=1`。
4. **负例·非法四型值 exit≠0**：`python deliverables/experts/baigong-software-team/skills/sop/scripts/state-transition.py --ticket T07NEG --from 1 --to 1 --ticket-type 开发 --ledger "$T07_TMP/nl.jsonl" --states "$T07_TMP/nst.jsonl" > /dev/null 2>&1; python deliverables/experts/baigong-software-team/skills/sop/scripts/state-transition.py --ticket T07NEG --from 4 --to 5 --kind signoff --ticket-type 开发 --sign 工程师交付签 --sign QA审计签 --return-type "已完成" --ledger "$T07_TMP/nl.jsonl" --states "$T07_TMP/nst.jsonl" > "$T07_TMP/c4.out" 2>&1; test $? -ne 0` → 断言 exit≠0（argparse choices 机械拒，`$T07_TMP/c4.out` 尾行含 `invalid choice` 读数入回执；注：前置 1→1 建立笔为必要铺垫，4→5 请求因当前态≠4 亦必被拒，双拒任一命中均满足 exit≠0 断言，回执如实登记命中路径）。
5. **负例·4→5 缺 return_type exit≠0**：同上链改不带 `--return-type` 且先合法推态至 4（推态命令逐条 `--sign` 照 drill-02 L37–42 形制），落盘 `$T07_TMP/c5.out` → exit≠0 且尾行含 `缺 return_type`。
6. **旧五卡物理删除读数**：`ls deliverables/experts/baigong-software-team/agents/*.md > "$T07_TMP/c6.out" 2>&1` → 行数＝5（occurrence 口径）且文件集＝{software-team-lead,software-team-product,software-team-architect,software-team-qa,software-team-engineer}.md（`wc -l` 读数＝5 入回执）。
7. **注册面随动断言**：`python -c "import json;p=json.load(open('deliverables/experts/baigong-software-team/.codebuddy-plugin/plugin.json'));assert p['agentName']=='software-team-lead' and p['teamInfo']['leadAgent']=='software-team-lead' and set(p['teamInfo']['memberAgents'])=={'software-team-product','software-team-architect','software-team-qa','software-team-engineer'} and all(a.split('/')[-1].startswith('software-team-') for a in p['agents'])" > "$T07_TMP/c7.out" 2>&1` → exit 0。
8. **悬空零新增断言（门禁面）**：`bash deliverables/skills/object-audit/scripts/run-gates.sh --root . > "$T07_TMP/c8.out" 2>&1` → GATE PASS exit 0（check-pointers/check-source-of-truth OA-D6/MC-SOT-2 对 ARCHITECTURE.md L74–78／PRODUCT.md L32 五反引号路径随动后零新增悬空 BLOCK；对比基线＝开工首跑同式落盘 `$T07_TMP/c8-base.out` 读数登记）。
9. **包内旧卡路径引用清零断言**：`grep -rno 'agents/software-company-team-lead\.md\|agents/software-product-manager\.md\|agents/software-architect\.md\|agents/software-engineer\.md\|agents/software-qa-engineer\.md' deliverables/experts/baigong-software-team/ | wc -l > "$T07_TMP/c9.out"` → 读数＝**0**（起草基线实测＝**11**：`.codebuddy-plugin/plugin.json` agents[] ×5＋ARCHITECTURE.md L74–78 ×5＋PRODUCT.md L32 ×1；三处均属甲账随动面，随动+删除后清零。乙丙账史述句均不含该带目录反引号/引号形态，起草实测该式对史述面零误触）。
10. **版本三同源读数**：`grep -n '"version"' deliverables/experts/baigong-software-team/.codebuddy-plugin/plugin.json deliverables/experts/baigong-software-team/bundle.lock deliverables/experts/baigong-software-team/plugin.json > "$T07_TMP/c10.out"` → 三处读数均＝`0.1.15`（前值 0.1.14 后值 0.1.15 各附实测·F7 口径）。
11. **六演练回归**：`T06_TMP="$T07_TMP" bash deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-runner.sh > "$T07_TMP/c11.out" 2>&1` → exit 0 且 `SIX_DRILLS_GREEN` occurrence＝1（drill-02 随动加参后六链仍全绿；drill-05 走位随动＝禁动，见禁动面；注＝演练件内 Temp 注入变量名为 `T06_TMP`（drill-runner.sh L10–14 现盘实体），判据 3 单跑 drill-02 同式注入）。

## 票间关系
- 前置：T02（reconcile/state-transition/seat-permissions 实体）、T04（freeze cleared 行写侧形态）、T05（新五卡装填与注册面）、T06（drill-02/05/06 演练面）全部收口件——本票为其缺陷修复与清退随动票。
- 后置：SWB-T08（权限表数据面机械化规则票·`agent_type_to_seat` 丙账归其职权）。质量链＝产品席＋QA 席双席独立审计→三方收口→呈皮总放行后派工程师施工（裁定件§二）。

## 禁动面（零触碰）
- 两基线登记件本体与 `.collab/refs/external/` 全域（只读）；`.collab/` 其余域（回执除外）；`docs/`、`tools/`（基线快照禁手抄禁再生）。
- `config/seat-permissions.json`、`config/seat-permissions-hooks-map.json`（丙账归 T08）；`write-guard.py`、`lease-issuer.py`、`freeze-unfreeze.py`、`shadow-replay.py` 及其余 scripts 非本票两脚本（T07-A/C 两件除外）；`tests/s2/`、`tests/s4/` 测试实体（回归只跑不改）；drill-01/03/04/05/06 五演练（drill-05 走位随动＝禁动，engineer 席机械化归 T08 后另议）；新五席位卡五件；`avatars/` 六件；`skills/sop/templates/ticket-template.md`、`decision-pack-template.md`；`skills/software-orchestration/` 全域（乙账史述面）；`agents/software-team-*.md` 五卡内声明文本行零触碰。
- 工程师不得改本票票体四字段与验收行；本票不自判合格（制度③）——结论权＝QA/CI 面。

## 候裁点（单列·不自行拍）
1. **4→5 之外的回流语义面**：`return_type` 只挂 (4,5) 迁移＝起草裁量（「回流＝离开执行节点」语义取 §4 生命周期）；若产品席认定部分完成续接（5→6 后再 4）等场景需扩挂点位，属条款解释候裁，不在本票扩面。
2. **`.codebuddy-plugin/plugin.json` 注册面整体随动指向新五卡**＝物理清退的必要随动（旧卡删除后该注册清单指旧路＝悬空注册）。若产品席认定旧 bundle 注册面（name=baigong-software-team 形态）应整体退役而非随动，则本目改为该件退役处置——两案皆超出「删除」闭集语义，呈裁。
3. **`config/seat-permissions-hooks-map.json` `agent_type_to_seat` 五行旧卡名残留（丙账）**：新五卡 frontmatter `name:`＝`software-team-*`，投用后现行身份不命中映射→写侧 fail-closed。该面与 SWB-T08 写域行机械化同域，本票登记不动。
4. **README.md L72–76 旧五卡 token 账表行**＝史述基线账（append-only 纪律），删除旧卡后该行成旧账——随呈报件事项七「旧账池」路径处置，本票零触碰。

## 候补优化池登记句（不入本票议程·仅登记）
- drill-02 L65–67 与 drill-05 L75–76 呈核注记文本在本票修后可销账，但销账属演练面改写（T06 闭集件），另顺路票处置；PRODUCT.md L34–38 五档表旧叙事随 §20.1⑦ 收编整段、README L27/L60 史述句、`agents/*.md` 裸基名 WATCH 族，均登记候补池。

## 回执
落 `.collab/receipts/2026-11-03-SWB-T07-receipt.md`：开端 HEAD 实测＋完整文件清单（与 commit name-only 全等·删除五件如实列名）＋判据 1–11 逐条命令与实测读数＋乙账分账表（逐文件 occurrence 读数）＋丙账登记。交付笔单独 commit `collab:` 前缀只含闭集 15 件；回执笔随后单独笔。禁 `--no-verify`、禁 amend；pre-commit 门禁（object-audit run-gates）真拦时如实报告拦点并在闭集内修正重过，不得绕闸。