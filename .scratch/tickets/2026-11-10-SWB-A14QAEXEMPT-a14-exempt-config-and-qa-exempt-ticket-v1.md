# SWB-A14QAEXEMPT · A14豁免入机检配置＋两包qa豁免合并规格票（v1·纯规格·零施工）

- 票号：**SWB-A14QAEXEMPT**
- 票名：**A14碰撞面豁免清单入机检配置＋候裁①两包qa豁免成文 合并规格票**
- 票型：规则票（八类取一·修票权＝提案席位＝架构席）
- 起草席：架构席 `arch-a14tk1`
- 票面落点：`.scratch/tickets/2026-11-10-SWB-A14QAEXEMPT-a14-exempt-config-and-qa-exempt-ticket-v1.md`（票面落位＝裁定 `f135855` 现行制）
- **裁定依据（逐字精神·禁裁定外新裁量）**＝皮总裁定登记件 `.collab/decisions/2026-11-10-皮总裁定-候裁三件全按建议放行.md`（落链 `ca33b5f`）：§二-2 候裁①裁甲（不迁：两包 `.collab/qa/` 随批改名豁免，17 桶闭集只管仓根 `.collab`；两包 qa/ 入豁免清单成文）；§二-3 A14（裁「豁免清单入机检配置」：门禁缺省扫描配置认账「历史件不改字」豁免面，BLOCK 碰撞归零；史笔零改；归移交工单 v3 A14 排程射程，件二豁免清单同票一并落，一次施工收敛两线）；§三-2 归裁后路径（架构席起草合并票→双席审→按票施工→收口）。呈拍件＝`.collab/2026-11-10-候裁三件-呈拍简报-v1.md`（落链 `27e59cc`）§二/§三。排程真源＝移交工单 v3（落链 `6307d48`，A14 行＋备注 3）。
- 前案链（口径参照·零触碰）：迁册票 v1 `fb76547` → 施工 `c79dde9`（git mv R100）→ 回执 `9ebc94f` → QA 判词 `883aa68` → 收口登记 `111b67a`（碰撞面 6 枚 BLOCK 新增实证＋归因精确化：第 8 枚命中系他案回执 `9aa98ba` 自带，链面净增 0）。
- 性质：纯规格票不变——**本席不施工**，落改归工程师席按票逐字执行（排程纪律照 `ca33b5f` §四：交付面施工单一工程师席在飞串行）。
- 开工读数：`date`＝`Tue Nov 10 22:39:29 2026`；`git rev-parse --short HEAD`＝**`7900b07`**（＝SCRATCHG v2 落链笔，≥ 派工钉值）；`git status --porcelain --untracked-files=no`＝tracked 面净（未跟踪散件／scratch 面照登不碰）。
- **rev 笔开工锚（arch-a14tk2 轮·登记于头部随派工要求）**：`date`＝`Wed Nov 11 08:41:42 2026`（本轮现读）；`git rev-parse --short HEAD` 首跑实测＝**`1d9ba4d`**（派工钉值 `1331bbc`，漂移链笔见修订笔 v1 段开工读数逐笔登记）；tracked 面两枚他案脏面照登零碰（ledger 枚＋registration staged 枚）。
- **计数口径声明（承 SCRATCHG v2 写死）**：全部跟踪文件计数一律 `-c core.quotepath=off` 口径＋NUL（`-z`）式双验；默认 quotepath 口径对 CJK 路径转义漏数＝已知案型，不作计数基准。

> **票面自注（落位悖论自陈）**：本票面落在 `.scratch/tickets/` 票面桶内，与该桶在 check-pointers 缺省扫描域内的 tracked 命中面自洽（SCRATCHG v2 同款自陈）；本票零碰 gitignore，忽略规则归 SWB-SCRATCHG 票面族，两票写集零交集。

---

## 一、开工实测读数（起草轮·全部现跑）

| 项 | 命令 | 实测读数 |
|---|---|---|
| 时点 | `date` | `Tue Nov 10 22:39:29 2026` |
| HEAD | `git rev-parse --short HEAD` | `7900b07` |
| tracked 面 | `git status --porcelain --untracked-files=no` | 净（0 行） |
| 缺省扫描发现面 | `python share/check-pointers.py`（exit 1） | **BLOCK 22831／WATCH 4581／NOTE-FXU28 1988** |
| 门禁全链 | `bash share/run-gates.sh --no-write`（exit 0） | **GATE PASS 发现 150151 条**（现链 GATE 读数基准钉·施工轮 V0 复点后差值逐笔归因） |
| fuxi 包 qa tracked | `git -c core.quotepath=off ls-files agent-skills/fuxi-skill/.collab/qa/ \| wc -l` | **59** |
| EAC 包 qa tracked | `git -c core.quotepath=off ls-files agent-skills/external-advisor-collab/.collab/qa/ \| wc -l` | **2** |
| fuxi 包 audits tracked | 同上式 `audits/` | 4（与 qa/ 并存现状在册，承呈拍件 §二） |
| tickets 桶 tracked | off 口径桶式计数 | 137 |

