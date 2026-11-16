# DEBTCLN-R1 · 仓根散件迁册票 v1 · QA 席 fresh eyes 快审判词 v1

- 判词件：．collab／audits／2026-11-16-DEBTCLN-R1-快审判词-QA席-v1.md
- 审计对象：．scratch／tickets／2026-11-16-DEBTCLN-R1-ROOTCLN仓根散件迁册票-v1.md（链上版为准）
- 审型：快审（不施工·只审票面可施工性与判据可机械性）·体例照 SWB-RCTPATH-R3 快审先例
- 审席：QA 席 qa-debt1rev（fresh 实例·经主理人派工·未与起草席直连）

## 开工读数（本席审轮现跑·禁抄票值）

| 项 | 命令 | 本席实测 | 票面登记值 | 对拍 |
|---|---|---|---|---|
| 时点 | date '+%F %T %z' | 2026-11-16 21:0x +0800 | 2026-11-16 20:17:33 | 轮次差·正常 |
| HEAD | git rev-parse --short HEAD | b2bceb8 | 起草轮 2683594 | 票落链后 HEAD＝b2bceb8·与派工预期全等 |
| 票面钉版 | git ls-tree b2bceb8 票面路径 | blob eeb7719c527ffbcf50e03042b9b22a951c8dc8a0 | — | **全等**·审读以 git show b2bceb8 链上版为准 |
| tracked 脏面 | git status --porcelain | 恰一枚 M＝agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl | 同 | 全等·他案脏面本席零带入 |
| untracked 行数 | 同上 grep -c ?? | 二十三行 | 二十三行 | 全等 |
| 缺省指针钉值 | python share／check-pointers.py 缺省扫描 grep -c BLOCK／WATCH | BLOCK 22810／WATCH 4581 | 22810／4581 | 全等 |
| 全仓 GATE | bash share／run-gates.sh --no-write | GATE PASS exit 0·发现 **151502** | 151502 | 全等（见黄-3 前提条件） |
| 桶闸 | python share／check-collab-buckets.py | exit 0·一级目录判 14 枚｜违例 0｜名录对拍 一致 | 同 | 全等 |
| 链上锚 | git cat-file -e sha^{commit} 逐枚 | fb76547／c79dde9／9ebc94f／883aa68／111b67a／b2b61d7／ca33b5f／e49977a 八枚全 exit 0 | 同＋e49977a | 全在位 |
| 票面自靶 | python share／check-pointers.py --root . --target 票面实路径 | **exit 0** | exit 0 | 复证成立 |

本席全程零施工：主仓工作区除本判词一件外零改动；模拟施工全部落仓根 ．scratch／QA-DEBT1REV／ 族内一次性 worktree，取证毕已 git worktree remove --force 拆除并复跑钉值归位。

---

## 判词（红黄绿逐号）

### 绿-1 · 开工读数与在盘面对拍＝成立

- status 面：tracked M 恰一枚＝ledger 他案脏面，untracked 恰二十三行（仓根 ．collab／ 平放十二枚＋．collab／research／ 六枚＋仓根杂散五枚），与票 §〇 逐行登记形态一致。
- 仓根 ．collab／ tracked 一级平放：git ls-files ．collab／ 一级过滤＝**六枚**＝票 §二之一 所列五枚 md ＋ README.md（桶索引件·名录内合法存续）。票 §〇「五枚 md＋README」口径**属实**。
- 票 §〇「桶目录内 tracked 件共 216 枚」＝222−6＝216 **自洽**；git ls-files ．collab／ 总数实测 **222** **属实**。
- 结论：票面对在盘面的登记无虚报、无漏报。

### 绿-2 · 声明闭集完备性＝成立

- 五枚旧路径逐枚 git ls-files --error-unmatch 实证存在＝OLD_EXISTS 五枚全过。
- 目标桶零撞名：test -e 新路径逐枚＝TARGET_FREE 五枚全过（decisions 桶现有 tracked 件 120 枚内无同名）。
- 新路径落白名单：现读 share／check-collab-buckets.py 内嵌 BUCKET_WHITELIST frozenset 十七项含 **decisions**；与 ．collab／README.md「17 桶名录」行逐项对拍一致（闸自证对拍读数「名录对拍 一致」在册）。禁猜桶名条款满足＝白名单系现读非猜。
- 桶归属论证可核：README 桶总表 decisions 行 verbatim＝「裁定／裁决／收口登记（append-only·逐字誊录）」含「收口登记」字样；同线先例实证＝e49977a（COLLAB-STRUCT-1 施工笔）message 明登「仓根 ．collab 根面 20 件治理史散件逐件 git mv 同名归位 decisions（全 R100·根面散件终值 0）」，且 ．collab／decisions／ 现存呈拍简报同型件多枚（2026-11-04-SWB-ADR工序票-呈拍简报-v1 等）。票 §二之二 三据全部可复核。
- 施工命令可照判性：五条 git mv verbatim 已在一次性 worktree 内**照抄实跑**＝MV_OK，git diff --cached --name-status -M 出 **R100 恰五行**（逐枚 rename 百分百·零改字）。命令零歧义。

