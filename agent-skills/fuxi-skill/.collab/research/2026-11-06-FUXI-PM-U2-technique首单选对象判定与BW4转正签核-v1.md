# FUXI · PM-U2 technique 首单选对象判定＋BW-4 转正消费侧口径签核 v1

> 产品席（software-team-product-u8）亲笔｜日期＝2026-11-06｜性质＝产品判定件（FUXI 账域·research 面）·只读调查产物，除本件外零写入
> 开工 ANCHOR 实测＝HEAD `cb23a20f44d3f7299a326be3e3d269eb58d1d897`（工作树净——untracked 仅 `.scratch/` 与 ledger 过程面）；调查期间 HEAD 前移至 `177f5bc56da53a598c2667d9f08d0efad7add10c`（他席提交，本件不引用其票面），现盘 assert 汇总对前移后工作树实跑。
> 续判关系＝PM-U1（`agent-skills/fuxi-skill/.collab/research/2026-11-04-FUXI-PM-U1-下一段优先级产品判定-v1.md`）§二第5行（BW-4 随首单转正）＋§二第8行（f3 technique 首单·选小对象控范围）＋§三「第四段＝technique 首单＋BW-4 转正」的四段落地判定。
> fresh eyes 独立实跑：架构席票面并行起草中，本件零等待零引用。

---

## 一、现盘 assert 汇总实跑读数照登（本席实跑，不采信转述）

实跑 `agent-skills/fuxi-skill/gates/assert-tool.py` 全量：**27 项＝PASS 25／FAIL 1／PENDING_STAGE 1**，exit 0。

- FAIL＝BW-3（裸数字 6 处：`agent-skills/fuxi-skill/products/pending/miyazaki-hayao-perspective/` 三处＋`agent-skills/fuxi-skill/products/pending/mrbeast-perspective/` 三处）——FX-U4 实装后首咬，属产物侧真实缺陷读数，非工具故障，与本票两判定无阻塞关系（technique 首单产物不得复制该形态：registration/SKILL.md 内占比类数字必带三件套）。
- PENDING_STAGE＝BW-4（`agent-skills/fuxi-skill/gates/assert-tool.py` 函数 `bw_4_b_segment_decl` 现读＝桩行返回 `(READ_PENDING, "S1")`，未实装）——本件 §三 签核转正口径。
- 池形态实读：active 池条目 1（`agent-skills/fuxi-skill/products/david-fincher-perspective/`，`confirmation.md` 四字段在场，FC-6 PASS＝实条目确认引用行判绿）；pending 条目 2（miyazaki-hayao-perspective／mrbeast-perspective）；archive 3；**technique 轨产物＝0 条目**（GS-2 method 记录 0 条·空扫描合法态在册）。
- GS-4 PASS（元组 2 在场·κ 对账全一致）＝PM-U1 §二第2行诉求已兑现；FC-6 已随 FX-U6 首单入池兑现。即 PM-U1 首/二/三/四段中的第一至三段已落地，本票＝第四段的产品侧两件。

依据面实读：`agent-skills/fuxi-skill/specs/technique-spec.md`（六段节闭集／B 段存在且非空占位＝BW-4／卡体五字段）、`agent-skills/fuxi-skill/adapters/method.md`（RIA++ 六段／防误触发护栏三件套＝B 段边界＋诱饵测试＋触发断言／Air-gapped 语料封闭给定 B-6）、`agent-skills/fuxi-skill/adapters/classifier.md`（Q1-Q4 决策序／J-4 方法工具书判例／J-5 教科书规程判例）、`agent-skills/fuxi-skill/gates/assertion-catalog.md` BW-4 行＋ST-3/BW-3/ST-9/ST-10 扫描面口径、`agent-skills/fuxi-skill/gates/validator-source-anchor.py` L1（卡级 B 段空占位＝BW-4 咬点）、`agent-skills/fuxi-skill/contracts/evidence-grading.md` EG-6（一手占比门槛 50／新鲜度窗口 12 月／黑名单非空）、`agent-skills/fuxi-skill/products/README.md`＋`agent-skills/fuxi-skill/products/pending/README.md` 池规程。

