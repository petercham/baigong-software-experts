# ITER-W2-T2b · check-ticket 票面机检脚本票 · 工程师席施工回执（v1）

- 席位署名＝施工＝eng-iter-t2b（BUILD 施工席·内容生产＋取证生产·席零 git 写）＋本席＝eng-iter-t2b-r2（RECEIPT 回执成文席·全窗 git 命令只读·投递归主理人统一执行＝裁决登记 c34f204e 口径·一票一新鲜实例）
- 票面＝.scratch／tickets／2026-11-19-ITER-W2-T2b-check-ticket机检脚本票.md（139 行·blob ad795b26ce52aed20b09163e6144d933b0019846·链上 0847e001）；QA 快审判词＝.collab／audits／2026-11-19-ITER-W2-T2b-QA快审判词-v1.md（74 行·blob fa1b7c4c9cca80af70dd65df47f3c58649cff5a1·链上 2ad25bca）；放行登记＝.collab／decisions／2026-11-19-ITER-W2-T2b-票级放行登记-v1.md（38 行·blob 319503c17bf7a6ec8740528f356303e943addf86＝本席链上现算补钉·链上 431d7a6c）
- 写集恰两枚＝S1 新建 check-ticket.py 一枚＋S2 sop／SKILL.md 索引随动一枚（J-3 采甲）；BUILD 笔＝1659dfcf39da478c0577b0fc279ec978f4c5c226（parent 431d7a6c＝放行登记笔·COMMIT_EXIT=0 ELAPSED=9s＝α 常态闸＝转引主理人投递窗读数）
- 体例＝照 receipt-template.md 现势（bb1a08d99c9eb05f6d2fda214c1301bbe979ac99／27 行·链盘两态对钉见 §四）七节骨架实占·节次按派工书 §一～§七 排布·先例＝T2a 回执取形（2026-11-19-ITER-W2-T2a-施工回执-eng-iter-t2a-r2-v1.md）·本回执一次成文（append 不适用）·零反引号零 at·叙述裸文＋全角斜杠·命令缩进段。

## 一、开工读数（本席当轮现跑·禁抄旧数）

    date 现跑＝2026-11-19T05:05:35+08:00（施工回执成文窗）
    git rev-parse HEAD ＝ 1659dfcf39da478c0577b0fc279ec978f4c5c226＝四十位对钉全等命中（＝BUILD 笔链顶现势·零后继·本窗尚无回执笔＝本件成文后由主理人投递）
    链序 git 逐笔^现跑＝1659dfcf^＝431d7a6c（放行）＋431d7a6c^＝2ad25bca（QA快审）＋2ad25bca^＝0847e001（开票）＋0847e001^＝a6e9055d（T2a收口）＝链序 1659dfcf（BUILD）←431d7a6c（放行登记）←2ad25bca（QA快审）←0847e001（开票）←a6e9055d（T2a收口）逐笔^相衔零断
    git rev-parse --git-dir 现跑＝D:／multi-agent-collab-devkits／.git／worktrees／baigong-software-team＝worktree 独立 gitdir 坐实
    锁态现跑＝worktree 独立 gitdir 内 lock 族零枚＝NO_LOCK_FILES（ls 通配存在性现跑零命中）
    脏面现跑＝staged 零枚＋tracked M 零枚（git diff --name-only 计数中 1018 枚全落 sparse skip-worktree D 态面＝git status --porcelain 现跑「 D」恰 1018 枚照登勿处理·处置归主理人投递侧沿册）＋?? 零枚（开工窗）
