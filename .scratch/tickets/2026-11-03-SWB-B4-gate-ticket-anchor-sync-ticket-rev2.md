# SWB-B4 · rev2 定点增补补丁件（project_domain_md 修值目＋16/15 差一勘正＋四席 deny 旧字面随动＋B4-C 表述改写＋矩阵补 design 行＋tests fixture 承接）

- 本件＝B4 票（`.scratch/tickets/2026-11-03-SWB-B4-gate-ticket-anchor-sync-ticket.md`·`9ae0b8a`＋勘正 `232bcfb`）之 **rev2 定点增补**（参 ES v3.1 体例：原票不动、补丁件另立）。原票未被本件推翻条款照旧；冲突处以本件为准。
- 修单真源＝会师件（`3ad4d99`）§二 B4 黄四目；QA 审票 `1c72966` 黄-1/黄-2/黄-3＋另注（SPEC_ID_HOME 段——**已被 B2 rev2 补丁一认领**，B4 不重复吞并，见本件补丁六边界注记）；PM 审票 `d6eef8a` B4-Y1/Y2/Y3。
- 开工 ANCHOR 随原票（B3 收口后）。

## 补丁一（B4-Y2·`project_domain_md` 修值目入闭集）

`seat-permissions.json` engineer 行（实测现值 `project_domain_md = "docs/collab-project-structure.md"`＝作废名残留）：

1. 修值＝`"docs/STRUCTURE.md"`（裁定三§二点九定名·B1-C 承诺承接）。
2. 并入判据 6 相等断言面：STRUCTURE.md 抽取的 `project_root`/`delivery_paths` 与 engineer 机械行集对账时，**同批断言** `project_domain_md` 值逐字＝`docs/STRUCTURE.md` 且 `test -f <项目>/docs/STRUCTURE.md` 存在（7 项目逐一）。
3. 声明闭集不变（seat-permissions.json 已在册）；本目入 B4-E 施工规格追加第 4 条。

## 补丁二（B4-Y1·闭集 16/15 差一勘正·展开表钉死）

原注「16 件展开口径」按 QA 清点展开＝15 件差一未交代。**勘正定案＝闭集实为 15 件**（原「16」＝起草误计，勘正从少不从多；回执 name-only 全等按 15 跑）：

| # | 件 |
|---|---|
| 1 | agent-skills/object-audit/scripts/check-ticket-reconcile.py |
| 2 | agent-skills/object-audit/scripts/check-collab-lint.py |
| 3 | agent-skills/object-audit/scripts/run-gates.sh |
| 4 | agent-experts/baigong-software-team/skills/sop/scripts/write-guard.py |
| 5 | agent-experts/baigong-software-team/skills/sop/scripts/lease-issuer.py |
| 6 | agent-experts/baigong-software-team/config/seat-permissions.json |
| 7 | agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json |
| 8 | agent-skills/multi-collab/SKILL.md |
| 9 | agent-skills/object-audit/SKILL.md |
| 10 | agent-skills/object-build/SKILL.md |
| 11 | agent-skills/bundle-assembly-registration/SKILL.md |
| 12 | agent-experts/baigong-software-team/bundle.lock |
| 13 | agent-experts/baigong-software-team/plugin.json |
| 14 | agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json |
| 15 | agent-experts/baigong-software-team/README.md（append-only） |

**rev2 闭集追加**（本补丁新增可写面·展开后合计 24 件）：

```
16 agent-experts/baigong-software-team/tests/s2/test_lease_instantiation.py
17 agent-experts/baigong-software-team/tests/s2/test_ledger_core.py
18 agent-experts/baigong-software-team/tests/s3/test_dispatch_gate.py
19 agent-experts/baigong-software-team/tests/s4/test_enforcement.py
20 agent-experts/baigong-software-team/tests/probes/run-probes.sh
21 agent-experts/baigong-software-team/tests/acceptance/drills/drill-03-write-side-intercept.sh
22 agent-experts/baigong-software-team/tests/acceptance/drills/drill-05-freeze-recover.sh
23 agent-experts/baigong-software-team/skills/sop/scripts/ledger-init.sh
24 agent-experts/baigong-software-team/tests/acceptance/drill-runner.sh（如断言路径锚涉改则入·零改则从回执申报退出）
```

## 补丁三（B4-Y2·四席 deny `deliverables/**` 旧字面随动入 B4-B/C）

实测（HEAD `3ad4d99`）`seat-permissions.json` deny_globs 含 `deliverables/**` 字面＝**四行**：host（L16 区）／product（L25 区）／architect（L34 区）／qa（L44 区）。

1. B2 后该字面永空转（fail-closed 兜底仍在但显式硬拦层失效）→ B4 随新树换代：四行 `deliverables/**` → **项目根相对新树字面**（语义随 B4-B1 两级锚定案：权限字面读作项目根相对，则 bundle 面防护行换代＝对应 delivery 路径枚举语义——百工侧以 engineer 行同款 delivery_paths 补集口径；host/product/architect/qa 四席非交付席，deny 换代字面＝`agents/** skills/** config/** hooks/** tests/** avatars/**` 六目录行入各席 deny 枚举（B4-E STRUCTURE↔engineer 同源对账同款真源，不复写名录＝引用 B1-C 百工 delivery_paths 行））。
   - 注：`seat-permissions-hooks-map.json` 内同源 deny 行（`deliverables/` 命中 5 处）同步随动。
