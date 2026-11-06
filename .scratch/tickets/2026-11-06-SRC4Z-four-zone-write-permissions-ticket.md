# TK-SRC4Z · 四区写权限总表入纪律面＋sources 守卫改文成稿＋deliverables/ 语义校正批票（rev1）

- **rev1 声明行（2026-11-06·作者席原位修订）**：消化双席独立审票＝QA 审件 `.collab/qa/2026-11-06-SRC4Z-QA审票-v1.md`（commit `d5ae8fa`·红2黄3绿10）＋PM 审件 `.collab/qa/2026-11-06-SRC4Z-PM审票-v1.md`（commit `51dcd5c`·红0黄4）。rev1 改动＝R1 断言如实化（§二/§五-B＋敞口登记）；R2 落点 C1 改派随 §B 人类落笔（主理人裁定）；Y1 行数判据改对照口径；Y2 判据5 dev-discipline 1→4；Y3 草案 §B.5 命令1 改可执行式；黄-3 §九.2 域界注；黄-4 §C 限定语。候裁径裁登记（主理人已径裁·均不扩面）＝**H1 note 不加注／H2 案 a／H3 零触／H4 落点选型确认**。获批裁定面（sources 语义／四区表／落笔分工主体）零动。
- 起草席＝架构席；起草开工实测 HEAD＝`27fa36b`；rev1 开工实测 HEAD＝`d5ae8fa`（rev1 笔开工 `git rev-parse --short HEAD`）。
- 票型＝规则票（纪律面成文＋守件配置改文成稿随票呈交＋文档语义校正）；起草＝架构席（dev-discipline §六.1）；执行分工见 §五（A＝工程师席；B＋C1＝皮总人类身份落笔）。
- 本票面件＝起草产物（随批）；**本票起草席零改守件本体、零执行**；随票草案件＝`.collab/design` 草案一件（路径见 §〇）。

## 〇 声明闭集（本票唯一可写面）

起草笔（本批·`collab:` 前缀）：
1. `.scratch/tickets/2026-11-06-SRC4Z-four-zone-write-permissions-ticket.md`（本票面）
2. `agent-experts/baigong-software-team/.collab/design/2026-11-06-SRC4Z-守件配置改文草案-v1.md`（随票草案：§A 逐字插入块＋§B 逐席改前/改后＋§B.6 人类落笔清单＋§C 逐处处置表＋§0 取证读数）

执行笔（工程师席·落点A，另 commit·前缀按执行票惯例）：
3. `agent-experts/baigong-software-team/skills/software-orchestration/references/dev-discipline.md`（落点A：文末追加 §九 块）

（rev1·R2 改派：原执行笔第 4 项 `docs/PRODUCT.md` 移出工程师执行面——机械路不可达（QA 探针：lease-issuer 签发 REJECT＋`docs/**`∈engineer deny_globs 命中 DENY），改随落点 B 转皮总人类落笔＝草案件 §B.6 清单第 3 项。人类笔不入声明闭集机械对账面。）

探针/回执面（重定向·批毕清理）：
4. 仓根 `.scratch/SRC4Z-probe/`（执行/验收探针区；起草席探针残留现居 `.scratch/SRC4Z-draft/`，随收口删除）
5. 回执件＝`.collab/` 过程域（执行席落位按席位写域）

禁动面（本票全域零触碰·含执行段）：
- `agent-experts/baigong-software-team/config/seat-permissions-hooks-map.json`、`config/seat-permissions.json`（＝落点B 改文对象，**机械席位零触**——纪律约束面；机械可达性实况见 §二 R1 敞口登记，见 §五-B）
- `agent-experts/baigong-software-team/hooks/hooks.json`
- 版本三同源＝`.codebuddy-plugin/plugin.json`／`bundle.lock`／包根 `plugin.json`（bump 已落 `bd178a9`＝0.1.30，本批零再 bump）
- GWP-DEPLOY 票面（`.scratch/tickets/2026-11-06-GWP-DEPLOY-0.1.30-四段链部署票-v1.md`·另案在审）
- `skills/sop/references/architecture-v2.9-copy.md`／`product-v2.9-copy.md`／`docs/SWB-交接件v2.9-*.md`（哈希登记面·落点C 判定零触）
- `docs/PRODUCT.md`（rev1 起＝人类落笔面，机械席零触）
- `docs/STRUCTURE.md`、`docs/ARCHITECTURE.md`、`.collab/decisions/` 全部、`tools/`、`tests/` 全部内容、`.archive/`

