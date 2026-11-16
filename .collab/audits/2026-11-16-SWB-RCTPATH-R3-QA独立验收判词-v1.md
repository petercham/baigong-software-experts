# SWB-RCTPATH-R3 · QA 独立验收判词 v1（fresh eyes·全判据亲跑）

- 票号：SWB-RCTPATH-R3
- 验收席：qa-rctb3v（fresh QA 实例·不读工程师席过程·只以链上件＋现盘独立验证）
- 验收对象：微票 SWB-RCTPATH-R3 施工批（票面笔 0f4291c→放行登记 daebaa4→BUILD 80e8612→RECEIPT adaa7ed）
- 依据件：⟦.scratch/tickets/2026-11-16-SWB-RCTPATH-R3-20-handoff节题去编号微票-v1.md⟧（票面）；⟦.collab/decisions/2026-11-16-SWB-RCTPATH-R3-放行登记-v1.md⟧（放行登记·§二 硬化口径）；⟦.collab/receipts/2026-11-16-SWB-RCTPATH-R3-施工回执-工程师席-v1.md⟧（回执·仅对盘不抄读数）
- 体例自证：本判词提及文件一律仓根相对纯路径（正斜杠）；引用既有原文以 ⟦⟧ 标记；路径不落反引号指针（防自咬）。落链前本判词自靶 python share/check-pointers.py --root . 对本件实路径 exit 0（读数见 §四）。

## 〇、开工读数（当轮现跑·禁抄旧数）

- 时点＝date 实测 2026-11-16 当轮；HEAD＝git rev-parse --short HEAD ＝ **adaa7ed**（＝RECEIPT 笔＝链顶·与派工预期全等 ✓）。
- 票面 blob sha 钉版核对＝git ls-tree 0f4291c 对 .scratch/tickets/2026-11-16-SWB-RCTPATH-R3-20-handoff节题去编号微票-v1.md → blob sha ＝ **90e901a155b35e5efbbba52ed55d4b04973994b4**，与派工预期／放行登记 §二-2 硬化项**全等一枚** ✓（旧行取证以链上版为准，未凭工作区或记忆）。
- 三件（票面／放行登记／回执）全文已读。
- tracked 脏面照登＝ledger 一枚 M 态（agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl）＋仓根散件群（.collab 根散 md／.collab/research 散 md／.py／.scratch_uds 系／.scratch_wbdocs.html／assert-modified-run2.txt）——全部他案脏面，本席零带入零清理。

## 一、V 系逐判（红／黄／绿）

### V1 新行 verbatim 对盘 — **绿**

python 单行提取现盘 agent-skills/multi-collab/references/20-handoff.md 行 28 ＝ ⟦### 留存过程件正文内的仓内文件引用写法（两域两制）⟧，与判词侧独立写死的期望串（决策者亲选自然题形态·零序号·零 ID 注记·全角括号）**逐字符 EQUAL**；与放行登记 §二-3 写死的新行形态全等。

### V2 diff 面窄 — **绿**

- git show --stat 80e8612 ＝恰落点件一件·**1 file changed, 1 insertion(+), 1 deletion(-)**；
- git diff --numstat 80e8612^ 80e8612 ＝ 1 1 仅落点件；
- 全 diff hunk 头恰一枚＝@@ -25,7 +25,7 @@（仅行 28 一块）；diff --git 文件清单恰一枚；
- BUILD 面旧行（80e8612 父面行 28）与链上 0f4291c 版落点件行 28 两路 git show 提取比对＝**逐字符 EQUAL**（＝旧行未经中间笔篡改）。

### V3 结构 — **绿**

- wc -l 落点件＝**66**；链上 0f4291c 版同件 wc -l＝**66**（66→66 等式坐实）；
- grep -c「二之二」该件＝**0**；grep -c「决策者裁定」该件＝**0**（两字样曾同居行 28，现该件内绝迹）；
- 节题行号实测：grep -n '^## \|^### ' ＝ 5／9／28／36／55／62；扩至全部标题形态行（含行 12 模板示例行 # <件号>）＝ 1／5／9／12／28／36／55／62——与派工口径 5／9／12／28／36／55／62 **不动位** ✓（新旧两版标题行号集经 python 对拍完全一致）；
- 节序语义＝一（行 5）／二（行 9）／新自然题（行 28）／三（行 36）／四（行 55）／五（行 62）完整连续，放行登记口径「旧『二之二』槽位由新自然题逐字替换，余槽零变」坐实。

### V4′ 差量基线 — **绿**

python share/check-pointers.py --root . --target agent-skills/multi-collab/references/20-handoff.md → **exit 1·恰一枚悬空＝行 24**（BLOCK OA-D6·deliverables 旧径 handoff-discipline.md 悬空），内容逐字＝票 §〇／放行登记 §〇 在册基线，**零新增 BLOCK／WATCH**；行 24 该枚仍另案候补池性质，本票零处置 ✓。

