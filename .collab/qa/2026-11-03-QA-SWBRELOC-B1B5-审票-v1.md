# QA-SWBRELOC-B1B5 · 独立审票报告 v1（QA 席·证伪导向·只读审票）

- 审票轮 HEAD 实测＝`232bcfb`（≥ 开工门槛 `232bcfb` ✓）。
- 被审五票及落盘笔：B1＝`b5fd2b4`／B2＝`f017a51`／B3＝`d584d7b`／B4＝`9ae0b8a`＋勘正微笔 `232bcfb`／B5＝`8f5efa9`。
- 审票依据直读：施工基线 v3（`.collab/design/2026-11-03-restructure-proposal-draft-v3.md`）＋B0 冻结登记＋收口登记 `ed5d3c0`（R⑧(i) 向）＋裁定 `f135855`/`f5a0d96`（`.collab/decisions/` 两件在架）。
- 计数口径＝occurrence；关键计数双验（`git -c core.quotepath=off ls-tree/ls-files | grep -c` 与分桶求和互拍）。

## 〇、基线读数亲测（对票面值）

| 项 | 票面值 | QA 亲测 | 判定 |
|---|---|---|---|
| B2 票：f017a51 时 `git ls-files deliverables/` | 198 | **198** | ✓ |
| B2 票分桶：bundle 88／eac 7／mc 10／oa 40／ob 9／bar 6／fuxi 37／README 1 | 198 合计 | 逐桶全等（88+7+10+40+9+6+37+1） | ✓ |
| B3 票：f017a51 时 `.collab/` tracked 合计 | 597 | **597**（分桶 85+159+51+16+24+242+1+17＝595，另 `.collab/evidence/` 下 **2 支 tracked** 件补齐＝597） | ✓（附注见 B3-R3） |
| B3 票：f017a51 时 `.scratch/` tracked | 2 | 2 | ✓ |
| B3 票 untracked 面：refs 8835／evidence 3827／inbox 9／dispatch 10 | — | refs 8835 ✓／inbox 9 ✓／dispatch 10 ✓／evidence 现盘 3857（开工后 run-gates 证据件动态增长 30，开工首步重取基线即可，非票错） | ✓ |
| d584d7b 时点 `.collab/.scratch` tracked | — | 600（597＋B 批票 3 支）→ reconcile 新枚举在 B4 开工时点数以现场为准 | 备注 |
| 三哈希在册值 | `3f335333…/7214ad14…/efb4f765…` | 登记件头块 L5–L8 逐字在册；哈希锚＝V13 贴文体（非全文件），故 B4 尾追加不破、B5 搬家不破 | ✓ |
| 现盘 run-gates | — | `bash deliverables/skills/object-audit/scripts/run-gates.sh --root .` → exit 0·GATE PASS·发现 631（reconcile 票 84·exit 1 走②） | ✓ 现盘可跑 |

## 一、逐票三态

### B1 骨架票 — 认可（黄 1）

- 认可面：闭集 20 件逐行清点全等（3 顶层 README＋7×2 壳＋规范件＋.gitignore＋票目录 README）；判据 1–7 均机械可判＋负例款；B1-D 规范件＝B4 先决真源引用不复写 ✓；壳与 B2 mv 不撞的「壳内无同名子目录」机制自洽；WorkBuddy 装载面（`.codebuddy-plugin`/plugin.json/hooks 随包走）不与三分类目录/gitignore 块冲突 ✓；誊写禁令辖域外自察声明合规。
- **黄-1（gitignore 块对仓根无效）**：B1-E 七行 `/**/.collab/<bucket>/` 形态，QA 临时仓实测＝对**仓根** `.collab/refs/` 不命中（exit 1）、对嵌套 `a/b/.collab/refs/` 命中（exit 0）。即该防御块只防项目级新桶漏入，不防仓根 `.collab/` 现桶——现桶由现行旧行保护（B1-E「只增不删」成立故无洞），判据 5 探针恰选嵌套形态故票面自洽。风险在 B5 全重写时引爆（见 B5-黄-1）。

### B2 交付面搬家票 — 不认可（红 2·黄 2）

