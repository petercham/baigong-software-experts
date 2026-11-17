# BAIGONG-DEP0131 · 装配与本地 WorkBuddy 四段转正票（v1·0.1.30→0.1.31 合并增量批）

- 票号：BAIGONG-DEP0131（族名锁定，勿改）
- 票型：独立部署票（deploy-gate 硬门 §二.1：部署闭集动作只立单独部署票，禁并入他票尾注条款）
- 起草席：架构席 arch-dep131（fresh 实例·主理人派工）
- 获批段界：到④转正止（§〇.1 登记＝用户同一指令明示授权载体成立·deploy-gate §四）
- 版本钉值：0.1.31（三同源 bump 触点在本票写集内＝§一 段⓪先行笔）
- 起草段产出＝仅本票面一件，单独 commit；起草席零执行任何部署动作、零碰装配面／市场源／缓存
- 纪律真源＝agent-experts/baigong-software-team/skills/software-orchestration/references/deploy-gate.md §二（独立票＋获批）、§四（用户同一指令明示含路径＝该次可直做）、§五（四段链①装配→②预览→③人类闸→④部署＋获批范围按段界定＋市场源备份一键回滚）
- 体例参照＝两枚先例票（.scratch/tickets/2026-11-06-GWP-DEPLOY-0.1.30-四段链部署票-v1.md／.scratch/tickets/2026-11-07-PROJINIT-DEPLOY-四段链部署票-v1.md），逐节参照；差异面（获批载体＝用户选段原文／bump 在本票内／四组件面装配含 devkit-tools 挂载／段界已明示）按本批实况改写
- 候裁点：2 枚（§七 J-1 装配 clean 闸与 ledger 他案脏面冲突取态／J-2 件数差集归因边界）——其余钉值全部本票钉死

> 票面自注（防自咬体例）：本票正文对仓内文件引用一律仓根相对纯路径裸文（正斜杠）；叙述性提及与仓外绝对路径用全角斜杠（／U+FF0F）；全文零 at 符号、零反引号。§六 命令块内为可照跑实文本（仓根相对段为正斜杠纯路径；仓外面命令含 Windows 绝对路径＝执行段专用，段界由执行席按命令块照跑，叙述面不落反引号）。本票成文后自靶 python share/check-pointers.py --root . --target 本票面仓根相对路径 须 exit 0（读数见 §五）。

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
- 锚定区间停手判据：开工时跑 git -c core.quotepath=off diff --name-only e880edb..<开工HEAD>，对 bundle 跟踪面（agent-experts/baigong-software-team/ 除 .collab/、.scratch/、tests/、README.md、docs/SWB-交接件）／本仓组件面（agent-skills/external-advisor-collab/、agent-skills/claim-commitment-governance/）／share 料源面 逐一列读数。本批＝增量批＝diff 非空属预期（起草实测：bundle 交付面 16 件 M、share 面多件 M、EAC／CCG 组件面空）——差集须逐行归因＝全部可归因至已收口批次（PROJINIT／SEMGV／模板线／SCRATCHCFG／DEBTCLN）＝绿；出现不可归因面（含 FUXI 线渗入 bundle 面）＝停手复核呈主理人。
- 组件面·skills 仓段：跨仓组件判据＝在 skills 仓跑 git rev-list -n1 后接 deep-research tag v1.0.2 的连拼 tag 名（照 bundle.lock 行 25 字面连拼）＝起草实测 730962e160bcf5b25f549c21f17c2c36848f4dfe，与 bundle.lock 行 25 ref 钉值一致性＋与前批回执登记读数比对；ref 未变＋tag sha 相等＝绿。
- devkit-tools 组件面：tag sha 起草实测 291ab447…（tag 建 2026-11-10＝晚于上次装配 e880edb）——本次装配预期新增 tools 挂载面＝首挂载件（上次装配面无 tools 目录＝起草实测坐实）；件数差集归因按 §七 J-2 口径。

## 一、四段动作序与逐段验收判据

### 段⓪ 版本 bump 笔（本票写集内·①段之前先行落链）

- 动作＝三同源 0.1.30→0.1.31 就地改值＋bundle.lock 行 8 note 沿革追加（口径见 §三），单 commit 落链。
- 写位闭集（逐文件列位·恰两文件三 version 触点＋一 note 触点）：
  - agent-experts/baigong-software-team/plugin.json＝行 3 version 一枚
  - agent-experts/baigong-software-team/bundle.lock＝行 5 version 一枚＋行 8 note 沿革追加一处
  - agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json＝行 3 version 一枚
