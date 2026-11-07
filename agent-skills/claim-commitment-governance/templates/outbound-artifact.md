# 外发件模板

> 外发门字段与判据见 `references/10-contract.md` 第 6 节与 `references/30-gates.md` `R6`、`R8`、`R9`、`R15`。本模板不复制判据正文。

## 1. 外发门（六字段，缺一不得外发）

- `outbound_type`：`clarification_request` / `commitment` / `acceptance` / `risk_notice` / `report` 取一
- `claims`：本件引用主张的 `claim_id` 闭集列表，以 `;` 分隔；必须是主张登记表的真子集或全集，不得含未登记或 `superseded` 的 ID，且必须与第 2 节表内 `claim_id` 列集合全等
- `fact_review`：`<结论>@<reviewer>`；`reviewer` 不得为本件生成方
- `commitment_review`：`<结论>@<reviewer>`；`reviewer` 不得为本件生成方，且不得与事实审查人相同
- `authorization`：`human:<ref>`；无人类授权不得填写
- `send_channel`：`draft_only` / `approved_send` 取一

## 2. 主张引用区

| claim_id | claim | evidence_tag | authority | status | external_effect |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 3. 授权区

- 授权主体：`human:<ref>`
- 授权范围：由 `authorization:` 所指 `DEC-` 条目承载（本模板不单设范围列）
- 授权依据：`authorization:<PREFIX>-<digits>`
- 授权时效：与所引主张的 `expiry` 同值

## 4. 正文区

正文每条承重主张必须能回指第 2 节表内某个 `claim_id`；表外主张不得出现在正文承重句内。

## 5. 发送动作边界

`send_channel=approved_send` 只表示人类已授权发送，不表示系统执行发送；实际发送动作在系统外，由人类执行。`approved_send` 时不得残留任何占位词或未替换的 `〔` 填空标记。
