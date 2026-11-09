# TK-PROJINIT 票面 rev2 · QA 席修正点抽查复审 v1

- 开工 HEAD 实测＝`1b77be7`（≥ 任务书下限 `1b77be7`，实测吻合）·分支 main·开工时 tracked 面无脏项（`git status --short` 命中仅 untracked `.scratch/`、`.collab/ledger/` 类运行面）。
- 被核主体＝`.scratch/tickets/2026-11-06-PROJINIT-项目锚定与初始化整改票-v2.md`：`wc -l` 实测 401（无尾换行符·`tail -c 1`＝`.`；git numstat 口径 89bb1a0 引入 402 增行＋1b77be7 1/1 微笔＝票面行数与任务书 401 行吻合）。
- 前序件盘上直读（四件）：会师对拍修单 `177f5bc`（177 行）、本席 v1 审件 `cb23a20`、裁定登记件 `d3bc512`＋§三之补 `5f2cf45`。未读产品席对 rev2 任何评审件（禁读面遵守）。
- 审法＝fresh eyes 证伪导向：三异议销账＋建议销账＋机械判据独立复跑，全部本席亲自实测（`git show` 版本级读数＋盘上实物回原文＋独立 python/awk 双验计数＋occurrence 口径 `grep -o | wc -l`），工程师/起草席申报零采信；不执行施工，只判可机械性与钉值可复现性。
- 计数口径声明：本审件所有计数＝occurrence（`grep -o … | wc -l`）为主，行数用 `wc -l`/python `splitlines` 双验；每判定附文件＋行号。
- 判定口径＝通过／异议（红＝阻断·黄＝修票级不阻断）／建议 三值。

---

## 〇、开工复测（票面 §十三 五组读数本席独立复打）

| 项 | 票面声称 | 本席实测 | 判定 |
|---|---|---|---|
| §十三.2 四脚本 `def project_root`／`return pack` | 48/32/56/44 · 76/60/84/72 | `grep -n "def project_root\|return pack"`＝write-guard 48/76、lease-issuer 32/60、commit-audit 56/84、memory-neutralize 44/72 | 命中 |
| 四段逐字同款 | GWP 红线 | 四段（L48–76／L32–60／L56–84／L44–72）独立抽段 sha256 四值全等＝`0858bcfc180a…` | 命中 |
| §3.1 替换锚文（docstring 首句） | 四件命中 | `grep -c 'GWP-P1-1 探针序换代：① SWB_REPO_ROOT＝项目根覆写面（测试重定向·覆写语义零动）；'`＝四件各 1 | 命中 |
| §十三.3 三读数 | 包 STRUCTURE 在／仓根 `docs/` 缺席／仓根 `.workbuddy/` 实存无 `swb-anchor` | `ls docs`→无此目录；`ls .workbuddy`→仅 `memory`；`ls .workbuddy/swb-anchor`→不存在 | 全命中 |
| §十三.4 基线 | dev-discipline 105／SKILL 26 且 L23＝deploy-gate 索引行／test_enforcement 294 | `wc -l`＝105／26／294；SKILL L23 实读＝deploy-gate 索引行逐字在位 | 全命中 |
| §十三.5 版本三同源 | 0.1.30 | `grep -o '"version": *"[^"]*"'`＝plugin.json／.codebuddy-plugin/plugin.json／bundle.lock 均 `0.1.30` | 命中 |
| runpy 现势开发态读数 | 走④落包根 | `python -c "import runpy; print(runpy.run_path(...write-guard)['project_root']())"`＝`D:\multi-agent-collab-devkits\agent-experts\baigong-software-team`＝包根 | 命中（现势缺陷坐实·与 §1.1 时序倒置陈述相符） |

开工复测七组全中：票面行号纪律在 rev2 成立，§3.1 替换锚文可指认。

---

## 一、复审主面逐项判定

### 1. Y-1 五型读数（主面 1）→ 通过〔销账〕

