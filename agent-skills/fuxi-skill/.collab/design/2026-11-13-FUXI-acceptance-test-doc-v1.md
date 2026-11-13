# FUXI · 验收测试文档 v1（口径件 A1-A11 对位测试条目十一枚）

> 性质＝过程域验收资产（验收测试文档·裁定 2026-11-12 方向修正件下游①·起链＝FX-U49）。上游真源＝agent-skills/fuxi-skill/.collab/design/2026-11-12-FUXI-产品口径件-v1.md（rev-2 终面·A1-A11 逐条＝本文件条目编号同源同序）。衔接纪律＝条目全部对位既有 `agent-skills/fuxi-skill/gates/assertion-catalog.md` 27 项断言（编号闭集）与其 runner 现跑读数，**不另造平行体系**——每条目自带「与既有断言衔接注」（复用／补位／不重叠三态）。
> 执行口径＝全部命令在仓根 D:\multi-agent-collab-devkits 下照跑；全部预期读数＝FX-U49 起草当轮（HEAD 754530b）实测登记，复跑不符＝红（如实登记不凑绿）。
> 判定三态闭集（人工条目通用）＝`满足`／`不满足`／`未验`（缺位即未测禁凑绿·承 EG-6 三态登记纪律）。
> 体量红线＝本文件 ≤400 行（验收判据＝wc -l 读数随收口回执）；条目头计数判据＝`grep -c "^### T-A"` ≡ 11。

## 〇、A 系→测试条目→既有 27 断言 衔接总览

| 条目 | 被测口径（口径件节） | 机检侧（既有断言复用） | 文档层补位（无对应机检臂处） | 判据类型 |
|---|---|---|---|---|
| T-A1 | §二 A1 结构机检基线全绿 | 全部 27 项＋selftest＝判据本体 | 无（全复用） | 机检 |
| T-A2 | §二 A2 契约与规范闭集存续 | ST-1／ST-2／FC-1／FC-2／ST-8 | 三契约节数人核对盘面 | 机检＋人核 |
| T-A3 | §二 A3 入场资格轴出口口径 | ST-9（四节节闭集）／ST-10（六路声明↔落盘） | 门槛读数行对契约面值逐字核对（无臂） | 机检＋人核 |
| T-A4 | §二 A4 效用轴出口口径 | 无（EG-6 白纸「只注册字段名不嵌值·零数值断言臂」） | 定线对盘＋读数行形态四类机械读数 | 机检（在场性/计数）＋人核 |
| T-A5 | §二 A5 验收档位口径 | 无（票面声明面 grep 先例口径） | 档位逐字串对盘＋档三零预开在场性 | 机检（grep）＋人核 |
| T-A6 | §二 A6 失败与暂缓语义 | FC-2 FM 五元组纪律子检查 | 暂缓两件套在场性（无臂） | 机检（grep）＋人核 |
| T-A7 | §二 A7 产物池验收口径 | FC-6（无确认来源条目数＝0） | confirmation 四字段逐枚人核 | 机检＋人核 |
| T-A8 | 勘正注① A8 FM 十二枚逐枚出口 | FC-2 FM 条目纪律子检＋枚数可 grep | 十枚消费位逐枚对盘（无臂） | 机检（grep）＋人核 |
| T-A9 | 勘正注② A9 双轨验证闸执行面 | GS-1／GS-2／GS-3／GS-4／GS-5 | VA 15 条目核对面＋harness 在场（无臂） | 机检＋人核 |
| T-A10 | 勘正注④ A10 三问可答＋黑名单在场 | ST-5（coverage-audit 三问字段） | 黑名单行在场非空（无臂） | 机检（grep）＋人核 |
| T-A11 | 勘正注⑤ A11 新鲜度正面义务 | 无（EG-6 明写非门槛不入门禁） | 读数行照产在场性 | 机检（grep） |

覆盖盘点（读数口径＝products/ 根直接条目＋products/pending/ 一层条目枚枚举＝30 条目基面）：EG-6 节头 30/30·黑名单行 30/30·新鲜度读数行 30/30·技法条目数行 25/30·决策三轴行 7/30（＝效用维已验七枚子集·EG-6「不追溯已验七枚」在册口径）。

