# reference-2026-10-24 参考素材 · 来源索引

> **性质**：索引件（入 git，属 `.collab/research/` 显式入库区）。**实体素材已移出本仓**，现址见 §一。
> **移出依据（2026-10-27 皮总拍）**：性质判据 B＝**出处**——第三方下载产物入我仓＝真源混淆，违单真源纪律；且该目录承载判词依据的部分（顶层 21 件自有 md ＋ `.discussion/` 30 件讨论记录）**早已全部在库**，未跟踪的 1025 件中仅 1 件是本仓自有史实件（已随本次入库），其余 1024 件全为第三方素材。
> **价值不丢三件套**：① 本索引件入 git；② 实体整目录移至仓外归档（保留原结构）；③ 明确"可重建/不可重建"（见 §三）。

## 一、实体现址（2026-10-27 二次迁移后实测）

> **皮总拍（2026-10-27）**：本批素材＝AIGC 视频团队专家包项目的开发参考，归属跟项目走，迁入该 bundle 目录下 `.dev/` 专属区；`.dev` 不入 bundle 快照（experts 主仓 `.gitignore` 排除·装配按 bundle.lock 经 git archive 取源，永远不会带出），其自身另立独立 git 仓做远端备份。

```
D:\multi-agent-collab-experts\workbuddy\hjh-aigc-video-team\.dev\
├─ README.md                      （.dev 区说明·两不原则·备份账）
└─ reference-2026-10-24\
   ├─ video-teams\            8 个第三方团队包 · 43M
   ├─ official-cos\          5 个团队包 · 236K（.codebuddy-plugin 结构）
   └─ summoned-2026-10-24\   3 个专家包 · 1.4M
   合计：972 个文件 / 44M
```

沿革：devkits 仓 → `D:\multi-agent-collab-archive\reference-2026-10-24\`（2026-10-27 出库）→ 本址（2026-10-27 归位拍）。旧 archive 址已清空（该目录现仅剩 `collab-backup-20261027\`）。

## 二、来源链条（2026-10-27 二次实测·已闭环，不再待补）

皮总质疑「来源应该就在本地目录里」——实测结论：**对一半**。可考来源确实在本地可考，但**远端 URL 本地不存在**。三层实测如下：

| 层 | 实测结果 |
|---|---|
| ① 包内 `.downloaded_at` | **只有 UTC 时间戳**，无 URL、无 COS key |
| ② 包内 `plugin.json` | 只有 `name` / `version` / `author.name`（如 `CodeBuddy Teams`、`吟游诗人基德`）；**无** `repository` / `homepage` / `url` 字段 |
| ③ 平台市场清单 `cb_teams_marketplace/.codebuddy-plugin/marketplace.json` | 命中 2 包：`ai-content-creator-team`、`kidd-content-expert`，`source` 记为**本地相对路径** `./plugins/<包名>`；市场 `owner`＝`Laurent Zhou <laurentzhou@tencent.com>` |

**结论**：来源＝**平台市场 `cb_teams_marketplace`（非公开 URL）**，取回路径只能"经平台市场重新拉取"，**没有可 bookmark 的远端地址**（市场目录本身也不是 git 仓，无 remote）。所以原「来源 URL 待皮总补」一项**撤销**——不是皮总忘了写，是这条信息在链路上根本不存在。

### 下载时刻（`.downloaded_at` 实测，UTC）

| 包 | 下载时刻（UTC） |
|---|---|
| video-teams/ai-content-creator-team | 2026-08-05T13:50:50.285Z |
| video-teams/ai-expert-studio | 2026-09-02T12:35:47.645Z |
| video-teams/humanize-ppt-team | 2026-08-05T14:07:03.070Z |
| summoned-2026-10-24/xiaoyunque-creative-team | 2026-10-24T02:00:51.585Z |
| summoned-2026-10-24/kidd-content-expert | 2026-10-24T02:03:15.407Z |
| summoned-2026-10-24/science-video-team | 2026-10-24T02:04:57.039Z |
| official-cos/* | 无 `.downloaded_at`（该批无下载时间戳） |

## 三、可重建性（2026-10-27 实测判定）

- **可否从远端 URL 重建：否** —— 无 URL、无 COS key（见 §二）。
- **可否经平台市场重建：有条件成立** —— 只要本机仍装有 `cb_teams_marketplace` 市场，同名包可重新拉取（`source`＝`./plugins/<包名>` 在本地仍存在）。但该市场是**平台侧托管快照**，市场本身下线/换版后同名包不可复现。
- **判定**：按「**不可重建**」口径处理（保守档）——本机原为唯一副本。
- **冷备（2026-10-27 已闭环）**：`.dev` 目录自立 git 仓 `c1d5958`（973 文件跟踪·含 README），推私有远端 `petercham/multi-agent-collab-aigc-video-team-dev`（main）一次成功。**「本机唯一副本」状态解除**（GitHub 远端＝第二副本），原「冷备盘位待安排」一项撤销。
- **价值保底**：该目录承载判词依据的部分（顶层 21 件自有 md ＋ `.discussion/` 31 件）**全部在 git 内**，实体丢失不影响史实链，只影响第三方素材本身的可复现性。

## 四、支撑 / 被引用处（仓内实测）

仓内引用该目录路径的件共 4 处：

- `deliverables/skills/multi-collab/references/90-changelog.md`
- `deliverables/skills/external-advisor-collab/references/20-rounds.md`
- `deliverables/skills/external-advisor-collab/references/40-artifacts.md`
- `deliverables/skills/external-advisor-collab/references/90-changelog.md`

（本目录 `.discussion/` 下的讨论会原始记录＝判词依据，不在移出范围内。）

## 五、仓内保留部分（未随之移出，仍在 git 内）

- 顶层自有 md 21 件（已跟踪）：R1→R2 变更说明、完整架构优化方案 v1.2 三稿、收口登记与身份交接、第一轮~第九轮外部顾问意见汇总等；
- `.discussion/` 31 件讨论会记录（30 件已跟踪 ＋ `20261026a-005.txt` 本次补入）。

## 六、如需取回

直接按 §一 路径取用。已纳入版本管理（2026-10-27 落地＝§一 所述 `.dev` 独立仓方案）；不要用 `git rm` 反向操作——历史里的 blob 不会因为后续删除而消失。
