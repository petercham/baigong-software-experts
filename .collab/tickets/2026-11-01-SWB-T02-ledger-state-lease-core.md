# SWB-T02 账本与状态核心：B0＋B1＋B2（含租约段实例化）（施工票·L3·架构席起草）

- 开端读数：ANCHOR＝08fc5ee（见总览件）；开工时实测 HEAD 附回执。
- 设计真源：`.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-02.md`（现行基线＝v2.9 登记生效（PM-R9 `8e63df6`＋QA-R9 `90b7da8`＋主理人登记记录 `ba3fbb6`）；V12 行号前缀（V12 n＝落盘物理 n−27）；产品本体 V12 L1–56 sha256=14605e18…；架构本体 V12 L57–230 sha256=17f4843a…；纯 LF）。
- 背景（自包含）：承接消费面声明第①项「租约段实例化←表2-1」（V12 L211）与第⑩项「缺陷定级←表2-2（P0/P1＝QA 双复核＋人类终裁）」（V12 L211·落点＝T02-C）。覆盖构件：B0 账本、B1 誊录登记、B2 状态机＋租约签发（§9 V12 L152–165）。时序：基线已生效，B0 开工合规（§18 基线化时序 V12 L213）；§18 补登条款（V12 L212）令「B0 施工票验收含'补登演示'并互引本条款」——落为本票验收判据 A6。租约＝{票ID·路径集·席位ID·哈希}（§17）；租约段经架构签注由 B2 从表2-1（V12 L70）实例化。账本六类记录＝派发/写入/签字/注入包哈希/intake 登记/呈报（§3）。
- 前置票：T01（P7 读数决定 B0 主路/退路形态；§9 B0 行「P7 阴性→本地裸仓＋PreToolUse 拦 force-push/amend＋异地镜像＋日终对账」）。P7 阴性时按候裁 Q-02 呈人类拍板后择路，不自行定。

## 声明闭集（11 件·本票唯一可写面）
- 声明闭集：
- deliverables/experts/baigong-software-team/skills/sop/scripts/ledger-init.sh
- deliverables/experts/baigong-software-team/skills/sop/scripts/intake-register.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/state-transition.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/lease-issuer.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/reconcile-daily.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/baseline-backfill-demo.py
- deliverables/experts/baigong-software-team/skills/sop/scripts/promote-manifest.py
- deliverables/experts/baigong-software-team/config/seat-permissions.json
- deliverables/experts/baigong-software-team/config/ticket-types.json
- deliverables/experts/baigong-software-team/tests/s2/test_ledger_core.py
- deliverables/experts/baigong-software-team/tests/s2/test_lease_instantiation.py

## 逐条施工规格

### T02-A ledger-init.sh（B0 主路/退路双形）
- 主路（P7 pass）：独立 git 服务初始化＝远端裸仓＋拒非快进（`receive.denyNonFastForwards=true`）＋拒强制推送（`receive.denyDeletes=true`）＋保护分支配置；退路（P7 negative）：本地裸仓＋输出「三重保证待 T04 hooks 与异地镜像＋日终对账补位」声明行（PreToolUse 拦截实体在 T04，本脚本只留配置锚）。
- 主信任锚＝git 原生哈希链（§3/§17）；记录级前向哈希字段 `prev_hash` 仅供单记录独立校验。

### T02-B intake-register.py（B1）
- 输入：人类输入原文件路径；输出：intake 登记记录（六类记录之「intake 登记」）入账＋登记号回显。
- 闭集六类誊录类型（表2-2「人类输入誊录与路由…B1 六类闭集，不做业务解析」）；脚本零裁量：不做任何业务解析，只登记与编号。

### T02-C state-transition.py（B2 状态迁移/登记/记账）
- 状态集＝节点 1 需求→2 设计→3 拆票→4 执行→5 发布→6 灰度（§4）＋挂起态（§17）；迁移合法性表硬编码，非法迁移 exit≠0。
- 每次迁移写「派发/签字/呈报」对应记录类；签字集合按表2-3（V12 L99）六节点签字行校验，缺一拒迁并写「呈报」类审计事件（触发源六闭集见 §4/§13）。
- 定级确认前置签收（§18⑩·V12 L211 随动）：迁移合法性表增「定级确认」前置签收字段——P0／P1 级缺陷相关迁移动作（进入/离开 4 执行 的缺陷票链迁移）在定级未确认时 exit≠0；定级权限归 QA 双复核＋人类终裁（表2-2 缺陷定级行·V12 L95），本脚本只校验签收字段在位、不判级。
- timeouts 缺省读取：工程师票 48h／呈报 24h（§13），未配置项＝不适用。

