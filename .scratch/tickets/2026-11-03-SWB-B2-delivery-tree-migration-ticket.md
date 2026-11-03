# SWB-B2 · 迁移施工票：交付面搬家（bundle＋六技能包 git mv＋PRODUCT/ARCHITECTURE→docs＋门禁扫描根同批随动）（施工票·L2·架构席起草）

- 起草实测 HEAD：`b5fd2b4`（B1 票面笔）；开工 ANCHOR＝开工实测 HEAD 应为 B1 施工收口笔或其后可达后继（B1 未收口不得开工本票），读数附回执开端。
- 施工基线真源＝方案 v3（B0 冻结态）§三表现位行＋§五 B2 行；D6 既裁＝git mv 保留历史＋**开工先打迁移前 tag `archive-pre-B2-<YYYYMMDD>`**＋fuxi 线小规模预演先行（预演目见 B2-A0）。
- **开工附注三项（B0 登记照录）**：①誊写禁令（裁定 `f5a0d96`）：本票全部搬家＝`git mv`（rename 检测保持历史）；判据＝「新位与原位 diff＝空（字节一致）」（本票无剥壳段，剥壳段申报＝恒 0）；②票面落位 `.scratch/tickets`（本票自身已在位）；③era 跨仓口径（不在本票，见 ESC1）。
- 计数口径＝occurrence；判据自带落盘；负例 exit≠0。读数锚 HEAD=`b5fd2b4`（起草实测）。

## 现盘基线读数（起草实测·对账用）
- `git ls-files deliverables/ | wc -l` ＝ **198**；分桶＝bundle 88／external-advisor-collab 7／multi-collab 10／object-audit 40／object-build 9／bundle-assembly-registration 6／fuxi-skill 37／deliverables/README.md 1。
- run-gates 现挂接＝`.git/hooks/pre-commit`（install-hooks.sh 生成·绝对路径指 `deliverables/skills/object-audit/scripts/run-gates.sh`）。

## 声明闭集（本批唯一可写面·目录级申报）
- 声明闭集：
- deliverables/experts/baigong-software-team/（git mv 源整树→agent-experts/baigong-software-team/）
- deliverables/skills/external-advisor-collab/（git mv→agent-skills/同名）
- deliverables/skills/multi-collab/（git mv→agent-skills/同名）
- deliverables/skills/object-audit/（git mv→agent-skills/同名）
- deliverables/skills/object-build/（git mv→agent-skills/同名）
- deliverables/skills/bundle-assembly-registration/（git mv→agent-skills/同名）
- deliverables/skills/fuxi-skill/（git mv→agent-skills/同名）
- deliverables/README.md（git rm·表并入仓根 README 归 B5·本批删除并在回执登记待并入行）
- agent-experts/baigong-software-team/bundle.lock（`path` 键值随动）
- agent-skills/object-audit/scripts/run-gates.sh（GATES_MD 候选序＋仓根探针随动）
- agent-skills/object-audit/scripts/check-pointers.py（DEFAULT_SCOPE/根探针/候选层随动）
- agent-skills/object-audit/scripts/check-pointer-closure.py（DEFAULT_PKG_FACES 随动）
- tools/check-source-of-truth.py（spec_file 头块锚＋用法注释路径随动）
- agent-experts/README.md／agent-skills/README.md（B1 名录行随动补「交付面已迁入」态）

## 逐条施工规格

### B2-A0 fuxi 预演目（D6 既裁·先行独立小步）
`git mv deliverables/skills/fuxi-skill agent-skills/fuxi-skill`（单独一笔）→ 判据 4 rename 断言跑绿后方可续 B2-A1；不成即 `git revert` 该笔呈核，不硬推。

### B2-A1 六包余五包＋bundle git mv
1. `git mv deliverables/skills/<五包> agent-skills/`（逐包名对应）。
2. `git mv deliverables/experts/baigong-software-team agent-experts/`。
3. `git rm deliverables/README.md`。
4. 壳位规则（防与 B1 壳撞）：mv 目标父目录内**不得已有同名子目录**——B1 只建了壳的 `.collab/docs` 内层（agent-experts/baigong-software-team/{.collab,docs} 已存在）！故 bundle mv 改形＝**内容注入式**：`git mv deliverables/experts/baigong-software-team/<逐项>` 十一项（agents avatars bundle.lock config hooks plugin.json settings.json skills tests README.md＋PRODUCT.md ARCHITECTURE.md 见 B2-B）入壳；六技能壳无此问题（B1 仅建 .collab/docs 壳于 agent-skills/<pkg>/ 下）——**同规则适用**：逐 git mv 包内项入壳，禁整目录替换。回执登记逐笔。
   - 注：`git mv <文件> 壳/` 逐件保 rename 历史成立（字节零动·誊写禁令合规）。

### B2-B PRODUCT/ARCHITECTURE→docs（v3 §三 L57＋§二点八既裁）
`git mv agent-experts/baigong-software-team/PRODUCT.md agent-experts/baigong-software-team/docs/PRODUCT.md`；ARCHITECTURE.md 同式。引用锚随动＝bundle README 索引行/README「出身」节外无声明面（plugin.json 未声明此两件＝v3 L64 既核）；随动逐处入回执。

