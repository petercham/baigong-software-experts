# REPO-RESTRUCT · 仓重整输入件 v1（全仓盘点账＋硬编码依赖清单＋结构决策点＋批次建议）·架构席起草

- 起草实测 HEAD：`ff72b92`（`git rev-parse --short HEAD`·工作仓 `D:\multi-agent-collab-devkits`·main）；开工 ANCHOR 读数＝`ff72b92`（本件开端笔即为该 HEAD 之后首笔）。
- 件型＝**重整输入件**（不是施工票）。依据＝裁定件 `.collab/decisions/2026-11-03-皮总裁定-工程师写域规范与仓根项目子包分层.md`（commit `ff72b92`·覆盖同日 15:5x `7a2bb62` 分层裁定）裁定二.4：项目子包命名与文件结构＝人类＋主理人协调定义；架构席出的是**机械迁移与门禁随动的施工票**，不代设计项目结构——而施工票的前置＝结构已定。本件＝该前置的输入账。
- 15:5x 方案（docs／.collab 下设 `{target_project_id}` 子包）骨架**作废**，本件按裁定二「仓根顶层先分项目子包」口径重拟；旧骨架未曾落盘（起草中断于取证阶段，盘上无旧件需替换——`git status --porcelain` 起草前实测读数见 §六回执节）。
- 计数口径声明：本件全部计数＝occurrence 口径（`grep -o … | wc -l`／`git ls-files | wc -l`／逐项 python 计数），判据命令一律自带落盘重定向；负例一律 exit≠0 断言。
- 行号口径：起草实测现盘物理行号（锚 HEAD=`ff72b92`）；后续复测若位移，以本件逐字文本锚定位为准（SWB-SOP-R1 落位程序条款同款）。
- 只读取证声明：本件全部判定附文件＋行号或命令读数；起草过程零落改交付面（闭集＝本件一件）。

## 声明闭集（1 件·本笔唯一可写面）
- 声明闭集：
- .collab/design/2026-11-03-repo-restructure-input-inventory-v1.md

---

## 一、现仓全量盘点账（顶层逐个：现落点／性质／tracked 账／目标子包候选／迁移风险）

### 1.0 仓根顶层实测清单（起草实测 `ls -a`＋`git ls-files` 双账）

