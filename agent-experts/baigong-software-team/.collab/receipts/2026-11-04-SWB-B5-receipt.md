# SWB-B5 · 收尾批（gitignore/README 重写＋D7 入库＋旧壳清灭）· 工程师回执 v1

- 回执席＝engineer-b5；票＝`.scratch/tickets/2026-11-03-SWB-B5-closure-gitignore-readme-ticket.md`（`8f5efa9`）＋rev2（`cccc0b7`·冲突以 rev2 为准）。
- 开工实测 HEAD＝`9f6675e`（≥B4 回执随正笔）；开工 `git status --short` 基线读数＝**空**（干净）；开工 `git ls-files` 计数基线＝**866**。
- 开工门禁族集签名＝`GATE PASS`（发现 8745·BLOCK OA-D6 族大头＝案卷换址既有实例·reconcile 票 96/对账 34/SKIP 62 全 WATCH exit 1＝B4 后常态）＝与 OA-D6 族大头＝案卷换址既有实例先例同态在册。

## 一、逐笔 commit 链

| 笔 | hash | 目 | name-only 读数 |
|---|---|---|---|
| B5-A | `66a0889` | .gitignore 两制全量重写（含 rev2 仓根七行＋三桶重立＋负向防御行） | 1 M |
| B5-B | `4e6fb6d` | 仓根 README 四节重写（白名单＋名录＋案卷索引＋era 注记＋deliverables/README 待并入行并入） | 1 M |
| B5-C | `0df8bef` | D7 入库 docs＋删源＋来源注两处＋三同源 0.1.19＋README 版本账行＋**门禁随动行**（check-entity 名册豁免·主理人裁 A） | 8 件＝docs 新件 A＋refs 删源（untracked 域不入 git 面·文件系统 rm 对账见 §三）＋两 copy M＋三 json/lock M＋百工 README M＋check-entity.py M |
| B5-D | 无 git 笔 | deliverables/ 空壳清灭＝盘上 untracked 空目录 rm（`git ls-files deliverables docs` 开工即＝**0**·B2/B3g 已清零 git 面）→ 空目录随空自灭＝无 commit 可落＝如实登记 | 0 |

- 禁 `--no-verify`＝全程未用；禁 amend＝未用；每笔 pre-commit 门禁族集全跑。

## 二、.gitignore 新旧条款映射表（全量·防防护静默丢失）

| 旧行（重写前号位） | 旧条款 | 处置 | 新行（重写后） |
|---|---|---|---|
| L1–3 | 治理原则注释（显式声明制/性质分区键） | 随迁 | 新头注（随迁＋B5 真源指针） |
| L6 | `.collab/process/` | 退役→仓根锚定行顶替 | `/.collab/process/` |
| L9 | `.collab/inbox/` | 退役→顶替 | `/.collab/inbox/` |
| L13 | `!.collab/research/` | 换代（窄→双层防御） | `!/.collab/research/`＋`!/**/.collab/research/`（新增任意层级负向防御＝票 B5-A3） |
| L17 | `.collab/evidence/` | 退役→顶替（rev2 指定格） | `/.collab/evidence/` |
| L24 | `.collab/backup/` | 退役→顶替 | `/.collab/backup/` |
| L27 | `.collab/dispatch/` | 退役→顶替 | `/.collab/dispatch/` |
| L30 | `.collab/tmp-*.txt` | 退役→顶替 | `/.collab/tmp-*.txt` |
| L33 | `.collab/refs/` | 退役→顶替 | `/.collab/refs/` |
| L37–39 | 外部快照三桶（video-teams/official-cos/summoned） | 随迁仓根留置位（rev2 A2-补2·ESC1 未执行＝仓根行维持两态口径之「后于 B5」态实测） | 同名三行 |
| L42–44 | 三桶配套负向三行 | 随迁 | 同名三行 |
| L47–49 | Thumbs.db/Desktop.ini/.DS_Store | 随迁 | 同 |
| L52 | `.workbuddy/` | 随迁 | 同 |
| L55–56 | `__pycache__/`＋`*.pyc` | 随迁 | 同 |
| L59–65 | B1 过渡增补 `/**/.collab/{refs,evidence,inbox,process,dispatch,backup}/`＋`tmp-*.txt` | 转正保留（任意层级面） | 同七行 |
| （无） | 仓根层级七行（rev2 A2-补1） | **新增** | `/.collab/{evidence,refs,inbox,process,dispatch,backup}/`＋`/.collab/tmp-*.txt` |
| （无） | era 留置面显式注记行 | **新增** | `!/.collab/research/` 行注记（留置面＝史实锚入库面不排除·ESC1 域） |

