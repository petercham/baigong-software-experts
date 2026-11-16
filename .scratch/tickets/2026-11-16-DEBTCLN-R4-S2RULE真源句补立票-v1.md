# DEBTCLN-R4 · S2RULE 体例三律②交付面规范真源句补立票（v1·规格票·起草笔零施工）

- 票号：**DEBTCLN-R4**（清债批次第四票·族名锁定，勿改）
- 票名：**S2RULE 体例三律②交付面规范真源句补立票**
- 票型：清债·规范句补立票（规范件纯 append 一行·既有行 byte 零扰动）
- 起草席：架构席 arch-debt4（fresh 实例·主理人派工）
- 票面落点：.scratch／tickets／2026-11-16-DEBTCLN-R4-S2RULE真源句补立票-v1.md
- 来源与裁定依据：债登记行真源＝SWB-RCTPATH-R2 收口登记候补池随动行（收口笔 b2b61d7·件 blob 121111bb·行 18 语义锚隙知会行＋行 29 候补池在册行「三律②真源句另线」）；决策者已裁起票（主理人派工在册）。派工令所称出处「CPPOOL 批次收口候补池」与 R3 票头原误同源，沿 R3 rev1 随正三＋R3 收口笔 6a29879 债销账行勘正链先行随正（旁证＝CPPOOL 收口 1527653 自带「候补池现余＝0 项在排」，该池无此行）。
- 候裁点：**0 枚**（见 §六；两项口径自决并附论证，先例在册）。

> **票面自注（防自咬体例）**：本票正文对一切路径仅叙述性提及＝裸文写＋全角斜杠（／U+FF0F），不落反引号路径指针；引用既有原文以 ⟦⟧ 标记。§二 展示块内＝补立后新行全文逐字，块内零路径 token（新句本体不含任何路径）；§二 施工命令围栏内半角径＝程序准绳（R3 票同形制命令经自靶 exit 0 在册＝围栏内不入机检违例面）。本票面成文后自靶 python share/check-pointers.py --root . --target 本票面实路径 须 exit 0（读数见 §七）。

---

## 〇、开工读数（起草轮现跑·禁抄旧数）

