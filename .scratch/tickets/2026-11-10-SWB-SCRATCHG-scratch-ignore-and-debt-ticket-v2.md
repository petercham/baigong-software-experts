# SWB-SCRATCHG · .scratch 族忽略规则与存量债治理规格票（v2·纯规格·零施工·放行 rev 笔）

- 票号：**SWB-SCRATCHG**
- 票名：**.scratch 族忽略规则与存量债治理规格票**
- 票型：规则票（八类取一·修票权＝提案席位＝架构席）
- 起草席／rev 席：架构席 `arch-scratchg1`（v1＝`00f7e7d` 作者席续写·代笔禁令兑现）
- 票面落点：`.scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v2.md`
- **本版 rev 依据**＝皮总裁定登记件 `.collab/decisions/2026-11-10-皮总裁定-候裁三件全按建议放行.md`（落链 `ca33b5f`）§二-1：**放行＝可进**＋候裁七条全部按立场表采可＋**放行前作者席出一笔修订（rev）带八项勘正**；八项勘正真源＝会师呈拍件 `.collab/2026-11-10-SWB-SCRATCHG-双席审会师-放行呈拍简报-v1.md`（落链 `cc08e3f`）§三；双席审件＝产品席 `9d40df1`（红0黄4观察2）＋QA 席 `5e3a22c`（红1黄5绿6）。
- **版本链**：v1＝`00f7e7d`（173 行）原件零触碰不回改（append-only 史实锚）；本版＝整件重写新件（先例体例＝COLLAB-STRUCT-1 v2 整件重写 `.scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v2.md`）。
- 性质：纯规格票不变——**本席不施工**，落改归工程师席按票逐字执行。
- 开工读数：`date`＝2026-11-10 22:24:26；`git rev-parse --short HEAD`＝**`ca33b5f`**（＝裁定登记笔本体，≥ 派工钉值）；`git status --porcelain --untracked-files=no`＝tracked 面 1 项他案 staged 照登不碰＝`A agent-skills/fuxi-skill/.collab/decisions/2026-11-10-皮总裁定-FUXI-C2C3验收工序票触发情况字段装配.md`（FUXI 会话在飞笔，零卷入）。
- **计数口径声明（本版起写死·承呈拍件 §五台账案型）**：本票全部跟踪文件计数一律 `-c core.quotepath=off` 口径＋NUL（`-z`）式双验；默认 quotepath 口径（CJK 路径转义带引号八进制行）对 grep 锚式漏数＝已知案型，不作计数基准。

> **票面自注（落位悖论自陈·承 v1）**：本票面自身落在本票治理对象（`.scratch` 族）之内——照近期体例落位（票面落位＝`.scratch/tickets/`·裁定 `f135855` 在册），方案甲规则族以 tickets 桶负向豁免行覆盖本件，落位与规则自洽。

---

## 一、开工实测读数（v2 起草轮·全部现跑·quotepath=off＋NUL 双口径）

| 项 | 命令 | 实测读数 |
|---|---|---|
| 时点 | `date` | `Tue Nov 10 22:24:26 2026` |
| HEAD | `git rev-parse --short HEAD` | `ca33b5f` |
| tracked 面 | `git status --porcelain --untracked-files=no` | 1 行＝FUXI-C2C3 staged（照登不碰，见票头） |
| tracked .scratch 总数 | `git -c core.quotepath=off ls-files \| grep -c '/\.scratch/\|^\.scratch/'` | **137**（NUL 式同值双验） |
| 桶表 | 同上逐桶前缀式 | 仓根 **38**／百工 **67**／fuxi **21**／EAC **11**／其余 **0**（合计 137 ✓） |
| tickets 桶／类B | 同上桶式 | tickets **136**／类B **恰 1**（点名＝`agent-experts/baigong-software-team/.scratch/COLLAB-STRUCT-1/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md`） |
| 未跟踪条目 | `git status --porcelain \| grep '^??' \| grep -c '\.scratch/'` | **213**（全仓 `??` ＝222＝.scratch 213＋散件 9） |

