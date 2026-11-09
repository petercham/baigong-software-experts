# TMP-DISC 票面 QA 席独立审票 v1（B 席·fresh eyes·证伪导向·只调研评审零施工）

- 被核件＝`.scratch/tickets/2026-11-05-TMP-DISC-temp-workspace-discipline-ticket.md`（开票 commit `546f850`，票面 157 行＝本席 `git show --stat 546f850` 实测 157 insertions 单件 commit）。
- 开工读数：`git rev-parse --short HEAD`＝`546f850`（≥546f850 ✓）；`git status --porcelain`＝空（净）。完工读数：HEAD＝`eb9de03`（他席在途推进，非本席产物）；本席收口前 `git status --porcelain` 仅本审计件＋commit 后自查（见第十一节）。
- 计数口径声明：除逐条注明外，全部＝**行计数**（`git -c core.quotepath=off grep -n <rev> -- <pathspec>` 行数），occurrence 口径另附 `grep -o | wc -l` 读数；计数一律按 commit 态（`git grep <rev>`）取数——多席共用仓下缺省工作树/index 态读数会被他席在途暂存扰动（本席实测两态有差，见第一节漂移读数）。判定全部附文件路径＋行号。
- 临时复测脚本／仿真件居仓内 `.scratch/qa-tmpdrev/`（本票纪律示范），完工删除，读数见第十一节。
- 锚定独立性申报：本席与产品席同时开审、未读其产品席件。诚实登记：必核项1 主式扫描的 grep 回显中出现过 `.collab/qa/2026-11-05-TMP-DISC-PM审票-v1.md` 的两行 incidental 引文（产品席件已被跟踪入库，扫描面命中无法规避）；本席全部判定系本席独立实跑产出（黄-1 系直接调用门禁机件自身算法复算所得，非引用产品席读数），未从该件采信任何结论。

## 总裁决

**红 1／黄 3／绿 12**＋观察 2。票面骨架（闭集对账、S1-S5 落位映射、锚行号、版本账缺口、平台兼容面）经独立复算全部立得住；**唯一红项＝§口径1 扫描面声明与口径2 基线钉值互斥**——按票面自身声明的扫描面，A2 前验基线不可复现（实测 47 行≠4）、施工后钉值 0 不可达（`.collab/` 历史 43 行旧措辞＝禁动面永不能清零），A2 按字面执行必死锁。修单一条一行级（口径1 排除清单补 `.collab/` 行），修后可放行施工。

## 一、前验读数复算（必核项1）——**红-1**

起草席申报：「旧措辞主式缺省扫描面基线读数＝4 命中（四脚本 docstring 各 1）」。本席按票面 §口径1 **字面扫描面**（＝`agent-experts/baigong-software-team/` 全 subtree，排除仅 `tests/`、`.scratch/`、`__pycache__/`、`*.pyc`、`avatars/`）复算主式四 pattern（§口径2）：

- **546f850（开票 commit 态）读数＝45 行＝45 occurrence／33 文件**（`git grep -n <rev> -- <pathspec>` 行计数＋`grep -o` occurrence 同值）；至 `eb9de03`（审票中段 HEAD）漂移＝47 行/48 occurrence/34 文件——漂移 2 行＝他席 TMP-DISC 产品席审票件新入面，印证「计数必须钉 commit 态」口径必要性（本席开工即按 commit 态取数）；
- **dd3e2cf（票面锚 commit）读数＝45 行＝45 occurrence／33 文件**；
- 其中 `.collab/` 面（qa 审票件＋receipts 回执，史实记录）＝dd3e2cf **41 行/29 文件**、546f850 **43 行**（差 2 行＝546f850..eb9de03 间产品席审票件两行入面）；
- 排除 `.collab/` 后（＝起草席实际测但未声明的面）：恰＝**4 行／4 文件**＝`commit-audit.py:17`／`decision-pack.py:14`／`dispatch-builder.py:19`／`write-guard.py:23`，与票面四件行号逐一同点 ✓。
- 起草席担心的其他命中面复扫：`agents/` 五卡＋`skills/software-orchestration/` 全卷 `grep "Temp"`＝**0 命中**（除四脚本外，交付面 `agents/`∪`skills/` 全树 `grep "Temp"`＝0）——旧措辞命中不在正文卷/席位卡/deploy-gate，而在 `.collab/` 史实面。

