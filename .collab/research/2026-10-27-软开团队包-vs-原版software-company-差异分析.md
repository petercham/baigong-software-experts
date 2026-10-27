# hjh-software-team（我方软开专家包）vs software-company（市场原版）差异分析

> 分析日期：2026-10-27｜分析人：主理人席（实读两侧盘面，非记忆）
> 比对对象：
> - **原版**：`C:\Users\peter\.workbuddy\plugins\marketplaces\experts\plugins\software-company\`（v1.1.0，`.downloaded_at`＝2026-10-09T04:10:31Z，平台市场下载）
> - **我方**：`C:\Users\peter\.workbuddy\plugins\marketplaces\my-experts\plugins\hjh-software-team\`（v1.2.1）；真源＝`D:\multi-agent-collab-devkits\workbuddy\hjh-software-team\`（与市场源逐字一致，diff 零差）

## 一、TL;DR

我方包＝原版 fork 后经 **T-B1 lead 瘦身批** 重构的版本：四个成员 MD **逐字未动**；差异全部集中在 **lead 席位（211 行单体 → 106 行薄席）＋新增 `software-orchestration` 技能（22 行索引＋7 个 references 分件 151 行）**，即"流程细则从席位 MD 下沉到技能分件按需加载"。另新增外部顾问讨论会兼任条款与完整展示元数据。

## 二、文件树对照

| 原版（7 件） | 我方（18 件） | 状态 |
|---|---|---|
| `.codebuddy-plugin/plugin.json` | 同 | 差异见 §三 |
| `.downloaded_at` | （无·自建非下载） | — |
| `agents/software-team-lead.md`（211 行） | `agents/software-company-team-lead.md`（106 行） | **重构** |
| `agents/software-{product-manager,architect,engineer,qa-engineer}.md` | 同名四件 | **逐字相同**（diff -q 四件全同） |
| （无） | `README.md`／`avatars/.gitkeep` | 新增 |
| （无） | `skills/software-orchestration/SKILL.md`（22 行）＋`references/` 7 分件（151 行） | **新增** |

行数账：原版 agents 合计 733；我方 agents 628＋skill 173＝801。常驻加载面（席位）从 733 → 628；流程细则（151 行）改为**判档后按需读**。

## 三、lead 席位差异（核心）

**原版结构**（211 行·全部内联）：身份 → 铁律 → 路由表 → 快速模式全节 → BugFix 全节 → 标准 SOP 全节 → 增量开发 → 协作规则 7 条 → 部分工作流 → 当你收到请求 → 最终产物规范 → 重要提示。

**我方结构**（106 行）：保留身份／铁律／严禁行为／子任务命名／路由判定表；**七段流程细则替换为「⛓ 必读」指针表**（quick-mode／bugfix-path／standard-sop／incremental-dev／partial-workflows／collab-rules／delivery-summary 七分件），明写"本文件不复述细则（避免第二真源，改一处漏一处）"。

**内容增量（原版没有的）**：
1. **「🗣️ 外部顾问讨论会（主持人兼任）」节**：触发即兼任、开工先载 `external-advisor-collab` 技能、职权闭集只行使程序职责、收口即卸任回归主理人——即本项目 2026-10-26 皮总裁定的主持人职权闭集纪律已编进席位。
2. 协作规则只留 §3 质量关卡（IS_PASS／智能路由判定），§1,2,4-7 下沉 `collab-rules.md`——下沉时刻意保留判据在席、程序在件，非机械搬运。

## 四、plugin.json 元数据差异

| 项 | 原版 1.1.0 | 我方 1.2.1 |
|---|---|---|
| name | `software-company` | `hjh-software-team`（fork 改名） |
| lead agent id | `software-team-lead` | `software-company-team-lead` |
| description | "Optimized multi-agent SOP workflow for fast software delivery" | "multi-role SOP workflow for **auditable** software delivery"（定位从快→可审计） |
| skills | （无字段） | `"skills": ["./skills/software-orchestration"]` |
| 展示元数据 | 无 | 新增 displayName／profession／displayDescription／categoryId／defaultInitPrompt／tags／quickPrompts；members 字段由 `name` 改 `displayName` |

版本谱系（缓存实证）：`cache\my-experts\software-company\1.1.0`（改名 lead 文件但 211 行单体）→ `1.1.1`（218 行：加讨论会兼任节，仍单体）→ **改包名 `hjh-software-team` 1.2.1**（瘦身后 106 行）。T-B1 瘦身＝1.1.1→1.2.1 之间发生。

## 五、装配与注册状态（顺带查实）

- 我方真源在 **devkits 仓内**（`workbuddy/hjh-software-team/`·拍板五①软开 bundle 自包含不出池，无 bundle.lock 装配链）；市场源＝`my-experts\plugins\hjh-software-team\`，两者逐字一致。
- **旧安装账仍挂**：`installed_plugins.json` 里 `software-company@my-experts 1.1.1`（lastUpdated 10-26）与 `video-company@my-experts 1.0.0` 仍在册；`hjh-software-team` 无安装记录（市场清单已声明 1.2.1）。
- **本会话实际激活的是原版单体**：当前 expert 注入路径＝`marketplaces\experts\plugins\software-company`（211 行单体 lead 全文在上下文里）——即我方瘦身版**尚未在平台侧生效**。

## 六、结论与建议

1. 差异定性：**结构重构（单体→席位薄索引＋技能分件按需加载）＋ 治理注入（讨论会主持人条款）＋ 元数据补全**；四成员能力面与原版零差。
2. 瘦身动机与已拍规则一致（席位 2500 token 红线·细则下沉 references），fork 是既定治理纪律在软开 bundle 上的落地样板。
3. **待办（不擅动）**：若要让瘦身版真正在会话中生效，需平台侧安装/更新 `hjh-software-team` 1.2.1（并处置旧 `software-company@my-experts` 安装账）——与 aigc-video-team 那次重注册同族工序，等皮总示下。