**v1 §一 读数勘正（勘正第 1 项·红-1/Y-1 承接）**：v1 所登「复点①＝109」「复点②＝136 系链漂移后新值」「仓根票面 10→37（SEMGV／PROJINIT／GWP-DEPLOY 他案落链所致）」三处**全部作废**——双席独立实跑证伪：同一提交 `329d16c` 默认口径＝109／off 口径＝**136**；同一提交 `14416e9` 默认口径＝109／off 口径＝**136**；`git diff --name-only 329d16c 14416e9`＝恰两文件（FUXI-U38 回执＋放行笔）**零 .scratch 面文件**；所列各票落链均早于 `329d16c` 两天以上。109→136 与 10→37 两个「增长」**均为默认口径转义漏数的口径差，起草窗跟踪面零漂移**。连带勘正：v1 §七(b) 与 §八.3 排程句引用的「票面数漂移」佐证**不成立，如实登记作废**（共享 index 并发风险的事实面本身——同窗 staged 他案一枚——仍属实，但不得以该假证据作论据；且该候裁项已随 R12 销账，见 §七-2）。「＝主理人现值全等」＝两个同口径错读互证，不构成双验——v2 起双验必为**同值双口径**（off＋NUL）。

**观察登记（勘正第 3、4 项落地）**
- O-1：仓根未跟踪非 .scratch 散件 9 枚（`.py`、`.scratch_wbdocs.html`、`assert-modified-run2.txt`、仓根 `.collab/research/` 产品席在途件等）＝非 .scratch 族，不入本票射程，卫生归 TMP-DISC 纪律面。
- O-2（勘正版）：仓根 `.scratch/multi-agent-collab-experts`、`.scratch/multi-agent-collab-skills` ＝**符号链接**（`ls -la` 实测＝`-> /d/multi-agent-collab-experts`、`-> /d/multi-agent-collab-skills`，创建时间戳 **Nov 9 17:06**，晚于 TMP-DISC 生效日 2026-11-05），git `??` 面各仅显一行，**非目录副本**；文件级 10 万量级主体实为各席 QA 复测树（头部＝`.scratch/FX-U14-qa` 9550、`FX-U15-qa2` 8933、`FX-U18-qa` 8251……两枚链接贡献各 1 行）。链接按 §八.2 落点口径的合规性另论（其时间戳使 v1「既有存量不追溯」前提不实）；本票零处置，随注另裁。
- O-3（分解式勘正版）：未跟踪按**互斥归组**口径分解＝仓根族（含带引号行）＋百工包内＋fuxi 包内＋EAC 包内，各组判据首段路径互斥；v1 分解式「163＋2＋30＋4＝199 ✓」与双席复跑「167＋2＋30＋4＝203 ≠ 201」均系镜像链接子路径**双重归组**所致（仓根行内含包内 `.scratch/` 子串同触两组模式），v2 起分解式以首段判据互斥（本轮 213 不再拆组报数，V0 当轮实测为准）。

## 二、现盘事实（v2 轮复点·施工输入）

### 2.1 tracked .scratch 桶表（开工现跑 137 件）

| 桶 | tracked | tickets 桶（类A） | 非 tickets（类B） |
|---|---|---|---|
| 仓根 `.scratch/` | 38 | 38 | 0 |
| `agent-experts/baigong-software-team/.scratch/` | 67 | 66 | **1**（点名见 §一表） |
| `agent-skills/fuxi-skill/.scratch/` | 21 | 21 | 0 |
| `agent-skills/external-advisor-collab/.scratch/` | 11 | 11 | 0 |
| 其余 | 0 | 0 | 0 |
| **合计** | **137** | **136** | **1**（双验 ✓） |

（与 v1 复点差值全部＝本票 v1 自身落链＋1（tickets 桶），其余零漂移——即 §一 勘正的正向印证。）

### 2.2 .gitignore 现行体例（承 v1 事实·零变化）
仓根 `.gitignore` 全文 66 行：头部注释（L1–L10）＋制①入库面注释（L12–L15）＋制②排除面（L17–L54）＋系统杂物／工具产物（L56–L66）。零生效 .scratch 规则（仅 L3/L13 注释行含 scratch 字样）。**链上史笔引用行号在册**＝`.gitignore:17`、`.gitignore:20`（FUXI 案判据件），任何插入不得移动 L1–L54。

