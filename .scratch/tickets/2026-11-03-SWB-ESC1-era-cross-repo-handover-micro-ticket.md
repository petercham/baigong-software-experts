# SWB-ESC1 · 迁移施工票：era 外部参照件跨仓移交微批（devkits → experts 仓·两仓两笔字节对账）
Status: 已结案（retire 宣告 2026-11-04·依 2026-11-04 审计对齐类免拍板放行裁定·票面退役批 SWB-RET）

- 本件＝ESC1 独立微批票（**会师件 `3ad4d99` §三.1 补票裁定＝从严向一次到位**；B0 清残注记二＝执行项定性不变·不上呈皮总）。
- 起草实测 HEAD：`cccc0b7`；开工 ANCHOR＝B 批任一封口后主理人排程点（与 B5 互不阻塞·B5 rev2 补丁四两态口径在册）。
- 施工基线真源＝v3 §三 L65 行（「视频团 era 外部参照件整体移交 experts 仓」）＋裁定 `f5a0d96`（誊写禁令·跨仓＝字节级复制＋删源＋两仓两笔字节对账）＋era 跨仓口径开工附注③（B 批五票照载同源）。
- **移交清单真源＝B3 rev2 回执「era 留置清单·出处二次分账表」**（B3 rev2 补丁五之 3：第三方外部快照＝移交候选／本仓自产＝不外移留项目桶）；本票开工首步＝从该回执抽取在册清单落盘 `$ESC1_TMP/handover-list.tsv`（件数钉值＝回执行数·开工实测登记）。
- 接收仓＝`D:\multi-agent-collab-experts`（下称 experts 仓）；计数口径＝occurrence；判据自带落盘；负例 exit≠0。

## 声明闭集（两仓两面·本批唯一可写面）

devkits 侧：
- era 留置面删除笔＝`agent-experts/baigong-software-team/.collab/research/`（B3 后新位）内清单命中件（tracked→`git rm`；untracked→文件系统删）
- （若 era 仍留置仓根 `.collab/research/`＝ESC1 先于 B3 执行的异常序）＝仓根留置位删源——开工以 B3 回执态定位

experts 侧：
- `research/era-2026-10/<逐件>`（接收落位闭集·命名零改＝字节对账可机械比对；若 experts 仓既有目录规范异→开工以该仓 README/结构件定落位并回执登记，件名基名仍零改）
- experts 仓 `.gitignore`（若其无 research/ 入库条款则免动·开工读其现面定案）

## 逐条施工规格

### ESC1-A 清单锁定（先行单独笔·devkits 侧只读）
1. 从 B3 rev2 回执表抽取移交候选逐件名＋sha256 落盘 `handover-list.tsv`（三列：基名/原位/sha256）。
2. 自产件二次甄别复核（出处口径＝件头来源声明/源料说明）＝回执逐件签字列；争议件＝留置不搬＋主理人核销行（缺省不外移＝真源离仓风险优先规避）。

### ESC1-B 字节级复制入 experts 仓（experts 侧单独 commit）
1. `cp <devkits 原位> <experts 接收位>` 逐件（禁 Agent 重新输出全文＝`f5a0d96` 铁律）。
2. experts 侧 commit（前缀随该仓纪律·回执登记其 commit hash）＝接收笔。
3. 接收断言：逐件 `sha256sum <experts 接收位>` ＝ handover-list 第三列（全等·落盘对账表）。

### ESC1-C 删源（devkits 侧单独 commit）
1. 断言全绿后方删源：tracked 件 `git rm`（untracked 件文件系统 rm）。
2. devkits 侧 commit（`collab:` 前缀）＝删源笔（回执登记本仓 commit hash＋两仓两笔 hash 并列表）。

### ESC1-D gitignore/索引随动
1. devkits 侧：era 留置面 gitignore 行（B5 已落＝`/.collab/research/reference-2026-10-24/…` 三桶行；若 era 件系 tracked 入库面则删源笔自然清零，ignore 行残留无害·B5 映射表在册）——零改缺省，开工读盘定案。
2. 仓根 README era 索引行（B5-B 第④节）：若 B5 已落「待移交」注记→本票收口后 B 批收口登记标「已移交·ESC1 回执指针」一行（不回头改 README·登记级）。

## 验收判据（全部机械可判·自带落盘·负例 exit≠0）
1. **两仓两笔字节对账**（B0 附注③销账目）：`handover-list.tsv` 行数＝experts 接收 commit `git show --name-only | wc -l`＝devkits 删源 commit `git show --name-only | wc -l`＝N（三值全等·含 untracked 面时删源侧以文件系统计数补账行）。
2. **逐件 sha256 全等**：接收断言表 exit 0；构造异字节负例 exit 1。
3. **devkits 侧清零**：`find <era 留置位> -type f | grep -c <清单基名族>`＝0。
4. **自产件未外移断言**：experts 接收面 `git show --name-only` 与「本仓自产」清单交集＝∅。
5. **无誊写违规**：复制全程 `cp` 命令读数入回执（禁全文重输出自察声明）。

## 禁动面
- devkits：清单外任何件（含 era 相邻自产研究件）；experts 仓既有件内容零触碰（只新增接收）。
- 两仓版本账（experts 仓版本账随其仓纪律，非本票裁）。

## 候裁点
无（era 移交＝执行项既定性；落位细节随 experts 仓结构件＝开工读取非候裁）。

## 票间关系
前置＝B3 rev2（回执清单真源）；与 B5 互不阻塞（两态口径）；后置＝B 批收口登记（四目③凭本票回执销账·登记级 README 注记刷新）。

## 回执
落 `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-SWB-ESC1-receipt.md`：开端 HEAD＋handover-list.tsv 全表＋两仓两笔 commit hash 并列表＋逐件 sha256 对账表＋判据 1–5 读数＋争议留置核销行。ESC1-B/ESC1-C 各单独 commit（跨仓两笔各仓一笔）；禁 `--no-verify`、禁 amend。

——arch-swbreloc · ESC1 微批票（新建创作类·誊写禁令辖域外自察；施工本体全程字节级）。
