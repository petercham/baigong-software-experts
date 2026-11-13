# SWB-SCRATCHCFG · 工程师席施工回执 v1（票附回执·tickets 桶·(h) 体例）

- 票号：SWB-SCRATCHCFG
- 票面真源：`.scratch/tickets/2026-11-11-SWB-SCRATCHCFG-seat-config-lease-sync-ticket-v1.md`（正文 §四/§五/§六＋修订笔 v1 R1–R5＋§九随裁笔乙款＝唯一依据·逐字照做零现场改写）
- 施工席：工程师席 eng-cfgb1（一票一新鲜实例·归裁后四步路径之②）
- 回执落名：`.scratch/tickets/2026-11-11-SWB-SCRATCHCFG-工程师回执-v1.md`（＝声明闭集第三件·V6 判据靶件·精确落名施工时定＝此名）
- 两笔：笔一施工笔＝`8be8884`（两 config 同批一笔禁拆笔）；笔二＝本回执笔（链上 sha 见 commit 面自证）

---

## S2 澄清段（逐字段·居首·V6 判据靶串只在此段出现一次）

落点体例澄清：「回执」双轨并存——票附回执（过程附随件·(h) 桶内纪律许可族之「回执」指此）留 `.scratch/tickets/` 桶；案卷回执（正式收口线）落所属项目 `.collab/receipts/<票ID>-receipt.md`。两轨不冲突：(h) 管免忽略豁免面入桶纪律，B-i 管存量单件处置。

---

## 一、V0–V7 全套现跑读数（禁抄历史读数·全部本席当轮实取）

### V0 开工三读数＋基线两式（落笔前当轮现跑）

- `date`＝`Fri Nov 13 19:29:19 2026`
- `git rev-parse HEAD`＝`9f13b07cc552c074f8000010eb34d130b7b6ddf4`（＝A14 收口登记笔·与派工钉值全等）
- `git status --porcelain --untracked-files=no`＝一枚他案脏面照登零碰零带入＝`M agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl`（仓根 untracked 散件群照登不入）
- 基线① s4 直跑：`python agent-experts/baigong-software-team/tests/s4/test_enforcement.py` → **exit 0**·PASS 行 13·`PASS t13_derived_consistency`＝1（输出留痕＝.scratch／SWB-SCRATCHCFG／v0-s4-before.txt 裸文写·已随完工自删）
- 基线② BLOCK＝`python share/check-pointers.py 2>/dev/null | grep -c "BLOCK"` 当轮现跑＝**22827**（留痕＝.scratch／SWB-SCRATCHCFG／v0-block-before.txt 裸文写·已随完工自删）。对起草轮钉值 22833 窗差 **−6 EXEMPT 归因**：链窗 `282f88f..9f13b07` 共 241 笔他案笔群在册；其中 −6 定向归因＝SWB-A14QAEXEMPT 施工笔 `3715cb7`（A14 豁免层插入＝README 旧字样六枚 BLOCK 转 WATCH 留痕·其 QA 判词笔 `01c1e88` 在册 V1-a「缺省面 18247 恰减 6 旧字样 BLOCK 归零」口径·本席 BLOCK 现跑 22827 与其后链态自洽）——非本票面引入。
- 锚态现读（V3 环境注·R1/R3 口径）：`.workbuddy/swb-anchor` 不在场·仓根层级 docs 目录下 STRUCTURE 结构件不在场（裸文写·防 OA-D6 后缀多义悬空＝FX-U48 修法①先例体例）·包内 `agent-experts/baigong-software-team/docs/STRUCTURE.md` 在场 → `project_root()` 落回**包根**＝A 式主用跑法成立环境坐实。

### V1 替换行在位（前后各附）

