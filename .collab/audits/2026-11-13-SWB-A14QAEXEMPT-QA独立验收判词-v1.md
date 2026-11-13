# SWB-A14QAEXEMPT · 施工批 QA 独立验收判词 v1（qa-a14v1·fresh eyes 只读零施工·2026-11-13）

> **当轮开工实测（落笔前现跑）**：`date`＝`Fri Nov 13 19:01:25 2026`／`git rev-parse HEAD`＝`a2f19b7341961a8523ef0636523082dcff0d4998`（短 `a2f19b7`＝回执笔）。tracked 脏面＝百工包 ledger 一枚（他案在飞照登零碰）。
> **fresh eyes 声明**：本判词全部读数＝本席现跑现算（前像臂/后像臂/归档臂/探针臂/损坏臂/对抗臂各自独立构造），未复用工程师 scratch 取证面（`.scratch/SWB-A14QAEXEMPT/` 全程零读零拷）；回执读数仅作事后对拍对象。取证面＝`D:\multi-agent-collab-devkits\.scratch\SWB-A14QAEXEMPT-QA\`（不 commit）。

## 〇、对象与开工锚对拍（不符即停闸未触发）

- 被验收件＝票 `D:\multi-agent-collab-devkits\.scratch\tickets\2026-11-10-SWB-A14QAEXEMPT-a14-exempt-config-and-qa-exempt-ticket-v1.md`（v1＋修订笔 R1-R7·修订段优先）之施工批两笔：BUILD＝`3715cb7`＋RECEIPT＝`a2f19b7`；放行登记＝`D:\multi-agent-collab-devkits\.collab\decisions\2026-11-12-主理人放行登记-SWB-A14QAEXEMPT按票开工.md`（落链 `dd10e9c`·候①采甲转 WATCH 带历史豁免标记／候②采甲仅成文桶名闭集机检维持候补池）。
- 链段对拍：`git log --oneline 73179da..HEAD` 恰两笔（BUILD＋RECEIPT）✓；BUILD 面恰两件（A `share/baseline-pointer-exempt.json`＋M `share/check-pointers.py`）✓；RECEIPT 面恰一件（A `.collab/receipts/2026-11-13-SWB-A14QAEXEMPT-施工批回执-v1.md`）✓；HEAD＝`a2f19b7` ✓。
- 计数口径＝R6 写死 SEV 字段式 `grep -Ec '^[^:]+:[0-9]+: BLOCK '`；全部扫描现跑本席亲发。

## 一、V0 口径核对（R1 双栏归因是否如实）

- 前像臂（本席独立构造：`git show 73179da:share/check-pointers.py` 落 scratch 同盘跑＝改前口径无豁免层）：缺省扫描 SEV-BLOCK **18253**／WATCH **4581**／NOTE-FXU28 **2002**；旧 drill 字样 BLOCK 恰 **6** 枚（行号 30/23/66/174/200/194 逐枚全等＝票 §2.1 五文件集）；README `--target` 前像 BLOCK **8** 枚（L23/L25/L72/L84×2/L88×2/L92 逐枚全等＝R7 现跑钉）。→ 与回执 V0 读数**逐值全等**。
- 双栏归因独立复现：链笔栏 `git rev-list --count dd10e9c..73179da`＝**73 笔**／`git diff --name-only`＝**67 件**／其中 md＝**22 枚** → 与回执「73 笔／67 件／22 枚 md」**全等**；NOTE 起草窗 1988→现窗 2002（+14＝链笔栏＋盘态快照副本族）、GATE 昨窗 151285→今窗 151339（+54 落 collab-lint 栏 5876→5930＝本席今窗现数 **5930** 全等）＝两栏均可归因，「不归因即停」未触发 → **R1 双栏口径如实**。
- 归档对拍臂（R1 新增·本席独立跑）：`git archive 73179da` 解包 `--root` 独跑＝干净链面前像 BLOCK **2196**／drill BLOCK **6**；`git archive HEAD` 独跑＝后像 BLOCK **2190**／WATCH 1655／drill BLOCK **0**／历史豁免留痕 **6**。链面差恰 **−6**＝与裸盘面 18253→18247 互验自洽（裸盘大头系盘态噪声栏，归档臂隔离链面栏）。

## 二、V1-V7 逐条读数（全部本席现跑）

| 判据 | 本席实测 | 对回执 | 判 |
|---|---|---|---|
| V1-a 缺省面 | SEV-BLOCK 18253→**18247**（恰 −6）；`grep -F '2026-11-08-drill' \| grep -c ' BLOCK '` → **0** | 全等 | 绿 |
| V1-b README target 面 | BLOCK 前 8 → 后 **0**（exit 1 因 WATCH 发现行在册＝既有 exit 语义「findings 非空即 1」，非判据违例） | 全等 | 绿 |
| V2 留痕 | 缺省面 `grep -c '历史豁免'` → **6** 逐枚 WATCH 行在册（候①采甲式文案）；WATCH 4581→**4587**（恰 +6）；README 面 → **8**；**历史豁免行内 BLOCK 字样 grep → 0**（R6 写死文案兑现） | 全等 | 绿 |
| V3 探针臂 | drill token 从配置件**程序化读取**（非手抄）写入集合外探针件（`.scratch/SWB-A14QAEXEMPT-QA/qa-probe-outside-set.md`）`--target` → **exit 1** BLOCK 照拦（豁免键＝token＋文件集合语义兑现） | 全等 | 绿 |
| V3 损坏臂 | 按 R6 未动 share 真配置——脚本副本＋同目录同名**截断** JSON → **exit 4**（infra error 文案在册＝R2 `SystemExit(4)` 兑现）；真件复点 items **9** 条＋bucket **2** 行完好 | 全等 | 绿 |
| V4 史笔零改 | 施工链 `git diff --name-status 73179da..HEAD` 恰三件（A＋M＋A 回执）·**零 R 行**；§2.1 五文件 blob `73179da` vs `HEAD` 两态五枚 sha 全等（22eee49/42df8e3/3d9d04e/58b52f0/10b39d1），追加对放行锚 `dd10e9c` 三态亦全等；两包 qa tracked＝**60/2**（off＋NUL 双式）两桶整桶 `diff 73179da..HEAD` **空集**；禁动面九路（.gitignore／run-gates.sh／60-gates.md／baseline-sot-dup.json／object-audit tests／README.md／agent-experts/**／ticket-template.md／docs/）diff 全 **0** 行 | 全等 | 绿 |
| V5 门禁全链 | `bash share/run-gates.sh --no-write` → **GATE PASS exit 0** 发现 **151339**；check-pointers 子输出行量 **24836**＝本席前像/后像独立复跑两态行量全等（diff 面恰＝6 行 BLOCK→WATCH 替换·12 行 < >）；check-ticket-reconcile 现跑 **184**（全 WATCH）零变化 | 全等 | 绿 |
| V6 守件 | `python -m py_compile share/check-pointers.py` 绿；`check-pointer-closure.py --selftest` → **PASS exit 0**（OA-D6-3＝4／OA-D6-4＝1／EXEMPT＝2／SUBSTR＝4／VIOLATION＝4 全 MATCH＝O-3 夹具零翻面） | 全等 | 绿 |
| V7 靶检 | 票面 `--target` → **exit 0**；回执件 → **exit 0**；新建 JSON 件 → **exit 0** | 全等 | 绿 |

**V7 既存存量口径（独立复现坐实·非照抄）**：`--target share/check-pointers.py` 两枚 BLOCK（references／20-handoff.md 与 docs／INDEX.md 两串拆写防自咬）——本席前像臂（前像脚本跑前像件）同跑出恰同两枚，token 逐枚全等、行号 230/262（前像）→272/304（现态）仅随新增行偏移；两枚所在源行＝前像文件中既有注释/docstring 行，本笔 diff 新增行仅一行含反引号且为豁免 WATCH 格式串（`%s` 占位非路径 token）；该件不在缺省扫描域（缺省面涉该文件命中＝**0**）故从未入 GATE 基线 → **坐实系 HEAD 既存存量、非本笔引入**；不扩 items／不改既存注释行＝票面闭集与 §4.2 硬线兑现。

**S2 一处改动核验（只读实读 diff）**：＋57 行零删＝`import json`＋EXEMPT_SNAPSHOT 同目录 HERE 式＋`load_exempt`（缺失＝`{}` 无豁免更严不更松；损坏/形态不符＝`raise SystemExit(4)`）＋check_dangling 内 exempt 单次读取＋豁免层插入位＝FX-U28 后缀归位层之后、含斜杠悬空 BLOCK append 之前；裸基名 WATCH 层未接豁免（实读现态源文）；`collab_bucket_exempt` 段消费面＝脚本内 **0** 处引用（候②采甲「仅成文」兑现）。

## 三、对抗例（本席自造·四臂）

1. **改豁免配置一字→探针翻脸**：scratch 副本配置 token `.collab/defects/` 段改一字（defects→defectX）＋施工版脚本副本缺省扫描 → SEV-BLOCK 回升 **18253**、drill BLOCK 恢复 **6 枚**照拦、历史豁免留痕 **0**、WATCH 回 **4581**＝豁免键 token 敏感性绿。
2. **删一行 items→对应变体恢复 BLOCK**：scratch 副本删 README config／seat-permissions.json 一条（拆写）（items 9→8）→ README target 面该枚 BLOCK 恢复 **1** 枚照拦、其余豁免留痕 **7** 枚存续＝逐条独立生效绿。
3. **缺失臂（R6 合规替跑）**：脚本副本居无同名配置的 scratch 目录跑 README 面 → 无豁免、BLOCK 恢复 **8** 枚、留痕 0、exit 1＝「缺失＝无豁免更严不更松」兑现（全程未碰 share 真配置）。
4. **形态不符臂**：items 非列表 JSON → **exit 4**（infra error 文案）＝R2 闭集兑现。

## 四、S1 配置件本体核对

`share/baseline-pointer-exempt.json`：items **9** 条＝drill 1 条（token＝旧桶路径串连接值＋五文件集合与票 §2.1 五文件逐字全等）＋README 8 条（八异 token 与 R7 围栏逐 token 全等·各 {README.md}）；第二段 collab_bucket_exempt 两行照 §4.3 逐字；note 字段含「17 桶闭集只管仓根 .collab」随登口径。骨架字段与 §4.1 规格全等。

## 五、与工程师回执读数不一致处

**无。** 本席独立现跑全部 V0-V7 读数（18253/4581/2002/6/8→0/18247/4587/6+8/exit1+exit4/60-2/24836/151339/184/selftest 五账/三靶检 exit 0）与回执逐值全等；对抗臂与归档臂为本席新增取证，回执无对应读数可对比。

## 六、红黄绿计数与总判

- **红＝0**；**黄＝1**（口径随登级·非本批缺陷）：check-pointers.py 自身 target 面两枚既存存量 BLOCK（references／20-handoff.md 与 docs／INDEX.md 注释行字样·拆写）未消——本笔未引入（前像臂坐实）、票面闭集禁扩 items、§4.2 禁改既存行，本批正确零动作；存量挂账候补池或另票处置，不阻本批。
- **绿＝17**（开工锚对拍 1＋V0 口径 1＋V1-a/V1-b/V2/V3 探针/V3 损坏/V4/V5/V6/V7 各 1＋归档互验 1＋S2 一处改动核验 1＋S1 本体核对 1＋对抗臂 4）。

**总判＝IS_PASS。** 票 §五 V0-V7 全判据本席 fresh eyes 现跑全绿；两笔封顶、声明闭集、禁动面、fail-closed、候①②采甲兑现全部坐实。

（本判词旧桶字样／README 八 token／既存存量目标串全部拆写或入围栏防自咬；临时工作物＝`D:\multi-agent-collab-devkits\.scratch\SWB-A14QAEXEMPT-QA\` 票号族目录·不 commit·完工随工作面处置。）
