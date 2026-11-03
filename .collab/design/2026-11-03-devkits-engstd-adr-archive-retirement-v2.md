# ENGSTD · devkits 工程规范定标设计件（ADR/归档/退役三题）v2 · 架构席定稿（双席审票修正批后）

- 起草实测 HEAD：`bce8ff4`（会师登记笔·`git rev-parse --short HEAD`·工作仓 `D:\multi-agent-collab-devkits`·main）；开工 ANCHOR 读数即此。
- 件型＝**定标设计件 v2（定稿）**：v1（`a136630`·`.collab/design/2026-11-03-devkits-engstd-adr-archive-retirement-v1.md`）经双席独立审票（PM `a00c798` 红1黄4／QA `3492912` 红2黄5），会师登记＝`.collab/2026-11-03-ES-工程规范定标-双席审票会师登记-v1.md`（`bce8ff4`）。按代笔禁令由作者席出 v2 完整定稿；**v1 原地不改**，效力关系＝后生效覆盖先前（本 v2 生效后 v1 只作史述）。
- 兼容基线不变＝裁定三（`.collab/decisions/2026-11-03-项目自由分层与collab固定结构及docs约定md.md`·§一~§二点九）。三题主结论经双席一致认可不推翻。
- 计数口径：occurrence 口径；**本版全部申报数附可复现命令**（Y-1 整改）；行号锚 HEAD=`bce8ff4`；判据命令自带落盘重定向；负例 exit≠0 断言。

## 声明闭集（1 件·本笔唯一可写面）
- 声明闭集：
- .collab/design/2026-11-03-devkits-engstd-adr-archive-retirement-v2.md

---

## 〇、修订记录（v1→v2·红/黄项逐条处置）

| 项 | 处置 | 落点 |
|---|---|---|
| **红-①**（PM红-1＋QA R1）E-ARC-1 扫描面缺口 | **定标＝全文本域扫描案**（弃「显式豁免清单＋README 记账」案，理由见 B.3-3）；纳入裸基名引用族口径；「先换锚」程序覆盖 receipts/qa/design/dispatch/docs/README 全部活引用族；保留 QA 硬线＝修好前票面族移除不得启动。会师件实测读数（48/84 票面外活引、receipts→票 88 处/29 票、deliverables 裸基名 67 处）沿用并标注复跑来源（§一-B 读数账） | E-ARC-1 重写 |
| **红-②**（QA R2）E-ARC-3「GATE PASS＝永存等价断言」不成立 | **撤销该主张**（实测复核：spec_file 锚指 decisions 去重＝3/13 名，verdicts.md 与十件现行裁定零锚＝断言覆盖面确实不足）；与 E-ADR-5 **并件升级为 decisions 逐名清单对账**（零新构件） | E-ARC-3′＋E-ADR-5′ |
| **Y-1** 申报数不可复现 | 票互引／交付面活引申报数全部重出＋每项附口径命令（v1 旧数 26/15 作废，重出读数见 §一-B 读数账；口径差异如实登记） | §一-B 读数账 |
| **Y-2** 权限数据面缺行点名 | A.2-3 增点名目：**seat-permissions 两 config 的 host（主理人）行现无 `.collab/decisions/` write_globs 授权行**＝裁定登记族现行租约机制下不可签发，补行属随动工目（与 ADR 族随动同票） | A.2-3 |
| **Y-3** E-ADR-3 双向校验半缺 | 补被取代件存在性查核＋新→旧向校验（Supersedes 行指旧件且旧件 Status 回指，缺边即拒） | E-ADR-3′ |
| **Y-4** E-RET-1 词形不对称 | (a)(b) 词形对齐闭集＝`退役[：:]`∪`物理清退`∪`清退`先例词族（实测现盘「退役：」7 处／「物理清退」6 处），机制上线不误判先例 | E-RET-1′ |
| **Y-5** E-ADR-4 白名单无内容约束 | 适用域**明示限 `*ADR-*` 文件名族**（裁定登记族史实注记不误触）＋注记行内容约束（必含日期戳＋触发件引用，禁改既有行语义） | E-ADR-4′ |
| **Y-6** SemVer 引用位置 | deprecation→minor 条款改挂 **SemVer FAQ 款**（v1 误挂 §7＝MAJOR 条款）；引用账 #7 同步更正 | C.1＋引用账 |
| **Y-7** ㊺违例存量定性 | check-collab-lint 三处 spec_file 锚票面＝拍板㊺判据下**违例存量**，定性改「**闭环化换锚先行**」（EAC-CLN 先例同类）；**删除「实质不可删」判定**——该类票移除前须先把 spec_file 换锚至其闭环件，换锚批先行 | B.3-3＋E-ARC-1′ 附款 |

