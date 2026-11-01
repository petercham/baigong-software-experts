# fuxi-skill · active 生效池（产物存放约定件）

> 性质＝交付件约定面（自包含成文）。本目录＝`-perspective`／`-technique`／`-bundle` 产物的 active 生效池注册路径；约定件与留档区约定件（`deliverables/skills/fuxi-skill/rejected/README.md`）同款留档约定。
> 记法：R<n>＝决策清单条款；AC-<n>＝`deliverables/skills/fuxi-skill/contracts/artifact-contract.md` 节号；ST/FC/BW/GS-<n>＝`deliverables/skills/fuxi-skill/gates/assertion-catalog.md` 断言编号。正文零过程域指针；命名英文 kebab。

## 一、生效池定义（R16 落盘约定）

- active 生效池＝产物目录注册路径＝`deliverables/products/`（与 `deliverables/skills/` 同级的交付面路径；产物＝独立 skill 本体，不与工具包目录混放，隔离扫描基面干净）。
- 每产物＝独立 skill 本体目录，目录名＝`<对象名kebab>-perspective`／`<对象名kebab>-technique`／`<对象名kebab>-bundle`（kebab 纪律）。
- 入池前置（自动调整产物处置三定义域口径照引）：写入本池必须经**人工确认＋独立提案＋版本审计**；确认前产物落待确认暂存区（约定名 `pending/`）；`archive/`＝历史记录区（过程留痕／工具运行证据），免产物级机检，装载不被触及。
- 判别口径双证据＝生效区字节哈希＋装载记录（R16），缺一即视为改动生效产物；装载记录侧当期环境实证不可得（缺口在册＝`deliverables/skills/fuxi-skill/gates/validator-catalog.md` §5.1，不重复造桩）。

## 二、当期读数口径

- 机检＝FC-6：本目录 listing＋每条目人工确认引用行扫描；目录不存在＝PENDING（ST-5 先例）；目录在场且空＝空扫描合法态判绿。
- 当期读数＝无人工确认来源条目数 **0**——此 0 属**空池平凡真**（规程级实证），非产物级实证：验收行不得表述为「active 池健康」类产物级绿；产物级实证随真实蒸馏首单接入时复跑。
- 三态注：规程级（约定件＋空池在场＝当期绿）／待数据（产物条目到位后逐条验确认引用行）／环境不可得未验（装载记录侧）。

## 三、条目确认引用行格式（机读钉死）

每个产物目录根部的确认件（约定文件名 `confirmation.md`，随首份产物入池时随件创建），其内含机读引用行（格式钉死，FC-6 扫描对象）：（约定名当期未建档·非仓内指针·外部仓豁免口径注明：首份产物入池时随件创建）

```json
{"字段注册": ["产物id", "人工确认引用", "提案件引用", "版本审计引用"]}
```

- 四字段在场非空；`产物id` 须与目录名逐字全等；`人工确认引用`＝看板「人工闸结论」栏引用或确认记录件路径（指针形态允许）。
- 缺 `confirmation.md` 或任一字段空＝该条目计「无人工确认来源」，FC-6 咬（验收判据＝该计数＝0）。（约定名当期未建档·非仓内指针·外部仓豁免口径注明：首份产物入池时随件创建）
