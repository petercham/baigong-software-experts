# ITER-W0B · README 门面刷新票（v1·填空式薄票·起草笔零施工）

- 票号：ITER-W0B（ITER-NEXT 批次 W0 次票·族名锁定勿改）
- 票名：README 门面刷新票
- 票型：门面刷新微票（README Token 表重算＋悬空指针改口径＋references 头注去点名·纯文案面零代码零逻辑）
- 起草席：架构席 software-team-architect（ITER-NEXT W0 开票笔·主理人派工）
- 票面落点：.scratch／tickets／2026-11-17-ITER-W0B-README门面刷新票-v1.md
- 载体形制＝皮总 11-17 薄票裁定三块（获批登记＋当轮取证读数＋当批增量＝声明闭集）＋验收判据节＋候裁单列；薄票模板未产（W1-T1-0 才产），本票按裁定 §二.2 手工填空（放行登记 §一.1 在册）

> 票面自注（防自咬体例）：叙述面一切路径＝裸文＋全角斜杠（U+FF0F·下同），不落反引号路径指针、零 at 符号；引用既有原文以 ⟦⟧ 标记；命令一律缩进段（非围栏反引号）。本票成文前已以探针件实测：缩进段含不存在路径 exit 0＋叙述面裸文点名 spec-anchors／v2.9-copy／deploy-gate 三面 exit 0（指针识别需反引号围裹＝裸文叙述不触发·探针用毕即拆 ls 坐实）。本票落笔前自靶 python share/check-pointers.py --root . --target 本票面实路径 须 exit 0（读数见完工回报）。

---

## 〇、获批登记（指令原话＋计划行＋写集路径＋段界）

- **皮总开工指令原话**（2026-11-17 15:44·放行登记 8454c38 在册引同文）：⟦对照迭代计划，开工实施"百工软件团队"的下一轮迭代！⟧＝批次整体认可触发。
- **计划 v2 §五 W0 行 T0b 逐字**：⟦T0b｜README 门面刷新：Token 表按实测重算（274 行/6,494 token）、两处悬空指针改口径、7 份 references 头注去点名文件⟧（.collab／board／2026-11-17-五份复盘合流与下一轮迭代计划-v2.md §五）。
- **现势实数随正**：放行登记 8454c38 采纳值 2 ⟦references 十一件非七份⟧——头注去点名按 §一 现跑点名命中面出（十一件中命中七件）；悬空指针现跑 BLOCK 三枚非计划所称两处（差量见 §四 J-1）。
- **口径真源**：盘点件 O7 节（.collab／board／2026-11-17-专家团包实体盘点与优化方案-v1.md 行 213-218）＝Token 表按现五卡重算＋指针改口径＋头注去点名；版本账迁 CHANGELOG 一项**不入本票射程**（见 §四 J-2）。
- **写集路径清单**：①agent-experts／baigong-software-team／README.md；②agent-experts／baigong-software-team／skills／software-orchestration／references／ 十一件头注行（执行面＝§一 点名命中七件的承载行·其余四件头注零触）。
- **段界**：本票只管 起草（本笔）／QA 单席快审／主理人票级放行／工程师施工／QA 独立验收／收口登记 全六段的载体与判据；起草笔只产本票面，零改 README、零触 references、零执行清理。
- **前奏降档依据**：薄票裁定件（0a53ea5 链上）§二.2＝薄票＋单席快审一次；放行登记 8454c38 §一.2 采纳值 1 在册。

## 一、当轮取证读数（起草轮现跑·禁抄计划旧数）

警示行（R3 假钉值教训在册）：本节全部读数＝当轮现跑，下游验收读数各自当轮现跑，本表只作起草态基线对照。

