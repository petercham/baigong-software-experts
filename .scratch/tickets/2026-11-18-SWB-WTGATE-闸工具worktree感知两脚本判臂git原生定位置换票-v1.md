# SWB-WTGATE · 闸工具 worktree 感知票＝share 两枚门禁脚本判臂改 git 原生定位（check-source-of-truth 兄弟仓相对径解析锚随主工作区根＋check-hook-health 钩子目录定位随共享 common dir＝两枚行内置换与插段·零新口径零新闸零路由改动）｜v1

> 票号＝SWB-WTGATE（编号续位现盘自查＝仓根 .collab 与 agent-skills 两域 tickets/receipts 桶 grep WTGATE 字样零命中坐实＝新建 v1 案型；本线先例 SWB-BKTCLS／SWB-A14H1 同族裸号段在册）｜起草＝架构席（arch-swb-wtgate）｜日期＝2026-11-18｜被派＝**工程师席**（两枚脚本改动一笔＋工程师回执一笔＝施工段封顶两笔）；本席只出票面零碰 share/ 真源＝纯规格零施工红线写死（改动归放行后工程师席施工）。
> 落位实证更正随注（派工所指与盘面冲突·照先例落位）：「票落仓根 .collab/tickets/」经实证不可行＝仓根 .collab 现无 tickets 桶（ls 现读）＋share/check-collab-buckets.py 内嵌十七桶白名单 frozenset（该件 L46-50 现读）不含 tickets＝新建该桶必触 MC-BUCKET-1 BLOCK（该闸在 run-gates 清单在场）；本线先例票面实名均落仓根 .scratch/tickets/（git ls-files 面 SWB-BKTCLS 票实名居此坐实＋.gitignore L61-64 票面桶豁免行在册）＝本票照先例落 .scratch/tickets/、起草回执与工程师回执落仓根 .collab/receipts/（先例体例同）。
> 排程依据（已放行在册·票面禁候裁）：agent-skills/fuxi-skill/.collab/receipts/2026-11-18-FUXI-FX-U50起草回执-v1.md §四-呈裁请求项②＋§五-拦停尝试读数（worktree 根闸两枚红＝兄弟包缺位案型＋钩子 common-dir 案型·决策者裁＝另立维护票修工具面）＋该回执 §五 候补池随注一行在册＋主理人目标终态＝各活跃业务线各住各的 worktree、主根留守 share 维护与合并（本日在册议题）。本票即该维护票·对象＝仓根工具面非 fuxi 包。
> 开工锚照登（起草席 2026-11-18 当轮实测）：开工 HEAD＝8d6b67401ebfbc4a8b34326514b350c93db5ad65（链顶现读＝派工预期值全等·分支 main 现读）；git status --porcelain 去 ?? 读数＝两枚＝仓根 .collab/board/2026-11-17-五份复盘合流与下一轮迭代计划-v2.md（M·他案在飞）＋仓根 agent-skills/fuxi-skill/.collab/receipts/2026-11-18-FUXI-U50起草回执-v1.md（A·他窗旧名残件挂共享 index·blob 80c9948f72bf126f2ea7f55d6853b25314509a2d 现读 git ls-files -s 坐实＝脏面照登零碰零 reset 严禁带入）；untracked 面照登零带入（仓根 .scratch 取证群／.py 散件群等）；worktree 面现读＝D:/multi-agent-collab-devkits.wt/agent-skills/fuxi-skill 挂 fuxi/main＋D:/multi-agent-collab-devkits.wt/agent-experts/baigong-software-team 挂 baigong-software/main（git worktree list 现读·共链共享对象库各独立 index）＋两枚 prunable/散置 worktree 照登零触。工程师席开工 ANCHOR＝开工当轮 HEAD 实测（应为含本票起草笔或其后续合法放行笔的链顶）·照登；ANCHOR 不符＝停手上报，禁带差开工。
> 开工前置对账（读数当轮实读相符方可动笔·**改动面起点 blob 必对开工基线当轮现算，禁沿用本票面抄录值——U34 教训面自践**）：①改动面两枚起点 blob＝share/check-source-of-truth.py 与 share/check-hook-health.py 对开工基线 git ls-tree 现算（起草回填值对 8d6b6740 现算＝4fe99f6cd869b90df383463a4ad1d650075f0004（840 行）／b778dc757f67351f21f104203f9253a2280e7925（165 行）＝参考位·见 §一 表）＋两枚对 HEAD 工作面净（git status --porcelain 带两 pathspec 空集现跑）；②禁动对钉八枚 blob 对开工基线现算回填 §一；③钩子面钉值＝.git/hooks/pre-commit 盘上件 git hash-object 现跑＝8b7857701594264421832edd30dae7e401f85719 与 check-hook-health.py EXPECTED_HOOK_BLOB 常量（该件 L47 现读）**全等坐实**（FX-U50 §五 改撤归原后存续态）；④两态基线（起草当轮实跑在册 §〇-4/§〇-5）＝主仓根 run-gates 全套＝GATE PASS exit 0；worktree 根同套＝GATE BLOCK 恰两枚（check-source-of-truth exit 2＋FX-HOOK-1）＝本案两红现场复现；⑤check-source-of-truth 自咬＝--selftest-seatdecl 五用例全绿 exit 0（起草当轮实跑）；⑥pins 工具自咬＝agent-skills/fuxi-skill/gates/check-ticket-pins.py --selftest 用例 5／反常 0 exit 0（起草当轮实跑；该器＝本票 pins 实位＝短式 share/ 下无同名件＝FX-U50 回执案型在册）。开工读数不符＝停手上报，禁带差开工。
> 钉形态注（本票 pins＝**行内置换两态钉＋插段入位钉**共九枚·写死 §二）：本批改动＝三枚行内置换（两调用点＋一钩子拼径行）＋三处插段（一 import 行＋两个辅助函数定义段）——S 围栏只放**改后新段全文**（工程师逐字来源＝围栏正文；旧段全文落 §二 置换表＝围栏外正文＝A=0⇒V1*=B−D 归零自洽＝case4_old_zero_ok 先例形制）；旧值三钉 V0=B=1/1/1·旧行号＝767／777（csot 基线行号现跑）／115（hook 基线行号现跑）（对基线盘 D 各 1）⇒V1* 各 **0**；新值六钉 B=0／A=1／D=0⇒V1* 各 **1**。钉语对开工基线现跑 B 值＝§〇-3 在册；**钉语防自染自查**＝九枚钉语完整串只落钉块与归属 S 围栏；§〇／置换表正文提及旧值以全角引号承载（与钉语正文无公式效力·pins 只消费围栏正文）；围栏内代码行零反引号＝零指针 token 入扫面自查在册。工程师开工对九钉对开工基线逐枚复算 V0 相符方可动笔＝D-92；现算与表钉不符＝H-0 停笔呈裁禁凑绿。
> 指针纪律注（A 条款自我适用·写死）：本票面一切反引号路径＝仓根起始完整路径且落笔时点目标已在盘实点（share／gates／receipts 逐路径实查在册；短式裸名反引号 token 一律避写＝OA-D6 后缀多义案型自践）；尚未生成件（本席回执／工程师改动后态／工程师回执）一律裸文写（无反引号）；盘符路径与 worktree 绝对径一律裸文写不进反引号。落笔后对本票面跑 python share/check-pointers.py --target 仓根相对路径 必 exit 0 零 BLOCK＝写死判据（§三-6）。登记类文书路径逐件全写禁 brace 简写（R-13 自遵）。
> D-95 分段落笔硬条款（链面封顶自算·派工要件）：起草段＝**票面一笔封顶＋回执一笔＝两笔封顶**；施工段（工程师·随放行）＝**改动笔一笔（两枚脚本＝share/check-source-of-truth.py＋share/check-hook-health.py 恰两面·声明闭集内单笔）＋工程师回执一笔＝两笔封顶**；本票链封顶＝起草二＋施工二＝**四笔封顶自算坐实**（审票判词／放行／QA 验收／收口登记随 §五 收口链另段不预占）；**每笔 pathspec 限定 add 与 commit 紧邻无窗口·FX_COMMIT_DECLARE 声明本笔面＝纯路径清单形态（承 FX-U32 闸形）**；禁 git add -A、禁 amend、禁裸 git commit；message 零 at 符号字符（用「at 符号」字样）零反引号；commit 带 ≥7 分钟 timeout 且输出重定向落盘仓根 .scratch/SWB-WTGATE-draft/ 或 .scratch/SWB-WTGATE-build/ 防强杀；查 config 一律旗在前只读语法；资源不足先 commit 已完成面再回报现状，禁裸退；零落账回报无效。
> 并发防护（D-58 案型随带）：pathspec add 与 commit 两端齐带紧邻无窗口（提交闸 fail-closed 无声明 BLOCK exit 1＝设计如此禁 BYPASS）；落笔前后 git diff --cached --name-only 两读并排入回执，差集恰本笔面（起草当轮共享 index 上他案旧名残件一枚＝照登·pathspec 提交天然隔离）；撞 index.lock 或 cannot lock ref＝有界等待一轮即呈报主理人（零删锁零二次重试）。他案在飞面点名＝仓根 board 计划 v2（M）＋agent-skills/fuxi-skill/.collab/receipts 旧名残件（A·staged·blob 80c9948f）＋?? 散件群＝全部零碰零带入；链上他案笔照登不归因。同仓另一会话（百工软件/experts 线）活跃在飞＝只用精确单 pathspec，add/commit 两端齐带。
> 取证面纪律（D-94＋R-10）：起草段取证／scratch 装配预演物全部落仓根 .scratch/SWB-WTGATE-draft/ 不 commit（patched 两枚预演副本＋两态基线日志＋自咬日志居此·用毕呈报不拆供 QA 复跑参照）；本票零取证新物入链；untracked 证据域不随 worktree 案型（FX-U50 案型乙）与本票无关·候补池随注引用。

