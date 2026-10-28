# 回执 · T-fuxi-rename-01 fuxi-skill 九卷改名批施工

> **开端 HEAD 实测读数**（本席 `git rev-parse HEAD` 时点·开工实测）：
> - `D:\multi-agent-collab-skills` ＝ `c42640eca84d407ffd1fed9f1c9f78877507b2e2`
> - `D:\multi-agent-collab-devkits` ＝ `6f03d0bef1b3d5db8a86e1e5d50020cdced7457e`
>
> **归属：执行者席（实例名 exec-engineer-tfix06）**
> 归席理由句：结构/闸/改动面＝架构席设计稿已定（《2026-10-28-设计稿-改名批-v1》＝条款文本真源），执行者照施工。
> 效力：fail-closed 照稿施工；本回执＝收口认盘依据，全部读数为盘上实测。
> 日期：2026-10-28（票链日内）

---

## 一、逐 S 步骤盘上坐标

### S1 · git mv 九卷＋R8 拆分出列（skills 仓）

- 九卷 `git mv` 保历史，`git status` 全 `R` 状态rename：`R1-人格镜片字段闭集.md→persona-lens-fields.md`／`R2-导入映射七式.md→import-mapping.md`／`R3-技法镜片六维卡.md→technique-lens-card.md`／`R4-归包判定与边界.md→pack-boundary.md`／`R5-验收卡与盲评规程.md→acceptance-blind-eval.md`／`R6-化名命名规程.md→alias-naming.md`／`R7-体量帽与拆件三式.md→token-cap-splitting.md`／`R8-契约锚与改判账.md→contract-anchors.md`／`R9-自主蒸馏工序.md→self-distillation.md`。
- 新建 `D:\multi-agent-collab-skills\.dev\`＋`fuxi-amendment-ledger.md`（账半）：表 α 照稿抄入＋R8 §三改判账全部照录＋R8 §四快照读数随迁＋R9 〔裁决出处〕段（E2）随迁入"builder 修订账"节续行＋旧名残留登记节。
- 判据实测：`git ls-files | grep -P '[\x{4e00}-\x{9fff}]'` ＝ **0**；`git log --follow` 抽三卷（self-distillation／contract-anchors／persona-lens-fields）均追至 `2407f18`／`c42640e`／`88ad58f`（＝Q2 判据的 fix-05/fix-03/fix-01 链）。

### S2 · 包内 M1–M9 全量改锚＋例外 E1–E5

- M1 文件名指针（32 处）→ 新文件名整串替换；M2 裸 `R#` 卷引用 → 裸基名指针（各卷＋SKILL 工序表＋README）；M3 标题行去卷号（`# R8 · 契约锚与改判账`→`# 契约锚与闸门条款`＝名实随拆分重定，其余＝`# <中文题>`）；M4 归属行 `分卷 R#·`→`分卷·`；M5 SKILL 工序主线"卷"列 9 行 17 枚→裸基名列；M6 SKILL references 索引重写（文件列去 `references/` 前缀＋表头上补"下表路径均在 `references/` 下"一行＋"内容"列删条款枚举尾＋"何时必读"列不动）；M7 `⛓ V3:行号` 一律未动；M8 `MC-FX-*`／`T-fuxi-*`／`D-NN` 一律未动；M9 卷内自指随机械走。
- E1＝R8 §三整节出列入账半（不重锚，旧坐标原文照录）；E2＝R9 〔裁决出处〕段出列入账半；E3＝R8 §四随迁＋A 半原位留一行"上游参照快照读数见账半"；E4＝FACT-1 条款文本内 `R9 卷四节（⛓ R9-…）`→`self-distillation 卷四节（⛓ self-distillation.md）`（入重签）；E5＝README 三处裸 R#（R9/R5/R6）按 M2 改齐。
- A→B 节间指针一行按稿立（contract-anchors 卷头〔改判账〕行＝运行期追溯指引非来历陈述；稿内编译段勾选项照留，zhurong 未建＝编译票再裁）。
- **V3 澄清注＝不立**（皮总拍板⑬票1＝A）。
- Y1 裁据句＝八字版「同形异判就此有裁据。」回 self-distillation 四节 7 款末句「复审帽必查直读原文。」之后紧接（长版未追）。grep 命中＝1。
- 判据实测：包内 `grep -rnE '\bR[1-9]\b' --include='*.md'`（去 V3: 坐标）**＝0**；`⛓ V3:` 计数前后等值（逐卷 22/29/14/13/17/26/14 等值；R8→contract-anchors 13→13 含账半留行；R9 0→0）＝锚未误伤。

