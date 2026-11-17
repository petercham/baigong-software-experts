# BAIGONG-DEP0131 · 装配与本地 WorkBuddy 四段转正票（v1·0.1.30→0.1.31 合并增量批）

- 票号：BAIGONG-DEP0131（族名锁定，勿改）
- 票型：独立部署票（deploy-gate 硬门 §二.1：部署闭集动作只立单独部署票，禁并入他票尾注条款）
- 起草席：架构席 arch-dep131（fresh 实例·主理人派工）
- 获批段界：到④转正止（§〇.1 登记＝用户同一指令明示授权载体成立·deploy-gate §四）
- 版本钉值：0.1.31（三同源 bump 触点在本票写集内＝§一 段⓪先行笔）
- 起草段产出＝仅本票面一件，单独 commit；起草席零执行任何部署动作、零碰装配面／市场源／缓存
- 纪律真源＝agent-experts/baigong-software-team/skills/software-orchestration/references/deploy-gate.md §二（独立票＋获批）、§四（用户同一指令明示含路径＝该次可直做）、§五（四段链①装配→②预览→③人类闸→④部署＋获批范围按段界定＋市场源备份一键回滚）
- 体例参照＝两枚先例票（.scratch/tickets/2026-11-06-GWP-DEPLOY-0.1.30-四段链部署票-v1.md／.scratch/tickets/2026-11-07-PROJINIT-DEPLOY-四段链部署票-v1.md），逐节参照；差异面（获批载体＝用户选段原文／bump 在本票内／四组件面装配含 devkit-tools 挂载／段界已明示）按本批实况改写
- 候裁点：3 枚（§七 J-1 装配 clean 闸与 ledger 他案脏面冲突取态／J-2 件数差集归因边界／J-3 docs 装配排除取态·rev1 增）——其余钉值全部本票钉死。rev2 随注：三枚已经主理人按「不上楼」过滤采纳归并（J-1 采 (b)／J-2 采归因口径照单／J-3 采甲案），落规格见 §十，票面对应停手候裁态由 §十 置换生效。
- **rev1 修订笔（2026-11-17·作者席 arch-dep131·append-only 增段·开工 HEAD 实测 6b57304＝v1 落链笔）**：主理人增补指令＝皮总指令性问题「docs 不参与执行，不应该进装配面，对吧？」入票。取证读数／谓词能力口径／规格取态全部落 §九（新增段）；候裁 J-3 增列 §七；写集与判据随动补项同见 §九。v1 既有正文零回改（J-1／J-2 框架、获批登记、四段结构、禁动面、回滚条款全部零动）。
- **rev2 修订笔（2026-11-17·作者席 arch-dep131·双席快审回流修票段·开工 HEAD 实测 0b54a44）**：红 1 黄 6 一次修完＋候裁三枚主理人采纳规格落 §十（K-1／K-2／K-3）。红-1＝段⓪ numstat 钉值算术错（原 3/3 与 rev1 4/3 均不实）→改逐文件钉＋夹具实测（git diff --no-index --numstat 现跑＝plugin.json 1/1＋.codebuddy-plugin/plugin.json 1/1＋bundle.lock 甲案 6/3＝合计 8/5；乙案形制 2/2 备查）；六黄落位＝W4／W6 宿主写面具名（§二 W 表）·段⓪时序钉死句（§一段⓪）·§六 与票头自注节号勘正（两处）·段①删装配面前置步入动作列（§一段①）·段②步 6 json 解析级对比口径（§二段②）·§〇.4 十六件改 13 件＋tests 三枚差集照登（§〇.4 锚定区间行）。修订形制＝实质条款原位置换（红项系数值勘正）＋§十 尾部增段；获批登记／四段结构／禁动面／回滚框架零动。

> 票面自注（防自咬体例）：本票正文对仓内文件引用一律仓根相对纯路径裸文（正斜杠）；叙述性提及与仓外绝对路径用全角斜杠（／U+FF0F）；全文零 at 符号、零反引号。§六 命令块内为可照跑实文本（仓根相对段为正斜杠纯路径；仓外面命令含 Windows 绝对路径＝执行段专用，段界由执行席按命令块照跑，叙述面不落反引号）。本票成文后自靶 python share/check-pointers.py --root . --target 本票面仓根相对路径 须 exit 0（读数见附节·rev2 勘正原误指 §五）。

## 〇、获批登记、开工前置与被部署内容

### 〇.1 获批登记（票面开端·各段执行前置）

- 用户（皮总）指令原话：「现在先装配并本地 WorkBuddy 部署（不是真的部署到市场）」。
- 主理人呈选段界，用户选定「批到④本地转正（推荐）」，选项描述原文＝「装配→本地市场源→直接转正进宿主缓存 0.1.31，您指令即人类闸当场过——新团队立即可用，改前后均留备份可一键回滚。远端市场零动作」。
- 获批路径清单（用户选项原文点名＋本票 §二 写集闭集对齐）：仓外装配面 D:／multi-agent-collab-devkits-build、本地市场源 C:／Users／peter／.workbuddy／plugins／marketplaces／my-experts、宿主缓存 C:／Users／peter／.workbuddy／plugins／cache／my-experts／baigong-software-team、备份目录 C:／Users／peter／.workbuddy／backup。
- 效力判定＝deploy-gate §四「用户在同一指令中已明示授权某次具体部署动作（含路径）」载体成立；③人类闸按选项语义＝用户指令本身当场过闸（不重跑，见 §四 段③）。
- 获批段界＝到④止（选项明示「批到④本地转正」）。④之后的远端市场／上架面零授权＝§六 禁动面第 1 条封死。
- 各段执行前核对批准在案（写死）：①②④每一段开工第一步＝在工作回执登记本 §〇.1 读数＋主理人转呈的派工读数；读数不含本段授权字样＝停手，回执登记「部署项缺批准」（deploy-gate §三执行席义务）。

