# AIGC Video Team

AIGC 视频团队专家团：制作总监统筹六席，以**多模态生成（文生图／图生视频）为生产手段**，按五档工作流把视频需求从选题推到成片发布。本团队不执行传统手工美术与实拍。

## 类型

Team 型（多角色协作团队）

## 功能

- **7 席位中枢辐射编排**：主理人（制作总监·对标制片体系）＋内容策划、编剧、美术指导（Production Designer）、导演、剪辑师、运营（合规与发布）
- **AIGC 生产链路**：选题（含 AIGC 可生成性评估）→ 剧本（原创/打磨/**文字改编**：小说·科普·新闻→剧本，忠实度三档＋版权前置闸）→ 视觉生成（风格板·种子管理·提示词模板）→ 镜头生成（图生视频/文生视频·生成-筛选-重生成迭代）→ 剪辑合成（生成素材质检）→ 合规发布（AI 生成内容标识核查）
- **五档工作流路由**：极速（纯混剪）/ 快速（单条口播短剧）/ 返工快捷 / 标准 SOP（系列品牌片）/ 部分工作流
- **治理设计**：成员零治理盘写盘（产出经 SendMessage 回传）、运营席唯一质量放行点（剪辑师仅自检）、行业判据须引用户提供的规则库
- **有界回路**：审核最多 2 轮，超限输出遗留问题报告

## 使用示例

- 把这篇小说章节改编成 3 集短剧剧本：先确认忠实度档位，再出可生成剧本。
- 围绕这个主题做一条 60 秒抖音口播视频：钩子、脚本、生成方案、成片方案和封面一起出。
- 审这条成片：合规、AI 生成内容标识、质量、平台适配逐项过，给发布策略。

## 出身

本专家团由本仓（multi-agent-collab-skillpack）草稿区 `.collab/research/drafts-2026-10-23/aigc-video-team/`（批 28 判词放行态 `e0927f4`/`1a7e26a`）转化而来。沿革：初版误以 skill 形态交付（定性见裁-37④·已撤包除名 `1e16824`）；本体经影视工业岗位体系审计（裁-33）＋AIGC 生产手段全量改造（裁-38 Q3=A）；前身包 video-company v1.0.0 退役，本版 v1.1.0 更名 aigc-video-team（裁-37⑥ 皮总定名「AIGC 视频团队」）。

## 头像

头像未生成（`avatars/` 暂空）。如需自定义头像，要求：
- 格式：PNG（推荐）或 JPG
- 尺寸：512×512 px
- 大小：单张不超过 500KB
- 文件名对应 plugin.json members[].avatar：team.png / aigc-video-team-lead.png / aigc-content-strategist.png / aigc-screenwriter.png / aigc-production-designer.png / aigc-director.png / aigc-editor.png / aigc-operations.png

## 安装

将专家包目录放到专家目录下：

```
~/.workbuddy/plugins/marketplaces/my-experts/plugins/aigc-video-team/
```

然后运行注册命令使其可见：

```bash
python3 scripts/register_expert.py <expert-dir>
```

## 打包分享

```bash
zip -r aigc-video-team.zip aigc-video-team/
```
