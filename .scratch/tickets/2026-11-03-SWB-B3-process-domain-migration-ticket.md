# SWB-B3 · 迁移施工票：过程域搬家（换锚先行→tickets 搬家→案卷分桶→未入库大块）（施工票·L2·架构席起草）
Status: 已结案（retire 宣告 2026-11-04·依 2026-11-04 审计对齐类免拍板放行裁定·票面退役批 SWB-RET）

- 起草实测 HEAD：`f017a51`（B2 票面笔）；开工 ANCHOR＝B2 收口笔之后可达后继。B3a（换锚先行）跑绿前 B3b（tickets mv）**禁启动**（硬线·B0 登记照录）。
- 施工基线真源＝方案 v3（B0 冻结态）§三表 L60–70＋§五 B3 行＋裁定 `f135855`。
- **开工附注三项（B0 登记照录）**：①誊写禁令 `f5a0d96`：仓内一律 `git mv`（tracked）／文件系统 mv＝字节搬运（untracked）；判据＝新位与原位 diff＝空；②票面落位 `.scratch/tickets`（项目内）；③era 跨仓＝ESC1 独立微批（不在本票）。
- 计数口径＝occurrence；判据自带落盘；负例 exit≠0。基线读数锚 HEAD=`f017a51` 实测：tickets 85／qa 159（＋2 untracked）／receipts 51／decisions 16／design 24／research 242／board 1／根散件 17（tracked 合计 **597**）；refs 8835／evidence 3827／inbox 9／dispatch 10（untracked 文件系统面）。

## 归项目分账函数（机械口径·全票统一·回执附逐件分桶表）
按基名正则**顺序**判定（首中即停）：
1. 名含 `SWB` 或 `TKT` 或 `SWBFIX` → **baigong**（TKT 系＝SWB 分票案卷线——勘误注记：v3 L70 将两支 untracked TKT 件标 fuxi，与分账函数冲突＝分账函数为准，v3 该行按 erratum 登记回执，不静默改基线）；
2. 名含 `FUXI` → **fuxi-skill**；
3. 名含 `EAC` 或 `外部顾问` → **external-advisor-collab**；
4. 名含 `SOP|ENG-|QA-|ARCH|MC-|GH-|DIRRELOC|GATE1|产品席|架构席|软开团|席位|装配面|机检链|纯净性|活文档|收尾批` → **baigong**；
5. 名含 `视频|video|短剧|导演|编剧`（era 族） → **ESC1 移交清单候选**（本票不搬）；
6. 其余＝**人工分账面**：回执逐件列表＋默认归 **baigong**（仓级/软开线缺省桶＝v3 L62「纯仓级归百工」口径）。

## 声明闭集（目录级申报·本批唯一可写面）
- 声明闭集：
- .collab/tickets/ → 各项目 .scratch/tickets/（git mv）
- .collab/qa/ receipts/ board/ design/ 及 .collab/ 根 17 散件 → 各项目 .collab/<同桶>/（git mv）
- .collab/decisions/ 16 件 → 按 B3c2 归项目 `.collab/decisions/`（git mv）
- .collab/research/ 非 era 件 → 各项目 .collab/research/（git mv；era 候选留置）
- .collab/refs/ evidence/ inbox/ dispatch/ process/ → 各项目 .collab/<同桶>/（文件系统 mv·untracked 面）
- 随动改锚文本面＝B3a 清单（回执逐处）＋.scratch/tickets/README.md

## 逐条施工规格

### B3a 换锚先行（硬线前置·单独 commit）
1. 全引用族路径串改写：`.collab/tickets/` 前缀引用 → 目标项目 `.scratch/tickets/` 前缀——扫描面＝receipts／qa／design／decisions／dispatch／docs／仓根 README／deliverables（含 spec_file 头块 check-collab-lint 三处 EAC-SK5 机检票锚＝**Y-7 闭环化换锚先行**先例口径，改指其换锚后新位）；裸票 ID 基名族零改（非路径语义·ES v2 R3 账豁免口径）。
2. 跑绿判据（下判据 1）后 B3a 收笔，B3b 方准开工。

### B3b tickets 搬家（git mv·按分账函数）
`git mv .collab/tickets/<file> <项目>/.scratch/tickets/<file>` 逐笔批量；`.collab/tickets/` 目录随空自灭。Matt Pocock 式头部转换（Status/Blocked-by 行）**不做**（随裁项＝否·回执登记一行）。

