# SWB-RET · 施工票：票面退役批（B 批＋ESC1＋CD1＋ES2 票面族退役手续 ＋ .scratch/cd1 临时面清灭 ＋ refs 快照 docs/adr 残留处置）（施工票·L2·架构席起草·审计对齐类）

- 起草实测 HEAD＝`7a9b4d3`（ES2 收口登记笔）；开工 ANCHOR＝开工实测 HEAD ≥ `7a9b4d3`（其后含裁定登记笔），读数附回执开端。
- 裁定真源＝`.collab/decisions/2026-11-04-皮总裁定-审计对齐类免拍板放行.md`（已直读）：免拍板放行类＝审计/记录/过程域对齐；**覆盖 B 批总收口登记 §六「票面保留不 retire 候业务终验」候闸口径**（原登记行史笔不回改·后生效覆盖先前）；程序链不变＝出票→双席审票→工程师施工→QA→收口。
- 退役体例真源＝ES 案 T-B/T-C（`agent-experts/baigong-software-team/.collab/design/2026-11-03-devkits-engstd-adr-archive-retirement-v2.md` 〔v3 §效力链注：T-B/T-C 未被覆盖照常有效·指针只指不搬〕）：
  - T-B＝**不建归档面**（`_archive/` 类落位否案）——票面移除程序不变三要素＝票首 `已结案` 标记→单独 commit `retire:` 前缀＋消息含 `RETIRE <票ID>`→批尾 tag `archive-<YYYYMMDD>`；寻回行写票目录 README：`git log --diff-filter=D --grep "RETIRE <票ID>"` → `git show <笔>^:<旧路径>`；
  - E-ARC-1′ 换锚先行硬线＝移除前活引用清零（本批实测见下）；裸票 ID 基名族零改＝非路径语义豁免口径沿用。
- 开工附注三项：①誊写禁令 `f5a0d96`（本票＝搬家/移除类：git rm 史实入 git 历史＋tag 承载，无誊写目；票面本体＝创作类辖域外自察）；②票面落位 `.scratch/tickets`；③era（不在本票）。
- 计数口径＝occurrence；判据自带落盘重定向；负例 exit≠0。

## 现盘落位实测（起草取证·回执附开工复测）

1. **退役对象 13 支**（仓根 `.scratch/tickets/` tracked·实测枚举全列）：
```
.scratch/tickets/2026-11-03-SWB-B1-restructure-skeleton-ticket.md
.scratch/tickets/2026-11-03-SWB-B1-restructure-skeleton-ticket-rev2.md
.scratch/tickets/2026-11-03-SWB-B2-delivery-tree-migration-ticket.md
.scratch/tickets/2026-11-03-SWB-B2-delivery-tree-migration-ticket-rev2.md
.scratch/tickets/2026-11-03-SWB-B3-process-domain-migration-ticket.md
.scratch/tickets/2026-11-03-SWB-B3-process-domain-migration-ticket-rev2.md
.scratch/tickets/2026-11-03-SWB-B4-gate-ticket-anchor-sync-ticket.md
.scratch/tickets/2026-11-03-SWB-B4-gate-ticket-anchor-sync-ticket-rev2.md
.scratch/tickets/2026-11-03-SWB-B5-closure-gitignore-readme-ticket.md
.scratch/tickets/2026-11-03-SWB-B5-closure-gitignore-readme-ticket-rev2.md
.scratch/tickets/2026-11-03-SWB-ESC1-era-cross-repo-handover-micro-ticket.md
.scratch/tickets/2026-11-04-SWB-CD1-concurrency-discipline-ticket.md
.scratch/tickets/2026-11-04-SWB-ES2-seatcard-gate-routing-ticket.md
```
（README.md 不退役＝现役索引面随动改写；`agent-*/…/.scratch/tickets/` 项目级 85 支历史票**不在本批射程**——已收口旧票退役随后续批次，本票对象＝B 批后置队列裁定点名 13 支。）
2. **reconcile 机理与基线**（现码直读 `check-ticket-reconcile.py`）：缺省票目录枚举＝仓根 `.scratch/tickets/` ＋三分类项目级候选（`ticket_dirs` 存在才入列）；`os.listdir` 单层不递归；`CLOSED_RE=已结案`（正文前 400 字符命中）→ **跳过枚举不入对账**；枚举空→`SystemExit(4)` 防假绿。现盘基线读数＝`票 98（对账 34／SKIP 缺声明 64）｜发现 146（全 WATCH）｜exit 1`。13 支现无「已结案」字面＝在 98 计数内。
3. **扫描面冲突核验（E-ARC-1′ 换锚先行）**：交付面（agent-experts/agent-skills/softwares 非过程域）对 13 支全路径引用＝**0 命中**（实测）＝活引用已净，移除硬线绿；过程域（.collab 桶）对 13 支票名引用＝861 文件级命中（史述账·.collab 在 check-pointers 缺省扫描排除域＝不判悬空·不改不吞）。check-pointers `iter_markdown` 缺省三分类 scope：仓根 `.scratch/` 不在扫描域（os.walk 不触）＝退役票面自身旧路径引用不产悬空（机理注记入回执）。
4. **`.scratch/cd1/` 临时面**：untracked（tracked＝0）·顶层条目 **20**／find 文件数 **66**（CD1 验证轮 Temp 工件·两口径并报——清灭闸计数口径见候裁①）。
5. **refs 快照 docs/adr 残留**：QA-ES2V L93 定位实测命中＝`agent-skills/external-advisor-collab/.collab/refs/skills-research-2026-10-28/AGI-Super-Team/docs/adr`＝9 文件物理在盘·该快照树 tracked＝**0**·`git check-ignore` 该面 exit **0**（已 ignore 态）；版本面断言基线＝`git ls-tree -r HEAD | grep "docs/adr/"`＝**0**。

