# DEBTCLN-R5 · TOKPAR 红线参数化 · QA 独立验收判词（v1·QA 席·排程第 5 步）

- 验收席：QA 席 qa-debt5v（fresh eyes 独立验收·主理人派工·任务代号 DEBTCLN-R5-QAV）
- 验收对象：BUILD 笔 db81936（靶件 share／count_agent_tokens.py 插入 7 行）＋ RECEIPT 笔 5a848a9（回执面）
- 依据：票面 .scratch／tickets／2026-11-16-DEBTCLN-R5-TOKPAR红线参数化票-v1.md（222 行·含 rev1 段·链上 blob 对钉见 §〇）＋放行登记 .collab／decisions／2026-11-16-DEBTCLN-R5-放行登记-v1.md（9d95b5e）＋回执 .collab／receipts／2026-11-16-DEBTCLN-R5-施工回执-工程师席-v1.md（三件全文本席当轮现读）
- 验收对拍口径：V2 以票 rev1 段修正版命令为准（正文 §三 V2 命令含语法缺陷＝放行登记 §二 禁逐字照跑条款遵行）
- 防自咬体例自注：叙述面路径裸文＋全角斜杠（／U+FF0F）·零反引号·零 at 符号·引文 ⟦⟧；命令围栏内半角径＝程序准绳（R3／R4／R5 票同形制在册）。本件落笔前自靶 check-pointers --target 本件实路径须 exit 0（读数见 §五）。

---

## 〇、开工读数（本席当轮现跑·禁抄旧数·体例三律③）

- HEAD＝git rev-parse --short HEAD → **5a848a9**（＝RECEIPT 笔·链顶·与派工预期全等）。
- 链序现跑（git log --oneline -4）＝5a848a9（RECEIPT）→ db81936（BUILD）→ a33f390（他案 INVOLVE4 登记插笔）→ 9d95b5e（放行登记）＝父子逐笔相衔·与派工预期链序全等；他案插笔 a33f390 归因在册非本票违例（§四 V6）。
- git status --porcelain＝tracked 脏面恰一枚 M＝agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl＋?? 当轮群（2026-11-12 系列平放 md＋.collab／board／＋.collab／research／＋仓根杂散群·活体群计数当轮照登）＝全部他案照登零带入勿动。
- index.lock＝不存在（NO_INDEX_LOCK 现坐实）。
- 票面链上 blob 现跑对钉＝git rev-parse HEAD:票面路径 → **cf8ae98543e67a37fb4423dbe2c6235f859612be**（222 行现读·含 rev1 段）与派工预期全等。
- 基线参照面＝链上父笔 a33f390 树面靶件＝改前态（blob e755faef 系谱见回执 §〇·本席现读该面 33 行＋无参行为基线快照落取证族 .scratch／debt5v／）。
- 取证族＝本席 .scratch／debt5v／（V／对抗臂快照·用毕即拆 ls 坐实见 §五）。

## 一、V 系逐项读数（全现跑·禁凭记忆）

**V1 零回归 ＝ 绿**
- python -m py_compile 靶件 → **exit 0**。
- 无参运行 → **exit 0·7 行全 OK·OVER 0**·token 七枚 1889／2462／2480／2465／2289／2496／2496（max 2496 贴线未过）＝与改前基线（票 §〇／放行登记 §〇／回执 §〇 三源）逐项全等；本席独立复现＝取 a33f390 树面改前脚本落盘现跑，改前改后无参输出 diff **零行**。
- 行 7 字面：grep -c "RED_LINE = 2500" 靶件＝**1**；git show a33f390 面同式＝**1**（改前改后均恰 1·非 0→1 型·皮总拍板值面零改坐实）。
- numstat a33f390..db81936 ＝ **7／0**（纯插入零删除·删除行集空）。

**V2 对拍（rev1 段修正版命令逐字跑）＝ 绿**
- 先按命令字面 HEAD^ 于链顶现跑：HEAD^＝db81936（40 行态）→ exit 1·读数 CHANGED [16..33] LEN 40 40——此系命令基线语义（对拍对象须为施工父笔面），非缺陷，照登。
- 照票 §三 口径「HEAD^ 写法按实际父笔 sha 置换」→ 置换 **a33f390** 重跑 → **exit 0**·打印 **CHANGED [] LEN 33 40 BLK c2e49c06383fb4da9c1395c269319e2365561761733ab783264782aee3e67abe DISK 2a549d226c3704ce90296a7daa7979507faf2d4011a92eeca5fbfcecd3fd233e** ＝**四项全达**（既有 33 行零改动·错位对拍空集·块哈希对钉·盘 sha 对钉）。
- 靶件链上 blob＝git ls-tree HEAD → **ba4d92973501e9ea0e79f5a36791a8365be53bb8** 对钉全等；靶件行数 **40**；盘 sha256＝**2a549d22…** 全值对钉；CR 字节计数现算＝**0**（口径注明：靶件 LF 无 CR）。