2. 入判据 7 矩阵面：矩阵增「旧字面 `deliverables/**` occurrence＝0」断言行（全 config 域 grep）。
3. 附注：architect 行既有 `docs/PRODUCT.md` 等三件套 deny 与 `deny_globs_note` 零动（ES v3 权限随动既落地面，不重复处理）。

## 补丁四（B4-Y3·B4-C 自问自答改写·表述定案）

原 B4-C「deny 改枚举 `.collab/ledger/**` 等租约外桶？＝否（精化方向按收口定案）」自问自答形态作废，改写为定案陈述：

> **B4-C 定案（R⑧ (i) 向）**：engineer 行 deny 保留 `.collab/**` 为基线；**精化＝在 host 三席租约授权面侧**按 B1-D 规范闭集（B1 rev2 后＝十一桶含 design）逐桶枚举减授权：凡规范闭集内 host 租约可写桶（`ledger/` 等签发面桶），从对应席 deny 中显式让出并以注记行对表（R⑧ 过渡态(III) 冲突面在册消账）；非授权桶维持 deny 不让。**桶名以 B1-D 规范件为唯一真源（grep 引用不复写名录）**。

判据 7 矩阵随动换代＝**11 桶×相关席**（原 10 桶矩阵作废；design 行补入——design 桶＝史实锚入库面，host 无写权外溢＝deny 维持格，逐格读数入回执）。

## 补丁五（黄·tests fixture 与 sop 脚本路径字面承接·B4-B 追加目）

write-guard/lease 两级锚换代（B4-B）后，tests/drills fixture 旧路径字面必随（否则六演练/s2/s4 回归必红＝验收 3 硬线不可达）：

- `tests/s4/test_enforcement.py`（5 处 fixture 路径＋path_globs 字面）／`tests/s2/test_lease_instantiation.py`（1）／`tests/s2/test_ledger_core.py`（1·叙述行随新域描述）／`tests/s3/test_dispatch_gate.py`（1·同）／`tests/probes/run-probes.sh`（1·注释锚）／`drill-03`（2 处 `--path "deliverables/experts/..."` 探针路径→项目根相对新字面）／`drill-05`（1·叙述注释）／`ledger-init.sh`（1·路径注释）——全部入 rev2 闭集（补丁二 16–23 号）＋回执逐处表。
- 与 B2 rev2 补丁四桶 C 的认领闭环：B2 判据 3 桶 C 标「→B4」的 21 处命中＝本补丁实装面，两票账目互指闭合（B2 回执桶 C 行数＝本补丁逐处表行数对账断言）。

## 补丁六（边界注记·SPEC_ID_HOME/pkg_dir 段不重复认领）

QA「另注」建议 B4 认领 run-gates `SPEC_ID_HOME/pkg_dir` 段——**已由 B2 rev2 补丁一（B2-C8 之 4）认领**（换代与 mv 同批互锁＝B2 判据 4 可达性所需）。B4 闭集含 run-gates.sh 仅涉 GATES_MD/EVIDENCE 路由叙述面；`pkg_dir` 段 B4 期零触碰＝边界注记入回执，防双改。

## 补丁七（PM B4-Y1·R①②③ 回执处置目）

B4 回执固定增节「R①②③ 处置/在册」：R①（票面字段级约束随落位再核）＝再核结论一行（rev2 体例下票面字段无新增约束＝在册续观）；R②（host docs 转正代写·promote-manifest 通道对表）＝对表读数一行（promote-manifest.py 路径锚随 B4-B 两级锚换代自然覆盖·在册）；R③（tests/ 共写双席对表）＝对表一行（tests 面本 rev2 入 B4 闭集＝共写面已按单席作业，对表无冲突）。均非施工改笔＝回执级。

## 销账对位（本件覆盖修单目）

| 修单目 | 本件处置 |
|---|---|
| B4 黄·project_domain_md 修值目 | 补丁一 |
| B4 黄·16/15 差一交代 | 补丁二（勘正 15＋rev2 追加 9＝24 展开表钉死） |
| QA 黄2·四行 deny 旧字面随动申报 | 补丁三 |
| B4 黄·B4-C 自问自答改写 | 补丁四 |
| R-4 附随·矩阵补 design 行 | 补丁四（11 桶矩阵） |
| B2 rev2 桶 C 承接（tests fixture） | 补丁五（互指闭合） |
| QA 另注·SPEC_ID_HOME 段 | 补丁六（边界注记归 B2） |
| PM B4-Y1·R①②③ | 补丁七 |
| PM B4-Y3·engineer 现面读数 | 回执附「engineer 现面读值 vs 相等断言」读数（判据 6 执行时附） |

## 回执随动
回执增节：15＋9 展开表 name-only 全等＋四席 deny 换代前后读数＋`deliverables/**` occurrence 0 断言＋11 桶×席矩阵＋tests fixture 逐处表（与 B2 桶 C 对账）＋R①②③ 处置节＋边界注记（补丁六）。

——arch-swbreloc · rev2 补丁件（新建创作类·誊写禁令辖域外自察）。
