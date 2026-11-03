# 项目分层目录方案 · object-audit

本项目＝对象审计总入口技能。分层如下：

- `SKILL.md` — 技能入口定义件
- `references/` — 技能参考件（审计骨架、测项标准等）
- `scripts/` — 机检脚本（run-gates.sh 等门禁脚本）
- `tests/` — 脚本配套测试件

交付面＝`SKILL.md`＋`references/`＋`scripts/`＋`tests/`；`docs/` 为项目文档面，不属于交付路径。

```yaml
schema_version: 1
project_root: "."
delivery_paths:
  - SKILL.md
  - references/
  - scripts/
  - tests/
```
