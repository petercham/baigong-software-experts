# SWB-WTGATE 起草回执 v1（闸工具 worktree 感知票·起草段回执笔·架构席 arch-swb-wtgate 落笔）

> 性质＝起草席回执（票 §五 链面之二＝起草段两笔封顶之笔二；落仓根 .collab/receipts 桶＝票 §一-2 声明面兑现）。｜落笔＝架构席 arch-swb-wtgate｜日期＝2026-11-18。
> 被回件＝.scratch/tickets/2026-11-18-SWB-WTGATE-闸工具worktree感知两脚本判臂git原生定位置换票-v1.md（票面起草笔＝e5f5a3a6＝本链第一笔＝起笔当轮链顶；票面 blob fc5f51730ba29522ad44f97cdb072a0e1aea8a46 链面 ls-tree 现读＝落笔后值）。

## 〇、开工当轮实测与落位更正登记

- 开工当轮 HEAD 实测＝8d6b67401ebfbc4a8b34326514b350c93db5ad65＝链顶现读＝派工预期值全等·带差零开工；分支 main 现读；git status --porcelain 去 ?? 读数＝两枚＝仓根 .collab/board/2026-11-17-五份复盘合流与下一轮迭代计划-v2.md（M·他案在飞）＋仓根 agent-skills/fuxi-skill/.collab/receipts/2026-11-18-FUXI-U50起草回执-v1.md（A·他窗旧名残件挂共享 index·blob 80c9948f72bf126f2ea7f55d6853b25314509a2d git ls-files -s 现读坐实＝脏面照登零碰零 reset·pathspec 提交天然隔离严禁带入）；锁面＝NO-INDEX-LOCK 现读；worktree list 现读＝主根挂 main＋D:/multi-agent-collab-devkits.wt 下两工作区（fuxi/main／baigong-software/main）＋两枚散置/prunable 照登零触。
- 落位更正登记（票 §头随注全录）：派工所指「票落仓根 .collab/tickets/」盘面实证不可行＝该桶不存在（ls 现读）＋share/check-collab-buckets.py 十七桶白名单 frozenset（L46-50 现读）不含 tickets＝新建即触 MC-BUCKET-1 BLOCK；本线先例 SWB-BKTCLS 票面实名＝.scratch/tickets/2026-11-16-SWB-BKTCLS-桶名闭集机检规格票-v1.md（git ls-files 坐实）＋.gitignore L61-64 票面桶豁免行在册＝本票照先例落 .scratch/tickets/、回执落仓根 .collab/receipts/；已向主理人呈报该项更正（落笔前 SendMessage 在册）。
- 票号续位＝仓根 .collab 与 agent-skills/fuxi-skill/.collab 两域 tickets/receipts 桶 grep WTGATE 字样零命中现跑坐实＝新建 v1 案型；SWB 先例号段（BKTCLS/A14H1/SCRATCHCFG 等）grep 枚举在册。

## 一、改动面与禁动面 blob 对开工基线现算表（票 §一 回填值出处·对 8d6b6740 git ls-tree 现算）

- 改动面两枚起点 blob＝share/check-source-of-truth.py 4fe99f6cd869b90df383463a4ad1d650075f0004（840 行）／share/check-hook-health.py b778dc757f67351f21f104203f9253a2280e7925（165 行）＋两枚对 HEAD 工作面净（git status --porcelain 带两 pathspec 空集现跑）＝未施工坐实。
- 禁动对钉八枚对 8d6b6740 现算回填＝run-gates.sh 11a6f4d4／install-hooks.sh f71474ac／check-pointers.py 33781b31／check-staged-declaration.py 04f2889f／baseline-sot-dup.json 2c44d339／baseline-seat-decl.json f6171c7d／sot-external-provenance.txt c7b2141d／agent-skills/fuxi-skill/gates/check-ticket-pins.py 3cc80e61。
- 钩子面盘上对钉＝git hash-object .git/hooks/pre-commit 现跑＝8b7857701594264421832edd30dae7e401f85719 与 check-hook-health.py L47 EXPECTED_HOOK_BLOB 常量 grep 现读逐字符全等＝FX-U50 改撤归原后存续态坐实＝本票禁动钩子的钉值基面。

