# SWB-GTFAST QA 票级验收判词－v1

> 验收席＝qa-swb-gtfast-acc（fresh eyes 单席）｜日期＝2026-11-19｜受理依据＝票面 v2（.scratch/tickets/2026-11-18-SWB-GTFAST-闸提交门靶检与周期全量与钩子动态根扫描域划界-v2.md 盘上 blob f403bcf7f8558395f34e29b0b273ae841dd16d74 现算对表全等）＋H-0 裁定（decisions 桶 10e518c2 笔＝判据一改相对口径）＋放行链（aa0a3aec／af5f7a3a）＋施工链（R0＝3fea556f＋64cf4c89；续施＝d93cc863＋17f26c6d）。
> 本判词全部结论当轮现跑现读，工程师取证族仅作互证参照；本席全程零 git 写（add／commit／amend／stash 零笔），只读 git 命令照用；取证族落 .scratch/SWB-GTFAST-acc-qa/。

## 一、开工三读数照登（当轮现跑）

- HEAD＝17f26c6df343fad7e69d618402571db6dc7dd94a＝main 现读（链顶对回执笔全等）。
- 脏面＝M 一枚＝.collab/board/2026-11-17-五份复盘合流与下一轮迭代计划-v2.md（他案在飞·照登零碰零 reset）＋?? 散件群照登零带入。
- 锁面＝NO-INDEX-LOCK 现读（.git/index.lock 不在盘）；验收全程未撞锁、未写锁。
- worktree 五条照登＝主根挂 main＋qa_t10_dy（detached·prunable）＋D:/cs1-wt（detached）＋baigong-software-team 挂 baigong-software/main＋fuxi-skill 挂 fuxi/main。

## 二、逐判据红黄绿表（八条＋H-0 修正口径）

| 判据 | 读数（现跑） | 判 |
|---|---|---|
| ① 提交门计时（H-0 相对口径） | 循环段合计 9.259s（逐枚 provenance 166ms／skill-meta 166／pointers 4272／entity 367／lint 173／closure 279／csot 368／ticket-reconcile 2263／adr 274／hook-health 215／buckets 166）＝对工程师 8.9s 同档达标；端到端两读 284.4s／289.6s 照登＝差额归因裁决段全桶读（复核＝端到端减循环段约 275s 对工程师 py-end 285.8s 吻合）＝票外缺口不作红判（承 10e518c2 裁定四之判据一相对口径；SWB-GTBLOAT 另票射程） | 绿 |
| ② 取径不更判据 | 空暂存 exit 0 打印 GATE PASS（--staged 暂存面为空）；--target 目录两枚各 exit 2（lint／closure 措辞各承先例）；真阳性靶两枚 exit 1（lint 靶 .scratch/tickets/2026-11-06-SRC4Z-four-zone-write-permissions-ticket.md 发现 5 行＝缺省全扫属该文件 5 行逐行全等；closure 靶 agent-experts/baigong-software-team/.collab/README.md 发现 5 行＝全扫 5 行逐行全等）；零发现靶两枚 exit 0 零发现汇总；子集方向单侧违例两枚均 0；七枚零改动件（csot／ticket-reconcile／staged-declaration／provenance／skill-meta／adr／buckets）ls-tree 两态 blob 全等＝缺省输出等值由代码零字节坐实 | 绿 |
| ③ 全量移位周期闸可对账 | check-entity 单枚 exit 0（注入与缺省两口径）＋A/B＝起点副本 1f4be322 exit 1 恰一枚 OA-T1 BLOCK（.workbuddy/memory/2026-11-18.md:34 count=8）对改后 exit 0＝假阳性归零；全套缺省模式 --no-write 不带 ALLOW_GATE_DOWN＝GATE PASS exit 0 首次自然绿复现；FINDING_RE 口径现算总 27,051（pointers 22,806＋closure 3,754＋csot 467＋ticket-reconcile 10＋lint 14＋entity 0）对 R0 后基面 27,052 差集恰 1＝OA-T1 族归零项余零差；全套 real 396.9s 对工程师 394.8s 同档（IO 波动族） | 绿 |
| ④ 钩子钉随正 | .git/hooks/pre-commit 现算 git hash-object＝02d30d01e53f9c7b38803dfbd1d599f9a23c4d16 对钉全等；check-hook-health.py L47 现读 EXPECTED_HOOK_BLOB＝新钉（恰一行行内置换＝改动笔 diff 减一加一核见）；hook-health 现跑 exit 0＝snapshot hook-blob 对新钉在场；install-hooks 幂等复跑 exit 0「已是最新」且复跑后 hash 不变 | 绿 |
| ⑤ worktree 侧零触主根 | 旗两态同值＝主根与 D:/cs1-wt 各现读 D:/multi-agent-collab-devkits/.git/hooks（共享 common dir 坐实）；临时 detached worktree（建验拆）内 --show-toplevel 落该工作区根＝动态根解析命中；钩子裸跑 GATE PASS exit 0（该工作区暂存面空＝--staged 空靶路径）；主根 .collab/evidence/gates 计数 12,825 前后两读零增＝工作区侧不写主根桶；worktree remove 后 list 复五条＝ANCHOR 照登数 | 绿 |
| ⑥ 绕行归零（Y5 快照口径） | 收口点桶快照现跑＝12,825 枚（验收全程 --no-write 不写桶＝收口复读仍 12,825）；H-0 裁定笔 10e518c2（03:48:10）起新增桶件 9 枚、bypass grep 命中 0＝裁定笔起零新增留痕（全桶 bypass 存量 250 枚系裁定前留痕存量随注不归本票）；OA-T1 归零旁证见判据③ | 绿 |
| ⑦ fail-closed 与闭集 | --staged 指非工作区 exit 4 文案命中（infra error: --staged 需工作区）；PATH 剥离 git 不可用场景 exit 4（脚本层 die_infra 分支命中，dirname 缺位报错＝环境层噪音并登）；--target 目录 exit 2 两枚；缺省模式损坏路由表（假树 json 围栏在位缺必填键）exit 4「路由表缺必填键」复现；ALLOW_GATE_DOWN 留痕语义不变＝裁决段 PY 段逐字节零动坐实（见判据⑧）＝留痕写盘语义零扰动旁证；真桶不跑 bypass 例（取证纪律）＝以裁决段零动口径兑现 | 绿 |
| ⑧ 链面闭集 | 开工 ANCHOR 78627f36..HEAD 的 share/ 域 diff 恰七枚＝声明面（run-gates／entity／lint／closure／pointers／install-hooks／hook-health）；起点七枚对 ANCHOR ls-tree 全等（11a6f4d4／1f4be322／d963f5a2／717a2adf／33781b31／f71474ac／7fd83074）；改后七枚 blob 对回执面单全等（c2918140／bd694fe5／ed518bb9／52623ef6／d5e2cfe2／ad14f0d1／1df6ea44）；禁动面点名十枚两态 ls-tree 全等（60-gates.md b68cbfc7／两基线 json 2c44d339 与 f6171c7d／csot d7c261bf／ticket-reconcile 5c58d7de／staged-declaration 04f2889f／provenance 4de9fa63／skill-meta a100bdad／adr f71442d8／buckets 922fe2e9）；run-gates PY 裁决段归一零动＝起点 L157-543 对现值 L211-597 各 387 行 CR 归一后 diff 零行；三包域 diff 空集＋链上 workbuddy 域 diff 空集；append-only＝票面 v2／rev 回执／rev 窄复核判词链上各恰一笔＋起草回执／QA 审票判词／产品审票判词链前单笔＝零回改；票面 v1 件盘上保留作史 | 绿 |

