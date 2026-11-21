# QA 判词：视频团审查整改批（票 QA-video-gate-01）

- 验证人：席严过关（software-qa-engineer）·fresh eyes 独立取证（未照抄工程师回执自测；回执仅作对照）
- 日期：2026-10-28
- 被验对象：skills 仓 `D:/multi-agent-collab-skills`、experts 仓 `D:/multi-agent-collab-experts`
- 判据源：`.collab/research/2026-10-28-施工蓝本v1-视频团审查整改批.md` §验收判据 1–7＋§红线＋§边界
- 约束遵守：未修改任何既有文件；临时件仅 `.collab/tmp-qa/`（本轮未需用）；判词为本件唯一新增。

## 开端两仓 HEAD 实测读数

- skills 仓 HEAD = `b188fe2cba613af7aadbc8913f3aebca0c8a4bcd`（＝要求值 b188fe2 ✓）·commit 信息含 WP 编号要素 ✓
- experts 仓 HEAD = `20daf8ed61785bca8dc957e983231870d14b8ae1`（＝要求值 20daf8e ✓）
- skills 仓整改批主体 commit = `f60a521e19d2bf98906fec06dfa9525fe4444cce`（WP1–WP5＋WP6 前置下沉件）；`f60a521` 是 `b188fe2` 的祖先（`git merge-base --is-ancestor` 真）＝HEAD 收口 commit 在同一主线。

---

## 判据 1：两仓 HEAD/commit 对位＋五新 tag＋旧 tag 未变 — **PASS**

**五新 tag 存在且指向 b188fe2**（`git tag --points-at b188fe2` 实测恰此五个）：
```
aigc-video-content@v1.7.0     => b188fe2cba613af7aadbc8913f3aebca0c8a4bcd
aigc-video-governance@v1.3.0  => b188fe2cba613af7aadbc8913f3aebca0c8a4bcd
aigc-video-orchestration@v1.3.0 => b188fe2cba613af7aadbc8913f3aebca0c8a4bcd
aigc-video-release@v1.4.0     => b188fe2cba613af7aadbc8913f3aebca0c8a4bcd
aigc-video-visual@v1.4.0      => b188fe2cba613af7aadbc8913f3aebca0c8a4bcd
```

**旧 tag 指向未变**（`git log -1 --format=%H <tag>` 逐条实测）：
```
aigc-video-governance@v1.2.0   => 4d0614e63cbe82d1ae2df850c4ca25c1acf69e57（＝F01 governance@v1.2.0 commit·整改批之前 ✓）
aigc-video-content@v1.6.0      => 8733bb4d4b5c571a358b6b1daea60d7ea7b1d4e4（＝h06/V6 commit·整改批之前 ✓）
aigc-video-orchestration@v1.2.0 => e2910f22a78cd09f3cd66839e7a580db9bbc1704（＝F03 commit·整改批之前 ✓）
aigc-video-visual@v1.3.0       => d3bc853f9833599a6c31137e80156668f3e25b4e（＝G02 commit·整改批之前 ✓）
aigc-video-release@v1.3.0      => b7676225e4bf6082c39b7f49326929ab95e0cb34（＝G03 commit·整改批之前 ✓）
```
五旧 tag 全部指向各自整改批之前历史 commit 且均为 b188fe2 祖先（`--is-ancestor` 全真）＝**未被 `tag -f` 重打到新 commit**，不可变性合规 ✓。

**登记项（如实·minor 观察）**：experts 仓 HEAD commit（20daf8e）信息自述「五组件 tag→commit 映射随行更新 → b188fe2」，即新 tag 曾于 f60a521、后经收口 commit 重打至 b188fe2。因该五个 tag 均为**本次整改批新建**（非既有不可变 tag），重打不构成对既有 tag 改写；bundle.lock note 内 tag→commit 映射（b188fe2）与实测 tag 指向同源一致。不构成 FAIL，登记为过程性说明。
另注：skills 仓另有三个非本域旧 tag（`content@v1.3.0`/`visual@v1.3.0`/`release@v1.3.0` 无 `aigc-video-` 前缀·指向历史 commit）与 `deep-research@v1.0/.1`，均不在本票范围，指向未受本批影响。

