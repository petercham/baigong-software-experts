# TOOLHOME v4 QA席独立验证判词 v1（fresh eyes·证伪导向·全判据本席独立实跑）

- 席位：qa-toolhomev（fresh eyes 独立实例）｜日期＝2026-11-10｜性质＝QA 席独立验证判词（票级验收结论面对 TOOLHOME v4 施工批）
- 被执行票面＝`.collab/drafts/2026-11-09-TOOLHOME票草案-v4.md`（落链笔 ccf6383）；放行裁定＝`.collab/decisions/2026-11-10-皮总裁定-工单规范三票全放行.md`（e12afd3）
- 工程师回执＝`.collab/receipts/2026-11-10-TOOLHOME-v4-工程师回执-v1.md`（对照用非判据）；工程师取证区（`.scratch` 下 TOOLHOME-eng-mvdef5 面）全程禁读——一切判据本席独立实跑，扫描/比对实现本席自写
- 总裁决：**红 0／黄 4／绿 8**（逐项三态见 §二；V4b「BLOCK 族零新增」子句＝呈裁未复·本席不裁）

## 〇、开工／完工读数（实测照登）

- 开工：date＝Tue Nov 10 05:24:23 2026；HEAD＝33339d73fdb3a5e3d4c191269719fb55551b26eb；`git status --porcelain --untracked-files=no`＝空（净）。
- 中途照登：取证期间共享索引出现他案 staged 一枚（fuxi 缺陷台账归因复盘件 M 态·FX-U29/TR29 线）——非本席触碰·本席判词笔 pathspec 限定零带入。
- 链上复核：`git merge-base --is-ancestor fbfbac0 HEAD` exit 0（开工锚在链）。fbfbac0..HEAD 区间共 16 笔：本票面笔＝b7e6ded／ddc1e23／fb6b594／33339d7 四笔＋内容落他案链笔 291ab44（笔4 内容）；其余 11 笔＝FX-U33 族他案照登。
- 独立取证面＝仓根 `.scratch/qa-toolhomev/`（worktree 五个：fbfbac0／ddc1e23／fb6b594／HEAD 两时点＋两基线＋装配两 out 居仓外同级临时区）——完工前删除，读数在本件在册。

## 一、对账（验证项1）

- 各笔 `git show --name-only -M` 与本席独立重建清单全等：
  - b7e6ded＝R100 七对（tools 七件）＋A 十一（share 新侧）＝18 迁入对；旧侧 object-audit scripts 十一枚 D 未随笔（违例一坐实·见 §七）。
  - ddc1e23＝M 十三面（pins:82／publish:137／share 十一件）＝锚 13 处落 12 文件＋truename/count 自述注释随动；与回执 §二 13 面清单全等。
  - fb6b594＝M 5（README、bundle-assembly 三件、70-charter）＋A 1（object-audit scripts 下 README 指针件）＋D 11（旧侧消解）＝17 面＝声明 17 面全等。
  - 291ab44＝bundle.lock＋fuxi 收口登记件＋publish.py 三面（TOOLHOME 内容两面＋FX-U33 收口面一件）。
  - 33339d7＝回执一件。
- 链外面零触碰：区间 40 面＝TOOLHOME 面 28 面（share 18A＋tools 7D＋object-audit scripts 11D＋scripts 下 README 1A＋消费随动 5M＋仓根 README 1M＋pins 1M＋publish 1M＋bundle.lock 1M＋receipt 1A，其中 publish/bundle.lock 经 291ab44）∪ FX-U33 面 12 面（contracts 两件／gates assert-tool＋catalog／fuxi tickets 2／receipts 3／qa 1／defects 1／TR29 随注 1）——两案面交集＝publish.py＋bundle.lock 两件，恰为笔4 卷入事故面（§七复勘），除此零交叠。
- 他案笔对 share/ 与 tools/ 两目录路径 `git log fbfbac0..HEAD -- share tools` 命中仅本票两笔（b7e6ded／ddc1e23）＝他案零触碰坐实。

## 二、逐项三态判定表