| 项 | 命令 | 实测读数 |
|---|---|---|
| 时点 | date '+%F %T %z' | 开工 2026-11-17 04:10:48 +0800（收尾复跑见 §七） |
| HEAD | git rev-parse --short HEAD | **6a29879**（＝DEBTCLN-R3 收口登记笔·链顶·与派工预期链态相符·父子逐笔 0265a77→7f898b0→c8ef4cc 实跑全等 R3 八笔链账） |
| tracked 脏面 | git status --porcelain | 恰一枚 M＝agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl（他案脏面·禁碰禁入票） |
| untracked 全集 | 同上 | ?? 二十四行（2026-11-12 系列平放 md＋.collab／research／＋仓根杂散等）——全部他案/知会面，不入声明闭集，计数照登当轮值（活体群随外案漂移·禁钉死） |
| 靶件定位 | find 全仓 name=\*20-handoff\*（排除 .git／） | 仓内规范真源＝**恰一枚**＝agent-skills／multi-collab／references／20-handoff.md＝本票靶件。另见同名面非射程照登：①仓根 .scratch／ 取证族与 fuxi 包 .scratch／ 树内 worktree 副本多枚（FX-U14…U39／SWB-A14QAEXEMPT 族·当轮 find 计数照登＝活体群禁钉死）；②邻仓证据备份面 agent-experts／baigong-software-team／.collab／evidence／publish／backup-20261023-＊ 两枚＝ignored 早期快照（R3 rev1 随正二口径：非 tracked·50＋52 行早期形态·不含行 24／行 30 指针句与两域两制节）零触；③.scratch／tickets／ 内 RCTPATH-R3 票面一件＝票面非靶。**结论＝本仓规范面单点债，开票。** |
| 靶件基线哈希 | sha256sum＋git hash-object＋git cat-file | 盘态（CRLF 面口径）sha256＝**68b5de7c**97c397a0cd48086c67e793fd6085205a557b5ec2541d6f1274320321；blob＝**4f6258bbad3758f8d62906df46be78b44f52e4d3**（链＝盘＝工作区净态·git status 对该文件零命中）；blob 面（LF 口径）sha256＝148124c8a10ec23c35916c6689aeee543cf289aa603661376be24cad506dc6c4——三面可对账零矛盾＝R3-QAV 观察「sha256 三口径并存」口径执行，本票登记一律注明口径。 |
| 靶件行数/行尾制 | wc -l＋python 字节计数 | 66 行；盘态行尾制＝CRLF 六十六枚全数一致（append 手段须随动＝施工命令前置断言在册 §二） |
| 锚点行定位 | sed＋逐行 sha256 | 行 28 节题「留存过程件正文内的仓内文件引用写法（两域两制）」（RCTPATH-R3 现役态）sha256＝a8f00e1e…；行 30＝两域两制第 1 目（含「仍照交接件体例三律②＝附含盘符完整本地绝对路径——该律不变」引律句）sha256＝f561c696…；行 62＝§五 节题「五、消息方向律」sha256＝2c588686…；行 66＝§五 末行（投递分件条）sha256＝731e8d8f…＝本票 append 锚（文件末尾追加位）。行 30 内「含盘符完整本地绝对路径」串靶件内命中恰一枚＝现文引律非立句坐实。 |
| 三律②现文分布坐实 | git grep（tracked 全域）＋grep 记忆面 | 交付面规范文件内「三律②」字样＝**恰一枚**＝20-handoff 行 30（引用形态·该节本体只管文件正文域）；体例三律完整成句（①md 落盘②盘符绝对路径③当轮 HEAD 实测）仓内规范面**零枚**＝唯一在册成句居仓外记忆面 .workbuddy／memory／MEMORY.md 行 26（非登记面·非规范件·按本仓「记忆≠事实」律无流程效力）；工具面随动引用＝share／check-ticket-reconcile.py 行 375 注释 ⟦回执指针两形态（ENG-S7 扩认·工具向票面体例三律②「含盘符完整路径」对齐）⟧＝引律名非律文真源。→ **债＝坐实：规范真源件正文点名引用一条交付面无真源的律（语义锚隙已在真源件本体成形＝RCTPATH-R2 QA 判词黄-1 预言态），成文触发条件按该登记行口径成立（条款已引用＋主理人裁起票）。** |
| 新 token 无先例 | git grep 「交接件体例三律②·真源句」tracked 全域 | **零命中**＝补立句新 token 无先例（§二 前置断言 NEWTOKEN-PRESENT 依据） |
| 消费面核查 | grep share／全部闸脚本＋全仓 md | 无脚本消费 20-handoff 行内容作输入：check-collab-lint 行 37 仅注释指 §二 三正面判据条款真源（射程外零触）；check-pointers 行 272 docstring 以本件为写法样例（非内容消费）；check-ticket-reconcile 行 375 注释引三律②字样＝补立后该引用锚落定（工具零改·口径天然对齐）；全仓「两域两制」字样仅 20-handoff 自身；票模板/门禁配置零指 §五/两域两制节。→ append 一行＝对全部消费脚本零输入面变化（V3 论证根基）。 |
| 缺省指针钉值 | python share/check-pointers.py 缺省扫描 grep -c BLOCK／grep -c WATCH | **BLOCK 22809／WATCH 4582**（R3 收口定格新态·与派工预期全等·活体面随外案摆动禁钉死） |
| 靶件改前自靶 | python share/check-pointers.py --root . --target 靶件实路径 | **exit 0**（R3 清偿后零悬空在册） |
| 全仓门禁基线 | bash share／run-gates.sh | **GATE PASS exit 0·发现 151502**（与开工预期基线全等·活体面禁钉死） |
| 消费脚本改前基线 | check-collab-lint／check-source-of-truth 现跑（禁凭记忆填值·R3 红-1 教训执行） | lint **exit 1**（EAC-L1 2006／EAC-L2 4097／EAC-L3 0·分账 EXEMPT 0／SUBSTR 1029／VIOLATION 4097·--selftest exit 0 脚本本体健康）；csot **exit 0**（模式 dual｜文件 129｜BLOCK 0（新命中 0）｜基线豁免 54（WATCH）｜指针 WATCH 413）。 |
| 版本账现态 | grep version SKILL＋changelog 末行＋先例实物 | agent-skills／multi-collab／SKILL.md version **4.11**＝90-changelog 末行 v4.11 同源；先例实物两枚在册：①RCTPATH-R2 条款插入施工笔 **0da2566**（git show --name-only 恰靶件一枚·真条款整节插入·SKILL 未 bump·changelog 零条目·经双席快审＋QA IS_PASS 绿10＋收口放行成链）；②RCTPATH-R3 节题微票施工笔 **80e8612**（同文件单行替换·同形零动）。 |
| 仿真落笔坐实（取证族 .scratch／debt4／·用毕即拆） | 两式实跑 | 式一主体就地 append（§二 同款前置三断言）→ 靶件自靶 exit 0·lint 输出与基线 diff **零行**·csot 计数零变化·缺省 BLOCK 22809／WATCH 4582 **零变化**·GATE PASS exit 0 发现 151502→git restore 三面复原（status 零命中＋盘 sha 68b5de7c＋blob 4f6258bb）。式二隔离副本 append（前置断言反证在册：新 token 在场拒改 NEWTOKEN-PRESENT／行数≠66 拒改 NOT-66-LINES／尾无 CRLF 拒改 NO-CRLF-EOL）→ 产物 67 行·新行 sha256＝**d7c97f79**…（§二 钉值）·盘 sha256＝3e5373c2…·blob＝6ec1a37b…·V2 式对拍打印 CHANGED [] LEN 66 67 exit 0。**＝补立句零自咬·零机检增量·零消费面扰动，坐实。** |