## 声明闭集（14 件·本批唯一可写 git 面）
- 声明闭集：
- .scratch/tickets/2026-11-03-SWB-B1-restructure-skeleton-ticket.md
- .scratch/tickets/2026-11-03-SWB-B1-restructure-skeleton-ticket-rev2.md
- .scratch/tickets/2026-11-03-SWB-B2-delivery-tree-migration-ticket.md
- .scratch/tickets/2026-11-03-SWB-B2-delivery-tree-migration-ticket-rev2.md
- .scratch/tickets/2026-11-03-SWB-B3-process-domain-migration-ticket.md
- .scratch/tickets/2026-11-03-SWB-B3-process-domain-migration-ticket-rev2.md
- .scratch/tickets/2026-11-03-SWB-B4-gate-ticket-anchor-sync-ticket.md
- .scratch/tickets/2026-11-03-SWB-B4-gate-ticket-anchor-sync-ticket-rev2.md
- .scratch/tickets/2026-11-03-SWB-B5-closure-gitignore-readme-ticket.md
- .scratch/tickets/2026-11-03-SWB-B5-closure-gitignore-readme-ticket-rev2.md
- .scratch/tickets/2026-11-03-SWB-ESC1-era-cross-repo-handover-micro-ticket.md
- .scratch/tickets/2026-11-04-SWB-CD1-concurrency-discipline-ticket.md
- .scratch/tickets/2026-11-04-SWB-ES2-seatcard-gate-routing-ticket.md
- .scratch/tickets/README.md

（`.scratch/cd1/` 清灭＝untracked 文件系统面不入 git 闭集（目二单独判据）；refs 快照面零动作（目三判定在册）。）

## 逐条施工规格

### RET-A 退役宣告先行（单独 commit·append 标记行·不移除）

对 13 支票面各在**首行（标题行）之后插入一行**退役宣告（逐字统一）：

```
Status: 已结案（retire 宣告 2026-11-04·依 2026-11-04 审计对齐类免拍板放行裁定·票面退役批 SWB-RET）
```

- 体例依据＝ES 票面移除程序「票首行 `已结案` 标记」前置项＋E-ARC-1′ 裸票 ID 基名零改（宣告行不含票 ID 路径语义）；
- 该行落位＝正文前 400 字符内＝`CLOSED_RE` 命中面＝**本笔起 reconcile 即跳过 13 支**（对账目过渡显性化，见判据 2）；
- commit 前缀 `collab:`（宣告笔非移除笔，E-ARC-2 三要素挂 RET-B 笔）。

