# SWB-GTFAST · 闸提速与射程票＝扫描域划界首位（lint 剪枝口径修正＝包内 .collab/.scratch 划出主根射程＋各全树剪枝补 .workbuddy/）＋提交门改靶检（run-gates 新增 --staged·逐枚优先级按实测耗时）＋全量扫描移位周期闸（日终对账窗现跑）＋钩子动态根（去 --root 硬编码·EXPECTED_HOOK_BLOB 钉随正）｜v2

> 本版＝**v2（rev 轮票面）＝取代 v1**（盘上同名 v1 件保留作史参照，不再受理工依据）；取代理由一句话＝产品席红旗 R1（S1-a 现文保留主根 .scratch 约两万枚 md/txt 入扫＝提交门秒级主根口径结构性不可达）＋两席同族判据①造靶盲区（QA Y1），主理人会师决议定 rev 修单落实（S1-a 保留面收窄＋判据①双靶＋QA 黄旗措辞并入＋候补池随注两行），点名处外 v1 内容零动。
> 票号＝SWB-GTFAST（编号续位现盘自查＝仓根 .scratch/tickets 与仓根 .collab 两域 grep GTFAST 字样零命中现跑坐实＋git grep 对 HEAD 全仓零命中＝新建 v1 案型；本线先例 SWB-WTGATE／SWB-BKTCLS 同族裸号段在册）｜起草＝架构席（arch-swb-gtfast）｜日期＝2026-11-18｜rev＝架构席（arch-swb-gtfast-rev·fresh 接手即认领·会师决议措辞落笔）｜rev 日期＝2026-11-19｜被派＝**工程师席**（施工段笔数随放行另计·见 §五）；本席只出票面零碰 share/ 真源＝纯规格零施工红线写死。
> 排程依据（已批在册·票面禁候裁排程）：决策者 2026-11-18 21:48 皮总原话口径「分析合理，起票治理」＝起闸治理票；观察账登记件＝.scratch/2026-11-18-观察账-闸全量扫描临界区时长-v1.md（在盘现读·32 行·现象样本＋归因候选＋开查触发条件在册）＝**本票＝该观察账提级产物**（提级触发命中在册：闸假阳性拦合法提交＋绕行留痕达临界观察值）。
> 落位实证随注（承 WTGATE 先例）：仓根 .collab 无 tickets 桶（share/check-collab-buckets.py 十七桶白名单不含 tickets＝新建触 MC-BUCKET-1）＝本票面照先例落 .scratch/tickets/（.gitignore L61-64 票面桶豁免行在册现读）、起草回执落仓根 .collab/receipts/。
> 开工锚照登（起草席 2026-11-18 当轮实测）：开工 HEAD＝2d0116a9581f306da8940b41c875232089cd4b41（链顶现读＝改动笔 811bd223＋回执笔 2d0116a9 之后·分支 main 现读）；git status --porcelain 去 ?? 读数＝恰一枚＝仓根 .collab/board/2026-11-17-五份复盘合流与下一轮迭代计划-v2.md（M·他案在飞·零碰零 reset 严禁带入）；?? 散件群＝32 枚照登零带入（.py 散件／.scratch 取证族／worktree 侧台账散件等）；锁面＝NO-INDEX-LOCK 现读（.git/index.lock 不在盘）；worktree list 现读六条照登＝主根挂 main＋qa_t10_dy（detached·prunable）＋D:/cs1-wt（detached）＋D:/multi-agent-collab-devkits.wt/agent-experts/baigong-software-team 挂 baigong-software/main＋D:/multi-agent-collab-devkits.wt/agent-skills/fuxi-skill 挂 fuxi/main＋D:/multi-agent-collab-devkits.wt/wtgate-verify（detached 挂 2d0116a9＝WTGATE 验收在飞件·勿动勿判脏零触）。工程师席开工 ANCHOR＝开工当轮 HEAD 实测（应为含本票起草笔或其后续合法放行笔的链顶）照登；ANCHOR 不符＝停手上报，禁带差开工。
> 并发防护（承 WTGATE 同制）：每笔 pathspec 限定 add 与 commit 紧邻无窗口；FX_COMMIT_DECLARE 本笔面＝纯路径清单形态；禁 git add -A、禁 amend、禁裸 git commit；message 零 at 符号字符零反引号；commit 带长 timeout 且输出重定向落盘仓根 .scratch/SWB-GTFAST-build/；撞 index.lock 或有界等待一轮即呈报主理人（零删锁零二次重试）；本仓提交权归一在册＝投递归主理人唯一链面操作员，本席与工程师席全程禁 git 写操作（起草段＝只落盘两文件＋回报）。

---

## 〇、复核结论（架构席 2026-11-18 对 2d0116a9 实读实跑实查，票内定稿依据）

