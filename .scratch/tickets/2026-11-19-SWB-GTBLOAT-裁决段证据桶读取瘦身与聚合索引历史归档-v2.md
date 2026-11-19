# SWB-GTBLOAT · 提交门最后一段＝裁决段全桶读治理票＝聚合索引续算（出口③语义逐位守恒）＋证据桶 legacy 分拣候领制（主根只分拣不代处置·流水是史实零删）｜advisory 落盘体量＝候裁单列｜v2

> 本版＝**v2（rev 轮票面）＝取代 v1**（盘上同名 v1 件保留作史参照，不再受理工依据）；取代理由一句话＝主理人查盘轮所见 v1 旧值（b9525bc1／132 行）未含 10:58／11:12 两度转引＝起草随修与查盘并发错过（本席随修后盘上实值已为 da665555／148 行＝当轮现跑自证在下）＝rev 轮按主理人六条落实清单逐处校平＋隔离出账口径按清单二校正（回退重算含 quarantine＝流水是史实）＋候裁新增 C-2 呈清；点名处外 v1 内容零动。｜rev＝架构席（arch-swb-gtbloat·同席续写·著作席存活实例接手即认领）｜rev 日期＝2026-11-19。

> 票号＝SWB-GTBLOAT（编号续位现盘自查：仓根 .scratch/tickets 域 grep GTBLOAT 零命中现跑＝票面桶零同名件；仓根 .collab 域命中五件＝H-0 裁定升案行／收口登记候排行／QA 判词照登行／呈裁简报知会行＝系该案号在册预留＝本票＝预留兑现新建 v1 案型；git grep HEAD 命中四处同在上述链上登记件内）｜起草＝架构席（arch-swb-gtbloat）｜日期＝2026-11-19｜被派＝工程师席（施工段笔数随放行另计·见 §五）；本席只出票面＋回执零碰 share/ 真源＝纯规格零施工红线写死。
> 排程依据（已批在册·票面禁候裁排程）：决策者 2026-11-19 10:17 皮总原话口径「把主根侧部分按你的想法修好」＝本票放行依据。S2 射程两度裁定时间线照登＝主理人转引决策者口径 2026-11-19 10:58（主根＝工具包总包非百工运行时空间；核定证据归属＋迁册设计）→ 决策者再裁 2026-11-19 11:12（**分拣候领制**：主根只识别·隔离·登记候领三步闭集，不替项目做任何越界操作；认领与取回/销毁决定权归各项目会话）＝**11:12 裁定取代 10:58 转引中「主理人按判据机械迁册到对应工作区侧桶」设计**＝本票 S2 按候领制落笔。归因衔接一行＝H-0 裁定件升案（.collab/decisions/2026-11-19-SWB-GTFAST-H0裁定-提交门60s红线归因裁决段-v1.md 二-2：候补池 §四-6 证据件瘦身升案＝开另票暂名 SWB-GTBLOAT，三选项射程＝本票雏形）＋GTFAST 收口登记遗留归置首项（.collab/decisions/2026-11-19-SWB-GTFAST收口登记-v1.md 一-1）＋观察账续账归本票（.scratch/2026-11-18-观察账-闸全量扫描临界区时长-v1.md＝本票＝该观察账候选一时长维度的处方；销账续账归本票收口）。
> 落位实证随注（承 GTFAST 先例）：仓根 .collab 无 tickets 桶（check-collab-buckets 十七桶白名单不含 tickets）＝票面照先例落 .scratch/tickets/（.gitignore L59-64 豁免行在册现读）、起草回执落仓根 .collab/receipts/。
> 开工锚照登（起草席 2026-11-19 当轮实测）：开工 HEAD＝335dbbe86a63a98d19a1bdfbdeac3533ff5ae71d（链顶现读·分支 main 现读）；git status --porcelain 脏面＝M 恰一枚（仓根 .collab/board/2026-11-17-五份复盘合流与下一轮迭代计划-v2.md·他案在飞·零碰零带入）＋?? 散件群 33 枚照登零带入（起草段两态基线现跑曾短暂出现暂存 A 一枚＝本票临时计时靶件·用毕 restore 复原即删＝非开工脏面＝登记口径写明）；锁面＝NO-INDEX-LOCK 现读（.git/index.lock 不在盘）；worktree list 现读五条照登＝主根挂 main＋qa_t10_dy（detached·prunable）＋D:/cs1-wt（detached）＋D:/multi-agent-collab-devkits.wt/agent-experts/baigong-software-team 挂 baigong-software/main＋D:/multi-agent-collab-devkits.wt/agent-skills/fuxi-skill 挂 fuxi/main（GTFAST 期六条中的 wtgate-verify 已不在册＝现读五条为准）。工程师席开工 ANCHOR＝开工当轮 HEAD 实测照登；ANCHOR 不符＝停手上报，禁带差开工。
> 并发防护（承 GTFAST 同制）：每笔 pathspec 限定 add 与 commit 紧邻无窗口；禁 git add -A、禁 amend、禁裸 git commit；message 零 at 符号字符零反引号；commit 带长 timeout 且输出重定向落盘仓根 .scratch/SWB-GTBLOAT-build/；撞 index.lock 或有界等待一轮即呈报主理人；本仓提交权归一在册＝投递归主理人唯一链面操作员，本席与工程师席全程禁 git 写操作（起草段＝只落盘两文件＋回报）。

---

## 〇、复核结论（架构席 2026-11-19 对 335dbbe8 实读实跑实查，票内定稿依据）

