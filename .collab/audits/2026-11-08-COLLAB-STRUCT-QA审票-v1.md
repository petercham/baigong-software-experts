# COLLAB-STRUCT 票包 QA 席独立审票 v1（B席·fresh eyes·证伪导向）

- 审席：qa-structc1｜审期开工读数：`2026-11-08 20:35`／开工 HEAD＝`cde6f90`（≥派工下限 `4e5b630` 对钉）／`git status --porcelain --untracked-files=no`＝空（tracked 面净）。
- 被核件（blob 开工复算全等）：
  1. `.scratch/tickets/2026-11-08-COLLAB-STRUCT-1-结构名实对齐与规范成文票-v1.md`＝191 行／24,590B／sha256 前 12 `f5f1222dfdb9`（复算＝`f5f1222dfdb960b8…` ✓）；
  2. `.scratch/tickets/2026-11-08-COLLAB-STRUCT-B345-工序纪律并案维护票-v1.md`＝115 行／9,763B／前 12 `2cbc268b`（复算＝`2cbc268b0f489b46…` ✓）。
- 审尺真源直读：`.collab/decisions/2026-11-08-皮总裁定-collab结构规范重定义与缺陷清单并案.md`（b8bdadc·blob 5,056B／sha256 前 12 `ea8061101341` 复现 ✓）；两票所引其余真源 commit 全部实证存在：`c848a78`（blob 8,772B／`cea90e88afa9` ✓）／`0259cd6`（blob 6,272B／`9dc187945f91` ✓）／`b2150c5`／`b0b449d`／`b4a75d5`／`b080b9d`／`6cf2767`／`50164c9`——零虚引。
- 只读纪律：仓面零改动；一切施工验证在仓根 `.scratch/qa-structc1/` 隔离 git worktree（`wt-sim`／`wt-base`／`wt-b8bdadc`）内模拟，完工前已全部 `git worktree remove` 删除（读数附本件）。

## 一 总判

**票面整体高质量、真源忠实、基线钉值可复现；但存在两处机械判据自相矛盾（红）与六处规格锚/口径缺陷（黄）。结论＝修票可放行面：R1/R2 须 v2 修，黄项建议随 v2 一并勘正。**

红 2／黄 6／绿 13（逐项判定见下）。

## 二 红项（钉值对不上＝红，两条均为判据自相矛盾）

### R1 §5.3 ls-files 断言与 §6 禁动面／候裁①互斥（审面 3 可机械判定性）

- 票面 §5.3：`git ls-files | grep -c "/\.collab/qa/\|\.collab/qa/"` 路径面＝**0**。
- 实测现值＝**286**（`git ls-files | grep -c "\.collab/qa/"`，双验）；分布＝仓根 `.collab/qa/` 8＋包内 230＋`agent-skills/fuxi-skill/.collab/qa/` 48 含 44+2 与引号路径 2＝46＋`agent-skills/external-advisor-collab/.collab/qa/` 2。
- 票面 §6 明写 fuxi/EAC 两包 qa 面「本票默认不动」、§7 候裁①未拍。本席隔离 worktree 按 §3.B1 只迁两域（8＋230）模拟：迁后该 grep 读数＝**48≠0**→ **判据 3 在票面默认射程下必 FAIL**。判据要么改钉值为 `48（他包存量照登，候裁①未裁前不作 0 判）`，要么把候裁①「并入同批 mv」案写死——二者必择一。
- 注：mv 两域对象数 8＋230＝238 与 §4「mv 面 242＝8+230+4」自洽（+4＝adr 迁入件），此点无矛盾。

### R2 §5.5「mv 改名预期差值≈0」与候裁①案乙（旧文不追改）互斥

