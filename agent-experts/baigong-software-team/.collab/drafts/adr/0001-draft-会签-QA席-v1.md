# ADR-0001 草案会签件 · QA 席 v1（qa-adrlrev·会签三席之 QA 席·独立口径）

- 被签对象＝`.collab/drafts/adr/0001-adr-initiation-trigger-criteria-draft.md`（草案笔 `5a1b2fc`）。
- 开工读数：`git rev-parse --short HEAD`＝`5a1b2fc`；`git status --porcelain`＝他席在途三行（`?? .collab/ledger/`、`?? .scratch/eng-adrl0/`、`?? .scratch/structfix/`），本席名下净。
- 草案 sha256 实测复现＝`9a2c90e32b8535e1bfcdf61cd8508b9e3cc5e7f606982c5a3d0623277b922564`（4385 字节）＝派单钉值全等 ✓。
- 独立性：未读产品席会签件；判据文本基准＝票面修订笔覆盖后终态（`ebdb8b4` 修订笔 v1 段，本席 R-1/黄-4 修法出自本席前审 `d934b27`，本次不复用旧结论、全部重跑）。
- 口径＝occurrence；临时复测面＝`.scratch/qa-adr0001/`（完工已删，读数附下）。

## 表态

**完全认可**（附观察两项·非保留项、不拦终写；保留项语义＝未闭合禁终写，本席无未闭合项）。

自指合法性注记段逐席表态（S4.1 要求）：**认可**——本 ADR 记录对象＝「判据立项」决策自身，命中 T4（新增工序入口闸＝工序环节新增）按判据而立＝合法自指；自证点成立：判据辖运行时决策之立项时机、不辖记录件自身诞生形态，无循环——先后由同批链序固定（判据文本先随 SOP 落包票成文、本草案后笔，现盘链序实证：修订笔 `ebdb8b4` 先于草案笔 `5a1b2fc`）。

## 会签三问判定

### 问一（判据本体逐字对等）＝绿·零出入

实跑＝python 逐行逐字节 diff：票面 S1 围栏块（票面 L40-52 原笔体）应用修订笔条目4（「按入线四词 grep」→「按入线四词的关键词 grep」）后去行首三空格缩进，vs 草案决策节围栏块（草案 L24-35）：

- 行数＝12 vs 12；**去缩进后逐字节全等**＝True；
- 两块 sha256（去缩进后）＝`66e18afabedd7cd6…` 两方全等；
- 锚句 occurrence（草案全件）＝T1／T2／T3／T4／N1／N2／N3／混合件＝拆分处理／覆盖链／申诉线 各＝**1**（十锚全中）；
- 申诉线四字态（「入线四词的关键词」）＝在位（修订笔复原态与草案一致＝票面自设「＝调研成文」等式已闭合）；
- 逐行 diff 输出＝零字节差（唯一形态差＝票面块带 3 空格列表缩进、草案块顶格——围栏内缩进属载体层非文本层，终写落 docs/adr 后该形态即真源，不构成出入）。

**结论：判据本体无任何非授权出入。**

### 问二（E-ADR 机件预检·对修订笔终态 OA-E-ADR-N 口径）＝绿·全断言可过

机件现盘态（HEAD `5a1b2fc`）：`check-adr.py` 未落（S3 工程师段在途·a2198e6 路由登记在册）、50-document `E-ADR` 命中＝0、60-gates `OA-E-ADR` 命中＝0——＝本问为**预检预测**，逐项对表：

