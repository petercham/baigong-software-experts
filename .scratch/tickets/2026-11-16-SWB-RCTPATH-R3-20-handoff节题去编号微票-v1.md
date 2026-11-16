# SWB-RCTPATH-R3 · 20-handoff 节题去编号微票（v1·纯规格票·零施工·零规范落笔）

- 票号：**SWB-RCTPATH-R3**（族名锁定，勿改）
- 票名：**20-handoff「留存过程件正文内的仓内文件引用写法」节题去编号微票**
- 票型：维护·微票（小改动快审链＝SCRATCHCFG 先例链：开票→双席快审→放行→工程师 BUILD＋RECEIPT 两笔→fresh QA 独立验收→收口）
- 起草席：架构席 arch-rcttk3（fresh 实例·主理人派工）
- 票面落点：.scratch／tickets／2026-11-16-SWB-RCTPATH-R3-20-handoff节题去编号微票-v1.md
- 来源与裁定依据：SWB-RCTPATH 甲案条款经 RCTPATH-R2 修订票（票面 89f796d／rev-1 b6a4ac6·归裁登记 4ea0d58）落规范面（BUILD 0da2566·收口登记 b2b61d7）时，节题以「二之二」插档编号插入。决策者（皮总）斥「二之二」命名反人类，经选项归一亲选**「去编号自然题」取向**＝节题改为无序号自然题形态；且确立「今后规范面插新节不再造『X之二』式插档编号」取向。本票＝该裁定的规范面执行票。
- 候裁点：**0 枚**（见 §四论证：两项随动裁量均已本席论证自决闭合，无实质分歧呈裁）。

> **票面自注（防自咬体例）**：本票正文对一切路径仅叙述性提及＝裸文写＋全角斜杠（／U+FF0F），不落反引号路径指针；引用既有原文以 ⟦⟧ 标记替换。§二 施工规格块内的旧行／新行＝落笔实文本（构成条款实质·两块内均不含路径 token·天然安全）。本票面成文后自靶 python share/check-pointers.py --root . --target 本票面实路径 须 exit 0（读数见 §七）。

---

## 〇、开工读数（起草轮现跑·禁抄旧数）

| 项 | 命令 | 实测读数 |
|---|---|---|
| 时点 | date '+%F %T %z' | 2026-11-16 17:55:12 +0800 |
| HEAD | git rev-parse --short HEAD | **b2b61d7**（＝RCTPATH-R2 收口登记笔＝链顶·派工预期值全等） |
| tracked 脏面 | git status --porcelain 过滤 | ledger 一枚 M 态（agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl）＋仓根散件群（.collab 根散 md 十二枚／.collab／research 散 md 六枚／.py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt）——全部他案脏面，照登零带入零清理 |
| 落点件行数 | wc -l agent-skills／multi-collab／references／20-handoff.md | **66 行**（＝R2 收口后 58＋8 现势） |
| 目标行定位 | grep -n 二之二 该件 | **仅行 28 恰一枚**（该件内「二之二」字样唯一命中＝单行替换无歧义） |
| V4′ 基线 | python share/check-pointers.py --root . --target 落点件实路径 | **exit 1·恰一枚悬空＝行 24**（BLOCK OA-D6＝deliverables／experts／baigong-software-team／skills／software-orchestration／references／handoff-discipline.md 旧径悬空·不在 share／baseline-pointer-exempt.json 豁免清单＝该件 grep handoff-discipline 计数 0 实测） |
| 缺省 BLOCK 钉值 | python share/check-pointers.py 缺省扫描 grep -c BLOCK | **22810** |
| 缺省 WATCH 钉值 | 同轮 grep -c WATCH | **4581** |
| 全仓 GATE 钉值 | bash share/run-gates.sh | **GATE PASS exit 0·发现 151502**（三钉值全部与派工预期现跑全等） |
| 链上锚 | git cat-file -e <sha>^{commit} 逐枚 | 4ea0d58／89f796d／b6a4ac6／8cb7fc1／764afbf／5adf535／b2b61d7 全部在位 exit 0 |
| 本席 scratch 工作区 | — | .scratch／rcttk3／（完工自删·commit 留证保留） |

