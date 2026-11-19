# SWB 窄放行登记＝check-entity 嵌套 worktree 剪枝先行（v1）

- 时间：2026-11-19 · 登记席：主理人
- 先例：SWB-GTFAST R0 提速先行（窄放行登记＝紧急窄修径施径验径登，处方面随票）。
- 动因：边界落链批二投递被提交门 OA-T1 三枚 BLOCK 拦死，命中面全在 fuxi 嵌套 worktree 运行时空间（观察记录 `.collab/2026-11-19-SWB-观察记录-主根闸扫面撞嵌套worktree-v1.md` 在册）。不修则批二后续全部同拦＝主根已裁收尾动作被自家闸卡死。
- 窄修内容（语义物理化·非新增豁免类别）：`share/check-entity.py iter_scan_files` walk 时剪掉三分类目录树下任何含 `.git`（目录或 worktree 指针文件）的子目录整支＝嵌套 git 仓检出面不入主根扫描域。
- 验证读数（现跑）：
  - 修前（闸内缺省注入）：GATE BLOCK 3 枚（README.md:1/:3、share/check-source-of-truth.py:164，全在 fuxi worktree 面）→ 提交拒。
  - 修后：`python3 share/check-entity.py --root .` exit 0、BLOCK 0；闸缺省注入 GATE_PROJECT_NAMES 口径复跑亦 BLOCK 0。
  - 对照：主根管辖面命中零变化（修前一轮 baigong 面命中＝手工注入多项目名非闸口径，不作数）。
- 处方面（非本笔）：全量扫面闸族（check-source-of-truth／check-pointers 索引面）统一 worktree 排除口径＝GTBLOAT 续施射程＋候裁 C-1 同族，随票呈。窄修禁写进真源条文前不入 skill；本笔仅代码窄修＋观察记录＋本登记三枚入账。
- 健康账注：本轮期间他案（百工侧）在主根链连投批一收尾四笔（65867205/13b41b6a/a452f8ad/fe8a9480，ALLOW_GATE_DOWN=1 留痕豁免＝其报闸删除面盲区崩溃在册 `.scratch/2026-11-19-SWB-闸staged靶检删除面崩溃-观察记录-v1.md`）。百工侧在自己 worktree 却向主根 main 投递＋用豁免投删除面＝协作面观察点，不归本笔处理，随 GTBLOAT 会师呈。
