# SWB-T08R · 规则票修正版（R2）：权限表数据面机械化——engineer 写域按裁定一/裁定三重做＋deny 唯二联动处置＋约定 md 机制声明（规则票·L2·架构席起草·双席审票退回后修正）

- 起草实测 HEAD：`17171b2`（裁定三补充条款笔）。开工 ANCHOR 义务＝开工时实测 HEAD 为 `17171b2` 或其后可达后继，读数附回执开端。
- **废止声明**：本票废止 `.collab/tickets/2026-11-03-SWB-T08-seat-permissions-mechanization.md`（笔 `a76fe07`·下称 v1）——v1 双席退回（会师件 `.collab/2026-11-03-SWBFIX-T07T08-双席审票会师登记-v1.md`·`2ccc1ce`），本票＝作者席修正版（裁定件 `ff72b92` L27「生产权随作者席」）。v1 保留在册不作废件删除，其 engineer 写域段与判据 1–4 不再有效。
- 裁定基线链（盘上直读·后生效覆盖先）：
  - 裁定〇＝`.collab/decisions/2026-11-03-皮总裁定-SWB票包遗留三件.md`（`6d40ece`）③＝权限表机械化选项 A（本票票型与总范围仍承接）；
  - 裁定一＝`.collab/decisions/2026-11-03-皮总裁定-工程师写域规范与仓根项目子包分层.md`（`ff72b92`）：可写＝项目路径＋交付路径（含编译、部署）；**唯二排除＝项目路径下的 `.collab` 与 `docs`**；写域配置随项目走、docs 内专文定义（L9–12；L14 明文替换 v1 `deliverables/**` 案）；
  - 裁定三＝`.collab/decisions/2026-11-03-皮总裁定-项目自由分层与collab固定结构及docs约定md.md`（`18bf840`＋`17171b2` 补充条款）：规范面闭集三件（`{project_id}/.collab` 固定结构／docs 约定 md 机制／席位按 md 写入与校验）；自由面＝项目根除 `.collab` 外用户自定义；**用户 md 内 `.collab` 段一律不认**；**统一规范无特例**（含软开团、SWB 自身）；每项目子包＝独立自包含完整工作空间；
  - 双席审件＝`.collab/qa/2026-11-03-PM-SWBFIX-T07T08-审票-v1.md`（`0434754`）＋`.collab/qa/2026-11-03-QA-SWBFIX-T07T08-审票-v1.md`（`cf75f1e`）——修单 R1–R4＋条款 2/5/6/7/8 逐条覆盖见下表。
- 设计真源对照（登记面·只读禁写·`.gitignore:33` 不入 git 追踪＝行号以现盘直读为准）＝`.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md`：表2-1 节＝物理 L98–106；工程师行＝物理 L105；architect/qa 行＝物理 L103–104；表注·转正代写款＝物理 L107；路径锚定款＝物理 **L108**；顶层枚举款（逐字钉死六类）＝物理 **L110**；§3 回流四型＝物理 L141；受保护区词条＝物理 L230；§20.2③＝物理 L256。（Y1 黄修正：v1 所引 L107/L106 两处已改为 L110/L108 实测值；逐字引文与真源串对位义务不变。）
- 计数口径声明：occurrence 口径；判据命令一律自带落盘重定向；负例一律 exit≠0；行号＝起草实测现盘物理行号（锚 `17171b2`），开工复测位移则以逐字文本锚定位。
- Temp 条款（Y2 同款教训前置）：判据用仓外 Temp＝`T08_TMP` 由调用方注入，**必须 Windows 盘符形态**（例 `D:/…`；Git Bash 挂载形态 `/d/…` Windows python 不可直读，实测 `FileNotFoundError`）；禁 `/tmp`。

## 修单映射表（双席修单八条→本票落点·逐条对位）

