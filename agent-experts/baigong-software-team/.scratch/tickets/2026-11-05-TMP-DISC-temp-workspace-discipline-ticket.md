# TMP-DISC 临时工作物落位与清理纪律施工票（架构席起草·交付面写入＝工程师席按票施工）

- 开端读数：devkits HEAD 以本票 commit 实测为准；开票侧实测 `git rev-parse --short HEAD`＝`dd3e2cf`（main），`git status --porcelain` 净。
- 背景（决策依据·自包含）：2026-11-05 实证事故——决策者发现盘根堆积约 28 个验证席临时目录（`qa-*-tmp`／`t*-tmp`／`b3tmp`／`tmp-cd1`／`Temp` 等，合计约 350MB），已手动清理、主理人复扫归零。根因两条：①历轮派工书明文要求「复测置仓外 Temp（仓外盘符路径或系统 Temp）」——防仓内污染的动机对，但把垃圾堆到仓外公共区；②收口票无清理判据——各席堆完就走没人收。既有既决：票面落位＝项目 `.scratch/tickets`（2026-11-03 决策者裁定）＋文档治理三层文件域定义「临时层＝项目 `.scratch/`·批毕可弃」——临时区定义本仓已有，历轮未用对。口径＝决策者 2026-11-05 已裁四款（适用范围／唯一落点＝仓根 `.scratch/<票号>/`／收口清理判据／派工件禁仓外 Temp 路径模板＋席位拒指权），本票按此成文，口径不得现场改判。留存归档去向之项目指定归档仓＝仓外归档仓 `multi-agent-collab-archive`（本段登记实例名，交付面条文载泛指「项目指定归档仓」）。
- HOLD：无。
- 改动面闭集＝15 件：（闭集外零触碰）
- 声明闭集：
  - agent-experts/baigong-software-team/skills/software-orchestration/references/dev-discipline.md
  - agent-experts/baigong-software-team/skills/software-orchestration/SKILL.md
  - agent-experts/baigong-software-team/skills/sop/scripts/commit-audit.py
  - agent-experts/baigong-software-team/skills/sop/scripts/decision-pack.py
  - agent-experts/baigong-software-team/skills/sop/scripts/dispatch-builder.py
  - agent-experts/baigong-software-team/skills/sop/scripts/write-guard.py
  - agent-experts/baigong-software-team/agents/software-team-lead.md
  - agent-experts/baigong-software-team/agents/software-team-product.md
  - agent-experts/baigong-software-team/agents/software-team-architect.md
  - agent-experts/baigong-software-team/agents/software-team-qa.md
  - agent-experts/baigong-software-team/agents/software-team-engineer.md
  - agent-experts/baigong-software-team/README.md
  - agent-experts/baigong-software-team/plugin.json
  - agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json
  - agent-experts/baigong-software-team/bundle.lock

开票侧实体核验：以上 15 件 `git ls-files` 实测在位（dd3e2cf）。

回执落点＝`.collab/receipts/2026-11-05-TMP-DISC-工程师回执-v1.md`（文件名级回执指针行）。

## §口径（判据定义·票内自包含）

1. **交付面扫描面**（A2/A3 用）＝`agent-experts/baigong-software-team/` 全 subtree，排除：`tests/`、`.scratch/`、`__pycache__/`、`*.pyc`、`avatars/`。既往历史票（`.scratch/tickets/`）内旧措辞＝史实记录 append-only，不入违例计数（扫描面已排除，登记读数即可）。
2. **旧措辞主式**＝`-e "重定向至 Temp" -e "置系统 Temp" -e "仓外 Temp" -e "置仓外 Temp"`。施工前缺省扫描面基线读数＝4 命中（四脚本 docstring 各 1，开票侧实测 dd3e2cf）——不得按「本就不含」跳过 S3。
3. **禁例引标记**＝〔禁例引〕：交付面内引用被禁旧措辞作作废声明的句，带此标记方入白名单（先例＝CLN-PURE 禁例引口径）；S1 成文已带标记。
4. 全部行号锚为 dd3e2cf 读数；工程师施工以 pattern 命中为准，命中与票面预期不符按实测登记上报（H6）。

## S1 dev-discipline 卷 §八 新节（逐字·append 至卷末）

`agent-experts/baigong-software-team/skills/software-orchestration/references/dev-discipline.md` 文末（现末行「4. 当期无机检义务。」之后）追加，逐字照录：

