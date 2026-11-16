# SWB-RCTPATH-R3 · 放行登记 v1（产品席笔·双席快审后放行）

## 〇、开工读数（当轮现跑·禁抄旧数）

- 时点＝date '+%F %T %z' 实测 2026-11-16 18:31:45 +0800；HEAD 现跑＝3b82e59（＝QA 席快审判词笔＝当轮链顶；产品席判词笔 2fed3cc 居其前）。
- 票面钉版：git ls-tree 0f4291c 对 .scratch/tickets/2026-11-16-SWB-RCTPATH-R3-20-handoff节题去编号微票-v1.md → blob sha＝90e901a155b35e5efbbba52ed55d4b04973994b4，与派工预期**全等**。
- 双席判词钉版：QA 席笔 3b82e59 件 .collab/audits/2026-11-16-SWB-RCTPATH-R3-快审判词-QA席-v1.md blob sha＝9f92201445650aa7349531860ec4a70f31525606（红0黄2绿7＝可放行）；产品席笔 2fed3cc 件 .collab/decisions/2026-11-16-SWB-RCTPATH-R3-快审判词-产品席-v1.md blob sha＝aebfa89f811646960f48627ad388709b8020838c（红0黄0绿5＝可放行）。
- 三钉值本席亲跑全等零摆动：缺省扫描 python share/check-pointers.py → grep -c BLOCK＝**22810**、grep -c WATCH＝**4581**；bash share/run-gates.sh → **GATE PASS exit 0·发现 151502**。
- V4′ 落点件自靶基线现跑：python share/check-pointers.py --root . --target agent-skills/multi-collab/references/20-handoff.md → **exit 1·恰一枚悬空＝行 24**（deliverables 旧径·OA-D6·另案候补池性质零处置）。
- 落点件现势读数：wc -l＝**66**；grep -c「二之二」＝**1**（恰居行 28）；grep -c「决策者裁定」＝**1**（同居行 28）；节题行号 grep -n 实测＝**5／9／28／36／55／62** 六节原位。
- 旧行链上版提取（黄-2 硬化预演）：git show 0f4291c 版落点件行 28 verbatim＝⟦### 二之二、留存过程件正文内的仓内文件引用写法（两域两制·决策者裁定 SWB-RCTPATH 甲案）⟧，与票 §二 S1 旧行块**逐字符全等**。
- tracked 脏面照登＝ledger 一枚 M（agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl）＋仓根散件群（.collab 根散 md／.collab/research 散 md／.py／.scratch_uds 系／.scratch_wbdocs.html／assert-modified-run2.txt）——全部他案脏面，零带入零清理。

## 一、依据链

- 决策者裁定链：RCTPATH-R2 收口后「二之二」命名负反馈→AskUserQuestion 选项归一，决策者亲选**「去编号自然题」取态**；同时确立「今后规范面插新节不再造『X之二』式插档编号」取向（票 §来源段在册）。本票＝该裁定的规范面执行票。
- 票面＝.scratch/tickets/2026-11-16-SWB-RCTPATH-R3-20-handoff节题去编号微票-v1.md（笔 0f4291c·blob 90e901a…全等钉版·候裁 0 枚）。
- 双席 fresh 快审＝QA 席 3b82e59（红0黄2绿7）＋产品席 2fed3cc（红0黄0绿5），两席独立判可放行；黄项两枚均属非阻断随批项，§二 写死消化。
- SCRATCHCFG 微票先例链（小改动快审链体例：开票→双席快审→放行→工程师 BUILD＋RECEIPT→fresh QA 验收→收口）；本登记体例参照先例 .collab/decisions/2026-11-16-SWB-RCTPATH-R2-放行登记-v1.md。
- 沿革锚：归裁登记 4ea0d58／R2 票面 89f796d＋rev-1 b6a4ac6／R2 施工 0da2566＋回执 659ec9a／QA 验收 5adf535／收口登记 b2b61d7——在册闭环，本票零回改。

## 二、随批采纳值写死（施工与验收照此）

1. **黄-1 更正规格表述**（票 §二 S2 证据句读数错位＝「二之二」其余命中实居 .collab／.scratch 本链史账件而非外包 refs 族；结论面不翻）：更正规格以本登记为准＝⟦agent-skills 规范面内「X 之二」式插档编号仅行 28 一枚（实跑坐实）；external-advisor 外包 refs 族自带独立治理链不在本票射程；本链史账件命中 append-only 不回改⟧。票面 append-only **不回改**，验收照本条口径，不照票面原句错位读数。
2. **黄-2 硬化入验收**：工程师开工读数与 QA 验收开工读数均须**钉票面 blob sha 90e901a155b35e5efbbba52ed55d4b04973994b4 全等一枚**；旧行以 git show 0f4291c 版落点件行 28 提取为准，**禁凭工作区或记忆改写**。
3. **施工规格＝单行替换**（票 §声明闭集逐字照录，一字不改）：旧行＝⟦### 二之二、留存过程件正文内的仓内文件引用写法（两域两制·决策者裁定 SWB-RCTPATH 甲案）⟧→ 新行＝⟦### 留存过程件正文内的仓内文件引用写法（两域两制）⟧。同位单行换行：落点件 wc -l **66→66**；diff 恰 1 增 1 删单 hunk；grep「二之二」该件 **1→0**；grep「决策者裁定」该件 **1→0**；节序行号 **5／9／28／36／55／62 不动位**（V3）；V4′ 差量对拍**零新增 BLOCK／WATCH**（行 24 既有悬空仍另案不背）；三钉值 **22810／4581／151502** 验收现跑全等。
4. **禁动面照票 §二写死**：同件行 1–27、29–66 零触碰（行 29–34 甲案条款正文条目 1–5 零改动）；链上历史件 append-only 零回改（含链上一切「二之二」字样与行 24 悬空）；share/ 门禁配置零触；ledger／leases／.gitignore 零手写；他案脏面零带入。

## 三、排程红线

- 工程师席 BUILD＋RECEIPT **两笔串行**（交付面单一工程师席在飞；尾标闭集 -BUILD／-RECEIPT）；BUILD 落链笔＝取向生效时点。
- fresh QA 席按票 §三 V 系＋本登记 §二 硬化项独立验收（尾标 -QAV）；验收开工读数须含票面 blob sha 钉版全等一枚。
- 收口登记（尾标 -GCLOSE）随登观察行两条：黄-1 更正规格（居本件 §二-1）；产品席快审 O-2 派工简报行数微偏（留档性质，零动作）。
- **候裁 0 枚**：本登记不新增决策者事项；两项随动裁量（ID 注记去／条款不立）已由票 §二 论证自决、双席零修单背书。

## 四、本笔自证

- 本笔面＝恰本登记件一件；票面／规范面／双席判词／链上件／门禁配置／账本面全程零触碰。
- 落笔后自靶：python share/check-pointers.py --root . --target .collab/decisions/2026-11-16-SWB-RCTPATH-R3-放行登记-v1.md → 期望 exit 0（实跑读数随回报）。
