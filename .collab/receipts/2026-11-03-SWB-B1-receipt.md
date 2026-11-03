# SWB-B1 · 骨架票施工回执

- 票面：`.scratch/tickets/2026-11-03-SWB-B1-restructure-skeleton-ticket.md`（原票 `b5fd2b4`）＋ rev2 定点增补 `.scratch/tickets/2026-11-03-SWB-B1-restructure-skeleton-ticket-rev2.md`（`721d40c`·冲突处以 rev2 为准）。
- 施工席＝工程师席施工员（engineer-b1）；交付 commit＝`c7f87e7`；回执＝本笔单独 commit。
- 回执落位口径＝旧域 `.collab/receipts/`（B 批回执落位·收口登记统一说明）。

## 开工手续读数

- `git rev-parse --short HEAD` ＝ `ebde5f9`（≥ `ebde5f9` 放行基准，ANCHOR 义务满足）。
- `git status --short` ＝ 仅两支 2026-11-01 TKT untracked 旧件（`.collab/qa/2026-11-01-TKT-双席审审流程事件汇总-v1.md`、`.collab/qa/2026-11-01-TKT-最终分票全文汇总编辑-v1.md`），非本席产物、未触碰。
- 门禁开工基线首跑：`bash deliverables/skills/object-audit/scripts/run-gates.sh --root .` → GATE PASS exit 0（发现 631 条·落盘对拍基准）。

## 三项开工附注执行自察

1. 誊写禁令（`f5a0d96`）：本票＝新建创作类件（空壳目录/规范件/STRUCTURE.md/README），辖域外自察声明照注；本批零既有内容位移，零 `git mv`／零搬家目。
2. 票面落位（`f135855`）：本回执涉票引用一律锚 `.scratch/tickets/`。
3. era 跨仓口径：本票不涉及，知悉登记（字节级复制两笔对账在 ESC1/experts 仓侧）。

## 放行条件合并账三目知悉登记

1. 「`/**/` 形态不命中仓根」断言已被净仓复现推翻（check-ignore 实测命中）→ B1-E 过渡块按票面原文执行，未据该错误断言增删（追加块七行逐字照票）；
2. QA 新黄①（无斜杠 join 形态五处残留）认领归 B2/B4，B1 未碰；
3. B1-D 规范件物理位＝`deliverables/experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md`、桶闭集＝rev2 十一桶串（含 design），已按此落笔。

## rev2 补丁逐条读数

- 补丁一（R-4 design 桶扩员）：规范件桶名闭集串已用十一桶串；判据 4 换代串读数（见下表 C4）＝1；规范件头注依据注记行读数：
  `grep -c "design 桶入闭集＝会师件" …/collab-fixed-structure.md` ＝ 1（依据注记行在位）。
- 补丁二（E 节知悉注记）：`.gitignore` 追加块文本零改；知悉注记写入本回执＝本节。实测读数（完工态）：`git check-ignore .collab/refs/x`（仓根层级）exit 0＝命中——与放行条件合并账（会师登记 `ebde5f9` §二）一致：原「`/**/` 形态不命中仓根」断言已被净仓复现推翻（git 语义 `/**/` 匹配零或多个中间目录→仓根命中），B1-E 按票面原文执行未据错误断言增删；B1 期仓根＋任意层级排除桶防护自洽，终写承接责任仍在 B5 rev2（run-gates `EVIDENCE_DIR="$ROOT/.collab/evidence/gates"` 现仍写仓根且 B4 不改）。

## 判据 1–7 逐条命令与读数