**双向验证读数**：旧规则逐条 check-ignore 复验＝保留/顶替项仍 ignore（下表矩阵 1–10、17–19 全 IGNORE）；退役无顶替项＝**无**（旧排除面全数由新行承接＝零静默丢失）；tracked 867→868 全量对拍新 gitignore（`check-ignore --stdin --no-index`）命中＝**2**＝`.collab/evidence/*team-rename-01*` 两支＝B3c2 tracked 单列先例（tracked 优先于 ignore＝B3 rev2 补丁四在册口径）＝吞失 0。

## 三、D7 哈希链（字节级复制＋删源·誊写禁令 f5a0d96 辖域内）

- 迁移前基线（开工首步落盘）：旧暂住位 `agent-experts/baigong-software-team/.collab/refs/external/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md` 整件 sha256＝`3fda41e6fd47db427abf164ff387a1710f9776b0f073a72bd72cafbea984cda4`（262 行 wc／split 263 末空）。
- 新位 `agent-experts/baigong-software-team/docs/SWB-交接件v2.9-产品设计与架构设计-2026-11-03.md` 整件 sha256＝`3fda41e6…cda4` **逐字等** ✓。
- 三哈希（新位复算·段切口径物理 L29–260／L29–84／L85–260·LF join 无尾换行）：全文 `3f335333e0fe4bc2a3532688588a6fde5a313981ef8bf04fc05ff8a1934ccb9b`／产品 `7214ad14259b175fd6912806e2b3a7bb3655ff35053098f9ed5df66c2d9691f3`／架构 `efb4f7658c1e5555fcf310cdf4ae91ecbf6ce5cfe19c420c293e0e62cc1078c4` ＝票面值**逐字等** ✓（V13 恒等式零扰动）。
- 删源＝旧暂住位 `rm`（该域＝untracked 排除面＝git 无删除笔·文件系统对账＝refs/external 目录现存 22 件不含该件）。
- 来源注两处随动＝`skills/sop/references/{product,architecture}-v2.9-copy.md` 头注「源路径」改 `docs/SWB-交接件v2.9-…-2026-11-03.md`＋登记件入库注记句（哈希段零动）。
- 版本三同源 0.1.18→**0.1.19** 读数＝plugin.json `0.1.19`／bundle.lock `0.1.19`／.codebuddy-plugin/plugin.json `0.1.19` ✓；README append-only＝百工 README 版本账 v0.1.18 行后追加 v0.1.19 行（1 行 append·前 40 后 41 行账段读数）。

### 门禁随动行（主理人裁 A·B3a 剪枝先例同规格·本回执在册＝防双治）

- 落笔＝`check-entity.py` 增设「史实锚登记件名册」豁免面：`REGISTRATION_NAME_ROSTER` 元组（基名精确匹配·`SWB-交接件v2.9-*-2026-11-03.md` 一入册·**append-only** 注记在位）＋`in_registration_roster` 文件级跳过；名册行日期字面拆段拼接防自咬（drive-path 注释先例同法）。语义依据＝check-entity 自注「扫描域＝规范件」＋B3a 剪枝先例＋check-pointers 裁-23 记录件排除先例＝既有语义物理化非新增豁免类别。
- 对照读数＝豁免前该件探针 `docs/SWB-交接件…:3 BLOCK OA-T1 pattern=date count=1`（复现在案）→ 豁免后全仓 `pattern=date count=0`·check-entity exit **0**·findings **0**。
- 负例探针＝临时规范件 `agent-skills/object-audit/probe-neg-oat1-tmp.md`（裸日期 2026-11-04）→ 仍 BLOCK 命中 exit≠0 ✓＝豁免不外溢实证；名册单元探针＝命中新 docs 件／不命中 `PRODUCT.md`／不命中旧版 `-2026-11-02.md` 三断言全过。
- **防双治收账行**（照 c282aef 同例）：check-entity 登记件名册豁免＝**B5 已落**——后续票面若含 check-entity 同族议题按已落登记处理，勿双治；本行候主理人 B 批收口登记面随纳。

## 四、判据 1–7 读数

