# SWB-SCRATCHCFG · config 租约随动微规格票 v1 产品席快审判词 v1

- 审票席：产品席 `pm-cfgrev`（fresh eyes·未读 QA 席并行审票产出·只落自家判词）
- 被核物：`.scratch/tickets/2026-11-11-SWB-SCRATCHCFG-seat-config-lease-sync-ticket-v1.md`（落链 `a23ccd2`·129 行·轻量维护档＝快审档位如实）
- 档位：快审（票体四字段＋引用面＋排程＋钉值抽查＝审票面四目闭集，见 §五计数表）

## 〇、开工实测读数（本席当轮现跑·禁抄旧数）

- 窗口一（审程实测轮）：`date`＝2026-11-11 00:54／HEAD＝`a23ccd2`（＝被核票落链笔本体）
- 窗口二（成文轮·本判词开端锚）：`date`＝`Wed Nov 11 07:39:46 2026`／`git rev-parse --short HEAD`＝`5cba2ea`（FX-U39 他案在飞推进＝链位较起草轮 `282f88f`、票笔 `a23ccd2` 后移，他案笔照登零碰）
- `git status --porcelain --untracked-files=no`＝仅 `M agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl` 一枚（他案在飞脏面·本席零碰零带入）
- 票钉三式复点（窗口二现跑）：s4 直跑 `python agent-experts/baigong-software-team/tests/s4/test_enforcement.py` → exit 0·PASS 行 **13**·`PASS t13_derived_consistency` 在场；BLOCK 基线 `python share/check-pointers.py 2>/dev/null | grep -c "BLOCK"` ＝ **22833**（与票 V0 钉值全等）；`grep -ci scratchg .../leases.jsonl` ＝ **0**／`wc -l` ＝ **7**（与票 §一＋V4 钉值全等）
- 引用锚在位：`ca33b5f`／`7900b07`／`f173c03`／`7fe59f1`／`8977648`／`282f88f`／`9278445`／`3cba063` 全 `git cat-file -e <sha>^{commit}` 本席实测在位

## 一、裁意忠实性（已裁(e)→S1 最小兑现链）

- **(e) 逐字对照**（`ca33b5f` §二-1）：「类B 例外单件＝取 B-i（迁回执桶）＋随动硬约束＝工程师租约禁动面随动」——裁意指向**租约面随动**（票内租约段层），未含配置常驻规则层扩面授权字样；本票把缺口定性为「配置常驻层未落位＋签发兑现面」＝另票承接，归收口登记 §二 已裁(e) 后果线不新增呈裁——**忠实，绿**。
- **S1 核心论证复核成立**：本席独立读 `write-guard.py` 现文＋跑探针实证——`glob_match` L152-153 全角括注剥离＋L157 CJK 检测；`decide()` 先 deny 后租约；**reason 内 glob 取原文字面**（探针读数见 §四）。两 config engineer 行现盘均含桶级 `".collab/receipts/**"`（`seat-permissions.json` L58／`seat-permissions-hooks-map.json` L28·数组第 9/22 项·json 实测位次与票 §一 全等；两文件该行逐行相等＝t13 断言强约束在场）。现词汇内确无否定语法——「单点除外」不可能以 glob 一行达成而不改守件，**起草席实测钉死成立，绿**。
- **零机效变化款实证**：本席做非仓面沙箱对拍——两 config 副本照 S1-a/b/c 全替换后：① write-guard 对 B-i 目标件（COLLAB-STRUCT-1 施工回执）deny 决策仍 deny，仅 reason 内 glob 字面随替换行随动（deny 机效本体不变）；② 完整包副本跑 s4 → **exit 0·13 PASS·t13 PASS**（＝同步替换下 s4 全批零翻面，不止 t13——比票 V2 声称面更强一档的独立旁证）。S1 三段逐字可照录（全角括注在 JSON 字符串内合法，副本臂 json.load 过）——**绿**。
- **rename 通道口径实证**：`agent-experts/baigong-software-team/hooks/hooks.json` PreToolUse 写钩子 matcher＝`Write|Edit|MultiEdit|Write to file|Modify a file`→write-guard；Bash matcher 只路由 `commit-audit.py`（不读 deny_globs）——`git mv` 不在 deny_globs 消费链＝「迁件动作不被拦」写实成立——**绿**。
- **S2 体例澄清**：逐字承收口登记 §四口径（双轨并存·(h) 管免忽略豁免入桶纪律／B-i 管存量单件处置）；本席构造含 S2 逐字段的样本回执跑 `check-pointers.py --target` ＝ **exit 0**（含 `<票ID>` 模板字面不触发悬空）——照收口登记 §四成文属实，**绿**。

