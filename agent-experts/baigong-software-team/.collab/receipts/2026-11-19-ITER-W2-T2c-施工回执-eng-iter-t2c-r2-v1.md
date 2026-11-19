# ITER-W2-T2c·审法口径票·工程师席施工回执（v1）

- 席位署名＝施工＝eng-iter-t2c（BUILD 施工席·内容生产＋取证生产·席零 git 写）＋本席＝eng-iter-t2c-r2（RECEIPT 回执成文席·全窗 git 命令只读·投递归主理人统一执行＝裁决登记 c34f204e 口径·一票一新鲜实例）
- 票面＝.scratch／tickets／2026-11-19-ITER-W2-T2c-审法口径票.md（139 行·blob f283e610edfab26878843ad50faa1d3d0b2a5878·链上 23c53326）；QA 快审判词＝.collab／audits／2026-11-19-ITER-W2-T2c-QA快审判词-v1.md（76 行·blob 0739358f6ea5378e25b8abdb9e08586498c20c47·链上 da004d80）；放行登记＝.collab／decisions／2026-11-19-ITER-W2-T2c-票级放行登记-v1.md（46 行·blob 2f48e922e94a44d52fd7324e48a9dd3619eea6ff＝本席链上现算补钉·链上 817eeba5＝真位包内 decisions 桶＝T2b 真位案型同族）
- 写集恰三枚＝S1 standard-sop 卷尾部添新节一枚（append）＋S2 judgment-form-spec 判词形制真源卷新建一枚＋S3 SKILL.md 索引随动一枚；BUILD 笔＝1c772c0f6dceb518f1257b3f76a1bc3b393ee6f3（parent 3c9b9480＝他案 T2h 收口笔·COMMIT_EXIT=0 α 常态闸＝转引主理人投递窗读数）
- 体例＝照 receipt-template.md 现势（skills／sop／templates／receipt-template.md＝bb1a08d99c9eb05f6d2fda214c1301bbe979ac99／27 行七节骨架·链盘两态对钉见 §四）实占·节次按派工书 §一～§七 排布（T2h 先例同款排布）·先例取形＝T2h 回执链面 75eafc1a 面 blob 17445b60f4454662ce95601d11765a11bae9414c／83 行链上现读取形·本回执一次成文（append 不适用）·零反引号零 at·叙述裸文＋全角斜杠·命令缩进段。

## 一、开工读数（本席当轮现跑·禁抄旧数）

    date 现跑＝2026-11-19T08:32:50+08:00（施工回执成文窗）
    git rev-parse HEAD 开工首跑＝1c772c0f6dceb518f1257b3f76a1bc3b393ee6f3＝四十位对钉全等命中（＝BUILD 笔链顶现势·本窗尚无回执笔＝本件成文后由主理人投递）
    链序 git 逐笔^现跑＝1c772c0f^＝3c9b9480（T2h 收口）＋3c9b9480^＝817eeba5（T2c 放行）＋817eeba5^＝219e418d（T2h 验收判词）＋219e418d^＝da004d80（T2c 快审）＋da004d80^＝75eafc1a（T2h 回执）＋75eafc1a^＝23c53326（T2c 开票）＋23c53326^＝a099adcc（T2h 施工）＝链序 1c772c0f←3c9b9480←817eeba5←219e418d←da004d80←75eafc1a←23c53326←a099adcc 逐笔^相衔零断·与派工预期全等
    git rev-parse --git-dir 现跑＝worktree 独立 gitdir（主仓 .git／worktrees／baigong-software-team）坐实
    锁态现跑＝独立 gitdir 内 lock 族零枚＝NO_LOCK_FILES＋NO_INDEX_LOCK（ls 通配存在性现跑零命中）
    脏面现跑＝staged 零枚＋tracked M 零枚＋?? 恰一枚＝他案 T2e 票面（arch-iter-t2e 在飞·未落链·照登零触碰零带入）＋sparse skip-worktree D 态恰 1018 枚照登勿处理（git status --porcelain 现跑「 D」计数·处置归主理人投递侧沿册）