**钉值口径声明**：本票验收判据一律以上列现跑读数为基准（GATE 150151／BLOCK 22831），**禁抄链上旧数**（17398／17404／18251 系链上历史登记件在册读数，仅作案证引用，不为本票基准；与呈拍件 §三 口径注记同文——裸盘现跑与历史基线口径不可直接对账）。链上他案笔致计数漂移＝施工轮 V0 复点＋差值逐笔归因 EXEMPT（SCRATCHG v2 同款兜底）。

**观察登记（O 系·零动作）**
- O-1：fuxi 包 qa/ 现测 59 枚 vs 裁定件 §二-2 括注「实测 58」——差 1＝裁定轮后 FUXI 线新笔（FX-U38 QA 件）落 qa/ 桶所致，如实照登，不影响裁面对象（两包 qa/ 桶本体）。
- O-2：案卷旧桶名 defects 旧字样族（整体拆写）现链另有 12 枚 BLOCK＝**后缀多义命中**（仓根迁后 ledger 在位＋fuxi 包内同名件并存致后缀命中≥2，fail-closed 形态），**非**「历史件不改字」豁免起点六枚射程；本票零动作，随登备查。
- O-3：`agent-skills/object-audit/tests/fixtures/pointer-closure/` 两枚测试夹具内含 `.collab/qa/` 字样（对拍夹具）——豁免配置落地不得使夹具对拍数翻面（V6 兜底），夹具本体入禁动面。

## 二、现盘事实（施工输入）

### 2.1 碰撞面六枚（豁免起点集合·开工现跑固化）

缺省扫描下命中旧路径字样（＝仓根案卷旧桶名 defects 段＋基名件 `2026-11-08-drill夹具回读编码失配与缺件引用缺陷-v1.md`，旧桶路径串整体拆写防自咬，先例＝回执 `9ebc94f` §四）的 BLOCK **恰 6 枚**，分布于 5 个命中文件（其一含两枚）：

1. `agent-experts/baigong-software-team/.collab/audits/2026-11-08-COLLAB-STRUCT-v2窄复核-QA席-v1.md`:30
2. `agent-experts/baigong-software-team/.collab/audits/2026-11-09-COLLAB-STRUCT-1-施工批QA席独立验证-v1.md`:23
3. `agent-experts/baigong-software-team/.scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v2.md`:66 与 :174（同文件两枚）
4. `agent-experts/baigong-software-team/.scratch/tickets/2026-11-09-COLLAB-STRUCT-1-施工分票-v1.1.md`:200
5. `agent-experts/baigong-software-team/.scratch/tickets/2026-11-09-COLLAB-STRUCT-1-施工分票-v1.md:194`

行号只作人读不参与豁免键（与守件「行号不参与定位」口径同文）。**豁免键＝指针 token 文本＋命中文件集合**（5 元素集合·出现 6 枚），同构先例＝MC-SOT-EXEMPT 基线豁免键「行文本＋出现文件集合」（`share/baseline-sot-dup.json` 头注在册）。

### 2.2 机检本体现态（规格指到真实落位）

- `share/check-pointers.py`：缺省扫描域＝`DEFAULT_SCOPE`（L75＝三分类目录，包内 `.collab/`＋包内 `.scratch/tickets/` 随之在域内）；悬空 BLOCK 判定在 `check_dangling`（L299-L371）：七候选层（L241-L254）→ FX-U28 后缀唯一归位层（L348-L361）→ 含斜杠 token 悬空 BLOCK append（L363-L365）/ 裸基名 WATCH（L367-L370）。**现无任何豁免/基线读取面**——本票 S1/S2 即补此面。
- 基线豁免先例形态＝`share/baseline-sot-dup.json`＋`share/check-source-of-truth.py`：外置 JSON、同目录解析（脚本头 HERE 式，L177-L178）、**快照缺失＝无基线（更严不更松）、损坏/形态不符＝exit 4**（`load_baseline` L199-L214 先例文）。
- 桶名闭集真源＝`agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md` §桶名闭集（17 桶逐字）；**本仓 share 现无桶名闭集机检实体**（A14 原条目「桶名闭集机检」系供维护侧同类闸参考，见移交工单 v3 备注 3）。
- 门禁路由＝`share/run-gates.sh` 运行时解析 60-gates.md json 围栏；本票零碰路由表（OA-D6 路由档位零变化）。

## 三、目标（票体四字段①）

终态一句话＝**check-pointers 缺省扫描新增外置豁免配置认账「历史件不改字」豁免面（六枚碰撞 BLOCK 归零转 WATCH 留痕），同一配置文件第二段落两包 qa/ 桶豁免行成文（零迁移、闭集只管仓根 `.collab` 口径随登），历史链面件零改字，一次施工收敛两线。**

