# SWB-WTGATE · QA独立验收判词（验收段·fresh eyes单席·票级）｜v1

> 票＝SWB-WTGATE（票面居 .scratch/tickets/2026-11-18-SWB-WTGATE-闸工具worktree感知两脚本判臂git原生定位置换票-v1.md）｜验收席＝QA席（qa-swb-wtgate-acc）｜日期＝2026-11-18｜性质＝票级独立验收判词（只审不裁·只读不写链·全程零 git 写操作，只读 git 命令不限）。
> 判词体例＝开工读数／逐判据读数表（红黄绿三态）／对抗臂／黄项如实／总判＋回执忠实性。全部读数当轮现跑；工程师回流件与起草回执读数只作互证参照，零复用自报值。
> 开工三读数现跑＝HEAD＝2d0116a9581f306da8940b41c875232089cd4b41（链顶＝工程师受阻回流件笔·分支 main 现读）；脏面照登＝仓根 .collab/board/2026-11-17-五份复盘合流与下一轮迭代计划-v2.md（M·他案）＋?? 散件群（含 .collab 散件／.scratch 取证群／.py 散件／agent-experts 下 states.json 与 ITER 票面散件等）＝全部他案与登记面零碰；锁面＝全程零撞 index.lock（本席只读 git 零写锁·等待轮数 0）。
> 链面现读＝8d6b6740（开工锚）→e5f5a3a6（票面笔）→d93da4a4（起草回执笔）→f1940a38（产品席审票判词笔）→c1ee8eb7（QA席审票判词笔）→b9982a04（放行登记笔）→811bd223（施工改动笔）→2d0116a9（受阻回流件笔＝链顶）父子逐笔现读相衔零断；reflog 顶三笔均为正常 commit 形态（零 amend 痕迹·非 amend 字样现读）。
> 账面对象对钉现读＝票面 blob fc5f51730ba29522ad44f97cdb072a0e1aea8a46／wc 203 行全等；起草回执 blob b888a582877229fa8d5e6b9e5e7b0197ecd3f426 全等（wc -l 47／按含末行无换行形制行数为 48＝两口径照登）；改动面两枚现 blob＝share/check-source-of-truth.py d7c261bf555ae2288720ecc3f8336790b366a65d 860 行／share/check-hook-health.py 7fd83074bf50144fa5220283da1f93e079e4d5ed 182 行＝对派工预期全等；两枚对 HEAD 工作面净（status 带两 pathspec 空集现跑·staged 面单空集＝工程师 staged 就位面已随 811bd223 落链坐实）。

---

## 一、逐判据读数表（红黄绿三态·全部当轮现跑·取证输出落 .scratch/SWB-WTGATE-qa/）

判据①主根零感知＝**绿（带黄注 Y1）**：
- 改后 csot 主根直跑（python share/check-source-of-truth.py --root 主根）＝exit 0，汇总行「模式 dual｜文件 129（agents 7＋skills 122）｜BLOCK 0（新命中 0）｜基线豁免 54（WATCH·键＝文本＋文件集合）｜指针 WATCH 413｜exit 0」对开工基线「dual｜BLOCK 0｜豁免 54｜WATCH 413」逐字全等（csot-mainroot-qa.log）。
- 改后 hook-health 主根直跑＝exit 0·snapshot 行「hooksPath-readings=0｜hook-blob=8b7857701594264421832edd30dae7e401f85719｜hook-mode=0o0」对基线逐字节全等（hook-mainroot-qa.log）。
- 全套闸主根现跑（bash share/run-gates.sh --root 主根 --no-write）＝exit 1 GATE BLOCK 恰一枚＝agent-experts/baigong-software-team/.workbuddy/memory/2026-11-18.md:34 OA-T1 BLOCK（他案记忆面日期字面·扫描域划界缺陷候补池在册）＝**非 GATE PASS 33389**。与起草基线日志全日志 diff＝20 行（gate-mainroot-diff-vs-draftbaseline.txt）＝全部归因他案与登记面：①check-pointers 新增 FUXI-FX-U50 回执 L9 悬空一枚（他案新落文件）②check-entity date count 0→1＋OA-T1 两行（他案记忆面）③check-ticket-reconcile 票 160→161／SKIP 117→118（本票链入册自然变动）④check-adr coverage 一行（staged 空·非 pre-commit 上下文）⑤GATE PASS→GATE BLOCK 裁决行。**两枚被改脚本的分项输出行零差**＝改动零扰动坐实；GATE PASS 基线不可复现归因环境面在他案窗，非本笔之害（见黄注 Y1）。

