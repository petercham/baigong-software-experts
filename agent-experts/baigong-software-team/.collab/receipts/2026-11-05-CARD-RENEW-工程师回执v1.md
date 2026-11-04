# CARD-RENEW 工程师回执 v1（工程师席·eng-card1）

- 票面＝`agent-experts/baigong-software-team/.scratch/tickets/2026-11-05-CARD-RENEW-卡片换代与席位命名换代施工票.md`
- 开工 HEAD 实测＝`5c7c4cc`（`git rev-parse --short HEAD`，开工帽头读数）
- 施工 commit＝`3c38fef`（`feat: CARD-RENEW 卡片与席位命名换代 0.1.23（票面T1-T8逐字照录）`，pathspec 限定提交，pre-commit 钩子放行 GATE PASS）
- 回执 commit＝本笔（`collab:` 前缀，落盘本件）
- 完工 HEAD＝回执 commit 后 HEAD（本笔入库后 `git rev-parse --short HEAD` 读数见下方「六、HEAD 链」）

## 一、完整写入/修改/改名文件清单（21 件·与施工 commit `3c38fef` name-only 清单全等）

改（16）：

| # | 文件 |
|---|---|
| 1 | `agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json` |
| 2 | `agent-experts/baigong-software-team/plugin.json` |
| 3 | `agent-experts/baigong-software-team/bundle.lock` |
| 4 | `agent-experts/baigong-software-team/agents/software-team-lead.md` |
| 5 | `agent-experts/baigong-software-team/agents/software-team-product.md` |
| 6 | `agent-experts/baigong-software-team/agents/software-team-architect.md` |
| 7 | `agent-experts/baigong-software-team/agents/software-team-engineer.md` |
| 8 | `agent-experts/baigong-software-team/agents/software-team-qa.md` |
| 9 | `agent-experts/baigong-software-team/skills/software-orchestration/references/standard-sop.md` |
| 10 | `agent-experts/baigong-software-team/skills/software-orchestration/references/quick-mode.md` |
| 11 | `agent-experts/baigong-software-team/skills/software-orchestration/references/bugfix-path.md` |
| 12 | `agent-experts/baigong-software-team/skills/software-orchestration/references/collab-rules.md` |
| 13 | `agent-experts/baigong-software-team/skills/software-orchestration/references/partial-workflows.md` |
| 14 | `agent-experts/baigong-software-team/docs/PRODUCT.md` |
| 15 | `agent-experts/baigong-software-team/docs/ARCHITECTURE.md` |
| 16 | `agent-experts/baigong-software-team/README.md` |

改名（5·`git mv`·R100 图像字节零动·old/new 双列）：

| # | old | new |
|---|---|---|
| 17 | `agent-experts/baigong-software-team/avatars/software-company-team-lead.png` | `agent-experts/baigong-software-team/avatars/software-team-lead.png` |
| 18 | `agent-experts/baigong-software-team/avatars/software-product-manager.png` | `agent-experts/baigong-software-team/avatars/software-team-product.png` |
| 19 | `agent-experts/baigong-software-team/avatars/software-architect.png` | `agent-experts/baigong-software-team/avatars/software-team-architect.png` |
| 20 | `agent-experts/baigong-software-team/avatars/software-engineer.png` | `agent-experts/baigong-software-team/avatars/software-team-engineer.png` |
| 21 | `agent-experts/baigong-software-team/avatars/software-qa-engineer.png` | `agent-experts/baigong-software-team/avatars/software-team-qa.png` |

回执自身＝`agent-experts/baigong-software-team/.collab/receipts/2026-11-05-CARD-RENEW-工程师回执v1.md`（回执笔，非交付笔，不入 21 件闭集）。

提交前自证：`git diff --cached --name-only | wc -l` ＝ 21；`git diff --cached --name-status -M` ＝ 16 M ＋ 5 R100（与上表逐行全等）。提交后自查：`git show --stat HEAD` ＝ `21 files changed, 153 insertions(+), 119 deletions(-)`＋五行 rename 100%；`git show --name-only --format= HEAD | wc -l` ＝ 21。未用 `git add -A`/`.`；未用 `--no-verify`/amend/reset。

