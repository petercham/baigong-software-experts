# SWB-T08R-A1 · 工程师完工回执（增补补行·随 T08R 同批施工笔）

- 票面＝`agent-experts/baigong-software-team/.scratch/tickets/2026-11-03-SWB-T08R-A1-augment-permission-rows.md`（起草笔 `e440131`）；施工＝与 SWB-T08R 同票同批一次 commit（交付笔同 T08R 回执 §6，闭集 6 件零扩员）。
- Temp＝`D:/eng-t08r-tmp`（＝`$T08R_A1_TMP` 同目录·Windows 盘符形态）；开工 HEAD／基线／互锁复测读数见 `.collab/receipts/2026-11-03-SWB-T08R-receipt.md` §0（开工实测 HEAD＝`ba00a0f`，f135855／e440131 双验可达）。

## A1-J1–J5 逐条命令与实测读数

- **A1-J1 数据面补行断言**（`D:/eng-t08r-tmp/j-a1-1.out`·exit 0）：host `write_globs` 含 `.collab/decisions/` occurrence＝1 且 host 总行＝15；architect `write_globs` 恰 9 行＝拆行后 8 行集∪{`docs/adr/`}；architect `deny_globs` 六行全等＝`["docs/PRODUCT.md","docs/ARCHITECTURE.md","docs/STRUCTURE.md",".archive/**","deliverables/**",".collab/audits/**"]`；`docs/**` 串在 architect 行（两 config）occurrence＝0；hooks-map architect `deny_globs` 与源件全等（t13 同源性佐证另见 s4 c8.out 绿）。
- **A1-J2 签发面正负例**（`D:/eng-t08r-tmp/j-a1-2.out`·lease-issuer 均带 `--countersign architect:probe`——countersign 校验先于子集校验之票面注记照执行）：
  - 开工基线先跑先落盘（j-a1-2-base.out）：`architect docs/adr/0001-probe.md`→exit 2／`docs/PRODUCT.md`→exit 2／`docs/process/probe.md`→exit 2／`host .collab/decisions/2026-11-03-probe.md`→exit 2；
  - 施工后：`architect docs/adr/0001-probe.md`→**exit 0**；`architect docs/PRODUCT.md`→**exit 2**（≠0 ✓）；`architect docs/process/probe.md`→**exit 2**（≠0 ✓）；`host .collab/decisions/2026-11-03-probe.md`→**exit 0**。基线→施工后无一条反向。
- **A1-J3 写侧两读数**（`D:/eng-t08r-tmp/j-a1-3.out`）：Temp 直写租约行 `{"ts":"t","lease":{"ticket_id":"A1J3","seat_id":"architect","path_globs":["docs/adr/"],"hash":"h"}}`＋write-guard 喂 `{"agent_type":"software-architect",…}`：`docs/adr/0002-probe.md`→stdout 无 `"permissionDecision"`（allow·不自造词）；`docs/PRODUCT.md`→deny 且原因行含 `glob='docs/PRODUCT.md'` occurrence＝1。
- **A1-J4 docs fail-open 守卫断言**（`D:/eng-t08r-tmp/j-a1-4.out`·exit 0）：(a) 全席位机械 `docs/` 起始写行集＝{`docs/adr/`}（恰 ⊆ 申报闭集）；(b) architect deny 三件套字面两 config occurrence 各＝1；(c) `git ls-files docs/` 顶层子名（adr 除外＝现盘 README.md／process 系）拼探针路径喂各席机械写行→命中＝0（全绿＝枚举开口无 fail-open 现盘窗口）。
- **A1-J5 合账复算断言**（`D:/eng-t08r-tmp/c2.out`＝判据 2 同式合跑·exit 0）：总行 **36**／非机械 **10**；逐席＝合账表第三行逐值 host 15/3·product 3/0·architect 9/4·qa 4/2·engineer 3/0·human 2/1；开工基线同式先跑 34/14（c2-base.out）对照在案。

## 合账表三行复算读数（单一账）

| 口径 | 总行 | 非机械 | 逐席（总行/非机械） | 实测凭证 |
|---|---|---|---|---|
| 现盘基线（开工复测） | 34 | 14 | host 13/4·product 3/0·architect 7/5·qa 4/2·engineer 5/2·human 2/1 | c2-base.out |
| T08R 原账一后（票面申报·被合账取代） | 34 | 10 | host 14/3·product 3/0·architect 8/4·qa 4/2·engineer 3/0·human 2/1 | —（A1 合账条款） |
| T08R＋A1 合并后（权威·实跑） | **36** | **10** | host 15/3·product 3/0·architect 9/4·qa 4/2·engineer 3/0·human 2/1 | c2.out |

## 随动条款执行读数

- README 版本账 append 行＝A1 扩句版（「权限表数据面机械化（SWB-T08R＋A1）：…依据＝皮总裁定 ff72b92/18bf840/5358ea4＋ES 终态收口 28381a6」）在位；既有行零回改。
- 版本不独立 bump＝A1 随 T08R 一次 bump：三同源前值 0.1.15→后值 0.1.16（c10.out）。
- Aug3 E-ADR-4 基名引用式 `\b\d{4}-[A-Za-z0-9._-]+\.md`＝字面钉死登记条款，无本批施工面（门禁挂载归 60-gates 路由裁量面）——如实登记零落点。
- Aug4＝A1-J4 实体，已在位断言跑绿（见上）。

## 候裁 A1①–A1③ 逐条呈裁原文引用＋主理人既裁执行

- **A1①**「ES 终态收口 §四-1 席位卡面…卡面执行规范随动票归属——与 T08R 候裁 R⑥ 同域合并呈裁」→主理人已裁＝席位卡面句不入本批、归 ES §四-1 卡面随动票；本批席位卡零触碰（票面内预留按此裁执行，未留空）。
- **A1②**「architect `explicitly_not_writable` 列含 `"docs/"` 与 Aug2 枚举开口的设计基线偏差——随 R⑨ 同笔呈 B4 票包再锚追认」→主理人已裁＝随 R⑨ 同笔 B4 追认；本批该列零动（转录面维持），偏差随 R⑨ 在册。
- **A1③**「三件套实体缺位过渡期…是否需过渡期 README 索引注记＝主理人裁」→主理人已裁＝无害前置（探针 Q-c/Q-d 实证签发/租约双兜底无敞口）、不做过渡处置；本批未造三件套实体、未加过渡注记。
- 不自判合格（制度③）；本回执全部为判据实测读数，验收归双席与收口。