| 顶层项 | 性质 | git tracked | 体量（实测） | 目标子包候选（§三 D1/D2 未裁前＝候选非终态） | 迁移风险 |
|---|---|---|---|---|---|
| `README.md` | 仓根索引（治理约定＋目录结构表） | ✅1 件 | 目录结构表 L12–18 现描述 `deliverables/{对象名}/`、`docs/`、`.collab/*` 三层 | 仓根留一份新仓根 README（项目子包索引）；旧文入史述 | **高**：L12–18 表＋L28–30 索引路由条款＝仓根目录定义真源，重组后整表重写；行文内姊妹仓/远端段零迁移 |
| `.gitignore` | 仓级排除声明 | ✅1 件 | 56 行；`.collab/*` 系条款 12 处（L6,9,13,17,24,27,30,33,37–39,42–44） | 仓级保留一份＋各项目子包内自带同构 gitignore（候选） | **高**：全部 `.collab/` 前缀条款随子包搬家逐条重写；`!.collab/research/` 负向防御条款（L13,42–44）需同形随动 |
| `deliverables/` | **交付面** | ✅203 件（含带引号路径 3 件＝CJK 文件名口径） | `skills/` 六包＝bundle-assembly-registration 6＋external-advisor-collab 7＋fuxi-skill 37＋multi-collab 10＋object-audit 40＋object-build 9；`experts/baigong-software-team` 93 件；`README.md` 1 | 候选＝按项目拆：百工软开团专家包一项目子包；六个 skills 包各自或分组（§三 D2 待裁）；`deliverables/README.md` 索引随拆随写 | **最高**：203 件全量搬家＋§二硬编码依赖清单全线随动（门禁扫描根、bundle.lock path、spec-provenance 锚全部牵动） |
| `docs/` | 规范文档面 | ✅8 件 | README 1＋process 1＋research 6 | 候选＝随所属项目子包内 `docs/`（裁定一.3 写域口径下 docs＝项目根唯二排除之一）；跨项目共享研究底稿归属＝§三 D3 | **中**：体量小；但 seat-permissions「docs 转正代写/`.archive` 落位」通道条款与 promote-manifest 语义牵动 |
| `.collab/` | 过程域＋治理史实锚混合 | ✅557 件 | tickets 83／qa 146(＋2 未tracked)／receipts 48／decisions 12／design 16／research 242／board 1／evidence 2(文件域 3507)／refs 0 tracked(文件域 8835)／根文件 7（FUXI 收口报告 5＋冻结入账补录 1＋SWB 票包遗留呈报 1）／dispatch 0 tracked(10 文件)／inbox·process 0 tracked | 候选＝**每项目子包内自带统一治理结构**（裁定二.2「各子包内自带其治理结构，规范统一不分叉」）＝`{project}/.collab/{tickets,qa,receipts,decisions,...}`；跨项目仓级治理史（`decisions/` 裁决记录·拍板史）归属＝§三 D3 **重点待裁** | **最高**：557 tracked＋约 12,400 文件系统文件（refs 8835＋evidence 3507 两个未入库大块）；SWB 票包在途（T07/T08 未施工、双席审票在途）——票内互锁见 §四批次 B4 |
| `tools/` | 仓级门禁工具（非交付包） | ✅7 件 | check-source-of-truth.py／check-truename.py／count_agent_tokens.py／baseline-seat-decl.json／baseline-sot-dup.json／check-truename-names.txt／sot-external-provenance.txt（＋`__pycache__/` 不入库） | 候选＝仓级共享工具区一份 vs 随项目走（§三 D4 待裁）；`check-source-of-truth.py` 现硬编码软开 bundle 路径（§二 G10） | **中**：7 件小体量，但其扫描配置与基线快照内嵌旧路径，搬家即换锚 |
| `.genie` 外围 | — | 不入库 | **实测不存在**：仓根无 `.genie*` 条目（`ls -a` 全量＝上表八项＋`.git`＋`.workbuddy`）；仓内 `find -maxdepth 2 -name "*.genie"`＝0 | 无需处置 | 零（登记实测读数，防主理人转述口径与本仓实证不符） |
| `.workbuddy/` | 会话工具产物 | ❌（gitignore L52） | 存在但排除 | 不迁移 | 零 |

> 仓根文件级补充实测：`.collab/tmp-w7-msg.txt`（gitignore L30 排除）在盘＝.collab 根无归属临时件先例，重组时按同判据处置。

### 1.1 `.collab/` 过程域按项目线归槽预分类（文件名前缀机械账·起草实测）

分桶口径＝基名模式匹配（`*SWB*|*TKT*`→SWB 线；`*FUXI*`→FUXI 线；`*EAC*|*外部顾问*`→EAC 线；`ENG-*/QA-*/ARCH-*/MC-*/GH-*/*SOP*/*软开团*/DIRRELOC/*GATE1*/…`→百工软开团 SOP 线；余＝余量待人工分账）。tracked 件读数：

| 域 | SWB 线 | FUXI 线 | EAC 线 | 软开团 SOP 线 | 余量待裁 | 小计 |
|---|---|---|---|---|---|---|
| tickets | 27 | 21 | 11 | 20 | 4 | 83 |
| qa | 52 | 22 | 2 | 28 | 42＋2 未tracked | 146＋2 |
| receipts | 21 | 0 | 0 | 3 | 24 | 48 |
| design | 0 | 9 | 0 | 1 | 6 | 16 |
| board | 0 | 0 | 0 | 0 | 1 | 1 |
| 小计 | 100 | 52 | 13 | 52 | 77 | 294＋2 |

