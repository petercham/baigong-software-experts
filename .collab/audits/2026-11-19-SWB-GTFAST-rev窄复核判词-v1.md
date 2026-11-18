# SWB-GTFAST rev 轮窄复核判词 v1（QA 席 qa-swb-gtfast-narrow·fresh eyes 只复核 rev 差异面＋R0 修单复跑·判词落 audits 桶·投递归主理人）

> 性质＝rev 轮窄复核＋R0 落链后实效独立复跑（只审不裁·全程零 git 写＝add/commit/amend/stash/reset 零笔·只读 git 不禁·判词只落盘投递归主理人）。复核对象六项＝rev 差异清单对拍／append-only 零回改／R0 修单独立复跑（主判据·禁抄工程师读数）／全套闸差集抽验／R0 越界检查／卫生抽查。取证族＝仓根 .scratch/SWB-GTFAST-narrow-qa/（本席新建·不拆供收口参照）。
> 被核件＝票面 v2（f403bcf7 183 行）＋rev 回执（b0938912 59 行）＋两审票判词（c8bc3e6d 笔投递／78627f36 笔投递）＋R0 改动笔 3fea556f＋R0 回执笔 64cf4c89＋窄放行登记件（盘上在读）。

## 〇、开工三读数＋锁态（当轮现跑照登）

- 链顶现跑＝git rev-parse HEAD＝64cf4c899d74556fcd8392e5954e07d8024c4a44（＝R0 回执笔在链顶·对派工预期全等）；分支＝main 现读。
- 脏面＝git status --porcelain 去 ?? 恰一枚＝仓根 .collab/board/2026-11-17-五份复盘合流与下一轮迭代计划-v2.md（M·他案在飞·零碰零 reset）；?? 散件群照登零带入（含本席新建取证目录）。
- 锁态＝NO-INDEX-LOCK 现读（.git/index.lock 不在盘）；worktree list 现读五条照登（与工程师 ANCHOR 照登数五条全等＝票面 §三-5 v2 校平口径在场）。
- 账面对象对钉现跑＝票面 v2 盘上 hash-object f403bcf7／183 行＝派工值全等；rev 回执 b0938912／59 行全等；产品判词 18cafe31／90 行、QA 判词 a3afd297／55 行＝盘上现算（链上 blob 见 §二）；R0 改动笔 numstat 25/4 现读＋改后 blob 8f64a3b2 现算全等＋起点 blob d963f5a2 存在性现跑坐实；R0 回执件 e499871b／49 行链上盘上双向全等。

## 一、rev 差异清单对拍（复核项一）

对法＝双路：①rev 回执 §一 十三条逐处（位置＋旧文要点＋新文要点＋依据判词项）对票面 v2 现文逐处核实；②链上 v1（git show 3f69a775 件）对盘上 v2 全文 diff 现跑（取证＝narrow 族终端读数），diff 面与回执清单逐处对齐。

- 逐处核实结果＝十三条全在场且指向正确：标题 v2 标记在位／文首取代理由行＋rev 席位日期行新增（＝回执第 1 条）／§〇-2 归因侧重校平段新增含 168,347／146,329／92%／6,075/6,357＝与产品席黄①及两席独立计数一致（第 2 条）／§一-1・2 声明面改 v2 件＋append-only 注＋rev 回执件（第 10 条）／§二 S1-a 保留面收窄重写＝根 .collab 不剪照审＋根 .scratch 除 tickets 子树外剪＋包内段数 ≥2 款存续＋A/B 读数族照登（第 3 条）／§二 S4-a 围栏随注 Y6 一行（第 9 条）／§三-1 造靶甲＋造靶乙双口径＋两层门分别登记（第 4 条）／§三-2 子集方向写死＋对称 diff 禁跑（第 5 条）／§三-3 差集账补第四项＝lint 主根 .scratch 松散面归零 6,075 行口径＋tickets 11 枚保留注（第 6 条）／§三-5 改「施工 ANCHOR 照登数」（第 7 条）／§三-6 计数快照口径（第 8 条）／§四-7・8 候补池两行（第 11 条）／票尾 rev 随注一行＝改动点名处清单（第 12 条）。
- 第 13 条零动确认独立核＝起点 blob 表七枚对钉现跑全等（run-gates 11a6f4d4／entity 1f4be322／lint d963f5a2／closure 717a2adf／pointers 33781b31／install-hooks f71474ac／hook-health 7fd83074）＋禁动面现跑＝60-gates.md b68cbfc7／baseline-sot-dup 2c44d339／baseline-seat-decl f6171c7d／钩子 8b785770／hook-health L47 常量旧钉存续＝除点名处逐段零动坐实。
- diff 全文对拍＝链上 v1 对盘上 v2 的 git diff 改动块＝与回执十三条一一对齐，无清单外改动块（唯一非语义差＝v1 无末换行 v2 带末换行＝行数 178→183 自洽）。
- 决议六项逐项落实核实＝①S1-a 保留面收窄（在位·见上）②判据①双口径造靶（在位）③QA 黄旗措辞并入 Y2 子集方向／Y3 ANCHOR 数／Y5 计数快照／Y6 python3 硬字面登记不追改（四处全在位）④回执瑕疵随正居回执件 §二（629→609 串件随正＋S3-a/S3-b→S4-a/S4-b＝本席独立现跑佐证＝new-hook-fenced.sh 609 字节＋git hash-object 02d30d01 对钉全等＝随正读数真）⑤候补池两行 §四-7/8（在位）⑥其余零动（＝第 13 条独立核绿）。

