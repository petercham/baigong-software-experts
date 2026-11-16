# SWB-RCTPATH-R3 · 施工回执 v1（工程师席 eng-rctb3·回流四型之「完成」）

- 票号：SWB-RCTPATH-R3
- 收件人：主理人（team-lead）
- 目的：完工回传——行 28 节题去编号单行替换 BUILD 笔＋本回执 RECEIPT 笔两笔链态与逐项硬判据实测读数登记，供 fresh QA 独立验收。
- 来源：【来源】eng-rctb3（工程师席）·按票 §二 写死规格与放行登记 §二 硬化口径施工。
- 状态：待处理

> **本回执体例自证**：本回执正文对仓内文件的提及一律仓根相对纯路径（正斜杠）＝落点件《留存过程件正文内的仓内文件引用写法（两域两制）》第 2 目自我实践（该节题去编号形态＝本票施工成果）。引用旧行／新行用 ⟦⟧ 标记。落笔后本回执自靶 `share/check-pointers.py` exit 0（读数见 §四）。

## 〇、开工读数（现跑·与放行登记硬化项对齐）

- git rev-parse --short HEAD ＝ **daebaa4**（＝放行登记笔＝派工预期链顶·如实登记）。
- 票面 blob sha 钉版核对：git ls-tree 0f4291c 对 .scratch/tickets/2026-11-16-SWB-RCTPATH-R3-20-handoff节题去编号微票-v1.md → blob sha ＝ **90e901a155b35e5efbbba52ed55d4b04973994b4**，与派工预期**全等一枚** ✓（放行登记 §二-2 硬化项坐实）。
- 放行登记全文已读：.collab/decisions/2026-11-16-SWB-RCTPATH-R3-放行登记-v1.md（39 行）。
- 旧行链上版提取：git show 0f4291c 版落点件行 28 verbatim ＝ ⟦### 二之二、留存过程件正文内的仓内文件引用写法（两域两制·决策者裁定 SWB-RCTPATH 甲案）⟧，与施工规格旧行**逐字符全等**·未凭工作区或记忆改写 ✓。
- 落点件开工基线现跑：agent-skills/multi-collab/references/20-handoff.md wc -l＝**66**；grep -c「二之二」＝**1**；grep -c「决策者裁定」＝**1**；节题行号 grep -n ＝ 5／9／12／**28**／36／55／62（六节＋模板示例行 12 原位）——与放行登记 §〇 全等。
- git status --porcelain 照登零带入零清理＝ledger 一枚 M 态（agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl）＋仓根散件群（.collab 根散 md 十二枚／.collab/research 散 md 六枚／.py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt）——全部他案脏面，本票零带入。

## 一、施工内容（严格照票 §二＋放行登记 §二-3）

- 落点件＝agent-skills/multi-collab/references/20-handoff.md（66 行），**仅行 28**。
- 单行替换：旧行 ⟦### 二之二、留存过程件正文内的仓内文件引用写法（两域两制·决策者裁定 SWB-RCTPATH 甲案）⟧ → 新行 ⟦### 留存过程件正文内的仓内文件引用写法（两域两制）⟧（规格 verbatim·一字不改）。
- 施工手段＝精确字符串替换（Edit 工具单处替换·非重写文件）。
- 同件行 1–27、29–66 零触碰（行 24 悬空枚零处置·行 29–34 甲案条款正文条目 1–5 零改动）。

## 二、两笔链态

- **BUILD 笔** sha ＝ **80e8612**（git show --stat＝恰一件＝落点件·1 file changed, 1 insertion(+), 1 deletion(-)）·message collab: 起头·尾标 [SWB-RCTPATH-R3-BUILD] 置最末。
- **RECEIPT 笔** sha ＝ 本回执落链笔（见 git log 链顶·尾标 [SWB-RCTPATH-R3-RECEIPT] 置最末）。
- 两笔串行：先 BUILD 后 RECEIPT·一票一新鲜实例·工程师席单席在飞。

## 三、逐项硬判据实测读数（施工后现跑）

- **diff 面**：git diff --stat 落点件＝**1 insertion 1 deletion**；git diff 全文＝**仅行 28 一块 hunk**（@@ -25,7 +25,7 @@）✓。
- **行数**：wc -l 落点件 **66→66** ✓。
- **grep 两项**：grep -c「二之二」该件 **1→0** ✓；grep -c「决策者裁定」该件 **1→0** ✓（两项同居旧行 28）。
- **节题行号不动位**：grep -n 实测＝5／9／12／**28**／36／55／62 ✓（行 28 新节题 ⟦### 留存过程件正文内的仓内文件引用写法（两域两制）⟧ 原位）。
- **V4′ 自靶**：python share/check-pointers.py --root . --target agent-skills/multi-collab/references/20-handoff.md → **exit 1·恰一枚悬空＝行 24**（BLOCK OA-D6 deliverables/experts/baigong-software-team/skills/software-orchestration/references/handoff-discipline.md 旧径·另案候补池性质零处置）——与基线**全等零新增** ✓。
- **三钉值现跑**（count 脚本口径照先例＝缺省扫描输出 grep -c）：python share/check-pointers.py 全输出 → grep -c BLOCK＝**22810**、grep -c WATCH＝**4581**——与放行登记 §〇 在册值**全等零摆动** ✓（全仓 run-gates 系验收席射程·本席未跑）。
- **边界坐实**：git status 坐实施工后 tracked M 面＝ledger 一枚（他案脏面·未碰）＋落点件一枚（本票自件）——该件外零新增 M ✓；BUILD 笔 git diff --cached --name-only 坐实仅自件 ✓。

## 四、本回执自靶（落链前现跑）

- python share/check-pointers.py --root . --target .collab/receipts/2026-11-16-SWB-RCTPATH-R3-施工回执-工程师席-v1.md → **exit 0** ✓（正文提及文件一律仓根相对纯路径·旧径引用段无）。

## 五、完成清单

1. 开工读数四项坐实（HEAD daebaa4／票面 blob sha 全等／放行登记 39 行全读／旧行链上版提取）✓
2. 单行替换施工·逐项判据全绿 ✓
3. BUILD 笔 **80e8612** 落链（FX_COMMIT_DECLARE 挂 commit 命令侧＝纯路径清单仅落点件·STAGED-DECL staged 1｜声明 1｜超额 0）✓
4. 本回执件落链 RECEIPT 笔 ✓
5. scratch 自删确认：本席无 scratch 工作区残留（本票纯 Edit 单处替换·未建 scratch 子目录；git status 坐实无本席新增散件）✓

## 六、红线自查

- 只写落点件＋回执两件：agent-skills/multi-collab/references/20-handoff.md 与 .collab/receipts/2026-11-16-SWB-RCTPATH-R3-施工回执-工程师席-v1.md——其余零写 ✓
- 链上历史件 append-only 零回改（含链上一切「二之二」字样与行 24 悬空）✓
- share/ 门禁配置零触·ledger／leases／.gitignore 零手写·他案脏面零带入 ✓
- 纪律：禁 add -A／禁 amend／禁 no-verify·add 紧邻 commit·commit 前坐实仅自件·message collab: 起头零 at 零反引号·尾标置最末·commit 类 timeout 十分钟档·未撞锁（index.lock 未遇·有界等待未触发·零删锁）✓