---

## 〇、复核结论（架构席 2026-11-18 对 8d6b6740 实读实跑实查，票内定稿依据）

1. **链顶与票号与在册性（读数一）**：开工 HEAD＝8d6b67401ebfbc4a8b34326514b350c93db5ad65＝链顶现读＝FX-U50 收口登记笔；两域 tickets/receipts 桶 grep WTGATE 字样零命中＝票号续位坐实。
2. **两枚判臂实位现读（通读全文坐实）**：
   - **件一 share/check-source-of-truth.py（840 行）**：兄弟仓默认包根常量 L164 DEFAULT_PKG＝../multi-agent-collab-experts/workbuddy/baigong-video-team（兄弟仓并列于主工作区根同父目录的相对径·前提白纸 L162-163 在册）；两消费点＝main 函数内 L767 pkg_abs 拼接行＋L777 skills_abs 拼接行（均 os.path.abspath(os.path.join(root, 相对径)) 形态＝root 为仓根时 ../ 段解析正确；root 为 worktree 根时 ../ 段方向指错→目录不存在→L769/L779 usage error exit 2）。import 面现状＝无 subprocess（grep import subprocess 计数 0 现跑）。
   - **件二 share/check-hook-health.py（165 行）**：钩子面判臂 L115＝hook 路径拼接行＝os.path.join(root, ".git", "hooks", "pre-commit") 字面拼径——worktree 根的 .git 是 gitfile 指针文件非目录（worktree 盘现读 .git 文件内容＝gitdir 指针行）→L116 isfile 假→L122 snapshot 行 hook-file=absent→L131-133 期望钩子不在盘 BLOCK FX-HOOK-1。import 面现状＝subprocess 已在（L40）。
