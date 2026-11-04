# SWB-B2 · rev2 定点增补补丁件（门禁换代闭集扩全 R-2＋入壳补 `.codebuddy-plugin` 目 R-3＋判据钉值/分账重写）
Status: 已结案（retire 宣告 2026-11-04·依 2026-11-04 审计对齐类免拍板放行裁定·票面退役批 SWB-RET）

- 本件＝B2 票（`.scratch/tickets/2026-11-03-SWB-B2-delivery-tree-migration-ticket.md`·`f017a51`）之 **rev2 定点增补**（参 ES v3.1 体例：原票不动、补丁件另立）。原票未被本件推翻条款照旧；冲突处以本件为准。
- 修单真源＝会师件（`3ad4d99`）§一 R-2/R-3＋§二 B2 黄三目；QA 审票 `1c72966` 红-1/红-2/黄-1/黄-2；PM 审票 `d6eef8a` B2-Y1/B2-Y2/S4。
- 开工 ANCHOR 随原票（B1 收口后）；本 rev2 笔在盘＝开工前提。

## 补丁一（R-2·声明闭集扩——门禁扫描根换代补全）

原票声明闭集**追加六行**（B2 门禁换代面自此完整＝判据 4「每笔后 GATE PASS」机械可达）：

```
- agent-skills/object-audit/scripts/check-skill-meta.py（B2-C8）
- agent-skills/object-audit/scripts/check-entity.py（B2-C8）
- agent-skills/object-audit/scripts/check-provenance.py（B2-C8）
- agent-skills/object-build/scripts/publish.py（B2-C8）
- agent-skills/object-audit/scripts/run-gates.sh（追加目：SPEC_ID_HOME/pkg_dir 段＋头部注释锚——原票已列本件，本 rev2 扩其施工目）
- agent-skills/fuxi-skill/gates/assert-tool.py（B2-C9 生效池注册路径声明行随动）
```

### B2-C8 三子脚本＋publish.py＋run-gates 内嵌段换代（与 mv 同批互锁·QA 红-1 四段逐销）

行号锚＝HEAD `3ad4d99` 现盘旧位实测（开工位移以逐字文本锚定位）：

1. **check-skill-meta.py**：`find_root`（L68–72）根探针 `isdir(explicit/"deliverables")` → 换代＝`isdir(cur/"tools") and any(isdir(cur/c) for c in ("agent-experts","agent-skills","softwares"))`（与 B2-C1 check-pointers 同款探针）；扫描根 `deliverables/*/SKILL.md`（L35 语义面＋代码内路径构造）→ 三分类目录候选；头部 `spec_file:` 注释锚 L5/L14/L29/L30 与退出码闭集引注 L40 旧字面 → 新树字面（史述段不在此列＝回执分账）。
2. **check-entity.py**：`SCAN_ROOT_DIRS = ("deliverables",)`（L112）→ `("agent-experts","agent-skills","softwares")`；根探针（L128）同 1 换代；L28/L35/L109–110 叙述段旧域描述随动（活代码注释面）。
3. **check-provenance.py**：根探针（L99）同 1 换代；`existing_providers`（L184–192）双域探 `root/deliverables`＋`root/deliverables/skills` → 换代＝三分类目录下一层＋项目目录一层（等价语义：providers 枚举集换代前后逐名相等断言入判据 8）；缺省 target 扫描 `<仓根>/deliverables/*/scripts/*.py`（L45 语义）→ `agent-*/<项目>/scripts/*.py`；头块锚 L5/L30/L32 随动。
4. **run-gates.sh 内嵌裁决段**（QA 红-1 之 4）：`SPEC_ID_HOME`（L209–215）**键值零动**（前缀→包名语义不变）；其解析段 `pkg_dir = os.path.join(ROOT, "deliverables", …)` 双域探 `deliverables/<pkg>`/`deliverables/skills/<pkg>`（L264–272）→ 换代＝`root/<分类>/<pkg>` 三分类候选（`agent-skills/<pkg>`、`agent-experts/<pkg>`、`softwares/<pkg>`；解析后 OA-*/MC-*/EAC-*/OB-* 可解析断言入判据 8）；头部 `spec_file:` 注释锚 L4/L13/L22/L34 旧字面 `deliverables/multi-collab/references/60-gates.md` → `agent-skills/multi-collab/references/60-gates.md`（＝PM S4 spec_file 注释锚同笔随动）。
5. **publish.py**（object-build·同族探测逻辑·原全套票无认领＝rev2 并入 B2）：头块 `spec_file:` 锚 L5/L14/L23 → `agent-skills/object-build/references/60-publish.md`；`deliverables/<pkg>`/`deliverables/skills/<pkg>` 双域探（L147/L159）→ 三分类候选；L340（痕迹扫描面叙述）/L477（S-04 缺省域）/L1159（help 文案）随动。
6. `install-hooks.sh` L85 文案行（`deliverables/ 或 deliverables/skills/ 下 multi-collab/...`）＝钩子再生覆盖（B2-C6 已在位·不另列）。