### 〇.2 开工前置（起草轮现跑照登·执行段各段开工复跑）

| 项 | 命令 | 起草实测读数（2026-11-17） |
|---|---|---|
| HEAD | git log --oneline -1 | 332004f（＝DEBTCLN-R5 收口登记笔＝链顶·DEBTCLN 五票全清后首笔窗口） |
| tracked 脏面 | git status --porcelain -uno | 恰一枚 M＝agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl（他案脏面·照登零带入零清理·豁免注见 §七 J-1） |
| untracked | git status --porcelain 过滤 | 活体群（各席 scratch 族等）＝不进装配面（publish.py 纪律⑤信息行实证）·零带入 |
| check-pointers 缺省 | python share/check-pointers.py | exit 1·BLOCK 22809／WATCH 4582／NOTE 2039（全部他案存量面·禁钉死随轮照登） |
| lint | python share/check-collab-lint.py | exit 1·EAC-L1 2006／L2 4097／L3 0·VIOLATION 4097（他案存量） |
| csot | python share/check-source-of-truth.py | exit 0·BLOCK 0·基线豁免 54·指针 WATCH 413 |
| 全仓 GATE | bash share/run-gates.sh | GATE PASS exit 0·发现 151502 |
| skills 仓面 | cd ../multi-agent-collab-skills 后 git status --porcelain -uno | 空（跨仓组件源 clean） |

### 〇.3 被部署内容与三同源取证（只读取证在案）

- 被部署批＝自 0.1.30 转正（2026-11-06）以来的仓面增量合批＝PROJINIT 线、SEMGV 语义治理线、模板线、SCRATCHCFG、DEBTCLN 五票偿债批次等全部已收口增量（链上实绩＝e880edb（上次装配锚·见 〇.4）..332004f 区间）。
- 版本咬合裁定依据＝.collab/decisions/2026-11-07-皮总裁定-语义治理改造立项与合并批升号重新装配.md ③④＝合并批升号案 a＋升号后重新装配；该登记件 §三 明示升号 0.1.30→0.1.31、0.1.31 系 REMOTE-PUB 预留不钉号、占用不构成冲突。
- 三同源现值（起草实测·grep 行号在案）＝agent-experts/baigong-software-team/plugin.json 行 3＝0.1.30；agent-experts/baigong-software-team/bundle.lock 行 5＝0.1.30；agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json 行 3＝0.1.30。三枚恰三处（仓内其余 version 字样均属组件 SKILL.md frontmatter 等非 bundle 版本面，零碰）。
- bundle.lock 组件面现值四行（ref 钉值·tag 名拆写＝组件名与版本号分立，照跑命令时按 bundle.lock 行内字面连拼）＝external-advisor-collab tag v1.1.3／deep-research tag v1.0.2（跨仓·skills 仓）／claim-commitment-governance tag v1.2.0／devkit-tools tag v0.1.0（material＝share·target＝tools）。起草轮 tag sha 实跑：8418b3ac…／730962e1…（skills 仓）／56f63da1…／291ab447…。
- 宿主现态（起草实测）：市场源包目录 C:／Users／peter／.workbuddy／plugins／marketplaces／my-experts／plugins／baigong-software-team＝80 件、两 plugin.json 与 marketplace.json baigong 条目三读数均 0.1.30；宿主缓存 C:／Users／peter／.workbuddy／plugins／cache／my-experts／baigong-software-team＝列 0.1.1／0.1.22／0.1.24／0.1.27／0.1.29／0.1.30（0.1.30 带 .in_use 无 .orphaned_at，其余带 .orphaned_at）；installed_plugins.json 条目（my-experts 列下 baigong-software-team 键）＝installPath 指 0.1.30、version 0.1.30；0.1.31 未占号（市场源与缓存均无该目录）。
- register_expert.py 定位结果（起草全盘检索实证·非缺位）：市场源侧在位＝C:／Users／peter／.workbuddy／plugins／marketplaces／workbuddy-builtin／skills／expert-manager／scripts／register_expert.py；宿主缓存另两枚＝C:／Users／peter／.workbuddy／plugins／cache／workbuddy-builtin／skill-expert-manager／5.11.3-wb…／scripts／ 与 5.9.3-wb…／scripts／。参数形制以脚本 docstring 行 9 与 argparse 分支（行 210）实证＝register_expert.py <expert-dir> [--marketplace-dir <dir>] [--session-id <id>]。usage 面差沿用先例注记：脚本对 --help 不识别（把 --help 当目录参数报「expert directory does not exist」＝起草实跑在册），不得据此误判参数不存在。

