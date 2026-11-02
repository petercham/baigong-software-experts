# SWB-T03 注入构造与派发闸：B3＋B4（注入面＋串行/派发）（施工票·L3·架构席起草）

- 开端读数：ANCHOR＝08fc5ee（见总览件）；开工时实测 HEAD 附回执。
- 设计真源：`.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-02.md`（现行基线＝v2.9 登记生效（PM-R9 `8e63df6`＋QA-R9 `90b7da8`＋主理人登记记录 `ba3fbb6`）；V12 行号前缀（V12 n＝落盘物理 n−27）；产品本体 V12 L1–56 sha256=14605e18…；架构本体 V12 L57–230 sha256=17f4843a…；纯 LF）。
- 背景（自包含）：承接消费面声明第④项「注入面←表2-3」（V12 L211，表体 V12 L99–109）与第⑤项「串行/派发←表2-2/§4」（表体 V12 L84–98，§4 节位 V12 L113–114）。覆盖构件：B3 注入构造＋串行闸、B4 决策包装配（§9 V12 L152–165）。违纪模式表行 4「跳过环节或签字集合缺一即通过→表2-3＋B3 串行闸」、行 15「派发身份不符/注入包超集/串行被破→Agent ID 互验＋B3 白名单＋串行闸」、行 16「审查注入面自选/灰度现场裁量→dispatch-spec 机械定义＋B4 机械门禁」（产品 §4 V12 L26–41）的拦截面主承接在本票。
- 前置票：T02（账本记录类、seat-permissions/ticket-types 同源件）。

## 声明闭集（7 件·本票唯一可写面）
- 声明闭集：
- deliverables/experts/baigong-software-team/skills/sop/scripts/dispatch-builder.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/serial-gate.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/decision-pack.py
- deliverables/experts/baigong-software-team/config/dispatch-spec.json
- deliverables/experts/baigong-software-team/config/ticket-authors.json
- deliverables/experts/baigong-software-team/tests/s3/test_dispatch_gate.py
- deliverables/experts/baigong-software-team/tests/s3/test_decision_pack.py

## 逐条施工规格

### T03-A dispatch-spec.json（审查注入面机械定义·消费面④落点）
- 行集＝表2-3（V12 L99–109）七行逐行转录＝六节点行＋维护行（`维护·节点 1–3｜签字集合＝产品席＋架构席（合签）｜按主表`·V12 L108）：节点号、签字集合（逐项名）、人类角色列；每节点附「审查注入面」数组＝机械列明该节点审查者所见件集（§2 表注 V12 L109：「QA 审计切片显式列明；产品含已登记 intake 只读＋架构触发项命中件草稿态；工程师只见本票＋上游内容副本。审查者看什么由 dispatch-spec 机械定义，不许自选」）；spec 声明面另转录表2-3 轻签点表注（V12 L110 逐字引文：「轻签点＝合法签收形态，不构成产品 §4 违纪行 4（V10 L54）之跳过环节；未达准入判据（§17 维护票词条）而走维护票→转流程变更票重审」）。
- 头部注 `derived_from: 表2-3`；票类清单引用 ticket-types.json 同源（§3 同源校验）。

### T03-B dispatch-builder.py（B3 注入构造·机械展开）
- 输入票 ID → 按 dispatch-spec 机械展开注入包（禁手拼路径）；注入包哈希写账本「注入包哈希」记录类（§3 六类）。
- 白名单超集检测：展开结果 ⊖ spec 声明面 ≠ ∅ → exit≠0（违纪行 15「注入包超集」拦截）。
- Agent ID 互验键双向比对（§8 派发约定 V12 L151：「name 传 Agent ID 禁中文名；互验键双向比对；同源四方」）；不符 → 计差异（口径 §13：分子｛Agent ID 不符∨包哈希不符∨白名单超集｝）。

### T03-C serial-gate.py（B3 串行闸·消费面⑤落点）
- 规则＝§4（V12 L113–114）「执行期全系统一票活跃，新派发被串行闸拒绝」；§9 B3 行「活跃票非零拒绝派发」；表2-2（V12 L92）「票内工作：工程师，一票一新鲜实例，票间串行」。
- 读数源＝账本活跃票计数；活跃≠0 时任何派发请求 exit≠0 且写「呈报」类审计事件。

### T03-D decision-pack.py（B4 决策包装配）
- 机械计算＋异常强制呈报：触发源六闭集｛租约越界 deny／对账差≠0／活性自检失败／引用扫描命中／超期／熔断｝（§4 V12 L114）逐码实现为呈报触发枚举；主理人仅投递（表2-2 V12 L91）；呈报面含缺陷定级字段（§18⑩·V12 L211 次级承接：P0/P1 定级＝QA 双复核＋人类终裁，决策包呈报面呈现定级与定级确认状态）。
- 灰度→全量机械门禁（表2-2 V12 L97「QA 按声明判据机械门禁，不得现场裁量」）：判据读取＝票内声明字段，脚本比对读数，不符拒出 full-rollout 决策包。

### T03-E ticket-authors.json（修票权映射·与 T02 同源）
- 转录表注（V12 L79）六映射：开发票→架构修｜缺陷票→QA 修｜部署票三字段→工程师部署域重写｜生产票目标字段→状态机依放行记录机械派生｜规则票→提案席位｜维护票→架构席修；票类清单∈ticket-types.json 同一集合。

## 验收判据（全部机械可判）
1. `python -c "import json;d=json.load(open('deliverables/experts/baigong-software-team/config/dispatch-spec.json'));assert len(d['nodes'])==7;assert all(len(n['signoffs'])>0 for n in d['nodes'])"` 退出 0（表2-3 七行＝六节点＋维护行，签字集合非空）；
2. 同源断言：`python -c "import json;a=set(x['id'] for x in json.load(open('deliverables/experts/baigong-software-team/config/ticket-types.json'))['types']);b=set(json.load(open('deliverables/experts/baigong-software-team/config/ticket-authors.json'))['authors']);assert a==b"` 退出 0；
3. 串行闸冒烟：账本预置 1 张活跃票后调 dispatch-builder → exit≠0 且账本新增「呈报」记录恰 1 条（读数入回执）；
4. 超集冒烟：样例票注入面超出 spec 声明 → dispatch-builder exit≠0，回显差异集；
5. `python deliverables/experts/baigong-software-team/tests/s3/test_dispatch_gate.py deliverables/experts/baigong-software-team/tests/s3/test_decision_pack.py` 退出 0；
6. 触发源六码枚举齐备：`grep -c 'TRIG_' deliverables/experts/baigong-software-team/skills/sop/scripts/decision-pack.py` ≥6 且六码名与 §4 六项一一对应（回执附 grep 读数对照表）。

## 票间关系
- 前置：T02。后置：T04（B5 拦 force-push 时经账本活跃票口径）、T06（六条演练中「派发-执行-回流」链消费 B3/B4）、T05（席位卡「脚本调用点」行引用本票实体名）。

## 禁动面（零触碰）
- 两基线登记件本体、`.collab/` 全域（回执除外）、`docs/`、T01/T02/T04/T05/T06 声明闭集全部文件。
- 工程师不得改本票票体四字段。

## 候裁点（单列·不自行拍）
- 无新增。派发记录导出形态若涉 P9 读数依赖，属观测项不属闸前提（§10 规则）。

## 回执
落 `.collab/receipts/2026-11-01-SWB-T03-receipt.md`：开端 HEAD＋完整文件清单＋判据 1–6 实测读数。commit 单独笔，`collab:` 前缀只含本票闭集件。