### 2.3 关键机理实证（v1 起草轮现跑＋双席独立复跑三方全等·写实承本体）
1. **忽略规则不影响已跟踪文件**：tracked 类B 件 `git check-ignore -q`（缺省）＝exit 1（index 挡回）；加 `--no-index`＝exit 0（规则命中）。`git grep`／`git log`／`git diff`／门禁对 tracked 件扫描行为在忽略落地后**零变化**——忽略只管未跟踪可见性（status/add），不管已跟踪扫描。V4 钉死。
2. **现行门禁均不经 `git status` 读 .scratch**：`share/check-ticket-reconcile.py` 文件系统枚举票目录双候选（L329–L353）＋`find_root` 找 `deliverables` 目录本仓无（L126–L138，**缺省调用必 exit 2**，run-gates 内调带 `--root`）；`share/check-entity.py` L177 显式剪 `.scratch`；`share/check-pointers.py` L188–L201 后缀索引除外 `.scratch/` 族（D-94）；`share/run-gates.sh` 及 share 脚本族零 `rg`。→ 忽略规则对上述门禁**零行为差异**。
3. **规则族隔离探针三方验证**：作者席＋产品席＋QA 席各自以 `git -c core.excludesFile=<探针文件>` 覆盖式跑真仓路径（`.gitignore` 零触碰·diff 空集自证），§五 V1–V3/V5 全部预期读数＝三方探针实测读数。`/**/` 对包内三级与仓根双形态覆盖闭合经行4-only 探针实证；`/.scratch/*` 行系制②「嵌套桶级＋仓根显式」体例配对行（QA 判定＝体例冗余·无害·保留）。
4. **`__pycache__` 交互**：`.scratch/tickets/__pycache__/x.pyc` 探针 exit 0 命中 L65 `__pycache__/`＝票面桶内编译缓存不借豁免还魂（前提＝插入位在 L65 之前，§4.1 选位在册）。

## 三、目标（票体四字段①）

终态一句话＝**`.gitignore` 立 .scratch 族生效忽略规则（tickets 票面桶负向豁免＋桶内纪律条款写死），tracked 存量按机械分流判据处置至「.scratch 族内 git 面只剩 tickets 桶」，链上历史判据读数零翻面，仓外临时区卫生两条硬条款并入成文。**

背景口径（决策者 2026-11-10 18:58 裁定原文）：「.scratch 不进 git 是应该定义在 .gitignore 的，目的就是各种临时开发调试的东西往里面塞。」放行裁定（2026-11-10 22:17 皮总「全按建议拍」）：本票放行＋方案甲本体采可＋候裁七条按立场表全部采可（`ca33b5f` §二-1）。

## 四、规格（票体四字段②·逐条到落位·纯规格零施工）

### 4.0 方案本体（已经双席独立证伪存活·v2 禁改写）

方案甲＝.scratch 族整体忽略＋tickets 桶负向豁免；存量类A 票据零迁移零脱跟踪；与裁定 `f135855`（票面落位）、README 白名单表行、check-ticket-reconcile 票目录口径三处现制兼容零随动。方案乙对照登记（不采）＝族整体忽略含 tickets＋票面迁合规桶。以下 S1–S3 承 v1 本体逐字不变，仅随已裁条款挂接（§4.6）。

### 4.1 S1 · .gitignore 规则规格（精确到行·承 v1 本体不变）

插入落位＝现行 L54（第三方快照配套负向组尾行·REFERENCE-SOURCES 配套行）与其后空行之后、现行 L56 `# ── 系统杂物／工具产物（旧 L47–L56 随迁）──…` 节头之前——即制②排除面尾部新增一节。**选位依据**＝L1–L54 行号零移动（链上史笔引用 `.gitignore:17`/`.gitignore:20` 保住，V8 兜底）＋制②内容连续性＋插入位在 L65 `__pycache__/` 之前（§2.3-4 前提）。

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

