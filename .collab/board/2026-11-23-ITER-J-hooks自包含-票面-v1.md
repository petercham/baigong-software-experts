# ITER-J 部署态 hooks 引用脚本路径修复·起草段票面 v1

## 〇、分档判据读数（必填·机械入档）

声明闭集文件数＝写集具名枚数现数一枚（见 §三 S1），对微档判据行（standard-sop 行 85＝微档 ≤1 文件且改动 ≤10 行且入线四词零命中）＝条①命中；改动行数预估：四条 command 行改 4 行＋_anchors 追加候 1 行＝改 4 至 5 行、增 0 至 1 行＝条②命中（管道 grep 逐词现跑见下）；入线四词＝词表照 standard-sop 行 64—67 现跑取词（T1 真源形态／T2 文件域结构／T3 席位职权／T4 工序链本体），对靶文件现盘面逐词现跑计数四词各 0（四道 grep -c 现跑逐词登记见 §二），对施工笔 diff 面机械复核闸见 §四 V6＝条③命中。
入档结论＝微档（三条判据全命中·现跑为据）；错判即红条款未触发申明＝本档未错判、条款未触发。

## 一、获批登记

指令原话逐字＝⟦工具钩子出了点问题（它引用的脚本路径不存在）｜部署后在多处实践中遇到以上反馈，注意是否引用脚本应该自包含才是正解⟧（皮总 2026-11-23 01:41 明示）。指向登记件＝.collab／board／2026-11-23-外部输入-HOOK缺陷-反馈登记-v1.md（唯一缺陷基线·皮总原话逐字＋主理人取证五目在册·行数现跑 15）。
裁定与计划依据＝通道判定行现读：登记件 L14「通道判定〔主理人蒸馏〕」段＝⟦缺陷修复＝按施工票载体走开票链（沿 ITER-G／H 微票工序）；起草归架构席（hooks 装配面属架构域）⟧（登记件行 15 现读）；待裁点同段具名＝双形并列与否由票面提案、双席审、主理人放行，本票以候裁 J-1 承载不在此拍（见 §五）。
写集路径清单（仓根相对径·逐枚编号具名·现数计数一枚）＝
S1＝agent-experts／baigong-software-team／hooks／hooks.json（唯一写集·见 §三）。
段界＝本笔＝起草段票面入链＋预检闸干跑（本席职权边界＝起草＋只读取证；不施工＝不改被修文件 S1、不 commit 链笔归主理人段后工序；落笔在放行后施工窗由持写权席照 §三 规格与 §四 V 系执行）。
止痛归因声明＝本票未引入任何损耗口径命名（无常数／固有／成本入排程或条文），不适用一行申报。
回执收口并笔申明＝本票起草席＝执行类票候裁自列（现数计数一枚＝J-1），六字标记＝候裁一枚在册；放行登记落位制对起草席无字段＝放行归主理人段（真源见开发纪律卷 §十二）。

## 二、当轮取证读数（现跑·禁抄旧数）

警示行（预置固定·逐字照抄）：本节全部读数＝当轮现跑，下游验收读数各自当轮现跑，本表只作起草态基线对照。

表头固定四行名（预置固定·读数入槽）：

    | 项 | 命令 | 实测读数（当轮现跑） |
    |---|---|---|
    | 时点 | date 现跑 | 2026-11-23 01:46（收尾复跑见完工回报） |
    | HEAD | git rev-parse --short HEAD | 33a4a522＝链顶现读；与派工预期比对＝派工单未钉 sha＝以现跑为锚（PF-2 以本 sha 入锚） |
    | index.lock | ls .git／index.lock | NO_INDEX_LOCK（ls 无此件实证） |
    | 脏面 | git status --porcelain | tracked 脏面 0 枚；?? 当轮计数照登 1 枚＝本缺陷基线登记件（他案活体群禁钉死·即本票 §一 指向件） |

