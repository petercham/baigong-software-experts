# PUB-EXCL 批 QA 独立验证 v1（fresh eyes·证伪导向）

- 席位：qa-pubexcl（PUB-EXCL 批独立验证席）
- 日期：2026-11-05
- 验证对象：PUB-EXCL 票面 8f26d5d ＋ 实装笔 a9dddd2 ＋ 工程师回执 58a3a67
- 方法：不信施工方回执，一切以本席实测为准；六判据逐项。

## 一、开端 HEAD 实测读数

- `git -C /d/multi-agent-collab-devkits rev-parse --short HEAD` = **58a3a67** ✓（与票令预期一致，继续验证）
- 分支 = main；`git status --porcelain` 输出空＝工作区净（跑装配器前后各核一次，均净）。
- 注：实测期间本席 `py_compile` 于 `agent-skills/object-build/scripts/__pycache__/` 产生的编译缓存为 gitignore 未跟踪件（`git check-ignore` 命中），不入装配面（取料走 `git archive`＝已提交 blob）、不改 HEAD、porcelain 恒净——非工作区脏。

## 二、判据逐项读数

### 判据① 对账 — 绿
- `8f26d5d`（票面）：恰一件 `.scratch/tickets/2026-11-05-PUB-EXCL-assemble-process-domain-exclusion-ticket.md` ✓
- `a9dddd2`（实装）：恰三件 `README.md`、`agent-skills/object-build/SKILL.md`、`agent-skills/object-build/scripts/publish.py` ✓
- `58a3a67`（回执）：恰一件 `agent-experts/baigong-software-team/.collab/receipts/2026-11-05-PUB-EXCL-receipt.md` ✓
- `git log 8f26d5d..58a3a67`＝两笔（a9dddd2＋58a3a67），链上无交杂 commit ✓
- `git status --porcelain` 工作区净 ✓

### 判据② 实装忠实性 — 绿
- 排除码位于 `git_archive_blobs()` 成员循环内（现版 L730-731），紧跟既有 `__pycache__/.pyc` 过滤（L728-729）之后、`result[rel] = …`（L732）之前，与票面 §3.2 落点一规格一致。
- 判定式＝段匹配：`any(seg in (".collab", ".scratch") for seg in rel.split("/"))`，非子串匹配 ✓
- diff 另见 publish.py L676 一处 docstring 防误读补注（候裁④裁定落笔，随带注释非逻辑改动，仍在 publish.py 件内）。
- 对抗例实测（python -c 单测判定式，12 例全对）：
  - 命中不误漏：`.collab/x.md`、`a/.collab/b/x.md`、`x/.scratch/y.md`、`src/.collab`（末段）、`a//.collab/b.md`（空段旁路）均判排除 ✓
  - 子串不误伤：`.collabx/foo.md`、`x.collab/foo.md`、`a/.scratchx/b.md`、`foo.collabbar.md`、`my.collab.bak/y.md` 均判保留（bad=0）✓
- `python -m py_compile agent-skills/object-build/scripts/publish.py` exit 0 ✓

### 判据③ 装配面读数独立实测 — 绿
- `find` 装配面（`D:/multi-agent-collab-devkits-build/baigong-software-team/`）总文件数 = **112** ✓（钉 112）
- `ASSEMBLY.manifest.json` `files` = **110** ✓（钉 110）；元数据两件 = `COPY.state` + `ASSEMBLY.manifest.json`，112 = 110 + 2 ✓
- EAC target（`skills/external-advisor-collab/`）= **8 件** ✓；deep-research target（`skills/deep-research/`）= **11 件** ✓
- 装配面内 `.collab`/`.scratch` 段文件数 = **0** ✓（find＋grep 段匹配式）
- 交叉自洽核算：源仓 HEAD tracked bundle 618 件 − 过程域 526 件 − `bundle.lock`（装配器 `body_exclude` 索引件，publish.py L864-867 既有行为）= 92 件；92 + EAC 8 + DR 11 = 110＝manifest files ✓；COPY.state 末块（[sync n=1]）文件行 = 110 ✓；装配面文件清单与「源仓交付段＋两组件」逐路径 diff 全等 ✓
- 附带核：装配面 `plugin.json` version = 0.1.22 与源仓 bundle.lock/plugin.json 三同源读数一致；bundle 版本线未 bump＝本轮装配面（注册态产物）内容变化不入版本账，符合纪律①射程（README 随动的只是 object-build v0.6 行）。

