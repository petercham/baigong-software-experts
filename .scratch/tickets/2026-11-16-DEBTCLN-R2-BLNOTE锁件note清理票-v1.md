# DEBTCLN-R2 · BLNOTE 锁件 note 清理票（v1·规格票·起草笔零施工）

- 票号：**DEBTCLN-R2**（清债批次第二票·族名锁定，勿改）
- 票名：**BLNOTE 锁件 note 清理票**
- 票型：清债·内容清理票（锁文件 note 字段去过程黑话·其余 byte 零扰动）
- 起草席：架构席 arch-debt2（fresh 实例·主理人派工）
- 票面落点：.scratch／tickets／2026-11-16-DEBTCLN-R2-BLNOTE锁件note清理票-v1.md
- 来源与裁定依据：决策者已裁「起票」——挂账行登记（2026-11-09 补裁点⑨）：bundle.lock 组件一（external-advisor-collab）与组件二（deep-research）的 note 字段含同型过程黑话＝案批名／指令时刻／拍板编号／仓 sha 短串引用。系 SEMGV-T6（治理面黑话清理）射程外遗留，另票候排至今。
- 候裁点：**1 枚**（见 §四；随动裁量两项自决闭合并附论证）。

> **票面自注（防自咬体例）**：本票正文对一切路径仅叙述性提及＝裸文写＋全角斜杠（／U+FF0F），不落反引号路径指针；引用既有原文以 ⟦⟧ 标记。§二 与 §三 命令块内＝落笔实文本（双引号包径·不含反引号 token·天然安全）。本票面成文后自靶 python share/check-pointers.py --root . --target 本票面实路径 须 exit 0（读数见 §七）。

---

## 〇、开工读数（起草轮现跑·禁抄旧数）

| 项 | 命令 | 实测读数 |
|---|---|---|
| 时点 | date '+%F %T %z' | 2026-11-16 23:15:15 +0800 |
| HEAD | git rev-parse --short HEAD | **d4cb54b**（与派工预期值全等） |
| tracked 脏面 | git status --porcelain | 恰一枚 M＝agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl（他案脏面·禁碰禁入票） |
| untracked 全集 | 同上 | ?? 二十三行（仓根 .collab／ 平放 2026-11-12 系列 md 十二枚＋.collab／research／ md 六枚＋仓根杂散五枚：.py／.scratch_uds_assert.txt／.scratch_uds_pinsself.txt／.scratch_wbdocs.html／assert-modified-run2.txt）——全部他案/知会面，不入声明闭集（与派工预期形态全等） |
| 靶件定位 | Glob 全仓 bundle.lock＋邻仓 find | **本仓恰一枚**＝agent-experts／baigong-software-team／bundle.lock＝本票靶件。邻仓 D:／multi-agent-collab-experts 另有一枚（workbuddy／baigong-video-team／bundle.lock）＝他仓他包，非本债项射程，本票零触。**结论＝本仓内债，非跨仓债，正常开票。** |
| 靶件基线哈希 | sha256sum＋git hash-object | sha256＝cf1fb51899b4c5f30cc64d8d7e32d85fe1af7ae76ad0679096c1b0cf8c251580；blob＝973048685e0d655c3427e4fa04fa19394b25c66c |
| 靶件 JSON 基线 | python json.load | 解析 OK·components＝4（bundle＋四组件行＋assembly_exclude＋conventions 结构在册） |
| note 消费方 grep | grep -rn note 于 share／全部闸脚本＋agent-skills／object-build／scripts／publish.py | **note 字段零消费方**：publish.py 装配器只读 bundle.name／components 五键（component·repo·ref·path·target）／material／assembly_exclude／conventions，不读 note；check-adr.py 只定位 bundle.lock 做 ADR 挂载锚，不读 note。→ 清理 note 文案＝对全部消费脚本零输入面变化（V4 论证根基） |
| 缺省指针钉值 | python share/check-pointers.py 缺省扫描 grep -c BLOCK／grep -c WATCH | **BLOCK 22810／WATCH 4582** |
| 锁件消费闸基线 | python share/check-adr.py --root . | **exit 0**（改前基线现跑在册） |

## 一、案件本体与黑话清点

