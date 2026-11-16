# DEBTCLN-R4 · QA 席独立验收判词 v1（fresh eyes·票 §三 V 系＋放行登记 §二 口径·全现跑）

- 案名＝DEBTCLN-R4 S2RULE 真源句补立施工批（BUILD 172fa7254dc62b7f5028ab700e18cf737f3a5240 ＋ RECEIPT 2ce120b272de9bd06200b96173b9afab191987a8）
- 审票依据＝.scratch／tickets／2026-11-16-DEBTCLN-R4-S2RULE真源句补立票-v1.md（§三 V 系原文现读·票面链上 blob 现跑复验＝317ff37213461c45a1e4bda03f33913123d00e08 与派工预期全等·无 rev）＋.collab／decisions／2026-11-16-DEBTCLN-R4-放行登记-v1.md（§二 口径写死项逐条照办）
- 验收席＝QA 席 qa-debt4v（fresh 实例·独立于施工席与起草席）·全部读数本席当轮现跑，禁凭记忆项零违例
- 体例自注（防自咬）：本件对一切路径仅叙述性提及＝裸文写＋全角斜杠（／U+FF0F）·零反引号·零 at；引用既有原文以 ⟦⟧ 标记；本件落笔后 commit 前自靶 python share／check-pointers.py --root ． --target 本判词实路径 → exit 0（读数见 §六）

## 〇、开工读数（当轮现跑·禁抄旧数）

- 时点＝date 实测 2026-11-17 07:02:03 ＋0800。
- HEAD 现跑＝**2ce120b**（＝RECEIPT 回执笔＝链顶·与派工预期全等）。链序核对＝62f9211 放行登记 → 172fa72 BUILD → 2ce120b RECEIPT，git log 62f9211..2ce120b 区间恰两笔·外案插笔零起＝并发窗对本批两笔零发生。
- git status --porcelain 当轮读数＝tracked 脏面恰一枚 M＝agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl（他案）＋?? 仓根／.collab 平放群当轮 24 行（2026-11-12 系列＋.collab／research／＋仓根杂散·活体群计数照登禁钉死）——全部他案脏面·零带入零 add 零清理禁扩集，与派工预期形态一致。
- .git/index.lock＝不存在（开工实测）。
- 票面链上 blob 复验＝317ff372 全等；回执链上 blob 现跑＝905553b2b4fcf193d841b7f23c0bf0eeb663e3a1（派工未钉回执 blob·照登）。
- 靶件改后三面净态＝盘＝链＝工作区（git status 对靶件路径零命中）；链上 blob＝6ec1a37bcff229e204a2c62f8a62cecc151106fe（git rev-parse 172fa72 面现跑）。

## 一、V 系逐判（全机械·本席现跑）