- 依据链三枚真源对钉现跑＝票面 git rev-parse 23c53326:票径＝f283e610edfab26878843ad50faa1d3d0b2a5878＋链面 wc 139 行＋盘 hash-object 现算＝同值＝链盘两态对钉 SAME；快审 rev-parse da004d80:判词径＝0739358f6ea5378e25b8abdb9e08586498c20c47／76 行＋盘对钉 SAME；放行 rev-parse 817eeba5:放行径＝2f48e922e94a44d52fd7324e48a9dd3619eea6ff／46 行（本席现算补钉）＋盘对钉 SAME。
- 竞态照登＝开工窗 ?? 面恰他案 T2e 票面一枚（在飞未落链）＝对本票链零扰；本回执全部对钉基准＝BUILD 笔 1c772c0f 及其链上各笔·不受后继笔影响（T2h 先例口径）；开工窗他案笔 T2h 收口族 3c9b9480 已落链＝^817eeba5 相衔＝无害竞态照登；收尾窗他案笔 T2e 票面笔 c9bf765b 正向落链＝^1c772c0f 父子^相衔零断·面单恰一枚对本票写集三枚前缀零命中＝零扰本票面＝开工窗 ?? 那枚转在册态（与 T2h 回执竞态正面范同形续登）。

## 二、BUILD 面单现跑＋写集三枚成对表＋投递记

- BUILD 笔面单本席现跑＝git show --name-only --numstat 1c772c0f 现跑＝恰三枚零夹带＝S1 33／0＋S2 40／0＋S3 2／1＋name-status 面＝M＋A＋M 对 S1 改／S2 新建／S3 改三型吻合；面单前缀面现跑＝三枚全落 agent-experts／baigong-software-team／声明闭集内＝零枚落主仓／share／agent-skills（cut uniq 现算）。
- 投递记转引（主理人投递窗现跑读数·标注转引不冒充本席现跑）＝COMMIT_EXIT=0 α 常态闸＋add 三 pathspec 紧邻 commit＋FX_COMMIT_DECLARE 三枚挂 commit 命令侧；本席随注复核＝BUILD 笔 message 文本 grep COMMIT_EXIT 字面零命中＝字面内嵌项纯转引·坐实面以下行为准。
- post-commit 日志行本席盘面现读坐实（非转引·日志件居 ignore 域不入链）＝.collab／evidence／hooks／post-commit.log 现读 1c772c0f 行＝2026-11-19T08:29:57 1c772c0f POST-COMMIT-PAIR PASS HEAD面单=3 声明=3＝面单与声明对等核验通过（沿 T2h 面单=5 声明=5／T2b 面单=2 声明=2 先例口径）。
- 写集三枚开工改后双 blob 双行数成对表（开工值＝本席对 parent 3c9b9480 链面现跑；改后值＝本席对 1c772c0f 链面 rev-parse 与盘 hash-object＋wc 成对现跑对钉）＝
        S1 skills／software-orchestration／references／standard-sop.md　开工 3c9b9480:面＝5d147775a205f2b60869a88f2aa09b71a28aa873／77 行（rev-parse＋show 管道 hash-object 成对全等）　→　改后 0d70601c0229f4d3ca883f0de7298447f93d3460／110 行＝链面＝盘面 SAME·numstat 33／0 删侧恰零＝纯 append 坐实＋行数账 110−77＝33 两账互算全等
        S2 skills／software-orchestration／references／judgment-form-spec.md　开工 absent 前置坐实（parent 链面 rev-parse exit 128 现跑）　→　改后 c7bfe8ded07630284e9707726c69947b45e5fceb／40 行＝链面＝盘面 SAME·numstat 40／0 全增吻合新建
        S3 skills／software-orchestration／SKILL.md　开工 3c9b9480:面＝07d0f9b67a56c3d0e1d7f1918d3d1f652f0dbd39／28 行　→　改后 176ec0dcefbec7bbff98512748b7d9ff75107d09／29 行＝链面＝盘面 SAME·numstat 2／1＝一行改一行增＝28→29 两账互算独立现算与预期全等
- S1 新节在位抽查现读＝节题「分档与审法口径（SWB 审法终态·H-2 已裁入卷）」居行 77＋五块节题行 83／89／97／101／108 全在位＝三档三制（含 J-5 归位②阈值条款行 85＝微档 ≤1 文件且改动 ≤10 行／标准档 ≤5 文件·对计划 b2de6dc8 行 32／33 现读一致）＋审法四纪律（含纪律四后口径附条「引用名必附 blob 钉值」条文成文）＋窄复核退役三件套＋用例产权四环节＋H1H2 行 22 效力段逐字引行 110 在位（引文内半斜杠全角化＝登记面口径申明在册）；逐块真源 blob＋行号附注在位抽查＝新节 28 行段内含附注行恰 10 枚现算（b2de6dc8 系八枚＋e6d3f57e 系三枚＋史案 bca59651／04f70454／319503c1 引用行）。
- S2 七节抽查现读＝节题一～七行 5／10／16／22／27／33／38 全在位；J-5 计数口径在位＝行 17 红黄入账＋绿余不入数值＋行 19 V0 不计＝三枚全中；先例判词四枚具名对钉复跑＝T2b 快审 fa1b7c4c／74 行＋T2h 快审 c55e7f90／73 行＋T2b 验收 ad8faeaa／64 行＋T2a 验收 01f0be4d／60 行＝本席 cat-file 行数现算全等；MC-PAIR-1 载体指向补钉复核＝share／check-collab-buckets.py blob e098bd5528b257ab88f5adb88c83d2bd5768ef45／312 行链面现读对钉＋判据段族行 64-129 锚行现读命中（只读指向·share 本体零触）。
- S3 索引随动现读＝judgment-form-spec 索引枚入新行在位（改后面行 28）＋standard-sop 索引行随动描述含「＋分档与审法口径（SWB 审法终态）」现读命中＋references 目录 ls 现数恰 13＝索引行现数恰 13＝对等自校随动坐实（12＋1）。

