# PUB-EXCL · 施工票：publish.py 装配面过程域排除口径（实装票·L2·架构席起草·装配器维护类）

- 起草实测 HEAD＝`841c3ec`（换钉批 QA 独立验证放行笔）；开工 ANCHOR＝开工实测 HEAD ≥ `841c3ec`，读数附回执开端。
- 决策依据＝皮总 2026-11-05 01:07 原话「按你的推荐，补」（补排除口径）；条款根基＝皮总拍板㊻写权闭集＋㊺交付物纯度（过程件不入交付面）；装配面定性＝部署先行预览面（`agent-experts/baigong-software-team/skills/software-orchestration/references/deploy-gate.md` §五），未来整面复制进市场源注册——过程域混入＝交付面污染。
- 背景链（今日实测）：治理层换钉批（`62f0043`/`fef5dbc`）后装配段重跑成功（exit 0·装配面＝仓外 `D:\multi-agent-collab-devkits-build\baigong-software-team\`）；QA 放行报告＝`agent-experts/baigong-software-team/.collab/qa/2026-11-04-换钉批-QA独立验证-v1.md`。
- 计数口径＝occurrence；判据自带落盘重定向；负例 exit≠0。
- 本票只定义施工与验收；起草席零落改（本票面即本批唯一过程件产出）。

## 一、问题实证（起草取证·回执附开工复测）

### 1.1 排除口径现状（直读 `agent-skills/object-build/scripts/publish.py`·实测行位）

装配取源两条路径共用**唯一取料函数** `git_archive_blobs()`（def L707，调用点两处：L862 bundle 本体面、L871 每一组件 git archive 解出面）。现存过滤点：

| 位 | 现文（实测逐字） | 辖域 |
|---|---|---|
| L727-728（`git_archive_blobs` tar 成员层） | `if "__pycache__/" in rel or rel.endswith(".pyc"):` → continue | 两条取料路径共用（编译缓存件） |
| L861-864（`do_assemble` 本体复制循环） | `body_exclude = {LOCK_FILENAME, STATE_FILENAME, ASSEMBLY_MANIFEST}` ＋ `rel.startswith(LOCK_FILENAME + "/")` | 仅 bundle 本体（三元数据＝索引件/同步账本/装配全账） |

**无任何 `.collab`/`.scratch` 排除条款**——两条取料路径皆无。

### 1.2 装配面现形态读数（`D:\multi-agent-collab-devkits-build\baigong-software-team\` 只读实测）

| 量 | 读数 | 口径 |
|---|---|---|
| 装配面文件系统总文件数 | **664** | `find . -type f \| wc -l` |
| 装配计划文件数（ASSEMBLY.manifest.json `"files"`） | **662** | 664 ＝ 662 ＋ COPY.state ＋ ASSEMBLY.manifest.json（账本/元数据两件不在 plan 内） |
| 过程域文件（路径段恰为 `.collab` 或 `.scratch`） | **552** | 段匹配实测＝`.collab` 段 488 ＋ `.scratch` 段 64 |
| 其中 bundle 本体面 | `.collab` 472 ＋ `.scratch` 53 ＝ 525 | 源仓 `git ls-tree -r HEAD agent-experts/baigong-software-team` 同口径核对 |
| 其中 EAC 组件子树（装配面 `skills/external-advisor-collab/`） | `.collab` 16 ＋ `.scratch` 11 ＝ 27 | ref 树 `git ls-tree -r external-advisor-collab@v1.1.2 agent-skills/external-advisor-collab`＝35 条目含 27 过程域 |
| 其中 deep-research 组件子树 | 0 | 装配面 `skills/deep-research/`＝11 文件全交付 |

> 更正任务背景一处表述：「bundle 本体面 `.collab/` 488 件」不确——488＝两路径 `.collab` 段合计（本体 472 ＋ EAC 树 16）；`.scratch` 合计 64（本体 53 ＋ EAC 树 11）。552 总数吻合。

### 1.3 病灶补强（起草实测）

- 装配面 662 plan 文件中 552（83.4%）为过程域——未来整面复制进市场源＝把两仓治理流水（裁决记录/QA 报告/历史票面/外部素材快照）整体交付给注册用户。
- 现盘无一段落既含 `.collab`/`.scratch` 子串又非该段名（`find … | tr '/' '\n' | grep -E "\.collab|\.scratch" | grep -vx "\.collab|\.scratch"` ＝空）→ 段匹配与子串匹配现盘同读数，选**段匹配**为规格（语义精确、防未来误伤如 `.collabfoo/`；名为 `.collab` 的文件级同规则排除，现读数＝0，且与 `object-build/references/60-publish.md` §九 「`.` 开头条目不可发布」既有约定同向）。
- `.codebuddy-plugin/plugin.json` 段名非 `.collab`/`.scratch`——排除口径天然不触注册面主文件（该文件＝装配账 `source:`/`copy:` 锚，见 publish.py L769-771，不得误伤）。

## 二、目标（一句话）

重装配后的装配面只剩注册态交付件：过程域（`.collab`/`.scratch` 路径段）零入面，且既有排除与幂等/漂移停纪律零回归。

## 三、实装规格（写死·可机械验证）

### 3.1 过滤点择定＝tar 成员层（解出后落盘前），非 git archive pathspec 层

择定理由（三条，回执须逐条对应）：
1. **单点覆盖两条取料路径**：`git_archive_blobs()`（L707）是 L862 本体面与 L871 组件面共用取料口——成员层过滤一处实装，两路径自动同规则（本体面经 L862 同函数进，故无需在 L863 `body_exclude` 处重复实装）。
2. **语义精确位**：该点 `rel` 已剥前缀＋反斜杠归一（L720-726），段匹配判据在此最干净。
3. **不用 pathspec 排除层**：`git archive` 对 `:(exclude)` 魔数支持跨版本不稳；且若给 archive 追加多 pathspec，L730-733「取源路径下无文件 ⇒ exit 3」的空结果校验语义会被排除项扭曲（组件只剩过程域时现应 exit 3 报警，pathspec 法会静默出空）——成员层法保住该校验原语义。

### 3.2 逐位施工（行位以开工实测为准，以下为起草实测锚位）

**落点一：`agent-skills/object-build/scripts/publish.py` L727-728 后追加（`git_archive_blobs` 内，`result[rel] = …` 之前）**

现文（锚）：
```python
        if "__pycache__/" in rel or rel.endswith(".pyc"):
            continue  # 编译缓存件不入装配面
