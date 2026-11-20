# 仓根 .collab 桶索引（治理史面）

六目录＝需求最终确认前阶段的标准界定，非全生命周期闭集。

## 桶总表（目录·放什么·谁法定写）

| 目录 | 放什么 | 法定写席 |
|---|---|---|
| `decisions/` | 裁定／裁决／收口登记（append-only·逐字誊录） | 主理人 |
| `audits/` | 审计结论／验收判词／复核件 | QA 席 |
| `receipts/` | 回执／完工回传件 | 对应产出席 |
| `board/` | 看板／状态总览 | 主理人 |
| `design/` | 设计稿（过程域·史实锚入库） | 架构席 |
| `research/` | 调研件 | 产出席 |
| `refs/` | 外部参照（排除面不入库） | 落件席 |
| `evidence/` | 证据流水（排除面不入库） | 落件席 |
| `inbox/` | 席位收件投递面（排除面不入库） | 主理人投递 |
| `process/` | 过程流水（排除面不入库） | 落件席 |
| `dispatch/` | 派发存档（排除面不入库） | 主理人 |
| `adr/` | ADR 过程面收口草案（一题一文档·禁多版本存活） | 主理人 |
| `drafts/` | 交接件草稿（顶层直落·无分子包·过期版入 `drafts/archive/`） | 产品／架构／QA／工程师共写域（租约粒度防护） |
| `architect/` | 架构席非交接件写权域 | 架构席 |
| `product/` | 产品席非交接件写权域（含会签补件） | 产品席 |
| `ledger/` | 账本三文件（ledger／leases） | 主理人 |
| `returns/` | 席位回流件面（returns/engineer） | 工程师席 |
| `claims/` | 机核认领清单 jsonl（件名与行型形态＝ITER-B 协议票面 v2 R4.1 verbatim 条款号指向） | 收单席位 |
| `instances/` | 实例码名册 roster.md（行格式＝R1.3 verbatim 指向） | 主理人投递 |
| `qa/` | QA 席非交接件写权域（存量桶实盘清算入册·现盘判词件即在位该桶） | QA 席 |

## 20 桶名录

`decisions/ audits/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/ drafts/ adr/ architect/ product/ ledger/ returns/ claims/ instances/ qa/`＋README 索引件

未列子包存续不禁，按项目阶段取用。

`drafts/` 顶层直接落交接件草稿、无分子包；唯一例外子包＝`drafts/archive/`（过期版本归档）；每交接件在 drafts 顶层只存一件存活态最新版。

历史案卷内 .collab/qa/ 字样＝改名前旧路径，读作 .collab/audits/

票面与临时工作物的唯一落点＝所属项目仓根（项目根＝含 `docs/STRUCTURE.md` 之探针锚目录）下的 `.scratch/<票号>/`；本仓百工项目锚＝`agent-experts/baigong-software-team/docs/STRUCTURE.md`；现行体例目录名 `.scratch/tickets/` 入表，规格名 `tickets/` 不再使用。

## 仓根性质注

仓根 `.collab/`＝本仓治理史面，无席位写权机检（seat-permissions 只辖软开团包内席位），落件按惯例＋decisions 归口。