## 一、案件本体与坐实

债＝体例三律②（消息中提及文件必附含盘符的完整本地绝对路径）在交付面规范文件无规范真源句；现行真源只在治理纪律面（用户级记忆成句＋历史拍板件），而**引用该律的条款已在交付面规范件正文在册**（20-handoff 行 30 两域两制第 1 目点名「交接件体例三律②」），工具面亦随动引用（reconcile 行 375）。失步形态＝「纪律只活在记忆里」＋真源件内一条引用无在册所指＝与「引用只指不搬」的引用前提（所指须在册）有隙。

口径辨析（§六 自决①论证）：三律②＝**消息面**纪律；两域两制节＝**文件正文域**规范（其第 1 目自宣「本节约束文件正文域……不约束消息面域」）。故真源句的自然落点不在两域两制节内（塞入即与该节自立域界自相矛盾），而在同件消息面纪律专节＝§五 消息方向律（该节现辖消息方向三条，消息面文件引用体例属同域）。候选 b（该族他件）与候选 c（销账候证）取否理由见 §六 自决①。

## 二、声明闭集（＝恰一枚施工面·文件末尾纯 append 一行·禁酌情）

**S1 · 靶件末尾 append 一行**（新行 verbatim·该文件 §五 bullet 体例·句内零路径 token）：

```text
- **消息面文件引用体例（交接件体例三律②·真源句）**：席位间消息／交接文书在会话与消息内提及文件，必附**含盘符的完整本地绝对路径**——交接件体例三律②的交付面现行规范真源句＝本句，本件两域两制节第 1 目所引「交接件体例三律②」锚本句；三律其余二条（①交接件一律 md 落盘、③来件开端附当轮 HEAD 实测）真源在治理纪律面，交付面不重复成句——成句触发＝后续条款引用该律致执行歧义时另线提级。
```

新行 sha256（UTF-8 无行尾口径）＝**d7c97f79717c85c86b5cdac768dae937c952695edee0eafdf00db30043690b42**（起草轮仿真实跑钉版·V2 复算）；新行字符数 203。

**施工手段规格（唯一准绳·程序化 append＋三重前置断言防手误）**：

```bash
python -c "p='agent-skills/multi-collab/references/20-handoff.md';s=open(p,encoding='utf-8',newline='').read();b='- **消息面文件引用体例（交接件体例三律②·真源句）**：席位间消息／交接文书在会话与消息内提及文件，必附**含盘符的完整本地绝对路径**——交接件体例三律②的交付面现行规范真源句＝本句，本件两域两制节第 1 目所引「交接件体例三律②」锚本句；三律其余二条（①交接件一律 md 落盘、③来件开端附当轮 HEAD 实测）真源在治理纪律面，交付面不重复成句——成句触发＝后续条款引用该律致执行歧义时另线提级。';assert s.count('交接件体例三律②·真源句')==0, 'NEWTOKEN-PRESENT';assert s.count(chr(10))==66, 'NOT-66-LINES';assert s.endswith(chr(13)+chr(10)), 'NO-CRLF-EOL';open(p,'a',encoding='utf-8',newline='').write(b+chr(13)+chr(10));print('APPENDED-1')"
```

