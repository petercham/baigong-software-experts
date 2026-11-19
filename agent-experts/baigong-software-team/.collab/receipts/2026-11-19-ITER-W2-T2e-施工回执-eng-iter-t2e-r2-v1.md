# ITER-W2-T2e·tests 接线与工具归属定版票·工程师席施工回执（v1）

- 席位署名＝施工＝eng-iter-t2e（BUILD 施工席·内容生产＋取证生产·席零 git 写）＋本席＝eng-iter-t2e-r2（RECEIPT 回执成文席·全窗 git 命令只读·投递归主理人统一执行＝裁决登记 c34f204e 口径·一票一新鲜实例）
- 票面＝.scratch／tickets／2026-11-19-ITER-W2-T2e-tests接线与工具归属定版票.md（179 行·blob 1c52febbbecf5fcff851ffca1fbab17e6cce5485·链上 c9bf765b）；QA 快审判词＝.collab／audits／2026-11-19-ITER-W2-T2e-QA快审判词-v1.md（80 行·blob 773e05741e5ee924eaba4b3d03eb9e1b652efd8a·链上 036bad68）；放行登记＝.collab／decisions／2026-11-19-ITER-W2-T2e-票级放行登记-v1.md（本席链盘现跑＝blob dcbb9d4a0e16193007d1d2aaa7138bc913d3d0a9／45 行·链上 0663312f·转引面值 46 行与本席现跑 45 行差一行＝一行级转引漂移案型同族登记见 §七-5）
- 写集恰四枚＝S1 tests／run-all.sh 入口件新建一枚＋S2 skills／sop／SKILL.md 定版两行一枚＋S3 .collab／decisions／EXT-2026-11-19-T2e-G7三工具归属定版知会单-v1.md 新建一枚＋S4 skills／sop／references／external-ticket-spec.md 卷尾台账 append 一枚；BUILD 笔＝b0870455d131bf41c0bd5e8d958e69768aca324a（parent 9e76d08f＝他案 T2c 收口笔·COMMIT_EXIT=0 α 常态闸＝转引主理人投递窗读数）
- 体例＝照 receipt-template 现势（skills／sop／templates／receipt-template.md＝bb1a08d99c9eb05f6d2fda214c1301bbe979ac99／27 行·本席三面对钉现跑＝链 rev-parse＝show 管道 hash-object＝盘 hash-object 三面全等）实占·先例取形＝T2c 回执链面 3bdabc89 面 blob 0840733aa90d8de28cdc447db12150556cf76ba5／86 行链上现读取形（show 管道 hash＋wc 现跑对钉）·本回执一次成文（append 不适用）·零反引号零 at·叙述裸文＋全角斜杠·命令缩进段。

## 一、开工读数（本席当轮现跑·禁抄旧数）

    date 现跑＝2026-11-19T10:25:36+08:00（施工回执成文窗）
    git rev-parse HEAD 开工首跑＝b0870455d131bf41c0bd5e8d958e69768aca324a＝四十位对钉全等命中（＝T2e BUILD 笔链顶现势·本窗尚无回执笔＝本件成文后由主理人投递）
    链序 git 逐笔^现跑＝b0870455^＝9e76d08f（他案 T2c 收口）＋9e76d08f^＝cd837ced（他案 T2c 验收）＋cd837ced^＝0663312f（T2e 放行）＋0663312f^＝036bad68（T2e 快审）＋036bad68^＝3bdabc89（他案 T2c 回执）＋3bdabc89^＝c9bf765b（T2e 开票）＋c9bf765b^＝1c772c0f（他案 T2c 施工）＝链序 b0870455←9e76d08f←cd837ced←0663312f←036bad68←3bdabc89←c9bf765b←1c772c0f 逐笔^相衔零断；八枚集合与派工预期全等·唯面值相邻两枚（c9bf765b／3bdabc89）顺序误抄＝面值链序误抄案型沿册（BUILD 笔在册同款）·机械现读为是
    git rev-parse --git-dir 现跑＝worktree 独立 gitdir（主仓 .git／worktrees／baigong-software-team）坐实
    锁态现跑＝独立 gitdir 内 lock 族零枚＝NO_LOCK_FILES＋NO_INDEX_LOCK（ls 通配现跑计数 0）
    脏面现跑＝staged 零枚＋tracked M 零枚＋?? 零枚（他案 T2c／T2e 在飞面均已随各自笔落链转在册态＝开工窗无在飞活体照登）＋sparse skip-worktree D 态恰 1018 枚照登勿处理（git status --porcelain 现跑「 D」计数·处置归主理人投递侧沿册）
