# DEBTCLN-R1 · 仓根散件迁册施工批 · QA 席 fresh eyes 独立验收判词 v1

- 判词件：．collab／audits／2026-11-16-DEBTCLN-R1-QA独立验收判词-v1.md
- 审计对象：施工笔 5838f3c（BUILD·五 mv＋快照一条目）＋回执笔 edf18ba（RECEIPT·落 ．collab／receipts／）
- 验收基准：链上票面 b2bceb8 态（blob eeb7719c527ffbcf50e03042b9b22a951c8dc8a0·119 行实测）之 V 系＋放行登记 0e7cf4c 态（blob c53384e983b35769153a6c6401b4f5435354e95d）§二-1 修正口径与 §四 钉值表
- 审席：QA 席 qa-debt1v（fresh 实例·经主理人派工·未读工程师席思路·只以盘面实测＋链上规格对拍）
- 体例：本件路径叙述一律裸文＋全角斜杠（／U+FF0F），命令块内双引号包径，不落反引号包径；命令读数全为本席当轮现跑，禁抄旧数。

## 〇、开工读数（本席验收轮现跑）

| 项 | 命令 | 本席实测 | 预期/钉值 | 对拍 |
|---|---|---|---|---|
| 时点 | date 现跑 | 2026-11-16 23:0x +0800 | — | 轮次差·正常 |
| HEAD | git rev-parse --short HEAD | edf18ba | 派工预期 edf18ba | 全等 |
| 票面钉版 | git ls-tree b2bceb8 对票面路径 | blob eeb7719c527ffbcf50e03042b9b22a951c8dc8a0；git show 版 wc -l＝119 | 钉值 eeb7719c…／119 行 | 全等 |
| 放行登记钉版 | git ls-tree 0e7cf4c 对登记路径 | blob c53384e983b35769153a6c6401b4f5435354e95d | 钉值 c53384e9… | 全等 |
| tracked 脏面 | git status --porcelain | 恰一枚 M＝agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl | 他案脏面照登 | 形态合 |
| untracked | 同上 grep -c ?? | 23 行（平放十二＋research 六＋杂散五） | 票 §二之三 清单 | 形态全等 |
| 并发面 | git worktree list 实文本 | 主 worktree 外两枚他案残留＝C:／Users／peter／AppData／Local／Temp／qa_t10_dy（prunable）＋D:／cs1-wt | 放行登记 §〇 照登清单 | 全等·本席零触碰 |
| 链序 | git log --oneline | 2683594→b2bceb8 票→4cfeb31 产品席→b5564a1 QA 主笔→18c41b0 QA rev1→0e7cf4c 放行→5838f3c 施工→edf18ba 回执 | 链上史件链序 | 相符 |

pre 态基线由本席自建隔离 worktree（0e7cf4c 态）亲跑坐实：git ls-tree -r 0e7cf4c 计数＝总数 225／一级文件 6／桶内 219（与放行登记 §二-1「本登记落链后 pre＝225／6／219」全等）。该 worktree 用毕即拆，拆后 git worktree list 复跑＝与开工照登清单全等＝零残留坐实。

## 一、V 系逐项 pre／post 读数表（修正口径）

