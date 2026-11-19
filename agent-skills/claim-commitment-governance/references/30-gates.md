# 30-gates · 脚本闸、负样本闸、调用契约

> 本文件只持判据编号与判据句；字段闭集、相容矩阵、状态语义、词表、抽取模式一律指针 `references/10-contract.md`，不复写。判据行可复述所判的判定条件，但复述处须标 `→ §N.M`，且被引编号必须存在于 `10-contract` 对应小节内。

## 1. 人工闸消费点（不复制条文）

人工闸七类的**唯一正文在 `references/10-contract.md §8`**。本文件只规定四处消费点与所需证据：

- 外发前（`gate-outbound`）：`10-contract §8` 第 2 类与第 6 类必须有 `authorization` 记录，缺则不得置 `send_channel=approved_send`。
- 降级或豁免（`validate`）：`10-contract §8` 第 3 类与第 4 类必须有 `approver` 形如 `human:<ref>`，席位或系统签署不足以成立。
- 外部权威与法律合同解释（`validate`）：`10-contract §8` 第 1 类与第 5 类在人类签署前，相关主张 `status` 不得为 `accepted`、`authority` 不得为 `binding`。
- 沉默效力（`reconcile`）：`10-contract §8` 第 7 类不自动成立；超时只产生复核项，不产生状态迁移。

## 2. 脚本闸 R1–R17

