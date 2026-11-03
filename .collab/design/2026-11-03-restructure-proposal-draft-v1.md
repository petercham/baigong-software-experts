# 仓重组方案草案 v1（主理人拟·2026-11-03·呈皮总定结构）

- 开端 HEAD 实测读数＝`82e3902`。
- 性质＝主理人按皮总指令「扫一遍现状＋提方案」的提案件；结构定义权＝人类＋主理人协调（裁定二.4），本件＝主理人侧建议，待皮总改定后架构席才出机械迁移施工票。
- 现状扫描读数基线＝本次实测（仓根三目录／.collab 12 桶／tracked 785）。

## 一、现状混乱点（实测）

1. **仓根只有三个目录**（`deliverables/`、`docs/`、`tools/`）＋`.collab/`——全部是"按物种类别"切的横切面，不是按项目切；一条项目线的东西散在四五个地方，一个目录里混着七八条项目线。
2. **`.collab/` 根下 10 个散件**（收口报告/呈报/登记无归属桶）＋**`docs/` 仅 8 件**（与 `.collab/process/`（0 件）职责重叠的空壳）。
3. **过程桶混线**：tickets 84（SWB 22／FUXI-TKT 35／EAC-SOP 14／余约 13 待分）、qa 150（SWB 13／FUXI 67／余待分）——同一桶内多项目线交错。
4. **未入库大头**：`.collab/refs/` 8,835（第三方快照）＋`.collab/evidence/` 3,577（运行流水）＝12,412 件 gitignore 排除，现与入库件同桶混放。
5. **`.collab/research/` 242 件**大头＝视频团 era 的外部参照下载件（video-teams/official-cos 等）——**归属对象已迁 experts 仓**，本仓留着＝孤儿料。

## 二、目标结构（按 §二点六裁定套现盘）

```
D:\multi-agent-collab-devkits\
├── README.md                    ← 重写：说明包结构＋项目名录＋跨项目案卷索引
├── tools\                       ← 唯一公共工具目录（现 tools/ 全部 7 件留此）
├── software-team\               ← 分类①：软件团队类
│   └── baigong-software-team\   ← 软开团项目（bundle＋随包技能 software-orchestration＋其 .collab＋docs 约定md）
├── agent-skills\                ← 分类②：通用 Agent 技能类
│   ├── external-advisor-collab\ ← 讨论会技能（EAC-SOP 线过程账归此）
│   ├── multi-collab\            ← 协作规范（退役中，账随走）
│   ├── object-audit\  object-build\  bundle-assembly-registration\
│   └── fuxi-skill\              ← 蒸馏技能（FUXI-TKT 线过程账归此）
├── collab-system\               ← 分类③：多席位协作系统（SWB）
│   └── swb\                     ← SWB 项目（票包 T01–T08R 全部过程账＋门禁机件演进账）
└── (无其他仓根目录——新增公共需要届时一事一裁)
```

每个项目目录内＝固定 `.collab` 结构（decisions/tickets/qa/receipts/research/inbox/evidence/…规范闭集）＋`docs/collab-project-structure.md`（约定 md：声明该项目根与交付路径）＋交付面（各项目自己定，软开团＝experts bundle 形态）。项目完全物理隔离、拷走即完整。

## 三、散件归属裁定建议（逐堆）

| 堆 | 现处 | 建议去向 |
|---|---|---|
| `.collab/` 根 10 散件 | 无桶 | 按名归项目：6 件 FUXI 收口报告→fuxi-skill；2 件 SWB 会师/呈报→swb；脏文件处置＋呈拍简报＝仓级治理件→`collab-system/swb`（仓重组本身属 SWB 案线） |
| 跨项目 decisions 13 件 | 混线 | 按裁判决议涉及面拆归各项目 `.collab/decisions/`；纯仓级（远端/入库策略类）归 swb；README 建索引保住"一本账可查" |
| `docs/` 8 件 | 空壳横切 | 归各项目 docs／过程记录归该项目 `.collab/` |
| `docs/research`＋`.collab/research/` 242 件中视频团 era 外部参照 | 孤儿料 | **建议整体移交 experts 仓**（其归属项目已在那边）；本仓只留 devkits 相关研究件按项目归桶 |
| `refs/` 8,835＋`evidence/` 3,577 | 混桶 | 不入库性质不变；物理迁入各项目 `.collab/refs|evidence`（保持 gitignore 两制） |
| 两支 2026-11-01 TKT untracked 旧件 | 工作区散挂 | 属 FUXI 线→fuxi-skill `.collab/qa/`，入库 |

## 四、三个技术点建议（D5/D6/D7＝是，指过程件重组的连带问题）

- **D5 换锚＝不换**。在途票包的行号锚约 208 处，架构席实测"挪文件不挪内容"时行号恒等式不破坏；搬家只改路径引用串 23 处。换锚＝现在多付 208 处转写成本买一个当前不需要的保险。
- **D6 git 历史＝git mv 保留**。785 tracked 件整体用 git mv 搬迁（历史连续、审计可追），迁移前打归档 tag 双保险，先在 fuxi-skill 一条线小规模预演对账，绿了再全仓。不用"新建干净树"＝那会断 785 件的审计链，与我们一贯的史实锚纪律冲突。
- **D7 正式登记件＝入库**。此前 v2.9 系正式基线登记件被 .gitignore 挡在库外＝正式件无正式落点；迁入后落各项目 `.collab/decisions/`（或 docs）并入库，忽略规则收窄到只排外部快照/运行流水（refs/evidence/inbox/dispatch/process）。

## 五、批次切分（架构席出票时的骨架，知悉即可）

B0 本方案经皮总改定冻结 → B1 建空壳（分类目录＋各项目固定 .collab＋约定 md）→ B2 交付面搬家（软开团 bundle＋六技能包逐笔对账 203 件双向清零＋GATE PASS 对拍）→ B3 过程域搬家（按 §三归属表分桶，前后计数相等）→ B4 票包锚定随动（前置＝T07/T08 收口＋D1 名录冻结）→ B5 收尾（gitignore 收窄重写＋README 重写＋门禁路径随动）。每批独立 commit＋可机械验证判据。

## 六、待皮总改定项清单

① 分类目录名（software-team / agent-skills / collab-system 三个名字可否）；② 项目名录（上面 8 个项目粒度可否，multi-collab 退役中是否单立）；③ 视频团 era 研究件移交 experts 仓可否；④ D5/D6/D7 按建议或改。