1. **热点现跑坐实（本席独立复跑）**：run-gates.sh PY 裁决段 load_history（L375-404 现读）＝sorted(os.listdir) 全桶读 .collab/evidence/gates/ 逐枚 json.load；本席把该函数体自链顶件逐字节抽出挂驱动现跑（取证 .scratch/SWB-GTBLOAT-draft/lh_micro.py＋lh-micro-run1.txt）＝**elapsed 322.0s**／桶内 json 件数 **12,833**（另有非 json 散件一枚＝2026-11-04-SWB-B5-judoca-readings.txt 现读在册）／specs_counted 20／counts 总和 20,960／坏件 1／bypass 件 250。工程师席取证值＝微基准 294.3s（.scratch/SWB-GTFAST-build/ 在册）对四投递端到端实测 292-305s/笔吻合＝热点定稿；本席 322.0s 与 294.3s 同量级＝IO 波动族读数并存不追因（承 GTFAST 读数族并存先例口径）。缺省档同构（H-0 裁定一在册：循环约 24s＋PY 段约 295s）。
2. **GTFAST 已治面与未治面现读**：扫描段已靶化（.scratch/GTFAST-timing/per-gate-timing.txt 十一枚旧值表在册；改后循环段合计 8.9-9.259s＝QA 判词①行在册）；真提交端到端仍 284-305s＝差额全量＝裁决段桶读（H-0 裁定＋QA 判词 Y-N2 两处归因在册吻合）。桶体量现跑＝**.collab/evidence/gates 全桶 41GB**（du 现读）／单件中位 147KB／最大件 67.3MB（2026-11-09-check-pointer-closure-exit1-at12-40-15.json）／p75 约 1.4MB＝全桶读成本与体量同因。
3. **load_history 语义约束（唯一用途＝出口③次数轴·逐条现读）**：调用点唯一＝L493 load_history(set())，先于出口②写盘段（L512 起）＝本轮件不入历史。判据语义四要素（L375-404 现读）＝(a) 每个 spec_id 统计未处置轮次累计、同 run 内同 spec 只计 1 次（seen_runs 去重键＝(spec, run)）；(b) bypass 证据件整件不计（L390）；(c) 坏件跳过不删（L388 continue＝流水是史实）；(d) exit_by_spec 记录键同＝首见 (spec,run) 时该件的 exit 值入集（E-3 判据 L507 读该集）。**简单改读最近 N 枚＝破坏 (a) 全量累计＝禁**（H-0 裁定四同款：属规范面抢跑，禁凑绿禁变通）。60-gates.md（agent-skills/multi-collab/references/）出口③条文本体（三轴表「次数／趋势｜运行历史｜evidence/gates/ 累计」行＋出口③表行）＝本票零动；本票设计＝数据仍居 evidence/gates 桶内、计数定义零变＝按读法一不触条文（两读法口径之争＝rev 轮升候裁 C-2 呈清见 §四，不自行裁）；若施工中发现任何形态被迫动条文＝即升 C1 契约整改呈裁。
4. **桶面事实现跑**：.collab/evidence/gates 全桶 untracked＝git ls-files 计数 **0** 现跑＝非版本库资产＝归档/拆解属主根盘卫生＋工具面射程；桶名 evidence 在 share/check-collab-buckets.py BUCKET_WHITELIST（L46-48 现读）白名单在册；该闸扫描深度＝.collab **一级目录** listdir（L110-125 现读）＝gates/ 之下任何子层（含本票新增 aggregate/ archive/）不落其射程＝桶名闭集零冲击坐实。除 run-gates.sh 外消费方现跑核清单（全仓 grep evidence/gates 命中面）＝仅两枚：60-gates.md 文字提及两处（L18 出口②表行＋L87 三轴表行）＋agent-skills/object-build/scripts/publish.py gate_a2（L433-455 现读＝运行前后桶根 listdir 差集取当期件＋endswith .json 过滤＝**非递归 listdir＋json 后缀过滤双保险**＝新增子目录天然不入集，零改动零冲击；该件居三包＝禁动面）。其余命中面＝他包 .scratch 取证副本（FX-U14/U15 假树拷贝·零触）。
5. **既有先例与衔接件现读**：H-0 裁定三选项射程＝桶读上限／历史桶归档／裁决段瘦身＝本票 S1/S2 两子项＋S3 候裁；收口登记一-1＝GTFAST 遗留归置首项＝本票；观察账（.scratch/2026-11-18-观察账-闸全量扫描临界区时长-v1.md）候选一行＝「闸时长/增量扫描」候排＝本票兑现其时长维度处方；GTFAST 取证目录（.scratch/GTFAST-timing/＋.scratch/SWB-GTFAST-build/）＝本票基面对照证据，收口前零拆（呈裁简报三在册）。
6. **两态基线现跑（起草当轮·收口判据基面）**：
   - 空暂存 --staged 档现跑＝GATE PASS exit 0／real **386ms**（.scratch/SWB-GTBLOAT-draft/staged-empty.timing 现跑；GTFAST 期同形态读数在册 .scratch/GTFAST-timing/staged-empty-run.log）。
   - 真暂存面端到端一枚计时＝当轮现跑在册（临时靶件 tmp-gtbloat-baseline-target.md 造靶→git add→bash share/run-gates.sh --staged 计时→git restore --staged 复原＋删靶＝红线唯一例外口径：只 add/restore 不 commit）＝**STAGED-TARGET exit=0 real 414.2s**（.scratch/SWB-GTBLOAT-draft/staged-target.timing 现跑；GTFAST 期同形态 304.6s／294.2s／296.3s 读数在册＝同因同族 IO 波动读数并存不追因＝热点量级坐实不变）。
   - 逐枚靶检耗时表引用＝.scratch/GTFAST-timing/per-gate-timing.txt（旧值）＋QA 判词①改后循环段逐枚值（provenance 166ms／skill-meta 166／pointers 4272／entity 367／lint 173／closure 279／csot 368／ticket-reconcile 2263／adr 274／hook-health 215／buckets 166＝合计 9.259s）。
   - 证据桶计数现值现跑＝12,833 json／12,834 条目／41GB（§〇-1/-2）；缺省模式全套闸自然绿基面＋FINDING_RE 口径总 **27,051**（QA 判词③在册＝pointers 22,806＋closure 3,754＋csot 467＋ticket-reconcile 10＋lint 14＋entity 0）＝本票验收对拍基面。
