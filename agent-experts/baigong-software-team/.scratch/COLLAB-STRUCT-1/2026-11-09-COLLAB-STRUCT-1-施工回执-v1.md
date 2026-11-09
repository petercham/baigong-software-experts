# COLLAB-STRUCT-1 施工回执 v1（工程师席·回流四型＝完成）

- 票号：COLLAB-STRUCT-1｜回执版本：v1｜施工依据＝票面 v1.1（agent-experts/baigong-software-team/.scratch/tickets/2026-11-09-COLLAB-STRUCT-1-施工分票-v1.1.md，落链 303dcec，落笔前 blob 复算 sha256 8005e7f60b7464f15447ac61791fb848593747eac738d1f64f866c49f151e4de 与 git show 303dcec blob 全等对钉成立）
- 开工读数（首跑 12:04）：date＝Mon Nov 9 12:04:35 2026／HEAD＝0a4249a1e1fee252df9a3a403e4bef5f65dea98d（≥票面 T3 收口登记笔对钉成立）／status 他案 untracked 取证面照登不碰、tracked 面净。
- 中断续飞读数（12:32）：date＝Mon Nov 9 12:32:58 2026／HEAD＝a9908e5cdb117817dbed764ef8e0b183932a4dff（链上他案 D45 线两笔 9db7f92／a9908e5 照登未触，开工锚 0a4249a 在链）／staged 面＝本票施工面大面积滞留（271 R＋19 非 R）。

## 一、两笔 commit sha 与 A/B 同批一 commit 自证

- 施工笔＝e49977aa86acd66ac5b1f1746876ecae47be24c8：name-status 构成＝251 R100＋14 M＋7 A。A 组（seat-permissions.json／seat-permissions-hooks-map.json／五席位卡／collab-fixed-structure.md／standard-sop.md／两份 README／.gitignore／tests 三件＝14 M＋1 A 仓根 README＋1 A 包内 architect README）与 B 组（audits 迁移 244 R＋adr 四件 R＋票族三件 R＋ledger 三件 A＋architect 占位 A＋20 散件新路径 A）同处一笔＝A/B 同批一 commit 自证成立。
- 补齐续笔＝d616b77（恰 20 files changed，全为 20 散件旧路径 D）：e49977a 落账时 commit 级 pathspec 用目录级 .collab/decisions 未覆盖 .collab/ 根面散件旧路径，20 件呈「新路径已入账＋旧路径滞留 staged」mv 半态；本笔以 20 旧路径精确 pathspec 补齐入账，跨两笔 -M 检测＝20 件逐件 R100（清单＝取证区 r20-list.txt）。偏离申报见 §六-1。
- 禁 amend／禁 add -A／双侧 pathspec＝逐笔 commit 级 pathspec 限定，他案 staged／残项零卷入（git show --name-only 两笔全清单 ∈ §4 闭集）。

## 二、§4 声明闭集逐件对钉

- 配置／席位卡／规范／README／.gitignore／tests 面 15 路径：14 M＋1 新建 A 全部入账（e49977a）。
- 20 散件旧→新路径：旧路径 D 入 d616b77、新路径 A 入 e49977a、跨笔 R100＝20（逐件清单 r20-list.txt）。
- 票族三件旧／新路径：R100 三件入 e49977a。
- add 面 5 新链件：仓根 .collab/README.md、包内 architect 占位 README、ledger 三 jsonl——全部 A 入账 e49977a。
- delete 面 1 件 untracked：.collab/tmp-w7-msg.txt 盘删不入 commit（留痕见 §五-4）。

## 三、§5 九判据逐条实测读数

### 判据 1（JSON 合法＋同源全等）
seat-permissions.json json.tool exit 0；seat-permissions-hooks-map.json json.tool exit 0；两文件 host／product／architect／qa／engineer 五席 deny_globs 数组逐席全等＝True。