- 实物回原文：`commit-audit.py` L30–37 实测＝L30 注释行、L31 `TICKET_ID_PATTERNS = [`、L32 SWB 型、L33 `TKT\d+`、L34 `TK-[A-Za-z0-9-]+`、L35 `.collab/tickets/`、L36 GWP-P6-1 补入 `[A-Z][A-Z0-9]{1,9}-\d{3,4}-[A-Z][A-Z0-9]{1,14}`（行内注释自注「GWP-P6-1 项目票号 XXX-NNNN-WORD 型」）、L37 闭括号。
- rev2 §开篇 L3「L31–37 实物＝五型在册，L36 系 GWP-P6-1 补入的 XXX-NNNN-WORD 型；v1『四型』读数过时，命中结论不变〔D-2〕」＋§1.3 L81「L32 SWB、L33 TKT、L34 TK-、L35 .collab/tickets/、L36 GWP-P6-1 补 `XXX-NNNN-WORD` 型」＝逐型逐位与实物全等。
- TK-PROJINIT 命中 L34 `TK-[A-Za-z0-9-]+\b` 复核成立。**Y-1 勘正如实、销账。**

### 2. Y-2 绝对路径（主面 2）→ 通过带口径瑕疵〔销账＋黄①〕

- rev2 §六 L254 夹具段：`R0＝仓根绝对路径（bash 形如 /d/multi-agent-collab-devkits）`＋警示句「相对路径按进程 cwd 解析，WG 以 cwd＝FP 运行时仓根相对 `--leases` 会读空＝必假红」；L256 `LEASES＝$R0/.scratch/projinit/leases.jsonl`（绝对）；判据 4a（L270）`--leases $LEASES`（绝对·D-3）＋`--path <FP绝对路径>/...`；4b（L271）同口径；判据 3 系列（L258）runpy 逐件独立进程＋`r'<脚本绝对路径>'`。rev1 假红链条（相对 `--leases`＋cwd＝FP→`load_leases` 读空→必 deny）已消灭。销账成立。
- 可机械性实物佐证（本席回脚本核）：LI `--leases` 默认缺省但可覆写（lease-issuer.py L135）、LI 签发前 `os.makedirs(dirname(leases_file), exist_ok=True)`（L113）；WG `--leases`/`--ledger`/`--map` 均可覆写（write-guard.py L295–297）；`ALLOW` 输出形态＝stderr `ALLOW write-guard path=…: {reason}`＋exit 0（write-guard.py L323–326）＝4a 钉值形态与实物吻合；architect `write_globs` 含 `.collab/drafts/design/`（两 config 之 seat-permissions.json 实测命中）过 LI 写域子集校验；`COUNTERSIGN_SIGNER＝"architect"`（lease-issuer.py L21）＋L87 签注格式校验＝`architect:qa` 过关。判据 4 骨架可跑。
- **黄①（口径瑕疵）**：`R0` 声明采 bash 形 `/d/multi-agent-collab-devkits`——本席实测该形制仅在「bash→argv 自动路径转换」通道成立（`python -c … /d/multi-agent-collab-devkits` 经 argv 传入＝python 侧见 `D:/multi-agent-collab-devkits` 可达）；但**写进 python 源内字符串字面量则不转换**：`os.path.exists('/d/multi-agent-collab-devkits')`＝False。判据 3 系列/4c/5b 的 runpy 形制恰是把绝对路径写进 `python -c "…run_path(r'<路径>')"` 源内——执行席若按票面「bash 形」的 R0 填值即 FileNotFound＝假红。修票级：R0 应写死 Windows 盘符形（`D:/…` 或 `D:\\…`）或双形并注明各通道适用性。

### 3. Y-3 预算自洽（主面 3）→ 口径已修、基数失实带尾差〔部分销账＋黄②③〕

本席独立 numstat 口径重算（不采信票面任何「实算」声称）：

