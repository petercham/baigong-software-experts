# SWB-T07 · 工程师回执（reconcile 读侧容 cleared 行＋旧五席位卡物理清退＋回流四型标签机械化）

- 施工席＝工程师席（engineer-t07·新鲜实例）；被执行票面＝`agent-experts/baigong-software-team/.scratch/tickets/2026-11-03-SWB-T07-reconcile-cleared-oldcards-returntype.md`（全文直读·逐字施工）。
- 开工 HEAD 实测＝`f135855`（`git rev-parse --short HEAD`·工作仓 `D:\multi-agent-collab-devkits`·main）——票面 ANCHOR `6d40ece` 之可达后继 ✓（放行裁定件 `f135855` 即开工锚）。
- 开工 `git status --porcelain` 读数＝仅两条 2026-11-01 TKT untracked 旧件（`.collab/qa/2026-11-01-TKT-双审批计件汇总-v1.md`／`.collab/qa/2026-11-01-TKT-最终分票全文汇编-v1.md`）＝与指派相符 ✓。
- 完工 HEAD＝交付笔 `006d149`（回执笔随后单独笔）；`git log -1` 确认落笔（pre-commit 门禁 GATE PASS 存量 BLOCK/WATCH 告警不阻断口径）。
- 计数口径声明：本回执全部计数＝occurrence 口径（`grep -o … | wc -l` 或逐项 python 计数），非 `grep -c` 行数口径；判据命令一律自带落盘重定向。
- Temp＝仓外 `D:/t07-swb-tmp`（`T07_TMP`；Y2 随修口径＝Windows 盘符全域一致形态注入，Git Bash 与 Windows python 同域可读，非 Git Bash 挂载形态）；仓内零运行残留（完工 `git status --porcelain` 读数见第八节）。

## 开工附注（会师件 §四 T07 侧黄项）落实登记

| 黄项 | 会师件口径 | 落实读数 |
|---|---|---|
| Y2 判据 11 Temp 同域条款 | Temp 注入须全域一致路径（禁挂载形态） | 注入 `T06_TMP="D:/t07-swb-tmp/drills"` 盘符形态→六链全绿（c11 读数）；未用 `/d/…` 挂载形态 |
| Y3 判据 4 弱断言随修 | 先合法推态至 4 再喂非法值＋对照段 | 票面原式链照跑（exit 2 命中 argparse 路径）＋对照段＝新票合法推态至 4 后喂 `已完成`→exit 2 尾行 `invalid choice`（c4/c4b 双读数如实登记：两式命中路径均为 argparse choices 机械拒） |
| Y4 乙账漏登件 | 补登 `skills/sop/scripts/liveness-selfcheck.py:112` 旧身份 1 occurrence | 乙账分账表已补登（开工基线实测＝1）；本票零触碰 |
| Y5 注释锚两口径混写 | 交付代码注释锚改「V13 L113（物理 L141）」 | `state-transition.py` `RETURN_TYPES` 行注释实写＝`# §3 回流件四型闭集（V13 L113·物理 L141）`（按会师件修正写法落码，未照票面混写串） |

## 一、写入/修改文件清单（与交付笔 commit name-only 全等对账）

`git show --name-only --pretty=format: 006d149 | sort` 实测 15 件＝票面声明闭集 15 件全等 ✓：

修改（10 件）：
1. `deliverables/experts/baigong-software-team/skills/sop/scripts/reconcile-daily.py`（T07-A：L95 单行→四行读侧容 cleared 行，逐字照票面代码块）
2. `deliverables/experts/baigong-software-team/skills/sop/scripts/state-transition.py`（T07-C.1–4：RETURN_TYPES 常量行＋`--return-type` argparse choices＋transition 签名增参＋(4,5) 必填/非(4,5) 禁挂双校验＋payload 增键）
3. `deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-02-dispatch-exec-return.sh`（T07-C 随动：L43–44 该次 4→5 调用行追加 `--return-type 完成` 一处加参，六名判据/断言零动）
4. `deliverables/experts/baigong-software-team/.codebuddy-plugin/plugin.json`（甲账随动：`agents[]` 五行→新五卡路径；`agentName`/`leadAgent`→`software-team-lead`；`memberAgents`→新四员；`members[].id` 五行→新五 ID；`displayName/profession/avatar/role` 行零动；版本行 0.1.14→0.1.15）
5. `deliverables/experts/baigong-software-team/ARCHITECTURE.md`（甲账随动：L15–19 编制图五节点名＋L74–78 五反引号路径逐处替换新五卡对应名与路径，行文其余零动）
6. `deliverables/experts/baigong-software-team/PRODUCT.md`（甲账随动：L32 反引号路径→`agents/software-team-lead.md`，该句其余零动；L34–38 五档表零触碰）
7. `deliverables/experts/baigong-software-team/bundle.lock`（版本行 0.1.14→0.1.15）
8. `deliverables/experts/baigong-software-team/plugin.json`（版本行 0.1.14→0.1.15）
9. `deliverables/experts/baigong-software-team/README.md`（「出身」版本账 append-only 追加 v0.1.15 一行；既有行零回改）
10. `deliverables/experts/baigong-software-team/skills/sop/templates/return-template.md`（T07-C 随动：「回流头」节「回流态」行后插迁移登记行，模板其余零动）

