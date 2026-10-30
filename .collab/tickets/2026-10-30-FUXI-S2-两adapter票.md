# FUXI-S2 · 两 adapter 票

> 票号＝FUXI-S2｜开票＝主理人｜日期＝2026-10-30｜被派＝工程师席
> ANCHOR＝开工前取当轮 HEAD 实测读数（回执开端必附）
> 施工输入真源（直读照做）：
> ①`.collab\design\2026-10-30-FUXI-S2-票面前置定义-v1.md`——对象分类器（四问决策序·四值闭集 {person,method,mixed,out-of-scope}·11 判例表·混淆表规程 n=48/硬下限 40·总体一致率 ≥85%＋mixed 召回 ≥75% 已锁定）＋hold-out 两轴（轴一＝时间轴照 v2.1 P-7；轴二＝近邻对象/主题配平轴·写死）＋§三 S2 骨架（adapters 章节闭集·编译形态）。主理人已裁：C-1 采四值＋分层消歧／C-2 轴二定名照准／C-3 预注册值锁定／C-4 `adapters/` 子目录落点照准。
> ②设计真源（只读）＝`.collab\design\2026-10-30-fuxi-skill-merge-boundary-design-v2.md` §十一 S2 行＋§三 分轨 schema＋R19/R23/B5/B10/D10。
> 派票口径＝S2 不以 S1 验收为硬门（按序派发不互锁·S1 已 PASS 在案）。

## 一、任务（交付闭集）

声明闭集：
- `deliverables/skills/fuxi-skill/adapters/person.md`
- `deliverables/skills/fuxi-skill/adapters/method.md`
- `deliverables/skills/fuxi-skill/adapters/classifier.md`
- `deliverables/skills/fuxi-skill/gates/assert-tool.py`
- `deliverables/skills/fuxi-skill/gates/assertion-catalog.md`
- `deliverables/skills/fuxi-skill/README.md`

1. **person adapter**：按前置定义 §三骨架＋v2 §三 persona-IR 五层节闭集成文（六路采集／五层 persona-IR／防编护栏／常驻语义／联网独立开关默认关 R19）。
2. **method adapter**：同构（Adler+ 五路提取／RIA++ 六段 technique-IR／防误触发护栏／即用即走语义／Air-gapped R19·外部请求计数恒 0 声明）。
3. **对象分类器**：前置定义 §一决策序＋判例表成文入 `classifier.md`（输入注册三元组→四值闭集·边界判例照抄）。
4. **工具随动**：FC-5〔S2 执行〕（bundle 两层验证状态字段命名空间隔离·互借字段检出＝0·R23）转实装；**黄-2 收口**＝FC-4 接入看板状态 token 扫描（看板正文/契约词表句私扩值必咬）；**黄-1 随动**＝断言目录 FC-2 条目文案「既有4＋新增21」改实数 26（4+22），看板栏沿写处不改（板＝历史存证）。
5. **断言目录随动**：FC-5 标签→实装；两 adapter 结构断言（person 无「执行步骤」段／method 无「表达 DNA」段——ST 类新增两项〔S2 建〕）登记。
6. **包 README**（新建）：fuxi-skill 包级 README 骨架（产品名＋一句话定位＋目录地图 contracts/gates/adapters/rejected；详细件与相近工具对照表留 S4 补全——登记为 S4 验收位不展开）。

## 二、验收判据（照抄 v2 §十一 S2 行＋前置定义＋裁值）

1. 两 adapter 互不含对方 IR 字段——工具脚本可查实跑：person.md 无「执行步骤」段、method.md 无「表达 DNA」段，diff＝∅。
2. method 轨外部请求计数恒 0：声明在场＋静态检查（method.md 无联网工具调用条款）读数。
3. person 轨离线运行用例通过（离线声明＋开关默认关条款在场，实跑留 S3 harness，当期＝条款级验证）。
4. 三类样本分类与人工标注一致附混淆表：分类器规程件实存＋混淆表规程（n 值/达标线/盲标操作定义）照前置定义逐点；当期无真实样本＝规程级验收，读数标注「规程在场、实测待 S3」。
5. 语料主题配平检查条款（D10）在两 adapter 语料执行面条款在场。
6. FC-5 转实装 selftest 配对咬放；黄-2 扫描接入后坏样本（看板私扩 token）必咬复现。
7. assert-tool selftest 全绿 exit 0；连跑两次全等；run-gates GATE PASS 零新增红（前后附证）。
8. 全件零过程域指针（pointer-closure VIOLATION＝0）；命名英文 kebab。

## 三、纪律

- 只写上列声明闭集六件（交付笔单笔·前缀 `ENG-S2:`）＋回执笔（`.collab\receipts\2026-10-30-ENG-S2-工程师回执v1.md`·开端附 ANCHOR＋完工 HEAD＋清单≡name-only＋八读数）。
- 看板新板（如记 S2 事件）＝过程笔另 commit（`.collab\board\`）。
- 禁 --no-verify、禁 amend、禁 push；遇 HOLD 不开工（本票无 HOLD）。
- 候补池不动：黄-3（value_decl_diff 逐点位口径）不在本票范围。