## 判据 2：bundle.lock 三账同源＋bundle 1.7.0＝plugin.json＋perspective 未动 — **PASS**

五组件行逐行对读（lock ref ↔ skills 仓 tag 实测 ↔ 各域 SKILL.md version 行）：
```
governance  ref=aigc-video-governance@v1.3.0 → tag→b188fe2 ✓ | SKILL.md:5 version: 1.3.0 ✓
content     ref=aigc-video-content@v1.7.0    → tag→b188fe2 ✓ | SKILL.md:5 version: 1.7.0 ✓
orchestration ref=aigc-video-orchestration@v1.3.0 → tag→b188fe2 ✓ | SKILL.md:5 version: 1.3.0 ✓
visual      ref=aigc-video-visual@v1.4.0     → tag→b188fe2 ✓ | SKILL.md:5 version: 1.4.0 ✓
release     ref=aigc-video-release@v1.4.0    → tag→b188fe2 ✓ | SKILL.md:5 version: 1.4.0 ✓
```
- bundle 版本行：bundle.lock `"bundle.version" = "1.7.0"` ✓；plugin.json（`.codebuddy-plugin/plugin.json:3`）`"version": "1.7.0"` ✓ 两值同源。
- perspective 行未动：`git diff f7cd951..HEAD -- bundle.lock` 输出中 grep perspective **零命中**（ref 仍 `aigc-video-perspective@v1.2.0`→2be5308，SKILL.md version 1.2.0 三账自洽）。
- README.md:27 版本账含 1.7.0 整行（六 WP 要素＋「席位动＝导演席预检契约」注记）✓。

## 判据 3：门禁独立复跑 — **PASS**

- skills 仓 `bash tools/run-gates.sh` → 末两行读数：`check-source-of-truth: 模式 dual｜文件 98（agents 7＋skills 91）｜BLOCK 0（新命中 0）｜基线豁免 54｜指针 WATCH 333｜exit 0`；`run-gates(skills 仓薄启动器)：适用项 1（SOT 双根对账）｜exit 0`。**SKILLS_GATES_EXIT=0** ✓
- devkits 仓 `bash deliverables/skills/object-audit/scripts/run-gates.sh` → `GATE PASS（发现 387 条，均按路由表走②不拦提交）`＋SOT 行 `BLOCK 0（新命中 0）｜exit 0`。**DEVKITS_GATES_EXIT=0** ✓
- **ANCHOR 登记**（devkits run-gates.sh spec-provenance 头）：MC-GATE-1 anchor「本件正文的 json 围栏是唯一机器源」sha256=0ff571c0…·MC-GATE-2 anchor「门禁脚本只读」sha256=64e5d90d…·MC-GATE-3 anchor「显式留痕的绕过」sha256=ce35d452…·spec_version 3.9·effective 2026-10-23。三锚在位未篡改。

## 判据 4：token 实测（script-v1·ceil·被测＝两仓 HEAD 工作树·实测人＝席严过关） — **PASS（含登记项）**

帽内实测：
```
aigc-director.md（导演 MD·含预检条款后）        = 2461 ≤ 2500 ✓
handoff-ledger.md（新·governance）             = 1596 ≤ 2500 ✓
director-self-check.md（新·visual）            = 1098 ≤ 2500 ✓
shot-plan-approach.md（新·visual·WP6 下沉件）   = 686 ≤ 2500 ✓
```
涉改既有件读数照登：
```
orchestration-steps.md      = 2640 （OVER 预防线·见下口径注）
confirmation-gates.md       = 2320 OK
asset-registry.md           = 2475 OK
narrative-continuity-criteria.md = 2379 OK
script-chain.md             = 1881 OK
script-chain-per-artifact.md = 1790 OK
storyboard-script-spec.md   = 2169 OK
consistency-gate-checks.md  = 2425 OK
```
口径注：蓝本验收判据 7 帽＝「全部**新增** references ≤2500」（三新件 1596/1098/686 全帽内 ✓）；orchestration-steps 2640 属**既有涉改件**超 2500 预防线——按蓝本判据 7 口径属登记项非 FAIL（HEAD commit 信息亦自述该回落 2808→2640 与口径）。如实照登为 minor 登记项。

