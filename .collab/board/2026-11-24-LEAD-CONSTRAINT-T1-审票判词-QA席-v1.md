# SWB-LC-T1 · LEAD-CONSTRAINT 案①带外面化 · 审票判词 · QA 席 v1

- 审席＝QA 席（fresh eyes＝三票单席一次审；全部取证本席当轮现跑，零誊起草席读数互证）
- 审对象＝.collab／board／2026-11-24-LEAD-CONSTRAINT-T1-施工票-v1.md（本席现跑两式＝238 行／git hash-object 现算 b84bcbf690160ff1894dcaff44719f3b45aade84＝链上 HEAD blob 现读全等＝链上笔 f050a46b 本体＝与派工预期 238 行全等）
- 审窗读数（本席现跑）＝链顶 f050a46b（＝三票入链笔＝起草窗预期 6b2cc481 后顺一投递笔＝窗移非异象）＋date 2026-11-24 17:1x＋NO_INDEX_LOCK＋tracked 脏面 0 枚
- 只读自证＝零 git 写；远端面＝席位禁检索守禁＝本席仅核登记面（零检索坐实）；探针落仓根 .scratch／QA-REV-LEAD-CONSTRAINT／＝台账重定向＝真账终核 7／8＋7 零染

## 判据一 · 票型面三闸独立复跑归零 —— 绿

check-ticket／preflight-ticket／check-pointers --target 票面 本席现跑＝三闸各 BLOCK 0／WATCH 0 exit 0＝申报互证成立。

## 判据二 · §二 取证读数复跑 —— 绿

    仓内无 workflow 现跑＝.github／ 盘现仅 ISSUE_TEMPLATE 一枚＋.github／workflows 目录不存在＝复现
    run-gates 行 141 SCRIPTS 十一枚现跑计数＝11 枚具名对位（check-provenance…check-collab-buckets）＝复现
    CRLF 环境差现跑＝run-gates 盘现 CR 计数 543＝行数 543＝全 CRLF 案型复现＋git config core.autocrlf 现读＝true＝「CI checkout LF 面＝对钉哈希漂移风险」成立＝S1 段五「禁对钉哈希比对只比内容与 exit 码」为对症兑现锚＝绿
    远端面登记核＝git remote -v 两面在位（本席只读核登记面存在性）；GitHub Actions 开通态／保护态／令牌权限面＝§二·丙三查证项登记槽位在册（回填＝开工 V0 前置＝登记正确性＝本席只核登记面＝形制完备）
    钉值件可核性＝git rev-parse HEAD 全式四十位现跑可解析＝复现
    三台账开工拍 7／8＋7＝复现；链序 6b2cc481←0db682b7←55c2471c＝起草窗在册＋审窗顺一投递笔 f050a46b＝窗移照登

## 判据三 · V 系可机械执行性＋远端四断言臂「本地可先行」与「必待远端」分列核 —— 绿

本地可先行预演臂＝§四 V2「仓内可跑臂」五臂（run-gates --no-write 一致性／钉值件自对臂 git cat-file 两式／workflow 结构 awk＋grep 锚臂／CODEOWNERS 覆盖 grep 臂／本地闸零扰动臂）＝全部本地资源在位可先行；远端断言臂四枚（首笔 PR 绿＋首行哈希对钉／改弱样件红／钉值缺位红／main 直推 403 拒）＝必待保护面＋Actions＋首笔 PR＝票面两臂族分列具名清晰＝绿。

改弱样件臂（产品席 C-1 截断臂）可判性独立推演＝取源规则 6a 兑现臂（工具层从钉位检出＝候选分支面提交的改弱 SCRIPTS 样件不被 CI 执行）＝被检面只提供内容对象＝样件红语义自洽＝样件构造形制（SCRIPTS 清空／闸恒零退出）落候选分支不入 main＝可构造＝绿。