- 依据链三枚真源对钉现跑＝票面 git rev-parse c9bf765b:票径＝1c52febbbecf5fcff851ffca1fbab17e6cce5485＋show 管道 wc 179 行全等；快审 rev-parse 036bad68:判词径＝773e05741e5ee924eaba4b3d03eb9e1b652efd8a／80 行全等；放行 rev-parse 0663312f:放行径＝dcbb9d4a0e16193007d1d2aaa7138bc913d3d0a9／45 行（show 管道 wc＝grep 计数＝盘 wc 三口径互算全等·盘 hash-object 成对全等）＝链盘两态对钉 SAME·行数对转引面值 46 差一行登记 §七-5。
- 竞态照登＝作业窗他案两笔已落链＝cd837ced（T2c 验收判词笔）＋9e76d08f（T2c 收口笔）＝^相衔现读零断＝无害竞态照登（T2h／T2c 先例口径）；本回执全部对钉基准＝BUILD 笔 b0870455 及其链上各笔·不受后继笔影响。

## 二、BUILD 面单现跑＋写集四枚成对表＋投递记＋drill-05 候裁面

- BUILD 笔面单本席现跑＝git show --name-only --numstat b0870455 现跑＝恰四枚零夹带＝S1 43／0＋S2 2／0＋S3 58／0＋S4 5／0（删侧四枚皆零＝新建与纯 append 两型吻合）；面单前缀面现跑＝四枚全落 agent-experts／baigong-software-team／声明闭集内＝零枚落主仓／share／agent-skills。
- 投递记转引（主理人投递窗读数·标注转引不冒充本席现跑）＝COMMIT_EXIT=0 α 常态闸＋add 四 pathspec 紧邻 commit＋FX_COMMIT_DECLARE 四枚挂 commit 命令侧。
- post-commit 日志行本席盘面现读坐实（非转引·日志件居 ignore 域不入链）＝.collab／evidence／hooks／post-commit.log 现读 b0870455 行＝2026-11-19T10:23:10 b0870455 POST-COMMIT-PAIR PASS HEAD面单=4 声明=4＝面单与声明对等核验通过（沿 T2c 面单=3 声明=3 先例口径）。
- 写集四枚开工改后双 blob 双行数成对表（开工值＝本席对 parent 9e76d08f 链面现跑；改后值＝本席对 b0870455 链面 rev-parse 与盘 hash-object＋wc 成对现跑对钉）＝
        S1 agent-experts／baigong-software-team／tests／run-all.sh　开工两态 absent 前置坐实＝转引 BUILD 席现跑（链面 ls-tree 具名零行＋盘 ls 不可达）　→　改后 1d5f9aeb953c4de12835ae42422be0fcafcd8e03／43 行＝链面＝盘面 SAME·numstat 43／0 全增吻合新建
        S2 agent-experts／baigong-software-team／skills／sop／SKILL.md　开工 9e76d08f:面＝fe3977d3e3ef9f5877e14ae8998f6dd5242178c3／38 行（rev-parse＋show 管道 hash-object＋show 管道 wc 三面全等）　→　改后 d76785e223311a823d6a29b981530e689cb8f846／40 行＝链面＝盘面 SAME·numstat 2／0＝38→40 两账互算全等
        S3 agent-experts／baigong-software-team／.collab／decisions／EXT-2026-11-19-T2e-G7三工具归属定版知会单-v1.md　开工两态 absent 坐实＝转引 BUILD 席现跑　→　改后 c5c1f79aa9882d096fea410ab52ab9cb82130638／58 行＝链面＝盘面 SAME·numstat 58／0 全增吻合新建
        S4 agent-experts／baigong-software-team／skills／sop／references／external-ticket-spec.md　开工 9e76d08f:面＝208fbf0bfa2b9e2ceabe47b4f2470c06101f9f6c／104 行　→　改后 e8986941307b2b8abd9d0e82a25a1f4507191733／109 行＝链面＝盘面 SAME·numstat 5／0＝104→109 两账互算全等＝append 正文零回改坐实＝parent 面 diff 删侧恰 0 行本席现跑
