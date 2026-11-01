# SWB-T05 专家包装配（B6 职能承载票）：席位卡装填＋变更通道装载（施工票·L3·架构席起草）

- 开端读数：ANCHOR＝08fc5ee（见总览件）；开工时实测 HEAD 附回执。
- 设计真源：`.collab/refs/external/SWB-交接件v2.4-产品设计与架构设计-2026-11-01.md`（V7；产品 L25–79 sha256=664ef6b2…；架构 L80–237 sha256=e0801956…）。
- 背景（自包含）：§9 声明「B6＝装配施工票，编号空缺刻意」——本票即 B6 职能的显式并入声明票。承接消费面声明第③项「席位卡装填←§5/§7」（V7 L223；§5 工件矩阵 V7 L133–141，§7 纪律编目 V7 L144–156）与第⑧项「变更通道←§12」（V7 L190–191）。同时装配面逐行落实 §8 专家包装配表（V7 L157–167）。违纪模式表承接：行 3「上游席位代写下游产出→红线②＋U4＋G4」的装填面在本票（席位卡纪律行）；行 8「裸纪律入卡→'无裸纪律'验收（§7）」的装填面在本票、验收断言在 T06。
- 前置票：T02、T03、T04（席位卡「脚本调用点」行必须引用三票已落盘实体名，引用不得指向缺席件）。P3 读数（T01）决定 disallowedTools 装填（见候裁 Q-06）。

## 声明闭集（13 件·本票唯一可写面）
- 声明闭集：
- software-team/plugin.json
- software-team/settings.json
- software-team/agents/software-team-lead.md
- software-team/agents/software-team-product.md
- software-team/agents/software-team-architect.md
- software-team/agents/software-team-qa.md
- software-team/agents/software-team-engineer.md
- software-team/skills/sop/SKILL.md
- software-team/skills/sop/references/architecture-v2.4-copy.md
- software-team/skills/sop/references/product-v2.4-copy.md
- software-team/skills/sop/templates/ticket-template.md
- software-team/skills/sop/templates/decision-pack-template.md
- software-team/skills/sop/templates/return-template.md

## 逐条施工规格（逐行对位 §8 表 V7 L157–167）

### T05-A plugin.json
- `name=software-team`；`expertType=team`；`teamInfo{leadAgent, memberAgents}`；members 五席（lead＋product/architect/qa/engineer）。锚 [实证: plugin-json-spec:24-26,53-57]（核验按 §19 持盘者直读，回执附核对结论行）。

### T05-B settings.json
- 键名 `"agent"`（[实证: spec-team:110-120]）。

### T05-C agents/software-team-lead.md（主理人接口卡）
- 内容闭集＝红线五条＋铁律四条摘要＋路由判定表＋脚本调用清单＋句「一切流程状态以账本为准」（§8 行2）；红线/铁律摘要锚点＝spec-team:62-66 / spec-agent:122-136（§19）。
- 路由判定表必须列五类变更通道路由（§12 V7 L190–191：C1／产品票／规则票／技能票／施工票＝L3 载体非 L2 通道）——消费面⑧的主落点。
- maxTurns＝200（§8 行7 [实证: spec-agent:21,93]）。

### T05-D 四席位卡（§5 恒常工件·消费面③落点）
- 每卡结构＝§5 行1 逐字：**身份一句＋权限四行＋席位纪律≤10 条（各带保证类别标注 G1–G5）＋脚本调用点**；「装什么/不装什么」执行：不装技法正文、流程全文。
- 权限四行源＝表2-1 对应席位行（写域/可写/不可写/载体）转录；席位纪律源＝§7 席位纪律段（V7 L155）逐席：工程师——一票一新鲜实例、回流四型、不改票体四字段；QA——判词归签字席、审计以任务实体承载；产品——解析件只引 intake、范围签两层判据；架构——租约签注唯一生产权、灰度判据不得现场裁量；主理人卡另加「零业务写、路由不做业务解析」。
- 通用纪律 U1–U7 按席位相关性入卡，**每行带主保证标注**（§7 落盘为纪律标注列）；U7 行标注逐字含「P3[未验证:P3·能力面]＋G5 辅助面」（§7 V7 L154 诚实申报，不得改写成已保证形态）。
- frontmatter 标准字段；**不声明 tools 字段**（[实证: spec-agent:5-7]）；disallowedTools 仅 P3 实测 pass 才装配（候裁 Q-06，P3 未过时四卡缺省不含该字段）。
- 成员卡 maxTurns＝50（§8 行7）。