## 二、候裁一条有效性＋本席表态（§七扩面取态）

- **留白属实**：对照 `ca33b5f` 逐字，已裁(e) 只裁「租约禁动面随动」＋B-i 处置本体，未覆盖「部署态两 config 是否让出父桶＋write_globs 扩行」机效扩面——§七确属未覆盖真分歧，呈裁程序正确（收口登记 §二 预留路径兑现），**绿**。
- **三款声称对盘核验**：甲款先例在册（engineer `deny_globs_note` 现文自证 returns/inbox/drafts 父桶让出＋双兜底成例）；乙＝缺省最小兑现；丙＝守件改动另案（本票三件封顶不含）——三态描述与现盘一致。
- **本席表态＝倾向乙**（供裁不自行拍）：产品口径理由链复核成立——① B-i 处置本体已收口（`7fe59f1` R100 恰两式）且 rename 闭口已成文，裁(e) 语义已全兑现于乙款；② 扩面（甲）净收益只剩「engineer 经租约改写 receipts 桶历史件」——案卷 append-only 语义下该行为恰应拦，扩面无正当需求；③ 甲款后果＝超出裁(e)「目标桶单点」语义的治理扩面，且动表2-1 席位行转录面（write_globs 行）＝程序成本高于本案需求（见黄-3 程序注）。

## 三、排程可执行性

- 「工程师单笔施工两 config 同批禁拆两笔（防 t13 中间态红）」§八写死＝与 t13 逐行相等断言机理对盘，**绿**。
- 声明闭集三件封顶／禁动面六列／守件零触碰清单对盘现径；票间关系与 A14 写集零交集（其写集＝share 两件＋其回执·`3cba063` 面核）照登属实；README 八条 BLOCK 不在射程照登（归 A14 rev 候补线＝收口登记 §三口径）——**绿**。
- V6 判据（回执含「落点体例澄清」计数 1）与 (h) 桶内纪律许可族（票面族＝票／回执／README 索引类件）相容——**绿**。

## 四、票内钉值现跑复点＋机理写实抽查

| 项 | 票钉 | 本席现跑 | 判定 |
|---|---|---|---|
| s4 基线 | exit 0·13 PASS | exit 0·PASS 13·t13 在场 | ✓ |
| BLOCK 基线 | 22833 | 22833 | ✓ |
| leases | scratchg 计数 0·总行 7 | 0·7 | ✓ |
| 缺口实证①② | 两 config 含桶级行·第 9/22 项·无除外形态 | 全等（json 位次实测） | ✓ |
| 三笔施工面 | 9增0删／R100 恰两式／README 1改 | `git show --name-status` 全等 | ✓ |
| glob_match 机理 | L152-178 无否定语法·L153 括注剥离·先 deny 后租约 | 现文对读全等（L152 起函数·L261-264 deny 循环·L271-276 租约段） | ✓ |

**但 V3 判据本体自锁（红-1）**：票 V3 a 式钉「施工前 reason 含 `glob='.collab/receipts/**'`（剥离后值）；施工后**同 reason 字符串逐字全等**」。本席 write-guard 注入探针实测（engineer 身份注入·`--map` 现盘 vs S1 已替换副本·`--ledger/--leases` 重定向 `.scratch/` 临时区）：reason 内 glob 段取 **deny_globs 原文字面、非剥离后值**——施工前 `glob='.collab/receipts/**'`、施工后 `glob='.collab/receipts/**（B-i 迁件目标单点除外·通道口径见 deny_globs_note SWB-SCRATCHCFG 段）'`——reason 逐字全等按字面**必不成立**（glob 段必随替换行变）。零机效变化的**本体结论**经探针成立（决策仍 deny），缺陷仅在判据措辞口径——修面＝勘正一行（改「reason 骨架前缀 `路径∈deny_globs（表2-1 明确不可写·seat=engineer glob=` 逐字在场＋glob 段随替换行字面逐字在场」或等价口径），措辞级零本体改动。