## 一 决策依据（自包含·已拍）

仓根 `.collab/decisions/2026-11-06-皮总拍板-sources四区写权限与deliverables语义校正.md`（commit `27fa36b`）裁定要点：

1. **四区写权限总表**（{root}/{project_id}/ 结构）：`sources/`＝仅人类可写（全席位＋主理人只读；原始用户输入＝唯一事实源；解析件/digest/转正件禁入）；`docs/`＝按文档归属席位（结构/架构/ADR＝架构席、产品说明书＝产品席、其余逐件主理人指定）；`.collab/`、`.archive/`＝席位租约面/主理人落位；其余全部＝代码交付面工程师按票租约。
2. `sources/**` 入各席 deny_globs＝**改文成稿随票呈交**，实际落笔由皮总以人类身份执行（裁定已注明授权出处）。
3. deliverables/ 语义校正：`deliverables/{project_id}`＝devkits 工作空间下各项目真实工作空间；`deliverables/` 只是 {root} 末尾段，非专家团包内自有子包；装机包内文档涉 `deliverables/` 字样按此语义读（实测装机 0.1.29 缓存无 `deliverables/` 子目录＝盘上旁证）。
4. 旧 `Sources\...` 历史引文不回改；今后新文书一律 `sources/` 新路径。

## 二 起草取证（现文实测·真源对账面同步登记·rev1 随双席审件补正）

- 写侧机件实读：`skills/sop/scripts/write-guard.py`——**现无「人类判定放行」机制**；deny_globs 检查先于租约面；人类＝hooks 面外直通（hooks-map `_anchors.席位覆盖说明` 既载「人类直通＝设计语义」；seat-permissions.json human 行 carrier＝「平台外签名工具」）。生效边界全文见草案件 §B.4。
- **守件保护实态（rev1·R1 消化·QA 端到端探针实证）**：`config/**` ∈ host/product/architect/qa 四席 deny_globs，**不在** engineer deny_globs 且 **在** engineer write_globs（交付面换代行）；QA 实证＝合法签发 engineer `config/**` 租约（exit 0）→ 写守件 **ALLOW**。⇒ 守件保护实态＝**四席 deny＋engineer 租约可达＋tests/s4 t13 事后断言兜底＋票面纪律**（v1 所称「config 在五席 deny 内机械路本就不可达」＝不实断言，rev1 更正）。**敞口如实登记在案**：是否给 engineer 补 `config/**` deny／租约面禁签守件行＝超出已裁定范围（裁定只裁 sources/\*\*）**不入本批**，由主理人另呈皮总候裁。本批 §B 改文不触 engineer 对 config 的可达性。
- 派生断言实读：`tests/s4/test_enforcement.py` L268-272——hooks-map 各席 deny_globs 与 seat-permissions.json 源件逐行全等（「派生面禁改写」）⇒ §B 两文件必须同批同值。
- 现盘写 sources/ 探针：五席均 deny（reason＝路径∉当席租约）；植入 `path_globs:["sources/**"]` 租约后现盘 map＝ALLOW（敞口实证）、草拟 map＝DENY（封窗实证）。读数＝草案件 §0.3（双席独立复现于 QA 审件 §二 T-A~T-E）。
- 落点可达性（rev1·R2 消化·QA 探针 P-1~P-5）：`docs/PRODUCT.md` 经 engineer 签发 REJECT exit 2＋植入租约仍 DENY（`docs/**`∈engineer deny）＝**无合格机械执行路**；落点A `dev-discipline.md` 经 engineer 域行 `skills/**` 签发通过（P-2 exit 0＋写侧 ALLOW 实证）＝工程师路可达（票 §五 措辞按域行口径）。
- 真源对账基线：`python tools/check-source-of-truth.py`＝`文件 129｜BLOCK 0（新命中 0）｜基线豁免 54｜指针 WATCH 413｜exit 0`（双席复跑逐字段全等）。
- 版本现值：三同源均 `0.1.30`（`bd178a9` 已落 bump）。
- 落点选型（H4 主理人已径裁＝确认）：四区总表入 `dev-discipline.md`（跨项目写权纪律真源卷，文末追加 §九）；**不入** 本包 `docs/STRUCTURE.md`——该件承载本包 bundle 面 delivery_paths（项目根探针锚结构），四区总表属宿主 {root}/{project_id}/ 结构，两结构不混写。

