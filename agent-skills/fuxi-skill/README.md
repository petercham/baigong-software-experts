# fuxi-skill

> 性质＝交付件本体（包级 README 详细件·S4 定稿）。相近工具对照表置顶（先于任何二级标题）＝命名防误解硬性要求的登记位，机检＝BW-6。

| 维度 | fuxi-skill | nuwa-skill | cangjie-skill |
|---|---|---|---|
| 对象 | 具名真实人物／可分离方法·技法文本／混合对象（三类显式分类） | 具名人物（人格蒸馏） | 书籍·技法文本 |
| 产物 | `-perspective` 常驻视角产物＋`-technique` 即用即走能力卡（双规范永不相并，混合＝bundle 双蒸双验） | 人格产物单轨 | 能力卡单轨 |
| 验证 | 双验证器分立＋交叉嫁接（D2/D3）＋统一 harness＋人工锚点一致率协议（S0b） | 其自有验证链 | 其自有验证链 |

与前序同名旧物无继承关系。

一句话定位＝把「具名真实人物」与「可分离方法／技法文本」两类蒸馏对象，沿 persona／method 双轨各自提炼为常驻视角产物（`-perspective`）与即用即走能力卡（`-technique`），两轨各有独立中间表示、独立验证闸与独立护栏，永不相并。

产品前提＝合并基座、不合并路径：红利全部在共享内核 L0（语料纪律／证据分级／留档／治理／统一测量层），提取层与验证闸界保持双轨；合并已坏四条自查信号（IR 串味／锚失去可回查位置／门禁统一到最弱／内部矛盾消失）出现任一条＝退回分层，四信号为每次版本评审强制检查项（机械检出位＝ST-3/6/7／FC-3／GS-3/GS-5／BW-5）。

## 目录地图

| 目录 | 职能 | 在册件 |
|---|---|---|
| `specs/` | 双输出规范表（输出规范面·S4 建） | `specs/perspective-spec.md`（`-perspective` 规范表·四节闭集·机检 ST-8）／`specs/technique-spec.md`（`-technique` 规范表·四节闭集·段名前缀归一化口径钉死） |
| `contracts/` | 共享内核 L0（三契约·声明面） | `contracts/evidence-grading.md`（证据三级标注 EG-1..6）／`contracts/failure-modes.md`（失败模式 if-then 表 FM-1..5＋条目）／`contracts/artifact-contract.md`（产物契约 AC-1..5·状态词表与看板契约） |
| `gates/` | 结构层门禁（机械断言）＋交叉加固 validator（S3） | `gates/assertion-catalog.md`（断言目录·27 项）／`gates/assert-tool.py`（断言工具·退出码闭集 0/1/2·内置 selftest）／`gates/validator-source-anchor.py`（method 轨硬门 validator·六层·生成/判分分离）／`gates/validator-public-anchor.py`（person 轨软门 validator·六层·格式检查表＝当期唯一门禁位·judge 分数只作参考位）／`gates/harness-common.py`（harness 非判据共用件·无判据无阈值）／`gates/validator-catalog.md`（validator 断言目录＋验证记录字段注册表＝同源定义面·阈值预注册表） |
| `adapters/` | 双轨填料＋对象分类器（S2 建） | `adapters/person.md`（persona 轨 adapter·六节闭集）／`adapters/method.md`（technique 轨 adapter·六节闭集）／`adapters/classifier.md`（对象分类器·四值闭集＋决策序＋判例表＋混淆表规程） |
| `rejected/` | 淘汰留档区（可枚举基面） | `rejected/README.md`（留档约定＋coverage-audit 三问口径） |

产物生效池在包内路径 `products/`（active 池约定件＝该目录 README；未生效留档走隔离归档区约定名 `archive/`）。

## 边界速览（详情各归本件）

- 两 IR 永不相并：persona-IR 五层 ≠ technique-IR RIA++ 六段；混合对象经双蒸双验打包为 bundle（编译形态之一，不是第三 IR）。
- 验证闸界：method 轨确定性硬门（机械断言→三臂对照→诱饵测试→留出集）；person 轨 public-anchor 软门（盲评 rubric＋绝对线＋decoy＋泄漏检查＋人工锚点）；两侧判据不得互套。
- 风险档分轨：person 轨联网＝独立开关默认关＋opt-in＋来源黑名单；method 轨 Air-gapped（外部请求计数恒 0）。
- 对象分类发生于建表注册时（显式分类器）；产物轨别与输入对象分类两词表不同层不互替。

## 使用口径

对象登记 → `adapters/classifier.md` 分类（四值闭集＋决策序）→ 对应 adapter 蒸馏（`adapters/person.md`／`adapters/method.md`）→ validator 门禁（method 轨 `gates/validator-source-anchor.py` 硬门／person 轨 `gates/validator-public-anchor.py` 软门；结构层断言＝`gates/assert-tool.py`）→ 产物入 active 生效池 `products/`（**人工确认前置**：入池须人工确认＋独立提案＋版本审计，确认前落隔离归档区，见池约定件）→ 装载口径按宿主显式注册制（分卷注册期预编译，装载期仅从已注册分卷选择）。

术语表（六词）：

- **基座**＝共享内核 L0（`contracts/`＋调度与门禁），只调度与门禁、不含领域判据。
- **adapter**＝双轨填料件（提取结构与各轨判据所在），基座/填料界＝B1。
- **validator**＝轨各一的分立验证脚本（硬门/软门），闸分离的物理体现。
- **门禁位**＝拉退出码的判定层（method 轨六层机械链；person 轨当期＝格式检查表＋泄漏检查）。
- **参考位**＝只出读数不进门禁的判定层（person 轨 judge 层当期恒参考位，读数与 `calibration_state` 并列行）。
- **三态读数**＝PASS／FAIL／PENDING_STAGE（未验同族）：PENDING 不算 fail 不算 pass、汇总单列，禁假绿。

## 修订注记

- v2（2026-10-30·S4 批）：骨架升级＝详细件定稿：相近工具对照表置顶（机检 BW-6）＋目录地图增 `specs/` 两规范表＋断言计数随批 20→25＋使用口径与术语表新段；「S4 补全登记」两勾选框随本批关闭。版本受控＝本文件随批版本号递增。
