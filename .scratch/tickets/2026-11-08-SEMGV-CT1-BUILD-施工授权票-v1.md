# TK-SEMGV-CT1-BUILD · 施工授权票：契约整改七件面＋校验器＋夹具随动（v1）

- 票 ID＝`TK-SEMGV-CT1-BUILD`。票型＝施工授权票（非设计票、非分票、非部署票；同 T1-BUILD `b9169c6`／T2-BUILD `5f32548` 先例，授权票非分票）。
- 开票席＝主理人；落笔时点 2026-11-08 11:4x–12:0x +0800；落笔前实测 HEAD＝`56ee808`；他案未跟踪在制品照登不碰。
- 批准载体＝呈放行件 `.collab/decisions/2026-11-08-呈皮总-SEMGV-CT1契约整改审面收口呈放行.md`（`c0aa7bc`）选项 A＋皮总原话「放行。」；放行登记＝`.collab/decisions/2026-11-08-主理人登记-皮总批准SEMGV-CT1放行.md`（`56ee808`）。
- **规格唯一真源**＝`.scratch/tickets/2026-11-08-SEMGV-CT1-契约整改规格票-v3.md`（commit `e3935e7`，293 行／47,236 字节／sha256 `d9cf2dc2b754189ed5d4fb5b5f945271371514604263e147cc726df6c79979c5`；主理人已独立复算＝blob 与该 sha 全等）。工程师读规格以 `e3935e7` 的 blob 为准（`git cat-file blob "e3935e7:.scratch/tickets/2026-11-08-SEMGV-CT1-契约整改规格票-v3.md"`），不以工作区快照为准。v3 未覆盖处＝停手上报，不得自行扩规格。
- 本票不复制契约条款正文；一切修法全文（M-1~M-7 逐字照落文本）与校验器施工规格（S-1~S-5）只在 v3 §1／§2 内。

## 〇、开工前置（不符即停手上报，不自行纠偏）

1. 开工第一步实跑 `date`、`git rev-parse --short HEAD`、`git status --porcelain --untracked-files=no`，三读数写入回执开端；HEAD 应 ≥ `56ee808`（并发线可能前移，如实登记差值，不 rebase、不等待）。
2. 实跑 `git cat-file -e e3935e7^{commit}` ＋ v3 票面 sha256 复算＝`d9cf2dc2…979c5`，确认规格真源逐字节在位。
3. 复核被改对象现态基线（主理人开票前实测誊录，工程师开工复算核对）：
   - T1 七件：`git diff 9e04dc0..HEAD -- agent-skills/claim-commitment-governance/` **空输出**；行数实测 92／217／50／98／43／44／33＝577；
   - 校验器：`agent-experts/baigong-software-team/skills/sop/scripts/semantic-governance.py`＝1,618 行／81,550 字节／sha256 `77286b33d39ca7bf9b28d6b4918846ea84cbecd19f6d6eb4985b5f40d7d1e453`；
   - 闭集配置：`agent-experts/baigong-software-team/config/semantic-closed-sets.json`＝49,446 字节／sha256 `d09156ab8bf30dc1c9b963d88d4da1475beed563641edb56581f3921ed5ab0bb`；
   - T1 验收夹具：`.scratch/tickets/2026-11-07-SEMGOV-T1-BUILD-verify.py`＝2,097 行／sha256 `25fc83b451c12522f58872abbc37d1a39038b5646dc01ebfa12d835444ef508d`。
   任一不符＝停手上报。

## 一、写集闭集（超集即停手上报）

### W1 · 契约七件中的四件（交付面·按 v3 §1 M-1~M-7 逐字照落）

| # | 目标文件（绝对路径前缀 `D:\multi-agent-collab-devkits\agent-skills\claim-commitment-governance\`） | 现态行数 | 预算改后（v3 §3） | 牵动修法 |
|---|---|---|---|---|
| 1 | `references\10-contract.md` | 217 | 225（＋8） | M-2 修法1/2、M-3 修法2、M-4 修法1/2、M-6、M-7 |
| 2 | `references\20-artifact-mapping.md` | 50 | 52（＋2） | M-1 修法1/2 |
| 3 | `references\30-gates.md` | 98 | 100（＋2） | M-2 修法3、M-3 修法1、M-4 修法3（§4 标题行＋A3／A4 两行）、M-5 修法1/2/3 |
| 4 | `templates\claim-register.md` | 44 | 45（＋1） | M-1 修法4（填写说明第 11 条逐字全文） |

