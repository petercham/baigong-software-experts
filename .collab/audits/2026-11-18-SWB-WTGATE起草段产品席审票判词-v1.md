# SWB-WTGATE 起草段产品席审票判词 v1（闸工具 worktree 感知维护票·起草段两笔·产品席 prod-swb-wtgate fresh eyes 独立审计）

> 性质＝双席独立审之产品席判词（fresh eyes·与 QA 审席互不读·单独一笔）；审对象＝票面 .scratch/tickets/2026-11-18-SWB-WTGATE-闸工具worktree感知两脚本判臂git原生定位置换票-v1.md（笔 e5f5a3a6·blob fc5f5173）＋起草回执 .collab/receipts/2026-11-18-SWB-WTGATE-起草回执-架构席-v1.md（笔 d93da4a4·blob b888a582）；审面＝维护票准入与口径一致性为主·全部读数本席当轮独立现跑·不复用他席读数。

## 〇、开端三读数＋两枚对象 blob 双读对钉

- 开工 HEAD＝d93da4a41135a1f30e6bb4281c8160670c1e17cd＝链顶现读＝派工预期全等；分支 main 现读；链上自基线 8d6b6740 起恰两笔（e5f5a3a6＋d93da4a4）＝起草段两笔封顶零超额现证。
- 脏面照登零碰＝仓根 board 计划 v2（M 他案）＋agent-skills/fuxi-skill/.collab/receipts 旧名残件（A staged·blob 80c9948f72bf126f2ea7f55d6853b25314509a2d git ls-files -s 现读坐实＝本席全程零碰零 reset）；?? 散件群照登零带入。
- 票面对象双读＝盘上 git hash-object ≡ e5f5a3a6 树内 ls-tree 现读＝fc5f51730ba29522ad44f97cdb072a0e1aea8a46 全等·行数 203＝派工口径全等。
- 回执对象双读＝盘上 hash-object ≡ d93da4a4 树内值＝b888a582877229fa8d5e6b9e5e7b0197ecd3f426 全等；行数口径＝wc -l 报 47＝末行无换行符形制（od 现读末字节为汉字非换行）·grep -c 与 awk NR 均 48＝与派工 48 行口径一致＝回执 §五「204 插入＋末行无换行符如实照登」同形制自洽。
- 两笔面数各自恰一枚（git show --name-only 现跑＝票面笔恰票面／回执笔恰回执）＝起草段链面闭集现证。

## 一、维护票准入四判据逐项

1. **判据一·无 API 变更＝绿**：票 §二 零碰随注写死两枚「退出码闭集零动」＋命令行旗面零动（--root/--pkg/--skills-root/--selftest-seatdecl 全部零碰点名）＋快照行形制零动（唯 hook-file=absent→hook-blob 在场＝判臂修正自然读数变化·票 §二 S2 白纸）；§三-6 判据含「--root 不存在＝两枚各自 usage error exit 2」抽验。改动性质＝只换「root 拼径」为「解析锚拼径」＝判臂内部定位逻辑·主根态 §〇-6 预演逐字节等价实证在册。本席对基线实读坐实改动面内无命令行/exit 码新增面：csot L767/L777 旧拼接行与 L769/L779 usage error exit 2 臂在场（现读）·hook L115 旧拼径行与 L122 absent 快照行、L131-133 FX-HOOK-1 计数臂在场（现读）＝置换目标面与票述逐行全等。
2. **判据二·轻量＝绿**：改动面恰两枚（§一-3/4 声明闭集）；numstat 预期 22 2／18 1 本席独立核算闭合＝csot 插入段 17 行＋函数间两空行＋import 1 行＋置换两行＝22 增 2 删；hook 插入段 15 行＋两空行＋置换一行＝18 增 1 删；行数收口 840+22-2=**860**／165+18-1=**182** 机械自洽＝§三-1 判据基数可信。
3. **判据三·实证驱动＝绿**：触发案型实存性 grep 现核＝被引件 agent-skills/fuxi-skill/.collab/receipts/2026-11-18-FUXI-FX-U50起草回执-v1.md 在 HEAD 在册（git grep HEAD 命中）；§四 L54 呈裁请求项②（worktree 根闸另两枚＝兄弟包缺位＋钩子 common-dir 案型＝决策者裁措辞在册）实命中；§五 L66/L68 拦停尝试读数（GATE BLOCK 恰两枚＝check-source-of-truth exit 2＋FX-HOOK-1 期望钩子不在盘·两枚均标「§四呈裁请求项②已在册存量案型」）实命中＝「worktree 工作区提交被拦」案型白纸在册。另本席旁证现跑：worktree 根 .git 现读＝gitdir 指针文件（非目录）·git 2.55.0.windows.3 下 rev-parse 带 --path-format=absolute --git-path hooks 主根与 worktree 根两态输出同值＝主仓 .git/hooks＝票 §〇-7 机械根据独立复现成立。
4. **判据四·未达判据转道条款＝绿**：票 §三 H-0 被动咬处置分支写死（九钉不符／pins exit≠0／主根闸非 GATE PASS／两红未归零／numstat 与 wc 偏离／面数≠2／禁动面 blob 不符＝当场是红停笔＋回流件登记＋呈主理人裁另案＋异常销账路径收口）；开工 ANCHOR 不符＝停手上报禁带差开工（§开工锚照登）；超射程面三行单列 §四 另票候排＝「维护票装不下即转另案/升档」路径在册。