## 一、案件本体

RCTPATH-R2 已收口：甲案条款（两域两制·留存过程件正文仓内文件引用写法）以「二之二」插档编号节题 append 落规范面（全链 89f796d→…→0da2566→659ec9a→5adf535→b2b61d7 在册闭环）。收口后决策者裁定：「二之二」式插档编号命名反人类，节题改去编号自然题形态；并确立今后规范面插新节不再造「X之二」式插档编号之取向。

本票＝该裁定的规范面落地微票：**只改一行节题，条款正文与其余一切零触碰**。条款效力不因节题措辞变动而变——节题是编号与注记壳，条款本体＝条目 1–5 正文（行 30–34），本轮零改动。

## 二、施工规格（票体①·声明闭集内·逐字写死）

### S1 · 节题行单行替换（唯一施工面）

落点件＝agent-skills／multi-collab／references／20-handoff.md，**行 28 单行替换**。旧行与新行均不含路径 token（反引号包裹仅为块内引文安全，非指针落笔）：

```markdown
旧行（行 28 现行 verbatim）：
### 二之二、留存过程件正文内的仓内文件引用写法（两域两制·决策者裁定 SWB-RCTPATH 甲案）
```

```markdown
新行（施工后 verbatim）：
### 留存过程件正文内的仓内文件引用写法（两域两制）
```

- 替换＝同位单行换行（行数不变：66→66；diff 恰 1 增 1 删单 hunk）。
- 工程师照录 §二 两块内实文本，一字不改（V3 逐字符对等判据）。

### S1 附论证 · 裁定 ID 注记（「决策者裁定 SWB-RCTPATH 甲案」字样）去留＝**去**（本席裁量结论·非候裁）

决策者选定自然题形态 verbatim 不含该注记；本席独立论证同向取去，三条理由：
1. **裁定沿革真源在链不在壳**：甲案裁定与沿革已登记于归裁登记 4ea0d58、票面 89f796d／b6a4ac6、收口登记 b2b61d7——链上件＝史实锚，规范面节题无需自带 ID 徽章（指针只指不搬·记录链≠正文链）。
2. **注记本身即插档编号思维的伴生物**：「X之二·决策者裁定 ID」是插档补丁的两件套；去编号留 ID 注记＝壳去半截，与决策取向（自然题）不彻底。
3. **可追溯性不损失**：节题正文「留存过程件正文内的仓内文件引用写法（两域两制）」字样与归裁登记件、票面族名互查可达（grep 语义词即中），无需节题内嵌 ID。

按派工口径：默认＝按决策者选定形态执行，不单列候裁。

### S2 随动裁量项 · 「今后规范面插新节不再造 X 之二编号」取向是否另立规范条款＝**不立**（本席论证自决·不上缴）

1. **取向已由票面执行体现**：本票新节题（无编号自然题）即先例实物——规范面先例＋票面成文叙述（本 §一／§二 在册）＝体例归一的依据面已足；QA 抽验与人工闸（dev-discipline §七 口径）可承载纪律面。
2. **YAGNI／最小改动面**：另立条款＝扩写面（新条款文本＋落点节选定＋二次验收面），与本微票「只动一行」声明闭集直接冲突；无现行违例压力（全仓 tracked 面「二之二」式插档编号除本行外零存量——git grep 实测其余命中全部居 external-advisor-collab 外包 refs 族＝不在本仓规范面射程），无条款必要。
3. **自指悖论**：若立「禁插档编号」条款，该条款本身即一次「插新节」动作——立在哪、编什么号，当场撞自身射程；规避成本（如落既有节内随增行）又回到扩面。
结论：取向以**先例＋票面成文**形态生效，不落新规范条款。候裁 0 枚。

