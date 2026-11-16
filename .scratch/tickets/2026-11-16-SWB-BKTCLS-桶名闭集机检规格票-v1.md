# SWB-BKTCLS · 仓根 .collab 桶名闭集机检规格票（v1·纯规格·零施工）

- 票号：**SWB-BKTCLS**
- 票名：**仓根 .collab 桶名闭集机检规格票（移交工单 v3 A14 在册缺口修路）**
- 票型：维护（机检规格票·体例照 SWB-CPTRACE／CPRC4／CPRC5／A14H1 先例·施工归后续工程师席）
- 起草席：架构席 arch-cpool3
- 票面落点：.scratch／tickets／2026-11-16-SWB-BKTCLS-桶名闭集机检规格票-v1.md
- 来源：候补池在册项「桶名闭集机检（A14 候②）」＋移交工单 v3 A14 行（.collab／decisions／2026-11-09-移交工单-百工软件团队层问题汇总-v3.md 行 A14：「增 .collab 桶名闭集校验机检项：闭集外桶名即报违例（建议挂维护侧同类闸时同型实现）」）
- 候裁点：§六（本票预期零枚·见彼节说明）

> **票面自注**：本票正文对一切路径仅叙述性提及＝裸文写＋全角斜杠（／U+FF0F），不落反引号路径指针＝防自咬体例；引文块承载原文时反引号内容以 ⟦⟧ 标记替换。

---

## 〇、开工读数（起草轮现跑·禁抄在册旧数）

- git rev-parse --short HEAD ＝ **9fb9256**（＝票一落链后链顶·开工读数如实登记·晚于派工预期 34431fb＝本票链段自带票一笔）。
- 门禁构成现跑取证（留痕＝本席 scratch 族 gates-run.txt·--no-write 只读模式）：bash share/run-gates.sh --root . --no-write → **exit 0·GATE PASS（发现 151502 条）**——在册钉值 151508 与本次现跑 151502 差 6 枚＝如实登记读数差（在册钉值系 A14H1 施工笔口径；本票不追因、验收轮以当轮现跑对拍为准）。
- 门禁脚本名单现读＝share／run-gates.sh 行 141 SCRIPTS 清单一行：**10 项**（check-provenance／check-skill-meta／check-pointers／check-entity／check-collab-lint／check-pointer-closure／ROOT／share／check-source-of-truth／check-ticket-reconcile／check-adr／check-hook-health——末项经 ROOT／ 前缀跨域挂载形态·清单项两种形态注释在源码行 136-140 在册）；循环体＝行 144-155（同域裸名→SELF_DIR 解析·ROOT／ 前缀→仓根相对解析）；pre-commit 钩子调用序现读＝钩子行 6 声明闸在前、行 7 run-gates 在后。
- 路由表现读＝agent-skills／multi-collab／references／60-gates.md json 围栏恰一处：per_spec **25 条目**＋on_severity 3 档＋escalate 5 键（在册称「门禁 79 条」口径见 .workbuddy／memory／MEMORY.md 行 49＝条款总账口径·非路由表条目数·本票不复算）。
- 桶面现盘枚举（本票机检闭集的实测底）：仓根 .collab／ 一级目录实存 **15 个**＝audits／ board／ decisions／ design／ dispatch／ drafts／ evidence／ inbox／ ledger／ process／ qa／ receipts／ refs／ research／ returns；一级直落散文件群（untracked 案卷散件 16 枚＋README.md）照登。
- 闭集成册值现读＝仓根 .collab／README.md 「17 桶名录」行（行 29）：**decisions／ audits／ receipts／ board／ design／ research／ refs／ evidence／ inbox／ process／ dispatch／ drafts／ adr／ architect／ product／ ledger／ returns／**＋README 索引件；在册效力源＝皮总裁定登记件 .collab／decisions／2026-11-10-皮总裁定-候裁三件全按建议放行.md §二-2 裁甲（**17 桶闭集只管仓根 .collab**；两包 qa／ 随批改名豁免）。
- 现盘与闭集对拍（差集现算）：**qa／ ＝闭集外桶·实存·内藏受跟踪文件 7 枚**（git ls-files .collab／qa 计数＝7·A14QAEXEMPT／SCRATCHCFG 等 11-10 后判词件落点）＝**当前唯一存量违例**；adr／ architect／ product 三桶在册但盘上不存在＝不判违例（闭集＝白名单制非必存制）；历史残留句（README 行 35）称历史案卷内 .collab／qa／ 字样读作 audits／——但现盘 qa／ 桶内为 11-10 后**新落件**非历史残留＝违例坐实非语义遗留。
- 射程外事实照登：嵌套 .collab 面（agent-experts／baigong-software-team／.collab／ 含 adr／architect／product／defects 外无违例·agent-skills／fuxi-skill／.collab／ 含 defects／ 与 tickets／·external-advisor-collab 包含 inbox／）＝按裁甲**不入本票射程**（17 桶闭集只管仓根）。
- 他案脏面照登零带入＝ledger 一枚（M 态）＋仓根散件群＋亡席残族；index 除本票单件外零 staged。

