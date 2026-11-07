# elements-of-style-technique

> 性质＝`-technique` 产物本体（method 轨·即用即走能力卡集）。触发命中即读卡，用完退场，不常驻对话全程；本产物不扮演任何人、不冒充具名人物发言。
> 总则：宁可生成一个诚实标注局限的 60 分产物，也不要一个看似完美的 90 分造假产物。
> 封闭语料声明：全部 R 段引文只锚定收讫封闭语料（Gutenberg eBook #37134《The Elements of Style》by William Strunk·1920 自订商业修订版·sha256 封印件），零基座记忆补全；外部请求计数=`0`。
> 诚实边界三句：本产物语料＝1920 自订商业修订版；R 段引文只锚定该版收讫文本（哈希封印）；对 1918 私印初版的条目差异不作任何断言（不可本地实证）；1959 起 Strunk & White 修订本受版权保护、非本语料、禁混换。
> 卡集规模 N=`7`（蒸馏实况定数·减除留痕见 registration「采集与蒸馏声明」节语料主题配平行）；`验证状态` 全部＝`未验`（validator L1 机械层判绿＝当期唯一实证位，L2-L6 工件缺位记未验，不进取门禁位）。

### 元数据（AC-1..AC-3）

- `产物id`=`elements-of-style-technique`（与目录名逐字全等）
- `所属轨`=`method`
- `编译形态`=`single`
- `快照时戳`=`2026-11-06`
- `版本号`=`v0.1`
- `复审到期日`=`2027-01-05`
- `calibration_state`=`待校准`（method 轨登记缺省值，无软判据层不造 κ）
- 准入证据卡（三栏）：`evidence_grade`=`机械断言`（validator-source-anchor L1 实跑判绿＝当期唯一门禁位）｜`control_arm`=`未测`（三臂对照工件缺位）｜`leakage_check`=`未检`（test-prompts 题面未对照语料——判分段预注册件缺位＝未验如实）

---

### eos-t-01 paragraph-unit-topic 一段一题成块法（Ch III Rule 8）

```json
{"出处": "source_id=eos-b1:elements-of-style:original-full-text.md；位置=Ch III Rule 8 · p.15 · L554-555（佐证 L565-569、L571-573、L557-563、L614-616）", "触发": "草稿段落混装两个以上话题，或改稿后段落膨胀、读者抓不住意义单位时", "步骤": "列话题清单→一话题一段→简短主题可不细分→过渡句可独立成段", "边界": "适用多话题展开切块；不适用清单体与模板固定段；简短单段与过渡句段为规则自设例外", "验证状态": "未验"}
```

## R 原文

「Make the paragraph the unit of composition: one paragraph to each topic.」（source_id=`eos-b1:elements-of-style:original-full-text.md`·位置＝Ch III Rule 8 · p.15 · L554-555）

## I 诠释

段落＝作文单位：先把主题切分成话题，每个话题做成一段的主语，读者才不需要自己在意义单位之间自行划界。

## A1 案例

解说段「a subject requires subdivision into topics, each of which should be made the subject of a paragraph」（位置＝L565-566）＋切分目的段「to aid the reader」（位置＝L567-569）＋细分程度段（位置＝L571-573）。

## A2 触发场景

草稿段落混装两个以上话题；改稿后段落膨胀读者抓不住单位；长文需要按话题切块时。不触发：清单体、固定模板段。

## E 执行步骤

①列出当前段落承载的话题清单；②话题多于一个→按话题各拆独立段落，每段一题；③主题简短可不细分（「there may be no need of subdividing」L557-563）；④过渡句可独立成段（L614-616）。

## B 边界

适用＝散文/文档多话题展开的切块；不适用＝清单体、模板固定段；简短主题单段与过渡句独立成段是规则自设例外（L557-563、L614-616），不判违例。

---

### eos-t-02 topic-sentence-frame 主题句起收成框法（Ch III Rule 9）

```json
{"出处": "source_id=eos-b1:elements-of-style:original-full-text.md；位置=Ch III Rule 9 · p.17 · L635（佐证 L626-627、L634-641、L643-652、L664-684）", "触发": "议论或说明段需要显式观点框定，或段落以离题收尾时", "步骤": "定主题→主题句置段首→中段展开主题句→末句强调或给出后果→叙述描写段例外不套", "边界": "适用议论/说明段；叙述描写段合法例外；此法过频成腔调须与无主题句段式交替", "验证状态": "未验"}
```

## R 原文

「(a) the topic sentence comes at or near the beginning;」（source_id=`eos-b1:elements-of-style:original-full-text.md`·位置＝Ch III Rule 9 · p.17 · L635）

## I 诠释

三段式段落框：段首主题句→中段解释/证实/展开主题句→段尾强调主题句思想或陈述重要后果；起收相符，避免以离题收尾。

## A1 案例

Stevenson《Walking Tours》九句段逐句拆注（1 Topic sentence…9 strong conclusion）（位置＝Ch III Rule 9 · p.17 · L664-684）＋Lecky 史例段（位置＝L695-713）。

## A2 触发场景

议论/说明段需要显式框定观点；段落结尾跑题（以离题收尾）时。不触发：叙述/描写段常态。

