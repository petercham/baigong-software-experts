# ENG-S2 票二：席位 MD 交接与收口声明补缺（工程师席·交付面写入）

- 开端读数：devkits HEAD 以本票 commit 实测为准。
- HOLD 检查：无 HOLD——审票意见（F 系列两轮）已清账，票一链 QA 已 PASS。
- 背景（决策依据·自包含）：通用协作纪律整合清单经决策者七项裁决（含 QA 补行终句、lead 拒写权句自指循环形态「拒绝并自行改派」），锁三票序：票一 handoff 卷成文（已完成·QA PASS＋F2/F10 修正链 QA PASS）→本票 席位 MD 补缺→票三 G6 修订＋机检。席位 MD 须带自指短声明（真源在纪律卷，短声明不复写）；lead 拒写权句采「拒绝并自行改派工程师席」形态（防「报主理人改派」在 lead 席上的自指循环）。工程师席声明同步句（L2·G6 修订镜像）随票三同 commit——**本票工程师 MD 只加收口声明一行（L5），其「写权边界」节零动**。
- 改动面闭集＝八件：
  1. `workbuddy/baigong-software-team/agents/software-company-team-lead.md`
  2. `workbuddy/baigong-software-team/agents/software-qa-engineer.md`
  3. `workbuddy/baigong-software-team/agents/software-architect.md`
  4. `workbuddy/baigong-software-team/agents/software-product-manager.md`
  5. `workbuddy/baigong-software-team/agents/software-engineer.md`（仅 T3 节一行）
  6. `workbuddy/baigong-software-team/plugin.json`
  7. `workbuddy/baigong-software-team/bundle.lock`
  8. `workbuddy/baigong-software-team/README.md`

## T1 lead MD（三处）

① 现「## 写权边界」节引文段末 append 一行（同节内）：

> 本席受命向交付面写入时应当拒绝并自行改派工程师席——细则见 dev-discipline 拒写权条。

② 文件末新增节（节名与引文块体例随各席位 MD 现行「写权边界」节样式）：

```
## 交接与收口声明

> 本席收口声明前跑收口自检五件套（缺项只报部分完成）、不改他人文档、报告按来源层级标注——细则见 handoff-discipline。
> 本席派工件只给目标与验收，不给怎么做——见 handoff-discipline 派工件干净度条。
```

③ 「流程细则（⛓ 必读·已下沉）」表末 append 一行：

> | 需要交接上下文/写交接件/收口声明/向上呈报 | `skills/software-orchestration/references/handoff-discipline.md` |

## T2 QA MD：文件末新增节

```
## 交接与收口声明

> 本席收口判定前逐件核对回执清单与交付面纯净性（含编号可解析抽验）——细则见 dev-discipline。
> 本席收口声明前跑收口自检五件套（缺项只报部分完成）、不改他人文档、报告按来源层级标注——细则见 handoff-discipline。
```

## T3 架构 MD、产品 MD、工程师 MD：文件末各新增节（同一体例·仅一行；工程师 MD 除此节外全文件零动）

```
## 交接与收口声明

> 本席收口声明前跑收口自检五件套（缺项只报部分完成）、不改他人文档、报告按来源层级标注——细则见 handoff-discipline。
```

## T4 版本账（三件）

- `plugin.json`、`bundle.lock`：版本 `0.1.7` → `0.1.8`（双源同值）。
- `README.md` 版本账段 append 一行（体例随现行版本账行，措辞自包含，参考形态）：

> **版本账 v0.1.8**（2026-10-30·席位声明补缺批）：五席位 MD 增「交接与收口声明」自指短声明节（lead 另补拒写权自指句＋⛓ 必读表 handoff-discipline 路由行；QA 补收口判定核对行）——细则真源在 software-orchestration 纪律两卷，席位侧只载自指短声明不复写。plugin.json＋bundle.lock 双 0.1.8。

## 自检与回执（J6 四读数必附——形式约束数值＝单次增量 ≤8 行/席、每声明 ≤1 行、与纪律卷条文最长连续重合 <12 CJK、声明句「本席」＋卷名 grep 双命中）

- 逐席 J6 读数表：本次声明块增量行数（lead 声明增量＝3 行≤8；QA＝2；架构/产品＝各 1；工程师＝0）＋每条声明单行实测＋与 dev-discipline/handoff-discipline 条文逐对比最长连续重合 CJK 读数（预期 <12，如触线停手上报不得改写卷文凑数）＋grep 双条件命中读数。
- 声明块定界（供将来自检参照）：「## 交接与收口声明」节起至节末；lead 拒写权句归「写权边界」节；⛓ 路由行只计路由账不计声明块。
- run-gates（仓内在册实体路径）GATE PASS（附输出载体）；check-source-of-truth 无新增 BLOCK（附读数）；禁列过程痕迹扫描用终式 `见?第\s*\d+\s*轮|轮次戳|〔[^〕]*·轮〕|轮次号[：:]`，净增行命中按三分账如实登记（H6：票面预期与实测冲突按实测登记上报）。
- 版本前后值各附实测（plugin.json／bundle.lock 两处 grep，0.1.7→0.1.8）。
- 回执落 `D:\multi-agent-collab-devkits\.collab\research\2026-10-30-ENG-S2-工程师回执-v1.md`：开端 HEAD＋完整文件清单（与 commit name-only 全等）＋J6 读数表＋全部机制断言附实测载体（N4）。

## 红线

只动闭集八件；`agents/software-engineer.md` 仅新增 T3 节（「写权边界」节零动——L2 同步句随票三）；skills 两卷（dev-discipline/handoff-discipline）零触碰（细则修订属票三）；声明句逐字照录一字不改——对定稿句有异议停手上报；席位 MD 其余节零触碰。