## 二、append-only 零回改（复核项二）

- 六件链上历史现跑＝票面 v1（git log 单笔 3f69a775）／票面 v2（单笔 cbd67fa5）／起草回执（单笔 9fb79267）／rev 回执（单笔 1af37c34）／产品判词（单笔 c8bc3e6d）／QA 判词（单笔 78627f36）＝各恰一笔 touched＝零回改。
- 链上 blob 对盘上件双向现算全等＝产品判词 18cafe31＝盘上；QA 判词 a3afd297＝盘上；rev 回执 b0938912＝盘上；R0 回执 e499871b＝盘上；票面 v2 盘上 f403bcf7 对 HEAD 零 diff；v1 票面盘上 262ccecaa 对链上全等＝留史未动。
- 各投递笔面单现读＝cbd67fa5／1af37c34／78627f36／c8bc3e6d／64cf4c89 各恰一枚 A 态文件＝面单齐。
- 随登一处＝.collab/decisions/2026-11-19-SWB-GTFAST窄放行登记-R0提速先行-v1.md 盘上在盘在册（内容现读在位·§四 健康账笔在位）但链态＝untracked 未落链＝登记件本体尚欠投递一笔（黄 Y-N1 随注·见 §七）。

## 三、R0 修单独立复跑（复核项三·主判据·全程本席现跑零抄工程师读数）

- 改后单枚现跑主根＝python3 share/check-collab-lint.py --root .＝exit 1／real 0.717s（lint-after-time.txt）＝亚秒级达标（工程师 0.889s／架构席 0.797s／产品席 7.2s 同档族·IO 波动不追因）。
- 发现数＝VIOLATION 14（EAC-L2 14＝根 .collab 面 3＋tickets 子树 11）＝预期全等；tickets 面 11 行对 baseline log（.scratch/SWB-GTFAST-draft/gate-mainroot-baseline.log）提取的 11 行 set-equal True 现跑；本席发现行集与工程师取证件（.scratch/SWB-GTFAST-R0-build/lint-after-out.txt）逐行对拍全等（LINT-FINDINGS-SAME）。
- 入扫枚数现算（iter_files 复用现跑）＝669 枚（根 .collab 面 336＋tickets 面 65＋其余存续面 268＝加和自洽）对工程师 668＝差一枚＝登记件 .collab/decisions/2026-11-19-… 系工程师开工窗后新落件＝可归因漂移非异常；根 .scratch 非 tickets 松散面入扫枚数现算＝0＝保留面收窄谓词生效坐实。
- 起点 blob 副本同窗对照现跑＝git cat-file 取 d963f5a2 落临时件＋hash-object 复核 d963f5a2 全等→实跑＝exit 1／real 105.4s／发现 VIOLATION 4,262（EAC-L1 2,091＋EAC-L2 4,262 中 VIOLATION 面）／入扫现算 158,604 枚＝与工程师读数族（125.8s／155.9s／发现 6,353 行／入扫 158,594）同量级＝入扫 −99.6% 复算成立；发现行数口径差（6,353 行＝run-gates FINDING_RE 口径 vs 单枚 VIOLATION 计数口径）＝口径不同非矛盾（本席全套闸差集侧现算 6,353→14 见 §四＝与工程师严丝合缝）。
- 自靶复现＝python3 share/check-pointers.py --target share/check-collab-lint.py＝exit 1／恰四枚 WATCH／与工程师取证件（ptr-target-after.txt）CRLF 归一后 diff 零行全等＝存量四枚（头注禁模式示例字面既有形态）零新增坐实；BLOCK 计数 0。
- --selftest 改后现跑＝exit 0 全 MATCH＝判据函数本体零动旁证（与工程师 selftest-after 同判）。
- 与工程师五判据回执忠实性逐项对照＝判据 1（0.889s/668/14）本席 0.717s/669/14＝同档同集可归因差一枚＝忠实；判据 2（155.9s/158,594/6,353 行）本席 105.4s/158,604＝同量级读数族并存＝忠实；判据 3（385.4s/差集 −6,339/总 27,052）本席现跑见 §四 全等＝忠实；判据 4（四枚 WATCH 存量）本席逐字节对拍全等＝忠实；判据 5（禁动面）见 §五 全等＝忠实。另＝工程师回执 §三-1 分项加和 335+65+268＝668 系加和笔误（实 668 与枚数全等、分项和 671）＝口径笔误不影响结论（黄 Y-N2 随注）。

