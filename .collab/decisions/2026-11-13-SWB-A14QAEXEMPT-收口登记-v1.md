# SWB-A14QAEXEMPT · 收口登记 v1（主理人件）

## 〇、开工读数（落笔前现跑）

- `date '+%F %T %z'` ＝ 见本笔 commit 前现跑登记（回执与判词读数窗后）
- `git rev-parse --short HEAD` ＝ `01c1e88`（QA 判词笔＝本登记直接 parent）
- tracked 脏面照登零碰零带入＝`agent-experts/baigong-software-team/.collab/ledger/ledger.jsonl`（他案 ledger 脏枚）；仓根 `.collab/` untracked 散件群（史登记件族）照登零带入。

## 一、质量链全账（逐笔在册）

| 段 | 笔次 | 判词/读数 |
|---|---|---|
| 票面 v1 | `cb1de00` 前起链（arch-a14tk1 起草） | 纯规格零施工 |
| 双席独立审票 | PM `cb1de00` 红1黄4绿10／QA `498fe09` 红1黄3绿14 | 红面同构窄修可放行 |
| 票面微 rev | `d88d2a8` | R1-R7 全措辞/口径/列面勘正级，方案本体零动 |
| 放行登记 | `dd10e9c`（同桶皮总裁定 SCRATCHCFG 按乙＋本票按票开工） | 候①采甲转 WATCH 带历史豁免标记／候②采甲仅成文 |
| 工程施工＋回执 | 施工 `3715cb7`（恰两件）＋回执 `a2f19b7` | V0-V7 全绿现跑·两笔封顶 |
| QA fresh eyes 独立验收 | `01c1e88` | IS_PASS 红0黄1绿17·V1-V7 全量照跑＋对抗四臂全绿＋与回执逐值全等 |

零对立段次；无呈拍回流（候①②审票三席一致甲/甲，放行登记时已过滤不占决策者）。

## 二、生效口径（自此生效）

1. **豁免机检配置上盘**＝`share/baseline-pointer-exempt.json`：items 九条＝旧桶 defects 段 drill 一 token × 五文件六枚＋README 八 token 各一文件八枚；fail-closed＝缺失无豁免（更严不更松）／损坏形态不符 `SystemExit(4)`。
2. **check-pointers 豁免层**＝FX-U28 后缀归位层之后、含斜杠悬空 BLOCK append 之前单点插入；命中不计 BLOCK 改出 WATCH 行带「历史豁免」留痕（行内禁含 BLOCK 字样）；三入口（缺省/--target/--scope）同口径消费；裸基名 WATCH 层不接豁免。
3. **计数效果钉值**＝缺省面 SEV-BLOCK 18253→18247（恰 −6）；README target 面 8→0；WATCH 4581→4587（+6）；checker 行量 24836 两态全等；GATE PASS 发现 151339。
4. **候①兑现**＝六枚旧桶 drill 指针转 WATCH 留痕（带历史豁免标记）；**候②兑现**＝`collab_bucket_exempt` 两行成文（fuxi 包 qa＋external-advisor-collab 包 qa）消费面 0 处引用＝仅成文零迁移，桶名闭集机检维持候补池。

## 三、事故与异常照登（史账不回改）

- **11-12 落笔窗中断**：席运行于 19:02 整体终止，当时 STAGED-DECL 放行＋门禁链跑完但 commit 未成＝链上无 BUILD 笔、两件半成品滞留工作区；11-13 续建窗逐字对拍规格复原后全部判据重新现跑再落笔（诚实照登于回执〇节）。
- **staged→??/M 归因终口径**：index 重置动作非 eng-a14c1 席发起、链上无痕迹＝**不可完全归因**；最合理解释＝中断窗内他席/工具链 index 清理或 reset 类操作波及（当时窗内 TOOLHOME 批在飞）。内容盘上完好，不构成事故。
- **inbox 唤起复活案型**（主理人侧登记）：亡席 inbox 指令可唤起席实体（新 task_id、席型保住）＝与 FUXI「实例终结→续写通道失效径改 fresh」先例分野；本例续用成功＝续作优先续用被唤起席，兜底才 fresh。

## 四、遗留与随动

- **黄-1 挂候补池**＝`share/check-pointers.py` 自身 target 面两枚既存存量 BLOCK（HEAD 既有注释行字样，QA 前像臂独立坐实非本笔引入；该件不在缺省扫描域从未入 GATE 基线）——处置（改注释行或入豁免）候另票，不在本票。
- V0 钉值口径随登＝票起草窗 22833（`7900b07` 参照）→开工窗 18253＝链笔栏（dd10e9c..73179da 73 笔/67 件/22 枚 md 他案笔群）＋盘态栏双栏归因在册，R1 口径兑现，「不归因即停」未触发。
- **排程解锁**＝SWB-SCRATCHCFG 四步路径之②（工程师席三件封顶施工·两 config 同批一笔禁拆笔）自此可派；V3 取 R1 A 式三条件式（随裁笔①段写死）。

## 五、本笔自证

- 本笔面＝恰本登记件一件（decisions 桶新建）；
- 落笔前后靶检 `python share/check-pointers.py --target <本件>` 各 exit 0；
- 纪律＝pathspec 两端齐带·add/commit 紧邻无窗口·FX_COMMIT_DECLARE 环境变量形态纯路径清单·禁 add-A/amend/no-verify·message 零 at 符号·输出重定向 `.scratch/SWB-A14QAEXEMPT/`·长 timeout·撞锁有界等待零删锁。
