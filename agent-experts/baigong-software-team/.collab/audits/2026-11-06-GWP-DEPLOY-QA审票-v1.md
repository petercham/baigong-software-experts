# TK-GWP-DEPLOY · QA 独立审票 v1（fresh eyes·审票席＝qa-gwpdep1）

- 开工读数：`git rev-parse --short HEAD` = **d3c0071**（＝被审票面起草落盘笔，main）。审票段零执行部署动作、零改票面。
- 被审对象＝`.scratch/tickets/2026-11-06-GWP-DEPLOY-0.1.30-四段链部署票-v1.md`（d3c0071）。
- 审法＝票面引用链上事实逐条实跑核验＋deploy-gate §二/§五逐段对表＋WorkBuddy 平台面本机实测。未读产品席审件（`.collab/qa/2026-11-06-GWP-PM审票-v1.md` 仅目录列举在案，内容未读·fresh eyes 纪律）。

## 一、判定总表

**红 0 ／ 黄 3 ／ 绿 17**

| # | 项 | 判定 |
|---|---|---|
| G1 | 链上六笔 commit 实存且 message 与票面 §0.2 描述相符（`5b8936e` 四守卫脚本＝stat 恰四文件；`a67dc37` 红0黄4·17/17 绿；`bd178a9` 三同源 0.1.29→0.1.30；`0fac23c` 回执；`d3c0071` 票面；`162d7b1` 批准补录） | 绿 |
| G2 | 批准登记 §四 实读在案：措辞含「获批范围＝全程四段（批到④止）」＋「人类闸③仍须皮总真实验证…方可进④」＝票面 0.1 引文逐字吻合 | 绿 |
| G3 | 仓面三同源 grep＝`plugin.json:3`／`bundle.lock:5`／`.codebuddy-plugin/plugin.json:3` 三读数＝0.1.30，行号 L3/L5/L3 与票面 M0 声称一致 | 绿 |
| G4 | `git status --porcelain -uno`（已跟踪面）＝空，与票面 M0 声称一致；skills 组件仓 `D:\multi-agent-collab-skills` 同项亦空（publish.py 纪律⑤ 会连带校验组件仓，见 publish.py L855-868） | 绿 |
| G5 | 纪律⑤ 前置真在码内：`git_clean_or_die` 判定面＝`status --porcelain -uno`（publish.py L679）＝票面 M0 命令口径与之同形；ref 可解析前置＝`git_ref_commit_or_die`（L693 起） | 绿 |
| G6 | publish.py 缺省落点取证属实：L1209 `--out` help＝「缺省＝仓外同级 -build」逐字吻合；代码 L846-849 `out_dir = <bundle_repo>-build/<bundle 名>`；0.1.29 回执 L15 实证缺省落点＝`D:\multi-agent-collab-devkits-build\baigong-software-team` | 绿 |
| G7 | 装配面现存 0.1.29 旧装配体实测＝81 文件（含 ASSEMBLY.manifest.json＋COPY.state），manifest `bundle_version 0.1.29`／`bundle_source_commit e63c527…`＝判据 1b 基线 81 件出处实存；`COPY.state` 块计数 `grep -c '^\[sync n='`＝3（判据 1e 命令口径可跑） | 绿 |
| G8 | 81 件钉值合理性独立核：`e63c527..HEAD` 对 `agent-experts/baigong-software-team` 的 A/D/R 变更仅 `.collab/` 七笔（publish.py L730 `.collab`/`.scratch` 段不进取）；bump/GWP 均为在位文件就地改；组件 `external-advisor-collab@v1.1.3` tag 在位、skills 仓 `deep-research@v1.0.2` tag 在位——理论零增减成立，且票面≠81 停手条款兜差集 | 绿 |
| G9 | 市场源 W2 路径实存；三 version 读数实测＝根 plugin.json **0.1.29**／.codebuddy-plugin/plugin.json **0.1.29**／marketplace.json baigong 条目 **0.1.29**＝段②步1 预期三读数吻合 | 绿 |
| G10 | W5 缓存目录列实测＝`0.1.0/0.1.1/0.1.22/0.1.24/0.1.27/0.1.29` 六目录，与票面 4a 旧目录清单逐一吻合；`0.1.29\` 内 `.in_use` 标记实测在位＝4b 「同款转正实证形制」声称吻合 | 绿 |
| G11 | register_expert.py 真源在位（`…\workbuddy-builtin\skills\expert-manager\scripts\register_expert.py` 实列）；`--session-id` 参数实支持（docstring L9＋argparse 分支 L210-211；`_write_session_marker` L103-109 写 `.created-by-session`）＝票面 §6.1 取证引用吻合；空参直跑 exit 0＋usage 输出（无崩溃） | 绿 |
| G12 | 预览标记回收行为登记吻合平台已知形态：重核回执 §6.2 两度实证「即写即读在位→约 1 秒被平台回收」；票面步5「如实登记读数、不强留、不伪造」＝与该实证形态同调，未声称标记驻留 | 绿 |
| G13 | robocopy/certutil 均在位（`C:\Windows\system32\robocopy.exe`、`certutil.exe` 实测）；`MSYS_NO_PATHCONV=1 robocopy /MIR` 与 `robocopy /E` 备份形制均有 0.1.29 回执先例实证跑通 | 绿 |
| G14 | W4 备份目录命名形制与市场源备份先例吻合（backup\ 下 `market-src-baigong-0.1.22-pre-cln-20261105`／`-0.1.24-`／`-0.1.27-pre-deploy-20261105` 既往件实列在位；票面新目录 `…0.1.29-pre-deploy-20261106` 未存在＝「新建」声称吻合，W4 与 §六还原路径两处同字串＝票内自洽） | 绿 |
| G15 | 四段链条文对表：①装配（独立票＋QA 终审绿＋三件套＋幂等复跑）、②预览（先备份→MIR→register --session-id 挂卡必步）、③人类闸（代理不可代跑）、④部署（③明示通过＋明示批准双前置＋注册刷新＋缓存宿主自写）逐段与 deploy-gate §五表＋要点1/2/3/4 吻合；获批范围按段界定引用正确（批到④止≠③自动过） | 绿 |
| G16 | §六回滚条款＝deploy-gate §五要点4「备份一键回滚＋部署面保持旧版不碰」成文化；「②不动缓存→④未执行则缓存无需回滚」推理与 W5＝宿主自写面定位自洽 | 绿 |
| G17 | 起草席写集＝仅票面：`git show d3c0071` 单笔只含票面一件（起草声称零执行零落改吻合）；批准补录 `162d7b1`＝批准文件 5 行追加、是 d3c0071 祖先（≥162d7b1 声称吻合） | 绿 |
| **Y1** | **段①锚定「开工实测 HEAD ≥162d7b1」非钉死**：获批内容面＝TK-GWP 批（止于 `bd178a9`/票批 `d3c0071`）。若开工前他席向 bundle 跟踪面／agent-skills／skills 仓提交**不改件数**的内容变更（如 docs 就地修），M0 clean 读数＋1b 件数＋1c 版本三判据仍全绿，未获批内容将随锚定进装配。票面「他席先行污染真源＝停止条件」只覆盖**未提交**脏面。建议：锚定改钉值（＝批准/起草时 HEAD），或候裁条款补一句「`d3c0071..开工HEAD` 区间 bundle 跟踪面／组件面有 diff＝停手复核」。非阻断：1d 已要求 manifest 锚定 commit 读数入回执，事后可检出 | 黄 |
| **Y2** | **市场源现势已偏离 0.1.29 回执实证态**：市场源实测 **80 件**（缺 `settings.json`），而 0.1.29 回执实证同步后态＝81 件全等，装配面与缓存 `0.1.29\` 内 `settings.json` 均在位——即市场源面在 0.1.29 部署后丢过一件（何因不在本票审界）。票面段②步1 开工读数只登记三 version 未含**件数读数**；`/MIR` 同步会把 81 件拉齐（本批无害），但 §六还原以现 80 件备份为准＝还原后仍缺该件。建议：步1 增「市场源件数」基线读数并如实登记 80≠81 差集 | 黄 |
| **Y3** | **票面步5「先读 usage 确认参数形制」与脚本 stdout 实况有面差**：register_expert.py 的 usage 打印（L195-198）只列 `<expert-dir> [--marketplace-dir]`，**不含** `--session-id`（该参数在 docstring L9 与 argparse L210 实证支持）。执行席若只读 stdout usage 可能误判参数不存在。票面声称的形制 `<expert-dir> [--marketplace-dir] [--session-id]` 本身属实（本审实测吻合）。建议：步5 补注「usage 打印不含 --session-id，以脚本 docstring/argparse 为准」 | 黄 |

## 二、两必查项独立实测读数

**必查① 产品↔架构一致性（票面↔deploy-gate §五↔链上事实）**
- deploy-gate §二.1（独立部署票·禁尾注）、§二.2（呈报用户确认）、§五四段表、要点1-4、实证背景②（预览卡丢失＝丢注册步）逐条对票面：票型登记＝§二.1 ✓；批准登记 §四 直读 ✓；②段注册必步＋先例教训写死 ✓；③段代理禁跑 ✓；④段双前置＋回执附批准出处 ✓；回滚＝要点4 成文化 ✓。零断链。
- 链上事实逐条实跑：六 commit 全实（G1）；三同源 L3/L5/L3 行号实读吻合（G3）；publish.py L1209 逐字吻合（G6）；0.1.29 回执 L15 缺省落点吻合（G6）；备份先例路径实列（G14）；81 件基线实存＋零增减合理性独立核（G7/G8）。

**必查② WorkBuddy 平台兼容性（本机实测）**
- 市场源/缓存/备份/注册脚本四路径逐一 `ls` 实列吻合（G9/G10/G11/G14）；缓存六旧目录清单逐一吻合 4a（G10）。
- register_expert.py `--help` 直跑：非崩溃、exit 0 打 usage（脚本把未知参 `--help` 当 expert-dir 报不存在后回落 usage——见 G11 空参实测）；参数形态按 docstring＋argparse 实核吻合。
- `.created-by-session` 回收形态登记与重核回执 §6.2 实证吻合，票面未夸大驻留声称（G12）。
- robocopy／certutil 可执行性实测在位（G13）。

## 三、放行结论

**放行（红0·黄3）**。票面四段链与纪律真源零断链，引用链上事实全部实跑属实，平台路径与命令实测可执行——可进段①派发。三黄项均为判据完备性补强建议（Y1 锚定钉值、Y2 件数基线读数、Y3 usage 面差补注），不构成停手项；建议主理人在派工指令中随行登记 Y1/Y2 两条，避免执行席踩面差。

- 审票席写集自证：本件一件（`.collab/qa/` 下），单独 commit·`collab:` 前缀·pathspec 只含本件。
- 独立部署动作零触：本审票全程未运行 publish.py／robocopy／register_expert.py 写路径，只读取证＋`--help`/空参只读探测。
