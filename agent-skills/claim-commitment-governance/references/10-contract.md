# 10-contract · 主张—来源—责任—验证—外发契约

> 本文件是主张行字段、验证登记、来源层判定、相容矩阵、状态语义、人工闸、禁止自决、词表与抽取模式的**唯一真源**。
> 复制口径：字段闭集、矩阵、状态语义硬规则、词表、抽取模式、人工闸七类、禁止自决八条的**正文不得复制**到其他 references；`30-gates` 的判据行可复述其所判的**判定条件**，但须标 `→ §N.M` 指向本文件小节，且被引编号必须存在于对应小节内。
>
> **摘要复述的唯一例外与其绑定（治红4-05 的自洽冲突）**：`SKILL.md` 的「契约总则」10 条是本文件正文的**摘要复述**（供主文件自足），属上述禁令的**明示例外**；其成立条件是被双向绑定——每条总则须逐字含本文件对应真源的关键子串，任一处改义即判违例（`c27`）。除该节外，本文件正文不得以任何形式复制到 `references/` 或 `templates/`。

## 1. 主张行登记面（表 A）：必填 17 ＋ 条件必填 3 ＝ 20 列

| 分组 | 字段 | 闭集／格式 | 必填性 |
|---|---|---|---|
| 身份 | `claim_id` | `C-[0-9]{3,}`；同一主张跨件复用同一 ID | 必填 |
| 身份 | `claim` | 一句一主张，不得复合 | 必填 |
| 身份 | `claim_type` | `fact` / `requirement` / `commitment` / `assumption` / `authorization` / `measurement` / `risk` | 必填 |
| 来源 | `source_layer` | `legal_regulatory` / `contractual` / `approved_baseline` / `customer_request` / `technical_design` / `internal_assumption` | 必填 |
| 来源 | `evidence_tag` | `FACT` / `INFERENCE` / `JUDGMENT` / `UNKNOWN` / `STALE` | 必填 |
| 来源 | `authority` | `binding` / `consultative` / `internal_only` / `unverified` | 必填 |
| 状态与效力 | `status` | `draft` / `accepted` / `frozen_assumption` / `external_pending` / `external_confirmed` / `superseded` / `rejected` | 必填 |
| 状态与效力 | `external_effect` | `none` / `internal_only` / `outbound_pending` / `outbound_authorized` | 必填 |
| 责任 | `requestee` | `<role-kind>:<ref>` 或 `none`；`role-kind` ∈ `human` / `seat` / `org` | 必填 |
| 责任 | `accountable_party` | 同上格式，交付与执行责任主体 | 必填 |
| 责任 | `decision_owner` | 同上格式，决策与批准主体 | 必填 |
| 责任 | `responsibility_basis` | `source:<PREFIX>-<digits>` / `authorization:<PREFIX>-<digits>` / `none`，或 `<自由描述>`（**该行 `authority` 必须为 `unverified`**） | 必填 |
| 生成与批准 | `generated_by` | `<generator-kind>:<ref>`；`generator-kind` ∈ `human` / `seat` / `system` | 必填 |
| 生成与批准 | `approver` | `<approver-kind>:<ref>` 或 `none`；`approver-kind` ∈ `human` / `seat` / `system` | 必填 |
| 时效 | `expiry` | `YYYY-MM-DD` 或 `none`；兼作批准有效期（同一主张的有效性与批准有效性同轴） | 必填 |
| 引用 | `linked_artifacts` | `<kind>:<value>` 列表，以 `;` 分隔；`kind` ∈ `source` / `cite` / `artifact` / `authorization` | 必填 |
| 可比对 | `assertion_form` | `qualitative` / `quantity` / `datetime` / `identifier` / `completeness` | 必填 |
| 可比对 | `comparability_ref` | `CMP-[0-9]{3,}` 或 `none`；`assertion_form ≠ qualitative` 时禁 `none` | 条件必填 |
| 主张时效 | `review_owner` | `<role-kind>:<ref>`；`status = frozen_assumption` 时禁 `none` | 条件必填 |
| 主张时效 | `reopen_trigger` | 一句可判的重开条件；`status = frozen_assumption` 时禁 `none` | 条件必填 |

