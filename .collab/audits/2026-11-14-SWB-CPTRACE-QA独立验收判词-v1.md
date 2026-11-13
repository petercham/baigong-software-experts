# SWB-CPTRACE · QA 席独立验收判词 v1（fresh eyes·一切判据本席现跑）

- 验收席：qa-cptracev（QA 席·独立验收轮）
- 规格真源＝`.scratch/tickets/2026-11-14-SWB-CPTRACE-候补池新批规格票-v1.md`（v1 R1·链上 4f8be48＋613b581）
- 验收对象＝施工笔 `0d36f90`（尾标 [SWB-CPTRACE-BUILD]）＋回执笔 `32eb065`（尾标 [SWB-CPTRACE-RECEIPT]）；链＝613b581 → 0d36f90 → 32eb065
- 工程师回执件＝`.scratch/tickets/2026-11-14-SWB-CPTRACE-工程师回执-v1.md`
- fresh eyes 声明：本席未读工程师席任何过程留痕（其 scratch 取证族已随完工自删亦未找）；一切读数本席现跑，票面与回执钉值只作对拍对象不作抄值。
- 体例自证：本判词对各席 scratch 取证族留痕仅叙述性提及＝裸文写全角斜杠不落可达全径（受 dev-discipline §八 第 5 项约束·本票 S1 新条款对判词同样生效）；反引号路径形态引用者均已实测在场。

## 〇、开工读数（本席验收轮现跑）

- `date`＝`Sat Nov 14 03:57:11 2026`
- `git rev-parse --short HEAD`＝`32eb065`（＝派工预期链顶全等）
- `git status --porcelain`＝tracked 脏面只剩 ledger 一枚他案照登零带入＝M agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl；仓根 untracked 散件群照登不入（仓根 .collab／ 案卷散件十二枚＋仓根 .collab／research／ 散件六枚＋散件 .py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt）
- 链面坐实：`git log 613b581..32eb065` 恰两笔，尾标依序 [SWB-CPTRACE-BUILD]／[SWB-CPTRACE-RECEIPT] 全等；`git diff --name-only 613b581..32eb065` 恰三件＝dev-discipline＋SCRATCHCFG 票附回执＋CPTRACE 工程师回执，与派工预期全等。
- 开工窗 index.lock＝free（未撞锁）。

## 一、V0–V7 逐条现跑读数

### V0 开工基线（口径写死：本席开工时点已为施工后态，前像取 0d36f90^＝613b581 态 blob 现靶；回执现态独立复跑佐证见 V3）

- 靶检 SCRATCHCFG 票附回执**前像**（613b581 态）→ exit **1**·BLOCK 恰 **3**（行 24／25／73·悬空目标均指已自删的工程师 scratch 取证族＝裸文写 .scratch／tickets 前缀下 SWB-SCRATCHCFG 族内 v0-s4-before.txt、v0-block-before.txt、v7-rungates-before-build.txt 三枚）＋NOTE-FXU28 短式归位注记一枚（行 43）不进 findings——与票面 §一在册读数全等；回执笔现态复跑 exit **0** 佐证见 V3。
- 靶检 dev-discipline **前像**（613b581 态）→ exit **1**·BLOCK 恰 **2**（前像行 110／126 两枚对包文档全径悬空＝裸文写 docs／STRUCTURE.md 反引号可解析形态＝既存基线非本笔引入，系既存坐实）。
- 缺省面 BLOCK 计数现跑见 V4（本席开工窗现跑即施工后态＝22827，与回执声称值对拍差 0）。

### V1 条款落位

- `grep -c "scratch 取证族可达路径不入留存工件"` 于 dev-discipline＝**1** ✓
- `grep -c "受 §八 第 5 项约束"` 于 dev-discipline＝**1** ✓
- 条款本体逐字：本席程序化从票面 §三 S1-a 围栏提取（去围栏行）→ 原始文本级 `in` dev-discipline 判据＝**True** ✓；S1-b 短句同法 `in`＝**True** ✓。

### V2 条款面零回归

- 靶检 dev-discipline 现态 → exit **1**·BLOCK 恰 **2**＝V0 前像同值 ✓（现态行号 111／127＝前像 110／126 因 S1-a 在其前插入一行整体下移一位，枚数与目标字样零变＝零新指针坐实；S1-a 条款内反引号 token `.scratch/<票号>/` 带尖括号不当路径形态＝本席 V7 现靶 exit 1 恰 2 不含新枚直接佐证）。

### V3 回执复原兑现

