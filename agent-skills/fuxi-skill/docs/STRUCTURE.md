# 项目分层目录方案 · fuxi-skill

本项目＝伏羲（fuxi-skill）perspective-pack-builder 技能。分层如下：

- `SKILL.md` — 技能入口定义件
- `references/` — 技能参考件（V3 形态设计契约、炼成工序等）
- `products/` — 视角包成品（按契约炼成的 perspective pack 产物）

交付面＝`SKILL.md`＋`references/`＋`products/`；`docs/` 为项目文档面，不属于交付路径。

```yaml
schema_version: 1
project_root: "."
delivery_paths:
  - SKILL.md
  - references/
  - products/
```