7. **聚合读成本预演（本席现跑）**：按 §二 S1 聚合件形态造探针件（covered_files 12,833 名＋seen_pairs 20,960 对＋counts/exits）＝体量约 1.46MB／json 载入 **7ms**（.scratch/SWB-GTBLOAT-draft/ 探针现跑即造即删）＝聚合读稳态成本亚秒级坐实；真暂存面端到端十秒级档＝循环段 9.3s＋亚秒级桶读＋靶件 IO＝预算内机械可达。
8. **桶污染成因与归属判据抽样（主理人转引决策者口径 10:58＋再裁 11:12＝S2 射程依据；本席当轮复跑对照）**：
   - 桶面分居现状现读＝主根桶 **12,836** 枚（本席现跑；对主理人转引值 12,836 全等；与本席起草早段 12,834 之差＝间隔期自然新增不追因）；百工 worktree 侧 .collab/evidence/gates/＝**367** 枚现读（主理人转引 357＝间隔期自然增长并存）；fuxi worktree 侧＝**7** 枚现读（转引全等）。
   - 污染成因在册＝旧钩子硬编码 --root 主根（GTFAST S4 已治＝新钩子动态根 GATE_ROOT_DIR 现读在册 02d30d01 件）＝分居前所有工作区提交全写主根桶；QA 窄复核判词黄项 Y2「留痕组 commit 字段＝他案链顶 9be69eb7」＝钩子 env 交叉案型续证在册；新钩子生效后分居自 S4 落链起自然发生（现读三桶并存坐实）。
   - 归属判据预演（本席现跑·400 枚随机抽样·种子 7）＝证据 json 自带 commit 字段（60-gates 出口②格式在册）→ git branch --contains 判归属：纯包含性判据**区分度弱**（多分支包含 380／400＝分支共享历史段全含；单分支命中仅 14＝main 9＋baigong-software/main 5；不可判 6）＝**可施工判据须收窄为分支独有段口径**（§二 S2-b 落笔）；本抽样如实登记为「可判他面窄、不可判 legacy 为主」的盘面事实＝候领制下不可判件留主根归档层＝预期终态非缺陷。

---

## 一、声明闭集与禁动面

**本票射程（改动面候选闭集·施工段笔数随放行另计）**：

1. .scratch/tickets/2026-11-19-SWB-GTBLOAT-裁决段证据桶读取瘦身与聚合索引历史归档-v2.md（本票面 v2·rev 席落盘件·投递归主理人；同名 v1 件盘上保留作史参照不入投递面）
2. 仓根 .collab/receipts 桶内「2026-11-19-SWB-GTBLOAT起草回执-架构席-v1」件（起草席回执·已落盘）＋「2026-11-19-SWB-GTBLOAT票面rev回执-架构席-v1」件（rev 席回执·裸文写·投递归主理人）
3. share/run-gates.sh（改·**仅 PY 裁决段内嵌段**＝load_history 取径换聚合读＋聚合增量续算段＋归档段＝本票改动面之一；bash 壳段／扫描段／靶检分派段／路由表解析段／fail-closed 臂零动）
4. share/gate-bucket-triage.py（新增·S2 分拣工具件＝独立工具非闸件不进 SCRIPTS 清单＝§二 S2-c）
5. 仓根 .collab/decisions 桶内「2026-11-19-SWB-GTBLOAT分拣清单-<批次>-v1」登记件（S2-③候领清单·tracked 治理史面·**主理人执行面产出**＝投递归主理人）
6. 仓根 .collab/receipts 桶内工程师回执件（施工段另笔·落链后补入本闭集随回执申报＝先例口径）
7. 桶内非链面运行时产物（不入版本库·不入链面 diff）＝.collab/evidence/gates/aggregate/ 聚合目录＋.collab/evidence/gates/archive/ 归档子层＋.collab/evidence/gates/quarantine/ 隔离层（S1/S2 运行时生成·隔离动作＝主理人执行面）

**禁动面点名＋零碰清单（写死）**：agent-skills/multi-collab/references/60-gates.md（blob b68cbfc7df9f20a2ae41c86499863793f0ec9dfa 对链顶现算全等现读＝**出口③条文与路由表 json 围栏零动**；被迫动条文即升 C1 呈裁）／.git/hooks/pre-commit（盘上件现值 **02d30d01e53f9c7b38803dfbd1d599f9a23c4d16** 现跑对 GTFAST 新钉全等＝本票不涉钩子路径预期零动；若实跑发现涉钩子＝即呈裁不自改）／share/check-hook-health.py EXPECTED_HOOK_BLOB 行零字节／share/check-staged-declaration.py／check-pointers／check-pointer-closure／check-collab-lint／check-entity／check-source-of-truth／check-ticket-reconcile／check-adr／check-provenance／check-collab-buckets／check-skill-meta（十一枚检查脚本零字节＝本票只动 run-gates.sh 一枚）／run-gates.sh bash 壳段 L1-215 与扫描段 L160-213 零字节＝只动 heredoc 内 PY 段（heredoc 起 L216-224 env 前缀行零动，函数体 L375-404 与主流程 L493／L512 段为改动锚区）／share/baseline-sot-dup.json blob 2c44d339890811304d7f1cd3a355d88ee547e5e6＋share/baseline-seat-decl.json blob f6171c7db03cf79529c89795fd243e2a78a22b12 零字节／**agent-experts／agent-skills／softwares 三包内容零碰**（publish.py 在包内＝只读复核零改动）／仓根 .collab/ 全域（含 board 他案 M 面）零碰零投递外落笔／起草段证据桶**只读零拆**（归档动作归施工段代码运行时执行，起草段零 move 零删）／.scratch/GTFAST-timing 与 .scratch/SWB-GTFAST-build 取证族零拆零改（基面对照证据）／任何 .workbuddy/ 记忆面零碰／worktree 各工作区 checkout 零触／git config 零写／链上他案笔照登不归因。

