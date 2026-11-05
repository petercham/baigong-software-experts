# 项目分层目录方案 · fuxi-skill

本项目＝伏羲（fuxi-skill）perspective-pack-builder 技能。分层如下：

- `README.md` — 包级详细件（性质自注＝交付件本体·相近工具对照表置顶）
- `adapters/` — 对象分类适配件（person/method/classifier 三型）
- `contracts/` — 契约真源（artifact-contract／evidence-grading／failure-modes）
- `gates/` — 机检闸面（assert-tool／harness／validator 族）
- `products/` — 视角包成品（按契约炼成的 perspective pack 产物）
- `rejected/` — 淘汰候选留档面
- `specs/` — 对象规范件（perspective-spec／technique-spec）

交付面＝上述七目录/件；`docs/` 为项目文档面，不属于交付路径。

非枚举面＝生成物与装配元数据（COPY.state、bundle.lock、plugin.json、settings.json、仓侧 README.md）不逐件枚举，声明面对其零覆盖属既成惯例（STRUCT-FIX 成文·C-3 机检据此豁免）。
点号名顶层面（`.collab/`、`.scratch/`、`.codebuddy-plugin/` 等）不入声明射程，机检对账对其零覆盖属既成惯例。

```yaml
schema_version: 1
project_root: "."
delivery_paths:
  - README.md
  - adapters/
  - contracts/
  - gates/
  - products/
  - rejected/
  - specs/
```
