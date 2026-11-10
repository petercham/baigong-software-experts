# QA-SCRATCHREV · SWB-SCRATCHG 规格票 v1 QA 席独立审（B席·fresh eyes·证伪导向）v1

- 被核件：`.scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v1.md`（落链笔 `00f7e7d`，本席 `git show --name-only 00f7e7d` 实测恰一件＝本票面 ✓；`wc -l` 实测 **173** 行＝派工书所称 174 系尾行口径差，照登不影响判定）
- 审席：QA 席 `qa-scratchrev`（fresh 实例）；A 席（产品席）并发审同一票，本席零读其产出
- 总裁决：**红 1／黄 5／绿 6**——红项一条（§一 复点①与链漂移注读数系 quotepath 口径假象，票面自设的「已知案型」陷阱本票自陷）；票体四块主体规格（S1 规则块机理／S2 分流判据族／S3 联动面／V 判据族）经独立复跑与仓外探针证伪**大部成立**，修单归作者席与候裁面

## 〇、开工读数（本席当轮现跑·全部 `git -c core.quotepath=off` 口径另注）

- `date` ＝ `Tue Nov 10 19:33:42 2026`
- `git rev-parse HEAD` ＝ `00f7e7dd2cfcdb09af4603f02930663a43275324`（＝派工钉值恰等，无后续他案笔）
- `git status --porcelain --untracked-files=no` ＝ 空（净，零残项）
- 口径声明：本审全部计数默认 `-c core.quotepath=off`＋NUL 安全式双验；票内如用默认口径（中文路径转义带引号）读数，单独分账（见红-1）
- 引用可达：票 §六 commit 锚五枚 `329d16c`／`14416e9`／`f135855`／`adc4dc3`／`d83d452` 全部 `git cat-file -e <sha>^{commit}` 实测在位 ✓

## 一、红项（1）

### 红-1 · §一 复点①＝109 与链漂移注「仓根票面 10→37（他案落链所致）」＝quotepath 口径假象——同 HEAD 双口径实测证伪

- 票面位置：§一 表 L22（复点① `git ls-files | grep -c '/\.scratch/\|^\.scratch/'` ＝ **109**「＝主理人现值全等」）、L23-24（复点② `-z | tr` 口径＝136）、L31 链漂移注（「仓根 `.scratch/tickets/` tracked 数由 10 增至 37（SEMGV 线／PROJINIT／GWP-DEPLOY 票面他案落链所致）」）、§七(b) L155 佐证引用。
- 本席独立实测（现跑）：
  - 同一提交 `329d16c`：默认口径 `git ls-tree -r --name-only 329d16c | grep -c '/\.scratch/\|^\.scratch/'` ＝ **109**；`quotepath=off` 口径 ＝ **136**。
  - 同一提交 `14416e9`：默认口径 ＝ **109**；`quotepath=off` 口径 ＝ **136**。
  - 仓根 tickets 桶：`329d16c` 默认口径 ＝ **10**、off 口径 ＝ **37**；`14416e9` off 口径 ＝ **37**。
  - `git diff --name-only 329d16c 14416e9` ＝ 恰两文件（`agent-skills/fuxi-skill/.collab/receipts/2026-11-10-FUXI-FX-U38放行登记-v1.md`＋`agent-skills/fuxi-skill/.collab/tickets/2026-11-10-FUXI-FX-U38起草回执-v1.md`），仓根 `.scratch/tickets/` 命中 ＝ **0**。
  - 全链扫（`git rev-list` 前 700 笔逐笔 off 口径计数变化点）：`.scratch` tracked 总数 109 的时点＝`5c39456`（11-07 13:36），此后至 `329d16c` 单调爬至 136，**起草窗（18:56→19:04）内该值恒为 136 无跳变**。