- 依据链三枚真源对钉现跑＝票面 git rev-parse 0847e001:票径＝ad795b26ce52aed20b09163e6144d933b0019846＋git show 管道 wc 现跑 139 行＋盘 hash-object 现算＝同值＝链盘人三面对钉 SAME；快审 rev-parse 2ad25bca:判词径＝fa1b7c4c…／74 行＋盘对钉 SAME；放行 rev-parse 431d7a6c:放行径＝319503c17bf7a6ec8740528f356303e943addf86／38 行（本席现算补钉·派工给口径为现算 blob／38 行·落值坐实）＋盘对钉 SAME。
- thin 真源三面对钉现跑＝rev-parse HEAD:模板径＝1703b61073ef4894d0abf3612d957ad439dca69f＝盘 hash-object 同值＋wc 80 行＝判据单一真源成立（模板本体＝禁动面·零触坐实见 §四）。

## 二、BUILD 面单现跑＋依据链对钉＋写集两枚成对表

- BUILD 笔面单本席现跑＝git show --name-only --numstat 1659dfcf 现跑＝恰两枚零夹带＝S1 check-ticket.py 483／0（新建）＋S2 sop／SKILL.md 1／1＝对放行 §四「写集＝新建 check-ticket.py 一枚＋sop SKILL 索引行 30 一处＝两枚」闭集零越界；面单 grep share 前缀现跑零枚＝share 不入面单。
- 投递记转引（主理人投递窗现跑读数·标注转引不冒充本席现跑）＝BUILD 笔 COMMIT_EXIT=0 ELAPSED=9s＝α 常态闸＋add 两 pathspec 紧邻 commit＋FX_COMMIT_DECLARE 两枚挂 commit 命令侧。
- post-commit 日志行本席对链上日志文件现读坐实（非转引）＝.collab／evidence／hooks／post-commit.log 末行现读＝2026-11-19T04:56:41 1659dfcf POST-COMMIT-PAIR PASS HEAD面单=2 声明=2＝面单与声明对等核验通过（对等实证沿 T2a 面单=7 声明=7 先例口径）。
- 主理人独立 scoped 复核对钉（转引主理人窗在册值·与施工席 eng-iter-t2b 回报全等）＝S1 blob 5a9aa5fd／483 行＋py_compile exit 0＋--selftest exit 0 夹具 14 枚全绿复跑对等＋S2 dcb33a45／37＋numstat 1／1 对钉全等；本席 §四／§五 逐枚现跑全等命中（下段成对表＋§五复跑臂）。
- 写集两枚开工改后双 blob 双行数成对表（开工值＝本席对 parent 431d7a6c 链上现跑＝与票面 §二.9 开工在册钉值全等·改后值＝本席对 1659dfcf 链上 rev-parse 与盘 hash-object＋wc 现跑）＝
        S1 skills／sop／scripts／check-ticket.py　开工 absent（parent 链上 ABSENT＋票面 §二.9 两态 absent 在册）　→　改后 5a9aa5fd2531ba2b5db182ba6f43958787771b39／483 行（wc -l 现算入册＝行数不设写死面值沿册）
        S2 skills／sop／SKILL.md　开工 3e0bdc64958b4fb4919c25e825b9731d7d95aaae／37 行　→　改后 dcb33a45460106bef9281bd91e081722fcee5807／37 行
  ＝两枚盘 blob＝链上 blob 逐枚 SAME 零漂移（git hash-object 盘现算 vs git rev-parse 1659dfcf:径现取两种法对拍全等）；scripts 目录枚数现跑＝git ls-tree 1659dfcf 现算 19 枚＝18＋1（S2 自校行 ls 口径自动随动无需改坐实·票 §三 S2 条款成立）。

## 三、施工席申明面登记（转引 BUILD 笔 message 在册申明＋本席可复核面随注）

