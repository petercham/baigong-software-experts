# COLLAB-STRUCT-1 施工分票 v1 · 产品席独立审票件（fresh eyes·证伪导向·只读零改）v1

- **票号／席位**：COLLAB-STRUCT-1｜产品席（pm-struct-tkv）｜本件＝**审票产出**，非施工依据、非产品本体变更
- **被核物**：`D:\multi-agent-collab-devkits\agent-experts\baigong-software-team\.scratch\tickets\2026-11-09-COLLAB-STRUCT-1-施工分票-v1.md`（落链 `2a4e262`）
- **依据件（完整直读·只读零改）**：
  1. `D:\multi-agent-collab-devkits\.scratch\tickets\2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v2.md`（主票 v2·链笔 `5eeeb3a`）
  2. `D:\multi-agent-collab-devkits\.collab\decisions\2026-11-09-皮总裁定-STRUCT-v2放行与六项候裁取态.md`（链笔 `6c495d4`）
- **落点纪律**：本件落 `audits/` **新桶**（B7 向前进纪律），**禁落旧 `qa/` 桶**；只落过程域，不写任何交付面（`docs/`／`config/`／`agents/`／`skills/`／代码域零触碰）。

---

## §0 开工读数与纪律申报（落笔前实跑·一律以实测为准）

- `date` ＝ `Mon Nov  9 03:16:03     2026`（本机时钟）
- `git rev-parse HEAD` ＝ `a68d6ecd938cd77648767d450edd95fe3319fe1a`（短 `a68d6ec`）；`rev-parse --abbrev-ref HEAD` ＝ `main`
- `git status --short --untracked-files=no`（tracked 面）＝ **空（净）**
- **预期钉对钉**：派工预期 HEAD `2a4e262` ≠ 实测 HEAD `a68d6ec`。实测 `2a4e262` 为 HEAD **ancestor（YES）**，其 parent ＝ `4adca3dea42fd120914359971c070562d202f340`；区间 `git rev-list --count 2a4e262..HEAD` ＝ **1**，`git log --oneline 2a4e262..HEAD` ＝ `a68d6ec collab: COLLAB-STRUCT-1 施工分票 v1 QA席独立审票件（fresh eyes·证伪导向·红3黄4·建议打回）`。
- **链漂不影响本审票基线（实测）**：该唯一一笔 `a68d6ec` 只落 `agent-experts/baigong-software-team/.collab/audits/` 一件；`git log --name-only 2a4e262..HEAD` 过滤三件被核物／依据件＝**空**，过滤 `\.collab/qa/|plugin.json|bundle.lock|software-team-*.md`＝**空**。即无 SEMGV-T3 施工笔、无 STRUCT 施工笔、三件零改。现盘基线有效，本件所有读数在 `a68d6ec` 时点成立。
- **fresh eyes 申报（诚实登记）**：`git log --oneline` 系链漂核查的机械输出，带出上述 commit subject 含「红3黄4·建议打回」字样。本席**未打开该审票件正文、未读取其内容、未与其作者通信**；本件的分级、判词、逐条读数全部由本席独立自跑形成，条数巧合不作比对、不引用。本席独立结论为「**红 3／黄 2·打回**」，与标题字样条数不同。
- **只读零改声明**：全程 `wc`／`sha256sum`／`git ls-files`／`git grep`／`git log`／`git show`／`git mv -n`（dry-run）／`python -m json.tool`／只读 python 集合运算；`git mv` **一律带 `-n`**，dry-run 后复测 tracked 面仍净、qa 计数仍 294，未落地任何改动。三件被核物／依据件零改。
- **他案在制品照登不碰**：完整 `git status --short` 列出大量 untracked 在制品（`.collab/ledger/`、`.collab/research/` 6 件、`.scratch/FX-U*` 系列、`.scratch/PM-U*`、`SEMGV-T2/`、`SRC4Z-draft/`、bundle `.collab/ledger/`、`agent-skills/fuxi-skill/.scratch/FX-U*`、若干 `assert-*.txt`／`st-*.py.txt`／`.scratch_wbdocs.html` 等），全属他案在制品，本席逐类照登、零触碰。

### 哈希链登记（依据件 sha256 全值·本席实测）

| 件 | 行数 | 字节 | sha256 |
|---|---|---|---|
| 施工分票 v1（被核物） | 247 | 39,002 | `d8ec7b94e46eda470b14d75d69ba64ed668678d87996b49b91db9ce660c47776`（前 12 `d8ec7b94e46e`＝派工钉，全等） |
| 主票 v2 | 251 | 46,944 | `984bffb7fcb08bb42fc67050b078e3fc709a81cd6cd6339d6da2ae406f37cc25` |
| 皮总裁定 | 92 | 9,397 | `7ded3258a84c4f3a455fae7ad3b8a75133d82a4cfa29bfa62951d9b0b2bbd6e8`（前 12 `7ded3258a84c`＝派工钉，全等） |

