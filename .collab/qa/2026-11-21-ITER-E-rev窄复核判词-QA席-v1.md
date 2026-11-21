# ITER-E rev-1 窄复核判词（QA席·rev 段五处闭合＋append-only 自证＋红3互斥消除·不复扫全票旧绿面·判词生产者＝QA席·投递归主理人）

出品＝BG／QA席 qa-e-rev2／2026-11-21
出品锚＝baigong-software-experts｜main｜c567372666c58860b6e970023886966f7be99d67｜2026-11-21T12:08:03+08:00（四值＝git remote get-url origin 末段仓名／git branch --show-current／git rev-parse HEAD／date -Iseconds 全部开工窗现跑）
版本行＝v1 一次成文·append-only·后续修订票尾续 rev 段互不回改
复核对象＝.collab／architect／2026-11-21-ITER-E-仓库结构归位与史面收编-规则票-v1.md（rev-1 后终态＝270 行／f62b97b5d60a8faa005f2a98297efa5a7866f473）
对照件＝.collab／qa／2026-11-21-ITER-E-审票判词-QA席-v1.md（本席上轮·红〇黄二绿八）＋.collab／product／2026-11-21-ITER-E-审票判词-产品席-v1.md（红一黄二绿十四）
复核射程＝rev 段五处闭合＋append-only 零回改自证＋红3（双席黄差）互斥消除＝只此七项，v1 旧绿面不复扫（派工口径）。

## 〇、对钉读数段（本席开工对钉·全部现跑）

- HEAD＝c567372666c58860b6e970023886966f7be99d67＝派工预期 c5673726 全等；链顶＝c5673726（rev-1 落件笔·尾标 -RECEIPT 合规零粘连）父 be213e64（产品席判词笔）父 52847995（本席判词笔）＝逐枚相衔零断（git log 现跑）。
- 票面终态现跑＝270 行／git hash-object＝f62b97b5d60a8faa005f2a98297efa5a7866f473＝派工钉值全等。
- append-only 零回改自证复跑＝head -n 238 管道 git hash-object --stdin --path 票面路径＝4c2703de01a05b8efb0ff7d6e07073f70253fbb0＝双席判词登记前段基线全等＝前 238 行逐 byte 零回改坐实。
- index.lock 现读＝无；脏面＝?? 簇照登（.DEVKITS-POINTER.bak／flatten 族取证残留／msg 族／agent-skills 目录面）照登零带入＝与本席上轮登记同族零变化。

## 一、七项逐判（红／黄／绿·逐项现跑取证）

### 复核项1 对钉＝绿

- 见 §〇：HEAD／票面行数与 sha／前段零回改三钉全等；三值任一不合即停手条款未触发。

### 复核项2 红一闭合核＝绿

- rev 段勘正三数现读（票面 L247—251）＝旧世代对照 39／ignore 桶 129／等式 5＋39＋129＝173 ✓＝与本席上轮独立复跑值（判词黄①）逐值全等。
- 本窗台账再复跑（quar_orphans.txt 管道现跑）＝总基数 grep -c 现跑 173／wc -l 172（末行无换行案型采 173＝口径沿册）；顶桶分布＝.collab 134／skills 26／tests 7／config·docs·README·bundle.lock·plugin.json·.codebuddy-plugin 各一；.collab 内层＝decisions 1／dispatch 8／evidence 99／ledger 1／refs 25；evidence 子目录群现跑＝blind-eval 1＋corpus-t9 22＋gates-fuxi-t03 2＋gates-zhulong-t02 8＋harness 56＋publish 6＝95＋散枚 4＝99 自洽。
- 按勘正桶算复跑＝旧世代对照 26＋7＋6＝39 ✓；ignore 不收编 8＋25＋1＋95＝129 ✓；收编 5＋39＋129＝173 ✓＝与孤本基数全等＝真闭合。
- 成因句核＝「132 只能由 8＋25＋99 凑出＝evidence 散四枚既计收编又再计 ignore＝双计」＝与本席上轮黄①归因句全等（99 含已收编散四枚＝双计机理成立）。
- 逐桶归因零改动核＝v1 条款一／条款三理由句在位逐字照存（append-only 前段 hash 全等即前 238 行零动的机械自证＝理由句零改动随之成立）；rev 段 L252 零改动申明与实际相符。