本票特有靶面读数行族（命令→输出成对落位）：

    git rev-parse HEAD:agent-experts/baigong-software-team/hooks/hooks.json
    → fff5714522e58b0f5a2c46170ea3402d2e720a2f
    git cat-file blob fff5714522e58b0f5a2c46170ea3402d2e720a2f（管道换行符计数）
    → 56 行（靶件链面对钉＝56 行／fff5714522e58b0f5a2c46170ea3402d2e720a2f 三式配对自证）
    python share/check-pointers.py --target agent-experts/baigong-software-team/hooks/hooks.json
    → exit 0（靶自靶绿）
    grep -c 真源形态／grep -c 文件域结构／grep -c 席位职权／grep -c 工序链本体 于靶文件逐词现跑
    → 0／0／0／0（入线四词对盘现面逐词命中全零）
    grep -n 行首双点斜杠形制 于市场缓存面 my-experts／baigong-software-team／0.1.36／hooks／hooks.json
    → L17／L27／L37／L49 四命中＝部署面与仓内真源同一缺陷形制复现坐实
    ls 市场缓存 0.1.36 面 skills／sop／scripts／ 管道 grep 被引三枚名
    → write-guard.py／memory-neutralize.py／commit-audit.py 三枚在包内实存
    grep -c pack_root 缓存 0.1.36 面 write-guard.py
    → L40 定义行在＝脚本本体自包含性沿登记件取证目四成立（缺陷仅在调用径）
    grep -n PLUGIN_ROOT 于本机市场面官方插件 hooks 全域（workbuddy-builtin 各家 hooks.json）
    → 五条 command 命中全带 CODEBUDDY_PLUGIN_ROOT 前缀形制（sheetagent／wecom-a2a-auth／subscription-gate×2／workbuddy-docx）
    grep -n PLUGIN_ROOT 于 workbuddy-docx 最新缓存版 hooks.json 内带 scripts 子径行
    → L9＝bash 引插件根下 scripts／wb／local／setup.sh＝以插件根变量指 scripts 子径先例在册
    grep -rn PLUGIN_ROOT 于本仓全域
    → 命中 0＝仓内真源现态无该变量先例（本票即首入）
    git log --oneline -5 现跑
    → 33a4a522／e3586b83／34f129bb／cd06813d／7569a930 逐笔相衔自证（链顶＝ITER-I 收口笔）

## 三、声明闭集（写集＋禁动面）

S1＝agent-experts／baigong-software-team／hooks／hooks.json 落笔规格 verbatim＝四条 command 值由现盘行首双点斜杠形制逐条改为插件根自包含形制，改后四条 JSON command 字段值依次为（缩进段＝落笔目标值 verbatim·JSON 内半角斜杠照命令面承载）：
    python "${CODEBUDDY_PLUGIN_ROOT}/skills/sop/scripts/write-guard.py"
    python "${CODEBUDDY_PLUGIN_ROOT}/skills/sop/scripts/memory-neutralize.py" prehook
    python "${CODEBUDDY_PLUGIN_ROOT}/skills/sop/scripts/commit-audit.py" prehook
    python "${CODEBUDDY_PLUGIN_ROOT}/skills/sop/scripts/commit-audit.py" posthook
语义面保留口径＝_note 四行逐字零扰动；_anchors 既有五键（工件矩阵／决策词表锚点／B11／B5／P4镜像）逐字零扰动＝P4 镜像行候裁口径不动；P4 镜像行＝双形并列同交付·缺省不启用退路·择路由候裁 Q-04 先例口径（先例出处＝hooks.json 链面 blob fff5714522e58b0f5a2c46170ea3402d2e720a2f 内该键＝cat-file 管道现跑取读）。
JSON 结构骨架禁改＝只改四条 command 串；如需自包含锚说明仅可在 _anchors 对象内追加新键一条（追加属内容允许·禁删禁改既有条目＝键数五枚可增至六枚、既有五键值 byte 零扰动）。

禁动面五行族（预置固定·逐字照抄）：

- 链上史件零回改；账本零手写；FUXI 零碰；?? 他案群照登零带入；.gitignore 零触。

本票特有禁动面逐项写死＝hooks.json 除四条 command 值与 _anchors 追加候一键外 byte 零扰动；被引三枚脚本零触；bundle.lock／assembly 装配面／版本号三同源零触（随包分发触 bump 候 DEP 窗＝主理人段编排·不在本票射程）；thin 模板真源零触；开发纪律卷零触；docs 两枚零触；市场缓存面只读（取证用·禁写）。

## 四、验收判据（V 系·用例唯一产出处）

V 系骨架（预置固定·命令与期望由槽填）：

- V0 开工读数＝当轮现跑 HEAD＋链序＋锁态＋脏面照登（禁扩集口径沿先例）。
    date 现跑＋git rev-parse --short HEAD＋ls .git／index.lock＋git status --porcelain 四读数＝§二 表头四行当轮在册（禁扩集）
- V1 靶面钉值零漂移＝开工对钉值与下游验收复跑对拍；漂移即停手回报。
    git cat-file blob fff5714522e58b0f5a2c46170ea3402d2e720a2f 管道换行符计数＝开工对钉现算；验收复跑同命令对拍＝漂移即停手回报
- V2 施工动作＝施工步骤命令 verbatim＋断言＋程序化动作读数。
  槽填＝落笔前程序化动作（施工窗执行·非起草窗）：
    python -c 载入 hooks.json 现盘→四条 command 串值逐一替换为上节目标值→json 解析自证→落盘
    断言＝改后 python 解析 hooks.json exit 0；command 四值与 §三 目标值全等；_anchors 既有五键 byte 全等；JSON 键序与缩进骨架零变