V2 完备性臂现跑＝六段锚 grep -c '^    段'＝6 命中／远端断言臂计数＝5（四臂＋标题自引）命中＝复现。

## 判据四 · 声明判据消费体形制 —— 黄-1

decision-pack full-rollout 消费体现读＝声明判据逐项字符串等值比对读数；四判据 expect 形制（「绿且首行工具层哈希对钉值全等」「红（取源钉位＝改后脚本不被执行）」「拒（保护面 403 面）」）＝非谓词解析＝机械比对退为字面传通、语义判定前置在 QA 填读面＝判据仍可执行（沿表2-2 填读制）但四枚 expect 与回执二元值间需 QA 填读归一一行约定＝与同日 T4、T2 同案型＝随 rev 一行（填读闭集值具名）。

## 判据五 · 租约段互斥性＋写域字面合法性 —— 绿

三票 path_globs 交集现算＝T4∩T1＝∅／T1∩T2＝∅／T4∩T2＝∅；T1 path 命中 T2 deny（.github／**＝T2 明确「.github／ 域零触＝T1 射程」）＋T2 path 命中 T1 deny（run-gates／check-staged-declaration／reconcile 装配族＝T1 禁动枚举）＝跨票互斥双向坐实；本票 path∩deny＝∅＝字面仓根相对 posix 合法＝绿。

## 判据六 · J-1 席位写域案型技术侧表态（工单第 6 项）—— 绿＋黄二枚

技术侧直证（本席 lease-issuer 实测探针＝countersign 形制合规＋台账重定向 scratch）＝engineer 席位行现读 write_globs 无 .github／ 无 share／ 行；.github／workflows／gate-replay.yml／.github／CODEOWNERS／share／gate-replay-tool-pin.txt／share／install-hooks.sh 四枚具名对 engineer 逐枚 exit 2 REJECT「越出席位写域行」＝J-1 甲态实测拒＝直证成立。票面 J-1 预设口径「甲先行实测，实测拒转乙随呈」＝本席实测结果恰落该预设去路＝程序自洽＝J-1 面绿。

黄-2＝「S4 件＝share／ 域写先例在册」归因台账不可证：leases.jsonl 现行态（两份台账全检）零 share／ 条目；config 席位行零 share 行；FX-U34／BKTCLS 链上笔虽写 share 面但租约台账无在册记录＝「当票租约在册先例」不可直证＝与 T4 判词红-3 同根案型（T4 无 J 槽计红、T1 有 J-1 三形态槽覆盖 share／ 两枚＝后果已兜底＝本票计黄）。

黄-3＝钉值件首写执行面未闭合：§三 S3「首写＝人类侧动作＝主理人仅誊录（host 无 share／ 写域＝双兜底沿册）」＋6c 写权钉死＝与 S3 入当票 path_globs（工程师施工租约面）之间写执行主体未具名——host 席位行 write_globs 现读无 share／（写侧同样 deny）＝誊录笔经何租约落链未闭环＝一行补口径（拟＝工程师当票租约受决策者确认值誊写＝6c 申明改「令值＋誊写＋确认」三段）＝放行段裁。

黄-4＝§二·丙查证项三「EDTA 前笔预践登记在册（403 验证臂位）」与登记面不符：预践登记件（.collab／decisions／2026-11-24-皮总亲践-签2前两步预践登记-v1.md）现读＝「Administration 收窄效果（403 面）未验＝T1 落地后随哨兵日核面取证登记（本案不造假验证）」＝403 面＝未验非已践＝引用把「未验」誊成「预践在册」＝一行修（改为「403 面未验＝归本票判据臂四取证」）。

## 总判