（断言＝新 token 零先例否则拒改／基线恰 66 行否则拒改／盘态尾行 CRLF 否则拒改——行尾制随动断言系本件 CRLF 实测态所定（§〇 行尾制行在册）。产物＝同文件 67 行·既有 66 行 byte 零扰动；工程师用其它手段须同等过 V1／V2。）

**改后靶件预期态（仿真钉版·复算基准非验收钉值）**：67 行；blob＝6ec1a37bcff229e204a2c62f8a62cecc151106fe；盘态 sha256＝3e5373c252f987698a7bd2ff1eb23b30d4cb6f2f472d0d7280ae316b039e0261（CRLF 面口径）。

### 禁动面（写死）

- 靶件既有 66 行全部 byte 级零扰动（含行 24（R3 清偿态）／行 28 节题／行 30 两域两制第 1 目引律句——**不改行 30 加锚**，同文件同名律名成锚，见 §六 自决①末段／§五 全部三行）。
- 版本账零动：agent-skills／multi-collab／SKILL.md frontmatter version 4.11 不 bump；90-changelog 零新增条目（口径自决②·先例实物在册·见 §六）。
- 60-gates.md 行 110 同族第二例活体悬空零触（观察行候另案，§四）。
- fuxi 包 .scratch／ 树内全部 20-handoff 副本零触（FUXI 零碰）；邻仓证据备份面 ignored 两枚零触。
- 他案脏面零带入：ledger.jsonl 之 M 态＋?? 当轮全集＝禁碰禁入库。
- 链上史件零回改；账本面零手写；.gitignore 零触。

## 三、验收判据（全机械·命令＋钉值·禁凭记忆填值）

- **V0 开工读数**：施工轮现跑 HEAD＝6a29879 链上本票落链后最新值如实照登；git status 他案脏面形态与 §〇 一致（ledger 一枚 M＋?? 当轮值照登——他案归因禁扩集·R1-GCLOSE／R2／R3 先例口径；本票落链后本票面转 tracked，?? 不含本票）。
- **V1 真源句落位（靶件面）**：
  1. grep -c 新 token「交接件体例三律②·真源句」于靶件 ＝ **1**；于靶件既有态基线（git show HEAD 前态）＝ **0**（前置断言复证）。
  2. python share/check-pointers.py --root . --target agent-skills／multi-collab／references／20-handoff.md → **exit 0**（改前基线 exit 0 在册 §〇；新句零路径 token＝零指针增量，仿真在册）。
- **V2 append 单行判据（REST-EQUAL 式）**：git show --numstat 于施工笔＝**1／0**（纯 append 零删除）；逐行对拍改行集＝**[]（既有行零改动）**＋行数 66→67＋新行哈希对钉：

```bash
python -c "import subprocess,hashlib;b=open('agent-skills/multi-collab/references/20-handoff.md',encoding='utf-8').read().splitlines();a=subprocess.run(['git','show','HEAD^:agent-skills/multi-collab/references/20-handoff.md'],capture_output=True).stdout.decode('utf-8').splitlines();d=[i+1 for i,(x,y) in enumerate(zip(a,b)) if x!=y];print('CHANGED',d,'LEN',len(a),len(b),'L67',hashlib.sha256(b[66].encode('utf-8')).hexdigest());raise SystemExit(0 if d==[] and len(a)==66 and len(b)==67 and hashlib.sha256(b[66].encode('utf-8')).hexdigest()=='d7c97f79717c85c86b5cdac768dae937c952695edee0eafdf00db30043690b42' else 1)"
```