| 编号 | 判据 |
|---|---|
| R1 | 字段闭集合规：`claim_type`、`source_layer`、`evidence_tag`、`authority`、`status`、`external_effect`、`assertion_form`、`required_environment`、`required_checks`、`actual_environment`、`actual_checks`、`qa_result`、`exemption`、`completeness_mode`、`outbound_type`、`send_channel` 逐一落在 `10-contract` 第 1、3、4、6 节给定闭集内 → §1 §3 §4 §6。 |
| R2 | 引用闭合：`linked_artifacts` 至少含一条 `source:` 或 `cite:` 条目（编号形态，或 `10-contract` 第 11 节无号写法的自由文本降级形态）；**编号形态条目**的前缀落在 `10-contract` 第 1 节引用前缀闭集内；**在册解析判的实施边界（不得外推）**＝`REQ-`／`CMP-` 类编号在登记表内解析判（`regids`），来源面／绑定层号（`INTK-`／`RES-`／`MSR-`／`DOC-`／`DEC-`／`AUTH-` 等）的在册性在本包机检面之外（无绑定层注入面），该面为**登记性说明**＋欠条 `30-gates` A4 人工闸承接；**降级形态条目**（`source:`／`cite:` 后非 `PREFIX-digits`）不参与解析判，但所在主张行 `authority` 必须为 `unverified`——判据同第 11 节正向可判条件，`authority ≠ unverified` 即违例；**条件格旁路（例外）**＝行级三条件成立的行（`approver` 形如 `human:<ref>` 且 `status` 在条件集内且 `expiry ≠ none`），本支不判行级 `authority`——**旁路判与该行 `authority` 取值无关**（判据同源复用，与 R7 条件格同一判据，不得另立）；旁路只免行级封顶，在册性照旧 A4 登记、证据纪律照旧 §9；`artifact:` 与 `authorization:` 只能附加；`actual_environment = production` 时，`linked_artifacts` 须含至少一条 `artifact:`，且该 `artifact:` 须在表 A/B/C/D 的编号面内可解析 → §1 §11。 |
| R3 | 登记闭包：每个被引 `claim_id` 必须属于唯一主张登记表已登记集合且 `status ≠ superseded`；允许真子集，禁止未登记引用与回引已作废主张。 |
| R4 | 验证对账四支：①`actual_environment` 序位不低于 `required_environment` 序位，且 `required_checks` 为 `actual_checks` 子集，任一不满足须 `exemption ≠ none` → §3；②`unverified` 视为未达任何要求环境，配 `qa_result ∈ {passed_at_actual, passed_with_exemption}` 即违例；③`original_requirement_ref ≠ none` 时，`required_environment` 序位不得低于表 C 该 REQ 行 `req_required_environment` 序位，`required_checks` 必须包含该行 `req_required_checks` 集合，除非 `required_change_record ≠ none` 且其签署为 `human:<ref>` 且该 `<ref>` 与同 `claim_id` 表 A 行 `approver` 列同值；**该同值判对本表所有行生效，无论 `original_requirement_ref` 是否为 `none`**——表 A 该列为 `none` 而记录非 `none` 即违例；④`required_environment ≠ none` 或 `required_checks ≠ none` 时，`original_requirement_ref` 不得为 `none`。 |
| R5 | 批准与时效完整六支：①`exemption ≠ none` 须齐 `approver`、`reason`、`scope`、`expiry` 且均非 `none`；②`exemption ≠ none` 时 `fallback_criterion` 与表 D `reopen_trigger` 均不得为 `none`；③`status = frozen_assumption` 须齐 `expiry`、`review_owner`、`reopen_trigger` 且均非 `none` → §7.2；④`approver` 与 `generated_by` 均须符合 `kind:ref` 格式；⑤同一 `claim_id` 的表 A `reopen_trigger` 与表 D `reopen_trigger` 均非 `none` 时必须同值 → §3。 |
| R6 | 外发授权与审查独立：`external_effect = outbound_authorized` 或 `send_channel = approved_send` 须有 `authorization` 且其签署人等于 `approver` 的人类主体；`fact_review` 与 `commitment_review` 的审查人不得等于 `generated_by`，两名审查人互不相同 → §6。 |
| R7 | 来源层与权威相容：`source_layer` 与 `authority` 的组合必须落在 `10-contract` 第 2 节相容矩阵的「允许」格或已满足「条件」判据的「条件」格内；矩阵外组合一律判违例 → §2。 |
| R8 | 证据强度与外发效力三支：①`evidence_tag ∈ {UNKNOWN, STALE}` 时 `authority` 不得为 `binding`，`status` 不得为 `accepted`，`external_effect` 不得为 `outbound_authorized` → §7.7；②`evidence_tag ∈ {INFERENCE, JUDGMENT}` 时，`external_effect ∈ {outbound_pending, outbound_authorized}` 不得配 `authority = binding`；③`authority = binding` 时 `linked_artifacts` 须含至少一条 `cite:`。 |
| R9 | 内外防火墙与占位闸：外发件不得引用 `status = frozen_assumption` 的主张充当外部确认 → §7.2；`send_channel = approved_send` 时不得残留 `10-contract` 第 5 节占位词表中任一词或未替换的 `〔` → §5。 |
| R10 | 历史不可回写：`superseded` 旧行保留原样，不得覆盖、删除或改写；状态变更只许新增行并记录 `claim_status_delta` → §7.5。 |
| R11 | 同键同值：表 B 内 `cmp_key` 相同的多行，其 `cmp_value` 必须全等——`cmp_kind=quantity` 比数值，`cmp_kind=datetime` 比时点，`cmp_kind=identifier` 比被引编号，`cmp_kind=completeness` 比 `completeness_mode` 与两个计数的组合。触发条件是 `cmp_key` 相等，不以 `source_artifact` 是否相同、不以任何可选字段是否填写为条件。**附加支（`source_artifact` 的消费点）**：该列必须非 `none` 且形如 `artifact:<PREFIX>-<digits>`（前缀落在 `10-contract` 第 1 节引用前缀闭集内）；同一 `cmp_key` 下行数 ＞ 1 时，这些行的 `source_artifact` 不得全等——同键多行的意义就是「同一对象由不同工件各自给出数值」，若来源全等则不是跨件比对点，判违例 → §4。 |
| R12 | 完备性计数三支：①`cmp_kind=completeness` 须 `enumeration_count > 0`，且 `completeness_mode=cleared` 时 `remaining_count = 0`、`completeness_mode=partial` 时 `remaining_count > 0` → §4；②`enumeration_count` 不得小于该主张 `original_requirement_ref` 所指表 C 行的 `req_enumeration_base`（该行该列为 `none` 时本支跳过）；③非 `completeness` 类断言的三列 `completeness_mode`/`enumeration_count`/`remaining_count` 必须均为 `none`。 |
| R13 | 责任主体与依据五支：①`source_layer` ∈ 1–4 层时 `accountable_party` 不得为 `none`，且 `responsibility_basis` 不得为 `none`；②`requestee` 不得单独充当 `accountable_party`；③`decision_owner` 只对 `authority ∈ {binding, consultative}` 强制非空，`authority ∈ {internal_only, unverified}` 时允许为 `none` 并单列；`authority = binding` 时 `approver` 必须以 `human:` 起头，且其 `<ref>` 部分与 `decision_owner` 的 `<ref>` 部分相同；④编号与角色不得自产：`source_layer` ∈ 5–6 层且 `accountable_party = none` 的主张须在聚合与判词单列「无责任主体主张」，禁以硬编主体填充；承载＝`20-artifact-mapping` 第 1 节交付汇总单列区；机检＝R13 第五支；引用型字段无编号时只能填自由文本并标 `unverified`，禁造号；角色引用无角色册时允许 `<role-kind>:<自由描述>`，不得留空、不得编位号；⑤单列区对账（**仅 `reconcile` 面消费**）：被校件集合同时含登记表与交付汇总时，交付汇总单列区条数须等于表 A 中 `source_layer` ∈ 5–6 层且 `accountable_party = none` 的行数，且三元素（条数／`claim_id` 清单／不可归属原因）齐；被校件集合不含交付汇总时本支跳过（机检边界如实登记，不外推）。 → §1 §11。 |
| R14 | 断言形态自陈与语境化抽取三支：①`assertion_form = qualitative` 的主张文本不得命中 `10-contract` 第 4 节数量（阿拉伯）、数量（中文）、时点、完备性任一语境化模式；②`assertion_form ≠ qualitative` 时 `comparability_ref` 不得为 `none`；③`comparability_ref ≠ none` 时其 `CMP-` 编号必须命中表 B 某行的 `cmp_id`，且该行 `claim_id` 与本主张的 `claim_id` 相同 → §4。 |
| R15 | 外发件主张闭集一致：外发门 `claims` 字段列出的 `claim_id` 集合，必须与主张引用区表内 `claim_id` 列集合全等；正文每条承重主张须回指表内某个 `claim_id` → §6。 |
| R16 | 标识与需求主表可解析四支：①`assertion_form=identifier` 的主张其 `cmp_value` 必须在表 C 已登记且 `definition_ref ≠ none`；②`original_requirement_ref ≠ none` 时必须命中表 C 中以 `REQ-` 起头的 `id_value` 行，且该行 `status = defined`；③表 C 中 `id_value` 以 `REQ-` 起头的行，其 `id_key` 必须为 `需求`；④`id_value` 不以 `REQ-` 起头的行，其 `id_key` 不得为 `需求`（需求条目只认这一种识别口径）→ §4。 |
| R17 | 登记表唯一性：`01` 模板四张表的表头列名序列必须与 `10-contract` 第 1 节（表 A）、第 3 节（表 D）、第 4 节（表 B、表 C）的字段序列逐列全等，不得增减列或改序。**机检覆盖面（不得外推）**：`c06` 只承担「表头列序逐列全等」与「表 A 表头在本包内唯一」两项；「每个项目只有一处 A／B／C／D」属**项目级唯一性**，包内无第二个项目实例可判，归 T2 `reconcile` 承担；表 B／C／D 的**表头在本包内唯一**亦归 T2（本包只对表 A 断言唯一） → §1 §3 §4。 |