### 判据④ 幂等 — 绿
- 跑装配器前核源仓 `git status --porcelain` 净（源一致性闸前提成立）。
- 命令：`python agent-skills/object-build/scripts/publish.py --assemble "D:/multi-agent-collab-devkits/agent-experts/baigong-software-team"`（票面判据 1 同款）
- 输出＝「baigong-software-team: 装配面已一致（第 1 块，110 文件），零写入」exit 0 ✓（命中幂等短路，未追加空块）
- 复跑前后装配面读数不变：`find | sort | sha256sum` 摘要全等、总文件数 112→112 ✓

### 判据⑤ 活性反证 — 绿（加分项实锤）
- 取 841c3ec（a9dddd2 之前）旧版 publish.py 与现版，同一输入（repo=devkits 仓、ref=HEAD、prefix=bundle 路径）分别调 `git_archive_blobs()`：
  - 旧版：members=**618**，其中 `.collab`/`.scratch` 段成员=**526**（样例 `.collab/README.md`、`.collab/board/board-2026-10-30.md`、`.collab/decisions/2026-10-22-裁决记录.md`）
  - 现版：members=**92**，其中过程域成员=**0**
- 同一输入·旧含 526 过程件·现零成员＝排除码真正在起作用，非空转 ✓

### 判据⑥ 禁动面零命中 — 绿
- `git diff 841c3ec..HEAD --name-only` 改动面恰五件：票面（.scratch/tickets/…）、README.md、object-build SKILL.md、publish.py、回执（.collab/receipts/…）——全部落在允许清单内 ✓
- `git diff 841c3ec..HEAD --name-only -- agent-skills/external-advisor-collab/ agent-experts/baigong-software-team/bundle.lock` = 0 行 ✓
- `.collab/` 下改动仅回执一件；FUXI 相关（`git diff --name-only | grep -i fuxi`）= 0 ✓
- README diff 核＝仅 object-build 行 v0.5→v0.6 一处，baigong 行 v0.1.18 原文未动（旧行账态＝既有观察项，非本批引入）。

## 三、红黄绿计数

- **红 0 ｜ 黄 0 ｜ 绿 6**（判据①～⑥全绿）＋活性反证实锤加分 1

## 四、活性反证与观察

1. 活性反证读数见判据⑤：618→92、526→0，排除码活性确凿。
2. 观察-1：本席 py_compile 副产物 `scripts/__pycache__/publish.cpython-313.pyc` 为 gitignore 未跟踪件，不入装配面、porcelain 恒净，不构成工作区脏（留档防后人误读）。
3. 观察-2：README v0.1.18 旧行与 bundle.lock 0.1.22 三同源差账＝841c3ec 既有账态（此前 QA 报告已列为既有观察），非 PUB-EXCL 批引入，射程外不记账。
4. 观察-3：装配器 `body_exclude` 把 bundle.lock 排除出装配面属既有行为（L864-867），与 PUB-EXCL 新增排除两条码互不干扰；判据③交叉核算已消化该差值（618−526−1=92）。

## 五、结论

**放行。** 六判据全绿、红 0 黄 0；实装忠实票面规格（成员层段匹配·位置正确·对抗例零误伤），装配面读数 112/110/8/11/0 五钉全中，幂等零写入复现，排除码活性实锤，禁动面零命中。
