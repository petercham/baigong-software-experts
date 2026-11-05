# 项目分层目录方案 · baigong-software-team

本项目＝百工软件团队专家包（bundle 面打包体）。分层如下：

- `agents/` — 角色定义件（主理人/架构/产品/工程/QA 等席定义）
- `skills/` — 包内技能件（sop 等技能目录）
- `config/` — 包配置（席位权限、编排配置等）
- `hooks/` — 钩子件
- `tests/` — 包级测试件
- `avatars/` — 头像资源
- `docs/adr/` — ADR 正件族（架构席终写落位·编号四位·永存面不入退役流程；不属于交付路径）

交付面＝上述 bundle 面六目录；`docs/` 为项目文档面，不属于交付路径。

非枚举面＝生成物与装配元数据（COPY.state、bundle.lock、plugin.json、settings.json、仓侧 README.md）不逐件枚举，声明面对其零覆盖属既成惯例（STRUCT-FIX 成文·C-3 机检据此豁免）。
点号名顶层面（`.collab/`、`.scratch/`、`.codebuddy-plugin/` 等）不入声明射程，机检对账对其零覆盖属既成惯例。

```yaml
schema_version: 1
project_root: "."
delivery_paths:
  - agents/
  - skills/
  - config/
  - hooks/
  - tests/
  - avatars/
```