### T-A1 结构机检基线全绿（A1）

- 被测对象＝`agent-skills/fuxi-skill/gates/assert-tool.py`（runner 本体）＋`agent-skills/fuxi-skill/gates/assertion-catalog.md`（编号闭集声明面）。
    python agent-skills/fuxi-skill/gates/assert-tool.py
    python agent-skills/fuxi-skill/gates/assert-tool.py selftest
    grep -c "^### " agent-skills/fuxi-skill/gates/assertion-catalog.md
- 通过判据＝第一条末行 `汇总 PASS=27 FAIL=0 PENDING_STAGE=0 总数=27` 且 exit 0；第二条末行 `selftest 用例 164／反常 0` 且 exit 0；第三条 ≡ 27（三值随收口回执登记）。
- 与既有断言衔接注＝**复用**（27 断言＝A1 口径判据本体，本文档零新增判据面）；PENDING 不算 fail 不算 pass·汇总单列·禁假绿三态语义真源＝断言目录头注逐字。

### T-A2 契约与规范闭集存续（A2）

- 被测对象＝三契约节闭集声明面 `agent-skills/fuxi-skill/contracts/evidence-grading.md`／`agent-skills/fuxi-skill/contracts/failure-modes.md`／`agent-skills/fuxi-skill/contracts/artifact-contract.md`＋`agent-skills/fuxi-skill/specs/` 两规范表。
    grep -c "^## EG-" agent-skills/fuxi-skill/contracts/evidence-grading.md
    grep -c "^## FM-" agent-skills/fuxi-skill/contracts/failure-modes.md
    grep -c "^## AC-" agent-skills/fuxi-skill/contracts/artifact-contract.md
    python agent-skills/fuxi-skill/gates/assert-tool.py | grep -c "^FC-2 PASS"
- 通过判据＝三契约节数 ≡ 6／5／5；第四条 ≡ 1（FC-2 读数行「注册表 41 字段·双向 diff=∅」在册）。
- 与既有断言衔接注＝**复用** ST-1／ST-2／FC-1／FC-2／ST-8；**补位**＝三契约节数人核对盘面（断言侧 diff 已咬多节缺节改名，本节只登数供对账）。

### T-A3 入场资格轴出口口径（A3）

- 被测对象＝EG-6 门槛族白纸值面 `agent-skills/fuxi-skill/contracts/evidence-grading.md` EG-6 节＋产物条目 registration.md `语料门槛登记（EG-6）` 节（30 条目基面）。
    grep -c "一手占比门槛.＝70" agent-skills/fuxi-skill/contracts/evidence-grading.md
    grep -c "贴线带脱离线.＝80" agent-skills/fuxi-skill/contracts/evidence-grading.md
    grep -c "一手条目数门槛.＝5" agent-skills/fuxi-skill/contracts/evidence-grading.md
    grep -c "补充调研重触发上限.＝3" agent-skills/fuxi-skill/contracts/evidence-grading.md
    grep -c "技法条目数门槛.＝5" agent-skills/fuxi-skill/contracts/evidence-grading.md
    grep -l "语料门槛登记（EG-6）" agent-skills/fuxi-skill/products/*/registration.md agent-skills/fuxi-skill/products/pending/*/registration.md | wc -l
    grep -l "语料黑名单" agent-skills/fuxi-skill/products/*/registration.md agent-skills/fuxi-skill/products/pending/*/registration.md | wc -l