### 〇.4 锚定区间与上次装配读数（停手判据基准）

- 上次装配实绩（装配面 ASSEMBLY.manifest.json 起草直读）＝assembled_at 2026-11-09T11:16:29、bundle_source_commit e880edb8…（短式 e880edb）、bundle_version 0.1.30、files 88、components 三枚（claim-commitment-governance tag v1.2.0 已含；devkit-tools 组件行后立）。装配面现盘 90 件（88＋ASSEMBLY.manifest.json＋COPY.state）＝既往遗留预览面，本票①段以重装配覆盖式重出（装配纪律：重装配＝删装配面重跑）。
- 锚定区间停手判据：开工时跑 git -c core.quotepath=off diff --name-only e880edb..<开工HEAD>，对 bundle 跟踪面（agent-experts/baigong-software-team/ 除 .collab/、.scratch/、tests/、README.md、docs/SWB-交接件）／本仓组件面（agent-skills/external-advisor-collab/、agent-skills/claim-commitment-governance/）／share 料源面 逐一列读数。本批＝增量批＝diff 非空属预期（rev2 复算勘正读数：bundle 面按本节排除口径＝13 件 M——原登 16 件系未排除 tests 段，差集恰 tests 三枚＝tests/acceptance/drills/drill-05-freeze-recover.sh／tests/acceptance/drills/drill-06-replay-reconcile.sh／tests/s2/test_lease_instantiation.py 逐枚在册；share 面多件 M、EAC／CCG 组件面空）——差集须逐行归因＝全部可归因至已收口批次（PROJINIT／SEMGV／模板线／SCRATCHCFG／DEBTCLN）＝绿；出现不可归因面（含 FUXI 线渗入 bundle 面）＝停手复核呈主理人。
- 组件面·skills 仓段：跨仓组件判据＝在 skills 仓跑 git rev-list -n1 后接 deep-research tag v1.0.2 的连拼 tag 名（照 bundle.lock 行 25 字面连拼）＝起草实测 730962e160bcf5b25f549c21f17c2c36848f4dfe，与 bundle.lock 行 25 ref 钉值一致性＋与前批回执登记读数比对；ref 未变＋tag sha 相等＝绿。
- devkit-tools 组件面：tag sha 起草实测 291ab447…（tag 建 2026-11-10＝晚于上次装配 e880edb）——本次装配预期新增 tools 挂载面＝首挂载件（上次装配面无 tools 目录＝起草实测坐实）；件数差集归因按 §七 J-2 口径。

## 一、四段动作序与逐段验收判据

### 段⓪ 版本 bump 笔（本票写集内·①段之前先行落链）

- 动作＝三同源 0.1.30→0.1.31 就地改值＋bundle.lock 行 8 note 沿革追加（口径见 §三），单 commit 落链。
- 写位闭集（逐文件列位·恰两文件三 version 触点＋一 note 触点）：
  - agent-experts/baigong-software-team/plugin.json＝行 3 version 一枚
  - agent-experts/baigong-software-team/bundle.lock＝行 5 version 一枚＋行 8 note 沿革追加一处
  - agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json＝行 3 version 一枚
- 判据（rev2 置换段⓪ numstat 行·红-1 勘正）：numstat 逐文件钉形制（夹具＝rev2 轮现跑 git diff --no-index --numstat 对复制件复现，禁凭推演）：
  - agent-experts/baigong-software-team/plugin.json＝1 增 1 删
  - agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json＝1 增 1 删
  - agent-experts/baigong-software-team/bundle.lock＝按取态分钉：J-3 甲案（rev2 已采＝现行口径）＝6 增 3 删（version 1/1＋note 同句替换 1/1＋assembly_exclude 落行＝tests/ 行逗点化 1/1＋三枚新条目行 3 增）；乙案形制备查＝2 增 2 删
  - 合计＝甲案 8 增 5 删（夹具实测在册＝rev2 回报随登）。原 v1「3/3」与 rev1「4/3」均不实＝作废。
- 其余判据零变：json 可载断言两 json＋bundle.lock 三件 parse-OK；改后 grep 三读数＝0.1.31 且仓内 0.1.30 于三文件零残留（bundle.lock 组件 note 沿革史文内旧版本号字样属史实锚＝不计残留，以行 5 唯一 version 键为准）；四件套门禁改前改后 exit 钉值全等（§〇.2 基线随轮照登）。
- 时序钉死句（rev2·PM 黄-2 落规格）：assembly_exclude 三枚条目（docs/PRODUCT.md／docs/ARCHITECTURE.md／docs/adr/）落行形制＝尾追加（tests/ 行行尾逗点化＋随后三行各一枚，逐字照 §十 K-3 块），与三同源 version 改动并入段⓪同一 commit——J-3 未裁态本不得落链 bump 笔（原时序口径随注）；J-3 经主理人采纳甲案后＝规格生效，bump 笔落链前置＝本票双席审票会师放行在案。

### 段① 装配（派工程师席·一票一新鲜实例）

