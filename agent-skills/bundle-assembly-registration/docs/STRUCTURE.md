# 项目分层目录方案 · bundle-assembly-registration

本项目＝装订注册技能。分层如下：

- `SKILL.md` — 技能入口定义件
- `references/` — 技能参考件（装订工序、注册台账格式等）

交付面＝`SKILL.md`＋`references/`；`docs/` 为项目文档面，不属于交付路径。

```yaml
schema_version: 1
project_root: "."
delivery_paths:
  - SKILL.md
  - references/
```