---

# T-A · ADR／决策记录机制

## A.1 业界最佳实践对照

1. **Nygard 格式与状态机**（2011 定式）：一条决策一件短文档，五段＝Title/Status/Context/Decision/Consequences；Status 合法取值 proposed／accepted／rejected／deprecated／superseded；**编号单调递增永不复用；被推翻的决策留在日志中标 superseded，因为「知道它曾经是决策」本身有价值**。〔来源：Architecture Decision Records Written by Your Coding Agent／2026-11-03 检索／§"What an architecture decision record is"引 adr.github.io 与 Nygard 2011／https://nimbalyst.com/blog/architecture-decision-records-written-by-your-coding-agent〕
2. **supersede 不改写纪律**：「Treat accepted records as immutable. If a decision changes, write a new ADR instead of editing the old one. Then mark the old record as superseded and link both documents together.」＋常见错误清单点名「Editing accepted records — rewriting history destroys the value of the log」。〔来源：Architecture Decision Records (ADR) Explained: A Complete Guide／2026-11-03 检索／§Status Lifecycle＋§Common Mistakes／https://vickybytes.com/blog/architecture-decision-records-explained〕
3. **MADR 状态与替代流程**：Status 闭集 `proposed | accepted | rejected | deprecated | superseded by <adr>`；supersession＝新建 ADR→旧件 Status 改 `Superseded by new-adr`→新件反向 `Supersedes old-adr`（双向）。〔来源：MADR 模板实战指南／2026-11-03 检索／§元数据头＋§八 supersession 流程／https://blog.csdn.net/gitblog_00602/article/details/161209131；模板真源 adr.github.io/madr〕
4. **落位惯例与「ADR 长存 vs 过程物归档」之分**：惯例 `docs/adr/`／`docs/decisions/`，编号＋slug；工具链（adr-tools/Log4brains）以编号件不删为前提。〔来源：ADR Explained／§Where to Store；ADR glossary／§"A superseded ADR is never deleted; the history is the value"／https://www.getlockstep.dev/glossary/adr〕

## A.2 本仓采纳口径（定标结论·双席认可）

1. **落位＝维持 `.collab/decisions/`，不迁 `docs/`**（理由不变：docs＝当前存活干净交接件定义／spec-provenance 锚现状／裁定三§二点六.4 治理记录归项目 `.collab`）。ADR 正件与裁定登记**同桶分族**，不新增子目录。
2. **件体格式＝Nygard 最小骨架＋状态行闭集＋双向互链**：命名定式（决策登记现式保留；ADR 正件 `YYYY-MM-DD-ADR-NNN-<slug>.md`·NNN 三位零填充·项目内单调递增不复用）；头部块必含 `Status：`（闭集 `Proposed/Accepted/Rejected/Deprecated/Superseded by <件>`）／`Deciders：`／`Date：`／`Author：`／`Registrar：` 五行；supersede 程序＝新件落盘＋旧件**只改 Status 行一处**＋双向互链；旧件正文其余零触碰。
3. **三族分权落盘（定标·Y-2 补目）**：
   - 决策者裁定登记族＝登记权＝主理人（誊录权明文·Author/Registrar 分离自洽代笔禁令）；
   - 架构决策正件族（ADR）＝落盘权＝架构席（`.collab/drafts/{design,adr}/` 草稿→`.collab/decisions/ADR-*` 正件；draft 无 `Status: Accepted` 不生效，正件落盘即生效）；
   - 判词族＝verdicts.md 既有规范一字不动。
   - **随动点名（Y-2）**：`config/seat-permissions.json` 与 `config/seat-permissions-hooks-map.json` 对 `.collab/decisions/` **零 write_globs 行**（实测：两 config 全部 write_globs 无该路径＝现盘 grep 零命中）——裁定登记族（host/主理人行）与 ADR 族（architect 行）在现行租约机制下**均不可签发**。后续施工票须补两行：host 行＋`.collab/decisions/`（裁定登记誊录通道）＋architect 行＋`.collab/decisions/`（仅 `*ADR-*` 文件名族）；与 T08R 权限机件同面，避两次动权限表。
   - 分族机械判据＝文件名族前缀闭集：ADR＝`*ADR-*`；判词＝verdicts.md 单件；其余＝裁定登记族。