### RET-B 票面移除（单独 commit·E-ARC-2 三要素）

1. `git rm` 13 支逐名（物理移除＝史实由 git 历史承载＝ES T-B「不建归档面」定案口径；**不建任何 retired/ 子目录**＝归档面否案沿用）。
2. commit message：前缀 `retire:` ＋消息体逐票含 `RETIRE <票ID>` ×13（票 ID＝文件名基名·`git show --name-only` 13 行 D 态）。
3. `.scratch/tickets/README.md` 重写随动（同笔内）：现状行改＝「本目录现役票＝无（B 批后置队列 13 支已于本笔退役）」＋**退役名录 13 行**（基名＋收口登记 commit 指针）＋**寻回行**：`git log --diff-filter=D --grep "RETIRE <票ID>"` → `git show <笔>^:<旧路径>`（ES 体例逐字）。
4. **批尾 tag**：`archive-retirement-20261104`（`archive-*` 前缀闭集形态·判据在册）。
5. 硬线前置＝RET-A 跑绿（判据 2 宣告过渡读数）后 RET-B 方准开工（换锚先行同构时序）。

### RET-C `.scratch/cd1/` 临时面清灭（untracked 文件系统面·不入 commit）

1. 前置断言：`git ls-files .scratch/cd1/ | wc -l`＝0（零 git 面确认·有 tracked 即停手呈报）；
2. 清灭动作＝`rm -rf .scratch/cd1`（**批量确认闸口径**＝顶层条目 20 逐项对照清单确认后执行；若执行器按 find 文件数 66 计触阈值闸拒＝**停本项候裁**（禁硬闯款），候裁①在册）；
3. 后置断言：`find .scratch/cd1 -type f 2>/dev/null | wc -l`＝0；`git status --porcelain` 对 `cd1` 行＝0。

### RET-D refs 快照 docs/adr 残留处置＝判定零动作·留盘（定标在册）

1. **定标＝留盘不清除**：该面＝外部调研快照（refs 桶＝gitignore 两制排除面·check-ignore exit 0 实证在 ignore 态）——清除无版本面收益（本就不 tracked）且毁外部参照素材；「外部参照件不入我仓版本库」既有裁决由 ignore 态已满足；
2. **N-2 不染色断言**（判据 5）：版本面 `git ls-tree -r HEAD | grep -c "docs/adr/"`＝**0** 前后全等；该快照树 `git ls-files | wc -l`＝0；
3. 处置定性入回执一行（QA-ES2V 黄-2 候补池项自此核销）。

## 验收判据（全部机械可判·自带落盘·负例 exit≠0）

1. **闭集全等**：RET-A 笔 `git show --name-only`＝13 件；RET-B 笔＝14 件（13 D＋README M）；`git show -M --name-status` RET-B＝D 行 13／M 行 1（无 A 行＝无归档面新建断言）。
2. **reconcile 三时点对拍**（开工基线→RET-A 后→RET-B 后·各落盘）：`python agent-skills/object-audit/scripts/check-ticket-reconcile.py --root .`——开工读数复现现盘（票 98 系）→ **RET-A 后＝98−13＝85**（13 支转 CLOSED 跳过·exit 码与 WATCH 账随 13 支退出对账面的变化逐笔入回执）→ **RET-B 后＝仍 85**（枚举零漂移＝已宣告即已跳过·移除不二次扰动）；三时点均 **exit≠4**（票目录非空恒成立＝仓根目录在位＋项目级 85 支在架＝防假绿断言）。
3. **移除三要素断言**：RET-B commit message `grep -c "RETIRE"` ≥13 且前缀 `retire:`；`git tag -l "archive-*" | grep -c retirement` ＝1；README 寻回行 `grep -c "diff-filter=D"`＝1。
4. **寻回可行实证**（退役≠删除史实判据）：抽 3 支（B1 原票/CD1/ES2）跑 `git show <RET-B笔>^:.scratch/tickets/<基名>` → `wc -l` >0 且首 400 字符含 Status 宣告行（＝史实链完整）。
5. **docs/adr 版本面零染色**：判据 RET-D 前后两跑全等＝0；`git check-ignore` 快照路径 exit 0 在位。
6. **cd1 清灭断言**：RET-C 前置/后置三读数（0/0/0）。
7. **门禁零回归**：run-gates GATE PASS exit 0 对开工基线零新增族（13 票面退出 OA-D6-5 对账族＝该族 WATCH 读数减项归因入回执＝预期减非新增）；六演练 `SIX_DRILLS_GREEN`＝1（盘符口径）。
8. **负例**：Temp 构造仅含空 `.scratch/tickets`（无 .md）仓骨架 → reconcile exit **4**（防假绿机理不随退役失效断言）。

