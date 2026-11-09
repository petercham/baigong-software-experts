# CLN-PURE 装配净化施工票 · QA 独立审票 v1

- 被核件：`agent-experts/baigong-software-team/.scratch/tickets/2026-11-05-CLN-PURE-装配净化施工票.md`（177 行）
- 开工 HEAD 实测：`git rev-parse --short HEAD`＝`6529209`（main）＝任务预期值，与票面开票锚 `3cf3ad1` 关系实测：`git merge-base --is-ancestor 3cf3ad1 HEAD`＝真；`git diff --name-only 3cf3ad1..HEAD` 对闭集 43 件交集＝**空**（3cf3ad1..6529209 仅一票面 commit，闭集件自开票侧锚读后零漂移——票内全部行号锚读按 3cf3ad1 有效）。
- 轮次戳：2026-11-05 · QA 席 fresh eyes 独立审（与产品席同题互不读）。
- 审法声明：全部判据均实跑取样（grep/python/find/隔离副本实验），未改票面本体、未动真源与装配面；探针临时副本已清理（仓根 `probe_facetmp/` 确系本席实验残留，已删；`.tmp_qa_facetmp/` 用后即删）。

## 判决

**不通过——需修票后方可施工。** 施工方案本体（S1–S8）自洽可执行、装配面/真源对拍全部成立；但验收判据两条（A3 补充扫描、A7 闭包 WATCH 预期）与禁动面/实测读数存在机械性硬冲突，照票执行必触发票内「停手上报」红线。两条均为判据文案修正，不动施工面。

计数：**红 2 · 黄 3 · 绿 12**

---

## 红项（必修票）

### R1｜A3 补充扫描 pattern 与禁动面硬冲突（不可清零、白名单无出口）

票面 A3 补充扫描：主式之外追加 `probe-results`／`V10 L`／`V11 L`／`.collab/tickets` 实指，「白名单同§口径3」「施工后应零命中，命中即回扫对应 S 节补净」。实测装配面现面（6529209 旧面取样）：

- `V10 L` 在 `architecture-v2.9-copy.md` **正文**命中 2 处（实测行 28「转正代写条款住本表注（**V10 L104 实物**）」、行 55「…（V10 L54）之跳过环节」）；
- `.collab/tickets` 在副本正文命中 3 处（实测行 18/20/21＝表2-1 席位权限转录行）；
- 两副本正文＝票面禁动面（「逐字钉死基线副本·正文零字动」「哈希等式破坏＝立即停手上报」），S3 只动 L1 头注；
- 白名单核对：§口径3 ②只豁免副本正文内「决策登记锚哈希（7 位 commit 形态）」入 **A4**，未覆盖正文内 `V10 L` 行号锚与 `.collab/tickets` 词汇；①「席位卡／config／技能正文」措辞未显式含基线副本正文（且即便计入，其不可动性不变——命中仍在面上）。

⇒ 施工后补充扫描必然 ≥5 命中、必然无法「回扫补净」（禁动面锁死），按票面「命中即回扫」与红线「口径有异议＝停手上报」将卡死收口。修法＝补充扫描显式排两副本正文（或把②白名单扩至「副本正文内规范转录条款文本本体」并入 A3 补充口径）。旁证：主 A3 式 `V13 L` 在两副本正文命中＝0（实测 awk NR>1 复核），主式无此冲突——冲突仅系补充式追加变体与禁动面组合。

### R2｜A7「check-pointer-closure WATCH 清零」预期被实测证伪＋新指针 WATCH 未预登记

票面 A7：「check-pointer-closure 对 EAC 包面 multi-collab 不可达 WATCH 应随 S2 清零，清零数即随动证据」＋「GATE PASS exit 0 零新增（前后发现数对比）」。实测：

1. 直跑 `python agent-skills/object-audit/scripts/check-pointer-closure.py`（缺省两包面）：multi-collab 相关 WATCH 中，**S2 触及件**（SKILL.md／10-roles／20-rounds／30-discipline／40-artifacts／spec-anchors）随 S2 清零成立；但 `references/90-changelog.md` 内 multi-collab 不可达 WATCH **4 条**（实测 19/27/27/34 行）——90 件＝票面禁动面（仓内保留），**必残留**；另 `.scratch/tickets/2026-10-30-EAC-SK6-黄项最小修正票.md:10` 1 条（历史票，不在任何 S 节）。「清零」按包面口径不成立（按装配面口径则该门禁本就不扫装配面——两读法都不成立）。
2. 实验（隔离副本＋门禁实跑）：S2 对 40-artifacts L85 的改指新值 `` `../../software-orchestration/references/handoff-discipline.md` `` 在**源仓包面**＝新增 OA-D6-4 不可达 WATCH 1 条（实测门禁输出、exit 1）——该相对指针只在装配面可解（见绿项 G9：装配面可解性成立）。A7 只预免了「本票回执落盘前」1 条 WATCH，未登记此条 → 按「零新增」逐笔口径将撞「实测与票面预期冲突按实测登记上报」红线。
3. 基线读数不可对拍：票面「3cf3ad1 基线含同类 WATCH 146 条」——本席直跑口径 WATCH 计数＝**3200**（含 .collab/.scratch 过程域文件），146 应为 run-gates 挂 narrower 口径；A7 前后对比未锁同口径读数定义。

