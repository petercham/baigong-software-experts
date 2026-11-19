# SWB-GTBLOAT 起草回执＝裁决段证据桶读取瘦身与聚合索引历史归档票·架构席｜v1

> 起草席＝arch-swb-gtbloat｜日期＝2026-11-19｜被派＝工程师席（施工段随放行另计）｜本回执＝起草段两笔之二（票面＋回执＝两笔封顶·投递归主理人唯一链面操作员）。
> 票面＝.scratch/tickets/2026-11-19-SWB-GTBLOAT-裁决段证据桶读取瘦身与聚合索引历史归档-v1.md（盘上件·正文裸文零反引号围栏零 at 符号字符现跑计数各 0）。

## 一、开工读数（当轮现跑）

- HEAD＝335dbbe86a63a98d19a1bdfbdeac3533ff5ae71d（链顶现读·分支 main 现读）。
- 脏面＝git status --porcelain：M 恰一枚＝仓根 .collab/board/2026-11-17-五份复盘合流与下一轮迭代计划-v2.md（他案在飞·零碰零带入）＋?? 散件群 33 枚照登零带入。起草段两态基线现跑曾短暂出现暂存 A 一枚＝临时计时靶件 tmp-gtbloat-baseline-target.md（造靶→git add→跑闸计时→git restore --staged→删件＝红线唯一例外口径＝只 add/restore 零 commit；用毕盘上复原现跑坐实＝该枚不在收尾脏面）。
- 锁面＝NO-INDEX-LOCK（.git/index.lock 不在盘·开工前后两读各 exit 2）。
- worktree list 现读五条照登＝主根挂 main＋qa_t10_dy（detached·prunable）＋D:/cs1-wt（detached）＋D:/multi-agent-collab-devkits.wt/agent-experts/baigong-software-team 挂 baigong-software/main＋D:/multi-agent-collab-devkits.wt/agent-skills/fuxi-skill 挂 fuxi/main（GTFAST 起草期第六枚 wtgate-verify 已不在册＝现读五条为准）。
- 票号续位实证＝仓根 .scratch/tickets 域 grep GTBLOAT 零命中现跑；.collab 域命中四处＝H-0 裁定升案行／收口登记候排行／QA 判词照登行／呈裁简报知会行＝案号在册预留＝本票＝预留兑现新建 v1。

## 二、基线现跑读数（票面 §〇-6 同源）

1. **load_history 全桶读微基准（复跑对照·回执要件）**＝自链顶 c2918140 件逐字节抽出 load_history 函数体挂驱动现跑（取证 .scratch/SWB-GTBLOAT-draft/lh_micro.py＋lh-micro-run1.txt）＝**elapsed 322.0s**；桶 json 件数 **12,833**（另非 json 散件一枚＝2026-11-04-SWB-B5-judoca-readings.txt）；specs_counted 20／counts 总和 20,960／坏件 1／bypass 件 250／distinct run 2,990。对工程师席取证值 294.3s（.scratch/SWB-GTFAST-build/ 在册）＝同量级读数族并存不追因（IO 波动先例口径）；对四投递端到端 292-305s 吻合＝热点定稿存续。
2. 空暂存 --staged 现跑＝GATE PASS exit 0／real **386ms**（.scratch/SWB-GTBLOAT-draft/staged-empty.timing）。
3. 真暂存面端到端计时＝临时靶件 staged 后跑 bash share/run-gates.sh --staged 全程 date +%s%N 前后差＝exit 0／real **414,153ms**（.scratch/SWB-GTBLOAT-draft/staged-target.timing；GTFAST 期同形态 304,559ms 在册＝同因同族波动并存）。
4. 逐枚靶检耗时表引用在册＝.scratch/GTFAST-timing/per-gate-timing.txt（旧全扫值）＋QA 判词①改后循环段合计 9.259s 逐枚值＝本票不动扫描段照引。
5. 证据桶现值现跑＝12,834 条目（12,833 json）／**41GB**（du）／单件中位 147KB／最大 67.3MB／p75 约 1.4MB。
6. 缺省模式全套闸基面引用在册＝自然绿 exit 0＋FINDING_RE 总 **27,051** 逐脚本分项（QA 判词③）＝本票验收对拍基面（本票不动扫描面＝应恒等）。
7. 聚合读成本预演＝按票面 §二 S1-a 形态造探针件（covered 12,833 名＋seen_pairs 20,960 对）＝体量 1,457,068B／json 载入 **7ms**＝聚合稳态亚秒级坐实。
8. 面基对钉现跑＝run-gates.sh blob **c29181404b266cee2cce1259219b0c646c1e716c**（597 行·git ls-tree 现读＋git show 管道 hash-object 复跑全等）；钩子盘上件现值 **02d30d01e53f9c7b38803dfbd1d599f9a23c4d16** 对 GTFAST 新钉全等；60-gates.md blob **b68cbfc7df9f20a2ae41c86499863793f0ec9dfa** 对链顶现读全等；桶名闭集面＝check-collab-buckets 扫描深度＝.collab 一级 listdir 实读坐实（aggregate/ archive/ 子层零冲击）；桶消费方现跑核清单＝全仓 grep 命中＝仅 60-gates.md 文字两处＋agent-skills/object-build/scripts/publish.py gate_a2（非递归 listdir＋json 后缀过滤双保险＝零冲击）＋他包 .scratch 假树副本（零触）。