- 判定：复点①（默认口径）与复点②（NUL 原始口径）之间 109→136、票面桶 10→37 的「漂移」全部由**命令形态切换**产生——默认口径下 CJK 路径转义为带引号八进制行（`329d16c` 树内带引号 tracked 行 1057 枚、仓根 tickets 桶带引号 **27** 枚），grep 锚式 `^\.scratch/` 对其漏数；两 HEAD 各自同口径读数完全相等＝起草窗内 tracked .scratch 面**零漂移**。「SEMGV 线／PROJINIT／GWP-DEPLOY 票面他案落链所致」归因不实（上述诸票 11-07/11-08 已落链，均已在 `329d16c` 树内）。票 §一 表头自称「occurrence 口径＋双验」，恰落入票链上既立的 quotepath 转义漏数已知案型；「＝主理人现值全等」＝两个同口径错读互证，不构成双验。§七(b) 并发佐证面（10→37）随此污染——共享 index 并发风险事实面（同窗 staged 他案一枚属实）仍在，但票内给出的票面数漂移佐证为假。
- 修单向：§一 复点①/链漂移注按双口径重写归因；§七(b) 佐证句换实读数。归作者席。

## 二、黄项（5）

### 黄-1 · §一 未跟踪读数「双验 ✓」分解归组互斥不干净＋现轮漂移

票 L25：`?? .scratch` ＝199「双验：仓根不带引号 163＋仓根带引号 2＋百工包内 30＋fuxi 包内 4＝199 ✓」。本席现轮复跑：总 ＝ **201**（漂移＋2 可容，V0 当轮再实测吸收）；但按同式分解＝仓根不带引号 167＋仓根带引号 2＋百工 30＋fuxi 4＝**203 ≠ 201**——差值来自镜像目录行子路径双重归组（仓根 `.scratch/FX-U11-qa/adv-*/...` 行内含包内 `.scratch/` 子串，同时命中两组模式）。票内 199 组自洽系同案型下的凑和式对账，「✓」不成立。基线类读数，不翻判定，登记随修。

### 黄-2 · 票头「候裁点：单列 §七 六条」与 §七 实列七条自相矛盾

票 L9 现文「六条」；§七 实列 **(a)-(g) 七条**（本席机检 `grep -c '^- \*\*('` 对 §七 段＝7）；§八 L164「候裁七条呈皮总归裁」与落链笔 message「候裁七条单列」均为七。表述面内部矛盾，一行勘正。

### 黄-3 · 租约段 deny_globs 与候裁(e) B-i 取态矛盾未登记

票 L147-150 租约段：path_globs 含 `.gitignore`＋`agent-experts/baigong-software-team/.scratch/COLLAB-STRUCT-1/*`；deny_globs 含 `/**/.collab/**`。而 §4.2 B-i（L102）＝`git mv` 至**所属项目 `.collab/receipts/`**——目标面正落在 deny_globs 禁写面内。若候裁(e)裁 B-i，本租约段承载不了处置面，须随裁改租约；票面未登记该依赖。禁动面与取态二面的联动缺口，一行补注可修。

### 黄-4 · V7 第三式「缺省口径」照字面不可跑＋run-gates 无基线钉值

票 L137 V7。本席现跑 `python share/check-ticket-reconcile.py`（仓根 cwd）＝ **exit 2**「未能定位仓根；请用 --root 指定」——该脚本 `find_root`（`share/check-ticket-reconcile.py` L126-138）向上找 `deliverables` 目录，本仓无此目录，缺省调用必失败；`share/run-gates.sh` 内调带 `--root "$ROOT"`（L141-156 段实测），带 `--root .` 重跑＝exit 1·票 134／发现 184 全 WATCH。V7 判据句「`python share/check-ticket-reconcile.py` 缺省口径读数不新增阻断」照字面不可跑，须补 `--root`；且「GATE PASS 前后对拍发现数不新增」未钉基线数（本席基线现跑 `bash share/run-gates.sh` ＝ GATE PASS 发现 **150138** exit 0，可作参照钉值）。

### 黄-5 · tickets 桶豁免＝全桶免忽略，票面对「临时调试物借桶免忽略」无判据写死

九行块（票 L84-89）语义＝四桶 `.scratch/tickets/` 下**任何**新落件均免忽略、进 git 可见面（探针实证：`!/**/.scratch/tickets/**` 命中豁免，`git check-ignore --no-index -q agent-experts/baigong-software-team/.scratch/tickets/x.md` ＝ exit 1）。裁定意图＝「.scratch＝临时调试落位区」，豁免语义＝留档桶；但 §4.1/§4.2/V 判据族均未写死「tickets 桶内新落件仅限票面」的防线（TMP-DISC §八.3 清理判据管盘面不管 git 面——票 §六 L144 自己点明此镜像关系）。属既定留档桶口径的设计暴露而非机理错，但票面应把「借 tickets 桶落临时物＝违例（纪律面）」或「接受该暴露」写死一条供裁。归候裁/修单面。

