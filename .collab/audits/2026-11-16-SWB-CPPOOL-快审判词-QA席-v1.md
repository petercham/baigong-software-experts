# SWB-CPPOOL · 候补池三票快审判词 v1（QA 席 qa-cpool3rev·fresh eyes）

- 开工 HEAD 现跑读数：git rev-parse --short HEAD ＝ **8792a97**（＝派工预期值全等·链顶＝SWB-RCTPATH 票笔）。
- 开工工作区照登：tracked 脏面一枚＝M agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl（他案·零带入）；仓根 untracked 散件群照登零带入；index 除本判词外零 staged。
- fresh eyes 声明：未读任何产品席审票产出；全部判定＝本席盘上直读＋现跑复现所得。
- 体例自注：本件正文对路径仅叙述性提及＝裸文＋全角斜杠（／U+FF0F）；引用票面／源码原文时反引号内容以 ⟦⟧ 标记替换＝防自咬。
- 被审三票（均在盘·行数全等票面登记）：票一＝.scratch／tickets／2026-11-16-SWB-CPJOIN-并发落链共享index卷入预防条款评估票-v1.md（88 行）；票二＝.scratch／tickets／2026-11-16-SWB-BKTCLS-桶名闭集机检规格票-v1.md（96 行）；票三＝.scratch／tickets／2026-11-16-SWB-RCTPATH-回执内包根相对写法预防条款票-v1.md（80 行）。

---

## 票一 SWB-CPJOIN（并发落链共享 index 卷入预防条款评估票）

**计数＝红 1｜黄 1｜绿 8**

红项：

- 红-1（取证引文与在册原件不符＋与票面同段自引闭集互斥）：票面 §二 样本② 句＝ ⟦卷入未退净前一次 commit 被门禁正确拦下（check-staged-declaration exit 4→GATE BLOCK＝闸活性正面样本）⟧。本席现取证：工程师施工回执（.collab／receipts／2026-11-16-SWB-A14H1-施工回执-工程师席-v1.md 行 83）原文＝ ⟦上述卷入未清前一次 commit 被门禁拦下（check-collab-lint exit 4·GATE BLOCK）⟧——**拦下者真源回执写＝check-collab-lint exit 4，票面改写成 check-staged-declaration exit 4**。且票面同段防线 1 自引声明闸退出码闭集 ⟦0 放行／1 卷入 BLOCK／2 用法错／4 基础设施错⟧：卷入形态在声明闸处＝**exit 1**，exit 4＝基础设施错——票面该句即便按改后归因亦与其自引闭集互斥（闸名与退出码双错置）。结论面（有闸在岗拦下＝活性样本）未被推翻，但该样本正被候选三结论 ⟦已机械化为声明闸（pre-commit fail-closed·案②活性实证）⟧ 用作支点，须勘正＝红。

黄项：

- 黄-1（在册两源矛盾未随注）：收口登记（.collab／decisions／2026-11-16-SWB-A14H1-收口登记-v1.md §三）⟦声明闸两拦两正（描述句失型／卷入面 GATE BLOCK）⟧ 与工程师回执 ⟦check-collab-lint exit 4⟧ 对同场拦下的闸归因互斥（主理人侧归声明闸线／工程师侧归 check-collab-lint）。票面采收口登记侧未随注两源矛盾。本席旁证：声明闸活性另有独立在册实证＝b8994a0 笔面 ⟦staged-declaration gate exit 1 correct block prose-form declare⟧（exit 1 与自引闭集吻合）＝活性结论不依赖案②归因、总结论不翻，故列黄不列红。

绿项（本席独立试装命令＋读数）：

