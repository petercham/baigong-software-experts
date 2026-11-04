# SWB-B4 · 门禁/票面锚定随动票 · 工程师回执 v1

- 回执席＝engineer-b4；票＝`.collab/2026-11-04-SWB-B4-收口登记-v1.md`（仓根面·票面 `9ae0b8a`＋rev2 `efbdcc0`·已退役·寻回见 SWB-RET 退役名录·冲突以 rev2 为准）。
- 开工实测 HEAD＝`a05ed58`（≥B3 收口登记笔；engineer-b3 无追加随正笔在笔上）；`git status --short` 基线读数＝空（干净）。
- 开工基线门禁族集（run-gates GATE PASS exit 0·发现 8689）：BLOCK OA-D6×3774／WATCH OA-D6×1365／OA-D6-3×1006／OA-D6-4×2042／MC-SOT-1×54／MC-SOT-2×413／EAC-L1×17／EAC-L2×18／**reconcile 族＝GONE 窗口态**（缺省票目录旧位空→票 0 发现 0＝B3 预告目）。
- 开工 `git ls-files .collab .scratch`＝**40**（仓根过渡面）；全仓 `(^|/)\.(collab|scratch)/` 口径＝**635**（B3 收口守恒值 638 中 3 件＝B3 后主理人裁定登记笔新增后口径·开工落盘＝635 在册）。

## 一、闭集 name-only 全等表（15＋9＝24 展开口径·rev2 补丁二钉死）

| # | 件 | 实动 | 笔 |
|---|---|---|---|
| 1 | agent-skills/object-audit/scripts/check-ticket-reconcile.py | 改 | `52d4328`＋`4d59b37` |
| 2 | agent-skills/object-audit/scripts/check-collab-lint.py | **零触碰**（spec_file 三锚已在 B3 换新位·开工实测即新位＝Y-7 已被 B3 顺带闭合，回执登记） | — |
| 3 | agent-skills/object-audit/scripts/run-gates.sh | **零触碰**（补丁六边界注记＝`pkg_dir`/`SPEC_ID_HOME` 段归 B2 rev2 补丁一已落；GATES_MD/EVIDENCE 路由叙述面无旧字面残留＝实测 grep 零命中） | — |
| 4 | agent-experts/baigong-software-team/skills/sop/scripts/write-guard.py | 改（B4-B 两级锚） | `f4c8c50` |
| 5 | agent-experts/baigong-software-team/skills/sop/scripts/lease-issuer.py | 改（B4-B 账本根项目根锚） | `f4c8c50` |
| 6 | agent-experts/baigong-software-team/config/seat-permissions.json | 改（B4-C/E＋补丁一/三） | `f4c8c50` |
| 7 | agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json | 改（同源随动） | `f4c8c50` |
| 8–11 | agent-skills/{multi-collab,object-audit,object-build,bundle-assembly-registration}/SKILL.md | **零触碰**（实测＝四件 spec_file 锚已在位无旧 `.collab/tickets` 字面；黄-3 悬空在 references 非 SKILL 本体＝路由入随动面见 §五，SKILL 本体入册不吞并） | — |
| 12 | agent-experts/baigong-software-team/bundle.lock | 改 0.1.17→0.1.18 | `cebb758` |
| 13 | agent-experts/baigong-software-team/plugin.json | 改 同上 | `cebb758` |
| 14 | agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json | 改 同上 | `cebb758` |
| 15 | agent-experts/baigong-software-team/README.md | append-only 一行 v0.1.18 | `cebb758` |
| 16 | tests/s2/test_lease_instantiation.py | 改（L82 断言随新域） | `3a5a783` |
| 17 | tests/s2/test_ledger_core.py | 改（L5 叙述） | `3a5a783` |
| 18 | tests/s3/test_dispatch_gate.py | 改（L5 叙述） | `3a5a783` |
| 19 | tests/s4/test_enforcement.py | 改（L5＋L83/L88/L167/L180 五处） | `3a5a783` |
| 20 | tests/probes/run-probes.sh | 改（L43 注释锚） | `3a5a783` |
| 21 | tests/acceptance/drills/drill-03-write-side-intercept.sh | 改（L28/L32 两处探针路径） | `3a5a783` |
| 22 | tests/acceptance/drills/drill-05-freeze-recover.sh | 改（L19 叙述注释） | `3a5a783` |
| 23 | skills/sop/scripts/ledger-init.sh | 改（L11 路径注释） | `3a5a783` |
| 24 | tests/acceptance/drill-runner.sh | **零改＝申报退出**（实测无路径锚涉改面＝grep deliverables/ROOT 零命中） | — |

