# SWB-CPTRACE · 工程师席施工回执 v1（票附回执·tickets 桶·(h) 体例）

- 票号：SWB-CPTRACE
- 票面真源：`.scratch/tickets/2026-11-14-SWB-CPTRACE-候补池新批规格票-v1.md`（v1 R1 修订态·正文 §三/§四/§五/§六＝唯一依据·逐字照做零现场改写）
- 施工席：工程师席 eng-cptrace1（一票一新鲜实例·票间串行）
- 回执落名：`.scratch/tickets/2026-11-14-SWB-CPTRACE-工程师回执-v1.md`（＝声明闭集第二件）
- 两笔：笔一施工笔＝`0d36f90`（条款面 S1 两处＋存量三枚复原同批一笔）；笔二＝本回执笔（链上 sha 见 commit 面自证）
- 体例自证：本回执正文对本席及他席 scratch 取证族留痕仅叙述性提及＝族名/基名裸文写＋全角斜杠，不落反引号可达全径＝本票 §三 S1 新条款首件实践

---

## 一、开工读数（当轮现跑·禁抄票面钉值）

- `date`＝`Sat Nov 14 03:36:42     2026`
- `git rev-parse --short HEAD`＝`613b581`（＝票面 R1 勘正笔＝链顶·与派工预期起点全等）
- `git status --porcelain`＝tracked 脏面一枚他案照登零碰零带入＝M agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl；仓根 untracked 散件群照登不入（仓根 .collab／ 案卷散件十四枚＋散件 .py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt＋仓根 .collab／research／ 散件五枚）＝与票面 §〇 登记面全等
- 开工窗 index.lock＝free（未撞锁）

## 二、V0 开工基线三条（落笔前当轮现跑）

- 靶检 SCRATCHCFG 票附回执 → **exit 1**·BLOCK 计数 **3**（＝票面 §四处置前读数全等）
- 缺省面 BLOCK 计数现跑（python share/check-pointers.py 2>/dev/null 管至 grep -c "BLOCK"）＝**22827**（留痕＝本席 scratch 票号族 v0-cp-default.txt·裸文写·完工随族自删·与票面 §〇 钉值全等）
- 靶检 dev-discipline 落点文件 → **exit 1**·BLOCK 恰 **2**（＝票面 §五 V0 括注在册的既存两枚＝行 110／126 对包文档全径悬空·S1 改动前既有）

## 三、V 系完工自验全跑读数（逐条达标）

- **V1 条款落位**：grep 计数「scratch 取证族可达路径不入留存工件」＝**1**；grep 计数「受 §八 第 5 项约束」＝**1**；条款本体逐字对拍＝票面 §三 S1-a 围栏内容（去围栏行）与 S1-b 短句原始文本级 in 判据 **True**（python 程序化提取票面围栏段逐字比对）
- **V2 条款面零回归**：靶检 dev-discipline → **exit 1**·BLOCK 恰 **2**＝V0 同值（S1 新增行零新指针＝尖括号形态坐实）
- **V3 回执复原兑现**：靶检 SCRATCHCFG 票附回执 → **exit 0**·BLOCK 计数 **0**（NOTE-FXU28 注记行在场不进 findings·处置一次收敛未触发同式复原复跑）
- **V4 缺省面零扰动**：完工侧缺省 BLOCK 现跑 **22827** − 开工窗现跑 **22827** ＝ **0**（该件不在缺省域坐实兑现）
- **V5 门禁零回归**：bash share/run-gates.sh → **GATE PASS exit 0**·发现 **151457**（＝SCRATCHCFG 链上读数同值·零回归不升新红栏；留痕＝本席 scratch 票号族 v5-rungates.txt·裸文写·完工随族自删）
- **V6 声明闭集与零动自证**：笔一链上 git show --name-only 面＝**恰两件**＝dev-discipline＋SCRATCHCFG 票附回执（多一无少＝违例·达标）；blob 级对拍＝dev-discipline 后像删去 S1-a 插入段与 S1-b 追加短句后与 HEAD blob **逐字节相等**（recon equals True·unified diff n=0 hunk 恰两枚＝@@ -44 +44 @@ 与 @@ -85,0 +86 @@＝改动面恰＝§三第 3 行替换＋§八第 5 项插入·其余逐字零动）；回执件行级对拍＝改动行恰 **[24, 25, 73]** 三行·行数前后 87＝87·禁触行 37／43／55／85／86 逐行相等 **True**＝除三行外逐字节零动
- **V7 落笔前靶检**：笔一 commit 面＝STAGED-DECL staged 2｜声明 2｜超额 0·pre-commit check-pointers 对 staged 面跑过 GATE PASS 不拦（链上留痕＝笔一 commit 日志）；本回执件落笔前靶检 **exit 0** 才 commit（读数在回执笔 commit 日志）