### S3 · devkits 现役面按 §②.2 点名改（6 文件）

| 文件 | 改动 |
|---|---|
| `tools/check-pack-structure.py` | spec_file 三行（:5/:14/:23）→`contract-anchors.md`；FACT-1 spec_anchor 新版全文＋sha 重签；新立 MC-FX-NAME-1 provenance 块（初挂 sha）；件头注释"R8 卷"→"contract-anchors 卷"；NAME-1 lint 实现（见 S4） |
| `tools/check-truename.py` | spec_file 行→`contract-anchors.md`（锚/sha 未触＝V8-1 不重签）；件头注释措辞行 |
| `tools/check-blind-eval.py` | spec_file 行＋BLIND-1 spec_anchor 新版全文＋sha 重签；:15 注释→`acceptance-blind-eval 卷` |
| `tools/check-truename-pseudonyms.txt` | :3 维护面注→`alias-naming 卷` |
| `deliverables/skills/multi-collab/references/60-gates.md` | §四对账表 V8-1 行路径→`contract-anchors.md`＋STRUCT-1/2、BLIND-1、FACT-1 四行"R8 卷"→"contract-anchors 卷"（＝点名 5 行）；§四加 MC-FX-NAME-1 依据行＋json 围栏 per_spec 加 `"MC-FX-NAME-1": {"commit": "advisory"}`（NAME-1 spec_id 解析所需＝§⑤.2 机检挂点闭集内动作） |
- run-gates.sh 自身三 provenance 锚未触及（未碰锚行＝不重签，符合稿注）。
- 历史面（.collab 全部／.workbuddy/memory／判词／回执／engine-snapshots）零改动＝登记不改闭集（登记入账半"旧名残留登记"节）。
- 判据实测：`grep -rn 'R8-契约锚' tools/ deliverables/` ＝ 0。

### S4 · sha 重签链（§②.3）

- 重签二条款（＝设计稿判定"文本有动的"）：
  - BLIND-1（文内 `⛓ R5 ④-5`→`⛓ acceptance-blind-eval ④-5`）：新 sha ＝ `20881258b20a76abf7d65618b0660854400b1120f09f6b8cb2d2fa56b5b940f3` → `check-blind-eval.py` spec_anchor＋spec_clause_sha256。
  - FACT-1（E4 改锚）：新 sha ＝ `799061d58e39cb9aa3e4a7ae3fb6732156697bed706ea184905b31c2cfe937e8` → `check-pack-structure.py`。
- 不重签三条款复算等值实测（＝Q4）：V8-1 ＝ `c92d14e0…`（新旧同）／STRUCT-1 ＝ `1b0b2748…`（新旧同）／STRUCT-2 ＝ `6428536e…`（新旧同）——锚行逐字未动，sha 独立复算与脚本登记值相符。
- NAME-1 新条款初挂 sha ＝ `2d459a2bdb14b9c92ebd35b1b56b61c160fb5fa35587b6bf2b37898b08750411`。
- 闭合判据实测：`check-provenance.py` **exit 0**（锚命中唯一＋sha 相符）。
- kebab 正则算法口径＝check-provenance 规范（锚行去首尾空白→连续空白压单空格→UTF-8→sha256）。