| 判据 | 钉值（放行登记口径） | pre 亲跑 | post 亲跑 | 判定 |
|---|---|---|---|---|
| V1 总数 | 不变（pre 225） | 225（0e7cf4c ls-tree -r） | 225（5838f3c ls-tree -r）；HEAD 态 226＝回执件入桶链增·口径内 | 绿 |
| V1 一级过滤 | 恰 README.md 一枚 | 6（五散 md＋README） | 恰 README.md 一枚（5838f3c 与 HEAD 两态均坐实） | 绿 |
| V1 桶内 | pre＋5 | 219 | 224（5838f3c）；HEAD 225＝回执链增 | 绿 |
| V2 桶闸 | exit 0·一级目录判 14｜违例 0｜名录对拍一致 | （票/登记在册） | python share/check-collab-buckets.py＝exit 0·14 枚｜违例 0｜一致 | 绿·形态不变 |
| V3 缺省扫描 BLOCK | 22810 零新增 | 22810（放行登记亲跑在册） | 22810（HEAD 现跑 grep -c BLOCK） | 绿·零增 |
| V3 缺省扫描 WATCH | 4581＋恰 1 | 4581 | 4582（＋恰 1） | 绿 |
| V3 历史豁免行 | 6＋恰 1 | 6 | 7（＋恰 1·新行＝窄复核件行 5 落 WATCH「｜历史豁免（token＋文件集合）」留痕·不落 BLOCK·逐枚列名核对＝其余六枚全为既有 defects 桶消解豁免行） | 绿 |
| V3 全仓 GATE | GATE PASS exit 0·151502＋恰 1 | 151502（放行登记亲跑在册） | bash share/run-gates.sh＝GATE PASS exit 0·发现 151503 | 绿 |
| V4′ handoff 靶 | 恰一枚行 24 悬空·零新增 | 隔离 worktree 0e7cf4c 缺省扫描中该件行 24 恰一枚 BLOCK 在册 | --target agent-skills/multi-collab/references/20-handoff.md → 恰行 24 一枚 BLOCK（handoff-discipline.md 悬空）·零新增 | 绿 |
| V4 name-status | R100 恰五行＋M 恰一行 | — | git show --name-status -M 5838f3c＝R100 恰五行＋M 恰一行（share/baseline-pointer-exempt.json）·其余零卷入 | 绿 |
| V4 迁的闭集 | 票 §二之二 S1 声明五枚 | 链上票面逐枚列名 | 五对 rename 旧路径名逐枚全等＝双席审会师-放行呈拍简报／候裁三件-呈拍简报／挂账清点-呈拍简报／SWB-SCRATCHCFG-放行呈拍简报／SWB-SCRATCHG-收口登记（新名＝旧名入 decisions 桶） | 绿 |
| V4 JSON diff | items 追加恰一条目·既有条目零改 | — | diff＝仅 ＋6 行一对象追加；json.load OK（items＝10）；条目 token＝.collab/2026-11-10-SWB-SCRATCHG-双席审会师-放行呈拍简报-v1.md·files＝恰 agent-experts/baigong-software-team/.collab/qa/2026-11-10-SWB-SCRATCHG-产品席窄复核-v1.md 一枚＝票 S2 verbatim 对拍全等 | 绿 |
| V5 ledger | 仍 M·未入本批任何 commit | M | post git status 仍恰一枚 M；git show --name-only 两笔 grep -c ledger＝0 | 绿 |
| V5 ?? 面 | 二十三行形态未动 | 23 | 23·两笔 commit 零卷入 | 绿 |
| V5 FUXI 面 | 零触 | — | 两笔 name-only grep -c fuxi＝0 | 绿 |
| V5 链上史件零回改 | 四枚 blob 恒定 | b2bceb8 票 eeb7719c／4cfeb31 产品判 619fb945／18c41b0 QA判 cc788e9／0e7cf4c 登记 c53384e9 | HEAD 态 ls-tree 四枚 blob sha 与上述逐枚全等 | 绿 |
| V6 回执读数对盘 | 宣称＝实跑 | — | 见 §二 | 绿·零不实 |
| V6′ 自靶复证 | 票面链上现文 --target exit 0；回执件同式 exit 0 | — | 票面靶 exit 0；回执件靶 exit 0（本席现跑） | 绿 |

## 二、V6 回执宣称读数逐项对盘

回执（.collab/receipts/2026-11-16-DEBTCLN-R1-施工回执-工程师席-v1.md·edf18ba）宣称读数与本席亲跑逐项对拍：

- 开工 HEAD＝0e7cf4c＝链上放行登记 sha：链序坐实。合。
- pre 计数 225／6／219：本席 ls-tree -r 0e7cf4c 独立复算＝225／6／219。全等。
- post V1 225／README 一枚／224：本席 ls-tree -r 5838f3c 复算全等。合。
- post 三钉值 BLOCK 22810／WATCH 4582／历史豁免 7／GATE 发现 151503：本席 HEAD 现跑四项全等。合。
- post R100 恰五行＋M 恰一行＋JSON 仅 items 追加一条目：本席 git show 复跑全等。合。
- handoff 靶行 24 恰一枚零新增：本席 --target 复跑全等。合。
- 桶闸 exit 0·14｜0｜一致：本席复跑全等。合。
- 并发面宣称未自建临时面零残留：本席开工照登清单＝放行登记照登清单＝回执开工清单三态全等坐实。合。

