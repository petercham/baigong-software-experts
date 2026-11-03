# SWB-B4 · 迁移施工票：门禁/权限机件票目录与新树锚定随动（check-ticket-reconcile 改造＋write-guard/lease 两级锚＋R⑧⑨精化追认）（施工票·L2·架构席起草）

- 起草实测 HEAD：`d584d7b`（B3 票面笔）；开工 ANCHOR＝B3 收口笔之后可达后继（票目录已在新位＝本票缺省改造前提）。
- 施工基线真源＝方案 v3 §五 B4 行＋收口登记 `ed5d3c0` §三（R①②③⑤⑥⑧⑨ 路由）＋B0 登记 B 批判据四目②。
- **开工附注三项（B0 登记照录）**：①誊写禁令 `f5a0d96`（本票＝原位代码文本随动批非搬家批·照注自察）；②票面落位 `.scratch/tickets`；③era 跨仓口径（不在本票＝ESC1）。
- 计数口径＝occurrence；判据自带落盘；负例 exit≠0。行号锚 HEAD=`d584d7b`（现盘旧位实测·开工若位移以逐字文本锚定位）。

## 声明闭集（16 件展开口径·目录级简写申报·本批唯一可写面）
- 声明闭集：
- agent-skills/object-audit/scripts/check-ticket-reconcile.py
- agent-skills/object-audit/scripts/check-collab-lint.py
- agent-skills/object-audit/scripts/run-gates.sh
- agent-experts/baigong-software-team/skills/sop/scripts/write-guard.py
- agent-experts/baigong-software-team/skills/sop/scripts/lease-issuer.py
- agent-experts/baigong-software-team/config/seat-permissions.json
- agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json
- agent-skills/multi-collab/SKILL.md
- agent-skills/object-audit/SKILL.md
- agent-skills/object-build/SKILL.md
- agent-skills/bundle-assembly-registration/SKILL.md
- agent-experts/baigong-software-team/bundle.lock／bundle 版本三同源＋README append（见 B4-F）

（注：末两行展开＝bundle.lock＋plugin.json＋.codebuddy-plugin/plugin.json＋README 四件；回执 name-only 全等口径＝16 件展开名录：所列 11 行＋版本三同源＋README＋run-gates／check-collab-lint 已含行内＝回执首节固定展开表。）

## 逐条施工规格

### B4-A check-ticket-reconcile 缺省票目录改造（B 批判据四目②）
现盘 `default_tickets(root)`（L315–317）＝`root/.collab/tickets` 单目录。改：
1. 缺省票目录枚举＝**按项目双候选**：对仓根下 `{agent-experts,agent-skills,softwares}/<project>/` 各项目取 `<project>/.scratch/tickets/`；无则跳过（不再回落 `.collab/tickets`——旧域 B3b 已灭）。
2. **扫描面非空正断言（防假绿·T09 输入件 G5 危险形态款）**：枚举结果为空列表时 → `sys.stderr.write("infra error: 票目录枚举为空（门禁哑火形态）\n"); raise SystemExit(4)`。判据见验收 1。
3. `--ticket` 显式入口语义零动；`COLLAB_PREFIX` 交付面排除逻辑随新树：票目录前缀判定改 `.scratch/tickets/` 语义（票面声明路径比对域不变）。
4. spec_file 头块内 `.collab/tickets/2026-10-30-EAC-SK5-机检票.md` 三处（check-collab-lint L5/L14/L23）→ 改指 B3 新位 `agent-skills/external-advisor-collab/.scratch/tickets/2026-10-30-EAC-SK5-机检票.md`（Y-7 闭环化换锚对位；clause_sha256 不动——锚＝条款文本非路径）。

### B4-B write-guard / lease-issuer 路径锚两级化（v3 §五 B4「两级化」款）
1. `write-guard.py` `repo_root()`（L48–49 注释「上溯六级＝仓根」）**换代＝项目根锚**：项目根＝自脚本位置上溯首个含 `docs/STRUCTURE.md` 的目录；仓根（`.git` 所在）仅用于交付 listing 与 git 子命令。权限字面读作**项目根相对**（表2-1 路径锚定款语义随迁：`seat-permissions-hooks-map.json` L7「路径锚定」注记同步改「项目根字面」）。
2. `lease-issuer.py` L33 账本根缺省 `cwd/.collab/ledger` → `<项目根>/.collab/ledger`（项目根解析同款 helper；`SWB_LEDGER_ROOT` 覆写语义零动）。
3. 六演练＋s2/s4 回归全绿为验收硬线（验收 3）。

