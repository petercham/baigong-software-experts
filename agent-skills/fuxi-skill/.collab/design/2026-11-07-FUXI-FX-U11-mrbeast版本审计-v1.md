# FUXI-FX-U11 · mrbeast-perspective 版本审计 v1

> 票号＝FX-U11｜工序＝S2 版本审计件（票面 §二 S2·闭集第 7 件）｜日期＝2026-11-07｜审计执行＝工程师席（FUXI 线·FX-U11 票内新鲜实例）
> 性质＝入池前置三件套之「版本审计」件。审计时点＝移池前（S5 未执行），本件 sha256 表＝移池前基线，供 S5 移池后对拍（票面 §三判据 4「三文件移池后 sha256 ≡ S2 审计基线表逐值全等」）。
> 模板先例＝FX-U6 david-fincher 首单版本审计件·第二单照抄件形。

## ① 审计对象版本账

| 字段 | 登记值 | 审计核对 |
|---|---|---|
| 产物id | `mrbeast-perspective` | 与 `agent-skills/fuxi-skill/products/pending/` 下目录名逐字全等 ✓ |
| 版本号 | `v0.2` | SKILL.md 元数据 L13 ✓ |
| 快照时戳 | `2026-10-31` | SKILL.md 元数据 L12 ✓ |
| 复审到期日 | `2027-01-29` | SKILL.md 元数据 L14 ✓（对账见 §④） |
| T9 复跑批次指针 | 复跑批次＝`FUXI-T9`（registration.md 首行注「复跑批次 FUXI-T9」）；收口报告＝`agent-skills/fuxi-skill/.collab/receipts/2026-10-31-FUXI-T9-端到端回归收口报告-v1.md`（票面 `fce3489`／回执 `bb3213e` 在账）；门禁面 ST-10 当期读数「批次 eos-b1、t9 逐路存在性检 18/18 在场」＝批次存在性工具实证 | ✓ |

版本账补注（如实）：本对象随件正文在入池前经 FX-U10 交付笔（`f0998bb`）四处行内原地补口径／内容微动（B1-B4·见 §③），**版本号与快照时戳未随动改登**——该形态＝FX-U10 票面在册设计（补口径非版本迭代·内容微动语义零变），版本账三戳维持 v0.2／2026-10-31／2027-01-29 现登值，本审计按现登值核账。

## ② 随件三文件 sha256 审计基线表（移池前实算）

实算时点＝开工 ANCHOR `874d0be` 现盘态；命令＝`sha256sum`（仓内 `agent-skills/fuxi-skill/products/pending/mrbeast-perspective/`）。

| 文件 | sha256（移池前基线） |
|---|---|
| `SKILL.md` | `8869c8cf7a4a492d6dc7154a774838e77a04abd95c94fc47c36aa88c03d1b787` |
| `registration.md` | `0f3c0ebcfb817fd1b27f34c2c38141022e3b861c2070dc1527eb8322f2b270f6` |
| `test-prompts.md` | `6d6d22c813675929e82cd822214b1b9cd96f7a78bef92e371fbcdcd89559ae3e` |

对拍约定：S5 移池后三文件 sha256 须与本表逐值全等（`git mv` 字节零改＝R100 rename 实证面）；任何不等＝移池违例，按票面 §四整批退回。

SHA 形态注（U10-QA 登记项在册同款）：本表为工作区态 `sha256sum` 实算值；与 U10 回执 L96-97 改后态两值逐字全等（SKILL.md／registration.md），即本基线表＝U10 收口态封字节基线；test-prompts.md 自入壳以来内容零改。git blob LF sha 与工作区 sha 差异归因 autocrlf 工作区 CRLF＝归一化后内容等价（U10-QA 登记项③口径照登）。

## ③ 入池前变更史（U10 四处行内改动·commit 指针照登）

- commit `f0998bb`（全哈希 `f0998bb759ab25d5dba0afde45ed2a9b8d60b89d`）＝「FUXI-FX-U10: 交付笔 S1-S4（mrbeast BW-3 三处出清＋B4 透明度补注）」；`git show --stat` 实跑＝`2 files changed, 4 insertions(+), 4 deletions(-)`（SKILL.md `4 ++--`／registration.md `4 ++--`）＝恰两文件四处行内原地＝票面所述对上；行数不变（66/38 现盘 `wc -l` 实算对上 U10 回执「66→66／38→38」）。
- 四处内容＝SKILL.md L62（B1 批级锚 κ 补口径）／registration.md L36（B2 同口径）／SKILL.md L34（B3 脱裸 % 形态转述态出清）／registration.md L37（B4 窗内 10 条判定依据显形补注·非改数）——细账见 U10 回执与收口登记 `d86b34d`。
- 该 commit 是 `agent-skills/fuxi-skill/products/pending/mrbeast-perspective/` 路径的最近一次改动（`git log --oneline -- <path>` 实跑＝`f0998bb` 居首，其前仅入壳笔 `4f9e43f`）；此外无未入账变更（开工 status 净，untracked 均与产物路径无关）。本票对三文件＝字节零改（票面 §四·U10 起封字节）。

## ④ 复审到期日核对（AC-5 规则：快照＋90 日）

- 实算：`2026-10-31 + 90 日 ＝ 2027-01-29`（python `datetime.date(2026,10,31)+timedelta(days=90)` 读数）。
- 登记值：SKILL.md L14 `复审到期日`=`2027-01-29`。**逐字对上 ✓**（当前日期 2026-11-07 未过期）。

## ⑤ 审计结论行

**版本审计通过**：版本账三戳（v0.2／快照 2026-10-31／复审到期 2027-01-29）自洽且 AC-5 规则实算逐字对上；随件三文件基线哈希已封表（≡U10 收口态回执值）；入池前变更史闭合至 `f0998bb`（U10 补口径与内容微动），无游离变更。本审计不裁质量、不代确认——资格裁量与候裁项 C 随确认包呈皮总（S4 人工闸）。

——工程师席（FX-U11 票内新鲜实例）审计·2026-11-07·除本件外零写入。
