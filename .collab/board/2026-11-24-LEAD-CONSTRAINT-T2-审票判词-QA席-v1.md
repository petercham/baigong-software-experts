# SWB-LC-T2 · LEAD-CONSTRAINT 案②逃生门上锁 · 审票判词 · QA 席 v1

- 审席＝QA 席（fresh eyes＝三票单席一次审；全部取证本席当轮现跑＋现场构造样件族＝非同构防共盲）
- 审对象＝.collab／board／2026-11-24-LEAD-CONSTRAINT-T2-施工票-v1.md（本席现跑两式＝208 行／git hash-object 现算 31275080a51912fe133d9accd67017106e55fbf3＝链上 HEAD blob 现读全等＝链上笔 f050a46b 本体＝与派工预期 208 行全等）
- 审窗读数（本席现跑）＝链顶 f050a46b＋date 17:1x＋NO_INDEX_LOCK＋tracked 脏面 0 枚
- 只读自证＝零 git 写；令牌样件＝内存构造不落仓内可提交面；台账探针全部重定向 .scratch／QA-REV-LEAD-CONSTRAINT／＝真账终核＝外层 7＋内层 8＋leases 7 零染自证

## 判据一 · 票型面三闸独立复跑归零 —— 绿

check-ticket／preflight-ticket／check-pointers --target 票面 本席现跑＝三闸各 BLOCK 0／WATCH 0 exit 0＝互证成立。

## 判据二 · §二 取证读数复跑 —— 绿

    绕过锚现跑＝check-staged-declaration.py 行 149 bypass 赋值行命中＋run-gates.sh 行 37／66／167／528 四处命中＝插验签调用点坐实锚复现（另随登＝行 193 GATE_BYPASS 读入点＋行 480—482 证据件 bypass 键写入段＝S1 修二「行 481 锚」精确命中）
    R-7 四组现跑刷新＝2760／2629／334＋四枚存量债闸命中 334／334＝对票面 2754／2623／333 活体增量照登成立
    「签字」类现状现跑＝仓根 ledger grep 签字 计数 0＝开工基线面在场；RECORD_TYPES 六类两处字面副本现读＝reconcile-daily 行 19＋intake-register 行 25 逐字全等＝「字段级扩展不扩枚举」前提约束在册复现
    旁路零覆盖精确口径引文＝⟦零覆盖面对「旁路＋票 ID 形态」；旁路无票撞 orphan 顺带拦＝非对旁路本身⟧＝本席 v1 审票判词绿二补证面逐字对位（同日 LEAD-CONSTRAINT-审票判词-QA席-v1.md 行 70／112 现读在册）＝口径承接真实
    三台账开工拍 7／8＋7＋链序＋四词各 0 预核＝复现

## 判据三 · V 系可机械执行性 —— 绿（六臂具名可跑）＋黄（标注态输出形制未钉）

V2 完备性臂现跑＝四修锚 grep -c '^    修'＝4 命中／探针六臂计数＝6 命中＝复现。

独立构造用例①＝非同构令牌样件族（内存构造＝夹具密钥 HMAC-SHA256 族≠实现件拟用非对称私钥＝故意非同构防共盲）＝五出口互异可判直证：有效形→绿通过；同码二次→红复用；过期形→红过期；超范围形→红范围；伪造签名形→红验签失败＝「四形（有效／过期／复用／超范围）＋无证」判据族＝每形出口可归因具名＝机械可判性坐实＝判据可判。

独立构造用例②＝配对核三形样例台账（--ledger 重定向＋--leases／--states／--repo-root 三锚＝scratch 域三枚样例＝齐形／缺签字形／缺 commit 形）＝本席现跑：现版 reconcile-daily 对三形 diff 读数恒 0（三形互不可分）＝配对核臂＝S5 新增臂＝现状不可分恰证该臂为必要新增＝样件族已备好＝可验收。

黄-1＝「标注态逐一对位」期望值输出形制未钉＝现版对账输出键面（counts_by_type／diff／diff_items）现读在场，但 S5 新增臂的标注态字段名／落位件（呈报类载荷 vs 读数行）票面未具名＝验收「逐一对位」需放行段钉一行输出形制（否则填读归一靠裁量＝违「不得现场裁量」）。

