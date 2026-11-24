# SWB-LC-0001 · LEAD-CONSTRAINT C1 提案包 审票判词（QA席·fresh eyes·v1）

判词尺＝judgment 自靶（pointers 尺本件归零沿 PF-H 先例；check-ticket／preflight 票面骨架尺对判词面不归靶）。被审件＝.collab／board／2026-11-24-LEAD-CONSTRAINT-主理人约束面外置-C1提案包-v1.md（258 行现跑 wc 中＝与派工面值全等）。提案方＝架构席＝本席独立审计臂（提案方回避原则·§12 C1 行现读在册）。互不读他席产出在册（本窗零读产品席产出）。本窗禁 git 写＝只读 git＋hash-object／rev-parse／cat-file 族在册；判词落位＝工单指定 board 审票面单一写面。

## 〇、开工与收尾读数（当轮现跑）

    开工：date＝2026-11-24 14:17｜HEAD＝4a8f9688（链顶现读＝被审件投递笔＝较票面起草基线 a22d3c9a 后移一笔＝投递活体照登非漂移）
    链序现跑＝4a8f9688←a22d3c9a←9bb48400←039c36c1←6b96c732←2c7dc6f4←d1a88d1d 逐枚 %p 相衔零断（d1a88d1d parent f91af560 cat-file 现读＝与票面 §五·甲 六枚链序全等扩展）
    index.lock＝NO_INDEX_LOCK｜脏面＝git status --porcelain 空输出（tracked 零枚＋?? 零枚当轮现数）
    台账开工拍＝仓根 .collab／ledger／ledger.jsonl 7 行／包 8 行／仓根 leases 面不存在（ls 坐实）／包 leases.jsonl 7 行＝四值与票面 §五·甲 申报逐枚全等
    收尾复跑＝对钉集 23 枚收尾＝开工值全等（§一）；真账两台账两拍 7／8 行零染（探针标记 grep 各 0）；被审件收尾盘现未动（本席零触）

## 一、审项一＝对钉集 23 枚两式独立复算（非同构抽样臂＝本席自选靶径全跑）

复算口径＝枚枚现跑 wc -l／sha1sum 盘现／链面两工具互证（git rev-parse HEAD:<path> 与 git hash-object 双跑）。计数现跑＝§五·丁清单恰 23 枚＝与派工面值全等。

读数＝23 枚行数列＋盘现 sha 列全中（零失配）；链面值申报七枚（hooks 三脚本＋hooks.json＋run-gates＋check-staged-declaration＋check-hook-health）两工具现跑全中（如 write-guard 链面 634425b5／commit-audit 238cf3ef／memory-neutralize f0335ed9／hooks.json 57c83b62／run-gates 11a6f4d4／check-staged-declaration 04f2889f／check-hook-health 80429ca8 逐枚中）。

链面 blob CR 计数现跑＝七枚链面全 CR=0（autocrlf=true 清洁入库坐实）＋盘现 CR 计数＝行数（23 枚中盘可核者全 CRLF）＝票面 §五·丁 CR 随登列逐枚复现。形制注＝本机 git hash-object 对 tracked 径自动套 autocrlf 清洁滤＝hash-object 臂＝链面值＝rev-parse 臂全等＝两式自洽（此点同时为 §四 CRLF 处方取证）。

注一枚（黄一前身核＝见 §六黄一）＝V1 验收臂文字枚举（hooks 三＋hooks.json＋闸四＋对账装配四＋本机钩子两＋「模板两枚」＝16 枚构面）＜§五·丁在册 23 枚（模板族实登六枚＋check-ticket 一枚＝七枚未入 V1 枚举）；丁段为超集＝按丁段全跑即覆盖＝实质不破、臂文字归 rev。

## 二、审项二＝探针实证面独立复现（本案立论地基·非同构自造样件族）

本席不复用提案方 P1／P2 命令形（非同构臂＝自选标记 SWB-QA7777＋自选旁路形态族＋hooksPath 改指本席 .scratch 空目录）。全部 prehook 注入面跑（--ledger 显式重定向 .scratch／SWB-LC-QA／probe-ledger*.jsonl＋SWB_REPO_ROOT 三锚在册＝在册硬纪律践）。

    旁路四臂（带票 ID 形态＝真旁路语义面）：
    Q1 git commit --no-verify -m SWB-QA7777（--no-verify 尾置异标）→ exit 0·零输出·台账零入账＝复现提案 P1
    Q2 git commit -n -m SWB-QA7777（-n 短式）→ exit 0 零输出＝旁路词面族对 -n 同样零覆盖（提案未测形态·本席补获）
    Q3 git -c core.hooksPath= commit（置空形态）→ exit 0 零输出（提案 P2 为 =／tmp 改写＝非同构变体复现）
    Q4 git -c core.hooksPath=.scratch／…／emptyhooks commit（改指空目录）→ exit 0 零输出
    对照两臂（在册应拦）：
    Q5 git commit 无票 ID → exit 2＋BLOCK orphan 命中＝复现提案 P3
    Q6 git commit --no-verify --amend → exit 2＋BLOCK amend＝词面族在岗第二直证

