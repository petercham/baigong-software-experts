# TK-GWP-DEPLOY ①②段回执 v1（完成回流·②收口即停）

- 回流型＝完成（四型之「完成」：段①＋段②全判据绿到②收口）。
- 票面＝`.scratch/tickets/2026-11-06-GWP-DEPLOY-0.1.30-四段链部署票-v1.md`（rev1·唯一执行依据·全文通读后照做）。
- 回执体例＝票面 §八（本件＝①②合并分段回执·W6 允许「分段回执可加后缀分件」；主理人派工指定本件名）。回执计数：本次 1 件（上限 4 内）。
- 席位＝工程师席 eng-gwpdep12（一票一新鲜实例，本票唯一实例）。

## 〇、开工读数（票面 §0.1 批准登记＋§一 M0＋QA Y1 锚定区间）

- **批准登记读数**：直读仓根 `.collab/decisions/2026-11-06-皮总拍板-GWP放行与写权移交与memory写权.md` §四——「皮总明示批准＝开 GWP-DEPLOY 四段链部署票，获批范围＝全程四段（**批到④止**）」；含④授权字样＝在案。本次仅执行①②（主理人派工明示禁进④）。
- **开工 HEAD 读数**＝`e0878cb`（`git rev-parse --short HEAD`）≥ 派工基线 `162d7b1`（`git merge-base --is-ancestor 162d7b1 HEAD` 实证成立）。装配锚定 commit＝`e0878cb`。
- **M0 复测**：仓面三同源 grep version → `plugin.json` L3／`bundle.lock` L5／`.codebuddy-plugin/plugin.json` L3 三读数＝**0.1.30** ✓；`git status --porcelain -uno`＝空 ✓。
- **锚定区间停手判据（QA Y1）**：`git diff --name-only d3c0071..HEAD` 读数＝四件——仓根 `.collab/decisions/…sources四区写权限….md`、`.scratch/tickets/…GWP-DEPLOY…票-v1.md`、包 `.collab/qa/…PM审票`、包 `.collab/qa/…QA审票`＝全部 `.collab/`／`.scratch/` 治理流水面。细判三面：
  - bundle 跟踪面（`agent-experts/baigong-software-team/` 除 `.collab/`／`.scratch/`）＝**零 diff**；
  - 本仓组件面（`agent-skills/external-advisor-collab/`）＝**零 diff**；
  - skills 仓组件面：`bundle.lock` 钉 `deep-research@v1.0.2`＝tag 指向 `730962e`＝skills 仓现势 HEAD，`git diff --name-only 'deep-research@v1.0.2'..HEAD -- skills/deep-research/`＝**零 diff**。
  - 判定＝**绿**（仅治理流水面），读数照登继续，未触发停手。

## 一、段①装配回执

**动作**：`python agent-skills/object-build/scripts/publish.py --assemble agent-experts/baigong-software-team`（**未带 `--out`**·缺省落点＝`D:\multi-agent-collab-devkits-build\baigong-software-team`）。脚本输出＝`baigong-software-team: 已装配（第 4 块，79 文件，bundle@e0878cb）`，exit 0。

| 判据 | 读数 | 判定 |
|---|---|---|
| 1a 产物三件套 | 顶层枚举见 `ASSEMBLY.manifest.json`＋`COPY.state` 两件在位；交付件计数＝79（脚本自报） | 绿 |
| 1b 件数对账 | 装配面文件总数（含两件）＝**81**＝0.1.29 基线 81（79＋manifest＋COPY.state），零增减 | 绿 |
| 1c 版本三读数 | manifest `bundle_version`＝0.1.30；装配面 `.codebuddy-plugin/plugin.json`＝0.1.30；装配面根 `plugin.json`＝0.1.30 | 绿 |
| 1d 锚定钉值 | manifest `bundle_source_commit`＝`e0878cb427c4bc6dd8967e131454834f06e67aa4`（＝开工 HEAD e0878cb 全 sha） | 绿 |
| 1e 幂等复跑 | 第二次直跑同命令：输出＝`装配面已一致（第 4 块，79 文件），零写入`；`grep -c '^\[sync n=' COPY.state` 前后两读数＝**4 = 4**；装配面 81 文件逐文件 SHA256 前后 diff＝空（字节零变化） | 绿 |

