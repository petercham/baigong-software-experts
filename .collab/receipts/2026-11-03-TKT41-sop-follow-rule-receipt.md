# TKT41 · SOP 域随动规则票 · 工程师席执行回执

- 被执行票面：`.collab/tickets/2026-11-03-TKT41-SWB-sop-follow-rule-ticket.md`（105 行·sha256 前 8 `fdeca580`·起草笔 `59e2f59`）
- 执行席＝工程师席（engineer-tk41）·S-A~S-E 全目照票·文本锚定法＋同文件行号降序落笔
- **开端 HEAD 实测＝`a490ea1`**（TKT40/41 会师放行笔·MERGE-V13 收口链上·在票体 commit `59e2f59` 之后）

## 一、判据 0 前验复测（开工实测·与票面 §〇 逐项相等后方落文）

| 项 | 期望 | 实测 |
|---|---|---|
| `grep -roE 'v2\.9\|V13 L\|V12 L\|交接件v2' deliverables/` | 0 | 0 |
| quick-mode.md 行数 | 29 | 29 |
| bugfix-path.md 行数 | 20 | 20 |
| plugin.json L3 | `"version": "0.1.13"` | 逐字相等 |
| bundle.lock L5 | `"version": "0.1.13"` | 逐字相等 |
| SKILL.md frontmatter | `version: 1.1.2` | L5 命中 1 |
| lead 卡 L34 豁免句实物串 `（快速模式/BugFix 快捷路径除外）` | 20 字符·该行唯一命中 | `grep -o \| wc -l`＝1·L34 实物逐字相等 |
| 12 件闭集在盘 | 12 | 12 |

## 二、S-A~S-E 执行摘要

- S-A：quick-mode.md／bugfix-path.md 各于 L3 承载声明行后插空行＋退役声明头注一行（逐字＝票面 S-A 规格文本；bugfix 版档位名换「BugFix 快捷路径」其余逐字同）；两卷正文其余零触碰。
- S-B：lead 卡 L34 整串删除 `（快速模式/BugFix 快捷路径除外）`，删后该行＝`- ❌ 禁止跳过前序阶段直接进入后续阶段`；L45–59 路由四档表与 L94 零触碰。
- S-C：§20.1①–⑥ 过渡口径标注九落点全部落位（含 ③＝qa MD `## Test Writing Standards` 节头后·起草裁量面），统一模板行照票；具名对账表见 §四。
- S-D：SKILL.md L16/L17「何时必读」列行内改为 `技法参考（档位已退役 v2.9 §20.1⑦·轻工作量走维护票）`×2；description（L3）触发词未动；frontmatter `version: 1.1.2`→`1.1.3`。
- S-E：plugin.json L3 `0.1.13`→`0.1.14`；bundle.lock L5（bundle 本体行）`0.1.13`→`0.1.14`（components 行零触碰）；README 版本账区 v0.1.13 行之前新增 v0.1.14 行（逐字＝票面 S-E 规格文本）。

## 三、判据 1–8 执行后实测读数

1. `grep -c '快捷路径除外' agents/software-company-team-lead.md`＝**0** ✓
2. `grep -c '退役声明（v2.9 §20.1⑦）'`：quick＝**1**／bugfix＝**1**；行数 29→**31**／20→**22**（各＋2 加性）✓
3. `grep -rc '过渡口径（v2.9 §20.1'` 逐文件：qa MD **3**／engineer MD **1**／standard-sop **2**／deploy-gate **1**／dev-discipline **1**／lead 卡 **1**（合计 **9 落点**）✓
4. SKILL.md：`技法参考（档位已退役 v2.9 §20.1⑦`＝**2**；`判定走 ⚡ 快速模式后`＝**0**；`判定走 🔧 BugFix 快捷路径后`＝**0**；`version: 1.1.3`＝**1** ✓
5. plugin.json L3＝bundle.lock L5＝`0.1.14`（各命中 **1**）；SKILL `version: 1.1.3` 命中 **1**；README `版本账 v0.1.14` 行在位命中 **1**（现盘 L39）✓
6. `grep -rc 'v2\.9'` 逐文件：quick 1／bugfix 1／lead 1／qa 3／engineer 1／standard-sop 2／deploy-gate 1／dev-discipline 1／SKILL 2／README 1／PRODUCT 0／ARCHITECTURE 0＝合计 **14** ✓；`grep -ro 'V13 L' deliverables/ \| wc -l`＝**1**（README 版本账行内）✓
7. 闭集对账：`git show --name-only <执行笔>`＝声明闭集 12 件＋本回执＝**恰 13 件**（清单＝§一 12 件＋`.collab/receipts/2026-11-03-TKT41-sop-follow-rule-receipt.md`）；`git status deliverables/` 闭集外零改动 ✓
8. 禁动面复核：software-orchestration 其余五卷（collab-rules／delivery-summary／handoff-discipline／incremental-dev／partial-workflows）／PRODUCT.md／ARCHITECTURE.md／avatars／`deliverables/skills/` 三包／票包七件＋tickets/README／TKT40 票面与 SOP-R1 票面／三件登记面＝git 状态零改动；`.collab/` 域仅本回执一件新增（候处置池两份 2026-11-01 TKT qa 汇编件系开工前既存 untracked·零触碰）✓