靶件四枚组件行 note 逐枚清点。**在册债项面＝组件一＋组件二**（补裁点⑨登记射程）：

### 枚一 · external-advisor-collab note（文件第 19 行）

⟦软开 bundle 首个装配组件（皮总 2026-10-28 口径：分仓＝维护/分发维度，部署到 WorkBuddy＝把相关 skills 装配进专家团）。真源＝本仓 agent-skills/external-advisor-collab（同仓组件·repo="." 解析为仓根）；装配产物＝仓外 -build 预览面＝派生产物非第二真源（纪律③产物不入库）。组件版本与 SKILL.md version 同源＝1.1.3；沿革：tag v1.0（2026-10-25 决议批）→v1.0.1（改名批）→v1.1.0（20261029a 案技能升级批·十落点条款＋版本 bump SK-3·锁版本 bump＋bundle 重装配＝决策者 2026-10-30 04:11 指令授权）→v1.1.1（2026-10-30 EAC-CLN 指针闭集整改·决策者拍板㊺·程序条款语义零动）→v1.1.2（2026-11-04 治理层换钉批·B2 搬家后 ref/path 失步致装配 exit 3·决策者「纠正吧」·条款语义零动）→v1.1.3（2026-11-05 CLN-PURE 装配净化批·包面非法指针自包含化＋40-artifacts 交接判据改指装配包内 handoff-discipline §三·条款语义零动）。lead 讨论会兼任节「加载技能 external-advisor-collab」自此命中包内装配件（部署态自包含·D 项收口）⟧

黑话分类登记：
- 案批名／票号类：决议批／改名批／20261029a 案／EAC-CLN／治理层换钉批／CLN-PURE／SK-3／40-artifacts（过程本体文件指针）／D 项收口（拍板项编号）
- 指令时刻类：2026-10-30 04:11（精确到分）
- 拍板编号类：㊺（决策者拍板㊺）
- 人格与指令引语类：皮总×1／「纠正吧」／指令授权
- 仓 sha 短串类：无

### 枚二 · deep-research note（文件第 29 行）

⟦跨仓组件（票 T-deepresearch-01·皮总 R-1 fork 登记）：真源＝skills 仓 skills/deep-research（MIT 派生自 staruhub/ClaudeSkills deep-research V8.1.2·克隆 hash 66e02d23642f0c63ccb07b46a88104eade402d44·登记见该技能 README）；解耦口径＝R-6：席位与编排零变化，本行为组件新增＋平台刷新载体（宿主缓存按包版本刷新），调研起手式自动路由靠技能 description 触发词，不动席位；v1.0→v1.0.1 修因＝QA-deepresearch-01 minor-a/b/c 收口（SKILL.md 四件套句删近逐字摘要改纯指针＋补 .md 后缀、methodology 中英混排修·票 T-deepresearch-02）；v1.0.1→v1.0.2 修因＝EAC-CLN 指针闭集整改（README 变更记录行消费侧仓案面指针改自包含陈述·皮总拍板㊺·skills 仓 730962e）⟧

黑话分类登记：
- 案批名／票号类：T-deepresearch-01／T-deepresearch-02／QA-deepresearch-01／minor-a／EAC-CLN／R-1／R-6（编号引用）
- 指令时刻类：无
- 拍板编号类：㊺（皮总拍板㊺）
- 人格类：皮总×2
- 仓 sha 短串类：730962e（skills 仓 commit 短串）
- 外部产地指纹（**保留自决·见 §四之二**）：66e02d23642f0c63ccb07b46a88104eade402d44＝上游 fork 克隆全 hash＝溯源数据非我方过程引用，且该技能 README 在册登记（登记句随文保留）

枚三（claim-commitment-governance）与枚四（devkit-tools）note 另含同型黑话（SEMGOV-T3／EAC 先例／D 项收口同构／TOOLHOME 票 S2／ccf6383／e12afd3 等），**不在补裁点⑨登记射程**→§四 候裁①，本票不动。bundle 本体 note 与 conventions／assembly_exclude 零黑话、零动。

## 二、声明闭集（＝两枚 note 的「现文→清理后文」对照规格·封顶两行面·禁酌情）

