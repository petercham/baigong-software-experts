# SWB-GTFAST QA 审票判词 v1（QA 席 qa-swb-gtfast-rev·fresh eyes 独立审·判词落 audits 桶·投递归主理人）

> 被审件＝.scratch/tickets/2026-11-18-SWB-GTFAST-闸提交门靶检与周期全量与钩子动态根扫描域划界-v1.md（现算 hash-object＝262ccecaa68afa689c45572db7e1ac6df142eabe 全等票面钉·wc -l 现跑＝178 行全等）；回执＝.collab/receipts/2026-11-18-SWB-GTFAST起草回执-架构席-v1.md（现算＝b5f6ea74848b9033a6c5895de661e929c3c52e7a·50 行全等）。审＝只审不裁·全程零 git 写（add/commit/amend/stash 零笔）·只读 git 不禁·未读产品席判词。

## 〇、开工三读数＋锁态（当轮现跑照登）

- HEAD＝9fb792673ac0652b481b6e5dfe3ada35852414d2（链顶现跑＝回执笔在链＝票面笔 3f69a775＋回执笔 9fb79267 两笔封顶兑现现读）；分支＝main 现读。
- 脏面＝git status --porcelain 去 ?? 恰一枚＝仓根 .collab/board/2026-11-17-五份复盘合流与下一轮迭代计划-v2.md（M·他案在飞·零碰）；?? 散件群照登零带入（.py 散件／.scratch 取证族／worktree 侧台账散件等）＝与起草轮 32 枚同族＋本席取证新增。
- 锁态＝NO-INDEX-LOCK 现读（.git/index.lock 不在盘）；core.hooksPath 三读之 --get-all 现跑空 exit 1＝键净·钩子唯一经共享 .git/hooks。
- worktree list 现读五条＝主根挂 main＋qa_t10_dy（detached prunable）＋D:/cs1-wt＋两业务包 worktree＝wtgate-verify 已拆（回执笔登记）＝票面开工照登六条系起草轮锚态，非现态。
- 取证面＝仓根 .scratch/SWB-GTFAST-rev-qa/（本席新建）；三包零碰；任何 .workbuddy/ 记忆面文件零碰（含被咬件本体只读引用）。

## 一、逐审项红黄绿表