- **替换句给整句、增段给整段**——一律逐字照 v3「修法全文」围栏，禁改写、禁补句、禁顺手润色。行号＝v3 标注的现态行号（`sed -n` 复现定位），落笔前逐处回原文核对定位；定位与 v3 病灶引文不符＝停手上报。
- 行数预算为钉值参考：落盘实测与预算差值**如实登记**（v3 §3 明示工程师以实测定值），不强行凑数、不改规格。
- **三件零触**：`SKILL.md`、`references\40-provenance-map.md`、`templates\outbound-artifact.md` 及一切表结构列数（表 A 20／B 9／C 7／D 13）＝验收判据 2 实证零改动。
- 表结构列数七件全零变化、守恒式七桶构成不变（v3 票头纪律行）。

### W2 · 校验器两件（按 v3 §2 S-1/S-2/S-3/S-4）

| # | 目标文件（绝对路径前缀 `D:\multi-agent-collab-devkits\agent-experts\baigong-software-team\`） | 规格 |
|---|---|---|
| 5 | `skills\sop\scripts\semantic-governance.py` | S-1（R2 降级形态支·触发条件精确限定·「无冒号」「kind 未知」两支不得被吞）＋S-2（R4③ 同值支＋作用域提层至全部 `required_change_record ≠ none` 行）＋S-3（R13 第五支单列区对账·**仅 reconcile 接入**·不含交付汇总时跳过不静默·取数＝标题行后逐条正则取 `claim_id` 计数） |
| 6 | `config\semantic-closed-sets.json` | S-4：全路径＝专家包根 `config/`（`skills/sop/config/` 不存在）；闭集逐字派生源随 W1 改动重算（R2／R4／R13 判据句、§11 各行、`:83` 单元格、交付汇总必填面、§4 标题行 A1–A4、A3／A4 两新行）；件数与 key 结构不变 |

### W3 · T1 验收夹具随动（过程域·按 v3 §2 S-5）

| # | 目标文件 | 规格 |
|---|---|---|
| 7 | `D:\multi-agent-collab-devkits\.scratch\tickets\2026-11-07-SEMGOV-T1-BUILD-verify.py` | S-5：七件正文改动牵动其**摘要类期望**——R2／R4／R13 判据行摘要、§11 表、`c13`／`c14`／`c26` 族、**`c07`**（`EXPECT_D_FORMAT['required_change_record']` 含 `:83` 旧句整串 exact 面）、**`c23` 承接行族**（`EXPECT_TARGETS` 现含 `T-A1`／`T-A2`，A3／A4 入表后随动重算）。按改后正文重算摘要期望后复跑 `--all`／`--mutate`／`--selfcheck`／`--stats` 全绿（红4-03「摘要常量随动」同源教训：改正文不重算摘要＝错值复活）。**只准动期望常量，禁改夹具判定逻辑** |

### W4 · 工程师回执

- `D:\multi-agent-collab-devkits\.scratch\tickets\2026-11-08-SEMGV-CT1-BUILD-回执-v1.md`，单独一笔 commit。
- 落点＝`.scratch/tickets/` 过程域（同 T1/T2-BUILD 先例）；门禁 `check-ticket-reconcile.py` 前缀假设 WATCH 已在册、advisory、不阻断（归 T6），不得为规避改落点或改门禁。

### 租约写域实证（主理人已代跑·两态逐字实录）

呈放行件与 v3 S-5 要求 fixture／`*.py` 面租约随动。主理人开票前实跑 lease-issuer 两态如下（仓外临时台账、不入账）：

**态一（skills/config 面·签发成功）**：