**V3 带参生效 ＝ 绿（五臂＋位次＋glob 全达）**
1. --limit 2500（不带 glob）与缺省输出 diff **零行**·exit 0 全等（显式同值＝缺省）。
2. --limit 2400 → **exit 1·OVER 5**；--limit 2496 → **exit 0**；--limit 1888 → **exit 1·OVER 7**（与放行登记 §二 预期全等）。
3. --limit 无值 → **exit 1**·stderr 首行 ⟦count_agent_tokens: --limit 后须整数值⟧（fail-fast 坐实）；--limit abc → **exit 1**·ValueError 栈（invalid literal for int）＝已申报差量两臂复证·禁误计回归。
4. 位次两序（--limit 2400 前置＋glob 后置 vs glob 后置＋--limit 末置，glob 臂 "share／*.py"）→ 两输出 **cmp 逐字节全等**·exit 均 1。
5. glob 臂不带 --limit：本席独立复现＝git archive 分别取 a33f390 面与 HEAD 面 share 树隔离跑同 glob——两输出各 14 行·OVER 均 10·exit 均 1·diff **恰一行**＝唯一差行＝靶件自身行 token 读数 **415→521**（靶件自内容增长＝预期自引用漂移·非行为回归·其余 13 行零差）＝归因独立复现坐实（改前臂快照 sha c687abaa… 与票 §〇 及回执基线全等）。

**V4 门禁零扰动 ＝ 绿（四件套与放行登记 §〇 基线全等）**
- check-pointers 缺省扫描 → exit 1·**BLOCK 22809／WATCH 4582**＝与基线**双零变化**（插入块零反引号零路径 token＝零出账实测坐实）。
- bash share／run-gates.sh → **GATE PASS exit 0·发现 151502 照登**（活体禁钉死口径沿用·与基线全等）。
- check-collab-lint → **exit 1** 基线（EAC-L1 count=2006／EAC-L2 count=4097／EAC-L3 count=0）与基线读数全等。
- check-source-of-truth → **exit 0**（模式 dual｜文件 129｜BLOCK 0（新命中 0）｜基线豁免 54｜指针 WATCH 413）与基线全等。
- 四件套 exit 钉值全部本席当轮现跑对拍（R3 假钉值教训口径）。

**V5 自靶 ＝ 绿**：check-pointers --target 三件现跑＝靶件 **exit 0**／票面（链上现文含 rev 段） **exit 0**／回执面 **exit 0**。

**V6 面单 ＝ 绿**
- BUILD 笔 db81936 name-status＝**恰靶件一枚 M**；RECEIPT 笔 5a848a9 name-status＝**恰回执一枚 A**。
- 父子相衔现跑＝db81936^＝a33f390／5a848a9^＝db81936。
- 链上区间 9d95b5e..5a848a9 面单核他＝恰三笔＝他案插笔 a33f390（SWB-PIPEAUDIT-INVOLVE4 登记件·归因在册非本票违例·照 R2 收口 §四 终版口径不拆笔不回改）＋BUILD＋RECEIPT。
- 两笔 message 纪律现读＝collab: 起头／at 计数两笔均 **0**／反引号计数两笔均 **0**／尾标 -BUILD／-RECEIPT 各置 message 最末（现跑 tail 坐实）。
- 钩子互证在册＝RECEIPT message 载明 ⟦STAGED-DECL staged 1 声明 1 超额 0 互证⟧（BUILD 笔钩子读数随回执链上登记）；本席另独立复跑钩子实体 check-staged-declaration.py（FX_COMMIT_DECLARE 挂声明）→ exit 0·打印 STAGED-DECL 读数行＝钩子活性坐实。随登观察：BUILD 笔自身 message 未内嵌 STAGED-DECL 读数行（钩子 stdout 不入 message·链上内嵌证据仅 RECEIPT 一枚承载）＝既有钩子形态所定非违例·观察随登。

## 二、对抗臂（fresh eyes 必做六臂）

