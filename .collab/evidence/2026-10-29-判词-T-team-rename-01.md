# 判词：T-team-rename-01 两团百工全层改名整链复核（QA 席 fresh eyes 独立证伪）

> 席位：QA 席 qa-rename · 2026-10-29
> 条款真源：设计稿 v2 `.collab/design/2026-10-29-设计稿-两团百工改名-v2.md`；被审对象＝工程师回执 `.collab/evidence/2026-10-29-回执-team-rename-01.md`（含补录节）所报五批＋补 tag＋补刀。
> 方法＝全部当场复算（grep/git/python 实跑），不采信回执任何读数；红线＝三仓真源零修改（本席只读＋落本判词一件）。
> occurrence 口径沿用 v2 §三声明：「活面」＝grep 排除 `.git/`、`.collab/`、`.workbuddy/`、`.dev/`；「历史面」＝被排除目录内命中＋活面中标注沿革/原话/版本账行。

## 开端三仓 HEAD 读数（本席开工轮 `git rev-parse HEAD` 实测）

| 仓 | HEAD | tracked 状态 |
|---|---|---|
| devkits | `ae01181a210999c5981ac42fb9930ca8ca6859ee` | tracked clean（未跟踪仅 .collab/research 历史件） |
| experts | `87199fa8eaf454519fe1a034770c17127b6481fb` | tracked clean（未跟踪仅 .collab/.workbuddy） |
| skills | `0511b48dd12834c045c9739cd0b52fdb8cfe7a46` | clean |

与回执末态（devkits 回执落盘后 `ae01181`／experts `87199fa`／skills `0511b48`）及票面预期一致＝三仓锚定无漂移。

## 一、复核项逐条判读（七项全过）

### 1. 旧名残留清零 → 绿

双验＝①工作区 grep 活面扫描；②`git grep` tracked 内容面 commit 前后对比。

**id 旧名（`hjh-software-team|hjh-aigc-video-team`）活面读数**：
- skills＝**0**（全仓亦 0）；
- experts 活面仅 2 行＝bundle README:27（v1.5.0 沿革句·append-only 豁免）＋README:29（版本账 v2.0.0 append 行·含「旧→新」登记字样＝历史面新增）——与豁免清单逐行对上；
- devkits 活面仅 2 行＝bundle README:35（v2.0.0 append 行）＋README:37（v1.2.0 沿革句）——同上对上。

**中文旧名活面**：devkits `软件开发团队`＝2 行＝10-roles.md:49（原话引文＋〔原话引用·旧团名系史实逐字·机检豁免注〕在位，豁免注实测已加）＋README:35 append 行；experts `AIGC ?视频团队`＝README:27/:29 两豁免行；skills＝**0**。
**英文旧名（Software Company|Software Development Team|AIGC Video Team）活面**：devkits＝README:35 append 行 1；experts＝README:29 append 行 1；skills＝**0**。基线 19 行全改成立。

**git grep tracked 内容面 commit 差（可复算账）**：devkits 6d80232^＝135 → 8b2e6d1＝120（Δ15＝清单 16−版本账 append 含旧名 1，与回执口径声明吻合）；experts 42a157c^＝10 → HEAD＝2（Δ8，余 2＝两豁免行）；skills 0511b48^＝9 → HEAD＝**0**。
工作区全仓（含历史面）现值：devkits 328／experts 114／skills 0——experts 与回执 114 恰符；devkits 回执 325→今 328 差 3＝回执文件自身入库（cd214d0）与其后历史面增量，属时间移非活面漂移（主理人已裁「自算 Δ」口径，此处不判红）。

### 2. 新名一致性 → 绿

