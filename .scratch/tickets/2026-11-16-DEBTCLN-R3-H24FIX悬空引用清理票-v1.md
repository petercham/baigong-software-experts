# DEBTCLN-R3 · H24FIX 悬空引用清理票（v1·规格票·起草笔零施工）

- 票号：**DEBTCLN-R3**（清债批次第三票·族名锁定，勿改）
- 票名：**H24FIX 悬空引用清理票**（20-handoff 规范文件行 24 悬空引用清理）
- 票型：清债·指针纠偏单行票（规范件一行内路径 token 改指现役落点·其余行 byte 零扰动）
- 起草席：架构席 arch-debt3（fresh 实例·主理人派工）
- 票面落点：.scratch／tickets／2026-11-16-DEBTCLN-R3-H24FIX悬空引用清理票-v1.md
- 来源与裁定依据：CPPOOL 批次收口（收口笔 1527653）候补池新行登记＝「20-handoff 行 24 B2 搬家史遗留悬空另案候排」；决策者已裁起票（时候已到类＝坐实缺陷＋修法现成）。
- 候裁点：**0 枚**（见 §六；两项口径自决并附论证，先例在册）。

> **票面自注（防自咬体例）**：本票正文对一切路径仅叙述性提及＝裸文写＋全角斜杠（／U+FF0F），不落反引号路径指针；引用既有原文以 ⟦⟧ 标记（⟦⟧ 内 ASCII 路径经联测 probeE 坐实不入指针机检射程）。§二 展示块内＝现文与清理后文逐字对照，**行内反引号在展示面剥除**（反引号包裹的悬空旧径会自咬，联测 probeA 坐实；剥除后裸文形态经联测 probeD 坐实安全），施工命令为准绳（程序化替换自动保留原文反引号面）。本票面成文后自靶 python share/check-pointers.py --root . --target 本票面实路径 须 exit 0（读数见 §七）。

---

## 〇、开工读数（起草轮现跑·禁抄旧数）