删除（5 件·物理删除如实列名）：
11. `deliverables/experts/baigong-software-team/agents/software-company-team-lead.md`
12. `deliverables/experts/baigong-software-team/agents/software-product-manager.md`
13. `deliverables/experts/baigong-software-team/agents/software-architect.md`
14. `deliverables/experts/baigong-software-team/agents/software-engineer.md`
15. `deliverables/experts/baigong-software-team/agents/software-qa-engineer.md`

删除方式＝`git rm`（退役五目口径：宣告先行＝README 版本账 append＋注册配置面同批清零先落，物理移除＋引用清零断言后验——本笔内注册面随动与物理删除同批提交 ✓）；非迁移类操作，无誊写面。新五卡五件零触碰（commit 不含）。

## 二、验收判据 1–11 逐条命令与实测读数

### 判据 1 正例·cleared 行台账对账 exit 0 → PASS

台账构造＝一在册票据 T07J1＋一条 product 席在册租约＋一条 cleared 行（逐字段照 freeze-unfreeze.py L123–125 落盘形态 `{"ts":…,"cleared":true,"cleared_count_prior":1,"by":"freeze-unfreeze.py freeze"}`）。

```
python deliverables/experts/baigong-software-team/skills/sop/scripts/reconcile-daily.py --ledger "$T07_TMP/j1/l.jsonl" --leases "$T07_TMP/j1/leases.jsonl" --states "$T07_TMP/j1/states.json" --repo-root . > "$T07_TMP/c1.out" 2>&1
```

实测＝**exit 0**；c1.out 读数＝`…"leases": 1, …"diff": 0…`（cleared 行不计数不 crash）✓。开工基线（改前同式）＝exit 1＋尾行 `KeyError: 'lease'`（缺陷复现属实·QA 件第六节同款）。

### 判据 2 回归·既有对账形态不破坏 → PASS

```
python deliverables/experts/baigong-software-team/tests/s2/test_ledger_core.py deliverables/experts/baigong-software-team/tests/s2/test_lease_instantiation.py > "$T07_TMP/c2.out" 2>&1
```

实测＝**exit 0**；c2.out 尾三行＝`PASS t06_hold_requires_human_direct / PASS t07_timeouts_defaults / PASS t08_reconcile_diff_writes_report`（t08 orphan 租约呈报形态＝diff≥1＋呈报恰 1 仍在位）✓。

### 判据 3 正例·四型入账读数 → PASS

```
T06_TMP="$T07_TMP" bash deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-02-dispatch-exec-return.sh   # exit 0＋DRILL02_GREEN
python - "$T07_TMP/drill02/ledger.jsonl" > "$T07_TMP/c3.out" 2>&1 <<'PY'（票面回读断言脚本体逐字）
```

实测＝drill-02 单跑 **exit 0**；c3.out＝`return_type=完成 occurrence=1 OK`（断言 event=transition∧return_type=完成∧from=4∧to=5 恰 1）✓。

### 判据 4 负例·非法四型值 exit≠0 → PASS

票面原式链（前置 1→1 建立笔＋4→5 请求带 `--return-type "已完成"`）实测＝**exit 2**；c4.out 尾行＝`state-transition.py: error: argument --return-type: invalid choice: '已完成' (choose from '完成', '部分完成', '受阻', '异常')` ✓。命中路径如实登记＝argparse choices 机械拒先于状态机（票面「双拒任一命中」注记之实际命中面）；Y3 随修对照段＝新票合法推态 1→1→2→3→4 后喂非法值→**exit 2** 同 `invalid choice` 尾行（c4b.out）——排除「当前态≠4 被拒」假绿可能，choices 实装在位实证 ✓。

### 判据 5 负例·4→5 缺 return_type exit≠0 → PASS

新票 T07MISS 合法推态至 4（推态命令逐条 `--sign` 照 drill-02 L37–42 形制），4→5 不带 `--return-type`：实测＝**exit 2**；c5.out＝`REJECT ticket=T07MISS 4→5: 4→5 回流迁移缺 return_type（回流四型闭集 {完成,部分完成,受阻,异常}·§3）` ✓。补测防误挂支（T07-C.3 第二校验·回执登记非票面判据）＝新票 T07MIS 1→2 带 `--return-type 完成`→exit 2＋尾行 `return_type 只许挂 4→5 回流迁移（防误挂…）`（c5c.out）✓。

