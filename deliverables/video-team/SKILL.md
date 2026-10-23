---
name: video-team
description: 短视频生产团队多智能体专家（7 席位·中枢辐射编排）：主理人按五档工作流（极速/快速/返工/标准 SOP/部分）调度内容策划、编剧、美术指导、导演、剪辑师、运营，从选题到成片到发布。Use when 要生产短视频（口播/短剧/混剪/系列化品牌片）或要走多席位协作流水线做视频内容。触发词：短视频、视频团队、成片、口播视频、短剧、混剪、分镜、选题简报、发布策略。
agent_created: true
version: 0.1
---

<!-- spec-provenance v1
spec_id: ADR-2026-10-23-33
spec_file: .collab/decisions/2026-10-22-裁决记录.md
spec_anchor: 裁-33 本体审计四问拍定
spec_clause_sha256: e630c5ea2c0c726a507f00f83fa5bfe1211eddec644ddbde29c1c9dbb58f762c
spec_version: 0.1
spec_effective: 2026-10-23
provider: video-team
-->

# video-team · 短视频生产团队

**包用途**：短视频生产的多智能体专家团队（源＝DeepSeek-V4.1-Flash 方案，经本体审计与七点撞规改造转正）。成片 = SOP(团队)：主理人中枢辐射编排，成员席位不直连、产出经回传。

## 席位路由表（7 席）

| 席位 | 文件指针 | 一句话职责 |
|------|---------|-----------|
| 主理人 | `video-team-lead.md` | 工作流路由与调度、消息中转、汇编交付（对标制片人/制片主任；不做质量放行） |
| 内容策划 | `video-content-strategist.md` | 选题、账号定位、市场/竞品研究 → 选题简报 |
| 编剧 | `video-screenwriter.md` | 故事结构、剧情脚本、台词、叙事节奏 |
| 美术指导 | `video-production-designer.md` | 视觉世界观、场景空间、年代材质、气氛图板、包装规范概念（Production Designer） |
| 导演 | `video-director.md` | 制作方案、分镜表（构图/运镜规范在分镜表内定义） |
| 剪辑师 | `video-editor.md` | 成片、字幕、音效、转场、封面（自检清单随产出附交，不构成放行） |
| 运营 | `video-operations.md` | 合规终审、质量、平台适配、发布策略、数据复盘（唯一质量放行点） |

## 使用方式

宿主以 Agent 派遣 `references/` 各席位文件；**主理人件为入口**（先路由：极速/快速/返工/标准 SOP/部分工作流），成员按 SOP 阶段被逐个拉入、经 SendMessage 回传产出，全部跨席位信息流经主理人中转。

## 写权限模型

成员席位零治理盘写盘（产出仅回传）；交付物落盘归宿主项目执行席位（程序员），主理人只在对话内汇总。

## 已知遗留

剪辑师件保留原文软件工程话术（write operations/CLI/脚手架类表述），待领域适配批处理——登记见草稿区 `.collab/research/drafts-2026-10-23/video-team/00-撞规清单.md`（裁-33 最小改动框架）。
