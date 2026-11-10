# SWB-SCRATCHG · .scratch 族忽略规则与存量债治理规格票（v1·纯规格·零施工）

- 票号：**SWB-SCRATCHG**
- 票名：**.scratch 族忽略规则与存量债治理规格票**
- 票型：规则票（八类取一·修票权＝提案席位＝架构席）
- 起草席：架构席 `arch-scratchg1`
- 开端读数：ANCHOR＝`329d16c67b31ed8b238fa33c236e054fedacc6ad`（开工实测 2026-11-10 19:01:12 +0800）；`git status --porcelain --untracked-files=no` 读数＝tracked 面 1 项他案在飞登记照登不碰＝`A "agent-skills/fuxi-skill/.collab/tickets/2026-11-10-FUXI-FX-U38起草回执-v1.md"`（FUXI-U38 起草回执 staged·链上他案笔零触碰）
- 前置票：无（TMP-DISC 批 2026-11-05 既成纪律＝本票口径输入，非前置施工票）
- 候裁点：**单列 §七 六条·起草席不自行拍**

> **票面自注（落位悖论自陈）**：本票面自身落在本票治理对象（`.scratch` 族）之内——照近期体例落位（票面落位＝`.scratch/tickets/`·裁定 `f135855` 在册），方案甲规则族以 tickets 桶负向豁免行覆盖本件，落位与规则自洽。

---

## 一、开工实测读数（起草轮·全部现跑·occurrence 口径＋双验）

| 项 | 命令 | 实测读数 |
|---|---|---|
| 时点 | `date` | `Tue Nov 10 19:01:12 2026`（开工首步） |
| HEAD | `git rev-parse HEAD` | `329d16c67b31ed8b238fa33c236e054fedacc6ad`（＝主理人 19:00 侧读数全等） |
| tracked 面 | `git status --porcelain --untracked-files=no` | 1 行＝FUXI-U38 staged（照登不碰，见票头） |
| tracked .scratch 复点① | `git ls-files \| grep -c '/\.scratch/\|^\.scratch/'` | **109**（＝主理人现值全等） |
| 起草中链漂移 | `git rev-parse --short HEAD`（复点时刻） | `14416e9`（起草期间他案落链，见注） |
| tracked .scratch 复点② | `git ls-files -z \| tr '\0' '\n' \| grep -c '/\.scratch/\|^\.scratch/'` | **136**（链漂移后新值；桶表见 §二.1） |
| 未跟踪 .scratch 条目 | `git status --porcelain \| grep '^??' \| grep -c '\.scratch/'` | **199**（双验：仓根不带引号 163＋仓根带引号 2＋百工包内 30＋fuxi 包内 4＝199 ✓） |
| 未跟踪全仓条目 | `git status --porcelain \| grep -c '^??'` | **208**（＝.scratch 199＋非 .scratch 散件 9；主理人现值 ≈209＝同口径微漂，如实登记） |
| 未跟踪文件级展开 | `git status --porcelain --untracked-files=all \| grep '^??' \| grep -c '\.scratch/'` | **102358**（文件级 occurrence 口径；主体＝仓根 `.scratch/` 下姊妹仓镜像目录副本两枚，见 §二.4 观察 O-2） |
| 现行忽略态三样本 | `git check-ignore -v .scratch/TMPLRULE-eng agent-skills/fuxi-skill/.scratch/FX-U26 agent-experts/baigong-software-team/.scratch/COLLAB-STRUCT-1` | **exit 1**（三样本均未忽略＝主理人实测复核全等） |
| .gitignore 现文 | `grep -in scratch .gitignore` | 仅 L3/L13 两条**注释行**含 scratch 字样，**零生效规则**（复核全等） |

**链漂移注**：起草窗内（19:01→复点时刻）HEAD 由 `329d16c` 漂至 `14416e9`，仓根 `.scratch/tickets/` tracked 数由 10 增至 37（SEMGV 线／PROJINIT／GWP-DEPLOY 票面他案落链所致）。此即多席共用仓根票目录的实况登记，供 §七候裁(b) 并发面参考；两值均如实登记，施工开工以施工席当轮再实测为准（V0）。

