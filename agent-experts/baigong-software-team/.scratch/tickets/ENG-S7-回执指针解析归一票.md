# ENG-S7 回执指针解析归一票（工程师席·交付面写入）

- 开端读数：devkits HEAD 以本票 commit 实测为准。
- 声明闭集：
  - `deliverables/skills/object-audit/scripts/check-ticket-reconcile.py`
- 背景（自包含）：ENG-S6 真实面对账 0→3 后新增 3 笔 WATCH＝「票有声明闭集但回执指针解析不到」。根因（S6 回执已登记）：现行票面（ENG-S4/S5/S6）回执落盘路径写作绝对 Windows 路径（`D:\...\.collab\research\...`），而 `find_receipt` 只认相对 `.collab/` 正斜杠反引号路径＝工具面与票面约定不兼容（指针形态面）。执行层缺陷直修。修法判决（主理人）＝**工具面扩认**：`find_receipt` 接受指向 `.collab/` 内的绝对盘符路径（大小写不敏感、反斜杠归一），不改历史票面、票面模板保持绝对路径写法（体例三律②本就要求含盘符完整路径——工具应向票面约定对齐，不是反过来）。
- HOLD：无。

## T1 find_receipt 扩认

`find_receipt` 解析扩展：反引号内路径若为绝对盘符路径（`[A-Za-z]:[\\/]...`），归一化（反斜杠→斜杠、大小写不敏感比对仓根前缀）后落在本仓 `.collab/` 内＝合法回执指针并解析读取；仓外绝对路径＝不算回执指针（现状保持）。三段对账/声明解析（S6 已修形态）/SKIP 语义/退出码零动。

## T2 用例补强

selftest 追加：绝对盘符路径回执票→解析成功对账执行（case8）；仓外绝对路径→不算回执（既有 SKIP/语义如实）。

## 自检与回执（N4 附载体）

- selftest 全用例（含新增）全 [OK] exit 0；
- **真实面前后**：修正前读数（票 29／对账 3／发现 3 WATCH·S6 回执在册）→修正后复跑（对账 3 发现应 0 或残数如实上报——残数＝回执与 commit/声明真实不符，不遮账）；
- run-gates GATE PASS 全量读数（该件 exit 1→0 或残值如实）；禁 --no-verify。
- 回执落 `D:\multi-agent-collab-devkits\.collab\research\2026-10-30-ENG-S7-工程师回执-v1.md`，单独 commit（前缀 `collab:`）。

## 红线

只动该脚本一件；历史票面零触碰；发现真实不符＝上报不遮。
