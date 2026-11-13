# SWB-SCRATCHCFG · QA 席独立验收判词 v1（四步路径之③·V1–V7 全量现跑·fresh eyes 只读零施工）

- 验收席：qa-cfgb1v（本席·一票一新鲜实例·与施工席 eng-cfgb1 零共享）
- 票面真源：.scratch/tickets/2026-11-11-SWB-SCRATCHCFG-seat-config-lease-sync-ticket-v1.md（含修订笔 v1 R1–R5＋§九随裁笔乙款＝本判词判据唯一依据·开工已全文直读）
- 验收对象两笔：施工笔 8be8884（两 config 同批一笔）＋回执笔 afb75e0（落名 .scratch/tickets/2026-11-11-SWB-SCRATCHCFG-工程师回执-v1.md）
- 判据取态：随裁笔乙款＝V3 走 R1 A 式三条件式，b 式不启用（照登随裁）。

## 〇、开工三读数（本席当轮现跑·禁抄旧数）

- date＝Fri Nov 13 20:03:38 2026
- git rev-parse HEAD＝afb75e0912a3a0ae40e2190dea2d507951e67911（＝回执笔＝链顶·与派工钉值全等）
- git status --short：tracked 脏面一枚他案照登零碰零带入＝M agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl；仓根 untracked 散件群照登不入；链上 FUXI／A14 笔群照登零碰。
- 链面坐实：git log --oneline 9f13b07..HEAD 恰两笔＝afb75e0 尾标 [SWB-SCRATCHCFG-RECEIPT]＋8be8884 尾标 [SWB-SCRATCHCFG-BUILD]；git diff --name-only 9f13b07..HEAD 恰三件＝两 config＋票附回执＝声明闭集全等，无多无少。

## 一、V1–V7 逐条读数（全部本席现跑现算·禁抄回执声称值）

- **V0 基线两式**：s4 直跑现盘＝exit 0·PASS 13·t13 在场＝1；BLOCK 缺省面现跑＝**22827**（与回执声称值对拍全等；对票面起草轮钉 22833 窗差 −6＝A14 豁免层 README 旧字样六枚 BLOCK 转 WATCH·其链上判词口径在册 EXEMPT 归因随先例）。
- **V1 替换行在位**：前值（8be8884 前像 blob 副本 grep）＝0／0；后值（现盘）＝1／1 全中。逐字对照＝两文件 engineer 行现盘替换元素与本席从票面 §四 S1-a 围栏程序化提取值**逐字相等 True**（两文件各自）；S1-c 段（票面第二围栏）在位且 note 以其收尾 True（两文件各自）。旧裸元素形态前像各 1、现盘各 0＝替换语义坐实。
- **V2 派生面随动机检**：s4 直跑 exit 0·PASS 行 13·t13 命中 1；两 JSON load 合法 exit 0；两文件 engineer 行 deny_globs **逐行相等 True**（本席程序化对拍）。回执声称之「s4 前后输出 diff 全等」留痕件已随施工席完工自删＝该声称本席不可复现，照登（现盘态独立读数为绿）。
- **V3 R1 A 式三条件式（探针两跑·重定向本席 scratch 票号族·真租约面零写）**：
  - 前跑＝8be8884 前像 hooks-map（等价施工时现盘）跑包根字面 path，reason 全文：路径∈deny_globs（表2-1 明确不可写·seat=engineer glob='.collab/receipts/**' path=.collab/receipts/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md）→ deny
  - 后跑＝现盘 hooks-map，reason 全文：路径∈deny_globs（表2-1 明确不可写·seat=engineer glob='.collab/receipts/**（B-i 迁件目标单点除外·通道口径见 deny_globs_note SWB-SCRATCHCFG 段）' path=.collab/receipts/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md）→ deny
  - 条件① 骨架前缀前后逐字相等＝True；条件② 前跑 glob 段＝旧字面 True＋后跑 glob 段＝S1-a 替换行逐字 True；条件③ 前后均 deny True。**三条件全中＝零机效变化款机械判据成立**。
  - 与回执声称两段 reason 全文逐字对拍＝**全等**。
  - 探针留痕（probe-ledger 四行＝write_deny×2＋trigger_report×2）居本席 scratch 族＝临时区合规完工自删；真 leases／ledger 零写自证＝现盘 ledger 脏面仍仅他案开工即在册一枚、探针全部重定向。
  - 锚态坐实：仓根无 .workbuddy/swb-anchor 声明件＝project_root 落回包根＝A 式主用跑法成立环境在册（两跑包根字面均入 deny_globs 分支＝判别力坐实，非「路径∉当席租约」退路形态）。
- **V4 签发兑现判据**：前值（git show 9f13b07 版 leases.jsonl）scratchg 计数＝0／现盘＝0；行数 7→7 全等＝租约面零手写。非欠账口径随票 S3 成文句照登（无架构签注串可引＝不强签不补录）。
- **V5 BLOCK 零新增**：现跑 22827＝V0 基线 22827＝本票新增 0（与回执声称值对拍全等）。
- **V6 回执含澄清段**：靶串拆写判据（落点体例澄＋清）回执内 grep＝**1** 唯一命中；本席另立居首判据：靶串命中居回执首章节段（正文「一、V0–V7」读数节之前）＝True；S2 段（票面第五围栏）整段逐字段在场＝True（程序化比对）。
- **V7 门禁**：bash share/run-gates.sh → **GATE PASS exit 0**·发现 **151457**（与回执声称值对拍全等；对 A14 判词 151339 窗差 118＝链窗他案笔群 EXEMPT 归因口径随先例照登）。靶检四件＝票面 exit 0／两 config 各 exit 0／**回执件本席现跑 exit 1**（见黄-1）。