```
追加：
```python
        if any(seg in (".collab", ".scratch") for seg in rel.split("/")):
            continue  # 过程域段不入交付面（PUB-EXCL·皮总 2026-11-05「补」·㊺交付物纯度）
```
语义＝`rel` 按 `/` 切段，任一段**恰等于** `.collab` 或 `.scratch` ⇒ 跳过（非子串匹配）。两条取料路径同函数自动同覆盖；`.codebuddy-plugin` 段不命中＝注册面零误伤。

**落点二：`agent-skills/object-build/SKILL.md` frontmatter `version: 0.5` → `version: 0.6`**

**落点三：仓根 `README.md` 版本账 object-build 行（起草实测 L40）`v0.5` → `v0.6`**（版本账同源＝SKILL.md frontmatter 人工对账，无门禁咬合；随动理由见候裁①）

汇总：产出文件数＝**3**；与预算一致，超出即停手。

> object-build 包**无** `references/90-changelog.md`（实测 references/＝10/15/20/40/50/60 六件）——「changelog append」体例在 EAC 包，不在本包，本票闭集不含 changelog。

## 四、边界

做什么：publish.py 成员层排除实装＋object-build 版本随动两点。
不做什么／禁改清单：**bundle.lock、全部 tag（尤其 `external-advisor-collab@v1.1.2`/`v1.1.1`）、百工 bundle 内容面（`agent-experts/baigong-software-team/` 全树）、门禁族（tools/＋agent-skills/object-audit/scripts/check-*）、FUXI 账域（agent-skills/fuxi-skill/）零触**；60-publish.md 条文不动（见候裁③）；`git_clean_or_die` docstring（L673-677）不动（其「未跟踪文件不进装配面」陈述仍真，见候裁④）；`body_exclude` 三元数据排除不重构不搬家。

## 五、输入件（路径逐件）

- `agent-skills/object-build/scripts/publish.py`（读 L643-654 装配段纪律注释＋L707-734 `git_archive_blobs`＋L858-878 取源计划段：改点与既有排除锚位）
- `agent-skills/bundle-assembly-registration/references/10-assemble.md`（读 §四取件顺序＋§五产物核对＋§六「删装配面重跑」唯一处置：验收工序依据）
- `agent-skills/bundle-assembly-registration/SKILL.md`（读 §五 C1–C10 出口判据表：验收对齐）
- 本票面（判据钉值表）

## 六、产出件（写域闭集）

- 修改：`agent-skills/object-build/scripts/publish.py`（§3.2 落点一）
- 修改：`agent-skills/object-build/SKILL.md`（version 0.5→0.6）
- 修改：`README.md`（版本账 object-build 行 v0.5→v0.6）
汇总：产出文件数＝3。

## 七、验收判据（每条可跑·钉值来自起草实测）

前置工序（非改动·装配面纪律④允许）：**先整删 `D:\multi-agent-collab-devkits-build\baigong-software-team\` 再重装配**。理由（写死防走捷径）：装配器无「删不在计划内的旧文件」步——不删旧面重跑，552 旧过程件会成孤儿留盘，判据 2 必假红；「删装配面重跑」＝10-assemble.md §六既有唯一处置，幂等复跑判据（判据 4）阶段不再删。

| # | 判据 | 命令口径 | 钉值 |
|---|---|---|---|
| 1 | 重装配成功 | `python agent-skills/object-build/scripts/publish.py --assemble "D:/multi-agent-collab-devkits/agent-experts/baigong-software-team"` | exit 0 |
| 2a | 过程域零入面 | 装配面根 `find . -type f \| awk -F/ '{for(i=2;i<=NF;i++) if($i==".collab"\|\|$i==".scratch"){print;break}}' \| wc -l` | **0** |
| 2b | 装配面文件总数 | `find . -type f \| wc -l` | **112**（＝110 交付＋COPY.state＋ASSEMBLY.manifest.json） |
| 2c | 装配全账计数 | ASSEMBLY.manifest.json `"files"` | **110**（＝662−552） |
| 2d | 账本末块行数 | `COPY.state` 末块 `^[0-9a-f]{64} ` 行数 | **110** |
| 3a | EAC target 非空＋交付计数 | `find skills/external-advisor-collab -type f \| wc -l` | **8**（枚举＝SKILL.md／docs/STRUCTURE.md／references/{10-roles,20-rounds,30-discipline,40-artifacts,90-changelog}.md／sources/spec-anchors.md；与 ref 树 35−27 互证） |
| 3b | deep-research target 非空＋计数 | `find skills/deep-research -type f \| wc -l` | **11**（零过程域，前后不变） |
| 4 | 幂等复跑 | 同判据 1 命令再跑一次 | exit 0 且输出含「零写入」 |
| 5a | 既有排除不回归 | 装配面 `find . -type d -name "__pycache__"`＝0；`find . -name "*.pyc"`＝0；装配面无 `bundle.lock` | 三读数为零/不存在 |
| 5b | 注册面主文件仍在 | `test -f .codebuddy-plugin/plugin.json` | exit 0 |
| 5c | 三元数据在位 | 装配面根存在 COPY.state＋ASSEMBLY.manifest.json | 两件均在 |
| 6 | 语法闸 | `python -m py_compile agent-skills/object-build/scripts/publish.py` | exit 0 |
| 7 | 工序出口判据 | 按 `bundle-assembly-registration/SKILL.md` §五 C1–C10 全表跑 | C1–C7 全绿（C8–C10 属注册段＝本票射程外，不跑不记） |

**计数随动声明（起草实测）**：C1–C10 与 10-assemble.md §五产物核对表全部为**相对等值断言**（装配全账计数 vs 装配面非元数据计数 vs 末块行数），无裸 662/552 引用；全仓交付面（agent-skills/＋agent-experts/ 交付段）grep `662`/`552` 无工序文案命中（命中仅存于过程域票面与外部素材快照，不在射程）。→ 判据文案零随动，钉值由本票 §七 承载。

## 八、负样本（每条配一句）

1. 判据 1 不过 → 装配器报错停（exit≠0）＝实装改坏取料路径。
2. 判据 2a 不过 → 装配面仍见 `.collab/`/`.scratch/` 目录＝过滤条件未命中（段匹配写成了子串漏写或加错函数）。
3. 判据 2b/2c/2d 不过 → 计数互不相等或 ≠110/112＝排除范围过宽/过窄或旧面未删净。
4. 判据 3a/3b 不过 → 组件 target 空或计数漂＝误伤了交付件（排除条件越界）。
5. 判据 4 不过 → 复跑追加新块/重写文件＝幂等短路被排除改动破坏。
6. 判据 5a 不过 → `__pycache__`/pyc/`bundle.lock` 重现＝既有排除回归。
7. 判据 5b 不过 → plugin.json 缺失＝排除误伤注册面，装配账 `source:` 锚断。
8. 判据 6 不过 → 语法错＝笔误级，未落改即修。

## 九、停止条件（遇此停手上报，不自行处理）

歧义：段匹配 vs 子串匹配若现盘出现新段落含子串非段名（开工复测 §1.3 命令重跑非空）→ 停手上报；越界：需改禁改清单任何一件；依赖缺失：`git_archive_blobs` 结构已与 §3.2 锚文不符（如已另有人改）→ 停手上报。

## 十、回滚

git 层面：`git revert <本批笔>`（三件同笔，单 revert 全撤）。数据层面：装配面＝派生产物非真源（纪律④），回滚后旧工具重装配即复原（含 662 旧读数）；两 tag／lock 未触＝无数据回滚面。无不可回滚步骤。

## 十一、预算

改文件 ≤3｜改行 ≤10（publish.py +2／SKILL.md ±1／README ±1）｜步骤 ≤8（删面→施工→py_compile→装配→计数判据→幂等复跑→回归判据→回执）。

## 十二、候裁清单（单列·票面不自行裁决）

1. **README 版本账行随动**：object-build 行 v0.5→v0.6 已列入闭集落点三（与 SKILL.md frontmatter 同源对账）；若裁「仓根版本账只记 bundle 不记工具包」，则落点三撤出闭集、改数＝2。
2. **排除纪律是否成文入 `bundle-assembly-registration/references/10-assemble.md`**（§三纪律表或 §五补一行「过程域段不入装配面」＋该包 version 0.1 bump）：本票否动（改动面最小化）；判据文案实测无需随动，纪律条文补写候后批独立裁定。
3. **publish.py 是否为新条款挂 spec-provenance 块**：新条款在 60-publish.md 无对应条文；挂块需先给 60-publish.md 补条文＝闭集扩至 object-build references（本票否动）；现以代码注释标来历（PUB-EXCL＋拍板时刻），候后批随 60-publish.md 条文一并挂锚。
4. **`git_clean_or_die` docstring L675「未跟踪文件（各仓 .collab/ 治理流水常态）根本不进装配面」**：本批后该陈述仍真（讲的是未跟踪文件），但读者易误读为「.collab 一律不进」；本票否动（不为防误读扩面），登记候裁。

## 十三、开工复测清单（回执开端必附）

1. `git rev-parse --short HEAD`（≥`841c3ec`）。
2. publish.py L727 现文逐字命中 §3.2 锚文。
3. 装配面 664/662/552 三读数复测（§1.2 口径）。
4. §1.3 子串-非段名段落实测＝空（若非空＝触发停止条件歧义条款）。
