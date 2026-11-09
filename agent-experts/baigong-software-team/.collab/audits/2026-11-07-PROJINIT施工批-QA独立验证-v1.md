# QA-PROJINITV1 · TK-PROJINIT 施工批独立验证报告 v1（fresh eyes·证伪导向）

- 席位＝qa-projinitv1（独立实例）·验证时点 HEAD＝`5d6c7a8`（开工实测）·基线＝放行登记笔 `2215108`
- 开工 `git status --porcelain` 基线残项登记：两 `.collab/ledger/`、`.scratch/FX-*` 系、`.scratch/PM-U5/`、`.scratch/SRC4Z-draft/`、`.scratch/qa-rpubrev/`、`.scratch_wbdocs.html`——全部未触碰
- 被验对象＝票面 `.scratch/tickets/2026-11-06-PROJINIT-项目锚定与初始化整改票-v2.md`（rev5 置顶口径·时效序 rev5＞rev4＞rev3＞正文·已完整直读）；交付笔 `a4aefb7`；回执笔 `5d6c7a8`
- 工程师自报一律不采信：以下每读数本席独立实跑；扫描/比对实现全部本席自写（`.scratch/qa-projinitv1/` 夹具＝probe_series.py / wg_series.py / s1b_two_state.py·跑毕即删·删除读数见 §六）

## 〇、总裁决

**红 0 ／ 黄 0 ／ 绿 17**（对账 1 ＋判据 1–13 ＋config 两片同源 ＋禁动面 ＋回执纯净性）。
登记级注记四条（非红非黄，§五）。对抗项已试不咬清单一条（§四）。

## 一、对账面（绿）

1. `git show --name-only a4aefb7`＝**恰 8 件**；与票面 rev4/rev5 八件闭集（四脚本＋dev-discipline＋SKILL.md＋两 config）**全等**；与回执 §五清单（正则独立抽取 8 件）**全等**。
2. `git diff --name-only 2215108..a4aefb7`＝恰 8 件（交付笔自身零夹带）。
3. `git diff --name-only 2215108..5d6c7a8`＝9＋1 件：8 交付＋回执（第 9 件·`collab:` 单件笔）＋`agent-skills/fuxi-skill/.collab/research/…PM-U5…`（＝链上他案并发笔 `bbed4f0`，FUXI 产品席产物·非本批面·如实登记非越集）。
4. reflog：`2215108..5d6c7a8` 区间内三笔全为 `commit:` 型，**零 amend／零 reset**（区间外旧 `edcd88c reset` 属 FUXI 他案史，不涉本链）。
5. numstat 本席重算＝**338 ≤ 420**（5+5、6+6、2+2、29+3、4×(48+22)）。

## 二、判据 1–13 逐条独立复跑读数（全样本席自造夹具·argv 传路径·runpy 逐件独立进程）