- 余量 77 件＝文件名不含项目 token 的历史案卷（如 `2026-10-22-裁决记录` 系、裸叙事回执），**逐件人工分账属施工批前置**；本件给出机械预分类读数＋分桶正则，不代裁归属。
- `decisions/`（12 tracked）＝跨项目治理史实锚，**不按上述前缀拆**——归属＝§三 D3。
- `research/`（242 tracked）＝跨项目研究底稿，同上＝§三 D3。
- 未入库大块（`refs/` 8835 文件·`.gitignore:33` 整段排除；`evidence/` 3507 文件·L17 排除；`dispatch/` 10·L27；`inbox/` 9·L9；`process/` 0·L6）＝**文件系统迁移面**（非 git mv 面），批次 B3 单独处置。

### 1.2 正式登记件滞留账（触因账·随裁定延续）

- 正式基线 v2.9 现落 `.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md`（tracked=0·被 `.gitignore:33` 排除·实测 `git check-ignore -v` 命中该条款；`wc -l`＝259＝260 行无尾换行，与票包「260 物理行」口径一致）。
- 全仓对该件的路径字符串引用（occurrence 口径·仓内排除 refs 自身）＝**23 处/19 文件**：tickets 12 文件 16 处（TKT40 独占 5）＋receipts 4＋qa 1＋**交付面 2**（`deliverables/experts/baigong-software-team/skills/sop/references/{product,architecture}-v2.9-copy.md` 各 L1 来源注）。
- 该件哈希锚定三值（票包引用基线·全文 `3f335333…`／产品段 `7214ad14…`／架构段 `efb4f765…`）**与文件路径无关**——搬家不断哈希锚，只断路径串与物理行号锚（V13 n＝物理 n−28 恒等式随头块走，搬家不改头块则不断）。此读数供 §三 D5 锚定方式候裁引用。

### 1.3 `deliverables/` 交付面性质细分（重组候选的原料）

| 包 | tracked | 性质 | 与谁耦合（实测） |
|---|---|---|---|
| `experts/baigong-software-team` | 93 | 专家团 bundle（核心项目交付物） | bundle.lock L7 `"path": "deliverables/experts/baigong-software-team"`；hooks 运行面脚本（§二 G5–G9）；`skills/sop/references/{product,architecture}-v2.9-copy.md` 基线副本；`skills/sop/scripts/run-gates` 消费面 |
| `skills/object-audit` | 40 | 门禁引擎（跨项目通用工具包） | run-gates.sh 为 pre-commit 入口；install-hooks.sh 把 `.git/hooks` 指向本包（相对脚本自身位置解析，包体搬家自咬低风险，**引用它的路径**随动面在 README/hooks 文档） |
| `skills/multi-collab` | 10 | 协作规范包（含 60-gates 路由真源） | run-gates.sh/install-hooks.sh 头部 spec-provenance `spec_file: deliverables/multi-collab/references/60-gates.md`（L4,13,22／L4）；check-* 六件退出码闭集条款同锚 |
| `skills/external-advisor-collab` | 7 | 外部顾问协作包 | check-pointer-closure.py L77 DEFAULT_PKG_FACES 硬编码本包路径 |
| `skills/fuxi-skill` | 37 | FUXI 项目交付物（项目线独立） | `products/` 内迁史（DIRRELOC C2） |
| `skills/object-audit+object-build+bundle-assembly-registration` | 40+9+6 | 通用对象工具链 | object-build/publish.py 内 `.collab/decisions|evidence` 路径引用（L456,462,411） |

## 二、门禁与脚本旧路径硬编码依赖清单（逐条文件＋行号·起草实测）

> 口径：只列**现行活引用**（脚本运行时解析/扫描根/配置字面/注册字面）；史述句与票面包裹路径不入本清单（分账先例＝T07-B 甲乙丙三分账）。行号锚 HEAD=`ff72b92`。