- S1 内容抽查现跑＝头注四行族全在位（用途行 2＋声明行 3＋运行窗两态行 4＋族名行 5）＋「纯标准库零第三方依赖」声明 grep 恰 1 现跑（计划 v2 行 123 逐字本体在位）＋黄-6 乙案 probes 跳跑申明在位现读＝头注行 6-9 原因申明＋执行序行 36-38 跳跑申明行在输出面。
- S3 内容抽查现跑＝八字段节题 grep 现数恰 8（字段一至八行 5／11／16／24／30／42／49／55）＋效力域声明五行现数恰 5（行 18-22）＋黄-5 改后形制在位现读命中＝行 26「MC-PAIR-1 配对段＝本链已施（T1c BUILD 笔 2d90ccb50fdb0f34f54cd9d90d1776ab07cfbdbe）‖ 主仓未含桶名闭闸扩展（主仓唯一笔 f530859c5fc8ab1afc927c9392b8a570f446b3dd＝MC-BUCKET-1 本体）」＋行 35 成对枚数「MC-PAIR-1 本链 6‖主仓 0＋CLOSEOUT_NAME_RE 本链 2‖主仓 0」＋四闸八值成对在位抽查＝行 26 check-pointers 33781b312e7029a02ec05626121bcf12c78d7276／551‖d5e2cfe2c831dc100d4c8ea523e763422445af4e／552 等命中＋四十位面现跑＝出现 35 枚·去重 26 枚·cat-file 可解析 26／26 零悬空＋裸八位零枚（E1 口径复算·对转引面值 35 枚全配对吻合）。
- S4 内容抽查现跑＝卷尾 rev-1 段五枚行在位（段题行＋空行＋§四.3 表头两行照录＋台账一行）＋台账行对 S3 件名逐字对号 grep 恰 1 现跑＋「（模板尾·固定形制）」行原位零动现读（黄-3 不沿袭缺模板尾行形制坐实）。
- drill-05 候裁面（本席独立复跑坐实·随正条款形制入回执＋验收呈请引用）＝
        S1 实效现跑＝worktree 根窗 bash tests／run-all.sh＝exit 1＝末行 RUN_ALL_RED red_chain=acceptance／drill-runner.sh green=5／6（六段＝py 五枚全 GREEN＋drill-runner 段 RED·逐段具名读数在册）
        drill-05 独立复跑（T06_TMP 注入式）＝exit 1＝RED 行＝「deny 原因非 freeze 联动」复现；drill-01 至 04 GREEN＋drill-06 注入窗独立复跑 GREEN（DRILL06_GREEN exit 0）＝红项仅此一枚坐实
        归因本席现读＝drill-05 行 55 grep 判据「B10 freeze 态全写 deny」为明文 vs write-guard.py 行 240 ensure_ascii=True（deny 输出面中文字面转义·行 117／142 皆 False 唯行 240 True 现读钉位）自 TK-GWP 笔 5b8936e7163024b7965d8816a35f3b6d6be5f018（链上 subject 现读对号＝守卫装配缺陷整改批）起必失配＝存量漂移非本笔所致
        先证链上现读＝QA 审票笔 93434e052d491768f3380cd671917ea25f45be48 subject 内嵌「drill05-06 开工基线即红未钉（编码不匹配＋夹具缺目标件，b8bdadc 既有）」命中
        主理人裁口径沿册＝存量红非本笔所致·E5 前置「零红态现势」面值失实案型「前置现势面值必现跑」·修 drill 触 tests 28 枚禁动面／修 write-guard 触禁动面＝两路皆不可修＝如实申报随候裁面（放行 §三黄-6 口径·三案落定值随 numstat 实测照登）
- probes 零扰动坐实复跑＝tests／probes／results／probe-results.json 盘 hash-object 现跑 acf3bbc752539a0c30eba8ae499e90516605c0e4 对转引面值全等＋mtime 现跑 1794981576 对转引面值全等＋tests 域 scoped status 现跑零枚（run-all.sh 已随 BUILD 笔落链转在册态）＋既有面 diff 现跑零枚＝跳跑申明生效坐实。