## 二、A1–A8 逐条实测读数

### A1 旧花名归零＝绿
命令：`grep -roE "齐活林|许清楚|高见远|寇豆码|严过关" agent-experts/baigong-software-team/ --include="*.md" --include="*.json"`（包根 cwd 执行）
- 白名单外计数＝**0**。
- 白名单内残余（豁免·不判违例）：`README.md:61`（v1.2.3 史实行：许清楚/高见远/寇豆码/严过关 4 命中）——append-only 未回改。
- `.collab/**`、`.scratch/**`（本票面与历史票引用裁定原文）、git 历史面＝豁免射程内，未顺手清。
- 前值对照：施工前白名单外命中＝55。

### A2 旧职业标签归零（断言串口径）＝绿
断言串闭集＝`交付总监|Delivery Director|QA工程师|QA 工程师|QA Engineer|Software Architect|Software Engineer`，同 grep 口径：
- 白名单外计数＝**0**（`.collab/`、`.scratch/`、README 史实行、docs/SWB-交接件 之外全命中面为空）。
- 前值对照：施工前白名单外命中＝36。
- 裸「架构师」「工程师」「产品经理」按口径②/③不入断言串；候裁①现案（泛指席位简称不换）照票面执行：collab-rules L11–12、partial-workflows L10–12/L14、ARCHITECTURE L28、standard-sop 句尾主语（「架构师一次性输出」「工程师将」）零动。
- 三分账注记：「架构工程师／开发工程师／质量审计师」内部含「架构师/工程师」子串＝SUBSTR 不判违例。

### A3 新名成对在位（结构式判据）＝绿
逐席三文件读数（`grep -c`）：
- 注册卡 `.codebuddy-plugin/plugin.json`：包好用 2／姜通透 1／顾长远 1／柯会码 1／沈得严 1——包好用行外多一处＝T1.4 `defaultInitPrompt` 定稿句内联命中（结构判据＝members `displayName` 恰 1，经 JSON 解析核验 members 段内恰 1＝OK，行计数不作判据，票面 Y3 口径）。
- 包装卡 `plugin.json`：五名各 2（`name`＋`displayName` 双键）。
- 席位卡：frontmatter `zh: "<名>"` 恰 1 ＋ 正文标题行 `^# .* - <名>$` 恰 1，五席读数均 2（lead/product/architect/engineer/qa 各：1＋1）。
- profession 两卡＋席位卡成对：JSON 解析逐字段核验五席 `profession.zh/en` 在两卡 members 段全 OK（项目负责人/Project Lead、产品经理/Product Manager、架构工程师/Architect Engineer、开发工程师/Development Engineer、质量审计师/QA Auditor）；席位卡 frontmatter 两行按 T4 逐条落位。
- avatar：两卡新引用名各 5（计 10）＝`grep -c '"avatar": "avatars/software-team-' .codebuddy-plugin/plugin.json plugin.json` → 5/5；改名后文件在位：`ls avatars/` ＝ software-team-{lead,product,architect,engineer,qa}.png 五件 ＋ team.png（team.png 及其两卡引用零动）。

### A4 三同源同值＝绿
`grep -n '"version"' bundle.lock plugin.json .codebuddy-plugin/plugin.json`
- 前值实测：三处全 `0.1.22`（bundle.lock:5 / plugin.json:3 / .codebuddy-plugin/plugin.json:3）。
- 后值实测：`bundle.lock:5 "version": "0.1.23"` / `plugin.json:3 "version": "0.1.23"` / `.codebuddy-plugin/plugin.json:3 "version": "0.1.23"`——三读数全等＝0.1.23。
- JSON 合法性：三件 `json.load` 全过（JSON OK x3）。

