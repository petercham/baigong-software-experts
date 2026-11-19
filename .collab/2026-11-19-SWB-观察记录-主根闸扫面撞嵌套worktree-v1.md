# 观察记录：主根闸全量扫面撞入嵌套 worktree 运行时空间（v1）

- 立账时间：2026-11-19 18:30 · 立账席：主理人（发现即立，不候拍）
- 现象：批二投递（摘跟踪 baigong 面）提交门 GATE BLOCK＝OA-T1 三枚命中全在 `agent-skills/fuxi-skill/`（README.md 项目名×2＋date×18／share/check-source-of-truth.py drive-path×6）。该面早已摘 main 跟踪＋ignore，盘上现身＝**fuxi worktree 本体**（worktree list 实测：`D:/multi-agent-collab-devkits/agent-skills/fuxi-skill [fuxi/main]`＝边界落链批一「磁盘文件保留原位候 worktree move 接续」已接续）。
- 归因候选（现势证据指向甲）：
  - 甲＝check-entity `iter_scan_files` 沿 `os.walk` 三分类目录，不识别嵌套 git worktree 根（其 `.git` 为文件指回主根 .git/worktrees/），扫入他项目运行时空间规范件。＝主根闸扫描面划界缺陷（S4 动态根只治了钩子根定位，没治全量扫面排除）。
  - 乙＝fuxi 侧规范件自身 OA-T1 违例。不成立：该面在 fuxi 自己的 worktree 由 fuxi 钩子自查，且 fuxi/main 现链干净提交在册（1edfa0df）。
- 影响：边界落链批二投递被闸拦＝主根收尾动作被自家闸卡死；不处理则后续五批全部同拦。
- 临时口径 vs 根因：本轮＝窄修（walk 剪含 `.git` 条目的子目录＝嵌套 worktree 根不入扫面）＝既有语义物理化（主根闸只扫主根管辖面），非新增豁免类别；**非处方**——处方面＝全部全量扫面闸（check-source-of-truth 亦已扫到 fuxi 面 skills:lens-gongqijin 467 findings 靠基线豁免扛着／check-pointers 索引面）统一 worktree 排除口径，归 GTBLOAT 续施射程＋候裁 C-1 同族，随票呈。
- 样本：本轮 3 枚 BLOCK（全部命中件在他项目 worktree 内）＋对照笔＝17:51 同闸 GATE PASS（当时 fuxi 盘上为空）＝撞面随 worktree move 接续而重现。
- 开查触发条件已满足＝影响投递即开查；本记录随窄修笔同链。
