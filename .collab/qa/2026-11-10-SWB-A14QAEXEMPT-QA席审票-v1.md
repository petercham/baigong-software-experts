# SWB-A14QAEXEMPT 合并规格票 v1 · QA 席独立审票判词 v1（fresh eyes·只读零改·证伪导向）

- 审票席：qa-a14rev（QA 席）
- 被核物：`.scratch/tickets/2026-11-10-SWB-A14QAEXEMPT-a14-exempt-config-and-qa-exempt-ticket-v1.md`（落链笔 `3cba063`，`git show --name-only 3cba063` 恰一件＝票面自身，实测）
- 开工实测：`date`＝`Tue Nov 10 23:32:42 2026`；开工 HEAD＝`3cba063143ed187206a9155f8dd4293a6342160a`（main）；审程中 HEAD 推进至 `4355423`（FX-U39 票面笔三＝他案链笔，照登不归因不触碰）
- fresh eyes 纪律：未读产品席并行审票产出；本件只落自家判词
- 依据件全文读实（逐一）：裁定登记件 `ca33b5f`、呈拍件 `27e59cc`、`share/check-pointers.py` 全文（495 行）、`share/check-source-of-truth.py` 先例段（L160-214）、`share/run-gates.sh` 涉面（FINDING_RE L196、SCRIPTS L141）、e12afd3 裁定原文锚清单句、TOOLHOME v4 草案（`ccf6383`）锚清单段、`share/baseline-sot-dup.json` 头部与结构、`agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md` 桶名闭集段

---

## 一、总判：红 1／黄 3／绿 14 · 不放行（红一窄 rev 后可放行）

红一项为规格内部两文句对损坏臂返回码自相矛盾＋所引先例行为与票面断言实证不符，施工席按票无法同时照做且 V3 必自矛——单点可修，不构成方案本体否决。豁免面治理取向、六枚集合、S2 落位、V4/V5/V6/V7 全部存活（见逐项落位）。

## 二、逐项落位（审票面六块）

### A1 · 碰撞面六枚集合复核＝绿

现跑 `python share/check-pointers.py`（工作区·exit 1）按 SEV 字段口径反查豁免键 token（旧桶路径串·本件拆写防自咬：桶段＝仓根 collab 桶下 defects 旧桶名＋drill 基名全名，先例＝回执 9ebc94f §四）的 BLOCK 行：恰 **6 枚**、恰 **5 文件**（其一两枚 :66/:174），行号 30/23/66/174/200/194 与票 §2.1 逐枚全等（Python 复核 sev-BLOCK drill＝6、files＝5 双验）。干净归档对拍（`git archive 7900b07`／`git archive HEAD` 两枚归档各现跑）：drill 命中 6/6 两态全等。豁免键（token 文本＋命中文件集合）＝单 token×5 文件集合，六枚全在集合内、可钉死；同构先例 `share/baseline-sot-dup.json` 实读确认（items＝text＋files、头注豁免键声明在册）。

O-2 复核＝绿（不在射程属实）：现链 defects 字样族 SEV-BLOCK 非 drill token 现跑 **16 枚**＝三枚异 token（归因复盘 6／回复盘 5〔基名链上不存在，ls-files 实测零命中〕／GWP-guard-assembly-defects 票引 5），token 文本与豁免键 drill 全不同→按 §4.1 判定语义「token 不在配置＝照 BLOCK」，确不入豁免射程。计数 12（票面）vs 现跑 16＝链上他案笔面差（见黄-2 勘）。

### A2 · V 判据可跑性复核

