# DEBTCLN-R1 · ROOTCLN 仓根散件迁册票（v1·规格票·起草笔零施工）

- 票号：**DEBTCLN-R1**（清债批次第一票·族名锁定，勿改）
- 票名：**仓根散件迁册票（ROOTCLN）**
- 票型：清债·迁册票（同构先例链＝A14 迁册：票 v1 fb76547 → 工程 git mv c79dde9 → 回执 9ebc94f → QA 判词 883aa68 → 收口 111b67a）
- 起草席：架构席 arch-debt1（fresh 实例·主理人派工）
- 票面落点：.scratch／tickets／2026-11-16-DEBTCLN-R1-ROOTCLN仓根散件迁册票-v1.md
- 来源与裁定依据：决策者（皮总）2026-11-16 20:15 令＝清债批次开张、仓根散件迁册列第一票（消息面指令·批次背景）。已坐实事实：仓根 .collab／ 直接平放一批过程件，违反桶结构闭集；闭集机检闸 check-collab-buckets（MC-BUCKET-1）已挂 run-gates（per_spec 23·CPPOOL 批次所立，收口 b2b61d7 台账在册）。
- 候裁点：**0 枚**（见 §四论证：桶归属按闭集白名单＋同线先例全部自决闭合）。

> **票面自注（防自咬体例）**：本票正文对一切路径仅叙述性提及＝裸文写＋全角斜杠（／U+FF0F），不落反引号路径指针；引用既有原文以 ⟦⟧ 标记。§二 施工命令块内＝落笔实文本（双引号包径·不含反引号 token·天然安全）。本票面成文后自靶 python share/check-pointers.py --root . --target 本票面实路径 须 exit 0（读数见 §七）。

---

## 〇、开工读数（起草轮现跑·禁抄旧数）

| 项 | 命令 | 实测读数 |
|---|---|---|
| 时点 | date '+%F %T %z' | 2026-11-16 20:17:33 +0800 |
| HEAD | git rev-parse --short HEAD | **2683594**（与派工预期值全等） |
| tracked 脏面 | git status --porcelain | 恰一枚 M＝agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl（他案脏面·禁碰禁入票） |
| untracked 全集 | 同上 | 仓根 .collab／ 平放 2026-11-12 系列 md 十二枚＋.collab／research／ 未入库 md 六枚＋仓根杂散五枚（.py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt）——合计 ?? 二十三行，全部不入声明闭集（清单见 §二之三） |
| 仓根 .collab／ tracked 平放散件 | git ls-files .collab／ 一级过滤 | **五枚 md**（逐一列名见 §二之一）＋README.md（桶索引件·名录内合法存续）；桶目录内 tracked 件共 216 枚零触碰 |
| 桶名白名单现读 | 读 share／check-collab-buckets.py 内嵌集＋.collab／README.md 名录行对拍 | 十七桶闭集＝decisions／audits／receipts／board／design／research／refs／evidence／inbox／process／dispatch／drafts／adr／architect／product／ledger／returns；README 名录行解析对拍＝一致 |
| 桶闸现跑 | python share/check-collab-buckets.py | **exit 0**·一级目录判 14 枚｜违例 0｜名录对拍一致 |
| 缺省指针钉值 | python share/check-pointers.py 缺省扫描 grep -c BLOCK／grep -c WATCH | **BLOCK 22810／WATCH 4581** |
| 全仓 GATE 钉值 | bash share/run-gates.sh | **GATE PASS exit 0·发现 151502**（三钉值全部与派工预期现跑全等） |
| 链上锚 | git cat-file -e <sha>^{commit} 逐枚 | fb76547／c79dde9／9ebc94f／883aa68／111b67a／b2b61d7／ca33b5f 全部在位 exit 0 |
| 目标桶撞名检查 | test -e 新路径逐枚 | 五枚目标名 .collab／decisions／ 下**全部不存在**＝零撞名 |

## 一、案件本体

仓根 .collab／ 一级平放五枚 tracked 过程件（2026-11-10／2026-11-11 落件的呈拍简报四枚＋收口登记一枚），属桶结构闭集违例面（一级平放＝非桶落位）。CPPOOL 批次已迁七枚桶存量并立新闸 check-collab-buckets；A14 迁册先例（defects 桶迁册＝票→git mv→回执→QA→收口五笔同构链）在册。本票＝清债批次第一票，把这五枚 tracked 平放件 git mv 迁入 decisions 桶，零内容改动。

