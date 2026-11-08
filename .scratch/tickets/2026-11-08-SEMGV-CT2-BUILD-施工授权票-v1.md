# TK-SEMGV-CT2-BUILD · 施工授权票：契约两处修法＋校验器旁路＋config/夹具窄随动（v1）

- 票 ID＝`TK-SEMGV-CT2-BUILD`。票型＝施工授权票（非设计票、非分票；同 T1-BUILD `b9169c6`／T2-BUILD `5f32548`／CT1-BUILD `f780ce4` 先例）。
- 开票席＝主理人；落笔时点 2026-11-08 14:4x–14:5x +0800；落笔前实测 HEAD＝`e6806b8`（本票落链后即为此值±）；他案未跟踪在制品照登不碰。
- 批准载体＝呈放行件 `.collab/decisions/2026-11-08-呈皮总-SEMGV-CT2契约整改审面收口呈放行.md`（`dde4dd8`）选项 A＋皮总原话「放行。」；放行登记＝`.collab/decisions/2026-11-08-主理人登记-皮总批准SEMGV-CT2放行.md`（`e6806b8`）。
- **规格唯一真源**＝`.scratch/tickets/2026-11-08-SEMGV-CT2-契约整改规格票-v2.md`（commit `3340ab3`，199 行／33,748 字节／sha256 `ea715f9e306b1eb5a1e3ef6284698f967b6ef65a13e7ad8ca5dd106d2f269689`；主理人落笔前独立复算＝blob 与该 sha 全等）。工程师读规格以 `3340ab3` 的 blob 为准（`git cat-file blob "3340ab3:.scratch/tickets/2026-11-08-SEMGV-CT2-契约整改规格票-v2.md"`），不以工作区快照为准。**v2 未覆盖处＝停手上报，不得自行扩规格**（CT1-BUILD 三处实证先例＝c11 探针／D09 锚／T-A3 靶点均停手待裁后才动）。
- 本票不复制契约条款正文；一切修法全文（CM-1 修法 1/2/3/5 逐字照落文本）与校验器施工规格（CS-1）只在 v2 §1／§2 内。

## 〇、开工前置（不符即停手上报，不自行纠偏）

1. 开工第一步实跑 `date`、`git rev-parse --short HEAD`、`git status --porcelain --untracked-files=no`，三读数写入回执开端；HEAD 应 ≥ `e6806b8`（并发线可能前移，如实登记差值，不 rebase、不等待）。
2. 实跑 `git cat-file -e 3340ab3^{commit}` ＋ v2 票面 sha256 复算＝`ea715f9e…9689`，确认规格真源逐字节在位。
3. 复核被改对象现态基线（主理人开票前实测誊录，工程师开工复算核对，任一不符＝停手上报）：
   - 契约七件（`agent-skills/claim-commitment-governance/`）：行数实测 **92／225／52／100／43／45／33＝590**；且 `git diff 4700456..HEAD -- agent-skills/claim-commitment-governance/` **空输出**（CT1-BUILD 后该面零新笔）；
   - 校验器：`agent-experts/baigong-software-team/skills/sop/scripts/semantic-governance.py`＝**1,691 行／85,543 字节／sha256 `62d27687f0302af5945ca604787539c6e7e6fcd6c7a68094eeb42b1d148c8037`**；
   - 闭集配置：`agent-experts/baigong-software-team/config/semantic-closed-sets.json`＝**53,829 字节／sha256 `f38dc492f1e9dced2144fb2c61bae088a994e2edd2c11a9cdf62347ddc96150d`**；
   - T1 验收夹具：`.scratch/tickets/2026-11-07-SEMGOV-T1-BUILD-verify.py`＝**2,100 行／sha256 `67fdee3e5dd5a6ab5319220fcd1849d48d7c647db16e3094c584c80b076a4d4e`**。
4. 夹具使用口径钉死：`python .scratch/tickets/2026-11-07-SEMGOV-T1-BUILD-verify.py --all <pkg>`——**必带 `<pkg>` 包目录参数**（不带＝`IndexError`，主理人 2026-11-08 实证系使用口径非夹具缺陷）。

## 一、写集闭集（超集即停手上报）

### W1 · 契约两件（交付面·按 v2 §1 逐字照落）