改动面起点 blob 表（对开工链顶 335dbbe8 git ls-tree 现算回填＝参考位；工程师开工对开工基线当轮现算对账，不符＝H-0 停笔呈裁禁凑绿）：

    share/run-gates.sh  c29181404b266cee2cce1259219b0c646c1e716c（597 行·git ls-tree HEAD 现读＋git show 管道 hash-object 复跑全等）

钩子面盘上对钉（非 git 面）：.git/hooks/pre-commit 现值 02d30d01e53f9c7b38803dfbd1d599f9a23c4d16＝开工态对钉全等现跑；本票预期钩子 blob 与 EXPECTED_HOOK_BLOB 双双零扰动＝收口判据六复跑对钉。

---

## 二、施工规格（工程师照录·本席零施工·改动＝锚行定位＋插段/行内置换·程序化替换先断言计数再替换）

**总则（写死）**：判据语义本体零动＝出口③次数定义／(spec,run) 去重口径／bypass 整件排除／坏件跳过不删四要素逐条存续（§〇-3）；本票改的是**读取取径**与**物理布局**，不是计数口径；LF/CRLF 形制随基线存续禁改写；run-gates.sh 头注 spec-provenance 块零字节（三块锚行与 clause_sha256 不动＝check-provenance 零扰动）；PY 段 fail-closed 兜底臂（L597 后 except 按 4）零动。

**S1 · 聚合索引续算（主收益子项·直打 292-305s 热点）**

S1-a 聚合件落位与形态（写死）：聚合目录＝EVIDENCE_DIR 之下子目录 aggregate/（即 .collab/evidence/gates/aggregate/＝居 evidence 桶内＝桶名闭集射程内·§〇-4 buckets 一级扫描深度坐实零冲击；publish.py 非递归 listdir＋json 后缀过滤双保险零冲击）；聚合件＝aggregate/history-v1.json 单枚，字段闭集＝agg_version（整型 1）／covered_files（已折叠件名排序列表·桶根件裸名）／counts（spec 到累计次数映射）／exits（spec 到历史 exit 值集合映射·E-3 轴）／seen_pairs（[spec, run] 对列表·去重轴持久化）／covered_through（已覆盖完整日的末日 YYYY-MM-DD）／built_at／stats（covered 计数与坏件计数知数）。**聚合件名带 .json 后缀且居 aggregate/ 子目录＝天然不入桶根 listdir 的 .json 过滤集＝load_history 主路径永不把聚合件当证据件**（双保险：即便误列，聚合件无 findings 键，参与为零）。

S1-b load_history 改版（锚区 L375-404 整函数置换·签名 load_history(exclude_names) 存续）：
- 取径＝读聚合件（存在且合法）→ counts/exits/seen_pairs 载入为基态 → 桶根 sorted(os.listdir) 取 .json 且名 ∉ covered_files 且名 ∉ exclude_names＝**未覆盖窗** → 窗内逐件按既有折叠语义续算（坏件 continue 且不入 covered；bypass 件 continue 且不入 covered——bypass 件不计次但**可入 covered**＝它永远不贡献计数，登记入 stats 知数即可；折叠体＝原 L392-403 循环体逐字存续＝(spec,run) 去重键／exit 首见入集口径一字不动）。
- 聚合件缺失／解析失败／版本不符＝**回退全桶重算**＝桶根件＋archive/ 子层件＋quarantine/ 各归属子层件**三表**按文件名归并排序（三处件名同为全桶文件名＝归并后＝与分拣归档前全桶 sorted 同一全序＝**流水是史实纪律存续＝rev 轮按主理人清单二校正＝回退重算路径含 quarantine**）折叠 → 现算后重写聚合件（回退一次成本＝现全桶读量级≈300s＝一次性尖峰登记知数行，不视为闸失败）。**回退轮计数随注（写死）**：quarantine 件在回退重算中入账＝隔离后首个回退轮出口③读数会出现一次性回升（＝他案账短暂重现＝回退语义＝回到分拣前全史）；该轮末续算写盘前隔离臂复扫重归位（S2-a② 幂等＝已隔离件名不在桶根＝不重复移动）＋聚合按桶面现态重写＝回升仅此一拍不续存＝知数行登记回升差值供对账。
- NO_WRITE 只读模式＝聚合件零读改之外零写（读聚合＋窗续算照常＝只读模式语义存续；aggregate/ 目录不存在＝视作空聚合走回退重算但**不落盘**＝只读模式聚合缺失时代价＝当轮全桶读，登记知数行）。

S1-c 聚合续算写盘点（出口②写盘段之后追加·锚区 L544 written 收口行后插段）：写盘模式轮末把**本轮新写证据件＋本轮窗内既有未覆盖件**折叠进聚合件＝covered_files 并上桶根全部已折叠件名、counts/exits/seen_pairs 按续算结果重写、covered_through 更新＝**每轮聚合自足续算，零全桶重读**。原子写＝先写 aggregate/history-v1.tmp 再 os.replace 置换 history-v1.json（Windows 同语义＝无半件被下一轮读到）；写失败＝die(4)（fail-closed：聚合欠账不得静默＝证据件写失败同码先例 L543）。
- **等价性论证（写死进回执对拍）**：折叠顺序＝文件名全局 sorted；covered_files 每轮并入当时桶根全件＝任一 run 的全部件在同轮或更早轮整组入覆盖（同 run 件在该 run 结束时已全部在场；崩溃残组件由下一轮整组折叠＝旧路径同样读到的就是这批在场件＝语义对等）；未覆盖窗折叠在 covered 前缀之后进行、窗内 sorted＝与全桶 sorted 前缀延拓同序；exit_by_spec 首见口径依赖折叠序＝前缀延拓不变＝逐位一致。**等价性机械判据见 §三-2**。

S1-d 知数与观测（写死）：PY 段 stdout 追加一行桶面知数（形如 gate-bucket：桶件数／覆盖数／窗件数／聚合读耗时 ms／归档移动枚数），入 SUMMARY 不进 FINDING_RE 口径（非发现行＝不扰 27,051 族计数对拍）；该行为收口判据五的读数来源。