- 票面 §5.5：「mv 面 242 件文件名变→路径型 advisory 行改名不减不增＝预期差值≈0」。
- 实测：历史 `*.md` 内 `.collab/qa/` 字面引用存量（b8bdadc 时点复现）＝**205 文件／290 行**（`git grep -l/-c` 对 b8bdadc 复跑＝205/290 精确命中票面值；HEAD 现值漂移至 207/300＝b8bdadc..HEAD 新增链件自然增长，非票面错）。这些行当前指向**实存文件**（可解析）；mv 后若按候裁①案乙不追改，全部转**悬空指针**＝check-pointers 新命中。
- 隔离对拍实证（同一 run-gates `--no-write` 窄口径，worktree 形态）：干净 HEAD 树 `wt-base`＝GATE PASS 发现 **6,586**；模拟施工树 `wt-sim`（242 mv＋A 组改＋B3 补链全套）＝GATE PASS 发现 **6,598**＝**+12**（分项：check-pointers 行 3,972→3,992 **+20**、check-ticket-reconcile 144→165 **+21**、check-pointer-closure 2,090→2,082 −8）。差值非零且方向确定为**增**——「≈0」预期与票面自身候裁①案乙直接矛盾。主盘形态（含 untracked 取证树）该增幅只会更大（引用行基数 290）。
- 修票建议：§5.5 预期改「差值>0 属候裁①案乙既有语义，逐条归因即可」或改判据为「GATE PASS 不翻红＋差值全部归因到 mv 引面」，删「≈0」钉。

## 三 黄项（规格锚错位/口径缺口，不推翻票面主结构）

### Y1 A1.6 键名错位：`write_globs_note` 实为 `deny_globs_note`
- 票面 A1.6「`write_globs_note` 内三子域对表句随之改…`drafts/deploy` 字样改 `drafts`」；实测 engineer 行 `write_globs_note`（:54）无 `drafts/deploy` 字样，该字样实在 **deny_globs_note**（:59）内。模拟施工按票面字面替换不命中＝须按实物键改。锚点错、语义可达→黄。

### Y2 「十一桶」旧计数随动面缺失
- 票面 A4 桶闭集换代 11→16，但全仓「十一桶」字样 occurrence 口径＝**34**（`git grep -o | wc -l`），分布于 config 两文件（seat-permissions.json `:7`、`:59` deny_globs_note／hooks-map `:29`）、六技能包 `.collab/README.md`、包 README 等——票面 A 组随动清单与 §5.2 判据 grep 均不覆盖「十一桶」字样→施工后 config 真源读「16 桶」、旁注仍读「十一桶」＝规范面自相矛盾残留。建议 A1/A2 补字样随动行＋§5.2 grep 补钉「十一桶」在 config 两文件＝0。

### Y3 A4 新 16 桶闭集漏 `returns/`（既有 tracked 实体桶）
- 新闭集＝decisions/audits/receipts/board/design/research/refs/evidence/inbox/process/dispatch/drafts/adr/architect/product/ledger——无 `returns/`；实测仓根与包内 `.collab/returns/` 均有 tracked 实体（仓根 2 件），engineer 行 write/deny 均在用 `returns/engineer/`。规范件现行 `:12`「闭集外目录名不入规范」条款下，16 桶漏 returns 使既有实体桶落闭集外。与裁定「未列子包存续不禁」不冲突（六目录非闭集限定），但**规范真源自身的桶名闭集行**与其自身实体面矛盾→黄，建议 v2 补 `returns/`（17 桶）或在规范件注记未列桶语义。