**引用形态**：`source:` 后接 `INTK` / `RES` / `MSR` / `DOC` 前缀编号；`cite:` 后接同一前缀编号再跟 `#` 与条款位置或日期；`artifact:` 后接 `TKT` / `RCP` / `PRD` / `QAV` / `DLV` / `OUT` / `REQ` / `CMP` 前缀编号；`authorization:` 后接 `AUTH` / `DEC` 前缀编号。

**来源载体边界**：`INTK` 前缀只证明「该输入件来自何处、摘要为何」，不证明其内容为 `FACT`，也不证明其具 `binding` 权威。任何 `FACT` 或 `binding` 的成立须另行满足第 2 节相容矩阵与第 7 节硬规则。

**责任主体边界**：`requestee` 是请求对象，不得单独充当 `accountable_party`；`source_layer` ∈ 1–4 层（法定／合同／批准基线／客户书面要求）时，`accountable_party` 不得为 `none` 且 `responsibility_basis` 必须非 `none`，即责任主体必须挂来源或授权依据；第 5／6 层（`technical_design`／`internal_assumption`）**允许** `accountable_party = none`，但聚合与判词须单列「无责任主体主张」，**不得以硬编填充替代**——无依据时宁可空着并如实计入该类，不得写一个凑数的主体。

**字段裁撤记录**：主张行不设 `source_kind`（与 `source_layer` 语义重叠，R1–R17 中无判据消费其取值，已删）；不设 `approval_scope`（授权范围由 `authorization:` 所指 `DEC` 条目承载，本列无语义判据，已删）；不设 `verification_ref`（验证块以 `claim_id` 为主键挂在表 D，主张行无需再挂指针）。逐字段消费方对照见票面 §0.4。

## 2. 来源层判定序与相容矩阵

**来源层判定序（按序取首个命中，不得跳序）**：

1. 该主张的法定或监管依据可指认到外部强制规则 → `legal_regulatory`。
2. 该主张的约束来自已签署合同的条款 → `contractual`。
3. 该主张来自经批准并生效的基线件 → `approved_baseline`。
4. 该主张来自客户书面提出的要求 → `customer_request`。
5. 该主张来自本方技术设计决定 → `technical_design`。
6. 以上均不成立 → `internal_assumption`。

**判定序的落格要求**：判定为 1–4 层的，`responsibility_basis` 必须非 `none` 且指向可解析的 `source:` 或 `authorization:` 引用；1–4 层而无书面载体（如仅口头新要求）**不得**落入该层，按第 6 步归 `internal_assumption`，并在 `claim` 内注明「未成文」。

**第 2 步落格的取证方式（`contractual` 专用，治「附件是否随合同签署」无字段可证）**：技术要求写在合同附件里、而「该附件是否随合同签署」这一事实**在本契约字段面内无取证字段**（与 `N9` 同类）。故 `contractual` 落格前须由人类确认附件与合同的签署关系，结论记入 QA 判词，承接方式同 `30-gates §4` 的 `A1`／`A2`；无该确认的，一律**不得**落 `contractual`，按第 6 步归 `internal_assumption` 并在 `claim` 内注明「附件与合同的签署关系未确认」。

**多源拆条（治第 5 步不可达）**：一条主张若同时有多份书面载体指向不同来源层（例如既有客户书面要求、又有本方技术设计决定），**必须按层拆为多条主张各落一层**，不得用「按序取首个命中」把后者吞掉。`source_layer` 一行只记一层；第 5 步 `technical_design` 的可达性由此保证。拆条后各条共用同一 `linked_artifacts` 子集与同一 `original_requirement_ref`，责任主体可不同。

| `source_layer` | `binding` | `consultative` | `internal_only` | `unverified` |
|---|---|---|---|---|
| `legal_regulatory` | 条件 | 允许 | 禁止 | 允许 |
| `contractual` | 条件 | 允许 | 禁止 | 允许 |
| `approved_baseline` | 条件 | 允许 | 禁止 | 允许 |
| `customer_request` | 条件 | 允许 | 允许 | 允许 |
| `technical_design` | 禁止 | 禁止 | 允许 | 允许 |
| `internal_assumption` | 禁止 | 禁止 | 允许 | 允许 |

