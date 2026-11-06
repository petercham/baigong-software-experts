# FUXI-FX-U6 · 入池确认包 · david-fincher（呈皮总）

> 票号＝FX-U6｜工序＝S3 确认包件（票面 §二 S3·闭集第 8 件·「一句话可批」本体）｜日期＝2026-11-06｜备包＝工程师席（FX-U6 票内新鲜实例）｜呈递路径＝经主理人呈皮总
> 本件＝S4 人工闸的呈审面对象。工程师席备包即停：包成即停手，确认前禁移池、禁预建 confirmation.md（票面 §四「人工闸不可代位」）。

## ① 一句话请求

**批准 david-fincher-perspective v0.2 入 active 生效池？是／否**

（批准范围＝限本对象·限 v0.2 版；拍「是」＝进入 S5 移池＋confirmation.md 首单实例；拍「否」＝留 pending/ 待补，本票按否收口上报。）

## ② 资格读数表

| 项 | 当期实读数（开工 ANCHOR `b813207` 现盘实跑） | 判定 |
|---|---|---|
| 门禁 27 项三态汇总 | `PASS=25 FAIL=1 PENDING_STAGE=1 总数=27`·exit 1 | 汇总与开工基线全等 |
| 唯一 FAIL 归属 | BW-3 六处＝miyazaki 3＋mrbeast 3；**david-fincher 两处已由 U5（`5826b40`）补口径，当期明细零命中＝归零实证** | 本对象 BW-3 清账 |
| 结构门禁（ST 族） | ST-1..ST-10 全 PASS；ST-4 本对象回归条目 6/6、ST-10 批次 t9 逐路 18/18 在场 | 全绿 |
| 要素/注册/池规程（FC 族） | FC-1..FC-6 全 PASS；FC-6 现读「active 池条目 0·空池平凡真·规程级实证非产物级」＝**本单即其产物级实证对象** | 全绿（平凡真待替换） |
| 校准（GS 族） | GS-1..GS-5 全 PASS；GS-4＝κ 报告与 calibration_state 逐元组对账全一致（元组 2 在场·κ 点值 0.801887/1.0） | 校准态工具有据 |
| EG-6 门槛 | 一手占比 `58.3` ≥ `50`（统计口径：本人原文态条目数/要素条目总数；样本量 12；一致性系数 κ=0.801887＝s0c-anchors-b1 封印软门锚点·三锚对账链在册） | **门槛过** |
| selftest 四件 | 155／40／22／19 用例·反常全 0 | 判据活性在证 |
| 版本账 | v0.2／快照 2026-10-31／复审到期 2027-01-29（＝快照＋90 日实算逐字对上） | 审计通过（S2 件在案） |

## ③ 如实呈报面（三条，不加工）

1. **新鲜度窗口受限行在册**：落 12 个月窗口内条目=`4`/`12`＝窗口判据按字面不过，走 FM-S-01 受限路径如实登记（受限行＝`受限`，诚实边界节加厚降期望，禁凑档）。按在册口径该行不阻入池（PM 判词「无受限行」指无 EG-6 受限档位行），**是否接受窗口受限态入池由皮总当场裁**。
2. **三缺位在册，不得读作质量绿**：`control_arm`=`未测`（三臂对照缺位）；`leakage_check`=`未检`（题面未对照语料，输入面工件缺位）；judge 层（盲评 rubric／绝对线／decoy）＝参考位读数缺位。三者均为产物本体登记的缺位如实态。
3. **BW-3 红账存续对象非本对象**：唯一 FAIL 的六处裸数字全部属 miyazaki-hayao-perspective／mrbeast-perspective 两产物，不入本票射程（红账出清归各自后续入池批工序）；david 两处已清（U5 `5826b40`）。

## ④ 引用链

- 独立提案件（S1）：`agent-skills/fuxi-skill/.collab/design/2026-11-06-FUXI-FX-U6-david-fincher入池提案-v1.md`
- 版本审计件（S2）：`agent-skills/fuxi-skill/.collab/design/2026-11-06-FUXI-FX-U6-david-fincher版本审计-v1.md`（含移池前三文件 sha256 基线表）
- 票面（合同）：`agent-skills/fuxi-skill/.collab/tickets/2026-11-06-FUXI-FX-U6-首单入池实跑票-v1.md`（落账 `051b032`）
- 产物本体（pending 现位）：`agent-skills/fuxi-skill/products/pending/david-fincher-perspective/`（SKILL.md／registration.md／test-prompts.md 三件）
- 池规程真源：`agent-skills/fuxi-skill/products/README.md` §一入池前置＋§三确认引用行格式
- 确认落件（获批准后由主理人誊录）：`agent-skills/fuxi-skill/.collab/decisions/2026-11-06-FUXI-入池确认-david-fincher-perspective-v1.md`

## ⑤ 批准话术草案（＝誊录模板）

皮总拍「是」时，主理人按下列形态誊录（确认原话＋确认人＋日期＋批准范围限本对象本版本）：

> 确认人＝皮总｜日期＝<确认当日>｜确认文本（原话）：「批准 david-fincher-perspective v0.2 入 active 生效池。」｜批准范围＝限 david-fincher-perspective 本对象、限 v0.2 本版本。

confirmation.md 四字段引用行预填值（S5 获确认后落用，产物id 与目录名逐字全等）：

```json
{"产物id": "david-fincher-perspective", "人工确认引用": ".collab/decisions/2026-11-06-FUXI-入池确认-david-fincher-perspective-v1.md", "提案件引用": ".collab/design/2026-11-06-FUXI-FX-U6-david-fincher入池提案-v1.md", "版本审计引用": ".collab/design/2026-11-06-FUXI-FX-U6-david-fincher版本审计-v1.md"}
```

（预填值仅为待裁预案；**人工确认引用字段在皮总确认落 `.collab/decisions/` 之前不生效**，工程师席不预建该件、不预填指向非皮总件——票面 §四。）

——工程师席（FX-U6 票内新鲜实例）备包·2026-11-06·包成即停于 S4。