| 项 | 命令 | 实测读数 |
|---|---|---|
| 时点 | date '+%F %T %z' | 2026-11-17 01:40:56 +0800（收尾复跑见 §七） |
| HEAD | git rev-parse --short HEAD | **88c2b80**（＝DEBTCLN-R2 收口登记笔·链顶·与派工预期链态相符） |
| tracked 脏面 | git status --porcelain | 恰一枚 M＝agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl（他案脏面·禁碰禁入票） |
| untracked 全集 | 同上 | ?? 二十四行（仓根 .collab／ 平放 2026-11-12 系列 md 十二枚＋.collab／research／ md 六枚＋仓根杂散五枚＋本批次新增面）——全部他案/知会面，不入声明闭集，计数照登当轮值（活体群随外案漂移·禁钉死） |
| 靶件定位 | Glob 全仓 name=\*20-handoff\* | 仓内规范真源＝**恰一枚**＝agent-skills／multi-collab／references／20-handoff.md＝本票靶件。另见两类同名件非射程：①邻仓证据备份面＝agent-experts／baigong-software-team／.collab／evidence／publish／backup-20261023-＊／multi-collab／references／20-handoff.md 两枚（tracked 证据备份·历史快照零触）；②fuxi 包 .scratch／ 树内 worktree 副本多枚（agent-skills／fuxi-skill／.scratch／FX-U14／FX-U15 族）——其行 24 同含旧径 token 且居缺省扫描面（agent-skills 在 DEFAULT_SCOPE 内）贡献 BLOCK 数枚＝FUXI 零碰零处置归因照登。**结论＝本仓规范面单点债，开票。** |
| 包内部署面分列 | find agent-experts／ 全域 name=\*20-handoff\* | 仓内规范面与包内备份面皆含旧径 token（备份面＝evidence／publish／backup-20261023-130728 一枚现文在册），债登记所指＝仓内规范真源；备份面属证据快照族零触，如实分列如上 |
| 靶件基线哈希 | sha256sum＋git hash-object | sha256＝72b7b2842c2859b346bce5ee5ce91b2e80ead7ac575ee501a558a7f551460a7e；blob＝**d408872c24be709e4ac24b8761ecea9372d391b9**（盘＝链＝工作区净态，git status 对该文件零命中） |
| 靶件行数 | wc -l | 66 行（与 RCTPATH-R2 回执「基线 58→66」在册态相符） |
| 行号复验 | sed -n 24p | 行 24 现文＝含旧径 token 的「决策/设计类交接件附加判据」段＝与债登记行号**全等零漂移**（RCTPATH-R3 改动面＝行 28 节题，未推进行 24；该微票单行替换不增删行） |
| 悬空坐实①链面 | git log --oneline -1 -- 旧径 | 旧径末笔＝**91eb86f**（SWB-B2-A1 交付面主体搬家批＝git mv 迁出笔·此后该路径链上绝迹） |
| 悬空坐实②盘面 | ls deliverables | **No such file or directory**（exit 2）；git ls-files deliverables＝空（tracked 零件）＝盘链两面零命中坐实 |
| 悬空坐实③机检 | python share/check-pointers.py --root . --target agent-skills／multi-collab／references／20-handoff.md | **exit 1·恰一条**＝该文件行 24 BLOCK OA-D6 指针悬空（旧径 token→目标不存在）；行 24 其余指针（本包 90-changelog 相对径）解析正常 |
| 搬家落点实证 | Glob＋Read 目标文件 | 旧径内容现居＝agent-experts／baigong-software-team／skills／software-orchestration／references／handoff-discipline.md（B2 搬家 git mv 保 rename 历史·91eb86f 迁入）；该件在册且**§三 行 20 现题＝「三 三正面判据（决策/设计类交接件）」**＝与行 24 引用语义（三正面判据全文真源）逐字对榫 |
| 缺省指针钉值 | python share/check-pointers.py 缺省扫描 grep -c BLOCK／grep -c WATCH | **BLOCK 22810／WATCH 4582**（与派工预期仓级缺省面全等） |
| 旧径 token 活体面分布 | git grep 旧径 token（tracked 全域） | 命中五件分账＝①本靶件行 24（唯一入机检 BLOCK 的规范面命中）；②agent-skills／multi-collab／references／60-gates.md 行 110（同 token 另一活体悬空＝该文件自身行 110 表格列·缺省扫描在册 BLOCK·**非本债射程**→§四 观察行候另案）；③④⑤既往审计/回执三件（.collab／audits／RCTPATH-R2 两快审＋.collab／receipts／RCTPATH-R3 回执·均 ⟦⟧/叙述形态引用取证读数＝不入 BLOCK 零触） |
| 消费面核查 | grep share／全部闸脚本＋check-collab-lint＋check-source-of-truth | 无脚本消费 20-handoff 行 24 内容本身：check-collab-lint 仅注释行指 §二 三正面判据条款真源（条款正文面零动）；check-source-of-truth 的 spec_file 锚＝handoff-discipline 本件现役径（在册正确态）；票模板/门禁配置零指该段。→ 行 24 指针纠偏＝对全部消费脚本零输入面变化（V3 论证根基） |
| 全仓门禁基线 | bash share／run-gates.sh | **GATE PASS exit 0·发现 151503**（与开工预期基线全等·活体面随外案摆动禁钉死） |
| 消费脚本改前基线 | check-collab-lint／check-source-of-truth 现跑 | 均 **exit 0**；check-source-of-truth 读数＝模式 dual｜文件 129｜BLOCK 0（新命中 0）｜基线豁免 54（WATCH）｜指针 WATCH 413（改前值在册·改后对拍见 V3） |
| 版本账现态 | grep version agent-skills／multi-collab／SKILL.md | version 4.11（＝90-changelog v4.11 末行同源）；RCTPATH-R3 先例读数在册＝该微票施工笔 80e8612 单件 touch·施工前后 SKILL version 均 4.11 未 bump·changelog 无对应条目（git show 坐实） |

## 一、案件本体与悬空坐实

靶件行 24 现文 verbatim（全角冒号段为叙述帽；块内展示面剥反引号，口径见票面自注）：

```text
**决策/设计类交接件的附加判据（三正面判据·可判）**：本节原载三正面判据全文与保护句，现已删除——全文真源＝devkits 仓软件团内部卷 deliverables/experts/baigong-software-team/skills/software-orchestration/references/handoff-discipline.md §三；原三条与保护句的快照及迁移沿革见本包 references/90-changelog.md v4.6／v4.8 行，以真源为准。
```

