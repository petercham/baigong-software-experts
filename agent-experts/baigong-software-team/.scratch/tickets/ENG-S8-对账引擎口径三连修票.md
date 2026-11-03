# ENG-S8 对账引擎口径三连修票（工程师席·交付面写入）

- 开端读数：devkits HEAD 以本票 commit 实测为准。
- 声明闭集：
  - `deliverables/skills/object-audit/scripts/check-ticket-reconcile.py`
- 背景（自包含）：S7 修通回执指针后对账全执行，显形既有不符（S7 回执「新增残数如实登记」节在册），三源均系工具口径缺陷：①`git show --name-only` 中文名走 core.quotepath 八进制转义未解＝与回执清单（UTF-8 明文）全等比对必不中（段一缺项×3）；②`receipt_commits` 把回执中「票面（开票笔 hash）」行误收成对账 commit 指针（开票笔非交付笔，段一必不中）；③S6 多行列表声明解析对列表头贪心过度——紧随的普通叙述行（`- 背景…`／`- HOLD：无。`）被收进声明集（段三杂项 7＋笔）。执行层口径直修，一票清完防打地鼠。
- HOLD：无。

## T1 quotepath 解转义

所有 `git show --name-only` 类调用改走 `git -c core.quotepath=false ...`（或等效解码八进制转义），使中文名输出与回执 UTF-8 明文可比。

## T2 段一 commit 指针收集口径

`receipt_commits` 只收**交付笔**指针：行内含「交付」/「代码笔」/「实装」类交付标记＋hex（7-40 位）者入集；「开端 HEAD」「票面」「回执」行不入（回执笔自对账另循既有渠道如既有则保持）。口径写进 docstring。

## T3 声明列表条目收紧

多行列表 `- ` 条目仅当为**路径形态**才入声明集：含 `/` 或 `\` 或以已知扩展名结尾（.md/.py/.sh/.json/.lock/.txt）；纯叙述行（`- 背景…`／`- HOLD…`）不入。单行形态口径不动。

## T4 selftest 补强

case10：中文名文件票面（git quotepath 场景）→段一匹配成功；case11：回执含「票面（hash）」行→不入对账集不误报；case12：声明列表夹叙述行→声明集只含路径条目。合成票内嵌同现行体例。

## 自检与回执（N4 附载体）

- selftest 全用例（九＋三）全 [OK] exit 0；
- **真实面前后**：修正前（S7 终态实测：票 30／对账 4／发现 26）→修正后复跑（发现应大幅收敛；**残数逐笔列因**＝若暴露回执与 commit 真实不符（清单真缺项）＝如实上报不遮账不硬压，属施工纪律真问题按 E-4 通道呈）；
- run-gates GATE PASS 全量读数＋该件 exit 码前后；禁 --no-verify；**禁 amend**（改错另起 append 笔）。
- 回执落 `D:\multi-agent-collab-devkits\.collab\research\2026-10-30-ENG-S8-工程师回执-v1.md`（开端 HEAD＋清单≡name-only＋真实面前后对比＋残数因表），单独 commit（前缀 `collab:`）。

## 红线

只动该脚本一件；三段对账/基面分段/SKIP/退出码框架零动（只修三个收集/比较口径）；残数不遮账。
