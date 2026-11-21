# QA-deepresearch-01 判词 · deep-research@v1.0 证伪导向独立验证

- 票号：QA-deepresearch-01｜验证人：严过关（software-qa-engineer·fresh eyes）｜日期：2026-10-28
- 验收蓝本：devkits 仓 `.collab/research/2026-10-28-设计方案v2-deep-research施工蓝本.md` §四（8 判据按任务票展开版）
- 纪律申明：全程未修改任何被验文件；自建样例全部置于 `D:/multi-agent-collab-devkits/.collab/tmp-qa/`；未复用工程师自测样例。

## 开端·两仓 HEAD 实测读数

| 仓 | 实测 | 读数 |
|---|---|---|
| skills 仓 | `git log --oneline -1` | `3a087a3 deep-research v1.0 建件·fork 登记（票 T-deepresearch-01）`＝预期 ✓；`git describe --tags`＝`deep-research@v1.0`；`git rev-parse deep-research@v1.0`＝`3a087a3110991dd52ad02b589fa5c6b38b0d0ace`（tag 正指向该 commit）✓ |
| devkits 仓 | `git log --oneline -1` | `b0c1163 软开团 v1.3.3：bundle.lock 增跨仓组件 deep-research@v1.0…`＝预期 ✓ |
| skills 仓工作区 | `git status --porcelain` | 空＝被验对象未被事后改动 ✓ |
| devkits 工作区 | `git status --porcelain` | **`M workbuddy/hjh-software-team/.codebuddy-plugin/plugin.json`（未提交改动·见判据 3/登记面异常）** |

## 逐判据三态判定

### 判据 1 — 两仓门禁 exit 0 → **PASS**
- skills 仓 `bash tools/run-gates.sh` → `SKILLS_GATES_EXIT=0`。ANCHOR 行：`check-source-of-truth: 模式 dual｜文件 95（agents 7＋skills 88）｜BLOCK 0（新命中 0）｜基线豁免 56｜指针 WATCH 294｜exit 0`；薄启动器汇总行：`run-gates(skills 仓薄启动器)：适用项 1（SOT 双根对账）｜exit 0`。
- devkits 仓 `bash deliverables/skills/object-audit/scripts/run-gates.sh` → `DEVKITS_GATES_EXIT=0`。ANCHOR 行：`GATE PASS（发现 350 条，均按路由表走②不拦提交）`。

### 判据 2 — SKILL.md token ≤5000 → **PASS**
- 口径申明（按脚本头注四要素）：口径版本 **script-v1**（CJK≈1 token/字、非 CJK≈ceil(/4)）＋被测 commit **`3a087a3`**＋实测人 **严过关（QA-deepresearch-01）**＋取整 **ceil**。
- 命令：`python tools/count_agent_tokens.py D:/multi-agent-collab-skills/skills/deep-research/SKILL.md` → `OK 2397`。2397 ≤ 5000 ✓。

### 判据 3 — 路由零悬空＋frontmatter＋触发词覆盖 → **PASS（附 minor 登记面异常）**
- 路由表指向文件存在性逐件实测（`[ -f ]` 循环）：methodology.md／quality-gates.md／notes-format.md／domains/{software-tech, market-competitor, film-tv, _new-domain-template}.md／scripts/verify_citations.py／evals/routing-evals.json ＝ **9/9 EXISTS，零悬空** ✓。
- frontmatter：`name: deep-research` ✓（SKILL.md:2）；`version: 1.0` ✓（:5）；description 触发词覆盖「帮我调研/行业分析/赛道/竞品/选型/政策/综述/值不值得做/入行/英文 research memo·literature review」＋Do NOT 反向清单＋弱信号先澄清 ✓（:3）。
- 抽 5 条 should 用例对照 description 话术：rt-01「帮我调研」✓／rt-02「行业分析」✓／rt-03「赛道＋值不值得进」✓／rt-04「选型」✓／rt-07「政策梳理」✓（另 rt-06「综述报告」、rt-08「转行入行」、rt-10「research memo」亦命中）。routing-evals should 10 条／should-not 8 条＋2 弱信号条＝20 条 ✓。
- **minor-a（登记面·HEAD 口径）**：SKILL.md 内 `references/30-discipline` 指针无 `.md` 后缀（真文件名 `30-discipline.md`·真位于 devkits 仓 deliverables 面），可解析但不精确。
- **major-1（登记面·HEAD 口径）**：见判据 8 前登记面核对——plugin.json `skills[]` 第三行 `./skills/deep-research` **不在 HEAD `b0c1163` 内，仅存在于工作区未提交改动**（详下方登记面核对）。