悬空成因链（链上在册）：v4.8 行立该指针句时旧径有效→DIRRELOC-C1 迁 workbuddy／→deliverables／experts／→SWB-B2-A1（91eb86f）整体搬家入壳 agent-experts／baigong-software-team／；RCTPATH-R2 甲案条款插入与 R3 节题去编号两微票均对该行 24 悬空「零处置差量零新增」（回执在册），挂 CPPOOL 候补池至本票清偿。债＝坐实；修法＝改指现役落点（§二 口径论证）。

## 二、声明闭集（＝恰一枚施工面·一行内单 token 替换·禁酌情）

**S1 · 靶件行 24 单 token 替换**。旧径 token（B2 搬家史悬空径）→ 现役径 token（Glob＋行 20 内容实证）：

```text
旧：deliverables/experts/baigong-software-team/skills/software-orchestration/references/handoff-discipline.md
新：agent-experts/baigong-software-team/skills/software-orchestration/references/handoff-discipline.md
```

替换后行 24 全文 verbatim（同样剥反引号展示·施工命令自动保留原文两处反引号包裹）：

```text
**决策/设计类交接件的附加判据（三正面判据·可判）**：本节原载三正面判据全文与保护句，现已删除——全文真源＝devkits 仓软件团内部卷 agent-experts/baigong-software-team/skills/software-orchestration/references/handoff-discipline.md §三；原三条与保护句的快照及迁移沿革见本包 references/90-changelog.md v4.6／v4.8 行，以真源为准。
```

**清理口径＝改指现役路径**（vs 删引用 vs 改叙述语·自决理由见 §六 自决①）。行内其余成分（含本包 90-changelog 相对径指针）逐字零动；其余 65 行 byte 零扰动。

**施工手段规格（唯一准绳·程序化单 token 替换防手误）**：

```bash
python -c "p='agent-skills/multi-collab/references/20-handoff.md';s=open(p,encoding='utf-8').read();old='deliverables/experts/baigong-software-team/skills/software-orchestration/references/handoff-discipline.md';new='agent-experts/baigong-software-team/skills/software-orchestration/references/handoff-discipline.md';assert s.count(old)==1, 'OLD-TOKEN-NOT-1';open(p,'w',encoding='utf-8').write(s.replace(old,new));print('REPLACED-1')"
```

（断言前置＝旧 token 现文恰一枚否则拒改；产物＝同文件同编码同行数 66；工程师用其它手段须同等过 V1／V2。）

### 禁动面（写死）

- 靶件其余 65 行全部 byte 级零扰动（含行 22 干净指令类判据段／行 28 节题（RCTPATH-R3 现役态）／§二 两域两制全节／§三至§五全部）。
- 版本账零动：agent-skills／multi-collab／SKILL.md frontmatter version 4.11 不 bump；90-changelog 零新增条目（口径自决②·先例在册·见 §六）。
- 60-gates.md 行 110 同 token 另一活体悬空零触（非本债登记射程→观察行候另案候补池，§四）。
- fuxi 包 .scratch／ 树内全部 20-handoff 副本零触（FUXI 零碰）；邻仓证据备份面 evidence／publish／backup-20261023-＊ 两枚零触。
- 他案脏面零带入：ledger.jsonl 之 M 态＋?? 当轮全集＝禁碰禁入库。
- 链上史件零回改；账本面零手写。

## 三、验收判据（全机械·命令＋钉值·禁凭记忆填值）

- **V0 开工读数**：施工轮现跑 HEAD＝88c2b80 链上本票落链后最新值如实照登；git status 他案脏面形态与 §〇 一致（ledger 一枚 M＋?? 当轮值照登——**他案归因禁扩集**（R1-GCLOSE／R2 先例口径），本票落链后本票面转 tracked，?? 不含本票）。
- **V1 悬空清零（靶件面）**：
  1. grep -c 旧径 token 于靶件 ＝ **0**；grep -c 现役径 token 于靶件 ＝ **1**（旧行 24 现含新 token 命中）。
  2. python share/check-pointers.py --root . --target agent-skills／multi-collab／references／20-handoff.md → **exit 0**（改前基线＝exit 1 恰一条在册 §〇；改后零发现＝该文件全部指针可解析，起草轮仿真联测旁证＝现役 token 无 BLOCK 命中，唯 .scratch 放置面包相对径 90-changelog 不可解析系仿真放置伪影，落位真文件该相对径解析正常＝改前机检恰一条不含它，坐实）。