| 审项 | 判 | 关键读数（全部当轮现跑） |
| 票面/回执对钉忠实性 | 绿 | 票面 262ccecaa…／178 行；回执 b5f6ea74／50 行；链笔面恰各一枚（git show --stat 现读）；改动面七枚起点 blob 对开工基线全等现算（run-gates 11a6f4d4／entity 1f4be322／lint d963f5a2／closure 717a2adfe／pointers 33781b31／install-hooks f71474ac／hook-health 7fd83074）＝§一 回填值全对 |
| 逐枚耗时复跑 | 绿（读数并存） | 本席 lint 单枚复跑 real 2m19.872s exit 1 发现 6353 行（与基线 perf 件 6353 分项全等）＝主理人 141603ms／起草席 1m34s／起草席复跑 1m45.6s／本席 139.9s＝四读数并存 IO 波动不追因；csot 单枚 0.564s；hook-health 0.254s；§〇-2 转引表对 per-gate-timing.txt 全表逐项对读全等（十一枚合计 167395ms＝票面约 168s 成立；lint 占比 84.6％＝约 84％ 成立） |
| 判据①提交门临界区 ≤60s | 绿（可达·见红旗定性专节） | 靶检路径下 lint 只吃暂存 ∩ md/txt＝枚级毫秒；预算＝豁免九枚约 5.5s＋pointers 索引面约 10s＋靶化三枚秒级＋进程启动与写盘≈20s 量级；临时验证工作区＝全新 checkout（无 .scratch 堆积面）＝扫描面天然只有 tracked 面；造靶定义闭合（worktree add＋暂存一枚＋计时）复原路径＝判据⑤ worktree remove＋worktree list 复读在册 |
| 判据②取径不更判据 | 黄 Y2 | lint／closure 判据函数与输出行形制现读＝靶检只换入参文件集＝逐行 diff 方向可执行；惟 check-collab-lint check_l3＝目录级分组判据（编号唯一性）：靶集下配对不全则该行整体不出＝靶检输出是缺省输出子集而非对称等集；判据文应写死子集方向（靶 ⊆ 全扫属该文件行）或声明 L3 目录级案型随向豁免，否则收口轮按对称 diff 跑会假红 |
| 判据③全量移位周期闸可对账 | 绿 | 差集闭集现读坐实＝check-entity .workbuddy BLOCK 恰一枚（现跑复见）＋closure 输出 .workbuddy 命中 18 行（起草 perf 件 grep 现算）＋lint 包内卷宗族 WATCH 行（本席 S1-a 模拟补丁实跑＝6353 降至 14，消减 6339 行逐行可归因）＝三项差集闭集与 §三-3 登记一致；FINDING_RE 口径基面 33391 系起草当轮值（口径随动先例在册） |
| 判据④钩子钉随正 | 绿 | 现钩子 hash-object＝8b785770…全等于 check-hook-health.py L47 EXPECTED_HOOK_BLOB 现读＝存续态坐实；票面 S4-a 围栏 L106-114 本席逐字节重建＝02d30d01e53f9c7b38803dfbd1d599f9a23c4d16 对票面钉值全等＋对起草盘件 new-hook-fenced.sh（609 字节）cmp 全等；bash -n 语法净；install-hooks.sh L86 HOOKS_DIR 锚行现读＝置换锚存在；幂等已是最新分支 L117 在册 |
| 判据⑤worktree 侧零触主根 | 黄 Y3 | 机制面绿：新钩子 GATE_ROOT_DIR 随 --show-toplevel 解析＋旗 git -C D:/cs1-wt rev-parse --path-format=absolute --git-path hooks 现跑＝主根与 worktree 同读数（共享 common dir）＝S4-b 两态可行性本席当轮重跑复证；惟判据文「worktree list 复读回到开工照登六条」＝陈旧计数（wtgate-verify 已于回执轮拆除·现读五条）＝应改「回到施工 ANCHOR 照登数」 |
| 判据⑥绕行归零复验 | 绿（随注 Y5） | S1-b 划界归零现跑实证＝本席补丁副本工序：check-entity 现跑 BLOCK 恰一枚（行 34 与行 51 日期字面命中 pattern=date count=2＝与票面 §〇-4 全等复现）；L177 剪枝闭集四项锚串恰一枚（断言计数现跑＝1）补第五项 .workbuddy 后副本现跑 exit 0 BLOCK 归零＝「划界后假阳性归零」机械判据写死且可执行坐实；惟「当日新增」计数口径＝证据桶文件名日粒度，收口窗基线快照差计未写死＝建议补「收口点计数快照」一句 |
| 判据⑦fail-closed 三例 | 绿（随注） | --staged 下 git 不可用＝S2-b 写死 die_infra exit 4 不落全扫不静默＝语义闭合；--target 目录 exit 2＝check-pointers L516 die_usage 先例现读在册，S2-d 承引措辞在册；损坏路由表 exit 4＝run-gates 路由表 json 解析失败 exit 4 在 60-gates §六 表内＋PY 段兜底 except 按 4 现读（L539-542）；可操作性随注：scratch 假树需预置 share/ 十一枚脚本＋三分类目录任一才能过定位段，fixture 准备量应在施工回执写明（非阻断） |
| 判据⑧链面闭集 | 绿 | 申明面 3-9＝恰七枚全落 share/＝与 diff --name-only 过滤前缀同域＝申明明细闭合；10 钩子盘上件非链面／11 回执件出 share/ 前缀不碰撞；禁动面对钉现算＝60-gates.md b68cbfc7／baseline-sot-dup 2c44d339／baseline-seat-decl f6171c7d／reconcile-daily ff1e4d87 四枚全等 |
| S4 核钉流程与 WTGATE 零冲突 | 绿 | S4-c 五步流程在册（改器→重装→现算对钉→L47 恰一行置换→改后现跑 exit 0）；WTGATE 已落改动现读＝check-hook-health 已含 git_hooks_dir 函数（L77）＝S4 只碰 L47 常量行不碰定位臂＝零冲突坐实；install-hooks 与 run-gates 无共享改动面 |
| S3 挂接位与候补池无重叠 | 绿 | reconcile-daily 只引用不改动在册；§四-6 证据件瘦身归另票候排＝与 S3 挂接登记无重叠；WTGATE 收口登记候补池随注行（取径两制统一／证据件瘦身）现读＝两行均候排非本票射程＝无冲突 |
| 候裁 C-1／C-2 呈现 | 绿（不代裁） | C-1 两态咬面呈现经代码现读核＝L238 基名索引 walk 现文确含 .workbuddy（索引面未剪＝背书现状）＋后缀索引已排 .scratch 族注释现读＝呈现无失真；C-2 出口①语义面判据本体＝归决策者闸呈现合规 |

## 二、红旗定性专节（主理人转引新实测复核＋定性）

