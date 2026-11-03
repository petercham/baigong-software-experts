# SWB-CD1 · 施工票：并发纪律成文（同席多实例禁令＝software-orchestration 派席纪律卷新建＋五席位 MD 守则行＋版本账随动）（施工票·L2·架构席起草·无机件施工目）

- 起草实测 HEAD＝`3b03738`（B 批总收口笔）；开工 ANCHOR＝开工实测 HEAD ≥ `3b03738`，读数附回执开端。
- 裁定链真源（照此成文·交付物内禁引过程件路径＝拍板㊺指针闭集）：
  - `.collab/decisions/2026-11-04-皮总裁定-主理人永不并发派席.md`（`12a3c4a`）；
  - `.collab/decisions/2026-11-04-皮总裁定-并发口径修正-禁同席多实例.md`（`d1c9849`＋随动 `7fbd1ea`＋终态 `10865cf`）——**后生效覆盖先前**，终态口径＝①红线唯一＝**不允许同席多实例并发**（异席并发不禁）；②成文面＝software-orchestration＋席位守则面；③写集互斥、experts 声明面、lease 单实例登记机件方案全部撤销不入题；④并发能力/性能伸缩归 Agent 平台基座（本项目不设计不登记）；⑤**本票无机件施工目**＝纯纪律条款成文。
- 开工附注三项（照录体例）：①誊写禁令（`f5a0d96`）：本票＝新建创作类条款成文＝辖域外自察声明（票内条款文本＝设计供给，施工落盘非搬家）；②票面落位 `.scratch/tickets`（`f135855`）；③era 跨仓口径（不在本票）。
- 计数口径＝occurrence；判据命令自带落盘重定向；负例 exit≠0；token 读数申报四要素（口径 script-v1＋被测 commit SHA＋实测人＋取整 ceil）。

## 现盘落位实测（起草取证·回执须附开工复测）

- 主理人流程域技能＝`agent-experts/baigong-software-team/skills/software-orchestration/`（SKILL.md frontmatter version 1.1.3＋references 十卷）；
- 席位 MD 五件＝`agent-experts/baigong-software-team/agents/software-team-{lead,architect,product,engineer,qa}.md`；token 实测（HEAD `3b03738`·script-v1/ceil）：lead 1412／engineer 1002／architect 873／qa 930／product 813（全部 ≤2500 红线内）；
- 版本三同源现值＝0.1.19（bundle.lock L5／plugin.json L3／.codebuddy-plugin/plugin.json L3）；bundle README 版本账尾行＝v0.1.19（append-only 面）；
- `collab-rules.md`＝fork v1.2.0 逐字下沉件（C3 逐字门保护）＝**本票禁入面**；engineer MD L29 既有条款「一票一新鲜实例、票间串行」＝G1 串行闸机制面（engineer 票型专属·更严），本票零触碰零改写。

## 声明闭集（11 件·本批唯一可写面）

```
1 agent-experts/baigong-software-team/skills/software-orchestration/references/dispatch-discipline.md（新建）
2 agent-experts/baigong-software-team/skills/software-orchestration/SKILL.md（索引行＋触发词/description＋version 1.1.3→1.1.4）
3 agent-experts/baigong-software-team/agents/software-team-lead.md（纪律行段追加一行）
4 agent-experts/baigong-software-team/agents/software-team-architect.md（席位纪律一行）
5 agent-experts/baigong-software-team/agents/software-team-product.md（席位纪律一行）
6 agent-experts/baigong-software-team/agents/software-team-qa.md（席位纪律一行）
7 agent-experts/baigong-software-team/agents/software-team-engineer.md（席位纪律一行·见 CD-D 注）
8 agent-experts/baigong-software-team/bundle.lock（0.1.20）
9 agent-experts/baigong-software-team/plugin.json（0.1.20）
10 agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json（0.1.20）
11 agent-experts/baigong-software-team/README.md（版本账 append 一行）
```

## 逐条施工规格

### CD-A 新建派席并发纪律卷 `references/dispatch-discipline.md`

条款文本定稿如下，施工逐字落盘（本段＝交付条款真源供给·非搬家目）：

