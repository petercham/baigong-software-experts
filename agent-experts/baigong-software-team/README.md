# Baigong Software Team（百工软件团队）

百工软件团队专家团：项目负责人统筹产品经理、架构工程师、开发工程师、质量审计师四席，按固定 SOP 把需求推到可验收交付，每步留证据与判定级别。

## 类型

Team 型（多角色协作团队）

## 功能

- **5 席位 SOP 协作**：主理人（项目负责人·包好用）＋产品经理（姜通透）＋架构工程师（顾长远）＋开发工程师（柯会码）＋质量审计师（沈得严）
- **工作流路由**：主理人收到请求先判断档位（标准 SOP／维护票／部分工作流／增量开发），再定席位编排与推进顺序
- **可审计交付**：需求→设计→拆票→执行→发布→灰度六节点全程留痕；账本为唯一真相，租约写侧校验与机械门禁执法，产品席＋QA席独立复审（生成方不自判），执行期一票活跃

## 使用示例

- 我有一个开发需求，请按标准流程走一遍：出 PRD、出设计、拆票、串行执行、独立验收，每步留判定证据。
- 这份设计／交付请做独立复审：按三态覆盖矩阵逐项给结论，列出必补项——生成方不自判，终裁归我。

## 出身

本专家包为**市场包 fork 自维护**：

- **基线**＝WorkBuddy 专家中心市场包 `software-company` **v1.1.0**（下载戳 **2026-10-09**，宿主插件缓存内该包 1.1.0 目录 mtime 实测）。
- **fork 后本地改动清单**（除以下三项外，五席 MD 逐字照录市场版，零改写）：
  1. **plugin.json 形态适配**：市场版仅 7 键、过不了注册校验（缺 displayName），改用 my-experts 注册形态 18 键（注册适配层，非席位定义层改动）；
  2. **lead 改名**：文件名 `software-team-lead.md`→`software-company-team-lead.md`，内容仅 frontmatter `name:` 一行同步（Q3 拍定差，diff 市场版＝仅此一处）；
  3. **版本升 1.1.1**（Q5 拍定）：版本号变更逼宿主刷新运行缓存，规避「同版本号免刷新」漂移。