- **单件 name-only 核验（实测）**：`git diff-tree --no-commit-id --name-only -r 2a4e262` ＝ **1 件**；`git show --name-status` ＝ `A agent-experts/baigong-software-team/.scratch/tickets/2026-11-09-COLLAB-STRUCT-1-施工分票-v1.md`；subject ＝ `collab: COLLAB-STRUCT-1 施工分票 v1 落盘（纯规格零施工·单件双侧 pathspec）`。
- **链笔 ancestor**：`5eeeb3a`／`6c495d4`／`2a4e262` 三者 `cat-file -t` ＝ `commit`，`merge-base --is-ancestor … HEAD` ＝ YES／YES／YES。
- 本件自身 sha256 与 commit sha 属自指值，正文不预写，由完工回报实测给出（体例同被核物 §7 L225）。

---

## §1 判词

> ## **打回（不放行）· 红 3 ／ 黄 2 ／ 其余核通过**
>
> 施工分票 v1 作为「工程师席唯一施工依据」**不合格**，建议勘办后重出 v1.1（或 v2）。理由：三项红项均直接作用于机械施工与回执判据 —— **R1** 令判据 3 误判 FAIL 或诱使误动禁动面；**R2** 令判据 9 施工后实测 4≠3 误判 FAIL；**R3** 令 B1 包内 234 件整目录 `git mv` 落入 `audits/qa/` 嵌套子目录、名实对齐目标整体落空。三项皆非标注级，属「机械照跑即出错」。
>
> 绿项（六项取态主体、九判据形制钉、洁净删改合法性、§4/§6/租约/三态/零施工自证）逐条实测核通过，见 §2；这些不构成「给假绿」——本判词以三项红项为准。

| 级 | 编号 | 一句话 | 落位 |
|---|---|---|---|
| 红 | **R1** | 判据 3 硬钉「施工后终值＝48」与现盘两包 50 冲突，且同句「现值不锁死」自相矛盾 | 分票 L12／L95／L191／L205；裁定 §三① L25（依据件·只呈报不改） |
| 红 | **R2** | 判据 9 落位现值漏算施工分票自身（现 1 非 0），施工后应为 4 非 3 | 分票 L12／L198 |
| 红 | **R3** | B1 包内整目录 `git mv qa audits` 在 `audits/` 桶已存在（B7 必然）时落入 `audits/qa/` 子目录 | 分票 §3 B1 L95；连带 §5 判据 3／4 |
| 黄 | **Y1** | 判据 8 `docs/adr` 现值钉 3（`:22`/`:23`×2）与实测 2（`:22`+`:24`）不符；A3 行号标法与现盘颠倒 | 分票 L53–55／L196（有「内容锚定位」兜底，不阻断） |
| 黄 | **Y2** | 洁净机检「案乙」候裁态标签残留于交接件，与裁定 §四 L47「不再保留两态供裁措辞」有张力 | 分票 L12 |

---

## §2 审票范围·逐条实测读数

### §2.1 六项取态落位（对照裁定 §三／§四）

**① 案乙不追改＋两包不并入＋README 去歧义句逐字 —— 主体绿、数值口径红（R1）**
- 去歧义句逐字三方对拍（实测）：裁定 L27 与分票 L75 均含核心串 `历史案卷内 .collab/qa/ 字样＝改名前旧路径，读作 .collab/audits/` → **True（逐字全等）**；分票 §2 A5 L74 规定两份 README 各加一行，落位齐备。
- 四件套处置：分票 §1.5 L22（①件位 B 组 mv 全量归位／②旧路径字面 append-only 不追改／③去歧义两份 README／④增量面 B7 封口）与裁定 §三① L26 逐项一致。
- 「两包不并入、维持默认射程不动」：分票 §3 B1 L95、§6 L205、§5.3 L191 均有落位 → 忠实。
- **但数值口径见 R1（§2.3）**：L95／L205 沿用「fuxi 46＋EAC 2」，L191 硬钉终值 48，与现盘 48＋2＝50 不符。

