# multi-agent-collab-devkits · 多 Agent 协作开发工具包仓

> 归属：皮总（决策者）· 建包：2026-10-22 · 维护：本包独立于 creative_skyline，不与其互写。
> 沿革：2026-10-26 拆仓（原 multi-agent-collab-skillpack·拍板三）→ 同日升格 **devkits 开发工具包仓**（拍板四 G-1／拍板五①／拍板六⑥）。本仓＝各维度**整合打包的可用开发工具**，内部豁免正交切分（拍板五①）。2026-11-03/04 仓目录重整 B 批（B1–B5）：交付面与过程域案卷迁入**三分类项目壳**（`agent-experts/`、`agent-skills/`、`softwares/`），旧 `deliverables/`、仓根 `docs/` 树退役清灭（本 README＝SWB-B5 重写笔）。
> 姊妹仓：`../multi-agent-collab-experts`（video bundle＝定义＋角色＋图＋索引）；`../multi-agent-collab-skills`（被开发对象业务技能真源·video 五域）。三仓并列同一父目录为运行前提。
> 远端：https://github.com/petercham/multi-agent-collab-devkits （private·待建）；旧远端 https://github.com/petercham/multi-agent-collab-skillpack 保留作归档（tag `v0.1.0`）。
> knowledge 独立领域边界已登记（G-5·K2·拍板六①）：内容出生时按出池条件建仓，本轮不建。

## 一、仓性质与运行前提

本仓＝多 Agent 协作**开发工具包仓**：协作技能、专家包、门禁工具（`tools/`）、治理史实锚同仓。仓根入库面白名单＝下表；其余顶层目录出现＝违例（门禁断言见 SWB-B5 回执判据 1）。

## 二、仓根白名单结构表（B 批终态）

| 路径 | 性质 | 进 git | 说明 |
|---|---|---|---|
| `README.md` | 仓根索引 | ✅ | 本件（根只放 README·薄写不复写正文） |
| `agent-experts/` | 分类目录①：专家包项目 | ✅ | 项目壳＝交付面＋`docs/`＋`.collab/`案卷＋`.scratch/tickets/`票面 |
| `agent-skills/` | 分类目录②：独立技能项目 | ✅ | 同上结构 |
| `softwares/` | 分类目录③：软件工程项 | ✅ | 空名录·届时按票入册 |
| `tools/` | 仓级门禁/工具脚本 | ✅ | 跨项目通用件（check-source-of-truth、check-truename 等）；项目级门禁脚本住各项目 `scripts/` |
| `.scratch/tickets/`（各项目内） | 票面落位 | ✅ | 票面真源落位（皮总裁定·票面落 scratch）；仓根 `.scratch/tickets/` 仅存 B 批过渡票（退役候裁见 B 批收口登记） |
| 各项目 `.collab/{decisions,qa,receipts,board,research,design}/` | 史实锚案卷 | ✅ | 判词/裁决/回执/核验/研究/设计稿·append-only |
| 各项目 `docs/` | 项目级规范/活文档 | ✅ | STRUCTURE/PRODUCT/ARCHITECTURE 等 |
| `.collab/{refs,evidence,inbox,process,dispatch,backup}/`＋`tmp-*.txt` | 过程流水/证据/运行时 | ❌（gitignore） | 仓根层级另含过渡留置面：`evidence/gates/`（run-gates 出口②现仍写仓根·过渡态在册）＋`inbox/主理人/`（出口③） |
| `.collab/research/`（仓根） | era 留置面 | ⚠️ 暂存 | era 跨仓移交面（ESC1 域·待移交）＋外部快照三桶 ignore 态（见四节注） |
| `.workbuddy/`、`__pycache__/`、系统杂物 | 会话/编译产物 | ❌（gitignore） | 可弃 |

**分区判据**（一句话）：这份东西是拿来**照着做**的（交付面/docs，审），还是拿来**查当时发生了什么**的（案卷，记），还是**用完可弃**的（process/evidence/inbox，不入库）。入库面/排除面两制条款真源＝`.gitignore`（SWB-B5 重写笔·新旧映射表在 B5 回执）。

## 三、项目名录（七项目·闭集）

名录闭集真源＝各分类目录 README＋SWB-B1 票面声明；本表为汇总视图。

