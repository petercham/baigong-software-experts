# ITER-W1-T1c · 判词统一命名与收口-验收配对机检票 · 工程师席施工回执（v1）

- 席位署名＝engineer 席·施工＝eng-iter-t1c（两枚写集改盘完成）＋接手投递＝eng-iter-t1c2（BUILD＋RECEIPT 两笔投递·只投递零重写逻辑）——接手投递案型如实登记见 §五
- 票面＝.scratch／tickets／2026-11-18-ITER-W1-T1c-判词命名与配对机检票-v1.md（157 行·blob debc64aa）；放行登记（含 §六 rev-1＝变体二并集＋V4 三跑制）＝.collab／decisions／2026-11-18-ITER-W1-T1c-票级放行登记-v1.md
- EFFECTIVE_DATE 字面值＝**2026-11-18**（J-5 采甲＝BUILD 笔落链当日·S1 常量写死＝验收对钉值）
- 本回执一次成文（append 不适用）·零反引号零 at·叙述裸文＋全角斜杠·命令缩进段。

## 〇、开工读数（接手席 eng-iter-t1c2 当轮现跑·禁抄旧数）

    date 现跑＝2026-11-18（15:41 窗）
    git rev-parse --short HEAD ＝ fa1d8196＝对钉全等命中（＝放行登记 rev-1 笔链顶现势·零后继）
    链序 git log --oneline -4 --format='%h %p'＝fa1d8196→ff9a55c4→7a68d6e4→3bc1f5a5 父子^逐笔相衔零断
    ls .git／index.lock＝NO_INDEX_LOCK（worktree 独立 index·gitdir＝主仓 .git／worktrees／baigong-software-team 现核）
    git status --porcelain 脏面照登＝tracked M 恰两枚＝本票写集两枚（share／check-collab-buckets.py＋agent-skills／multi-collab／references／60-gates.md·前席改盘未投实态）＋staged 零枚＋?? 零枚（他案脏面在主仓侧·本 worktree 零带入）
- 票面与放行件 blob 双对钉现跑＝票面链上 blob debc64aa（盘 sha256 现算 7e37590f…）＋放行件链上 blob b32b9572（盘 sha256 现算 2a09db16…）＝盘链双在
- 靶件基线三面（改前链上态）＝check-collab-buckets.py 链上 blob 922fe2e9／git show wc -l ＝169 行；60-gates.md 链上 blob b68cbfc7／179 行——与票 §四 V1 钉值全等命中。改后面＝check-collab-buckets.py 312 行（盘 sha256 f598bd56…）；60-gates.md 183 行（盘 sha256 6982cb15…）。

## 一、BUILD 笔施工读数（票 §三 S1／S2＋放行登记 §三＋§六 rev-1 终态为准）

