# EAC-SK4 修订票（multi-collab/20-handoff.md·决策/设计类交接件通用判据段）

> 开票＝主理人｜2026-10-30｜接票席＝架构席｜HEAD 基准＝fd88a7b（SK-3 完工后）
> 依据＝皮总拍板㊹——施工序第四票。
> 只改：`deliverables\skills\multi-collab\references\20-handoff.md`＋`multi-collab\references\90-changelog.md`（如该包有 changelog；无则按该包现行登记惯例落一条，先读现文定落点）append。

## 任务（落点 C2）

§二 增「决策/设计类交接件附加判据」小段（不动五规格骨架），内容三件：

1. **三正面判据成文**（通用形态，与 external-advisor-collab/40-artifacts §四之二互指、不复写其讨论会特有禁列）：
   ①引用闭集可达——收件人凭其输入闭集可核对件内一切引用；
   ②无第三方过程痕迹——他席署名/轮次/草案史不入正文（件级来源帽除外）；
   ③状态词只述现行效力——沿革归 changelog。
2. **保护句**：件级来源帽与既有硬性字段（含 `约束：` 行「六道硬约束」串等）不受本判据禁则波及。
3. **互指针**：过程痕迹禁列示例见 external-advisor-collab/references/40-artifacts.md §四之二（单真源：通用判据在此、讨论会特有禁列在彼，双向不重复正文）。

changelog：multi-collab 侧对应登记一行（落点→来历＝20261029a 案交接体例实证＋拍板㊹；仓相对路径口径）。

## 红线
- 五规格骨架 diff＝零改动（只增段）；既有 L12-18 帽规格、L22 硬约束串等一律不动。
- external-advisor-collab 包全部文件零动作（已定稿）。
- 真源内无过程指针措辞；不 bump multi-collab 版本（本次为增段兼容——若该包版本语义惯例要求 bump，先报主理人裁，不擅 bump）。

## 验收
1. 新段存在且三判据＋保护句＋互指针三件齐（grep 短语各 ≥1）；
2. 五规格骨架 diff 空（git diff 面只含新段＋changelog 行）；
3. external-advisor-collab 全包 diff 空；
4. 一次 commit，回报 hash＋读数＋该包登记落点说明。
