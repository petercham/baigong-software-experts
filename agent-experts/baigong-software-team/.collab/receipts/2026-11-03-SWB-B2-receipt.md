# SWB-B2 · 交付面搬家回执（施工席 engineer-b2）

- 规格源＝原票 `.scratch/tickets/2026-11-03-SWB-B2-delivery-tree-migration-ticket.md`（`f017a51`）＋ rev2 定点增补 `...-rev2.md`（`843784a`·冲突处以 rev2 为准）。
- 开工 HEAD 实测＝`6c17e64`（B1 收口登记笔≥要求）；开工前 `git status --short` 仅见两支 2026-11-01 TKT untracked 旧件（未触碰·收口时依旧在位）。
- 开工 tag＝`archive-pre-B2-20261104`→`6c17e64`（D6 既裁·判据7 读数＝tag 在册 1）。
- 落位说明：主理人指令落仓根 `.collab/receipts/`（原票新桶落位行与指令冲突处以指令为准·随 B1 回执先例同桶）。

## 基线两栏（开工落盘）

| 栏 | 读数 |
|---|---|
| 起草票锚 `f017a51` 实测 | deliverables＝198（bundle 88／EAC 7／MC 10／OA 40／OB 9／BAR 6／fuxi 37／README 1） |
| B2 开工点实测 | deliverables＝**199**（＋1＝B1-D 规范件 `skills/sop/references/collab-fixed-structure.md`）；删 deliverables/README.md 1 件→mv 件＝**198** |
| v3 §三「203 件」 | 起草时点漂移·按实测立账（rev2 补丁三登记行照落） |
| run-gates 挂接 | `.git/hooks/pre-commit`（绝对路径指旧位 run-gates.sh·钩子再生前后读数见判据4-C6 节） |
| 门禁开工基线 | `GATE PASS（发现 631 条）` exit 0·族集读数见判据4 |
| 六演练开工基线 | exit 0·SIX_DRILLS_GREEN＝1（T06_TMP 须 Windows 可读临时目录·Git Bash /tmp 形态 drill-05 假红＝环境口径·B1 收口随注①同族·登记不修件） |
| md 面基线（PM B2-Y2） | 开工 7 → 收口 45（mv 把旧树叙述面整体迁入新桶所致·本批不判红·B 批收口后 ES 退役批／另裁处理·逐处清单见附表乙） |
| py/sh/json 面基线 | 开工扫描面（agent-experts/agent-skills/tools）命中 12 行＋旧树内活引用 113 行（搬家前盘点·桶 B 认领目改毕归零） |

## 逐笔 commit 链（每笔后门禁 GATE PASS·禁 --no-verify／amend 均未触碰）

| 笔 | hash | 内容 |
|---|---|---|
| B2-A0 fuxi 预演 | `4f9e43f` | fuxi-skill 七项逐件 `git mv` 入壳（R100×37 全 rename）·判据4 rename 断言先行绿 |
| B2-A1 主体＋C 换代 | `91eb86f` | 五技能包逐 item mv 入壳＋bundle 顶层**十三项**逐笔 mv（`.codebuddy-plugin` 单列在册＝注册面三件 plugin.json／bundle.lock／.codebuddy-plugin/plugin.json 全逐笔在册）＋`git rm deliverables/README.md`＋B2-C1..C8 门禁扫描根同批换代＋install-hooks 文案＋钩子再生＋版本三同源 0.1.16→0.1.17＋README 版本账追加行＋两域名录补「交付面已迁入」态 |
| B2-B 二段 mv | `a8ae0fe` | PRODUCT.md／ARCHITECTURE.md 二段 mv 入 `agent-experts/baigong-software-team/docs/`（两段均在册·R100×2） |
| B2-C2 补笔 | `3d6b888` | check-pointer-closure selftest fixture join 随新树（declared 闭集件内活路径·--selftest 对拍全等 PASS） |
| B2-C8 补笔 | `8e603b1` | check-entity 注释末行旧域字面随动（桶 B 改毕归零·declared 件内） |
| 本回执 | （本笔） | 单独 commit `collab:` 前缀 |

逐笔 R 分布：A0＝R100 37；A1＝R100 148＋R073–R099 13（＝随动编辑的闭集件·mv＋内容换代同笔）＋M4（agent-experts/README、agent-skills/README、assert-tool、tools/check-source-of-truth）＋D1（deliverables/README.md）；B2-B＝R100 2；两补笔＝M1 各。R 行占比＝mv 件 100%（A/D/M 例外＝票面申报随动件闭集内）。