### 判据 6 旧五卡物理删除读数 → PASS

```
ls deliverables/experts/baigong-software-team/agents/*.md > "$T07_TMP/c6.out" 2>&1
```

实测＝`wc -l` 读数＝**5**；文件集＝{software-team-lead, software-team-product, software-team-architect, software-team-qa, software-team-engineer}.md（c6.out 五行逐名相符）✓。

### 判据 7 注册面随动断言 → PASS

票面 python 断言命令逐字跑（agentName＝software-team-lead∧leadAgent 同∧memberAgents 集＝新四员∧agents[] 五行均 software-team- 前缀）实测＝**exit 0**（c7.out 空输出）✓。

### 判据 8 悬空零新增断言（门禁面）→ PASS

```
bash deliverables/skills/object-audit/scripts/run-gates.sh --root . > "$T07_TMP/c8.out" 2>&1
```

实测＝**GATE PASS exit 0**（发现 628 条·均按路由表走②不拦提交）。开工首跑对比基线＝同式落盘 `$T07_TMP/c8-base.out`＝GATE PASS exit 0（发现 620 条）。差值登记：620→628（+8）＝①README append 一行致 L55 既有 BLOCK `references/deploy-gate.md` 行号位移＋②旧卡删除使 references 七件＋README L27 裸基名行新入 WATCH 提及嫌疑族（D6 裁-21 划界「裸基名不 BLOCK」＝乙账史述面既有登记）＋③check-ticket-reconcile 对旧票面声明路径 WATCH 随旧卡删除更新。**BLOCK 集按内容归一化（行号掩蔽）对账＝零新增**：base BLOCK 出现行 424 与 post 432 差值全部为行号位移重复行（`sed 's/:[0-9]*:/:N:/'` 排序后 diff exit 0）；ARCHITECTURE.md L74–78／PRODUCT.md L32 五反引号路径随动后 check-pointers 零命中（c8.out 中该两文件无 OA-D6 带目录路径悬空条目）✓。

### 判据 9 包内旧卡路径引用清零断言 → PASS

```
grep -rno 'agents/software-company-team-lead\.md\|agents/software-product-manager\.md\|agents/software-architect\.md\|agents/software-engineer\.md\|agents/software-qa-engineer\.md' deliverables/experts/baigong-software-team/ | wc -l > "$T07_TMP/c9.out"
```

开工基线实测＝**11**（与票面申报 11 全等：.codebuddy-plugin agents[]×5＋ARCHITECTURE L74–78×5＋PRODUCT L32×1）；完工实测＝**0** ✓。

### 判据 10 版本三同源读数 → PASS（F7 前后值各附实测）

前值（开工实测）：`.codebuddy-plugin/plugin.json:3`＝`0.1.14`、`bundle.lock:5`＝`0.1.14`、根 `plugin.json:3`＝`0.1.14`。
后值（c10.out 实测）：
```
deliverables/experts/baigong-software-team/.codebuddy-plugin/plugin.json:3:  "version": "0.1.15",
deliverables/experts/baigong-software-team/bundle.lock:5:    "version": "0.1.15",
deliverables/experts/baigong-software-team/plugin.json:3:  "version": "0.1.15",
```
三处均＝`0.1.15` ✓；README 版本账 append 一行 v0.1.15 已落（既有行零回改）。

### 判据 11 六演练回归 → PASS

```
T06_TMP="D:/t07-swb-tmp/drills" bash deliverables/experts/baigong-software-team/tests/acceptance/drill-runner.sh > "$T07_TMP/c11.out" 2>&1
```

实测＝**exit 0** 且 `SIX_DRILLS_GREEN` occurrence＝**1**（六链 DRILL01–06 逐链 GREEN；drill-02 随动加参后仍全绿；drill-05 走位零触碰）✓。Y2 口径＝Temp 用 Windows 盘符全域一致形态注入（非挂载形态）。

## 三、乙账分账表（逐文件旧名 occurrence 读数·开工基线实测）

口径＝`grep -o 'software-company-team-lead\|software-product-manager\|software-architect\|software-engineer\|software-qa-engineer' <file> | wc -l`（裸名全包扫描形态，乙账史述面不含判据 9 带目录路径形态）。