**红-1 判由（可机械性死锁）**：§口径1 是 A2/A3 的声明扫描面，未排除 `.collab/`；而①A2「施工前基线＝4」按字面扫描面实测＝45（546f850 commit 态，行/occurrence 两口径等值；eb9de03 中段 HEAD 漂移至 47），不可复现（H6 会逼工程师按实测登记上报，前后对拍失锚）；②A2「施工后命中＝0」在字面扫描面下永不可达——`.collab/` 43 行旧措辞＝append-only 史实面＋票面自身禁动面（「`.collab/` 账本面」）＋红线（口径四款不改），工程师无法改动任何一条；③A2 宽式 `grep "Temp"` 白名单同样未列 `.collab/` 史实命中（宽式在 `.collab/` 命中大量 Temp 字样）→「非白名单命中＝违例回扫 S3」同样死锁。**修单 R-1（一行级）**：§口径1 排除清单补一行 `.collab/`（措辞建议：「排除：tests/、.scratch/、**`.collab/`（史实锚面＝旧措辞留档不入违例计数，登记读数即可）**、__pycache__/、*.pyc、avatars/」），并把基线两读数（字面 47／净面 4）补登口径行，其余判据零动。

## 二、闭集 15 件对账（必核项2）——绿

- 15 件逐件 `git ls-files --error-unmatch`：15/15 **IN**（无缺件、无票面笔误件）。
- S-x 落位映射一一对应：S1→dev-discipline（1）＋S2→SKILL.md（1）＋S3→四脚本（4）＋S4→五席位卡（5）＋S5→三同源＋README（4）＝**15＝声明闭集全等**；无孤儿规格、无闭集外落改暗示（禁动面逐条＝README 版本账外其余、tests/、deliverables/、.collab、.gitignore、两基线副本——与闭集零交集）。
- 「开票侧实体核验＝以上 15 件 dd3e2cf 在位」复测＝成立（HEAD 在位＋dd3e2cf 锚行号命中见第三、四节）。

## 三、定稿文本忠实＋禁例引自洽（必核项3）

- 四条款真源逐句对照（派工书转述四款 vs §八四款）：款1 适用范围列举＋不分席位 ✓；款2 唯一落点＋多仓并排各仓各自 `.scratch/`＋三禁（盘根裸路径／系统 Temp 含 Windows `AppData\Local\Temp` 与 Git Bash `/tmp` 例举／仓外自建点）✓；款3 清理判据＝删除＋读数或归档＋读数＋收口态零残留＋消费面（主理人汇编＋QA 人工闸）✓；款4 禁仓外 Temp 模板＋〔禁例引〕作废句＋席位拒指权 ✓——**无走样**（口径真源见第五节登记面读数）。
- 〔禁例引〕标记：当前**交付面**（排除 tests/.scratch/.collab）`grep "〔禁例引〕"`＝**0**（全仓仅票面自身 4 处＋`.scratch/tickets/2026-11-05-CLN-PURE…票` 1 处裸「禁例引」＋两份 `.collab/research` 旧案裸串——先例口径＝CLN-PURE 票 A3 句「禁例引语句如出现须带『禁例引』标记方入白名单」在册 ✓）。S1 成文后 dev-discipline 〔禁例引〕＝1 处（§八.4）＝A3 钉值 1 **可机械成立** ✓；旧措辞经标记＋A2 豁免规则（含标记行不计）不入违例 ✓，与「4→0」（净面口径）自洽——但仅在 R-1 修单落地后自洽（见红-1）。
- 节号连续性：dev-discipline 现有 `## 一`~`## 七`（L6/18/38/46/52/61/71 实测），新增 `## 八` 号序正确；S1 追加点＝现末行「4. 当期无机检义务。」实测＝文件末行 ✓。

## 四、判据可机械性 A0–A7（必核项4）