3. **钉语 B 值现跑（pins 自洽基面）**：旧段三枚对开工基线 grep -cF＝csot 旧 pkg_abs 行 **1**／csot 旧 skills_abs 行 **1**／hook 旧 hook 拼径行 **1**（行号 767／777／115 现跑）；新段六枚（import subprocess 行／resolve_sibling_root 定义行／两新调用行／git_hooks_dir 定义行／新 hook 拼径行）对基线各 **0**。
4. **主仓根基线现跑（起草当轮·收口全等判据基面）**：bash share/run-gates.sh 带 --root 主仓根与 --no-write＝**GATE PASS exit 0（发现 33389 条，均按路由表走②不拦提交）**；分项关键读数＝check-source-of-truth「模式 dual｜文件 129（agents 7＋skills 122）｜BLOCK 0（新命中 0）｜基线豁免 54（WATCH·键＝文本＋文件集合）｜指针 WATCH 413｜exit 0」＋check-hook-health「HOOKHEALTH-SNAPSHOT hooksPath-readings=0｜hook-blob=8b7857701594264421832edd30dae7e401f85719｜hook-mode=0o0」零发现＋check-adr「bundle 根＝主仓 baigong-software-team｜docs/adr 盘上件=1｜桶1=1 桶2=21 桶3=1｜发现 0｜exit 0」＋check-ticket-reconcile「票 160（对账 43／SKIP 缺声明 117）｜发现 184（全 WATCH）｜exit 1（advisory）」＋check-entity 五谓词各 count=0＋check-collab-buckets「一级目录判 14 枚｜违例 0｜名录对拍 一致」（日志落 .scratch/SWB-WTGATE-draft/gate-mainroot-baseline.log）。
5. **worktree 根基线现跑（两红复现）**：同命令 --root 指 worktree 根＝**GATE BLOCK exit 1 恰两枚**＝①check-source-of-truth exit 2「usage error: 包目录不存在：../multi-agent-collab-experts/workbuddy/baigong-video-team」②check-hook-health「BLOCK FX-HOOK-1 期望钩子不在盘：.git/hooks/pre-commit」（snapshot 行 hook-file=absent）；该根其余闸＝check-adr exit 0（桶2=20）／check-entity 五谓词各 0／check-collab-buckets 违例 0／check-pointers OA-D6 族 advisory 路由照登不入阻断（日志落 .scratch/SWB-WTGATE-draft/gate-worktree-root-baseline.log）；兄弟仓两径主仓侧在盘实测＝D:/multi-agent-collab-experts/workbuddy/baigong-video-team＋D:/multi-agent-collab-skills/skills（ls 现读存在）。
6. **scratch 装配预演（起草轮·仓根 .scratch/SWB-WTGATE-draft/patched/ 不 commit）**：两枚基线副本按 §二 规格程序化置换（旧段计数断言 1/1/1 全过）→**改后 csot 对主仓根现跑**＝「模式 dual｜文件 129｜BLOCK 0｜基线豁免 54｜指针 WATCH 413｜exit 0」与 §〇-4 基线行**逐字节全等**（diff 零行·注＝预演副本需与基线 json 同目录并置＝BASELINE_SNAPSHOT 自脚本位置寻径＝既有行为非判臂改动·施工在真位天然无此问题）；**改后 csot 对 worktree 根现跑**＝exit 0 同款读数（**exit 2 归零坐实**）；**改后 hook-health 两态现跑**＝主仓根与 worktree 根各 exit 0·snapshot 行均「hooksPath-readings=0｜hook-blob=8b7857701594264421832edd30dae7e401f85719｜hook-mode=0o0」（**absent/BLOCK 归零＋主根读数零扰动坐实**）；numstat 预演＝csot「22 2」／hook「18 1」（git diff --no-index 现算）＝§三-1 判据基数。
7. **git 旗可行性现读**：本机 git version 2.55.0.windows.3；rev-parse 带 --path-format=absolute 与 --git-path hooks 在主仓根与 worktree 根两态现跑均输出 D:/multi-agent-collab-devkits/.git/hooks（**同值＝共享 common dir 下钩子目录绝对路径**）；--git-common-dir 两态现跑均输出 D:/multi-agent-collab-devkits/.git（其父目录＝主工作区根＝兄弟仓解析锚）；主工作区根下该锚＝仓根＝新旧行为逐字节等价（预演 diff 零行实证 §〇-6）。旗不支持（git 旧形态）回退分支写死 §二。
8. **钩子与安装器禁动静证**：.git/hooks/pre-commit 内容现读＝两行调用各带 --root 硬编码主仓根字面（第三面案型＝钩子内 git 子进程 env 交叉致 check-adr 跨环境串染假阳 159 枚＝**本票禁动**·候补池随注）；share/install-hooks.sh 生成行 L100-101 同款仓根字面插值＝**本票禁动**（钩子再生成覆回硬编码形态＝候补池随注）；EXPECTED_HOOK_BLOB 常量零改动写死 §三-4（若该钉值语义需随 worktree 语义调整＝列入候裁禁自行改）。

