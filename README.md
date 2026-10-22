# multi-agent-collab-skillpack · 多 Agent 协作开发技能包

> 归属：皮总（决策者）· 建包：2026-10-22 · 维护：本包独立于 creative_skyline，不与其互写。
> 本包是「多 Agent 协作开发」方法论的**交付件仓库**：skill 包、专家定义、治理裁决与研究底稿。

## 目录结构（三层·按性质分区）

| 目录 | 性质 | 进 git | 说明 |
|---|---|---|---|
| `deliverables/{对象名}/` | **交付件** | ✅ | 每个对象一个目录：skill 包、专家包等最终交付物 |
| `docs/` | **规范文档** | ✅ | 方法论说明、研究底稿（research/） |
| `.collab/decisions/` | **治理史实锚** | ✅ | 判词、裁决、呈拍记录——append-only，只增不改 |
| `.collab/process/` | 过程流水 | ❌（gitignore） | 会话日志、工具输出、临时产物 |
| `.collab/inbox/` | 席间消息 | ❌（gitignore） | 多 Agent 消息总线，actor 在末级目录 |

**分区判据**（一句话）：这份东西是拿来**照着做**的（deliverables/docs，审），还是拿来**查当时发生了什么**的（decisions，记），还是**用完可弃**的（process/inbox，不入库）。

## deliverables 现状

| 对象目录 | 内容 | 状态 |
|---|---|---|
| `object-audit/` | 对象审计总入口（骨架＋7 对象判据分件） | v0.1·活跃 |
| `object-build/` | 对象构建总入口（三问＋六步＋3 分件） | v0.1·草稿 |
| `tri-collab/` | 四席协作纪律 | v2.4·活跃 |

（plan-tickets / ticket-flow / doc-governance / skill-contract-audit 暂留用户级 skill 库，是否迁入待拍。）

## 治理约定（本包自指）

1. **单写者**：本包所有 git 写操作由唯一执行通道完成；审计/研究席永无写盘权。
2. **decisions 只增不改**：判词与裁决落 `.collab/decisions/`，append-only；勘误＝原文后注。
3. **命名**：目录与文件名 ASCII 小写 kebab-case；文档正文中文自由。
4. **skill 形态约束**（源自研究裁决，见 docs/research/）：入口少、分件多、**分件平铺一层不嵌套**（官方 spec "one level deep"）。
5. **引证纪律**：七类引证失效扫描（强词法/弱词法/URL 反查可机检），见 `deliverables/object-audit/references/00-skeleton.md`。

## 本包的两个设计决定（出处见 .collab/decisions/2026-10-22-裁决记录.md）

- **不按对象拆 skill**——业界无先例（Parnas 1972／ISO 9001 §0.1／buf／ESLint 生态），判据＝「边界是否等于加载边界」。
- **`.collab` 按性质分区不按 actor**——`.` 前缀不表达 git 归属；decisions 进 git 是 ADR 惯例（决策记录必须可追溯）。
