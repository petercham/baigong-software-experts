# STRUCTURE.md 存量清查（架构席 v1·只读零施工）

- 票据：皮总（2026-11-05 16:55）拍②＝STRUCTURE.md 一次性存量人工清查（ADR-L0 调研 v1 §2.3 案一落地）
- 开工 HEAD 实测：`ebdb8b4`（`git rev-parse --short HEAD`，main）；开工工作区我席名下净（`?? .collab/ledger/` 他席在途未触碰）
- 性质：只读审查·零施工（未修任何 STRUCTURE 文件）；occurrence 口径＝每份附声明条目＋ls/git ls-files 双验读数（ebdb8b4 态实测）
- 范围：仓根＋七份 STRUCTURE 实物（`git ls-files "*STRUCTURE.md"`＝7 命中：bundle 1＋agent-skills 6）
- 漂移分类三型＝①声明领先实装（declared∉实存）②实态领先声明（实存∉declared）③措辞漂移（语义不合拍）；分级＝必修（声明误导后续动作）／随正（惯例未宣）／观察（登记不追）

## 〇、仓根面（无 STRUCTURE 实物）

- 实读＝仓根无 `docs/`、无 `docs/STRUCTURE.md`（`ls docs/` 空返回、`ls docs/STRUCTURE.md` 无）；仓根顶层＝`README.md`＋`agent-experts/ agent-skills/ softwares/ tools/`＋`.collab/ .scratch/`。
- 定性＝**仓根治理层无 STRUCTURE 声明面属既成设计**：仓根层文件域真源＝`.gitignore`（SWB-B5 全量重写·两制入库面/排除面自注「是否进 git 由本文件显式声明」）＋三分类目录面（check-entity SCAN_ROOT_DIRS＝agent-*/softwares）。不算漂移；登记一条观察（见 §三 O-2：仓根 decisions/design/research 等治理桶的目录闭集真源＝`skills/sop/references/collab-fixed-structure.md` 十一桶，但仅在 bundle 技能内，仓根无本地镜像——跨层引用可解但 STRUCTURE 化缺位）。
- 涉 ADR-L0 在途＝`agent-experts/baigong-software-team/docs/adr/` 将由该批初始化——相关漂移按派工令②**批后终态标注候裁不判红**（见 §一.1）。

## 一、逐份清查（7 份）

### 1. `agent-experts/baigong-software-team/docs/STRUCTURE.md`（bundle）

声明条目：六目录（agents/skills/config/hooks/tests/avatars）＋`docs/adr/` 条目＋yaml delivery_paths 六目录行。
实态顶层（ls）：`README.md agents/ avatars/ bundle.lock config/ docs/ hooks/ plugin.json settings.json skills/ tests/`；docs/ 实态＝`ARCHITECTURE.md PRODUCT.md STRUCTURE.md SWB-交接件v2.9-…md`（git ls-files 双验同）。

| 漂移 | 型 | 级 | 处置建议 |
|---|---|---|---|
| `docs/adr/` 声明在位、目录不存在（L11）＝红-2 活例 | ① | **候裁（批后终态）** | ADR-L0 同批初始化后自动消解；若该批未落＝升必修补目录或删声明行。**本清查不判红**（派工令②） |
| 顶层 `README.md`／`plugin.json`／`bundle.lock`／`settings.json` 四件未声明 | ② | 随正 | 属装配元数据/版本账/宿主配置族；建议补一行「装配元数据与宿主配置文件（plugin.json/bundle.lock/settings.json）＋仓侧版本账（README）＝非枚举惯例件」豁免措辞句（与 §三 C-3 草案防误报联动） |
| docs/ 内交接件 v2.9 登记件未枚举 | — | 不算 | docs 面＝项目文档面不逐件枚举（声明体例如此），史实锚名册件另有登记面 |

delivery_paths yaml 六目录 ↔ seat-permissions deny 六目录行同源对账＝在位一致（ES 批既有断言 A1-J4 面），零漂移。

### 2. `agent-skills/bundle-assembly-registration/docs/STRUCTURE.md`

声明＝SKILL.md＋references/；实态＝`SKILL.md docs/ references/`。**零漂移**（七份中最干净，可作对照基准样板）。

### 3. `agent-skills/external-advisor-collab/docs/STRUCTURE.md`

声明＝SKILL.md＋references/；实态＝`SKILL.md docs/ references/ sources/`。

| 漂移 | 型 | 级 | 处置建议 |
|---|---|---|---|
| `sources/` 实存未声明（实体＝`sources/spec-anchors.md` git 面在位） | ② | **必修** | `sources/`＝dev-discipline §二.5「唯一允许进交付物的自包含料源」＝交付组件本体（CLN-PURE 批 spec_file 锚迁此件），声明面缺它＝delivery_paths 少一条装配/授权射程；补条目行＋yaml 随动 |

### 4. `agent-skills/fuxi-skill/docs/STRUCTURE.md`（**最大漂移**）

声明＝SKILL.md＋references/＋products/（yaml 同三条）。
实态（ls＋git ls-files 双验）＝`README.md adapters/ contracts/ docs/ gates/ products/ rejected/ specs/`＋`.collab/ .scratch/`——**`SKILL.md` 与 `references/` 均不存在**（`git ls-files agent-skills/fuxi-skill/SKILL.md` 空返回），实存六目录（adapters/contracts/gates/specs/rejected/README.md）全部未声明；仅 `products/` 声明↔实存吻合。