- V0＝绿：WATCH **4581**／NOTE-FXU28 **1988** 两值与票钉值逐字全等；BLOCK-anywhere 口径 22831→现跑 22833（+2，逐笔归因＝`f173c03` SCRATCHG 忽略规则笔之 R100 迁回执致两枚 SCRATCHG 独立审件旧回执路径指针悬空，两行现读点名，归因兜底条款合规）；GATE 全链现跑 `bash share/run-gates.sh --no-write`＝GATE PASS exit 0，发现 **150271**（vs 钉 150151，+120＝7900b07..HEAD 六笔他案链笔所致：回执 R100 迁移引用面＋FX-U39 票面引用面，改面自有发现＝0 解析坐实，兜底条款适用成立）。
- V1＝规格可跑（黄-3 计口径除外）：`grep -F '2026-11-08-drill' | grep -c ' BLOCK '` 现跑＝6，施工后→0 判据机械无歧义。
- V2＝绿：标记字样「历史豁免」grep 可判；甲式 BLOCK→WATCH 同位换行→WATCH+6 成立；「SEV 随裁改钉」留位合规。
- V3＝红（红-1，见 §三）。
- V4＝绿（表述面）：`git diff <base> HEAD --name-only 恰三件` 已封死任何历史件动字（动即超集 FAIL），blob 复点五文件＋qa 59/2 双验＋零 R 行四道闸互锁充分——「豁免入配置但史笔被动字」形态全封。
- V5＝绿：BLOCK 与 WATCH 同走 findings 列表（check-pointers L321-370 实读，两 SEV 同列表同 print），甲式六枚换 SEV 不换行数→GATE 总量不变推理机械成立；OA-D6 路由 advisory（run-gates 实读）不拦提交，前后 GATE PASS exit 0 判据自洽。
- V6＝绿（现跑复现）：`python -m py_compile share/check-pointers.py` 绿；`python share/check-pointer-closure.py --selftest` 入口存在（--help 实测），现跑 PASS exit 0（分账 4/1＋三态 2/4/4 全 MATCH）。
- V7＝绿：票面靶检现跑 `--target` exit 0 复现。

### A3 · 规格落位真实性＝绿

现盘逐位对照：`DEFAULT_SCOPE` L75＝三分类目录✓；`check_dangling` L299-L371✓；七候选层 L241-L254✓；FX-U28 后缀归位层 L348-L361（归位放行 continue 在 L361）✓；含斜杠悬空 BLOCK append L363-L365✓；裸基名 WATCH L366-L370✓。S2 插入点＝L361 continue 之后、L363 append 之前＝**唯一点**无歧义；裸基名走 else 分支（L366）天然不接豁免，与「裸基名层不接豁免」条款自洽；`--target`/`--scope`/缺省三入口共用 `check_dangling`（L463/L475），豁免层置入即三入口同口径，写实。SOT 先例面：外置 JSON＋HERE 式 L177-178✓、`load_baseline` L199-214✓、SOT 豁免转 WATCH 形态（输出行实读「基线豁免…WATCH」）与候①甲同构属实。现无豁免/基线读取面（check-pointers 全文实读，零 json import）＝「现无豁免面、本票补此面」写实。

### A4 · 史笔零改字防线＝绿

V4 四闸（见 A2）＋§4.5 禁动面闭集＋租约 deny（`agent-experts/**` 全域 deny＝五命中文件在 deny 内，机械前置防）三层叠合，足以封死「豁免入配置但历史件被动字」。迁册五件套/裁定/呈拍/工单未逐件入 V4 命令，由 name-only 恰三件全集蕴含间接封死——间接但充分（动任一即 name-only 超集）。

### A5 · O-1／O-3 观察复核

- O-1＝坐实：fuxi qa 现跑 59（off 口径＋NUL 双验＝59/59）、EAC qa 2（2/2）；58→59 归因复核＝桶内最新三枚为 FX-U36/U37/U38 QA 独立验证件，FX-U38 落桶所致属实。
- O-3＝表述可执行＋机理复核绿：两夹具现含旧 qa 桶字样（拆写＝仓根 collab 桶下 qa 桶名·substr.md L3／violations.md L3 实读）；现链两态（工作区＋两归档）check-pointers 夹具面发现＝**0**；夹具 token 走含斜杠分支在七候选层先行解析命中（`--target` 夹具 exit 0 实测＋模块级复算 resolve 命中）→根本到不了豁免层，「不翻面」有机理保证非仅口号；V6 兜底命令两式（--selftest 入口存在已实测）可跑。