- 靶检 SCRATCHCFG 票附回执现态 → exit **0**·BLOCK 计数 **0** ✓（一次收敛，无需 §四收敛再处置）。
- 改动三行现文核形态：行 24／25／73 均已为裸文形态＝去反引号＋全角斜杠＋随注「裸文写·已随完工自删」，基名三枚逐一对上 ✓。

### V4 缺省面零扰动

- `python share/check-pointers.py 2>/dev/null | grep -c "BLOCK"` 本席现跑＝**22827**；对回执声称值 22827 对拍差＝**0** ✓（无窗差，无需 EXEMPT 归因）。

### V5 门禁零回归

- `bash share/run-gates.sh` → **GATE PASS exit 0** ✓·发现数现跑＝**151457**，对回执声称 151457 对拍差＝0（无窗差）；无新红栏。

### V6 声明闭集与零动自证

- 面核：BUILD 笔面恰两件（dev-discipline numstat 2增1删＋SCRATCHCFG 票附回执 numstat 3增3删）；RECEIPT 笔面恰一件（CPTRACE 工程师回执）；全窗 `613b581..32eb065` 恰三件封顶 ✓（多一无少＝否·核过）。
- dev-discipline blob 级零动自证：后像删去 S1-a 插入段与 S1-b 追加短句后与 613b581 前像 **逐字节相等＝True** ✓；分段严格前缀判据补核＝True ✓；hunk 恰两枚（@@ -41,7 +41,7 @@ 与 @@ -83,6 +83,7 @@）✓。
- 回执件零动自证：前后行数相等（86＝86）；改动行恰 **[24, 25, 73]** ✓；禁触行 37／43／55／85／86 逐行相等＝True×5 ✓；除三行外全文件逐字节零动＝**True** ✓。

### V7 本票面与施工面防自咬

- 三件现靶：CPTRACE 票面 → exit **0**·BLOCK 0 ✓；CPTRACE 工程师回执 → exit **0**·BLOCK 0 ✓；dev-discipline → exit 1·BLOCK 恰 2＝V2 既存两枚、无新自咬枚 ✓。
- 本判词件落笔前靶检 exit 0（读数见本席 commit 前跑·commit 面留痕）。

## 二、对抗三臂（判据非虚设证明·副本上验·验完随本席 scratch 族自删）

- **臂A**：dev-discipline 复制副本，改动条款本体一字（「叙述性」→「叙述型」）→ V1 逐字 `in` 判据＝**False（红）** ✓（标题句 grep 仍 1 恰证逐字 in 判据不可被单 grep 替代）。
- **臂B**：SCRATCHCFG 票附回执复制副本，恢复行 24 反引号全径形态 → 靶检回 **exit 1·BLOCK 1**（行 24 悬空再现）✓＝V3 exit 0 非虚设。
- **臂C**：回执复制副本，三行之外任意一行（行 20）改一字 → 逐字节零动判据＝**False（红）**、改动行恰三判据＝False ✓＝V6 行级零动判据非虚设。

## 三、窗差归因

- V4：现跑 22827＝回执声称 22827，差 0，无窗差。
- V5：现跑发现 151457＝回执声称 151457，差 0，无窗差。
- 本席开工窗＝回执落链后即时窗，无他案笔插入，全链读数零窗差。

## 四、总判

**IS_PASS**·红 **0**／黄 **0**／绿 **8**（V0–V7 全绿）＋对抗三臂全按预期翻红（判据非虚设坐实）。

- 条款面（S1-a/S1-b）逐字落位·零回归；存量三枚复原兑现·exit 0 收敛；缺省面与门禁零扰动；闭集恰三件封顶·blob 级零动；防自咬三件达标；链面两笔尾标与 diff 面全等。
- 他案脏面（ledger 一枚＋仓根 untracked 散件群）照登零带入；链上 FUXI 笔群照登零碰；禁动面抽查（share／ 两 config 与 FUXI 面均不在 diff 面内）零碰属实。
- 本判词仅一枚 commit（判词一件）；纪律自证＝pathspec 两端齐带·add 紧邻 commit 无窗口·FX_COMMIT_DECLARE 环境变量形态·禁 add-A／amend／no-verify 全程未用·message collab 前缀零 at 零反引号尾标 [SWB-CPTRACE-QA-VERIFY]·commit 输出重定向本席 scratch 族落盘·timeout 七分钟档·撞锁有界等待零删锁·临时工作物居本席 scratch 票号族完工随族自删。

——qa-cptracev·判词落 `.collab/audits/2026-11-14-SWB-CPTRACE-QA独立验收判词-v1.md`
