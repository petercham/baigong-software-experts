# AIGC 视频团队 · 七席返工说明（批 28 一阶段）

- 日期：2026-10-23
- 依据：裁-38 Q1=A（skill 包轨已撤，批 27）＋Q3=A（全量七席 AIGC 化，皮总已拍）；皮总定名「AIGC 视频团队」——团队不能执行传统手工美术与实拍，**多模态生成是生产手段**。
- 基线：专家包面 `my-experts/plugins/video-company/agents/` 七件（＝治理盘 b2933cc 态＋frontmatter），**只读复制**；本批全部改动落本草稿区，专家包面零碰（三阶段：草稿返工→gate-qa 复核→主理人执行专家包面更名重装）。

## 文件更名与 Agent ID 定案（主理人 L2）

| 旧（基线） | 新 |
|---|---|
| video-company-team-lead.md | aigc-video-team-lead.md |
| video-content-strategist.md | aigc-content-strategist.md |
| video-screenwriter.md | aigc-screenwriter.md |
| video-production-designer.md | aigc-production-designer.md |
| video-director.md | aigc-director.md |
| video-editor.md | aigc-editor.md |
| video-operations.md | aigc-operations.md |

frontmatter `name` 同步；正文内所有旧 Agent ID/文件名指针同步改（含主理人件子任务命名清单 22 处＋成员表文件指针）；团队建议命名 `video-<项目简称>`→`aigc-<项目简称>`（含返工 `aigc-rework-<问题简称>`）；英文团队名「Short Video Production Team」→「AIGC Video Team」。**displayName/profession（人名齐上线/许爆款等）保留不改**。

## 逐席改动清单

### 1. 主理人（aigc-video-team-lead.md）
- 开篇加团队定性句：多模态生成（文生图/图生视频/文生视频）为生产手段，不执行实拍与手工美术制作；派单/验收话术「拍摄/实拍/现场」→「生成/合成/产出」（依据＝裁-38 Q3=A 皮总原话语境）。
- 标准 SOP 链路改 AIGC 生产链路：选题→剧本→视觉生成（美术设计方案＋镜头生成方案）→剪辑合成→发布；各档编排步骤同步（极速＝素材生成+合成出片；快速＝镜头生成+合成出片）。
- 成员表职责列同步（美术指导→场景概念生成与视觉资产库；导演→镜头生成方案；剪辑师→生成素材质检、合成成片）。
- 输入白名单回传件名「分镜与制作方案」→「分镜与镜头生成方案」；标准 SOP 第 4/5/6 步转件与产出名同步。
- 系列化增量：美术指导增量补「复用风格板/参考图/种子」；反馈回路新增「生成质检连续不合格→导演改方案→主理人呈用户」路由。
- 默认工具链拆生成侧（文生图/图生视频模型按可用性选型）＋合成侧（剪映/PR/达芬奇）。
- **判档逻辑（五档路由表）不变、铁律不变、写权限模型不变。**

### 2. 内容策划（aigc-content-strategist.md）
- Constraints 加「生产手段＝多模态 AI 生成（不实拍），选题评估必含 AIGC 可生成性」。
- 简报「制作规范」节新增 **AIGC 可生成性** 行（可生成/部分可生成/不可生成三档结论；不可生成标注转人工素材或建议改选题，不得默许进入生产链路）。
- 新增「AIGC 可生成性评估」节：五判据（主体稳定性/动作复杂度/文字与界面/实拍依赖素材/风格可得性）＋三档结论处置（依据＝裁-38 Q3=A）。

### 3. 编剧（aigc-screenwriter.md）
- 话术适配：「shootable」→「generable（不实拍）」；「怎么拍」→「怎么生成」；「画面可执行」条补生成高风险画面显式标注义务；输入白名单加「待改编文字原文（仅 Mode 3）」。
- **新增 Mode 3: Text Adaptation（文字内容改编）**（依据＝裁-37②⑥）：①版权提示前置（未确认授权只出改编方案不出全文）②忠实度分级（原著向/借鉴向/灵感向，先确认档位，未确认按原著向假设并置顶待确认）③文体识别与改编策略（小说/科普/新闻/观点文四体：视角转换、信息密度取舍、单集/多集切分）④科普类专项（论点→画面化转译；数据不虚构、无数据不补造、示意画面标注）⑤输出结构五节。
- Mode 1/2 结构与规则不动。

### 4. 美术指导（aigc-production-designer.md）
- 去实拍/手工依赖：Goal/Constraints 改「可生成」语境；「美术组统筹（置景/道具/陈设/平面施工）」→「视觉资产统筹（AIGC 形态职责）」；道具场景清单改「生成场景内视觉元素本体」。
- 气氛图板节加产出形态行：概念图/气氛图/场景设计图均以**文生图生成**交付（场景概念生成图、关键帧视觉稿、风格参考图集）。
- **新增第 7 节「AIGC 视觉生成本体」**：风格一致性手段（风格板/参考图策略/种子管理/负面提示词）、生成提示词模板（六槽位：主体＋环境＋光线＋色调＋风格＋镜头感，禁止各席自拼）、视觉资产库管理（统一编目供系列化复用）。
- 一致性检查清单加「跨镜头风格一致（色温/笔触/材质无漂移）」项；Design Rules「可执行」→「可生成」（生成不可靠要求须给替代策略）；版权安全条补「生成产物注明模型＋AI 标识需求（合规交运营）」。
- 「指导拍摄或剪辑」类话术→「指导镜头生成与剪辑合成」；输出契约产出构成同步。
- **本体框架不动**：视觉世界观/场景空间/年代材质/气氛图板/包装规范概念五件套保留；构图/运镜仍归导演。

