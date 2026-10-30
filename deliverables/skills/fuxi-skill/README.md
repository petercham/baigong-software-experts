# fuxi-skill

> 性质＝交付件本体（包级 README 骨架·S2 建）。详细件与相近工具对照表留 S4 补全（登记为 S4 验收位，本骨架不展开）。

一句话定位＝把「具名真实人物」与「可分离方法／技法文本」两类蒸馏对象，沿 persona／method 双轨各自提炼为常驻视角产物（`-perspective`）与即用即走能力卡（`-technique`），两轨各有独立中间表示、独立验证闸与独立护栏，永不相并。

## 目录地图

| 目录 | 职能 | 在册件 |
|---|---|---|
| `contracts/` | 共享内核 L0（三契约·声明面） | `contracts/evidence-grading.md`（证据三级标注 EG-1..6）／`contracts/failure-modes.md`（失败模式 if-then 表 FM-1..5＋条目）／`contracts/artifact-contract.md`（产物契约 AC-1..5·状态词表与看板契约） |
| `gates/` | 结构层门禁（机械断言） | `gates/assertion-catalog.md`（断言目录）／`gates/assert-tool.py`（断言工具·退出码闭集 0/1/2·内置 selftest） |
| `adapters/` | 双轨填料＋对象分类器（S2 建） | `adapters/person.md`（persona 轨 adapter·六节闭集）／`adapters/method.md`（technique 轨 adapter·六节闭集）／`adapters/classifier.md`（对象分类器·四值闭集＋决策序＋判例表＋混淆表规程） |
| `rejected/` | 淘汰留档区（可枚举基面） | `rejected/README.md`（留档约定＋coverage-audit 三问口径） |

## 边界速览（详情各归本件）

- 两 IR 永不相并：persona-IR 五层 ≠ technique-IR RIA++ 六段；混合对象经双蒸双验打包为 bundle（编译形态之一，不是第三 IR）。
- 验证闸界：method 轨确定性硬门（机械断言→三臂对照→诱饵测试→留出集）；person 轨 public-anchor 软门（盲评 rubric＋绝对线＋decoy＋泄漏检查＋人工锚点）；两侧判据不得互套。
- 风险档分轨：person 轨联网＝独立开关默认关＋opt-in＋来源黑名单；method 轨 Air-gapped（外部请求计数恒 0）。
- 对象分类发生于建表注册时（显式分类器）；产物轨别与输入对象分类两词表不同层不互替。

## S4 补全登记（验收位·不在本骨架展开）

- [ ] 详细 README 件：产品定位展开＋使用路径＋术语表。
- [ ] 相近工具对照表置顶：本产品线 vs nuwa-skill vs cangjie-skill（对象／产物／验证三行对照）；如涉同名歧义，对照表内一行声明「与前序同名旧物无继承关系」，不展开。
