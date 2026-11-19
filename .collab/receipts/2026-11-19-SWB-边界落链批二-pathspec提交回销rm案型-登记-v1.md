# SWB 边界落链批二＝pathspec 提交回销 rm --cached 案型登记（v1）

- 时间：2026-11-19 · 登记席：主理人
- 案型：`git rm --cached <批次> `后接 `git commit --pathspec-from-file <批次>`，提交只落了登记件＋ignore 两枚（8942e55f），128 枚摘除被回销、index 现数 783 未减。
- 机理：pathspec 提交的 next-index 按**工作区现态**构造——rm --cached 只改 index、磁盘文件仍在，构造时该面与 HEAD 无差＝不入提交，且提交后 index 被工作区态回写＝摘除效果清零。声明闸读数（next-index 子集 diff）同步只见 2 枚＝闸咬不到此类回销。
- 教训条款候选（候规则票，不入本批）：
  1. `rm --cached` 类摘跟踪投递＝禁 pathspec 提交，只许无 pathspec 提交＋分批 staging（每批 staged 面恰等于声明面）；
  2. 完工回报必查提交面（`git show --name-status` 计数对上声明数）——照「收到完工回报必查盘」纪律，本案主理人自查逮住。
- message 夸面违例自登记：8942e55f message 称「本批 130 枚入账」实入账 2 枚＝措辞比事实快＝登记健康账；禁 amend，以本件＋后续各批如实 message 补正。
- 修正路径（本批即走）：unstage 全部 → 逐批 `git rm --cached --pathspec-from-file` → 无 pathspec `git commit -F`（FX_COMMIT_DECLARE 当批恰声明）。主根 index 仅主根会话在写＝无他席插入窗，卷入闸仍全跑兜底。
