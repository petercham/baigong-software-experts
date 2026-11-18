# SWB-WTGATE 起草段 QA 审票判词 v1（闸工具 worktree 感知票·审票段 QA 席 fresh eyes 独立审计·qa-swb-wtgate 落笔）

> 性质＝审票判词（票 §五 收口链「双席独立审」之 QA 席件·审票段另段不预占施工链账）。｜审＝QA 席 qa-swb-wtgate｜日期＝2026-11-18。
> 审计对象＝票面 .scratch/tickets/2026-11-18-SWB-WTGATE-闸工具worktree感知两脚本判臂git原生定位置换票-v1.md（blob fc5f51730ba29522ad44f97cdb072a0e1aea8a46·笔 e5f5a3a6）＋起草回执 .collab/receipts/2026-11-18-SWB-WTGATE-起草回执-架构席-v1.md（blob b888a582877229fa8d5e6b9e5e7b0197ecd3f426·笔 d93da4a4）。
> 开工三读数＝HEAD d93da4a41135a1f30e6bb4281c8160670c1e17cd（链顶现读＝起草回执笔＝票面笔 e5f5a3a6 之合法后继·派工预期全等）＋分支 main 现读＋git status 去 ?? 两枚＝board 计划 v2（M·他案）＋FUXI-U50 旧名残件（A·staged·blob 80c9948f72bf126f2ea7f55d6853b25314509a2d git ls-files -s 现读坐实＝照登零碰零 reset 未带入）。锁面＝开工无 index.lock·全程零撞锁（等待轮数 0）。
> 读数独立性申报＝以下全部读数本席当轮现跑现算，零复用回执自报值；本席全程对两枚改动面对象／禁动八枚／钩子／worktree 两工作区／他案面＝只读零写。

## 一、逐项读数（要件八条·逐条实跑）

1. **开工三读数＋双读对钉**：两枚审计对象盘链双读全等对钉——票面盘 blob＝fc5f5173…＝HEAD 值；回执盘 blob＝b888a582…＝HEAD 值；票面 203 行／回执 47 行（numstat 48 插入＝末行无换行符形制＝与回执 §五 自报自洽）。两枚改动面对象＝share/check-source-of-truth.py 盘 blob 4fe99f6cd869b90df383463a4ad1d650075f0004（840 行）＋share/check-hook-health.py 盘 blob b778dc757f67351f21f104203f9253a2280e7925（165 行）＝盘＝HEAD＝票 §一 起点回填值全等＝未施工坐实。【绿】

2. **两态基线复现**：主仓根 bash share/run-gates.sh 带 --root 主仓根与 --no-write＝GATE PASS exit 0 发现 33389 条＝与票 §〇-4 声称全等；分项 csot 汇总行「模式 dual｜文件 129（agents 7＋skills 122）｜BLOCK 0（新命中 0）｜基线豁免 54（WATCH·键＝文本＋文件集合）｜指针 WATCH 413｜exit 0」逐字段对票面声称全等；hook-health snapshot 行「hooksPath-readings=0｜hook-blob=8b785770…｜hook-mode=0o0」在场。worktree 根 D:/multi-agent-collab-devkits.wt/agent-skills/fuxi-skill 同闸＝exit 1 GATE BLOCK 恰两枚＝check-source-of-truth exit 2「usage error: 包目录不存在：../multi-agent-collab-experts/workbuddy/baigong-video-team」＋FX-HOOK-1「期望钩子不在盘：.git/hooks/pre-commit」（snapshot hook-file=absent）＝两红复现；该根其余闸绿（check-adr exit 0 桶2=20／check-entity 各谓词 0／check-collab-buckets 违例 0）。该根 .git 现读＝gitdir 指针文件（gitfile 非目录实证）。日志落 .scratch/SWB-WTGATE-review/qa-gate-mainroot.log 与 qa-gate-worktreeroot.log。【绿】

