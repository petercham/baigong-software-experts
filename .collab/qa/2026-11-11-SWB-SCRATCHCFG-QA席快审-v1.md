# QA-cfgrev · SWB-SCRATCHCFG config 租约随动微规格票 v1 QA 席快审 v1

- 审票席：QA 席 `qa-cfgrev`（fresh eyes·未读产品席 pm-cfgrev 并行产出——其件当轮仅见 staged 文件名一件照登零读零碰；本席只落自家判词）
- 被核物：`.scratch/tickets/2026-11-11-SWB-SCRATCHCFG-seat-config-lease-sync-ticket-v1.md`（落链 `a23ccd2`·129 行·`git log a23ccd2..HEAD -- <票面>` 命中 0＝起草后零触碰 ✓）
- 档位：**快审**（轻量维护档票·票面本体／链条面按 T10 轻量档射程申报注理由·照登合规）

## 〇、开工实测（本席当轮现跑）

- `date` ＝ `Wed Nov 11 07:46:54 2026`
- `git rev-parse HEAD` ＝ `5cba2ea967a439b1119de912b536582fcde2d7ea`（＝FX-U39 施工笔一改动原子笔·他案链上笔照登零碰）
- tracked 脏面＝2：`A .collab/qa/2026-11-11-SWB-SCRATCHCFG-产品席快审-v1.md`（产品席在飞笔·零碰零带入）＋`M agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl`（他案脏面·零碰零带入，本席 commit 全程 pathspec 限定）
- 依据锚 `282f88f／9278445／ca33b5f／a23ccd2` `git cat-file -e` 四枚全在位 ✓；`ca33b5f` §二-1 随裁(e) 原文实读＝「取 B-i（迁回执桶）＋随动硬约束＝工程师租约禁动面随动」✓

## 一、机理复核结论（本席独立读守件源码＋只读探针——起草席「机理钉死」声明三态判定）

| # | 起草席声明 | 本席独立取证 | 三态 |
|---|---|---|---|
| M1 | write-guard `glob_match`（L152–178）消费词汇**无机械否定语法** | 现读函数体全 26 行：仅＝全角括注剥离（L153）→CJK/∪−描述行不参与匹配（L157）→`**`/`*`/`?`/字面转义四分支，无任何否定／例外／`!` 分支 | **属实** |
| M2 | 全角括注经 L153 剥离后**零机效变化**（host 行成例） | 探针 a：替换行 `strip(rep)≡".collab/receipts/**"` 逐字相等＝True；探针 b（host 成例直跑 write-guard）：host 行现值（docs 星号加括注成例）对包根 docs 下 PRODUCT 件（实面 `agent-experts/baigong-software-team/docs/PRODUCT.md`）→ deny 命中、对 docs 下 adr 子目录假想件 → 不命中＝括注语义零机效、机效仍 docs 单层星号 | **属实** |
| M3 | `decide()` 先 deny_globs（L261–266）后租约面（L268–274） | 现读 `decide()` 全函数：deny 枚举循环在前、leases 加载匹配在后，命中 deny 即 return | **属实** |
| M4 | 推论「deny 单点除外不可 glob 达成（不改守件）」 | 探针 c：替换行对桶内目标件与桶内他件均仍命中（`gm=True/True`）＝除外未达成；结合 M1 词汇闭集＝两 config 内无达成手段 | **成立（票基础论证不塌）** |
| M5 | rename 通道不在写钩子消费链（S1-c 口径） | 包级 hooks 登记件（实面 `agent-experts/baigong-software-team/hooks/hooks.json`）L13 写钩 matcher 闭集＝`Write\|Edit\|MultiEdit\|Write to file\|Modify a file`——Bash 内 `git mv` 不经 write-guard | **属实** |

**票 §二 机理写实段整体复核＝与守件源码全等，无夸大无走样。**

## 二、V 判据现跑读数表

