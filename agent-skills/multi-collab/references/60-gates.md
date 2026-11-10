# 出口路由与门禁（退出码·三出口·升级）

> 期别：**编译期**（路由表改动＝改判据＝L0；调整计数＝查历史，不是改表）。
> 出处：本地约定（显式标注）——「严重度由规范定、出口由治理定、次数由运行历史定」三轴分离为本件归纳；「退出码可当门禁」沿用 `40-deployment.md`「A 形态五条硬规则 4·超期是算出来的」；「生产方不兼判定方」「治理盘唯一写盘出口」＝业界通识（职责分离）＋本包 `SKILL.md`「六道硬约束」。
> 与另两件的关系（**只指路径，不复写正文**）：发布闸与发布器行为见 `object-build/references/60-publish.md`；规范来源判定与 exit 3 的成因见 `object-audit/references/70-provenance.md`。

## 〇、三条铁律（违反即设计违规，不是风格问题）

1. **判据与处置分离**。检查脚本**只输出**「严重度 ＋ spec_id ＋ 位置 ＋ 一句话」，**不决定拦不拦**。脚本源码里出现 `if blocking:` 之类的策略判断，即为设计违规。
2. **退出码是闭集**（§六）。未定义的码**一律按 4 处理**，且**任何非 0 都不得计绿**。
3. **本件正文的 json 围栏是唯一机器源**。人读说明与机读配置写在同一个文件里，避免两份必然漂移；实现**不得**另存一份配置（另存＝第二真源）。

## 一、三个出口（阻断与否是治理决定，不是严重度的推论）

| 出口 | 载体 | 形态 | 谁接 | 阻断？ |
|---|---|---|---|---|
| **① 提交前拦截** | `.git/hooks/pre-commit` → 调门禁入口脚本 | stdout 一行一封：`<file>:<line>: <SEV> <spec_id> <msg>`；退出码决定提交是否被拒 | 提交者本人（即时） | **是**（按路由表） |
| **② 审计报告（证据）** | `.collab/evidence/gates/<日期>-<脚本>-<短摘要>.json` ＋ 当期报告一行摘要 | `{run, script, commit, findings:[{file,line,spec_id,severity,msg,detail}], exit}` | 审计席（进「未绿」桶） | 否 |
| **③ 呈拍（上报决策者）** | `.collab/inbox/<主理人>/<日期>-呈拍-gates.md` | 每条 ≤5 行：`spec_id｜计数｜趋势｜建议动作＋利害`，**须合呈拍三律**（`10-roles.md「六、呈拍三律」`） | 主理人 → 决策者 | 否（但是升级信号） |

**为什么①选版本库提交钩子，而不是 AI 工具钩子**：工具钩子的"写入后"型回调官方明写**不可阻断**——它只能让模型看见错误输出，而文件**已经写完**。提交钩子与工具无关，覆盖所有提交（含人手改、含别的工具改）。"写入后兜底"型设计一律不采用：**它看起来在拦，实际拦不住。**

**钩子文件本身不入仓**：它是每台机器的本机配置，克隆后天然失效；入仓反而制造"以为有门禁"的假象。入仓的是**幂等安装器**（可复现）。

## 二、路由表（唯一机器源）

