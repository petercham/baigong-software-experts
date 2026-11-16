# SWB-BKTCLS · QA 独立验收判词 v1（QA 席 qa-cpoolb1v·fresh eyes）

- 性质 ＝ 票级验收判词（判据集＝票面 §四 V0～V6＋rev-1 §八 两层射程口径＋追加对抗臂·一切判据独立现跑，工程师自检读数只作对照不作依据）
- 被验对象 ＝ 三笔链：526b5ce 迁册笔／f530859 挂闸笔／261743b 回执笔
- 票面 ＝ ．scratch／tickets／2026-11-16-SWB-BKTCLS-桶名闭集机检规格票-v1.md（§八 rev-1 效力高于正文·per_spec 基线 22／挂闸后 23·V2 两层射程为准·正文「全仓 grep 零命中」口径作废禁用）
- 放行登记 ＝ ．collab／decisions／2026-11-16-SWB-BKTCLS-放行登记-v1.md
- 回执（对照面）＝ ．collab／receipts／2026-11-16-SWB-BKTCLS-施工回执-工程师席-v1.md
- 本席纪律 ＝ 只读＋现跑取证＋探针即做即删零残留·临时工作物全程居 ．scratch／qa-cpoolb1v／·唯一写＝本判词件

## 〇、开工读数（本席现跑·禁抄在册旧数）

- git rev-parse --short HEAD ＝ 261743b（＝回执笔链顶·与派工预期全等）。
- 开工脏面照登＝agent-experts／baigong-software-team／．collab／ledger／ledger．jsonl 一枚（M 态·他案脏面·全程零碰零带入）；仓根一级散文件群＋untracked 案卷散件群照登零碰。
- 仓根 ．collab／ 一级现盘＝14 目录＋README＋一级散文件群（17 枚 md 案卷）·零 qa 目录（ls 现读坐实）。

## 一、逐判据红黄绿（全部本席独立现跑）

### V0 首跑归零 ＝ 绿

- bash share／run-gates．sh --root ． --no-write → exit 0·GATE PASS（发现 151502 条）。
- 全量输出 grep -c MC-BUCKET-1 ＝ 0（违例行零）。
- 本闸行读数＝⟦check-collab-buckets：一级目录判 14 枚｜违例 0｜名录对拍 一致⟧＝本闸对发现数贡献 0 坐实。
- 发现数对基面 151508 差 6＝如实登记（见 §三 归因项·非本闸贡献·V0 判据两目 exit 0＋grep 0 全中）。

### V1 闸有牙 ＝ 绿（双臂）

- 臂一（真桶面探针）：mkdir ．collab／zprobe → python share／check-collab-buckets．py --root ． → exit 1·恰 1 行违例＝⟦．collab/zprobe:1: BLOCK MC-BUCKET-1 桶名闭集违例（桶名 zprobe ∉ 17 桶名录）⟧（行形态含 冒号1冒号 BLOCK MC-BUCKET-1 全形态）→ rmdir 复跑 exit 0·ls 复点 zprobe 残留 0。
- 臂二（等效试装·副本面）：脚本 README 路径无参数化（读死 --root 下 ．collab／README．md）——本席等效设计＝scratch 族内造探针根 ．scratch／qa-cpoolb1v／arm2root／（仅含 ．collab／README．md 副本）→ --root 指探针根跑。
  - 试装甲（名录行删 returns 一词·反引号段保留）→ exit 1·WATCH 漂移行出现＝⟦．collab/README.md:1: WATCH MC-BUCKET-1 名录漂移（README 名录行解析集 ≠ 脚本内嵌集：仅README有=- 仅脚本有=returns）⟧＝对拍自证有牙坐实。
  - 试装乙（意外收获·名录行反引号段整体删净）→ exit 4 infra error＝⟦README 名录行解析不到（锚字样命中但窗口内无反引号段）⟧＝fail-closed 对拍自证失效不得静默放行行为在册坐实。
  - 原件零触＝git status --porcelain 对 ．collab／README．md 全程空输出。
- 探针面全部即做即删·复扫零残留（见臂C）。

### V2 存量消解（rev-1 两层射程）＝ 绿

- 层一（路径面）：git ls-files 输出 grep -c 仓根前缀 ．collab／qa／＝0；仓根一级 ls 零 qa 目录；git log --follow 迁后新路径（SCRATCHG-QA席施工验收判词-v1．md）exit 0 改名保史（526b5ce 追至 9278445 落 qa 桶史笔可续）。
- 差量照登＝git ls-files 无锚 grep 字样 collab／qa 命中 66 枚＝分布对拍：agent-experts／baigong-software-team 4＋agent-skills／external-advisor-collab 2＋agent-skills／fuxi-skill 60＝全落裁甲豁免嵌套包面（票面 §〇 射程外事实在册）＝仓根域内归零成立，与 rev-1「全仓字样不可满足」论证一致。
- 层二（内文面）：7 枚迁后新路径逐件 python share／check-pointers．py --root ． --target 各 exit 0（七值读数 0／0／0／0／0／0／0 全绿·内文零改自引仍可解析零翻红）。

### V3 域口径 ＝ 绿

- agent-skills／fuxi-skill／．collab／defects／ 现盘在场（内件一枚现读）→单跑本闸全输出 grep -c defects＝0＝嵌套包桶零命中·只管仓根裁甲复证。

### V4 钉值零扰动 ＝ 绿

