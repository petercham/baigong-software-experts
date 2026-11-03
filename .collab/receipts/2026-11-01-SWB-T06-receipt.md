# SWB-T06 回执（验收双臂与触发判据 B9 职能承载票·交付笔 9a3013c）

- 票面＝`agent-experts/baigong-software-team/.scratch/tickets/2026-11-01-SWB-T06-acceptance-system-b9.md`；执行席＝工程师席（交付面唯一写权席位）。
- 计数口径声明：本回执全部计数＝occurrence 口径（`grep -o … | wc -l` 或逐项计数），非 `grep -c` 行数口径。
- 本回执＝过程记录居治理域（P-Ⅲ）；交付件正文纯度自适（本件不收留交付件正文）。

## 一、开端读数

- 开工实测 HEAD＝`0beb004`（`git log --oneline -1`＝`0beb004 collab: README 随批——T05 转已收口…`），与票面 ANCHOR 之后前置收口态相符，如实登记。
- 开工时工作树脏项＝`.collab/qa/` 两件 untracked（非本票产物·零触碰留存）。

## 二、交付笔与文件清单（commit name-only 对账口径）

- 交付笔＝`9a3013c`（message 前缀 `SWB-T06:`；未用 `--no-verify`、未 amend）。
- `git show --name-only --pretty=format: 9a3013c`（去空行）计数＝**11**，与声明闭集逐一对位：
  1. deliverables/experts/baigong-software-team/tests/acceptance/metrics-gate.py
  2. deliverables/experts/baigong-software-team/tests/acceptance/count-assert.py
  3. deliverables/experts/baigong-software-team/tests/acceptance/drill-runner.sh
  4. deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-01-transcription-routing.sh
  5. deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-02-dispatch-exec-return.sh
  6. deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-03-write-side-intercept.sh
  7. deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-04-decision-pack-escalation.sh
  8. deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-05-freeze-recover.sh
  9. deliverables/experts/baigong-software-team/tests/acceptance/drills/drill-06-replay-reconcile.sh
  10. deliverables/experts/baigong-software-team/config/thresholds.json
  11. deliverables/experts/baigong-software-team/tests/acceptance/equivalence-sampling-log-template.md
- 门禁实录：首两笔落笔被 pre-commit 门禁（object-audit OA-T1 项目实体·drive-path BLOCK）拦下两次
  （拦点＝本票件内盘符字面 `D:/t06-tmp` 与一处正则字面误读为盘符）；均为闭集内合规修正
  （Temp 缺省改调用方注入 `T06_TMP:?`／正则改写法不落 drive-path 形态）后复检重落笔，第三次通过。
- 禁动面自证：`git status --short` 交付前后差异仅上述 11 件＋本回执；`.collab/` 其余、`docs/`、
  T01–T05 闭集文件零触碰；演练运行残留零入仓（全部落仓外 Temp＝`T06_TMP` 注入路径）。

## 三、验收判据 1–7 逐条实测读数

1. **thresholds 断言**：`python -c "import json;t=json.load(open('…/config/thresholds.json'));assert t['diff_rate_threshold']==0.02 and t['deny_freeze_max_s']==60 and t['stable_def_chains']==10"` → **exit 0**。
2. **metrics-gate 自测**：`metrics-gate.py --selftest` → **exit 0**；`route_correction_rate: manual_observation` 行 grep 命中＝**1**（occurrence 口径）。
3. **混用隔离对照**（自测样区读数对照）：
   - 样区 A（差异率超限 0.30>0.02）→ 输出 `code=METRIC_ANOMALY … 停用手拼强制 B3＋呈报人类`；该读数内熔断码（`FUSE_FREEZE_REPORT`/冻结呈报）grep 命中＝**0**；
   - 样区 B（rounds_fail=2）→ 输出 `code=FUSE_FREEZE_REPORT … 只呈报不自触发`；该读数内手拼禁用码（`METRIC_ANOMALY`/停用手拼）grep 命中＝**0**；
   - 自测行输出 `MIX_ISOLATION_OK: 两判定路径代码分离·两读数互斥`。两判定路径＝两独立函数（judge_metric_anomaly / judge_fuse）。
4. **drill-runner**：`bash …/tests/acceptance/drill-runner.sh`（T06_TMP 注入仓外 Temp）→ **exit 0** 且输出 **SIX_DRILLS_GREEN**（读数见第四节）。
5. **演练脚本数**：`ls …/tests/acceptance/drills/*.sh | wc -l` ＝ **6**。
6. **count-assert 自咬**：`count-assert.py --mode1 agent-experts/baigong-software-team/.scratch/tickets/2026-11-01-SWB-T06-acceptance-system-b9.md --expect 11` → `申报=11 实数(实现A)=11 交叉(实现B)=11 cross_ok=True` → **exit 0**（本票申报 11＝实数 11）。
7. **差异率分子三分量构造样例**：`--construct-sample` 逐分量对仓外 Temp 账本各构造一样例，三行读数各 `count_before=0 count_after=1 delta=+1`；汇总计数行 `metric2_diff_rate: numerator=3 by_component={'agent_id_mismatch': 1, 'whitelist_superset': 1, 'pack_hash_mismatch': 1}`（三分量各 +1）。