判据②worktree 两红归零＝**绿**：
- 对照基线红（旧 fuxi worktree 根 D:/multi-agent-collab-devkits.wt/agent-skills/fuxi-skill 全套闸现跑）＝exit 1 GATE BLOCK 恰一枚＝check-source-of-truth exit=2「usage error: 包目录不存在：../multi-agent-collab-experts/workbuddy/baigong-video-team」（gate-fuxiwt-qa.log）；**FX-HOOK-1 已消失**（该根 hook 分项 snapshot 行 hook-blob 在场）＝开工两红中钩子红归零。该根 csot 仍红＝run-gates L141 SCRIPTS 清单 ROOT/share/ 前缀取径取该工作区自带 checkout 旧副本（grep resolve_sibling_root 该根盘面计数 0 现跑坐实·该根 HEAD＝1aadaedc 旧检出）＝分发时序案型照登不作红判（派工已裁口径）。
- 兑现验证（验证工作区 D:/multi-agent-collab-devkits.wt/wtgate-verify＝detached @2d0116a9 现读·其 share/ 两枚 blob 链上现读＝改后版 d7c261bf／7fd83074 全等·该工作区 status 净）：
  - 全套闸形态＝bash share/run-gates.sh --root 该根 --no-write＝**GATE PASS exit 0（发现 6691 条）**＝两红归零坐实（gate-verifywt-qa.log·usage error 零命中＋FX-HOOK-1 零命中）。
  - csot --root 该根直跑＝exit 0·汇总行与主根态 diff 零行逐字全等（csot-verifywt-qa.log）。
  - hook-health --root 该根直跑＝exit 0·snapshot 行 hook-blob 在场对钉（hook-verifywt-qa.log）。
- 归因对照＝该根 git rev-parse --path-format=absolute --git-common-dir 现读＝主仓 .git 绝对径（兄弟仓解析锚）＋钩子居共享 common dir 机制生效实证。

判据③钩子零字节＝**绿**：.git/hooks/pre-commit 盘上 git hash-object 现跑＝8b7857701594264421832edd30dae7e401f85719 对钉全等；share/install-hooks.sh 对 HEAD blob f71474ac4a7c7e6f8e754c8f55b123c64d541507 对开工基线全等。

判据④EXPECTED_HOOK_BLOB 零动＝**绿**：share/check-hook-health.py L47 现读＝EXPECTED_HOOK_BLOB 常量原值 8b785770…全等；改动笔 811bd223 对该件 diff 全部加减行枚举现跑＝hunk 仅 @@74,6 +74,23（git_hooks_dir 插段）与 @@112,7 +129,7（拼径行置换）两枚，EXPECTED_HOOK_BLOB 字样在 diff 体零出现（连上下文不在＝改动不邻常量·强于判据要求）；numstat 该件 18 1 对预期全等。

判据⑤自咬＋清单存续＝**绿**：
- 两枚自靶＝check-pointers --target share/check-hook-health.py exit 0；--target share/check-source-of-truth.py exit 1 恰两枚 BLOCK（L113 存量悬空 experts 与 skills 两例·现读 L113 注释行在场）。相对口径对咬＝对 811bd223 前原件副本同靶 exit 1 恰同两枚，BLOCK 集（去路径前缀）diff 空集＝无新增即绿（ptr-csot-after-qa.log／ptr-csot-base-qa.log·已裁相对口径·禁凑 exit 0 自遵）。
- run-gates.sh blob 11a6f4d4 对开工基线全等＋SCRIPTS 清单 L141 两行现跑存续＝ROOT/share/check-source-of-truth 前缀项与裸名 check-hook-health 项均在。
- 自咬两器＝check-source-of-truth --selftest-seatdecl 全绿 exit 0；check-ticket-pins --selftest 用例 5／反常 0 exit 0（seatdecl-selftest-qa.log／pins-selftest-qa.log）。
- usage error 面＝hook-health 对不存在 root 现跑改后／基线原件两态各 exit 2 usage error 行为零变；csot 对 --pkg ../不存在径现跑 exit 2 usage error（闭集存续）。csot 对不存在 root 的 fakeroot 抽项＝改后 exit 0 与工程师照登一致（旧拼径 ../ 段折叠在盘机理·与 QA 审票黄-1 同机理·不作行为变动判）。

