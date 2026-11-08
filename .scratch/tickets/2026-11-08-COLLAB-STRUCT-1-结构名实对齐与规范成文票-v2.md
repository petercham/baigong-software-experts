# COLLAB-STRUCT-1 .collab 结构名实对齐与规范成文票（架构席·过程件规格票·纯规格零施工）v2

- **票号**：COLLAB-STRUCT-1｜**版本**：v2（append-only 序链 v1→v2；v1＝f5f1222dfdb9／24,590B／4e5b630 落链，本件取代其为施工依据）｜**起草席**：架构席（arch-struct1c）
- **开工读数（实测）**：`date`＝`Sun Nov 8 22:22:26 2026`（本机时钟）／HEAD＝`67a3462`（＝派工令预期钉值，对钉成立）／`git status --porcelain --untracked-files=no`＝空（tracked 面净；他案 untracked 取证面照登不碰：`.scratch/FX-U1x*`、`.collab/ledger/`〔本票射程内补链对象〕、`.collab/tmp-w7-msg.txt`〔候裁②对象〕、research 散件等）。
- **裁定真源（条款依据·已完整直读）**：
  1. `.collab/decisions/2026-11-08-皮总裁定-collab结构规范重定义与缺陷清单并案.md`＝`b8bdadc` 落链（blob 5,056B／`ea8061101341`）——结构裁定七条。
  2. `.collab/decisions/2026-11-08-皮总裁定-ADR工序写入权与drafts治理.md`＝`67a3462` 落链（blob 3,339B／`16fe47f5d145`）——**v2 追加输入**：ADR 统一主理人写／会签＝状态闸／人类闸按产品设计层分级／会签＝讨论流程任意席位可发起·主理人组织／时序＝收口→呈报人类→正式 ADR 件／ADR drafts 交接件一题一文档禁多版本存活。
- **修单来源（v2 唯一修订条款面）**：
  - `.collab/qa/2026-11-08-COLLAB-STRUCT-双席审票会师对拍与裁定-v1.md`（`agent-experts/baigong-software-team/.collab/qa/`，commit `36dfb78`，blob 5,373B／`7843fb3bf7f9`）＝红三黄七合并清单＋裁定「两票非废票级、主票出 v2、修单只是输入作者席亲笔、候裁六项继续单列不重审、红-1/红-3 钉值终态挂候裁①」。
  - 皮总 ADR 裁定件（上 2.）随动面＝其 §三 连带影响清单（seat-permissions adr 写域改判／ADR 工序真源 `b0b449d` 链改写／一题一文档细则）。
  - **修单之外零自扩射程**；工具归属/shareds 自包含议题＝另票 TOOLHOME（已径裁，不入本票）。
- **v1 双席审票基准**：A 席 `559f2a8`（红2黄5绿11）＋B 席 `93434e0`（红2黄6绿13）——已会师对拍，本票不重审只落位。
- **两笔封顶兑现**：本票＝主票第二笔（v1＋v2 恰封顶）；v2 回来后双席窄复核（改哪段复验哪段），不开新面、不再出 v3。
- **v1 处置行（ADR 裁定⑥「一题一文档、禁一题多版本存活」落笔）**：v2 落链起，同题施工依据存活态唯一＝本件 v2；v1 链上件照登不动（append-only 史实锚，PROJINIT v1/v2、SEMGV-T1 v1-v5 多版链先例同构），v1 自此**不再是施工依据**——B2 实例化、工程师施工票、双席窄复核一律指向本 v2。
- **门禁基线（本席开工时点实跑）**：`bash agent-skills/object-audit/scripts/run-gates.sh --no-write` ＝ **GATE PASS exit 0／发现 31,885**（主盘形态；较 v1 起草时点 31,875 漂移 +10＝`b8bdadc..67a3462` 区间新增链件路径型 advisory，照登；跨形态比数禁令见 §5 判据1）。

## 0 已入账裁定转录（忠实执行，不复议）

