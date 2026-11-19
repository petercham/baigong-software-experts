# workbuddy-runtime · WorkBuddy 运行时适配条款卷

> 本卷承载 WorkBuddy 运行时架构下的席位侧适配条款六目＝运行态适配面成文真源（R-1 提交权归一执行／R-2 worktree 双嵌套路径形态／R-3 sparse 与 reapply／R-4 闸临界区与临时席生命周期／R-5 两仓成对与 NOT-IN-WT-CHAIN／R-6 席零 git 写可证性上限）。效力指向＝ITER-W2-T2f 票面 §三 S1 落笔规格＋票级放行登记（真位＝agent-experts／baigong-software-team／.collab／decisions／2026-11-19-ITER-W2-T2f-票级放行登记-v1.md＝blob 860c48760de43a92c39924a30e9e39706808f66e／43 行·链面 rev-parse＝show 管道 hash＝盘 hash 三式全等现跑在册）§二 施工放行随正条款合并消费；消费来源＝裁决登记与六枚收口登记的「供 T2f 消费」宣告面（＝票面 §一 现读六面＋T2e 收口行 124 直供面＝J-1 采甲链上效力面重建）。引用即漂移＝本卷一切面值随附来源件 blob 短式＋行号，凡涉主仓值必「本链值 ‖ 主仓现势值」成对讲法·两侧各自现跑·禁凭记忆禁裸名。体例三零申明＝全卷反引号零／at 零／非缩进段半斜杠零·判定命令一律四空格缩进段·入线四词字面禁写条款在位。

卷例（固定）：每目七段制＝条款本体／适用窗／现象／机理／适配动作／判定命令／依据附钉（票面 §三 四段制「现象／机理／适配动作／判定命令」＋放行登记 §二「每目四段制＋判定命令缩进段＋依据附钉成对讲法」＋派工口径「条款本体＋适用窗」并纳＝两口径计数面全收·零空转条款）；判定命令＝席侧可现跑形制，出口可机械判；依据附钉的收口件真位皆 agent-experts／baigong-software-team／.collab／decisions／ 桶（嵌套前缀面·R-2 形态族自证）。

## R-1 提交权归一执行条款

### 条款本体

各席（工程师／QA／产品／架构）＝内容生产者＋取证生产者：写正文件落盘＋message 载体（含全部 V 系自证读数）落 .scratch＋回报交付物路径／blob／读数给主理人，全窗零 git 写操作（不 add 不 commit 不 amend 不 stash 不 reset）；主理人＝唯一链面操作员，按席回报 pathspec＋message 载体机械执行 add 单 pathspec 紧邻 commit＋FX_COMMIT_DECLARE＋-F 承载＋输出重定向，逐字誊录零改写席内容；席侧只读 git 命令不禁（开工对钉与忠实性复测所需）。

### 适用窗

一切席位窗自开工至完工全程（开票／快审／REVFIX／BUILD／RECEIPT／独立验收／收口／放行登记）；除非另有裁决对特定席解锁，本条默认全窗适用；派工书若含 git 写动作指令＝违例面，席位有权指出并请改定（请求改派不构成违例）。

### 现象

旧体例席各自 commit 案型账＝staged 悬挂五枚（席暂存未投即终结）＋残骸锁损耗约 1.2 小时＋T1d 工程师席会话超时折损两枚＋「回报自述与实态不符」案（席对 git 状态自述不可靠）＝裁决立据。

### 机理

WorkBuddy 架构下席位＝按需 spawn 临时进程，与单笔 8～10 分钟闸临界区结构性错配；同 worktree 全局 index 锁本已强制提交段串行，席各自 commit 零吞吐收益只有排队损耗——串行既不可避免，排队权归唯一常驻席为最优（裁决登记 §二 机理定性段）。

### 适配动作

