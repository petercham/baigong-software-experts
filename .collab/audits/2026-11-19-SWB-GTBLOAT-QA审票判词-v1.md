# SWB-GTBLOAT · QA 独立审票判词＝fresh eyes 票级审（与产品席互不读·会师归主理人）｜v1

审票席＝qa-swb-gtbloat-rev｜日期＝2026-11-19｜受理工件＝票面 v2（.scratch/tickets/2026-11-19-SWB-GTBLOAT-裁决段证据桶读取瘦身与聚合索引历史归档-v2.md＝153 行／blob 2cc046f23cd1d186d4fee5c3162cdd1161fa654e 现算全等 rev 回执申报值；v1＝148 行／da665555 现算全等＝盘上作史参照并存）＋起草回执 v1＋rev 回执 v1。本席全程只审不裁、零 git 写操作、证据桶只读零拆零移零隔离；全部结论当轮现跑，未引用产品席任何判词。

## 一、开工三读数（当轮现跑照登）

- HEAD＝124a3f6cda1201557fe027cc0ad7f9935f1826f6（开工现读＝分支 main 现读；对派单链笔 96bbca8e／124a3f6c 全等）。
- 中段链面漂移如实登记＝本席取证窗内主理人落两笔：07ec7a39（票面 v2 笔）＋dbd144ae（rev 回执笔）＝本席判词对账基面随动改为链顶 dbd144ae451d2336af09e1a3a9202b3f0c635d7b（收工复跑对钉全部在 dbd144ae 现算，见审五）。
- 脏面＝M 恰一枚（.collab/board/2026-11-17-五份复盘合流与下一轮迭代计划-v2.md 他案在飞·零碰零带入）＋?? 散件群 33 枚照登零带入＋rev 回执暂存 A 一枚（主理人链面动作·非本席）；本席全程暂存面零动作。
- 锁面＝NO-INDEX-LOCK 现读（.git/index.lock 不在盘）；本席只读 git 命令族＝天然零写锁。
- worktree 现读五条＝主根挂 main＋qa_t10_dy（detached·prunable）＋D:/cs1-wt（detached）＋.wt 下百工侧挂 baigong-software/main＋fuxi 侧挂 fuxi/main。

## 二、审一＝S1 语义守恒实证（本席主战场）

现读对象＝链顶 share/run-gates.sh（blob c29181404b266cee2cce1259219b0c646c1e716c 现算全等·见审五）load_history L375-404 逐行对票面 v2 §二 S1 聚合四轴设计逐轴对拍：

1. (spec,run) 去重轴＝seen_runs 持久化为 seen_pairs＝四轴闭集存续，载入基态后续算用持久集做键＝语义存续（绿）。
2. bypass 整件排除（L390 doc.get bypass 真即 continue）＝v2 取径内 bypass continue 不计次＝计数语义存续（绿）；covered 归属见漂移清单 Y1。
3. 坏件跳过不删（L388-389 continue＝流水是史实）＝v2 坏件 continue 且不入 covered＝当轮不参与、件留存、下轮窗内再遇＝与旧路径每轮重读重跳过＝结果逐位等价（绿）；本席现跑坏件恰一枚＝.collab/evidence/gates/2026-11-12-check-pointer-closure-exit1-at12-48-42.json（14,044,013B 残损）＝每轮窗内重读代价 14MB 级＝秒级不入 60s 红线射程（绿）。
4. exit 首见入集（L401-403 仅 (spec,run) 新见时 add doc.get exit）＝v2 exits 轴持久化＋窗续算沿用同键＝逐位等价（绿）；E-3 消费面 L507 读该集零动（绿）。
5. exclude_names 参数语义＝现读调用点唯一＝L493 load_history(set()) 恒空集（grep 现跑＝全仓无其它调用方）＝参数存续＝窗过滤名 ∉ exclude_names 存续；被exclude 件不入 covered＝下轮重新判定＝与旧路径每次调用重判一致＝零漂移（绿）。
6. 同 run 跨轮重复件＝出口②文件名带时刻（L525-526）＋同 run 件同轮全在场（唯一写者·load_history 先于写盘段 L493＜L512＝本轮件不入历史）；崩溃残组件＝covered 只在轮末 S1-c 原子写＝残组件留在未覆盖窗由下轮整组折叠＝与旧路径读到同批在场件＝语义对等（绿）。
7. 聚合件自污染＝聚合件 .json 后缀＋居 aggregate/ 子层＝桶根非递归 listdir（L382 os.listdir 现读坐实）＋名过滤双保险＝主路径永不见聚合件（绿）。

