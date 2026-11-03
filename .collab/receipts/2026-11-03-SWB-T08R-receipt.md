# SWB-T08R＋T08R-A1 · 工程师完工回执：权限表数据面机械化＋增补补行（一次施工批）

- 施工席＝工程师席（engineer-t08r）；票面＝`.collab/tickets/2026-11-03-SWB-T08R-seat-permissions-mechanization-rev2.md`（R2·`4082ff3` 放行链）＋`.collab/tickets/2026-11-03-SWB-T08R-A1-augment-permission-rows.md`（`e440131`·同票同批）。
- Temp＝`D:/eng-t08r-tmp`（Windows 盘符形态·判据/探针/演练共用·仓内零运行残留）；occurrence 口径；判据命令全部自带落盘重定向。

## 0. 开工读数

- 开工 `git rev-parse --short HEAD` 实测＝`ba00a0f`（SWB-T07 回执笔·`e440131` 之直接后继；`git merge-base --is-ancestor` 双验 f135855／e440131 均为 HEAD 可达祖先＝两票 ANCHOR 义务满足）。
- `git status --porcelain` 开工读数＝两条未跟踪件（`.collab/qa/2026-11-01-TKT-双审批计件汇总-v1.md`、`.collab/qa/2026-11-01-TKT-最终分票全文汇编-v1.md`），非本批可写面、不纳入任何 commit，如实登记。
- T07 并行互锁复测＝开工基线全套先跑先落盘：c2-base 全表 34 行／非机械 14（逐席 host 13/4·product 3/0·architect 7/5·qa 4/2·engineer 5/2·human 2/1）＝与两票开工基线逐值全等；c4-base 四条负例均 exit 2；j-a1-2-base 四条基线均 exit 2（architect docs/adr exit 2＝缺陷在基线存在）。基线相符＝T07 未动共享面，正常开工；版本链读数＝三同源现值 0.1.15（T07 已先行落笔）→本批按票面条款走 0.1.15→0.1.16。

## 1. 完整写入清单（与交付 commit name-only 对账全等·6 件）

1. `deliverables/experts/baigong-software-team/config/seat-permissions.json`
2. `deliverables/experts/baigong-software-team/config/seat-permissions-hooks-map.json`
3. `deliverables/experts/baigong-software-team/.codebuddy-plugin/plugin.json`
4. `deliverables/experts/baigong-software-team/bundle.lock`
5. `deliverables/experts/baigong-software-team/plugin.json`
6. `deliverables/experts/baigong-software-team/README.md`

落笔序按 A1 建议行位序：先 T08R 账一拆行（host `{intake,reviews}`／architect `{design,adr}`）→Aug1 host 尾追加 `.collab/decisions/` →Aug2 architect 两改（write_globs 尾追加 `docs/adr/`＋deny 三件套枚举开口＋deny_globs_note 新键）→T08R-A engineer 段＋B2 deny 唯二＋两注记键→hooks-map B2/C/Aug2.4→D 段三版本件＋README。全部逐字文本锚替换，无锚串位移。

## 2. 修单映射表逐条落点读数（R1–R4＋条款2/5/6/7/8）

- R4＝engineer 写域段按裁定一/三重做：`write_globs`＝3 机械行＋`write_globs_note`＋`project_domain_md` 两注记键在位（c1 断言·无用户目录硬编码）。
- 条2＝B2 deny 唯二联动：两 config engineer `deny_globs`＝`["docs/**", ".collab/**"]` 相等（c1）；防护迁移凭证＝c5 r2/r3 读数（`∉当席租约` occ 各 1、`deny_globs` occ 各 0）。
- R1＝新构型无「全域行＋具体路径」组合：c3 exit 0／c4 四条 exit 2 对位。
- R2＝正则 v2 首字符容 `.`、字符类不含 `{}`：c2/c2-base 同式复算吻合申报值。
- R3＝全表读数 34 基线属实（c2-base）。
- 条6＝R⑧并入 B2 同段：过渡态(III) 缺省维持，c5 r4 读数如实登记（见 §5）。
- 条7＝承载＝约定 md 交付路径字段：`project_domain_md` 键在位（c1），md 实体本批不落（票面 E 节）。
- 条8＝真源行号随动不涉数据面，零施工面。