- **A0**：run-gates/check-pointer-closure 两件在位 ✓；本席基线实跑：`run-gates.sh`＝**GATE PASS exit 0**（发现 9211 条均②路由）；`check-pointer-closure.py` 缺省两包面（`agent-skills/external-advisor-collab`＋`agent-experts`）跑通 exit 0（WATCH 尾部读数在册）。钉值口径成立。黄外观察见 O-1（A0 自身证据件写 `.collab/evidence/gates/`＝gitignore 排除面，不在 `.scratch` 落点口径内——既有机件行为，登记不拦）。
- **A1**：五个锚串当前各＝0（可 0→1 迁移核验）✓；`^## 八` 前 0 后 1 可测 ✓。
- **A2**：**红-1**（见第一节）——钉值 0/4 仅在未声明的净面上成立；豁免规则（〔禁例引〕行不计）本身清晰可测 ✓；宽式白名单五列对交付面完备性本席已独立核＝绿（见下条）。
- **A3**：钉值 1 可达 ✓（第三节复算）。
- **A4**：前基线＝五卡 `grep -c "席位守则·dev-discipline 卷"` 各 **0** ✓；插入锚行号＝dd3e2cf 实测 lead L75／product L37／architect L37／qa L37／engineer L38——**五锚全中** ✓；五卡新行含「本席」＋卷名自指 ✓（lead 行含「本席」✓，四卡行含「本席」✓）。`git show --stat` 行数读数口径可行 ✓。
- **A5**：三同源现值行号复测＝`plugin.json:3`／`.codebuddy-plugin/plugin.json:3`／`bundle.lock:5` **全中**；且三文件 `"version"` 行各**恰 1 处**（bundle.lock components 组件行无 `"version"` 键＝只 ref tag）→ S5 替换与 A5 grep 读值均无歧义 ✓；`SKILL.md` frontmatter `version: 1.1.4`＝L5 实测 ✓→1.1.5 可测 ✓。
- **A6**：`grep -c "版本账 v0.1.24" README.md` 现值＝**0**；`v0.1.25`＝0；插入位锚（「- **版本账 v0.1.23**（…」行＝README L65，「## 头像」节＝L67）实测在位可达 ✓。README 版本账序本就非单调（v0.1.20 在 L39、v0.1.7 在 L54），append-only 插 L65 后不违既有例 ✓。
- **A7**：run-gates 前后对拍＋closure WATCH 不新增＋py_compile＋pytest 前后对拍——四件 docstring 文案改动不在任何 tests/ 断言面（`tests/` 对「重定向至 Temp」字面 grep＝**0 命中** 复测 ✓）→ 可机械 ✓。**并发噪音豁免口径缺声明（黄-3 之外的口径观察 O-2 一并计）**：多席共用仓并发时 run-gates/closure 前后对拍可能被他席在途写入扰动——票面未写「他席并发致读数漂移→逐笔归因即可」的豁免句（A7 已写 closure「若新增逐笔归因上报」＝半覆盖；run-gates「基线发现数不新增」无归因豁免句）。不单独列黄，并入 O-2。

## 五、版本账缺口实证（必核项5）——绿

- README 无「版本账 v0.1.24」行＝实测（grep 0）✓ 缺口属实；
- bump 落点＝`git log -S '"version": "0.1.24"' -- plugin.json`＝**`a885ad7`**（CLN-PURE 施工批），`git show a885ad7 --stat` 含 README 行数＝**0**（该批未触 README＝漏登记属实）✓；
- S5 补记文本恰当性：逐目对 `a885ad7` 事实——`bundle.lock assembly_exclude` 恰**五类**（README.md／docs 交接件／deep-research README／EAC 90-changelog／tests/，json 解析实测）✓；EAC 组件 ref＝`external-advisor-collab@v1.1.3` ✓；三同源 0.1.23→0.1.24 于该 commit ✓——补记无虚笔，「补记：据既有 commit 回补」字样符合 append-only 前例（README L59 v1.2.4 行同款补记句式先例在册）✓。
- 三同源现值 0.1.24 三处行号复测见 A5 条（L3/L3/L5）✓。

## 六、WorkBuddy 平台兼容性面（必核项6）——绿

- 落点可写可达实证＝本批全程：`.scratch/qa-tmpdrev/` 建→写脚本→跑→删，仓内 `.scratch` 先例在位（`agent-experts/baigong-software-team/.scratch/tickets/` 已跟踪多票；仓根 `.scratch/tickets/` 亦有在位票）。
- 装配面冲突核验：票面**未声称** assembly 排除 `.scratch`（背景段只引 2026-11-03 既决票面落位＝无声称失实）；本席回 `publish.py` 实测确认兼容性：L730 `if any(seg in (".collab", ".scratch") for seg in rel.split("/")): continue`（PUB-EXCL 段）＝`.scratch` 任何路径段裁出装配面 ✓；L795-817 `assembly_exclude` 解析＋L890-908 谓词共用 ✓——§八落点与装载/注册机制零冲突。
- `.gitignore` 行为实测：`git check-ignore -v "…/.scratch/<票号>/probe.txt"` exit 1＝不忽略（临时物不入史实面靠 §八.3 清理判据人工闸收口，与 .gitignore 制①「项目 .scratch/tickets/ 默认入库」声明一致）✓ 无机制矛盾。
- **黄-2（口径锚定）**：§八.2「所属项目**仓根** `.scratch/`」锚定口径未钉——本仓现态**双 `.scratch/tickets` 树并存**（仓根 `.scratch/tickets/2026-11-05-PUB-EXCL-…票` 与壳层 `agent-experts/baigong-software-team/.scratch/tickets/…`，本票自身落壳层）；机件口径真源＝hooks-map「路径锚定」款「项目根＝含 docs/STRUCTURE.md 之探针锚目录」＝壳层（实测 `agent-experts/baigong-software-team/docs/STRUCTURE.md` 在位、仓根无 `docs/STRUCTURE.md`）。判定不受阻（A 系列判据不含 `.scratch` 路径解析），但「仓根」二字歧义恰是本次事故（落点漂移堆垃圾）的孪生风险。修单建议 Y-2 一行：§八.2 或口径节钉「项目根＝hooks-map 路径锚定探针（docs/STRUCTURE.md）锚目录」。