- **V2 byte 级零扰动（REST-EQUAL 式）**：git diff --numstat 于靶件＝**1／1 恰一行**（行 24 位置段）；逐行对拍改行集＝**{24}**：

```bash
python -c "import subprocess;b=open('agent-skills/multi-collab/references/20-handoff.md',encoding='utf-8').read().splitlines();a=subprocess.run(['git','show','HEAD:agent-skills/multi-collab/references/20-handoff.md'],capture_output=True).stdout.decode('utf-8').splitlines();d=[i+1 for i,(x,y) in enumerate(zip(a,b)) if x!=y];print('CHANGED',d,'LEN',len(a),len(b));raise SystemExit(0 if d==[24] and len(a)==len(b)==66 else 1)"
```

→ **exit 0** 且打印 CHANGED [24] LEN 66 66（HEAD 基线以本票落链后链上笔为准；行数 66→66 零增删）。
- **V3 消费面零变化**：check-collab-lint 与 check-source-of-truth 现跑均 **exit 0**（与 §〇 改前基线 exit 码全等）；check-source-of-truth 计数照登对拍（改前＝BLOCK 0／豁免 54／指针 WATCH 413）——若指针 WATCH 计数因本行 token 换径有差＝如实照登＋归因＝指针落点纠偏的面径变化（该脚本消费池含 skills 面），禁遮掩禁扩集；票模板／门禁配置消费面零指该段（§〇 坐实）＝零变化先验。
- **V4 缺省扫描钉值**：python share/check-pointers.py 缺省扫描 grep -c BLOCK／grep -c WATCH → 预期 **BLOCK 22809（−1＝靶件行 24 悬空清偿归因本笔）**／**WATCH 4582（零变化）**；fuxi 树副本行 24 同 token 在册 BLOCK 零变化（零触归因）；60-gates 行 110 BLOCK 零变化（零触归因）。bash share／run-gates.sh → GATE PASS exit 0，发现数照登（基线 151503·活体面随外案摆动禁钉死·变化归因照登）。
- **V5 自靶**：python share/check-pointers.py --root . --target 施工后回执实路径 → exit 0；本票面（链上现文）同式 exit 0 复证。
- **V6 笔面单恰靶件**：口径照 R2 收口登记 §四 终版＝**核验时点 git diff --cached --name-only 实测 staged 恰靶件一枚（或本笔面单件）＋钩子 STAGED-DECL 互证为准**；commit 树面并发窗裹入他案＝归因在册不构成施工违例（迁册类先例在册）；**禁写总数增减类伪钉值**。

## 四、观察行（随登·不立项不候裁）

- 60-gates.md 行 110 同 token 活体悬空一枚＝同族债第二例，修法同款（改指现役径·该处语义＝MC-SEAT-DECL 条款级依据指 §十，现役件在册含 §十）；射程外零动，候补池候另案候排。
- fuxi 树 .scratch／ 副本族对该 token 的缺省扫描 BLOCK 贡献＝取证面非真源面（D-94 口径），FUXI 零碰。
- 邻仓证据备份面两枚含旧径现文＝publish 历史快照族，派生证据非真源，零触。

## 五、排程（串行两笔施工段）

链第 1 步＝本票起草笔（架构席·本笔）。第 2 步＝双席快审（产品席＋QA 席 fresh eyes：审 S1 替换可照抄性·V 系完备性·口径自决两项取舍）。第 3 步＝放行登记（主理人）。第 4 步＝工程师施工一笔（靶件一枚·§二 命令）＋**回执一笔**（落 .collab／receipts／ 桶·R1 勘正口径）。第 5 步＝fresh QA 按 §三 V 系独立验收判词。第 6 步＝收口登记（主理人）。