| 修单 | 内容 | 本票落点 |
|---|---|---|
| R4（红⑦） | 写域段按裁定一/三重做（负式不可直书→承载与参数化） | T08R-A＋T08R-E＋候裁 R⑧ |
| 条2 | 唯二排除 vs deny_globs 联动矛盾显式处置＋s4 t13 随动 | T08R-B2（机械化处置＋探针证据＋设计基线偏差登记） |
| R1（红） | v1 判据2 与 lease-issuer L70–71 子集校验互斥 | v1 判据 2 随废止取消；新构型下无「`deliverables/**` 全域行＋具体路径」组合，负/正例改判据 3/4/5（探针 P-a/P-b 实测对位） |
| R2（红） | 判据4 正则不容首字符 `.`→目标永不可达 | 机械判定标准 v2 正则修正（见下节）＋基线复算 34/14→10（起草探针 P-regex 落盘复现） |
| R3（红） | 「全表 30 行」应为 34 | T08-B 节读数改 34（host 13/product 3/architect 7/qa 4/engineer 5/human 2＝34·python 复算 P-regex 同读数） |
| 条6 | 候裁⑧并入同处置 | T08R-B2 同段处置＋候裁 R⑧新版三案（本批缺省＝过渡态不固化） |
| 条7 | 候裁⑤重议为部署路径承载 | 由裁定三.18 关闭：承载＝约定 md 交付路径字段（T08R-E 提 schema）；v1 候裁⑤取消 |
| 条8 | 真源行号两处（L107→L110、L106→L108） | 头部真源对照行已按实测改附；T07 侧黄（Y2–Y5）不属本票，由主理人按会师件§四作 T07 开工附注投放 |

## 机械化判定标准 v2（R2 修正口径·审查与判据共用）
- 机械行＝匹配 `^[.A-Za-z0-9][A-Za-z0-9._/*-]*$`（首字符容 `.`；**字符类不含花括号**——含 `{}` 行即判非机械，与「花括号占位符＝非机械行」条款自洽，v1 字符类含 `{}` 的自咬消除）。
- 行为事实基线（复测属实）：非机械行在 lease-issuer L70–71 与 write-guard `glob_match` L100–105 恒不命中＝无害滞留；`**` 全域行对具体路径在 lease-issuer 子集校验不命中（QA P8 探针复现），负排除式不可直书——故项目根可写面只能以**具体前缀行**表达，其内容从约定 md 读取（T08R-E），本票不硬编码任何用户目录。
- 起草探针 P-regex（盘上 python 直读）：现盘全表 write_globs 总行数＝**34**（非机械 **14**＝host4/product0/architect5/qa2/engineer2/human1，与双席复算逐值全等）；本票账一构型后＝总行 **34**（engineer 5→3、host 13→14、architect 7→8）、非机械 **10**（host3/arch4/qa2/human1）。

## 声明闭集（6 件·本票唯一可写面）
- 声明闭集：
- deliverables/experts/baigong-software-team/config/seat-permissions.json
- deliverables/experts/baigong-software-team/config/seat-permissions-hooks-map.json
- deliverables/experts/baigong-software-team/.codebuddy-plugin/plugin.json
- deliverables/experts/baigong-software-team/bundle.lock
- deliverables/experts/baigong-software-team/plugin.json
- deliverables/experts/baigong-software-team/README.md

## 逐条施工规格

### T08R-A engineer 写域段重做（裁定一＋裁定三形态）

`config/seat-permissions.json` engineer 行 L49 现值（逐字）：
`"write_globs": ["（工作空间根∪部署路径）−受保护区", ".collab/inbox/engineer/", ".collab/returns/engineer/", ".collab/drafts/deploy/", "限定当票租约路径集"],`
替换为（三机械行保留＝表2-1 逐行转录忠实性维持，行为零变化：三行今日已机械在位）：
`"write_globs": [".collab/inbox/engineer/", ".collab/returns/engineer/", ".collab/drafts/deploy/"],`
同席增两注记键（不新增任何用户目录硬编码——裁定三.3「无特例」＋补充条款「机械化方案不得为任何项目留特例通道」）：
- `"write_globs_note": "项目根∪交付（编译、部署）路径可写面＝参数化承载：每项目 docs 约定 md（见 project_domain_md 键）声明，门禁/租约机件读 md 取项目根与交付路径后以具体前缀行注入当票租约——D1 项目命名未裁（裁定二.4），枚举行随重组 B 批填充，本批不建行；描述行（v1 前值）与『限定当票租约路径集』入本注记（行为零变化款：两者在两层校验恒不命中）。"`
- `"project_domain_md": "docs/collab-project-structure.md"`（约定文件名＝本票提案，经双席审票定＝裁定三①「实施细节由架构席提方案、双席审票确定」；路径读作项目根相对，每项目必有——裁定三补充条款「独立自包含」）