### Y4 §5.6 判据前提失效：drill-05／drill-06 **开工基线即红**，票未附基线读数
- 本席直跑（两形态：系统 Temp `mktemp -d` 与 `/tmp/qastc1` 各一）：`drill-05-freeze-recover.sh` exit 1（RED：`deny 原因非 freeze 联动`）；`drill-06-replay-reconcile.sh` exit 1（RED：`负扫面命中读数缺位`）。
- 红因定位（只读取证）：drill-05 因 write-guard deny 输出走 `ensure_ascii=True`（write-guard.py `:234-240`），reason 落盘为 `\uXXXX` 转义，drill-05 的 `grep -q 'B10 freeze 态全写 deny'` 中文明文必不命中（`w1.txt` 实测：deny 在位、`B10 freeze 态全写 deny` 明文命中数＝0）——**freeze 联动行为本身正常**（手工复现 deny 在位），系夹具 grep 与脚本输出编码不匹配；drill-06 因夹具引用目标 `.collab/archive/old-note.md` 不存在＋shadow-replay 脏件扫描 exit 0（应 exit≠0）→`replay-dirty.json` 未生成。b8bdadc 时点两 drill 夹具与 write-guard 同体（`git log b8bdadc..HEAD -- <四件+两 config>` 空）＝红在票前既有。
- 矛盾点：§5.6 判「施工后复跑 exit 0」且 §6 禁动面锁死脚本本体＝工程师无法在射程内修红因。票面 §1 只附 run-gates 基线未附两 drill 基线读数。→黄（判据不可达风险＋基线未钉），建议 v2 补两 drill 开工基线实测＋红因呈报或豁免条款。

### Y5 §5.7 check-adr「现态 exit 0／读数须同值」裸跑不成立
- `python agent-skills/object-audit/scripts/check-adr.py` 裸跑＝**exit 4**（infra error：根锚四序皆空）。票面所引读数「exit 0／docs/adr 盘上件=1／桶1=1 桶2=20 桶3=1」只在带 `--bundle-root`（或 run-gates 内路由）形制下复现——run-gates 内该值两形态均复现 ✓（`桶1=1 桶2=20 桶3=1｜发现 0｜exit 0`）。判据须写明调用形制→黄。

### Y6 基线 31,875 只在主盘工作区形态可复现，跨形态不可复算
- 主盘 `run-gates.sh --no-write` 实跑＝GATE PASS 发现 **31,878**（对票面 31,875 差 +3，归因＝b8bdadc..HEAD 新增链件：`重蒸批-批计划`／`重蒸批RB1首`／`FUXI-重蒸批-架构席` 三件各入 check 面 1 行命中；五枚 decisions 新件命中 0——+3 逐条对上，口径无异常）。
- 但同一 b8bdadc 检出在隔离 worktree 复跑＝**6,582**、干净 HEAD worktree＝**6,586**——主盘与 worktree 形态读数差一个数量级（主盘扫描含工作区 untracked 取证树）。§5.5「对基线 31,875 窄口径零回归」须钉死**同形态（主盘工作区）**＋开工/收工两读数对拍，否则不可机械复算→黄。窄口径单一真源行（run-gates.sh `:516` print）实证在位 ✓。

## 四 绿项（逐条实测对上，13 项）