| 项 | 命令 | 实测读数（2026-11-17 16:05~16:20 现跑） |
|---|---|---|
| 时点 | date '+%F %T %z' | 开工 2026-11-17 16:05:28 +0800（收尾复跑见完工回报） |
| HEAD | git rev-parse --short HEAD | 开工＝**8454c38**（＝W0W1 放行登记笔）；落笔＝本票父笔（W0A 落链后链顶＝4217aa1 系本批 W0A 票笔·链序照登） |
| index.lock | ls .git／index.lock | **不存在**（NO_INDEX_LOCK） |
| 脏面 | git status --porcelain | tracked 脏面 **零枚**＋?? 当轮计数 **29 行**（他案活体群·照登零带入禁钉死） |
| README 行数 | wc -l 于 agent-experts／baigong-software-team／README.md | **98 行**（与放行登记 §〇 相符） |
| Token 表现行读数面 | python share／count_agent_tokens.py ＋ 带 glob 臂 "agent-experts／baigong-software-team／agents／*.md" | 缺省臂＝外仓七枚全 OK（1889／2462／2480／2465／2289／2496／2496·exit 0·**面非百工五卡**＝README 现表口径错位实证）；五卡臂现跑＝lead **1736**／product **1103**／architect **1162**／engineer **1261**／qa **1232**·**exit 0 全 OK**；行数面 wc -l＝lead 79／product 47／architect 48／engineer 50／qa 50＝**274 行**；合计 token＝**6,494**（与计划 v2 §五 T0b 括号值全等＝现表 628 行／7,999 token 旧账失实坐实） |
| 红线 2500 面 | grep -n "2,500\|≤2500" README＋python share／count_agent_tokens.py 行 7 | README 行 83 ⟦判据线＝每席 ≤2,500（红线）⟧＋行 85 表头 ⟦≤2500?⟧ 在册＝**字面值禁动**；脚本行 7 ⟦RED_LINE = 2500⟧＝线值真源（皮总 10-25 拍板值·DEBTCLN-R5 收口在册·该脚本文件禁触） |
| README 悬空指针现跑 | python share／check-pointers.py --root . --target agent-experts／baigong-software-team／README.md | **exit 1**＝BLOCK **3 枚**＋WATCH **1 枚**：行 38 ⟦sources／spec-anchors.md⟧ BLOCK／行 44 ⟦skills／sop／references／{product,architecture}-v2.9-copy.md⟧ BLOCK／行 62 ⟦references／deploy-gate.md⟧ BLOCK／行 27 WATCH 提及嫌疑 software-company-team-lead.md（裸基名不 BLOCK）。＝计划所称「两处」系旧读数（现势三枚·差量归 J-1） |
| references 现数 | ls 于 agent-experts／baigong-software-team／skills／software-orchestration／references／ | **十一件**（与放行登记 §〇 相符：bugfix-path／collab-rules／delivery-summary／deploy-gate／dev-discipline／dispatch-discipline／handoff-discipline／incremental-dev／partial-workflows／quick-mode／standard-sop） |
| 头注点名 grep 现跑 | grep -c software-company-team-lead 于 references／*.md | 点名命中＝**七件各恰 1 枚**（bugfix-path／collab-rules／delivery-summary／incremental-dev／partial-workflows／quick-mode／standard-sop＝头注承载行形制＝本件承载 ＋反引号围裹 software-company-team-lead.md＋（fork v1.2.0）§… 逐字下沉件…）；零命中＝四件（deploy-gate／dev-discipline／dispatch-discipline／handoff-discipline＝头注已泛指形制·零触）。盘点所称「7 份」在头注面恰中＝旧数唯悬空指针面滞后 |
| README 自身点名 | grep -c software-company-team-lead README.md | **4 枚**（行 27／35／46／63 版本账叙述面＝fork 沿革史文·射程见 §四 J-3） |
| 目标件存在性 | ls 于 agent-experts／baigong-software-team／agents／ | 现五卡＝software-team-lead／product／architect／engineer／qa 五枚在位＝software-company-team-lead.md 仓内确无同名件（WATCH 语义相符） |
| 基线门禁 | python share／check-pointers.py --root . 缺省扫描 grep -c BLOCK／WATCH | **BLOCK 22809／WATCH 4582**（与 R5 收口定格同态·活体面禁钉死） |

## 二、声明闭集（写集＋禁动面·写死）

**S1 · 写集具名清单（上限面单）**：

1. agent-experts／baigong-software-team／README.md（改动面＝Token 计数节重算＋悬空指针口径句改写·版本账史文段禁改，见禁动面）
2. references／ 七件承载行改写（具名＝bugfix-path.md／collab-rules.md／delivery-summary.md／incremental-dev.md／partial-workflows.md／quick-mode.md／standard-sop.md；改法＝头注承载行点名件名改泛指口径句，保留 ⟦源/施工 commit 账目由仓侧维护、不随包分发⟧ 泛指句与其余正文 byte 零扰动）；references／ 其余四件（deploy-gate／dev-discipline／dispatch-discipline／handoff-discipline）头注零触