黄-2＝S3 消费入账通道未具名＝「入账归既有账本机件通道」现检索＝写「签字」类记录既有实体＝state-transition.py／sign-verify.py（六节点签字面）＝均非令牌消费通道；S3 本体申明「只读零写」＝消费入账主体（S1 与 S2 调用侧内嵌 vs 新小机件）票内未闭环＝一行钉主体（防「零写申明」与「入账动作」自相抵）。

## 判据四 · 声明判据五枚可构造性核 —— 绿＋黄（同黄-1 根）

五判据（有效正臂／无证降闸臂／同码复用臂／过期超范围两枚／配对三形臂）逐一对位构造面：前四枚＝本席样件族直证可构造可判；第五枚＝三形样件已构造、判据对位待 S5 输出形制钉死（黄-1 同根＝不重复计）＝可执行面绿、判据面一黄。

## 判据五 · 租约段互斥性＋写域案型（J-2 表态＋share 面缺口）—— 红

互斥面绿＝三票 path 两两交集空（T2∩T1＝∅／T2∩T4＝∅）；T2 path 命中 T1 deny 三枚（run-gates／check-staged-declaration／reconcile 装配族）＋T1 path 命中 T2 deny（.github／**）＝双向互斥坐实；本票 path∩deny＝∅；deny_globs 含 60-gates.md／intake-register.py 精让枚＝与 §三 禁动枚举对位。

红-1＝share 面四枚（S1 run-gates／S2 check-staged-declaration／S3 gate-token-verify／S4 gate-token-issue）写域随动无案型槽＋「先例在册」台账不可证：

    config 席位行现读＝engineer write_globs 无 share／ 行；host／human 席位行亦无 share／＝share 面＝现配写域空洞；lease-issuer 探针＝share／run-gates.sh／share／gate-token-verify.py 具名对 engineer exit 2 REJECT（实测直证甲态不可行）
    J-2 只覆盖 S5（skills／sop／scripts／ 一枚）＝S1—S4 share 面票内无同款候裁位；「share／ 域写先例在册（FX-U34／BKTCLS／PF 族）」＝leases.jsonl 两份台账全检零 share／ 条目＝先例＝链上笔有、租约台账无＝不可直证
    后果＝工程师当窗四枚必撞拒＝开工即停手＝与同日 T4 判词红-3 同根案型（T4 全写集无槽／T2 S1—S4 无槽＝同根不并档各票自计）

J-2 技术侧表态（工单第 6 项）＝skills／sop／scripts／ 面＝engineer 席位行 write_globs 不含该径（config 现读直证）＋探针 reconcile-daily.py 具名 exit 2 REJECT＝甲态实测拒＝票面预设「甲先行实测拒转乙随呈」恰落预设去路＝程序自洽＝该枚绿；与 T1 J-1 同案型＝席位扩行归 C1 通道两级注随呈＝QA 无异议；附请＝三票 share／.github／skills-sop 三面扩行宜并一案随呈（同 config 文件同面＝分批三签＝YAGNI 观察一行）。

## 总判

- 计数＝红 1／黄 2／绿 4（绿＝三闸归零·§二 读数全复现·令牌四形＋无证五出口独立构造可判·互斥面坐实）。
- 红-1＝share 面四枚写域随动无槽＋先例申报台账不可证＝rev 补 J 槽（S1—S4 同款三形态）＋先例归因改如实。
- 黄-1 配对核标注态输出形制钉一行；黄-2 S3 消费入账主体钉一行。
- 总判＝不可现态放行＝rev-1 后最狭窄复核＝本席红臂复跑（share 面 lease 探针复跑＋J 槽在位核）＋配对臂输出形制对表即可，无需全轮复审。
- 席位纪律随登＝令牌样件内存构造用毕即散；探针台账族落 .scratch／QA-REV-LEAD-CONSTRAINT／用毕即拆随完工回报；真账零染终核在册（7／8＋7 全等基线）。

## 复审-1 续段（rev-1 转绿臂·QA 席机检臂单席一次跑·append-only 追加＝v1 判词段零回改）

