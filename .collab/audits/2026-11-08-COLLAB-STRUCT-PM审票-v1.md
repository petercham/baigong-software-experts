# COLLAB-STRUCT 票包·产品席独立审票 v1（A 席·fresh eyes）

- **审席**：产品席（pm-structc1·fresh 实例）｜**性质**：产品层独立审票，只调研评审零施工（审程未改任何既有文件，落盘仅本件）
- **开工实测读数**：`2026-11-08 20:35`／HEAD＝`cde6f90`（≥派工下限 `4e5b630` 在链实证 `git merge-base --is-ancestor` exit 0）／`git status --porcelain --untracked-files=no`＝空（tracked 面净）。他案 untracked 照登不碰（`.collab/ledger/`、research 散件、`.scratch/FX-*` 取证树群）；派工令所注 index 残留他案 staged（fuxi FX-U22 放行登记）经本席开工复点 `git diff --cached --name-only`＝空（该件已随 `cde6f90` 落链，index 现净），施工承诺不卷入。
- **被核两件（开工 blob 复算全等）**：
  - `.scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v1.md`＝191 行／24,590B／sha256 `f5f1222dfdb9…`（与派工令三值全等）
  - `.scratch/tickets/2026-11-08-COLLAB-STRUCT-B345-工序纪律并案维护票-v1.md`＝115 行／9,763B／sha256 `2cbc268b…`（全等）
- **审尺真源**：`.collab/decisions/2026-11-08-皮总裁定-collab结构规范重定义与缺陷清单并案.md` 全文直读（工作区 sha256 前 12＝`ea8061101341`／blob 5,056B＝主票 `:5` 所钉值复现）；另两真源：审计件 `c848a78`（`cea90e88afa9`/8,772B ✓）、复盘清单 `0259cd6`（`9dc187945f91`/6,272B ✓）——三真源 sha／字节与两票面所钉逐值吻合。
- **独立第三方读数（本席自跑）**：`run-gates.sh --no-write` 于 HEAD cde6f90＝**GATE PASS（发现 31,878）**（主票开工基线 31,875，差 3 条＝b8bdadc→cde6f90 新增链件〔重蒸批三件＋FX-U22 三件＋decisions 散件〕路径型 advisory 增量，方向一致，归因照登不糊账）；`check-adr.py --bundle-root agent-experts/baigong-software-team`＝`docs/adr 盘上件=1｜桶1=1 桶2=20 桶3=1｜exit 0`（与主票 §5.7 钉值全等）。

## 判例口径声明

计数一律 occurrence 口径（字面命中数，注明文件/行）；判定逐条附文件＋行号；红＝机械不可行或判据与条款互斥级／黄＝措辞·钉值·口径缺陷级（骨架可行可修）／绿＝实证闭合。三态如实，禁假绿。

---

# 第一部分 主票 COLLAB-STRUCT-1（结构名实对齐与规范成文票）

## G-1 四项裁定忠实映射——绿

裁定 `.collab/decisions/…皮总裁定…md` §二 四项＋§三 六目录标准态，逐项对位票面，未见夹带复议：

| 裁定 | 票面落点 | 对位实证 |
|---|---|---|
| ① drafts 顶层落件无子包＋单存活态 | 主票 `:13` 转录／A1.1·3·4·6（`:54-59`）四席 write_globs 旧子包（prd/design/adr/proposals/deploy）全改 `.collab/drafts/`／A3（`:70-74`）四卡写域行随动／B5（`:97`）归档条款 | 裁定「归档子包除外」→票定 `drafts/archive/` 给理由三条＋候裁③单列，未越裁；`drafts/archive/` 被 `.collab/drafts/` 前缀命中推论经 `lease-issuer.py:129-130` startswith 源码复核成立 |
| ② adr 单立不入 architect | `:14` 转录／A1.2·5 deny 改 `.collab/adr/**`／A1.3 architect write `.collab/adr/`／B2（`:94`）四件迁入包内 `.collab/adr/`、仓根不建空目录／禁动面 `docs/adr/` 一字不动（`:130`） | 迁入对象实体实证＝`git ls-tree b8bdadc …/.collab/drafts/adr/`＝恰 4 件（0001 草案／0001 final／会签-QA／会签-产品）与裁定 §二.2「四件迁入」名目吻合；仓根 `.collab/adr/` 现无实体 ✓（「本批不建」非虚述） |
| ③ 过期入归档子包 | A4（`:78`）规范真源新行「唯一例外子包＝`drafts/archive/`…每交接件只存一件存活态最新版」／B5 现 drafts 顶层零散件（实测 ✓）＝前向纪律 | 裁定把落位精确形态留给票面，票给方案＋替代案代价＋候裁③——程序正当 |
| ④ 十一项清单联动并案 | §8（`:159`）并案票 B345＝复盘清单项 9/10/11 | 并案票独立核见第三部分；两票写集零交叠见 G-6 |

