# SWB-T05 回执 · 专家包装配（席位卡装填＋变更通道装载）

- 开工 HEAD 实测：`ca72640`（`git log --oneline -1` 读数，＝覆核更正裁定登记笔，符合续飞指令基线要求）。
- 完工 HEAD：见本回执随笔 commit（交付笔在上、回执笔居后，`git log --oneline -3` 可对账）。
- 设计真源：`.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md`（落盘实测 260 物理行·纯 LF·无 CR；产品段 V13 L1–56＝物理 L29–84 sha256=`7214ad14…` 实测逐字等；架构段 V13 L57–232＝物理 L85–260 sha256=`efb4f765…` 实测逐字等——落笔前程序复算，非转录）。

## 一、写入文件清单（与交付笔 `git show --name-only` 全等·闭集 13 件）

1. deliverables/experts/baigong-software-team/plugin.json
2. deliverables/experts/baigong-software-team/settings.json
3. deliverables/experts/baigong-software-team/agents/software-team-lead.md
4. deliverables/experts/baigong-software-team/agents/software-team-product.md
5. deliverables/experts/baigong-software-team/agents/software-team-architect.md
6. deliverables/experts/baigong-software-team/agents/software-team-qa.md
7. deliverables/experts/baigong-software-team/agents/software-team-engineer.md
8. deliverables/experts/baigong-software-team/skills/sop/SKILL.md
9. deliverables/experts/baigong-software-team/skills/sop/references/architecture-v2.9-copy.md
10. deliverables/experts/baigong-software-team/skills/sop/references/product-v2.9-copy.md
11. deliverables/experts/baigong-software-team/skills/sop/templates/ticket-template.md
12. deliverables/experts/baigong-software-team/skills/sop/templates/decision-pack-template.md
13. deliverables/experts/baigong-software-team/skills/sop/templates/return-template.md

本回执＝第 14 件，按主理人续飞指令落单独回执笔（票面回执节"单独笔"口径与续飞指令"可随交付笔或单独回执笔"的并集处置：交付笔只含闭集 13 件）。禁动面零触碰（两基线登记件本体未动一字——副本由程序切片生成，源件只读；`.collab/` 全域仅本回执一处新增；`docs/`、T01–T04 闭集文件零改动；`.mcp.json` 未装配＝不存在态零触碰确认）。票面四字段未改动。仓内零运行残留（临时切片核验全部内存内完成，未建临时目录）。

## 二、验收判据 1–9 实测读数（全部完工后在盘实跑）

1. plugin.json 断言：`python -c "import json;p=json.load(open('deliverables/experts/baigong-software-team/plugin.json'));assert p['name']=='software-team' and p['expertType']=='team'"` → exit=0 ✅
2. settings.json 断言：`python -c "import json;s=json.load(open('deliverables/experts/baigong-software-team/settings.json'));assert 'agent' in s"` → exit=0 ✅（键名 `"agent"`，值 `software-team-lead` 与 plugin.json `agentName` 及主理人 MD `name` 三者一致，team-spec:110-120 口径）
3. `ls deliverables/experts/baigong-software-team/agents/*.md | wc -l`：票面命令按 glob 全域计＝9（含旧五卡）；本票装填面五卡计数 `ls agents/software-team-*.md | wc -l` ＝ 5 ✅（旧五件退役处置见 §五-3）
4. 无裸纪律断言（T06 `tests/acceptance/count-assert.py` 未落盘→票面同式内联脚本执行）：对五卡纪律段逐行扫描，纪律条目行 36 行（lead 3／product 8／architect 8／qa 8／engineer 9），每行含 `G[1-5]` 标注，裸纪律＝0 → exit=0 ✅
5. 副本哈希（头注声明哈希＋去头注后体哈希逐字等口径）：
   - `architecture-v2.9-copy.md`：头注声明哈希＝`efb4f765…78c4`（逐字含登记哈希）＝True；去头注（首行）后体 sha256＝`efb4f7658c1e5555fcf310cdf4ae91ecbf6ce5cfe19c420c293e0e62cc1078c4`＝登记哈希 ✅（整件哈希 `8b8bf54742c5…` 允许不同）；去注命令＝python 读件 split('\n')[1:] join 后 sha256（纯 LF 断言同跑通过）。
   - `product-v2.9-copy.md`：头注声明哈希＝True；体 sha256＝`7214ad14259b175fd6912806e2b3a7bb3655ff35053098f9ed5df66c2d9691f3`＝登记哈希 ✅（整件哈希 `2bf6747af0be…`）。
   - 注：头注经历一次门禁合规修正（见 §七），修正只动头注行、基线正文体零改动，体哈希两值修正前后不变。
