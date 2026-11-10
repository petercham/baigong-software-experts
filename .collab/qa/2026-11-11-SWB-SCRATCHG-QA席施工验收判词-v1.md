# QA-SCRATCHGACC · SWB-SCRATCHG 施工三笔 QA 席独立验收判词 v1

- 验收席：QA 席 `qa-scratchrev`（fresh eyes·未参与施工·承本席 v2 窄复核判据上下文）；票面真源＝`.scratch/tickets/2026-11-10-SWB-SCRATCHG-scratch-ignore-and-debt-ticket-v2.md`（落链 `7900b07`·本席复核 `git log 7900b07..HEAD -- <票面>` 命中 0＝施工期零触碰 ✓）
- 被验收物（eng-scratchg1 三笔·本席逐笔 `git show --name-status` 独立对平）：
  - `f173c03`（23:22）忽略规则笔＝`M .gitignore`（numstat 9/0 ✓）
  - `7fe59f1`（23:44）类B 处置笔＝`R100` 恰两式位点（迁出源面＝百工包 `.scratch/COLLAB-STRUCT-1/` 下「2026-11-09-COLLAB-STRUCT-1-施工回执-v1」件（旧路径现盘已掏空＝迁移到位副证），迁入目标面＝`agent-experts/baigong-software-team/.collab/receipts/2026-11-09-COLLAB-STRUCT-1-施工回执-v1.md`）✓
  - `8977648`（23:55）README 改句笔＝`M README.md`（numstat 1/1 ✓）

## 〇、开工读数（本席当轮现跑 2026-11-11）

- `date` ＝ `Wed Nov 11 00:06:25 2026`（已过零时→判词按当日日期命名）
- `git rev-parse HEAD` ＝ `89776484f181a3ade0693ace25decc6abd5f41b8`（恰＝三笔末笔 README 笔）
- `git status --porcelain --untracked-files=no` ＝ 空（tracked 面净，无他案 staged 残留）
- `7900b07..HEAD` 区间全笔清点＝12 笔：三笔 SCRATCHG 施工＋五笔 FUXI-U39 票面/回执群＋一笔 A14 票面（`3cba063`）＋本席/产品席两件窄复核判词＋无关笔——链上他案笔照登零碰

## 一、V0–V9 终态独立实跑读数表（不采信工程师自报）