## 七、候裁项 tests/ 面事实基础（必核项7）——事实对、计数口径含糊（黄-3）

- 「tests/ 经 assembly_exclude 裁出装配面」＝**事实成立**（bundle.lock 顶层 `assembly_exclude` 含 `"tests/"`，json 解析实测）✓；
- 「probes 确用 mktemp／系统 Temp」＝**事实成立**（`tests/probes/*.sh` 11 件 `grep -l mktemp`＝11；s2/s3/s4 用 `tempfile.TemporaryDirectory()`＝运行器自清理，实测样例行 s2:128／s3:131／s4:283）✓；
- 「共 12 文件命中 Temp 族」＝**计数口径未声明且多口径不同值**：全 tests `grep -l "Temp"`（区分大小写）＝**16 文件**；`grep -rl -i temp`＝**25 文件**；仅 `tests/probes/` 面 `-i temp`＝**12 文件**（＝唯一使「12」成立的读径）。核心裁决理由（仓内验收件非交付面条款面／进程内 tempfile 自清理≠人工席堆目录不收口／改动量大无交付面效力）事实基础无误→候裁两案均可拍，不红；计数行建议修单 Y-3 钉口径（「probes 目录 temp 族（不分大小写）12 文件」或改「16 文件（区分大小写 Temp）」）。

## 八、S4 自指行形式约束复测（票面 L100 委托 QA 复测项）——**黄-1**

本席直接调用门禁机件 `tools/check-source-of-truth.py` 自身函数（`max_cjk_overlap`＋`mask_quote_exempt`＋`extract_clause_units`，S1 定稿文本注入壳层卷仿真件跑——仿真件居 `.scratch/qa-tmpdrev/` 已删）复算「与 §八条文最长连续重合」：

- **四卡共用行**＝**9 CJK**（段＝『所属项目仓根 `.scratch/<票号>/`：』）＜12 阈值 ✓ 票面申报成立；
- **lead 卡行**＝**13 CJK**（段＝『唯一落点＝所属项目仓根 `.scratch/<票号』）≥12＝按 handoff 卷 §十.3（实测阈值条款＝handoff-discipline.md L58「≥12 CJK 判复写」）越线——票面 L100 自检只报 9 值、未分 lead 行另算＝**自核申报不完备**。
- 为何黄不红：现装机件面**不会误报**——C 段（MC-SEAT-DECL）只扫白名单节（`## 写权边界`／`## 交接与收口声明`，S4 明言新行入席位守则节不入白名单节）；A1（MC-SOT-1）行级重合需 ≥2 文件同文本（lead 行单例）；且 run-gates 缺省调 `check-source-of-truth.py --root` 时 `--pkg` 缺省＝姊妹仓视频包（实测本仓 sot 跑 129 文件＝agents 7＋skills 122，**baigong 席位卡不在缺省扫描面**，findings 引用 baigong＝0）。→ 无门禁红信号，属书面自核声明失真＋扩面后隐患。修单 Y-1：lead 卡行改写避『唯一落点＝所属项目仓根』连续段（如「落点只认所属项目 `.scratch/<票号>/` 区」），或票面把 lead 行复测读数（13 CJK）如实分列并呈 handoff §十.3 候裁。

## 九、其余绿项汇总（判定＋读数）

