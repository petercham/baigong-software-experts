# REMOTE-PUB 远端上架规划票 v1（架构席·过程件·零代码零交付面写入）

- 开端读数：devkits HEAD 票首实测 `5dbc4c5`（2026-11-05 起草时 `git rev-parse --short HEAD`，main 分支）。本票 commit 笔号随回执另报。
- 背景（决策依据·自包含）：皮总口径（L1·已拍·不得复议）：「本地市场源注册＋平台刷活动安装版＝预览；真正的部署＝发布到对应的平台市场。」既有四段链（装配→预览→人类闸→本地转正，见 `agent-experts/baigong-software-team/skills/software-orchestration/references/deploy-gate.md` §五）只覆盖本地段；远端平台市场上架＝本票规划的缺失段。远端发布线已获皮总发话启动（2026-11-05 21:1x「发布到 WorkBuddy 及不同平台市场算部署」）。
- 调研事实引用口径：票内引用 Explore 席 2026-11-05 调研结论＋本票起草时架构席本机复测读数（复测命令与读数随条款给出），不重查、不引用账本外状态源。
- 改动面闭集＝1 件：本票文件自身（`.scratch/tickets/2026-11-05-REMOTE-PUB-远端上架规划票-v1.md`）。本票＝规划件，后续施工另立票。
- 声明闭集：
  - `agent-experts/baigong-software-team/.scratch/tickets/2026-11-05-REMOTE-PUB-远端上架规划票-v1.md`

---

## §〇 既有事实登记（调研已证＋架构席复测，后续票直接引用）

F1. 提交通道＝open.workbuddy.cn 网页三段向导（上传 .zip ≤20MB → 确认市场展示信息 → 提交审核）；**无任何 CLI/API 自动提交通道**；官方 expert-manager 技能脚本止步于本地 validate/package。
F2. 审核＝安全扫描＋AI 审核＋人工抽检，≤7 工作日出结果；驳回附原因与安全检测报告（tix.qq.com），可修改重提。账号开发者认证（身份证/人脸核身或营业执照）＝只能人类亲为。收费决策（免费/付费）上架后不可逆。
F3. 上架包硬规范：`.codebuddy-plugin/plugin.json` 必须在；team 型包根必须有 `settings.json`；`hooks/`、`commands/`、`.lsp.json`＝违禁（官方 validate_expert.py 第 294-299 行实证在位，本票复测命中该段原文）；frontmatter 禁 tools 字段；tags/quickPrompts/defaultInitPrompt 均固定 3 个；defaultInitPrompt 须＝quickPrompts[0]；displayDescription.zh 须 40-50 字；头像 PNG 512×512 ≤500KB。
F4. 架构席复测读数（起草时实测，命令可复跑）：
   - `sha256sum` 于 `agent-experts/baigong-software-team/`：仓根 `plugin.json` ＝ `316486f98746f3b7…`；市场源部署面 `.codebuddy-plugin/plugin.json` ＝ `a14c9bf5d0aac29f…`（两处不同源坐实）。
   - 仓根：`name="software-team"`、无 `defaultInitPrompt` 字段、`author.email="baigong@example.invalid"`；部署面：`name="baigong-software-team"`、有 `defaultInitPrompt`、`author.email="petercham@users.noreply.github.com"`。**author 两处亦不同源**（漂移第三证）。
   - 两处共同项：`version=0.1.27`、`quickPrompts` 均 6 条、`displayDescription.zh` 均 179 字。
   - `hooks/hooks.json` 在位（结构＝`_spec/_anchors/hooks` 三键，纯事件→脚本路由登记）；`config/seat-permissions.json`、`config/seat-permissions-hooks-map.json` 在位。
   - `bundle.lock` 顶层键含 `assembly_exclude`（装配排除机制在册，§B-4 处置通道依赖此机制）。
