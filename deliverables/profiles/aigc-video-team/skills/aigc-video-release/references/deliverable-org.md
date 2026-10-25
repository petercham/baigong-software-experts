# 交付物组织与增量返工 — Deliverable Organization＋Incremental Rework Support

> 本件承载剪辑席位 MD 下沉的操作细则（批 3b-P4·依据设计件 §六 P4 与 §5.3）。两节文本随节整体搬运、不改写（标题层级按 references 平铺结构归一）；其中「写权限一致性」注记行为 v1.4.0 标记行（R2 §2.1/§2.2），按附录 B「随节沉，措辞不改」整体迁入本件。席位 MD 以索引指针指向本件。本件不反向引用席位文件路径（引用方向单向）。

## Deliverable Organization

Follow the structure defined in the production design:
- 工程文件在项目根目录
- 字幕文件在 `subtitles/` 目录
- 音效/BGM 清单在 `audio/` 目录
- 封面和发布文案在 `publish/` 目录
- 生成素材对应表（素材编号 ↔ 镜头号）随制作摘要交付
- 遵循导演分镜脚本中的精确镜头编号与时长

> 写权限一致性：以上组织形态描述交付物的逻辑结构；按写权三分法（v1.4.0），本席为**快速/极速档生产工件代行写入者**（随 A-05），产出以 SendMessage 回传为交付形态（跨席传递只回传资产 ID 清单＋四段式摘要，不传二进制）。<!-- v1.4.0: 依据 R2 §2.1/§2.2 -->

## Incremental Rework Support

When receiving a rework request (修改报告或系列化增量):

1. **Read existing project first** — understand the current cut before modifying
2. **Minimal changes** — only modify what's necessary. Do NOT re-edit the entire video; 增量片段优先复用既有生成参数与风格板。
3. **Preserve existing quality** — ensure existing shots and audio are not broken
4. **Document changes** — clearly list what was changed and why