```

## 八 临时工作物落位与清理纪律

1. 适用范围＝一切临时工作物：QA 复测区／工程师施工试跑暂存／架构取证探针／演练预演区／装配对拍区，不分工序席位。
2. 唯一落点＝所属项目仓根 `.scratch/<票号>/`：跨仓对拍需多仓并排的，各落各自仓 `.scratch/` 内；禁盘根裸路径（磁盘根直接建目录）、禁系统 Temp 目录（宿主临时环境变量展开所得目录，含 Windows `AppData\Local\Temp` 与 Git Bash `/tmp`）、禁仓外任何自建点。
3. 收口登记票必含清理判据：本票声明闭集外的临时区批毕删除＋附删除读数；确需留存者归档至项目指定归档仓＋附留存归档读数。收口态＝零残留——工作仓 `git status` 净＋本票 `.scratch/<票号>/` 已清或已登记留存去向。消费面＝收口票判定段：主理人汇编收口票时列入该项，QA 席收口判定核对删除/留存读数（人工闸）。
4. 派工书／票面禁写仓外临时路径模板（旧措辞〔禁例引〕「置系统 Temp」「置仓外 Temp」作废）；席位受命含此类路径时有权指出违例并请改派落位。
```

- 口径注：§八条款文本＝决策者已裁四款逐字成文，席位卡行（S4）只载自指短声明不复写条文（handoff 卷 §十形式约束）。
- 验收＝A1＋A2＋A3。

## S2 SKILL.md 随动（`agent-experts/baigong-software-team/skills/software-orchestration/SKILL.md`）

1. frontmatter L5：`version: 1.1.4` → `version: 1.1.5`。
2. frontmatter description（L3）两处替换（同句其余零动）：
   - 「通用开发纪律（写权闭集·代码纯度·回执清单·QA 纯净）的按需加载索引」→「通用开发纪律（写权闭集·代码纯度·回执清单·QA 纯净·临时工作物落位清理）的按需加载索引」
   - 触发词尾部「席位实例唯一。」→「席位实例唯一、临时工作物、.scratch 落位、清理判据、零残留。」
3. 正文 references 索引表 dev-discipline 行（L24）内容列替换：
   - 旧：「通用开发纪律全节（写权闭集／代码纯度／工程师完工回执／QA 纯净职责·四闸一体／票面起草职权／检出条款消费面对账）」
   - 新：「通用开发纪律全节（写权闭集／代码纯度／工程师完工回执／QA 纯净职责·四闸一体／票面起草职权／检出条款消费面对账／临时工作物落位与清理纪律）」
   - 该行「何时必读」列零动。
- 验收＝A5。

## S3 sop 脚本 docstring 旧措辞改新落点措辞（四件·只动 docstring 一行，功能逻辑零动）

行号为 dd3e2cf 锚读，以整句命中为准，逐字替换：

1. `skills/sop/scripts/commit-audit.py` L17：
   - 旧：`运行落盘一律可重定向：--ledger 与 SWB_LEDGER_ROOT；验证运行请重定向至 Temp（仓内零运行残留）。`
   - 新：`运行落盘一律可重定向：--ledger 与 SWB_LEDGER_ROOT；验证运行请重定向至所属项目仓根 .scratch/<票号>/（批毕即删·仓内与仓外公共区零残留）。`
2. `skills/sop/scripts/decision-pack.py` L14：
   - 旧：`运行落盘一律可重定向：--ledger/--out 与 SWB_LEDGER_ROOT；验证运行请重定向至 Temp。`
   - 新：`运行落盘一律可重定向：--ledger/--out 与 SWB_LEDGER_ROOT；验证运行请重定向至所属项目仓根 .scratch/<票号>/（批毕即删）。`
3. `skills/sop/scripts/dispatch-builder.py` L19（docstring 内跨行句第二段）：
   - 旧：`验证运行请重定向至 Temp，不得在仓内留运行残留。`
   - 新：`验证运行请重定向至所属项目仓根 .scratch/<票号>/（批毕即删·不得留运行残留）。`
4. `skills/sop/scripts/write-guard.py` L23：
   - 旧：`验证运行请重定向至 Temp（仓内零运行残留）。`
   - 新：`验证运行请重定向至所属项目仓根 .scratch/<票号>/（批毕即删·仓内零运行残留）。`

- 开票侧核验：tests/ 对「重定向至 Temp」docstring 字面零在位断言（dd3e2cf 实测 grep 零命中）；四件仅 docstring 文案，键值/regex/退出码零动。
- 验收＝A2。

## S4 五席位卡守则节各补一行自指短声明（逐字）

插入位＝各卡「- 不允许同席多实例并发…」行之后（lead 卡 L75 后，其余四卡 L37/L37/L37/L38 后；行号锚 dd3e2cf）。运行时权限写域行永禁动（本行入席位守则节，不入权限四行节）。

lead 卡（`agents/software-team-lead.md`）逐字一行：

```
- 本席派工书与票面禁写仓外临时路径模板（盘根裸路径／系统 Temp／仓外自建点）；临时工作物唯一落点＝所属项目仓根 `.scratch/<票号>/`【席位守则·dev-discipline 卷】
```