1. 席侧只读 git 命令白名单族具名＝rev-parse／show／log／status／diff／hash-object／ls-tree／ls-files／cat-file／grep／numstat／merge-base／check-ignore／blame／config 读＋merge-base --is-ancestor 判定；写族（add／commit／amend／stash／reset／checkout／rebase／rm／mv／gc／clean／branch／tag／config 写）零触·index 零触碰。
2. 载体三件套＝正文件（写集落盘·嵌套真位）＋message 载体（.scratch 取证族内·collab: 起头单行裸文·全角斜杠·零反引号零 at·尾标照段别取用）＋回报读数（完工前现跑 hash-object＋wc 现算终态钉随回报面上账，禁自含面值）。
3. 尾标署名归属＝commit message 内嵌席位署名与尾标闭集（-TICKET／-BUILD／-RECEIPT／-QA-REV／-QAV／-RELEASE／-GCLOSE 照段别）；作者归属不丢＝主理人誊录不改席内容本体（零业务写红线不破）。

### 判定命令

    # 三跑形制：开工窗一次＋完工前一次对拍（期望＝两次读数对写集自洽）
    git status --porcelain | grep -cE "^[MARCDS]"        # staged 列非零枚数＝本席窗期望 0（席零 add 坐实面；" D" 列首字符空格不入本计数）
    git log --format=%s -n 30 | grep -c "零git写"        # 近 30 笔新式链面携「零git写」申明面计数＝本窗现跑 15（新体例已成链面主流口径·参考面）
    ls "$(git rev-parse --git-dir)" | grep -c "\.lock$"  # worktree 独立 gitdir 锁族＝本窗现跑 0＝NO_LOCK_FILES（判据对象＝rev-parse --git-dir 现读路径，非主仓 .git 面）

### 依据附钉

裁决登记 17add574／23 行（真位＝agent-experts／baigong-software-team／.collab／decisions／2026-11-18-提交权归一裁决登记-v1.md·盘同位可达＝本窗链面 rev-parse 全等现跑）行 9 口径段＋行 11 只读白名单段＋行 15 实证案型段＋行 16 机理定性段＋行 21 真源升级段（本卷债源宣告）；T1e 收口 04f70454／129 行行 104（新体例销账判定与上限面＝与 R-6 互指）＋行 112（新体例席窗体验·净收益面归 T2f 消费宣告）；票面 614d5031／199 行 §一 获批登记段（派工书＝裁决 c34f204e 口径）。

## R-2 worktree 双嵌套路径形态

### 条款本体

本仓 worktree 根＝包目录，git 在册真位带嵌套前缀 agent-experts／baigong-software-team／…；同仓同时存在仓根级在册目录族（.collab／.scratch／share／README 等＝包化换代前史面·sparse 部分检出态下盘不可达而链面在；公共技能族域随 ITER-W4 账本瘦转为装配消费形态＝真源归主根公共账·本仓账本不再在册该域，装配面 skills／ 下经组件行落位）——两形态并存＝必现跑判定，禁按形态直觉落位：写入前必以 git ls-files／git ls-tree 具名探查两态（仓根级＋嵌套级）后落册在真位；读取链面真位一律 git show HEAD:径 口径（盘不可达≠链面 absent）。

### 适用窗

任何席位开工对钉与落位判定前；受命产物写 .collab／docs／skills／tests 等交付面时；派工书所给路径无前缀或带前缀存疑时；.scratch 取证族落位（根级／嵌套级混写案沿册·盘落位以 ls 现跑先例为准）。

### 现象

误落位三例沿册＝派工面（T2a 案：派工书所给径于 HEAD 树 absent＝真位在另一级）／施工面（T2b 案：施工席首笔误落 worktree 根 skills／ 即归位拆净坐实·sparse D 态计数 1018 未变＝零误删）／判词面（T2d-α 案：QA 验收席判词首落仓根 .collab／audits／＝该席自查 mv 回包路径＝根 .collab／audits 已空）；同一形态族两处现身＝本仓常态风险面。