---

## 判据 5：语义红线 grep 独立取证 — **PASS**

1. **导演判定权栏含「无放行权」**：aigc-director.md:39 现文＝`**打回权（负向拦停）·无放行权**——…放行点唯一性不动`；:52 预检契约行含 `**打回权＝负向拦停权，非放行权**` ✓（HTML 注释照录原文「无（仅自检，不构成放行）」＝append 纪律允许注记式改写 ✓）
2. **「唯一放行点」运营表述两处未变**：experts 仓命中恰两处＝aigc-operations.md:28（放行/退回判定（唯一放行点））＋aigc-video-team-lead.md:25（唯一放行点＝运营）。`git diff f7cd951..HEAD -- agents/aigc-operations.md agents/aigc-video-team-lead.md` 输出行数＝**0**（两文件整文件零动）✓。skills 仓既有两处（episode-beat-templates.md:73／iron-laws.md:37）：iron-laws.md 整文件零 diff；episode-beat-templates.md 涉改 diff 面仅 :57 一处术语改（分场大纲→逐场大纲），:73 放行表述行零动 ✓
3. **G2 硬闸对象＝文学剧本定稿表述未变**：confirmation-gates.md:27 `G2 剧本闸：对象＝**文学剧本定稿**（文学作品·前体料源）…` 与整改批前基线（`git show f60a521^` 同文件:27）逐字同文；`git diff f60a521^..HEAD` 中含「文学剧本」的增行全部属**新增 WP2 追加节**（:50/:53），其中 :27 既有行零命中 diff ✓。新增 A4–A7 文本自证「G2 硬闸对象不变＝文学剧本定稿，A4–A7 为呈闸前置读数，不构成新闸、不判语义」✓
4. **通则5 文本零动**：script-chain.md:38 通则5 行与基线（f60a521^ 该文件:31）逐字同文；diff 中含「通则5」的增行仅为注记/挂账节标题（均自述「通则5 零改动」）✓。铁律件 iron-laws.md 整文件 diff 行数＝0 ✓
5. **`grep -r 逐场大纲` 主名命中分布**：skills 仓 18 命中／7 文件（script-chain、script-chain-per-artifact、screenplay-craft、episode-beat-templates、content SKILL.md、confirmation-gates、director-self-check）＋experts 仓导演 MD:48 ✓。**「分场大纲」残留恰两处**：① script-chain.md:8 别名注记本体（「别名＝分场大纲／…——**别名仅此注记一次**」＝蓝本所定恰一处 ✓）；② content SKILL.md:3 description 触发词列「…逐场大纲、分场大纲…」。**登记 minor**：触发词列含别名属检索面用法，非正文术语主名违例；若从严解读「别名注记恰一处」，此为第二处出现——如实登记为 minor 观察项，不判 FAIL（正文层注记确恰一处）。
6. **无新增语义判定权措辞（六 WP 新增段抽读）**：handoff-ledger.md:10「本账不产生任何判定效力…放行点仍唯一＝运营席＋人类确认闸」＋:48「本件不设任何席位的内容判定权」；confirmation-gates.md WP2 节「零新增席位语义判定权」「只判形状/读数，不判值好坏」；director-self-check.md:4「无放行权」＋:27「打回＝负向拦停权，不是放行权」；narrative-continuity-criteria.md WP3 节为读取义务非判定权。全部新增段无「放行／判定内容好坏」语义授权 ✓

## 判据 6：单真源验证 — **PASS**

