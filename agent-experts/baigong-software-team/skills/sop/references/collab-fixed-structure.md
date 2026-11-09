# .collab 固定结构规范（collab-fixed-structure）

头注：本件＝规范面（泛化级·裁定三§二点五无特例）。
依据注记：design 桶入闭集＝会师裁定 R-4（从 v3 §三具体申报优先）；v3 §二标准结构图无 design 桶＝基线内部第二处不自洽，按 erratum 走收口登记增补（同既有勘误程序），不改冻结基线文本。
六目录＝需求最终确认前阶段标准界定；桶闭集换代 11→17＝结构落改＋returns 补录
adr 单立之业界实践锚＝Michael Nygard《Documenting Architecture Decisions》(2016)：ADR 记录难以逆转的架构决策，其 Consequences 常直接驱动或否定产品需求（取证口径＝人类工程实践通例优先）

## 桶名闭集（逐字）

每个项目包的 `.collab/` 目录桶名闭集＝

`decisions/ audits/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/ drafts/ adr/ architect/ product/ ledger/ returns/`＋README 索引件

`drafts/` 顶层直接落交接件草稿、无分子包；唯一例外子包＝`drafts/archive/`（过期版本归档）；每交接件在 drafts 顶层只存一件存活态最新版。

闭集外目录名不入规范；`.collab/` 根下散件无归属分区者按 tmp- 前缀惯例处理（现仓 .gitignore 既有语义）。

## 两制入库声明

- 入库面（进 git·史实锚）：`decisions/`、`audits/`、`receipts/`、`board/`、`design/`、`research/`（设计稿属过程域＝v3 §三 L64 既载语义，design 归入库面随 R-4）、`drafts/`、`adr/`、`architect/`、`product/`、`ledger/`、`returns/`（ledger 补链＝账本三文件入链后入名录；returns 在用面本已入库＝名录补全非新开）。
- 排除面（.gitignore 排除·过程流水/外部参照/临时）：`refs/`、`evidence/`、`inbox/`、`process/`、`dispatch/`，另含 `backup/`、`tmp-*.txt`（现仓 .gitignore 既有语义承接）。

## 与用户 STRUCTURE.md 的边界

用户 `STRUCTURE.md` 内出现 `.collab` 子目录规范＝不认（裁定三§一.3 照录）：项目分层目录方案只辖交付面与文档面，`.collab` 案卷面结构一律以本规范件为准，不由项目侧自定。

## 对 B4 的先决真源指针

本件＝B4 门禁 deny `.collab/**` 显式枚举减授权精化的先决真源（引用指针，不复写 B4 行文本）：B4 闭集内枚举桶名时以本件桶名闭集为逐字依据。

票面与临时工作物的唯一落点＝所属项目仓根（项目根＝含 `docs/STRUCTURE.md` 之探针锚目录）下的 `.scratch/<票号>/`；本仓百工项目锚＝`agent-experts/baigong-software-team/docs/STRUCTURE.md`；现行体例目录名 `.scratch/tickets/` 入表，规格名 `tickets/` 不再使用。

——规范件新建创作类·誊写禁令辖域外自察。