## 三 实装规格（三落点·条款全文＝草案件逐字块）

### 落点A 纪律面成文（工程师席执行）

`dev-discipline.md` 现 §八 末行（「4. 派工书／票面禁写仓外临时路径模板…」）之后**文末追加**草案件 §A 逐字块（新 §九 五款：四区分权总表／sources 唯一事实源与双拦语义＋两域界注／deliverables 读法／旧引文不回改／出处指针）。append-only：现文 §一~§八 一字零动。

### 落点B deny_globs 改文＋C1 校正行（皮总人类身份落笔·全机械席零触）

对象＝`config/seat-permissions.json`（源件）＋`config/seat-permissions-hooks-map.json`（hooks 消费面），两文件同批：五机械席（host/product/architect/engineer/qa）各 `deny_globs` 数组末尾追加 `"sources/**"`；human 行 `deny_globs: []` 零动；其余键零动（H1 径裁＝note 不加注）。逐席改前/改后对照表＋落笔后核验收法（JSON 断言＋pytest s4＋负样本翻拒复跑命令·rev1 命令1 已改可执行式）＝草案件 §B.1-B.5，皮总可逐键照抄；**rev1·R2 并入**＝草案件 §B.6 人类落笔清单三项（两 config＋PRODUCT.md L75 校正行）。生效边界如实陈述（席位面三层拦＋人类面＝hooks 外直通无白名单机制＋守件自身保护实态见 R1）＝草案件 §B.4，不虚构机制。

### 落点C deliverables/ 语义校正（C1＝随 B 人类笔；C2-C6＝零触判定）

逐处处置表＝草案件 §C（实测 grep 定位六族·限定语＝交付面 md＋测试件域）：
- C1 `docs/PRODUCT.md` L75 后追加一行语义校正注（案 a·H2 径裁定案；**rev1 改派＝随 §B.6 皮总人类落笔**，不入工程师执行面）；
- C2 `dev-discipline.md` L8 零改（读法由 §九.3 承载）；
- C3 基线副本 `architecture-v2.9-copy.md`（L25/26/27/174）零触（哈希登记面；H3 径裁＝头注区亦零触）；
- C4 登记件 `docs/SWB-交接件v2.9-*.md`（L108/109/110/257）零触（登记面不回改）；
- C5 `README.md` L30 版本账历史行零触；C6 `tests/` 三件沿革注释零触（历史引文）。

## 四 验收判据（全机械可判·回执附逐项读数）

