# ENGSTD v3.1 · 一行级定点批（ES v3 快验黄-1/2/3 修点）· 架构席作者席

- 起草实测 HEAD：`31cf6c1`（QA 快验件笔·`git rev-parse --short HEAD`·工作仓 `D:\multi-agent-collab-devkits`·main）；开工 ANCHOR 读数即此。
- 件型＝**定点补丁件**（体例裁量登记：取「新建 v3.1」案，弃「v3 原地 append」案——两者皆合法（作者席 self），取新建为保 v1/v2/v3 版本链完整与 QA 单席复核对位；三原件零改动）。
- 效力链：v1（`a136630`）→ v2（`289a55c`·收口 `2f196d9`）→ v3（`e1de307`）→ 本 v3.1。双席快验 v3 结果＝PM 完全认可（`5b6a439` 零红零黄）＋QA 认可带保留（`31cf6c1` 黄3）。本批修毕即转完全认可（预授权形制）；**本批只动三修点，其余全部条款以 v3 为准（指针只指不搬）**。
- 计数口径：occurrence；锚 HEAD=`31cf6c1`。

## 声明闭集（1 件·本笔唯一可写面）
- 声明闭集：
- .collab/design/2026-11-03-devkits-engstd-adr-archive-retirement-v3.1.md

---

## 一、修点三条（覆盖 v3 对应条款文本；修后文本为真源）

### 黄-1 · E-ADR-2″ 补正断言（封非首位/非四位编号三构型绕过·QA 攻测点 1 实测 adrneg2）

E-ADR-2″ 增首行正断言，修后全文：

```
E-ADR-2‴ 编号正断言＋唯一＋递增（v3.1 修）：
  (0) 正断言：`docs/adr/` 目录内全部 `*.md` 文件名必匹配 `^(\d{4})-[A-Za-z0-9._-]+\.md$`，
      否则 exit 1（封 `use-pg-0001.md` 编号非首位、`12345-five.md`/`001-three.md` 非四位逃账）；
  (1) 提取集 `^(\d{4})-` 重复 occurrence>1 exit 1；
  (2) 新落盘编号＝既有最大＋1（跳号/复用 exit 1）。
```

（(1)(2) 语义＝v3 E-ADR-2″ 原式零动；(0) 为新增前置。）

### 黄-2 · E-ADR-5″ 桶互斥修正（verdicts.md 双计·现盘 0+13+1=14≠13 字面永假）

桶2 口径明示排除 verdicts.md，修后全文：

```
E-ADR-5‴ 三面对账（v3.1 修·桶互斥）：
  桶1＝`git ls-files docs/adr/` 逐名 test -f 全存在（缺名 exit 1）；
  桶2＝`.collab/decisions/` 逐名清单对账（v2 E-ARC-3′ 原式）**排除 verdicts.md**
       （排除式：ls-files 结果过滤 `grep -v 'decisions/verdicts\.md$'`）；
  桶3＝verdicts.md 单件在盘 test -f；
  和式断言＝桶1＋桶2＋桶3 ＝ `git ls-files docs/adr/ .collab/decisions/ | wc -l`
       （现盘对账基线：0＋12＋1＝13 ✓）；
  删除行 BLOCK 断言（`D docs/adr/` ∪ `D .collab/decisions/`）逐字同 v3 E-ADR-5″ 零动。
```

### 黄-3 · E-ADR-4″ 注记触发件引用式换代（消与 NNNN 制不自洽）

v2 E-ADR-4′「必含日期戳＋触发件引用」中引用式随动换代，修后文本：

```
注记行内容约束（v3.1 修）：必含 `YYYY-MM-DD` 日期戳＋触发件引用——引用式闭集＝
  `^\d{4}-`（docs/adr 现行 NNNN 制）∪ `ADR-\d{3}`（历史制残留兼容）∪ 案件路径形态
  （`.collab/…` 或 `docs/…` 全路径）；三式皆不命中＝注记不合格 exit 1。
  其余（适用域 docs/adr 族限定、diff 白名单、行级只增约束）逐字同 v3 E-ADR-4″ 零动。
```

## 二、登记级注记处置（不修文本·归口登记·QA N-1/N-2/N-3＋PM 注记②③）

| 观察 | 处置声明 |
|---|---|
| PM 注记②（STRUCTURE.md 与 docs 实况镜像句）＋注记③（deny 开口改显式枚举三件套） | 归 **T08R 权限表施工票**消化（与 v3 §三「具体机械写法随 T08R 定形」同口）；STRUCTURE.md 落地批（B 批约定 md 票）随带镜像句。 |
| QA N-1（glob_match 无排除语法→deny 开口枚举式对 docs 未来新子面 fail-open 向） | 归 T08R：施工票补 **docs 面枚举闭集断言**（docs 顶层子目录名录闭集＝STRUCTURE 约定面镜像＋机检比对）；本席认可该风险与 T08R R⑧(i) 同构，随同票处置。 |
| QA N-2（门禁缺省面不含 docs＝adr advisory 非常驻） | 归**门禁路由裁量**（60-gates 路由表加 `check-pointers --scope docs/adr` 类挂载属路由表改写职权＝门禁面非本定标面）；advisory 补偿断言先随 E-ADR-3″ 校验批常驻，路由加挂后升常驻。 |
| QA N-3（裁定登记族误写 ADR supersede 语法的域外半缺） | 保守向·不修：裁定登记族走「不删只注记」机理不用 ADR 语法（v2 A.2/v3 〇表在案），族界清晰；如后续成真按违例路由。 |

## 三、回执（v3.1 起草笔）

- 开端 HEAD 实测＝`31cf6c1`；本笔单独 commit（`collab:` 前缀·只含声明闭集 1 件）；禁 `--no-verify`、禁 amend；门禁拦截如实报告不绕闸。
- 三修点均一行级文本定点：黄-1＝E-ADR-2‴ 前置正断言；黄-2＝E-ADR-5‴ 桶2 排除 verdicts.md＋和式基线 0+12+1=13；黄-3＝注记引用式三式闭集（NNNN∪历史制∪案件路径）。v1/v2/v3 原件零改动。修毕候 QA 单席复核销账＝终态收口（PM 面已完全认可）。