## 三、黄七枚随正落实申明逐枚（放行登记 §三＝0663312f 面 dcbb9d4a／45 行链上现读为据·本席链上＋盘面现跑抽查）

1. 黄-1 落实＝EXT 件引文取 T2h 收口行 126 口径＝S3 行 47「成文依据引文＝T2h 收口登记 blob 7f889958182c0d195f9ce4857472506ebb41973f／142 行 行 126 现读」命中现跑＋链上 git show 7f889958 行 126 现读＝「③工单体形制四件套已可复用」起句逐字命中＝行 124 同款挂账句成对沿册。
2. 黄-2 落实＝产出件零沿袭「不受域闸」措辞＝四枚产出件 grep 现跑各 0（S1 0／S2 0／S3 0／S4 0）。
3. 黄-3 落实＝产出件不沿袭缺模板尾行形制＝S3 EXT＝八字段形制（无模板尾行位＝形制适用面登记）＋S4 规范卷「（模板尾·固定形制）」行原位零动现读（§二 S4 抽查在册）。
4. 黄-4 两态口径落实＝check-ticket --target EXT 面两态本席复跑＝缺省态 exit 1＝BLOCK 恰 14／WATCH 恰 0＋--since 2026-11-19 强制入域态 exit 1＝BLOCK 恰 14／WATCH 恰 0（工具结论行现读两态全等）＝票面骨架判据对工单体不适配＝T2h EXT 先例 14 枚同形＝分治案型沿册（放行 §一读数对票面＝本两态读数对 EXT 产出面如实照登）。
5. 黄-5 落实＝改后形制全线在位现读命中＝S3 字段四 R-1（行 26）＋字段五（行 35）＋S4 台账行三处成对讲法全线（抽查读数见 §二 S3／S4 段）。
6. 黄-6 落实＝乙案落笔坐实＝跳跑申明行在位现读（§二 S1 段）＋实效读数随面单照登候裁面（§二 drill-05 段）。
7. 黄-7 抽查＝thin 行 5 verbatim 现读在位（thin 1703b610／80 行行 5「使用说明（固定）…」命中）＋本四枚产出件使用说明行位＝S3 EXT grep 0 现跑＝T2h EXT 先例三枚（e5ead96d／b68fc823／5a2a0ccd 件面 grep 各 0 现跑）同形＝不适用照登登记面口径沿册（S1＝shell 头注形制·S2／S4＝索引与台账位）。

## 四、禁动面两态现跑复验逐枚（链面 rev-parse vs 盘 hash-object）

- 链账 b0870455 面单恰四枚零夹带（§二）＋链上史件零回改＝八笔父链逐笔^相衔零断（§一）＋c9bf765b／0663312f 对本 HEAD merge-base --is-ancestor 现跑皆 YES（正向落链非 amend 非 rebase）。
- thin 判据真源零触＝skills／software-orchestration／references／thin-ticket-template.md＝1703b61073ef4894d0abf3612d957ad439dca69f／80 行两态对钉 SAME。
- check-ticket.py 本体两态 SAME＝skills／sop／scripts／check-ticket.py＝5a9aa5fd2531ba2b5db182ba6f43958787771b39 链面＝盘面。
- 五模板两态 SAME＝receipt bb1a08d9／27 行（本回执体例真源）·ticket 139d0b8b／118 行·closeout 7c14c074／57 行·return c2350972／39 行·decision-pack c7f0950e／48 行＝链盘逐枚全等。
- 席位卡五枚两态 SAME＝lead 87c493c1·architect 802b2df6·engineer 4a53bd5a·product 6ef32397·qa 58b351a5（链盘逐枚现跑全等）。
- config 七 json 两态 SAME＝dispatch-spec 5ba2450f·seat-permissions-hooks-map ff8ccf6d·seat-permissions a4d02872·semantic-closed-sets da2e4869·thresholds c7bacfb9·ticket-authors 5f0bb6c4·ticket-types b4b8f23d＝链盘逐枚全等。
- .githooks 两枚两态 SAME＝post-commit 61bad3d3／pre-commit dc5b3aad。
- 三同源两态 SAME＋版本零 bump＝plugin.json 473317da·.codebuddy-plugin plugin.json a87e66e4·bundle.lock 2635ad65 链盘全等＋plugin.json 版本面现读 0.1.31 零 bump 坐实。
- 哈希锁两卷两态 SAME＝skills／sop／references／architecture-v2.9-copy.md 9a648030／176 行·product-v2.9-copy.md dbf49d0b／56 行＝链盘＋行数三口径全等（本席现算补钉路径＝转引面值钉值对号命中）。
- README 两态 SAME＝fc449fa9＋semantic-governance.py 7cd56d09 盘 hash 现算 SAME（复勘补钉登记）。
- share 全域两态零枚＝git status 与 git diff scoped -- share 现跑皆零枚＋BUILD 面单前缀四枚全落包内＝diff 面与面单两面皆零。
- tests 既有 28 枚 dirty 零现跑＝ls-files tests 现数 29（28 既有＋本笔 run-all.sh）＋scoped status 零枚＋diff 现跑零枚。
- 主仓路径只读以外零触碰（本席仅 rev-parse／show／log／status／diff／hash-object／ls-tree／ls-files／cat-file／grep／merge-base／wc 只读）；账本零手写·FUXI 零碰·.gitignore 零触·sparse 零处理·他案面零带入（staged 零枚）；盘落 CRLF 制式沿册＝全部对拍在剥 CR blob 面等值成立。