→ **exit 0** 且打印 CHANGED [] LEN 66 67 L67 d7c97f79…（基线以施工笔父笔链上态为准；HEAD^ 写法按排程本笔父＝该笔前链顶，工程师按实际父笔 sha 置换并照登）。
- **V3 消费面零变化**：check-collab-lint 现跑 **exit 1 与 §〇 实测基线 exit 1 全等**＋计数照登（EAC-L1 2006／EAC-L2 4097／EAC-L3 0·VIOLATION 4097）＋改前改后输出 diff **零行**＝findings 零新增（仿真在册）；check-source-of-truth 现跑 **exit 0 与基线全等**＋计数照登（BLOCK 0／豁免 54／指针 WATCH 413）——有差＝如实照登＋归因，禁遮掩禁扩集；reconcile 行 375 工具注释零改＝引用锚落定属语义面非输入面（消费脚本输入零变化先验＝§〇 消费面核查）。
- **V4 缺省扫描与门禁**：python share/check-pointers.py 缺省扫描 grep -c BLOCK／grep -c WATCH → 预期 **BLOCK 22809／WATCH 4582 双零变化**（新句零路径 token＝零指针增量·仿真逐值在册）；60-gates 行 110 BLOCK 零变化＝零触归因；fuxi 树副本 BLOCK 零变化＝FUXI 零碰归因。bash share／run-gates.sh → GATE PASS exit 0，发现数照登（基线 151502·活体面随外案摆动禁钉死·变化归因照登·**禁总数增减类伪钉值**）。
- **V5 自靶**：python share/check-pointers.py --root . --target 施工后回执实路径 → exit 0；本票面（链上现文）同式 exit 0 复证。
- **V6 笔面单恰靶件**：口径照 R2 收口登记 §四 终版＝**核验时点 git diff --cached --name-only 实测 staged 恰靶件一枚（或本笔面单件）＋钩子 STAGED-DECL 互证为准**；commit 树面并发窗裹入他案＝归因在册不构成施工违例；禁写总数增减类伪钉值。

## 四、观察行（随登·不立项不候裁）

- 60-gates.md 行 110 同 token 活体悬空一枚＝同族债第二例在册未销（R3 观察行续登），候补池候另案候排。
- 三律①③交付面不成句＝本票显式设触发（后续条款引用致歧义时另线提级）；本批零处置坐实，防 scope 扩面。
- reconcile 行 375 工具注释对三律②的引用＝真源句立后锚落定；注释文本是否随动补指新句＝工具面零改观察行（语义已闭合，禁顺手扩面）。
- sha256 三口径并存观察（R3-QAV 随登）沿用：本票 §〇/§二 全部登记已注明口径（盘 CRLF 面值／blob 值）。

## 五、排程（串行两笔施工段）

链第 1 步＝本票起草笔（架构席·本笔）。第 2 步＝双席快审（产品席＋QA 席 fresh eyes：审 S1 新行可照抄性·V 系完备性·口径自决两项取舍·落点择一论证）。第 3 步＝放行登记（主理人）。第 4 步＝工程师施工一笔（靶件一枚·§二 命令）＋**回执一笔**（落 .collab／receipts／ 桶·R1 勘正口径）。第 5 步＝fresh QA 按 §三 V 系独立验收判词。第 6 步＝收口登记（主理人）。

## 六、候裁面（必有节·**候裁 0 枚**）

- **自决① · 落点口径＝候选 a 之 a2 形态：20-handoff §五 消息方向律末 append 真源句一行**（禁硬塞·YAGNI＋单真源优先·三选一自决附论证）：
  - **取 a2 理由**：三律②＝消息面纪律；20-handoff 内消息面域专节＝§五 消息方向律（现辖消息方向三条＝同域）。真源句入 §五＝纯 append 一行·不触任何既有行·bullet 体例同源·消费面（行 30 引律）同件闭合＝在文件内闭环零跨包新指针。
  - **否 a1（两域两制节内补句）**：该节第 1 目自宣 ⟦本节约束文件正文域……不约束消息面域⟧——消息面真源句塞入该节＝与节内自立域界正面互搏（体例自相矛盾）；且行内扩展触既有行，成本高于纯 append。
  - **否 b（该族他件：10-roles＝席位与决策权分层／30-formats＝交付物格式规格／50-antipatterns＝反例集／60-gates＝门禁表／70-charter＝章程纪律／90-changelog＝沿革账·Glob 实证现役件名如上）**：无一为消息面行为纪律专面；20-handoff 是该族唯一携消息面纪律之件（§五），且引用侧（行 30）即在 20-handoff——真源与引用跨件分居反增互指面。
  - **否 c（销账候证＝纪律真源归用户级记忆层）**：记忆面按本仓自立之律「记忆≠事实」＋记忆中立化在册＝无登记效力；交付面条款（行 30）与工具注释已点名引用该律＝语义锚隙已在规范件本体成形，销账＝永久承认规范件悬空引用，与该登记行自设之出路（「归规范面另线候排；成文触发＝条款引用致歧义时提级」——引用已在·主理人已裁开票）相悖；双真源风险不成立＝记忆面成句非登记真源，立句即唯一在册真源，消「纪律只活在记忆里」失步正是本债销法。
  - **不改行 30 加显式锚**（随 a2 附带取舍）：同文件同名律名（「交接件体例三律②」）出现即成锚，行 30 零触保既有行 byte 稳定；若双席或主理人认须行 30 补「见 §五」式指句＝随其裁落另出微票，不预判。
