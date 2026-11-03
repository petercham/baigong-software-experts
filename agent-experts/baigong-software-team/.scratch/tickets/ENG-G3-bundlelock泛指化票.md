# ENG-G3 bundle.lock 泛指化票（工程师席·执行层修正）

- 开端读数：devkits HEAD 以当轮实测为准。
- 背景（决策依据）：独立核验留下两处边界项——①装配面可达性机检首跑唯一真信号＝bundle.lock conventions.output 含装配预览面盘符字面（`D:\...-build\...`）；②bundle.lock conventions.repo 说明含仓工具带行号自指（`publish.py:829`）。交付物指针闭集裁定要求交付面内容闭环自包含，两处须泛指化。

## 改动（仅 `workbuddy/baigong-software-team/bundle.lock` 一件＋版本账）

1. conventions.output 值中盘符字面 → 泛指措辞（保留语义：缺省输出＝「<bundle 源仓名>-build/<bundle 名>」预览面，不写绝对路径）。
2. conventions.repo 值中 `publish.py:829 join 解析` → 删行号与仓工具自指，改「由装配器解析」类泛指。
3. 版本账（纪律①每变必 bump）：bundle.lock bundle.version 0.1.4→0.1.5＋`.codebuddy-plugin/plugin.json` 0.1.4→0.1.5 同源＋README 版本账 append 一行（泛指化登记，措辞自包含、不带票号过程码）。

## 红线
- 只动上述三件；components 数组、ref tag、note 字段现文零动（note 内沿革史实按既有口径保留）。
- 跨技能引用（OA-D6-4 十七处）＝候裁项，严禁顺手修。

## 完工自检＋回执
- `deliverables/skills/object-audit/scripts/check-pointer-closure.py` 对 bundle 面复跑：OA-D6-3 命中应归零（如实记读数）；OA-D6-4 读数不变（候裁面）。
- `bash deliverables/skills/object-audit/scripts/run-gates.sh` GATE PASS。
- 回执落 `.collab/research/2026-10-30-ENG-G3-工程师回执-v1.md`：开端 HEAD＋完整文件清单（commit name-only 全等）＋复跑读数＋门禁读数。完成后 SendMessage 回 main。
