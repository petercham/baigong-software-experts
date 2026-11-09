# 迁册票-defects桶消解 施工批 · QA席独立证伪验证 v1（fresh eyes·只读·八判据）

- 验证席位＝QA席 qa-mvdefv；被验对象＝工程师席 eng-mvdef5 两笔：笔1＝c79dde9（迁册笔）＋笔2＝9ebc94f（回执笔）。
- 执行依据票面＝.collab/decisions/2026-11-09-迁册票-仓根defects桶违闭集-v1.md（落链笔 fb76547·票面 blob 89e9824a9985348d51b7a1fc450bdfe6da44b426 复点现盘全等＝票面未改）。
- 裁决口径（主理人已裁·本件适用）＝旧路径连排字样命中面仅剩票面自指＋链上历史 QA 判词＋.scratch 历史取证面＝判通过；除票面外历史件不改字。
- 本席开工 HEAD 现读＝9ebc94f（链顶）；验证期间链进他案笔（4ba69e7／4de027f／479dd39／baec554／ba70da0 等 FUXI-U29/U30 与 TMPL-STD 案笔）照登零碰。
- 体例注＝本件对旧路径字样一律拆写（桶名与日期段分排），防本件成新增连排命中面。
- 临时工作物＝仓根 .scratch/迁册票-defects桶消解-QA/（不跟踪）。

## 总裁决

绿＝八判据全过（8/8）；红＝0；黄＝2（均为回执文内辅助申报读数误差，不涉终态、不改判过）：

- 黄-1＝回执§三判据1读数注「仓根 .collab 现盘＝16 桶＋README」与§五同句——实测现盘＝14 目录＋README.md（且§五自列名录仅 13 名）。辅助计数申报不实；票面③终态机检核心判据（defects 计数 0）不受影响。
- 黄-2＝回执§四反向核查行称裸基名受跟踪命中面「与上表同集」——实测裸基名「2026-11-08-drill夹具」受跟踪命中＝8 件＝七件表＋回执自身（回执§二拆写行含裸基名）。申报误差；回执提及基名＝自述面非活指针，不影响判过。

黄项归账与是否出窄修 append 归主理人裁，本席不自裁。

## 八判据逐条实测读数（全部独立复跑·禁采信回执申报值）

