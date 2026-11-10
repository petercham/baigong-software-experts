# SWB-TMPLRULE-01 施工段 QA 席独立验证 v1（fresh eyes·当轮现跑·回执禁读采信面在册）

- 判定席＝QA 席（qa-tmplrule-v1·fresh 实例·一票一实例）
- 开工 HEAD 实测＝`501a8756e6948599c1d0ff5ecdcc38bf547254b6`（当轮 `git rev-parse HEAD` 现读，＝链顶＝笔二回执笔）
- 案件坐标复点（全部当轮现跑吻合）：票面落链 `dc19d82`＝`dc19d827044363debf599eb70f0e79417ef57b89`；票面 blob＝`d988f9fa540196ae9ae4e85978c73108f15d8552`（`git rev-parse "dc19d82:.collab/drafts/2026-11-09-工单模板规则票草案-v1.md"` 现读＋blob 自哈希复算 `hashlib.sha1(b'blob %d\0'+data)` 全等）；放行裁定 `e12afd3` 在 HEAD 链上（`git merge-base --is-ancestor e12afd3 HEAD` 过）＋裁定件内「都批」逐字在场 grep -c＝1；笔一＝`2044c9b625a8b8a6411c0da5eeaf6dba692dcf8b`（其父＝`ff46472264437bee571256f8483c2e8dc8349f3b`＝开工 ANCHOR 全等）；笔二＝`501a875`（其父＝笔一全等）；模板件施工前 blob＝`a6ae67fbba86290c700aef91b0dc6f3d6df9724c`（`git rev-parse "2044c9b~1:agent-experts/baigong-software-team/skills/sop/templates/ticket-template.md"` 现读＋blob 自哈希复算全等）。
- 取证面纪律：工程师取证区 `.scratch/TMPLRULE-eng/` 全程未读；回执 `.collab/receipts/2026-11-09-工单模板规则票-回执-v1.md` 仅判据九对照面读取一次，本件全部读数均系当轮独立现跑，零抄回执数字。
- 取证临时物＝仓外 `qa-tmplrule-v1-tmp 区`＋仓外两净化身 worktree（`qa-wt-base 区`／`qa-wt-head 区`），完工前自删附读数（见 §末清理段）。

## 判据逐项（红/黄/绿＋命令＋当轮读数）

### 判据1 对账闭集＝绿

- `git show --name-only 2044c9b…`：恰两件＝`agent-experts/baigong-software-team/skills/sop/SKILL.md`＋`agent-experts/baigong-software-team/skills/sop/templates/ticket-template.md`。
- `git show --name-only 501a875…`：恰一件＝`.collab/receipts/2026-11-09-工单模板规则票-回执-v1.md`。
- `git log ff46472264437bee571256f8483c2e8dc8349f3b..HEAD --oneline`：恰两笔（2044c9b＋501a875），均属本票，无他案笔需归因。
- reflog 无 amend/reset 痕迹：`git reflog --format='%gd|%gs' -60 | grep -cE '\|(amend|reset)'` ＝0（按 reflog 动作段精确检，message 内「禁amend」字样不误计）。
- numstat 分账：笔一＝SKILL.md 1/1＋模板 56/0；笔二＝回执 67/0。

### 判据2 逐字照录独立复算＝绿

- 自写 python：blob 直读票面（blob d988f9f…）取 fenced text 块（L30–L66＝37 行）；blob 直读模板件笔后态（`2044c9b:` 态）取并入条款区（标题行 L60 后 T1 起至 T10 条款末续行＝38 行）。去行首缩进后：票面 1358 字符（去换行归一）／模板 1358 字符（去换行归一）；difflib SequenceMatcher（autojunk off）去换行归一字符流全等＝True、非 equal 操作段＝[]。含换行态 1394 对 1395，差一行＝T9 段「档位1 票面族；档位2 史账判定件族（逐件登记禁回改）；」拆为两独立行（unified diff 唯一 hunk ＠＠ -31 +31,2 ＠＠，仅换行适配零改字）——单列归因：允许的一处拆行适配坐实。
- 改动纯追加：模板件 numstat 删除行＝0（56/0）。
- T10 分级表体＋分级依据注对 `.collab/drafts/2026-11-09-规范工单模板草案-v2.md`（blob 45d97cf…）§二-分级表 L86–L93 逐行在场复算：表体 L88–L91 四行＋分级依据注 L93 整行匹配全在场；唯一「缺」＝L86 v2 节标题行（含「防过程膨胀」字样）——非表体非注，模板件以自有节标题承载，不计缺。

