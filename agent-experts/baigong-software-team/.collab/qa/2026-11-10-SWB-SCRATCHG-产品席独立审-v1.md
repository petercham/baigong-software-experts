# SWB-SCRATCHG 规格票 v1 · 产品席独立审件（A 席 · fresh eyes · 只读零改被核物）

- 审席：产品席 `pm-scratchrev`（fresh 实例）
- 被核件：仓根 `.scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v1.md`（落链笔 `00f7e7d`，下称"票面"，行号＝该文件现读行号）
- 并发纪律：QA 席同时并发审同一票，本席零读其产出；链上他案笔照登不碰。

## 〇、开端读数（本席开工首步实测）

| 项 | 命令 | 本席读数 |
|---|---|---|
| 时点 | `date` | `Tue Nov 10 19:33:42 2026` |
| HEAD | `git rev-parse HEAD` | `00f7e7dd2cfcdb09af4603f02930663a43275324`（＝票面落链笔，恰对钉） |
| tracked 面 | `git status --porcelain --untracked-files=no` | 净（零行，票面开工所登 FUXI-U38 staged 一枚已随 `4f84484` 落链，现 tracked＝在场照登） |
| 落链笔恰一件 | `git show --name-only --format= 00f7e7d` | 恰一行＝票面自身 ✓ |

## 一、审尺 1 · 忠实性 —— PASS（带 W-1 注）

**核心产品问＝方案甲规则块是否忠实落地裁定目标态；tickets 桶负向豁免是否架空裁定意图。**

实测与判定：

1. 裁定目标态两面在 S1 规则块全部落地：票面 §4.1 九行块（L84–L89 围栏）以 `/**/.scratch/*`＋`/.scratch/*` 立 .scratch 族生效忽略——本席以 `git -c core.excludesFile=<探针文件>` 覆盖式复跑（.gitignore 零触碰）：`.scratch/x`→exit 0 命中 `/.scratch/*` 行、`agent-experts/baigong-software-team/.scratch/x` 与 `agent-skills/fuxi-skill/.scratch/x`→exit 0 命中 `/**/.scratch/*` 行＝"临时开发调试的东西往 .scratch 塞、不进 git"对**任意层级新增临时物全量生效**，与 18:58 裁定原文语义直对。
2. 豁免面宽度实测＝**最窄可行**：`!/**/.scratch/tickets/`＋`!/**/.scratch/tickets/**`＋仓根配对两行，仅放行 tickets 桶；探针复跑（V2 口径·桶内放一枚不存在样本路径）仓根 tickets 桶与百工 tickets 桶各→exit 1（豁免成立），`agent-skills/fuxi-skill/.scratch/FX-U26/probe`→exit 0（桶外照旧忽略），tickets 桶内 `__pycache__` 编译缓存样本→exit 0 命中 `.gitignore:65:__pycache__/`（票面 L94 声明逐字兑现＝豁免不纵票桶杂物还魂）。豁免面未外溢。
3. 张力处理合规：裁定「.scratch 不进 git」与现盘 135 件 tracked 历史票据（刻意留档≠临时调试物）之间确有口径张力——票面未自决：§4.0 方案甲/乙对照登记、形态之争单列候裁(d)（票面 L157）、§4.2 类A 句尾再指候裁(d)（L100），并如实标注方案乙代价面含「票面落位裁定翻案」（L71）。该呈裁的事在票面呈了，未在票内偷拍。
4. W-1（WATCH）：票面 §4.2 把类A 135 件统称「刻意留档票据面」，对仓根桶内 12 枚 B 批过渡票欠准——仓根 `README.md` L22/L88 在册「仓根 `.scratch/tickets/` 仅存 B 批过渡票（退役候裁见 B 批收口登记）」，过渡票既有"候退役"身份与「刻意留档」标签不完全咬合。方案甲下零冲突（不预决其退役），但裁(d)时措辞宜区分"永久留档票面"与"过渡候退役票面"。

结论：**PASS**——目标态忠实落地、豁免面窄且经探针实证、真张力全部上呈候裁，无架空、无票内自决。

## 二、审尺 2 · 候裁面完备与不越权 —— PASS（带 Y-4 勘正）

七条逐判（票面 §七 L154–L160）：

