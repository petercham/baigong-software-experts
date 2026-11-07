# TK-SEMGOV-T1-BUILD · 施工授权票：技能包七件落地（v5 票面逐字节还原）

- 票 ID＝`TK-SEMGOV-T1-BUILD`。票型＝施工授权票（非设计票、非分票、非部署票）。
- 开票席＝主理人；落笔时点 2026-11-07 20:01:11 +0800；落笔前实测 HEAD＝`503ecca`；tracked 面净。
- 批准载体＝`D:\multi-agent-collab-devkits\.collab\decisions\2026-11-07-呈皮总简报-SEMGOV-T1放行施工.md`（`503ecca`）＋皮总原话「批准施工」；授权口径登记＝`D:\multi-agent-collab-devkits\.collab\decisions\2026-11-07-主理人登记-皮总批准SEMGOV-T1放行施工与施工授权口径.md`。
- **规格唯一真源**＝`D:\multi-agent-collab-devkits\.scratch\tickets\2026-11-07-SEMGOV-T1-技能包与契约票-v5.md`（commit `6db881a`，3458 行／294,858 字节／sha256 `dab8179516a84cfa7eba23efea735e456e2e629bce11d9768c3a616f62411ec5`）。本票**不复制、不改写、不重新解释任何契约条款**；施工动作＝把该票 §2.1–§2.7 的围栏内容逐字节还原为真实文件。
- 本票不含条款正文；工程师读规格时以 `6db881a` 的 blob 为准，不以工作区快照为准（`git show 6db881a:<票面>` 抽取）。

## 〇、开工前置（不符即停手上报，不自行纠偏）

1. 开工第一步实跑 `git rev-parse --short HEAD` 与 `git status --porcelain --untracked-files=no`，两读数写入回执开端；HEAD 应 ≥ `503ecca`（并发线可能已前移，如实登记差值，不 rebase、不等待）。
2. 实跑 `git cat-file -e 6db881a^{commit}` 与票面 sha256 复算，确认规格真源在位且逐字节全等。
3. 复核 `agent-skills/claim-commitment-governance/` **不存在**（本票施工前应为零施工件）；若已存在任何文件＝停手上报，不得就地覆盖。

## 一、写集闭集（超集即停手上报）

### W1 · 技能包七件（交付面·逐字节还原）

| # | 目标绝对路径前缀＝`D:\multi-agent-collab-devkits\agent-skills\claim-commitment-governance\` | 规格来源（v5 票面围栏行号） | 内容行数 |
|---|---|---|---|
| 1 | `SKILL.md` | §2.1 围栏 447–540 | 92 |
| 2 | `references\10-contract.md` | §2.2 围栏 544–762 | 217 |
| 3 | `references\20-artifact-mapping.md` | §2.3 围栏 766–817 | 50 |
| 4 | `references\30-gates.md` | §2.4 围栏 821–920 | 98 |
| 5 | `references\40-provenance-map.md` | §2.5 围栏 924–968 | 43 |
| 6 | `templates\claim-register.md` | §2.6 围栏 972–1017 | 44 |
| 7 | `templates\outbound-artifact.md` | §2.7 围栏 1021–1055 | 33 |

七件内容行数合计 **577**，与票面 §2.0b 自报一致。围栏开闭行本身不计入文件；文件末尾以围栏内最后一行为准，**禁自行补尾空行、禁改换行符、禁改 BOM、禁改编码**（一律 UTF-8 无 BOM，LF/CRLF 以围栏原样为准，逐字节比对判定）。

### W2 · 验收夹具（过程域·随票交付但不入技能包）

- `D:\multi-agent-collab-devkits\.scratch\tickets\2026-11-07-SEMGOV-T1-BUILD-verify.py` ← v5 票面 §3.0 `python` 围栏 1067–3165（内容 2097 行），逐字节还原。
- **依据**：票面 §2.0 行 410「`verify.py` 为验收夹具，随票交付但不入技能包」；会师裁定十九逐字重申。放行路径中「七件＋夹具落到包目录」系面向决策者的通俗合称，不作逐字落位规格（见授权口径登记件裁定 A）。
- **禁止**：不得把该文件（或其副本、符号链接、改名件）写入 `agent-skills/claim-commitment-governance/`。

### W3 · 工程师回执

- `D:\multi-agent-collab-devkits\.scratch\tickets\2026-11-07-SEMGOV-T1-BUILD-回执-v1.md`，单独一笔 commit。
- 与 v5 票回执同族落点；门禁 `check-ticket-reconcile.py` 的 `.collab/` 前缀假设会再报一条 WATCH，**已在册、advisory、不阻断**（归 T6），不得为规避它改落点或改门禁。

### 写集之外零写

除 W1 七件、W2 一件、W3 一件外，工程师本票**不得写入任何文件**（含临时脚本落仓内、缓存、日志、`.gitignore`、`settings.json`）。临时抽取／复跑一律在仓外临时目录（`mktemp -d`）进行，批毕清理，读数入回执。

## 二、禁动面