结论：回执宣称零不实、无硬凑痕迹。

## 三、对抗臂（四发）

- 臂① 工作区残面：git diff HEAD --name-only＝仅 ledger 一枚（他案脏面）＝工程师未留未提交残面。命中 0。
- 臂② 豁免条目越权抽查：新条目全文 grep BLOCK＝False（豁免行零 BLOCK 字样）；token 只覆盖枚1 旧路径一枚；files 恰窄复核件一枚＝无宽免扩面。命中 0。
- 臂③ rename 逐字节等值：三枚（双席审会师呈拍／挂账清点呈拍／SCRATCHG 收口登记）git show b2bceb8 旧路径 vs git show HEAD 新路径 sha256 全 match＝纯移动保 blob 坐实（超 ≥2 要求）。命中 0。
- 臂④ commit 卷入面：5838f3c name-status 恰六路径（5 rename＋1 JSON）＝恰声明闭集；edf18ba name-only 恰一枚＝恰回执件。零卷入他面。命中 0。

对抗四发零命中。

## 四、回执 §五 口径差定性（供收口登记定夺）

实况溯源（本席现跑 grep）：票 §五 写「回执一笔（落 ．scratch／tickets／）」；放行登记 §三 同样写「回执笔落 ．scratch／tickets／」——两处文本一致，并非放行登记写死 receipts 桶；实际派工令写死 ．collab／receipts／，工程师按派工令落位 receipts 桶。

本席定性：先例面压倒性支持 receipts 桶＝同族迁册先例（defects 桶消解回执·链 9ebc94f）在册 ．collab／receipts／，近批次 BKTCLS／RCTPATH-R2／RCTPATH-R3／A14H1 等施工回执全部同桶在册（git ls-files 坐实）；.scratch／tickets／ 实为本票票面落位，票 §五 该句疑系与票面落位混写＝笔误级，放行登记 §三 系随引未勘。工程师落位 receipts 桶＝符合桶闭集（decisions 等十七桶白名单内合法桶）＋同族先例＋派工令，结果合规无需回改。建议收口登记就此勘正一句口径（回执落位以 receipts 桶为准），随放行登记黄面一并消化。非阻断。

## 五、红黄绿计数与结论

- 红：0
- 黄：1＝回执落位口径差（§四·票 §五＋放行登记 §三 随引笔误级·工程师按派工令＋先例落位合规·留收口登记勘正一句·非阻断）
- 绿：V1（三子目）／V2／V3（四子目）／V4′／V4（四子目）／V5（四子目）／V6／V6′ 自靶＋开工读数钉版面＝判定面全绿；对抗臂四发零命中

**结论行：IS_PASS**——施工批 5838f3c＋回执笔 edf18ba 全判据（修正后 V 系＋放行登记钉值表）pre/post 亲跑对拍全合，豁免链落地且零宽免，rename 逐字节等值，边界零卷入、链上史件零回改，回执读数零不实；唯一黄项为回执落位口径文本差，合规落位、留收口勘正，不构成返工。

## 六、本笔自证

- 本笔面＝恰本判词件一件；add 与 commit 各带本笔 pathspec；commit 前 git diff --cached --name-only 坐实仅自笔面。
- 临时面：取证用隔离 worktree（0e7cf4c 态）用毕即拆·复照零残留；临时读数文件居仓根 ．scratch／ 用毕即删。
- 他案脏面（ledger M＋?? 二十三枚＋两枚他案 worktree）全程零触碰零带入。
- 本笔落链前自靶：python share/check-pointers.py --root . --target ．collab／audits／2026-11-16-DEBTCLN-R1-QA独立验收判词-v1.md → exit 0（实跑随完工回报）。
