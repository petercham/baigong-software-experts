# TK-PROJINIT-DEPLOY · 独立部署票：PROJINIT 项目锚定与初始化整改批 · 四段链部署（0.1.30 仓面增量批）

- 票 ID＝`TK-PROJINIT-DEPLOY`。票型＝独立部署票（deploy-gate.md §二.1：部署闭集动作只立单独部署票，禁并入他票尾注）。
- 起草席＝架构席 arch-pjdep1；起草实测 HEAD＝`8c07f24`（开工第一步 `git rev-parse --short HEAD` 读数，≥ 派工基线 `8c07f24`）。
- 起草段产出＝本票面一件，单独 commit；起草席零执行任何部署动作、零改任何代码。
- 批准载体＝仓根 `.collab/decisions/2026-11-07-皮总指令-PROJINIT装配部署链开工.md`（皮总原话「装配部署链开工，交付面 "D:\multi-agent-collab-devkits-build"」）；**获批段界未明示＝候裁（§七 J-2）**。
- 版本咬合＝本批核心矛盾：三面现值均已是 0.1.30，PROJINIT 改动系 0.1.30 版本号之下的仓面增量（零 bump 口径）——**版本择案候裁（§七 J-1），票面全部版本钉值留白待裁，不自行钉号**。
- 纪律真源＝`agent-experts/baigong-software-team/skills/software-orchestration/references/deploy-gate.md` §二（独立票＋获批两条件）、§五（四段链①装配→②预览→③人类闸→④部署＋「获批范围按段界定／验证不过回修重走①②／市场源备份一键回滚」要点）。本票各段验收判据即引该件条款为据。
- 体例参照＝GWP-DEPLOY 先例票（`.scratch/tickets/2026-11-06-GWP-DEPLOY-0.1.30-四段链部署票-v1.md`，含 rev1 消化面），本票逐节参照；差异面（版本基线／被部署内容／③清单／锚定区间基准）按本批实况改写。
- **rev1 修订笔（2026-11-07·作者席 arch-pjdep1 原位修订·开工 HEAD 实测 `8f98033`）**：双席独立审票会师＝双席一致放行·红 0 无对立分歧——产品席审件 `69a3a7f`（放行带修·黄2）＋QA 席审件 `8f98033`（放行·黄3）。本笔消化五黄（PM Y1 过渡口径对账段补写／PM Y2 ③判据4 注入形制钉死／QA Y1 ③判据5 human 行断言限定口径／QA Y2 组件面锚定命令形制改 skills 仓 tag sha 比对／QA Y3 还原命令以回执实际备份路径读数为准）。修订面＝判据补强/登记文字级；**获批登记、四段结构、候裁节两案框架（钉值继续留白）、禁动面、③清单六条框架零动**。
- **过渡口径对账（rev1·PM Y1）**：deploy-gate.md L33 自带过渡口径注（v2.9 §20.1⑤：独立 deploy-gate 四段卷→发布硬门禁二＋灰度机械门禁＋转正代写，**四段流程保留为装配运维面**）——本批＝本地装配运维面四段链＋开工登记件（2026-11-07 皮总指令）批准载体，对账成立。deploy-gate §五①段前置括注「票面写清目标段＝只到预览」＝**默认示例非本票约束**；本票获批段界＝以登记件＋皮总最终明示为准（0.1：默认全程批到④止，段界未明示前执行席只到②收口即停）。

## 〇、获批登记与写集闭集

### 0.1 获批登记（票面开端·执行前置）

- 批准出处＝`.collab/decisions/2026-11-07-皮总指令-PROJINIT装配部署链开工.md`：皮总明示「装配部署链开工」＝deploy-gate §二.2 人类明示开工批准载体；**获批段界未明示**（登记件§二.3 自证在册）。
- **票面默认口径（写死·以皮总最终明示为准）**：按先例默认写「全程四段（批到④止）＋③人类闸仍停等皮总真实验证明示」；**段界未获皮总明示前，执行席只到②收口即停**（两候选＝批到②止／批到④止，登记件《获批段界选项》在册，主理人呈裁后按裁定修订本票）。
- **各段执行前核对批准在案（写死）**：①②④每一段开工第一步＝直读上述登记件并在工作回执登记读数＋主理人转呈的段界明示读数；缺登记/读数不含本段授权字样＝停手，回执登记「部署项缺批准」（deploy-gate §三执行席义务），等主理人补呈报。
- 获批范围按段界定（deploy-gate §五要点1）：即便批到④止，④前置＝③人类明示通过＋明示批准（§二.2），两条件任一缺＝④不得执行。

