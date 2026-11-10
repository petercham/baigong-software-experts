# SWB-SCRATCHCFG · config 层租约随动微规格票（v1·纯规格·零施工）

- 票号：**SWB-SCRATCHCFG**
- 票名：**config 层租约随动与签发兑现微规格票**
- 票型：维护（轻量工作分支·体例四查全列＋引用面必查，本体／链条面按射程申报注理由＝T10 轻量档）
- 起草席：架构席 `arch-scratchg1`（＝SCRATCHG v2 租约段作者席·起草权归本席＝收口登记 §二路由兑现）
- 票面落点：`.scratch/tickets/2026-11-11-SWB-SCRATCHCFG-seat-config-lease-sync-ticket-v1.md`
- 开端读数：ANCHOR＝见 §一（起草轮现跑·禁抄旧数）
- 前置票：SWB-SCRATCHG（v2＝`7900b07`·收口登记 `282f88f`·本案任务书来源＝其 §二 黄-1 处置路由＋§四 澄清建议）
- 候裁点：单列 §七（一条·起草暴露真分歧再入呈裁面＝收口登记 §二 预留路径兑现）

> **票面自注**：本票面落 tickets 桶（豁免行覆盖·SCRATCHG 规则块 L59–L64 现势）；本票射程＝包级 config 两件，与票面落位无交互。

---

## 一、开工实测读数（起草轮现跑·全部当轮实取）

| 项 | 命令 | 实测读数 |
|---|---|---|
| 时点 | `date` | `Wed Nov 11 00:39:50 2026` |
| HEAD | `git rev-parse --short HEAD` | `282f88f`（＝收口登记笔本体） |
| tracked 面 | `git status --porcelain --untracked-files=no` | 净（空读数） |
| 缺口实证① | `grep -n "receipts" agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json` | L28 engineer `deny_globs` 含 `".collab/receipts/**"`（桶级行·无单点除外形态；数组位次＝第 9/22 项·python json 实测） |
| 缺口实证② | `grep -n "receipts" agent-experts/baigong-software-team/config/seat-permissions.json` | L58 engineer 同款含行（同位次）；两文件除该行外 receipts 字样零命中（豁免类字样 regex 扫描零命中＝QA 判词 `9278445` §三复现） |
| 派生面断言在场 | `agent-experts/baigong-software-team/tests/s4/test_enforcement.py` L261–273 | t13_derived_consistency＝hooks-map 各席 `deny_globs` 逐行相等源件断言（L271）＝改一必咬另一 |
| s4 基线（现跑） | `python agent-experts/baigong-software-team/tests/s4/test_enforcement.py` | **exit 0**·13 用例全 PASS（含 `PASS t13_derived_consistency`；注：本仓 pytest 模块缺席＝该类件走自带 run_self 直跑形态） |
| 签发面读数 | `grep -ci scratchg agent-experts/baigong-software-team/.collab/ledger/leases.jsonl` | **0**（文件在场·总行数 7） |
| 守卫消费机理 | `agent-experts/baigong-software-team/skills/sop/scripts/write-guard.py` L261–264＋L152–178 | deny_globs 逐 globs 消费先于租约面（命中即 deny）；`glob_match` 先剥全角括注再判——**含 CJK 的 pattern＝描述行不参与机械匹配**；括注剥离后 pattern 机效不变（既有成例＝hooks-map host 行 `docs/*（除转正代写通道与docs/adr/）`＝括注描述态·机效仍 `docs/*`） |
| 三笔施工面在册 | `git show --name-only f173c03 7fe59f1 8977648` | .gitignore 9增0删／R100 恰两式位点／README 1改——config 两件不在 SCRATCHG 声明闭集＝工程师守闭集未越权（QA 判词黄非红定性输入·复核全等） |

**引用面**（轻量档必查项）：收口登记件 `.collab/2026-11-11-SWB-SCRATCHG-收口登记-v1.md`（`282f88f`）§二／§四；QA 验收判词 `.collab/qa/2026-11-11-SWB-SCRATCHG-QA席施工验收判词-v1.md`（`9278445`）§三／§五；SCRATCHG v2 票 `.scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v2.md`（`7900b07`）§六租约段（规格母本）；锚 `ca33b5f`（裁定登记）／`f173c03`／`7fe59f1`／`8977648`／`282f88f`／`9278445` 全部 `git cat-file -e <sha>^{commit}` 起草轮实测在位。

## 二、缺口定性（承 QA 黄-1·本席复核一致）