---

## 一、声明闭集（git 面·起草段两笔封顶 2 面·施工段封顶两笔两面）

1. .scratch/tickets/2026-11-18-SWB-WTGATE-闸工具worktree感知两脚本判臂git原生定位置换票-v1.md（本票面·起草席一笔·add/commit 恰本面）
2. 仓根 .collab/receipts 桶内「2026-11-18-SWB-WTGATE-起草回执-架构席-v1」件（起草席回执·另笔·裸文写·A 条款）
3. share/check-source-of-truth.py（改·施工改动笔·§二 S1 规格逐字照录＝一处 import 插行＋一处函数插段＋两处行内置换·其余全部零字节）
4. share/check-hook-health.py（改·同笔·§二 S2 规格＝一处函数插段＋一处行内置换·其余全部零字节）
5. 仓根 .collab/receipts 桶内工程师回执件（施工段另笔·裸文写·A 条款·落链后补入本闭集随回执申报＝先例口径承 FX-U50 §一）

（＝链封顶总账：起草 2（票面一＋回执一）＋施工 2（两枚真源改动一笔＋工程师回执一笔）＝**四笔封顶自算坐实**。）

改动面起点 blob 表（两枚被改实体·对起草 ANCHOR 8d6b6740 git ls-tree 现算回填＝参考位；工程师开工对开工基线当轮现算对账，不符＝按放行票射程核因登记呈报＝H-0 停笔呈裁·禁凑绿禁回改·U34 教训面自践）：

    share/check-source-of-truth.py    4fe99f6cd869b90df383463a4ad1d650075f0004（840 行·被改实体＝import 插行一处＋norm 函数段后插段一处＋L767/L777 行内置换两处·其余全部零字节）
    share/check-hook-health.py        b778dc757f67351f21f104203f9253a2280e7925（165 行·被改实体＝find_root 函数段后插段一处＋L115 行内置换一处·其余全部零字节）

禁动对钉表（八枚·对起草 ANCHOR 8d6b6740 git ls-tree 现算回填＝参考位；工程师开工对开工基线当轮现算对账）：

    share/run-gates.sh                        11a6f4d4ee1b384117ae405c68024198b025f037（禁动对钉＝清单行 L141 十一枚 SCRIPTS 存续零动＝验收硬判据⑤）
    share/install-hooks.sh                    f71474ac4a7c7e6f8e754c8f55b123c64d541507（禁动对钉＝钩子生成器零字节＝候补池随注所指另票射程）
    share/check-pointers.py                   33781b312e7029a02ec05626121bcf12c78d7276（禁动对钉＝靶检工具本体存续）
    share/check-staged-declaration.py         04f2889f21a3684511d9a74d2ca22e0998409ed1（禁动对钉＝暂存声明闸零扰动）
    share/baseline-sot-dup.json               2c44d339890811304d7f1cd3a355d88ee547e5e6（禁动对钉＝豁免基线 json 零字节）
    share/baseline-seat-decl.json             f6171c7db03cf79529c89795fd243e2a78a22b12（禁动对钉＝席位基线 json 零字节）
    share/sot-external-provenance.txt         c7b2141d5968389411e8a683fff7d9300db049a9（禁动对钉＝产地注记白名单零字节）
    agent-skills/fuxi-skill/gates/check-ticket-pins.py  3cc80e61b41cbf5db7eb0d949545607b7ccd401d（禁动对钉＝pins 实位工具零字节）

钩子面盘上对钉（非 git 面·hash-object 现算）：.git/hooks/pre-commit 盘上 blob＝8b7857701594264421832edd30dae7e401f85719 收口必全等＝验收硬判据③（钩子全域禁动）；该钉值与 check-hook-health.py EXPECTED_HOOK_BLOB 常量全等态存续＝收口复跑 snapshot 行对钉必现跑再现（§〇-2 起草基面）。

禁动面点名＋零碰清单（写死）：上表禁动对钉八枚＋钩子全域（.git/hooks 全体＋git config 零写）＋run-gates.sh 清单与循环体＋两枚豁免基线 json＋白名单 txt＋**agent-skills/fuxi-skill/ 全域零字节**（含其 .collab 两桶＋gates 全部＋contracts/specs/adapters/products/SKILL.md＋evidence 域文件面）＋agent-experts/ 全域零字节＋softwares/＋tools/＋仓根 README＋agent-skills/multi-collab/ 规范面零字节（路由表 60-gates.md 围栏零动＝本票不新增 spec_id 零路由改动）＋仓根 .collab/ 全域（含 board 他案 M 面与 receipts 桶他案旧名残件 A 面＝零碰零带入）＋仓根 .scratch/ 全部既有面零碰＋worktree 两工作区零触（本票全程不碰其 checkout）＋链上他案笔照登不归因＋宿主装载面／仓外兄弟仓（D:/multi-agent-collab-experts／D:/multi-agent-collab-skills）＝只读零写入零补盘。

