# T-deepresearch-01 施工回执（deep-research v1.0 建件·仓内登记）

- 席：software-engineer（寇豆码）·票 T-deepresearch-01
- 施工依据：devkits 仓 .collab/research/ 下「2026-10-28-设计方案v2-deep-research施工蓝本」（R-1~R-6 已拍板·裁定语义见 .collab/decisions/ 下同日皮总拍板件）
- 日期：2026-10-28

## 〇、开工 HEAD 实测读数（串行环境·唯一在飞席）

| 仓 | 开工 HEAD | 收口 HEAD |
|---|---|---|
| multi-agent-collab-skills | `8733bb4d4b5c571a358b6b1daea60d7ea7b1d4e4` | `3a087a3110991dd52ad02b589fa5c6b38b0d0ace` |
| multi-agent-collab-devkits | `ba8453a6cc570fbccace9ef160d337f51dbb0d56` | `b0c116349c77cb4b666bee0552fc33e5a28b4280` |

开工基线门禁预跑：skills 仓 run-gates exit 0（SOT 双根·BLOCK 0）；devkits 仓 run-gates GATE PASS exit 0。

## 一、skills 仓交付物闭集（真源 `skills/deep-research/`·11 件）＋token 实测（script-v1）

| 文件 | token | 线 |
|---|---:|---|
| SKILL.md | **2397** | ≤5000 ✓（MC-SKILL-LINE） |
| README.md | 1045 | MIT 派生登记四要素齐（原作 URL／hash 66e02d23642f0c63ccb07b46a88104eade402d44／克隆日期 2026-10-28／升级清单八条）＋MIT 义务声明 ✓ |
| references/methodology.md | 1614 | ≤2500 ✓（三关／措辞分级／矩阵节／context 三桶／可推翻条件） |
| references/quality-gates.md | 1280 | ≤2500 ✓（Gate 0–5＋评分卡节·启用条件＝full/high-stakes） |
| references/notes-format.md | 921 | ≤2500 ✓（五段体例＋数据卡体例＋矩阵数据卡体例） |
| references/domains/software-tech.md | 1278 | ≤2500 ✓（九段·剥 CLI·十二段负面必含·Radar） |
| references/domains/market-competitor.md | 1363 | ≤2500 ✓（九段·TAM/SAM/SOM 红旗·七层 so-what·同源去重） |
| references/domains/film-tv.md | 1617 | ≤2500 ✓（九段·数据卡全格式位＋「待验证」·无预置行业数字） |
| references/domains/_new-domain-template.md | 1291 | ≤2500 ✓（九段自建＋自建质检清单·去环境耦合件） |
| scripts/verify_citations.py | 2737 | MIT 派生头注登记（原作仓／hash／克隆日期／派生改造三条目） |
| evals/routing-evals.json | 1245 | JSON 合法；should=10／should-not=10（含 2 条弱信号标注）；中文起手式覆盖：帮我调研/行业分析/赛道/竞品/选型/政策/综述/值不值得做/转行入行/续轮 delta/英文 memo |

frontmatter：`name: deep-research`＋`version: 1.0`＋description 含调研起手式话术与反向清单（体例照仓内 aigc-video-* 头部·含 `agent_created: true`）。

## 二、门禁读数

- **skills 仓**：`bash tools/run-gates.sh` → SOT 双根对账（95 文件＝agents 7＋skills 88，新面含 deep-research 全部 9 个 .md）｜BLOCK 0（新命中 0）｜deep-research 相关发现 0 条｜**exit 0**
- **devkits 仓**：`bash deliverables/skills/object-audit/scripts/run-gates.sh` → GATE PASS（发现 350 条均 advisory 存量 WATCH·与开工基线同量，新增零）｜**exit 0**
- 证据件 ANCHOR：devkits `.collab/evidence/gates/2026-10-28-check-source-of-truth-findings350-at13-29-27.json`（exit 0）
- 未绕钩、未改门禁（ALLOW_GATE_DOWN 未使用；门禁脚本零改动）。

## 三、两仓 commit／tag 读数

- skills 仓 commit：`3a087a3`「deep-research v1.0 建件·fork 登记（票 T-deepresearch-01）」（11 files, +1028）
- skills 仓 tag：`deep-research@v1.0` → 指向 `3a087a3110991dd52ad02b589fa5c6b38b0d0ace`（不可变·此后升版走新 tag）
- devkits 仓 commit：`b0c1163`「软开团 v1.3.3：bundle.lock 增跨仓组件 deep-research@v1.0（skills 仓真源·MIT fork 登记随件 README）·仅组件新增＋平台刷新载体·席位与编排零变化（R-6 解耦·票 T-deepresearch-01）」（3 files：bundle.lock 组件行＋版本 1.3.2→1.3.3／plugin.json version 1.3.3／README 版本账 1.3.3 行注明「仅组件新增＋平台刷新载体，席位与编排零变化」）
- devkits 未跑 --assemble、未碰市场源/缓存（②③④段属主理与人类闸）。

## 四、红线 grep 自证清单（deep-research 目录全域·大小写不敏感）

| 模式 | 命中 |
|---|---:|
| tianyancha | 0 |
| inference.sh | 0 |
| qingyan | 0 |
| market-research-reports | 0 |
| curl | 0 |
| 带盘符绝对路径（正则 `[A-Za-z]:[\\/]`·排除 URL） | 0 |

引用四件套＝指针 external-advisor-collab references/30-discipline 第五节（只指不搬）✓；证据标签闭集五标英文＋措辞分级在位✓；领域九段体例四文件统一✓。

## 五、验收判据自查（蓝本 §四 1–6；第 7 判据 assemble 属主理后续段）

1. skills 仓 run-gates exit 0＋SKILL.md 2397≤5000 ✓
2. 路由表指向闭集内文件零悬空（SOT A2 对 deep-research 零发现；SKILL.md §三 四行指针全部实存）✓
3. verify_citations.py 样例跑通：坏样例（悬空 [5]＋缺目＋编号断档）→FAIL exit 1；干净样例→PASS exit 0 ✓
4. 吸收六件 grep 在场：保鲜期 7 处／口径关·三角关（三关）／共识·存在分歧·个人推测／强信号·弱信号／`_new-domain-template` 路由行／矩阵字段表·逐格三标 ✓
5. 剥离红线零命中（见§四）✓
6. README 四要素＋MIT 声明齐（见§一）✓

**IS_PASS＝YES**（判据 1–6 全绿；7 待主理段 assemble）

## 六、遗留事项

1. **判据 7（主理段）**：devkits `--assemble` exit 0＋manifest 记数＋预览卡——属主理与人类闸②③④段，本票未跑。
2. **plugin.json skills[] 数组未加 `./skills/deep-research`**：该行为装配（assemble）产物注册面——external-advisor-collab 先例中 skills[] 行与装配同步；本票按「不跑 assemble」纪律未预加，主理段装配时应由装配步带上（登记于此防漏）。
3. **视频团 bundle 引用行**：蓝本明示另票候补（experts 仓侧），未做。
4. skills 仓 autocrlf 提示（LF→CRLF）：与仓内既有行为一致，无 .gitattributes 干预，不影响门禁。
5. 施工偏差登记（零设计决策改动）：README 变更记录内两处蓝本文件引用改为仓内目录＋文件名描述写法（避 drive-path 门禁前车之鉴），语义等价。