- python share／check-pointers．py 独立现跑：跑前 grep -c BLOCK＝22810／跑后 grep -c BLOCK＝22810＝前后全等零扰动（双读数落 ．scratch／qa-cpoolb1v／pointers-before．txt／pointers-after．txt）。
- 与在册钉值 22816 差 6＝如实登记（同 §三 归因项·票面 V4 原文口径「22816 或当轮实测值」＝当轮实测 22810 在判据口径内·前后全等目坐实）。

### V5 挂载形态 ＝ 绿

- git show --name-only 三笔＝笔一恰 7（R100 迁册对 name-only 形态·name-status 复点恰 7 对 R100 全 14 路径 qa→audits）／笔二恰 3 件（share／check-collab-buckets．py·share／run-gates．sh·agent-skills／multi-collab／references／60-gates．md）／笔三恰 1 件（回执）＝各恰声明闭集。
- git diff f530859^ f530859 -- share／run-gates．sh＝恰 SCRIPTS 名单一行增一裸名项 check-collab-buckets·循环体／裁决 PY 段／SPEC_ID_HOME 映射零 diff 坐实。
- 60-gates．md＝json 围栏现跑计数恰 1（grep -c ```json＝1）；python 解析围栏：per_spec 条目数＝23（挂闸前基线 22＋MC-BUCKET-1＝rev-1 口径全等）·MC-BUCKET-1 路由＝commit block·on_severity 3 档／escalate 5 键零动；diff＝per_spec 增一条目＋§四对账表增一条款行（判据一句话＋指向闸实体不复写参数）＋尾逗号随动＝其余条目零动。

### V6 防自咬 ＝ 绿

- python share／check-pointers．py --root ． --target share／check-collab-buckets．py → exit 0；--target 回执件 → exit 0（双靶全绿·本判词落笔前自靶见 §五）。

## 二、追加对抗臂 ＝ 全中

- 臂C-1（诚实口径复算）：V1 探针删净后单跑闸复扫＝exit 0·⟦一级目录判 14 枚｜违例 0｜名录对拍 一致⟧＝zprobe 零残留；全闸 V0 输出 grep MC-BUCKET-1＝0 复证。
- 臂C-2（集合级对拍·非逐词目测）：python 独立解析（不调闸）README 名录行反引号段集 vs 脚本 BUCKET_WHITELIST frozenset 字面抽取集＝17 对 17 全等·两差集皆空。
- 臂C-3（让闸失灵尝试）：①点前缀违例目录 ．collab／．dotprobe→BLOCK 命中（违例形态行恰 1·点前缀目录照判＝目录判定不以点开头豁免）；②嵌套层级 ．collab／audits／nestedprobe→零命中＝单层射程不递归坐实（os．listdir 写死与规格 §2-2 全等）；③探针 rmdir 复跑 exit 0 零残留。真桶全程未破坏（audits 内 nestedprobe 为空目录即建即删·桶内受跟踪件零触）。

## 三、差 6 登记项（不归本闸·不归本批）

- GATE 发现数本席现跑 151502 与在册基面钉值 151508 差 6；check-pointers 缺省 BLOCK 本席现跑 22810 与在册钉值 22816 差 6＝两读数互证同链态同盘面（本席窗内自洽），差值同枚数＝同源。
- 归因登记：①本闸贡献 0 机械坐实（V0 闸行读数违例 0·V4 前后全等）；②票面 §八 随注已在册同型差（起草窗 151502 vs 钉值 151508 差 6＝QA rev 轮现跑回钉 151508·归因链态差异不追因）＝本席当轮读数与起草窗读数值全等复现（151502），在册钉值与施工窗三读数（151508）差因居链态／盘面漂移（含 fuxi 包 ．scratch 族受跟踪探针面参与扫描域之链态波动），非本批三笔任何一笔贡献（三笔 name-only 闭集内无件落 check-pointers DEFAULT_SCOPE 缺省扫描域＝迁册对居仓根 ．collab／、挂闸三件居 share／与 multi-collab 规范件、回执居 ．collab／receipts／）。
- 按票面钉值随登义务口径：差值逐项归因毕·本闸贡献行数＝0＝登记绿不判红；后续轮钉值以当轮现跑为准（22810／151502 随登）。

## 四、总裁决

- **IS_PASS**
- 计数＝绿 7／黄 0／红 0（V0～V6 七判据全绿·追加对抗臂全中·差 6 登记项不归本闸不归本批）。
- 一句话＝闸有牙（违例 BLOCK／漂移 WATCH／解析失效 exit 4 三态全实测触发）·存量两层消解坐实·域口径写死复证·挂载三笔恰声明闭集·钉值零扰动·防自咬全绿。

## 五、纪律自证

- 本判词落笔前自靶 python share／check-pointers．py --root ． --target 本判词路径 exit 0 后方 commit（读数落 ．scratch／qa-cpoolb1v／selfgate．txt）。
- 只读零写（唯一写＝本件）；探针即做即删零残留（zprobe／arm2root／dotprobe／nestedprobe 四探针面全删·终扫坐实）；他案脏面 ledger 一枚照登零带入；本席临时工作物居 ．scratch／qa-cpoolb1v／。
- 单件 pathspec 两端齐带·add 紧邻 commit 零窗口·commit 前 git diff --cached --name-only 坐实仅自件·FX_COMMIT_DECLARE 纯路径前置·禁 add-A／禁 amend／禁 no-verify·message collab: 起头零 at 零反引号·尾标置最末位·commit 输出重定向 ．scratch／qa-cpoolb1v／·timeout 十分钟档·撞锁有界等待零删锁。
- 开工读数＝261743b；收工读数现跑登记于完工回报。

（判词完）
