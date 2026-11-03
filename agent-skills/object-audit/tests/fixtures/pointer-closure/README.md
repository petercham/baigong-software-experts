# pointer-closure 对拍测试件（ENG-G2 WP-3）

> 件级来源帽：本件系通用纪律落地批（WP-3）所立对拍件，两检查各含正例／反例／豁免行／遮除行／自咬反例。
> 本目录是**预期违规样本**：全仓扫描的缺省包面不含本件所在目录（object-audit 不在缺省两包面内），
> 只有脚本 `--selftest` 口径才以本目录为包面。预期数写死在脚本 `EXPECTED` 常量，
> 改本目录任何样本必须同步改预期数，否则对拍红。

## 样本清单

| 件 | 喂给 | 预期 |
|---|---|---|
| `violations.md` | OA-D6-3 | 四模式各一行真命中＝VIOLATION 4 |
| `exempt.md` | OA-D6-3 | 两行带豁免标记（史实锚／T-注）＝EXEMPT 2 |
| `substr.md` | OA-D6-3 | 反引号段两行＋围栏内两行＝SUBSTR 4 |
| `dangling.md`＋`refs/present-target.md` | OA-D6-4 | 带目录段不可达指针＝1；可达指针与裸基名＝0（自咬反例判绿） |
| `README.md`（本件） | 全检 | 描述性措辞不含四模式字面＝0 命中（扫描器不咬自家说明书·自咬反例） |

合计预期：OA-D6-3（VIOLATION）＝4／OA-D6-4＝1；三态分账 EXEMPT＝2／SUBSTR＝4／VIOLATION＝4。
