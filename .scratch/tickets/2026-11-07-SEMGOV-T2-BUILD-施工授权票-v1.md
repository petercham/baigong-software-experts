# TK-SEMGOV-T2-BUILD · 施工授权票：校验器脚本＋闭集配置落地（v1）

- 票 ID＝`TK-SEMGOV-T2-BUILD`。票型＝施工授权票（非设计票、非分票、非部署票；同 T1-BUILD 先例 `b9169c6`，授权票非分票）。
- 开票席＝主理人；落笔时点 2026-11-07 23:5x +0800；落笔前实测 HEAD＝`e84d6cc`；他案未跟踪/暂存在制品照登不碰。
- 批准载体＝`.collab/decisions/2026-11-07-呈皮总-SEMGOV-T2规格票审面收口呈放行.md`（`831a484`）选项 A＋皮总原话「批准放行」；放行登记＝`.collab/decisions/2026-11-07-主理人登记-皮总批准SEMGOV-T2放行.md`（`e84d6cc`）。
- **规格唯一真源**＝`.scratch/tickets/2026-11-07-SEMGOV-T2-校验器与夹具规格票-v3.md`（commit `8388470`，357 行／46,367 字节／sha256 `a1546625eb9a0880f2b57108101cb3874295390a6185c1d9072c675e3146d480`；主理人已独立复算＝工作区 blob 与该 sha 全等）。工程师读规格以 `8388470` 的 blob 为准（`git cat-file blob "8388470:.scratch/tickets/2026-11-07-SEMGOV-T2-校验器与夹具规格票-v3.md"`），不以工作区快照为准。v3 未覆盖处＝停手上报，不得自行扩规格。
- 本票不复制契约条款正文；一切判据／闭集／元规则正文只在 v3 §1 与 T1 七件真源内。

## 〇、开工前置（不符即停手上报，不自行纠偏）

1. 开工第一步实跑 `date`、`git rev-parse --short HEAD`、`git status --porcelain --untracked-files=no`，三读数写入回执开端；HEAD 应 ≥ `e84d6cc`（并发线可能前移，如实登记差值，不 rebase、不等待）。
2. 实跑 `git cat-file -e 8388470^{commit}` ＋ v3 票面 sha256 复算＝`a1546625…d480`，确认规格真源逐字节在位。
3. 复核交付两件均不存在（实测已核：`agent-experts/baigong-software-team/skills/sop/scripts/semantic-governance.py` 与 `config/semantic-closed-sets.json` 均缺失＝零起稿）；若已存在任何一件＝停手上报，不得就地覆盖。
4. 复核 T1 七件基线：`git diff 9e04dc0..HEAD -- agent-skills/claim-commitment-governance/` 空输出（V1 基线钉值 O-3）；非空＝停手上报。

## 一、写集闭集（超集即停手上报）

### W1 · 交付两件（交付面）

| # | 目标文件（含盘符完整路径） | 规格 |
|---|---|---|
| 1 | `D:\multi-agent-collab-devkits\agent-experts\baigong-software-team\skills\sop\scripts\semantic-governance.py` | v3 §1.2(1)：三子命令逐字照 `30-gates.md` §3 契约表；判据归属 6/6/5；人工闸消费点 2/1/1；N1–N8/N10 元规则；不可机检项零实现；不消费版本号 |
| 2 | `D:\multi-agent-collab-devkits\agent-experts\baigong-software-team\config\semantic-closed-sets.json` | v3 §1.2(2)：14 组闭集逐项标注真源节号，逐字派生 |

**config 层级钉值（v3 §0.4 授权施工票钉死——主理人开工实测依据）**：`skills/sop/config/` 不存在；专家包根 `agent-experts/baigong-software-team/config/` 存在且现有 6 件 json（`dispatch-spec.json`／`seat-permissions.json` 等）；既有 scripts 一律经包根 `config/` 消费（`lease-issuer.py` 缺省 `--config`＝`pack_root()/config/seat-permissions.json`）。⇒ **本票钉死第 2 件落位＝专家包根 `config/`**（与 v3 §1.1 声明闭集路径一致、与既有一切 config 消费形态同源）；**不新建 `skills/sop/config/` 目录**。`sop/SKILL.md` 行 27 scripts 索引随动属 T3，本票零触。

**夹具承载钉值**：v3 §1.1 交付闭集恰 **2 件**＋「不自造第三件文件名」与 §1.1 夹具「独立数据文件」形态存在张力，本票钉死＝**夹具一律内嵌 `semantic-governance.py`**（负样本、变异源、同源自证机制全部内嵌；或以数据节形态落 `semantic-closed-sets.json` 内部）。**独立第三文件＝越界**；如实现上确需第三文件，停手上报候裁。夹具不得落 `tests/**`（禁动面）。

### W2 · 工程师回执

- `D:\multi-agent-collab-devkits\.scratch\tickets\2026-11-07-SEMGOV-T2-BUILD-回执-v1.md`，单独一笔 commit。
- 落点＝`.scratch/tickets/` 过程域（同 T1-BUILD W3 先例）；门禁 `check-ticket-reconcile.py` 的 `.collab/` 前缀假设可能再报 WATCH——已在册、advisory、不阻断（归 T6），不得为规避改落点或改门禁。