### 判据3 V1 十二标志语＝绿

对 `git show 2044c9b:` 模板件态逐语 `grep -c`：新规时间效力＝1／两轴正交＝1／主效力＝4／取代＝撤销＝1／五席制＝1／外部交接票必填＝1／历史编号＝1／拆写＝1／排除档位＝3／三档＝2／封口条款＝2／全量档＝2。十二语各≧1 全过。

### 判据4 V2 存量零触碰＋禁动面＝绿

- `git diff ff46472264437bee571256f8483c2e8dc8349f3b..HEAD --name-only` 全集＝三件（回执＋SKILL＋模板），⊆ 三件闭集。
- 禁动面 pathspec diff 空集：`.collab/drafts/`、`agent-skills/`、`tools/`、`agent-experts/baigong-software-team/plugin.json`、`agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json`、`agent-experts/baigong-software-team/bundle.lock`、`.collab/tickets/`、`.collab/audits/` 全空（`tools/` 目录对两栖点 `git ls-tree` 均不存在＝该禁动面为空集是恒真态，照登）。
- `.collab/receipts/` 桶内 diff 明细＝仅 `A` 一枚＝回执新件（笔二豁免面兑现），其余既有件零触碰。

### 判据5 V3 门禁＝绿

- 脚本现盘名＝`share/run-gates.sh`（票面 dispatch 口径所写 tools 斜杠 run-gates 点 py 在现盘不存在，照登票面口径与现盘差异归因＝TOOLHOME 迁册后落 share）。
- 对等净化身两跑：两枚 detached worktree 分别检出 ff46472 与 501a875（同置于仓根同盘同级位，保 `check-source-of-truth.py` 默认相对兄弟包 `../multi-agent-collab-experts/workbuddy/baigong-video-team` 两侧同可解析），各跑 `bash share/run-gates.sh --root <各自根> --no-write`：两跑行数 7791＝7791；BLOCK 族归一（行号抹平＋根径归一）集合 3116 对 3116，新增（HEAD 有 BASE 无）＝0、BASE 有 HEAD 无＝0。两跑尾 BLOCK 同值＝FX-HOOK-1「期望钩子不在盘」＝linked worktree 无 `.git/hooks/pre-commit` 所致的本席取证环境项，两侧同态对称，非本票引入。
- 主仓现盘对 HEAD 跑 `bash share/run-gates.sh --no-write`＝exit 0＋`GATE PASS（发现 150131 条，均按路由表走②不拦提交）`（主仓 `.git/hooks/pre-commit` 在盘＝`-rwxr-xr-x … Nov 10 04:38`，FX-HOOK-1 不触发）。
- 两笔提交当时 pre-commit GATE PASS 态＝等效坐实：主仓钩子 04:38 已在盘（早于两笔 18:15/18:19）、链上两笔均为 commit 型（reflog 无 amend/reset）、HEAD 等效重跑 GATE PASS＋BLOCK 族对基线零新增。回执所自述「BLOCK 行计数 18251 对 18251」不采信不比对（其基线预跑时点主仓未跟踪噪音面与今轮不同态，原始计数不可跨环境复现），本席以归一差集零新增为判定读数。

### 判据6 V4 档位账＝绿

- 模板件现盘（＝HEAD blob）行号读数：档位1 行＝L94、档位2 行＝L95、档位3 行＝L96（L97 为其续行）、封口条款独立行＝L103（居三档列表之外，T9 拆写兑现）。
- 票面自载口径计数：`grep -c -E '^\s*档位[123] '`＝3＋`grep -c '^封口条款：'`＝1→合计 4＝合。
- 单独说明「原档位4」提及行不构成误计的判据口径：L98「原「档位4 向前进封口」从档位列表移出…」与 L99 属 T9 条款正文照录句，行首非「档位数字＋空格」亦非「封口条款：」，两计数式均不命中；「封口条款」grep -c＝2＝L98 提及＋L103 标志行，标志行恰一枚。

### 判据7 V5 纯净性＝绿