- 前值：`grep -c "B-i 迁件目标单点除外" agent-experts/baigong-software-team/config/seat-permissions.json`＝**0**；hooks-map 同式＝**0**
- 后值：两式各＝**1**／**1**
- 逐字对拍自证＝两文件原始文本级各含票面 §四 S1-a 围栏逐字串（python `in` 判据 True·含引号 JSON 元素形态）；S1-c 段两文件 `deny_globs_note` 尾部逐字 endswith 票面围栏 True

### V2 派生面相等随动机检（s4 既有断言零翻面·只跑不改）

- 后跑 `python agent-experts/baigong-software-team/tests/s4/test_enforcement.py` → **exit 0**·`grep -c "PASS t13_derived_consistency"`＝**1**·PASS 行总数＝**13**
- 前后对拍＝`diff .scratch/SWB-SCRATCHCFG/v0-s4-before.txt .scratch/SWB-SCRATCHCFG/v2-s4-after.txt` 空输出＝**前后输出全等**
- 两 JSON 合法＝票面 §五 V2 命令原式（python json 双件 load）→ **exit 0**
- 两文件 engineer 行 `deny_globs` 逐行相等（t13 口径预验）＝True

### V3 deny 除外行生效探针（R1 A 式三条件式为准·b 式不启用随乙裁）

命令要素（写死照 R1）：`--path`＝包根字面 `.collab/receipts/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md`；`--map` 全径＝`agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json`；engineer 身份注入＝`--input .scratch/SWB-SCRATCHCFG/probe-payload.json`（`{"agent_id":"eng-cfgb1","agent_type":"software-team-engineer"}` 经 `read_identity` 主路 stdin 形态）；`--ledger`/`--leases`/`--freeze-state` 一律重定向 `.scratch/SWB-SCRATCHCFG/probe-*.jsonl` 族（临时区·完工自删）。

- **前跑**（现盘＝未替换 config·exit 0）reason 全文：

  `路径∈deny_globs（表2-1 明确不可写·seat=engineer glob='.collab/receipts/**' path=.collab/receipts/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md）→ deny`

- **后跑**（S1 已替换 config·exit 0）reason 全文：

  `路径∈deny_globs（表2-1 明确不可写·seat=engineer glob='.collab/receipts/**（B-i 迁件目标单点除外·通道口径见 deny_globs_note SWB-SCRATCHCFG 段）' path=.collab/receipts/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md）→ deny`

- 三条件判定：① 骨架前缀 `路径∈deny_globs（表2-1 明确不可写·seat=engineer glob=` 前后**逐字相等**＝True（归属分支不变）；② 前跑 glob 段＝`.collab/receipts/**` 字面在场＝True；后跑 glob 段＝S1-a 替换行逐字段在场＝True；③ 前后决策均 deny＝True。**三条件全中＝零机效变化款机械判据成立**。
- 对照随登：v1 旧式「同 reason 字符串逐字全等」＝False（R1 机理勘正在册·glob={g!r} 嵌入原样 pattern 字面，措辞随动必随 glob 段变；以 R1 三条件式为准）。
- 探针留痕＝`.scratch/SWB-SCRATCHCFG/probe-ledger.jsonl` 4 行（write_deny×2＋trigger_report×2）＝落临时区合规；真账 leases/ledger 全程零写。

### V4 签发兑现判据（状态机面登记）

- `grep -ci scratchg agent-experts/baigong-software-team/.collab/ledger/leases.jsonl` 前后＝**0→0**
- `wc -l` 前后＝**7→7** 全等＝租约面零手写反证
- 非欠账口径（§S3 成文句随登）：leases.jsonl 唯一生产权＝lease-issuer（架构签注＋写域子集校验硬闸）；本票施工**未签发**＝无可引用的架构签注串（§六租约段「席位 ID／票 ID／哈希由状态机签发，非人工填写」＋B2 租约实例化权在架构签注面，工程师席无自签权＝不强签不补录）；SCRATCHG 案卷面同口径先例旁证在册（leases scratchg 计数 0＝惯态钩子未装下可达·非欠账）。

