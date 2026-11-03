# 项目分层目录方案 · external-advisor-collab

本项目＝外部顾问讨论会治理技能。分层如下：

- `SKILL.md` — 技能入口定义件
- `references/` — 技能参考件（规程、模板、裁决引文等）

交付面＝`SKILL.md`＋`references/`；`docs/` 为项目文档面，不属于交付路径。

```yaml
schema_version: 1
project_root: "."
delivery_paths:
  - SKILL.md
  - references/
```