- **(a) 仓外卫生两硬条款并入与否**：确属决策者保留闸。条款②与既有 TMP-DISC §八.3 收口清理判据（真源 `agent-experts/baigong-software-team/skills/software-orchestration/references/dev-discipline.md` §八第 3 款，本席现读在册）部分重叠，"向前强化句"＝新措辞成文权归决策者，并入与否候裁合法。合法。
- **(b) 并发重估口径登记**：票面只登记「FUXI 案候补池 R12『并发规矩不立』真义＝会话职责划分防串扰≠并发风险管理不需要」供裁、不预设结论（L155）——照另口径背景判**合法面，不判违例**。唯其佐证读数面有失真处，见审尺 4 之 Y-1（候裁合法、佐证须勘正）。
- **(c) 他案射程**：方案甲读法下 fuxi 21＋EAC 11 全落类A 零处置＝争点自动消解、裁乙才复活——归属之争候裁合法（迁移他案面存量属会话职责划分＝决策者/主理人闸）。合法。
- **(d) 历史留档形态**：留 `.scratch/tickets/`＋豁免 vs 迁合规桶——两制各有在册依据（`f135855` 落位裁定 vs 裁定新口径），属两裁张力归并＝**确属决策者保留闸**（非已裁回流：`f135855` 裁的是票面落位，本条裁的是存量保留形态，且票面明标甲承接现行制）。合法。
- **(e) 类B 取态**：B-i 迁 `agent-experts/baigong-software-team/.collab/receipts/`（本席核该桶在管在册＝tracked 95 件，回执体例对口；类B 件现读首行＝「COLLAB-STRUCT-1 施工回执 v1」＝内容类型判定属实）vs B-ii `git rm --cached`——处置取态候裁合法，票面明令"未裁不得施工"（L101）。合法。
- **(f) T9 括注**：表述面增益，票面已给零随动默认（§4.3 第 2 条，本席现读 `agent-experts/baigong-software-team/skills/sop/templates/ticket-template.md` L93–L103 档位3 措辞与封口条款在册，"正交不冲突"判定成立）——随不随动候裁不过度。合法。
- **(g) README 随动**：本席现读 `README.md` L18/L22 白名单行现文在方案甲下语义未变（票面桶仍进 git）＝"现文仍准确"判定属实；加 ignore 态行与否＝表述面候裁、未裁零动（禁动面 L123 已框）。合法。

回流检查：无已裁事项回流候裁（18:58 裁定目标态本身未在票内被裁——票面按目标态成文规格，属执行面照落；`f135855` 现行制被承接而非重开）。过度候裁检查：无——七条各自挂在真分歧或决策者措辞权上，票面对每条均给了"未裁零动"缺省。

- **Y-4（黄）**：票头 L9 写「候裁点＝单列 §七 **六条**」，§七 实列七条（a–g），§八.1 又写「候裁**七条**呈皮总归裁」——票内自相矛盾，一行勘正（应为七条）。

结论：**PASS**（候裁面完备、不越权、无回流、无藏自决；Y-4 属计数笔误不伤语义）。

## 三、审尺 3 · 可施工性（产品视角）—— PASS（带 Y-3）

1. 分流判据族可照字面执行：类A 路径判据（含 `/.scratch/tickets/` 段∨仓根前缀）、类B 补集判据、类C `??` 面判据——三级均为纯路径/状态机械式，无自由裁量词；类B 点名件存在性本席复跑坐实（下审尺 4）。V0 已要求施工席当轮再实测，判据不硬编码清单的写法成立。
2. V0–V8 逐条可机械跑判定：V1/V2 探针口径本席已代跑全兑现（§二.1 读数）；V5 钉值本席现跑＝`git check-ignore -v agent-skills/fuxi-skill/.collab/evidence/corpus/rb8-suppl` → exit 0 命中 `.gitignore:20:/**/.collab/evidence/`，叠加探针规则族后命中行仍 L20＝不翻面实证复现；`grep -n '/\*\*/\.collab/evidence/' .gitignore` → 20 ✓；V8 插位前提核实＝.gitignore 全文 66 行、L52–L54 为 REFERENCE-SOURCES 配套负向组尾、L55 空行、L56 节头「# ── 系统杂物／工具产物…」——票面"插在 L54 与其后空行之后、L56 节头之前"落位描述属实可行，L17（制②节头）/L20（evidence 行）零移动可由 diff 兜底。
3. **Y-3（黄）**：V3 硬钉 `.scratch/` 未跟踪计数→**0** 在并发窗口脆弱——tickets 桶豁免面上任何**尚未 commit 的新票面**（本票放行后的施工票面本身、或并发他案新起草票面）在 V3 跑时刻会以 `?? .scratch/tickets/<新票>.md` 现身→假 FAIL。本席现跑确认现盘 tickets 桶内 `??` 面＝0（该钉当前成立），但票面自证 §一 已示仓根票目录多席共用实况。修案：V3 拆两读——`.scratch` 族内 **∉tickets 桶** 的 `??` 计数→0；tickets 桶内 `??` 逐笔登记为"未落链新票面"不计违例。不伤方案本体，放行 rev 顺手修。

