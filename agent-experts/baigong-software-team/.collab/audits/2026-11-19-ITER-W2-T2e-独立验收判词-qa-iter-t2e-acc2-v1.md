# ITER-W2-T2e · tests 接线与工具归属定版票 · fresh QA 独立验收判词（v1）

判词席位＝qa-iter-t2e-acc2（fresh eyes 全新实例·与开票／快审／放行／施工／回执五席零上下文共享·只审不裁·全部读数当轮现跑·链上件读数只作互证参照零承接·零 git 写＝投递归主理人·裁决 c34f204e 口径）。件名照派工单指定全名落位（件名形制案型随登见 §五-丙）。判词归签字席＝本件为验收判词面；收口归产品席窗（收口件必引本判词件名全名）。

## 〇、开工读数（当轮现跑·禁抄旧数）

- 开工首跑 HEAD＝bb762391ce66ca70fe88884ddaac53e15159de01 四十位＝派工预期链顶全等＝T2e RECEIPT 笔链顶现势＝正常开工（无竞态分支触发）。
- ^现读链序＝bb762391←b0870455←9e76d08f←cd837ced←0663312f←036bad68←3bdabc89←c9bf765b←1c772c0f 九笔逐枚^相衔零断现跑（9e76d08f＝他案 T2c 收口笔＋cd837ced＝他案 T2c 验收笔＝插笔归因照登零触碰＝对钉基准锚不受影响）。
- worktree 独立 gitdir＝主仓／.git／worktrees／baigong-software-team 现读坐实；NO_LOCK_FILES＝gitdir 文件族现跑 lock 文件零枚（bundle.lock＝bundle 族受控 tracked 件非 lock 族＝归因照登）；staged 零枚＋tracked M 零枚＋?? 零枚；sparse D 态 1018 枚照登勿处理。

## 一、依据链六枚双对钉（链上 rev-parse＋show 管道 wc＋盘 hash-object 成对·面值必现跑）

- 票面＝c9bf765b 面 1c52febbbecf5fcff851ffca1fbab17e6cce5485／179 行＝三面对钉全等（绿）。
- 快审＝036bad68 面 773e05741e5ee924eaba4b3d03eb9e1b652efd8a／80 行＝全等（绿）。
- 放行登记＝0663312f 面真位包内 decisions 桶 dcbb9d4a0e16193007d1d2aaa7138bc913d3d0a9／45 行＝全等（绿·派工面值 45 与现跑 45 吻合；BUILD／RECEIPT 面转引 46 之差已在回执 §七-5 登记一行级转引漂移案型·本席现跑 45 坐实该登记属实）。
- BUILD 笔＝b0870455 面单恰四枚＝run-all.sh 43／0＋SKILL.md 2／0＋EXT 知会单 58／0＋external-ticket-spec.md 5／0＝与派工面值全等（绿）。
- RECEIPT 笔＝bb762391 面 faaafd0cdb88f3d0ab07c5440b83a75461188fb9／94 行＝全等（绿）。
- 体例真源＝receipt-template bb1a08d99c9eb05f6d2fda214c1301bbe979ac99／27 行链面现跑全等＋先例取形＝T2h 验收判词 3f973b0f／76＋T2c 验收判词 763c8c78／79 链上 show 全等（绿）。

## 二、判据 1-9 逐项现跑三态表

