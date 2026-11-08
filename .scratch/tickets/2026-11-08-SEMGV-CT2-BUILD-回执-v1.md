# SEMGV-CT2-BUILD 回执 v1（工程师席 eng-semgov-t2b）

授权票＝`180c96f`（blob 读票面）；规格唯一真源＝CT2 v2 blob `3340ab3`（sha256 `ea715f9e306b1eb5a1e3ef6284698f967b6ef65a13e7ad8ca5dd106d2f269689`／199 行／33,748B）。

## 0. 开工三读数＋租约＋基线四组钉值（判据 1）

- 开工时点：date 实测 2026-11-08 14:50:15；开工 HEAD＝`180c96f`；tracked 净（他案 untracked 面照登不碰）。
- 规格 blob 复算：`git cat-file blob 3340ab3` → sha256 `ea715f9e…9689` 全等＝放行件登记值；199 行／33,748B 全等。
- charter/票面 sha 全等核对通过（票面 85 行／`f31f72b7…`）。
- 租约态一：`lease-issuer.py` 查询面 exit 0，ticket hash＝`d1c41947…`（≠CT1 `6bff8c12…`，因 ticket_id 不同，属预期）；`agent-skills/**` 与 `.scratch/**` 拒签 exit 2＝票面闭集承载授权（`86d9963` 裁定 B 先例，未开新裁量）。
- 基线四组钉值核对全等：py `62d27687f030…`／1,691 行／85,543B；config `f38dc492f1e9…`／53,829B；夹具 `67fdee3e5dd5…`／2,100 行；七件合计 590 行＋契约面 `git diff 4700456..HEAD` 空。
- 五处病灶行定位核对全等后动工。

## 1. 写集对账（判据 2、13）

name-only 对账＝**施工笔 `8a41d563` 恰 6 件**：

1. `agent-skills/claim-commitment-governance/references/10-contract.md`（W1）
2. `agent-skills/claim-commitment-governance/references/30-gates.md`（W1）
3. `agent-skills/claim-commitment-governance/templates/claim-register.md`（W1）
4. `agent-experts/baigong-software-team/skills/sop/scripts/semantic-governance.py`（W2·CS-1）
5. `agent-experts/baigong-software-team/config/semantic-closed-sets.json`（W3）
6. `.scratch/tickets/2026-11-07-SEMGOV-T1-BUILD-verify.py`（W4）

回执笔＝本件 1 件。两笔封顶＝**未超**（无在途裁定随动笔）。契约其余四件（SKILL.md／20-artifact-mapping／40-provenance-map／outbound-artifact）`git diff` 全空。全部 add/commit 双侧逐路径 pathspec；禁项（`--no-verify`／`--amend`／`reset`／`git add -A`）零使用；期间 `index.lock` 撞锁三次等待至释放（他案在持，未删锁）。在途他案面照登：本笔前另有 FUXI 面并发笔 `1a5a759` 落链（非本席产出，照登）。

## 2. 判据逐条读数（判据 3–12）

### 判据 3 · 10-contract.md 逐字对位

- 行数 225→227（＋2＝修法 1 独立段落位含修法 5 第二句，合 §3 预算）。
- v2 围栏逐字对位（剥 `> ` 前缀后全文 in 检索）：fence#2（修法 1 唯一例外句）in ✓；fence#3（修法 2 替换区间自「此时 `linked_artifacts` 的降级形态条目…」起）in ✓；fence#5（修法 5 封顶适用边界句）in ✓；fence#6（CM-2 修法 1 单列区机检取数口径句）in ✓。
- 旧缝合句「此时 `source:` 面若仍为自由文本」残留＝False；「（行 178）」残债随修法 2 替换区间整体消改＝False（裁定四十八去行号锚留节锚口径）。
- 「不另设字段面」「伪承载」钉句在位 ✓。

### 判据 4 · 30-gates.md 逐字对位

- 行数 100→100；逐行 zip 对比 old/new 全文：差异行恰 1 行且为 `| R2 |` 行。
- R2 行新句＝修法 3 全文逐字在位：「条件格旁路（例外）」✓「与该行 `authority` 取值无关」✓「A4」✓「§9」✓。
- 第一支句／在册解析边界句／production 第三支逐字保留＝True（按「；」分段对 blob 原句逐段 in 检索）；R 行数 17 不变。

### 判据 5 · claim-register.md 逐字对位

- 行数 45→45；注 11 行末追加 CM-2 机检取数口径句逐字在位；`^\d+\.\s` 计数＝11 不变。

### 判据 6 · CS-1 实现 diff 对位

- diff 落位＝`check_r2` 降级形态支内（`if not m:` 之后、`if rec.get("authority") != "unverified":` 之前）插入 `cond_ok` 三条件旁路：`_human(approver)` ∧ `status in _cond_status_set(cs)` ∧ `not _none(expiry)`；helper 复用零复制（无第二份条件判据正文）。
- 四支不吞面（无冒号／kind 未知两支在上方原样 continue；前缀闭集外／REQ-·CMP- 不在册支在下方）＋branch=1／branch=3 逐字不动（diff 仅降级支内一处 hunk）。
- 注释卫生：本次改动注释全部功能描述，零票号／裁定号／案卷字样（CT1 时代「S-1/M-3/QA 黄-3」字样随本次注释重写清出）。
- py_compile OK；py 行数 1,691→1,699（+8＝旁路语句 6 行＋注释 2 行净增）。

### 判据 7 · 护栏四态对抗亲跑（隔离样本·仓外临时目录，样本跑毕已清理）

