# SWB-B3 · rev2 定点增补补丁件（承接旧仓根 docs 8 件 R-1＋design 桶照 §三 执行 R-4＋判据1 扫描面写死 R-5＋evidence 2 支 tracked 单列 git mv R-6＋基线两栏/域对齐）
Status: 已结案（retire 宣告 2026-11-04·依 2026-11-04 审计对齐类免拍板放行裁定·票面退役批 SWB-RET）

- 本件＝B3 票（`.scratch/tickets/2026-11-03-SWB-B3-process-domain-migration-ticket.md`·`d584d7b`）之 **rev2 定点增补**（参 ES v3.1 体例：原票不动、补丁件另立）。原票未被本件推翻条款照旧；冲突处以本件为准。
- 修单真源＝会师件（`3ad4d99`）§一 R-1/R-4/R-5/R-6＋§二 B3 黄三目＋§三.2（TKT erratum 照引义务）；PM 审票 `d6eef8a` S2/S6/B3-Y1/Y2/Y3；QA 审票 `1c72966` 红-1/红-2/红-3。
- 开工 ANCHOR 随原票（B2 收口后）；B3a 跑绿前 B3b 禁启动硬线不变。

## 补丁一（R-1·承接旧仓根 `docs/` 8 件入声明闭集＋禁动面改口径）

原票禁动面「`docs/`（旧仓根·B5）」**作废**，换代口径：「旧仓根 `docs/`＝**B3 内容分流面**（本票）＋B5 只灭残壳」。

### B3g 旧仓根 docs 分流（git mv·按分账函数·新增施工目）

基线实测（HEAD `3ad4d99`·`git ls-files docs/`）＝**8 件**：

| 件 | 形态 | 归桶（按分账函数＋内容形态） |
|---|---|---|
| `docs/README.md` | 索引件 | 百工 `.collab/receipts/`（索引史实面·B5 灭壳时此件已不在位·B5-D 删源目自动清零） |
| `docs/process/2026-10-22-建包过程记录.md` | 过程记录 | 名含建包/软开线→**baigong** `.collab/receipts/`（过程账归 receipts＝B3c 根散件同标） |
| `docs/research/R1..R6`（6 件） | 判词依据研究件 | 名 R1..R6＝切分/同构/标准体系/拆分代价/目录治理/README 分工＝仓级软开线研究→**baigong** `.collab/research/` |

- 逐笔 `git mv docs/<件> agent-experts/baigong-software-team/.collab/<桶>/<件>`；`docs/` 目录随空自灭（B5-D 残壳检查届时读空＝断言自洽）。
- 声明闭集追加一行：`- docs/（旧仓根）8 件 → 百工 .collab/receipts|research/（git mv·B3g）`。
- 引用随动：全仓对 `docs/process/`、`docs/research/R` 的活路径引用随 B3a 换锚面同批处理（扫描面已含 docs）；史述豁免同制。
- 判据随动入判据 2（守恒式含 docs 8 件侧：迁前 `git ls-files docs/`＝8 → 迁后 0）＋判据 5（旧域清零含 `find docs -type f | wc -l`＝0）。

## 补丁二（R-4·design 桶照 v3 §三 L64 执行＋erratum 登记程序落笔）

