# ENGSTD · devkits 工程规范定标设计件（ADR/归档/退役三题）v3 · 架构席定稿（ADR 正件落位 docs 随动批）

- 起草实测 HEAD：`5358ea4`（ADR 落位裁定登记笔·`git rev-parse --short HEAD`·工作仓 `D:\multi-agent-collab-devkits`·main）；开工 ANCHOR 读数即此。
- 件型＝**定标设计件 v3（定稿·随动批）**：本次唯一覆盖条目来源＝`.collab/decisions/2026-11-03-皮总裁定-ADR正件落位docs.md`（`5358ea4`·裁定原文「那就必须要有 ADR 正件能放入 docs 才行，这样才符合行业范式」）。
- 效力链：v1（`a136630`）→ v2（`289a55c`·红2黄7修正·双席快验销账收口 `2f196d9`）→ 本 v3。**v2 原地不动**，本 v3 生效后为定标真源；v2 未被本裁定覆盖的全部条款（三族分权、Nygard 骨架＋Status 闭集＋supersede 双向、SOP 裁决落地节点、T-B/T-C 全部结论、E-ADR/E-ARC/E-RET 判据机理）**照常有效**，本件只落随动面——件内引用未改条款以「v2 §x.x」指针指认（指针只指不搬）。
- 计数口径：occurrence 口径；行号/读数锚 HEAD=`5358ea4`；判据命令自带落盘重定向；负例 exit≠0 断言。

## 声明闭集（1 件·本笔唯一可写面）
- 声明闭集：
- .collab/design/2026-11-03-devkits-engstd-adr-archive-retirement-v3.md

---

## 〇、修订记录（v2→v3·覆盖条目处置）

| 项 | 来源 | 处置 | 落点 |
|---|---|---|---|
| T-A 定标点①「ADR 正件落位维持 `.collab/decisions/` 不迁 docs」 | 裁定 `5358ea4` §二.1/.3 | **作废→改「ADR 正件族落 `docs/adr/`」**；子形态定标＝`docs/adr/NNNN-slug.md`（见 §一-A 定标理由） | §一-A |
| E-ADR-1..5′ | 随动① | 落位路径/扫描面口径随动；**机理零动**（编号唯一不复用、Status 闭集、supersede 双向图、accepted 不可变、分桶对账骨架全保留） | §一-B |
| E-ADR-5′ 分桶对账 | 随动① | 桶结构改三面对账＝`docs/adr/` ADR 族＋`.collab/decisions/` 裁定登记族＋`verdicts.md` 判词族（判词单件留 decisions 桶内机械判据不变） | §一-B E-ADR-5″ |
| E-ARC-1′ 引用扫描面 | 随动① | ADR 入 docs 后扫描/永存口径随动（ADR 族不入移除流程＝新「永存面」，与 decisions 同权；扫描面补 `docs/adr/` 域） | §二 |
| seat-permissions 随动目 | 随动① | **v2 Y-2 点名目更正**：architect 行补 **docs 侧 ADR 子面**授权（`docs/adr/` write_globs＋该行 deny_globs `docs/**` 同步开口），v2 原「architect 行补 `.collab/decisions/` 仅 `*ADR-*` 族」**作废**；host 行补 `.collab/decisions/`（裁定登记誊录通道）**不变** | §三 |
| STRUCTURE.md 内容口径 | 随动① | 补「docs 两面制＋ADR 子面条目」定义（§一-A.3 文本可直接引用） | §一-A.3 |

其余全部条目（含 v2 红①②黄1–7 处置、呈报节备案项）＝零变更。

---

## 一、T-A 随动定标

### A.1 落位子形态定标＝`docs/adr/NNNN-slug.md`（候裁不留·直接定）

1. **子形态取业界惯例件**：`docs/adr/` 子目录＋四位零填充编号＋slug 文件名（`0001-<slug>.md`），弃「docs 根同桶 `ADR-NNN`」案。理由三条：①裁定判据本体＝「符合行业范式」，业界落位惯例正是 `docs/adr/`＋编号（`0007-use-postgresql.md` 形态·v2 A.1-4 引账在案），同桶散放无工具链兼容（adr-tools/Log4brains 皆认 `docs/adr/`）；②docs 根＝三件套（STRUCTURE/PRODUCT/ARCHITECTURE·裁定三§二点九）薄面，ADR 散入即破三件套名录闭集观感，子目录＝docs 内自有子面，与「根只放索引/约定」惯例同轨；③编号语义换代正当性：ADR 编号此前从未上线（现盘 `Supersedes`＝0、无任何 `ADR-NNN` 件在盘·实测），无迁移负担，直接采业界 NNNN 制免于二次换形。
2. **编号口径**：项目内 `docs/adr/` 单调递增不复用（E-ADR-2″ 随动，正则改 `^(\d{4})-`）。
3. **与裁定三 docs 定义的兼容成文（docs 两面制定标）**：裁定三§二点八定义 docs＝「当前存活的干净交接件」，辖 PRODUCT/ARCHITECTURE/STRUCTURE 三件套＝**交接文档面**（被取代即出 docs、历史归 git＝T-B B.3-2 机理）。ADR 族性质不同＝**决策日志面（永久记录面）**：一件 ADR 不是别的文档的历史态，其自身就是史实记录，行业纪律明确「superseded ADR never deleted、留档因其记录过」（v2 A.1-1/4 引账）。据此定标闭集：
   - **docs 两面制**：docs＝①交接文档面（三件套·现行存活·被取代即出）＋②`docs/adr/` 决策日志面（**永不出 docs**：Accepted/Rejected/Deprecated/Superseded 全部留档原位，Status 就地更新＋双向互链承载演化——与 T-B「decisions 永不删」同权同级，理由同源＝史实锚＋被引用面）；
   - 「docs 被取代即出」条款辖域**明示限交接文档面**，不辖 adr 面（v2 B.3-2 文本加辖域限定句，机理零动）；
   - STRUCTURE.md 内容口径补条目（可直接引用文本）：「`docs/adr/`＝本项目架构决策日志子面：编号四位递增不复用；状态闭集 Proposed/Accepted/Rejected/Deprecated/Superseded by <件>；supersede 只改 Status 行＋双向互链；本面全部件永不删除，被取代件原位留档。」