4. **SOP 增「§十一之一 裁决落地」节点**：裁决队列出列件＝对应席位（裁定登记＝主理人／ADR＝架构席／判词＝独立审计席）在到达后首笔可写窗口内落盘 decisions 并单独 commit；落盘前该裁决不具执行效力（票面引用未落盘裁决＝引用方违例）。
5. **`.collab/human/deliberations/`＝审议过程面（无效力）／`.collab/decisions/`＝裁决生效登记面（闭集三族）**（分工定标不变）。

## A.3 可机械判定条款草案（v2 定稿）

```
E-ADR-1 头块断言：文件名匹配 `*ADR-*` 的 decisions 件，头 12 行内必含
  `^- Status：(Proposed|Accepted|Rejected|Deprecated|Superseded by .+)$`
  ＋`^- Deciders：`＋`^- Date：YYYY-MM-DD`＋`^- Author：`＋`^- Registrar：`；缺任一行 exit 1。
E-ADR-2 编号唯一不复用＋递增：`ADR-(\d{3})` 提取集重复 occurrence>1 exit 1；
  新落盘编号必＝既有最大＋1（跳号/复用 exit 1）。
E-ADR-3′ 双向 supersede 全向校验（Y-3）：
  (a) 旧→新向：Status 含 `Superseded by X` 的件，X 必在盘（缺＝悬空 supersede exit 1）
      且 X 头块含 `^- Supersedes：` 行并指回该案名；
  (b) 新→旧向：任何含 `Supersedes：Y` 的件，Y 必在盘且 Y 的 Status 行必含本件引用；
  双向图边缺一 exit 1（python 逐边校验）。
E-ADR-4′ accepted 不可变（Y-5 适用域＋注记约束）：适用域**明示限 `*ADR-*` 件**
  （裁定登记族的史实注记追加不受本条辖制，走「原件不删只作注记」机理）；
  diff 白名单＝Status 行＋Supersedes 行＋文末追加注记行；
  注记行内容约束＝必含 `YYYY-MM-DD` 日期戳＋触发件引用（`ADR-\d{3}` 或案件路径），
  且不得与既有行文本重合改写（行级 diff 判定：追加＝新增行 only）。
E-ADR-5′ 三族分桶对账（与 E-ARC-3′ 并件，见 B.3）：decisions 逐名清单三桶
  （`*ADR-*`／`verdicts.md`／登记族）和＝`git ls-files .collab/decisions/ | wc -l`；桶外件 exit 1。
```

---

# T-B · 归档策略

## B.1 核心争点与业界对照（不变）

- A 案（工作树零归档面）：「history preserved → absolutely no reason not to remove」＋「delete and **tag the revisions**」＋归档目录弊病「links or relative references will no longer apply」。〔SE 289904／Thomas Owens 答＋Sergio Velasquez 答／https://softwareengineering.stackexchange.com/questions/289904/delete-unused-source-code-from-the-repository-or-keep-an-archive-folder〕
- B 案（自建归档面）：`git mv` 入 `_archive/`＋归档 README 登记退役日期（心理安全网）。〔dev.to／§Code Graveyard／https://dev.to/masaoshimadaopen/dont-delete-archive-how-i-safely-retired-zombie-code-with-git-mv-and-archive-53a0〕

## B.2 读数账（v2 重出·Y-1·全部附命令·锚 HEAD=`bce8ff4`）

