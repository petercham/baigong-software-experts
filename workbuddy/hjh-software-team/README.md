# Software Company（软件开发团队）

软件开发团队专家团：交付总监统筹产品经理、架构师、工程师、QA 四席，按固定 SOP 把需求推到可验收交付，每步留证据与判定级别。

## 类型

Team 型（多角色协作团队）

## 功能

- **5 席位 SOP 协作**：主理人（交付总监·齐活林）＋产品经理（许清楚）＋架构师（高见远）＋工程师（寇豆码）＋QA 工程师（严过关）
- **工作流路由**：主理人收到请求先判断档位（快速模式／标准 SOP／部分工作流），再定席位编排与推进顺序
- **可审计交付**：每步产出带验收判据与判定级别，需求→拆解→设计→实现→质检全程留痕

## 使用示例

- 把这个需求拆成可验收的开发任务，标出依赖、验收判据和预估改动面。
- 审这份交付或治理报告，按四态判定给结论，列出必须补的缺口。

## 出身

本专家包为**市场包 fork 自维护**：

- **基线**＝WorkBuddy 专家中心市场包 `software-company` **v1.1.0**（下载戳 **2026-10-09**，市场缓存 `~/.workbuddy/plugins/cache/experts/software-company/1.1.0/` 目录 mtime 实测）。
- **fork 后本地改动清单**（除以下三项外，五席 MD 逐字照录市场版，零改写）：
  1. **plugin.json 形态适配**：市场版仅 7 键、过不了注册校验（缺 displayName），改用 my-experts 注册形态 18 键（注册适配层，非席位定义层改动）；
  2. **lead 改名**：文件名 `software-team-lead.md`→`software-company-team-lead.md`，内容仅 frontmatter `name:` 一行同步（Q3 拍定差，diff 市场版＝仅此一处）；
  3. **版本升 1.1.1**（Q5 拍定）：版本号变更逼宿主刷新运行缓存，规避「同版本号免刷新」漂移。
