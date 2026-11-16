# SWB-BKTCLS · 施工回执 v1（工程师席 eng-cpoolb1·回流四型＝完成）

- 性质 ＝ 施工完工回传件（回流四型之「完成」·票面 §二 施工目三笔全数落链）
- 票面 ＝ .scratch/tickets/2026-11-16-SWB-BKTCLS-桶名闭集机检规格票-v1.md（rev-1 段效力高于正文·V2 以 §八 两层射程为准）
- 放行登记 ＝ .collab/decisions/2026-11-16-SWB-BKTCLS-放行登记-v1.md
- 施工席 ＝ eng-cpoolb1（工程师席·单席在飞·一票一新鲜实例·未复用未并行）

## 〇、开工读数（现跑·禁抄在册旧数）

- git rev-parse --short HEAD ＝ 5c8efc8（＝放行登记笔链顶·与派工预期全等）。
- git status --porcelain --untracked-files=no 脏面照登＝ledger 一枚（agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl·M 态·他案脏面零带入·全程未碰）。
- 开工前置 GATE 现跑（迁册笔前）＝ bash share/run-gates.sh --root . --no-write → exit 0·GATE PASS 发现 151508（与放行登记随批钉值全等）。
- 桶面现盘＝仓根 .collab 一级目录 15 枚（含 qa）＋README＋一级散文件群照登零碰；git ls-files .collab/qa 计数＝7（与票面 §〇 预期全等）。

## 一、三笔链（一笔一 commit·增量落链）

| 笔 | sha | 件数 | 尾标 |
|---|---|---|---|
| 笔一 迁册 | 526b5ce | name-status 恰 7 对 R100（14 路径） | [SWB-BKTCLS-MOVE1] |
| 笔二 挂闸 | f530859 | name-only 恰 3 件 | [SWB-BKTCLS-BUILD] |
| 笔三 回执 | 本笔 | 恰 1 件（本回执） | [SWB-BKTCLS-RECEIPT] |

### 笔一（迁册笔·先）＝qa 桶存量违例消解

- 7 枚受跟踪判词件 git mv 入 .collab/audits/（取态唯一＝票面 §2-6 写死·defects 先例 c79dde9 同型）：A14QAEXEMPT-QA席审票／A14QAEXEMPT-产品席审票／SCRATCHCFG-QA席快审／SCRATCHCFG-QA席窄复核／SCRATCHCFG-产品席快审／SCRATCHCFG-产品席窄复核／SCRATCHG-QA席施工验收判词（各 v1）。
- R100 纯迁册内容零改字＝staged blob 七值对钉（250f27a4／a30a33ff／504757b6／e6072764／c16e9d8a／7884405f／bd024a46）·迁后 rmdir 空目录 qa·链上史笔不追改。
- 迁前／迁后 GATE 现跑＝151508／151508 全等零波动（迁册笔自身对发现数零影响·票面 §三 预期坐实）。
- 落链前 V2 两层预跑＝层一 ls-files 域 qa 前缀计数 0＋层二 7 枚新路径逐件 python share/check-pointers.py --root . --target 新路径 各 exit 0（内文零改自引形态仍可解析·零翻红·未触发停手上报条件）。

### 笔二（挂闸笔·后）＝三件

1. 新建 share/check-collab-buckets.py＝按票面 §2-1～2-5 规格实装：只读；扫描域写死仓根 .collab 一级子目录 os.listdir 单层不递归不扫嵌套；内嵌 frozenset 白名单 17 项（与 .collab/README.md 行 29「17 桶名录」现读逐项对拍全等）；违例行形态＝.collab/<桶>:1: BLOCK MC-BUCKET-1 桶名闭集违例（桶名 X ∉ 17 桶名录）（line 恒 1 照 check-collab-lint EAC-L3 目录级先例·兼容 run-gates FINDING_RE）；README 对拍自证＝运行时解析名录行反引号段（锚字样「17 桶名录」窗口 5 行·尾斜杠归一）集合≠内嵌集⇒输出 WATCH MC-BUCKET-1 名录漂移行（解析不到名录行＝exit 4 fail-closed）；仓根 .collab 不存在＝exit 4；零违例＝exit 0；一级文件不判；退出码闭集 0/1/2/4 照 60-gates §六；自咬纪律＝本件全文零反引号包径（照 check-collab-lint.py 头注先例）。
2. share/run-gates.sh 行 141 SCRIPTS 名单增一裸名项 check-collab-buckets（现读确认形态后单行编辑·diff 坐实仅该行·循环体／裁决 PY 段／SPEC_ID_HOME 映射零动）。
3. agent-skills/multi-collab/references/60-gates.md＝json 围栏 per_spec 增 "MC-BUCKET-1": {"commit": "block"} 一条目＋§四对账表增一条款行「仓根 .collab 桶名闭集校验」（判据一句话＋指向闸实体·不复写参数）；围栏恰一处复点＝1；per_spec 条目数 22→23（随登放行登记随批值）。

