# FUXI-FX-U6 · david-fincher-perspective 版本审计 v1

> 票号＝FX-U6｜工序＝S2 版本审计件（票面 §二 S2·闭集第 7 件）｜日期＝2026-11-06｜审计执行＝工程师席（FUXI 线·FX-U6 票内新鲜实例）
> 性质＝入池前置三件套之「版本审计」件。审计时点＝移池前（S5 未执行），本件 sha256 表＝移池前基线，供 S5 移池后对拍（票面 §三判据 4「三文件移池后 sha256 ≡ S2 审计基线表逐值全等」）。

## ① 审计对象版本账

| 字段 | 登记值 | 审计核对 |
|---|---|---|
| 产物id | `david-fincher-perspective` | 与 `products/pending/` 下目录名逐字全等 ✓ |
| 版本号 | `v0.2` | SKILL.md 元数据 L13 ✓ |
| 快照时戳 | `2026-10-31` | SKILL.md 元数据 L12 ✓ |
| 复审到期日 | `2027-01-29` | SKILL.md 元数据 L14 ✓（对账见 §④） |
| T9 复跑批次指针 | 复跑批次＝`FUXI-T9`（registration.md 首行注「复跑批次 FUXI-T9」）；收口报告＝`.collab/receipts/2026-10-31-FUXI-T9-端到端回归收口报告-v1.md`（票面 `fce3489`／回执 `bb3213e` 在账）；门禁面 ST-10 当期读数「批次 t9 逐路存在性检 18/18 在场」＝批次存在性工具实证 | ✓ |

## ② 随件三文件 sha256 审计基线表（移池前实算）

实算时点＝开工 ANCHOR `b813207` 现盘态；命令＝`sha256sum`（仓内 `products/pending/david-fincher-perspective/`）。

| 文件 | sha256（移池前基线） |
|---|---|
| `SKILL.md` | `c8f9c3536cbc4a541381cf2c31ca8d3f9ecb1dcb9d1f9247dd063f6ee60e0f30` |
| `registration.md` | `16de53798163bad283dcc968670853b4b54d9c0f4e28159d06f970a396d27141` |
| `test-prompts.md` | `9d01441a98d305c4c40a2fa47b211500b93adea6d7487fd3ab3d333d04039f01` |

对拍约定：S5 移池后三文件 sha256 须与本表逐值全等（`git mv` 字节零改＝R100 rename 实证面）；任何不等＝移池违例，按票面 §四整批退回。

## ③ 入池前变更史（U5 补口径两行改动·commit 指针照登）

- commit `5826b40`（全哈希 `5826b40dd108df7ba41899f4c302c9fba800587b`）＝「FUXI-FX-U5: david-fincher两件BW-3补口径（L61/L36原地补一致性系数κ=0.801887软门锚点元组读数·红账清偿首笔david归零）」；`git show --stat` 实核＝改动两文件恰各一行（SKILL.md L61／registration.md L36，2 files changed, 2 insertions(+), 2 deletions(-)）＝票面所述「两行改动」对上。
- 该 commit 是 `products/pending/david-fincher-perspective/` 路径的最近一次改动（`git log -1 -- <path>` 实跑＝`5826b40`）；此外无未入账变更（开工 status 净，untracked 均与产物路径无关）。

## ④ 复审到期日核对（AC-5 规则：快照＋90 日）

- 实算：`2026-10-31 + 90 日 ＝ 2027-01-29`（python `datetime.date(2026,10,31)+timedelta(days=90)` 读数）。
- 登记值：SKILL.md L14 `复审到期日`=`2027-01-29`。**逐字对上 ✓**（当前日期 2026-11-06 未过期）。

## ⑤ 审计结论行

**版本审计通过**：版本账三戳（v0.2／快照 2026-10-31／复审到期 2027-01-29）自洽且 AC-5 规则实算逐字对上；随件三文件基线哈希已封表；入池前变更史闭合至 `5826b40`（U5 补口径），无游离变更。本审计不裁质量、不代确认——资格裁量随确认包呈皮总（S4 人工闸）。

——工程师席（FX-U6 票内新鲜实例）审计·2026-11-06·除本件外零写入。
