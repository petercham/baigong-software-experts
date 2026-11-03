# ENG-S3 票三：G6 修订＋L2 同步句＋机检 MC-SEAT-DECL＋OA-D6-5（工程师席·交付面写入）

- 开端读数：devkits HEAD 以本票 commit 实测为准。
- HOLD 检查：无 HOLD——票三设计件（ARCH-R8·`9860f64`）在册，外部审票意见无未清项。
- 背景（决策依据·自包含）：三票序（拍板㊾）前两票已过 QA 双绿。票三按《票三施工输入设计-v1》（`.collab/research/2026-10-30-票三施工输入设计-v1.md`·`9860f64`）执行，主理人对设计件三候裁点裁决：①MC-SEAT-DECL 三读数 SEV 全 WATCH＋mode advisory＝按设计案（加重只改表不改脚本）；②quote 豁免仅全角引号＝采（更严不更松）；③声明闭集源格式＝票面显式 `声明闭集：` 行约定＝采。票分裁决＝**一票两 commit**（WP-1 文本面前置→WP-2 代码面后继·自举序：条文先落、机检后挂表，防「条文落而机检未落」半程态）。
- **逐字文本唯一来源＝设计件对应节**（设计件＝仓内可达过程件，其「定稿文本」段落系条款真源，照录不得改写；对其有异议停手上报）：
  - DD §二 整节替换文本＝设计件 §一.2；
  - L2 工程师同步句改后句＝设计件 §二；
  - object-audit 50-document D6 表新增行＋判定要点行＝设计件 §四。

## WP-1（文本面 commit·前缀 `ENG-S3a:`）改动面闭集

1. `workbuddy/baigong-software-team/skills/software-orchestration/references/dev-discipline.md`：§二 整节原地换代替换为设计件 §一.2 定稿文本（含新 §二.1-4＋原 §二.2/3 语义零动重编号 5/6＋原 §二.4 保留为 §二.7 仅机检参数列举面扩 D6-5）；SKILL.md `version: 1.0.5`→`version: 1.1.0`＋changelog（该包 changelog 件体例）登记行。
2. `workbuddy/baigong-software-team/agents/software-engineer.md`：「写权边界」节约束①句（现文 L154）整行替换为设计件 §二 改后句——逐字；该节其余与文件其余零动。
3. `deliverables/skills/object-audit/references/50-document.md`：D6 表 append 设计件 §四 新增行＋判定要点行（逐字）；该包 SKILL.md `version: 0.6`→`version: 0.7`＋其 changelog 登记行。
4. `workbuddy/baigong-software-team/.codebuddy-plugin/plugin.json`＋`bundle.lock`：本 WP 零动（版本账随 WP-2 收口批·bundle 每批 bump 镜像在 WP-2 落）。

## WP-2（代码面 commit·前缀 `ENG-S3b:`）改动面闭集

1. `deliverables/skills/object-audit/scripts/check-source-of-truth.py`：按设计件 §三 扩 C 段——`check_seat_decl()` 定向比对（节标题白名单定界／基线抽取单元恰一规则／括注豁免仅全角引号 ≤10 CJK 遮除／「本席」＋卷名 grep 双条件）＋基线快照 `baseline-seat-decl.json`（总量 ≥15 回裁线）＋自比对自咬五用例（含洗白反例＋真词条不误伤＋缺「本席」咬合）实跑附读数。
2. `deliverables/skills/object-audit/scripts/check-ticket-reconcile.py`（新脚本）：按设计件 §四 三段对账——段一 commit↔回执走 git name-only（实现体内禁 os.walk·结构性封死单面统摄），段二回执↔交付面、段三回执↔票面声明走交付面 listing；票面声明源＝`声明闭集：` 显式行；缺声明＝SKIP 不算绿；fixture 自咬实跑附读数。
3. `deliverables/skills/multi-collab/references/60-gates.md`（json 表）：挂两行——`MC-SEAT-DECL`、`OA-D6-5`（SEV WATCH·mode advisory·扫描面按设计件）；multi-collab `SKILL.md` version `4.9`→`4.10`＋`90-changelog.md` append v4.10 登记行（体例随现行账行·措辞自包含·必含要素：两 spec 进表首挂 advisory／版本账按包惯例取步／**MC-M1 顺延改 4.11 再登记防撞号**）。
4. `workbuddy/baigong-software-team/.codebuddy-plugin/plugin.json`＋`bundle.lock`：`0.1.8`→`0.1.9`；`README.md` 版本账 append 一行（措辞参考设计件 §5.3·体例随现行账行·自包含）。

## 自检与回执（N4·全部附实测载体）

- 每 WP：run-gates GATE PASS（附输出·WP-2 挂表后基线变化如实登记新旧条数）；check-source-of-truth 无新增 BLOCK；两新机检件自咬用例全绿读数；J6 对 L2 改后句四读数（增量/行长/最长重合 <12 现跑/grep 双条件）；版本前后值各附 grep/blob 实测（1.0.5→1.1.0／0.6→0.7／4.9→4.10／0.1.8→0.1.9）；净增行禁列终式扫描三分账。
- 回执落 `D:\multi-agent-collab-devkits\.collab\research\2026-10-30-ENG-S3-工程师回执-v1.md`：开端 HEAD＋**两笔交付 commit 各自 name-only 与各自 WP 清单全等**＋全部机制断言载体。回执单独 commit（前缀 `collab:`）。

## 红线

只动上述闭集；handoff-discipline 卷零触碰（条文真源已在位）；multi-collab 除 60-gates/SKILL/changelog 三件外零触碰；设计件定稿段落逐字照录一字不改；自举序不得颠倒（WP-2 不得先于 WP-1）；对设计件文本有异议停手上报。