| 项 | 判 | 一句话依据（本席独立读数） |
|---|---|---|
| 对账（项1） | 绿 | 四笔＋291ab44 name-only 与申报清单全等；链外他案面照登分账 |
| V6 消解实态 | 绿 | `git ls-files tools/`＝0；`git ls-files share/`＝恰 18 件清单对票面迁入判定表全等；tools 目录盘上不存在 |
| V4 门禁现态 | 绿 | 现值 `share/run-gates.sh --no-write` exit 0 GATE PASS（发现 149525 条主盘口径）；裸跑自锚定位复现 exit 0 |
| V4b 两时点门禁臂 | 绿 | 时点1（ddc1e23 干净 worktree）exit 0 GATE PASS 6372；时点2（fb6b594）exit 0 GATE PASS 6437；钩子两行现读指 share 新径＋core.hooksPath 无值 |
| V4b「BLOCK 零新增」子句 | 黄（呈裁未复） | 本席同构干净盘口径复算＝+159／−0（工程师主盘口径 +852／−0）——两口径全部归因迁改旧径悬空族·零他因；子句裁点候皮总，本席不裁 |
| V1 封口＋锚清单 | 绿 | 四前缀样例两时点独立跑＝基线 94／收口 86；差集：消解恰 8＝迁改清单内件、豁免族外新增 0；谓词反查 13 处全在场、残留 tools 谓词代码面 0 命中 |
| V2 装配 | 绿 | HEAD 干净 worktree 两跑 exit 0（106 文件）／幂等零写入；挂载位 tools 恰 18＝声明数；改造前基线 worktree 独立跑 88 文件；非 tools 面 88 件逐件 sha 对拍全等（digest 不回归，manifest 两件内容差＝组件数 3→4 预期）；blob 对钉开工值全等（publish fab474be…／bundle.lock 3b59c236…） |
| V3 冒烟 | 绿（附形态呈报） | 四自检件料源 vs 挂载副本带 --root 两侧 exit 全等（0/0×4）；14 件无自检申报核对无缺项；挂载裸跑「未能定位仓根」形态复勘属实＝非改造引入（见黄-4） |
| V5 纯净性 | 绿 | 各笔写集 ⊆ 票面六列举闭集；五笔 message 零 at 符号字符实测（grep 计数 0×5）；他案面零带入 |
| 笔4 卷入面纯净性 | 绿 | 291ab44 内 publish.py S2 断言六行＋bundle.lock devkit-tools 组件行 11 行纯插入＝TOOLHOME S2 闭集对位；publish fbfbac0..HEAD 全量 diff＝锚一行＋S2 断言六行两处，零他逻辑；291ab44 两 blob 与 HEAD 终值全等；tag devkit-tools@v0.1.0 → 291ab447 ls-tree share 恰 18 |
| 违例两件复勘（项7） | 绿（账实相符） | 见 §七 |
| 交付物纯净性（项8） | 绿 | share 18 件零过程件指针（py 内 scratch 字样＝扫描面排除逻辑注释非指针）；scripts 下 README 指针件＋回执件 check-pointers 靶检各 exit 0 |
| 迁入零改（S4 承账） | 黄-1 附注 | 18 对中 17 对 b7e6ded 落链 blob 与开工旧 blob 全等；run-gates.sh 例外＝SCRIPTS 取源两行已在笔1 改 share——与笔1 message 自述「本笔 staged 零内容改」不符（见黄-1） |
| S2 内容差面核 | 绿 | 工具代码逻辑零改动逐行实核：share 侧内容差全部＝锚谓词一行／docstring／help 文案／注释字样随迁（check-skill-meta 5 行、check-source-of-truth 9 行、truename/count 各 1 行），无逻辑臂改动 |
| 专属族留包 | 绿 | fuxi gates 受跟踪 8 件全在场（六 py＋两 catalog）；publish.py 本体留 object-build；区间内该面触碰仅 FX-U33 射程（assert-tool/catalog）＋本票 pins 锚一行 |

## 三、V1 独立读数明细

- 命令＝`git grep -l -E "tools/(check-|baseline-|count_agent_tokens|sot-external)" -- ":!.scratch"` 分别对 fbfbac0 与 HEAD 两引用跑：94／86 件。
- 基线−收口＝恰 8 件＝bundle-assembly 三件＋70-charter＋object-audit scripts 下 run-gates＋tools 三 py（迁改清单内件全消解）。
- 收口−基线＝空（豁免族外零新增）。收口 86 桶分布＝包内 .collab 68＋仓根 .collab 13＋包内 .scratch/tickets 4＋90-changelog 1＝86；档位一票面族（草案 v3／v4 窄复核 QA 判词等）在 86 内实点命中在册。

