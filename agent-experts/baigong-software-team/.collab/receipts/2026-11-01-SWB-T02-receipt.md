# SWB-T02 账本与状态核心（B0＋B1＋B2 含租约段实例化）回执（工程师席 Kou Douma）

- 票面：`agent-experts/baigong-software-team/.scratch/tickets/2026-11-01-SWB-T02-ledger-state-lease-core.md`（77 行·V13 换锚后现行态）
- 开工时实测 HEAD：`14c9c6b023347eb588c24522723ed15a07239906`（`git rev-parse HEAD` 读数·落笔前无新笔即此值）。
- 前置读数：T01 探针 P7（git 独立服务可建性）＝**pass**（`deliverables/experts/baigong-software-team/tests/probes/results/probe-results.json` P7 行实读）→ 按票面 T02-A 主路形态施工；退路形态实现为 ledger-init.sh 的 negative 分支（默认取数走主路）。P7=pass ⇒ 候裁 Q-02 未触发、未拍任何候裁点。
- 设计真源核验（开工前置）：登记件 `.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md` 纯 LF·split 口径 260 行；产品本体段（物理 L29–84＝V13 L1–56·56 行）sha256 实算＝`7214ad14259b175fd6912806e2b3a7bb3655ff35053098f9ed5df66c2d9691f3` 命中票面声称值；架构本体段（物理 L85–260＝V13 L57–232·176 行）sha256 实算＝`efb4f7658c1e5555fcf310cdf4ae91ecbf6ce5cfe19c420c293e0e62cc1078c4` 命中。表2-1 六席位行（物理 L99–106＝V13 L71–78 区）与表注三条款（V13 L80–82＝物理 L108–110）直读转录。

## 完整文件清单（与 commit name-only 全等·12 件＝声明闭集 11 件＋本回执）
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
- .collab/receipts/2026-11-01-SWB-T02-receipt.md

## 验收判据 1–8 逐条实测读数（计数一律 occurrence 口径 `grep -o … | wc -l`）

**运行面声明**：票面禁动面含 `.collab/` 全域（回执除外），而 B0 缺省账本根＝仓根 `.collab/ledger/`（§9 B0 行）。为不触碰禁动面，全部冒烟/验收对账本写入经脚本环境变量 `SWB_LEDGER_ROOT` 重定向至系统 Temp（`/tmp/swb-t02-*`），仓根 `.collab/ledger/` 零写入；脚本缺省行为仍为仓根账本（交付形态不变）。

1. **ledger-init 主路**：`bash deliverables/.../scripts/ledger-init.sh && echo INIT_OK` → 退出 0、输出含 `INIT_OK`；配置读数回显：`B0_FORM=main`／`B0_P7_STATUS=pass`／`receive.denyNonFastForwards=true`／`receive.denyDeletes=true`／`protected_branch_hook=installed`（裸仓 pre-receive 保护分支拒删钩子）。**PASS**
2. `python -c "import json;d=json.load(open('deliverables/experts/baigong-software-team/config/seat-permissions.json'));assert len(d['seats'])==6"` → 退出 0（六席位行＝表2-1 行数·逐行转录含写域/可写内容/明确不可写/载体四列＋表注三条款）。**PASS**
3. `python -c "import json;t=json.load(open('deliverables/experts/baigong-software-team/config/ticket-types.json'));assert len(t['types'])==8"` → 退出 0（票型八类＋修票权六映射＋同源声明）。**PASS**
4. **lease-issuer 冒烟**：样例签发 `--ticket TKT-SAMPLE3 --seat engineer --countersign "architect:sig-T02-smoke3"` → 退出 0；python 断言四键：`A4_KEYS_EXACT: ['hash','path_globs','seat_id','ticket_id']`（断言＝sorted(keys)==sorted(四键)·退出 0）；重复签发未签注件 `--ticket TKT-NOSIGN`（无 countersign）→ 退出 **2**（≠0）。另测非架构席签注（`qa:sig`）→ 拒（§7 唯一生产权）。**PASS**
5. `python deliverables/.../tests/s2/test_ledger_core.py deliverables/.../tests/s2/test_lease_instantiation.py` → 退出 **0**；读数：test_ledger_core 8 项 PASS＋test_lease_instantiation 7 项 PASS（15 项全绿；三段式＝工程师写脚本、CI 机械执行、QA 出结论——本回执只附执行读数）。**PASS**
6. `python deliverables/.../scripts/baseline-backfill-demo.py` → 退出 0；两基线条目读数（账本 JSONL grep -o occurrence 计数各＝**1**）：
   - 产品设计 v2.9：`"sha256": "7214ad14259b175fd6912806e2b3a7bb3655ff35053098f9ed5df66c2d9691f3"`（56 行·落盘哈希实算非转录）＝v2.9 登记段实测值逐字等 ✓
   - 架构设计 v2.9：`"sha256": "efb4f7658c1e5555fcf310cdf4ae91ecbf6ce5cfe19c420c293e0e62cc1078c4"`（176 行·同）逐字等 ✓
   - 脚本头注互引 `clause: 架构v2.9 §18 补登条款（V13 L214）` 在位；append-only 只追加。**PASS（A6 补登演示义务履行）**