- V3 落盘坐实＝面单核验（git show --numstat／--name-only 于施工笔）。
  槽填＝命令＝git show --numstat --name-only 于施工笔→期望面单枚数 1＝S1 具名归因；numstat 增删行数与改动预估带相符（删 4 起＋增 4 起＋候追加 1 行）。
- V4 自靶 exit 0＝落笔前各靶件 check-pointers --target 现跑。
  槽填＝
    python share/check-pointers.py --target agent-experts/baigong-software-team/hooks/hooks.json
    期望 exit 0（起草窗基线现跑已＝exit 0 见 §二）
- V5 面单互证＝声明闭集 vs 实测 numstat 对等（零越档）＋缺省扫描对施工前基线只平或降、非零逐枚归因禁遮掩。
    python share/check-pointers.py 缺省面改前基线现跑＝exit 0（NOTE-FXU28 类仅 NOTE 行不入计数）
    python agent-experts/baigong-software-team/skills/sop/scripts/check-ticket.py 缺省目录模式改前基线现跑＝BLOCK 40／WATCH 0＝存量他案尾标在册沿 F 先例具名归因
    改后复跑期望＝两闸读数只平或降；升即逐枚归因禁遮掩
- V6 升档停手闸＝入线四词（词表以票级放行登记勘正表为准）grep 于施工笔 diff 面→命中 0；命中任一＝停手呈主理人升全量档，禁自行继续。
  槽填＝四词＝真源形态／文件域结构／席位职权／工序链本体（词表照 standard-sop 行 64—67 现跑取词·无票级勘正表随＝沿 ITER-I 先例口径）；起草窗预核＝对靶现盘面四词各 0（§二 现跑）；施工窗＝git show 施工笔 diff 面逐词 grep 期望各 0。

## 五、候裁单列（必有节·可 0 枚）

预置固定行：批次编排类不上楼＝不自列候裁。
J-1＝议题＝开发态仓内直跑 hooks.json 与部署态插件根形制之双形问题处置。两侧论证＝甲侧（单一自包含形制·建议采纳）：宿主加载包后钩子命令 cwd＝会话工作目录（登记件取证目二坐实），仓内直跑属开发面调试而非宿主加载路径；变量形制在仓内 git 面仅为字面串、宿主注入面才展开，仓内直跑两态皆无解（现盘 .. 形制在仓根起算同样落空）＝保留双形＝保留两条各半瘫的调用径；脚本本体自包含（取证目四）已使包内任意 cwd 可解，单一形制即可覆盖宿主全部三面。乙侧（双形并列）：沿本文件 _anchors P4 镜像行既有「双形并列同交付·缺省不启用退路」先例口径。建议采纳值＝甲；若主理人裁乙＝追加动作＝_anchors 追加行具名退路＋command 双行形制，改动行数升候 8—10 行（复算口径见 §三 落笔规格四条＋候追加一行）＝仍在微档改动带内、判档不受影响。

## 六、链衔接纪律（预置固定·不重写）

- 开工现跑 HEAD＋链序照登；单 pathspec add 紧邻 commit＋FX_COMMIT_DECLARE 挂 commit 命令侧＝仓根相对路径（两端皆为声明侧卫生纪律·缩小卷入命中面·非拦截机制——c4aad87 三实验坐实提交侧拦不住他席 staged 注入）；卷入防线＝（钩子在岗时）post-commit 比对真实树当场报（HEAD 面单与声明清单对等核验·不符即醒目告警＋仓内日志一行）；commit 前先跑自靶 exit 0。
- message 用 -F 文件承载（防引号与中断·先例在册）＝message 文件落仓根 .scratch／ 取证族·用毕即拆 ls 坐实。
- 落链硬口径＝-F 承载＋commit 输出重定向落盘＋后台执行（中断教训先例在册）；commit 类命令 timeout 600000。
- 体例＝裸文＋全角斜杠·零 at 零反引号·命令缩进段；尾标闭集（-TICKET／-BUILD／-RECEIPT／-QA-REV／-QAV／-RELEASE／-GCLOSE 照段别取用·收口段一律 -GCLOSE）；族名随 message 内嵌。
尾标闭集自校（预置·复算口径）：近 30 笔 git log --format=%s 管道 grep 尾标族计数＝新式尾标命中照列；旧链 -CLOSEOUT 存量＝沿革照登不回改。
- 禁 add -A／禁 amend／禁 --no-verify；message 以 collab: 起头·零 at 零反引号·＝号串联关键读数。
- 撞锁两态口径＝lock 在飞等待自然消退、实证陈旧按先例删锁留证；他案脏面照登零带入。
- 临时工作物落仓根 .scratch／；取证族用毕即拆 ls 坐实随完工回报。

（模板尾·固定形制：append-only 票面后续修订在票尾续 rev 段，rev 段间互不回改）