```markdown
# 派席并发纪律（dispatch 卷）

> 本卷承载主理人派席与席位实例并发的协作纪律——多席治理问题，非性能调度问题。

## 一 唯一红线

1. **不允许同席多实例并发**：同一席位（席位身份按席位角色名判定；同一席位下实例名带后缀或先后改派的多个实例＝同一身份）同时运行两个及以上实例＝违例。
   主理人派发时该席位存在在途实例＝不得开出同席第二实例；
   席位发现自己处于第二并发实例（同身份重复受派）＝立即停手、不产出、向上报告。
2. **异席并发不禁**：不同席位并发施工/验证＝允许形态；主理人不得以写集互斥、
   保守串行等理由自行加严为串行。性能强弱与开几席的弹性归 Agent 平台基座
   （会话/实例调度层），本专家团不设计、不登记、不承载并发配置条款。

## 二 报告路径卫生（操作定式）

3. 被验/被施工链在途扩展＝先通知在途席补目，禁止补派第二实例写同一报告路径；
   报告件命名族 append-only（v1/v2 族名递增），禁覆写既有史账。

## 三 责任主体与无机件条款

4. 本纪律拦截责任主体＝主理人派席纪律＋各席位守则（第二实例拒产并报）；
   不建登记表、不扩租约机件、不设机械闸——违例处置＝登记健康账，既往不追溯。
```

- 自包含铁律：卷内**零引用**裁定件路径/commit hash/「皮总」措辞（判据 3 断言）。
- 通用开发域纪律口径（不挂具体技能范畴名）。

### CD-B SKILL.md 随动（索引＋触发＋版本）

1. references 索引表追加一行：`| references/dispatch-discipline.md | 派席并发纪律全节（同席多实例禁令·异席并发不禁·报告路径卫生·无机件条款） | 主理人拟派席/考虑多席并发时；席位受派自查实例唯一性时 |`；
2. frontmatter `description` 追加触发短语「／派席并发纪律（同席多实例禁令）」；触发词行追加「同席多实例、并发派席、席位实例唯一」；
3. frontmatter `version: 1.1.3` → `1.1.4`；
4. 体量披露/触发描述须过 `check-skill-meta`（OA-S5/S2）exit 0。

### CD-C 主理人席位 MD 守则行（software-team-lead.md）

「## 纪律行」段末尾追加一行：

```
- 不允许同席多实例并发——派发时该席位存在在途实例即不得开同席第二实例；异席并发不禁、不得自行加严成串行【C 派席并发纪律·dispatch 卷】
```

既有条款（平台红线五条/铁律四条/路由表/脚本清单/纪律行现三行）零触碰。

### CD-D 四成员席位 MD 各一行

architect/product/qa/engineer 四件各在其纪律段（engineer＝「## 席位纪律」段尾；architect/product/qa＝该件纪律/权限段尾，开工以各件实际段名为准·回执登记落位行号）追加统一行：

```
- 不允许同席多实例并发：发现本席位被开第二并发实例＝立即停手不产出并向上报告【席位守则·dispatch 卷】
```

- engineer 注：既有 L29「一票一新鲜实例、票间串行【G1 serial-gate】」＝票型专属机制面，与本行（席位身份级守则）并存零冲突；本行仍加（闭集固定），若回执判定语义重复＝登记不删。
- token 红线：各件追加 ≤150 tok，追加后 `count_agent_tokens.py` 全五件仍须 OK ≤2500（判据 4）。

### CD-E 版本账随动（纪律①）

交付面（skills/＋agents/ 均在 bundle 内）变更→三同源 bump **0.1.19→0.1.20**＋bundle README 版本账 append 一行（内容＝「并发纪律成文＝dispatch 卷新建＋五席位守则行＋software-orchestration 1.1.4·纯条款面无机件」）。

## 验收判据（全部机械可判·自带落盘·负例 exit≠0）

