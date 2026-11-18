# ITER-W2-T2d-α · worktree 本地快闸票 · 工程师席施工回执（v1）

- 席位署名＝engineer 席·施工＝eng-iter-t2da（BUILD 施工席·内容生产＋取证生产·席零 git 写）＋本席＝eng-iter-t2da-r2（RECEIPT 回执成文席·全窗 git 命令只读·投递归主理人统一执行＝裁决登记 c34f204e 口径）
- 票面＝.scratch／tickets／2026-11-19-ITER-W2-T2d-alpha-worktree-local-fastgate-ticket.md（226 行·blob 6853e110c61c52e0956c46e762be53ead7659dcf·链上 1d5af22f）；QA 快审判词＝.collab／audits／2026-11-19-ITER-W2-T2d-α-QA快审判词-v1.md（67 行·blob 5984a24b9ef05a6382239107de2c471fff67a997·链上 03aedd6a）；放行登记＝.collab／decisions／2026-11-19-ITER-W2-T2d-α-票级放行登记-v1.md（33 行·blob 1db0ffe9a51e9c926c39e0f8d312532960047046·链上 92703c42·本席链上现算补钉）
- 写集恰两枚＝S1 .githooks／pre-commit 17 行＋S2 .githooks／post-commit 30 行（皆新建 verbatim 照落零改写）；BUILD 笔＝4c19642caf4008761dd4c553f44c5ffe010e59ca（parent 92703c42＝放行登记笔·COMMIT_EXIT=0 ELAPSED=350s＝旧钩子路径末段大税·ALLOW_GATE_DOWN=1 留痕在册＝转引主理人投递窗读数）
- S3 配置动作（非文件写·归主理人投递窗）已执行＝per-worktree 键 core.hooksPath 落 config.worktree＝**键漂移案新案型完整登记见 §三**（票面 §三 S3 verbatim 命令欠 --worktree 旗＝票面规格缺陷·主理人当窗纠偏＋本席三面回读复跑坐实）
- 体例＝照 receipt-template.md 现势（b6264dde／26 行·链盘双钉见 §四）七节骨架实占·节次按派工书 §一～§七 排布·本回执一次成文（append 不适用）·零反引号零 at·叙述裸文＋全角斜杠·命令缩进段。

## 一、开工读数（本席当轮现跑·禁抄旧数）

    date 现跑＝2026-11-19（施工回执成文窗）
    git rev-parse HEAD ＝ 4c19642caf4008761dd4c553f44c5ffe010e59ca＝四十位对钉全等命中（＝BUILD 笔链顶现势·零后继）
    链序 git rev-parse ^ 现跑＝4c19642ca^＝92703c4285b3dedd80acd033abeb12ce022b6601＋92703c42^＝03aedd6ac5fe2c472330c0f5edbe5d0c1d65cf3c＋03aedd6a^＝1d5af22f4fd8c814ae0496490fb3baa75bc8fa32＋1d5af22f^＝3bcb7f2b4df8aebaca5387b39a0637a3c4eb1a77＝链序 4c19642a←92703c42（放行登记）←03aedd6a（QA快审）←1d5af22f（开票）←3bcb7f2b（T1e收口）逐笔^相衔零断
    git rev-parse --git-dir 现跑＝D:／multi-agent-collab-devkits／.git／worktrees／baigong-software-team＝worktree 独立 gitdir 坐实（分支 baigong-software／main）
    锁态现跑＝worktree 独立 gitdir 内 lock 族零枚＝NO_LOCK_FILES（ls＋find 两种法现跑零命中）
    脏面现跑＝staged 零枚＋?? 零枚；tracked M 计数现跑＝1018 枚＝sparse skip-worktree D 态已知存量面（git status --porcelain 现跑 D 态恰 1018＝两口径同值）照登勿处理（处置归主理人投递侧沿册）
- 票面真源对钉现跑＝git rev-parse 1d5af22f:票面径＝6853e110c61c52e0956c46e762be53ead7659dcf＝派工钉值全等＋git show 现跑行数＝226 行＝两值对钉全等。

## 二、BUILD 面单现跑＋依据链对钉现跑

