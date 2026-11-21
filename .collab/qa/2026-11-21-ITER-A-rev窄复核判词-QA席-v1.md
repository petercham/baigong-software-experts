# ITER-A 规则票 rev 窄复核判词（QA 席 qa-arev3·fresh 单实例·rev 窄复核口径＝只复核 rev-1 五处修订闭合性＋append-only 完整性＋终态闸读数·不重审全票面七条·GTWWRITE rev 窄复核先例口径）

出品＝BG／qa-arev3／2026-11-21
出品锚＝baigong-software-experts｜main｜0f92adfbfaae66e6ff0c793d1868f51ef426be1b｜2026-11-21T08:31:56+08:00（四值＝git remote get-url origin 末段仓名现跑／git branch --show-current／git rev-parse HEAD／date -Iseconds 本窗现跑值登记·落笔收尾复跑见末行）

总判行＝红 0／黄 0／绿 7＝rev-1 五处修订逐处闭合＋append-only 前段零回改＋终态自靶全绿＝可放行（放行裁定权归签字席＝主理人程序确认·本席出闭合性结论非放行本身）。
体例三零申明＝本件反引号 0／at 0／非缩进段半斜杠 0（叙述面路径裸文＋全角斜杠·命令一律四空格缩进段）。
fresh eyes 申明＝两席审票判词件本体零读（红线＝不改票面与回执·零承接其内嵌读数）＝本判词全部读数＝本席当轮现跑自造＝独立互证非串供。
同席多实例申明＝本席＝qa-arev3 fresh 单实例，发现本席位无第二并发实例在册。
窄复核射程申明＝本席只对 rev-1 五处修订（红1／红2／红3／黄1／黄2）闭合性＋票面 append-only 完整性＋终态闸读数出判；票面七条本体（忠实性／落位形态／verbatim 形制／取号／候裁／V 系可机械性）不在本窗射程＝沿 GTWWRITE rev 窄复核先例口径。

## 〇、开工对钉（当轮现跑）

    git rev-parse HEAD                     → 0f92adfbfaae66e6ff0c793d1868f51ef426be1b
    git status --porcelain                 → staged 零枚＋tracked M 零枚＋?? 簇照登（.DEVKITS-POINTER.bak／agent-skills 目录面／msg-w5ticket.txt 他案残留）
    ls .git／index.lock                    → NO_INDEX_LOCK

对钉口径＝派工钉 HEAD＝0f92adfb 或其可验证后代＋clean＋NO_INDEX_LOCK＋两枚 sha／行数现跑——四项现跑全等兑现（tracked 面 clean＝?? 簇他案脏面照登零带入沿票面 §二 同簇口径·非 tracked 脏枚＝clean 判据成立）。
两枚被验件盘态现算＝票面 194 行／16cf429f983b1c3cb5afba3ffb83043cc3d800ae 全等；回执 58 行／bbe9231757e301dc88b8ebd8c8622336d003e2bb 全等＝派工钉值两枚全等坐实。
修订历史参照现跑＝链笔 9823106e（QA 席审票判词笔·尾标 -REV 闭集内）可解析在册；链笔 81b3ec34（产品席审票判词笔·尾标 -PROD-REV 闭集外）可解析在册＝两枚判词件盘在＝.collab／qa／与 .collab／product／下 ITER-A 审票判词各一枚 ls 现跑在册；rev-1 段＝票面行 186—194 现读在场。

## 一、rev-1 五处修订闭合性逐判（现跑·逐枚）