### B4-C R⑧ 精化落地（先决闭集＝B1 规范件 `collab-fixed-structure.md`）
seat-permissions 两 config：engineer 行 deny `.collab/**`（json L52／hooks-map L28）**精化＝显式枚举减授权**——deny 改枚举 `.collab/ledger/**` 等租约外桶？＝**否（精化方向按收口定案）**：保留 `.collab/**` 为基线 deny＋**增补与三 host 租约行对表的豁免注记行**（R⑧ 过渡态(III)＝签发可写拦显性化冲突在册消账）＝按 (i) 向：三席 host 写行 `.collab/ledger/` 等与 deny `.collab/**` 的冲突面，精化＝deny 枚举逐桶列名但**除** B1-D 规范闭集中 host 租约授权桶（回执附桶×席 10×9 矩阵逐格读数）。语义红线＝`.collab` 固定结构桶名以 B1-D 规范件为唯一真源（grep 引用不复写名录）。

### B4-D R⑨ 设计真源追认改笔（V13 再锚议程·append-only）
现行登记件（B3 后暂住 `agent-experts/baigong-software-team/.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md`）表2-1 行与「受保护区」词条 vs 裁定一唯二排除偏差：**不改正文**——文末追加追认注记一行（含日期戳＋裁定一指针＋「表2-1 语义按裁定一唯二排除追认」句）＋V13 恒等式保护声明（尾追加不扰动 L1–260 行号；追加行不入 V13 段·回执重算三哈希不变断言＝验收 5）。

### B4-E engineer 枚举行按 D1 名录填充（T08R write_globs_note「D1 未裁不建行」尾账）
seat-permissions engineer 行补项目根相对机械行：`"agents/**","skills/**","config/**","hooks/**","tests/**","avatars/**"`（百工 bundle 面＝STRUCTURE.md delivery_paths 同源——**机检对账＝与 STRUCTURE YAML 逐行相等断言**验收 6）；`.collab`/`docs` 唯二排除保持 deny（现面已在）。hooks-map 同源行随动。

### B4-F 版本账随动（纪律①）
三同源 bump 0.1.17→0.1.18＋README append-only 追加一行（B4 内容＝门禁权限机件新树两级锚随动）。

## 验收判据（全部机械可判·自带落盘·负例 exit≠0）
1. **缺省票目录非空正断言**：`python agent-skills/object-audit/scripts/check-ticket-reconcile.py --root . > $B4_TMP/c1.out 2>&1` → exit 0（新树票在架）；负例构造（仓外 Temp 复制仓骨架无票目录）exit 4。
2. **票对账命中正读数**：c1.out 内「票 N」N≥当前在架票数（回执登记读数）；旧 `.collab/tickets` 回落路径 grep 源件 occurrence＝0。
3. **回归全绿**：六演练 SIX_DRILLS_GREEN＝1；s2/s4 exit 0；run-gates GATE PASS 对开工基线零新增族；write-guard/lease 探针＝B4-A/B 改造后 `--path-glob "agents/**"`（项目根相对）exit 0、`"docs/PRODUCT.md"` exit 2（对位 T08R 判据形态迁移）。
4. **spec 锚存在性**：全部 `spec_file:` 头块路径逐条 `test -f` 全存在（python 抽取→exit 0）；`.collab/tickets/` 旧式锚 occurrence＝0。
5. **V13 三哈希不变**：登记件全文/产品段/架构段三哈希复算＝`3f335333…/7214ad14…/efb4f765…` 逐字等（追记仅尾追加；`wc -l` 增长值＝追加行数入回执）。
6. **STRUCTURE↔engineer 行相等断言**：python 抽 STRUCTURE.md delivery_paths 与 seat-permissions engineer 机械行集比对＝全等 exit 0。
7. **R⑧ 矩阵读数**：deny 枚举×host 写行 10 桶×相关席矩阵落盘 c7.out：授权桶∩deny＝∅（逐格读数）。

## 禁动面
交付内容语义面（席位卡声明文本行、SOP 正文、60-gates 路由表——路由表加挂 `--scope docs/adr` 属门禁路由裁量＝另票）；登记件正文（仅尾追加）；`docs/STRUCTURE.md`（B1 成品·本票只读源）；`.collab/`（旧仓根残留 era 面）；`tools/` 其余。

## 候裁点
无（R⑧⑨路径既裁＝本票执行；路由加挂不在本票＝另票另裁）。

## 票间关系
前置＝B2（新树路径在位）＋B3（票目录在位）＋R⑧过渡态在册（`ed5d3c0`）。后置＝B5（README/gitignore 终写引用本票落定态）。

## 回执
落 `agent-experts/baigong-software-team/.collab/receipts/2026-11-03-SWB-B4-receipt.md`：开端 HEAD＋name-only 全等＋判据 1–7 读数＋R⑧ 矩阵表＋V13 哈希三值。交付笔单独 commit；禁 `--no-verify`、禁 amend。