**「条件」的判据**：`approver` 形如 `human:<ref>`，且 `status` ∈ `accepted` / `external_pending` / `external_confirmed`，且 `expiry ≠ none`；`legal_regulatory` 与 `contractual` 另须 `linked_artifacts` 含至少一条 `cite:` 引用。

**四件套承接条款（本包只登记承接点，不复写正文）**：外部引用四件套（文件名／日期／条款位置／可访问 URL）的正文由 `bundle:external-advisor-collab` 的「谁主张谁举证」条款承担，不在本文件复写；本包只在上一段的「条件」判据处**消费**其结论，即要求 `cite:` 引用存在且可解析。跨包规范一律以「包名 ＋ 条款名」引用，本文件不写任何跨包路径，也不重复四件套的四项要素清单。

**未在矩阵中出现的组合一律判违例**，不做默认放行。

## 3. 主张级验证登记（表 D）

验证块是**主张级**的：每条主张在表 D 有且仅有一行，主键 `claim_id`。表 D 是验证面的唯一登记处，主张行不重复承载验证字段。

| 字段 | 闭集／格式 | 填写归属 | 必填性 |
|---|---|---|---|
| `claim_id` | `C-[0-9]{3,}`；须在表 A 已登记 | 生产者 | 必填 |
| `original_requirement_ref` | `REQ-[0-9]{3,}` 或 `none`；指向表 C 的 REQ 行 | 需求侧 | 必填 |
| `required_environment` | `mock` / `test` / `integration` / `production` / `none` | 需求侧；生产者照录，QA 不得回写 | 必填 |
| `required_checks` | `functional` / `security` / `performance` / `compliance` / `robustness` 的子集，以 `;` 分隔，或 `none` | 同上；集合语义，非全序 | 必填 |
| `required_change_record` | `none`，或 `<原值>→<新值>@<approver>`；`<approver>` 须与本行 `approver` 同值 | 需求或生产者变更要求时 | 必填 |
| `actual_environment` | 同四值，另允许 `unverified` | 只由 QA 填 | 必填 |
| `actual_checks` | 同五值集合的子集，以 `;` 分隔，或 `none` | 只由 QA 填 | 必填 |
| `qa_result` | `pending` / `passed_at_actual` / `passed_with_exemption` / `failed` / `blocked` | 只由 QA 填 | 必填 |
| `exemption` | `none` / `partial` / `full` | 生产者申请、人类批准 | 必填 |
| `reason` | 一句可判理由 | `exemption ≠ none` 时 | 条件必填 |
| `scope` | 受限面描述 | `exemption ≠ none` 时 | 条件必填 |
| `fallback_criterion` | 一句可判的回退判据 | `exemption ≠ none` 时 | 条件必填 |
| `reopen_trigger` | 一句可判的重开条件 | `exemption ≠ none` 时 | 条件必填 |

**环境轴序位（全序，唯一参与大小比较的轴）**：`mock` = 1 ＜ `test` = 2 ＜ `integration` = 3 ＜ `production` = 4。`unverified` 不参与比较，出现即视为未达任何要求环境；`none` 表示未提出要求，不参与比较。

**检查轴（集合，不排序）**：`required_checks` 与 `actual_checks` 按集合包含关系判定，不做大小比较。

**同名双面字段**：`reopen_trigger` 在表 A（主张冻结的重开条件）与表 D（降级的重开条件）各有一面；同一 `claim_id` 两面均非 `none` 时必须同值（见 `30-gates` `R5` 第五支）。

## 4. 可比对断言（表 B）与受限抽取模式

**可比对断言登记表（表 B）列**：`cmp_id` / `cmp_key` / `cmp_kind` / `cmp_value` / `completeness_mode` / `enumeration_count` / `remaining_count` / `claim_id` / `source_artifact`。