## 一、案件本体与缺口坐实

仓根 .collab／ 桶名结构闭集（17 桶）成文处＝规范真源（.collab／README.md 名录行）＋.gitignore 两处，**无目录面机检**——桶名随写随造。实证两案在册：①defects／ 桶（11-08 笔 36dfb78 落点）→迁册票 v1 fb76547 落链、11-09 收口销账（工程 c79dde9 git mv＋回执 9ebc94f＋QA 判词 883aa68＋收口登记 111b67a·迁册票真源＝.collab／decisions／2026-11-09-迁册票-仓根defects桶违闭集-v1.md·其 §④ 注记「桶名闭集无目录面机检（移交工单 v3 A14 实证在册）＝本票只消解存量违例，机检闸门归 v3 A14 条目排程」）；②**qa／ 桶＝本票开工轮现盘实证仍在**（存量未消解·0 枚机检在岗＝再落件无人拦——本票 §〇 现算坐实）。缺口＝A14 案候②·A14 实证在册。

## 二、规格正文（机检设计）

### 2-1 落点与实体

- 新增检查脚本＝**share／check-collab-buckets.py**（仓根 share 桶·与十同侪同族·只读·唯一写动作仍在 run-gates.sh 出口②）。
- 挂载＝share／run-gates.sh 行 141 SCRIPTS 名单增一**同域裸名项** check-collab-buckets（形态①·行 144-148 解析路径自动命中 share／ 下同名脚本·零循环体改动）。
- 路由随挂＝60-gates.md json 围栏 per_spec 增一条目 ＝ "MC-BUCKET-1": {"commit": "block"}（路由表＝唯一机器源·读表规则 5 要求 spec_id 可在提供者规范件解析到·见 2-5）。

### 2-2 判据（闭集断言·白名单制）

- 扫描域写死＝**仓根 .collab／ 一级子目录**（os.listdir 单层枚举·不递归·不扫嵌套 .collab——射程口径＝皮总裁甲在册句「17 桶闭集只管仓根 .collab」）。
- 判定＝枚举所得目录名 ∉ 内嵌白名单 17 项闭集 ⇒ 输出一行违例；一级**文件**不判（散文件群另有观察账·非本闸射程）；README 索引件不判。
- 违例输出行形态（照铁律「严重度＋spec_id＋位置＋一句话」·同侪 file:line 前缀兼容 run-gates FINDING_RE）＝违例桶仓根相对径＋:1: BLOCK MC-BUCKET-1 桶名闭集违例（桶名 X ∉ 17 桶名录）——line 恒 1＝目录级检查定位约定（先例＝check-collab-lint EAC-L3 目录级检查 line 恒 1 在册形态）。
- 空面 fail-closed：仓根 .collab／ 不存在＝基础设施错 exit 4（仓根异常不得静默放行）；.collab／ 存在且零违例＝exit 0。退出码闭集照 60-gates §六（0／1／2／4）。