其余四卡（product／architect／qa／engineer 各逐字同一行）：

```
- 临时工作物只落所属项目仓根 `.scratch/<票号>/`：受命文书含仓外临时路径模板时，本席有权指出违例并请改定落位，请求改派不构成违例【席位守则·dev-discipline 卷】
```

- 形式约束自检（handoff §十）：每卡单次增量 1 行（≤8 行）✓；每行 ≤1 行无续行✓；含「本席」自指串＋真源卷名「dev-discipline 卷」✓；与 §八条文最长连续重合＝「有权指出违例并请改」9 CJK＜12 阈值（开票侧预核，QA 复测）。
- 验收＝A4。

## S5 版本与版本账

1. 三同源 `0.1.24` → `0.1.25`（开票侧实测现值：`plugin.json` L3＝0.1.24／`.codebuddy-plugin/plugin.json` L3＝0.1.24／`bundle.lock` L5（bundle.version）＝0.1.24）：
   - `plugin.json`：`"version": "0.1.24",` → `"version": "0.1.25",`
   - `.codebuddy-plugin/plugin.json`：同行同改
   - `bundle.lock`：`"version": "0.1.24",` → `"version": "0.1.25",`（bundle 块内；components 组件行零动）
2. `README.md` 版本账块追加两行（插入位＝「- **版本账 v0.1.23**（…）」行之后、「## 头像」节前的空行前；append-only，不回改既有行）：

```
- **版本账 v0.1.24**（2026-11-05·CLN-PURE 装配净化批·补记）：publish.py 支持 bundle.lock 顶层 `assembly_exclude`（五类过程本体件裁出装配面）＋装配面存量非法指针全数自包含化＋EAC 组件 ref 换钉 `external-advisor-collab@v1.1.3`（组件版本 1.1.2→1.1.3）＋config/hooks/脚本注释面案号行号锚自包含化。三同源 0.1.23→0.1.24。补记：本行系 TMP-DISC 批发现上批漏登记版本账，据既有 commit 回补。
- **版本账 v0.1.25**（2026-11-05·TMP-DISC 临时工作物落位与清理纪律批）：决策者 2026-11-05 四款口径成文——`skills/software-orchestration/references/dev-discipline.md` 新增 §八（一切临时工作物唯一落点＝所属项目仓根 `.scratch` 区／收口登记票必含清理判据零残留／派工件禁仓外临时路径模板＋席位拒指权）；SKILL.md 索引＋触发词随动 1.1.4→1.1.5；sop 四脚本 docstring 旧 Temp 重定向措辞改仓根 `.scratch` 落点措辞；五席位卡守则节各补一行落位自指短声明。三同源 0.1.24→0.1.25（纪律①每变必 bump·三同源）。
```

- 验收＝A5＋A6。

## 禁动面

- 技能正文其余条款：`dev-discipline.md` §一~§七、software-orchestration 其余九卷、`skills/sop/` 其余件；
- 两基线副本（`skills/sop/references/product-v2.9-copy.md`／`architecture-v2.9-copy.md`）一字不碰；
- `tests/` 全部内容（含 probes 的 mktemp 重定向面，见候裁单列）；`deliverables/` 他面；
- 五席位卡运行时权限写域行（权限四行节）；席位卡除 S4 指定插入行外其余零动；
- 各脚本功能逻辑（S3 四行 docstring 之外零动）；`bundle.lock` components 组件行/ref tag/note 零动；
- `.collab/` 账本面（状态迁移必经脚本）；`.gitignore`。

## 验收判据（可机械·occurrence 口径 grep 钉值·全部附前后实测·F7）