独立等价性探针（自造 .scratch/SWB-GTBLOAT-rev-qa/qa_equiv_probe.py，不复用起草 lh_micro）现跑对当轮真桶：

- 甲路径＝逐字折叠体全桶读＝桶 json 12,841 枚／elapsed 398.0s／specs 20／counts 总和 20,973／坏件 1／bypass 250／去重对 20,973（与回执值 322.0s/12,833/20,960/1/250 同族＝间隔期自然增长＋IO 波动并存不追因＝回执忠实性见末节）。
- 乙路径模拟＝同件流按日界分 28 轮增量折叠（covered 前缀延拓＝S1-b 窗续算同构）＝DIFF_counts 空集／DIFF_exits 空集／seen_pairs 集合全等（20,973＝20,973）＝两路径逐轴 diff 空集＝聚合续算设计对本桶面语义守恒实证成立（绿）。
- 真聚合件按 S1-a 形态落本席取证目录（不落真桶）＝1,485,928B／json 载入 best 4.1ms mean 8.1ms＝对回执探针 1,457,068B/7ms 全等量级（绿）。

语义漂移点清单＝无行为级漂移；三处口径含糊列黄（Y1／Y2／Y3，见对抗臂①汇总）。

## 三、审二＝性能判据可达性

- 真暂存端到端 ≤60s 结构性可达＝成立（绿）：聚合载入 4-8ms（本席现跑）＋靶检循环段 9.259s（GTFAST QA 判词①在册·本票零动扫描段）＋未覆盖窗秒级（当轮新件＋bypass 群 0.42GB＋坏件 14MB＝现跑取证）＋bash 壳与钩子链开销＝预算内；本席空暂存现跑＝GATE PASS exit 0 real 436ms（回执 386ms 同族）。
- 等价性判据②两路径 diff 空集在归档后复跑口径＝可执行（绿）：甲基表在隔离后桶面冻结一次；归档后乙对甲基表复拍＝甲旧代码不再对归档后桶面重跑（旧两表读法会漏 archive 层）＝票面「对甲路径基表」措辞正确；本席乙路径模拟已证窗续算对冻结基表逐位等。
- 回退活性判据可造靶＝成立（绿）：scratch 假树篡改 history-v1.json 即触发三表重算面（判据④形态）；本席假树已跑通三表归并读数面（见对抗臂③）。
- 一处口径缺口＝聚合首轮建立尖峰与本票判据①计时次序未写死：部署后首轮＝聚合缺失＝全桶重算≈398s（本席实测现值）＞60s 硬线；若判据①造靶计时恰为该首轮＝机械假红。随注 Y2。

## 四、审三＝S2 判据活性对抗臂

- 独立归属抽样（对抗臂②本体＝.scratch/SWB-GTBLOAT-rev-qa/qa_attribution_probe.py：换种子 20261119／N＝120／判据收窄为 merge-base --is-ancestor 分支独有段口径＝v2 口径）现跑读数＝多分支包含 114／单分支包含 main 3／单分支包含 baigong-software/main 1／不可判（hits 空）2＝对起草席 400 枚种子 7 预演（多含 380／单含 14＝main 9＋baigong 5／不可判 6）比例忠实（单含率 3.3 对 3.5％；不可判率 1.7 对 1.5％）＝预演忠实性成立（绿）。
- hits 空两枚深挖＝其 commit 反查 git branch --contains 全分支＝命中 backup/fuxi-full-20261029＝该分支不在工具现读闭集（回执登记在册）＝按 v2 判据落不可判 legacy 留主根归档层＝预期终态非缺陷（绿·如实登记）。
- 隔离即出账与现实现自洽＝坐实（绿）：load_history 桶根 os.listdir 非递归（L382 现读）＝quarantine/ 子层件天然不入稳态射程；publish.py gate_a2 非递归 listdir＋json 后缀过滤双保险（L433-443 现读）＝零冲击；check-collab-buckets 扫描深度＝.collab 一级 listdir（L110-115 现读）＝gates/ 之下任何子层不落射程；全仓 grep 消费方＝仅 run-gates.sh＋60-gates.md 文字两处＋publish.py gate_a2 三处（现跑核清单与票面 §〇-4 全等）。
- triage 工具件＝盘上不存在（现读 share/gate-bucket-triage.py＝不在＝预期内·新增件归施工面）；fail-closed exit 4 与只读约束可验性＝判据可写成施工后 PATH 剥离＋桶不可读两例（绿·待施工段复现）。
- 施工随注 Y4：quarantine 子层名带归属分支名含斜杠（baigong-software/main）＝落盘为两级嵌套目录＝v2 三表归并实现必须递归收集叶目录（本席假树首轮单层列目录漏件、修正递归后全中＝实证提醒转工程师）。