## 三、S1-a／S1-b 划界实效（判据七读数）

- lint 改后单枚现跑 exit 1／real 0.516s＝亚秒级达标；入扫 645 枚（构成分解＝根 .collab 341＋tickets 子树 65＋其余存续面 239）；发现 14 枚（EAC-L2 全部）对工程师 R0 与续施两份基面逐行集合对拍全等（mine-eng 0／eng-mine 0）。
- A/B＝起点 d963f5a2 副本同轮现跑 real 118.1s／发现 6,353 行（EAC-L1 2,091＋L2 4,262）＝对 R0 回执 155.9s／6,353 行读数族同档（IO 波动不追因）＝入扫与耗时降幅复核成立。
- .workbuddy 整词剪枝四脚本改动点在位现读行位＝check-entity.py L177（五项）／check-collab-lint.py L164（整词任何深度）／check-pointer-closure.py L127（三项）／check-pointers.py L335（扫描域 walk 三项）。
- check-pointers.py L238 基名索引面未随划界（起点与现值该段逐行对拍全等）＝候裁 C-1 未裁零动兑现。
- S1-b 现盘行为差＝零：closure 起点副本对改后全扫发现行差集双向 0（3,754 对 3,754）；pointers 起点副本对改后全扫 22,806 对 22,806 零差＝.workbuddy 现盘扫描面零命中（工程师登记口径复核一致＝基线 log 族系文本提及形态）。

## 四、对抗臂读数（三枚＋）