- 删行基数：四脚本各段＝76−48＋1／60−32＋1／84−56＋1／72−44＋1＝**29×4** ✓（与票面「删 29」一致）。
- 增行基数：§3.1 代码块行数＝**55 行**（python `splitlines` 抽取 fenced python 块＝55；awk 独立二验＝55）。票面 §3.1 L104「56 行实算〔D-4 口径基数〕」＋§十 L319「增 56（§3.1 代码块实测 56 行）」——**声称 56 ≠ 实测 55**。差异最可能来源＝替换插入时与前置代码间的分隔空行＋1（可解释），但票面把 55 行的块标注为「实测 56 行」＝与 v1 Y-3 同类的「实算失实」残留，唯幅度从「口径级」缩至「1 行级」。
- 独立合计复算：4×(29+55)＝336＋纪律面 31（§A 24＋§B 删 3＋增 4＝见主面 5 实测）＋SKILL ≈5＝**≈372**；票面声称 ≈376（按 56 计）＝差 4。两者皆 ≤420 ⇒ **上限结论不变、不会触发完工核账伪红**；「各≈55 只计增行」旧口径确已消灭（L319 明文作废）。
- §〇表 D-4 行勘正前后一致性：`git show 1b77be7` 微笔 diff 实测＝该行由「纪律面 ≈59＋SKILL ≈5≈404」改「纪律面 31＋SKILL ≈5≈376」；改后与 §十 L319 现文逐字同值＝**前后一致销账**（1b77be7 numstat＝该件 1 增 1 删＝纯微笔·未触他行）。
- 步骤收敛复核：L319 列举段 occurrence 实测＝「→」8 个⇒按箭头切分＝**9 环节**；若把「纪律面两笔（§十追加＋§九.3 改写）」按两笔拆开＋SKILL 随动独立计＝**11 环节**。两种自然读法均≠票面自称「恰 10 环节」。v1「11＞≤10」矛盾在 rev2 未逐值闭合，只是从「超出上限」变为「列举与自称计数不合」。修票级＝写死计数口径（逐环节编号列出＝恰 10，或改口径注）。
- 结论：D-4 口径改造方向正确、上限自洽可达，唯两处「实算」尾差（56/55、恰10/列举 9|11）＝修票项。

### 4. 重合①②（主面 4）→ 全通过〔销账〕

- **R-1 计数**：`ls scripts/ | grep -c '\.py$'`＝16、`grep -c '\.sh$'`＝1（目录含 `__pycache__`）；剔在批 4 件＝**12 py＋1 sh**——rev2 §四 L228、§1.3 L80 声称吻合。cwd 锚复算＝逐件 grep `os.getcwd()`：CWD 组＝baseline-backfill-demo／freeze-unfreeze／intake-register／liveness-selfcheck／promote-manifest／reconcile-daily／serial-gate／shadow-replay／sign-verify／state-transition＝**10 件**；PACK 组＝decision-pack／dispatch-builder＝2 件——与 §1.3「cwd 锚 10 件、decision-pack/dispatch-builder 系 pack_root 锚」全等。
- **R-2 docstring 序同构**：票面代码块 docstring 序＝① env 覆写在场即回→② 锚定件路「先自 cwd 上溯、后自包根上溯」→③ STRUCTURE 事后校验路「先自 cwd 上溯、后自包根上溯」→④ 落回包根 fail-safe；代码循环＝`for probe in (_anchor_hit, _structure_hit):` ×`for d0 in (os.getcwd(), os.path.dirname(pack)):`＝anchor@cwd 链→anchor@包根上链→structure@cwd 链→structure@包根上链→`return pack`。逐层比对＝**严格同构**（锚类整体先于结构类、各类内 cwd 先于包根上）；R-2 销账成立。四件逐字同款红线经判据 7（sha256 对拍）锁死，属可判机械面。

### 5. 机械判据抽核（主面 5）→ 大体可判，判据 11 带软出口〔黄④〕；行数全中