## 六、候裁面（必有节·**候裁 0 枚**）

- **自决① · 清理口径＝改指现役路径**：行 24 语义＝「全文真源＝…§三…以真源为准」＝可达性是该句的效力本体。三选比较＝删引用：真源句悬空改悬空语义为断链，「以真源为准」失锚，弃；改叙述语（裸文＋全角斜杠去反引号）：逃离机检射程，与靶件自家 §二 两域两制第 4 条自立口径（反引号包裹指针「天然入既有指针机检可解析面＝悬空即报」）相悖，且该文件即规范真源更应示范在检形态，弃；改指现役路径：语义零变化·真源句恢复可达·机检转绿，取。指向件禁臆造＝落点经 Glob＋行 20 节题逐字对榫实证（§〇 在册）。批次编排类不上楼＝不自列候裁。
- **自决② · 版本账零动**：本笔＝路径 token 纠偏＝条款语义零变化（三正面判据正文/保护句/沿革句零动）。先例实物在册＝同文件同族面修先例 RCTPATH-R3（节题去编号微票）施工笔 80e8612 单件 touch·SKILL version 前后均 4.11 未 bump·changelog 零条目，经双席快审＋QA＋收口放行成链。同案同判。若双席快审或主理人认须 bump 4.11→4.12＋changelog 补行＝随其裁落，不预判。

## 七、起草笔自证（落笔后、commit 前实跑）

- 开工读数＝§〇 全表（当轮现跑·HEAD 88c2b80）。
- 本票面自靶＝python share/check-pointers.py --root . --target .scratch／tickets／2026-11-16-DEBTCLN-R3-H24FIX悬空引用清理票-v1.md → **exit 0**（实跑坐实·读数见完工回报）。
- 防自咬体例联测在册（.scratch／debt3／ 取证族·用毕即拆口径见回报）：probeA 反引号旧径入围栏＝BLOCK 命中（自咬坐实）；probeB 同现文裸行入正文＝BLOCK；probeC 全角斜杠 ⟦⟧＝exit 0；probeD 围栏内引号串＝exit 0；probeE ASCII ⟦⟧＝exit 0；probeF ⟧⟦ 拆段引文＝exit 0；probeG/probeH 现役径行入围栏＝唯一命中＝包相对径伪影（放置面所致）；sim2 全文件仿真替换＝行 24 旧 BLOCK 消失坐实。
- 靶件基线双哈希＝§〇 在册（sha256 72b7b284…／blob d408872c…）；V2 的 git show HEAD 基线以本票落链后链上态为准（本票笔不触靶件，HEAD 态靶件哈希不变）。
- 本笔面＝恰票面一件；其余全程零触碰；他案脏面零带入。

## 八、链衔接纪律段（各笔共守·写死）

- 单件／本笔面 pathspec 两端齐带（add 与 commit 各带本笔面路径）；add 紧邻 commit 零窗口；commit 前 git diff --cached --name-only 坐实仅自笔面。
- FX_COMMIT_DECLARE＝仓根相对纯路径清单（逗号或换行分隔）**挂 commit 命令侧**（挂 add 侧会被 STAGED-DECL-BLOCK 拦）。
- 禁 add -A／禁 amend／禁 --no-verify；message 以 collab: 起头·零 at 符号·零反引号；尾标置 message 最末位。**本票各笔尾标闭集**：本票笔 -TICKET／QA 快审笔 -QA-REV／产品快审笔 -PM-REV／放行登记笔 -PM-RELEASE／工程师施工笔 -BUILD／工程师回执笔 -RECEIPT／QA 验收笔 -QAV／收口登记笔 -GCLOSE（族名 DEBTCLN-R3 随尾标内嵌）。
- 一票一 commit 增量落盘；commit 类命令 timeout 600000ms；撞 index.lock 有界等待零删锁。
- 防自咬体例＝票面／回执正文路径裸文＋全角斜杠叙述形态；引文 ⟦⟧；票面与回执自身须过 check-pointers --target exit 0 后才可落链。
- 临时工作物只落仓根 .scratch／debt3／ 族；本席起草笔只写票面这一件。

---

（票尾·append-only：后续修订以 rev 段位在此处续笔，正文原段零改写）