### 2-3 闭集真源同步防线（防两源漂移）

- 白名单 17 项以 frozenset 内嵌脚本＋随附 **README 对拍自证**：脚本运行时解析 .collab／README.md 「17 桶名录」行（行 29 锚字样「17 桶名录」），解析所得集合 ≠ 内嵌集合 ⇒ 输出 WATCH MC-BUCKET-1 名录漂移行（两源不一致本身即报）——闭集改动必须两处同步，改一漏一即红。
- 防自咬：脚本自身文件内一切桶名例证一律不落可解析反引号指针（照 check-collab-lint 头注自咬纪律先例）。

### 2-4 豁免口径

- **无豁免面设计**：闭集外桶唯一合法消解路径＝迁册（git mv＋指针随动＋靶检 exit 0·defects 先例 c79dde9 全链在册形态）或闭集名录本身经裁定扩容（规范真源改动＝另走裁定链·见 §六）。不设豁免快照文件（对照 A14 豁免快照教训＝豁免命中仍出 WATCH 行不可闭）。

### 2-5 spec_id 与规范真源配套

- MC 前缀经 SPEC_ID_HOME 映射提供者＝multi-collab（run-gates.sh 行 215-221 在册映射）；读表规则 5 解析径＝agent-skills／multi-collab 规范件里须出现 MC-BUCKET-1 或 BUCKET-1 字样——**配套施工目（列入票内声明闭集）**＝agent-skills／multi-collab／references/ 规范件（建议 60-gates.md 或 20-handoff.md 择一·施工轮现读定）增一条目＝「仓根 .collab 桶名闭集校验」条款行（内容＝判据一句话＋指向本闸实体·不复写参数）。此＝门禁工具线既有框架内的配置随挂（移交工单 v3 A14 行修法列「门禁工具线（check-collab-lint／run-gates 域）」在册授权），**非新流程条款**。

### 2-6 存量违例消解（首跑归零前置·同票同批）

- 施工顺序写死＝**同票声明闭集内先迁 qa／ 后挂闸**（或同批原子落链·顺序＝迁册笔→挂闸笔）：qa／ 7 枚受跟踪件 git mv 入 audits／（审计判词性质归 audits 桶·README 桶总表行 10「审计结论／验收判词」定性在册；取态唯一·不留二择一避免执行期裁量——内容属性现读＝7 枚均为 QA／产品判词件）；链上史笔不追改（在册口径）；指向 .collab／qa／ 的受跟踪引用件全仓 grep 逐件随动＋靶检 exit 0（照迁册票 §②-4 工序）。
- 首跑预期＝挂闸笔起 BLOCK 违例读数 **0 枚**（存量已先消）；若 qa／ 处置翻案（决策者裁扩名录纳入 qa／），17 桶名录行随裁改 18＋脚本白名单随动＝另出修订轮·本票不预写。

## 三、影响与钉值评估（写死）

- check-pointers 缺省 BLOCK 钉值 **22816 零扰动**：本闸为独立新脚本，不改 check-pointers 任何口径；已知事实照登＝check-pointers DEFAULT_SCOPE＝agent-experts／agent-skills／softwares 三分类（源码行 76），缺省扫描域不含 .collab（裁-23 拍板 2 排除·源码行 53 在册）也不含 share／——本闸域口径＝仓根 .collab／ 单层·与 DEFAULT_SCOPE 零交集、不复用其口径。
- GATE 发现数：挂闸后当轮起 ＝现跑基面 **＋0**（首跑违例预期 0·存量已同批消解）；qa／ 迁册笔自身对发现数的影响＝7 件换路径不涉 BLOCK 计数面（audit 件内指针随动改径后靶检归零），预期波动 ≤ 个位且随迁册笔 GATE PASS 读数现场坐实（在册钉值口径差异照登不归本票追因）。
- 钉值随登义务＝验收轮现跑 run-gates 全量读数与当轮在册钉值对拍，差值逐项归因（本闸贡献行数＝0）。
- pre-commit 钩子时序零触（声明闸→run-gates 两段不变·新脚本在 run-gates 循环内获得位置）。