- **上游关系**：fork 自维护，上游后续版本不自动追；需要时人工 diff 市场缓存对账一次（版本账即本节）。
- **版本账 v1.3.0**（2026-10-28）：软开 bundle 由「无装配环节·真源直拷」改「有装配环节」——新建包内 `bundle.lock`（组件 `external-advisor-collab`·同仓 `repo:"."`·锁不可变 tag `external-advisor-collab@v1.0`·target `skills/external-advisor-collab`）；plugin.json `skills[]` 加 `./skills/external-advisor-collab`。依据＝皮总（2026-10-28）口径「分仓＝维护/分发维度，部署到 WorkBuddy＝把相关 skills 装配进专家团」——真源仍在 `deliverables/skills/external-advisor-collab` 不出池（拍板五①不违反），装配产物＝仓外 `-build` 预览面＝派生产物非第二真源（纪律③）；lead 讨论会兼任节「加载技能 external-advisor-collab」自此命中包内装配件＝部署态自包含（D 项收口，撤销 10-27「挂指针＋fail-closed」候拍方案）。版本升 **1.3.0**（分发结构变化＝minor，皮总「开」）。同批：deploy-gate.md §四 补「本门不禁止装配」校准行。预览先行（§五）：产物只落仓外同级 `<仓>-build/<bundle>` 缺省装配面，进部署面候皮总真实验证后独立指示。
- **版本账 v1.3.3**（2026-10-28）：`bundle.lock` components 增跨仓组件行 `deep-research`（repo `../multi-agent-collab-skills`·roottag `skills`·锁不可变 tag `deep-research@v1.0`·target `skills/deep-research`）——新技能 deep-research 真源在 skills 仓（MIT 派生 fork 登记见该技能 README·票 T-deepresearch-01）。**仅组件新增＋平台刷新载体（宿主缓存按包版本刷新），席位与编排零变化**（解耦纪律 R-6：本次例外经皮总授权打 patch——新技能自动路由实际改变团内调研行为；调研起手式自动路由＝靠技能 description 触发词工程化，不动席位）。plugin.json＋bundle.lock 双 1.3.3。同批回修（票 T-deepresearch-02·QA-deepresearch-01 判词收口）：组件 `deep-research` 锁 tag v1.0→v1.0.1（QA minor-a/b/c 收口·skills 仓新不可变 tag·旧 tag v1.0 保留）＋plugin.json `skills[]` 补登 `./skills/deep-research` 提交入库（QA major-1 收口·一行注册行·随同票 commit 入库）。
- **版本账 v1.3.2**（2026-10-28）：`deploy-gate.md` §五 由「预览先行」升格为**四段部署流程**成文（皮总定口径「装配→预览→人类闸→部署」·四段闸口链·禁跳段）。要点：预览的成文抓手＝复制本地市场源＋宿主注册命令挂预览卡（宿主工具链提供，非 `-build` 目录本身）；人类闸不可由代理代跑；获批范围按段界定。SKILL.md 索引行/description/触发词同步，技能版本 1.0.1→1.0.2；plugin.json＋bundle.lock 双 1.3.2。
- **版本账 v1.3.1**（2026-10-28）：补齐 `avatars/` 六件（五席位＋team）——此前仅 `.gitkeep`、图片从未入库（fork 遗留缺口，官方规范要求 512×512 PNG）。样式＝纯色异色底＋白色姓氏大字＋职业名小字：齐＝深蓝／许＝青绿／高＝紫／寇＝琥珀／严＝砖红，五色互不相同（皮总拍「头像用姓可以，背景色必须区分开」）；team＝深板岩底＋五色姓氏方块。版本升 1.3.1。同批补正：`bundle.lock` bundle 版本行 1.3.0→1.3.1（该行为 plugin.json version 的同源镜像·纪律①每变必 bump——v1.2.x 各 bump 批无 lock 行属先行态，v1.3.0 起此行为 bump 必改项）。