- 语义账：可写面（项目根∪交付路径）＝md 数据驱动（B 批机件消费＝施工票，机制代码本票零触碰）；唯二排除（项目根下 `.collab`、`docs`）＝本票 B2 段 deny 落实；三 `.collab` 机械行与「排除 .collab」的设计基线冲突＝旧表2-1 授权 vs 裁定一新口径的既有矛盾，**不自行消解**，候裁 R⑧三案呈裁（本批缺省过渡态＝三行保留）。
- 起草探针（Temp 配置构型＝本规格值·Windows 路径形态）：P-a `--path-glob ".collab/returns/engineer/V1.md"`→**exit 0**（签发面现状保持）；P-b `docs/x.md`→**exit 2**；`.collab/ledger/x`→**exit 2**。

### T08R-B 全表逐行机械化审查（v1 保留段·行数读数按 R3 修正）

现盘全表 **34** 行 write_globs（host 13／product 3／architect 7／qa 4／engineer 5／human 2——python 复算＝34，v1「30」作废）。两分账：
- **账一（本票机械修正·语义零变化）**：①engineer 段＝T08R-A；②host `.collab/human/{intake,reviews}/`→拆 `.collab/human/intake/`、`.collab/human/reviews/`；③architect `.collab/drafts/{design,adr}/`→拆 `.collab/drafts/design/`、`.collab/drafts/adr/`。账一后全表非机械行＝**10**（逐值见 P-regex）。
- **账二（候裁滞留·零动）**：host `.collab/tickets/{id}/仅生命周期字段`／`docs/转正代写`／`.archive/退役定稿落位`；architect tickets 描述行／`开发票四字段`／`租约段签注与灰度判据（票内）`／`tests/共写（增删改走 C1）`；qa tickets 描述行／`tests/共写`；human「签名经主理人落…」——现恒不命中＝无害滞留，候裁 R①–R④。回执附全表 34 行逐行审查读数表。

### T08R-B2 engineer deny_globs 唯二联动显式处置（修单条2＋条6 同段）

现值（seat-permissions.json L51 逐字）：`"deny_globs": ["docs/**", ".archive/**", ".collab/**", "tests/**"]`——`.archive/**`＋`tests/**`＝裁定一「唯二排除」之外的第三/四排除，显形互斥。**机械化处置（本批落）**：改为 `"deny_globs": ["docs/**", ".collab/**"]`（＝唯二排除直书）。同步 `config/seat-permissions-hooks-map.json` engineer 行 L28 `deny_globs` 同值（s4 t13 派生同源断言 `row["deny_globs"] == src_deny[...]` 随两文件一致更新而绿）。`deny_globs_note` 随动改写（删旧双层双址豁免注，增新注：「`.archive/`、仓根 `tests/` 出 deny 列系裁定一唯二排除落实（2026-11-03 ff72b92）；其防护由租约签发面承载——不在 engineer write_globs 域即不可签发，写侧『路径∉当席租约』deny 兜底（起草探针 P-c 实测）；仓根 `tests/` 真源域双层双址条款随 B4 票包再锚与重组批重释。」）。

- 防护面不降级论证（起草探针 P-c·Temp hooks-map 构型＋deliverables 租约）：`tests/root-judgement-truth.py`→仍 **deny**（原因行＝`路径∉当席租约 path_globs…`）；`.archive/old.md`→仍 **deny**（同因）；`docs/x.md`→deny 经 deny_globs（`glob='docs/**'`）。s4 t03 断言面只断 `"permissionDecision":"deny"` 字符串（test_enforcement.py L93–99 直读），原因行变更不破断言。
- 设计基线偏差登记：表2-1 工程师行「明确不可写」列（物理 L105）含 `.archive/`、仓根 `tests/`——数据面按裁定收缩后与该列不再逐行对位，属**裁定覆盖设计基线**的预期偏差，随 B4 票包 V13 再锚/设计修订呈请追认（候裁 R⑨），本票不自行改设计真源。
- **候裁⑧并入处置（新版 R⑧）**：三 `.collab` 授权子域与「排除 .collab」矛盾＋`.collab/**` deny 吞回流件路径——起草探针 P-d（现盘 map 未改构型）：`.collab/returns/engineer/V1.md` 租约内写→仍 **deny**（`glob='.collab/**'`）。三案：(i) 裁定三① `.collab` 固定结构规范颁行、其中显式授权 engineer `returns/inbox/drafts-deploy` 子域，deny `.collab/**` 精化为显式枚举减授权（精化清单先决＝固定结构规范闭集，规范落票尚未在包）；(ii) 绝对排除→删三 write_globs 行＋回流件落盘路径迁出 `.collab`（改设计基线，return-template L4 随动）；(iii) 本批过渡态＝三行保留＋`.collab/**` deny 保留＝签发可/写拦的显性化冲突维持（**缺省＝(iii)，非固化**，回执如实登记该读数）。产品席已表向＝deny 精化方向（(i) 向）、allow 穿 deny 反模式不取——本票采( i ) 之先决登记，不自行落精化枚举（清单无规范真源可引＝无据建行，fail-open 风险：枚举减授权对新开子域默认放行）。

