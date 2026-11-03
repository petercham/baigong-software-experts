# 仓重组方案草案 v3（主理人拟·2026-11-03·终态口径全量合成）

- 开端 HEAD 实测读数＝`a333fb4`。
- 取代 v1/v2（含 v2 勘误段）。依据＝裁定三全文（§二点五 无特例／§二点六 两级路径＋仓根白名单／§二点七 分类名录＋交接件两级分流／§二点八 活文档进 docs）。
- 版本线：百工 bundle 维持 0.1.14 开发态续 bump（皮总 19:25 裁定）。

## 一、目标结构（仓根白名单闭集：README＋tools＋三个分类目录）

```
D:\multi-agent-collab-devkits\
├── README.md                       ← 重写：包结构说明＋项目名录＋跨项目案卷索引
├── tools\                          ← 全仓唯一公共工具目录（现 7 件：run-gates 挂接的
│                                     check-source-of-truth / check-truename / count_agent_tokens 等）
├── agent-experts\                  ← agents 类型项目（专家团）
│   └── baigong-software-team\      ← 百工软开团＝多席位协作系统本体（版本账 0.1.14 连续）
├── agent-skills\                   ← 单技能项目
│   ├── external-advisor-collab\    ← 讨论会技能
│   ├── multi-collab\               ← 协作规范（退役中·账随走）
│   ├── object-audit\               ← 对象审计（机检脚本随包走）
│   ├── object-build\               ← 对象构建
│   ├── bundle-assembly-registration\ ← 装配注册
│   └── fuxi-skill\                 ← 蒸馏技能（含 products 产物池）
└── softwares\                      ← 传统软件项目分类（当下为空，届时再入）
```

- 名录拼写＝`agent-experts`（已决·拼写候裁项由主理人按裁定件㊺ L46 名录明文判定销账，2026-11-03）。
- 项目总数＝7。每项目自包含完整工作空间（拷走即完整）、物理隔离、无特例。

## 二、每个项目内部的标准结构（规范闭集三段式）

```
<project>\
├── docs\
│   ├── STRUCTURE.md  ← 约定 md（项目根/交付路径声明·T08R 提案·字段项目根相对字面
│   │                                   ＋YAML 围栏块＋schema_version＋delivery_paths 拒 docs 前缀行）
│   └── <当前存活的干净交接件>        ← 产品设计/架构设计等持久分发级文档（§二点八）
│                                       例：百工 docs\PRODUCT.md、ARCHITECTURE.md（从包根迁移）
│                                       例：SWB 交接件 v2.9 正式登记件（D7 入库落此）
├── .collab\                         ← 固定结构（专家团规范定义·用户 md 不得覆写）
│   ├── decisions\                   裁决/裁定/判词（史实锚·入库）
│   ├── qa\ receipts\ board\         审件/回执/看板（史实锚·入库）
│   ├── research\                    判词依据研究件（入库·负向防御规则随动）
│   ├── refs\ evidence\ inbox\ process\ dispatch\   （gitignore 两制不变）
│   └── README 索引\跨项目案卷只指不搬
├── .scratch\tickets\                ← 票包（推荐落位·Matt Pocock 式：一票一文件/依赖序编号/
│                                     Status+Blocked by 行；高频迭代·非持久分发对象）
└── <交付面·各项目自定>               ← 百工＝bundle 面（agents/skills/config/hooks/tests/plugin.json/
                                      bundle.lock/avatars/settings.json）；技能＝SKILL.md+references
```

票面落位二选一（`.scratch/tickets` vs `.collab/tickets`）＝待裁项②；下表按推荐态写。

## 三、现状→归宿全账（实测口径）

