# SWB-ES2 施工回执（engineer-es2 席·合并收账小票）

- 票面真源＝`.scratch/tickets/2026-11-04-SWB-ES2-seatcard-gate-routing-ticket.md`（定稿链 `bc6dc73`→`ab704b4`→`78fd5bf`→`c126716`·逐字照录落盘，定稿句零改写）。
- 开端 HEAD 实测＝`c126716`（≥ ANCHOR 要求 ≥`c126716` ✓）；施工笔 HEAD＝`f6ffa26`。
- 计数口径＝occurrence；`git -c core.quotepath=off`；负例 exit≠0。

## 判据 1 · 闭集全等

`git -c core.quotepath=off show --name-only --format= f6ffa26` ＝ 8 件，与声明闭集全等：

```
agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json
agent-experts/baigong-software-team/README.md
agent-experts/baigong-software-team/agents/software-team-architect.md
agent-experts/baigong-software-team/agents/software-team-engineer.md
agent-experts/baigong-software-team/agents/software-team-lead.md
agent-experts/baigong-software-team/agents/software-team-qa.md
agent-experts/baigong-software-team/bundle.lock
agent-experts/baigong-software-team/plugin.json
```

product 卡未出现＝未涉席零染 ✓。GREEN。

## 判据 2 · 条款 occurrence 钉值

- lead 卡 `grep -c "\.collab/decisions/"` ＝ **1** ✓
- architect 卡 `grep -c "docs/adr/"` ＝ **1** ✓
- 「分层写入按项目约定 md 校验」engineer+qa 两卡 `grep -o | wc -l` ＝ **2** ✓
- product 卡三串（`.collab/decisions/`／`docs/adr/`／`分层写入按项目约定`）命中 ＝ **0** ✓

GREEN。

## 判据 3 · 数据面对表断言（防卡面造新权）

python json 实跑：lead 卡句路径串集合＝{`.collab/decisions/`} ⊆ host write_globs（seats[0] 尾项＝`.collab/decisions/`）＝True；architect 卡新句路径串集合＝{`docs/adr/`} ⊆ architect write_globs（seats[2] 尾项＝`docs/adr/`）＝True；断言 exit 0。两 config 零改动（`git status --short config/` 行数＝0）✓。GREEN。

## 判据 4 · 纯增行断言

`git diff --numstat`（施工前工作区）：lead 1/0、engineer 1/0、qa 1/0、architect 1/1（写域行原位插改）；`git diff -w --stat`＝4 insertions(+), 1 deletion(-)；architect 旧写域行全文为新版前缀包含＝PREFIX_CONTAINS True（「- 写域：」行两版皆唯一）。product／其余文件在 agents/ diff 零出现 ✓。GREEN。

## 判据 5 · token 红线前后（四要素申报）

口径四要素：①script-v1 口径（`tools/count_agent_tokens.py`：CJK≈1 token/字、非 CJK≈4 字符/token）；②取整＝ceil；③判据线＝每席 ≤2500；④实测人＝engineer-es2；脚本＝`python tools/count_agent_tokens.py "agent-experts/baigong-software-team/agents/*.md"`（同一显式 glob 口径前后两跑）。

| 席位 | 前（基线现值复现） | 后（f6ffa26 态） | 增量 | ≤120? |
|---|---|---|---|---|
| lead | 1474 | 1533 | +59 | ✓ |
| architect | 921 | 942 | +21 | ✓ |
| engineer | 1049 | 1115 | +66 | ✓ |
| qa | 978 | 1044 | +66 | ✓ |
| product | 860 | 860 | 0 | ✓ |

前跑基线五值 1474/921/1049/978/860 与票面现值全等复现；后跑五件全 OK ≤2500。GREEN。

## 判据 6 · 门禁零回归＋六演练

- `run-gates.sh`：开工基线 `c126716`（detached 实跑）＝**GATE PASS 发现 8814**；施工笔 `f6ffa26` ＝**GATE PASS 发现 8814**；Δ0、零新增族（OA-D6 叙述面亦零增量，归因登记＝卡句为纯声明句不含悬空指针形态）。
- SKILL 零涉断言：本批 name-only 无 `SKILL.md`／技能正文（判据 1 闭集表内零出现）✓；`check-skill-meta.py --root .` exit 0 ✓。
- 六演练（盘符口径 `T06_TMP="C:/Users/peter/AppData/Local/Temp/es2-drills2"`）：**SIX_DRILLS_GREEN** exit 0（六链全绿）。
  - 已知坑复现登记：POSIX `/c/...` 口径首跑 drill-05 环境性崩红（Windows python 不解析 Git Bash 路径），换盘符 `C:/` 口径后全绿——非代码缺陷，票面开工附已预告此坑。

GREEN。

## 判据 7 · 版本账

`grep '"version"'` 单行口径三处全等 `0.1.21`（bundle.lock L5／plugin.json L3／.codebuddy-plugin/plugin.json L3）✓；README `git diff --numstat` ＝ **1/0**（版本账 v0.1.21 append 一行·append-only）。GREEN。

## 判据 8 · 条款在位负例

Temp 复制 engineer+qa 两卡、删 engineer 卡纪律句后重跑判据 2 式：occurrence 读数＝1 ≠ 2，断言 `[ "$N" -eq 2 ]` **exit 1** ✓。GREEN。

## 四卡落位行号表

| 卡 | 落位行 | 形态 |
|---|---|---|
| software-team-lead.md | L76 | 「## 纪律行」段尾追加（誊录权句·定稿逐字含【表2-1 host 行誊录权明文】挂注） |
| software-team-architect.md | L22 | 「- 写域：」行原位插改·行尾追加「、`docs/adr/` ADR 落盘写权（编号四位形态随 ES 定标）」·该行其余逐字不动·「明确不可写」行零动 |
| software-team-engineer.md | L39 | 「## 席位纪律」段尾追加（分层校验句·定稿逐字） |
| software-team-qa.md | L38 | 「## 席位纪律」段尾追加（同句·定稿逐字） |

择词登记行：无——「载 surface」按票面缺省逐字保留，未触发改「承载面」选项。

## 三条登记申报

1. **黄-2 挂注处置**：维持票面定稿挂注原文「【裁定三执行规范·project_domain_md 载 surface】」照录落盘（engineer L39／qa L38 同句），解析面按 A 席黄-2 登记级口径处理＝不另出修单；qa 卡「制度③」同构先例在册（qa L29）。
2. **N-2 条件化缓挂引用面**：本批零机件零文档（60-gates／run-gates／scripts 零触碰、`docs/adr/` 目录未造）＝符合 ES2-B 五出口封死裁定。触发双前置在册：①首支 ADR 落项目 `docs/adr/`；②触发批同批实装 run-gates 挂载形态＋E-ADR-3″ 补偿断言随批常驻。落账归主理人收口登记。
3. **architect 卡 L22 旧代字面候补池申报**：写域行内 `.collab/tickets/` 旧代字面＝B3 后卡面残留，属候补池口径（同 CD1 收口黄-3），非本批射程，未改笔、未吞并。

## 禁动面自查

seat-permissions 两 config／60-gates／run-gates／scripts 全域／docs 全域（adr 目录未造）／product 卡／software-orchestration 各卷／票面本身／`.scratch/cd1/`（既有残留未碰·仍 untracked）——本批 name-only 交集为空 ✓。

## 红黄绿汇总

判据 1–8 ＝ **全绿（红 0 黄 0）**；六演练 SIX_DRILLS_GREEN（盘符口径证据行见判据 6）。

——engineer-es2（SWB-ES2 施工席）。
