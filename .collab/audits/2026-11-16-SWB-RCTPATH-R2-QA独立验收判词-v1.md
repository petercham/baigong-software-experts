# SWB-RCTPATH-R2 · QA 独立验收判词 v1（fresh eyes·全部判据现跑）

- 票号：SWB-RCTPATH-R2
- 收件人：主理人（team-lead）
- 目的：甲案条款落地批（BUILD 0da2566＋RECEIPT 659ec9a）fresh QA 独立验收判词——逐 V 现跑读数＋对抗臂三发＋红黄绿清单。
- 来源：【来源】qa-rctb1v（QA 席）·判据＝票面 §四 V 系经 §九 rev-1 更正后口径（V4′ 差量／行数基线 58 wc -l 口径）＋派工单判据。
- 状态：待处理

> 体例自证：本判词正文对仓内文件提及一律裸文＋全角斜杠（／U+FF0F）＝票 §3.3 条款第 3 目防自咬体例；引文块内反引号内容以 ⟦⟧ 替换。本判词落链前自靶 python share/check-pointers.py --root . --target 本件实路径 → exit 0（读数见 §五）。

## 〇、开工读数（现跑·不采信工程师回执自证）

- git rev-parse --short HEAD ＝ **659ec9a**＝派工预期开工链顶（RECEIPT 笔）✓。
- 票面链父＝git rev-parse --short 89f796d^ ＝ **4ea0d58**＝归裁登记笔·与票 §〇 登记全等。
- 落点件现文行数 wc -l ＝ **66**；git show 4ea0d58 同件 ＝ 58 行＝基线在册 ✓。
- git status --porcelain 照登零带入零清理＝ledger 一枚 M 态（agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl）＋仓根散件群（.collab 根散 md 十二枚／.collab／research 散 md 六枚／.py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt）——全部他案脏面，与票 §〇／回执 §〇 清单全等，本席零带入零清理。
- 本席 scratch 工作区＝.scratch／rctqav／（完工自删·commit 留证保留）。

## 一、总判

**IS_PASS**——逐 V 全绿、对抗臂三发全绿、红 0 黄 0 绿 10。工程师回执 §四 各读数与本席独立现跑全部吻合（对拍不以其为据）。

## 二、逐 V 现跑读数

- **V2′（差量口径）**：git diff --numstat 4ea0d58..HEAD 对落点件＝**8 新增／0 删除**；git diff 全文＝**恰一个 hunk**（@@ 计数＝1；diff 内 "-" 前导行仅文件头一行，零内容删除）；落点件 wc -l＝**66＝58＋8**（wc -l 口径·rev-1 N-2 更正后等式）✓ 绿。
- **V3（逐字对等）**：自写提取脚本（程序化定位票 §3.3 围栏标记对、取块内正文不含围栏行）＝块体 7 行；落点件行 28～34 段 7 行；两段 sha256 **全等**＝9fe12612594f087e4eb0f15f5c471cf03c9a7e32b0e8749b4bedb65c00215207 双侧同值→ **byte_equal=True** ✓ 绿。
- **V4′（差量自靶·rev-1 N-1 口径）**：现跑 python share/check-pointers.py --root . --target 落点件实路径 → **exit 1·输出恰一行＝恰一枚 BLOCK**＝行 24 既有悬空（deliverables／experts／…／handoff-discipline.md 旧径·OA-D6 标记）＝登基线（票 §九 N-1 在册基线）全等，**零新增 BLOCK／WATCH**（输出行计数＝1，无 WATCH 行）✓ 绿；同轮 python share/check-pointers.py --root . --target 回执件实路径 → **exit 0** ✓ 绿；同轮对票面（R2 票面）--target → **exit 0**（正文 V4 其余子目仍生效）✓ 绿。该枚既有悬空零处置＝另案候补池口径在册，本席确认未顺手修。
- **V5（钉值对拍）**：现跑 bash share/run-gates.sh → **exit 0·GATE PASS（发现 151502 条）**＝在册钉值 151502（CPPOOL 收口登记 151508→151502 随登后值）**全等零扰动** ✓ 绿；缺省 check-pointers 独立现跑（--root . 全域）→ exit 1·grep -c BLOCK ＝ **22810**＝在册缺省 BLOCK 钉值（收口登记 22816→22810）**全等** ✓ 绿；WATCH 计数同轮 4581 随登（无在册钉值冲突）。读数无摆动、无需归因链态。
- **V6（边界）**：git show --name-only 0da2566 ＝ **恰一件**＝落点件；git show --name-only 659ec9a ＝ **恰一件**＝回执件 ✓；对开工窗底 cbadb15..HEAD git diff --stat ＝ **两文件 67 插入**＝恰落点件＋回执件，此外零触；禁动面对拍（cbadb15..HEAD 限定 pathspec 域＝dev-discipline／share／ 全域／两票面／放行登记／双席快审判词＝**零文件命中**）✓ 绿；对票链窗底 4ea0d58..HEAD 全域＝恰六件（R2 票面＋双席快审判词＋放行登记＋落点件＋回执）＝票链自身件群＋施工两笔，零意外件 ✓ 绿。
- **禁动面复查（既有 58 行一字未改）**：落点件 diff 仅一个插入 hunk（8 行全为 "+" 前导），hunk 外零改动；插入段前后上下文行与 4ea0d58 版逐行仍在；节题序＝一（行 5）／二（行 9）／二之二（行 28·新）／三（行 36）／四（行 55）／五（行 62）＝编号与节序不动 ✓ 绿。