```json
{
  "version": 1,
  "outlets": {"commit": 1, "report": 2, "escalate": 3},
  "on_severity": {
    "BLOCK": {"commit": "block", "report": true},
    "WATCH": {"commit": "advisory", "report": true},
    "DEFER": {"commit": "advisory", "report": true}
  },
  "escalate": {
    "repeat_threshold_block": 3,
    "repeat_threshold_watch": 5,
    "on_spec_unresolved": true,
    "on_infra_error": true,
    "on_new_spec_first_hit": true
  },
  "per_spec": {
    "OA-T1": {"commit": "block"},
    "OA-D1-1": {"commit": "block"},
    "OA-D6": {"commit": "advisory"},
    "OA-S5": {"commit": "advisory"},
    "OA-S2": {"commit": "advisory"},
    "OA-D8-4": {"commit": "advisory"},
    "MC-SOT-1": {"commit": "advisory"},
    "MC-SOT-2": {"commit": "advisory"},
    "MC-SKILL-LINE": {"commit": "advisory"},
    "MC-SOT-EXEMPT": {"commit": "advisory"},
    "EAC-L1": {"commit": "advisory"},
    "EAC-L2": {"commit": "advisory"},
    "EAC-L3": {"commit": "advisory"},
    "OA-D6-3": {"commit": "advisory"},
    "OA-D6-4": {"commit": "advisory"},
    "MC-SEAT-DECL": {"commit": "advisory"},
    "OA-D6-5": {"commit": "advisory"},
    "OA-E-ADR-1": {"commit": "advisory"},
    "OA-E-ADR-2": {"commit": "advisory"},
    "OA-E-ADR-3": {"commit": "advisory"},
    "OA-E-ADR-4": {"commit": "advisory"},
    "OA-E-ADR-5": {"commit": "advisory"}
  }
}
```

**读表规则（实现须逐条落实，不许"取默认"了事）**

| # | 情形 | 处置 |
|---|---|---|
| 1 | `per_spec` 有该 `spec_id` | 用它的 `commit` |
| 2 | `per_spec` 无该 `spec_id` | 用 `on_severity[<SEV>]` 的默认 |
| 3 | 出现**未知 SEV**（不在 BLOCK/WATCH/DEFER） | **exit 4**（表的取值域被写坏了，不得猜） |
| 4 | 任一必填键缺失、json 解析失败 | **exit 4**（fail-closed，不得"降级为不拦"） |
| 5 | 表里的 `spec_id` 指向的条款在规范件里解析不到 | **exit 3**（提供者欠账，见 §六） |

## 三、三条轴必须分开，不许混成一列

| 轴 | 由谁定 | 存在哪 | 例 |
|---|---|---|---|
| **严重度** `SEV` | **规范自己**（规范件里已写"阻断/关注/可延后"） | 各规范件的「判定要点」段 | 归属缺＝阻断 |
| **出口** `outlet` | **本件的路由表**（治理决策） | 上面那段 json | 同一条款可配成"拦并记"或"只记" |
| **次数／趋势** | **运行历史** | `evidence/gates/` 累计 | 同一 `spec_id` 累计次数 |

把三者合成一列（例如"重要就拦"）是这类机制最常见的死法：**严重度一改，出口跟着变；出口一改，历史计数失去意义。**

## 四、`per_spec` 每一条的严重度依据（对账表·缺依据的不许配 `block`）