## 二、现盘事实（起草轮实测·施工输入）

### 2.1 tracked .scratch 存量桶表（复点②口径 136 件）

| 桶 | tracked 件数 | 其中 tickets 桶 | 非 tickets 桶 |
|---|---|---|---|
| 仓根 `.scratch/` | 37 | 37 | 0 |
| `agent-experts/baigong-software-team/.scratch/` | 67 | 66 | **1**（点名＝`.scratch/COLLAB-STRUCT-1/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md`） |
| `agent-skills/fuxi-skill/.scratch/` | 21 | 21 | 0 |
| `agent-skills/external-advisor-collab/.scratch/` | 11 | 11 | 0 |
| 其余（softwares 等） | 0 | 0 | 0 |
| **合计** | **136**（双验＝37+67+21+11+0 ✓） | **135** | **1**（双验＝136−135 ✓） |

（开工复点①＝109 与复点②＝136 的差值全部来自链漂移期的他案开票笔，桶表按复点②现盘现跑生成。）

### 2.2 .gitignore 现行体例（真源＝仓根 `.gitignore` 全文 66 行）
结构＝头部注释（L1–L10·治理原则 2026-10-22 皮总拍「是否进 git 由本文件显式声明」）＋制①入库面注释（L12–L15·含「项目 .scratch/tickets/」默认入库存述）＋制②排除面（L17–L54：嵌套 `.collab` 运行流水桶七行＋仓根层级显式防护行七行＋research 负向防御两行＋第三方外部快照三桶及配套负向）＋系统杂物/工具产物（L56–L66）。**历史判例引用行号在册**＝链上史笔引用 `.gitignore:17`、`.gitignore:20`（FUXI S0c/T9 判据件），任何插入不得移动 L1–L54 行号。

### 2.3 关键机理实证（起草轮现跑·防误判写实）
1. **忽略规则不影响已跟踪文件**：对 tracked 非 ticket 件跑 `git check-ignore -q`（缺省口径）＝exit 1（被 index 挡回，不报忽略）；加 `--no-index` ＝exit 0（规则命中）。即 `git grep`／`git log`／`git diff`／门禁对 tracked 件的扫描行为在忽略规则落地后**零变化**——忽略只管未跟踪可见性（status/add），不管已跟踪扫描。判据式样本读数已钉 §五 V4。
2. **现行门禁均不经 `git status` 读 .scratch**：`share/check-ticket-reconcile.py` 按文件系统枚举 `.scratch/tickets/` 双候选目录（缺省票目录口径）、`share/check-entity.py` 遍历时显式剪除 `.scratch` 目录、`share/check-pointers.py` 后缀路径索引显式除外 `.scratch/` 族（D-94 口径 L188–L200）；`share/run-gates.sh` 及 share 脚本族零 `rg` 调用（grep 文件扫描不吃 gitignore）。→ 忽略规则落地对上述门禁**零行为差异**。
3. **规则族已隔离探针验证**：起草轮以 `git -c core.excludesFile=<探针文件>` 覆盖式探针跑真仓路径（`.gitignore` 零触碰·探针目录用毕已删零残留），§五 V1–V3 全部预期读数＝探针实测读数，非推演。

### 2.4 观察登记（不归本票射程·随注）
- O-1：仓根未跟踪非 .scratch 散件 9 枚（含 `.py`、`.scratch_wbdocs.html`、`assert-modified-run2.txt`、仓根 `.collab/research/` 下六枚产品席在途件等）＝非 .scratch 族，不入本票射程，卫生归 TMP-DISC 纪律面。
- O-2：仓根 `.scratch/multi-agent-collab-experts/`、`.scratch/multi-agent-collab-skills/` ＝姊妹仓镜像目录副本（文件级 102358 枚主体）。TMP-DISC §八.2 口径「跨仓对拍各落各自仓 `.scratch/` 内」——此两枚系该纪律生效日（2026-11-05）前后既有存量，按工单规范 T1 新规时间效力条款不追溯；方案甲落地后其 git 面自动消隐，盘占清理归仓卫生面另裁。