## 禁动面

- 交付面全域（agent-experts/agent-skills/softwares 内容面）＝本批 git 闭集全在仓根 `.scratch/tickets/`＝交付面交集空；bundle 三同源＋bundle README（非涉不动＝本批零交付面变更零 bump 自声明，随收口登记追认格）；
- seat-permissions 两 config／全部 scripts（reconcile/check-pointers 机理零触碰＝扫描面随动由 CLOSED_RE 既有语义承载，不改码）；
- `.collab/` 全域（decisions 桶裁定件＝真源只读引用；861 处过程域史述引用零改）；
- 项目级 `.scratch/tickets/` 85 支历史票（退役批次分离·候后续裁定）；`tools/`、`.gitignore`、仓根 README；`.scratch/cd1/` 之外的 `.scratch/` 面。

## 候裁点

1. **cd1 清灭闸计数口径**：顶层条目 20 vs find 文件 66——若确认闸按文件数计且拒＝停该项候主理人裁（禁硬闯）；按顶层条目计＝本票口径直接执行。
2. （呈备）refs 快照留盘定标如主理人欲清除，收口前点名即可（RET-D 反转为单文件系统 rm 目·判据 5 不变）。

## 票间关系

前置＝ES2 收口（`7a9b4d3`）＋免拍板裁定登记笔。后置＝本票收口登记（主理人）＋项目级 85 支历史票退役是否另批＝收口呈裁一行（本票不吞并）。双席审票＝**串行派发**（`12a3c4a` §2 款沿用）。

## 回执

落 `agent-experts/baigong-software-team/.collab/receipts/2026-11-04-SWB-RET-receipt.md`：开端 HEAD＋两笔 name-only/name-status＋reconcile 三时点对拍表（含 13 支 WATCH 减项归因）＋三要素读数＋寻回实证 3 支读数＋cd1 三读数（或停闸呈报）＋RET-D 定标行＋门禁对拍读数。RET-A/RET-B 各单独 commit（`collab:`／`retire:`）＋批尾 tag；禁 `--no-verify`、禁 amend；门禁真拦如实报告不绕闸。

——arch-swbreloc 起草（新建创作类·誊写禁令辖域外自察；本票止于终态设计，严禁起草笔落改）。

---

## 修订笔（append-only·2026-11-04·A 席审票 `650874c` 修单·主理人裁采甲案·作者席自笔）

本节覆盖原票以下段落读数/条款（其余条款照旧）：§实测 3「861 文件级／史述账零改」半段（R-1）、§实测 2 基线「票 98」与判据 2「98→85→85」（Y-1）、§禁动面「.collab 全域…史述引用零改」条款（R-1 随动）、声明闭集（扩 RET-A0 面）。

### R-1 修订（采甲案·新增 RET-A0 换锚目）

**机理更正（认错账）**：原票「.collab 在 check-pointers 缺省扫描排除域」断言不实——`check-pointers.py` L75 `DEFAULT_SCOPE=(agent-experts, agent-skills, softwares)`，`iter_markdown` 不排除三分类目录下 `.collab` 子桶＝**项目桶在扫描域内**；仓根 `.collab`/仓根 README 才在域外。原「交付面 0 命中＝活引用已净」口径系扫描域误设。