**结构裁定（`b8bdadc`）七条——同 v1 §0：**
1. drafts 分子包＝**错误定义废止**：交接件草稿直接落 `drafts/` 顶层，无子包（归档子包除外）；每交接件只留一件存活态最新版，过期版本入归档子包。
2. **adr 单立 `.collab/adr/`**（不在 architect/ 下）——条件问「adr 可否涉产品需求变更」裁定取证＝是（ADR 工序链 `b0b449d` 三方会签含产品席＋ADR-0001 产品席保留项 R-PM-1 `b2150c5`；业界锚见 A4 依据行〔黄-7〕）。交付面 `docs/adr/` 终写位不动；过程面 `drafts/adr/` 四件迁入。
3. `architect/`＝架构席非交接件写权域——规格有域无实体，须补建。
4. `audits/`＝名实对齐：实体 `qa/` 改 `audits/`（仓根＋包内），席位卡／seat-permissions.json／hooks-map 同批随动。
5. `ledger/`＝两处 untracked 补 commit 入链。
6. 未列子包（board/dispatch/evidence/inbox/process/receipts/refs/research/returns 等）存续不禁，按项目阶段取用。
7. 六目录定位＝需求最终确认前阶段的标准界定，非全生命周期闭集（目标态表头注必带该限定）。

**ADR 工序裁定（`67a3462`）六条——v2 新增：**
8. **写权改判：ADR 统一由主理人写**（推翻甲案架构席终写／乙案会签补件区两候裁＝销账）；seat-permissions 现值须随此改判重排。
9. 会签＝状态闸：相关席位会签收口＝通过判定；收口结果呈报人类（知悉/授权放行）。
10. 人类闸分级：涉产品设计层→必须人类授权放行；不涉→会签收口可自决。
11. 会签＝讨论流程（同构）：任意席位可发起；主理人组织相关席位参与讨论和会签。
12. 时序：讨论/会签→收口→呈报人类知悉/授权放行→形成执行交接的正式 ADR 件。
13. drafts 治理随大盘：讨论过程中的 ADR 交接件＝drafts 成员，与其他 drafts 同治理原则；一题一文档，禁止一题多版本存活。

## 1 现态基线钉值（v2 落笔前 67a3462 时点实测）

### 1.1 配置与规范面（逐件行数／字节／sha256 前 12）

| 件 | 现态（v2 复点，与 v1 §1.1 全等＝本区间零扰动） |
|---|---|
| `agent-experts/baigong-software-team/config/seat-permissions.json` | 73 行／8,655B／`2e92c7b97af2` |
| `agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json` | 40 行／4,003B／`0d25b6057c93` |
| `agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md` | 27 行／1,719B／`403db8e0e0f5` |
| `agent-experts/baigong-software-team/.collab/README.md` | 12 行／635B／`9e9397c74902` |
| 仓根 `.collab/README.md` | **不存在**（审计实锤） |
| `agents/software-team-product.md` | 46 行／3,227B／`a1c6a4f8ecce`（`:22` 含 `.collab/drafts/prd/`） |
| `agents/software-team-architect.md` | 47 行／3,825B／`1c51935d3ca6`（`:22` 含 `.collab/drafts/{design,adr}/`＋`docs/adr/`；`:23` 含「`docs/adr/` 除外」例外子句；`:24` 可写内容含「ADR」） |
| `agents/software-team-qa.md` | 49 行／3,848B／`0bcda097f0f7`（`:22` 含 `.collab/drafts/proposals/`；`.collab/audits/`＝悬空指空） |
| `agents/software-team-engineer.md` | 49 行／3,951B／`b4331d7422c4`（`:22` 含 `.collab/drafts/deploy/`） |
| `agents/software-team-lead.md` | 77 行／5,298B／`c2287132f1e8`（**v2 改判：非零触碰**——`:50` 席位派发路由行含「系统设计、ADR、开发票、边界约束 → software-team-architect」＝ADR 裁定随动面） |
| `skills/software-orchestration/references/standard-sop.md` | `:50` 起「ADR 工序（决策记录链）」节六款——`:52` 链序款＝`b0b449d` 工序链成文面（「…四方收口草案→架构席终写入 `docs/adr/`」）＝ADR 裁定⑧改写对象 |
| `.gitignore` | `:13` 注释行含 `.collab/{decisions,qa,receipts,board,research}/` 字样（注释面，行为零关） |

### 1.2 目录实体与 tracked 计数（67a3462 复点）

