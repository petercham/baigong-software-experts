# SWB-ADR 工序票 · B 席 QA 审回执 v1（qa-adrtk·只读审票零施工·fresh eyes）

- 开工实测 HEAD＝`f1bfaa1`（＝作者席两黄修订笔·与派单预期一致）；工作区除本回执件零改动。
- 被核件＝`.scratch/tickets/2026-11-04-SWB-ADR-process-ticket.md`（v1 终态·起草笔 `89734fd`＋修订笔 `f1bfaa1`）。
- 前序链直读核对在盘：拍板登记件 `.collab/decisions/2026-11-04-皮总拍板-ADR工序链确认.md`（`b0b449d` 在链且为 `f1bfaa1` 祖先·`git merge-base --is-ancestor b0b449d f1bfaa1` exit 0）；A 席回执 `.collab/qa/2026-11-04-SWB-ADR工序票-A席产品审-v1.md`（`4065311`）；架构席对照评估件（G-1～G-7）在盘。
- 纪律：已决工序链与条款甲/乙正当性不重审；本审只核成文一致性/平台兼容/判据可跑/修订零扰动/候裁无夹带。

## 总裁决：**拦**（红 1 · 黄 1 · 绿 4＋注记三条）

红-1 非工序链本身问题、非 A 席两黄残留——是 G-2 数据面增行与在盘机件硬编码的**未登记冲突**：按票面原文施工必致派发机全链 FATAL，且修机件无写权路（闭集不含、禁动面禁触、候裁③射程不覆盖）。修票一笔（候裁⑥单列或闭集扩员条款）后可复审放行。细则见下。

---

## 红-1（拦）：G-2 节点行 append 击穿 dispatch-builder 七行硬断言＋S3 测试同断言——闭集无配套件、禁动面禁触、候裁③不覆盖＝按票施工必然破坏派发机

**实证实跑**（Temp 面仿真·仓内零残留）：
- 机件硬编码＝`skills/sop/scripts/dispatch-builder.py` L65–66：`if len(spec.get("nodes", [])) != 7: raise SystemExit("FATAL: dispatch-spec 行数≠表2-3 七行（六节点＋维护行）")`——load_spec 无参数化、无节点数注记键可读。
- 测试实体同钉＝`tests/s3/test_dispatch_gate.py` L60：`assert len(spec["nodes"]) == 7`（现盘基线跑 PASS exit 0）。
- 仿真读数＝现盘 dispatch-spec（7 nodes）深拷贝 append 票面 L48–58 形态的「ADR·落盘」行（8 nodes）写入 Temp 后调 `load_spec`：`SystemExit: FATAL: dispatch-spec 行数=8 ≠ 表2-3 七行（六节点＋维护行）`——**任何**后续派发（含非 ADR 票）均在 load_spec 处 FATAL＝fail-closed 全线停摆。

**票面授权面逐条对不上**（行号＝被核件）：
1. 闭集 8 件（L20–28）不含 `skills/sop/scripts/dispatch-builder.py`、不含 `tests/s3/`；
2. 禁动面 L111「seat-permissions.json / hooks-map / **scripts 七脚本** / 60-gates / dispatch 卷零触碰」——dispatch-builder 在七脚本射程内，施工批碰不得；
3. 候裁③（L119）登记射程＝「docs/adr 目录初始化＋门禁常驻挂载＋E-ADR-3″ 校验器实装（涉脚本）」＝ES2 双前置②口径——**未含 dispatch-builder 行数口径随动**＝缺位清单 G-1～G-7 与 a84ca78 评估件均未列此项（评估件①只及「租约四字段无节点维」，未及 dispatch-builder 七行钉）。
4. 判据 2（L98）「dispatch-spec.nodes 含 node=="ADR·落盘" 恰 1」＝验收侧只查新行存在，不查机件兼容——验收绿与机件红可并存＝**判据族漏检面**。