### V5 全仓门禁现跑全等 — **绿**

- bash share/run-gates.sh → **GATE PASS exit 0·发现 151502**（与三钉值派工预期全等）；
- 缺省扫描 python share/check-pointers.py 全输出 grep -c BLOCK ＝ **22810**、grep -c WATCH ＝ **4581**——与在册钉值全等零摆动。

### V6 历史件零回改 — **绿**

- 「二之二」史账命中对拍：git grep -c 于 0f4291c 与 HEAD 两态——基线 7 件命中数（1/1/1/1/2/1/8）在 HEAD 全部**原值在位**，新增 4 件命中全部居本链 R3 新件（快审判词两件／放行登记／回执），**零件回改**；
- 链锚十四枚 git cat-file -e 逐枚＝4ea0d58／89f796d／b6a4ac6／cbadb15／0da2566／659ec9a／5adf535／b2b61d7／0f4291c／3b82e59／2fed3cc／daebaa4／80e8612／adaa7ed 全部在位 exit 0；git log 顺序核对＝4ea0d58→89f796d→…→b2b61d7→0f4291c→2fed3cc／3b82e59→daebaa4→80e8612→adaa7ed 顺序无断（2fed3cc 与 3b82e59 双席判词先后无碍＝两笔各恰一件互不涉）。

### V7 回执对盘 — **绿**

回执 §〇／§三 各项宣称读数与本席亲跑值逐项一致，零不实：HEAD 链态（daebaa4 开工→80e8612→RECEIPT）✓；票面 blob sha 全等 ✓；旧行链上版提取＝放行登记在册 verbatim ✓；wc -l 66 ✓；grep 两项 1→0 ✓；节题行号含行 12 原位 ✓；V4′ exit 1 恰一枚行 24 ✓；三钉值 22810／4581 ✓（回执自述未跑全仓 run-gates＝如实留白，本席已补跑 151502 全等）。
甲案条款第 2 目自我实践抽查：回执正文提及文件（落点件／放行登记／share/check-pointers.py／链上判词件等）一律仓根相对纯路径形态，零盘符、零反引号包路径、零包根相对形态 ✓；回执自靶 --target 本席复跑 **exit 0** ✓。票面自靶 --target 复跑 **exit 0** ✓。

## 二、对抗臂（四发·全部零命中）

1. **篡改面**：git diff HEAD -- 落点件（工作区 vs HEAD 面）＝**0 行**＝工作区与链上面一致，无未落链漂移 ✓。
2. **新行 token 扫描**：行 28 新行 python 检反引号＝无；检斜杠／.md／.py／.json 等路径 token＝**零**；无编号前缀残留 ✓。
3. **条款正文零扰动**：git show 80e8612 版行 29–34 与 0f4291c 版同区间 python 逐字节比对＝**byte_equal True**（双侧区段 sha256 前缀 ab5024f213fdc4bd 全等）——甲案条款条目 1–5 一字未动。
4. **他案脏面零带入**：链上六笔（0f4291c／2fed3cc／3b82e59／daebaa4／80e8612／adaa7ed）git show --name-only 逐笔清单＝**各恰一件**且均为本案自件（票面／两判词／放行登记／落点件／回执），ledger 及仓根散件群无任一卷入 ✓。

## 三、总判

**IS_PASS**。红 **0**·黄 **0**·绿 **7**（V1–V7）。无修正指令。

取向生效确认：BUILD 落链笔 80e8612 已落·「留存过程件正文内的仓内文件引用写法（两域两制）」去编号自然题节题现盘在位；「今后规范面插新节不造 X 之二」以先例＋票面成文生效（票 §二-S2 自决口径·双席零修单背书）。

## 四、本笔自证

- 本笔面＝恰本判词件一件；规范面／票面／链上件／门禁配置／账本面全程零触碰；他案脏面零带入。
- 落笔后自靶＝python share/check-pointers.py --root . --target .collab/audits/2026-11-16-SWB-RCTPATH-R3-QA独立验收判词-v1.md → **exit 0**（实跑读数随回报）。
- 临时工作物＝.scratch/qa_rctb3v/ 四枚对拍产物（门禁输出／缺省扫描输出／史账命中两份），完工自删（commit 留证随回报）。
- 纪律坐实：只写判词一件；禁 add -A／禁 amend／禁 no-verify；add 紧邻 commit；commit 前 git diff --cached --name-only 坐实仅自件；FX_COMMIT_DECLARE 挂 commit 命令侧；message collab: 起头零 at 零反引号；尾标 [SWB-RCTPATH-R3-QAV] 置最末；commit 类 timeout 600000ms。
