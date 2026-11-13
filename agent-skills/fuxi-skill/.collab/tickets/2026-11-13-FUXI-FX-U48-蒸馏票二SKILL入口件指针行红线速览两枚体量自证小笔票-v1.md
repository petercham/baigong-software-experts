# FUXI-FX-U48 · 蒸馏票二＝SKILL.md 入口指针与体例面小笔票（红线速览 append 两枚指针行＋修订注记一行＝纯增三行·指 EG-6 节条款系不指行号·体量红线 ≤200 行自证·票三不开与 E10/H-2 零预开登记）｜v1

> 票号＝FX-U48（编号续位现盘自查＝agent-skills/fuxi-skill/.collab/tickets/ 枚枚举现读最大＝FX-U47 无 U48 存量＋tickets＋receipts 内容 grep `FX-U48` 零命中＝续位坐实）｜起草＝架构席（arch-fuxi-u48）｜日期＝2026-11-13｜被派＝**工程师席**（交付面单一工程师席串行·SKILL.md 纯增三行一笔＋工程师回执一笔＝施工段封顶两笔）；本席只出票面零碰 SKILL.md／contracts/／gates/ 真源＝纯规格零施工红线写死（SKILL.md 改动归放行后工程师席施工）。
> 排程依据（已放行在册·票面禁候裁）：FX-U47 收口登记件 `agent-skills/fuxi-skill/.collab/decisions/2026-11-13-FX-U47收口登记-补研自驱蒸馏上约闭环.md`（在册：EG-6 契约白纸现含补研执行工序八子款＝L99-106；随动口径白纸＝票二随验收通过即刻起链·架构席 fresh 真席型）；票二定义真源＝蒸馏提案 §四-2 `agent-skills/fuxi-skill/.collab/design/2026-11-12-FUXI-补研自驱工序蒸馏提案-v1.md`（「票二＝入口指针与体例面（小笔·可与票一分开）：SKILL.md 工序主线表/红线速览落指针行（指契约新增条款系）＋候裁报告件要件若 H 面落 SKILL.md 侧的指针装配。非契约面，体量红线 ≤200 行自证」逐字在册）；承 FX-U47 票面 §四-5「票二 SKILL.md 指针面＝随票一落地后起」。
> 开工锚照登（起草席 2026-11-13 当轮实测）：开工 HEAD＝`ae6c530a5f7c47767807018549ff7455b7f35d99`（全 sha＝FX-U47 收口登记笔＝链顶·与派工实测报同轮坐实）；`git status --porcelain | grep -v '^??'` 读数＝恰两枚＝agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl 与 share/check-pointers.py（他案在飞脏面·照登零碰严禁带入）；untracked 面照登零带入。工程师席开工 ANCHOR＝开工当轮 HEAD 实测（应为含本票起草笔或其后续合法放行笔的链顶）·照登；ANCHOR 不符＝停手上报，禁带差开工。
> 开工前置对账（读数当轮实读相符方可动笔·**改动面起点 blob 必对开工基线当轮现算，禁沿用本票面抄录值——U34 教训面自践**）：①改动面起点 blob＝agent-skills/fuxi-skill/SKILL.md 对开工基线 `git ls-tree` 现算入回执（起草回填值对 `ae6c530` 现算见 §一 表＝参考位）；②禁动对钉十八枚 blob 对开工基线现算回填 §一；③门禁基线（起草当轮实跑在册 §〇-5）＝assert-tool 汇总 `PASS=27 FAIL=0 PENDING_STAGE=0 总数=27` exit 0＋FC-2 读数行「注册表 41 字段·双向 diff=∅·实例⊆注册·FM条目纪律·值互洽全等」＋BW-3 读数行「产物正文实跑命中=0（扫描 90 件·实扫描判绿）」＋GS-5 读数行「断言基数27」；④check-ticket-pins --selftest＝用例 5／反常 0 exit 0（起草当轮实跑）；⑤SKILL.md 现面形制现跑在册 §〇-2（行数 41＋四 H2 节＋两契约锚行 L31 唯一命中＋blob 与 FX-U47 票禁动对钉回填值全等＝契约批窗口内 SKILL.md 零漂移）。开工读数不符＝停手上报，禁带差开工。
> 账权＝FUXI 项目：本票落 FUXI 账域 tickets 桶；起草回执与工程师回执落 FUXI 账域 receipts 桶（裸文写·A 条款）。
> 钉形态注（本票 pins＝新行入位钉·三钉写死 §二·全部 V0=0/V1=1 形态）：一围栏＝S1 三行逐字围栏；三钉各为 S1 围栏行内逐字子串（钉1＝款A行头串＝「条款系」词形紧邻全角左括号形态、钉2＝款B行头串＝「要件」词形紧邻全角左括号形态、钉3＝款C行头串＝v2.1 全角括注注记头形态·禁同构简写引用＝钉语逐字只落钉块与归属围栏）；三钉钉语对开工基线 `ae6c530` 现跑 B＝0（§〇-6）、归属围栏内各恰一行 A＝1、无替换旧行 D＝0→钉值 0/1 公式自洽（V0*=B／V1*=B+A−D）；插入与 append 均无替换旧行＝全部旧行号段「-」。围栏外正文零逐字钉语连续串（防自染自查＝钉语完整串只落钉块与归属围栏，本注与 §〇-6 只述形态计数不落逐字串；起草轮 pins 预跑读数 §六在册）。工程师开工对三钉对开工基线逐枚复算 V0 相符方可动笔＝D-92；现算与表钉不符＝H-0 停笔呈裁禁凑绿。
> H-0 案型防再现（照 U41/U42/U43/U47 派工三条）：落地面＝SKILL.md 居 OA-T1 扫描域（agent-*/**）——S1 三行成文形态＝款C 注记头日期段与票号段置全角括注内（「v2.1（2026-11-13·…·FX-U48）」＝豁免③口径·U40 H-0 勘正笔 `2098fe9` 定形＋v18/v19 注记头先例在契约与目录面通过 check-entity 归零实证）；款A/款B 零日期零票号零裸率形；成文形态构造物 check-entity date/discipline-no/ticket-no 谓词归零对拍＋裸形态活性对照探针读数在册 §〇-7；票面自身居 .collab/tickets＝check-entity 扫描面剪枝不咬（U41 §〇-6 在册）。工程师落笔前对追加稿构造物跑 check-entity date 计数 0 读数先行入回执。时戳占位符写死 `%ct`（`%cT` 非法占位符禁复用）。
> BW-3 避自咬措辞纪律（写死·对票面全部文本与 S1 围栏成文适用）：SKILL.md 不在 BW-3 产物级扫描面（入口主件非产物正文）但成文仍自守同规（U47 同款口径）——S1 三行内「占比／计数」词形零裸率形（条款名引用＝契约条款头逐字，承契约白纸措辞系零嵌值）；本票零数值门槛新增（既值 70／80／5／3／4/5／[0.75,0.90] 零触碰零重述入新行；唯一行数值＝体量自证 41→44 与 ≤200，属体量红线既有白纸值）。收口靶检＝assert BW-3 读数行 PASS 零扰动（§三-4）。
> 指针纪律注（A 条款自我适用·写死）：本票面一切背引号路径＝仓根起始完整路径且落笔时点目标已在盘实点（tickets／decisions／contracts／gates／design／receipts／share 逐路径实查在册）；尚未生成件（本席回执／工程师改动面／工程师回执）一律裸文写（无背引用）。指针行本体指针目标＝契约节级引用（EG-6 节内条款白纸／EG-6 报告件要件条款）＝指节不指行号防漂移，体例承工序主线表①②③行真源指针先例（agent-skills/fuxi-skill/SKILL.md L20-22 在册形制）。落笔后对本票面跑 check-pointers --target 必 exit 0 零 BLOCK＝写死判据（§三-7）。登记类文书路径逐件全写禁 brace 简写（R-13 方法线索在册·自遵）。
> D-95 分段落笔硬条款（链面封顶自算·派工要件）：起草段＝**票面一笔封顶＋回执一笔＝两笔封顶**（本票面＝起草笔一·回执另笔落 receipts 桶）；施工段（工程师·随放行）＝**改动笔一笔（SKILL.md 单面·声明闭集单面）＋工程师回执一笔＝两笔封顶**；本票链封顶＝起草二＋施工二＝四笔封顶自算坐实（QA 判词／收口登记随 §五 收口链另段不预占）；**每笔 pathspec 限定 add 与 commit 紧邻无窗口·FX_COMMIT_DECLARE 声明本笔面＝纯路径清单形态（承 FX-U32 闸形·声明含描述文字被自家闸咬案型在册）**；禁 git add -A、禁 amend、禁裸 git commit；message 零 at 符号字符（用「at 符号」字样）；commit 带 ≥7 分钟 timeout 且输出重定向落盘仓根 .scratch/FX-U48-draft/ 或 .scratch/FX-U48-build/ 防强杀；查 config 一律旗在前只读语法；资源不足先 commit 已完成面再回报现状，禁裸退；零落账回报无效。
> 并发防护（D-58 案型随带）：pathspec add 与 commit 两端齐带紧邻无窗口（提交闸 fail-closed 无声明 BLOCK exit1＝设计如此禁 BYPASS）；**add 后紧邻 commit 缩短共享 index 窗口（D-58 教训·本批写死）**；落笔前后 git diff --cached --name-only 两读并排入回执，差集恰本笔面；撞 index.lock 或 cannot lock ref＝有界等待一轮即呈报主理人（零删锁零二次重试）。他案在飞面点名＝ledger.jsonl 与 share/check-pointers.py 两枚脏面零碰零带入；链上他案笔照登不归因。
> 取证面纪律（D-94＋R-10）：起草段取证／H-0 对拍／scratch 装配预演物全部落仓根 `.scratch/FX-U48-draft/` 不 commit；本票零取证新物入链。

---

## 〇、复核结论（架构席 2026-11-13 对 `ae6c530` 实读实跑实查，票内定稿依据）

1. **链顶与票号与在册性（读数一）**：开工 HEAD＝`ae6c530`（全 sha ae6c530a5f7c47767807018549ff7455b7f35d99）＝FX-U47 收口登记笔＝链顶；收口登记件 blob `8a22e4b7c3f9b33491d9bbf233cfa09d1d2bf6b7` 在盘在册（对开工基线 `git ls-tree` 现算）；tickets 桶枚枚举现读最大＝FX-U47、U48 枚枚举零命中＋tickets＋receipts 内容 grep `FX-U48` 零命中＝票号续位坐实＋新建 v1 案型；蒸馏提案 rev 面 blob `ba8d0e85244b63ad34f42b6fcf024ffb843fdfa8` 对开工基线现算与提案自载值全等＝票二定义承接源只读对钉在册；FX-U47 票面现册 blob `8ab55e74b57c304c0eed05925d45f7c23f516974`（含 §七 rev 勘正与黄新-1 登记段＝现值）在册。
2. **SKILL.md 现面形制现跑（落点坐实）**：`agent-skills/fuxi-skill/SKILL.md` 对开工基线现跑——行数 `wc -l`＝**41**（体量红线 ≤200 现基线＝前后差判据基面）；H2 节头四枚（工序主线表 L16／轨界与红线速览 L27／references 索引 L35／修订注记 L39）；工序主线表①②③行指针先例 L20-22 在册；红线速览两契约行＝L31（起串「证据分级／失败模式两契约」现跑 `grep -cF` ≡ **1** 命中＝唯一锚坐实）；修订注记段 v2.0 行＝L41＝现盘末行（起串「v2.0（入口件换代批）」唯一命中）；SKILL.md blob `a97f6e20c6e57ed692ab9a68d840830e49ef6c85` 对开工基线现算＝与 FX-U47 票禁动对钉回填值全等＝契约批窗口内 SKILL.md 零漂移。
3. **落位坐实（红线速览插两行＋文件尾 append 一行）**：款A/款B 落位＝现盘 L31 两契约行之后（新 L32/L33）；款C 落位＝现盘末行 L41 之后文件尾追加（新 L44）。落位形制论证＝提案 §四-2 白纸「工序主线表/红线速览落指针行」二选一授权＋黄-3 勘正判界「工序①②③执行条款白纸已在册·adapters 三件真源指针 L20-22 在册」＝主线表六步链骨架零触；补研工序＝EG-6 触发的执行分支非第七步＝指针挂红线速览两契约行下＝语义邻接位（设计自决·理由随 v2.1 注记行自载）；中间插入非文件尾 append 的「纯增」机械语义＝numstat 删除列 0＋difflib 零 delete/replace opcode＝既有行全体逐字存续（§三-1）。
4. **指针目标在场性现跑（指节不指行号）**：契约 EG-6 八子款条款头串八枚对 `agent-skills/fuxi-skill/contracts/evidence-grading.md` 收口现面 `grep -cF` 各 ≡ **1**（§〇-8 同读数·契约 106 行白纸在册）＝款A 指针目标八子款名逐一可在契约命中；款B 指针目标「暂缓入池报告件要件条款」＝契约 L104 在册条款头（款项引用形态）；契约现面 blob `c40e5010a018bd4051cc45b28a1c15ed78b76962` 对开工基线现算在册（禁动对钉）。
5. **门禁基线现跑（起草当轮·收口零扰动判据基面）**：assert-tool 汇总 `PASS=27 FAIL=0 PENDING_STAGE=0 总数=27` exit 0＋FC-2 读数行「注册表 **41** 字段·双向 diff=∅·实例⊆注册·FM条目纪律·值互洽全等」＋BW-3 读数行「产物正文实跑命中=0（扫描 90 件·实扫描判绿）」＋GS-5 读数行「层名11·白名单6+6·断言基数27·机械层名两白名单在场·层名声明↔代码 diff=∅（只增不减）」；check-ticket-pins --selftest＝用例 5／反常 0 exit 0＝**本票零断言零代码施工＝gates 全域禁动（§一）**＝上述读数收口必与开工全等＝§三-4 机械证明面。
6. **钉语 B 值现跑（pins 自洽基面）**：三钉钉语对开工基线逐枚 `grep -cF` 现跑＝**各 0**（对 agent-skills/fuxi-skill/SKILL.md 现面）；钉语完整串不落本票正文防自染＝§头钉形态注写死（§三判据以「三枚指针行头串＝钉块针语」指代不复打）；起草轮 pins 预跑读数 §六在册。
7. **H-0 案型对拍先跑（构造物居 .scratch/FX-U48-draft/ 不 commit）**：对拍构造两探针——①成文形态探针（S1 三行逐字取入基线副本装配现跑件复制，落位 .scratch/FX-U48-draft/h0probe/agent-skills/probe-fx-u48/）现跑 `python share/check-entity.py --root .scratch/FX-U48-draft/h0probe`＝`pattern=date count=0`／`pattern=drive-path count=0`／`pattern=discipline-no count=0`／`pattern=ticket-no count=0` exit 0＝**成文形态归零坐实**（款C 全角括注豁免③口径经实跑实证）；②谓词活性对照探针（裸日期段对照件落位 .scratch/FX-U48-draft/h0probe-bare/）现跑＝`pattern=date count=1`＋BLOCK exit 1＝date 谓词对落地面形态活体在册＝①的归零非空跑坐实；票面自身居 .collab＝扫描剪枝不咬（覆盖不对称案型承 U40 六-R3 在册）。
8. **scratch 装配预演（起草轮·.scratch/FX-U48-draft/ 不 commit）**：票面 S1 三行逐字取入基线副本装配现跑＝SKILL.md diff **+3/-0**（插入两行＋尾 append 一行·既有行零改动）＋行数 **41→44**＋difflib deleted_chars **0**（delete/replace opcode 零）＋三枚指针行头串对拟后面各 **1**／对基线各 **0**＋体量红线 44 ≤ 200＝§三-1/-2 判据可机械跑坐实；装配后构造物 check-entity 四谓词 **count=0** exit 0（＝§〇-7 探针①同源件）。
9. **工序参照通读申报**：票面体例承 FX-U47 全册通读在册（`agent-skills/fuxi-skill/.collab/tickets/2026-11-13-FUXI-FX-U47-蒸馏票一EG6补研执行工序八子条款契约原子笔票-v1.md`）；入口件指针先例＝SKILL.md ①②③行＋红线速览既有五行形制现读在册；契约承接面＝EG-6 节尾八子款现面（L99-106）现读在册；本票条款面零新口径＝两枚指针行全部所指＝契约白纸既文（FX-U47 已上约），入口件零复写细则（真源指针制存续）。
10. **指针行路径形制设计注（编排自决留痕·工程师禁改形）**：S1 款A/款B 反引号路径＝仓根起始全路径形制（`agent-skills/fuxi-skill/contracts/evidence-grading.md`），与 SKILL.md 既有行短式形制（contracts/evidence-grading.md＝包内跨目录引用·resolve 候选层四在包内语境解析通过）不同形同指向。择全路径理由两条：①A 条款指针纪律自我适用＝本票面一切背引号路径＝仓根起始完整路径（票面内短式 token 因 .scratch 历史副本后缀多义被 OA-D6 后缀唯一命中层判悬空＝起草轮初跑 BLOCK 2 枚实测在册 §六，全路径形制复跑 exit 0）；②S1 围栏逐字入落地面＝票面可核与落地面可核同形制零歧义。落地面校验两证在册：真面 SKILL.md 基线 check-pointers exit 0（现跑）；fake-tree 装配件（.scratch/FX-U48-draft/faketre/ 完整包副本置入 S1 三行）check-pointers exit 0（＝§三-5 改后 SKILL.md 靶检判据可机械跑坐实；裸拷贝无同目录件形态的 BLOCK 系预演移动件自有形态噪声，与落地面无关）。§三-5 收口靶检值以真面施工件为准。

---

## 一、声明闭集（git 面·起草段两笔封顶 2 面·施工段封顶两笔两面）

1. agent-skills/fuxi-skill/.collab/tickets/2026-11-13-FUXI-FX-U48-蒸馏票二SKILL入口件指针行红线速览两枚体量自证小笔票-v1.md（本票面·起草席一笔·add/commit 恰本面）
2. receipts 桶内「2026-11-13-FUXI-U48起草回执-v1」件（起草席回执·另笔·裸文写·A 条款）
3. agent-skills/fuxi-skill/SKILL.md（改·施工改动笔·§二 S1 fenced 逐字照录＝红线速览段 L31 后插两行＋文件尾 append 一行＝纯增三行·既有行零字节）
4. receipts 桶内工程师回执件（施工段另笔·裸文写·A 条款·落链后补入本闭集随回执申报＝先例口径承 U43/U47 §一）

改动面起点 blob 表（一枚被改实体·对起草 ANCHOR `ae6c530` 现算回填＝参考位；工程师开工对开工基线当轮现算对账，不符＝按放行票射程核因登记呈报＝H-0 停笔呈裁·禁凑绿禁回改·U34 教训面自践）：

    agent-skills/fuxi-skill/SKILL.md    a97f6e20c6e57ed692ab9a68d840830e49ef6c85（被改实体＝红线速览段插两行＋文件尾 append 一行·其余全部零字节）

禁动对钉表（十八枚·对起草 ANCHOR `ae6c530` `git ls-tree` 现算回填＝参考位；工程师开工对开工基线当轮现算对账）：

    agent-skills/fuxi-skill/contracts/evidence-grading.md      c40e5010a018bd4051cc45b28a1c15ed78b76962（禁动对钉＝契约白纸 FX-U47 已上约·本票零字节）
    agent-skills/fuxi-skill/contracts/failure-modes.md         b16fc79d417d4035b7c42d446302c55eb762ca80（禁动对钉）
    agent-skills/fuxi-skill/contracts/artifact-contract.md     35f5b456906dcec6a8fd43fff4b1be8eae5c6a2d（禁动对钉）
    agent-skills/fuxi-skill/gates/assertion-catalog.md         acfae11640f7d8dae07901869a01de3d5ad9a018（禁动对钉＝零断言零注记施工＝票三未开注记零随动）
    agent-skills/fuxi-skill/gates/assert-tool.py               dfc1fd47ce1ca394808e03c29e9887c4fe17fde3（禁动对钉＝零机器断言施工·assert 基数 27 不动收口必全等）
    agent-skills/fuxi-skill/gates/check-ticket-pins.py         3cc80e61b41cbf5db7eb0d949545607b7ccd401d（禁动对钉）
    agent-skills/fuxi-skill/adapters/classifier.md             23c72e8e1fd9e6d09032ff3906b2ff23e7930631（禁动对钉＝adapters 三件禁动①）
    agent-skills/fuxi-skill/adapters/person.md                 c5d5cff6e2793ca0ef5eaf4d7142abbaa59e0682（禁动对钉＝adapters 三件禁动②）
    agent-skills/fuxi-skill/adapters/method.md                 587b75d609f0786ad32f85392c8d0fdf22399dec（禁动对钉＝adapters 三件禁动③）
    agent-skills/fuxi-skill/specs/perspective-spec.md          3a9d9a9d162a9814fff5d8995d893d5e86f4c9e3（禁动对钉＝specs 域零碰）
    agent-skills/fuxi-skill/specs/technique-spec.md            e852bff1b8054c299e7b8cec8550c9489d160a68（禁动对钉＝specs 域零碰）
    agent-skills/fuxi-skill/README.md                          bcd875c5a7a83a345d0b820b501d85c1f2b00213（禁动对钉＝README 旧值另票在册·本票零碰）
    agent-skills/fuxi-skill/.collab/decisions/2026-11-13-FX-U47收口登记-补研自驱蒸馏上约闭环.md  8a22e4b7c3f9b33491d9bbf233cfa09d1d2bf6b7（禁动对钉＝排程依据在册件＝史证零回改）
    agent-skills/fuxi-skill/.collab/design/2026-11-12-FUXI-补研自驱工序蒸馏提案-v1.md  ba8d0e85244b63ad34f42b6fcf024ffb843fdfa8（禁动对钉＝口径件与提案 design 面禁动）
    agent-skills/fuxi-skill/.collab/tickets/2026-11-13-FUXI-FX-U47-蒸馏票一EG6补研执行工序八子条款契约原子笔票-v1.md  8ab55e74b57c304c0eed05925d45f7c23f516974（只读对钉＝票面体例先例承件·史账零回改）
    .collab/decisions/2026-11-13-皮总裁定-FUXI蒸馏票一放行＋H1H2采纳建议.md  59d75a2f586fe1d2139ae5d979d7d673cefe3bf6（禁动对钉＝上游裁定誊录件＝史证零回改）
    share/check-pointers.py                                    1e6b9b710739cfc5a8cb9a23b658f80b4fa8c864（禁动对钉＝HEAD 基线值；该件工作面他案在飞脏＝照登零碰·对账一律 `git ls-tree HEAD` 面）
    share/check-staged-declaration.py                          04f2889f21a3684511d9a74d2ca22e0998409ed1（禁动对钉）
    share/run-gates.sh                                         3e442001b68d3478e2a0d8177632a51909abe57d（禁动对钉）

（语料面禁动点名＝agent-skills/fuxi-skill/.collab/evidence/ 全域不入 git＝文件面零碰口径承 U38/U41 在册注；本票零取证新物＝指针行落点材料＝契约现面＋提案 §四-2。）

禁动面点名＋零碰清单（写死）：上表禁动对钉与只读对钉全部＝本票禁动面＋**contracts/ 全域零字节（契约白纸 FX-U47 已收口＝本票非契约面·提案 §四-2 白纸）**＋**gates/ 全域零字节（assert-tool.py／assertion-catalog.md／check-ticket-pins.py＝零断言零注记＝票三不开在册）**＋**adapters/ 三件（classifier／person／method）零字节**＋specs/ 全域零字节＋products/ 全域零字节（含全部 registration 随件＝已验登记面与补课批登记面禁动）＋rejected/／active 面零字节＋decisions 桶全部裁定誊录件与登记件＋U36-U47 链面（含蒸馏票一票面与回执与收口登记）＋蒸馏提案 design 面与口径件面零字节＋receipts／research／audits／qa／defects 桶全部在案件零字节＋SWB 线面／SEMGV／SCRATCHG／A14 他案面＋share/ 全域＋agent-experts/ 全域（含 ledger 他案脏面零碰零带入）＋softwares/＋仓根 .collab/ 全域（本票被引裁定件只读）＋仓根 .scratch/ 全部既有面零碰＋链上他案笔照登不归因＋宿主装载面／仓外零写入。

---

## 二、施工规格（fenced＝唯一文字来源逐字成文·工程师照录·本席零施工·排程已放行零开放措辞）

**gates 随动面段落（写死）**：本批**零断言零代码零注记施工**——assert-tool.py 判据臂零增（GS-5 断言基数 27 不动）／assertion-catalog.md 断言条目与修订注记段零字节（本批入口件指针笔无契约面改动＝目录注记无的放矢＝票三不开在册）／FC-2 注册表 41 字段零扰动／BW-3 管辖零随注（产物级扫描面零扩·本批无产物正文改动）。收口判据证明基数不动＝§三-4 现跑四读数与开工基线 §〇-5 全等＝机械证明面。候选机器断言族（域名去重／log 序／在场对盘／请求复算／六节结构）＝零采纳零启动（FX-U47 收口登记白纸「票三零采纳不开」在册·§四-1）。

**S1 · agent-skills/fuxi-skill/SKILL.md（改·恰三行纯增＝红线速览段现 L31 两契约行之后插入款A、款B 两行＋文件尾现末行 L41 之后 append 款C 一行·既有三十八行零字节）**

```text
S1 施工面＝三行纯增·逐字照录（一行成文·行从其自身首字符起＝缩进不入行；行序＝款A→款B（插于现盘 L31 起串「证据分级／失败模式两契约」行之后，§〇-3 锚行现跑唯一命中）；款C 追加于现盘末行起串「v2.0（入口件换代批）」行之后＝文件尾）：

- 补研自驱执行条款系（补充调研触发后的自驱执行工序四段闭集与配套登记条款系＝八子款〔补研执行工序总则／换路径攻站序列／阻断形态如实登记／对照臂收获登记操作／补批封印体例增补／暂缓入池报告件要件／请求计数台账口径／低信息量对象确认轮短路由〕）＝`agent-skills/fuxi-skill/contracts/evidence-grading.md` EG-6 节内条款白纸（补研自驱蒸馏批上约在册）——细则归契约，本件只指不搬。
- 暂缓入池候裁报告件要件（装配条件＝仅确认轮零获态触发＋件体四节闭集＋报告件不自裁）＝`agent-skills/fuxi-skill/contracts/evidence-grading.md` EG-6 暂缓入池报告件要件条款指针。
- v2.1（2026-11-13·入口件指针行小笔批·FX-U48）：红线速览段增两枚指针行（补研自驱执行条款系／暂缓入池候裁报告件要件），均指 EG-6 节内契约新增条款系＝补研自驱蒸馏批八子款白纸在册；工序主线表六步链骨架零触＝补研工序指针挂红线速览两契约行下（补研非第六步，属 EG-6 触发的执行分支）；真源指针制存续＝入口件零复写细则；体量红线 ≤200 行自证＝收口 44 行。

零碰随注（写死·禁顺手扩面）：SKILL.md 既有三十八行全部零字节（frontmatter 六行零动·定位／旧物／防误用三段零动·工序主线表六步链含①②③行先例指针列零动·红线速览既有五行零动（含两契约行本体＝插行锚位不改其字）·references 索引节零动·修订注记 v2.0 行零动）；指针行零复写契约细则＝只指节不指行号（防漂移·体例承①②③行先例）；零新增节头（H2 节头计数收口必 ≡4）；零触 description／version 字段之外面——frontmatter `version: 2.0` 值零动（版本线归 README 同源另票口径＝本票零扩面·修订注记 v2.1 行＝注记段行不触 frontmatter）。照录缩进格式纪律＝票面展示块内行照录时缩进不入行＝目标文件行从其自身首字符起（SKILL.md 现盘红线速览行无前置空格＝照抄缩进入行即 diff 落位判据面自红）。
```

**本票钉值块（机器可读·V0*=B／V1*=B+A−D·起草席对基线 `ae6c530` 现算回填·实跑预演在册 §六·插入与 append 均无替换旧行＝旧行号段全「-」）**：

```pins
PIN|agent-skills/fuxi-skill/SKILL.md|补研自驱执行条款系（|0|1|-
PIN|agent-skills/fuxi-skill/SKILL.md|暂缓入池候裁报告件要件（|0|1|-
PIN|agent-skills/fuxi-skill/SKILL.md|v2.1（2026-11-13·入口件指针行小笔批·FX-U48）|0|1|-
```

（三钉现算依据（基线＝`ae6c530` 现算·起草当轮 `grep -cF` 逐枚现跑在册 §〇-6）：钉1-3＝SKILL.md 三新行入位臂——三钉语对基线各 0 命中（B=0）·各落 S1 围栏对应行首恰一行（A=1）·无替换旧行（D=0）⇒V0*=0／V1*=1 公式自洽。**钉语防自染自查**＝三钉钉语完整串在本票围栏外正文零落字（§头钉形态注／§〇 各段措辞与钉语完整串形态不同＝钉语带行头全角左括号形态只落钉块与归属围栏；§三判据以「三枚指针行头串＝钉块针语」指代不复打；款C 行内「（补研自驱执行条款系／…」＝后续字符非全角左括号＝不构成钉1 完整串，装配预演三钉语对拟后面各恰 1 坐实 §〇-8），起草轮 pins 预跑读数 §六在册。三钉两两互不含自查＝各钉为各行行头独立子串、行头串互不相同。工程师开工对三钉对开工基线逐枚复算 V0 相符方可动笔＝D-92；现算与表钉不符＝H-0 停笔呈裁禁凑绿。pins 现跑命令与读数入 §六。）

---

## 三、判据（收口判据闭集·逐条实跑留读数·起草轮 scratch 装配预演证据随注）

1. **SKILL.md 纯增与落位（机械）**：`git diff --numstat 开工ANCHOR..HEAD -- agent-skills/fuxi-skill/SKILL.md` ＝「**3 0**」（增三删零＝既有行全体逐字存续·删除列非 0 即红＝既有行被动案型）；行数收口 `wc -l` ＝ **41→44**（前后差＝3＝纯增行数判据）；收口 H2 节头计数 `grep -c '^## '` ≡ **4**（零新增节头）；三枚指针行头串（＝钉块三枚钉语，逐字见 pins 块）收口 `grep -cF` 各 ≡ **1** 行（逐条 grep 命中判据）；落位＝款A/款B 新 L32/L33（两契约行下）＋款C 新 L44（文件尾修订注记段）（hunk 头名点入回执）；difflib 纯增自证＝python 对开工基线与收口两面跑 `difflib` 比对，**deleted_chars ＝ 0** 且 delete／replace opcode 数＝**0**（两读数入回执）。预演证据＝起草轮 scratch 装配件（§〇-8）＝diff +3/-0＋节头 4＋wc 44＋difflib 删 0 全等在册。
2. **体量红线自证（机械）**：开工基线 `wc -l` ＝ **41** 现跑在册（§〇-2＝派工「SKILL.md 现面行数先实测登记」要件落账）；收口 `wc -l` ≡ **44** ≤ **200**＝体量红线自证读数（提案 §四-2 红线＋SKILL.md 修订注记 v2.0 行 ≤200 白纸在册＝本票不触不改）。
3. **改动原子性（机械）**：改动笔 `git show --name-only --format='' <该笔sha>` 恰 **1 面**（agent-skills/fuxi-skill/SKILL.md·多一少一即红＝多一面＝越出声明闭集案型即红·少一面＝改动未落）；`git diff --name-only 开工ANCHOR..HEAD -- agent-skills/fuxi-skill/` 本链笔面 ⊆ §一 声明闭集（链上他案笔照登不归因本链）；§一 禁动对钉十八枚收口点 `git ls-tree HEAD` 对开工点全等（含契约／gates 三件／adapters 三件／specs 两件／README／design／U47 票面／收口登记件／裁定件／share 三件）。
4. **门禁零扰动四读数（零断言施工机械证明面·主判据）**：收口 `python agent-skills/fuxi-skill/gates/assert-tool.py` 现跑四读数与开工基线 §〇-5 **逐字全等**＝汇总 `PASS=27 FAIL=0 PENDING_STAGE=0 总数=27` exit 0（assert 基数 **27** 不动）＋FC-2 读数行「注册表 **41** 字段·双向 diff=∅·实例⊆注册·FM条目纪律·值互洽全等」＋BW-3 读数行「产物正文实跑命中=0（扫描 90 件·实扫描判绿）」＋GS-5 读数行「断言基数27」；assert-tool.py blob 收口 `git ls-tree HEAD` 对开工基线全等（`dfc1fd47ce1ca394808e03c29e9887c4fe17fde3`＝禁动对钉收口必全等）＝**基数不动证明闭合**＝四读数全等＋工具件 blob 全等双保险。
5. **票面与落地面自证（机械）**：`python agent-skills/fuxi-skill/gates/check-ticket-pins.py --selftest` ≡ 用例 5／反常 0 exit 0；`check-ticket-pins --ticket 本票面 --base 开工ANCHOR实sha` ≡ 钉行 **3**｜违例 **0**｜exit 0（钉数 `grep -c '^PIN|'` ≡ 3 申报）；本票面＋改后 SKILL.md `python share/check-pointers.py --target <件>` 各 exit 0；改后 SKILL.md 复制件对 check-entity 四谓词零命中＝工程师落笔前对追加稿构造物现跑 `python share/check-entity.py --root <构造面>` `pattern=date count=0` 读数先行入回执（H-0 案型防再现·§头写死）。
6. **链面闭集（机械）**：`git diff --name-only 开工ANCHOR..HEAD` 本链笔 ⊆ §一 声明闭集四面（票面／起草回执／SKILL.md／工程师回执）；`git diff --name-only 开工ANCHOR..HEAD -- agent-skills/fuxi-skill/contracts/ agent-skills/fuxi-skill/adapters/ agent-skills/fuxi-skill/specs/ agent-skills/fuxi-skill/products/ agent-skills/fuxi-skill/gates/ agent-skills/fuxi-skill/README.md` ＝ **空集**（禁动面零扰动机械读数）；`git diff --name-only 开工ANCHOR..HEAD -- agent-skills/fuxi-skill/gates/assert-tool.py agent-skills/fuxi-skill/gates/assertion-catalog.md` ＝ **空集**（零机器断言零注记施工＝gates 全域零扰动）。
7. **落链前靶检（起草与施工各自）**：每笔落链前 `python share/check-pointers.py --target <本笔件仓根相对路径>` exit 0 零 BLOCK＝写死判据（起草轮本票面读数 §六在册）。

（H-0 被动咬处置分支（写死）：实跑出现——三钉现算与表钉不符／pins exit≠0 或钉数≠3／assert 收口非 PASS=27 FAIL=0／FC-2 读数非 41 字段／BW-3 非命中 0／SKILL.md numstat 非「3 0」或 wc 差非 3 或 difflib deleted_chars≠0 或 delete／replace opcode 非 0／改动笔面数≠1／禁动面 blob 对钉不符／contracts／adapters／specs／products／gates／README 面非空集／check-entity 收口非 0／run-gates 非 GATE PASS＝当场是红：工程师席立即停笔（禁改判据、禁凑绿、禁回改史账、禁自行加帽），回流件如实登记咬合明细＋定位串＋复现命令，呈主理人裁另案；本票按异常销账路径收口。咬出缺陷≠事故，凑绿＝事故。）

---

## 四、登记项知会（已裁登记·不入本票射程·非候裁·随收口知会）

1. **票三机检面单列票＝不开（零采纳）**：候选断言族（域名去重／log 序对拍／在场对盘／请求复算／六节 validator）＝FX-U47 收口登记白纸「票三零采纳不开」在册（`agent-skills/fuxi-skill/.collab/decisions/2026-11-13-FX-U47收口登记-补研自驱蒸馏上约闭环.md`）；本票零断言零注记＝gates 全域禁动对钉自证；凡后续改判采任一项＝另票＋扰动面集中形制承提案 §四-3 在册口径，非本票射程。
2. **E10 验收装配候选＝条款文字零预开照旧**：档三执行席位口径重审未呈拍前零预开（FX-U47 票 §四-3／§四-8 在册＝承载票＝蒸馏票线后续 EG-6 契约票，非本票）；本票两枚指针行零 E10 字样零验收装配指针。
3. **H-2 帧级标注＝已裁不入零预开照旧**：候补池候排（FX-U47 §四-1 在册）；本票条款面与指针行零帧级标注字样。
4. **README 旧值另票照旧**：README 断言基数旧值差＝另票修（FX-U47 §四-6 在册）；本票 README 禁动对钉；SKILL.md frontmatter `version: 2.0` 与包版本线同源口径＝随 README 另票一并核，本票零扩面（S1 零碰随注写死）。
5. **验收测试文档票（A1-A11 线）＝与本票并行另线**：FX-U47 收口登记随动口径白纸（验收测试文档票上游与票二并行）＝其起票与射程归主理人排程，本票零碰零预开。

---

## 五、回执与链条

起草回执＝receipts 桶「2026-11-13-FUXI-U48起草回执-v1」件（裸写·另笔·本席出）：含开工 HEAD 照登（`ae6c530`）＋起草笔 sha＋staged 两读差集自查行＋改动面起点 blob 与禁动对钉十八枚对开工基线现算 blob 表（＝票面回填值出处）＋起草轮全部现跑读数（assert 基线四读数／pins selftest 与本票预跑／pointers 靶检／SKILL.md 现面形制读数〔行数 41／节头 4／锚行唯一〕／三钉钉语 B 值现跑／H-0 对拍两探针／scratch 装配预演读数）＋§四 登记项转录＋撞锁等待轮数照登＋自查完工判据逐条。

收口链＝票面笔（起草一笔）＋起草回执笔→双席独立审（fresh eyes 互不读·同时派出·QA 席＋产品席）→会师→rev（如有修单）→放行呈皮总→工程师改动笔＋工程师回执笔→QA fresh eyes 全实跑（§三逐条复现＋对抗例：对抗一「纯增活性」＝scratch 副本改一既有红线速览行一字→§三-1 numstat 删除列／difflib 臂必红；对抗二「钉块 fail-closed 活性」＝删整 pins 块必非零 exit／删单枚钉必违例如实登记；对抗三「体量自证活性」＝scratch 副本尾插百行→§三-2 ≤200 臂必红）→收口登记；台账随注归台账席收口另笔，本票零预写。

施工段 commit 计划闭集＝改动笔（SKILL.md 单面＝封顶一笔）→工程师回执笔（封顶一笔）＝**施工段两笔封顶**；D-95 分段落笔＋FX_COMMIT_DECLARE（纯路径清单形态）＋pathspec 两端条款同 §头写死。本票链面封顶总账＝起草 2（票面一＋回执一）＋施工 2（改动一＋工程师回执一）＝**四笔封顶自算坐实**（双审件／rev／放行／QA 判词／收口登记各随其链另计不预占）。

---

## 六、落款（起草席自查读数·2026-11-13·arch-fuxi-u48）

- 起草开工 HEAD 实测＝`ae6c530a5f7c47767807018549ff7455b7f35d99`（＝FX-U47 收口登记笔＝链顶·起跑即报当轮读数与派工实测同轮坐实）；`git status --porcelain | grep -v '^??'` 读数＝恰两枚＝ledger.jsonl＋share/check-pointers.py（他案在飞·零碰零带入）；untracked 面照登零带入。
- 开工前置现跑在册：改动面起点 blob＋禁动对钉十八枚对 `ae6c530` 现算 blob 回填 §一；assert 基线 `PASS=27 FAIL=0 PENDING_STAGE=0 总数=27` exit 0＋FC-2「注册表 41 字段·双向 diff=∅」＋BW-3「产物正文实跑命中=0（扫描 90 件）」＋GS-5「断言基数27」；pins selftest 用例 5／反常 0 exit 0；SKILL.md 现面＝行数 **41**／H2 节头 4／两契约锚行唯一命中／blob `a97f6e20` 与 FX-U47 票禁动回填值全等（§〇-2）；契约八条款头收口面各 ≡1（§〇-4）。
- H-0 对拍在册（§〇-7）：成文形态探针（S1 三行装配件复制）check-entity＝date count=0／drive-path count=0／discipline-no count=0／ticket-no count=0 exit 0；裸日期段对照探针＝date count=1＋BLOCK exit 1＝谓词活性坐实。
- scratch 装配预演在册（.scratch/FX-U48-draft/ 不 commit）＝票面 S1 三行逐字取入基线副本装配现跑＝SKILL.md diff **+3/-0**＋H2 节头 **4**＋wc **41→44**＋difflib deleted_chars **0** 且 delete／replace opcode 数 **0**＋三钉语对拟后面各 **1**／对基线各 **0**——§三-1/-2 判据可机械跑坐实；fake-tree 完整包副本（.scratch/FX-U48-draft/faketre/）置入三行后 check-pointers exit 0＝§三-5 改后件靶检可跑坐实（§〇-10 在册）。
- pins 与靶检在册：起草轮预跑（落链前）＝`check-ticket-pins: 票 .collab/tickets/2026-11-13-FUXI-FX-U48-蒸馏票二SKILL入口件指针行红线速览两枚体量自证小笔票-v1.md（base ae6c530a）钉行 3｜违例 0｜exit 0`；命令＝`python D:\multi-agent-collab-devkits\agent-skills\fuxi-skill\gates\check-ticket-pins.py --root agent-skills/fuxi-skill --ticket ".collab/tickets/2026-11-13-FUXI-FX-U48-蒸馏票二SKILL入口件指针行红线速览两枚体量自证小笔票-v1.md" --base ae6c530a5f7c47767807018549ff7455b7f35d99`；靶检＝`python share/check-pointers.py --target "agent-skills/fuxi-skill/.collab/tickets/2026-11-13-FUXI-FX-U48-蒸馏票二SKILL入口件指针行红线速览两枚体量自证小笔票-v1.md"` exit 0（落链前在册＋落链后终值入回执）；靶检初跑曾 BLOCK 两枚短式指针（后缀多义）→S1 两行改仓根全路径形制后复跑 exit 0＝设计注 §〇-10 留痕。
- 红线申报：本席产出＝tickets 桶本票一笔＋receipts 桶回执一笔；SKILL.md／contracts/／gates/／specs/／adapters/／products/／evidence/／research/／receipts 他案面／audits/／qa/／defects/／decisions/／design/／口径件面／蒸馏提案面／README／share/／agent-experts/／softwares/ 零字节（本席起草全程——scratch 装配预演件不落任何真源）；SKILL.md 本笔零碰＝施工归放行后工程师席；零 git config 写；零 BYPASS；零 amend；零删锁；U36-U47 他案链面照登零碰。
- 时戳占位符纪律＝本票链上占位一律 `%ct`（`%cT` 非法形态禁复用＝U41 勘正先例）。

（票面完——蒸馏票二入口指针小笔票：排程已放行照此成文零候裁；登记项五条单列知会；本席起草段止于此。）

移交登记：本笔落链＝fresh 架构席接手笔（arch-fuxi-u48b）·前手实例（arch-fuxi-u48）终结于落链前·接手程序＝复核→认可→接收认领→移交登记·复核读数＝pins 3/0 exit0＋靶检 exit0＋四件套现读齐·接手复核逮票面自染短式 token 一处（§〇-10 自载 contracts/evidence-grading.md 反引号形态入 OA-D6 后缀多义 BLOCK＝起草席 §〇-10 自载 token 未复跑覆盖·本登记行自述亦裸文写＝同案型防再现）＝修法①去反引号随接手笔修正（主理人裁决授权在册·正文语义零变）·修正后复跑＝靶检 exit 0＋pins 钉行 3 违例 0 exit 0。