4. **三族分权不变**：ADR 正件落盘权＝架构席（v2 A.2-3）——权随族走，族迁 docs，权不变；裁定登记族与判词族留 `.collab/decisions/`（裁定 `5358ea4` §二.3 明示不在覆盖范围）。

### A.2 E-ADR 族条款随动文本（机理零动·只改落位/扫描面）

```
E-ADR-1″ 头块断言：适用面改 `docs/adr/*.md`（项目内）；头 12 行必含
  Status 闭集行＋Deciders＋Date＋Author＋Registrar 五行（内容同 v2 E-ADR-1）。
E-ADR-2″ 编号：文件名 `^(\d{4})-` 提取集重复 occurrence>1 exit 1；
  新落盘＝既有最大＋1（跳号/复用 exit 1）。
E-ADR-3″ 双向 supersede 全向校验：适用域改 docs/adr/ 集；(a)(b) 双向图语义与
  缺边 exit 1 判定逐字同 v2 E-ADR-3′。
E-ADR-4″ accepted 不可变：适用域＝`docs/adr/*.md`（v2 的 `*ADR-*` 文件名族限定
  随之改为 adr 目录族限定——限定语义等价＝「只辖 ADR 族，不辖裁定登记族史实注记」不变）；
  diff 白名单与注记行内容约束逐字同 v2 E-ADR-4′。
E-ADR-5″ 三面对账（并 E-ARC-3′）：
  桶1＝`git ls-files docs/adr/` 逐名 test -f 全存在（缺名 exit 1）；
  桶2＝`.collab/decisions/` 逐名清单对账（v2 E-ARC-3′ 原式）；
  桶3＝verdicts.md 单件在盘；
  三桶和＝决策记录面总数断言＋任何 commit diff 出现 `D docs/adr/` 或 `D .collab/decisions/`
  行＝BLOCK（git show --name-status 过滤·零新构件）。
```

## 二、E-ARC-1′ 扫描面口径随动

- ADR 入 docs 后，ADR 族**不进入票面移除流程**（票面族定义不变＝tickets 域），改挂「永存面」与 decisions 同权：删除即 BLOCK（E-ADR-5″ 已含 `D docs/adr/` 断言）。
- E-ARC-1′ (a) 全文本域扫描的 `--include` 域不变（自然覆盖 `docs/adr/`）；(b) 裸基名族新增实例化口径＝票 ID 若被 adr 件引用，换锚目标改指该 adr 件（adr 永存＝理想换锚目的地）。
- 新增补偿断言：adr 件内对票面的引用属活引用（adr 永不删→断链风险常驻），E-ADR-3″ 校验批附带跑 `grep -rno "\.collab/[a-z]*/[^ )\`\"']*\.md" docs/adr/` 存在性逐条 test（缺件读数入回执·advisory 起步）。

## 三、seat-permissions 随动目（更正点名·替代 v2 Y-2 之 architect 目）

1. **作废目**：v2 A.2-3「architect 行补 `.collab/decisions/`（仅 `*ADR-*` 文件名族）」——ADR 不落 decisions，该作废；`.collab/decisions/` 侧 architect 零授权恢复原状。
2. **新目**：architect 行补 `docs/adr/` write_globs 行＋**同席 deny_globs `docs/**` 行同步开口**（改 `docs/**` 为不排除 adr 子面的形态，具体机械写法随 T08R 权限表施工票定形；两行必须同批，缺一即写侧 fail-closed＝新立残留窗口，引 v2 C.2 第 3 目「同批清零」同款纪律）。
3. **不变目**：host 行补 `.collab/decisions/`（裁定登记誊录通道）＝v2 Y-2 原样有效。
4. 施工归口不变：与 T08R 权限机件同票，避两次动权限表。

## 四、引用账

本批新增依据＝裁定件本体（四件套：`.collab/decisions/2026-11-03-皮总裁定-ADR正件落位docs.md`／2026-11-03／§一裁定原文＋§二.3 落位改定款／仓内路径非 URL）；业界落位与「superseded never deleted」依据沿用 v2 引用账 #1/#2/#3/#4 不动。

## 五、回执（v3 起草笔）

- 开端 HEAD 实测＝`5358ea4`；本笔单独 commit（`collab:` 前缀·只含声明闭集 1 件）；禁 `--no-verify`、禁 amend；门禁拦截如实报告不绕闸。
- v1/v2 原地不动作史述；本 v3 为定标真源。
- 覆盖条目处置一句话：ADR 正件族落位改 `docs/adr/NNNN-slug.md`（业界惯例子形态·定标理由三条），docs 成两面制（三件套交接面「被取代即出」明示不辖 adr 面＝adr 决策日志面与 decisions 同权永存），E-ADR/E-ARC 机理零动只换落位与扫描面，权限随动＝architect 行补 `docs/adr/`＋deny 开口同批、host 行不变。