结论复核＝「本地闸对跳钩子／改钩子路径零覆盖」属实＝提案立论地基成立 ✅。精确化随登（绿注）＝本席补证一条边界：旁路命令**不带票 ID 形态**＝撞 orphan 顺带拦（本席首轮五臂 exit 2 直证＝BLOCK orphan）；旁路命令**带票 ID 形态**＝exit 0 零拦零痕＝即「零覆盖」精确面＝旁路＋有票形态；现闸对旁路的偶遇系 orphan 判据顺带非对旁路本身＝对提案结论无推翻、仅补精确边界（供 T2 票规格引用时取精确口径）。

台账纪律自证＝探针入账全居 .scratch／SWB-LC-QA／（probe-ledger 7 行＋probe-ledger3 2 行＝标记行逐读＝呈报类 block 记录）；两真账 SWB-QA999／SWB-QA7777／qa-control grep 各 0 命中＝真账零染对讲复现；探针件用毕即拆＝拆前 ls 在册→rm→拆后 ls 不存在（§七）。

## 三、审项三＝票体自包含＋V 系可执行性＋拆票预案无环

票体四字段①②③④齐现读（行 62／66／80／91）；声明闭集自包含＝写集具名 S1 一枚＝§〇 与②规格两处口径一致；候裁单列 §四在场（J 系三枚两侧论证＋签系五枚具名＋起草席不自拍申明）＝形制齐。

V 系逐臂可执行性核＝V0（链顶＋链序＋锁＋脏面＋台账拍）本席全臂复跑命中＝可执行；V1 可执行但枚举面有缺口（黄一）；V2 三案五字段实质齐＝设计段行号级具名（甲 208／210／215／217／219·乙 223／225／229／231／233·丙 237／239／242／244／246＝十五锚各恰一枚段内在位）＋四段辅节各在场（取舍 §二怎么选＋§六丁／拆票预案 §五戊／边界互见 §二末两节／呈签点 §四签系）＝绿（注＝裸 grep 计数含定义行与 §六 引言行混计＝「≥5 命中」读法须按节段级复现＝沿 BG-16 黄二先例口径本次实质成立不列黄）；V3 投递面单＝本席当轮复算＝git show 4a8f9688 --numstat＝恰一枚 259 增 0 删＝「纯增删除列零」命中（259＝258 行＋末行无换行计数口径照登沿 BG-16 先例）；V4 三闸本席独立复跑＝check-ticket BLOCK 0／WATCH 0 exit 0＋preflight 同＋pointers exit 0＝全中；V5 台账两式 7／8＝本席两拍复跑全等＋探针重定向面在位；V6 四词各 grep 恰 2 命中＝命中行＝行 16＋行 88 具名逐一对位＝自引外各零＝申报成立（形制随登＝行 88 居 §三③ 节内·票面自引称「§六 V6 本行」＝节归属文字错位一枚＝不影响计数复现＝绿注）；V7 依赖边现读枚举＝T4→T1→T2→T3 四边＋T2 软面臂／T3 报警臂挂 T1 后半＝单向可列·零回边＝无环申明成立。

拆票预案写集域具名核＝T1（.github／workflows／gate-replay.yml 新建＋share／install-hooks.sh 段＋decisions 登记件）／T2（run-gates＋check-staged-declaration＋新件 gate-token-verify＋仓根账本载荷扩展）／T3（新件 check-lead-health＋新件 lead-watch.yml＋config 两枚哨兵行）／T4（白名单基线件或修票）＝T1∩T2 零交叠（install-hooks vs 两闸脚本互斥具名）；T1∩T3＝同 .github／workflows／ 目录但文件枚枚具名互斥（gate-replay.yml vs lead-watch.yml）＝不重叠申明成立；T2 账本载荷扩展与 T3 config 面互斥＝交叠零（RECORD_TYPES 六类闭集零动申明＝本席现读 reconcile-daily.py 行 19 六类直证＝「签字」类载荷扩展不取新记录类路径与 B16-f J-1 在册裁例自洽）。