1. S2 numstat 1／1 行内插入形制＝派工面值「37→38／增1比删0」算术自矛盾沿册续登＝行内一处插入两账只能其一（行内最小置换＝增1删1＝行数不变 37；若加行方为 37→38）；施工席按票面 §三 S2 规格「索引句末插入」＋J-3 随正行 30 锚落笔＝实测 1／1 零加行零凑数＝如实登记候裁值侧＝裁定归验收席（先例＝T2a S5 面值 36→38 两账皆指 37 案·按规格落笔零凑数＝正确处置范沿册）。本席旁证现跑＝S2 改后行数 wc 37 与开工 37 全等＝numstat 1／1 与行数账自洽。
2. 落位双嵌套案沿册复现＝worktree 根即包目录·git 在册真位为嵌套包路径 agent-experts／baigong-software-team／…；施工席首笔 S1 误落 worktree 根 skills／（?? 新建误建面）＝现跑发现即归位嵌套真位＋误建族拆净坐实（施工席申明＝find 零枚＋sparse D 态计数 1018 未变＝零误删）＝转引 BUILD 笔申明在册；本席开工窗 ?? 零枚复跑＝拆净态成立。
3. CT-8 同受 --since 闸落码＝票面 §三.4 CT-8 目未显式标日期闸·与 V2 期望「T2a 正样例面 exit 0」冲突（CT-8 无闸则 T2a 叙述面必 WATCH 3＝exit 1）＝施工席以计划行 120 扫描域条款（规范生效日后新票防炸基线）消解＝采闸内写死形制落码＝候验收席复核（J-1 采甲在册·转引 BUILD 笔申明）；本席复跑臂佐证＝T2a 链面 --since 2026-11-20 正样例 exit 0 见 §五＝消解后 V2 期望成立。
4. mtime 案不采＝面日期取法采文件名日期前缀＋无前缀名回落 git 新增笔 author date；mtime 案不采原因＝sparse 检出 worktree 内盘面文件 mtime 全为 checkout 时点现值＝对存量面日期必误判必炸＝案型随登（转引 BUILD 笔申明在册）。

## 四、禁动面两态现跑复验逐枚（链上 rev-parse vs 盘 hash-object）

- 链上史件三枚零触＝票面 ad795b26／139 行·快审 fa1b7c4c／74 行·放行 319503c1／38 行＝链上 rev-parse 与盘 hash-object 逐枚 SAME＋wc 行数全等（§一 三面对钉）。
- thin 判据真源零触＝1703b610／80 行三面对钉 SAME（§一）＝只读解析零扰动。
- 五模板两态 SAME＝receipt bb1a08d9／27·ticket 139d0b8b／118·closeout 7c14c074／57·return c2350972／39·decision-pack c7f0950e／48＝链盘逐枚全等（receipt-template＝本回执体例真源）。
- 席位卡五枚两态 SAME＝lead 87c493c1／79·architect 802b2df6／48·engineer 4a53bd5a／50·product 6ef32397／47·qa 58b351a5／50＝链盘逐枚全等。
- config 七 json 两态 SAME＝dispatch-spec 5ba2450f／110·seat-permissions a4d02872／73·seat-permissions-hooks-map ff8ccf6d／40·semantic-closed-sets da2e4869／1128·thresholds c7bacfb9／40·ticket-authors 5f0bb6c4／25·ticket-types b4b8f23d／26＝链盘逐枚全等。
- .githooks 两枚两态 SAME＝pre-commit dc5b3aad／17·post-commit 61bad3d3／30＝链盘全等。
- 三同源版本面零 bump＝plugin.json 473317da／118·.codebuddy-plugin plugin.json a87e66e4／122·bundle.lock 2635ad65／70＝链盘 blob 逐枚 SAME＋版本面三处现读同值 0.1.31＝J-4 采乙零 bump 口径沿册坐实。
- 哈希锁两卷两态 SAME＝architecture-v2.9-copy 9a648030／176·product-v2.9-copy dbf49d0b／56＝链盘全等。
- README 两态 SAME＝fc449fa9／99＝链盘全等零触。
- share 全域两态零枚＝git diff --name-only HEAD -- share 现跑空输出＋BUILD 笔面单 grep share 前缀现跑零枚＝diff 面与面单两面皆零；thin 本体零触（三面对钉 §一）。
- 链上史件零回改＝本票五笔（开票 0847e001／快审 2ad25bca／放行 431d7a6c／BUILD 1659dfcf／本回执待投）正向落链·父子^相衔零断（§一 链序现跑）·本席零 amend 零 rebase；账本零手写＝本席窗零触碰；FUXI 零碰；他案脏面零带入＝staged 零枚现跑；主仓路径只读查询以外零触碰；docs／.collab 三桶（本回执新件除外）／.gitignore／tests／ 零触（面单零枚 §二）。

