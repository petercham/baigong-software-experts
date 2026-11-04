# SWB-CD1 施工回执 v1（engineer-cd1）

- 票面真源＝`agent-experts/baigong-software-team/.collab/receipts/2026-11-04-SWB-CD1-收口登记-v1.md`（票面定稿链 `b2f95aa`→`20d35a1`→`51002b5`→`ec71dcf`·已退役·寻回见 SWB-RET 退役名录）。
- 开工实测 HEAD＝`ec71dcf`（≥票面 ANCHOR `3b03738`，读数附此）；收口施工笔 HEAD＝`19b313a`（本回执单独次笔）。
- 计数口径＝occurrence；token 申报四要素见判据 4；负例 exit≠0 体例照票。
- 施工续飞说明：首轮现场＝闭集 11 件全落盘零 commit（会话中断非门禁拦红）；本笔经 pre-commit 门禁 GATE PASS 干净入库，禁 `--no-verify` 未用、amend 未用。

## 一 闭集 name-only 全等表（判据 1）

`git show --name-only --format= 19b313a | sort` 与票面声明闭集 11 件逐行 diff＝零差 → **J1_NAMEONLY_EQUAL**。

| # | 票面声明 | 实提交 | 等 |
|---|---|---|---|
| 1 | skills/software-orchestration/references/dispatch-discipline.md（新建） | ✓ create mode 100644 | ✓ |
| 2 | skills/software-orchestration/SKILL.md | ✓ | ✓ |
| 3 | agents/software-team-lead.md | ✓ | ✓ |
| 4 | agents/software-team-architect.md | ✓ | ✓ |
| 5 | agents/software-team-product.md | ✓ | ✓ |
| 6 | agents/software-team-qa.md | ✓ | ✓ |
| 7 | agents/software-team-engineer.md | ✓ | ✓ |
| 8 | bundle.lock | ✓ | ✓ |
| 9 | plugin.json | ✓ | ✓ |
| 10 | .codebuddy-plugin/plugin.json | ✓ | ✓ |
| 11 | README.md | ✓ | ✓ |

## 二 判据 1–8 读数

1. **闭集全等**＝11/11 全等（上表）→ 绿。
2. **条款 occurrence**：`不允许同席多实例并发`（五 MD＋dispatch 卷六件 grep -o|wc -l）＝**6**；`异席并发不禁`（lead MD＋卷）＝**2**；`不建登记表`（卷 grep -c）＝**1** → 绿（钉值 6/2/1 按 Y-1/Y-2 修后定稿文本起算自洽）。
3. **自包含断言**：新增/改动七面（CD-A 卷＋CD-B SKILL＋CD-C/D 五席位中落行五 MD 按七面口径=卷/SKILL/lead/arch/product/qa/engineer）逐面 `grep -c "\.collab/decisions\|12a3c4a\|d1c9849\|7fbd1ea\|10865cf\|皮总"` ＝**七面全 0**；负例自证＝Temp 构造含引用副本，grep 命中 1，对其跑「＝0 断言」（`| grep -qx "0"`）exit=**1**（断言式负例 exit≠0 体例）→ 绿。
4. **token 红线前后读数（四要素申报）**：口径＝script-v1（CJK≈1 tok/字、非 CJK≈4 字符/tok）；被测 commit＝前跑 `ec71dcf`、后跑 `19b313a`；实测人＝engineer-cd1；取整＝ceil。前后两跑同显式 glob 口径（R-1）＝`python tools/count_agent_tokens.py "agent-experts/baigong-software-team/agents/*.md"`：

| 席位 MD | 前 | 后 | 增量 | ≤2500 | 增量≤150 |
|---|---|---|---|---|---|
| architect | 873 | 921 | +48 | OK | ✓ |
| engineer | 1002 | 1049 | +47 | OK | ✓ |
| lead | 1412 | 1474 | +62 | OK | ✓ |
| product | 813 | 860 | +47 | OK | ✓ |
| qa | 930 | 978 | +48 | OK | ✓ |

前跑五值与票面现盘落位实测登记值逐值全等 → 绿。

