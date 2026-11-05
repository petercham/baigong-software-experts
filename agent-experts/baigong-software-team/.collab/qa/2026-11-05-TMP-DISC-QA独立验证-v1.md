# TMP-DISC QA 席独立验证 v1（qa-tmpdv·fresh eyes·证伪导向·工程师自报零采信）

- 开工读数：HEAD `67ebb4e`（`git rev-parse --short HEAD` 实测）；`git status --porcelain`＝`?? .collab/ledger/`（既往呈报账本残项，如实登记未触碰）。
- 完工时 HEAD 已推进至 `b0e9fb9`（他席在途笔：`138e39a` 票面 v2 时序注记／`c4ae3e3` ADR 调研 v2／`75d6cfc` ADR-L0 开票／b0e9fb9——均系 TMP-DISC 链外交互笔，并发登记）。
- 总裁决＝**放行（红 0／黄 1／绿 15）**；黄-1＝A8 仓外系统 Temp 面本批相关证据文件一枚残留未清（见下）。
- 口径：occurrence 计数＋`git -c core.quotepath=off`；扫描/比对实现全部本席自写（Python 逐字节 diff、AST 对拍、集合对账），工程师读数一律未复用。

## 0. 对账三方全等＋链核

- 票面声明闭集（`.scratch/tickets/2026-11-05-TMP-DISC-temp-workspace-discipline-ticket.md` 声明段 15 行，本席正则抽取）＝`git show --name-only 1274dbf`（15 行）＝回执清单 15 行：**集合全等 ✓**（自写脚本 `set^==∅`）。注：回执清单排列顺序≠name-only 顺序（集合口径全等，顺序登记为读数级观察）。
- 面分账：`1274dbf` 面＝恰 15 件＝闭集（零越集）；`4d7bd8c` 面＝仅票面文件（修票二笔＝票面授权落笔）；`67ebb4e` 面＝回执＋回流件（`.collab/receipts/`＋`.collab/returns/engineer/`，回执笔治理面）；`git diff 607c600..67ebb4e` 面＝闭集 15＋票面＋回执＋回流＋他席调研件 1（`d9a7b1d`＝arch-tmpd ADR 调研笔，链间他席笔另账登记，不入本批）。
- reflog 全 `commit:` 条目（本批链区间）＝**零 amend／零 reset**；开工帽链核：`1274dbf parent=607c600` ✓；`4d7bd8c parent=1274dbf` ✓；`67ebb4e parent=d9a7b1d`（链间插他席笔，如实登记）。

## 1. A1–A6 逐判据独立复跑（本席实跑）

- **A1**：`^## 八 临时工作物落位与清理纪律`＝**1**；四条款锚句（`适用范围＝一切临时工作物`／`唯一落点＝所属项目仓根`／`收口登记票必含清理判据`／`禁写仓外临时路径模板`）各＝**1**；前值（607c600 面）各＝0。
- **A2 主式**（四 pattern，扫描面＝口径1 排 tests/.scratch/.collab/__pycache__/pyc）：施工前（`git grep 607c600`）＝**4**——逐笔＝票面钉值 4（commit-audit.py:17／decision-pack.py:14／dispatch-builder.py:19／write-guard.py:23）✓；施工后现面命中＝1 行＝`dev-discipline.md:85`〔禁例引〕行＝票面预登记 EXEMPT 逐笔登记，**违例＝0** ✓。
- **A2 宽式 `Temp`**：扫描面命中 4 行，逐笔判因全落票面白名单——①lead 卡 L76「宿主 Temp 区」禁项列举；②README L67 版本账 v0.1.25 行叙述；③dev-discipline L83 §八.2 括号示例列举；④dev-discipline L85 〔禁例引〕句。四脚本新 docstring `Temp` 各 **0** ✓。非白名单命中＝0。
- **A3**：`〔禁例引〕` dev-discipline 单件面＝**1**（前 0）✓。
- **A4**：`席位守则·dev-discipline 卷` 五卡各＝**1**（前值 607c600 面各 0）；`1274dbf` numstat 五卡各 **1 行增量**（1/0 ×5）✓；五卡新行**逐字全等**票面定稿（自写脚本逐行比对：lead 卡＝修订后新句「宿主 Temp 区」措辞逐字 ✓，四共用卡＝同一定稿行逐字 ✓）；旧弃用句「禁写仓外临时路径模板（盘根裸路径…」五卡面＝零在位 ✓；插入位＝各卡「不允许同席多实例并发…」行之后 ✓；权限四行节零动 ✓。
- **A5**：三同源读值 `0.1.25`×3（行号复测＝plugin.json L3／.codebuddy-plugin/plugin.json L3／bundle.lock L5 bundle 块内；components 组件行零动）——前值 `0.1.24`×3 同位 ✓；SKILL `^version:`＝`1.1.5`（前 `1.1.4`）✓；SKILL diff 面＝恰 3 行（description／version／references 索引行）＝S2 三处 ✓，description 两处替换与触发词尾部随动逐字在位 ✓。
- **A6**：`版本账 v0.1.24`＝1＋`版本账 v0.1.25`＝1（前值各 0＝开票侧缺口读数随此填补）✓；README 插入位＝v0.1.23 行后、「## 头像」节前 ✓；append-only（diff 仅 2 增行，既有行零改）✓。