## 五、E／V 面转引＋本席当轮复跑臂（主理人窗项转引标注不冒充）

- V5 缺省扫描本席复跑＝python3 share／check-pointers.py --root . 单跑 exit 1＝BLOCK 恰 1863／WATCH 现跑恰 1007（严格标记行口径计数现跑：行首路径冒号行号 BLOCK 段 1863／WATCH 段 1007）＝BLOCK 对在册锚 1863 全等零漂移＋WATCH 对锚 1009 差减两枚＝归因沿册转引＝他案 T2c 验收窗取证副本（.scratch／t2cacc／chain-root-audits／ PM 审票＋QA 审票同名件在盘本席 ls 坐实＝「仓内无同名件」WATCH 条件不再触发＝减 2＝取证窗内容敏感归因条款沿册·只平或降成立·禁判漂移）。
- check-pointers 四面自靶本席复跑＝S1／S2／S3／S4 逐枚 --target 现跑＝各 exit 0 输出零行全等（转引 BUILD 在册读数同值）。
- check-ticket --target EXT 面两态复跑见 §三-4（BLOCK 恰 14／WATCH 恰 0 两态全等＝分治案型沿册）；S1／S2／S4 非票面不适用照登（目录模式 exit 0 域闸全豁免沿册＝转引）。
- V6 入线四词＝转引 BUILD 合成面读数 0／0／0／0＋本席复跑＝S2／S4 diff 增行面＋S1／S3 全件面合成件现跑＝真源形态 0／文件域 0／席位职权 0／工序链 0＝停手闸未触发。
- E5 接线实效判据面＝S1 实效 exit 0＋RUN_ALL_GREEN 未达＝归因与不可修申报见 §二 drill-05 候裁面（本席复跑三读数坐实＝非本笔所致＝验收呈请引用面）；其余 E 系＝工单形制／效力域自证／三工具去向／台账入账＝§二 S3／S4 抽查面在册＋§三逐枚。
- 验收席后续独立现跑项＝fresh QA 独立验收一枚归验收席当轮现跑（放行 §四 排程在册·本席窗不预跑不冒充）。

## 六、本笔纪律自证（RECEIPT 笔）