## 判据逐条实测（三态＝绿/绿/绿…全绿）

### 判据1 双向对账（rev2 补丁三钉值双式）
- `git ls-files agent-experts/ | wc-l`＝**92** ✓（89＝bundle 88＋规范件 1 ＋B1 壳 3）
- `git ls-files agent-skills/ | wc -l`＝**122** ✓（109 六包＋B1 壳 13）
- `git ls-files deliverables/ | wc -l`＝**0** ✓
- Σ＝214＝mv 198＋两域壳 16；对起草基线口径 214−17（壳全 17＝两域 16＋softwares/README 1）＝**197** ✓；软wares 独立读＝1。
- 勘对注记照 rev2：规范件归属侧＝experts 记账（92/122 分解·Σ 与 91/123 口径全等 214·逐笔 name-status 可裁决）。

### 判据2 rename 字节一致（誊写禁令判据）
- 各笔 `git show -M --name-status` R 分布如上；A0/A1/B2-B 三笔内全部 mv 件 R100（除申报随动件）。
- 抽样 10 件 `git diff <笔>^:<旧> <笔>:<新> | wc -l`＝**0**（A0 五件＋A1 五件实测·见工作记录）。剥壳段＝恒 0（本票无剥壳·开工附注①照录）。

### 判据3 活引用清零（rev2 补丁四三桶分账·台账制）
终态扫描 `grep -rno "deliverables/" agent-experts/ agent-skills/ tools/ --include='*.py' --include='*.sh' --include='*.json'`＝**74 行**（106 occurrence·occurrence 口径）。
判据式：命中 74 − 桶 C 在册 65 − 桶 A／呈核在册 9 ＝ **0** ✓（桶 B 改毕自然归零＝declared 九件＋tools 主件旧路径全数清零·逐件 grep 复核＝0）。
负例实证：合成账外命中件 → 台账判定 exit 1 ✓（命中即咬·可跑性已验）。

**桶 B＝B2-C8/C9 自认领（本批改毕归零·不入终态账）**：
| 件 | 改点 |
|---|---|
| check-skill-meta.py | 根探针换代＋扫描根三分类候选＋头块锚 L5/L14/L29/L30＋退出码闭集引注 L40 |
| check-entity.py | SCAN_ROOT_DIRS＋根探针＋L28/L35/L109–110 叙述＋L247 注释字面（补笔 8e603b1） |
| check-provenance.py | 根探针＋existing_providers 三分类＋spec_file 多探段＋default_targets＋头块锚 L5/L30/L32＋infra 文案三处 |
| publish.py | 头块锚×3＋pkg_dir_of/list_pkgs 三分类＋痕迹扫描面 needles＋gate_a3 注释＋help 文案 |
| run-gates.sh | spec_file 注释锚 L4/L13/L22/L34（PM S4 同笔）＋仓根探针＋GATES_MD 候选序＋S-03 注释 L127＋pkg_dir 段（SPEC_ID_HOME 键值零动） |
| assert-tool.py（B2-C9） | L28 叙述＋_PRODUCTS_SUBPATH＝`("products",)`（生效池＝本技能目录内 products/·STRUCTURE delivery_paths 既载） |
| install-hooks.sh | L4/L15 spec 锚＋L85 钩子文案（钩子再生覆盖＝B2-C6） |
| check-pointers.py（B2-C1） | DEFAULT_SCOPE 三分类＋根探针两处＋候选层三分类＋check_orphans 三域＋孤儿落点改真实路径＋help＋docstring |
| check-pointer-closure.py（B2-C2） | DEFAULT_PKG_FACES 换代＋根探针＋头注释＋selftest fixture join（3d6b888） |

**桶 C＝后续票认领欠账（65 行·逐处登记）**：
| 文件:行号 | 桶别→认领票 |
|---|---|
| check-ticket-reconcile.py L6(头块锚已改)＋其余 41 行（.collab 票目录未迁·票面引用/fixture 面） | C→**B4**（B2-C7①既列不在本批；头块 spec_file 一行随动已改＝P-2 自存活所需·回执登记） |
| config/seat-permissions.json 7 行（L5/L6/L7/L16/L25/L34/L44） | C→**B4 rev2**（deny 四行＋字面随动） |
| config/seat-permissions-hooks-map.json 5 行（L7/L12/L16/L20/L24） | C→**B4 rev2** |
| skills/sop/scripts/ledger-init.sh L11（PACK_ROOT 注释行） | C→**B4 rev2** |
| tests/s2/test_lease_instantiation.py L82 ／ tests/s2/test_ledger_core.py L5 ／ tests/s3/test_dispatch_gate.py L5 | C→**B4 rev2**（fixture 路径字面同批改） |
| tests/s4/test_enforcement.py L5/L83/L88/L167/L180（5 行） | C→**B4 rev2** |
| tests/probes/run-probes.sh L43（注释内禁面叙述） | C→**B4 rev2** |
| tests/acceptance/drills/drill-03 L28/L32（2 行）／drill-05 L19（1 行·注释） | C→**B4 rev2** |