- 通过判据＝五值 grep 各 ≡ 1；EG-6 节头 ≡ 30（＝30/30 全在场·ST-9 四节节闭集兜底）；黑名单行 ≡ 30（EG-6 在场性判据·不设状态字段）。读数行**值对账**（registration 内读数行的门槛值与契约白纸逐字核对、贴线带/薄面触发与登记一致）＝人工三态判定：逐条目判 `满足`／`不满足`／`未验`（抽样面＝active 池四枚全核＋pending 池抽查 ≥5 枚含 jay-adelson-perspective 暂缓态一枚）。人工读数对账判界成文（rev-1·产品 Y-1）＝active 全核＋pending 抽样 ≥5（合计 9/30 抽样面）；30 条目全体面逐字值对账非本条目判绿前置（全体面补机器对账臂＝候选池另票口径）；判绿时「已核」（active 四枚）／「抽样核」（pending 抽查枚）两态分立可读登记。
- 与既有断言衔接注＝**复用** ST-9（四节节闭集＝容器在检）／ST-10（六路声明↔落盘）；**补位**＝门槛读数对契约面值逐字核对无机器臂（EG-6 门槛族只注册字段名不嵌值先例）——本节即唯一对盘面；新鲜度读数不入本条目出口式（A3 否定面＋T-A11 正面面分立）。

### T-A4 效用轴出口口径（A4）

- 被测对象＝EG-6 数值达标线条款白纸面＋已验七枚子集 registration 三轴读数行（样枚＝`agent-skills/fuxi-skill/products/pending/andrej-karpathy-perspective/registration.md`）。
    grep -c "计数对 4/5" agent-skills/fuxi-skill/contracts/evidence-grading.md
    grep -c "0.75, 0.90" agent-skills/fuxi-skill/contracts/evidence-grading.md
    grep -c "决策生成胜率.＝数值" agent-skills/fuxi-skill/products/pending/andrej-karpathy-perspective/registration.md
    grep -c "决策生成相似度.＝数值" agent-skills/fuxi-skill/products/pending/andrej-karpathy-perspective/registration.md
    grep -l "决策对照可分性" agent-skills/fuxi-skill/products/*/registration.md agent-skills/fuxi-skill/products/pending/*/registration.md | wc -l
- 通过判据＝契约两条定线 grep 各 ≡ 1；样枚胜率/相似度读数行各 ≡ 1；三轴读数行在场条目数 ≡ 7（＝效用维已验七枚子集·不追溯已验七枚口径＝EG-6 定线④在册）。**数值达线判定**（4/5 计数对分子、相似度落带 [0.75, 0.90]、可分三态）＝人工三态判定 `满足`／`不满足`／`未验`——EG-6 白纸「零新设机器数值断言·线值不落代码嵌值」＝禁为本条目新增机器断言（新增＝另票）。四类机械读数（对盘件在场／计数对相等／逐题成对／时戳先后）按 EG-6 验收工序读数形态条款逐条对盘登记。
- 与既有断言衔接注＝**不重叠**（效用轴＝断言体系设计态空白面，本文档＝唯一推导对盘面）；assert 注册面只登记字段名零嵌值＝本条目与 27 断言无共用判据臂。

### T-A5 验收档位口径（A5）

- 被测对象＝档位口径两逐字源（仓根 .collab/decisions/2026-11-12-皮总裁定-FUXI-P3补课六项全按建议批.md 与 agent-skills/fuxi-skill/.collab/tickets/2026-11-12-FUXI-FX-U44-P3补课批首票介质阻断型五枚加低信息量一枚补研批次票-v1.md）＋出口可核对交付面锚（registration EG-6 节内 `技法条目数` 读数行）。
    grep -c "档二起步＋档三只给补料达标的件开" .collab/decisions/2026-11-12-皮总裁定-FUXI-P3补课六项全按建议批.md
    grep -c "档三（C2/C3 验收工序）只对补料达标件开" agent-skills/fuxi-skill/.collab/tickets/2026-11-12-FUXI-FX-U44-P3补课批首票介质阻断型五枚加低信息量一枚补研批次票-v1.md
    grep -l "技法条目数" agent-skills/fuxi-skill/products/*/registration.md agent-skills/fuxi-skill/products/pending/*/registration.md | wc -l