## 四、V4 发现数差值独立归因（票面口径＝逐条归因禁糊账）

- 本席同构口径（基线/现值两干净 worktree 各自工具跑）：GATE PASS 发现数 基线 6274（旧侧 tools 链）→ 现值 6437，差值 +163。
- 逐检查器对表：check-pointers 缺省扫面 BLOCK 行 1823→1982（+159）；check-ticket-reconcile 发现 143→145（+2，票 133 不变·全 WATCH·链上票面波动）；check-collab-lint SUBSTR 9→10（+1）；其余（entity／provenance／skill-meta／adr／pointer-closure／sot）零变化。合计 +162 已归因＋口径尾差 1（collab-lint 分账行呈现截断）。
- 工程师主盘口径（+1127＝pointers+877／collab-lint+250／reconcile+3）＝主盘含未跟踪包内 scratch 副本面（本席主盘同跑＝149525 条同量级印证），方向与本席归因一致：全部＝迁改名路径字样命中增减。判：口径可复算、归因方向属实。

## 五、V4b「BLOCK 族零新增」子句独立复算（关键·呈裁面）

- 同构干净盘两时点行级差集（归一化去行号）：**+159／−0**。工程师申报（主盘脏面口径）+852／−0——两口径结论同型：该子句在缺省扫面全量史账命中口径下机械不可达，坐实。
- 本席 159 独立归因分类计数：tools 旧径悬空 88／object-audit scripts 全旧径悬空 57／裸 scripts 相对径悬空 7／object-audit scripts 简写旧径 7＝159 全闭合。
- 零他因混入核验：159 行所在文件集 ∩ 区间内被新增文件集＝空；∩ 区间内被修改文件集＝空——新增全部落在他案未触碰的史账判定件上，唯一致因＝料源迁改致旧径字样悬空（S4 禁回改＋迁册必致）。工程师四类归因（610/196/42/4）与四类同族·本席读数为其干净盘子集，**「无他因混入」申报属实**。
- 三态如实＝该子句裁点候皮总（甲＝差值归因放行／乙＝豁免机制另票／丙），本席未裁。

## 六、V2/V6/tag/blob 钉读数

- blob 对钉开工现读：publish.py（fbfbac0 值）＝fab474be2d1509841f6bd56d64fa900b93bfa3e6；bundle.lock（fbfbac0 值）＝3b59c23674cbbcf9675a4d9addd6122fb2d0ee31——与票面④全等。
- V2 改造前基线（fbfbac0 干净 worktree 实跑）＝88 文件 exit 0；改造后（HEAD 干净 worktree）run1 exit 0「106 文件 bundle@33339d7」／run2「装配面已一致·零写入」；106−88＝18＝share 组件挂载数＝声明数；挂载 18 件与 share 料源逐件 sha 256 全等（HIT 18/18）。
- 既有组件不回归：改造前后两 out 的非 tools 面 88 件逐件 sha 对拍全等（ASSEMBLY.manifest.json／COPY.state 两件内容差＝组件行 3→4 账本随动，非组件文件回归）。
- tag＝devkit-tools@v0.1.0 rev-list → 291ab447d7c07933282f56c92c2abbcdca6664d6；`git ls-tree -r` 该 tag share 恰 18 件；tag 名 message 拆写零 at。

## 七、违例两件复勘（工程师如实入账·本席核账实相符）

1. **笔1 pathspec 缺旧侧致 11 枚 D 滞留**：坐实（b7e6ded name-only 无旧侧 D；`git ls-tree` 对 b7e6ded..fb6b594 全部十三链上笔核旧侧受跟踪计数恒 11＝滞留窗口史实）。**零实害核验**：滞留窗口内旧侧树面完整可用——本席在 ddc1e23 时点以旧侧 object-audit scripts 下脚本直跑 check-pointers 正常出读数（exit 0 扫描成功形态）；新侧 share 链同时全绿（时点1 GATE PASS）。双存过渡＝功能无害；违例＝账实相符·窗口零实害坐实。
2. **笔4 撞 ref lock 内容入他案笔（D-58 案型）**：坐实——291ab44（parent 恰 fb6b594）含 publish.py＋bundle.lock 两面；publish.py 该处 diff＝S2 断言六行（与票面 S2 闭集对位）；bundle.lock＝devkit-tools 组件行 11 行纯插入（material=share 形态＋path=share＋target=tools 挂载语义）；两 blob 至 HEAD 零再改（全等）。TOOLHOME-4 独立标记全链 grep 零命中＝提交失败申报与链上缺失互证。FX-U33 收口面（登记回执件）与本票两面零内容交叠。账实相符。
3. bypass 旁路核查（本席加验臂）：全链证据件 `"bypass": true` 共 11 枚全部为 2026-10-23 存量（首批门禁自证期），本票窗口零 bypass 记录＝无静默绕闸。

