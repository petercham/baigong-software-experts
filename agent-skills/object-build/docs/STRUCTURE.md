# 项目分层目录方案 · object-build

本项目＝对象构建总入口技能。分层如下：

- `SKILL.md` — 技能入口定义件
- `references/` — 技能参考件（装配工序、规范件模板等）

交付面＝`SKILL.md`＋`references/`；`docs/` 为项目文档面，不属于交付路径。

```yaml
schema_version: 1
project_root: "."
delivery_paths:
  - SKILL.md
  - references/
```