判据⑥豁免留痕核验＝**绿（带黄注 Y2）**：.collab/evidence/gates/ 现读 at21-22-08 组七枚＋at21-22-27 组六枚均 bypass＝true／reason＝1 非静默；其中 27 组 commit 字段＝b9982a04（＝改动笔父·21:22:27 与改动笔提交时刻吻合＝改动笔投递的直接留痕组），08 组 commit 字段＝9be69eb7（他案链顶·见 Y2）；拦截枚两处均＝agent-experts/baigong-software-team/.workbuddy/memory/2026-11-18.md:34 OA-T1（日期字面·扫描域划界缺陷候补池在册）。本席未碰该记忆文件（他案写面零字节红线自遵·仅闸输出行引用）。

判据⑦禁动面抽查＝**绿**：811bd223 name-only 恰两枚（csot／hook-health）；2d0116a9 name-only 恰一枚（回流件）；name-status 均 M 单父链正常；8d6b6740..HEAD 链面 name-only 共八枚＝票面／起草回执／两席审票判词／放行登记／回流件／share 两枚＝全落本票链各段申明面；链面 diff 对 agent-experts／agent-skills／softwares 三包＝空集（pins 工具零触）；禁动对钉八枚对 8d6b6740／b9982a04／HEAD 三态 git ls-tree 现算逐枚全等（11a6f4d4／f71474ac／33781b31／04f2889f／2c44d339／f6171c7d／c7b2141d／3cc80e61）。

钉值收口复跑（§三-2）＝**绿**：check-ticket-pins --ticket 本票面 --base b9982a04（工程师开工 ANCHOR）＝钉行 9｜违例 0｜exit 0；票面 grep 钉数 9 对咬；收口面 grep -cF 逐枚＝旧段三枚各 0＋新段六枚各 1 全符。

---

## 二、对抗臂（四枚·全部当轮现跑）

臂一·改动与票面 §二 围栏逐字对拍＝**绿**：票面 S1-A／S1-B／S1-C／S2-D／S2-E 五个围栏正文逐行／逐段程序化对拍在盘改后两文件＝全部在场为真（含前导空格逐字）；＝工程师逐字来源链路闭合。

臂二·禁动面 blob 两态 SAME＋零 amend 复跑＝**绿**：八枚禁动钉面三态 ls-tree 全等（§一判据⑦）；改动笔与回流笔 name-status 均 M 形态＋单父＋reflog commit 字样（零 amend／零 rebase 痕迹）；链线性 rev-list --parents 逐笔单父相衔。

臂三·fail-closed 活性＋主根零感知活性＝**绿（带黄注 Y3）**：
- 删整 pins 块副本（.scratch/SWB-WTGATE-qa/ticket-nopinblock.md）→ check-ticket-pins＝infra error 票面无机器可读钉块 exit 4＝fail-closed 活性成立。
- 删单枚钉（git_hooks_dir 定义钉）副本→钉行 8／违例 0／exit 0＝**工具不自动登记违例**（见 Y3）；机械咬合存在于判据层 grep 钉数 9 对咬（本席现跑 9 全等）＝收口不受影响，票 §五 对抗一预期「删单枚钉必违例」与工具实态不符照登。
- 主根零感知活性＝scratch 副本（liveness/ 并置基线 json）对改后 csot 汇总行字面改一字符→输出汇总行随之变化 diff 命中＝判臂读数活性成立、汇总行非硬编码假绿。