**口径边界（写死）**：本票只迁 tracked 件；一切 untracked 散件未入库、归属需决策者或后续票定，本票仅 §二之三 知会清单，**不入施工声明闭集**。

## 二、清点、分流与施工规格

### 之二之一 · 五枚 tracked 平放件清点与桶归属分流

| # | 旧路径（仓根相对） | 件性质 | 新桶路径 |
|---|---|---|---|
| 1 | .collab／2026-11-10-SWB-SCRATCHG-双席审会师-放行呈拍简报-v1.md | 主理人呈皮总会师呈拍件 | .collab／decisions／2026-11-10-SWB-SCRATCHG-双席审会师-放行呈拍简报-v1.md |
| 2 | .collab／2026-11-10-候裁三件-呈拍简报-v1.md | 主理人呈皮总候裁呈拍件 | .collab／decisions／2026-11-10-候裁三件-呈拍简报-v1.md |
| 3 | .collab／2026-11-10-挂账清点-呈拍简报-v1.md | 主理人呈皮总挂账呈拍件 | .collab／decisions／2026-11-10-挂账清点-呈拍简报-v1.md |
| 4 | .collab／2026-11-11-SWB-SCRATCHCFG-放行呈拍简报-v1.md | 主理人呈皮总放行呈拍件 | .collab／decisions／2026-11-11-SWB-SCRATCHCFG-放行呈拍简报-v1.md |
| 5 | .collab／2026-11-11-SWB-SCRATCHG-收口登记-v1.md | 收口登记件 | .collab／decisions／2026-11-11-SWB-SCRATCHG-收口登记-v1.md |

**桶归属论证（全部自决·候裁 0）**：
1. decisions 在十七桶白名单内（闸脚本内嵌集与 README 名录行现跑对拍一致·§〇 在册）——新路径全部落闭集白名单，禁猜桶名条款满足＝桶名非猜、现读白名单。
2. README 桶总表 decisions 行 verbatim 含「收口登记」；呈拍简报归 decisions＝**同线先例**：COLLAB-STRUCT-1 迁移批（链 e49977a 段）即把仓根平放呈拍简报／收口登记同类件迁 decisions，现存 .collab／decisions／ 内呈拍简报同型件多枚在册（如 2026-11-04-SWB-ADR工序票-呈拍简报-v1／2026-11-06-PROJINIT-放行呈拍与四条待裁-v1 等）。
3. receipts 桶内呈拍简报先例＝FUXI 线件（U41／U42 系列），与本批 SWB 线不同线，不交叉引用；本批五枚均为 SWB 线呈拍／收口面，按同线同归。

### 之二之二 · 施工声明闭集（封顶＝六笔面·git mv 五＋配置随动一）

**S1 · 五枚 git mv（唯一移动面·命令 verbatim）**：

```bash
git mv ".collab/2026-11-10-SWB-SCRATCHG-双席审会师-放行呈拍简报-v1.md" ".collab/decisions/2026-11-10-SWB-SCRATCHG-双席审会师-放行呈拍简报-v1.md"
git mv ".collab/2026-11-10-候裁三件-呈拍简报-v1.md" ".collab/decisions/2026-11-10-候裁三件-呈拍简报-v1.md"
git mv ".collab/2026-11-10-挂账清点-呈拍简报-v1.md" ".collab/decisions/2026-11-10-挂账清点-呈拍简报-v1.md"
git mv ".collab/2026-11-11-SWB-SCRATCHCFG-放行呈拍简报-v1.md" ".collab/decisions/2026-11-11-SWB-SCRATCHCFG-放行呈拍简报-v1.md"
git mv ".collab/2026-11-11-SWB-SCRATCHG-收口登记-v1.md" ".collab/decisions/2026-11-11-SWB-SCRATCHG-收口登记-v1.md"
```