| 现位 | 件数 | 去向 |
|---|---|---|
| `deliverables/experts/baigong-software-team/` | bundle 全树 | → `agent-experts\baigong-software-team\`（交付面原位语义）；PRODUCT/ARCHITECTURE 两件→其 `docs\`（§二点八随动＋引用锚更新） |
| `deliverables/skills/<六包>` | 203 件（deliverables 面）| → `agent-skills\<各包>\`；`deliverables/README.md` 删除（表并入仓根 README） |
| `deliverables/experts/baigong.../tests/probes` 等 SWB 机制面 | — | 留 bundle 内（本就是百工交付物·无独立 SWB 项目） |
| `.collab/tickets/` 84 件 | 混线 | 按票号归项目：SWB/SWBFIX/SWB-T/T07-T08R→百工；TKT/FUXI→fuxi-skill；EAC/SOP→external-advisor-collab 或百工（按票主项目）；落位按裁项② |
| `.collab/qa/` 150／`receipts/` 48／`board/` 1 | 混线 | 同上按项目归 `.collab\qa|receipts|board\` |
| `.collab/decisions/` 13 件 | 跨项目 | 按裁决涉及面归项目 `.collab\decisions\`；纯仓级（远端/入库策略类）归百工；仓根 README 建一本账索引 |
| `.collab/` 根 10 散件 | 无桶 | 6 FUXI→fuxi-skill；2 SWBFIX＋脏文件处置＋呈拍简报→百工 |
| `.collab/design/` 17 件 | 混线 | 按案线归项目 `.collab\design\`（设计稿属过程域；其中现行有效设计稿若属交接件性质→docs，按 §二点八 存活判据逐件分） |
| `.collab/research/` 242 件 | 视频团 era 大头 | 判词依据类按项目归位；**视频团 era 外部参照件整体移交 experts 仓**（待裁项③）；devkits 相关留各项目 |
| `.collab/refs/` 8,835／`evidence/` 3,577 | 未入库 | 迁各项目对应桶（gitignore 两制随动重写） |
| `.collab/inbox/` 9／`dispatch/` 10／`process/` 0 | 运行流水 | 迁各项目同名桶（不入库不变）；旧流水可径归档 |
| `docs/` 8 件（process/research 子桶） | 空壳横切 | 内容归各项目 docs 或 `.collab` |
| `tools/` 7 件 | 全仓消费 | 留仓根 `tools\`（§二点六唯一公共）；`run-gates.sh` 在 object-audit 包内，其 `ROOT/tools/` 锚＝B4 改上溯/参数注入 |
| 工作区 2 支 2026-11-01 TKT untracked 旧件 | 散挂 | fuxi-skill `.collab\qa\` 入库 |
| `.gitignore` | 全文件 | B5 重写（两制：史实锚入库／外部快照+运行流水排除；路径全部随新树） |

## 四、三技术点（建议冻结）

- D5 换锚＝不换（实测挪文件不挪内容行号恒等式不破坏；只改 23 处路径引用串）；
- D6 git mv 保留历史＋迁移前打归档 tag＋fuxi 线小规模预演先行（785 tracked 件审计链不断）；
- D7 正式登记件（SWB 交接件 v2.9 系）＝入库落百工 `docs\`（§二点八落点确认）。

## 五、批次切分（架构席出票骨架）

- **B0** 本方案裁定冻结（含裁项①②③落定）。
- **B1** 空壳：三分类目录＋7 项目固定 `.collab` 骨架＋约定 md 落位（含 B4 前的旧门禁不误跑处置）。
- **B2** 交付面搬家：bundle＋六技能包逐笔 git mv，203 件对账双向清零＋GATE PASS 对拍；PRODUCT/ARCHITECTURE→docs 随动改锚。
- **B3** 过程域搬家：按 §三表分桶，前后分桶计数相等；票面按裁项②落位形态迁移（含 Matt Pocock 式头部转换与否随裁）。
- **B4** 门禁/票面锚定随动：check-ticket-reconcile 缺省票目录改造＋票目录新旧双清零硬判据＋run-gates `ROOT/tools` 上溯化＋hooks-map/write-guard 路径锚两级化＋T08R 枚举行按 D1 名录填充。**前置＝T07/T08R 收口＋R⑧过渡态处置先行**（PM 黄-3 硬前置）。
- **B5** 收尾：gitignore 重写＋仓根 README 重写（结构＋名录＋跨项目案卷索引）＋D7 登记件入库。

每批单独 commit＋可机械验证判据（对账清零/计数相等/门禁零回归对拍）。

## 六、待裁清单（终版·两项·拼写项已销账）

1. 票面落位：`.scratch/tickets`（推荐·高频迭代语义）vs `.collab/tickets`（现行·机检改造量小）；
2. 视频团 era 研究件移交 experts 仓：可否。

> 清残注记（2026-11-03·主理人指令）：原第 1 项「拼写：agent-experts vs 原话 agent-expers」＝无效候裁项，按裁定件㊺（`.collab/decisions/2026-11-03-皮总裁定-项目自由分层与collab固定结构及docs约定md.md` L46 名录明文＝agent-experts／agent-skills／softwares）判定销账＝拼写定夺 `agent-experts`，无待裁语义；B1+ 迁移票闭集目录名一律 `agent-experts`。

（版本线 0.1.14 续 bump 已裁；排程序列＝T07 放行→T08R 施工→B0→B1+ 不变。）