**② 20 件散件归位 `decisions/`＋删 tmp 留痕三值 —— 全绿**
- 三方对名（python 集合运算·实测）：盘上根面散件 **20** ＝ 分票 §4 旧路径 **20** ＝ 裁定 §五 **20**；`盘上==§4旧` **True** 差集 `[]`；`§4旧==裁定§五` **True** 差集 `[]`。
- tmp 留痕三值（实测）：`.collab/tmp-w7-msg.txt` ＝ **23 行／2,270B／sha256 `037a83b30b08741c9bf476496284ce7357b5f164388f4f1a697e5627a9a50056`**，与分票 §3 B9 L105／§7 L219、裁定 §三② L32 逐字全等；`.gitignore:36` ＝ `/.collab/tmp-*.txt`（实测命中）。
- 落位：分票 §3 B9 L103–106（R100 保真、删除前先复算三值、不符即停手呈报）、§4 20 旧/20 新路径、§6 L214 改判、§7 L219 回执必附 —— 齐备。
- `decisions/` 直系 tracked ＝ **56**（实测），与分票 L191「现值 56＋20＝76」口径自洽；裁定 §三② L31 记「现有 55 件」为裁定落笔时点值，+1 漂移照登，零同名冲突（`comm` 等价核验：盘上根面 20 与 decisions 56 无同名）。

**③ `drafts/archive/` 包内、不复用仓根 `.collab/archive/` —— 绿**
- 分票 §3 B5 L99 三条理由（同域同主／天然命中 `write_globs` 前缀／与仓根 `.collab/archive/` 语义分域）与裁定 §三③ L35 一致；明文「**不复用仓根 `.collab/archive/`**」。

**④ 零 bump —— 绿**
- 三同源（实测）：`plugin.json`／`.codebuddy-plugin/plugin.json` ＝ `0.1.30`／`0.1.30`，`bundle.lock` 含 `0.1.30` ×1；分票 §1.4 L21、§6 L209、租约 note L246 均声明零 bump，现盘未动。

**⑤ 先 SEMGV-T3 后 COLLAB-STRUCT-1＋开工复点五卡 —— 绿**
- 五卡现态（实测·行数/字节/sha256 前 12）：`product 46/3227/a1c6a4f8ecce`、`architect 47/3825/1c51935d3ca6`、`qa 49/3848/0bcda097f0f7`、`engineer 49/3951/b4331d7422c4`、`lead 77/5298/c2287132f1e8` —— 与分票 L11 钉值**全等**。
- 五卡 `T3` 挂载句 `grep -c` ＝ **0／0／0／0／0**（实测）；链上 `2a4e262..HEAD` 无 T3 施工笔；分票 §1.2 L19、§1.3 L20（含「若链上已现 T3 施工笔即以其为基线、五卡 sha 钉作废重取」）、§6 L210 齐备。

**⑥ `.scratch/tickets/` 住址成文行逐字 —— 绿**
- 住址成文行三方对拍（实测）：核心串 `票面与临时工作物的唯一落点＝所属项目仓根（项目根＝含 docs/STRUCTURE.md 之探针锚目录）下的 .scratch/<票号>/；本仓百工项目锚＝…；现行体例目录名 .scratch/tickets/ 入表，规格名 tickets/ 不再使用。` 在**裁定 L43／分票 A4 L66／分票 A5 L78 三处逐字命中 True**；L68 另「规范表据此承认现行 `.scratch/tickets/` 体例，规格名 `tickets/` 作废」；分票 L5 本件落点自述亦按此体例。六项取态忠实、无改写。

### §2.2 九条机械判据 ↔ 主票 v2 §5（逐条对照）

**形制钉保留核验（三项全绿）**：
- 判据 1「run-gates 计数一律**同形态两读数对拍**（主盘对主盘、worktree 对 worktree）、**禁跨形态比数**」→ 分票 L189 逐字保留（对照主票 v2 §5.1 L169）✓
- 判据 6「drill 两件基线与复跑一律用 **`T06_TMP` 注入形制**；裸跑 exit 1 同值不同因」→ 分票 L194 逐字保留（对照 §5.6 L174）✓
- 判据 7「`check-adr.py --bundle-root agent-experts/baigong-software-team`，钉 exit 0／`docs/adr 盘上件=1｜桶1=1 桶2=20 桶3=1`；裸跑 exit 4 非用态」→ 分票 L195 逐字保留（对照 §5.7 L175）✓。**本席实跑**：`check-adr: bundle 根＝…｜docs/adr 盘上件=1｜桶1=1 桶2=20 桶3=1｜发现 0｜exit 0` —— 与钉值**全等**（另脚本自报 `E-ADR-4″ 本次未执行…未执行判据不得计绿`，如实照登，非本判据面）。