**桶 A＝史述豁免（tools 面·9 行）**：
| 文件:行号 | 性质 |
|---|---|
| tools/check-source-of-truth.py L58／L80 | 旧域史实叙述（裁决条目出处注／W6 遗留实测引注）＝A 史述 |
| tools/baseline-seat-decl.json L7/L23/L30/L37 | 席位声明基线快照内旧域字面（--regen-seat-baseline 程序化件·随 B4 席位权限表换代重生成）＝A 史述（B4 认领随动重生成登记） |
| tools/count_agent_tokens.py L13 | 拆仓口径注释＝A 史述 |
| tools/count_agent_tokens.py L20 | **目外呈核**：活 glob `deliverables/experts/*/agents/*.md` 已随搬家失效（该件＝人读 token 计数工具·不在门禁链·不在 B2 声明闭集＝禁动面五件之一）→ 候裁不自行拍单列（见候裁节） |

无斜杠 join 五处处置回执分账：check-collab-lint L131（根探针·不在闭集→未改·B3a/B4 域＝票面 B2-C7②口径）／check-collab-lint L279（fixture join·不在闭集→未改·登记呈核·--selftest 现咬 infra error 读数见候裁）／check-source-of-truth L507＋L754（B2-C5 闭集内→**已改**）／assert-tool L142（B2-C9 闭集内→**已改**）。commit-audit.py `.collab/tickets` 活正则 2 处＝回执分账（L15/L35·`.collab` 未迁面·B4 域·零触碰）。

### 判据4 门禁零回归
- 开工基线 c4-base＝GATE PASS 631（族集：check-collab-lint SUBSTR8/VIOLATION18·check-pointer-closure SUBSTR101/VIOLATION86·reconcile WATCH 全量＝B1 收口随注① reconcile 读数时点/环境依赖口径照用）。
- 每笔后跑门禁：A0 后绿·A1 后 GATE PASS 648·B2-B 后（钩内直跑）GATE PASS 648·两补笔后 GATE PASS 648。
- 族集对拍 base→final：**NEW families＝none／GONE families＝none**；计数差三族＝既有族实例增（非新违例族·B1 收口 WATCH 43→51 先例同口径）：
  - check-pointer-closure OA-D6-3 86→88、OA-D6-4 17→19：＋4＝**B1 壳件 `.collab/README.md` ×2 首次入 agent-experts 包面**（B1-D 预登记行 `deliverables/experts/.../collab-fixed-structure.md` 跨包指针落包内＝出包指针＋包内不可达·桶 A 性质·B4 换锚随动）＋PRODUCT 行级位移；
  - check-pointers BLOCK OA-D6 10→23：＋15 全部＝B1 壳 README／迁入 md 旧路径指针随新树扫描面（agent-experts 壳＋fuxi products README＋multi-collab 三 md）现位可扫＝**搬家后既有悬空面换址再现**（史述/规范叙述 md 面＝PM B2-Y2 口径 B 批收口后处理·advisory 族不拦）；−5＝deliverables/README.md 删除＋旧址行消失。
- **md 面 BLOCK 增 15 行呈核**（不自行拍单）：全部为 md 文档面旧域指针悬空＝rev2「md 面口径」既载不判红面·其中 8 行＝B1 壳 README 预登记行（B1 成品禁动面）→ 候裁节列目。
- 钩子再生两读数（B2-C6·不手改）：前＝`exec bash "D:/.../deliverables/skills/object-audit/scripts/run-gates.sh" --root "D:/multi-agent-collab-devkits"`＋文案行旧字面；后＝`exec bash "D:/.../agent-skills/object-audit/scripts/run-gates.sh" --root "D:/multi-agent-collab-devkits"`＋文案行新字面（install-hooks.sh 再生成）。

### 判据5 六演练回归
`T06_TMP=<Windows 可读 Temp> bash agent-experts/baigong-software-team/tests/acceptance/drill-runner.sh` → exit 0 且 `SIX_DRILLS_GREEN` occurrence＝**1** ✓（新路径实跑·drill-03/05 内桶 C fixture 字面按 B4 前口径不改＝演练仍绿）。