- **判据 5b 可判且钉值可复现**：推演＋现盘佐证——cwd＝包根时，`_anchor_hit(pack)` 被 normcase 排除（代码 L113–114），自包根上链＝`dirname(pack)` 起：仓根实测无 `swb-anchor`（§〇表已测）、无 `docs/STRUCTURE.md`（仓根 docs 缺席）、`/d` 与 `D:\` 层均无锚/结构（v1 审 A14 已实测排除旁路）→ 落 `return pack`＝钉值「四读数＝包根」可复现；FP 锚不在该起点祖先链上→必不命中＝与票面「已知边界行为」语义一致。判读 §七-8（L295）语义正确（本判据红＝边界语义变呈裁，≠修复失败）。
- **判据 10 依据实物核实**：commit-audit `prehook`（L153–173）＝`classify_command` 只机检 amend/rebase/force-push（CMD_PATTERNS L40–44）＋orphan 仅在 `is_commit_command` 为真时追加（L160）→非 commit 命令无 hits＝`return 0` 过闸——H-1(a)「Bash matcher 只路由 commit-audit，落锚非 commit 命令＝天然过闸」的申报经实物核验属实。hooks.json 实测＝Bash matcher 仅挂 commit-audit prehook/posthook；写侧 matcher＝`Write|Edit|MultiEdit|Write to file|Modify a file`；两 config 五席 `write_globs` 均无 `.workbuddy`（json 解析实测 hits＝[]）＝H-1 前提「不在任何席位 write_globs」属实。
  **黄⑤**：判据 10「落笔 exit 0 无拦截」在开发仓自身跑时，「无拦截」可能因环境未装载 hooks 而恒真＝假绿通道；票面宜注明该判据须在 hooks 装载态（或明示 hooks 未装载时读数效力降级）。
- **判据 11 判定式不完备**：`grep -c '开发面' dev-discipline.md` 后跟「§九 区间≥1」——区间未给机械表达式（需 `sed -n '/## 九/,/## 十/p' | …` 类接线方可跑）；`deliverables` 前后对照钉值写作「出现次数差＝0 **或如实登记**」＝带软出口的非单向判定。可跑性成立、可判定性打折＝修票级补正。
- **§A 24 行／§B 三换四 行数实测**（python 抽取＋票面内文双验）：§A fenced markdown 块＝**24 行**（首行为空行＝「含前置空行」口径属实）；§B 替换块＝**4 行**；§B 旧锚文块＝**3 行**；判据 8 钉值 `wc -l` 105→**130** 复算＝105＋24＋1＝130 ✓ 自洽可判；判据 8 第四读数 `grep -o '只是 {root} 的末尾段' dev-discipline.md | wc -l` 现盘＝**1**（改后钉 0 可判）✓。
- **计数口径内部不合**（黄⑥）：§开篇 L10 声明「计数口径＝occurrence」，而判据 8/11 命令形制用 `grep -c`（行计数非 occurrence）——两处对同一名词不同口径，成文后若某关键词多行内多次出现则两口径读数分叉。修票级＝判据命令改 `grep -o … | wc -l` 或声明判据区例外口径。

### 6. 裁定一致性＋平台兼容性（主面 6）→ 双根一致、条件化诚实、禁动在列；逐字声称带转写差〔黄⑦〕

- **双根口径逐字比对**（python 字符串包含实测）：登记件原句「专家团具备两个面的操作段，开发面= {dev_root}/{project_id}，交付面={del_root}/deliverables/{project_id}。…」在登记件＝True；rev2 §1.2b 同句（等号全角化＋加反引号排版）＝True；追加裁定 §三之补逐字「和项目根一样，用户指定，在开发期间不需要提前引导用户，只有收到用户的交付相关指令的时候才需要根据用户指定的目录构建，并提供用户相关引导。」两文均逐字在位＝True；语义三分句两文均逐字在位＝True。
  **黄⑦**：§1.2b 标题声称「登记件逐字」，实为**带排版转写的转述**（`=`→`＝`、插反引号）——语义零漂移、可指认回登记件，唯「逐字」二字失准（改「逐句转写·语义未动」即闭合）。
- **lazy 建档条款无歧义性**：§1.2b-4、§3.2 交付面条、§五.8、§A 草件第 5 款四处均含「用户指定＋开发期不预建不引导＋收交付指令时按用户指定目录构建＋引导＋独立 git 不入写保护/租约/账本」要素；§十一 H-7 撤销留痕（L331「曾设即销」）与登记件「H-7 候裁由此销账」一致。无歧义、无与登记件冲突。
- **§九.3 草件 §B 对位核**：§B 旧锚文三行与 dev-discipline **现盘 L99–101 逐行逐字全等**（python 切片比对 `==`＝True·无 DIFF）——替换对象可机械指认；§B 新四行含「双根模型／开发面＝`{dev_root}/{project_id}`／`{root}` 读作 `{dev_root}`／交付面另归独立 git／不入四区建档与写保护面」＝与裁定要点拆解①②语义一致。
- **锚定语义×hooks 平台行为条件化诚实性**：§二 L92「条件声明（写死·系 H-4）」明示「上溯起点仅 `os.getcwd()` 与 `dirname(包根)` 两处」「二者皆不成立时四链落包根＝已知边界行为（fail-safe·deny 不开窗）」＋判据 5b 钉该场景＋§五.9 P-⑥ 复测条随裁——不夸大表述；H-4（§十一 L328）附 hooks 相对命令形制读数（实物 hooks.json 命令＝`python "../skills/sop/scripts/…"` 实测相对形制在案·GWP 候裁⑧在册）。条件化诚实，D-1 处置到位。唯 §〇表 D-1 行落点栏「§七-11」指针错位——5b 的判读行实为 **§七-8**（L295），§七-11（L298）系判据 9 判读——黄⑧（指向漂移·修票级，票内其余落点栏抽查未见同类错指〔§六-5b/§六-10/§七-12 抽查均对位〕）。
- **禁动面在列**：§四 L224「`deploy-gate.md` 整件＋`SKILL.md` L23 索引行（Z-3）」在禁动清单；§七-11 L298「deploy-gate.md/SKILL.md L23 在列即红」负读在位；§3.2「L23 deploy-gate 索引行零动」＋§3.4 产出六件清单不含该两件——三面（禁动清单／负样本／产出闭集）互洽。

---

## 二、建议销账（v1 S1~S5＋对拍归并项对照 rev2）

| v1 项 | rev2 处置声称 | 本席核 | 销账 |
|---|---|---|---|
| S1（H-1(a) 补实·现盘无豁免实体） | §十一 H-1 重写：无机械实体＋真实通道＝host 非 hooks 写径 | 「豁免」occurrence 复算＝scripts＋config `grep -o 豁免` 计数＝**1**（hits 居 `seat-permissions-hooks-map.json` L7 注释行「非由 deny_globs 豁免」＝否定语义用法，非豁免机制实体）；lease-issuer L104–106 REJECT exit 2 实物在位；commit-audit 非 commit 命令过闸实物核实（见主面 5） | 销账（票面「grep『豁免』零命中」措辞按 occurrence 口径实测＝1 次否定用法命中——语义结论不受影响，措辞宜改「零机制实体」；计入黄⑥同族口径瑕疵不另立） |
| S2（裁定登记件补账） | §〇「已销账：主理人 177f5bc 誊录落账在盘」 | 登记件盘上实存（Read 命中全文）；§开篇引用指向该件 | 销账 |
| S3（H-4 呈裁补实） | §十一 H-4 补 hooks 相对命令形制读数 | 实物 hooks.json 相对形制实测吻合 | 销账 |
| S4（计数漂移） | §四 12 py＋1 sh | 盘面实测复核（主面 4） | 销账 |
| S5（docstring 序） | §3.1 代码块序同构 | 逐层比对（主面 4） | 销账 |
| R-1/R-2（双席重合） | §〇已修 | 独立复跑 | 销账 |
| Z-1~Z-4（裁定增补） | 已并入 | 主面 6 | 销账（Z-3 禁动在列、Z-4 H-7 撤销留痕在位） |

---

## 三、异议清单（红＝阻断／黄＝修票级不阻断）

- **红＝零**。三处 v1 红项（Y-1/Y-2/Y-3）核心缺陷均已消灭或降为尾差；rev2 未发现新阻断缺陷；无偷拍（已决正文零 config/hooks/版本改文，全部悬置 H 区候裁·抽查 §3.1.3／S6／§五.6／§开篇版本位与 v1 A18 结论一致维持）。
- **黄①**（§六 L254/L258）：`R0` bash 形 `/d/…` 与 runpy 源内路径不兼容（argv 通道经 msys 转换可达、源内字符串不可达·本席实测 False）——执行席按票面形填值即判据 3 系列/4c/5b 假红。修＝钉 Windows 盘符形。
- **黄②**（§3.1 L104／§十 L319）：「§3.1 代码块实测 56 行」实算失实＝**55 行**（python/awk 双验）；总预算实算 ≈372 非 ≈376（≤420 结论不变）。
- **黄③**（§十 L319）：「恰 10 环节」与列举不合＝箭头切分 9、逐笔拆分 11，两读均≠10；计数口径未写死。
- **黄④**（§六判据 11 L280）：「§九 区间」无机械表达式＋钉值「差＝0 或如实登记」软出口＝判定非单向。
- **黄⑤**（§六判据 10 L279）：「无拦截」读数在 hooks 未装载环境恒真＝假绿通道未设防（依据实物属实，唯判据效力条件未声明）。
- **黄⑥**（§开篇 L10 vs §六判据 8/11）：声明口径 occurrence 与判据命令 `grep -c`（行计数）不合；H-1「grep 豁免零命中」实测 occurrence＝1（否定用法注释行）同族措辞瑕疵。
- **黄⑦**（§1.2b L67 标题）：「登记件逐字」实为带排版转写的转述（语义零漂移·可指认回登记件）。
- **黄⑧**（§〇表 D-1 行）：落点栏「§七-11」应为「§七-8」（5b 判读行实测 L295）。

计数＝红 0／黄 8。

## 四、总判

**放行带修**（三态中第二态）：

- 放行面：v1 三异议核心缺陷全部消灭（Y-1 五型勘正逐位全等；Y-2 假红链条消除＋判据 4 骨架实物可达；Y-3 口径改造方向正确、上限 420 经独立复算 ≈372 自洽不触发伪红）；双席重合项①②独立复跑销账；裁定双根/lazy/H-7 撤销与登记件一致性逐字核验通过；§B 旧锚文与现盘 L99–101 逐字全等；行数判据（24/3→4/105→130）复算全中；H-4 条件化表述诚实不夸大；deploy-gate＋SKILL L23 禁动三面互洽；开工复测七组读数全命中、四段 sha256 全等。
- 带修面：八项黄＝修票级（两处「实算」尾差＋三处判据口径补正＋一处路径形制钉死＋一处转写措辞＋一处落点指针），全部不动放行方向、不动技术核心、不动候裁面；建议作者席 rev3 微笔或施工票开工复测时以回执更正销账（黄①②③涉执行期伪红/假绿通道，**须在施工开工前闭合**；黄④⑥⑦⑧为成文精度项）。

——QA 席（rev2 复审·fresh eyes）·开工 HEAD `1b77be7`·本审件全部判定基于票面原文＋仓内实物实测（版本级 `git show`＋盘上回读＋独立计数双验），未参考任何其他席位对 rev2 之评审件；除本审件外零改动、零施工执行。