### 判据 2（grep 钉值）
drafts 子包字样对（prd／design／adr／proposals／deploy）在 config＋agents＋collab-fixed-structure.md 三面：零命中（grep exit 1；开工基线现值 13 行）；config 面 collab/qa 字样：0（开工基线 2 文件命中）；「十一桶」在用面（config＋包内 README）：0（开工基线 4 行 5 occurrence）。

### 判据 3（ls-files 断言·终值公式钉）
全仓 qa 桶终值＝53＝开工复点两包现值之和（fuxi 51＋EAC 2＝53）→两读数相等 PASS（禁与常数 48 比数条款照执；开工复点较票面登记值 48 漂移 +3＝FUXI 线在途链笔随增，照登）。仓根 audits tracked＝10（迁入 10）；包内 audits tracked＝244（迁入 234＋目标桶既有 10 件照登并存另计）；包内 adr tracked＝4；architect tracked＝1（占位 README）；ledger 三 jsonl tracked＝3；仓根 .collab/ 根面 tracked 散件＝0（仓根 README 索引件＝本批新建，不属散件）；.collab/decisions/ 直系 tracked＝79＝开工复点 58＋归位 20＋他案 1（9db7f92 移交工单 v2，照登）。开工复点注：票面登记基线 56／qa 桶 233 均系史实登记值，开工实测现值 58／234 照登承公式。

### 判据 4（mv 保真＋防嵌套）
公式＝复点两桶和（234＋10＝244）＋adr 4＋票族 3＋散件 20＝271＝实测 R100 总数（e49977a 251＋跨笔归位 20），全 R100。两处 audits 防嵌套断言：包内 git ls-files audits 面 grep -c "/qa/"＝0；仓根同式＝0。adr 四件新旧 blob 双点对拍全等：0001-adr-initiation-trigger-criteria-draft.md＝e725a2780759／-final.md＝29eefccc5c17／0001-draft-会签-QA席-v1.md＝61add2922f33／0001-draft-会签-产品席-v1.md＝8f96375ca6ae（旧路径 drafts/adr 面 e49977a^ 对 HEAD .collab/adr 面，git rev-parse 全等）。20 件归位逐件 R100 清单＝取证区 r20-list.txt（20 行全 R100）。

### 判据 5（门禁零回归对拍·同形态两读数）
主盘形态：开工基线 GATE PASS exit 0／发现 32,442（12:05 实跑）→施工后干净复跑 GATE PASS exit 0／发现 33,429（Δ+987，不翻红）。worktree 形态对做（同形态两读数·0a4249a 对 d616b77 两 worktree 各实跑）：GATE PASS exit 0／7,233 → GATE PASS exit 0／7,350（Δ+117）。差值逐条归因（worktree 行级对拍＋路径反归一，取证区 gates-wt-base.txt／gates-wt-post.txt）：新增命中 151 行级条目，分族＝旧文 .collab/qa/ 字样族＋drafts 子包字样族＋仓根散件旧路径族＋票族 mv 旧路径族＝132 条（qa 族 44／drafts 子包族 2／仓根散件族 10／票族 mv 面 76＝族界按命中路径首匹配口径，与主盘形态 hits 分布同构）；另 19 条系本批新配置文案面触发（14＝seat-permissions.json host 行新增 .collab/adr/ 与 docs/adr/ 两写域项命中 OA-D6-3 出包指针 WATCH；4＝README 与 config 桶名录 .collab/ 字样 OA-D6-3／4 WATCH；1＝collab-fixed-structure.md 住址成文行内脱引短式字样 docs/STRUCTURE.md＝BLOCK 级新命中 1 枚，逐条申报见 §六-2）。BLOCK 族两态：24,617→24,978（主盘）＝全部悬空型命中含三族旧字样存量（qa 字样 3,680／drafts 子包 26／仓根散件名 154＝本批 mv 转悬空部分）＋既有基线悬空存量照登；归因基数开工复点＝qa 字样 222 文件／370 行、drafts/adr 80 行、十一桶 97 occurrence（随盘漂移照登）。GATE PASS 不翻红＋零「基本通过」式糊账。