- BUILD 笔面单本席现跑＝git show --name-only --numstat 4c19642caf4008761dd4c553f44c5ffe010e59ca 现跑＝恰两枚零夹带＝post-commit A 30／0＋pre-commit A 17／0＝对票 §三 闭集两枚零越界（V3 面单核验达）。
- 投递记转引（主理人投递窗现跑读数·标注转引不冒充本席现跑）＝BUILD 笔 COMMIT_EXIT=0 ELAPSED=350s＝旧钩子路径末段大税态（α 生效前症状延续预期态）＋ALLOW_GATE_DOWN=1 留痕在册＋add 两 pathspec 紧邻 commit＋FX_COMMIT_DECLARE 两枚挂 commit 命令侧＝派工书在册。
- 写集两枚盘链双对钉本席现跑＝
        git hash-object 现算＝pre-commit dc5b3aadfbcfdf06a0bfda7584268f04733d9180＋post-commit 61bad3d3ec12ed436e62d62d0ae75b14c938d246
        git rev-parse 4c19642ca:两枚径＝同上两值＝盘 blob 与链上 blob 全等零漂移
        wc -l 现跑＝17／30 恰数＋CR 字节 grep -c 现跑两枚各 0＝LF 制式＋bash -n 现跑两枚各 exit 0
        sha256sum 现跑＝049dc02c5feffc4f400831f8dd03cc3967bacf6f47b9fb37ac4d7bbea0decacd／52f1ebbe9989d327cd08e2949fa760f7a551e524edd19c182e601c69ce10f51f＝对主理人独立复核对钉全等
- 主理人独立复核对钉（与施工席 eng-iter-t2da 回报全等·转引标注）＝verify_pair.py 独立复跑 VERBATIM_BYTE_EQUIV True×2（票面 §三 缩进段剥缩进提取与盘落两枚逐字节等值）＝本席对链上票面 blob 与盘落两枚复算 blob 全等＝verbatim 效力链上闭合间接可证（对拍程序本体在 .scratch／t2dabuild／verify_pair.py 取证面在册·本席不复跑脚本只复跑 blob 面）。
- 依据链三枚对钉现跑＝票面 6853e110… 226 行（1d5af22f·见 §一）＋放行登记链上 rev-parse 92703c42:放行径＝1db0ffe9a51e9c926c39e0f8d312532960047046／33 行（本席现算补钉·派工未给钉值如实登记）＋QA 判词 rev-parse 03aedd6a:判词径＝5984a24b9ef05a6382239107de2c471fff67a997／67 行＝对票内引值全等。

## 三、S3 键漂移案完整登记（新案型）

- 案情＝票面 §三 S3 verbatim 命令为

        git config core.hooksPath agent-experts/baigong-software-team/.githooks

  欠 --worktree 旗。票面前提「extensions.worktreeConfig=true 在位→键落 config.worktree」不成立＝该开关在位仅使 worktree 层配置**可用**，写侧仍需显式 --worktree 旗；裸设实落主仓 .git／config。
- 归因＝票面规格缺陷（照票 verbatim 执行反而错）＝非操作违票；误落窗＝约一分钟主仓钩子临时指主仓根不存在路径＝fail-open 风险窗（登记如实·窗内主仓零投递动作则实际暴露面为零＝登记风险面不冒充事故面）。
- 主理人当窗纠偏工序 verbatim（转引主理人投递窗现跑读数）＝
        ① git config --unset core.hooksPath＝UNSET_EXIT=0＋主仓 .git／config grep hookspath exit 1＝清除坐实
        ② git config --worktree core.hooksPath agent-experts/baigong-software-team/.githooks＝SET_WT_EXIT=0
        ③ 三面回读＝worktree 侧落 config.worktree＋该文件键在位＋主仓侧读空 exit 1＝主仓恢复零感知
- 本席三面回读复跑现跑＝
        git config --show-origin --get core.hooksPath 现跑＝file:D:／multi-agent-collab-devkits／.git／worktrees／baigong-software-team／config.worktree＋tab＋agent-experts／baigong-software-team／.githooks＝WT_KEY_READ_EXIT=0＝键落位坐实
        cat config.worktree 现跑＝core 段三键＝sparseCheckout／sparseCheckoutCone／hooksPath＝行 4 键在位（grep -in hookspath 现跑命中行 4 exit 0）
        git -C D:／multi-agent-collab-devkits config --get core.hooksPath 现跑 exit 1 空＝主仓键面空坐实
        grep -in hookspath 主仓 .git／config 现跑 exit 1 零命中＝误落已清坐实