---

## 二、判定一：technique 首单选对象

### 2.1 资格线（硬门轨＝source-anchor 消费面决定，不是偏好问题）

首单对象须同时满足四条（PM-U1 §二第8行「选小对象·单一操作性方法文本」的操作化）：

1. **单一操作性技法**＝分类器 Q2 否＋Q4 有（判例 J-4 方法工具书／J-5 教科书操作规程型），可被抽成 R/I/A1/A2/E/B 六段结构；拒绝 mixed 案型（J-3 拆两轨＝首单范围翻倍）。
2. **一手来源可锚性（硬门资格线）**＝存在**单一、完整、位置可逐字成对回查**的一手文本：产物 R 段原文引文带 `source_id`＋位置成对（FC-3），validator-source-anchor L1 逐卡检。来源散见于演讲录/幻灯简报/二手重构拼盘的候选＝位置成对锚不稳，直接剔。
3. **语料可得性实指**＝method 轨 Air-gapped 纪律（B-6）：原文由用户提供封闭语料，无文本即停。候选须能指认到**具体可交付文本版本**（公有版全文/用户提供书目），不得停在题材名。
4. **体量可控**＝首单端到端（产物三件＋ST-3/BW-4/FC-3/ST-9 产物侧＋source-anchor L1 实跑＋BW-4 随批转正）一段内收口；卡数可枚举、正文规模可控。

### 2.2 候选菜单（三候选＋逐条可锚性评估与否决理由）

| 候选 | 一手来源可锚性评估 | 判定 |
|---|---|---|
| **A《The Elements of Style》（Strunk & White）** | **过**：单一成书文本，1918 年初版公有领域全文可整本封闭给定（B-6 无版权交付障碍），规则条目有章/节/条目编号——`source_id`＋位置成对回查为机械动作；全书即操作性规则文本（规则＋改正方法＋范例），J-4 案型直配。 | **推荐首单** |
| **B《Getting Things Done》（David Allen）** | 过（单一成书，版次位置可成对），但可得性依赖用户提供受版权书本文本；体量约三百页，方法论为流程套件（收集—处理—组织—回顾—执行），可卡片化方法与 apparatus 叙述混杂，跨段落佐证密度逐方法不均——首单端到端范围膨胀风险。 | 次选备位（A 实施受阻时顶替） |
| **C OODA 环（John Boyd）** | **不过→剔**：无单一操作性文本载体——一手料散于讲座口头记录、幻灯简报（图片态幻灯的文本层薄）、后人重构拼盘；位置成对锚不定型；题材解释面已被二手文献重度污染，基座先验冒充蒸馏的泄漏面大（FM-M-02 术语壁垒＋hold-out 时间轴口径悬空风险）。硬门资格线第 2 条直接剔。 | 剔 |

候选外排除登记（防后续追问）：《如何阅读一本书》（Adler）不入菜单——`agent-skills/fuxi-skill/adapters/method.md` 首节已把 Adler 分析阅读＋五路提取作为 method 轨**工序方法论**照搬入册（C2）；再以同一文本蒸馏为**产物本体**＝工具蒸自身工序，自指混淆面（IR 串味变体），产品席定性排除，非语料问题。

### 2.3 判定：推荐首单＋范围闭集建议

**推荐首单对象＝《The Elements of Style》**，对象 id＝`elements-of-style`，产物目录名＝`elements-of-style-technique`（`<对象名kebab>-technique` 命名纪律）。

范围闭集建议（产物落位形态照 person 轨先例，轨别字段换值）：