- **交接账本体只在 handoff-ledger.md**：`grep -rln 'criteria_ref'` 两仓全扫＝命中文件**仅** handoff-ledger.md 一件。其余处全为指针：asset-registry.md:76（「本体单真源＝同域 handoff-ledger.md…本件不重述——防两处真源」）、orchestration-steps.md:13/21/46（⛓ 指针行）、confirmation-gates.md:53（⛓）、narrative-continuity-criteria.md:53（⛓）、aigc-director.md:52（⛓ 全路径指针）。打回票契约要素（判据引用＋轮次账＋超轮升级人类仲裁）闭集定义只在 handoff-ledger.md §二/§四成文 ✓
- **自检判据本体只在 director-self-check.md**：形状项清单＋圣经比对表＋执行体裁仅此一件；visual SKILL.md:25 索引行＝摘要＋装载时机，导演 MD ⛓ 指针一行 ✓
- **导演 MD 下沉段与 shot-plan-approach.md 语义对读（下沉零变）**：QA 自建对读（tmp-qa/director_old.md=f7cd951 版导演 MD vs 下沉件 :7-16）六条方法细则 bullet（Core creative challenges／Visual style／Toolchain／生成-筛选-重生成迭代／G3 提示词定稿闸／G4 生成预算闸）**逐字等值**；唯一差异＝⛓ 行指针措辞「见 `skills/…/shot-generation.md`」→「见同域 `shot-generation.md`」（引用改写·细则本体零变；该逐字孤儿 bullet 本体仍在 shot-generation.md 不复制＝防两处真源注记在位）✓。三新件在 f60a521→b188fe2 收口 commit 间零 diff ✓

## 判据 7：悬空指针零容忍 — **PASS（含既有项登记）**

- QA 自建解析器（tmp-qa/ptr_check.py）扫 12 涉改件全部反引号 `*.md` 基名指针＋全路径指针：`checked 12 files; missing = 0`＝**悬空零命中**（含跨域指针 storyboard-script-spec／generation-materials-and-degradation／shot-generation／qc-and-criteria／self-check／topic-brief／handoff-ledger 等目标文件全部在位）。
- 导演 MD 三新 ⛓ 指针目标在位：`skills/aigc-video-governance/references/handoff-ledger.md`✓／`skills/aigc-video-visual/references/director-self-check.md`✓／`skills/aigc-video-visual/references/shot-plan-approach.md`✓（＝蓝本验收判据 2「指向 WP5/WP1 件零悬空」一并过）。
- SKILL.md 索引登记：governance SKILL.md:21（handoff-ledger）／visual SKILL.md:20+25（shot-plan-approach、director-self-check）均入索引 ✓
- **跨仓指针写法**：本批新增跨仓指针＝导演 MD → skills 域全路径写法（skills/… 前缀·无反引号包裹跨仓基名）符合通例。机检扫出 orchestration-steps.md 内 6 个反引号包裹的 experts 席位基名（`aigc-director.md` 等）＝**全部为整改批前既有行**（`git diff f60a521^..HEAD` 该模式增行零命中；旧版已含），属存量写法非本批引入，登记为既有项（SOT 门禁对其判「指针 WATCH 不 BLOCK」口径）。

## 判据 8：术语裁定落地抽读 — **PASS**

- **scene_by_scene_outline 主名统一**：主名「逐场大纲」落位 7 件＋导演 MD（见判据 5.5）；「分场大纲」残留仅别名注记一处＋SKILL.md 触发词列（见判据 5.5 minor 登记）；script-chain-per-artifact.md:4 / screenplay-craft.md:18 / episode-beat-templates.md:57 涉改处均已改主名并注「v1.7.0 术语主名统一」✓
- **treatment 别名＋synopsis 防混注记在场**：script-chain-per-artifact.md:24＝「treatment 行业＝『故事详述』（详述稿／创意阐述稿同族读法）。**防混**：本件 `synopsis` 为 schema 字段名，**≠行业 synopsis**（后者＝资方摘要体裁）」✓
- **外部文档单集粒度主张入候补池挂账文本在场（content 域）**：script-chain.md:40-42 挂账候补池节＝「外部术语文档主张『系列 IP 可按单集粒度产 story_outline/treatment』——与我方通则5 冲突，**不采纳、通则5 零改动**；登记候补池，出池条件＝系列化重度生产实际暴露该需求」✓；:28 单集按单件走注记（皮总裁定①）在场 ✓；链注吸收外部设计理由（script-chain.md 主名〇节＋挂账节描述，不带外部路径——涉改件 grep 无外部文档路径引用）✓