1. **闭集全等**：本批 commit `git show --name-only` 与声明闭集 11 件全等。
2. **条款 occurrence 断言**：`grep -o "不允许同席多实例并发" <五席位MD五件+dispatch卷> | wc -l` ＝ **6**（五 MD 各 1＋卷内第 1 条 1）；异席禁则成文＝`grep -o "异席并发不禁" agents/software-team-lead.md skills/software-orchestration/references/dispatch-discipline.md | wc -l` ＝ **2**；无机件条款＝`grep -c "不建登记表" references/dispatch-discipline.md` ＝ 1。
3. **自包含断言（拍板㊺指针闭集）**：新增/改动七面（CD-A/B/C/D 落盘物）`grep -c "\.collab/decisions\|12a3c4a\|d1c9849\|7fbd1ea\|10865cf\|皮总"` ＝ **0**；负例＝Temp 构造含引用副本 exit≠0。
4. **token 红线前后读数**：`python tools/count_agent_tokens.py "agent-experts/baigong-software-team/agents/*.md"` 前后两跑落盘——前＝基线（873/1002/1412/813/930 复现或按开工 HEAD 实测）；后＝全五件 OK ≤2500 且单件增量 ≤150；回执申报四要素。
5. **SKILL.md 随动断言**：`grep -c "dispatch-discipline.md" skills/software-orchestration/SKILL.md` ＝ **1**；`grep -c "version: 1.1.4"` ＝ 1；`python agent-skills/object-audit/scripts/check-skill-meta.py --root .` exit 0。
6. **门禁零回归＋六演练**：`bash agent-skills/object-audit/scripts/run-gates.sh --root .` → GATE PASS exit 0 对开工基线零新增族；六演练 `SIX_DRILLS_GREEN` occurrence＝1。
7. **版本账**：三同源 grep version 逐处＝`0.1.20`（三值全等）；README diff 仅增行（append-only 断言）。
8. **条款在位负例**：Temp 复制 bundle 骨架删 dispatch 卷条款行 → 判据 2 式重跑 exit 1。

## 禁动面

- `agent-skills/object-audit/` 全域（裁定 §八「object-audit 两面」措辞与 §七终态口径「software-orchestration＋席位守则面」之差＝以 §七收口口径为准·主理人派单已裁＝边界注记入回执，非候裁，object-audit 零触碰）；
- `references/collab-rules.md`（C3 逐字下沉门）；`software-team-engineer.md` L29 既有 G1 条款字面；seat-permissions 两 config 与全部 sop scripts（无机件施工目＝数据面/机件面零触碰）；
- `multi-collab` 技能面（写侧既有条款零动）；`docs/`、`.collab/`（除回执）、`tools/`、`.gitignore`、仓根 README。

## 候裁点

无（范围终态裁定一条即闭环；object-audit 措辞差＝边界注记；性能伸缩归平台基座＝不设计不登记）。

## 票间关系

前置＝B 批总收口（`3b03738` 后呈程·裁定排程款）。后置＝B 批收口登记队列并笔「CD1 健康账口径」一行（主理人）；双席审票＝**串行派发**（裁定 `12a3c4a` §2 实践随动款：先 A 席成笔入库再派 B 席，B 席读到 A 席报告须声明独立口径）。

## 回执

落 `agent-experts/baigong-software-team/.collab/receipts/2026-11-04-SWB-CD1-receipt.md`：开端 HEAD＋name-only 11 件全等＋判据 1–8 逐条读数＋token 前后表（四要素）＋席位行落位行号表＋object-audit 边界注记＋engineer 语义重复登记行（如触发）。交付笔单独 commit（`collab:` 前缀）；禁 `--no-verify`、禁 amend；门禁真拦如实报告不绕闸。

——arch-swbreloc 起草（新建创作类·誊写禁令辖域外自察）。

## 增补注记（append-only·2026-11-04·票面设计注记 1 裁定落笔）

- **object-audit 不入题＝主理人裁定·判据 §七 收口口径**（案内程序裁定·不入拍板台账）：终态裁定原话「只需要纪律限定不允许同席多实例并发就够了」＋§七自述「收口·覆盖前述范围外延」＋YAGNI 无实证缺口不动面（object-audit 现面无派席程序面，挂引用行＝无问题推演造面）；§八「两面」措辞按 §七 读——**不补 rev2、object-audit 零触碰维持**（本票禁动面首行语义自此定案，回执边界注记按此行落）。