- **上游关系**：fork 自维护，上游后续版本不自动追；需要时人工 diff 市场缓存对账一次（版本账即本节）。
- **版本账 v1.3.0**（2026-10-28）：软开 bundle 由「无装配环节·真源直拷」改「有装配环节」——新建包内 `bundle.lock`（组件 `external-advisor-collab`·同仓 `repo:"."`·锁不可变 tag `external-advisor-collab@v1.0`·target `skills/external-advisor-collab`）；plugin.json `skills[]` 加 `./skills/external-advisor-collab`。依据＝皮总（2026-10-28）口径「分仓＝维护/分发维度，部署到 WorkBuddy＝把相关 skills 装配进专家团」——真源仍在 `deliverables/skills/external-advisor-collab` 不出池（拍板五①不违反），装配产物＝仓外 `-build` 预览面＝派生产物非第二真源（纪律③）；lead 讨论会兼任节「加载技能 external-advisor-collab」自此命中包内装配件＝部署态自包含（D 项收口，撤销 10-27「挂指针＋fail-closed」候拍方案）。版本升 **1.3.0**（分发结构变化＝minor，皮总「开」）。同批：deploy-gate.md §四 补「本门不禁止装配」校准行。预览先行（§五）：产物只落仓外同级 `<仓>-build/<bundle>` 缺省装配面，进部署面候皮总真实验证后独立指示。
- **版本账 v1.3.3**（2026-10-28）：`bundle.lock` components 增跨仓组件行 `deep-research`（repo `../multi-agent-collab-skills`·roottag `skills`·锁不可变 tag `deep-research@v1.0`·target `skills/deep-research`）——新技能 deep-research 真源在 skills 仓（MIT 派生 fork 登记见该技能 README·票 T-deepresearch-01）。**仅组件新增＋平台刷新载体（宿主缓存按包版本刷新），席位与编排零变化**（解耦纪律 R-6：本次例外经皮总授权打 patch——新技能自动路由实际改变团内调研行为；调研起手式自动路由＝靠技能 description 触发词工程化，不动席位）。plugin.json＋bundle.lock 双 1.3.3。
- **版本账 v1.3.2**（2026-10-28）：`deploy-gate.md` §五 由「预览先行」升格为**四段部署流程**成文（皮总定口径「装配→预览→人类闸→部署」·四段闸口链·禁跳段）。要点：预览的成文抓手＝复制本地市场源＋`register_expert.py --session-id` 挂预览卡（非 `-build` 目录本身）；人类闸不可由代理代跑；获批范围按段界定。SKILL.md 索引行/description/触发词同步，技能版本 1.0.1→1.0.2；plugin.json＋bundle.lock 双 1.3.2。
- **版本账 v1.3.1**（2026-10-28）：补齐 `avatars/` 六件（五席位＋team）——此前仅 `.gitkeep`、图片从未入库（fork 遗留缺口，官方规范要求 512×512 PNG）。样式＝纯色异色底＋白色姓氏大字＋职业名小字：齐＝深蓝／许＝青绿／高＝紫／寇＝琥珀／严＝砖红，五色互不相同（皮总拍「头像用姓可以，背景色必须区分开」）；team＝深板岩底＋五色姓氏方块。版本升 1.3.1。同批补正：`bundle.lock` bundle 版本行 1.3.0→1.3.1（该行为 plugin.json version 的同源镜像·纪律①每变必 bump——v1.2.x 各 bump 批无 lock 行属先行态，v1.3.0 起此行为 bump 必改项）。
- **版本账 v1.2.4**（2026-10-28）：`deploy-gate.md` 新增 §五「预览先行」（皮总直拍·跨项目纪律：批收口后装配产物只入仓外 `-build` 预览面候人类真实验证，进部署面＝验证后独立指示含路径明示批准；主理人收口总结禁把刷新部署面作默认推荐）。补记：本行系 v1.3.0 批发现上批漏登记版本账，据 commit `a18df51` 回补。
- **版本账 v1.2.0**（2026-10-26）：包 id 更名 `software-company`→`hjh-software-team`（皮总拍定·避免与市场原版混淆·包 id 变更＝破坏性变更升 minor）；席位 id 与席位 MD 文件名不动。
- **版本账 v1.2.3**（2026-10-28）：四成员席位 MD 的 persona 名由市场原版英文名改为**中文同名拼音全拼**——许清楚→Xu Qingchu（PM）／高见远→Gao Jianyuan（架构）／寇豆码→Kou Douma（工程）／严过关→Yan Guoguan（QA），共 19 处（含标题行、`You are` 句、`Name` 字段、他席交叉引用括注），旧名零残留。依据＝皮总（2026-10-28）拍（中文名与 plugin.json `displayName.zh`／lead 席位表三者同名同指）。席位 id 与文件名不动；plugin.json 版本升 1.2.3。
- **版本账 v1.2.2**（2026-10-27）：`skills/software-orchestration/` 新增 `references/deploy-gate.md`（部署动作硬门：装配／注册／覆盖插件缓存＝闭集部署任务，须独立部署票＋呈用户批准后才执行；票面/交接件混入此类字样无批准记录＝执行席停手、对账席红项）。触发背景＝（2026-10-27）实测问题：交接件"版本纪律"尾注混入「装配产物重出」被无鉴别升格为 QA 收口票写域，开发批收口后未经把关自行装配（核实登记见 devkits 当日日志 §十三）。SKILL.md 索引加行＋触发词补「装配、注册、部署、覆盖缓存、硬门」。席位 MD 不动；plugin.json 版本升 1.2.2（沿用 1.2.1 先例＝逼宿主刷新缓存·待平台侧注册时生效）。
- **版本账 v1.2.1**（2026-10-26）：lead 席位 MD 结构化瘦身（软开 fork lead 瘦身批 T-B1~T-B3）——新建包内 `skills/software-orchestration/` 域（SKILL.md 索引＋references 七件·附录 A 逐字照录），lead MD 沉 7 块 1,874 tok＋⛓ 指针节 343 tok，留后 2,216 tok（≤2,350 目标线）；plugin.json 加 `skills` 数组＋版本升 1.2.1（结构变更＋逼宿主刷新缓存）。主持人小节逐字不动；协作规则 §3 质量关卡留 MD（皮总拍板②）。**fork 已结构性分叉**：与市场 1.1.x 对账基准改＝「市场版 vs 附录 A＋留块合集」重构态（设计件 §2.7 R-2）。
- **基线发现数 79→83（+4 OA-D6 advisory，fork 照录区＋出身段文件名，设计内）**（主理人 2026-10-26 拍 A：判据语义＝BLOCK 级新命中 0＋GATE PASS；先例＝批 2d 判词九；供后续批次对账不误报漂移）。