### A6 · 钉值口径＝绿（附黄-3 计数口径）

链上 SHA 13 枚 `git cat-file -e` 全在位（fb76547/c79dde9/9ebc94f/883aa68/111b67a/36dfb78/6307d48/27e59cc/ca33b5f/e12afd3/f135855/7900b07/9aa98ba＝13/13 OK）；票面开工读数（HEAD 7900b07＝SCRATCHG v2 落链笔✓、tickets 桶 137→现 138＝A14 票面自身落链所致✓）；旧数 17398/17404/18251「案证引用不作基准」口径与呈拍件 §三 注记同文属实。计数口径缺陷见黄-3。

## 三、红项

- **红-1（V3 损坏臂返回码自相矛盾＋先例引用失实）**：§4.1/§4.2 写「JSON 损坏/形态不符＝exit 4（两式先例文照搬）」，V3 探针钉「JSON 截断→exit 4」；但所引先例 `check-source-of-truth.py` `load_baseline`（L199-214）实发行为＝`raise SystemExit('infra error: …')` 带字符串参→**exit 1**，本席实证：截断 baseline 副本至损坏→`CORRUPT_ARM_EXIT=1`（stderr 正是先例文案）。check-pointers 尾部 wrapper `except SystemExit: raise` 同构→照搬先例文落 check-pointers 同样 exit 1。两文句（「先例文照搬」vs「exit 4」）互斥：照搬则 V3 损坏臂必 FAIL，写 exit 4 则违「照搬」。修单（窄 rev 一处）＝损坏臂**返回码写死 `raise SystemExit(4)`**（对齐退出码闭集「基础设施错＝4」），先例只引「缺失＝无豁免／损坏＝infra 错不猜语义」形态不引其返回码语句；或引用句改为「先例形态＋闭集码校正」。红一之外 fail-closed 两臂语义本体（缺失＝无豁免更严不更松）完备无歧义。

## 四、黄项

- **黄-1（§六 锚归属誊写走样）**：票 §六「check-pointers 自锚系其 13 处中第 13 处已裁不开 v5」——e12afd3 原文在册口径＝第 13 处＝「tools 自身件 **check-source-of-truth** 内嵌自锚」（TOOLHOME v4 随动清单点名 check-pointers 系 L121 与 :442 **两处**谓词，非第 13 处）。实质面不伤（S2 不触 find_root 谓词属实，实读 L114-128/L438-451 零涉），但引用件口径须勘正后引用链才干净。
- **黄-2（O-2 计数差未注归因）**：票 O-2「旧字样族另有 12 枚 BLOCK」vs 本席现跑 **16 枚**（归因复盘 6＋回复盘 5＋GWP 引 5）。非豁免射程判定不受影响（三 token 全异于豁免键，射程复核仍绿），但其中归因复盘 token 存在**环境依赖读数**：裸盘＝BLOCK 6 枚（fuxi 包 `.scratch/FX-U14/FX-U15` 未跟踪树副本多义→后缀命中≥2 fail-closed），干净归档＝NOTE-FXU28 归位 1 枚——同 token 两态异 SEV。建议施工轮 V0 复点时对该字样族现算＋归因随登（票内 12 枚数作开工读数留史不改，追加现值随登即可）。
- **黄-3（V1「BLOCK 计数」口径混计风险）**：票 §一「BLOCK 22831」系 **grep-anywhere 口径**，实测该口径含 WATCH 行（WATCH 文案含「不 BLOCK」字样致混计：现跑 BLOCK-anywhere 22833≈SEV-BLOCK 18253＋WATCH 4581）。V1「BLOCK＝V0−6」若沿用 anywhere 口径，则六枚转 WATCH 后新行文案若含「BLOCK」字样则计数不降→判据 FAIL 依赖未写死的标记文案。修＝V0/V1/V2 计数一律写死 SEV 字段式（`grep -Ec '^[^:]+:[0-9]+: BLOCK '` 类），或写死豁免 WATCH 行文案不含 BLOCK 字样。另 V3「配置缺失臂（临时移开配置件）」在共用工作区多席在飞窗＝移 share 在盘件有他案门禁窗内读空风险，票已给「不可行时以损坏臂替」——建议升格为「缺失臂在共用窗径禁用损坏臂替，复原步骤删」一并收进 rev。