### 声明闭集（施工面封顶）

- `agent-skills/multi-collab/references/20-handoff.md` 行 28 节题行**单行替换**＝本票唯一规范面施工（S1）。
- 工程师两笔＝BUILD（上述单件单行替换）＋RECEIPT（票附回执落 .scratch／tickets／ 桶·SCRATCHCFG 先例体例：回执名基名 2026-11-16-SWB-RCTPATH-R3-工程师回执 族·精确落名施工时定）。

### 禁动面（写死）

- 同件其余任何行零触碰：行 1–27、29–66 全部一字不动；**行 29–34 甲案条款正文（条目 1–5）零改动**；行 24 遗留悬空指针（deliverables 旧径·V4′ 基线恰一枚）**零处置**——不背不修不删（另案候补池性质沿用 R2 rev-1 N-1 口径）。
- 其余规范件零触碰：agent-skills／dev-discipline／references／20-handoff.md 不在仓（实测 agent-skills 无 dev-discipline 目录）＝按派工口径登记为「该路径不存在·自然零触」；实际同族纪律件 agent-experts／baigong-software-team／skills／software-orchestration／references／dev-discipline.md 一字不触（含被引用的 §三／§七／§八-5 节）。
- 链上一切历史件 append-only 零回改：归裁登记 4ea0d58、原票面 8792a97、R2 票面 89f796d／rev-1 b6a4ac6、双席判词 8cb7fc1／764afbf、QA 验收判词 5adf535、收口登记 b2b61d7、施工笔 0da2566、回执笔 659ec9a——其中一切「二之二」字样**一律不回改**（史账不回改）。
- 门禁配置零触：share／ 全域、share／baseline-pointer-exempt.json、60-gates 面零动（本票无新闸）。
- 账本面零手写：ledger／leases 零碰；`.gitignore`／`.collab／` 案卷面零触。
- 他案脏面（ledger M 一枚＋仓根散件群）零带入零清理。

## 三、验收判据（票体②·全机械·命令＋钉值）

- **V0 开工读数**：当轮现跑 HEAD（开工链顶＝本票落链 sha 后后继笔起点）＋git status 他案脏面清单照登＝与 §〇 形态一致。
- **V1 byte 级单行 diff**：施工笔后 git diff <本票链>..HEAD -- 落点件实路径 ＝仅该件；git diff --numstat ＝**1 增 1 删**；hunk 外零改动（65 行上下文零前导 +/-）。
- **V2 新旧行逐字符对等**：施工前 git show HEAD 该件行 28 与 §二 旧行块**逐字符全等**；施工后该件行 28 与 §二 新行块**逐字符全等**（python 单行提取比对 exit 0 形态）；该件 wc -l **66→66**；grep -c 二之二 该件 **1→0**；grep -c 决策者裁定 该件 **1→0**（字样仅存于行 28·§〇 grep 实证明细可复跑）。
- **V3 结构节序**：施工后该件节题面（grep -n '^## \|^### '）＝行号 5／9／28／36／55／62 六节不动位；节序＝一／二／（行 28 新自然题）／三／四／五 完整连续——QA 旧口径「一／二／二之二／三／四／五」中「二之二」槽位由新自然题节题逐字替换，余槽零变（新旧节题清单 diff 恰一行）。
- **V4′ 差量基线复证**：开工基线＝python share/check-pointers.py --root . --target 落点件实路径 → **exit 1·恰一枚悬空＝行 24**（deliverables 旧径·不在 baseline-pointer-exempt.json 豁免清单）；施工后同式读数与基线对拍＝**零新增 BLOCK／WATCH**（行 24 读数枚数与内容逐字不变；该枚仍另案不背）。
- **V5 全仓门禁钉值现跑全等**：bash share/run-gates.sh → GATE PASS exit 0·**发现 151502**；缺省扫描 python share/check-pointers.py grep -c BLOCK ＝**22810**、grep -c WATCH ＝**4581**——三钉值与 §〇 开工读数全等零摆动（票附回执落 tickets 桶不在缺省扫描域＝不扰钉）。
- **V6 边界**：git show --name-only BUILD 笔＝恰落点件一枚；RECEIPT 笔＝恰回执一枚；两笔零触其余真源／门禁／账本面；禁动面 pathspec 域 git diff 零命中。
- **V7 自靶**：票附回执靶检 python share/check-pointers.py --root . --target 回执实路径 → **exit 0**；本票面（链上现文）--target exit 0 复证。

