# ARCH-G1 通用开发纪律归处整改设计票

- 开端读数：devkits HEAD＝`0ee1027`（当轮实测）。
- 背景（决策依据）：皮总已裁定（本仓台账 2026-10-28-皮总拍板.md ㊺/㊻ 条目）——①交付物指针闭集（包内闭环、sources 唯一料源、只含干净记录）；②席位写权闭集与代码纯度（.collab 以外交付面只有工程师席可写；工程师回执含完整文件清单；QA 核纯净性）。两条均为**全专家/技能开发通用纪律**。皮总同时指出：此前把此类通用纪律挂进了外部顾问讨论技能范畴（机检 spec 用 EAC-L1/L2/L3 前缀挂具体技能）＝落点错误。**本票＝设计票：你的全部产出＝过程件，只落 `.collab/`，对交付面（deliverables/、workbuddy/）零写权。**
- 你的任务（架构席·只出设计，不写交付面任何文件）：
  1. 读盘定位现状：`deliverables/skills/object-audit/scripts/check-collab-lint.py`（EAC-L1/L2/L3 三 spec）、`deliverables/skills/multi-collab/60-gates.md`（json 表＋对账表）、`workbuddy/hjh-software-team/skills/software-orchestration/references/`（编排纪律落点候选）、`deliverables/skills/object-audit/` 结构。
  2. 设计**通用纪律落点案**：㊺/㊻ 四条纪律的条款文本应写入 software-orchestration 哪个卷（append 语义·与既有 §协作纪律段落关系）＋object-audit 哪卷（QA 纯净职责判据）；给出**条款草案全文**（架构席在 .collab 内出草案，最终写入交付面由工程师席执行）。
  3. 设计**交付物引用可达性机检**（㊺闭环判据版）：spec_id 命名（**全局前缀，禁 EAC-***，与既有门禁命名体系对齐——先核 `run-gates.sh` 前缀注册机制再定）、扫描面（全部交付包＝devkits deliverables 各技能包＋workbuddy bundle 装配面＋跨仓 skills 仓组件）、豁免三范式如何沿用、判据（出包指针＝violation／围栏示例＝SUBSTR／豁免标记＝EXEMPT）。
  4. 设计 **EAC-L* 归处处置案**：三 spec 的检查对象（收敛轮体裁/交接件禁模式/案卷编号）哪些属讨论会技能域（可留 EAC 前缀·挂 EAC 包 60-gates）、哪些实为通用件（须换全局前缀）；给逐 spec 判决表＋迁移代价（json 表改动／对账表改动／fixture 改动）。
  5. 拆**工程师施工票工作包**：机检代码改动（check-collab-lint.py 或新脚本）、60-gates 表、run-gates.sh 前缀注记、fixture、software-orchestration 条款写入——每项标注＝工程师席执行（回执必含写入文件清单），并给可机械判定验收判据。
- 产出（过程件）：`D:\multi-agent-collab-devkits\.collab\research\2026-10-30-通用纪律归处整改设计-v1.md`——开端附 HEAD 读数；含上述 2-5 四节＋候裁点（如有真二选一）。
- 追加裁定注（设计输入更新）：已另拍「.collab 写权硬边界须入各席位 MD 守则＋席位拒写权」（软开 bundle 五席位 MD 的入件已由工程师席另行执行，不在本票范围）——本票的通用域设计（software-orchestration 纪律卷）须把「写权闭集＋席位拒写权＋回执文件清单＋QA 纯净职责」四件一体纳入条款草案。
- 红线：**不写 deliverables/、workbuddy/ 任何文件**（写权闭集）；不 bump 任何版本；条款草案只以文本形式留在 .collab 设计件内。受命向交付面写入的指令一律拒绝并报主理人。