1. **A 落点真源对账零新增漂移**：执行笔后 `python tools/check-source-of-truth.py` 复跑＝exit 0 且 `BLOCK 0（新命中 0）`（对比 §二基线行）；基线豁免 54／指针 WATCH 413 若变动，逐项列差集读数如实登记（§九块为加性纪律条款，预期 WATCH 不新增；新增者逐条说明）。
2. **A 落点在位**（rev1·Y1 消化）：`grep -c '四区写权限总表' dev-discipline.md`＝1；`grep -c '仅人类（用户）可写' dev-discipline.md`＝1；行数不钉固定增量（逐字块行数随 rev 文本变动）＝判据改**前后 `wc -l` 读数对照登记**口径（现盘基线 85），回执含前值/后值两读数且差值＝草案件 §A 逐字块行数（rev1 实测＝20 行含前置空行；差值不符＝回执红）。
3. **B 草案可照抄**：草案件 §B.2/B.3 对照表五席×两文件＝十行改前/改后逐键齐备＋§B.6 人类落笔清单三项（皮总核验项：无省略号歧义——每席改前/改后末两元素字面完整）；本判据对**草案件**判定，不对 config 判定（config 现面零动＝见判据 7）。
4. **B 落笔后翻拒复跑**（皮总落笔后由 QA 探针复跑，非本票工程师执行面）：植入 `path_globs:["sources/**"]` engineer 租约＋写 `sources/x` → 期望 deny·reason 含 `glob='sources/**'`；五席 payload 写 sources/ 全 deny；草案件 §B.5 命令1 期望读数由 miss×5 翻 OK。探针落 `.scratch/SRC4Z-probe/` 批毕删。
5. **C 落位 grep 对表**（rev1·Y2 消化）：`grep -c 'deliverables/'` 前后同值＝`architecture-v2.9-copy.md`(4)／`docs/SWB-交接件v2.9-*.md`(4)／`README.md`(1)；`dev-discipline.md` **1→4**（§九.3 三行自带该字样＝落点A 加性命中如实登记）；PRODUCT.md 1→2（校正行在位·人类笔）＋`grep -c '语义校正（2026-11-06 裁定）' docs/PRODUCT.md`＝1。
6. **版本零再 bump**：三同源复跑仍均 `0.1.30`（前后各附 grep 读数；前后同值亦须如实登记）。
7. **禁动面核验**：执行笔 `git show --name-only` 与 §〇 声明闭集执行笔全等（rev1＝仅 dev-discipline.md 一件）；`git diff <开工HEAD>..收口HEAD -- **/config/seat-permissions*.json **/hooks/hooks.json **/plugin.json **/bundle.lock **/docs/PRODUCT.md tools/ tests/` 空读数（config＋PRODUCT.md 改动笔＝皮总人类笔，单独 commit·不入机械席 name-only 对账链）。
8. **探针清理**：`.scratch/SRC4Z-draft/`（起草席残留）＋`.scratch/SRC4Z-probe/` 批毕删除＋读数回执（dev-discipline §八.3 收口态＝零残留）。

## 五 落笔分工

- **落点A**＝工程师席按票执行（交付面写权；开发票 path_globs 经 engineer 域行 `skills/**` 承载——QA 探针 P-2 实证该路签发 exit 0＋写侧 ALLOW；显式全路径行 `skills/…/dev-discipline.md` 签发 REJECT＝P-3 实证，措辞按域行口径）。
- **落点B＋C1**＝改文草案呈皮总，以人类身份照草案件 §B.6 清单三项落笔（两 config deny_globs＋PRODUCT.md 校正行）；工程师席与全部机械席位**零触 config 与 PRODUCT.md**——此为纪律＋禁动面约束；机械可达性如实陈述（rev1·R1）＝config 四席 deny＋engineer 经租约**可达**（守件敞口已登记候裁），PRODUCT.md 对 engineer 机械路不可达（R2 实证）。
- 落笔顺序建议：皮总 B＋C1 笔可先可后（与落点A 零文件交集）；但 0.1.30 部署链装配前须全部入齐（登记件§三.2）。

## 六 版本归属

SRC4Z 随 0.1.30 部署链同批（登记件§三.2：涉守件配置＝与守卫补丁同批随 0.1.30 部署前入）；bump 已落 `bd178a9`（三同源 0.1.29→0.1.30），**本批零再 bump**；REMOTE-PUB 整改批 0.1.31 不动。

## 七 候裁处置（rev1·四条已由主理人径裁＋一敞口新增候裁）

- **H1**（note 加注）＝径裁**不加注**（config 改面零扩，沿革走登记/票面）。
- **H2**（C1 案 a/b）＝径裁**案 a**（加读法注；案 b 改写超裁定字面否掉）。
- **H3**（v2.9-copy 头注区加注）＝径裁**零触**（最小干预与登记纪律同向）。
- **H4**（落点选型）＝径裁**确认** dev-discipline §九单点成文（另入 STRUCTURE 类结构件＝新增改面须另呈）。
- **H5（rev1 新增·R1 敞口）**：engineer 对守件 config 租约可达（write_globs 含 `config/**`）＝既有实况非本批引入；是否补 engineer `config/**` deny 或租约面禁签守件行＝**超出已裁定范围（裁定只裁 sources/\*\*）不入本批**，由主理人另呈皮总候裁（0.1.30 随批 or 独立批次由皮总定）。

## 八 提交纪律

起草笔/rev1 笔＝本票面＋草案件两件，pathspec 逐件 `git add`，message 前缀 `collab:` 注明 TK-SRC4Z；禁 `--no-verify`／amend／`git add -A`。执行笔另 commit（工程师席·落点A），回执对账＝§四.7 name-only 全等口径。
