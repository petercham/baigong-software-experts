# SWB-ES2 · 施工票：合并收账小票（ES §四-1 席位卡面随动 ＋ QA N-2 门禁路由处置判定）（施工票·L2·架构席起草）

- 起草实测 HEAD＝`7acbbca`（CD1 收口登记笔）；开工 ANCHOR＝开工实测 HEAD ≥ `7acbbca`，读数附回执开端。
- 挂账真源（回原文直核·非转述）：
  - **目一**：ES 终态收口登记 `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-ES-工程规范定标-终态收口登记-v1.md` §四-1「席位卡写域延伸：主理人卡誊录权明文（`.collab/decisions/`）＋架构席卡 `docs/adr/` 落盘写权（原位插改）」；T08R-A1 回执 L31（A1① 既裁＝席位卡面句不入 T08R 批、归 ES §四-1 卡面随动票）；T08R-A1 收口登记 L31（R⑥ 席位卡纪律句同归此票）；R⑥ 原义＝T08R 票面 L127「engineer/QA 席位卡是否增『按项目约定 md 严格遵循分层写入/校验』纪律句（裁定三③执行规范的卡面承载）」。
  - **目二**：QA N-2 定义＝ES v3.1 §二 L62 行「QA N-2（门禁缺省面不含 docs＝adr advisory 非常驻）归门禁路由裁量（60-gates 路由表加 `check-pointers --scope docs/adr` 类挂载属路由表改写职权）；advisory 补偿断言先随 E-ADR-3″ 校验批常驻，路由加挂后升常驻」；后置队列在册＝B 批总收口登记 §六-2。
- 开工附注三项（照录）：①誊写禁令 `f5a0d96`（本票＝条款句插入＝创作类辖域外自察）；②票面落位 `.scratch/tickets`；③era（不在本票）。
- 计数口径＝occurrence；判据自带落盘；负例 exit≠0；token 读数申报四要素（script-v1＋SHA＋实测人＋ceil）。

## 现盘落位实测（起草取证·回执附开工复测）

- 五席位卡 token 现值（HEAD `7acbbca`）：lead 1474／architect 921／engineer 1049／qa 978／product 860（全 ≤2500，追加余量充足）；
- **数据面已先行**（卡句＝誊录明文非新权）：seat-permissions.json host 行 write_globs 已含 `.collab/decisions/`（L13）；architect 行 write_globs 已含 `docs/adr/`（L33）＝卡面明文与 config 现面对表，两 config 本票零触碰；
- engineer/qa 卡既有纪律段（「## 席位纪律」段）在位；卡面执行规范无「按项目约定 md」句（R⑥ 缺口实证）；
- N-2 机理取证：全 7 项目 `docs/adr/` 目录存在数＝**0**（无首支 ADR）；`check-pointers.py --scope <不存在/空目录>` 实测＝`infra error: 扫描域内没有任何 .md` **exit 4**；run-gates.sh SCRIPTS 清单项形态＝仅「裸名」/「ROOT/ 相对路径」两种（L131–143），**不支持 per-script `--scope` 参数注入**；60-gates 路由表 `per_spec` 现面无 adr 族 spec_id。

## 声明闭集（8 件·本批唯一可写面）

```
1 agent-experts/baigong-software-team/agents/software-team-lead.md（誊录权明文一句·纪律行段尾）
2 agent-experts/baigong-software-team/agents/software-team-architect.md（docs/adr/ 写权句·写域行原位插改）
3 agent-experts/baigong-software-team/agents/software-team-engineer.md（R⑥ 纪律句·席位纪律段尾）
4 agent-experts/baigong-software-team/agents/software-team-qa.md（R⑥ 纪律句·席位纪律段尾）
5 agent-experts/baigong-software-team/bundle.lock（0.1.20→0.1.21）
6 agent-experts/baigong-software-team/plugin.json（0.1.21）
7 agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json（0.1.21）
8 agent-experts/baigong-software-team/README.md（版本账 append 一行）
```

（product 卡零触碰＝ES/R⑥ 均不涉产品席；60-gates／run-gates／scripts／两 config 零触碰＝目二判据见下。）

## 逐条施工规格

### ES2-A 目一：卡面执行规范随动（ES §四-1＋R⑥）

条款句定稿（＝交付真源供给·施工逐字落盘；与 CD1 席位行体例同构＝短声明＋方括号挂注）：

1. **lead 卡**「## 纪律行」段尾追加：
```
- 裁决/裁定登记誊录唯一落位＝所属项目 `.collab/decisions/`——皮总口径逐字登记、append-only、他席零改写；主理人不产裁决本体【表2-1 host 行誊录权明文】
```
2. **architect 卡**写域行（「- 写域：」行）**原位插改**：行尾追加「、`docs/adr/` ADR 落盘写权（编号四节形态随 ES 定标）」（该行其余逐字不动；「明确不可写」行 `docs/` 字面＝表2-1 转录面零动——与机械面分层纪律在册）。
3. **engineer 卡／qa 卡**「## 席位纪律」段尾各追加同一句：
```
- 分层写入按项目约定 md 校验：项目 `docs/STRUCTURE.md` YAML 块＝项目根与交付路径唯一真源，交付面写入域外即停手呈报【裁定三执行规范·project_domain_md 载 surface】
```
   （注：句内「载 surface」若施工席判中英混排不雅＝改「承载面」，改动入回执一行，语义零动。）
4. 注册面纪律自查：卡句与 config 现面对表（判据 3）——本票**不新增任何权限语义**＝纯明文随动。

### ES2-B 目二：QA N-2 处置判定＝条件化缓挂（本票零机件零文档施工·主理人裁）

本席判定（YAGNI 论证·会师裁「票内论证或回执申报均可」之票内侧）：