（黄-3 随动面追加改动件＝agent-skills/multi-collab/references/{90-changelog.md,60-gates.md}＋agent-skills/object-audit/references/90-changelog.md 三件＝不在 24 闭集内，按 B3 收口登记「黄-3 换锚收账在册·B4 随动面」路由入 `cebb758` 分账，见 §五。候裁不自行拍＝此路由系 B3 收口登记既载指令，非本席新增裁量。）

## 二、逐笔 hash

| 笔 | 内容 |
|---|---|
| `52d4328` | collab: SWB-B4 B4-A reconcile 缺省票目录按项目 `.scratch/tickets` 枚举＋非空正断言 exit 4＋回执指针项目根基面/形态③（销 GONE 窗口） |
| `f4c8c50` | collab: SWB-B4 B4-B/C/E 两级锚换代＋R⑧(i) deny 精化＋engineer 枚举行＋project_domain_md 修值＋四席 deny 换代 |
| `3a5a783` | collab: SWB-B4 rev2 补丁五 tests fixture 面承接（八件） |
| `cebb758` | collab: SWB-B4 B4-F 版本三同源 0.1.18＋README＋黄-3 换锚＋（B4-D 件＝refs 排除面不入 git） |
| `4d59b37` | collab: SWB-B4 B4-A 随正·docstring 旧式锚清零 |
| （回执笔） | collab: SWB-B4 回执＋B4-D 追认随动＋B4 后复跑（本笔） |

## 三、判据逐条读数（七目·负例均实测）

1. **缺省票目录非空正断言**：`python agent-skills/object-audit/scripts/check-ticket-reconcile.py --root .` → exit 1（新树票在架·发现走②）；负例＝Temp 复制仓骨架（agent-skills/foo 无票目录）→ `infra error: 票目录枚举为空（门禁哑火形态）` **exit 4** ✓。
2. **票对账命中正读数**：c1.out 首行「票 **96**（对账 34／SKIP 缺声明 62）」≥在架票数（全仓 `.scratch/tickets` 活票实测 96·含 README 索引 2 件 SKIP）；旧式 `.collab[/\]tickets` 锚＝闭集 24 件 grep occurrence＝**0**（含随正笔 `4d59b37` 后）。
3. **回归全绿**：六演练 `SIX_DRILLS_GREEN` occurrence＝1（T06_TMP＝Windows 可读 Temp·B2 先例口径）；s2（ledger+lease 连跑）exit 0；s4 exit 0（t13 派生一致性含两 config 同源逐席全等）；s3 exit 0；run-gates `GATE PASS`；lease-issuer 探针 `--path-glob "agents/**"` **exit 0**／`--path-glob "docs/PRODUCT.md"` **exit 2** ✓（项目根相对字面·对位 T08R 形态迁移）。
4. **spec 锚存在性**：全仓 `spec_file:` 头块 python 抽取逐条 test -f＝missing **0**（七类载体 py/sh/md/tools 全域）；`.collab/tickets/` 旧式锚＝0（并入判据 2 面）。
5. **V13 三哈希不变**：B4-D 追认＝登记件尾追加 3 行（`wc -l` 260→263 口径 split 行数增 3）；段切复算（贴文正文物理 L29–260／产品 L29–84／架构 L85–260·LF join 无尾换行）＝`3f335333e0fe4bc2…ccb9b`／`7214ad14259b175f…91f3`／`efb4f7658c1e5555…78c4` 三值**逐字等**（追加前后各跑一次＝前后恒等）。登记件＝`/**/.collab/refs/` 排除面（.gitignore L59）不入 git 面＝不入 commit name-only；正文零改动·仅尾追加（追加行含裁定一指针＋「表2-1 语义按裁定一唯二排除追认」句＋V13 恒等式保护声明）。
6. **STRUCTURE↔engineer 行相等断言**：判据脚本＝本 receipts 桶 `2026-11-03-SWB-B4-judoca.py`（c6 节）→ exit 0：delivery_paths 六行 `[agents/, skills/, config/, hooks/, tests/, avatars/]` ↔ engineer write_globs 交付面枚举行 `[agents/** … avatars/**]` 逐行相等；`project_domain_md` 逐字＝`docs/STRUCTURE.md`；七项目 `test -f docs/STRUCTURE.md`＝缺 **none**；hooks-map 同源逐席全等 OK。PM B4-Y3 现面读值附＝改前 `project_domain_md="docs/collab-project-structure.md"`（作废名残留·rev2 补丁一实测值）→ 改后 `docs/STRUCTURE.md`。
7. **R⑧ 矩阵读数**：c7 节（同脚本）→ exit 0；矩阵读数见 §四。旧字面 `deliverables/**`／`deliverables/` occurrence（全 config 域六 json）＝**0** ✓。