## 四、九落点对账表（条款号×路径×行位×锚文本×标注句）

行位＝落笔前现盘行（锚）／落笔后实物行（注）；同文件多落点已按行号降序落笔防漂移。

| # | 条款 | 路径 | 锚行（前盘） | 注落位（后盘） | 标注句 |
|---|---|---|---|---|---|
| 1 | ① | `agents/software-qa-engineer.md` | L71 节头 `## Test Round Control (STRICT — MAX 2 ROUNDS)` | L73 | QA 两轮上限→三段式机械判绿＋缺陷票回流 |
| 2 | ② | `agents/software-engineer.md` | L87 `- No duplicate implementations across files` | L88 | IS_PASS 自审出口→制度③＋三段式 |
| 3 | ② | `skills/.../references/standard-sop.md` | L33 `   - 全部文件完成后执行 **全局一致性审查**（IS_PASS: YES/NO）` | L34 | 同② |
| 4 | ④ | `agents/software-qa-engineer.md` | L57 节头 `#### Smart Routing Decision (CRITICAL):` | L58 | 智能路由三态分派→回流四型＋B2 状态机迁移 |
| 5 | ④ | `agents/software-company-team-lead.md` | L90 `   - QA 每轮测试后必须做出智能路由判定（Engineer/QA/NoOne）` | L91 | 同④ |
| 6 | ⑤ | `skills/.../references/deploy-gate.md` | L32 节头 `## 五、四段部署流程（2026-10-28 皮总定口径：装配 → 预览 → 人类闸 → 部署）` | L33 | 独立 deploy-gate 四段卷→发布硬门禁二＋灰度机械门禁＋转正代写（四段流程保留为装配运维面） |
| 7 | ⑥ | `skills/.../references/dev-discipline.md` | L42 `2. 对账口径＝\`git show --name-only <commit>\` 与回执清单**全等**；缺项/多项＝违例（回执失真）。` | L43 | 人工回执全等对账→B2/B5 账本（回执保留为申报载体） |
| 8 | ①④ | `skills/.../references/standard-sop.md` | L43 `   - **最多 2 轮测试**：第 1 轮发现问题反馈修复，第 2 轮回归验证。2 轮仍不过则输出报告标注遗留问题` | L45 | （①＋④合并一行：QA 两轮上限→三段式机械判绿＋缺陷票回流；智能路由三态分派→回流四型＋B2 状态机迁移） |
| 9 | ③ | `agents/software-qa-engineer.md` | L90 节头 `## Test Writing Standards` | L93 | 工程师写脚本/CI 机械执行/QA 出结论（存量测试资产保留为技术面，不作验收结论源） |

全部九行统一模板形态：`> **过渡口径（v2.9 §20.1·X）**：<替代形态句>（旧条款保留为技法面，验收结论一律以 SWB v2.9 基线为准）`。

## 五、版本账升号读数（执行后）

- `.codebuddy-plugin/plugin.json` L3＝`"version": "0.1.14"`
- `bundle.lock` L5＝`"version": "0.1.14"`（bundle 本体行·components 行零触碰）
- `README.md` L39＝版本账 v0.1.14 行在位
- `skills/software-orchestration/SKILL.md` L5＝`version: 1.1.3`（独立线 1.1.2→1.1.3）

## 六、附注

1. **保留⑤（会师件 §二·TKT41 门禁读数入回执）**：执行后实跑 `bash deliverables/skills/object-audit/scripts/run-gates.sh` 读数＝**GATE PASS（发现 526 条，均按路由表走②不拦提交）**，exit 0；无 BLOCK 级新账（README sources/spec-anchors.md、deploy-gate.md 悬空等 OA-D6 既有旧账形态与基线一致）。pre-commit 钩子门禁于本执行笔提交时同径通过。
2. **S-B L94 引文 `**` 包裹注记**：票面所引 lead 卡 L94 串省略了实物盘面的 `**` 包裹——实物形态＝`1. 分析请求，**首先判断工作流类型**（快速模式/BugFix/标准 SOP/部分工作流）`；该行＝本票不动面，零触碰，读数以盘面实物为准。
3. **tickets/README L22 SOP-R1 状态行随批登记句（照会师件 §四口径）**：tickets/README L22「SWB SOP 退役规则（候执行）」行改指本票＝主理人随批手续，不在本票闭集、本席未触。本回执登记事实：TKT41 已落盘并已执行完毕（本回执即执行笔唯一回执件）；SOP-R1 自此转历史票面（append-only 留存原位·不再具执行授权），§20.1⑦「规则票一张」载体读 TKT41。
4. **回执文件名注记**：派工文书简写 `.collab/receipts/2026-11-03-TKT41-receipt.md`；本席按票面 §四 指名全名 `2026-11-03-TKT41-sop-follow-rule-receipt.md` 落盘（被执行票面为准）。
5. 停手项：**无**。