## 四、R0 落链后全套闸差集抽验（复核项四）

- 现跑＝bash share/run-gates.sh --root . --no-write（不带 ALLOW_GATE_DOWN）＝exit 1／real 312.7s（gate-run-time.txt；与工程师 385.4s／起草 529.8s 读数族并存不追因＝较起草基线 8m49.7s 已降）。
- GATE 裁决＝BLOCK 在场照登恰一枚＝agent-experts/baigong-software-team/.workbuddy/memory/2026-11-18.md:34 OA-T1＝属预期照登不绕行（S1-b 未施工＝GTFAST 射程在册）；本席零 ALLOW_GATE_DOWN。
- FINDING_RE 口径逐脚本现算（本席对 gate-run.log 现跑）＝pointers 22,806／lint 14／closure 3,754／csot 467／ticket-reconcile 10／entity 1＝总 27,052；对起草基线 33,391 分项（22,806/6,353/3,754/467/10/1）＝**lint 差 −6,339＋其余五脚本差 0＝与票面 v2 §三-3 归因行及工程师读数逐项全等**。
- lint 差集逐行分面现算＝根 .scratch 松散面（非 tickets）6,064 行＋包内卷宗面 275 行＝和 6,339 严丝合缝＝票面 §三-3「主根归零项 6,064＋包内 275」核数命中；改后新增行 0＝零新增发现＝取径不更判据旁证（子集方向）；tickets 保留面 11 行对基线 set-equal True。
- 临界区现状登记＝R0 后主根缺省全扫仍 5.2 分钟级＝大头移至 check-pointers 全扫（22,806 发现面）＝S2/S1-b 射程随后续段＝与窄放行登记「落笔后闸临界区预期 1.5 分钟级」的方向一致但需 S2 靶检与 S1-b 兑现后复测（随注口径·非 R0 射程）。

## 五、R0 越界检查（复核项五）

- 改动笔面单＝git show --numstat 3fea556f＝恰一枚 share/check-collab-lint.py（25/4）；git diff --name-only 3fea556f^..HEAD -- share/ 现跑＝恰同单枚。
- 谓词对规格＝diff 全文现读＝四条谓词逐一对位票面 v2 §二 S1-a（包内段数 ≥2 剪／根 .collab 不剪／根 .scratch 仅 tickets 子树存续／.git+__pycache__ 存续）；FIXTURE_MARK 臂与 check_l1/l2/l3 与 read_lines 零动（改动全居 iter_files 函数体）＝只换入扫文件集坐实。
- S1-b/S2/S3/S4 零触＝对钉全等现跑：run-gates.sh 盘上 11a6f4d4／钩子 .git/hooks/pre-commit 8b785770／check-hook-health.py L47＝旧钉 8b785770 字面存续／install-hooks.sh f71474ac／60-gates.md b68cbfc7／两枚基线 json 2c44d339・f6171c7d＝八面全等零触。

## 六、卫生抽查（复核项六）