7. **非法迁移冒烟**：票 TKT-A7 推进至节点 4 后请求 `--from 4 --to 1` → 退出 **2**（≠0）；stderr＝`REJECT ticket=TKT-A7 4→1: 迁移 4→1 不在合法性表（前进链单向）`；「呈报」类记录 occurrence 计数（`grep -o '"type": "呈报".*"ticket_id": "TKT-A7", "from": 4, "to": 1' | wc -l`）＝**1**。**PASS**
7a. **定级签收冒烟（§18⑩随动）**：缺陷票 BUG-A7a 推进至节点 3，请求进入 4 执行 `--ticket-type 缺陷 --severity P0`（定级未确认）→ 退出 **2**（≠0）；stderr＝`REJECT ticket=BUG-A7a 3→4: 定级确认前置签收缺席：P0 级缺陷票链迁移 3→4 候「定级确认」签收（定级权＝QA双复核＋人类终裁，本脚本不判级）`；「呈报」类记录 occurrence 计数＝**1**；签收字段在位（`--severity-confirmed`＋表2-3 节点 3 签字集）后同迁移放行（测试 t05 绿）。**PASS**
8. **promote-manifest 冒烟**（docs 根经 `--docs-root` 重定向至 Temp 冒烟面，仓根 `docs/` 禁动零触碰）：
   - 读数一（哈希一致）：manifest 声明哈希 `f19971abcd66…89fb2c`＝草稿实算 → 退出 0、输出 `PROMOTED … dest=…\docs\sample-final.md`，冒烟 docs 目录新增 `sample-final.md`（来源哈希随回显附出）。
   - 读数二（篡改）：追加篡改后重跑同一 manifest → 退出 **2**（≠0）；stderr＝`REJECT: 草稿哈希不符 manifest 声明 … actual=113fc9bb… declared=f19971ab…`；docs 目录清单前后无新增（`ls` 前后读数同）。**PASS**

## 施工要点与假设（单列）
- 六类誊录类型闭集取数＝施工包 SWB-CP-v1.1 B1 行「路由六类闭集判定表（产品需求/审查审计/规则意见/SOP变更/询问/指令）」（`.collab/refs/external/` 在盘旧真源·v2.9 表2-2 只声明「六类闭集」未重出枚举）；闭集外类型拒登（测试 t02 绿）；脚本零裁量、不做业务解析。
- 状态机：挂起态迁移仅 `--human-direct` 可触发（脚本不得自触发·§9 B2）；紧急停票写「呈报」类留痕不入触发源闭集；前进链单向（4→1 类回退全部落非法）；签字集合按表2-3 六节点行硬编码；触发源六闭集校验在位；timeouts 缺省 48h/24h（§13）。
- 租约：四字段＝{ticket_id,path_globs,seat_id,hash} 精确闭集；countersign 必填且签注人须 `architect:` 前缀（§7）；实例化源＝seat-permissions.json 逐席位行；请求路径集须为写域行子集（零裁量）；`deny_globs` 数组已随工程师等席位埋设（消费实体在 T04 B5·消费面②）。
- seat-permissions 头部 `derived_from: 表2-1`＋表注三条款（路径锚定/判据真源双层双址/枚举款六类）照 v2.9 转录；工程师行「明确不可写」含 `仓根 tests/（跨发布验收判据真源·架构/QA 共写域）` 逐字随转录；两配置文件均带同源声明（断言在 T03 验收）。
- 交付物闭集纪律：代码件对 `.collab/` 零引用目标指针——补登演示脚本的登记件取数＝功能数据源（环境变量 `SWB_BASELINE_DOC` 优先，缺省在 refs/external 按 v2.9 登记名 glob 取最新落盘件，不写死带日期文件名），非引用目标；其余脚本无任何 `.collab/` 过程件引用。
- 仓闸随动修正一笔（闭集内合规修正·复检通过再落笔）：首跑闸 BLOCK＝`OA-T1 项目实体命中 pattern=date`（baseline-backfill-demo.py 缺省路径常量携带 `2026-11-03` 日期实体）→ 改为日期无关 glob 取数（同上条），A6 重跑读数见判据 6（全绿不变）；其余闸打印（check-pointers/check-ticket-reconcile 等旧账 WATCH/BLOCK 系 OA-D6 族既有旧账）随路由表走②打印不拦，非本笔新命中。
- 判据 6 重跑读数（修正后）：`A6_EXIT=0`；两 sha256 串 grep -o occurrence 各＝1；账本哈希读数＝`eea4638b…9990c936`／`2c9dbf51…a1b9f05c`（append-only 续链）。
- 测试件 argv 面：test_ledger_core 接受兄弟测试文件路径参数并按票面判据 5 形制机械执行（子进程退出码透传）。

## 禁动面自证
本笔 add 仅上面 12 路径；两基线登记件、`.collab/`（本回执除外）、`docs/`、T01/T03/T04/T05 闭集件、票面文字＝零触碰；两条 untracked 旧件（`.collab/qa/2026-11-01-TKT-*` 两支）未动未提交。账本/租约/状态/冒烟 docs 全部落系统 Temp。

## 停手项／候裁
无。Q-02 未触发（P7=pass）；Q-07 已裁（选项 A·双层双址条款已按现行口径落 T02-D）。无判据先天不可满足项（与 T01 判据 2 先例不同，本票八判据字面均可满足且全绿）。

## 完工读数
- commit：见本回执随笔（`collab:` 前缀·单独一笔·name-only＝12 件）；完工 HEAD 于回报附实测值。
