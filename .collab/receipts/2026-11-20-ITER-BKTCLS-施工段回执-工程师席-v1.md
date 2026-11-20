# ITER-BKTCLS 施工段回执 v1（工程师席 eng-bktcls·fresh 单实例·票＝.collab／architect／2026-11-20-ITER-BKTCLS-桶名闭集扩册-规则票-v1.md §三 F1／F2 施工写集·一次成文 append-only）

## 〇、开工读数（本席当轮现跑·禁抄旧数）

- 时点＝起窗 2026-11-20 23:3x（起窗未单落 date 读数，收尾复跑＝2026-11-20T23:41:59+08:00 现跑在册）。
- HEAD＝git rev-parse --short HEAD 现跑 9345a605＝放行登记笔＝派工预期链顶全等（放行登记面单所指 9345a605 在册）。
- 链序＝git log 现跑 9345a605^＝87130238／87130238^＝2f2032fd／2f2032fd^＝ec6957c0／ec6957c0^＝af31b31b 父子相衔零断。
- 锁态＝ls .git／index.lock 现跑＝NO_INDEX_LOCK。
- 脏面＝git status --porcelain 现跑＝tracked 零枚＋?? 簇照登（.DEVKITS-POINTER.bak／agent-experts／baigong-software-team／.scratch／tickets／msg-w5ticket.txt 他案残留／agent-skills 目录面）＝与两判词?? 簇同群照登不清洗零带入。
- 票面与放行件 blob 双对钉现跑＝F1 链面 rev-parse e098bd5528b257ab88f5adb88c83d2bd5768ef45＋盘 hash-object 同值全等（312 行）；F2 链面 rev-parse 1060d97b027278111d157ee23c329732252a9a19＋盘 hash-object 同值全等（41 行＝sparse 物化后盘链两式全等＝产品判词观察面正例复现）；自裁登记件 d9dbee26／config b4b8f23d／receipt 模板 bb1a08d9／ticket-template 139d0b8b 四钉全等；BKTCLS 票面 d8f48080／产品判词 d5ebbfb1／QA 判词 251396c1／放行登记盘 e27acf99 全等。
- sparse 前置现读＝core.sparseCheckoutCone true＋sparse-checkout 文件现数七行（含 /.collab/ 与 /share/ 行＝主理人单径物化已执行现读引用＝本席未再动 sparse＝§四① 前置满足态沿判词窗）。

## 一、BUILD 笔施工读数（照票 §三 verbatim·改动面逐处）

F1＝share／check-collab-buckets.py＝规格四处全落（numstat＝插 7 删 6）：

    ①frozenset 追加三枚 claims／instances／qa（行 54—58 体内裸写追加·零反引号自咬沿守）＝追加后内嵌集枚数 20（V2 现跑）
    ②README_ANCHOR 常量「17 桶名录」改「20 桶名录」（与 F2① 节题字样同步）
    ③头注与 docstring 名录锚字样族三处随改（行 7／53／105）＋「内嵌白名单 17 项闭集」计数字样随改「20 项闭集」
    ④头注规格指向段追加沿革一行＝出处三件裸写＝自裁登记件＋本票面＋QA 席 C1 判词（qa 清算出处）

F2＝.collab／README.md＝规格三处全落（numstat＝插 5 删 2）：

    ①名录节节题「17 桶名录」改「20 桶名录」
    ②名录行反引号段追加三枚「claims/ instances/ qa/」（带尾缀斜杠沿现制＝解析器尾缀归一口径零动）
    ③桶总表追加三行＝claims＝机核认领清单 jsonl（件名与行型形态＝ITER-B 协议票面 v2 R4.1 verbatim 条款号指向·只指不搬）／法定写席＝收单席位；instances＝实例码名册 roster.md（行格式＝R1.3 verbatim 指向）／法定写席＝主理人投递；qa＝QA 席非交接件写权域（存量桶实盘清算入册·现盘判词件即在位该桶）／法定写席＝QA 席

落笔坐实＝本席零 git 写（红线）＝两枚改动以盘写落位呈投递态；git status --porcelain -uno 收尾现跑＝tracked M 恰两枚＝F1／F2 具名对等零越档；numstat 逐枚＝F1 7／6、F2 5／2＝扰动面全落 §三 具名处（逐 hunk diff 全文见 §三 归因）。

## 二、V 系全套读数（本席当轮现跑·改后终态）