| 判据 | 票钉 | 本席现跑 | 判定 |
|---|---|---|---|
| V0 基线 | s4 直跑 exit 0·13 PASS（含 t13）；BLOCK＝**22833** | s4 exit **0**·PASS 行 **13**·`PASS t13_derived_consistency`＝**1**（`.scratch/qa-cfgrev/s4-run.log`）；`check-pointers\|grep -c BLOCK`＝**22833** 与钉值**逐字全等** | ✓ 钉值全部复现 |
| V1 前值 | 前值 0 | 两 config `grep -c "B-i 迁件目标单点除外"`＝**0/0** | ✓ |
| S1 逐字性 | 替换行对现盘行现读对拍 | 两文件 engineer `deny_globs` 第 9/22 项＝`".collab/receipts/**"` 逐字在场（python json 现读，位次与票 §一 全等）；替换串无 JSON 破壁字符、可照录 | ✓ |
| V2 派生面 | t13 逐行相等强约束 | t13 断言实读 L271–272＝各席 `deny_globs` 列表逐行相等；两文件 engineer deny 表现值逐行全等（json 对拍）；两 JSON `json.load` exit 0 | ✓ |
| **V3 探针** | 前跑 reason 含 `glob='.collab/receipts/**'`；后跑**同 reason 字符串逐字全等** | **两缺陷实跑反证**（见 §三红-1） | **红** |
| V4 签发面 | 0→0·`wc -l`＝7·禁手写反证 | `grep -ci scratchg leases.jsonl`＝**0**、行数 **7** ✓；强化面：`"SCRATCHCFG-test"` 对 `grep -ci scratchg`＝**0**＝SCRATCHCFG 字样不含 SCRATCHG 子串，未来随票签发不会假污染 V4 计数 | ✓ |
| V5 | config json 不入扫描面 | `check-pointers.py` 扫描面＝`iter_markdown` 仅 `.md`（L285–297 实读）；两 config `--target` 直跑 exit 0 旁证 | ✓ |
| V6/V7 | 回执靶检可跑 | 判据随回执名执行＝可跑形态 ✓；`run-gates.sh` 可跑（本席未重跑全门＝快审档，读数归施工/验收轮） | ✓（可跑性） |
| S3 签发定性 | SCRATCHG 补签必 REJECT | lease-issuer **只读探针（--leases 重定向 .scratch 临时件）**：`--ticket SCRATCHG --seat engineer --path-glob ".gitignore" …` → **exit 2 REJECT**「请求路径越出席位 engineer 写域行」；countersign 硬闸 L110–115 实读 ✓＝「状态机面非人工件」写实 | ✓ |
| S2 体例澄清 | 收口登记 §四口径照录 | 双轨并存／(h) 管免忽略豁免面·B-i 管存量单件＝与收口登记 §四＋QA 判词 §五 三处对照无走样 | ✓ |

## 三、红黄台账

- **红-1（V3 判据自我矛盾＋探针路径锚错位，措辞级窄修可销）**：
  1. **reason 逐字全等式不成立**：deny reason 由 L266 `glob={g!r}` 嵌入**原样 pattern 字符串**（非剥离后值）——施工后 config 值即替换行本体（含括注），reason 必随 S1-a 措辞变化，「后跑同 reason 字符串逐字全等」对正确施工也必假红。零机效变化的正确机械表达＝**前后均命中 deny_globs 归属分支（reason 前缀 `路径∈deny_globs` 不变）＋决策 deny 不变**，glob 字段则应＝替换行逐字段。
  2. **路径锚式跑不通**：本仓仓根无 swb-anchor 锚定声明件、无 docs 目录下 STRUCTURE 结构件（现盘实测两缺）→ `project_root()` 落回包根、权限字面读作**包根字面**；照票 --path 式（全仓根路径 `agent-experts/baigong-software-team/.collab/receipts/…`）直跑 → reason＝「路径∉当席租约」形态，**deny_globs 分支根本不进**——票钉前跑读数「含 glob='.collab/receipts/**'」在当轮现盘不可复现（且此错位使前跑即已＝b 式形态，探针失去判别力）。修正＝--path 用包根字面 `.collab/receipts/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md`（本席以此直跑 → deny reason 恰含 `glob='.collab/receipts/**'` ✓ 复现票钉），或显式 `SWB_REPO_ROOT` 锚定并随登两式读数。b 式（甲裁）预登记在包根字面式下判别成立，无需改。
