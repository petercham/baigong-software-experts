# STRUCT-FIX 票面独立审票 v1（QA 席·B 席 fresh eyes·只审不改）

- 帽：开工 HEAD 实测 `git rev-parse --short HEAD`＝`4a28614`（STRUCT-FIX 开票笔本体＝被核对象笔，票开端读数 f199c30 为其父侧依据笔，均实测在位）；工作区他席在途＝`.collab/ledger/`＋`.scratch/structfix/`（开票侧读数区，不入本审写域）。
- 被核对象：`.scratch/tickets/2026-11-05-STRUCT-FIX-structure-declaration-alignment-ticket.md`（4a28614 态，架构席起草）。
- 口径：工程师申报零采信·一切读数本席自己实跑（跑于 4a28614 态）；只读零施工；临时读数居仓根 `.scratch/qa-structrev/`（批毕自删，关键读数已随本件登记）。

## 结论

**红 0／黄 2／绿 5**。黄＝判据命令语法两处（不实质动摇票面设计，建议修票笔后放行施工）；全部前态钉值与预跑读数复现成立。建议路由＝**双黄随修票笔（append-only 修订段）更正后按 HOLD 排程放行**，无需重审级返工。

## 逐条审尺读数（全部本席实跑）

### ① 实态核对——绿（票面前态读数全复现）

- 七份 STRUCTURE 条目/yaml 计数复跑（有效口径 `grep -c '^- [`]'`／`grep -c '^  - '`）：fuxi 3/3、EAC 2/2、object-build 2/2、multi-collab 2/2、object-audit 4/4、bundle-assembly-registration 2/2、bundle 7/6——**七份逐一同票面申报** ✓（bundle 7/6 差值＝`docs/adr/` 条目注「不属于交付路径」不入 yaml＝票面既成例外，实测吻合）。
- 「非枚举面」现盘零命中复跑：`git grep -c "非枚举面" -- "*STRUCTURE.md"` exit 1；`git grep -l` exit 1——零命中 ✓。
- fuxi 顶层清单：`git ls-files agent-skills/fuxi-skill/ | cut -d/ -f3 | sort -u | grep -v '^\.'`＝8 行（README.md adapters contracts docs gates products rejected specs）✓ 同票面 readings-N 八行申报。
- fuxi SKILL.md/references 全史零落笔：`git log --all --follow -- agent-skills/fuxi-skill/SKILL.md` 空返回；`git log --all --follow -- agent-skills/fuxi-skill/references/` 空返回——从未存在（非删除）✓；盘上亦不存在 ✓；STRUCTURE 建立笔实测＝`c7f87e7`（SWB-B1 骨架票壳批）✓ 同票面「B1 壳批模板先行态」定性。
- 闭集 11 件 `git ls-files` 在位复跑＝11/11 ✓；README 版本账尾行＝v0.1.25 @L67 ✓；三同源现值＝`0.1.25` @ plugin.json L3／.codebuddy-plugin/plugin.json L3／bundle.lock L5 ✓ 行号锚逐一同票面。
- 小噪声登记（不判色）：票 L20「闭集 8 件全部 git ls-files 实测在位」vs 声明闭集块列 11 行——自检段已自解（8 路径行＋S5 三同源补正＝11），三同源在位本席复跑亦真，纯措辞噪声。

### ② A 判据可执行性——黄 2

- **黄-1（A1/A2/A8 条目计数命令转义缺陷）**：票面 A1 式写作 `grep -c '^- \`' …`。bash 单引号内 `\`` 是**字面反斜杠＋反引号**，该式实跑返回 `0`（exit 1）——按票面逐字执行则前态钉值 3/3 不可达。有效写法实测：`grep -c '^- [`]'`（BRE 方括号包裹）→ fuxi 前态＝3 ✓ 钉值可达；`grep -cF '^- \`'`（含杂散反斜杠）＝0 ✗。同型错误在 A1「后态＝7」、A2「后态＝3/3」、A8「仍 2/2」条目计数面全套传导。yaml 计数式 `grep -c '^  - '` 语法无缺陷 ✓。**建议修票笔＝计数式统一改 `'^- [`]'` 形态。**
- **黄-2（A4 逐字对等基准载体歧义）**：§口径 1 定稿句以反引号包裹展示（L29），S1 定稿全文内落位句无包裹（L55）。实测：L29 去包裹反引号后与 L55 逐字节同一（sha256 前 12 位均 `15b98b5a1653`，229 字节）；含包裹则 − 文件行必不相等。A4「同串与票面 §口径 1 逐字节对等」未指明**去包裹态**——机械执行有歧义窗口（低风险，可合理消解）。**建议修票笔＝A4 钉基准＝去包裹内串（可附 sha256）。**
- **A5 对偶不变式现行七份复算＝绿**：七份逐份 yaml⊆条目行断言全 PASS（bundle 例外＝docs/adr 条目不入 yaml，既成形态）；A2 实体在位 `test -d` EAC sources ✓ TRUE（`sources/spec-anchors.md` git 面在位）；object-build scripts ✓ TRUE（`scripts/publish.py` git 面在位）。
- 判据链有效性旁证：S1 定稿全文形态复核＝条目 7/yaml 7 可达、七条 `test -e` 全真（README/adapters/contracts/gates/products/rejected/specs 盘上全 EXISTS）。