## 三、目标（票体四字段①）

终态一句话＝**`.gitignore` 立 .scratch 族生效忽略规则（tickets 票面桶负向豁免），tracked 存量按机械分流判据处置至「.scratch 族内 git 面只剩 tickets 桶」，链上历史判据读数零翻面**。

背景口径（决策者 2026-11-10 18:58 裁定原文）：「.scratch 不进 git 是应该定义在 .gitignore 的，目的就是各种临时开发调试的东西往里面塞。」＝目标态＝`.gitignore` 立生效规则、`.scratch` 族作为临时开发调试落位区。现盘双重冲突＝①无生效规则（仅注释行）＋②tracked 存量 136 件已入库（含刻意留档票据，不能一刀切 `git rm --cached`）。

## 四、规格（票体四字段②·逐条到落位·纯规格零施工）

### 4.0 方案选型总述（候裁(d) 挂钩）

- **方案甲（本票推荐）**：.scratch 族整体忽略＋tickets 桶四行负向豁免。存量 135 件票据**零迁移零脱跟踪**；与既有裁定 `f135855`（票面落位＝`.scratch/tickets`）、README 仓根白名单表 `.scratch/tickets/` 行进 git 行、`check-ticket-reconcile.py` 缺省票目录口径三处现制**全部兼容零随动**。
- **方案乙（对照登记）**：族整体忽略（含 tickets）＋135 件票面迁合规桶（如各项目 `.collab/tickets/`）。代价面＝票面落位裁定翻案＋check-ticket-reconcile 票目录口径改造＋README 白名单表随动＋T9 档位3 措辞随动＋封口条款连锁（新落件引用旧落位字样违例面扩大）。射程波及 fuxi/EAC 他案面＝§七候裁(c) 成真。
- 以下 S1–S3 按**方案甲**成文；若裁乙，本票 S1 之后全部作废重出 rev，不得现场混合。

### 4.1 S1 · .gitignore 规则规格（精确到行）

插入落位＝现行 L54（第三方快照配套负向组尾行·REFERENCE-SOURCES 配套行）与其后空行之后、现行 L56 `# ── 系统杂物／工具产物（旧 L47–L56 随迁）──…` 节头之前——即制②排除面尾部新增一节。**选位依据**＝L1–L54 行号零移动（链上史笔引用 `.gitignore:17`/`.gitignore:20` 读数可读性保住，见 §2.2）＋制②内容连续性（.scratch＝过程/临时族，归制②不归杂物节）。

插入块＝**九行**（三注释行＋六规则行·逐字真源如下围栏·施工逐字照录）：

```
# ── .scratch 族（制②补充·SWB-SCRATCHG·决策者 2026-11-10 裁定：.scratch 不进 git 定义在 .gitignore）──
# 临时开发调试落位区整体排除；唯一豁免＝票面桶 .scratch/tickets/（票面真源落位·裁定 f135855 体例承接）。
# 体例承制②「嵌套桶级＋仓根显式」双形态配对；机理＝忽略只管未跟踪可见性，已跟踪件扫描行为零变。
/**/.scratch/*
/.scratch/*
!/**/.scratch/tickets/
!/**/.scratch/tickets/**
!/.scratch/tickets/
!/.scratch/tickets/**
```

行义注记（不入库·仅本票在册）：第 4 行＝任意层级 .scratch 直接子项忽略（含仓根，gitignore 中「/前缀＋`**/`＋/」匹配零或多级目录）；第 5 行＝仓根层级显式防护行（体例承 L30–L36 组）；第 6–9 行＝tickets 桶两级负向豁免（目录行＋内容行成对，先例＝L52–L54 配套负向体例）。`git check-ignore -v` 对仓根样本命中末行可能显示负向行（末匹配取胜），**退出码闭集才是判据**（V1 钉值按 `--no-index` 口径写死）。

与现行 `__pycache__/`、`*.pyc` 行交互：`.scratch/tickets/__pycache__/x.pyc` 类文件仍被后置既有规则忽略（探针实证 exit 0）＝票面桶内编译缓存不借豁免还魂，无需额外行。