## 3. `semantic-governance` 三子命令调用契约

脚本本体、闭集配置与夹具属 SEMGOV-T2；本文件只定调用契约与判据归属。依赖记号见第 5 小节。

| 子命令 | 用途 | 通过 | 不通过 |
|---|---|---|---|
| `validate --artifact <file> --kind <artifact-kind>` | 单件：R1、R2、R5、R7、R14、R16 与必填面 | exit 0 | exit≠0，输出违例字段与判据号 |
| `reconcile --artifacts <file-list>` | 跨件：R3、R10、R11、R12、R13、R17 | exit 0 | exit≠0，输出差异集与判据号 |
| `gate-outbound --artifact <file>` | 外发前：R4、R6、R8、R9、R15 与人工闸消费点 | exit 0 | exit≠0，且不得把工件标为可外发 |

## 4. 负样本闸 N1–N10 与人工闸承接项 A1–A4

每条负样本必须让**其声明的那一支判据**变红；由别的判据顺带命中不算通过（那叫假阴）。每条须写明「变异由哪条判据的哪个比较目标生成」。

**这一段是 §4 的元规则本体，不是说明性前言**：负样本的通过条件**不得**被放宽为「任一判据变红即可」——两者是不同的断言，后者会把「声明的那一支根本没被造出来」的假阴全部变成通过。本段与下表同受机检：本段取摘要，表内每行的「应咬判据·支」列逐行受检；改义即红。