### 0.2 被部署内容（链上实绩·只读取证在案）

- 被部署批＝TK-PROJINIT 项目锚定与初始化整改批（票面 `.scratch/tickets/2026-11-06-PROJINIT-项目锚定与初始化整改票-v2.md`）：交付笔 `a4aefb7`（恰 8 件，起草复核 `git show --stat a4aefb7` 在案）→ 回执笔 `5d6c7a8`（回执件＝包内 `.collab/receipts/2026-11-06-TK-PROJINIT-工程师回执-v1.md`，判据 1-13 全绿）→ QA 独立验证红0黄0绿17（收口登记笔 `03bb0fe`）→ 收口登记 `03bb0fe`。
- 被检真源闭集（部署内容面·恰 8 件）＝`agent-experts/baigong-software-team/` 下：`skills/sop/scripts/{write-guard.py, lease-issuer.py, commit-audit.py, memory-neutralize.py}`（project_root 双显式路换代）＋`skills/software-orchestration/references/dev-discipline.md`（§十进场建档工序含 S1b＋§九.3 双根随动）＋`skills/software-orchestration/SKILL.md`（触发词/索引随动）＋`config/seat-permissions.json`＋`config/seat-permissions-hooks-map.json`（architect STRUCTURE 两键解锁＋五席 sources/** deny）。
- 版本面：PROJINIT 批零 bump（版本归 H-6 统筹口径）；仓面三同源现值＝0.1.30（起草实测 plugin.json L3／bundle.lock L5／.codebuddy-plugin/plugin.json L3 三读数在案）。版本择案＝§七 J-1 候裁。

### 0.3 写集闭集（超集即停手上报）

起草席（本票）写集＝**仅本票面** `.scratch/tickets/2026-11-07-PROJINIT-DEPLOY-四段链部署票-v1.md`。

执行席（①②④段）写集＝以下六面闭集，此外零写：

| # | 面 | 路径（起草实测取证·非臆测） | 写形态 |
|---|---|---|---|
| W1 | 装配面（仓外） | `D:\multi-agent-collab-devkits-build\baigong-software-team\` | 装配器覆盖写 |
| W2 | 本地市场源包目录 | `C:\Users\peter\.workbuddy\plugins\marketplaces\my-experts\plugins\baigong-software-team\` | robocopy /MIR 同步 |
| W3 | marketplace.json | `C:\Users\peter\.workbuddy\plugins\marketplaces\my-experts\.codebuddy-plugin\marketplace.json` | **仅经 register_expert.py 写入**，禁手改 |
| W4 | 市场源备份目录（新建） | `C:\Users\peter\.workbuddy\backup\market-src-baigong-0.1.30-pre-deploy-20261107\` | robocopy /E 新建（命名随本批现值版本与日期） |
| W5 | 宿主缓存 | `C:\Users\peter\.workbuddy\plugins\cache\my-experts\baigong-software-team\`（版本子目录随 J-1 裁定） | **宿主自写**，执行席只读观测 |
| W6 | 回执件（仓内） | `agent-experts/baigong-software-team/.collab/receipts/2026-11-07-PROJINIT-DEPLOY-回执-v1.md`（分段回执可加后缀分件） | 单独 commit·`collab:` 前缀 |

路径取证出处＝起草实测：交付面根实存（内含 `baigong-software-team\`＝GWP-DEPLOY 装配面遗留 81 件、`baigong-software-team-0.1.29.zip`、`baigong-software-team.pre-cln-old`——均既往遗留面，零触零删）；市场源两 plugin.json＋marketplace.json baigong 条目三读数＝0.1.30、件数 80；缓存目录列 `0.1.0/0.1.1/0.1.22/0.1.24/0.1.27/0.1.29/0.1.30`；`register_expert.py` 真源在位（路径同先例票 W3 注）。

## 一、段①装配（派工程师席·一票一新鲜实例）

**动作**：`python agent-skills/object-build/scripts/publish.py --assemble agent-experts/baigong-software-team`

- **缺省输出**＝仓外同级 `-build`（publish.py `--out` help 实证「缺省＝仓外同级 -build」；开工登记件 §二.2 实证缺省落点即皮总指定交付面 `D:\multi-agent-collab-devkits-build`）。**禁带 `--out`**——先例教训：0.1.29 装配首跑误用 `--out` 指 build 根＝平铺污染（0.1.29 回执在册）。
- 装配前置（publish.py 纪律⑤自带闸）：源仓已跟踪面 clean＋ref 可解析。开工复测项 **M0**＝起草取证读数复核：仓面三同源 `grep -n '"version"' agent-experts/baigong-software-team/plugin.json agent-experts/baigong-software-team/bundle.lock agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json` → 三读数；**预期值随 J-1**：批 (b)＝0.1.30（起草实测在案）；批 (a)＝bump 笔先行落链后三读数＝裁定版本号，现值仍 0.1.30 且 bump 笔不在案＝停手上报（bump＝仓面改动，归另案微票先行，非本部署票射程——见 §五.1）。另复测 `git status --porcelain -uno`＝空（起草实测空）。任一不符＝停手上报（他席先行污染真源＝停止条件）。
- 装配锚定 commit＝开工实测 HEAD（回执开端登记，≥`8c07f24`）。
- **锚定区间停手判据**：开工时在主仓跑 `git diff --name-only 03bb0fe..<开工HEAD>`（基准＝PROJINIT 收口登记笔 `03bb0fe`，非先例的 d3c0071）——读数对 **bundle 跟踪面**（`agent-experts/baigong-software-team/` 除 `.collab/`／`.scratch/` 段）／**组件面·本仓段**（`agent-skills/external-advisor-collab/`）任一有 diff＝**停手复核呈主理人**（防未获批内容随锚定进装配——M0 clean 只覆盖未提交脏面，本条覆盖已提交增量）。起草实测：`03bb0fe..8c07f24` 区间 bundle 面 diff＝空、本仓组件段 diff＝空，其余增量全系 `agent-skills/fuxi-skill/` 他项目面＋根 `.collab/` 治理面（＝绿，读数照登回执）。
  - **组件面·skills 仓段（rev1·QA Y2 改形制）**：跨仓组件真源＝skills 仓 `D:\multi-agent-collab-skills` 的 `skills/deep-research/`——主仓基准 sha `03bb0fe` 在 skills 仓不存在，**禁以主仓 sha 硬套字面直跑**（实跑报错）。机械形制＝以 bundle.lock 组件 ref 钉值比对：`grep -n '"ref"' agent-experts/baigong-software-team/bundle.lock` → L15 `external-advisor-collab@v1.1.3`＋**L25 `deep-research@v1.0.2`**（ref_kind＝tag，起草核实行号在案）；在 skills 仓跑 `git rev-list -n1 deep-research@v1.0.2`（tag sha 读数）＋与上次装配（GWP-DEPLOY ①段回执）登记的 tag sha 读数比对——ref 钉值未变＋tag sha 相等＝绿；ref 变更或 tag sha 漂移＝停手复核呈主理人。两读数照登回执。基线读数（起草实测在册）＝前批 GWP-DEPLOY 回执 L16 登记 tag 指向 `730962e`，skills 仓 `git rev-list -n1 deep-research@v1.0.2` 现值＝`730962e160bcf5b25f549c21f17c2c36848f4dfe` 相等＝起草段该面已绿。

**段①验收判据（全部机械可跑·读数附回执）**：

| # | 判据 | 命令口径 | 钉值 |
|---|---|---|---|
| 1a | 产物三件套在位 | 装配面顶层枚举 | `ASSEMBLY.manifest.json`＋`COPY.state` 两件在位＋交付件计数读数登记 |
| 1b | 件数对账 | 装配面文件总数（含两件） | 与 0.1.29/GWP-0.1.30 装配基线 **81 件**（79 交付＋manifest＋COPY.state）比对；≠81＝如实登记差集清单并停手呈报（PROJINIT＝在位文件就地改＋dev-discipline 增行，理论零增减件，差异须有人解释） |
| 1c | 版本三读数 | manifest `bundle_version`＋装配面 `.codebuddy-plugin/plugin.json` version＋装配面根 `plugin.json` version（grep） | **钉值留白待 J-1**：批 (a)＝裁定版本号（候选 0.1.31）；批 (b)＝0.1.30；三读数必彼此相等，否则即红 |
| 1d | 锚定钉值 | manifest `bundle_source_commit` | ＝开工实测 HEAD 短/全 sha 对应 |
| 1e | 幂等复跑 | 第二次直跑同命令 | 零写入：`COPY.state` 块计数复跑前后相等（`grep -c '^\[sync n=' COPY.state` 两读数相等）、装配面字节无变化 |

**段①收口**＝五判据全绿＋回执读数；红＝停手，不进②。

## 二、段②预览（派工程师席·①收口后方可进）

**动作序（六步·先备份后同步，顺序写死）**：

1. 开工读数：市场源现值取证＝根 `plugin.json`＋`.codebuddy-plugin/plugin.json` 两 version＋`marketplace.json` baigong 条目 version，三读数预期＝**0.1.30**（起草实测在案——**非先例的 0.1.29**，GWP-DEPLOY 已把 0.1.30 装进市场源）。≠0.1.30＝停手上报（市场源现势与票面基线不符）。**另登记市场源件数读数**：起草实测市场源现势＝**80 件**（缺 `settings.json`，先例 rev1·QA Y2 同族面差在册）——本批 `/MIR` 同步将以 81 件装配面拉齐（无害）；备份与 §六还原口径随之注明：**备份＝现 80 件实况为准**，还原后亦为 80 件态，回执登记此差集。
2. `marketplace.json` 部署前 SHA256 登记（`certutil -hashfile` 或 python hashlib）。
3. **备份先行**：robocopy /E 市场源现目录 → W4 备份目录（新建·命名 `market-src-baigong-0.1.30-pre-deploy-20261107`）。判据＝备份件数＝备份前市场源件数（逐一对数）；既往备份零覆盖零删（本票禁触 `backup\` 下其余目录）。
4. 同步：`MSYS_NO_PATHCONV=1 robocopy /MIR <W1装配面> <W2市场源>`。判据＝全量对账非抽查：市场源与装配面文件清单 diff 空集＋逐文件 SHA256 全量对账全等＋robocopy 失败计数＝0。
5. **注册挂卡（必步·禁纯复制替代）**：`python C:\Users\peter\.workbuddy\plugins\marketplaces\workbuddy-builtin\skills\expert-manager\scripts\register_expert.py <W2市场源包目录> --session-id <主理人派工给出的预览会话 UUID>`。先读 usage 确认参数形制 `<expert-dir> [--marketplace-dir] [--session-id]`，未猜参。**usage 面差注记（先例 rev1·QA Y3 沿用）**：脚本 stdout usage 打印不含 `--session-id`——该参数以脚本 docstring 与 argparse 分支实证支持（先例 QA 实跑吻合）；**usage 打印不作准**，不得据 usage 缺项误判参数不存在而弃带 `--session-id`。
   - 先例教训写死（deploy-gate §五实证②）：**历轮预览卡丢失＝纯文件复制丢注册步**——②段无注册步＝②未收口。
   - 标记观测纪律：`.created-by-session` 即写即读登记内容读数，**约 1 秒被平台回收＝已知行为**——如实登记读数，不强留、不伪造标记。
6. 核验读数：市场源根 plugin.json／`.codebuddy-plugin/plugin.json`／`marketplace.json` baigong 条目三 version＝**J-1 裁定值**（批 (b)＝0.1.30＝与现值同＝本步读数不翻转，核验点转为「条目哈希对比＋内容哈希对账装配面」）；`marketplace.json` 注册前后哈希对比＝差异仅 baigong 条目版本账目＋他条目（hjh 等）零动；注册复跑幂等（第二轮跑后哈希不变）＝绿。

**段②收口即停手呈报（票面写死）**：执行席到②收口即停，回执呈报「预览已挂、候人类闸」。**禁自动进④**——④派发权＝主理人持有，且前置＝③皮总明示通过＋段界明示（0.1）。

## 三、段③人类闸（停等·代理不可代跑）

- deploy-gate §五要点3 写死：人类闸不可由代理代跑，主理人/执行席不得以「我验证过了」充当③。
- 执行席与主理人此段零动作；主理人转呈下方验证要点清单交皮总，验证结果（过/不过/现象）回报归日志账。

**验证要点清单（架构席按 PROJINIT 八件修复面给出·交皮总③段用·装配态宿主实跑）**——夹具＝任一**空白宿主项目目录**（不含 `docs/STRUCTURE.md`、不含 `.workbuddy/swb-anchor`，记 `FP`），预览态挂上后在宿主内实跑四脚本探针序；四脚本路径统一记 `PKG\<脚本>`＝装配态包根 `C:\Users\peter\.workbuddy\plugins\marketplaces\my-experts\plugins\baigong-software-team\skills\sop\scripts\` 下对应件；逐件取样形制＝**逐件独立进程** `python -c "import runpy; print(runpy.run_path(r'<脚本绝对路径>')['project_root']())"`（禁同一命名空间串 exec＝假绿通道；判据内路径一律盘符正斜杠形，bash 挂载形仅 argv 通道可达）。

1. **env 覆写路**：cwd＝`FP\src`（自建）＋`SWB_REPO_ROOT` 覆写＝`FP` 绝对路径→逐件打 `project_root()`。钉值＝四读数**逐字一致＝覆写值原字面**（不做 abspath 归一·PROJINIT §3.1 条款1a）＝env 值生效。
2. **锚定声明件路**：无 `SWB_REPO_ROOT`；建 `FP\.workbuddy\swb-anchor`（内容首行 `project_root: .`）→cwd＝`FP\src`→逐件打 `project_root()`。钉值＝四读数逐字一致＝`FP` 绝对路径（锚件命中＝权威锚）。
3. **双缺位回落路（GWP-P1-1 探针序保持）**：删 `FP` 锚件、`FP` 无 STRUCTURE、无 env→逐件打 `project_root()`。钉值＝四读数逐字一致＝**包根**绝对路径（fail-safe＝与修前语义同＝降档路零回归）；随后造 `FP\docs\STRUCTURE.md`（无锚）复跑＝四读数翻正＝`FP`（事后校验路在位）。
4. **deny 面不破（fail-safe 不开窗）**：**注入形制钉死（rev1·PM Y2·参照先例 rev1·PM Y4 钉形制体例，按本判据＝正常 deny 路非 fail-closed 异常路取形）**：cwd＝未锚态 `FP`（无 env、无锚件、无 STRUCTURE——即判据3 场景）；跑 `python <装配态包根>\skills\sop\scripts\write-guard.py --path "<FP内任一路径，如 FP\docs\X.md>"`，stdin 喂合法 payload JSON 样例 `{"hook_event_name":"PreToolUse","tool_input":{"file_path":"<同上路径>"}}`（`--path` 为测试注入面·优先于 payload.tool_input——write-guard L316 实证；无租约注入＝payload 不含可归因身份字段）。钉值四项：① `--map` 缺省解析读数＝未锚态下 `--map` 缺省落**装配态包根** `config\seat-permissions-hooks-map.json`（pack_root fail-safe 降档路，回执登记该读数）；② stdout 逐字含 deny JSON（`hookSpecificOutput`＋`"permissionDecision":"deny"`＋`permissionDecisionReason` 非空——deny_output() L232-240 形制，ensure_ascii 转义中文属已知形制）；③ reason 含「席位不可归因」字样（身份缺位路 L259）；④ **exit＝0**（PreToolUse 决策经 JSON 表达，deny 正常路 exit 0——勿与先例 GWP 判据 6a 异常注入 fail-closed exit 2 形制混用，那条测的是坏 `--map` 异常路，本条测的是缺锚缺身份的正常 deny 路）。四读数任一不达＝红（fail-safe 落包根却开出 allow 通道＝开窗回归）。
5. **config 两片成文在位**：装配态两 config `python -c` json 可载＋断言＝architect `deny_globs` 不含 `docs/STRUCTURE.md`＋源件 architect `write_globs` 含 `docs/STRUCTURE.md`＋五席（host/product/architect/engineer/qa）`deny_globs` 含 `sources/**`（两文件十处）＋human 行零动（**rev1·QA Y1 限定口径**：该断言仅源件面 seat-permissions.json 可跑——六席含 human；hooks-map 面 `seats` 实况**无 human 行**（五席 host/product/architect/engineer/qa）系既成事实，回执照登「hooks-map 无 human 行＝既成事实非缺陷」，禁在 hooks-map 面跑该断言致假红）＋两文件 architect `deny_globs` 逐行全等（t13 等价口径现场复核）。
6. **建档工序可读（S1b 在册）**：装配态 `grep -c '进场建档'`、`grep -c 'S1b'`、`grep -c 'swb-anchor'` 对 `skills\software-orchestration\references\dev-discipline.md` 三读数各 ≥1（§十 S1-S6＋S1b 补行成文）；`skills\software-orchestration\SKILL.md` grep `swb-anchor` ≥1（触发词＋索引行随动）＝工序文书随装配可达。

**H-4 挂钩注记（不列③判据）**：钩子进程 cwd 实态取数属**部署后另票实测**（PROJINIT H-4 候裁在册·回执 5d6c7a8 已登记「钩子现盘未落痕呈裁」）——本票票面登记为后程，③段清单零含；「SWB_REPO_ROOT 注入载体落定或 hooks cwd ∈ 宿主树」条件未落定前，判据 2 场景在 hooks 相对命令形制下的边界读数（落包根＝fail-safe）系已知行为非本闸红项。

## 四、段④部署（派工程师席·③明示通过＋明示批准双前置＋段界明示）

**前置核对（三前置缺一＝④不执行）**：③皮总明示结论登记（主理人转呈记录在案）＋0.1 批准登记复读读数＋段界明示读数（含④授权字样）＋主理人对④的路径明示批准（deploy-gate §二.2）。

**动作**：市场源已在 W2＝`register_expert.py` 刷新（同②步5 命令形制）＋宿主更新进缓存（宿主自管 W5）。注册动作回执**附批准出处**（登记件路径＋批准读数引文）。

**段④验收判据**：

| # | 判据 | 命令口径 | 钉值 |
|---|---|---|---|
| 4a | 缓存版本目录 | `ls C:\Users\peter\.workbuddy\plugins\cache\my-experts\baigong-software-team\` | **随 J-1**：批 (a)＝新增 **`<裁定版本号>\`**（候选 `0.1.31\`）目录，旧目录 `0.1.0/0.1.1/0.1.22/0.1.24/0.1.27/0.1.29/0.1.30` 全部在位零动；批 (b)＝同版本刷新是否重建缓存**未实证**——判据改法候裁时定（J-1 批 (b) 附注），实测形制（内容哈希对账装配面＋时间戳/标记读数）照登回执 |
| 4b | 缓存内版本 | 缓存新目录（或 0.1.30 目录）`plugin.json` grep version＋`.in_use` 标记观测 | 版本＝J-1 裁定值＋`.in_use` 读数照登（0.1.29/0.1.30 回执同款转正实证形制） |
| 4c | 仓面零污染 | 源仓 `git status --porcelain -uno` | 除回执件外空 |

## 五、禁动面（全段通用·触及即红·停手上报）

1. **仓面真源零触**：部署票全程不改仓内任何已跟踪文件（`skills/`、`config/`、`hooks/`、`docs/`、版本三同源、`tests/` 等）；唯一仓内新写＝W6 回执件。**J-1 批 (a) 情形**：bump 至 0.1.31＝仓面版本三同源改动＝**另案微票先行落链**（GWP 随批 bump 先例＝bump 笔在装配锚定之前），本部署票自身仍零触版本面。
2. **REMOTE-PUB 面零触**：不做平台上架、不重打上架 zip；REMOTE-PUB 票面及其 §F 口径零触。**0.1.31 号位＝REMOTE-PUB 预留（不钉号）**——J-1 占用与否＝皮总裁决域，票面不自行占用。
3. **旧版本缓存目录不删**：W5 缓存下 `0.1.30` 及更早版本目录、市场源备份既往件、`baigong-software-team.pre-cln-old`、`baigong-software-team-0.1.29.zip` 等遗留面零触零删。
4. `marketplace.json`／`installed_plugins.json` 禁手改（只经注册脚本/宿主）。
5. 装配步 publish.py 禁带 `--out`（防平铺污染先例）；`-build` 根面（W1 之外）零写。

## 六、回滚条款

- **触发场景枚举**：① **③不过**（主判据场景）；② **②段中途失败**＝MIR 同步已完成／注册报错／核验读数不达（市场源已处新内容中间态）→ 两条处置路径＝**还原**（下方同一命令直接复用）或**留置候主理人裁**（回执登记现象后停手），执行席不得自行择路续跑④。
- **③不过/②失败还原**：市场源还原＝`MSYS_NO_PATHCONV=1 robocopy /MIR "<段②步3 回执登记的实际备份路径>" "C:\Users\peter\.workbuddy\plugins\marketplaces\my-experts\plugins\baigong-software-team"` 一键还原（deploy-gate §五要点4）。**还原路径耦合注（rev1·QA Y3）**：W4 备份名含日期 `20261107`，票面命令源串写死与实际创建名存在跨日错位风险——**还原一律以段②步3 回执实际备份路径逐字读数为准**，禁按票面字面另拼路径（同日内执行则两者一致）。随后 `register_expert.py` 刷新使 marketplace.json 条目回 0.1.30；**缓存面回滚口径随 J-1**：批 (a)＝缓存保持 0.1.30 不动（②段不动缓存，④未执行则无需回滚）；批 (b)＝同版本场景缓存是否已被覆写**未实证**→还原判据＝市场源三 version 读数回 0.1.30＋与备份目录全量哈希对账全等，缓存面现象如实呈报，禁手动向缓存目录写文件（W5＝宿主自写面）。按现象开票回修，修后重走①②。
- 还原基准注记＝备份以段②步1 实况件数（起草实测 80 件·含 `settings.json` 缺失面差集登记）为准，还原后件数＝备份件数，回执登记读数。
- 装配面 W1＝仓外预览面非真源，还原时无需回滚（留待下批重装配）。

## 七、候裁条款（票面对应钉值留白·遇此停手上报，不自行处理）

- **J-1 版本咬合候裁（本票核心留白）**：三面现值均已是 0.1.30，PROJINIT＝0.1.30 版本号之下仓面增量（零 bump 口径）；先例 4a 判据「缓存新增 `0.1.30\` 目录」无从成立，同版本再部署的转正机制**未实证**。两案供皮总裁：
  - **(a) bump 至 0.1.31 后走四段链**：全部版本钉值按 0.1.31 写死（M0 预期三读数、1c 三钉值、②步6 三读数、4a/4b 缓存判据）；0.1.31＝REMOTE-PUB 预留（不钉号）——**占用与否候裁**；bump 笔＝①段前另案微票（§五.1）。
  - **(b) 零 bump 同版本重装配**：钉值维持 0.1.30；④段判据改法与缓存行为实测形制**须候裁时定**（宿主对同版本刷新是否重建缓存未实证，转正机制可能不触发——裁时须一并给 4a 替代判据与缓存回滚口径）。
  - **票面所有版本相关钉值（1c、②步6、4a、4b）＝留白待 J-1**；J-1 未裁＝①段可依据登记件开工预核对，但版本钉值判据段不得强行执行，停手候裁。
- **J-2 获批段界候裁**：批到②止 vs 全程批到④止（＋③人类闸仍停等）——票面按先例默认写全程（0.1），以皮总最终明示为准；**段界未明示前执行席只到②收口即停**。
- 停止条款：开工读数与票面基线不符（仓面三同源读数与 J-1 裁定态不符／市场源现值≠0.1.30／批准登记缺位或措辞不含本段授权）→ 停手上报；装配纪律⑤前置不过→停手上报，禁自行清理或提交他席改动；判据 1b 件数≠81 且差集无法归因本批内容→停手呈报；注册脚本报错→如实回报，不得另路伪造标记或手改 marketplace.json；宿主缓存判据不达→停手呈报宿主侧现象，禁手动向缓存目录复制文件；段③任何形态「代跑验证」指令到达执行席→拒绝并回执登记（deploy-gate §五要点3）；同席多实例并发＝立即停手报告（席位守则）。

## 八、回执体例

- 各段收口各出回执（W6，可分件：`…-PROJINIT-DEPLOY-①装配回执-v1.md` 等），开端附开工 HEAD 读数＋批准登记读数＋J-1/J-2 裁定读数；单独 commit、`collab:` 前缀、pathspec 只含回执件、禁 `--no-verify`/amend/`git add -A`。
- **回执计数钉死**：④段收口回执**兼全链终回执**（终回执不独立成件）＝全链回执总数上限钉 **4 件**（①②③呈报登记＋④兼终）；终段内容并入④回执登记：四段各自判据读数＋版本三对账（仓面／装配面／缓存·随 J-1 裁定值）＋批准出处引用。

## 九、预算

段①≤6 步｜段②≤6 步｜段④≤3 步；写集六面闭集；仓内新写＝回执分件（≤4 件）。超出即停手上报。