**租约段按票列字面不可签发（红-2）**：本席跑 `lease-issuer.py` 对拍（countersign 注·`--leases` 重定向临时区）：`--path-glob "agent-experts/baigong-software-team/config/**"` 单项 → exit 0 签发 OK；再加票 §六 租约段所列 `--path-glob ".scratch/tickets/2026-11-11-SWB-SCRATCHCFG-*"` → **REJECT exit 2「越出席位 engineer 写域行」**。engineer `write_globs` 无 tickets 桶行、lease-issuer 子集校验语义＝相等／前缀／**子串**三式（非 glob），票 §六 括注「config/** 在册＝签发子集校验可过」只对 config 单项成立。后果＝按票列租约段字面整段签发必拒；若剔 tickets glob 只签 config，则票附回执落笔在部署态（钩子装上时）落「路径∉当席租约」deny——**租约覆盖不可达＝程序死锁**。修面两径其一（措辞／列面级）：回执不落租约面（随 SCRATCHG 等先例体例，惯态钩子未装下可达）或呈裁扩 tickets 桶授权（＝另案，本案不值）。旁证：SCRATCHG 先例＝leases scratchg 0（票 §一 自钉）＝先例体例本已「回执不经租约面」。

## 五、计数与逐项落位

- **红 2**＝R-1 V3 a 式 glob 值口径失实致判据按字面自锁（§四·修面措辞级）；R-2 §六 租约段含 tickets 桶 glob 经 lease-issuer 实测必拒＝租约覆盖死锁（§四·修面列面级）。
- **黄 3**＝Y-1 V3 探针锚定敏感未写死：本席实测不带 `--map` 全径／锚定注时 `project_root()` 落回包根（本仓 devkits 根无 `.workbuddy/swb-anchor`＝PROJINIT 锚件未入开发仓惯态），reason 翻「路径∉当席租约」形态——V3 两跑须写死 `--map` 全径＋同环境注记，否则同 reason 对拍不可复现；Y-2 体例观察登记（非本票错）：工程师票附回执落 tickets 桶在部署态将系统性不可写（write_globs 无该桶＋签发必拒）＝既有惯例的部署态债，归治理面另账；Y-3 呈裁材料注：候裁甲若裁及＝表2-1 write_globs 行转录改动＝C1 级程序成本，票 §七 甲款未列程序面，呈裁时应补。
- **绿（抽查目）**＝G-1 裁意忠实链（§一）；G-2 S1 三段逐字可照录＋JSON 合法（副本臂）；G-3 rename 通道机理写实（hooks.json matcher 对读）；G-4 零机效变化款独立实证（探针＋s4 副本臂全批 13 PASS）；G-5 S2 澄清逐字承收口登记 §四＋样本靶检 exit 0；G-6 候裁留白属实三款对盘（§二）；G-7 排程单笔两 config 禁拆写死对盘（§三）；G-8 钉值复点全等（s4／BLOCK 22833／leases 0·7／缺口位次／三笔面）；G-9 引用锚八枚在位＋票间零交集照登；G-10 禁动面／守件清单／(h) 桶内纪律相容。

## 六、结论

**不放行——微型 rev 后可径放**（先例同型＝A14 rev 修单全措辞级判词口径）。修单两条（皆勘正级·零本体改动）：

1. V3 a 式改 reason 对拍口径（glob 段随替换行字面随动＋reason 骨架前缀逐字相等，或等价机械式）＋V3 写死探针 `--map` 全径与锚定环境注记（一并收 Y-1）。
2. §六 租约段 path_globs 列面勘正：剔 tickets 桶 glob 或写明回执不落租约面随先例体例（二选一，建议后者）。

**候裁表态（本席供裁）＝倾向乙**：裁(e) 逐字只及「租约禁动面随动」，扩面未裁属实；乙款已全兑现裁(e) 语义（迁件本体收口＋rename 闭口成文）；甲款净收益＝改写历史回执＝案卷 append-only 下恰应拦行为，且伴 C1 级转录改动成本——扩面无正当需求。

## 七、纪律自证

- 只读审票：除本判词外零改动；他案在飞面（FX-U39 链笔群、ledger.jsonl 脏面、A14 rev 在飞、qa-cfgrev 并行产出）照登零碰零带入，未读 QA 席产出＝fresh eyes 属实。
- 机理探针全落临时区 `.scratch/pm-cfgrev/`（payload／probe-ledger／probe-leases／patched map 副本／s4copy 沙箱臂），完工自删附读数（随回票）。
- 落笔前靶检 `python share/check-pointers.py --target .collab/qa/2026-11-11-SWB-SCRATCHCFG-产品席快审-v1.md` exit 0（读数随回报）；commit＝collab: 前缀·pathspec 两端齐带·FX_COMMIT_DECLARE 两端同值·紧邻无窗口·message 零 at 符号字符·禁 add -A/amend/--no-verify·输出重定向 `.scratch/` 落盘·超时给足·撞锁有界等待 30s×10 零删锁·完工 `git show --name-only HEAD` 恰一件自证。