- 表 B 是**可比对断言行**的唯一登记处。**「唯一」指表只有一处**，不是「每个键只有一行」：同一 `cmp_key` 可以有多行，各行的 `source_artifact` 指名该数值由哪份工件给出；同键多行即构成跨件比对点（见 `30-gates` `R11`）。
- `cmp_id` 格式 `CMP-[0-9]{3,}`；`cmp_kind` ∈ `quantity` / `datetime` / `identifier` / `completeness`，须与所引主张的 `assertion_form` 相同。
- `cmp_key` 是「同一可识别对象」的键；**触发比对以 `cmp_key` 相等为条件，不以任何可选字段是否填写为条件**。
- `cmp_value` 是该对象的取值：数量为数值；时点为 `YYYY-MM-DD` 或 `YYYY-MM-DDThh:mm`；标识为被引编号；完备性为 `resolved`。
- `identifier` 类断言的 `cmp_value` 必须在**标识与需求主表（表 C）**已登记，且其 `definition_ref` 非 `none`。
- `completeness` 类断言必须填 `completeness_mode` ∈ `cleared` / `partial`，且 `enumeration_count` ＞ 0；`cleared` 时 `remaining_count` 必须 ＝ 0，`partial` 时 `remaining_count` 必须 ＞ 0。其他 `cmp_kind` 三列均写 `none`。

**受限抽取模式（闭集，语境化：先有断言引导词，再有数值或时点）**

| 类 | 模式（正则片段） |
|---|---|
| 数量（阿拉伯） | `(剩余\|还剩\|还缺\|缺口\|共\|合计\|总计\|已\|待\|完成\|核销)\s*[0-9]+(\.[0-9]+)?\s*(人日\|人\|天\|小时\|分钟\|次\|个\|条\|项\|处\|万元\|元\|%)` |
| 数量（中文） | `(剩余\|还剩\|还缺\|缺口\|共\|合计\|总计\|已\|待\|完成\|核销)\s*[一二三四五六七八九十百千万两]+\s*(人日\|人\|天\|小时\|分钟\|次\|个\|条\|项\|处\|万元\|元\|成\|倍)` |
| 时点 | `(于\|截至\|截止\|止于\|完成于\|清零于\|定于\|在)\s*(20[0-9]{2}-[0-9]{2}-[0-9]{2}\|[0-9]{1,2}月[0-9]{1,2}日)` |
| 完备性 | `(清零\|一条不剩\|无遗漏\|核销完毕\|关闭完毕\|验收完毕)\s*(于\|之日\|为止\|完成)` |

**收窄依据（口径变更，取代上一版的裸量词触发）**：上一版把 `全部` / `所有` / `一律` / `均已` / `全覆盖` 作为完备性触发词，这些词在纪律性文本里高频出现（本文件自身就有三处），会把普通工作票系统性误判为完备性断言并逼出假计数。本版改为**引导词＋数值或时点**的语境化模式，裸量词不再触发；`c20` 用四例普通工作票正样本与四例真断言正样本双向实跑固定这一收窄。

**标识类不做抽取兜底**：标识形态（线号、表号、条目号）与治理语汇大量重名，正则抽取误报高于漏报代价；其覆盖改由「申报 `assertion_form=identifier` 即强制入表 ＋ 表 C 可解析」承担。

**标识与需求主表（表 C）列**：`id_key` / `id_value` / `definition_ref` / `status` / `req_required_environment` / `req_required_checks` / `req_enumeration_base`。

- 表 C 同时承担两件事：**标识定义**（`id_key`／`id_value`／`definition_ref`／`status`）与 **原始需求的要求面**（`req_*` 三列）。二者共用一张表是因为 REQ 条目本身就是一种标识；分两张表会产生两处 `REQ-` 编号真源。
- `id_value` 是编号本体，`REQ-` 起头的行即「原始需求条目」；`id_key` 是分类键，且**`id_value` 以 `REQ-` 起头的行其 `id_key` 必须为 `需求`，非 `REQ-` 起头的行其 `id_key` 不得为 `需求`**——需求条目只认这一种识别口径，不得另立第二口径。
- `status` ∈ `defined` / `draft` / `retired`；`status ≠ defined` 的 `id_value` 不得被任何主张引用。
- `req_required_environment` ∈ 环境轴四值或 `none`；`req_required_checks` ∈ 检查轴五值子集（以 `;` 分隔）或 `none`；`req_enumeration_base` 为非负整数或 `none`（该需求的原始枚举基数）。
- 非 `REQ-` 行的三列 `req_*` 一律写 `none`。