---

## 二、施工规格（fenced 新段＝唯一文字来源逐字成文·工程师照录·本席零施工·排程已放行零开放措辞）

**总则（写死·两面共用）**：工程师施工＝程序化全文替换（old→new 逐字·先断言 old 计数＝申报值再替换·替换后断言 old 计数归零＋new 计数＝申报值），禁手改整行、禁顺手扩面；插段以锚行在场断言定位（旧段不落围栏故其真身以开工基线盘面现面为准＝替换前计数断言即对钉）；改后行数＝csot 840→**860**／hook 165→**182**（§三-1 wc 判据）；换行与 EOF 形制随基线存续禁改写（LF 存续）。**旧段/新段承载分工（pins 公式自洽写死）**：新段全文逐字只落各 S 围栏（＝工程师逐字来源＋pins A 值载体）；旧段全文逐字只落本节围栏外置换表与钉块钉语（不落任何 S 围栏＝A=0⇒V1*=B−D 归零自洽＝case4_old_zero_ok 先例形制·FX-U50 回执形制同源）。

**S1 · share/check-source-of-truth.py（改·四处＝一处 import 插行＋一处函数插段＋两处行内置换）**

置换表（围栏外·旧段逐字＝对基线盘替换前计数断言用）：置换一（L767 整行）旧段＝「    pkg_abs = os.path.abspath(os.path.join(root, args.pkg))」→新段见围栏 A 第一行；置换二（L777 整行）旧段＝「        skills_abs = os.path.abspath(os.path.join(root, args.skills_root))」→新段见围栏 A 第二行（两行前导空格按围栏逐字保留）。

插段一（import 面）：对基线断言「import re」行紧邻「import sys」行恰一处在场→两者之间插入围栏 B 整行（字母序位 re→subprocess→sys 照围栏）。

插段二（函数插段）：在 norm 函数段与 collect_md 函数定义行之间插入围栏 C 全段（函数间两空行形制照基线存续；围栏 C＝插入全文逐字·不含围栏行本身）。

```text
S1-A 两处行内置换后新行全文（含前导空格逐字）：
    pkg_abs = resolve_sibling_root(root, args.pkg)
        skills_abs = resolve_sibling_root(root, args.skills_root)
```

```text
S1-B import 插入行全文：
import subprocess
```

```text
S1-C 函数插入段全文（置于 norm 函数段之后、collect_md 定义行之前）：
def resolve_sibling_root(root: str, rel: str) -> str:
    """兄弟仓相对径（../ 起头）的解析锚＝主工作区根（worktree 感知）。

    worktree 工作区根下 ../ 段相对径方向指错（兄弟仓并列于主工作区根的同父目录）；
    解析锚改取 git rev-parse --path-format=absolute --git-common-dir 输出的父目录。
    主工作区根下该锚＝仓根本身＝新旧行为逐字节等价。git 不可用／旗不支持／非
    ../ 起头径＝照旧相对 root 拼接（fail-soft 回退，不更松不更严）。
    """
    if rel.startswith('..'):
        proc = subprocess.run(
            ['git', '-C', root, 'rev-parse', '--path-format=absolute',
             '--git-common-dir'],
            capture_output=True, text=True)
        if proc.returncode == 0 and proc.stdout.strip():
            anchor = os.path.dirname(os.path.normpath(proc.stdout.strip()))
            return os.path.abspath(os.path.join(anchor, rel))
    return os.path.abspath(os.path.join(root, rel))
```

零碰随注（写死）：csot 其余全部行零字节＝spec-provenance 头注块零动／DEFAULT_PKG 与 DEFAULT_SKILLS_ROOT 常量零动（L164-165）／A1/A2/B/C 判据臂零动／基线豁免链零动／--selftest-seatdecl 面零动／退出码闭集零动；本改动只换「root 拼径」为「解析锚拼径」＝判据语义零变（主根逐字节等价＝§〇-6 diff 零行实证）。

**S2 · share/check-hook-health.py（改·两处＝一处函数插段＋一处行内置换）**

置换表（围栏外·旧段逐字）：置换（L115 整行）旧段＝「    hook = os.path.join(root, ".git", "hooks", "pre-commit")」→新段见围栏 E（前导四空格按围栏逐字保留）。

插段：在 find_root 函数段与 read_hookspath_readings 函数定义行之间插入围栏 D 全段（函数间两空行形制照基线存续；围栏 D＝插入全文逐字·不含围栏行本身）。

```text
S2-D 函数插入段全文（置于 find_root 函数段之后、read_hookspath_readings 定义行之前）：
def git_hooks_dir(root):
    """钩子目录定位＝git 原生旗（worktree 感知）。

    worktree 工作区的 .git 是 gitfile 指针文件非目录，钩子物理居共享 common
    dir 的 hooks/；rev-parse --path-format=absolute --git-path hooks 在主工作区
    根与 worktree 根两态同读数＝共享 common dir 下钩子目录绝对路径。旗不支持
    （git 旧形态）＝回退旧拼径 root/.git/hooks（主仓根行为零变）。
    """
    proc = subprocess.run(
        ["git", "-C", root, "rev-parse", "--path-format=absolute",
         "--git-path", "hooks"],
        capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0 or not proc.stdout.strip():
        return os.path.join(root, ".git", "hooks")
    return os.path.normpath(proc.stdout.strip())
```

