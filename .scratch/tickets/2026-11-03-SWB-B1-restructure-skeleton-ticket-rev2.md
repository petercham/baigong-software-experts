# SWB-B1 · rev2 定点增补补丁件（design 桶扩员＋gitignore 仓根层级知悉注记）
Status: 已结案（retire 宣告 2026-11-04·依 2026-11-04 审计对齐类免拍板放行裁定·票面退役批 SWB-RET）

- 本件＝B1 票（`.scratch/tickets/2026-11-03-SWB-B1-restructure-skeleton-ticket.md`·`b5fd2b4`）之 **rev2 定点增补**（参 ES v3.1 体例：原票不动、补丁件另立、版本链追加）。原票全部未被本件推翻之条款照旧生效；本件条款与原文冲突处＝以本件为准（后笔覆盖前笔·append-only）。
- 修单真源＝会师件 `.collab/2026-11-03-SWB-B1B5-双席审票会师-处置裁定-v1.md`（`3ad4d99`）§二黄路由 B1 行＋§一 R-4（design 桶裁决定向＝从 §三 表设 design 桶）。
- 开工 ANCHOR 义务随原票：开工实测 HEAD 应 ≥ 本 rev2 笔。计数口径＝occurrence；判据自带落盘；负例 exit≠0。

## 补丁一（R-4 承接·B1-D 规范桶闭集扩员含 design）

B1-D 规范件 `deliverables/experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md` 桶名闭集由十桶扩为 **十一桶**，逐字闭集串换代为：

```
decisions/ qa/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/
```

- 两制入库声明随动：`design/` 归**入库面**（史实锚·与 decisions/qa/receipts/board/research 同制——设计稿属过程域＝v3 §三 L64 既载语义）。
- B1-B 各项目 `.collab/README.md` 预登记桶名录＝十一桶（随上串）。
- **依据注记（规范件内头注追加一行）**：「design 桶入闭集＝会师件 `3ad4d99` R-4 裁定（从 v3 §三 L64 具体申报优先）；v3 §二标准结构图（L40–43）无 design 桶＝基线内部第二处不自洽，按 erratum 走 B 批收口登记增补（同 TKT L70 勘误程序），不改冻结基线文本。」
- 判据 4 随动换代（原「＝1 整串逐字存在」式不变，串值换）：
  `grep -o "decisions/ qa/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/" deliverables/experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md | wc -l` ＝ **1**。
- 声明闭集件数不变（20 件·规范件仍一件）。

## 补丁二（B1-E gitignore 过渡块知悉注记·不改动块文本）

B1-E 追加块文本**零改**；票内追加知悉注记一节（施工时写入票面回执口径，不入 .gitignore 注释以外之处）：

> 知悉（QA B1-黄-1 实测）：`/**/` 形态对**仓根**层级 `.collab/<bucket>/` 不命中（`git check-ignore .collab/refs/x` exit 1）、对嵌套层级（`a/b/.collab/refs/x`）命中。故 B1 期仓根现桶防护＝**现行旧行在位**（B1-E「只增不删」成立→B1 期无洞，判据 5 探针选嵌套形态故票面自洽）；仓根层级防护行的**终写承接责任在 B5 rev2**（B5 全重写若退役旧行＝仓根 `.collab/evidence/` 等失护——run-gates `EVIDENCE_DIR="$ROOT/.collab/evidence/gates"`（L98）现仍写仓根且 B4 不改，见 B5 rev2 补丁一）。

判据不增（知悉注记非断言项）。

## 销账对位（本件覆盖修单目）

| 修单目 | 本件处置 |
|---|---|
| R-4（B1-D 桶闭集扩 design） | 补丁一 |
| B1 黄（E 节 `/**/` 不防仓根知悉注记） | 补丁二 |
| R-4 附随（B4-C 矩阵补 design 行） | 归 B4 rev2（本件供闭集真源＝十一桶串） |

## 回执随动
回执增一节「rev2 补丁逐条读数」：判据 4 换代串读数＋规范件头注行读数。原回执要求不变。

——arch-swbreloc · rev2 补丁件（本件自身＝新建创作类·誊写禁令辖域外自察）。
