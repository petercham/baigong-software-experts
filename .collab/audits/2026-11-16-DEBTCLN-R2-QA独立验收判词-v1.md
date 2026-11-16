# DEBTCLN-R2 · QA 独立验收判词 v1（QA 席 qa-debt2v·fresh eyes·全部现跑禁抄回执）

- 结论：**IS_PASS**＝红 0／黄 0／绿＝全套判据面（V0–V6＋钉值＋对抗四臂＋并发窗两案型独立核验定性）
- 开工读数：HEAD＝**e4616b5**（与派工预期全等）；链序核对＝5f616d0 票笔 → 1811bf4 rev1 扩面 → 0a7e292 QA 快审 → ad74861 产品快审 → 2bfbb00 放行登记 → 9cbe850 BUILD → e4616b5 RECEIPT 相对次序全等（其间插外案笔 e6229be／c0f5382＝归因照登）。
- 时点＝date 实测 2026-11-17 01:05 前后（本轮现跑）。
- 脏面照登（本验收轮现跑）：tracked 恰一枚 M＝agent-experts／baigong-software-team／．collab／ledger／ledger.jsonl（他案）＋?? 二十四行（活体群随外案漂移·放行登记 §二-1 现跑照登口径）——全部他案，零带入零清理零 add。
- 依据件只读面：票面 blob＝git ls-tree 1811bf4 复验＝**faf1d6926f81e975e5cc1dea76f70fc754944d3c** 全等；票面／双席判词／放行登记各自 git log 复跑＝入链笔各恰一枚（5f616d0＋1811bf4／0a7e292／ad74861／2bfbb00）＝零回改坐实；双席判词 blob 745b2ac＋d613c3a 全等复验。

## 一、V 系逐项实跑（全部本席现跑）

- **V1 黑话清零（票 §八 rev 段 28 枚 token verbatim）**：
  - 对后态链上内容（git show HEAD 版靶件落隔离件后跑）→ **exit 0**·28 枚全部计数 0（皮总／决议批／改名批／20261029a／SK-3／04:11／EAC-CLN／㊺／换钉批／纠正吧／CLN-PURE／40-artifacts／D 项收口／T-deepresearch-01／R-1／QA-deepresearch／minor-a／T-deepresearch-02／R-6／730962e／指令授权／SEMGOV-T3／EAC／TOOLHOME／票 S2／ccf6383／e12afd3／票面草案 逐枚零）。
  - 对前态（git show 2bfbb00 版＝blob 9730486）同命令 → **exit 1**·28/28 命中非零（皮总×3／EAC×3／㊺×2／D 项收口×2／EAC-CLN×2／其余逐枚≥1）＝**判据区分度复验成立（非空转）**。
- **V2**：json.load 解析打印 **PARSE-OK·components＝4**·exit 0。
- **V3**：git diff 2bfbb00 9cbe850 --numstat 于靶件＝**4／4 恰四行**；diff 全文改动行＝第 19／29／39／50 行四枚 note 值行（四 hunk 段号 -16／-26／-36／-47 各 7 行窗内恰一行改）。结构化对拍（2bfbb00 链上态 vs 9cbe850 链上态·四枚 note 置等哨兵）→ 打印 **REST-EQUAL**。另加本席独立 byte 级对拍：前后两态各 68 行（LF 切分），差异行号集合＝{19,29,39,50} 恰四枚 note 值行，其余全部行 byte 级相等＋行数相等 → **NONNOTE-BYTE-EQUAL True**（lock_version／bundle 行含其 note／四组件行非 note 键／版本值／assembly_exclude／conventions 全部零扰动自证）。
- **V4**：python share/check-adr.py --root ． → **exit 0**（桶1=1 桶2=20 桶3=1 发现 0·与放行登记 §〇 基线全等）；publish.py 组件五键断言 → **True**。
- **V5 自靶**：python share/check-pointers.py --root ． --target 本判词件实路径 → **exit 0**（实跑坐实·读数随完工回报）。
- **V6（处置口径＝放行后补充·9cbe850/e4616b5 树面两件案型）**：见 §三。
- **钉值**：python share/check-pointers.py 缺省扫描 → grep -c BLOCK＝**22810 零新增**／grep -c WATCH＝**4582 零新增**；bash share/run-gates.sh → **GATE PASS exit 0·发现 151503**（与开工基线 151503 全等·本验收轮实测零摆动·故无归因事项）。
- 靶件三面哈希复验：链上后态 blob＝**44e4633f0327fbf0e1f10ed4ce2901ac54d8e82f**（9cbe850 与 HEAD 同值）／前态 blob＝**973048685e0d655c3427e4fa04fa19394b25c66c**（2bfbb00）／工作区 sha256＝**c0b25a2140b6d09a7205d075ad90e573ffa6d39288fef0a50919c63030ac165f**（与回执 §三 宣称值全等）；靶件 status 零命中＝盘上态与链上态一致（core.autocrlf=true 环境下 CRLF 换算后全等·链上 blob 哈希为准绳）。

## 二、对抗臂（四臂全做·全过）