## 三、票面产出

- 落位＝.scratch/tickets/2026-11-19-SWB-GTBLOAT-裁决段证据桶读取瘦身与聚合索引历史归档-v1.md。
- blob（git hash-object 现算·S2 射程随修后终值）＝**da66555512fe06f29e46196a3fa27e7b155f7ac5**｜行数＝**148**｜反引号计数 0／at 符号计数 0（现跑）。随修前两值＝b9525bc18c34924ec8612ec55e4086820a418b4b／132 行（登记作史）。
- 自靶＝python share/check-pointers.py --target 票面仓根相对路径 **exit 0** 现跑三拍在册（.scratch/SWB-GTBLOAT-draft/selftarget.out／selftarget2.out／selftarget3.out＝落笔后／修注后／S2 随修后各一枚）。
- S 节摘要＝S1 聚合索引续算（aggregate/history-v1.json 单枚聚合＝covered_files＋counts＋exits＋seen_pairs 四轴持久化；load_history 改读聚合＋未覆盖窗续算；坏聚合回退全桶重算含 archive/ 层不含 quarantine/ 层；原子写 tmp＋os.replace；写盘点＝出口②后轮末续算）＋S2 证据桶分拣候领制＋归档分层（按决策者 11:12 裁定口径＝三步闭集识别/隔离/登记候领；quarantine/<归属分支>/ 子层＝隔离即出账不入出口③计数射程；archive/ 归档口径存续；认领与取回/销毁决定权归各项目会话；禁向他区落件/代删/催领；隔离与登记＝主理人执行面）＋S3 写盘体量候裁单列（甲维持／乙聚合落盘／丙只落 BLOCK＝乙丙触出口②条文即升 C1；裁前零施工）。
- 验收硬判据摘要＝真暂存面端到端 ≤60s 硬线＋十秒级档目标／等价性两路径 diff 空集（基线桶面＝隔离后桶面重定·lh_micro.py 甲路径复用在册）／缺省模式 27,051 族差集零／fail-closed 三例＋回退活性／桶面机检零冲击／钩子钉 02d30d01 零扰动／链面闭集 diff ⊆ 声明面（代码面两枚＝run-gates.sh 改＋gate-bucket-triage.py 增）／新增判据⑧＝分拣候领三读数闭合（活动桶他案来源计数归零（commit 抽样反查）＋quarantine 层计数＋分拣清单登记件在册；「各工作区侧桶账自洽」移出射程归各工作区自证）。
- 候裁清单＝**C-1（必列）＝S3 证据件写盘体量**（甲乙丙＋利害＋乙丙触 C1 呈清）；其余窗口口径／归档触发／隔离出账口径已落成机械判据非裁项（若审出隔离出账触出口②③条文语义＝按票面随注升裁不自行裁；若审出反例走 H-0 分支呈裁）。

