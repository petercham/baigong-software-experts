# SWB-B3 · 过程域搬家回执（engineer-b3 施工席）

- 被回执票＝`.scratch/tickets/2026-11-03-SWB-B3-process-domain-migration-ticket.md`（`d584d7b`）＋rev2 补丁件（`ab8b8b9`·冲突以 rev2 为准）。
- **开工 HEAD 实测＝`5b5bcf2`**（B2 收口登记笔·`git log --oneline -3` 确认）；开工 `git status --short`＝仅两支 2026-11-01 TKT untracked 旧件（随批入库✓）。

## 一、逐笔 commit 链

| 笔 | hash | 目 | name-status 读数 |
|---|---|---|---|
| B3a | `b29bc20` | 换锚先行（硬线）＋Y-7 闭环化先行 mv＋B2 路由并入项 | 5×R100＋101 件文本面＋6 机件/SKILL 锚改写＋7 壳 README |
| B3b | `5eb2381` | tickets 搬家 | 84×R100（百工53/fuxi21/eac10）＋旧桶目录随空自灭 |
| B3c | `47fd524` | qa/receipts/board/design 四桶＋仓根散件 | 266×R100（qa167/receipts53/board1/design24＋根散件 tracked 21） |
| B3c2 | `4a73f3e` | decisions 归项目＋evidence 2 支 tracked 单列 | 15×R100（decisions 余 13＋evidence 2） |
| B3d | `f0e2616` | research 分桶＋era 留置 | 215×R100（百工195/eac13/fuxi7）＋era 26 条留置 |
| B3e＋B3g | `f4570f9` | 未入库大块字节 mv＋旧仓根 docs 8 件分流＋随动 README | 8×R100（docs 面）＋1 M（.scratch/tickets/README）＋untracked 面文件系统 mv |
| 回执 | 本笔 | 本件＋附件逐件表 | 1 A＋1 A（附件 tsv） |

- 誊写禁令（裁定 `f5a0d96`）照执：tracked 面全程 `git mv`＝**593 笔 R100·零非 R100**（附件＝`2026-11-03-SWB-B3-receipt-附件-逐件R100表.tsv` 593 行）；untracked 大块＝同盘（D:）`shutil.move`＝os.rename 字节搬运·零重新输出。
- 改锚笔与 mv 笔的混笔注记：B3a 内含 5 支 Y-7 先行 git mv＝票面 Y-7 闭环化换锚先例口径强制（spec_file 锚指票面件·不先行 mv 则改锚后 provenance exit 3 必红——实测死锁坐实），回执分账在册。

## 二、开工基线两栏（rev2 补丁五之 1）

| 面 | 票面起草读数（`f017a51` 锚） | 开工实测读数（`5b5bcf2` 首步重取·立账基准） |
|---|---|---|
| tracked `.collab`＋`.scratch` 同域 | 597 | **621** |
| tickets / qa / receipts / decisions / design / research / board | 85/159/51/16/24/242/1 | **85/165/53/16/24/242/1** |
| 仓根散件 tracked | 17 | **21**（含 4 支 ES/SWB 登记件后续笔入库漂移） |
| evidence tracked | — | **2**（rev2 补丁四两支·判词/回执 team-rename-01） |
| docs tracked | — | **8** |
| refs / evidence / inbox / dispatch（untracked find） | 8835/3827/9/10 | **8835/4017/9/10**（evidence 门禁续写漂移在册·4017→4022→…随每跑门禁续增） |
| era 命中（research tracked·quotepath=off 钉口径） | — | **26** |
| 项目侧 `.collab/.scratch` 壳件 tracked | — | **7**（B1 壳 README×7） |
| 门禁开工基线 | 631（B1 期值·参考） | **GATE PASS 648**·族集＝EAC-L1×17／EAC-L2×18／OA-D6-3×88／OA-D6-4×19／OA-D6 BLOCK×23＋WATCH×15／MC-SOT-1×54／MC-SOT-2×413／reconcile commit×1（OA-T1 零实例） |

## 三、判据逐条读数（全部实测落盘）