**S2 · 证据桶分拣候领制＋归档分层（决策者 11:12 裁定口径＝主根只分拣不代处置·流水是史实零删）**

S2-a 三步闭集（写死＝主根动作止于此三步，任何迁册/代处置形态作废）：
- ①**识别**＝工具面按证据 json 的 commit 字段（60-gates 出口②格式在册＝doc.commit 键现读 L530 写盘侧）反查归属（反查工具＝git 只读命令＝branch --contains／merge-base --is-ancestor），产出分拣清单（逐件登记：件名／commit 字段值／包含分支读数／归属判定／件指纹 hash-object 现算＋**按日聚合汇总行**＝每日件数×归属分列＝rev 轮按主理人清单一a 落笔）；归属判据机械口径（本席抽样预演 §〇-8 后收窄＝分支独有段款）：hits＝{现势分支 b ∈ 工具现读 git branch 闭集（当轮实值＝main／baigong-software/main／fuxi/main＝分支名参数化非硬编码＝通用规格）｜git merge-base --is-ancestor c b 真（等价 git branch --contains 现势分支集）}；判定＝hits=={main} 或 main∈hits ⇒ 主根账（共享历史段＝主干史实）；hits 单元素且非 main ⇒ **可判他案件**（＝baigong-software/main 独段或 fuxi/main 独段＝适用 fuxi 7 枚与将来任何 worktree＝禁一次性脚本）；hits 多他案分支不含 main／c 缺失或为 none／c 不可解析（不在库＝残骸件）／hits 空 ⇒ **不可判**＝留主根 legacy 归档层。
- ②**隔离**＝可判他案件从主根活动桶（桶根层）移入主根侧隔离层 .collab/evidence/gates/quarantine/<归属分支名>/<件名>（主根亲管盘内 os.replace 移件＝合规动作；零删；桶 untracked 已核实；桶名闭集零冲击＝buckets 一级扫描深度坐实 §〇-4）；不可判 legacy 件按 S2-d 归档层口径处置；零删零改名零压缩；**隔离层不入稳态计数射程＝写死**（quarantine/ 子层内件名带 .json 但居子层＝与 aggregate/ 同款形态＝天然不入桶根非递归 listdir 的 .json 过滤集＝load_history 稳态主路径与聚合续算面均不见＝隔离即出账＝污染账归位的机械落点）；**回退重算面含 quarantine/＝rev 轮按主理人清单二校正写死**（流水是史实纪律存续＝S1-b 三表归并；语义＝回退＝回到分拣前全史＝隔离出账仅在稳态路径成立）。
- ③**登记候领**＝分拣清单落仓根 .collab/decisions/ 登记件（tracked 桶＝治理史面·体例 2026-11-19-SWB-GTBLOAT分拣清单-<批次>-v1＝裸文写·投递归主理人）明示各归属方自领；**认领与处置（取回/销毁）决定权归各项目会话**＝主根与百工侧零代处置。

S2-b 禁动面新增（写死·11:12 裁定二）：任何席（含工程师席与架构席）与主理人均**不得向他案 worktree 检出目录落件**（迁册到工作区侧桶的设计＝已作废不施工）、**不得代删他案归属件**、认领时限**不催不设默认销毁**；工程师席施工＝只交工具件与判据读数，隔离动作与登记件投递＝**主理人执行面**（按本票判据机械执行并留痕）；他案工作区侧桶账自洽＝各工作区自证＝票外如实登记（§四）。

S2-c 工具载体（通用规格非一次性脚本）：新增 share/gate-bucket-triage.py＝独立工具件（不进 run-gates SCRIPTS 清单＝非闸件不扰全套闸面；只读主根活动桶＋git 只读命令＋写 quarantine 层与清单 stdout/落盘件由调用方指定；--root 定位承同族口径；fail-closed：git 不可用/桶不可读＝exit 4）；头注带 spec-provenance 三块形制（承 run-gates 先例兜底＝provenance 缺省域不扫 share/＝登记随注）。本票代码改动面＝run-gates.sh（S1）＋本工具件（S2）两枚。

S2-d 归档子层（legacy 与已覆盖旧件·承两度转引前设计存续）：.collab/evidence/gates/archive/（evidence 桶内子层＝双机检零冲击坐实）；归档＝os.replace 移件零删零改名＝可逆（回退＝移回桶根即复原态）；触发口径机械＝①件名日期前缀严格早于本轮 RUN_DAY（同日不归＝护 publish gate_a2 当期件语义＝运行前后桶根 listdir 差集）②件名 ∈ covered_files（已入聚合覆盖＝计数已续算）③不在 aggregate/ archive/ quarantine/ 内；归档在 S1-c 续算写盘**之后**执行（先折叠后搬家顺序写死）；NO_WRITE 模式零执行归档零隔离（只读面零移动）。桶 41GB 全留存＝归档不回收盘＝盘级压缩清理属主根盘卫生另案候排（§四-3），本票零删任何字节。

S2-e 执行顺序写死（S1/S2 耦合面）：先 S2 工具就位→主理人跑识别出清单→隔离动作落盘→**聚合索引在归位后的桶面上建**（首轮＝对隔离后桶面全桶重算＝§三-2 等价性基线随之重定；**covered_files 折叠口径随分拣时点重定基线写明**＝分拣后首轮建的聚合＝covered 只含隔离后桶根在场件＋archive/ 件名，quarantine 件名不入稳态 covered 集＝它们在场但不在稳态射程＝回退重算路径按三表另行覆盖＝S1-b）→此后每轮 S1-c 续算＋S2-d 归档＋S2-a② 隔离臂幂等复扫常态运行。quarantine 层件若将来被归属方自领取回＝归各工作区侧桶＝其计数账由该侧闸自然续算（主根零代劳）。

**S3 · 证据件写盘体量＝候裁单列（呈选项与利害·裁前零施工）**