### B2-C9 fuxi 生效池注册路径声明随动（轻目）

`agent-skills/fuxi-skill/gates/assert-tool.py` L28 附近「`deliverables/products/`＝active 生效池注册路径（FC-6 池计数基面）」＝活路径声明（非史述）→ 随新树改 `agent-skills/fuxi-skill/products/`（fuxi 交付面＝STRUCTURE delivery_paths `products/` 既载；B1-C 名录在位）。

## 补丁二（R-3·B2-A1 入壳枚举勘正补目）

原票「十一项」勘正＋补目，换代为**bundle 顶层十三项逐笔枚举**（实测锚 HEAD `3ad4d99`：`git ls-files deliverables/experts/baigong-software-team/ | awk -F/ '{print $4}' | sort -u` ＝ 13）：

```
可见十二项：agents/ avatars/ bundle.lock config/ hooks/ plugin.json settings.json
            skills/ tests/ README.md PRODUCT.md ARCHITECTURE.md
隐藏一项  ：.codebuddy-plugin/（WorkBuddy 注册面＝plugin.json 版本同源三件之一·装载面高危项）
```

- 逐笔 `git mv deliverables/experts/baigong-software-team/<项> agent-experts/baigong-software-team/` 入壳（内容注入式规则不变）；`.codebuddy-plugin/` 一笔单列入回执（QA 平台兼容性必核命中位）。
- PRODUCT.md／ARCHITECTURE.md 先入 bundle 根壳，随即 B2-B 二段 mv 入 `docs/`（两段均在册）。
- 判据随动：判据 1 桶计数含 `.codebuddy-plugin/plugin.json`（experts 侧）；回执「注册面三件（plugin.json／bundle.lock／.codebuddy-plugin/plugin.json）逐笔在册」断言行。

## 补丁三（判据 1 重写·钉值双式）

原票判据 1 多口径自缠（87/109/110/197/Σ−17 并存）作废，换代为**单一可跑双式＋钉值**：

```
(a) git ls-files agent-experts/ | wc -l ＝ 92
(b) git ls-files agent-skills/  | wc -l ＝ 122
(c) git ls-files deliverables/  | wc -l ＝ 0
```

推导账（回执附对账表·逐桶）：
- **开工实测基线两栏登记**：起草票锚 `f017a51` 实测 deliverables＝**198**（分桶 bundle 88／EAC 7／MC 10／OA 40／OB 9／BAR 6／fuxi 37／README 1）；**B2 开工点**＝198＋1（B1-D 规范件 `collab-fixed-structure.md` 新入 tree）＝**199**；删 `deliverables/README.md` 1 件 → mv 件＝**198**。v3 §三「203 件」＝起草时点漂移，按实测立账（登记一行）。
- agent-experts 侧＝89（bundle 88＋规范件 1）＋B1 壳 3（agent-experts/README＋baigong `.collab/README`＋`docs/STRUCTURE`）＝**92**。
- agent-skills 侧＝109（六包）＋B1 壳 13（agent-skills/README＋6×`.collab/README`＋6×`docs/STRUCTURE`）＝**122**。
- Σ＝214＝mv 198＋两域壳 16；对起草基线口径：214−17（壳全 17＝两域 16＋softwares/README 1）＝**197** ✓。
- 勘对注记（诚实分账）：会师件引 QA 复算钉值「experts 91／skills 123」与本席独立推导「92／122」**Σ 全等（214）·分解差 1**＝B1-D 规范件归属侧记账口径差（本席＝规范件入 bundle skills 子树随 experts mv，与逐笔 mv 事实一致）；断言以本件推导链＋逐桶回执表为准，复审席若持异见以逐笔 name-status 裁决。