## 三、黄九枚随正落实申明逐枚（放行登记 §三＝817eeba5 面 2f48e922／46 行链上现读为据·本席链上＋盘面现跑抽查）

1. 黄-1／黄-2＝票面四词枚数自报失准＝登记勘正性质＝产出件零涉＝三枚产出件 grep 自报计数行零命中·零沿袭。
2. 黄-3 落实＝S3 落点行 18 锚现读坐实＝改后面 standard-sop 索引行＝行 18（diff 面现跑该行变更）；行 25＝handoff 索引行＝diff 面零触碰坐实＝失实锚未照用。
3. 黄-4 落实＝开工两态盘上现跑对钉非 absent 形制＝S1 开工钉 5d147775／77＋S3 开工钉 07d0f9b6／28 盘上在位现跑对钉成立＋S1／S3／check-ticket.py 三件 ls-files 旗标现跑＝H 非 S（skip-worktree 归因失实未复活）。
4. 黄-5 表头命令列漂移行不沿袭＝产出件三枚 grep「git rev-parse HEAD 现跑」「index.lock 在场」两行族各零命中。
5. 黄-6 落实＝产出件零写死取证窗名＝grep t2carch／t2cbuild／t2crec 三词对三枚产出件各零命中（现跑）。
6. 黄-7＝J-1 乙案行号勘正＝乙案已不采＝随裁消解零涉。
7. 黄-8 落实＝S2 计数口径行附采裁理由随正真源指向在位现读＝817eeba5 面 §二 J-5 行＋§三黄-8 行（真源 blob 2f48e922／46 行链面在位对钉见 §一）。
8. 黄-9 落实＝禁动五行族引导行「- 」前缀不沿袭＝三枚 diff 新增面 grep「禁动面五行族」零命中（现跑）。
9. 转写句附钉可解析性抽查现跑＝产出件全部短式钉值 git rev-parse --verify 逐枚可解析＝12／12 全通（b2de6dc8／e6d3f57e／bca59651／04f70454／319503c1／817eeba5／2f48e922／fa1b7c4c／c55e7f90／ad8faeaa／01f0be4d／e098bd55）＋转写锚逐枚现读内容对拍＝计划 v2 行 30-34／38-41／45／57-62／66／90／111 七段＋bca59651 行 76＋04f70454 行 114＋319503c1 行 29＋e6d3f57e 行 22＝逐枚命中且语义与转写句对应；引用面 blob 本体钉＋行数成对＝b2de6dc8／174 行·e6d3f57e／29 行·e098bd55／312 行 cat-file 现算全等。

## 四、禁动面两态现跑复验逐枚（链面 rev-parse vs 盘 hash-object）