### A5 门禁＝绿
`bash agent-skills/object-audit/scripts/run-gates.sh`（开票侧 find 实测路径＝票面所载实体在册）
- 施工前跑：exit 0，末行 `GATE PASS（发现 9015 条，均按路由表走②不拦提交）`。
- 施工后跑：exit 0，末行 `GATE PASS（发现 9015 条…）`——总数 9015→9015 零新增。
- 施工 commit 时 pre-commit 钩子同口径放行（输出 GATE PASS 9015）。
- 分段注记：check-ticket-reconcile 段内计数 147→171（全 WATCH·GATE 总数不变，系本票声明闭集 21 路径存在性态随施工翻转＋缺回执 WATCH 行，属该检查器对未收口态的预期读数；收口对账见 A7）。

### A6 引用闭环＝绿（缺省两包面读数不新增）
`python agent-skills/object-audit/scripts/check-pointer-closure.py`——为排多席共用工作区脏态干扰，前后值均在各自 commit 的**干净 detached worktree** 实测：
- 前态 worktree @`5c7c4cc`：`spec=OA-D6-3 count=534`／`spec=OA-D6-4 count=1174`。
- 后态 worktree @`3c38fef`：`spec=OA-D6-3 count=534`／`spec=OA-D6-4 count=1174`——**零新增**。
- 口径登记：当前工作区直跑读数 1057/2107 偏高＝本地被 .gitignore 遮蔽件（.scratch 票面包面等）进入扫描射程所致，两态 worktree 口径一致可比；F11 终式读数见 §四。

### A7 声明闭集对账＝绿（21 件全认·回执在位）
`python agent-skills/object-audit/scripts/check-ticket-reconcile.py --root . --ticket "agent-experts/baigong-software-team/.scratch/tickets/2026-11-05-CARD-RENEW-卡片换代与席位命名换代施工票.md"`
- 回执落盘前跑（预跑）：`票 1（对账 1／SKIP 缺声明 0）｜发现 1（全 WATCH）`——WATCH＝「票有声明闭集但回执指针解析不到（缺回执＝未绿项·证据缺）」，即判据所防的正是回执缺位态；声明闭集解析＝21 件全认（缺声明＝0，SKIP 0）。
- 回执落盘＋回执笔入库后复跑读数（回执笔 `f8088fa` 后实测）：`票 1（对账 1／SKIP 缺声明 0）｜发现 1（全 WATCH）｜exit 1`——对账登记 1、SKIP 0、声明闭集 21 件全认＝判据主体绿；残余 WATCH 行＝「票有声明闭集但回执指针解析不到」——原因＝票面 §自检与回执节只有「回执落 `.collab/research/`」目录级字样，无文件名级回执指针行（检查器 RECEIPT_TAIL_PTR_RE 需票内含反引号包裹的回执文件名指针），票面＝起草席职权、工程师无修票权不擅加，指针行补挂候主理人/起草席处置，如实呈报。

### A8 禁动面零扰动＝绿
- `docs/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md`：不在 `git show --name-only HEAD` 清单（21 件内无此件）＝零触碰；文件 sha256 前实测 `0275354f397e4bfd…` ＝ 后实测 `0275354f397e4bfd53f38da160637dfe67f3ce46a8d3e7a23399dbbed43495d8` 全等。登记件内 V13 三基线哈希登记行（全文 `3f335333…`／产品段 `7214ad14…`／架构段 `efb4f765…`）随行内容物理未动（该件 diff＝空）。
- commit name-only 清单（21 行）与票面声明闭集（21 行）全等：16 M 逐路径全等；5 改名按 old/new 双列对齐（声明行＝new 位，old 位为 `git mv` 源）。
- 席位 id／`agents/software-team-*.md` 文件名／`agents[]`／`teamInfo` 零动（diff 核验：两卡 agents[]/teamInfo 段无改动行）；`.collab/**` 交付性内容、`.archive/**` 零触碰；旧名白名单内未顺手清（A1 残余 4 命中即证）；新名未回补史实行。
- 装配面/部署面（`~/.workbuddy/plugins/` 全系）零触碰（本票未执行任何装配/注册动作，传导链①装配步候主理人排程）。

## 三、T 节施工对照（逐节落位声明）