## 三、绿项（6·独立证伪存活）

- **绿-1 桶表与分流判据族读数独立复现**：`14416e9` 树 off 口径 `.scratch` tracked＝**136** 恰等；桶表 仓根 37／百工 67（tickets 66）／fuxi 21／EAC 11＝136 ✓；类A 135 ✓；类B 恰 1 件点名 `agent-experts/baigong-software-team/.scratch/COLLAB-STRUCT-1/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md` 复现恰等（该件由 `9f265fe` 落 track）。当轮 HEAD 态 137＝136＋票面自身（`00f7e7d`），符合预期。V6 现跑基线＝1 ✓。
- **绿-2 九行块机理探针全部符合票预期**：本席自建探针（`git -c core.excludesFile=<探针文件>` 覆盖式，真仓 .gitignore 零触碰，diff 空集自证）——V1 三路径 exit 0 且命中行分别＝`/.scratch/*`（仓根）／`/**/.scratch/*`（两包内）逐路径合票钉；V2 三式 exit **1/1/0** 全等；`/**/.scratch/*` 对包内三级目录与仓根双形态覆盖闭合（行4-only 探针实证 `/**/` 在 gitignore 中确匹配零或多级＝票 L92 行义注记不实反为真，行5 系体例冗余行·无害）；`__pycache__` 交互＝`.scratch/tickets/__pycache__/x.pyc` exit 0 命中 `.gitignore` L65 `__pycache__/`（票 §4.1 L94 断言成立，前提＝插入位在 L65 之前的选位，票 §4.1 选位依据在册）。
- **绿-3 §2.3 机理三写实复跑成立**：tracked 类B件现行 `check-ignore` 缺省 exit 1／探针块叠加后缺省仍 exit 1（index 挡回）／`--no-index` exit 0 命中块行——「已跟踪不受忽略管辖」机理正确；`share/check-entity.py` L177 显式剪 `.scratch`、`share/check-pointers.py` L188-201 后缀索引除外 `.scratch/` 族（D-94 注记行实读在位）、`share/check-ticket-reconcile.py` L332 缺省票目录双候选 `.scratch/tickets`——门禁不经 git 忽略面读数，落地零行为差异成立；share 脚本族零 `rg` 调用复查无命中。
- **绿-4 FUXI 封印判据不翻面独立核毕**：判据源直读 `adc4dc3` 笔落件 `agent-skills/fuxi-skill/.collab/qa/2026-11-10-FUXI-FX-U37-QA独立验证-v1.md` L25（判据 2 段内语料落位口径行）＝「`git check-ignore` 对 rb8-suppl 路文件 exit 0」——票 §4.3-1 引述忠实、编号对位（该件判据 2＝封印链工序，L21-25）。本席现跑：`agent-skills/fuxi-skill/.collab/evidence/corpus/rb8-suppl` 在场；`git check-ignore -v` ＝ exit 0 命中 `.gitignore:20:/**/.collab/evidence/`；探针块叠加后复跑仍 exit 0 命中行不变＝插入 L54 后不翻面成立。`gitignore:20` 引用在 FUXI 票面实文核实（`agent-skills/fuxi-skill/.collab/tickets/2026-11-06-FUXI-FX-U2-证据归位与封印票-v1.md` L22「禁动 gitignore」句同文在位——票 §六 L142「FX-U2 辖 FUXI 案自身」读法与原文相容）。
- **绿-5 T9 正交性与行号锚保护成立**：`agent-experts/baigong-software-team/skills/sop/templates/ticket-template.md` 档位3＝L96、封口条款＝L103（票引 L93-L103 区间对位）；档位3 管措辞违例豁免、gitignore 管可见性——正交判读成立，忽略规则不使档位3/封口条款失效。`.gitignore` 全文 66 行（wc 实测）、L17＝制②节头、L20＝evidence 行现读全等；插入位（L54 `REFERENCE-SOURCES.md` 配套负向行后空行处、L56 节头前）保 L1-L54 行号零移动，V8 `git diff` 删 0 增 9＋`sed -n '17p;20p'` 对拍形态机械可跑。
- **绿-6 历史留档语义论证自洽＋落链笔合规**：仓根 tickets 桶 38 件 tracked＝历史留档票据面（票 §三 L64「不能一刀切」）；方案甲/乙代价对照（§4.0）与候裁(d) 归属划界清晰，产品取舍归候裁不归本席改判；`00f7e7d` 笔面恰一件、`collab:` 前缀、message 零 at 符号字符（用字样）形态合规。

