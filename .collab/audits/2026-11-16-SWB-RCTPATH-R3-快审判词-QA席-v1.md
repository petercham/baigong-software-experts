# SWB-RCTPATH-R3 · 20-handoff 节题去编号微票 · 快审判词（QA席·v1·fresh eyes）

- 判席：QA 席（fresh 实例·与产品席同时独立审票，未读彼席产出）
- 审对象：`.scratch/tickets/2026-11-16-SWB-RCTPATH-R3-20-handoff节题去编号微票-v1.md`（票面落链笔 0f4291c）
- 体例自证：本判词对仓内文件提及＝仓根相对纯路径（正斜杠）；叙述性提及（含悬空旧径）＝裸文＋全角斜杠（／U+FF0F）；引用票内原文以 ⟦⟧ 标记。本判词自靶 python share/check-pointers.py --root . --target 本件实路径 exit 0 后落链（读数见 §一）。

## 一、开端读数（本审轮现跑·禁抄票内旧数）

| 项 | 实测读数 |
|---|---|
| 时点 | 2026-11-16 18:20:50 +0800（date 现跑） |
| HEAD | **0f4291c**（＝票面落链笔·与派工预期全等） |
| 票面 sha | git hash-object 票面 ＝ **90e901a155b35e5efbbba52ed55d4b04973994b4** |
| 票面笔坐实 | git show --stat 0f4291c ＝ **1 file changed, 119 insertions**＝笔仅票面一件 ✓ |
| 落点件 | `agent-skills/multi-collab/references/20-handoff.md` wc -l ＝ **66 行**（与票 §〇 全等） |
| 落点件自靶 | python share/check-pointers.py --root . --target agent-skills/multi-collab/references/20-handoff.md ＝ **exit 1·恰一枚悬空＝行 24**（BLOCK OA-D6·deliverables／experts／baigong-software-team／skills／software-orchestration／references／handoff-discipline.md 旧径·share/baseline-pointer-exempt.json grep handoff-discipline ＝ 0 枚＝不在豁免清单）＝与票 §〇 V4′ 基线全等 ✓ |
| 缺省 BLOCK 钉 | python share/check-pointers.py 缺省扫描 grep -c BLOCK ＝ **22810** ✓ 现跑全等 |
| 缺省 WATCH 钉 | 同轮 grep -c WATCH ＝ **4581** ✓ 现跑全等 |
| 全仓 GATE | bash share/run-gates.sh ＝ **GATE PASS exit 0·发现 151502** ✓ 三钉值全部现跑全等零摆动 |
| 票面自靶 | python share/check-pointers.py --root . --target .scratch/tickets/2026-11-16-SWB-RCTPATH-R3-20-handoff节题去编号微票-v1.md ＝ **exit 0** ✓ 亲跑复现 |
| 链上锚 | git cat-file -e 逐枚：4ea0d58／89f796d／b6a4ac6／8cb7fc1／764afbf／5adf535／b2b61d7 全部在位 exit 0 ✓（禁动面另列 8792a97／0da2566／659ec9a 亦全部在位 ✓） |
| 他案脏面 | git status：ledger 一枚 M（agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl·diff 1 增 0 删·零反引号 token＝不扰钉）＋仓根散件群＋`.collab/` 根与 research 散 md——与票 §〇 登记形态一致·照登零带入 |

## 二、逐判据红黄绿

### V1 · 旧行 verbatim 对盘 —— **绿**

python 提取比对实跑：落点件行 28 现行文本 ＝ ⟦### 二之二、留存过程件正文内的仓内文件引用写法（两域两制·决策者裁定 SWB-RCTPATH 甲案）⟧ ＝ 票 §二 旧行块（票面行 45）**逐字符全等 True**；od -c 字节面复核中圆点＝U+00B7、括号全角、顿号、空格位（SWB 前单空格）全部一致。票内两块以 python 按票面行 45／50 提取再比对，非目测。改错字符致 diff 失败的风险＝零。

### V2 · 新行形态合决策者取态 —— **绿**

