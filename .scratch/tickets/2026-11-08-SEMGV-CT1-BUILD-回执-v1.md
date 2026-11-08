# TK-SEMGV-CT1-BUILD · 工程师回执 v1

- 票＝`TK-SEMGV-CT1-BUILD`（施工授权票 `f780ce4`）；席＝工程师（eng-semgov-t2b）；回执落笔 2026-11-08 12:3x +0800。
- 规格唯一真源＝`e3935e7` blob（v3·sha256 `d9cf2dc2b754189ed5d4fb5b5f945271371514604263e147cc726df6c79979c5`／293 行／47,236 字节）——开工复算全等（见①），全程按 blob 副本施工，未以工作区快照为准。
- 在途裁定两件（主理人开票人职权内）：`b47709e` 裁定一（c11 探针层豁免·甲案窄化）＋`6b0fc5d` 裁定二（T-A3 靶点剔出·丁案窄化）——夹具侧改动按裁定件执行，见「判定面偏离」专段。

## ① 开工三读数

- `date`＝`Sun Nov 8 11:54:13 2026 +0800`；`git rev-parse --short HEAD`＝`f780ce4`（＝开票钉值，未前移）；`git status --porcelain --untracked-files=no`＝空（他案未跟踪面照登不碰）。
- 真源在位：`git cat-file -e e3935e7^{commit}` exit 0；blob sha256 复算＝`d9cf2dc2…979c5` 全等（293 行／47,236B）。
- 基线四组复算全等：七件 `git diff 9e04dc0..HEAD -- agent-skills/claim-commitment-governance/` 空＋行数和 577（92/217/50/98/43/44/33）；py `77286b33d39ca7bf9b28d6b4918846ea84cbecd19f6d6eb4985b5f40d7d1e453`／1,618 行／81,550B；config `d09156ab8bf30dc1c9b963d88d4da1475beed563641edb56581f3921ed5ab0bb`／49,446B；verify.py `25fc83b451c12522f58872abbc37d1a39038b5646dc01ebfa12d835444ef508d`／2,097 行。
- 病灶 16 处 `sed -n` 逐处回原文核对定位与 v3 引文相符后方落笔。

## ② 租约态一复跑读数

- 同款命令（`--ticket SEMGV-CT1-BUILD-WDDEMO-1 --seat engineer --countersign "architect:CT1-BUILD-WRITEDOMAIN-DEMO" --path-glob "skills/**" --path-glob "config/**"`，`--leases` 指仓外临时件 `tmp.0X1GAVqZrz/l1.jsonl`）：exit 0，hash＝`6bff8c1283417ee9cb339e0f7b64df0a78224916be4c56ebfe48cb66e629a959` 与票面钉值全等。
- 态二（七件面＋fixture 面）拒签发＝票面既定预期（授权由票 §一 写集闭集承载，照 `86d9963` 裁定 B 先例），本席未重复实跑。

## ③ 落账 commit（三笔·超两笔封顶之例外见登记）

1. 施工笔＝`4700456`（恰 7 件，`collab:` 前缀，`git show --name-only --format=""` 与写集 W1–W3 全等，见⑤）；
2. 裁定二随动笔＝`38296b0`（恰 1 件 verify.py）——例外登记：原票两笔封顶；主理人裁定二件（`6b0fc5d`，12:26:39 落链）要求 T-A4 留靶点面＋EXPECT_TARGETS 注释行，该要求到达时施工笔已落（本席未见该裁定件、按裁定一消息施工），据裁定件补随动一笔。笔数 3＝2＋裁定派生 1，如实登记不辩称合票。
3. 回执笔＝本笔（恰 1 件＝本文件）。

## ④ 判据 1–12 实测读数