行义注记（不入库·仅本票在册）：第 4 行＝任意层级 .scratch 直接子项忽略（`/**/` 匹配零或多级＝探针实证）；第 5 行＝仓根层级显式防护行（体例承 L30–L36 组·冗余无害保留）；第 6–9 行＝tickets 桶两级负向豁免（目录行＋内容行成对，先例＝L52–L54）。`git check-ignore -v` 对仓根样本命中末行可能显示负向行（末匹配取胜），**退出码闭集才是判据**（V1 按 `--no-index` 口径写死）。

### 4.2 S2 · 存量分流判据族（判据不硬编码清单·承 v1 本体＋已裁取态挂接）

- **类A 保留跟踪（判据：路径 ∈ `.scratch/tickets/` 桶）**：路径含 `/.scratch/tickets/` 段（或仓根 `.scratch/tickets/` 前缀）者＝留档票据面，随 S1 负向豁免行保留跟踪，**零动作**。开工落桶＝136 件全落类A（仓根 38／百工 66／fuxi 21／EAC 11），四桶全部零施工。**已裁(d)＝取甲**（留原区＋豁免行，零迁移·§七-4）；**已裁(c)＝fuxi／EAC 他案射程径销**（方案甲下全落类A 零处置·§七-3）。措辞承产品席 W-1：仓根桶内含 B 批过渡票（README L22/L88 在册候退役身份）与永久留档票面并存在方案甲下零冲突（不预决其退役），标签上区分「永久留档票面／过渡候退役票面」。
- **类B 脱跟踪（判据：路径 ∈ .scratch 族 ∧ ∉ tickets 桶 ∧ tracked）**：落桶＝**恰 1 件**（点名见 §一表，开工输入非判据本体）。**已裁(e)＝取 B-i**（§七-5）：`git mv` 至 `agent-experts/baigong-software-team/.collab/receipts/`（内容类型＝施工回执＝案卷类·该桶在管在册·产品席核 95 件体例对口）；**随动硬约束＝勘正第 8 项**：工程师租约禁动面随 B-i 目标目录随动——v1 租约段 `deny_globs` 含 `/**/.collab/**` 与 B-i 目标面正面相撞（QA 黄-3），v2 租约段已按裁态改写（§六租约段：deny 面除外目标桶＋path_globs 增目标落位），未随裁前承载不了处置面。
- **类C 未跟踪存量（判据：`git status --porcelain` `??` 面 ∩ .scratch 族）**：S1 落地后自动消隐，**零 git 动作**；盘面清理归 TMP-DISC §八.3＋§4.6-A 硬条款（§七-1）＋O-2 符号链接合规性随注另裁——本票不做批量删除（禁动面 §4.5）。

### 4.3 S3 · 他案判据面联动评估（承 v1 本体·三方实证）

1. **FUXI 封印判据面（`adc4dc3` 笔 QA 判据件判据2·L25 语料落位口径行）**：读数口径＝`git check-ignore` 对 **evidence 面** rb8-suppl 路文件 exit 0（另载 .gitignore `/**/.collab/evidence/` 现算坐实；链上史笔引用 `.gitignore:17`/`:20`）。S1 九行插在 L54 后＝L17/L20 零移动、evidence 规则零改动 → **不翻面**（作者席＋QA 席两方探针叠加复跑均仍 exit 0 命中行仍 L20）。FUXI 族史笔「工序取证面＝仓根 `.scratch/FX-U37/`（不 commit·D-94）」类句在 S1 后语义加强＝无翻面冲突，施工笔落链后随注 FUXI 会话一行即可，无随改义务。取态＝不改判据、不豁免、随注（V5 钉死）。
2. **T9 排除档位措辞（`agent-experts/baigong-software-team/skills/sop/templates/ticket-template.md` 档位3＝L96、封口条款＝L103）**：档位3＝引用旧字样豁免面，与 gitignore 忽略规则**正交**；S1 落地不使档位3/封口条款失效。**已裁(f)＝零随动**（§七-6），不加括注。
3. **扫描面机理（防误判写实）**：忽略只作用未跟踪面；tracked 件的 `git grep`/`git log`/`git diff`/门禁全部零变化（§2.3-1、2）。**施工席提醒**：对 tracked 件跑缺省 `git check-ignore` 得 exit 1 ≠ 规则未生效（index 挡回）；验证规则本体必用 `--no-index`（V1）。V4 pathspec 覆盖面注记（QA 附注）：`git grep -- '*/.scratch/tickets/*'` 的 `*` 不跨 `/`＝不含仓根桶——判据为前后全等对拍仍成立，覆盖面按注记执行。