### 4.2 S2 · 存量 136 分流判据族（可机械·按桶给·判据不硬编码清单）

分流判据＝**路径判据 ∧ 内容类型判据** 两级机械式：

- **类A 保留跟踪（判据：路径 ∈ `.scratch/tickets/` 桶）**：路径含 `/.scratch/tickets/` 段（或仓根 `.scratch/tickets/` 前缀）者＝刻意留档票据面，随 S1 负向豁免行保留跟踪，**零动作**。落桶读数（复点②）：仓根 tickets 37／百工 66／fuxi 21／EAC 11＝135 件全落类A，四桶全部**零施工**。历史留档形态之争＝候裁(d)，方案甲默认「留 .scratch＋负向规则」。
- **类B 脱跟踪（判据：路径 ∈ .scratch 族 ∧ ∉ tickets 桶 ∧ tracked）**：落桶读数＝**恰 1 件**（点名见 §2.1，作为开工输入而非判据本体）。处置二式（**取态归候裁(e)**，施工席按裁定逐字执行，未裁不得施工）：
  - B-i 迁合规桶：`git mv` 至所属项目 `.collab/receipts/`（该件内容类型＝施工回执＝案卷类，TMP-DISC 回执落点体例对口），迁移后 git 面 .scratch 族只剩 tickets 桶；
  - B-ii 就地脱跟踪：`git rm --cached -- <路径>`（文件留盘、被忽略规则覆盖、历史可追溯、不 revert）。
- **类C 未跟踪存量（判据：`git status --porcelain` `??` 面 ∩ .scratch 族）**：S1 落地后自动消隐（git 面不再可见），**零 git 动作**；盘面清理归 TMP-DISC §八.3 收口清理判据（各票收口自清）＋§2.4 O-2 姊妹仓镜像副本随注另裁——本票不做批量删除（禁动面 §4.5）。
- **按桶落判据总表（复点②口径）**：仓根 37＝37 类A／0 类B；百工 67＝66 类A／1 类B；fuxi 21＝21 类A／0 类B；EAC 11＝11 类A／0 类B。合计 136＝135 类A＋1 类B（双验 ✓）。**方案甲下 fuxi 21／EAC 11 两桶全部落类A＝零处置**——他案面存量射程之争（候裁(c)）在方案甲读法下自动消解为「无需处置」，若裁乙则该争点复活（见 §5.2）。

### 4.3 S3 · 他案判据面联动评估（写实·翻面防控）

1. **FUXI 封印判据面（`adc4dc3` 笔 QA 判据件判据2）**：其读数口径＝`git check-ignore` 对 **evidence 面** rb8-suppl 路文件 exit 0（真源句另载 .gitignore `/**/.collab/evidence/` 现算坐实；链上史笔另引用 `.gitignore:17`/`:20` evidence 行号）。S1 九行插在 L54 之后＝**L17/L20 行号零移动、evidence 规则零改动** → 该判据读数**不翻面**（起草轮探针实证：叠加本规则族后 `git check-ignore` 对 `agent-skills/fuxi-skill/.collab/evidence/corpus/rb8-suppl/probe` 仍 exit 0·命中行仍 `L20:/**/.collab/evidence/`）。FUXI 族史笔中「工序取证面＝仓根 `.scratch/FX-U37/`（不 commit·D-94 口径）」类登记句在 S1 后**语义加强**（从不 commit 变为被忽略）＝无翻面冲突，随注即可，无需 FUXI 会话随改。取态＝**不改判据、不豁免、随注 FUXI 会话**（FUXI 侧未来复跑判据2 读数不变；V5 钉死）。
2. **T9 排除档位措辞（`agent-experts/baigong-software-team/skills/sop/templates/ticket-template.md` L93–L103）**：档位3 已把「仓根 .scratch 族＋仓根 evidence 面＋各包内 .scratch／暂存族」列为排除档位——T9 语义＝**引用旧字样豁免面**，与 gitignore 忽略规则**正交不冲突**（一个管措辞违例豁免，一个管 git 可见性）。S1 落地不使 T9 任何档位失效；封口条款（L103·新落件引用旧字样＝违例）亦零联动。**取态＝零随动**；「是否借本票顺手在 T9 档位3 加括注『现 gitignore 已族级忽略』」＝表述面增益非必需＝**候裁(f)**（随动＝另票还是本票内扩面，起草席不拍）。
3. **`git grep`／门禁扫描面机理（防误判写实）**：忽略规则只作用于**未跟踪面**（status 可见性、`git add` 默认不吞并提示）；对**已跟踪文件**，`git grep`、`git log`、`git diff`、`check-ticket-reconcile.py`（文件系统枚举）、`check-entity.py`（显式剪 .scratch）、`check-pointers.py`（显式除外 .scratch 族）、`run-gates.sh`（grep 面非 git 面）全部**行为零变化**——机理实证见 §2.3 第 1、2 条。**特别提醒施工席**：对 tracked 件跑 `git check-ignore`（缺省）得 exit 1 ≠ 规则未生效，被 index 挡回所致；验证规则本体必用 `--no-index` 口径（V1）。

