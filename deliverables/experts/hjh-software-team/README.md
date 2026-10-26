# Software Company（软件开发团队）

软件开发团队专家团：交付总监统筹产品经理、架构师、工程师、QA 四席，按固定 SOP 把需求推到可验收交付，每步留证据与判定级别。

## 类型

Team 型（多角色协作团队）

## 功能

- **5 席位 SOP 协作**：主理人（交付总监·齐活林）＋产品经理（许清楚）＋架构师（高见远）＋工程师（寇豆码）＋QA 工程师（严过关）
- **工作流路由**：主理人收到请求先判断档位（快速模式／标准 SOP／部分工作流），再定席位编排与推进顺序
- **可审计交付**：每步产出带验收判据与判定级别，需求→拆解→设计→实现→质检全程留痕

## 使用示例

- 把这个需求拆成可验收的开发任务，标出依赖、验收判据和预估改动面。
- 审这份交付或治理报告，按四态判定给结论，列出必须补的缺口。

## 出身

本专家包为**市场包 fork 自维护**：

- **基线**＝WorkBuddy 专家中心市场包 `software-company` **v1.1.0**（下载戳 **2026-10-09**，市场缓存 `~/.workbuddy/plugins/cache/experts/software-company/1.1.0/` 目录 mtime 实测）。
- **fork 后本地改动清单**（除以下三项外，五席 MD 逐字照录市场版，零改写）：
  1. **plugin.json 形态适配**：市场版仅 7 键、过不了注册校验（缺 displayName），改用 my-experts 注册形态 18 键（注册适配层，非席位定义层改动）；
  2. **lead 改名**：文件名 `software-team-lead.md`→`software-company-team-lead.md`，内容仅 frontmatter `name:` 一行同步（Q3 拍定差，diff 市场版＝仅此一处）；
  3. **版本升 1.1.1**（Q5 拍定）：版本号变更逼宿主刷新运行缓存，规避「同版本号免刷新」漂移。
- **上游关系**：fork 自维护，上游后续版本不自动追；需要时人工 diff 市场缓存对账一次（版本账即本节）。
- **版本账 v1.2.0**（2026-10-26）：包 id 更名 `software-company`→`hjh-software-team`（皮总拍定·避免与市场原版混淆·包 id 变更＝破坏性变更升 minor）；席位 id 与席位 MD 文件名不动。
- **基线发现数 79→83（+4 OA-D6 advisory，fork 照录区＋出身段文件名，设计内）**（主理人 2026-10-26 拍 A：判据语义＝BLOCK 级新命中 0＋GATE PASS；先例＝批 2d 判词九；供后续批次对账不误报漂移）。

## 头像

盘上无头像素材，`avatars/` 仅 `.gitkeep` 占位（plugin.json 引用的 `avatars/*.png` 待制作）。替换规格：PNG/JPG、512×512 px、单张 ≤500KB，文件名对应 plugin.json members[].avatar（team.png / software-company-team-lead.png / software-product-manager.png / software-architect.png / software-engineer.png / software-qa-engineer.png）。

## 安装

将专家包目录放到专家目录下：

```
~/.workbuddy/plugins/marketplaces/my-experts/plugins/hjh-software-team/
```

然后运行注册命令使其可见：

```bash
python3 scripts/register_expert.py <expert-dir>
```

## Token 基线（收编批登记·Q4=B 暂不设线只登记）

**口径四要素**：①口径版本＝`script-v1`（`tools/count_agent_tokens.py`：CJK≈1 token/字、非 CJK≈4 字符/token）；②实测对象＝仓内五席 MD 终态；③实测人＝eng-pkg-ta2；④取整方式＝ceil。收编批**不套 2500 线**（Q4 拍 B），lead 超线事实显式登记为**红线待治理**（超 AIGC 线 43%，治理另案）。

| 席位 MD | 行数 | token | 2500 线参照 |
|---|---|---|---|
| software-company-team-lead.md | 211 | **3,578** | **OVER（+43%·红线待治理）** |
| software-product-manager.md | 93 | 1,072 | 绿 |
| software-architect.md | 142 | 1,475 | 绿 |
| software-engineer.md | 150 | 1,865 | 绿 |
| software-qa-engineer.md | 137 | 1,371 | 绿 |
| **合计** | **733** | **9,361** | — |

注：lead 3,578 系 name 行改名后读数（市场版 3,576 净增 2 token，与设计件 §一.1 部署面复算一致）；四成员与市场缓存逐字节一致。

## 维护规则

**改席位定义只改仓内真源（本目录），部署面（`marketplaces/my-experts/plugins/hjh-software-team/`）只准从仓内复制生成**；运行缓存（`cache/my-experts/`）为宿主自管可再生副本，不入治理。