### 判据 6（drill／s2 差值口径·注入形制）
开工基线（POSIX 挂载注入形制 T06_TMP 指仓内取证区挂载点）：drill-05 exit 1（红因「RED: deny 原因非 freeze 联动」）／drill-06 exit 1（红因「FileNotFoundError … 负扫面命中读数缺位」）＝缺陷台账 agent-experts/baigong-software-team/.collab/… 史实面与仓根 .collab/defects/2026-11-08-drill夹具回读编码失配与缺件引用缺陷-v1.md 同型（该台账在册只读引用）。B6 改后同形制复跑：drill-05 exit 1 红因「deny 原因非 freeze 联动」＝与基线同型；drill-06 exit 1 红因「FileNotFoundError 同路径族＋负扫面命中读数缺位」＝与基线同型→PASS（缺陷面不因本票恶化，修路另案＝禁动面未触）。补充读数照登：同两件以 Windows 盘符注入形制跑，基线 12:07 与复跑 12:44 均为 drill-05 exit 1 同红因／drill-06 exit 0 DRILL06_GREEN＝两时点同态零翻转（POSIX 挂载假红系已登记环境口径案型）。s2 夹具 python agent-experts/baigong-software-team/tests/s2/test_lease_instantiation.py：基线 exit 0→复跑 exit 0 不变。

### 判据 7（check-adr 命令形制）
python agent-skills/object-audit/scripts/check-adr.py --bundle-root agent-experts/baigong-software-team：exit 0／读数「docs/adr 盘上件=1｜桶1=1 桶2=20 桶3=1｜发现 0」＝与开工基线读数同值（docs/adr 盘上一字未动复点＝本批 diff docs 面 0 文件）。

### 判据 8（ADR 随动面 grep 钉值）
standard-sop.md「架构席终写」＝0（开工现值 1）；software-team-architect.md「docs/adr」＝0（开工现值 2＝写域行＋明确不可写行）；「可写内容：设计、ADR」＝0（开工现值 1）；lead 卡旧路由行「系统设计、ADR、开发票」＝0＋新行「ADR 文书（起草与 docs/adr 落盘＝主理人自写，不派发） | software-team-lead（本席）」命中 1；seat-permissions.json host 行含两项 .collab/adr/ 与 docs/adr/ ＝命中 1；architect 行含 docs/adr/ ＝0（json 解析面断言 False）。

### 判据 9（过渡期向前进＋票面落位核对）
落位两口径：git ls-files .scratch/tickets/ 宽 grep COLLAB-STRUCT＝0（开工现值 3→0）；bundle 面 -E 票族专名（结构名实对齐与规范成文票｜工序纪律并案维护票）＝3（开工现值 0→3）＝dev-discipline:83 唯一落点复现；自指免疫＝本施工分票 v1／v1.1 与回执件名含 COLLAB-STRUCT 但不含票族专名，不入计数。向前进核对：放行笔 0a4249a 至本回执区间，qa 旧桶 A 状态新增＝0（区间内 qa 桶行全为本批 R 迁移行）。

## 四、租约段实例化（票末租约由本实例执行）
engineer 席经 lease-issuer.py 签发：countersign＝architect:COLLAB-STRUCT-1-v1.1／path_globs 四 glob（config／agents／skills／tests bundle 面行级 glob，逐 sub-glob 经写域子集校验）exit 0／hash 302bb15a8d6ac6bf9cdffb6105f824560756f4dbb46c75881a121e7441e8e9a0 入账 leases.jsonl（该文件随 B3 补链同批入链）。仓根治理面路径（.collab/、.scratch/ 仓根面）不在 seat-permissions 席位写域可枚举行内＝签发面不开口，仓根 mv 操作经 git 命令面由票面授权执行（§6 已明判非禁动面），如实申报见 §六-3。