- V0 开工读数＝§〇 成对讲成立（HEAD 9345a605＝票面 §二 预期 8244197b 之放行后合法后继值）。
- V1 靶面钉值零漂移＝对钉集改后复跑逐枚：自裁登记 d9dbee26／config b4b8f23d／receipt 模板 bb1a08d9／ticket-template 139d0b8b／BKTCLS 票面 d8f48080／两席判词 d5ebbfb1＋251396c1／放行登记 e27acf99／.gitignore 3a8f39c1＝全等零漂移；F1 e098bd55→c7c5d354、F2 1060d97b→655e133a＝唯二扰动＝逐处归因＝V2 断言申报面（§一 具名处），其余零触。
- V2 两源计数臂＝票 §四 命令段 verbatim 现跑＝输出「20 20 True」＝内嵌集 20＝README 解析集 20＝集合全等（新锚定位内含自证）exit 0。
- V2 实盘跑臂＝python share／check-collab-buckets.py --root . --seg bucket 现跑＝末行「check-collab-buckets：一级目录判 14 枚｜违例 0｜名录对拍 一致」exit 0＝qa 存量隐性违例清算归零坐实＝本票主旨自证（改前本窗基线现跑＝「判 14 枚｜违例 1｜对拍 一致」exit 1＝违例恰 qa 一枚＝与两判词改前基线全等；态差归因＝扩册入集非闸逻辑改动）。
- V2 回归臂＝票 §四 命令段 verbatim 现跑＝输出「17 True ['claims', 'instances', 'qa']」＝旧十七枚全存续零扰动＋差集恰三枚无越册扩桶。
- V2 关键句臂＝grep -c「20 桶名录」现跑＝share／check-collab-buckets.py 4／.collab／README.md 1＝各 ≥1；grep -c '"qa"' 现跑＝1 ≥1＝锚字样两源同步在场＋新枚入集。
- V3＝归投递窗（本席零 git 写）＝申明口径＝投递笔面单应恰三枚＝F1＋F2＋本回执（施工＋回执并笔先例沿承·派工具名三枚同笔）。
- V4 自靶落笔前现跑＝check-pointers --target 票面 exit 0／--target 起草段回执 exit 0／check-ticket --target 票面 BLOCK 0／WATCH 0 exit 0＝三面全过（回执侧只跑 check-pointers＝闸种指名口径·check-ticket 七节闸施回执面不适用禁双闸）。
- V5 面单互证只平臂＝check-ticket 缺省扫描改前现跑 BLOCK 21／WATCH 0 exit 1＝改后复跑 BLOCK 21／WATCH 0 exit 1＝只平（两判词窗基线 18→本窗 21＝sparse 扩面存量差量两席备案在册＝放行登记 §三 写死「只平跑臂以施工窗当轮现值为准」口径执行）；--seg pair 改前改后皆「收口件在判 14 枚｜判词件命中 13 枚｜配对违例 1」只平；--seg bucket 改前 exit 1（物化后基线）→改后 exit 0＝态差归因＝扩册＋F2 落盘非闸逻辑改动（票 V5 归因句在册）。
- V6 升档停手闸＝入线四词（真源形态改动／文件域结构改动／席位职权改动／工序链本体改动）于 git diff 面 grep -n 现跑＝四词零命中（grep exit 1＝零命中形制）＝名单空＝标准档成立无升档触发。

## 三、禁动面逐项零触坐实（现跑）

- 两票面本体／两席判词／decisions 各件／链上史件＝pin 复跑全等（§二 V1 读数）＝零回改。
- 历史引语行族＝grep「17 桶闭集」复跑＝行 9／35 两处皮总裁甲句在位未触（35＝原 34 随头注插一行顺延＝行位推移非内容改动）＝diff 全文零 hunk 含该两行坐实。
- F1 其余 byte＝MC-PAIR-1 段全体／扫描射程逻辑／退出码闭集零扰动＝diff 全文仅 §一 具名处七 hunk 行段；行为面自证＝pair 段改前改后读数逐值只平。
- F2 其余段落＝diff 仅桶总表尾插三行＋名录节节题＋名录行两 hunk；行 38（原 35）历史案卷 qa 字样口径行 grep 复跑在位零触；仓根性质注零触；桶总表既有十七行零改。
- 「17」字样收尾复跑＝脚本内残存三处＝行 9／35 史锚（应零改＝在位）＋行 11 沿革行「17→20」自引用（＝F1④ 规格本体）＝无漏改计数面；README「17」字样零残留（grep 面随两源计数臂集合断言内含）。
- tests／／skills／ 真源／config／／.gitignore／本仓 .git 写对象面＝pin 与 status 复跑零触；本席全程 git 只读＝rev-parse／log／status／ls-files／hash-object／diff／config 读＋零 add／commit／amend／stash／sparse-checkout 写。

## 四、取证族拆除坐实

本窗取证族零建＝全部读数现跑直出终端未落盘；唯一载体＝.scratch／bticket／msg-bktcls-build.md（ignore 域自写·check-ignore 现跑判定＝.gitignore 59／60 行命中在册）＝供投递窗 -F 承载用毕即拆＝拆权归主理人（本席留证不拆）。

## 五、案型登记（如有）

无新案型。存量差量两枚照登归因：check-ticket 缺省 18→21＝两判词窗 sparse 扩面备案沿承（施工窗现值为准口径）；bucket 闸起草窗 exit 4→本窗改前 exit 1→改后 exit 0＝物化＋扩册两态差归因在册（票 V5 归因句＋放行登记 §三 在册）。

## 六、本笔纪律自证（RECEIPT 笔）

本席一票一新鲜实例·fresh 单实例在场申明＝无本席他并发实例；写件恰三枚＝F1＋F2＋本回执＝票 §三 授权两枚＋派工具名回执同笔授权一枚＝零越档；落笔前自靶三面 exit 0 读数在 §二 V4；本回执落笔后自靶现跑＝check-pointers --target 本回执 exit 0（读数随回报）；尾标载体＝.scratch／bticket／msg-bktcls-build.md＝单行＋尾换行＋-BUILD；本席零 git 写＝投递归主理人；index 净＝收尾复跑无 staged；跨席交互零直连＝全部经主理人。
