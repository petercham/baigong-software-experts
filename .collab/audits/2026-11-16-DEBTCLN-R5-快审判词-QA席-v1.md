# DEBTCLN-R5 · TOKPAR 红线参数化票 v1 · QA 席快审判词（v1）

- 判词件：2026-11-16-DEBTCLN-R5-快审判词-QA席-v1（本席独写·与产品席互不知晓互不读）
- 审的件：链上票面＝.scratch／tickets／2026-11-16-DEBTCLN-R5-TOKPAR红线参数化票-v1.md（起草笔 8eff7c2·票面 blob 复跑＝5c352038355d69b93dc6719d7da125a9ee3f4b24 对钉全等·行数 176 对钉全等）
- 判词：红 2／黄 1／绿 8＝**缓放行·呈修单两条（均为票面自身读数与验收命令笔误·§二 施工规格本体经干跑坐实可照抄·不改施工语义）**

> 体例自注（防自咬）：本判词叙述面路径一律裸文＋全角斜杠；引用票面原文以 ⟦⟧；命令引用居围栏内＝程序准绳不入机检违例面（R3／R4 票同形制自靶 exit 0 先例在册）。本件落笔后自靶实跑读数见 §五。

## 一、开工读数（当轮现跑·禁抄票面）

- HEAD＝git rev-parse --short HEAD → **8eff7c2**（＝派工预期·起草笔链顶·其后无笔）。
- 票面链上 blob＝git rev-parse 于 8eff7c2 树面 → **5c352038355d69b93dc6719d7da125a9ee3f4b24**（与派工钉全等）；git show 面 wc -l ＝176（全等）。
- git status --porcelain 读数＝tracked 脏面恰一枚 M＝agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl（他案）＋?? 当轮 28 行（2026-11-12 系列平放 md＋.collab／board／＋.collab／research／＋仓根杂散群＝全部他案照登零带入；与票 §〇 开工轮计数 28 同值——票面已声明活体群禁钉死，故非钉值仅随登）。
- index.lock＝不存在（NO_INDEX_LOCK）。
- 收尾复跑：三扫描复跑对开工前基线 diff 零行＋.scratch／debt5rev／ 用毕即拆坐实（ls 不存在）＋?? 计数复跑仍 28 行（取证族零残留）。

## 二、逐项复核结果（审项对派工令八目）

### 绿-1 靶面判定（审项1）

- git ls-files 过滤复跑＝tracked 恰一枚＝share／count_agent_tokens.py。
- find 全量（排除 .git／）＝118 枚＝真身 1＋其余 117；117 枚归树复跑＝.scratch／ 根树 112＋agent-skills／fuxi-skill／.scratch／ 树 5＝两族闭集坐实（两树之外 0 枚）。
- **check-ignore 全量复跑（超出票面抽查口径）＝117／117 全部 ignored**。
- 三簇 sha256 复算＝55ccdf0ecdea ×1（真身）／9df22fc4902b ×106／abe98debbcf1 ×11——计数与票面全等；真身盘 sha 全值复跑＝55ccdf0ecdea8dcaf32d38e61fdfd3fb84390581dd8416cf60a10e41acc084e6 全等。
- 簇②抽样抬头行 2＝tools 字样＋CRLF 坐实；簇③与真身归一化行尾后逐字节全等（CRLF 33 枚差）坐实；三簇行 7 均携 RED_LINE = 2500 坐实（抽样）。

### 绿-2 硬编码定位（审项2）

- grep -n 2500 靶件＝恰一处＝行 7 RED_LINE = 2500；python 全文计数＝1；行 30／31 消费经常量非字面（逐行现读全等票面引文）。
- 现读全文 33 行＝脚本内无其它 2500 关联硬编码（CJK 正则＋除数 4 系口径参数·射程外）；行尾制 CR＝0 枚。
- 仓内他处归因复跑：check-source-of-truth.py 行 52／90 注释引 2500 分轨口径＋行 161 SKILL_LINE = 5000 全等；70-charter.md 行 47＝口径引用行（count_agent_tokens 恰一枚在该行）全等。

### 绿-3 改前基线全套（审项3）

- 无参：exit 0·7 行全 OK·OVER 0·token 七枚 1889／2462／2480／2465／2289／2496／2496（max 2496）·输出 sha256＝06289e5a15a0…全等票钉。
- glob 臂 share／＊.py：exit 1·14 行·OVER 10·sha＝c687abaa7c37…全等票钉。
- --help 改前臂：exit 0·输出 0 字节（被当 glob 消费）＝票面形态照登坐实。
- 靶件基线三钉：blob＝e755faef886f46b870a8a965c8029d55d527459b（git hash-object 复跑全等）·33 行·1545 字节——全等。

### 绿-4 门禁四件套基线（审项4·钉值面）＋红-1（SCRIPTS 计数）