1. **钩子实位现读**：.git/hooks/pre-commit 盘上件＝六行（shebang＋注释三行＋set -u＋两行调用）；git hash-object 现跑＝8b7857701594264421832edd30dae7e401f85719 与 share/check-hook-health.py L47 EXPECTED_HOOK_BLOB 常量（现读）**全等坐实**（存续态）。钩子两行调用均硬编码主根绝对路径字面 D:/multi-agent-collab-devkits（声明闸行＋末行 exec bash run-gates.sh --root 主根）；钩子件住共享 common dir（.git/hooks）＝被一切 worktree 的 commit 共享触发＝worktree 侧提交也触发主根全扫＋主根 BLOCK 风险殃及分支工作区（射程坐实）。core.hooksPath 未配置（git config --get 现读空 exit 1）＝钩子唯一经 .git/hooks 生效。
2. **提交链耗时与脚本耗时现跑归因（主理人转引实测＋本席复跑对照）**：观察账样本两枚＝改动笔 7m03s／回执笔 6m57s（证据件套出 at21-22-08 组＝主理人转引）；**主理人当轮逐枚实测在册**（取证件＝.scratch/GTFAST-timing/per-gate-timing.txt 现读全表）＝check-collab-lint **141603ms**／check-pointer-closure 10278ms／check-pointers 9974ms／check-ticket-reconcile 3056ms／check-source-of-truth 601ms／check-entity 475ms／check-adr 385ms／check-hook-health 301ms／check-provenance 272ms／check-collab-buckets 233ms／check-skill-meta 217ms＝总计约 168s；**本席复跑对照**＝lint 一枚复跑 real 1m45.6s（约 105.6s·与转引 141.6s 同量级·读数差如实登记不追因）＋csot 单枚复跑 real 0m0.676s（日志 .scratch/SWB-GTFAST-draft/ 两件）。
   **根因坐实三件（归因段定稿）**：
   - 根因一＝**热点单点 check-collab-lint 占约 84%（141603ms／168s）**：该件 L153-154 os.walk 整仓根但剪枝闭集仅 .git／__pycache__ 两项＝各包**包内 .collab/.scratch 记录卷宗全量入扫**（计数现跑＝agent-skills/external-advisor-collab 包内 .collab/.scratch 族 12602 枚／agent-skills/fuxi-skill 包内 7530 枚；主理人转引口径 8839／6738 系不同 find 口径＝两读数并存不追因）；逐文件逐行跑 L2_PATTERNS 九组正则＝耗时主头坐实。**归因侧重校平（rev 轮·产品席黄①落实）**＝耗时大头实测在**主根 .scratch 松散取证面**：仓根 .scratch 全量 168,347 枚／md-txt 146,329 枚＝磁盘 md-txt 总面约 92%（产品席与 QA 席两席独立现跑计数全等＝find 口径）；baseline log 现读 lint 6,357 行发现中 6,075 行（95.6%）出处主根 .scratch＝扫描成本主体与发现产出主体分离；包内卷宗为**次大头**。**本席实读勘正随注（转引括注「同侪脚本皆剪 .collab/.scratch」的精确化）**＝剪枝闭集含 .collab/.scratch 者实为 check-entity L177 一枚＋check-ticket-reconcile L295-298 过程域剔除臂两枚；check-pointers L334 与 check-pointer-closure L126 的 walk 亦不剪（其扫描域＝三分类目录/包面故包内卷宗照入＝两枚 WATCH 族大头来源），唯 lint 连扫描域都不设＝整仓根入扫＝最重。
   - 根因二＝**扫描域虚宽通病**：tracked 面 1921 枚（git ls-files 现跑）对磁盘扫描面 .md/.txt 粗计 15 万+（find 现跑＝含他包卷宗＋.workbuddy/ 记忆面＋scratch 取证族全量入扫）。
   - 根因三＝**提交门语义错位**：全仓体检挂每次提交＋裁决段写证据件 33391 发现逐条落 json（advisory 全量落盘＝单次证据件群 MB 级＝周期侧负担挂提交临界区）。
3. **全量扫描无缓存无并行无增量现读**：share/run-gates.sh L141 SCRIPTS 清单十一枚串行（L144-155 循环体逐枚 python 调用）＝零缓存零并行零增量坐实；run-gates.sh 已内置 --no-write 只读模式（L67 帮助行）；各全树脚本各自独立 os.walk，剪枝闭集现状＝check-entity L177（.git／__pycache__／.collab／.scratch 四项）／check-collab-lint L154（.git／__pycache__ 两项·**扫整仓根**）／check-pointer-closure L126（包面 walk·两项）／check-pointers L238 索引 walk＋L334 扫描域 walk（两项／两项）／check-ticket-reconcile L295（三项含 node_modules）／csot L256＋L693（两项·扫兄弟仓与技能真源根）＝各面均不含 .workbuddy/。
4. **扫描域虚宽假阳性咬闸实证现跑**：python share/check-entity.py --root 主根（GATE_PROJECT_NAMES 注入缺省口径）现跑＝**BLOCK 恰一枚**＝agent-experts/baigong-software-team/.workbuddy/memory/2026-11-18.md:34 OA-T1 项目实体命中 pattern=date count=2（该件＝他包运行时记忆面·git check-ignore 现读＝.gitignore L71 .workbuddy/ 规则命中＝**untracked 非 tracked**（git ls-files 全仓 .workbuddy 计数 0 现跑））；该 BLOCK 经路由表 OA-T1 判 block＝**全套闸现跑出口①＝GATE BLOCK exit 1**（见 §〇-6）＝合法提交被咬＝迫使 ALLOW_GATE_DOWN=1 留痕绕行（本日证据件留痕存量现读＝.collab/evidence/gates 全桶 12707 枚 json 中 bypass 留痕 150 枚现跑计数·当日新增在册 at21-22-08 组）＝留痕常态化临界值坐实。
5. **既有可复用机制现读**：share/check-pointers.py 已有 --target 单文件靶检（L75/L482/L515-523 现读·各席落笔前自查先例常态化·本席本票面落笔前自靶在册 §六）＋--scope 扫描域入参；check-ticket-reconcile.py 已有 --ticket 靶入参（L784 append 现读）；check-staged-declaration.py 已在钩子链 run-gates 之前 fail-fast（不进 run-gates 清单·头注 L16-18 现读）＝暂存面取径先例在册；reconcile-daily.py 实体＝agent-experts/baigong-software-team/skills/sop/scripts/reconcile-daily.py blob ff1e4d87e88116ac1da324907f10c9bde13a36c6 现读（日终对账六类记录 vs git 提交交叉核·非闸件·周期位置在册）；60-gates.md json 围栏＝路由表唯一机器源（run-gates.sh 运行时解析 L230-256·出口①②③语义／退出码闭集 0-4／ALLOW_GATE_DOWN 留痕硬规矩 L527-530）＝**本票判据本体零动**（见 §一 禁动面）。
6. **两态基线现跑（起草当轮·收口判据基面）**：主根全套闸 bash share/run-gates.sh --root 主根 --no-write 现跑（后台重定向件 .scratch/SWB-GTFAST-draft/gate-mainroot-baseline.log）＝**GATE BLOCK exit 1 恰一枚**＝- agent-experts/baigong-software-team/.workbuddy/memory/2026-11-18.md:34 OA-T1 BLOCK（＝§〇-4 假阳性在闸面现行复现）；按 run-gates FINDING_RE 口径逐脚本发现数现算＝**总 33391**（check-pointers BLOCK 18231／WATCH 4575＋check-collab-lint WATCH 6353＋check-pointer-closure WATCH 3754＋check-source-of-truth WATCH 467（注＝含链上 WTGATE 改动后态·单枚汇总行「文件 129｜BLOCK 0｜基线豁免 54｜指针 WATCH 413」另含 NOTE 行不入计数）＋check-ticket-reconcile WATCH 10＋check-entity BLOCK 1）；provenance／skill-meta／adr／hook-health／collab-buckets 各零发现。**钉值口径随动写明**：派工转引旧链态值 BLOCK 族 22810／GATE 族 151502 系 DEBTCLN-R1 至 BKTCLS 期旧链态值（该两票在册原文现读＋「钉值系链态值·验收轮以当轮现跑对拍为准」先例口径在册）＝本票基面以 §〇-6 现跑值为准，旧值作废不追因；钩子 blob 现值对钉全等（§〇-1）。
7. **改名取径可行性现读**：git diff --cached --name-only 对改名笔天然输出新旧两侧路径行（先例笔 526b5ce7 七枚 git mv 在册形态＋本席 git log --diff-filter=R 现读印证）＝S2 靶集「含新增／改名两侧」的机械取径成立；check-pointers --target 形态下 build_indexes(root) 仍整仓建索引（L510 现读＝靶检只收窄被检文件集，解析锚索引不动＝判据口径零动的天然形态）。