1. **执行定向**：`.collab/design/` 24 件（现盘 tracked 实测·票面 17＝起草漂移，按实测立账）按分账函数入 `<项目>/.collab/design/`——**design 桶存在性由 B1 rev2 补丁一（十一桶闭集）承接**，本票 B3c「qa/receipts/board/design 四桶」行自此与规范闭集无碰撞。
2. **erratum 登记程序（第二笔·同 TKT 程序）**：v3 §二标准结构图（L40–43 桶名录无 design）与 §三 L64（design 入 `.collab\design\`）＝基线内部不自洽；**从 §三 具体申报**（会师件 R-4 裁定）。B3 回执落「v3 §二结构图 erratum 增补登记」一行，照引 §三 L64 原文：「`.collab/design/` 17 件 | 混线 | 按案线归项目 `.collab\design\`（设计稿属过程域；其中现行有效设计稿若属交接件性质→docs，按 §二点八 存活判据逐件分）」＋判定依据＝会师件 `3ad4d99` R-4。不改冻结基线文本。
3. **交接件甄别行**（§三 L64 后半句实装）：design 24 件逐件按裁定三 §二点八 存活判据分「过程域留 design 桶」vs「现行有效交接件→项目 `docs/`」；回执逐件表列「去向」列（缺省＝design 桶，交接件＝显式个案）。

## 补丁三（R-5·判据 1 扫描面照 B3a 申报面写死可跑式）

原票判据 1 全仓 grep＋两豁免＝不可执行（evidence/gates 974 命中且续增），作废换代：

```
for d in .collab/receipts .collab/qa .collab/design .collab/decisions .collab/dispatch docs README.md deliverables; do grep -rno "\.collab/tickets/" "$d" 2>/dev/null; done > $B3_TMP/c1.raw
grep -v "^\./\.collab/tickets/" $B3_TMP/c1.raw | wc -l ＝ 0
```

- 扫描面＝**B3a 申报面闭集**（receipts/qa/design/decisions/dispatch/docs/仓根 README/deliverables——逐字同 B3a 第 1 条），evidence/inbox 等运行流水面**不在扫描面**（豁免由扫描面构造承载，非清单豁免＝会师件 R-5「照申报面限定」择一写死）。
- 豁免仍留史述账（票面史述逐处入回执）；负例＝账外命中 exit 1。
- 申报面外残留（若存在）＝回执登记不判红（该面由 B4 换锚与 ES 退役批收口·在册）。

## 补丁四（R-6·evidence 桶 2 支 tracked 件单列 git mv＋防脱库断言）

`.collab/evidence/2026-10-29-判词-T-team-rename-01.md`＋`2026-10-29-回执-team-rename-01.md`＝**tracked**（早于 gitignore 增补入库·实测 `git ls-files .collab/evidence/`＝2）——从 B3e「文件系统 mv·untracked 面」**摘出**：

1. 此 2 支走 `git mv`（归桶＝分账函数规则 4 `QA-/席位` 族→**baigong** `.collab/evidence/`；`git mv` 不受目标 ignore 规则影响＝新位入 index 不被 B1 过渡块 `/**/.collab/evidence/` 吞）。
2. 判据 2 增补断言（防脱库/悬挂）：
   - `git status --porcelain | wc -l`＝**0**（mv 后无残留删除/未追踪脏态；执行批次收笔时点断言）；
   - 新位不被 ignore 吞断言：`git ls-files "agent-experts/baigong-software-team/.collab/evidence/" | grep -c "team-rename-01"`＝**2**。
3. B3e 其余 evidence 面（untracked·实测现盘 3800+）仍走文件系统 mv，零改。

## 补丁五（黄·基线两栏＋守恒式同域口径＋era 二次分账）

1. **开工首步重落盘 untracked 基线**（PM S6）：回执分「票面起草读数（`f017a51` 锚）／开工实测读数」两栏——refs/evidence/inbox/dispatch 四桶开工即 `find … | wc -l` 落盘（evidence 门禁续写漂移 3827→3857+ 已在册）；判据 4 守恒式以**开工实测栏**为基。
2. **判据 2 同域口径**（PM B3-Y3）：守恒式双侧一律 `git ls-files .collab .scratch | wc -l` 单命令同域口径——迁前开工实测值 X → 迁后＝X＋2（两支 TKT 入库）＋…（docs 侧另账：`git ls-files docs/` 8→0 独立断言，不并入本式，防双计）；逐桶表前后相等照旧。原票「597＋2」＝`f017a51` 锚参考值，开工以实测 X 立账（B 批票面/壳件在 `.scratch` 域两侧同现＝自然相消）。
3. **era 留置按出处二次分账**（PM B3-Y2）：正则 5 命中面（实测 research tracked 面命中 26 条含目录展开）→ ESC1 移交清单附件强制两列分账：**第三方外部快照**（`drafts-2026-10-23/aigc-video-team*`、`video-team*` 源料族＝移交候选）vs **本仓自产**（如 `2026-10-23-视频团队本体审计_v1.md`＝判词依据件·**不外移留项目桶**）；出处判定口径＝件头来源声明/源料说明在位者，回执逐件标注＋主理人核销。ESC1 清单真源＝本回执表（供 ESC1 票引用）。

## 销账对位（本件覆盖修单目）

| 修单目 | 本件处置 |
|---|---|
| R-1（旧仓根 docs 8 件归宿悬空） | 补丁一（B3g 承接＋禁动面改口径＋判据随动） |
| R-4（design 桶碰撞·从 §三 设桶） | 补丁二（照 §三 执行＋erratum 第二笔登记＋B1 rev2 扩员供源） |
| R-5（判据1 豁免不可执行） | 补丁三（扫描面照申报面写死闭集 for 式） |
| R-6（evidence 2 支 tracked 脱库） | 补丁四（git mv＋porcelain 空＋不被 ignore 吞断言） |
| B3 黄·判据2 基线域/断言域对齐 | 补丁五之 2 |
| B3 黄·era 按出处二次分账 | 补丁五之 3 |
| B3 黄·开工重落 untracked 基线两栏 | 补丁五之 1 |
| §三.2 TKT erratum 照引义务 | B3 回执照引 v3 L70 原文：「工作区 2 支 2026-11-01 TKT untracked 旧件 | 散挂 | fuxi-skill `.collab\qa\` 入库」＋判定依据＝分账函数规则 1＋B0 四目④未锁归属（原票勘误注记已在位，回执照引补齐） |

## 回执随动
回执增节：B3g docs 8 件逐笔表＋design 24 件去向表（含交接件甄别列）＋erratum 两笔登记（§三 L70＋§二结构图 L40–43）＋判据 1 换代式读数＋evidence git mv 三断言读数＋基线两栏表＋era 出处二次分账表（ESC1 清单真源）。

——arch-swbreloc · rev2 补丁件（新建创作类·誊写禁令辖域外自察；本票搬家目仍 git mv／untracked 文件系统 mv 分制）。