advisory 全量逐条落 json（现跑：单轮可至 MB 级、最大件 67MB、桶中位 147KB＝41GB 堆积之源）是否瘦身＝**出口②行为口径面**＝本票不自行落。呈裁选项与利害：
- 甲案＝维持逐条全量落盘（现状）：出口②审计粒度最全；S1/S2 已消桶读成本，写侧成本（逐条 json.dump＋41GB 盘）存续。
- 乙案＝advisory 发现聚合落盘（按 spec 计数＋样本若干＋全量明细转旁路大附件件）：写侧瘦身直打 41GB；害＝出口②「findings 全量」形态变更＝60-gates.md 出口②表行形态列（findings:[{...}]）即触条文＝升 C1 契约整改（C-2 同款呈清）＋publish.py gate_a2 读 findings 判 block 的消费面随动（该件居三包＝动它需契约票）。
- 丙案＝只落 BLOCK 路由件＋计数摘要（advisory 明细不落）：最瘦；害同乙且审计席「未绿」桶明细缺失面更大。
架构席倾向＝甲（S1/S2 已解端到端痛点＝写侧收益/契约代价比不划算），倾向不作裁＝裁权归决策者；**裁前 S3 零施工**＝本票 §一 闭集不含任何写盘形态改动。

---

## 三、判据（收口判据闭集·逐条实跑留读数）

1. **提交门真暂存面端到端计时（机械·验收硬判据①）**：真暂存面造靶（临时 md 含合法指针→git add→git commit 全程 date +%s%N 前后差现跑＝钩子全链真实提交口径；靶随投递或复原登记）＝端到端 real **≤60s 硬线**＋**十秒级档（≤30s）目标读数登记**；同轮空暂存读数复现（ms 级）。基面对照＝本票起草基线 414.2s 现跑在册（GTFAST 期同因读数族 292-305s 并存）。
2. **聚合读 vs 全桶读等价性（机械·验收硬判据②·核心）**：同一桶面快照两路径对拍＝(甲) 链顶 c2918140 的 load_history 函数体逐字节抽出挂驱动（本席已造 .scratch/SWB-GTBLOAT-draft/lh_micro.py＝复用）对现桶全桶读＝counts/exits 全表读数；(乙) 改版后聚合读路径同桶读数；**diff（counts 逐项＋exits 逐项＋seen_pairs 规模）＝空集写死**。**基线桶面＝隔离（S2-②）后的主根桶面**＝聚合索引建在归位后桶面上（11:12 裁定四随改＝等价性基线随分居后桶面重定；甲驱动读数亦在隔离后桶面跑＝两侧同面）。再跑第二拍＝归档动作发生若干轮后（桶根＋archive/ 态），乙路径对甲路径基表 diff 仍空集＝归档不丢史实机械坐实。抽样对拍随跑＝出口③计数读数（E-1/E-2/E-4 趋势读数行）对旧路径输出 diff 空集（真桶面自然绿态＋scratch 假树注例各一）。
3. **缺省模式全套闸对现基面差集零（机械·验收硬判据③）**：不带 --staged 全套闸 --no-write 现跑＝GATE 裁决对 QA 判词③基面（自然绿 exit 0＋FINDING_RE 总 27,051 逐脚本分项）差集零（本票不动扫描面＝应恒等）；写盘模式现跑一轮＝出口②新件照常生成＋S1-d 知数行在册＋27,051 族计数零扰动（知数行不入 FINDING_RE 口径复跑核）。
4. **fail-closed 三例存续（机械·验收硬判据④）**：--staged 下 git 不可用（临时 PATH 剥离实跑）exit 4；损坏路由表（scratch 假树注入）exit 4；聚合件人为损坏（scratch 假树内篡改 history-v1.json）＝回退全桶重算路径活性＝当轮读数仍与乙判据基表全等＋知数行登记回退原因；ALLOW_GATE_DOWN 留痕语义不变＝假树内 bypass 生效时证据件 bypass 行在册复跑一例（真桶零污染）。**ALLOW_GATE_DOWN 真提交全程零使用**（自然绿态下零豁免＝使用计数 0 收口申报）。
5. **桶面机检零冲击（机械·验收硬判据⑤）**：check-collab-buckets 现跑 exit 0 零发现（aggregate/ archive/ quarantine/ 子层生成后复跑＝一级扫描深度实证）；publish.py gate_a2 零改动复跑活性（scratch 假树或真桶当期口径任一实跑＝当期件取径不受子层影响）；桶根 listdir 计数＝原件数＋3 目录数现读登记。
8. **分拣候领制三读数闭合（机械·验收硬判据⑧·11:12 裁定四随改）**：①主根**活动桶**（桶根层）内他案来源证据计数归零＝工具按 §二 S2-a 判据复扫桶根层＝可判他案命中数 0 现跑；②quarantine 层计数现读（按归属分支子目录分列）＋逐件 commit 字段抽样反查（随机抽样 N≥100 现算）＝抽样命中归属与层内子目录全等；③分拣清单登记件在册（.collab/decisions 桶内·tracked·件数与 quarantine 层计数全等）。三读数闭合＝分拣完成判据。**「各工作区侧桶账自洽」不入本票判据**＝候领制下主根无法代验＝移出射程归各工作区自证（§四-7 如实登记）。隔离前后主根出口③计数随动登记＝判据零动、数据归位到判据本有射程（隔离件出账＝污染账剥离＝出口③本意）；隔离与出口②③条文语义的关系口径（证据位置两读法）＝**升候裁 C-2 呈清不自行裁**（§四 候裁单列 C-2＝rev 轮按主理人清单五新增）。
6. **钩子/钉值零扰动（机械·验收硬判据⑥）**：收口点 .git/hooks/pre-commit git hash-object ＝ 02d30d01e53f9c7b38803dfbd1d599f9a23c4d16 全等；EXPECTED_HOOK_BLOB 行对开工基线 git diff 零行；check-hook-health 现跑 exit 0。
7. **链面闭集（机械）**：收口点 git diff --name-only 开工ANCHOR..HEAD ⊆ §一 声明面 1-3＋5-6（代码面＝share/run-gates.sh 改＋share/gate-bucket-triage.py 增两枚）；§一 禁动面各件收口点 git ls-tree 对开工点全等；三包内容域 diff 空集；60-gates.md blob b68cbfc7 对开工点全等。