- **自决② · 版本账零动**：本笔＝真源句补立＝对既有条款语义零变化（行 30 引律句语义不变·两域两制制度不变）。先例实物两枚在册：①同件同族**条款整节插入**先例 RCTPATH-R2 施工笔 0da2566＝name-only 恰靶件一枚·version 前后均 4.11 未 bump·changelog 零条目，经双席快审＋fresh QA IS_PASS＋收口放行成链；②同件单行改先例 RCTPATH-R3 80e8612 同形零动。同案同判。若双席快审或主理人认须 bump 4.11→4.12＋changelog 补行＝随其裁落，不预判。

批次编排类不上楼＝不自列候裁；两项均属票内口径归起草席位闭合（handoff-discipline §十一-2 程序内裁量）。

## 七、起草笔自证（落笔后、commit 前实跑）

- 开工读数＝§〇 全表（当轮现跑·HEAD 6a29879·收尾时点见完工回报）。
- 本票面自靶＝python share/check-pointers.py --root . --target .scratch／tickets／2026-11-16-DEBTCLN-R4-S2RULE真源句补立票-v1.md → **exit 0**（实跑坐实·读数见完工回报）。
- 防自咬体例取证在册（.scratch／debt4／ 取证族·用毕即拆口径见回报）：probe 行 30 现文＋补句拼接体＝--target exit 0；新句 verbatim 件＝sha256 与 §二 钉值 d7c97f79 全等；§〇 仿真落笔两式（就地式＋隔离副本式）全套读数在册（§〇 末行），复原三面坐实（status 零命中／盘 sha 68b5de7c／blob 4f6258bb）——本票笔成文时点靶件仍＝改前净态（修票不施工·git status 对靶件零命中在册）。
- 靶件基线双哈希＋行尾制＝§〇 在册（盘 sha256 68b5de7c…CRLF 面／blob 4f6258bb…／行 28・30・62・66 四行 sha256 定位钉／CRLF 66 枚）；V2 基线以本票落链后链上笔为准（本票笔不触靶件，HEAD 态靶件哈希不变）。
- 本笔面＝恰票面一件；其余全程零触碰；他案脏面零带入。

## 八、链衔接纪律段（各笔共守·写死）

- 单件／本笔面 pathspec 两端齐带（add 与 commit 各带本笔面路径）；add 紧邻 commit 零窗口；commit 前 git diff --cached --name-only 坐实仅自笔面。
- FX_COMMIT_DECLARE＝仓根相对纯路径清单（逗号或换行分隔）**挂 commit 命令侧**（挂 add 侧会被 STAGED-DECL-BLOCK 拦）。
- 禁 add -A／禁 amend／禁 --no-verify；message 以 collab: 起头·零 at 符号·零反引号；尾标置 message 最末位。**本票各笔尾标闭集**：本票笔 -TICKET／QA 快审笔 -QA-REV／产品快审笔 -PM-REV／放行登记笔 -PM-RELEASE／工程师施工笔 -BUILD／工程师回执笔 -RECEIPT／QA 验收笔 -QAV／收口登记笔 -GCLOSE（族名 DEBTCLN-R4 随尾标内嵌）。
- 一票一 commit 增量落盘；commit 类命令 timeout 600000ms；撞 index.lock 有界等待零删锁。
- 防自咬体例＝票面／回执正文路径裸文＋全角斜杠叙述形态；引文 ⟦⟧；票面与回执自身须过 check-pointers --target exit 0 后才可落链。
- 临时工作物只落仓根 .scratch／debt4／ 族；本席起草笔只写票面这一件。

---

（v1 尾·append-only：后续修订在此处续 rev 段，rev 段间互不回改）