## 2. §八内容对已裁四款忠实（逐句核定）

- 自写脚本：票面 S1 围栏代码块（7 行）vs dev-discipline.md 落地 L79-85（文件末 7 行）＝**逐字节全等**（splitlines 全等＋diff 无差）。四款语义：①一切临时工作物不分席位 ✓②唯一落点＝探针锚项目仓根 `.scratch/<票号>/`＋禁盘根/系统Temp/仓外自建 ✓③收口必含清理判据＋零残留收口态＋消费面人工闸 ✓④派工禁仓外路径模板＋席位拒指权 ✓。追加语境＝现末行「4. 当期无机检义务。」之后（§八前一行＝空行，追加位合规）。
- §八.2 探针锚括注＝`config/seat-permissions-hooks-map.json` **L7「路径锚定」款原文逐字**（自写 JSON 逐行机检：锚句「项目根＝含 docs/STRUCTURE.md 之探针锚目录」L7 含＝True，§八.2 含＝True）。

## 3. 门禁零回归（A7·本席自跑，worktree 洁净面对拍）

- 对拍面＝本席临时区 `git worktree` 检出（`607c600`／`1274dbf`／`67ebb4e` 三态；同级包 `../multi-agent-collab-experts`＋`../multi-agent-collab-skills` 经临时区外部嵌放满足解析——worktree 缺同级包时 check-source-of-truth 报 usage error exit 2＝环境性判因，非门禁回归）。
- `run-gates.sh`：三态均 **GATE PASS exit 0**（发现 5161→5004→5007，本席面内部口径）。零回归判据按本席面内前后对拍：check-pointer-closure **VIOLATION 539→539→539 恒等**（SUBSTR 2941→2949 增 8＝归因 `d9a7b1d` 他席调研件反引号段，非本批）；check-source-of-truth 129 文件｜BLOCK 0｜基线豁免 54｜WATCH 413 **三跑恒等**；check-ticket-reconcile 差分行逐笔判因：新增＝回执指针解析时序（1274dbf 时回执未落＝「缺回执」WATCH，67ebb4e 落笔后消解＝预期流程序）＋他席调研件行；删除＝同左消解行。**交付笔归因新增违例＝0**。
- 四脚本 `python -m py_compile` 全过 ✓；**AST 对拍**（自写，去 docstring 后 ast.dump）：四件 607c600 vs 现面全等＝功能逻辑零动机械证实 ✓（含 docstring 则不等＝docstring 单行差异，与 S3 逐字新句核对全中）。
- tests s2·s3·s4 五件直跑：worktree 基线态 exit 0×5＋主面现态 exit 0×5 前后对拍全绿 ✓（`__main__` 直跑体例，pytest 收集 0＝与回执登记口径一致）。
- 读数级观察（不归因本批·登记）：①工程师申报发现数 9222/9222 在本席 worktree 面不可复现（扫描面构成差异：worktree 无历史 evidence 流水残面＋同级包嵌放形态不同）——零回归结论采本席面内对拍口径；②worktree 面 check-ticket-reconcile 曾出「回执失真·缺项」TMP-DISC 行，**主面直跑零复现**＝归因本席 worktree 环境伪象（内嵌含 .git 的同级包拷贝 `git clean -fdq` 不删所致脏路径面），主面（权威门禁面）回执对账零失真行。

