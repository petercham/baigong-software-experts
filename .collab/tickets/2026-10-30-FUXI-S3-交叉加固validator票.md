# FUXI-S3 · 交叉加固 validator 票

> 票号＝FUXI-S3｜开票＝主理人｜日期＝2026-10-30｜被派＝工程师席
> ANCHOR＝开工前取当轮 HEAD 实测读数（回执开端必附）
> 施工输入真源（直读照做）＝`.collab\design\2026-10-30-FUXI-S3-施工输入设计-v1.md`（§〇落点骨架＋§一 source-anchor 六层＋§二 public-anchor 六层＋§三 harness 归口＋§四两确认＋§五验收映射三态＋§六随动）。其 §七候裁五点主理人已裁：C-1 绝对线＝四维各均值 ≥3.0（五级量表）锁定／C-2 数值包锁定（诱饵命中上限 0·边缘诚实度期望档位 ≥80%·60/40 种子·×5 一致率下限照件内推荐值）／C-3 person 白名单扩「格式检查表」六值照扩／C-4 validator 分立四件照案／C-5 D7 不提前不留接口位。
> 设计真源（只读参考）＝`.collab\design\2026-10-30-fuxi-skill-merge-boundary-design-v2.md` §十一 S3 行＋D2/D3/D5/D12＋B12/R24/R18/R21/R25。
> 派票口径＝S3 不以 S0b 完工为硬门（已签「S0a 与 S1–S3 照常推进」＋DeepSeek 改写句：人工锚点项等 S0b 交付元组，未交付记「未验」，不以总通过推定）。

## 一、任务（交付闭集）

声明闭集：
- `deliverables/skills/fuxi-skill/gates/validator-source-anchor.py`
- `deliverables/skills/fuxi-skill/gates/validator-public-anchor.py`
- `deliverables/skills/fuxi-skill/gates/harness-common.py`
- `deliverables/skills/fuxi-skill/gates/validator-catalog.md`
- `deliverables/skills/fuxi-skill/gates/assert-tool.py`
- `deliverables/skills/fuxi-skill/gates/assertion-catalog.md`
- `deliverables/skills/fuxi-skill/README.md`

1. **四新建件**：照施工输入 §〇/§一/§二/§三——
   - `validator-source-anchor.py`：六层（机械断言→三臂对照【臂名写死 old/new/without_skill】→诱饵→留出集→嫁接＝泄漏检查＋边缘诚实度）；生成段/判分段分离；退出码闭集 0/1/2。
   - `validator-public-anchor.py`：六层（格式检查表〔D2 嫁接机械位·当期唯一门禁位〕→盲评 rubric→绝对线【C-1 裁值写入】→decoy→泄漏检查→人工锚点卡〔未交付记未验〕）；judge 层分数一律参考位不作门禁位（B12/R24）。
   - `harness-common.py`：非判据共用件（归一化哈希/json 读盘/报表行格式），不含判据。
   - `validator-catalog.md`：validator 层断言目录＋验证记录字段注册表（R25 同源定义面）；顶部 harness 单 owner 声明；对照组构成表落盘路径注册＝`.collab\evidence\harness\`（交付面只注册路径不存数据）；「同模型」声明行＋局限声明口径入注册表字段。
2. **assert-tool 随动**：GS-1..3 转实装（基面＝验证记录目录）；person 白名单扩「格式检查表」六值（C-3）。
3. **断言目录随动**：GS-1..3 标签转实装；F-1＝§五「其余 7 项」改「8 项」；F-2＝GS 分期标签文案随动。
4. **README 随动**：目录地图增 validator 四件行（gates 段内）。

## 二、验收判据（照抄 v2 §十一 S3 行＋施工输入 §五三态口径）

1. gate_source 双向机械断言不匹配数＝0（GS-1..3 实装实跑读数）。
2. source-anchor 退出码可复现：同输入连跑判分段读数全等；生成/判分分离实证。
3. 时间切分可核对行＋哈希泄漏比对：validator 实跑样例（合成样本 %TEMP% 不落仓）跑通。
4. run-to-run ×5 方差数在报：方差报告行格式实装（合成样本演示）。
5. 验证记录可回查位置与 harness 字段同源：validator-catalog 注册表字段↔报表行字段 diff＝∅。
6. D12 排他性正确率独立成行、不并入总分：报表格式实证。
7. 跨家族盲评双跑／三臂读数／人工锚点项／R20 装载核对＝按三态口径各记「规程在场待数据」或「未验」，**不得记绿**；stub schema 已建不推定绿。
8. selftest（含 assert-tool 73 例不回归＋validator 各自 selftest 咬放例配对）exit 0；连跑两次全等；run-gates GATE PASS 零新增红。
9. 全件零过程域指针；命名英文 kebab。

## 三、纪律

- 交付笔单笔（前缀 `ENG-S3:`）＋回执笔（`.collab\receipts\2026-10-30-ENG-S3-工程师回执v1.md`·开端附 ANCHOR＋完工 HEAD＋清单≡name-only＋九读数）。
- 看板如记 S3 事件＝过程笔另 commit。
- 禁 --no-verify、禁 amend、禁 push；遇 HOLD 不开工（本票无 HOLD）。
- 候补池不动：黄-C（看板扫描盲区）、黄-3（value_decl_diff 口径）不在本票范围。
- 两平台确认（装载记录不可导出／「同模型」不可独立校验）按施工输入 §四措辞如实落「未验」，禁以 stub 推定绿。