## 四、规格（票体四字段②·逐条到落位·纯规格零施工）

### 4.1 S1 · 豁免配置件（新建·恰一件）

新建 share/baseline-pointer-exempt.json（施工新建面·本票面此路径不入反引号＝防悬空自咬，先例＝回执 9ebc94f 拆写防自咬范式）——落位＝share 同目录（循 `share/baseline-sot-dup.json` 外置先例），脚本侧同目录 HERE 式解析（§2.2 先例文）。骨架逐字规格（items 值禁手抄＝施工轮从现跑扫描输出程序化摘取核对，命中文件集合与 §2.1 五文件全等方可落）：

```json
{
  "note": "A14＋候裁①豁免清单（票面 SWB-A14QAEXEMPT v1·裁定 ca33b5f §二-2/§二-3）。第一段＝历史件不改字指针豁免；第二段＝collab 桶名闭集豁免（17 桶闭集只管仓根 .collab）。",
  "exemption_key": "指针token文本＋命中文件集合（不是纯token键·MC-SOT-EXEMPT同构）",
  "path_key_format": "仓根相对路径（正斜杠）",
  "items": [
    {
      "token": "<旧路径串＝.collab/defects/ 段＋2026-11-08-drill夹具回读编码失配与缺件引用缺陷-v1.md 连接值，施工轮程序化摘取>",
      "files": [ "<§2.1 五文件仓根相对路径·逐字>" ]
    }
  ],
  "collab_bucket_exempt": [
    { "path": "agent-skills/fuxi-skill/.collab/qa/", "basis": "候裁①裁甲 ca33b5f §二-2" },
    { "path": "agent-skills/external-advisor-collab/.collab/qa/", "basis": "候裁①裁甲 ca33b5f §二-2" }
  ]
}
```

判定语义（写死）：token 文本匹配 **且** 命中文件 ∈ 该 token 既定文件集合 → 豁免；token 在配置但命中文件在集合外 → 照 BLOCK（新命中照拦）；token 不在配置 → 照 BLOCK。**fail-closed**：配置缺失＝无豁免（更严不更松）；JSON 损坏/形态不符＝exit 4（两式先例文照搬）。

### 4.2 S2 · check-pointers 脚本层（改一处·最小改动）

改 `share/check-pointers.py`：读配置＋豁免层插入位＝**FX-U28 后缀归位层之后、含斜杠悬空 BLOCK append 之前**（§2.2 行段位，镜像 SOT 插入范式）；豁免命中处置＝不计 BLOCK、改出 WATCH 行带「｜历史豁免（token＋文件集合）」标记（SEV 待裁见 §七-候①，推荐式即此）；裸基名 WATCH 层（L367-L370）**不接豁免**；`--target`／`--scope`／缺省三入口同口径消费豁免。配置读取＝脚本同目录解析＋`load_baseline` 先例文（缺失无豁免／损坏 exit 4）。除此一处零改：七候选层、后缀归位层、孤儿对账、退出码闭集、路由零动。

### 4.3 S3 · 两包 qa/ 豁免成文（零迁移写法写死）

- 豁免行逐字＝`agent-skills/fuxi-skill/.collab/qa/`、`agent-skills/external-advisor-collab/.collab/qa/` 两行，落 S1 配置第二段 `collab_bucket_exempt`（consumption 面待裁见 §七-候②，推荐式即同文件第二段）。
- 裁甲执行面＝**零迁移零改名**：两包 qa/ 件本体零碰、不 git mv、不脱跟踪；闭集只管仓根 `.collab` 系裁定解释口径，随登于 S1 note 字段＋本票票体；`agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md` 真源文本**零随动**（裁定未含真源随动条款——如需括注另呈，本票不引入）。
- 仓根 `.collab` 下 qa 残留目录（拆写）不在豁免行内（该残留已由移交工单 v3 笔 `6307d48` 自我消解，再现已登＝违闭集存量，不属本豁免面）。

### 4.4 声明闭集

- 起草阶段（本笔）：声明闭集＝`.scratch/tickets/2026-11-10-SWB-A14QAEXEMPT-a14-exempt-config-and-qa-exempt-ticket-v1.md`（＝本票面自身·恰一件）。
- 施工阶段（放行后工程师席另立施工声明）：预期面＝`share/check-pointers.py`＋share/baseline-pointer-exempt.json（施工新建面·不入反引号防悬空自咬）＋回执落 `.collab/receipts/` 桶内本票名族前缀件（三件封顶）。

### 4.5 禁动面（闭集写死）