## 四、审项四＝CRLF 处方技术成立性（现跑取证）

取证链现跑＝①core.autocrlf＝true 现读中；②链面 blob CR 计数＝七枚全 0（CRLF 在入库面已被清洁＝链面跨平台单一真值）；③盘现全 CRLF（CR 计数＝行数 23 枚逐中）；④run-gates.sh grep hash 现跑＝零枚＝可进 CI 判据族（SCRIPTS 行十一枚具名现读行 141＝与票面「十一枚」枚数全等）本体零钉哈希比对＝「禁对钉哈希、只比内容与 exit 码」在现存闸面零对抗（该处方＝新增约束非现状改判）；⑤check-hook-health blob 臂现读＝盘现 blob_sha1 实现（行 89—93）＝票面「CI 侧取 git 对象面」＝改配语义非复跑语义＝T1 票规格承接位具名；⑥--no-write「汇总读数与 exit 码与写盘模式一致」现读行 67 在册＝FX-U21/D-86 引证对位。裁定＝处方技术成立 ✅；跨环境漂移风险已在册自申报（§六丁风险行「CRLF／路径分隔符＝T1 验收面双向断言」）＝承接位在场。缺项申明＝GitHub 侧 Actions／分支保护两态＝本席禁检索不自救＝无查证权＝维持票面 ⚠️ 登记为决策者侧待核项（T1 开工首步进其 §二）＝本席不判。

## 五、审项五＝独立构造用例（防共盲·两枚）＋现状盘点抽核

用例一＝§六甲(2)「证据链回指」判据可执行性草案：取「run-ts＋commit 配对」构造 CI 侧断言行族＝⟦status check 绿绑定 commit sha＝GitHub 状态 API 只读面⟧／⟦本地伪造证据件不触远端状态＝差分必现形⟧／⟦CI 不可用＝降级须决策者签＝无自动旁路断言⟧＝三判据各单一期望无二义＝该机制段可拆施工判据成立（与失效承接段「不开自动旁路」互洽）。

用例二＝J-1 甲案（离线签名令牌）与既有账本闭集的互锚可解析性：RECORD_TYPES 六类现读直证（含「签字」类）＝载荷扩展字段不扩枚举路径可机械判（枚举行 grep 恒等臂）；「同码二次＝红」＝随机码消费态 append 可查重＝单一真源在仓根账本＝判据可执行；「验签靠公钥不靠渠道」＝公钥在仓＝链面可钉＝与 §五·丁对钉体例同款。甲案两侧论证自咬面复核＝票面驳乙案「主理人不可写登记面在仓内无处安放」与本席对 write-guard 租约面现状认知一致（host 持账本写权＝自咬＝乙案缺陷陈述成立）＝荐甲无异议。

盘点抽核（丙段逐条现跑）＝ALLOW_GATE_DOWN 五处现读命中（check-staged-declaration 行 149＋run-gates 行 37／66／167／528＝逐枚对位）＋行 481 区 bypass 键写回现读命中（doc["bypass"]=True）；hooks.json matcher 三臂现读（Write|Edit 族／Read|Grep／Bash 两臂）＝「全部运行于宿主会话权限层内」装载面属实；check-hook-health 当轮现跑 exit 0·快照 hook-blob=6bc60801／hooksPath-readings=0＝票面补充盘点两枚逐字中；git remote -v origin 两态在位中；§11 外置物表 CI 行「人类侧／托管面」定性现读在册＋§12 L2 四类（C1 适用＝TCB 行为／拦截阈值／seat-permissions）行 122 现读在册＝签1／签3／签4 归 C1 通道判据可归位；config seat-permissions 两枚在盘＝签4 随动面实体在位。缺省扫描辅证＝run-gates --no-write 当轮 GATE BLOCK 五枚具名（provenance exit4／sot exit2／OA-T1 三枚＝含 tests／b16e 新面一枚＝他案存量群沿 BG-16 审票口径归因＝与提案包 V4 自靶判据分面不混）。

## 六、判词计数＝红 0／黄 2／绿 6

红面＝零枚（立论地基探针面独立复现属实；申报读数零失配；结论链零推翻）。

