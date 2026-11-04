# SWB-B5 · 迁移施工票：收尾（gitignore 全量重写＋仓根 README 重写＋D7 登记件入库 docs＋旧壳目录清灭）（施工票·L2·架构席起草）
Status: 已结案（retire 宣告 2026-11-04·依 2026-11-04 审计对齐类免拍板放行裁定·票面退役批 SWB-RET）

- 起草实测 HEAD：`9ae0b8a`（B4 票面笔）；开工 ANCHOR＝B4 收口笔之后可达后继。
- 施工基线真源＝方案 v3 §五 B5 行＋§三 L71（gitignore 两制）＋D7（登记件入库落百工 docs）。
- **开工附注三项（B0 登记照录）**：①誊写禁令 `f5a0d96`：D7 入库＝**字节级复制＋删源**（refs→docs 同仓跨域·git 视角＝新增加＋删除两笔对账，判据＝sha256 与三哈希不变）；gitignore/README＝新建创作类重写（辖域外自察）；②票面落位 `.scratch/tickets`；③era 跨仓（ESC1）。
- 计数口径＝occurrence；判据自带落盘；负例 exit≠0。

## 声明闭集（7 件·本批唯一可写面）
- 声明闭集：
- .gitignore
- README.md（仓根·重写）
- agent-experts/baigong-software-team/docs/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md（D7 入库新位）
- agent-experts/baigong-software-team/.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md（删源笔·若 B3e 曾搬则指彼位）
- deliverables/（壳目录残壳清灭·应为空残留检查）
- docs/（旧仓根 docs 残壳清灭：process/research 内容 B3 已分流，README 索引件删除·内容入回执史述）
- agent-experts/baigong-software-team/bundle.lock（D7 引用锚随动·若涉版本账则三同源＋README append 展开入闭集）

## 逐条施工规格

### B5-A .gitignore 全量重写（v3 L71 两制）
以新树路径重写全文件（旧行全废重立·重写非誊写＝创作类）：
1. 入库面（史实锚）＝各项目 `.collab/{decisions,qa,receipts,board,research}/`＋`docs/`＋`.scratch/tickets/`＋交付面——默认不 ignore；
2. 排除面＝任意层级 `/**/.collab/{refs,evidence,inbox,process,dispatch,backup}/`＋`/**/.collab/tmp-*.txt`＋`__pycache__/ *.pyc`＋系统杂物＋`.workbuddy/`；
3. 负向防御条款（先例 L13/L42–44 形态）＝`!/**/.collab/research/`＋era 留置面若仍在仓根 `.collab/research/` → 显式注记行；
4. 旧仓根条款（`.collab/process/` 等前缀系）全部退役——回执附新旧条款映射表。

### B5-B 仓根 README 重写（白名单结构＋名录＋跨项目案卷索引）
新 README 四节：①仓性质一句话＋姊妹仓/远端段（旧件随迁句）；②仓根白名单结构表（README＋tools＋三分类·v3 §一照态）；③项目名录七行（分类/项目 id/一句话/版本线）；④**跨项目案卷索引**＝「跨项目案卷按参与项目归档＋本索引只指不搬」（B0 前主理人口径）：decisions/research 归桶表逐名指针（B3c2 回执表为源）。旧 README 治理约定六节随迁移分账：仍有效条款并入或指 ES 定标/规范件真源（指针不复写）。

### B5-C D7 登记件入库（v3 D7·裁定三§二点八落点）
1. 字节级复制：`cp <暂住位>/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md → agent-experts/baigong-software-team/docs/` ＋删源（refs 暂住位）。
2. 三哈希不变断言（V13 恒等式零扰动——文件搬家不挪内容＝D5 既裁实证面）。
3. 引用随动：全仓对旧暂住路径的引用串（ES v2 R 账 23 处基线经 B3a 后余量）逐处改新 docs 位；活引用清零断言入判据。
4. bundle 面引用随动：`skills/sop/references/{product,architecture}-v2.9-copy.md` 头注「源路径」两处改 docs 新位（来源注刷新＝交付面变更→三同源 bump 0.1.18→0.1.19＋README append 行）。

### B5-D 旧壳清灭
`deliverables/`、旧 `docs/` 残壳确认空/仅剩索引件 → 删除（`git rm` 索引件·空目录随空自灭）；判据＝顶层目录集＝白名单终态。

## 验收判据（全部机械可判·自带落盘·负例 exit≠0）
1. **顶层终态白名单断言**：`ls -d */ > $B5_TMP/c1.out` → {agent-experts, agent-skills, softwares, tools}＋点目录；`deliverables|docs`（旧）出现＝exit 1。
2. **check-ignore 抽查矩阵**：`git check-ignore` 逐形态 exit 码断言——项目 `.collab/decisions/x.md`≠ignore／`.collab/refs/y`＝ignore／`.scratch/tickets/z.md`≠ignore／`docs/PRODUCT.md`≠ignore（≥8 形态矩阵落盘）。
3. **D7 字节一致**：新位 sha256＝迁移前登记 sha256（开工首步落盘基线）＋三哈希（全文/产品段/架构段）逐字等 `3f335333…/7214ad14…/efb4f765…`。
4. **旧路径引用清零**：`grep -rno "refs/external/SWB-交接件v2\.9[^\"' )]*" . --include='*.md' | grep -v 回执史述豁免 | wc -l`＝0。
5. **README 索引完整性**：仓根 README 项目名录行数＝7；跨项目案卷索引行数≥B3c2 回执表行数（python 计数 exit 0）。
6. **门禁零回归＋六演练全绿**（对开工基线）。
7. **版本三同源 0.1.19**＋README append-only（前后读数）。

## 禁动面
交付面除 B5-C 来源注两件＋版本账外零触碰；各项目 `.collab`/`.scratch` 案卷内容零触碰（只索引不改）；`tools/`；era 留置面（ESC1 域）。

## 候裁点
无。

## 票间关系
前置＝B2/B3/B4 收口。后置＝ESC1（era 跨仓·独立微批随 B4/B5 后）＋B 批收口登记（主理人）＋票面退役批（ES E-ARC-1′ 首跑对象＝B 批六票自身——B 批收口后按 ES 退役程序 retire 或保留至终验，主理人裁）。

## 回执
落 `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-SWB-B5-receipt.md`：开端 HEAD＋name-only 全等＋新旧 gitignore 映射表＋判据 1–7 读数＋D7 哈希链。单独 commit；禁 `--no-verify`、禁 amend。