1. 闭集 15 件对账全等（第二节）；2. S3 四旧句 dd3e2cf 行号 L17/L14/L19/L23 逐字全中＋新句无 Temp 字样（四新 docstring 手核零 Temp 串）；3. tests 对 docstring 旧句零在位断言申报＝实测 0 ✓；4. dev-discipline 节号／末行锚（第三节）；5. A3 〔禁例引〕交付面现 0→1 可达（第三节）；6. A4 前五卡基线 0＋五插入锚行号全中（第四节）；7. 三同源现值＋唯一 version 行＋SKILL.md 1.1.4@L5（A5 条）；8. README v0.1.24 缺口＋补记文本对 a885ad7 逐目忠实（第五节）；9. publish.py PUB-EXCL 段＋.scratch 可写可达＋gitignore 无矛盾（第六节）；10. 候裁三事实基础成立（第七节）；11. 宽式 Temp 白名单完备性：交付面（排四脚本＋tests/.scratch/.collab/avatars）`grep "Temp"`＝**0 命中**（exit 1 实测）→施工后宽式命中＝白名单五列全集，A2 宽式在交付面可执行；12. A7 机检链（GATE PASS exit 0＋closure exit 0＋pytest 面不涉 docstring）可执行。

## 十、缺陷台账与计数

| 编号 | 级别 | 判由 | 修单 |
|---|---|---|---|
| 红-1 | 红 | §口径1 扫描面未排除 `.collab/`：A2 基线「4」按字面扫描面实测＝45 行/33 文件（546f850 commit 态；中段 eb9de03 漂移 47/34）不可复现；施工后钉值 0 不可达（`.collab/` 43 行史实旧措辞＝禁动面＋append-only）；宽式白名单同缺该列→A2 前后判据字面死锁 | R-1：§口径1 排除清单补 `.collab/` 行＋补登两口径基线读数（一行级） |
| 黄-1 | 黄 | S4 自核「最长连续重合＝9 CJK」未覆盖 lead 卡行：机件口径复算 lead 行＝13 CJK≥12（handoff §十.3），四卡行＝9 ✓；现门禁不误报（白名单节外＋缺省 sot 扫描面不含 baigong 卡） | Y-1：lead 行改写避连续段，或票面分列 13 CJK 读数呈候裁 |
| 黄-2 | 黄 | §八.2「所属项目仓根」锚定歧义实证：仓根与壳层双 `.scratch/tickets` 树并存；机件真源锚（docs/STRUCTURE.md 探针）＝壳层，票未钉 | Y-2：§八.2 或口径节钉探针锚句（一行级） |
| 黄-3 | 黄 | 候裁计数「12 文件 Temp 族」口径未声明：实测区分大小写全 tests＝16 文件／不分大小写＝25／仅 probes＝12（唯一成立读径）；核心理由三事实全对故不红 | Y-3：计数行钉口径 |
| O-1 | 观察 | A0 run-gates 证据件写 `$ROOT/.collab/evidence/gates/`（gitignore 排除面）＝§八.3「git status 净」读数口径盖不到 ignore 面运行残留；既有机件行为不拦 | 不改票，收口登记附注即可 |
| O-2 | 观察 | 口径2 主式「仓外 Temp」⊃「置仓外 Temp」包含重叠（同句可双计）＋A2 未声明行/occurrence 口径（本席钉 commit 态实测两口径等值＝546f850 45/45，但 eb9de03 工作推进致两口径分叉 47 行/48 occurrence）＋缺省 `git grep` 无 rev 时读 index/工作树态会被他席在途暂存扰动——A2 前后读数应钉「rev 态＋口径」双声明。对净面钉值 4/0 无影响。A7 run-gates 对拍无他席并发归因豁免句（closure 有半覆盖句） | 可选随行修单，不列缺陷 |

**计数＝红 1／黄 3／绿 12**（绿＝第九节 12 条）。修单 R-1 落地（＋宜带 Y-1/Y-2/Y-3 三一行级）后票面可机械执行性闭合，建议放行工程师施工；口径四款本体不改判（修单全部落在口径声明面，不触碰定稿四款文本）。

## 十一、收口自证（本席纪律示范）

- 临时物清单＝`.scratch/qa-tmpdrev/`：`overlap_check.py`／`dev-discipline-sim.md`（S1 仿真壳件）／`sot.out`／`rungates_before.out`——删除前 `ls` 读数四件在册；`rm -rf` 后 `ls .scratch/`＝`tickets` 单目录（零残留读数 ✓）。
- 除本审计件外交付面／账本面零写入；状态零迁移（核票阶段无状态面）；未用 `--no-verify`；commit 见下（`collab:` 前缀·pathspec 限定本件）。
- 本席收口读数：`git status --porcelain` 于本件 commit 后＝不含本件；`git show --stat HEAD` 自查单件（读数随回报附 main）。

——qa-tmpdrev · TMP-DISC 独立审票（B 席·本席实跑·除本报告外零触碰·产品席件 incidental grep 两行外未读未采信）