1. **B3a 跑绿＝mv 前置断言（rev2 补丁三换代式·扫描面闭集 for 式）**：`for d in .collab/receipts .collab/qa .collab/design .collab/decisions .collab/dispatch docs README.md deliverables; do grep -rno "\.collab/tickets/" "$d"; done`＝**0**（换锚前同式实测＝174 occurrence/104 件）。史述豁免（逐处登记·形态保持改写非删除）：皮总裁定-票面落位件 L12／v3 基线件 L60＋L96／PM-SWBRELOC 审票 L28＝4 处（旧前缀字面→无歧义形态词·语义零改）。票面原式（全仓 grep＋两豁免）按 rev2 作废。
2. **tracked 总数守恒（rev2 补丁五之 2·双侧同域口径）**：开工 621（旧域）＋7（项目侧壳）＝**628** → 收口 38（旧域残）＋600（项目侧）＝**638**＝628＋2（TKT 两支入库）＋8（docs 侧迁入）✓ 精确全等。docs 侧另账独立断言：开工 `git ls-files docs/`＝**8** → 收口＝**0** ✓。逐桶相等核：tickets 85＝Σ项目 `.scratch/tickets` **85**✓；qa 165＋2＝**167**✓；receipts 53＋21 根散件＝**76**（Σ项目 74＋旧域 `.scratch/tickets` B 批票 12 另计·见注）✓；design **24**✓；decisions **16**✓；research 现位 248＝Σ项目 222＋era 留置 26＝开工 242＋docs research 迁入 6 ✓（留置件明细见判据 5 注·随正笔 `QA-B3` 黄目①：原表述「242＝Σ222＋era 20」系分解式误写，正解即本式）。board **1**✓。
   - 注：根散件 21 全归 receipts（票面归桶定标：收口报告/登记/呈报/处置注记→receipts·裁决本体零存在根面）；receipts 桶 74 项目侧＝53＋21。
3. **字节一致**：`git log --name-status -M 5b5bcf2..HEAD` 全 593 笔搬家目＝**R100 占比 100%**·例外＝无。
4. **untracked 面守恒（以开工实测栏为基）**：refs **8835＝8835** ✓（百工 external 26＋eac engine-snapshots 530＋skills-research 8279）；evidence 开工 4017 → 项目侧 138＋仓根残 3927＝4065＝4017＋48（漂移全数＝`gates/` 出口②随本票门禁六跑续写·续写面在册）＋era 留置 1 计入对账 ✓；inbox 9＝3（eac）＋6（仓根 `主理人/` 留置）✓；dispatch 10＝7（百工）＋3（era 派工书留置）✓；process 0✓。
5. **旧域清零**：`find .collab -type f`＝**3971**＝era 留置（research tracked 26＋dispatch era 3＋evidence era 1）＋仓根活写面留置（`evidence/gates` 3934＋`inbox/主理人` 6·run-gates 出口②③硬编码仓根＝B1 随注承接 B4/B5·过渡态在册）＋`tmp-w7-msg.txt` 1（gitignore 排除面 untracked·留置）。`find .collab/tickets`＝**0**（目录灭）✓；`find docs`＝**0**（B3g 后目录随空自灭＝B5-D 残壳断言自洽）✓。
6. **门禁零回归（族集口径）**：收口跑＝**GATE PASS exit 0**（发现 8684·均②路由）；族集对开工基线＝**NEW none**；GONE＝reconcile `commit` 族 ×1＝**过渡态在册不判红**（缺省票目录 `.collab/tickets` 空→零票零发现＝票面预告「扫描面非空危险形态」B4 必修目窗口读数）；裸实例计数增长（OA-D6 BLOCK 23→3773 等）全为在册族实例＝换址既有族实例成立（B2 先例口径·不作判据）。
7. **两支 untracked 入库**：`git ls-files | grep 2026-11-01-TKT-双席审计/最终分票`＝**2** ✓（归桶＝分账函数规则 1→**baigong `.collab/qa/`**·v3 L70 erratum 见§五）。

补（rev2 补丁四三断言）：evidence git mv 后收笔时点 `git status --porcelain | wc -l`＝**0** ✓；`git ls-files agent-experts/baigong-software-team/.collab/evidence/ | grep -c team-rename-01`＝**2**（不被 B1 过渡块 ignore 吞）✓；B3e 其余 evidence 面走文件系统 mv 零改 ✓。

## 四、B3a 换锚明细