- 绿一·append-only 完整性＝票面 head -n 185 管道 git hash-object --stdin --path 归一口径现算＝7e4a86ab203982ff2e15c039777b0c521ed702ec＝与派工钉值全等＝v1 段（行 1—185）零回改坐实；rev-1 段＝票面行 186—194 九行续段（行 186 段题＋行 187 空＋行 188—194 六条修订项）＝票尾续段形制合规（模板尾行 185 固定形制句申明「rev 段间互不回改」在位）；回执侧 append-only 佐证＝回执 head -n 57 管道同口径现算＝16c09dce26f1f0ed06864d4fdb10e932ff3745e2＝起草态回执钉值全等＝rev 归因行 append 于行 58＝前段零回改 → 闭合。
- 绿二·红1 闭合＝rev 段（票面行 189）勘正指向＝「该件行 24」在位；三态现跑引文对象件＝ITER-B 全链收口登记件（.collab／decisions／2026-11-21-ITER-B全链-收口登记-v1.md＝32 行／02a341dec18cb351509453a14673c9a1e66ebcee 现算全等）行 24＝ ⟦观察账不变＝V-10／.DEVKITS-POINTER.bak⟧ 引文对象句（现盘态／链态 5d49a883／链态 0c9672b3 三态 sed 取行现跑全等）；行 23＝ ⟦2. 分析件 2f2032fd v2 随修⟧ 另一句＝原错锚「行 23」坐实且已勘正为行 24＝三态一致 → 闭合。
- 绿三·红2 闭合＝bundle.lock（89 行／b27c18da12b066c706b1c84494542cae5612aeb2 盘 hash-object 现算全等）行 45／55＝ref 实钉 tag 两枚（multi-collab 组件 ｖ4.11／object-audit 组件 ｖ0.9·tag 名全式见 bundle.lock 行 45／55 现行现读＝sed 取行现跑坐实）＝补钉笔 f883c4da 可解析在册（git cat-file -t → commit＋git show --name-only 面单含该锁件＋merge-base --is-ancestor f883c4da HEAD → exit 0 后代坐实）；PENDING-E1 字样现册恰 2 枚全落行 49／59 note 史面旧标记串（grep -o PENDING-E1 → 2＋grep -n 具名两行现跑＝行 49／59）；rev 段 A3（票面行 190）按行 49／59 具名重写在场＝含 ⟦行 49／59⟧ note 史面终态口径＋⟦行 45／55⟧ ref 槽已实钉 tag 补钉兑现口径两处具名；bundle.lock 本体零触＝git status --porcelain -- bundle.lock 现跑空＝零改；bundle.lock 盘 blob 对 HEAD blob 现跑＝b27c18da 两式全等 → 闭合。
- 绿四·红3 闭合＝rev 段（票面行 191）对 F5 具名化在位＝V2 纯增臂对 F5 期望写死 ⟦numstat 删除列恰 2／新增列恰 2 具名归因两处（行 3＋行 24）⟧＋该臂「其余面删除列 0」射程勘正只指 F3＋F4 删除列恰 1 口径不变＋V3 申报扰动面名单增具名 F5 照 F4 先例；归因两处＝F5 SKILL.md（31 行／60360b387e7774fdc755c10e56be14dcd70ac82a 现算全等）行 3 描述句触发词段＋行 24 dev-discipline 索引行描述段＝现盘两行皆为既有行（sed 取行现跑＝行 3 description 触发词列／行 24 引用 dev-discipline 索引行＝既有态坐实＝现盘无纯增位可承载关键句）；关键句 ⟦产物生命周期与登记闭合⟧ 现盘 grep -c → 0 exit 1＝现盘零现（未施工态符合）；自造夹具复现互斥已消＝本席夹具按 rev 修订后预期构造 F5 两处置换（行 3＋行 24）后 git diff --numstat 现跑＝删除列 2／新增列 2＝与 rev 修订期望恰 2／2 一致≠原 V2 期望删除列 0＝原两臂互斥坐实且已消歧（构造实证＝删除侧 2 枚 grep -c ＋关键句命中 2 grep -c 现跑） → 闭合。
- 绿五·黄1 闭合＝rev 段（票面行 192）口径句在场＝⟦§八.2「禁仓外任何自建点」之「自建」＝未经人类明示批准之落点；§十一目 3 仓外落点例外通道＝该禁令的明示批准路径（批准原话逐字录于派工书或票面后方可用）⟧＝两节并存非冲突口径申明在位；条款 verbatim 本体不动申明在位；锚点现跑＝dev-discipline（agent-experts／baigong-software-team／skills／software-orchestration／references／dev-discipline.md）行 83 §八.2 ⟦禁仓外任何自建点⟧ 现读在位（grep -n 现跑）＝口径句所指两节皆实体在册 → 闭合。
- 绿六·黄2 闭合＝回执 rev 归因行 append 在场（回执行 58＝arch-a-rev1 窗·黄2 闭合归因行＝⟦回执面入线四词现跑读数更正＝四词各 1（全落行 32 自引用现跑登记行）⟧＋申明投递笔 V6 名单须含该回执面命中全枚）；回执面入线四词现跑各 1（真源形态改动＝1／文件域结构改动＝1／席位职权改动＝1／工序链本体改动＝1·grep -c 现跑）＝四枚命中全落回执行 32 自引用现跑登记行（grep -n 现跑＝各词命中行号均 32）＝词表具名自引用面＝名单外零命中＝标准档结论不受摇 → 闭合。

