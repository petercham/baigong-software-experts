# 主理人登记：SEMGOV-T1-BUILD 收束核验（独立查盘全绿）与真文件审派出

- 落笔时点：2026-11-07 20:3x +0800；核验基线 HEAD＝`54fe775`（`54fe77520b5b422a291806c6a1ca487aa4387be4`）。
- 本件性质：登记件。登记主理人**不采信工程师自报**、独立复跑所得读数与收束判定；不含契约条款正文。

## 一、查盘三件套（FUXI 铁律·逐项实测）

| 项 | 工程师回报 | 主理人独立实测 | 结论 |
|---|---|---|---|
| 收口 HEAD | `54fe775` | `54fe775`／全串 `54fe77520b5b422a291806c6a1ca487aa4387be4` | 全等 |
| 尾两笔 | `54fe775`／`9e04dc0` | `git log -4`＝`54fe775 / 9e04dc0 / b9169c6 / 86d9963` | 全等 |
| 施工笔改动件数 | 8 | `git show --name-only --format="" 9e04dc0 \| grep -c .`＝8 | 全等 |
| 回执笔改动件数 | 1 | 同法 `54fe775`＝1 | 全等 |
| 改动件清单 | W1 七件＋W2 夹具／W3 回执 | 逐件打印与闭集一致；回执 §二 前段 9 件逐件列名（含本件） | 全等 |
| tracked 面 | 净 | `git status --porcelain --untracked-files=no`＝空 | 全等 |

## 二、主理人独立静态复验（自写实现，不复用工程师脚本）

自 `git cat-file blob 6db881a:<v5票面>` 取原始字节（294,858 字节／3,458 行／sha256 `dab81795…11ec5`），按围栏行号切片与真文件逐字节比对：

| 件 | 行数 | 字节 | EQ |
|---|---|---|---|
| `SKILL.md` | 92 | 7,331 | True |
| `references/10-contract.md` | 217 | 21,922 | True |
| `references/20-artifact-mapping.md` | 50 | 5,841 | True |
| `references/30-gates.md` | 98 | 16,799 | True |
| `references/40-provenance-map.md` | 43 | 7,474 | True |
| `templates/claim-register.md` | 44 | 4,050 | True |
| `templates/outbound-artifact.md` | 33 | 1,674 | True |

- 七件合计 **577 行**，与票面 §2.0b 自报全等。
- 夹具 2,097 行／135,600 字节／sha256 `25fc83b451c1…444ef508d`，与 §0.7 钉值 `25fc83b4…508d` 全等。
- 包内文件数＝7、与声明闭集列表全等、`.py` 数＝0；过程域名正则命中＝0；`## 0.7`／读数段标题命中＝0。
- `git diff 503ecca..54fe775 -- <v5票面> <v5回执>`＝空输出（真源一字未动）。
- **总判定 ALL_GREEN**。

## 三、主理人独立动态复跑（真文件上重跑，非照抄历史读数）

| 读数 | 实测 | 钉值 |
|---|---|---|
| `--all` | exit 0、`^OK\s+c\d\d` 命中 **28**、FAIL 0 | 28/28 |
| `--mutate` | exit 0、BITE **241**、汇总 `241/0/0`、覆盖 `28/28`、判定行「全绿」 | 241 咬住／0 假通过／0 MUTATE_FAILED |
| `--selfcheck` | exit 0、靶点 59 个锚唯一命中 59 不合格 0、双斜杠转义 0、空桶 `id_seq` 已登记、FAIL 行 0 | 59/59＋转义 0 |
| `--stats` | exit 0、**111 行** | 111 行 |
| 三闸 | `check-skill-meta.py --root .` exit 0（1 行 coverage 提示）；`check-provenance.py --root . --target …/SKILL.md` exit 0（空输出＝零 findings）；`check-entity.py --root .` exit 0（6 行，各 pattern count=0） | 三闸 exit 0、零 BLOCK |

**「空跑绿」疑虑排除**：读 `check-provenance.py` 真源，`--target` 走显式文件分支（`main()` 行 340 起），`check_file()` 对 `.md` 同样逐块跑 P-1/P-2/P-3；空输出＝零 findings，非跳过。并用脚本自带 `existing_providers()`／`resolve_anchor()` 独立复算：providers 8 个，`claim-commitment-governance` 在集；spec-provenance 七键齐；`spec_file` 所指登记件存在；锚 `## 一、变更项（四项）` 命中恰 1；条款 sha 复算 `f73f8dedc717019628bb10728da064e3f3030a86c934ef249b774f12dd60c9ae` 与声明全等 ⇒ **VERDICT PASS**。v5 出票期「provider 无法解析」的欠账已在真文件期真实补齐。

## 四、主理人自身三处命令笔误（如实自陈·不计工程师账）

1. 首次三闸复跑把 `--target` 一并发给 `check-skill-meta.py`／`check-entity.py`，二者不接受该参数 → exit 2。系**我方命令错误**，按各脚本自身参数形制重跑后 exit 0。
2. `grep -c "^OK c"` 未对上输出格式（实为 `OK   c26` 多空格）→ 误得 0；改 `^OK\s+c\d\d` 正则后得 28。
3. 锚定位首版自行 `lstrip('#')` 后仍拿带 `##` 的锚串匹配 → 误得 0；改用脚本 `resolve_anchor()` 真源逻辑后命中 1。

三处均属「自报读数必复算」纪律对主理人同样适用的一面；错在复算式，不在被核物。已逐条订正后重跑，结论未被误判带过。

## 五、收束判定

查盘三件套齐备、静态全绿、动态全绿、真源未触碰、回执三态明示与 9 件清单逐件在位 ⇒ **`TK-SEMGOV-T1-BUILD` 收束成立**。工程师「收口即停」遵守：未进真文件审／试填／改契约／升号／装配／部署。

两点在册知悉：①回执笔 sha 的自指约束（回执写于自身提交前，物理上不含自身 sha，按 v5 回执同族惯例由完工回报给出 `54fe775`，非漏写、未 amend、未产生第三笔）；②两笔提交触发的指针门禁 advisory 输出与 `.scratch/tickets/` 回执落点 WATCH 均为在册既有项、非本票引入，不改门禁、不改落点。

## 六、放行路径第 3 步派出（两席并发·fresh eyes）

- 按裁定十五第 3 步：派 **QA 席＋产品席对真文件审**（被核主体＝`agent-skills/claim-commitment-governance/` 真文件＋夹具＋回执；**不再对票面围栏审**，票面仅作逐字比对基准）。
- 两席**同时派出、互不读对方本轮产出、各自单独 commit**；禁同席多实例，异席并发合法。
- 裁定十九机检兜底、交付物指针闭环、平台兼容性、契约语义可用性边界列入必核面；**放行 ≠ 语义验收**：真文件审不得替「真实 PRD 试填」（第 4 步／T2 硬闸）背书。
- 审件落点统一为 `D:\multi-agent-collab-devkits\agent-experts\baigong-software-team\.collab\qa\`（与 v5 窄审两席同族，避免新增路径归一化债）。

## 七、后续票序不变

第 4 步真实 PRD 试填（T2 硬闸，另票）→ 第 5 步试填暴露契约不对则改契约再落、不带病发布 → T1–T6 完成与 PROJINIT 合并同版本批升号（建议 0.1.31）→ 重新装配 → 三同源同步；部署链③人类闸仍须皮总真实验证明示，代理不得代跑。