## 五、V 系转标（V5 对锚＋自靶转引＋本席当轮复跑臂·主理人窗项转引标注不冒充）

- V0 开工读数＝§一（本席当轮现跑）。
- V1 开工对钉＝§二成对表开工列（S1 两态 absent＋S2 3e0bdc64／37＝本席对 parent 431d7a6c 链上现跑＝票面 §二.9 在册钉值零漂移复现）＋thin 三面对钉 §一。
- V2 三态复跑臂本席当轮现跑（脚本＝agent-experts／baigong-software-team／skills／sop／scripts／check-ticket.py）＝
        一·--selftest 复跑 exit 0＝内置夹具 14 枚全绿（正样例零发现／违例合成七目归因／缺件与真源失联 exit 4 语义）＝对放行在册「夹具 14 枚全绿」读数全等；
        二·正样例复跑＝T2a 链上票面 --since 2026-11-20 exit 0＝BLOCK 0／WATCH 0（票面 V2 槽填三跑口径之正样例随正后断言坐实）＋T2b 在盘票面 --since 缺省 exit 0＝BLOCK 0／WATCH 0；
        三·违例合成复跑＝.scratch／t2bbuild／2026-11-21-syn-missing-sec.md exit 1＝BLOCK 恰 1 枚归因 CT-1 缺节题行命中＋WATCH 2 枚＝CT-8 对 T2b 票面自体两枚（黄-6 口径全等）；
        四·缺件 exit 4 复跑两态＝--target 不存在面 exit 4＋--template 不存在 exit 4＝fail-closed 不降级成立。
  取证落 .scratch／t2brec／（selftest-rerun／pos-t2a-rerun／pos-t2b-rerun／syn-missing-rerun／exit4-target／exit4-template 六件在册·ignore 域）。
- V3 落盘坐实＝§二 面单现跑恰两枚零夹带＋numstat 483／0＋1／1＝对放行 §四逐枚预期全等；S1 行数 483＝wc 现算入册（无预钉面值沿册）。
- V4 自靶＝转引施工席读数（.scratch／t2bbuild／selftarget-s1.txt＋selftarget-s2.txt 在册零行＝新脚本件与 S2 面各 check-pointers --target exit 0）＋本席当轮复跑＝--target S1 面 exit 0 输出零行＋--target S2 面 exit 0 输出零行（落 .scratch／t2brec／selftarget-s1-rerun.txt＋selftarget-s2-rerun.txt）＋本回执件落笔前自靶 exit 0 读数见 §六。
- V5 缺省扫描本席现跑＝python3 share／check-pointers.py --root . 单跑 exit 1＝BLOCK 恰 1863／WATCH 恰 1009＝对放行在册锚 1863／1009 全等零漂移＝本施工面零新增（取证窗 .scratch／t2brec／ 落 ignore 域零入 WATCH＝T2a 验收黄-1 取证窗内容敏感案型沿册预防成立）；本席不复跑全链其余闸不冒充。
- V6 入线四词本席现跑＝BUILD 笔 diff 面（git show 1659dfcf 加减行现取 grep 逐词）＝真源形态 0／文件域 0／席位职权 0／工序链 0＝四词全零＝标准档维持零升档·停手闸未触发（取证件 .scratch／t2brec／build-diff-lines.txt 在册）；对 S1 全件面逐词现跑亦 0／0／0／0＝§三 S1 规格第 1 条禁写四词条款前置保证坐实；本回执件自身词面命中随完工回报登记＝申明面自指·沿先例口径不在 V6 射程（V6 射程＝施工笔 diff 面）。
- 验收席后续独立现跑项（本席窗不预跑不冒充）＝fresh QA 独立验收一枚＝V2 三态真跑全套＋违例存量样本 3bc1f5a5 型复现面＝归验收席当轮现跑（放行 §四 排程在册）。