| # | 主票 v2 §5 | 分票 | 现值实测（本席自跑） | 判 |
|---|---|---|---|---|
| 1 | L169 JSON 合法＋同源全等＋同形态对拍 | L189 | 两 config `python -m json.tool` exit **0／0**；递归取 `deny_globs` 路径 A=6／B=5，共同 5 路径逐席全等 **True**、不等路径 `[]` | 绿 |
| 2 | L170 grep→0（drafts 子包现值 13 行；十一桶 5occ/4 行；`collab/qa` in config→0） | L190 | drafts 子包 `git grep -n … \| wc -l` ＝ **13**；十一桶 **occurrence 5／lines 4**；`git grep -c "collab/qa" -- config` ＝ **1+1**（现值非零，终值 0 待施工） | 绿 |
| 3 | L171 两态钉（态甲 48／态乙 0） | L191 取态甲 | `git ls-files \| grep -c` ＝ **294**；分桶：仓根 qa **10**、bundle qa **234**、fuxi **48**、EAC **2**；两包和 **50** | **红 R1** |
| 4 | L172 mv 全 R100＋adr blob 双点对拍 | L192 加 20 归位 | 公式在位；`git mv -n` 见 **R3** | **红 R3 连带** |
| 5 | L173 门禁零回归（GATE PASS 不翻红＋同形态＋差值归因） | L193 取态甲＋逐条归因＋禁「基本通过」 | 形制钉在位；`31,901` 属开工时点登记参考值（施工时点项，见 §4） | 绿 |
| 6 | L174 drill/s2 差值口径＋`T06_TMP` | L194 | 形制钉在位；基线 exit 1/1、s2 exit 0 属施工时点项（见 §4） | 绿 |
| 7 | L175 check-adr 命令形制 | L195 | 实跑 exit 0／读数全等（见上） | 绿 |
| 8 | L176 ADR 随动面（`docs/adr` 现值 3＝`:22`/`:23`×2） | L196 照录 | `git grep -c "docs/adr" -- architect.md` ＝ **2**；`git grep -n` 命中 **`:22`＋`:24`**；`:23` 为「可写内容」行不含该字面。`架构席终写`＝**1**、`可写内容：设计、ADR`＝**1**、lead `ADR…software-team-architect` 路由＝**1** | **黄 Y1** |
| 9 | L177–179 落位核对 3→0／0→3＋向前进核对 | L197–199 | `git ls-files ".scratch/tickets/" \| grep -c COLLAB-STRUCT` ＝ **3**（✓）；`git ls-files "<bundle>/.scratch/tickets/" \| grep -c` ＝ **1**（施工分票自身）非 0 | **红 R2** |

- **无遗失判据**：1–9 逐条对位；主票 v2 §5.3/§5.5 的「两态供裁」按裁定 §四 L47 收敛为态甲单钉，分票 L18／L82／L148／L171 的「两态」均为一般语义／真实文件名，非「两态供裁」措辞 → 正确随动。
- **§5 其余钉值**：`.collab/audits/` tracked＝复点两桶和、`.collab/adr/`＝4（实测 bundle `drafts/adr/` 恰 **4** 件 ✓）、`.collab/architect/`≥1、ledger 三文件 tracked 态（实测三文件仍 untracked ✓）、根面散件→0、decisions 直系 56＋20＝76 —— 口径自洽（除 R1/R3 连带面）。

### §2.3 数值口径重点（R1 详证·用户指定复核项）

**现盘实测（本席独立自跑，`core.quotePath=false`）**：
```
仓根 .collab/qa/                                  = 10
bundle agent-experts/.../.collab/qa/              = 234
agent-skills/fuxi-skill/.collab/qa/               = 48   ← 非 46
agent-skills/external-advisor-collab/.collab/qa/  = 2
git ls-files | grep -c "/\.collab/qa/\|\.collab/qa/" = 294
.collab/decisions/ 直系                           = 56
仓根 .collab/ 根面散件                            = 20
bundle .collab/audits/ tracked（B7 前向落件）      = 4
```

**票面/裁定硬钉**：裁定 §三① L25「施工后终值＝**48**（fuxi 46＋EAC 2 照登，非 FAIL）」；分票 §5.3 L191 同钉 48（46＋2）；分票 §3 B1 L95「其余包 qa 面（fuxi **46**＋EAC 2）」；分票 §6 L205「fuxi（**46**）、EAC（2）」。而分票 L12 开工复点行**已如实申报**：现值 294、「两包存量较登记 46＋2 漂移 **+2**＝他案 FUXI-FX-U23 新增 QA 验证件随增，照登不碰，案乙不并入、终值钉 48 照登非 FAIL，**现值以施工开工复点为准、不锁死本数**」。

**判定：构成验收判据冲突，工程师机械照跑会误判 FAIL。**
1. 施工取态甲（案乙不追改、两包不并入）：B1 只 mv 仓根 10＋bundle 234，两包 qa **原封不动留盘**。故施工后 `git ls-files | grep -c` 的终值 ＝ 两包留存之和 ＝ **开工复点现值 ＝ 50**（现盘），不是 48。
2. L191 把「施工后终值＝48」写成机械断言；同句括注「现值以施工开工复点为准、不锁死本数」只放宽了**现值**，未放宽**终值**——而终值本就等于两包现值之和，一句之内自相矛盾。「非 FAIL」括注只解释 48 的构成（46＋2），未授权 50。
3. 后果二选一：工程师跑出 50 ≠ 48 → 判 **FAIL**；或为凑 48 而误动两包 → 违反案乙与 §6 L205 禁动面。两条都错。
4. 三层错位：票内自相矛盾（终值锁死 vs 现值不锁死）／票与现盘不符（48 vs 50）／票与裁定字面相符但与裁定意图（「两包照登不并入」）不符。根因是裁定 L25 的 48 系**裁定落笔时点史实值**（当时两包确 46＋2），现值因他案漂移为 48＋2＝50；分票 L12 察觉漂移却未让判据 3／§3B1／§6 随动。