### 绿-3 · 豁免论证可推翻性＝经实测未推翻（链条闭环复现）

本席不采信票面 grep 读数，自行三向取证＋一次实弹复现：

1. 扫描域定义现读：check-pointers.py DEFAULT_SCOPE ＝ 三分类目录（agent-experts／agent-skills／softwares），仓根 ．collab／ 按裁-23 拍板 2 排除。票称「缺省扫描域＝三分类目录」**属实**。
2. 命中面自扫：五枚旧路径 token 与纯基名 token 各向 grep 三分类目录全域＝**仅一枚命中**＝agent-experts／baigong-software-team／．collab／qa／2026-11-10-SWB-SCRATCHG-产品席窄复核-v1.md 行 5 反引号包径引枚 1 旧路径（含 ．collab／ 前缀形态）。其余四枚旧 token 扫描域**零命中**＝票面「仅枚 1」读数**成立**。
3. 该引用件在盘态：git ls-files 实证 tracked、check-ignore 实证 NOT_IGNORED＝确在缺省扫描域内可被扫到。
4. 实弹复现（隔离 worktree·链上版 b2bceb8 起点·零触主仓）四态差量：
   - 基线（仅 checkout 零改动）：BLOCK 3830／WATCH 1655／历史豁免 6
   - 仅 S1 五 mv 不加豁免：BLOCK **3831**（**恰 +1 BLOCK**）／WATCH 1655／枚 1 token 出「BLOCK OA-D6 指针悬空」行 → 票面「git mv 后旧路径消失、后缀归位层对非 ．scratch 索引命中 0＝新增恰一枚 BLOCK」**复现成立**（后缀索引写死排除仓根 ．scratch 族，取证件不计入多义化，与脚本注释口径一致）
   - 五 mv ＋ 豁免条目一枚：BLOCK **3830**（**回基线·零增**）／WATCH **1656**（**恰 +1**）／历史豁免 **7**（**恰 +1**）／枚 1 出行案＝「WATCH OA-D6 历史指针豁免 …｜历史豁免（token＋文件集合）」
   - 豁免行文案实测**零 BLOCK 字样**＝V3 grep -c BLOCK 不被污染（脚本 R6 写死文案·实测印证）
   - 链条结论：「豁免后 BLOCK 零增／WATCH 恰 +1／历史豁免恰 +1／run-gates 发现总数基线 +1」**全部成立**，未推翻。
5. 豁免条目格式对拍：现读 share／baseline-pointer-exempt.json items 共九枚，枚 6／7 先例（token＝．collab／2026-11-03-SWB-B3-收口登记-v1.md 与 ．collab／2026-11-04-SWB-B4-收口登记-v1.md，files＝单元素列表）与票 S2 拟追加条目（token＝枚 1 旧路径文本，files＝恰窄复核件仓根相对路径一枚）**同型**；键制＝token 文本＋命中文件集合（非纯 token 键），与脚本 load_exempt 消费路径一致。追加位置＝items 尾部一条目＝既有条目零改可行。
6. 快照件消费面：grep baseline-pointer-exempt 全仓＝仅 check-pointers.py 一处消费（＋pyc 缓存）＝票面「仅一闸消费·其余闸零扰」**属实**。
7. 先例机制链上锚：ca33b5f 在册（豁免清单入机检配置所立裁定线），A14 五笔链 fb76547→c79dde9→9ebc94f→883aa68→111b67a 八锚全在位。

### 绿-4 · V 系可机械判定＝逐条可跑可判

- V1：git ls-files ．collab／ 总数现跑 **222**（→217 目标可达）；一级过滤现跑六枚（→仅 README 一枚）＝判据命令＋钉值双双可机械执行。
- V2：桶闸现跑 exit 0·一级目录判 14 枚｜违例 0｜名录对拍 一致＝与 V2 钉值全等；脚本注释写死「一级文件不判」＝untracked 平放件不触此闸，V1「口径使然非违例」与 V2 自洽。
- V3：三钉值现跑全部对拍全等（BLOCK 22810／WATCH 4581／GATE 发现 151502）；基线真身落票 §七且与 §〇 零摆动（票 §七 读数＝本席实测值）。
- V4：R100 口径经实弹复现可行（sim 出恰五行 R100）；M 恰一行＝豁免件（本席以同一编辑式实测可出单件 M＋diff 仅 items 追加一条目）；git diff --cached --name-only 恰六路径在复现中读数为「五枚新名＋豁免件」＝恰六可判。
- V5／V6：禁动面 pathspec 域零命中判据可跑；V6 自靶本席已复证票面 --target exit 0（回执靶检属第 4 步产出，快审阶段判其判据可行）。
- 附面零扰实测：check-pointer-closure 与 check-collab-lint 缺省扫描面均**不含仓根 ．collab／**（前者 DEFAULT_PKG_FACES＝两包面＋扫描面收窄写明 ．collab／** 不进；后者按票 §七 分账），五枚件移动不触两闸＝票 §七「EAC-L2 零起波」结论面成立。

