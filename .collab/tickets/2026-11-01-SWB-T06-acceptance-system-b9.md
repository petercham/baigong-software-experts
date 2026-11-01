# SWB-T06 验收双臂与触发判据（B9 职能承载票）：验收体系＋指标口径＋六条演练（施工票·L3·架构席起草）

- 开端读数：ANCHOR＝08fc5ee（见总览件）；开工时实测 HEAD 附回执。
- 设计真源：`.collab/refs/external/SWB-交接件v2.7-产品设计与架构设计-2026-11-01.md`（现行基线＝v2.7 三方收口·登记 `900d85f`；V10 行号前缀；产品本体 V10 L26–80 sha256=2b3675e1…；架构本体 V10 L81–239 sha256=1a9febe8…；纯 LF）。
- 背景（自包含）：§9 声明「B9＝验收施工票，编号空缺刻意」——本票即 B9 职能的显式并入声明票。承接消费面声明第⑦项「验收双臂←§16＋产品设计§4」（V10 L224；§16 节位 V10 L209–211，产品 §4 节位 V10 L45–67）与第⑨项「触发判据←§13」（V10 L193–199）。验收三段式＝工程师写脚本、CI 机械执行、QA 出结论（表2-2 V10 L114）＝双臂之一；人工等效性抽检（产品 §4 V10 L67：抽≥20% 验收行判定等效性，签字入册）＝双臂之二。违纪模式表承接：行 10「计数/数字声明失实→制度④计数即断言」（count-assert 落点）、行 12「生成方自判合格性→制度③状态申报制」（结论权归 QA 面落点）、行 13「降级态无人承接→§14 承接表具名」（抽样记录面）。
- 前置票：T01–T05 全部（演练链逐条跑通依赖全部机制实体在位；验收对装配面与机制群全量核验）。

## 声明闭集（11 件·本票唯一可写面）
- 声明闭集：
- deliverables/experts/baigong-software-team/tests/acceptance/metrics-gate.py
- deliverables/experts/baigong-software-team/tests/acceptance/count-assert.py
- deliverables/experts/baigong-software-team/tests/acceptance/drill-runner.sh
- deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-01-transcription-routing.sh
- deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-02-dispatch-exec-return.sh
- deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-03-write-side-intercept.sh
- deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-04-decision-pack-escalation.sh
- deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-05-freeze-recover.sh
- deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-06-replay-reconcile.sh
- deliverables/experts/baigong-software-team/config/thresholds.json
- deliverables/experts/baigong-software-team/tests/acceptance/equivalence-sampling-log-template.md

## 逐条施工规格

### T06-A thresholds.json（§13 成值集中登记·消费面⑨落点）
- 逐值转录 §13（V10 L199），每值附 `source` 注：`diff_rate_threshold=0.02`（差异率阈值 2%）；`metric_anomaly_set`＝三闭集｛差异率>2%／活性自检失败／派发互验连续3次不一致｝；`fuse_set`＝｛连续两轮不通过／退回率>0.30｝（标注 C1 可调）；`deny_freeze_max_s=60`（缺省，C1 可调）；`timeouts`＝｛engineer_ticket_h=48／escalation_h=24｝（未配置项＝不适用）；`stable_def_chains=10`（"稳定后"＝连续 10 链抽样零差异）。
- 差异率口径字段化：分子集＝｛agent_id_mismatch／pack_hash_mismatch／whitelist_superset｝，分母＝completed_dispatch_count（§13 逐字）。

### T06-B metrics-gate.py（三指标＋阶段终点机械面）
- 三指标（产品 §4 V10 L46）：①Hooks 拦截数＝deny 事件计数（含活性自检核验联动）；②派发互验差异率＝按 A 节口径计算，超限＝触发指标异常处置（停用手拼强制 B3＋呈报人类，**不与熔断混用**——两判定路径代码分离，混用即红项）；③路由纠正率＝**明示不机械化**：脚本输出 `manual_observation` 标记行，不产自动判定。
- 阶段终点（产品 §4 V10 L47）：α＝7 日＋六条演练全绿→呈拍；β＝2 周指标全绿→呈拍；γ＝4 周无熔断升级→收口；三终点判定读账本读数，输出三态（met/not-met/pending）。
- 熔断判定独立函数：读 fuse_set，命中→输出冻结呈报码（冻结发起权仍＝人类直通触点，表2-2 V10 L119；本脚本只呈报不自触发）。