- **版本账 v2.0.0**（2026-10-29·票 T-team-rename-01·皮总拍板㉑）：两团全层改名——包 id 更名 `hjh-software-team`→`baigong-software-team`（bundle 目录 git mv·`.gitignore:22` 注释活引用随行）；中文显示名「软件开发团队」→「百工软件团队」（拍板⑰⑲）；英文显示名「Software Company」→「Baigong Software Team」（拍板⑳ A3 案）；plugin.json name/plugin/displayName/profession/description＋lead MD :3/:6/:9＋四席位 MD:8 英文自述＋software-orchestration SKILL:3（1.0.2→1.0.3）随行；external-advisor-collab 组件 10-roles :25/:48 改＋:49 豁免注＋@v1.0.1 换 ref（devkits 同批 commit）。**id 更名升 major＝拍板⑳口径，覆前例**（v1.2.0 前例按破坏性升 minor 记账）。〔本行版本号 2.0.0 已被拍板㊷覆盖：id 更名＝身份切割不续旧序列，见下行〕
- **版本账 v0.1.0**（2026-10-29·皮总拍板㊷·覆盖上行 2.0.0 口径）：百工与旧团（hjh-* 血脉 v1.0.0–v1.3.3＋2.0.0 记账）**做身份切割，版本号重新起算**；皮总定 **0.1.0** 而非 1.0.0——理由原话「起码的头像生成都还没做过，而且暂时没有计划做，先不认为是正式可用版」（avatars/ 现存六件＝旧团 v1.3.1 时代产物随目录平移，百工身份未生成过任何资产）。plugin.json version 与 bundle.lock 版本行同源改 0.1.0；软件编排技能 1.0.3 为组件自身版本不受影响。旧序列 v1.0.0–v1.3.3 各账行转**前血脉沿革**（留档不续账）。
- **版本账 v0.1.1**（2026-10-30·2026-10-29a 案技能升级批联动）：组件 `external-advisor-collab` 锁 tag v1.0.1→**v1.1.0**（十落点条款升级＋SKILL.md 版本 1.0.1→1.1.0·tag 打于升级批收净 HEAD·组件版本与 SKILL.md 同源）；plugin.json＋bundle.lock 双 0.1.1（纪律①每变必 bump·同源镜像）。触发＝皮总 04:11 指令「升级到专家包里装配」——授权范围＝装配①＋预览②两段，人类闸③/部署④候明示。同日另记：宿主 skills 散装面曾于 04:09 直拷过一次性旧态三包（备份 skills-backup-2026-10-30），该通道不属本项目部署口径，bundle 装配转正后以装配面为准。
- **版本账 v0.1.2**（2026-10-30·EAC-CLN·皮总拍板㊺指针闭集整改）：组件 `external-advisor-collab` 锁 tag v1.1.0→**v1.1.1**（交付物指针闭环清理：悬空样本指针内联成文／provenance spec_file 迁包内 `sources/spec-anchors.md`／changelog 案面路径清除——程序条款语义零动·引用形态清理＝补丁级）；组件 `deep-research` 锁 tag v1.0.1→**v1.0.2**（跨仓同步整改：README 变更记录行 devkits 案面指针改自包含陈述·skills 仓新不可变 tag）；plugin.json＋bundle.lock 双 0.1.2（纪律①每变必 bump·同源镜像）。同批包本体整改：README/deploy-gate 三处宿主家目录绝对路径写法改泛指陈述（㊺扫描口径下家目录路径模式零命中）。
- **版本账 v0.1.20**（2026-11-04·SWB-CD1 并发纪律成文批）：并发纪律成文＝dispatch 卷新建＋五席位守则行＋software-orchestration 1.1.4·纯条款面无机件。plugin.json＋bundle.lock＋.codebuddy-plugin/plugin.json 三同源 0.1.19→0.1.20（纪律①每变必 bump）。
- **版本账 v0.1.21**（2026-11-04·SWB-ES2 席位卡面随动批）：ES §四-1 卡面随动＝lead 誊录权明文＋architect adr 写权句＋engineer/qa 分层纪律句·纯明文面 N-2 零机件。plugin.json＋bundle.lock＋.codebuddy-plugin/plugin.json 三同源 0.1.20→0.1.21（纪律①每变必 bump·三同源）。
- **版本账 v0.1.22**（2026-11-04·治理层换钉批）：bundle.lock 组件行 ref/path 失步致装配 fail-closed（ref 钉旧 tag 落旧布局树·path 已随 B2 搬家批改新坐标·装配器取料落空 exit 3）——EAC 组件 ref 换钉 @v1.1.2（现内容新落点补打不可变 tag·技能条款语义零动·组件版本 1.1.1→1.1.2 随同源纪律）。plugin.json＋bundle.lock＋.codebuddy-plugin/plugin.json 三同源 0.1.21→0.1.22（纪律①每变必 bump·三同源）。
- **版本账 v0.1.16**（2026-11-03·SWB-T08R＋A1 权限表数据面机械化批）：权限表数据面机械化（SWB-T08R＋A1）：engineer 写域参数化＋deny 唯二落实＋hooks-map 新五身份补行＋host 裁定登记誊录权＋architect ADR 写域与 docs 三件套枚举开口，依据＝皮总裁定 ff72b92/18bf840/5358ea4＋ES 终态收口 28381a6；plugin.json＋bundle.lock 双 0.1.16（纪律①每变必 bump·三同源）。
- **版本账 v0.1.18**（2026-11-04·SWB-B4 门禁/票面锚定随动批）：门禁权限机件新树两级锚随动＝check-ticket-reconcile 缺省票目录按项目 `.scratch/tickets` 枚举＋非空正断言 exit 4＋回执指针项目根基面；write-guard/lease-issuer 锚换代＝项目根（docs/STRUCTURE.md 探针）；R⑧(i) deny `.collab/**` 显式枚举减授权精化（B1-D 十一桶真源）；engineer 枚举行按 STRUCTURE delivery_paths 填充＋project_domain_md 修值 docs/STRUCTURE.md；四席 deny 旧交付树字面换代；tests fixture 九件随新树；V13 登记件 R⑨ 尾追加追认（三哈希不变）。plugin.json＋bundle.lock＋.codebuddy-plugin/plugin.json 三同源 0.1.18（纪律①每变必 bump）。
- **版本账 v0.1.19**（2026-11-04·SWB-B5 收尾批）：D7 登记件入库＝`docs/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md`（字节级复制＋删源·三哈希不变 3f335333…/7214ad14…/efb4f765…）；`skills/sop/references/{product,architecture}-v2.9-copy.md` 来源注「源路径」两处随动改 docs 新位（来源注刷新＝交付面变更）；仓根 .gitignore 两制全量重写＋仓根 README 四节重写（非交付面·随批登记）。plugin.json＋bundle.lock＋.codebuddy-plugin/plugin.json 三同源 0.1.19（纪律①每变必 bump）。
- **版本账 v0.1.17**（2026-11-04·SWB-B2 交付面搬家批）：交付面搬家＝bundle 十三项 git mv 入壳 agent-experts/baigong-software-team/＋六技能包入壳 agent-skills/＋PRODUCT/ARCHITECTURE→docs/ 二段 mv＋门禁扫描根换代（run-gates/check-pointers/check-pointer-closure/check-skill-meta/check-entity/check-provenance/publish/assert-tool/bundle.lock path 键随动）；plugin.json＋bundle.lock＋.codebuddy-plugin/plugin.json 三同源 0.1.17（纪律①每变必 bump）。
- **版本账 v0.1.15**（2026-11-03·SWB-T07 微修票）：旧五席位卡（software-company-team-lead／software-product-manager／software-architect／software-engineer／software-qa-engineer 五件）物理清退＋`.codebuddy-plugin/plugin.json` 注册面随动指向新五卡（agents[]／agentName／teamInfo／members[].id）；plugin.json＋bundle.lock 双 0.1.15（纪律①每变必 bump·三同源）。依据＝皮总裁定②（`.collab/decisions/2026-11-03-皮总裁定-SWB票包遗留三件.md`）·SWB-T07。
- **版本账 v0.1.14**（2026-11-03·TKT41 SOP 域随动规则票收编批）：quick-mode/bugfix-path 两卷退役头注收编＋lead 卡豁免句删除＋§20.1①–⑥ 过渡口径标注九落点＋SKILL.md 索引两行随动 1.1.2→1.1.3；plugin.json＋bundle.lock 双 0.1.14。依据＝SWB v2.9 基线 §20.1⑦（V13 L227·全文 sha256 3f335333…）。
- **版本账 v0.1.13**（2026-10-31·纪律落点批·SOP-B1）：软开团 SOP 域条款批（分诊件 F1/F3 修票）——standard-sop.md 步骤 3 增「迁移/合并类设计附加项（条件触发）」对照样本机制对账表条款＋步骤 5 QA 增对账表覆盖度核对行；dev-discipline 增 §七 检出条款↔消费面对账（起草侧义务）＋§五 关系节互指行随动（与 handoff-discipline §九 互指）；software-orchestration 1.1.1→1.1.2（组件版本与 SKILL.md 同源纪律）。候裁面 SOP-B2（F2）未排施工、零实装。plugin.json＋bundle.lock 双 0.1.13。
- **版本账 v0.1.12**（2026-10-31·纪律落点批）：纪律落点批——dev-discipline 增 §六 票面起草职权、handoff-discipline 增 §十一 候裁面闭集（原§十一顺延§十二）、主理人席位卡两行自指短声明、software-orchestration 1.1.0→1.1.1；候裁机检当期不建咬面（候补池登记）。plugin.json＋bundle.lock 双 0.1.12。
- **版本账 v0.1.11**（2026-10-30·活文档批）：包内新增 `PRODUCT.md`（产品设计说明书：定位／用户与场景／五档能力地图／五席价值主张／质量承诺／非目标／交付形态）＋`ARCHITECTURE.md`（架构设计文档：编制图／席位三层与写权模型／技能包分卷地图／装配与版本架构／门禁架构／关键设计决策／演进边界）——两份为活文档，后续随批更新；plugin.json＋bundle.lock 双 0.1.11（纪律①每变必 bump·同源镜像）。
- **版本账 v0.1.10**（2026-10-30·收尾微票·门禁接线+席位声明 J6 收敛批）：run-gates 检查器清单追加 `check-ticket-reconcile`（OA-D6-5 声明闭集对账器挂门禁入口，缺省跑＝存量票 SKIP 走②属预期）；四席位 MD（主理人／架构／产品／QA）写权边界声明行末补「——细则见 dev-discipline」卷名指针（grep 双条件缺项整改）；工程师席写权边界②句改自指短声明（与 dev-discipline §三 条文最长连续重合压回 <12 CJK，语义不变＝回执含写入清单＋对账全等）。MC-SEAT-DECL 真实面读数 5→0。plugin.json＋bundle.lock 双 0.1.10（纪律①每变必 bump·同源镜像）。
- **版本账 v0.1.9**（2026-10-30·通用协作纪律整合·票三 G6+机检批）：`dev-discipline.md` §二 换代重写（G6 五要素入条：指针与内容同拦／不可解析编号功能性定义／开发叙事例外制／声明闭集制＋三段对账基面分段）；engineer MD 写权边界约束①同步句（J6 四读数入 evidence）；object-audit 文档域增 **D6-5 声明闭集对账**＋新检查器 `check-ticket-reconcile.py`（首挂 advisory）；`check-source-of-truth.py` 扩 C 段 **MC-SEAT-DECL**（J6 四读数机检）；multi-collab 60-gates 路由表进两行（MC-SEAT-DECL／OA-D6-5，均 advisory·multi-collab 版本账连锁 4.9→4.10）。software-orchestration 1.0.5→1.1.0、object-audit 0.6→0.7。plugin.json＋bundle.lock 双 0.1.9。
- **版本账 v0.1.8**（2026-10-30·席位声明补缺批）：五席位 MD 增「交接与收口声明」自指短声明节（lead 另补拒写权自指句＋⛓ 必读表 handoff-discipline 路由行；QA 补收口判定核对行）——细则真源在 software-orchestration 纪律两卷，席位侧只载自指短声明不复写。plugin.json＋bundle.lock 双 0.1.8。
- **版本账 v0.1.7**（2026-10-30·通用协作纪律整合批）：技能 `software-orchestration` 1.0.4→**1.0.5**——references 新增《交接与协作纪律》卷（handoff-discipline：交接件规格／三正面判据／append-only／收口自检五件套／验收读数分账／报告三律与核验分级／派工件干净度／机制断言须附实测／席位声明形式约束·交接/收口/报告/隔离律的通用真源，与《通用开发纪律》卷互指不复写），SKILL.md 索引增行＋触发词补「交接件、收口自检、报告三律、席位声明」；dev-discipline §五 关系节补互指一行。跨面包本包外的登记：multi-collab 技能包三正面判据全文真源迁本卷 §三（该包正文改沿革快照指针·版本账随其包内登记）。plugin.json＋bundle.lock 双 0.1.7（纪律①每变必 bump·同源镜像）。
- **版本账 v0.1.6**（2026-10-30·编制名册修正＋派工侧加载路由）：①《通用开发纪律》卷 §一 席位名册修正——软开团编制闭集＝主理人／产品／架构／工程师／QA 五席，删名册中不存在的「研究」编制；并增条款：调研是各席通用技能不是席位，调研取证按问题适配席位派执行、不新设研究席编制。②主理人席位 MD「⛓ 必读」路由表增通用开发纪律卷加载行（触发＝拟票/派工含代码性质或交付面写入）——派工合规硬门自此对派工侧也有加载入口，纪律不再只对席位侧生效。plugin.json＋bundle.lock 双 0.1.6（纪律①每变必 bump·同源镜像）。
- **版本账 v0.1.5**（2026-10-30·交付面自包含收口）：`bundle.lock` conventions 两处泛指化——装配缺省输出面盘符绝对路径字面删除，改「与 bundle 源仓同级的 `<bundle 源仓名>-build/<bundle 名>` 预览面」泛指措辞；repo 说明中仓工具带行号自指删除，改「由装配器解析」。语义零动（缺省输出规则与解析职责不变），交付物指针闭集口径下交付面内容闭环自包含。components 数组/ref tag/note 字段零动。plugin.json＋bundle.lock 双 0.1.5（纪律①每变必 bump·同源镜像）。
- **版本账 v0.1.4**（2026-10-30·通用纪律落地批）：技能 `software-orchestration` 1.0.3→**1.0.4**——references 新增《通用开发纪律》卷（写权闭集／代码纯度／工程师完工回执／QA 纯净职责四闸一体·席位级权限声明真源在各席位 MD「写权边界」节互指不复写，机检判据真源在审计器 D6-3/T6 只指不搬），SKILL.md 索引增行＋触发词补「写权闭集、回执清单、代码纯度、拒写权」。审计器包（仓内 deliverables 面）同批增交付包指针闭集条款与可达性子判据＋干净度六测 T6（该包版本账随其包内登记）。plugin.json＋bundle.lock 双 0.1.4（纪律①每变必 bump·同源镜像）。
- **版本账 v0.1.3**（2026-10-30）：席位写权边界条款入 MD＋README 出包标识清理＋装配器排除缓存件。①五席位 MD 各新增「写权边界」一节：过程席位（产品／架构／QA）与主理人席写权域＝过程域（`.collab/` 及其子目录），交付面无写权限（受命写入＝拒绝并报主理人改派）；工程师席＝交付面唯一写权席位（写入不得携带过程件指针，完工回执须含完整文件清单）。②README 自身出包标识清理：token 计数表删实测人列与实测 commit 列、口径句改泛指「token 计数脚本（script-v1 口径）」、批次码改「lead 瘦身批」、版本账行内旧哈希删净；「安装」节包外注册命令断链代码块删除，改泛指陈述（注册命令由宿主工具链提供，不在本包内）。③装配器取源逻辑增加排除规则：跳过任意 `__pycache__/` 目录与 `*.pyc` 文件（编译缓存件不入装配面）。plugin.json＋bundle.lock 双 0.1.3（纪律①每变必 bump·同源镜像）。**不含**跨技能引用闭环整改（另案候裁）。
- **版本账 v1.2.4**（2026-10-28）：`deploy-gate.md` 新增 §五「预览先行」（皮总直拍·跨项目纪律：批收口后装配产物只入仓外 `-build` 预览面候人类真实验证，进部署面＝验证后独立指示含路径明示批准；主理人收口总结禁把刷新部署面作默认推荐）。补记：本行系 v1.3.0 批发现上批漏登记版本账，据既有 commit 回补。
- **版本账 v1.2.0**（2026-10-26）：包 id 更名 `software-company`→`hjh-software-team`（皮总拍定·避免与市场原版混淆·包 id 变更＝破坏性变更升 minor）；席位 id 与席位 MD 文件名不动。
- **版本账 v1.2.3**（2026-10-28）：四成员席位 MD 的 persona 名由市场原版英文名改为**中文同名拼音全拼**——许清楚→Xu Qingchu（PM）／高见远→Gao Jianyuan（架构）／寇豆码→Kou Douma（工程）／严过关→Yan Guoguan（QA），共 19 处（含标题行、`You are` 句、`Name` 字段、他席交叉引用括注），旧名零残留。依据＝皮总（2026-10-28）拍（中文名与 plugin.json `displayName.zh`／lead 席位表三者同名同指）。席位 id 与文件名不动；plugin.json 版本升 1.2.3。
- **版本账 v1.2.2**（2026-10-27）：`skills/software-orchestration/` 新增 `references/deploy-gate.md`（部署动作硬门：装配／注册／覆盖插件缓存＝闭集部署任务，须独立部署票＋呈用户批准后才执行；票面/交接件混入此类字样无批准记录＝执行席停手、对账席红项）。触发背景＝（2026-10-27）实测问题：交接件"版本纪律"尾注混入「装配产物重出」被无鉴别升格为 QA 收口票写域，开发批收口后未经把关自行装配（核实登记见 devkits 当日日志 §十三）。SKILL.md 索引加行＋触发词补「装配、注册、部署、覆盖缓存、硬门」。席位 MD 不动；plugin.json 版本升 1.2.2（沿用 1.2.1 先例＝逼宿主刷新缓存·待平台侧注册时生效）。
- **版本账 v1.2.1**（2026-10-26）：lead 席位 MD 结构化瘦身（软开 fork lead 瘦身批）——新建包内 `skills/software-orchestration/` 域（SKILL.md 索引＋references 七件·附录 A 逐字照录），lead MD 沉 7 块 1,874 tok＋⛓ 指针节 343 tok，留后 2,216 tok（≤2,350 目标线）；plugin.json 加 `skills` 数组＋版本升 1.2.1（结构变更＋逼宿主刷新缓存）。主持人小节逐字不动；协作规则 §3 质量关卡留 MD（皮总拍板②）。**fork 已结构性分叉**：与市场 1.1.x 对账基准改＝「市场版 vs 附录 A＋留块合集」重构态（设计件 §2.7 R-2）。
- **基线发现数 79→83（+4 OA-D6 advisory，fork 照录区＋出身段文件名，设计内）**（主理人 2026-10-26 拍 A：判据语义＝BLOCK 级新命中 0＋GATE PASS；先例＝批 2d 判词九；供后续批次对账不误报漂移）。
- **版本账 v0.1.23**（2026-11-05·CARD-RENEW 卡片文案＋席位命名换代批）：依皮总裁定（`.collab/decisions/2026-11-05-皮总裁定-席位职业标签与花名换代.md`）五席花名换代（包好用/姜通透/顾长远/柯会码/沈得严）＋职业标签换代（项目负责人/产品经理不变/架构工程师/开发工程师/质量审计师）＋en 随动；头像五件改名与席位 id 同族（图像本体不重制）；卡片文案换代＝displayDescription/defaultInitPrompt/quickPrompts(5+1)/tags/description 对齐提案＋五席意见定稿，注册卡与包装卡口径分裂消除；README 功能/使用示例两节换代（旧「快速模式」档位与五段旧链口径随此退役）。三同源 0.1.22→0.1.23。
- **版本账 v0.1.24**（2026-11-05·CLN-PURE 装配净化批·补记）：publish.py 支持 bundle.lock 顶层 `assembly_exclude`（五类过程本体件裁出装配面）＋装配面存量非法指针全数自包含化＋EAC 组件 ref 换钉 `external-advisor-collab@v1.1.3`（组件版本 1.1.2→1.1.3）＋config/hooks/脚本注释面案号行号锚自包含化。三同源 0.1.23→0.1.24。补记：本行系 TMP-DISC 批发现上批漏登记版本账，据既有 commit 回补。
- **版本账 v0.1.25**（2026-11-05·TMP-DISC 临时工作物落位与清理纪律批）：决策者（2026-11-05）四款口径成文——`skills/software-orchestration/references/dev-discipline.md` 新增 §八（一切临时工作物唯一落点＝所属项目仓根 `.scratch` 区／收口登记票必含清理判据零残留／派工件禁仓外临时路径模板＋席位拒指权）；SKILL.md 索引＋触发词随动 1.1.4→1.1.5；sop 四脚本 docstring 旧 Temp 重定向措辞改仓根 `.scratch` 落点措辞；五席位卡守则节各补一行落位自指短声明。三同源 0.1.24→0.1.25（纪律①每变必 bump·三同源）。
- **版本账 v0.1.26**（2026-11-05·ADR-L0 判据成文＋首支点火批）：standard-sop ADR 工序节增第 6 款立项触发判据（T1-T4 入线/N1-N3 不入线＋混合拆分/覆盖链/申诉线）＋SKILL 索引触发词随动 1.1.5→1.1.6＋ADR-0001 首支落 docs/adr/（案 a 自指点火·ES2 双前置①②闭合）＋跨包随动（object-audit 0.8→0.9 E-ADR 五断言实装挂线／multi-collab 4.10→4.11 五 spec 进路由表）。三同源 0.1.25→0.1.26（纪律①每变必 bump·三同源）。