已裁(e)「租约随动」硬约束在 SCRATCHG v2 **票内租约段已闭合**（deny 加目标桶单点除外表述），但**配置常驻规则层未落位**：两 config 文件 engineer 行 deny 枚举含 `.collab/receipts/**` 桶级行、无任何除外形态；leases.jsonl SCRATCHG 签发记录 0。devkits 侧 hooksPath 未装（HOOKHEALTH `hooksPath-readings=0`＝本仓惯态）＝物理拦截现不在本仓发生；缺口实质＝**部署态语义面**（engineer 再写该 receipts 目标件将 deny／未来 B-i 型迁件同撞）＋**签发流程兑现面**（零记录）。

**机理写实（防误判·写死）**：现有 config 消费词汇（write-guard `glob_match`＋`decide()` 先 deny 后租约）**无机械否定语法**——deny 行内全角括注经 L153 剥离后**零机效变化**（host 行成例在册）。故「单点除外」不可能以增删一行 glob 语法在两 config 内达成而不改守件；凡声称达成者＝误读消费链。本票据此成文 S1（零机效变化款）＋候裁 §七（机效扩面真分歧呈裁）。

## 三、目标（票体四字段①）

终态一句话＝**两 config 文件 engineer 行按已裁(e) 完成措辞级随动（括注除外形态＋注记通道口径成文·零机效变化）、落点体例澄清一行成文、签发兑现定性为状态机面并写明路径判据；部署态机效扩面与否归 §七候裁，本票不预设。**

## 四、规格（票体四字段②·逐条到落位行级）

### S1 · 两 config 文件同步随动（三件封顶之内·逐字写死）

**S1-a** `agent-experts/baigong-software-team/config/seat-permissions.json` L58 engineer 行 `deny_globs` 数组：将元素 `".collab/receipts/**"` 原位替换为——

```
".collab/receipts/**（B-i 迁件目标单点除外·通道口径见 deny_globs_note SWB-SCRATCHCFG 段）"
```

**S1-b** `agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json` L28 engineer 行 `deny_globs` 数组：**同款逐字替换**（两文件派生面逐行相等＝t13 断言强约束，改一必随另一）。

**S1-c** 两文件同位 `deny_globs_note` 字段尾部各 append 同一段（逐字）：

```
SWB-SCRATCHCFG 随动段＝已裁(e) B-i 通道口径成文：B-i 型存量迁件经 git rename 通道执行（write-guard 消费面＝Write/Edit PreToolUse 写钩子，rename 不在其消费链＝迁件动作不被拦）；迁后件之后续写入保护维持桶级 deny 不变（案卷 append-only 语义承接）；租约签发兑现＝状态机面——leases.jsonl 只经 lease-issuer 生产（架构签注＋写域子集校验），禁手写补录。
```

**S1 机效声明（写死）**：替换行经 `glob_match` L153 括注剥离＋L157 CJK 检测链＝剥离后仍 `.collab/receipts/**`＝**机效零变化款**（同 host 行 `docs/*（除…）` 成例＝词汇内措辞随动上限）；本票默认射程到此为止，**机效扩面（父桶让出＋写域扩行）不在本票**＝§七候裁。

### S2 · 落点体例澄清一行成文（收口登记 §四口径承接）

本票 §二 后不设新件——澄清条款入施工回执首段（逐字）：

```
落点体例澄清：「回执」双轨并存——票附回执（过程附随件·(h) 桶内纪律许可族之「回执」指此）留 `.scratch/tickets/` 桶；案卷回执（正式收口线）落所属项目 `.collab/receipts/<票ID>-receipt.md`。两轨不冲突：(h) 管免忽略豁免面入桶纪律，B-i 管存量单件处置。
```

### S3 · 签发兑现定性（状态机面·勿手填规格）

判定如实＝**签发兑现属状态机面非人工件**：leases.jsonl 唯一生产权＝`lease-issuer.py`（countersign `architect:` 前缀硬闸 L110–115＋写域子集校验 L123–127）。SCRATCHG 补签现不可行＝其请求面（`.gitignore`＋receipts 目标件）均不在 engineer `write_globs` 行内＝子集校验必 REJECT——**此即 §七候裁依赖链**：机效扩面（甲）裁否则签发兑现对该案永久不可达。兑现路径成文＝**未来 B-i 型票随票经 B2 租约实例化（本席签注）**；SCRATCHG 案卷面登记口径＝leases.jsonl scratchg 计数 0 **非欠账**（钩子未装惯态＋补签被写域校验拦），判据见 V4。

### 声明闭集（施工面封顶三件内）

