# QA-SWBRELOC-B1B5 · rev2 修后复审报告 v1（QA 席·fresh eyes·证伪导向·只读复审）

- 复审轮 HEAD 实测＝`5ffbbeb`（≥ 开工门槛 `5ffbbeb` ✓）。
- 被审六件（rev2 补丁件＋ESC1 新票，均 `.scratch/tickets/`）：B1 rev2 `721d40c`／B2 rev2 `843784a`／B3 rev2 `ab8b8b9`／B4 rev2 `efbdcc0`／B5 rev2 `cccc0b7`／ESC1 `5ffbbeb`。
- 修单真源直读：会师件 `.collab/2026-11-03-SWB-B1B5-双席审票会师-处置裁定-v1.md`（`3ad4d99`）；本席 v1 审票件 `.collab/qa/2026-11-03-QA-SWBRELOC-B1B5-审票-v1.md`（`1c72966`）对照销账。
- 复审主面＝B2/B3 全面复审（v1 红 5 支全在 B2/B3）；B1/B4/B5/ESC1＝修正点验证抽查。除本报告外零触碰。

## 〇、手续与体例核验

1. **原票零改动核实 ✅**：六笔 rev2/ESC1 commit `git show --name-only` 逐笔实测＝各仅含自身一个新建文件；五张原票 `git log --follow` 各自末笔仍为起草笔（B1 `b5fd2b4`／B2 `f017a51`／B3 `d584d7b`／B4 `9ae0b8a`+`232bcfb`（审前已认微清）／B5 `8f5efa9`）——零触碰成立。
2. rev2 体例＝「原票不动、补丁件另立、冲突处以 rev2 为准」逐票头注在册 ✓；销账对位表五票齐备，逐目对位会师修单 ✓。

## 一、红项逐笔销账（修后全面复审）

### R-2（B2 红1·门禁换代闭集不完整）→ B2 rev2 补丁一：✅ 闭合（附新黄①②，见 §四）

- **闭集扩六行**核收：check-skill-meta／check-entity／check-provenance／publish＋run-gates 追加目（原票已列本件）＋assert-tool——v1 红-1 指「三子脚本＋run-gates 内嵌段无票认领」四处全部入册，且 publish.py＝QA v1 未点名之同族新发现，认领正确。
- **行号锚逐项直读实测**（对现行脚本）：
  - check-skill-meta.py：`find_root` 探针实测 L72–73（explicit）/L77（walk-up）∈ 票称 L68–72 ✓；`spec_file` 锚 L5/L14 ✓、L29/L30 叙述锚 ✓、退出码闭集引注 L40 ✓；扫描根语义面 L35 ✓＋代码构造 L183–192（双域 pkg_dirs）✓。
  - check-entity.py：`SCAN_ROOT_DIRS = ("deliverables",)` 实测 **L112 逐字全等** ✓；根探针 L128 ✓；叙述段 L28/L35/L109–110 全中 ✓。
  - check-provenance.py：根探针 L99 ✓；`existing_providers` 双域探实测 L187–188（票称 L184–192＝含注释与收尾，区间含实点 ✓）；缺省 target 语义 L45 ✓＋patterns L313–314 ✓；头块锚 L5/L30/L32 ✓。
  - run-gates.sh：`SPEC_ID_HOME` 实测 **L209–215 逐字对位** ✓；解析段 `pkg_dir = os.path.join(ROOT, "deliverables", …)`＋nested 双域探实测 L264–270（票称 L264–272 ✓）；头部 spec_file 锚 L4/L13/L22/L34 四锚全中 ✓（＝PM S4 注释锚同笔随动在册）。
  - publish.py：头块锚 L5/L14/L23 ✓；双域探 L147–152/L159–163（票称 L147/L159＝首锚点 ✓）；L340/L477/L1159 三处逐字对位 ✓。
  - assert-tool.py：L28 生效池注册路径声明实测逐字在册 ✓（L142 `_PRODUCTS_SUBPATH = ("deliverables", "products")` 无斜杠形态＝新黄①，见 §四）。