> **不预设结论**：裁定件为依据件、已入册人类裁定，本席零改、亦不代裁。修单分两层呈报（§3 R1）：分票侧由架构席随动；裁定侧若认为「终值钉 48」是实质意图而非史实登记值，须由主理人／人类压缩点出一笔裁定随注勘办，本席不预设取哪一条。

### §2.4 洁净 vs 逐字张力（用户指定复核项）

**三方对拍实测（主票 v2 原文出处钉 → 分票新值）**：

| 删改点 | 主票 v2 原文 | 分票实测 | 新值自包含性 |
|---|---|---|---|
| A3 lead `:50` | L103 含 `裁定 67a3462` → **True** | L58 含 `裁定 67a3462` → **False**；含 `ADR 文书（起草与 docs/adr 落盘＝主理人自写，不派发）` → **True** | 路由语义完整 |
| A4 依据注记 | L109 含 `b8bdadc`／`b0b449d`／`b2150c5` → **True（全含）** | L64 三者 → **False（全清）**；含 `Michael Nygard《Documenting Architecture Decisions》(2016)` → **True** | 业界锚＋「桶闭集换代 11→17＝结构落改＋returns 补录」自成文 |
| A7 链序款 | L123 含 `ES E-ADR-1″` → **True** | L86 → **False**；保留「编号四位·Status 闭集·头块五行」 | 条款自包含 |
| A7 正式件款 | L125 含 `R10/R11/R21` → **True** | L88 → **False**；保留「主理人逐字照录…哈希对等方可落 `docs/adr/`」 | 条款自包含 |
| A7 条款乙 | L126 含 `制度③` → **True** | L89 → **False**；保留 `防自审条款（转正代写通道）` → **True** | 辖域成文完整 |

**出处钉精确串清零复跑（全 0）**：`67a3462`／`b8bdadc`／`b0b449d`／`b2150c5`／`制度③`／`E-ADR`／`SRC4Z`／`裁定⑧`／`黄-`／`红-`／`青-`；`R10[^0]`／`R11`／`R21` 亦全 0。（注：宽正则曾于 L104/183/192/198/219 命中 `R10`，逐行核为 `R100` 保真串假阳性，非内部编号。）

**判定：删改合法、未损伤任一替换目标串的可执行性、无「不该删却删」。**
- 合法性依据：裁定 §二 L19「分票由架构席起草（**干净决策件形制**，对开发团队只呈现决策与执行条款、禁过程痕迹）」＋§四 L52「本件 §三 的候裁编号与治理史登记**仅属治理史面，不进施工交接件**；交接件由架构席另起草为干净决策件」。删去的是案卷指针／出处钉／内部编号，属治理史面；保留的是可自包含执行的条款文本（上表逐条 True）。
- 「交付物指针闭集」：案卷指针不得随替换文本写入席位卡／规范真源等交付面。若照主票 v2 逐字把 `67a3462`／`b8bdadc`／`R10/R11/R21` 写进 `agents/*.md` 与 `collab-fixed-structure.md`，反而**违反**该闭集。故「逐字入票」张力应解为：分票 §2 标题「替换文本逐字入票」指**入票后的替换文本即施工唯一逐字依据**（工程师照本票逐字替换，不得回主票 v2 取带钉原文），而非「与主票 v2 原文逐字全等」——此解与裁定 L19／L52 相容。
- **「该删未删」：有 1 处（黄 Y2）** —— L12 残留「**案乙**不并入」（候裁态标签，详见 §2.6）。
- **「不该删却删」：未发现** —— A3 lead 新行、A4 两行 append、A7 第 1–4 款逐条核过，实质条款与自包含成文均保留；第 5–6 款按 §6 L211 零动声明在位。

### §2.5 结构与自证