**泛指口径句规格（七件同形·逐字）**：承载行反引号点名段 ⟦software-company-team-lead.md⟧ 改 ⟦软开团队 lead 席位卡（出身自市场包 software-company v1.1.0 之 fork）⟧；行内 ⟦（fork v1.2.0）⟧ 及其余成分原样。改后该七行 grep software-company-team-lead 命中翻零；改后各件自靶须 exit 0（探针形制已实测 exit 0 在册 §票面自注）。

**S2 · README 改动面规格**：

1. **Token 计数节重算**：表体五行＋合计行改当轮现跑值＝行 79・47・48・50・50／token 1736・1103・1162・1261・1232／全部 ≤2500 绿／合计 274 行・6,494 token；表列形制（口径版本＝script-v1）沿用；⟦读法⟧ 段旧账叙述同步改口径（旧值转沿革注或删旧留新＝施工席定文风，判据只钉表体数字对脚本现跑输出逐项全等）。
2. **悬空指针改口径三枚**（行 38／44／62 现位）＝按盘点件 O7.2 精神：⟦sources／spec-anchors.md⟧ 句补泛指限定「仓侧登记件，不随包分发」；⟦skills／sop／references／{product,architecture}-v2.9-copy.md⟧ 句改指明现位 skills／sop／references／ 在位件形制（该两件仓内实存在＝见禁动面核查行）；⟦references／deploy-gate.md⟧ 句补包内现位限定。改后 README 自靶 **exit 0**（BLOCK 三枚清零；WATCH 行 27 枚属 J-3 射程，未裁则照旧）。
3. 版本账史文段（行 30-71）**叙事内容零改写**＝仅允许 S2.2 三处指针口径句的最小随动；行数随动如实照登禁钉死。

**禁动面（写死）**：

- **Token 表口径要素四件禁改值**＝①script-v1 口径声明②ceil 取整声明③判据线 ≤2,500 与目标 ≤2,350 字面④实测基线句式——只改表体数据行，不改口径要素含义与 2500／2,350 线值字面。
- **2500 线值真源不动**＝share／count_agent_tokens.py 整件禁触（numstat 面单零出现）；该脚本 --limit 参数化面（DEBTCLN-R5 已收口）＝验收命令可用 --limit 但缺省 2500 语义零变。
- agents／ 五卡零触；skills／software-orchestration／SKILL.md 零触；references／ 十一件正文（承载行外）byte 零扰动；skills／sop／references／ 三件零触（product-v2.9-copy／architecture-v2.9-copy／collab-fixed-structure 在位件＝README 行 44 指向的 {product,architecture}-v2.9-copy 名现势实存于该目录＝悬空归因待 J-1 细分，施工面只改 README 叙述不搬件）。
- 链上史件零回改；账本零手写；FUXI 零碰；?? 他案群照登零带入；.gitignore 零触；.collab／ 全桶零触（回执笔除外）。

## 三、验收判据（用例唯一产出处·全机械·命令＋期望读数·读数由命令输出嵌入禁手填）