1. **顶层终态白名单**：`ls -d */`＝{agent-experts, agent-skills, softwares, tools}；`deliverables|docs` 出现＝无（exit 0 正·负例构造＝出现即 exit 1 在判据脚本内）。点目录=find 面见判据 1 补。
1 补. **rev2 补丁二仓根 `.collab` find 两断言**（口径＝主理人裁「B 批施工新残留＝0」）：`find .collab -type f`＝4159（门禁续写漂移在册）；era research 正则＝**26** ✓；逐桶＝qa 3（QA-B3×2＋QA-B4·主理人登记面）／receipts 0／tickets 0／decisions 2（11-04 皮总裁定并发两支·主理人登记面）／design 0／refs 0／process 0／board 0／inbox 6（`主理人/` 活写面出口③）／dispatch 3（era 派工书·ESC1 并入消费）；**B5 施工新增仓根残留＝0**（`find -newer` 排除 evidence/gates 续写面＝0）✓。14 命中逐条归因表（主理人续批指令要求逐条枚举·收口笔复点＝14 全等）＝

| # | 文件 | 定性 |
|---|---|---|
| 1–3 | `.collab/qa/2026-11-03-QA-B3-独立验证-v1/v2.md`＋`.collab/qa/2026-11-04-QA-B4-独立验证-v1.md` | 主理人登记面（B3/B4 QA 核验件·B4 收口登记笔落仓根＝归置候收口后治理目·非 B5 残留） |
| 4–5 | `.collab/decisions/2026-11-04-皮总裁定-主理人永不并发派席.md`＋`并发口径修正-禁同席多实例.md` | 主理人登记面（B4 收口期皮总裁定链·tracked 在册·归置候裁） |
| 6–8 | `.collab/dispatch/2026-10-28-R6视频团/R7短剧编剧团/R8导演-派工书.md` | era 留置面（B3 回执 §七「era 族留置 dispatch 3」原班·ESC1 并入消费） |
| 9–14 | `.collab/inbox/主理人/2026-10-23/24/26/28/29/30-呈拍-gates.md` | 仓根活写面留置（run-gates 出口③硬编码仓根＝B1 随注承接 B4/B5 过渡态·B3 回执在册） |