## 四、候裁面（必有节·**候裁 0 枚**）

两项随动裁量已在 §二 论证自决：① 裁定 ID 注记去留＝去（决策者选定形态 verbatim 不含注记＋三条独立理由同向，无对立方案残余）；② 「不再造 X 之二编号」取向＝不另立条款（先例实物＋票面成文已体现取向，立条款撞 YAGNI 与自指悖论）。两项均无实质分歧，不入呈裁面。如双席快审发现真分歧按程序单列另呈。

## 五、与微票链的衔接

本票＝链第 1 步（架构席起草·本笔）。第 2 步＝产品席＋QA 席双席 fresh eyes 快审（审 S1 逐字规格可判性／禁动面完备性／V 系可机械性／两项自决论证可驳性）。第 3 步＝放行登记（主理人）。第 4 步＝工程师单席两笔：BUILD（单件单行替换）＋RECEIPT（票附回执）。第 5 步＝fresh QA 按 §三 V 系独立验收。第 6 步＝收口登记（主理人）。取向生效时点＝第 4 步 BUILD 落链笔；「今后插新节不造 X 之二」自收口起以先例＋本票 §二 成文面生效。

## 六、落链纪律段（起草笔与后续各笔共守·写死）

- 单件 pathspec 两端齐带（add 与 commit 各带本笔面路径）；**add 紧邻 commit 零窗口**；commit 前 git diff --cached --name-only 坐实仅自件。
- FX_COMMIT_DECLARE＝仓根相对纯路径清单（逗号或换行分隔）**挂 commit 命令侧**（环境变量前置挂 commit；挂 add 侧会被 STAGED-DECL-BLOCK 拦——share／check-staged-declaration.py 机理在册）。
- 禁 add -A／禁 amend／禁 --no-verify；message 以 collab: 起头·零 at 符号·零反引号；尾标置 message 最末位。**本票各笔尾标闭集**：本票笔 -TICKET／QA 快审笔 -QA-REV／产品快审笔 -PM-REV／放行登记笔 -PM-RELEASE／工程师施工笔 -BUILD／工程师回执笔 -RECEIPT／QA 验收笔 -QAV／收口登记笔 -GCLOSE（族名 SWB-RCTPATH-R3 随尾标内嵌）。
- 一票一 commit 增量落盘；commit 类命令 timeout 600000ms；撞 index.lock 有界等待零删锁。
- commit 输出重定向 .scratch／rcttk3／（工程师席随其席族目录）＝完工自删（commit 留证保留）。
- 防自咬体例＝票面／回执正文路径裸文＋全角斜杠叙述形态；引用既有原文用 ⟦⟧ 标记；票面自身须过 python share/check-pointers.py --root . --target <票面> **exit 0** 后才可落链。
- 临时工作物只落仓根 .scratch／<席族>／ 族；只写票面这一件（起草笔），不碰规范面本体。

## 七、起草笔自证

- 开工读数＝§〇 全表（当轮现跑·HEAD b2b61d7 与派工预期全等）。
- 落笔前靶检＝python share/check-pointers.py --root . --target .scratch／tickets／2026-11-16-SWB-RCTPATH-R3-20-handoff节题去编号微票-v1.md → 期望 exit 0（落笔后、commit 前实跑，读数随回报）。
- 本笔面＝恰票面一件；规范面／链上件／门禁配置／账本面全程零触碰；他案脏面零带入。
