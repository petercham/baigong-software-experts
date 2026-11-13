# SWB-A14QAEXEMPT · 施工批回执 v1（工程师席 eng-a14c1·2026-11-13）

- 票面：`.scratch/tickets/2026-11-10-SWB-A14QAEXEMPT-a14-exempt-config-and-qa-exempt-ticket-v1.md`（v1＋修订笔 R1-R7·效力＝修订段优先）
- 放行登记：`dd10e9c`（候①采甲转 WATCH 带历史豁免标记·候②采甲仅成文）
- 两笔封顶：施工笔＝`3715cb7`（S1＋S2 同笔一次收敛）＋回执笔＝本笔。零 amend。
- 开工/收笔 HEAD：开工窗（11-12 首轮）＝`dd10e9c`；中断后续建窗开工＝`73179da`（11-13 18:32 现跑）；本回执笔后 HEAD 见 git log。

## 〇、中断事件照登（诚实申报）

11-12 施工轮落笔窗（add 后 commit 输出重定向件 build-commit.txt 在册＝STAGED-DECL 放行＋门禁链全跑）中断，链上无 BUILD 笔；两件半成品滞留工作区（`share/check-pointers.py` M＋`share/baseline-pointer-exempt.json` ??）。11-13 恢复轮现跑对拍＝半成品与票面 §4.1/§4.2＋R2/R6/R7 规格逐项合拍（json import／load_exempt 缺失无豁免＋损坏 SystemExit(4)／豁免层插入位 FX-U28 归位层之后含斜杠 BLOCK append 之前／WATCH 行不含 BLOCK 字样／items 9 条＋bucket 2 行），全部判据在 73179da 链位重新现跑后落笔。index.lock 撞锁：11-12 有界等待至释零删锁（他案 git 进程正当持锁照登）；11-13 开工窗锁 free。

## 一、文件清单回执（声明闭集三件封顶）

1. 新建 `share/baseline-pointer-exempt.json`——骨架照 §4.1 逐字；items 9 条＝drill 1 条（token 连接值＋五文件集合）＋README 8 条（R7 扩面·八异 token 各 {README.md}）；**token 与 files 值零手抄**＝从缺省扫描实跑输出（V0-default-scan.txt／V0-readme-target.txt）程序化摘取（摘取器＝.scratch 件 extract_exempt.py），命中文件集合与 §2.1 五文件全等闸＋行号人读核对闸（drill 30/23/66/174/194/200·README 23/25/72/84×2/88×2/92）实跑通过方可落；第二段 collab_bucket_exempt 两行照 §4.3 逐字（零迁移·consumption 留待桶名闭集机检挂面＝候②采甲）。
2. 改 `share/check-pointers.py`——仅 §4.2 一处（＋57 行零删）：import json＋EXEMPT_SNAPSHOT 同目录 HERE 式＋load_exempt（缺失＝{} 无豁免更严不更松；损坏/形态不符＝raise SystemExit(4)＝R2 勘正·只取 SOT 先例结构不取抛出语句）＋check_dangling 内 exempt 单次读取＋豁免层插入位＝FX-U28 后缀唯一归位层之后、含斜杠悬空 BLOCK append 之前；豁免命中＝不计 BLOCK、出 WATCH 行带「｜历史豁免（token＋文件集合）」标记（R6：行内不含 BLOCK 字样）；裸基名 WATCH 层不接豁免；三入口（缺省/--scope/--target）同口径（消费点居 check_dangling 内）；七候选层／后缀归位层／孤儿对账／退出码闭集／路由零动。
3. 本回执件（`.collab/receipts/` 票名族前缀命名）。

## 二、V0-V7 实跑读数（全部现跑·SEV 字段式口径＝R6）

### V0 开工复点（R1 双栏口径）

- 续建窗开工读数：`date`＝Fri Nov 13 18:32:31 2026；`git rev-parse --short HEAD`＝`73179da`；tracked 脏面＝百工包 ledger 一枚（他案在飞照登零碰）＋本租约两件半成品（见〇节）。
- 前像臂（改前口径＝HEAD 版脚本 `git show 73179da:` 落 .scratch 同目录跑·无豁免配置）：缺省扫描 SEV-BLOCK **18253**／WATCH **4581**／NOTE-FXU28 **2002**；旧字样 BLOCK 恰 **6** 枚（行号 30/23/66/174/194/200 逐枚全等＝§2.1 集）；README `--target` 前像 BLOCK **8** 枚。
- 双栏归因（对票 §一 起草窗参照值 22831 anywhere／18253 SEV／1988／GATE 150151）：链笔栏＝`dd10e9c..73179da` 共 **73 笔／67 件／22 枚 md**（FUXI 链笔群＋SCRATCHCFG 线＋FX-U49 收口等，全部他案笔逐笔照登）；盘态栏＝未跟踪快照副本族增减（NOTE 1990→2002＝+12 归链笔栏新落件＋盘态副本；GATE 昨窗 151285→今窗 151339＝+54 全落 check-collab-lint 5876→5930 栏＝链笔栏新落件所致）。两栏均可归因＝「不归因即停」未触发。
- 归档对拍臂（R1 新增·备查）：前像臂＝链面脚本口径同盘跑；drill 6 枚两态全等在册。