- **V1 真源句落位＝绿**。新 token「交接件体例三律②·真源句」python 计数靶件盘态＝**恰 1**；基线（git show 62f9211＝施工笔父笔链上态）＝**0**；行 30 定位钉 sha256 前缀逐行 python 实算＝行 28 a8f00e1e／**行 30 f561c696 不变**／行 62 2c588686／行 66 731e8d8f＝四钉改后全合＝行 30 及锚点行 byte 零触坐实；python share／check-pointers.py --root ． --target agent-skills／multi-collab／references／20-handoff.md（**真径**·放行 §二-2 口径）→ **exit 0**。
- **V2 append 单行判据＝绿**。git show --numstat 172fa72＝**1／0** 纯 append 零删除；git show --name-status 172fa72＝**M 恰靶件一枚**；票 §三 V2 对拍命令 verbatim（基线按放行口径置换为链上父笔 62f9211）→ **exit 0** 打印 **CHANGED [] LEN 66 67**＋**L67 d7c97f79717c85c86b5cdac768dae937c952695edee0eafdf00db30043690b42** 与票 §二 钉值全等；新行字符数 **203**；链上 blob 现跑＝**6ec1a37b** 与仿真钉版全等；盘态 sha256（CRLF 面口径）现跑＝**3e5373c2**52f987698a7bd2ff1eb23b30d4cb6f2f472d0d7280ae316b039e0261 与仿真钉版全等；CRLF 枚数＝python 字节级实测 **67 枚**（66→67 随动·新行行尾 CRLF 随靶件；Git Bash 下 grep 对行尾回车计数恒 0 系工具伪读数，本席未采）；CHANGED 文件集＝链上区间 [20-handoff.md, 回执件]，其中靶件面单恰靶件。三口径注明：盘 CRLF 面值／blob LF 值／新行 UTF-8 无行尾值——本判词全部钉值带口径。
- **V3 消费面零变化＝绿**。check-collab-lint 现跑 **exit 1**（全扫描基线真值·含 ignored 取证族历史落盘面·advisory 不碍 GATE·非施工回归）·计数＝spec EAC-L1 **2006**／EAC-L2 **4097**／EAC-L3 **0**·分账 EXEMPT 0／SUBSTR 1029／VIOLATION **4097**·--selftest **exit 0**（脚本本体健康）；check-source-of-truth 现跑 **exit 0**·读数＝模式 dual｜文件 129｜BLOCK **0**｜基线豁免 **54**（WATCH）｜指针 WATCH **413**——与放行 §〇 基线全等。差量归因＝本席对 62f9211 前态做**盘上就地置换**对照（链上父笔 LF 字节经 CRLF 随动重建→盘 sha256 现跑＝68b5de7c 与改前基线值全等＝置换自证；三扫描改前跑毕→还原现态→还原 sha 现跑＝3e5373c2 与改后值全等＋git status 对靶件零命中三面坐实）：**lint／csot／缺省指针扫描 改前改后输出全文 diff 各＝0 行＝findings 零新增**；靶件在 lint 输出面命中＝**0 枚**（新行反引号 0／盘符斜杠 token 0／at 0 逐字符实测＝零自咬）。reconcile 行 375 注释零改（两文件未入两笔面＝name-status 坐实）。
- **V4 缺省扫描与门禁＝绿**。check-pointers 缺省扫描 grep -c BLOCK＝**22809**／grep -c WATCH＝**4582**＝**双零变化**（改前置换态同值＝双态实证）；60-gates.md 行 110 BLOCK **改前改后各恰一枚在册零变化**＝零触归因（该枚活体悬空续候另案·见对抗臂-3）；fuxi 树副本面零变化＝FUXI 零碰归因（链上两笔面单零 fuxi 件坐实）；bash share／run-gates.sh → **GATE PASS exit 0·发现 151502** 当轮现跑照登（与基线全等·禁钉死口径执行）。
- **V5 自靶＝绿**。链上票面 --target → **exit 0**；回执件 --target → **exit 0**；本判词面自靶见 §六。
- **V6 笔面单恰靶件＋钩子互证＝绿**。口径照 R2 收口 §四 终版：BUILD 笔 git show --name-status＝恰靶件一枚 M；RECEIPT 笔＝恰回执一枚 A；两笔 commit message 均含 **STAGED-DECL staged 1｜声明 1｜超额 0** 钩子互证在册；链上区间 62f9211..2ce120b 全域变更面单＝恰｛靶件，回执｝两枚＝并发窗零裹入（D-58 三面互证无需启用）。

## 二、对抗臂（fresh eyes 必做·全过）