- 复审窗读数（本席现跑）＝链顶 e5110637＋date 17:5x＋NO_INDEX_LOCK＋tracked 脏面 0 枚；本票 rev 面两式现跑全等＝237 行／6bfdafc36e419ce0b61525cf5733c9bb1dd4750e（链面＝盘现＝派工预期）；三闸对含 rev 段全票面现跑 BLOCK 0／exit 0。
- 只读自证＝零 git 写；探针落 .scratch／QA-REV2-LC／（pairing 样件 ledger／leases／states 三枚＋lease 探针两态）＝真账终核开工拍＝终拍全等零染。

红-1 销账＝成立（R-1＝J-3 槽补实＋五枚 REJECT 直证对拍）：
- rev-1 窗申明「path_globs 五枚逐枚对 engineer 现跑＝五枚全部 exit 2 REJECT」＝本席独立复跑对 engineer＋countersign 形制合规＋台账重定向 scratch＝五枚（run-gates／check-staged-declaration／gate-token-verify／gate-token-issue／双前缀 reconcile-daily）逐枚 exit 2 REJECT「越出席位写域行」＝rev 窗读数复现全等。
- J-3 槽补列在册＝并案号 LEAD-CONSTRAINT-写域随动并案三票互指现读；甲态＝本窗五枚实测拒直证在册／乙态扩行归并案窗＝与 T4／T1 同批＝程序自洽。
- 先例归因改如实＝两址台账 grep share／ 条目零本席现跑复证＝「不可直证」成立。
- J-2 实测补录一行（reconcile-daily 具名 exit 2）＝恰落 v1 预设去路＝该面闭。

黄-1 销账＝成立（R-2 pair-gap 键闭集可判性＝现场构造样件一枚验证）：
- 现场构造三形样件台账（齐形＝commit 真钉／缺签字形／缺 commit 形＝--ledger／--leases／--states 三锚重定向 scratch）＝现版 reconcile-daily 跑＝diff 0 三形互不可分（复证「该臂为必要新增」）；R-2 钉值闭集 {missing-signature, missing-commit, complete} 三值对位可判性核＝键 pair-gap 落 diff_items 载荷内增具名键＝输出行形制沿既有一行一键读数列＝三值机械可判（验收「逐一对位」按三值判＝无需放行段再裁形制）＝销。随登一行＝现版 diff_items 为字符串列非键值载荷，S5 落码时「diff_items 载荷内增具名键」的具体 schema 须施工回执具名＝实现细节归施工面不判违例。
- 黄-2 销账＝成立（R-3 入账主体闭环具名机件可指性）：R-3 钉定「消费入账动作归 S1／S2 调用侧内嵌臂＝ledger.jsonl append 行经脚本面写入」＝可指实体现读＝append_record 同款账本写入机件在 state-transition.py 行 155／sign-verify.py 行 116—141 等八件同款在册（写入类＝RECORD_TYPES 六类零动＝载荷扩展具名）；本席复核＝「签字」类记录既有实体均非令牌消费通道（六节点签字面）＝R-3 「既有账本机件通道对令牌消费无现成实体→闭环钉定调用侧内嵌」归因如实＝销。

计数变化＝红 1→0；黄 2→0。

并案实测表（同 T4 判词件随附全表＝本票面五枚读数为其中段＝此处不重复全表；本票段读数：未注入 5／5 REJECT＝注入-乙 5／5 ALLOW 翻转＝share／ 四枚＋skills／sop／scripts／reconcile-daily 一枚经双前缀 skills／ 扩行命中）：一句话结论＝可行形态取乙。

T2 一句话结论＝rev-1 转绿成立＝红一枚销＋黄两枚全销＋并案五枚两态读数在册＝可放行候裁（J-2／J-3 待放行段裁＋黄-ProdA／B 随登面照登）。

（自靶＝本续段落笔前后 check-ticket judgment 尺＋check-pointers --target 本判词件现跑＝BLOCK 0／WATCH 0／exit 0＝judgment 尺归零；preflight 尺＝票骨架目不适用判词件＝沿历轮案型不跑具名；探针族用毕即拆 ls 0 随完工回报。）