| # | 读数 |
|---|---|
| 1 | `git show --name-only --format="" 4700456`＝7 件与 W1–W3 闭集全等（清单见⑤）；裁定二随动笔恰 1 件；回执笔恰 1 件 |
| 2 | `git diff --name-only` 四改件内零 SKILL.md／40-provenance-map／outbound-artifact；表头行机械对拍（HEAD blob vs 盘上，逐文件 `headers-equal: True`）四件全 True；`git diff` 新增行中表标题/表头行 grep 0 命中 |
| 3 | `wc -l` 四改件＝225／52／100／45＝预算，差值 0／0／0／0；七件合计 590＝预算 590，Δ0 |
| 4 | 逐字面 grep（fixed-string，检索范围＝四改件）：「无责任主体主张单列区」1／「单列区（≠桶）」1／「跨表同值回指」1／「无论本行 `original_requirement_ref` 是否为 `none`」1／「编号两分发放」1／「A3 \|」1／「A4 \|」1／「A1–A4」1／「`req_*` 三列取值规则」1／「例外一支」1／「^11\. 交付汇总」1——逐条恰命中（措辞＝v3 围栏） |
| 5 | `semantic-governance.py selfcheck`（改后真文件）：`SELFPROOF groups_compared=34 red=0`＋`SELFPROOF mutations_total=4 red=4` exit 0 |
| 6 | S-1 正反（仓外样本 5 例）：自由文本＋`authority=unverified`→exit 0；＋`internal_only`→红 `spec=R2 field=linked_artifacts branch=2 … value=free-desc`；「无冒号」支回归仍红（value＝原条目）不被吞；「kind 未知」支回归仍红不被吞；`source:RES-0001` 编号形态闭集内→exit 0 |
| 7 | S-2 三红：`@human:A` vs 表 A `human:B`→红 `field=required_change_record branch=3 claim_id=C-001`；H2（`ref=none` 行＋表 A `approver=none`＋记录非 none）→修后转红（同 branch=3；validate 面 exit 0＝R4 归 gate-outbound 归属面，登记）；`@seat:X`→红；正样本同值→exit 0 |
| 8 | S-3 四态：reconcile 单列区 4≠命中 5→红 `field=solo_claim_area branch=5 value=count=4!=hits=5`；缺不可归属原因→红 `value=three-elements-incomplete`；`validate --kind 交付汇总` 单件→不判⑤ exit 0；reconcile 不含汇总→跳过判定面可见 `RECHECK-ITEM spec=RECHECK-ITEM field=r13_branch5_solo_area value=skipped-not-both-register-and-summary`（不计 exit）；5=5 三元素齐→exit 0 |
| 9 | 夹具四类（改后真文件重跑）：`--all` 28 OK／0 FAIL exit 0；`--mutate` 244 条全咬／假通过 0／MUTATE_FAILED 0 exit 0（含 D09 新锚 `BITE c26 …§11 整节摘要不等于期望`）；`--selfcheck` 自证全绿 exit 0（内容面 229 条可生效 229）；`--stats` 合计 28 条分布之和＝检查数 exit 0。判据 9 补充口径（主理人裁定件）＝随动重算后全绿＋对抗三态（见⑥）＋D09 新锚 OK-RED（已在 --mutate 读数内） |
| 10 | 配置↔真源＝selfcheck 34 比对全过（V6 同源）；抽 3 处核对：config `g12.r_table` R2 行含「降级形态条目」字面 True／`g13.a_table` A 行集＝[A1,A2,A3,A4]／其 `after_heading`＝「## 4. 负样本闸 N1–N10 与人工闸承接项 A1–A4」——全等 |
| 11 | `git diff 56ee808..<本回执前HEAD>` 对 CT1 v1/v2/v3 三票面＝空输出；T2 v3（`2026-11-07-SEMGOV-T2-校验器与夹具规格票-v3.md`）diff 空；试填两件（passA/passB1）diff 空 |
| 12 | `git status --porcelain --untracked-files=no`（收口前最后读数见⑧） |

## ⑤ 完整写入／修改文件清单（＝`git show --name-only 4700456` 全等）

1. `agent-skills/claim-commitment-governance/references/10-contract.md`（M-2修法1/2、M-3修法2、M-4修法1/2、M-6、M-7）
2. `agent-skills/claim-commitment-governance/references/20-artifact-mapping.md`（M-1修法1/2）
3. `agent-skills/claim-commitment-governance/references/30-gates.md`（M-2修法3、M-3修法1、M-4修法3、M-5修法1/2/3）
4. `agent-skills/claim-commitment-governance/templates/claim-register.md`（M-1修法4）
5. `agent-experts/baigong-software-team/skills/sop/scripts/semantic-governance.py`（S-1/S-2/S-3）
6. `agent-experts/baigong-software-team/config/semantic-closed-sets.json`（S-4 重算：14 组与 key 结构不变，随动段＝R2/R4/R13 判据句、§11 各行、`:83` 单元格、交付汇总必填面、§4 标题 A1–A4、A3/A4 两行；diff 20+/10-）
7. `.scratch/tickets/2026-11-07-SEMGOV-T1-BUILD-verify.py`（S-5 期望常量随动：c07 格式列新串／c13 R2·R4·R13 三 digest／c14 §4 标题常量／c16 条目 10→11／c22 交付汇总行＋SEC3 digest／c23 A 行集＋ACCEPT_DIGEST＋标题／c26 SEC11_DIGEST＋禁令字面「不自产编号」→「编号两分发放」＋D09 锚重设；判定逻辑零改，判定面偏离两处见专段）
8. 回执笔＝本文件（单独一笔）。

## ⑥ 判定面偏离（专段·引裁定件·QA fresh eyes 必审）

累计**两处**，均在主理人在途裁定授权内，其余夹具改动仍限期望常量：

1. **c11 探针层行级豁免**（裁定一 `b47709e`·甲案窄化）：仅 `HUMAN_GATE_PROBES` 循环增「行内含『人工闸』」豁免；BANNED_PHRASES／逐行全等／义素组合／STRONG·PLACEHOLDER 词表层豁免条件零动。A3 行零牵动。对抗三态实跑（仓外包副本）：
   - 态①A4 行在位真件 → `--all` c11 绿（28 OK／0 FAIL）；
   - 态②§8 原行「1. 外部权威来源的确认。」复制进 30-gates 表外行（副本包）→ 必仍红：读数 `FAIL c11 references/30-gates.md 出现人工闸正文短语『外部权威』（第二真源）` exit 1（同读数附 `FAIL c01 包目录名…`＝副本目录名所致，与判据无关，照登）；
   - 态③「外部权威」出现在非 A 行且不含「人工闸」（副本包）→ 必仍红：同 `FAIL c11 …『外部权威』` exit 1。