结论：**PASS**（判据与验收全机械可跑；Y-3 为验收钉值加固项）。

## 四、审尺 4 · 读数对钉独立复跑 —— WATCH（核心桶表全复现；两处归因句不实）

**先立计数口径**：本席按主理人钉规以 `git -c core.quotepath=off ls-files` 及 `git ls-files -z | tr '\0' '\n'` 双口径跑，并复现假读数：默认 quotepath 口径现盘 `git ls-files | grep -c '/\.scratch/\|^\.scratch/'`＝**110**（假），off/z 口径＝**137**（真）——票面复点① 109 即同机理假读数（在 `329d16c` 时刻 `git ls-files`（默认口径）跑值）。

复跑对钉表（现盘 vs 票面）：

| 票面钉值 | 本席复跑 | 判定 |
|---|---|---|
| tracked .scratch 复点②＝136 | 现盘 137（z 口径）／137（off 口径） | **复现**——恰＋1＝票面自身（`00f7e7d` 落链后 `git show --name-only` 恰一件核死） |
| 桶表 仓根37/百工67/fuxi21/EAC11/其余0 | 现盘 38/67/21/11/0（z 口径分桶 grep 逐桶跑） | **复现**（仓根＋1＝本票） |
| tickets 桶 135／类B 恰 1 | 现盘 136／恰 1（点名件逐字全等＝`agent-experts/baigong-software-team/.scratch/COLLAB-STRUCT-1/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md`） | **复现** |
| 现行忽略态三样本 exit 1 | `git check-ignore -v .scratch/TMPLRULE-eng agent-skills/fuxi-skill/.scratch/FX-U26 agent-experts/baigong-software-team/.scratch/COLLAB-STRUCT-1` → exit 1 | **复现** |
| .gitignore 仅 L3/L13 注释含 scratch | `grep -in scratch .gitignore` → 仅 L3/L13 | **复现** |
| 未跟踪 199（拆 163＋2＋30＋4） | 现盘 202（拆 166＋2＋30＋4）／全仓 `??` 211（散件 9） | **同构**（链上微漂＋3，票面 L26 已自注微漂如实登记口径） |
| 文件级 102358 | 现盘 102403（`--untracked-files=all` 口径） | **同构微漂** |
| V1–V3/V5 探针预验钉值 | 本席自造探针 `agent-.../../.scratch/pm-scratchrev/probe.gitignore` 覆盖式复跑全兑现（§二.1 段读数） | **复现** |
| 探针残留自查＝0 | `ls .scratch` 过 `grep -c 'SWB-SCRATCHG'` → 0 | **复现** |
| 五锚 commit 在位 | `git cat-file -e` ×5（`329d16c6…ad`/`14416e9`/`f135855`/`adc4dc3`/`d83d452`）全 OK | **复现** |
| 靶检 exit 0 | `python share/check-pointers.py --target .scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v1.md` → exit 0（NOTE 级两行非违例） | **复现** |

**两处不实（本审件黄项主源）**：