### B3c 案卷桶搬家（git mv）
qa/receipts/board/design 四桶按分账函数入 `<项目>/.collab/<同桶>/`。
**根 17 散件归桶定标**（固定结构闭集无 `cases/` 桶＝不新增桶，B1-D 规范红线）：逐件按内容形态归同名桶——收口报告类→`receipts/`；会师/收口/冻结**登记**类→`receipts/`（登记件＝质量链过程账，非裁决本体；裁决本体只在 decisions）；呈报/呈拍简报类→`receipts/`；裁定/拍板/裁决件形态＝不存在于根面（历来在 decisions）；脏文件处置注记→`receipts/`。即根散件 17 件全部归所属项目 `.collab/receipts/`，逐件回执表列名对位。

### B3c2 decisions 归项目（v3 L62 口径·16 件逐件回执表）
裁决涉及面判定＝件内裁项主语：涉 SWB 机制/百工 bundle/仓级目录与入库策略/版本线 → **baigong**；涉 FUXI → **fuxi-skill**；涉 EAC → **external-advisor-collab**；跨项目无法单归者（如裁决记录 2026-10-22 系早期混合案）→ **baigong**（仓级缺省桶）＋仓根 README 跨项目案卷索引一行（索引行 B5 落笔·票内登记待并清单）。`verdicts.md` 单件＝判词面随 baigong。

### B3d research 分桶（git mv）
非 era 按分账函数入项目；era 候选（正则 5 命中）＝**留置原位** `.collab/research/`，列 ESC1 移交清单附件。

### B3e 未入库大块（文件系统 mv·untracked）
`mv .collab/refs/<x> <项目>/.collab/refs/`、evidence/inbox/dispatch/process 同式；refs 三子桶（external/engine-snapshots/skills-research）按判词依据项目归（external SWB 系→baigong·快照/技能调研→external-advisor-collab＋回执分账）。`.gitignore` B1 过渡块已覆盖任意层级——零改。

### B3f D7 衔接注记（不施工）
SWB 登记件 v2.9 现暂住 baigong/.collab/refs/external/（随 B3e 搬家）——**入库落 docs 归 B5**（v3 D7），本票只保搬家字节一致。

### 随动改锚（B3b/B3c 后·同批尾笔）
仓根 `.scratch/tickets/README.md` 更新（过渡票目录仅剩 B 批票·注记）；B1/B2 票内旧路径引用**不改**（史述票面）。

## 验收判据（全部机械可判·自带落盘·负例 exit≠0）
1. **B3a 跑绿＝mv 前置断言**：`grep -rno "\.collab/tickets/" . --include='*.md' --include='*.py' --include='*.sh' --include='*.json' | grep -v "^\./\.collab/tickets/" | grep -v "^\./\.scratch/" | wc -l` ＝ **0**（豁免清单＝票面史述逐处入回执）；未 0＝B3b 禁启动。
2. **tracked 总数守恒**：迁前 597 → 迁后 `git ls-files | grep "\.collab/\|\.scratch/" | wc -l` ＝ 597＋2（两支 untracked 入库）－0；逐桶表前后相等（tickets 85＝Σ项目 .scratch/tickets；qa 159＋2＝Σqa…）。
3. **字节一致**：B3b/B3c/B3d 各笔 `git show -M --name-status` R100 占比 100%（例外＝无；改锚笔单走不混 mv 笔）。
4. **untracked 面守恒**：迁前 find 计数基线（refs 8835／evidence 3827／inbox 9／dispatch 10）→ 迁后 Σ项目同名桶 find 计数和＝基线（era 留置件计入 research 侧对账）。
5. **旧域清零**：`find .collab -type f | wc -l` ＝ era 留置数＋0（其余全空）；`find .collab/tickets 2>/dev/null | wc -l`＝0（目录灭）。
6. **门禁零回归**：run-gates GATE PASS 对开工基线零新增族（check-ticket-reconcile 此时仍扫旧缺省＝B3a 后旧目录已空→其「扫描面非空」危险形态预告＝B4 必修目·B3 回执登记该窗口读数非绿不判红＝过渡态在册）。
7. **两支 untracked 入库**：`git ls-files | grep -c "2026-11-01-TKT"`＝2（归桶按分账函数＝baigong·v3 L70 erratum 回执登记）。

## 禁动面
交付面文件内容（除 B3a 改锚文本行）、`docs/`（旧仓根·B5）、`tools/`、仓根 README（B5）、era 留置 research 内容、`agent-*/` 内 B1/B2 成品结构。

## 候裁点
无。归桶争议＝人工分账面走回执清单＋主理人核销，不上呈皮总（执行层）。

## 票间关系
前置＝B2 收口。后置＝B4（票目录缺省改造依赖 B3b 完成态）、ESC1（era 清单依赖 B3d）。

## 回执
落 `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-SWB-B3-receipt.md`：开端 HEAD＋逐笔 name-status＋逐桶对账表（含人工分账清单＋v3 L70 erratum＋era 留置清单）＋判据 1–7 读数。B3a 单独 commit；B3b–e 分笔 commit（`collab:`）；禁 `--no-verify`、禁 amend。