## 四、R⑧ 销态前后对照＋11 桶×席矩阵

**销态前（过渡态 III）**：engineer deny `.collab/**` 基线＋host 租约行对表豁免注记未落＝租约在册仍 deny 冲突面在册。同探针实测（旧 hooks-map `git show` 重放）：lease-issuer 对 `.collab/returns/engineer/probe-r8.md` 签发 exit 0 后，write-guard＝`deny（glob='.collab/**'）`。
**销态后**：engineer deny 换代＝显式枚举减授权（deny 枚举逐桶列名·除 B1-D 规范闭集 host 租约授权桶＋本席写域三子域父桶让出）；同探针 write-guard＝`ALLOW（路径∈租约）` **exit 0**；`.collab/returns/engineer/`、`.collab/inbox/engineer/`、`.collab/drafts/deploy/` 三授权子域签发 exit 0＋写侧 allow 实测在笔；非授权桶 `.collab/ledger/x.md` 同席仍 **deny** ✓。

**11 桶×席矩阵**（A＝write_globs 命中／D＝deny 命中／·＝两不命中·桶名真源＝`skills/sop/references/collab-fixed-structure.md` grep 引用不复写）：

| 桶 | host | product | architect | qa | engineer |
|---|---|---|---|---|---|
| decisions/ | A | · | · | · | D |
| qa/ | · | · | · | · | D |
| receipts/ | · | · | · | · | D |
| board/ | · | · | · | · | D |
| design/（rev2 补行） | · | · | · | · | D |
| research/ | · | · | · | · | D |
| refs/ | · | · | · | · | D |
| evidence/ | · | · | · | · | D |
| inbox/ | A | · | · | · | A（engineer 授权子域让出） |
| process/ | · | · | · | · | D |
| dispatch/ | · | · | · | · | D |

design 行＝史实锚入库面，host 无写权外溢＝deny 维持格（逐格读数上表）。授权桶∩deny＝∅（engineer 授权子域∩deny 枚举＝∅ 机判行在 c7 输出）。host 租约面桶（ledger/signatures/dlq/commitments/human/release-record/manifest/config/archive/tickets）在 engineer deny 枚举显式在册不让（矩阵未列＝十一桶闭集外 host 专桶·不让读数＝`x.md` deny 实测）。

## 五、黄-3 换锚收账（B3 收口登记路由·最小随动·回执分账）

规范面 5 条悬空→换锚后 check-pointers 对位 BLOCK 全灭（base→final diff 实证 5 行消失）：
- multi-collab/90-changelog L23/L29/L32 三条（五维对比分析／裁决记录 spec_file／fuxi-merge design）→ `agent-experts/baigong-software-team/.collab/...` 全位。
- multi-collab/60-gates L156（`.collab/decisions/verdicts.md` 唯一文件句）→ 百工项目根全位。
- object-audit/90-changelog L9（T10 回执引用位）→ 百工项目根全位。

版本账随动说明：三件为沿革/路由登记面文字换锚，无条款语义变更＝multi-collab/object-audit 包版本账不动（登记级随动·同 B3 收口登记黄-3 口径）。

## 六、tests fixture 逐处表 ↔ B2 回执桶 C 对账

B2 回执桶 C 标「C→**B4 rev2**」的 tests 行＝5 登记行（ledger-init 1／s2×2＋s3 一行／s4 5 行／probes 1／drill-03 2＋drill-05 1）＝**13 处**（弃票面「21」锚值取实数口径）；本回执逐处表＝16 处（s4 含 L5 叙述行＋drill-03 含 JSON 体内 1 处同行计＝13＋叙述随动 3）。两票账目互指闭合：桶 C 13 处全数实装＝断言面 grep 后 tests 八件机械位旧字面 occurrence＝0（残留 3 处＝本批换代注记内引用性提及·非机械位）。drill-runner＝闭集 24 号申报零改退出。

## 七、门禁族集对拍（开工基线→收口）

