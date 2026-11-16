# SWB-A14H1 · check-pointers 自身两枚悬空处置规格票（v1·纯规格·零施工）

- 票号：**SWB-A14H1**
- 票名：**A14 黄-1 处置规格票·悬空指针检查器自身文件内两枚既存 BLOCK**
- 票型：维护（轻量工作分支·单批最小票形态·体例照 SWB-CPTRACE／SWB-CPRC4／SWB-CPRC5 先例）
- 起草席：架构席 arch-a14h11
- 票面落点：`.scratch/tickets/2026-11-16-SWB-A14H1-check-pointers自身两枚悬空处置规格票-v1.md`
- 来源：候补池在册项「A14 黄-1」（悬空指针检查器自身文件内两枚既存 BLOCK），获决策者裁定开票处置
- 候裁点：§七（本票预期零枚·闭集收紧自查见彼节）

> **票面自注**：本票正文对一切悬空目标仅叙述性提及＝裸文写＋全角斜杠（／U+FF0F），不落反引号路径指针＝防自咬（CPTRACE 条款体例自证）；正文反引号路径形态引用者均已实测在盘可解析；§六前后形态对照块内 token 以 ⟦⟧ 标记包裹（⟦⟧ 为票面定位标记非落盘内容，落盘时 ⟦⟧＝反引号字符）。

---

## 〇、开工读数（起草轮现跑·禁抄在册旧数）

- `git rev-parse --short HEAD`＝`8d98588`＝与派工预期链顶全等。
- `git status --porcelain` 照登零带入：tracked 脏面一枚＝M agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl（他案）；仓根 untracked 散件群＝.collab／ 案卷散件群＋.collab／research／ 群＋.py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt＝一律照登、零带入、零清理；亡席残族 .scratch／arch-cprc41／ 等现盘实存（gitignore 面不入 porcelain）＝照登零读零引用零清理；index 零 staged。
- 自靶现跑＝`python share/check-pointers.py --target share/check-pointers.py`（完整输出落本席 scratch 族 selfgate-before.txt 无截断）＝**exit 1·BLOCK 恰两枚**（读数原文见 §二）。
- 缺省域现跑读数＝`.scratch/a14h1-default.txt`（在册缺省跑落盘件·grep -c "BLOCK" 口径＝**22816**·与在册钉值吻合·其中 `^share/` 开头行计数＝**0**）。
- 豁免快照现读＝`share/baseline-pointer-exempt.json` items 计 **9** 项（token＋files 结构），本两枚 token（references／20-handoff.md 与 docs／INDEX.md 二值）均**不在册**（python 逐项现查坐实）。
- 目标实存性现查＝`agent-skills/multi-collab/references/20-handoff.md` 实存 **6138 字节**；仓根 `docs` 目录不存在（ls 坐实）。

## 一、声明闭集

1. **案件名**：A14 黄-1＝悬空指针检查器 `share/check-pointers.py` **自身文件内**两枚既存 BLOCK 悬空。
2. **射程**＝仅该文件内两处文案：
   - **行 272**：`resolve()` 函数 docstring 内候选解析式第四条示例中的例证 token；
   - **行 304**：带斜杠落空分支的注释论证段中的真死引用例证 token。
3. **改动性质**＝纯文本（docstring／注释）文案改动，**零逻辑改动**。
4. **禁动面（全部一字不动）**：
   - 该文件一切可执行逻辑：判定函数体、正则（BACKTICK_RE／FILE_LINE_RE／ANNOTATION_RE 等）、跳过表（SKIP_EXACT／SKIP_SUBSTR 及示例/占位/命令片段跳过机制——扩白名单＝真源口径改动，禁入本票射程）、候选构造逻辑；
   - `DEFAULT_SCOPE` 常量（行 76）；
   - 豁免快照 `share/baseline-pointer-exempt.json`（不扩 items）;
   - `share/run-gates.sh`（含行 141 调用形态）；
   - 路由表 OA-D6 严重度配置；
   - 该文件内除行 272／304 两枚点名行外的一切行（含 docstring／注释其余全部文字）。

## 二、取证（在册实测事实＋本席开工轮复跑坐实）

**自靶输出照录（改前态·selfgate-before.txt 全件两行·exit 1；防自咬体例＝块内去反引号包裹、斜杠换全角，反引号包裹态在 scratch 读数件实存）**：

```
share/check-pointers.py:272: BLOCK OA-D6 指针悬空 references／20-handoff.md → 目标不存在
share/check-pointers.py:304: BLOCK OA-D6 指针悬空 docs／INDEX.md → 目标不存在
```