## 5. 强断言词表与占位词表

| 类别 | 闭集 |
|---|---|
| 强断言 | `必须` / `一律` / `全部` / `绝不` / `保证` / `确保` / `均已` / `全覆盖` |
| 占位词 | `待定` / `暂定` / `待补` / `TBD` / `TODO` / `待确认` / `placeholder` / `〔` |

**两表分工（治重叠）**：强断言词表只用于「外发件禁语检测」与「占位检测」，不参与断言形态判定；完备性抽取模式（第 4 节）与强断言词表不共享任何触发词。`〔` 是模板填空标记；外发件在 `send_channel=approved_send` 时不得残留任一占位词或任一未替换的 `〔`。

## 6. 外发门

| 字段 | 闭集／格式 |
|---|---|
| `outbound_type` | `clarification_request` / `commitment` / `acceptance` / `risk_notice` / `report` |
| `claims` | 本件引用主张的 `claim_id` 闭集列表；允许是主登记表的真子集，不得含未登记或 `superseded` 的 ID |
| `fact_review` | `<结论>@<reviewer>`；`reviewer` 不得等于 `generated_by` |
| `commitment_review` | 同上；`reviewer` 不得等于 `generated_by`，且不得与 `fact_review` 的 `reviewer` 相同 |
| `authorization` | `human:<ref>`；无人类授权不得写 |
| `send_channel` | `draft_only` / `approved_send` |

`send_channel=approved_send` 只表示人类已授权发送，不表示系统执行发送；实际发送动作在系统外，由人类执行。

## 7. 状态语义硬规则

1. `accepted` 不等于 `external_confirmed`；内部接受不得写成外部确认。
2. `frozen_assumption` 只限内部：`expiry`、`review_owner`、`reopen_trigger` 三者均不得为 `none`，`expiry=none` 直接判违例；不得外溢为默认认可。
3. `external_pending` 超时只触发复核与升级，不自动变为 `external_confirmed`。
4. `external_effect=outbound_authorized` 只能由人类闸设置。
5. `superseded` 保留旧行，不删除、不改写；被 `superseded` 的主张不得再被任何工件引用。
6. QA 按 `actual_environment` / `actual_checks` 判定通过，不回写 `required_environment` / `required_checks`。
7. `evidence_tag` 为 `UNKNOWN` 或 `STALE` 时，`status` 不得为 `accepted`，`authority` 不得为 `binding`，`external_effect` 不得为 `outbound_authorized`。

## 8. 人工闸七类（唯一真源）

以下七类事项必须人类拍板，机器与席位均不得代判：

1. 外部权威来源的确认。
2. 外发授权。
3. 需求降级或豁免的批准。
4. 范围或验收口径的变更。
5. 法律、合同或责任解释。
6. 外发动作本身。
7. 是否将沉默视为认可；默认一律不算。

## 9. 禁止工具自决八条

1. 不得从文本自行推断权威性。
2. 不得把 `UNKNOWN` 或 `INFERENCE` 自动升格为 `FACT`。
3. 不得把内部冻结自动转为外部确认。
4. 不得自动降级要求环境或要求检查。
5. 不得自动发送任何外发件。
6. 不得自动生成对外承诺。
7. 不得自动判定业务事实真伪。
8. 不得自动改写历史主张状态。

## 10. deep-research 证据标签消费映射

| deep-research 标签 | 本契约 `evidence_tag` |
|---|---|
| `FACT` | `FACT` |
| `INFERENCE` | `INFERENCE` |
| `JUDGMENT` | `JUDGMENT` |
| `UNKNOWN` | `UNKNOWN` |
| `STALE` | `STALE` |