- 动作序（rev2 补前置步·QA 黄-1）：**先删装配面** D:／multi-agent-collab-devkits-build／baigong-software-team 整目录（do_assemble 不清陈旧残留——manifest note 既有口径「重装配＝删装配面重跑」入正文动作列），再跑 python agent-skills/object-build/scripts/publish.py --assemble agent-experts/baigong-software-team。删前留装配面现盘件数读数（起草实测 90 件）随回执登记。
- 禁带 --out（先例教训：0.1.29 首跑误带 --out 指 build 根＝平铺污染）。缺省落点＝仓外同级 D:／multi-agent-collab-devkits-build／baigong-software-team（publish.py --out help 实证＋皮总既往指定交付面同路径）。
- 装配前置复测 M0：三同源三读数＝0.1.31（段⓪ bump 笔在案＝git log 查得；现值仍 0.1.30 或 bump 笔不在案＝停手上报）；git status --porcelain -uno 除 ledger 一枚他案 M 外空——该枚 M 与 publish.py 纪律⑤ clean 闸（行 679 实证＝-uno 非空即 exit 3）冲突取态＝§七 J-1 候裁，J-1 未裁①段不得强跑。
- 装配锚定 commit＝开工实测 HEAD（回执开端登记，≥段⓪ bump 笔）。锚定区间停手判据按 §〇.4 跑。

段①验收判据（全部机械可跑·读数附回执）：