3. **钉审**：python agent-skills/fuxi-skill/gates/check-ticket-pins.py 带 --ticket 票面仓根相对径与 --base 8d6b6740＝钉行 9｜违例 0｜exit 0；票面 grep -c '^PIN|' ≡ 9 对咬。九钉形制独立现算（基线 8d6b6740 ls-tree 拉出算面）：旧三钉对基线 grep -cF＝1/1/1＋行号现算 767／777／115＝票面声称全等；新六钉对基线各 0＝全等。【绿】

4. **改动方向可行性（本席核心增值项）**：
   - 实位通读＝csot L767 pkg_abs 拼接行＋L777 skills_abs 拼接行现读形态与票 §〇-2 逐字对位；DEFAULT_PKG／DEFAULT_SKILLS_ROOT 常量实位 L164-165＝票面声称行位全等；csot import 面无 subprocess（现读 import 列＝argparse/json/os/re/sys）；hook L115 拼径行现读对位；hook import 面 subprocess 已在（L40 组）＋EXPECTED_HOOK_BLOB 常量 L47 现读＝8b7857701594264421832edd30dae7e401f85719 与钩子盘上 git hash-object 现跑值逐字符全等。
   - git 旗两态现跑＝git version 2.55.0.windows.3；rev-parse 带 --path-format=absolute --git-common-dir 于主根与 worktree 根两态同输出 D:/multi-agent-collab-devkits/.git（父目录＝主工作区根＝兄弟仓解析锚）；--git-path hooks 两态同输出 D:/multi-agent-collab-devkits/.git/hooks；两命令两态 exit 0＝票 §〇-7 声称全等。兄弟仓两径主仓侧在盘实测存在。
   - fail-soft 回退逻辑自洽核＝resolve_sibling_root 仅对 ../ 起头径走 git 旗，旗失败（returncode≠0／空输出）回退旧拼接＝旧行为保留；主根下锚＝仓根＝新旧逐字节等价路径成立。git_hooks_dir 旗失败回退 root/.git/hooks 同构。两回退分支＝「不更松不更严」语义自洽。【绿】

5. **假树预演复跑**：.scratch/SWB-WTGATE-draft/patched/ 在场。独立核验＝副本 blob＝d7c261bf…／ad6170f5…（非两枚真源＝预演副本不入真源坐实）；行数 860／182＝§三-1 wc 判据基数；git diff --no-index 现算 numstat＝csot 22 2／hook 18 1＝§三-1 基数对咬；副本内新六钉各恰 1＋旧三钉各归 0＝规格逐字置换坐实；并置三件（两基线 json＋白名单 txt）blob 与 share/ 原件全等＝预演环境纯净。本席独立复跑四发＝改后 csot 主根 exit 0／改后 csot worktree 根 exit 0（exit 2 归零复现）／改后 hook-health 主根 exit 0／worktree 根 exit 0；改后 csot 主根全文输出 vs 本席原件主根现跑全文输出 diff 零行（逐字节全等强证·非仅汇总行）；改后 csot 主根输出 vs worktree 根输出全文 diff 零行（两态全等＝修复语义坐实）；改后 hook-health 两态输出全文 diff 零行＋snapshot 行对基线逐字节全等。【绿】

6. **改动面对象未动坐实＋禁动抽查**：两枚改动面对 HEAD／盘现读 ≡ 起点值（要件1 已坐实）＋两 pathspec status 空集；禁动八枚 blob 对 HEAD 与对基线 8d6b6740 双向现算＝两两全等＝票 §一 回填八值全等（run-gates 11a6f4d4／install-hooks f71474ac／check-pointers 33781b31／staged-decl 04f2889f／两基线 json 2c44d339＋f6171c7d／白名单 c7b2141d／pins 3cc80e61）；钩子盘上 blob 现跑＝8b785770…对钉全等存续。【绿】

