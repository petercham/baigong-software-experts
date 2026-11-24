# SWB-LC-T4 · LEAD-CONSTRAINT 存量债消化卫生票 · 审票判词 · QA 席 v1

- 审席＝QA 席（fresh eyes＝三票单席一次审＝机检确定性臂；全部取证本席当轮现跑，起草席申报读数逐条独立复跑互证＝零誊面）
- 审对象＝.collab／board／2026-11-24-LEAD-CONSTRAINT-T4-施工票-v1.md（本席现跑两式＝212 行／git hash-object 现算 5555c8b5dfa444029009602c3c460269edc8f1dc＝链上 HEAD blob 现读全等＝链上笔 f050a46b 本体＝与派工预期 212 行全等）
- 审窗读数（本席现跑）＝链顶 f050a46b（＝三票入链笔＝起草窗预期 6b2cc481 后顺一投递笔＝窗移非异象）＋date 2026-11-24 17:1x＋NO_INDEX_LOCK＋tracked 脏面 0 枚＋本判词落位前 ?? 群照登
- 只读自证＝零 git 写；探针族全部落仓根 .scratch／QA-REV-LEAD-CONSTRAINT／＝用毕即拆随完工回报；探针入账全部重定向该域＝真账终核＝外层账本＋内层账本＋leases 三件 wc -l 现跑对票面开工基线全等零染自证（枚数入完工回报）

## 判据一 · 票型面三闸独立复跑归零 —— 绿

三闸对票面 --target 本席现跑（起草席申报 BLOCK 0 三组＝本席独立复跑互证）：

    check-ticket --target 票面 → BLOCK 0／WATCH 0 exit 0
    preflight-ticket --target 票面 → BLOCK 0／WATCH 0 exit 0
    check-pointers --target 票面 → exit 0（零行）

三闸三票九跑全归零＝申报互证成立＝绿。

## 判据二 · §二 取证读数与债清单复算 —— 红（两枚 B1 根因归因失实＋两行旧数违「现跑」申明）＋绿（D1 对位）

D1 三枚对位复算＝绿：最新批次证据件（run 值 2026-11-24T15:28:42 与 16:08:10 两批）check-entity findings 三枚逐枚对位全等＝workbuddy-runtime.md:144 project-name／dev-discipline.md:160 date／tests／b16e／test_adversarial_guards.py:88 drive-path；60-gates.md json 围栏现读 per_spec OA-T1 commit=block 直证路由表配 block 属实；本席现跑 python share／check-entity.py --root . 注入 GATE_PROJECT_NAMES＝run-gates 行 135 缺省值（multi-agent＋-collab-devkits 拆串拼接现读）复现时三枚全命中（另＝裸跑不注入时 project-name 子判据记 coverage 未执行＝见黄-3）。

R-7 四组读数活体增量复算＝绿：本席现跑 ls 计数 2760／bypass 真值 2629／run 键去重降闸批次 334／四枚存量债闸命中批次 334／334＝对票面 2754／2623／333 三窗递增活体增量照登成立（票面三窗在册口径复现）。

红-1＝两枚 B1 根因归因与现跑失实→承接修案不达声明判据（连带判据四不可达）：

    B1-a＝票面「真源锚件失联行族（缺位锚件例＝.collab／decisions／2026-10-25-皮总拍板.md＝ls 现跑不存在）」＝证伪：该文件 ls 现跑在场（12838 字节）＋链上 b29bc20d 换锚笔在场且为链上锚新位＝票面「不存在」不可复现。现跑真因＝check-provenance 行 348 infra 分支「扫描域为空（〈分类目录〉／＊／scripts／＊ 不存在）」＝本仓根三分类目录 glob 现跑＝agent-experts／＊／scripts／＊ 0 命中／agent-skills／＊／scripts／＊ 仅 README.md（py／sh 过滤后 0）／softwares 缺位＝hits 空集→exit 4；旁证＝同脚本自 devkits 外层仓根跑 exit 0（该根 glob 命中 object-build／scripts／publish.py）。S5 落笔规格＝「缺位锚件逐枚改锚」＝不触及扫描域空支＝声明判据「exit 码 expect 非4」在 S5 修案下不可达。全仓 spec_file 缺位真例现跑＝恰一枚＝check-pointers.py 头块指 agent-skills／object-build／references／50-directory.md（盘现缺位＝ls 坐实）＝票面未点名该真例＝修案对象错位坐实。
    B1-b＝现跑 exit 2 复现（＝「usage error: 包目录不存在：../multi-agent-collab-experts/workbuddy/baigong-video-team」）＝但根因＝调用锚径：该缺位径系仓根相对展开（自 devkits 根展开＝../＝D 根侧不存在；自外层根跑默认 pkg 缺省展开 exit 0 直证 sister 仓在盘场景）＝「他仓包目录缺位案型」表述下「注记行追加（S2）」不作用于 usage-error 前置支（该支先于任何扫描与白名单消费）＝声明判据「exit 码 expect 非2」在 J-2 采甲（S2 承接）下不可达。
    连带＝声明判据四「run-gates --no-write expect exit 0」＝现跑 exit 4（BLOCK 臂＝provenance exit4＋sot exit2＋OA-T1 三枚）＝判据一/二不达则判据四必不达＝收口口径「缺省态跑通零降闸」整链受阻。

