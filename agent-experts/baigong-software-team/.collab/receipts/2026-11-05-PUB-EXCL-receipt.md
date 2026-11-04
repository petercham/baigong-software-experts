# PUB-EXCL 施工回执（engineer-lockfix 席·装配面过程域排除口径实装票）

- 票面真源＝`.scratch/tickets/2026-11-05-PUB-EXCL-assemble-process-domain-exclusion-ticket.md`（票面落链 `8f26d5d`）·决策依据＝皮总 2026-11-05 01:07「按你的推荐，补」。
- 开端 HEAD 实测＝`8f26d5d`（≥ ANCHOR 要求 ≥`841c3ec` ✓）；`git status --porcelain` 基线＝空（净）。
- 施工笔 HEAD＝`a9dddd2`（三件闭集·单 commit·未用 --no-verify·未 amend）。
- 计数口径＝occurrence；判据自带落盘重定向；负例 exit≠0。

## 开工复测四件（§十三）

1. `git rev-parse --short HEAD` ＝ `8f26d5d` ✓
2. publish.py L727-728 现文逐字命中 §3.2 锚文（`if "__pycache__/" in rel or rel.endswith(".pyc"):` → `continue  # 编译缓存件不入装配面`）✓
3. 装配面三读数复测＝**664 / 662 / 552**（total／manifest files／过程域段匹配）——与 §1.2 钉值全等 ✓
4. §1.3 子串-非段名段落实测＝**空**（未触发停止条件歧义条款）✓

## 前置工序（§七）

