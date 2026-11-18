# SWB-GTFAST 起草回执 v1（闸提速与射程治理票·起草段回执笔·架构席 arch-swb-gtfast 落笔）

> 性质＝起草席回执（起草段两笔封顶之笔二＝票 §一-2 声明面兑现·落仓根 .collab/receipts 桶）。｜落笔＝架构席 arch-swb-gtfast｜日期＝2026-11-18。
> 被回件＝.scratch/tickets/2026-11-18-SWB-GTFAST-闸提交门靶检与周期全量与钩子动态根扫描域划界-v1.md（票面 blob 与行数见 §四 终值登记·含主理人转引实测数据改写一轮＝射程优先级重排 S1 划界首位／S2 靶检／S3 周期闸／S4 钩子）。
> 落位与投递随注＝仓根 .collab 无 tickets 桶＝票面照 WTGATE 先例落 .scratch/tickets/、回执落 .collab/receipts/（.gitignore L61-64 票面桶豁免行现读在册）；本仓提交权归一在册＝本席两文件只落盘，add/commit 投递归主理人唯一链面操作员。

## 〇、开工当轮实测照登

- 开工 HEAD 实测＝2d0116a9581f306da8940b41c875232089cd4b41（链顶现读·分支 main 现读＝改动笔 811bd223＋回执笔 2d0116a9 之后＝派工预期链态全等·带差零开工）。
- 脏面照登＝git status --porcelain 去 ?? 恰一枚＝仓根 .collab/board/2026-11-17-五份复盘合流与下一轮迭代计划-v2.md（M·他案在飞）；?? 散件群 32 枚照登（.py 散件／.scratch 取证族／worktree 侧台账散件等）＝全部零碰零带入零 reset。
- 锁态现读＝NO-INDEX-LOCK（.git/index.lock 不在盘）；core.hooksPath 未配置（git config --get 空 exit 1）＝钩子唯一经共享 .git/hooks 生效。
- worktree list 现读六条照登＝主根挂 main＋qa_t10_dy（detached·prunable）＋D:/cs1-wt（detached）＋D:/multi-agent-collab-devkits.wt/agent-experts/baigong-software-team（baigong-software/main）＋D:/multi-agent-collab-devkits.wt/agent-skills/fuxi-skill（fuxi/main）＋D:/multi-agent-collab-devkits.wt/wtgate-verify（detached 挂 2d0116a9＝WTGATE 验收在飞件·全程零触零判脏）。
- 票号续位实证＝.scratch/tickets 与 .collab 两域 grep GTFAST 零命中＋git grep 对 HEAD 全仓零命中现跑＝新建 v1 案型坐实。

## 一、改动面起点 blob 与钩子对钉（对 2d0116a9 现算·票 §一 回填值出处）

- 改动面七枚起点 blob＝run-gates.sh 11a6f4d4（543 行）／check-entity.py 1f4be322（302 行）／check-collab-lint.py d963f5a2（341 行）／check-pointer-closure.py 717a2adfe（293 行）／check-pointers.py 33781b31（551 行）／install-hooks.sh f71474ac（136 行）／check-hook-health.py 7fd83074（182 行）＝git ls-tree HEAD 现算；七枚对 HEAD 工作面净（status 无该七 pathspec 条目现读＝未施工坐实）。
- 禁动面对钉现算＝60-gates.md b68cbfc7df9f20a2ae41c86499863793f0ec9dfa／baseline-sot-dup.json 2c44d339／baseline-seat-decl.json f6171c7d／reconcile-daily.py ff1e4d87（引用件只读）。
- 钩子面盘上对钉＝git hash-object .git/hooks/pre-commit 现跑＝8b7857701594264421832edd30dae7e401f85719 与 check-hook-health.py L47 EXPECTED_HOOK_BLOB 常量 grep 现读逐字符全等＝开工存续态。

## 二、两态基线与耗时现跑读数（起草当轮·日志落仓根 .scratch/SWB-GTFAST-draft/）

