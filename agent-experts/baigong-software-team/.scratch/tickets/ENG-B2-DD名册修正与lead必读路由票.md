# ENG-B2 DD 名册修正＋lead 必读路由票（工程师席）

- 背景（决策依据·自包含）：决策者指出两处缺陷——①通用开发纪律卷 §一.2 名册写「主理人/产品/架构/QA/研究」，但软开团编制闭集＝主理人/产品/架构/工程师/QA 五席，**不存在「研究」席位**（调研是各席通用技能，非编制）；②主理人席位 MD 的流程细则「⛓ 必读」路由表**缺通用开发纪律卷的加载路由**——派工合规硬门约束的是主理人，但主理人没有任何被路由到该卷的入口，纪律实际只对席位侧生效、不对派工侧生效。
- 改动面闭集＝三件：`workbuddy/baigong-software-team/skills/software-orchestration/references/dev-discipline.md`、`workbuddy/baigong-software-team/agents/software-company-team-lead.md`、版本账三处（plugin.json／bundle.lock／README）。他包零动。

## T1 dev-discipline.md（两处）

1. §一 第 2 条：「其他席位（主理人/产品/架构/QA/研究）」→「其他席位（主理人/产品/架构/QA）」。
2. §一 第 4 条后增第 5 条（逐字）：
   > 5. 调研是各席通用技能，不是席位：对决策者疑问的调研取证按问题适配席位派执行，不新设「研究席」编制。

## T2 lead MD 必读路由增行

「流程细则（⛓ 必读·已下沉）」表末增一行（表体例对齐现有行）：

> | 拟票/派工含代码性质或交付面写入 | `skills/software-orchestration/references/dev-discipline.md` |

## T3 版本账

- plugin.json version `0.1.5`→`0.1.6`；bundle.lock bundle.version 同步 `0.1.6`；README 版本账节 append 一行登记本次变更（名册修正＋派工侧加载路由），措辞自包含、无过程编号。

## 自检与红线

- `bash tools/run-gates.sh` GATE PASS；JSON 双可解析；改动面 grep 确认仅三件＋版本账。
- 回执（只落 `.collab/research/`）：`2026-10-30-ENG-B2-工程师回执-v1.md`——开端 HEAD 实测＋完整文件清单（与 commit name-only 全等）＋门禁读数。
- 红线：不碰 multi-collab/EAC；不 bump 他包版本链。
