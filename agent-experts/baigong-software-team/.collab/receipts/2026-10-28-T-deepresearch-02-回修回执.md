# T-deepresearch-02 回修回执 · deep-research 收尾（QA 判词后回修单）

- 票号：T-deepresearch-02｜执行席：寇豆码（software-engineer）｜日期：2026-10-28
- 上游依据：devkits 仓 `.collab/evidence/2026-10-28-QA-deepresearch-01-判词.md`（有条件通过·8/8 实体 PASS）
- 改动性质：全部登记面/文案级，零设计决策改动。

## 开端·两仓 HEAD 实测读数

| 仓 | 实测 | 读数 |
|---|---|---|
| skills 仓 | `git log --oneline -1` | `3a087a3 deep-research v1.0 建件·fork 登记（票 T-deepresearch-01）`；`git describe --tags`＝`deep-research@v1.0`；工作区干净 |
| devkits 仓 | `git log --oneline -1` | `b0c1163 软开团 v1.3.3：bundle.lock 增跨仓组件 deep-research@v1.0…`；`git status --porcelain` 含 `M workbuddy/hjh-software-team/.codebuddy-plugin/plugin.json`（＝QA major-1 所指未提交行） |

## 逐修点前后对照

### major-1（放行装配段前提）— 已收口
- 文件：devkits 仓 `workbuddy/hjh-software-team/.codebuddy-plugin/plugin.json`（skills[] 段）
- 前：工作区已改未提交（`git diff` 显示 `+ "./skills/deep-research"`，HEAD `b0c1163` 内仅两行）
- 核对：增行内容正确（三行＝software-orchestration／external-advisor-collab／deep-research），与 bundle.lock target `skills/deep-research` 对位
- 后：补提交 **`d3715a7`**（信息含「plugin.json skills[] 补登 ./skills/deep-research·QA major-1 收口」·注明 R-6 仅注册行·随 b0c1163 同票）

### minor-a＋minor-b（SKILL.md §七 四件套句）— 已收口
- 文件：skills 仓 `skills/deep-research/SKILL.md:69`
- 前：`**四件套**：外部引用须带 文件名／日期／条款位置／可访问 URL，缺任一件该参照不承重——细则真源见 external-advisor-collab 技能 references/30-discipline 第五节（只指不搬，不复制正文）。`
- 后：`**四件套**：引用四件套条款以 external-advisor-collab 技能 references/30-discipline.md §五为真源，本处只指针不复制（要素构成、缺件不承重、补交逾期降格等细则一律以该节为准）；本技能 §七-三关/hard fail 为其调研产物面加严延伸。`
- 效果：近逐字摘要句删除改纯指针语义（minor-b）；指针补 `.md` 后缀（minor-a）；文内零带盘符路径（drive-path 检查 0 命中）。
- 附带：SKILL.md:5 frontmatter `version: 1.0`→`1.0.1`（与组件 tag 同源 bumped）。

**变形点登记（已报主理并获核准·2026-10-28）**：
- 现象：minor-a＋minor-b 合并修好后（指针语义＋`references/30-discipline.md` 带 .md 加反引号），skills 仓门禁 run-gates.sh 出 BLOCK 1（新命中 1）exit 1＝`skills:deep-research/SKILL.md:69 BLOCK MC-SOT-2 指针悬空 references/30-discipline.md → 包根/所在目录/技能真源根多探均不存在`。
- 原因：check-source-of-truth.py A2（MC-SOT-2）对反引号内带 / 的 .md 路径做四探针可达性（bundle 根/所在目录/技能真源根/剥 skills/ 前缀），无跨仓探针；30-discipline.md 真源在 devkits 仓 deliverables 面，从 skills 仓扫描面天然不可达＝被判悬空。既有豁免通道（tools/sot-external-provenance.txt 白名单）仅适用「来源标注／源＝」产地注记行，改白名单＝改门禁，违本票硬约束。原 v1.0 该行不被拦＝指针为纯文本无反引号，POINTER_RE 不匹配。
- 处置（主理核准口径）：该路径保持**纯文本不带反引号**（与 v1.0 该行原形态同构），语义句式与 `.md` 后缀按票面一字不动，门禁零改动恢复 exit 0。主理核准理由①＝跨仓真源指针在 skills 仓扫描面天然不可达属门禁探针已知边界（A2 四探针无跨仓项），纯文本无包反引号写法与本仓既有跨仓指针先例（「真源在该包只指不搬」类表述）同构，不属绕钩——POINTER_RE 不匹配是形态约定不是豁免通道滥用；②此形态（纯文本＋语义句式）定为跨仓指针通例（主理收进项目记忆）。
- 未采备选：B＝路径入白名单（改门禁，弃）；C＝裸基名 `30-discipline.md` 加反引号（转 WATCH 但指针不精确且新增 WATCH 噪音，弃）。

### minor-c（中英混排文风）— 顺手修
- 文件：skills 仓 `skills/deep-research/references/methodology.md:16`
- 前：`2–4 席为宜， rarely 超 5；` → 后：`2–4 席为宜，极少超过 5；`

## 修后账目读数

### skills 仓
- 新 commit：**`d43bfd1`**（deep-research v1.0→v1.0.1：QA minor 收口…）
- 新不可变 tag：**`deep-research@v1.0.1`** → `d43bfd1bede17ec3cd803f732f44019d6ec33dc2`；旧 tag `deep-research@v1.0` → `3a087a31…` 保留不动（`git tag -l` 两 tag 在场）
- 门禁：`bash tools/run-gates.sh` → **exit 0**；ANCHOR＝`check-source-of-truth: 模式 dual｜文件 95（agents 7＋skills 88）｜BLOCK 0（新命中 0）｜基线豁免 56（WATCH·键＝文本＋文件集合）｜指针 WATCH 294｜exit 0`
- token 复测（口径四要素：script-v1＋被测 commit `d43bfd1`＋实测人寇豆码＋ceil）：`python tools/count_agent_tokens.py …/SKILL.md` → **OK 2416 ≤ 5000** ✓（methodology.md＝1615 顺登）

### devkits 仓
- 新 commit：**`d3715a7`**（major-1 补提交）＋**`ea37b64`**（bundle.lock＋README 回修账），紧邻两 commit、均基于 `b0c1163`
- bundle.lock 组件行：ref `deep-research@v1.0`→`deep-research@v1.0.1`，note 追加修因一行（QA minor-a/b/c 收口·票 T-deepresearch-02）
- README 版本账 v1.3.3 行内追加注记：「组件 deep-research 锁 tag v1.0→v1.0.1＋plugin.json skills[] 补登提交入库（QA major-1 收口）」
- 门禁：`bash deliverables/skills/object-audit/scripts/run-gates.sh` → **exit 0**；ANCHOR＝`GATE PASS（发现 350 条，均按路由表走②不拦提交）`＋SOT 行 `BLOCK 0（新命中 0）… exit 0`
- 未跑 `--assemble`、未碰市场源/缓存/预览面（装配段留主理后续·minor-d 候补项照旧）

## 收尾核验
- 两仓 commit 时前置钩子门禁均过（devkits 两次 commit 钩子输出 `GATE PASS`；skills 仓 commit 后复跑 run-gates exit 0）；未改任何门禁脚本/白名单/钩子。
- 两仓工作区被跟踪文件均干净（skills `git status --porcelain` 空；devkits 无未提交跟踪改动）。

## IS_PASS

**IS_PASS = YES** —— major-1／minor-a／minor-b／minor-c 全部收口；minor-d（--assemble＋manifest 记数）按票面留装配段。HEAD 口径注册面三行就位，装配段可放行。