臂四·回退路径活性＝**绿**：改动笔 diff 导出 change.patch，scratch 假树（revertsim/）对改后两枚盘态 patch -R 反向应用 exit 0，复原后两枚 git hash-object 现算＝4fe99f6cd869b90df383463a4ad1d650075f0004／b778dc757f67351f21f104203f9253a2280e7925＝对开工起点 blob 全等＝revert 即复原坐实。（自纠注：本臂首跑因 hash-object 误带 git -C 主仓参数致读数错位，当场定位复跑更正，最终读数以复原文件本体现算为准。）

---

## 三、黄项如实

- 黄-1：主根全套闸 GATE PASS 发现 33389 当轮不可复现＝他案记忆面 OA-T1 持续在场（与工程师回流 §四 闸拒主因同一枚·本席两探针外工程师已证持续）；两枚被改脚本分项输出对基线零差＝判据①核心（改动面零感知）仍绿，环境基线漂移归因照登不入本票射程。
- 黄-2：at21-22-08 证据组 commit 字段＝9be69eb7（他案 ITER 线链顶 commit·非本链任何笔）＝钩子硬编码 --root 主根＋git 子进程 env 交叉案型（票 §四-1 候补池随注所指第三面）续证；改动笔直接留痕组应为 at21-22-27（commit 字段 b9982a04 吻合提交时刻）；两组均 bypass 非静默＝留痕核验本身通过，字段归因注照登供候补池票消费。
- 黄-3：pins 工具删单钉不违例（对抗臂三实跑＝钉行 8／违例 0／exit 0）＝票 §五 对抗一预期与工具实态偏差；机械对咬现居判据层（grep 钉数申报值）＝建议工具面另票射程（候补池候排·本票不收口改动）。
- 黄-4：旧 fuxi worktree 全套闸形态仍一枚红（ROOT/share 前缀取径＝该根旧检出副本）＝分发时序照登（派工已裁不作红判）；run-gates 取径两制统一口径候补池随注已在其回流件在册，本席复核坐实不加码。
- 黄-5：起草回执行数两口径（wc -l 47／含无换行末行 48）＝体例登记非失实。

## 四、回执忠实性（工程师回流件 §三 五判据读数对照本席现跑）

- ①主根零感知：工程师「GATE PASS 33389 对开工基线 diff 零行」＝其当窗读数；本席当轮 GATE PASS 不可复现（他案面介入·黄-1），csot 汇总行／hook snapshot 行两枚分项读数双方与基线三方全等＝核心值忠实。
- ②两红归零：工程师「钩子红归零＋csot 全套闸形态仍红（旧副本取径）＋csot 直跑 exit 0 汇总行逐字全等＋hook 两态直跑 exit 0」＝本席全部复现一致；兑现窗（验证工作区全套闸归零）＝本席现跑 GATE PASS exit 0 达成其移交项＝忠实且闭环。
- ③钩子零字节：8b785770／f71474ac 双方现跑全等＝忠实。
- ④EXPECTED_HOOK_BLOB：L47 原值＋diff 连上下文零出现＝双方现跑一致＝忠实（工程师「强于判据要求」措辞经本席独立核属实）。
- ⑤自咬＋清单：seatdecl 全绿 exit 0／pins 用例 5 反常 0／run-gates blob 与两清单行／hook fakeroot exit 2／csot fakeroot exit 0 机理注／靶检相对口径 BLOCK 集空集＝本席逐项复跑一致＝忠实。另核 §二 staged blob d7c261bf／7fd83074＝811bd223 落链 blob 全等＝「就位面重投零重施工」申报经链面坐实。

## 五、总判

**可收口（验收通过）**。五判据全绿（①带黄注 Y1 环境归因／其余直绿）；改动面原子性、钉值收口、禁动闭集、豁免留痕非静默、回退路径、兑现窗（worktree 全套闸两红归零 GATE PASS exit 0）全部当轮现跑坐实；工程师回执忠实性逐项对照零失配。黄项五枚均不入本票收口射程（环境面／候补池面／工具面另票射程／口径面），不拦收口。

（判词完——验收段判词一枚·投递归主理人；本席全程只读 git＝零 add 零 commit 零 amend 零 stash；取证族居仓根 .scratch/SWB-WTGATE-qa/ 用毕呈报不拆供收口参照；他案面／两 worktree 检出／钩子／config／禁动面全程零碰。）