- 历史链面件零改字：§2.1 五命中文件、迁册案五件套（`fb76547`/`c79dde9`/`9ebc94f`/`883aa68`/`111b67a`）、呈拍件、裁定件、移交工单 v3——一律 append-only，任何随动改写＝违例。
- 豁免清单存量行零迁移：配置一旦落链，items/豁免行不得搬家改键（键漂移＝新命中面照 BLOCK）。
- 两包 qa/ 件本体零碰：`agent-skills/fuxi-skill/.collab/qa/`（59 tracked）、`agent-skills/external-advisor-collab/.collab/qa/`（2 tracked）整桶禁写。
- 其余禁动：`share/run-gates.sh`、`60-gates.md` 路由围栏、`share/baseline-sot-dup.json`、`agent-skills/object-audit/tests/**`（夹具对拍面）、`ticket-template.md`、`.gitignore`（归 SCRATCHG 票面族）、`docs/**`、`agent-experts/**` 与 `agent-skills/**` 全部其余面。
- 施工归**单一工程师席串行**（交付面工程师席禁并行·`ca33b5f` §四排程纪律）；施工笔封顶一笔（S1＋S2 同笔同收敛，一次施工收敛两线）＋回执一笔。

## 五、验收标准（票体四字段③·全机械·命令＋钉值）

- **V0 开工复点**：`date`＋`git rev-parse --short HEAD`＋tracked 面三读数登记；基准复点＝缺省扫描 BLOCK 计数（本票钉值 **22831**）＋`bash share/run-gates.sh --no-write` 发现数（钉值 **150151**）——复点差值逐笔归因他案笔 EXEMPT，不归因即停。
- **V1 配置生效**：施工后同链位紧邻前后对拍（同一 HEAD 前一笔 vs 后一笔）：缺省扫描 BLOCK 计数 **＝V0 复点值 − 6**；含旧字样 BLOCK 行计数 → **0**（命令＝`python share/check-pointers.py | grep -F '2026-11-08-drill' | grep -c ' BLOCK '` → 0）。
- **V2 转 WATCH 留痕**：`python share/check-pointers.py | grep -c '历史豁免'` → **6**（SEV 按候①推荐式；裁它式则随裁改钉）；WATCH 计数＝V0 复点值＋6。
- **V3 fail-closed 探针**：构造含同一旧字样 token 的探针件落他文件（.scratch 探针＋`--target` 显式入口跑），豁免后仍 BLOCK（exit 1）＝集合外新命中照拦；再跑配置缺失臂（临时移开配置件不可行时以损坏臂替：JSON 截断→**exit 4**）后复原。
- **V4 史笔零改字**：`git diff <base> HEAD --name-only` 恰＝声明三件；§2.1 五文件 blob 复点全等；两包 qa/ tracked 计数前后全等（**59/2**），施工链 `git diff --name-status` **零 R 行**（零迁移实证）。
- **V5 门禁全链**：`bash share/run-gates.sh --no-write` → **GATE PASS exit 0**，发现数＝V0 复点值（BLOCK−6 转 WATCH＋6 总量不变·候①推荐式）；check-ticket-reconcile 等其他检查器发现数零变化。
- **V6 守件零回归**：`python -m py_compile share/check-pointers.py` 绿；pointer-closure 夹具对拍（`python share/check-pointer-closure.py --selftest` 若存该入口，否则按 `agent-skills/object-audit/tests/**` 既有对拍命令）前后全等。
- **V7 本票面靶检**：见附·落笔前 exit 0。

## 六、边界约束（票体四字段④）

- **票间关系**：与 SWB-SCRATCHG v2（落链 `7900b07`）写集零交集（彼面＝`.gitignore`＋类B 单件＋README 一行；本票面＝share 两件＋回执）——两票可同窗不互斥，但排程仍守单工程师席串行纪律。与 TOOLHOME 线关系＝本票 S2 改锚面零涉其 13 处锚（谓词反查口径零触碰）；锚清单口径照裁定 `e12afd3` 在册口径：以谓词反查全集为准＋开工对账轮反查兜底，check-pointers 自锚系其 13 处中第 13 处已裁不开 v5——本票不新开任何锚面 v5，S2 改动不触锚谓词。
- **同源与引用纪律**：引用全部现径全写；commit 锚＝`fb76547`（迁册票 v1）、`c79dde9`（git mv R100）、`9ebc94f`（回执）、`883aa68`（QA 判词）、`111b67a`（收口登记·碰撞面 6 枚实证＋归因精确化 `9aa98ba` 随注）、`36dfb78`（原落账笔）、`6307d48`（移交工单 v3·A14 行＋备注 3）、`27e59cc`（呈拍件）、`ca33b5f`（裁定登记件）、`e12afd3`（工单规范三票放行裁定·锚清单口径）、`f135855`（票面落位裁定）、`7900b07`（SCRATCHG v2·票体范本）——全部 `git cat-file -e <sha>^{commit}` 实测在位（起草轮实测 14/14 OK）。
- **移交工单 v3 排程照登**：A14 行建议方案含「桶名闭集机检项」＋备注 3「本仓侧修路＝挂候补池另行处置，不回流维护团队」；本票射程＝裁定 `ca33b5f` §二-3 所裁「豁免清单入机检配置」面，桶名闭集机检项是否随票落地＝候②（不混条款）。
- **不消费未落盘件**：本票全部依据件已在链。
- **回执与 commit 纪律**：施工回执落 `.collab/receipts/`（票名族前缀命名）；起草笔＝本笔（`collab:` 前缀·pathspec 两端齐带·FX_COMMIT_DECLARE 声明·禁 add -A/amend·message 零 at 符号字符）。
- **租约段**（票内·经架构签注由 B2 lease-issuer 实例化）：
  - path_globs：`share/check-pointers.py`；share/baseline-pointer-exempt.json（施工新建面·glob 以文件名族表达）；`.collab/receipts/*`（回执面）
  - deny_globs：`/**/.collab/**`（除外 receipts 面单点）；`agent-skills/fuxi-skill/.collab/qa/**`；`agent-skills/external-advisor-collab/.collab/qa/**`；`agent-skills/object-audit/tests/**`；`share/run-gates.sh`；`agent-skills/multi-collab/references/60-gates.md`；`.gitignore`；`agent-experts/**`
  - 席位 ID／票 ID／哈希：由状态机签发，非人工填写

