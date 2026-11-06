# TK-PROJINIT 票面 v1 · QA 席独立审票 v1

- 开工 HEAD 读数＝`6e61902`（≥ 票面 ANCHOR `c858348`，实测 `git log` 确认 6e61902 为 c858348 之直接子件）·分支 main·开工时 `git status --porcelain` 无 tracked 脏项。
- 被核物＝`.scratch/tickets/2026-11-06-PROJINIT-项目锚定与初始化整改票-v1.md`（318 行·commit 6e61902 单件引入·`git show --stat` 实测 318 insertions 吻合）。
- 审法＝fresh eyes：全文通读＋票面引用实物逐条回原文/回脚本/回测试实测（含实测运行：runpy 探针读数、s4 全套跑通、四段 project_root() sha256 对拍）。未读任何其他席位对此票之审件。
- 判定口径＝通过／异议／建议 三值；异议＝票面声称与实物不符或判据不能机械执行；只谈生产力工具面，不评内容本体。

---

## 一、逐条判定表

| # | 票面条目（行号） | 判定 | 证据（实测） | 结论 |
|---|---|---|---|---|
| A1 | §开篇 L4「起草实测 HEAD＝c858348」＋§十三.1 | 通过 | `git log --oneline` 实测 c858348 存在且为 6e61902 父件；开工读数 6e61902≥c858348 | 锚合 |
| A2 | §一.1 L20／§3.1 L61／§十三.2 探针行号四读数（write-guard L48–76／lease-issuer L32–60／commit-audit L56–84／memory-neutralize L44–72） | 通过 | `grep -n "def project_root"`＝48/32/56/44；`grep -n "return pack"`＝76/60/84/72，逐一吻合；四段逐字抽取后 sha256 四值全等（66e81119…）＝票面「四段逐字相同」声称成立；首行 `def project_root() -> str:`、docstring 首句、末两行 `d = parent`/`return pack` 逐字命中 | 行号纪律成立，§3.1 替换锚文可指认 |
| A3 | §一.1 时序倒置缺陷描述（②以宿主预置 docs/STRUCTURE.md 为前提→④落包根） | 通过 | 实物 `project_root()` 函数体实测：②③ 均以 `os.path.isfile(join(d,"docs","STRUCTURE.md"))` 为判定前提，缺位落 `return pack`；本仓根 `docs/` 实测缺席（`ls docs` 无此目录）→开发态现势走 ④＝包根，与票面 §1.3 读数一致；runpy 实跑 write-guard/lease-issuer 读数＝`D:\multi-agent-collab-devkits\agent-experts\baigong-software-team`＝包根，坐实「四链全锚错处」前提 | 缺陷陈述与实物相符 |
| A4 | §开篇 L3「TK-PROJINIT 命中 commit-audit TK- 现闭集第三型——commit-audit.py L31–35 四型在册」 | 异议 | 实物 commit-audit.py L31–37：`TICKET_ID_PATTERNS` 现为**五型**（L32 SWB-、L33 TKT、L34 TK-、L35 .collab/tickets/、L36 GWP-P6-1 补入的 XXX-NNNN-WORD 型）；「L31–35 四型在册」为过时读数（L31–35 恰只覆盖前四型）。TK-PROJINIT 命中 L34 `TK-[A-Za-z0-9-]+` 本身成立 | 声称与实物不符（低危·不改结论方向）：闭集现五型，修票改文 |
| A5 | §1.3 L37「grep -n "return pack" 四读数＝L76／L60／L84／L72」＋L38 包 STRUCTURE 存在/仓根缺席＋L39 default_ledger_root（write-guard L85–87／lease-issuer L63–65）＋L40 test_enforcement 294 行/t13＝L259–272 逐行全等断言 | 通过 | 四读数实测全中；`agent-experts/baigong-software-team/docs/STRUCTURE.md` 存在·yaml 块 `project_root: "."`＋delivery_paths 六目录实测在案；仓根 `docs/` 实测缺席；write-guard L85–87／lease-issuer L63–65＝`SWB_LEDGER_ROOT 覆写∨<project_root()>/.collab/ledger` 实测吻合；test_enforcement.py `wc -l`＝294、t13 居 L260（注释 L259）至 L272，断言＝两 config 各席 deny_globs 逐行全等，实测在位 | 取证读数链全部复测通过 |
| A6 | §1.3 L41–45 config 写权实态四读数 | 通过 | 实测两 config：`docs/STRUCTURE.md` ∈ architect `deny_globs`（两 config 同文）；architect `write_globs` 含 `docs/adr/`；host `write_globs` 含 `docs/转正代写` 描述行；两 config grep `sources/` 零命中；engineer `write_globs` 含 `skills/**` | 五读数全中；H-1/H-2 前提（建档落笔无合格机械席位路）成立 |
| A7 | §3.1 替换代码块逻辑自审（_anchor_hit 自指闭合／_structure_hit 降档／⑤ fail-safe／SWB_REPO_ROOT 优先） | 通过（附 S5 建议） | 逐行推演：env 短路先回＝条款 1(a) 覆写优先成立；`_anchor_hit` normcase 排除包根＋首 `project_root:` 行相对值按 d 解析比对 d 自身＝自指闭合成立，坏锚/无键行均落 False；`_structure_hit` 排除包根＝旧②语义降档；全缺位 `return pack`＝旧④逐字保持；纯 stdlib 零 import＝「无跨件 import」条款成立。唯代码循环序＝anchor@cwd→anchor@pack上→struct@cwd→struct@pack上，与其自附 docstring 编号序（②struct@cwd 先于④pack上两路）存在一个场景差（见 S5） | 机制可用·判据 2a/2b/2c/3a/3c/3d 按此代码逻辑推演均可达钉值 |
| A8 | §3.2 挂点读数：SKILL.md 现 26 行／dev-discipline §九 已落链 commit 719f124／standard-sop.md L13＝步骤1接收用户需求 | 通过 | `wc -l`＝SKILL.md 26、dev-discipline 105；§九 居 dev-discipline L87（git log 实测 719f124 执行笔＝dev-discipline 单件追加 §九）；standard-sop.md L13 实测＝「1. **接收用户需求**」 | 挂点与工序位置声称全部吻合 |
| A9 | §3.4 产出文件数＝修改 6 件／超出即停手 | 通过 | 四脚本＋dev-discipline＋SKILL.md 清单闭合＝6；无隐藏新增仓内件（锚定件/四区/STRUCTURE 均声明落宿主项目，本仓零新增） | 闭集自洽，与 §六.9 双对面判据呼应 |
| A10 | §四 禁动面清单 vs 票面条款实质越界核查 | 通过（附 S4 计数建议） | 逐条扫正文：config 改文仅出现于 H-1/H-2/H-3 候裁（正文 §3.1.3/S6 均悬置待裁，未写入已决条款）＝零偷拍；hooks.json 明示否动（H-4 呈裁归后续）；版本三同源实测现值 0.1.30 三处吻合·票面不钉号；包 docs/STRUCTURE.md 零动；tests/ 全树零触（§五.3 红线明示）；S3 只引用 ledger-init.sh 既有件读用不改。唯「其余 sop scripts（9 件）」计数与实物不符：scripts 目录实有 16 件 .py＋1 件 .sh，剔在批 4 件后余 12 件 .py＋1 .sh（§五.7「其余 10 件工具面 cwd 锚」读数＝10 实测吻合，另两件 decision-pack/dispatch-builder 系 pack_root 锚非 cwd 锚） | 禁动面无实质越出；一处事实计数漂移（见 S4） |
| A11 | §五.3 测试面兼容声称（t13 零触必绿；t02/t03 显式接线锚换代零扰；该文件 grep project_root/SWB_REPO_ROOT 零命中） | 通过 | 实测跑 `python agent-experts/baigong-software-team/tests/s4/test_enforcement.py`＝PASS t01..t13 十三行·exit 0（现势绿基线）；t02/t03 实测均 subprocess＋`--ledger/--leases/--freeze-state` 显式重定向 Temp；该文件 grep `project_root`/`SWB_REPO_ROOT`＝零命中（声称限该文件，成立；tests 全树另有 count-assert.py L251 读 SWB_REPO_ROOT，不在该声称射程、其 repo_root 独立实现不随本批改＝tests 禁动面自洽） | 兼容处置成立；「不得为绿改 tests」红线可判 |
| A12 | §五.4/§五.5 fail-safe 保持＋包自声明不劫持宿主 | 通过 | 旧④语义「不开 fail-open 窗口」在新⑤逐字随迁（票面 §五.1 对照＋代码末段 `return pack`）；`_anchor_hit`/`_structure_hit` 均 normcase 排除 pack 自身＝包自声明 `project_root: "."` 不劫持两路成立（现行代码同构行为实测保持） | 兼容声称与替换代码逻辑一致 |
| A13 | §五.2 deploy-gate §五 四段链引用＋票型引用（§开篇 L5 皮总登记件 §一.4 已通过票型；L10 §一.3 预留 0.1.31） | 通过 | deploy-gate.md L32 实测＝「## 五、四段部署流程（装配→预览→人类闸→部署）」；`.collab/decisions/2026-11-06-皮总拍板-GWP放行与写权移交与memory写权.md` L11 实测「REMOTE-PUB 上架整改批顺延 0.1.31」、L13 实测「基础设施修复票票型＝按建议通过：人类批准开场＋临时豁免域＋修后回归探针」 | 两处引用逐点命中实物登记件 |
| A14 | §六 验收判据机械可执行性抽查（抽 9 组：1/2a/3a/4a/4b/4c/5/6/7＋9 组双对面） | 部分异议 | 组 6 实测现势绿（见 A11）；组 7 对拍法实测可行（本审件即以同法对四段抽段 sha256 全等）；组 1 py_compile 可行；组 3a/3c/3d 逻辑推演落包根可达钉值（本仓根与 D:\ 均无锚/STRUCTURE，实测排除旁路命中）；组 2a/2b/4c 推演可达；组 9 两跑 `git diff --name-only`/`--cached` 指向可指认。**唯组 4a/4b 命令口径自相矛盾**：`--leases .scratch/projinit/leases.jsonl` 为仓根相对字面，而该判据要求 WG 以 cwd＝FP 运行→相对路径解析为 `FP/.scratch/projinit/leases.jsonl`→租约文件读空→`load_leases` 返回 []→必 deny＝4a 预期 ALLOW 必然假红（4b 同口径连带）。4a 其余要素经实物核验可绿：LI `--seat architect --path-glob .collab/drafts/design/` 过写域子集校验（architect write_globs 含该行·实测）、`architect:qa` 过签注校验（COUNTERSIGN_SIGNER＝architect·lease-issuer L87）、WG allow 形态＝stderr `ALLOW`＋stdout 无 deny JSON＋exit 0（write-guard L326 实测形态吻合） | 判据主体可机械执行；4a/4b 需修口径（--leases 改绝对路径）后方可跑 |
| A15 | §六 判据 8 钉值自洽（dev-discipline 105→105＋§A 行数） | 通过 | §A 草件 fenced 块实测＝L299–317 共 19 行（含前置空行），§十 本体 18 行＋1 空行；前值 105 实测在案→后值钉＝124，差值判据机械可判；三 grep 读数（进场建档/swb-anchor×2）现值均 0→成文后 ≥1 可判 | 钉值自洽可执行 |
| A16 | §七 负样本判读 10 条 vs §六 判据组映射 | 通过 | 10 条逐条回读：1↔判据1/7、2↔2a/4a、3↔2b、4↔3a、5↔3c/3d、6↔4b、7↔5、8↔6、9↔8、10↔9——每条判据组皆有对应负读，方向语义（红＝停手/呈裁）与 §八 停止条件一致 | 负样本面闭集无悬空 |
| A17 | §八 停止条件＋§九 回滚＋§十 预算（步骤≤10／增删合计≤260） | 部分异议 | 停止条件五款均可指认（含「派工书要求改 config/hooks＝停手」＝与 H 区候裁互锁自洽）；回滚口径 git 单批 revert＋锚件删除即回落＝与探针语义一致成立。**预算不自洽**：§3.1 每脚本＝删 29 行（L48–76 段）＋增 55 行（§3.1 代码块实测 55 行）＝增删合计 84/件×4＝336，另 dev-discipline ≈19＋SKILL ≈4，总增删合计≈359＞260；括注「四脚本各≈55」实为只计增行，与「增删合计」口径冲突；步骤列举实测 11 个环节＞「步骤≤10」 | 预算若照跑必在完工核账时触发「超出即停手」＝执行期伪红；修票即可 |
| A18 | §十一 H-1~H-6＋登记不施工 vs 正文分列／偷拍核查 | 通过 | 正文六处涉 config/版本/hooks 全部以「候裁 H-x／呈裁／归主理人」悬置（§3.1.3、S6、§3.2 注、§五.6、§开篇版本位、§四），已决正文零 config 改文条款；H-5 声明「票面按最近者胜出实现·另裁则一行级改」＝预留修票口非偷拍 | 候裁不越权，分列纪律成立 |
| A19 | H-1 两案机械可行性核查（WorkBuddy 平台兼容性） | 建议 | 实测 write-guard hooks matcher＝`Write|Edit|MultiEdit/Write to file/Modify a file`（hooks.json），人类不经 agent 工具＝不受 hooks 拦截＝票面 §1.2.3「人类行为机械面不受限」对平台机制的利用正确；但 (a)「当票租约临时豁免域」在现盘**无机械实体**：lease-issuer 零裁量子集校验（L102–107）拒签任何越出 host write_globs 的请求行（host write_globs 实测不含 `.workbuddy/`），write-guard/config 均无「豁免」机制（scripts+config grep 豁免零命中）——(a) 的现盘真实落点＝host 经非 hooks 写径（如 Bash 重定向，Bash matcher 只路由 commit-audit）落锚，这属既有平台事实而非租约通道；票面未点破 | H-1(a) 现状描述需补实（见 S1），候裁本身程序正确 |
| A20 | 部署态（平台缓存目录）与开发态两形态探针换代成立性（平台兼容性） | 建议 | 开发态：本仓根无锚无仓根 STRUCTURE（实测）→⑤落包根＝与现势同·零回归（§五.7 声称成立，附条件＝仓根 STRUCTURE 须永缺席，票面已如实登记）。部署态：判据 4a 以显式 cwd＝FP 证明锚定路在「脚本进程 cwd ∈ 项目树」时成立；但实物 hooks 命令为相对路径 `python "../skills/sop/scripts/…"`（hooks.json 实测），钩子进程 cwd 归属＝平台侧未定项（GWP 候裁⑧「命令绝对化/`$CLAUDE_PROJECT_DIR` 载体」在册未施工＝本票 H-4 正确悬置）。若钩子进程 cwd 居包内/平台缓存树，则锚件双上溯路（cwd 上溯∨包根上溯）皆触不到用户项目根——锚件路在部署态的实际生效性条件系于 H-4 裁定；票面 §二「装配/部署态…四脚本同锚该根」为条件性成立。§3.1 新代码 `for probe in (_anchor_hit,_structure_hit)` 外循环＝锚类整体先于结构类（含 anchor@包根上溯先于 struct@cwd），与条款 2「锚定＞STRUCTURE」权威优先级一致，与 docstring ②③④编号序读感有别（编号序会被读成 struct@cwd 先于 pack 上溯路）——判据 2b 钉值在两读法下同值，无判据歧义，唯 docstring 措辞宜随票修正 | 开发态零回归坐实；部署态生效性条件已在 H-4 正确悬置（见 S3），非票面缺陷 |
| A21 | §开篇 L5／§一.2 决策依据引用（决策者三轮裁定＋总纲·2026-11-06·票面自转述） | 建议 | 核证：票面 §1.2 四款口径逐句实测命中 `.workbuddy/memory/2026-11-06.md` L89–96 皮总原话（含「首先…锚定」「应该是专家团按规范提示给用户」「xxx.md 甚至 xxx.txt…誊录校验通过后迁移」「只能引导用户，不能强制用户」逐句吻合）；但 `.collab/decisions/` 现行登记件中**无**本裁定批登记件（grep 裁定关键词仅 memory 命中）——按本团纪律 memory 无流程效力，裁定口径目前只有票面自转述＋memory 旁证两源 | 裁定内容与票面转述一致（非异议），但裁定登记件未落账＝呈主理人：施工前补誊录登记件，使票面决策依据有账内锚（见 S2） |
| A22 | §十四 §A 草案件 vs 票面正文互恰（工序六步表 ↔ §A S1–S6；校验六目 ↔ §A 括号六目缩句） | 通过 | 逐目对照：S1 锚定（含 SWB_REPO_ROOT 同效且优先）／S2 四区／S3 账本骨架／S4 收集入 sources／S5 誊录＋六目／S6 落笔——两文语义一致无矛盾；§A 六目缩句与 §3.3 六目逐目对应（四区枚举完备／delivery_paths 块／project_root 行／未声明询问／声明未建补建／原件格式不作要求）；§A「不代改原件、不要求用户按规范重写」与裁定③④口径一致 | 正文↔候裁↔草件三区互恰，无偷拍无漂移 |