- 闸链切换坐实本席现跑双仓对拍＝git rev-parse --git-path hooks＝worktree 侧＝agent-experts／baigong-software-team／.githooks／；主仓侧（-C 主仓根）＝.git／hooks／＝两仓各归其位；.githooks／ ls 现跑＝pre-commit＋post-commit 两枚在位（755·1181／2107 字节）。
- 时序硬约束合规申明＝两枚文件先投链（4c19642a）→键后设＝反序 fail-open 禁＝实际工序合约束；S3 键名大小写口径沿票面（读侧不区分·写侧标准形）。

## 四、禁动面两态现跑复验逐枚

- 主仓钩子 blob 现算对钉＝git hash-object 主仓 .git／hooks／pre-commit（只读）现跑＝8b7857701594264421832edd30dae7e401f85719＝派工钉值全等；主仓 .git／hooks／ls 现跑＝pre-commit 在位＋post-commit absent（NO_MAIN_POST_COMMIT 沿册）＋余皆 .sample 样板零触。
- share 全域两态＝主仓侧 share 域 git status 现跑＝零枚（转引标注归主理人窗主仓面复核对钉沿册）；worktree 侧本席现跑＝git diff --name-only HEAD -- share 现跑空输出＋git status 对 share／席卡／config／模板／.gitignore 域非 D 态零枚＝worktree 侧零触自证坐实。
- 席卡五枚两态现跑＝architect 802b2df6／engineer 4a53bd5a／lead 87c493c1／product 6ef32397／qa 58b351a5＝链上 rev-parse 4c19642ca:径 与盘 hash-object 逐枚全等（两态 SAME 零触）。
- config 两 json 两态现跑＝seat-permissions.json a4d02872＋dispatch-spec.json 5ba2450f＝链盘逐枚全等；其余五 json 同窗两态 SAME（thresholds／semantic-closed-sets／ticket-authors／ticket-types／seat-permissions-hooks-map 在位零触）。
- 四模板两态现跑＝ticket 677faaa5／closeout ea18b9a1／return c2350972／decision-pack c7f0950e＝链盘逐枚全等；receipt-template.md 两态＝b6264dde896f8817ccb87db04174fad690635112 链盘全等＋现跑 wc -l＝26 行＝体例真源现势坐实。
- .gitignore 两态现跑＝3a8f39c1fe608a5572b8158bef416d1fb604b027 链盘全等＝零触；evidence 桶 ignore 行现跑 check-ignore 命中 /**/.collab/evidence/＝S2 日志落位面在位零改动。
- 链上史件零回改＝本票五笔（开票 1d5af22f／快审 03aedd6a／放行 92703c42／BUILD 4c19642a／本回执待投）正向落链·父子^ 相衔零断·本席零 amend 零 rebase；账本零手写＝本席窗零触碰；FUXI 零碰；他案脏面零带入＝staged 零枚现跑；主仓路径只读查询以外零触碰。

## 五、V 系自查转标（本席可复核项现跑·主理人窗项转引标注不冒充）

- V0 开工读数＝§一（本席当轮现跑）。
- V1 靶面钉值零漂移＝本席现跑＝主仓钩子 blob 8b785770 全等＋.githooks／ 开工面已转 BUILD 后态（两枚在位＝§三 闸链对拍）＋写集两枚盘链双钉全等（§二）；check-pointers 单跑锚 1863／1009 与主仓根 run-gates 529 秒／逐闸 223s-13s-11s＝转引在册值不冒充本席现跑。
- V2 施工动作面单＝§二 verbatim 转引＋本席现跑复核＝bash -n 两枚各 exit 0／行数 17／30／CR 零枚／blob 双钉；S3 设键回读三面＝§三 本席复跑坐实。
- V3 落盘坐实＝BUILD 笔 --numstat 现跑 A 17／0＋A 30／0 恰两枚零越界（§二）。
- V4 自靶＝转引施工席读数（--target pre-commit／post-commit 各 exit 0·取证件 selftarget-pre／post.txt 在册）＋本席现跑＝--target 两枚各当窗复跑在册＋本回执落笔前自靶见 §六。
- V5＝缺省扫描全链 BLOCK 族（infra 三枚＋FX-HOOK-1 一枚）＝转引放行 §二 与 QA 快审在册值；FX-HOOK-1 查二态随 hooksPath 键在位后的语义漂移归 H-1 甲在册（不隐归 GTFAST／W2-C1 收口重定形）＝本席不复跑全链闸不冒充；本席现跑面＝自靶两枚 exit 0（V4）。
- V6 入线四词＝本席现跑对 BUILD 笔 diff 面（git show 4c19642a 加减行现取 grep 逐词）＝真源形态 0／文件域 0／席位职权 0／工序链 0＝标准档维持零升档·停手闸未触发（取证件 build-diff-lines.txt 在册）；本回执件自身词面命中＝申明面自指·沿先例口径不在 V6 射程（V6 射程＝施工笔 diff 面）·命中计数随完工回报登记。
- α 效能四判据 A-1～A-4＋对抗臂五枚＝归 fresh QA 验收席当轮现跑（本席窗不预跑不冒充）。

