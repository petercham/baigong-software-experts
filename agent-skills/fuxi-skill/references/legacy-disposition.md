# fuxi-skill · 旧代 references 九卷处置表（legacy-disposition）

> 性质＝交付件本体（自包含成文·换代处置映射面）。本卷＝宿主装载面同名旧代（旧 V3 代工序件）references 九卷 → 仓内双轨真源的逐卷处置表，供旧代消费方定位新真源。处置＝判定＋指针，非搬运——本卷零旧卷正文。
> 记法：以下路径＝包根相对。处置取值闭集（七式）＝直接随迁／适配／合并／拆分／降级／裁撤／不随迁——取值域沿用旧代导入处置技法口径，用作本次换代逐卷判定口径。
> 九行＝宿主旧代 references 卷目清单逐卷恰一行（卷名逐字）。架构席预判九行经工程师席对宿主面九卷只读实读逐卷复核，九行判定与仓内在册真源在场性相符，零改判。

| 旧卷名 | 旧职能一句话 | 七式判定 | 仓内承接真源路径 | 判定依据一句话 |
|---|---|---|---|---|
| `persona-lens-fields` | 人格镜片字段闭集表（11 字段＋件内禁项＋token 预算） | `裁撤` | `specs/perspective-spec.md` | 新链 perspective 输出规范已由 perspective-spec 四节闭集重写，旧字段表不随迁 |
| `technique-lens-card` | 技法镜片六维卡节序与检验半分界 | `裁撤` | `specs/technique-spec.md` | 新链 technique 输出规范已由 technique-spec 四节闭集重写，六维卡节序不随迁 |
| `pack-boundary` | 归包判定与边界表（资产类型→归属判定句） | `裁撤` | `adapters/classifier.md`＋`products/README.md` | 对象归属判定由分类器四值闭集＋决策序承载；包/池归属纪律由池约定件承载 |
| `contract-anchors` | V3 外部静态锚、契约确认读数与设计裁索引 | `裁撤` | `contracts/artifact-contract.md`＋`contracts/evidence-grading.md`＋`contracts/failure-modes.md` | 新链契约真源＝仓内三契约本体；旧卷所锚外部静态件（仓外 V3 卷）不随迁 |
| `self-distillation` | 自主蒸馏工序（调研计划／素材采集登记／先核事实候核账） | `裁撤` | `adapters/person.md`＋`contracts/evidence-grading.md` | 六路采集语料纪律在 person adapter 在册；素材证据分级与标注由 evidence-grading 契约承载 |
| `alias-naming` | 化名命名规程（锚／梗／联想三要件＋化名映射纪律） | `裁撤` | `products/README.md` | 新链产物实名 kebab 命名纪律在册（池约定件第一节），化名制整体废止 |
| `acceptance-blind-eval` | 验收卡与盲评规程（五维评分卡入库闸＋双席复跑） | `裁撤` | `gates/validator-public-anchor.py`＋`gates/validator-catalog.md` | 新链 person 轨验收＝格式检查表门禁位＋judge 层恒参考位（软门六层）；独立复跑原则由 validator 目录承载 |
| `token-cap-splitting` | 体量帽与拆件式闭集（单件帽值＋拆件四式＋压缩边界） | `降级` | `README.md` | 装载口径条款级在册（分卷注册期预编译，装载期仅从已注册分卷选择）；旧帽数值与拆件细则不随迁，欠账登记见本卷尾节 |
| `import-mapping` | 外部镜片库导入映射七式闭集（逐节处置表） | `不随迁` | `references/legacy-disposition.md` | 七式＝本次换代自身的处置技法，其成品即本卷；新链无导入工序 |

## 候补观察登记

- `token-cap-splitting` 降级行的欠账一句：分卷细则（旧帽数值口径、拆件式闭集、压缩要素对账规程）未随迁——分卷需求现仅条款级在册（包 `README.md` 使用口径段）。该细则日后如有真实消费场景，由装载面另卷补齐；本行＝候补观察登记，不另立工序。

## 卷尾登记行

- 宿主面旧代装载卷（宿主技能装载区同名旧代 `fuxi-skill` 卷＝本表九卷出处）：原位原状未触碰；其换代部署归注册面另工序，非本卷射程。

## 修订注记

- v1（入口件换代批）：初版＝旧九卷七式闭集处置表落交付面；九行判定经宿主面只读实读复核，架构席预判零改判。