- T1 七目：version/description/displayDescription/defaultInitPrompt/tags/quickPrompts(6 条)/members 整块逐字照录（JSON 解析＋git diff 复核）。
- T2 六目：version/description（＝T1.2 同串）/displayDescription（＝T1.3 同块）/tags（＝T1.5 同块）/quickPrompts（＝T1.6 同块）/members（name+displayName 双键同值，卡内顺序保持 lead/product/architect/qa/engineer 不重排）。
- T3：bundle.lock L5 版本行单行改动，其余行零动。
- T4 五目：五席位卡 frontmatter 姓名职业行＋标题行花名位，其余正文零动（五卡 diff 行数：lead 10／product 6／architect 10／engineer 10／qa 10＝与 T4 点名列严格一致）。
- T5 五卷：standard-sop 六处（L8/L15/L20/L31/L38 全行定稿含「质量审计师将」/L41）、quick-mode 两处、bugfix-path 三处、collab-rules L10、partial-workflows L13——全部按 occurrence 点名逐行替换，句尾泛指主语按口径②零动。
- T6 两件套：PRODUCT L8/L10/L48–52 行首格、ARCHITECTURE L15–19/L74–78 行首格——行其余格零动（diff 计数 PRODUCT 14／ARCHITECTURE 20 行，与点数目一致）。
- T7 五目：L3／功能三行／使用示例两行／头像节整段替换／版本账 v0.1.23 行追加于出身节版本账块现末行（基线发现数行）之后、「## 头像」节标题之前，体例照现行登记行。
- T8：五件 `git mv` R100（图像字节零动，diff 面 `Bin` 无内容差异）＋两卡引用 10 处随改名换代＋team.png 及引用零动；候裁⑥（图内旧姓大字错位）不施工、照票面登记呈报。

## 四、F11 过程痕迹终式读数

票面 F11 终式＝`见?第\s*\d+\s*轮|轮次戳|〔[^〕]*·轮〕|轮次号[：:]`。对回执本件跑该终式：实测读数＝**1**（＝§四自登记行自身含终式字面「轮次戳」＝自指命中，与票面自指行同型态；票面读数实测＝1 与票面预期 1 对上）。回执不改动票面凑数（H6 口径：预期与实测冲突按实测登记）。除此自指行外无过程痕迹命中。

## 五、偏差与如实申报

1. **回执落点偏差**：票面 §自检节写「回执落 `.collab/research/`」，主理人派发指令明示落 `.collab/receipts/2026-11-05-CARD-RENEW-工程师回执v1.md`——本回执按主理人指令落位，差异如实登记呈报（候裁不擅改，落点归主理人裁定追认）。
2. **候裁七目全部照票面现案执行、未裁项零动**：①裸职业简称不换；②lead profession.zh＝「项目负责人」；③两卡 description 统一新串；④README L3 与 PRODUCT L8 同新文（PRODUCT L8 用 T7.1 定稿句全文，Y1 同值口径）；⑤「测试」动词位不动；⑥头像画面文字错位登记不施工；⑦quickPrompts 备 6 条全保留（实删数＝0，宿主 5 槽实测留②预览段）；⑧头像改名按票面执行（改名 5 件成对，无回退触发）。
3. **A5 分段 WATCH 计数 147→171**：GATE 总数 9015→9015 不变、exit 0 放行，WATCH 增项＝本票声明路径存在性态翻转＋回执未落盘期 WATCH，非 BLOCK 级新增（判据语义＝BLOCK 新命中 0＋GATE PASS，先例＝README 基线发现数行主理人拍 A 口径）。
4. **A6 口径说明**：多席共用工作区含他席未提交脏态与 .gitignore 遮蔽件，前后对比采用两 commit 干净 worktree 同口径实测（见 A6），非工作区直跑值对比。
5. T 节定稿文本零改写、零异议；闭集外零触碰（施工 commit 恰 21 件即证）。

## 六、HEAD 链与完工读数

- 开工 HEAD＝`5c7c4cc`
- 施工 commit＝`3c38fef`（main）
- 回执 commit＝本笔 `collab: CARD-RENEW 工程师回执v1（A1-A8逐条读数·21件闭集全等）`（pathspec 限定＝本回执件一件）