（H-0 被动咬处置分支（写死）：实跑出现——起点 blob 对表不符／等价性 diff 非空／端到端超 60s／27,051 族出现非零漂移／桶名机检转红／钩子 blob 现算变动／分拣复扫可判他案命中非零＝当场是红：工程师席立即停笔（禁改判据、禁凑绿、禁回改史账、禁自行删桶任何件、禁向他案 worktree 任何落件），回流件如实登记咬合明细＋定位串＋复现命令，呈主理人裁另案；咬出缺陷≠事故，凑绿＝事故。）

（灰度判据声明字段（decision-pack 装配核对面·票内声明不现场裁量）：本票灰度＝无灰度全量切换（run-gates 即改即生效；隔离动作＝主理人执行面一次性批次＝不入灰度面）；回退路径＝改动笔 git revert 一笔（run-gates.sh blob 对开工基线复原＋triage 工具件随 revert 删除）＋桶面复原＝aggregate/ archive/ 两子层整体删除即回开工态（聚合可再生＝删聚合件后旧路径零依赖；归档件删层前先移回桶根＝史实零损）＋quarantine 层不随代码回退拆除（隔离件已出账＝回退代码后旧 load_history 对 quarantine 不可见＝旧路径桶根 listdir 同样不递归＝语义自洽；如需桶面全复原＝quarantine 件逐件移回桶根即可＝可逆登记）＝§三-6 旧钉复现＋§三-2 甲路径同表复现即回退验证面。）

---

## 四、候裁单列与登记项知会

**候裁单列（真分歧才列）**：

- **C-1（必列）＝S3 证据件写盘体量**：甲乙丙三案与利害见 §二 S3；乙丙任一选定＝触 60-gates.md 出口②形态条款＝自动升 C1 契约整改（契约票先例）＋publish.py 消费面随动另票；甲案＝本票闭集不变零追加。裁前零施工。
- **C-2（rev 轮新增必列）＝分拣隔离与 60-gates 出口②③条文语义（证据位置口径）**：出口②表行载体列＝.collab/evidence/gates/<日期>-<脚本>-<短摘要>.json（字面＝桶根层件名形态）；出口③三轴表行＝次数来源＝evidence/gates/ 累计（字面不限层级）。分拣隔离把可判他案件移入 evidence/gates/quarantine/ 子层＝**件仍在 evidence/gates/ 域内但离开稳态计数射程**＝两种读法：读法一（本票采纳）＝条文只约束写盘落位与计数来源域（桶根），子层隔离＝数据归位到判据本有射程（各工作区各算各账＝出口③本意），零触条文；读法二＝「evidence/gates/ 累计」按递归全域读＝隔离即改计数域＝触条文。两读法各有咬面（读法二成立则桶内一切子层机制——含 aggregate/ 双保险设计——皆需契约背书），架构席不自行裁：施工与验收按读法一推进；若 QA/产品席裁定采读法二＝升 C1 契约整改（60-gates.md 改动走契约票先例）＋本票 S2 暂停呈裁。利害＝读法一零契约成本即刻可施工；读法二先改条文再施工＝工期加一契约票往返。
- 其余无真分歧候裁：窗口口径（整日粒度）／归档触发（已覆盖＋非同日两判据）／隔离出账稳态口径（含回退轮回升一拍随注）＝§二 已给机械判据与等价性论证＝设计规格非裁项；若 QA/产品两席审出反例＝按 H-0 分支呈裁。

**登记项知会（已裁登记／非本票射程·随收口知会）**：

1. 观察账（.scratch/2026-11-18-观察账-闸全量扫描临界区时长-v1.md）销账续账归本票收口＝收口登记件引 §三-1 读数对其「单次提交临界区超 10 分钟」开查触发条件做反证（十秒级达标＝该账时长维度闭合；候选三跨工作区 IO 面仍挂原账）。
2. GTFAST 取证目录（GTFAST-timing／SWB-GTFAST-build）＝本票基面对照证据，随本票收口一并处置（呈裁简报三在册）＝归主理人收口动作，本席与工程师零拆。
3. 桶 41GB 盘级卫生（压缩/清理/分层存储）＝主根盘卫生另案候排（本票零删字节＝S2 只移不删）。
4. GTFAST 候补池 §四-7「取证桶用毕即拆」纪律落点（席位规程＋收口检查单＋可选卫生机检）＝百工侧职权射程，本票零落纪律条款。
5. 本仓提交权归一在册（席禁 git 写·投递归主理人）＝本票全程遵此（起草段两文件只落盘）。
6. worktree 侧证据桶独立性随注：EVIDENCE_DIR 随 ROOT 解析＝各工作区各桶各聚合互不涉＝S1/S2 改动天然 per-root（run-gates.sh 同文件共享 checkout＝代码随链走，桶数据随根走）。
7. 「各工作区侧桶账自洽」＝票外（11:12 裁定四随改）＝候领制下主根无法代验＝归各工作区会话自证；本票只闭合 §三-8 主根侧三读数。将来其它项目 worktree 遗落主根件＝同款流程复用（S2-a 分支集现读自动入集＝通用规格已落，非一次性脚本）。
8. 百工 worktree 侧桶 367 枚／fuxi 侧 7 枚现读在册（§〇-8）＝认领后其账由该侧闸续算＝主根零代劳零落件（§二 S2-b 禁动面）。

---

## 五、回执与链条

