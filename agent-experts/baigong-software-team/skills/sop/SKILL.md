---
name: sop
description: 百工软件团队 SOP 技法域（SWB v2.9 装配）：按需拉取两基线副本（产品设计 v2.9＋架构 v2.9）、三模板（票模板/决策包模板/回流件模板）与 TCB 脚本调用细则。Use when 起草任何票型需要票体四字段自包含结构时／装配决策包或呈报包需要字段格式时／完工回流需要回流四型格式时／席位需要引用产品设计或架构基线条款原文时／查询状态机、租约、串行闸、写侧校验等脚本调用细则时。触发词：票模板、票体四字段、决策包、呈报包、回流件、回流四型、基线副本、架构 v2.9、产品 v2.9、租约、串行闸、验签、影子重放。
agent_created: true
version: 1.0.0
---

# sop · SOP 技法与基线按需拉取索引

本技能按 §5 工件矩阵装填：技法正文、模板、正反例按需拉取；**纪律不装于本技能**（纪律陈述住席位卡一行，强制在脚本与钩子）。

## references 索引（基线整件副本·按需阅读）

- `references/product-v2.9-copy.md`：产品设计 v2.9 本体整件副本（源件一字不改；头注含来源路径与源分段哈希）。
- `references/architecture-v2.9-copy.md`：架构设计 v2.9 本体整件副本（同上）。

引用纪律：引用以 §号＋V13 行号锚定位；副本哈希与基线登记哈希一致方可作引用目标。

## templates 索引（三件）

- `templates/ticket-template.md`：票模板——票型八类清单＋票体四字段自包含结构（目标／规格／验收标准／边界约束）。
- `templates/decision-pack-template.md`：决策包模板——呈报包／full-rollout 包字段格式（与 `scripts/decision-pack.py` 输出对齐）。
- `templates/return-template.md`：回流件模板——回流四型（完成／部分完成／受阻／异常）。

## scripts 索引（TCB 脚本·被调用时查阅其头部规范）

`scripts/` 装 TCB 脚本实体（T02/T03/T04 交付）：`state-transition.py`／`lease-issuer.py`／`intake-register.py`／`reconcile-daily.py`／`promote-manifest.py`／`ledger-init.sh`／`baseline-backfill-demo.py`／`dispatch-builder.py`／`serial-gate.py`／`decision-pack.py`／`write-guard.py`／`commit-audit.py`／`liveness-selfcheck.py`／`freeze-unfreeze.py`／`memory-neutralize.py`／`shadow-replay.py`／`sign-verify.py`。另装语义治理校验脚本 `semantic-governance.py`（SEMGOV-T2 交付·判据真源＝claim-commitment-governance 包 30-gates §2–§3）：三子命令口径＝`validate --artifact <file> --kind <artifact-kind>`（单件 R1/R2/R5/R7/R14/R16）／`reconcile --artifacts <file-list>`（跨件 R3/R10/R11/R12/R13/R17）／`gate-outbound --artifact <file>`（外发前 R4/R6/R8/R9/R15＋人工闸消费点）；exit 0 通过／exit≠0 输出违例字段与判据号。

## 正反例（技法面）

- 正例·票体：四字段各自包含完整语义，下游不读他件即可执行；验收标准行全部机械可判（命令＋期望读数）。
- 反例·票体：验收标准写"质量良好／尽量覆盖"＝不可机械判＝技法失败（做坏了），退回重起草。
- 正例·回流：按四型之一如实申报，受阻态直陈阻塞点与所需输入。
- 反例·回流：以"基本完成"混称态＝越出四型闭集，状态机拒绝登记。
