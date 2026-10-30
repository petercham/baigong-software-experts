# FUXI-T8 · public-anchor 层序序号一行制归一修正票（观察-1 收口）

> 票号＝FUXI-T8｜起草＝架构席（arch-fuxi-tr1）｜日期＝2026-10-31｜被派＝工程师席（主理人路由）
> ANCHOR＝开工前取当轮 HEAD 实测读数（回执开端必附）；起草时点 HEAD 实测＝`0af2f34`
> 来历（自包含）：QA-S0b 独立核验（`.collab/qa/2026-10-31-FUXI-S0b-QA验证报告-v1.md` 观察-1）移交口径差：`validator-public-anchor.py` 头部 docstring 层名序列＝「L0 格式检查表→…→L5 人工锚点卡」（零基），实跑读数行前缀＝「L1 …→L6 …」（一基，代码 L393 `enumerate(results, 1)`）——既有件内自相矛盾，非 S0b 批引入（S0b 批对该件 pathspec 零触碰在册）。
> **架构席裁定＝归一一基制**：①runtime 读数行前缀与验证记录 id（`P%02d` 同源 seq）已按 L1–L6 落盘在案（harness 证据件＋selftest 判例行 L599 检查 (2,3,4) 均一基），改 runtime 侧＝与既有证据冲突＋行为变更，禁；②同族 `validator-source-anchor.py` docstring 与 runtime 双双一基 L1–L6（家族惯例）；③`validator-catalog.md` VA-P-01「public-anchor L0 格式检查表」与 VA-P-06「L5 人工锚点卡」两处散文引用＝同错源，一并随正。修＝文案侧（docstring/注释）＋目录两处引用行逐字 +1 位移，**运行行为零变更**。

## 一、声明闭集（本票唯一改动面，两件）

- `deliverables/skills/fuxi-skill/gates/validator-public-anchor.py`
- `deliverables/skills/fuxi-skill/gates/validator-catalog.md`

## 二、施工规格

### S1 · `validator-public-anchor.py` 文案侧序号 +1（仅 docstring/注释行）

层名锚定的机械位移（层名→新序号映射＝格式检查表 L1／盲评rubric L2／绝对线 L3／decoy L4／泄漏检查 L5／人工锚点卡 L6）：

1. 头部 docstring 层序行（现 L6）：「L0 格式检查表 → L1 盲评rubric → L2 绝对线 → L3 decoy → L4 泄漏检查 → L5 人工锚点卡」→「L1 格式检查表 → L2 盲评rubric → L3 绝对线 → L4 decoy → L5 泄漏检查 → L6 人工锚点卡」。
2. 各层函数 docstring 首词同映射位移（现位 L131/L195/L220/L244/L266/L320）。
3. 同文件内其余序号引用行按语义随正：现 L25「本件 L5 只做…」→ L6；现 L93 注释「本件 L5 薄封装」→ L6；现 L222「同 L1 参考位口径」→「同 L2」；现 L323「元组交付前 L1-L3 分数一律参考位」→「L2-L4」；现 L385 注释「L0 格式检查表 fail＝不进盲评层；L4 泄漏 fail」→「L1 格式检查表 fail…；L5 泄漏 fail」；现 L420 注释「与 L3 decoy 同源」→「L4 decoy」；现 L557/L559 selftest 注释「→L0 fail→」「（L0 fail）」→「L1 fail」。
4. 判分段/生成段逻辑、`LAYERS` 元组、`enumerate(results, 1)`、记录 id 格式、selftest 用例本体＝**零改动**（改动面全部为注释与 docstring 文本）。

### S2 · `validator-catalog.md` 两处引用行随正

- VA-P-01 断言内容行：「public-anchor L0 `格式检查表`」→「public-anchor L1 `格式检查表`」；同行「L0 fail 不进盲评层」→「L1 fail 不进盲评层」。
- VA-P-06 断言内容行：「L5 `人工锚点卡`」→「L6 `人工锚点卡`」。
- （VA-S-07 行「L1 断言向量位数」指 source-anchor L1 机械断言＝已一基正确，零动。）
- 修订注记按文件既有最高版次加一 append 一行（层序序号归一随正，条目与数值零动）。

## 三、验收判据（三态禁假绿）

1. 序号一致性三向对拍：py 文件 docstring 头部层序行 ≡ `LAYERS` 元组顺序 ≡ 实跑报表行前缀序列（同一合成批次连跑取行，读数在案）——三向均 L1–L6。
2. 该 py 文件 `grep -n "L0"` 命中＝**0**；`grep -c "人工锚点卡"` 行内含「L6」；「L1-L3」／「L4 泄漏」旧形态全文件命中＝0。
3. **行为零变更实证**：selftest 全绿（例数与开工 ANCHOR 盘全等，零增零删）；连跑两次逐字节全等；同一输入批次前后报表行逐字节全等（本票不得改变任何对外读数）。
4. assert-tool 全量与开工盘逐项读数全等；run-gates 同盘态对照零新增红。
5. validator-catalog 两处替换逐字节对拍＋修订注记新行在场；节结构与 §四预注册表数值零动。

## 四、禁动面

- 两件之外零触碰；source-anchor／s0b-kappa／harness-common／assert-tool 零触碰。
- 层名闭集（validator-catalog §二 值注册 11 值）零动；断言条目文本除 S2 明列两处外零动；预注册数值零动。
- py 文件内一切代码逻辑行（判据／常量／函数体／用例数据）零动——diff 面须全部为注释/docstring 行（回执附逐 hunk 归位声明）。

## 五、候裁点

无（序号制式属交付面内部口径，归一族既有惯例（source-anchor 一基）即程序内技术裁量）。