## 3. 判据 0–11 逐条命令与实测读数（落盘 `D:/eng-t08r-tmp/`）

| 判据 | 落盘 | 实测读数 | 判定 |
|---|---|---|---|
| 0 Temp 条款＋基线先跑 | c2-base.out／c4-base.out | 34/14 逐席全等；四负例 exit 2×4 | 基线对位 ✓ |
| 1 数据面断言 | c1.out | engineer write_globs 恰 3 行集全等；deny＝`["docs/**",".collab/**"]`；hooks-map engineer deny 与源件相等；`project_domain_md` 在位；四展开串 occurrence 各＝1 → exit 0 | PASS |
| 2 机械审查（修正正则） | c2.out | 施工后＝**36/10**（合账表第三行·A1 取代 34/10 申报值）；逐席 host 15/3·product 3/0·architect 9/4·qa 4/2·engineer 3/0·human 2/1 → exit 0 | PASS |
| 3 正例·签发面 | c3.out | `--seat engineer --path-glob ".collab/returns/engineer/x.md"` → exit 0 | PASS |
| 4 负例·四越域 | c4.out | `docs/x.md`→exit 2／`.collab/ledger/x`→exit 2／`.archive/x.md`→exit 2／`src/app.py`→exit 2（基线同值＝不得放开条款满足） | PASS |
| 5 写侧 deny 链 | c5.out（原始输出 c5-raw.out） | `docs/x.md`→deny 且 `glob='docs/**'` occ＝1；`tests/root-judgement-truth.py`→deny `∉当席租约` occ＝1·`deny_globs` occ＝0；`.archive/old.md`→同前值；`.collab/returns/engineer/x.md`（c3 租约在册）→仍 deny 且 `glob='.collab/**'` occ＝1 | PASS（R⑧ 过渡态如实登记） |
| 6 身份映射端到端 | c6.out | 五新键 json 断言 exit 0；Temp 租约行＋write-guard 喂 `software-team-engineer` → stdout 无 `"permissionDecision"`（放行·不自造 allow） | PASS |
| 7 旧身份零破坏 | c7.out | drill-03 注入 `T06_TMP` 后单跑 exit 0（`DRILL03_GREEN`，旧串 `software-engineer` 经 legacy 行仍命中 deny 链读数） | PASS |
| 8 测试实体回归 | c8.out | s2（test_lease_instantiation）exit 0＋s2 ledger exit 0＋s4 exit 0（t03 deny 字符串断言、t13 派生同源断言随两 config 一致更新绿） | PASS |
| 9 六演练回归 | c9.out | `T06_TMP="D:/eng-t08r-tmp" bash …/drill-runner.sh` → exit 0 且 `SIX_DRILLS_GREEN` occurrence＝1 | PASS |
| 10 版本三同源 | c10.out | 前值三处 0.1.15（T07 先落）→后值三处 0.1.16 同值 | PASS |
| 11 门禁＋票体自咬 | c11.out／c11b.out | run-gates GATE PASS occurrence＝1 exit 0；count-assert mode1 T08R 票＝申报 6＝实数 6 exit 0 | PASS |

A1-J1–J5 读数另见 `.collab/receipts/2026-11-03-SWB-T08R-A1-receipt.md`（同批回执笔）。

## 4. 全表逐行审查读数表（施工后 36 行·含 A1 增两行）