| 编号 | 负样本 | 应咬判据·支 | 变异生成源 |
|---|---|---|---|
| N1 | 原始需求为真实联调，主张却初始写 `required_environment=mock`，`exemption=none`，无 `required_change_record`。 | R4·第三支 | 表 C `req_required_environment` 比较目标 |
| N2 | 子集实现被声明为全量：`required_checks` 含 `security`，`actual_checks` 缺 `security`，`exemption=none`。 | R4·第一支 | 集合包含比较目标 |
| N3 | 有书面批准但无实测读数：`approver=human:<ref>` 在位，`actual_environment=unverified`，`qa_result=passed_at_actual`。 | R4·第二支 | 环境轴 `unverified` 与 `qa_result` 的相容目标 |
| N4 | 降级（`exemption=partial`）无 `fallback_criterion` 或无表 D `reopen_trigger`。 | R5·第二支 | 表 D 两列非 `none` 约束 |
| N5 | 外发件把 `evidence_tag=UNKNOWN` 的主张写成 `authority=binding`。 | R8·第一支 | `evidence_tag`×`authority` 相容目标 |
| N6 | 内部 `frozen_assumption` 主张被外发件引作外部确认。 | R9·第一支 | `status`×外发引用面 |
| N7 | 完备性断言 `completeness_mode=cleared` 而 `remaining_count=1`；或 `enumeration_count=0`。 | R12·第一支 | `completeness_mode` 与 `remaining_count` 的取 0 目标 |
| N8 | 验收对象替换：`actual_environment=production`，但 `linked_artifacts` 无任何 `artifact:` 指向实测读数件。 | R2·第三支 | `actual_environment`×`artifact:` 存在性目标 |
| N9 | 时间与产物不绑定：读数件时点晚于 `expiry`，仍把 `qa_result` 记为 `passed_at_actual` 且无批准续期。 | **不可机检**——由人工闸 A1 承接 | 读数件时间戳在本契约管辖的字段面之外 |
| N10 | 分母替换：`cmp_kind=completeness` 的 `enumeration_count` 小于表 C 该 REQ 行的 `req_enumeration_base`。 | R12·第二支 | 表 C 枚举基数比较目标 |

**人工闸承接项（明示不可机检，不冒充机检）**

| 编号 | 事项 | 承接方式 |
|---|---|---|
| A1 | N9：读数件时点是否晚于批准有效期。 | 读数件时间戳属外部产物，本契约无字段承载；若强行为此增设「读数件登记时点」列，等于把证据面塞进主张表，与本批反过度设计冲突。改由 `30-gates §1` 的降级/豁免消费点在人工闸 3 类处核验，并在 QA 判词人工复核清单列出。 |
| A2 | N4 的「回退判据是否可判」（即 `fallback_criterion` 文本本身是否可判）。 | 语义可判性无可靠机检；由人工闸 4 类处核验，机检只保证该列非 `none`（R5·第二支）。 |
| A3 | 表 A／B／C／D 主键（`claim_id`／`cmp_id`／`id_value`）**行级唯一**：同表内重复主键是否可判。 | 行级重复属登记表建行流程的内部约束。`check_r17`（`:855-875`）三支只担表头列序与计数唯一，`30-gates:34` R17 覆盖面明文亦不含主键行级唯一；为其单开 R17 支须跨被校件聚合行数据，与本次「R 号不增、R17 覆盖面不外推」边界冲突（裁定四十二 R-1 优先走人工路线）。改由建行流程（先登记后引用）保证，并由 QA 判词人工复核清单列出主键重复扫描结果。 |
| A4 | **来源面／绑定层编号的在册性**：引用了绑定层未发放的号（`INTK-`／`RES-`／`MSR-`／`DOC-`／`DEC-`／`AUTH-`）。 | 该面真源在包外（项目绑定层／外部登记件），本包无注入面可校——`check_r2` 解析支（`:458-460`）仅对 `REQ-`／`CMP-` 查 `regids`，其余前缀落闭集即放行（自造 `INTK-9999`／`RES-0001`／`DEC-0001` 实测三例 exit 0）。契约侧相应把「可在登记表解析」明写为**登记性说明**（修法见 M-3），由人工闸 1 类（外部权威来源确认）消费点核验＋QA 判词人工复核清单登记。 |

