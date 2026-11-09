# STRUCT-FIX 产品席独立审票 v1（pm-structrev·A席·fresh eyes·只审不改）

- 帽·开工 HEAD 实测：`git rev-parse --short HEAD`＝`4a28614`（main）；被核对象＝`.scratch/tickets/2026-11-05-STRUCT-FIX-structure-declaration-alignment-ticket.md`（实体＝bundle 层 `agent-experts/baigong-software-team/.scratch/tickets/` 同名件，仓根无此件），对象笔实测＝`4a28614`（git log -1 -- 该路径）。
- 依据件＝清查报告 `.collab/research/2026-11-05-STRUCTURE存量清查-架构席-v1.md`（f199c30）；交叠核对＝ADR-L0 票 `agent-experts/baigong-software-team/.scratch/tickets/2026-11-05-ADR-L0-initiation-criteria-sop-and-first-adr-ignition-ticket.md`（含修订笔 v1 段全读）。
- 性质＝只读零施工；临时读数居仓根 `.scratch/pm-structrev/`（r1–r9 九件），批毕自删（关键读数已全部内联本件）；未读任何他席评审件。
- 前态钉值现势性核验：`git diff --name-only f199c30..4a28614 -- <闭集11件>`＝空返回——开票钉值未被在途笔移动，票面读数对当前 HEAD 仍有效。

## 结论

**红 0 ／ 黄 3 ／ 绿 10。**票面整体自洽、判据可机械、清查项无漏配，可放行开工；三条黄均为引用锚/口径措辞级，随正不阻塞施工。

## 黄项（措辞/锚点/口径需随正）

- **Y-1 HOLD 段引用锚错置（实质结论不受影响）**：票 HOLD 段称「ADR-L0 票面 S 节已自注『object-audit scripts/ 声明面已覆盖新脚本落位，零随动需求』」——该引句在 ADR-L0 票面全文 grep 不存在（`grep -n '零随动\|声明面已覆盖\|声明已覆盖' <ADR-L0票>` exit 1 零命中）；引句实源＝清查报告 §一.6 附注（报告 L69，措辞逐字吻合）。实质结论本席独立实证成立：object-audit `docs/STRUCTURE.md` 现盘已宣 `scripts/`（r3 全文实读四条含 scripts/＋tests/），check-adr.py 落 `scripts/` 已被声明覆盖，本票对该 STRUCTURE 仅惯例句零条目随动的裁定不依赖该错置引用。随正方向＝引用出处改标清查报告附注，或改述为「ADR-L0 票 S3b/S3c 落位面与其 scripts/ 声明面包覆关系经清查附注确认」。
- **Y-2 惯例句豁免名单未覆盖点号顶层面——C-3 豁免面留一条将来误报缝**：惯例句按件名列举五件（COPY.state／bundle.lock／plugin.json／settings.json／仓侧 README.md），但 bundle 顶层 git 面实测还有 `.codebuddy-plugin/`（内件＝`.codebuddy-plugin/plugin.json`，git ls-files 在位）＋`.collab/`＋`.scratch/` 三个点号目录零声明零豁免名（r6 `ls -a`＋git 面双验）。清查报告 `ls` 无 `-a` 同漏此面，票随报告继承。将来 C-3 按「顶层实存↔声明」对账时，点号目录若不在其扫描排除口径内即成常驻误报——恰是惯例句要消灭的东西。票内 A1 用了 `grep -v '^\.'` 排除但只居判据命令层，未成文为口径。随正方向＝§口径 1 补一句「点号名顶层面不入声明射程」（或 C-3 实装规格明载排除式）；改动零票面 S 节动，属口径段一行级。
- **Y-3 「随正 5 条」计数与枚举不闭合（继承自报告）**：票背景句「随正 5（COPY.state×3＋bundle 顶层四件）」括注枚举仅 4 件次；报告原文＝「随正 5 条（COPY.state×3＋bundle 顶层四件一句＋软性）」，表级随正行实测 4 行（`grep -c '随正 |'`＝4），第五项「软性」在报告内无定义实体。本票覆盖面无缺（见 G-8），纯计数口径不实——回执/对账按枚举 4 件走即可，票背景句宜随正为「随正 4（COPY.state×3＋bundle 顶层四件一句）」或注明第五项即报告的未定义软性项。

## 绿项（实证通过·带读数）