- 判据：numstat 恰 3 增 3 删（note 行＝同行替换仍计 1／1）；json 可载断言两 json＋bundle.lock 三件 parse-OK；改后 grep 三读数＝0.1.31 且仓内 0.1.30 于三文件零残留（bundle.lock 组件 note 沿革史文内旧版本号字样属史实锚＝不计残留，以行 5 唯一 version 键为准）；四件套门禁改前改后 exit 钉值全等（§〇.2 基线随轮照登）。

### 段① 装配（派工程师席·一票一新鲜实例）

- 动作＝python agent-skills/object-build/scripts/publish.py --assemble agent-experts/baigong-software-team
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
6. 核验读数：市场源三 version 读数＝0.1.31；marketplace.json 注册前后哈希对比＝差异仅 baigong 条目；注册复跑幂等（第二轮跑后哈希不变）＝绿。

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
| W4 | marketplace.json | C:／Users／peter／.workbuddy／plugins／marketplaces／my-experts／.codebuddy-plugin／marketplace.json | 仅经 register_expert.py 写入，禁手改 |
| W5 | 市场源备份目录（新建） | C:／Users／peter／.workbuddy／backup／market-src-baigong-0.1.30-pre-deploy-20261117 | robocopy /E 新建 |
| W6 | 宿主缓存 | C:／Users／peter／.workbuddy／plugins／cache／my-experts／baigong-software-team（新增 0.1.31 子目录） | 宿主自写，执行席只读观测 |
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

## 六、命令块（执行段照跑·自靶验证在 §五读数节）

本票所有命令已在 §〇.2／§一／§二 各判据列明命令口径；引用的验证命令起草轮已现跑：check-pointers 缺省／lint／csot／run-gates 四件（§〇.2 读数）；publish.py --help 用法面（--assemble／--out 缺省句实证）；register_expert.py docstring 与 argparse 分支实证＋--help 面差实证；git diff 锚定区间形制实证；robocopy /MIR 与 /E 形制沿用两先例部署票实跑在册形制。装配与注册两步属部署闭集动作＝起草席零跑，由执行席按本票照跑。

## 七、候裁条款（票面对应点停手上报·不自行处理）

- J-1 装配 clean 闸与 ledger 他案脏面冲突取态：publish.py 纪律⑤（行 679 实证）＝-uno 已跟踪面非空即 exit 3；开工前置允许 ledger.jsonl 一枚他案 M 照登豁免，两制冲突。三案供裁：(a) 主理人协调 ledger 归属案收口落链后开工（仓面真 clean）；(b) 归属案席位即时点落链该枚账本行（非本票动账本）；(c) 其他取态。J-1 未裁＝①段不得强跑（禁自行 stash／checkout／commit 他案面）。
- J-2 件数差集归因边界：装配面 files 预期基线＝上次 88＋devkit-tools 首挂载增项（share tag 树 18 件·装配排除面后实数以 manifest 为准）。判据口径：差集全部可归因（devkit-tools 首挂载＋〇.3 增量批文件增减）＝绿；出现无法归因行＝停手呈报主理人，不得以「数量相近」放行。归因表随①回执逐行列出。
- 停止条款汇总（遇此即停）：三同源读数与 0.1.31 预期态不符／市场源现值≠0.1.30／批准登记读数不含本段授权／锚定区间现不可归因面／注册脚本报错（如实回报，禁另路伪造标记或手改 marketplace.json）／宿主缓存判据不达（呈报宿主侧现象）／同席多实例并发＝立即停手报告（席位守则）。

## 八、回执体例

- 各段收口各出回执（W7·可分件：段⓪兼 bump 落链登记／①装配回执／②预览回执／④转正回执兼全链终回执），开端附开工 HEAD 读数＋批准登记读数＋J-1／J-2 裁定读数；单独 commit、collab: 前缀、pathspec 只含回执件、add 与 commit 紧邻无窗口、FX_COMMIT_DECLARE 声明挂 commit 命令侧、禁 add -A／amend／--no-verify、message 零 at 零反引号、commit 类 timeout 七分钟档。
- 回执计数上限钉 4 件（③段收口并入②或④回执登记）；终段内容并入④回执：四段判据读数＋版本三对账（仓面／装配面／缓存＝0.1.31）＋批准出处引用＋还原基准注记（备份实况件数读数）。

## 附、票面自查读数（起草轮现跑）

- 自靶＝python share/check-pointers.py --root . --target .scratch/tickets/2026-11-17-BAIGONG-DEP0131-装配与本地WorkBuddy四段转正票-v1.md → exit 0（读数随 commit message 登记）。
- 全文零 at 零反引号自查＝grep 计数 0；仓内引用仓根相对纯路径裸文、叙述与仓外路径全角斜杠自查在册。
- 起草席 scratch 工作族＝.scratch/arch-dep131/（取证留痕·完工随族自删）。
