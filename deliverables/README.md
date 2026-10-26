# deliverables/ 索引

> 规则：本目录根**只放本索引**；对象按类型入五类子包（裁-38 Q2=A：`skills/`、`experts/`、`nodes/`、`tickets/`、`documents/`；`experts/` 原名 `profiles/`，2026-10-26 皮总拍定更名——专家包对象应归 experts）；新增对象先定类型再入对应子包，并在本索引登记一行。

## skills/ — skill 对象

| 对象目录 | 内容 | 版本·状态 |
|---|---|---|
| `skills/object-audit/` | 对象审计总入口（骨架＋7 对象判据分件） | v0.5 · 活跃（2026-10-23 增 `70-provenance.md` 规范来源声明·9 分件；裁-21 三条 L0 划界——T1/S1 date 豁免·D6 指针 vs 提及；裁-23 落地——S1/T1 改名史实句豁免·S-02 默认域排除 `.collab/`·规范件人名泛指化；裁-25 账本日期豁免＋SKILL.md 出生声明块；批 29 五类子包路径适配——S-01/S-02/S-04/run-gates 扫描域与解析双域化） |
| `skills/object-build/` | 对象构建总入口（三问＋六步＋6 分件：skill/装订/角色/票/目录/发布） | v0.5 · 草稿（2026-10-22 并入票构建真源 `40-ticket.md`＋目录治理 `50-directory.md`；2026-10-23 增 `60-publish.md` 发布形态真源；裁-25 §四 `copy:` 变量式＋S-05 `object-build/scripts/publish.py` 落地；裁-28 `publish.py --prune` 白名单收缩入口＋§八 prune 项对账豁免；批 29 五类子包路径适配——publish.py 包定位 resolver 双域） |
| `skills/multi-collab/` | 协作纪律（权限分级版：唯一写权＋开放读权席位＋md 交接件机制） | v4.4 · 活跃（2026-10-22 由 tri-collab 改名·主文件＋7 分件；裁-25 SKILL.md 出生声明块＋判词机检最小约定入 `60-gates.md`；裁-28 判词分账 `verdicts.md`＋G-1 关账登记＋Q5 关账注；v3.3 交接区边界定死为 .collab/**；v3.4 真源归属反转——本器＝协作纪律真源；v3.5 读域隔离强制边界写明（SKILL.md 是声明不是执法）；v3.6 主文件补读域边界指针（最小加载面同步）；v3.7 增 `60-gates.md` 出口路由·退出码·升级；v3.8 评审席须异后端（登记项·同后端判定不计入判定链）；v3.9 判词与流水分治；v4.0 派遣合规判据（A-3·约束行必含「六道硬约束」串·缺＝不合规派遣）；v4.3 R2 顾问提交件三制（A-17 轮次戳·三档表态·讨论轮机制·见沿革 `90-changelog.md` v4.3 条）；v4.4 R2 市场事实库与引用治理（A-15）＋`60-gates.md` 退出码家族注记（见沿革 `90-changelog.md` v4.4 条）。〔注：v4.1–v4.2 沿革已于 2026-10-25 补登记入 `90-changelog.md`「补登记（2026-10-25·主理人令）」节·取证 commit `a2caa4f`／`b8f8dda`〕） |

## experts/ — 专家包对象

| 对象目录 | 内容 | 版本·状态 |
|---|---|---|
| `experts/hjh-aigc-video-team/` | AIGC 视频团队（Team 型专家团·7 席位·多模态生成为生产手段·项目圣经＋五道人类确认闸 G1–G5：主理人/策划/编剧/美术指导/导演/剪辑/运营） | v1.5.0 · 活跃（源＝my-experts 注册态 `plugins/aigc-video-team/` 只读复制；批 28 AIGC 返工＋批 30 项目圣经（裁-41）＋批 32 五道确认闸（裁-44）经 gate-qa 复核后由主理人执行专家包面重装 v1.3.0（史实锚不改），批 3a 升 v1.4.0（`2d317c1`）；本目录为其注册态快照（运行时产物 .pending-preview-session 不入快照不入 zip）；批 29 入仓；v1.4.1 三席改名（皮总拍定）；v1.5.0 包 id 更名 aigc-video-team→hjh-aigc-video-team（皮总拍定 2026-10-26）） |
| `experts/hjh-software-team/` | 软件开发团队专家包（Team 型·5 席位：交付总监/产品经理/架构师/工程师/QA·市场 v1.1.0 fork·自维护） | v1.2.0 · 活跃（源＝市场包 `software-company` v1.1.0 fork（下载戳 2026-10-09）；fork 改动三项＝plugin.json 注册形态适配＋lead 改名 `software-company-team-lead`＋版本升 1.1.1（Q5），五席 MD 逐字照录；收编批 T-A1 落盘，改定义只改仓内真源、部署面只准从仓内复制；v1.2.0 包 id 更名 software-company→hjh-software-team（皮总拍定 2026-10-26）） |

## nodes/ · tickets/ · documents/ — 占位

| 子包 | 状态 |
|---|---|
| `nodes/` | 空·占位（流程/工序节点定义对象；迁入时须在本索引登记） |
| `tickets/` | 空·占位（票卡/批次对象；迁入时须在本索引登记） |
| `documents/` | 空·占位（治理文档/台账对象；迁入时须在本索引登记） |

**已退役（2026-10-22·决策者拍·三技能合并）**：`plan-tickets`、`ticket-flow` —— 有效内容全部并入 `object-build/references/40-ticket.md`；原件按 `SKILL.md.retired` 先例改名归档（史实锚保留）。上游 `to-tickets`（matt pocock）**不碰**，仅作只读参照系与细则指针（spec-cross-audit 10 检）。

`video-team/`（2026-10-23·裁-38 概念纠偏撤包——专家团误做成 skill 形态，本体只认专家包轨 aigc-video-team；git 史 b2933cc/c2931d5 留痕）

**未迁入（留用户级 skill 库·是否迁入待拍）**：doc-governance、skill-contract-audit、identity-governance。判据见 `.collab/decisions/2026-10-22-裁决记录.md` 候办第 5 条；迁入时须同步处理原件指向，避免双真源。其中 identity-governance 系交接核验补登的**暗依赖**（补登日期见裁决记录）——此前三方（交接单/本索引/裁决记录）均漏登记，而 `multi-collab/SKILL.md` 与 `multi-collab/references/50-antipatterns.md` 两处活指针指向它。