清理口径＝保留决策理由句（为何锁此版本·版本沿革链），去过程黑话（票号／案名／指令时刻／拍板编号／sha 短串／人格引语）；日级日期随批名一并去（批名本体即黑话，日级日期系其附属叙述，非锁文件读者所需——自决论证见 §四之三）。**清理后文为逐字可照抄规格**（下列块内文本＝JSON 字符串值内部内容，落文件时 repo 句的双引号照枚一现文形态转义为反斜杠引号）：

**S1 · 枚一 note 替换（现文见 §一枚一 ⟦⟧ 全引，清理后文如下）**：

```text
软开 bundle 首个装配组件（口径：分仓＝维护/分发维度，部署到 WorkBuddy＝把相关 skills 装配进专家团）。真源＝本仓 agent-skills/external-advisor-collab（同仓组件·repo="." 解析为仓根）；装配产物＝仓外 -build 预览面＝派生产物非第二真源（纪律③产物不入库）。组件版本与 SKILL.md version 同源＝1.1.3；沿革：tag v1.0→v1.0.1（改名）→v1.1.0（技能升级＝十落点条款＋版本 bump＋锁版本 bump＋bundle 重装配）→v1.1.1（指针闭集整改·程序条款语义零动）→v1.1.2（治理层搬家后 ref/path 失步致装配 exit 3 的纠正·条款语义零动）→v1.1.3（装配净化＝包面非法指针自包含化＋交接判据改指装配包内 handoff-discipline §三·条款语义零动）。lead 讨论会兼任节「加载技能 external-advisor-collab」自此命中包内装配件（部署态自包含）
```

**S2 · 枚二 note 替换（现文见 §一枚二 ⟦⟧ 全引，清理后文如下）**：

```text
跨仓组件（fork 登记组件）：真源＝skills 仓 skills/deep-research（MIT 派生自 staruhub/ClaudeSkills deep-research V8.1.2·克隆 hash 66e02d23642f0c63ccb07b46a88104eade402d44·登记见该技能 README）；解耦口径＝席位与编排零变化，本行为组件新增＋平台刷新载体（宿主缓存按包版本刷新），调研起手式自动路由靠技能 description 触发词，不动席位；v1.0→v1.0.1 修因＝QA 复核收口（SKILL.md 四件套句删近逐字摘要改纯指针＋补 .md 后缀、methodology 中英混排修）；v1.0.1→v1.0.2 修因＝指针闭集整改（README 变更记录行消费侧仓案面指针改自包含陈述）
```

**施工面规格**：唯一改动面＝该文件两行 note 值（现文件第 19／29 行）。工程师施工手段自选（整件重写或程序化替换均可），但 V3 钉死＝前后 diff 仅这两行。建议程序化两段替换防转义手误：先把 S1／S2 清理后文各落 .scratch／debt2／note1_new.txt／note2_new.txt（裸文本无引号），再跑：

```bash
python -c "import json;p='agent-experts/baigong-software-team/bundle.lock';d=json.load(open(p,encoding='utf-8'));d['components'][0]['note']=open('.scratch/debt2/note1_new.txt',encoding='utf-8').read().rstrip('\n');d['components'][1]['note']=open('.scratch/debt2/note2_new.txt',encoding='utf-8').read().rstrip('\n');open(p,'w',encoding='utf-8').write(json.dumps(d,indent=2,ensure_ascii=False)+'\n')"
```

（此式产物格式＝现文件同构：两空格缩进＋非转义中文＋尾换行，V3 diff 自证。工程师用其它手段须同等过 V2／V3。）

### 禁动面（写死）

- 锁件其余全部字段 byte 级零扰动：lock_version／bundle 行（含其 note）／四组件行的 component·repo·roottag·ref·ref_kind·path·target·material 键／枚三枚四 note／assembly_exclude／conventions。
- 版本值零动：bundle 0.1.30／各 ref tag 值／ref_kind。
- 他案脏面零带入：agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl 之 M 态＋?? 二十三行全集＝禁碰禁入库。
- 邻仓 workbuddy／baigong-video-team／bundle.lock 零触（非本仓）。
- 链上史件零回改；账本面零手写。

## 三、验收判据（全机械·命令＋钉值·禁凭记忆填值）