5. **SKILL 随动**：`grep -c "dispatch-discipline.md" SKILL.md`＝**1**；`grep -c "version: 1.1.4"`＝**1**；`check-skill-meta.py --root .` exit＝**0**（OA-S5/S2 过，coverage 提示＝--project-name 未注入子判据未执行，非红项）→ 绿。
6. **门禁＋六演练**：`run-gates.sh --root .`（现盘含未清临时面）exit＝**0** → `GATE PASS（发现 8797 条，均按路由表走②不拦提交）`；族集＝{check-collab-lint, check-entity, check-pointer-closure, check-pointers, check-source-of-truth, check-ticket-reconcile} 与开工登记族集同集＝**零新增族**（+4 增量归因见黄项 Y-b）。六演练＝`T06_TMP="D:/multi-agent-collab-devkits/.scratch/cd1/tmp-drill"`（Windows 盘符形态口径·R-4）`bash …/drill-runner.sh` exit 0，`SIX_DRILLS_GREEN` occurrence＝**1** → 绿。
7. **版本账**：`grep '"version"'` 单行取法（R-2）三处＝bundle.lock `"version": "0.1.20"`／plugin.json `"version": "0.1.20"`／.codebuddy-plugin/plugin.json `"version": "0.1.20"`＝三值全等；README `git diff --numstat`＝**1 增 0 删**＝append-only → 绿。
8. **条款在位负例**：Temp 复制五 MD＋卷、删卷内条款字面 → 判据 2 式重跑 raw＝5≠6，断言 `[ = 6 ]` exit＝**1** → 绿。

## 三 席位行落位行号表（追加行·Y-2 后无「（Agent ID）」括号注口径·行末指针照票面）

| 席位 MD | 段 | 落位行号 |
|---|---|---|
| software-team-lead.md | 「## 纪律行」段尾 | L75 |
| software-team-architect.md | 「## 席位纪律」段尾 | L37 |
| software-team-product.md | 「## 席位纪律」段尾 | L37 |
| software-team-qa.md | 「## 席位纪律」段尾 | L37 |
| software-team-engineer.md | 「## 席位纪律」段尾 | L38 |

## 四 口径登记句

- **O-3/R-5 登记**：engineer 席位新增行「不允许同席多实例并发…【席位守则·dispatch 卷】」**无 G 标注**＝纪律自保证型条款（拦截主体＝主理人派席纪律＋席位拒产并报，卷内§三无机件条款明定不建登记表/不扩租约/不设机械闸），**非缺标注**；与 engineer L29 既有 G1 串行闸条款（票型专属机制面）并存，语义部分重叠照票面＝登记不删。
- **R-3 登记**：票面「双席审票＝串行派发」为审票轮程序款，施工未将其扩写回「派席一律串行」旧口径——成文面红线唯一＝同席多实例禁令，异席并发不禁。
- **object-audit 边界注记**：照票面增补注记（§七收口口径·主理人裁定），object-audit 全域零触碰（本笔 name-only 无 agent-skills/object-audit 任何件）；§八「两面」措辞按 §七 读，非候裁。
- **誊写禁令自察**：本批＝新建创作类条款成文（票内定稿文本＝交付真源供给），落盘非搬家，辖域外自察声明照票面开工附注①。

## 五 黄项（如实登记·不硬闯）

- **Y-a 临时面清灭被拦**：施工期判据读数工作目录 `.scratch/cd1/`（66 件 untracked）清灭两次触本机 safe-delete 批量确认闸（阈值 50），用户拒绝放行 → 按禁硬闯款停止清除，临时面留存。该面为 git 未跟踪面（`git check-ignore` 判定＝非忽略、但 untracked ∉ 任何 commit），不入版本库、不影响闭集全等与门禁路由（run-gates 输出中无 `.scratch/cd1` 主体发现行）；清灭动作候主理人/用户侧处置。
- **Y-b 门禁总数 +4 增量归因**：开工登记基线＝GATE PASS 8793（qa-cd1rev 独立复跑值）；收口现盘＝GATE PASS 8797。增量 4 条族＝check-ticket-reconcile WATCH「未声明生成件」——历史票 ENG-S8/ENG-S9 声明闭集未覆盖 bundle.lock／README／四席位 MD 等路径，本批提交后对账器把该批 commit 路径归因至历史票名下 WATCH。非新门禁族、非 BLOCK、不拦提交；处置建议＝候裁（历史票闭集追认或账器归属口径，均出本票闭集零触碰）。
- **Y-c 基线对照 worktree 环境性红**：为对照基线曾在 `.scratch/cd1/baseline-wt` 挂 `ec71dcf` 隔离 worktree 跑门禁＝GATE BLOCK（check-source-of-truth exit=2）＝环境性伪影（worktree 落 scratch 子路径致扫描闭集面不同），不代表开工基线；开工基线以主工作盘 qa-cd1rev 实测 GATE PASS 8793 为准。该 worktree 已 `git worktree remove` 移除，仓内 worktree 账干净。

——engineer-cd1 施工回执 v1（施工笔 `19b313a`；回执笔另笔随本件 commit）。
