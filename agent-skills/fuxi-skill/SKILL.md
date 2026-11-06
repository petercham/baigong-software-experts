---
name: fuxi-skill
description: 伏羲双轨蒸馏技能入口：把「具名真实人物」与「可分离方法／技法文本」沿 persona／method 双轨各自提炼为常驻视角产物（-perspective）与即用即走能力卡（-technique），两轨独立中间表示、独立验证闸、永不相并；装载口径＝宿主显式注册制，分卷注册期预编译。Use when 要做视角蒸馏／能力卡蒸馏、要生成或审查 -perspective／-technique／-bundle 产物、要走对象分类四问与入池规程、或要为装载做分卷注册；触发词：蒸馏、视角、perspective、technique、能力卡、对象分类、入池、双轨、伏羲。
version: 2.0
agent_created: true
---

# fuxi-skill · 入口主件

**定位**：本件＝技能入口主件（工序主线表＋真源指针）。细则一律只指仓内真源路径、不复写——各真源件自包含成文，本件与其零重复。包级详细件＝`README.md`（性质自注＝交付件本体·相近工具对照表置顶），本件与它同源同版本线。

**与前序同名旧物（旧 V3 代工序件）无继承关系。** 旧代读者定位本包新真源：见 `references/legacy-disposition.md`（旧九卷七式处置表卷）。

**防误用**：本技能＝builder（蒸馏工序与门禁的工具链），不是产物库本体、不在运行时扮演任何人；产物（`products/` 池内 `-perspective`／`-technique`／`-bundle`）是编译输出，消费产物与使用本工序是两件事。

## 工序主线表（六步链·骨架在表，细则指真源）

| 步 | 动作一句话 | 细则真源（仓内路径） |
|---|---|---|
| ① 对象登记 | 候选对象以注册描述三元组（题名／对象描述／来源）登记入建表注册记录 | `adapters/classifier.md`（§一 输入定义；注册记录实体落点行） |
| ② 对象分类 | 分类器四问决策序出四值闭集 `person`／`method`／`mixed`／`out-of-scope`（建表注册时显式分类，非运行时路由） | `adapters/classifier.md`（四值闭集＋决策序＋判例表＋混淆表规程） |
| ③ 双轨蒸馏 | 按轨走对应填料件提取：persona 轨六路采集语料纪律／method 轨可分离文本前置 | `adapters/person.md`／`adapters/method.md`（各恰六节闭集） |
| ④ 验证闸门禁 | method 轨硬门／person 轨软门各自分立（判据不得互套）；结构层断言全批跑；验证记录字段同源 | `gates/validator-source-anchor.py`（method 硬门）／`gates/validator-public-anchor.py`（person 软门·格式检查表＝当期唯一门禁位，judge 层恒参考位）／`gates/assert-tool.py`（结构层·三态读数禁假绿）／`gates/validator-catalog.md`（断言目录＋字段注册表） |
| ⑤ 入池 | 产物入 active 生效池 `products/` 前置＝人工确认＋独立提案＋版本审计；确认前落隔离归档区 | `products/README.md`（池约定件·生效池定义＋条目确认引用行格式）；产物元数据与状态词表见 `contracts/artifact-contract.md` |
| ⑥ 装载 | 宿主显式注册制：分卷注册期预编译，装载期仅从已注册分卷选择 | `README.md`（使用口径段）；分卷细则欠账登记见 `references/legacy-disposition.md` 候补观察节 |

## 轨界与红线速览（详情各归真源件，此处只指不搬）

- 两 IR 永不相并（persona-IR ≠ technique-IR）；混合对象＝双蒸双验 bundle（编译形态之一，非第三 IR）：`README.md` 边界速览段＋`contracts/artifact-contract.md`。
- 输出规范：perspective／technique 各恰四节闭集＝`specs/perspective-spec.md`／`specs/technique-spec.md`。
- 证据分级／失败模式两契约＝`contracts/evidence-grading.md`／`contracts/failure-modes.md`（共享内核 L0，双轨共用）。
- 淘汰候选留档纪律＝`rejected/README.md`。
- 三态读数（PASS／FAIL／PENDING_STAGE）：PENDING 不算 fail 不算 pass、汇总单列，禁假绿——实现与口径见 `gates/assert-tool.py`。

## references 索引

- `references/legacy-disposition.md` — 旧代同名技能 references 九卷 → 本包新真源的逐卷处置表（旧代读者定位卷；处置＝判定＋指针，非搬运）。

## 修订注记

- v2.0（入口件换代批）：初版＝按包 `README.md` 使用口径重写入口主件（六步工序主线表＋真源指针制）；体量红线 ≤200 行；旧九卷处置表随批落 `references/legacy-disposition.md`。宿主装载面换代部署归注册面另工序，不在本件射程。