## 头像

`avatars/` 六件 PNG 在位（team＝团队图，五席各一；v1.3.1 版本账在册补齐批）。替换规格：PNG/JPG、512×512 px、单张 ≤500KB，文件名对应 plugin.json members[].avatar（team.png / software-team-lead.png / software-team-product.png / software-team-architect.png / software-team-engineer.png / software-team-qa.png）。

## 安装

将专家包目录放到宿主插件市场源的专家目录下（宿主根目录随安装环境而定，此处不写宿主路径），然后运行宿主注册命令使其可见（注册命令由宿主工具链提供，不在本包内）。

## Token 计数（终态·软开 fork lead 瘦身批后）

**口径要素**（缺一不计绿）：①口径版本＝token 计数脚本（script-v1 口径：CJK≈1 token/字、非 CJK≈4 字符/token）；②取整方式＝**ceil**（`-(-(n) // 4)`）；③判据线＝每席 ≤2,500（红线），目标 ≤2,350；④实测基线＝lead 瘦身批终态所在提交。

| 席位 MD | 行数 | token | ≤2500? | 口径版本 | 下沉件数 | 下沉 token |
|---|---|---|---|---|---|---|
| software-company-team-lead.md | 106 | **2,216** | 绿（≤2,350 目标线内） | script-v1 | 7 | 1,874 |
| software-product-manager.md | 93 | 1,072 | 绿 | script-v1 | 0 | 0 |
| software-architect.md | 142 | 1,475 | 绿 | script-v1 | 0 | 0 |
| software-engineer.md | 150 | 1,865 | 绿 | script-v1 | 0 | 0 |
| software-qa-engineer.md | 137 | 1,371 | 绿 | script-v1 | 0 | 0 |
| **合计** | **628** | **7,999** | — | script-v1 | **7** | **1,874** |

**读法（MD 是 cost center，references 是 asset）**：lead 瘦身前 3,777（旧基线更名前账，此后置）→ 瘦身后 2,216，净降 1,561；资产侧 `skills/software-orchestration/`＝references 七件正文 1,874 tok（附录 A 逐字账）＋SKILL.md 索引 631 tok（≤5,000 技能层线内）。**总量不降反微增**——成本从「每次会话全付」移到「按档触发才付」；下沉内容在 references 中逐字承载（C3 逐字门保护），lead MD 以「⛓ 必读」硬读指针直达（确定性通道，不依赖语义匹配）。四成员席位零改动（token 复算与收编批账一致：1,072／1,475／1,865／1,371）。

## 维护规则

**改席位定义只改仓内真源（本目录），部署面（`marketplaces/my-experts/plugins/baigong-software-team/`）只准从仓内复制生成**；运行缓存（`cache/my-experts/`）为宿主自管可再生副本，不入治理。
