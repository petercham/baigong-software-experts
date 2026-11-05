# CLN-PURE 净化终态 QA 验收报告 v1（qa-clnv 席·fresh eyes·独立证伪）

- 被验面＝`D:\multi-agent-collab-devkits-build\baigong-software-team\`（新装配面·工程师自报 78 文件·bundle@a885ad7）；旧面挪存＝同目录旁 `baigong-software-team.pre-cln-old\`（本席只登记存在性，零触碰）。
- 开工实测：`git rev-parse --short HEAD`＝`d978b5a`（main）＋`git status --porcelain` 净；核验过程中 HEAD 前移至 `a0f3ee7`（回执补账笔·bundle 子树 diff＝仅回执件一件，装配面字节不受影响，见 §七-5）。
- 北极星验收标准（决策者 2026-11-05 口径·本次验收唯一准绳）原文：装配（编译）产物＝面向 LLM 执行的内容本体，必须**干净、零过程痕迹，不给部署后 LLM 执行带来任何噪声**——不得含开发过程叙事（版本逐版账/案卷/沿革/验收探针实体/指向装配面不存在文件的引用）。
- 工程师自报读数零采信：全部本席亲自实跑；扫描器本席自写（`qs_scan.py`／`qs_dangling.py`，occurrence 口径逐 pattern 逐笔落账）。禁读另一席旧核验件＝零读；未复用工程师任何脚本。

## 总裁决：**放行②预览挂卡**（红 0／黄 2／绿 12·观察 5）

黄两项均为票面白名单④预登记＋跨仓禁写残余（非本批违例），不构成不放行；详见 §四。

---

## §一 对账（绿-1）

- 两笔施工 name-only 并集实数＝**43**（8418b3a 6 件＋a885ad7 37 件，无交集重复）；与票面声明闭集 43 件 **diff 全等**（`diff` 零输出）。闭集外零触碰。
- reflog 精确动作扫描：`grep -E 'amend|reset:|rebase|checkout'` 命中全部为 commit 消息体引语（「零amend」字样）与 checkout 迁移动作，**零 amend／零 reset 动作**。
- tag：`git tag -l "external-advisor-collab@*"` 含 `external-advisor-collab@v1.1.3`；解析锚＝`8418b3acb8b1392cd214daaad31dc0b34580b0ba`（annotation 型）＝票面 S8 指定（S2 落定 commit）。两笔均为 HEAD 祖先（`merge-base --is-ancestor` 双真）。
- 三同源读数：`plugin.json`＝`0.1.24`、`.codebuddy-plugin/plugin.json`＝`0.1.24`、`bundle.lock bundle.version`＝`0.1.24`；EAC `SKILL.md frontmatter`＝`version: 1.1.3`；`bundle.lock` EAC 行 `ref`＝`external-advisor-collab@v1.1.3`。全部同钉 ✓。

## §二 装配重跑（绿-2）

- 本席未删现面（避免破坏被验对象），改用 `--out` Temp 全新装配复跑全链：`publish.py --assemble agent-experts/baigong-software-team --out /tmp/...` exit 0「已装配（第 1 块，78 文件）」；全新面文件清单与现面清单 `diff` 全等、内容逐文件 sha256 全等（除两账件外 BYTE_IDENTICAL）。A0「删旧重装」效果经全新装配独立等价复现。
- 现面幂等复跑：`publish.py --assemble agent-experts/baigong-software-team` → exit 0、「装配面已一致（第 1 块，78 文件），零写入」；复跑前后全面 sha256 摘要逐字节全等（80 文件）。
- 文件总数实数＝**80**＝78 内容件＋2 装配元数据账件（COPY.state＋ASSEMBLY.manifest.json）——与回执补账笔 110−32＝78＋2 账件口径对账成立；COPY.state 末块 files 条目＝78 ✓。
- 五类被裁件 find 读数（现面与全新面双跑同值）：根 `README.md`＝0、`docs/SWB-交接件*`＝0、`skills/deep-research/README.md`＝0、`skills/external-advisor-collab/references/90-changelog.md`＝0、`tests/` 目录＝0。
- `.collab`／`.scratch` 混入＝**0**（`find -name/-path` 双口径）；`__pycache__`/`*.pyc`＝0（本席 py_compile 产生的残留已清，终面摘要与开工快照逐字节全等）。

## §三 北极星终态扫描（绿-3/4/5·本席自写扫描器·occurrence 口径）

全面 74 个文本文件（排除 png）逐 pattern 读数：

| pattern | occ | 判因归档 |
|---|---|---|
| `multi-collab` | **0** | — |
| `SWB-` | **0** | —（附：空格形态 `SWB v2.9`＝13 处＝版本命名词汇本体，档②） |
| `TKT[0-9]` | **0** | — |
| `90-changelog` | **0** | — |
| `test_enforcement` | **0** | — |
| `probe-report`/`probe-results` | **0** | — |
| `D:\\` 盘符 | 1 | ASSEMBLY.manifest.json 账件字段＝白名单⑤（账件不扫·票口径3⑤）→档② |
| `.collab/[a-z]+/名.(md\|json)` 实指 | 0；宽式 1＝ticket-template `<票ID>` 占位符 | 运行时词汇＝档①白名单① |
| `[0-9a-f]{7,8}\b` 原式 | 184 | 见 A4 分账 §五，违例 0 |
| 独立 7-8 位 token（带边界式） | 8 | 全部豁免（§五逐笔） |
| `V1[0-3] L` | 4 | 两基线副本头注段切句 2＋arch copy 正文钉死段 `V10 L104`/`V10 L54` 2＝白名单②（票面 S3 保留字面闭集＋预登记命中逐字对上）→档① |
| `版本账` | 8 | 全部＝「版本账由仓侧维护、不随包分发」自包含陈述（PRODUCT L12/L73/L78、ARCH L173/L177/L217 等）＝档②运行时词汇 |
| `案卷` | 8 | EAC 讨论会纪律条款词汇＋SOP 规范条款词汇（dev-discipline 闭集句/handoff 过程编号定义/baseline 副本钉死段）＝档② |
| `沿革` | 16 | 「沿革件不随包」自包含句（S2/S6 修法产物）＋基线副本钉死段纯度条款本体＝档①/② |
| `候裁` | 24 | SOP 运行时概念（handoff-discipline §十一候裁面闭集／候裁 Q-02/04/05 条款锚／模板字段）＝档② |
| `皮总` | 32 | 全部在 EAC 技能条款本体（§二 皮总（决策者席）角色定义／「2026-10-26 皮总裁定」条款出处锚／deploy-gate 四段口径锚）＝档②技能规则内容，非百工开发过程叙事（观察-2） |

**三档分账总读数**：档①（基线副本钉死条款文本/头注段切句·豁免逐笔＝V1[0-3] L 4＋白名单② hex 4＋`.collab/tickets` 词汇命中含于 arch copy 19）＋档②（运行时词汇/权限 glob 本体＝版本账 8＋案卷 8＋沿革主体＋候裁 24＋皮总 32＋`.collab/` 权限 glob 枚举行等）＋档③（过程叙事/悬空引用违例）＝**0**。

### 悬空引用独立复核（本席自写解析器）

全面路径样 token 抽取＝110 条直接解析可达（OK）＋49 目录前缀引用（权限 glob 本体）＋4 占位符＋4 条无扩展名词汇＋4 条 DANGLING 候选逐判：

1. `skills/deep-research/SKILL.md:69` `references/30-discipline.md §五`＝跨技能引用带技能名限定（「external-advisor-collab 技能 references/…」），装配面内 `skills/external-advisor-collab/references/30-discipline.md` §五 实存在位→可解析，档②（deep-research 跨仓真源禁写）；
2. `skills/deep-research/references/quality-gates.md:9` `evals/routing-evals.json`＝技能根口径可达（`skills/deep-research/evals/routing-evals.json` 在位），同目录口径落空→松散形态登记（黄-2）；
3-4. 模板两件 `scripts/decision-pack.py`/`scripts/state-transition.py`＝sop 技能根口径可达（`skills/sop/scripts/` 两件在位），模板叙述运行时词汇→档①白名单①。

**hooks 执行链解析**：hooks.json 三脚本 `../skills/sop/scripts/{commit-audit,memory-neutralize,write-guard}.py` 自 hooks/ 解析全部在位 ✓。

**deep-research 消费侧 README 悬垂四处（票面白名单④预登记·本席独立复现）**：`references/methodology.md:3`、`references/domains/film-tv.md:3`、`references/domains/_new-domain-template.md:3`、`scripts/verify_citations.py:10`（「登记见 README」类指向句，README 已被裁出）＋MIT 义务残余载体在位读数＝verify_citations.py 头注 L3–11（原作仓库 URL＋MIT 许可＋克隆 hash 40 位＋派生作品声明句）全在位 ✓。跨仓禁写＝不可修，登记（黄-1）。

### LLM 视角抽查（随机 5 交付 MD）

`agents/software-team-lead.md`（frontmatter+守则）、`skills/software-orchestration/references/standard-sop.md`、`skills/sop/references/collab-fixed-structure.md`、`skills/software-orchestration/references/handoff-discipline.md`、`skills/external-advisor-collab/SKILL.md`：头注全部为「承载/出处/自包含」式现行效力陈述；无「第几轮改成这样」、无案号施工叙事、无指向缺件的执行指令。EAC 40-artifacts L85 新指针 `../../software-orchestration/references/handoff-discipline.md` §三 装配面解析可达且该节确载三正面判据（§三 三正面判据（决策/设计类交接件）①引用闭集可达②无第三方过程痕迹③状态词只述现行效力）✓。**无让执行期 LLM 困惑的过程叙事。**

## §四 黄项（2·均为预登记残余非新增违例）

- **黄-1**＝deep-research 消费侧 README 悬垂引四处（白名单④预登记·MIT 义务载体·跨仓禁写不可修）＋MIT 义务残余载体裁出后在位读数已附。残余风险携往④部署段：若 MIT 义务要求随包许可声明，需 deep-research 跨仓修票把义务声明内联到 SKILL.md/头注（本席建议④段前处置）。
- **黄-2**＝deep-research 包内两指代松散式（SKILL.md §七 跨技能引用无路径段·quality-gates.md `evals/…` 技能根口径才可达）——装配面均可解析、执行期无歧义阻断，但形态严于北极星口径应内联；同属跨仓真源禁写面，登记随黄-1 一并携往④段。

## §五 A4 hex 分账（绿-6·逐笔判因）

原式 184 出现分账：COPY.state 161＋ASSEMBLY.manifest.json 3＝账件不扫（白名单⑤）；`66e02d23…` 5 段＝40 位 MIT 克隆 hash 子串（verify_citations.py L6 一段·夹带防线复核＝该行无独立 7-8 位 token）；基线副本头注/校验段 64 位子串（product L1 8 段/arch L1 8 段/backfill-demo L24-25 16 段）＝非 commit 指针；独立 token 8 笔逐笔：`20261024`×2＝纯日期形态（票 A4 明列不算）、`dc2d4e6`×2／`a0fd121`／`7342f2f`＝两基线副本**正文钉死段**commit 锚（白名单②·哈希等式在位佐证见 §八）、`7214ad14`／`efb4f765`＝baseline-backfill-demo.py L9/L10 sha256 前缀引用（票 S5 明列豁免）。**违例＝0。**

## §六 A6 独立复跑（绿-7）

装配面（无 tests/）下 `bash skills/sop/scripts/ledger-init.sh`，`SWB_LEDGER_ROOT` 重定向 Temp、`SWB_PROBE_RESULTS` 不设＝无读数源：exit **0**、`B0_FORM=main`（取数走主路缺省）、`B0_P7_STATUS=missing` 缺档容错落主路、无 FATAL；仓与装配面零残留（面内无 `.collab` 生成）。`bash -n` 过。

## §七 A7 门禁与闭环对拍（绿-8）

- `bash agent-skills/object-audit/scripts/run-gates.sh`（主盘直跑；`tools/run-gates.sh` 不存在＝派工单笔口误登记）：**GATE PASS exit 0**（发现 9153 条均路由②不拦）。
- check-pointer-closure 同口径锁死对拍（同命令、worktree 居仓同级 `D:\multi-agent-collab-devkits-qa-wt`·用毕已 `worktree remove` 归位）：
  - 施工前基线 `5da4581`＝WATCH 1756（D6-3 538／D6-4 1218）；
  - 施工末笔 `a885ad7`＝WATCH **1744**（D6-3 536／D6-4 1208）＝**净减 12**（消 13 笔＝S2 触及件 multi-collab WATCH 11＋commit-audit.py 拆段消 P1 `.collab/` 字面 2；增 1 笔＝S2 新指 `../../software-orchestration/…` 仅装配面可解＝EXEMPT③预登记）；
  - 回执笔（`d978b5a`/`a0f3ee7` worktree）＝1782，增 38 笔全部＝回执件自身清单行自引（历史先例形态），施工本体零新增实锤。
  - EXEMPT 预登记三笔在册复核（a885ad7 口径）：①90-changelog 内 multi-collab WATCH 4 条（19/27/27/34 行）✓；②EAC-SK6 历史票 1 条 ✓（实文件名＝`…EAC-SK6-M1-黄项最小修正票.md:10`，票面登记名省 M1 后缀＝观察-4）；③S2 新指 1 条 ✓。
- 主盘直跑 WATCH 3238 与 worktree 读数差＝主盘游离未跟踪 `.collab/refs` 快照件族（worktree 无该等文件）＝SOT 伪影沿先例登记（观察-3）。

## §八 功能不回归（绿-9/10/11/12）

- config 六 JSON＋hooks.json＋plugin.json＋.codebuddy-plugin/plugin.json 全部解析通过 ✓。
- 装配面 `skills/sop/scripts/` 全部 py 文件 py_compile exit 0 ✓；`ledger-init.sh`＋tests/ 侧 drill-runner＋六演练＋探针 sh 全部 `bash -n` 过 ✓；两 validator（fuxi gates 同名两件＝仓内实存唯一 validator 对）py_compile 过 ✓。
- 基线副本哈希等式独立重算在位：仓侧交接件物理 L29–84 段 sha256 前 8＝`7214ad14` ✓、L85–260 段＝`efb4f765` ✓；装配面两副本去头注体与登记段逐字节等值（3613/3613、18885/18885）——禁动面未破。
- commit-audit.py 拆段功能字面在位复现：`r"\bSW" + r"B-[A-Z]*\d+\b"`＋`r"\.coll" + r"ab/tickets/…"` 两段拼接形态实存、拼后语义＝原判据；源仓件与装配面件字节全等。
- assembly_exclude 谓词行为独立对抗测（本席 import publish.py 直调）：五合法项全命中、`docs/PRODUCT.md`/`testsx/`/`a/tests/` 全不误伤；非法项 `*`／`..`／`/abs`／非字符串／非 list 全部 fail-closed die_usage exit 2 先于任何写 ✓；过程域段 `.collab/.scratch` 装配器段级排除（L730）在位 ✓。
- S7 五席位卡复跑 grep：`SWB-`/`A-1x`/`TKT` 五卡全部 **0/0/0**（前后同值·零改动）✓。

## §九 观察登记（5）

1. 全新装配 bundle 源 commit＝装配时刻 HEAD（实测两次分别 `a885ad7`/`a0f3ee7`），manifest 随装配时刻记账＝装配器既有语义，产物字节两态全等，不影响结论。
2. 皮总字样 32 处全在 EAC 条款本体（角色定义＋裁定日期锚），判档②；若北极星口径未来收紧「决策者姓名锚」形态，属 EAC 真源批次不在本票射程。
3. closure 主盘 vs worktree 读数差（§七）。
4. 票面 A7 EXEMPT② 文件名少记 M1 后缀。
5. 核验期间 HEAD 前移 `d978b5a→a0f3ee7`（回执补账笔），bundle 子树 diff 仅回执一件，装配面经逐字节摘要证明不受影响。

## §十 纪律自证

只写本报告一件（`.collab/qa/` 本席写域）＋仓外 Temp/仓同级 worktree（全部用毕清理归位）；装配面终态与开工快照逐字节全等；仓 `git status --porcelain` 终检净；未读另一席旧核验件；未复用工程师脚本；未改账本。

—— 完 ——