| `spec_id` | 配 | 规范依据（条款锚） | 依据状态 |
|---|---|---|---|
| `OA-T1` 项目实体 | `block` | `object-audit/references/10-skill.md「判定要点」`：「问净」不合格＝阻断 | **足** |
| `OA-D1-1` 归属声明随身 | `block` | `object-audit/references/50-document.md「判定要点」`：D1-1 归属缺＝阻断 | **足** |
| `OA-D6` 引用完整性（悬空） | `advisory` | 同上「判定要点」的阻断清单里**没有 D6**（只列 D1-1／D2-1／D2-3／D3／D7-1／D7-2／D8-2） | **缺** |
| `OA-D8-4` 索引对账 | `advisory` | 同上：`D8-4` **未列**（只列 D8-1 关注、D8-2 阻断） | **缺** |
| `OA-S5` 体量披露 | `advisory` | `10-skill.md「判定要点」`「问净」覆盖 S1–S5，而「问界」单列"容量"可判关注——同一测项两种读法 | **冲突** |
| `OA-S2` 触发描述 | `advisory` | 同 `OA-S5`（S2 属 S1–S5 段，但「判定要点」只按"四问"分级，未到测项级） | **冲突** |
| `MC-SOT-1` 骨架-本体行级重合 | `advisory` | `70-charter.md「4.1 三守门①单真源」`（本包规范件·正文已落盘） | **足**（mode 仍 advisory＝§九·② 先取信号；升 block 属另一次拍板） |
| `MC-SOT-2` 反引号 .md 指针可达性 | `advisory` | `70-charter.md「4.1 三守门①单真源」`（同上） | **足**（同上） |
| `MC-SKILL-LINE` 技能层 ≤5000 | `advisory` | `70-charter.md「4.2 2500 分轨」`（本包规范件·正文已落盘） | **足**（同上） |
| `MC-SOT-EXEMPT` 基线豁免形态 | `advisory` | `70-charter.md「4.3 基线豁免形态」`（本包规范件·正文已落盘；拍板＝皮总拍板 §九·①） | **足**（同上） |
| `EAC-L1` 议题包/汇总体裁 | `advisory` | `external-advisor-collab/references/20-rounds.md` §二/§三（收敛类必含「合流与分歧清单」节）＋`40-artifacts.md` §一 收敛类注/§二 新提议登记（条款正文已落 provider 包·EAC-SK1/SK2） | **足**（首挂 advisory＝EAC-SK5 票面 T3；升 block 候条款实跑零误报读数入 evidence 后另拍） |
| `EAC-L2` 交接件禁模式 | `advisory` | `external-advisor-collab/references/40-artifacts.md` §四之二（件性声明行＝扫描面定位判据·讨论会特有禁列）＋本包 `20-handoff.md` §二（三正面判据·通用侧·EAC-SK4） | **足**（同上） |
| `EAC-L3` 议题包编号唯一性 | `advisory` | `external-advisor-collab/references/20-rounds.md` §一.5 编号纪律闭集（一包一轮·已分发禁 v2·EAC-SK1） | **足**（同上） |
| `OA-D6-3` 交付包指针闭集 | `advisory` | `object-audit/references/50-document.md` D6 表 D6-3 行（条款正文已落 provider 包·ENG-G2 WP-2） | **足**（首挂 advisory＝ENG-G2 裁②；升 block 候实跑零误报读数入 evidence 后另拍） |
| `OA-D6-4` 交付包内指针可达性 | `advisory` | 同上 D6-4 行（同上） | **足**（同上·首跑读数见交付回执，跨技能引用面命中属另案候裁项信号） |
| `MC-SEAT-DECL` 席位自指短声明形式约束 | `advisory` | `deliverables/experts/baigong-software-team/skills/software-orchestration/references/handoff-discipline.md` §十（条款正文已落盘·ENG-H1） | **足**（首挂 advisory＝整合清单 §六；升 block 候实跑零误报读数入 evidence 后另拍） |
| `OA-D6-5` 施工票声明闭集对账 | `advisory` | `object-audit/references/50-document.md` D6 表 D6-5 行（条款正文先落·同票先行 commit） | **足**（首挂 advisory＝整合清单 §六；存量不回扫豁免复核挂事件锚·§八-5） |
| `OA-E-ADR-1` ADR 头块断言（docs/adr 族） | `advisory` | `object-audit/references/50-document.md` E-ADR 节 E-ADR-1″ 行（条款正文随 ADR-L0 同批先落 provider 包） | **足**（首挂 advisory＝ADR 工序放行裁定候裁③既批射程；升 block 候实跑零误报读数入 evidence 后另拍） |
| `OA-E-ADR-2` ADR 编号正断言＋唯一＋递增 | `advisory` | 同上 E-ADR 节 E-ADR-2‴ 行（同上） | **足**（同上） |
| `OA-E-ADR-3` ADR 双向 supersede 全向校验 | `advisory` | 同上 E-ADR 节 E-ADR-3″ 行（同上） | **足**（同上） |
| `OA-E-ADR-4` ADR accepted 不可变 | `advisory` | 同上 E-ADR 节 E-ADR-4″ 行（同上） | **足**（同上） |
| `OA-E-ADR-5` ADR 三面对账（桶互斥和式） | `advisory` | 同上 E-ADR 节 E-ADR-5‴ 行（同上） | **足**（同上） |

> 注（批 5-③ W6 留痕·覆盖批 5-② 同处留痕）：上表四条规范依据的**正文已落本包** `70-charter.md` §四（4.1／4.2／4.3），读表规则 5 由「id 串出现在本件 json 围栏内」的**自指式满足**转为**条款级真满足**（四条 id 均可在 `70-charter.md` 解析到，非仅在本件 json 围栏内出现）。`mode` 一律维持 `advisory` 不变——依 decisions §九·②「先挂 advisory 取信号」；升 block 须先有条款级依据再由治理改本表（配套规则 2）。