**实现级偏离申报一处（候追认）**：NAME-1 kebab lint 首挂实测把装载面入口主件 `SKILL.md` 自触 BLOCK——`^[a-z0-9]+(-[a-z0-9]+)*\.md$` 字面对平台技能协议固定名 `SKILL.md` 永不可满足＝永假 BLOCK 闸（全生态 SKILL 包同样自触）。处置＝脚本侧对 `base=='SKILL.md'` 豁免（lint 对象实＝references 卷名），**条款文本一字未动**，该豁免在码内注释登记＋本回执申报候裁。属稿未写之机器细节，按"机检只验形态"精神择最小实现，不阻塞。

### S5 · 帽检前后读数表（script-v1／ceil／实测人＝exec-engineer-tfix06／被测 commit＝skills `76f30b7`）

| 件 | 改前（架构席§⓪基线） | 改后实测 | 稿预估 | 帽态 |
|---|---|---|---|---|
| SKILL.md | 2488 | **2455** | ≈2443（差+12） | OK |
| persona-lens-fields | 1808 | 1793 | 1794 | OK |
| import-mapping | 1877 | 1861 | 1862 | OK |
| technique-lens-card | 1036 | 1031 | 1031 | OK |
| pack-boundary | 1050 | 1034 | 1035 | OK |
| acceptance-blind-eval | 1932 | 1920 | 1921 | OK |
| alias-naming | 2497 | **2495** | 2495 | OK（贴线 WATCH 登记不阻塞） |
| token-cap-splitting | 1411 | 1401 | 1401 | OK |
| contract-anchors | 2499 | **2038** | ≈2019（差+19） | OK（余量 462） |
| self-distillation | 2492 | **2404** | 2410（差−6） | OK（余量 96） |
| README.md（不帽检） | 1592 | 1603 | 1606 | n/a |

逐件 ≤2500 全 OK；预估差全部 ≤±60＝无回 S2 触发。`check-pack-structure.py` 全套（含帽面＋结构面＋NAME-1 命名面）＝BLOCK 0／WATCH 52。

### S6 · run-gates 双仓

- devkits 仓根 `bash deliverables/skills/object-audit/scripts/run-gates.sh`：**exit 0／GATE PASS**；开工基线＝发现 448 条（MC-SOT-2 341／MC-SOT-1 54／MC-FX-FACT-1 52／MC-FX-BLIND-1 1），改后＝发现 479 条（MC-SOT-2 372／MC-SOT-1 54／MC-FX-FACT-1 52／MC-FX-BLIND-1 1）。**BLOCK=0 零新增红**；MC-SOT-2 差值＝改名引起的 WATCH 存量重组（旧九卷件头 `SKILL.md` 裸基名行 −8，新裸基名互指＋SKILL 索引新文件名行 +39，均为 D6 裁-21"裸基名不 BLOCK"既有口径），非新 BLOCK 类。
- skills 仓薄启动器 `bash tools/run-gates.sh`：**exit 0**（SOT=0 V8=0 STRUCT=0·WATCH=52）。

### S7 · 安装面同步（编译段未建＝本轮裸复制例外·先删后拷）

- `rm -rf C:\Users\peter\.workbuddy\skills\fuxi-skill\` → 整包复制真源 → `diff -rq` 真源包 vs 安装面＝**零差异（DIFF-EMPTY）**；旧中文九件已随删除动作清零，安装面 references 实测只存新九名。
- 安装面 grep 旧名（`R#-` 式＋九中文卷名）＝0；`.dev/` 账半不在包目录＝天然不在复制面（安装面零锚）。

### S8 · tag／bundle.lock（票面覆盖：不打 tag）