- **臂① 插入块与票 §二 展示块程序化对榫 ＝ 全达**：程序提取票面 python 围栏块与靶件行 16-22 实插块比对＝**逐字节全等**（BYTE_EQUAL True）·双 sha256 均 **c2e49c06383fb4da9c1395c269319e2365561761733ab783264782aee3e67abe**·LEN 均 **316** 字符；逐行七枚钉（无行尾口径）现算 7／7 复现对榫（77bc232f／a7f427fa／e5d5e92a／332cac5f／ef708572／7db57d09／f30c539d）。
- **臂② 禁动面逐处现读零触 ＝ 全达**：git diff a33f390..db81936 改动行集＝仅 ＋7 插入行（零 − 行）；行 7 sed 现读 ⟦RED_LINE = 2500⟧ 原样；CJK 正则行＋tokens 口径函数（ceil 非CJK／4）现读原样；默认 glob 两条（行 26-27 现位）在场原样；exit 语义尾行（行 40）⟦sys.exit(1 if bad else 0)⟧ 原样。
- **臂③ 盘上同名 .py find 计数 ＝ 坐实 118**：排除 .git 与本席取证族后 find 计数＝**118**（真身 1＋快照/嵌入副本 117）＝与基线全等·117 枚零触零合并（本席首轮未排除自族读数 120＝自增两枚隔离副本·归因照登非外案漂移）。
- **臂④ 取证族零残留 ＝ 坐实**：.scratch／debt5、.scratch／debt5rev、.scratch／debt5rev1、.scratch／debt5nar 四族 ls 现核＝**全部 GONE**（前席宣称即拆兑现）；**.scratch／pmdebt5rev 在场**＝产品快审席残留·git check-ignore 坐实 ignored 面·机检零扰动＝照登提醒不判红（放行登记 §四 卫生观察在册延续）。
- **臂⑤ --help 改后与改前基线全等 ＝ 全达**：改后 --help → exit 0·空输出 0 字节；本席取 a33f390 面改前脚本独立现跑 --help → exit 0·0 字节；cmp 两输出**逐字节全等**＝无 argparse 坐实（改前既有形态保持）。
- **臂⑥ 新参数语义零规范面扩散 ＝ 坐实**：git grep --limit 全 tracked 命中恰 5 枚＝全部系本案文书（票面／两快审判词／放行登记／回执）叙述面；*.py 全域命中＝**仅靶件自身一枚**＝他文件零引 --limit 语义·零扩散。

## 三、红黄绿计数与结论

| 面 | 判定 |
|---|---|
| V1 零回归 | 绿 |
| V2 对拍（rev 修正版·父笔置换） | 绿 |
| V3 带参五臂＋位次＋glob 归因 | 绿 |
| V4 门禁四件套零扰动 | 绿 |
| V5 三件自靶 | 绿 |
| V6 面单＋钩子互证 | 绿 |
| 对抗臂①-⑥ | 绿（六臂全达） |

**红 0／黄 0／绿 12。结论＝IS_PASS（放行进入收口登记步）。**

随登观察（不立项不判红）：①BUILD 笔 message 未内嵌钩子 STAGED-DECL 读数行（链上内嵌证据由 RECEIPT 承载·本席钩子独立复跑活性坐实）；②.scratch／pmdebt5rev 他案残留 ignored 面（提醒归收口席处置）；③V2 命令 HEAD^ 字面于链顶跑必判 LEN 40 40＝命令基线语义使然，票面置换口径已覆盖，验收各笔须照实际施工父笔置换照登。

## 四、案型登记

- 本席全程未遇 SIGTERM／SIGPIPE／index.lock 冲突；全程零删锁·零 amend·零 add -A。
- 首轮两处取证路径笔误（cd 后相对路径错位）致两臂当轮空跑＝当轮即纠重跑全达·错位读数归因照登（臂③ 120 读数同源）＝取证操作噪音非施工面问题。

## 五、本笔纪律自证（QAV 笔）

- 本笔面＝恰本判词一件；add 单 pathspec 紧邻 commit；commit 前 git diff --cached --name-only 坐实恰判词一枚；FX_COMMIT_DECLARE 挂 commit 命令侧；落笔前自靶＝python share／check-pointers.py --root . --target 本判词实路径 → **exit 0**（读数随完工回报 inline）。
- 靶件／票面／回执／账本／.gitignore／FUXI／他案脏面全部零触零带入；链上史件零回改；账本零手写。
- 本席取证族 .scratch／debt5v／ 用毕即拆＝落链后 ls 坐实随完工回报。
- 尾标 -QAV 置 message 最末（族名 DEBTCLN-R5 随尾标内嵌）；防自咬体例＝裸文＋全角斜杠·零 at·零反引号。

（v1 尾·append-only：如需追加随正在此续笔）
