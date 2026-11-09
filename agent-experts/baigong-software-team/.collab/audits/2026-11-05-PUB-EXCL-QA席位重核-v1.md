# PUB-EXCL 批 · QA 席位重核 v1（qa-team-pex · fresh eyes · 独立证伪）

- 性质＝合法席位重核：此前一次核验（`96b065b`，件＝`.collab/qa/2026-11-05-PUB-EXCL-QA独立验证-v1.md`）因派工席位不合规被判无效重派；本席对该旧核验件**零读取**（仅列名取证），全部读数本席亲自实跑，工程师自报与旧核验读数一律不采信。
- 开工实测 HEAD＝`96b065b`（main·≥`841c3ec` ✓）；`git status --porcelain`＝空（净）；分支＝`main`。
- 被验三笔：票面 `8f26d5d`／实装 `a9dddd2`／回执 `58a3a67`；票面真源＝`.scratch/tickets/2026-11-05-PUB-EXCL-assemble-process-domain-exclusion-ticket.md`（本席完整直读，判据唯一来源）。
- 复测置仓外 Temp＝`D:/qa-team-pex-tmp/`（Windows 盘符形态，跑完即弃）。
- 计数口径＝occurrence；全部命令本席实跑附读数。

## 一、判据① 对账（恰账／链上／净面／reflog）

| 目 | 实跑读数 | 判定 |
|---|---|---|
| 票面笔 `8f26d5d` name-only | 恰 1 件＝票面本体（`.scratch/tickets/2026-11-05-PUB-EXCL-...-ticket.md`） | 绿 |
| 实装笔 `a9dddd2` name-only（`-c core.quotepath=off`） | 恰 3 件＝`README.md`＋`agent-skills/object-build/SKILL.md`＋`agent-skills/object-build/scripts/publish.py`，与票面 §六 闭集全等 | 绿 |
| 回执笔 `58a3a67` name-only | 恰 1 件＝`agent-experts/baigong-software-team/.collab/receipts/2026-11-05-PUB-EXCL-receipt.md` | 绿 |
| 链 `841c3ec..HEAD` | 恰 4 笔＝`8f26d5d`（票面）→`a9dddd2`（实装）→`58a3a67`（回执）→`96b065b`（无效席位旧 QA 笔，派工令在册承认）；三笔间无交杂他件 | 绿（见观察-1） |
| 工作区 | `git status --porcelain`＝0 行 | 绿 |
| reflog | `git reflog -100 --format="%gd %gs"` 精确扫 `amend/reset/rebase/cherry` 动作词＝**0 命中**（初扫 4 命中系 commit message 正文含 "cherry/amend" 字样，非动作记录） | 绿 |

## 二、判据② 实装忠实性

- 直读 `publish.py` 现版 `git_archive_blobs()`（def L708）：排除逻辑落在**成员循环内**——`rel` 剥前缀＋反斜杠归一之后、`result[rel] = ...` 之前，紧跟既有 `__pycache__` 排除行后，与票面 §3.2 落点一逐字相符：
  ```python
  if any(seg in (".collab", ".scratch") for seg in rel.split("/")):
      continue  # 过程域段不入交付面（PUB-EXCL·皮总 2026-11-05「补」·㊺交付物纯度）
  ```
  段匹配＝`rel.split("/")` 逐段与 `(".collab", ".scratch")` 元组等值比对（`seg in tuple`＝等值非子串），非子串匹配 ✓。
- **对抗例实测**（Temp 仓 `D:/qa-team-pex-tmp/excl-test/` 自建，9 条受控路径，直接 import 现版/旧版 publish.py 调 `git_archive_blobs()` 同输入对拍）：
  - 现版输出 6 条：`.collabsub/f.txt`、`.collabx/c.txt`、`filecalled.collab`、`keep.txt`、`x.collab/d.txt`、`y/.collabfoo/e.txt` ——被排除恰 3 条：`.collab/a.txt`、`.scratch/b.txt`、`deep/.collab/inner.txt`。
  - 子串形态**零误伤**：`.collabx`／`x.collab`／`.collabfoo`／`.collabsub`／文件级 `filecalled.collab` 全部保留（5/5 零误伤）；嵌套深层段 `.collab` 正确排除。
  - 旧版（`841c3ec` 版 publish.py）同输入输出 9 条全含（含 3 条段命中）＝排除确为本批新增。
- 语法闸：`python -m py_compile agent-skills/object-build/scripts/publish.py` → exit **0** ✓。
- diffstat 对预算：`git show --stat a9dddd2`＝3 files, 5 insertions(+), 2 deletions(-)（publish.py +3 行＝排除 2 行＋docstring 候裁④补注 1 行；SKILL.md ±1；README ±1）＝票面 §十一 预算 ≤10 行内。
- 版本两点随动实读：SKILL.md frontmatter `version: 0.6`（L5）；README L40 版本账 object-build 行 `v0.6` ✓（README L54 沿革映射行 `v0.5` 为历史沿革陈述非版本账行，不在票面闭集射程）。