- **V0 开工读数**：施工轮现跑 HEAD＝d4cb54b 链上本票之后最新值如实照登；git status 他案脏面形态与 §〇 一致（ledger 一枚 M＋?? 二十三行→本票落链后本票面转 tracked，?? 仍二十三行不含本票）。
- **V1 黑话 token 清零（判据 token 清单＝下列 21 枚·检索域＝components[0] note＋components[1] note 两段串联）**：

```bash
python -c "import json;d=json.load(open('agent-experts/baigong-software-team/bundle.lock',encoding='utf-8'));t=d['components'][0]['note']+d['components'][1]['note'];toks=['\u76ae\u603b','\u51b3\u8bae\u6279','\u6539\u540d\u6279','20261029a','SK-3','04:11','EAC-CLN','\u32ba','\u6362\u9489\u6279','\u7ea0\u6b63\u5427','CLN-PURE','40-artifacts','D \u9879\u6536\u53e3','T-deepresearch-01','R-1','QA-deepresearch','minor-a','T-deepresearch-02','R-6','730962e','\u6307\u4ee4\u6388\u6743'];print([(k,t.count(k)) for k in toks]);raise SystemExit(0 if all(t.count(k)==0 for k in toks) else 1)"
```

→ **exit 0** 且打印清单全部计数 0。（token 中文以 unicode 转义内嵌防 shell 引号面事故；清单语义＝§一 分类登记全集：皮总／决议批／改名批／20261029a／SK-3／04:11／EAC-CLN／㊺／换钉批／纠正吧／CLN-PURE／40-artifacts／D 项收口／T-deepresearch-01／R-1／QA-deepresearch／minor-a／T-deepresearch-02／R-6／730962e／指令授权）
- **V2 结构可解析不变**：python -c "import json;json.load(open('agent-experts/baigong-software-team/bundle.lock',encoding='utf-8'));print('PARSE-OK')" → exit 0 打印 PARSE-OK；components 数仍 4。
- **V3 byte 级零扰动**：git diff --unparsed 式对拍＝git diff --numstat 于靶件＝**2／2 恰两行**；git diff 全文＝改动行仅两行 note 值行（第 19／29 行位置段）；python 结构化对拍：

```bash
python -c "import json,subprocess;a=json.loads(subprocess.run(['git','show','HEAD:agent-experts/baigong-software-team/bundle.lock'],capture_output=True).stdout);b=json.load(open('agent-experts/baigong-software-team/bundle.lock',encoding='utf-8'));a['components'][0]['note']=a['components'][1]['note']=b['components'][0]['note']=b['components'][1]['note']='X';print('REST-EQUAL' if a==b else 'DRIFT')"
```

→ 打印 **REST-EQUAL**（除两枚 note 外全结构深相等；HEAD 基线以本票落链后链上笔为准·§七 注）。
- **V4 锁消费脚本现跑零变化**：python share/check-adr.py --root . → **exit 0**（与 §〇 基线对拍全等）＋V2 解析式即 publish.py 前置读锁面之等价复现（其组件五键断言：python -c "import json;d=json.load(open('agent-experts/baigong-software-team/bundle.lock',encoding='utf-8'));print(all(c.get(k) for c in d['components'] for k in ('component','repo','ref','path','target')))" → True，改前后同值）。publish.py --assemble 全流水不在本票现跑＝其 git_clean_or_die 需三仓全净工作区＋产物落仓外 -build 面，与他案脏面现状互斥且属装配动作非校码动作；note 零消费方（§〇 grep 坐实）＋五键断言＋JSON 解析＋check-adr 四面对拍＝行为零变化的充分机械面，如实登记此口径。
- **V5 自靶**：python share/check-pointers.py --root . --target 施工后回执实路径 → exit 0；本票面（链上现文）同式 exit 0 复证。
- **V6 边界**：施工笔 git diff --cached --name-only＝**恰靶件一枚**；禁动面 pathspec 域（邻仓文件／ledger／枚三枚四 note 行／conventions）零命中；他案脏面状态零变化。

## 四、候裁面（必有节·**候裁 1 枚**）