## 五、观察登记（零动作）

- O-4：仓根 `.collab/qa/` 空目录（0 文件·untracked）本审程窗内 00:22 在盘再现；`git ls-files '.collab/qa/*'`＝0。按票 §4.3 口径「再现已登＝违闭集存量，不属豁免面」照登候裁，本席零碰（本判词落位＝主理人派工指定仓根 qa 桶，与桶名闭集真源 17 桶无 qa 桶之张力一并呈裁）。
- O-5：他案在飞面照登零碰——开工 status 之 FX-U39 票面 staged M、COLLAB-STRUCT 回执 staged R、票面桶 A→R 迁移态全程未触；两归档＋工作区扫描对六改面自有发现＝0（解析坐实）。
- O-6：fuxi 包 `.scratch/FX-U14/FX-U15` 未跟踪树快照（5 副本）为裸盘扫描噪声主源（单文件 41 BLOCK×5 面）——与黄-2 环境依赖读数同根，归 TOOLHOME/SCRATCHG 线既有射程，本票零动作。

## 六、实跑读数表（本席现跑·全部可复点）

| 项 | 读数 | 对票值 | 判定 |
|---|---|---|---|
| 开工 HEAD | 3cba063（→4355423 他案推进照登） | ≥7900b07 | ✓ |
| 缺省扫描 BLOCK（anywhere 口径） | 22833 | 票钉 22831 | +2 归因合规（f173c03 R100 迁回执→SCRATCHG 两枚独立审件旧回执路径悬空 BLOCK 新增，两行现读点名） |
| 缺省扫描 BLOCK（SEV 字段口径） | 18253 | — | 口径澄清基准（黄-3） |
| 缺省扫描 WATCH | 4581 | 票钉 4581 | ✓ 全等 |
| NOTE-FXU28 | 1988 | 票钉 1988 | ✓ 全等 |
| drill token BLOCK（anywhere／SEV 两式） | 6／6 | 票面 6 枚 | ✓ 双验全等 |
| drill 命中文件集合 | 5 文件·:66/:174 同文件两枚 | 票 §2.1 逐枚 | ✓ 全等 |
| defects 字样族非 drill BLOCK | 16（三异 token 6/5/5） | 票 O-2 12 | 黄-2 归因随登 |
| 归档 7900b07 全扫 | BLOCK-anywhere 2026·drill 6 | 起草轮同链位 | 裸盘 vs 归档口径不可对账（呈拍 §三 注记同文），drill 6/6 两态全等 |
| 归档 HEAD 全扫 | BLOCK-SEV 2028·drill 6·NOTE 1152 | — | 干净面复点备查 |
| GATE 全链 `--no-write` | PASS exit 0·发现 150271 | 票钉 150151 | +120 他案六笔链笔致（改面自有发现 0 解析坐实）·兜底条款适用 |
| fuxi qa / EAC qa tracked | 59／2（off＋NUL 双验 59/2） | 票 §一 59/2 | ✓ 全等（O-1 坐实） |
| fuxi audits tracked | 4 | 票 §一 4 | ✓ |
| tickets 桶 tracked | 138（仓根桶 40） | 票 §一 137 | +1＝A14 票面自身落链 ✓ |
| py_compile check-pointers | 绿 | V6 | ✓ 复现 |
| check-pointer-closure --selftest | PASS exit 0（分账 4/1·三态 2/4/4 MATCH） | V6 | ✓ 入口存在＋前后值在册 |
| 损坏臂探针（SOT 先例实测） | exit **1**（先例文案照发） | 票 V3 钉 exit 4 | **红-1 实证** |
| 票面靶检 `--target` | exit 0 | V7/附 | ✓ 复现 |
| 链上 SHA 存在性 | 13/13 OK | 票 §六 14 枚宣称 | 本席点验 13 枚全在位 |
| 7900b07..HEAD diff | 7 文件·五命中文件零涉·qa 桶零 R | §4.5/V4 | ✓ 史笔未动旁证 |