| 漂移 | 型 | 级 | 处置建议 |
|---|---|---|---|
| 声明 SKILL.md/references/ 不存在＝delivery_paths 两条指向虚件 | ① | **必修** | 该包已解冻续推（FUXI 解冻拍板在 decisions），若入装配或租约射程则 delivery_paths 全虚；重写声明段与 yaml 对齐实态（SKILL.md 若为规划态＝须标「规划未落」注记或删） |
| 六实存目录未声明 | ② | **必修** | 同上批重写：contracts/（契约真源）＋gates/（assert-tool 机件面，ST-9 断言实体）＋adapters/specs/rejected 逐条定位入声明 |
| 处置路径 | — | — | 建议随下一 FUXI 维护票带「STRUCTURE 重写」子目（一行动作级），不另立票 |

### 5. `agent-skills/multi-collab/docs/STRUCTURE.md`

声明＝SKILL.md＋references/；实态＝`COPY.state SKILL.md docs/ references/`。

| 漂移 | 型 | 级 | 处置建议 |
|---|---|---|---|
| `COPY.state` 未声明 | ② | 随正 | 装配哈希账件（CLN-PURE §口径3 白名单已认其「账件本体」身份）＝生成物不枚举惯例；并入 §三统一措辞句 |

### 6. `agent-skills/object-audit/docs/STRUCTURE.md`

声明＝SKILL.md＋references/＋scripts/＋tests/；实态＝声明四条＋`COPY.state`＋docs/ 全吻合。

| 漂移 | 型 | 级 | 处置建议 |
|---|---|---|---|
| `COPY.state` 未声明 | ② | 随正 | 同 #5 并入统一措辞句 |

附注（非 STRUCTURE 漂移）：ADR-L0 修订笔已定 check-adr 定位四序含「③缺省自解 bundle.lock」——object-audit scripts/ 声明面已覆盖新脚本落位，零随动需求。

### 7. `agent-skills/object-build/docs/STRUCTURE.md`

声明＝SKILL.md＋references/；实态＝`COPY.state SKILL.md docs/ references/ scripts/`。

| 漂移 | 型 | 级 | 处置建议 |
|---|---|---|---|
| `scripts/` 实存未声明（实体＝`scripts/publish.py` git 面在位＝装配器本体） | ② | **必修** | publish.py＝run-gates 外挂与 CLN-PURE assembly_exclude 的执行主体＝核心交付组件缺声明；补条目行＋yaml 随动（object-audit 已宣 scripts/ 同族先例现成） |
| `COPY.state` 未声明 | ② | 随正 | 并入统一措辞句 |

## 二、计数摘要

- 清查面：STRUCTURE 实物 **7/7 逐份**（声明条目 24 条／yaml 路径 20 行全核）＋仓根面 1（无实物定性登记）；
- 漂移总账：**必修 4 条**（fuxi 双向 2＋EAC sources/＋object-build scripts/）／**随正 5 条**（COPY.state×3＋bundle 顶层四件一句＋软性）／**观察 3 条**（O-1 docs/adr 批后终态候裁、O-2 仓根 STRUCTURE 化缺位、O-3 softwares/ 壳无 STRUCTURE——`ls softwares/` 仅 README.md，探针锚缺位走 write-guard fail-safe 回落包根，解冻/启用时须补）／零漂移样板 1 份（bundle-assembly-registration）；
- 措辞漂移型＝0；声明领先实装（除 docs/adr 候裁项）＝仅 fuxi 一处（且属声明陈旧非规划领先）。

## 三、最实质三条（回报口径同步）

1. **fuxi-skill 声明面与现实完全脱节**（七份中唯一「declared∉实存」双向漂移）：delivery_paths 声明的 SKILL.md/references/ 在 git 面与盘上均不存在，六个实存目录（contracts/gates/adapters/specs/rejected/README）零声明——该包一旦进装配或租约射程，权限/取料按声明面走即全虚。建议随下一 FUXI 维护票带 STRUCTURE 重写子目，不另立票。
2. **两个「核心交付组件未上声明面」**：object-build `scripts/`（publish.py＝装配器执行主体）＋EAC `sources/`（dev-discipline 钦定唯一交付料源面）——声明缺位＝delivery_paths 授权/装配射程少一条，且与 C-2 同源对账（seat-permissions deny 六目录式）在技能包侧无镜像可比。各补一行＋yaml 随动即闭。
3. **生成物/元数据未枚举惯例缺统一措辞**：`COPY.state`（三包）＋bundle 顶层 `plugin.json/bundle.lock/settings.json/README.md` 均未声明——现状各自默认「惯例不宣」但未成文；将来 C-3 结构一致性机检（调研 v1 §2.2 主空白）实装时这些全数变常驻误报。建议：STRUCTURE 样板（以 bundle-assembly-registration 为底）加一行「生成物与装配元数据（COPY.state/bundle.lock/plugin.json/settings.json/仓侧 README）＝非枚举面」豁免措辞，四随正一次并闭。

## 四、清理与自检

- 临时读数区＝`.scratch/arch-struct/`：本次全部即时读数内联本件、**零落盘**（ls/git ls-files/grep 均为即时执行），故该目录未建亦无需删除——登记读数＝`ls .scratch/ | grep arch-struct`＝无命中（批毕即删义务真空真）；
- 只读零施工声明：未修任何 STRUCTURE 文件；除本件外零写入；必修/随正处置全部候裁（皮总拍②口径＝审查报告，不施工）；
- 本报告落 bundle 层 `.collab/research/`（与本仓 research 桶先例同层）；仓根在途 untracked 件（.collab/ledger/）未触碰。
