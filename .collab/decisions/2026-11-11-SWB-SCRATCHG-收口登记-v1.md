# SWB-SCRATCHG 收口登记 v1

- 开工实测：date＝2026-11-11 00:29:47／HEAD＝9278445（QA 验收判词笔）／tracked 面净／分支 main。
- 依据：皮总裁定登记件 `.collab/decisions/2026-11-10-皮总裁定-候裁三件全按建议放行.md`（落链 ca33b5f）；规格票 v2 `.scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v2.md`（落链 7900b07）。

## §一 链条在册

| 段 | 笔 | 面 |
|---|---|---|
| 票 v2 放行 rev | 7900b07 | 票面整件重写 |
| 双席窄复核 | d50c296／4a5099f | 产品席绿6黄0红0watch3／QA席闭合6红0黄0观察1 |
| 施工笔一 忽略规则 | f173c03 | .gitignore（9增0删·九行块逐字节照录·QA独立对拍双sha256同值5bff83f0d9f9坐实） |
| 施工笔二 类B处置 | 7fe59f1 | R100 恰两式位点（COLLAB-STRUCT-1 施工回执 .scratch/→.collab/receipts/） |
| 施工笔三 README改句 | 8977648 | README.md L22 逐字照落 §4.4-F |
| QA 独立验收 | 9278445 | 红0黄1绿＝验收通过（V0–V9 终态独立实跑全绿·九行块逐字节独立复点不采信席报） |

## §二 黄-1 处置＝config 层租约随动缺口→另票在册

现场（QA 判词实证＋工程师单列呈报一致）：包级 `agent-experts/baigong-software-team/config/seat-permissions.json` 与 `seat-permissions-hooks-map.json` 的 engineer deny_globs 含 `.collab/receipts/**` 行、无 B-i 目标桶单点除外；tests/s4 派生面两文件逐行相等断言在场；leases.jsonl SCRATCHG 租约签发记录＝0。

判定采 QA 口径＝黄非红（票内租约段已闭合、工程师守声明闭集未越权改 config＝合规；缺口在配置常驻规则层未落位＝结构缺口真实）。

处置路由＝另票：`SWB-SCRATCHCFG` config 层租约随动微票（两 config 文件同步随动＋租约签发兑现），归已裁(e)「租约随动」的施工后果线**不新增呈裁**；起草归 SCRATCHG 租约段作者席（续派中）；若起草暴露真分歧再入呈裁面。

## §三 README 既有 8 条 BLOCK 悬空指针处置＝并册 A14 线候补行

QA 对拍坐实本笔零新增（before/after 八条同位全等）；归属＝不在 A14 票豁免六枚集合（其写集不含 README）＝另账未在册。

处置路由＝与 A14 豁免线同族（史笔不改字铁律 vs 指针机检碰撞），并入 A14 票 v2 rev 候补：待 A14 双席审回票归集后，由 A14 作者席 rev 时将八枚（L23/25/72/84×2/88×2/92）入豁免 items、碰撞面集合扩至 6 文件、V1 判据随扩 −8−6。**不在双席审在飞期改票面**（防污染 fresh eyes）。

## §四 观察面登记

- (h)/(e)「回执」措辞相歧＝维持观察不票微 rev（tickets 桶票附回执惯例与案卷回执 receipts 桶双轨并存）；未来 config 维护票（即 §二 SCRATCHCFG）补一行落点体例澄清。
- 仓外四目录（D:\semgvt6-clone、D:\semgvt6-assemble-tmp、D:\semgvt6-assemble-tmp2、D:\qa-semgovt6v2-tmp）＝删除权在皮总，随收口继续点名候手动处置。

## §五 收口宣告

SCRATCHG 质量链三段闭＝工程 IS_PASS→QA fresh eyes 独立验收通过→主理人会师收口。无新呈裁（§二§三均系 ca33b5f 已裁线内后果）。票 v2 候裁段零留白存续。交付面排程纪律（单一工程师席串行）全程无违例。
