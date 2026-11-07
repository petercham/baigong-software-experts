# 20-artifact-mapping · 工件必填面

> 本文件只回答「哪类工件要挂哪些面、闸门在哪」，**不复写字段闭集与判据正文**：字段名、闭集值、相容矩阵、状态语义一律指针 `references/10-contract.md`，判据编号指针 `references/30-gates.md`。

## 1. 七类工件的必填面

| 工件 | 必填面 | 可选面 | 闸门归属 |
|---|---|---|---|
| PRD | 表 A 全列（20 列）；表 D 全列（每条主张一行）；`claim_type` 至少含一条 `requirement` | 表 B（有数量、时点、标识、完备性断言时转为必填）；表 C | 节点 1 需求；对外时加外发门 |
| 需求解析 | 表 A 全列；表 D 全列；每条解析结论须 `linked_artifacts` 含 `source:` 或 `cite:` | 同 PRD | 节点 1；解析件只引来源，不复制改写原文 |
| 工作票 | 表 A 的 `claim_id`／`claim`／`claim_type`／`source_layer`／`evidence_tag`／`authority`／`status`／`external_effect`／`generated_by`／`linked_artifacts`／`assertion_form`／`comparability_ref`；表 D 的 `claim_id`／`original_requirement_ref`／`required_environment`／`required_checks`／`required_change_record`／`actual_environment`／`actual_checks`／`qa_result`／`exemption` ＋ 降级四列 | 表 B | 节点 3 拆票；执行前校验 |
| 回执／回流件 | 表 D 的 `actual_environment`／`actual_checks`／`qa_result`；`claim_status_delta`；完成范围对照 | 表 B | 节点 4 执行；QA 前对账 |
| QA 判词 | 表 A 的 `claim_id`／`evidence_tag`／`authority`／`status`／`external_effect`；表 D 全列；逐条证据读数（`artifact:` 指向实测读数件） | 表 B | 节点 4／5；不得回写 `required_*` |
| 交付汇总 | 主张摘要；验证汇总；未绿项；豁免项；补验触发；**聚合字段七桶＋分母**（见第 3 节） | 外发门（若对外） | 节点 5 发布；对外前过 `gate-outbound` |
| 对外呈报／函件 | 外发门全字段（`outbound_type`、`claims`、`fact_review`、`commitment_review`、`authorization`、`send_channel`）；主张引用区 | 附加说明 | 外发前；人类授权后仅允许 `approved_send` 声明 |

## 2. 登记闭包

- **唯一主张登记表**：每个项目只有一处表 A（主张）、一处表 B（可比对断言行）、一处表 C（标识与需求）、一处表 D（主张级验证）；路径由项目绑定层注入，本技能包不写死路径。**绑定层注入什么、不注入什么见 `10-contract.md §11`**：绑定层只提供「登记表路径 ＋ 编号与角色位号的发放主体」，不提供任何判定规则；本包不自产编号与角色位号。
- **登记闭包**：任何工件引用的 `claim_id` 必须已在表 A 登记，且 `status ≠ superseded`。**允许真子集**——外发件与 QA 判词通常只引承重子集，不要求与 PRD 集合全等。
- **ID 解析**：`claim_id`、`cmp_id`、`REQ-` 前缀编号、`CMP-` 前缀编号，一律在登记表内解析；解析不到即判 `R2` 违例。

## 3. 交付汇总聚合字段（七桶＋分母，互斥且完备）

七个桶**互斥**，且必须**完备**——即七桶之和恒等于 `total_claims`。分桶按下列判定序取首个命中，不得跳序、不得重复计入：

1. `qa_result ∈ {failed, blocked}` → 计入 `failed`。
2. `actual_environment = unverified` → 计入 `unverified`。
3. `qa_result = passed_with_exemption` → 计入 `excluded_by_approval`。
4. `required_environment = none` → 计入 `not_required`（**本步必须先于第 5／6 步**：未提出要求环境的主张不参与环境实况分桶，故即便 `actual_environment` 落了 `mock`／`test`／`integration` 也不得记入 `mock_only`）。
5. `actual_environment = production` 且 `qa_result = passed_at_actual` → 计入 `real_env_passed`。
6. `actual_environment ∈ {mock, test, integration}` → 计入 `mock_only`。
7. 其余（`required_environment ≠ none` 且 `actual_environment = production` 且 `qa_result = pending`）→ 计入 `pending`。

| 字段 | 语义 |
|---|---|
| `total_claims` | 本次交付涉及的、在表 D 已登记的主张总数（分母＝表 D 行数） |
| `real_env_passed` | 判定序第 5 步命中数 |
| `mock_only` | 判定序第 6 步命中数（含 `integration`，不把 `integration` 掉出等式） |
| `unverified` | 判定序第 2 步命中数 |
| `failed` | 判定序第 1 步命中数 |
| `excluded_by_approval` | 判定序第 3 步命中数 |
| `pending` | 判定序第 7 步命中数 |
| `not_required` | 判定序第 4 步命中数 |

**守恒式（闭合，无游离项）**：`real_env_passed + mock_only + unverified + failed + excluded_by_approval + pending + not_required = total_claims`，且 `total_claims` 必须等于表 D 行数。任一行无法落入任一桶即判违例（不得默认放行，不得计入「未绿项」冲抵）。

**口径说明**：上一版把 `real_env_passed + mock_only + unverified` 三项当成闭式，导致 `production + passed_with_exemption`、`production + pending` 两类正常态掉出等式并被错误列入未绿项。本版改为七桶互斥完备，分母锚定表 D 行数。

**第 4 步前移的理由（治 `not_required` 恒不可达）**：上一版把「其余（含 `required_environment = none`）」放在第 7 步，而 `actual_environment` 闭集内没有 `none`，故凡 `required_environment = none` 的主张都会先被第 5 步 `actual_environment ∈ {mock, test, integration}` 吞进 `mock_only`——语义相反（未提要求被记成只在 Mock 验过），且 25 种「要求环境 × 实际环境」组合穷举下第 7 步命中 0，`not_required` 恒不可达。本版把「未提出要求环境」前移到第 4 步，并保留第 7 步承接「有要求、实况在 production、QA 未结论」这一真实剩余类。