| 判据 | 票钉 | 本席终态实跑 | 判定 |
|---|---|---|---|
| V0 | 类B 基线式＝1（off 口径） | 1（施工前值本席 v2 窄复核轮已现跑＝1；终态侧见 V6＝0） | ✓ |
| V1 | exit 0＋逐路径命中行 | exit 0：仓根样本命中 `.gitignore:60:/.scratch/*`，包内两路径命中 `.gitignore:59:/**/.scratch/*`（新块内行号 59/60 在册） | ✓ |
| V2 | 1/1/0 | `--no-index -q` 三式＝**1 / 1 / 0** | ✓ |
| V3-a | 216→0 | 目录级 **0**／文件级 **0**（票 §一 基线 213＋他案窗差→席报 216 同型；终态归零复现） | ✓ |
| V3-b | 空清单 | `?? .scratch/tickets/` 零命中（grep rc＝1）——当轮恰无未落链新票面 | ✓ |
| V3-c | 225→9 基线式 | 全仓 `??` ＝ **9**、`.scratch` ∩ `??` ＝ **0**；九枚散件清单逐枚对平＝票 O-1 六枚 research＋`.py`＋`.scratch_wbdocs.html`＋`assert-modified-run2.txt`（基线存续面一致） | ✓ |
| V4 | 类A 缺省 exit 1＋grep 前后全等 | 类A 首件缺省 `check-ignore -q` ＝ exit 1（index 挡回机理）；`git grep -l "TMP-DISC" -- '*/.scratch/tickets/*'` ＝ **5**（本席 v2 窄复核轮前值 5＝前后全等） | ✓ |
| V5 | exit 0＋行号仍 20 | rb8-suppl `check-ignore -v` exit 0 命中 `.gitignore:20:/**/.collab/evidence/`；`grep -n` 行号 **20** | ✓ |
| V6 | 类B 终态 0＋tickets 137→138 归因 `3cba063` | 类B 终态 **0**（off＋NUL 双验同值）；tickets 桶 **138**＝137＋1，+1 归因 `git show --name-only 3cba063`＝恰落 `.scratch/tickets/2026-11-10-SWB-A14QAEXEMPT-a14-exempt-config-and-qa-exempt-ticket-v1.md` 一枚＝**归因实证成立** | ✓ |
| V7 | GATE PASS＋reconcile 不新增阻断（他案增数 EXEMPT 逐笔核） | `run-gates.sh` GATE PASS exit 0 发现 **150330**（席自测 150271→本席 +59＝间隔窗 FUXI-U39 回执笔 `5f4a1bf` 等在飞面致增，逐笔归因 EXEMPT 口径核过）；`check-ticket-reconcile.py --root .` exit 1·票 **136**／SKIP 93／发现 **184**（184 恰＝席钉；票 +1 与 SKIP +1＝`3cba063` A14 票面自身入 SKIP 组，归因实证）；缺省调用复证仍 exit 2（机理零变） | ✓ |
| V8 | 删 0 增 9＋sed L17/L20 前后全等 | numstat `9 0 .gitignore`；`sed -n '17p;20p'` 现面＝`7900b07^` 侧 base 面**逐字全等**；全文 75 行＝66＋9；九行块落位 L56–L64（L54 REFERENCE-SOURCES＋L55 空行后、杂物节头现 L65＝票 §4.1 选位兑现）；`__pycache__/` 现 L74 在块后（§2.3-4 前提成立） | ✓ |
| V9 | 三式 | ①短语 grep README ＝ **1**；②L22 diff 恰 1 改（1/1）且终态行与票 §4.4-F 规格文本**逐字比对一致**（进 git 列仍 ✅ 不变）；③`ls-files receipts/ | grep -c "COLLAB-STRUCT-1-施工回执"` ＝ **1**（off＋NUL 双验同值，CJK 陷阱案型照防） | ✓ |

## 二、九行块逐字节性独立复点（禁采信席报 NINE-LINE-BYTE-IDENTICAL）

本席独立切拍：从 v2 票面正则切 §4.1 唯一围栏块（9 行）vs `.gitignore` 终态 L56–L64（9 行）——**逐字节相等＝True**，双 sha256 前 12 位同值 **`5bff83f0d9f9`**。席报不采信，自证成立 ✓。

## 三、租约/配置随动缺口独立勘查判定（工程师单列呈报候裁面）

现场实测：
- `agent-experts/baigong-software-team/config/seat-permissions.json` L58 engineer `deny_globs` **含** `".collab/receipts/**"`，无票 §六「除外 receipts 目标面单点」对应行；`seat-permissions-hooks-map.json` L28 同款含行；两文件均无 `!receipts` 类豁免字样（regex 扫描零命中）。
- 消费面机理实证：`agent-experts/baigong-software-team/skills/sop/scripts/write-guard.py` L261-264 逐 globs 消费 `deny_globs`（路径 ∈ deny → permissionDecision deny）；`agent-experts/baigong-software-team/tests/s4/test_enforcement.py` 判据 1 含派生面两文件席位集相等断言——改任一须两文件同步，派生面约束真实在场。
- 租约签发面：`.collab/ledger/leases.jsonl` 中 `grep -ci scratchg` ＝ **0**＝本票无 lease-issuer 签发记录。
- 三笔成链未被拦的现场解释：本仓 devkits 侧 hooksPath 未配置（HOOKHEALTH-SNAPSHOT `hooksPath-readings=0`、hook-mode=0o0——沿 FUXI U37 判词同读数＝本仓惯态，非本案异动），config deny 物理拦截仅在装配部署态生效。