```
01 host 机械 .collab/ledger/                 02 host 机械 .collab/signatures/
03 host 机械 .collab/dlq/                    04 host 机械 .collab/commitments/
05 host 机械 .collab/human/intake/  ←账一②拆行  06 host 机械 .collab/human/reviews/ ←账一②拆行
07 host 非机械 .collab/tickets/{id}/仅生命周期字段  ←账二滞留·候裁R①
08 host 机械 .collab/release-record/         09 host 机械 .collab/manifest/
10 host 非机械 docs/转正代写                  ←账二滞留·候裁R②
11 host 非机械 .archive/退役定稿落位           ←账二滞留·候裁R②
12 host 机械 .collab/config/                 13 host 机械 .collab/inbox/engineer/
14 host 机械 .collab/archive/                15 host 机械 .collab/decisions/  ←Aug1 新增
16 product 机械 .collab/drafts/prd/          17 product 机械 .collab/product/
18 product 机械 .collab/drafts/proposals/    19 architect 机械 .collab/drafts/design/ ←账一③拆行
20 architect 机械 .collab/drafts/adr/        ←账一③拆行  21 architect 机械 .collab/architect/
22 architect 机械 .collab/drafts/proposals/  23 architect 非机械 .collab/tickets/票面文档（起草与按修票权修订） ←账二滞留·候裁R①
24 architect 非机械 开发票四字段              ←账二滞留·候裁R①
25 architect 非机械 tests/共写（增删改走 C1）  ←账二滞留·候裁R③
26 architect 非机械 租约段签注与灰度判据（票内）←账二滞留·候裁R①
27 architect 机械 docs/adr/                  ←Aug2.1 新增
28 qa 机械 .collab/audits/                   29 qa 非机械 .collab/tickets/缺陷票（修票权） ←账二滞留·候裁R①
30 qa 非机械 tests/共写                      ←账二滞留·候裁R③
31 qa 机械 .collab/drafts/proposals/         32 engineer 机械 .collab/inbox/engineer/
33 engineer 机械 .collab/returns/engineer/   34 engineer 机械 .collab/drafts/deploy/
35 human 机械 .collab/human/deliberations/   36 human 非机械 签名经主理人落 .collab/human/reviews/ ←账二滞留·候裁R④
```
合计 36 行／非机械 10（host 3／product 0／architect 4／qa 2／engineer 0／human 1）＝合账表第三行逐值（A1-J5 复算凭证＝c2.out）。

## 5. 候裁 R①–R⑨ 逐条呈裁原文引用＋本批处置

- **R①**「host/architect/qa `.collab/tickets/` 三席字段级约束…超 path_glob 表达力——展开＋注记 vs 维持现样」→本批账二滞留零动（行 07/23/24/26/29 维持现样）。
- **R②**「host `docs/转正代写`／`.archive/退役定稿落位`＝promote-manifest 机械通道非席位租约写…建行/删行/改注记」→账二滞留零动（行 10/11）。
- **R③**「architect/qa `tests/共写（增删改走 C1）` 机械化＝扩权…双席对表」→账二滞留零动（行 25/30）。
- **R④**「human 行…不入 hooks 强制面——机械化与否」→账二滞留零动（行 36）。
- **R⑤**「约定 md 文件名＋最小 schema 两字段形制…双席审票裁名」→本批落数据面注记键 `project_domain_md`＝提案值 `docs/collab-project-structure.md`，实体不落。
- **R⑥**「engineer/QA 席位卡是否增…纪律句…随 B 批或卡面随动票处置」→席位卡零触碰。
- **R⑦**「drill-05 走位改 engineer…归 T06 闭集」→drill-05 走位零触碰（c9 六演练全绿佐证）。
- **R⑧**「…(iii) 过渡态维持（本票缺省）…产品席建议 (i) 向已登记在案」→本批采缺省 (iii)：**过渡态读数如实登记**＝c5 r4 `.collab/returns/engineer/x.md` 租约在册仍 deny（`glob='.collab/**'` occ＝1）＝签发可/写拦显性化冲突维持，非固化。
- **R⑨**「表2-1 工程师行『明确不可写』列…与裁定一唯二排除的设计基线偏差——B4 票包再锚/设计修订呈请追认」→本票未改设计真源，偏差在册呈追认。
- 仓根路径锚定前置条款：本批仓根字面（`.collab/**`、`docs/**`）按「无裸公共区」假设参数化落笔，无特例通道。

## 6. 交付笔与回执笔

- 交付笔＝本批闭集 6 件单独 commit（`collab:` 前缀＋票号）；回执笔＝本回执＋A1 回执随后单独笔。禁 `--no-verify`、禁 amend＝未使用；pre-commit 门禁实跑通过、无拦点。
- 不自判合格（制度③）：以上全部为机械读数，验收判定归双席再审与收口。