| # | 本席实跑读数 | 判定 |
|---|---|---|
| 1 | `py_compile` 四脚本逐一 exit 0 | 绿 |
| 2a | FP 锚定＋cwd＝FP/src→四读数逐字一致＝FP 绝对路径 | 绿 |
| 2b | 锚定＋FP/src 造近端 `docs/STRUCTURE.md`→四读数＝FP（锚胜近端） | 绿 |
| 2c | `SWB_REPO_ROOT`＝正斜杠盘符形覆写值→四读数＝覆写值**原字面**（不归一） | 绿 |
| 3a | 无锚无结构 cwd＝FP→四读数逐字＝包根（fail-safe） | 绿 |
| 3b | 无锚＋FP/docs/STRUCTURE.md cwd＝FP/src→四读数＝FP（事后校验路） | 绿 |
| 3c | 锚件 `project_root: ../elsewhere`→四读数＝包根（自指闭合负判咬中） | 绿 |
| 3d | 锚件无键行乱文本→四读数＝包根 | 绿 |
| 4a | 本席自签夹具租约（LI TK-PROJINIT-TEST architect `.collab/drafts/design/` exit 0）→WG 写 FP 内目标：stdout deny JSON 缺席＋stderr `ALLOW … 路径∈租约`＋exit 0 | 绿 |
| 4b | WG 写 FP/docs/ARCHITECTURE.md→deny JSON 在场（glob=`docs/ARCHITECTURE.md`）＋ledger write_deny 留痕增量 1 | 绿 |
| 4c | 无 `SWB_LEDGER_ROOT` cwd＝FP/src→`default_ledger_root()` 四读数逐字＝`FP\.collab\ledger` | 绿 |
| 5 | 本仓根 cwd：哨兵 deny（qa 身份＝越租约 deny 文案；未知身份＝席位不可归因 deny 文案）＋缺省锚＝包根；**修前对拍**＝`git show 2215108` 快照 write-guard 与本席现盘 write-guard 以同一 identity/MAP/空租约面调 `decide()` 三路径对拍＝**逐字全等**（sentinel／docs／audits 三行 pre==post True），decide 段源码 pre/post 全等 | 绿 |
| 5b | 锚定 FP＋cwd＝包根＋无覆写→四读数＝包根（边界行为钉死·H-4 挂钩随裁句在册） | 绿 |
| 6 | `tests/s4/test_enforcement.py` exit 0＋`PASS t01..t13` 十三行逐行在册（BLOCK 四行＝t05/t06 注入型预期 stderr 噪音） | 绿 |
| 7 | 四段（`ANCHOR_FILE = ` 起→`return pack` 止·55 行）sha256 本席重算＝`d4368256f255d6bd…aba9c6ce` **四件全等**（回执值 `72ad0b5e…` 与本席值不同＝抽取边界口径差异〔回执未附其命令全文〕；判据钉值＝四段一致性，一致性独立成立——见 §五注-1） | 绿 |
| 8 | occurrence 口径：`进场建档`=1／`swb-anchor`(dd)=2／`swb-anchor`(SKILL)=2 前三≥1；`只是 {root} 的末尾段`=0；dev-discipline `wc -l`=**131**（＝105＋§A 24＋S1b 补行 1＋§B(+1) rev5 公式恰中）；**路径硬写红线**：交付 8 件 grep 盘符/绝对路径/`.workbuddy` 绝对形态＝零命中（仅相对字面 `.workbuddy/swb-anchor`＝票面落位写死允许面）；config 无平台 memory 路径预填 | 绿 |
| 9 | 触及面：交付笔恰 8 件；SKILL.md L23＝deploy-gate 索引行现盘逐字在位（diff hunk 只及 L3/L24）；plugin.json/.codebuddy-plugin/bundle.lock 现值 `0.1.30` 三同源零动 | 绿 |
| 10 | 未锚态 fakeproj2 文件系统直接落锚 exit 0→2a 前半四读数翻正＝FP2；效力降级句按 rev3 黄⑤口径随动登记（现盘钩子装载态本席与工程师同读数＝工具通道无落痕，不作 H-1(a) 通道实体证据） | 绿 |
| 11 | §B 新四行逐字＝草件块（in 判定 True）；**全文件 unified diff 精确定位**＝仅两 hunk：`@@ -99,3 +99,4 @@`（旧三行→新四行·removed 面恰＝旧三行逐字）＋`@@ -105,0 +107,25 @@`（文末追加）→§九.1/.2/.4/.5 与 §一~§八**一字零动**（前后缀段逐字相等 True）；deliverables/ 段内差值＝旧三行 3／新四行 3＝**0**；§A 草件 24 行对文末块零缺失零改写；S1b 补行恰 1 行含 rev5 口径要素（S1b／平台域运行时确认／rev5／注册两件套／如实登记） | 绿 |
| 12 | 两 config json 可载 True；architect deny 不含 `docs/STRUCTURE.md`（两文件）True；源件 architect write 含 True；s4 exit 0＋t13 PASS。**扩展面**：五席 deny 含 `sources/**` 两文件十处 True＋human 行 `deny_globs: []` 改前后逐字段全等 True；**拒签双拦实测**＝LI engineer `sources/**` REJECT exit 2＋WG engineer 写 `sources/x.md` deny JSON（glob=`sources/**`）在场 | 绿 |
| 13 | S1b 两态夹具本席按票面 rev5 段判定序**自造执行器重做**（无代码实体＝工序条款自装配）：态一（模拟 memory 落位根内）registered=True＋config 两片差集非空＋json 可载＋两片同批 t13 语义复跑绿＋STRUCTURE 平台域注记≥1；态二（根外）registered=False＋config/STRUCTURE diff 空＋登记读数行在位；两态行为零反转·对路径值零断言 | 绿 |

