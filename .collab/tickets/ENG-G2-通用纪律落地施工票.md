# ENG-G2 通用纪律落地施工票（工程师席）

- 开端读数：devkits HEAD 以当轮实测为准（≥`a7c043f`）。
- 你是工程师席＝交付面唯一写权席位。设计真源＝`D:\multi-agent-collab-devkits\.collab\research\2026-10-30-通用纪律归处整改设计-v1.md`（commit `a7c043f`·先读全文），条款草案全文已逐字备好，**照抄写入、不再创作**。
- 主理人裁决（对设计件 §三候裁点）：①EAC-L2 迁移**分票**（本票不做 WP-4）；②OA-D6-3/D6-4 首挂 **advisory**；③扫描面首批只入两包面（external-advisor-collab＋baigong-software-team bundle），其余 `--pkg` 逐包扩面。

## 工作包（按依赖序 WP-2 → WP-1 ∥ WP-3 → WP-5）

**WP-2 object-audit 条款面**：`deliverables/skills/object-audit/references/50-document.md` 增 D6-3（交付包指针闭集）行（草案照 §1.2）＋D6-4 行；`SKILL.md` 五测表升六测（T6 干净度六测口径照草案）＋version bump（按该包惯例配版本账）；`90-changelog.md` append 登记行。

**WP-1 software-orchestration 落卷**：`workbuddy/baigong-software-team/skills/software-orchestration/references/dev-discipline.md` 新建（四节条款全文照设计件 §一甲稿逐字）；该包 `SKILL.md` 索引增一行＋version 1.0.3→1.0.4；changelog 登记行。

**WP-3 可达性机检新建**：`deliverables/skills/object-audit/scripts/check-pointer-closure.py` 新建（判据照设计件 §二：OA-D6-3 四模式＋OA-D6-4 可达性·豁免三范式沿用 check-collab-lint 成文号·`--pkg` 参数·缺省两包面）；`run-gates.sh` SCRIPTS 挂一行；`multi-collab/60-gates.md` json per_spec 两行（**advisory**）＋对账表两行；对拍 fixture 落 `object-audit/tests/fixtures/pointer-closure/`（含自咬反例必判绿样例）；py_compile＋fixture 对拍自证。

**WP-5 复验**：全仓 `bash deliverables/skills/object-audit/scripts/run-gates.sh` GATE PASS＋基线读数登记；新检两 spec 首跑读数如实记录（advisory 不拦，命中如实列）。

## 红线
- 不做 WP-4（EAC-L2→MC-HAND-1 迁移＝另票）；不碰 EAC/multi-collab 条款正文（60-gates 表行除外）；不 bump 他包版本链（本票涉 object-audit 与 software-orchestration 两包按各自惯例 bump）。
- 交付面内容不得携带过程件指针（㊺/㊻②）：条款文本照草案写入后自查——草案若含过程件指针字样须停下报主理人，不得自行改写设计真源。

## 完工回执（㊻③）
落 `.collab/research/2026-10-30-ENG-G2-工程师回执-v1.md`：开端 HEAD；**完整写入/修改文件清单**（commit name-only 全等对账）；门禁读数＋新检首跑读数＋fixture 对拍读数；各 WP 机械判据逐项三态。完成后 SendMessage 回 main：回执路径＋commit 列表＋文件清单＋关键读数。