## 四、施工面自证（声明闭集两件封顶·两笔封顶）

- 笔一（`0d36f90`）面＝恰两件＝agent-experts／baigong-software-team／skills／software-orchestration／references／dev-discipline.md＋.scratch／tickets／2026-11-11-SWB-SCRATCHCFG-工程师回执-v1.md（numstat 5增4删＝dev-discipline 一行替换＋一行插入＋回执三行改写）
- dev-discipline 改动两处（逐字照录票面·零现场改写）：§八 第 4 项之后新增第 5 项（插入位置＝原第 85 行之后·S1-a 围栏内容逐字）；§三 第 3 项句尾追加随动短句（S1-b 逐字）。除此之外该文件逐字节零动（V6 blob 级对拍达标）
- 回执件三枚处置（逐枚按 §四处置指令）：行 24／行 25／行 73 反引号包裹的 scratch 族全径 token 改裸文形态＝去反引号＋半角斜杠换全角斜杠＋随注「裸文写·已随完工自删」（基名 v0-s4-before／v0-block-before／v7-rungates-before-build·均指已自删的 SCRATCHCFG 工程师取证族）；禁触五行零动
- 行尾注记：dev-discipline 工作盘曾被宿主 autocrlf 落为 CRLF，本席已复原为 LF 与 blob 同形态（零动自证以 git blob 字节面为基面·autocrlf 换端警告如实照登）；两文件 blob 内容改动面均恰如上，无行尾污染入链
- 禁动面自证：`share/` 全域零改（check-pointers.py／baseline-pointer-exempt.json／check-pointer-closure.py／run-gates.sh 一字未碰·未扩豁免 items）；FUXI 面零碰；史件 append-only 零回改（仓根与两包 .collab／ 案卷三件套、ADR 落盘面、ledger／leases／config、SCRATCHCFG 票面真源与 QA 判词本体一字未碰·唯一例外＝S2 点名回执三行定向复原）；他案脏面（ledger 一枚＋仓根 untracked 散件群）照登零带入；`tests/` 面本票未跑未改（票面未列跑项）

## 五、纪律自证（commit 全套·两笔各自）

- pathspec 两端齐带（add 与 commit 均带同件清单）；add 与 commit 同命令链紧邻无窗口；`FX_COMMIT_DECLARE` 环境变量形态＝仓根相对纯路径清单（笔一两件逗号分隔／笔二一件）；禁 add-A／禁 amend／禁 --no-verify 全程未用；message `collab:` 前缀＋尾标 [SWB-CPTRACE-BUILD]／[SWB-CPTRACE-RECEIPT]·零 at 符号零反引号；commit 输出重定向本席 scratch 票号族落盘（build-commit.log·裸文写·完工随族自删）；timeout 八分钟档；开工窗 index.lock free 照登·全程未撞锁零删锁；落笔前靶检 exit 0；他案脏面照登零碰零带入
- 开工窗插曲如实照登：笔一首次 commit 尝试因 FX_COMMIT_DECLARE 前缀式赋值未穿透 pre-commit 钩子进程环境，被 STAGED-DECL-BLOCK 拦下（声明 0＝钩子侧读数）＝未落链零副作用；随即改 export 形态重跑 add＋commit 紧邻链，第二次 STAGED-DECL＝staged 2｜声明 2｜超额 0 落链。首次拦截件＝机检按规运作样本，非违例
- 临时工作物＝本席 scratch 票号族（SWB-CPTRACE-eng＝靶检留痕／缺省面基线留痕／V6 对拍脚本／commit 日志）＝完工自删（自删读数见本席完工回报）