红-2＝§二 两行读数＝旧批次数（违「现跑·禁抄旧数」申明）＋C2 归因失效：

    「check-hook-health exit 1 BLOCK 命中一枚＝FX-HOOK-1（现值 6bc60801 期望 8b785770）」＝现跑 check-hook-health exit 0 零 BLOCK＝行 47 现钉＝6bc608017756c6c505ddd086c4a25e4943402583＝与盘现钩 blob 全等；「期望 8b785770」＝BG-15 施工笔 28b7a40f 随正前旧钉（git merge-base 现跑＝28b7a40f 系起草窗链顶 6b2cc481 祖先＝随正已在起草窗前入链）＝该行为旧钉时代读数誊写；C2 残留登记族「FX-HOOK-1 重装正钉回路＝BG-15 在册＝认领方＝主理人排程」＝BG-15 已施工闭卷（链上读数在案）＝归因失效＝V2「不含 infra 炸点」臂该枚前提已消。
    「check-adr OA-E-ADR-5 findings 计数 159」＝159 枚仅存于 2026-11-20 批次证据件（11 枚全 159）＝票面申报批次 15:28:42 无 check-adr 证据件；本席现跑 check-adr findings 0 exit 0＝159 系旧批次数非当轮现跑。
    「check-collab-buckets exit 1 BLOCK 命中一枚＝MC-BUCKET-1 仓根 .collab/quarantine」＝本席现跑本仓根 check-collab-buckets exit 0 违例 0（.collab／quarantine 盘现不存在＝已迁 .collab／board／quarantine-baigong-root-copy-2026-11-20／＝迁件笔链上在案）；MC-BUCKET-1 finding 仅存 2026-11-20／21 旧批证据件；申报批次无 collab-buckets 证据件＝第三行旧数；C1 残留登记族「V2 全绿臂受阻」前提已消（V2 实际受阻项＝provenance exit4＋sot exit2 两枚 infra＝与红-1 同根）。

绿面随登＝V2 完备性臂 awk 两式本席现跑＝5（^S[0-9]＝锚）／3（D1- 具名）命中；钉集抽核＝write-guard 502 行／634425b5／commit-audit 464／238cf3ef／memory-neutralize 273／f0335ed9／hooks.json 56／57c83b62（现盘定位＝agent-experts／baigong-software-team／hooks／hooks.json＝票面未具全径＝随登不判违例）／check-staged-declaration 196／04f2889f／run-gates 543／11a6f4d4 链面盘现两式全等；三台账开工拍 7／8＋7 复现；绕点行号未涉本票。

## 判据三 · 白名单基线件形制对表 —— 绿＋一黄

S1 豁免键形制申报＝「沿 MC-SOT-EXEMPT 先例＝行文本＋出现文件集合＝不取纯文本键防搬家盲区同制」＝真源对表＝check-source-of-truth.py 行 54—55／138／172—173 现读＝豁免键字面「行文本＋出现文件集合」＋「不取纯文本键以堵搬家盲区」逐语义命中＝申报属实＝绿。

黄-1＝S1 四字段闭集（spec_id＋行文本＋出现文件集合＋债条目归因）＝SOT 豁免键与 check-entity 既有名册豁免（行 116—130＝基名精确匹配名册）两先例的混成第三形；票面称「与 MC-SOT-EXEMPT 既有豁免实现同构」按现读两先例各取一轴＝键语义需放行段逐字钉死（消费臂＝J-1 采甲态 check-entity 判定面读臂）＝形制不判红、放行为前置澄清。

## 判据四 · 租约段机读字面＋席位写域（J 面缺失核） —— 红

path_globs／deny_globs 机读字面本身＝合法（仓根相对 posix 半斜杠＝票面自注口径全等；本票 path∩deny＝∅ 现算）。