| # | 读数 | 命令（落盘重定向省略） | 本次实测 | 会师登记数（复跑来源＝PM/QA 审件） |
|---|---|---|---|---|
| R1 | 票目录内对票文件全路径互引 | `grep -rno "tickets/2026-[0-9]*-[A-Za-z0-9._-]*\.md" .collab/tickets/ \| wc -l` | **26**（排自引 **24**） | 复跑 39（排自引 37）——口径差＝会师席正则含无日期前缀票名形态；两式并存登记，判据取 E-ARC-1′ 全式 |
| R2 | deliverables→票全路径活引 | `grep -rno "\.collab/tickets/[^ )\`\"']*" deliverables/ \| wc -l` | **15** | 4（会师席全式路径口径）／67（裸基名族） |
| R3 | deliverables 裸票名 token 族 | `grep -rEo "(ENG\|EAC\|FUXI\|SWB\|SOP\|GH\|MC)-[A-Z]?[A-Za-z0-9]+[0-9]+[A-Za-z]*\|TKT[0-9]+\|DIRRELOC" deliverables/ \| wc -l` | **217**（含 SKILL/changelog 史述与检查器 ID 引用） | 67（会师席窄口径＝活引用分账后）——**量级确证：裸基名族远大于全路径族，扫描面必须覆盖** |
| R4 | receipts→票面活引 | `grep -rno "\.collab/tickets/[2E][^ )\`\"',，]*" .collab/receipts/ \| wc -l` | **42**（窄式） | 88 处/29 票（会师席全式） |
| R5 | qa/design/dispatch/docs/README→票面活引 | `grep -rno "\.collab/tickets/[^ )\`\"',，]*" .collab/qa/ .collab/design/ .collab/dispatch/ docs/ README.md \| wc -l` | **101** | 107（会师席全式） |
| R6 | spec_file 锚指 tickets（去重） | `grep -rh "spec_file: \.collab/tickets/" deliverables/ tools/ \| sort -u` | **1 名**（EAC-SK5-机检票×3 处） | 同 |
| R7 | spec_file 锚指 decisions（去重） | `grep -rh "spec_file: \.collab/decisions/" deliverables/ tools/ \| sort -u` | **3 名**（裁决记录/2026-10-25/2026-10-26）/13 名 | 3/13 同 |

> 结论性读数：R3/R4/R5 证会师席红-①指认属实——面外活引用体量大于面内；v1 申报数（26/15）按会师裁语**作废为本表 R1/R2 口径化重出值**。check-pointers 缺省不扫 `.collab`（L68 裁-23 排除）＝断链无声面，由 E-ARC-1′ 自带扫描补偿。

## B.3 定标结论＝③分族处置（主结论不变·判据重写）

1. **永不归档/永不删除族**：`.collab/decisions/` 全部三族＋verdicts.md——史实锚＋spec 出处，任何批不得删；永存断言由 **E-ARC-3′ 逐名清单对账**承载（红-②整改，见下）。
2. **docs 族**：不归档——被取代即出 docs，历史态归 git 历史（「归 .collab 或归档」中归档一支定标＝git 历史＋tag，不建物理面）。
3. **票面族＝收口后条件式移除**（E-ARC-1′ 重写·红-①整改）：
   - **扫描面定标＝全文本域扫描案**（二选一中弃豁免清单案；理由＝豁免清单需人肉维护且本仓断链先例族皆生于「扫描面小于引用面」，全式扫描零维护成本、体量实测可承受）。E-ARC-1′ 全文见下。
   - **裸基名引用族入口径**：除全路径串外，同查该票 ID 裸基名 token 族（R3 正则同款按票 ID 实例化）。
   - **「先换锚」程序覆盖全部活引用族**：receipts／qa／design／dispatch／docs／仓根 README／deliverables（含 spec_file 头块）——任一引用族命中即触发换锚批先行：引用方逐处改指（改指目标＝该票收口终态件／回执／会师登记件），换锚批完成后方可进移除批。
   - **Y-7 定性修正**：check-collab-lint 三处 spec_file 锚 EAC-SK5 机检票＝拍板㊺判据下**违例存量**（该票自身即闭环件形态），定标＝**闭环化换锚先行**（EAC-CLN 先例同类：违例存量以换锚闭环处置，不冻结不豁免）；v1「实质不可删」判定**删除**——不存在不可删的票，只存在「换锚未先行」的票。
   - **QA 硬线（保留·写死）**：E-ARC-1′ 判据修好并跑绿之前，**票面族移除一律不得启动**（含单票试点）。
   - 移除程序不变：票首行 `已结案` 标记→单独 commit `retire:`＋消息含 `RETIRE <票ID>`＋批尾 tag `archive-<YYYYMMDD>`；寻回行写票目录 README：`git log --diff-filter=D --grep "RETIRE <票ID>"` → `git show <笔>^:<旧路径>`。
4. **出口条件**：仓外归档（2026-10-27 先例）＝过程大块唯一出口（不变）。

## B.4 可机械判定条款草案（v2 定稿）