黄二＝
- 黄一＝V1 验收臂枚举面与 §五·丁对钉清单不自洽（V1 文字构面 16 枚 vs 丁段在册 23 枚＝模板族六枚＋check-ticket 一枚未入 V1 枚举＝「模板两枚」与丁段实登六枚冲突）。影响评级＝不阻塞（丁段为超集＝收尾按丁段全跑即全覆盖＝本席已 23 枚全跑零失配坐实），但 V1 作为机械判据文字复跑口径会漏七枚＝归起草席 rev 一行（建议改 V1＝「§五·丁全集 23 枚两式全等」）。
- 黄二＝T4 排程申明三处不一致（T4 行「随 T2 前后排程」vs 依赖序列表「T4→T1→T2→T3」T4 首位 vs §六丁「T4 先收窄需求面」）。影响评级＝不推翻无环性（T4 零前置＝任意插位无回边＝V7 不破），但拆票路由时 T4 槽位两读＝归起草席 rev 一句定死（荐按 §六丁时序＝T4 首位＝与「先收窄降闸需求面」论证自洽）。

绿六＝
- 绿一＝对钉集 23 枚两式独立复算全中（行数列＋盘现 sha 全中；链面申报七枚双工具互证全中；CR 随登列逐枚复现；blob 面 CR=0×七枚取证）。
- 绿二＝旁路零覆盖立论地基非同构臂独立复现（四旁路臂 exit 0 零痕＋对照两臂 exit 2 逐一对位；补获 -n 短式与 hooksPath 置空两形态＝覆盖面超提案原探针；精确边界随登＝零覆盖面对「旁路＋票 ID 形态」，旁路无票撞 orphan 顺带拦＝供 T2 规格取精确口径）。
- 绿三＝提案包自靶三闸独立复跑归零（check-ticket／preflight／pointers 各 exit 0 BLOCK 0 WATCH 0）＋V3 投递笔复算恰一枚 259/0 纯增＋V0 全臂（链顶／链序 %p 相衔／锁／脏面／台账四拍）命中。
- 绿四＝CRLF 处方技术成立（六步取证链闭合＝§四；风险自申报承接位在位；GitHub 侧两态零查证权如实＝沿票面 ⚠️ 不判）。
- 绿五＝三案五字段＋四辅节实质完备（十五锚行号级具名）＋候裁 J1J2J3 两侧论证在场＋RECORD_TYPES 六类闭集直证＋J-1 甲案互锚可解析（用例二）＝席内落拍荐值本席无异议。
- 绿六＝拆票预案 V7 无环复核成立＋写集域枚枚具名零交叠（T1∩T3 同目录异文件＝具名互斥坐实）＋丙段盘点逐条现跑逐一对位（含 481 bypass 写回／matcher 三臂／§11 CI 行／§12 L2 四类／config 两枚实体）。

## 七、候裁与呈报面核＋纪律与收尾申明

候裁核＝J-1 荐甲无异议（用例二互锚成立）；J-2 荐甲无异议（乙案「不投」缺陷陈述与链上防改不防不投语义自洽）；J-3 荐甲无异议（P1 探针直证乙案窗口期＝本席 Q1—Q4 独立复现更强直证支撑甲）。签系五枚对照 §12 L2 四类逐枚可归位（签1＝TCB＋阈值＋新设签字面／签2＝TCB 承载者权限面／签3＝L2 条款语义变更／签4＝seat-permissions／签5＝确认型随呈）＝本席知悉在册＝本窗零签字需求申明成立。合议面＝本判词与产品席判词互不读＝合议归主理人投递窗归并沿册。

自靶臂＝pointers --target 本判词 exit 0 现跑在册（check-ticket／preflight 票面骨架尺对判词不归靶沿 PF-H 先例＝桶路由 judgment 尺投递窗必复跑沿册）。

本窗纪律自证＝fresh eyes 零读他席产出；零 git 写（只读 rev-parse／log／show／cat-file／hash-object／ls／grep／wc／sha1sum 族）；探针族台账显式 --ledger 重定向 .scratch／SWB-LC-QA／＋SWB_REPO_ROOT 三锚＝真账两台账两拍 7／8 行零染（标记 grep 各 0 两式自证在册）；探针件用毕即拆＝拆前 ls 在册→rm→拆后 ls 现跑不存在在册；写面＝判词一枚＝工单指定唯一落位；被审件收尾复跑未动（盘现零触坐实）。

收尾读数＝链顶现读随收尾复跑入完工回报（他案活体群照登零带入口径）；被审件盘现 258 行对开工全等；台账收尾拍 7／8＝开工拍全等。

——QA席·qa-lc·审票判词一枚·探针夹具用毕即拆