| # | 判据 | 命令口径 | 钉值 |
|---|---|---|---|
| 1a | 产物三件套在位 | 装配面顶层枚举 | ASSEMBLY.manifest.json＋COPY.state 在位＋files 计数登记 |
| 1b | 件数对账 | 装配面 find 计数 vs 上次 88＋tools 面 18 件首挂载 | 非钉死＝差集逐行归因（§七 J-2 边界）：devkit-tools 首挂载＝预期增项；其余差集须逐行归因至 〇.3 增量批内容，不可归因＝停手 |
| 1c | 版本三读数 | manifest bundle_version＋装配面两 plugin.json grep version | 三读数彼此相等＝0.1.31 |
| 1d | 锚定钉值 | manifest bundle_source_commit | ＝开工实测 HEAD 全 sha 对应 |
| 1e | 幂等复跑 | 第二次直跑同命令 | COPY.state 块计数复跑前后相等（grep -c 形制 ^[sync n= 两读数相等）＋装配面字节无变化 |

段①收口＝五判据全绿＋回执读数；红＝停手不进②。

### 段② 预览（派工程师席·①收口后方可进）

动作序（六步·先备份后同步，顺序写死）：

1. 开工读数：市场源现值三读数（根 plugin.json／.codebuddy-plugin/plugin.json／marketplace.json baigong 条目）预期＝0.1.30；≠0.1.30＝停手上报（市场源现势与票面基线不符）。件数读数照登（起草实测 80 件）。
2. marketplace.json 部署前哈希登记（certutil -hashfile 或 python hashlib）。
3. 备份先行：robocopy /E 市场源现目录 → 新建备份目录（命名惯例照旧＝market-src-baigong-0.1.30-pre-deploy-20261117·随现值版本与当日日期；既往备份零覆盖零删·backup 面其余目录零触）。判据＝备份件数＝备份前市场源件数。
4. 同步：MSYS_NO_PATHCONV=1 robocopy /MIR 装配面 → 市场源包目录。判据＝全量对账非抽查：市场源与装配面文件清单 diff 空集＋逐文件哈希全量对账全等＋robocopy 失败计数 0。
5. 注册挂卡（必步·禁纯复制替代）：python 后接 C:／Users／peter／.workbuddy／plugins／marketplaces／workbuddy-builtin／skills／expert-manager／scripts／register_expert.py 的市场源包目录实路径＋--session-id 主理人派工给出的预览会话 UUID（参数真源见 〇.3；先例教训写死＝历轮预览卡丢失系纯文件复制丢注册步，deploy-gate §五实证②）。标记观测纪律：.created-by-session 即写即读登记内容读数，约 1 秒被平台回收＝已知行为，如实登记、不强留、不伪造。
6. 核验读数（rev2·QA 黄-2 改 json 解析级口径）：市场源三 version 读数＝0.1.31；marketplace.json 对比＝注册前后各跑一次 python json 解析（python -c 形制：json.load 后取 plugins 列表内 baigong-software-team 条目 version 值＝两值对比单独登记；他条目＝hjh-aigc-video-team／hjh-software-team 两条目 name＋version 四值注册前后逐值对拍），「差异仅 baigong 条目」判定以解析级读数为准，文件级哈希仅作幂等复跑对账（第二轮注册后哈希不变＝绿），两判定分写不禁混用。

段②收口回执呈报后按获批段界进③④（本票③非停等闸，见段③）。

### 段③ 人类闸（本批＝用户预授权当场过闸·不重跑·不可代跑条款留档）

- 本批特殊取态＝获批登记件（〇.1 用户指令原话＋选项原文「您指令即人类闸当场过」）使③段以引用获批件方式收口，不重跑真实验证清单。deploy-gate §五要点3「人类闸不可由代理代跑」零废除——本批非代理代跑，系决策者本人在指令中明示过闸；该条款对其他批照常生效，本票不为其创设例外。
- ③段验收判据＝回执引用获批登记件 §〇.1 三读数（指令原话／选项原文／段界）逐字在案＝绿；缺任一读数＝④不执行。
- 后验证留档：转正后用户实际使用现象回报归日志账；若出现不过现象＝按现象开票回修，修复后重走①②④（deploy-gate §五要点4 同款处置，市场源按 §五 回滚）。

### 段④ 转正进宿主缓存（派工程师席·③收口后）

前置核对（缺一＝④不执行）：③收口读数＋〇.1 批准登记复读读数＋主理人转呈的④派发读数（含路径授权字样）。

动作：市场源已在位＝同段②步 5 命令形制再跑 register_expert.py 刷新（不带 --session-id 转正态刷新沿用先例口径）＋宿主更新进缓存（缓存面＝宿主自写，执行席只读观测）。注册动作回执附批准出处（〇.1 引文）。

段④验收判据：

| # | 判据 | 命令口径 | 钉值 |
|---|---|---|---|
| 4a | 缓存新增 | ls 缓存目录（仓外绝对路径见 〇.3） | 新增 0.1.31 目录；既有 0.1.1／0.1.22／0.1.24／0.1.27／0.1.29／0.1.30 全部在位零动 |
| 4b | 装载态核验 | 缓存 0.1.31 目录 plugin.json grep version＋.in_use 观测＋installed_plugins.json 条目 python 直读 | version＝0.1.31＋.in_use 在位读数照登＋条目 installPath／version 两读数翻正＝0.1.31（翻正前后两读数都登记） |
| 4c | 仓面零污染 | git status --porcelain -uno | 除回执件与 ledger 他案枚外空 |

宿主装载不达＝停手呈报宿主侧现象，禁手动向缓存目录复制文件（W5＝宿主自写面）。

## 二、写集闭集（超集即停手上报）

起草席（本票）写集＝仅本票面 .scratch/tickets/2026-11-17-BAIGONG-DEP0131-装配与本地WorkBuddy四段转正票-v1.md。

执行席写集＝以下七面闭集，此外零写：

| # | 面 | 路径 | 写形态 |
|---|---|---|---|
| W1 | 仓面 bump 触点 | 段⓪写位闭集三文件（§一段⓪列位） | 单独 commit（collab: 前缀） |
| W2 | 装配面（仓外） | D:／multi-agent-collab-devkits-build／baigong-software-team | 装配器覆盖写（删装配面重跑口径） |
| W3 | 本地市场源包目录 | C:／Users／peter／.workbuddy／plugins／marketplaces／my-experts／plugins／baigong-software-team | robocopy /MIR 同步 |
| W4 | marketplace.json＋.created-by-session 预览标记件 | C:／Users／peter／.workbuddy／plugins／marketplaces／my-experts／.codebuddy-plugin／marketplace.json；市场源包目录内 .created-by-session（rev2·PM 黄-1 具名并入） | 仅经 register_expert.py 写入，禁手改；.created-by-session 为脚本注册步即写物＝非独立写面，观测读数即写即读登记（约 1 秒被平台回收＝已知行为） |
| W5 | 市场源备份目录（新建） | C:／Users／peter／.workbuddy／backup／market-src-baigong-0.1.30-pre-deploy-20261117 | robocopy /E 新建 |
| W6 | 宿主缓存＋installed_plugins.json | C:／Users／peter／.workbuddy／plugins／cache／my-experts／baigong-software-team（新增 0.1.31 子目录）；C:／Users／peter／.workbuddy／plugins／installed_plugins.json（rev2·PM 黄-1 具名并入） | 两文件均宿主自写，执行席只读观测（4b 判据即读 installed_plugins.json 条目两读数前后照登） |
| W7 | 回执件（仓内） | agent-experts/baigong-software-team/.collab/receipts/2026-11-17-BAIGONG-DEP0131-回执-v1.md（分段可加后缀分件） | 单独 commit·collab: 前缀 |

## 三、bundle.lock note 行更新口径（append-only 沿革追加）

bundle.lock 行 8 note 现文（bundle 本体版本行·纪律①④句）保持逐字零动，仅在句末追加沿革片段（append-only＝只追加不回改既有文字）。追加后可照录文本：

```
"note": "bundle 本体版本行（semver·每变必 bump＝纪律①；版本值与 .codebuddy-plugin/plugin.json 的 version 同源，装配步不注入版本号＝纪律④产物不可手改）。沿革：0.1.30→0.1.31＝合并批升号（裁定登记 2026-11-07·案 a）＝自 0.1.30 转正以来 PROJINIT／SEMGV／模板线／SCRATCHCFG／DEBTCLN 五批次增量合并重装；devkit-tools 组件自此批起首挂载进装配面"
```

- 工程师照录上块 verbatim（构成条款实质·块内零反引号；块内路径 token 属 JSON 字符串字面＝非指针落笔）。
- 若主理人／双席审票对沿革措辞有改，以审后定稿 verbatim 替换本块，纪律①④原句仍零动。

## 四、禁动面（全段通用·触及即红·停手上报）

1. 远端市场零动作：不发任何市场发布／上架／推送命令；REMOTE-PUB 面零触；0.1.31 占号依据＝2026-11-07 裁定登记件（REMOTE-PUB 预留不钉号），REMOTE-PUB 顺延后续号。
2. FUXI 零碰：agent-skills/fuxi-skill/ 面及其 .scratch 族、FUXI tags 零触；锚定区间差集若现 FUXI 渗入 bundle／组件面＝即停呈报。
3. 历史件零回改：链上已收口票／回执／审件／decisions 零改；bundle.lock 组件 note 沿革史文零动（仅行 8 bundle 本体 note 按 §三 追加）。
4. 他案脏面零带入：ledger.jsonl M 枚及其后随他案改动零 add 零清理零 stash；untracked 活体群零碰。
5. 账本零手写：agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl 禁任何手写写入（状态变更必经脚本·席位守则）。
6. 既有备份零触零删：C:／Users／peter／.workbuddy／backup 下既往十枚目录零触；装配面遗留件（baigong-software-team-0.1.29.zip、baigong-software-team.pre-cln-old）零触零删。
7. marketplace.json／installed_plugins.json 禁手改（只经注册脚本／宿主）。
8. 装配步禁带 --out；build 根面（W2 之外）零写。
9. 缓存目录禁手动写入（W6＝宿主自写面）；旧版本缓存目录零删。
10. 段③任何形态「代理代跑验证」指令到达执行席＝拒绝并回执登记（deploy-gate §五要点3）。

## 五、回滚路径

- 触发场景枚举：① 转正后用户真实使用出现不过现象（现象回报即触发评估）；② ②／④段中途失败＝市场源已处新内容中间态、注册报错、判据读数不达——两条处置路径＝还原（下方命令）或留置候主理人裁（回执登记现象后停手），执行席不得自行择路续跑。
- 市场源一键还原＝MSYS_NO_PATHCONV=1 robocopy /MIR 以段②步 3 回执登记的实际备份路径为源、市场源包目录为目标 还原（deploy-gate §五要点4）。还原路径耦合注（先例 QA Y3 沿用）：票面备份名含日期 20261117 与实际创建名存在跨日错位风险——还原一律以回执实际备份路径逐字读数为准，禁按票面字面另拼。
- 还原后 marketplace.json 回 0.1.30＝再跑 register_expert.py 刷新（市场源已回旧内容＝注册读数自然回旧值）；哈希基准＝段②步 2 登记的部署前哈希对账回等＝绿。
- 缓存面回滚口径：0.1.31 已进缓存＝禁手动删（W6 宿主自写面）；回滚判据＝市场源三 version 读数回 0.1.30＋与备份目录全量哈希对账全等；宿主是否自动回落 0.1.30 装载态＝未实证现象，如实呈报候主理人裁（installed_plugins.json 条目读数前后照登）。
- 装配面 W2＝仓外预览面非真源，还原无需回滚（留待下批重装配）。
- 仓面 bump 笔回滚＝段⓪笔 revert 另案微票（链上 revert，禁 amend／禁 reset）。

## 六、命令块（执行段照跑·自靶验证在附节读数·rev2 勘正原误指 §五）

本票所有命令已在 §〇.2／§一／§二 各判据列明命令口径；引用的验证命令起草轮已现跑：check-pointers 缺省／lint／csot／run-gates 四件（§〇.2 读数）；publish.py --help 用法面（--assemble／--out 缺省句实证）；register_expert.py docstring 与 argparse 分支实证＋--help 面差实证；git diff 锚定区间形制实证；robocopy /MIR 与 /E 形制沿用两先例部署票实跑在册形制。装配与注册两步属部署闭集动作＝起草席零跑，由执行席按本票照跑。

## 七、候裁条款（票面对应点停手上报·不自行处理）

- J-1 装配 clean 闸与 ledger 他案脏面冲突取态：publish.py 纪律⑤（行 679 实证）＝-uno 已跟踪面非空即 exit 3；开工前置允许 ledger.jsonl 一枚他案 M 照登豁免，两制冲突。三案供裁：(a) 主理人协调 ledger 归属案收口落链后开工（仓面真 clean）；(b) 归属案席位即时点落链该枚账本行（非本票动账本）；(c) 其他取态。J-1 未裁＝①段不得强跑（禁自行 stash／checkout／commit 他案面）。
- J-2 件数差集归因边界：装配面 files 预期基线＝上次 88＋devkit-tools 首挂载增项（share tag 树 18 件·装配排除面后实数以 manifest 为准）。判据口径：差集全部可归因（devkit-tools 首挂载＋〇.3 增量批文件增减）＝绿；出现无法归因行＝停手呈主理人，不得以「数量相近」放行。归因表随①回执逐行列出。J-3 采甲案时基线再减 docs 裁出三件（§九），归因表随动。
- J-3 docs 装配排除取态（rev1 增·主保证＝皮总拍）：docs 族是否本批即裁出装配面（§九 取证与规格在册）。两案：(a) 本批即排＝按 §九 规格落 bundle.lock assembly_exclude 三条目（docs 族仅 STRUCTURE.md 保留入包）；(b) 本批照旧入包＋另票修路（docs 排除归后续独立微票）。J-3 未裁＝①段可跑但 assembly_exclude 维持现值五条目不动（现值即含 docs/SWB-交接件一枚＝既有排除面），装配面 docs 族按现值态出面对账。
- 停止条款汇总（遇此即停）：三同源读数与 0.1.31 预期态不符／市场源现值≠0.1.30／批准登记读数不含本段授权／锚定区间现不可归因面／注册脚本报错（如实回报，禁另路伪造标记或手改 marketplace.json）／宿主缓存判据不达（呈报宿主侧现象）／同席多实例并发＝立即停手报告（席位守则）。

## 八、回执体例

- 各段收口各出回执（W7·可分件：段⓪兼 bump 落链登记／①装配回执／②预览回执／④转正回执兼全链终回执），开端附开工 HEAD 读数＋批准登记读数＋J-1／J-2 裁定读数；单独 commit、collab: 前缀、pathspec 只含回执件、add 与 commit 紧邻无窗口、FX_COMMIT_DECLARE 声明挂 commit 命令侧、禁 add -A／amend／--no-verify、message 零 at 零反引号、commit 类 timeout 七分钟档。
- 回执计数上限钉 4 件（③段收口并入②或④回执登记）；终段内容并入④回执：四段判据读数＋版本三对账（仓面／装配面／缓存＝0.1.31）＋批准出处引用＋还原基准注记（备份实况件数读数）。

## 九、docs 装配排除（rev1 增段·皮总指令性问题入票·取证与规格）

### 九.1 现场取证（rev1 轮现跑·禁抄旧数）

- assembly_exclude 现值（bundle.lock 行 53-59 直读）＝五条目闭集：README.md／docs/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md／skills/deep-research/README.md／skills/external-advisor-collab/references/90-changelog.md／tests/。＝docs 族已有既有条目一枚（交接件·精确 relpath 型），CLN-PURE S1 机制在位坐实。
- 装配面 docs 现态＝四件入包：ARCHITECTURE.md／PRODUCT.md／STRUCTURE.md／adr/0001-adr-initiation-trigger-criteria.md（-build 面与宿主缓存 0.1.30 两侧 ls 实测一致；仓面另有 SWB-交接件一枚已被排除＝五条目对账吻合）。
- docs 运行时消费点（禁全排依据·实测在册）：
  - agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md 行 31＝「本仓百工项目锚＝agent-experts/baigong-software-team/docs/STRUCTURE.md」——席位规范指包内 docs/STRUCTURE.md；
  - agent-experts/baigong-software-team/skills/sop/scripts/ 四脚本 project_root 探针序③＝STRUCTURE.md 事后校验路（commit-audit.py 行 83 _structure_hit／lease-issuer.py 行 59／memory-neutralize.py 行 71／write-guard.py 同族；docstring 行 93 探测序同文）。夹具实测（rev1 轮·-build 现盘）：cwd＝含 docs/STRUCTURE.md 的夹具目录→四路探针输出翻正＝夹具根；cwd＝装配面自身→落包根（fail-safe）＝两路读数登记在案（③段判据同款形制）。
  - 其余引用面（software-team-engineer.md 行 40／software-team-qa.md 行 39／dev-discipline.md 行 83／ledger-init.sh 行 11）均以 docs/STRUCTURE.md 为项目根探针锚语义＝保留该一枚即全覆盖；PRODUCT.md／ARCHITECTURE.md／adr 子面在包面运行时零消费点（rev1 grep 实测：仅 software-team-lead.md 行 51 提及 docs/adr＝主理人仓内落盘语义、standard-sop.md 行 58 提及 docs/ARCHITECTURE.md＝开发面路径语义，两处均不要求包内实存）。

### 九.2 谓词能力口径（publish.py 源码定口径·非臆测）

- parse_assembly_exclude（行 795-815）＋is_assembly_excluded（行 817-821）实证：条目两型＝装配面 relpath 精确全等／尾斜杠目录前缀条目（锚定装配面根）；禁通配（星号问号方括号即 die_usage exit 2）／禁绝对路径／禁 .. 段；键缺席＝空清单。
- **组合能力判定＝支持**：「排目录＋豁免单文件」不可用「docs/ 前缀条目＋docs/STRUCTURE.md 反向豁免」表达（谓词无豁免语义），但可用两枚精确条目＋一枚前缀条目等效表达——不排 docs/ 整目录，改精确列出待裁三件：docs/PRODUCT.md、docs/ARCHITECTURE.md、docs/adr/（尾斜杠前缀条目）。＝机制零缺口，无需改 publish.py（发布器能力禁令守住）。

### 九.3 规格取态（甲案＝本批即排的落点规格·J-3 裁甲时生效）

- bundle.lock assembly_exclude 由五条目增至八条目＝追加三枚（append-only·既有条目零动）：docs/PRODUCT.md／docs/ARCHITECTURE.md／docs/adr/。docs/STRUCTURE.md 保留入包＝部署态两处消费点（collab-fixed-structure.md 行 31＋四脚本探针序③）不指向真空。
- 写集随动：该三枚追加属 bundle.lock 行 53-59 段内追加一行改两行形态，并入 §一 段⓪ bump 笔同一 commit（W1 写位闭集随之补「bundle.lock 行 58 后追加三条目」一处；numstat 判据随动＝3 增 3 删改为 4 增 3 删·追加行为纯增行）。
- 装配面判据随动（J-3 裁甲）：1b 归因基线减 docs 裁出三件；新增机械判据 1f＝装配面 ls docs 目录实测＝仅 STRUCTURE.md 一枚在列（PRODUCT.md／ARCHITECTURE.md／adr 零在列）＋装配面四脚本探针夹具路复跑（夹具＝临时含 docs/STRUCTURE.md 目录·用毕即拆）读数＝夹具根翻正＝绿。
- 回滚口径随动：assembly_exclude 追加行随 bump 笔 revert 一并回滚（§五 仓面回滚条款同笔同案，无独立还原面）；市场源／缓存还原口径零变。

## 十、候裁归并落规格（rev2 增段·主理人已按「不上楼」过滤采纳·不再呈拍）

双席快审回流＝产品席红 0 黄 3 绿 2（判词在链 87 行·入库笔 0bfef02 卷入案型另登不涉本票效力）＋QA 席红 1 黄 3（判词 blob 5478976d）。红-1 与六黄落位全部原位置换／随注于对应段（段⓪ numstat 行＝红-1 勘正／段①动作列＝QA 黄-1／段②步 6＝QA 黄-2／W4·W6 行注＝PM 黄-1／段⓪时序句＝PM 黄-2／§六 与票头自注节号＝PM 黄-3／§〇.4 十六件句＝QA 黄-3）。本节落三枚候裁采纳规格，置换 §七 对应候裁态：

- **K-1（J-1 采 (b)）**：装配 clean 闸取态＝归属件 ledger.jsonl 那枚 M 由**归属线**（账本写入必经脚本之归属案席）在①段开工时点即时落链清闸——前置动作＝①段开工第一步跑 git status --porcelain -uno 读数，若 ledger 仍 M＝回执登记并请主理人转归属席落链，落链后复读数＝空方可进 publish.py（落链责任席＝该账本行归属案执行席·非本票任何席）；归因注记写死＝该笔系他案内容零改写零触碰仅归属落链，链上归因随①回执登记。本票各席对 ledger.jsonl 仍零写零 add（§四.4／§四.5 零变）。
- **K-2（J-2 采归因口径照单）**：件数对账三基线＝上次装配 manifest files 88／devkit-tools 首挂载 share tag 树 18／装配面现盘 90——三读数双席快审已独立复现对钉（读数在两根判词在册）。执行口径＝①段以装配面实出 files 对「88＋18−docs 裁出三枚（K-3 生效态）」预期值差集逐行归因至已收口批次（PROJINIT／SEMGV／模板线／SCRATCHCFG／DEBTCLN＋devkit-tools 首挂载）即绿；出现不可归因行＝停手呈报，不得以数量相近放行；归因表随①回执逐行列出。
- **K-3（J-3 采甲案·§九.3 规格生效）**：bundle.lock assembly_exclude 五条目增至八，落行形制钉死＝列表尾追加（tests/ 行行尾逗点化＋其后三行各一枚），可照录块：

```
    "tests/",
    "docs/PRODUCT.md",
    "docs/ARCHITECTURE.md",
    "docs/adr/"
```

  - docs/STRUCTURE.md 保留入包（§九.1 两处消费点不指向真空）；夹具实测 numstat（rev2 轮 git diff --no-index --numstat 对复制件复现）＝bundle.lock 6 增 3 删＝并入段⓪合计 8 增 5 删（逐文件钉值见 §一段⓪ rev2 置换行）。
  - 随批注一行（PM 建议采纳）：bundle.lock 行 8 note 沿革句尾追加「；docs/PRODUCT.md 与 docs/ARCHITECTURE.md 与 docs/adr/ 系 assembly_exclude 裁出非缺失」——防部署态读者误判。§三 verbatim 块以本节追加后文本为准：

```
"note": "bundle 本体版本行（semver·每变必 bump＝纪律①；版本值与 .codebuddy-plugin/plugin.json 的 version 同源，装配步不注入版本号＝纪律④产物不可手改）。沿革：0.1.30→0.1.31＝合并批升号（裁定登记 2026-11-07·案 a）＝自 0.1.30 转正以来 PROJINIT／SEMGV／模板线／SCRATCHCFG／DEBTCLN 五批次增量合并重装；devkit-tools 组件自此批起首挂载进装配面；docs/PRODUCT.md 与 docs/ARCHITECTURE.md 与 docs/adr/ 系 assembly_exclude 裁出非缺失"
```

  - §九.3 判据 1f 生效（装配面 ls docs 仅 STRUCTURE.md 一枚在列＋四脚本探针夹具路复跑翻正）；J-3 未裁态候补句作废（乙案形制仅留 §一段⓪备查一行）。

## 附、票面自查读数（起草轮现跑）

- 自靶＝python share/check-pointers.py --root . --target .scratch/tickets/2026-11-17-BAIGONG-DEP0131-装配与本地WorkBuddy四段转正票-v1.md → v1 轮 exit 0（读数随 v1 commit message 登记）；rev1 轮增补后复跑 exit 0（读数随 rev1 commit message 登记）；rev2 轮修订后复跑 exit 0（读数随 rev2 commit message 登记）。
- 全文零 at 零反引号自查＝grep 计数 0；仓内引用仓根相对纯路径裸文、叙述与仓外路径全角斜杠自查在册。
- 起草席 scratch 工作族＝.scratch/arch-dep131/（取证留痕·完工随族自删）。