1. 写集四枚链盘双对钉＝绿：tests／run-all.sh 1d5f9aeb953c4de12835ae42422be0fcafcd8e03／43＋skills／sop／SKILL.md d76785e223311a823d6a29b981530e689cb8f846／40＋EXT 知会单 c5c1f79aa9882d096fea410ab52ab9cb82130638／58＋skills／sop／references／external-ticket-spec.md e8986941307b2b8abd9d0e82a25a1f4507191733／109＝链面 rev-parse＝盘 hash-object＝wc 三面逐枚全等；开工前置面现跑＝S2 开工 9e76d08f 面 fe3977d3／38＋S4 开工 208fbf0b／104＋S1 与 S3 parent 面 absent 坐实（ls-tree 零行＋rev-parse exit 128）。
2. BUILD 笔面单恰四枚零夹带＋删侧全零＋S4 纯 append＝绿：name-status 恰 A＋M＋M＋A 四枚＝numstat 43／0＋2／0＋58／0＋5／0 删侧四枚皆零；面单前缀四枚全落本包声明闭集；S4 对 parent 面 diff 删侧^-行现跑恰 0＝append 坐实（S2 删侧同跑亦 0）。
3. 回执 §七案型六枚登记在位＝绿：七节节题七枚齐＋§七逐枚现读＝①面值链序误抄②E5 前置现势面值必现跑③shell argv 展形制 run_step 改形④WATCH 取证窗双向归因⑤转引漂移一行级⑥check-ticket 工单体两态 BLOCK 恰 14 三度复现＝六枚全在位含案型①⑤两枚点名项。
4. EXT 知会单形制＝绿：八字段节题 grep 现数恰 8（字段一至八）＋效力域声明五行现数恰 5＋诉求体三枚 R-1 随动知会／R-2 动作诉求／R-3 仅备案逐项标型现数恰 3＋四闸八值两仓成对在位（抽查 check-pointers 33781b31…‖d5e2cfe2… 与 run-gates 11a6f4d4…‖c2918140… 两对命中；buckets／hook-health 两对亦在位）；四十位面现跑＝出现 35 枚·去重 26 枚·cat-file 可解析 26／26 零悬空＋裸八位 0 枚。
5. run-all.sh 头注与 probes 零扰动＝绿：「纯标准库零第三方依赖」声明 grep 恰 1＋黄-6 乙案跳跑申明在位（头注行 6-9 原因段＋执行序行 36-38 输出面申明行现读）＋probes 真位 tests／probes／results／probe-results.json 盘 hash-object＝acf3bbc752539a0c30eba8ae499e90516605c0e4 对钉全等＋mtime 现跑 1794981576 全等＋链面 rev-parse 同值＋tests 域 scoped status 零枚＝跳跑生效坐实（派工件「tests／probe-results.json」省形写法真位现算补钉见 §五-甲）。
6. 禁动面＝绿：tests ls-files 现数 29＝28 既有＋run-all.sh＝既有 28 枚 scoped diff 零枚；share 全域 scoped status＋diff 零枚；thin 1703b610／80 链盘 SAME；check-ticket.py 5a9aa5fd 链盘 SAME；五模板 bb1a08d9／27·139d0b8b／118·7c14c074／57·c2350972／39·c7f0950e／48 链盘全 SAME；版本三同源 473317da／a87e66e4／2635ad65 链盘 SAME＋0.1.31 三处现读零 bump；加测批量＝席卡五枚＋config 七 json＋.githooks 两枚＋哈希锁 9a648030／176 与 dbf49d0b／56＋README fc449fa9＋semantic-governance.py 7cd56d09 全 SAME（diff HEAD scoped 零行）。
7. V5 缺省扫描复跑＝绿：check-pointers.py --root . exit 1＝BLOCK 行恰 1863 对在册锚全等＋WATCH 行现跑恰 1007≤1009＝取证窗归因沿册成立（.scratch／t2cacc／chain-root-audits 副本 70 枚在盘 ls 坐实＝两条历史 WATCH 消隐＝只平或降判据成立·禁判漂移条款兑现）。
8. check-ticket EXT 面两态＝绿：缺省态 exit 1＝BLOCK 恰 14／WATCH 0＋--since 2026-11-19 态 exit 1＝BLOCK 恰 14／WATCH 0（summary 行现读）＝票面骨架判据对工单体不适配＝分治案型三度复现沿册＝非违例。
9. 机检对产出面＝绿：check-pointers --root . --target 四面（run-all.sh／SKILL.md／EXT／spec）各 exit 0 输出零行现跑全等；本判词自靶见 §六落笔后现跑。

## 三、drill-05 存量红归因抽查（主理人裁口径沿册·不计红判项）