### ③ OA-T1 门禁兼容预跑复现——绿

- 真判据链复跑（`check-entity.py`＝run-gates.sh SCRIPTS 清单项直跑，GATE_PROJECT_NAMES＝run-gates 缺省注入口径 `multi-agent-collab-devkits`）三样本：惯例句行（定稿逐字）＝date 命中 **0**；版本账 v0.1.27 新行（定稿逐字，日期在全角括注内）＝date 命中 **0**；裸日期对照样本＝命中 **1**（BLOCK 行判据链有效）——同票面四样本预跑读数（惯例句裸 0／版本账行裸 0／对照 1）✓ 复现。
- 仓根现盘基线：check-entity 全扫描面五模式 count 全 0（date=0）——本票落笔后新增文本仅惯例句（零日期）＋版本账行（括注日期），不破基线 ✓。七份 STRUCTURE 现盘 `20xx-xx-xx` 逐份 grep＝0 ✓ 同票面「扫描面内已核」。

### ④ 三同源相对值风险——绿（无歧义死锁，一附带登记）

- 票面写法机械可执行：HOLD 排 ADR-L0 后＋「按彼时现值 +1 随动并附前后读数（H6/F7）」＝执行时读现值即可定值，无死锁。A6 另含链序判据（README v0.1.26 行在位先于本票行）＝HOLD 违反可机检。
- 附带登记（不判色）：S5 定稿行文本内嵌绝对值「三同源 0.1.26→0.1.27」——与「绝对值按现值随动」原则并置，若 ADR-L0 落地值偏离其 A5 钉值（0.1.26）则逐字文本与随动规则矛盾；现 ADR-L0 票 A5 已钉死 `0.1.25→0.1.26`（ebdb8b4 修票态），两票钉值咬合，风险闭合。

### ⑤ WorkBuddy 平台兼容面（fuxi 声明删 SKILL.md＝装配断链否）——绿

- `bundle.lock` components 实测全列＝`["external-advisor-collab", "deep-research"]`——**fuxi 非 bundle 组件**，lock 面 `grep fuxi` exit 1 零引用。
- 两 `plugin.json` `skills` 数组实测＝仅包内路径（`./skills/sop`、`./skills/software-orchestration`／`./skills/software-orchestration`、`./skills/external-advisor-collab`、`./skills/deep-research`）——零 fuxi 引用。
- 全仓引用面：`fuxi-skill/SKILL.md` 命中仅历史 `.collab/design` 文字坐标（叙述件·非装配面）；json/lock 装配闭集零引用。删 SKILL.md 声明＝**零装配断链** ✓。

### ⑥ 撞号/撞面（与 ADR-L0 票互核）——绿

- ADR-L0 票（ebdb8b4 修票态）写集含 bundle README＋三同源＝交叠二面与 STRUCT-FIX HOLD 声明互核一致；ADR-L0 S3d 钉 README 插 v0.1.25 行后（＝现 L67 后）＋三同源 0.1.25→0.1.26，STRUCT-FIX 插「彼时尾行后」＝插入序两票自洽无撞行。
- object-audit 面：ADR-L0 票 L118 自注「docs/STRUCTURE.md（docs/adr 条目 L11 已在位＝无需改）」；STRUCT-FIX 对 object-audit STRUCTURE 仅惯例句零条目动——两票对该文件动作零交叠 ✓。ADR-L0 写集不触其余六份 STRUCTURE（STRUCTURE.md 命中仅 bundle 份一条注句）✓。

## 修票建议（双黄路由·append-only 修订笔即可）

1. A1/A2/A8 条目计数式改 `grep -c '^- [`]' …`（或附等价 `grep -cF` 无杂散反斜杠写法），前态钉值不变（3/3·2/2·2/2 复现成立）。
2. A4 基准钉＝「去包裹内串」＋可选 sha256 钉值（本席实测前态候选句内串 sha256 前 12＝`15b98b5a1653`）。

## 附：本席临时读数登记（`/.scratch/qa-structrev/` 批毕已自删）

r1-counts.txt（初跑口径噪声登记）／r2-a1caliber.txt（A1 命令三写法对比：票面逐字式＝0、grep -F 杂散式＝0、方括号有效式＝3）／r3-a5-dual.txt（A5 七份对偶复算全 PASS）／r4-oat1-prerun.txt（三样本 check-entity 真判据链读数）／r5-a4-ambiguity.txt（L29/L55 sha 对等核）／sentence-L29/L55.txt（惯例句两处对比）。

## 修订记录

（append-only，修票面笔此后追加）
