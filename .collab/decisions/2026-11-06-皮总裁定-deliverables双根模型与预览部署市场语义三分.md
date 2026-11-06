# 皮总裁定 · deliverables/ 双根模型与预览/部署/市场语义三分

- 登记日期：2026-11-06
- 登记人：主理人（誊录决策者原话）
- 开工 HEAD 读数：65ccedb

## 一、裁定原文（逐字）

> deliverables/ 的正确用法是这样：
> 1、专家团具备两个面的操作段，开发面= {dev_root}/{project_id}，交付面={del_root}/deliverables/{project_id}。所有专家团开发的不同项目的交付都集中在 {del_root}/deliverables/ 管理。
> 2、所谓交付面就是我们所说的装配-清理编译，干净的可交付件的存放路径，这个路径也是需要单独 git 的，而且我听同事说，git 本身好像支持基于开发面创建公开的用于交付的仓
> 3、预览是指的用户本地部署到 Agent 系统内，部署指的是发布到 git，而之前说的发布到指定 Agent 平台的市场并不属于专家团的职责，是人类自己的另外操作流程，不应该在专家团内部或者装配 skill 内部定义。

## 二、裁定要点拆解

1. **双根操作面**：开发面 `{dev_root}/{project_id}` 与交付面 `{del_root}/deliverables/{project_id}` 分根；全部项目交付集中于 `{del_root}/deliverables/` 统一管理。
2. **交付面定性**＝装配-清理编译后的干净可交付件存放路径；**单独 git**；「git 基于开发面创建公开交付仓」机制＝同事转述，待考证（外部引用按四件套纪律补证后方可承重）。
3. **语义三分**：预览＝用户本地部署进 Agent 系统；部署＝发布到 git；发布到 Agent 平台市场＝人类另流操作，**出专家团职责边界**，不得在专家团内部或装配 skill 内部定义。

## 三、盘面冲击面（主理人登记，非裁定内容）

- `skills/software-orchestration/references/dev-discipline.md` L99-101（SRC4Z 语义校正句）现文＝单根模型（「`deliverables/` 只是 {root} 的末尾段」）——与双根裁定冲突，须随 PROJINIT 票面归并改写。
- `skills/software-orchestration/references/deploy-gate.md`（四段链 ②④ 段含「本地市场源」「register_expert.py 刷新＋宿主更新进缓存」）＋ `SKILL.md` L23 索引行——「部署」语义须改指发布到 git，「市场」类动作出边界；＝另案微票（架构席交卷后开，禁同席多实例）。
- `agent-experts/baigong-software-team/docs/PRODUCT.md` L75 仓面外指指针（前请示微票）＝并入本裁定处置域，不单列。
- PROJINIT rev2 在飞：锚定语义（swb-anchor/探针/租约/账本）一律锚开发面根；交付面不入建档与写保护面。

## 三之补·追加裁定（同日 18:0x·逐字）

> 和项目根一样，用户指定，在开发期间不需要提前引导用户，只有收到用户的交付相关指令的时候才需要根据用户指定的目录构建，并提供用户相关引导。

拆解：交付根 `{del_root}` 与项目根同规格＝**用户指定**；**开发期间不预建、不引导**；仅当收到用户交付相关指令时，按用户指定目录构成交付面并提供相应引导（lazy 建档）。**H-7 候裁由此销账**（del_root 锚定方式＝交付指令时用户指定＋lazy 构建，无需另裁）。

## 四、归并路径

- 向 arch-projinit1 发裁定增补令（rev2 吸收双根＋dev-discipline L99-101 冲突改写列随动项＋候裁 H-7 单列 {del_root} 锚定粒度）。
- git 交付仓机制＝派研究席考证，四件套引用呈报，不承重仅参照。
- deploy-gate 语义整改＝独立微票，候架构席 rev2 交卷后续开。
