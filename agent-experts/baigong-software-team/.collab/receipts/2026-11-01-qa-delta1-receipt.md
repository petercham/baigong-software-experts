# Receipt · 2026-11-01 · qa-delta1（SWB v2.7 ↔ bundle QA 视角对照评估票）

- 开工 HEAD 实测：`git rev-parse --short HEAD` ＝ `dfbc47a`（main）。
- 三基线哈希复现（python 段切·LF join 无尾换行）：
  - 全文 L28–278 ＝ e6b80dd535392abe83fba6f12374d97bdc469a48220e727ae93b2917b6f7c594 ✅
  - 产品本体 L53–107 ＝ 2b3675e1601af2f5317ceb701124c8a84728c85e9d66c62da2b6d593b02a5dc8 ✅
  - 架构本体 L108–266 ＝ 1a9febe8f08fcef37e9c09d7f7fc55294746ae704663958895dc3c1ef6ae5aee ✅
- 独立性：未读架构席同题件（`.collab/research/2026-11-01-baigong-bundle-vs-swb-v2.7-delta-v1.md`）；未读 `.collab/qa/` 下 TKT35 在途件。
- 交付件：`.collab/research/2026-11-01-baigong-bundle-vs-swb-v2.7-delta-QA-v1.md`（本票唯一交付文件）＋本 receipt。除此之外零文件改动；工作区两份既有 untracked 汇编件未触碰。
- 读数汇总：正向对照 28 条目＝已有 0／口径差 12／缺失-票包将建 15／缺失-票包不建 1；反向对照 15 条（相撞 3／替换 2／吸收 8／口径差→相撞 1／未提及 1）；CR-QA＝6 条。
- 关键计数双实现：违纪表行 16（shell occ ↔ python 正则）；IS_PASS 11（shell occ ↔ python 累加）；A 侧轮次上限族 10 occ。
- 完工回报：commit 哈希见本 commit（`collab:` 前缀，只含两件）；最高风险 top3＝CR-QA-02 tests/ 写权反转＞CR-QA-01 轮次上限与熔断分母互污＞CR-QA-05 双臂验收结论不可互认。