六目录定位限定句（「需求最终确认前阶段的标准界定，非全生命周期闭集」）在 A4 `:80` 与 A5 `:84` 两处均带＝裁定 §三 原语义忠实；未列子包存续条款（§0.6／A5）对位裁定括注行。票面对裁定②「docs/adr 终写位不动」同时入 §6 禁动面——忠实。

## G-2 §1 现态基线钉值复现——绿

工作区／b8bdadc 快照双口径复点，抽验全部命中：seat-permissions.json 73/8,655B/`2e92c7b97af2` ✓；hooks-map 40/4,003B/`0d25b6057c93` ✓；collab-fixed-structure.md 27/1,719/`403db8e0e0f5` ✓；包内 README 12/635/`9e9397c74902` ✓；仓根 README 不存在 ✓；四席位卡 46/47/49/49 行＋sha `a1c6a4f8ecce`/`1c51935d3ca6`/`0bcda097f0f7`/`b4331d7422c4` 全等（`:22` 行内容逐卡核对：product 含 drafts/prd ✓、architect 含 drafts/{design,adr} ✓、qa 已写 `.collab/audits/`＝悬空指空实锤 ✓（audits 实体确无）、engineer 含 drafts/deploy ✓）；lead 卡 77/5,298/`c2287132f1e8`＋无 drafts/qa/audits 命中（grep 0）✓；`.gitignore:13` 注释含 `.collab/{decisions,qa,…}` 且排除面不含 qa 字面（check-ignore 预验包内 audits/x.md 两态不 ignore）✓。
计数钉值（b8bdadc）：仓根 `.collab/` tracked 84／qa 8／根面散件 20 md 全 tracked／tmp-w7-msg.txt untracked／实体子目录 13 ✓；包内 tracked 593／qa 230／drafts 4 全住 `drafts/adr/` 顶层 0／根面 3 件（2 登记呈拍＋README）／实体 13 含 drafts·product 无 architect·adr·audits ✓；fuxi qa 46／EAC qa 2 ✓；ledger untracked 恰三文件逐名点名 ✓；`.collab/qa/` 字面存量 205 文件／290 行、`drafts/adr` 26 行——occurrence 独立复跑全等 ✓；三同源 0.1.30×3 ✓；drill-05 `:17/:22/:27/:49`、drill-06 `:20`、s2 `:95/:96` 逐行读数吻合 ✓；`lease-issuer.py:127-130` 逐字／startswith 子集校验语义属实 ✓。

## R-1 §5.2 grep 判据与 A1.6 规格互斥（判据必翻红）——红

