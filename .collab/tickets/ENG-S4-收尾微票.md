# ENG-S4 收尾微票（工程师席·交付面写入）

- 开端读数：devkits HEAD 以本票 commit 实测为准。
- 声明闭集：
  - `deliverables/skills/object-audit/scripts/run-gates.sh`
  - `workbuddy/baigong-software-team/agents/software-company-team-lead.md`
  - `workbuddy/baigong-software-team/agents/software-architect.md`
  - `workbuddy/baigong-software-team/agents/software-product-manager.md`
  - `workbuddy/baigong-software-team/agents/software-qa-engineer.md`
  - `workbuddy/baigong-software-team/agents/software-engineer.md`
  - `workbuddy/baigong-software-team/.codebuddy-plugin/plugin.json`
  - `workbuddy/baigong-software-team/bundle.lock`
  - `workbuddy/baigong-software-team/README.md`
- 背景（自包含）：票三 QA PASS 后遗留三项执行面欠账（QA-S3 报告欠-1/欠-2 相关＋MC-SEAT-DECL 真实面 5 命中整改）。均已裁口径，本票纯执行：①新检查器未挂门禁入口；②四席写权边界声明行缺卷名（MC-SEAT-DECL d 条）；③工程师写权边界②句与 dev-discipline §三.1 实测重合 21 CJK（复写嫌疑，J6 判复写线 ≥12）。整改口径＝㊾已拍 J6 数值现行，非新裁。
- HOLD：无。

## T1 run-gates.sh 接线

`deliverables/skills/object-audit/scripts/run-gates.sh` SCRIPTS 段挂 `check-ticket-reconcile.py`（挂接形态与位置照设计件 §4.4：`.collab/research/2026-10-30-票三施工输入设计-v1.md` 9860f64 §4.4；缺省跑＝存量票全 SKIP 属预期）。挂后 run-gates 实跑 GATE PASS，读数如实登记（新检查器 SKIP 26 条走②）。

## T2 四席写权边界声明行补卷名

lead/architect/product/QA 四 MD「写权边界」节现行声明行（QA-S3 读数定位：lead:111／architect:146／product:97／QA:141）行末补「——细则见 dev-discipline」尾串（形态照 engineer 同节既有句例）。语义零改写只补指针。

## T3 engineer 写权边界②句收敛

`software-engineer.md` L154 现句②「②完工回执必须完整包含本次写入/修改的文件清单（对账＝commit 文件清单与回执清单全等）」与 dev-discipline §三.1 实测重合 21 CJK——改写为自指短声明形态（含「本席」＋「dev-discipline」卷名、语义不丢：回执含写入清单＋对账全等、与 §三.1 条文最长连续重合 <12）。改写幅度最小；改后 J6 四读数现跑附值。

## T4 版本账

`plugin.json`＋`bundle.lock`：`0.1.9`→`0.1.10`；`README.md` 版本账 append 一行（体例随现行账行·自包含措辞：run-gates 挂 OA-D6-5 检查器＋席位声明行 J6 收敛整改）。

## 自检与回执（N4 附载体）

- run-gates GATE PASS（挂后全量读数·SKIP 数如实登记）；
- MC-SEAT-DECL 复跑（softdev 调项）＝整改后 5 命中清零或残数如实登记（若 d 条/c 条仍命中＝改写不彻底，继续收敛至 <12 或上报，不得放宽判据）；
- T2/T3 各行 J6 读数（行长/最长重合现跑/grep 双条件）；
- 净增行禁列终式三分账；
- 版本前后值各附实测（0.1.9→0.1.10）。
- 回执落 `D:\multi-agent-collab-devkits\.collab\research\2026-10-30-ENG-S4-工程师回执-v1.md`（开端 HEAD＋清单≡name-only＋全部载体），回执单独 commit（前缀 `collab:`）。

## 红线

只动声明闭集九件；纪律两卷零触碰；skills 三包零触碰（版本账不动——本批未触其内容）；multi-collab 零触碰；席位 MD 只动写权边界节声明行；对整改口径有异议停手上报。