## 二、与回执声称值逐值对拍

对拍全等项：开工链钉 9f13b07→afb75e0；ledger 脏枚他案同枚；BLOCK 22827；s4 exit 0／PASS 13／t13=1；V1 前后 0/0→1/1；V3 两段 reason 逐字全等＋三条件全中；V4 0→0／7→7；V5 22827；V6=1；V7 GATE PASS／151457；numstat 面 4增4删与两文件各一行替换＋一行 note 尾 append 形态吻合。

**不一致一处**＝V7 回执件靶检：回执笔落笔时声称 exit 0（commit 日志在册），本席现跑 **exit 1**＝三枚 BLOCK 悬空指向施工席 scratch 票号族留痕件（回执正文引用之 s4 前后留痕与 run-gates 留痕三径），根因＝SCRATCHG 先例体例「临时工作物完工自删」与「回执正文引用留痕径」的时序缝隙＝落笔时在场故当时绿、完工自删后卫检必悬空＝票面两要求互搏之设计缝隙，非施工面新增悬空、非两 config 或票面引入。另登不可复现声称项一处＝V2「s4 前后输出 diff 全等」留痕已自删（见 V2 行）。

## 三、对抗臂（本席自造三臂·取证居本席 scratch 不 commit·禁碰真文件）

- **臂A（派生面一字改动）**：现盘 hooks-map 副本改替换行一字（除外→除处）→ t13_derived_consistency **红**＝AssertionError「席位 engineer deny_globs 与源件不一致（派生面禁改写）」＝断言真实咬合，非摆设。
- **臂B（删 note append 段）**：现盘 note 摘除 S1-c 段副本 → S1-c 在位判据与收尾判据**双双红**＝判据敏感。
- **臂C（一字改动之探针侧）**：以臂A副本 map 跑 V3 后跑探针 → 决策仍 deny 但 glob 段偏离 S1-a 逐字＝V3 条件②**破**＝三条件式对一字篡改有判别力。

三臂皆按预期红／破＝V1／V2／V3 判据非虚设。

## 四、禁动面与零动自证

- git diff 9f13b07..HEAD 对名点名守件六枚／tests 全面／leases.jsonl／ledger.jsonl／.gitignore／仓根 .collab 案卷面＝**读数全空**。
- 零动自证（blob 级 8be8884^ 对 8be8884 程序化对拍·两文件各自）：顶层键集相等 True；其余席位行逐字相等 True；engineer 行 deny_globs 22→22 元素、同位变更**恰 1**；note append-only（前像为后像严格前缀）True、增量段去 S1-c 逐字后剩余为空串 True（纯尾部 append 无插改）；hooks-map 之 _anchors 三键零动 True；seat-permissions.json engineer 行除 deny_globs／deny_globs_note 外八键全零动 True。

## 五、总判

- **IS_PASS＝绿**：V1–V7 核心判据全绿·对抗三臂全按预期·禁动面全净·与回执对拍除下述黄项外逐值全等。
- 红＝**0**。
- 黄＝**1**（黄-1＝V7 回执件靶检本席现跑 exit 1＝票面「完工自删」与「回执引用留痕径」互搏之设计缝隙，根因链完整、非施工面责任；建议归治理面另账＝回执引用 scratch 留痕宜用叙述性描述或留痕改落票附件内，不入本案）。
- 绿＝**7**（V0 基线／V1／V2／V3／V4／V5／V6）＋V7 之 GATE PASS 与三件靶检（靶检四件中三件绿一枚黄）。
- 随登观察两处（不计黄）：① V2 前后 diff 全等声称系留痕已自删之不可复现声称，本席以现盘独立读数覆盖；② run-gates 内 check-adr 栏 E-ADR-4″ 未执行计不上绿＝非 pre-commit 上下文惯态照登，与本票无涉。

## 六、纪律自证（本判词笔）

- pathspec 两端齐带／add 紧邻 commit 无窗口／FX_COMMIT_DECLARE 环境变量＝本笔面仓根相对纯路径清单／禁 add -A 禁 amend 禁 no-verify／message collab 前缀＋中文正文＋尾标 [SWB-SCRATCHCFG-QA-VERIFY]／正文零 at 符号零反引号（引用用「」或裸文写）／落笔前靶检本判词件 exit 0 才落笔／commit 输出重定向 scratch 票号族 QA 目录／撞锁有界等待零删锁。
- 本席临时工作物（前像副本／探针族／留痕／对抗臂副本）居 .scratch/ 下 SWB-SCRATCHCFG-QA 族＝完工自删附读数；工程师席 scratch 取证族（SWB-SCRATCHCFG 本名族·已自删）零读零拷（fresh eyes 硬纪律·本判词正文对上述族仅叙述性提及不落可达全径留痕引用）。
- 他案脏面照登零带入＝ledger 一枚＋仓根 untracked 散件群＋链上 FUXI／A14 笔群全程零碰。