红-3＝写集全部落点现配不可签发＋票无写域候裁槽＋先例申报不可证：

    lease-issuer 现跑探针（countersign 形制合规＝architect:值；台账重定向 scratch）＝T4 全部七枚 path_globs（含 share／三枚＋双前缀 skills／tests 四枚＋票面本体一枚）对 engineer 席逐枚 exit 2 REJECT「越出席位写域行」；config 现读＝engineer write_globs＝.collab 三段＋agents／skills／config／hooks／tests／avatars 六 glob（无 share 行无 .github 行）；子集谓词现读＝g==d ∨ g.startswith(d.rstrip('/')) ∨ d in g＝具名文件面对 skills／** 类行亦不命中（双前缀盘现路径面；探针直证）。
    票面申报 ⟦share／ 域写面＝FUXI-FX-U34 与 SWB-BKTCLS 两案当票租约在册先例沿守⟧＝台账现面不可证：leases.jsonl 现行态七枚逐枚现读＝零 share／ 条目（两文件台账全检）；config 席位行零 share 行＝先例＝不可直证。
    票内无写域随动候裁槽（T4 候裁仅 J-1 消费形态／J-2 用法形态＝无 T1-J-1／T2-J-2 同款案型位）＝施工窗当票租约必撞拒＝开工即停手＝票级自洽缺口。

（租约射程注记其二「tests／面入租约而席位 deny 让出条款」＝本席核＝qa 席注记在册＋判定层「租约在册 path_globs 命中→allow」读源在场＝让出机制本体在案；但本票 tests／ 面归工程师席执行＝engineer 席位行 tests／** 在册无让出需求＝该注记对工程师面零扰动＝不判违例。）

## 判据五 · 声明判据可机械执行性（criteria 消费体形制核） —— 黄

decision-pack.py full-rollout 消费体现读＝判据读取＝声明字段逐项**字符串等值**比对读数（行 120—128 现读；REJECT 路径写呈报类审计事件＝B4 载体在位）。本席探针实证＝expect「非4」形制下，读数填「非4」字面＝出包 OK；读数填「0」＝REJECT 读数与声明不符＝exit 拒＝「非X／0 或豁免标注行具名在场」类 expect 非谓词解析＝语义判定前置在 QA 填读面、机械比对退为字面传通＝判据仍可执行（沿表2-2 填读制）但四枚 expect 中有两枚按判据二分析在现修案下语义永不可能绿＝与红-1 同根＝本栏计黄-2（expect 形制核）＋可达性归红-1。

黄-3＝V3 段「J-1 采乙态则 check-entity 入面单」与 J-1 定义（甲＝check-entity 判定面增基线读臂／乙＝闸本体不动）甲乙互反＝票内三处（§〇 采甲随候裁／§三 采乙才入写集／V3 采乙入面单）口径互斥；且票面 path_globs 未含 check-entity.py＝采甲（荐值）终态下该枚无租约载体＝档位＋文件数（六枚＞5）随动面未备＝放行段裁甲必 rev。

黄-4＝V2 探针臂「python share／check-entity.py --root . → D1 三文件违例行归零」调用语境未钉：裸跑时 project-name 子判据记 coverage 未执行＝D1-a 臂自洗（两枚即「归零」假象）＝验收臂须 run-gates 注入语境或显式 --project-name 实参＝形制补一行。

黄-5＝V2 臂「tests／b16e／run-all.sh 或该夹具既有入口现定位复跑」＝现读 tests／b16e／ 目录仅 test_adversarial_guards.py 一枚，run-all.sh 在 tests／ 根＝票面路径不存在＝「现定位」兜底在但具名路径失实一行级。

## 判据六 · 席位写域案型表态（工单第 6 项对 T4 面） —— 随红-3

技术侧表态＝engineer 席写域不含 share／ 与仓根面（config 现读直证）；甲态（租约具名直纳）经本席实测＝对 engineer 全拒＝甲不可行直证；可行路径＝席位行扩行（乙）＝T1／T2 已具名走程序，T4 票未列＝T4 红-3 的修法＝随 rev 补同款候裁槽＋先例申报改「登记不可证」如实归因。

## 总判