- 新体例申明＝席零 git 写·投递归主理人统一执行（裁决登记 c34f204e 口径）＝本席全窗 git 命令仅只读＝rev-parse／show／log／status／diff／hash-object／ls-files／ls-tree／cat-file／grep／merge-base／wc 读＝零 add 零 commit 零 amend 零 stash 零 config 写·index 零触碰。
- 面单恰回执一枚＝本件；投递动作归主理人（add 单 pathspec 紧邻 commit＋FX_COMMIT_DECLARE 挂 commit 命令侧＝本回执仓根相对径一枚＝主理人侧执行·本席只产载体）。
- message 载体＝.scratch／t2erec2／msg-receipt.txt 落盘（单行裸文·collab: 起头·裸文＋全角斜杠·零 at 零反引号·尾标 -RECEIPT·内嵌全部关键读数·wc -l＝1 落盘后现跑坐实＝两案型在册勿复现条款兑现）＋/tmp／t2erec2-msg-receipt.txt 备份（cp 命令参数形制见载体投递面·reapply 连带删案型防险沿册）。
- 落笔前自靶＝python3 share／check-pointers.py --root . --target 本回执实路径 exit 0 输出零行现跑（读数落 .scratch／t2erec2／selftarget-receipt.txt 随回报）＋体例三零自查现跑＝本件反引号 0／at 0＝皆零；非缩进段半斜杠面＝恰两行＝载体行 /tmp 根备份 OS 保留路径本体（与 T2c 先例回执行同形同位沿册照登）＋本申明行自指命中一枚（申明行自身述及该路径＝自指沿先例口径不在禁例射程·叙述面其余非缩进段半斜杠零）；短式钉列举面＝回执登记面对钉值以八位短式列举＝先例回执同款形制＝四十位全式居写集四枚成对表与依据链三枚面。
- 完工前自查硬条款坐实＝回报前现跑 ls 坐实回执件＋载体两件在盘＋回执盘 blob 现算（读数随回报 inline）。
- 收尾自证＝盘现跑 git status＝staged 零枚＋tracked M 零枚＋?? 恰一枚＝本回执一枚＋sparse D 态 1018 枚照登；HEAD 收尾复跑对钉基准不受影响；取证族 .scratch／t2erec2／（runall-now／drill05-inj／drill06-inj／v5-pointers-rec2／ct-ext 两态／sp-recheck／diffplus-synth／selftarget-receipt／msg-receipt 载体）居 ignore 面不入 status（取证族保留不归拆除＝reapply 防险沿册·沿 T2a／T2b／T2c／T2h 先例口径）。
- 链上后续沿放行登记＝fresh QA 独立验收一枚→产品席收口一枚（MC-PAIR-1 在判预期随收口件 +1）；本笔投后本票链为五笔（开票＋快审＋放行＋施工＋本回执）。

## 七、案型登记

1. **开工链序面值相邻两枚顺序误抄沿册**＝派工面值 c9bf765b／3bdabc89 相邻顺序与机械现读相反（放行笔 §〇自矛盾同款＝BUILD 笔开工窗已报备同款）＝八枚集合全等唯两枚次序误抄＝机械现读为是＝沿册续登。
2. **E5 前置现势面值失实＝「前置现势面值必现跑」新案型**＝票面 E5 前置「零红态现势」与现势不符＝drill-05 存量红两因在册（ensure_ascii 漂移 5b8936e7 起＋夹具）＝照票 verbatim 执行反而红＝修两路皆触禁动面＝不可修如实申报＝条文候选沿 BUILD 登记续证（本席三复跑读数坐实）。
3. **shell argv 展形制触体例三零＝run_step 参数化改形正面范沿册转引**＝BUILD 首稿 dollar 加 at 符连写一枚即改 run_step 形制归零＝本席现跑佐证＝S1 全件反引号 0／at 0 终态坐实。
4. **WATCH 取证窗双向归因首例沿册转引**＝先例只预增侧·本窗减侧差 2 归因坐实＝本席复跑 1007 对锚 1009 差减复现＋取证件在盘 ls 坐实＝归因条款只平或降成立。
5. **转引漂移一行级复现登记**＝放行登记行数转引面值 46 行 vs 本席三口径现跑 45 行（show 管道 wc＝grep 计数＝盘 wc 互算全等＋无末行换行排查＝末字节 0a 在位）＝blob 钉值 dcbb9d4a 成对全等＝一行级转引漂移＝T2c 验收黄-A 同族＝入候补池候选续登。
6. **check-ticket 对工单体两态 BLOCK 恰 14 三度复现**＝T2h 先例 14／T2c EXT 案型／本票 EXT 面两态各 14＝分治案型沿册稳态读数＝机检缺位候补池续登。

模板纪律（预置申明行）＝零反引号零 at·叙述裸文＋全角斜杠·命令缩进段·append 不适用（回执一次成文）。