2. **T-A3 剔出 EXPECT_TARGETS**（裁定二 `6b0fc5d`·丁案窄化）：T-A4 留靶点面（OP-del／OP-rev／OP-pad 三咬全过，见 --mutate 读数）；EXPECT_TARGETS 处注释行指 `6b0fc5d`。替代护栏对抗实跑（仓外副本）：A3 行「**行级唯一**」→「**行级重复**」→ `FAIL c23 承接项 A1–A4 内容摘要不等于期望` exit 1；复原→`exit 0 fails=[]`。
- D09 锚随 M-4 重设（裁定二准）：旧锚「**本技能不自产编号，也不自产角色位号**」被 M-4 消去＝MUTATE_FAILED 事实（重算前实测 `!! c26 D09 … MUTATE_FAILED 锚在本包任一文件均不存在`）；新锚「**编号两分发放**：**来源面／跨包编号**」→「**编号全部自造发放**：**来源面／跨包编号**」＝`BITE c26 D09 §11『编号两分发放』反转为『编号全部自造』… -> §11 整节摘要不等于期望` OK-RED。
- v3/S-5 牵动清单未预见面＝三处（c11 探针冲突／D09 锚消去／c24-T-A3 无 REV 词）——均由停手上报→在途裁定承接，补记归裁定件＋本回执，v3 原件 append-only 零触。

## ⑦ 行数实测 vs 预算差值登记

SKILL.md 92（零触）／10-contract 225（Δ0）／20-artifact 52（Δ0）／30-gates 100（Δ0）／40-provenance 43（零触）／claim-register 45（Δ0）／outbound-artifact 33（零触）；合计 590＝预算 Δ0；表结构列数七件全零变化（表头行对拍全等，判据 2）。

## ⑧ 仓外临时目录与仓内洁净读数

- 仓外＝`C:\Users\peter\AppData\Local\Temp\tmp.0X1GAVqZrz`（规格 blob 副本／三生成器补丁器／正反样本／对抗副本包 adv·adv2·guard2／租约 l1.jsonl）——批毕清理，清理读数见完工回报（宿主 safe-delete 对含盘符路径会拒，清理用 python `shutil.rmtree` 于 python 通道执行，子目录 adv/adv2/guard2 已随各自用例先行清理）。
- 仓内：本批曾生成 `agent-experts/baigong-software-team/skills/sop/scripts/__pycache__/semantic-governance.cpython-313.pyc`（写集外·py_compile 残留）→ 已 `rm`；后续跑脚本全程 `PYTHONDONTWRITEBYTECODE=1`。
- `git status --porcelain --untracked-files=no` 收口读数：空（他案未跟踪面照登，见完工回报）。
- 提交纪律：三笔各自 `git add`／`git commit` 双侧显式逐路径 pathspec；未用 `-A`／`--amend`／`reset`／`--no-verify`；pre-commit 门禁照常通过（advisory WATCH 长输出照登，未改门禁）。
- 并发照登：开工 HEAD `f780ce4`→收口区间他案线续笔（`d444a37`/`6b0fc5d`/`b47709e`/`f364803`/`55af9fb` 等）照登不碰；一次 `.git/index.lock` 撞锁（他案在持）→等待空位后落账，未删锁。

## 三态明示

1. **做了但没落盘**：本回执落笔前的全部抽取／重算／变异／对抗实跑在仓外临时目录进行，读数以命令输出誊入本件；仓内无临时脚本无中间文件（pyc 残留一处已即删，见⑧）。
2. **落盘了但没提交**：本文件写入 `.scratch/tickets/` 后至 `git add` 前为工作区新文件态。
3. **提交了但没对账**：回执笔 commit 后至完工回报给出「`git status` 他案照登＋各笔 sha＋`git show --name-only` 逐笔对件」三项实测前，此态存在；由完工回报补齐。

## 收口即停

射程止于「四件＋两件＋夹具随动落成＋三笔落账＋本回执」。未跑 QA 独立验、未复跑试填、未动 T3–T6／升号／装配／部署。

## 补记（append·裁定二 `6b0fc5d` 读数要求项）

- 剔 T-A3 后靶点计数（`--stats`）：靶点 60 个；REV 对 38 组；`EXPECT_TARGETS` 长度 60（T-A3 不在场＝False，T-A4 在场＝True）。
- `--selfcheck` 锚唯一计数：靶点 60 个，锚唯一命中 60 个，不合格 0 个。
- 裁定二读数预期核对：`--all` 余 FAIL 0（甲案补丁已落夹具后 c11 消，28 OK／exit 0）；`--mutate` MUTATE_FAILED 0（244 全咬）。
- 本补记＝回执 append 一笔（照仓内回执 append 先例，回执原件段落不删不改）。