### 复核项3 黄一裁决复核（九枚交叉验证）＝绿

- 机理行号独立对读（share／check-pointers.py 本窗现读）＝架构席引用全部成立：L128 load_exempt 把 items 逐条目建成「token 文本→命中文件集合」表（L142—149 键＝item 的 token 原文·值＝frozenset）；L385 逐 token 循环（反引号正则 findall＝同行多 token 各自入扫）；L412 豁免查表键＝tok＝反引号 token 原文（行号未剥＝带行号形态 token 之豁免键必带行号态；剥行号仅发生于 L396 strip_pointer_form 后缀归位层＝引用句相符）；L413 命中文件∈集合→出 WATCH 历史豁免行（L413—418）；L420—421 每未解析 token 独立 append 一条 BLOCK＝无按行去重层＝推论「一条目抵一 token·漏任一即该条照 BLOCK」成立。
- 独立夹具复跑（本窗现跑）＝收编五枚自隔离区 evidence／decisions 桶只读复制入 .scratch／ITER-E-qa-rev2／fixture／＝git hash-object 五值对钉票面 §二.9 全等（66b667a3／740501f1／74413e0d／f0dcfff5／61942554）＋行数 30／97／152／78／60 全等；check-pointers --target 逐枚现跑＝收官呈拍简报 exit 0 零发现／deepresearch 判词 BLOCK 悬空一枚（L4）／video-gate 判词四枚（L6 一枚＋L103 同行三枚各自独立成条：handoff-ledger／director-self-check／shot-plan-approach）／deepresearch-01 回执一枚（L38）／回修回执三枚（L17＋L23＋L36＝其中 :69 与 :16 行号态两枚坐实）＝悬空计数 1＋4＋1＋3＝九枚。
- 裁决「九」＝九立＝与架构席 rev 段裁决、本席上轮夹具读数三方全等；产品席「八」（1＋3＋1＋3）归因＝按行去重人工计数（L103 三枚并作二枚）＝非闸行为（L420 逐 token 独立成条现读反证）＝红3 互斥消除＝九裁死成立。
- 夹具用毕即拆＝rm -rf 后 ls 坐实零命中＝FIXTURE_REMOVED（本席夹具位＝.scratch／ITER-E-qa-rev2／含夹具父目全拆）。

### 复核项4 黄二注记核＝绿

- ⑥基数注记现读在位（票面 L263）＝三要素齐：物理基数 942 枚不变（零删申明）／孤本属性基数 173→168（收编五枚入链后非孤本＝⑥裁时删之无损）／⑥总单引用口径须随注现值 168＋终删权仍候⑥＝本段零删零动。
- 票面禁删红线复跑＝全文 grep 删除族现跑：rm 命令命中仅一枚＝L93 P1 命令段 rm -f 指 .git／info／sparse-checkout（派工 F1 段具名＝非隔离区面）；其余「删除」字样命中＝L24／L111 派工引文禁写删除项句、L186 numstat 删除列、L215 边界②零删除动作申明＝皆非删除动作项＝零违例。

### 复核项5 「八→九」置换完备核＝绿