票内新行块（票面行 50）＝ ⟦### 留存过程件正文内的仓内文件引用写法（两域两制）⟧，与派工转述的决策者亲选形态逐字符一致；python 检新行不含「二之二」「SWB」「RCTPATH」「决策者裁定」任一 token＝无任何序号与 ID 注记 ✓。架构席「ID 注记去留＝去」三条论证（沿革真源在链不在壳／注记系插档思维伴生物／语义 grep 互查可达）独立复核成立：落点件内「决策者裁定」字样 grep -c ＝ 1 恰存于行 28，新行不含＝票 V2 的 1→0 判据自洽；链上归裁登记 4ea0d58、票面族名与节题语义词互查可达，可追溯性不损失。**无站不住处。**

### V3 · 声明闭集完备 —— **绿**

声明闭集＝行 28 单行替换一枚；禁动面逐条在册且可机械判：同件行 1–27／29–66 零触碰、行 29–34 条款正文（条目 1–5 实居行 30–34）零改动、行 24 悬空零处置、链上历史件「二之二」字样 append-only 零回改、门禁配置／账本／他案脏面零触。独立复测：落点件内「二之二」grep -n 仅行 28 恰一枚＝单行替换无歧义 ✓；节题面 grep -n '^## \|^### ' ＝ 行号 5／9／28／36／55／62 六节＝与票 V3 钉值全等 ✓。agent-skills／dev-discipline／references／20-handoff.md 不存在实跑坐实（ls 无此目录＋git ls-files 全域 dev-discipline 仅 agent-experts/baigong-software-team/skills/software-orchestration/references/dev-discipline.md 一枚）＝票面登记失实风险＝零 ✓。

### V4 · 验收判据可机械判定 —— **绿**

全部判据均为命令＋钉值形态：byte 级 diff 恰 1 增 1 删单 hunk／wc -l 66→66／grep -c 二之二 1→0／grep -c 决策者裁定 1→0／节序行号钉死。差量口径 V4′＝落点件自靶基线 exit 1 恰一枚悬空＝行 24，**本席亲跑复证全等**（见 §一表）；三钉值 BLOCK 22810／WATCH 4581／GATE 发现 151502 **本席亲跑全等**。票据回执落 tickets 桶不在缺省扫描钉扰面的宣称：与本轮 run-gates 输出形态一致（根 `.scratch/` tickets 桶无新增 WATCH 路由命中）。

### V5 · 防自咬体例 —— **绿**

票面自靶 exit 0 本席亲跑复现 ✓；票 §票面自注与 §六 防自咬条款在册（裸文＋全角斜杠／⟦⟧ 引用／反引号不落指针）；§二 旧行块与新行块逐块检＝不含路径 token（无斜杠无扩展名形态）✓；票面 grep 反引号包裹路径＝零枚。

### V6 · 落链纪律条款 —— **绿**

§六 逐条在册：单件 pathspec 两端齐带＋add 紧邻 commit 零窗口；FX_COMMIT_DECLARE 挂 commit 侧（并引 `share/check-staged-declaration.py` 机理＝本席核读该脚本属实：声明源闭集环境变量优先、挂 add 侧无声明即 fail-closed 硬拦，叙述准确）；尾标闭集全列（-TICKET／-QA-REV／-PM-REV／-PM-RELEASE／-BUILD／-RECEIPT／-QAV／-GCLOSE·族名内嵌）；禁 add -A／禁 amend／禁 --no-verify；collab: 起头·零 at·零反引号·尾标置最末；commit 类 timeout 600000ms；撞 index.lock 有界等待零删锁；scratch 完工自删。与 V6 验收判据（BUILD 笔／RECEIPT 笔各恰一枚＋禁动面 pathspec 域 git diff 零命中）互为闭环。

### V7 · 架构席两项自决裁量复核 —— **绿（附黄-1 证据读数不准·见 §三）**

① ID 注记去：论证成立（见 V2）。② 「不再造 X 之二」不另立条款：三条理由（先例实物体现／YAGNI 最小改动面／自指悖论）主体成立——本票新节题即先例、立条款即扩面、条款自身落点当场撞射程，推演均可复验。唯第 2 条内一处证据读数陈述失准＝黄-1（不推翻结论，见下）。

## 三、黄项（两项·均不阻塞放行·各附修正建议）