- 通过判据＝两条逐字串各 ≡ 1（口径件 §七 勘正注⑧ 修正后形制＝两段各自对盘〔拼接〕口径同源）；技法条目数读数行在场 ≡ 25（30 条目基面·口径随注＝grep -l 命中条目数）；档二出口对盘（`技法条目数` 读数行对契约面值 5 逐字）＝人工三态 `满足`／`不满足`／`未验`；**档三出口（C2/C3 三件套）＝`未验` 态登记**（档三验收批执行席位口径重审在册候补池＝候排＝非本档位测试射程，在场性判据＝过程域取证件三件面只登记不装配）。
- 与既有断言衔接注＝**不重叠**（档位口径＝票面声明＋过程取证件面，27 断言无对应项）；票面 grep 先例口径（A5 原核对面保留过程域面）承 §六 登记。

### T-A6 失败与暂缓语义三态全可判（A6）

- 被测对象＝`agent-skills/fuxi-skill/contracts/failure-modes.md`（处置词表闭集行）＋暂缓两件套（agent-skills/fuxi-skill/products/pending/jay-adelson-perspective/registration.md 去向行＋agent-skills/fuxi-skill/.collab/receipts/2026-11-12-FUXI-FX-U44-jay-adelson暂缓入池候裁报告-v1.md）＋`agent-skills/fuxi-skill/rejected/README.md`（出清留档侧只读）。
    grep -c "降级.／.阻断.／.转人工闸" agent-skills/fuxi-skill/contracts/failure-modes.md
    grep -c "去向行＝暂缓入池" agent-skills/fuxi-skill/products/pending/jay-adelson-perspective/registration.md
    ls agent-skills/fuxi-skill/.collab/receipts/ | grep -c "暂缓入池候裁报告"
    grep -c "本轮改动.*人工闸结论" agent-skills/fuxi-skill/contracts/artifact-contract.md
- 通过判据＝处置词表行 ≡ 1（三态词表闭集在册）；jay 去向行 ≡ 1；候裁报告件 ≡ 1 枚（暂缓成立判据两件套＝去向行＋报告件 在场性机械坐实）；第四条 ≡ 1＝看板「人工闸结论」栏对盘（rev-1·产品 Y-2 补行＝口径 A6 点名第三核对面 AC-5 三栏契约在场 grep：三栏标题名闭集行「本轮改动／触发的坏信号／人工闸结论」逐字对 artifact-contract AC-5 节；该栏人裁处置语义＝人工三态对盘＝记录件非控制器条款辖内）。双禁（禁自动出清禁自动入池）／暂缓≠出清／受限路径随撤条件三处语义＝人工三态对盘（对 FM-S-01 处置列与 EG-6 三限条款逐字核）。
- 与既有断言衔接注＝**复用** FC-2 FM 条目纪律子检查（五元组非空＋处置列措辞扫描＋轨别匹配）；**补位**＝暂缓两件套在场性无机器臂（过程域记录件不在产物扫描面）＝本节文档层补位。

### T-A7 产物池验收口径（A7）

- 被测对象＝`agent-skills/fuxi-skill/products/README.md`（入池前置＋四字段格式）＋active 池四条目 confirmation.md（david-fincher-perspective／elements-of-style-technique／miyazaki-hayao-perspective／mrbeast-perspective）。
    python agent-skills/fuxi-skill/gates/assert-tool.py | grep -c "^FC-6 PASS"
    grep -c "产物id" agent-skills/fuxi-skill/products/david-fincher-perspective/confirmation.md
- 通过判据＝第一条 ≡ 1（FC-6 读数行「active 池条目 4·无人工确认来源条目数=0」在册＝验收判据该计数＝0 的机读消费位）；第二条 ≡ 1（样枚四字段机读块在场）；**四字段逐枚人核**（`产物id`／`人工确认引用`／`提案件引用`／`版本审计引用` 在场非空＋`产物id` 与目录名逐字全等）＝人工三态 4/4 枚 `满足` 方可判绿；读数口径三态分立（规程级绿／产物级实证／环境不可得未验）照 products/README §二 逐字对盘。
- 与既有断言衔接注＝**复用** FC-6；**补位**＝无（确认引用行四字段 FC-6 机读侧已咬缺字段空字段 id 不符＝selftest 配对族在册）。

### T-A8 FM 十二枚逐枚出口验收（A8·勘正注①）

