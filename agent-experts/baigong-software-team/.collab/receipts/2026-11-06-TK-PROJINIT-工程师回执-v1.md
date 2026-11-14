
# TK-PROJINIT 工程师回执 v1（完成回流）

- 票面＝`.scratch/tickets/2026-11-06-PROJINIT-项目锚定与初始化整改票-v2.md`（rev5 置顶勘正段口径·时效序 rev5＞rev4＞rev3＞正文）
- 放行登记＝仓根 `.collab/decisions/2026-11-06-皮总放行-PROJINIT开工.md`（`2215108`）
- 开工 HEAD 实测＝`2215108`（≥放行登记笔·命中）；交付笔＝`a4aefb7`；完工 HEAD＝本回执笔
- 开工 `git status --porcelain` 基线残项登记：两 `.collab/ledger/`、`.scratch/FX-*` 系、`.scratch/SRC4Z-draft/`、`.scratch/qa-rpubrev/`、`.scratch_wbdocs.html`——全部未触碰

## 一、开工复测（§十三 五项读数）

1. `git rev-parse --short HEAD`＝`2215108` ✅
2. 四脚本 `project_root()` 行号＝write-guard L48/L76、lease-issuer L32/L60、commit-audit L56/L84、memory-neutralize L44/L72——命中 §3.1 锚文；替换段逐字相同核验（正则抽取比对）＝True ✅
3. 包自带 `agent-experts/baigong-software-team/docs/STRUCTURE.md` 存在；本仓根 `docs/` 缺席；`.workbuddy/` 实存（内含 memory）无 `swb-anchor` 三读数 ✅
4. dev-discipline `wc -l`＝105、§九.3 冲突句三行锚文逐字命中（L99–101）；SKILL.md `wc -l`＝26 且 L23＝deploy-gate 索引行；test_enforcement.py `wc -l`＝294 ✅
5. 版本三同源现值 `0.1.30` 零动；两 config `sources` 改文前零命中；commit-audit L31–37 五型在册（含 GWP-P6-1 第五型）；lease-issuer L104–107 REJECT 段在位 ✅

## 二、H-4 挂钩实测取数（施工首项·判据 5b 在册·不改票面语义不自行拍设计）

实测面（如实登记）：
- 部署缓存面 `~/.workbuddy/plugins/cache/my-experts/baigong-software-team/0.1.30/hooks/hooks.json` 在位（PreToolUse 三 matcher：写侧 write-guard／读侧 memory-neutralize／Bash commit-audit·命令＝相对形制 `python "../skills/sop/scripts/…"`）。
- 本会话工具通道写探针 .scratch／projinit／hook-probe.txt 裸文写·已随完工自删（Write 工具落笔）→ 包面 `.collab/ledger/ledger.jsonl` 与仓根 `.collab/ledger/` **均无对应留痕行**；缓存面 0.1.30 树下亦无 `.collab/ledger/`（find 零命中）。
- 读数结论：本会话现盘＝钩子进程未在任何可达账本落痕＝钩子进程 cwd／账本落位＝平台未定项实态（H-4 在册项现状证据）。票面主路（`SWB_REPO_ROOT` env＋swb-anchor 双显式路）生效性不受该读数影响（判据 2a/4a 已证）；「从 cwd 上溯找锚」路现盘生效性＝H-4 归裁前维持 §二条件声明口径。呈裁随主理人。

## 三、租约面（当票租约只读消费·lease-issuer 实体签发）

- TK-PROJINIT engineer 席租约：path_globs＝["skills/**","config/**"]（写域子集校验过闸 exit 0·countersign＝architect:team-lead-dispatch-PROJINIT·入账包面 leases.jsonl）——8 件闭集全命中该两片。
- 判据 4a 夹具租约 TK-PROJINIT-TEST（architect `.collab/drafts/design/`）落 `.scratch/projinit/leases.jsonl`（夹具内·随夹具删）。
- 回执件落位＝`.collab/receipts/`：engineer deny_globs 含 `.collab/receipts/**`——回执落笔走 `collab:` 通道＝沿 TK-GWP/TK-SRC4Z 等近期 TK 回执先例（主理人派工书明令回执落该目录·本席照令）。