**黄-1 · 票 §二 S2 论证 2「无现行违例压力」句内证据读数与实测不符**：票文称 ⟦全仓 tracked 面「二之二」式插档编号除本行外零存量——git grep 实测其余命中全部居 external-advisor-collab 外包 refs 族⟧。本席 git grep 实跑：「二之二」字面其余命中全部居 `.collab/` 案卷族（R2 判词／收口登记／回执）与 `.scratch/` 票面族＝**本链史账件，非外包 refs 族**；而 external-advisor-collab 的 `references/` 规范面内「X 之二」式编号**确有存量**（`agent-skills/external-advisor-collab/references/40-artifacts.md` §四之二节题、`agent-skills/external-advisor-collab/references/20-rounds.md` 「两式之二」行内用法）。结论面仍站得住（agent-skills 规范面内「二之二」式插档编号存量除行 28 外＝零，git grep 全域 agent-skills 实跑仅行 28 一枚；外包件族划出本仓规范面射程属既有体例），但证据句把两类命中互相错位。**修正建议**：主理人放行登记或票面勘误注（append-only）改为——「agent-skills 规范面内『二之二』式插档编号仅存行 28 一枚；git grep 其余命中＝本链 `.collab/`／`.scratch/` 史账件＋外包 external-advisor-collab 件族『X 之二』式编号（§四之二等·划外包先例不入本仓规范面射程，划界口径如册）」。

**黄-2 · 对抗臂暴露读取面缺口（硬化建议·非票面缺陷）**：票 V1／V2 比对旧行／新行取 §二 两块文本，未写明须从**票面链上 sha 固定版**（0f4291c 版）git show 提取还是读工作区现文；工作区票面理论上可被篡改后蒙过 V2（票面自靶 V7 只检指针不检内容未变）。当前由双席快审＋放行登记钉 sha＋第 5 步 fresh QA 三面兜住，风险低。**修正建议**：第 5 步验收判词开工读数增一行「票面 git hash-object ＝ 0f4291c 版 blob sha 90e901a155b35e5efbbba52ed55d4b04973994b4 全等」钉值，§二 两块提取一律 git show 链上版。

## 四、对抗臂（设想施工席违例·逐发检票面拦截力）

| 假想违例 | 拦截判据 | 结果 |
|---|---|---|
| 改多行／顺手改行 29–34 | V1 diff 恰 1 增 1 删单 hunk＋hunk 外零前导 +/-；V2 wc -l 66→66＋grep -c 两串 1→0 | **拦下** |
| 顺手修／删行 24 悬空 | V4′ 对拍＝行 24 读数枚数与内容逐字不变＋零新增 BLOCK／WATCH；V1 hunk 外零改动 | **拦下** |
| 回改链上历史件「二之二」 | V6 BUILD 笔 git show --name-only ＝恰落点件一枚＋禁动面 pathspec 域 git diff 零命中＋禁动面写死枚列链上九 sha | **拦下** |
| 新行自带 ID 注记／序号 | V2 施工后行 28 与 §二 新行块逐字符全等（python 比对 exit 0 形态） | **拦下** |
| 篡改工作区票面旧／新行块 | 票面 V 系无 sha 钉（见黄-2）；由链上 0f4291c＋双席快审＋放行登记钉版兜住 | **兜住（建议按黄-2 硬化）** |

四发主案全拦＝票面判据有牙；唯读取面（票面版本固定）留一档薄面，已附硬化建议。

## 五、附注（信息·不计红黄）

- 派工文书称票面 116 行，实测 wc -l ＝ 119＝派工侧元数据口径误差；票面自身未宣称行数，不构成票面问题。
- 链上历史件含「二之二」字样实存处（零回改对象）实测分布：R2 双席判词与 QA 验收判词／R2 收口登记／R2 回执／R2 票面／本 R3 票面＝append-only 条款对象齐全，本席审中零触碰。

## 六、总判

**红 0 · 黄 2 · 绿 7（V1–V7 全绿）。总判＝可放行**。黄-1＝票面论证证据句读数错位（结论不翻·建议勘误注或放行登记内更正）；黄-2＝验收读取面硬化建议（放行登记／第 5 步验收判词内落实即可）。两项均不构成返工修单必要。三钉值与 V4′ 基线全部本席亲跑全等，票面自靶 exit 0 亲跑复现，票面笔仅一件坐实，dev-discipline 不存在宣称实跑属实。

—— QA 席（SWB-RCTPATH-R3 快审）·判词自靶 exit 0 后落链 [SWB-RCTPATH-R3-QA-REV]