### 5. 导演（aigc-director.md）
- 去现场调度：开篇/Constraints 改「镜头生成方案＋分镜表」，明确不执行实拍与现场调度，镜头运动以生成参数表达（运镜提示词、时长、首尾帧），流程＝生成-筛选-重生成迭代。
- 「Implementation Approach（制作方案）」→「Shot Generation Approach（镜头生成方案）」：生成方式选项改（图生视频/文生视频/文生图+运镜/模板化混剪；实拍类需求转译或标注转人工素材）；新增**生成-筛选-重生成迭代流程**条（验收判据→批量生成→筛选→调参重生成；单镜头重生成预算默认 ≤3 次）。
- 分镜表字段适配（每镜头：画面生成描述/参考图（引美术指导图集编号）/生成方式/预期时长/备选策略）；构图/运镜规范唯一出处条款保留＋补「运镜给出生成模型提示词表述」；首尾帧衔接关系标注。
- 输入白名单第 2 项补「美术指导的生成素材是直接素材」；提示词沿用美术指导模板、本席只填镜头感槽位。
- **分镜表保留、Mode 结构不动、任务分解仍为零（裁-33 已删）。**

### 6. 剪辑师（aigc-editor.md）
- 素材来源改 AIGC 生成产物：Core Identity/输入白名单同步（新增「AIGC 生成素材」输入项；导演产出名改「镜头生成方案＋分镜表」）。
- **新增「生成素材质检」工序（合成前必做）**：五缺陷项表（闪烁/形变/一致性缺陷/物理错误/时长画幅不符）×识别要点×处置（可用/后期可救/需重生成建议单）；重生成建议单经主理人转导演；预算用尽→备选策略→上报主理人；用户实拍素材（如有）同过一致性检查。
- 自检清单加「生成素材质检单已随附」项；素材元数据条补「source: 生成模型/用户素材」；工具链补「素材生成」层。
- **清软件工程话术遗留（裁-33 登记项，逐处领域适配）**：「Follow the storyboard and task list」→「storyboard and shot-generation plan」；「Implement Tasks/ALL-AT-ONCE」→「Deliver Assets」；「Task T01/project infrastructure」→「Project Setup」；「consecutive write operations」→「in one go」；「No separate mkdir」→「No separate setup rounds」；「No unnecessary shell commands/scaffolding CLIs/empty scaffolding」条删除（并入 Complete delivery）；「bug routed back」→「rework routed back」；「Incremental Development Support（new feature）」→「Incremental Rework Support」；「over-engineering」→「over-processing」；「COMPLETE DELIVERABLES」条去 `TODO` 代码味改交付语义；「Deliverable Organization」去「导演文件列表相对路径」改「分镜表镜头编号与时长」。
- 剪辑/节奏/字幕/音频职责不变；自检不构成放行不变；有界回路 2 轮不变。

### 7. 运营（aigc-operations.md）
- 合规审核新增 **AI 生成内容标识** 核查项：按平台要求核查 AI 声明/标注（发布勾选/画面标识/简介声明）；各平台声明义务逐条引用户文档（出处纪律沿用），缺则标「未经核实」；真人换脸/声音克隆另查深度合成专项；**未标注＝放行阻断项**。
- 平台适配段新增「AI 生成内容限流/标签规则」：已标注/未标注分发差异、AI 专属话题标签、批量低质 AIGC 限流风险；发布策略补「标注方式＋规避限流的发布节奏」建议。
- 三栏「管什么」同步；输入白名单第 2 项导演产出名对齐。
- **其余不动**：唯一放行点、判定=放行/退回、出处纪律、2 轮上限、报告格式。

## 未改动声明

- **框架**：七席编制、五档工作流（极速/快速/返工/标准 SOP/部分工作流）、铁律四条＋严禁行为、各席 Mode 结构（除编剧按指令新增 Mode 3）、三栏/权限四类/输入白名单三件套、写权限模型、有界回路 2 轮——全部不动。
- **人名**：齐上线/许爆款/剧有梗/美得很/构得美/卞得顺/严过审 及 displayName/profession 全部保留。
- **判档逻辑**：主理人工作流路由表判定条件不变。
- 专家包面（my-experts/plugins/video-company/）零碰；旧草稿区（drafts-2026-10-23/video-team/）零碰；deliverables/ 零碰。

## 自查结果（2026-10-23）

- grep「实拍｜拍摄现场｜置搭｜道具制作｜摄影指导到场」：命中 10 处，**全部为对比语境**（「不执行实拍」「替代实拍/手工」「实拍类需求转译」「实拍依赖素材」「非实拍还原」「用户提供的实拍素材（如有）」），符合指令豁免。
- grep 旧 Agent ID（video-company-team-lead/video-content-strategist/video-screenwriter/video-production-designer/video-director/video-editor/video-operations）：**零命中**。
- grep「shootable/Short Video Production Team/怎么拍/可拍摄/可拍剧本」：**零命中**。
