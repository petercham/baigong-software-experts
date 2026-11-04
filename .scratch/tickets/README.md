# .scratch/tickets · 仓根过渡票目录索引

现状＝本目录现役票＝无（B 批后置队列 13 支已于本笔退役）。

退役名录（SWB-RET 票面退役批·13 支·基名＋收口登记 commit 指针）：

| 退役票面基名 | 收口登记（commit 指针） |
| --- | --- |
| `2026-11-03-SWB-B1-restructure-skeleton-ticket` | `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-SWB-B1-收口登记-v1.md`（`47fd524`） |
| `2026-11-03-SWB-B1-restructure-skeleton-ticket-rev2` | `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-SWB-B1-收口登记-v1.md`（`47fd524`） |
| `2026-11-03-SWB-B2-delivery-tree-migration-ticket` | `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-SWB-B2-收口登记-v1.md`（`47fd524`） |
| `2026-11-03-SWB-B2-delivery-tree-migration-ticket-rev2` | `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-SWB-B2-收口登记-v1.md`（`47fd524`） |
| `2026-11-03-SWB-B3-process-domain-migration-ticket` | `.collab/2026-11-03-SWB-B3-收口登记-v1.md`（`a05ed58`） |
| `2026-11-03-SWB-B3-process-domain-migration-ticket-rev2` | `.collab/2026-11-03-SWB-B3-收口登记-v1.md`（`a05ed58`） |
| `2026-11-03-SWB-B4-gate-ticket-anchor-sync-ticket` | `.collab/2026-11-04-SWB-B4-收口登记-v1.md`（`10865cf`） |
| `2026-11-03-SWB-B4-gate-ticket-anchor-sync-ticket-rev2` | `.collab/2026-11-04-SWB-B4-收口登记-v1.md`（`10865cf`） |
| `2026-11-03-SWB-B5-closure-gitignore-readme-ticket` | `.collab/2026-11-04-SWB-B5-收口登记-v1.md`（`50e726a`） |
| `2026-11-03-SWB-B5-closure-gitignore-readme-ticket-rev2` | `.collab/2026-11-04-SWB-B5-收口登记-v1.md`（`50e726a`） |
| `2026-11-03-SWB-ESC1-era-cross-repo-handover-micro-ticket` | `.collab/2026-11-04-SWB-B批总收口登记-v1.md`（`3b03738`·ESC1 段） |
| `2026-11-04-SWB-CD1-concurrency-discipline-ticket` | `.collab/2026-11-04-SWB-CD1-收口登记-v1.md`（`7acbbca`） |
| `2026-11-04-SWB-ES2-seatcard-gate-routing-ticket` | `.collab/2026-11-04-SWB-ES2-收口登记-v1.md`（`d7e6df9`） |

寻回：`git log --diff-filter=D --grep "RETIRE <票ID>"` → `git show <笔>^:<旧路径>`（ES 票面移除程序体例＝不建归档面，史实由 git 历史承载）。

注记：
- 旧仓根 `tickets/` 桶搬家目已在 B3b 完成（git mv＋E-ARC-1′ 换锚先行·B3a 跑绿后启动）；
- 票面落位＝`.scratch/tickets`（裁定 `f135855`）；
- B4＝check-ticket-reconcile 缺省票目录按各项目 `.scratch/tickets/` 双候选改造（前置＝本批完成态）；
- 项目级 `.scratch/tickets/` 历史票（各所属项目）不在 SWB-RET 射程＝退役批次分离候后续裁定。