F5. 我方装配器＝`agent-skills/object-build/scripts/publish.py`（`--assemble` 产装配面含 `.codebuddy-plugin/`＋manifest＋COPY.state，现 81 件）；官方 `package_expert.py` 先跑 validate 再 zipfile 打包，只跳隐藏文件与 `__pycache__/node_modules`——`docs/`、`config/`、`ASSEMBLY.manifest.json`、`COPY.state` 会全进 zip。

---

## §A 上架取料面定源（架构域结论，非候裁）

**A-1 定源结论：上架 zip 唯一取料＝`publish.py --assemble` 装配面的下游导出（经 §C 上架打包步裁剪），禁止任何人工拼料、禁止从仓根或市场源目录直接压 zip。**

链路定形：`仓（git 真源） --publish.py 发布--> 市场源部署面 --publish.py --assemble--> 装配面 --pre-publish 裁剪步--> 上架暂存面 --官方 validate_expert.py--> zip`。

**A-2 真源判据（plugin.json 两处不同源＝316486f9 ≠ a14c9bf5 的处置）**：

1. 唯一真源＝**仓根 `agent-experts/baigong-software-team/plugin.json`**（git 在册件）。市场源部署面 `.codebuddy-plugin/plugin.json` 只能是 `publish.py` 的逐字产物，不得手改。
2. 市场条目名基线＝`baigong-software-team`（现行市场条目名＋目录名，不改）。据此仓根 `plugin.json` 的 `name` 须由 `software-team` 改 `baigong-software-team`（归 §B-2 整改票 T1）。
3. 漂移清零判据（可机械验证）：整改后跑 `publish.py --check`（五态报告）＝无漂移绿；且
   `sha256sum agent-experts/baigong-software-team/plugin.json agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json` 两值全等。
4. author 两处不同源同法处置：真源改仓根，部署面随发布跟随，不单独改市场源侧。

---

## §B 六缺口整改规格（逐条到落位＋机械判据）

落位面：以下 T1-T6 全部改**仓根真源**（§A-2 纪律），市场源部署面经 `publish.py` 发布跟随，装配面经 `--assemble` 重出。判据中的 `<pkg>` ＝ `agent-experts/baigong-software-team`。

**B-1（缺口①）quickPrompts 6→3**：
- 选择判据（闭集三能力面覆盖）：a) 主链路＝标准流程全跑（现 index 0）；b) 独立复审＝差异化卖点（现 index 1）；c) 部署/上线段＝本专家团区别于普通开发团的独有承诺（现 index 4「按四段链上到预览」那条）。现 index 2（外部顾问）、3（调研）、5（轻量维护）裁掉。
- 选择后 index 0 不动＝保持「我有一个开发需求，请按标准流程走一遍…」为首位（喂 B-2 机械式）。
- 判据：`python -c "import json,sys;d=json.load(open('<pkg>/.codebuddy-plugin/plugin.json',encoding='utf-8'));assert len(d['quickPrompts'])==3"` 退出码 0。仓根同式同判。

**B-2（缺口②）defaultInitPrompt 补齐＋机械式**：
- 规格：整改后两文件均含 `defaultInitPrompt` 字段，且其值**逐字＝该文件 `quickPrompts[0]` 的 zh 值**（机械式，禁独立措辞）。现部署面既有值（「我是项目负责人包好用…」）作废重写。
- 判据：`python -c "import json;d=json.load(open(P,encoding='utf-8'));assert d['defaultInitPrompt']==d['quickPrompts'][0] or d['defaultInitPrompt']['zh']==d['quickPrompts'][0]['zh']"`（按实际字段形态取对应式，整改票内定形）退出码 0，两文件都跑。
- 同票附带：仓根 `name` `software-team`→`baigong-software-team`（§A-2-2）。