1. §1.1 十一件钉值全等：seat-permissions.json 73/8,655/`2e92c7b97af2`、hooks-map 40/4,003/`0d25b6057c93`、collab-fixed-structure.md 27/1,719/`403db8e0e0f5`、包内 README 12/635/`9e9397c74902`、仓根 `.collab/README.md` **确不存在**、四席位卡 46/3,227/`a1c6a4f8ecce`／47/3,825/`1c51935d3ca6`／49/3,848/`0bcda097f0f7`／49/3,951/`b4331d7422c4`、lead 卡 77/5,298/`c2287132f1e8`（grep drafts/qa/audits＝0 命中 ✓ 零触碰成立）。
2. 四席位卡 `:22` 行现值逐字对上票面引文（含 qa 卡「`.collab/audits/` 悬空指空」实锤：`.collab/audits/` 实体确不存在；engineer 卡含 `drafts/deploy/`）。
3. §1.2 仓根 `.collab/`：实体子目录 13 ✓、根面散件 20 md ✓＋`tmp-w7-msg.txt`（untracked＋gitignore `:36` 命中 ✓票面「非链上对象 rm 即可」成立）、tracked 84（b8bdadc 时点复现 ✓；HEAD 89＝链上自然漂移，票钉落笔时点如实）。
4. §1.2 包内：13 子目录（含 drafts/product 无 architect/adr/audits/tickets）✓、tracked 593 ✓、qa 230 ✓、drafts 4 件全住 `drafts/adr/` 顶层 0 散件 ✓。
5. 他包 qa：fuxi 46 ✓、EAC 2 ✓；adr 四件现落位 `drafts/adr/` 逐件点名 ✓。
6. ledger untracked 恰三文件 ✓（点名三路径与 `git status` 全等；仓根 ledger.jsonl＋包内 leases/ledger.jsonl；ledger 三件不在 gitignore 排除面＝`git check-ignore` exit 1，补链无 ignore 障碍 ✓）。
7. 历史引用存量（b8bdadc 复现）：`.collab/qa/` 205 文件／290 行 ✓；`drafts/adr` 26 行 ✓（occurrence 口径双验＝328／40 附登，票面用行口径标注为「行」＝口径如实）。
8. tests 三件样例引用行级全等：drill-05 `:17/:22/:27/:49`、drill-06 `:20`、test_lease `:95/:96` 逐行对上 ✓；`lease-issuer.py:127-130` 子集校验＋`:160` config 默认、`write-guard.py:321` map 默认、`lease-issuer :130` startswith 语义（A3 引）实证 ✓；`freeze-unfreeze.py`／`dispatch-builder.py` 存在 ✓；门禁/守卫脚本面 grep `.collab/qa`/`drafts/prd` 等硬编码＝**0 命中**（`git grep -- scripts hooks`）✓＝票面「读 config 非硬编码＝零随动」实证成立。
9. §5.1 判据：两 JSON `json.tool` exit 0 ✓；五席 deny_globs 逐席全等实测＝True（host/product/architect/qa/engineer）✓——模拟 A1/A2 同批改后仍全等 ✓。
10. §5.4 判据模拟实证：隔离树按 §3 全套 staged 后 `git diff --cached -M --name-status`＝**R100 恰 242**、非 R100 的 R 行＝0（mv 保 blob 全真）✓；audits 8＋230 tracked 到位、`.collab/adr/`＝4、`architect/`≥1、ledger 三件入链 ✓（判据 3 其余子断言全过，唯路径面 0 见 R1）。
11. A6 gitignore 语义实证：`git check-ignore` 对 `…/.collab/audits/x.md` 与 `…/.collab/qa/x.md` 两态均 exit 1（不 ignore）＝「改名零 ignore 行为变化」✓；`:13` 注释行含 qa 字样仅此一处 ✓。
12. 候裁②③④⑤⑥与正文无互斥：②散件 20＋tmp 与 §6 一致；③`drafts/archive/` 与裁定§三「归档子包」条款一致且 lease-issuer startswith 语义实证支持「零新增配置行」论；④三同源版本号现均 0.1.30 实测 ✓ 与「零 bump」一致；⑤SEMGV-T3 `b4a75d5` 在链属实、五卡 `:22` 交叠面实证；⑥`.collab/tickets/` 无实体（两仓点 ls 皆无）与票面体例陈述一致。唯候裁①与判据 3 互斥＝已计入 R1。
13. B345 票基线：SKILL.md 26/4,805/`2e1122c2f7ea`＋`version: 1.1.6`（:5）✓、handoff 78/6,263/`971a8a35ad3e`✓、dev 131/12,071/`5336693548f9`✓（§八 :80 起四款在位，款 3 内容对上）、dispatch 22/1,446/`831c2734baad`✓（§二 存在 :14）、TEMPLATE（包内 `.scratch/tickets/`）48/2,877/`33d5f2f1bada`✓（:20-24 自检节「附读数」体例对上）；B3 口径差取证三读数全复现：b080b9d 回执内 24579/12494 ✓、6cf2767 QA 件内 31429/19007/垫空格 ✓、本席开工实跑 31,878/票称 31,875（链漂移 +3 归因见 Y6）✓；两票写集零交叠自证成立（B345 闭集四件不在主票 §4 闭集内，逐行对读 ✓）。