### T08R-C hooks-map 身份映射补行（v1 保留段·双席全绿）

`config/seat-permissions-hooks-map.json` `agent_type_to_seat`（L32–38）追加五行（旧五行保留 legacy——drill-03/drill-05/tests-s4 旧身份零破坏；实测新五身份现盘全不命中→写侧 fail-closed 全灭）：
```json
    "software-team-lead": "host",
    "software-team-product": "product",
    "software-team-architect": "architect",
    "software-team-qa": "qa",
    "software-team-engineer": "engineer"
```
`_spec`「席位覆盖说明」行尾补注：「新五卡 frontmatter name（`software-team-*`）与旧五名双载；旧名＝legacy 别名，其清退随 B 批身份面收敛。」

### T08R-D 版本账随动（v1 保留段·纪律①三同源）

`.codebuddy-plugin/plugin.json` L3、`bundle.lock` L5、根 `plugin.json` L3 三处 version 同源 bump（现值 0.1.14；若 T07 已先行落笔则 0.1.15→0.1.16，否则 0.1.14→0.1.15——前后值各附实测 grep 读数·F7）。`README.md` 版本账 append-only 一行：「权限表数据面机械化（SWB-T08R）：engineer 写域参数化＋deny 唯二落实＋hooks-map 新五身份补行，依据＝皮总裁定 ff72b92/18bf840」。既有行零回改。（联动注记承 PM 判11：若 T07 候裁②裁成 `.codebuddy-plugin` 整体退役，本段对该件随动落空——收口批登记。）

### T08R-E docs 约定 md 机制规范声明（裁定三①②③承载面·本票只声明不落文件）

本票闭集无 md 实体件（md 属各项目 docs＝自由面产物，随项目建立与 B 批重组落位）；本节＝规范声明，B 批机件与门禁按此消费：
1. **约定文件名（提案）**＝`{project_root}/docs/collab-project-structure.md`（名由双席审票定＝候裁 R⑤）；每项目必有（独立自包含：项目子包可整体拷走即完整）。
2. **机读节最小 schema（提案）**：节标题 `## swb-project-domain` 内两字段——`project_root: <项目根仓根字面>`；`delivery_paths:` 列表行（交付/编译/部署路径，仓根字面）。其余节＝人读自由描述，机检不解析。
3. **消费规则**：租约/门禁机件读该 md 取项目根与交付路径→engineer 当票租约以具体前缀行注入（lease-issuer 子集校验形态可达＝P8 探针）；md 缺失/字段缺→engineer 项目域空＝**fail-closed**（仅按其余在位行签发）。
4. **`.collab` 不可覆写条款**：md 内任何 `.collab` 开头节/路径行，机检**一律忽略并按违例登记**（裁定三.3）；`.collab/**` deny 与固定结构校验不受 md 内容影响（裁定二 §二.19）。
5. **无特例条款**：本机制对项目无差别（含软开团自身、SWB 自身）；seat-permissions 静态 JSON 不硬编码任何用户目录（本票 engineer 行零用户目录行即此条款自证）。
6. 上述 3/4/5 的可机械验证判据（md 解析器＋`.collab` 段忽略断言＋项目自包含闭环断言）＝**B 批施工票验收面**（机制代码非本票闭集）；本票落数据面注记键（`project_domain_md`）＋本段规范文本（票面＝规范登记载体）。

## 验收判据（全部机械可判·命令自带落盘·负例一律 exit≠0）