## 二、两态基线全套现跑读数（起草当轮·不复用他席读数）

1. 主仓根：bash share/run-gates.sh 带 --root 主仓根与 --no-write＝**GATE PASS exit 0（发现 33389 条，均按路由表走②不拦提交）**；分项关键行＝check-source-of-truth「模式 dual｜文件 129（agents 7＋skills 122）｜BLOCK 0（新命中 0）｜基线豁免 54（WATCH·键＝文本＋文件集合）｜指针 WATCH 413｜exit 0」／check-hook-health「HOOKHEALTH-SNAPSHOT hooksPath-readings=0｜hook-blob=8b7857701594264421832edd30dae7e401f85719｜hook-mode=0o0」零发现／check-adr「桶1=1 桶2=21 桶3=1｜发现 0｜exit 0」／check-ticket-reconcile「票 160（对账 43／SKIP 缺声明 117）｜发现 184（全 WATCH）｜exit 1 advisory」／check-entity 五谓词各 count=0／check-collab-buckets「一级目录判 14 枚｜违例 0｜名录对拍 一致」＝日志落 .scratch/SWB-WTGATE-draft/gate-mainroot-baseline.log。
2. worktree 根（D:/multi-agent-collab-devkits.wt/agent-skills/fuxi-skill）：同命令 --root 指该根＝**GATE BLOCK exit 1 恰两枚**＝①check-source-of-truth exit 2「usage error: 包目录不存在：../multi-agent-collab-experts/workbuddy/baigong-video-team」②check-hook-health BLOCK FX-HOOK-1「期望钩子不在盘：.git/hooks/pre-commit」（snapshot hook-file=absent）＝两红现场复现＝日志落 .scratch/SWB-WTGATE-draft/gate-worktree-root-baseline.log；该根 .git 文件内容现读＝gitdir 指针行（gitfile 非目录实证）；兄弟仓两径主仓侧在盘实测存在（ls 现读）。
3. 自咬两器：python share/check-source-of-truth.py 带 --root 与 --selftest-seatdecl＝五用例全绿 exit 0（日志 .scratch/SWB-WTGATE-draft/seatdecl-selftest-baseline.log）；python agent-skills/fuxi-skill/gates/check-ticket-pins.py --selftest＝用例 5／反常 0 exit 0（日志 .scratch/SWB-WTGATE-draft/pins-selftest.log）。

## 三、scratch 装配预演全套读数（票 §〇-6 出处·.scratch/SWB-WTGATE-draft/patched/ 不 commit）

- 程序化置换＝对两枚基线副本按票 §二 规格 old→new 替换：旧段计数断言 1/1/1 全过→置换落位；numstat＝git diff --no-index 现算＝csot「22 2」／hook「18 1」＝§三-1 判据基数。
- 改后 csot 对主仓根现跑 exit 0＝汇总行与开工基线 §二-1 该分项**逐字节全等**（diff 输出文件 csot-mainroot-diff2.txt 零行；注＝预演副本与基线 json 同目录并置一次即达＝BASELINE_SNAPSHOT 自脚本位置寻径＝既有行为非判臂改动·真位施工天然无此步·如实照登）。
- 改后 csot 对 worktree 根现跑 exit **0**（汇总行同款＝exit 2 归零坐实）。
- 改后 hook-health 两态现跑＝主仓根 exit 0 与 worktree 根 exit 0，snapshot 行均「hooksPath-readings=0｜hook-blob=8b7857701594264421832edd30dae7e401f85719｜hook-mode=0o0」＝absent/BLOCK 归零＋主根读数零扰动坐实。
- git 旗两态可行性现读＝git 2.55.0.windows.3；rev-parse 带 --path-format=absolute 分别配 --git-path hooks 与 --git-common-dir，主根与 worktree 根两态输出同值（前者＝主仓 .git/hooks＝共享 common dir 钩子目录；后者父目录＝主工作区根）＝两判臂修正的机械根据。