- **黄-1（本票租约段自身必 REJECT，一句勘正可销）**：§六 path_globs 第二项 `.scratch/tickets/2026-11-11-SWB-SCRATCHCFG-*` 经 lease-issuer 子集校验（L129–132）＝**直跑 exit 2 REJECT**（不在 engineer `write_globs` 任何行）；`agent-experts/baigong-software-team/config/**` 单项 → **exit 0 可签发**（票注「config 子集校验可过」实证 ✓）。本票 S3 对 SCRATCHG 揭同款缺口，自家租约段却把必拒 glob 列入实例化请求面＝内部不自洽。勘正＝请求面只留 config 两件 glob，票附回执落位按 (h) 体例＋dev 态无物理拦截先例登记（或注明此 glob 不入子集校验）。甲裁亦不解此项（甲加的是 receipts 行非 .scratch 行）。
- **观察-1**：「禁拆两笔防 t13 中间态红」——判据本体（两 config 同批一笔·声明闭集封死拆笔形态）正确且必要（t13 对**工作树文件**直读相等，拆笔中间态恰是咬合面）；但 `run-gates.sh` 内无 s4/test_enforcement（grep 零命中）＝「中间态红」非门禁自动承载，系人工跑位承载。判据保留，措辞勿暗示门禁自动拦。
- **观察-2**：lease-issuer 写域校验票引 L123–127，实段 L123–133（domain 取值＋循环 REJECT）——引用精度级，不须动。

## 四、§七候裁机效陈述（不代裁·如实呈）

甲乙丙三式机效差异呈述与本席独立读数**全等无失真**：
- **乙（缺省）**＝两 config 零结构改动（纯措辞＋注记）；现状 deny 桶级拦＝后续写入 engineer 不可达；SCRATCHG 补签永久 REJECT（§二探针 exit 2 实证）；迁件动作经 rename 不受拦（M5 实证）＝已裁(e) 语义最小兑现。
- **甲**＝engineer deny 让出 receipts 父桶＋`write_globs` 加行（两 config 两行联改·t13 必同批）；V3 换 b 式在包根字面路径下可跑；签发链解锁但 engineer 经租约可及**整桶**＝超「单点」语义＝治理决策属实；纵深减层先例（returns/inbox/drafts 让出成例·两 config note 在册）转录如实。
- **丙**＝守件消费链扩否定例外键＋tests/s4 扩展＝另案，超本票三件封顶——三件闭集（两 config＋票附回执）自洽。
起草席倾向乙＝其机效陈述无夸大；本席不表态归裁。

## 五、总裁决

**红 1／黄 1／绿（V0·V1·S1 逐字·V2·V4·V5·S3·S2·M1–M5 机理面全绿）**——**不放行（窄修后可径放）**：红-1（V3 判据两缺陷）＋黄-1（租约段 tickets glob）均为措辞级单句修，不摇 S1 措辞随动本体、不摇「零机效变化」主论证（该论证独立复核为真）、不摇 S3 状态机定性（实证）。修后可径放免复审轮。

## 六、纪律自证

- 只读审票：除本判词外零改动；探针全程 `--ledger/--leases/--freeze-state` 重定向 `.scratch/qa-cfgrev/` 临时件，`leases.jsonl`/`ledger.jsonl`/两 config/守件/tests 零碰（V4 面 mtime/行数＝7 未动）。
- 临时工作物＝仓根 `.scratch/qa-cfgrev/`（s4-run.log＋探针 out/err/log 诸件），完工自删附 ls 读数（§4.4-A-2 消费面沿用）。
- 他案在飞面（FX-U39 施工笔群、pm-a14rev/qa-a14rev、A14 rev 票面、ledger 脏面、pm-cfgrev staged 判词件）照登零碰零带入；fresh eyes＝产品席产出未读。
- commit＝`collab:` 前缀·pathspec add/commit 两端齐带·FX_COMMIT_DECLARE 声明本笔面·紧邻无窗口·message 零 at 符号字符·禁 add -A/amend/--no-verify·输出重定向 `.scratch/` 落盘·commit 调用 timeout ≥ 十分钟·撞锁有界等待 30s×10 零删锁·落笔前靶检 `--target 本件` exit 0·完工 `git show --name-only HEAD` 恰一件自证。