- `D:\multi-agent-collab-devkits\.scratch\tickets\2026-11-07-SEMGOV-T1-技能包与契约票-v1.md` ～ `-v5.md`（五版票面）、`…-v4-receipt.md`、`…-v5-receipt.md`：**一字不动**。
- `.collab\decisions\**、`.collab\qa\**`、`agent-experts\baigong-software-team\.collab\**`：零写（登记件由主理人落笔）。
- `agent-skills\fuxi-skill\**` 及一切他案在制品、`docs\**`、`.archive\**`、`audits\**`、`tools\**`、`agent-skills\object-audit\**`：零写、零改、零删。
- 三同源版本面 `plugin.json`／`bundle.lock`／`.codebuddy-plugin\plugin.json`、`config\**`、`tests\**`：本票零触（版本升号与组件挂载属合并批与 T3，另票）。
- 禁 `git add -A`、禁 `--amend`、禁 `reset`、禁 `--no-verify`、禁强推、禁改他人 commit。

## 三、验收判据（全部机械可跑·读数逐条入回执）

| # | 判据 | 命令口径 | 钉值 |
|---|---|---|---|
| 1 | 七件逐字节全等 | 自 `git show 6db881a:<票面>` 抽 §2.1–§2.7 围栏内容 → 与目标文件逐件 `cmp`／sha256 比对 | 七件全等，diff 0 |
| 2 | 目录闭集 | `find agent-skills/claim-commitment-governance -type f` 排序后与 W1 七件路径比对 | **恰 7 件**，零多余、零缺失 |
| 3 | 夹具逐字节全等 | 自 `6db881a` 抽 §3.0 围栏 → 与 W2 文件比对；并与票面 §0.7 自证读数（`25fc83b4…508d`／135,600 字节）核对 | 全等 |
| 4 | 夹具不入包 | `find agent-skills/claim-commitment-governance -type f` 中零 `.py` 文件 | 0 命中 |
| 5 | 过程域名零命中（裁定十九兜底） | 对七件＋夹具全文 `grep -nE 'anti[0-9]*\.py|build\.py|anchor_check\.py|all[0-9]*\.txt|self[0-9]*\.txt|mut[0-9]*\.txt|stats[0-9]*\.txt|tpl_v[0-9]*\.md'` | **0 命中**（含 `anti5.py` 及同族） |
| 6 | 读数说明段零复制 | 七件＋夹具全文检索 `## 0.7`、`本票围栏自测读数`、`反证与正向实测` 等 §0.x 专属标题串 | 0 命中 |
| 7 | 夹具四类读数（对真文件跑） | `verify.py --all / --mutate / --selfcheck / --stats`，PKG 指向真实包目录 | `--all` 28/28；`--mutate` 241 咬住／0 假通过／0 MUTATE_FAILED／覆盖 28/28；`--selfcheck` 锚唯一 59/59＋双斜杠转义 0；`--stats` 111 行（分布和 28、分组和 226） |
| 8 | 三闸真包实跑 | `check-skill-meta.py --root .`、`check-provenance.py --root . --target agent-skills/claim-commitment-governance/SKILL.md`、`check-entity.py --root .` | 三闸 exit 0、零 BLOCK；`provider` 可解析（v5 出票态因包不存在未能解析，本票**必须补齐这组真读数**） |
| 9 | 写集对账 | `git show --name-only --format="" <施工笔>` 与 W1＋W2＋W3 声明闭集排序比对 | 全等；回执笔单件恰 1 件 |
| 10 | 真源未被触碰 | `git diff 503ecca..<收口HEAD> -- .scratch/tickets/2026-11-07-SEMGOV-T1-技能包与契约票-v5.md .scratch/tickets/2026-11-07-SEMGOV-T1-v5-receipt.md` | 空输出 |
| 11 | 收口洁净 | `git status --porcelain --untracked-files=no` | 空 |

判据 7／8 的读数须为**本票真文件上重跑所得**，禁照抄票面 §0.7 或回执的历史读数；若与钉值不符＝如实登记实际读数并停手上报，**禁改夹具、禁改七件正文以求绿**。

## 四、提交与回执形态

1. 施工笔：`git add` 仅 W1 七件＋W2 一件（可用显式逐路径列出，禁 `-A`），单笔 `collab:` 前缀 commit；回执笔另起一笔，只 `git add` W3 一件。
2. 两笔提交**各自落账后才算收束**（做了没落盘／落盘没提交／提交没对账，三态逐条写，不合并成「已完成」）。
3. 回执必含：①开工 HEAD 实测读数；②提交前复测 HEAD；③提交时点 HEAD；④两笔 commit sha；⑤判据 1–11 逐条实测读数（含命令与输出要点）；⑥**完整写入／修改文件清单**（对账口径＝`git show --name-only` 与清单全等）；⑦仓外临时目录清理读数；⑧`git status` 净读数。
4. 回执中禁出现「过程域零指针」一类全称断言；涉及零命中的表述须写清**检索范围、命令与实测读数**（本批 R5-01 教训）。

## 五、收口即停

本票射程仅到「七件＋夹具落成真文件并回执落账」。**不得**自行进入真文件审、真实 PRD 试填、改契约、升号、装配、部署或任何发布动作。收口后回报主理人，由主理人派 QA＋产品席对真文件审（放行路径第 3 步）。

## 六、异常停止条件（任一命中即停手上报）

- 规格真源 `6db881a` 不可解析或 sha256 不等；
- 开工时包目录已存在任何文件；
- 任一验收判据与钉值不符；
- 并发线在写集内产生改动（如实登记区间读数，不自行合并）；
- 需要写入写集闭集之外的任何文件。