| # | 文件 | 行号 | 硬编码内容 | 重组牵动 |
|---|---|---|---|---|
| G1 | `deliverables/skills/object-audit/scripts/check-pointers.py` | L74 | `DEFAULT_SCOPE = ("deliverables",)` | 仓根顶层若分项目子包，默认扫描根失配＝门禁哑火或全悬空 |
| G2 | 同上 | L120,319–324,380–383 | 仓根定位探针 `os.path.isdir(os.path.join(cur,"deliverables"))`；`pkg_bases = [deliverables, deliverables/skills]` 双域枚举 | 根探针认不出新树＝infra error exit 4 族 |
| G3 | 同上 | L218,220 | 指针解析候选 `root/deliverables/rel`、`root/deliverables/skills/rel` | 跨包短写法指针全部改道 |
| G4 | 同上 | L5,14,23 | spec-provenance `spec_file: deliverables/object-audit/references/50-document.md`、`deliverables/object-build/references/50-directory.md` | 头块锚随路径改＋clause_sha256 不变（锚＝条款文本非路径，provenance 复核仅改 spec_file 行） |
| G5 | `.../scripts/check-ticket-reconcile.py` | L101,317,526–527,542,551 | `COLLAB_PREFIX = "." + "collab" + "/"`；缺省票目录 `.collab/tickets` | 票目录改 `{project}/.collab/tickets` 后缺省扫描面落空＝对账哑火（exit 0 假绿，**危险形态**） |
| G6 | `.../scripts/check-pointer-closure.py` | L63,77 | P1 形态正则 `\.collab/`；`DEFAULT_PKG_FACES = ("deliverables/skills/external-advisor-collab", "deliverables/experts")` | 两包面字面随新树重写 |
| G7 | `.../scripts/run-gates.sh` | L4,13,22,137 | spec 锚 `deliverables/multi-collab/references/60-gates.md`×3＋SCRIPTS 清单（含 `ROOT/tools/check-source-of-truth` 仓根 tools 字面） | 60-gates 搬家→三 spec 锚重写；tools 归属裁后 SCRIPTS 行随动 |
| G8 | `.../scripts/check-collab-lint.py` | L5,14,23 | spec 锚 `agent-skills/external-advisor-collab/.scratch/tickets/2026-10-30-EAC-SK5-机检票.md`（**锚在 .collab 过程域**） | EAC 案卷迁 `{project}/.scratch/tickets/` 后 spec_file 行重写 |
| G9 | `.../scripts/install-hooks.sh` | L4,73,85 | spec 锚 60-gates；`RUNNER="$SELF_DIR/run-gates.sh"`（相对自身＝搬家自洽）；注释路标行 | 仅注释/spec 随动，机制面低风险 |
| G10 | `tools/check-source-of-truth.py` | L41–45,104–107 | spec 锚 handoff-discipline 路径；用法注释 `--pkg deliverables/experts/baigong-software-team` | bundle 搬家→注释用法＋调用方（run-gates 调用参数）随动 |
| G11 | `deliverables/experts/baigong-software-team/bundle.lock` | L7 | `"path": "deliverables/experts/baigong-software-team"` | 注册字面随新树重写（纪律④产物不可手改→须经装配口径 bump） |
| G12 | `.../config/seat-permissions.json` | L7,13,22,24,25,31,33,34,40,42,43,49,51,52,59 | 全部席位 write/deny_globs＝仓根相对字面（`.collab/…`／`docs/**`／`deliverables/**`／`tests/**`） | 裁定一口径（项目根∪交付路径可写·唯二排除项目根 `.collab`/`docs`）＝表语义重写；且路径锚定语义随「仓根」→「项目根」换代 |
| G13 | `.../config/seat-permissions-hooks-map.json` | L7,12,16,20,24,28–29 | deny_globs 仓根字面＋路径锚定注记「读作仓根字面」 | 同 G12 换代；hooks 安装面（平台 settings）路径同步 |
| G14 | `.../skills/sop/scripts/ledger-init.sh` | L15 | `LEDGER_ROOT="${SWB_LEDGER_ROOT:-$PWD/.collab/ledger}"` | 账本根随项目根走 |
| G15 | `.../skills/sop/scripts/shadow-replay.py` | L39,43,124,163 | 白名单正则 `\.collab/(ledger|decisions|tickets|receipts|refs|manifest|human)/`；PROCESS_ARCHIVE_DIRS 四串；`.collab/` 排除判定 | 白名单正则随子包路径形态改（`.collab/` 中段匹配可保形，前缀加项目层则需扩形） |
| G16 | `.../skills/sop/scripts/commit-audit.py` | L35 | 票 ID 正则 `\.scratch/tickets/[^\s"']+` | 票路径形态改→正则随动 |
| G17 | `.../skills/sop/scripts/write-guard.py` | L283 | 哨兵路径 `.collab/liveness/sentinel-write` | 随项目根 |
| G18 | `.../skills/sop/scripts/sign-verify.py`／`promote-manifest.py` | L5,6,14,105／L7 | `.collab/signatures/`／`.collab/human/reviews/`／`.collab/manifest/` 语义注释＋入参形态注释 | 注释与缺省形态随动 |
| G19 | `.gitignore` | L6,9,13,17,24,27,30,33,37–39,42–44 | `.collab/*` 系 12 条款＋`!.collab/research/` 负向防御 | 全表按新树重写（两制区分先例保留：判词进 git／流水不进） |
| G20 | `README.md`（仓根） | L12–18,28–30 | 三层目录结构表＝仓根组织真源定义；索引路由条款 | 整表重写为新仓根树；条款随 §三 裁定形制 |
| G21 | `deliverables/README.md` | L4 | 索引行 `deliverables/experts/baigong-software-team` | 随拆随写 |
| G22 | `deliverables/skills/object-build/scripts/publish.py` | L411,456,462,675 | `.collab/evidence`／`.collab/decisions` 落盘目标字面 | 发布通道路径随项目根 |
| G23 | `deliverables/skills/multi-collab/SKILL.md`／`references/90-changelog.md`／`references/60-gates.md` | 47／14,20,29／156 | `.collab/` 规范叙述面 | 规范叙述随新树口径改（泛化规范面 vs 仓级实例分账见红线节） |