三条配套规则：

1. **`block` 必须有条款级依据**。没有依据就只能是 `advisory`——**不许因为"这条看起来很重要"就配 `block`**。理由：误报会让人关掉门禁，而"重要"是主观判断，不是判据。
2. **`block` 的依据在规范里升级，必须先进规范、后进本表**。想把 `OA-D6` 升成 `block`，正确路径是先改 `object-audit/references/50-document.md「判定要点」`（L0），再改本表；**只改表＝脚本的强制力超过了条款的强制力**，那条线一破，本件就退化成一张"谁声大听谁的"的清单。
3. **依据"冲突"的两条取 `advisory` 是本席裁定，列入待拍**。取舍理由：升格会立刻增加误报面，而降格的漏报可由审计席的人判补足——**门禁死于误报，不死于漏报**。

**尚未落盘的条款不得进表**：`OA-D6-2`（指针禁用序号定位）在 `50-document.md` 落盘前**不许**出现在 `per_spec` 里。写进表而规范不存在 ⇒ 该检查器一跑就 exit 3，等于把门禁自锁（自举顺序见 `object-audit/references/70-provenance.md`「自举期特例」）。

## 五、升级判据（4 条·全部机判·不许改成人判）

| # | 条件 | 为什么升级 | 初值 |
|---|---|---|---|
| **E-1** | 同一 `spec_id` 的**阻断级**未处置次数累计 ≥ 3 | 同一处反复违规＝不是疏忽，是规范或工具链有系统问题 | 3（待拍） |
| **E-2** | 同一 `spec_id` 的**关注级**累计 ≥ 5 | 长尾噪音会让人关掉门禁，必须上交 | 5（待拍） |
| **E-3** | 任一 `spec_id` 由 **exit 1** 转为 **exit 3** | 规范侧失联＝**提供者**欠账（锚点没了/条款变了），产物方无从自救 | 立即 |
| **E-4** | 任一 `spec_id` **首次**命中（历史零记录） | 可能是新规范只落了文本没落工具，也可能是判据写错了——两种情况都要人看一眼 | 立即 |

**禁止自动降级**：连续 N 次零违规**不得**把某条从①移进②。降级＝改判据＝L0（`10-roles.md「二、决策权分层·判据要改就是 L0」`）。脚本只允许在报告里记一行"该条款连续 N 次无违规"，**不自行改路由**。

**出口③的量**：一次呈拍最多 5 条（超出的按计数降序截断，其余进②并附全量指针）。理由：呈拍是稀缺通道，**一次倒 20 条等于没呈**。

## 六、退出码闭集（可直接当门禁）

| 码 | 含义 | 谁的问题 | 默认出口 | 计绿？ |
|---|---|---|---|---|
| **0** | 通过（零发现） | — | 无（加"总是报告"开关时才写②） | 是 |
| **1** | 违规（≥1 条发现） | **产物方** | 按路由表（①或②，并②） | 否 |
| **2** | 用法错（参数缺／输入路径不存在／找不到规范文件） | 调用方/配置 | ①拦 ＋ ③立即 | 否 |
| **3** | **规范侧失联**（锚点解析不到／锚歧义／条款摘要不符） | **规范提供者** | ①拦 ＋ ③立即（E-3） | 否 |
| **4** | 基础设施错（运行时版本不符／目标不可读／钩子环境异常／路由表损坏） | 工具体系 | ①拦 ＋ ③立即（E-4） | 否 |
| 其他 | 未定义 | — | **一律按 4** | 否 |

四条硬规矩：