### 4.4 已裁条款成文（原候裁段消解·七条全部裁毕并入票体）

候裁登记见 §七；本节＝裁后条款正文，施工席按此逐字执行。

- **A（并入·已裁(a)）· 仓外临时区卫生两条硬条款**：
  1. 仓外临时工作区目录**一律带票 ID 命名**（现盘惯例 `FX-U37-qa`／`TMPLRULE-eng` 族的仓外对应形态）；
  2. **完工笔前自删附读数**（`ls` 删除前清单＋删除后 `grep -c` 归零读数落回执）。
  两处条款管辖仓根及仓外公共区临时物，与 TMP-DISC §八.3 收口清理判据衔接（该判据管盘面·A-2 向前强化完工笔时序）。**首批存量处置样本四处点名**（开工 `ls -d` 实测在位）：`D:/semgvt6-clone`、`D:/semgvt6-assemble-tmp`、`D:/semgvt6-assemble-tmp2`、`D:/qa-semgovt6v2-tmp`——**票面只列处置规格不涉删除动作，删除权在皮总（安全闸拦截面维持）**；处置随本票施工线呈皮总单次点名执行。
- **B（已裁(c)）· fuxi／EAC 射程径销**：方案甲下两桶 32 件全落类A 零处置，射程争点径销登记，不再另列。
- **C（已裁(d)）· 历史留档票据保留形态＝甲**：留原区＋豁免行，零迁移（承接 `f135855` 现行制）。
- **D（已裁(e)）· 类B 例外单件＝B-i 迁回执桶**：`git mv` 至 `agent-experts/baigong-software-team/.collab/receipts/`＋**租约随动硬约束**（§六租约段已按此改写；工程师席核对租约面后方可施工）。
- **E（已裁(f)）· T9 括注零随动**：不碰 `ticket-template.md` 一字。
- **F（已裁(g)）· README 白名单表随一行**：施工票射程内含 `README.md` 一行随动（规格如下，工程师逐字照落）——L22 行说明列现文「仓根 `.scratch/tickets/` 仅存 B 批过渡票（退役候裁见 B 批收口登记）」陈旧面（现盘 38 件）改为：「仓根 `.scratch/tickets/`＝历史留档票面桶（B 批过渡票候退役在册）；仓根及各包 `.scratch/` 其余族＝gitignore 忽略态（SWB-SCRATCHG）」——进 git 列不变（仍 ✅）；行内其余零动。
- **G（已裁(h)·QA 黄-5 咬出防线缺口）· 票面桶内纪律条款写死**：**`.scratch/tickets/` 桶内新落件仅限票面族**（票／回执／README 索引类件）；**借 tickets 桶落临时调试物＝违例**（纪律面条款·消费面＝各席开票自检＋QA 收口核对该桶 `??` 面逐笔归因，见 V3 第二读）。机理注记＝豁免使整个票面桶免忽略（探针实证桶内任意新件 exit 1），TMP-DISC §八.3 清理判据管盘面不管 git 面（§六引用纪律自点镜像关系）——防线缺口以纪律条款补位，非规则改动。

### 4.5 声明闭集（本 rev 起草阶段唯一可写面）

- 声明闭集：
  - `.scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v2.md`（＝本票面自身·恰一件）

rev 起草＝纯规格零施工：`.gitignore`、v1 原件、双席审件、呈拍件、裁定登记件、任何 .scratch 既有文件、守件、账本面一律零触碰。施工阶段声明闭集＝放行后工程师施工票按 S1＋S2-B-i＋§4.4-A/F 另立（预期面＝`.gitignore`＋类B 迁移两式位点＋`README.md` 一行）。

### 4.6 禁动面