**判定＝黄（非红）**：票 §六「租约段」文本层面已按裁(e)改写（票内承载·本席 v2 窄复核已判闭合）；票的施工声明闭集＝`.gitignore`＋类B 两式位点＋README 一行，**config 两件不在票射程**——故工程师席未改 config＝守闭集不越权，非施工违例；但已裁(e)「租约随动」意图在**配置常驻规则层未落位**＝结构性缺口真实存在（部署态下 engineer 再写该 receipts 目标件将被 deny；后续任何 B-i 型迁件同撞），且租约签发面零记录。缺口须另票（config 层两文件同步随动＋签发流程兑现）处置——归属呈主理人/皮总裁，本席不代裁。**施工产出本体不因此翻红**（产出正确性由 §一/§二全绿承载）。

## 四、README 既有 8 条 BLOCK 面

- 前后对拍：本席取 8977648 父提交面 README 全文（before）与终态（after）各跑 `check-pointers --target README.md`——after＝**8 条**（L23/25/72/84×2/88×2/92，与席报逐条行号全等）；before 文本面八处悬空目标串逐一同位在场（braced shorthand／ESC1 票退役件／reference 三桶／B3B4 收口登记／仓根 config 路径等＝系历史既有悬空）→ **本笔零新增** ✓（L22 改句未引入任何新指针，V7 第三式 exit 1 为 README 面既有 BLOCK 存续态非新增）。
- 归属：A14 票（`3cba063`）v1 起草阶段声明闭集＝其票面自身、施工面＝share 两件＋回执——**不含 README**（票 §票间关系自述写集零交集）→ README 八条 BLOCK 不在 A14 豁免射程＝**另账未在册**，如实呈报候裁（不翻本验收红黄，他案既有面）。

## 五、(h)/(e) 措辞歧义表态

票 (h) 许可族括注「票／回执／README 索引类件」中的「回执」与 (e)/§六 施工回执落点体例（`.collab/receipts/<票ID>-receipt.md`）构成双轨字样：tickets 桶内历史大量 `*-回执-v1.md`＝票附回执惯例，案卷回执归 receipts 桶——两者并存不冲突（(h) 管免忽略豁免面入桶纪律，B-i 管存量单件处置），**表态＝维持观察、不需本票微 rev**；建议未来机检配置类维护票补一行澄清（tickets 桶「回执」＝票附回执，案卷回执落 receipts 桶），非阻断项。

## 六、总裁决

**红 0／黄 1／绿（V0–V9 全判据＋九行块逐字节＋三笔面单对平）**——**验收通过**。

- 黄-1＝config 层租约随动缺口＋租约签发面零记录（§三；治理归属另票呈裁，不推翻产出）
- 观察两项＝README 八条 BLOCK 另账未在册（§四）＋(h)/(e) 双轨措辞澄清建议（§五）
- 链上他案面（FUXI-U39 群笔、A14 票面、双席判词）照登零碰；V7 增数逐窗归因合规 EXEMPT 口径。

## 七、纪律自证

- 只读验收：除本判词外零改动；全程无探针需求（终态真面直跑，`.gitignore` 已是实面对象——本席零写）。
- 临时复测物＝仓根 `.scratch/qa-scratchgacc/`（gates.log／reconcile.log／readme-after.log／README-before.md 四件），完工前删除附 ls 读数（§4.4-A-2 消费面自示范）。
- 落笔前靶检 `check-pointers.py --target <本件>` 必 exit 0（读数随回报）；commit＝collab: 前缀·pathspec 两端齐带·FX_COMMIT_DECLARE·紧邻无窗口·message 零 at 符号字符·禁 add -A/amend/--no-verify·输出重定向落盘·超时 ≥10 分钟·撞锁有界等待零删锁·完工 `git show --name-only HEAD` 恰一件自证。