- 认可面：198 基线与分桶读数全等；开工 tag `archive-pre-B2-*`（D6）+ fuxi 预演先行 + 不成即 revert 的止损时序成立；R100＋抽样 10 件 diff＝0 的誊写禁令判据可执行；`git rm deliverables/README.md` 后 197/0 双向清零口径可机械验证；bundle.lock `path` 键随动在位；PRODUCT/ARCHITECTURE→docs 与 STRUCTURE 拒 docs 前缀款自洽（PRODUCT/ARCHITECTURE 非 delivery_paths 行）。
- **红-1（门禁扫描根换代缺口＝判据 4 不可达）**：B2 判据 4 要求「每笔后 run-gates GATE PASS exit 0」。QA 对机件源码推演证伪：B2-A1 完成（deliverables/ 树灭）后——
  1. `check-skill-meta.py` `find_root` 强校验 `isdir(root/deliverables)` → die_usage **exit 2**（run-gates L404-408：exit 2/3/4 → `blocked_by` → 阻断）；
  2. `check-entity.py` `SCAN_ROOT_DIRS=("deliverables",)` → 扫描空 → **exit 4**；
  3. `check-provenance.py` `default_targets`/`providers` 空 → **exit 4**；
  4. `run-gates.sh` 内嵌裁决段 `spec_id_resolvable` 的 `pkg_dir = ROOT/deliverables/<pkg>`（L267–270）硬编码——B2-C3 只申报「GATES_MD 候选序＋仓根探针」，未含此段 → OA-*/MC-*/EAC-* 全部解析失败 → **exit 3**。
  而 `check-skill-meta.py`／`check-entity.py`／`check-provenance.py` 不在 B2 声明闭集、不在 B2-C7「不在本批」清单、也不在 B4 十六件闭集——**三个门禁子脚本＋run-gates 一处内嵌段的新树随动无票认领**，B2 判据 4 与声明闭集互斥：要么 GATE 必红，要么违闭集补件。此为 B2 票面硬伤。
- **红-2（逐笔入壳枚举缺第 12 顶层项 `.codebuddy-plugin`）**：f017a51 实测 bundle 顶层＝12 项（agents 5／avatars 7／config 6／hooks 1／skills 34／tests 28／bundle.lock／plugin.json／settings.json／README.md／PRODUCT／ARCHITECTURE＝11 可见＋隐藏 `.codebuddy-plugin` 1 文件）。B2-A1 十一项枚举漏 `.codebuddy-plugin`——该目录＝WorkBuddy 平台注册面（plugin.json 版本同源三件之一）。守恒判据 1（197）会拦下漏搬，但施工规格形态即漏项；且 B2 闭集「plugin.json ×2」只在 B4 展开注记中出现，B2 逐笔面未点名。
- 黄-1：判据 1 分桶数叙述混乱（「agent-skills 109→110 对账口径以回执逐桶表为准」＋「Σ新桶−B1 壳件＝197」）——QA 复算：Σ新桶＝91(experts 88+壳3)＋123(skills 110+壳13)＝214，B1 壳件＝17（顶层 3＋experts 2＋skills 12），214−17＝197 ✓ 公式成立，但票内「87/109」两数与实测 91/123 不符、且以回执自为准＝判据自弱化；建议票面钉死 91/123。
- 黄-2：判据 3「活引用清零」豁免清单将吞掉约 90 处未修 py/sh/json 命中（reconcile 42＋provenance 15＋skill-meta 12＋entity 8＋publish 8＋baseline-seat-decl 4＋hooks-map 5＋seat-permissions 7＋tests/drills 面等），其中多数非史述而是**活代码旧路径**（部分无任何后续票认领，同红-1）；史述豁免与活引用欠账应分账。

### B3 过程域搬家票 — 不认可（红 2·黄 2）

