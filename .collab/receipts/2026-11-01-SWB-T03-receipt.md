# SWB-T03 回执 · 注入构造与派发闸（B3＋B4）· engineer-t03

- 票面：`.collab/tickets/2026-11-01-SWB-T03-injection-dispatch-gate.md`（59 行·V13 锚现行态）
- 开工 HEAD 实测读数：`git rev-parse HEAD` = `3a0c06226331afce949c940fb675e92c6ae1a742`（＝放行读数 3a0c062，一致）
- 完工 HEAD：见本回执随同一笔 commit（`collab:` 前缀·name-only＝下述 8 件＝声明闭集 7 件＋本回执）

## 完整写入/修改文件清单（与 commit name-only 全等·8 件）
1. deliverables/experts/baigong-software-team/skills/sop/scripts/dispatch-builder.py（新建）
2. deliverables/experts/baigong-software-team/skills/sop/scripts/serial-gate.py（新建）
3. deliverables/experts/baigong-software-team/skills/sop/scripts/decision-pack.py（新建）
4. deliverables/experts/baigong-software-team/config/dispatch-spec.json（新建）
5. deliverables/experts/baigong-software-team/config/ticket-authors.json（新建）
6. deliverables/experts/baigong-software-team/tests/s3/test_dispatch_gate.py（新建）
7. deliverables/experts/baigong-software-team/tests/s3/test_decision_pack.py（新建）
8. .collab/receipts/2026-11-01-SWB-T03-receipt.md（本回执）

禁动面自查：T01/T02 闭集全部文件、两基线登记件、`.collab/` 全域（回执除外）、`docs/` 零触碰；工作区两条 TKT 旧 untracked 件未动未提交；仓内无脚本运行残留（全部运行验证经 `--ledger/--states/--agents/--out` 重定向 Temp）。

## 验收判据 1–6 实测读数（全部实跑取数）

### 判据1 — PASS
命令（票面逐字）：`python -c "import json;d=json.load(open('deliverables/experts/baigong-software-team/config/dispatch-spec.json'));assert len(d['nodes'])==7;assert all(len(n['signoffs'])>0 for n in d['nodes'])"`
读数：**退出 0**。行集＝表2-3 七行逐行转录（六节点行＋维护行 `维护·节点1-3｜签字集合＝产品席＋架构席（合签）｜按主表`）；每节点附审查注入面数组（机械列明各席位所见件集，按 V13 L109 表注三分句装填）；轻签点表注 V13 L110 逐字转录于 `table_notes`；头部注 `derived_from: 表2-3`；票类清单引用 ticket-types.json 同源。

### 判据2 — 字面呈核＋语义 PASS
- 票面字面命令实跑：**退出 1**（`TypeError: string indices must be integers`）。先天不可满足成因：命令假定 `ticket-types.json['types']` 为含 `id` 键对象数组，而前置票 T02 已收口交付面现行态为**字符串数组**（`["产品需求","开发",…]`，T02 闭集禁动不可改形）。按硬纪律5 不改票面、不触 T02 件，字面判据呈核。
- 语义判据（同源集合相等断言，票面意图＝authors 键集∈ticket-types 同一集合）实跑：**退出 0**，两侧集合全等＝｛产品需求、开发、缺陷、部署、规则、流程变更、验收、维护｝八类。
- 归位注记（呈核不新增候裁）：表注六映射（V13 L79）直列覆盖票型八类中五类＋维护；其余三类（产品需求/流程变更/验收）按票型语义归位（产品需求→产品席提案；流程变更→提案席位·规则票同类；验收→QA席·表2-2 三段式出结论席），归位注记随件内 `same_origin_closure_note` 与 `table_six_mappings_verbatim` 附源。

### 判据3 — PASS
账本预置 1 张活跃票（states.json 预置 `{"SWB-T99":{"state":4,…}}`）后调 dispatch-builder（CLI 实跑·Temp 重定向）：
- 读数：`exit=2`（≠0），stderr 回显 `REJECT serial-gate ticket=SWB-J3: 活跃票=1 非零，新派发被串行闸拒绝（呈报记录 hash=628de9e5…）`
- 账本「呈报」新增恰 1 条：`grep -o '"type": "呈报"' ledger.jsonl | wc -l` = **1**
- 同形态入测试件 t02（test_dispatch_gate.py）常跑。

### 判据4 — PASS
样例票请求注入面含 spec 声明面外条目（`他票票体副本`）调 dispatch-builder（Temp 重定向）：
- 读数：`exit=3`（≠0），回显差异集 `差异集=['他票票体副本']`；差异条目同时入账本呈报记录 `superset_items` 字段。
- 同形态入测试件 t04 常跑。

### 判据5 — PASS
命令（票面逐字）：`python deliverables/experts/baigong-software-team/tests/s3/test_dispatch_gate.py deliverables/experts/baigong-software-team/tests/s3/test_decision_pack.py`
读数：**退出 0**；PASS 计数＝14（test_dispatch_gate 7 项＋test_decision_pack 7 项，兄弟件经 argv 机械执行）。

### 判据6 — PASS（附 grep 读数对照表）
命令：`grep -c 'TRIG_' deliverables/experts/baigong-software-team/skills/sop/scripts/decision-pack.py`
读数：**8 ≥ 6**；occurrence 口径 `grep -o 'TRIG_' … | wc -l` = **12**。

六码名与 §4（V13 L115）六项一一对应对照表：

| §4 六闭集项 | 码名（decision-pack.py L40–45） |
|---|---|
| 租约越界 deny | `TRIG_LEASE_DENY = "租约越界deny"` |
| 对账差≠0 | `TRIG_RECONCILE_DIFF = "对账差≠0"` |
| 活性自检失败 | `TRIG_LIVENESS_FAIL = "活性自检失败"` |
| 引用扫描命中 | `TRIG_REF_SCAN_HIT = "引用扫描命中"` |
| 超期 | `TRIG_OVERDUE = "超期"` |
| 熔断 | `TRIG_CIRCUIT_BREAK = "熔断"` |

六码逐码呈报可出包实跑证据＝test_decision_pack t01（逐码 exit0＋入账恰一·六条）。

## occurrence 口径声明
本回执全部计数读数以 `grep -o '<pat>' <file> | wc -l` 为唯一口径（与 `grep -c` 行计数口径并列处已分列注明：判据6 `grep -c`=8 为票面指定口径，occurrence=12 为声明口径）。

## 候裁点处置
票面候裁节＝「无新增」，本票未自设候裁。派发记录导出形态未引 P9 读数作闸前提（§10 规则遵行：导出形态属观测项）。

## 异常路由项
- 判据2 字面命令先天不可满足（成因与处置见上·呈核项，非闸异常）。
- 仓闸对既有旧账（OA-D6 系）打印随路由表走②不拦，未触发绕闸需求；落笔前 name-only 复检通过。