**定性**：这是票面内部可预见的自相矛盾（G-2 要求落行 × 禁动面＋闭集使随动修复无路），非需求争议、非已决链重审。修补建议（归起草席措辞·本审不代拟定稿）：二选一——①新增候裁⑥单列「dispatch-builder 行数口径＋S3 测试随动＝涉脚本改动·归 trigger 批同批」并把工序链首支 ADR 落盘前的过渡态（8 nodes 与 7 行硬码共存窗口）写明禁派发窗口或先修机件顺序条款；②闭集扩员纳入两机件套随笔（须先裁其写权通道＝config/**、tests/** ∈ engineer write_globs 在盘可路·票面 L14 自证）。任一即可销红。

## 黄-1（本席新出）：判据 4 钉死文本 × 判据 7 增量界 ≤180 互斥——按票面给定文本逐字落位必红判据 7（预算超约 12）

**实跑**（Temp 面 dry-run·script-v1 口径＝`tools/count_agent_tokens.py` 同款 CJK≈1/非CJK≈4·ceil·对现盘三卡施加票面 L74–76 纪律行＋L78 G-7 换代行文本逐字转写）：
- architect 942→1056（Δ114＝纪律行 74＋换代行净增 42）；product 860→899（Δ39）；qa 1044→1083（Δ39）；**合计 Δ192 ＞ 判据 7（L103）「增量合计 ≤180」**。
- 各卡 ≤2500 界无虞（最大 1056）。转写误差 ±5 量级不改变结论（余量仅 ~12）。
- 定性：判据 4（L100）钉「三卡各新增纪律行恰 1 行」＋换代行含「docs/adr/ 除外」＝文本被票面锁死，施工席无权自删字；判据 7 预算随之必炸。一行级修法＝预算上修（≤210）或起草席压缩换代行措辞——归作者席二选一，不触结构。

## 绿 1：修订零扰动核验——`89734fd`→`f1bfaa1` diff 恰三处文句级·G 处置结论/闭集/条款甲乙/禁动面零动

- `git show --name-status f1bfaa1`＝载体恰一件（`M .scratch/tickets/2026-11-04-SWB-ADR-process-ticket.md`）；`89734fd` 载体恰一件（`A` 同路径）。双笔均单笔单件 ✓。
- diff 读数＝恰三 hunk：①L69 SOP 会签语义追加「保留项闭合归位」段（销 A 席黄-1）；②L102 判据 6 仓根路径→全路径（销 A 席黄-2）；③L120 候裁④状态注记（随动 b0b449d）。声明闭集（L20–28）、条款甲乙（L34–35）、G-1～G-7 处置结论文句、禁动面（L107–113）、候裁①②③⑤正文——diff 零染 ✓。
- 票面 L123 落款行/起草读数行未随修＝「史实如实不改」口径与 L120 注记自洽 ✓。

## 绿 2：验收判据 1–9 独立复跑（现盘＝施工前态·开工复测口径）——除判据 7 界见黄-1 外全可跑，判据 6 修后口径非假绿坐实

| 判据 | 复跑读数 | 判定 |
|---|---|---|
| 1 闭集全等 | 两载体笔文件集＝{票面} ⊆ 闭集（票面自身落 .scratch 面沿 B 批先例）；config/交接件/scripts 交集＝空 | ✓可跑 |
| 2 同源断言 | python 现盘实跑：`set(authors)==set(types)`＝True（8=8）；三 config `json.load` exit 0；nodes＝[1..6,'维护·节点1-3'] 无「ADR·落盘」（施工前＝0 预期） | ✓可跑（新行恰 1 为施工后断言，机件击穿见红-1） |
| 3 票型钉值 | `grep -c '"ADR"' config/ticket-types.json`＝0（exit 1·施工前预期）；施工后钉 1 可跑 | ✓ |
| 4 SOP/卡面钉值 | standard-sop `grep -c "ADR"`＝0（施工前）；architect 卡现盘 L24＝裸行「明确不可写：`docs/`」在位（换代后可跑） | ✓ |
| 5 config 零染 | seat-permissions/hooks-map 两笔零出现＝现盘 git log 可跑 | ✓ |
| 6 基线/STRUCTURE 零染 | 交接件/STRUCTURE 现盘零 diff 可跑；**修后全路径** `git ls-files agent-experts/baigong-software-team/docs/adr/`＝0 ✓——与闭集条目 L28 同锚（项目根＝含 docs/STRUCTURE.md 探针锚目录＝bundle 根·seat-permissions L5 两级锚条款），路径非恒零空转＝A 席黄-2 假绿风险确已消解 | ✓（修后成立） |
| 7 token 界 | 五值实跑（工具输出序·script-v1＋被测 `f1bfaa1`＋实测人 qa-adrtk＋ceil）：lead 1533／architect 942／engineer 1115／qa 1044／product 860——与票面 L16 五值集合全等；增量界见黄-1 | ⚠ |
| 8 负例 | 「终写件与收口草案 diff 非空」Temp 面构造可跑 | ✓可跑 |
| 9 纪律 | 双闸＋pre-commit 真跑在盘实核：`.git/hooks/pre-commit`→`agent-skills/object-audit/scripts/run-gates.sh`（八检查含 check-ticket-reconcile·非空转） | ✓ |

## 绿 3：产品↔架构一致性＋写通道/租约/hooks-map 面核盘（红-1 之外零矛盾）

- 席位卡/config/租约面：architect write_globs 含 `docs/adr/`（seat-permissions L33）＋三件套外 docs 子面不入 deny、防护＝签发面写域子集校验＋写侧租约双兜底（L37 注记原文在盘）＝票面 L78「机制面零改动仅卡面对齐」取证属实；hooks-map L16（product）/L24（qa）deny 含 `.collab/drafts/adr/**`＝票面 L77「会签席不可改草案」取证属实；lease-issuer L20 四字段＝{ticket_id,path_globs,seat_id,hash} 无节点维＝docs/adr 挂席位租约通道（path 维）兼容，与 a84ca78 结论一致。
- config/**、agents/**、skills/** ∈ engineer write_globs（L53）＝票面 L14 写通道取证属实；docs/STRUCTURE.md ∈ architect deny 枚举（L36）且不入任何 write_globs＝候裁②取证属实。
- 黄-1 修后「保留项闭合归位」段（L69）：呈人类裁定→decisions 登记（host write_globs 含 `.collab/decisions/`·L13）→架构席重誊草案落 `.collab/drafts/adr/`（architect 既有写域）→全链重走会签——**三跳全落既有写域＝零新开**；与 §12/C1 通道零冲突（改权仍归 C1·L62 两线成文未动）；死锁消解成立（草案修订权＝架构席照新裁定重誊·誊聚无裁量·条款甲语义延伸自洽）。✓
- 表2-3 现盘七行（L127–136 物理行）与 dispatch-spec nodes 七行同源对齐＝票面 L12 锚行读数（§3 L141／表2-3 L131、L136／§12 L205、L206）逐行复验全中。✓

## 绿 4：WorkBuddy 装配兼容性＋候裁①②③⑤无夹带＋候裁④闭合注记与盘上实态相符

- 闭集 8 件皆 bundle 内常规装配面（三 config＋三席位卡＋standard-sop.md），docs/adr 条件件带「单独施工批禁触」硬注＝无未裁目录预建；候裁③不出票面＝门禁挂载延至触发批，工序本身经 SOP 节＋账本签字（state-transition 既有通道）可先行运转＝不致工序不可执行（ES2 双前置②在册）。✓
- 票面正文逐段扫：对产品面改动＝product 卡一行＋节点行 product 注入面；对 QA 面＝qa 卡一行＋节点行 qa 注入面；均在已拍链成文射程。G-6 STRUCTURE 条目/G-5 基线三行＝只给文本不落位（候裁②/①②）。候裁⑤备选案零夹带正文。✓
- 候裁④状态注记实核＝`.collab/decisions/2026-11-04-皮总拍板-ADR工序链确认.md` 在盘、b0b449d 落链且为票面修订笔祖先＝「已闭合随 b0b449d」与盘上实态相符；票面 L5 起草读数行保留史实＝合规。✓

## 注记三条（不判档·供裁定笔/回执引用）

1. **基线哈希自锁实态**（供候裁①裁）：交接件现盘全文 sha256≠L5 声明值（实测 `3fda41e6…` vs 声明 `3f335333…`）——因 B4-D 已在盘落「追认注记」尾追加（L261·自declared「V13 恒等式保护＝物理 L261 起尾追加区·三基线哈希不扰动」）＝**盘上已有「尾追加不入 V13 段」先例格式**；候裁①选项应含此先例（采「勘定追记」节与 B4 先例同构）。本审不复算 B4 回执口径的段哈希（naive 行切复算不命中≠B4 处置失效）。
2. **票面 L16 五值序**＝「(lead/product/architect?) 序按工具输出面回执复测钉值」——工具输出序（路径字母序）＝architect 942／engineer 1115／lead 1533／product 860／qa 1044；票面猜测序有误但已自我声明随复测钉值＝自消解，回执复测值已随判据 7 行钉死。
3. **state-transition 超时回落**＝票型未在 timeouts 时回落「工程师票」缺省（L126 在盘实码）＝ADR 类入 types 无机件炸点；write-guard/serial-gate 无 authors/types 硬编码（grep 零命中）。

## 对 A 席三绿两黄的复核意见

- **黄-1（保留项闭合死锁）→ 修后销账确认**：修订笔 L69 补段与 A 席建议方向一致（呈人类裁定＋架构席重誊），本席绿 3 独立复跑三跳写域归属＝全部既有域、deny 语义不损、与 §12 无碰——消解成立，非文字遮羞。
- **黄-2（判据 6 假绿）→ 修后销账确认**：全路径口径与闭集条目、两级锚条款三处对齐（见判据表行 6），修后断言非恒零空转。
- **绿 1（工序链成文无走样）→ 复核同意**：票面 L4/L50/L68/L34–35/L70–71/L74 与拍板件 L14–19 逐要素再对照无走样（A 席表已列，本席抽验链序/条款甲乙/owner-champion 语义三处独立复读一致）。
- **绿 2（调研件引用无走样）→ 复核同意**：R10/R11/R21 引语语义与补核件结论一致性抽验通过；票面对「产品+QA 会签」未挂业界旗号＝无冲突表述。
- **绿 3（候裁无夹带）→ 复核同意**：本席独立扫描结论同（候裁①②③⑤正文零夹带）；并补候裁①盘上先例注记一条（见注记 1）。
- **A 席未覆盖面＝本席红-1**：产品审射程不含机件硬编码对账，G-2 增行与 dispatch-builder/S3 测试七行钉冲突为 B 席新出——非 A 席失察，属机件面审计射程。

## 红黄清单摘要

- **红-1**：G-2「ADR·落盘」节点行 × dispatch-builder.py L65–66 七行硬断言（＋tests/s3 L60 同钉）＝按票施工后 load_spec FATAL、全派发停摆；配套修机件无授权路（闭集不含·禁动面 L111 禁触·候裁③不覆盖）→ 修票：候裁⑥单列或闭集扩员＋过渡态条款，复审可销。
- **黄-1**：判据 4 锁死文本下判据 7 增量预算 ≤180 必炸（dry-run Δ192）→ 预算上修或措辞压缩，一行级。
- **绿**：修订零扰动恰三处／判据族除 7 外全可跑且判据 6 修后非假绿／写域·租约·hooks-map 一致性（红-1 外）／装配兼容＋候裁无夹带＋候裁④注记属实。

**总裁决：拦**（红-1 一处·修票一笔即复审；工序链与条款甲乙本体无议）。

——qa-adrtk B 席 QA 审·只读零触碰·除本回执件零文件改动·开工读数 HEAD `f1bfaa1`。
