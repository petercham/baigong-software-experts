# ENG-S5 自咬预期同步票（工程师席·交付面写入）

- 开端读数：devkits HEAD 以本票 commit 实测为准。
- 声明闭集：
  - `tools/check-source-of-truth.py`
- 背景（自包含）：ENG-S4 将席位声明行 MC-SEAT-DECL 真实面命中 5→0 清零后，`--selftest-seatdecl` 内嵌用例 case1_real_seats 的预期值仍是整改前现态快照 5，实跑 0 → MISMATCH exit 1（回执 4ebfa62/df97bb6 已登记读数）。预期系现态快照同步，非判据改动。
- HOLD：无。

## T1（唯一改动）

`tools/check-source-of-truth.py` 内 `--selftest-seatdecl` 用例 case1_real_seats 预期值 5→0（现盘定位：selftest 段用例表；只改该数值与其紧邻注释中的现态注记，判据常量 MIN_CJK=12／QUOTE_EXEMPT_MAX=10／grep 双条件／≥15 回裁线零动）。

## 自检与回执（N4 附载体）

- `--selftest-seatdecl` 五用例全 [OK] exit 0（附读数）；
- MC-SEAT-DECL softdev 调项实跑仍 0 命中（判据零动实证·附读数）；
- run-gates GATE PASS（附读数·禁 --no-verify，笔笔过闸）。
- 回执落 `D:\multi-agent-collab-devkits\.collab\research\2026-10-30-ENG-S5-工程师回执-v1.md`（开端 HEAD＋清单≡name-only＋载体），单独 commit（前缀 `collab:`）。

## 红线

只动该一件；该文件其余逻辑零动；判据常量零动——对判据数值有异议停手上报（数值属拍板面非执行面）。