## 三、config 两片同源（绿·本席自实现 t13 复跑）

- 现盘两 config 各席 `deny_globs` 逐行全等 True；`derived_from` 头注在位。
- 逐席键位 diff（改前后独立比对）＝恰两片键闭集：五席 deny＋`sources/**`／architect deny−`docs/STRUCTURE.md`／architect write＋`docs/STRUCTURE.md`——**零越片键**。
- human 行改前后全等 True；六席行数在位（lease-issuer `len(seats)!=6` FATAL 路在册）。

## 四、对抗面（自造还原态·对抗跑）

- ADV-1 源件 architect deny 单侧补回 `docs/STRUCTURE.md`→本席 t13 复跑**咬**（MISMATCH architect）。
- ADV-3 map 单侧删 qa `sources/**`→**咬**（MISMATCH qa）。
- ADV-2 architect `write_globs` 拿掉 `docs/STRUCTURE.md`（deny 面不动）→t13 **不咬**＝语义事实登记：t13 锁两文件 deny_globs 逐行全等，write 面不在其射程（t13 原文 `row["deny_globs"]==src_deny[...]` 实证）——**对抗项已试不咬清单仅此一条**，属判据语义边界非缺陷（write 面防护＝租约签发面写域子集校验承载，H-2 择(c) 双拦面另证）。
- 锚件负判 3c/3d、拒签双拦、越界 4b 全咬（见 §二）。

## 五、登记级注记（非红非黄·如实分账）

1. **判据 7 哈希值双读数并存**：回执 `72ad0b5e…151c01ab` vs 本席重算 `d4368256…aba9c6ce`——判据钉值＝「四段逐字一致」而非具体哈希，两跑各自四段全等成立；差异归因＝抽取起止边界口径不同（回执未附命令全文，不可逐字节复推）。登记不阻断。
2. **链上他案并发笔**：`2215108..5d6c7a8` 含 `bbed4f0`（FUXI-PM-U5 产品席件）非本批面，本批交付笔零夹带；另开工后工作区新现 `agent-skills/fuxi-skill/products/pending/mrbeast-perspective/` 两 ` M` 残项＝他席在飞工作，本席未触碰如实登记。
3. **回执落笔通道注记**：回执自陈走 `collab:` 通道落 `.collab/receipts/`（engineer deny_globs 含该面）＝沿 TK-GWP/TK-SRC4Z 先例＋派工书明令——先例一致性本席核＝在案先例多笔同型，登记不阻断。
4. **§十 S1b 补行含「TK-PROJINIT 票面 rev5 段」票面指针**＝rev5 段授权补行口径逐字内嵌（「判定序见票面 rev5 段」即授权字面），非违例过程件指针；dev-discipline L34/L83/L84 与两脚本 docstring 的 `.scratch`／案卷字样＝修前既有通用纪律文本（不在本批两 hunk 新增面内），非本批新入。

## 六、残留纪律读数

- 报告落笔前夹具区＝`.scratch/qa-projinitv1/`（81K·夹具清单：probe_series.py／wg_series.py／s1b_two_state.py／pre-fix-snapshot／fakeproj／fakeproj2／s1b-state／leases×2／ledger／s1b-register.txt／status-post.txt）。
- 报告写毕删除夹具：`rm -rf .scratch/qa-projinitv1` 毕→`git status --porcelain` 对 `qa-projinitv1` **零命中**＝仓内零运行残留（删除读数见回执呈报与 commit 后复扫）。
- 本席全程只写 `.collab/qa/` 报告一件＋`.scratch/qa-projinitv1/`（自删）；未改任何其他文件、未 push；commit 只含本报告一件（`git diff --cached --name-only` 自证附呈报）。

## 七、门禁噪音处理登记

提交时门禁存量 BLOCK/WATCH 按派工纪律 `>/dev/null 2>&1` 屏蔽＋`git log --oneline -1` 独立确认落笔；无 `--no-verify`、无 amend。
