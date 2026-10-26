# 审核报告格式与模板 — Review Report Format

> 本件承载运营席位 MD 下沉的报告格式与模板（批 3b-P5·依据设计件 §六 P5 与 §5.5）。文本随节整体搬运、不改写（标题层级按 references 平铺结构归一；模板代码块逐字保留）；席位 MD 以「⛓ 必读」指针直达本件，不在 MD 内复述细则（避免第二真源）。本件不反向引用席位文件路径（引用方向单向）。

## Review Report Format

After running all reviews, generate a concise report:

```markdown
# Review Report

## Summary
- 审核项: X | 通过: Y | 未过: Z
- 覆盖范围: 公开面全量 / 关键路径（estimated）
- 路由判定: NoOne / Editor / Known Issues

## 未过项 (if any)
- 问题描述（Expected vs actual）— [Timecode: 00:12-00:15] — 规则/质量依据 — 修改建议

## Known Issues (if Round 2 still fails)
- Issue description and affected module
```