- 计数＝红 3／黄 5／绿 4（绿＝三闸归零·D1 债清单对位·R-7 四组活体复算·白名单键先例对表；完备性臂／钉集／台账基线复现＝随登不另计）。
- 红-1＝两枚 B1 根因归因失实（皮总拍板锚件在场证伪／真因＝扫描域空＋调用锚径）→S5／S2 修案不达声明判据一至四→收口「缺省态零降闸」整链不可达＝放行前 rev（B1 诊断段重写＋修案与判据对齐）。
- 红-2＝§二 两行旧批次数违现跑申明（hook-health 旧钉读数＋check-adr 159）＋C2 归因失效（BG-15 已闭卷）＝rev 两行刷新＋C2 销态。
- 红-3＝写域／租约自洽缺口（全 path_globs 现配不可签发＋先例申报台账不可证＋无写域候裁槽）＝rev 补 J 槽＋先例归因改如实。
- 总判＝不可现态放行＝rev-1 后最狭窄复核＝本席红臂复跑（provenance／sot 修案对表现跑＋lease 探针复跑）即可，无需全轮复审。

## 复审-1 续段（rev-1 转绿臂·QA 席机检臂单席一次跑·append-only 追加＝v1 判词段零回改）

- 复审窗读数（本席现跑）＝链顶 e5110637（＝rev-1 入链笔）＋date 2026-11-24 17:5x＋NO_INDEX_LOCK＋tracked 脏面 0 枚；三票 rev 面两式现跑全等＝T4 261 行／415334685a843e41d52292e963f8896158536cfe＋T2 237 行／6bfdafc36e419ce0b61525cf5733c9bb1dd4750e＋T1 264 行／79464e5385fda0628f31d2297419751d0466f98a（链面＝盘现＝派工预期）；三票票型面三闸对含 rev 段全票面本席现跑＝九跑各 BLOCK 0／exit 0（rev 段自引读数互证成立）。
- 只读自证＝零 git 写；探针族全部落仓根 .scratch／QA-REV2-LC／＝台账重定向（lease 探针两态 leases 落 scratch 两枚＋pairing 样件 ledger 落 scratch）＝真账终核＝外层 1／包内 7／双前缀 8＋quarantine 副本 8＋leases 两址各 7＝开工拍终拍两式全等零染自证；探针域用毕即拆 ls 0 随完工回报。

红-1 销账＝成立（R-1 重写面与本源取证逐点对拍全命中）：
- 锚件在场＝双前缀址 agent-experts／baigong-software-team／.collab／decisions／2026-10-25-皮总拍板.md ls 现跑在场 12838 字节（单前缀址仍缺位＝v1「不存在」叙述对票面所指名址证伪）＋换锚笔 b29bc20d 链上现读在场（message 含皮总拍板×2 迁 decisions 具名）＝R-1 其一全对。
- provenance 真因对拍＝行 348 infra 分支「扫描域为空（〈分类目录〉／*／scripts／* 不存在）」现读命中＋本席独立复跑＝自包根 --root . exit 4（stderr 该行现读）／自 devkits 外层仓根跑 exit 0（旁证复现＝外层三分类 glob 命中仅 object-build／scripts／publish.py 一枚＝本仓根空集真因坐实）＝R-1 全对。
- sot 真因对拍＝行 164 DEFAULT_PKG 字面＋行 737 --pkg 缺省值现读＝仓根相对展开支；行 768—769 usage-error 支先于任何扫描与白名单消费现读；sister 仓在盘（D:／multi-agent-collab-experts／workbuddy／baigong-video-team ls 现跑）＋外层根跑 exit 0 复现直证＝R-1 其二全对。
- 缺位真例独立重扫＝全仓 spec_file 锚 28 枚／缺位恰一枚＝check-pointers.py:23 → agent-skills／object-build／references／50-directory.md（包根 ls 现跑缺位）＝与 R-1「恰一枚」点名具名全等；该枚处置归 R-3 写域随动同案面或 S2 注记面随裁＝存续申明照登。
- 新臂口径「非4／非2」可达性独立判定＝provenance 非4：bing-a 可达（空集支转 coverage 注记＋exit 0＝机械可满足）；bing-b 不可达（脚本零动则包根跑 exit 4 依旧，且 rev 替换 criteria #2 括注已绑死「＝零实例承接态 coverage 注记行具名在场」＝bing-b 态下无该行＝自斥）。sot 非2：bing-① 可达（行 164—171 存在性检查降级承接→入判定态＝判据三／四两判据均可满足）；bing-② 仅判据四可达＝判据三「现跑」按 V2 探针臂字面（python share／check-source-of-truth.py --root . 单独跑）仍 exit 2。bing-② 触 run-gates deny 让出＝与 R-3 缩扩申明互扣＝联动闭环申明照登。
- 黄新-1＝bing-b／bing-② 两臂与替换 criteria #2／#3 配对不完备（放行段若裁此两臂则 criteria 须随动改联＝裁-据联动一行级＝不挡转绿＝随登）。