### 租约写域实证（主理人已代跑·读数誊录如下）

呈放行件 §四要点＝「`lease-issuer.py` 对该写域可正常签发租约」。本票真授权＝本票面写集闭集（同 T1-BUILD `86d9963` 裁定 B 先例）；lease-issuer 侧只需**写域可签发实证**。主理人开票前已实跑成功（仓外临时台账、不入账），命令与输出逐字誊录：

```
$ python3 agent-experts/baigong-software-team/skills/sop/scripts/lease-issuer.py \
    --ticket SEMGOV-T2-BUILD-WDDEMO --seat engineer \
    --countersign architect:T2-BUILD-WRITEDOMAIN-DEMO \
    --path-glob "skills/**" --path-glob "config/**" \
    --leases <mktemp -d>/leases-t2-demo.jsonl
exit=0
{"ts": "2026-11-07T15:58:06Z", "lease": {"ticket_id": "SEMGOV-T2-BUILD-WDDEMO", "path_globs": ["skills/**", "config/**"], "seat_id": "engineer", "hash": "20fc6d73af468f8249bd75af50dba32ae56855a146a10879221e324ab062dc2c"}, "countersign": "architect:T2-BUILD-WRITEDOMAIN-DEMO", "instantiated_from": "config/seat-permissions.json"}
```

- **口径实证（开票过程实录）**：首跑以具体文件路径喂 `--path-glob`（`skills/sop/scripts/semantic-governance.py`）被零裁量子集校验拒签发（exit 2）；改按席位写域**行**粒度（`skills/**`、`config/**`，与既有 TK-SRC4Z 租约同款形态）签发成功。⇒ 本票租约实证一律按写域行粒度喂；写集闭集细粒度授权仍由本票 §一 W1 承载。
- countersign 钉值逐字 `architect:T2-BUILD-WRITEDOMAIN-DEMO`，性质＝**写域实证样例**（脚本只验 `architect:` 前缀＋非空），**非入账租约、非架构席实质签注**——架构席实质签注权（§7）不受此样例影响，如实声明。
- `--leases` 必指仓外临时目录——仓内 `.collab/ledger/**` 在工程师 deny 面，禁写入仓内台账。
- 工程师开工复跑同款命令（同 ticket/countersign/path-glob 钉值），核对 exit 0＋四字段＋hash `20fc6d73…dc2c` 可复算（canonical json 确定性），誊入回执；不符＝停手上报。

### 写集之外零写

除 W1 两件＋W2 回执一件外零写入（含临时脚本落仓内、缓存、日志）。一切抽取／复算／变异实跑在仓外临时目录进行，批毕清理，读数入回执。

## 二、禁动面（v3 §1.5 全量，不放宽）

T1 v1–v5 五版票面与 v4/v5 回执、**T2 v1（`ce1591b`）／v2（`562ce71`）／v3（`8388470`）三版票面一字不动**、已落成七件与 T1 验收夹具（`9e04dc0` 基线）、`.collab/decisions/**`、`.collab/qa/**`、`agent-experts/baigong-software-team/.collab/**`、三同源 `plugin.json`／`bundle.lock`／`.codebuddy-plugin/plugin.json`、除 T2 两件外的 `config/**`、`tests/**`、`docs/**`、`agent-skills/fuxi-skill/**`、他案在制品。禁 `git add -A`／`--amend`／`reset`／`--no-verify`。触碰任一面须另走票面，不得就地改。

## 三、必载钉值（v3 授权由本票钉死项）

1. **OBS-2 非法 `--kind` 输出口径（裁定三十八）**：`validate --kind` 收到闭集外七值之外的取值时，stdout 必含一行逐字格式：
   `VIOLATION spec=KIND-CLOSED-SET field=kind value=<原输入值>`
   且退出码固定 **exit 2**。QA 独立验按本钉值机检（`grep -c '^VIOLATION spec=KIND-CLOSED-SET field=kind value='`＝1／输入合法值时＝0）。
2. **`--kind` 七值闭集**（v3 §1.2(1) Y-P3）＝逐字派生 `20-artifact-mapping.md` §1 行 9–15 表首列：`PRD`／`需求解析`／`工作票`／`回执／回流件`／`QA 判词`／`交付汇总`／`对外呈报／函件`。
3. **三子命令判据归属 6/6/5**（v3 §1.2(3)）：validate＝R1,R2,R5,R7,R14,R16；reconcile＝R3,R10,R11,R12,R13,R17；gate-outbound＝R4,R6,R8,R9,R15；并集恰 R1–R17、两两交集空；人工闸消费点 2/1/1（外发前→gate-outbound；降级/豁免＋外部权威与法律合同解释→validate；沉默效力→reconcile）。实现内该划分须可静态指认（注释表或映射表逐字）。
4. **同源纪律（v3 §1.2(2) 末段＋V6）**：14 组闭集逐字派生自四真源；提供可机检「配置↔真源逐字全等／规范化摘要全等」自证入口（内嵌实现）；**等长反义改写、值漂移、常量改义、列序互换四类变异全数造红**，干净副本全绿（防橡皮图章）。
5. **元规则（不得放宽）**：每条负样本只让其**声明的那一支判据**变红，别的判据顺带命中＝假阴不算通过；N9／A2／`contractual` 人工确认项**零机检实现**。
6. **V8 射程切割**：版本号字面命中 0 的扫描对象＝脚本代码与调用面文本，排除 `semantic-closed-sets.json` 组 14 值本体（含 `0.1.30`／`version: 1.0.2` 字面，系真源逐字派生）。