**语境性质（实读坐实）**：
- **行 272**（resolve() docstring·候选四示例）原文＝六空格缩进的候选第四条「4. 相对本文件所在包根（包内跨目录引用，如 ⟦references/20-handoff.md⟧）」——反引号内 token 系**例证 token**，演示「包内跨目录短写法」这一候选式，非作者立活指针。
- **行 304**（带斜杠落空分支注释论证段）原文＝「② 更要紧的是它会**吞掉真报**——⟦docs/INDEX.md⟧ 这类指针的父目录已被删除，」——作者用**真死引用**作悬空典型形态的例证；该注释的论证力度依赖此例证性。

**目标实存性**：
- token「references／20-handoff.md」的真实件 `agent-skills/multi-collab/references/20-handoff.md` **实存**（6138 字节·tracked）；但从 share／ 上下文按 resolve() 七候选全落空——share 桶无 references／ 子目录；share／ 文件的 pkg_root 候选层＝仓根，仓根／references／20-handoff.md 不存在；短写法跨包对 share 桶不可解析（§〇现查＋源码行 281-293 直读坐实）。
- token「docs／INDEX.md」**全仓真无**＝仓根无 docs／ 目录（§〇 ls 坐实）＝真死引用。

**关键新事实（勘正前案在册句·CPTRACE 收口在册句扰动担忧解除）**：
- `DEFAULT_SCOPE = ("agent-experts", "agent-skills", "softwares")`（check-pointers.py 行 76·直读坐实）——**share／ 桶不在缺省扫描域**。
- `share/run-gates.sh` 行 141 对 check-pointers 为缺省形态调用（`--root $ROOT`），不扫 share／。
- 缺省现跑输出（`.scratch/a14h1-default.txt`）零 `^share/` 行；grep -c "BLOCK" 口径＝**22816 与在册钉值吻合**。
- 豁免快照 9 项不含此两枚（§〇现查）。
- ⇒ **黄-1 处置对缺省钉值零扰动**（不涉钉值随动）；前案 CPTRACE 收口在册句「因在缺省域涉基线扰动（−4 或转 WATCH）需独立排程评估与 A14 豁免口径交互」的扰动担忧由本批实测**解除**；另票法理仍立（根因异＝share 交付面跨域＋例证 token 性质，非回执史件定向改字族）。

## 三、取态裁定（架构席职权·写死·不留开放选项）

### 枚一＝行 304（docs／INDEX.md·真死引用例证）→ 叙述化复原

- **取态＝叙述化复原**：去该 token 反引号＋半角斜杠换全角（／U+FF0F）＋随注（注明该件已随历史搬家消亡＝本注释所论悬空典型形态的真例）。前后形态逐字节写死于 §六枚一。
- **先例两级在册**＝CPTRACE 施工笔 `0d36f90` ＋ CPRC4 施工笔 `f237e83`（两级皆：去反引号使 BACKTICK_RE 不再捕获＋全角斜杠双保险防其它形态捕获＋随注保全例证可读性）。
- **论证**：该 token 事实形态本就＝真死引用（父目录已随历史搬家消亡，§二实查坐实），叙述化＝形态与事实对齐，无语义损失；且该注释的论证力度依赖「真死引用」例证性——随注正是把这一例证性从「反引号指针形态」迁移为「叙述形态＋消亡注记」，论证力度零损。
- **不取改字补全**：docs／INDEX.md 全仓真无（§二），无可补全的真实目标＝补全径不可行（造一个假目标＝违禁动面）。
- **不取豁免**：入 A14 豁免 items＝share 交付面真源口径改动＋豁免命中仍出 WATCH 行（单文件 exit 恒 1 黄不可闭）＋违 A14 收紧取向——CPTRACE／CPRC4 两级机械否决在册，不重议。

### 枚二＝行 272（references／20-handoff.md·例证 token·目标在他包实存）→ 叙述化复原（甲案）

- **取态＝甲案叙述化复原**（同枚一基本体例：去反引号＋全角斜杠；**不加**消亡随注——该件未消亡，加注即失实）。前后形态逐字节写死于 §六枚二。
- **乙案（换全径写法）不取·理由写死**：
  1. **示例教学语义破坏**：候选四这条示例教的是「**包内跨目录短写法**」（与候选二「全路径写法」相对——候选二的示例正是全径形态 `agent-skills/multi-collab/references/40-deployment.md`，docstring 行 269 直读在册）。换成全径＝把候选四示例改成候选二形态的示例＝该示例教的东西被改掉＝超出「纯文本零逻辑」射程的**语义改动**，违 §一-3 改动性质声明。
  2. **目标实存性不改变悬空判定**：checker 以文件所在上下文解析（resolve 七候选层含 pkg_root 层＝对 share 文件即仓根），短写法在 share 桶不可解析是**该 checker 的既定口径**（跨包短写法只认三分类目录桶前缀式，源码行 283-293 直读坐实）。枚二 token 的目标虽在他包实存，但它在此处**从来不是活指针**＝docstring 内例证 token；叙述化＝形态与「例证非指针」的事实对齐，同枚一同构。
  3. **扩白名单禁入射程**：checker 跳过机制已有「示例、占位、纯锚点、命令片段不判」的先例概念（SKIP_SUBSTR 注释·源码行 85-87 直读在册），可为「例证 token 不判」作论证素材——但扩 SKIP 白名单＝**真源口径改动**，禁入本票射程（§一-4），不取、不列候裁（取用才呈）。