- 仓根 `.collab/`：根面散件 20 件 md（＝`.collab/defects/` 桶建立后计数，与 v1「20 件」同值）＋`tmp-w7-msg.txt`（untracked）；实体子目录含 `qa/`（tracked 8）＋`defects/`（tracked 1＝drill 夹具缺陷台账 `1324B`，`36dfb78` 落链）。**无 drafts/product/architect/adr/audits 实体**。仓根 `.collab/` tracked 合计 93 件（含 defects 桶新增；其中根面散件 20 件全 tracked）。
- 包内 `agent-experts/baigong-software-team/.collab/`：tracked 594 件（＝v1 593＋会师裁定件 1）；其中 `.collab/qa/` **231 件**（＝v1 230＋会师裁定件）；`.collab/drafts/` 4 件全部住 `drafts/adr/` 子包（drafts 顶层散件＝0）；`returns/` tracked 2（仓根另 2＝在用实体桶，黄-2 取证）。
- 其余包 qa 面（候裁①射程对象）：`agent-skills/fuxi-skill/.collab/qa/` tracked **46**；`agent-skills/external-advisor-collab/.collab/qa/` tracked **2**；合计 **48**（与 §5.3 两态钉值一致）。
- ledger untracked 恰三文件（复点）：`.collab/ledger/ledger.jsonl`、`agent-experts/baigong-software-team/.collab/ledger/leases.jsonl`、`…/ledger.jsonl`。
- 历史文内旧路径引用存量（67a3362→67a3462 已漂移，照登）：tracked `*.md` 内 `.collab/qa/` 字面＝**209 文件／308 行**（v1 时点 205/290＋本区间审票/会师链件自带引用）；`drafts/adr` 字面＝**46 行**（v1 26＋同区间增量）。迁移射程测算按 §7 候裁①两态口径。
- 「十一桶」字样存量（黄-1 取证，67a3462 实测）：全仓 occurrence＝**42**（`git grep -o "十一桶" | wc -l`）；baigong 包内＝**19 occurrence／15 行**，其中**在用规范/配置面＝4 处**（`seat-permissions.json:7`＋`:59`〔×2 occurrence 同行〕、`seat-permissions-hooks-map.json:29`、包内 `.collab/README.md:5`），其余 15 occurrence＝历史案卷（qa//receipts/research/版本账 v0.1.18 行）＝append-only 不追改；六外包 `.collab/README.md` 各 1＝跨包面（§7 候裁⑦）。
- 键名错位钉证（红-2）：`drafts/deploy` 字样实在 `seat-permissions.json:59`＝engineer 行 **deny_globs_note**（非 v1 A1.6 所称 write_globs_note `:54`）；`:54` write_globs_note 内无 drafts 字样。配置/席位卡/规范真源三范围 drafts 子包字面现值＝**13 行**（本席 `-E` 实测）。
- 夹具/消费面随动取证：`drill-05-freeze-recover.sh`（`:17/:22/:27/:49` 用 `.collab/drafts/prd/` 样例）、`drill-06-replay-replay-reconcile.sh` 同款 `:20`、`test_lease_instantiation.py:95/:96`；`lease-issuer.py:127-130` 子集校验按 write_globs 行逐字命中；`check-adr.py` 只锚 `docs/adr`＝零随动（命令形制钉值见 §5 判据7）；`.gitignore` 对 `.collab/audits/x.md` 两态均不 ignore（`git check-ignore` exit 1 实测）。
- **基线读数钉（本席 67a3462 实跑）**：`drill-05` exit **1**／`drill-06` exit **1**（红基线，红因＝缺陷台账 `.collab/defects/2026-11-08-drill夹具回读编码失配与缺件引用缺陷-v1.md`〔`36dfb78` 链〕＝黄-5 判据改差值口径的对象）；`python agent-experts/baigong-software-team/tests/s2/test_lease_instantiation.py` exit **0**；`check-adr.py` 裸跑 exit **4**（infra error，非用态）；`check-adr.py --bundle-root agent-experts/baigong-software-team` exit **0**／`docs/adr 盘上件=1｜桶1=1 桶2=20 桶3=1`。

## 2 施工规格 A 组：配置与规范成文（逐件行级，规格文本逐字入票）

> 施工序约束：A 组与 B 组迁移**必须同批一 commit**（配置指新名／实体已就位，两态不并存）。
> 行号锚＝67a3462 现态读数；施工票开工读数须复点，行号漂移按内容锚定位。

### A1 `config/seat-permissions.json`（