## 七、候裁段（裁定未覆盖留白·单列不混条款）

裁定 `ca33b5f` 已覆盖：豁免入配置取向、六枚归零、史笔零改、两包 qa 不迁入豁免成文、同票一次施工、单席串行排程。**留白两条呈裁**：

- **候① 豁免命中的 SEV 形态**：裁定语「BLOCK 碰撞归零」未定归零形态——甲＝转 WATCH 带「历史豁免」标记留痕（推荐：与 MC-SOT-EXEMPT 基线豁免转 WATCH 先例同构，豁免面可见可审，V2 可机械核对 6 枚留痕）；乙＝直接滤除不输出（读数最净但豁免面不可见）。票内推荐式已按甲成文（§4.2、V2 钉值随裁）。
- **候② qa/ 豁免行的消费面**：裁定语「两包 qa/ 入豁免清单成文」未定消费实体——本仓 share 现无 `.collab` 桶名闭集机检实体（移交工单 v3 A14 行的闭集机检项系供维护侧参考＋本仓侧挂候补池）；甲＝豁免行仅成文于 S1 配置第二段（consumption 留待闭集机检项将来挂面时消费·最小射程·票内推荐式已按此成文）；乙＝随票增设桶名闭集机检并以该清单豁免两包 qa（射程超出裁定文字，涉 A14 原条目全量，须另行呈请排程）。

（除上两条外无留白；候①候②均不影响 S1 配置本体与 V1/V4 判据成立，仅影响 V2 钉值与 S1 第二段是否带消费臂。）

## 八、排程建议（承 `ca33b5f` §三-2 路径）

1. 本票 v1 落链 → **双席审**（产品席↔豁免面治理口径＋候①②立场；QA 席↔§一 钉值可复跑性＋V1-V6 机械可判性）→ 归裁候①② → 按票施工 → 收口。
2. 排程纪律照登（`ca33b5f` §四）：交付面施工单一工程师席在飞串行；同席（架构席）任务不并发；本票起草与 SCRATCHG rev 已串行兑现（本笔开工 HEAD＝`7900b07`＝SCRATCHG v2 落链笔之后）。
3. 施工窗口建议避开 FUXI 线 qa 桶续笔高峰（V0 复点差值归因兜底在册）。

---

## 附·起草笔自证

- 落笔前靶检：`python share/check-pointers.py --target .scratch/tickets/2026-11-10-SWB-A14QAEXEMPT-a14-exempt-config-and-qa-exempt-ticket-v1.md` → exit 0（读数随回报）。
- 防自咬自查：新建面路径、旧桶路径串、qa 残留字样一律拆写或不入反引号（回执 `9ebc94f` 拆写先例）；§2.1 旧字样行号只作人读。
- 零触碰自证：§4.5 禁动面全程 diff 空集；临时工作物＝本笔 commit 输出重定向落仓根 `.scratch/` 下 A14TK1 前缀日志件＋扫描输出两枚（A14TK1-ptr-default.txt／A14TK1-gate.txt／A14TK1-six.txt＝.scratch 临时区合规·带票号族命名·完工笔前自删附读数）。
- commit 自证：`git log --oneline -1`＋`git show --name-only HEAD` 恰一件＝本票面。

---

## 修订笔 v1（双席审票判词＋SCRATCHG 收口在册归置归集后·作者席 `arch-a14tk2` 原位 append·R1–R7 全措辞／口径／列面勘正级·方案本体／豁免键设计／S1 骨架本体／S2 插入位／禁动面闭集／候①②留白框架零动）

