# 仓重组方案草案 v2（主理人拟·2026-11-03·按 §二点六＋§二点七重提）

- 开端 HEAD 实测读数＝`b9b30f3`。
- 取代件＝`2026-11-03-restructure-proposal-draft-v1.md`（其分类目录名 software-team/agent-skills/collab-system 作废；交接件归属口径按 §二点七两级分流更新）。
- 依据裁定＝裁定三全文（§二点五 无特例／§二点六 两级路径＋仓根白名单／§二点七 分类名录＋交接件两级分流）。

## 一、目标结构（三分类 · 八项目 · 唯一公共 tools）

```
D:\multi-agent-collab-devkits\
├── README.md                     ← 重写：包结构说明＋项目名录＋跨项目案卷索引
├── tools\                        ← 唯一公共工具目录（现 tools/ 7 件全留：门禁/真源对账/token计数）
├── agent-experts\
│   └── baigong-software-team\    ← 软开团专家包（bundle＋PRODUCT.md/ARCHITECTURE.md 进其 docs/）
├── agent-skills\
│   ├── external-advisor-collab\  ← 讨论会技能
│   ├── multi-collab\             ← 协作规范（退役中）
│   ├── object-audit\             ← 对象审计（含 run-gates 等机检脚本随包走）
│   ├── object-build\             ← 对象构建
│   ├── bundle-assembly-registration\ ← 装配注册
│   └── fuxi-skill\               ← 蒸馏技能（FUXI 全过程账归此）
└── softwares\
    └── swb\                      ← 多席位协作系统（SWB 开发线：T01–T08R 票账＋探针＋设计件）
```

- 分类名录按皮总 19:1x 原话；其中「agent-expers」按拼写更正登记为 `agent-experts`（＝主理人引申注明，若您要原拼写请指出）。
- 每项目内＝固定 `.collab`（decisions/tickets(或.scratch)/qa/receipts/research/board/inbox/evidence/refs）＋`docs/`（约定 md＋持久文档）＋自由分层面。约定 md＝`docs/collab-project-structure.md`（T08R 已提案，字段用项目根相对字面）。

## 二、交接件两级分流（§二点七新纪律的落位表）

| 件类 | 性质 | 落位 |
|---|---|---|
| 产品/架构文档、正式基线登记件（如 SWB 交接件 v2.9）、README、PRODUCT/ARCHITECTURE | 持久·可分发 | 项目 `docs/` |
| 分票票包（T 系/TKT 系/SOP 系票面） | 高频迭代·非持久 | **推荐＝项目 `.scratch/tickets/`**（Matt Pocock 式：一票一文件、编号、Status/Blocked-by 行）；备选＝项目 `.collab/tickets/`（现行） |
| 审票件/判词/回执/会师登记/收口报告 | 裁决史实锚 | 项目 `.collab/qa|receipts|decisions/`（维持入库） |
| 拍板/裁定 | 跨案权威 | 项目 `.collab/decisions/`＋仓级 README 索引 |
| 研究底稿/外部参照 | 判词依据·第三方 | 归项目 `.collab/research|refs/`；视频团 era 件移交 experts 仓 |

**主理人推荐＝`.scratch/tickets/`**，理由：①票面更新频繁且被审改多轮，与 `.collab` 的史实锚性质确实不同层；②Matt Pocock 范式与我们工序天然对位（spec→tickets→逐票施工，Status 行＝票状态机雏形）；③`.collab` 瘦身后其"裁决史一本账"更纯净。
**代价（须随动）**：`check-ticket-reconcile.py` 缺省票目录、票包对账链、门禁 SCRIPTS 锚全要改——这正是输入件点名过的危险形态（缺省票目录漏随动＝exit 0 假绿），B4 批硬判据必须含"新旧两目录对账双清零"。

## 三、SWB 交付物归属问题（新暴露·需您裁）

SWB 的交付物（席位权限配置、执法钩子、SOP 脚本、探针测试）现在实装于软开团 bundle 内（`agent-experts/baigong-software-team/` 下的 config/hooks/tests）——机制的家在 softwares/swb、运行面却挂在专家包里。物理隔离口径下两条路：
- **甲（推荐）**：SWB 项目＝机制真源（代码＋票账住 `softwares/swb/`），其交付物经**装配步**注入软开团 bundle（仓内已有 `publish.py --assemble` 先例）；bundle 内相应面标注"装配产物非真源"；
- 乙：SWB 不单立项目，其开发账并入软开团项目（省事但 SWB 与专家包耦合延续，违背您"每个项目独立自包含"方向）。

## 四、其余归属账（承 v1 §三，增量）

- `.collab/` 根 10 散件：6 件 FUXI→`agent-skills/fuxi-skill`；2 件 SWBFIX→`softwares/swb`；脏文件处置＋呈拍简报→`softwares/swb`（仓重组属 SWB 案线）。
- 跨项目 decisions（13 件）：按裁决涉及面归各项目 `.collab/decisions/`，README 建索引；纯仓级（远端/入库策略）归 `softwares/swb`。
- `docs/` 8 件→归各项目；两支 2026-11-01 TKT untracked 旧件→fuxi-skill `.collab/qa/` 入库。
- `refs/` 8,835＋`evidence/` 3,577→各项目对应桶（gitignore 两制不变）。

## 五、批次骨架（架构席出票基准）

B0 本方案裁定冻结 → B1 空壳（三分类＋八项目固定 .collab＋约定 md）→ B2 交付面搬家（软开团＋六技能包 203 件逐笔对账清零＋GATE PASS 对拍）→ B3 过程域搬家（按 §二/§四归属表分桶，前后计数相等；票面按裁定的落位形态迁移）→ B4 票包锚定＋门禁随动（前置＝T07/T08R 收口＋票目录裁决；含 check-ticket-reconcile 缺省面改造）→ B5 收尾（gitignore 收窄＋README 重写＋tools 消费路径按仓根唯一公共定位）。

## 六、待裁清单（收敛后只剩四项）

1. 拼写确认：`agent-experts`（我的更正）还是 `agent-expers`（原话）；
2. 票面落位：`.scratch/tickets`（推荐）还是 `.collab/tickets`；
3. SWB 归属：甲（装配注入·推荐）还是乙（并入软开团）；
4. 视频团 era 研究件移交 experts 仓：可否。
（D5 不换锚／D6 git mv 保留打 tag／D7 正式登记件入库——v1 建议未在 §二点七 被推翻，视您"照准"即冻结。）

## 勘误（19:17 皮总指正·HEAD `2771512` 后追加）

- **§一 softwares\swb 行作废（主理人造概念违例·同「公共区」同族）**：多席位协作系统不是独立项目——baigong-software-team 就是 SWB 的本体与交付载体，SWB 票包产出的机制面（config/hooks/tests/skills.sop）已在该包内＝其自己的家。§三「SWB 归属甲/乙」伪题撤销。
- 分类名录维持 agent-experts／agent-skills／softwares 三类（§二点七原裁定），但**当下 softwares 类为空**（无传统软件项目，届时再有项目再入）；项目名录收缩为 7 个：软开团×1＋技能×6。
- SWB 全部过程账（T 系票包/审件/回执/交接件 v2.9 登记件）→ 归 `agent-experts/baigong-software-team/.collab|docs`。
- 待裁清单随之收敛为三项：拼写（agent-experts vs agent-expers）、票面落位（.scratch/tickets vs .collab/tickets）、视频团研究件移交 experts 仓。