```
$ python3 agent-experts/baigong-software-team/skills/sop/scripts/lease-issuer.py \
    --ticket SEMGV-CT1-BUILD-WDDEMO-1 --seat engineer \
    --countersign "architect:CT1-BUILD-WRITEDOMAIN-DEMO" \
    --path-glob "skills/**" --path-glob "config/**" \
    --leases <mktemp -d>/l1.jsonl
exit=0
{"ticket_id": "SEMGV-CT1-BUILD-WDDEMO-1", "path_globs": ["skills/**", "config/**"], "seat_id": "engineer", "hash": "6bff8c1283417ee9cb339e0f7b64df0a78224916be4c56ebfe48cb66e629a959"}
```

**态二（七件面＋fixture 面·被拒签发）**：

```
$ python3 …/lease-issuer.py --ticket SEMGV-CT1-BUILD-WDDEMO-2 --seat engineer \
    --countersign "architect:CT1-BUILD-WRITEDOMAIN-DEMO" \
    --path-glob "agent-skills/claim-commitment-governance/**" \
    --path-glob ".scratch/tickets/2026-11-07-SEMGOV-T1-BUILD-verify.py" \
    --leases <mktemp -d>/l2.jsonl
exit=2
REJECT: 请求路径 'agent-skills/claim-commitment-governance/**' 越出席位 engineer 写域行（表2-1 实例化源），拒签发
```

- **口径裁决（照 T1-BUILD `86d9963` 裁定 B 先例）**：本票真授权＝本票 §一 写集闭集；lease-issuer 只承载 skills/config 面写域实证。七件面／fixture 面在 engineer `write_globs` 行外（`seat-permissions.json` 实测＋态二实证），**无法经 lease-issuer 签发**——v3 S-5「另授新租约」按现态机件不可达，如实登记；该两面授权由本票票面闭集承载（与 T1-BUILD 七件＋fixture 落位同模式、T1 施工实证未被 write-guard 拦截）。countersign 钉值逐字 `architect:CT1-BUILD-WRITEDOMAIN-DEMO`＝**写域实证样例**（脚本只验前缀＋非空），非入账租约、非架构席实质签注。
- 工程师开工复跑态一同款命令（同 ticket/countersign/path-glob），核对 exit 0＋hash `6bff8c12…9a59` 可复算（canonical json 确定性），誊入回执；不符＝停手上报。`--leases` 必指仓外临时目录，禁写入仓内台账。

### 写集之外零写

除 W1 四件＋W2 两件＋W3 一件＋W4 回执外零写入（含临时脚本落仓内、缓存、日志）。一切抽取／复算／变异实跑在仓外临时目录进行，批毕清理，读数入回执。

## 二、禁动面（不放宽）

- **CT1 v1（`2c69805`）／v2（`5f103b4`）／v3（`e3935e7`）三版票面一字不动**；T1 v1–v5 票面与回执、T2 v1–v3 票面、T1/T2-BUILD 回执一字不动。
- 未触三件（`SKILL.md`／`40-provenance-map.md`／`outbound-artifact.md`）零改动（判据 2 实证）。
- `.collab\decisions\**`、`.collab\qa\**`、`agent-experts\baigong-software-team\.collab\**`、试填两件（`a56a192`）：零写（登记件由主理人落笔）。
- 三同源 `plugin.json`／`bundle.lock`／`.codebuddy-plugin\plugin.json`、除 `semantic-closed-sets.json` 外一切 `config\**`、`tests\**`、`docs\**`、`agent-skills\fuxi-skill\**`、他案在制品：零触。
- 禁 `git add -A`／`--amend`／`reset`／`--no-verify`。触碰任一面须另走票面，不得就地改。

## 三、验收判据（全部机械可跑·读数逐条入回执）