| 分类 | 项目 id | 一句话 | 版本线 |
|---|---|---|---|
| agent-experts | `baigong-software-team` | 百工软件团队专家包（五席 SOP 驱动·账本为真相·租约写门·机检门禁） | v0.1.18（plugin.json＋bundle.lock＋.codebuddy-plugin 三同源·纪律①每变必 bump） |
| agent-skills | `multi-collab` | 协作纪律（权限分级版：唯一写权＋开放读权席位＋md 交接件机制） | v4.10 |
| agent-skills | `object-audit` | 对象审计总入口（骨架＋对象判据分件＋仓级门禁脚本族） | v0.8 |
| agent-skills | `object-build` | 对象构建总入口（三问＋六步＋分件：skill/装订/角色/票/文档/发布） | v0.6 |
| agent-skills | `bundle-assembly-registration` | 专家包装配＋注册工序（T 步骤型·运行时挂载·不持发布器能力） | v0.1 |
| agent-skills | `external-advisor-collab` | 外部顾问讨论会治理（席位职权闭集·轮次程序·决议规则） | v1.1.1 |
| agent-skills | `fuxi-skill` | 伏羲 perspective-pack-builder（人格/技法双轨蒸馏工具链·产物住本包 `products/`） | 批受控（S4 定稿·包 README 随批版本号递增） |

（`softwares/`＝空名录·届时再入。新项目按票追加。）

### 交付对象历史索引（并入自旧 `deliverables/README.md`·B2 回执登记待并入行·`git show 91eb86f^:deliverables/README.md` 取证）

旧 `deliverables/skills/` 表五行（对象现址＝`agent-skills/<id>/`·版本·状态沿革）：

| 对象目录（旧址→新址） | 内容 | 版本·状态 |
|---|---|---|
| `skills/object-audit/` → `agent-skills/object-audit/` | 对象审计总入口（骨架＋对象判据分件·含 `70-provenance.md`/`60-gates.md` 系） | v0.8 · 活跃（裁-21/23/25 豁免链、批 29 五类子包适配沿革见其 `90-changelog`） |
| `skills/object-build/` → `agent-skills/object-build/` | 对象构建总入口（三问＋六步＋6 分件） | v0.5 · 草稿（`copy:` 变量式＋publish.py prune 白名单沿革） |
| `skills/bundle-assembly-registration/` → `agent-skills/bundle-assembly-registration/` | 专家包装配＋注册工序（指针式不持发布器能力） | v0.1 · 草稿（注册执行体待定·候补触发＝实际重注册时） |
| `skills/fuxi-skill/` → `agent-skills/fuxi-skill/` | 伏羲蒸馏技能（结构层门禁骨架＋L0 共享内核＋products 池） | 草稿→S4 定稿批受控（DIRRELOC-C2 产物内迁本包 `products/`） |
| `skills/multi-collab/` → `agent-skills/multi-collab/` | 协作纪律（权限分级版） | v4.10 · 活跃（v3.3→v4.10 沿革见 `90-changelog.md`） |

（注：B2 回执待并入行记「skills 表 6 行」；旧 README 实测数据行＝5（表头另计）＋独立 `external-advisor-collab` 当时未列旧表（其出生即在新树 EAC-SK 批）＝现名录 6 技能项目。读数差登记回执。）

旧 `deliverables/experts/` 表两行：

| 对象 | 真源 | 版本·状态 |
|---|---|---|
| baigong-software-team | 本仓 `agent-experts/baigong-software-team/`（软开 bundle·生产力工具·拍板五①豁免出池·2026-11-01 ㊽ 回迁收口→B2 入壳） | v0.1.18 · 活跃（「改定义只改仓内真源、部署面只准从仓内复制」不变；bundle.lock 与包内 plugin.json 同源） |
| baigong-video-team | bundle＝`../multi-agent-collab-experts/workbuddy/baigong-video-team/`（业务专家 bundle 住姊妹仓·指针只指不搬）；五域技能真源＝`../multi-agent-collab-skills/skills/` | v2.0.0 · 活跃（沿革全文见该包 `README.md`；拆仓前历史留本仓 git 史） |

**已退役（2026-10-22·决策者拍·三技能合并）**：`plan-tickets`、`ticket-flow`——有效内容全部并入 `object-build/references/40-ticket.md`；原件按 `SKILL.md.retired` 先例改名归档（史实锚保留）。上游 `to-tickets`（matt pocock）**不碰**，仅作只读参照系与细则指针。

**已撤包（2026-10-23·裁-38 概念纠偏）**：`video-team/`——专家团误做成 skill 形态，本体只认专家包轨 aigc-video-team；git 史 b2933cc/c2931d5 留痕。

**未迁入（留用户级 skill 库·是否迁入待拍）**：doc-governance、skill-contract-audit、identity-governance。判据见 `agent-experts/baigong-software-team/.collab/decisions/2026-10-22-裁决记录.md` 候办第 5 条；迁入时须同步处理原件指向，避免双真源。其中 identity-governance 系交接核验补登的**暗依赖**——`agent-skills/multi-collab/SKILL.md` 与 `references/50-antipatterns.md` 两处活指针指向它。

