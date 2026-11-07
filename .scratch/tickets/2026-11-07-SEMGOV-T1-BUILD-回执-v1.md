# TK-SEMGOV-T1-BUILD · 工程师回执（v1）

- 票 ID：`TK-SEMGOV-T1-BUILD`；票型＝施工授权票（非设计票、非分票、非部署票）。
- 回执席：工程师席（`eng-semgov-build1`）；工作仓 `D:\multi-agent-collab-devkits`，分支 `main`。
- 施工规格唯一真源：`6db881a` 的 v5 票面 blob（`.scratch/tickets/2026-11-07-SEMGOV-T1-技能包与契约票-v5.md`）。
- 施工授权票：`b9169c6`（落笔前读数 `503ecca`）；授权口径登记：`86d9963`。
- 施工动作＝把 v5 票面 §2.1–§2.7 围栏逐字节还原为 W1 七件、§3.0 围栏逐字节还原为 W2 夹具；不含契约改动、升号、装配、部署。收口即停。
- 本回执按体例落盘 md，聊天消息只作导读。

---

## 〇、开工前置读数（开工第一步实跑，写入回执开端）

| 项 | 实测命令 | 实测读数 |
|---|---|---|
| **① 开工 HEAD** | `git rev-parse --short HEAD` | **`b9169c6`** |
| 开工 HEAD 全值 | `git rev-parse HEAD` | `b9169c6492d81600d35c8a4dc1803921b35a6c1f` |
| 开工分支 | `git rev-parse --abbrev-ref HEAD` | `main` |
| 开工 tracked 面 | `git status --porcelain --untracked-files=no` | **空**（tracked 面净） |
| 规格真源 commit 在位 | `git cat-file -e '6db881a^{commit}'` | `EXIT=0`；`git cat-file -t 6db881a` → `commit` |
| v5 票面 blob 字节 | `git cat-file -s "6db881a:<票面>"` | `294858` |
| v5 票面 blob 行数 | `git cat-file blob … \| wc -l` | `3458` |
| v5 票面 blob sha256 | `git cat-file blob … \| sha256sum` | `dab8179516a84cfa7eba23efea735e456e2e629bce11d9768c3a616f62411ec5` |
| 工作区票面对照 | `sha256sum <工作区票面>` | 同上值，294858 字节／3458 行；blob 与工作区逐字节全等 |
| blob 换行/BOM | python 二进制读 | `CR=0`（纯 LF）、`BOM=b'# S'`（无 BOM）、`NL=3458` |
| 目标目录不存在性 | `[ -e agent-skills/claim-commitment-governance ]` | `ABSENT`（零施工件，可建） |
| W2/W3 不存在性 | `[ -e …-BUILD-verify.py ]`／`[ -e …-BUILD-回执-v1.md ]` | 均 `ABSENT` |
| 三件必读 | 施工授权票／v5 真源／授权口径登记 | 全部完整绝对路径读入；真源规格按围栏行号分段核读 |

**并发线差值如实登记**：主理人派工书所记「落笔前读数＝`b9169c6`（tracked 面净）」与我开工实测 `b9169c6` **一致、无差值**；施工票本文所记落笔前读数 `503ecca`（19:41:57）为更早时点，我实测 `b9169c6`，其间并发线前移（见判据 10 基线核实：`6db881a`→`503ecca`→`b9169c6`）。按派工书「不 rebase、不等待、不合并他案改动」执行，未据此改口径。

---

## 一、写集闭集与逐字节还原读数

一律以 `git cat-file blob 6db881a:<票面>` 的**字节**为准；仓外临时目录内 python 以二进制切片（不设 newline、不设 encoding）写出；抽取脚本以 heredoc 内联运行，仓内零临时脚本／中间文件。围栏边界经 `grep -nE '^(```|~~~)'` 实测定位，与票面行号逐一吻合：