修法＝A7 改「multi-collab WATCH 随 S2 **净减**（S2 触及件清零；90 件＋历史票残留 N 条＋新指针 1 条逐笔登记 EXEMPT）」＋规定前后读数的同口径跑法。

---

## 黄项（修单列给主理人，不拦施工）

- **Y1｜deep-research README 裁除后装配面悬垂引 4 处未逐笔登记**：`skills/deep-research/` 装配面文件对自家 README 的指向实测 4 处（`references/domains/film-tv.md:3`、`references/domains/_new-domain-template.md:3`、`references/methodology.md:3`、`scripts/verify_citations.py:10` 均含「登记见 README／按 README…」句）。README 经 exclude 裁出后此四句成装配面悬垂引。票面口径④只登记了「README 内义务声明指向句」一事，未逐笔登记消费侧四处；且 deep-research 真源跨仓禁写＝不可修。建议票面补一行「消费侧 README 引 4 处＝悬垂但 A3/A4 pattern 不命中，登记即止」（实测该四处不命中 A3/A4 任何 pattern，门禁无碰撞——故黄不拦红）。
- **Y2｜S2「改后 EAC 包面对 multi-collab／90-changelog 字面命中＝零（90 件本体除外）」的范围歧义**：EAC 真源面 git 跟踪件里 `.scratch/tickets/`（历史票）与 `.collab/` 研究件含 multi-collab／90-changelog 命中（实测）；若「包面」含 tracked 过程域＝不为零。装配面口径（.collab/.scratch 段 PUB-EXCL 已排除，publish.py L730 实测在码）下该句成立。建议票面注明「包面＝装配面口径」。
- **Y3｜票内行号锚读的小偏差登记**：S1「do_assemble 起 L795」实测 def 在 L796（L795 为装饰前一行）；S2/S4/S5 各件行号抽点核对基本咬合（write-guard L5/L7/L9/L49 命中、commit-audit L9/L15/L32 命中、EAC SKILL L20/L22/L32 命中、test_lease_instantiation L81-82 断言命中、test_enforcement L51-55/L131 命中）。票面已自带「施工以 pattern 命中为准」免责口径，不构成错，登记读数即可。

---

## 绿项（12 项，全部实测）