**B-3（缺口③）displayDescription.zh 179→40-50 字**：
- 重写口径：一句话覆盖「四席协作＋标准流程到独立验收＋全程留证」三要素；字数＝python `len()` 对 zh 字符串计数（含标点），40≤len≤50。
- 架构席候补句（45 字·终值由产品席出稿、整改票内定稿，架构不越内容域终审）：「百工软件团队：产品、架构、工程、QA 四席协作，按标准流程从需求到独立验收，每步留判定证据。」
- 判据：`python -c "import json;d=json.load(open(P,encoding='utf-8'));s=d['displayDescription']['zh'];assert 40<=len(s)<=50"` 退出码 0。

**B-4（缺口④·本票核心架构决策）hooks/ 违禁处置——选项表＋倾向**：

处置面澄清：执法钩子（`hooks/hooks.json`＋`config/seat-permissions*.json`）＝本地版的系统执法件，功能不可弃；违禁的是**上架 zip 内出现 `hooks/` 目录**。故选项只裁「上架 zip 内执法面形态」，本地装配面保留全量执法。

| 选项 | 内容 | 功能损失 | 风险 |
|---|---|---|---|
| 甲 | 上架 zip 剔除 `hooks/`，保留 `config/seat-permissions*.json`（钩子不激活，配置成死数据） | 无远端执法（同乙丙） | **虚假可供性**：包内留有权限配置而无执法，买家误以为有门禁；validate 虽不禁 config/ 但语义自相矛盾 |
| 乙 | 钩子判定逻辑迁入技能 references 装载说明（指令层模拟权限纪律） | 机械执法→纯指令自觉，G1 事前阻断类保证全失效 | 指令可被无视＝与「写必经租约·越界被拒」的原设计宣称不符；改动面大（动交付面 skills） |
| 丙 | 上架版＝**无执法钩子降级变体**：`hooks/`＋`config/seat-permissions-hooks-map.json`＋`config/seat-permissions.json` 整组从上架 zip 剔除（装配/本地面全量保留）；README 上架版如实声明「远端版不含写侧门禁钩子，门禁纪律为流程性约束」 | 无远端执法 | 最低：zip 无自相矛盾件；本地版功能零损失；诚实申报降级面 |

**架构席倾向（L2 域内结论）＝丙**。理由：违禁项整组剔除后 zip 内容自洽；`bundle.lock` 既有 `assembly_exclude` 机制但**不得用于本项**（装配面同时服务本地转正，剔除会废本地执法），剔除落在 §C pre-publish 裁剪步的「上架剔除闭集」，与装配面解耦。上架剔除闭集（目录级·相对上架暂存面根）＝`hooks/`、`config/seat-permissions.json`、`config/seat-permissions-hooks-map.json`。
- 判据：上架暂存面 `test ! -e <暂存面>/hooks && test ! -e <暂存面>/config/seat-permissions.json && test ! -e <暂存面>/config/seat-permissions-hooks-map.json` 退出码 0；官方 `validate_expert.py` 对暂存面跑出 0 error；装配面反向断言 `test -e <装配面>/hooks/hooks.json` 存在（本地执法件未误删）。

**B-5（缺口⑤）上架 zip 清单定源**：
- 规格：zip 根必须含 `.codebuddy-plugin/plugin.json`（取料＝装配面，装配面已含该目录，F5 实证）；打包步＝§C pre-publish 脚本，zip 内路径相对暂存面根。
- 判据：`unzip -l <上架zip> | grep -c '^[^ ]* *[0-9]* *[^ ]* \.codebuddy-plugin/plugin\.json$'` ≥1（或按 unzip 列式等价 grep，打包票内定形）；且官方 validate 对解包面 0 error。

**B-6（缺口⑥）settings.json 入包确认**：
- 规格：仓根 `settings.json` 在位（实测已在）；确认其在 `publish.py` 发布清单＋装配面＋上架暂存面三级均在（team 型包根硬要求）。若现清单未含，整改票把它入仓根清单。
- 判据：`test -f <暂存面根>/settings.json` 退出码 0（装配面同式）。