| # | 判据 | 命令口径 | 钉值 |
|---|---|---|---|
| 1 | 写集对账 | `git show --name-only --format="" <施工笔>` 与 W1–W3 七件声明闭集排序比对 | 全等＝恰 7 件；回执笔恰 1 件 |
| 2 | 三件零触＋列数零变化 | `git diff HEAD~1..HEAD --stat` 中零 SKILL.md／40-provenance-map／outbound-artifact；四改件 diff 中表头行列（`| claim_id |…` 等）零改动 | 零命中 |
| 3 | 改后行数 | `wc -l` 四改件 | 实测 225／52／100／45＝预算或如实登记差值；合计 590±Δ（Δ 登记） |
| 4 | M 修法逐字落位抽检 | 对四改件 grep：「无责任主体主张单列区」（20-artifact）、「单列区（≠桶）」段、「跨表同值回指」段、「无论本行 `original_requirement_ref` 是否为 `none`」（30-gates R4③ 扩展）、「编号两分发放」两段、「A3｜」「A4｜」两新行＋§4 标题行「A1–A4」、「`req_*` 三列取值规则」段、「例外一支」段、「填写说明 11.」条 | 逐条恰命中（措辞以 v3 围栏为判据） |
| 5 | 校验器 selfcheck | `python3 …/semantic-governance.py selfcheck`（子命令形态） | 34 比对项全过＋`SELFPROOF mutations_total=4 red=4` exit 0（现成口径承 S-4） |
| 6 | S-1 降级支正反 | 仓外构造：自由文本 `source:`＋`authority=unverified` → 绿；＋`authority=binding` → R2 红（value 标 `free-desc`） | 正绿反红；「无冒号」「kind 未知」两支回归不红被吞（构造样本各验） |
| 7 | S-2 同值支＋作用域 | 样本：`@human:A` vs 表 A `approver=human:B` → 红；`ref=none` 行＋表 A `approver=none`＋记录非 none → 红（**修前双 exit 0 的 H2 缺口必转红**）；`@seat:X` → 红 | 三红全中 |
| 8 | S-3 ⑤支 | reconcile 含交付汇总：单列区条数≠表 A 命中数 → 红；缺三元素 → 红；validate 单件喂交付汇总 → **不判⑤**（零红）；reconcile 不含交付汇总 → 跳过且判定面可见（不静默） | 四态全中 |
| 9 | 夹具四类读数 | 对改后真文件跑 `--all`／`--mutate`／`--selfcheck`／`--stats` | 全绿；四类读数登记（`c07`／`c23` 族已随动重算——若未重算必炸，炸＝未随动证据） |
| 10 | 配置↔真源逐字全等 | selfcheck 同源比对（V6 口径）＋抽 3 处改句（R2 句／§4 标题 A1–A4／A3 行）核对 json 派生段 | 全等 |
| 11 | 真源未触 | `git diff 56ee808..<收口HEAD> -- <CT1 v1/v2/v3 三票面> <T2 v3> <试填两件>` | 空输出 |
| 12 | 收口洁净 | `git status --porcelain --untracked-files=no` | 空（他案未跟踪面照登） |

判据 5–10 读数须为本票改后真文件上重跑所得，禁照抄历史读数；与钉值不符＝如实登记实际读数并停手上报，**禁改规格、禁改夹具判定逻辑以求绿**。

## 四、提交与回执形态

1. 施工笔：`git add` 仅 W1 四件＋W2 两件＋W3 一件（显式逐路径，禁 `-A`），单笔 `collab:` 前缀 commit；回执笔另起一笔，只 add W4 一件。两笔各自落账后才算收束（三态逐条写）。
2. 回执必含：①开工三读数；②租约态一复跑读数＋hash 核对；③两笔 commit sha；④判据 1–12 逐条实测读数（命令＋输出要点）；⑤**完整写入／修改文件清单**（对账口径＝`git show --name-only` 与清单全等）；⑥行数实测 vs 预算差值登记；⑦仓外临时目录清理读数；⑧`git status` 读数。
3. 回执中禁全称断言；零命中表述须写清检索范围、命令与实测读数（R5-01 教训）。

## 五、收口即停

本票射程仅到「四件＋两件＋夹具随动落成并回执落账」。**不得**自行进入 QA 独立验、复跑试填、T3–T6、升号、装配、部署。收口后回报主理人，由主理人派 QA fresh eyes 独立验＋产品席同拆仓澄清件复跑试填兜底（四硬伤消失＝整改生效实据）。

## 六、异常停止条件（任一命中即停手上报）

- 规格真源 `e3935e7` 不可解析或 sha256 不等；
- 开工基线（§〇.3 四组 sha/行数）任一不符；
- v3 病灶行号定位与现文件引文不符；
- 任一验收判据与钉值不符且非行数差可登记项；
- 并发线在写集内产生改动（如实登记区间读数，不自行合并）；
- 需要写入写集闭集之外的任何文件。