### T06-C count-assert.py（制度④计数即断言·机检器）
- 模式1 票面闭集解析：定位 `- 声明闭集：` 锚行→计数其后连续 `- <路径>` 裸路径条目行→与票面申报数 N 比对，不符 exit≠0（缺声明＝SKIP 不算绿）。
- 模式2 无裸纪律计数（§7 V10 L157「验收核验'无裸纪律'」）：扫描席位卡纪律行，缺 `G[1-5]` 标注即计入裸纪律，非零 exit≠0。
- 模式3 总览映射表行数比对：映射表行数 vs 实物文件数，两实现交叉验（计数双实现）。

### T06-D 六条演练（§17 词条 V10 L213 六名逐字＋产品 §4 α 终点「六条演练全绿」）
六脚本名对位闭集六名：
- drill-01＝誊录路由：人类输入→B1 登记→路由读数链全绿；
- drill-02＝派发-执行-回流：B3 展开→一票活跃→回流四型之一入账；串行闸对第二派发 exit≠0 亦属全绿条件；
- drill-03＝写侧拦截：无租约写→deny 读数＋呈报码；
- drill-04＝决策包呈拍：触发源六码之一→B4 包→呈拍记录；
- drill-05＝停刀-恢复：freeze→清租约→全写 deny→解冻（人类令牌）→自计时 ≤60s；
- drill-06＝重放对账：B8 重放→差异三分类＋引用扫描结论→日终对账差=0。
- `drill-runner.sh`：依序执行六脚本→全绿 exit 0 输出 `SIX_DRILLS_GREEN`；任一红→exit≠0 并指名红链。

### T06-E equivalence-sampling-log-template.md（人工等效性抽检·双臂之二）
- 模板字段：抽样行清单（≥20% 验收行，附各行所属票号）、判定结论（验收全绿是否等价于条款达成）、签字栏（产品席或 QA 席）、日期；签字入册路径注＝`.collab/human/reviews/`（v2.7 表2-1 人类行；本票只产模板，不产入册动作）。

## 验收判据（全部机械可判）
1. `python -c "import json;t=json.load(open('deliverables/experts/baigong-software-team/config/thresholds.json'));assert t['diff_rate_threshold']==0.02 and t['deny_freeze_max_s']==60 and t['stable_def_chains']==10"` 退出 0；
2. `python deliverables/experts/baigong-software-team/tests/acceptance/metrics-gate.py --selftest` 退出 0，且读数含 `route_correction_rate: manual_observation` 行（grep 命中）；
3. 混用隔离断言：metrics-gate 自测样区内差异率超限样本 → 输出「指标异常」路径读数且**无**熔断码；熔断样区 → 输出熔断呈报码且无手拼禁用码（两读数互斥，回执附对照）；
4. `bash deliverables/experts/baigong-software-team/tests/acceptance/drill-runner.sh` 退出 0 且输出 `SIX_DRILLS_GREEN`；
5. `ls deliverables/experts/baigong-software-team/tests/acceptance/drills/*.sh | wc -l` ＝6；
6. count-assert 自咬：`python deliverables/experts/baigong-software-team/tests/acceptance/count-assert.py --mode1 .collab/tickets/2026-11-01-SWB-T06-acceptance-system-b9.md` 对本票跑模式1（锚行解析）→ 申报 11＝实数 11，exit 0（读数入回执）；
7. 差异率分子三分量各一构造样例 → metrics-gate 计数各 +1（三分量读数）。

## 票间关系
- 前置：T01、T02、T03、T04、T05（演练链消费全部机制实体）。后置：无（终票；呈拍后由人类决策者按产品 §4 阶段终点推进 α）。

## 禁动面（零触碰）
- 两基线登记件本体、`.collab/` 全域（回执除外）、`docs/`、T01–T05 全部声明闭集文件（演练只调用不改动被测实体；被测实体缺陷→开缺陷票走 QA 面，不得在本票内修他票文件）。
- 工程师不得改本票票体四字段；本票不得自判合格（制度③）——验收结论权＝QA/CI 面。

## 候裁点（单列·不自行拍）
- 无新增。路由纠正率明示不机械化（设计原样，不留机械闸）；CI 不可用时本票验收走降级＝本地脚本执行＋QA 复核结论（§11 CI 行/产品 §5 行6），降级启用属运营态决定，呈人类知悉。

## 回执
落 `.collab/receipts/2026-11-01-SWB-T06-receipt.md`：开端 HEAD＋完整文件清单＋判据 1–7 实测读数。commit 单独笔，`collab:` 前缀只含本票闭集件。