- **未打 tag**（tag `fuxi-skill@v1.4.0` 归收口票＝票面硬点）；skills 仓 tag 面实测仍至 `v1.3.0`。
- frontmatter version 未动（1.1.0 与 tag 现差＝稿⑦.2 登记不清账另票候补，本票不动）。
- bundle.lock：实测跨仓引用只到包名级（skills 仓无 bundle.lock 文件、他包无 fuxi 卷路径级坐标）＝零动成立（稿⑦.3 假设实证）。

---

## 二、三面旧名 grep 零残留实测（Q1）

```
devkits 现役面（tools/＋deliverables/）:
  grep -rn 'R[1-9]-' → 零命中（唯一例外＝check-pack-structure.py 内 NAME-1 lint 自身
    的正则字面 `R[1-9]-` 与条款抄录，属探针本体非残留）
  grep '契约锚与改判账|人格镜片字段闭集.md|…九中文名' → exit 1（零命中）
skills 仓装载面（skills/fuxi-skill/）:
  grep 'R[1-9]-' → exit 1；中文旧卷名 → exit 1；裸 \bR[1-9]\b（去 V3:）＝0
安装面（C:\Users\peter\.workbuddy\skills\fuxi-skill\）:
  grep 'R[1-9]-'（去条款正则字面）＝0；diff -rq 零差异
skills 仓他包 5 处〔R1-#N〕/〔R2-#1〕式＝视频团票号注记，不改（产品席已裁·账半登记）
```

**残留登记（非 Q1 闭集词·未点名不改）**：devkits 运行时消息字符串内"R9 卷／R9 四节／R5 卷"措辞三处（`check-pack-structure.py` WATCH 消息×2、`check-blind-eval.py` WATCH 消息×1）＋60-gates.md §四 FACT-1 依据行内"R9 卷 S0.5 候核账规程"——§②.2 点名闭集未含此四行（点名行仅"R8 卷"措辞行），按 fail-closed 未改，登记候收口票裁是否追改。

## 三、git 两仓 commit 读数

- skills 仓：HEAD＝`76f30b7`（开端 `c42640e`）＝`refactor(fuxi-skill): T-fuxi-rename-01 九卷英文语义名+R8拆分出列 (v1.4.0-pre)`；文件清单＝九 rename＋SKILL.md／README.md 改＋`.dev/fuxi-amendment-ledger.md` 新＝无越界。
- devkits 仓：开端 HEAD＝`6f03d0bef1b3d5db8a86e1e5d50020cdced7457e`；本批 commit＝`3f4bfe6`（`refactor(gates): T-fuxi-rename-01 devkits 现役面改名批同步…`）；文件清单＝§S3 表 6 文件＋60-gates（路由 json＋§四行）＝无越界；提交钩子 run-gates 实跑 GATE PASS exit 0。
  本回执随下一 devkits commit 入仓（回执件本身＝证据面）。

## 四、QA 判据自检对照（Q1–Q8）

| # | 自检 |
|---|---|
| Q1 | 三面旧名 grep 零残留＝上表实测 ✓ |
| Q2 | `git log --follow` 抽 self-distillation／contract-anchors／persona-lens-fields 追至 `2407f18`/`c42640e`/`88ad58f` ✓ |
| Q3 | experts 仓 tracked 文件零改动＋`git diff HEAD -- *perspective-design-v3*`＝空（0 行）✓ |
| Q4 | `check-provenance.py` exit 0；V8-1/STRUCT-1/STRUCT-2 sha 复算等值 ✓ |
| Q5 | 帽检表逐件入上表，全 OK 且与 §③ 预估差 ≤±60 ✓ |
| Q6 | run-gates 双仓 exit 0／BLOCK=0 零新增红 ✓ |
| Q7 | 安装面 diff 空；账半不在安装面；Y1 八字句 grep＝1 ✓ |
| Q8 | 账半＝表 α 九行＋旧名残留登记节非空＋R8 §三全文照录＋§四快照照录＋R9 裁决出处段照录 ✓ |

（回执终＝收口认盘不认报；本件落盘 commit 见 git 节末注。）