起草回执＝仓根 .collab/receipts 桶「2026-11-19-SWB-GTBLOAT起草回执-架构席-v1」件（裸写·本席出）：含开工读数照登（HEAD 40 位／分支 main／脏面 M1＋A1＋??33／NO-INDEX-LOCK／worktree list 五条）＋基线现跑读数（load_history 微基准 322.0s 复跑对照工程师 294.3s／空暂存 386ms／真暂存 304.6s／桶计数 12,833＋41GB／聚合探针 1.46MB-7ms）＋票面 blob＋行数＋自靶 exit 0 读数＋§四 候裁一项与知会六条转录＋纪律申报（零 git 写／落笔前后红线自查）。

链面＝票面笔＋起草回执笔（起草段两笔封顶·投递归主理人唯一链面操作员）→双席独立审（QA 席＋产品席 fresh eyes）→会师→rev（如有修单）→放行→工程师施工段（笔数随放行另计·代码面两枚＝run-gates.sh 改＋gate-bucket-triage.py 增＝一笔或两笔案型随放行定）＋工程师回执笔→主理人执行面（S2-②隔离批次＋S2-③分拣清单登记笔＋投递＝三读数留痕）→QA fresh eyes 全实跑（§三逐条复现＋对抗例：对抗一「等价性活性」＝scratch 假树注入一枚必咬中的历史件形态（如带 exit 3 的 spec 件）必使 E-3 聚合读数与全桶读数同现＝两路径任一漏读即红；对抗二「归档不丢史实活性」＝归档后删聚合件强制回退路径＝三表重算（桶根＋archive/ ＋quarantine/＝rev 轮口径）读数仍全等于分拣归档前全史基表（回升一拍随注＝对账差值在册）；对抗三「回退路径活性」＝假树 revert 后旧 load_history 对未归档桶复现旧读数；对抗四「分拣判据活性」＝scratch 假树注一枚必属他案独段 commit 形态件必被分入 quarantine 对应子层＋注一枚不可判件必留 legacy＝误归即红）→收口登记（含观察账销账续账随笔＋GTFAST 取证族处置呈请）。

D-95 分段落笔：起草段＝**票面一笔＋回执一笔＝两笔封顶**；rev 段＝**票面 v2 一笔＋rev 回执一笔＝两笔封顶**；施工段随放行另计不预占；本席起草段与 rev 段止于此。

---

## 六、落款（起草席自查读数·2026-11-19·arch-swb-gtbloat）

- 开工 HEAD 实测＝335dbbe86a63a98d19a1bdfbdeac3533ff5ae71d（链顶现读·分支 main）；脏面＝board 计划 v2 一枚 M＋A 一枚＋?? 33 枚＝照登零碰零带入；锁面＝NO-INDEX-LOCK；worktree list 五条照登。
- 票号续位＝.scratch/tickets 域 grep GTBLOAT 零命中现跑；.collab 域命中＝H-0 裁定／收口登记／QA 判词／呈裁简报四处＝案号预留在册＝新建 v1。
- 基线现跑在册：load_history 全桶微基准 322.0s（件数 12,833／specs 20／坏件 1／bypass 250）；空暂存 --staged 386ms exit 0；真暂存 --staged 304.6s exit 0（造靶复原两步在册）；桶 du 41GB；聚合探针 1.46MB 载入 7ms；run-gates.sh blob c2918140 对链顶现算全等；钩子 blob 02d30d01 对 GTFAST 新钉现跑全等；60-gates.md blob b68cbfc7 对链顶现读全等。
- 靶检自咬＝python share/check-pointers.py --target 本票面仓根相对路径 exit 0 零 BLOCK（落笔后现跑在册回执；本票面零反引号＝零可提取指针＝OA-D6-4 案型自查）。
- S2 射程随修随登（2026-11-19 当日两度转引两笔时间线）＝10:58 转引（迁册设计）→ 11:12 再裁（分拣候领制取代迁册）＝本票 S2 按 11:12 口径落笔；本席复跑对照＝主根桶 12,836／百工侧 367／fuxi 侧 7 现读＋400 枚 commit 字段归属抽样（§〇-8）＝可判他面窄不可判为主＝候领制预期终态。

（rev 轮随注（arch-swb-gtbloat·2026-11-19）＝本 v2 取代 v1。并发口径如实登记＝主理人查盘所见 v1 旧值 b9525bc1／132 行（未含两度转引）；本席随修轮已于查盘同窗把 v1 就地修至 da665555／148 行（含 §〇-8／S2 候领制全节／判据⑧／声明面 4-5＋7＝当轮现跑自证在册）——两读并存不追因＝rev 轮不再争 v1 现值，改以本 v2 为受理工件。v1（da665555 态）→v2 差异逐处＝①标题行「归档分层」改「legacy 分拣候领制」＋文首取代理由行新增（清单六取代自证）；②§一 声明面 1-2 随 v2 与 rev 回执校平（v1 盘上保留作史不入投递面）；③§二 S1-b 回退重算两表改三表＝**含 quarantine/ 层**（清单二校正＝流水是史实）＋回退轮计数回升一拍随注新增；④§二 S2-a① 分拣清单增按日聚合汇总行＋commit 字段写盘侧 L530 实读随注＋分支名参数化措辞收紧（清单一a/四）；⑤§二 S2-a② 隔离层两口径拆写＝稳态不入射程（与 aggregate/ 同款形态坐实）／回退重算含之（清单二）；⑥§二 S2-e covered_files 折叠口径随分拣时点重定基线写明（清单二）；⑦§三-8 末句改升 C-2 明示；⑧§四 候裁新增 **C-2 证据位置口径两读法**（清单五＝呈选项利害不自行裁）＋非裁项行补隔离出账口径。其余 v1 内容零动＝S1 主体（聚合四轴/原子写/续算点/等价性论证）／S2-b 禁动面／S2-c 工具件／S2-d 归档口径／S3 甲乙丙／判据①-⑦与⑧前三读数／H-0 分支／灰度回退／§四知会八条／落款读数族照旧；rev 回执＝仓根 .collab/receipts 桶「2026-11-19-SWB-GTBLOAT票面rev回执-架构席-v1」件。）