1. **声明闭集 43 件双向对拍成立**：票面 L6 块头（DECL_LINE_RE 口径 Python 实配＝命中 L6、正文空、紧随列表 43 行）；43 件 `git ls-files --error-unmatch` 逐件在位（6529209）、去重后无重复；S1–S8 涉及文件集与 43 件**双向差集＝空**（publish.py×1＋bundle.lock×1＋EAC×6＋sop 副本/卷×3＋config×6＋hooks.json×1＋scripts×14＋docs×2＋orchestration 七卷×7＋plugin.json×2＝43，逐类清点相符；S7 五卡不入列＝票面自述，实测五卡对 `SWB-|A-1x|TKT` 及扩展 pattern 均零命中）。
2. **assembly_exclude 五件 ↔ A1 find 五类一一对应**：README.md／docs/SWB-交接件*／skills/deep-research/README.md／skills/external-advisor-collab/references/90-changelog.md／tests/ ↔ A1 五类逐类同；装配面现面实测该五类全在（README×2、docs 含交接件、90 件、tests/28 文件），真源五件 git 跟踪在位、票面禁动面锁定——exclude 只作用装配面，无顺手动真源口子（发布链只读 git archive blob）。
3. **装配面 README/tests 无漏裁**：面内 README.md 恰 2 份（根＋deep-research，均在 exclude 精确项）；tests 目录面内仅根级 1 个；`.collab/.scratch` 真源 README 已按段排除（publish.py L730 实测）。
4. **A0 前提成立且执行序可行**：现码 `do_assemble` 无 prune 步（实测 plan→落盘→记账结构；幂等短路只比 new_hashes 末块集，存量残留不会被清）——「不删旧面 exclude 不生效于存量」判断正确；删面重跑后 COPY.state 随面同删、账块重建，幂等路径干净。`git_clean_or_die -uno`＝已跟踪零改动即放行（未跟踪只报不拦），票据/审票件落 .collab 不阻装配。
5. **exclude 键缺席＝行为零变化**可行：现码读 lock 用 `lock.get(...)` 系例，新增顶层键对 deep-research 等其余 bundle 无波及（本仓仅此一份 bundle.lock，实测）。
6. **fail-closed 非法项口径可在码**：现码已有 `die_usage` 先于写面（装配步校验段实测全部先于落盘）；S1 要求取源与幂等对账共用同一谓词——现码两处循环（plan 构造 L865-875 区 / new_hashes L882-887 区）结构上可挂同一函数，票面「禁两套逻辑」约束正确。
7. **A3 主式在装配面现面的命中集＝S1–S6 闭集 ∪ exclude 五类 ∪ 白名单**（逐目录实测）：agents 目录、templates、deep-research 正文（非 README）、software-orchestration 除 L3 头注外、settings.json、avatars、plugin.json、.codebuddy-plugin、两包 STRUCTURE.md＝全部零命中；有命中的保留件全部落入 S3/S4/S5/S6 动作清单。S4 硬约束实测咬合：`table_notes["判据真源双层双址"]` 键＋`tests/` 字样＝tests/s2/test_lease_instantiation.py:81-82 在位断言实读确认；hooks.json 仅结构断言（test_enforcement t01 实读）。
8. **A4 在保留面命中集全覆盖**（现面取样）：两基线副本正文 commit 锚（arch L61/L124/L144＝dc2d4e6/a0fd121/7342f2f，product L56＝dc2d4e6）＝口径②白名单；baseline-backfill-demo 2 处＝A4 显名白名单；software-orchestration 七卷 L3×7＝S6 清除；seat-permissions L59（ff72b92）／hooks-map L5（ba0c785）＝S4 清单内行号。bundle.lock 不入装配面（body_exclude 实测 LOCK_FILENAME），其 note 内 7 位哈希（6d80232/730962e）不进 A4 扫描面——S8 随换钉自包含化属仓侧卫生，无门禁碰撞。
9. **S2 改指落点实测成立（装配面）**：目标件装配面在位 `skills/software-orchestration/references/handoff-discipline.md`，其 §三 标题实读＝「三正面判据（决策/设计类交接件）」、三判据句（引用闭集可达／无第三方过程痕迹／状态词只述现行效力）逐字在位——票面「指向成立」核验通过（源仓面包面不可达问题见 R2）。
10. **A5 现值与升序链成立**：plugin.json L3／.codebuddy-plugin/plugin.json L3／bundle.lock bundle.version 三同源现值均 `0.1.23`；EAC SKILL.md frontmatter `version: 1.1.2`；tag 列表现含 v1.0→v1.1.2、v1.1.3 不存在——S8 次序（S2 commit→tag→换钉→exclude→清扫）＋装配器 ref 不可解析＝exit 3（git_ref_commit_or_die 实读）保障收齐后方可 A1。
11. **A6 取数容错如实**：ledger-init.sh 现行 heredoc `except: print("missing")` → 非 negative 一律主路（实读 L20-28＋else 分支），tests/ 裁除后无 FATAL 路径；票面「非新增能力」自述诚实。`SWB_LEDGER_ROOT` 重定向＝无仓残留可判（LEDGER_ROOT 默认仅 $PWD/.collab/ledger）。
12. **A2 幂等读数可判**：现码幂等短路打印「装配面已一致（第 N 块，M 文件），零写入」＋exit 0（L888-894 实读）——exclude 生效后新块不含被裁件、复跑对账同口径（受 S1 同谓词约束保障），A2 判据文本可机械执行。

---

## 修单摘要（给主理人）

1. A3 补充扫描：显式排两基线副本正文（或将 §口径3 ②扩至「副本正文规范转录文本本体」入 A3），消除与禁动面的不可清零冲突（R1）。
2. A7：「清零」改「S2 触及件清零＋90 件 4 条＋.scratch 历史票 1 条＋S2 新指针 1 条＝逐笔 EXEMPT 登记」；前后发现数锁同口径跑法读数（R2）。
3. 票面补登记 deep-research 消费侧 README 引 4 处悬垂（Y1）；S2 注补「包面＝装配面口径」（Y2）。

（红线自检：本件未改票面、未动闭集件、未写禁动面；全部结论以实测读数承载，可复核。）