（occurrence 双验＝票面引用 6 枚 BLOCK 集合以 grep 管道式＋Python SEV 字段式两式独立复算，两式 6/6 全等、5 文件集合全等；qa 计数以 off 口径＋`ls-files -z` NUL 计数两式，两式 59/2 全等。）

## 七、候①②表态

- **候①（豁免命中 SEV 形态）＝取甲**（转 WATCH 带「历史豁免」标记留痕）。理由：①与 `baseline-sot-dup.json`＋SOT 豁免转 WATCH 先例同构（输出行实读「基线豁免…WATCH」在册），豁免面可见可审，符合「豁免入配置」裁定的治理取向（裁语「BLOCK 碰撞归零」＝计数归零非行消失）；②V2 可机械核对 6 枚留痕，乙式（滤除不输出）使 V2 无从判起、豁免面不可审计；③本席现跑确认 BLOCK→WATCH 同走 findings 列表，甲式 V5 总量不变推理机械成立。**附条**：甲式 WATCH 行文案须避开「BLOCK」字样（黄-3 联动），否则 V1 anywhere 口径不降——rev 一并写死。
- **候②（qa/ 豁免行消费面）＝取甲**（豁免行仅成文于 S1 第二段，consumption 留待闭集机检项将来挂面）。理由：本仓 share 现无桶名闭集机检实体（本席 grep 全部 share/*.py 零命中「桶名闭集/collab-fixed-structure」坐实），乙式随票增设机检＝射程超出裁定 ca33b5f §二-3 文字（裁定只裁「豁免清单入机检配置」认账 BLOCK 碰撞面），且移交工单 v3 备注 3「本仓侧修路＝挂候补池另行处置」在册——乙式须另行呈请排程，不混本票。

## 八、结论

**不放行（红一窄修后可放行）**。红-1＝V3/§4.1 损坏臂返回码自相矛盾＋先例引用行为失实（实证 exit 1 vs 票钉 exit 4），修单一处：损坏臂返回码写死 `SystemExit(4)` 对齐退出码闭集、先例引用句只引形态不引码。建议随 rev 一并处置黄-1（锚归属勘正：第 13 处＝check-source-of-truth 自锚）＋黄-2（O-2 现值 16 随登＋环境依赖注）＋黄-3（计数口径写死 SEV 字段式＋缺失臂共用窗禁移改损坏臂独跑）。方案本体（豁免键设计／S2 唯一插入点／fail-closed 两臂／V4 四闸／一次施工收敛两线）全部存活；候①②均取甲与本席 A1-A6 复核结论一致。

## 九、自证

- 只读零改自证：本席全程零 git mv／零 add／零 commit（落链前）；未建 baseline-pointer-exempt.json、未改 check-pointers.py、未碰 .gitignore／租约／两包 qa／夹具。
- 临时工作物＝仓根 `.scratch/qa-a14rev/`（扫描输出四件＋两枚干净归档＋损坏臂探针目录＋两枚分账件），完工笔前自删附读数：`rm -rf .scratch/qa-a14rev` 后 `ls .scratch/ | grep -c qa-a14rev` → 0。
- 判词落位＝仓根 qa 桶（主理人派工指定），与 O-4 同栏呈裁；本件 message 零 at 符号字符；pathspec 两端齐带；禁 add -A／禁 amend。
- 落笔前靶检：`python share/check-pointers.py --target .collab/qa/2026-11-10-SWB-A14QAEXEMPT-QA席审票-v1.md` → exit 0（读数见回票）。