`rm -rf D:\multi-agent-collab-devkits-build\baigong-software-team\`（仓外派生产物·10-assemble.md §六既有唯一处置）→ 重装配。删面后 -build 目录内仅剩既有 `baigong-software-team.zip`（既往文件，未触）。

> 时序注记：首笔实装后曾按序跑 py_compile（exit 0）与装配，装配器纪律⑤源一致性闸 fail-closed exit 3（`M README.md` 未提交＝前提不成立正确拦截）；随即先落 commit `a9dddd2` 再重装配＝闸语义正常，非实装缺陷。

## 写入清单（commit name-only 对账口径）

`git -c core.quotepath=off show --name-only --format= a9dddd2` ＝ **3 件**，与票面 §六 产出闭集全等：

```
README.md
agent-skills/object-build/SKILL.md
agent-skills/object-build/scripts/publish.py
```

- 落点一：publish.py `git_archive_blobs()` tar 成员层追加段匹配两行（`__pycache__` 排除行之后、`result[rel] = …` 之前）——单点覆盖本体面（L862）与组件面（L871）两条取料路径；`body_exclude` 零重构零搬家；未用 pathspec 排除层（保住「取源路径下无文件 ⇒ exit 3」空结果校验原语义）。
- 落点二：object-build SKILL.md frontmatter `version: 0.5`→`0.6`。
- 落点三：仓根 README 版本账 object-build 行 `v0.5`→`v0.6`（候裁① lead 裁采·版本账同源人工对账）。
- diffstat＝3 files, 5 insertions(+), 2 deletions(-)（publish.py +4：排除两行＋docstring 补注两行〔含续行〕；SKILL.md ±1；README ±1）＝预算内（≤10 行）。

## 候裁四条落笔申报（lead 2026-11-05 裁定）

- 候裁①＝采：README 版本账行随动已入闭集落点三（闭集 3 件照票面）。
- 候裁②＝不入本票：排除纪律成文入 bundle-assembly-registration 挂候补池——本批该包零触 ✓（name-only 交集为空）。
- 候裁③＝照票否动：未挂 spec-provenance；来历以代码注释标注（`PUB-EXCL·皮总 2026-11-05「补」·㊺交付物纯度`）✓。
- 候裁④＝采：`git_clean_or_die` docstring 防误读补写一行（票面未给定稿句，按候裁段语义一句话措辞，全文如下）：「（PUB-EXCL 补注防误读：本句只讲「未跟踪文件」这一类；已跟踪过程域段自 PUB-EXCL 批起另由取料成员层排除，两事两条码。）」——该补写在 publish.py 内，已含于 `a9dddd2`，非本回执目。

## 判据 1–7 逐条读数（全部实跑）

| # | 判据 | 读数 | 判定 |
|---|---|---|---|
| 1 | 重装配成功 | `已装配（第 1 块，110 文件，bundle@a9dddd2）` exit **0** | GREEN |
| 2a | 过程域零入面 | 段匹配计数＝**0** | GREEN |
| 2b | 装配面文件总数 | `find . -type f \| wc -l` ＝ **112** | GREEN |
| 2c | 装配全账计数 | manifest `"files"` ＝ **110** | GREEN |
| 2d | 账本末块行数 | COPY.state 末块 `^[0-9a-f]{64} ` ＝ **110** | GREEN |
| 3a | EAC target 非空＋计数 | **8** 件（枚举见下） | GREEN |
| 3b | deep-research target | **11**（零过程域，前后不变） | GREEN |
| 4 | 幂等复跑 | `装配面已一致（第 1 块，110 文件），零写入` exit **0** | GREEN |
| 5a | 既有排除不回归 | `__pycache__` 目录＝**0**；`*.pyc`＝**0**；装配面无 `bundle.lock`（不存在） | GREEN |
| 5b | 注册面主文件仍在 | `test -f .codebuddy-plugin/plugin.json` exit **0** | GREEN |
| 5c | 三元数据在位 | COPY.state＋ASSEMBLY.manifest.json 均在 | GREEN |
| 6 | 语法闸 | `python -m py_compile …publish.py` exit **0** | GREEN |
| 7 | 工序出口判据 C1–C7 | 见下表 | GREEN |

判据 3a EAC 八件逐件枚举（与票面钉值枚举全等＝ref 树 35−27 互证）：

```
skills/external-advisor-collab/SKILL.md
skills/external-advisor-collab/docs/STRUCTURE.md
skills/external-advisor-collab/references/10-roles.md
skills/external-advisor-collab/references/20-rounds.md
skills/external-advisor-collab/references/30-discipline.md
skills/external-advisor-collab/references/40-artifacts.md
skills/external-advisor-collab/references/90-changelog.md
skills/external-advisor-collab/sources/spec-anchors.md
```

判据 7 · C1–C7 全表读数（C8–C10 属注册段＝本票射程外，不跑不记）：

- C1 装配器 exit 0 ✓
- C2 装配全账存在；files 110 ＝ 装配面非元数据计数（112−COPY.state−ASSEMBLY.manifest.json）110 ✓
- C3 同步账本存在；末块 [sync n=1] 文件行数 110 ＝ 全账计数 110 ✓
- C4 两组件解析 commit 40 位十六进制＋ref_kind＝tag 与索引件一致：external-advisor-collab@v1.1.2→`62f0043b2830c8b4000a98e1e65b05dcff422531`；deep-research@v1.0.2→`730962e160bcf5b25f549c21f17c2c36848f4dfe` ✓
- C5 装配面＝仓外同级 `D:\multi-agent-collab-devkits-build\baigong-software-team\`，不在任何源仓树内 ✓
- C6 两 target 非空目录（8／11 件）✓
- C7 幂等复跑含「零写入」exit 0 ✓

版本读数随带：manifest bundle_version＝0.1.22（与 lock/plugin 三同源一致，零漂移）。

## 禁动面自查（票面 §四）

bundle.lock／两 tag（`external-advisor-collab@v1.1.2`·`v1.1.1`）／百工 bundle 全树（`agent-experts/baigong-software-team/`）／门禁族（tools/＋object-audit check-*）／FUXI 账域／60-publish.md／bundle-assembly-registration 包——`a9dddd2` name-only 三件与上述各面**交集为空** ✓（本回执件为 collab 域单独 commit，亦在禁动面之外）。

## 钩子噪音登记

`a9dddd2` 提交时 check-pointers/check-ticket-reconcile 输出大量既有 WATCH/BLOCK 账项（票 88·发现 170 全 WATCH），末行 **GATE PASS**（发现 8831 条按路由表走②不拦提交）＝既有账态如实通过，零 --no-verify。

## 红黄绿汇总

判据 1–7 ＝ **全绿（红 0 黄 0）**；开工复测四件全等复现；候裁四条按 lead 裁定落笔无偏离。

——engineer-lockfix（PUB-EXCL 施工席）。
