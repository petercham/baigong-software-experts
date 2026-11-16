# QA-cfgrev2 · SWB-SCRATCHCFG 票面修订笔 v1（1d9ba4d）QA 席窄复核 v1

- 审票席：QA 席 `qa-cfgrev2`（fresh eyes·只读零改·证伪导向；产品席窄复核件 `2026-11-11-SWB-SCRATCHCFG-产品席窄复核-v1.md` 桶内在场照登零读零碰）
- 被核物：`.scratch/tickets/2026-11-11-SWB-SCRATCHCFG-seat-config-lease-sync-ticket-v1.md` 修订笔 v1＝commit `1d9ba4d`（45增1删·原位 append·唯一被删行＝v1 末行无换行符归一＝正文零回改 ✓）
- 射程＝主理人命定三面闭集（自家红1黄1 落位闭合／修订笔自洽新扫／关键读数抽验复跑），禁扩面。

## 〇、开工实测（本席当轮现跑）

- `date` ＝ `Wed Nov 11 08:37:24 2026`
- `git rev-parse --short HEAD` ＝ `1d9ba4d`（＝修订笔本体＝现盘 HEAD·修订后 `git log 1d9ba4d..HEAD -- <票面>` 命中 0 ✓）
- tracked 脏面＝2 照登零碰零带入＝`M agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl`（他案脏面）＋`M agent-skills/fuxi-skill/products/pending/steve-jobs-perspective/registration.md`（FUXI 在飞 staged）——与修订笔开工读数所登两枚同面 ✓
- 锚 `1331bbc／c0f9e59／a23ccd2／1d9ba4d／282f88f／9278445` `git cat-file -e <sha>^{commit}` 六枚全在位 ✓

## 一、面1 · 自家 v1 快审红1黄1 落位闭合核

### 红-1（V3 判据自我矛盾两缺陷）→ R1 勘正 → **闭合**

- **缺陷①（reason 嵌原样 pattern 非剥离值）**：R1「机理勘正」句现读对拍守件源码＝write-guard L266 `f"...glob={g!r}..."` 嵌 deny_globs **原样字面**（本席 grep 实测 L266 行号与句式逐字全等）；R1 三条件式重写后本席按修订文本**照跑实跑一遍**（A 式·探针面全重定向 `.scratch/qa-cfgrev2/`·真 config 零碰·后跑＝票面围栏逐字提取 S1-a 生成 scratch 副本）：
  - 前跑（现盘 config）reason 解码＝`路径∈deny_globs（表2-1 明确不可写·seat=engineer glob='.collab/receipts/**' path=…）→ deny`
  - 后跑（S1-a 已替换副本）reason 解码＝同骨架·glob 段＝替换行逐字段在场
  - **条件① 骨架前缀逐字相等＝真；条件② 前跑 glob 段＝`.collab/receipts/**` 字面＋后跑 glob 段＝S1-a 逐字段＝真；条件③ 前后决策均 deny＝真；三条件全中＝V3 勘正版机械判据成立**（`.scratch/qa-cfgrev2/v3-pre.log`／`v3-post.log`／`v3-verdict.txt` 在册）。诚实申报：本席首跑 cond2 假负系自家比对口径含围栏外层双引号，修正口径（元素值比对）后为真——判据文本无歧义，系探针席操作差，不构成票面缺陷。
- **缺陷②（project_root 落回包根致全仓根 path 失判别力）**：R1 锚定环境注写死包根字面 A 式——本席现盘复核锚定环境＝仓根层级锚定声明件（.workbuddy 桶下 swb-anchor）与仓根层级 STRUCTURE 结构件两缺实测 ✓（包根 `agent-experts/baigong-software-team/docs/STRUCTURE.md` 在场≠仓根层级·`_structure_hit` 判 d≠包根故不命中·与 R1 陈述机理全等）；**反证跑**（照 v1 全仓根 path 直跑）＝reason 翻「路径∉当席租约」形态·deny_globs 分支不进（`v3-v1path-form.log` 在册）＝R1 所引「QA 实跑反证」读数现盘复现 ✓；A 式包根字面跑法本席复跑恰复现票钉 glob 字面 ✓。