- rev 起草阶段：上列声明闭集之外全仓零触碰（含 `.gitignore`、v1 票面）。
- 施工阶段（放行后生效）：`.gitignore` L1–L54 既有行零移动零改写（只在 L54 后空行处插九行块）；tickets 桶全部 tracked 件零触碰（类A 零动作）；`git rm -r`／批量删除／`git clean` 全族禁用；`share/` 守件零触碰；`ticket-template.md` 零触碰（已裁(f)）；仓外四处存量目录＝票面零删除动作（删除权在皮总）；`README.md` 仅 §4.4-F 一行射程。
- 历史笔不追改：链上史笔（含 v1 票面全部原文、含其不实叙述——由本 v2 勘正件随链销账，不回改）一律 append-only。

## 五、验收标准（票体四字段③·全机械·occurrence 口径·命令＋钉值）

> 施工席施工轮跑；钉值经作者席＋双席三方探针预验。

- **V0 开工**：`date`＋`git rev-parse --short HEAD`＋`git status --porcelain --untracked-files=no` 三读数登记；类B 基线式＝`git -c core.quotepath=off ls-files | grep '/\.scratch/\|^\.scratch/' | grep -v '/\.scratch/tickets/\|^\.scratch/tickets/' | wc -l` ＝**1**（off 口径不受转义陷阱）；全仓 `??` 基线＝`git status --porcelain | grep -c '^??'` 当轮实测登记（V3 第二读基线定义于此·勘正第 7 项）。
- **V1 规则生效（--no-index 真口径）**：`git check-ignore --no-index -v .scratch/x agent-experts/baigong-software-team/.scratch/x agent-skills/fuxi-skill/.scratch/x` → **exit 0** 且逐路径命中行分别＝`/.scratch/*` 行与 `/**/.scratch/*` 行（新块内行号回执在册）。
- **V2 tickets 桶豁免**：`git check-ignore --no-index -q .scratch/tickets/probe.md; echo $?` → **1**；`git check-ignore --no-index -q agent-experts/baigong-software-team/.scratch/tickets/probe.md; echo $?` → **1**；`git check-ignore --no-index -q agent-skills/fuxi-skill/.scratch/FX-U26/probe; echo $?` → **0**。
- **V3 未跟踪消隐（拆两读·勘正第 6 项·产品席 Y-3 承接）**：
  - **V3-a 桶外读**：`.scratch` 族内 ∉tickets 桶的 `??` 计数 → **0**——`git status --porcelain | grep '^??' | grep '\.scratch/' | grep -v '\.scratch/tickets/' | wc -l` → 0（探针态目录级／文件级均复现 0，含嵌套镜像内 tickets 文件不借豁免还魂）。
  - **V3-b 桶内读**：tickets 桶内 `??` **逐笔登记为「未落链新票面」不计违例**（并发窗口敏感面：放行后施工票面本身／他案新起草票面会以 `?? .scratch/tickets/<新票>.md` 现身＝假 FAIL 源）；该逐笔归因面同时是 §4.4-G 桶内纪律条款的 QA 消费面。
  - **V3-c 全仓读（基线定义补·勘正第 7 项）**：全仓 `??` 计数＝「基线」＝**V0 当轮登记值**，施工后 → 基线 − (V0 当轮 .scratch `??` 计数)；散件面存续不计本票。
- **V4 已跟踪扫描零变化（机理钉验）**：类A 任取一枚（回执点名制）`git check-ignore -q <tracked-ticket-path>; echo $?` → **1**（index 挡回实证）；`git grep -l "TMP-DISC" -- '*/.scratch/tickets/*' | wc -l` 前后读数**全等**（覆盖面注记：该 pathspec `*` 不跨 `/` 不含仓根桶·QA 附注在册）。
- **V5 FUXI 判据不翻面**：`git check-ignore -v agent-skills/fuxi-skill/.collab/evidence/corpus/rb8-suppl` 对登记在场路文件 → exit 0 且命中行仍 `/**/.collab/evidence/`；`grep -n '/\*\*/\.collab/evidence/' .gitignore` → 行号仍 **20**（前值 20）。
- **V6 存量终态（方案甲）**：收口后 `git -c core.quotepath=off ls-files | grep '/\.scratch/\|^\.scratch/' | grep -v '/\.scratch/tickets/\|^\.scratch/tickets/' | wc -l` → **0**（基线 1·类B 处置闭环）；tickets 桶 tracked 计数前后全等（前值＝V0 当轮实测·off 口径）。
- **V7 门禁零回归（勘正第 5 项·QA 黄-4 承接：补 `--root` 用法＋基线钉值）**：
  - `bash share/run-gates.sh` → **GATE PASS exit 0**；基线钉值＝**发现 150138**（QA 席 `5e3a22c` 现跑参照钉）；前后对拍发现数不新增（附前后读数；链上他案笔致增数逐笔归因 EXEMPT，判因附他席件路径证据）。
  - `python share/check-ticket-reconcile.py --root .` → **exit 1·票 134／发现 184 全 WATCH**（产品席现跑基线钉＝缺省调用必 exit 2「未能定位仓根」系 `find_root` 找 `deliverables` 本仓无＝已知机理，**必须带 `--root .`**）；前后对拍不新增阻断。
  - `python share/check-pointers.py --target .scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v2.md` → exit 0。