### 笔三＝本回执（落 .collab/receipts/·单件落链）

## 二、完工自检 V0～V6 现跑读数（回报用·正式验收归 fresh QA 席）

- V0 首跑归零＝挂闸笔起 GATE PASS exit 0·发现 151508（迁前／迁后／挂闸后三读数全等＝本闸贡献 0）·全量输出 grep -c MC-BUCKET-1 违例行＝0。
- V1 闸有牙＝臂一：mkdir .collab/zprobe 探针→单跑 python share/check-collab-buckets.py --root . →exit 1 恰 1 行 zprobe 违例（违例桶径前缀＋line 1＋BLOCK＋一句话全形态）→rmdir 复跑 exit 0；臂二：README 副本（.scratch/eng-cpoolb1/v1arm2/ 席族面·原件 git status 零触）名录行删 returns 一词→.collab/README.md:1: WATCH MC-BUCKET-1 名录漂移行出现 exit 1＝对拍自证有牙。
- V2 存量消解＝层一链上复点 git ls-files grep qa 前缀＝0；ls 仓根 .collab 零 qa 目录；git log --follow 新路径 exit 0（改名保史）；层二 7 枚新路径逐件靶检链上复跑各 exit 0。（rev-1 两层射程口径·全仓 grep 零命中表述未用作依据）
- V3 域口径复证＝agent-skills/fuxi-skill/.collab/defects 现盘在场（射程外事实）→单跑本闸该桶零命中行（只管仓根·裁甲复证）。
- V4 缺省钉值零扰动＝python share/check-pointers.py 现跑 grep -c BLOCK 跑前 22816／跑后 22816 全等（双读数落 .scratch/eng-cpoolb1/pointers-before.txt／pointers-after.txt）。
- V5 挂载形态＝git show --name-only 笔二恰 3 声明件／笔一恰 7 对 R100；run-gates.sh diff＝SCRIPTS 名单行恰增一裸名项其余零 diff；60-gates.md diff＝＋3/−1（per_spec 一条目＋对账表一行＋围栏尾逗号随动）·围栏恰一处·其余条目零动。
- V6 防自咬＝python share/check-pointers.py --root . --target share/check-collab-buckets.py exit 0；本回执落笔后自靶 exit 0（见下笔纪律段）。

## 三、插曲照登

- 零插曲：无撞锁（撞 index.lock 轮数 0·零删锁）；无他席卷入（commit 前 git diff --cached --name-only 每笔坐实仅票内声明件·ledger 脏面全程未 staged 未带入）；无 add -A／无 amend／无 no-verify；CRLF 转换 warning 两枚系 autocrlf 常态提示非异常照登。

## 四、禁动面自查坐实

- check-pointers.py／DEFAULT_SCOPE／豁免快照／SKIP 两表一字未动（V4 双读数全等佐证）；run-gates.sh 除 SCRIPTS 行外零动；60-gates.md 围栏其余条目零动；check-collab-lint.py 零动；嵌套 .collab 各包桶面零碰（V3 佐证）；仓根 .collab 一级散文件群零碰零清理；agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl 他案脏面零带入（收工 git status 复点仍在 M 态未入链）；链上 FUXI 笔群零碰；qa 桶 7 枚件内容零改字（R100 机械坐实）；dev-discipline／20-handoff 条款正文零动。

## 五、收工读数

- 收工 HEAD 现跑登记于完工回报（本回执正文写就于笔二链顶 f530859 之上）。
- 他案脏面收工照登＝ledger 一枚 M 态仍在·未带入任何笔。

## 六、纪律自证

- 一笔一 commit 增量落链；迁册笔 pathspec 只含 14 条 qa→audits 路径对（git mv 自带 staged·add 步骤无需）；挂闸笔三件各自 pathspec 两端齐带·add 紧邻 commit 零窗口·commit 前 git diff --cached --name-only 坐实仅票内声明件；FX_COMMIT_DECLARE＝每笔实触仓根相对纯路径清单前置（纯路径零描述句）；禁 add -A／禁 amend／禁 no-verify；message collab: 起头零 at 零反引号；尾标置最末位；commit 输出重定向 .scratch/eng-cpoolb1/ 席族目录；commit 类 Bash timeout 十分钟档；本回执自靶 exit 0 后方 commit；临时工作物居 .scratch/eng-cpoolb1/ 完工自删（commit 留证文件随席族自删·链上读数已全文登记于本回执）。