**22 行活引用清单（作者席复核实测·与 A 席读数对账）**：`git grep -n -F -f <13全路径清单> -- agent-experts/ agent-skills/ softwares/` 复跑＝**22 行／23 occurrence／20 文件**（双命中行＝`receipts/2026-11-03-SWB-B1-receipt.md` L3＋L39、`receipts/2026-11-04-SWB-B5-receipt.md` L3＋L83）——**与 A 席 22/23/20 全等** ✓。逐处 file:line 全表（22 行·百工项目桶）：
```
qa/2026-11-03-PM-SWBRELOC-B1B5-审票-v1.md:9
qa/2026-11-03-QA-B1-独立验证-v1.md:36（check-ignore 示例命令史述行）
qa/2026-11-04-SWB-B5-QA-v1.md:6／CD1-QA-v1.md:3／CD1-PM审票-v1.md:4／CD1-QA复审-v1.md:4
qa/2026-11-04-SWB-ES2-PM审票-v1.md:3／ES2-QA-v1.md:3／ES2-QA复审-v1.md:3／ESC1-QA-v1.md:6
receipts/2026-11-03-SWB-B1-receipt.md:3,39／B2-receipt.md:3／B3-receipt.md:3／B4-receipt.md:3
receipts/2026-11-04-SWB-B5-receipt.md:3,83／CD1-receipt.md:3／ES2-receipt.md:3／ESC1-receipt.md:3
receipts/2026-11-03-SWB-B1-收口登记-v1.md:4／B2-收口登记-v1.md:4
```
（以上均系 `agent-experts/baigong-software-team/.collab/` 前缀下件。）

**RET-A0 施工规格（置于 RET-A 之前·单独 commit `collab:`）**：对上述 20 文件 22 行逐处换锚，两式按行性质：
- **式①（语义引用行：回执 L3 票面真源族／收口登记被收口票行／qa 头部被核物行＝18 行）**：反引号全路径 → 改指该票**收口登记件路径＋票面 commit 指针**（形如 `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-SWB-B1-收口登记-v1.md`（票面 `b5fd2b4`·已退役·寻回见该件名录）——目标在位＝resolve 命中不悬空）；
- **式②（命令/示例史述行：qa-B1 L36、B1-receipt L39、B5-receipt L83＝3 行）**：全路径串断链化＝反引号内改**裸基名**（提及嫌疑级 WATCH 容许）＋句尾「（票面已退役·SWB-RET）」注记——命令史迹语义保留，(a) 全路径机械零达成。

**闭集扩（声明闭集 14 件 → 34 件）**：追加 RET-A0 二十文件（上表 20 文件全路径行，锚行 `- 声明闭集：` 下条目）；禁动面「.collab 全域」条款随动加豁免行：「**例外＝RET-A0 二十文件 22 行换锚面**（真源 v2 L101–106 换锚程序覆盖 receipts/qa 族＝有授权改锚；除此 22 行外 .collab 桶零触碰）」。

**判据增（新判据 9·RET-B 启动硬线）**：RET-A0 收笔后 `python agent-skills/object-audit/scripts/check-pointers.py --root . > $RET_TMP/c9.out 2>&1` → 对 13 支全路径串 `grep -c "BLOCK OA-D6"` 涉票行＝**0**＋`git grep -o -F -f <13清单> -- agent-experts/ agent-skills/ softwares/ | wc -l`＝**0**（E-ARC-1′ (a) 机械零·真源 L113–121「修好跑绿前票面族移除禁启动」硬线＝置于 RET-B 前置断言）；(b) 裸基名族残留逐处分账写入 **RET-B commit 消息体**（乙案 (b) 款形态·机械侧仍 0）。

**时序换代**：RET-A0（换锚）→ 判据 9 跑绿 → RET-A（宣告）→ RET-B（移除）→ RET-C/RET-D。

### Y-1 修订（判据 2 基线行换代）

判据 2 三时点换代＝「**开工实测 N → N−13 → N−13**」：开工首步 reconcile 落盘定 N（作者席起草复测＝**票 99（对账 35／SKIP 缺声明 64）｜发现 147｜exit 1**——本 RET 票自身入枚举；原票 98 系＝本票落盘前时点读数，作废）；原「98→85→85」字样由本节覆盖。其余机理（CLOSED_RE 跳过／exit≠4 防假绿）不变。

### Y-2 修订（体量数换代·可复现口径）

