# STRUCT-FIX 全批 QA 独立验证 v1（qa-structv·fresh eyes·证伪导向·八面亲跑）

- 开工 HEAD 实测＝`e2660ea`（≥派工钉 `e2660ea` 满足）；开工 `git status --porcelain` 残项＝`.collab/ledger/`、`.scratch/structfix/`（他席在途·本席零触碰如实登记）
- 被验批次：交付笔 `093cabb`（feat:·闭集 11 件）＋回执笔 `e2660ea`；票面＝`.scratch/tickets/2026-11-05-STRUCT-FIX-structure-declaration-alignment-ticket.md`（起笔 `4a28614`→修订笔覆盖段 `c0434fe`＝唯一施工依据→作者自纠 `3c6a16c`，三笔链 `git log --follow` 实测在位）
- 链序核验：`093cabb` parent＝`73f77c6`（ADR-L0 收口）；`--is-ancestor` 三跑＝`73f77c6`/`c7d4be1`/`3c6a16c` 全为 `093cabb` 祖先＝HOLD（ADR-L0 批后交付）机械坐实
- 读数区＝`.scratch/qa-structv/`（gates-post-main／gates-baseline-main／闭集对账／S1 定稿抽取等），批毕即删，本件即读数留存载体（§八.2）

## 总判：IS_PASS（红 0／黄 1／绿 7）

## 逐项读数表

### 面1 闭集对账＝绿

- `git show --name-only 093cabb`＝11 件，与票面声明闭集 11 路径行 `diff` 全等（排序后零差异）；与回执 ㊻③ 清单 11 条全等；票面声明闭集全命中零缺件。
- 回执笔 `e2660ea` name-only＝回执单件（落点＝票面指定 `.collab/receipts/` 路径名逐字吻合）。

### 面2 A1 fuxi 重写＝绿

- 后态条目计数式 `'^- [`]'`＝7、yaml `'^  - '`＝7（R-1 覆盖段换代式）；前态 `4a28614^` 态复跑＝3/3 命中票面前态钉值。
- S1 定稿逐字对读（diff 实装）：票面外栏 L41-68 内文＋R-4 增补句按「惯例句行之后同段无空行」并入后，与实文件 `agent-skills/fuxi-skill/docs/STRUCTURE.md` 逐字节 MATCH。
- 七条目 `test -e` 全真（README.md/adapters/contracts/gates/products/rejected/specs）；新文本 `SKILL.md`/`references/` 命中＝0/0 零虚宣残留；候裁 Q-1＝`ls agent-skills/fuxi-skill/SKILL.md` 不存在（未补建，合规）。
- 实态行 `git ls-files … | cut -d/ -f3 | sort -u | grep -v '^\.'`＝八行（README.md adapters contracts docs gates products rejected specs）＝七行全在声明＋剩 `docs`＝声明句既载排除项，双向咬合。

### 面3 A2 两补声明＝绿

- EAC：条目 3/yaml 3（前态 2/2 复现）；`sources/` 条目行、「交付面＝」句、yaml 行三处与票面 S2 去包裹内串逐字节对读全真；`test -d …/sources` 真。
- object-build：条目 3/yaml 3（前态 2/2 复现）；S3 三处逐字节对读全真；`test -d …/scripts` 真。

### 面4 A3/A4 惯例句＝绿

- `git grep -l "非枚举面" -- "*STRUCTURE.md"`＝7 文件（恰＝七份闭集 STRUCTURE）；`-c` 七行均＝1；前态 `4a28614^` 态复跑 exit 1 零命中（前态钉值复现）。
- A4 独立复算基准：§口径 1 去包裹内串＝228 字节·sha256 前 12＝`15b98b5a1653`（与票面 R-2 钉值全等；H6「228 vs 229」之争以实测 228 成立）。七份落位整行去首尾空白逐字节比对＝七份全 228 字节·sha12 全等。
- R-4 增补句（点号顶层面豁免第二句）七份逐字命中＝7/7，且落位＝惯例句行后同段无空行（fuxi 整件 diff 侧证）。

### 面5 A6 版本账＝绿

- 三同源后态＝`0.1.27`×3（plugin.json L3／.codebuddy-plugin/plugin.json L3／bundle.lock L5）；前态 `73f77c6` 态三值＝`0.1.26`×3（前后钉值全咬合）；三 JSON `json.load` 合法。
- README 版本账 v0.1.27 行＝1（L69）；链序＝v0.1.26 行 L68 先于 v0.1.27 行 L69；S5 行与票面去包裹态逐字节对读（唯一差＝票面行首尾反引号包裹，与 S2/S3 指示行同处理）；行内日期 `2026-11-05` 在全角括注内＝载体合规。