- 声明闭集：
  - `agent-experts/baigong-software-team/config/seat-permissions.json`（S1-a＋S1-c）
  - `agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json`（S1-b＋S1-c）
  - 票附回执＝仓根 `.scratch/tickets/` 桶内本票同名族回执件（基名 `2026-11-11-SWB-SCRATCHCFG-工程师回执` 族·精确落名施工时定）（tickets 桶·(h) 体例·含 S2 澄清段）

### 禁动面

- 守件零触碰：`agent-experts/baigong-software-team/skills/sop/scripts/write-guard.py`／`agent-experts/baigong-software-team/skills/sop/scripts/lease-issuer.py`／`agent-experts/baigong-software-team/skills/sop/scripts/state-transition.py`／`agent-experts/baigong-software-team/skills/sop/scripts/decision-pack.py`／`agent-experts/baigong-software-team/skills/sop/scripts/reconcile-daily.py`／`agent-experts/baigong-software-team/skills/sop/scripts/memory-neutralize.py` 一字不碰（机效扩面涉守件者归 §七另案）；
- `agent-experts/baigong-software-team/tests/s4/test_enforcement.py` 及其余 tests 面零触碰（既有断言零翻面＝只跑不改）；
- `leases.jsonl`／`ledger.jsonl` 及账本面零手写（状态变更必经脚本）；
- 两 config 除 S1-a/b/c 指定行段外零动（五键闭集／其余席位行／`_anchors` 三键零动）；
- `.gitignore` 零触碰（SCRATCHG 已收口面存续）；`.collab/` 案卷面零触碰；
- 链上史笔不追改：SCRATCHG 三施工笔＋判词＋收口登记件全零碰。

## 五、验收标准（票体四字段③·全机械·occurrence 口径·命令＋钉值）

- **V0 开工**：`date`＋`git rev-parse --short HEAD`＋`git status --porcelain --untracked-files=no` 三读数登记；基线两式：s4 直跑＝exit 0（13 PASS·起草轮钉值）＋BLOCK 基线＝`python share/check-pointers.py 2>/dev/null | grep -c "BLOCK"` 当轮现跑登记（起草轮读数＝**22833**·全部系历史既有悬空面含 README 八条在册——他案窗差按 EXEMPT 逐笔归因口径随 V7 先例）。
- **V1 替换行在位**：`grep -c "B-i 迁件目标单点除外" agent-experts/baigong-software-team/config/seat-permissions.json` ＝**1**；hooks-map 同式＝**1**（前后各附，前值 0）。
- **V2 派生面相等随动机检（s4 既有断言零翻面）**：`python agent-experts/baigong-software-team/tests/s4/test_enforcement.py` → **exit 0** 且 `grep -c "PASS t13_derived_consistency"` ＝**1**、PASS 行总数＝**13**（前后对拍全等）；两文件 JSON 合法＝`python -c "import json;[json.load(open(p,encoding='utf-8')) for p in ('agent-experts/baigong-software-team/config/seat-permissions.json','agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json')]"` exit 0。
- **V3 deny 除外行生效探针（零机效变化款·机理钉）**：write-guard 注入探针两跑（--path＝`agent-experts/baigong-software-team/.collab/receipts/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md`＋engineer 身份注入·`--ledger`/`--leases` 重定向至 `.scratch/SWB-SCRATCHCFG/probe-ledger.jsonl` 族＝临时区合规完工自删）：施工前 deny 决策 reason 含 `glob='.collab/receipts/**'`（剥离后值）；施工后**同 reason 字符串逐字全等**＝措辞随动机效零变化自证。若 §七裁甲，本判据换装预登记 b 式：reason 翻为「路径∉当席租约」形态（＝deny_globs 不再命中·租约闸接力）——两式皆机械可跑，取态随裁。
- **V4 签发兑现判据（状态机面登记）**：`grep -ci scratchg agent-experts/baigong-software-team/.collab/ledger/leases.jsonl` 前后＝**0→0**（非欠账口径＝§S3 成文句在回执在册）；租约面禁手写反证＝该文件 mtime/行数前后全等（`wc -l`＝7）。
- **V5 BLOCK 计数零新增**：`python share/check-pointers.py 2>/dev/null | grep -c "BLOCK"` 与 V0 基线对拍＝本票新增 **0**（config json 不入指针扫描面＋票附回执落 tickets 桶不在缺省扫描域；他案增数 EXEMPT 逐笔归因）。
- **V6 回执含澄清段**：`grep -c "落点体例澄清" <票附回执件>` ＝**1**（S2 逐字段比对一致·回执精确落名施工时定，本判据随回执名执行）。
- **V7 门禁零回归**：`bash share/run-gates.sh` → GATE PASS exit 0（前后发现数不新增·他案窗差 EXEMPT 归因随 SCRATCHG V7 先例口径）；票附回执靶检＝`python share/check-pointers.py --target <票附回执件路径>` exit 0。