**S2 · 豁免快照随动一枚（配置面唯一改动·防自咬论证）**：五枚中仅枚 1 的旧路径 token 在 check-pointers 缺省扫描域（三分类目录）内有引用命中——agent-experts／baigong-software-team／.collab／qa／2026-11-10-SWB-SCRATCHG-产品席窄复核-v1.md 行 5 反引号包径引用枚 1 旧路径（当轮全扫描域穷尽 grep＝其余四枚旧 token 零扫描域命中·命中面全在仓根 .collab／ 与仓根 .scratch／＝非缺省扫描域）。现状该 token 经仓根候选解析存活零发现；git mv 后旧路径消失、后缀归位层对非 .scratch 索引命中 0＝新增恰一枚 BLOCK。链上史件禁回改（append-only），处置＝照 A14 先例既有机制（皮总裁定 ca33b5f §二-3「豁免清单入机检配置」所立历史件不改字豁免层＋快照件 items 6／7 同型旧路径 token 在册先例），向 share／baseline-pointer-exempt.json items 追加一枚条目：token＝枚 1 旧路径文本，files＝恰该窄复核件仓根相对路径一枚。追加后该枚落「历史豁免」WATCH 留痕行，不落 BLOCK。快照件仅 share／check-pointers.py 一闸消费（当轮 grep 坐实），其余闸零扰。

工程师施工笔＝S1 五 mv＋S2 一条目，**一笔面六件**（git diff --cached --name-only 坐实恰六）。

### 之二之三 · 未入库散件清单（仅知会·不入声明闭集·本票零处置）

- 仓根 .collab／ 平放 untracked md 十二枚＝2026-11-12 系列：主理人进度盘点／交接方本侧优化迭代分析判断／代办账登记-token-key日志异常待查／同一产品双实例外部协作交接机制缺口诊断／实践方外部Skill建议书（v1／v2／v3／v4／v5／v6／v7 七枚）／统一工单抽象本侧判断——归属需决策者或后续票定。
- .collab／research／ untracked md 六枚（2026-11-07／2026-11-08 GEO 与 LobeHub 系列）＝已在桶内未入库，非平放违例。
- 仓根杂散五枚＝.py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt。
- 以上全部**不在本票施工声明闭集内**；施工笔 git status 对它们零增零删零改即 V 系边界。

### 禁动面（写死）

- untracked 散件全集（§二之三）：零碰零入库零清理。
- agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl 之 M 态＝他案脏面：禁碰禁入票禁 add。
- FUXI 面（agent-skills／fuxi-skill／ 全域＋仓根 .scratch／ 内 FX 族）零触。
- 链上历史件内容零回改：五枚件本体＝纯移动零改字（git mv 保 blob）；被引用史件（含上述窄复核件）一字不改。
- 门禁面除 S2 快照一条目外零触：share／ 其余全部、路由表、桶闸本体零动；`.gitignore` 零动。
- 账本面（仓根与包内 ledger／leases）零手写；桶目录内既有 tracked 件（216 枚）零移动。

## 三、验收判据（全机械·命令＋钉值·禁凭记忆填值）

- **V0 开工读数**：施工轮现跑 HEAD＋git status 他案脏面清单照登＝与 §〇 形态一致（ledger 一枚 M＋?? 二十三行）。
- **V1 tracked 平放清零（tracked 口径）**：施工笔后 git ls-files .collab／ 一级过滤＝**仅 README.md 一枚**（现五枚散 md 全部消失于一级）；git ls-files .collab／ 总数 **222→217**。文件系统面 untracked 平放十二枚仍在盘＝口径使然，非违例。
- **V2 桶闸**：python share/check-collab-buckets.py → **exit 0**·一级目录判 14 枚｜违例 0｜名录对拍一致（与开工读数全等）。
- **V3 门禁钉值对拍（以本票落链后现跑 §七 读数为基线·禁凭记忆填值）**：施工笔后 bash share/run-gates.sh → **GATE PASS exit 0**；缺省扫描 grep -c BLOCK＝基线值**零新增**；grep -c WATCH＝基线值**＋恰 1**（新增行＝S2 豁免留痕行·文案含「｜历史豁免」标记·grep -c 历史豁免 相应＋1）；run-gates 发现总数＝基线＋1。基线读数落笔于 §七（本票落链后现跑），验收以当轮现跑复测对拍，任何其它摆动＝红。
- **V4 零内容改动**：施工笔 git show --name-status -M ＝**R100 恰五行**（rename 百分百相似＝纯移动零改字）＋**M 恰一行**（share／baseline-pointer-exempt.json）；M 件 diff＝仅 items 追加一条目（行数＋若干、既有条目零改）；git diff --cached --name-only（commit 前）＝恰六路径。
- **V5 边界**：施工笔 name-only 六路径全部落声明闭集（.collab／ 五枚旧新名＋快照件一枚）；禁动面 pathspec 域（untracked 清单／ledger／fuxi 面／.gitignore）git diff 零命中；他案脏面状态零变化。
- **V6 自靶**：票附回执靶检 python share/check-pointers.py --root . --target 回执实路径 → exit 0；本票面（链上现文）同式 exit 0 复证。