1. 主根全套缺省模式＝bash share/run-gates.sh --root 主根 --no-write 现跑（后台重定向·real 8m49.752s）＝**GATE BLOCK exit 1 恰一枚**＝- agent-experts/baigong-software-team/.workbuddy/memory/2026-11-18.md:34 OA-T1 BLOCK＝假阳性咬闸在闸面现行复现（日志 gate-mainroot-baseline.log 35591 行）。
2. 发现数按 run-gates FINDING_RE 口径现算＝总 **33391**＝check-pointers BLOCK 18231／WATCH 4575＋check-collab-lint WATCH 6353＋check-pointer-closure WATCH 3754＋check-source-of-truth WATCH 467＋check-ticket-reconcile WATCH 10＋check-entity BLOCK 1；其余五枚零发现＝票 §〇-6 基面登记值；旧钉 22810／151502 系旧链态值（DEBTCLN-R1／BKTCLS 票原文现读）＝作废不追因（BKTCLS 钉值口径随动先例）。
3. 单枚耗时逐枚现跑计时（串行单独·--root 主根）＝check-collab-lint 1m34s／check-pointers 9.1s／check-pointer-closure 8.0s／check-ticket-reconcile 2.4s／check-entity 0.4s／check-adr 0.4s／check-provenance 0.3s／check-hook-health 0.2s／check-collab-buckets 0.2s／check-skill-meta 0.2s／**csot 单枚现跑 real 0m0.676s**（票 §〇-2 派工要件「自己现跑一枚 csot 单枚耗时」兑现＝不必再烧 7 分钟；观察账 7m03s／6m57s 两样本系主理人转引注明）。
   **耗时数据改版登记（主理人转引＋本席复跑对照）**：主理人当轮逐枚实测转引（取证件＝.scratch/GTFAST-timing/per-gate-timing.txt 本席现读全表核对）＝lint 141603ms／closure 10278ms／pointers 9974ms／ticket-reconcile 3056ms／csot 601ms／entity 475ms／adr 385ms／hook-health 301ms／buckets 233ms／provenance 272ms／skill-meta 217ms＝总计约 168s；**本席复跑对照＝check-collab-lint 一枚复跑 real 1m45.6s（约 105.6s）**＝与转引 141.6s 同量级，读数差如实登记不追因；本席首轮单独计时（1m34s）亦在册三读数并存。
   **包内卷宗计数本席复跑对照**＝find 口径＝external-advisor-collab 包内 .collab/.scratch 族 12602 枚／fuxi-skill 包内 7530 枚（主理人转引 8839／6738 系不同 find 口径＝两读数并存不追因）；tracked 面 git ls-files 现跑 1921 枚；磁盘 .md/.txt 粗计 find 现跑 158942 枚。根因三件（热点单点 lint 占约 84%／扫描域虚通病／提交门语义错位含 9MB 证据件）已照写入票 §〇-2 归因段；票面并附本席实读勘正随注（转引括注「同侪皆剪 .collab/.scratch」精确化＝entity L177＋ticket-reconcile L295-298 剪，pointers L334 与 closure L126 亦不剪，唯 lint 连扫描域都不设＝整仓根入扫最重）。
4. 假阳性实证补强现跑＝check-entity 现跑 BLOCK 恰一枚居 .workbuddy 记忆面＝该件 git check-ignore 命中 .gitignore L71＝untracked（git ls-files 全仓 .workbuddy 计数 0）；绕行留痕存量现读＝.collab/evidence/gates 全桶 12707 枚 json 中 bypass 留痕 150 枚（grep 计数现跑）＝留痕常态化临界值在册。

## 三、新钩子候选预演读数（票 §三-4 判据基数出处）