实测 `config/seat-permissions.json` 内 `drafts/deploy` 字面＝**2 处**：`:53` write_globs＋`:59` **deny_globs_note**（注记句「本席写域授权子域（`.collab/returns/engineer/`、`.collab/inbox/engineer/`、`.collab/drafts/deploy/`）…」）。票 A1.6（`:59` 行）只改 write_globs 元素＋点名「**write_globs_note** 内三子域对表句随之改」——**键名错位**：该字样实际在 deny_globs_note，write_globs_note（`:54`）内无此字面。后果＝按票面规格施工后，§5.2 钉值「`git grep -c "drafts/prd\|drafts/design\|drafts/adr\|drafts/proposals\|drafts/deploy" -- …config…agents…collab-fixed-structure.md ＝ 0」实得 **1**，判据 2 机械 FAIL。修法＝A1.6 改动面补点名 deny_globs_note 内该字面随动（一行级），或 §5.2 显式排除注记面并逐处登记。

## R-2 §5.3「qa 路径面＝0」与 §6 禁动面默认射程互斥——红

§5.3 钉 `git ls-files | grep -c "/\.collab/qa/\|\.collab/qa/" ＝ 0`（全盘路径面）；但 §6（`:132`）明载 fuxi `.collab/qa/`＋EAC `.collab/qa/`「是否同批改名＝候裁①射程，**本票默认不动**」。实测该 grep 现值＝286 命中横跨四目录（仓根 8＋包内 230＋fuxi 46＋EAC 2）；§3.B1 只 mv 仓根＋包内两处——**候裁①未裁「并入」时判据 3 必 FAIL**（余 48 件命中）。§7 候裁①（`:144`）「建议并入案乙同批 mv…或单列下一批——供裁」＝未拍，判据却把其中一肢当既成事实钉死。修法＝判据拆两态条件钉值（裁并入→0；裁下一批→48 照登＋归因），或候裁①先裁后重出 B1/判据。骨架不伤，判据级互斥＝红（本仓「判据凑不上」教训同族，如实不打折）。

## Y-1 A 组 adr 条款依据口径漏业界面——黄

皮总纠偏口径（派工令转录）＝补充问「adr 是否涉产品需求变更」的取证口径＝**人类工程实践通例**非本仓现状。裁定登记件 §二.2 取证三证齐：①ADR 工序链 `b0b449d`（三方会签含产品席）②ADR-0001 产品席保留项 R-PM-1 `b2150c5`③业界参照 Nygard《Documenting Architecture Decisions》2016（ADR Consequences 常直接驱动/否定产品需求）。票面 §0.2（`:14`）与 A3/A4 依据句只引①②仓内两证，业界口径未誊入成文面。结论未伤（单立条件成立）；本席独立复点①②均实证在册（b0b449d/b2150c5 存在、b2150c5 会签件含 R-PM-1 字面命中 ✓）。修法＝A4 依据注记段／A5 README 依据行补一行业界口径出处，一行级。

## Y-2 「十一桶」旧计数与注记内旧桶名不在 A1/A5 改动面——黄

桶闭集换代 11→16 后仍钉旧计数／旧桶名的四处：`config/seat-permissions.json:7`（table_notes「B1-D·十一桶」）、`:59`（deny_globs_note「十一桶闭集内 board/…/process/**qa**/receipts…」——句内枚举还用旧桶名 `qa`）、`seat-permissions-hooks-map.json:29`（同款十一桶字样）、包内 `.collab/README.md:5`（「B1-D 规范件·十一桶」）。A1/A5 逐件规格未点名、§5.2 grep 模式不覆盖——换代落链后成悬空旧计数。修法＝并入 A1/A5 一行级随动，或票面显式申报为存量噪声照登面。

## Y-3 16 桶新闭集漏 `returns/`——黄

A4（`:78`）新闭集逐字清点＝16 桶计数无误（decisions/audits/receipts/board/design/research/refs/evidence/inbox/process/dispatch/drafts/adr/architect/product/ledger）；但缺 `returns/`：包内 `.collab/returns/` 有 tracked 2 件、engineer write_globs 明授 `.collab/returns/engineer/`（`seat-permissions.json:53`）、裁定 §三 未列子包括注亦点名 returns——而规范真源 `collab-fixed-structure.md:12`「闭集外目录名不入规范」与之互斥（现 11 桶既有缺口在换代时未顺修）。修法＝闭集补 `returns/`，或票面明注 returns 归裁定「未列子包允许存续」白名单语义（与裁定 §三 括注缝合）。

## Y-4 判据 7 check-adr 复跑命令形制不足——黄

§5.7（`:126`）命令字面 `agent-skills/object-audit/scripts/check-adr.py` 裸跑实测＝infra error「根锚四序皆空…不降级不计绿」exit≠0；补 `--bundle-root agent-experts/baigong-software-team` 后读数与票钉全等（exit 0／盘上件=1／桶1=1 桶2=20 桶3=1）。零扰断言本体成立，复跑命令缺参＝回执执行按字面跑会误判非零。一行级补形参。

## G-5 候裁六项单列自洽核（不重审正当性，只核与正文互斥）——绿（①项判据联动例外已由 R-2 承载）

- 候裁②：散件 20＋tmp-w7 实体复点全实（20 tracked md／tmp-w7 untracked）；§6 不搬不删自洽；「附页 A〔起草时可补〕」＝候裁面留白，非正文缺件。
- 候裁③：正文 B5 给方案＋三理由＋替代案代价在册＝规格供裁形态自洽。
- 候裁④：三同源 0.1.30 实测复现；「零 bump＋升号归 PROJINIT 合并批」与 §6 禁动面（三同源零触碰）一致。
- 候裁⑤：b4a75d5 实证存在＝SEMGV-T3 v2 规格票落链件（票面本体候放行，链上无 T3 施工笔——`git log` 扫描未见）；「五卡 77/46/47/49/49」行数与 b4a75d5 及现态五卡全等（字节 5221/3181/3778/3902/3799 双点复现）；「STRUCT 开工读数须复点五卡现态」条款与 §0 开工读数体例自洽。两案条款互不污染（本票 §6 不预写 T3 挂载句 ✓）。
- 候裁⑥：票面住址 `.scratch/tickets/` 体例与两票实际落位一致 ✓。
- 唯候裁①与 §5.3 判据联动成 R-2 红——单列面自身（两案供裁＋本席建议）表述自洽，红在判据未随射程条件化。

## G-6 票间关系与写集自证——绿

主票 §4 声明闭集 13 文面件＋mv 242（8＋230＋4 计数算术对）＋add 3（ledger 点名三件实测恰此三件）；B345 闭集四件（software-orchestration SKILL.md＋三 references）不在主票闭集内——两票「零交叠」自证经对拍成立。§8「B345 写集＝references 三件＋SKILL.md 索引行」与 B345 §3 四件闭集一致（SKILL.md＝索引行载体）。mv 保真判据（R100 全 R 行／adr 四件 blob 双点对拍）机械可验。

## G-7 引用路径／commit 存在性实证——绿

票面全部引用实体逐一 Glob／ls／git 实证存在：`run-gates.sh`／`check-adr.py`／`write-guard.py`／`lease-issuer.py`／`freeze-unfreeze.py`／`dispatch-builder.py`／drill-05／drill-06／test_lease_instantiation.py／五席位卡／两 config／规范真源／包内 README／TEMPLATE-票面模板-v2.md（`agent-experts/baigong-software-team/.scratch/tickets/` 48 行／2,877B／`33d5f2f1bada` 与 B345 钉值全等，untracked 工作区件·作零触碰基线用成立）／复盘清单／审计件——无「引用不存在的脚本/文件」命中（本仓既有教训面专项扫过）。引用 commit 全部 `git cat-file -t` 存在：b8bdadc/c848a78/0259cd6/b0b449d/b2150c5/b4a75d5/b080b9d/6cf2767/50164c9 ✓。

## G-8 终态最佳实践对标（产品面·时效＞权威口径）——绿

- **adr/ 单立**：与业界通例一致——决策记录独立目录（`docs/adr/` 模式，Nygard 2016 出处＋MADR/ADR-Tools 活跃实践）＝权威面成立；「按角色子包塞 ADR」反为反模式。本仓交付面 docs/adr 已是该模式，过程面 `.collab/adr/` 单立与之同构＝终态健康。
- **drafts 顶层扁平＋archive 归档**：交接件基数小（docs 交接件 4 件，裁定理由），扁平化＝业界对低基数目录的一致建议（避免深目录过度分层）；「单存活态最新版」＝单一真源实践；git mv 进 archive 子包保留可读归档，与 git history 有冗余但系裁定明定的显式纪律，票面如实执行。
- **audits 更名**：产物目录按产物性质（审计面）而非席位名命名，语义更稳（席位名可变、产物名不变），对 fresh-eyes 与外部读者友好。
- **纵深减层申报**（`:62`）：drafts 共写域后席位互防降为租约粒度——票面如实登记为裁定①机械后果不藏不糊，符合「减层须申报」纪律；产品侧判定＝可接受（基数小＋租约点名文件＋QA 纯净核验兜底）。
- 时效面：所引业界参照（Nygard 2016）虽老但为 ADR 领域稳定共识，且 MADR 等近三年活跃项目沿同一结构＝无更新证据推翻；无与近三月/六月更优实践冲突面。

## 主票小结

忠实映射成立、基线钉值扎实、引用面全实存；**红两条均在判据面**（R-1 键名错位、R-2 判据未随候裁射程条件化）——不伤骨架，修后可放行；黄三条为成文完备性（依据口径／旧计数随动／闭集补 returns）＋一条命令形参。

---

# 第二部分 并案票 COLLAB-STRUCT-B345

## G-9 并案依据与问题转录忠实——绿

裁定 §二.4 并案令＋复盘清单（0259cd6）项 9/10/11 原文直读对位：票 §0 三行转录与清单 `:18/:19/:20` 逐列吻合（严重级/现状口径一致：9/10 候开票、11 轻档已行重档候裁）。三读数取证实证：b080b9d 回执链内 grep「24579」命中（FX-U17/U19 回执件在册）✓；6cf2767 commit message 内「31429」「19007」字面命中 ✓；`run-gates.sh:516` ＝`print("GATE PASS（发现 %d 条…"）` 汇总出口实证 ✓——B3「同盘不同口径」问题本体在册非虚。

## Y-5 §1 钉值行号错位（handoff `:45`）——黄

票 §1 表钉「§七 报告三律『引用的数带名字带口径』`:45`」——实测该句在 `handoff-discipline.md:40`（§七 header `:38`、三律条目 `:40-42`；`:45` 已是 §八 内容行）。§五 `:30`／dev-discipline §八 `:80-85` 两处行号锚经复点准确。错位不伤施工（A1 规格「append 于 §七 段尾，不动既有三行」语义仍可定位：§七 段尾＝`:42` 后），但钉值面＝计数/锚点类缺陷，v2 或施工回执勘一行即可。

## G-10 B345 基线钉值与规格可执行性——绿

四落点件行数/字节/sha 复现全等：SKILL.md 26/4,805/`2e1122c2f7ea`（`version: 1.1.6` 恰 1 命中）✓；handoff 78/6,263/`971a8a35ad3e` ✓；dev 131/12,071/`5336693548f9` ✓；dispatch 22/1,446/`831c2734baad` ✓；§四.1「纯增行」判据＋前后行数 78/131/22 对钉可验；§四.2 grep 钉值（窄口径≥1／清理清单行≥1／version 恰 1）机械可验；A1/A2 追加文本不触既有行＝append-only 兼容；A4 SKILL.md 索引两行（`:24` dev／`:25` handoff）实存可补短语；dispatch §二 header `:14` 实存（A3 候选条款落位可定位）。§5 禁动面（agents/** 五卡含 lead）与 A3「席位 MD 案候裁未拍前禁动」自洽——B5 重档落位两案单列候裁，正文默认技能域案＝与声明闭集四件（不含 agents）互斥面闭合。

## G-11 版本零 bump 口径两票一致——绿

B345 §A4「SKILL version 不动，归三同源合并批」与主票候裁④同口径；三同源 0.1.30 实测在位；SKILL.md `version: 1.1.6` 现态恰一处 grep 可自证。两票零 bump 承诺与 §6/§5 禁动面一致。

---

# 总裁决与计数

**红 2 ／ 黄 5 ／ 绿 11**

| 态 | 编号 | 一句话 |
|---|---|---|
| 红 | R-1 | 主票 §5.2 grep 判据与 A1.6 键名错位（`drafts/deploy` 实在 deny_globs_note），按规格施工判据必 FAIL——修一行条款或判据 |
| 红 | R-2 | 主票 §5.3「qa 路径面＝0」把候裁①未裁选项当既成事实，默认射程下判据必 FAIL——判据须按候裁①裁后终态条件化 |
| 黄 | Y-1 | adr 单立依据成文面只落仓内两证，漏皮总纠偏口径的业界面（Nygard 2016）——一行级补 |
| 黄 | Y-2 | 「十一桶」旧计数＋注记内旧桶名 `qa` 四处不在 A1/A5 随动面——补随动或显式照登 |
| 黄 | Y-3 | 16 桶新闭集漏 `returns/`（tracked 实体＋engineer 授权子域在其下）——补桶或注白名单语义 |
| 黄 | Y-4 | §5.7 check-adr 复跑命令缺 `--bundle-root` 形参，字面跑非零——一行级补 |
| 黄 | Y-5 | B345 §1 handoff 句行号锚 `:45` 实为 `:40`——勘一行 |
| 绿 | G-1…G-11 | 裁定四项忠实映射／基线钉值全复现（三真源哈希＋242/593/290/26 等计数 occurrence 复跑全等）／候裁面自洽／票间零交叠／引用路径与 commit 全实存／终态业界对标成立／B345 转录忠实＋规格可执行＋版本口径两票一致 |

**产品席放行建议**：两票骨架放行、判据面打回修——R-1/R-2 两条红均为行级/判据级修（v2 rev 或会师裁定并案修单即可闭），不需重出票；黄五项建议随 v2 一并收（Y-1/Y-4/Y-5 一行级；Y-2/Y-3 需条款点名）。候裁六项维持单列不重审。

## 三态明示

1. **做了但没落盘**：两票＋三真源全文直读；配置/席位卡/夹具/tests/脚本消费面只读实测（wc/sha/grep/ls-tree/check-ignore/lease-issuer 源码段）；run-gates `--no-write`＋check-adr 本席独立复跑（31,878／adr 读数全等）——均只读，仓内零临时脚本零中间文件。
2. **落盘了但没提交**：本件写入 `.collab/qa/` 后至 `git add` 前为工作区新文件态。
3. **提交了但没对账**：commit 后至完工回报给出「status 他案照登＋`git show --name-only` 恰本件＋HEAD」实测前此态存在，由完工回报补齐，不预标已完成。

**纪律自证**：只评审零施工（除本件外仓内一字节未动）；index 他案 staged 面未卷入（提交前 `git diff --cached --name-only` 自证只含本件）；未读 QA 席任何评审件（fresh eyes 隔离）；禁 --no-verify／禁 amend／pathspec 限定本件。

——产品席 pm-structc1·2026-11-08