## 三、对抗臂三发读数

1. **篡改试验（机检有牙验证·不碰链上件）**：复制落点件到 .scratch／rctqav／ 下改名喂 check-pointers --target：追加假想悬空反引号指针（仓根相对不存在径）→ 被报 **BLOCK 行 68 指针悬空**（exit 1）；第二发追加包根相对形态反引号 token → 同样落网 **BLOCK 行 71 指针悬空**＝包根相对违例形态现制下已入 BLOCK 射程（原票 §四 候补 WATCH 判据面之现行覆盖佐证）。读数照登后两副本自删。附注：篡改副本行 24 额外多报一枚 ⟦references/90-changelog.md⟧ 悬空＝**副本落位所致解析伪影**（相对锚点随副本所在目录解析），链上原件 --target 读数仍恰一枚 BLOCK（本席 §二 V4′ 现跑坐实）＝非落点件缺陷、不归红。✓ 绿。
2. **回执正文写法复查（甲案自我实践面）**：回执件反引号 token 程序化提取（配对反引号正则）＝12 枚逐一目测归类＝仓根相对纯路径 2 种各 2 枚＋命令行／子命令片段 6 种，**含盘符形态 0 枚／包根相对形态 0 枚**＝条款第 2 目自我实践成立；回执内旧径提及居行 14／24＝裸文＋全角斜杠叙述态＝条款第 3 目允许形态、不入反引号集。✓ 绿。
3. **落点件插入后结构复查**：节题序列完整（§见上 §二 V6 行号布局）；markdown 围栏行计数＝2（偶＝配对闭合）；落点件 CR 字节计数＝**0**；回执件 CR 计数＝**0**；行号布局与回执 §三 宣称（行 26 既有末段／行 27 既有空行／行 28～34 条款块／行 35 新增空行／行 36 §三 节题）逐行对位吻合。✓ 绿。

## 四、红黄绿清单

- 红：0。
- 黄：0。
- 绿：10（V2′／V3／V4′落点差量／V4′回执自靶／V4′票面自靶／V5 双钉值全等／V6 三目／禁动面复查＝按判据位计数）＋对抗臂三发全绿（另计臂内附注一项＝篡改副本解析伪影，如实登记不归红）。
- 回执 §四 宣称读数对拍：8／0 新增删除、66 行、byte_equal=True、exit 1 恰一枚零新增、回执 exit 0、GATE 151502——六项与本席独立现跑**全部吻合**，零不实宣称。

## 五、完工纪律自证与自靶读数

- 只写本判词件一件；自靶 python share/check-pointers.py --root . --target 本判词件实路径 ＝ **exit 0**（读数见完工回报·落链前现跑坐实）；
- 单件 pathspec 两端齐带·add 紧邻 commit 零窗口·commit 前 git diff --cached --name-only 坐实仅自件·FX_COMMIT_DECLARE＝仓根相对纯路径挂 **commit 命令侧**·禁 add -A／禁 amend／禁 no-verify·message 以 collab: 起头·零 at 零反引号·尾标 [SWB-RCTPATH-R2-QAV] 置最末位·commit 输出重定向 .scratch／rctqav／·commit 类 timeout 十分钟档·撞锁有界等待零删锁；
- 他案脏面（ledger M 一枚＋仓根散件群 untracked）照登零带入零清理；链上 FUXI 笔群零碰；对抗臂产物居 .scratch／rctqav／ 自族目录已自删（v3 提取脚本与门禁输出留该目录随族自删）。