## 四、候裁面（必有节·**候裁 0 枚**）

随动裁量两项均自决闭合：① 桶归属＝decisions（白名单现读＋同线先例＋README 桶表 verbatim，无对立方案实质残余）；② 枚 1 旧 token 史引用处置＝S2 豁免快照追加（既有 A14 机制＋同型先例 items 6／7·裁定线内后果非新裁）。如双席审发现真分歧按程序单列另呈。

## 五、链衔接（同构 A14 五笔）

链第 1 步＝本票起草笔（架构席·本笔）。第 2 步＝双席快审（产品席＋QA 席 fresh eyes：审 S1 命令可照判性／S2 豁免论证可驳性／V 系可机械性）。第 3 步＝放行登记（主理人）。第 4 步＝工程师施工一笔（五 mv＋快照条目）＋回执一笔（落 .scratch／tickets／）。第 5 步＝fresh QA 按 §三 V 系独立验收判词。第 6 步＝收口登记（主理人）。

## 六、落链纪律段（各笔共守·写死）

- 单件／本笔面 pathspec 两端齐带（add 与 commit 各带本笔面路径）；add 紧邻 commit 零窗口；commit 前 git diff --cached --name-only 坐实仅自笔面。
- FX_COMMIT_DECLARE＝仓根相对纯路径清单（逗号或换行分隔）**挂 commit 命令侧**（环境变量前置挂 commit；挂 add 侧会被 STAGED-DECL-BLOCK 拦）。
- 禁 add -A／禁 amend／禁 --no-verify；message 以 collab: 起头·零 at 符号·零反引号；尾标置 message 最末位。**本票各笔尾标闭集**：本票笔 -TICKET／QA 快审笔 -QA-REV／产品快审笔 -PM-REV／放行登记笔 -PM-RELEASE／工程师施工笔 -BUILD／工程师回执笔 -RECEIPT／QA 验收笔 -QAV／收口登记笔 -GCLOSE（族名 DEBTCLN-R1 随尾标内嵌）。
- 一票一 commit 增量落盘；commit 类命令 timeout 600000ms；撞 index.lock 有界等待零删锁。
- 防自咬体例＝票面／回执正文路径裸文＋全角斜杠叙述形态；引文 ⟦⟧；票面与回执自身须过 check-pointers --target exit 0 后才可落链。
- 临时工作物只落仓根 .scratch／<席族>／ 族；本席起草笔只写票面这一件。

## 七、起草笔自证（落笔后、commit 前实跑）

- 开工读数＝§〇 全表（当轮现跑·HEAD 2683594 与派工预期全等）。
- 本票面自靶＝python share/check-pointers.py --root . --target .scratch／tickets／2026-11-16-DEBTCLN-R1-ROOTCLN仓根散件迁册票-v1.md → **exit 0**（实跑坐实）。
- 票在盘基线（V3 基线真身·票落盘后全闸现跑）：缺省扫描 **BLOCK 22810／WATCH 4581**（与开工钉值零摆动）；bash share/run-gates.sh → **GATE PASS exit 0·发现 151502**（与开工钉值零摆动）；check-collab-lint 分账 L1 2006／L2 4097／L3 0 零扰动；check-ticket-reconcile 票 148→149（本票入册 SKIP 缺声明 105→106·发现 184 零增）。EAC-L2 零起波＝票面体例字样无禁模式命中，实跑坐实。
- **V3 验收基线以本行为准**：施工笔后对拍＝BLOCK 22810 零新增／WATCH 4581＋恰 1（S2 豁免留痕行）／run-gates 发现 151502＋恰 1／桶闸 exit 0 形态不变；任何其它摆动＝红。
- 本笔面＝恰票面一件；其余全程零触碰；他案脏面零带入。