## 五 审面 2（WorkBuddy 平台兼容性）单列读数

- 目录规范换代 11→16 与现行门禁/守卫引用面冲突实测：run-gates.sh 路由表（:141 SCRIPTS 九名）只调 check-* 九件＋`ROOT/tools/check-source-of-truth`；九件＋tools 面 grep 硬编码 `.collab/qa`/`drafts/*`＝0；`check-collab-lint.py` 只锚 `/decisions/`、`/tickets/` 段（:91）；`check-adr.py` 锚 `.collab/decisions`＋`docs/adr`（:91-92）＋活引用正则 `\.collab/[a-z]+/…`（:105，advisory 级）——换代不需改任何脚本本体即通，票面「机件零触碰」兼容成立 ✓（引用路径全部 Glob/ls 实证存在后才引用，含 `tools/check-source-of-truth.py`）。
- 唯一兼容性缺口＝Y2（十一桶字样）与 Y3（returns 桶）两处措辞面。

## 六 计数与读数台账（本席复测取证面，已随完工删除）

- 取证目录＝仓根 `.scratch/qa-structc1/`：worktree 三枚（wt-sim/wt-base/wt-b8bdadc，另 wt-repo 一枚用毕即删）＋run-gates 输出五份＋drills/s2 输出六份＋junction 两枚（姊妹仓解析锚）。完工前处置＝`git worktree remove --force` 全数＋junction/输出文件删除；本件为唯一新增落盘件。
- 关键复测读数：主盘 run-gates 31,878 exit 0／b8bdadc worktree 6,582 exit 0／干净 HEAD worktree 6,586 exit 0／模拟施工树 6,598 exit 0（分项见 R2）；R100=242／qa 路径面 286→48（模拟后）；s2 `test_lease_instantiation.py` 基线与模拟后均 exit 0（PASS 全列）；drill-05/06 两形态均 exit 1（见 Y4）；check-adr 裸跑 exit 4、run-gates 内 exit 0 读数同值。
- 三态明示：做了未落盘＝上述全部复测（仓面只读，worktree 树已删）；落盘未提交＝本件至 commit 前为工作区新文件态；提交未对账＝commit 后由完工回报附 `git show --name-only` 恰本件＋status 他案照登补齐。

## 七 判定汇总

| # | 判项 | 态 |
|---|---|---|
| R1 | §5.3 路径面=0 vs 默认射程残留 48（候裁①未拍） | 红 |
| R2 | §5.5 差值≈0 vs 案乙必增（实测 +12，check-pointers +20） | 红 |
| Y1 | A1.6 write_globs_note→实物 deny_globs_note | 黄 |
| Y2 | 十一桶字样随动缺失（config 两文件在列） | 黄 |
| Y3 | 16 桶闭集漏 returns 实体桶 | 黄 |
| Y4 | 判据6 drill 基线即红＋禁动面锁死修路 | 黄 |
| Y5 | 判据7 check-adr 调用形制未钉 | 黄 |
| Y6 | 31,875 基线跨形态不可复算须钉同形态 | 黄 |
| G1-G13 | §1.1/§1.2 钉值、引用行级、JSON/五席全等、mv 保真 242、gitignore 语义、候裁②-⑥无互斥、B345 全基线＋三读数复现、脚本面零硬编码等 | 绿 |

**总判＝两件均非废票级：主票 COLLAB-STRUCT-1 需 v2 修 R1/R2＋勘 Y1-Y6；B345 仅一行锚勘（§1 现 §七 三律首句实在 :40 非 :45，append 位「§七 段尾」不受影响）随 v2 顺手，判据四条本体绿。**

——qa-structc1·本件＝唯一落盘产出·哈希链随单笔 commit 入账。