- 落位＝`agent-skills/fuxi-skill/products/pending/elements-of-style-technique/`，随件三件套＝`SKILL.md`＋`test-prompts.md`＋`registration.md`（pending 约定件条目清单行随批增行，轨别列值＝`method`——注意与 person 先例不同词表行：分类器四值输出＝`method`（J-4），产物 `所属轨` 取值＝`method`（AC-1 值注册表三值），两词表不同层不互推）。
- registration 四节闭集照 ST-9 逐字（注册三元组／分类器四问决策记录／采集与蒸馏声明／语料门槛登记 EG-6）；EG-6 侧封闭语料一手占比天然高（原文即一手），但新鲜度窗口月数=12 对成书文本的读数口径须如实登记（书初版远超窗口＝按 EG-6 现文照判，登记受限口径不凑档——此为 EG-6 对 method 轨首例适用，读数语义须写清不造第二套门槛）。
- 首单完成定义（控范围，PM-U1「小对象」钉）＝产物侧结构检实扫（ST-3 technique 六段／BW-4 实装实扫／FC-3／ST-9）＋source-anchor L1 机械断言层实跑；VA-S 六层中三臂/诱饵/留出/泄漏/边缘诚实度层随 harness 批次工件到位前一律记未验（VA-X-01 三值纪律在册，不以缺工件推定绿也不因缺工件阻塞转正）。BW-4 转正随本批（见 §三）。
- 语料动作前置＝用户提供封闭文本（B-6）：1918 公有版全文为默认建议，用户若指定其他版次则以该版封闭收讫＋封存时戳登记（method 侧 T 定义）。

**对象确认是否另设闸＝判否**。理由：①入池人工闸已在池规程（pending→active＝人工确认＋独立提案＋版本审计，确认人＝皮总），再设选对象闸＝入池规程外增设闸位，恰属 PM-U1 §五须产品签核的规程变更，产品席现判不扩；②B-6 语料封闭给定要求本身已把对象确认固化为人类动作点——用户交付/指定封闭文本＝对象的事实确认位，无需重复建制；③分类判定不靠闸靠机检面：四问决策记录入 registration（ST-9 咬节闭集），分歧走 classifier §四人工终裁机制。选对象动作本身＝产品席范围意见＋主理人任务令射程，无需第三闸。

---

## 三、判定二：BW-4 转正消费侧口径签核

消费语义签核面（断言编号、代码结构、selftest 配对形态归架构席，本签核不管辖）：

**【产品签核 · BW-4 转正消费侧口径】本断言防＝technique 产物能力卡缺 B 段（边界）＝徒有其名的技法包：无边界声明的卡撑不起本轨防误触发护栏三件套（B 段边界＋诱饵测试＋触发断言，B-3），违「边界必须明确、验证不过不晋级」铁律（B-7），失效面＝误触发即本轨失效模式（M-3）。判绿条件＝产物级扫描面内每个 technique 轨条目的每张能力卡 B 段存在且非空占位，逐卡全量判，禁「至少一卡绿」平滑；「存在」形态以 specs 真源为准不另造＝`agent-skills/fuxi-skill/specs/technique-spec.md` 节闭集表段名注册闭集（含段名前缀归一化口径：裸段名「B」与全形态「B 边界」两写法同判合法，描述名须与注册描述名逐字全等）＋卡体五字段 `边界` 非空——即断言工具 `TECHNIQUE_CARD_SECTIONS`/`TECHNIQUE_CARD_FIELDS` 注册位单源，卡解析面复用 ST-3 technique 侧既有归一化口径，禁第二套解析。判红＝任一条目任一卡 B 段缺位或空占位（空串／纯空白／占位符样文本按 specs 空占位口径），或描述名漂移（归 ST-3 咬面时 BW-4 读数行须注明不重复咬，防一号两判）；判红语义＝铁律机械位缺位，该产物不晋级，退回补写（禁以 VA 层后续层读数补偿）。扫描面＝与既有产物级扫描面枚举同基（`agent-skills/fuxi-skill/products/` 根直接条目＋`agent-skills/fuxi-skill/products/pending/` 一层下产物目录；`agent-skills/fuxi-skill/products/archive/` 免检自动继承；ST-3/BW-1/BW-2/BW-3/BW-5(b)/ST-9/ST-10 同基），technique 条目按轨别/目录后缀（-technique／-bundle technique 层）入扫，person 条目不入 BW-4 判据面。空扫描态口径写死两态：(a) **转正批次**＝BW-4 实装转正必须与首个 technique 产物同批，验收读数必须出现「扫描 N 件·N≥1」实扫判绿——空扫描不得作转正批次验收读数（PM-U1 §二第5行「实装了也只是空扫描＝工具自嗨」判词现行效力，随首单转正＝转正条件本身）；(b) **转正后稳态**＝technique 条目为零时判绿但读数行必须带「空扫描合法态」标注（同族 ST-3/BW-3/FC-5 三态读数保真同制，防空池平凡真被误读为产物级实证），转正前当期保持 PENDING（不算 PASS 不算 FAIL，VA-X-01 未验三值同族）。**