### 机理

worktree 根即包目录＝盘相对路径与 git 在册路径两态不重合（包路径前缀增减一字即两形态）；sparse 部分检出又使仓根级在册面在盘呈 D 态不可达——「盘 ls 不可达」「链面 absent」「真位在哪一级」三问必分离现跑，任何单一态不可作他态代理（引用即漂移的路径面同族）。

### 适配动作

1. 落位判定三式＝①git ls-files 具名径命中态现跑 ②git ls-tree -r HEAD 具名径命中态现跑 ③盘 ls 可达性现跑——三读数齐后落册在真位（两态皆无＝新建按写集声明径落）。
2. 误落位处置＝新建误落面 mv 回真位（照 T2d-α 先例）＋find 具名复验零残留＋随完工回报照登归因。
3. 取证族落位＝写集声明含 .scratch 族路径时照声明级落；受命文书所给临时路径与仓内落位纪律冲突时，席位有权请改定落位（临时工作物只落仓根 .scratch／ 族＝席位守则面）。
4. 全程写嵌套真位＝零误建面现跑坐实（本卷自身落位即本条款自证样本）。

### 判定命令

    git ls-files | grep -c "^agent-experts/baigong-software-team/skills/"   # 嵌套级 skills 在册枚数＝本窗现跑 43
    git ls-files | grep -c "^skills/"                                        # 仓根级 skills 族在册＝本窗现跑 0（skills 真位唯一＝嵌套级）
    git ls-tree -r HEAD --name-only | grep -c "^\.collab/decisions"         # 仓根级 decisions 链在册＝本窗现跑 159（sparse 未检出 D 态面）
    git ls-tree -r HEAD --name-only | grep -c "^agent-experts/baigong-software-team/.collab/decisions"   # 嵌套级 decisions＝本窗现跑 46（收口件桶）
    # 落位判定单件形制（替换具名径现跑）：
    git ls-files agent-experts/baigong-software-team/skills/software-orchestration/SKILL.md | wc -l      # =1＝嵌套级在册坐实

### 依据附钉

T2a 收口 42a3db47／145 行行 74（派工面侧误落位案＋供 T2f 消费宣告）；T2b 收口 21d1fccc／140 行行 73（施工面误落位＋归位拆净坐实）；T2d-α 收口 97cfda37／140 行行 69（判词面误落位＋根 evidence 副产物照登）＋行 126（双嵌套形态族两处现身宣告）；本窗判定命令五枚读数即现势成对样本。

## R-3 sparse skip-worktree 与 reapply

### 条款本体

sparse 未检出 D 态＝本链已知存量面（本窗现跑恰 1018 枚）＝照登勿处理：不判脏面违例、不判误删、席位不得自行 checkout／restore／reapply 处置；若 sparse 位翻转（D 态计数对开工基线异动）＝主理人 sparse-checkout reapply 机械复原后席位继续施工，勿阻塞请示；reapply 有连带删 untracked 取证族风险＝取证族效力面双保险口径写死＝盘核验（便捷面）＋链上 message 内嵌读数（持久面）——取证族内容效力以链上面闭合，盘面被连带清除不构成效力损失。

### 适用窗

开工读数脏面计数分解现跑时；完工回报照登时；.scratch 取证族对账时发现族失踪；V0／V5 面任何涉及 status 计数的判据消费时。

### 现象

位翻转案型第三例在册（快审窗 1018 行 D 态·主理人 reapply 复原＋验收窗同型）；reapply 连带删 untracked 取证族续证＝四族出盘（.scratch 下 t1dbuild／t1dbuild2／t1drecv3／t1dacc 四族盘不可达＝链上 message 内嵌读数面闭合其效力）；同案型波及候选＝WorkBuddy 适配条款收集清单九枚两态 absent（链面具名仅登记引用行命中零本体＋盘 find 零枚＝归主理人侧复原）。

### 机理

