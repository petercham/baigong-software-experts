# ENG-S6 声明闭集解析修正票（工程师席·交付面写入）

- 开端读数：devkits HEAD 以本票 commit 实测为准。
- 声明闭集：
  - `deliverables/skills/object-audit/scripts/check-ticket-reconcile.py`
- 背景（自包含）：QA-S45 核验发现（黄-1/黄-2）：`check-ticket-reconcile.py` 的 `DECL_LINE_RE` 只认单行「声明闭集：a、b」形态；票面模板 v2 与 ENG-S4/ENG-S5 实际采用**多行列表**形态（「声明闭集：」行＋后续 `- 路径` 行）——实测两票解析读数为空被计 SKIP「缺声明」。后果＝OA-D6-5 三段对账对真实票面全数未执行（对账 0），检查器进门禁后对最新票亦零对账效力；selftest 全绿仅因合成用例用单行形态。修法＝**工具面接受两形态**（单行＋多行列表），票面形态不改（模板 v2 多行列表为现行约定）。执行层缺陷＝施工票直修，非候裁面。
- HOLD：无。

## T1 check-ticket-reconcile.py 解析修正

`DECL_LINE_RE` 解析逻辑扩展＝识别「声明闭集：」行后紧随的列表行（`- ` 起）为闭集条目，直至空行/非列表行止；单行「声明闭集：a、b」既有形态保持兼容。其余逻辑（三段对账/基面分段/SKIP 语义/退出码）零动。

## T2 用例补强

`--selftest` 追加用例：多行列表形态票面→解析成功对账执行（case6_multiline_ok）；「声明闭集：」行后无列表行→仍 SKIP。合成票面内嵌于脚本（同现行自包含体例）。

## 自检与回执（N4 附载体）

- `--selftest` 全用例（含新增）全 [OK] exit 0；
- **真实面读数前后**：修正前 HEAD 全量跑 `check-ticket-reconcile.py`（票 29／对账 0／SKIP 29 现态如实附值）→修正后复跑（对账应覆盖含声明行的现行票＝ENG-S3/S4/S5 等笔，SKIP 数下降，逐票读数入回执）；
- run-gates GATE PASS（挂链后全量读数）；禁 --no-verify，笔笔过闸。
- 回执落 `D:\multi-agent-collab-devkits\.collab\research\2026-10-30-ENG-S6-工程师回执-v1.md`（开端 HEAD＋清单≡name-only＋真实面前后对比表），单独 commit（前缀 `collab:`）。

## 红线

只动该脚本一件；三段对账判据语义零动（只修解析）；对账发现新增违例（真实票回执/commit 与声明不符）＝如实登记上报不遮账——修解析不是修结果。