## 二、终态闸读数（自靶＋缺省·现跑）

- 自靶三面现跑＝check-pointers --target 票面（194 行终态）exit 0／check-ticket --target 票面 exit 0／check-pointers --target 回执 exit 0＝三面全绿（真 exit 码现取）。
- 缺省三闸只平臂现跑＝check-ticket 缺省扫描 BLOCK 27／WATCH 0 exit 1（起草锚 §二.9＝BLOCK 25＋差量 2 枚逐枚归因＝起草后落链之链笔闭集外尾标两枚＝9823106e -REV 与 0f92adfb -REV 系＝全落链上存量笔非本票或 rev 引入·V5 差量机制按设计工作＝只平成立）；check-collab-buckets --seg bucket 判 16 枚｜违例 0｜exit 0＝只平；check-pointers 缺省 exit 1（命中全落 agent-skills 只读邻域存量族＝OA-D6 族 2797＋NOTE-FXU28 族 817 现数＝ITER-A 相关命中 0 grep -c 现跑＝非本票射程）＝只平成立。

## 三、案型随登（非违例不入色）

- 黄2 口径措辞与现跑轻差＝rev 段（票面行 193）称黄2 命中面含「本次归因行本体」，但归因行本体按体例避四词字面（回执行 58 用「入线四词」统称而非四词字面）＝归因行本体实际不自增命中＝现跑四词各 1 仅落回执行 32＝V6 投递名单实际只需含行 32 一枚自引用面；措辞宽于现跑＝不构成闭合缺口（归因行在场＋四词全落自引用行＝黄2 核心闭合成立）＝照登不入色。
- 窄复核未覆盖面＝票面七条本体（忠实性／落位／verbatim／取号／候裁／V 系可机械性）本窗零复审＝沿前轮两席审票结论在册（红3 黄2 已触发 rev-1 修订）＝本窗只判修订闭合，不背书全票面＝放行前如需全票面复签另窗出。

## 四、纪律自证与载体

- 本席写集恰一枚链内写件＝.collab／qa／2026-11-21-ITER-A-rev窄复核判词-QA席-v1.md＝本件；载体＝.scratch／aticket／msg-arev3.md（单行＋尾换行＋尾标 -QA-REV·只写不 commit·ignore 域）。
- 本席零 git 写＝全程只读 git 命令（rev-parse／log／show／status／grep／hash-object／merge-base／cat-file／ls-tree／sed）；零 add／commit／amend／stash／checkout；红线「不改票面与回执」坐实＝收尾 git status 现跑 .collab／ 域新增恰一枚核数随回报登记。
- 夹具族＝.scratch／qa-arev3／（F5 置换模拟基线一枚＋改后一枚）用毕即拆＝拆净 ls 坐实随完工回报登记；.scratch／aticket／ 既有取证件只读零拆。
- 落笔前自靶＝check-pointers --target 本判词现跑读数随回报；本判词不跑 check-ticket＝闸种指名（判词非票面七节体例＝跑即假红禁沿先例）。
- 禁动面自证＝票面／回执／F1—F5／config／三同源／闸脚本／链上史件本窗零触＝收尾 git status 现跑核数随回报登记。

收尾复跑＝date -Iseconds 现跑登记值随回报；HEAD 复跑＝0f92adfb 零插笔＝与开工锚全等；本窗 git status 现跑＝.collab／ 域新增恰一枚（qa 桶本判词一枚＝核数坐实写集恰一枚）；夹具族 .scratch／qa-arev3／ 拆净读数随完工回报登记；本判词终态行数与自算哈希＝自引用禁则不入本件正文＝随完工回报消息具名。

（append-only·后续随正续 rev 段互不回改）
