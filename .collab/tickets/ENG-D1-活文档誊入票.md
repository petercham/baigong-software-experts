# ENG-D1 百工团活文档誊入票（工程师席·交付面写入）

- 开端读数：devkits HEAD 以本票 commit 实测为准。
- 声明闭集：
  - `workbuddy/baigong-software-team/PRODUCT.md`（新建）
  - `workbuddy/baigong-software-team/ARCHITECTURE.md`（新建）
  - `workbuddy/baigong-software-team/.codebuddy-plugin/plugin.json`
  - `workbuddy/baigong-software-team/bundle.lock`
  - `workbuddy/baigong-software-team/README.md`
- 背景（自包含）：百工软件团队 bundle 自 fork 以来无产品/架构活文档，本次补齐两件。内容真源＝起草件两件（产品席/架构席各自产出·已 commit `846b77b` 入库），正文已过洁净自查（零盘符、零案面指针、涉包内机制一律包内相对路径）。誊入规则＝正文逐字照起草件，仅**整节删除文末「取证」节**（PRODUCT L82 起、ARCHITECTURE L240 起至节末；ARCHITECTURE 头部引言行内「载体见文末取证节」短语随删改顺——该引言行整体删除或去掉括注半句，保持行文通顺，除此零改写）。references 卷数口径＝十卷（两席独立实测一致），不得写"十一卷"。
- HOLD：无。

## T1 PRODUCT.md 新建

正文＝起草件 `.collab/design/2026-10-30-baigong-team-PRODUCT.md`（blob `846b77b` 版）全文，删除「## 取证（誊入交付包时删除本节；正文自包含）」整节（含其下所有行）。文件其余逐字照录。

**指针归一（誊入时统一口径·两文件通用）**：两文件落位 bundle 根，一切反引号文件指针必须**从 bundle 根可解析**——`references/xxx.md` 形态一律改写为 `skills/software-orchestration/references/xxx.md`（PRODUCT 实测含 8 处短形：bugfix-path/deploy-gate/dev-discipline/handoff-discipline/incremental-dev/partial-workflows/quick-mode/standard-sop；ARCHITECTURE 实测含 10 处短形含 collab-rules/delivery-summary）；短形→长形一一对应无歧义，属形态归一非内容改写。归一后跑 check-pointer-closure 须零违例。`plugin.json` 裸形（ARCH 一处）改 `.codebuddy-plugin/plugin.json` 同口径。

## T2 ARCHITECTURE.md 新建

正文＝起草件 `.collab/design/2026-10-30-baigong-team-ARCHITECTURE.md`（blob `846b77b` 版）全文，删除「## 取证（誊入交付面时整节删除）」整节；首行引言区涉「载体见文末『取证』节，誊入交付面时整节删除」括注一并去除（该句其余部分保留通顺）。文件其余逐字照录。T1 指针归一口径同样适用本文件。

## T3 版本账

- `plugin.json`＋`bundle.lock`：`0.1.10`→`0.1.11`；
- `README.md` 版本账 append 一行（体例随现行账行·自包含措辞，参考）：

> **版本账 v0.1.11**（2026-10-30·活文档批）：包内新增 `PRODUCT.md`（产品设计说明书：定位／用户与场景／五档能力地图／五席价值主张／质量承诺／非目标／交付形态）＋`ARCHITECTURE.md`（架构设计文档：编制图／席位三层与写权模型／技能包分卷地图／装配与版本架构／门禁架构／关键设计决策／演进边界）——两份为活文档，后续随批更新；plugin.json＋bundle.lock 双 0.1.11（纪律①每变必 bump·同源镜像）。

## 自检与回执（N4 附载体）

- 誊入忠实度：PRODUCT/ARCHITECTURE 正文与起草件 blob 逐字比对＝除删节外零差（附脚本读数）；
- 新文件指针扫描：`check-pointer-closure.py` 对 bundle 面运行＝两新文件包内相对指针全部可达零新增违例（附读数；涉 `skills/...` 相对路径须能在包根解析）；
- 禁列终式 `见?第\s*\d+\s*轮|轮次戳|〔[^〕]*·轮〕|轮次号[：:]` 对两新文件扫描三分账；
- run-gates GATE PASS；版本前后值实测（0.1.10→0.1.11）；
- 回执落 `D:\multi-agent-collab-devkits\.collab\research\2026-10-30-ENG-D1-工程师回执-v1.md`，单独 commit（前缀 `collab:`）；禁 --no-verify／禁 amend。

## 红线

只动闭集五件；起草件两件（.collab/design/）零触碰；席位 MD/skills 各卷零触碰；正文除声明的删节外一字不改——对正文内容有异议停手上报（内容属产品席/架构席起草面）。