## 五、审四＝验收判据逐条机械判定性（八条）

- 判据①端到端计时＝可判（机械硬线＋十秒级目标登记）；靶造复原成对路径成立（临时 md 造靶→单 pathspec add→提交或 restore 复原登记）；唯 Y2 次序口径需补（见上）。隔离动作不入审票段执行＝判据已写成主理人执行面形态（合规）。
- 判据②等价性两路径 diff 空集＝可判（甲驱动 lh_micro 复用＋乙聚合读数＋冻结基表二拍）；本席当轮已预跑同构＝现值 diff 空集。
- 判据③缺省全套闸 27,051 族差集零＝可判且本席已现跑预验＝bash share/run-gates.sh --no-write 现跑＝GATE PASS exit 0／发现总数 27,051 与基面逐位全等（real 447.8s＝含本席并发探针 IO 竞争＝同族不追因；该读数反证 PY 段热点＝与票面归因吻合）。
- 判据④fail-closed 三例＋回退活性＝可判（PATH 剥离／假树路由表／假树篡改聚合件三靶皆可造；ALLOW_GATE_DOWN 使用计数 0 申报可数）。
- 判据⑤桶面机检零冲击＝可判（子层生成后 check-collab-buckets 复跑＋gate_a2 当期取径复跑＋桶根计数＝原件数＋3 目录数）。
- 判据⑥钩子钉零扰动＝可判且本席现跑＝.git/hooks/pre-commit hash-object＝02d30d01e53f9c7b38803dfbd1d599f9a23c4d16 对 GTFAST 新钉全等；check-hook-health.py EXPECTED_HOOK_BLOB 行现读同值（L47）。
- 判据⑦链面闭集＝可判（diff --name-only ⊆ 声明面＋禁动面 ls-tree 两态对读）。
- 判据⑧三读数闭合＝可判（桶根复扫他案命中 0／quarantine 分层计数＋抽样反查 N≥100／decisions 登记件件数对全等）；本席抽样外推＝可判他案件约百余枚量级（12,841 × 1/120≈107）＝N≥100 近全量＝机械可行。

## 六、审五＝禁动面与链面闭集（对收工链顶 dbd144ae 现算）

- share/run-gates.sh＝c29181404b266cee2cce1259219b0c646c1e716c 对开工基线全等（git ls-tree 现读）＝起点 blob 对钉存续（绿）。
- 60-gates.md＝b68cbfc7df9f20a2ae41c86499863793f0ec9dfa 全等（绿）；.git/hooks/pre-commit＝02d30d01 全等（绿）；share/install-hooks.sh＝ad14f0d162c65472ea4983edebbbc5f1bab5f7f0 全等（绿）；share/baseline-sot-dup.json＝2c44d339890811304d7f1cd3a355d88ee547e5e6／share/baseline-seat-decl.json＝f6171c7db03cf79529c89795fd243e2a78a22b12 全等（绿）。
- SCRIPTS 清单存续＝现读 L167 十一枚在册未变；triage 不入围猎核对＝清单内无 gate-bucket-triage＋盘上无该件（绿）。
- 三包零碰＝本席零触；publish.py 现读只读取证（blob db621eaf66d3bafefc36ef5ef514e82eda58b47b 现算登记·非禁动钉值＝知会读数）（绿）。
- 票面 v1 blob da665555／148 行现算全等；v2 blob 2cc046f2／153 行现算全等＝两版并存 append-only（绿）。

## 七、审六＝对抗臂读数汇总

对抗臂①（聚合对 load_history 语义漂移专臂）＝行为级零漂移（见审一逐要素对拍＋等价性探针 diff 空集）；口径含糊三枚列黄：