### B2-C 门禁扫描根同批随动（缺则本批 GATE 必红＝同批硬随动）
1. `check-pointers.py`：`DEFAULT_SCOPE = ("deliverables",)`→`("agent-experts","agent-skills","softwares")`；根探针 `isdir(cur/"deliverables")`→`isdir(cur/"tools") and any(isdir(cur/c) for c in ("agent-experts","agent-skills","softwares"))`；候选层 `root/"deliverables"`/`root/"deliverables"/"skills"`→三层分类目录候选（`root/<分类>/<rel>`＋`root/<分类>/<pkg>/<rel>` 保持跨包短写法可解析）；infra error 文案同步。
2. `check-pointer-closure.py`：`DEFAULT_PKG_FACES = ("deliverables/skills/external-advisor-collab", "deliverables/experts")`→`("agent-skills/external-advisor-collab", "agent-experts")`。
3. `run-gates.sh`：GATES_MD 候选序改 `$ROOT/agent-skills/multi-collab/references/60-gates.md` 前置（旧两候选删）；仓根探针同 1 改。
4. `bundle.lock` L7 `"path"` → `"agent-experts/baigong-software-team"`。
5. `tools/check-source-of-truth.py`：头块 spec_file 锚 `deliverables/experts/...`→`agent-experts/...`；L104–107 用法注释路径随动。
6. 钩子再生（不手改）：`bash agent-skills/object-audit/scripts/install-hooks.sh` 重生成 `.git/hooks/pre-commit`（回执附生成前后两读数）。
7. **不在本批**＝check-ticket-reconcile（.collab 票目录未迁·B4 改造）、check-collab-lint spec 锚（指 .collab/tickets·B3a/B4 域）、60-gates/SKILL.md 等规范叙述内旧路径史述面（回执分账史述不改·活引用清零断言见判据 3 豁免史述口径）。

## 验收判据（全部机械可判·自带落盘·负例 exit≠0）
1. **双向对账清零**：迁前基线 198（本票首段）→ `git ls-files agent-experts/ agent-skills/ | wc -l` ＝ **197**（198−1 删 deliverables/README.md）＋`git ls-files deliverables/ | wc -l` ＝ **0**；分桶＝agent-experts 87（88−2 mv docs＋…按逐件回执对账表核）／agent-skills 109（含 STRUCTURE.md 1＝B1 生成→**110** 对账口径以回执逐桶表为准，判据式＝Σ新桶−B1 壳件＝197）。
2. **rename 字节一致断言（誊写禁令判据）**：本批 commit `git show -M --name-status > $B2_TMP/c2.out`：R 行占比＝mv 件 100%（R100 全等·无 A/D 例外除 bundle.lock 等 5 件随动文件申报）；对 mv 抽样 10 件 `git diff <笔>^:<旧> <笔>:<新> | wc -l` ＝ 0（字节一致）。
3. **活引用清零（史述豁免制）**：`grep -rno "deliverables/" agent-experts/ agent-skills/ tools/ --include='*.py' --include='*.sh' --include='*.json' | grep -v "<史述豁免清单>" | wc -l`＝**0**（豁免清单＝回执逐处人工分账史述行·先例＝T07-B 乙账形态）；负例＝任一非豁免命中 exit 1。
4. **门禁零回归**：开工基线首跑（B2-A0 前）落盘 c4-base → 每笔后 `bash agent-skills/object-audit/scripts/run-gates.sh --root . > $B2_TMP/c4.out 2>&1` → GATE PASS exit 0 且零新增族。
5. **六演练回归**：`T06_TMP="$B2_TMP" bash agent-experts/baigong-software-team/tests/acceptance/drills/drill-runner.sh > $B2_TMP/c5.out 2>&1` → exit 0 且 `SIX_DRILLS_GREEN` occurrence=1。
6. **版本账随动**：bundle 不入代码性变更？——mv＋bundle.lock path 改＝交付面变更→**三同源 bump 0.1.16→0.1.17**＋README append-only 追加行（依 F7/纪律①·回执前后读数）。
7. **tag 在册**：`git tag -l "archive-pre-B2-*" | wc -l` ≥1（D6 既裁对位）。

## 禁动面
- `.collab/` 全域（除回执）、`docs/`（旧仓根）、仓根 README（B5）、`.gitignore`（B1 已增补块·本批不再动）、六包与 bundle 内**非随动清单文件**内容零触碰（mv 字节零动）、`tools/` 除 check-source-of-truth 外五件零触碰、`agent-*/` 壳的 .collab/README 与 docs/STRUCTURE.md 零触碰（B1 成品）。

## 候裁点
无（名录/落位/版本线均既裁；PRODUCT/ARCHITECTURE 落 docs 既裁）。

## 票间关系
- 前置：B1 收口（壳与 STRUCTURE 在位）。后置：B3（过程域搬家·票面 E-ARC-1′ 换锚先行）；B4（check-ticket-reconcile/票目录改造＋R⑧⑨精化·依赖 B2 新路径为基）。

## 回执
落 `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-SWB-B2-receipt.md`（新桶首件·回执随新落位）：开端 HEAD＋逐笔 name-status＋逐桶对账表＋判据 1–7 读数＋史述豁免清单。交付笔单独 commit（`collab:` 前缀·B2-A0 预演笔单走）；禁 `--no-verify`、禁 amend。
