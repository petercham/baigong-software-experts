# COLLAB-STRUCT-B345 工序纪律并案维护票·B3/B4/B5（架构席·过程件规格票·纯规格零施工）

- **票号**：COLLAB-STRUCT-B345｜**版本**：v1｜**起草席**：架构席（arch-commitment-design）
- **并案依据**：皮总裁定 `.collab/decisions/2026-11-08-皮总裁定-collab结构规范重定义与缺陷清单并案.md`（`b8bdadc`·blob 5,056B／`ea8061101341`）§二.4「十一项清单（`0259cd6`）联动并案：候开票 B3／B4／B5 与本次结构整改**同批出票处理**，不单开」；问题真源＝`.collab/2026-11-08-百工团队层问题复盘清单-v1.md`（`0259cd6`·blob 6,272B／`9dc187945f91`）项 9／10／11。
- **落点域**＝`agent-experts/baigong-software-team/skills/software-orchestration/`（复盘清单落点列「→ software-orchestration 随包技能」逐项照认）。
- **开工读数**：与主票 `COLLAB-STRUCT-1` 同笔开工同次实测（`2026-11-08 19:18:02 +0800`／HEAD `b8bdadc`／tracked 净）——两票同批起草，见主票 §8 票间关系。
- **两笔封顶**：v1＋（如需）v2。

## 0 三项问题转录（照 `0259cd6` 原文口径，不复议）

| # | 问题 | 严重级 | 现状 |
|---|---|---|---|
| 9（B3） | 票面/复跑 BLOCK 计数口径不统一（宽窄两口径 24579 vs 19007） | 低（每批多一轮「口径差非盘面差」解释成本） | 候开票 |
| 10（B4） | scratch 取证目录无清理规程（archive 解包树单席约 179MB·补复验三席累计数 GB untracked） | 低（磁盘卫生·无效力损害） | 候开票 |
| 11（B5） | 任务清单与落链面脱节（清单挂旧快照与实际链态不符） | 低（汇报噪声·误导盘面判断一次） | 轻档已即日执行；重档是否条款化候裁 |

## 1 现态基线钉值（落笔前实测）

| 件 | 现态 |
|---|---|
| `skills/software-orchestration/SKILL.md` | 26 行／4,805B／`2e1122c2f7ea`（frontmatter `version: 1.1.6`） |
| `references/handoff-discipline.md` | 78 行／6,263B／`971a8a35ad3e`（§五 收口自检五件套 `:30`；§七 报告三律「引用的数带名字带口径」`:45`） |
| `references/dev-discipline.md` | 131 行／12,071B／`5336693548f9`（§八 临时工作物落位与清理纪律 `:80-85` 四款在位） |
| `references/dispatch-discipline.md` | 22 行／1,446B／`831c2734baad` |
| `.scratch/tickets/TEMPLATE-票面模板-v2.md`（包内） | 48 行／2,877B／`33d5f2f1bada`（自检节 `:20-24`） |

**口径差实证基数（B3 取证）**：同一 run-gates 跑的两种读数并存——工程师回执 b080b9d 记「BLOCK24579／WATCH12494」＝**逐行 grep 严重度标签宽口径**；QA 6cf2767 记「GATE PASS 31429 BLOCK 垫空格口径 19007」＝**GATE PASS 行「发现 N 条」汇总窄口径**（`run-gates.sh:516` print 源）；本票开工实跑＝GATE PASS／发现 31,875。三读数同盘不同口径＝问题本体在册。

**B4 现条款缺口**：`dev-discipline.md §八.3` 已要求「收口登记票必含清理判据＋删除读数」，缺＝**取证目录清单行模板化**（哪些目录属本票取证面未成格式，主理人汇编无对账抓手）——补格式不补义务。

**B5 现档态**：轻档（收口登记时同步勾任务清单）已即日执行（复盘清单原文）；重档＝写入主理席位 MD 守则（走变更通道）候裁——本票给建议不自行拍。

## 2 施工规格（逐件行级，规格文本逐字入票）

### B345-A1 `references/handoff-discipline.md` §七 追加一款（B3 单一真源钉死）

现 §七.1「报告三律」第 3 句「引用的数带名字带口径」既有；本款在其下追加分条（append 于 §七 段尾，不动既有三行）：

```
4. 门禁计数单一真源＝run-gates 汇总行：引用门禁发现计数一律取 `GATE PASS（发现 N 条…）`／`GATE BLOCK：` 行 N 值（run-gates.sh 汇总出口），命名「窄口径」；逐行严重度标签 grep 计数＝「宽口径」，仅限归因明细用，票面/回执两口径同现时必各带口径名且以窄口径为判据值。禁裸数「BLOCK xxxx」无口径名（先例＝复盘清单项9：宽 24,579 vs 窄 19,007 同盘两读数）。
```

### B345-A2 `references/dev-discipline.md` §八.3 追加清理清单行格式（B4 规程化）

§八.3 段尾追加：

```
3a. 清理清单行格式（收口登记/回执必含，主理人汇编对账抓手）：逐行「`<取证目录相对路径> ｜ 删除｜留存去向`」列齐本票全部取证目录（含 QA 复测树／对拍树／干跑区），收口态每行落「删除」＋`ls` 空读数或「留存→归档仓路径」；无取证面者写「本票零取证面」一行，禁留空。
```

### B345-A3 B5 重档建议（条款本体不入本票写集，只出建议文本供裁）