## 四、判据 1–13 逐项读数（全部实跑·夹具落 `.scratch/projinit/`·跑毕即删）

| # | 读数 | 判定 |
|---|---|---|
| 1 | `py_compile` 四脚本逐一＝四件 exit 0 | 绿 |
| 2a | FP 锚定＋cwd＝FP/src→四读数逐字一致＝`D:\multi-agent-collab-devkits\.scratch\projinit\fakeproj` | 绿 |
| 2b | 锚定＋FP/src 造近端 STRUCTURE→四读数＝FP（锚胜近端） | 绿 |
| 2c | 覆写 `SWB_REPO_ROOT=…/other`→四读数＝覆写值原字面（正斜杠不归一·S-pm8） | 绿 |
| 3a | 无锚无结构 cwd＝FP→四读数逐字＝包根（fail-safe） | 绿 |
| 3b | 无锚＋FP/docs/STRUCTURE.md cwd＝FP/src→四读数＝FP（事后校验路） | 绿 |
| 3c | 锚件 `project_root: ../elsewhere`→四读数＝包根（自指闭合负判） | 绿 |
| 3d | 锚件无键行乱文本→四读数＝包根（同 3a） | 绿 |
| 4a | LI 签发 exit 0→WG 写 FP/.collab/drafts/design/x.md：stdout deny JSON 缺席＋stderr `ALLOW write-guard path=.collab/drafts/design/x.md: 路径∈租约` ＋exit 0 | 绿 |
| 4b | WG 写 FP/docs/ARCHITECTURE.md→deny JSON 在场（glob＝docs/ARCHITECTURE.md）＋ledger deny 留痕 1 行 | 绿 |
| 4c | 无 `SWB_LEDGER_ROOT` cwd＝FP/src→`default_ledger_root()` 四读数逐字＝`FP\.collab\ledger` | 绿 |
| 5 | 本仓根 cwd＋`WG --sentinel`＝deny JSON 与修前基线逐字同形态（席位不可归因 deny）＋缺省锚读数＝包根 | 绿 |
| 5b | 锚定 FP＋cwd＝包根＋无覆写→四读数＝包根（已知边界行为钉死·H-4 挂钩在册随裁复测） | 绿 |
| 6 | `agent-experts/baigong-software-team/tests/s4/test_enforcement.py` exit 0＋`PASS t01..t13` 十三行（改 config 后与 commit 后两跑均绿） | 绿 |
| 7 | 四件抽 `ANCHOR_FILE = ` 行至 `return pack` 段：四段 sha256 逐字一致＝`72ad0b5e…151c01ab`（段 55 行·rev3 基数） | 绿 |
| 8 | `进场建档`＝1／`swb-anchor`(dev-discipline)＝2／`swb-anchor`(SKILL)＝2 前三≥1；`只是 {root} 的末尾段`＝0；dev-discipline `wc -l` 105→**131**＝105＋§A 24＋补行 1＋§B(+1) 公式恰中 | 绿 |
| 9 | commit 前双对面：`git diff --name-only` 与 `git add` 后 `git diff --cached --name-only` 两跑读数各恰＝**8 件**（config/hooks/plugin/bundle.lock/tests/deploy-gate/SKILL L23 零入列零改）；numstat 合计＝**338**≤420 | 绿 |
| 10 | 未锚态 fakeproj2 直接文件系统落锚 exit 0 无拦截→2a 前半读数翻正＝FP2 四读数 | 绿（依据句按 rev4 段第 5 点：裁定口径＋现盘双读数并存；本会话 hooks 装载态＝见 §二 H-4 实测＝工具通道未落痕，「落笔 exit 0」读数按 rev3 黄⑤口径效力降级登记，不作 H-1(a) 通道实体证据） |
| 11 | §九区间 `开发面` 计数≥1（＝1）；旧冲突句零命中；deliverables/ 差值口径（rev3 黄④单向判定）＝改写段内旧三行 3 次／新四行 3 次差值 **0**；git diff 该文件删行面除 §九.3 三行外＝0（§九.1/.2/.4/.5 逐字零动）；新句逐字＝§B 草件块 | 绿 |
| 12 | 四读数全中：两 config json 可载＝True；architect deny 不含 `agent-experts/baigong-software-team/docs/STRUCTURE.md`（两文件）＝True；源件 architect write 含＝True；s4 exit 0＋t13 PASS。扩展读数＝五席 deny 含 `sources/**` 两文件十处＝True＋human 行 `[]` 零动＝True；拒签双拦实测＝LI 对 engineer `sources/**` REJECT exit 2＋WG 写 sources／x.md（裸文写·虚构样本名＝租约拒签双拦实测夹具输入·从未落盘） deny JSON（glob='sources/**'）在场 | 绿 |
| 13 | S1b 两态夹具（argv 传路径·零路径字面断言）：态一（根内）registered=True＋config 差集非空＋json 可载＋两文件同批 t13 绿＋STRUCTURE 平台域注记≥1＝GREEN；态二（根外）registered=False＋config/STRUCTURE diff 空＋登记读数行在位＝GREEN；夹具 exit 0 | 绿 |

