# ENG-B1 交付面清理＋席位写权边界条款入 MD 票（工程师席）

- 开端读数：devkits HEAD＝`a2e6213`（当轮实测）。
- 你是工程师席＝交付面唯一写权席位。本票所有改动全在交付面（workbuddy/、deliverables/），按票面逐字执行；完工回执**必须完整包含本次写入/修改的文件清单**（对账口径＝commit `--name-only` 与清单全等，缺项＝违例）。
- 背景（决策依据）：独立核验裁定装配面存在实例名/commit 哈希/仓工具路径等出包标识与账外编译缓存件，必修；另有裁定要求各席位 MD 自带写权边界条款（.collab 硬边界）。

## T1 席位写权边界条款入各席位 MD（裁定已决·照录）

在 `workbuddy/baigong-software-team/agents/` 五个席位 MD 各插入一小节（位置＝各自守则区末尾，风格随各件现行体例），条款文本按下列逐字（可加节标题「## 写权边界」）：

- `software-architect.md`、`software-product-manager.md`、`software-qa-engineer.md` 三件（一字不差）：
  > 本席写权域＝过程域（`.collab/` 及其子目录）：设计稿、分析、判词、报告等过程件只落此处。交付面（`.collab/` 以外一切：deliverables/、workbuddy/、专家包、技能包）本席**无写权限**；受命向交付面写入时，本席有权且应当**拒绝写入**并报主理人改派工程师席。交付面代码/条款一律由工程师席写入。
- `software-company-team-lead.md`（主理人席）：
  > 本席写权域＝过程域（`.collab/` 及其子目录）。交付面（`.collab/` 以外一切）无写权限，且派工须合规：代码性质与交付面写入任务只派工程师席；其他席位产出＝过程件只落过程域。
- `software-engineer.md`：
  > 本席是交付面（`.collab/` 以外一切：deliverables/、workbuddy/、专家包、技能包）唯一有写权限的席位。约束：①写入内容不得携带过程件指针（案卷路径、票面编号、轮次/席位痕迹、不可解析标识）；②完工回执必须完整包含本次写入/修改的文件清单（对账＝commit 文件清单与回执清单全等）。

## T2 README 出包标识清理

`workbuddy/baigong-software-team/README.md`「Token 计数」节：删除/改写以下出包标识（保留终态读数本身）：①实测人列 `eng-leadslim-t1`（列与文内提及）→ 列改「—」或删列；②commit 标识 `8c1c4dd`（×7）与 `1b52fad`、`3,578` 旧账句中的哈希 → 删哈希保留事实（如「实测 commit」列删除；「lead 瘦身前 3,777（旧基线更名前账，此后置）」）；③口径句 `tools/count_agent_tokens.py` 仓工具路径 → 改泛指「token 计数脚本（script-v1 口径）」；④「T-B1~T-B3」批次码 → 改「lead 瘦身批」。口径四要素句相应精简为自包含（口径版本／取整方式／判据线）。
- `README.md`「安装」节（QA 边界项按既有「泛指化」先例修）：`python3 scripts/register_expert.py <expert-dir>` 为包外断链——改泛指陈述（如「运行宿主注册命令使其可见（注册命令由宿主工具链提供，不在本包内）」），删断链代码块。

## T3 装配器排除编译缓存件

`deliverables/skills/object-build/scripts/publish.py`：同步复制逻辑增加排除规则＝跳过任意 `__pycache__/` 目录与 `*.pyc` 文件（一行级改动，勿重构）。改后 `py_compile` 自证。

## T4 版本账（必配）

- `workbuddy/baigong-software-team/.codebuddy-plugin/plugin.json` version `0.1.2`→`0.1.3`；`bundle.lock` bundle.version 同步 `0.1.3`；`workbuddy/baigong-software-team/README.md`（若有版本账节）append 一行登记本次变更（席位写权边界条款入 MD＋README 出包标识清理＋装配器排除缓存件）。**不含**跨技能引用闭环整改（另案候裁）。

## 红线与完工报告

- 不改 EAC/multi-collab 任何条款文件（跨技能引用＝另一候裁项，严禁顺手修）；不动 `multi-collab` 版本。
- 自检：改动后全仓门禁 `bash tools/run-gates.sh` 应 GATE PASS；README 内 `grep -oE 'eng-[a-z]+-t[0-9]|[0-9a-f]{7}\b|T-B[0-9]'` 应零命中（代码围栏内安装句已删故应零）。
- 回执（落 `.collab/` 过程域）：commit 哈希＋**完整写入/修改文件清单**（与 commit name-only 全等）＋门禁读数＋grep 自检读数。