- **候裁① · 枚三枚四 note 同型黑话是否扩面**：组件三 note 含 ⟦SEMGOV-T3 挂载⟧⟦体例照 EAC 先例⟧⟦D 项收口同构⟧，组件四 note 含 ⟦TOOLHOME 票 S2⟧⟦票面草案 v4 ccf6383 放行 e12afd3⟧⟦TOOLHOME S2 改造臂⟧——与登记债项完全同型，但补裁点⑨ 登记文本点名组件一／二，扩面＝超登记射程新裁量，架构席不自扩。候处置：并入本票施工前放行＝需决策者或双席快审扩登记一句话；不扩＝本票按现闭集施工，余面挂账第三票。本票现闭集**不含**枚三枚四。
- **自决② · 外部产地全 hash 66e02d2…44 保留**：该 40 位串＝上游 fork 克隆指纹（外部产地溯源数据），非「仓 sha 短串」类（该类指我方仓 commit 短串如 730962e）；读者＝装配维护者核溯源所需，且同行自带「登记见该技能 README」登记锚。保留不动，如决策者认定亦属黑话可裁删。
- **自决③ · 日级日期随批名一并去**：登记射程＝指令时刻（精确到分）；日级日期本身未列黑话类。处置自决＝日级日期全部系于批名／指令句（如「2026-10-30 EAC-CLN 指针闭集整改」），批名既去，孤存日期无信息增量且仍泄露治理节奏，随去。版本沿革链（tag v1.0→…→v1.1.3）全保留＝决策理由句本体。

## 五、链衔接

链第 1 步＝本票起草笔（架构席·本笔）。第 2 步＝双席快审（产品席＋QA 席 fresh eyes：审 S1／S2 清理后文可照抄性·V1 token 清单完备性·候裁①取舍）。第 3 步＝放行登记（主理人·含候裁①裁决落账）。第 4 步＝工程师施工一笔（靶件一枚）＋回执一笔（落 .scratch／tickets／）。第 5 步＝fresh QA 按 §三 V 系独立验收判词。第 6 步＝收口登记（主理人）。

## 六、落链纪律段（各笔共守·写死）

- 单件／本笔面 pathspec 两端齐带（add 与 commit 各带本笔面路径）；add 紧邻 commit 零窗口；commit 前 git diff --cached --name-only 坐实仅自笔面。
- FX_COMMIT_DECLARE＝仓根相对纯路径清单（逗号或换行分隔）**挂 commit 命令侧**（环境变量前置挂 commit；挂 add 侧会被 STAGED-DECL-BLOCK 拦）。
- 禁 add -A／禁 amend／禁 --no-verify；message 以 collab: 起头·零 at 符号·零反引号；尾标置 message 最末位。**本票各笔尾标闭集**：本票笔 -TICKET／QA 快审笔 -QA-REV／产品快审笔 -PM-REV／放行登记笔 -PM-RELEASE／工程师施工笔 -BUILD／工程师回执笔 -RECEIPT／QA 验收笔 -QAV／收口登记笔 -GCLOSE（族名 DEBTCLN-R2 随尾标内嵌）。
- 一票一 commit 增量落盘；commit 类命令 timeout 600000ms；撞 index.lock 有界等待零删锁。
- 防自咬体例＝票面／回执正文路径裸文＋全角斜杠叙述形态；引文 ⟦⟧；票面与回执自身须过 check-pointers --target exit 0 后才可落链。
- 临时工作物只落仓根 .scratch／debt2／ 族；本席起草笔只写票面这一件。

## 七、起草笔自证（落笔后、commit 前实跑）

- 开工读数＝§〇 全表（当轮现跑·HEAD d4cb54b 与派工预期全等）。
- 本票面自靶＝python share/check-pointers.py --root . --target .scratch／tickets／2026-11-16-DEBTCLN-R2-BLNOTE锁件note清理票-v1.md → **exit 0**（实跑坐实）。
- 靶件基线双哈希＝§〇 在册（sha256 cf1fb51…／blob 9730486…）；V3 的 git show HEAD 基线以本票落链后链上态为准（本票笔不触靶件，HEAD 态靶件哈希不变）。
- 本笔面＝恰票面一件；其余全程零触碰；他案脏面零带入。