## 三、判据③ 装配面读数（仓外 `D:\multi-agent-collab-devkits-build\baigong-software-team\`）

| 目 | 命令口径 | 钉值 | 实跑读数 | 判定 |
|---|---|---|---|---|
| 文件总数 | `find . -type f \| wc -l` | **112** | **112** | 绿 |
| manifest files | `ASSEMBLY.manifest.json` `"files"` | **110** | **110** | 绿 |
| 元数据两件 | `COPY.state`＋`ASSEMBLY.manifest.json` 在根 | 均在 | 均在（112＝110＋2 闭合） | 绿 |
| COPY.state 末块 | `[sync n=1]` 块 `^[0-9a-f]{64} ` 行数 | **110** | **110** | 绿 |
| 过程域段文件 | 票面 §七 2a awk 段匹配口径 | **0** | **0** | 绿 |
| 过程域目录 | `find . -type d \( -name .collab -o -name .scratch \)` | 0 | **0**（目录级亦零） | 绿 |
| EAC target | `find skills/external-advisor-collab -type f` | **8** | **8**，逐件枚举与票面 §七 3a 钉值枚举全等（SKILL.md／docs/STRUCTURE.md／references/{10-roles,20-rounds,30-discipline,40-artifacts,90-changelog}.md／sources/spec-anchors.md） | 绿 |
| deep-research target | `find skills/deep-research -type f` | **11** | **11** | 绿 |
| 既有排除不回归 | `__pycache__` 目录／`*.pyc`／`bundle.lock` | 0/0/不存在 | **0／0／不存在** | 绿 |
| 注册面主文件 | `test -f .codebuddy-plugin/plugin.json` | exit 0 | 存在 ✓ | 绿 |
| C4 组件解析 | manifest components | tag＋40 位 hex | `external-advisor-collab@v1.1.2`→`62f0043b2830...2531`、`deep-research@v1.0.2`→`730962e160bc...4dfe`，ref_kind 均＝tag | 绿 |
| bundle_version | manifest | 0.1.22 三同源 | **0.1.22** | 绿 |

## 四、判据④ 幂等复跑

- 跑前闸：源仓 `git status --porcelain`＝0 行（净，源一致性闸前提成立）。
- 跑前装配面摘要：`find . -type f -print0 | sort -z | xargs -0 sha256sum | sha256sum`＝`81f19570380f6f43a395f9f4594031848bbb71cd02ca43a6cac5c8865178c5f2`。
- 票面工序命令复跑：`python agent-skills/object-build/scripts/publish.py --assemble "D:/multi-agent-collab-devkits/agent-experts/baigong-software-team"` → exit **0**，末行＝`baigong-software-team: 装配面已一致（第 1 块，110 文件），零写入`（含「零写入」✓）。
- 跑后同口径摘要＝`81f19570380f6f43a395f9f4594031848bbb71cd02ca43a6cac5c8865178c5f2`，`cmp` 前后文件＝**逐字节全等**。绿。

## 五、判据⑤ 活性反证（旧版 vs 现版同输入对拍）

真实源仓 bundle 本体面输入（`git_archive_blobs(repo, "58a3a67", "agent-experts/baigong-software-team")`）：

| publish.py 版本 | 取料成员总数 | 过程域段成员 |
|---|---|---|
| 旧版（`git show 841c3ec:...publish.py`） | **618** | **526** |
| 现版（`a9dddd2` 后） | **92** | **0** |

618−526＝92＝现版读数，闭合恒等成立；排除效果实锤非假绿。绿。

## 六、判据⑥ 禁动面零命中

`git -c core.quotepath=off diff --name-only 841c3ec..HEAD` 全链改动面实跑＝**6 件**：票面／README／object-build SKILL.md／publish.py／回执＝被验五件全在册，第 6 件＝`agent-experts/baigong-software-team/.collab/qa/2026-11-05-PUB-EXCL-QA独立验证-v1.md`（无效席位旧 QA 笔 `96b065b` 产物，居 QA 席位写域、系本次重派链条既有事实，非三笔实装面产出——见观察-1）。

禁动面逐面 diff 命中数（同口径）：