- 认可面：597 守恒基线亲测成立（含 evidence 2 tracked 补齐，见红-3）；B3a 换锚先行→B3b mv 的硬线时序与 B4 exit 4 正断言构成哑火双闭合（窗口内 reconcile 空扫＝GATE PASS 假绿形态，B3 判据 6 已登记「过渡态在册」＋B4 落地封死＝成立）；era 留置＋ESC1 移交清单附件形态清晰；TKT 两支 erratum 登记不静默改基线＝合规形态；分账函数顺序闭集＋人工分账缺省桶可执行。
- **红-1（design 桶与 B1-D 规范闭集碰撞）**：B1-D 固定结构桶闭集＝`decisions qa receipts board research refs evidence inbox process dispatch`（无 design）；B3c 却申报「qa/receipts/board/**design** 四桶按分账函数入 `<项目>/.collab/<同桶>/`」。B3c 自己声明「固定结构闭集无 cases/ 桶＝不新增桶，B1-D 规范红线」，同一红线对 design 未适用——v3 §三 L64（design 入 `.collab\design\`）与 v3 §二标准结构图（无 design 桶）**基线内部自相矛盾**，票未消化即照 §三 执行。后果：B4-C deny 逐桶枚举矩阵（10 桶×席）不含 design＝防护矩阵漏桶。须裁定 design 归宿（归 `process/`（流水属性）或 `refs/`（素材属性）或修规范闭集扩员并随动 B4 矩阵），并修票。
- **红-2（判据 1 命令扫描面与申报扫描面不一致→机械不可达）**：B3a 申报扫描面＝receipts/qa/design/decisions/dispatch/docs/仓根 README/deliverables；判据 1 命令却是全仓 `grep -rno "\.collab/tickets/" .` 仅排两条——实测仓根 `.collab/evidence/gates/` 下 974 个历史证据 json 命中（门禁流水＝史实不可改），豁免清单须逐条列千行＝不可执行。且 run-gates 持续向 `.collab/evidence/` 写新 json（审票亲跑即增 30），豁免面动态漂移。修法＝判据命令扫描面照申报面限定，或加 `grep -v "^\./\.collab/evidence/\|^\./\.collab/inbox/"` 整桶豁免。
- **红-3（evidence 桶内 2 支 tracked 件与 B3e「文件系统 mv」形态冲突）**：`.collab/evidence/2026-10-29-判词-T-team-rename-01.md`＋同回执＝tracked（早于 gitignore 增补入库），而 B3e 规定 evidence 桶＝untracked 面文件系统 mv。文件系统 mv 后＝index 仍持旧路径而工作树缺文件（`git status` 悬挂删除），判据 2（ls-files 597 守恒）与判据 5（find 旧域清零）互相打脸。修法＝此 2 支单列走 `git mv`＋R100 断言，其余 evidence 走文件系统 mv。
- 黄-1：reconcile 过渡窗口（B3b 后→B4 前）旧目录空→其现版缺省返回 [] exit 0＝门禁哑火且 GATE PASS。票面已登记在册＋B4 exit 4 封死＝双闭合成立；QA 口径＝可接受，但 B3 回执须附该窗口 reconcile 读数实证（票已要求「窗口读数非绿不判红」，执行时不得省略）。
- 黄-2：仓根 `.scratch/tickets/` 五张 B 批票不在分账函数辖内（B3「随动改锚」仅注记留过渡），B4 新枚举只扫项目级 `.scratch/tickets/` → B 批票在 B4–B 批收口期间游离于 reconcile 对账外。窗口短且票面退役批有安排＝黄项登记，B 批收口登记时核销。

### B4 门禁随动票 — 认可（有条件·黄 3）

- 认可面：B4-A 缺省票目录按项目双候选枚举＋**扫描面非空 exit 4 正断言**（B 批判据四目②到位·判据 1 负例 exit 4 构造在位·run-gates 裁决段对子脚本 exit 4 阻断成立＝防假绿闭环）；先决闭集＝B1-D 规范件（R⑧(i) 向·`ed5d3c0` §三对位）✓；R⑨ 尾追加追认＋三哈希＝V13 贴文体锚（头块 L5–8 在册定义）→ 尾追加不破哈希＝自洽 ✓；STRUCTURE↔engineer 枚举行相等断言（验收 6）把 B1-C 已登记的 `project_domain_md` 作废名残留修入闭集 ✓；V13 恒等式保护声明在位。
- 黄-1（闭集计数注记不自洽）：「16 件展开名录＝所列 11 行＋版本三同源＋README＋…已含行内」按 QA 清点＝11 行＋bundle.lock＋plugin.json×2＋README＝15；16 与 15 差一未交代（或 write-guard/lease 外另有件未列名）。回执「name-only 全等」断言将首先被此坑绊住，须勘正展开表。
- 黄-2（四席位 `deny_globs` 旧字面随动未申报）：host/product/architect/qa 四行 `deliverables/**` deny 字面在 B2 后永空转。租约制「路径∉租约→deny」fail-closed 兜底仍在（无敞口），但显式硬拦层失效；B4-B 只申报 hooks-map「路径锚定」注记与 engineer 行。应在 B4 闭集内把四行 `deliverables/**` 改新树字面（仓根字面 vs 项目根字面随 B4-B1 语义定），补入判据 7 矩阵面。
- 黄-3（B4-C 文本表述含混）：「deny 改枚举…？＝否（精化方向按收口定案）」自问自答形态＋「除 B1-D 规范闭集中 host 租约授权桶」语义需回执矩阵（10 桶×席）逐格钉死；判据 7 已设矩阵＝可执行，表述建议改写以免施工歧义。
- 另注（不判黄）：SPEC_ID_HOME/`pkg_dir` 新树随动（＝B2 红-1 之 4）恰属本票 run-gates.sh 在闭集之便，建议一并认领——B4 票面现文未列该段。

### B5 收尾票 — 认可（有条件·黄 2）

- 认可面：gitignore 两制重写＋新旧条款映射表＋check-ignore ≥8 形态矩阵（含负向断言）＝机械可判；D7 入库＝字节级复制＋sha256＋三哈希双断言（誊写禁令落地形态最完整）；顶层终态白名单断言含旧壳出现＝exit 1 正防；README 重写含跨项目案卷「只指不搬」索引（B0 口径照录）；B5-C4 三同源 0.1.19 bump＋来源注两处随动。
- 黄-1（终写 gitignore 引爆 B1-黄-1）：B5-A2 排除面用 `/**/.collab/{refs,evidence,...}/`＋「旧仓根条款全部退役」——实测 `/**/` 形态**不命中仓根层级**（见 B1-黄-1）。B3 后 run-gates 证据件仍写仓根 `.collab/evidence/gates/`（`EVIDENCE_DIR="$ROOT/.collab/evidence/gates"` 未随新树，B4 未改），旧行退役后该面失去 ignore 防护→新证据 json 可被误 add。修法＝B5-A2 同批保留/新立仓根层级 `.collab/evidence/` 等显式行（或把 EVIDENCE_DIR 归 B4/B5 随动目），判据 2 矩阵补仓根层级形态探针。
- 黄-2（ESC1 无票体＝流程缺口·QA 口径）：era 留置（B3d）→ESC1 跨仓微批（B0 注记二＝执行项「随 B 批或独立微批」）→B5 票间关系列后置，但 `.scratch/tickets` 五票＋旧 `.collab/tickets` 均无 ESC1 票体，B 批收口登记归主理人。QA 口径＝**不构成硬缺口**（B0 已定性执行层＋B5 已排后序＋B3d 留置清单＝移交真源在位），但收口登记前须补 ESC1 独立微批票或收口登记内明载「era 移交随 B5 尾笔执行＋两仓两笔字节对账读数」，否则 B0 附注③（跨仓两笔对账）无落账处。B5-B README 索引行对 era 留置面宜标「待移交 experts 仓」注记。

## 二、互锁链推演结论

1. B1 壳↔B2 入壳碰撞规则：**成立**（壳内同名子目录不存在的构造＋内容注入式 mv），但 B2 十一项枚举漏 `.codebuddy-plugin` 破完整性（红）。
2. B3a 换锚硬线↔B4 exit 4 封死：**成立**（哑火双闭合＋过渡态登记），判据 1 命令形态须修（红-2）。
3. B1 规范件↔B4 deny 枚举精化：**成立**（先决闭集引用不复写；唯 design 桶漂移＝B3 红-1 须在 B4 矩阵前裁定）。
4. B3d era 留置↔B5 后置 ESC1：**排程成立·票体缺位**＝黄（收口前补票或收口登记内并案执行）。
5. 誊写禁令判据五票落地：**全部成立**（B2 R100+抽样、B3 R100＋改锚笔分离、B5 sha256+三哈希、B1/B4 辖域外自察）。
6. 门禁换代链：**断裂**——`check-skill-meta.py`／`check-entity.py`／`check-provenance.py` 三子脚本＋run-gates 内嵌 `pkg_dir` 段的 `deliverables` 硬编码随动无票认领（B2 未列·B2-C7 未列·B4 闭集未列），B2 判据 4「每笔后 GATE PASS」机械不可达＝全套五票最大单点风险（B2 红-1）。
7. B2 tag 机制↔B3 过渡窗口：tag `archive-pre-B2-*` 开工前打（D6·判据 7 在册断言）＋fuxi 预演先行可 revert＝时序风险可控 ✓；B3 窗口哑火双闭合 ✓（见互锁 2）。

## 三、结论表态

**有条件认可→修正后放行**：B1＝认可（黄 1 随行）；B4＝有条件认可（黄 3）；B5＝有条件认可（黄 2）；**B2＝不认可·须修票**（红 2：门禁随动无认领件＋入壳枚举漏 `.codebuddy-plugin`）；**B3＝不认可·须修票**（红 3：design 桶规范碰撞须裁、判据 1 扫描面须修、evidence 2 支 tracked 件须改 git mv）。

须修点清单（按严重序）：
1. **B2-R1**：为 `check-skill-meta.py`／`check-entity.py`／`check-provenance.py`＋run-gates 内嵌 `pkg_dir`/SPEC_ID_HOME 段的新树随动找出路——或入 B2 闭集（B2-C 追加第 8 目），或明列入 B4 闭集并调整 B2 判据 4 为「B2-C 清单改后 GATE PASS」（否则 B2 开工即锁死在 GATE 红）。建议 B2 闭集内完成（扫描根换代＝B2 既有议题「门禁扫描根同批随动」的自然延伸，B2-C 现文只列 5 件机件不完整）。
2. **B2-R2**：B2-A1 入壳枚举补第 12 顶层项 `.codebuddy-plugin/`（WorkBuddy 注册面），逐笔入回执。
3. **B3-R1**：design 桶归宿裁定（三选一：并入 process/ 流水属性、并入 refs/ 素材属性、或扩 B1-D 规范闭集并随动 B4 矩阵），修 B3c 行。
4. **B3-R2**：判据 1 grep 扫描面照 B3a 申报面限定或整桶豁免 evidence/inbox，避免千行历史 json 吞清单。
5. **B3-R3**：`.collab/evidence/` 两支 tracked 件（2026-10-29 判词＋回执）单列 git mv，不入文件系统 mv 面。
6. **B4-Y1**：16 件展开表勘正（现文展开＝15 件，差一交代）。
7. **B4-Y2**：host/product/architect/qa 四行 `deny_globs` 旧字面 `deliverables/**` 随动新树字面入闭集与判据 7 矩阵。
8. **B5-Y1**：gitignore 重写保留仓根层级排除行（或 run-gates EVIDENCE_DIR 随新树），check-ignore 矩阵补仓根层级探针。
9. **B5-Y2／ESC1**：B 批收口登记前补 ESC1 微批票或在收口登记内并案执行两仓字节对账；README era 留置面标「待移交」注记。
10. 随行小项：B1 规范件对 `design/` 的沉默随 B3-R1 一并处理；B2 判据 1 分桶数改钉 91/123；B4-C 自问自答表述改写。

QA 席侧确认项：B4 防假绿正断言（exit 4＋负例构造）认可；B5 D7 哈希链双断言认可；五票誊写禁令判据均可执行；三哈希锚＝V13 贴文体→B4 尾追加/B5 搬家均不破；现盘门禁可跑基线 631 条对拍口径成立。

——qa-relocrev·本报告只增不改（除本文件外零触碰）。