### 4.4 声明闭集（本票起草阶段唯一可写面）

- 声明闭集：
  - `.scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v1.md`（＝本票面自身·恰一件）

起草阶段＝**纯规格零施工**：`.gitignore`、任何既有 .scratch 文件、守件（hooks/门禁脚本）、账本面一律零触碰。施工阶段声明闭集由放行后 rev／施工票按 §4.1–§4.2 裁定结果另立（预期＝`.gitignore`＋类B 单件处置面）。

### 4.5 禁动面

- 起草阶段：上列声明闭集之外全仓零触碰（含 `.gitignore`）。
- 施工阶段（放行后生效）：`.gitignore` L1–L54 既有行零移动零改写（只在 L54 后空行处插九行块）；`.scratch/tickets/` 桶全部 tracked 件零触碰（类A 零动作）；`git rm -r`／批量删除／`git clean` 全族禁用；`.collab/` 账本面零触碰；`share/` 守件零触碰；`README.md` 白名单表随动与否＝候裁(g)（未裁零动）。
- 历史笔不追改：链上史笔（含 `.gitignore` 头部注释旧行号引用句）一律 append-only。

## 五、验收标准（票体四字段③·全机械·occurrence 口径·命令＋钉值）

> 全部判据由**施工席**在放行后施工轮跑；起草轮已以 excludesFile 覆盖探针预验（§2.3 第 3 条），下列钉值＝探针实测值。

- **V0 开工**：`date`＋`git rev-parse --short HEAD`＋`git status --porcelain --untracked-files=no` 三读数登记；类B 件存在性复点＝`git ls-files -z | tr '\0' '\n' | grep '/\.scratch/\|^\.scratch/' | grep -v '/\.scratch/tickets/\|^\.scratch/tickets/' | wc -l` 施工前基线读数登记（本票复点②＝1）。
- **V1 规则生效（--no-index 口径·忽略判定真口径）**：`git check-ignore --no-index -v .scratch/x agent-experts/baigong-software-team/.scratch/x agent-skills/fuxi-skill/.scratch/x` → **exit 0** 且逐路径命中行分别＝`/.scratch/*` 行与 `/**/.scratch/*` 行（新块内行号在册回执）。
- **V2 tickets 桶豁免**：`git check-ignore --no-index -q .scratch/tickets/probe.md; echo $?` → **1**；`git check-ignore --no-index -q agent-experts/baigong-software-team/.scratch/tickets/probe.md; echo $?` → **1**；`git check-ignore --no-index -q agent-skills/fuxi-skill/.scratch/FX-U26/probe; echo $?` → **0**。
- **V3 未跟踪消隐**：施工后 `git status --porcelain | grep '^??' | grep -c '\.scratch/'` → **0**（起草基线 199）；`git status --porcelain | grep -c '^??'` → 基线减 199 值（散件 9 枚仍显＝不归本票）。
- **V4 已跟踪扫描零变化（机理钉验）**：类A 任取一枚（回执点名制）`git check-ignore -q <tracked-ticket-path>; echo $?` → **1**（缺省口径被 index 挡回＝已跟踪不受忽略管辖实证）；`git grep -l "TMP-DISC" -- '*/.scratch/tickets/*' | wc -l` 前后读数**全等**（tracked 扫描面零变化）。
- **V5 FUXI 判据不翻面**：`git check-ignore -v agent-skills/fuxi-skill/.collab/evidence/corpus/rb8-suppl` 对登记在场路文件 → exit 0 且命中行仍 `/**/.collab/evidence/`；`grep -n '/\*\*/\.collab/evidence/' .gitignore` → 行号仍 **20**（前值 20）。
- **V6 存量终态（方案甲）**：施工收口后 `git ls-files -z | tr '\0' '\n' | grep '/\.scratch/\|^\.scratch/' | grep -v '/\.scratch/tickets/\|^\.scratch/tickets/' | wc -l` → **0**（基线 1，类B 处置闭环读数）；tickets 桶 tracked 计数前后全等（前值＝V0 当轮实测）。
- **V7 门禁零回归**：`bash share/run-gates.sh` → GATE PASS exit 0（前后对拍发现数不新增）；`python share/check-pointers.py --target .scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v1.md` → exit 0；`python share/check-ticket-reconcile.py` 缺省口径读数不新增阻断（票目录走文件系统枚举＝不受忽略影响，§2.3 实证）。
- **V8 .gitignore 体例**：`git diff <base> -- .gitignore` → 删除行 **0**、新增行 **9**；`sed -n '17p;20p' .gitignore` 读数前后全等（L17/L20 史笔引用锚保护）。