### T05-E skills/sop/
- `SKILL.md`：按需拉取技法正文、模板、正反例；**不装纪律**（§5 行2「纪律不按需」）。
- `references/architecture-v2.4-copy.md`＋`references/product-v2.4-copy.md`：两基线整件副本（§5 行3「本架构＋产品设计副本」/§8 行5）；副本头部注来源 sha256 与源路径；验收断言副本哈希与基线登记哈希一致。
- `templates/` 三件＝票模板/决策包模板/回流件模板（§8 行5「templates＝票/决策包/回流件」）；票模板含票型七类清单与票体四字段自包含结构（§3）；回流件模板含回流四型（完成/部分完成/受阻/异常，§3）。

### T05-F 同源与引用纪律
- 席位卡脚本调用点只可引用 T02/T03/T04 声明闭集实体名（缺席引用＝红项，§16 对照源铁律）；本票不写 hooks.json（属 T04 闭集）、不写 config/*.json（属 T02/T03 闭集）。

## 验收判据（全部机械可判）
1. `python -c "import json;p=json.load(open('software-team/plugin.json'));assert p['name']=='software-team' and p['expertType']=='team'"` 退出 0；
2. `python -c "import json;s=json.load(open('software-team/settings.json'));assert 'agent' in s"` 退出 0；
3. `ls software-team/agents/*.md | wc -l` ＝5；
4. 无裸纪律断言：对五卡逐行扫描纪律条目行，每行必含 `G[1-5]` 标注——`python software-team/tests/acceptance/count-assert.py --bare-discipline` 退出 0（消费面⑦联动，本票交付时 T06 该子件未落则本判据以同式内联脚本执行，读数入回执）；
5. 副本哈希：`sha256sum software-team/skills/sop/references/architecture-v2.4-copy.md` 对位架构基线本体哈希 e0801956…（副本含来源头注行故整件哈希允许不同，断言＝头注声明哈希＝登记哈希＋去头注后体哈希逐字等；去注命令读数入回执）；product 副本同理对位 664ef6b2…；
6. `grep -c 'maxTurns' software-team/plugin.json` 等装配读数：plugin.json 内 lead maxTurns＝200、成员＝50（JSON 路径断言脚本退出 0）；
7. 四卡无 `tools:` 字段：`grep -L '^tools:' software-team/agents/software-team-{product,architect,qa,engineer}.md | wc -l` ＝4；
8. 路由判定表五通道行齐：`grep -cE 'C1|产品票|规则票|技能票|施工票' software-team/agents/software-team-lead.md` ≥5；
9. `ls software-team/skills/sop/templates/*.md | wc -l` ＝3。

## 票间关系
- 前置：T02、T03、T04。后置：T06（验收双臂对装配面全量核验）。

## 禁动面（零触碰）
- 两基线登记件本体（本票只产副本，源件一字不动）、`.collab/` 全域（回执除外）、`docs/`、T01–T04 全部声明闭集文件（hooks.json/config/scripts 均不得由本票写入或改动）。
- 工程师不得改本票票体四字段。

## 候裁点（单列·不自行拍）
- Q-01：交付根路径实例化——设计真源以专家包相对路径表述（`agents/…`、`skills/sop/…`），落盘至本仓的根（本票暂按 `software-team/` 顶层）属落盘约定，呈决策者追认。
- Q-03：`.mcp.json` 三 server（ledger/CI/签名）auth 形态按 P8 求证后填（§8 行6 [未验证:P8]）——P8 读数未出前本票**不装配 .mcp.json**，装配与否随 P8 呈拍。
- Q-06：disallowedTools 装填条件＝P3 实测 pass（§8 行3 [未验证:P3]）；P3 阴性/不定 → 不装配，席位感知备选退化走人类拍板（§14 行3）。

## 回执
落 `.collab/receipts/2026-11-01-SWB-T05-receipt.md`：开端 HEAD＋完整文件清单＋判据 1–9 实测读数＋§19 锚点直读核对结论（三份 spec 行号核对记录）。commit 单独笔，`collab:` 前缀只含本票闭集件。