1. V0 链笔五枚现跑：git log --oneline -1 对 2dd1d4a／b8994a0／9a15849／3160d4e／6d1933d 各 exit 0（笔面全在链；b8994a0 message 含 append 归因自述全文）。
2. 6d1933d 口径如实：笔面在册句 ⟦红线唯一＝同席多实例·异席并发不禁禁自行加严⟧ 与票面防线 3 引文吻合＝候选一「错峰＝自行加严＝本身违例」决定性论证成立。
3. 声明闸头注退出码闭集现读（share／check-staged-declaration.py 行 23-25）＝0／1／2／4 不含 3，与票面防线 1 所引闭集吻合；「FX-U30 上线」出处在头注在册。
4. pre-commit 钩子现读＝声明闸先调（行 6）、run-gates exec 在后（行 7），与票面「钩子行 6 调用·先于 run-gates」吻合。
5. 样本①取证链对账：收口登记 §三 与 b8994a0 笔面互相咬合（v1 正文一字未动·blob 字节全等·append 恢复归因三要素齐）＝案①描述不失实。
6. D-58 先例件实存（.collab／drafts／2026-11-09-卷入登记-SEMGVT6v4入9a15849-v1.md）：件内 §一-2 ⟦name-only 实测恰两件⟧ §一-3 TR27 反向复现 §一-4 blob cd95efd7 全等 与票面引述逐项吻合；9a15849 git show --name-only 本席现跑＝恰两件全等。
7. 观察行提级条件可判定：⟦出现任一「卷入致内容损／需回滚／归因无法 append 恢复」样本即提级重评⟧——三判据各有机械／流程观察面（内容损＝blob 对拍／回滚＝史笔形态／归因不可恢复＝append 件缺位），与在册「样本 2 均自愈·影响坐实即提级」口径对齐＝非悬空。
8. 候选二成本引文实存可定位：RET 判词两句实测在盘＝agent-experts／baigong-software-team／.collab／audits／2026-11-04-SWB-RET-QA-v1.md 行 64（worktree SOT 伪影沿先例登记）＋行 86（worktree 五枚 remove 归位自证）。随注：票面未给全径但全仓 grep 恰一处命中＝可定位、不失实。

票一结论＝**需 rev**（红-1 定点勘正：案②闸名＋退出码两处改真＋黄-1 两源矛盾随注一行；其余论证面不动）。

## 票二 SWB-BKTCLS（桶名闭集机检规格票）——核心技术票·深查

**计数＝红 2｜黄 2｜绿 12**

红项：

- 红-1（§〇 现跑读数失实）：票面 ⟦路由表现读＝……per_spec **25 条目**＋on_severity 3 档＋escalate 5 键⟧。本席现跑（python 解析 60-gates.md 唯一 json 围栏）＝**per_spec 恰 22 条目**＋on_severity 3＋escalate 5。窗口对账＝git diff --name-only 9fb9256..8792a97 恰两枚票面件、60-gates.md 窗内零改动＝非他笔漂移所致；25 疑系误并 on_severity 三档入计。票面自称「现跑·禁抄在册旧数」而读数错登＝红（一行改真可消）。
- 红-2（V2 判据照票面跑出必红且无合法消解路径＝判据级互斥）：V2 ⟦git grep 旧径受跟踪引用零命中⟧ 未写死 grep 射程。本席实测：全仓受跟踪文件含 ⟦collab/qa⟧ 字样命中 **251 枚文件**（百工包内约 175＋fuxi 包 32＋仓根案卷与票面群＋share／baseline-pointer-exempt.json 一枚等）。其中：两嵌套包 qa／ 引用＝裁甲在册豁免面**禁动**（票二 §五 自载 ⟦嵌套 .collab 各包桶面零碰⟧）；历史案卷叙述态引用＝史面**不追改**（票二 §2-6 自载 ⟦链上史笔不追改⟧）；7 枚迁移件中 **5 枚内文含旧桶自引**，而 §五 写死 ⟦qa／ 桶 7 枚件内容零改字（纯迁册·git mv R100 预期）⟧——「内容零改＋史面不改＋豁免面禁动」三约束下，字面「零命中」机械不可满足。＝V2 需 rev（修法示例：射程写死＝仅「以反引号指针形态指 7 枚件旧全径」＋限定缺省扫描域＋豁免面与叙述态照登为允许行；同族教训在册＝COLLAB-STRUCT 产品席审票判词对 §5.3 钉值的同型点名）。

黄项：