- **Y-1（黄）· 链漂移注归因不实**：票面 L31 与 L46 称「109→136 差值全部来自链漂移期他案开票笔」「仓根 `.scratch/tickets/` tracked 数由 10 增至 37（SEMGV 线／PROJINIT／GWP-DEPLOY 票面他案落链所致）」——本席实翻驳倒：①`329d16c..14416e9` 区间恰 2 笔（`4f84484`/`14416e9`，FUXI-U38 回执与放行笔），`git diff --name-only 329d16c 14416e9` **零 .scratch 面文件**；②z 口径下两锚点 tracked .scratch 均＝136、仓根 tickets 均＝37（无变化）；③所谓"落链所致"的 SEMGV-T3 v2 落链于 `b4a75d5`（2026-11-08 18:18）、PROJINIT v1 落链 2026-11-06、GWP-DEPLOY 票面亦 11-06 线——全部先于 `329d16c`（11-10 18:56）两天以上。109→136 与"10→37"两个"增长"皆系 `git ls-files` 默认 quotepath 转义中文路径致 grep 漏数的**口径差**，非链漂移增量。HEAD 确漂（两锚隔 8 分钟两笔他案落链＋开工 staged 一枚＝并发实况真），但票面把口径差归因为开票增量，且该失实佐证喂给了候裁(b) 与 §八.3 排程建议——佐证须勘正，候裁(b) 本体仍合法成立（见审尺 2）。
- **Y-2（黄）· 观察 O-2 三连不实**：票面 L58 称仓根 `.scratch/multi-agent-collab-experts/`、`.scratch/multi-agent-collab-skills/` 为「镜像目录副本（文件级 102358 枚主体）」「该纪律生效日（2026-11-05）前后既有存量」——本席实翻：①两枚均为**符号链接**（`ls -la` → `-> /d/multi-agent-collab-experts` 与 `-> /d/multi-agent-collab-skills`），不展开计文件（git `??` 面各仅显一行），非目录副本；②文件级 102k 主体实为各席 QA 复测树（分桶计数头部＝`.scratch/FX-U14-qa` 9550、`FX-U15-qa2` 8933、`FX-U18-qa` 8251……两枚链接贡献＝各 1 行）；③链接创建时间戳＝**Nov 9 17:06**，晚于 TMP-DISC 生效日 2026-11-05 四天——「既有存量不追溯」前提不实（其按 §八.2 落点口径的合规性另论）。O-2 自注「不归本票射程」，零动规格本体，但呈给裁面的观察事实须改。

结论：**WATCH**——规格消费的全部关键读数（桶表/类B/探针预验/靶检/锚链）独立复跑成立；两条**归因/观察句**不实（Y-1/Y-2），不出规格错、出在证据叙述面，rev 勘正后可销。

## 五、审尺 5 · 排程/互斥登记 —— PASS（带 W-2 注）

- 与 FUXI-U38 在飞面互斥描述属实：票面 L7/L21 所登 staged 件 `agent-skills/fuxi-skill/.collab/tickets/2026-11-10-FUXI-FX-U38起草回执-v1.md` 现 tracked 在场（随 `4f84484` 落链），本席零触；§六.1「本票施工面只涉 `.gitignore`＋类B 单件，不涉 fuxi `.collab/` 任何面」与 §4.4/§4.5 闭集一致。
- 「FX-U2 票面『禁动 gitignore』辖 FUXI 案自身不辖本票」核实属实：该句在档＝`agent-skills/fuxi-skill/.collab/tickets/2026-11-06-FUXI-FX-U2-证据归位与封印票-v1.md` L22（封印登记语境），辖域确为该票自身施工面；本票增 gitignore 之授权源＝决策者 18:58 裁定＋开票前主理人确认授权链（票面 L142 自设），口径成立。
- §六.2 引用件路径本席抽检在册（TMP-DISC 票面、其 QA 审计件、ticket-template、README、share 三脚本）；`share/run-gates.sh` 零 `rg` 调用复核＝`grep -c 'rg ' → 0` ✓；`share/check-entity.py` L177 显式剪 `.scratch` ✓；`share/check-pointers.py` L200–L201 后缀索引除外 `.scratch/` 族（D-94 口径）✓；`share/check-ticket-reconcile.py` L329–L353 缺省票目录走文件系统枚举 ✓——§2.3 机理声明三条全部对码复现。基线补登：`python share/check-ticket-reconcile.py --root .` → exit 1（票 134／发现 184 全 WATCH 级）＝施工前后对拍起点在册，V7「不新增阻断」可跑。
- W-2（WATCH）：§六.1 排程句「本票放行笔先于任何 FUXI 续笔触及 gitignore 的窗口」为程序性安排——租约 `deny_globs` 只束本票施工席，机制上拦不住 FUXI 会话在放行-施工窗口内对 `.gitignore` 的并发笔；互斥靠主理人排程兑现，随注即可，不必加闸（本票面九行块与 evidence 行无交互已由 V5 实证，风险有限）。

## 六、判定台账