cone-mode sparse 检出范围外索引位在 worktree 不物化＝status 报工作树列 D（索引在·盘不在＝非删除事件）；reapply 重建工作树时 untracked／ignore 域文件（取证族居之）可能被连带清掉——故取证族不得以盘态为唯一效力面（假完成案型的取证面防线同源）。

### 适配动作

1. D 态计数现跑形制入开工与完工两次回报（计数命令见判定命令；对开工基线只平即绿，异动＝报归因候主理人 reapply）。
2. sparse 零处理＝纪律自证段固定项（席位不 flip 位、不 reapply、不 restore）。
3. 取证族双保险＝关键读数一律内嵌 message 载体（单行裸文内嵌＝链上持久）；.scratch 副本用毕即拆或照登保留皆可，效力不依赖其存活。
4. 他案 ?? 群与本案取证族照登零带入（投递侧卷入防线归主理人 post-commit 面单核验）。

### 判定命令

    git status --porcelain | grep -c "^ D"     # 本链现值＝本窗现跑 1018（存量基线面；开工／完工两跑对拍＝平即绿）
    git status --porcelain | grep "^ D" | sed "s/^ D //" | cut -d/ -f1-2 | sort | uniq -c | sort -rn | head -5   # D 态归因抽样＝最大簇＝仓根 .collab/decisions 族（全部落 sparse 未检出区＝非误删；公共技能族域随 ITER-W4 账本瘦转为装配消费形态＝真源归主根公共账·本仓账本摘跟踪该域后 D 态归因分布随摘跟踪段现跑更新）
    git config --get core.sparseCheckout       # 本链现读＝true（主仓侧成对＝本链 true ‖ 主仓未设该键＝主仓 status D 态现跑 0 枚）
    git sparse-checkout list | head -3         # cone 范围列示现读（范围外即 D 态来源区）

### 依据附钉

T1d 收口 bca59651／126 行行 67（位翻转案型＋reapply 连带删取证族续证＋收集清单波及宣告·供 T2f 消费）；裁决登记 17add574／23 行行 21（收集清单「reapply 连带删后主理人已复原」句）；D 态计数成对＝本链 1018 ‖ 主仓现势 0 枚（主仓侧 status --porcelain 现跑·只读）。

## R-4 闸临界区×临时席生命周期错配

### 条款本体

提交段串行归一主理人（见 R-1·非并行化问题而是生命周期问题）；席侧零 commit 等待＝席位生命周期全部用于内容生产与取证；α 钩子键（本链 core.hooksPath 现读在位）生效后投递窗全链秒级（10s／9s 两笔实测在册）＝席侧零闸等待；超时 SIGTERM 残骸锁（index.lock／next-index-PID.lock 族）不再生产于席侧＝存量残骸只照登零处理，删锁权归主理人（实证陈旧按先例删锁留证）。

### 适用窗

席位窗时间预算与超时防线设定；撞锁两态处置时；回执与回报面的锁面／闸面读数消费时；残骸锁出现在任一 gitdir 侧时。

### 现象

旧体例席前台 commit 被超时 SIGTERM 砍死留 index.lock／next-index-PID.lock 残骸＝损耗约 1.2 小时在册；T1d 三席接力案型＝提交窗占临时席生命周期大头；新体例席窗体验反证＝席窗零 commit 等待／零撞锁／零会话超时折损（T1e 收口行 112）；α 键生效后投递窗全链秒级＝10s／9s 两笔实测（T2d-α 收口行 123）；主仓常见目录侧 next-index 前缀残骸锁三十枚 mtime 全早于验收窗＝案型在册只读零处理（复审签登记-丙形制）。

### 机理

席位＝按需 spawn 临时进程，与单笔 8～10 分钟闸临界区结构性错配＝席内提交＝把生命周期最贵资源（会话窗）烧在排队与闸上；同 worktree 全局 index 锁本已强制提交段串行＝席侧并行 commit 无吞吐收益；α 钩子键（core.hooksPath 指向包内 .githooks）生效＋投递归一后＝闸临界区移出席窗、投递窗压缩至秒级＝错配消解。