```text
S2-E 行内置换后新行全文（含前导空格逐字）：
    hook = os.path.join(git_hooks_dir(root), "pre-commit")
```

零碰随注（写死）：hook-health 其余全部行零字节＝**EXPECTED_HOOK_BLOB 常量行（L47）零字节**（验收硬判据④·若其语义需随 worktree 语义调整＝候裁禁自行改）／MARKER 与 EXPECTED_CALL_TARGETS 零动／查一 hooksPath 臂零动／查二可执行位 POSIX 判臂零动／查三 MARKER＋调用行后缀含判＋blob 对钉臂零动／快照行形制零动（唯 hook-file=absent→hook-blob 在场为判臂修正之自然读数变化）／退出码闭集零动。

**本票钉值块（机器可读·V0*=B／V1*=B+A−D·起草席对基线 8d6b6740 现算回填·实跑预演在册 §六）**：

```pins
PIN|share/check-source-of-truth.py|    pkg_abs = os.path.abspath(os.path.join(root, args.pkg))|1|0|767
PIN|share/check-source-of-truth.py|        skills_abs = os.path.abspath(os.path.join(root, args.skills_root))|1|0|777
PIN|share/check-source-of-truth.py|import subprocess|0|1|-
PIN|share/check-source-of-truth.py|def resolve_sibling_root(root: str, rel: str) -> str:|0|1|-
PIN|share/check-source-of-truth.py|    pkg_abs = resolve_sibling_root(root, args.pkg)|0|1|-
PIN|share/check-source-of-truth.py|        skills_abs = resolve_sibling_root(root, args.skills_root)|0|1|-
PIN|share/check-hook-health.py|def git_hooks_dir(root):|0|1|-
PIN|share/check-hook-health.py|    hook = os.path.join(root, ".git", "hooks", "pre-commit")|1|0|115
PIN|share/check-hook-health.py|    hook = os.path.join(git_hooks_dir(root), "pre-commit")|0|1|-
```

（九钉现算依据（基线＝8d6b6740 现算·起草当轮 grep -cF 逐枚现跑在册 §〇-3）：旧值三钉＝B(基线命中)=1/1/1·A=0（旧段不落任何 S 围栏＝置换表在围栏外正文无公式效力）·D(旧行位命中)=1/1/1⇒V1*=0 归零自洽（case4_old_zero_ok 先例形制）；新值六钉＝B=0·A=1（各落归属 S 围栏恰一行）·D=0⇒V1*=1（case5_new_one_ok 形制）。**钉语防自染自查**＝九枚钉语完整串只落钉块与归属 S 围栏；§〇-2／置换表外正文引用旧值以全角引号承载或拆段裸写（与钉语正文无公式关系·pins 只消费围栏正文）。**围栏外无其他 pins 干扰围栏自查**＝本票仅 S1-A/S1-B/S1-C/S2-D/S2-E 五个 text 围栏＋一个 pins 围栏，S 围栏内行零反引号路径 token＝S_HEAD_RE 归属各恰命中本面路径。九钉钉语两两互不含自查＝旧新调用行两两不同串；import subprocess 与 def 定义行与其余各行互不含坐实（git_hooks_dir 定义行不含新 hook 调用行段＝互不含）。工程师开工对九钉对开工基线逐枚复算 V0 相符方可动笔＝D-92；现算与表钉不符＝H-0 停笔呈裁禁凑绿。）

---

## 三、判据（收口判据闭集·逐条实跑留读数·起草轮 scratch 装配预演证据随注）

