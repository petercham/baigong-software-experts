# SWB-TMPLRULE-01（票①）收口登记（主理人收口笔）

## 〇、开工实测

- 落笔当轮 HEAD 复点＝`43d1a5c`（QA 判定笔＝链顶）；开工查盘轮 HEAD＝`ff46472`（工程师开工 ANCHOR 同值）。
- index 他案 staged 项一枚（`agent-skills/fuxi-skill/.collab/tickets/2026-11-10-FUXI-FX-U38-补课排产P2带五枚补充调研批次票-v1.md` M 态）＝他案 FUXI 在飞物，照登零碰；本笔 pathspec 隔离恰本件。

## 一、链条在册

1. 票面＝规则票 v1（架构席 arch-tmpl2 亲笔）落链 `dc19d82`，blob `d988f9fa540196ae9ae4e85978c73108f15d8552`；双席审绿判词在册（`7e34a4c`／`b58a793`）＋窄复核 `ea25f18`。
2. 放行＝皮总裁定「都批」登记笔 `e12afd3` 在册（落点定案取态乙＝条款并入基线本体）。
3. 开工查盘（主理人）：票面 blob 在 HEAD 与 `dc19d82` 全等＝未漂移；写集目标 `ticket-template.md` blob `a6ae67f` 且 `dc19d82..HEAD` 零触＝无先前执行残留；v2 草案锚 `1370153` 在链未漂移。
4. 工程师席 eng-tmplrule-b1（software-team-engineer 真专家席·单一 fresh 串行）两笔封顶完工：笔一条款笔 `2044c9b`（面单恰两件＝模板件追加 56 行零删除＋sop 技能 SKILL.md（全径 `agent-experts/baigong-software-team/skills/sop/SKILL.md`）版本行 1.0.0→1.0.1 恰一行）；笔二回执笔 `501a875`（回执 v1 新建 67 行落 `.collab/receipts/`）。零第三笔零 amend 零绕闸。
5. 主理人查盘核收相符：面单纯净、numstat 对上、`ff46472..HEAD` 差集恰三件⊆声明闭集、十二标志语独立 grep 全≧1、封口条款 L103 档位列表外单列、包版本三同源零碰。
6. QA fresh eyes 席 qa-tmplrule-v1（software-team-qa 真专家席·单一串行）独立验证判定件落 `.collab/audits/2026-11-10-SWB-TMPLRULE-01-QA席独立验证-v1.md`，判定笔 `43d1a5c`（面单恰判定件一件 80 行）。工程师回执对其只作对照禁采信、`.scratch/TMPLRULE-eng/` 全程禁读。

## 二、判定要点（QA 九判据＝红 0 黄 0 绿 9）

- 对账闭集＝两笔封顶面单纯净＋reflog 零 amend/reset；逐字照录＝自写 python blob 直读 difflib（autojunk off）1358 对 1358 字符全等、唯一差＝T9 段一处拆行适配（仅换行零改字单列归因）、删除行 0、T10 分级表对 v2 草案逐行在场。
- V1 十二标志语逐值在册；V2 diff 全集三件⊆闭集＋禁动面全空；V3 两净化身 worktree 对等两跑 BLOCK 归一 3116 对 3116 双向差集零新增＋主仓现盘 GATE PASS；V4 档位行 L94/L95/L96＋封口条款独立行 L103＝计数四；V5 他案 staged 零带入＋声明闸两笔在册；㊻㊺纯净性＝靶检三件 exit 0、并入段引用归因合规、`.scratch` 点名属字样非指针；回执对照逐值全对上无冲突。

## 三、异常登记（如实·均非阻断）

1. QA 落笔撞 index.lock 窗口（5 秒×40 试上限用尽前段他案 FUXI 链持续在飞）；共享 index 一度含他案 FUXI-U38 staged 态，声明闸共享面 fail-closed 咬「超额 1」＝闸正确行为非本案卷入；对策＝pathspec 两端齐带（next-index 视图）后续第 7 试成功，他案 staged 零碰零删锁零 amend。
2. QA 首轮对钉 blob 复算曾 sha1sum 直 pipe 漏 git blob 头误比，当轮以 blob 自哈希＋certutil 落盘双复自纠，两钉全等坐实——工具口径误差登记判定件备查。
3. QA 判定件首轮靶检抓到两枚悬空指针字样（run-gates 旧径字样＋他案在飞件径名），改字样写法复跑 exit 0——靶检闸有效实证。
4. 工程师席回报两笔落链后 index 出现他案 staged 项＝他案 FUXI 在飞（其后经 `dcdb497`/`a9167bd`/`7a16b9f` 自笔入库），本案两笔因 pathspec 两端齐带未被带入（面单实证）。
5. 工程师回执 V3 自述原始 BLOCK 计数 18251 不跨环境复现——QA 单列不采信不比对，以净化身 worktree 对等两跑口径为准。

## 四、候裁项销账（共享 index 并发风险成文开票）

- 本案收口呈报时曾候用户裁「混合笔 D-58 族第二实证＝共享 index 并发窗口风险成文开票与否」。该议题与 FUXI 案候补池 R12 行同题，用户已于 FUXI 案裁定并经誊录登记笔 `dcdb497` 在册：**R12 并发规矩不立＝不开票不成文不建提交排队机制；风险处置口径＝维持既有三防线（声明闸 fail-closed＋pathspec 两端齐带＋index.lock 有界等待零删锁）＋事后对账介质兜底**。
- 本案 QA 落笔异常 1 即该三防线的现场有效性实证（fail-closed 正确咬闸＋pathspec 隔离落链成功）。本案候裁项随该裁定销账，不再回流候裁；R12 池行销行或挂池取态归 FUXI 台账席随注（`dcdb497` 原话口径）。

## 五、排程随动与候办

- 模板线（工单规范三案）状态：规则票（票①）＝本登记收口成立；TOOLHOME（票②）已收口 `46d614c`；SEMGV-T6（票③）已收口 `d346acc`——**三票全链闭**。
- 挂账行（bundle.lock 组件一／二 note 同型过程字样）另票候排，不在本票面。
- 仓外临时区四处候用户处置：`D:\semgvt6-clone`、`D:\semgvt6-assemble-tmp`、`D:\semgvt6-assemble-tmp2`、`D:\qa-semgovt6v2-tmp`；本案 QA 仓外物（`qa-tmplrule-v1-tmp`＋两净化身 worktree）已自删附读数，工程师未用仓外物。

## 六、收口宣告

SWB-TMPLRULE-01（票①）质量链＝作者票 v1→双席审绿→放行「都批」→工程师两笔封顶→主理人查盘核收→QA fresh eyes 红 0 黄 0 绿 9→会师→本登记＝**收口成立**。T1–T10 条款并入票模板真源生效（新规向前进不追溯存量），模板件所属 sop 技能版本注记 1.0.0→1.0.1 随笔。