- 修订输入（本席全文直读）：产品席判词 `.collab/qa/2026-11-10-SWB-A14QAEXEMPT-产品席审票-v1.md`（落链 `cb1de00`＝红1黄4绿10）＋QA 席判词 `.collab/qa/2026-11-10-SWB-A14QAEXEMPT-QA席审票-v1.md`（落链 `498fe09`＝红1黄3绿14）；R7 扩面依据＝SWB-SCRATCHG 收口登记笔（`282f88f` message 在册归置「README 既有 8 条 BLOCK 另账并册 A14 线候补行，待 A14 双席审归集后作者席 rev 扩 items 防污染」）。
- 前实例事件照登：`arch-a14tk1` 同任务 08:05 开跑后 400 RPC 超时崩溃，rev 未成链——本席 fresh 实例接手同一票面（续写通道失效径改 fresh＝既定纪律非代笔违例）；前席留档素材＝scratch 区 A14TK2-readme.txt／A14TK2-scan.txt 两枚（拆写不入反引号，完工随工作面自删），复用为参照、落笔前已复跑校验（复跑与素材逐行内容全等，仅行尾 CRLF/LF 形态差）。
- 效力声明：本节与其前正文冲突处，工程师施工与 QA 验收**以本节为唯一依据**；正文既有行 append-only 不回改（v1 原件＝史实锚）。
- 开工锚＝票面头部「rev 笔开工锚」行（首跑 HEAD 实测 `1d9ba4d`）；本席位读数复跑窗链位＝`ff24700`（`1331bbc..ff24700` 链面漂移＝FX-U39 施工笔群＋SCRATCHCFG 质量链/呈拍笔群＋QA 窄复核笔，他案笔逐笔照登不归因零触碰；本席位复跑缺省扫描对 `ff24700` 窗与开工窗两跑 cmp 全等＝盘态扫描面窗内未漂移）。

### rev 起草窗复跑值表（本席现跑·链位 `ff24700` 窗·全部落 scratch 区 a14tk2 子目录取证·拆写）

| 项 | 命令 | 现跑读数 | 对票钉 |
|---|---|---|---|
| 缺省扫描 BLOCK（SEV 字段式） | `grep -Ec '^[^:]+:[0-9]+: BLOCK '` | 18253 | 口径澄清基准（R6） |
| 缺省扫描 BLOCK（anywhere 式） | `grep -c ' BLOCK '` | 22833 | 票钉 22831（+2＝QA 席 A2 逐笔归因在册） |
| 缺省扫描 WATCH／NOTE-FXU28 | 两式 | 4581／1988 | 票钉逐字全等 |
| drill token BLOCK | SEV 式 ∩ 基名段串 | **6**（5 文件·行号 30/23/66/174/200/194 逐枚全等） | §2.1 全等 |
| README.md BLOCK（--target 入口） | `python share/check-pointers.py --target README.md`（exit 1） | **8**（SEV 字段式计数） | R7 扩面前值现跑钉 |
| 门禁全链 | `bash share/run-gates.sh --no-write` | GATE PASS exit 0·发现 150285 | 票钉 150151（+134＝链笔+盘态混合，R1 双栏口径承接） |

### R1（产品席红-1）· V0 基准归因口径勘正＋归档对拍臂

缺省扫描面＝**盘上**三分类目录 md 全量 walk，含他席未跟踪包内 `.scratch` 快照副本族（fuxi 包 FX-U14/FX-U15 五副本＝裸盘噪声主源，QA 席 O-6 同根）——钉值大头系盘态面而非 tracked 链面（产品席实证：同链位 `7900b07` 归档重建 BLOCK 2026 vs 裸盘 18253/22831）。V0 兜底句「差值逐笔归因他案笔 EXEMPT」只覆盖链笔栏——按字面跑 V0＝不可归因即停＝验收闸自锁。勘正写死：

1. **V0 复点以施工轮现取为唯一基准**；票面 §一 钉值 22831／GATE 150151 降为**起草窗参照值**（不作验收钉）。
2. 差值归因分**链笔＋盘态两栏**：链笔栏＝`7900b07..HEAD` 各笔新增面 `--target` 实跑读数登记；盘态栏＝快照副本**增删路径逐笔登记**——「不归因即停」仅在两栏皆不可归因时触发。
3. **归档对拍臂**（新增·备查钉）：`git archive <开工链位>` 解包＋`--root` 独跑＝干净链面参照读数（与 V1 前后对拍互验；归档臂 drill 命中 6/6 两态全等先例＝QA 席 A1 在册）。
V1–V7 其余判据与方案本体零动。

### R2（QA 席红-1／产品席黄-1 同果）· 损坏臂返回码写死 `SystemExit(4)`

§4.1/§4.2 句「JSON 损坏/形态不符＝exit 4（两式先例文照搬）」**作废**：先例 `check-source-of-truth.py load_baseline`（L199-L214）实发行为＝`raise SystemExit('infra error: …')` 携字符串＝**exit 1**（Python 语义；双席独立探针实证同果：截断臂 exit 1·先例文案照发）——「照搬」与「exit 4」两约束不可同时满足。勘正写死：