- 臂一 钩子钉活性：对票面 S4-a 围栏八行逐字节重建＋末换行追加＝hash 现算 02d30d01e53f9c7b38803dfbd1d599f9a23c4d16 对钉全等且与盘上钩子件字节全等；GATE_ROOT_DIR 行逐行审＝定位落空即 printf 报错 exit 4 fail-closed，非工作区裸跑现跑 exit 4 文案命中；篡改一字符臂＝独立 git init 假树内现算 d77bd3c6 必触 hook-health BLOCK exit 1（登记：假树未 git init 时 hook-health 经 git -C 向上解析落回真仓钩子＝既有定位语义非本票改动面，登记不判红）。
- 臂二 缺省模式语义回归：SCRIPTS 十一枚清单存续（L167 现读逐枚在列）；不带 --staged 时 targs 恒空、调用行逐字＝改前原行（diff 审见插段全部处 STAGED 判定内）；--no-write 语义段与裁决段零动（判据⑧归一 diff 零行）＝缺省路径行为零变坐实。
- 臂三 C-1／C-2 未裁面零动坐实：check-pointers.py 改动 diff 仅 L334-335 一处注释加行＋剪枝行，不含 L238 索引段；60-gates.md blob b68cbfc7 两态全等＝路由表 json 围栏零动。
- 补臂 自靶七枚合靶复现：改后现跑 exit 1 恰四枚 WATCH 对起点件同靶恰同四枚＝零新增 WATCH／BLOCK 零（check-collab-lint.py 头注示例字面存量形态＝工程师申报口径复核全等）。

## 五、回执忠实性（工程师续施回执＋R0 回执关键读数对拍）

| 回执读数 | QA 现跑值 | 对拍 |
|---|---|---|
| entity OA-T1 归零 exit 0 | exit 0（两口径）＋A/B 起点 exit 1 恰一枚 | 全等 |
| 缺省全套闸 GATE PASS exit 0 | exit 0 GATE PASS | 全等 |
| 总 27,051 对 R0 基面差集恰 1 | 27,051；逐脚本差集全 0；entity 0 对 1＝差 1 | 全等 |
| 缺省 real 394.8s | 396.9s | 同档 |
| --staged 三次 294.2／304.6／296.3s | 端到端 284.4／289.6s | 同族（IO 波动） |
| 循环段 8.9s | 9.259s | 同档 |
| 钩子 02d30d01／hook-health exit 0／裸跑 exit 4 文案／幂等 exit 0 | 全数复现 | 全等 |
| lint 改后 0.889s 入扫 668 发现 14 | 0.516s 入扫 645 发现 14 | 发现全等；入扫差 23 见黄项 Y-N1 |
| closure 起点 9,115ms diff 空集 | 8,881ms 差集双向 0 | 全等 |
| pointers 起点 diff 空集 | 22,806 对 22,806 零差 | 全等 |
| 旗两态同值 | 主根与 cs1-wt 各现读全等 | 全等 |
| 禁动面十枚对开工点全等 | 两态 ls-tree 逐枚全等 | 全等 |

## 六、黄项如实（登记不归红）

- Y-N1 lint 入扫枚数 645 对 R0 回执 668＝盘上自然漂移（根 .collab 341 对 335＝＋6 系链上落笔新增；其余存续面 239 对 268＝-29 系取证散件与 ?? 群面变动；tickets 子树 65 对 65 全等）；发现 14 枚逐行全等＝判据面零行为差，归因照登。
- Y-N2 提交门端到端仍 284-296s＝H-0 相对口径不作红判；归因复核坐实＝循环段外差额约 275s 对工程师 py-end 285.8s 吻合＝裁决段全桶读 12,825 枚＝SWB-GTBLOAT 另票射程照登（本票禁动面零动维持）。
- Y-N3 钩子裸跑环境形制差＝带 MSYS 路径转换禁用旗时 exit 4（环境层 git 定位落空），缺省环境 exit 0 正常走完空靶路径＝两态 fail-closed 语义皆正确，登记不判红。
- Y-N4 S1-b 三枚（closure／pointers／lint 叠加面）现盘划界零行为差＝现盘扫描面 .workbuddy 零命中；物理划界在位系防未来咬闸的射程面，实效以对账口径登记（与工程师登记一致）。
- Y-N5 check-ticket-reconcile 汇总行「发现 184」与 FINDING_RE 现算 10 并存＝该件汇总行含对账行形态两口径并存，承票面先例口径登记不追因。

## 七、总判

**可收口。** 八判据（含 H-0 裁定相对口径修正）全绿：提交门循环段 9.259s 达标＋靶检对账子集违例零＋OA-T1 假阳性归零＋全套闸自然绿 GATE PASS exit 0＋钉随正链全过＋worktree 侧零触主根＋绕行归零（裁定笔起 bypass 零新增）＋链面闭集与 append-only 零违例；对抗臂三枚补一枚全过；回执忠实性逐项对拍全等或同档。红旗清单＝空。黄项五枚均系盘上漂移归因、口径并存或另票射程照登，无一触票面 H-0 触发条件。S3 零代码兑现＝缺省模式即周期执行体现形态在册。候裁 C-1／C-2 未裁零动坐实。

（判词完——SWB-GTFAST 票级独立验收＝可收口；投递归主理人。）
