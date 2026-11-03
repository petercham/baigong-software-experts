# 决策包模板（SWB v2.9 · §4 异常强制呈报＋表2-2 决策包装配归状态机脚本）

> 决策包／呈报包装配与呈报＝状态机脚本（B4 decision-pack.py），主理人仅投递。本模板＝包字段格式说明与人工核对骨架，与 `scripts/decision-pack.py` 输出对齐。
> 构造注入包／决策包时剥除过程痕迹段（源头即纯，P-Ⅰ 前置）；已转正外部件按其级列入注入闭集，未转正件不入。

## 一、呈报包（异常强制呈报·触发源六闭集）

触发源六闭集（§4）：租约越界 deny ／ 对账差≠0 ／ 活性自检失败 ／ 引用扫描命中 ／ 超期 ／ 熔断。触发码越出闭集＝脚本拒绝装配。

```json
{
  "pack_type": "呈报",
  "trigger_source": "〔六闭集取一〕",
  "ticket_id": "〔票 ID〕",
  "evidence": { "〔证据键〕": "〔读数/路径〕" },
  "defect_grading": {
    "severity": "〔P0/P1/P2/…或 null〕",
    "severity_confirmed": false,
    "grading_authority": "QA 双复核＋人类终裁（表2-2）——脚本呈现定级与定级确认状态，不判级"
  },
  "delivery": "主理人仅投递（表2-2）；装配与呈报＝状态机脚本（B4）",
  "built_at": "〔UTC 时间戳〕",
  "pack_hash": "〔canonical_json sha256·脚本回填〕"
}
```

呈报同时写账本「呈报」记录类（append_record·哈希入账）。呈报时限：工程师票 48h／呈报 24h（timeouts 缺省，未配置项＝不适用）。

## 二、full-rollout 包（灰度→全量机械门禁·表2-2）

判据读取＝票内声明字段；无声明→拒绝出包并写「呈报」类审计事件（不得现场裁量）。

```json
{
  "pack_type": "full-rollout",
  "ticket_id": "〔票 ID〕",
  "criteria_checked": [ { "criterion": "〔判据名〕", "expect": "〔声明期望值〕" } ],
  "readings": { "〔判据名〕": "〔实测读数〕" },
  "gate": "QA 按声明判据机械门禁通过（表2-2）；单签＝full-rollout（表2-3 节点6）",
  "built_at": "〔UTC 时间戳〕",
  "pack_hash": "〔canonical_json sha256·脚本回填〕"
}
```

## 三、投递与在途登记

- 投递后至人类拍板前＝呈报在途承诺，登记 `.collab/commitments/`（投递回执、拍板期限、超时转呈报）。
- 呈拍（人类正式拍板）专指门一/门二签字与保险丝件；呈报知悉＝登记型投递（两门制）。