| # | 命令 | 读数 | 三态 |
|---|---|---|---|
| 1 | `ls -d */ \| sort` | 可见目录集＝{agent-experts, agent-skills, deliverables, docs, softwares, tools}，与票面白名单（.collab/.git/.workbuddy 为隐藏目录另列实测在位：`.collab/ .git/ .scratch/ .workbuddy/`）对账：白名单外新增目录＝无 | 绿 |
| 2 | `ls agent-experts/ agent-skills/` | agent-experts/＝README.md＋baigong-software-team；agent-skills/＝README.md＋六技能目录（external-advisor-collab, multi-collab, object-audit, object-build, bundle-assembly-registration, fuxi-skill）；与声明名录全等；softwares/＝仅 README.md（空名录） | 绿 |
| 3 | python 逐 7 件抽取 YAML 围栏→`schema_version==1`＋`delivery_paths` 无 `docs/` 前缀行 | 7/7 件解析通过，读数表见下节；仓外 Temp 构造含 `docs/x` 负例→命中拒判（脚本 exit 逻辑对负例返回非 0 路径）；正式跑 exit 0 | 绿 |
| 4 | `grep -o "decisions/ qa/ receipts/ board/ design/ research/ refs/ evidence/ inbox/ process/ dispatch/" deliverables/experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md \| wc -l` | ＝1（rev2 换代串·occurrence 口径） | 绿 |
| 5 | `git check-ignore -v agent-experts/baigong-software-team/.collab/refs/x agent-skills/fuxi-skill/.collab/evidence/y` | 两查均命中（`.gitignore:59:/**/.collab/refs/`、`.gitignore:60:/**/.collab/evidence/`）exit 0；`git check-ignore .scratch/tickets/2026-11-03-SWB-B1-restructure-skeleton-ticket.md` → exit 1（票面不被 ignore＝断言满足） | 绿 |
| 6 | `bash deliverables/skills/object-audit/scripts/run-gates.sh --root .` | 完工后跑＝GATE PASS exit 0（发现 631 条）；对开工基线 diff：无新增发现族——check-ticket-reconcile「未声明生成件」WATCH 实例 43→51（既有族实例增加：旧票对仓根新目录/新文件的脏路径 WATCH，均②路由不拦）、check-pointer-closure SUBSTR 分账 98→101（示例计数·非违例）；VIOLATION 族 86→86 零增 | 绿（如实报实例增量如上） |
| 7 | `git show --name-only` vs 声明闭集 20 件 | 全等（见下节对账） | 绿 |

## STRUCTURE YAML 解析读数表（判据 3）

| 项目 | schema_version | delivery_paths | docs/ 前缀行 |
|---|---|---|---|
| agent-experts/baigong-software-team | 1 | agents/ skills/ config/ hooks/ tests/ avatars/ | 无 |
| agent-skills/external-advisor-collab | 1 | SKILL.md references/ | 无 |
| agent-skills/multi-collab | 1 | SKILL.md references/ | 无 |
| agent-skills/object-audit | 1 | SKILL.md references/ scripts/ tests/ | 无 |
| agent-skills/object-build | 1 | SKILL.md references/ | 无 |
| agent-skills/bundle-assembly-registration | 1 | SKILL.md references/ | 无 |
| agent-skills/fuxi-skill | 1 | SKILL.md references/ products/ | 无 |

负例（仓外 Temp）：delivery_paths＝[docs/x] → docs_prefix=YES → 拒判命中。

## 闭集对账（判据 7）

`git show --name-only --format= c7f87e7`（20 行）与票面声明闭集 20 件逐行全等：
`.gitignore`、`.scratch/tickets/README.md`、`agent-experts/README.md`、`agent-skills/README.md`、`softwares/README.md`、`agent-experts/baigong-software-team/.collab/README.md`、`agent-experts/baigong-software-team/docs/STRUCTURE.md`、`agent-skills/{external-advisor-collab,multi-collab,object-audit,object-build,bundle-assembly-registration,fuxi-skill}/.collab/README.md`（6 件）、`agent-skills/{同上六项}/docs/STRUCTURE.md`（6 件）、`deliverables/experts/baigong-software-team/skills/sop/references/collab-fixed-structure.md`。

## 禁动面自察

- `deliverables/` 仅 B1-D 一件新建，零触碰其余（bundle 版本账零动·零 bump）；`tools/`、旧 `docs/`、`.collab/` 全域（除本回执新落位）、仓根 `README.md` 零触碰；`.gitignore` 只增 9 行（注释 1＋空行 1＋规则 7），零删零改行（`git diff --stat .gitignore`＝9 insertions(+), 0 deletions）。

## 门禁拦阻如实报告

- pre-commit 门禁真跑（未用 `--no-verify`、未 amend）：commit `c7f87e7` 成笔，无 BLOCK 拦下本批；
- 判据 6 实例增量如实登记于上表，未自行消音。

## 候裁点

无（票面候裁点＝无；本批施工中未遇需自行拍板的新裁点，无候裁单列项）。

——engineer-b1 · SWB-B1 回执（本件＝新建创作类·誊写禁令辖域外自察）
