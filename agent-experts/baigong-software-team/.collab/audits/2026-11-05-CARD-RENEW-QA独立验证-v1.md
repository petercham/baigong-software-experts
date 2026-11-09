# CARD-RENEW QA 独立验证 v1（qa-card1·fresh eyes·证伪导向）

- 帽头开工实测 HEAD＝`5c7c4cc`（开工时读数）；核验完结时 HEAD＝`2aea4b5`。
- 被核对象＝盘上实物＋票面＋回执，工程师自报读数零采信、全部亲自复跑。
- 票面＝`.scratch/tickets/2026-11-05-CARD-RENEW-卡片换代与席位命名换代施工票.md`（完整直读）。
- 回执＝`.collab/receipts/2026-11-05-CARD-RENEW-工程师回执v1.md`（f8088fa 落笔＋2aea4b5 补录笔）。
- **被核 commit 对账呈报（红项前置申报）**：派工单所写施工 `6d1e5f2`／回执 `7ce53a5` 在本仓**不存在**（`git cat-file -t` 两笔均 `Not a valid object name`，`git log --all`／`fsck` dangling 23 笔全扫无此二哈希）。链上实物＝施工 `3c38fef`（feat: CARD-RENEW 卡片与席位命名换代 0.1.23）、回执 `f8088fa`（collab: 工程师回执v1）、回执补录 `2aea4b5`（collab: A7复跑读数补录）。三笔在 main 链、reflog 无 amend/reset。判定＝派工单读数过期/笔误，被核实物以链上三笔为准（本核验按实物执行）。
- 开工时序注记：本席核验期间工程师席仍在施工（本席前两轮快照见脏工作区 15–19 件未提交态）；终态复核时 `git status --porcelain`＝0（净树），全部判据按净树＋commit 实物读数。

## 逐项裁决（PASS/FAIL＋实测读数）

### 1. A1 旧五花名归零＝PASS
命令：`grep -roE "齐活林|许清楚|高见远|寇豆码|严过关" agent-experts/baigong-software-team/ --include="*.md" --include="*.json"`（@HEAD 2aea4b5 净树）
- 白名单外命中＝**0**；逐命中分类：仅 `README.md:61` 4 命中（v1.2.3 版本账史实行＝票面 A1 白名单样例，逐字核对为史实行本体）——豁免成立。
- 豁免面闭集性核查：全包 md/json 命中面＝README L61 一行＋`.collab/**`＋`.scratch/**`，均在票面白名单射程；无白名单外文件。
- 仓外追踪面 `git grep` 另见 `agent-skills/external-advisor-collab/.collab/research/…答疑记录…md`＝`.collab/**` 豁免射程。
- 施工前对照（本席独立读数，核验中途 HEAD 5c7c4cc 未含施工态）：两卡＋五席位卡＋五技法卷＋docs＋ARCHITECTURE 白名单外命中 50＋（逐文件 2–3 命中/件），与回执前值 55 量级一致。

### 2. A2 断言串闭集归零＝PASS
断言串＝`交付总监|Delivery Director|QA工程师|QA 工程师|QA Engineer|Software Architect|Software Engineer`，同 grep 口径白名单外命中＝**0**（含 docs/SWB-交接件排除后仍 0）。裸「架构师」「工程师」不入串照票面口径执行；「架构工程师／开发工程师／质量审计师」子串命中按 SUBSTR 三分账不判违例。施工前本席读数＝39（闭集 16 件面），回执前值 36（包根口径）量级一致。

### 3. A3 新名成对（结构式判据）＝PASS
python 解析两卡 members＋席位卡 frontmatter 逐席核验（五席全 True）：
- 注册卡 members `displayName` 恰 1／包装卡 `name`+`displayName` 双键同值／席位卡 frontmatter `zh:`＋标题行各 1：五席全对（lead/product/architect/engineer/qa）。
- profession zh/en 两卡＋席位卡成对：项目负责人/Project Lead、产品经理/Product Manager、架构工程师/Architect Engineer、开发工程师/Development Engineer、质量审计师/QA Auditor 全对。
- grep 行计数读数：注册卡 包好用2（多一处＝T1.4 defaultInitPrompt 定稿句内联，Y3 口径不判违例）/其余 1；包装卡五名各 2；席位卡各 2——与回执读数全等。
- avatar：两卡新引用各 5 计 10＝`ls avatars/` 五新 png＋team.png 在位；旧名 png 在两卡＋md 面（白名单外）残留引用＝0。

### 4. A4 三同源 0.1.23 同值＝PASS
`grep -n '"version"' bundle.lock plugin.json .codebuddy-plugin/plugin.json` → 三读数全等 `0.1.23`（bundle.lock:5／plugin.json:3／.codebuddy-plugin/plugin.json:3）；HEAD 5c7c4cc 前值三处全 `0.1.22`（`git show` 复测）。