- 两笔面单纯净：笔一恰两件／笔二恰一件（判据1 读数），开工时 index 在飞他案 staged 项（当时现读＝FUXI 线「皮总裁定 FUXI-R12 并发规矩不立 P2 带补丁起」裁定件 A 态，他案在飞物）未带入任一笔面单。
- `FX_COMMIT_DECLARE` 提交闸形态在册：两笔 message 均含「FX_COMMIT_DECLARE 声明本笔面」声明段＋pathspec 限定字样；两笔 message 零 at 符号字符（`git log --format='%s%b' ff46472..HEAD | grep -c '@'`＝0）。

### 判据8 纯净性㊻/㊺＝绿

- 靶检现跑：`python share/check-pointers.py --target "agent-experts/baigong-software-team/skills/sop/templates/ticket-template.md"` exit 0；`--target ".collab/receipts/2026-11-09-工单模板规则票-回执-v1.md"` exit 0；（随带 `--target "agent-experts/baigong-software-team/skills/sop/SKILL.md"` exit 0）。
- 交付面（模板件）指针扫描逐处归因：L62 并入注指 `.collab/drafts/2026-11-09-工单模板规则票草案-v1.md`＋落链 sha dc19d82／裁定 sha e12afd3；L105 T10 表头注指 `.collab/drafts/2026-11-09-规范工单模板草案-v2.md`——均属仓内治理史面真源指针（条款文本唯一真源溯源所需，票面 §② 自载「fenced＝条款文本唯一真源」同向），目标在盘可解析、靶检 exit 0，非案卷取证路径非仓外外指，判合规。L96 `.scratch` 族点名＝T9 条款正文对取证族的规范点名＝字样非指针（判据口径单列）。模板件并入段无任何 `.scratch/TMPLRULE-eng` 类案卷路径、无仓外面外指。
- 回执件（过程面）允许案卷指针：其 §七 自述取证落 `.scratch/TMPLRULE-eng/`（该目录在盘未跟踪，可解析），exit 0 兑现。

### 判据9 回执对照（只对照不采信）＝绿

对照读数：回执开端 HEAD＝ff46472（与本席独立复点全等）；对钉双核 blob d988f9f／a6ae67f 在册（本席独立复算两钉全等）；§一 清单与两笔 name-only 全等（本席独立跑面单相符）；V1–V5 逐条有读数（V1 十二语计数与本席独立 grep 读数逐值相符；V4 计数 4 与本席独立行号读数同态；逐字照录 1358 字符与本席独立复算同值）。无读数冲突。回执自述 BLOCK 原始计数 18251 不可跨环境复现一节已在判据5 单列归因，不构成冲突判红项。

## 异常与在飞面登记（如实不粉饰）

- 开工 `git status --porcelain` tracked 净兑现（无 M／D），index 他案 staged 一枚＝FUXI 线「皮总裁定 FUXI-R12 并发规矩不立 P2 带补丁起」裁定件 A 态（他案在飞物，全程零碰）；落笔轮复点 index 他案 staged 一枚变为他案 FUXI-FX-U38 补课排产票面 A 态（前枚经他案链自行处置离 index）＝他案并发在飞推进照登，与本票判定无涉、未带入本笔。
- 主仓 `tools/` 目录不存在（两栖点 `git ls-tree` 均无）＝票面禁动面列举沿旧径名，空集恒真照登。
- 本席首轮 blob 复算曾以 sha1sum 直 pipe 误比（漏 git blob 头），当轮即以 blob 自哈希复算＋certutil 落盘字节双重复核自纠，两钉全等坐实——本席工具口径误差，非被验面对象异常，登记备查。

## 总判

九判据＝红 0／黄 0／绿 9。**放行收口成立**（红 0 兑现）。停手条件三条均未触发：票面 blob 无漂移（对钉全等）、两笔面单零他案混入、门禁 BLOCK 族归一差集零新增。

## 落笔纪律自证

- 本判定件落笔前靶检 `python share/check-pointers.py --target ".collab/audits/2026-11-10-SWB-TMPLRULE-01-QA席独立验证-v1.md"` exit 0（读数见回报）。
- `FX_COMMIT_DECLARE` 声明＋pathspec 限定恰本判定件一件 add/commit 紧邻无窗口；禁 add -A／禁 amend／禁 --no-verify；message 零 at 符号字符；撞 index.lock 有界等待（5 秒×40 试上限）禁删锁；他案 staged 项与他案面零碰零带入（面单恰本件一件）。

## 取证清理段（完工前自删）

- 仓外取证区＋两净化身 worktree 清理命令与读数见本席完工回报（清理发生于本笔落链之后、回报之前，读数随 SendMessage 在册）。