- check-pointers 缺省：exit 1·BLOCK 22809／WATCH 4582＝全等票钉与派工预期。
- 靶件改前自靶：exit 0 坐实。
- 门禁入口实体＝share／run-gates.sh（ls 坐实·run-gates.py 仓内无此名＝票 §〇 勘正属实）；bash share／run-gates.sh → **GATE PASS exit 0·发现 151502** 全等。
- check-collab-lint exit 1（EAC-L1 2006／EAC-L2 4097／EAC-L3 0·EXEMPT 0／SUBSTR 1029／VIOLATION 4097）全等；csot exit 0（BLOCK 0／豁免 54／指针 WATCH 413／文件 129）全等。
- **红-1**：票 §〇 宣称 ⟦SCRIPTS 清单现读 12 项不含本靶件⟧——现读 share／run-gates.sh 行 141 逐项点名＝**恰 11 项**（check-provenance／check-skill-meta／check-pointers／check-entity／check-collab-lint／check-pointer-closure／ROOT／share／check-source-of-truth／check-ticket-reconcile／check-adr／check-hook-health／check-collab-buckets）。计数不实＝假钉值命中（R3 教训型）。实质结论不受影响＝count_agent_tokens 确实不在 SCRIPTS 名单＋install-hooks.sh 零引用＋git grep tracked 无运行时调用（消费面核查独立复跑成立）＝改码输入面零变化论证仍真。修单：12→11 一处数字勘正。

### 绿-5 施工规格可照抄性＝核心审项（审项5·隔离副本 .scratch／debt5rev／ 干跑·用毕即拆）

- 第一步 heredoc 逐字落盘：块 sha256＝**c2e49c06383fb4da9c1395c269319e2365561761733ab783264782aee3e67abe** 全等票钉·块字符数 316 全等。
- 第二步逐字执行（复制真身副本上）：四前置断言全过（MULTI-LITERAL／LIMIT-PRESENT／NOT-33-LINES／CRLF-UNEXPECTED）＋BLOCK-HASH 对钉＋ANCHOR 唯一→INSERTED-7-LINES exit 0。
- 改后产物四钉：40 行／盘 sha **2a549d226c37…**全等／blob **ba4d92973501…**全等／py_compile exit 0——仿真钉版全套坐实。
- 反证臂：对已插入面重跑第二步＝LIMIT-PRESENT＋NOT-33-LINES 双断言触发拒绝＝防重插守卫真咬。
- 行为五臂：不带参 vs 改前基线 diff **0 行**·exit 0 全等；--limit 2500 vs 不带参 diff **0 行**；--limit 2400→exit 1·OVER 5；--limit 2496→exit 0；--limit 无值→exit 1·stderr 错误行 count_agent_tokens: --limit 后须整数值——全等票宣称。
- 位次两序：glob 后置式与 --limit 前置式输出**逐字节全等**（cmp 零差·快照 sha＝6abdb53c97c8…连票面引用前缀都对榫）·OVER 8。
- glob 臂不带 --limit：exit 1·14 行·OVER 10·sha＝c687abaa…与改前基线**全等**（旧行为不变条不破坏）。
- 加验臂（票 §二／§三 申报面）：--limit 1889→OVER 6；--limit 1888→OVER 7；--limit abc→exit 1（ValueError 异常面）；--help 改后臂 exit 0 空输出＝与改前基线全等（argparse 否裁的基线论据独立坐实）。
- 行 7 改后原样在场（grep -c＝1）＋插入位＝行 15 注释后／if 行前逐行现读坐实＋默认 glob 两条在场。
- 取证族零扰动：干跑期间三扫描复跑对开工读数 diff 全 0 行（BLOCK 22809／WATCH 4582／lint spec 计数／csot 末行）；靶件 git status 零命中（真身全程未触）。

### 绿-6 体例与红线审项（审项6·除 V2 命令面见红-2）

- 行 7 字面 2500 禁改条款在 §二 禁动面写死＋皮总 10-25 拍板值出处在册＝在册坐实。
- 防自咬体例：票面自靶复跑 python share／check-pointers.py --root . --target 票面实路径 → **exit 0**（输出 0 行）。
- 票面零机检增量：票已落链（8eff7c2），当轮缺省 BLOCK 22809／WATCH 4582 与 §〇 起草态全等＝票面入扫零增量坐实。

### 绿-7 消费面核查（§〇 末行）

- git grep tracked 复跑：count_agent_tokens 命中面＝史件／登记／注释／charter 口径引用＋靶件自身＋check-source-of-truth.py 行 86 注释（同款实现口径）——无任何运行时调用坐实＝V3 论证根基成立。

### 绿-8 候裁 0 的两项自决·本席独立表态