### 5. A5 门禁实跑＝PASS（附环境口径注记）
- 主仓净树直跑：`bash agent-skills/object-audit/scripts/run-gates.sh` exit 0、`GATE PASS（发现 9015 条）`——与回执读数全等。
- 本席独立干净 worktree 对拍（`/d/qa_crn_base`@5c7c4cc／`/d/qa_crn_mid`@3c38fef／`/d/qa_crn_post`@f8088fa，与主仓同级路径保 sibling 相对引用可达）：**施工前后 4948→4948 零新增**（exit 0 GATE PASS×2）；回执笔后 4964（+16＝回执件自身案面路径指针 WATCH，非施工批）。
- 环境注记：TEMP 路径下 worktree 跑 `GATE BLOCK：check-source-of-truth exit=2`（`usage error: 包目录不存在：../multi-agent-collab-experts/workbuddy/baigong-video-team`）＝该检查器 sibling 仓相对定位随 worktree 位置失效＝环境态，非本批实物问题；同仓 /d 同级复跑即 PASS。

### 6. A6 引用闭环＝PASS
- `check-pointer-closure.py` 干净 worktree 对拍：前 @5c7c4cc＝`OA-D6-3 count=534／OA-D6-4 count=1174`；后 @3c38fef＝**534/1174 零新增**——与回执读数逐值全等。
- 新头像引用可达：两卡 `avatar` 五新引用逐指在位 png（改名 5 件 `git show --name-status -M`＝R100×5，HEAD 旧 blob 对 index 新 blob 哈希 BLOB-EQUAL×5＝图像字节零动）；team.png 两引用零动。
- 回执笔后 @f8088fa＝534/1188（+14＝回执件 13 行＋dispatch 旧档 1 行 OA-D6-4，皆 .collab 案面自引，非施工闭集面）。

### 7. A7 check-ticket-reconcile＝PASS（判据主体）＋黄项登记（残余 WATCH 漂移）
- 本票面单跑（--root . --ticket 本票）：@f8088fa＝`票 1（对账 1／SKIP 缺声明 0）｜发现 1（全 WATCH）｜exit 1`——声明闭集解析 21 件全认、缺声明 0＝判据主体绿；WATCH＝「票无回执指针行致回执解析不到」（票面 §自检节仅目录级字样，工程师无修票权不擅加，回执已如实呈报候起草席——本席核实票面确无文件名级回执指针行）。
- **漂移读数（新发现·上报）**：@当前 HEAD 2aea4b5（回执补录笔后）复跑＝`发现 2（全 WATCH）`：①「回执清单有而全部 commit name-only 全无」②「回执清单越出票面声明闭集」——两者命中面均＝回执改名节 old 位列出的五旧 png 路径（检查器把 old 列当回执清单项，对 name-only 只列 new 位的改名呈现判「越集」）。＝回执按票面 A8「old/new 双列」口径书写与检查器清单语义不匹配，全 WATCH 级·GATE 不拦；处置归起草席/主理人（回执补挂回执指针行后触发暴露）。不判施工红。
- 全仓基线：89 票面读数（对账 35／SKIP 54）＝既有族态，非本批新增。

### 8. A8 禁动面零扰动＝PASS
- `docs/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md`：`git diff 5c7c4cc..HEAD`＝0 行（零触碰）；文件 sha256 实测 `0275354f397e4bfd…495d8` 与回执登记全等；登记件内三基线哈希段本席独立段切重算（LF join）：全文 L29–260＝`3f335333e0fe…`✓／产品段 L29–84＝`7214ad14259b…`✓／架构段 L85–260＝`efb4f7658c1e…`✓——三哈希不变。
- 两卡 diff 面 agents[]/skills[]/teamInfo 零改动行（`git show 3c38fef` 抽 diff 行 grep＝空）；席位 id／席位卡文件名／`agents/software-team-*.md` 在位可核。

### 9. 对账：commit 清单≡票面声明闭集≡回执清单＝PASS
- 票面声明闭集解析（python 逐行）＝21 件；`git show --name-only 3c38fef`＝21 行；集合全等（declared−committed＝∅、committed−declared＝∅，改名件 new 位对齐，old 位在 name-status R100 行）。
- 回执文件清单 vs commit name-status old+new 全集：回执列 21 新位＋5 旧位 ⊆ commit 面，commit 面无一缺失于回执＝全等（python 对拍双向空差集）。
- f8088fa 回执笔 name-only＝恰回执 1 件（pathspec 限定自证成立）；reflog 无 amend／reset／--no-verify 痕迹（三笔逐笔在链）。

