# baigong-software-experts · 百工软件团队专家包仓

> 仓性质：本仓＝百工软件团队专家包独立仓（remote＝petercham/baigong-software-experts·出仓归位 2026-11-21·史面真源＝`.collab/decisions/2026-11-21-出仓归位-迁仓登记-v1.md`）。
> 沿革：2026-11-21 自 devkits 仓出仓归位独立成仓；devkits 时代仓面文案随 SWB-BG-06（ITER-E）重写退役，史面沿存于投递前链笔（append-only 载体换代案型·施工回执在册）。

## 一、仓性质一行

本仓＝百工软件团队专家包（bundle）独立仓：包体（嵌套层）＋治理案卷＋仓级共享料源同仓。仓根入库面白名单＝下表；其余顶层目录出现＝违例（门禁断言沿 SWB-B5 回执判据 1）。

## 二、仓根白名单结构表（ITER-E 归位态）

| 路径 | 性质 | 进 git | 说明 |
|---|---|---|---|
| `README.md` | 仓根索引 | ✅ | 本件（根只放 README·薄写不复写正文） |
| `agent-experts/baigong-software-team/` | bundle 包体（嵌套前缀层） | ✅ | 包体唯一盘面＝`bundle.lock` bundle.path 具名指向；包内＝交付面（`skills/`、`agents/`、`avatars/`、`hooks/`）＋`docs/`＋`config/`＋`.collab/` 案卷＋`.scratch/tickets/` 票面＋`tests/`＋三同源（`plugin.json`／`bundle.lock`／`.codebuddy-plugin/plugin.json`） |
| `share/` | 仓级共享料源（门禁/工具脚本真源） | ✅ | 仓级闸与料源件（check-collab-buckets、check-pointers、baseline-pointer-exempt、run-gates、install-hooks 等）；使用方包装配时自包含嵌入包内 `tools/` 挂载位；项目级专属门禁脚本住包内 `skills/sop/scripts/` |
| `.collab/`（仓根） | 治理史实锚案卷 | ✅ | 桶名闭集真源＝`.collab/README.md` 名录行（MC-BUCKET-1 机检对拍）；史实锚桶 append-only |
| `.collab/{decisions,qa,receipts,board,research,design}/`（包内） | 史实锚案卷 | ✅ | 判词/裁决/回执/核验/研究/设计稿·append-only |
| `.collab/{refs,evidence,inbox,process,dispatch,backup}/`＋`tmp-*.txt` | 过程流水/证据/运行时 | ❌（gitignore） | 嵌套桶级＋仓根显式双形态配对行（两制在册） |
| `.scratch/tickets/`（仓根＋包内） | 票面落位 | ✅ | 票面真源落位（票面落 scratch 裁定承接）；仓根及各包 `.scratch/` 其余族＝gitignore 忽略态（SWB-SCRATCHG） |
| `softwares/` | 软件工程项名录 | ✅ | 空名录·届时按票入册（README 一枚在位） |
| `agent-skills/` | DEP 装配预览消费面 | ❌（gitignore） | 组件取源＝对象库＋tag，非盘面（五组件锁 tag 独立仓可解析·SWB-BG-06 §二.7 现跑在册）；忽略只管未跟踪可见性，不伤对象库取源 |
| `.workbuddy/`、`__pycache__/`、系统杂物 | 会话/编译产物 | ❌（gitignore） | 可弃 |

**分区判据**（一句话）：这份东西是拿来**照着做**的（交付面/docs，审），还是拿来**查当时发生了什么**的（案卷，记），还是**用完可弃**的（process/evidence/inbox，不入库）。入库面/排除面两制条款真源＝`.gitignore`（SWB-B5 重写笔·ITER-E G8 增行在册）。

## 三、嵌套层保留条款（反摊平·SWB-BG-06 立票）

嵌套层保留条款：仓根 agent-experts／baigong-software-team／ 前缀层＝本 bundle 包体唯一盘面（bundle.lock bundle.path 具名指向），合法结构禁摊平＝任何「把嵌套层内容上移根层」提案＝拆装配链案型（bundle.lock path／plugin.json／装配线全失步）＝须经全量档流程变更票重裁，禁以维护名义就地摊平；本条款立票＝SWB-BG-06（ITER-E）·勘正链锚＝迁仓登记件 §五。

## 四、项目名录（一项·闭集）

名录闭集真源＝各分类目录 README；本表为汇总视图。新项目按票追加。

| 分类 | 项目 id | 一句话 | 版本线 |
|---|---|---|---|
| agent-experts | `baigong-software-team` | 百工软件团队专家包（五席 SOP 驱动·账本为真相·租约写门·机检门禁） | v0.1.35（plugin.json＋bundle.lock＋.codebuddy-plugin 三同源·纪律①每变必 bump） |

（`softwares/`＝空名录·届时再入。devkits 时代技能项目六行随出仓退役，史面沿存于投递前链笔。）

## 五、治理约定（沿可存续句·自旧册随迁）

1. **单写者**：本仓 git 写操作由唯一执行通道完成；审计/研究席永无写盘权——现行有效·机检真源＝`agent-experts/baigong-software-team/config/seat-permissions.json`＋hooks 面（T08R 机械化）。
2. **decisions 只增不改**：append-only，勘误＝原文后注——现行有效·协作纪律语义沿 multi-collab 组件（取源＝对象库＋tag）。
3. **命名**：目录与文件名 ASCII 小写 kebab-case；文档正文中文自由——现行有效·定标真源＝`agent-experts/baigong-software-team/.collab/receipts/2026-11-03-ES-工程规范定标-终态收口登记-v1.md`。
4. **索引路由**：每一级子包根只放 README.md（边界一句话＋索引·薄写不复写正文）——现行有效·定标沿 doc-governance D5-3（用户级技能库面·非本仓件）。
5. **skill 形态约束**：入口少、分件多、分件平铺一层不嵌套（官方 spec "one level deep"）——现行有效·研究依据留包内 research 桶指针。
6. **引证纪律**：七类引证失效扫描——真源＝object-audit 组件 references/00-skeleton.md（取源＝对象库＋tag·指针不复写）。

## 六、本包的两个设计决定（沿存·出处＝`agent-experts/baigong-software-team/.collab/decisions/2026-10-22-裁决记录.md`）

- **不按对象拆 skill**——业界无先例（Parnas 1972／ISO 9001 §0.1／buf／ESLint 生态），判据＝「边界是否等于加载边界」。
- **`.collab` 按性质分区不按 actor**——`.` 前缀不表达 git 归属；decisions 进 git 是 ADR 惯例（决策记录必须可追溯）。