**交叉硬数字（供决策点引用）**：§二清单合计 **23 条目／约 60 个行级锚**；其中交付包内运行时脚本 8 件、配置文件 2 件、门禁脚本 5 件、仓级工具 1 件、gitignore/README 2 件、规范叙述面 3 件。

## 三、需人类＋主理人定夺的结构决策点清单（架构席不自行拍·全部单列）

| # | 决策点 | 两案（利弊） | 架构席技术注记（只供裁，不裁） |
|---|---|---|---|
| D1 | **项目子包命名名录**（仓根顶层目录名闭集） | 候选槽（按现盘项目线）：百工软开团专家包／SWB 案项目／FUXI／external-advisor-collab／multi-collab／object-audit／object-build／bundle-assembly-registration／仓级共享区（decisions 史）——命名风格（kebab-case ASCII·现 README L33 命名约定） | 名录与粒度＝人类＋主理人协调定义（裁定二.4）；架构席只保证**名录一定，映射表即机械可展开** |
| D2 | **六 skills 包＋专家 bundle 归属切分**：每包各立项目子包 vs 分组共享子包 vs 「工具类留仓级共享区」 | 各立＝治理彻底但 93+109 件全散；分组＝object-audit/object-build/bundle-assembly-registration 三通用工具一包、multi-collab/external-advisor-collab 两规范包一包、fuxi/baigong 各独立 | 耦合实测：object-audit 门禁被全仓消费（G1–G9），若其入某项目子包，其余项目的门禁调用路径全改；若留仓级，＝「仓级共享工具区」是否算项目子包之外的例外顶层（破分层纯度）需裁 |
| D3 | **跨项目治理史与共享研究底稿归属**：`decisions/`（12）＋`research/`（242）留仓级 `.collab/` vs 打散入项目子包 | 留仓级＝治理史单一连续可查，但仓根出现「无项目」顶层例外；打散＝分层纯度，但跨项目裁决（如本裁定、裁决记录·2026-10-22 系）无家可归 | 裁定二.2 说各子包内自带统一治理结构——**跨子包裁决落点**裁定件未覆盖＝真空点，呈请补裁 |
| D4 | **`tools/` 归属**：仓级共享 vs 随项目走 | 同 D2 逻辑；check-source-of-truth 现专配软开 bundle（G10），baseline-*.json 系 bundle 基线快照 | 基线快照再生开关（`--regen-*`）内嵌路径，随归属换锚 |
| D5 | **票包锚定方式是否同批改**（V13 物理行号锚→条款号/哈希段锚） | 改＝一次转换成本（现盘 SWB 在途票包 V13 L 锚 occurrence＝T01..T06+总览 94＋TKT40 100＋TKT41 13＋T08 1＝**约 208 处**）后续零搬家；不改＝本次迁移登记件若改头块则再搬一次 | 实测读数：登记件哈希三值与路径无关（§1.2）；若登记件**整体 git mv 不动内容**，V13 恒等式（n＝物理 n−28）不破坏——**不改内容则行号锚不碎**，碎的是 23 处路径串（G 清单外另 19 文件）。利弊核心＝「挪文件不挪内容」可行性 |
| D6 | **git 历史口径**：`git mv` 全量保留历史 vs 重放式新树＋旧树归档 tag | mv＝历史连续（rename 检测·DIRRELOC C1 先例）；重放＝干净但断账（414+143 tracked 件史不可 bisect） | 体量实测：tracked 总量 765（含 CJK 引号路径 10 件口径）；rename 检测对 765 件批量 mv 无已知障碍（DIRRELOC 先例仅 25 件，量级差 30 倍需预演） |
| D7 | **登记件 v2.9 入库口径**：迁入后落点（SWB 项目子包内 `docs/`？）＋`.gitignore:33` 存废（外部引擎快照 8835 文件仍宜排除·正式登记件宜入库＝两制区分） | 整条款废＋白名单负向规则（先例 L13/L42–44 形态）vs 条款改窄到 `refs/engine-snapshots*/` | 触因账＝§1.2；皮总 15:47「正式基线无正式落点」指认在新分层下的承接落点需随 D1 一并裁 |
| D8 | **写域配置项目化承载**（裁定一.3）：每项目 `docs/` 内专文定义写域配置（规范级）＋seat-permissions.json 作数据面随项目走 | 与 SWB-T08 在途票对表：T08 engineer 行机械化现值 `deliverables/**` 已被裁定一覆盖→**T08 修正批**须按「项目根∪部署路径−{.collab,docs}」重拟 | 本件不重开 T08（生产权随作者席流程：审票回来由起草席修正）；此处仅登记依赖关系＝重组批 G12/G13 与 T08 修正批同域，**先后序需主理人排** |
| D9 | **统一治理结构的最小集**：每项目子包内 `.collab/` 子域闭集（tickets/qa/receipts/decisions/…哪些必配、哪些选配）＋`.gitignore` 是否每子包一份 | 必集全配＝规范统一；选配＝轻量项目省层 | 「规范不分叉」＝必集闭集需定义；此定义本身属泛化规范面还是仓级实例，呈请明确（红线见 §五） |