## 补丁四（判据 3 重写·豁免账三桶分账）

原票判据 3「豁免＝史述」一桶吞约 90 处活代码旧路径＝不可执行（QA 黄-2），作废换代：

扫描命令不变（`deliverables/` 于 `*.py/*.sh/*.json`），豁免清单＝**三桶逐处登记账**（回执强制表：文件:行号:桶别）：

- **桶 A＝史述豁免**：叙述性史实／旧域描述（非活代码语义），逐处入表。
- **桶 B＝B2-C8/C9 自认领**（补丁一）：check-skill-meta 12 行／check-entity 8 行／check-provenance 15 行／publish.py 8 行／run-gates 注释锚 4 行＋pkg_dir 段／assert-tool 1 行——**本批内改后必零**（不入豁免终态账，改毕即从命中面消失）。
- **桶 C＝后续票认领欠账**（逐处标认领票）：check-ticket-reconcile.py 42 行→B4；seat-permissions.json 7 行＋seat-permissions-hooks-map.json 5 行→B4（rev2 补丁二四行 deny＋字面随动）；tests 面（`tests/s2/test_lease_instantiation.py` 1／`tests/s2/test_ledger_core.py` 1／`tests/s3/test_dispatch_gate.py` 1／`tests/s4/test_enforcement.py` 5／`tests/probes/run-probes.sh` 1／`tests/acceptance/drills/drill-03` 2／`drill-05` 1）＋`skills/sop/scripts/ledger-init.sh` 1（注释行）→**B4 rev2**（write-guard/lease 项目根锚换代时 tests fixture 路径字面同批改，B4 rev2 闭集已扩）。
- 判据式：命中 − 桶 C 在册 − 桶 A 在册 ＝ **0**（桶 B 改毕自然归零）；负例＝账外命中 exit 1。
- **md 面口径**（PM B2-Y2）：随动清单**不涵盖**包内 md 文档锚路径行（六包 SKILL/references 内 `deliverables/` 叙述＝规范叙述史述面，门禁 check-pointers 兜底在位）；开工前跑一次 md 面读数入回执（`grep -rno "deliverables/" agent-experts/ agent-skills/ --include='*.md' | wc -l` 基线入册），本批不判红、B 批收口后 ES 退役批/另裁处理。

## 补丁五（判据 8 新增·换代前后等价断言）

1. `existing_providers` 换代前后运行输出枚举集逐名相等（改前落盘 vs 改后落盘 `diff`＝0）。
2. run-gates 裁决段对 OA-*/MC-*/EAC-*/OB-*/PUB-* 抽样 spec_id（各≥2）解析命中数换代前后相等（改前/改后各跑一次落盘对拍）。
3. 判据 4 门禁零回归照旧＝自此机械可达（每笔后 GATE PASS）。

## 销账对位（本件覆盖修单目）

| 修单目 | 本件处置 |
|---|---|
| R-2（三子脚本＋run-gates 段换代无认领） | 补丁一（B2-C8/C9 闭集扩·同批互锁） |
| R-3（入壳枚举漏 `.codebuddy-plugin`） | 补丁二（十三项勘正枚举） |
| B2 黄·判据1 钉值双式 | 补丁三（92/122/0＋推导账＋勘对注记） |
| B2 黄·判据3 史述/欠账分账 | 补丁四（三桶账） |
| B2 黄·203 vs 198 漂移行 | 补丁三（基线两栏登记） |
| PM S4（run-gates spec_file 注释锚） | 补丁一之 4（同笔随动） |

## 回执随动
回执增节：闭集展开表（原 14 目录级＋追加 6 行）＋逐桶钉值对账表＋豁免三桶逐处表＋判据 8 等价读数＋`.codebuddy-plugin` 逐笔在册行＋md 面基线读数。

——arch-swbreloc · rev2 补丁件（新建创作类·誊写禁令辖域外自察；本票搬家目仍全 git mv）。