- 具名覆盖声明现读在位（票面 L256）＝覆盖清单六句逐句现读命中：§三 配套必自面条款内「悬空存量指针八 token」「必增 BLOCK 八枚」「尾续 items 八条目」「八 token 逐枚入 items」四处＋§四 V5「G9 八 token 豁免抵收支编增量」一处＋§五 自决不列申明④「G9 豁免八 token」一处＝六句全正为九 ✓；随裁施工口径更新句在位（items 尾插九条目＝deep-research 两 token 按行号态分列两条目）＋清单效力优先申明（现数九枚＝单列七行＋末行明书两 token 各一）。
- 残留扫描现跑＝全文「八 token／八条目／八枚」族命中行＝26／32／116／209／225＋L256 覆盖句自身引用＝覆盖声明（L256）之后（L257—270）零残留 ✓；覆盖声明之前命中属 append 覆盖效力正常射程。
- 归因注记一枚（不计数不入黄）＝L26／L32 两处「写集八枚」＝G1—G8 写集枚数口径（G9 于同句另列具名），非 G9 token 计数句＝不在 rev 裁决射程与本次覆盖清单定义内＝v1 旧面措辞观察项照登（写集逐枚具名枚举无歧义、可施工性不受影响；§〇 九枚口径在册）＝不入黄不处置。

### 复核项6 终态闸自靶＝绿

- check-pointers --target 票面终态现跑＝exit 0 零发现（rev 段新面含缩进段命令与 token 清单 verbatim＝指针面过闸）。
- check-ticket --target 票面终态现跑＝BLOCK 0／WATCH 0 exit 0。
- 缺省扫描读数照登（只平当轮同点对拍·不作裁）＝check-ticket 缺省＝BLOCK 34／WATCH 0 exit 1（本席上轮锚 33 差 +1＝增量归因＝链笔 be213e64 尾标 -PROD-REV 闭集外 CT-6 命中现读具名＝他案投递侧增量非票面引入；rev 笔 c5673726 尾标 -RECEIPT 合规不入违例）；check-pointers 缺省＝BLOCK 2790／WATCH 997 exit 1＝与票面 §二.10 钉值逐值全等＝存量族只平；buckets 闸缺省＝exit 1／配对违例 1／汇总行「生效日 2026-11-18｜收口件在判 14｜命中 13｜违例 1」＝与 §二.8 全等＝F4 未施工＝改前态在册只平。

### 复核项7 判词自靶＝绿（读数随回报补登）

- 本判词写毕后 check-pointers --target 本判词现跑＝exit 0（读数随回报）；零反引号零 at 字符现算＝各零枚；判词体例＝裸文＋全角斜杠·命令居缩进段＝自查过。
- check-ticket 对判词件非零＝链上判词先例同态存量常态（本席上轮判词 rev 补登段在册）＝不入本判词违例不追。

## 二、结论句

- 红〇／黄〇／绿七。
- 结论＝可放行。rev-1 五处闭合全部成立：红一三数勘正与真账闭合复跑全等；黄一「九」裁决经机理行号对读＋独立夹具复跑（1＋4＋1＋3＝九）三方交叉验证裁死＝红3 互斥消除；黄二⑥基数注记在位＋禁删红线零违例；append-only 零回改机械自证全等；置换覆盖六句齐＋声明后零残留；终态闸自靶两闸 exit 0。
- 施工窗带下口径沿册＝G9 必按 verbatim 清单九枚入 items（:69 与 :16 行号态分列两条目＝豁免键带行号态＝机理现读坐实）；⑥总单引用孤本口径现值 168 随注。
- 观察项一枚（不入黄不处置）＝票面 L26／L32「写集八枚」旧措辞（写集枚数口径非 token 计数）＝归因照登见复核项5。

## 三、席位纪律段

- 本席夹具一处＝.scratch／ITER-E-qa-rev2／（收编五枚试挂复制件）＝判词落盘＋自靶复跑毕 rm -rf 拆除＋ls 坐实＝FIXTURE_REMOVED 登记见复核项3。
- 本席全程零 git 写（add／commit／amend／stash／checkout／restore 零触）；git 只读命令＝rev-parse／log／ls-files／hash-object／branch／remote／status 未禁面内；隔离区只读零写零删。
- 本判词自身哈希不入正文（自算即自变案型沿守）＝终态行数与 sha 随完工回报消息具名。
- 尾标＝判词笔沿 -RECEIPT（-REV 缺集先例口径＝派工具名）·尾标后零粘连数字（CT-6 案型自查）。

（append-only·本判词后续修订票尾续 rev 段互不回改）

-RECEIPT