**段①收口＝五判据全绿**，进②。

## 二、段②预览回执（六步·先备份后同步序照票）

1. **开工读数**：市场源现值＝根 `plugin.json` 0.1.29／`.codebuddy-plugin/plugin.json` 0.1.29／`marketplace.json` baigong 条目 0.1.29——三读数＝0.1.29 ✓ 与票面基线相符。**市场源件数基线读数（QA Y2）**＝**80 件**（缺 `settings.json` 差集如实登记，与票面起草实测 80 件相符；追因非本票审界）。
2. **marketplace.json 部署前 SHA256**＝`46ca8b8286209cefc9bf2409ff843089f6f0efaa43fdeb465230ad64b63e7937`。
3. **备份先行（W4）**：`robocopy /E` 市场源现目录 → `C:\Users\peter\.workbuddy\backup\market-src-baigong-0.1.29-pre-deploy-20261106\`（新建·票面 W4 命名形制），robocopy exit 1（＝成功复制）。**备份件数＝80＝备份前市场源件数** ✓（备份以现 80 件实况为准，还原后亦 80 件态——票面 §六还原基准注记随动确认）。`backup\` 下其余既往目录仅列名查看，**零覆盖零删零触** ✓。
4. **同步**：`MSYS_NO_PATHCONV=1 robocopy /MIR <W1装配面> <W2市场源>`，exit 1（成功·失败计数 0）。判据全量对账非抽查：市场源 vs 装配面文件清单 diff＝**空集**（81 = 81）；逐文件 **SHA256 全量对账 81/81 全等**；robocopy 无 ERROR 行。
5. **注册挂卡（必步·未以纯复制替代）**：参数形制先读源码确认（docstring L9＋argparse L210-211 实证 `<expert-dir> [--marketplace-dir] [--session-id]`；stdout usage L195-198 不含 `--session-id`＝按票面 rev1 QA Y3 补注，usage 不作准）。命令＝
   `python C:\Users\peter\.workbuddy\plugins\marketplaces\workbuddy-builtin\skills\expert-manager\scripts\register_expert.py C:\Users\peter\.workbuddy\plugins\marketplaces\my-experts\plugins\baigong-software-team --session-id 7e588692-d914-49de-87fb-ba0b5ffa7c17`
   输出＝`Validation passed → Updated existing registration → 🎉 registered and visible`，exit 0。
   - **会话 id 取证形制登记**：主理人派工未附具体 UUID、指示「取平台现势」。实测取证＝本会话进程环境 `CODEBUDDY_MCP_CONFIG` 内 `X-WorkBuddy-MCP-Context` JWT payload 解码 → `sessionId = 7e588692-d914-49de-87fb-ba0b5ffa7c17`（`workspace = D:/multi-agent-collab-devkits` 吻合本工作区）；此值与历轮预览挂卡回执所用会话 id 同值＝同一 WorkBuddy 会话现势。旁注：同环境 `CODEBUDDY_SESSION_ID = 01a1afa1-977a-7f32-84e2-0ef0604ede5d` 系 CLI 子进程会话号非平台会话 UUID，未采用。未伪造。
   - **预览标记观测**：脚本跑毕即刻实测 `.created-by-session` 在位、内容＝`7e588692-d914-49de-87fb-ba0b5ffa7c17`（36 字节）；**+3s 复测＝GONE**＝已知平台约 1 秒回收行为（重核回执 §6.2 同态复现）。如实登记、不强留、不伪造。
6. **核验读数**：市场源根 `plugin.json`／`.codebuddy-plugin/plugin.json`／`marketplace.json` baigong 条目三 version＝**0.1.30 / 0.1.30 / 0.1.30** ✓。marketplace.json 注册后哈希＝`589638cf165c74b64c3af2fb576fe4835eaf9b47837a440d062af52c2b104779`（≠部署前哈希＝注册步生效实证）。**注册复跑幂等**：第二轮同命令 exit 0 后哈希复测＝`589638cf…` **不变** ✓。他条目登记读数：`hjh-aigc-video-team = 1.7.0`、`hjh-software-team = 1.3.3`（本票全程未对二者做任何写动作；本件对 marketplace.json 的唯一写入者＝register_expert.py 两轮）。诚实登记局限：步2 按票面仅要求哈希登记，未存部署前内容快照件，故「差异仅 baigong 条目」以「哈希变前后＋唯一写入者＝注册脚本＋他条目现值读数」三证支撑。

**②收口读数（派工要求）**：
- 市场源三处 version 读数＝**0.1.30 × 3** ✓；
- 宿主缓存 `C:\Users\peter\.workbuddy\plugins\cache\my-experts\baigong-software-team\` 只读观测＝`0.1.0 / 0.1.1 / 0.1.22 / 0.1.24 / 0.1.27 / 0.1.29` **旧六版本在位、零新增**（无 `0.1.30\`）＝**部署面未动实证** ✓。

## 三、停止声明（②收口即停）

- 本回执即「**预览已挂、候人类闸③**」呈报件。**未触段④**：未做缓存转正、未做注册刷新进④、缓存目录**零写入**（票面 §五禁动面 3＋W5 宿主自写面纪律）。
- ④派发权＝主理人持有，前置＝③皮总真实验证明示结论＋明示批准（deploy-gate §二.2／§五要点3：人类闸不可代跑）。本席候主理人对③的呈报安排。
- 段③验证要点清单五例（票面 §三）交皮总实跑用，本席未代跑。

## 四、禁动面自查（票面 §五）

1. 仓面真源零触：全程仓内已跟踪文件零改；`git status --porcelain -uno` 回执落笔前复测＝空（除本回执件）✓。
2. REMOTE-PUB 面零触 ✓。
3. 旧版本缓存目录零删零触；市场源备份既往件零触 ✓；`pre-cln-old` 等遗留面零触 ✓。
4. `marketplace.json`／`installed_plugins.json` 未手改（只经注册脚本）✓。
5. publish.py 未带 `--out`；`-build` 根面（W1 之外）零写 ✓。
6. config/hooks 零触 ✓。

## 五、写入/修改文件与仓外路径清单（本票本席全部写动作）

| 面 | 路径 | 动作 |
|---|---|---|
| W1 装配面 | `D:\multi-agent-collab-devkits-build\baigong-software-team\`（81 件） | publish.py --assemble 覆盖写（两轮·第二轮零写入） |
| W2 市场源包 | `C:\Users\peter\.workbuddy\plugins\marketplaces\my-experts\plugins\baigong-software-team\` | robocopy /MIR 同步（80→81 件·拉齐 settings.json） |
| W3 marketplace.json | `…\my-experts\.codebuddy-plugin\marketplace.json` | 仅经 register_expert.py 两轮写入（未手改） |
| W4 备份目录（新建） | `C:\Users\peter\.workbuddy\backup\market-src-baigong-0.1.29-pre-deploy-20261106\`（80 件） | robocopy /E 新建 |
| W5 宿主缓存 | `…\cache\my-experts\baigong-software-team\` | **零写入**·只读观测 |
| W6 回执件 | 本件（`agent-experts/baigong-software-team/.collab/receipts/2026-11-06-TK-GWP-DEPLOY-工程师回执-12段-v1.md`） | 新建·单独 commit·`collab:` 前缀·pathspec 只含本件 |
| 临时 | `/tmp/*.sha`、`/tmp/*.list`、`/tmp/mp_after.json`（bash 临时对账中间物） | 只读对账用·非交付物·不落仓 |

— 工程师席 eng-gwpdep12 · 2026-11-06 · 状态＝②收口·③段等待