### T02-D lease-issuer.py（B2 租约签发·消费面①落点）
- 实例化源＝`config/seat-permissions.json` 逐席位行，行集＝表2-1（v2.9 版·V12 L70–79）六席位行逐行转录：写域/可写内容/**明确不可写**三列＋载体列标注——按 v2.9 表注三条款转录即得，不自行归置：路径锚定（裸路径一律读作仓根字面·V12 L80）／判据真源双层双址（仓根 `tests/`＝判据真源域·架构/QA 共写经 C1，交付树内 `deliverables/**/tests/**`＝施工与验收测试实体·工程师经租约·V12 L81）／枚举款六类（顶层只余六类含 `tests/`·V12 L82）；工程师行「明确不可写」列含 `仓根 tests/（跨发布验收判据真源·架构/QA 共写域）` 随 v2.9 表2-1 转录；`tests/` 归属读法按 v2.9 双层双址条款落：仓根 `tests/`＝判据真源域（架构/QA 共写、经 C1）、交付树内 `deliverables/**/tests/**`＝施工与验收测试实体（工程师经租约）；若裁定另有口径以裁定为准回改本目；「明确不可写」列另出 `deny_globs` 数组供 T04 B5 消费（消费面②的数据源在本票埋设，校验实体在 T04）。
- 签发输出＝`{ticket_id, path_globs, seat_id, hash}` 四字段 JSON 入账（§9 B2 行/§17 租约词条）；架构签注字段 `countersign` 必填（§7 架构纪律「租约签注唯一生产权」）。
- `config/seat-permissions.json` 头部注 `derived_from: 表2-1`；`config/ticket-types.json`＝票型八类闭集（产品需求/开发/缺陷/部署/规则/流程变更/验收/维护，§3·V12 L112）＋修票权映射（表注「修票权＝票类作者权」六映射·V12 L79：开发票→架构修｜缺陷票→QA 修｜部署票三字段→工程师部署域重写｜生产票目标字段→状态机依放行记录机械派生｜规则票→提案席位｜维护票→架构席修）。同源声明：本两文件与 T03 dispatch-spec、T05 ticket-authors 同一票类清单派生（§3），同源校验断言在 T03 验收。

### T02-E reconcile-daily.py（日终对账）
- 对账对象＝账本六类记录 vs git 提交/租约台账交叉核；差≠0 → 写「呈报」类审计事件（触发源「对账差≠0」）。

### T02-F baseline-backfill-demo.py（补登演示·§18 互引条款）
- 演示动作＝向账本追加两条基线条目：产品设计 v2.9（sha256=14605e18…，行数 56＝V12 L1–56 段实测）＋架构设计 v2.9（sha256=17f4843a…，行数 174＝V12 L57–230 段实测）；哈希引用落盘哈希非转录；append-only（只追加不回改）。
- 脚本头注互引：`clause: 架构v2.9 §18 补登条款（V12 L212）`。

### T02-G promote-manifest.py（转正代写·表2-1 主理人行/表注 V12 L79 落点）
- 实现表注定义：状态机脚本将验证通过的草稿按 `manifest` 清单文件声明复制入 `docs/` 并附来源哈希——唯一合法写入形态；代写主体＝本脚本（非任何 LLM 席位）。
- manifest 文件由账本域保管（表2-1 主理人可写域）；脚本校验草稿哈希＝manifest 声明哈希后方复制，不符 exit≠0。

## 验收判据（全部机械可判）
1. `bash deliverables/experts/baigong-software-team/skills/sop/scripts/ledger-init.sh && echo INIT_OK` 输出含 `INIT_OK` 且非快进/保护分支配置读数回显；
2. `python -c "import json;d=json.load(open('deliverables/experts/baigong-software-team/config/seat-permissions.json'));assert len(d['seats'])==6"` 退出 0（六席位行＝表2-1 行数）；
3. `python -c "import json;t=json.load(open('deliverables/experts/baigong-software-team/config/ticket-types.json'));assert len(t['types'])==8"` 退出 0（票型八类）；
4. lease-issuer 冒烟：签一张样例租约，`python` 断言输出四键恰为 `ticket_id,path_globs,seat_id,hash`；重复签发未签注件 exit≠0；
5. `python deliverables/experts/baigong-software-team/tests/s2/test_ledger_core.py deliverables/experts/baigong-software-team/tests/s2/test_lease_instantiation.py` 退出 0（工程师写脚本、CI 机械执行、QA 出结论——三段式，本票回执只附执行读数）；
6. `python deliverables/experts/baigong-software-team/skills/sop/scripts/baseline-backfill-demo.py` 退出 0，账本中两基线条目哈希与 v2.9 登记段实测值（14605e18…／17f4843a…）逐字等（回执附两读数）；
7. 非法迁移冒烟：state-transition 对「4 执行→1 需求」请求 exit≠0 且产生「呈报」类记录一条（读数入回执）；
7a. 定级签收冒烟（§18⑩随动）：state-transition 对定级未确认的 P0/P1 缺陷票链迁移（进入 4 执行）请求 exit≠0 且写「呈报」类记录一条（读数入回执）；
8. promote-manifest 冒烟：样例草稿哈希与 manifest 声明一致→复制入 `docs/` 成功并附来源哈希读数；篡改样例→exit≠0 且 `docs/` 无新增（两读数）。

## 票间关系
- 前置：T01（P7）。后置：T03（消费账本记录类＋seat-permissions 同源）、T04（消费 `deny_globs`＋租约台账）、T05（席位卡脚本调用清单引用本票实体名）。

## 禁动面（零触碰）
- 两基线登记件本体、`.collab/` 全域（回执除外）、`docs/`、`deliverables/experts/baigong-software-team/` 下非本票闭集路径、T01/T03/T04/T05 声明闭集全部文件。
- 工程师不得改本票票体四字段；账本历史 append-only 不回改。

## 候裁点（单列·不自行拍）
- Q-02：P7 读数阴性时 B0 退路三重保证的异地镜像承载方与凭证保管细节（§11 已定承载者＝人类侧，配置细节呈人类）。
- Q-07：**已裁**＝选项 A：采纳 v2.8 表2-1 表注三条款为正式口径（路径锚定 V12 L80／判据真源双层双址 V12 L81／枚举款六类 V12 L82·**测试实体跟随项目**；皮总 2026-11-02 ㊼·出处＝`.collab/decisions/2026-11-02-皮总拍板.md`）；裁定后读法以 T02-D 现行双层双址条款为准。

## 回执
落 `.collab/receipts/2026-11-01-SWB-T02-receipt.md`：开端 HEAD＋完整文件清单（与 commit name-only 全等）＋判据 1–8 全部实测读数。commit 单独笔，`collab:` 前缀只含本票闭集件。