## 四、迁移批次划分建议（可机械验证切分·每批自带对账判据骨架）

> 总纪律（沿用 DIRRELOC 先例）：每批独立 commit＋笔笔过闸；每批「迁移前读数→迁移后读数」对账；未入库面与 tracked 面分账；在途票包互锁。

- **B0 决策冻结批（零文件动作）**：D1–D9 裁毕→映射表终态落 `.collab/design/` 追补笔（append-only 修订注记）。判据：决策点九项各含皮总/主理人批语读数。
- **B1 仓根骨架批**：建项目子包空壳（各 README＋gitignore 形制随 D9）＋仓根 README 新目录表。判据：`git ls-files` 顶层枚举＝裁定终态名录闭集断言（exit≠0 负例＝名录外顶层出现即拒）。
- **B2 交付面 mv 批（tracked 203 件）**：`git mv` 按 D1/D2 终态映射；同笔随动 G1–G11+G21（扫描根/spec 锚/bundle.lock/SCRIPTS 清单）。判据：①迁移前 `git ls-files deliverables/ | wc -l`＝203→迁移后新面读数＝203＋旧面＝0（对账双向清零）；②`run-gates.sh --root .` GATE PASS 前后对拍（先例＝DIRRELOC C1 三笔判据）；③check-pointers 悬空基线零新增（开工首跑落盘对比）。**危险形态点名**：G5 缺省票目录若漏随动＝exit 0 假绿，B2 判据须含「票对账扫描面非空」正断言（现盘应命中 tickets 件数读数>0）。
- **B3 过程域 mv 批（tracked 294＋根 7＋未入库约 12,400 文件）**：`.collab/{tickets,qa,receipts,design,board}` 按 §1.1 分桶＋人工分账终表迁 `{project}/.collab/`；`refs/evidence/dispatch/inbox` 文件系统搬家（不入 git）；`decisions/research` 按 D3 裁处。判据：各桶 tracked 计数前＝后（逐桶对账表）；`git mv` rename 检测率读数（`git log --stat -M` 抽样）；未入库块迁移前后 `find … -type f | wc -l` 相等（refs=8835/evidence=3507 现值）。
- **B4 票包锚定随动批（互锁：排 T07/T08 施工收口之后）**：登记件按 D7 落点＋D5 锚定方式终态，23 处路径串（19 文件）随动；SWB 在途票 T07/T08 票面 ANCHOR 条款追加修订注记（append-only）。判据：旧路径串 occurrence 23→0（负例＝残留即 exit≠0）；新串 occurrence＝23；三哈希逐字不变断言。
- **B5 收尾批**：`.gitignore` 全表重写（G19）＋仓根/各 README 索引换代（G20/G21）＋seat-permissions 面按 D8 序与 T08 修正批对表＋`tools/` 按 D4 归位。判据：`git check-ignore` 抽查矩阵（判词件=不ignore／流水=ignore 逐形态 exit 码断言）。

