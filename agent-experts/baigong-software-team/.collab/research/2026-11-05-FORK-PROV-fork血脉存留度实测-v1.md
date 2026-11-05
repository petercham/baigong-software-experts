# FORK-PROV · fork 血脉存留度实测 v1

> 开端 HEAD 读数：`32acce31c28b7aa0d999178a23340f7405d90202`（main·2026-11-05）
> 研究席：research-fork1｜性质：只读取证实测（零改任何仓内文件，除本报告落盘）
> 委托问题：皮总主张「百工已是推倒性重构，fork 信息不该留」——实测该主张的证据基础。
> 比对基线实物＝`C:/Users/peter/.workbuddy/backup/market-src-hjh-software-team-1.2.1-20261028/`（fork v1.2.x 时代完整包备份，下称 **fork-1.2.1 备份**）

## 一、fork 基线实物在位性（实测）

| 实物 | 路径 | 版本读数 | 状态 |
|---|---|---|---|
| 官方市场原版 | `C:/Users/peter/.workbuddy/plugins/cache/experts/software-company/1.1.0/` | plugin.json name=`software-company` version=**1.1.0**；lead 文件名仍为 `software-team-lead.md`（11,486 B，211 行单体形态） | 在位（市场轨缓存） |
| fork 早期账 | `C:/Users/peter/.workbuddy/plugins/cache/my-experts/software-company/1.1.0/` | version=1.1.0，lead 已改名为 `software-company-team-lead.md` | 在位（旧安装账缓存，1.1.1 已于 10-28 卸载） |
| 卸载备份（1.1.1 完整包） | `C:/Users/peter/.workbuddy/backup/uninstall-software-company-1.1.1-20261028/` 内 `cache-1.1.1\` 与 `cache-1.1.1-moved\` 两份 | plugin.json version=**1.1.1**；两份 team-lead MD md5 全等（`f5e0cae8…`）；lead 219 行单体（含讨论会兼任节，无 references 下沉） | 在位 |
| fork 改名后市场源备份 | `C:/Users/peter/.workbuddy/backup/market-src-hjh-software-team-1.2.1-20261028/` | plugin.json name=`hjh-software-team` version=**1.2.1**；lead 106 行瘦身态＋`skills/software-orchestration/references/` 七件在位 | 在位（本报告存留度比对基线） |
| 同上 1.3.2 | `C:/Users/peter/.workbuddy/backup/market-src-hjh-software-team-1.3.2-20261028/` | version=1.3.2；lead MD 与七件 references 对 1.2.1 行尾归一后 **逐字节全等**（diff 空） | 在位 |
| 运行缓存多版 | `C:/Users/peter/.workbuddy/plugins/cache/my-experts/hjh-software-team/{1.2.1,1.3.0,1.3.1,1.3.2,1.3.3}/` | 各 plugin.json 版本同名 | 在位 |

结论一：fork 血脉实物链完整可得（1.1.0 官方原版 → 1.1.1 卸载备份 → 1.2.1/1.3.2 改名后市场源备份 → 缓存多版），任何时点的「与上游人工 diff 对账」都有盘面实物支撑，不存在「基线已不可得所以出身账失效」的前提。

## 二、七段条款存留度（现文 vs fork-1.2.1 备份 references 逐行 difflib＋细读）

比对方法：行尾归一后 `difflib.SequenceMatcher` 行级相似度＋unified diff 逐段细读。现文＝`agent-experts/baigong-software-team/skills/software-orchestration/references/`。

| 段 | fork 行数 | 现文行数 | 相似度 | 差异构成（实测 diff） | 定性 |
|---|---|---|---|---|---|
| quick-mode.md | 30 | 32 | 0.871 | 头注 commit 账目措辞改写＋新增「退役声明（v2.9 §20.1⑦）」＋席位名换代 2 行（工程师→开发工程师、寇豆码→柯会码） | 部分改写（骨架逐字存续） |
| standard-sop.md | 45 | 78 | 0.618 | 席位名换代 6 行＋过渡口径注记 2 行＋步骤3 对照样本对账表条款 1 行＋步骤5 核对行 1 行＋**新增「ADR 工序」整节 26 行** | 部分改写＋大量追加（旧五步骨架仍逐字存续，新增内容约占 1/3） |
| bugfix-path.md | 21 | 23 | 0.773 | 头注＋退役声明＋席位名换代 3 行 | 部分改写（骨架逐字存续） |
| collab-rules.md | 16 | 16 | 0.875 | 头注 commit 措辞＋1 行席位名（QA工程师→质量审计师） | 近逐字 |
| incremental-dev.md | 13 | 13 | 0.923 | 仅头注 commit 措辞一行 | **逐字存续**（正文零改） |
| partial-workflows.md | 15 | 15 | 0.867 | 头注＋1 行席位名 | 近逐字 |
| delivery-summary.md | 18 | 18 | 0.944 | 仅头注 commit 措辞一行 | **逐字存续**（正文零改；L17 `deliverables/software-company/` 旧路径已由 SCFIX 票裁改 docs/、尚未落盘） |

头注「逐字下沉」声称是否失实：**不失实**。七段现文与 fork-1.2.1 备份（即头注所指「fork v1.2.0」下沉时点态）比对，无一例整体重写；改写形态只有三类——①头注自身 commit 账目措辞（CLN-PURE 批 a885ad7）；②CARD-RENEW 席位花名/职业名换代带来的称谓替换（3c38fef）；③SWB v2.9 收编批（27caad3）与 SOP-B1（1aa014f）、ADR-L0（878746d）带来的叠加条款（退役声明/过渡口径注记/对账表条款/ADR 节），叠加处旧条款明文保留为「技法面」。git log --follow 实测七件的全部历史改动批＝搬家（git mv）、改名、头注措辞、上述叠加，无任何「整体替换内容」批。

结论二：「推倒性重构」主张与盘面不符——7/7 段仍以 fork 文本为主体骨架，其中 2 段正文 100% 逐字存续、4 段近逐字、仅 standard-sop 一段有大量追加但旧骨架仍在。fork 血脉＝当前活内容来源，非历史装饰。

## 三、出身账溯源用途实证＋机检依赖

### 3.1 「与上游人工 diff 对账」的实际执行记录（存在，1 例完整）

- `agent-experts/baigong-software-team/.collab/research/2026-10-27-软开团队包-vs-原版software-company-差异分析.md`——2026-10-27 主理人席实读两侧盘面的上游对账件：四成员 MD 逐字同（diff -q 全同）、lead 211→106 重构账、plugin.json 元数据差异表、版本谱系缓存实证（1.1.0→1.1.1→1.2.1）。该文同时查实了当时的部署错位（会话激活的仍是原版单体 lead）——即出身账指引的「需要时人工 diff 对账」在 10-27 实际发生过并产生了运维决策输入。
- 旁证：`.workbuddy/memory/2026-10-27.md:85` 登记该件落盘；`.workbuddy/memory/2026-10-28.md` §十三 记 1.1.1 旧安装账处置（10-28 卸载＋备份，即第一表实物链的由来）。
- 除此之外，`.collab/` 全域 grep（上游对账/upstream/fork diff/与上游/原版对账）再无第二次对账动作记录——使用频率低，但**非零**，且那一次正是靠出身账指向的缓存实物完成。

### 3.2 机检面消费实测（删除出身账行会不会红）

- `tools/check-source-of-truth.py`：grep `software-company` **零命中**。其 A2 指针探针对反引号 `.md` 路径只查含 `/` 者（裸基名只 WATCH 不 BLOCK，L588-590）；出身账与头注中的 `software-company`／`software-company-team-lead.md` 均为裸基名或包名字样，不在 BLOCK 面。删这些行只会减 WATCH 计数，不会红。
- `tools/baseline-sot-dup.json`：items 内 `software-company` **零命中**（含 files 键）。
- `tools/baseline-seat-decl.json:11`：存在旧键 `"softdev:agents/software-company-team-lead.md"`——该文件已物理清退（SWB-T07），此键为悬空旧快照键，扫描时不命中即闲置，删出身账行不影响它；它本身随 `--regen-seat-baseline` 自动清。
- `bundle.lock`／`plugin.json`／`settings.json`／`tests/`：`software-company` 全部零命中。
- `agent-skills/`、`tools/publish.py`：零命中。
- 唯一被机检活消费的旧名＝`config/seat-permissions-hooks-map.json:33` `agent_type_to_seat` 旧键组（write-guard.py L201/L311 消费）——此为身份映射活条款非出身账，且已由 SCFIX 票（HEAD 32acce3 落册）裁删除，待施工。

结论三：机检对出身账字段**零依赖**（删 README L24/L27/ARCHITECTURE L178/PRODUCT L12 不会红）；但「人工 diff 对账」路径的溯源功能有一例实证，且实物链在位使该功能随时可复用。

## 四、旧引用面全量清单（真源＋装配逻辑，排除 .collab/.scratch/宿主 memory 过程域）

| # | 命中 | 定性 |
|---|---|---|
| 1 | `README.md:24` 基线＝市场包 `software-company` v1.1.0 句 | 出身账句 |
| 2 | `README.md:27` fork 改动清单② lead 改名句 | 出身账句 |
| 3 | `README.md:46` 版本账 v0.1.15 旧五席位卡清退行 | 版本账史述（append-only 在册） |
| 4 | `README.md:60` 版本账 v1.2.0 包 id 更名行 | 版本账史述（前血脉沿革） |
| 5 | `README.md:86` token 计数表 `software-company-team-lead.md` 行 | 过期史实快照（该文件已清退；表头注明「lead 瘦身批后」口径，属历史读数非活条款） |
| 6 | `config/seat-permissions-hooks-map.json:33` `software-company-team-lead`→host | 活条款（旧席型兼容键·SCFIX 已裁删除、待施工） |
| 7–13 | 七件 references L3 头注「本件承载 `software-company-team-lead.md`（fork v1.2.0）逐字下沉件」（quick-mode/standard-sop/bugfix-path/collab-rules/incremental-dev/partial-workflows/delivery-summary 各一处） | 出处头注（经实测声称属实，非失实） |
| 14 | `references/delivery-summary.md:17` `deliverables/software-company/<项目>-delivery-<date>.md` | 活条款（旧团名路径·SCFIX T1 已裁改 `docs/delivery-…`，待施工） |
| 15 | `docs/ARCHITECTURE.md:178` 出身账第4款（fork 基线照录＋人工 diff 对账指引） | 出身账句 |
| 16 | `docs/PRODUCT.md:12` 出身背景句 | 出身账句 |
| 17 | `docs/SWB-交接件v2.9-…-2026-11-03.md:15` 随批轻注③「停跑①（旧 software-company 本体）已退场」 | 登记件史述句 |
| 18 | `tools/baseline-seat-decl.json:11` 旧席位键 | 机检基线快照悬空旧键（随 regen 自清） |
| 19 | `.gitignore` | 无 software-company 命中（实测） |

## 五、结论：「推倒性重构」主张的事实基础成立度

**不成立（三测两点推翻）**：

1. 内容面：七段 7/7 未整体重写——incremental-dev、delivery-summary 正文逐字存续，collab-rules、partial-workflows 仅一行席位名改动，quick-mode、bugfix-path 骨架逐字＋叠加退役声明，standard-sop 旧五步骨架逐字存续＋叠加约 1/3 新条款。百工的「重构」是**在 fork 骨架上叠加治理层**（纪律卷、门禁、ADR 工序、SWB 口径注记），非替换 fork 文本。头注「逐字下沉」声称经 v1.2.1 备份比对**属实**。
2. 溯源面：出身账指引的「人工 diff 对账」有 2026-10-27 一次完整执行实证（差异分析件在盘），实物链（1.1.0 缓存＋1.1.1 卸载备份＋1.2.x 市场源备份）全部在位可复用。
3. 唯一支持清理主张的实测点是**机检零依赖**（删出身账行不红）——但「不红」只说明删除无机检代价，不构成删除理由。

**处置建议（与 HEAD 在途 SCFIX 票口径对表）**：SCFIX 票（32acce3 落册）已把引用面三分：两处活条款残留（#6 hooks-map 旧键、#14 delivery-summary 旧路径）裁改，四处出处/出身（#7-13 头注、#15 ARCHITECTURE L178、#16 PRODUCT L12 及 #1/#2 README 出身段）按「事实不可变」在册留置。本实测支持该裁定：留置四处有溯源功能实证支撑，头注不失实无需改写。**若决策者仍要脱敏**（不点旧包名），最小方案＝七件头注改「本件承载本包 v1.2.x 时代 lead 席位 MD（`software-team-lead` 席）对应节下沉件」＋ARCHITECTURE L178/PRODUCT L12 改「基线＝官方市场某软件团队包（脱敏）」——但此代价＝切断 diff 对账锚点（改后再要对账需先考据旧包名），且 #5 README token 表旧文件名与版本账史述行（append-only）仍不可净零，脱敏收益不抵溯源损失。**不建议脱敏。**

另登记两实测副产品：①`tools/baseline-seat-decl.json:11` 悬空旧键（SWB-T07 后未 regen）；②README L86 token 表整表为旧五席历史快照（现 agents/ 已是 software-team-* 五件），属版本账口径内史实但如后续引用需注明快照时点。