### V1 配置生效（R7 两式分列）

- **V1-a 缺省面**：SEV-BLOCK 前像 18253 → 改后 **18247**（恰 −6）；含旧字样 BLOCK 行计数 `grep -F '2026-11-08-drill' | grep -c ' BLOCK '` → **0**。
- **V1-b README target 面**：前 8 → 后 **0**。

### V2 转 WATCH 留痕（候①采甲）

- 缺省面 `grep -c '历史豁免'` → **6**；WATCH 计数 4581 → **4587**（＝+6）；README target 面「历史豁免」→ **8**。

### V3 fail-closed 双臂

- 探针臂：drill token 程序化复用（从配置件读取拼接，禁手抄）落集合外文件（.scratch 探针件），`--target` 显式入口 → **exit 1** 照拦 BLOCK（BLOCK 行在册）。
- 损坏臂：按 R6 升格条款**未动真配置**——scratch 副本承载（脚本副本＋同目录同名截断 JSON＝半文件）跑 → **exit 4**（infra error 文案在册）；share 真件完好复点 items 9 条 OK（原「后复原」步骤已删＝R6）。

### V4 史笔零改字

- 施工链（base=73179da）`git diff --name-status`＝**A share/baseline-pointer-exempt.json ＋ M share/check-pointers.py**（回执笔后恰三件）；**零 R 行**（零迁移实证）。
- §2.1 五文件 blob 复点：`git ls-tree 73179da` 与 `git ls-tree 3715cb7` 两态五枚 sha 全等（22eee49/42df8e3/3d9d04e/58b52f0/10b39d1 前缀）＋对开工窗 dd10e9c 值亦全等。
- 两包 qa tracked＝**60/2**（off＋NUL 双式）：fuxi 桶 59→60 差值归因＝第 60 枚落链笔 `b564922`（FX-U40 QA 判词·11-11 16:04·系放行登记 dd10e9c 之祖先＝放行窗内已 60，票钉 59 系起草窗 7900b07 参照值）；EAC 桶 2 全等；`git diff 3715cb7^..HEAD` 两桶 diff 空集＝整桶未碰。
- 禁动面 diff 空集核验：`.gitignore`／`share/run-gates.sh`／`60-gates.md`／`share/baseline-sot-dup.json`／`agent-skills/object-audit/tests`／`README.md`／`agent-experts/**`／`ticket-template.md`／`docs/` → `git diff --name-only` 全空。

### V5 门禁全链

- `bash share/run-gates.sh --no-write` → **GATE PASS exit 0**，发现 **151339** 条；check-pointers 子输出改前后行量 **24836/24836 全等**（BLOCK−6 转 WATCH＋6 总量不变）；check-ticket-reconcile 184（全 WATCH）零变化；各检查器行数对昨窗唯一增量落 collab-lint 栏（链笔栏归因见 V0）。

### V6 守件零回归

- `python -m py_compile share/check-pointers.py` 绿；`python share/check-pointer-closure.py --selftest` → PASS exit 0（OA-D6-3＝4/OA-D6-4＝1/EXEMPT＝2/SUBSTR＝4/VIOLATION＝4 全 MATCH·前后全等＝O-3 夹具面零翻面）。

### V7 票面靶检

- `--target` 票面 → **exit 0**（落笔前现跑）。

## 三、靶检口径随登（施工两件自身）

`--target share/check-pointers.py` 两枚 BLOCK（悬空目标串一＝references/20-handoff.md 字样·二＝docs/INDEX.md 字样·拆写不入反引号防自咬）＝**HEAD 既存存量**：前像件（`git show HEAD:` 落 scratch）同臂同跑逐 token 全等、仅行号随新增行偏移（230/262→272/304）＝非本笔新增行引入；该件不在缺省扫描域（DEFAULT_SCOPE＝三分类目录）故从未入 GATE 基线。不为其改既存注释行（§4.2「除此一处零改」硬线）、不扩 items（票面 items 闭集写死）。JSON 件 `--target` exit 0。

## 四、纪律自证

- 两笔各自：FX_COMMIT_DECLARE＝纯路径清单（笔一 2 件／笔二本件）；pathspec add/commit 两端齐带、紧邻无窗口；禁 add -A／amend／no-verify 未碰；message 零 at 符号字符用字样；`collab:` 前缀＋[SWB-A14QAEXEMPT-BUILD]/[SWB-A14QAEXEMPT-RECEIPT] 尾标；commit 输出重定向落 `.scratch/SWB-A14QAEXEMPT/` 落盘（STAGED-DECL staged 2｜声明 2｜超额 0 在册）。
- 笔落笔前靶检：票面 exit 0 在册（三节＝自身两件既存存量归因口径随登）。
- 临时工作物＝`.scratch/SWB-A14QAEXEMPT/` 票号族目录（扫描输出／探针件／前像臂／摘取器／commit 日志），完工后随工作面处置。
- 他案面照登零带入：ledger 脏面一枚、仓根 untracked 散件族、链上 FUXI/SCRATCHCFG/FX-U49 笔群——diff 零涉。
- 防自咬：本回执旧字样 token／桶名串全部入围栏块外纯文本拆写或不入反引号；引用件全部既有盘上件。