- 两 bundle plugin.json：name/plugin＝`baigong-software-team`／`baigong-video-team`；displayName/profession＝{en: Baigong Software Team／Baigong Video Team, zh: 百工软件团队／百工视频团队}；version＝2.0.0（两仓）。
- bundle.lock name/path/version/组件 ref 全新值：devkits eac 换 @v1.0.1；experts 六组件 @v1.3.1/@v1.7.1/@v1.3.1/@v1.4.1/@v1.4.1/@v1.3.1。
- 目录实测＝devkits `workbuddy/baigong-software-team`、experts `workbuddy/baigong-video-team`。
- SKILL frontmatter：六域 description 全「百工视频团队」＋version 全对（1.3.1/1.7.1/1.3.1/1.4.1/1.4.1/1.3.1）；fuxi 1.4.2；eac 1.0.1；software-orchestration 1.0.3。
- 席位 MD 英文自述抽验：experts 导演席:15「in the Baigong Video Team」、devkits 架构席:8「in the Baigong Software Team」＝新名；10-roles :25/:48＝「百工软件团队」。
- **bundle.lock ref→tag→commit 逐组件实测**：六新 tag＋fuxi@v1.4.2 全部解析→`0511b48`（存在且＝HEAD）；eac@v1.0.1→`6d80232`。全对上。
- 新名正查活面：devkits 双串合计 17 行（software 12＋video 5，＝v2 预判 16＋append 行 1，对账吻合）；experts＝9（恰符 v2 预判 9）；skills＝9（恰符 v2 预判 9）。

### 3. git mv 链 → 绿

- experts `git log --follow settings.json`：跨 `42a157c` rename 续接至起仓 `a3775cd`＝链不断；B2 commit 面 22 文件（含 rename 检出＋`.gitignore`/README 内容行）。
- devkits `--follow quick-mode.md`：跨 `8b2e6d1` 续接至 `d949160`＝链不断；`--follow plugin.json` 同样续接至 v1.3.0 时代。第三文件抽验达标（共抽 3 文件跨两仓）。
- experts `.gitignore:3`＝`workbuddy/baigong-video-team/.dev/`：`git check-ignore -v` 实测命中（exit 0）；`git status --porcelain` 零 `.dev` 泄入；`.dev/` 目录在位（含 perspective-design-v3-2026-10-28.md＝fuxi 锚目标文件随目录走，内容在）。最高危单点消窗实证成立。
- devkits `.gitignore:22` 注释行已随批改新 id 字面。

### 4. tag 链 → 绿

- skills 仓 tag 全列核：旧 tag 未移动（fuxi-skill@v1.4.1→`e6c776a`、@v1.4.0→`5d4d38e`、governance@v1.3.0→`b188fe2` 等沿前值原样在位）；新 tag 七组件＋fuxi 全部→`0511b48`。
- **补 tag `aigc-video-perspective@v1.3.0`**：`cat-file -t`＝`tag`（annotated 实体）、`%(objecttype) %(*objectname)`＝`tag e6c776ae…`——annotated 指向 `e6c776a` 核实无误。
- devkits：eac@v1.0（→5434578 旧值未动）＋eac@v1.0.1（→6d80232）在位；experts 仓仍零 tag＝v2 §4.2 判例照录。
- 旁注：skills 仓历史裸名 tag（content@v1.3.0/release@v1.3.0/visual@v1.3.0）＝早于组件名前缀惯例的既有旧账，非本批引入，不动＝合规。

### 5. 帽检/门禁/provenance 复算 → 绿

- **帽检独立重算（count_agent_tokens.py 实跑）全 12 席与回执逐一相符**：experts strategist 1889／director 2462／editor 2480／operations 2465／production-designer 2289／**screenwriter 2496（OK）**／lead 2496；devkits architect 1481／lead 2215／engineer 1872／pm 1075／qa 1380；脚本整体 exit 0。编剧席 2496≤2500＝补刀（87199fa·单 commit 单文件 1 行·父 42a157c 核实）生效，零回潮。
- **run-gates 两仓当场全跑**：devkits exit 0（GATE PASS·511 条路由②不拦·check-pack-structure BLOCK=0 WATCH=70·blind-eval BLOCK=0）；skills 薄启动器 exit 0（SOT=0 V8=0 STRUCT=0·WATCH=70 沿既有）。
- **SOT 双调项双绿**：默认双根（DEFAULT_PKG 新值实测＝`../multi-agent-collab-experts/workbuddy/baigong-video-team`）exit 0·BLOCK 0（新命中 0）；`--mode single --pkg workbuddy/baigong-software-team --tag softdev` exit 0·BLOCK 0。
- **check-provenance exit 0**（绿即静默）＋**fuxi 锚 sha 独立重算**：按 `normalize_clause→sha256` 口径对 contract-anchors.md MC-FX-V8-1 条款行重算＝`8f64e1a1…30e03`，与 check-truename.py:7 `spec_clause_sha256` 登记值逐字符相等＝锚面未翻红实证（B1 diff 实测只动 :8 静态锚路径段＋SKILL.md:52 同款，:37/:39/:43 条款锚行零触碰）。check-truename exit 0（VIOLATION 0·EXEMPT 95·SUBSTR 7——与回执逐项相符）。
- truename 两处改后行内容人工核：SKILL.md:52 与 contract-anchors.md:8 均＝「experts 仓 workbuddy/baigong-video-team/.dev/ 区 perspective-design-v3-2026-10-28.md·文字坐标不建跨仓文件指针」——路径合法、目标文件实测在位、契约措辞未变。