exc1 骨架（三条件齐＋`authority=binding`＋source:/cite: 双自由文本）四变体（修后校验器 `validate --kind 工作票`）：

| 变体 | exit | R2 free-desc | R7 |
|---|---|---|---|
| 态① approver=none | 1 | ×2（branch=2） | ×1（cond-unmet） |
| 态② status=draft | 1 | ×2 | ×1 |
| 态③ approver=seat:lead | 1 | ×2 | ×1 |
| 态④ expiry=none | 1 | ×2 | ×1 |

四态全＝R2×2＋R7 双咬红 ✓；三条件齐→**exit 0 绿** ✓（旁路≠造绿通道：三条件不齐者双闸兜底）。

### 判据 8 · exc1 修前/修后对拍（H2 式）

- 修前校验器＋修前 config（＝HEAD `180c96f` 两 blob 取到仓外对拍）：exc1 样本 `validate` **exit 1**，违例恰 2 条＝`R2 branch=2 value=free-desc`（source: 与 cite: 各一）＝主记件 `0c697c3` §三 实测读数复现 ✓。
- 修后（当态）：同一样本 **exit 0** ＝语义正确绿 ✓。

### 判据 9 · 四支不吞对抗（行上三条件齐仍在位，旁路不误触）

| 样本 | exit | branch 读数 |
|---|---|---|
| 无冒号条目 | 1 | R2 branch=2（value=裸串） ✓ |
| kind 未知（boguskind:） | 1 | R2 branch=2 ✓ |
| `source:REQ-999` 不在册 | 1 | R2 branch=2 ✓ |
| production 无在册 `artifact:` | 1 | R2 **branch=3** ✓ |

四支全照红、branch 读数不变 ✓（branch=1 面：样本均含 source: 条目故不咬，与既有行为一致）。

### 判据 10 · config 读数

- 重算器（V6 同源再抽取）跑毕写回：`changed: [('30-gates', 'md_table', '编号')]`＝恰 `g12.r_table` 内嵌 gates R2 行一处。
- `git diff --numstat` config＝`1 1`（恰一行 1+/1-）✓；`g10` 等余组重算等值未变 ✓。
- 校验器 `selfcheck`：`groups_compared=34 red=0`＋`mutations_total=4 red=4` exit 0 ✓（W3 重算后复跑）。

### 判据 11 · 夹具读数

- 夹具 diff＝`2 insertions(+), 2 deletions(-)`：仅 `ROW_DIGESTS['c13']` 内 `'R2'`（`6d66ba6a…`→`e48bff7b…`）＋`SEC11_DIGEST`（`b35ca98e…`→`d4dfce09…`）两处按夹具自身 norm/sha 口径重算；其余 digest 复算等值未改（含 `c16`/`c23`/`c24`/`c27` 零随动面复跑等值）。
- 四类读数（均带 `<pkg>` 参数）：
  - `--all agent-skills/claim-commitment-governance`：28 判据全 OK，exit 0；
  - `--mutate`：变异体 244 条（结构面 15＋内容面 229）全咬／假通过 0／MUTATE_FAILED 0／覆盖 28/28，exit 0；
  - `--selfcheck`：自证全绿（内容面变异 229/229 可生效），exit 0；
  - `--stats`：exit 0；七件行数 92/227/52/100/43/45/33＝合计 **592**（590→592 合预算）；靶点 60／REV 对 38；三闸支数 7。

### 判据 12 · 表结构扫描

- 表列数七件全零变化：A=20／B=9／C=7／D=13 ✓。
- 守恒式与判定序文本零动：`## 2. 来源层判定序与相容矩阵` 节存在性＋HEAD/工作区文本对拍，本次 diff 未触及任何守恒式行与判定序段（10-contract 的 diff 仅 §11 区两处 hunk）✓。

## 3. 未预见面登记

本轮施工**零未预见面**：五处病灶行定位核对与 v2 规格全部对位，无停手上报项。CT1 三处先例（c11 探针／D09 锚／T-A3 靶点）对应的豁免面本轮未触碰（c11 豁免层不动、EXPECT_TARGETS 不动、D09 不动）。

## 4. 自查勘正登记

- 判据 4 核验脚本首轮误用 `| \`R2\`` 前缀检索（实际行形如 `| R2 |`）致假阴性读数，修正前缀后复跑取正读数（上表）——核验面勘正，被测件零影响。
- 判据 9 「REQ- 不在册」样本取 `source:REQ-999`（source 前缀闭集内、REQ- 不在册路径）；`CMP-` 同支同码路，不另造样。
- 修前对拍 config 亦取 HEAD blob（修前 py＋修前 config 成对），避免旁路只修一半的混态读数。

## 5. 三态明示

1. 做了没落盘：全部实跑读数在落盘前居会话内存，已随本件落盘；仓外样本目录（对抗样本、修前 blob 副本、规格副本）跑毕清理，仓内零临时文件。
2. 落盘没提交：本件写入后至 add 前为工作区新件态，随回执笔提交即消。
3. 提交没对账：回执笔落链后至查盘三件套（status 他案照登＋尾笔对上回报 sha＋name-only 恰本票一件）实测前。

## 6. 收口声明

判据 1–13 自验收全过；两笔封顶（施工笔 `8a41d563` 恰 6 件＋回执笔恰 1 件）。收口即停：QA fresh eyes／拆仓澄清件复跑兜底闸／对照表候裁项均不在本票射程，不越权预跑。