- 文本面＝扫描面闭集内 101 件 162 occurrence：具名引用 108 处→`<所属项目>/.scratch/tickets/<基名>`（分账函数）；泛引用/命令片段 54 处→`.scratch/tickets/` 项目中性新位（B4 缺省票目录语义）。
- spec_file 锚改写 8 处＋先行 mv 5 件（Y-7 闭环化·clause_sha256 零动·锚＝条款文本非路径）：check-collab-lint L5/L14/L23→`agent-skills/external-advisor-collab/.scratch/tickets/2026-10-30-EAC-SK5-机检票.md`；check-provenance L14＋multi-collab/object-audit/object-build SKILL.md→百工 decisions 裁决记录；tools/check-source-of-truth L5/L14/L23/L32→百工 research 交接件＋百工 decisions 皮总拍板 10-25；bundle-assembly-registration SKILL.md→百工 decisions 皮总拍板 10-26。改后 check-provenance exit 3→**0**、check-source-of-truth exit **0**。
- B2 收口路由并入项（主理人裁·候裁②③）：check-collab-lint L131 `find_root` deliverables→`tools`＋三分类候选；L279 selftest fixture 旧路径→新树（`--selftest` 六键对拍全 MATCH 复绿）；B1 壳 README 预登记行 collab-fixed-structure 悬空 ×7→`agent-experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md`（新位实存）。
- **B3a 门禁随动行（主理人批准①入册·`b29bc20` 在笔）**：`check-entity.py iter_scan_files` 目录剪枝增 `.collab`/`.scratch` 两段（一行）。依据＝该脚本自注「扫描域＝规范件…仍不接受扩到记录件（.collab/** 等）」＋check-pointers 裁-23 排除 .collab 先例；目录重整＝既有语义物理化，非门禁语义变更（主理人裁定用语）。
  - 对照读数（随动条件⑴）：**开工基线＝OA-T1 族零实例（GATE PASS 648 内该族零出现）**；不剪则搬家件入三分类目录即触发 OA-T1 BLOCK 新族（date×10＋drive-path×15＋ticket-no×2 实测＝新族红→pre-commit 真拦→B3b 起机械锁死）；**剪后 B3b 起各批复跑＝四模式（date/drive-path/discipline-no/ticket-no）全 count 0·entity exit 0·门禁输出内 OA-T1 findings＝0（仅 coverage 行非发现）**——收口复跑读数在册（GATE PASS 8689 笔内 OA-T1 零发现）。
  - **B4 收账登记（随动条件⑵）**：该行＝**B3a 已落·B4 收账**（B4 票面门禁机件闭集含 check-entity 同族议题时按已落登记防双治）。
  - **干跑实验全账（随动条件⑶·供 QA 对拍）**：开工基线 GATE PASS 648 → 未剪枝态全量 591 件复制干跑（已清理复原）＝**3988**·族签名＝EAC-L1 17→34／EAC-L2 18→36／**OA-T1 BLOCK 0→5（唯一新增族＝拟拦门族）**／OA-D6-3 88→473／OA-D6-4 19→1029／OA-D6 BLOCK 23→1473＋WATCH 15→470／MC-SOT 54/413 不变／reconcile 1。剪枝后实跑链＝B3a 后 695（NEW/GONE none）→收口 8684→复跑 8689（＝gates 证据续写微漂·族集恒等）；**OA-T1 全程零 findings**。OA-D6 BLOCK 实例 23→3773（收口值）＝全部＝案卷件换址后其内部历史指针在 check-pointers 全仓索引面下重新解析＝既有族实例增加（advisory 路由不拦·B2 BLOCK10→23 先例同口径）。

## 五、erratum 两笔照引（rev2 销账表文本）

1. **v3 §三 L70 TKT 归属勘误**：照引原文「工作区 2 支 2026-11-01 TKT untracked 旧件 | 散挂 | fuxi-skill `.collab\qa\` 入库」——判定依据＝归项目分账函数规则 1（名含 `TKT`→baigong）＋B0 四目④未锁归属（原票勘误注已在位，本回执照引补齐）；两支实落＝`agent-experts/baigong-software-team/.collab/qa/`。不改冻结基线文本。
2. **v3 §二结构图（L40–43 桶名录无 design）与 §三 L64 基线内部不自洽**：照引 §三 L64 原文「`.collab/design/` 17 件 | 混线 | 按案线归项目 `.collab\design\`（设计稿属过程域；其中现行有效设计稿若属交接件性质→docs，按 §二点八 存活判据逐件分）」＋判定依据＝会师件 `3ad4d99` R-4（从 §三 具体申报）。design 桶存在性由 B1 rev2 补丁一（十一桶闭集）承接。实测 24 件（票面 17＝起草漂移·按实测立账）。

## 六、design 24 件去向表（交接件甄别列·rev2 补丁二之 3）

分账结果：百工 15＋fuxi 9（FUXI 系）。逐件去向＝**全 24 件落所属项目 `.collab/design/`（缺省＝过程域）**；交接件甄别＝显式个案登记一件：`2026-11-03-restructure-proposal-draft-v3.md`（B 批迁移基线真源·B4/B5 票面仍在引用＝「现行有效」形态）**本票仍按缺省留百工 design 桶**——其「→项目 docs」升格判据＝§二点八 存活判据终判随 B5 仓根 README 结构索引落笔（回执在册·不提前）。余 23 件＝过程域无争议（历史设计稿/已执行案线）。

## 七、era 移交清单（ESC1 真源·出处二次分账·rev2 补丁五之 3）

**research 留置 26 条**（`.collab/research/` 原位）：

| 出处分账 | 件 | 处置 |
|---|---|---|
| 第三方外部快照（移交候选） | `drafts-2026-10-23/aigc-video-team.zip`（1 件）＋`aigc-video-team/`（**8 件**·实测＝zip 解包件不含目录重复）＋`video-team/` 源料族（15 件·含 original-5）＝**24 件** | **ESC1 移交候选**（件头有源料说明/返工说明在位·随正笔 `QA-B3` 黄目②：原「aigc-video-team/（9 件）＝25 件」计数误，正解 8 件＝第三方 24·总 26 不变） |
| 本仓自产（判词依据） | `2026-10-23-视频团队本体审计_v1.md`＝**1 件** | **不外移·留项目桶**（百工·判词依据件） |
| 外部参照（reference 族·另账） | `reference-2026-10-24/全能AIGC视频创作团队-架构与五维优化方案.md`＝1 件（正则命中计入 26 内） | 参照件·随 reference 族 ESC1 候选 |

（24＋1＋1＝26 合计全等；reference 那件在列 26 条内，按 REFERENCE-SOURCES.md 出处声明＝外部参照＝ESC1 候选。）
**era 族留置（research 外·B3e 二次分账）**：`dispatch/` 派工书 3（R6视频团/R7短剧编剧团/R8导演）＋`evidence/` 施工回执 1（2026-10-28-T-video-research-gate-01）＝4 支留旧仓根同名桶·ESC1 并入消费。
era 计数口径钉＝`git -c core.quotepath=off ls-files .collab/research | grep -cE '视频|video|短剧|导演|编剧'`＝**26**。

## 八、人工分账面（规则 6 缺省＝baigong·逐件清单）

tickets：README／TEMPLATE-票面模板-v2＋qa 24 支（v2.8/v2.9 系列／TKT 系外双席会师件等）＋receipts 4 支（qa-delta1／arch-tk1 过程债×1／draft4/5 intake 登记×2）＋decisions 14 支（皮总拍板/裁定系＋verdicts.md）＋design 15 支（改名设计稿/PRODUCT/adr-retirement 系/repo-restructure/restructure-proposal 系）＋research 196 支（讨论会轮次汇总/呈拍简报/reference 族/圣经整改/拆仓案等）＋board 1＋evidence 2。全量逐件表＝附件 tsv（593 行 R100 名录含归位）。

## 九、过渡态与随动登记（在册·不判红）

- check-ticket-reconcile 缺省票目录＝旧 `.collab/tickets` 已空→票 0 发现 0（GONE 族窗口）＝**B4-A 必修**（双候选枚举＋非空正断言 exit 4）；本票未触碰 reconcile（B4 闭集件）。
- 仓根留置面：`evidence/gates/`（run-gates `EVIDENCE_DIR` 出口②硬编码）＋`inbox/主理人/`（出口③呈拍面）＝B1 随注「run-gates 现仍写仓根且 B4 不改」承接＝B4/B5 治理目。
- `commit-audit.py`（bundle 交付面）L15/L35 活正则 `\.collab/tickets/` 旧路径 2 处＝交付面文件（B3 禁动面·非扫描面）＝B4 闭集随动在册（QA rev2 新黄③承接）。
- `.scratch/tickets/` 仓根仅余 B 批过渡票 12 tracked（B1–B5＋ESC1＋README）＝B5 收口目。
- Matt Pocock 式头部转换＝不做（随裁项＝否·本行登记）。
- D7 衔接（B3f 不施工）：SWB 登记件 v2.9 随 B3e 入 `agent-experts/baigong-software-team/.collab/refs/external/`·字节一致·入库落 docs 归 B5。
- `tmp-w7-msg.txt`＝gitignore `tmp-*` 排除面 untracked·留仓根不搬（B5 gitignore 重写时随判）。
- B2 随注三条照纳：门禁对拍统一＝Temp 三仓并排口径本回执未跑 Temp 面（真仓对拍值已落·Δ 全等由 QA 席并排复核）。

——engineer-b3 · SWB-B3 回执（搬家目全程 git mv／untracked 字节 mv 分制＝誊写禁令辖域内自察）。