1. **两面改动原子性（机械）**：改动笔 git show --name-only --format='' 对该笔 sha 恰 **2 面**（csot／hook-health·多一少一即红）；git diff --numstat 开工ANCHOR..HEAD 对两面分别＝share/check-source-of-truth.py「**22 2**」／share/check-hook-health.py「**18 1**」（起草轮 git diff --no-index 预演现算在册 §〇-6）；行数收口 wc -l＝csot **860**／hook **182** 两值（＝基线行数和 numstat 净增机械闭合）。预演证据＝起草轮 patched 装配件全过在册。
2. **钉值收口（机械）**：python agent-skills/fuxi-skill/gates/check-ticket-pins.py --ticket 本票面仓根相对径 --base 开工ANCHOR实sha ＝钉行 **9**｜违例 **0**｜exit 0（钉数 grep -c '^PIN|' 对票面 ≡ **9** 申报对咬）；收口面 grep -cF 逐枚＝旧段三枚各 **0**＋新段六枚各 **1**。
3. **主仓根零感知（验收硬判据①·机械）**：收口主仓根全套闸复跑＝bash share/run-gates.sh 带 --root 主仓根与 --no-write＝**GATE PASS exit 0（发现 33389 条）**与 §〇-4 全等（对在飞会话零感知）；分项＝改后 csot --root 主仓根现跑汇总行与 §〇-4 逐字节全等＋改后 hook-health --root 主仓根现跑＝exit 0 零发现＋snapshot 行「hooksPath-readings=0｜hook-blob=8b7857701594264421832edd30dae7e401f85719｜hook-mode=0o0」与基线逐字节全等（起草轮预演 diff 零行实证 §〇-6）。
4. **worktree 根两红归零（验收硬判据②·机械）**：收口 worktree 根全套闸复跑＝同命令 --root 指 worktree 根＝GATE BLOCK 两枚红面归零＝改后 csot --root worktree 根现跑 exit **0**（汇总行与主仓根态全等·预演实证 §〇-6）＋改后 hook-health --root worktree 根现跑 exit **0** 零发现（FX-HOOK-1 消失·snapshot 行 hook-blob 对钉在场）；对照取证＝开工两态基线日志两件（.scratch/SWB-WTGATE-draft/ 两 log）随回执与 QA 复跑参照；复现取证件对照写死＝收口读数逐行 diff 开工基线日志＝差集恰两枚红面消失行＋其 snapshot 行 absent→在场变化行，余零差。
5. **钩子与钉值存续（验收硬判据③④·机械）**：.git/hooks/pre-commit 盘上 git hash-object 现跑＝8b7857701594264421832edd30dae7e401f85719 对钉全等存续＋share/install-hooks.sh blob 对开工基线全等（f71474ac）＝两枚零字节；EXPECTED_HOOK_BLOB 常量行零改动＝§二 S2 零碰随注＋改动笔 numstat 内该件 diff 不含该行（git show 改动笔 diff 逐行核＝常量行只现于上下文零加减号）；若收口时该钉语义需随 worktree 调整＝列入候裁禁自行改（§四-4）。
6. **自咬与清单存续（验收硬判据⑤·机械）**：改后 csot --selftest-seatdecl 五用例全绿 exit 0（与开工基线 §开工前置⑤ 全等）；两枚脚本对 --root 旗与退出码闭集行为零变（用法错 exit 2 面抽一：--root 不存在＝两枚各自 usage error exit 2 现跑）；run-gates.sh blob 全等（11a6f4d4）＝清单行 ROOT/share/check-source-of-truth 与裸名 check-hook-health 两清单项存续（grep 该行现跑在册 §〇 禁动表）；check-ticket-pins --selftest 用例 5／反常 0 exit 0 存续复跑。
7. **落链前靶检与实体自查（起草与施工各自）**：每笔落链前 python share/check-pointers.py --target 本笔件仓根相对路径 exit 0 零 BLOCK＝写死判据（起草轮本票面读数 §六在册；改后两面收口靶检各 exit 0＝脚本件 .py 非 md＝check-pointers 射程外仍必跑＝--target 对 py 件 exit 0 案型照登）；收口面对两改后件 python share/check-entity.py --root 仓根 扫描面（三分类目录）不含 share/ ＝两面天然不入扫，本票两枚入链 md（票面居 .scratch/tickets 豁免桶＋回执居 receipts）＝check-entity 对 .collab/.scratch 剪枝在册＝四谓词计数 0 复跑随回执登记。
8. **链面闭集（机械）**：git diff --name-only 开工ANCHOR..HEAD 本链笔 ⊆ §一 声明闭集五面（票面／起草回执／csot／hook-health／工程师回执）；git diff --name-only 开工ANCHOR..HEAD -- share/ 除两枚改动面外＝**空集**；§一 禁动对钉八枚收口点 git ls-tree HEAD 对开工点全等。

（H-0 被动咬处置分支（写死）：实跑出现——九钉现算与表钉不符／pins exit≠0 或钉数≠9／主根闸复跑非 GATE PASS 或发现数波动非归因零／worktree 根两红未归零或新增红面／钩子 blob 或 install-hooks.sh blob 对钉不符／numstat 非「22 2／18 1」／wc 两值非 860/182／改动笔面数≠2／禁动面 blob 对钉不符／自咬用例变动＝当场是红：工程师席立即停笔（禁改判据、禁凑绿、禁回改史账、禁自行加帽、禁顺手消音非射程脏面），回流件如实登记咬合明细＋定位串＋复现命令，呈主理人裁另案；本票按异常销账路径收口。咬出缺陷≠事故，凑绿＝事故。）

（灰度判据声明字段（decision-pack 装配核对面·票内声明不现场裁量）：本票灰度＝无灰度全量切换（两枚判臂改动＝主根逐字节等价＋worktree 根归零两态判据即 §三-3/§三-4 全套闸复跑读数；回退路径＝改动笔 git revert 一笔＝两枚 blob 对开工基线复原＝§三-6 自咬与 §三-3 基线全等即回退验证面。）

---

## 四、登记项知会（已裁登记·不入本票射程·非候裁·随收口知会）