软项（不列缺口、随整改票顺做）：README.md＝推荐项，上架版 README 按 B-4 丙案加降级声明行；`author.email` 占位域名 `baigong@example.invalid` 换真实邮箱＝**值候皮总供给**（§G-4），字段落位归整改票。

---

## §C 打包与机检管线（架构域结论）

**C-1 机检闸：复用官方 `validate_expert.py` 只读校验，作为上架前强制闸**；复用面＝对「上架暂存面」跑，0 error 方可压 zip。**不复用官方 `package_expert.py` 作打包器**——它把 `docs/`、`ASSEMBLY.manifest.json`、`COPY.state` 等非必要件全进 zip（F5），且不含我方上架剔除闭集。
**C-2 自研 `pre-publish` 脚本**（归施工票 TK-4，落点建议 `agent-skills/object-build/scripts/pre_publish.py`，与 publish.py 同族）：输入＝装配面（`--assemble` 产物）；步骤＝复制暂存面→按 §B-4 上架剔除闭集＋§C-3 剔除非必要件→跑官方 validate→zip 落盘→体积判据。是否入 run-gates 家族＝暂不入（run-gates ＝仓内开发闸家族，pre-publish 是一次性上架工序步，非每次 commit 必跑），但在 pre-publish 内部调用 run-gates 全绿作为前置。
**C-3 zip 内容闭集（剔除面清单，相对暂存面根）**：`COPY.state`、`ASSEMBLY.manifest.json`、`tests/`、`.scratch/`（若装配面带）、`hooks/`、`config/seat-permissions.json`、`config/seat-permissions-hooks-map.json`。保留面＝其余全量（skills/、agents/、docs/、avatars/、settings.json、README.md、plugin.json、.codebuddy-plugin/）。docs/ 保留理由：技能 references 装载依赖，剔除即功能损失。
- 判据：`unzip -l <上架zip>` 行集与剔除闭集 `grep -E '(COPY\.state|ASSEMBLY\.manifest\.json|^.* tests/|hooks/|seat-permissions)'` 命中数＝0。
**C-4 体积判据**：`stat -c%s <上架zip>` ≤ 20,971,520（20MB 按 20×1024×1024 从严取值）；头像六张已实测达标（调研事实），预期无压力，超限即红项停手。

---

## §D deploy-gate 成文扩段（条款草案·append-only·落点归 TK-5 施工票）

落点：`agent-experts/baigong-software-team/skills/software-orchestration/references/deploy-gate.md` 文末追加 §六，不回改既有行。草案逐字：

> ## 六、第五段：远端上架（2026-11-05 皮总口径：「发布到 WorkBuddy 及不同平台市场算部署」）
>
> 四段链（装配→预览→人类闸→本地转正）收口后，**远端平台市场上架＝链外第五段**，独立立票＋逐闸人工，不得并入四段链任何一段的收口判词。
>
> | 闸 | 内容 | 闸主 |
> |---|---|---|
> | 上架拍板 | 是否上架、上哪个平台、包版本 | 决策者（呈拍面） |
> | 开发者认证 | 身份证/人脸核身或营业执照认证 | 人类亲为（无可自动化通道） |
> | 上传操作 | open.workbuddy.cn 三段向导上传 zip（≤20MB） | 人类亲为（无 CLI/API 通道） |
> | 审核应答 | ≤7 工作日出结果；驳回读 tix.qq.com 检测报告→回施工票修改重提 | 主理人编排＋人类提交 |
> | 收费决策 | 免费/付费，**上架后不可逆** | 决策者保留闸 |
>
> 版本维护：远端发布后任何整改＝本地链重走四段＋新版本号重传（发布管理重传），禁止直接改线上包；远端版本与仓内版本同源对账归日终对账面。

---

## §E 分票计划（施工票序列·依赖序）