### V5 BLOCK 计数零新增

- 施工后 `python share/check-pointers.py 2>/dev/null | grep -c "BLOCK"`＝**22827**＝V0 基线 22827 → 本票新增 **0**（config json 不入指针扫描面＋本回执落 tickets 桶不在缺省扫描域；窗差他案面＝无，前后同值）。

### V6 回执含澄清段

- V6 判据＝`grep -c` 对靶串「落点体例澄＋清」拆写防自咬（A14 判词拆写先例体例）现跑＝**1**（唯一命中＝本回执首段 S2 逐字段行·S2 逐字段比对一致＝python 原始文本级含票面 §四 S2 围栏段 True）

### V7 门禁零回归＋靶检

- 落笔前 `bash share/run-gates.sh` → **GATE PASS exit 0**（发现 151457·留痕＝.scratch／SWB-SCRATCHCFG／v7-rungates-before-build.txt 裸文写·已随完工自删；对 A14 QA 判词笔读数 151339 窗差 118＝链窗他案笔群 collab-lint 栏 EXEMPT 归因口径随 SCRATCHG/A14 先例·不归因即停未触发）
- 笔一落笔前靶检＝两 config `check-pointers.py --target` 各 **exit 0**；落笔后同式再跑各 **exit 0**
- 票面靶检（回执笔前）＝`python share/check-pointers.py --target .scratch/tickets/2026-11-11-SWB-SCRATCHCFG-seat-config-lease-sync-ticket-v1.md` exit 0；回执件靶检随回执笔 commit 面执行（读数在回执笔 commit 日志）。

## 二、施工面自证（声明闭集三件封顶·两笔封顶）

- 笔一（`8be8884`）面＝恰两件＝`agent-experts/baigong-software-team/config/seat-permissions.json`＋`agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json`（numstat 4增4删＝两文件各一行替换＋一行 note 尾 append＝S1-a/b＋S1-c）
- 零动自证（对 HEAD blob 程序化对拍）：两文件顶层键集相等 True；除 engineer 行外**其余席位行逐字相等** True；engineer 行旧元素 22→22、同位变更恰 1（即 S1-a/b 替换行）；`_anchors` 三键零动（hooks-map 顶层键集相等内含）；五键闭集零动。
- 禁动面自证：守件六枚（write-guard／lease-issuer／state-transition／decision-pack／reconcile-daily／memory-neutralize）一字未碰；`tests/` 面只跑未改（s4 只跑）；`leases.jsonl`／`ledger.jsonl` 零手写零迁移（ledger 脏面＝他案既有开工即在册照登）；`.gitignore` 零触碰；`.collab/` 案卷面零触碰；链上 SCRATCHG 三施工笔＋判词＋收口登记＋A14 笔群＋FUXI 笔群全零碰。

## 三、纪律自证（commit 全套·两笔各自）

- pathspec 两端齐带（add 与 commit 均带同件清单）；add 与 commit 同命令链紧邻无窗口；`FX_COMMIT_DECLARE` 环境变量形态＝仓根相对纯路径清单（笔一两件逗号分隔／笔二一件）；禁 add-A／禁 amend／禁 --no-verify 全程未用；message `collab:` 前缀＋尾标 [SWB-SCRATCHCFG-BUILD]／[SWB-SCRATCHCFG-RECEIPT]·零 at 符号零反引号；commit 输出重定向 `.scratch/SWB-SCRATCHCFG/` 落盘（build-commit.log）；timeout 八分钟档；开工窗 index.lock free 照登·全程未撞锁零删锁；落笔前后靶检各 exit 0；他案脏面（ledger 一枚／仓根 untracked 散件群／链上 FUXI 与 A14 笔群）照登零碰零带入。
- 临时工作物＝`.scratch/SWB-SCRATCHCFG/`（探针族／s4 前后留痕／靶检留痕／commit 日志）＝完工自删（自删读数见本席完工回报）。
