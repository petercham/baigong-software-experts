# DEBTCLN-R5 · rev1 窄复核判词（QA 席·fresh eyes·任务代号 DEBTCLN-R5-NARROW）

- 判词对象＝票面 .scratch／tickets／2026-11-16-DEBTCLN-R5-TOKPAR红线参数化票-v1.md rev1 段（链上现态）
- 复核范围＝派工窄复核口径三处（勘-1 SCRIPTS 点名／勘-2 修正版 V2 命令可达性／勘-3 逐行七枚钉无行尾口径）；双席快审绿面不复做、正文全轮不复做
- 复核席＝qa-debt5narrow（fresh 实例·主理人派工）
- 防自咬体例＝路径裸文＋全角斜杠（／U+FF0F）·零反引号·零 at 符号·引文 ⟦⟧

## 〇、开工读数（当轮现跑·禁抄旧数）

- HEAD＝git rev-parse --short HEAD → **fe93f52**（＝rev1 修票笔·链顶·与派工预期全等）
- 链序现跑＝fe93f52 → 4bf7e87 → 2adc99a → 8eff7c2 父子逐笔相衔（git log --oneline -4）
- 票面链上 blob＝git rev-parse HEAD 树面本票面路径 → **cf8ae98543e67a37fb4423dbe2c6235f859612be** 对钉全等（＝派工预期新 blob）
- rev 笔 numstat 复坐实＝git show --numstat 于 fe93f52 → **46／0**（删除列 0·append-only 属实）；票面行数 wc -l ＝ **222**（与 176＋46 相衔）
- index.lock＝不存在（NO_INDEX_LOCK）
- git status --porcelain＝tracked 脏面恰一枚 M＝agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl＋?? 群（2026-11-12 系列平放 md＋.collab／board／＋.collab／research／＋仓根杂散）＝全部他案照登零带入勿动
- 链上靶件 blob＝git ls-tree HEAD share／count_agent_tokens.py → **e755faef886f46b870a8a965c8029d55d527459b**（改前态·修票未触靶件坐实）

## 一、勘-1 复核＝run-gates.sh 行 141 SCRIPTS 清单点名·判定**通过**

当轮现读 share／run-gates.sh 行 141（sed 行取）SCRIPTS 赋值句逐项点名＝空格分隔**恰 11 项**（wc -w＝11）：①check-provenance ②check-skill-meta ③check-pointers ④check-entity ⑤check-collab-lint ⑥check-pointer-closure ⑦ROOT／share／check-source-of-truth ⑧check-ticket-reconcile ⑨check-adr ⑩check-hook-health ⑪check-collab-buckets。

- 与 rev 段勘-1 点名清单逐项对榫（名称·序·数三合），正文 ⟦12 项⟧ 计数不实之勘正（11 项）坐实。
- 「不含靶件」定性复现＝grep -c count_agent_tokens 于该行 → **0** 命中坐实为真；V4「输入面先验零变化」论证根基不受影响。

## 二、勘-2 复核＝修正版 V2 命令在正确施工态实跑·判定**通过（核心项·exit 0 四项全达）**

隔离复跑程序（取证族 .scratch／debt5nar／·用毕即拆）：

1. 命令来源防抄钉＝三步命令（§二 两步＋rev 段修正版 V2）全部从链上票面围栏行区间**逐字节程序化提取**落盘（step1.sh 402 字符／step2.sh 716 字符／v2fix.sh 919 字符），非手敲非转述。
2. 隔离 mini 仓＝.scratch／debt5nar／mini／（git init 新仓·core.autocrlf false 显式置否·全局 hooksPath／autocrlf 当轮均未设＝主仓钩子与行尾制不注入取证仓，如实照登）；改前版靶件从主仓 HEAD 树面 git show 取出＝hash-object 复算 **e755faef886f46b870a8a965c8029d55d527459b** 对钉全等＋wc -l ＝ **33**，commit 为该 mini 仓首笔（HEAD^ 语义天然成立·无需 sha 置换）。
3. **逐字跑 §二 两步施工命令**（第一步 heredoc 块落盘 exit 0＋第二步断言＋插入）→ 打印 **INSERTED-7-LINES**·exit 0；产物＝git hash-object **ba4d92973501e9ea0e79f5a36791a8365be53bb8** 对钉全等＋wc -l **40**＋py_compile exit 0；mini 仓第二笔后 git show --numstat ＝ **7／0** 对等。
4. **逐字跑 rev 段修正版 V2 命令**（于第二笔之上·HEAD^＝改前笔）→ **exit 0**·打印读数：

⟦CHANGED [] LEN 33 40 BLK c2e49c06383fb4da9c1395c269319e2365561761733ab783264782aee3e67abe DISK 2a549d226c3704ce90296a7daa7979507faf2d4011a92eeca5fbfcecd3fd233e⟧