## 五、§7 必附项
1. commit sha＝e49977a＋d616b77（§一）。
2. name-only／name-status 与 §4 闭集逐件对钉＝§二。
3. 九判据逐条实测＝§三。
4. tmp-w7-msg 删除前留痕三值：23 行／2,270B／sha256 037a83b30b08741c9bf476496284ce7357b5f164388f4f1a697e5627a9a50056——开工复点与票面钉全等无漂移，删前复算再次全等后盘删。
5. check-ignore 前后对拍：agent-experts/baigong-software-team/.collab/audits/x.md 前（12:06）与后（12:36）两态均 exit 1 不 ignore（开工基线 exit 1 在册）；.collab/tmp-w7-msg.txt 两态均命中 .gitignore:36 行（删前复点）。
6. 门禁同形态两读数＋差值逐条归因＝§三判据 5。
7. A/B 同批一 commit 自证＝§一。
8. 20 件归位逐件 R100＝§三判据 4＋取证区 r20-list.txt。

## 六、偏离与如实申报（逐条）
1. 施工落账拆两笔：e49977a（A+B 主体同批）＋d616b77（20 散件旧路径删除面补齐）。成因＝commit 级 pathspec 目录级条目未覆盖仓根 .collab/ 根面散件旧路径，e49977a 落账后 20 件呈 mv 半态滞留 staged；续笔以 20 旧路径精确 pathspec 补齐，跨笔 -M 检测 R100 全等零内容变。「A/B 同批一 commit」在 e49977a 成立，B9 旧路径面分裂续笔＝形态偏离如实申报，非语义违背（配置指新名／实体就位两态未并存）。
2. 门禁 BLOCK 族新增一枚非三族旧字样归因：agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md 第 31 行（A4 住址成文行·票面逐字条款「不得改写」）内脱引短式字样 docs/STRUCTURE.md（原文以反引号包裹）被 check-pointers 判悬空 BLOCK（该文件居 skills/sop/references/ 下相对解析落空；目标实体 agent-experts/baigong-software-team/docs/STRUCTURE.md 实存在位）。两条款冲突（逐字不得改写 vs 短式指针照例改全路径）从「逐字」条款，新 BLOCK 一枚登记在册＝advisory 路由不拦提交、GATE PASS 不翻红；短式指针已知案型照登。
3. 租约实例化形制申报：票末租约段 path_globs 语义为「覆盖 §4 闭集全路径」，lease-issuer 子集校验使仓根面路径（.collab/**、.scratch/**）无法经席位写域签发（写域行无该等前缀）；本席以 engineer 席 bundle 面四 glob 租约＋票面 §4 声明闭集承载仓根面授权，全程 git 命令面操作，未绕任何写侧机件。
4. 开工复点漂移照登（一切数值以开工复点为准条款）：五卡 sha 钉与票面登记值全异（链上 SEMGV-T3 施工笔 56f63da／e880edb 生效＝票面条款「即以其为基线，五卡 sha 钉作废按实测重取」命中）：product 47 行／3,699B／81fa026d8c55→施工后 47／3,665／c9171b67b283；architect 48／4,129／b231c9370ffd→48／3,852／3e16cdc07c20；qa 50／4,110／a873b3d8679a→50／4,100／6d9674b5225b；engineer 50／4,211／1d9367e52ecf→50／4,202→4,204／41465129c60d；lead 78／5,639／4d04ae313a6e→79／5,743／3ccbf17e4c14（lead 卡行数 78→79＝路由拆行登记）。fuxi qa 51（登记 46／48 漂移＝他案链笔随增）；包内 qa 复点 234（登记钉 233 同值）；decisions 直系复点 58（登记 56＋2）。归一 CRLF 口径注：仓内 autocrlf 环境，写盘 LF／checkout CRLF 既有口径（SEMGV-T3 收口口径随注在册）。
5. 十一桶在用面终值 0 后，历史案卷＋六外包旧字样未触（禁动面）：全仓「十一桶」occurrence 复点 97→施工后仍存史实面；.collab/qa/ 历史内文 222 文件／370 行照登不改（案乙口径＝新名生效点起按新名、旧文不追改）。
6. 取证区：agent-experts/baigong-software-team/.scratch/COLLAB-STRUCT-1/ 内留证小文件不 commit；中断前产生的门禁／commit 大输出文件（49M＋26M＋14M＋7.9M）已按清理判据删除（删前关键汇总行已固化于 *-summary.txt 小件）；drill 注入 Temp 目录（仓内挂载点与 D:/cs1-drill-tmp）批毕已清＝删除读数见本段；worktree D:/cs1-wt 已 remove。
7. message 零 at 符号字符（以「at 符号」字样代）；index.lock 抢占两次均等待重试未删锁。

## 七、净化对照表（§2 各替换文本 相对 规格来源 v2 票——agent-experts/baigong-software-team/.scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v2.md，251 行／46,944B／链笔 5eeeb3a——的删除／替换／定位串逐处）

写盘替换文本与 v2 差异全表（＝v1.1 依「自包含成文·替换文本内不得含链笔号／出处钉／过程编号／案卷指针」条款对 v2 的净化处；同名同值处不列）：

1. A1 第 3 处：v2 括注「（ADR 文书执笔权归主理人，架构席 adr 两面写权全清）」→ v1.1／写盘＝「（ADR 文书执笔权归 host）」（定位串＝architect 行 write_globs 删 docs/adr/ 项句）。
2. A1 第 8 处：v2 句内〔红-2 勘正：…〕括注整段删除；写盘 deny_globs_note 三处随动文本与 v1.1 逐字（① .collab/drafts/deploy/→.collab/drafts/ ② 十一桶闭集内 …qa… 段→十七桶闭集内 …audits… 段 ③ 首句先决真源指针「十一桶闭集」→「十七桶闭集」）。
3. A1 第 9／10 处：v2 尾部〔黄-1 在用锚点名随动①〕〔ADR 裁定⑧写权改判落点〕括注删除；写盘替换文本同值（（B1-D·十一桶）→（B1-D·十七桶）；docs/*（除转正代写通道）→docs/*（除转正代写通道与docs/adr/））。
4. A2：v2〔SRC4Z 两文件五席数组全等约束在册〕→ v1.1「（两文件五席数组全等约束）」；v2〔v2 新增随动，v1 A2「host 行零动」作废〕删除；v2〔黄-1 在用锚点名随动②〕删除。
5. A3 lead 卡新行：v2＝「| ADR 文书（起草与 docs/adr 落盘＝主理人自写，不派发，裁定 67a3462） | software-team-lead（本席） |」→ v1.1／写盘＝删「，裁定 67a3462」（链笔出处钉清除）；余四卡写域行替换文本与 v2 逐字同值。
6. A4 桶名闭集行：v2〔黄-2 修：v1 拟 16 桶漏 returns/…钉证，补桶入闭集〕→ v1.1「（17 桶；returns/ 为在用实体桶补录，仓根＋包内 tracked 实体各 2 件已钉证）」；v2 入库面行括注「ledger 补链＝裁定⑤」→ v1.1「ledger 补链＝账本三文件入链后入名录」。
7. A4 依据注记两行：v2 行①「（裁定 2026-11-08 b8bdadc）」删除、「同裁定结构落改」→「结构落改」；v2 行②〔黄-7 业界锚〕标删除＋句尾「；本仓两证 b0b449d／b2150c5 位次旁证」整段删除（案卷指针清除）。住址成文行＝v1.1 新增（v2 无此行），逐字入 collab-fixed-structure.md／两份 README 三处。
8. A5 仓根 README：v2「照裁定目标态表誊入…〔ADR 裁定⑧〕」→ v1.1「逐行名录以本票 §2 A4 的 17 桶闭集行与 config/seat-permissions.json 各席 write_globs 为据就地成文」（桶总表据此就地成文，adr 行法定写席＝主理人照执）；去歧义句「历史案卷内 .collab/qa/ 字样＝改名前旧路径，读作 .collab/audits/」＝v1.1 新增逐字行（两 README 各一）。
9. A7 第 1 款：v2「知悉/授权放行」→ v1.1「知悉／授权放行」；v2 尾括注「照 ES E-ADR-1″」删除（出处钉清除）。
10. A7 第 2 款：v2「（誊聚权不含裁量·条款甲语义延伸及重誊；落位仍在 .collab/drafts/adr/ 既有写域＝零新开写域）」→ v1.1「（誊聚权不含裁量、执笔权归主理人；落位 .collab/adr/＝零新开写域）」（落位桶名换代随 ADR 裁定⑧＋过程编号「条款甲语义延伸及重誊」改写）；v2「（A1-2/A1-5 承接）」删除；v2「（输入决策权恒在人类侧，三席会签不替代决策）」删除。
11. A7 第 3 款：v2「主理人职责＝执笔＋落盘担责（R10/R11/R21 语义随写权移主理人）」→ v1.1「主理人职责＝执笔＋落盘担责。」（过程编号清除）；v2「会签保留项落各席既有写域…＝零新写域」句并入第 2 款会签补件句（v1.1 定位）。
12. A7 第 4 款：v2「ADR 记的是四方已收敛决策，非架构单方设计稿」→ v1.1「ADR 记的是多方已收敛决策，非主理人单方草案」；v2「（转正代写通道·制度③）」→ v1.1「（转正代写通道）」（过程编号清除）。
13. A7 写权射程申报段：v2「（software-orchestration 随包技能域（B345 同域先例＝架构席随包技能维护权射程）；与 B345 票写集（handoff/dev/dispatch-discipline 三件＋SKILL.md）零交叠」→ v1.1「本件属随包技能域；standard-sop.md 不在并案维护票声明闭集内，两写集零交叠」（案卷指针与链笔号清除）。
14. B2 历史态照登行：v2「旧工序（架构席终写态）历史事实」→ v1.1「旧工序历史事实」；v2「ADR 裁定⑬」→ v1.1 无前缀（过程编号清除）。
15. B5：v2「（承 v1 我定形态，候裁③可推翻）」「理由三条照 v1」「与 host .collab/archive/」→ v1.1「归档子包落位＝drafts/archive/（包内…）」「不复用仓根 .collab/archive/」「与仓根 .collab/archive/（退役定稿落位）语义分域不混」（候裁编号与出处清除；理由③对象名按盘路径）。
16. B7：v2「违例A 条款成文」「违例实证在册＝…287→291 持续漂移」「与候裁①存量射程正交」→ v1.1 删编号与实证句（条款本体逐字）。
17. B8：v2「本票族三件现落仓根＝落点违规（主理人实证归因在册）」括注＋〔申报：本 v2 补写时点仍住违例位…〕整段删除（写盘 mv 文本不含）。
18. 其余 §5／§4／§6 面替换文本无写盘内容（判据与规格面），未入写盘。

## 八、三态明示（逐条分开写）
1. 做了但没落盘：两规格件＋票面全文直读、消费面只读实测（wc／sha／grep／ls-files／门禁基线／drill 形制／check-adr 形制／check-ignore）——仓内只读命令＋worktree 只读对做。
2. 落盘了但没提交：回执件本体落盘后至 git add／commit 前为工作区新增态；取证区小文件按票面 B8 条款保持不 commit。
3. 提交了但没对账：两笔落账后至本回执完工回报给出「status 他案照登＋git show 全清单对钉」实测前此态存在；由本回报补齐。

## 九、中断申报
本实例中断＝上游 502 网络故障（非执行缺陷）；中断现场＝施工面滞留 staged（D-95 条款形态）；处置＝查盘核对补齐落账，不缺损、零重施工；施工笔与补齐续笔 message 内均已随注。

——工程师席 eng-struct-c1·2026-11-09