| 编号 | 级别 | 一句话 | 位置 |
|---|---|---|---|
| R 系列 | — | **红 0 项** | — |
| Y-1 | 黄 | 链漂移注把 quotepath 口径差（109→136、10→37）误归因为链漂期开票增量，而两锚间 diff 零 .scratch 面、所列票面均先于锚落链——佐证面须勘正（候裁(b) 本体不伤） | 票面 L31、L46 |
| Y-2 | 黄 | O-2 两枚姊妹仓镜像实为符号链接（非目录副本、非 102k 主体、时间戳 11-09 晚于 TMP-DISC 生效日）——观察事实三处不实须改 | 票面 L58 |
| Y-3 | 黄 | V3 硬钉 `.scratch` 族未跟踪计数→0 对 tickets 桶内未落链新票面敏感（并发窗口假 FAIL）——拆「桶外→0／桶内 `??` 逐笔登记不计违例」两读 | 票面 L133 |
| Y-4 | 黄 | 票头「候裁点单列 §七 六条」与 §七 实列七条、§八.1「七条」自相矛盾——一行改「七条」 | 票面 L9 |
| W-1 | -watch | 类A「刻意留档票据面」标签对仓根桶 12 枚 B 批过渡票（README L22/L88 在册候退役）欠准——裁(d) 措辞宜区分 | 票面 L100 |
| W-2 | watch | §六.1 排程互斥系程序性安排，租约 deny_globs 拦不住 FUXI 会话并发 gitignore 笔——主理人排程兑现即可 | 票面 L142 |

**计数（occurrence 口径）**：红 **0**／黄 **4**（Y-1、Y-2、Y-3、Y-4）／watch **2**（W-1、W-2）。双验＝台账行数（4＋2＋0）与正文逐项出现处对读全等。

## 七、总裁决

**PASS-with-conditions（放行呈裁可进，rev 须带四黄勘正）**：

1. 产品层核心问（忠实性）过关＝方案甲忠实落地 18:58 裁定目标态、tickets 桶豁免面最窄且经独立探针复现、135 件存量张力全部上呈候裁(d) 未票内自决——**放行不违裁定**。
2. 规格消费面全部关键读数独立复跑成立（桶表 137=现盘 136＋本票自身、类B 恰 1 逐字对钉、V1/V2/V5 探针预验钉值全兑现、靶检 exit 0、五锚在位）——**票可作施工输入**。
3. 放行前 rev 必带：Y-1（链漂移归因改「quotepath 口径差＋两锚间零 .scratch 增笔，HEAD 漂移实况保留」）、Y-2（O-2 改符号链接实况＋102k 主体归各席 QA 复测树＋时间戳如实）、Y-3（V3 拆两读）、Y-4（六条→七条）。四条皆叙述/钉值加固级，不动方案甲本体、不动候裁七条结构。
4. 候裁七条本席立场（产品职权内）：(a) 并入与否随裁，票面"未裁零含"处理妥当；(b) 合法登记面（佐证修正后更净）；(c) 方案甲读法下消解成立；(d) 产品层倾向**甲**（零迁移零翻案，承接 `f135855` 现行制＋README 白名单行现文仍准确），形态之争终裁权属决策者；(e) 产品层不持特殊取态，B-i 体例对口证据更足（`.collab/receipts/` 在管 95 件），B-ii 最轻手——两条均合格；(f) 倾向零随动（票面默认）；(g) 倾向随动一行 ignore 态表述（可选）。

## 八、审席自证

- 只读自证：被核票面及全部引用件零改动——本席 commit 面恰一件＝本审件（下笔 pathspec 限定·add/commit 紧邻·`collab:` 前缀·message 零 at 符号字符·FX_COMMIT_DECLARE 声明闸照走·禁 add -A/amend/--no-verify）。
- 临时复测物落仓根 `.scratch/pm-scratchrev/`（本票议题内合法用法：`probe.gitignore`／`lsfiles.txt`／`reconcile-out.txt`／`commit-out.log`），完工前删除附读数＝见下节删除读数登记。
- 落笔前靶检：`python share/check-pointers.py --target agent-experts/baigong-software-team/.collab/qa/2026-11-10-SWB-SCRATCHG-产品席独立审-v1.md` → 必 exit 0（读数随回执）。
- 并发零读：QA 席同票并发审的全部产出本席零读取。
- 探针方法登记：本席未触 `.gitignore`，规则族复跑经 `git -c core.excludesFile=<本席探针文件>` 覆盖式（机理承票面 §2.3 第 3 条同法）。

## 九、临时区清理读数登记（完工笔）

- 删除前清单：`ls .scratch/pm-scratchrev` ＝ `probe.gitignore`、`lsfiles.txt`、`reconcile-out.txt`（＋commit 轮 `commit-out.log`）。
- 删除执行：`rm -r .scratch/pm-scratchrev`（commit 落链后执行）。
- 删除后读数：`ls .scratch | grep -c 'pm-scratchrev'` ＝ **0**（见完工回报）。

（本件＝产品席 A 席独立审件·自包含单件·审毕即绿放行呈裁链下一步。）