### 黄-1（本票租约段 tickets 桶 glob 必 REJECT 不自洽）→ R2 撤除 → **闭合**

- lease-issuer 复跑（`--leases` 重定向 scratch·真 leases.jsonl 零碰·行数 7 前后未动）：
  - `--path-glob ".scratch/tickets/2026-11-11-SWB-SCRATCHCFG-*"` → **exit 2 REJECT**「请求路径越出席位 engineer 写域行」（`r2-ticketsglob.log`）＝与 R2 陈述读数全等；
  - `--path-glob "agent-experts/baigong-software-team/config/**"` 单项 → **exit 0 可签发**（`r2-configglob.log`）＝与 R2「PM 席实证」读数全等。
- 子集校验语义对拍＝`g == d or g.startswith(d.rstrip("/")) or d in g`（实读 lease-issuer 循环体）＝R2「相等／前缀／子串三式非 glob」陈述 ✓；engineer `write_globs` 九行现读（json）＝无 tickets 桶行 ✓。
- 撤除后与 §S3 不再自打架：S3 揭 SCRATCHG「请求面不在写域＝必 REJECT」，自家租约段现只留可签发单项＝同构自洽 ✓。「甲裁亦不解此项」＝甲加 `.collab/receipts/` 行非 `.scratch` 行 ✓ 逻辑全等（R5 注② 随动 ✓）。

## 二、面2 · 修订笔自洽新扫

- **V3 三条件式 ↔ S 目/围栏互洽**：条件② 后跑 glob 段真源＝§四 S1-a 围栏（本席即从围栏逐字提取跑判据＝可照跑性实证）；R4 作废 v1「同 reason 逐字全等」句＋效力声明「冲突处以修订节为唯一依据」＝v1 正文 V3 旧句残留被覆盖而非打架 ✓。
- **租约段 ↔ §S3**：见上·闭合互洽。
- **候裁甲乙丙 ↔ 机效读数**：乙款＝后续写入拦（本席前跑 deny 复现）＋补签 REJECT（黄-1 探针同路 exit 2 复现）✓；甲款＝让出父桶＋写域加行→经租约整桶可达＝机理直读 decide() 租约分支 ✓；丙款＝守件扩展另案 ✓——三款陈述与 v1 快审 §四机效呈述全等无漂移 ✓。R5 注①（甲伴 C1 级转录成本）＝呈拍材料注·候裁留白零动 ✓。
- **R3 缺号**：R1 段内「锚定环境注（R3 并入·PM 黄-1）」＝R3 归并入 R1·非缺漏 ✓。
- **观察承接段**：run-gates 内无 s4/test_enforcement＝本席 `grep -c "s4\|test_enforcement" share/run-gates.sh` 实测 **0** ✓ 承接读数复现。
- **黄-1（新扫·措辞级·非修订笔引入·R1 新注使其显性化）· §六租约段 config glob 字面与权限字面锚定形态不一**：R1 现盘钉＝「project_root() 落回包根、权限字面读作包根字面」；而租约段（v1 遗留·R2 保留）config glob 字面＝`agent-experts/baigong-software-team/config/**` 全仓根式，与所引写域行字面 `config/**`（包根式·现读在册）形态不一。本席探针实证：按该 glob 实签租约喂 write-guard——现盘态（无锚·根＝包根）对 `agent-experts/baigong-software-team/config/seat-permissions.json` **不命中**（reason＝「路径∉当席租约」deny·`lease-consumption-fullroot.log`）；显式 `SWB_REPO_ROOT` 锚定仓根则**命中**（ALLOW·`lease-consumption-reporoot.log`）。即＝签发兑现的租约在现盘惯态消费面空转。不定红理据：惯态 hooksPath 未装（票 §二 自陈在册）＝消费面拦截本不发生；部署态（项目根锚定在位）全仓根式恰为正确锚；不摇任何 V 判据实跑结论。修向建议（随回执/呈裁材料一行可销）：租约段 glob 改 `config/**` 包根字面（本席旁证：`g == d` 恰等亦过子集校验·现盘消费面命中），或注明「本 glob 按仓根锚定态书写」。
- **观察-1（措辞注·不须动）· R1 B 式跑法无 deny 分支判别力**：B 式（SWB_REPO_ROOT 锚仓根＋--path 全仓根式）本席随登实跑＝前后两跑 reason 均「路径∉当席租约」形态·glob 段缺席·两跑全等（`b-b-pre.log`／`b-b-post.log`）——即 B 式复现的恰是锚定环境注所诊「前跑失判别力」同象（锚不改 deny 行字面故分支仍不进）。票面仅称 B 式「随登另册」未称其承载判据＝不构成虚假陈述；V3 判据跑法唯 A 式三条件式·施工/QA 验收轮勿误取 B 式。