1. **前置面全空**：`docs/adr/` 全项目存在数＝0、首支 ADR 未生、E-ADR-3″ 校验批未启动——N-2 系 ES v3.1 明文**后置条件项**（「先随校验批常驻，路由加挂后升常驻」）。
2. **直接加挂＝门禁自爆（机理实证）**：check-pointers 对空/不存在 scope＝infra error exit 4（实测），run-gates 对 exit 4 走 `on_infra_error` 升级＝路由此刻加挂必拦；且 run-gates SCRIPTS 形态不支持 `--scope` 参数＝加挂需 run-gates 参数化挂载机制先行＝为 0 条目面造新机件面＝违 YAGNI。
3. **路由表不预挂占位行**：`per_spec` 的 spec_id 须能在提供者规范件解析（读表规则 5＝解析不到 exit 3）＝无 adr spec 源，占位行＝违 60-gates 自纪。
4. **处置＝转条件化缓挂登记**（触发双前置在册：①首支 ADR 落入项目 `docs/adr/`；②触发批同批实装 run-gates 挂载形态（裸名/ROOT 形态扩参或 scope 包装脚本）＋E-ADR-3″ 补偿断言随批常驻）。落账＝B 批后置队列收口登记一行（主理人落笔），本票 60-gates/run-gates 零触碰。
5. 若主理人裁「至少文档面落一行」：候选＝60-gates §八（本件不定义什么）补「adr 挂载＝条件化缓挂在册」注记行——闭集加至 9 件，**由主理人裁后随 rev/回执定**，本票缺省不带。

### ES2-C 版本账随动（纪律①）

席位卡面＝bundle 交付面变更→三同源 bump **0.1.20→0.1.21**＋README 版本账 append 一行（内容＝「ES §四-1 卡面随动＝lead 誊录权明文＋architect adr 写权句＋engineer/qa 分层纪律句·纯明文面 N-2 零机件」）。

## 验收判据（全部机械可判·自带落盘·负例 exit≠0）

1. **闭集全等**：本批 commit `git show --name-only` 与声明闭集 8 件全等。
2. **条款 occurrence**：lead 卡 `grep -c "\.collab/decisions/"` ＝ **1**；architect 卡 `grep -c "docs/adr/"` ＝ **1**（写域行新插）；「分层写入按项目约定 md 校验」engineer+qa 两卡 `grep -o | wc -l` ＝ **2**；product 卡三串命中均＝0（未涉席零染断言）。
3. **数据面对表断言**（防卡面造新权）：python 抽取 lead 卡句路径串 ⊆ host write_globs、architect 卡新句路径串 ⊆ architect write_globs（config 现面 grep 命中在册：L13/L33）＝双真 exit 0；两 config `git diff` 空。
4. **纯增行断言**：四卡 diff＝各仅插入（lead/engineer/qa 各 +1/−0；architect 写域行 1 行改＝±1 行且旧行全文为新版前缀包含——`git diff -w` 核验）；product/其余文件零出现。
5. **token 红线前后**：`python tools/count_agent_tokens.py "agent-experts/baigong-software-team/agents/*.md"` 前后两跑落盘——前＝基线 921/1049/1474/860/978 复现；后＝五件全 OK ≤2500 且单件增量 ≤120；回执申报四要素。
6. **门禁零回归＋六演练**：run-gates GATE PASS exit 0 对开工基线零新增族（卡面短句＝OA-D6 叙述面预期 Δ 登记归因，非新增族）；六演练 `SIX_DRILLS_GREEN`＝1（盘符口径）。
7. **版本账**：三同源单行 version 全等 `0.1.21`（`grep '"version"'` 取单行口径）；README diff＝+1/−0。
8. **负例**：Temp 复制 engineer 卡删纪律句 → 判据 2 式重跑 exit 1。

## 禁动面

- seat-permissions 两 config（数据面已先行＝本票零触碰）；`agent-skills/multi-collab/references/60-gates.md` 与 `agent-skills/object-audit/scripts/run-gates.sh`＋全部 scripts（N-2 零机件判定＝目二施工面空）；`docs/` 全域（adr 目录**不造**——空目录无 git 实体且造之即预挂 N-2 前置）；software-orchestration/sop 技能正文；product 卡；CD1 dispatch 卷；`tools/`、`.gitignore`、仓根 README、`.collab/`（除回执）。
- 卡面既有各行（含 architect 卡 L22 `.collab/tickets/` 旧代字面＝**登记级观察申报**：属 B3 后卡面残留，候补池口径同 CD1 收口黄-3，本票不吞并不顺手改）。

## 候裁点

无（目一＝ES §四-1＋R⑥ 既裁执行；目二＝本票判定「条件化缓挂」呈主理人裁一行——裁「文档面补一行」则闭集+60-gates 随 rev/回执定，属裁后随动非候裁回流）。

## 票间关系

前置＝B 批总收口＋CD1 收口（`7acbbca`）。后置＝主理人收口登记落 N-2 条件化缓挂一行（触发双前置在册）＋architect 卡旧代字面候补池随账。双席审票＝**串行派发**（`12a3c4a` §2 款沿用）。

## 回执

落 `agent-experts/baigong-software-team/.collab/receipts/2026-11-04-SWB-ES2-receipt.md`：开端 HEAD＋name-only 8 件全等＋判据 1–8 读数＋token 前后表（四要素）＋卡句落位行号表＋「承载面」择词登记行（如触发）＋N-2 判定引用面＋architect 旧代字面观察申报。交付笔单独 commit（`collab:`）；禁 `--no-verify`、禁 amend；门禁真拦如实报告不绕闸。

——arch-swbreloc 起草（新建创作类·誊写禁令辖域外自察）。