- **§4 声明闭集（python 分组实测）**：配置／席位卡／规范／README／.gitignore／tests 面 ＝ **15**；20 旧路径 ＝ **20**；20 新路径 ＝ **20**；票族 6 行 ＝ **6** —— 与票面自述全等。add 面 5 件（L184）、delete 面 1 件（L185）、mv 计数公式（L183「复点两桶和＋4＋3＋20 全 R100」）在位。
- **§6 禁动面改判一处（绿）**：L214 明文「仓根 `.collab/` 根面 tracked 散件 20 件与 `.collab/tmp-w7-msg.txt` **不属禁动面**」，与裁定 §四 L48「改判一处：散件 20＋tmp 由不搬不删改归位＋删除，其余禁动面全部维持」一致；其余逐项（`docs/adr/`＋`docs/**`＋`.archive/**`、历史文内旧字样、fuxi/EAC、六外包 README、`.collab/defects/`、门禁机件本体、三同源零 bump、SEMGV-T3 写集、`standard-sop.md` 5–6 款、TOOLHOME、`software-orchestration` 其余三件＋SKILL.md）L203–L213 逐项维持。
- **租约段（绿）**：L229–L247 齐备 —— `ticket: COLLAB-STRUCT-1-施工分票-v1`／`seat: architect`／`countersign: "architect: 租约段签注（唯一生产权）由 B2 实例化"`／`path_globs` 单件／`deny_globs` 七项／`note` 完整自证（依据＝v2 251 行/46,944B/`5eeeb3a`＋裁定 `6c495d4`；不 mv／不改 config／不补链 ledger／不建目录／不删 tmp／不 bump／不预写 T3／不跑装配）。
- **三态明示（绿）**：L221–L224 逐条分开写「做了但没落盘／落盘了但没提交／提交了但没对账」；L225「本件 commit sha 与提交后态由完工回报实测给出，正文不预写自指值」。
- **纯规格零施工自证（现盘实测·绿）**：qa 桶全在（294）、根面散件 20 在、tmp 在（三值全等）、三同源 `0.1.30` 未 bump、五卡 T3 全 0、五卡 sha 与 L11 钉值全等、ledger 三文件仍 untracked、`drafts/adr/` 4 件在、bundle `audits/` 仅 4 件前向落件、`collab/qa` in config 现值 1+1 未改 —— **STRUCT 施工确未发生**，与票面「零施工」声明一致。
- **`git check-ignore -v "<bundle>/.collab/audits/x.md"`** ＝ exit **1**（不 ignore），A6 L82 两态对拍基线在册 ✓。

### §2.6 洁净机检（用户列明关键字·逐处列明）

| 关键字 | 命中行 | 逐处定性 |
|---|---|---|
| 候裁 | **L8** | 依据件文件名 `…放行与六项候裁取态.md` ＝不可改字面 ✓ |
| 待裁 | **L146, L147, L169, L170** | 声明闭集真实文件名（`…放行呈拍与H8待裁-v1.md`、`…放行呈拍与四条待裁-v1.md` 及其 `decisions/` 新路径）＝不可改字面 ✓ |
| 席面建议 | 0 | ✓ |
| 轮次 | 0 | ✓ |
| 见第 | 0 | ✓ |
| 态甲 | 0 | ✓ |
| 态乙 | 0 | ✓ |
| 两态供裁 | 0 | ✓（裁定 §四 L47 要求销账，落实） |
| 案甲 | 0 | ✓ |
| 修正案 | 0 | ✓ |
| 第1轮／第2轮／第3轮 | 0／0／0 | ✓ |
| 汇总件 | 0 | ✓ |

**更宽扫描（本席附加·诚实登记）**：
- **`案乙` → L12**（`案乙不并入、终值钉 48 照登非 FAIL`）＝ **黄 Y2**：候裁态标签残留于施工交接件，与裁定 §四 L47「施工票不再保留『两态供裁』措辞」及 §四 L52「候裁编号与治理史登记不进施工交接件」有张力；不损伤机械执行，但洁净度不达标，且会把「候裁已裁」的事实标签带回施工面。用户列明清单未含此词，属本席更宽扫描所得，如实报。
- `两态` → L18（「两态不并存」一般语义）／L82（「两态均不 ignore」一般语义）／L148, L171（真实文件名「快照两态」）＝ 非「两态供裁」✓
- `架构席` → L90, L196 ＝ 均为 `架构席终写` 目标串（A7 清零对象／判据 8 grep 钉），非席位署名 ✓
- `复核件` → L95 ＝ 漂移说明「STRUCT 复核件落链随增 +1 照登」，非过程编号 ✓
- 出处钉精确串（§2.4）全 0 ✓

**结论**：用户列明关键字命中**仅限不可改字面**（依据行文件名＋声明闭集真实文件名），主体合规；唯一例外为附加发现的 Y2。

### §2.7 本席独立证伪附加项（R2／R3 详证）