7. **判据机械判定性＋候补池＋禁动闭集**：§三-3 至 §三-6 五条验收硬判据逐条抽查＝均为「指定命令＋指定读数」形态可机械判定（本席已按其中 §三-3/§三-4 两态全套闸口径与 §三-2 钉审口径当轮预跑可行）；§三-1 numstat/wc 两值／§三-5 blob 对钉／§三-8 链面 ⊆ 声明闭集均机检式。候补池三行在册＝§四-1 钩子动态根＋钉值随正另票／§四-2 install-hooks.sh worktree 感知制度化另票／§四-3 untracked 证据域补盘口径候裁（另 §四-4 EXPECTED_HOOK_BLOB 语义候裁单列＝四条齐）。钩子全域禁动闭集完整＝§一「钩子全域（.git/hooks 全体＋git config 零写）」白纸＋§二 S2 零碰随注 EXPECTED_HOOK_BLOB 常量行零字节＋§三-5 双 blob 对钉＝三点闭环。链面闭集现跑＝git diff --name-only 8d6b6740..HEAD＝恰两枚（票面＋回执）∈ §一 声明闭集；票面笔 numstat 204 插入一面／回执笔 48 插入一面＝起草段两笔封顶恰两笔零超额坐实。【绿】

8. **靶检与实体自查**：python share/check-pointers.py --target 票面仓根相对径 exit 0；--target 回执仓根相对径 exit 0；check-entity 主根直跑＝五谓词（project-name/date/drive-path/discipline-no/ticket-no）count 各 0（项目名经 GATE_PROJECT_NAMES 注入面照登）；两态闸日志内 check-entity 面同读各 0。【绿】

## 二、红黄绿清单

- 红＝零。
- 黄一（票面措辞级·不影响施工）：§三-6「用法错 exit 2 面抽一：--root 不存在＝两枚各自 usage error exit 2 现跑」对 csot 不复现——本席现跑 --root 指不存在目录＝csot 原件 exit 0（root 不存在但 ../ 段折叠落点恰为在盘兄弟仓路径，isdir 判定通过）；hook-health 该 case exit 2 复现。判据本意「退出码闭集行为零变」在两态对照下成立（原件与改后副本同 exit 0＝行为零变坐实），但票面示例读数不准。建议收口对该抽项改用可复现读数基准＝--root 指仓内存在而无包目录下（原件 exit 2 复现坐实·本席现跑），或放行修注措辞；不构成施工障碍。
- 观察随注（非判据违例·归施工段 QA 补充案例）：同 fakeroot 案例下改后副本 exit 0（原件 exit 2）＝锚随主工作区根的 worktree 感知设计语义的自然读数变化（仓内子目录根下 ../ 段经锚折叠到兄弟仓在盘路径）＝与 §三-4 修复方向一致，登记备施工段收口对照。

## 三、总判

**可放行候施工。** 票面规格自洽（九钉形制独立复算全等·置换表与围栏分工公式自洽·声明闭集与链封顶自算坐实），改动方向可行性经本席两态现跑坐实（git 2.55 旗两态同读数·fail-soft 回退逻辑自洽·主根逐字节等价经全文 diff 零行强证），两态基线两红现场复现，预演假树判据基数全对咬，改动面未动与禁动面全数坐实。黄一条系票面 §三-6 抽项示例读数措辞不准，建议放行段修注或收口换基准，不拦放行。

## 四、纪律申报

本席产出＝本判词一件一笔落链（audits 桶＝本席写域）；两枚改动面对象／禁动八枚／钩子全域／git config／worktree 两工作区／他案面（board M 面＋残件 staged 面＋?? 群）＝全程零碰零带入零 reset；本笔面恰本件一枚·pathspec 限定 add 与 commit 紧邻；FX_COMMIT_DECLARE＝本笔面仓根相对纯路径；禁 add -A／禁 amend／禁 --no-verify；message 经 -F 承载·零 at 符号字符（用字样）零反引号·短 token 裸文写·零前向指针（本件引用一律历史 sha）；落笔前本件靶检 exit 0 先行在册（qa-target-judgment-wording.log 前置跑）；commit 输出重定向落盘仓根 .scratch/SWB-WTGATE-review/qa-judgment-commit.log；timeout 十分钟档；fresh eyes 纪律＝本席审计全程未读并行产品审席任何产出。

（判词完——起草段两枚对象审讫；施工段随放行归工程师席；本席止于此。）