红-2 销账＝成立（R-2 三行现数独立复跑对拍全等）：check-hook-health exit 0＋hooksPath-readings=0＋hook-blob 现值 6bc608017756c6c505ddd086c4a25e4943402583 与现钉全等；check-adr findings 0 exit 0（OA-E-ADR-5 命中计数现跑 0）；check-collab-buckets exit 0 违例 0＋.collab／quarantine NO_QUARANTINE_DIR 现跑。C1／C2 销态叙述成立＝V2 实际受阻项＝provenance exit4＋sot exit2 两枚 infra 本席复现（run-gates --no-write 现跑 exit 4 照登＝OA-T1 三枚 BLOCK 另面照登＝修复臂归 R-1 口径相符）。

红-3 销账＝成立（R-3 三件套齐＋探针复证）：J-3 槽补列在册（并案号 LEAD-CONSTRAINT-写域随动并案＝与 T1 rev R-2／T2 rev R-1 同案号三票互指现读）；先例归因改如实（本席两址台账 grep share／ 条目零现跑复证＝「台账面不可直证」成立）；租约段缩扩申明四裁臂示扩例在位（J-1 甲→check-entity 入 path＋deny 让出／J-2 bing-①→sot／bing-②→run-gates＋deny 让出／J-3 甲→具名直纳）；本席独立复跑 T4 path_globs 七枚对 lease-issuer（engineer＋countersign 形制合规＋台账重定向 scratch）＝七枚全部 exit 2 REJECT「越出席位写域行」＝rev 窗读数复现。

黄面处置清点：黄-3 销（R-4 甲乙互斥勘正读法钉死现读）；黄-4 销（criteria #1 已钉 run-gates 注入语境或显式 --project-name 实参）；黄-2 销（R-5 二首词闭集 {通过，绿，红，拒，当场红，具名在场}＝decision-pack 行 127 字符串等值比对现读复核＝闭集填读恢复机械比对语义）；黄-1／黄-5＝rev R-5 三具名挂账未销不静默丢＝随放行段处置＝随登。

计数变化＝红 3→0；黄 5→3（销 3＝黄-2／黄-3／黄-4；随登 2＝黄-1／黄-5；新增 1＝黄新-1）。

并案实测表（LEAD-CONSTRAINT-写域随动并案＝三票 path_globs 全集对 engineer 席 lease-issuer 两态读数＝本席并一跑枚举具名；派工全集 16 枚＝T4 七（含票面本体）＋T1 四＋T2 五（两票票面本体随登两枚＝共 18 枚）；未注入态＝config 盘现 engineer 行／注入-乙态＝scratch 注入副本 engineer 行扩四行 {share／ ＋ .github／ ＋ agent-experts／baigong-software-team／skills／ ＋ …／tests／}＝全部重定向 .scratch／QA-REV2-LC／ 用毕即拆）：

    未注入态＝18／18 枚 exit 2 REJECT「越出席位写域行」（甲态零 config 直纳＝全拒＝不可行实测直证）
    注入-乙态＝15／18 枚 exit 0 ALLOW 翻转＝T4 share／ 三枚＋双前缀 skills／ 两枚＋tests／ 一枚（六枚）＋T1 .github／ 两枚＋share／ 两枚（四枚）＋T2 share／ 四枚＋reconcile-daily 一枚（五枚）
    注入-乙态仍 REJECT＝三枚票面本体＝.collab／board／ 三票票面（board 桶 engineer deny 未让＋扩行未含＝写侧 write-guard deny 先于租约段现读＝票面本体写入主体非工程师席）
    并案一句话结论＝可行形态取乙＝engineer 席位行扩四行可兜尽十五枚施工写面；三枚票面本体须归投递窗／修票权席位另行租约＝具名不随扩。

T4 一句话结论＝rev-1 转绿成立＝红面三枚全销（归因重写对拍全命中＋新臂口径下 bing-a＋bing-① 组合使 criteria 四枚可达）＝可放行候裁（J-1／J-2／J-3 待放行段裁＋三黄随处置）。

（自靶＝本续段落笔前后 check-ticket judgment 尺＋check-pointers --target 本判词件现跑＝BLOCK 0／WATCH 0／exit 0＝judgment 尺归零；preflight 尺＝票骨架目（PF-2／PF-4）不适用判词件＝沿历轮案型不跑具名；席位纪律＝本席不写票面＝判词件唯一写面；台账三账两拍零染在册。）
