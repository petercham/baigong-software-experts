# AIGC Video Team

AIGC 视频团队专家团：制作总监统筹六席，以**多模态生成（文生图／图生视频）为生产手段**，按五档工作流把视频需求从选题推到成片发布。本团队不执行传统手工美术与实拍。**一切工作以经需求方（人类）确认的项目圣经为规约——圣经未确认，任何席位不开工。**

## 类型

Team 型（多角色协作团队）

## 功能

- **7 席位中枢辐射编排**：主理人（制作总监·对标制片体系）＋内容策划、编剧、美术指导（Production Designer）、导演、剪辑师、运营（合规与发布）
- **项目圣经（制作规约）闸**：立项第一件事＝主理人起草项目圣经（定位/平台受众/风格规约/形制/验收标准/禁忌红线/变更记录七节）→ 呈需求方**显式确认（不默认通过、不确认不开工）**→ 冻结 → 下游各席以圣经为准（美术风格从圣经推导不得自创、运营终审不符圣经＝放行阻断项）；极速档不豁免（简版风格卡一页仍须确认）
- **五道人类确认闸（G1–G5）**：G1 圣经定稿（含生成预算：单镜头重生成≤3 次默认＋总上限需求方定）→ G2 剧本定稿 → G3 生图/生视频提示词定稿 → G4 生成预算（预算内自动、超限才呈）→ G5 成片验收（**运营审核通过≠发布**，需求方验收后才出发布策略）；统一纪律＝显式确认、沉默不算、不确认不流转；铁律「闸不可跳，不得推定通过」
- **AIGC 生产链路**：选题（含 AIGC 可生成性评估）→ 剧本（原创/打磨/**文字改编**：小说·科普·新闻→剧本，忠实度三档＋版权前置闸）→ 视觉生成（风格板·种子管理·提示词模板）→ 镜头生成（图生视频/文生视频·生成-筛选-重生成迭代）→ 剪辑合成（生成素材质检）→ 合规发布（AI 生成内容标识核查）
- **五档工作流路由**：极速（纯混剪）/ 快速（单条口播短剧）/ 返工快捷 / 标准 SOP（系列品牌片）/ 部分工作流
- **治理设计**：暂存区八目录＋写权三分法（生产工件随 A-05：标准＝导演席、快速/极速＝剪辑席代行；治理件 bible/audit/state 归主理人；质检件 qc/ 判据脚本沙箱定向写——「主理人零生产写盘，不是零写盘」）、运营席唯一质量放行点（剪辑师仅自检）、行业判据须引用户提供的规则库 <!-- v1.4.0: 依据 R2 §2.1/§2.2——替换 v1.3.0「成员零治理盘写盘」表述，新旧条款对照见主理人件「写权限模型」节 -->
- **有界回路**：审核最多 2 轮，超限输出遗留问题报告

## 使用示例

- 把这篇小说章节改编成 3 集短剧剧本：先确认忠实度档位，再出可生成剧本。
- 围绕这个主题做一条 60 秒抖音口播视频：钩子、脚本、生成方案、成片方案和封面一起出。
- 审这条成片：合规、AI 生成内容标识、质量、平台适配逐项过，给发布策略。

## 出身

本专家团由本仓（multi-agent-collab-skillpack）草稿区 `.collab/research/drafts-2026-10-23/aigc-video-team/`（批 32 判词放行态 `42b34bf`/`60d1ea1`）转化而来。沿革：初版误以 skill 形态交付（定性见裁-37④·已撤包除名 `1e16824`）；本体经影视工业岗位体系审计（裁-33）＋AIGC 生产手段全量改造（裁-38 Q3=A）＋项目圣经机制（裁-41）＋五道人类确认闸（裁-44）；前身包 video-company v1.0.0 退役，v1.1.0 更名 aigc-video-team（裁-37⑥ 皮总定名「AIGC 视频团队」），v1.2.0 入项目圣经闸，v1.3.0 入五道确认闸，v1.4.0 入暂存区八目录＋写权三分法＋提示词资产制度＋G4 窄幅（R2 §2.1–2.3/§3.2·条款逐字照录，改动处带 v1.4.0 标记）。

## 头像

头像为**借用素材**：取自官方 `ai-content-creator-team` 专家团头像（同属 AI 内容创作语境，岗位语义近似映射：主理人←团队主理人、策划←creative-strategist、编剧←copywriter、美术指导←image-creator、导演←video-generator、剪辑←video-editor、运营←content-adapter），统一缩放至 512×512 PNG（≤500KB）。如需替换为定制头像，按以下规格覆盖同名文件即可：
- 格式：PNG（推荐）或 JPG；尺寸：512×512 px；大小：单张 ≤500KB
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

## Token 计数（终态·批 3b 结构化瘦身后）

**口径四要素**（缺一不计绿）：①口径版本＝`script-v1`（`tools/count_agent_tokens.py`：CJK≈1 token/字、非 CJK≈4 字符/token）；②实测 commit＝`6447f76`（七席 MD 终态所在提交，本表随批 3b-P6 落盘）；③实测人＝b3b-engineer；④取整方式＝**ceil**（`-(-(n) // 4)`）。判据＝每席 ≤2,500（红线），目标 ≤2,350。

| 席位 MD | 行数 | token | ≤2500? | 口径版本 | 下沉件数 | 下沉 token | 实测人 | 实测 commit |
|---|---|---|---|---|---|---|---|---|
| aigc-video-team-lead.md | 119 | 2,287 | 绿 | script-v1 | 12 | 10,774 | b3b-engineer | 6447f76 |
| aigc-editor.md | 112 | 2,333 | 绿 | script-v1 | 7 | 1,703 | b3b-engineer | 6447f76 |
| aigc-production-designer.md | 101 | 1,985 | 绿 | script-v1 | 2 | 1,367 | b3b-engineer | 6447f76 |
| aigc-operations.md | 135 | 2,188 | 绿 | script-v1 | 5 | 1,315 | b3b-engineer | 6447f76 |
| aigc-screenwriter.md | 146 | 2,285 | 绿 | script-v1 | 2 | 614 | b3b-engineer | 6447f76 |
| aigc-director.md | 108 | 2,300 | 绿 | script-v1 | 3 | 483 | b3b-engineer | 6447f76 |
| aigc-content-strategist.md | 107 | 1,845 | 绿 | script-v1 | 3 | 883 | b3b-engineer | 6447f76 |
| **合计** | **828** | **15,223** | — | script-v1 | **34** | **17,139** | b3b-engineer | 6447f76 |

**读法（MD 是 cost center，references 是 asset）**：常驻侧七席合计 15,223 tok（批 2d 后基线 28,398，−46.4%）；资产侧 `skills/` 五域 27 件 references 合计 18,473 tok＋5 件索引 SKILL.md 合计 2,971 tok（治理 662／编排 532／内容 492／视觉 500／发布 785，均 ≤2,500 预防线）。**总量不降**（28,398→36,667，+29.1%）——本次不是减总量，是把成本从「每次会话全付」移到「按需才付」；v1.4.0 硬条款本体在 references 中逐字承载（C3 逐字门保护），席位 MD 以「⛓ 必读」硬读指针直达（确定性通道，不依赖语义匹配）。

**计数规则说明**：
- 「下沉件数」＝承载该席下沉内容的 references 件数（共用件按件各计：`teammate-protocol.md` 为六席回传机制单真源，六席各计 1 件；`default-toolchain.md` 为剪辑席＋导演席共用，两席各计 1 件）。
- 「下沉 token」＝该席 MD 实际迁出块的 token 合计（逐块实测，P1–P5 累计）；因共用件按席分别计入，合计行含六席各自回传机制块（`08a466a` 逐块实测合计 1,249 tok）对单真源 `teammate-protocol.md`（452 tok）的重复计数（797 tok）——资产侧以去重后 18,473 tok 为准。
- 基线（批 2d 后·`ef3c66e`·script-v1 复算·7/7 与主理人独立复算 MATCH）：lead 10,886／editor 3,729／PD 3,118／operations 3,016／screenwriter 2,724／director 2,496／strategist 2,429，合计 28,398。此前基线表（非 CJK 取整截断口径）按读数四要素规则退出流通，不再作为判据。