- **V8 .gitignore 体例**：`git diff <base> -- .gitignore` → 删除行 **0**、新增行 **9**；`sed -n '17p;20p' .gitignore` 读数前后全等（L17/L20 史笔引用锚保护）。
- **V9（新增·随裁条款施工核验）**：`grep -c "票面真源落位（皮总裁定·票面落 scratch）" README.md` 前后各附（前＝1）；README L22 行 diff ＝**改 1 行**（§4.4-F 逐字比对）；类B 迁移后 `git ls-files "agent-experts/baigong-software-team/.collab/receipts/" | grep -c "COLLAB-STRUCT-1-施工回执"` → **1**（迁移到位·B-i）。

## 六、边界约束（票体四字段④）

- **票间关系**：与在飞 FUXI 案（含 U38 及其后笔）互斥登记＝本票施工面只涉 `.gitignore`＋类B 单件迁移＋README 一行，不涉 fuxi 任何面；FUXI 案自设禁动 gitignore 句（FX-U2 票面 L22「禁动 gitignore」）辖 FUXI 案自身、不辖本票——本票增 gitignore 授权源＝决策者 2026-11-10 18:58 裁定＋放行裁定 `ca33b5f`；排程互斥系程序性安排（产品席 W-2 照登：租约 deny_globs 只束本票施工席，拦不住 FUXI 会话并发笔，靠主理人排程兑现；九行块与 evidence 行无交互已由 V5 实证，风险有限）。
- **同源与引用纪律**：引用全部现径全写；commit 锚＝`329d16c`（v1 开工）、`00f7e7d`（v1 落链）、`9d40df1`（产品席审件）、`5e3a22c`（QA 席审件）、`cc08e3f`（呈拍件）、`ca33b5f`（裁定登记件）、`dcdb497`（R12 裁定）、`f135855`（票面落位裁定）、`adc4dc3`/`d83d452`（FUXI 封印判据/登记笔）——全部 `git cat-file -e <sha>^{commit}` 实测在位（v2 起草轮＋双席审件两方各自实测在册）。
- **TMP-DISC 纪律互洽核**：§八.2 唯一落点＋§八.3 收口清理判据＝席位工作区纪律；S1＝其 git 面补全；「完工前删除附读数」不因忽略规则豁免（清理判据管盘面，忽略只管 git 面）；§4.4-A 两条硬条款＝其向前强化（已裁并入）。
- **不消费未落盘件**：本票全部依据件已在链。
- **回执与 commit 纪律**：施工回执落 `.collab/receipts/<票ID>-receipt.md`（放行后定）；rev 起草笔＝本笔（`collab:` 前缀·pathspec 两端齐带·FX_COMMIT_DECLARE 声明·禁 add -A/amend·message 零 at 符号字符）。
- **租约段**（票内·经架构签注由 B2 lease-issuer 实例化·**已按已裁(e) 随动改写·勘正第 8 项**）：
  - path_globs：`.gitignore`；`agent-experts/baigong-software-team/.scratch/COLLAB-STRUCT-1/*`（类B 迁出源面）；`agent-experts/baigong-software-team/.collab/receipts/*`（类B 迁入目标面·B-i 随动授权）；`README.md`（仅 §4.4-F 一行·F 随动授权）
  - deny_globs：`/**/.collab/**`（**除外**上行 receipts 目标面单点）；`share/**`；`agent-skills/**`；`agent-experts/baigong-software-team/skills/sop/templates/ticket-template.md`（已裁(f) 零随动）；`.gitignore` L1–L54（行级防护以 V8 机械兜底）
  - 席位 ID／票 ID／哈希：由状态机签发，非人工填写