- **A0 开工**：开端 HEAD 实测读数＋`git status --porcelain` 净读数登记；施工前跑基线：`bash agent-skills/object-audit/scripts/run-gates.sh`＝GATE PASS exit 0（读数存档）＋`python agent-skills/object-audit/scripts/check-pointer-closure.py` 缺省两包面前置 WATCH 计数读数；
- **A1 新节在位**：`grep -c "^## 八 临时工作物落位与清理纪律" <dev-discipline>`＝**1**；四条款锚句各＝1：`grep -c "适用范围＝一切临时工作物"`／`grep -c "唯一落点＝所属项目仓根"`／`grep -c "收口登记票必含清理判据"`／`grep -c "禁写仓外临时路径模板"` 各＝**1**（dev-discipline 单件面）；
- **A2 旧措辞清零**：扫描面＝§口径1；主式四 pattern（§口径2）`grep -rn` 施工后命中＝**0**——豁免规则＝**含〔禁例引〕标记的行不计**（预登记必命中行：dev-discipline §八条款4 一行含「置系统 Temp」「置仓外 Temp」两处禁例引＝逐笔登记 EXEMPT 不入违例计数）（施工前基线＝4，前后各附读数）；宽式 `grep -rn "Temp"` 扫描面命中逐笔判因：白名单＝S1 §八条款2括号内示例列举＋条款4〔禁例引〕句＋lead 卡新行禁指措辞（「系统 Temp」作为禁项列举）＋README 版本账 v0.1.25 行 Temp 字样叙述＋S3 四脚本新 docstring 无 Temp（应零命中此列）；非白名单命中＝违例回扫 S3；
- **A3 禁例引标记核验**：`grep -c "〔禁例引〕" <dev-discipline>`＝**1**（§八条款4一处·交付面无其他裸旧措辞引用）；
- **A4 席位卡行在位**：`grep -c "席位守则·dev-discipline 卷" agents/software-team-lead.md`＝**1**；product／architect／qa／engineer 四卡各＝**1**（施工前五卡该串命中＝0，前后各附读数）；五卡单次 diff 增量各＝1 行（`git show --stat` 行数读数）；
- **A5 版本随动**：`grep '"version"' plugin.json .codebuddy-plugin/plugin.json`＋`grep '"version"' bundle.lock` 三同源读值＝`0.1.25`（前后各附实测·F7）；`grep "^version:" skills/software-orchestration/SKILL.md`＝`1.1.5`（前值 1.1.4 同附）；
- **A6 版本账登记**：`grep -c "版本账 v0.1.24" README.md`＝**1**＋`grep -c "版本账 v0.1.25" README.md`＝**1**（README 版本账既往无 v0.1.24 行＝开票侧实测缺口读数，本票 S5 补记行填补；前后读数各附）；
- **A7 门禁零回归**：施工后重跑 A0 两件——`run-gates.sh` GATE PASS exit 0（前后对拍：基线发现数不新增·附前后读数）；`check-pointer-closure.py` 缺省两包面 WATCH 计数不新增（新句指针均在反引号段内＝SUBSTR 范式；若新增逐笔归因上报）。四脚本 `python -m py_compile` 全过＋既有 tests/s2·s3·s4 全绿（`pytest agent-experts/baigong-software-team/tests/` 前后对拍）。

## 自检与回执（N4 附载体）

- 开工登记：开端 HEAD 实测读数＋A0 基线读数；
- 声明闭集 15 件＝改动闭集上限——闭集外零触碰；逐条 S1-S5 完成后自跑对应判据，全部收齐后跑 A1-A7 全量；
- 禁列过程痕迹自检 grep 用 F11 终式 `见?第\s*\d+\s*轮|轮次戳|〔[^〕]*·轮〕|轮次号[：:]`，命中按三分账登记；
- 回执落 `.collab/receipts/2026-11-05-TMP-DISC-工程师回执-v1.md`，单独 commit（前缀 `collab:`）；回执含全部写入文件清单（反引号包裹路径·与交付 commit name-only 全等）＋A1-A7 逐判据实测载体＋A2 宽式全命中逐笔判因＋五卡 diff 行数读数；
- 本票收口自带清理判据示范：施工完毕时本票 `.scratch/` 内除 `.scratch/tickets/` 本票面外零新增临时物；`git status --porcelain` 收口净读数附回执；
- 禁 `--no-verify`／禁 amend／禁 push 装配产物（纪律④产物不入库）。

## 候裁单列

1. **tests/ 面旧措辞措辞随动与否**：`tests/probes/*.sh`（11 件）与 s2/s3/s4 测试用 `mktemp -d` 与系统 Temp 作证据目录／落盘重定向（共 12 文件命中 Temp 族），与 §八「禁系统 Temp」字面冲突。架构席起草判断＝**不随动**（理由：tests/ 经 `assembly_exclude` 已裁出装配面＝仓内验收件非交付面条款面；测试进程内 tempfile 由运行器自清理，与「人工席堆临时目录不收口」不同对象；改 tests/ 触及禁动量大且无交付面效力）——按 §口径1 扫描面排除不入违例。若决策者认为测试面也应示范新落点（probes EVID_DIR 改 `.scratch/<票号>/`），另立微票，本票不含。此为落点射程解释项＝候裁，两案均已成文可拍。

## 红线

- 只动声明闭集 15 件：闭集外零触碰；
- 禁动面全节逐条生效；两基线副本一字不碰；
- §八四条款文本＝决策者已裁口径逐字成文，工程师/QA 不得改写措辞；定稿句有异议＝停手上报，不得现场裁量（口径四款本身不列候裁）；
- 落点二选一裁量已在 S1-S5 闭合为唯一方案（dev-discipline 增节＋最小随动面），无其他落点候裁；
- append-only：不改本票既有行；实测与票面预期冲突按实测登记上报（H6）。