- Y1＝v1/v2 §二 S1-b 同句自相矛盾＝「bypass 件 continue 且不入 covered——bypass 件不计次但可入 covered」前后半句对 covered 归属互斥；两读输出等价（bypass 恒不计数），但 covered_files 集与 stats 知数机械不同、判据②照测不出＝施工前措辞收窄（荐：bypass 入 covered＝免每轮重读 0.42GB 群）。
- Y2＝判据①计时与聚合首轮建立尖峰次序未写死＝首轮 398s 级尖峰若撞上造靶计时＝机械假红；补一句口径＝判据①前先跑一轮缺省/暂存预建聚合（尖峰轮读数登记知数行），造靶计时在聚合在场后。
- Y3＝v2 S2-e「此后每轮…S2-a② 隔离臂幂等复扫常态运行」射程未定＝若解读为全桶根逐件重判归属＝每轮万余枚 × 分支数 git 调用＝直接破判据①；且闸内移件与 S2-b「隔离动作＝主理人执行面」职权边界相抵；收窄口径＝复扫仅当轮新写件＋未覆盖窗（当轮新件恒为当前根分支段＝实际零动作）＝措辞写死。
对抗臂②（归属独立抽样复跑）＝见审三＝忠实性成立＋不可判两枚成因坐实（backup 分支不入闭集）。
对抗臂③（顺序违反推演＋回退可逆性＝.scratch/SWB-GTBLOAT-rev-qa/qa_order_adversary.py 假树现跑）＝
- 甲序（S2-e 写死序＝先隔离后建聚合）＝隔离 1 枚／稳态读数他案贡献出账／v2 三表回退＝回到分拣前全史（回升一拍形态＝与票面声明一致）；
- 乙序（违反序＝污染面建聚合后隔离）＝稳态读数仍含他案账＝对甲序基线差非零＝判据②基线对拍可机械检出（判定1 差值 1）；v2 三表回退面在回退轮与全史基表同值＝回退轮检不出乙序＝稳态对冻结基表是唯一检出点＝判据②必须含「聚合在场态稳态读数 vs 冻结基表」这一拍（票面已有＝坐实）；
- 灰度回退可逆性＝成立：改动笔 revert＋aggregate/ 与 archive/ 删层（archive 先移回桶根＝史实零损）＋quarantine 存续＝旧 load_history 桶根非递归不见 quarantine＝语义自洽；quarantine 逐件移回桶根即全复原（可逆登记在册）。

## 八、总判与回执忠实性

总判＝**可放行随注**：S1 语义守恒实证成立（本席独立探针两路径逐轴 diff 空集）；性能判据结构性可达（含首轮尖峰口径随注）；S2 三步闭集与现实现自洽坐实、归属判据抽样忠实；禁动面与链面闭集全部对钉全等；八判据逐条机械可判定。放行随注三枚＝Y1 Y2 Y3 措辞收窄建议在 rev 修单或施工放行条件内落实（均不改设计本体、不改判据硬线）；Y4 为施工实现随注；Y5 观察项＝聚合件 seen_pairs 随轮次线性增（当轮 1.49MB 载入毫秒级＝无近期危害＝不收口判据＝挂观察）。

回执忠实性＝起草回执与 rev 回执申报读数全部对拍：对钉六枚（run-gates／60-gates／钩子／install-hooks／两基线）全等；桶计数 12,833→12,841→12,847 自然增长族并存；微基准 322.0s 对本席 398.0s 同族（IO 波动先例口径）；坏件 1／bypass 250／specs 20 三值全等；聚合探针体量与载入毫秒值同量级全等；桶面三值（主根 12,836／百工 367／fuxi 7）本席复核主根桶增长族相符（worktree 侧本席未复读＝如实登记未验项）；400 枚预演比例经本席换种子独立复跑忠实；缺省基面 27,051 本席现跑逐位全等。无红旗。

纪律申报＝本席全程零 git 写（add/commit/restore/stash 零笔·只读命令族照登）；证据桶只读零拆零移零隔离（三枚全桶探针均只读＋聚合副本落 .scratch/SWB-GTBLOAT-rev-qa/ 取证目录不落真桶）；三包零碰；.workbuddy 零碰；他案 worktree 检出目录零落件零读内容；假树取证用毕即拆（fake_tree cleaned 读数在册）；取证族落位＝.scratch/SWB-GTBLOAT-rev-qa/（探针三件＋读数五枚＋聚合副本一枚）；同席多实例＝不存在；禁检索自救遵行＝全部读数本地现跑；受控查证豁免未动用。

（QA 审票段止于此＝判词一枚落盘；投递归主理人唯一链面操作员；判词权按表2-3 归签字席，本席出票级验收与审计读数面。）