---

## 一、声明闭集与禁动面

**本票射程（改动面候选闭集·施工段笔数随放行另计）**：

1. .scratch/tickets/2026-11-18-SWB-GTFAST-闸提交门靶检与周期全量与钩子动态根扫描域划界-v2.md（本票面 v2·rev 席落盘件·投递归主理人；同名 v1 件盘上保留作史参照不入投递面）
2. 仓根 .collab/receipts 桶内「2026-11-18-SWB-GTFAST起草回执-架构席-v1」件（起草席回执·已落链链上件 append-only 不回改）＋「2026-11-19-SWB-GTFAST票面rev回执-架构席-v1」件（rev 席回执·裸文写·投递归主理人）
3. share/run-gates.sh（改·S2 提交门模式＝参数面＋暂存取径＋分派段见 §二）
4. share/check-collab-lint.py（改·S1-a 剪枝口径修正＋S1-b 剪枝补 .workbuddy/＋S2-d 补 --target＝本票改动最重一枚）
5. share/check-pointer-closure.py（改·S1-b 剪枝补 .workbuddy/＋S2-d 补 --target）
6. share/check-pointers.py（改·S1-b 扫描域 walk 剪枝补 .workbuddy/——**基名索引面是否随划界＝候裁 C-1 见 §四**；S2 零改动＝--target 既有）
7. share/check-entity.py（改·S1-b 剪枝补 .workbuddy/ 一处＝四→五项；S2 豁免全跑零靶入参＝取舍见 §二 S2-c）
8. share/install-hooks.sh（改·S4 钩子体动态根＋钩子目录定位改 git 原生旗）
9. share/check-hook-health.py（改·S4 EXPECTED_HOOK_BLOB 常量行钉随正恰一行）
10. .git/hooks/pre-commit（盘上件·非 git 面·经改版 install-hooks.sh 重装再生＝S4）
11. 仓根 .collab/receipts 桶内工程师回执件（施工段另笔·落链后补入本闭集随回执申报＝先例口径）

**禁动面点名＋零碰清单（写死）**：agent-skills/multi-collab/references/60-gates.md（blob b68cbfc7df9f20a2ae41c86499863793f0ec9dfa 对开工基线现算回填＝**判据本体与路由表 json 围栏零动**；若周期闸需规范侧立据＝升候裁 C-2 见 §四，不自行裁）／share/check-source-of-truth.py（本票零改动＝豁免面见 §二 S2-c 表；其 walk 面＝兄弟仓与技能真源根，.workbuddy 候排随注 §四-3）／share/check-ticket-reconcile.py（本票零改动＝豁免全跑取舍见 §二 S2-c；其 listing 面 .workbuddy 现跑零命中＝S1 候排 §四-3）／share/check-staged-declaration.py（零字节）／share/check-provenance.py／share/check-skill-meta.py／share/check-adr.py／share/check-collab-buckets.py（四枚零字节＝豁免理由见 §二 S2-c 表）／run-gates.sh 裁决段内嵌 PY 段（L157-543）整体零动＝证据件写盘语义零动（瘦身归候补池 §四-6）／share/baseline-sot-dup.json blob 2c44d339890811304d7f1cd3a355d88ee547e5e6＋share/baseline-seat-decl.json blob f6171c7db03cf79529c89795fd243e2a78a22b12（两枚基线 json 零字节）／60-gates.md 路由表 per_spec 与 on_severity 语义零动／**agent-experts／agent-skills／softwares 三包内容零碰**（reconcile-daily.py 只引用不改动）／仓根 .collab/ 全域（含 board 他案 M 面）零碰／.collab/evidence/gates 证据桶只读零删／WTGATE 在飞面零触（D:/multi-agent-collab-devkits.wt/wtgate-verify 工作区＋.scratch/SWB-WTGATE-qa/ 取证目录）／任何 .workbuddy/ 记忆面文件零碰零删（S1 只改扫描剪枝，不碰被扫件）／worktree 各工作区 checkout 零触／git config 零写（钩子经 install-hooks.sh 再生成，不迁 hooksPath）／链上他案笔照登不归因。