## 判据 9：边界验证（不做项＝确未做） — **PASS**

- **无新席位**：plugin.json diff（f7cd951..HEAD）仅 version 行 1.6.3→1.7.0，`members` 段 diff 命中 0（members:86 起整段零动）；agents/ 目录 diff --stat 仅 aigc-director.md 一件（6+/11-）✓
- **α 未动**：`git diff f7cd951..HEAD -- agents/aigc-production-designer.md` 输出行数＝**0** ✓
- **scene_purpose 未引入**：两仓 grep 命中＝1 处，且为 script-chain.md:43 挂账不采口径（「`scene_purpose` 新字段（候 schema 真源核对另票）」＝登记不落地）✓
- **市场源/缓存未碰**：`C:/Users/peter/.workbuddy/plugins/marketplaces/my-experts/plugins/hjh-aigc-video-team/.codebuddy-plugin/plugin.json:3` 实测 `"version": "1.6.3"`（旧态保持）；该缓存目录 grep「打回权」零命中＝本批席位变更未泄漏入市场面 ✓
- 其余不做项旁证：G2 闸表/DAG×闸既有节零动（confirmation-gates.md WP2 节注释自证＋diff 行面核验＝全部增行为追加节）；不引入单集粒度（通则5 行零动·判据 5.4）。

---

# 总判

## 逐判据三态汇总
| 判据 | 判定 |
|---|---|
| 1 两仓 HEAD/tag 对位＋旧 tag 未变 | PASS |
| 2 bundle.lock 三账同源＋1.7.0 双同源＋perspective 未动 | PASS |
| 3 两仓门禁独立复跑 exit 0（ANCHOR 已登） | PASS |
| 4 token 帽＋涉改件读数照登 | PASS（登记项：orchestration-steps 2640） |
| 5 语义红线 grep 取证 | PASS（minor：触发词列别名第二处） |
| 6 单真源三对 | PASS |
| 7 悬空指针零容忍 | PASS（既有项登记：跨仓反引号 6 处为存量） |
| 8 术语裁定落地 | PASS |
| 9 边界不做项 | PASS |

## 问题登记（如实·含 minor，均不拦）
1. **[登记项] orchestration-steps.md token＝2640**＞2500 预防线——蓝本验收判据 7 帽＝新增件，既有涉改件超预防线按口径属登记非 FAIL；HEAD commit 已自述回落 2808→2640。建议后续拆件票处置。
2. **[minor] content SKILL.md:3 触发词列含「分场大纲」**——正文层别名注记确恰一处（script-chain.md:8），触发词列属检索面；从严口径下为别名第二处出现，登记备查。
3. **[过程说明] 五新 tag 曾打 f60a521、收口重打 b188fe2**——均系本批新建 tag，非既有不可变 tag 改写；lock note 映射（→b188fe2）与实测同源。合规，登记。
4. **[既有项] orchestration-steps.md 内 6 个反引号跨仓席位基名指针**——整改批前存量写法，本批零新增；SOT 门禁 WATCH 口径不 BLOCK。

## IS_PASS = **是（放行）**

全部九判据 PASS，无 FAIL 级缺陷；四条登记/minor 项均不构成回修理由。

## 路由建议
**放行装配段**（Send To: NoOne / 主理段四段链可继续）。无需回修工程师。遗留登记项 1（orchestration-steps 2640）与 2（触发词别名第二处）建议随下张例行票处理，不阻塞本批。

—— 席严过关（software-qa-engineer）· 票 QA-video-gate-01 · 2026-10-28