0. Temp 注入 Windows 盘符形态（见头部 Temp 条款）；开工基线判据（1b/3b/5b）先跑先落盘，与施工后读数并呈对照。
1. **数据面断言**：python 内联读两 config：engineer `write_globs` 集＝{`.collab/inbox/engineer/`,`.collab/returns/engineer/`,`.collab/drafts/deploy/`}（恰 3 行）；engineer `deny_globs`＝`["docs/**", ".collab/**"]`；hooks-map engineer 行 deny_globs 与源件相等；`project_domain_md` 键在位；host/architect 四展开串各 occurrence＝1 → 全断言 exit 0，读数落 `$T08_TMP/c1.out`。
2. **机械审查断言（修正正则）**：按「机械化判定标准 v2」正则 python 复算：总行数＝**34**；非机械行＝**10**（host3/product0/architect4/qa2/engineer0/human1）；开工基线同式先跑＝34/**14**（逐席 host4/product0/architect5/qa2/engineer2/human1）落 `$T08_TMP/c2-base.out`/`$T08_TMP/c2.out`。
3. **正例·签发面现状保持**：`lease-issuer --seat engineer --path-glob ".collab/returns/engineer/x.md"` → exit 0（施工前后不变·P-a 对位）→ `$T08_TMP/c3.out`。
4. **负例·四越域请求各 exit≠0**：`--path-glob` 依次 `docs/x.md`、`.collab/ledger/x`、`.archive/x.md`、`src/app.py`（探针样例串＝自由面典型用户目录形态，非规范建行——项目域未注入前缀不可签发即此判据本体），四条逐条 exit 码 echo 落 `$T08_TMP/c4.out`（P-b 对位；现盘开工基线同式＝四条均 exit 2，施工后不得放开）。
5. **写侧 deny 链三读数**：喂 engineer 身份：`docs/x.md`→deny 且原因行含 `deny_globs`＋`glob='docs/**'` occurrence＝1；`tests/root-judgement-truth.py` 与 `.archive/old.md`→仍 deny 且原因行含 `∉当席租约` occurrence 各 1、含 `deny_globs` occurrence 各 0（＝B2 防护面迁移到租约兜底的机械凭证·P-c 对位）；`.collab/returns/engineer/x.md`（租约在册）→仍 deny 且原因行含 `glob='.collab/**'`（＝候裁 R⑧过渡态读数登记·P-d 对位）→ 三读数落 `$T08_TMP/c5.out`。
6. **身份映射端到端**：hooks-map 五新键 json 断言 exit 0；Temp 直写租约行（`{"ts":"t","lease":{"ticket_id":"T08R6","seat_id":"engineer","path_globs":["deliverables/**"],"hash":"h"}}`）＋`write-guard --path "deliverables/experts/baigong-software-team/x.py"` 喂 `{"agent_type":"software-team-engineer","agent_id":"software-team-engineer-x"}` → stdout 无 `"permissionDecision"`（放行·与既有词表一致不自造 allow）→ `$T08_TMP/c6.out`。
7. **旧身份零破坏**：drill-03 单跑 exit 0（旧身份串 `software-engineer` 经 legacy 行仍命中）。
8. **测试实体回归**：s2（带兄弟件调用形制）与 s4 各 exit 0（t03 deny 断言、t13 派生同源断言随两 config 一致更新而绿）→ `$T08_TMP/c8.out`。
9. **六演练回归**：`T06_TMP="$T08_TMP" bash …/drill-runner.sh` → exit 0 且 `SIX_DRILLS_GREEN` occurrence＝1（drill-05 product 席走位零触碰＝候裁 R⑦未裁前保持）。
10. **版本三同源**：三文件 `"version"` 读数同值＝本批后值（前后值各附实测·F7）→ `$T08_TMP/c10.out`。
11. **门禁零回归＋票体自咬**：`bash deliverables/skills/object-audit/scripts/run-gates.sh --root . > "$T08_TMP/c11.out" 2>&1` → GATE PASS exit 0；`python …/count-assert.py --mode1 .collab/tickets/2026-11-03-SWB-T08R-seat-permissions-mechanization-rev2.md --expect 6` → exit 0。

## 票间关系
- 前置：裁定〇③＋裁定一＋裁定三（含补充条款）；SWB-T07（建议先派：版本链衔接；丙账身份面归本票 T08R-C 承接）。
- **后置/依赖（如实登记）**：engineer 对交付面租约的**实际放行**＝B 批（约定 md 落位＋机件读取＋D1 项目命名裁毕填充枚举行）——原缺陷（`--seat engineer` 交付面 REJECT）的闭环终点在 B 批判据，本票完成态＝数据面唯二对齐＋参数化承载就位＋身份面补全，非原缺陷即时闭环。B4 票包再锚批随 design 基线偏差追认（R⑨）。
- 质量链：本票→产品席＋QA 席双席再审→三方收口→呈皮总放行后派工程师施工。

## 禁动面（零触碰）
- 设计真源登记件与 `.collab/refs/external/` 全域；`.collab/` 其余（回执除外）；`docs/`、`tools/`；一切项目 docs 约定 md 实体（B 批落位，本票不落）。
- **T06 六演练除 drill-05 走位随动外零触碰**（走位改 engineer＝候裁 R⑦，未裁零触碰）；`write-guard.py`、`lease-issuer.py` 及其余 scripts 零触碰（机制代码＝T04 闭集；md 读取机件＝B 批施工票）；席位卡五新件零触碰（engineer/QA 卡按 md 校验的执行规范句＝候裁 R⑥）；`seat-permissions.json`／hooks-map 除本票点名行（engineer write_globs/deny_globs/note 键、host/architect 展开行、agent_type_to_seat 增行、_spec 注）外各键零动（`explicitly_not_writable`/`carrier`/`table_notes`/其余四席 deny 数组＝零动）。
- v1 票面本体零改动（废止声明在本票，append-only 治理惯例）；工程师不得改本票票体四字段与验收行；不自判合格（制度③）。

## 候裁点（单列·不自行拍）
- **R①** host/architect/qa `.collab/tickets/` 三席字段级约束（仅生命周期字段／票面文档修票权／缺陷票修票权）超 path_glob 表达力——展开＋注记 vs 维持现样。
- **R②** host `docs/转正代写`／`.archive/退役定稿落位`＝promote-manifest 机械通道非席位租约写（真源物理 L107 转正代写款）——建行/删行/改注记。
- **R③** architect/qa `tests/共写（增删改走 C1）` 机械化＝扩权（现恒不命中→改后可签发仓根真源域租约；C1 约束不可 path 判；真源 architect/qa 行＝物理 L103–104）——双席对表。
- **R④** human 行「签名经主理人落 .collab/human/reviews/」不入 hooks 强制面——机械化与否。
- **R⑤** 约定 md 文件名（本票提案 `docs/collab-project-structure.md`）＋最小 schema 两字段形制＝裁定三①明文「架构席提方案、双席审票确定」——本票所提即方案，双席审票裁名。
- **R⑥** engineer/QA 席位卡是否增「按项目约定 md 严格遵循分层写入/校验」纪律句（裁定三③执行规范的卡面承载）——卡面属 T05 装配面，随 B 批或卡面随动票处置。
- **R⑦** drill-05 走位改 engineer（B 批判据填充后方可行）——演练面改写归 T06 闭集。
- **R⑧**（v1 候裁⑧新版·三案见 T08R-B2）engineer 三 `.collab` 授权子域 vs 「排除 .collab」＋`.collab/**` deny 吞回流件路径：(i) 固定结构规范授权＋deny 精化（先决＝规范闭集在包）／(ii) 绝对排除＋回流件迁出 `.collab`（改设计基线）／(iii) 过渡态维持（**本票缺省**）。产品席建议 (i) 向已登记在案。
- **R⑨** 表2-1 工程师行「明确不可写」列（含 `.archive/`、仓根 `tests/`）与裁定一唯二排除的设计基线偏差——B4 票包再锚/设计修订呈请追认（本票不自行改设计真源）。
- **仓根路径锚定前置条款**：判据/探针涉及仓根字面者（`.collab/**`、`docs/**`）一律按裁定三补充条款「无裸公共区」假设参数化——仓重组（B0–B5）若改仓根布局，本票行号与仓根字面随 B 批再锚，不为本仓留特例通道（无特例条款）。

## 候补优化池登记句（不入本票议程·仅登记）
legacy 旧五身份别名行最终清退（B 批身份面收敛）、`agents/*.md` 裸基名 WATCH 族、tools 两基线快照再生（走 `--regen-*` 开关）、s2 t05 对新注记键的断言补强、约定 md 解析器与 `.collab` 段忽略机检（B 批施工票验收面），均登记候补池。

## 回执
落 `.collab/receipts/2026-11-03-SWB-T08R-receipt.md`：开端 HEAD 实测＋完整文件清单（与 commit name-only 全等）＋修单映射表逐条落点读数＋判据 0–11 逐条命令与实测读数（含开工基线 c2-base/c4 前值对照）＋全表 34 行逐行审查读数表＋候裁 R①–R⑨逐条呈裁原文引用＋R⑧过渡态读数如实登记。交付笔单独 commit `collab:` 前缀只含闭集 6 件；回执笔随后单独笔。禁 `--no-verify`、禁 amend；pre-commit 门禁真拦时如实报告拦点并在闭集内修正重过，不得绕闸。