## 四、V0-V8 判据可机械跑性三态评

| 判据 | 三态 | 实测注 |
|---|---|---|
| V0 | 照字面可跑 | date/HEAD/tracked 面三式现跑 ✓；类B 复点式 off 口径现跑＝1 ✓（该式 NUL 原始口径，不受 quotepath 陷阱——红-1 陷阱恰不在 V0 而在 §一 复点①） |
| V1 | 照字面可跑 | 探针态三路径 exit 0＋命中行钉值逐路径合（新块插后行号 L56-L64 段，回执在册要求合理） |
| V2 | 照字面可跑 | exit 1/1/0 全等复现 |
| V3 | 缺钉值（第二式） | 第一式→0 探针实证成立（目录级/文件级均复现 0，含嵌套镜像内 tickets 文件不借豁免还魂——探针 exit 0 复核）；第二式「基线减 199」之「基线」未定义（V0 三读数不含全仓 ?? 基线），且 199 现轮漂至 201（黄-1） |
| V4 | 照字面可跑（附注） | 缺省 exit 1 复现 ✓；`git grep -- '*/.scratch/tickets/*'` pathspec 的 `*` 不跨 `/`＝不含仓根 tickets 桶（现轮该式命中 5 枚，无 pathspec 全仓 24 枚）——判据为前后全等对拍仍成立，覆盖面注记随修 |
| V5 | 照字面可跑 | exit 0＋命中行不变＋`grep -n` 行号仍 20 现跑合 |
| V6 | 照字面可跑 | 基线 1 现跑 ✓（off 口径） |
| V7 | 缺钉值＋不可照字面跑 | reconcile 缺省式 exit 2（黄-4）；GATE PASS 发现数无基线钉（本席参照值 150138）；check-pointers 靶检式现跑 exit 0 ✓ |
| V8 | 照字面可跑 | 形态机械成立（§五 L138） |

## 五、口径分账与观察登记（不判红）

- 默认 quotepath vs off 双口径在 `ls-files`/`ls-tree` 面差 28 枚（.scratch 族 CJK 名件）；status 面目录级行多数不转义故票 ?? 读数基本可用——本审全部计数以 off＋NUL 双验为准，票内读数按上节分账。
- README L22 现文「仓根 `.scratch/tickets/` 仅存 B 批过渡票」相对现盘 38 件已陈旧——票候裁(g) 已列随动面，照登。
- 类C 消隐观察：两枚姊妹仓镜像目录（`.scratch/multi-agent-collab-experts`／`.scratch/multi-agent-collab-skills`）在场＝票 O-2 登记属实；探针态 ?? 全仓 210→9（散件面存续）符合类C 零 git 动作预期。
- 票面自注落位悖论（L11）自洽：票面自身落 tickets 桶＝豁免行覆盖，与规则族不冲突。

## 六、收口

- 判定汇总：**红 1／黄 5／绿 6**；V0-V8：照字面可跑 6、有歧义／缺钉值 2（V3、V7）。
- 红黄项均归作者席修单／候裁面处置，本席不改判产品取舍（候裁 a-g 七条本体不在 QA 射程）。
- 探针纪律自证：临时复测物居仓根 `.scratch/qa-scratchrev/`（九行块探针文件＋门禁输出重定向），commit 后删除；`git diff --stat -- .gitignore` 全程空集＝真仓忽略文件零触碰；本审件外零改动；完工删除读数随回报呈主理人。