- 链账 1c772c0f 面单恰三枚零夹带（§二）＋链上史件零回改＝八笔父链逐笔^相衔零断（§一）＋23c53326／da004d80 对本 HEAD merge-base --is-ancestor 现跑皆 YES（正向落链非 amend 非 rebase）。
- 依据链史件三枚零触＝票面 f283e610／139 行·快审 0739358f／76 行·放行 2f48e922／46 行＝链盘逐枚 SAME＋行数全等（§一）。
- thin 判据真源零触＝skills／software-orchestration／references／thin-ticket-template.md＝1703b61073ef4894d0abf3612d957ad439dca69f／80 行三面对钉 SAME。
- check-ticket.py 本体两态 SAME＝skills／sop／scripts／check-ticket.py＝5a9aa5fd2531ba2b5db182ba6f43958787771b39 链面＝盘面＝取证副本三面全等＋483 行。
- 五模板两态 SAME＝receipt bb1a08d9／27 行（本回执体例真源）·ticket 139d0b8b／118 行·closeout 7c14c074／57 行·return c2350972／39 行·decision-pack c7f0950e／48 行＝链盘逐枚全等。
- 席位卡五枚两态 SAME＝lead 87c493c1·architect 802b2df6·engineer 4a53bd5a·product 6ef32397·qa 58b351a5（J-4 采甲零加注核对兑现）。
- config 七 json 两态 SAME＝dispatch-spec 5ba2450f·seat-permissions-hooks-map ff8ccf6d·seat-permissions a4d02872·semantic-closed-sets da2e4869·thresholds c7bacfb9·ticket-authors 5f0bb6c4·ticket-types b4b8f23d＝链盘逐枚全等。
- .githooks 两枚两态 SAME＝post-commit 61bad3d3／pre-commit dc5b3aad。
- 三同源两态 SAME＋版本零 bump＝plugin.json 473317da·.codebuddy-plugin plugin.json a87e66e4·bundle.lock 2635ad65 链盘全等＋版本面三处现读同值 0.1.31 零 bump 坐实。
- 哈希锁两卷两态 SAME＝architecture-v2.9-copy 9a648030／176 行·product-v2.9-copy dbf49d0b／56 行。
- README 两态 SAME＝fc449fa9。
- semantic-governance.py 两态 SAME＝7cd56d09（本席复勘补钉登记）。
- share 全域两态零枚＝git status 与 git diff -- share scoped 现跑皆空输出＋BUILD 面单前缀 uniq 三枚全落包内＝diff 面与面单两面皆零。
- 主仓路径只读以外零触碰；tests／docs／.collab 三桶 scoped 现跑零枚；账本零手写·FUXI 零碰·.gitignore 零触·sparse 零处理·他案面零带入（staged 零枚）；盘落 CRLF 制式沿册＝全部对拍在剥 CR blob 面等值成立（防后续席以盘 byte 面 hash 误判漂移）。

## 五、E／V 面转引＋本席当轮复跑臂（主理人窗项转引标注不冒充）

- V5 缺省扫描本席复跑＝python3 share／check-pointers.py --root . 单跑 exit 1＝BLOCK 恰 1863／WATCH 恰 1009（严格标记行口径计数现跑）＝对在册锚全等零漂移＝本施工面零新增（本取证窗 .scratch／t2crec2／ 落 ignore 域零入 WATCH·读数落 .scratch／t2crec2／v5-pointers-rec2.txt）。
- check-pointers 三枚自靶＝转引 BUILD 笔在册读数（三枚各 exit 0 输出零行）＋本席当轮复跑＝三枚各 exit 0 输出零行现跑全等（S1／S2／S3 逐枚 --target·取证落 .scratch／t2crec2／sp-三枚）。
- check-ticket --target 三枚＝非票面不适用照登＝本席以链面只读副本复跑（盘位 share／check-ticket.py absent＝sparse 非检出面·沿 T2b 先例副本跑闸·副本 hash 5a9aa5fd 复算全等）＝各 exit 1＝BLOCK 恰 32／14／29（S1／S2／S3）＋WATCH 各零枚＝票面骨架判据对规范卷与索引卷不适配＝沿 T2h EXT 三枚不判违例先例口径·闸在岗复现＝缺节命中逐枚归因落 .scratch／t2crec2／ct-三枚（§七-2 案型）。
- V6 入线四词＝本席复跑＝三枚 diff 面合成件（仅新增行）现跑＝真源形态 0／文件域 0／席位职权 0／工序链 0＝停手闸未触发（转引 BUILD 在册读数同值全等）；S1 全件面四词 1／1／1／2 本席现算佐证＝命中行全为既有 ADR 节 T1-T4 词表行本体行 64-67＝存量面非 diff 面沿票面 §二.7 在册口径。
- E 面＝本票无独立 E 系判据枚＝E 系转引不适用照登；形制自证三面＝S1 纯 append 删侧零＋S2 absent 前置＋S3 两账互算＝本席 §二 现跑全落实。
- 验收席后续独立现跑项＝fresh QA 独立验收一枚归验收席当轮现跑（放行 §四 排程在册·本席窗不预跑不冒充）。

## 六、本笔纪律自证（RECEIPT 笔）

