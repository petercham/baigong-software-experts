# 期别审计（编译期 vs 运行时·对象体系的正交轴）

> **本件只持期别判据（问句式）。期别模型／装订链／无命中三态的设计规范在 `object-build/references/15-binding.md`，此处只留指针。**
>
> 出处：思想前身＝知识工程「知识库＋推理机」二分（Feigenbaum 1977【A 学术一手·PDF 已核】）；机制命名＝早期/晚期绑定、静态/动态链接（JLS §15.5、Ousterhout CS140【A】）；经验层＝Soar episodic memory【A 官方】＋CBR case base（Aamodt & Plaza 1994【A】）＋RAG non-parametric memory（Lewis 2020【A】）；工业成品＝VS Code `contributes.chatAgents`／`chatSkills`【A 官方】。

## P0 期别判定（审之前先问三句）

| 问 | 是 → | 审的尺子 |
|---|---|---|
| 这东西是**造的时候定死**、运行时不再改的吗？ | 编译期 | 契约＋负样本＋机检＋干净度 |
| 这东西是**每次按输入检索/生成**的吗？ | 运行时 | 检索有效性＋更新纪律 |
| 是**声明定死、挂载时检索**吗？ | 两态（技能层） | **要分段审**：声明面按编译期审，挂载面按运行时审 |

**审不出期别＝阻断**：用错尺子的后果比不审更坏——把案例库按编译期标准审，会逼出"案例库必须干净、必须穷尽"这类根本性错误要求（脏与不可穷尽是它的职责）。

## P1 编译期 vs 运行时：审计判据的差异（本器净增量）

| 维度 | 编译期对象（专家／节点／skill 契约） | 运行时对象（案例库／路由记录） |
|---|---|---|
| 干净度 | **必须过五测**（T1–T5） | **不要求**——脏是职责（记录件的学理依据：可更新性要求它不能被固化） |
| 穷尽性 | 可以且应当穷举 | **不可穷举**，"查不到"是合法终态 |
| 变更频率 | 封闭稳定（OCP：closed for modification） | 开放增长（CBR 的 RETAIN：案例库持续追加） |
| 审计轴 | 契约＋负样本＋机检 | **检索有效性**（该命中时命中吗）＋**更新纪律**（过期案例淘汰吗） |
| 主要失效模式 | 写冲突／格式漂移／契约违反 | 检索不到／案例过期／把旧案当新案用 |
| 归档 | 随结构性重建一次整批迁移 | 只增不删（史实锚），另设淘汰判据 |

**这一条直接改写对象路由**：案例库不该按"文档"或"skill"的标准审（那会要求它干净、可穷举、机检覆盖），它该按运行时对象审——查检索命中率和更新纪律。

## P2 期别写错的两个形态（可直接判）

| 形态 | 现象 | 判定 |
|---|---|---|
| **运行时要改的写进了编译期** | 案例/经验被硬编码进节点契约或角色定义；每加一条案例要改一次 skill | 关注（可延后）：能力增长成本随案例数线性上升 |
| **编译期该定的做成了可配项** | 「默认 X，项目可配」出现在判据/权限/写域上 | **阻断**：配置项存在即会被打开（单写者/判据不可自调这两条尤其致命） |

## P3 路由层缺出口（运行时对象特有）

**审**：若该对象设计了检索/调度，有没有答"查不到时怎么办"？

- 有明确三态之一（降级通用推理／显式报错／返回无匹配＋建议）＝通过。
- 完全没有 no-match 语义＝**关注**（黑洞：未命中时行为不可预测；业界两大厂商也都只有 routing 无 no-match，属普遍空白，不因此豁免）。

> 三态的设计形态与出处见构建侧 `15-binding.md`；**该三态为建议形态、未入正式协议**，不得作为验收判据引用，此处只用于判"有没有出口"。

## P4 三处必须修正的引用（核对出处准确性时用）

1. **ACT-R 没有 episodic memory**。ACT-R 官方只有 declarative＋procedural 两种记忆模块；procedural/semantic/episodic **三分是 Soar 的划分**（Soar 官方："Soar distinguishes three different types of LTM: procedural, semantic, and episodic"）。
2. **CBR 的起源是 Schank 1982《Dynamic Memory》**（Aamodt & Plaza 原文 `[Schank-82]`）；Schank & Abelson 1977《Scripts, Plans, Goals and Understanding》是脚本理论出处、CBR 的前史。两者都属实，引错年代失分。
3. **「挂载」不是学界标准词**。标准表述是「**运行时检索注入**（retrieve-time injection）」：RAG non-parametric memory／CBR RETRIEVE／in-context learning／episodic memory retrieval。

## 来源清单

| 来源 | 等级 | 用于 |
|---|---|---|
| https://bitsavers.org/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/PDF/1977/CS-TR-77-621.pdf | A Feigenbaum 1977 | 知识库＋推理机二分 |
| https://web.eecs.umich.edu/~soar/sitemaker/docs/misc/GentleIntroduction-2006.pdf | A Soar 官方 | episodic/procedural 三分＋procedural 不足才检索 |
| https://www.iiia.csic.es/~enric/papers/AICom.pdf | A Aamodt & Plaza 1994 | CBR 4R＋case base 与推理机分离 |
| https://arxiv.org/abs/2005.11401 | A Lewis 2020 | RAG：parametric vs non-parametric memory |
| https://code.visualstudio.com/api/references/contribution-points | A VS Code 官方 | chatAgents／chatSkills 的静态声明＋运行时激活 |
| https://docs.oracle.com/javase/specs/jls/se17/html/jls-15.html | A JLS | 编译期三步＋运行期求值 |
| https://web.stanford.edu/~ouster/cgi-bin/cs140-winter12/lecture.php?topic=linkers | A Stanford | 静态链接 vs 动态链接 |