## 六、新体例申明＋A-1 预告＋本席纪律自证（RECEIPT 笔）

- 新体例申明＝席零 git 写·投递归主理人统一执行（裁决登记 c34f204e 口径）＝本席与施工席均只产内容与载体；本席全窗 git 命令仅只读＝rev-parse／show／log／status／diff／hash-object／ls-files／ls-tree／cat-file／config --get／--show-origin（只读查询面）。
- A-1 预告＝RECEIPT 笔投递＝core.hooksPath 键生效后的**首笔真投递**＝该笔掐表读数即 A-1 负样例样本（开工→commit 返回全程·预期量级＝worktree 根全链闸秒级基面）＝读数归主理人投递窗回填·验收归 fresh QA（≤60 秒判据）。α 后秒级对照基线＝本笔前旧钩子路径 350 秒归档值（§七-3）。
- 面单恰回执一枚＝本件；投递动作归主理人（add 单 pathspec 紧邻 commit＋FX_COMMIT_DECLARE 挂 commit 命令侧＝本回执仓根相对径一枚＝主理人侧执行·本席只产载体）。
- message 载体＝.scratch／t2darecv／msg-receipt.txt 落盘（单行裸文·collab: 起头·裸文＋全角斜杠·零 at 零反引号·尾标 -RECEIPT·内嵌全部关键读数）＋/tmp／t2darecv-msg-receipt.txt 备份（reapply 连带删案型防险沿册）。
- 落笔前自靶＝python3 share／check-pointers.py --root . --target 本回执实路径 exit 0 现跑（读数落 .scratch／t2darecv／ 随回报）。
- 收尾自证＝盘现跑 git status＝staged 零枚＋?? 恰回执一枚＋HEAD 未变复跑＋sparse D 态照登＋取证族 .scratch／t2darecv／ 居 /**/.scratch/* 排除面不可见照登；本回执零反引号零 at。

## 七、案型登记

1. **S3 键漂移案（新案型·§三 完整登记）**＝票面 verbatim 命令欠 --worktree 旗＝「开关在位→键自动落 worktree」前提不成立＝票面规格缺陷类（照票执行反而错）＝处置＝当窗纠偏三步＋三面回读＋误落窗 fail-open 风险面登记；随带口径＝「写侧旗标＝配置命令 verbatim 必查项」入候补池建议（是否落盘归收口席裁）。
2. **reapply 载体案沿册**＝取证族 .scratch／t2dabuild／／t2darev／／t2darel／ 当窗在盘照登（未遭连带删＝沿册监控）；载体 /tmp 备份例沿用防险。
3. **旧钩子末段 350 秒归档＝α 后秒级对照基线**＝BUILD 笔 ELAPSED=350s＝α 生效前旧钩子路径末段大税读数归档在册（ALLOW_GATE_DOWN=1 留痕沿册至 W2-C1／GTFAST 收口复评）；RECEIPT 笔起走 α 动态根快闸＝两态对照锚。
4. **sparse D 态 1018 枚照登续证**＝开工／收尾两态同值照登勿处理＝机理归 W2-T2d 后续段与 sparse 存量出清消费沿册。

模板纪律（预置申明行）＝零反引号零 at·叙述裸文＋全角斜杠·命令缩进段·append 不适用（回执一次成文）。