```
E-ARC-1′ 移除资格判据（红-①重写·负例 exit≠0）：
  输入＝待移除票路径 P 与其票 ID T；
  (a) 全路径族：grep -rno --include='*.md' --include='*.py' --include='*.json' --include='*.sh' --include='*.txt'
      "$P" .  排除 P 自身与 `.git/` → occurrence 必＝0；
  (b) 裸基名族：grep -rno --include=… "$T" .（同款排除）→ 活引用 occurrence 必＝0
      （史述/沿革句豁免＝逐处人工分账后写入该票 RETIRE commit 消息体，机械侧仍须 0，
       分账放行发生在换锚批回执，不在判据内开口子）；
  (c) spec_file 族：grep -rn "spec_file: $P" deliverables/ tools/ → 必＝0
      （命中＝违例存量先走闭环化换锚批，Y-7）；
  任一非 0 → 移除被拒（exit 1）＋逐处清单入回执。
  门禁侧补偿：本判据自带全仓 grep，不依赖 check-pointers 缺省扫描域（裁-23 排除面不影响）。
E-ARC-2 移除笔三要素（不变）：`retire:` 前缀＋消息含 `RETIRE <T>`＋批尾 tag `archive-*`；
  git log --grep 与 git tag 双查缺项 exit 1。
E-ARC-3′ 史实锚永存＝decisions 逐名清单对账（红-②重写·与 E-ADR-5′ 并件）：
  撤销 v1「GATE PASS＝永存等价断言」主张（实测 R7：spec 锚仅覆盖 decisions 13 名中 3 名，
  verdicts 与十件现行裁定零锚）。
  新式：基线清单件 `.collab/decisions/` 逐名＝`git -c core.quotepath=false ls-files .collab/decisions/`
  快照入回执；校验＝清单逐名 `test -f` 全存在（缺名 exit 1）＋三族分桶和＝总数
  （E-ADR-5′ 同式）＋任何 commit diff 中出现 `D .collab/decisions/` 行＝BLOCK
  （git show --name-status 过滤·零新构件）。
```

---

# T-C · 组件退役规则

## C.1 业界对照（Y-6 更正后）

- **SemVer 退役双拍程序**：deprecation 属正常演化——**FAQ 款**：「当你弃用公共 API 的一部分时，更新文档并以携带弃用标记的 **minor** 版本发布；在后续 **major** 移除之前，应至少有一个携带弃用标记的 minor 版本发布」（v1 误挂 §7＝MAJOR 递增条款，本版改挂 FAQ；§7 仅补注「marked as deprecated → minor MUST increment」为正文旁证）。〔来源：Semantic Versioning 2.0.0 **FAQ**／2026-11-03 检索／FAQ "How should I handle deprecations…"／https://www.semver.org/；正文旁证 §7／同 URL；解读件 safeguard／§The rule／https://safeguard.sh/resources/blog/how-should-a-library-deprecate-an-api-what-semver-says〕
- **弃用通知五要素**：对象名／原因／替代物及示例／弃用发生版本＋计划移除版本／changelog 独立类目。〔safeguard／§"What a good deprecation notice contains"／https://safeguard.sh/resources/blog/deprecate-then-remove-how-to-retire-an-insecure-api-under-semver〕
- **两信号分立与审计两半**：Deprecation（在走）vs Sunset（何时停·RFC 9745/8594）；「deprecation nobody notices is no deprecation」；移除前静态 grep＋运行时观察找齐调用方。〔WSO2／§Set a Clear Deprecation Timeline／https://wso2.com/api-platform/learn/api-versioning-best-practices/；chagdev／§Audit 两半／https://chagdev.com/?p=736〕

## C.2 本仓采纳口径＝退役手续最小闭集（五目·不变）

1. 弃用宣告先行（五要素·宣告批与移除批至少隔一个可写批次；紧急安全族除外＝fail-closed 即拆＋宣告补记）。
2. 版本账 append-only 追加行（含「退役：<对象> 依 <裁定/票ID>」）。
3. 注册/配置面**同批**随动清零。
4. 物理移除＋引用清零断言。
5. bump 三同源＋GATE 对拍。

## C.3 T07 旧五卡退役复核（结论不变）

5/5 齐备；唯第 3 目 hooks-map `agent_type_to_seat` 五行旧卡名跨批残留（T07 拆 T08）——按「并批视同同批／或 T07 回执登记残留窗口＋T08 回执核销」闭环，不需改票（现盘实测旧五卡未删、version 0.1.14＝T07 未施工，缺口未成真）。

## C.4 条款草案（v2 定稿·Y-4 词形对齐）

```
E-RET-1′ 退役手续四查（词形闭集对齐）：对每个退役对象——
  词形闭集 W = 「退役[：:]」 ∪ 「物理清退」 ∪ 「清退」（先例词族·实测现盘
    「退役：」=7 处（.collab+deliverables）、「物理清退」=6 处（tickets）→
    上线首日不误判 T07 系先例）；
  (a) 宣告件存在：grep -rEo "$W" .collab/decisions/ .collab/tickets/ 命中对象名；
  (b) 版本账行存在：README grep "$W" 命中对象名（与 (a) 同词形集，不再单挂「退役：」）；
  (c) 旧路径族引用清零：活面 grep occurrence==0（口径同 E-ARC-1′ (a)(b)）；
  (d) version bump 读数三同源。
  任一缺→未完备读数入回执（advisory 起步，转 BLOCK 属门禁路由表裁量）。
```

