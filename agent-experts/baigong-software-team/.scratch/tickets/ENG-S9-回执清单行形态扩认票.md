# ENG-S9 回执清单行形态扩认票（工程师席·交付面写入）

- 开端读数：devkits HEAD 以本票 commit 实测为准。
- 声明闭集：
  - `deliverables/skills/object-audit/scripts/check-ticket-reconcile.py`
- 背景（自包含）：S8 真实面收敛 27→1；残 1 笔＝S4 回执清单为编号列表形态（`1. \`路径\`（修改）`），`RECEIPT_PATH_RE` 只收 `|` 表格行→整段解析空→误报「commit 有而清单无缺项」。人工复核实测（S8 回执在册）：4ebfa62 name-only 九件与 S4 回执列表九件全等＝回执与 commit 真实相符，纯工具解析口径残缺。裁决＝**工具扩认编号/项目符号列表形态清单行**（回执体例多样性由工具吸收，与 S7「工具向票面约定对齐」同判）；回执体例不统一（不强推表格）。
- HOLD：无。

## T1 RECEIPT_PATH_RE 扩认

回执清单行抽取扩展：除 `|` 表格行外，接受编号列表（`1. `）与项目符号列表（`- `）行内反引号路径 token（行内括号注记如「（修改）」不并入路径）；表格行既有口径零动；抽取集合去重语义不变。

## T2 selftest 补强

case13：回执清单＝编号列表形态→段二/段三解析成功对账全绿；case14：表格形态回归不回归（既有用例保持）。

## 自检与回执（N4 附载体）

- selftest 全用例（12＋2）全 [OK] exit 0；
- 真实面前后＝修正前（票 31／对账 5／发现 1）→修正后复跑（**发现应归 0 exit 0**；不归零＝逐笔列因上报不硬压）；
- run-gates GATE PASS 全量读数；禁 --no-verify／禁 amend。
- 回执落 `D:\multi-agent-collab-devkits\.collab\research\2026-10-30-ENG-S9-工程师回执-v1.md`，单独 commit（前缀 `collab:`）。

## 红线

只动该脚本一件；三段对账框架零动；残数不遮账。