- **自决①（取 flag＋value 位次无关·否 argparse／否环境变量／否仅 argv[1]）＝站得住**：argparse 会改 --help 改前基线（本席实跑两臂＝改前改后均 exit 0 空输出·帮助页将破坏零回归红线）＝否裁论据经实测坐实；位次无关两序逐字节全等＝实现有效且仅两行成本；环境变量不可显式审计＋与仓内 check-pointers --root／--target 惯例（现读在场）不合＝成立。
- **自决②（无值／非整值 fail-fast 申报差量）＝站得住**：无值臂改后 exit 1 带错误行／非整臂 exit 非零均实测复现；保持旧静默空扫＝调线拼错静默假绿反增运维缺口；无任何既有调用方（消费面核查真）＝差量不入回归面。两臂均已在 §二 申报面在册非暗改。

### 红-2 §三 V2 验收命令＝双重假拒式（票面命令自身缺陷）

本席在隔离副本上以票面命令**逐字表达式**（仅按票面自许口径把链上父笔 git show 面置换为改前副本态）实跑：施工完全正确态下该命令 **exit 1**（打印 CHANGED [16..33]＋BLK 77c355e4…）。两处缺陷：
1. 块提取式 blk＝''.join（l＋chr（10） for l in b.splitlines（True）［15:22］）——splitlines（True）已保留行尾，再叠 chr（10）＝行尾加倍 323→非 316 字符面，算出 sha＝77c355e4…≠钉 c2e49c06…（两式对照实测：keepends 不再加 chr（10）或 splitlines（）无 keepends 加 chr（10）＝均 c2e49c06…全等钉）。
2. CHANGED 计算＝zip（a.splitlines（True），b.splitlines（True））按位次对拍前 33 行——纯插入七行后既有行整体后移，位次对拍必判 16..33 全不同＝改行集永不空；票面预期 ⟦CHANGED []⟧ 在该命令形态下**与正确施工态不可同真**（剔除插入区间后对拍＝实测 CHANGED []＋LEN 33 33＝意图本身可达，命令形态未达）。
＝工程师照 §二 正确施工后，验收席照 §三 V2 逐字跑必假拒＝验收链自咬。修单：V2 命令两处形态勘正（块提取去 chr（10）叠加倍行尾＋CHANGED 对拍先剔除插入区间或错位对拍），预期读数行（CHANGED [] LEN 33 40 BLK c2e49c06… DISK 2a549d22…）经本席修正形态实跑全部可达、无需改。

### 黄-1 §二 块逐行 sha 七枚前缀钉口径未声明

票 §二 括注 ⟦块全文 sha256（UTF-8·含行尾 LF 面口径）…七行逐行 sha256 前缀钉＝…⟧：块全文钉 c2e49c06… 含 LF 口径实测全等；但逐行七枚钉只有**无行尾口径**（逐行内容不含行尾符）下七枚全部复现（实测 7／7 MATCH），按块口径自然延伸（行＋LF）则七枚全部不可复现（实测 7／7 MISMATCH）。逐行钉不在 V 系命令链（V2 用块全文哈希）＝不影响验收链，但口径歧义宜在 rev 中一句注明（逐行钉＝无行尾口径）。

## 三、红黄绿计数与结论

- **红 2**：红-1 SCRIPTS 现读计数不实（12→实 11·数字勘正）；红-2 §三 V2 验收命令逐字不可复现（正确施工态下 exit 1·两处形态笔误）。
- **黄 1**：黄-1 块逐行七枚钉口径未声明（无行尾口径才可复现）。
- **绿 8**：靶面判定／硬编码定位／改前基线全套／门禁四件套钉值面／施工规格可照抄性（两步命令＋五臂＋位次两序＋反证臂全过）／体例红线三目／消费面核查／候裁 0 两自决表态站得住。
- **结论＝缓放行**：§二 施工规格本体（两步命令＋块＋锚＋断言）经隔离干跑逐字可照抄、行为五臂与位次无关性全部复现、零回归与零机检增量坐实——票的施工语义无需动；两条红项均为票面自身读数与验收命令笔误，一行级勘正即可（红-1 数字一处＋红-2 命令两处形态＋黄-1 口径一句），修后无需再全轮、窄复核即可。

## 四、对下游的口径提示

- 修 rev 时 §〇 末行仿真臂与 §三 V3 各臂读数经本席复跑全部为真，无需动；仅 V2 命令形态与 SCRIPTS 计数两处。
- 验收轮若工程师已按 §二 正确施工：照 V2 修正形态跑（或等效错位对拍＋块哈希对钉＋盘 sha 对钉三件套），CHANGED []／BLK c2e49c06…／DISK 2a549d22…／LEN 33 40 四项均可达（本席实跑坐实）。

## 五、自证与链衔接

- 本判词落笔前自靶：python share／check-pointers.py --root . --target 本判词实路径 → **exit 0**（读数见完工回报）。
- 取证临时面＝.scratch／debt5rev／（改前副本＋改后仿真件＋块文件＋行为臂快照）＝用毕即拆坐实（rm 后 ls 不存在）。
- 本笔面＝恰本判词一枚；他案脏面零带入；链上史件零回改；账本零手写；.gitignore 零触；FUXI 零碰。

（v1 尾·append-only）