### 判据6 版本账随动
三同源 0.1.16→**0.1.17**：plugin.json／bundle.lock／.codebuddy-plugin/plugin.json 实测读数全 0.1.17 ✓；README 版本账 append-only 追加一行（v0.1.17 行在位·append 笔一度折行并入下条已即时修复＝本回执登记）。

### 判据7 tag 在册
`git tag -l "archive-pre-B2-*" | wc -l`＝1（archive-pre-B2-20261104→6c17e64）✓。

### 判据8（rev2 新增·换代前后等价断言）
1. `existing_providers` 换代前后**六 provider 实名成员资格全等**（真式执行·勿按逐名相等幻影名口径）：改前枚举 {experts, skills, 六包名}／改后枚举 {baigong-software-team, 六包名}；六实名 {EAC, MC, OA, OB, BAR, fuxi} pre∈／post∈ 全 True＝成员资格向量全等 ✓（experts/skills 二旧容器段与 baigong-software-team 新目录＝容器换形非 provider 实名·落盘对拍见工作记录）。
2. run-gates 裁决段 spec_id 解析命中换代前后相等：17 键全表 per-id 对＝改前 17×True／改后 17×True 全等 ✓（OA×9／MC×5／EAC×3 各≥2 抽样逐名 True；PUB-*／OB-* 表内零键＝SPEC_ID_HOME 映射在册但路由表无键·登记读数）。
3. 判据4 门禁零回归＝自此机械可达 ✓（每笔后 GATE PASS 实跑）。

## deliverables/README.md 待并入行（B5 认领）
删除的 deliverables/README.md＝索引表两节（skills/ 六对象行＋experts/ 两对象行）＋规则段＋退役/未迁入段。B5 并入仓根 README 时逐段搬运·本回执登记待并入＝「skills/ 表 6 行＋experts/ 表 2 行＋退役注＋未迁入注」原文以 `git show 91eb86f^:deliverables/README.md` 取证。

## 候裁（不自行拍·单列）
1. **tools/count_agent_tokens.py L20 活 glob 失效**：`deliverables/experts/*/agents/*.md` 随搬家落空（该件不在 B2 闭集·禁动面·非门禁链）→ 建议随 B4/B5 微票改 `agent-experts/*/agents/*.md`。
2. **check-collab-lint 两件（L131 根探针＋L279 fixture join）不在 B2 闭集**：根探针旧面已失效但该件缺省跑走 --root 注入不受影响（门禁绿·族计数不变）；`--selftest` 独立调用现咬 infra error（旧 fixture 路径）→ 建议 B3a/B4 闭集认领（票面 B2-C7②既指 B3a/B4 域）。
3. **B1 壳 README 预登记行 8 处旧路径指针悬空**（7×`.collab/README.md`＋1×fuxi 面相关 md）＝B1 成品禁动面＋md 面 B 批收口后处理口径 → 建议 B4 换锚批一并随动。
4. check-ticket-reconcile「未声明生成件」WATCH 增 3 行（B2-B 二段 mv＋C2 补笔路径对）＝该器以 .collab 票面为账基·B2 票在 .scratch 未入其账基面·B4 票目录迁移后自洽·登记级。

## 附表甲·逐桶对账表
- 开工 199＝198（起草 198 分桶：bundle 88／EAC 7／MC 10／OA 40／OB 9／BAR 6／fuxi 37／deliverables/README 1）＋B1-D 规范件 1（物理在 bundle skills 子树）。
- mv 198＝experts 侧 89（88＋规范件 1）＋skills 侧 109（六包）。
- B1 壳 16＝experts 3（README＋.collab/README＋docs/STRUCTURE）＋skills 13（README＋6×.collab/README＋6×docs/STRUCTURE）。
- 终态：agent-experts 92／agent-skills 122／softwares 1／deliverables 0；Σ(92+122)=214＝mv198＋壳16；214−壳17＝197 ✓。

## 附表乙·md 面读数（判据不判红·登记）
开工 7（全为 B1 壳 .collab/README 预登记行）→ 收口 45（＋38＝旧树 md 叙述面随 mv 迁入新桶＝扫描面换址非新增内容·逐处见终态 grep 台账·B 批收口后 ES 退役批／另裁处理）。

——engineer-b2 · SWB-B2 施工回执（全部搬家笔＝git mv·誊写禁令合规·剥壳段恒 0）