| # | 目标文件（前缀 `D:\multi-agent-collab-devkits\agent-skills\claim-commitment-governance\`） | 现态行数 | 预算改后（v2 §3） | 牵动修法 |
|---|---|---|---|---|
| 1 | `references\10-contract.md` | 225 | **227（＋2）** | CM-1 修法 1（`:219` 正向可判条件段后**新增独立段**＝正文行＋空行＋2，含修法 5 第二句同段）＋修法 2（`:221` 行内替换至段末）＋CM-2 修法 1（`:223` 段末追加·行内 0） |
| 2 | `references\30-gates.md` | 100 | **100（0）** | CM-1 修法 3（`:19` R2 行整行行内替换·同格扩写不加行） |
| 3 | `templates\claim-register.md` | 45 | **45（0）** | CM-2 修法 2（`:45` 注 11 行内替换·v2 §1 CM-2 修法 2 在册落位面） |

**W1 闭集＝契约三件**：`10-contract.md`（225→227）／`30-gates.md`（100→100）／`claim-register.md`（45→45）。其余四件（SKILL.md／20-artifact-mapping／40-provenance-map／outbound-artifact）契约面零改动（`git diff` 须空）。预算合计 590→**592**（v2 §3 钉值：逐件差量 0／＋2／0／0／0／0／0）。

### W2 · 校验器 CS-1（v2 §2 唯一施工规格）

`agent-experts/baigong-software-team\skills\sop\scripts\semantic-governance.py`：R2 降级形态支内（`:455-462`），在 `if rec.get("authority") != "unverified":`（`:459`）判定**之前**增条件格旁路——三条件 `cond_ok = (_human(rec.get("approver","")) and rec.get("status","") in _cond_status_set(cs) and not _none(rec.get("expiry","")))`，**同源复用既有 helper**（`_human`／`_cond_status_set :528`／`_none`），禁复制或另立；`cond_ok` 真→本条目不判行级 `authority`（continue），否则现行为逐字保留。四支不动（无冒号／kind 未知／`:464` 前缀闭集外／`:468` REQ-·CMP- 不在册）＋branch=1／branch=3 逐字不动。注释卫生照 SEMGOV-T2 QA 黄-1 先例：只写功能描述，禁票号／裁定号／案卷字样。

### W3 · 闭集配置随动（恰一处）

`agent-experts/baigong-software-team\config\semantic-closed-sets.json`：仅 `g12.r_table` 内嵌 gates `:19` R2 行逐字（config `:832`）→按改后正文重算（V6 口径）。`g10.positive_decidable_line` 等其余各处**重算即等值、禁改期望**（v2 §2 随动清单＝Y-2 收窄版钉死）。

### W4 · T1 验收夹具随动（仅两处重算面）

`.scratch/tickets/2026-11-07-SEMGOV-T1-BUILD-verify.py`：仅 `c13`（`ROW_DIGESTS['c13']` 内 `'R2'` 摘要随 gates R2 改句重算）＋`c26`（§11 整节 digest 随 10-contract §11 改句重算）两处按改后正文重算。**零随动面＝重算应等值、禁改期望**：`c16`／`c23`／`c24`／注 11 正文面／`c27`（v2 §2 钉死；改期望致红＝CT1-BUILD 反向教训）。四类读数 `--all`／`--mutate`／`--selfcheck`／`--stats` 随回执登记（红4-03 同源教训）。

**未预见面纪律**：夹具判定面（含 `--selfcheck` 34 比对、REV 靶点、D 族锚）与本票修法文本若遇 v2 未预见的冲突＝**停手上报**，等待裁（CT1 两次在途裁定＝先例；自行豁免＝违例）。

### W5 · 回执

`.scratch/tickets/2026-11-08-SEMGV-CT2-BUILD-回执-v1.md`（新件）：开工三读数＋逐项判据读数＋**完整写入/修改文件清单**（对账口径＝commit name-only 与清单全等·拍板㊻③）＋四类夹具读数＋三态明示＋自查勘正登记。

## 二、租约两态（照登·T1 `86d9963` 裁定 B 先例＋CT1-BUILD 实证沿用）

- lease-issuer 按 engineer `write_globs` 行粒度可签发面＝`skills/**`＋`config/**`（CT1 实签 hash `6bff8c1283417ee9cb339e0f7b64df0a78224916be4c56ebfe48cb66e629a959`）；
- `agent-skills/claim-commitment-governance/**` 与 `.scratch/**`（含 fixture `*.py`）在 engineer 写域行外、零裁量子集校验拒签 exit 2（CT1 实测 seat-permissions.json）；
- 处置照 T1 `86d9963` 裁定 B 先例＝**票面写集闭集＝真授权**，租约可签面照登、不可达面如实登记（v2 §2「另授含 fixture 路径与 `*.py` 的新租约」按现态机件不可达，以本票闭集为准）；工程师遇租约校验拒签＝按先例径行走票面闭集，不开新裁量。