1. **豁免/零宽免复验**：四枚 note 对 28 枚 token **逐枚**检索（非仅串联域）→ 逐枚零命中（PER-NOTE-ZERO）；bundle 行 note 附带扫亦零命中（防御面加测）；邻仓 D:／multi-agent-collab-experts 的 workbuddy／baigong-video-team／bundle.lock＝git hash-object 盘上值 **038dd77b1884c57e96019e835e68f60332dd39a4** 与邻仓 HEAD ls-tree blob 全等＋该件 status 零命中＋邻仓链上最后触笔＝42a157c（2026-10-29）远早于本链＝**零触坐实**。
2. **清理后文 JSON 往返**：后态链上内容 json.load → json.dumps（indent=2·ensure_ascii=False·尾换行）→ 与链上文件 **byte 级全等**（ROUNDTRIP-BYTE-EQ True）＋再解析深相等（REPARSE-EQ True）＝无转义漂移、无结构损。
3. **施工笔/回执笔全仓面单**：git show --name-status 9cbe850 → 计数 **恰两枚**（M 靶件＋A board 件）·零其它；e4616b5 → **恰两枚**（A 回执件＋A 卷入登记件）·零其它；git diff --name-status 2bfbb00 9cbe850 全仓面＝同样恰两枚＝两笔间链上无第三方改动面。
4. **回执 §四 取证三条复跑**：① board 件工作区 mtime＝2026-11-17 00:40:45 晚于 9cbe850 committer 时间 00:37:07（全等回执宣称）；② git status 该路径现跑＝**零命中**；③ git log 该路径现跑＝**仅 9cbe850 一枚**＝首次入链即被裹入本 BUILD 笔坐实。

## 三、并发窗两案型独立核验与定性（V6 处置口径）

- **案型一（9cbe850 树面两件）**：靶件 M＋board 件 A。board 件（．collab／board／2026-11-17-起票双审放行段深度分析与优化点面-v1.md）内容完整性双核＝链上 blob **2bed4ef9b679df3ade5eb9e109cdbdd5e7eb87c7** 全等预期＋git hash-object 盘上值同值＋git show 链上字节流与盘上 cmp 全等＋sha256＝**62cf965e7b83d4f22d6a4a5f7f71f2603fe12d1b88a335d4c24ed97ecabe8223** 与登记件宣称全等＋262 行全等＝**零损坐实**。
- **案型二（e4616b5 树面两件＋message subject 置换）**：回执件 A＋卷入登记件 A；该笔 message 起头段确系外案 subject（卷入登记句＋[SWB-PIPEAUDIT-INVOLVE] 标签）置换我方回执 subject，正文仍含回执六节读数段全文＋尾标 **-RECEIPT** 置最末＝COMMIT_EDITMSG 并发窗案型（D-58 同族新变体）与登记定性一致。卷入登记件（．collab／decisions／2026-11-17-卷入登记-9cbe850混合笔-v1.md）内容完整性双核＝链上 blob **8ad9addb59845ebe948967859cae7283263137c7** 全等预期＋盘上 hash-object 同值＋链上字节流与盘上 cmp 全等＝**零损坐实**。回执件链上 blob＝**9909c89680d0a363ef932b18f8548c9398905d7d** 与预期全等＋盘上 hash-object 同值＋六节（一至六）齐。
- **工程师席侧定性（照已登记口径独立复核）**：三方互证面本席无从重跑 commit 时点快照，但可达面全合——① 9cbe850 面单两枚中靶件恰 M·board 件恰 A 非 M（＝本席未改一字）；② board 件内容与其 blob 全等零损；③ 该路径首次入链即此笔＝注入窗口归因成立。结合主理人裁决「登记即完结·不拆笔不回改」在册＝**面单纯度与 message 污染面＝已登记归因·不构成施工违例**。
- 尾标闭集核验：9cbe850 尾标 **-BUILD**／e4616b5 尾标 **-RECEIPT**（置最末）＝各笔尾标合规（e4616b5 起头段污染系外案置换、归案型二已登记面）。

## 四、其它实跑读数与观察

- V0 脏面：tracked 恰一枚 M（ledger 他案）＋?? 24 行（与放行登记轮实测持平·活体群漂移照登）。
- 临时面：．scratch／debt2／ 族四枚 txt＝盘上零命中＝用毕即拆坐实；该目录本体仍存（空目录·居 .gitignore 第 60 行 /.scratch/* ignored 面·对 tracked 计数与 GATE 路由零扰）＝观察随登不判项。
- 观察随登（不判项不候裁）：① 派工令所书卷入登记件名「混杂笔」与链上实名「混合笔」一字之差·blob 8ad9addb 双面对拍全等＝同一件·系派工面转述勘误级，登记留痕；② 本席验收轮隔离临时件居 ．scratch／debt2v／ ignored 面·用毕即拆。

## 五、结论行

**IS_PASS**＝红 0／黄 0／绿全套（V0–V6＋钉值四项＋对抗四臂＋并发窗两案型内容完整性双核全零损＋禁动面 byte 级零扰动）。DEBTCLN-R2 施工批（9cbe850＋e4616b5）验收通过，可入收口登记环节。本判词件面＝恰本判词一件；他案脏面零带入；链上史件零回改零触碰。

## 六、本笔自证

- 落笔前自靶：python share/check-pointers.py --root ． --target ．collab／audits／2026-11-16-DEBTCLN-R2-QA独立验收判词-v1.md → **exit 0**（实跑坐实）。
- 本笔面＝恰本判词一件·add 单 pathspec 紧邻 commit·commit 前 git diff --cached --name-only 坐实恰一枚·FX_COMMIT_DECLARE 挂 commit 命令侧·未 amend·未 --no-verify·撞 index.lock 无（未遇）。