## 四、跨项目案卷索引（只指不搬）

口径（B0 前主理人口径）：**跨项目案卷按参与项目归档，本索引只指不搬**。归桶真源＝各项目 `.collab/<桶>/`；下表为逐名指针（源＝SWB-B3 回执 §三/§七表·B3c2 `4a73f3e`）。

### decisions（判词/裁决/呈拍·append-only）

归项目归档实测：百工 `agent-experts/baigong-software-team/.collab/decisions/`＝**16 件**（2026-10-22 裁决记录／2026-10-25·10-26·10-28·11-01·11-02 皮总拍板／11-02 主理人裁定-MERGEV12-TKT39候裁／11-03 皮总裁定×8（ADR正件落位docs·SWB票包遗留三件·写侧硬拦与签名裁撤与外连接备忘·工程师写域规范与仓根项目子包分层·票面落位scratch与T07T08R放行·迁移重整禁用誊写方式·项目级docs与collab分层子包·项目自由分层与collab固定结构及docs约定md）／verdicts.md）；其余六项目＝0 件。仓根 `.collab/decisions/`＝**2 件**（2026-11-04 皮总裁定-主理人永不并发派席／并发口径修正-禁同席多实例·B4 期新落·归置候登记面裁）。

### research（判词依据/研究底稿）

归项目实测：百工 202／external-advisor-collab 13／fuxi-skill 7／其余 0。仓根 `.collab/research/`＝**era 留置面 26 件＝待移交 experts 仓（ESC1·票面 `.scratch/tickets/2026-11-03-SWB-ESC1-era-cross-repo-handover-micro-ticket.md`）**——明细＝B3 回执 §七 era 移交清单（第三方外部快照 24＋自产审计 1＋外部参照 1；其中外部快照三桶 `reference-2026-10-24/{video-teams,official-cos,summoned-2026-10-24}/`＝ignore 态不入版本库·出处索引件 REFERENCE-SOURCES.md 入库＝「外部参照件不入我仓版本库」既有裁决承接）。era 族留置（research 外）：仓根 `dispatch/` 派工书 3＋`evidence/` 施工回执 1＝ESC1 并入消费。

### qa / receipts / board / design / tickets

qa＝百工 143＋eac 2＋fuxi 22＋仓根 3（QA-B3/B4 独立验证·B4 期新落·归置候裁）；receipts＝百工 74＋fuxi 6；board＝百工 1；design＝百工 15＋fuxi 9；票面＝百工 `.scratch/tickets/` 53＋eac 11＋fuxi 21＋仓根 `.scratch/tickets/` B 批过渡票 12（B1–B5＋ESC1＋README·退役候裁＝B 批收口后按 ES 退役程序·主理人裁）。仓根散件登记：`.collab/2026-11-03-SWB-B3-收口登记-v1.md`、`.collab/2026-11-04-SWB-B4-收口登记-v1.md`（登记人＝主理人·归置候裁）。

## 五、治理约定（自旧 README 六节随迁移分账）

1. **单写者**：本仓 git 写操作由唯一执行通道完成；审计/研究席永无写盘权——现行有效·机检真源＝百工 `config/seat-permissions.json`＋hooks 面（T08R 机械化）。
2. **decisions 只增不改**：append-only，勘误＝原文后注——现行有效·语义见 `agent-skills/multi-collab/`（协作纪律真源）。
3. **命名**：目录与文件名 ASCII 小写 kebab-case；文档正文中文自由——现行有效·定标真源＝ES 工程规范定标（`agent-experts/baigong-software-team/.collab/receipts/2026-11-03-ES-工程规范定标-终态收口登记-v1.md`）。
4. **索引路由**：每一级子包根只放 README.md（边界一句话＋索引·薄写不复写正文）——现行有效·真源＝doc-governance D5-3（用户级 skill 库·未迁入面见三节注）。
5. **skill 形态约束**：入口少、分件多、分件平铺一层不嵌套（官方 spec "one level deep"）——现行有效·研究依据留项目 research 桶指针。
6. **引证纪律**：七类引证失效扫描——真源＝`agent-skills/object-audit/references/00-skeleton.md`（指针不复写）。

## 六、本包的两个设计决定（出处＝`agent-experts/baigong-software-team/.collab/decisions/2026-10-22-裁决记录.md`）

- **不按对象拆 skill**——业界无先例（Parnas 1972／ISO 9001 §0.1／buf／ESLint 生态），判据＝「边界是否等于加载边界」。
- **`.collab` 按性质分区不按 actor**——`.` 前缀不表达 git 归属；decisions 进 git 是 ADR 惯例（决策记录必须可追溯）。