## 三之一、S2 射程随修登记（主理人转引决策者口径＋当轮实测＝两笔时间线照登）

- **10:58 转引**（决策者口径＝主根＝agent 原生开发工具包总包非百工运行时空间；核定证据归属；转引含「主理人按判据机械迁册到对应工作区侧桶」设计）→ **11:12 再裁**（决策者裁定＝**分拣候领制**＝主根只识别·隔离·登记候领三步闭集，不替项目做任何越界操作；认领与处置决定权归各项目会话）＝**11:12 裁定取代 10:58 转引中迁册设计**＝票面 S2 按候领制落笔（改动面＝标题行／排程依据行两度裁定时间线／§〇-8 新增／§一 声明面 4-5＋7 随扩／§二 S2 全节改写为三步闭集＋禁动面新增＋triage 工具件／§三-2 等价性基线随隔离后桶面重定／§三-5 三目录计数＋新判据⑧三读数闭合／§四-7・8 票外登记／H-0 分支与灰度回退随注／§五 链面主理人执行面＋对抗四）。
- 本席复跑对照（落笔前自行现跑）＝主根桶 **12,836** 枚（转引值全等；与起草早段 12,834 之差＝间隔期自然新增不追因）；百工 worktree 侧 .collab/evidence/gates/＝**367** 枚（转引 357＝自然增长并存不追因）；fuxi worktree 侧＝**7** 枚（转引全等）。
- 归属判据抽样预演现跑（400 枚随机·种子 7）＝证据 json commit 字段→git branch --contains 三分支（main／baigong-software/main／fuxi/main 现读在册＋backup 分支不入集登记）＝纯包含性区分度弱（多分支包含 380／400＝共享历史段全含；单分支命中 14＝main 9＋baigong 5；不可判 6）＝据此把 §二 S2-a 归属判据收窄为**分支独有段口径**（main∈hits＝主根账；hits 单元素非 main＝可判他案入 quarantine；其余＝不可判 legacy 留主根归档）。污染成因（旧钩子硬编码主根＝GTFAST S4 已治＋QA 判词 Y2 续证在册）照登票面 §〇-8。

## 四、纪律申报

- 零 git 写操作全程坐实：add/commit/amend/stash 零笔；两态基线现跑用过的唯一暂存动作＝临时靶件 add→restore--staged→删（红线唯一例外口径＝造靶复原两步·零 commit）；收尾脏面复核＝暂存面 0 枚／靶件不在盘／锁不在盘。
- 只读命令族照用不禁＝rev-parse／status／worktree list／ls-tree／show／hash-object／diff／log／grep／check-ignore 类。
- 红线面零碰＝agent-experts／agent-skills／softwares 三包内容零碰（publish.py／reconcile-daily.py／validator 族只读复核）；60-gates.md 零动（blob 对读）；钩子与 EXPECTED_HOOK_BLOB 零动（blob 对读）；GTFAST 取证族（GTFAST-timing／SWB-GTFAST-build）与链上件零碰零拆；任何 .workbuddy/ 记忆面零碰；证据桶起草段只读零拆（计数／du／逐件统计只读扫描＋S2 归属抽样只读＝零 move 零删零改零隔离）；他案 worktree 检出目录（D:/multi-agent-collab-devkits.wt/ 下两侧桶）＝只读计数零落件（11:12 裁定二守持）；board 他案 M 面零碰。
- 产出＝两文件（票面＋本回执）只落盘不投递＝提交权归一；取证中间件（lh_micro.py／timing／out／探针）居 .scratch/SWB-GTBLOAT-draft/＝本票取证族随收口处置。
- 同席多实例＝不存在（唯一架构席实例 arch-swb-gtbloat）。
- 禁检索自救遵行＝全部读数本地现跑现读；无外部检索动作。

（起草段止于此：票面一笔＋回执一笔＝两笔封顶；投递归主理人。）
