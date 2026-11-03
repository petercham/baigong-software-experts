# tickets 目录索引（活跃面 vs 历史账）

本目录＝票面账本（append-only·过程域）。历史票随回执/审计件的路径指针留存原位，不迁不删（指针只指不搬）。看活跃施工面只读本文件第一段即可。

## 一、活跃票包（当前可施工面·v2.9/V13 基线）

| 文件 | 角色 |
|---|---|
| `2026-11-01-SWB-ticket-pack-overview-v1.md` | 票包总览＝票目录（v1.5.1·含依赖序/候裁账/基线锚） |
| `2026-11-01-SWB-T01-platform-capability-probes-p1-p10.md` | 施工票 T01（**已收口**：放行 `e6f3647`·执行 `c38d77c`·QA 验证绿 `.collab/qa/2026-11-03-QA-T01-独立验证-v1.md`·判据 2 语义判据为准） |
| `2026-11-01-SWB-T02-ledger-state-lease-core.md` | 施工票 T02（候开工呈报） |
| `2026-11-01-SWB-T03-injection-dispatch-gate.md` | 施工票 T03 |
| `2026-11-01-SWB-T04-enforcement-hooks-b5-b7-b8-b10-b11.md` | 施工票 T04 |
| `2026-11-01-SWB-T05-expert-pack-assembly-b6.md` | 施工票 T05 |
| `2026-11-01-SWB-T06-acceptance-system-b9.md` | 施工票 T06 |

基线＝`.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md`（260 行·V13 n＝物理 n−28·头块三哈希 3f335333/7214ad14/efb4f765 落定）。

## 二、已闭合历史账（按战役分组·只读留存）

- **SWB 票包随动批（已完结）**：TKT28–39 系（再锚定/轻修/闭合核/Q-07 随动/卫生/剥壳 MERGE-V11、MERGE-V12 剥壳 V12、MERGE-V13 剥壳 V13）。TKT40 换锚系随动批延续。
- **SWB SOP 退役规则（已随 TKT41 执行·本票转历史）**：`2026-11-02-SWB-SOP-legacy-quickmode-bugfix-retirement-rule-ticket.md`——其 §20.1⑦ 随动义务由 TKT41（落盘 `59e2f59`·执行 `27caad3`·QA 验证绿 `799734f`）按 v2.9/V13 基线承接完成。
- **交付树回迁（已执行）**：`2026-11-01-DIRRELOC-*.md`。
- **软开团纪律/交付面批（已执行）**：ENG-B1/B2/D1/G2/G3/H1/H1F/H1F2/S2–S9、GH-D2、SOP-B1a、ARCH-G1、QA-G1、MC-M1。
- **EAC 技能升级战役（已闭）**：EAC-CLN、EAC-SK1–SK6 系。
- **FUXI 蒸馏工具链战役（已冻结入账）**：FUXI-S0a–S4/S0b/S0bP/S0c、FUXI-T1–T11、FUXI-S1a 系。
- **模板**：`TEMPLATE-票面模板-v2.md`。

历史票状态一律以各自回执/审计件（`.collab/receipts/`、`.collab/qa/`）与拍板台账（`.collab/decisions/`）为准；本索引仅指路不判态。