- .scratch/SWB-GTFAST-R0-build/＝18 件在盘在册（对工程师回执「取证族 18 件」计数全等·未拆）；.scratch/SWB-GTFAST-rev-prod/／rev-qa/／rev-arch/ 三席取证族在盘未拆（收口窗处置口径遵行）。
- 窄放行登记件 §四 健康账笔（主理人违例申报段）在盘在位；惟该件链态 untracked＝待投递（Y-N1）。

## 七、红黄绿总表与总判

| 复核项 | 判 | 关键读数 |
|---|---|---|
| rev 差异清单对拍 | 绿 | 十三条逐处在场指向正确＋全文 diff 与清单对齐＋决议六项逐项落实 |
| append-only 零回改 | 绿 | 六件各单笔＋链上盘上双向 blob 全等＋投递笔面单各恰一枚 |
| R0 修单独立复跑 | 绿 | 本席现跑 0.717s/入扫 669/发现 14（tickets 11 对基线全等）＋起点副本同窗 105.4s/158,604＋自靶四枚 WATCH 存量逐行全等＋selftest PASS＝与工程师回执忠实 |
| 全套闸差集抽验 | 绿 | exit 1/real 312.7s/OA-T1 照登不绕行＋lint −6,339 其余五枚零差＋总 33,391→27,052＋分面 6,064+275 严丝合缝＋零新增 |
| R0 越界检查 | 绿 | share 域面单恰一枚＋禁动八面对钉全等＝S1-b/S2/S3/S4 零触 |
| 卫生抽查 | 绿（随注） | R0-build 18 件在盘未拆＋登记件 §四 在位（Y-N1 随登） |

黄旗三枚（随注级·不阻断）：

- Y-N1＝窄放行登记件（.collab/decisions/…-R0提速先行-v1.md）治理族在册件尚 untracked 未落链＝请主理人补投递一笔入链（登记必落链口径）。
- Y-N2＝工程师回执 §三-1 入扫分项加和 335+65+268＝668 笔误（实和 671；枚数 668 与现算 669 窗差可归因）＝口径笔误随注不追改。
- Y-N3＝票面 v2 §二 S1-a「根 .scratch 除 tickets 子树外剪」存在措辞二读＝.scratch 直属零散文件剪或留两解（工程师实现取「直属不入扫」并自述申报）。本席现跑佐证＝baseline log 6,353 行中 .scratch 直属零散文件出处行 0 枚＝两读对发现集零影响＝登记收口窗措辞写死一句即可，禁因此回改 R0 落链件（append-only）。

**总判＝rev 可放行＋R0 落链实效坐实可放行（随注三枚）。rev 轮质量＝差异清单与票面 v2 现文严丝合缝、append-only 全绿、决议六项逐项兑现；R0 实效＝本席独立复跑亚秒级 lint／入扫 −99.6%／全套闸差集 −6,339 逐行归因命中且零新增／越界零触。**

下一步建议一句话＝登记件补投递入链后，按 GTFAST 原排程续施 S1-b/S2 段（主根缺省闸现余大头＝check-pointers 全扫面与 OA-T1 假阳性＝S1-b/S2 射程），收口窗一并处置取证桶与 Y-N3 措辞写死。

## 八、纪律申报

本席全程零 git 写（rev-parse／log／show／diff／cat-file／ls-tree／hash-object／worktree list／status 只读不禁）；判词落 .collab/audits/＝QA 写域；取证族落仓根 .scratch/SWB-GTFAST-narrow-qa/（新建·gitignored 临时域·用毕呈报不拆）；share/ 全域、三包内容、任何 .workbuddy/ 记忆面、票面与链上判词回执件、.workbuddy 面、worktree 各工作区、git config＝零碰零改；开工脏面 M 一枚＋?? 散件群零碰零 reset 零带入；撞锁零（NO-INDEX-LOCK）；同席多实例＝不存在（本席唯一在飞 QA 实例）；体例自查＝本件 at 符号字符 0／反引号围栏 0／文件引用仓根相对纯路径（正文直引件名＋blob 前缀）；落笔前自靶＝python3 share/check-pointers.py --target .collab/audits/2026-11-19-SWB-GTFAST-rev窄复核判词-v1.md 现跑 exit 0 零发现（读数随投递日志）。

（判词完——rev 窄复核＋R0 实效复核一枚；判词投递归主理人；本席未读他席 rev 轮任何未落盘意见。）