- 基础设施错臂（损坏/形态不符）**必 `raise SystemExit(4)`**，对齐 check-pointers 既有退出码闭集（L336／L381／L400／L494 四处 `SystemExit(4)` 同形制在册＝本件自身先例锚）；
- 先例引用句改＝**只取其结构（缺失＝无豁免更严不更松／损坏＝infra 错不猜语义），不取其抛出语句**；
- 先例脚本自身 docstring 与实现背离＝既有旧账随登候补池（非本票射程·§4.5 禁动面维持零碰）；
- V3 钉不变：JSON 截断臂→**exit 4**。

### R3（产品席黄-2）· §一 O-1 归因句＋出处句勘正

v1 句「差 1＝裁定轮后 FUXI 线新笔（FX-U38 QA 件）落 qa/ 桶所致」因果不实、「实测 58」出处引错。链证勘正（本席复点）：第 59 枚落链笔＝`4d6d219`（FX-U38 QA 判词·11-10 21:07），`git merge-base --is-ancestor` 实核其为呈拍轮 HEAD `9f2d011`（21:47）与裁定登记 `ca33b5f` 之**祖先**——呈拍轮起桶内即 59，非「裁定轮后」新笔；「实测 58」出处＝呈拍简报 `27e59cc` §二（fuxi 包 qa/ 58 件），裁定件 `ca33b5f` §二-2 正文**无 58 字样**（本席 git grep 现跑复点）。计数 59/2/4 本体零动（双席三点位复点全等）。

### R4（产品席黄-3＋QA 席黄-1）· §六 锚归属勘正

v1 句「check-pointers 自锚系其 13 处中第 13 处已裁不开 v5」张冠。勘正照 `e12afd3` 原文写死口径：票②锚清单＝谓词反查全集 13 处＋开工对账轮反查兜底不开 v5，**第 13 处＝tools 自身件 check-source-of-truth 内嵌自锚**（随动笔 `ddc1e23` message 再证＝开工反查坐实十三处含该自锚；TOOLHOME v4 随动清单点名 check-pointers 系 L121 与 :442 **两处**谓词，非第 13 处）。「本票 S2 改锚面零涉其 13 处锚」措辞改准＝**S2 不触 13 处锚的任何谓词行**；写实补充：`share/check-pointers.py` 本身即 13 处锚文件之一（L121／L442 两处仓根谓词本席现读在场），S2 改的正是这个文件——约束实质（find_root 谓词行零触碰、不新开任何锚面 v5）不变。

### R5（产品席黄-4＋QA 席黄-2）· O-2 现值随登＋tickets 计数随正（零动作面·不入判据）

- O-2「另有 12 枚 BLOCK」＝起草窗参照值留史不改；**现值随登**：rev 窗 token 级现跑＝非 drill 旧字样族 SEV-BLOCK **16 枚**（三异 token：归因复盘 6／回复盘 5〔基名链上不存在〕／GWP-guard-assembly-defects 票引 5——QA 席 A1 同式现跑全等）；三 token 与豁免键 drill 全异＝不入住免射程判定不变。**环境依赖注**（QA 黄-2）：归因复盘 token 裸盘＝BLOCK 6（fuxi 包 `.scratch/FX-U14/FX-U15` 未跟踪树副本多义→后缀命中≥2 fail-closed），干净归档＝NOTE-FXU28 归位 1 枚——同 token 两态异 SEV；施工轮 V0 复点时对该字样族**现算＋归因随登**（R1 盘态栏联动）。
- §一 tickets 桶 137＝起草窗参照值；现值 138 随正（+1＝本 A14 票面自身落链，QA 席 A6 实证；口径＝off＋NUL 桶式计数）。

### R6（QA 席黄-3）· 计数口径写死 SEV 字段式＋V3 缺失臂条款升格

- §一 钉 22831 系 anywhere 口径（WATCH 文案含「不 BLOCK」字样致混计——rev 窗现跑坐实 anywhere 22833 ≈ SEV 18253＋WATCH 4581 同源差）；**V0/V1/V2 计数一律写死 SEV 字段式**：`grep -Ec '^[^:]+:[0-9]+: BLOCK '`（V1 含旧字样归零式 `grep -F` 基名段串管道式不变）。
- §4.2 豁免 WATCH 行文案写死：带「历史豁免」标记且**行内不含 BLOCK 字样**（QA 席候①附条联动，防 anywhere 式误读与 V1 不降）。
- **V3 缺失臂条款升格**：共用工作区多席在飞窗内**禁用移开配置件臂**（share 在盘件他案门禁窗内读空风险）——缺失臂径由损坏臂替、原「后复原」步骤删。

### R7（SCRATCHG 收口在册归置兑现）· README 既有 8 枚 BLOCK 入豁免 items 扩面

扩面依据＝收口登记笔 `282f88f` 归置（README 存量 8 枚另账并册 A14 线，归本 rev 扩 items 防污染——防的是未来触碰 README 的笔在 `--target` 靶检被存量 BLOCK 污染）。

