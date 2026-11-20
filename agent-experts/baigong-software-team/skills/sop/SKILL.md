---
name: sop
description: 百工软件团队 SOP 技法域（SWB v2.9 装配）：按需拉取两基线副本（产品设计 v2.9＋架构 v2.9）、五模板（票模板/决策包模板/回流件模板/完工回执模板/收口登记模板）与 TCB 脚本调用细则。Use when 起草任何票型需要票体四字段自包含结构时／装配决策包或呈报包需要字段格式时／完工回流需要回流四型格式时／席位需要引用产品设计或架构基线条款原文时／查询状态机、租约、串行闸、写侧校验等脚本调用细则时。触发词：票模板、票体四字段、决策包、呈报包、回流件、回流四型、基线副本、架构 v2.9、产品 v2.9、租约、串行闸、验签、影子重放、完工回执、回执七节、收口登记、收口九节、判据三态、跨实例工单、身份戳、出身锚、claims 认领清单。
agent_created: true
version: 1.0.3
---

# sop · SOP 技法与基线按需拉取索引

本技能按 §5 工件矩阵装填：技法正文、模板、正反例按需拉取；**纪律不装于本技能**（纪律陈述住席位卡一行，强制在脚本与钩子）。

## references 索引（基线整件副本·按需阅读）

- `references/product-v2.9-copy.md`：产品设计 v2.9 本体整件副本（源件一字不改；头注含来源路径与源分段哈希）。
- `references/architecture-v2.9-copy.md`：架构设计 v2.9 本体整件副本（同上）。
- `references/external-ticket-spec.md`：他域工单规范卷——工单体八字段＋效力域五行＋诉求体闭集四型＋状态面闭集＋知会登记面（他域交互工单形制本体·票面形制不归本卷）。
- `references/cross-instance-protocol.md`：跨实例协作与认领协议条款本体（R1—R5：身份戳与出身锚／票号防撞／两向认领与关闭语义／claims 机核清单／跨实例工单体例）。

引用纪律：引用以 §号＋V13 行号锚定位；副本哈希与基线登记哈希一致方可作引用目标。

## templates 索引（五件）

- `templates/ticket-template.md`：票模板——票型九类清单＋票体四字段自包含结构（目标／规格／验收标准／边界约束）。
- `templates/decision-pack-template.md`：决策包模板——呈报包／full-rollout 包字段格式（与 `scripts/decision-pack.py` 输出对齐）。
- `templates/return-template.md`：回流件模板——回流四型（完成／部分完成／受阻／异常）。
- `templates/receipt-template.md`：完工回执模板——实占七节骨架（开工读数／施工读数／V 系读数／禁动面坐实／取证族拆除／案型登记／纪律自证）＋receipts 桶命名现占口径。
- `templates/closeout-template.md`：收口登记模板——实占九节骨架（开工读数／链账表／债销账／基线随动／随登随正案型／遗留随登／判据处置三态列／观察随登／批次面纪律自证）＋decisions 桶命名现占口径＋链账表生成指引。
索引枚数自校（预置·复算口径）：两基线副本／五模板／scripts 枚数断言以现跑为准（references 以 grep v2.9-copy 子集计数为口径＝恰 2·禁以 ls 全目录计数·templates 与 scripts 以 ls 目录计数）；目录增删＝本索引与计数随动。

## scripts 索引（TCB 脚本·被调用时查阅其头部规范）

`scripts/` 装 TCB 脚本实体（T02/T03/T04 交付）：`state-transition.py`／`lease-issuer.py`／`intake-register.py`／`reconcile-daily.py`／`promote-manifest.py`／`ledger-init.sh`／`baseline-backfill-demo.py`／`dispatch-builder.py`／`serial-gate.py`／`decision-pack.py`／`write-guard.py`／`commit-audit.py`／`liveness-selfcheck.py`／`freeze-unfreeze.py`／`memory-neutralize.py`／`shadow-replay.py`／`sign-verify.py`／`check-ticket.py`。另装语义治理校验脚本 `semantic-governance.py`（SEMGOV-T2 交付·判据真源＝claim-commitment-governance 包 30-gates §2–§3）：三子命令口径＝`validate --artifact <file> --kind <artifact-kind>`（单件 R1/R2/R5/R7/R14/R16）／`reconcile --artifacts <file-list>`（跨件 R3/R10/R11/R12/R13/R17）／`gate-outbound --artifact <file>`（外发前 R4/R6/R8/R9/R15＋人工闸消费点）；exit 0 通过／exit≠0 输出违例字段与判据号。
工具归属定版（ITER-W2-T2e·计划行 124 G7 口径）＝本包 scripts 桶为 check-ticket.py 唯一料源本体；check-bundle-parity 两仓零实体未建成（两仓 grep 零命中现证沿票面）＝归属随登归后续票；桶闸扩展料源＝仓根 share／ 面（主根窗领办）＝本包只保有随动账。入 run-gates 链与入 share 料源两动作＝他域＝EXT 知会单径（件名＝EXT-2026-11-19-T2e-G7三工具归属定版知会单-v1）；挂载判据 advisory 起步·随放行呈拍附裁（计划行 124 口径沿册）。
tests 接线＝tests 桶入口件 run-all.sh 居 tests／ 桶（ITER-W2-T2e 交付·纯标准库零第三方依赖声明在入口件头注）。

## 正反例（技法面）

- 正例·票体：四字段各自包含完整语义，下游不读他件即可执行；验收标准行全部机械可判（命令＋期望读数）。
- 反例·票体：验收标准写"质量良好／尽量覆盖"＝不可机械判＝技法失败（做坏了），退回重起草。
- 正例·回流：按四型之一如实申报，受阻态直陈阻塞点与所需输入。
- 反例·回流：以"基本完成"混称态＝越出四型闭集，状态机拒绝登记。