改动面起点 blob 表（对开工链顶 2d0116a9 git ls-tree 现算回填＝参考位；工程师开工对开工基线当轮现算对账，不符＝H-0 停笔呈裁禁凑绿）：

    share/run-gates.sh              11a6f4d4ee1b384117ae405c68024198b025f037（543 行）
    share/check-entity.py           1f4be3222df8459b83657f5da30851caccea2a51（302 行）
    share/check-collab-lint.py      d963f5a20aff12d2cf1442eeada840bcacf49f6d（341 行）
    share/check-pointer-closure.py  717a2adfe4b363609363e92e017cb16ac4124f1e（293 行）
    share/check-pointers.py         33781b312e7029a02ec05626121bcf12c78d7276（551 行）
    share/install-hooks.sh          f71474ac4a7c7e6f8e754c8f55b123c64d541507（136 行）
    share/check-hook-health.py      7fd83074bf50144fa5220283da1f93e079e4d5ed（182 行）

钩子面盘上对钉（非 git 面）：.git/hooks/pre-commit 现值 8b7857701594264421832edd30dae7e401f85719＝开工态对钉全等（§〇-1）；S4 改后新钉值＝§二 S4 逐字重建件现算 **02d30d01e53f9c7b38803dfbd1d599f9a23c4d16**（＝对 §二 S4-a 围栏字节序列 git hash-object 现跑·起草轮预演在册 .scratch/SWB-GTFAST-draft/new-hook-fenced.sh）。

---

## 二、施工规格（工程师照录·本席零施工·改动＝锚行定位＋插段/行内置换·程序化替换先断言计数再替换）

**总则（写死）**：各件 LF／CRLF 形制随基线存续禁改写（本仓 autocrlf=true 检出 CRLF 案型在册＝脚本内 read_lines 归一行不动）；判据口径一字不动只改取径（承 WTGATE「只改定位不改判据」规格）；各件头注 spec-provenance 块零字节（锚行与 clause_sha256 不动＝check-provenance 零扰动）。

**S1 · 扫描域划界（首位子项·根因一与根因二直打·两点）**

S1-a **lint 剪枝口径修正（最大单项收益·v2 依主理人会师决议改写保留面＝产品席红旗 R1 修单）**：check-collab-lint.py iter_files（L151-154 现读）剪枝规则改＝os.walk 整仓根存续，机械判据＝**目录名为 .collab 或 .scratch 且其相对仓根路径段数 ≥2 即剪（包内卷宗款存续）；根 .collab 不剪照审（治理本意＝主仓治理记录卷宗留射程，零稀释）；根 .scratch 除 tickets 子树外剪（保留面收窄款＝新增）**。仍是一句可机械判定的剪枝谓词，不改判据本体，只换入扫文件集，与本子项「EAC-L1/L2/L3 判据函数本体零动＝只换入扫文件集」总则零冲突。tickets 子树保留理由＝该子树＝.gitignore L61-64 豁免面＝主根票面真源＝lint EAC-L2 判据审计对象（票面先例）；保留成本可忽略＝baseline log 现读该子树 lint 发现仅 11 枚（本席 rev 复跑复核＝补丁副本输出中 tickets 子树命中恰 11 枚，与 baseline log 现读 11 枚全等＝读数登记见 rev 回执 §三）。归因写明＝业务包包内记录卷宗归**各包工作区自审**（各活跃线住各 worktree 的在册形态＝包闸在包工作区跑包面；主根提交门不背他包卷宗）；根 .scratch 松散取证面归**周期闸侧＋取证桶卫生候补池**（§四-7/§四-8）。预期效果登记（A/B 实测族照登）＝未改全扫 real 132.8s（发现 6,357 行）／S1-a v1 现文版 real 52.9s（入扫 20,899 枚其中根面保留 20,612 枚＝残留主根 .scratch 松散面约 45 秒级每提交固定税，v1 版作废）／**S1-a v2 修单版＝7.2s（产品席修法候选版实测）**；QA 席补丁副本实跑＝入扫 160,917 降至 20,845（−87.0%）／lint 139.9s 降至 65.7s（v1 现文口径下）；**本席 rev 复跑对照一枚**＝按 v2 修单判据造补丁副本（.scratch/SWB-GTFAST-rev-arch/lint-s1a-rev.py）现跑＝入扫 684 枚／real 0.797s／发现 14 枚（EAC-L2＝14＝根 .collab 面 3＋tickets 子树 11）＝同窗未改版单枚复跑 real 144.1s（日志四读数族 141.6s／132.8s／139.9s／144.1s 并存＝IO 波动不追因）。＝lint 热点从约 133-144s 级降至亚秒-7 秒级＝提交门秒级档主根口径机械可达。