- 新体例申明＝席零 git 写·投递归主理人统一执行（裁决登记 c34f204e 口径）＝本席全窗 git 命令仅只读＝rev-parse／show／log／status／diff／hash-object／ls-files／ls-tree／cat-file／grep／check-ignore／merge-base／config 读＝零 add 零 commit 零 amend 零 stash 零 config 写·index 零触碰。
- 面单恰回执一枚＝本件；投递动作归主理人（add 单 pathspec 紧邻 commit＋FX_COMMIT_DECLARE 挂 commit 命令侧＝本回执仓根相对径一枚＝主理人侧执行·本席只产载体）。
- message 载体＝.scratch／t2crec2／msg-receipt.txt 落盘（单行裸文·collab: 起头·裸文＋全角斜杠·零 at 零反引号·尾标 -RECEIPT·内嵌全部关键读数）＋/tmp／t2crec2-msg-receipt.txt 备份（cp 命令参数形制见载体投递面·reapply 连带删案型防险沿册）。
- 落笔前自靶＝python3 share／check-pointers.py --root . --target 本回执实路径 exit 0 输出零行现跑（读数落 .scratch／t2crec2／selftarget-receipt.txt 随回报）＋体例三零自查现跑＝本件反引号 0／at 0＝皆零；非缩进段半斜杠面＝恰两行＝载体行 /tmp 根备份 OS 保留路径本体（与 T2h 先例回执行 71 同形同位沿册照登）＋本申明行自指命中一枚（申明行自身述及该路径＝自指沿先例口径不在禁例射程·叙述面其余非缩进段半斜杠零）；短式钉列举面＝回执登记面对钉值以八位短式列举＝先例回执同款形制＝四十位全式居写集三枚成对表与依据链三枚面（黄-7 条款射程沿 T2h 册）。
- 收尾自证＝盘现跑 git status＝staged 零枚＋tracked M 零枚＋?? 恰一枚＝本回执一枚（开工窗他案 T2e 票面已随收尾窗 c9bf765b 投递转在册态＝?? 面净＝本件一枚＝他案面零带入沿册）＋sparse D 态 1018 枚照登；HEAD 收尾复跑＝c9bf765b（他案 T2e 票面笔·^1c772c0f 相衔＝§一竞态照登）＝本回执对钉基准不受影响；取证族 .scratch／t2crec2／（v5-pointers-rec2／sp-三枚／ct-三枚／check-ticket-copy／s1-diff／s2-diff／s3-diff／s1-add／s3-add／diffplus／s1-head／s2-head／selftarget-receipt／msg-receipt 载体）居 ignore 面不入 status（取证族保留不归拆除＝reapply 防险沿册·沿 T2a／T2b／T2h 先例口径）。
- 链上后续沿放行登记＝fresh QA 独立验收一枚→产品席收口一枚（MC-PAIR-1 在判预期随收口件 +1）；本笔投后本票链为五笔（开票＋快审＋放行＋施工＋本回执）。

## 七、案型登记

1. **落位双嵌套案沿册预防零发生**＝全程写嵌套真位 agent-experts／baigong-software-team／…＝worktree 根零误建现跑坐实（包内 agent-experts 子目录不存在＝ls 零命中）。
2. **check-ticket 对规范卷／索引卷必咬＝机检分治再证**＝本票三枚各 BLOCK 32／14／29 读数＝票面闸射程不覆盖规范卷与索引卷＝沿 T2h 工单体案型同族＝本票 S1／S2 规范卷侧＋S3 索引卷侧三型全复现＝工单体／规范卷／索引卷机检缺位入候补池候选续登。
3. **semantic-governance kind 条目缺位登记面随登**＝semantic-governance.py 7cd56d09 在岗（本席只读复勘 SAME）＝对本卷类（规范卷引用面）无对应 kind 闭集条目＝登记面缺位案型随登＝产出件引用面以钉值成对形制自足（§三-9 可解析性 12／12 佐证）；claim-register 模板桶包内不在位现跑照登（真源居 agent-skills／claim-commitment-governance／templates／＝装配面非包内仓盘面）。
4. **S3 增行反引号沿索引节既有形制登记面口径**＝S3 新增两行含反引号各一＝沿索引节行 14 起表格路径列既有形制（既有行同形制现算佐证）＝S3 规格无形制条款＝沿 T2h 验收登记面口径登记不判违例；at 零／半斜杠零现跑。
5. **投递记字面内嵌 grep 零命中案型随登**＝BUILD 笔 message 文本 grep COMMIT_EXIT 字面零命中＝投递记 α 常态闸／FX_COMMIT_DECLARE 读数纯系主理人投递窗转引＝本席以 post-commit 日志 PASS 行（面单=3 声明=3）为唯一链外坐实面＝转引与坐实分面形制沿册。

模板纪律（预置申明行）＝零反引号零 at·叙述裸文＋全角斜杠·命令缩进段·append 不适用（回执一次成文）。