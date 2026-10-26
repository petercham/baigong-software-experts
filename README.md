# multi-agent-collab-devkits · 多 Agent 协作开发工具包仓

> 归属：皮总（决策者）· 建包：2026-10-22 · 维护：本包独立于 creative_skyline，不与其互写。
> 沿革：2026-10-26 拆仓（原 multi-agent-collab-skillpack·拍板三）→ 同日升格 **devkits 开发工具包仓**（拍板四 G-1／拍板五①／拍板六⑥·目录改名候皮总侧关会话执行）。本仓＝各维度**整合打包的可用开发工具**，内部豁免正交切分（拍板五①）。
> 姊妹仓：`../multi-agent-collab-experts`（video bundle＝定义＋角色＋图＋索引）；`../multi-agent-collab-skills`（被开发对象业务技能真源·video 五域）。三仓并列同一父目录为运行前提。
> 远端：https://github.com/petercham/multi-agent-collab-devkits （private·待建）；旧远端 https://github.com/petercham/multi-agent-collab-skillpack 保留作归档（tag `v0.1.0`）。
> knowledge 独立领域边界已登记（G-5·K2·拍板六①）：内容出生时按出池条件建仓，本轮不建。

## 目录结构（三层·按性质分区）

| 目录 | 性质 | 进 git | 说明 |
|---|---|---|---|
| `deliverables/{对象名}/` | **交付件** | ✅ | 每个对象一个目录：本仓只放 skill 包（`deliverables/skills/` 五域）；专家包已迁出至姊妹仓（指针登记在 deliverables/README） |
| `docs/` | **规范文档** | ✅ | **根只放 README.md**，正文住子包：`research/`（研究底稿）、`process/`（过程记录） |
| `.collab/decisions/` | **治理史实锚** | ✅ | 判词、裁决、呈拍记录——append-only，只增不改 |
| `.collab/process/` | 过程流水 | ❌（gitignore） | 会话日志、工具输出、临时产物 |
| `.collab/inbox/` | 席间消息 | ❌（gitignore） | 多 Agent 消息总线，actor 在末级目录 |

**分区判据**（一句话）：这份东西是拿来**照着做**的（deliverables/docs，审），还是拿来**查当时发生了什么**的（decisions，记），还是**用完可弃**的（process/inbox，不入库）。

## deliverables 现状

见 [`deliverables/README.md`](deliverables/README.md)（对象清单真源在索引，本处不复写——指针只指不搬）。

## 治理约定（本包自指）

1. **单写者**：本包所有 git 写操作由唯一执行通道完成；审计/研究席永无写盘权。
2. **decisions 只增不改**：判词与裁决落 `.collab/decisions/`，append-only；勘误＝原文后注。
3. **命名**：目录与文件名 ASCII 小写 kebab-case；文档正文中文自由。
4. **索引路由**：每个一级子包（`docs/`、`deliverables/`）的**根只放一份 README.md**（＝该包边界一句话＋索引，薄写不复写正文），正文一律住子包并在索引登记一行；根目录出现正文＝违例（判据同 doc-governance D5-3）。子包根用 README.md 不用 INDEX.md——GitHub 目录级自动渲染、MkDocs/Docusaurus 认它、Google 风格指南明文「每个顶层包目录应有 README.md」；INDEX.md 零工具支持（依据见 docs/research/R6）。
5. **skill 形态约束**（源自研究裁决，见 docs/research/）：入口少、分件多、**分件平铺一层不嵌套**（官方 spec "one level deep"）。
6. **引证纪律**：七类引证失效扫描（强词法/弱词法/URL 反查可机检），见 `deliverables/object-audit/references/00-skeleton.md`。

## 本包的两个设计决定（出处见 .collab/decisions/2026-10-22-裁决记录.md）

- **不按对象拆 skill**——业界无先例（Parnas 1972／ISO 9001 §0.1／buf／ESLint 生态），判据＝「边界是否等于加载边界」。
- **`.collab` 按性质分区不按 actor**——`.` 前缀不表达 git 归属；decisions 进 git 是 ADR 惯例（决策记录必须可追溯）。