## 四、V 系机械验收判据（每条＝可照跑命令＋预期）

- **V0 首跑归零**：挂闸笔落链后 bash share/run-gates.sh --root . --no-write → exit 0；全量输出 grep -c "MC-BUCKET-1" 违例行＝**0**。
- **V1 闸有牙（对抗臂）**：scratch 族内造假桶探针＝mkdir .collab／zprobe／ （违例桶·空目录·探针毕即删）→ 单跑 python share/check-collab-buckets.py --root . → **exit 1·恰 1 行 zprobe 违例**；删探针复跑＝exit 0。臂二＝README 名录行副本删一词→WATCH 漂移行出现＝对拍自证有牙（副本面跑·原件零触）。
- **V2 存量消解坐实**：git ls-files .collab／qa 输出空；ls 仓根 .collab／ 读数零 qa 目录；git log --follow 新路径 exit 0（改名保史）；git grep 旧径受跟踪引用零命中。
- **V3 域口径写死复证**：fuxi-skill 包 .collab／defects／ 现盘在场（射程外事实）→单跑本闸＝该桶**零命中行**（只管仓根·裁甲复证）。
- **V4 缺省钉值零扰动**：python share/check-pointers.py 现跑 grep -c "BLOCK" ＝跑前跑后同值（22816 或当轮实测值·双读数现跑落盘）。
- **V5 挂载形态**：git show --name-only 各施工笔＝恰票内声明闭集件；run-gates.sh diff＝SCRIPTS 名单行恰增一裸名项·循环体零 diff；60-gates.md diff＝json 围栏恰增一条目＋围栏仍恰一处（围栏数≠1＝run-gates exit 4 自爆在先）。
- **V6 防自咬**：新脚本自身与施工回执靶检 exit 0；本票面落笔前自靶 exit 0（见 §七）。

## 五、禁动面

- check-pointers.py／DEFAULT_SCOPE／豁免快照三件／SKIP 两表一字不动；run-gates.sh 除行 141 SCRIPTS 名单行外全域不动（循环体／裁决 PY 段／SPEC_ID_HOME 映射不动——MC 前缀映射已在册无需增改）；路由表 json 围栏除增一 per_spec 条目外其余条目不动；check-collab-lint.py 全域不动。
- 嵌套 .collab 各包桶面零碰（裁甲射程外）；仓根 .collab／ 一级散文件群零碰零清理（照登）；他案脏面照登零带入；链上 FUXI 笔群零碰零代裁。
- qa／ 桶 7 枚件内容零改字（纯迁册·git mv R100 预期）。

## 六、候裁面（预期零枚·说明）

**候裁枚数＝0。** 逐面自查：①本票涉门禁配置面（SCRIPTS 名单／per_spec 条目／规范件配套条款行）＝移交工单 v3 A14 行在册修法列「门禁工具线」＋A14 候②候补池在册项＝**已批框架内执行分解**，不立新流程条款；②17 桶闭集本体＝已在册裁定（裁甲）复用，本票零新增规范；③qa／ 处置取态＝迁册（defects 先例同型·机械迁册未达流程变更判据·迁册票先例 fb76547 口径）；若验收或复审轮翻出真决策者范畴项（如决策者欲扩名录纳入 qa／），随该轮另列呈裁，不回改本票（append-only）。

## 七、纪律段（起草笔自证）