## 二、议题在册性核＝绿（随注一偏移如实登记）

- 票 §四 候补池三行随注实写入册：-1 钩子动态根＋钉值随正另票／-2 install-hooks.sh worktree 感知制度化／-3 untracked 证据域补盘口径是否立规＝三行标题与射程声明逐行在场现读。
- FX-U50 收口登记件（agent-skills/fuxi-skill/.collab/decisions/2026-11-18-FX-U50收口登记-计数随动三源随正闭环.md·注＝实名含「三源随正闭环」·派工书「三源 diff 闭环」为简写非失配）§五 新候补池三行 grep 实命中：①闸工具 worktree 感知维护票（两枚拦停消因）＝即本票射程全等；②install-hooks.sh 生成物 worktree 感知制度化＝票 §四-2 对位；③共享 index 他窗残件悬挂治理＝居本票并发防护条款（D-58 案型照登零碰）射程外·票 §四 未列＝无失配（票未声称对位）。
- 随注偏移如实登记＝票 §四-3（补盘立规）出处＝该回执 §一 案型乙（L19-23 实命中）而非收口登记新三行③；且 FX-U50 回执 §五「候补池随注一行」字样所指＝install-hooks 生成器行＝票 §四-2 引用对象，票 §四-1 亦自称「随注一行」＝同一「随注一行」标签两处并用（本票自序编号与他案原行号并存）＝不构成事实失配·建议 rev 或收口知会时消歧。

## 三、零新口径审＝绿（一处措辞黄见 §六）

- 票面成文引用代号对基线 8d6b6740 先例面既存性逐枚 git grep 现跑＝D-92（75 面）／D-95（95）／D-58（119）／D-94（95）／R-13（19）／U34（44）／U41（65）／H-0（177）／候补池（324）／MC-BUCKET-1（10）／FX-HOOK-1（10）／OA-D6（251）／case4_old_zero_ok（5）／case5_new_one_ok（5）／行内置换（FX-U50 票 6 处）／置换表／维护票＝全部既存＝零新代号零新状态词零新条款引入坐实；桶名零新建（本票不建桶·落位照先例）。
- 落位更正定性合规自洽＝share/check-collab-buckets.py L46-50 现读＝BUCKET_WHITELIST frozenset 恰十七项（decisions…returns）不含 tickets＝新建 .collab/tickets 必触 MC-BUCKET-1 坐实；.gitignore L61-64 现读＝!/.scratch/tickets/ 等四行票面桶豁免在册；先例件 git ls-files 现证＝SWB-BKTCLS／SWB-A14H1 票面实名均落 .scratch/tickets/（同桶既有票面数十枚）＝更正后的落位与回执 §〇 登记三证齐。
- 反引号纪律现跑＝回执零反引号（grep 计数 0）；票面反引号行 12 处全部为仓根起始完整路径且目标在盘（靶检 exit 0 机械背书）；未生成件（工程师回执等）裸文写＝票 §头 A 条款自我适用自洽。