- 黄-1（README 对拍自证规格留执行裁量＋行号错位）：§2-3 ⟦解析 ．collab／README.md「17 桶名录」行（行 29 锚字样「17 桶名录」）⟧——本席现读：锚字样在行 **27**（节标题行），名录清单列表体在行 **29**（该行内**不含**「17 桶名录」字样）＝「锚字样」与「清单行」跨两行且票面把两者并记一行，规格未写死从锚到清单的取行关联＝施工轮留裁量，可装但非机械闭合。随注：行 29 清单 17 项与本席对拍票面 §〇 引录逐项全等。
- 黄-2（GATE 读数差·归因随注）：票面 §〇 现跑 151502 与在册钉值 151508 差 6 枚如实登记；本席 HEAD 8792a97 现跑 bash share/run-gates.sh --root . --no-write → **exit 0·GATE PASS（发现 151508）**＝与在册钉值全等（票二票三两笔入链后已回钉值）。差值归因方向＝当窗 .scratch 票面群对 check-ticket-reconcile 观察面的进出波动，非本闸射程面＝黄随注不归红。

绿项（挂载面试装＋域口径对拍·本席现跑）：

1. SCRIPTS 名单挂载形态真实可装：share／run-gates.sh 行 141 现读恰十项，与票面 §〇 列举逐项全等；行 144-155 循环体现读＝形态①同域裸名 → SELF_DIR／＜name＞.py（行 147）＝「增裸名项 check-collab-buckets·零循环体改动」成立。
2. 名单缺件 fail-closed：行 149 die_infra「缺少检查脚本」＝「脚本先落、名单后挂」顺序错位会被基础设施错拦死＝挂载面有机械兜底。
3. MC 前缀映射在册：SPEC_ID_HOME（行 215-221）MC → multi-collab 现读全等；读表规则 5 解析器（行 259-297）收 ⟦MC-BUCKET-1⟧ 完整形态或裸 ⟦BUCKET-1⟧ 词边界形态于 agent-skills／multi-collab 任一 .md＝票面 §2-5「规范件配套条款行」落点正确。
4. 路由表现盘干净：json 围栏恰一处＋per_spec 现无 MC-BUCKET-1＝增量为净新增；围栏数≠1 → exit 4 自爆机理在 run-gates 裁决段在册＝V5「围栏仍恰一处」判据有机器兜底。
5. 违例行形态兼容：FINDING_RE（行 196-198）兼容 ⟦路径:1: BLOCK MC-BUCKET-1 …⟧；目录级 line 恒 1 先例实存＝check-collab-lint 行 182／185／240 三处 ⟦:1:⟧ 形态在册＝票面所称先例如实。
6. 存量违例坐实：git ls-files .collab／qa ＝ **7**（文件名七枚清单与票面 §〇 全等）；仓根 .collab／ 一级目录现枚举 15 个＝票面 15 桶列举全等；qa／ ∉ 17 桶名录＝唯一存量违例坐实；adr／architect／product 三桶现盘不存在（ls 三径均无）＝「白名单制非必存制」辨析属实。
7. README 名录与残留句对拍：行 29 清单 17 项逐项全等；行 35 历史残留句（旧 qa 字样读作 audits）在册＝票面「现盘 qa／ 内为 11-10 后新落件非历史残留」辨析属实（七枚文件名日期 11-10／11-11 现读坐实）。
8. 迁移与 ㊺指针闭集／豁免快照零机检交互（本席独立核·派工指定试查项）：share／baseline-pointer-exempt.json items 恰 **9** 项逐项现读——九 token 无一指 qa 桶或 7 枚件名；collab_bucket_exempt 两项仅两嵌套包 qa／（裁甲射程外）＝快照面与迁移面无交集；7 枚件居仓根 .collab＝check-pointers 缺省域外（见绿-9），迁入 audits 后其内文旧径自引**不入缺省扫描面不翻红**；check-pointer-closure 行 30 ⟦.collab/** 与其余规范件不进扫描面⟧ 在册＝closure 同样零触。票面「受跟踪引用全仓 grep 逐件随动＋靶检 exit 0」工序对向外出站引用（.scratch 票面群等）够用＝该交互面票面**已处理**（红-2 是 V2 射程措辞问题，非此面漏处理）。
9. 钉值对拍：python share/check-pointers.py --root . 缺省现跑 grep -c BLOCK ＝ **22816** 与票面钉值全等；DEFAULT_SCOPE 行 76 现读＝三分类元组（share／ 与仓根 .collab／ 均不在内）＋行 52-53 裁-23 拍板 2 排除句在册＝「本闸域与 DEFAULT_SCOPE 零交集·缺省 BLOCK 零扰动」论证坐实。
10. defects 先例链六笔现跑全在链 exit 0：36dfb78／fb76547／c79dde9／9ebc94f／883aa68／111b67a＝迁册先例引用如实。
11. 裁甲与移交工单引用如实：.collab／decisions／2026-11-10-皮总裁定-候裁三件全按建议放行.md §二-2 现读 ⟦裁甲＝不迁……17 桶闭集只管仓根 .collab⟧ 逐字吻合；移交工单 v3 行 A14（现读行 27）修法列 ⟦门禁工具线（check-collab-lint / run-gates 域）⟧ 与建议句同型＝「已批框架内执行分解·候裁 0 枚」有在册授权支撑。
12. 钩子时序与 pre-commit 断言属实：现读钩子＝声明闸先／run-gates 后两段＝§三「时序零触·新脚本在 run-gates 循环内获得位置」成立；--no-write 只读模式在 run-gates 参数段在册＝V0 照跑形态可用。

票二结论＝**需 rev**（红-1 一行读数改真＋红-2 V2 射程写死；黄二随带；规格主体＝挂载面／域口径／豁免交互／存量坐实全部试装通过，骨架不伤）。

## 票三 SWB-RCTPATH（回执内包根相对写法预防条款票）

**计数＝红 0｜黄 2｜绿 8**

黄项：

- 黄-1（例证四机理解释欠准·断言不翻）：票面称 ⟦.scratch/eng-adrl0/⟧ 形态 ⟦对 check-pointers 按文件上下文可解析＝不悬空⟧。本席现跑：python share/check-pointers.py --root . --target agent-experts／baigong-software-team／.collab／receipts／2026-11-05-ADR-L0-S4.3-终写回执-v1.md → exit 1·BLOCK 恰两枚（行 21／行 38·均 docs 域旧案·与票三射程无关照登），**行 3 该 token 零悬空行**＝「不悬空」断言与现机一致。但本席进函数级复算（resolve 七候选）：该 token 现因＝**尾斜杠致基名空串→候选八（同目录＋基名）命中文件自身所在目录**＝空洞可解析；所指 scratch 族现盘已自删（仓根与包内 .scratch／eng-adrl0 均不存在）＝票面「按文件上下文可解析」的措辞掩盖了空洞命中机理。断言真、归因欠准＝黄随注（恰好反向支撑票三本体＝该写法对跨包读者解析入口不唯一）。
- 黄-2（V0 行号口径微偏·票面已自留活口）：V0 引 ⟦check-ticket-reconcile.py 行 374-375 注释句⟧；本席现读三认态注释体起于行 **375**（374 为空行）、形态③注释行 381、RECEIPT_TAIL_PTR_RE 行 383-384、abs_ptr_to_rel docstring 行 386-391。票面正文引「行 374-391」＋V0 自注 ⟦行号以当轮现读为准⟧＝可容，随注不必 rev。

绿项（本席独立试装命令＋读数）：

1. V0 取证四件现盘实存（ls exit 0）：.collab／receipts／2026-11-14-SWB-CPRC5-工程师回执-v1.md／.collab／receipts／2026-11-16-SWB-A14H1-施工回执-工程师席-v1.md／agent-experts／baigong-software-team／.collab／receipts／2026-11-05-ADR-L0-S4.3-终写回执-v1.md／.collab／decisions／2026-11-16-SWB-A14H1-收口登记-v1.md（候补池观察行出处＝其 §四-④ 现读在册）。
2. reconcile 三认态逐字对拍：行 375 注释 ⟦回执指针两形态（ENG-S7 扩认·工具向票面体例三律②「含盘符完整路径」对齐）⟧ 与票面引文吻合；三态＝①仓根相对正斜杠反引号②含盘符绝对（ABS_RECEIPT_PTR_RE 行 380）③过程域尾段＋回执标记（RECEIPT_TAIL_PTR_RE 行 383-384）；⟦仓外绝对路径＝不算回执指针⟧＝abs_ptr_to_rel docstring 在册句；**包根相对不在三认态**＝三正则逐项核属实。
3. 解析口径引用如实：check-pointers resolve() 七候选注释与代码现读在册（含包根候选＝第四候选「相对本文件所在包根」——此即包根相对形态在悬空面可解析、却在回执对账三认态外的两制错位本体）；反引号 INLINE 形态提取＝裸文／全角斜杠叙述态不入机检属实。
4. dev-discipline 三引对拍全等：§三-2（行 42）对账口径 git show --name-only 全等；§八-5（行 86）scratch 取证族仅准叙述性提及；§二-1（行 21-22）盘符路径不入交付件＋过程域不受此限。
5. 例证一逐字对拍：CPRC5 回执行 26 现读＝票面引文（含 ⟦包根相对 token 改字补全为仓根相对全径⟧ 与括注）全等；被修原件＝ADR-L0 终写回执实存在盘。
6. 例证二逐字对拍：同上回执行 27 现读＝票面引文全等（错径旧域前缀 token 同场实证坐实）。
7. 例证三形态并存坐实：A14H1 施工回执行 7＝全角斜杠裸文叙述态、行 47／57＝命令读数半角仓根相对径——同一件内多形态并存现读属实＝「写法无条款约束·合规凭自择」坐实。
8. 乙案害面有在册支撑：worktree 盘符漂移同族问题＝RET 判词行 64 在册（SOT 缺省相对路径在临时 worktree 落空 exit 2 实录）；含盘符径解析依赖仓根前缀比对＝abs_ptr_to_rel startswith root_norm 现读坐实；「机检面对乙案收窄」与三认态②仅收回执标记形态（文件名含回执二字）吻合。

票三结论＝**可放行**（红 0；黄二均为归因措辞级随注，不动两取态对比与甲案建议的成立性；条款落地候裁面合规单列）。

---

## 总结论

- 票一＝**需 rev**（红 1：样本②拦下者闸名与退出码双错置——真源在册为 check-collab-lint exit 4／声明闸卷入形态闭集内为 exit 1，两处改真＋两源矛盾随注一行即可）。
- 票二＝**需 rev**（红 2：per_spec 现跑读数 22 非 25；V2「旧径受跟踪引用零命中」在内容零改＋史面不追改＋豁免面禁动三约束下机械不可满足＝射程须写死。骨架面——挂载／路由／域口径／存量坐实／豁免交互——全部独立试装通过）。
- 票三＝**可放行**（红 0 黄 2 随注）。
- 候裁面对账：三票候裁面均在单节单列、无自裁生效痕迹＝职权面零违例；票二候裁 0 枚主张有移交工单 v3 A14＋裁甲两处在册授权支撑，本席独立复核未见被压的决策者范畴项。

## 纪律段（本判词笔自证）

- 开工读数＝8792a97 现跑（见开端）；收工读数见完工回报。
- 本件防自咬＝路径裸文＋全角斜杠·引文 ⟦⟧ 标记·落笔前自靶 python share/check-pointers.py --root . --target 本件路径 exit 0（读数见完工回报）。
- 单件 pathspec 两端齐带·add 紧邻 commit 零窗口·commit 前 git diff --cached --name-only 坐实仅自件·FX_COMMIT_DECLARE＝仓根相对纯路径清单前置·禁 add -A／amend／no-verify·message collab 起头零 at 零反引号·尾标 [SWB-CPPOOL-QA-REV] 置最末位·commit 输出重定向 .scratch／cpool3qa／·timeout 十分钟档·撞 index.lock 有界等待零删锁。
- 只读被审三票＋取证；产品席审票产出零读（fresh eyes）；他案脏面照登零带入；判词落 .collab／audits／＝本席写域。
