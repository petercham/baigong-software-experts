# AIGC 视频专家团参照件（2026-10-24）

供「AIGC 视频团队」（`my-experts/aigc-video-team`）对标参照用。只读参照，不入交付面。

## 目录与来源

### official-cos/（源＝WorkBuddy 官方市场 CDN，权威官方源）
逐文件从 `acc-1258344699.cos.accelerate.myqcloud.com/workbuddy/expert-marketplace/plugins/<pkg>/` 拉取（即客户端召唤时实际下载的同一份）：

| 包 | 名称 | 类型 | 席位 | 作者 |
|---|---|---|---|---|
| ai-content-creator-team | 内容创作专家团 | team | 6（COS 现版；镜像旧版 7 含 creative-strategist） | CodeBuddy Teams（官方） |
| video-gen-team | 苍何视频生成团队（AI 视频创作团队） | team | 4 | 苍何 |
| video-dissection | 苍何视频解剖 | team | 3 | 苍何 |
| promo-creator-team | 袋鼠帝宣传片创作团队 | team | 6 | kangarooking |
| humanize-ppt-team | 卡尔的人感PPT专家团（含视频动效席） | team | 7 | 卡尔的AI沃茨 |

### video-teams/（源＝GitHub 第三方全量镜像 ahang1598/doubao-workbuddy-qwenwork-skills，同步至 2026-10-20）
含 official-cos 五包的镜像副本（用于交叉验证）＋官方 CDN 上已不存在的包：

| 包 | 名称 | 说明 |
|---|---|---|
| tiaoyue-screenplay-team | 跳跃视界·短剧创作专家团（v2.0.0，6 席） | 皮总所见「短剧创作专家团」即此（profession 字段＝短剧创作专家团） |
| ai-expert-studio | AI大模型专家团（5 席，含 Seedance 2.5 提示词工程参考件） | AI-HIVE Team |
| video-content-factory-studio | 视频内容工厂 Video Studio（5 席＋13 内嵌 skill） | 源＝作者原仓库 liangdabiao/workbuddy-expert-video-studio（GitHub）；皮总所见「内容工厂创作团」高度疑似此包 |

## 追加（2026-10-24 10:05）：方案 A 已兑现—— summoned-2026-10-24/

皮总经专家中心 UI 召唤，三个新包落盘本机市场目录（`.codebuddy-plugin/plugin.json`＋完整 agents/skills/avatars 全量件），已复制入本目录 `summoned-2026-10-24/`：

| 包 | 名称 | 类型 | 席位 | 作者 | 关键结论 |
|---|---|---|---|---|---|
| xiaoyunque-creative-team | 小云雀创作专家团 v1.1.0 | team | 6 | Pippit-dev <xiaoyunque@bytedance.com> | **字节/剪映官方实证**：bytedance.com 邮箱＋jianying.com 官网＋CLI 提交哈希三证俱全，皮总「剪映官方制作」判断属实 |
| science-video-team | 科普视频制作 v1.0.2 | team | 6 | AI_工具开发者 | 第三方；全场最强 SOP（双路径＋积分预算闸＋QC 如实闸＋确定性判据脚本） |
| kidd-content-expert | 吟游诗人基德创作专家 v1.0.0 | agent（单专家） | 1 | 吟游诗人基德 | bonus：皮总召唤时一并落盘；风格化编剧单点参照 |

三包已并入《五维对比分析.md》v2 与《全能AIGC视频创作团队-架构与五维优化方案.md》。下载量数据仍拿不到（登录态接口字段，静态通道无）。

## 历史缺口记录（保留备查）

1. **小云雀创作专家团：未拿到。** 静态清单 `expert_center.json`（lastUpdated 2026-08-18）与第三方镜像（2026-10-20）均无此包；官方 CDN 按 30+ 个拼音/英文 slug 猜测全部 404。判断为 2026-10-20 之后新上架、仅走登录态搜索接口（`/portal/operation-platform/market/expert/list`，需 Bearer token，token 不落明文盘）。
   - 另注：公开资料显示「小云雀」是**字节跳动剪映团队**的内容创作 App（百度百科/媒体报道）。WorkBuddy 是腾讯平台——若市场上确有「小云雀创作专家团」，**「剪映官方制作」存疑**，更可能是第三方借名，需拿到包体后看 author 字段定论。
2. **下载量数据：拿不到。** 静态清单与镜像均无下载量字段（镜像 README 的数字列是文件数）；下载量只在登录态接口返回。
3. **内容创作专家团版本差异**：COS 现版 6 席（无 creative-strategist），镜像 2026-10-20 版 7 席——官方在 8 月清单后改过席位，参照时以 official-cos 为准、镜像为旁证。

## 补口方案（待皮总拍）

- **A（最直接）**：皮总在 WorkBuddy 专家中心 UI 里召唤/下载「小云雀创作专家团」等内容工厂系新包 → 落盘 `~/.workbuddy/plugins/marketplaces/experts/plugins/` → 我直接读取入参照目录。
- **B**：皮总把专家详情页截图（含下载量、开发者名）发我，先补下载量与「官方性」判断。

## 追加（2026-10-24 09:30）：科普视频制作专家团——同样未拿到

- 静态清单（429/448 两条快照）全文检索「科普」：仅两个 **Agent 型单专家**（吟游诗人基德·知识视频创作专家、VibeKnow 手绘视频专家），无「科普视频制作」**专家团**。
- 镜像（10-20 同步）无此名；GitHub 搜「科普视频制作」命中的全是第三方 skill 仓（science-video-studio、kepu-short-video-team 等），无一标注为 WorkBuddy 市场上架包。
- 官方 CDN 按 40+ 个中英拼音 slug（kepu-video-*、science-video-*、popsci-*、edu-video-*、vibe-knowledge-* 等）探测全部 404。
- 结论：与「小云雀创作专家团」同情形——**10-20 之后新上架、只走登录态搜索接口**。补口仍走方案 A：UI 召唤落盘后我直接读取。