- 增量落盘＝骨架先落工作区·逐段填实·成文＋自靶 exit 0 后一次落链；本票面防自咬＝路径裸文＋全角斜杠·引文块 ⟦⟧·落笔前 python share/check-pointers.py --root . --target 本票路径 exit 0；
- 单件 pathspec 两端齐带·add 紧邻 commit 零窗口·commit 前 git diff --cached --name-only 坐实仅自件·FX_COMMIT_DECLARE＝本笔实触仓根相对纯路径清单前置·禁 add-A／禁 amend／禁 no-verify·message collab: 起头零 at 零反引号·尾标 [SWB-BKTCLS-TICKET] 置最末位·commit 输出重定向 .scratch／cpool3／·Bash commit 类 timeout 十分钟档·撞锁有界等待零删锁；
- 临时工作物居 .scratch／cpool3／（gates-run.txt／selfgate-*.txt／commit-*.txt）完工自删（commit 留证保留）；
- 本起草笔只写票面一件；share／ 下零触碰（施工归后续工程师席按 §二 执行）。

## 八、rev-1 更正段（append-only·作者席 arch-cpool3·双席快审会师对拍处置·已落链正文一字不改·后文读数以本段为准）

- rev 轮开工读数＝git rev-parse --short HEAD 现跑（本笔 add 前现读·登记于完工回报）；前笔链顶含票一 rev 笔 f5d50c7。

### 更正一（§〇 per_spec 现跑读数错登）

正文 §〇「路由表现读＝…per_spec **25 条目**」错登。双席独立现跑一致＝per_spec 实为 **22 条目**（QA 席以 python 解析 json 围栏＋窗口 diff 排除读数漂移坐实）。**22 为本票链段实测数**；正文 25 作废不回改（append-only），验收轮对拍以 22＋当轮现跑为准。骨架零伤：2-1／2-5 挂载规格不依赖该计数。

### 更正二（§四 V2 判据射程写死·承重修正）

正文 V2 第三目「git grep 旧径受跟踪引用零命中」**字面不可机械满足**：实测全仓 collab／qa 字样命中 251 枚文件，横跨三面无合法消解路径＝①裁甲豁免面（两包 .collab／qa／＝禁动射程外）；②链上史面（append-only 不追改）；③迁移 7 枚件内文自引 5 枚（迁册内容零改约束 R100）。照跑必红＝判据自身违机械可判性。**V2 第三目作废，改写为两层射程口径（此后读数以本段为准）**：
- 层一（路径面）＝**git ls-files 域内不再有 .collab／qa／ 前缀路径**：判据命令＝git ls-files 输出 grep -c 该前缀路径＝**0**；
- 层二（内文面）＝迁移 7 枚件换径后**其内文指针不因迁移翻红**：判据＝对迁移后新路径逐件 python share/check-pointers.py --root . --target 新路径 各 **exit 0**（件内文零改＝内容零改约束下自引基名／相对形态仍可解析＝照豁免与内容零改约束成立）。
- 两层皆绿＝V2 绿；全仓 grep 零命中表述**禁用**（该口径不再作为任何验收依据）。

### 随注（GATE 读数钉值差归因一句话）

正文 §〇 现跑 151502 与在册钉值 151508 差 6 枚：QA 席 rev 轮现跑已回钉值 **151508**（本席票一 rev 笔 commit 输出同步复见 151508＝互证坐实）；差因＝票起草时点链态差异（起草窗内他案笔涉指针面波动），不追因、不影响本闸「首跑违例预期 0」判据（V0 grep -c MC-BUCKET-1 违例行口径独立于发现数总量）。

### rev 段纪律自证

append-only＝本段落链笔不改正文任何既有字句（git diff 本笔＝纯尾部追加）；路径例证裸文＋全角斜杠·零反引号包径；落笔后本票自靶 exit 0 才 commit；单件 pathspec·FX_COMMIT_DECLARE 纯路径前置·尾标 [SWB-BKTCLS-REV1] 置最末位·commit 输出重定向 .scratch／cpool3／·timeout 十分钟档·撞锁有界等待零删锁。