- run-all.sh 实效现跑＝worktree 根窗 exit 1＝末行 RUN_ALL_RED red_chain＝acceptance／drill-runner.sh green=5／6＝红项具名 drills／drill-05-freeze-recover.sh（py 五枚＋drill-01 至 04 段全 GREEN 逐段具名在册）＝复现派工口径。
- 先证链上现跑＝QA 审票笔 93434e052d491768f3380cd671917ea25f45be48 subject 内嵌「drill05-06开工基线即红未钉（编码不匹配＋夹具缺目标件，b8bdadc既有）」命中＋该笔 merge-base --is-ancestor YES。
- write-guard.py 现读＝行 117／142 ensure_ascii=False＋行 240 ensure_ascii=True 钉位全等；-S 'ensure_ascii=True' 归因笔＝TK-GWP 笔 5b8936e7163024b7965d8816a35f3b6d6be5f018（subject 现读对号＝守卫装配缺陷整改批）＋链上 ancestor YES＝drill-05 行 55 明文 grep 判据「B10 freeze 态全写 deny」自该笔起必失配坐实。
- drill-05 注入式独立复跑 exit 1＝RED 行「deny 原因非 freeze 联动」复现；drill-06 合规注入窗（T06_TMP＝系统 Temp 全域一致径）独立复跑 exit 0＝DRILL06_GREEN＝红项仅此一枚坐实。
- 回执 §二随正条款登记在位现读＝drill-05 候裁面段五行族（含「两路皆不可修＝如实申报随候裁面」）在位＋验收呈请引用句在位。
- 归因链吻合主理人裁口径＝本项不计红判（绿）；本席取证窗首轮误用仓外 Linux Temp 致 drill-06 一次红＝runner 头注「禁 /tmp」约束＝改合规注入即绿＝取证窗侧形制随登 §五-乙非票面违例。

## 四、纪律自证与禁动面申明

- 本席全窗 git 仅只读 rev-parse／show／log／status／diff／hash-object／ls-files／ls-tree／cat-file／grep／merge-base／wc 读＝零 add 零 commit 零 amend 零 stash 零 config 写·index 零触碰。
- 主仓路径只读以外零触碰；share 全域零改动（只读跑闸）；链上史件零回改；sparse 零处理；他案面零带入；账本零手写；席位卡／config／.githooks／三同源／哈希锁／thin／五模板／tests 既有面／check-ticket.py 本体／README 零触（§二-6 批量 SAME 坐实）。
- 唯一写＝本判词一枚＋.scratch／t2eacc2／取证族（runall-now＋drill05-inj＋drill06-inj 两态＋v5-scan＋ct-ext 两态＋sp-one＋diffplus-synth＋ext40＋msg-acc 载体）落 ignore 域不入 status（收尾复跑坐实）。

## 五、案型登记（本席现跑面）

- 甲·转引路径省形一行级＝派工件「tests／probe-results.json」系省形写法，真位＝tests／probes／results／probe-results.json（链面 ls-tree 现算＋盘 find 现跑唯一命中）＝钉值 acf3bbc7／mtime 1794981576 两值对真位现跑全等＝省形引用必现算补钉案型同族随登（回执本体写法已为真位＝违例零发生＝预防性登记）。
- 乙·演练注入窗 Temp 域约束＝drill 族头注「T06_TMP 禁 /tmp·Git Bash 与 Windows python 同域」＝本席首轮注入 Linux Temp 形制 drill-06 一次红（FileNotFoundError＋unicodeescape 案）＝改系统 Temp 合规注入即 GREEN＝取证纪律形制随登＝对后续验收席可得＝非票面违例。
- 丙·指定件名与两制件名闭集形制差＝派工指定件名（含席位名中缀）vs judgment-form-spec 两制件名闭集与桶内先例五枚形制（日期-票族-QA独立验收判词-vN）＝照派执行成立·MC-PAIR-1 配对归收口席引名面＝收口席引本件须引本件实际全名＝一行级形制差随登候补池候选。

## 六、红黄绿与可验收性签（落笔后自靶现跑随附）

- 红＝0 枚＝判据 1-9 逐项现跑全绿＋drill-05 归因链吻合裁口径＋六枚依据对钉全等＋禁动面批量零漂移＋对抗复核（回执 §二转引组抽跑＝V5 1863 对锚全等／check-ticket 两态 14／probes 两值／四十位 26／26 零悬空）零转引失真。
- 黄＝0 枚＝本案无随正新增项；§五三枚皆登记面随登不入黄（沿册口径＝登记面与取证窗侧非产出件违例）。
- 绿＝§一依据链＋§二九判据＋§三归因抽查全数达标。
- 可验收性签＝过（可收口·否定性无）。
- 落笔后自靶＝check-pointers --root . --target 本判词实路径 exit 0 输出零行现跑读数入载体；体例三零自查＝本件反引号 0／at 0／非缩进段半斜杠恰三行＝§三与§五-乙引 runner 头注「禁 /tmp」两处＋本申明行自指＝皆 /tmp 根 OS 保留路径本体＝沿先例同形。

（v1 尾·append-only·本件一次成文无 rev 段）