- **判据 4 GATE PASS 机械可达性推演**：run-gates 以 `--root "$ROOT"` 显式传参调全部子脚本（实测 L137–151）——check-entity/check-provenance 的 explicit 分支不查 deliverables（仅 walk-up 分支查），真正断点在扫描根本身：check-skill-meta explicit 分支 L72 强校验→换代探针后解除 ✓；check-entity `SCAN_ROOT_DIRS` 换三分类候选后扫描非空 ✓；check-provenance 缺省 targets 换 `agent-*/<项目>/scripts/*.py` 后非空 ✓；run-gates `pkg_dir` 段换代后 OA/MC/EAC/OB/PUB 解析可达（SPEC_ID_HOME 键值零动＝前缀语义不变，合理）✓；install-hooks.sh L85 文案行＝钩子再生覆盖（B2-C6 在位）合理。**结论：v1 判定的四处断裂全部有主、同批互锁，判据 4 自此机械可达。**
- **判据 8 等价断言**：8-2（run-gates 裁决段抽样 spec_id 换代前后解析命中数相等）✅ 构造合理（换代前后命中同一组六包路径）。8-1（`existing_providers` 枚举集换代前后**逐名相等**）⚠️ **措辞不达**：现盘 providers 枚举面＝`deliverables/` 一层 ∪ `deliverables/skills/` 一层，实测含 `experts`、`skills` 两个**幻影目录名**；换代后枚举面＝三分类一层＋项目一层＝含 `baigong-software-team` 不含 `experts/skills`——**全集合逐名相等必红**，真等价式＝「六个 provider 实名（object-audit/object-build/multi-collab/external-advisor-collab/bundle-assembly-registration/fuxi-skill）成员资格换代前后全等」。＝新黄②（一行勘正可达，不阻断）。
- **闭集与豁免账再无缺口？——斜杠口径内 ✅／斜杠口径外残留 ⚠️**：判据 3 的 grep 口径＝`deliverables/`（带斜杠）。带斜杠命中面全部有主（桶 B 21＋桶 C 67＝enforcement 5＋s2 2＋s3 1＋probes 1＋drill-03 2＋drill-05 1＋ledger-init 1＋reconcile 42＋seat-permissions 7＋hooks-map 5＋assert-tool 1＝对账见下）。但 `os.path.join(root, "deliverables", …)` **无斜杠形态**不在此口径：`check-collab-lint.py` L131（walk-up 探针）/L279（selftest fixture 路径）、`tools/check-source-of-truth.py` L507（seatdecl fixture）/L754（walk-up）、`assert-tool.py` L142——五处实测在册、无任何票认领。实测危害面＝均**不破坏 GATE 链**（run-gates 恒显式传 `--root`，walk-up 分支不触发；selftest 面非门禁常驻调用，grep `--selftest` 调用点在 tests/drills 内未命中）——故不构成第二红，但属闭集外残留＝新黄①（建议 B2-C8 追加一行「无斜杠 join 形态同批改」或 B4 认领）。

### R-3（B2 红2·`.codebuddy-plugin` 漏项）→ B2 rev2 补丁二：✅ 闭合

- 票称锚式亲测：`git ls-files deliverables/experts/baigong-software-team/ | awk -F/ '{print $4}' | sort -u` ＝ **13** ✓；`ls -A` 十三项＝可见 12＋隐藏 `.codebuddy-plugin/` 1——与补丁二枚举**逐项全等**（agents/avatars/bundle.lock/config/hooks/plugin.json/settings.json/skills/tests/README.md/PRODUCT.md/ARCHITECTURE.md＋.codebuddy-plugin/）✓。
- `.codebuddy-plugin` 一笔单列入回执＋注册面三件在册断言＋判据 1 桶计数含 `.codebuddy-plugin/plugin.json` ✓；B4 rev2 展开表 #14 `.codebuddy-plugin/plugin.json` 互指在位 ✓（装载面＝plugin.json 版本同源三件之二在册）。

### R-4（B3 红1·design 桶碰撞）→ B1/B3/B4 三票联动：✅ 闭合