## 六、新体例申明＋本席纪律自证（RECEIPT 笔）

- 新体例申明＝席零 git 写·投递归主理人统一执行（裁决登记 c34f204e 口径）＝本席与施工席均只产内容与载体；本席全窗 git 命令仅只读＝rev-parse／show／log／status／diff／hash-object／ls-files／ls-tree／check-ignore／sparse-checkout list／config get 读＝零 add 零 commit 零 amend 零 stash 零 config 写·index 零触碰。
- 面单恰回执一枚＝本件；投递动作归主理人（add 单 pathspec 紧邻 commit＋FX_COMMIT_DECLARE 挂 commit 命令侧＝本回执仓根相对径一枚＝主理人侧执行·本席只产载体）。
- message 载体＝.scratch／t2brec／msg-receipt.txt 落盘（单行裸文·collab: 起头·裸文＋全角斜杠·零 at 零反引号·尾标 -RECEIPT·内嵌全部关键读数）＋/tmp／t2brec-msg-receipt.txt 备份（reapply 连带删案型防险沿册）。
- 落笔前自靶＝python3 share／check-pointers.py --root . --target 本回执实路径 exit 0 现跑（读数落 .scratch／t2brec／selftarget-receipt.txt 随回报）。
- 收尾自证＝盘现跑 git status＝staged 零枚＋?? 恰回执一枚＋HEAD 1659dfcf 未变复跑＋sparse D 态 1018 枚照登＋取证族 .scratch／t2brec／ 居 ignore 面不可见照登（取证族保留不归拆除＝reapply 防险沿册·沿 T2a／T2d-α 先例口径）；本回执零反引号零 at。
- 链上后续沿放行登记＝fresh QA 独立验收一枚→产品席收口一枚（MC-PAIR-1 第六件＝必引本票验收判词全名）；链封顶自算七笔·本笔投后为五。
- CRLF 制式对拍注记沿册＝盘落 CRLF＝全仓 core.autocrlf=true 存量制式（本席现跑 core.autocrlf＝true）＝全部 blob 对拍皆在剥 CR 面 blob 面等值成立＝制式面非内容面（防后续席以盘 byte 面 hash 误判漂移）。

## 七、案型登记

1. **派工面值算术自矛盾续证**＝本票 S2 面值「37→38」与 numstat 1／1（行内插入·行数不变）算术自矛盾＝与 T2a S5「36→38 两账皆指 37」同案型续证复现＝派生数字漂移病灶在派工面值面复现链第二枚实证＝处置范式沿册＝席按规格落笔零凑数＋如实登记候裁值侧＝裁定归验收（§三-1 在册）；CT-8 落码面「票面 §三.4 与 V2 期望冲突以计划行 120 消解」同属派生规格互斥候裁型＝候验收复核（§三-3）。
2. **引用即漂移·取真源不取引用＝候补池条文沿册续证**＝本票红-1 随正条款「全部判据正文一律以 thin 盘面真源运行时解析为唯一准·禁从票面引用行取 verbatim」＝放行登记 §四案型①在册候选条文；本回执全部对钉读数皆链上 rev-parse＋盘 hash-object＋wc 三式现跑零承接旧面引用＝同构自洽随登；落位双嵌套案（§三-2）＝派工面侧沿册复现第三枚（T2a 收口／验收／本票）＝工具体例面归 T2c 后票消费沿册。

模板纪律（预置申明行）＝零反引号零 at·叙述裸文＋全角斜杠·命令缩进段·append 不适用（回执一次成文）。