S1-b **各全树脚本剪枝闭集补 .workbuddy/**（与 .collab／.scratch 记录件划界同口径＝物理划界非日期级豁免）：check-entity L177（四项→五项）／check-collab-lint L154（并入 S1-a 一次改动：.workbuddy/ 整词目录任何深度皆剪）／check-pointer-closure L126（两项→三项）／check-pointers L334 扫描域 walk（两项→三项）；check-pointers L238 基名索引面是否同补＝**候裁 C-1 未裁前零动**；run-gates.sh 裁决段 spec_id_resolvable 内 L285 walk（包规范件解析面）＝S1 候排 §四-3；csot／ticket-reconcile walk＝§一 禁动面候排随注（现跑零命中）。.workbuddy 目录名整词划界（只剪目录段恰等 .workbuddy 者，不剪同名后缀文件）。

**S2 · 提交门射程收窄（run-gates.sh 新增 --staged 模式·逐枚优先级写明）**

S2-a run-gates.sh 参数面（锚行现读 L56-57 ROOT_ARG=""＋NO_WRITE=0 两行之后插一行 STAGED=0；L59-71 参数 while 内 --no-write 行之后插一支 --staged 处理行）。缺省模式（不带 --staged）行为零变＝全量扫描存续为周期闸执行体（S3）。

S2-b 暂存面取径（ROOT 定位段之后、路由表定位段之前插段）：--staged 置位时执行 git -C "$ROOT" diff --cached --name-only 取暂存文件集（改名两侧天然含入＝§〇-7 现读印证）；git 不可用或非工作区＝die_infra（exit 4 fail-closed，不得降级为全量也不得静默放行）；暂存集为空＝打印「GATE PASS（--staged 暂存面为空）」exit 0（无暂存内容＝提交门无可检靶，声明闸已在钩子链先跑零扰动）。

S2-c 逐脚本取径分派（**优先级按 §〇-2 实测耗时排**·L144-155 循环体内按 name 分派·靶集注入＝逐文件传参·文件名含空格必带引号）：

    第一（热点直打）
    check-collab-lint       新增 --target（见 S2-d）·暂存 ∩ .md/.txt＝141.6s 热点靶化（即便 S1-a 已划界，提交门仍靶检＝两子项独立生效）
    第二（合计约 20 秒族）
    check-pointers          既有 --target 逐个暂存 .md 传入（索引面不动＝判据零动天然形态·9.97s）
    check-pointer-closure   新增 --target（见 S2-d）·暂存 ∩ 包面（10.3s）
    其余九枚＝豁免全跑（单枚均 ≤3.1s·补靶入参复杂度不划算＝如实取舍写明·耗时读数按 §〇-2 转引实测值）
    check-ticket-reconcile  豁免全跑＝3056ms＝票面自对账判据面小
    check-source-of-truth   豁免全跑＝601ms＝判据面＝兄弟仓对账面＋基线豁免链·与暂存面无交集
    check-entity            豁免全跑＝475ms
    check-adr               豁免全跑＝385ms＝tracked 桶对账判据本身＝commit 可改 tracked 面故靶检不完备
    check-hook-health       豁免全跑＝301ms＝钩子单件健康
    check-provenance        豁免全跑＝272ms＝非整树 walk 件
    check-collab-buckets    豁免全跑＝233ms＝一级 listdir 单层
    check-skill-meta        豁免全跑＝217ms＝listdir 单层

    （豁免声明理由列闭集如上＝「不支持靶入参的脚本需补靶入参或声明豁免理由」要件兑现；豁免九枚合计约 5.5s＋靶化三枚秒级＋pointers 索引面 10s 级＝提交门目标秒级档预算内。）

S2-d 两枚脚本补 --target 统一规格（check-collab-lint／check-pointer-closure）：argparse 各加 --target（action append·default 空）；给定时＝既有文件枚举结果按 abspath 交集过滤（判据函数本体零调用路径改动＝只换入参文件集）；靶交集为空＝打印该件既有 coverage/分账行形制的零发现汇总 exit 0（不触「扫描域为空 exit 4」分支——该 infra 分支只在无 --target 缺省全跑面保留）；--target 目录参数＝die_usage exit 2（承 check-pointers 先例措辞）。**entity／ticket-reconcile 本票不补靶**（S2-c 取舍写明＝复杂度不划算；既有 --ticket/--target 面零动零用）。

S2-e 空靶跳过登记：--staged 下某靶检脚本靶交集为空＝run-gates 循环仍调用之（走 S2-d 零发现 exit 0 路径），汇总行照常入 SUMMARY＝「未执行的判据不得计绿」原则零违例（判据被执行、只是靶空）。

**S3 · 全量扫描移位周期闸（零新代码·位置写明）**

周期闸执行体＝share/run-gates.sh 缺省模式（不带 --staged 的全量十一枚串行）＝**现形态即周期执行体，本票不改其代码路径**；周期挂接点写明＝日终对账窗现跑：agent-experts/baigong-software-team/skills/sop/scripts/reconcile-daily.py（blob ff1e4d87 现读·六类记录 vs git 提交交叉核）跑毕同窗接续现跑全量闸，读数落 .collab/evidence/gates 证据桶（写盘模式·出口②③语义自动生效）＋汇总读数登记当日对账件。周期模式读数与提交门基线可对账口径＝**发现数钉值口径随动**：两态均以当轮现跑对拍（§〇-6 现跑值 33391 为起草基面登记值；旧钉 22810／151502 系旧链态值作废不追因＝BKTCLS「钉值系链态值」先例口径）；周期全量发现集对上一提交门基线的差集＝增量处置入口（差≠0→呈报路径承 reconcile-daily 触发源口径）。规范侧是否需为周期闸立据＝候裁 C-2（§四），本票不自行动 60-gates.md。**证据件瘦身随注**＝advisory 全量逐条落 json（单次证据件群 MB 级＝根因三）归周期闸侧处置＝候补池随注 §四-6（本票不动裁决段写盘语义）。

**S4 · 钩子动态根＋钉值随正＋安装器制度化**

S4-a install-hooks.sh 钩子体改版（GATE_HOOK_BODY 段 L95-102 整段置换为下方逐字；MARKER 行字符串零动＝幂等三分支判定臂存续；PY 探测段／存在性检查段零动；体内 GATE_ROOT_DIR 行含字面 $GATE_ROOT_DIR——安装器双引号字符串内必转义 \$GATE_ROOT_DIR 防安装期展开，逐字节产物以下围栏为准）：

    #!/usr/bin/env bash
    # generated-by: object-audit/scripts/install-hooks.sh
    # 提交前门禁（出口①）。规范来源：设计 v2 §2.5/60-gates。
    # 改判据请改路由表规范件（agent-skills/multi-collab/references/60-gates.md），不要改本文件。
    set -u
    GATE_ROOT_DIR="$(git rev-parse --show-toplevel 2>/dev/null)" || { printf 'infra error: 钩子无法定位工作区根（fail-closed 拒提）\n' >&2; exit 4; }
    "python3" "$GATE_ROOT_DIR/share/check-staged-declaration.py" --root "$GATE_ROOT_DIR" || exit $?
    exec bash "$GATE_ROOT_DIR/share/run-gates.sh" --root "$GATE_ROOT_DIR" --staged

    （逐字节形制＝八行各一换行＋printf '%s\n' 追加末换行＝文件以空行收尾，与现行钩子 od 现读末两字节 换行换行 同形制；该逐字重建件起草轮在盘现算 blob＝02d30d01e53f9c7b38803dfbd1d599f9a23c4d16（§一 钉注）；**v2 登记不追改一行＝QA Y6**：新钩子体内 python3 硬字面与安装器 PY 探测臂并存＝与现行钩子同形制无回退＝python-only 机器上该字面触 exit 127 fail-closed 拒提＝登记在册不追改，钉值 02d30d01 不因此动。）

S4-b install-hooks.sh 钩子目录定位制度化（L86 HOOKS_DIR 行置换）：HOOKS_DIR 定位改 git -C "$SELF_DIR 所在仓" rev-parse --path-format=absolute --git-path hooks（旗两态可行性＝WTGATE 票 §〇-7 现读在册：主根与 worktree 根同读数＝共享 common dir 钩子目录绝对路径）；旗失败回退旧拼径 $REPO_ROOT/.git/hooks（fail-soft 回退不更松不更严）；L88 存在性检查行语义不变。

S4-c 改钩子必先核钉流程（写死·反咬案型在册＝改钩子不核钉必被 check-hook-health 拦）：工程师顺序＝①改版 install-hooks.sh 落盘→②bash share/install-hooks.sh --root 主根 重装（幂等刷新分支）→③git hash-object .git/hooks/pre-commit 现算对钉 02d30d01e53f9c7b38803dfbd1d599f9a23c4d16 全等→④share/check-hook-health.py L47 EXPECTED_HOOK_BLOB 常量行**恰一行行内置换**为新钉值（钉随正）→⑤改后 hook-health 现跑 exit 0。任一步对不上＝H-0 停笔呈裁。

S4-d worktree 语义随注（写死不改钉）：钩子住共享 common dir 被全部 worktree 共享触发＝动态根行随调用工作区解析＝worktree 侧提交扫该工作区（其 share/ 在场＝同仓 checkout）；EXPECTED_HOOK_BLOB 单钉值语义不变（共享钩子单件）。

---

## 三、判据（收口判据闭集·逐条实跑留读数）

1. **提交门临界区秒级（机械·验收硬判据①·v2 造靶口径修正＝产品席红旗论据②＋QA Y1 同族）**：造靶**两枚都跑**，禁只跑其一——**造靶甲＝临时验证工作区**（git worktree add 临时路径·验毕 remove）内暂存一枚含合法指针的 .md，git commit 全程计时＝date +%s%N 前后差现跑＝real **≤ 60s**（预算依据＝豁免九枚合计约 5.5s＋靶化三枚秒级＋check-pointers 索引面 10s 级现跑上限＝§〇-2 转引实测值加总）；**造靶乙＝现主根当轮现跑口径**（新增·堵盲区：临时工作区 .scratch 近空＝该判据对 S1-a 两种形态都机械通过＝验收与痛点解耦＝v1 案型禁复现）＝主根现场暂存一枚含合法指针的 .md（用毕 reset 该枚零带入·禁碰他案脏面）实跑提交门，临界区计时读数**按两层门分别登记**＝提交门 --staged 档计时＋周期档（缺省全扫模式）计时各一读数。造靶甲读数入 ≤60s 硬线判定；造靶乙两读数＝主根现场实态登记对照（提交门 --staged 档对主根堆积面亦应秒级——S1-a 修单后根 .scratch 松散面不入提交门靶检与全扫；周期档仍分钟级属预期＝两态分工坐实）。
2. **取径不更判据（机械·验收硬判据②·v2 措辞精度并入＝QA Y2）**：同一靶文件集上，改后靶检输出逐发现行与该件缺省全扫输出中属该文件的行**逐行 diff 空集写死子集方向**＝靶检输出 ⊆ 缺省全扫属该文件行（靶集下配对不全则该行整体不出＝check-collab-lint check_l3 目录级分组判据案型＝**对称 diff 会假红禁跑**，只跑「靶行在全扫属该文件行中找不见」单侧＝子集违反才红）（两枚补靶脚本各验一枚暂存件：真阳性件＋零发现件两例）；--staged 空暂存 exit 0 读数在册；九枚豁免件中七枚零改动件（csot／entity／adr／hook-health／buckets／provenance／skill-meta）缺省模式输出对开工基线逐字节全等；lint 与 closure 两枚缺省全扫输出差集＝恰 S1 划界归零行（逐行归因入 §三-3 差集账）。
3. **全量移位周期闸可对账（机械·验收硬判据③）**：缺省模式代码路径零变＝不带 --staged 的收口复跑＝GATE 裁决与发现数（FINDING_RE 现算口径）对 §〇-6 基面差集恰＝S1 划界归零项（check-entity 的 .workbuddy BLOCK 消失＋check-pointer-closure .workbuddy WATCH 行消失＋check-collab-lint 包内卷宗族 WATCH 行消减＋check-collab-lint 主根 .scratch 松散面 WATCH 行归零（baseline log 现读该面出处 6,075 行＝S1-a v2 修单新增归零项，tickets 子树 11 枚保留＝§二 S1-a 登记）＝归因在册）＋链上他案笔自然漂移项逐笔归因，余零差；日终对账窗接续现跑读数登记件在册。
4. **钩子钉随正（机械·验收硬判据④）**：改后 .git/hooks/pre-commit git hash-object＝02d30d01e53f9c7b38803dfbd1d599f9a23c4d16 全等＋check-hook-health.py 现跑 exit 0 零发现（snapshot 行 hook-blob 对**新钉**在场）＋EXPECTED_HOOK_BLOB 常量行只现于改动笔 diff 的减一／加一行（git show 逐行核）；install-hooks.sh 重跑幂等＝「已是最新」分支 exit 0 读数在册。
5. **worktree 侧零触主根（机械·验收硬判据⑤）**：临时验证工作区内一次 --staged 提交实跑＝钩子定位读数＝该工作区根（run-gates 汇总行 --root 值现读＋证据件落该工作区 .collab/evidence/gates 而非主根＝取证件对照在册）；提交全程主根 .git/index.lock 不在盘（NO-INDEX-LOCK 前后两读）；主根主根证据桶当日新增计数零增（工作区提交不写主根桶＝IO 面随根划界坐实）；验毕 git worktree remove 清理＋worktree list 复读回到**施工 ANCHOR 照登数**（v2 校平＝QA Y3：v1「开工照登六条」系起草轮陈旧计数＝现读五条＝一律以工程师施工 ANCHOR 当轮照登数为准）。
6. **ALLOW_GATE_DOWN 绕行归零复验（机械·验收硬判据⑥）**：S1 划界后主根全套缺省模式复跑＝check-entity BLOCK 计数 **0**（§〇-4 假阳性归零）；OA-T1 族当日后续提交窗证据桶新增件 grep bypass 计数 **0**（收口窗后连续 ≥3 笔合法提交零留痕＝观察账开查触发条件③反证复验窗）；**v2 补收口点计数快照口径＝QA Y5**：「当日新增」计数口径＝证据桶文件名日粒度＝收口点先现跑落一计数快照（当日桶文件名件数＋bypass grep 数），收口窗后以快照差计读数，禁以窗口起点记忆值口算。
7. **fail-closed 与闭集不变（机械·验收硬判据⑦）**：退出码闭集零变抽验三例＝--staged 下 git 不可用场景（临时 PATH 剥离实跑）exit 4；--target 传目录 exit 2；缺省模式对损坏路由表（scratch 假树注入）exit 4 复现；ALLOW_GATE_DOWN 留痕语义不变＝BYPASS 生效时证据件 bypass 行在册复跑一例（scratch 假树内跑，不污染真桶）。
8. **链面闭集（机械）**：收口点 git diff --name-only 开工ANCHOR..HEAD -- share/ ⊆ §一 声明面 3-9 七枚；§一 禁动面各件（60-gates.md／csot／ticket-reconcile／staged-declaration／provenance／skill-meta／adr／collab-buckets／两枚基线 json）收口点 git ls-tree 对开工点全等；三包内容域 diff 空集。

（H-0 被动咬处置分支（写死）：实跑出现——起点 blob 对表不符／新钩子 blob 现算≠02d30d01／hook-health 改后仍红／缺省模式复跑出现 S1 归零项之外未归因差集／提交门计时超 60s／靶检 diff 非空集／worktree 提交触主根 IO＝当场是红：工程师席立即停笔（禁改判据、禁凑绿、禁回改史账、禁顺手消音非射程脏面），回流件如实登记咬合明细＋定位串＋复现命令，呈主理人裁另案；咬出缺陷≠事故，凑绿＝事故。）

（灰度判据声明字段（decision-pack 装配核对面·票内声明不现场裁量）：本票灰度＝无灰度全量切换（提交门模式经钩子即生效；回退路径＝改动笔 git revert 一笔＝share/ 七枚 blob 对开工基线复原＋install-hooks.sh 重装修复钩子回旧钉 8b785770＋EXPECTED_HOOK_BLOB 行随 revert 复原＝§三-4 旧钉复现即回退验证面。）

---

## 四、候裁单列与登记项知会

**候裁单列（真分歧才列·编排细节不列）**：

- **C-1 check-pointers 索引面是否随 .workbuddy/ 划界**：扫描域 walk（L334）划界无争议；但基名索引面（L238）现状含 .workbuddy 件＝他包记忆面基名参与「基名存在性」与「后缀唯一命中归位」两判据——划界＝他包记忆文件名不再为指针提供存在性背书（更严），不划界＝记忆面续当指针靶池（假阳性温床）。两态各有咬面，架构席不自行裁：本票 S1-b 默认只划扫描域，索引面随否请决策者裁。
- **C-2 周期闸规范侧立据**：60-gates.md 出口①现文＝「提交前拦截」；全量移位周期闸后，路由表/规范件是否需补「周期闸」条目（出口语义扩展或新出口）＝判据本体面＝若裁「需立据」则升 C1 级契约整改（60-gates.md 改动走契约票先例），本票不自行动。

**登记项知会（已裁登记·不入本票射程·随收口知会）**：

1. install-hooks.sh 生成行的 worktree 感知制度化本体随 S4-b 一并处置（候补池旧行「install-hooks.sh 制度化」＝本票射程内兑现，非候排）。
2. WTGATE 票 §四-1「钩子动态根＋钉值随正另票」＝本票 S4 即该另票兑现（收口后知会 WTGATE 线销行）。
3. S1 候排三面（run-gates 裁决段 walk／csot 两 walk／ticket-reconcile listing）＝现跑 .workbuddy 零命中或面在仓外，随收口登记候补池续位。
4. 观察账归因候选三（跨工作区共享 IO 面）＝S4/S2 落地后由 §三-5 判据实证收口，观察账本体归主理人席收口时销行（本票零碰观察账件）。
5. 本仓提交权归一在册（席禁 git 写·投递归主理人）＝本票全程遵此（起草段两文件只落盘）。
6. **证据件瘦身候补池随注（主理人转令在册）**：advisory 全量逐条落 json（33391 发现＝单次证据件群 MB 级＝根因三）归周期闸侧随 S3 处置＝另票候排；本票裁决段写盘语义零动。
7. **取证桶卫生纪律候补池随注（v2 新增·主理人会师决议）**：取证桶「用毕即拆」＝生命期划界非目录名划界；落点三处＝席位规程＋主理人收口检查单＋可选卫生 warn 机检＝百工侧职权移交射程，**本票不自行落任何纪律条款**（根 .scratch 残留面仍主导周期闸 lint 耗时的卫生侧根治归此，S1-a 修单只除提交门侧代价）。
8. **已闭案取证桶拆解＝主根盘上行动候排（v2 新增·主理人会师决议）**：现盘堆积在册＝.scratch/FX-U39-qa 26,629 枚／FX-U15-qa2 10,484 枚／FX-U18-qa 9,821 枚等（两席独立现跑全等）＝历批次收口未拆＝拆解动作候排主根盘上行动，非本票射程（本票零拆任何取证桶＝两席在飞取证族亦零拆）。

---

## 五、回执与链条

起草回执＝仓根 .collab/receipts 桶「2026-11-18-SWB-GTFAST起草回执-架构席-v1」件（裸写·本席出）：含开工读数照登（HEAD 40 位／分支／脏面计数 M1＋??32／锁态／worktree list 六条）＋两态基线现跑全套读数（缺省 GATE BLOCK exit 1 恰一枚＋发现数 33391 逐脚本分项／单枚耗时表十一枚）＋票面 blob＋行数＋新钩子候选 blob 现算 02d30d01 出处＋自靶 exit 0 读数＋§四 候裁两项与知会五条转录＋纪律申报（零 git 写／零真源碰／落位随注）。

链面＝票面笔＋起草回执笔（起草段两笔封顶·投递归主理人唯一链面操作员）→双席独立审（QA 席＋产品席 fresh eyes）→会师→rev（如有修单）→放行呈皮总→工程师施工段（笔数随放行另计·建议改动笔按 S1/S2/S4 分组但封顶另裁）＋工程师回执笔→QA fresh eyes 全实跑（§三逐条复现＋对抗例：对抗一「靶检不更判据活性」＝scratch 副本对补靶脚本注入一个必然咬中的暂存件缺陷必被 --staged 面咬出；对抗二「钩子钉活性」＝手改钩子一字符必触 hook-health BLOCK；对抗三「回退路径活性」＝假树 revert 后旧钉与旧基线复现）→收口登记。

D-95 分段落笔：起草段＝**票面一笔＋回执一笔＝两笔封顶**；施工段随放行另计不预占；本席起草段止于此。

---

## 六、落款（起草席自查读数·2026-11-18·arch-swb-gtfast）

- 开工 HEAD 实测＝2d0116a9581f306da8940b41c875232089cd4b41（链顶现读·分支 main）；脏面＝board 计划 v2 一枚 M＋?? 32 枚＝照登零碰零带入；锁面＝NO-INDEX-LOCK；worktree list 六条照登（含 wtgate-verify 在飞件零触）。
- 票号续位＝.scratch/tickets 与 .collab 两域 grep GTFAST 零命中＋git grep HEAD 全仓零命中现跑坐实＝新建 v1。
- 基线现跑在册：主根缺省模式 GATE BLOCK exit 1 恰一枚（.workbuddy OA-T1）＝日志 .scratch/SWB-GTFAST-draft/gate-mainroot-baseline.log；发现数逐脚本分项 §〇-6；单枚耗时表 §〇-2（csot 单枚现跑 real 0m0.676s）；钩子 blob 8b785770 对钉全等。
- 新钩子候选件现盘现算＝.scratch/SWB-GTFAST-draft/new-hook-fenced.sh blob 02d30d01e53f9c7b38803dfbd1d599f9a23c4d16（＝S4-a 围栏逐字节重建·§三-4 判据基数）；MARKER／两调用行后缀三 grep 各 1 坐实查三臂可过。
- 靶检自咬＝python share/check-pointers.py --target 本票面仓根相对路径 exit 0 零 BLOCK（落笔后现跑在册回执）。
- 红线申报：本席产出＝.scratch/tickets 票面一件＋.collab/receipts 回执一件＝只落盘不投递（提交权归一）；share/ 全域零字节（本票全程实读实跑只读）；三包内容零碰；.workbuddy 记忆面零碰；WTGATE 在飞面零触；git 写操作零笔（rev-parse／log／show／status／diff／ls-tree／cat-file／hash-object／check-ignore／grep 只读不禁）；git config 零写；同席多实例＝不存在（唯一架构席实例）。

（票面完——闸提速与射程治理票：提交门靶检＋全量移周期闸＋钩子动态根＋扫描域划界四子项规格齐；候裁两项单列待裁；本席起草段止于此。）

（rev 轮随注（arch-swb-gtfast-rev·2026-11-19）＝本 v2 取代 v1，改动点名处＝文首取代理由／§〇-2 归因侧重校平／§二 S1-a 保留面收窄＋A/B 复跑读数族／§三-1 造靶双口径／§三-2 子集方向／§三-3 差集账补主根 .scratch 归零项／§三-5 ANCHOR 照登数／§三-6 计数快照口径／§二 S4-a Y6 登记行／§一-1・2 声明面随 v2 与 rev 回执校平／§四-7・8 候补池随注两行；其余 v1 内容零动＝S1-b／S2 逐枚／S3／S4 逐字与钉值 02d30d01／候裁 C-1 C-2／禁动面点名照旧；rev 回执＝仓根 .collab/receipts 桶「2026-11-19-SWB-GTFAST票面rev回执-架构席-v1」件。）