- **叙述化后例证可读性核验**：后形态「如 references／20-handoff.md 这类写法」仍完整传达候选四所指写法（全角斜杠对中文读者无阅读障碍），例证保留、仅失去可复制的指针形态——此损失正是本票目标（例证 token 不该被当活指针解析）。

**两枚取态总述**：两枚皆叙述化复原（枚一带消亡随注·枚二不带）＝零 share 其它文件触面、零逻辑改动、零豁免扩面、零真源口径改动。

## 四、扰动登记（写死）

- **缺省钉值零扰动**：`DEFAULT_SCOPE`（行 76）不含 share／ 桶；run-gates.sh 行 141 缺省形态调用不扫 share／；缺省现跑 `.scratch/a14h1-default.txt` 零 `^share/` 行、grep -c "BLOCK" 口径＝**22816**（§二新事实）。⇒ 本票处置**不涉钉值随动**；前案 CPTRACE 在册句「因在缺省域涉基线扰动……需独立排程评估」的扰动担忧由本批实测解除（解除登记已在 §二，本节为扰动面写死）。
- **GATE 发现数口径**：上批在册钉值 151508；本票两枚在 share／ 桶、不在 run-gates 缺省调用射程 → **预期变化＝零**；验收判据以「无新红栏＋GATE PASS exit 0」为主判，发现数名义预期 −0（他案波动照 CPRC4／CPRC5 先例容忍口径）。
- **豁免快照零触面**：9 项 items 一字不动（两枚不在册也无需入册＝叙述化后 checker 不再捕获，无需豁免层介入）。

## 五、V 系机械验收判据（每条＝可照跑命令＋预期）

- **V0 改后自靶归零**：`python share/check-pointers.py --target share/check-pointers.py` → **exit 0** 且输出**零 BLOCK 零 WATCH**（空输出；NOTE 行若在场须逐行核文案非两枚旧 token）。
- **V1 改前后自靶差＝恰消此两枚**：改前态两枚清单照录＝行 272（token references／20-handoff.md）＋行 304（token docs／INDEX.md）（前态读数件 selfgate-before.txt 在册）；改后 V0 空输出＝差集恰此两枚、零新增。
- **V2 缺省面零扰动**：改后缺省跑 `python share/check-pointers.py` 完整输出落盘（禁截断）→ grep -c "BLOCK" 口径A 仍＝**22816**；**跑前跑后双读数皆须现跑落盘**（跑前读数可引 `.scratch/a14h1-default.txt` 但验收轮须自跑对拍）；`^share/` 行计数前后皆 **0**。
- **V3 逻辑零动**：`git diff` 该文件＝改动**仅限两行文案**（行 272／304·施工时实际行号为准）；其余行零 diff。判据写死＝**AST 对拍**：python ast 解析改动前后源码（剥 docstring 后 ast.dump 逐字符相等）＋`git diff --stat` 该文件＝**2 行改（+2 −2）、零增删行、零其它 hunk**；两口径并行，blob 级行数对拍兜底（后形态行长可变，字节级对拍只约束点名两行前后形态＝§六逐字节照抄）。
- **V4 防自咬**：本票面落笔前靶检 exit 0（起草轮自证·见 §八）；施工轮回执正文自身靶检 **exit 0**；回执正文对悬空路径仅叙述性提及（裸文写＋全角斜杠体例自证）。
- **计数法教训照录（硬线）**：枚数计数用**反引号包裹态计数**（python 读文件文本 count(chr(96)+token+chr(96))）或**逐字节对拍**为准；按行 `grep -cF` 有假红风险（同行多枚／非包裹态裸文命中同串）。两判据相抵时**以逐字节零动判据（V3）为准**。

## 六、逐枚施工指令（前后形态＝整行照抄级·⟦⟧＝反引号字符标记）

落点文件＝`share/check-pointers.py`（tracked·仓根 share 桶·行号以开工窗 8d98588 态为准，施工时以 token 定位复核）。定位方法＝按行内唯一子串定位（枚一搜「吞掉真报」、枚二搜「相对本文件所在包根」），不以纯行号定位（防随行偏移错位）。