＝主理人登记面 5＋era 面 3＋活写面 6＝**非 B 批施工新残留**（B5 施工新增仓根残留＝0 断言独立复跑成立）·仓根登记散件归置＝B 批收口后治理目（主理人裁在册不入本票闭集）。era 留置数两栏（B3 rev2 回执口径）＝开工 26（research tracked 正则）→收口 26 ✓；era 族 research 外＝dispatch 3＋evidence 1（`2026-10-28-T-video-research-gate-01-施工回执.md` 复点在位）＝4 支全等。仓根 `.collab` 根面另存登记散件 2（B3/B4 收口登记 v1·tracked）＋`tmp-w7-msg.txt`（ignore 面）＝均随判在册非违例。
2. **check-ignore 矩阵（≥12·实跑 24 形态）**：IGNORE 组（12）＝仓根 evidence/gates、refs、inbox、process、dispatch、backup、tmp-w7-msg、三桶 video-teams/official-cos/summoned、项目级 `.collab/refs/y`、项目级 `fuxi …/evidence/gates/x.json`、multi-collab `.collab/process/x`；TRACKOK 组（12）＝REFERENCE-SOURCES.md（负向行）、`.discussion/`、era 审计件、仓根 decisions/qa、项目 decisions、`.scratch/tickets/z.md`、仓根 docs/PRODUCT.md、项目 docs/PRODUCT.md、multi-collab SKILL.md、tools/*.py。rev2 四探针全中（evidence 仓根＝ignore／refs＝ignore／video-teams＝ignore／REFERENCE-SOURCES＝≠ignore）。
3. **D7 字节一致**＝§三全链 ✓。
4. **旧路径引用清零**：全仓 `.md` 出现＝60 occurrence——逐面分解＝**交付面活引用（skills/config/agents/bundle.lock/plugin.json 域）＝0** ✓；其余 60＝票面/回执/QA 史述登记面（append-only 史述豁免·票判据 4 括注口径）＋`.workbuddy/memory`（ignore 面）。逐文件分布＝`.scratch/tickets` B 批票 2＋百工 `.scratch/tickets` 票包 13 文件＋qa/receipts 史述 11＋design inventory 1＋两 copy（已改）＝改前后对照在册。
5. **README 索引完整性**：项目名录数据行＝**7** ✓（python 计数 exit 0）；四节跨项目案卷索引非空行＝含 decisions 逐名 16＋仓根 2／research 桶计数＋era 26 明细／qa-receipts-board-design-tickets 计数＝行数≥B3c2 表行户口径（B3 回执 §三＋§七两表＝15＋8 行→本索引对应指针段在位）；era 注记行「待移交 experts 仓（ESC1·票面实体）」＝True ✓。
6. **门禁零回归＋六演练全绿**：收口 run-gates＝`GATE PASS`（发现 8745 恒定·族集与开工签名对拍＝NEW 族 0·check-entity 族 post exit 0）；六演练＝`SIX_DRILLS_GREEN`（drill-01…06 逐卷 GREEN）。
7. **版本三同源 0.1.19**＋README append-only 前后读数＝§三 ✓。

## 五、黄项承接与读数差登记

- **黄-2（B4 回执自咬指针 3 条）收账**：`receipt.md:54` path_globs 字面／`receipt.md:3` 票面指针＝回执史述 append-only **不改写**（史实锚纪律）；`README.md:58` 旧行＝旧仓根 README 行随 B5-B 重写**自然消解**（新 README 无该行·check-pointers 现面该格消失在册）。三条＝登记面清理口径收账完毕。
- **README 表行读数差**：B2 回执待并入行记「skills 表 6 行」vs 旧件取证实测数据行＝**5**（表头 1 另计；external-advisor-collab 未列旧表＝其出生在新树）；新 README 并入段＝旧 5 行照录＋现名录 6 技能项目全在名录表＝读数差登记于此不自行抹平。
- `tmp-w7-msg.txt`＝新行 `/.collab/tmp-*.txt` 仍覆盖＝ignore 态留置随判在册（B3 回执承接口径闭合）。
- ESC1 未执行＝rev2 A2-补2 两态口径取「后于 B5」态＝仓根三桶行维持·era 索引标「待移交」✓；ESC1 实体票引用已随动入 README 四节（`.scratch/tickets/2026-11-03-SWB-ESC1-era-cross-repo-handover-micro-ticket.md`）。

## 六、红项史述（B5-C 曾拦·候裁后放行）

D7 入库首跑 pre-commit `GATE BLOCK OA-T1`（登记件 L3 裸登记日期首次入 check-entity 扫面＝B3 时住 refs 排除面物理不可扫）＝票面预案缺位如实报红→候裁呈报（A/B/C/D 四选项）→主理人**裁 A**（名册豁免·三条件随动）→§三门禁随动行落地→`0df8bef` 绿笔入库。fail-closed 闸未破·无一次 bypass。

## 七、收口复跑段（主理人续批指令·回执修订笔）

- 开工续批实测＝HEAD `0df8bef`（主理人侧给值全等复核✓）·工作区 clean·staged 空✓。
- **B5-D 灭壳断言现势读数**：`ls -a` 顶层集＝{agent-experts, agent-skills, softwares, tools}＋点目录（.collab/.git/.gitignore/.scratch/.workbuddy）；`ls -d deliverables docs`＝均不存在＝exit 1 断言反向成立✓（＝灭壳自然自灭·零 git 操作＝§一 B5-D 行登记口径再证）。
- **收口门禁族集复跑**＝`GATE PASS`（发现 8757·与回执笔时点读数同态＝差 12＝回执/证据件续写面·族集对开工基线 8745 **NEW 族 0**＝零回归✓；reconcile 票 96/对账 34/SKIP 62 全 WATCH exit 1 恒定）。
- **六演练收口跑**＝DRILL01–06 逐卷 `DRILLnn_GREEN`＋`SIX_DRILLS_GREEN` ✓。
- **判据 3 新位复算再证**＝docs 新位整件 sha256 `3fda41e6…cda4`＋三哈希 `3f335333…ccb9b`/`7214ad14…91f3`/`efb4f765…78c4` 收口时点复算逐字等✓（§三链再证）。
- 本节＝回执修订随批笔（仅含本回执件·append 于 §六 后＋§一 归因表补全＝前笔 `b357d1e` 后唯一合法修订面＝主理人续批指令点名目）。

——engineer-b5 · SWB-B5 回执（gitignore/README＝新建创作类·D7＝字节级复制＋删源＝誊写禁令辖域内自察）。