### 判据 4 — 吸收六件在场＋四件套只指不搬 → **PASS（minor-b）**
grep occurrence 口径（全树·含 README/references）：
| 件 | 命中 | 证据（文件:行·首处） |
|---|---|---|
| 保鲜期 | ≥7 处 | notes-format.md:66；film-tv.md:72；SKILL.md:61（STALE 定义挂保鲜期） |
| 口径关 | 1 处 | SKILL.md:71（三关①） |
| 三角（三角关） | 3 处 | SKILL.md:71（三关③）；quality-gates.md:31；README.md:17 |
| 共识·存在分歧·个人推测 | 各≥3 处 | SKILL.md:63；methodology.md:54-56；notes-format.md:62 |
| 强信号·弱信号 | 各≥2 处 | SKILL.md:24/26（§二标题+正文）；description:3 |
| _new-domain-template 路由行 | 2 处 | SKILL.md:37（路由表行）＋SKILL.md:44（按需清单） |

四件套只指不搬：SKILL.md:69 写「文件名／日期／条款位置／可访问 URL，缺任一件该参照不承重——细则真源见 external-advisor-collab 技能 references/30-discipline 第五节（只指不搬，不复制正文）」。对照 30-discipline.md §五（devkits 仓 :56-60）：四要素名称为摘要级复述，原条款其余细则（补交逾期降格、`30-formats.md §七 A-15` 联动、括注纪律、自报优于他查）**均未复制** ✓。
- **minor-b**：SKILL.md:69 四要素列举句与 30-discipline §五-2 核心句近逐字（「文件名／日期／条款位置／可访问 URL，缺任一件该参照不承重」）。按蓝本「只指不搬」从严读法可议为摘要越线一毫米；按「指针＋操作摘要」读法则合规。登记不判 FAIL。

### 判据 5 — 红线零命中 → **PASS**
deep-research 全树 grep（大小写不敏感·occurrence 口径）：
- `tianyancha`＝0／`inference.sh`＝0／`qingyan`＝0／`market-research-reports`＝0／`curl`＝0；
- 带盘符绝对路径（严格式 `\b[A-Za-z]:[\\/]` 去 http 干扰后）＝**0 处**；
- 附加面：`npm i|pip install|apt-get|brew install|npx |uvx` 安装面＝0 处（零第三方 CLI 佐证）。

### 判据 6 — verify_citations.py 独立样例测 → **PASS**
全部样例为 QA 自建于 `D:/multi-agent-collab-devkits/.collab/tmp-qa/`（example.* 虚构域，未复用工程师样例）：
| 样例 | 缺陷构造 | exit | 脚本判定 |
|---|---|---|---|
| bad-report-cited-noentry.md | 正文引 [3] 但参考文献无该条 | **1** | MISSING_REFERENCE（critical）FAIL |
| bad-report-outpool.md | 参考文献 URL 在来源池外 | **1** | INVENTED_URL（critical）FAIL |
| bad-report-gap.md | [1][3] 并用缺 [2] | **1** | 抓到（混合 MISSING_REFERENCE——因样例标题自含 `[2]` 字样被计入正文引用，QA 样例自身瑕疵，不影响 exit≠0 结论） |
| bad-report-gap2.md | 纯编号断档（标题无数字干扰） | **1** | NUMBERING_GAP（minor）仍 fail-closed ✓ |
| clean-report.md＋clean-sources.json | 干净（引用完整·池内·编号连续·占比≤25%） | **0** | PASS（0 issue 0 warning） |

≥1 坏样例（实为 3 个坏样例、覆盖悬空/池外/断档三类）exit 非 0 ✓＋干净样例 exit 0 ✓；fail-closed 语义含 minor 级断档也拦，符合头注③。

### 判据 7 — README 派生登记四要素＋MIT → **PASS**
README.md §MIT 派生登记表：①原作仓 URL `https://github.com/staruhub/ClaudeSkills`（:9）✓；②hash `66e02d23642f0c63ccb07b46a88104eade402d44`（:10，与任务给定值逐字符一致）✓；③克隆日期 2026-10-28（:10-11）✓；④升级清单八条（:14-23）✓。MIT 义务声明节（:25-27）含版权指向＋随分发保留义务＋按现状无担保 ✓。scripts/verify_citations.py 头注另有 MIT 派生登记（:3-11）✓。