| 文件 | 基线读数 | 完工读数 | 处置 |
|---|---|---|---|
| `README.md`（L27 沿革／L60 头像规格列举／L72–76 token 账表五行等） | 11 | 16（差值构成＝本票甲账随动条款强制的 v0.1.15 版本账 append 行含旧五名各 1；基线 11 不变、既有行零回改属实） | 史述面·零触碰 ✓ |
| `skills/software-orchestration/references/quick-mode.md`（L3 产地注记） | 1 | 1 | 零触碰 ✓ |
| `references/bugfix-path.md` | 1 | 1 | 零触碰 ✓ |
| `references/collab-rules.md` | 1 | 1 | 零触碰 ✓ |
| `references/delivery-summary.md` | 1 | 1 | 零触碰 ✓ |
| `references/incremental-dev.md` | 1 | 1 | 零触碰 ✓ |
| `references/partial-workflows.md` | 1 | 1 | 零触碰 ✓ |
| `references/standard-sop.md` | 1 | 1 | 零触碰 ✓ |
| `config/seat-permissions-hooks-map.json` | 5 | 5 | 丙账（见下）·禁动 ✓ |
| 根 `plugin.json`（头像行） | 5 | 5 | 乙账形态·本票仅 bump 版本行 ✓ |
| `.codebuddy-plugin/plugin.json` | 21 | 5 | 甲账随动 16 处清零；余 5＝members[].avatar 头像文件名行（票面明示零触碰·`avatars/software-*.png` 六件在盘非悬空，实测 avatars=6）✓ |
| `tests/acceptance/drills/drill-03-write-side-intercept.sh` | 1 | 1 | 禁动面 ✓ |
| `tests/acceptance/drills/drill-05-freeze-recover.sh` | 2 | 2 | 禁动面 ✓ |
| `tests/s4/`（四件合计） | 4 | 4 | 禁动面 ✓ |
| `skills/sop/scripts/liveness-selfcheck.py:112`（旧身份 1 处） | 1 | 1 | **Y4 补登件**·禁动面（非闭集）·零触碰 ✓ |
| `tools/baseline-seat-decl.json`＋`tools/baseline-sot-dup.json`（仓根 tools 两基线件·旧卡路径键） | 29（带目录路径形态实测） | 29 | 程序化基线·禁手抄禁再生·本票不再生·登记读数 ✓（run-gates 门禁链不消费两基线件，删除旧卡不触发门禁回归） |

乙账全部零触碰属实（完工 name-only 对账不含上表任何禁动件）✓。

## 四、丙账登记（本票零触碰）

`config/seat-permissions-hooks-map.json` L33–37 `agent_type_to_seat` 五行旧卡名：＝agent_type 身份映射非文件引用；新五卡 frontmatter `name:`＝`software-team-*`（实测五卡 L2 逐件相符），投用后现行身份不命中该映射→写侧 fail-closed。该面归 SWB-T08 票职权，本票禁动、完工读数 5→5 零动 ✓。

## 五、候裁点照票处置（不自行拍·单列）

1. 候裁①（4→5 之外回流语义扩挂）：未扩面，`return_type` 只挂 (4,5)＝照票。
2. 候裁②（.codebuddy-plugin 注册面随动 vs 整体退役两案）：照票执行随动案；若产品席后裁整体退役，本目改处置呈裁——本回执登记在案。
3. 候裁③（hooks-map 丙账五行残留）：登记不动归 T08 ✓。
4. 候裁④（README L72–76 旧五卡 token 账表行旧账）：零触碰随旧账池呈报 ✓。

## 六、禁动面自证

两基线登记件／`.collab/refs/external/`／`docs/`／`tools/`：零写入（commit 不含）✓；`config/` 两件、`write-guard/lease-issuer/freeze-unfreeze/shadow-replay` 及其余 scripts、`tests/s2/`、`tests/s4/`、drill-01/03/04/05/06、新五卡五件、`avatars/`、ticket/decision-pack 模板、`skills/software-orchestration/` 全域：零写入 ✓；票面四字段与验收行未改；本回执不自判合格（结论权＝QA/CI 面·制度③）。

## 七、程序口径

分笔＝交付笔 `006d149`（`collab:` 前缀·只含闭集 15 件）＋回执笔（本笔）。禁 `--no-verify` 未用、禁 amend 未用。pre-commit 门禁（object-audit run-gates）对交付笔真跑：GATE PASS 不拦（存量 BLOCK/WATCH 走②路由不阻断）。仓外 Temp 全部落 `D:/t07-swb-tmp`。

## 八、完工读数

- 完工 HEAD（交付笔）＝`006d149`；`git log -1 --oneline`＝`006d149 collab: SWB-T07 reconcile读侧容cleared行＋旧五席位卡物理清退注册面随动＋回流四型标签机械化`。
- 交付笔后 `git status --porcelain`＝仅同开工两条 2026-11-01 TKT untracked 旧件＝仓内零运行残留 ✓。