## 四、钉预跑与靶检读数

- pins 预跑＝python agent-skills/fuxi-skill/gates/check-ticket-pins.py 带 --ticket 本票面仓根相对径与 --base 8d6b67401ebfbc4a8b34326514b350c93db5ad65＝**钉行 9｜违例 0｜exit 0**（起草当轮现跑）；票面 grep -c '^PIN|' ≡ 9 对咬。
- 九钉 B/D 值对基线逐枚现算＝旧值三钉 1/1/1（行号 767／777／115 现跑）→V1*=0；新值六钉 0→1＝与票 §二 钉注全等＝D-92 工程师开工复算基面对等。
- 靶检＝python share/check-pointers.py --target 本票面仓根相对径 exit 0 零 BLOCK（落笔前一次过在册）；本回执件落笔前同法自靶 exit 0 先行登记（§六）。
- 票面反引号 token 枚举＝grep 反引号段现跑输出空集（本票面零反引号路径 token＝全部裸文写＝OA-D6 案型零暴露坐实）。

## 五、零施工红线申报＋纪律申报＋链账

- 零施工红线＝本席起草全程 share/ 两枚真源零碰＝blob 两值对开工基线全等坐实（§一）；本席产出＝.scratch/tickets 票面一笔＋本 receipts 回执一笔＝票 §一 声明面兑现；patched 预演副本居仓根 .scratch gitignored 临时域不入链。
- 链账＝起草段两笔封顶＝票面笔 e5f5a3a6（本席·起笔当轮链顶 8d6b6740）＋本回执笔（本笔）＝恰两笔零超额；施工段两笔封顶（两枚真源改动一笔＋工程师回执一笔）随放行另计；审票判词／放行／QA 验收／收口登记随票 §五 收口链另段不预占。
- 票面笔自查＝该笔 git show --name-only 恰一枚＝票面本件；票面 blob＝fc5f51730ba29522ad44f97cdb072a0e1aea8a46（链面 ls-tree 现读）；numstat 204 插入（盘面 wc -l 203＋末行无换行符形制如实照登）；笔内钩子全套闸读数随重定向落盘件承载＝GATE PASS 发现 33389 与开工基线全等＝起草笔对在飞闸零扰动坐实。
- 落链纪律申报＝本笔面恰本回执一件；pathspec 限定 add 与 commit 紧邻无窗口；FX_COMMIT_DECLARE 环境变量形态＝本笔面仓根相对纯路径清单；禁 add -A／禁 amend／禁 --no-verify／禁 ALLOW_GATE_DOWN；message 零 at 符号字符（用字样）零反引号·短式 token 裸文写·禁前向指针；落笔前本件靶检 exit 0 先行在册；commit 输出重定向落盘仓根 .scratch/SWB-WTGATE-draft/receipt-commit.log；Bash timeout 十分钟档；撞 index.lock 有界等待一轮即呈报零删锁（起草全程未撞＝零等待轮数照登 0）。
- 他案面自证＝本笔落链前后 git diff --cached --name-only 两读：前读＝他案旧名残件一枚（80c9948f·零碰）；票面笔后读＝同前（残件留面未带入·笔面恰自件一枚现证）；?? 群零带入；worktree 两工作区零触；钩子零触；git config 零写。
- 完工自查＝票 §三 起草侧各判据起草轮复现全绿（钉数 9 对咬／预跑违例 0／靶检 exit 0／两态基线全套在册／自咬两器全绿）；§四 登记项四条照录知会零碰（钩子动态根另票／install-hooks.sh 制度化另票／证据域补盘候裁／EXPECTED_HOOK_BLOB 语义候裁）。

（回执完——起草段回执笔＝两笔封顶之笔二；施工段随放行归工程师席；本席止于此。）