- **V0 开工读数**：施工轮现跑 HEAD＝本票落链后链顶如实照登；NO_INDEX_LOCK；tracked 脏面零枚＋?? 当轮照登（禁扩集）。
- **V1 Token 表逐项全等**：施工轮现跑 python share／count_agent_tokens.py "agent-experts／baigong-software-team／agents／*.md" → **exit 0**；表体五行 token 与 wc -l 行数与该输出＋wc 现跑 **逐项全等**（起草轮钉值 1736・1103・1162・1261・1232／79・47・48・50・50＝对照基线；五卡＝tracked 冻结面，漂移即停手回报）；合计行＝现跑求和（起草轮＝274・6,494）。
- **V2 红线字面零动**：grep -c "2,500" README → **1**（行 83 判据线在场）；git show --numstat 施工笔对 share／count_agent_tokens.py **零出现**；README ⟦≤2500?⟧ 表头字面在场。
- **V3 自靶翻正**：python share／check-pointers.py --root . --target agent-experts／baigong-software-team／README.md → **exit 0**（起草轮基线 exit 1·BLOCK 3 在册；J-3 未裁态 WATCH 行 27 不拦 exit——WATCH 不属 findings 拦截面＝改前 BLOCK 三枚清零即可翻 0，起草轮实态佐证：该件改前 exit 1 纯因三 BLOCK）。
- **V4 头注去点名坐实**：grep -rc software-company-team-lead 于 references／ → 七件承载行命中全 **0**＋四零触件保持 0＝**十一件合计命中 0 枚**；泛指口径句在场：grep -c "不随包分发" 于该七件 → 各 **≥1**（保留泛指口径句判据）。
- **V5 他文件零触＝面单核验**：git show --numstat 于施工笔 → 文件集 ⊆ {README.md ＋ references／七件}＝**恰八枚上限**·删除行对 references 各件 ≤1（承载行改写型）；对 agents／・SKILL.md・sop／references／・share／ 全部 **零出现**；缺省指针扫描 BLOCK 计数对基线 **只降不升**（起草轮 22809 对照·降量归因＝README 三枚＋头注七枚反引号点名面消解·逐枚归因禁遮掩）。
- **V6 链面与回执**：RECEIPT 笔面单恰 .collab／receipts／2026-11-17-ITER-W0B-施工回执-工程师席-v1.md 一枚；回执自靶 exit 0；BUILD／RECEIPT 面单核验照 R2 收口 §四 终版口径（staged 实测＋钩子 STAGED-DECL 互证）。

## 四、候裁单列

- **J-1｜悬空指针枚数差量（两处 vs 现跑三枚）**：计划 v2 §五 与盘点件 O7.2 所称「两处」＝旧读数；现跑 BLOCK 三枚（行 38／44／62）。其中行 44 所点 {product,architecture}-v2.9-copy 花括号复合名虽在 skills／sop／references／ 有同名实存件，但花括号复合 token 不可解析＝仍判悬空。**提请拍**：三枚全改口径（本票 §二 S2.2 按此备办）或按计划字面只改两处。不夹进判据；未裁态按三枚备办，票级放行随裁校正。
- **J-2｜版本账 15 行迁 CHANGELOG 不入本票**：盘点件 O7.4 含迁移项，计划 v2 §五 T0b 行未含＝按「计划行为准」自决排除。**若主理人裁并入**＝写集扩 CHANGELOG 一枚随 rev 补，不预判。
- **J-3｜README 自身 software-company-team-lead 四处（行 27／35／46／63）**：属版本账沿革史文（fork 出身事实陈述）＋WATCH 非拦截面；SCFIX 批「在册留置四处零动＝现态出身事实」先例在册。**提请拍**：史文保留照旧（本票按此备办·V3 未裁态可翻 exit 0）或随门面批改泛指（rev 补面）。

批次编排类不上楼＝不自列候裁；J-1／J-3 属改动面边界分歧归人拍，J-2 属射程并入归主理人。

## 五、链衔接纪律（各笔共守·写死）

- 开工现跑 HEAD＋链序照登（本笔父＝W0A 落链笔 4217aa1）；单 pathspec add 紧邻 commit；FX_COMMIT_DECLARE 挂 commit 命令侧＝票面仓根相对路径；commit 前先跑自靶 exit 0。
- 尾标＝-TICKET（先例 6b57304／8eff7c2／4217aa1 开票笔在册）；族名 ITER-W0B 随 message 内嵌。
- 禁 add -A／禁 amend／禁 --no-verify；message 以 collab: 起头·零 at 零反引号·＝号串联关键读数。
- pre-commit 跑全套 run-gates 约 300+ 秒＝commit 类命令 timeout 600000（先例 8454c38 首笔逾时未落链教训在册）。
- 撞锁两态口径＝lock 在飞等待自然消退、实证陈旧按先例删锁留证；他案脏面（?? 29 行当轮群）照登零带入。
- 临时工作物只落仓根 .scratch／ 本票取证族（本笔探针已用毕即拆 ls 坐实零残留）；本席起草笔只写票面这一件，README 与 references 零触（修票不施工）。

---

（v1 尾·append-only：后续修订在此处续 rev 段，rev 段间互不回改）
