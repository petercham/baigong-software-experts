# SWB-SCRATCHCFG · rev 笔（1d9ba4d）产品席窄复核 v1

- 复核席：产品席 `pm-cfgrev`（自家快审判词 `c0f9e59` 承诺「微型 rev 后可径放」之放行路径兑现轮；fresh eyes＝未读起草席工作过程、未读 QA 席快审判词正文本体——仅核其在链 `1331bbc`＋rev 件内引文，只读链上件＋rev 后票面）
- 被核物：`.scratch/tickets/2026-11-11-SWB-SCRATCHCFG-seat-config-lease-sync-ticket-v1.md` 修订笔 v1 段（L134–L173·原位 append·落链 `1d9ba4d` 恰一件 name-only 实测）
- 窄口径闭集＝R1–R5 核销＋黄-2 留观登记＋差量新扫，不重开全案、方案本体零动。

## 〇、开工实测读数（本席当轮现跑）

- `date`＝`Wed Nov 11 08:14:54 2026`／`git rev-parse --short HEAD`＝`1d9ba4d`（＝rev 笔本体）
- `git show --name-only 1d9ba4d`＝恰票面一件 ✓；`git diff a23ccd2..1d9ba4d -- <票面>`＝45 增 1 删（删行＝v1 末行无尾换行同款改写＝append-only 属实，v1 正文行零回改）✓
- `git status --porcelain --untracked-files=no`＝`M agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl`＋`M agent-skills/fuxi-skill/products/pending/steve-jobs-perspective/registration.md` 两枚他案在飞面照登零碰零带入
- 锚在位：`1331bbc`（QA 判词笔）`git cat-file -e` 实测在位 ✓
- rev 票面靶检复点：`python share/check-pointers.py --target .scratch/tickets/2026-11-11-SWB-SCRATCHCFG-seat-config-lease-sync-ticket-v1.md` → **exit 0** ✓

## 一、逐项核销表（R1–R5＋留观）

| 项 | 勘正声称 | 本席独立复跑/对读 | 判定 |
|---|---|---|---|
| **R1**（自家红-1 闭合） | V3 重写三条件式：①reason 骨架前缀逐字相等②glob 段前后取值写死③前后均 deny；机理句「L266 `glob={g!r}` 嵌原样 pattern 字面非剥离后值」 | 探针两跑现证：前跑 reason＝`路径∈deny_globs（表2-1 明确不可写·seat=engineer glob='.collab/receipts/**' path=…）→ deny`、后跑（S1 替换行副本 `--map`）＝同骨架＋glob 段逐字＝替换行全字面——三条件按 A 式全中、骨架前缀逐字相等恰与 R1 写死式一致；L266 现文对读属实 | **闭合** |
| **R3**（并入 R1·自家黄-1） | `--map` 全径写死＋锚定环境注（无 swb-anchor／仓根无 STRUCTURE→project_root 落回包根；A 式主用／B 式随登）＋QA 第二失判臂（全仓根路径直跑则 deny 分支不进 reason 翻形态）随登 | 现盘实测两缺属实（`.workbuddy/swb-anchor` 缺席、仓根 docs 层 STRUCTURE 结构件缺席——包根同名件被 `_structure_hit` d≠包根条款挡回＝落回包根 ④ 与注记一致）；本席自家首轮全径 `--path` 直跑恰复现「路径∉当席租约」翻形态＝失判臂实证；`--map` 全径两跑写死后可复现（本席即按此跑通） | **闭合** |
| **R2**（自家红-2 闭合） | 租约段撤 tickets 桶 glob、只留 `agent-experts/baigong-software-team/config/**` 单项；票附回执不落租约面随 SCRATCHG 先例体例成文；「甲裁亦不解此项」入呈拍注 | lease-issuer 实跑（countersign 注·leases 重定向临时区）：勘正后单项请求面 **exit 0 签发 OK**（四字段入账）＝死锁解除实证；回执不落租约面＝与 SCRATCHG leases scratchg 0 先例体例同型；甲加 receipts 行授权不解 .scratch 桶项＝语义对盘 | **闭合** |
| **R4**（表述随动） | 「同 reason 字符串逐字全等」句作废、以 R1 三条件式为准；零机效变化本体结论维持 | 随动落位在文；本体结论两席探针＋副本臂 s4 全批 13 PASS 旁证在自家快审在册，rev 未动替换文本本体（S1 三段逐字未回改＝diff 45 增全在修订段） | **闭合** |
| **R5**（自家黄-3） | 呈拍材料注①甲款 C1 级转录成本②甲不解 R2 项③表态归集（产品席乙＋起草席乙＋QA 不代裁机效陈述） | 三注齐在、候裁三款框架与留白零动（§七正文 diff 零触碰＝diff 面实证）；自家乙表态引文对快审原判无改写 | **闭合** |
| **黄-2 留观** | 「部署态 tickets 桶系统性不可写＝既有惯例部署态债归治理面另账＝PM Y-2 照登不入本案」 | 留观登记在文（R2 段内），不入 rev 处置面——恰按分工落位 | **登记属实** |
| 观察承接（QA 观察-1） | 禁拆两笔判据保留＋措辞注＝run-gates 内无 s4（grep 零命中）＝V2 人工跑位承载非门禁自动拦 | 本席 `grep -c "s4\|test_enforcement" share/run-gates.sh` ＝ **0** 复点同值；「V2 人工承载」措辞与 t13 机理对盘 | **属实** |

## 二、差量新扫（rev 段内）

- 效力声明段「以本节为唯一依据」＝ES2/CD1/TMP-DISC 先例体例同款；开工读数两枚他案照登与现盘全等；修订笔自证段口径与纪律一致。
- 新扫零新红零新黄：R1 A/B 两式皆机械可跑（本席 A 式跑通）；R2 勘正后可签发（本席跑通）；rev 未引入新引用悬空（票面靶检 exit 0 复点）；S1 替换文本／S2／声明闭集三件／禁动面六列零动（diff 45 行全居修订段）。
- 体例注（非缺陷）：主理人续单所指 `agent-skills/.collab/qa/` 桶实测不存在；本案两件前判词俱落仓根 `.collab/qa/`＝本件随本案体例落仓根桶（开单任务书原径亦此）。

## 三、结论

**放行**（红 0／黄 0／绿 7＝R1／R2／R3／R4／R5／黄-2 留观登记／观察承接复点）。自家 v1 红二黄三全部闭合，R1–R5 全措辞／列面勘正级兑现、方案本体与候裁框架零动属实——CFG 线产品席侧归集就绪，与 QA 席「窄修后可径放免复审轮」表态合流；§七候裁（甲乙丙取态）归裁面不受本复核影响，本席乙表态已在 R5 注③在册。

## 四、纪律自证

- 只读复核：除本判词外零改动；他案在飞面（ledger 脏面／registration staged 枚／arch-a14tk2 在飞／FUXI 链笔群）照登零碰零带入。
- 探针落临时区 `.scratch/pm-cfgrev/`（payload／patched-map 副本／probe-ledger／probe-leases 族），完工自删附读数（commit 日志留档随登）。
- 落笔前靶检 `python share/check-pointers.py --target .collab/qa/2026-11-11-SWB-SCRATCHCFG-产品席窄复核-v1.md` exit 0（读数随回票）；commit＝collab: 前缀·pathspec 两端齐带·FX_COMMIT_DECLARE＝纯路径清单·紧邻无窗口·message 零 at 符号字符·禁 add -A/amend/--no-verify·输出重定向 `.scratch/` 落盘·超时给足·撞锁有界等待 30s×10 零删锁·完工 `git show --name-only HEAD` 恰一件自证。