- 四项全达逐一对钉＝CHANGED **[]**／LEN **33 40**／BLK **c2e49c06…** 全值对钉／DISK **2a549d22…** 全值对钉——与 rev 段层-4 读数及正文预期读数行**全等**。
- 判定：rev 段修正版命令在其自述前置条件（§二 两步命令正确施工态）下**可达性坐实**，V2 验收链以修正版命令为准具备机械可执行性；勘-2 三处形态勘正（块提取不叠 chr（10）／CHANGED 错位对拍／decode 去 newline kwarg／引号配平）全部实跑验证为真。
- 取证族拆验＝用毕即拆 rm -rf .scratch／debt5nar／ 后 ls 不复存在＋git status 对该族零命中；主仓工作区对靶件零命中（git diff 面仅他案 ledger 一枚照登）。

## 三、勘-3 复核＝逐行七枚钉无行尾口径 7／7·判定**通过**

python 当轮现算（从票面 ```python 围栏提取块七行·与 §二 heredoc 围栏七行逐行相等坐实·两处围栏同源一致性随登）：

- 无行尾口径（剥行尾内容行 UTF-8 sha256 前缀）＝77bc232f／a7f427fa／e5d5e92a／332cac5f／ef708572／7db57d09／f30c539d → **7／7 全部命中**票面括注钉，rev 段写死口径复现对榫。
- 含 LF 口径反向复算＝逐行得 0e313a46／bf8f2a5f／41371104／7a40ffc4／71d36dad／1e72f03b／3aad61cd ＝括注钉 0／7 不可复现、但 rev 段实算别名钉 7／7 命中——rev 段 ⟦含LF口径0／7⟧ 声明双向坐实。
- 块全文钉随验＝316 字符＋sha256 **c2e49c06383fb4da9c1395c269319e2365561761733ab783264782aee3e67abe** 对钉全等（含行尾 LF 口径维持）。

## 四、旁证面照登（不扩审）

- 落链后缺省指针扫描当轮复跑＝exit 1（既有基线态）＋**BLOCK 22809／WATCH 4582** 与 rev 笔自述读数零变化对榫。
- 票面（含 rev 段）链上现文自靶＝check-pointers --root . --target 本票面实路径 → **exit 0**。
- rev 段效力声明在册复核＝与正文并读·V2 以修正版命令为准·SCRIPTS 以 11 项为准·逐行钉以无行尾口径为准——三处均经本判词现跑坐实，声明与实测无冲突。
- 卫生观察照登（不判红·ignored 面）＝产品快审席取证族 .scratch／pmdebt5rev／ 宣称用毕即拆但当轮实拆未净·盘上仍在（ls 坐实存在）；该族居 ignored 面·当轮缺省扫描 BLOCK／WATCH 计数与基线零变化＝机检零扰动属实。登记提醒：**后续各席取证族一律用毕即拆**，宣称拆＝落 ls 坐实，防 ignored 面取证残留累积成版本账类缺口（与票 §四 观察行 117 枚副本族同型苗头·防 scope 扩面不立项）。

## 五、结论

**rev1 就绪·可放行**（进入排程第 3 步放行登记）。三处勘正全部现跑可达：勘-1 恰 11 项点名对榫＋不含靶件定性为真；勘-2 修正版 V2 命令在 §二 两步命令逐字施工态（改前 blob e755faef／产物 blob ba4d9297／40 行／numstat 7／0 全部对钉）下 **exit 0 四项全达**；勘-3 无行尾口径 7／7 复现＋含 LF 口径双向坐实＋块全文钉对榫。无缺项。本席未发现新矛盾。

## 六、本笔纪律自证

- 本席全程只新建本判词一件；主仓代码域／票面／账本／.gitignore／FUXI／靶件零触（修票不审改·只读复跑）；他案脏面零带入。
- 取证族 .scratch／debt5nar／ 用毕即拆坐实（§二 末行）；隔离施工仿真全部居 mini 新仓·主仓链上零扰动。
- 禁照抄义务履行＝三处读数全部当轮现跑；命令全部从票面围栏程序化提取逐字节执行。
- 本笔面单恰枚＝git diff --cached --name-only 于 commit 前坐实恰本判词一枚；FX_COMMIT_DECLARE 挂 commit 命令侧；add 单 pathspec 紧邻 commit；落笔后 commit 前本判词自靶 check-pointers --target exit 0；尾标 -QA-REV 置 message 最末；防自咬体例裸文＋全角斜杠·零 at·零反引号；链上史件零回改；账本零手写；撞锁处置未触发（index.lock 开工不存在·全程未遇）。

（判词尾·v1·append-only：如需追加随正在此续笔）