### 绿-5 · 禁动面与体例＝在册齐备

- 在册禁动面：untracked 散件全集（§二之三 逐枚列名）、ledger M 态、FUXI 面（agent-skills／fuxi-skill／ 全域＋仓根 ．scratch／ FX 族）、链上史件内容（含被引窄复核件一字不改）、门禁面除 S2 一条目外零触、账本零手写、桶目录既有 216 枚零移动——面闭集可 pathspec 机械核。
- 票面防自咬体例：正文路径裸文＋全角斜杠叙述、施工命令块双引号包径不含反引号 token、引文 ⟦⟧；票面自靶 exit 0 本席独立复跑成立。
- 落链纪律段：单件 pathspec＋add 紧邻 commit＋FX_COMMIT_DECLARE 挂 commit 侧＋尾标闭集（本票笔 -TICKET／QA 快审 -QA-REV／产品 -PM-REV／放行 -PM-RELEASE／施工 -BUILD／回执 -RECEIPT／验收 -QAV／收口 -GCLOSE）齐备。

### 绿-6 · 对抗臂（三发·零命中未推翻票面）

- 对抗一发（派工指定）：五枚旧路径是否被包内（agent-skills／agent-experts）文件以反引号引用而票面漏列＝grep 三分类目录全域（含软基名形态）实证**仅一枚命中且票面已列**（窄复核件行 5）。**漏列零**。
- 对抗二发：五枚件**自身**内含反引号包径 token（枚 1／2／3／4／5 各含数枚，如枚 5 引 ．collab／decisions／ 与 ．collab／receipts／** 等）。移动后是否起波＝件从仓根 ．collab／ 移入 ．collab／decisions／，**两态均在非缺省扫描域**＝零起波；V3 钉值不受影响。**未推翻**。
- 对抗三发：豁免条目先追加而五枚未 mv（乱序态）＝该 token 当前经仓根候选解析存活→不产发现→追加无害、不新增行。**未推翻**。
- 对抗四发（钉值稳定性）：见黄-3——非票面缺陷，属验收轮环境条件。

### 黄-1 · 枚 3 旧路径在仓根 ．collab／ 史件内有一枚反引号引用·本票零处置（不拦·建议登观察账）

- 实测：git grep b2bceb8 命中 ．collab／audits／2026-11-10-裁权新规程两件会签-QA席附议判词-v1.md 行 7 以反引号包径引枚 3 旧路径（．collab／2026-11-10-挂账清点-呈拍简报-v1.md）。同族另有 ．collab／decisions／ 两件以反斜杠绝对盘径形态引枚 3／枚 4（非可解析 token 形态）。
- 票面口径**如实**：§二之二 明写「命中面全在仓根 ．collab／ 与仓根 ．scratch／＝非缺省扫描域」，故 V3 钉值零摆动成立、本票不因此欠豁免。
- 黄之理由：五枚 mv 后该枚仓根史件内旧路径将成为**已存在但未入任何豁免面的悬空 token**，一旦后续票以 --scope ．collab 扩面或该面入扫描域即暴露。属既有噪声非新增债，但清债批次应知会承接。
- 可机械处置口径（非拦项）：验收轮在回执或收口登记 observation 段登一则「枚 3 旧路径仓根 audits 面一枚反引号引用·零扫描域效力·待扩面票承接」。

### 黄-2 · 仓根 ．collab／ 一级平放违例面本票仅清 tracked 口径（不拦·口径已写死）

- 票 §一／§二之三 写死「只迁 tracked 件·一切 untracked 未入库散件不入声明闭集」＝口径清晰、不违例（桶闸一级文件不判）。
- 黄之理由：V1 判据用「tracked 口径」字样自限，故「仓根散件迁册」完工后**在盘面上仓根 ．collab／ 一级仍平放十二枚 md**。若清债批次以「仓根平放清零」为批次终点，须另票承接十二枚归属（决策者裁或后续票定），本票不承接＝验收轮勿把 V1 读成盘面清零。
- 可机械口径：验收判词结论行宜限定「tracked 平放清零达成·untracked 平放面按票面口径未处置」。

### 黄-3 · V3 钉值对拍须以「扫描面无临时 worktree／junction 残留」为前提（不拦·验收轮操作条件）