| # | 判据 | 本席独立读数 | exit | 判定 |
|---|---|---|---|---|
| 1 | defects 目录终态不存在＋被迁件 ledger 在位 | `ls .collab/` ＝14 目录＋README.md，无 defects；`ls .collab/ \| grep -c '^defects$'` ＝0（grep exit 1＝无匹配）；ledger 桶内被迁件在位（1324 字节） | ls 0／grep 1（无匹配＝期望态） | 绿 |
| 2 | 笔1 恰一改名对 R100 零夹带＋blob 对钉零改字 | `git show --name-status c79dde9`＝恰一枚 R100 改名对（旧＝defects 桶内件→新＝ledger 桶同名件），name-only 行数＝1 零夹带；blob 三方对钉全等＝c79dde9^ 旧路径 blob＝c79dde9 新路径 blob＝现盘 `git hash-object` 复算＝`553e5e012c47b4454afded555839997c4ecd45f4` | 0 | 绿 |
| 3 | follow 保史可追至原落账笔 | `git log --follow --oneline -- <新路径>`＝两笔史：c79dde9 改名笔＋36dfb78 原落账笔（现读在链） | 0 | 绿 |
| 4 | 新路径靶检 | 脚本位置现读勘正＝`agent-skills/object-audit/scripts/check-pointers.py`（tools/ 目录下无此脚本；票面§③-3 原命令即此路径）。复跑 `python … --target <新路径>` 零输出 | 0 | 绿 |
| 5 | 旧路径字样命中清单对账 | `git grep -l` 连排字样＝7 件，与回执§四清单逐件吻合：票面自指 1（decisions 迁册票 v1·2 处）＋历史 QA 判词 2（团包 .collab/audits/ 2026-11-08-v2窄复核＋2026-11-09-施工批独立验证）＋团包 .scratch 取证/票面 4（COLLAB-STRUCT-1 施工回执＋tickets v2／v1.1／v1）。零新增受跟踪引用未随动且未登记；反向核查反斜杠形制命中 0（吻合回执自证） | 0 | 绿（按裁决口径） |
| 6 | 回执面账实核对 | 笔2 `git show --name-status 9ebc94f`＝恰一枚 A 回执件（name-only 行数＝1）；开端 ANCHOR `7198736dc46b2519e9fa79fb2741a645b9769ba3` 复点＝真笔、fb76547 之后、c79dde9 祖先（is-ancestor exit 0）；回执含 name-only 对账清单＋五判据读数表；回执§三读数 1-4 与本席独立复测逐条吻合（0／exit0＋36dfb78／exit0／7 件）；「GATE PASS 149215」读数不可无 commit 复测（PASS 不留 JSON 取证；pre-commit 钩子盘上在位 blob cca2ab84·402 字节＋链上各笔全过＝旁证）＝不可证伪项非红；「16 桶」读数不实→黄-1 | 0 | 绿（黄-1／黄-2 随注） |
| 7 | 链上史笔未追改 | fb76547／36dfb78 均 HEAD 祖先（is-ancestor 各 exit 0）；36dfb78 树原路径 blob＝553e5e0 与现值全等（落账史未改）；fb76547 树票面件 blob＝89e9824a＝现盘复点全等；9ebc94f 树回执件 blob＝424357c9＝现盘复点全等；`git log 9ebc94f..HEAD --` 三案面（新路径件／回执／票面）＝空＝落链后零追改 | 0 | 绿 |
| 8 | 两笔 message 零 at 符号字符＋零散件混入＋封顶 | 两笔 `git log --format=%B` 各 grep 计数「at符号」＝0（grep exit 1）；两笔 name-only 各恰一件＝零散件混入；仓根 .scratch/迁册票-defects桶消解/ 取证面（commitmsg-1/2.txt）＝untracked 不跟踪；仓根 .scratch 受跟踪件＝十枚（tickets/ 历史票面九枚＋README·皆历史批落账）本批零新增；封顶＝`git log --all --grep "迁册票-defects桶消解"` 恰两笔（c79dde9＋9ebc94f）零追加 | 0 | 绿 |

## 判据外补强读数

- 取态乙独立复核＝被迁件自题「缺陷登记：…（D 编号候台账连号）」＋全文现象／归因／分层与处置登记形制＋「修路另票候排」明示＝台账登记性质；取态乙（并入 ledger 桶）判定成立，与回执§一申报一致。
- .collab/evidence/gates/ 2026-11-09 五枚 exit1 取证 JSON（untracked 排除面）＝check-pointers 失败流水（含他案 commit 4ba69e7／4de027f 等时点），非本批 commit 卷入面；与回执「首跑悬空一枚自证纠正」过程注不矛盾。
- README 17 桶名录 vs 现盘 14 目录＝adr／architect／product 三桶名仓根无目录面（README「未列子包存续不禁」口径＋桶名闭集机检归移交工单 v3 A14 排程＝票面④注记在册，不在本票射程，本件不立账）。
- 他案并发面实测在场（开工 status 现读＝drafts 规范工单模板 staged／FUXI registration.md 变更／FUXI 案链在飞）＝本席全程零碰，仅本判定件单面落笔。

## 落笔自证

- 本件落盘后、commit 前靶检 `check-pointers.py --target 本件路径` exit 0（读数入本席取证面）。
- pathspec 限定恰本件一枚、add 与 commit 紧邻；他案 staged／untracked 面零碰；message 零 at 符号字符用字样。
- 本件拆写自查＝落链后 `git grep -l` 连排字样复测命中面仍＝7 件零新增（本席落笔前基线＝7）。

判定完 · 总裁决＝绿（红0 黄2） · qa-mvdefv