## 4. A8 仓外零残留复核——黄-1

- 盘根：D 根 tmp 族＝`tmp`（mtime 11-05 13:46，先于交付笔 16:40）／`tmp_sky`／`tmp_sky_env`（09-29）；C 根 `temp`／`tmp`（09-07／11-01）——全部先于本批窗口，**本批零新建** ✓。
- 系统 Temp（`%TEMP%`＝`C:\Users\peter\AppData\Local\Temp`；Git Bash `/tmp` 同面）历史残留（`b3tmp`、`qa-*` 族，mtime 10-29～11-04）＝先批既存，照 A8「历史残留登记上报」：**上报**（决策者 11-05 手动清理约 28 项在先，此残系其外存量）。
- **黄-1**：`tmpd-final-gate.txt`（2,217,242 B·birth 2026-11-05 16:48:15＝回执笔落盘窗口内·内容含 TMP-DISC 相关行 26 处＝本批终态门禁证据运行面）残留系统 Temp **未清**。回执 A8 申报「本批相关目录＝0／收口复测双处命中＝0」——「目录」字面不为假，但**文件面漏登未清**，与 §八.3 收口零残留自示范叙事不符。修单＝删除该文件或登记留存去向（微票级，交付面 15 件不受影响）。

## 5. 版本账补记忠实性（v0.1.24 行对 a885ad7 逐目核）

三同源 `0.1.24`@a885ad7（plugin.json L3／.codebuddy L3／bundle.lock L5 实测）✓；`assembly_exclude` publish.py L795 起实装＋bundle.lock L32 五类在册（README／交接件 v2.9 文档／deep-research README／EAC 90-changelog／tests/）✓；EAC ref 换钉 `external-advisor-collab@v1.1.3`（bundle.lock L15）＋组件 1.1.2→1.1.3（`8418b3a` 笔题实证）✓；归因措辞诚实：607c600 README 面 `版本账 v0.1.24`＝0 命中＝「上批漏登记」事实确凿，「据既有 commit 回补」表述与 a885ad7 实体相符 ✓。

## 6. 纪律自证面（本席操作＝§八实证）

- 本席临时区＝仓根 `.scratch/qa-tmpdv/`（26 件证据件含三 worktree＋四份 gates 全量输出＋逐判据中间读数；证据 sha 链：gates_wt600_clean `8a4d2a9a…`／gates_wt127_clean `4b4059a1…`／gates_wt67_clean `64f19cf7…`）。
- 完工清理：worktree 经 `git worktree remove --force`＋长路径 robocopy /MIR 法全删＋`git worktree prune`（`git worktree list` 读数＝本席零残留）；`rm -rf .scratch/qa-tmpdv` → 删除读数：`ls .scratch/`＝`qa-adrlrev tickets`（qa-adrlrev＝他席在途临时区，未触碰），`ls .scratch/qa-tmpdv`＝No such file or directory ✓。
- 事故自报一笔：复测链中一次重定向误将一份 gates 输出文件落至 `.scratch/` 根（`gates_before_607c600_v2.txt`），发现即删（删除后 `ls .scratch/` 读数如上）；系本席命令链 cwd 误判，如实登记。
- 本席写入面＝本报告件一件；`git status --porcelain` 收口＝`?? .collab/ledger/`（既往残项）＋`?? .scratch/qa-adrlrev/`（他席面），本席面零脏项。

## 三态计数与修单

- **红 0**。
- **黄 1**：A8 系统 Temp 残留 `tmpd-final-gate.txt`（本批相关证据文件未清未登记留存去向）——修单＝删除或登记去向，微票收口即可。
- **绿 15**：三方全等／面分账零越集／reflog+帽链干净／A1／A2 主式（前 4 钉值全中·后 0·EXEMPT 恰 1）／A2 宽式全白名单＋四脚本 0／A3／A4（五卡逐字+lead 新句+旧句零在位+插入位）／A5（三同源+SKILL 恰 3 行）／A6＋append-only／§八逐字节全等＋探针锚句 L7 逐字／四脚本 AST 零动＋py_compile／门禁三跑恒等零回归＋tests 前后全绿／版本账补记四要素实证＋归因诚实／纪律自证闭环。