**通则**：除下列两枚点名行外全文件逐字节零动；⟦⟧ 为票面标记非落盘内容——落盘时 ⟦X⟧＝反引号＋X＋反引号、⟨X⟩ 不适用；本票 §六块内一律不落成对反引号包路径（防自咬体例）。

**枚一（行 304·叙述化复原·带随注）**——前形态整行原文（四空格缩进＋# 注释·⟦⟧ 处落盘为反引号字符）：

```
    #   ② 更要紧的是它会**吞掉真报**——⟦docs/INDEX.md⟧ 这类指针的父目录已被删除，
```

后形态整行全文：

```
    #   ② 更要紧的是它会**吞掉真报**——docs／INDEX.md（仓根 docs／ 目录已随历史搬家消亡＝本注释所论悬空形态的真例）这类指针的父目录已被删除，
```

（改动面＝仅该 token：去反引号＋半角／换全角／＋括注随注；行首缩进、①②序号、**吞掉真报**加粗号、破折号、行尾逗号及其余一切字符逐字节零动。下一行 305 起零触。）

**枚二（行 272·叙述化复原·不带随注）**——前形态整行原文（六空格缩进·docstring 内·⟦⟧ 处落盘为反引号字符）：

```
      4. 相对本文件所在包根（包内跨目录引用，如 ⟦references/20-handoff.md⟧）
```

后形态整行全文：

```
      4. 相对本文件所在包根（包内跨目录引用，如 references／20-handoff.md 这类写法）
```

（改动面＝仅该 token：去反引号＋半角／换全角／＋尾部「这类写法」四字（补接句法防叙述断裂）；候选序号「4.」、括号对、句读及其余一切字符逐字节零动。docstring 其余行零触。）

**施工轮禁触面（写死）**：两枚点名行之外的一切行——尤其 §一-4 禁动面所列各段（SKIP 表注释／DEFAULT_SCOPE／候选构造／302-308 注释段其余行／306 行 `to-tickets/references/…` 上游仓提及——该行有 EXTERNAL_MARK 机制在场，现跑非 BLOCK，勿顺手改）。

## 七、候裁面（闭集收紧·预期零枚）

**候裁枚数＝0。** 逐面自查：①两枚处置形态＝架构席职权（设计／边界约束面）已写死，无保留闸项；②枚二甲乙案权衡＝本席以源码直读＋语义分析收敛（乙案破坏示例教学语义＝非决策者范畴之利害对立，属技术裁量）；③真源口径改动（扩 SKIP／扩豁免／改 DEFAULT_SCOPE）三径全**不取**＝不取即零呈拍触发（呈拍条件＝取用才呈）；④无未收敛对立、无决策者保留闸项。若验收或复审轮翻出真决策者范畴项，随该轮另列，不回改本票（append-only）。

## 八、纪律段（起草笔自证）

- 增量落盘纪律＝已执行（开工读数后骨架先落**工作区文件**·逐段 append 填实·全程仅一次 commit＝成文＋落笔前靶检 exit 0 后一次落链；写作全程磁盘有可恢复在作成文＝防席亡全损体例）；
- 起草席临时工作物居本席 scratch 席族（.scratch／arch-a14h11／：selfgate-before.txt／after-probe.py／probe1.md 等留痕）＝完工随族自删（commit 留证文件 commit1.txt 除外可保留）；本票＝留存工件落 tickets 桶先例（CPRC5 同桶）；
- 本票面防自咬：悬空字样一律裸文写＋全角斜杠；§六前后对照块以 ⟦⟧ 标记承载 token、块内不落成对反引号包路径；落笔前本票面靶检 exit 0 才 commit；
- 后形态已试装预验（本席 scratch 族 after-probe.py＝两枚后形态整行装配于原件副本·自靶现跑 **exit 0**；AST 剥 docstring 对拍＝改动前后**逐字符相等**＝逻辑零动自证先跑在册。原件未触）；
- commit 纪律＝单件 pathspec 只 add 本票面一件·add 紧邻 commit 零窗口·禁 add-A／禁 amend／禁 no-verify·message `collab: ` 起头零 at 零反引号·尾标 [SWB-A14H1-TICKET] 置 message 最末位·commit 输出重定向 .scratch／arch-a14h11／commit1.txt·timeout 七分钟档（pre-commit hook 重扫慢·SIGTERM 教训在册）；
- 他案脏面（ledger 一枚＋仓根散件群＋亡席残族 .scratch／arch-cprc41／ 等）照登零带入零清理零引用；
- 不碰真源：本起草笔只写票面文件＋commit 票面一件；share／ 下零触碰（施工归后续工程师席按 §六执行）。

