# SWB-B1 · 迁移施工票：仓根骨架＋7项目固定结构空壳＋约定md落位＋.collab固定结构规范颁（施工票·L2·架构席起草）
Status: 已结案（retire 宣告 2026-11-04·依 2026-11-04 审计对齐类免拍板放行裁定·票面退役批 SWB-RET）

- 起草实测 HEAD：`c86a7d2`（B0 冻结登记笔）；开工 ANCHOR 义务＝开工时实测 HEAD 应为 `c86a7d2` 或其后可达后继，读数附回执开端。
- 施工基线真源＝`.collab/design/2026-11-03-restructure-proposal-draft-v3.md`（B0 冻结态）＋B0 冻结登记 `.collab/2026-11-03-SWB-B0冻结-仓目录重整方案v3基线登记-v1.md`。批次序＝B1→B2→B3→B4→B5（＋ESC1 随 B4 后）；本票＝B1。
- **开工附注三项（B0 登记照录·每票必载）**：
  1. 誊写禁令（裁定 `f5a0d96`）：迁移/搬家一律 `git mv`（仓内）或字节级复制＋删源（跨仓·两仓两笔字节对账）；禁 Agent 重新输出全文式誊写；涉迁移判据＝「新位与原位 diff 仅申报剥壳段／字节一致」。（本票＝新建创作类件为主＝辖域外自察声明，仍全批照注。）
  2. 票面落位（裁定 `f135855`）：`.scratch/tickets`；`.collab/tickets/`→`.scratch/tickets/` 搬家目在 B3（git mv＋E-ARC-1′ 换锚先行·跑绿前禁启动硬线）。
  3. era 跨仓口径：字节级复制两笔对账（experts 仓 `D:\multi-agent-collab-experts` 侧接收）。
- 计数口径＝occurrence；判据命令自带落盘重定向；负例 exit≠0 断言。行号/读数锚 HEAD=`c86a7d2`。

## 声明闭集（20 件·本批唯一可写面）
- 声明闭集：
- agent-experts/README.md
- agent-skills/README.md
- softwares/README.md
- agent-experts/baigong-software-team/.collab/README.md
- agent-experts/baigong-software-team/docs/STRUCTURE.md
- agent-skills/external-advisor-collab/.collab/README.md
- agent-skills/external-advisor-collab/docs/STRUCTURE.md
- agent-skills/multi-collab/.collab/README.md
- agent-skills/multi-collab/docs/STRUCTURE.md
- agent-skills/object-audit/.collab/README.md
- agent-skills/object-audit/docs/STRUCTURE.md
- agent-skills/object-build/.collab/README.md
- agent-skills/object-build/docs/STRUCTURE.md
- agent-skills/bundle-assembly-registration/.collab/README.md
- agent-skills/bundle-assembly-registration/docs/STRUCTURE.md
- agent-skills/fuxi-skill/.collab/README.md
- agent-skills/fuxi-skill/docs/STRUCTURE.md
- deliverables/experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md
- .gitignore
- .scratch/tickets/README.md

## 逐条施工规格

### B1-A 仓根三分类目录骨架（v3 §一白名单）
1. `mkdir agent-experts agent-skills softwares`＋三件薄写 README（各＝分类一句话＋项目名录索引行；名录＝`agent-experts/baigong-software-team`＋`agent-skills/{external-advisor-collab,multi-collab,object-audit,object-build,bundle-assembly-registration,fuxi-skill}`；softwares＝空名录＋「届时再入」行）。目录名一律 `agent-experts`（清残注记一·已决拼写）。
2. 本批不建任何软链/junction。

### B1-B 7 项目固定 `.collab` 骨架＋docs 壳
1. 每项目建 `.collab/README.md`（＝固定结构桶索引薄写，桶名录逐字真源＝B1-D 规范件）与 `docs/` 目录（经 STRUCTURE.md 落位自然生成）。桶目录本体（decisions/qa/receipts/board/research/refs/evidence/inbox/process/dispatch）＝B2/B3 文件落地时生成（git 不追空目录），`.collab/README.md` 预登记全桶名录。
2. 过渡态声明行（每 .collab/README 头一行）：「本包案卷自 B3 批起承接；现行在途案卷暂在仓根 .collab/」。

### B1-C 约定 md 落位（R⑤ 既裁归 B1·定名 STRUCTURE.md＝裁定三§二点九）
每项目 `docs/STRUCTURE.md` 体例（T08R 提案字段冻结）：正文（项目分层目录方案叙述）＋唯一 YAML 围栏块：
```yaml
schema_version: 1
project_root: "."            # 项目根相对字面
delivery_paths:              # 交付（含编译、部署）路径闭集
  - ...
```
- 百工＝delivery_paths：`agents/ skills/ config/ hooks/ tests/ avatars/`（bundle 面）；六技能＝`SKILL.md references/`（fuxi 增 `products/`；object-audit 增 `scripts/ tests/`）。
- **拒 docs 前缀行**（机检款）：delivery_paths 任何行以 `docs/` 开头＝违例。
- 已知数据面缺陷登记（不改数据面·随 B4 修）：seat-permissions `project_domain_md`＝`docs/collab-project-structure.md` 系作废名残留（裁定三§二点九定名 STRUCTURE.md）——B4 闭集内修值。