- **B1 rev2 补丁一**：十一桶闭集串 `decisions/ qa/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/` 逐字在册；判据 4 换代式串值换而式形不变 ✓；件数不变声明（20 件）合理（design 非新壳件）。
- **B4 rev2 补丁四**：矩阵 10 桶→**11 桶×席**（design 行补入＝史实锚入库面·host 无写权外溢＝deny 维持格）✓；B4-C 改写为定案陈述（v1 黄-3 自问自答作废）✓；桶名以 B1-D 规范件 grep 引用不复写 ✓。
- **B3 rev2 补丁二**：design 桶存在性引 B1 rev2 供源 ✓；三票口径互洽（B1 供闭集真源→B3 照 §三 执行→B4 矩阵随动）✓。
- **erratum 第二笔照引核验**：票内引 v3 §三 L64 文本 vs 冻结基线实测 L64——「`.collab/design/` 17 件 | 混线 | 按案线归项目 `.collab\design\`（设计稿属过程域；其中现行有效设计稿若属交接件性质→docs，按 §二点八 存活判据逐件分）」**逐字一致**（引文未含行首尾 `|` 表格竖线＝引用惯例容忍面）✓；v3 §二结构图实测 L40–43 桶名录确无 design＝erratum 定性属实 ✓。
- 实测立账：design tracked **24 件**（票面 17＝起草漂移）→ 补丁二「按实测立账」✓；交接件甄别行（§三 L64 后半句实装·缺省 design 桶）合理 ✓。

### R-5（B3 红2·判据1 豁免不可执行）→ B3 rev2 补丁三：✅ 闭合（附新黄③）

- **该式实跑一遍（只读 grep·HEAD `5ffbbeb`）**：for 式可跑 ✓；命中 **185 行/112 文件**——扫描面构造已把 `.collab/evidence/`（v1 实测 974 命中且续涨）与 inbox 完全排除在扫描面外＝v1 红-2 之「千行历史 json 吞账＋账面动态漂移」根因消除 ✓；账面自此**有限且静态**（185 行全部落 receipts/qa/design/decisions/dispatch/docs/README/deliverables 申报面）。
- 命中分解判定：史述面（receipts/qa 报告与回执内引用≈145 行）＝B3a 换锚不动的史实记录→回执史述账；活引用面（check-collab-lint 三处 EAC-SK5 票锚＝B3a 明文认领 ✓、check-ticket-reconcile 2、seat-permissions.json write_globs 3、architecture-v2.9-copy 3＝史述副本、commit-audit.py 2 等）→换锚/分账可清。
- ⚠️ 两处瑕疵（不阻断）：①票面第二级过滤 `grep -v "^\./\.collab/tickets/"` 实测**空转**（for 式带参 grep 输出路径无 `./` 前缀，且 tickets 本不在扫描面——无害但误导）；②`commit-audit.py` L15/L35 活正则 `\.collab/tickets/[^\s...]+` 命中 2 处＝活代码旧路径，B3a 认领清单未点名、B2 桶 B/C 未列、B4 24 件闭集不含——须回执分账（换锚或史述）＝新黄③。

### R-6（B3 红3·evidence 2 支 tracked 脱库）→ B3 rev2 补丁四：✅ 闭合

- 实测 `git ls-files .collab/evidence/` ＝ **2**（2026-10-29-判词-T-team-rename-01.md＋2026-10-29-回执-team-rename-01.md）✓ 与票面点名全等。
- 三断言可跑性：`git status --porcelain | wc -l`＝0（收笔时点）✓ 可跑；`git ls-files "agent-experts/baigong-software-team/.collab/evidence/" | grep -c "team-rename-01"`＝2——基名全 ASCII，quotepath 转义不影响 grep ✓ 可跑；「git mv 不受目标 ignore 规则影响」断言属实（tracked 件随 rename 保在册，`/**/.collab/evidence/` 只挡 untracked 新入）✓。
- B3e 其余 evidence（untracked 现盘实测 3907·续涨中）走文件系统 mv 零改 ✓ 与 tracked 两支分制成立——v1 红-3 之「判据 2/判据 5 互搏」解除。

## 二、待裁数字分歧：B2 判据1 钉值——**裁决＝作者席 92/122 对；本席 v1 复算 91/123 误**

- 独立重推导（HEAD `5ffbbeb` 实测）：bundle tracked **88** ✓／六技能包 **109**（7+10+40+9+6+37）✓／deliverables 合计 198 ✓。
- 决定性事实＝**B1-D 规范件物理位置**：B1 原票 L30/L57 明文新建 `deliverables/experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md`——即规范件建在 **bundle 子树内**（`deliverables/experts/...` 之下，非 `deliverables/skills/...`），B2 随 bundle 整笔 git mv → 物理落 `agent-experts/baigong-software-team/skills/sop/references/`。
- 故：agent-experts 侧＝88（bundle）＋1（规范件）＋3（experts 域壳＝agent-experts/README＋baigong `.collab/README`＋`docs/STRUCTURE`）＝**92**；agent-skills 侧＝109＋13（skills 域壳＝agent-skills/README＋6×`.collab/README`＋6×`docs/STRUCTURE`）＝**122**；(c) deliverables＝**0**。Σ＝214 双席全等；分解差 1 的根源＝本席 v1 把规范件虚记入 skills 侧（110＝109＋1）＝与 name-status 物理事实不符，**撤回 v1 钉值**。
- **唯一钉值＝`92 / 122 / 0`**（B2 rev2 补丁三双式成立；「勘对注记＋以逐笔 name-status 裁决」的复审路径成立，裁决如上）。
- 附带核：补丁三 mv 件账 198＋1（规范件入 tree）−1（删 deliverables/README）＝198 ✓；Σ214−壳 17＝197 与原判据式对起草基线口径自洽 ✓；203（v3）vs 198（实测）漂移登记行在位 ✓。

## 三、黄项抽查判定

| 目 | 判定 | 实测证据 |
|---|---|---|
| B3 判据2 同域口径 | ✅ | 双侧统一 `git ls-files .collab .scratch` 单命令＝现盘 611（.collab 601＋.scratch 11−1 README 重叠口径以命令现值为准）；迁前 X→迁后 X＋2 两支入库，B 批票两侧同现自然相消、docs 8 件另账防双计——口径自洽可跑。 |
| era 出处二次分账 | ✅（附口径注记） | 「research tracked 面命中 26 条」＝`git -c core.quotepath=off ls-files .collab/research/ \| grep -cE "视频\|video\|短剧\|导演\|编剧"` 实测 **26** 可复现 ✓（默认 quotepath 口径＝24，CJK 转义吞 2 例——回执宜钉 quotepath=off 口径）。自产例判定抽查：`2026-10-23-视频团队本体审计_v1.md` 实测 tracked、名含「视频」被正则命中＝补丁五「本仓自产·不外移留项目桶」判定**正确**；`drafts-2026-10-23/aigc-video-team*`、`video-team*`＝第三方快照移交候选 ✓——二次分账把 v1 PM 所忧「正则误留置自产件」缺口封住。附注＝命中面含 `reference-2026-10-24/全能AIGC视频创作团队-…` 1 件＝gitignore 负向行在册的入库判词依据件，出处分账表须防二次误伤（回执级·非票错）。 |
| 开工 untracked 两栏基线 | ✅ | 实测 refs 8835（票值 ✓）／evidence **3907**（3827→3857→3907 续涨＝「开工实测栏为基」必要性坐实）／inbox 9 ✓／dispatch 10 ✓。 |
| B4 rev2 追加 9 件 ↔ B2 桶 C 互指 | ✅ | tests fixture 面实测 `deliverables/` 命中 **13 处**（test_enforcement 5＋s2 两支各 1＋s3 1＋run-probes 1＋drill-03 2＋drill-05 1）＋ledger-init.sh 1＝**14 处**＝B2 桶 C 所列逐处数全等 ✓；B4 rev2 闭集 #16–24 九件覆盖全部命中文件（drill-runner.sh 实测零命中＝票面「零改则申报退出」条款恰容此态 ✓）；「B2 回执桶 C 行数＝B4 逐处表行数对账断言」＝互指闭合机械可判 ✓。B2 桶 C 写「21 处」系文件×处数口径混写（实测该组＝14），回执以逐处表为准＝非阻断。 |
| B4 补丁一 project_domain_md | ✅ | 实测现值 `"docs/collab-project-structure.md"`（L52）＝票称作废名残留属实；修值 `docs/STRUCTURE.md`＋判据 6 同批存在断言可跑 ✓。 |
| B4 补丁二 16/15 差一 | ✅ | 展开表 15 件逐行清点＝15 ✓（勘正从少不从多·回执 name-only 全等按 15 跑）；追加 9 件展开合计 24 与票面自洽 ✓。 |
| B4 补丁三 四席 deny 随动 | ✅ | 实测 seat-permissions.json `deny_globs` 含 `deliverables/**` 字面恰 **四行**（L16 host／L25 product／L34 architect／L44 qa）＝票称四行全等 ✓；hooks-map 命中 5 处 ✓；判据 7 增「旧字面 occurrence＝0」断言行可跑 ✓。 |
| B5 仓根显式行七行 | ✅ | A2-补1 七行（evidence/refs/inbox/process/dispatch/backup/tmp-*）逐行在册 ✓；引 run-gates `EVIDENCE_DIR` L98 实测逐字对位 ✓；现 gitignore L17 `.collab/evidence/` 旧行实测在册＝「退役时 `/`-锚定新行同批顶替」映射格成立 ✓。 |
| B5 第三方三桶重立 | ✅ | 现行 gitignore L37–39（三桶排除）＋L42–44（三负向行）实测逐字在册＝票称先例形态随迁属实 ✓；A2-补2 六行新树形态对位 ✓；ESC1 先后两态口径在位 ✓。 |
| B5 判据2 矩阵补四探针 | ✅ | 四探针（仓根 evidence/refs 命中＋快照三桶命中＋REFERENCE-SOURCES 负向）均可跑；现行 gitignore 语义下预期命中可推 ✓。 |
| ESC1 两仓两笔 sha256 对账可执行性 | ✅ | 判据 1 三值全等式（handover-list 行数＝experts 接收 commit 行数＝devkits 删源 commit 行数）可跑 ✓；逐件 sha256 断言＋异字节负例构造 ✓；判据 4 自产件未外移交集＝∅ 可机械判 ✓；experts 仓 `D:\multi-agent-collab-experts` 实测在架（README＋workbuddy）＝接收位落位「开工读该仓结构件」条款合理 ✓；清单真源引 B3 rev2 回执二次分账表＝B0 附注③落账处成立 ✓。 |
| B1 rev2 gitignore 知悉注记 | ✅ | 注记文本与 QA v1 实测结论逐点一致（`/**/` 不命中仓根／B1 期旧行在位无洞／终写承接归 B5 rev2）✓；不增判据合理 ✓。 |

## 四、新发现（rev2 引入·全部黄级·不阻断开工）

- **新黄①（B2·无斜杠 join 形态残留）**：`check-collab-lint.py` L131/L279、`check-source-of-truth.py` L507/L754、`assert-tool.py` L142 五处 `os.path.join(…, "deliverables", …)` 形态不入判据 3 grep 口径（`deliverables/` 带斜杠）＝闭集外残留。实测不破坏 GATE 链（run-gates 显式传 root；selftest 非门禁常驻）→ 黄级。建议：B2-C8 追加一行同批改，或 B4 认领（check-collab-lint 已在 B4 15 件表内、tools/check-source-of-truth 已在 B2 原票闭集内——两处顺笔即闭合）。
- **新黄②（B2·判据 8-1 等价式必红）**：`existing_providers` 换代前后**全集合逐名相等**断言现盘推演必红（现盘含幻影名 `experts`/`skills`；换代后含 `baigong-software-team`）。真等价式＝六 provider 实名成员资格全等。一行勘正。
- **新黄③（B3·commit-audit.py 活引用游离）**：`.collab/tickets/` 活正则 2 处＋路径口径史述 1 处无票认领＝B3a 换锚或回执史述分账须补目。
- **新黄④（B3·补丁三第二级 grep 空转）**：`grep -v "^\./\.collab/tickets/"` 对 for 式输出（无前导 `./`）空转；无害，回执注记口径即可。
- 随行注记：era 命中 26 需钉 `core.quotepath=off` 口径；`reference-2026-10-24/全能AIGC视频创作团队-…` 防二次误伤；B2 桶 C「21 处」→ 逐处表 14 处口径归一。

## 五、总裁决

**放行 B 批开工。**

- v1 红六账（R-1 至 R-6）经 rev2 **全部闭合**（逐项证据见 §一）；B2/B3 修后达可开工形态。
- 数字分歧裁决＝**92/122/0**（作者席对，本席 v1 91/123 撤回；§二）。
- 新发现四项均为黄级一行/一目级勘正，不触碰互锁链与判据可达性——**建议随开工附注落账**（新黄①②宜在 B2 开工首笔前以票面一行或回执注记补定，新黄③④随 B3a 回执处理），无需第三轮修票。
- ESC1 票体成立＝B0 附注③销账载体在位 ✓。
- 各票开工 ANCHOR 义务照旧（B1 rev2 笔 ≥`721d40c`… 逐票随原票）；本复审不构成开工令，开工排程归主理人。

——qa-relocrev2 · 本报告只增不改（除本文件外零触碰）·HEAD `5ffbbeb` 读数锚。