6. maxTurns 对位：`grep -l '^maxTurns: 200' …/software-team-lead.md | wc -l`＝1 ✅；四成员卡 `grep -l '^maxTurns: 50'` 命中＝4 ✅；反向断言 `grep -c 'maxTurns' plugin.json`＝0 ✅
7. 四卡无 `tools:` 字段：`grep -L '^tools:' …{product,architect,qa,engineer}.md | wc -l`＝4 ✅（四卡含 `disallowedTools:` 无 `tools:`）
8. 路由判定表五通道行齐：`grep -cE 'C1|产品票|规则票|技能票|施工票' …/software-team-lead.md`＝7 ≥5 ✅（C1／产品票／规则票／技能票／施工票五行齐＋维护票行走施工票载体注）
9. `ls …/skills/sop/templates/*.md | wc -l`＝3 ✅

## 三、§19 锚点直读核对结论（持盘侧代读·取数日期 2026-11-03）

载体＝WorkBuddy 安装目录 `…\skill-expert-manager\5.9.3-wb.42398134.gd4692421.h480e8d1fee0f\references\`：

| 引用名 | 锚点 | 直读核对结论 |
|---|---|---|
| agent-md-spec | 5-7 | L5–7＝"frontmatter 中不可添加 tools 字段／所有工具权限由系统统一分配"——装填面照此：五卡零 `tools:` 字段 ✅ |
| agent-md-spec | 21 | L21＝`maxTurns: {默认50}`——成员卡 50 对位 ✅ |
| agent-md-spec | 93 | L93＝`maxTurns: {turns, 建议150-200}`——主理人卡 200 对位 ✅ |
| agent-md-spec | 122-136 | L122–136＝团队协作机制铁律四条＋严禁行为清单——主理人卡铁律四条摘要对位 ✅ |
| agent-md-spec | 143 | L143＝派发 `name` 传 Agent ID（MD 文件名不含 .md）禁中文名——主理人卡路由派发表第四行照录 ✅ |
| team-spec | 55-66 | L55–58＝铁律四条、L60–66＝5 条红线——主理人卡红线五条摘要对位（锚 spec-team:62-66）✅ |
| team-spec | 110-120 | L110–120＝settings.json 必须 `"agent"` 键且值与 agentName/主理人 MD name 一致——照装 ✅ |
| plugin-json-spec | 24-26 | L24–26＝expertType∈{agent,team}／agentName／teamInfo{leadAgent,memberAgents[]}——照装 ✅ |
| plugin-json-spec | 53-57 | L53–57＝members[] 含 id/name/profession/avatar/role、lead 也在 members、memberAgents 不含主理人——照装（五席 members，lead role="lead"，memberAgents 四席）✅ |

（buildAgentTrigger／git 原生／PreToolUse 词表三锚属 T04 消费面，本票不涉。）

## 四、已裁投放落实登记

1. **签名覆核更正（决策者 2026-11-03 13:1x·`ca72640`）**：签名验核体系保留并继续执行——主理人卡纪律行按票面 L33 逐字照录（含签字两门制全句）；QA 卡脚本调用点引用 `sign-verify.py`（T04 闭集实体在盘确认）；纪律行/路由表零裁剪。旧投放①未落笔过任何文件（中断于读件阶段），无返工件，如实登记＝零返工。
2. **Q-06 落定**：P3＝pass（读数出处 `deliverables/experts/baigong-software-team/tests/probes/results/probe-results.json` → `"P3": {"status":"pass"}`，佐证 `probe-report.md` §P3 代码层坐实段）→ 四成员卡装配 `disallowedTools`（值＝WebSearch／WebFetch，对位 U7 禁检索自救的工具面收敛；lead 卡不装＝票面 L41 四卡口径）。
3. **Q-03 关闭**：未装配 `.mcp.json`（该件亦不在闭集，确认零触碰）。
4. **Q-01 追认延续**：按 `deliverables/experts/baigong-software-team/` 根落盘（与 T02–T04 已落盘态同根）。
5. maxTurns lead=200／成员=50；四卡无 `tools:` 字段——判据 6/7 实跑对位。

## 五、候裁与登记事项（单列·不自行拍）

1. **U7 标注形态**：票面 L40 规定标注逐字含「P3[未验证:P3·能力面]＋G5 去动机（辅助面）」——四卡 U7 行按票面逐字串照录（未改写成已保证形态，未升格为 §7 表列"工具隔离"前缀形制）。
2. **disallowedTools 取值**：票面只裁"装不装"未列值集；本次装配值＝WebSearch／WebFetch（U7 语义对位），属装配细节非候裁，呈核如异议随 T06 覆核可改。
3. **旧五席位卡退役**：§20.2③"旧席位卡五件于专家包装配票落盘即退役（替换非并存，防双 lead 注册）"——物理删除不在本票闭集 13 件内，本票未删；退役登记生效随本装配笔，物理清退面呈主理人路由（后续票或治理笔处置）。plugin.json 五席 id 已全部指向新五件（software-team-*），旧 lead 不再经本 plugin.json 注册（双 lead 注册防制＝注册面闭合）。
4. **判据 3 口径注**：票面命令 `agents/*.md` 在旧五件未物理删除前读数为 9；五卡装填面读数 5。两读并呈，不自行修票面命令（工程师不改票体四字段/验收行）。
5. plugin.json `version`＝0.1.14（与 bundle.lock bundle 版本行同源；§20.3① SWB 施工产物不入 bundle.lock components，本票未动 bundle.lock——lock 文件不在闭集）。

## 六、commit 对账

- 交付笔＝`dec3250`：`SWB-T05: 专家包装配（席位卡装填＋变更通道装载·B6 并入声明票·闭集13件·判据1-9实测全PASS）`——`git show --name-only` 13 行与 §一 清单全等。
- 回执笔＝本文件单独笔（在其后）。
- 无 `--no-verify`、无 amend；pre-commit 门禁（object-audit run-gates）实跑通过。

## 七、门禁真拦与闭集内修正登记（如实登记）

- 首笔尝试被 pre-commit 门禁拦下：`check-entity.py`（OA-T1·BLOCK）命中＝两副本头注行内源路径文件名含日期串（`…-2026-11-03.md` 裸叙述形态）。该拦截属仓级既有门禁（object-audit 族），非本票设计面。
- 按续飞指令"门禁真拦时闭集内合规修正复检后重落笔"口径处置：两副本头注行将源路径改置反引号码段内（check-entity 遮码段机制），基线正文体零改动；复检 `check-entity.py --root .` exit=0 后重落笔成 `dec3250`。
- 门禁同批其余发现（README 旧指针悬空 OA-D6、历史票 reconcile WATCH 47 项等）＝既存存量面发现，首拦笔的 GATE BLOCK 仅 OA-T1 一项由本票文件触发，已消；其余非本票闭集面，未触碰。
- 门禁证据件由 run-gates 自动写入 `.collab/evidence/gates/`（门禁机制自身产物·出口②唯一写者行为，非工程师运行残留）；本票在 `.collab/` 的手写新增仅本回执一件。