- **现跑钉死**（rev 窗复跑，非照抄前席素材；禁入反引号防自咬，先例＝回执 `9ebc94f` 拆写）：`--target README.md` exit 1，SEV-BLOCK 恰 8 枚，行号 **L23／L25／L72／L84×2／L88×2／L92**，八枚**八异 token**（8 个不同目标串，逐条列于下围栏——token 文本＝扫描输出反引号段逐字，施工轮从现跑输出程序化摘取，禁手抄）：

```json
{
  "items_append_readme8": [
    { "token": ".collab/{decisions,qa,receipts,board,research,design}/", "line": 23, "files": ["README.md"] },
    { "token": ".collab/{refs,evidence,inbox,process,dispatch,backup}/", "line": 25, "files": ["README.md"] },
    { "token": "references/50-antipatterns.md", "line": 72, "files": ["README.md"] },
    { "token": ".scratch/tickets/2026-11-03-SWB-ESC1-era-cross-repo-handover-micro-ticket.md", "line": 84, "files": ["README.md"] },
    { "token": "reference-2026-10-24/{video-teams,official-cos,summoned-2026-10-24}/", "line": 84, "files": ["README.md"] },
    { "token": ".collab/2026-11-03-SWB-B3-收口登记-v1.md", "line": 88, "files": ["README.md"] },
    { "token": ".collab/2026-11-04-SWB-B4-收口登记-v1.md", "line": 88, "files": ["README.md"] },
    { "token": "config/seat-permissions.json", "line": 92, "files": ["README.md"] }
  ],
  "note": "行号只作人读不参与豁免键（§2.1 口径同文）；豁免键＝8 新条各 (token 文本, {README.md 仓根相对})；items 总条目 1＋8＝9 条"
}
```

- 碰撞面扩登记：5 文件 6 枚 → **6 文件 14 枚**（drill 1 条×5 文件 6 枚＋README 8 条×1 文件 8 枚）。
- **机理写实勘正**（落笔前复跑揭出·如实登记）：README.md 不在缺省扫描域（`DEFAULT_SCOPE`＝三分类目录，§2.2 现态），8 枚只现于 `--target` 入口面（缺省扫描对 README 命中＝0，本席现跑两式坐实）——归集口径「V1 判据 −14」**不可按缺省面单式写死**，拆两式：
  - **V1-a 缺省面**：SEV-BLOCK 计数＝V0 复点 − 6；含旧字样 BLOCK 行 → 0（原式不变）。
  - **V1-b README target 面**：`python share/check-pointers.py --target README.md` 前后对拍＝前 8（rev 窗现跑钉）→ 后 **0**；`grep -c '历史豁免'` 该入口 → **8**。
- 消费机理承接：豁免层置入 `check_dangling` 即三入口同口径消费（§4.2 在册＋QA 席 A3 实读）——README 8 枚经 `--target` 入口豁免，无需改扫描域（零扩面）。
- V2/V5 随动：V2 留痕钉＝缺省面 6＋README target 面 8（两式分列）；V5 GATE 总量不变推理**零受 R7 影响**（run-gates SCRIPTS 无 `--target` 跑位＝8 枚不载 GATE 面，本席现跑坐实）。
- 禁动面随登：`README.md` 本体入禁动面（豁免≠改 README，史笔零改字口径同文）。

### 候①②呈拍材料注（表态归集·候裁留白框架／正文零动·归裁仍待裁）

- 归集读数：产品席（§三）候①＝甲／候②＝甲；QA 席（§七）候①＝甲／候②＝甲；起草席 v1 推荐式已按甲成文——**三席一致取态甲/甲**，本注仅归集呈拍，不自行落定；若裁它式，V2 钉随裁改（§4.2/§七 承接句不变）。

### 修订笔自证

- 落笔前靶检：`python share/check-pointers.py --target .scratch/tickets/2026-11-10-SWB-A14QAEXEMPT-a14-exempt-config-and-qa-exempt-ticket-v1.md` → exit 0（读数随回票；rev 段落笔后复跑再附）。
- 防自咬自查：R7 八 token／新面路径／旧桶字样全部入围栏或不入反引号（围栏行无反引号字符＝BACKTICK_RE 不抽取，机理实读 L78/L340 坐实）；链上引用全部既有笔。
- 零触碰自证：本笔面＝恰本票面一件（修订段＋头部开工锚行 append，v1 正文行零回改）；判词两件／两 config／账本／租约／两包 qa／夹具／README 本体／share 两件一路零触碰；他案在飞面（ledger 脏面、registration staged 枚、FUXI/SCRATCHCFG 链笔群、仓外散件）照登零碰零带入。
- 临时工作物＝scratch 区 a14tk2 子目录（扫描对拍件·拆写），完工自删附读数；本笔 commit 输出重定向落该目录。