| 面 | 命中 |
|---|---|
| `agent-skills/external-advisor-collab/`（正文条款） | **0** |
| `agent-experts/baigong-software-team/bundle.lock` | **0** |
| `agent-skills/fuxi-skill/`（FUXI 账域） | **0** |
| `agent-experts/baigong-software-team/` 内容面（剔除 `.collab/qa/`＋`.collab/receipts/` 两过程域路由后） | **0** |
| 门禁族 `tools/`＋`agent-skills/object-audit/` | **0** |
| `agent-skills/bundle-assembly-registration/`（候裁②不入本票随动） | **0** |
| `agent-skills/object-build/references/60-publish.md`（候裁③否动随动） | **0** |
| tag 面 | 9 枚在盘，`external-advisor-collab@v1.1.2`→`62f0043b...2531` 未挪 |

## 七、开工复测四件随带复现（票面 §十三口径，本席重测）

1. HEAD ≥ `841c3ec` ✓（现 `96b065b`）。
2. publish.py 锚文命中：`__pycache__` 排除行现文逐字在位、排除两行紧随其后 ✓。
3. 装配面三读数：本席读数口径为**重核后现盘**＝112/110/0（旧 664/662/552 为施工前基线，工程师回执已附复测，本席以终态判据覆盖）；装配面 `find | tr | grep` 子串-非段名段＝**0**。
4. §1.3 子串-非段名段落实测：源仓 HEAD 树 `-c core.quotepath=off` 口径＝**0** ✓。注记：默认 quotepath 口径会得 31 命中，明细＝`".collab` ×31——系 git 对含中文路径段的八进制转义引号前缀假象（`\"`＋段名拼出伪段），非真实段落；`quotepath=off` 复测归零，停止条件歧义条款未触发。

## 八、红黄绿计数

- **红 0｜黄 1｜绿 6**（判据①–⑥ 逐判全绿；黄-1 为派工钉值措辞与盘态差异，非实装缺陷，详见观察-1）。

## 九、活性反证与观察

- 活性反证：判据⑤ 旧/现版对拍 618/526 vs 92/0 实锤（见五）；对抗例 9 路径对拍 6/9（见二）——两路均证明排除码真实生效且无误伤通道，无假绿捷径。
- 观察-1（黄-1）：派工令判据⑥ 钉「diff 841c3ec..HEAD 改动面只落票面/README/object-build SKILL.md/publish.py/回执**五件**」，本席实跑全链＝**六件**，多出恰＝无效席位旧 QA 笔 `96b065b` 的报告件（`.collab/qa/` 写域内、派工令自身承认其在链上并要求 HEAD 从其起算）。**被验三笔实装面改动＝恰五件闭集成立**；禁动面八面逐面 0 命中不受影响。定性＝派工钉值未把重派链条既有笔计入，呈 lead 知悉即可，不构成实装面红项。
- 观察-2：回执 §写入清单自报 publish.py「+4（含续行）」vs `git show --stat` +3——回执以含续行口径计数，`--stat` 以 hunk 行计数，两读数同笔不矛盾（diff 全文本席直读逐行核对：排除 2 行＋docstring 补注 1 行）。
- 观察-3：`git_clean_or_die` docstring 补注一行＝候裁④「lead 2026-11-05 裁定采防误读补写」——补写全文回执逐字申报与 `a9dddd2` diff 实文逐字一致，落点在 publish.py 闭集件内。但如实申报证据层级：本席 `git grep -l "PUB-EXCL"` 全 `.collab`＋`.scratch` 域检索＝仅票面／回执／旧 QA 件三件命中；链级 `git log --grep="PUB-EXCL"`＝仅本批四笔，**无 PUB-EXCL 候裁裁定登记笔上盘**（本仓体例有「collab: 拍板登记」先例如 `ec2a238`），独立裁定件亦未上盘，裁定痕迹＝回执自报＋回执笔 commit message 「候裁四条按裁定落笔」措辞。票面原案 §四 对该 docstring 标「不动」＋§十二 候裁④标「本票否动」，补写之合规性完全系于该裁定属实；若 lead 侧无此裁定记录则此一目应回落为越票面红项。呈 lead 确认裁定在册即可销。
- Temp 现场：`D:/qa-team-pex-tmp/`（excl-test 对抗仓＋digest/log 件），仓内零运行残留；`__pycache__` 仅源仓 py_compile 副产物由既有 gitignore/排除口径辖域，工作区净读数佐证。

## 十、结论

**总裁决＝放行（红 0 黄 1 绿 6）**。PUB-EXCL 批（票面 `8f26d5d`＋实装 `a9dddd2`＋回执 `58a3a67`）三笔恰账、实装忠实票面 §3.2（段匹配成员层·对抗例零误伤）、装配面五钉全中（112/110/8/11/0）、幂等零写入摘要逐字节恒等、活性反证两路实锤、禁动面八面零命中。黄-1＝派工钉值措辞与链条既有事实差一笔，呈 lead 备案不拦。

——qa-team-pex（software-team-qa·PUB-EXCL 席位重核）。开工 HEAD `96b065b`·本席零读旧核验件·全部读数实跑。
