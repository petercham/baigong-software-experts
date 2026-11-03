# FUXI-T10 · check-pointers scheme-URL 形态漏网修正票

> 票号＝FUXI-T10｜起草＝架构席（arch-fuxi-tr1）｜日期＝2026-10-31｜被派＝**工程师席**
> ANCHOR＝开工前取当轮 HEAD 实测读数（回执开端必附）；起草时点 HEAD 实测＝`551317c`（TR2 分诊件笔）
> 来历（自包含）：T9 端到端复跑暴露——联网实采批产物 `source_id=`公开 URL 逐字``（T9 票裁-3 钉死形态）被交付面门禁 `check-pointers.py`（OA-D6）当仓内指针判悬空，每批必产 11± 条 BLOCK 级发现（路由②不拦提交但污染基线 519→530）。分诊（TR2 §一-1）定性与根因已实证：`URL_PATH_RE = ^[A-Za-z0-9][A-Za-z0-9.-]*\.[A-Za-z]{2,}/` 要求首段＝域名，`https://…` 的 `https:` 段含冒号不匹配；带尾斜杠 URL 又命中「以 `/` 结尾＝目录路径」放行分支 → 误入悬空判定。**该修法＝既有排除意图（脚本注释自陈「带域名的 URL 语法上就不是仓内相对路径」三类同族排除）的漏网形态补齐，非新增语义**（同 ENG-S6 先例：工具面接受形态＝施工票直修）。
> 同型先例：OA-D6 裸基名豁免（裁-21）/ENG-S6 声明闭集解析修正＝执行层缺陷直修通道在册。

## 〇、执行裁定（票内定稿，非候裁）

1. **条款零动**：`50-document.md` D6 表不增行不改行（`spec_clause_sha256` 必须保持 `f120944…0db0751` 全等——脚本头 spec-provenance 块零触动）；`60-gates.md` 路由表零动（OA-D6 严重度/路由不涉）。改动面＝纯脚本形态判定层。
2. **修法钉死（形态判定，禁语义判断）**：`looks_like_path()` 入口处增 scheme-URL 形态排除——token 以已知 scheme 前缀开头（`http://`／`https://`／`ftp://`，闭集常量 `SCHEME_PREFIXES`）即返回 False（语法上就不是仓内相对路径，与 HOME_PATH_RE/GIT_REF_RE 同族）。**禁**用「含 `://` 即排除」之外的启发式（如猜域名/猜外部项目）——60-gates §〇 铁律 1（脚本无权语义判断）。既有 `URL_PATH_RE`（裸域名形态）保留零动，两判并存。
3. **不新增夹具文件**（避免 deliverables 扫描面新件牵动其它检查计数）：验收以定向扫描对拍承载（§三判据2/3 用 `--target`/`--scope` 现盘件），脚本无 selftest 体制维持现状。

## 一、声明闭集（本票交付笔唯一改动面）

- `deliverables/skills/object-audit/scripts/check-pointers.py`（`SCHEME_PREFIXES` 常量＋`looks_like_path()` scheme 排除分支＋注释随动一行）
- `deliverables/skills/object-audit/SKILL.md`（version `0.7`→`0.8`）
- `deliverables/skills/object-audit/references/90-changelog.md`（append v0.8 行：措辞自包含＝scheme-URL 漏网形态补齐·条款零动·T9 复跑实证 11 条误报根因·验收读数引用位＝回执）

回执（另笔）：`.collab/receipts/2026-10-31-ENG-T10-工程师回执v1.md`。

## 二、施工规格

S1 · 脚本：常量段（`GIT_REF_RE` 行后）append：
```python
# scheme 前缀 URL（T9 复跑实证漏网形态：`https://…/` 带尾斜杠曾误入目录路径放行分支）。
# 与 HOME_PATH_RE/URL_PATH_RE/GIT_REF_RE 同族＝语法形态判定，非语义判断（铁律 1）。
SCHEME_PREFIXES = ("http://", "https://", "ftp://")
```
`looks_like_path()` 在 `SKIP_EXACT` 判定后、`#"/@"` 前缀判定前后均可（建议紧随 `tok.startswith("#")` 块后）插：
```python
    if tok.startswith(SCHEME_PREFIXES):
        return False
```
docstring/注释随动一行（「这三种写法」段改述为四形态或补一行，不删原注）。

S2 · 版本账：SKILL.md front-matter `version: 0.7`→`0.8`；90-changelog append v0.8 行（体例随 v0.7 行）。

S3 · 判分段实跑读数入回执（见 §三）。

## 三、验收判据（三态禁假绿）

1. **修正对拍（真咬不回归）**：修正前后对同一 HEAD 盘跑 `check-pointers.py`：`https://` 反引号 token 命中数 11→**0**；同时**真悬空仓内路径仍咬**——对抗注：临时在某案卷外 md 写 `` `deliverables/products/pending/nope/README.md` `` 型指针确认 BLOCK 复现后复位（或用既有现盘悬空读数非 URL 类零动对拍）。
2. **产物面定向扫描**：`--scope deliverables/products/pending` 跑＝OA-D6 命中 0（df3/mh2/mb6 全消）；其它检查器性质零动（check-entity/check-source-of-truth 等计数与基线全等）。
3. **run-gates 全链复原**：连跑两次逐字节全等＝`GATE PASS（发现 519 条…）`＝T9 前基线复原（530→519，恰 −11 全＝URL 类）；两笔 commit（交付＋回执）均过闸；红＝0。
4. **spec-provenance 零触动实证**：修正后脚本头 `spec_clause_sha256` 行逐字节未变（`git diff` 该行零出现）；`--target` 三产物逐件跑＝exit 0 且无 OA-D6 行。
5. **版本账对账**：SKILL.md version 行＝0.8＝changelog 新行版本号＝README 无涉（fuxi bundle 版本账不涉——本件＝object-audit 包独立版本账，包惯例取步）。
6. 禁动面：`50-document.md`/`60-gates.md`/产物九件/`run-gates.sh`/fuxi-skill 全包/夹具零触碰；`git show --name-only`≡声明闭集（交付笔恰 3 件）。

## 四、纪律

- 交付单笔（前缀 `ENG-T10:`）＋回执笔另 commit；回执开端附开工 ANCHOR。
- 禁 --no-verify、禁 amend、禁 push；候补池不动；发现新缺口只登记走 ㊵。

## 五、候裁点

无（修法＝既有排除意图漏网形态补齐·条款零动·ENG-S6 同通道先例在册；无对立分歧）。