- 被测对象＝`agent-skills/fuxi-skill/contracts/failure-modes.md`（条目表全 12 枚）＋十枚消费位交付面（对盘面逐枚点名：FM-S-02→断言目录 FC-3 条目面；FM-S-04／FM-M-03→`agent-skills/fuxi-skill/gates/validator-catalog.md`；FM-M-02→`agent-skills/fuxi-skill/specs/technique-spec.md`；FM-P-01→EG-2 硬规则＋abstain_tier 注册位；余枚按口径件 §六 勘正注① 表逐枚）。
    grep -c "^| FM-" agent-skills/fuxi-skill/contracts/failure-modes.md
    grep -c "^| FM-S-" agent-skills/fuxi-skill/contracts/failure-modes.md
    grep -c "^| FM-P-" agent-skills/fuxi-skill/contracts/failure-modes.md
    grep -c "^| FM-M-" agent-skills/fuxi-skill/contracts/failure-modes.md
    grep -c "FM-M-02" agent-skills/fuxi-skill/specs/technique-spec.md
    grep -c "FM-P-04" agent-skills/fuxi-skill/gates/validator-catalog.md
- 通过判据＝枚数 ≡ 12（分轨 5／4／3 对 FM-3／FM-4／FM-5 三节基线行逐字全咬）；两枚消费位对盘 grep 各 ≡ 1；**十枚逐枚出口判定**（触发→检出列读数形态可执行→处置命中三态词表闭集）＝人工三态逐枚 `满足`／`不满足`／`未验`（判定＝口径件 §六 勘正注① 表逐枚对盘，禁愿景句）。
- 与既有断言衔接注＝**复用** FC-2 FM 条目纪律子检（五元组＋轨别前缀匹配＋处置列不确定措辞扫描）＋selftest「FM 条目纪律咬放」配对族；**补位**＝十枚消费位逐枚对盘无机器臂＝文档层补位（本票不新增断言＝新增另票）。

### T-A9 双轨验证闸执行面出口（A9·勘正注②）

- 被测对象＝`agent-skills/fuxi-skill/gates/validator-catalog.md`（断言目录＋字段注册表＋阈值预注册表）＋`agent-skills/fuxi-skill/gates/validator-source-anchor.py`（method 硬门）／`agent-skills/fuxi-skill/gates/validator-public-anchor.py`（person 软门）＋harness 批次子目录面（agent-skills/fuxi-skill/.collab/evidence/harness/＝文件面不入 git＝在场性判据）。
    grep -c "^### VA-" agent-skills/fuxi-skill/gates/validator-catalog.md
    ls agent-skills/fuxi-skill/gates/validator-source-anchor.py agent-skills/fuxi-skill/gates/validator-public-anchor.py | wc -l
    ls agent-skills/fuxi-skill/.collab/evidence/harness/ | grep -c "^[^.]"
    python agent-skills/fuxi-skill/gates/assert-tool.py | grep -c "^GS-"
    grep -c "^### VA-X-02" agent-skills/fuxi-skill/gates/validator-catalog.md
- 通过判据＝VA 条目 ≡ 15；两 validator 脚本在场 ≡ 2；harness 批次子目录 ≡ 37（口径随注＝harness 目录直接子项枚数·文件面在场）；GS 断言输出行 ≡ 5（GS-1 person 204 条／GS-2 method 14 条／GS-3 全量 218 条不匹配 0／GS-4 元组对账／GS-5 基数 27 只增不减）；第五条 ≡ 1＝退出码闭集 0/1/2 对盘（rev-1·产品 Y-3 补行＝口径 A9 点名核对面 VA-X-02 条目节头在场 grep；闭集语义「0 无 fail 未验不拉码／1 任门禁层 fail／2 工具自身错误 fail-closed 不得吞成 0」＝人工三态对 validator-catalog VA-X-02 节逐字对盘，validator 实际拉码行为＝harness 批次执行面非本条目射程）。六要素（闸分离物理体现／method 硬门六层闭集／person 软门假绿违例语义／验证记录 20 字段同源／执行单 owner／落盘注册）＝人工三态逐条对盘 `满足`／`不满足`／`未验`。
- 与既有断言衔接注＝**复用** GS-1..GS-5（A1 机检面 GS 族现跑承接＝口径件 §六 勘正注② 核对面同源）；**补位**＝VA 目录 15 条目核对面与 harness 批次在场性无机器臂（验证记录目录＝过程域证据面不入产物扫描面）＝文档层补位。

