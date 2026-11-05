# 项目分层目录方案 · multi-collab

本项目＝协作纪律（权限分级版）技能。分层如下：

- `SKILL.md` — 技能入口定义件
- `references/` — 技能参考件（规程、模板、裁决引文等）

交付面＝`SKILL.md`＋`references/`；`docs/` 为项目文档面，不属于交付路径。

非枚举面＝生成物与装配元数据（COPY.state、bundle.lock、plugin.json、settings.json、仓侧 README.md）不逐件枚举，声明面对其零覆盖属既成惯例（STRUCT-FIX 成文·C-3 机检据此豁免）。
点号名顶层面（`.collab/`、`.scratch/`、`.codebuddy-plugin/` 等）不入声明射程，机检对账对其零覆盖属既成惯例。

```yaml
schema_version: 1
project_root: "."
delivery_paths:
  - SKILL.md
  - references/
```
