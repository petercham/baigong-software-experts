# TK-PROJINIT-DEPLOY 部署票 v1 · QA 席独立审 v1

- 审席＝qa-pjdeprev（fresh 实例）；审型＝独立审票（fresh eyes：未读、未参考任何他席审件；与并行产品席互不等待）。
- 开工 HEAD 读数＝`8fb747e`（main，≥ 派工基线 `8fb747e`／≥ 起草开工 `8c07f24`）。
- 被核件（唯一）＝`.scratch/tickets/2026-11-07-PROJINIT-DEPLOY-四段链部署票-v1.md`；落链笔＝`8fb747e`（`git log --oneline -1 -- <票面>` 实证）；件 sha256＝`53f8782abd28ba90f070b3c82e0f8175b5231871f97e6b93118313ef7af09d44`。
- 本审只读取证零写被核面；审件居 QA 写域 `.collab/qa/`，本件外零写。

## 一、实跑取证读数段（全部只读命令实跑）

1. 实绩链锚定：`git show --name-only a4aefb7`＝恰 8 件，逐路径与票面 L23 闭集逐字咬合（4 脚本＋dev-discipline＋SKILL.md＋两 config）；祖先序 `a4aefb7 < 5d6c7a8 < 01c7f16 < 03bb0fe < HEAD` 全真（`merge-base --is-ancestor` 四查全过）。`03bb0fe` 笔面判词「QA 红0黄0绿17」与票面 L22 一致；`5d6c7a8` 笔面「判据1-13全绿」与 L22 一致。`01c7f16` 笔含 PROJINIT QA 审件＋FUXI-U10 回执两件（并发吞并在册＝收口登记已申报，非票面谎报）。
2. 版本三同源：`grep -n '"version"'` → plugin.json **L3**＝0.1.30、bundle.lock **L5**＝0.1.30、.codebuddy-plugin/plugin.json **L3**＝0.1.30——行号与票面 L24 三读数逐字吻合；`git status --porcelain -uno`＝空（M0 clean 断言真）。
3. publish.py：`--out` help＝L1209 「装配输出目录（仅 --assemble 用；缺省＝仓外同级 -build）」逐字在案；`--assemble` L1206 在位；纪律⑤ clean＋ref 闸 L650/672/693 在位。装配面实况：`D:\multi-agent-collab-devkits-build\baigong-software-team` 文件数＝**81**（含 ASSEMBLY.manifest.json＋COPY.state）；build 根列＝`baigong-software-team / baigong-software-team-0.1.29.zip / baigong-software-team.pre-cln-old` 三件，与票面 L41 逐字吻合。manifest 键 `bundle_version`＋`bundle_source_commit` 在位（1c/1d 命令口径可跑）；`grep -c '^\[sync n=' COPY.state`＝4（1e 口径可跑）。
4. 市场源现势：根 plugin.json L3＝0.1.30、.codebuddy-plugin/plugin.json L3＝0.1.30、marketplace.json baigong 条目 version＝0.1.30（三读数＝票面 ②步1 预期）；件数＝**80**、`settings.json` 缺位实证（`ls settings.json` 无果；源仓内 settings.json 在位＝/MIR 拉齐逻辑成立）；marketplace.json 条目列＝hjh-aigc-video-team 1.7.0／hjh-software-team 1.3.3／baigong 0.1.30（②步6「他条目零动」可核）。
5. 备份面：`backup\` 下列既有 baigong 备份止于 `market-src-baigong-0.1.29-pre-deploy-20261106`——W4 新名 `market-src-baigong-0.1.30-pre-deploy-20261107` 与既往命名同形制且**不与既有备份冲突**。
6. 缓存面：`cache\my-experts\baigong-software-team\` 列＝`0.1.0/0.1.1/0.1.22/0.1.24/0.1.27/0.1.29/0.1.30` 与票面 L41、4a 基线逐字吻合；0.1.30 目录内 `.in_use`＋`settings.json`＋两 plugin.json version＝0.1.30＋运行时数字子目录在场＝「W5 宿主自写」语义实证（4b `.in_use` 观测口径可跑）。
7. register_expert.py（真源直读）：docstring L9 含 `[--session-id <session-id>]`；argv 分支 L210 `--session-id` 解析在位；报错路 usage 打印 **L195 不含** `--session-id`——票面 ②步5「usage 面差注记（Y3 沿用）」与脚本实况**逐字吻合**＝先例教训照搬无误。
8. 四脚本探针换代面：`ANCHOR_FILE = os.path.join(".workbuddy", "swb-anchor")` 行号＝write-guard **L48**／lease-issuer **L32**／commit-audit **L56**／memory-neutralize **L44**；四件同款四段语义（SWB_REPO_ROOT 覆写原样返回不做 abspath 归一→锚件权威→STRUCTURE 事后校验→fail-safe 包根）逐件 grep 在案——③清单判据 1/2/3 的钉值描述与代码语义对齐。write-guard `--path` L315（测试注入面）在位＝③判据 4 命令形制可跑。
9. config 两片（python json 直读）：两文件均 `seats` 列表结构（seat-permissions.json 六席含 human；hooks-map 五席无 human）；architect `deny_globs` **不含** docs/STRUCTURE.md（两片）＝真；源件 architect `write_globs` **含** docs/STRUCTURE.md＝真；五席（host/product/architect/engineer/qa）`sources/**` deny＝两片各 5/5＝**十处**全咬；两文件 architect `deny_globs` 逐行全等＝真——③判据 5 全部断言逐条实跑吻合。
10. 文书面 grep：dev-discipline.md `进场建档`=1／`S1b`=1／`swb-anchor`=2；SKILL.md `swb-anchor`=2——③判据 6 各 ≥1 全绿。
11. 锚定区间复测：`git diff --name-only 03bb0fe..8c07f24`＝零 bundle 面、零 external-advisor 面（读数全为 fuxi-skill 他项目面＋两治理面）＝票面 L50 起草实测吻合；`03bb0fe..HEAD` 增量＝本批部署票＋开工登记件＋fuxi 他案面（起草后零 bundle 面新增）。

## 二、判定

**放行**（票面机械可执行性与实绩链一致性成立；无红项；黄 3 条均为注记级，不构成停手条件）。

## 三、红项（阻塞）

无（红 0）。

## 四、黄项（建议·不阻塞）

- **黄1（③判据5 人读面歧义）**：票面 L90「human 行零动」——hooks-map 面 `seats` 实况**无 human 行**（实跑 seat_ids 列＝host/product/architect/qa/engineer 五席），该断言仅在源件（seat-permissions.json，human 行在场）可跑。建议回执口径＝「human 行零动」限源件面核，hooks-map 无 human 行系既成事实照登。票面 L90。
- **黄2（组件面锚定命令形制不可字面直跑）**：票面 L50 组件面含 skills 仓 `skills/deep-research/ 对应 ref 区间`——基准 sha `03bb0fe` 属主仓，在 skills 仓不存在（实跑 `git diff 03bb0fe..HEAD` 于 skills 仓报错）。ref 钉值＝tag `deep-research@v1.0.2`（bundle.lock L25），漂移面小；建议执行时给机械形制＝比对 skills 仓 tag sha 读数 vs 上次装配 manifest 快照＋tag sha 照登回执，勿以主仓 sha 硬套。票面 L50。
- **黄3（备份命名日期与 §六还原命令钉值耦合）**：W4 名含日期 `20261107`（票面 L37），§六还原命令**写死**该全路径（L120）——若 J-1 裁定致执行跨日，备份实际创建名与还原命令钉路径存在名义错位风险（票面 L37 自注「命名随本批现值版本与日期」与 L120 写死形自相微冲）。建议回执登记段②步3 **实际备份路径逐字串**为准，还原时以回执读数引用替代字面复用。风险低（同日内执行则无差）。

## 五、绿灯项（逐条核过·证覆盖）

- 绿1：实绩链四笔（a4aefb7/5d6c7a8/01c7f16/03bb0fe）在链、序真、判词读数与票面 L22 逐字咬合；8 件闭集与交付笔 name-only 恰等。
- 绿2：版本三同源行号级吻合（L3/L5/L3 均 0.1.30）；M0 clean 复测真空。
- 绿3：publish.py 缺省落点 help 逐字实证；装配面 81 件实况＝1b 钉值基线；build 根遗留面三件清单与 L41 吻合；1a/1c/1d/1e 命令口径全部机械可跑（manifest 键、COPY.state 计数式在位）。
- 绿4：市场源三 version＝0.1.30、件数 80、settings.json 缺位差集实证＝②步1 登记面真；marketplace.json 他条目在场可核零动。
- 绿5：缓存目录清单逐字吻合（含 4a 基线七目录）；0.1.30 缓存内 `.in_use` 在场＝4b 观测可跑；W5 宿主自写语义有盘上实证。
- 绿6：W4 备份命名与既往五件同形制零冲突；回滚命令基准（备份 80 件态）与票面 §六还原基准注记自洽。
- 绿7：register_expert.py 参数形制三面取证（docstring L9／argv L210／报错 usage L195 不含）——票面 Y3 注记精确照搬，无弃参误判风险。
- 绿8：四脚本探针换代行号 L48/32/56/44 同款四段语义逐件在案；write-guard `--path` 注入口径在位；③清单 1-4 判据钉值与代码语义对齐（覆写原字面／锚件权威／fail-safe 包根降档）。
- 绿9：config 两片十处 deny＋architect 两键解锁＋deny_globs 跨片全等——③判据 5 逐条实跑全咬。
- 绿10：文书三 grep＋SKILL 随动 grep 全 ≥1（③判据 6 绿）。
- 绿11：锚定区间基准 `03bb0fe`（非先例 d3c0071）复测读数与票面起草实测吻合；bundle/external-advisor 面 diff 空真。
- 绿12：停手条款对抗向＝同版本 0.1.30 现势下 M0 批(b)/批(a) 两路自洽（批(a)「现值仍 0.1.30 且 bump 笔不在案＝停手」堵死抢跑洞）；案(b) 4a 留白有 J-1 附注显式候裁＋停止条款「版本钉值判据段不得强行执行」兜底＝无执行歧义洞；②步1 市场源预期 0.1.30 在批(a) 下仍真（市场源未装 0.1.31）。

## 六、完工登记

- 本件＝本席写集唯一件；commit 后 `git show --name-only HEAD` 自证读数照登链下。
- 独立审声明：未读他席审件、未参考其结论；与并行产品审席零协调零等待。