本技能只消费 `bundle:deep-research` 的证据标签与来源池，不重做检索，不把研究结论升格为承诺。标签本体与措辞分级以 `bundle:deep-research` 包 `SKILL.md §六 证据纪律` 的「标签闭集（五标·英文）」（`:61`）与「措辞分级」（`:63`）为真源，细则见同包 `methodology.md:52`；**两者都不在该包的笔记格式细则文件**——v4 那句同时写错了**文件名**与**条款名**（文件名＋条款名双错），本版按部署件 `0.1.30`（`version: 1.0.2`）改正。语义分级本体不在本包，本文件不复写。
## 11. 编号与角色的发放主体

**本技能不自产编号，也不自产角色位号**：本文件出现的 `C-`／`CMP-`／`REQ-`／`INTK-`／`RES-`／`MSR-`／`DOC-`／`TKT-`／`RCP-`／`PRD-`／`QAV-`／`DLV-`／`OUT-`／`AUTH-`／`DEC-` 等编号，均由本技能之外的登记件或项目绑定层发放；本技能只**消费**其形态与可解析性，不生成、不续号、不补位。

**引用型字段五项闭集与无号写法**：

| 引用型字段 | 有编号时 | 无编号时（禁造号） |
|---|---|---|
| `source:` | 填真实编号（`INTK`／`RES`／`MSR`／`DOC` 前缀） | 填自由文本描述，并在同行 `authority` 标 `unverified` |
| `authorization:` | 填真实编号（`AUTH`／`DEC` 前缀） | 填自由文本描述（谁在何场合口头授权），并标 `unverified` |
| `linked_artifacts` | 填真实编号 | 该条不计入引用；来源面写自由文本并标 `unverified` |
| `comparability_ref` | 填真实 `CMP-` 编号 | 该主张 `assertion_form` 须为 `qualitative`；不得自造 `CMP-` 号充数 |
| `original_requirement_ref` | 填真实 `REQ-` 编号 | 填 `none`，并在 `claim` 内写明需求未成文；不得自造 `REQ-` 号 |

**角色引用两种合法形态**：有角色册时写 `<role-kind>:<ref>`（`role-kind` ∈ `human`／`seat`／`org`，`ref` 为角色册内的位号或人名）；**无角色册时**允许写 `<role-kind>:<自由描述>`，例如 `seat:需求侧接口人（未编位号）`。两种形态的共同下限：**不得留空**（空串、`—`、`无` 均判违例）；**不得编位号**（不得为不存在的角色自造编号）；**不得张冠李戴**（`human:` 之后不得填席位名，`seat:` 之后不得填人名）。

**正向可判条件（不写黑名单）**：凡某行在引用型字段或角色引用的 `<ref>` 位填了**自由描述**（即不是 `<PREFIX>-<digits>` 编号、也不是角色册内位号），该行 `authority` **必须**为 `unverified`——机器判的是「有没有如实降格证据强度」，不是「字符串像不像编号」。自由描述 ＋ `authority ∈ {binding, consultative, internal_only}` 一律判违例（`c26` 断言）。反之，未编号时填一个自造的 `PREFIX-digits` 也判违例：其前缀必须落在已登记前缀闭集内，本技能不发放前缀。

**无责任主体主张的单列口径**：`source_layer` ∈ 5–6 层且 `accountable_party = none` 的主张，在交付汇总与 QA 判词中**单列为一类**（「无责任主体主张」：条数 ＋ `claim_id` 清单 ＋ 不可归属的原因），不得摊进「未绿项」冲抵，也不得靠硬编一个主体让它消失。`decision_owner` 同理：`authority ∈ {binding, consultative}` 时不得为 `none`；`authority ∈ {internal_only, unverified}` 时允许为 `none` 并同样单列。

**格式判据的落地位置**：本节闭集与形态由闸夹具 `c26` 机检——五个引用型字段名逐字等、两句禁令（禁造号／不得留空）在位、表 A 示例行的编号前缀全部落在已登记前缀闭集内、角色三形态判定；本节正文改动即判红。