- 施工面构成＝前席 eng-iter-t1c 按 rev-1 裁定完成两枚写集改盘（MC-PAIR-1 配对段＋EFFECTIVE_DATE＝2026-11-18 入 S1；S2 三处落文入 60-gates）；接手席核验口径＝语法级检查＋断言读数，零逻辑重写、零修正（py_compile 现跑 OK＝无语法级错误触发改写条件）。
- 程序化断言读数（接手窗现跑·逐断言 PASS）：
  - S1 后置断言＝MC-PAIR-1 字样恰 6 处（≥1 PASS）／def scan_pair 恰 1（PASS）／主流程挂载行 scan_pair(root 在位（PASS）／EFFECTIVE_DATE ＝ "2026-11-18" 常量在位（PASS）／退出码闭集段零改照 diff 面核（PASS）／python -m py_compile exit 0（PASS）
  - S2 后置断言＝json 围栏恰 1 处（PASS）／per_spec 由 23 增至 24 键·恰一增·MC-PAIR-1 在 per_spec（PASS）／MC-PAIR-1 解析行在 §四 对账表＋命名口径条款段落文在位含字样 MC-PAIR-1（PASS）
- 落笔坐实＝add 单 pathspec 紧邻 commit；commit 前 staged 面单现跑恰两枚（git diff --cached --name-only ＝ 2）；FX_COMMIT_DECLARE 挂 commit 命令侧＝仓根相对径两枚逗号分隔；commit pathspec 同带两枚；message -F 承载＋输出重定向落盘＋有证转后台；钩子 STAGED-DECL 与 ALLOW_GATE_DOWN 读数见 BUILD 笔链上 message 与 .scratch／t1cbuild／commit-build.out（取证族在册）。
- BUILD 笔 git show --numstat＝check-collab-buckets.py 155／12＋60-gates.md 4／0＝恰两枚零越界（与 V3 同读数）。

## 二、V 系全套读数（接手窗现跑·票 §四＋放行登记 §六 rev-1 三跑制勘正版为准）

- V0 开工读数＝见 §〇（HEAD fa1d8196 对钉＋链序零断＋NO_INDEX_LOCK＋脏面照登两枚）。
- V1 靶面钉值零漂移（开工窗对拍）＝check-collab-buckets.py 改前 169 行／60-gates.md 改前 179 行／json 围栏恰 1／per_spec 改前 23→改后 24（恰一增＝预期内改面非漂移）／仓根 audits 桶 tracked 现跑 70 枚＝对票 §二 钉值全等命中。
- V2 施工动作断言读数＝见 §一（前后置断言全 PASS；前席改盘为既成事实面，本席以断言面复核）。
- V3 落盘坐实＝BUILD 笔 git show --numstat 恰两枚＝S1 M（155／12）＋S2 M（4／0）；零越界（对照 §三 闭集两枚）。
- V4 三跑制（rev-1 勘正口径·三跑各自现跑）：
  - 跑①主仓根桶面＝python3 share／check-collab-buckets.py --root 主仓根 --seg bucket ＝ exit 0＝「一级目录判 14 枚｜违例 0｜名录对拍 一致」（MC-BUCKET-1 存量判据面·取证落 v4-1-mainroot-bucket.out）
  - 跑②worktree 根配对面＝python3 share／check-collab-buckets.py --root . --seg pair ＝ exit 0＝「配对段：生效日 2026-11-18｜收口件在判 1 枚｜判词件命中 1 枚｜配对违例 0」（MC-PAIR-1 面＝rev-1 变体二并集实现坐实·取证落 v4-2b-wt-pair.out）；另跑 --seg all＝exit 4＝「infra error: 仓根 .collab／README.md 不存在」＝MC-BUCKET-1 本体面在 worktree sparse 域不落盘＝rev-1 在册预期案型（配对段先行输出未被吞·取证落 v4-2-wt-all.out）＝不归因本施工
  - 跑③60-gates 自靶＝worktree 域 python3 share／check-pointers.py --root . --target agent-skills／multi-collab／references／60-gates.md ＝ exit 1＝OA-D6 悬空三目标四行面（行5／111／173／181）；开工基线对拍＝HEAD 态 60-gates-head-copy.md 同域同参现跑 exit 1＝OA-D6 三目标四行（行5／110／169／177）＝目标集全等零新增（diff 对拍坐实）＝按 §四／rev-1 例外归因＝sparse 缺件存量案型不归因本施工；主仓根域另跑＝exit 1＝一枚存量悬空（deliverables 径 handoff-discipline）＝同为存量随登不归因（取证落 v4-3b／v4-3c／v4-3d）。S1 自靶＝check-pointers --target share／check-collab-buckets.py exit 0（取证落 v4-3a）。
- V5 缺省扫描＝只平引取证族在册件不另跑：post-rungates-main.out／post-rungates-wt.out（前席改后全量窗读数·居 .scratch／t1cbuild／）；其中 worktree 窗 check-collab-buckets exit 4／check-source-of-truth exit 2／FX-HOOK-1 BLOCK＝均放行登记 §四 在册缺件与 hook 漂移案型＝不归因本施工；主仓窗计数行口径照旧。
- V6 入线四词＝对施工笔 diff 面逐词现跑＝真源形态／文件域／席位职权／工序链：S1 面 0／0／0／0＋S2 面 0／0／0／0＝零命中＝标准档维持不升档。

## 三、禁动面逐项零触坐实（接手窗现跑）

- share／check-ticket-reconcile.py／share／run-gates.sh／sop 模板三件／closeout-template／.gitignore／包 .collab 其余＝git diff --stat 对上全部具名面＝空输出＝byte 零扰动。
- 桶面计数＝仓根 audits 桶 tracked 70 枚＝对票 §二 钉值不变；audits／decisions／receipts 三桶本两笔零增删（除本回执一枚 receipts 新增＝回执笔本责）。
- 链上史件零回改＝两笔均 add 正向落链无 amend／rebase；账本零手写（.collab／ledger／零触碰）；.gitignore 零触；FUXI 零碰（git status 现跑 FUXI 面零枚）；他案脏面零带入（worktree staged 零枚·?? 零枚）。

## 四、取证族处置

- 取证族具名＝.scratch／t1cbuild／：dispatch-eng-iter-t1c.md、probe_pair.py、fixture／、return-report.md（前席阻塞回流件）、60-gates-head-copy.md、build-diff-added.txt、prefix-rungates-main.out、post-rungates-main.out、post-rungates-wt.out、v4-wt-all.out＋接手窗新增 v4-1-mainroot-bucket.out、v4-2-wt-all.out、v4-2b-wt-pair.out、v4-3a-cp-s1.out、v4-3b-cp-60g-wt.out、v4-3c-cp-60g-headcopy.out、v4-3d-cp-60g-mainroot.out、buildmsg.txt、commit-build.out、return-report2.md。
- 处置口径＝**保留不拆**（偏离票 §六「用毕即拆」的随登申明）：本票为接手投递案型＋验收段＝fresh QA 需复核对拍基线件（60-gates-head-copy 与 v4 系读数＝V4 例外归因对拍锚）；.scratch 域＝git 排除面不入链零脏链风险；拆除归收口段处置随验收完成后另笔执行。

## 五、案型登记

1. **前席回报自述与实态不符（append-only 更正径）**＝eng-iter-t1c 阻塞回流件（return-report.md·2026-11-18 14:45 窗）自述「零交付·两枚写集文件零扰动·git status index 净」；主理人现跑坐实＋本席开工读数复核＝两枚写集已改盘未提交（M 恰两枚·numstat 155/12＋4/0）。处置＝回流件本体不回改（append-only）·更正效力＝本回执本节＋BUILD 笔 message 随登；该两枚改盘内容经 rev-1 裁定口径核验（语法级＋断言面）后由本席投递。根因观察＝回流窗与改盘窗时序不一致（文件 mtime 15:28-15:34 晚于回流件 14:45）＝自述滞后于自身后改＝如实登记不代断。
2. **staged／改盘悬挂案型第四枚**＝前席两枚写集改盘未投即收尾＝继 W0B 产品席／T1b 工程师席回执／T1b 产品席收口三枚「staged 悬挂未投即收尾」案型后同族第四枚（本枚形态＝worktree 脏面悬挂非 staged）。处置＝主理人有证接手投递（本两笔）。归因随登＝派工书级纪律无约束力实证续增·落链门禁归 W2-T2d 挂账在册。
3. hook 载体层漂移案型沿用＝ALLOW_GATE_DOWN=1 留痕绕过投递（pre-commit 链·声明闸照常跑·bypass 证据件＝commit-build.out 在册·非静默）＝漂移本体归 W2-C1 对账票。

## 六、本笔纪律自证（RECEIPT 笔）

- 面单恰回执一枚＝本件（add 单 pathspec 紧邻 commit·FX_COMMIT_DECLARE 挂 commit 命令侧＝本回执仓根相对径）。
- 落笔前自靶＝python3 share／check-pointers.py --root . --target 本回执实路径 exit 0（读数随 BUILD/RECEIPT 投递窗）。
- 收尾自证＝两笔投后 git status 现跑＝两枚写集与回执全部归零（index 净＋无残留 M）；取证族保留申明见 §四；本回执零反引号零 at。