### 适配动作

1. 席侧零 commit 等待＝时间预算全给内容生产＋取证，不为提交段与闸段留预算；commit 类长命令的 timeout 防线设定归主理人窗（落链硬口径＝-F 承载＋输出重定向＋后台执行）。
2. 撞锁两态口径＝lock 在飞等待自然消退（不删不自助）；实证陈旧＝呈主理人按先例删锁留证；席位不删任何锁。
3. 残骸锁只照登零处理＝登记进回报面（含主仓侧只读照登＝成对讲法＝本链 gitdir 枚数 ‖ 主仓 gitdir 枚数）；NO_LOCK_FILES 判据对象＝rev-parse --git-dir 现读路径（worktree 独立 gitdir 口径申明），不是主仓 .git 面。

### 判定命令

    ls "$(git rev-parse --git-dir)" | grep -c "\.lock$"        # 本链独立 gitdir 锁枚数＝本窗现跑 0＝NO_LOCK_FILES
    git config --get core.hooksPath                            # 本链现读＝agent-experts／baigong-software-team／.githooks 值面在位（α 键在岗）‖ 主仓侧成对＝git -C 主仓根 config --get core.hooksPath 现跑 exit 1 空＝主仓键面空
    ls "$(git -C /d/multi-agent-collab-devkits rev-parse --git-common-dir)" | grep -c "next-index.*\.lock$"   # 主仓侧残骸只读照登＝本窗现跑 30 枚（mtime 抽样全早于本窗＝陈旧残骸归主理人删锁权）
    git log --format=%aI -n 2 | head -2                        # 链顶两笔 author date 现读＝投递窗节奏参考面（秒级投递沿册＝登记文读数，非本命令判定项）

### 依据附钉

裁决登记 17add574／23 行行 15（残骸锁损耗实证）＋行 16（机理定性）；T1e 收口 04f70454／129 行行 112（席窗体验净收益面归 T2f 消费）；T2d-α 收口 97cfda37／140 行行 123（α 落地体验＝秒级＝归 T2f 消费）；复审签（票面复审签 v1＝真位 agent-experts／baigong-software-team／.collab／audits／ 桶·blob 25b1da6f／95 行）登记-丙（主仓侧残骸锁三十枚照登形制）；成对值＝本链锁 0 枚 ‖ 主仓侧 30 枚（本窗两侧现跑）。

## R-5 两仓成对与 NOT-IN-WT-CHAIN

### 条款本体

本链（worktree 链＝分支 baigong-software／main）与主仓（main 链）＝同库两链面两仓面；凡消费跨仓值（share 闸族钉值／工具面行数／链顶／钩子键态）一律「本链值 ‖ 主仓现势值」成对讲法＝两侧各自现跑（主仓侧＝git -C 主仓根只读查询·主仓零触碰）·面值并列入册·禁凭记忆禁单侧断言；他域改动是否入本链＝git merge-base --is-ancestor 他域笔对 HEAD 机械判据＝exit 1 报 NOT-IN-WT-CHAIN＝未入本 worktree 链＝消费面如实登记不冒充已生效；他域改动向我方知会＝知会登记台账入账路径（三行形制首样沿册）。

### 适用窗

两仓成对读数口径出现时（share 闸族／门禁脚本／钩子键面）；脏面与残骸归因时；V 系验收面复跑他域笔判据时；收口与放行登记消费他域钉值时。

### 现象