## 七、已裁登记（原候裁段消解·`ca33b5f` §二-1 逐条照登）

1. **(a) 仓外临时区卫生两条硬条款＝并入本票**——成文于 §4.4-A；四处存量目录首批样本点名（`D:/semgvt6-clone`、`D:/semgvt6-assemble-tmp`、`D:/semgvt6-assemble-tmp2`、`D:/qa-semgovt6v2-tmp`·开工 `ls -d` 实测在位），删除权在皮总。
2. **(b) 共享 index 并发重估＝不呈不立**——随 FUXI 案 R12「并发规矩不立」裁定（`dcdb497`）销账，维持不呈；皮总澄清口径照登＝「不立」真义＝会话职责划分防串扰，≠并发风险管理不需要；v1 曾引「票面数 10→37 漂移」作佐证＝**假读数已作废**（§一勘正），事实面（同窗 staged 一枚）仍属实但不另列条款。
3. **(c) fuxi／EAC 存量射程＝径销**——方案甲下自动消解（§4.4-B）。
4. **(d) 历史留档票据保留形态＝甲**——留原区＋豁免行零迁移（§4.4-C）。
5. **(e) 类B 例外单件＝B-i 迁回执桶**——＋随动硬约束＝工程师租约禁动面随目标目录随动（§4.4-D＋§六租约段改写，勘正第 8 项）。
6. **(f) T9 措辞括注＝零随动**（§4.4-E）。
7. **(g) README 白名单表＝随一行**（§4.4-F 规格入票面）。
8. **(h) 票面桶内纪律条款＝写死**（§4.4-G·QA 黄-5 防线缺口补位）。

（计数双验：本段八目＝七条已裁＋(b) 销账目；v1 票头「六条」笔误承 Y-4／QA 黄-2 勘正为「七条候裁」后现已全部裁毕归零＝本票**零候裁**。）

## 八、排程建议（承 `ca33b5f` §三-1 路径）

1. 本 rev（v2）落链 → **双席窄验**（产品↔随裁条款落位＋QA↔勘正与钉值加固）→ 工程师席**分笔施工**（忽略规则笔＝S1 九行＋类B 处置笔＝B-i 迁移＋README 一行＋桶内纪律条款消费面）→ QA 独立验收 → 收口。
2. FUXI 面：本票放行笔→施工笔窗口内 FUXI 续笔不触 `.gitignore`（其自设禁动本已覆盖＋主理人排程兑现，W-2 随注）；本票施工笔落链后随注 FUXI 会话一行（V5 不翻面实证可转抄），不构成 FUXI 侧动作义务。
3. 施工窗口建议避开多席开票高峰（并发事实面在§七-2 登记但不开条款）。
4. 排程纪律照登（裁定 §四）：交付面施工单一工程师席在飞串行；同席（架构席）任务不并发——SCRATCHG rev 与 A14 合并票起草串行安排。

---

## 附·rev 笔自证

- 落笔前靶检：`python share/check-pointers.py --target .scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v2.md` → exit 0（读数随回报）。
- 八项勘正落位自查：①§一 勘正段＋§二.1 括注；②§七 全段（候裁取消改已裁）＋票头无「六条」字样；③§一 O-2 勘正版；④§一 O-3；⑤§五 V7；⑥§五 V3-a/b；⑦§五 V3-c＋V0 基线定义；⑧§4.4-D＋§六租约段改写＋§七-5。
- 零触碰自证：v1 原件／双席审件／呈拍件／裁定登记件／`.gitignore` 全程 diff 空集；临时工作物＝本笔 commit 输出重定向落仓根 `.scratch/` 下 SCRATCHG-v2 前缀日志件（.scratch 临时区合规·带票号族命名·完工笔前自删附读数＝§4.4-A 条款自示范）。
- commit 自证：`git log --oneline -1`＋`git show --name-only HEAD` 恰一件＝本票面。