## 四、改动面对象未动坐实＋钩子全域禁动声明核＝绿

- 两枚真源对开工基线与 HEAD 双读全等＝check-source-of-truth.py 4fe99f6cd869b90df383463a4ad1d650075f0004（840 行现跑）／check-hook-health.py b778dc757f67351f21f104203f9253a2280e7925（165 行现跑）＝起草段未施工坐实；两枚对 HEAD 工作面净（git status --porcelain 带两 pathspec 空集现跑 exit 0）。
- 钩子全域禁动＝.git/hooks/pre-commit 盘上 git hash-object 现跑＝8b7857701594264421832edd30dae7e401f85719 ≡ check-hook-health.py L47 EXPECTED_HOOK_BLOB 常量 grep 现读逐字符全等＝FX-U50 改撤归原存续态现证；install-hooks.sh blob f71474ac4a7c7e6f8e754c8f55b123c64d541507 对基线全等存续；run-gates.sh blob 11a6f4d4 全等＋SCRIPTS 清单行（L141 现读）含 ROOT/share/check-source-of-truth 与 check-hook-health 两清单项存续。
- 禁动对钉八枚对 HEAD 现算全等＝check-pointers 33781b31／check-staged-declaration 04f2889f／baseline-sot-dup 2c44d339／baseline-seat-decl f6171c7d／sot-external-provenance c7b2141d／check-ticket-pins 3cc80e61（＋上述两枚）＝票 §一 回填值与盘面逐枚相符。

## 五、两枚对象靶检＋四谓词＋钉预跑（本席独立现跑）

- 靶检＝check-pointers.py --target 票面仓根相对径 exit 0；--target 回执件仓根相对径 exit 0（日志落仓根 .scratch/SWB-WTGATE-review/prod-targeticket-pointer.log 与 prod-receipt-pointer.log）。
- 四谓词＝check-entity.py --root 仓根现跑＝pattern=date／drive-path／discipline-no／ticket-no 各 count=0 exit 0（日志 prod-entity-mainroot.log）＝票 §三-7 收口预期口径一致。
- 钉预跑复算＝check-ticket-pins.py --ticket 票面 --base 8d6b6740 现跑＝钉行 9｜违例 0｜exit 0（日志 prod-pins-base.log）＋票面 grep -c 钉前缀 ≡ 9 对咬；旧三钉行号 767／777／115 对基线 git show 现读逐行全等。

## 六、回执要件齐性＝绿（一处票面措辞黄）

- 开端 HEAD（§〇 8d6b6740 照登）／两态基线（§二 主根 GATE PASS 发现 33389＋worktree 根恰两红全套读数）／钉预跑（§四 钉行 9 违例 0 exit 0＋九钉 B/D 逐枚）／零施工申报（§五 真源零碰＋blob 对基线全等）／纪律申报（§五 pathspec 紧邻＋FX_COMMIT_DECLARE 纯路径＋禁 add -A／amend／--no-verify＋有界等待零删锁轮数 0＋staged 两读自证）＝五要件齐。
- **黄-1（措辞层·不触口径实质）**：票 §四 节标题自称「已裁登记·不入本票射程·非候裁」，但同节 -3 行正文写「是否立规归决策者另裁」、-4 行标题即「EXPECTED_HOOK_BLOB 语义候裁」，§三-5 又引「§四-4」为候裁项＝标题「非候裁」与条目自标「候裁／另裁」字面自相矛盾（实质＝四条均为知会性登记＋未来裁归另案·不阻塞本票·无新口径引入）。建议 rev 修标题措辞或收口登记时随注消歧·不构成放行阻断。

## 七、红黄绿与总判

- 红＝**0**。
- 黄＝**1**（黄-1＝§四标题「非候裁」与条目自标「候裁」措辞自相矛盾·字面层·无实质口径变化）。
- 绿＝开工对钉／准入①②③④／议题在册性／零新口径／未动坐实＋钩子禁动／靶检四谓词钉预跑／回执要件齐性＝十项。
- **总判＝IS_PASS（红 0 黄 1·维护票准入成立·口径一致性成立·黄-1 建议 rev 或收口随注消歧·不阻断放行）**。

（判词完——产品席独立审止于此；本判词一笔落链；黄-1 处置归主理人汇点裁。）