## 六、边界约束（票体四字段④）

- **票间关系**：＝SCRATCHG 已裁(e) 施工后果线（收口登记 §二路由），**不新增呈裁**除 §七一条真分歧；归 A14 线（`3cba063`）零交集（其写集＝share 两件＋其回执，本票写集＝包级 config 两件＋票附回执——集合无交）；README 八条 BLOCK 并册 A14 rev 候补线（收口登记 §三）不在本票射程。
- **租约段**（票内·经架构签注由 B2 lease-issuer 实例化）：
  - path_globs：`agent-experts/baigong-software-team/config/**`（本票 S1 两件·注：engineer 写域行 `config/**` 在册＝签发子集校验可过）；`.scratch/tickets/2026-11-11-SWB-SCRATCHCFG-*`（票附回执）
  - deny_globs：守件／tests／账本面／`.gitignore`／SCRATCHG 已收口三面（按 §四禁动面同文）
  - 席位 ID／票 ID／哈希：由状态机签发，非人工填写
- **同源与引用纪律**：引用全径全写（本票各件路径均现径实测在位）；commit 锚见 §一；S1 三段替换文本＝本票围栏唯一真源，工程师逐字照录禁改写。
- **回执与 commit 纪律**：票附回执落 tickets 桶（S2 段居首）；每笔 `collab:` 前缀·pathspec 两端齐带·FX_COMMIT_DECLARE·紧邻无窗口·message 零 at 符号字符·禁 add -A/amend/--no-verify·输出重定向 `.scratch/` 落盘·超时给足·撞锁有界等待零删锁·完工 `git show --name-only HEAD` 恰一件自证。

## 七、候裁单列（真分歧呈裁·收口登记 §二「起草暴露真分歧再入呈裁面」兑现）

**唯一候裁＝部署态机效扩面取态**：措辞随动（本票 S1＝零机效变化款）后，部署态 engineer 再写 B-i 目标件仍被桶级 deny 拦（迁件动作经 rename 通道不受拦＝已闭一半；**后续写入**半截仍拦）。扩面两式：
- **甲（先例模型）**：仿 returns/inbox/drafts 让出成例——engineer deny 枚举让出 receipts 父桶＋`write_globs` 加 `.collab/receipts/` 授权行，防护＝签发面写域子集校验＋写侧「路径∉当席租约即拒」双兜底（纵深减层先例已在册）；后果＝engineer 经租约可及整个 receipts 桶（超出已裁(e)「目标桶单点」语义＝扩面治理决策＝归裁）；裁甲则 V3 换 b 式＋签发兑现链解锁（SCRATCHG 补签仍受「历史案惯态」限制随裁）。
- **丙（守件扩展）**：write-guard 消费链增否定例外键（如 `deny_exceptions`）＝守件改动另案（含 tests/s4 扩展）——本微票三件封顶不含。
- **乙（现状款＝默认缺省）**：S1 措辞随动＋rename 通道口径成文＝已裁(e) 语义最小兑现，后续写入拦＝案卷 append-only 语义下工程师本不应改写 receipts 历史件（拦即正确）；不扩面。
起草席立场（供裁不自行拍）：**倾向乙款**——B-i 本体已收口、rename 通道闭口已成文，扩面收益只剩「未来工程师经租约改历史回执」＝恰为应拦行为；甲的纵深减层先例彼时因授权子域常态化，本案无此常态需求。

## 八、排程建议

双席窄审（本微票体量＝轻档可并席快审）→ §七归裁 → 工程师单笔施工（两 config 同批一笔＝派生面强约束禁拆两笔防中间态断言红）→ 票附回执一笔 → V1–V7 判据随回执 → 收口随主理人。与 A14 rev 线（README 八枚入豁免）互斥零交集照登。

---

## 附·起草笔自证

- 落笔前靶检：`python share/check-pointers.py --target .scratch/tickets/2026-11-11-SWB-SCRATCHCFG-seat-config-lease-sync-ticket-v1.md` → exit 0（读数随回报）。
- 探针面：V3 探针要求 `--ledger` 重定向至 `.scratch/SWB-SCRATCHCFG/` 族——起草轮本席未跑 write-guard 探针（零写面自证＝无需探针，机理直读 L152–200/L243–274 现文在册）；若施工席跑，完工自删附读数（§4.4-A-2 消费面沿用）。
- 零触碰自证：两 config／守件／账本／SCRATCHG 三面全程 diff 空集；本笔面恰票面一件。