- 按票 §二 S3-a 围栏逐字节重建件落盘＝.scratch/SWB-GTFAST-draft/new-hook-fenced.sh＝git hash-object 现算＝**02d30d01e53f9c7b38803dfbd1d599f9a23c4d16**（629 字节·八行＋printf 追加末换行＝末空行形制与现行钩子 od 现读末两字节同制）。
- 查三臂手核＝MARKER 行 grep 计数 1／check-staged-declaration.py 后缀 1／run-gates.sh 后缀 1＝改后钩子对改后 EXPECTED_HOOK_BLOB（钉随正后）可过坐实。
- git 旗可行性＝rev-parse --path-format=absolute --git-path hooks 两态同读数先例系 WTGATE 回执 §三-4 在册（本机 git 2.55 系该票当轮现读）＝本票 S3-b 承引不重跑（同链态同机·转引注明）。

## 四、票面自查读数

- 票面改版轮随注＝主理人转引逐枚实测数据到达后票面改写一轮＝射程优先级重排（S1 扫描域划界升首位拆两点＝lint 剪枝口径修正＋.workbuddy/ 划界／S2 提交门靶检逐枚优先级写明＝lint 第一、pointers+closure 第二、其余九枚豁免不补靶＝复杂度取舍如实写明／S3 周期闸随证据件瘦身候补池随注／S4 钩子动态根）＋§〇-2 根因三件照写＋§三-1 验收判据补 date +%s%N 前后差现跑口径；票内 S 节交叉引用编号随重排全量校平（grep 逐处核读在册）。
- 票面 blob＝改写轮终值 hash-object 现算＝**262ccecaa68afa689c45572db7e1ac6df142eabe**·行数 **178**；初稿值 71a78677（at 字符修净前）与 fb7ee2e8（数据改写轮前）两值作废随注。
- 自靶＝python share/check-pointers.py --target 票面仓根相对路径 **exit 0** 零 BLOCK（改写轮后重跑现跑·日志 ticket-target-check3.log）；反引号计数 grep -c 现跑＝**0**（OA-D6 假悬空案型零暴露）；at 符号字符计数＝**0**。
- 体例自查＝文件引用仓根相对纯路径；提及文件盘符绝对径裸文写两处（钩子硬编码字面 D:/multi-agent-collab-devkits 系问题现场引用）；登记类路径逐件全写零 brace 简写。

## 五、纪律申报与链账

- 产出恰两文件＝票面（.scratch/tickets）＋本回执（.collab/receipts）＝起草段两笔封顶兑现；**全程零 git 写操作**（零 add／零 commit／零 amend／零 stash）＝只落盘待主理人投递（提交权归一遵行）；只读 git 命令（rev-parse／log／status／diff／ls-tree／check-ignore／grep／hash-object）不禁照用。
- 真源零碰申报＝share/ 全域零字节（全程只读实读实跑）；agent-experts／agent-skills／softwares 三包内容零字节（reconcile-daily.py 只读引用）；任何 .workbuddy/ 记忆面文件零碰（含被咬件本体）；WTGATE 在飞面零触（wtgate-verify 工作区＋.scratch/SWB-WTGATE-qa/）；git config 零写；证据桶只读零删。
- 取证面纪律＝起草段全部预演／日志落仓根 .scratch/SWB-GTFAST-draft/（gate-mainroot-baseline.log／csot-single-timing.log／perf-*.out 十枚／new-hook-fenced.sh／ticket-target-check*.log）＝gitignored 临时域不入链；用毕呈报不拆供 QA 复跑参照。
- 同席多实例＝不存在（本席唯一架构席实例）；临时工作物落位＝仓根 .scratch/SWB-GTFAST-draft/ 合规（受命文书含仓外临时路径模板时本席有权请改定＝本轮未遇）。
- 候裁两项照录待裁（票 §四）＝C-1 check-pointers 索引面划界与否／C-2 周期闸规范侧立据（若裁需＝升契约整改另票）；知会五条在册。

（回执完——起草段回执笔＝两笔封顶之笔二；投递归主理人；施工段随放行归工程师席；本席止于此。）