1. **3 与 1 必须分开**：处置人不同（提供者 vs 产物作者）。合并成一个"非零"就等于把"规范没人维护"记成"产物不合格"（`object-audit/references/00-skeleton.md「引证失效的七个类型·归属错」`）。
2. **未定义码不得计绿**。这是防"门禁空转变绿"的唯一一道；假绿是本仓最贵的失效形态。
3. **fail-closed**：非 0 默认拒提交。门禁自己坏掉还放行，等于把门禁做成装饰。
4. **显式留痕的绕过**：设环境变量 `ALLOW_GATE_DOWN=1` 时允许提交，但**必须**向②写一条 `{"bypass":true,"reason":"<变量值>","exit":<n>}`。**绕过必须留痕，不是静默**——这既避免环境缺件时逼人用"跳过钩子"（本包纪律明禁），又不给"悄悄绕过"留门。

> 注：本闭集（0/1/2/3/4）管**门禁脚本**；视频团队包 V 轨判据脚本另有一套 0/1/2 语义（R2 §5.3·本团自有设计·「2 不是通过」），两套家族不得互相套用。

## 七、接入（怎么装，不是怎么判）

- 安装器**幂等**：重复执行不产生差异；已存在同名钩子时**不覆盖**，改为提示人工合并（覆盖＝悄悄删掉别人装的东西）。
- 钩子内**一律用显式解释器调用**（如 `bash <script>` / `python <script>`），**不依赖可执行位**——权限位在部分文件系统上不具区分力，靠它会把"装不上"伪装成"已装好"。
- **门禁脚本只读**：不写治理盘、不写部署面、不改被检文件。唯一写动作是②的证据件，且该写动作在**入口脚本**里，不在各检查脚本内（检查器若可写，就多出一个写者）。
- **证据件的归属已定（裁-19）**：运行流水落 `.collab/evidence/`、**不入版本库**；判词属史实锚，落 `.collab/decisions/`、**入版本库**。二者按性质分治，不得混装。实现**不得**为证据缺失开"缺失即放行"的例外；准入闸 A2 的判词指针**只能指向 decisions 侧**，不得指向 evidence。
- **A2 判词机检最小约定（裁-25·主理人定形）**：判词行格式——`【判词】<批次>｜阻塞项：<无|列表>｜判定：<放行|有条件放行|不放行>`。机检**只认**「阻塞项：无」＋「判定：放行」的组合；其余组合（含"有条件放行"）一律算未绿。判词由**独立审计席**出，发布方/生产方不得自写判词自放行（六道硬约束 1）。指针落 `.collab/decisions/`。**判词机检扫描面＝`agent-experts/baigong-software-team/.collab/decisions/verdicts.md` 唯一文件（裁-28）**——判词史与裁决叙事分账，裁决记录里的说明文字凑出放行组合的假绿路径从机制上消除；verdicts.md 缺失＝无判词＝未绿。
- **config 读取语法条款（钩子载体层拆雷）**：凡工序内读取 git config（开工前置对账、交接巡检、门禁人工复点）一律用旗在前只读语法——hooksPath 三读逐字形态＝`git config --local --get-all core.hooksPath`／`git config --get-all core.hooksPath`／`git config --get-regexp "core\.hook"`（三读期望态＝均 exit 1 零读数＝键净）。旗在后形态（键名后直接跟旗）＝git 2.55 语义下写操作＝把旗字面写成键值＝全仓钩子静默解除＝D-102 案型（真盘两度自踩实证见 `agent-skills/fuxi-skill/.collab/qa/2026-11-10-FUXI-FX-U34-QA独立验证-v1.md` §〇）；票面 §头「开工前置对账」引用 config 三读时必逐字照抄上述三条只读命令，禁以键名与旗分隔的简写措辞落命令（照字面落即成写操作＝QA 判词新观察①在册）。

## 八、本件不定义什么

| 不定义 | 去哪 |
|---|---|
| 单条判据长什么样、判什么 | 各规范件的测项段（`object-audit/references/*.md`） |
| 脚本怎么实现、怎么组织 | 执行体自身（本件只约束"不许在脚本里做策略判断"） |
| 发布能不能发、发什么 | `object-build/references/60-publish.md` |
| 规范来源怎么判、exit 3 怎么来的 | `object-audit/references/70-provenance.md` |
| 谁有权改本表 | `10-roles.md「二、决策权分层」`（改判据＝L0） |