- **G-1 开工与对象笔**：HEAD＝`4a28614`＝对象笔（票起草笔即链顶）；`git status` 他席在途件未触碰。
- **G-2 前态钉值七份全中**（4a28614 现势，r1）：条目/yaml＝fuxi 3/3、EAC 2/2、object-build 2/2、multi-collab 2/2、object-audit 4/4、bundle-assembly-registration 2/2、bundle 7/6（docs/adr 条目不入 yaml＝既成形态，与 §口径 2 例外句吻合）；`git grep -c "非枚举面" -- "*STRUCTURE.md"` exit 1＝零命中。
- **G-3 A1 实态八行钉值与虚宣定性实证**：`git ls-files agent-skills/fuxi-skill/ | cut -d/ -f3 | sort -u | grep -v '^\.'`＝八行（README.md adapters contracts docs gates products rejected specs）与 A1 前态读数逐行吻合；`git log --all --follow -- agent-skills/fuxi-skill/SKILL.md` 空返回＝SKILL.md 全史零落笔坐实「虚宣非删除」；STRUCTURE 建立笔溯源＝`c7f87e7`（SWB-B1 骨架批·壳先行），票「B1 壳批模板先行态」定性成立。
- **G-4 两补声明实体与锚点实证**：`external-advisor-collab/sources/spec-anchors.md`、`object-build/scripts/publish.py` git 面在位（r2）；S2 插入锚句「`- \`references/\` — 技能参考件（规程、模板、裁决引文等）`」与 S3 锚句「（装配工序、规范件模板等）」现盘逐字命中（r3）——施工以 pattern 命中为准的 H6 口径可执行。
- **G-5 Q-3 边界清楚**：COPY.state git 面实测三包（multi-collab／object-audit／object-build）在位，EAC/fuxi 无——与报告及票 Q-3 申报一致；惯例句按件名列举不依赖计数，将来增减零随动的刻意设计成立。
- **G-6 HOLD 排程依赖自洽（审尺④）**：三同源现值 L3/L3/L5 均 `0.1.25`、README 版本账尾行＝v0.1.25（L67）实测如票钉；ADR-L0 S5 定 bump 0.1.25→0.1.26 逐字在位；本票「按彼时现值 +1」→0.1.27 相对值体例与之咬合，A6 链序读数（v0.1.26 行先于本票行）可机械核验。交叠两面（README 版本账尾行＋三同源）全入 HOLD；ADR-L0 HOLD＝无且不依赖本票＝单向依赖无环。两票对 bundle `docs/STRUCTURE.md` 面互不矛盾：ADR-L0 禁动面明载「docs/adr 条目 L11 已在位无需改」，本票仅落惯例句零条目动＋「ADR-L0 落地后自动咬合不判不补」——docs/adr 现盘不存在（`ls` 无此目录）与两票口径一致。
- **G-7 fuxi 重写七条目与实物用途相符（审尺⑤）**：七条目逐 `test -e` 全真；目录内容与声明释义逐条对得上实物——adapters＝person/method/classifier 三型 ✓、contracts＝artifact-contract/evidence-grading/failure-modes 三契约 ✓、gates＝assert-tool/harness/validator 族（另含 assertion-catalog/validator-catalog 目录件，「族」涵盖）✓、specs＝perspective-spec/technique-spec 双规范表 ✓、rejected＝README 留档约定 ✓、products＝README＋archive/pending 池 ✓；README「性质自注＝交付件本体·相近工具对照表置顶」实测于 README L3 逐字在位——定稿全文与包实际用途（perspective-pack-builder 双轨炼包）相符，无虚条目无漏实体（docs 除外＝声明句既载排除）。
- **G-8 清查项覆盖完备（审尺①）**：必修 4＝fuxi 双向（S1 整件重写一次闭）＋EAC sources/（S2）＋object-build scripts/（S3）＝4/4；随正表项 4＝COPY.state×3（multi-collab/object-audit 经 S4，object-build 经 S3 步骤3）＋bundle 顶层四件（S4 第四份）＝4/4；零漂移样板 bundle-assembly-registration 随批统一措辞（A8 护零破坏）；观察 3 不入票与派工令一致。惯例句落位合计＝S1/S2/S3/S4 四份＝7 份，与 A3＝7 咬合。无清查项漏配。
- **G-9 惯例句自包含可机械引用（审尺②）＋OA-T1 安全**：§口径 1 句与 S1 定稿句字符对等（全票仅 2 处出现＝口径定义＋S1 成品，出入仅 §口径 1 之外层反引号围栏，r9）——固定字串＋A3（文件数 7）＋A4（逐字 grep 7）双式钉值，将来 C-3 可据「非枚举面」字串定位豁免行并按括注件名豁免，措辞自包含（含件名闭集＋豁免效力声明「C-3 机检据此豁免」）。现盘七份 STRUCTURE 裸日期扫描 exit 1＝零命中，惯例句零日期，OA-T1 射程风险零（票「六份零日期」读数本席实测为七份零，出入无害）。产品判断：采「惯例句成文豁免」不逐件枚举＝正确方向，与报告最实质三条之 3 一致。
- **G-10 候裁三条边界清楚（审尺③）**：Q-1（fuxi SKILL.md 补建归 FUXI 本体批）——解冻拍板登记件在位可检（`.collab/decisions/2026-11-04-皮总拍板-FUXI解冻续推.md`），「删虚宣不补建＋若裁补建＝另批」路由干净；Q-2（惯例句升模板）——模板面实体 `object-build/references/50-directory.md` 在位且本票声明闭集不含＝未触面清楚，升否候裁不混淆存量批与模板批；Q-3——见 G-5。三条均「本票不径行＋候裁另批」体例，无边界渗透。

## 附·临时读数清理

`.scratch/pm-structrev/`（r1-prestate／r2-entity／r3-anchors／r4-fuxi／r5-anchors／r6-toplevel／r7-prov／r8-oat1／r9-consistency 九件）本批毕即 `rm -r` 删除，读数已全部内联上表；清理读数随回执链登记。