---

## 呈报节（v2 收敛后·仅备案非候裁）

- 固定结构闭集保守兼容选择不变（ADR 同桶文件名分族；若固定结构终名录含 adr 子桶只换落位语句）。
- R1/R3 口径差异登记：会师席复跑数与本版重出数因正则宽窄不同存在差值，均已双侧标注——判据落施工票时**以 E-ARC-1′ 全式为准**，申报账只作体量证据不作判据基线。

## 四、引用账（四件套·Y-6 更正标注）

| # | 来源文件 | 日期 | 条款位置 | URL |
|---|---|---|---|---|
| 1 | Architecture Decision Records (ADR) Explained: A Complete Guide | 2026-11-03 检索 | §Status Lifecycle／§Common Mistakes（accepted immutable）／§Where to Store | https://vickybytes.com/blog/architecture-decision-records-explained |
| 2 | MADR 模板实战指南 | 2026-11-03 检索 | §元数据头 Status 闭集／§八 supersession 双向流程 | https://blog.csdn.net/gitblog_00602/article/details/161209131 |
| 3 | Architecture Decision Records Written by Your Coding Agent | 2026-11-03 检索 | §What an ADR is（Nygard 2011·编号不复用·superseded 留档） | https://nimbalyst.com/blog/architecture-decision-records-written-by-your-coding-agent |
| 4 | ADR glossary — Lockstep | 2026-11-03 检索 | §The standard format（superseded never deleted） | https://www.getlockstep.dev/glossary/adr |
| 5 | Delete unused source code… or keep an archive folder? — SE | 2026-11-03 检索 | 问题正文＋Owens 答（delete+tag）＋Velasquez 答（archive 断链） | https://softwareengineering.stackexchange.com/questions/289904/delete-unused-source-code-from-the-repository-or-keep-an-archive-folder |
| 6 | Don't Delete, Archive… — DEV Community | 2026-11-03 检索 | §Code Graveyard＋§Lessons Learned | https://dev.to/masaoshimadaopen/dont-delete-archive-how-i-safely-retired-zombie-code-with-git-mv-and-archive-53a0 |
| 7 | Semantic Versioning 2.0.0 | 2026-11-03 检索 | **FAQ（deprecation→minor＋移除前至少一携带弃用的 minor）＝主挂**；§7 正文＝旁证（v1 误挂已正） | https://www.semver.org/ |
| 8 | How should a library deprecate an API? — Safeguard | 2026-11-03 检索 | §The rule＋§deprecation notice 五要素 | https://safeguard.sh/resources/blog/how-should-a-library-deprecate-an-api-what-semver-says |
| 9 | API Versioning Best Practices — WSO2 | 2026-11-03 检索 | §Deprecation Timeline（RFC 9745/8594） | https://wso2.com/api-platform/learn/api-versioning-best-practices/ |
| 10 | Sunset Banners Beat Surprise Breakage | 2026-11-03 检索 | §Audit 两半（静态＋运行时） | https://chagdev.com/?p=736 |

## 五、回执（v2 起草笔）

- 开端 HEAD 实测＝`bce8ff4`；本笔单独 commit（`collab:` 前缀·只含声明闭集 1 件）；禁 `--no-verify`、禁 amend；门禁拦截如实报告不绕闸。
- v1（`a136630`）不改不删，作史述；本 v2 生效后为定标真源。
- 三题结论一句话（不变＋判据升级）：T-A＝decisions 桶三族分权＋Nygard 状态行＋supersede 双向（E-ADR-1..5′ 补齐双向图与适用域）＋SOP 裁决落地闭环＋权限数据面补两行点名；T-B＝不建归档面、git 历史＋retire commit＋tag 承载、分族移除资格——**E-ARC-1′ 全文本域扫描＋裸基名口径＋全族换锚先行＋修好前票面族移除禁启动（QA 硬线）**、E-ARC-3′ 逐名清单对账替代 GATE PASS 等价主张；T-C＝五目闭集＋E-RET-1′ 词形闭集对齐先例词族，T07 复核 5/5 齐备唯跨批残留一项两笔闭环。