1. **新行对榫票 §二 展示块**＝程序化对拍（票 ```text 围栏内行 vs 链上 172fa72 面行 67）＝**逐字全等**（sha256 双 d7c97f79 前缀·LEN 203＝203）；剥反引号口径以程序对拍命令为准绳（本臂即该程序对拍本身）。
2. **版本账零动复验**＝agent-skills／multi-collab／SKILL.md frontmatter version 现读＝**4.11 未 bump**；90-changelog.md 末行仍 v4.11（2026-11-05 ADR-L0 条目）＝**本批零新条目**；两文件链上 62f9211..HEAD diff＝**空**＝未入笔面。先例实物同案同判（0da2566／80e8612 零 bump·放行 §三 采纳留痕在册）。
3. **60-gates.md 行 110 同族第二例零触坐实**＝该件行 110 现读＝MC-SEAT-DECL 行（依据列含 handoff-discipline.md 仓根旧径指针）现位在册；缺省扫描改前改后各恰一枚 BLOCK（OA-D6 指针悬空＝该枚·指向 deliverables／experts／…／handoff-discipline.md 目标不存在）＝本票零触＝该债候另案候补池，不在本票射程（票 §四 观察行口径）。
4. **.scratch／debt4／ 临时面零残留**＝ls 实测＝**不存在**（工程师回执 §四 宣称「用毕即拆」兑现坐实；本席取证族 .scratch／debt4v／ 用毕即拆见 §六）。
5. **并发窗口径**＝本区间链上仅两笔、面单零他案件＝无需启用 D-58 三面互证；回执笔 message 尾部自登案型＝首发 commit 遭 SIGPIPE 中断未落链、staged 面完好＋锁零残留两面坐实后直投重投、锁前钩子两度在册＝链上登记可查、链态终值无损伤（2ce120b 恰回执一枚），不构成违例。
6. **新 token 全域分布核查**＝tracked 全域 git grep 于 2ce120b：靶件恰 1＋票面 4＋双席判词与放行与回执各 1～2＝全部为登记面引文；盘态 untracked 面命中＝判词旧件＋本席取证备份（debt4v 内 target-current-backup.bin·用毕即拆）＝零规范面扩散零第二落点。

## 三、结论

- **IS_PASS**。红 **0**／黄 **0**／绿 **V0～V6 七判据＋对抗臂六目全绿**。
- 关键读数定格（现跑）：缺省 BLOCK 22809／WATCH 4582 双零变化；GATE PASS exit 0 发现 151502；lint exit 1（EAC-L1 2006／EAC-L2 4097／EAC-L3 0·VIOLATION 4097）＋selftest exit 0；csot exit 0（BLOCK 0／豁免 54／指针 WATCH 413）；靶件改后 blob 6ec1a37b／盘 sha 3e5373c2（CRLF 面）／新行 sha d7c97f79 三钉全等；行 30 定位钉 f561c696 零触。
- 观察随登（不立项不候裁）：①本席 V3 差量对照采「盘上就地置换＋sha 自证」式（68b5de7c↔3e5373c2 双向自证＋status 零命中复原三面坐实）——与 R3-QAV 先例同法，未采隔离副本（放行 §二-2 伪差异口径天然规避）；②60-gates 行 110 观察行三度续登候另案；③三口径纪律两案延续良好。

## 四、禁动面独立核（本席现跑）

- 靶件既有 66 行 byte 零扰动＝V2 CHANGED [] 独立复算坐实（含行 24 R3 清偿态／行 28 节题／行 30 引律句／行 62 节题／行 66 投递分件条）。
- 版本账两文件链上零 diff；60-gates 零触；fuxi 与 evidence 备份面未入笔面；ledger M 态＋?? 全集他案脏面未入任何笔；链上史件零回改（62f9211 以前链面本席未检改动＝链序两笔区间面单已闭）；.gitignore 未入笔面。

## 五、回执宣称值三面独立对账

- 回执 §二 宣称值（token 1／0，numstat 1/0，CHANGED []，L67 d7c97f79，blob 6ec1a37b，盘 3e5373c2，CRLF 67，203 字符，BLOCK 22809／WATCH 4582，GATE 151502，lint／csot 计数全套）＝本席独立现跑**逐项全合**；回执 §四 案型（撞锁未遇／SIGPIPE 首发中断重投／CRLF 随动）＝链上 message 与链态可对账无矛盾。

## 六、本笔自证（落笔后、commit 前实跑）

- 本判词面自靶＝python share／check-pointers.py --root ． --target .collab／audits／2026-11-16-DEBTCLN-R4-QA独立验收判词-v1.md → **exit 0**（实跑读数随完工回报）。
- 取证族＝.scratch／debt4v／（lint／csot／ptr 改前后快照＋selftest＋gates＋自靶输出＋置换备份件）·用毕即拆＝本笔落链后随完工回报拆除。
- 纪律面＝本笔面恰本判词一枚（add 单 pathspec·add 紧邻 commit·commit 前 git diff --cached --name-only 坐实恰一枚·FX_COMMIT_DECLARE 挂 commit 命令侧）；尾标 -QAV 置 message 最末·零 at 零反引号；他案脏面零带入；链上史件零回改；FUXI 零碰；账本零手写；撞 index.lock 如遇＝按有证删锁先例如实登记案型。