## 三、面3 · 关键读数抽验复跑表

| 项 | 票钉 | 本席现跑 | 判定 |
|---|---|---|---|
| BLOCK 计数钉 | 22833 | `python share/check-pointers.py 2>/dev/null \| grep -c BLOCK` ＝**22833** 逐字全等（`block-count.log`） | ✓ |
| leases 钉 | 0 / 7 行 | `grep -ci scratchg` ＝**0**·`wc -l` ＝**7**（探针前后均未动） | ✓ |
| V1 前值 | 0/0 | 两 config `grep -c "B-i 迁件目标单点除外"` ＝**0/0**（未施工态确认） | ✓ |
| s4 基线 | exit 0·13 PASS·t13 在场 | 直跑 exit **0**·PASS **13**·t13 ＝**1**（`s4-run.log`） | ✓ |
| V3 勘正版照跑性 | 三条件式 A 式 | 实跑三条件全中（§一 详录·含 JSON 解码 reason 口径说明） | ✓ |
| R2 lease-issuer 两跑 | exit2／exit0 | 复跑全等（§一 详录） | ✓ |
| 修订笔纪律面 | 恰一件·append-only | `git show --name-only 1d9ba4d` 恰票面一件·diff 纯 append（末行 NL 归一注记） | ✓ |

## 四、总裁决

**红 0／黄 1／绿多枚（红1黄1 落位闭合×2·V3 勘正版三条件实跑全中·钉值 22833／leases 0/7／s4 13PASS／V1 前值 0/0 全复现·R2 复跑全等·候裁三款陈述全等·append-only 恰一件）——放行。**

黄-1（租约段 config glob 字面锚定形态不一）＝措辞／登记级·惯态钩子未装下无实害·修向一行随回执材料或呈拍注可销·不另起修订轮；观察-1 随施工/QA 验收轮跑位注意。v1 快审「窄修后可径放免复审轮」承诺兑现确认：R1/R2 勘正面全部闭合。

## 五、纪律自证

- 只读零改：除本判定件外零改动；探针全程 `--map` 指现盘或 scratch 副本、`--ledger/--leases/--freeze-state` 重定向 `.scratch/qa-cfgrev2/`——真两 config／守件／tests／leases.jsonl／ledger.jsonl 零碰（leases 行数 7 前后全等）。
- 临时工作物＝仓根 `.scratch/qa-cfgrev2/`（identity／v3-pre／v3-post／v3-verdict／v3-v1path-form／b-pre／b-post／r2-两 log／lease-consumption 两件／s4-run／block-count／probe-ledger／probe-leases 族／replica-hooks-map）**如实登记不删**（主理人命定口径＝用完登记在册·与快审轮自删口径差异随命定）。
- 诚实申报：V3 首判 cond2 假负＝本席探针比对口径差（围栏外层引号），修正后复跑为真·过程读数两版均在册未掩。
- 他案在飞面（ledger 脏面、steve-jobs staged 枚、仓根杂物、FX-U39 链笔群、产品席窄复核件）照登零碰零带入；fresh eyes＝产品席窄复核产出未读。
- commit＝`collab:` 前缀·pathspec add/commit 两端齐带·FX_COMMIT_DECLARE 声明本笔面·紧邻无窗口·message 零 at 符号字符用字样·禁 add -A/amend/--no-verify·输出重定向 `.scratch/qa-cfgrev2/` 落盘·timeout ≥7 分钟·撞锁有界等待零删锁·落笔前靶检 `--target 本件` exit 0·完工 `git show --name-only HEAD` 恰一件自证。