## 六、边界约束（票体四字段④）

- **票间关系**：与在飞 **FUXI-U38**（票面 staged `A "agent-skills/fuxi-skill/.collab/tickets/2026-11-10-FUXI-FX-U38起草回执-v1.md"`）互斥登记＝本票施工面只涉 `.gitignore`＋类B 单件，不涉 fuxi `.collab/` 任何面；FUXI 案链上禁动 gitignore 句（FX-U2 票面「禁动 gitignore」）**辖 FUXI 案自身、不辖本票**——本票 gitignore 增笔之授权源＝决策者 2026-11-10 18:58 裁定，开票前需主理人确认该授权链覆盖（排程建议：本票放行笔先于任何 FUXI 续笔触及 gitignore 的窗口，避免判据复跑期插旗）。
- **同源与引用纪律**：本票引用全部现径全写（仓根 `.gitignore`、`agent-experts/baigong-software-team/skills/sop/templates/ticket-template.md`、`agent-skills/fuxi-skill/.collab/qa/2026-11-10-FUXI-FX-U37-QA独立验证-v1.md`、`agent-experts/baigong-software-team/.scratch/tickets/2026-11-05-TMP-DISC-temp-workspace-discipline-ticket.md`、`agent-experts/baigong-software-team/.collab/audits/2026-11-05-TMP-DISC-QA独立验证-v1.md`、`README.md`、`share/check-*.py`）；commit 锚引用＝`329d16c`（开工 ANCHOR）、`14416e9`（复点②时刻 HEAD）、`f135855`（票面落位裁定）、`adc4dc3`（FX-U37 QA 判词笔）、`d83d452`（FX-U37 封印登记笔）——全部 `git cat-file -e` 实测在位（起草轮）。
- **TMP-DISC 纪律互洽核**：TMP-DISC §八.2 唯一落点＝仓根 `.scratch/<票号>/`＋§八.3 收口清理判据＝席位工作区纪律；S1 忽略规则＝其 git 面补全（临时物既不 commit 也不再污染 status 面），两制互洽零冲突；「完工前删除附读数」条款不因忽略规则豁免（清理判据管盘面，忽略只管 git 面——§4.3 第 3 条机理的镜像陈述）。
- **不消费未落盘件**：本票全部依据件已在链；候裁未裁项零预设立场。
- **回执与 commit 纪律**：施工回执落 `.collab/receipts/<票ID>-receipt.md`（放行后定）；起草笔＝本笔（`collab:` 前缀·pathspec 两端齐带·禁 add -A·禁 amend·message 零 at 符号字符）。
- **租约段**（票内·经架构签注由 B2 lease-issuer 实例化）：
  - path_globs：`.gitignore`；`agent-experts/baigong-software-team/.scratch/COLLAB-STRUCT-1/*`（类B 处置面·取态候裁(e)后生效）
  - deny_globs：`/**/.collab/**`；`share/**`；`agent-skills/**`；`README.md`（候裁(g)未裁）；`.gitignore` L1–L54（行级防护以 V8 机械兜底）
  - 席位 ID／票 ID／哈希：由状态机签发，非人工填写