## E 执行步骤

①确定段落主题；②主题句置于段首或近段首；③中段句解释/证实/展开主题句；④末句强调主题句思想或陈述重要后果；⑤叙述/描写段常无主题句＝合法例外（L717-721）。

## B 边界

适用＝议论/说明段框定；不适用＝叙述/描写段（规则自设限定「As a rule」L626＋L717-721）；此法过频会成腔调（「this device, if too often used, would become a mannerism」L728-730），须与无主题句段式交替。

---

### eos-t-03 active-voice-choice 主动语态择语法（Ch III Rule 10）

```json
{"出处": "source_id=eos-b1:elements-of-style:original-full-text.md；位置=Ch III Rule 10 · p.19 · L744（佐证 L746-747、L762-764、L769-784、L808-818）", "触发": "施事者在场但动作被 be 结构或名词化掩埋、流程叙述主语涣散时", "步骤": "找真实施事者→改施事者主动骨架→施事者缺位或不相干则被动合法→悬念语序可用被动工具", "边界": "不适用施事者未知、不相干、有意隐去与主语连贯需要被动的场合（规则自设限定在场）", "验证状态": "未验"}
```

## R 原文

「Use the active voice.」（source_id=`eos-b1:elements-of-style:original-full-text.md`·位置＝Ch III Rule 10 · p.19 · L744）

## I 诠释

让做事者做句子主语、动作直接呈现——主动骨架更直接有力；语态选择＝主语聚焦决策，不是被动禁用令。

## A1 案例

「There were a great number of dead leaves lying on the ground.」→「Dead leaves covered the ground.」（位置＝L816-818）；「A survey of this region was made in 1900.」→「This region was surveyed in 1900.」（位置＝L794-796）。

## A2 触发场景

施事者在场但动作被 be 结构/名词化掩埋；流程叙述主语涣散、责任主语不明时。不触发：施事者缺位的合法被动。

## E 执行步骤

①找句子真实施事者；②改写为施事者主语的主动骨架；③施事者未知/不相干/有意隐去→被动合法（主语聚焦决定语态·L769-775）；④需要制造悬念的语序可用被动工具（L777-784）。

## B 边界

适用＝施事者在场的叙述与说明；不适用＝施事者未知/不相干/有意隐去、主语连贯需要被动的场合——「This rule does not, of course, mean that the writer should entirely discard the passive voice, which is frequently convenient and sometimes necessary.」（L762-764）。

---

### eos-t-04 positive-form-assert 正面肯定断言法（Ch III Rule 11）

```json
{"出处": "source_id=eos-b1:elements-of-style:original-full-text.md；位置=Ch III Rule 11 · p.21 · L833（佐证 L835-837、L839-841、L855-856、L858-884）", "触发": "句子以 not 系对冲措辞、否定式被用作回避断言时", "步骤": "找出否定表述实际所指→正面词改写→意向不明先确认再改→修辞对偶的 not 保留", "边界": "不适用否定真命题的合法直陈与修辞对偶；改写须以明确意向为据否则等于猜测", "验证状态": "未验"}
```

## R 原文

「Put statements in positive form.」（source_id=`eos-b1:elements-of-style:original-full-text.md`·位置＝Ch III Rule 11 · p.21 · L833）

## I 诠释

说「是什么」而非「不是什么」——正面词承载更确定的信息；「the weakness inherent in the word not」（L858）：not 承载与生俱来的弱化信号，回避型否定须改回直陈。

## A1 案例

「He was not very often on time.」→「He usually came late.」（位置＝L839-841）；not→正面词对表（位置＝L858-878）。

## A2 触发场景

句子以 not 系对冲措辞（not many／not often／not impossible）；否定式被用作回避断言时。不触发：否定本身即真命题核心的场合。

## E 执行步骤

①找出否定表述的实际所指；②用正面词直接改写（not very often→late 类词对·L858-878）；③原作者意向不明→先确认再改（「simply a guess at the writer's intention」L855-856）；④修辞性对偶（antithesis）中的 not 保留（L879-884）。

## B 边界

适用＝事实陈述与回避型否定；不适用＝否定真命题的合法直陈与修辞对偶（L879-884）；改写须以明确意向为据，意向不明时改正版＝猜测（L855-856），先确认再动。

---

### eos-t-05 concrete-specificity 具象特指唤像法（Ch III Rule 12）

```json
{"出处": "source_id=eos-b1:elements-of-style:original-full-text.md；位置=Ch III Rule 12 · p.22 · L894（佐证 L896-897、L899-901、L913-916、L944-948）", "触发": "行文充满抽象概括词、读者无法形成画面时", "步骤": "标抽象概括词→自问可观察层面→以确定特指具象细节替换→细节服务主导印象非全录", "边界": "不适用刻意保持抽象层级的总括与隐私合规约束场景；细节须核实过，禁为具象而造细节", "验证状态": "未验"}
```

## R 原文

「Use definite, specific, concrete language.」（source_id=`eos-b1:elements-of-style:original-full-text.md`·位置＝Ch III Rule 12 · p.22 · L894）

## I 诠释