**R2 — 判据 9 落位核对现值漏算施工分票自身**
- 分票 §5.9 L198：`git ls-files ".scratch/tickets/" | grep -c "COLLAB-STRUCT"` 施工后＝0（现值 3）；`git ls-files "agent-experts/baigong-software-team/.scratch/tickets/" | grep -c` 施工后＝**3**（现值 **0**）。分票 L12 亦写「bundle 项目根 `.scratch/tickets/` 内 **0 件**」。
- 实测：仓根 `.scratch/tickets/` COLLAB-STRUCT ＝ **3**（三件票族，✓）；bundle `.scratch/tickets/` COLLAB-STRUCT ＝ **1**，命中的正是 `2026-11-09-COLLAB-STRUCT-1-施工分票-v1.md` **本件被核物自身**（其名含 `COLLAB-STRUCT` 且已落 bundle tickets/）。
- 推演：§3 B8 L102／§4 票族六行只 mv 三件票族（v1 结构票／v2 结构票／B345 并案票），**不含施工分票自身**；施工回执按 §7 L218 落 `.scratch/` 面非 `tickets/` 子目录，不计入该 grep。故施工后 bundle `tickets/` 内 ＝ 1（分票自身）＋3（票族）＝ **4**，不是 3。工程师照 L198 跑出 4≠3 → 误判 FAIL。
- 定性：分票起草时（落盘前）bundle tickets/ 确为 0，落盘后自身使现值变 1，属**自指计数盲点**；L12 与 L198 均未随动。

**R3 — B1 包内整目录 `git mv` 落入 `audits/qa/` 子目录（dry-run 独立证伪·最硬）**
- 分票 §3 B1 L95 第二笔：`git mv agent-experts/baigong-software-team/.collab/qa agent-experts/baigong-software-team/.collab/audits`，意图「qa 改名 audits、平级」。
- 现盘实测：bundle `.collab/audits/` **目录已存在（DIR EXISTS）且 tracked 4 件**（`2026-11-08-COLLAB-STRUCT-产品席-v2窄复核-v3.md`、`…-QA席-v2窄复核-v2.md`、`…-v2终轮双席窄复核会师裁定-v1.md`、`2026-11-09-COLLAB-STRUCT-施工分票v1-QA席独立审-v1.md`）—— 正是 **B7 向前进纪律（L101）**「放行后一切新增审票／复核／登记类件直接落 `audits/` 目标名桶」的必然结果；仓根 `.collab/audits/` ＝ **DIR ABSENT**（tracked 0）。
- `git mv -n` dry-run 实测：
  - bundle 笔 → `Checking rename of '…/.collab/qa' to '…/.collab/audits/qa'`，逐件 `…/qa/x.md → …/audits/qa/x.md`；命中 `audits/qa/` 子目录 **468 行**，平级 `audits/[^q]` **0 行**，`mv-n exit=0`。
  - 仓根笔 → `Checking rename of '.collab/qa' to '.collab/audits'`，逐件平级 `.collab/audits/x.md`，落 `audits/qa/` **0 行**（目标目录不存在，改名正确）。
  - dry-run 后复测：tracked 面仍净、qa 计数仍 **294** —— 未落地。
- 根因：分票 **B7（放行即生效、审票件先落 audits）与 B1（整目录 mv 假设目标桶不存在）内在时序矛盾**，非现盘偶发。`git mv <src-dir> <existing-dir>` 语义＝把 src 移入 dst 成为子目录。
- 后果：bundle 234 件全部落到 `.collab/audits/qa/` 嵌套层而非 `.collab/audits/`；判据 3「`.collab/audits/` tracked＝复点两桶和」崩坏；判据 4 R100 新路径与 §4 声明闭集不符；A1/A2 config、五卡写的 `.collab/audits/` 与实际 `audits/qa/` 再度名实不齐；仓根笔正确／bundle 笔错误的不对称更易被漏检。**机械照跑即出错，名实对齐目标整体落空**。

---

## §3 修单建议（精确到落位·不预设结论）

> 本席为审票席，**零改被核物**；以下为呈主理人／架构席的修单建议，不含本席代为裁定。

**R1（红）· 分票侧（架构席随动）**：
- **L191（§5.3 判据 3）**：把「施工后终值＝48」改为「施工后终值＝**施工开工复点两包 qa 现值之和**（现盘 50＝fuxi 48＋EAC 2），**非 FAIL**；终值不锁死本数」，或等效表述；括注「现值以施工开工复点为准」须同时覆盖终值。
- **L12（开工复点行）**：「终值钉 48 照登非 FAIL」随动改为「终值＝两包开工复点之和（现盘 50）非 FAIL；46＋2＝裁定登记史实值」。
- **L95（§3 B1）／L205（§6）**：「fuxi 46＋EAC 2」「fuxi（46）、EAC（2）」改为「两包 qa 现值（现盘 fuxi 48＋EAC 2＝50），以开工复点为准」，或明确标注「46＋2 为裁定登记史实值、现值已漂移 +2」。
- **裁定侧（呈主理人／人类压缩点，本席不预设）**：裁定 §三① L25 的「终值＝48」若属实质取态意图而非史实登记值，须出一笔裁定随注／勘办笔澄清 48 的性质与「终值随开工复点」的口径；若属史实登记值，则只需分票侧随动即可。两案供裁，不回流请裁六项本体。