配套随批观察项（不属签核约束力，供架构票面参考）：BW-4 读数行建议随附条目数/卡数计数（与 BW-3「扫描 N 件」读数形态同族，保「漂亮读数骗人」防线上的读数可回查性）。

---

## 四、回执摘要（供主理人随架构票面登记）

- 判定件路径＝`agent-skills/fuxi-skill/.collab/research/2026-11-06-FUXI-PM-U2-technique首单选对象判定与BW4转正签核-v1.md`
- 首单对象推荐一句话＝**technique 首单选《The Elements of Style》（Strunk & White，1918 公有版整本封闭语料，id＝`elements-of-style-technique`，落 pending 三件套随批，BW-4 转正同批）**。
- BW-4 口径签核行＝本件 §三加粗签核块原文（整段随架构票面「产品签核」行登记）。
- 选对象不另设人工闸（判否，理由见 §2.3）；入池终闸维持池规程单一人工闸不变。

——产品席 software-team-product-u8·本件可推翻项已标注（首单对象可被用户指定语料顶替＝B 顶 A；BW-4 空扫描稳态口径若与门禁面重交付程序冲突，回产品段重签）。

---

## Append · 随正注记（2026-11-06·产品席亲笔·append-only·以上正文一字未动）

> 依据＝皮总裁定誊录件 `agent-skills/fuxi-skill/.collab/decisions/2026-11-06-皮总裁定-FUXI-语料版次改裁1920.md`（commit `25f4f0f`）＋PM-U4 判定件（commit `8b02db9`）§六随动面 2 预告笔。注记制，版本不另钉号。

1. **措辞随正声明（两处）**：§2.2 候选 A 行「1918 年初版公有领域全文可整本封闭给定」与 §四回执摘要「1918 公有版整本封闭语料」两处「1918」措辞随正——技法首单封闭语料基准改定为 **Gutenberg eBook #37134《The Elements of Style》William Strunk 1920 年自订商业修订版**（公有领域·预核 sha256=`bf5312eb0fa36837253ec84211cdab51deae01744e1de3ffef528aee43c27496`·收讫封存·版次如实登记 1920，引裁定件 `25f4f0f`）。§2.3「1918 公有版全文为默认建议」一语系同一字面随裁同承（"默认"载体随裁定迁移，该节其余判定不动）。
2. **#1232 指认歧义认领行**：本件初笔选对象只钉来源描述（"公有领域全文可整本封闭给定"）未钉电子书编号＝下游票面误指 #1232（实＝The Prince）的歧义源头——产品席认领一行；源头判定已在册＝PM-U4 件（`8b02db9`），指认勘误已落 FX-U8 票面（`edcd88c`），本行仅登记认领不另展开。
3. **判定效力声明**：判定一（首单选对象＝《The Elements of Style》，对象 id／产物目录名＝`elements-of-style-technique`）与判定二（BW-4 转正消费侧口径签核 §三加粗块原文）效力不变——本次仅语料载体版次随裁（1918 私印初本 → #37134 1920 自订定本），承重理由"公有可得性＋单文本可锚性"逐条复查全过（PM-U4 §二在册）；裁定禁随动面钉死清单（gates/ 全树、产物目录名、首单完成定义、BW-4 转正条件）本注记零触达，§2.3 范围闭集建议各条照旧。

——产品席 software-team-product-u8·append 笔·2026-11-06。
