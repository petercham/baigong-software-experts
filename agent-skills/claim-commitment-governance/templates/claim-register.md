# 主张登记表

> 每个项目只有一处主张登记表：表 A 是主张的唯一登记处，表 B 是**可比对断言行**的唯一登记处，表 C 是标识与原始需求要求的唯一登记处，表 D 是**主张级验证**的唯一登记处。字段闭集与判据见 `references/10-contract.md` 与 `references/30-gates.md`。

## 表 A · 主张登记（20 列）

| claim_id | claim | claim_type | source_layer | evidence_tag | authority | status | external_effect | requestee | accountable_party | decision_owner | responsibility_basis | generated_by | approver | expiry | linked_artifacts | assertion_form | comparability_ref | review_owner | reopen_trigger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | 示例主张须一句一断 | fact | customer_request | INFERENCE | consultative | draft | none | org:requesting-unit | org:delivery-unit | seat:decision-seat | authorization:DEC-001 | seat:authoring-seat | none | none | source:DOC-001;artifact:TKT-001 | completeness | CMP-001 | none | none |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## 表 B · 可比对断言登记（9 列）

| cmp_id | cmp_key | cmp_kind | cmp_value | completeness_mode | enumeration_count | remaining_count | claim_id | source_artifact |
|---|---|---|---|---|---|---|---|---|
| CMP-001 | 示例对象键 | completeness | resolved | cleared | 12 | 0 | C-001 | artifact:QAV-001 |
|  |  |  |  |  |  |  |  |  |

## 表 C · 标识与需求主表登记（7 列）

| id_key | id_value | definition_ref | status | req_required_environment | req_required_checks | req_enumeration_base |
|---|---|---|---|---|---|---|
| 需求 | REQ-001 | source:DOC-001 | defined | integration | functional;security | 12 |
| 线号 | 示例编号 | source:DOC-001 | defined | none | none | none |

## 表 D · 主张级验证登记（13 列）

| claim_id | original_requirement_ref | required_environment | required_checks | required_change_record | actual_environment | actual_checks | qa_result | exemption | reason | scope | fallback_criterion | reopen_trigger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | REQ-001 | integration | functional;security | none | integration | functional;security | passed_at_actual | none | none | none | none | none |
|  |  |  |  |  |  |  |  |  |  |  |  |  |

## 填写说明

1. 一句一主张，一句一行；复合主张必须拆行，不得合并。
2. 表 A 的 20 列、表 B 的 9 列、表 C 的 7 列、表 D 的 13 列，列序固定；闭集字段只取 `references/10-contract.md` 给定值，自定义值一律判违例。
3. `linked_artifacts` 用 `;` 分隔多值；至少一条 `source:` 或 `cite:`，`artifact:` 与 `authorization:` 只能附加。`actual_environment=production` 时必须有一条 `artifact:`。
4. `assertion_form` 必须自陈。写 `qualitative` 而文本命中数量、时点、完备性语境化模式者判违例（受 `references/30-gates.md` `R14` 约束）。
5. 写 `quantity`、`datetime`、`identifier`、`completeness` 时，必须在表 B 新增一行并在 `comparability_ref` 填其 `cmp_id`；`identifier` 类另须在表 C 登记该编号。
6. `completeness` 类必须在表 B 同时给出 `completeness_mode`（`cleared`／`partial`）、`enumeration_count`（＞0）与 `remaining_count`（`cleared` 为 0、`partial` ＞0）；其他类别三列写 `none`。
7. `status = frozen_assumption` 时必须填 `expiry`、`review_owner`、`reopen_trigger`，三者均不得为 `none`。
8. `status = superseded` 时保留旧行原样，新增替代行；旧行不得删除或改写，且不得再被任何工件引用。
9. `exemption ≠ none` 时表 D 必须填 `reason`、`scope`、`fallback_criterion`、`reopen_trigger`，且 `approver` 必须为 `human:<ref>`；同一 `claim_id` 的 `reopen_trigger` 在表 A 与表 D 均非 `none` 时必须同值。
10. 示例行中的 `org:`、`seat:`、`none` 均为格式占位；实际值由项目绑定层提供，本模板不写死任何项目值。
11. 交付汇总的「无责任主体主张」单列区三元素齐＝条数＋`claim_id` 清单＋不可归属原因（口径见 `references/10-contract.md` 第 11 节）；单列区**不是第八桶**，该类行仍按判定序正常落七桶之一（承载＝`references/20-artifact-mapping.md` 第 1／3 节）。机检取数口径＝单列区全区逐号计数：`claim_id` 只在清单行出现一次、原因叙述不复述 `C-` 编号、「条数」与「不可归属原因」字样原样在位（对位 `30-gates` R13⑤）。