**R2（红）· L12／L198**：二选一 ——（甲）把 grep 口径收窄为三件票族的精确文件名（如 `grep -E "结构名实对齐与规范成文票|工序纪律并案维护票"`，排除施工分票自身与回执），使现值 0／施工后 3 成立；（乙）保留现命令，把 bundle 现值改 **1**、施工后终值改 **4**，并声明施工分票自身计入、施工回执命名不带 `COLLAB-STRUCT`。同步修 L12「bundle 内 0 件」。

**R3（红）· §3 B1 L95**：包内笔改为**逐文件 mv 到已存在 `audits/` 平级**（如 `git mv <bundle>/.collab/qa/* <bundle>/.collab/audits/` 并逐件核 R100），或先明确 `audits/` 已有 4 件的处置（该 4 件本就应在 audits/，无需搬动）；**禁止整目录 `git mv qa audits`**。同时在 §5 判据 3／4 增「`.collab/audits/qa/` 子目录不存在」的反向机械断言；并在 §3 B7 与 B1 之间点明「放行即生效 ⇒ 施工开工时 audits/ 桶必非空」的时序处置。仓根笔（目标桶不存在）经 dry-run 平级正确，可保留但建议同样加断言。

**Y1（黄）· L196／L53–55**：判据 8 现值由「3＝`:22`／`:23`×2」改为「**2**（`:22` 写域行＋`:24` 例外子句行各 1；`:23` 为「可写内容」行不含该字面）」；A3 的 `:23`／`:24` 内容标法与现盘颠倒，按 §1.3 L20「行号按内容锚定位、不锁死行号」已兜底、不阻断，建议顺手勘正标注或统一改为内容锚表述。主票 v2 §1.1 L49／§5.8 L176 同源标注偏差一并照登（依据件零改）。

**Y2（黄）· L12**：把「案乙不并入」改为「两包不并入本批迁移（按裁定 ① 取态）」等不带候裁态标签的表述；保留 `候裁`（L8 依据件文件名）／`待裁`（L146/147/169/170 声明闭集真实文件名）等不可改字面不动。

---

## §4 只读边界与复跑范围声明（不给假绿）

- **本席自跑复现的读数**：开工三读数＋链漂核查；三件行数／字节／sha256；`2a4e262` 单件 name-only／name-status／ancestor；qa 四分桶与总数 294；decisions 56／根面散件 20／bundle audits 4；tmp 三值与 `.gitignore:36`；五卡 sha＋T3 全 0；三同源版本；`drafts/adr/` 4 件；ledger 三文件；`check-ignore` exit 1；判据 1（json.tool 0/0＋同源全等 True）、判据 2（13 行／5occ4行／1+1）、判据 7（check-adr 实跑 exit 0 读数全等）、判据 8 各现值锚、判据 9 两命令现值；§4 分组计数；20 件三方集合对名；洁净机检逐关键字行号；出处钉精确串清零；三方逐字成文行对拍；洁净删改三方对拍；`git mv -n` dry-run 两笔。
- **未由本席执行、且如实标为「施工时点复跑项」的项**（本席只读零改，不代替工程师产生施工基线）：`run-gates.sh --no-write` 两读数对拍（分票 L193 参考值 31,901 属开工时点登记）、drill 两笔 `T06_TMP` 注入形制基线（L194 钉 exit 1/1）、`test_lease_instantiation.py` exit 0、`python -m json.tool` **施工后**值、`git cat-file blob` 双点对拍、20 件逐件 R100 回执。本席核的是**命令形制是否在票内钉死、是否可机械验证、现值是否与现盘一致**，未报上述项的施工后读数，故不构成假绿。
- **fresh eyes／零改／落点**：未读另一席审票件正文、未通信（仅 commit subject 机械暴露已如实申报）；被核物与两依据件零改；本件只落 `audits/` 新桶过程域，未写任何交付面；他案在制品照登不碰。

---

## §5 本件落链声明

- 本件为 v1，单件双侧 pathspec `collab:` commit，禁 `git add -A`／`--amend`／`reset`／`--no-verify`；commit 带 ≥7 分钟 timeout（pre-commit 钩子输出约 8MB）。
- **本件 commit sha／行数／字节／sha256 前 12／`git show --name-only` 恰一件** 属提交后自指读数，正文不预写，由本席完工回报给主理人（team-lead）实测给出。
- 判词终态：**打回（不放行）· 红 3（R1/R2/R3）／黄 2（Y1/Y2）／其余核通过**；建议勘办 R1–R3 后重出施工分票 v1.1 再行审票。