### T-A10 EG-4 三问可答＋语料黑名单在场性出口（A10·勘正注④）

- 被测对象＝`agent-skills/fuxi-skill/contracts/evidence-grading.md` EG-4 节（三问口径）＋`agent-skills/fuxi-skill/rejected/README.md`（coverage-audit 三问字段闭集）＋rejected 批次 coverage-audit 三件＋registration 黑名单行（30 条目基面）。
    grep -c "哪些留下" agent-skills/fuxi-skill/rejected/rb1-2026-11-08/coverage-audit.md
    grep -l "哪些留下" agent-skills/fuxi-skill/rejected/*/coverage-audit.md | wc -l
    grep -l "语料黑名单" agent-skills/fuxi-skill/products/*/registration.md agent-skills/fuxi-skill/products/pending/*/registration.md | wc -l
    python agent-skills/fuxi-skill/gates/assert-tool.py | grep -c "^ST-5 PASS"
- 通过判据＝样枚三问字段 ≡ 1；三问命中审计件 ≡ 3（rejected 三批次全在场）；黑名单行在场条目 ≡ 30（EG-6 在场性判据·非空＝人工三态逐枚抽查 `满足`／`不满足`／`未验` 抽样 ≥5 枚）；ST-5 输出行 ≡ 1。三问口径（双轴字段＋control_arm＋leakage_check 缺任一＝不可答）＝人工三态对 EG-4 三字段逐条对盘。
- 与既有断言衔接注＝**复用** ST-5（rejected 可枚举＋coverage-audit 三问字段）；**补位**＝黑名单行在场非空无机器臂（registration EG-6 节内容值侧无检臂·ST-9 只咬节结构）＝文档层补位。

### T-A11 新鲜度正面义务出口（A11·勘正注⑤）

- 被测对象＝EG-6 新鲜度条款正面义务白纸面＋registration 新鲜度读数行（30 条目基面）＋实例枚 `agent-skills/fuxi-skill/products/david-fincher-perspective/registration.md`。
    grep -c "新鲜度非门槛" agent-skills/fuxi-skill/contracts/evidence-grading.md
    grep -l "新鲜度窗口读数" agent-skills/fuxi-skill/products/*/registration.md agent-skills/fuxi-skill/products/pending/*/registration.md | wc -l
    grep -c "落窗口内条目=" agent-skills/fuxi-skill/products/david-fincher-perspective/registration.md
- 通过判据＝契约否定面条款 grep ≡ 1（非门槛不入出口式＝A3 否定面不因本条改动）；读数行在场条目 ≡ 30（30/30 照产义务＝EG-6「读数照登照产」正面义务机械在场判据）；样枚比值式读数行 ≡ 1（登记形态＝「落窗口内条目数/要素条目总数」比值式对 EG-6 逐字）。
- 与既有断言衔接注＝**不重叠**（新鲜度＝EG-6 白纸非门槛·不作门禁判据·27 断言零对应臂＝本条目＝纯文档层补位唯一对盘面）。

## 六、执行序与总判定（收口面）

1. 执行序＝T-A1 → T-A2 → T-A7 → T-A9（机检主干先跑＝门禁四读数基面）→ T-A3／T-A4／T-A5／T-A6／T-A8／T-A10／T-A11（补位面）；全部机检命令读数逐条登记收口回执。
2. 总判定闭集＝十一条目全 `满足` → 验收通过；任一条目 `不满足` → 整体验收不过＋缺陷件呈报；任一条目 `未验` → 整体验收判「带未验项通过」须人类闸确认（禁凑绿·承三态登记纪律）。
3. 本档零机器断言＝断言基数 27 存续判据随收口复跑（assert 汇总 PASS=27 FAIL=0 PENDING_STAGE=0 总数=27 exit 0 必全等）。