### B1-D `.collab` 固定结构规范颁（R⑧(i) 向先决闭集·收口登记 `ed5d3c0` §三）
新建 `deliverables/experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md`（交付面规范位现址落笔，B2 随包 git mv 搬家目零动）：
- 桶名闭集（逐字）＝`decisions/ qa/ receipts/ board/ research/ refs/ evidence/ inbox/ process/ dispatch/`＋README 索引件；
- 两制入库声明＝decisions/qa/receipts/board/research 进 git；refs/evidence/inbox/process/dispatch 排除；
- 用户 STRUCTURE.md 内出现 `.collab` 子目录规范＝不认（裁定三§一.3 照录）；
- 本件＝B4 deny `.collab/**` 显式枚举减授权精化的先决真源（引用指针，不复写 B4 行文本）。
- 头注一行：本件＝规范面（泛化级·裁定三§二点五无特例）。

### B1-E .gitignore 最小增补块（B5 全量重写前的过渡防御·防 B2/B3 期项目级 .collab 大块漏入 git）
追加（不删现行任何行）：
```
# B1 过渡增补（B5 全重写前）：任意层级项目 .collab 排除桶
/**/.collab/refs/
/**/.collab/evidence/
/**/.collab/inbox/
/**/.collab/process/
/**/.collab/dispatch/
/**/.collab/backup/
/**/.collab/tmp-*.txt
```
（`.scratch/` 不 ignore＝票面入库面，裁定 `f135855` 语义。）

### B1-F `.scratch/tickets/README.md`
仓根过渡票目录索引（现状＝B 批票面六件；注记＝本目录属过渡态，B3 按项目归宿；旧 `.collab/tickets/` 搬家目在 B3）。

## 验收判据（全部机械可判·自带落盘·负例 exit≠0）
1. 顶层白名单断言：`ls -d */ | sort > $B1_TMP/c1.out` → 目录集＝{agent-experts,agent-skills,softwares,deliverables,docs,tools,.collab,.git,.workbuddy}（B1 期过渡集·deliverables/docs 在 B2/B5 灭）；新增白名单外目录＝exit 1。
2. 名录闭集断言：`ls agent-experts/ agent-skills/ > $B1_TMP/c2.out` → 子项与声明名录全等；softwares 空。
3. STRUCTURE 可解析＋拒 docs 行：python 逐 7 件抽取 YAML 围栏→`schema_version==1`＋`delivery_paths` 无 `docs/` 前缀行 → exit 0；构造含 `docs/x` 行负例（仓外 Temp）exit≠0。
4. 规范件桶名闭集断言：`grep -o "decisions/ qa/ receipts/ board/ research/ refs/ evidence/ inbox/ process/ dispatch/" deliverables/experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md | wc -l` ＝1（occurrence 口径·整串逐字存在）。
5. gitignore 探针：`git check-ignore -v agent-experts/baigong-software-team/.collab/refs/x agent-skills/fuxi-skill/.collab/evidence/y` 两查均 exit 0；`git check-ignore .scratch/tickets/2026-11-03-SWB-B1-restructure-skeleton-ticket.md` exit≠0（票面不被 ignore）。
6. 门禁零回归：`bash deliverables/skills/object-audit/scripts/run-gates.sh --root . > $B1_TMP/c6.out 2>&1` → GATE PASS exit 0 且对开工基线零新增族（开工首跑落盘对拍·读数入回执）。
7. 闭集全等：本批 commit `git show --name-only` 与声明闭集 20 件全等。

## 禁动面
- `deliverables/` 除 B1-D 一件新建外零触碰（含 bundle 版本账——本批不入交付包体，零 bump 自察）；`tools/`、`docs/`（旧）、`.collab/` 全域、`README.md`（仓根）零触碰；`.gitignore` 只增不删不改行。

## 候裁点
无（结构名录/拼写/落位／R⑤/R⑧ 路径均已裁）。

## 票间关系
- 后置：B2（本票目录壳＝B2 git mv 目的地——B2 须用「git mv <源目录> agent-experts/」入壳父目录形态，壳内同名子目录不存在故不撞）；B3 承接 .collab 桶；B4 引用本票规范件为先决真源。

## 回执
落 `.collab/receipts/2026-11-03-SWB-B1-receipt.md`：开端 HEAD＋name-only 20 件＋判据 1–7 逐条命令与读数＋STRUCTURE YAML 解析读数表。交付笔单独 commit（`collab:` 前缀）；禁 `--no-verify`、禁 amend；门禁真拦如实报告不绕闸。
