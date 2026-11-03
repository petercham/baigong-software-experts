# SWB-B5 · rev2 定点增补补丁件（gitignore 仓根层级显式防护行＋第三方外部快照三桶重立＋点目录 find 断言）

- 本件＝B5 票（`.scratch/tickets/2026-11-03-SWB-B5-closure-gitignore-readme-ticket.md`·`8f5efa9`）之 **rev2 定点增补**（参 ES v3.1 体例：原票不动、补丁件另立）。原票未被本件推翻条款照旧；冲突处以本件为准。
- 修单真源＝会师件（`3ad4d99`）§二 B5 黄两目；PM 审票 `d6eef8a` B5-Y1/Y2；QA 审票 `1c72966` B5-黄-1/黄-2。
- 开工 ANCHOR 随原票（B4 收口后）。

## 补丁一（B5-Y1/QA 黄-1·B5-A2 排除面重写必含仓根层级显式防护行＋外部快照三桶重立）

原票 B5-A2「任意层级 `/**/.collab/{…}/`」＋「旧仓根条款全部退役」**不足以防护仓根层级**（实测 `/**/` 形态对仓根 `.collab/<bucket>/` 不命中·B1 rev2 补丁二知悉同源）。B5-A 重写清单换代追加两组**仓根层级显式行**：

**A2-补1 仓根运行流水面防护行**（旧行退役后由新立仓根行承接）：

```
# 仓根层级运行流水面（run-gates EVIDENCE_DIR 现仍写仓根 $ROOT/.collab/evidence/gates·L98·B4 未改）
/.collab/evidence/
/.collab/refs/
/.collab/inbox/
/.collab/process/
/.collab/dispatch/
/.collab/backup/
/.collab/tmp-*.txt
```

- 依据：B3 后 era 留置面暂住仓根 `.collab/research/`（ESC1 域），门禁证据件仍续写仓根 `.collab/evidence/gates/`——旧行 `.collab/evidence/`（现 gitignore L17）退役时必须由上述 `/`-锚定新行同批顶替（新旧映射表该格＝「旧 L17 → 新 /.collab/evidence/」）。
- 注：`research/` 仓根留置面不被排除（史实锚入库面）＝负向行见 A2-补2。

**A2-补2 第三方外部快照三桶按新树/留置位重立**（现行 gitignore L37–39＋L42–44 先例形态随迁）：

```
/.collab/research/reference-2026-10-24/video-teams/
/.collab/research/reference-2026-10-24/official-cos/
/.collab/research/reference-2026-10-24/summoned-2026-10-24/
!/.collab/research/reference-2026-10-24/
!/.collab/research/reference-2026-10-24/.discussion/
!/.collab/research/reference-2026-10-24/REFERENCE-SOURCES.md
```

- 若 ESC1（era 跨仓微批）先于 B5 执行→该三桶随 era 留置面去向重算落位（B5 开工读 ESC1 回执态，映射表登记实际落位行）；若 ESC1 后于 B5→上述仓根行在位维持。
- era 留置面 gitignore 语义不变＝**外部参照件不入我仓版本库**既有裁决承接（PM B5-Y1 判据 B「真源混淆」纪律）。

**判据 2 矩阵补形态探针**（≥8 形态扩为 ≥12）：新增四探针——
1. `git check-ignore .collab/evidence/gates/x.json`＝ignore（仓根层级防护行命中）；
2. `git check-ignore .collab/refs/y`＝ignore；
3. `git check-ignore .collab/research/reference-2026-10-24/video-teams/z.md`＝ignore；
4. `git check-ignore .collab/research/reference-2026-10-24/REFERENCE-SOURCES.md`≠ignore（负向行命中）。

## 补丁二（B5-Y2·判据 1 点目录盲区补 find 计数断言）

原判据 1 `ls -d */` 不含点目录。追加断言：

```
find .collab -type f 2>/dev/null | wc -l ＝ era 留置数（＝B3 rev2 回执「era 留置清单」行数＋ERA 出册 research 面实测值，开工两栏读数）
find .collab/qa .collab/receipts .collab/tickets .collab/decisions .collab/design .collab/refs .collab/inbox .collab/process .collab/dispatch .collab/board -type f 2>/dev/null | wc -l ＝ 0
```

- 仓根 `.collab` 残留声明行（判据 1 注记）：「仓根 `.collab` 残留＝era 留置面（ESC1 域）＋外部快照留置面（A2-补2 ignore 态）＝**非违例**；其余桶＝0」。
- `docs/`、`deliverables/` 旧壳出现＝exit 1 断言照旧（B3 rev2 补丁一后 `docs/` 内容已分流＝B5-D 灭壳时点断言自然可达）。

## 补丁三（README 索引 era 注记行·QA 黄-2 关联项）

B5-B README 仓根重写第④节（跨项目案卷索引）对 era 留置面行标「**待移交 experts 仓（ESC1）**」注记（若 ESC1 已毕则标「已移交·ESC1 回执指针」）；索引行数断言随 B3 rev2 回执表行数口径（含出处二次分账列）。

## 补丁四（ESC1 票间关系随动）

原票票间关系「后置＝ESC1（独立微批随 B4/B5 后）」换代为引用实体票：**`.scratch/tickets/2026-11-03-SWB-ESC1-era-cross-repo-handover-micro-ticket.md`**（会师件 §三.1 补票裁定·本 rev2 同批出票）；ESC1 与 B5 先后序＝主理人排程裁，两票互不阻塞（B5 侧 A2-补2 两态口径已备）。

## 销账对位（本件覆盖修单目）

| 修单目 | 本件处置 |
|---|---|
| B5 黄·gitignore 仓根层级显式防护行（第三方快照三桶＋仓根 evidence 等） | 补丁一（A2-补1/补2＋矩阵四探针） |
| B5 黄·`ls -d */` 点目录盲区 find 断言 | 补丁二 |
| QA B5-黄-2·README era 注记 | 补丁三 |
| QA B5-黄-2/S1·ESC1 票体缺位 | 补丁四（引用 ESC1 票＝本批已出） |

## 回执随动
回执增节：gitignore 新旧映射表（含 L17→新仓根行、L37–39/L42–44→新树行逐格）＋判据 2 十二形态读数＋仓根 `.collab` find 两断言读数＋era 索引注记行读数。

——arch-swbreloc · rev2 补丁件（新建创作类·誊写禁令辖域外自察）。