1. **候补池随注一行（钩子动态根＋钉值随正另票）**：.git/hooks/pre-commit 两处 --root 硬编码主仓根字面＝worktree 内提交时钩子内 git 子进程 env 交叉致 check-adr 两跟混算假阳 159 枚（FX-U50 回执 §五 案型①白纸在册）＝本票禁动钩子＝EXPECTED_HOOK_BLOB 钉值零扰动＝对在飞会话 commit 闸行为零感知；钩子动态根＋该钉值随正＝另票候排。
2. **候补池随注二行（install-hooks.sh worktree 感知制度化）**：钩子生成器 L100-101 同款仓根字面插值＝钩子再生成覆回硬编码形态（FX-U50 回执 §五 候补池随注一行在册）＝制度化归技能票另票候排；本票零触该安装器。
3. **候补池随注三行（untracked 证据域补盘口径是否立规）**：untracked 域（证据语料）不随 worktree＝会话开工补盘前置（FX-U50 案型乙在册·与本票无关）＝是否立规归决策者另裁；本票零碰证据域。
4. **EXPECTED_HOOK_BLOB 语义候裁**：若未来钩子随正（候补池一行落地）致 blob 变动＝该常量随正与 worktree 语义适配＝另票射程（钉形制＝改动前先查钉值对账＝今日钩子改撤往返案型教训入票面纪律·本票自践＝§〇-2 全等坐实后方禁动写死）。

---

## 五、回执与链条

起草回执＝仓根 .collab/receipts 桶「2026-11-18-SWB-WTGATE-起草回执-架构席-v1」件（裸写·另笔·本席出）：含开工 HEAD 照登（8d6b6740）＋起草笔 sha＋staged 两读差集自查行＋改动面起点 blob 两枚与禁动对钉八枚对开工基线现算 blob 表（＝票面回填值出处）＋两态基线全套读数（主根 GATE PASS 发现 33389＋分项关键行／worktree 根两红复现明细）＋自咬两器读数＋scratch 装配预演全套读数（patched diff 零行＋numstat 22 2/18 1＋两态归零实证）＋§四 登记项转录＋撞锁等待轮数照登＋自查完工判据逐条。

收口链＝票面笔（起草一笔）＋起草回执笔→双席独立审（fresh eyes 互不读·同时派出·QA 席＋产品席）→会师→rev（如有修单）→放行呈皮总→工程师改动笔（两枚一面·一笔）＋工程师回执笔→QA fresh eyes 全实跑（§三逐条复现＋对抗例：对抗一「钉块 fail-closed 活性」＝删整 pins 块必 exit 4／删单枚钉必违例如实登记；对抗二「主根零感知活性」＝scratch 副本对改后 csot 再改一字符→§三-3 主根汇总行必变即红；对抗三「回退路径活性」＝scratch 假树对改动笔 revert→§三-3/§三-6 基线全等复现）→收口登记；台账随注归台账席收口另笔，本票零预写。

施工段 commit 计划闭集＝改动笔（两枚真源一面一笔·封顶一笔）→工程师回执笔（封顶一笔）＝**施工段两笔封顶**；D-95 分段落笔＋FX_COMMIT_DECLARE（纯路径清单形态）＋pathspec 两端条款同 §头写死。本票链面封顶总账＝起草 2＋施工 2＝**四笔封顶自算坐实**（双审件／rev／放行／QA 判词／收口登记各随其链另计不预占）。

---

## 六、落款（起草席自查读数·2026-11-18·arch-swb-wtgate）

- 起草开工 HEAD 实测＝8d6b67401ebfbc4a8b34326514b350c93db5ad65（链顶现读·派工预期全等）；脏面＝board 计划 v2（M·他案）＋FUXI-U50 旧名残件（A·staged·blob 80c9948f 现读）＝照登零碰零带入；锁面＝NO-INDEX-LOCK 现读。
- 开工前置现跑在册：改动面两枚起点 blob＋禁动对钉八枚对 8d6b6740 现算 blob 回填 §一（4fe99f6c/b778dc75＋11a6f4d4 等全表）；钩子 blob 8b785770 与 EXPECTED_HOOK_BLOB 全等坐实；两态基线＝主根 GATE PASS exit 0 发现 33389／worktree 根 GATE BLOCK 恰两枚（exit 2＋FX-HOOK-1）；seatdecl 自咬五用例全绿 exit 0；pins 自咬用例 5／反常 0 exit 0。
- scratch 装配预演在册（仓根 .scratch/SWB-WTGATE-draft/patched/ 不 commit）＝基线 blob 现读面＋§二 规格程序化置换＝旧段计数断言 1/1/1 全过→改后 csot 主根输出与基线 diff 零行＋worktree 根 exit 0 归零＋hook-health 两态 exit 0 且 snapshot 全等→numstat 22 2／18 1＝§三-1/-3/-4 判据可机械跑坐实。
- pins 与靶检在册：起草轮预跑＝九钉对基线 8d6b6740 现跑违例 0（预跑读数对 ANCHOR 现算随回执登记）；靶检＝python share/check-pointers.py --target .scratch/tickets/2026-11-18-SWB-WTGATE-闸工具worktree感知两脚本判臂git原生定位置换票-v1.md exit 0（落链前在册＋落链后终值入回执）。
- 红线申报：本席产出＝.scratch/tickets 本票一笔＋.collab/receipts 回执一笔；share/ 全部真源零字节（本席起草全程——patched 预演副本居仓根 .scratch 不落任何真源）；两枚脚本本笔零碰＝施工归放行后工程师席；零 git config 写；零 BYPASS；零 amend；零删锁；钩子零触；worktree 两工作区零触；他案链面照登零碰。
- 时戳占位符纪律＝本票链上占位一律 %ct（%cT 非法形态禁复用＝U41 勘正先例）。

（票面完——闸工具 worktree 感知维护票：排程已放行照此成文零候裁；登记项四条单列知会；本席起草段止于此。）