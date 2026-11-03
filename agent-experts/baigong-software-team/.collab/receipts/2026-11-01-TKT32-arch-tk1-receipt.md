# TKT32 · T05 判据 6 装填/断言对撞轻修 · 完工回执（arch-tk1）

## 开工/完工读数
- 开工实测 `git rev-parse --short HEAD` ＝ **06a1fee**（＝TKT32 登记件；票面锚 `eb5ef6c` 经 `git merge-base --is-ancestor` 实测为其祖先，合规链上相符）。
- 写面＝T05＋总览＋本回执恰三件；禁施工；F-2/F-3/4/5 未顺手改（F-2 候 Q-07 决策者裁）。

## 改前直读核撞（前置义务）
- T05 L35＝「- maxTurns＝200（§8 行7 [实证: spec-agent:21,93]）。」（lead 卡节内）
- T05 L42＝「- 成员卡 maxTurns＝50（§8 行7）。」
- T05 L58 改前＝「6. `grep -c 'maxTurns' software-team/plugin.json` 等装配读数：plugin.json 内 lead maxTurns＝200、成员＝50（JSON 路径断言脚本退出 0）；」
- 三处行位在盘、对撞属实（与主理人复核坐实一致），无停手项。

## 落笔两处
1. **T05 L58 判据 6 改写**（语义闭集按票面，措辞按票面体例）：
   「6. maxTurns 断言对位装填面（L35/L42 同源）：`grep -l '^maxTurns: 200' software-team/agents/software-team-lead.md | wc -l` ＝1 且 `grep -l '^maxTurns: 50' software-team/agents/software-team-{product,architect,qa,engineer}.md | wc -l` ＝4；反向断言防双源漂移：`grep -c 'maxTurns' software-team/plugin.json` ＝0（plugin.json 实证锚无该字段）；」
   ——断言对象＝五张席位卡 frontmatter（lead 200＋四成员 50，读数形态与装填面同源）＋反向断言 plugin.json 不含 maxTurns；其他判据零扩改。
2. **总览修订注**：append-only v1.2.2 注记（F-1 具名，出处引主笔席复核申报登记件路径；v1/v1.1/v1.2/v1.2.1 史不改）。

## 完工自检读数（实测）
- `maxTurns` 全包命中位置前后对照：改前 3 处（T05 L35/L42/L58）→ 改后 3＋1 处（T05 L35/L42/L58 同位改写＋总览修订注记史述 1）——**对撞消除**：L58 断言对象与 L35/L42 装填面同源，plugin.json 侧由正向断言转反向断言；
- 闭集件数复跑＝13/11/7/10/13/11（和 **65** 零变动）；
- 四表行数复跑＝**9/12/16/7** 零变动；
- 各票总行数：T05＝76（不变）／总览＝120（注记为同行内前插，行数不变）／余五票未触碰（diff --stat＝恰 2 files, 2+/2−）。