### 6. 装配冒烟复跑 → 绿

- 两 `publish.py --assemble` 当场重跑均 exit 0：软开＝「装配面已一致（第 1 块，40 文件）零写入」（幂等复跑＝确定性实证）；视频＝「已装配（第 2 块，110 文件，bundle@87199fa）」（自动锚到补刀后 HEAD＝链路活的）。
- -build 目录名＝新 id：`D:\multi-agent-collab-devkits-build\baigong-software-team\`＋`D:\multi-agent-collab-experts-build\baigong-video-team\`；-build 内 plugin.json 六字段读数＝两团全新值＋2.0.0（与真源一致）。ASSEMBLY.manifest bundle 锚＝8b2e6d1／87199fa。
- 文件计数口径注：`find` 计数 42／112＝publish 自报 40／110＋ASSEMBLY.manifest.json＋COPY.state 两件装配自身产物＝口径差非缺件（逐文件清单核对无缺）。旧名 -build 目录/zip 保留＝回滚备份口径，合规。
- **部署面零触碰核实**：`C:\Users\peter\.workbuddy\plugins\marketplaces\my-experts\plugins\` 两目录仍旧 id、marketplace.json `:6/:7/:12/:13` 仍旧 id 条目＝注册未动（票面明示此为边界非缺陷）✓。

### 7. 历史面零追改 → 绿

五批＋补刀 commit（0511b48/42a157c/6d80232/8b2e6d1/87199fa）`show --name-only` 逐一验＝**全部零触及** `.collab/`、`.workbuddy/`、`.dev/`。devkits 改名区间内 .collab 提交仅 cd214d0/ae01181 两件＝回执落盘/补录追加（A/M 仅回执文件本身＝证据登记非追改）；experts 区间内 .collab/.workbuddy 零提交（且两目录本就未跟踪）。历史面旧名原地未动。

## 二、红灯

**0 项。**

## 三、黄灯（登记不拦）

1. **绝对值账时移**：devkits 工作区全仓 id 旧名回执收口 325→本席复算 328（差 3＝回执文件入库及后续历史面增量）；v2 表值 296→340 同理。Δ 口径账（135→120→123 tracked）逐段对上＝非误伤非漏改。沿主理人「自算 Δ」裁，仅作口径注。
2. **-build 文件计数口径**：publish 自报（40/110）与磁盘 find（42/112）差＝装配自身两件（manifest＋COPY.state）。建议后续回执注明口径免误读。
3. **check-provenance 绿即静默**：exit 0 零输出，单看不自证跑过；本席以锚行 sha 独立重算补证。建议工具绿路径打一行计数摘要（卫生改进，非本票范围）。

## 四、对回执自报的偏差核查

回执全部关键读数（三仓 HEAD、Δ 账、新名 9/9/17、tag→commit 映射、帽检 12 席、门禁 exit 码、truename 95/7/0、装配 40/110 文件、plugin.json 六字段）经独立复算**零偏差**；补录节 87199fa 单文件单行、编剧席 2496、零回潮均实证成立。回执可信。

## 五、收口 status

- **status: PASS**（红 0 · 黄 3·登记候处置）
- 旧名活面残留读数一句话：**三仓活面旧 id／旧中文／旧英文残留＝除豁免清单逐行对上者外全部清零（skills 全仓 0；两 bundle 各仅版本账 append/沿革行；10-roles:49 原话豁免注在位）。**
- 本席触碰面＝仅本判词一件；三仓真源、tag、部署面零修改。
- 后续未动面（非缺陷）：B5 部署面重注册＝四段流程人类闸后另指示（marketplace.json 现仍旧 id＝注册未动的边界读数）。

（判词完 · QA 席 qa-rename · 落盘轮 devkits HEAD `ae01181`，本件＝新 HEAD 增量候选，入库与否由主理人裁）