- 计数＝红 0／黄 4／绿 4（绿＝三闸归零·§二 读数全复现·V 系可执行＋远端四臂分列清晰·租约三票互斥坐实；J-1 表态面另计绿）。
- 黄-1 criteria 填读闭集一行；黄-2 share 先例归因改如实；黄-3 钉值首写执行主体闭环一行；黄-4 EDTA-403 引用与登记面对齐一行＝四修各一行级＝可随放行段 rev 带修＝无不可放行红项。
- 总判＝可放行（带四黄随 rev）；放行段须裁 J-1（本席实测直证甲拒→乙随呈路径在案）＋J-2 owner 归决策者（本席无对立意见）。

## 复审-1 续段（rev-1 转绿臂·QA 席机检臂单席一次跑·append-only 追加＝v1 判词段零回改）

- 复审窗读数（本席现跑）＝链顶 e5110637＋date 17:5x＋NO_INDEX_LOCK＋tracked 脏面 0 枚；本票 rev 面两式现跑全等＝264 行／79464e5385fda0628f31d2297419751d0466f98a（链面＝盘现＝派工预期）；三闸对含 rev 段全票面现跑 BLOCK 0／exit 0。
- 只读自证＝零 git 写；探针落 .scratch／QA-REV2-LC／＝真账终核开工拍＝终拍全等零染；远端面＝席位禁检索守禁＝本席只核登记面沿册。

黄面两枚核销（本单修目＝criteria 首词闭集行＋查证项三如实化一行）：
- 黄-1（criteria 填读闭集）销账＝成立：rev R-3 落「expect 首词闭集取值＝{通过，绿，红，拒，当场红，具名在场}＝读数填首词＋归因注记＝decision-pack 比对＝首词等值」＋本票四判据 expect 首词取用＝{绿，红，红，拒} 具名对位＝本席对 v1 行 123—128 criteria 块现跑＋现读对位，四枚首词全等（绿且…／红（…）／红（…）／拒（…））；decision-pack 行 120—128 字符串等值比对现读复核＝闭集填读恢复机械比对语义＝销。如实随登一行＝decision-pack 消费体本体为整串等值非首词截取（行 127 str(readings[key]) != str(expect) 现读），首词闭集为填读归一约定＝约定面成立、机件零动＝与三票同款口径相符不判违例。
- 黄-4（查证项三如实化）销账＝成立：预践登记件（.collab／decisions／2026-11-24-皮总亲践-签2前两步预践登记-v1.md）rev 窗引用替换后口径「EDTA 前笔＝换钥匙两步已践登记在册（读面 fetch exit 0＋ls-remote 全等）；403 面未验＝归本票判据臂四取证」＝该件现读行 15／17 对位全等（读面两式在册＋Administration 收窄效果 403 面未验具名＋不造假验证申明）＝引用与登记面已对齐＝销。
- 黄-2（share 先例归因）销＝rev R-2「不可直证」如实化在册＋本席两址台账 grep share／ 零条目复证；黄-3（钉值首写主体闭环）销＝rev R-2 三段「令值＋誊写＋确认」具名＋誊写经当票租约 path_globs 在册态工程师席投递窗落笔＝与并案实测注入-乙态 share／gate-replay-tool-pin.txt ALLOW 读数自洽＝闭环成立。

计数变化＝红 0→0；黄 4→0。

并案实测表（同 T4 判词件随附全表＝本票面四枚读数为其中段：未注入 4／4 REJECT＝注入-乙 4／4 ALLOW 翻转＝.github／ 两枚＋share／ 两枚经扩行命中；票面本体一枚列随登段仍 REJECT＝投递窗主体）：一句话结论＝可行形态取乙。

T1 一句话结论＝rev-1 成立＝四黄全销＋J-1 甲拒四枚实测在册＝可放行候并案窗裁（乙态扩行随呈带确认）。

（自靶＝本续段落笔前后 check-ticket judgment 尺＋check-pointers --target 本判词件现跑＝BLOCK 0／WATCH 0／exit 0＝judgment 尺归零；preflight 尺＝票骨架目不适用判词件＝沿历轮案型不跑具名；探针族用毕即拆 ls 0 随完工回报。）