### 判据 8 — 交叉抽读质量（证伪向）→ **PASS（minor-c/d）**
- **film-tv.md 零预置行业数字**：正则 `[0-9]+(\.\d+)?\s*(亿|万|万亿|%|美元|元…)` ＝ 0 命中；全阿拉伯数字行逐行人工核＝段号、问题序号、:56「超 12 月」为 STALE 纪律阈值——无一处行业数字；§9 数据卡全「待验证 [格式位]」且明写「本包不预置数字」「待验证未清前不得进正文承重」（:64-73）✓。
- **九段体例四域一致**：software-tech／market-competitor／film-tv 各恰 9 段（`## [1-9]` 计数＝9/9/9），段名同构（定义与边界／结构图谱／核心指标与口径／关键玩家（候选）／内行必答／特有信息源／陷阱❌→✅／场景侧重／数据卡格式位）；_new-domain-template 九段＋使用规则＋自建质检清单 ✓。
- **证据五标闭集**：SKILL.md:61 `FACT/INFERENCE/JUDGMENT/UNKNOWN/STALE` 五标·「标签只写英文」·闭合写法（正斜杠列举无省略号）✓；notes-format/methodology 各处引用同闭集 ✓。
- **与 30-discipline 无条款冲突**：30-discipline §五为讨论回执引用纪律（四件套/引用高于括注/自报优于他查），deep-research §七 为其在调研产物面的超集延伸（三关/hard fail 均为加严不放松），无相反条款 ✓。
- **minor-c**：software-tech.md:15「缺省十字维」实列 10 维＝一致，但同文件多处中英混排体例行文（如 methodology.md:16 `rarely 超 5`）文风瑕疵，不影响判据。
- **minor-d（候补登记）**：蓝本 §四-7 含 `--assemble exit 0＋manifest 记数` 项——任务票判据未列入且 QA 纪律＝不得改动装配面（`-build` 预览面），本项 N.A.（留装配段验证）。

## 登记面核对（devkits HEAD＝b0c1163）

| 项 | 判定 | 证据 |
|---|---|---|
| bundle.lock 组件行 deep-research（repo=`../multi-agent-collab-skills`·ref=`deep-research@v1.0`·roottag=skills·path/target=skills/deep-research） | **PASS（HEAD 内）** | `git show HEAD:…/bundle.lock \| grep -c deep-research`＝5；字段与蓝本 §二 逐一对位 ✓ |
| plugin.json version 1.3.3 | **PASS（HEAD 内）** | `git show HEAD:…/plugin.json` version＝1.3.3（commit b0c1163 该文件最后改动） |
| plugin.json skills[] 三行（software-orchestration／external-advisor-collab／deep-research） | **FAIL** | **HEAD `b0c1163` 内 skills[] 仅两行（无 `./skills/deep-research`）；第三行仅存在于工作区未提交改动**（`git status`＝`M …/plugin.json`；`git diff` 显示 `+ "./skills/deep-research"`）。HEAD 口径下注册面未宣告该技能＝按 HEAD 装配/发布的 bundle 不含 deep-research 注册行。 |
| skills[] 路径悬空性 | 非悬空（设计如此） | `./skills/external-advisor-collab` 同样不在源仓面＝装配期由 bundle.lock `target` 落进 bundle（既有同构先例），deep-research 组件行 target 对位 ✓ |

## 问题账（含 minor）

1. **major-1**：devkits plugin.json `skills[]` 增行未提交——HEAD 注册面缺第三行，与验收判据「HEAD＝b0c1163·skills[] 三行」不符。修法＝提交该工作区改动（内容本身正确·一行）。
2. minor-a：SKILL.md:69 指针 `references/30-discipline` 缺 `.md` 后缀。
3. minor-b：SKILL.md:69 四件套要素句与 30-discipline §五-2 核心句近逐字复述（摘要级·其余细则未复制）。
4. minor-c：个别中英混排行文风瑕疵（methodology.md:16 等）。
5. minor-d：蓝本 §四-7 `--assemble`＋manifest 记数项不在本票判据面且 QA 禁改装配面＝未验，候补装配段。

## IS_PASS 总判

**IS_PASS = 有条件通过（1 major 待补提交）——路由建议：回修工程师（一行提交），不阻塞其余八判据。**

八项判据实体质量全部 PASS；唯一硬缺口＝devkits 登记面 plugin.json 增行停在工作区未提交（HEAD 口径 FAIL）。属登记收尾遗漏而非技能本体缺陷；建议工程师席在 devkits 仓补一提交（建议 message 注明 R-6 仅注册行＋随 b0c1163 同票 T-deepresearch-01），提交后即可放行装配段（届时补跑 `--assemble`＋manifest 记数＝minor-d 候补项）。