## 七、候裁单列（起草席不自行拍）

- **(a) 仓外临时区卫生两硬条款并入与否**：候选条款＝①仓根 `.scratch/` 下工作区目录一律带票 ID 命名（现盘已呈此惯例：`FX-U37-qa`／`TMPLRULE-eng` 等）；②完工笔前自删附读数（TMP-DISC §八.3 已有收口清理判据，此为向前强化句）。主理人已呈报、皮总未裁——并入本票成文与否随裁；未裁则本票零含。
- **(b) 共享 index 并发风险面是否借本票重估成文**：口径登记＝FUXI 案候补池 R12 皮总裁「并发规矩不立」，其真实口径＝**会话职责划分防串扰，不等于并发风险管理不需要**。本票实况佐证已登记＝§一 链漂移注（起草窗 25 分钟内 HEAD `329d16c`→`14416e9`、仓根票面 10→37）＋开工 tracked 面他案 staged 一枚。是否借本票开并发风险重估＝候裁，本票只登记口径供裁，不预设结论。
- **(c) fuxi／EAC 他案面存量处置射程**：方案甲读法下两桶 32 件全落类A＝零处置＝争点自动消解；若裁方案乙（票面迁桶），fuxi 21＋EAC 11 存量处置归 FUXI／EAC 会话职责面还是本票射程，须先裁归属再开迁面。
- **(d) 历史留档票据保留形态**：留 `.scratch/tickets/` ＋负向豁免规则（方案甲默认，承接裁定 `f135855` 现行制）vs 迁合规桶（`.collab/tickets/` 新桶或并入既有案卷桶）＝形态之争随裁；本票 S1 规则文本按甲成文。
- **(e) 类B 单件处置取态**：B-i 迁 `.collab/receipts/`（内容类型＝回执＝案卷类对口）vs B-ii 就地 `git rm --cached`（最轻手·历史在册·盘留）＝随裁。
- **(f) T9 档位3 措辞是否随动加括注**：随动＝另票还是本票内扩面＝随裁（§4.3 第 2 条已给零随动默认）。
- **(g) README 白名单表随动与否**：仓根 `README.md` 白名单表 `.scratch/tickets/` 行现文仍准确（票面桶仍进 git＝语义未变）；是否加 `.scratch/` 其余族 ignore 态行＝表述面随裁，未裁零动（禁动面已框）。

## 八、排程建议

1. 本票 v1 落链 → 双席审票（产品↔终态口径＋QA↔机械可判性）→ 候裁七条呈皮总归裁 → 按裁定出 rev 或直接放行施工票。
2. 与 FUXI-U38 面互斥关系（§六第 1 条）：本票放行前，FUXI 案不得触及 `.gitignore`（其自设禁动 gitignore 本已覆盖）；本票施工笔落链后随注 FUXI 会话一行（判据2 不翻面实证 V5 可转抄），不构成 FUXI 侧动作义务。
3. 施工窗口建议避开多席开票高峰（§七(b) 佐证面），主理人排程裁。

---

## 附·起草笔自证

- 本票落笔前靶检：`python share/check-pointers.py --target .scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v1.md` → exit 0（读数见回执笔）。
- 起草轮探针残留自查：`.scratch/SWB-SCRATCHG/`（excludesFile 探针目录）用毕已删·`ls .scratch | grep -c SWB-SCRATCHG` ＝ **0**（本票清理判据自示范）。
- commit 自证：`git log --oneline -1` ＋ `git show --name-only HEAD` 恰一件＝本票面。