## 三、验收判据（QA 独立验逐条对位）

| # | 判据 | 口径 |
|---|---|---|
| 1 | 开工三读数＋规格 blob 复算＝`ea715f9e…9689` 全等＋基线四组钉值核对 | 回执开端 |
| 2 | 写集恰 W1 三件＋W2 校验器＋W3 config＋W4 夹具＋W5 回执＝**≤7 件**；契约其余四件 `git diff` 空 | name-only 对账 |
| 3 | `10-contract.md` 225→227（＋2 独立段落位＝修法 1 段含修法 5 第二句）；`:221` 替换区间自「此时 `source:` 面…」起逐字＝v2 修法 2 全文；「不另设字段面」「伪承载」等钉句在位 | 逐字对位 |
| 4 | `30-gates.md` `:19` R2 行＝修法 3 全文逐字（「条件格旁路（例外）」「与该行 `authority` 取值无关」「旁路判与该行 `authority` 取值无关」「A4 登记」「§9」在位）；第一支／在册解析边界句／production 第三支一字不动；R 号与 R 总条数不动 | 逐字对位 |
| 5 | `claim-register.md` 注 11＝修法 2 替换后全文逐字；行数 45 不变；`c16` 编号条目计数 `^\d+\.\s`＝11 不变 | 逐字对位 |
| 6 | CS-1 旁路落位＝`:459` 判定前 `cond_ok` 三条件、复用 helper 零复制；四支＋branch=1/3 逐字不动（diff 对位） | 实现 diff |
| 7 | **护栏四态对抗亲跑**（v2 反证①②③＋CT1 在册口径）：approver=none／status=draft／approver=seat:／expiry=none 四变体→R2×2＋R7 双咬红；三条件齐→绿 | 隔离样本 |
| 8 | exc1 形态样本（`approver=human:…`＋`expiry=2026-12-31`＋`status=accepted`＋source:/cite: 自由文本）修后 `validate` **exit 0**＝语义正确绿；修前红复现（H2 式修前/修后对拍先例） | 隔离样本 |
| 9 | 四支不吞对抗：无冒号／kind 未知／`REQ-` 不在册／production 无在册 `artifact:` →照红（branch 读数不变） | 隔离样本 |
| 10 | config 仅 `g12.r_table` 一处变（diff 恰该行）；`g10` 等重算等值；`--selfcheck` 34 比对全过 | 读数 |
| 11 | 夹具仅 `c13['R2']`＋`c26` digest 两值变；`c16`/`c23`/`c24`/`c27` 等值未改期望；四类 `--all <pkg>`／`--mutate`／`--selfcheck`／`--stats` 读数登记（`--mutate` 4/4 红口径照旧） | 读数 |
| 12 | 表结构列数七件全零变化（A20／B9／C7／D13）；守恒式与判定序文本零动 | 文本扫描 |
| 13 | 两笔封顶＝施工笔＋回执笔；在途裁定随动笔仅在停手上报获裁后追加且如实登记「超出封顶＝裁定派生」 | 链核 |

- 禁 `--no-verify`／`--amend`／`reset`／`git add -A`；一切提交 add/commit 双侧 pathspec；他案面不碰（在途 FUXI 面照登）。
- **回执＋各笔全 commit 落账后才算收束**（收束未落账七次实证·铁律）。

## 四、放行后时序（登记件 `e6806b8` 钉死）

工程师（本票）→ QA 席 fresh eyes 独立验（判据 1–13·旁路护栏对抗亲跑）→ 同一拆仓澄清件复跑试填＝兜底闸（R-N1 消失实据：exc1 填法在真实材料走通）。对照表候裁项不在本票射程（`5d8d3ae` 呈拍中；裁「加」另出补票）。

## 五、三态明示

1. 做了没落盘：本票开票前只读核对（九件 `wc -l`／sha256 复算／v2 blob 复算／夹具 c13/c26 锚 grep 实测）。
2. 落盘没提交：本文件写入后至 add 前为工作区新件态。
3. 提交没对账：本笔落链后至查盘三件套（status 他案照登＋尾笔对上回报 sha＋name-only 恰本票一件）实测前。
