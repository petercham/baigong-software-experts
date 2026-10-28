# gates.md · T-fuxi-verify-01 各闸读数（2026-10-29）

复测面＝测试区三包 `packs/{david-fincher,mrbeast,miyazaki}`；脚本＝devkits `tools/`（HEAD `9ad54b2`）。
复测申报四要素（⑥-1）＝口径 script-v1＋被测 commit skills `5d4d38e`（=tag fuxi-skill@v1.4.0）／devkits `9ad54b2`＋实测人 engineer-fuxiv＋取整 ceil。

## 一、帽检（MC-FX-STRUCT-2 · count_agent_tokens.py · script-v1/ceil）

全部 12 件 OK（≤2500）：
```
david-fincher: SKILL 325 / 主件 1616 / deep 1292 / 台账 1998
mrbeast:       SKILL 323 / 主件 1529 / deep 1165 / 台账 1562
miyazaki:      SKILL 318 / 主件 1669 / deep 1332 / 台账 2395
```
读数＝帽未触发拆件（自主蒸馏件从起草期即按主件+deep 两段式写，⑥-4 分配未顶死）。**未发生 OVER→拆件路径＝第四式无损压缩本轮未触达**（见 report 逐条触达表）。

## 二、pack-boundary 判定（S0 归包判定句）

三主体逐判「是否需要具名作者/流派/理论来源才成立？」→**均是＝perspective**；两问序第二步：原料均为"人"→**人格镜片**（非技法镜片）。
近邻负例预判（防同包互抢）：运营/留存类场景归 yeshouxiansheng；镜头语言/动画类归 daweifenqi/gongqijin——三件 deep C 节 triggers 表互设"不触发"键（题组第 4 类负例题的件内侧）。
判定读数＝无归包争议件；`content/visual/release` 分流零发生。

## 三、缺①数量闸修订版（挂账计数型·人账不脚本）

修订版口径＝计数挂账不造新脚本闸（拍板 R5 修法「甲挂账计数型＋丙缺有处置词不扣死分」；明文禁"跨域复现≥2"类计数闸）。人工计数读数（可复核至各账行）：

| 件 | 心智模型(3–7) | 内在张力(≥2) | 诚实边界(≥3) | exemplars(2–5) | 判定 |
|---|---|---|---|---|---|
| daweifenqi | 4（deep A-M1..M4） | 2（T1/T2） | 3（M1 局限＋triggers 负例×2） | 4（deep B） | 计数达标·挂账 |
| yeshouxiansheng | 5（A-M1..M5） | 2（T1/T2·T2 降级旗） | 3（M1 局限＋triggers 负例×2） | 3（deep B） | 计数达标·挂账 |
| gongqijin | 5（A-M1..M5） | 2（T1/T2） | 3（M2/M3 边界＋triggers 负例×2） | 4（deep B） | 计数达标·挂账 |

〔触达证据〕三件 exemplars 均含时间码缺口＝〔存疑待核〕旗入候核账（无一条硬编时间码充数）＝修订版"缺有处置词不扣死分"实际起效点。

## 四、闸门一 V8（check-truename.py · 现行词典 CJK26/拉丁24）

- david-fincher：首轮 2×VIOLATION（台账内对照主体「Kubrick/库布里克」直书——现行词典旧条目命中新料区）→ 改写台账行为「恐怖片多条重拍纪录对照」→ 复检 0 VIOLATION，exit=0。
- mrbeast：0 VIOLATION，exit=0。〔限定读数〕现行词典**不含**三新主体真名（grep 实测零命中）→"0 命中"仅证明无旧词典词条漏入，不证明新主体真名零残留；新主体真名残留靠人工扫描（六文件 grep 真名＝全部落 `## meta（来源标注）` 豁免节内，deep/主件正文零真名）。**词典追加＝正式落包（S8）动作，测试区未追加＝候裁项**（追加后须复跑）。
- miyazaki：0 VIOLATION，exit=0（同限定）。另：正文曾出现「吉卜力」＝风格标签污染区，已改「手绘工坊」后复检。

## 五、闸门二结构（check-pack-structure.py --pack 三包）

首轮 BLOCK=3（各包缺 SKILL.md）→补测试区索引后 **BLOCK=0 WATCH=3** exit=0。
WATCH×3＝旧试产区 `research/distill-real-2026-10-28/` 三件采集账缺"独立原始载体 ID"列（历史区 FACT-1 增检报警·非本票产物；本票台账表头已含该列，零报警）。
必填节在位：identity/stance/traits/taboos/audience_contract/performance/exemplars(按需半)/meta 全绿；件内禁项（词汇清单/勾选框/传记/口号）反查未报。

## 六、闸门三盲评台账（check-blind-eval.py）

接口模式读数＝`WATCH 盲评台账零在盘` exit=1〔勘误·T-pres8-fix-01 N-02：原判登记 exit=0 系登记失实；脚本实跑 BLOCK=0 WATCH=1 → exit=1（有 WATCH 即 1），2026-10-29 复跑实测；run-gates 路由表对其走②advisory 不拦提交，故全量门禁仍 PASS，与本条 exit 读数不矛盾〕（预期内：本票＝生产者席，只产盲评包不自评不跑评；台账由 QA 盲评席跑批后落 `.collab/evidence/blind-eval/`）。
`--pack fuxi-verify-test@...` 尝试 exit=2（脚本按 skills 仓包目录定位 SKILL.md＝测试区包不在 skills 仓，机检接口对"测试区假想 pack 名"不适配——登记为工具摩擦 F-05，不修）。

## 七、事实三态（MC-FX-FACT-1 面）

三包镜片正文事实行 100% 带三态标签（起草即挂）；候核账合计〔分账拆分勘误·T-pres8-fix-01 N-06：行级复算（每行取首标为该行三态，K12/K-B7/K-M5/K-M12 双值行注明）——总数 14/8/21 不变，拆分修正〕：fincher 14 行（已核实 3＋双值 1〔K12：148 已核实/127 存疑〕/存疑 3〔K4/K5/K6〕/降级 7〔K1/K2/K3/K7/K11/K13/K14〕）、mrbeast 8 行（已核实 2〔K-B6/K-B7〕/存疑 4〔K-B1..B4〕/降级 1〔K-B5〕/料降级不标三态 1〔K-B8〕）、miyazaki 21 行（已核实 10〔K-M1/M3/M4/M5/M6/M9/M11/M12/M17/M20〕/存疑 8〔K-M7/M8/M10/M13/M14/M15/M16/M18〕/降级 3〔K-M2/M19/M21〕）。〔存疑待核-降级〕子态（A3）使用＝fincher K1/K2/K3/K7/K11/K13/K14、mrbeast K-B5、miyazaki K-M2/K-M19/K-M21（原判枚举漏 miyazaki 三行＝同项级联修正）、无遗漏旗入复审账（复审帽 2026-11-29）。