## 二、建议清单（S·不阻断放行）

- **S1（H-1(a) 描述补实）**：票面 H-1 案 (a)「当票租约临时豁免域」在现盘无机械实体——lease-issuer 写域子集校验（L102–107）对越出 host `write_globs` 的请求行一律 REJECT exit 2（host write_globs 实测不含 `.workbuddy/`），四脚本与两 config grep「豁免」零命中。现盘真实可走通道＝host 经非 hooks 拦截写径（Bash 重定向——Bash matcher 只路由 commit-audit，实测）落锚。建议 H-1 呈裁文补此读数，免裁定基于「租约可豁免」误设。
- **S2（裁定登记件补账）**：见 A21——决策者四款裁定现无 `.collab/decisions/` 登记件，建议主理人在归批/放行前誊录落账。
- **S3（H-4 关联读数随票呈交）**：hooks.json 相对命令形制＝钩子进程 cwd 未定项（GWP 候裁⑧在册），建议 H-4 呈裁时附该项，作为「锚件路部署态生效性」判据。
- **S4（计数漂移修文）**：§四 禁动面「其余 sop scripts（9 件）」——scripts 目录实测 16 件 .py＋1 件 .sh，剔在批 4 件余 12 件 .py＋1 .sh（其中 cwd 锚 10 件＝§五.7 读数吻合，decision-pack/dispatch-builder 为 pack_root 锚）；禁动范围本身不受影响（全数仍禁），仅列举计数宜修。
- **S5（docstring 编号序措辞）**：见 A20 末段——新代码 probe 外循环序与 docstring ②③④编号序读感有别，建议施工时按代码实况校正 docstring 或条款措辞（逐字同款红线内四件同步改，不影响判据）。