| 断言（OA-E-ADR-N 终态口径） | 草案对表读数 | 终写后预测 |
|---|---|---|
| OA-E-ADR-1（头块五行·前 12 行内·Status 闭集） | L5-L9 五行全中（`head -12 \| grep -c "^- (Status\|Deciders\|Date\|Author\|Registrar)："`＝**5**）；`Status：Accepted`∈闭集；Date 行＝``- Date：`2026-11-05```反引号包裹——按票面 §口径1 校验器遮反引号后匹配口径可过 | **实过** |
| OA-E-ADR-2（文件名四位正断言＋唯一＋新号＝最大＋1） | 终写落位名 `0001-adr-initiation-trigger-criteria.md` 匹配 `^(\d{4})-[A-Za-z0-9._-]+\.md$`（本席前审已仿真该正则，本名正例命中）；首支＝提取集 {0001} 唯一、0001＝既有最大(空集取0)＋1 | **实过** |
| OA-E-ADR-3（supersede 双向＋adr 内 `.collab/…` 活引用补偿） | `- Supersedes：`行缺省不设（草案 L11 明示注记）＝无出边；Status 无 `Superseded by`＝无入边＝双向图空＝真空真；草案 `.collab/` 引用 grep＝**0**＝补偿断言无对象＝真空真 | **真空真** |
| OA-E-ADR-4（accepted 不可变＋diff 白名单） | 首写笔＝新文件无历史 diff＝白名单机制不适用（约束对未来 diff 生效） | **真空真**（首笔）／此后各笔实判 |
| OA-E-ADR-5（三桶对账和式·根锚＝修订笔条目3 四序：bundle.lock 定位） | 现盘 bundle 根锚基线复测：桶1＝0／桶2（排除 verdicts.md）＝19／桶3＝1／和式＝20 ✓（与票面基线全等）；挂载态 run-gates 传仓根 `--root` 经四序③自解 bundle.lock→按 bundle 根算＝本席前审 Y-3 两炸路（仓根真空真摆设／仓根无 verdicts.md exit1）均被封 | 终写后桶1＝1→**1+19+1＝21 实过**（会签链若致 decisions 增件按 A7 实测登记） |

- 头块行位复核：五行居 L5-L9（前 12 行内 ✓）；Supersedes 缺省注记居 L11（不影响 E-ADR-1 五行判定）。
- 无发现不可过项。**预测终写笔 pre-commit 时和式读数＝21**（终写笔 index 含新件＝`git ls-files` 索引态已含，桶1 计数无时序洞）。

### 问三（载体纪律）＝绿·全零命中

本席亲跑（非采信起草席预跑）：

- **OA-T1 真判据链复跑**＝草案逐字节复制入探针树 `agent-experts/baigong-software-team/docs/adr/0001-adr-initiation-trigger-criteria.md`（模拟终写落位态），`python agent-skills/object-audit/scripts/check-entity.py --root .scratch/qa-adr0001/probe`：date／drive-path／discipline-no／ticket-no **四模式 count 全＝0**，**exit 0**——裸日期命中＝**0** ✓（Date 行反引号遮除生效、正文无裸日期、`YYYY-MM-DD` 未现）。
- **㊺指针闭集 grep（草案全件）**：`.collab/`＝**0** ✓；票面/案卷路径（`tickets/`、`.scratch/`）＝**0** ✓；票号形态 `\bT-?\d{3}\b`＝**0** ✓。背景节两处实锤改为自包含成文陈述（无路径指针）＝符合闭集纪律。

## 观察两项（非保留·不拦终写·回执可随带）

1. **背景节「『触发』五处」计数口径**：草案 L15 承票面称 ADR 工序票全文「触发」五处——本席实测＝行读数 5（grep -n 行号 15/60/100/125/127）、**occurrence 读数 6**（L125 行内含两处）。实质结论独立复核成立（六处全为挂载时序/候裁射程语义、零立项触发语义）。＝史述计数口径小疵，承自票面与调研，非判据本体，不改会签结论。
2. **正文两处反引号裸基名/自路径引用**（`standard-sop.md`、`docs/adr/0001-…`）：终写后 check-pointers 对 `docs/adr/` 面的解析——裸基名走基名索引、自路径相对本件目录解析——advisory 级观察，实跑读数待工程师段终面 A3/A6 对拍，无阻断向。

## 自检与清理

- 临时面＝`.scratch/qa-adr0001/`（探针树＋check-entity 输出），已删；清理读数＝`ls .scratch/ | grep -c qa-adr0001`＝**0**；仓外系统 Temp 零新建（本席全程未写仓外路径）。
- 本席除本会签件外零文件改动；commit＝本件单独一笔（`collab:` 前缀·pathspec 限本件·`git diff --cached --name-only` 自证 index 仅本件·未用 --no-verify/amend）。
- 禁读产品席会签件＝未读；与产品席并行独立。
- 会签签署入账＝账本签字通道（state-transition.py·归主理人落账，本席不代登）。