补充实测（票面施工规格内非判据项）：count-assert 模式2 对五席位卡裸纪律计数＝**0**（纪律行 3/8/8/8/9）exit 0；模式3 对总览四映射表行数 10/12/16/7 全 OK、六票实物计数 13/11/7/10/13/11 全 OK、闭集总件数 65＝65 OK（两实现交叉验），exit 0——即总览 §七 申报「交叉验第二实现」由本票闭合。

## 四、六条演练逐条实测读数（真调用机制实体·exit 码/日志行/账本行）

- **drill-01 誊录路由** GREEN：intake-register 登记读数 `REGISTERED reg_no=INTK-0001 class=指令 sha256=965a33…`；负例（誊录类越六闭集）exit≠0 拒收在位；账本回读「intake 登记」恰 1＋四字段/哈希链在位。
- **drill-02 派发-执行-回流** GREEN：dispatch-builder `OK dispatch … package_hash=a77030…`；一票活跃 `OK established ticket=DRILL02 state=1`；串行闸对第二派发 **exit≠0**（`REJECT serial-gate … 活跃票=1`＋呈报 hash=5f8f7b…，全绿条件之一）；回流完成型经 4→5 迁移入账（record_type=签字 ledger_hash=38322a…）；账本回读哈希链连续、派发=1/串行拒≥1/回流签字≥1。
- **drill-03 写侧拦截** GREEN：签核环节 sign-verify 正常调用，密钥缺位按 fail-closed 形态如实呈现 **exit=1**（verify_fail 入「签字」记录，不造假通过——签名验核体系保留现行态）；无租约写→write-guard deny 读数（permissionDecision=deny）；账本 write_deny=1＋呈报码「租约越界deny」=1。
- **drill-04 决策包呈拍** GREEN：触发码越六闭集负例 exit≠0；「引用扫描命中」→B4 包 `OK report-pack … pack_hash=a6151b…` 落盘＋呈拍记录 `decision_pack_report=1` 入账；灰度门禁无声明判据负例 exit≠0 在位。
- **drill-05 停刀-恢复** GREEN：预置租约经 lease-issuer 正常签发（lease hash=959a7a…）；冻结前租约内写放行；freeze 三步链全 ok＋自计时 `elapsed=0.004s ≤60s OK`；leases cleared 行在册；原租约内写转 deny（B10 联动）；无令牌解冻拒（fail-closed）→人类令牌解冻 `OK unfreeze`＋deny_all_writes=False 复位。
- **drill-06 重放对账** GREEN：shadow-replay 正扫面 exit 0，三分类读数 `missing_in_replay=0 missing_in_ledger=726 mismatch=0`（missing_in_ledger＝仓 git 链全量提交对 Temp 空账本＝预期形态，重放参照面＝真仓）；引用扫描结论＝词族/引用命中各 0；负扫面词族命中=1 过程件引用命中=1 exit≠0；日终对账（干净租约台账面）**diff=0**。

P4/P5 前置消解口径：本票演练链未遇引用 P4/P5 作闸前提处（写侧演练走 stdin 主路缺省形态＋Q-04 甲案硬拦现行态）；按裁定消解口径（写入串行发生·主理人不受看门狗管辖）执行，无 P4/P5 依赖判定。

## 五、呈核项（单列·本票未修他票文件）

1. **reconcile-daily.py:95 KeyError 差口（已知·实测复现）**：drill-06 附设探针＝对含 freeze cleared 行（无 `lease` 键）的租约台账跑日终对账 → **exit=1，尾行 `KeyError: 'lease'`**（探针读数文件居仓外 Temp）。停刀→对账链走真仓账本时必触发。按裁定不修他票文件，候主理人 YAGNI 微票处置。
2. **回流四型标签未机械化**：完成/部分完成/受阻/异常之「型」字段在全部机制实体落盘面未见机械化承载（grep 全 scripts 零命中「回流」）；现载体＝B2 迁移记录（G2 事后检出）。开缺陷呈核候裁。
3. **engineer 席位租约实例化非机械行**：seat-permissions.json engineer 写域首行「（工作空间根∪部署路径）−受保护区」＝非机械描述行，lease-issuer 零裁量子集校验无法对 `deliverables/**` 类请求实例化（drill-05 首跑实测 `REJECT: 请求路径 … 越出席位 engineer 写域行`，遂演练改走 product 席机械写域行完成）。写域行机械化属表2-1 数据面口径，候裁/规则票处置。
4. **CI 臂降级注记**：本票判据实测＝本地脚本执行形态（§11 CI 行/产品 §5 行6 降级路径）；降级启用属运营态决定，呈人类知悉。
5. **B7 演练链签核环节形态**：密钥根人类离线自持（§11），演练面构造签名样例在无密钥环下 fail-closed exit=1 如实呈现——若需演练链「验签通过」正例，需人类侧托管动作注入密钥（托管＝只保管不审批）。

## 六、候裁段

票面候裁段＝无新增；本回执无夹带新候裁（呈核项 1–3 为被测实体缺陷呈核，非候裁点）。

## 七、结论权声明（制度③）

本回执＝生成方交付申报＋证据读数索引；验收结论权归 QA/CI 面，本票不自判合格。