**批次依赖链**：B0→B1→B2→B3→B5；B4 双前置＝B0＋（T07/T08 施工收口），可与 B2/B3 并行准备、串行落笔（裁定 §三 排程同款）。

## 五、红线与边界（本件自设）

- 本件＝输入件：**未落改任何交付面/治理面文件**（闭集 1 件）；「目标候选」列全部标注候选非终态，不构成结构裁量。
- 泛化规范面零触碰红线延续：席位卡、随包技能（software-orchestration 等）、`deliverables/skills/` 规范正文在**结构未裁前**一字不动；G23 所列规范叙述面随动属后续施工批且需区分「仓级实例描述」vs「泛化条款」（后者不入重组面）。
- 本件不自判合格；决策点闭集九项全部待裁，任何一项未裁即开工 B1＝程序违例。

## 六、回执（起草笔）

- 开端 HEAD 实测＝`ff72b92`；起草前 `git status --porcelain`＝2 行（均 `?? .collab/qa/2026-11-01-TKT-双席审计过程件汇总-v1.md`／`?? .collab/qa/2026-11-01-TKT-最终分票件全文汇编-v1.md`＝他席未入库过程件，登记不处置）。
- 交付笔＝本笔单独 commit（`collab:` 前缀·只含声明闭集 1 件）；禁 `--no-verify`、禁 amend；pre-commit 门禁真拦时如实报告拦点，不绕闸。
- 本件 commit 后读数随后笔/回执追加（append-only）。