## 5. 依赖面与能力边界

**依赖记号形态**：反引号包裹的 `bundle:` 前缀 ＋ 组件名，**只写包名，不带版本号**。该记号是**人读指针，本包不提供解析器**；机检只断言其形态符合 `^bundle:[a-z0-9-]+$`，且组件名落在下表组件闭集内；存在性与版本一致性由装配期在 `bundle.lock` 的 `ref` 段校验（T3 装配后实测）——一致性比的是清单里的 `ref` 值，本包不写、不读、不比对任何版本号字面。不以仓根相对路径引用跨包文件，跨包规范一律「包名 ＋ 条款名」引用。

**为何不钉版本（本版改判，替代上一版把语义化版本钉在组件名后的写法）**：上一版给五个组件各钉了一个版本号，其中已可取证的两个组件版本与实物 frontmatter 不符（取证记录见出票票面 §0 处置表「修3-15」栏，写明读的是哪两个 `SKILL.md`、读到什么值）；另两个组件在本票出票时仓内无实体（`semantic-governance` 是 T2 交付物；`deep-research` 未随本仓分发，**但「仓内无实体」不等于「无法取证」**——证据在仓外插件缓存可读域 `…/my-experts/baigong-software-team/0.1.30/` 下的 `deep-research` 装配件，`version: 1.0.2`，两席与主理人已据该装配件核过条款名）。本仓内无对应目录，故不写未经本仓取证的版本数字；取证口径按装配件、不按本仓路径。本包**不消费版本号**——判据只验记号形态与组件名，不读版本段；钉死版本只会让 T2／T3 装配后任一方升级即把本包误判为红，且错值会被 T3 照抄继承。故一律不钉版本，版本一致性归 T3 承担。

| 组件 | 承担面 |
|---|---|
| `bundle:semantic-governance` | 校验脚本、闭集配置与负样本夹具（SEMGOV-T2）。 |
| `bundle:external-advisor-collab` | 外部引用四件套（`external-advisor-collab 谁主张谁举证`）。 |
| `bundle:deep-research` | 证据标签与措辞分级（包内 `SKILL.md §六 证据纪律`「标签闭集（五标·英文）／措辞分级」）。 |
| `bundle:object-audit` | 审计判据与发布闸（`check-skill-meta`、`check-provenance`、`check-entity`）。 |
| `bundle:sop` | 票型、状态机、租约。 |

**跨包条款名对照（本包只引用下列条款名，别名一律判违例）**：

| 组件 | 条款名写法 | 取证口径 |
|---|---|---|
| `bundle:semantic-governance` | 无跨包条款 | T2 交付物未出 |
| `bundle:external-advisor-collab` | `external-advisor-collab 谁主张谁举证` | 仓内可核 |
| `bundle:deep-research` | `deep-research §六 证据纪律` | 部署件已核（0.1.30，`version: 1.0.2`） |
| `bundle:object-audit` | `object-audit S3`／`object-audit S5` | 仓内可核 |
| `bundle:sop` | 无跨包条款 | 仓内可核 |

**这张表的用法（治红4-03：跨包条款名虚指是判据盲区）**：跨包条款一律以「包名 ＋ 空格 ＋ 条款位置」书写，条款位置写小节标签（`§六 证据纪律`）或条款标题（`谁主张谁举证`/`S3`/`第 3 步`）；**不得以他包的包内文件名充当条款位置**（即写成「某包 ＋ 某个 `xx-format` 式文件名 ＋ 条款」这种形式判违例——本包无法核他包的文件与节结构，那样写等于让条款名不可取证）。第三列只允许四值：`仓内可核`／`部署件已核（0.1.30，`version: 1.0.2`）`／`T2 交付物未出`／`无跨包条款`——取证口径本身是闭集，不许写「大概」「应该」。

**能力边界声明**：本文件不声称下列能力，下列能力由对应组件承担，本文件只留指针——脚本实现与负样本夹具（`bundle:semantic-governance`）；外部引用四件套（`bundle:external-advisor-collab`）；证据标签与措辞分级（`bundle:deep-research`）；审计判据与发布闸（`bundle:object-audit`）；票型、状态机、租约（`bundle:sop`）。