share 闸族两侧已分叉三枚在册（check-pointers 本链 33781b31／551 ‖ 主仓 d5e2cfe2／552；check-collab-buckets 本链 e098bd55／312 ‖ 主仓 922fe2e9／169；check-hook-health 本链 b778dc75／165 ‖ 主仓 1df6ea44／182＝两侧全漂移属实＝G7 定版知会单入账）；GTFAST 案五笔＋R0／WTGATE 后续笔对本链 HEAD merge-base 各报 NOT-IN-WT-CHAIN＝主仓链面新笔零归我方本窗；本包 check-ticket 料源定版＝唯一料源本体落本包 scripts 桶（定版条款沿册）。

### 机理

worktree 与主仓共享 gitdir 对象库但各持链 HEAD（本链 baigong-software／main ‖ 主仓 main＝两链分叉）；merge-base --is-ancestor 为纯祖先机械判据（exit 0 在链／exit 1 不在链）＝NOT-IN-WT-CHAIN 可核不靠转述；对象库共享＝主仓侧 blob 在本链可 --verify 解析（钉值可解析 ≠ 笔入本链＝两判据勿混）；同一修复禁两侧重复维护＝钉值随动对账备案形制（FX-HOOK-1 旧钉作废登记＋新钉现势登记）。

### 适配动作

1. 成对讲法形制＝来源面值（派工书／登记文转引）‖ 现势值（本窗缩进段命令现跑）并列写死；主仓侧取值＝只读命令族经 git -C 现跑·主仓写零触。
2. NOT-IN-WT-CHAIN 判据命令入各席 V 面（对知会单／登记文内他域笔 sha 具名现跑 merge-base）。
3. 他域改动入账＝知会登记台账三行形制（日期／来源单／我方响应面）＝入账路径直接取用。
4. 禁冒充已生效＝主仓侧已改＝本链消费面仍按本链钉值行事，直至汇链拍；我域侧随动账（如钩子钉值）另立登记面。

### 判定命令

    git merge-base --is-ancestor 335dbbe86a63a98d19a1bdfbdeac3533ff5ae71d HEAD; echo exit=$?    # 他域笔样例（主仓侧历史 HEAD 值）对 HEAD＝本窗现跑 exit 1＝NOT-IN-WT-CHAIN 复现
    git rev-parse HEAD                                                        # 本链链顶四十位现读
    git -C /d/multi-agent-collab-devkits rev-parse HEAD                       # 主仓链顶四十位现读（成对另一侧·只读）
    git rev-parse HEAD:share/check-pointers.py; git -C /d/multi-agent-collab-devkits rev-parse HEAD:share/check-pointers.py   # 分叉例成对现跑＝本链 33781b31 开头 ‖ 主仓 d5e2cfe2 开头
    git rev-parse --verify d5e2cfe2 | cut -c1-12                              # 对象库共享面＝主仓 blob 本链可解析（可解析≠在链·两判据分离坐实）

### 依据附钉

T2h 收口 7f889958／142 行行 125（知会登记台账三行首样＝NOT-IN-WT-CHAIN 判据机械可核＝供 T2f 运行时适配面消费）；T2d-α 收口 97cfda37／140 行行 52（GTFAST／WTGATE 笔 merge-base NOT-IN-WT-CHAIN 消费面如实登记）＋行 58（主仓侧零感知成对形制）；EXT-2026-11-19-T2e-G7 三工具归属定版知会单（真位＝同 decisions 桶·具名可查）三枚两侧分叉成对值；本窗四成对现跑＝链顶（241f71d5 开头 ‖ dbd144ae 开头）／check-pointers（33781b31 ‖ d5e2cfe2）／check-collab-buckets（e098bd55 ‖ 922fe2e9）／hooksPath（在位 ‖ exit 1 空）。

## R-6 席零 git 写可证性上限

### 条款本体

「席零 git 写」＝间接可证口径写死·无直接机械证＝上限登记面：git 历史无原生记录能力（记录结果对象不记录命令过程）＝任何「本席窗未执行 git 写」断言不可由链上史直接证伪或证实；席侧自证形制＝回报面纪律自证段＝闭集枚举全窗实读只读命令族＋唯一写清单＋index 零触碰＋锁面零现值，逐断言附现跑读数；机械面只存在两型＝事前写侧租约拦截（越界写被拒＝管路径不管命令种类）与事后账本互验（结果面不污染＝必要非充分）；不得把任一机械面宣称成「零 git 写」的直接证。