收口跑＝**GATE PASS exit 0**（发现 8732）。族集对开工基线：
- **NEW＝none**（无新族名）。
- **GONE→回归（预期 NEW 读数·B4-A）**：reconcile `commit` 族 GONE→**×8**＝票目录枚举回归后对账族自证在位（B3 预告窗口态如期闭合）。
- 计数漂移（同族内实例）：BLOCK OA-D6 3774→3771（黄-3 灭 5＋B4-D 尾追加新增 2→回执落位后复跑再灭）；OA-D6-3 1006→1044（两 config 新 deny 枚举行 `.collab/<桶>/**` 字面＝交付包面出包案面引用命中＝OA-D6-3 既有族实例增加·deny 字面＝权限声明非指针语义＝同 seat-permissions 既有 `.collab/` 写域行同族形态·advisory 不拦·登记在册）。
  - OA-D6-3 增目逐字分账（QA-B4 黄-3 随正·照该报告 §黄-3/§目10 Temp 三仓并排复算口径 483→528＝Δ+45 构成）：两 config 新 deny/写域枚举行命中 **37**＋receipts 桶 judoca.py 自身命中 **5**＋write-guard/lease-issuer 新注释行命中 **2**（三项计 44，Δ+45 之差 1＝该报告未逐项列明）；本回执上行 1006→1044（Δ+38）＝真仓直跑口径，与 Temp 口径环境不同不互比。定性同主线＝既有族实例·advisory 不拦。
- 其余族恒等：EAC-L1 17／EAC-L2 18／MC-SOT-1 54／MC-SOT-2 413／OA-D6 1365／OA-D6-4 2042。

## 八、R①②③ 处置/在册（rev2 补丁七·回执级）

- R①（票面字段级约束随落位再核）＝再核结论：rev2 体例下票面字段无新增约束＝**在册续观**。
- R②（host docs 转正代写·promote-manifest 通道对表）＝promote-manifest.py 未列 B4 闭集、其路径锚不涉两 config 字面；docs/*（除转正代写通道）deny 行零动＝**自然在册**（其仓根假设随 B4-B 的换代＝tests 面实测 t07 绿）。
- R③（tests/ 共写双席对表）＝tests 面本批入 B4 闭集单席（engineer-b4）作业，无第二席在途＝**对表无冲突**。

## 九、B3a 剪枝收账行（防双治）

check-entity.py `iter_scan_files` 剪 `.collab`/`.scratch`＝B3 已落（`b29bc20` 在笔·B3 收口登记候裁①正式追认）＝**本票零触碰零重复治**；本票 scan 面变化全在 reconcile 自身（票目录枚举），无 check-entity 随动目。防双治行在册（＝B3 回执 c282aef 已登）。

**黄-1 收账行（qa-b3v2 报告路由·报告位 `.collab/qa/2026-11-03-QA-B3-独立验证-v2.md`·笔 `1e3b811`）**：`tools/check-source-of-truth.py` 5 行 `spec_file` 锚行改写系 B3a 批次先行落地（QA-B4 实测头块 spec_file 行现存 5 行＝三处交接件锚＋一处皮总拍板锚＋一处 handoff-discipline 锚）（`b29bc20`「spec_file 锚 8 处改写」目内·定性 Y-7 闭环化机械前置＝不改则 provenance exit 3 必红），超出 B3a 票面申报扫描面字面＝登记级。据此按本席路由将「tools 内 spec_file 锚行」**显式并入 B4 改锚面**＝与 B3a 剪枝防双治同例收账；本票对该件**零触碰零改写**（开工直读复验 4 锚行现位＝`agent-experts/baigong-software-team/.collab/research|decisions/…` 新树位与真源实物 test -f 全在＝判据 4 missing 0 覆盖面内），登记不再治，防占 B3a 已落件成双治。

## 十、边界注记＋不自行拍目

- 补丁六：run-gates `SPEC_ID_HOME`/`pkg_dir` 段 B4 期**零触碰**（归 B2 rev2 补丁一已落）＝边界注记防双改。
- 回执落位分歧登记：任务指令指仓根 `.collab/receipts/`，票面 §回执指 `agent-experts/baigong-software-team/.collab/receipts/`＝按票面落位（B3 后回执按项目归宿语义），分歧登记不自拍。
- 誊写禁令 `f5a0d96` 自察：本票＝原位代码文本随动批·零搬家目·零 mv 目。
- era 面不涉及（ESC1）。

## 十一、完工 HEAD

完工实测 HEAD＝回执笔前一笔链尾（各笔见 §二）；`git ls-files .collab .scratch`＝42→（回执笔后＋2＝judoca＋receipt 入库）。

——engineer-b4·SWB-B4 回执（回执笔单独 commit·禁 --no-verify·禁 amend 全程实守）。
