# collab-lint 对拍测试件（EAC-SK5）

性质＝施工输入｜受众＝机检维护者（闭集声明）

> 件级来源帽：本件系 EAC-SK5 机检票（T4）所立对拍件，三检查各含正例／反例／豁免行／自咬反例。
> 本目录是**预期违规样本**：`check-collab-lint.py` 全仓扫描默认排除 `tests/fixtures/`（扫描面收窄＝主豁免的延伸），
> 只有脚本 `--selftest` 口径才扫本目录。预期数写死在脚本 `EXPECTED` 常量，
> 改本目录任何样本必须同步改预期数，否则对拍红。

## 样本清单

| 件 | 喂给 | 预期 |
|---|---|---|
| `.discussion/20261099-001-a.md`＋`.discussion/20261099-001-b.md` | EAC-L3 | 同编号两文件＝1 条 |
| `.discussion/20261099-002-round2.md` | EAC-L1 | 收敛类（收敛表态签字轮）缺「合流与分歧清单」节＝1 条 |
| `.discussion/20261099-002-round2-v2.md` | EAC-L3 | 同轮 v2 形态＝1 条（不进唯一性分组，避免双计） |
| `.discussion/第三轮汇总意见报告.md` | EAC-L1 | 头部缺「新提议登记」字段＝1 条 |
| `.discussion/第七轮汇总意见报告.md` | EAC-L1 | 登记「新提议＝无」→「应改出议题件」提示＝1 条 |
| `.discussion/20261099-003-round3-议题包.md` | EAC-L1 正例 | 收敛类＋该节在位＝0 条 |
| `handoff-sample.md` | EAC-L2 | VIOLATION 3＋EXEMPT 3＋SUBSTR 3 |
| `plain-normal-doc.md` | 全检 | 不在任何扫描面＝0 条（扫描面收窄＝主豁免实证） |
| `fence-sample.md` | EAC-L2（EAC-SK5-F 增补） | 围栏两行示例＝SUBSTR＋2；`GPT-4` 泄漏反例（修后判违规）＋CJK 紧邻提案编号（编号前无空格）钉死＝VIOLATION＋2；日期文件名钉死＝0 |
| `tickets/dir-scan-sample.md` | EAC-L2（EAC-SK5-F 增补） | 无声明行、靠 tickets 目录分支入面＝VIOLATION＋1（目录扫描分支 selftest 执行钉死） |

合计预期：EAC-L1＝3／EAC-L2（VIOLATION）＝6／EAC-L3＝2；三态分账 EXEMPT＝3／SUBSTR＝5／VIOLATION＝6。

## 自咬反例说明

`handoff-sample.md` 反引号段内的禁模式示例＝SUBSTR 判绿样本；扫描器自身源码注释内的
禁模式示例同样因反引号遮除判 SUBSTR——「扫描器引用禁模式不被禁模式杀掉」由此实证。
教训来源＝check-entity 头注所记「自伤先例」。