### 面6 A5/A8 对偶与样板＝绿

- 对偶不变式七份逐份（yaml delivery_paths 行⊆条目行集合，CRLF 容错复算）：fuxi 7↔7／EAC 3↔3／object-build 3↔3／multi-collab 2↔2／object-audit 4↔4／样板 2↔2／bundle 6⊆条目 7——七份全真；bundle `docs/adr/` 条目在位（L11 注「不属于交付路径」）不入 yaml＝既成例外实测成立。
- 样板份 `4a28614^→HEAD` diff＝纯 3 增 0 删（惯例句＋增补句＋空行），后态条目/yaml 仍 2/2＝零破坏。

### 面7 门禁＝黄（核心判据全真·两绝对读数不复现·根因＝环境在途件）

- 后态（HEAD 态盘）亲跑 `run-gates.sh`：`GATE PASS` exit 0·发现 9357；BLOCK 行 `grep -c BLOCK`＝5933（字面）·结构 BLOCK 4090／WATCH 5407。
- 基线（同主仓·11 件 `git checkout 73f77c6` 回退态复跑，跑毕即 `git checkout HEAD --` 还原核实）：`GATE PASS` exit 0·发现 9357·BLOCK 5933／结构 BLOCK 4090＝两态完全持平＝零新增 BLOCK 族。
- 两态发现行归一化 diff：后态侧净增仅 2 行汇总行；基线侧独有 29 行＝check-ticket-reconcile「未声明生成件」脏路径展开（恰为本批 11 件回退后成历史票未声明件＝本批改动正是该 WATCH 展开面的闭合方向）；SUBSTR 5799→5801（+2＝惯例句/增补句反引号段示例·判非违例类）、VIOLATION 1067 持平；check-adr 发现 0 exit 0；OA-T1 coverage 申报行两态各 1（既有形态）。
- **黄-1（H-QA-1）**：回执报「发现 9348／9348」与 reconcile「发现 177」按本席环境不复现（本席两态 9357／基线 reconcile 176→后态 149）。根因＝扫描面含开工时点 untracked 在途件（`.collab/ledger/`＋`.scratch/structfix/` 18 件）与工程师交付前环境不同；BLOCK 行 5933/5933 两席读数逐字吻合。判据面（GATE PASS·BLOCK 持平·新增面全 WATCH 族既有形态）两席全合＝不影响裁决。
- 探针教训登记：worktree 落 `.scratch/` 内跑基线＝扫描面翻倍＋跨仓相对路径断链（check-source-of-truth exit 2 假 BLOCK）；改仓外 worktree 与主仓回退两法，后者为有效基线。探针 worktree 已 `worktree remove`。

### 面8 ㊺㊻㊼红线＝绿

- 交付面零过程件指针：新落文本 `.collab/` 命中 7＝全为 R-4 增补句目录枚举示例（`` `.collab/` ``裸目录名），指向具体过程件形态 `grep '\.collab/[a-z]+/[^ ]+'` exit 1＝0。
- fuxi 实体目录零动：`093cabb` 对 fuxi 面 name-only 仅 `docs/STRUCTURE.md` 一件；实态八行前后同构。
- 六包 SKILL/changelog/代码域/softwares：`git diff --name-only 73f77c6 HEAD` 对 `SKILL.md|90-changelog|scripts/|\.py$|softwares` 全 exit 1 零命中；`docs/adr/` 本体零触碰（exit 1）；bundle STRUCTURE 内 `docs/adr/` 条目行零动（diff 增侧无该句）。
- `.collab/ledger/`、`.scratch/structfix/`：两笔 name-only 均无此路径＝零触碰（开工至完工 `git status` 残项恒等）。
- A7 OA-T1 独立口径量测（七份 STRUCTURE 全文＋README v0.1.27 行·去三载体后裸日期）＝八面全 0。

## 处置与登记

- 黄-1＝回执绝对读数与 QA 环境读数差（9 发现＋reconcile 行数差）：登记级·根因已锁（扫描环境在途件）·判据面两席全合·无需修票修件。
- 候裁 Q-1/Q-2/Q-3 本验证零触碰在位；观察面（清查报告观察 3）不入本票口径核实＝交付笔对 softwares/、仓根零命中。
- 本验证盘操作自证：11 件回退复跑基线后已 `checkout HEAD` 还原（`git status --short` 对该 11 件路径＝空）；`.scratch/qa-structv/` 批毕即删＋仓外 worktree `/tmp/wt-structv-baseline` 已移除。