- 转引计数复核：主仓根 .scratch 全量 168347 枚＝本席 find 现跑全等；全仓 md/txt 158946＝本席现跑全等（回执 158942 系轮间漂移 4 枚＝本席取证目录生长所致·不追因）；最大堆积 FX-U39-qa 26629／FX-U15-qa2 10484／FX-U18-qa 9821＝本席现跑逐枚全等。
- check-collab-lint L153-154 现读＝os.walk 整仓根·剪枝闭集仅 .git／__pycache__ 两项＝转引全等；入扫 md/txt 枚数本席裸 walk 现跑＝160917。
- S1-a 判据缺陷指称＝本席判定不成立（对抗臂①专臂实跑）：按票面 S1-a 现文机械判据做补丁副本（不碰真件·副本落本席取证目录）现跑＝入扫 160917 降至 20845（−87.0％）·lint 发现 6353 降至 14·lint 耗时 139.9s 降至 65.7s。根 .scratch 不剪＝票面明文言＝设计如此（票面桶豁免行 .gitignore L59-64 现读＝/tickets/ 段恰是 EAC-L2 判据靶面，根面全剪＝判据自灭）。
- 验收判据①在此判据下是否结构性不可达＝否，反证在册：--staged 模式下 lint 走靶检（暂存 ∩ md/txt＝枚级毫秒），根 .scratch 面根本不上提交临界区；60s 预算加总实测族约 20s 量级＝结构性可达。主根 .scratch 残留面（20276 枚 md/txt·非嵌套部分）压的是缺省全扫＝周期闸侧＝S3 射程，且其大头＝历批次 QA 取证桶收口未拆＝卫生问题非判据缺陷。
- 定性：不构成阻断放行级红旗＝黄旗随注（Y1）：建议票面随注一行「根 .scratch 残留面仍主导周期闸 lint 耗时·取证桶拆解归候补池 §四-6 同族另案」。
- 口径校正核（跨年说）：「跨年」字样在票面与回执两件全文 grep 零命中＝票面归因措辞未被带偏；本席 find 最老日期名目录 mtime＝2026-11-05＝本月内＝事实形态＝历批次收口未拆（与主理人复核一致）。

## 三、对抗臂读数

- 对抗臂①（S1-a 判据文对拍 lint 代码现文＋主根 .scratch 专臂）：见红旗定性专节全读数；补充＝§〇-2 实读勘正对拍＝check-entity L177 四项剪／check-ticket-reconcile L295-298 过程域剔除臂／check-pointers L334 与 closure L126 两项不剪＝四处现读全等勘正无虚。
- 对抗臂②（新钩子候选试挂＋fail-closed 语义）：围栏逐字节重建＝02d30d01 全等票面钉＋cmp 起草盘件全等（609 字节）；bash -n 净；非工作区 cwd 下裸跑重建件＝exit 4 出口打印 fail-closed 拒提文案现跑命中＝GATE_ROOT_DIR 取径 fail-closed 语义坐实；未真装钩子（只读评估·.git/hooks 零字节改动）。
- 对抗臂③（禁动面点名对拍声明闭集）：run-gates 裁决段内嵌 PY 段现读＝heredoc 起 L169 止 L543（票面 L157-543＝含环境变量前导段的裁决段整体，口径不矛盾）；S2 锚行 L56-57／L59-71／L144-155 均在裁决段之外＝声明改动面与禁动 PY 段零交集坐实；csot／ticket-reconcile／staged-declaration／provenance／skill-meta／adr／collab-buckets／两枚基线 json／60-gates.md 禁动点名与起点 blob 无矛盾；三包零碰申报与审项全程一致（本席实跑只读）。

## 四、回执忠实性

- 三读数并存登记（转引 141603ms／首轮 1m34s／复跑 1m45.6s）＝忠实在册，本席第四读数 139.9s 补登不追因；两口径包内卷宗计数并存（12602／7530 对转引 8839／6738）＝本席 find 现跑复算 12602／7530 与本席回执引用口径全等＝忠实。
- tracked 1921（回执）对当轮 1924＝链两笔落盘所致漂移＝如实可归因。
- 瑕疵两处（黄 Y4）：回执 §三 登 new-hook-fenced.sh 629 字节＝实测 609 字节（629 系同目录 new-hook-pinned.sh 的字节数＝串件）；回执 §三 引「票 §二 S3-a／S3-b」＝票面重排后编号为 S4-a／S4-b＝回执自身引用未随回执 §四 自称的校平走。hash 钉值／blob／行数均全等，不影响判据基数。

## 五、总判

可放行随注。八条验收判据全部机械可判定（两条随精度注 Y2／Y5＋一处陈旧计数 Y3）；根因三件归因经代码与现跑双对拍成立；S4 钉链三值（现钉 8b785770／新钉 02d30d01／L47 常量）流程闭合且与 WTGATE 已落改动零冲突；主理人转引「S1-a 判据缺陷致判据①结构性不可达」经当轮实跑不成立（黄旗随注 Y1 取而代之）。红旗清单＝零阻断红旗；黄旗六枚＝Y1 根 .scratch 残留面随注＋取证桶拆解另案；Y2 判据② diff 方向精度（子集方向写死）；Y3 判据⑤ worktree 计数措辞改 ANCHOR 照登数；Y4 回执 629 字节串件＋S3-a 旧编号引用；Y5 判据⑥当日新增需收口点计数快照口径；Y6 新钩子体硬字面 python3 与 PY 探测臂并存（与现行钩子同形制无回退·python-only 机器上 127 fail-closed 拒提＝登记不追改）。随注观察：审窗内证据桶 12707→12725 枚／bypass 留痕 150→168 枚＝OA-T1 假阳性仍咬主根＝收口紧迫性佐证（非票侧缺陷）。

（判词完——QA 席独立审毕；判词投递归主理人；本席未读产品席判词；全程零 git 写·share/ 与三包与 .workbuddy 记忆面零字节。）