### 10. T 节逐字照录抽检＝PASS（六目全逐字）
python 提取票面定稿块 vs 盘上实文比对：
- T1.7 members 块（注册卡）JSON 结构逐字全等＝True；T2.6 members 块（包装卡，含 name+displayName 双键、lead/product/architect/qa/engineer 卡内顺序保持）＝True。
- README L3 ≡ T7.1 新句＝True；PRODUCT L8 ≡ T6.1（T7.1 全文内联）＝True；README 功能三行 ≡ T7.2＝True；README 头像节新段 ≡ T7.4 逐字＝True。
- T5 抽检读数：standard-sop L8/L15/L20/L31/L38（含「质量审计师将」定稿）/L41、quick-mode L12/L18、bugfix-path L12/L17/L20、collab-rules L10、partial-workflows L13 逐行＝票面定稿句（句尾泛指主语照口径②零动）；T6 抽检 ARCHITECTURE L15–19/L74–78、PRODUCT L10/L48–52 行首格换代行其余格零动。
- README 版本账 v0.1.23 追加行在位（L65，append-only，既有史实行未回改）。

### 11. 两卡五面同值断言＝PASS
python 独立复跑：description 全等／displayDescription 全等／tags 全等／quickPrompts 全等（6 条全保留，实删 0＝候裁⑦现案）；members 按 id 对齐五席 displayName/profession/avatar/role 全对齐（包装卡 name≡displayName）＝五席全 True。

### 12. JSON 语法＝PASS
两卡＋bundle.lock `json.load` 三件解析全过（bundle.lock 为 JSON 形态，OK）。

## 总裁决＝**放行**（红 0／黄 3／绿 12）

- 绿（12）：A1、A2、A3、A4、A5、A6、A7判据主体、A8、闭集三方对账、T 节逐字抽检、两卡五面同值、JSON 语法。
- 黄-1：派工单被核 commit 读数 `6d1e5f2`／`7ce53a5` 仓内不存在（cat-file/log --all/fsck 三扫零中）；链上实物＝`3c38fef`＋`f8088fa`＋`2aea4b5`，本核验按实物执行——主理人更正派工读数。
- 黄-2：A7 在 2aea4b5 后残余 WATCH 2 行（回执改名节 old 列被判「越集/清单多出」＝票面 old/new 双列口径 vs 检查器 name-only 语义不匹配；全 WATCH 不拦）＋票面无回执文件名级指针行（回执已呈报候起草席）——处置归起草席/主理人，非施工面。
- 黄-3：回执笔/补录笔自身引入 pointer-closure +14 与 reconcile WATCH 计数漂移（A6 534/1174→534/1188、GATE 4948→4964）＝.collab 案面自引族态；**施工批 3c38fef 本体零新增实锤**（两值 534/1174 与 GATE 4948 前后逐值全等）。
- 观察（不判色）：run-gates 在 TEMP 路径 worktree 因 check-source-of-truth sibling 相对定位 GATE BLOCK＝环境态；②预览段候裁⑦宿主 5 槽实测、候裁⑥图像画面文字错位＝留传导链后续段，非本批射程。

——qa-card1·fresh eyes·全部读数本席亲跑（grep/python/git 原文命令见各节）

- F11 过程痕迹终式自检（终式实体在票面 §自检与回执节）：本件实测读数＝0＝零过程痕迹命中（登记行本体不含终式字面，无自指）。

## 附·主理人更正令核入（append 补录·HEAD 复跑读数）

主理人更正令（本席收件）三项核入：

1. **被核 commit 实号更正确认**：派工书 6d1e5f2/7ce53a5 系占位失实作废——本席核验自始按链上实物 `3c38fef`（施工）＋`f8088fa`（回执）＋补录笔执行（黄-1 即此，方向一致）。三方对账已按实号完成：`git show --name-only 3c38fef`＝21 件与票面声明闭集全等（python 双向差集空，见 §9）。
2. **回执落点差异＝主理人追认 `.collab/receipts/` 为合法真惯例**：本席原按落位合法处理＋差异如实登记（回执 §五-1 亦自申报），与本令一致——落点项不判违例，结案。
3. **A7 残余 WATCH 处置销账**：起草席已在链补挂（`6272e63` 票面文件名级回执指针行＋回执落点更正登记、`916bb49` 改名件 old 侧标注修单）。本席最新 HEAD `9815870` 复跑：`check-ticket-reconcile --root . --ticket 本票` ＝ **`票 1（对账 1／SKIP 缺声明 0）｜发现 0｜exit 0`**——原黄-2 两 WATCH 全销，A7 转全绿。

**修订后计数：红 0／黄 2／绿 13**（A7 由「判据主体绿＋黄尾」升全绿）。总裁决不变＝放行。黄余两项＝黄-1（派工读数失实，已由主理人更正令自证销因，留登记）、黄-3（回执笔自引 closure +14 族态，施工本体零新增实锤不变）。