## 三、异议清单（Y·修票项·均不改结论方向）

- **Y-1（A4·取证读数过时）**：§开篇 L3「commit-audit.py L31–35 四型在册」——实物 L31–37 现五型（L36 GWP-P6-1 补入 XXX-NNNN-WORD 型）。TK-PROJINIT 命中第三型的结论不受影响，读数须改。
- **Y-2（A14·判据 4a/4b 命令口径自相矛盾）**：`LI`／`WG` 的 `--leases .scratch/projinit/leases.jsonl` 为仓根相对字面，而判据要求 WG 以 cwd＝FP 运行——相对路径按进程 cwd 解析→FP 下无该文件→`load_leases` 读空→4a 预期 ALLOW 必假红。修法＝`--leases`（及判据 4 系列涉相对路径参数）改绝对路径。其余判据要素（architect path-glob 子集校验／architect 签注／ALLOW 输出形态）经实物核验全部可达，判据骨架有效。
- **Y-3（A17·预算不自洽）**：§十 增删合计 ≤260 与实算冲突——每脚本删 29＋增 55＝84×4＝336，加纪律面 ≈19＋SKILL ≈4 共 ≈359；括注「四脚本各≈55」系只计增行。另 §十 步骤列举 11 环节＞「步骤≤10」。不修则完工核账必触发「超出即停手」伪红。

## 四、总判

**放行带建议（带修票）**：票面技术核心（探针换代＋锚定声明件＋逐字同款红线＋fail-safe 保持）与仓内实物、既有 GWP 红线、测试面、禁动面全部对账通过；候裁 H-1~H-6 单列未混入已决正文，正文零偷拍；验收判据主体机械可执行。三处异议（Y-1 读数过时／Y-2 判据 4a/4b 相对路径假红／Y-3 预算口径不自洽）＝修票即可，不改放行方向。异议 3 条、建议 5 条。

——QA 席（qa-projinitrev2）·开工 HEAD 6e61902·本审件全部判定基于票面原文＋仓内实物实测，未参考任何其他席位审件。