写到可观察层面——特指胜过一般、确定胜过含混、具象胜过抽象；「definiteness of the details」（L944-948 区段）是抓住注意力可靠的方式。

## A1 案例

「A period of unfavorable weather set in.」→「It rained every day for a week.」（位置＝L899-901）；Browning《My Last Duchess》引诗细节例（位置＝L921-935）。

## A2 触发场景

行文充满抽象概括词（period／situation／problem 类）；读者无法形成画面、说服失焦时。不触发：刻意抽象层级的总括陈述。

## E 执行步骤

①标出抽象概括词；②自问「该情形的可观察层面是什么」；③以确定＋特指＋具象细节替换（时间/数量/感官形象）；④细节选择服务于主导印象，非细节全录（「It is not that every detail is given; that would be impossible, as well as to no purpose」L947-949）。

## B 边界

适用＝需要画面感的叙述与说服性写作；不适用＝刻意保持抽象层级的总括、隐私/合规约束场景；细节必须是核实过的事实，禁为具象而造细节。

---

### eos-t-06 omit-needless-words 冗词删削法（Ch III Rule 13）

```json
{"出处": "source_id=eos-b1:elements-of-style:original-full-text.md；位置=Ch III Rule 13 · p.24 · L979（佐证 L981-987、L1018-1042、L1057-1060、L1065-1074）", "触发": "there are、it is、the fact that 类空转句架在场、从句重复已立内容时", "步骤": "排查空转句架→冗语缩为单词→同内容短句合并→必要细节段不裁", "边界": "本规则不是写短句令；不得删除承载时间逻辑线索的必要信息；改写优先于纯删", "验证状态": "未验"}
```

## R 原文

「Omit needless words.」（source_id=`eos-b1:elements-of-style:original-full-text.md`·位置＝Ch III Rule 13 · p.24 · L979）

## I 诠释

每个词都要干活——文气来自紧凑：「Vigorous writing is concise.」（L981）句无不必要词、成分无不必要部分；不是人人写短句，而是 make every word tell。

## A1 案例

「the fact that」六连改（位置＝L1018-1042）；Macbeth 五短句并为 26 词（位置＝L1065-1074）；与 Rules 11/12 互见段（位置＝L1057-1060）。

## A2 触发场景

there are／it is／the fact that／in spite of the fact 类空转句架在场；从句重复已立内容时。不触发：承载必要时间/逻辑线索的长句。

## E 执行步骤

①排查空转句架；②冗语缩为单词（与正面式/主动式互见·L1057-1060）；③同一内容短句合并；④必要细节段不裁——「This requires not that the writer make all his sentences short… but that he make every word tell.」（L984-987）。

## B 边界

适用＝空转句架与冗语；不适用＝承载时间/逻辑线索必要信息的长句与必要细节段（L984-987 限定在场）；删除不得拆掉连贯性，改写优先于纯删。

---

### eos-t-07 emphatic-end-placement 强调置末排布法（Ch III Rule 18）

```json
{"出处": "source_id=eos-b1:elements-of-style:original-full-text.md；位置=Ch III Rule 18 · p.31 · L1336（佐证 L1338-1339、L1341-1344、L1354-1355、L1376-1395）", "触发": "句末落在背景信息、新信息被埋在句中、关键限定打断核心信息流时", "步骤": "确定想突出的要素→置于句末新信息位→置首强调须另有支持→圆周句中断造势为例外→原则外推至从句段落", "边界": "不适用已有其他支持手段的置首强调与刻意中断造势的圆周句", "验证状态": "未验"}
```

## R 原文

「Place the emphatic words of a sentence at the end.」（source_id=`eos-b1:elements-of-style:original-full-text.md`·位置＝Ch III Rule 18 · p.31 · L1336）

## I 诠释

把想突出的要素放句末＝句子的新信息落位（「the logical predicate, that is, the new element in the sentence」L1354-1355）；同一排布原则从词外推到从句与段落（「applies equally」L1393-1395）。

## A1 案例

Humanity fortitude 改写置末（位置＝L1341-1344）；Columbus 圆周句造势例（位置＝L1360-1374）。

## A2 触发场景

句末落在背景信息、新信息被埋在句中；关键限定打断核心信息流时。不触发：刻意圆周句与已有支持手段的置首强调。

## E 执行步骤

①确定全句想让读者记住的要素；②将该要素置于句末＝logical predicate 新信息位（L1354-1355）；③置首强调须另有支持手段（L1371-1375）；④需要悬念的中断语序可用圆周句工具（L1360-1374）；⑤原则外推至从句与段落排布（L1393-1395）。

## B 边界

适用＝陈述句与段落的信息排布；不适用＝已有其他支持手段的置首强调（「A subject coming first in its sentence may be emphatic, but hardly by its position alone」L1381-1382）与刻意中断造势的圆周句（互见 L1223-1225）。

---

- 卡数＝7；每卡六段节头（R 原文／I 诠释／A1 案例／A2 触发场景／E 执行步骤／B 边界）＋卡体五字段 json 块逐卡在场；`验证状态` 全部＝`未验`（AC-3：未验不进取门禁位）。