**§A 草件对拍补充读数**：dev-discipline 文末实际块 vs 票面 §A fenced 块（24 行）集合差＝仅 S1b 补行 1 行（rev5 段「补行字面由执行席按口径落笔」授权口径），草件行零缺失零改写。

**残留纪律**：`rm -rf .scratch/projinit/` 毕，`git status --porcelain` 对 `.scratch/projinit` 零命中＝仓内零运行残留 ✅

## 五、写入/修改文件清单（commit `a4aefb7` name-only 对账口径·恰 8 件）

1. `agent-experts/baigong-software-team/skills/sop/scripts/write-guard.py`（＋48/−22）
2. `agent-experts/baigong-software-team/skills/sop/scripts/lease-issuer.py`（＋48/−22）
3. `agent-experts/baigong-software-team/skills/sop/scripts/commit-audit.py`（＋48/−22）
4. `agent-experts/baigong-software-team/skills/sop/scripts/memory-neutralize.py`（＋48/−22）
5. `agent-experts/baigong-software-team/skills/software-orchestration/references/dev-discipline.md`（＋29/−3＝§十追加含 S1b 补行＋§九.3 改写）
6. `agent-experts/baigong-software-team/skills/software-orchestration/SKILL.md`（＋2/−2＝description 触发词行＋dev-discipline 索引行；L23 零动·diff hunk 面＝L3/L24 两处）
7. `agent-experts/baigong-software-team/config/seat-permissions.json`（＋6/−6＝architect STRUCTURE 两键＋五席 sources/**）
8. `agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json`（＋5/−5＝architect deny 移除 STRUCTURE＋五席 sources/**）

本回执件＝第 9 件·单独 `collab:` commit（只含该件）。交付笔 hash＝`a4aefb7`；回执笔 hash＝本笔（见 commit）。

## 六、口径与登记呈报（零自改·呈主理人）

- 版本位：本批属 0.1.31 线**不钉号**（H-6 统筹）——版本三同源零触（判据 9 双对面证）。
- 候裁零偷拍：H-1 收口/H-2 择(c)已实装/H-3 已实装/H-4 实测取证随裁/H-5/H-6 随批；登记不施工段（GWP P7①②③④／P2-1／P-⑤/P-⑥）零动。
- 判据 8 钉值口径注：票面正文「130」为 rev3 前口径，rev5 段写死修正值 **105→131**（§A 块＋补行 1＋§B(+1)）——实跑 131 恰中 rev5 口径，两读数并存如实登记。
- 落笔纪律自查：无 `--no-verify`／无 amend／无 `git add -A`；新文件先单件 `git add` 再 pathspec commit；commit message 带 `TK-PROJINIT` 票号形态（命中 commit-audit 五型第三型）。