## 八、黄项四条（如实·禁假绿）

- **黄-1（账实不符微项）**：笔1 message 自述「run-gates:141 SCRIPTS 取源一行＝锚面居笔2射程本笔 staged 零内容改（worktree 注改系笔2预置未 staged 如实注）」——blob 实测相反：b7e6ded 落链 share 侧 run-gates.sh 已含 SCRIPTS 行与例注释行改 share 终值（diff 开工旧 blob＝该两行）。功能无害（笔1 时点 share 取源已在场，链全绿），但该行为属笔2 射程内容提前入笔1 落链，且笔1 自查注记与 blob 实况不符＝申报精度缺陷。
- **黄-2（呈裁未复）**：V4b「BLOCK 族零新增」子句机械不可达（本席 +159／−0 独立复算全归因迁改悬空族），裁点候皮总，本席不裁（票面候裁路径回流在册）。
- **黄-3（迁序程序微偏）**：票面 S1 迁序写死「后消解 tools 空目录（单独一笔）」——实测 tools 盘上目录消解发生在笔3（fb6b594）窗口内（其 message 自述「tools 盘上目录已消」），无独立消解笔。受跟踪面 tools 已于笔1 R100 清空＋盘上空目录不入 commit＝该「单独一笔」要求对受跟踪面无可承载物，但票面字面与笔次形态不符，如实登记（另：链上亦无 tools 盘上消解时刻的独立可证读数，消解前各时点盘上存在性不可回溯实证）。
- **黄-4（形态呈报非违例）**：挂载副本裸跑（不带 --root）四自检件均「未能定位仓根」usage error——复勘属实＝挂载包根无三分类目录致 share 锚谓词不成立；基线旧工具于其原生树裸跑则自锚成立。该形态差异非本票改造引入（锚谓词三分类合取＝S3-A 定案②既有形制），票面 V3「exit 与料源版一致」在 --root 法下成立；「挂载后包内调用一律包内相对路径」口径下无实害，如实登记候主理人知悉。

## 九、锚谓词反查独立读数（e12afd3 写死口径·本席自写反查）

- share 锚谓词形态（isdir/join share／-d share／SCRIPTS ROOT/share）受跟踪面命中恰 13 处逐一点名：check-collab-lint.py:132／check-entity.py:146／check-pointer-closure.py:93／check-pointers.py:121 与 :442／check-provenance.py:99／check-skill-meta.py:72 与 :79／check-staged-declaration.py:69／check-source-of-truth.py:754（自锚·单引号形制）／run-gates.sh:81 与 :141／fuxi gates check-ticket-pins.py:82／object-build publish.py:137＝13（票面十二处＋自锚一处，口径全等）。
- 残留反查：`isdir(…"tools")`／`-d "…tools"` 形态于 share＋gates＋publish＋agent-experts 受跟踪代码面＝仅史账调研件／票面引文命中（豁免族），活动代码面 0 命中。

## 十、落笔纪律自查（本席判词笔）

- 临时复测物居仓根 `.scratch/qa-toolhomev/`（worktree 五＋比对清单）＋仓外同级装配 out 临时区——完工前删除附读数（本件落笔后执行·删除读数随回报）。
- 判词笔＝FX_COMMIT_DECLARE 声明恰本件一件；pathspec 限定 add 与 commit 紧邻无窗口；禁 add -A；禁 amend／--no-verify；message 零 at 符号字符。
- 落笔前靶检＝check-pointers --target 本件 exit 0（读数随回报）。
- 判词归签字席口径：本件＝QA 席验收结论面（票级），终局收口登记归主理人；V4b 子句候裁面归皮总。

〔回流四型＝完成型·TOOLHOME-QA·红0黄4绿8·V4b呈裁未复〕