复盘清单项 11 明载重档＝「写进主理席位 MD 守则（走变更通道）」。主理席位 MD＝`agents/software-team-lead.md`（现 77 行／`c2287132f1e8`）——**该件不在架构席写域**（席位卡走 C1/变更通道，见主票 §6 同族禁动面），本票只出候选条款文本：

```
候选条款（主理人侧收口操作规程）：收口登记落笔前，任务清单同步＝对链实测勾单（`git log --oneline` 区间核 vs 清单条目逐条对），清单挂账条目与实际链态不符时以链态为准改清单并注「清账随注」；禁先登记后补勾。
```

落位建议＝并入 `skills/software-orchestration/references/dispatch-discipline.md` §二 报告路径卫生段尾（主理人流程域技能面＝变更通道内），或席位 MD 本体走 C1——两案供裁；**本票写集默认取前者**（技能域内＝架构席随包技能维护权射程，见 §3 声明闭集），席位 MD 案候裁。

### B345-A4 `SKILL.md` 索引行随动（触发词面轻触）

- `references/dev-discipline.md`／`references/handoff-discipline.md` 两行「内容」列各补短语（「清理清单行格式」／「门禁计数口径单一真源」）；frontmatter `description` 触发词补「窄口径、宽口径、清理清单行、勾单」。
- **版本行零 bump 申报**：SKILL.md frontmatter `version: 1.1.6` 本票不动——包对外版本号归三同源合并批排期（与主票候裁④同口径，避免撞 PROJINIT 升号窗）；若裁定要求技能级随批 bump，另笔。

## 3 声明闭集（OA-D6-5 机检源·逐行完整路径）

- agent-experts/baigong-software-team/skills/software-orchestration/SKILL.md
- agent-experts/baigong-software-team/skills/software-orchestration/references/handoff-discipline.md
- agent-experts/baigong-software-team/skills/software-orchestration/references/dev-discipline.md
- agent-experts/baigong-software-team/skills/software-orchestration/references/dispatch-discipline.md

## 4 机械可验判据（施工回执必附实测）

1. append-only 对拍：三 references 件 difflib 行级对拍**纯增行**（deleted 行数＝0），前后行数实测登记（现 78/131/22 行对钉）。
2. grep 钉值：`git grep -c "窄口径" -- <handoff 件>` ≥1；`git grep -c "清理清单行" -- <dev 件>` ≥1；SKILL.md `git grep -c "version: 1.1.6"` ＝ 1（零 bump 自证）。
3. TEMPLATE 联动零触碰自检：本票不改 `TEMPLATE-票面模板-v2.md`（其 `:20-24` 自检节已有「附读数」体例，口径名约束经 handoff §七.4 传导即够——若双席审判定须模板同步钉一句，v2 rev 另笔，不预改）。
4. run-gates `--no-write` 复跑 GATE PASS 不翻红（对开工基线 31,875 窄口径零新增归因）。

## 5 禁动面闭集

- `agents/**` 五席位卡（含 lead——席位 MD 走变更通道，A3 席位 MD 案候裁未拍前禁动）；`config/**`；`docs/**`；`.archive/**`；代码与夹具域（`tests/**`）；`skills/sop/**`（B3 口径条款只落 handoff 纪律面，不改 run-gates.sh 本体——脚本汇总行为既有事实，条款追真源不追改工具）。
- 主票 `COLLAB-STRUCT-1` 写集全部件（两票写集零交叠自证＝本闭集四件不在主票 §4 声明闭集内）。
- SEMGV 案面全部（T3 v2 `b4a75d5` 候放行在案件条款互不污染）。

## 6 完工定义与三态明示（逐条分开写）

1. **做了但没落盘**：起草期三落点件＋TEMPLATE＋复盘清单／裁定两真源只读实测（wc/sha/grep＋run-gates 开工基线窄口径实跑）。
2. **落盘了但没提交**：本件写入 `.scratch/tickets/` 后至 `git add` 前为工作区新文件态。
3. **提交了但没对账**：commit 后至完工回报三项实测（status 照登／show --name-only 恰本件／尾笔 sha）前此态存在。

- **完工定义**：票面单笔 `collab:` commit＋回报附 sha／行数／字节／sha256＋自查勘正＋三态明示。
- **纪律**：双侧 pathspec 限定本件；禁 `git add -A`／`--amend`／`reset`／`--no-verify`；纯规格零施工；两笔封顶；落链即停候审。

---

## 租约段（架构席签注 · 由 B2 实例化）

```
lease:
  ticket: COLLAB-STRUCT-B345-v1
  seat: architect
  author_seat: arch-commitment-design
  path_globs:
    - .scratch/tickets/2026-11-08-COLLAB-STRUCT-B345-工序纪律并案维护票-v1.md
  deny_globs:
    - docs/**
    - .archive/**
    - agent-skills/**
    - agent-experts/**
    - softwares/**
    - tests/**
    - "*.py"
  note: 本票只出 B3/B4/B5 并案维护规格票面 v1 一件，零施工；不改 software-orchestration 四件一字、不碰席位卡、不改 run-gates 本体、不 bump SKILL 版本。依据＝复盘清单 0259cd6 项9/10/11＋皮总裁定 b8bdadc §二.4 并案令。B5 重档落位两案（技能域 vs 席位 MD C1）单列候裁，票面默认技能域案。两笔封顶；落链即停候双席审。
```