原「861 文件级命中」作废，换代为三笔可复现读数（作者席复跑·occurrence 口径·`git -c core.quotepath=off`）：①三分类扫描域内 13 支**全路径 occ＝23**（22 行/20 文件＝RET-A0 射程）；②仓根面（README＋仓根 .collab·缺省域外）全路径 occ＝**7**（不受 OA-D6 扫·不入 RET-A0·史述在册）；③tracked **裸基名 occ（排 `.scratch/` 自引）＝31**（A 席读数 30·差一未对账＝如实登记，回执以开工复跑为准）。原票 §实测 3/§禁动面「861」字样由本节覆盖。

### 修订笔自查（判据扰动确认）

判据 1 闭集全等数随扩（14→34·两笔读数分列：RET-A0 笔＝20 件／RET-A 笔 13 件／RET-B 笔 14 件）；判据 2 基线行换代（Y-1）；判据 3/4/5/6/7/8 **零扰动**（新增判据 9 独立条款）；三时点语义/tag/寻回链/RET-C/RET-D 条款零触碰。

——arch-swbreloc 修订笔（A 席 R-1/Y-1/Y-2 销账·甲案落地·append-only）。

### 修订笔之二（B 席复审两黄销账＋观察①②一行级处置）

开工基线＝HEAD 实测 `2d6fd55`＝B 席复审笔 ✓。本节 append-only：修订笔（之一）各段原文不动，以下覆盖句为准。

**黄-1 覆盖（式①行数 18→19）**：原「式①（语义引用行：…＝18 行）」覆盖＝**式①＝19 行**。差一补点名＝`qa/2026-11-03-PM-SWBRELOC-B1B5-审票-v1.md:9`（审票表格「被核票面」列表行＝语义引用行·按式①处置·B 席预演实证按式①处置该行后涉票 BLOCK 0）。归类复核＝式① 19 行＋式② 3 行＝22 行/23 occ 不变 ✓。

**黄-2 覆盖（判据 9(b) 括注写明三分句）**：原括注「（乙案 (b) 款形态·机械侧仍 0）」覆盖＝「**（乙案 (b) 款形态：①活引用面全路径族 occ＝0＝判据 9(a) 主句之 0；②式②设计保留之裸基名 token＝3 处（qa-B1-独立验证 L36、B1-receipt L39、B5-receipt L83）逐处分账写入 RET-B commit 消息体；③施工后裸基名残留读数 3 记入 RET 批回执）**」。判据 9(a) 主句与「修好跑绿前票面族移除禁启动」硬线语义不变。

**观察①采（ESC1 行换锚目标一行级定标）**：式① 中 `receipts/2026-11-04-SWB-ESC1-receipt.md:3` 行换锚目标定＝仓根面 `.collab/2026-11-04-SWB-B批总收口登记-v1.md`（commit `3b03738`）＋注记「（ESC1 票面已退役·收口见该件 ESC1 段）」；实证依据＝该目标在仓根面＝check-pointers 缺省扫描域外（DEFAULT_SCOPE 仅三分类·L75）＝目标安全，ESC1 收口账即在 B 批总收口登记（其 commit 消息点名「ESC1收口销账」）。其余式①行缺省式（各自收口登记件）不变。

**观察②采（B1/B2 收口登记 L4 自指行＝补注分支）**：`receipts/2026-11-03-SWB-B1-收口登记-v1.md:4`／`...-SWB-B2-收口登记-v1.md:4` 两行仍按式①计（19 行内含）但加覆盖句＝**该两行换锚文字不构成任何路径引用**（式①缺省式将使换锚目标＝件自身＝自指荒谬成立）；执行形态＝原反引号全路径删除，替换为纯文字指涉「（票面已退役·收口即本件·寻回见本节寻回行）」；该两行不留裸基名＝黄-2 之②③「3 处/读数 3」数额闭合。

**修订笔之二自查**：22 行/23 occ/20 文件清单与闭集 34 件均不变（黄-1 仅补式①括号点名·观察①仅定标换锚目标均不增换锚面）；判据 1–8、9(a)、时序换代、RET-A/B/C/D 各条款零扰动；本票面在仓根 `.scratch/tickets/`＝check-pointers 缺省扫描域外，本笔对门禁零影响；无 HOLD/已结案字样新增（reconcile 枚举不受扰）。

——arch-swbreloc 修订笔之二（B 席复审黄-1/黄-2 销账＋观察①②落地·append-only）。