| 票号 | 范围一句话 | 依赖 |
|---|---|---|
| RP-TK1 | 真源对账票：仓根 plugin.json 定源（name 改 baigong-software-team＋author 落位框架），publish.py 发布跟随，`--check` 清零＋两文件 sha256 全等 | 无（首票） |
| RP-TK2 | 合规整改票（plugin.json 字段族）：quickPrompts 三选三、defaultInitPrompt 机械式、displayDescription.zh 40-50 字终稿、author 邮箱真值（候 §G-4） | RP-TK1 |
| RP-TK3 | hooks 处置票（丙案）：上架剔除闭集定义入 pre-publish 规格＋README 上架版降级声明行 | RP-TK1（与 TK2 可并行） |
| RP-TK4 | 打包机检票：`pre_publish.py` 落盘（§C 全部判据内建）＋首跑产出上架 zip 全绿 | RP-TK2＋RP-TK3 |
| RP-TK5 | deploy-gate 成文票：§D 草案 append-only 落盘 | 无（可与 TK2/TK3 并行；建议先于 RP-TK6，上架动作须成文闸在先） |
| RP-TK6 | 上架伴随指引件：人类闸操作指引（账号认证步骤→上传→审核应答→收费决策呈拍模板），过程件居 `.collab/refs/` | RP-TK4＋RP-TK5 |

串行主链：TK1 → TK2/TK3（并行）→ TK4 → TK6；TK5 并行插入。

---

## §F 版本线建议

整改落地＝`0.1.27 → 0.1.29` bump 口径：仓根 plugin.json、市场源部署面 `.codebuddy-plugin/plugin.json`、（上架后）市场条目三同源。三同源纪律在册（publish.py 逐字发布＋`--check` 漂移检测机械保证），bump 随 RP-TK2 回执登记前后值各附实测 grep 读数。

> 版本号口径修正（2026-11-05 22:0x 皮总裁定头像文字换代＝AV-FIX 票·BugFix 快捷路径，0.1.28 由该批三同源先行占用）：本票 F 段原「0.1.28」顺延 **0.1.29**——真源对账/字段族/hooks/pre_publish 整改批一律按 **0.1.29** 记账。〔v1.1 修正笔，依主理人通知〕

---

## §G 候裁单列（呈拍面闭集·仅决策者保留闸项）

1. **是否上架拍板**：本规划票落盘≠上架授权；RP-TK6 后正式呈拍。
2. **收费口径**：免费/付费，上架后不可逆。
3. **开发者账号主体**：身份证/人脸核身个人认证 或 营业执照企业认证。
4. **author 邮箱真值**：替换 `baigong@example.invalid` 占位的实际邮箱值。

（取料面 §A、hooks 方案 §B-4-丙、打包管线 §C＝架构域结论，不进候裁。）

---

## §H 禁动面

- 业务 bundle（视频团等）：零触碰。
- GitHub 远端：零 push、零发布物外传。
- 交付面代码/配置/文档文件：本票零写入（§B/§D 全部为后续票条款草案，本票只落票文件一件）。

---

## 自检与回执

- 票首 HEAD 读数＝`5dbc4c5` 实测（见开端读数）。
- F4 各断言附复测命令（sha256sum/python json 断言/test），非转述即复跑可验。
- F11 禁列过程痕迹 grep 终式 `见?第\s*\d+\s*轮|轮次戳|〔[^〕]*·轮〕|轮次号[：:]` 对本票命中＝0（三分账登记：全免）。
- 候裁面实测 4 条，全部属保留闸（§G）。
- commit：`collab:` 前缀单票笔，pathspec 限定本票文件，无 --no-verify、无 amend；笔号随回执报 team-lead。

## 红线

- 闭集外零触碰；§〇 事实与实测读数有异议停手上报；append-only 不回改既有行（§D 草案落盘时）。
- 后续施工票未立未批前，架构席本人不动任何交付面。