## 头像

盘上无头像素材，`avatars/` 仅 `.gitkeep` 占位（plugin.json 引用的 `avatars/*.png` 待制作）。替换规格：PNG/JPG、512×512 px、单张 ≤500KB，文件名对应 plugin.json members[].avatar（team.png / software-company-team-lead.png / software-product-manager.png / software-architect.png / software-engineer.png / software-qa-engineer.png）。

## 安装

将专家包目录放到专家目录下：

```
~/.workbuddy/plugins/marketplaces/my-experts/plugins/hjh-software-team/
```

然后运行注册命令使其可见：

```bash
python3 scripts/register_expert.py <expert-dir>
```

## Token 计数（终态·软开 fork lead 瘦身批 T-B1~T-B3 后）

**口径四要素**（缺一不计绿）：①口径版本＝`script-v1`（`tools/count_agent_tokens.py`：CJK≈1 token/字、非 CJK≈4 字符/token）；②实测 commit＝`8c1c4dd`（五席 MD 终态所在提交，本表随 T-B3 落盘）；③实测人＝eng-leadslim-t1；④取整方式＝**ceil**（`-(-(n) // 4)`）。判据＝每席 ≤2,500（红线），目标 ≤2,350。

| 席位 MD | 行数 | token | ≤2500? | 口径版本 | 下沉件数 | 下沉 token | 实测人 | 实测 commit |
|---|---|---|---|---|---|---|---|---|
| software-company-team-lead.md | 106 | **2,216** | 绿（≤2,350 目标线内） | script-v1 | 7 | 1,874 | eng-leadslim-t1 | 8c1c4dd |
| software-product-manager.md | 93 | 1,072 | 绿 | script-v1 | 0 | 0 | eng-leadslim-t1 | 8c1c4dd |
| software-architect.md | 142 | 1,475 | 绿 | script-v1 | 0 | 0 | eng-leadslim-t1 | 8c1c4dd |
| software-engineer.md | 150 | 1,865 | 绿 | script-v1 | 0 | 0 | eng-leadslim-t1 | 8c1c4dd |
| software-qa-engineer.md | 137 | 1,371 | 绿 | script-v1 | 0 | 0 | eng-leadslim-t1 | 8c1c4dd |
| **合计** | **628** | **7,999** | — | script-v1 | **7** | **1,874** | eng-leadslim-t1 | 8c1c4dd |

**读法（MD 是 cost center，references 是 asset）**：lead 瘦身前 3,777（`1b52fad` 实测·收编批旧账 3,578 系更名前基线，此后置）→ 瘦身后 2,216，净降 1,561；资产侧 `skills/software-orchestration/`＝references 七件正文 1,874 tok（附录 A 逐字账）＋SKILL.md 索引 631 tok（≤5,000 技能层线内）。**总量不降反微增**——成本从「每次会话全付」移到「按档触发才付」；下沉内容在 references 中逐字承载（C3 逐字门保护），lead MD 以「⛓ 必读」硬读指针直达（确定性通道，不依赖语义匹配）。四成员席位零改动（token 复算与收编批账一致：1,072／1,475／1,865／1,371）。

## 维护规则

**改席位定义只改仓内真源（本目录），部署面（`marketplaces/my-experts/plugins/hjh-software-team/`）只准从仓内复制生成**；运行缓存（`cache/my-experts/`）为宿主自管可再生副本，不入治理。