## 四、验收判据（全部机械可跑·读数逐条入回执·对应 v3 V1–V11）

| # | 判据（对应 v3 V 号） | 命令口径 | 钉值 |
|---|---|---|---|
| 1 | V1 交付闭集 | `find agent-experts/baigong-software-team/skills/sop/scripts/semantic-governance.py agent-experts/baigong-software-team/config/semantic-closed-sets.json`；`git diff 9e04dc0..HEAD -- agent-skills/claim-commitment-governance/` | 两件在位；七件 diff 空 |
| 2 | V2 归属划分 | 从实现内映射表抽取三组 R 集 | 6/6/5、并集 R1–R17、两两交集空、人工闸 2/1/1 |
| 3 | V3 R 闭集强等 | 实现引用判据号全在 R1–R17 内、17 条全被消费恰一次 | 零增号／零改号／零重复 |
| 4 | V4 N 闭集＋元规则 | N1..N10 逐条＋「应咬判据·支」逐条可指认；元规则段在实现内整段可指认 | 10/10 |
| 5 | V5 负样本实跑 | 内嵌夹具逐条跑 | N1–N8、N10 各其声明支红且 `exit≠0`；N9/A2 机检实现数 0 |
| 6 | V6 同源自证 | 自证入口实跑＋四类变异实跑 | 14 组全等；四类变异全红；干净副本全绿 |
| 7 | V7a 三子命令实跑 | 对 T2 两件＋夹具样本＋`templates/` 示例行可映射 kind 者喂三子命令；**T1 七件本体只走 V6 自证面、不作 `--kind` 输入**（N-1） | exit 与「违例字段＋判据号」符合 §1.2(1)；七值逐值可跑；闭集外值按本票钉值 1 红 |
| 8 | V8 不消费版本号 | 脚本代码＋调用面文本扫版本号字面（排除 config 组 14 值本体） | 命中 0 |
| 9 | V9 交付面洁净 | 两件全文扫 `.collab/`、`.scratch/`、票名、盘符路径；扫 `verify.py` 引用 | 全 0 命中（写清检索范围＋命令＋读数） |
| 10 | V10 禁动面 | `git show --name-only <施工笔>` 与 W1＋租约读数对账；`git diff --name-only` 对禁动面 | 恰 2 件；禁动面空 |
| 11 | V11 不越界 | 零新增 R、零改七件、零 A1/A2/N9 机检、零人工闸代判（回执自陈＋主理人抽验） | 成立 |

判据 5–8 读数须为**本票真文件实跑所得**，禁照抄任何历史读数；与钉值不符＝如实登记实际读数并停手上报，**禁改判据口径以求绿**。

## 五、提交与回执形态

1. **施工笔**：`git add -- <W1 两件>` ＋ `git commit -m "eng: …" -- <W1 两件>`（**add/commit 双侧 pathspec**，裁定四十句式）；单笔落账。
2. **回执笔**：另起一笔，add/commit 双侧限定 W3 一件，`collab:` 前缀。
3. 两笔提交**各自落账后才算收束**（做了没落盘／落盘没提交／提交没对账，三态逐条写，不合并成「已完成」）。回执开端附开工／提交前两时点读数（并发前移照登）。
4. 回执必含：①开工三读数；②租约签发四字段输出誊录；③判据 1–11 逐条实测读数（命令＋输出要点）；④**完整写入/修改文件清单**（对账口径＝`git show --name-only` 与清单全等）；⑤仓外临时目录清理读数；⑥`git status` 读数（他案在制品照登）；⑦三态明示逐条。
5. 回执中禁全称断言（「零指针」类），涉零命中表述必写检索范围＋命令＋实测读数（R5-01 教训）。

## 六、收口即停

本票射程仅到「两件落成＋租约实证＋回执落账」。**不得**自行进入 QA 独立验、真实 PRD 试填（第 7 步硬闸归主理人另派）、改契约、T3–T6、升号、装配、部署或任何发布动作。收口后回报主理人。

## 七、异常停止条件（任一命中即停手上报）

- 规格真源 `8388470` 不可解析或 sha 不等；
- 交付两件任一件开工时已存在；
- 任一验收判据与钉值不符；
- 需要第三交付文件或触碰禁动面任一面；
- 租约对 `skills/**`＋`config/**` 写域签发失败；
- 并发线在写集内产生改动（如实登记区间读数，不自行合并）。