### 适用窗

完工回执与回报面纪律自证段填写时；QA 验收「零 git 写」断言判定面；本条款晋升门禁评估面（收口判据处置三态列）；候补池对账时（本枚＝已成文态）。

### 现象

T1e 收口销账目原文摘录＝「成立（间接可证·如实申明无直接机械证）」；同枚上限登记面（git 历史无原生记录能力）＝候补池去向＝WorkBuddy 运行时适配票 T2f 消费＝本目成文后该候补转「已成文」态。

### 机理

git 的可审计面＝提交对象／reflog／锁面／index 态＝全是结果面；命令过程不留痕＝过程断言（谁在窗内跑过什么）缺史锚；结果面干净（无新笔／无 staged／无锁／index 零触碰可由 status 与 ls 间接侧证）与过程干净之间隔不可闭合的推理缺口＝如实申报优于过度宣称（回报自述与实态不符案反向印证自述面必须配现跑读数）。

### 适配动作

1. 纪律自证段闭集枚举形制＝只读命令族实读具名（rev-parse／show／log／status／diff／hash-object／ls-tree／ls-files／cat-file／grep／numstat／merge-base／check-ignore／config 读）＋写集枚数具名＋index 零触碰＋sparse 零处理＋他案面零带入，一段入 message 载体随链持久。
2. 断言配读数形制＝每个「零」断言挂一条当窗现跑命令（staged 列零枚／锁零枚／链顶开工完工同值）＝效力面＝链上 message（R-3 双保险同源）。
3. QA 消费口径＝判绿以间接证链完整（开工竞态防呆＋改前改后两账互算＋scoped 面单零夹带＋锁面读数）为准，不要求直接机械证＝验收判据不悬空。
4. 晋升门禁＝如需过程级审计（钩子侧命令审计）＝WorkBuddy 平台侧行为本体＝非我域可改对象＝登记不实现（EXT 不出同案型＝无领办域可指）；条款卷判定命令族若晋升挂 run-gates＝归收口判据处置三态列裁面。

### 判定命令

    git rev-parse HEAD                                   # 开工对钉值与完工复跑同值＝本席窗零链面推进坐实面（投递归主理人）
    git status --porcelain | grep -cE "^[MARCDS]"        # staged 列非空格首字符枚数＝开工／完工两跑均 0＝零 add 间接证
    git log --format=%h -n 5                             # 近五笔链面具名现读＝开工链顶仍在位＝零扰动参考面

### 依据附钉

T1e 收口 04f70454／129 行行 104（销账判定原文摘录＋上限登记面＋候补池去向＝T2f 消费宣告）＋行 112（新体例运行面＝本卷 R-1／R-4 同枚来源）；裁决登记 17add574／23 行行 9（新体例本体）＋行 11（只读白名单）；票面 614d5031／199 行 §七 候补池去向句（R-6 可证性上限＝候补随 S1 落链转已成文态）。

## 尾注·随动与消费面（固定）

1. 本卷＝条款真源＝索引行只指向不复制（software-orchestration／SKILL.md references 索引节一行＝J-3 甲同款单真源口径）；席位卡随动核对归后续票裁面（票面 §三 席位卡零触申明）。
2. 本卷内全部八位短式钉值可解析性＝git rev-parse --verify 逐枚现跑全通归验收复跑面；凡引用即漂移＝下游消费必现跑复核。
3. 本卷判定命令族的晋升（挂 run-gates／入门禁库）＝收口判据处置三态列裁面归产品席收口窗＝非本卷预设。
4. 行数＝wc 现算入回执（沿册口径·卷内不写死面值）。