- 实测证据：本席建隔离 worktree（落仓根 ．scratch／QA-DEBT1REV／ 族）期间跑 run-gates → 发现 **151561**（＝基线 +59）；git worktree remove 拆除后复跑 → **151502** 归位。仓根 ．scratch／ 内既有 junction（指向两外仓）亦属同类污染源（脚本后缀索引虽排除 ．scratch 族，run-gates 汇总发现面口径不同）。
- 票面未写此前提。若不写，施工／验收轮任何取证用临时 worktree 残留都会造成**钉值对拍假红**。
- 可机械处置口径（非拦项）：V3 复测前必跑 `git worktree list` 与基线 GATE 读数确认（151502），任何临时 worktree 用毕即 `git worktree remove` 再读钉值；本席此次已实践同一手法可作先例。

---

## 总裁决

- 红：**0** 枚
- 黄：**3** 枚（黄-1 悬空 token 观察账承接／黄-2 tracked 口径限定结论行／黄-3 钉值对拍前置环境条件）——三项均**不拦**，属放行口径附加陈述与验收轮操作条件，不改票面本体。
- 绿：**6** 枚（开工读数对拍／声明闭集完备性／豁免论证实弹复现未推翻／V 系可机械判定／禁动面与体例／对抗臂三发零命中）
- 关键实弹结论：S1 五 mv 命令可照抄（R100 恰五行复现）；S2 豁免条目同型先例成立且使 BLOCK 回基线零增、WATCH 恰 +1、历史豁免恰 +1——票面核心论证经独立复现**未被推翻**。

**结论行：可放行。**（放行口径含黄三条：结论面须限定 tracked 口径、验收轮 V3 复测须先清临时 worktree、枚 3 仓根 audits 面悬空 token 登观察账承接。）

## 效力与席位声明

- 本件＝票级快审判词·落 ．collab／audits／ 带链；判词效力限于「可施工性／判据可机械性」面，终态验收判词属第 5 步 QA 独立验收轮，放行登记属主理人签字席（本席不自写自判·不自放行）。
- 全程只审本票一张：零施工、零改票面（append-only）、他案脏面（ledger M）零带入、票面引文全部取自链上版 git show b2bceb8。
- 模拟取证件居仓根 ．scratch／QA-DEBT1REV／ 族·已拆除零残留。

---

## 修正笔 rev1（本席自纠·append 段·对拍产品席并发判词 4cfeb31 后补跑实证）

本席判词落链（b5564a1）后，产品席并发快审判词（链笔 4cfeb31）出红-1＝V1 总数钉值 222→217 系减五误算。本席以独立 worktree（链上版 b2bceb8 起点·五枚 git mv 命令 verbatim 照抄实跑）复跑确认**采纳**，并自纠正文绿-4 中 V1 子目（正文原句「→217 目标可达」为误判·追认不覆写正文）。

### 红-1 · 票 §三 V1 总数子目钉值机械不自洽（假红死结·拦放行）

- 实测读数：git ls-files ．collab／ 总数 **pre 222 → 五 mv 照抄后 post 222 不变**；一级过滤 post＝仅 README.md 一枚（此子目成立）。
- 机械机理：git mv＝树内搬家（rename 非 delete）·tracked 总数必然不变；要总数达 217 须五枚脱 track＝与同票 V4「R100 纯移动恰五行」自相矛盾。工程师正确照 S1 施工后实测必为 222，V1 照文必判红＝**验收假红死结**（正确施工必过不了判据）。
- 票内自洽性定位：§〇「一级五枚＋README＋桶内 216＝222」加总成立；§三 V1「222→217」＝起草席把「一级清零」误算成「总数减五」，仅此一处误，同句一级过滤子目与 V2／V3／V4／V5／V6 均不受累。
- 可机械修正指令（一处窄修·两式任取）：① §三 V1 「git ls-files ．collab／ 总数 **222→217**」改「总数 **222→222 不变**（git mv 树内搬家·总数不变·清零面以一级过滤子目为准）」；② 或径删该总数子目、保留「一级过滤＝仅 README.md 一枚」子目。修正笔后 V 系其余判据零随动（桶闸 exit 0 读数不依赖总数子目）。

### 修订后汇总（取代上方总裁决段·正文原段留痕不覆写）

- 红：**1** 枚（红-1＝V1 总数子目伪钉值·与产品席 4cfeb31 红-1 同源同判·双席独立同靶）
- 黄：**3** 枚（黄-1／黄-2／黄-3 不变）
- 绿：**5** 枚（绿-1／绿-2／绿-3／绿-5／绿-6 不变；绿-4 之 V1 子目降红，其余 V 子目维持可机械判定）
- **修订后结论行：不可放行现面；V1 总数子目一处窄修后即可放行（豁免论证复现、R100 口径、三钉值、桶闸、对抗臂结论全部不受累）。** 销账归主理人裁程与窄复核轮。