| 件 | 开行 | 闭行 | 内容行 | 行数 | 字节 | sha256 |
|---|---|---|---|---|---|---|
| `SKILL.md` | 447 | 540 | 448–539 | 92 | 7331 | `82cec4c6a99239d6e088cebb3daba6aa4eed643f89ce2623737919e940b674db` |
| `references/10-contract.md` | 544 | 762 | 545–761 | 217 | 21922 | `e1e29886002accaea6a0858a3606941a32f66a7f15a8fc3186e4c701ec758867` |
| `references/20-artifact-mapping.md` | 766 | 817 | 767–816 | 50 | 5841 | `601dfdeb28ea967dac39f1900b3203d5a14645132621e5de32e6d64de3e0370c` |
| `references/30-gates.md` | 821 | 920 | 822–919 | 98 | 16799 | `0a876711aad95a082cca200352aa26b7536e6e093ad18c9509af78933c20a230` |
| `references/40-provenance-map.md` | 924 | 968 | 925–967 | 43 | 7474 | `0ad8df1b5cc6339c8c7952cd3516917a2d4fe9b973999f6f900c2953d60ffb5d` |
| `templates/claim-register.md` | 972 | 1017 | 973–1016 | 44 | 4050 | `b99a9e1b06dcbeeca30595a4927d2ddc9c7ecd983c774326964a7cb747b674f5` |
| `templates/outbound-artifact.md` | 1021 | 1055 | 1022–1054 | 33 | 1674 | `ad97cc111e2592b56d2a6beab214bfcd9ef9d3862343337680d5cbd90e3aeecf` |
| **W1 合计** | | | | **577** | | 与票面 §2.0b 自报 577 一致 |
| `verify.py`（W2 夹具） | 1067(```python) | 3165 | 1068–3164 | 2097 | 135600 | `25fc83b451c12522f58872abbc37d1a39038b5646dc01ebfa12d835444ef508d` |

禁补尾空行、禁改换行符、禁改 BOM、禁重排、禁顺手格式化、禁「修正」票面任何字，均遵守：写出字节＝围栏开行之后、闭行之前的原始字节（LF、无 BOM）。

**写集闭集声明（9 件，全部新增、零修改）**：
1. `agent-skills/claim-commitment-governance/SKILL.md`
2. `agent-skills/claim-commitment-governance/references/10-contract.md`
3. `agent-skills/claim-commitment-governance/references/20-artifact-mapping.md`
4. `agent-skills/claim-commitment-governance/references/30-gates.md`
5. `agent-skills/claim-commitment-governance/references/40-provenance-map.md`
6. `agent-skills/claim-commitment-governance/templates/claim-register.md`
7. `agent-skills/claim-commitment-governance/templates/outbound-artifact.md`
8. `.scratch/tickets/2026-11-07-SEMGOV-T1-BUILD-verify.py`（W2，过程域，不入技能包）
9. `.scratch/tickets/2026-11-07-SEMGOV-T1-BUILD-回执-v1.md`（W3，本件，回执笔单件）

写集之外零写；禁动面（v1–v5 五版票面、v4/v5 回执、`.collab/decisions/**`、`.collab/qa/**`、`agent-experts/**/.collab/**`、`agent-skills/fuxi-skill/**`、`docs/**`、`.archive/**`、`audits/**`、`tools/**`、`agent-skills/object-audit/**`、三同源版本面、`config/**`、`tests/**`）零写、零改、零删。

---

## 二、判据 1–11 逐条实测读数（本票真文件上实跑）

> 判据 7／8 读数均为本票落成的**真文件上重跑**所得，非照抄票面 §0.7 或 v5 回执历史读数。判据 9/10/11 含「收口态」的读数在时间上晚于回执笔提交，按体例在本节登记「施工笔时点实测」＋由完工回报补「收口态复核」，不编造。

**判据 1 · 七件逐字节全等**：仓外临时目录**独立二次抽取**（重新 `git cat-file blob` → 重新按行切 8 段）写入 expected/，与真文件逐件比对。python `bytes==` 逐件结果：`ALL_EIGHT_BYTE_IDENTICAL=True`（8 件全部 `cmp=EQ`、sha256 双侧一致、bytes 与 lines 双侧一致）；追加 shell `cmp -s` 逐件复核 → 8 行 `cmp … EQ`、`ALL_CMP_EQ`；diff 0。

**判据 2 · 目录闭集**：`find agent-skills/claim-commitment-governance -type f | sort` → 7 行、`COUNT=7`；与 W1 七件声明闭集排序 `diff -u` → `DIFF_0_DECLARED_EQ_ACTUAL`（零多余、零缺失）。

**判据 3 · 夹具逐字节全等＋§0.7 钉值**：独立二次抽取的 §3.0 围栏与 W2 `verify.py` `cmp=EQ`、sha256 双侧一致（`bytes=135600 lines=2097`）。钉值实算：`W2_DINGZHI: prefix=25fc83b4 match=True suffix=508d match=True bytes=135600 bytes_135600=True` —— 与票面 §0.7 自证读数 `25fc83b4…508d`／135,600 字节全等。

**判据 4 · 夹具不入包**：`find agent-skills/claim-commitment-governance -type f -name '*.py' | wc -l` → `PY_COUNT_IN_PKG=0`。

**判据 5 · 过程域名零命中**：检索范围＝**七件＋夹具共 8 个文件全文**；命令＝`grep -nE 'anti[0-9]*\.py|build\.py|anchor_check\.py|all[0-9]*\.txt|self[0-9]*\.txt|mut[0-9]*\.txt|stats[0-9]*\.txt|tpl_v[0-9]*\.md' <8 文件>`；实测 `GREP5_EXIT=1`、`GREP5_HITCOUNT=0`（含 `anti5.py` 及同族）。此为零命中的**范围/命令/读数**登记，非全称断言。

**判据 6 · 读数说明段零复制**：检索范围＝**同一 8 文件全文**；命令＝`grep -nE '## 0\.7|本票围栏自测读数|反证与正向实测' <8 文件>`；实测 `GREP6_EXIT=1`、`GREP6_HITCOUNT=0`。同为范围/命令/读数登记。

**判据 7 · 夹具四类读数（真包重跑）**：`PKG=agent-skills/claim-commitment-governance`（绝对路径 `/d/multi-agent-collab-devkits/agent-skills/claim-commitment-governance`），`V=.scratch/tickets/2026-11-07-SEMGOV-T1-BUILD-verify.py`：
- `python3 "$V" --all "$PKG"` → `ALL_EXIT=0`、`OK_LINES=28`、`FAIL_LINES=0`（首 `OK c01`、末 `OK c28`）；**28/28**。
- `python3 "$V" --mutate "$PKG"` → `MUTATE_EXIT=0`、`BITE_LINES=241`；末段「变异体合计 241 条（结构面 15 ＋ 内容面 226）／咬住 241 条 / 假通过 0 条 / MUTATE_FAILED 0 条／逐判据覆盖 c01=1/1 … c28=1/1／判定：全绿（241 条全咬、零假通过、零失败、覆盖 28/28）」；**241 咬住／0 假通过／0 MUTATE_FAILED／覆盖 28/28**。
- `python3 "$V" --selfcheck "$PKG"` → `SELFCHECK_EXIT=0`；「靶点 59 个，锚唯一命中 59 个，不合格 0 个」「双斜杠转义命中 0 处」「判定：自证全绿」；**锚唯一 59/59＋双斜杠转义 0**。
- `python3 "$V" --stats "$PKG"` → `STATS_EXIT=0`、`STATS_LINES=111`；「合计 28 条；分布之和 28 == 检查数 28 ：是」「分组之和 226 == 内容面 226 ：是」「七件行数：92/217/50/98/43/44/33，合计 577 行」；**111 行、分布和 28、分组和 226**。
- 先读夹具源码确认 `--mutate` 全程在 `tempfile.mkdtemp` 副本上 `copytree` 后写入、`rmtree` 清理（`run_mutations` 行 1742 起），真包只读，未被污染。

**判据 8 · 三闸真包实跑（v5 出票期未重跑，本票补齐真读数）**：
- `python3 agent-skills/object-audit/scripts/check-skill-meta.py --root .` → `META_EXIT=0`、`META_BLOCK_COUNT=0`（输出 1 行 `coverage: OA-S2「不含项目名」子判据未执行`）。
- `python3 agent-skills/object-audit/scripts/check-provenance.py --root . --target agent-skills/claim-commitment-governance/SKILL.md` → `PROV_EXIT=0`、`PROV_BLOCK_COUNT=0`（空输出 0 行，符合 §0.8 预期）。
- `python3 agent-skills/object-audit/scripts/check-entity.py --root .` → `ENTITY_EXIT=0`、`ENTITY_BLOCK_COUNT=0`（输出 6 行：4 个 pattern count=0 ＋ 2 行 coverage）。
- **provider 可解析（显式坐实，非空输出即跳过）**：仓外临时 python 直接 import 闸脚本函数复算 → `PROVIDERS_COUNT=8`、`PROVIDER_IN_SET claim-commitment-governance=True`、`SKILL_PROVENANCE_BLOCKS=1`、7 键齐、`provider_resolvable=True`、`SPEC_FILE_EXISTS=True`、`ANCHOR_HITS=1`（`## 一、变更项（四项）`）、`CLAUSE_SHA_RECOMPUTED=f73f8dedc717019628bb10728da064e3f3030a86c934ef249b774f12dd60c9ae`、`CLAUSE_SHA_MATCH=True`、`VERDICT=PASS provider可解析 + 条款sha相符 + 锚唯一命中`。`spec_file` 所指登记件解析与条款 sha **均相符**，未出现派工书 §五.8 的停手条件；未改七件正文一字求绿。

**判据 9 · 写集对账**：`git -c core.quotepath=false show --name-only --format="" <施工笔>` → `SHOW_COUNT=8`，清单与 W1＋W2 声明闭集排序 `diff -u` → `J9_BUILD_DIFF_0_DECLARED_EQ_ACTUAL`。回执笔恰 1 件：由完工回报以 `git show --name-only --format="" <回执笔>` 实测（回执笔提交后才有读数，见 §三）。提交前另加保险：暂存区 8 个 blob 逐一 sha256 与源围栏比对 → `ALL_STAGED_BLOBS_BYTE_IDENTICAL_TO_SOURCE=True`（`core.autocrlf=true` 但入库规范化为 LF，与源逐字节一致）。

**判据 10 · 真源未触碰**：基线核实 `git merge-base --is-ancestor 6db881a 503ecca` → `YES`（真源 17:28 早于基线 19:41，基线态已含两真源件），`git rev-list --count 503ecca..HEAD` 施工前 =2。`git diff 503ecca..HEAD -- <v5 票面> <v5 回执> | wc -l` 施工笔后实测 `DIFF_LINES=0`（空输出）。两笔施工 commit 均不含这两件路径，收口态由完工回报以 `<收口HEAD>` 复核同命令。

**判据 11 · 收口洁净**：`git status --porcelain --untracked-files=no` 开工＝空、提交前复测＝空、施工笔后＝空；收口态（回执笔提交后）由完工回报实测。仓内大量 untracked 均为他案在制品（`.collab/ledger/`、`.collab/research/`、`.scratch/FX-*` 等），不在本票写集内，未 `add`、未改一字；判据口径为 `--untracked-files=no`。

---

## 三、HEAD 三时点、两笔 commit sha 与三态明示

| 时点 | 实测读数 |
|---|---|
| ① 开工 HEAD | `b9169c6`（`b9169c6492d81600d35c8a4dc1803921b35a6c1f`），tracked 面净 |
| ② 提交前复测 HEAD | `b9169c6`（`git rev-parse --short HEAD`，8 件落盘后、施工笔提交前实测；本票执行期并发线未前移，tracked 面净） |
| ③ 施工笔提交时点 | 父＝`b9169c6`；施工笔提交后 HEAD＝`9e04dc0`（`9e04dc0e3473a2178e698ca59f7c89a8baf7817f`） |
| ③ 回执笔提交时点 | 父＝`9e04dc0`；回执笔提交后 HEAD＝**不预写入正文**（自指即失配，同族 v5 回执 §一行 30 既定惯例），由完工回报以 `git log --oneline -1`／`git rev-parse HEAD` 实测给出 |

**两笔 commit sha**：
- 施工笔（W1 七件＋W2 夹具，8 件，单笔）：**`9e04dc0`**（`9e04dc0e3473a2178e698ca59f7c89a8baf7817f`），`collab:` 前缀，消息「SEMGOV-T1-BUILD 七件落地＋夹具」，带 `Ticket: TK-SEMGOV-T1-BUILD` trailer。
- 回执笔（W3 本件，1 件，单笔）：**本笔自身**；其 sha 按自指约束不预写入正文，由完工回报（给 team-lead 的 `SendMessage`）实测给出，与主理人「`git log` 尾笔对上回报 sha」查盘口径一致。此处明标「由完工回报给出」，非漏写、非编造。

**三态明示（逐条写，不合并成「已完成」）**：
1. **做了没落盘**：v5 blob 抽取/独立二次抽取/判据 7/8 读数捕获/清理，全部在仓外临时目录（`mktemp -d`）以 heredoc 内联 python 运行，仓内零临时脚本、零中间文件；此类工作物从未落盘到仓内。
2. **落盘没提交**：W1 七件＋W2 夹具在 `git add` 前为工作区 untracked 文件（已落盘、未提交）；此态存在于施工笔提交之前，已由施工笔提交消除。
3. **提交没对账**：施工笔提交后、`git show --name-only` 对账读数完成前，此态存在；现已完成对账（`J9_BUILD_DIFF_0_DECLARED_EQ_ACTUAL`）。回执笔提交后至完工回报给出收口态判据 9/10/11 复核前，同态由完工回报补齐，不预先标「已完成」。

**提交形态遵守**：显式逐路径 `git add` 8 件（禁 `-A`），核验暂存区 `STAGED_COUNT=8`、`STAGED_MODIFIED_TRACKED=0`；两笔各自单件/单批提交；未 `--amend`、未 `reset`、未 `--no-verify`、未强推、未改他人 commit。提交触发指针门禁钩子打印大量历史 `[check-pointers] … BLOCK OA-D6` advisory 行（约 7 MB），系既有 advisory 输出、非本票引入，按票面 §六.2 照常提交、未改门禁。

---

## 四、仓外临时目录清理读数

5 个 `mktemp -d` 临时目录（抽取源、独立二次抽取、判据 7 读数捕获、判据 8 三闸输出、判据 8 provider 复算）全部位于 `C:\Users\peter\AppData\Local\Temp`（仓外）。`rm -rf` 首次因 safe-delete 包装拒绝 Windows 盘符路径（`SAFE_DELETE_INVALID_PATH`），改用仓外 python `shutil.rmtree` 清理：

- 清理前存在性：5 个 `exists=True`（文件数分别 1/9/4/3/0）。
- 清理后复查：5 个 `exists_after=False`；`ALL_FIVE_TMPDIRS_CLEANED=True`。
- 夹具 `--mutate` 自建 `semgov-x-*`／`semgov-m-*` 副本残留：`SEMGOV_MUTATE_LEFTOVER=0`（脚本自清）。
- 判据 2/9 用的两个 `/tmp/*.txt` 中间文本：`rm -f` 后复查 `exists=NO`（两者）。

---

## 五、收口即停与完工定义

- 本票射程**仅**到「七件＋夹具落成真文件并回执落账」；未进入真文件审、真实 PRD 试填、改契约、升号、装配、部署或任何发布动作。收口后回报主理人，由主理人派 QA＋产品席对真文件审。
- 完工定义：**回执＋各笔全 commit 落账后**才算收束；「做了没落盘／落盘没提交／提交没对账」任一态按未收束计（三态已在 §三 逐条如实展开）。主理人查盘三件：`git status --porcelain --untracked-files=no` 净读数、`git log` 尾笔与回报 sha 对上、回执写入清单与 `git show --name-only` 逐件全等 —— 收口态三项由完工回报补齐实测读数。
