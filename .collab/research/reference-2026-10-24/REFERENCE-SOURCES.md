# reference-2026-10-24 参考素材 · 来源索引

> **性质**：索引件（入 git，属 `.collab/research/` 显式入库区）。**实体素材已移出本仓**，现址见 §一。
> **移出依据（2026-10-27 皮总拍）**：性质判据 B＝**出处**——第三方下载产物入我仓＝真源混淆，违单真源纪律；且该目录承载判词依据的部分（顶层 21 件自有 md ＋ `.discussion/` 30 件讨论记录）**早已全部在库**，未跟踪的 1025 件中仅 1 件是本仓自有史实件（已随本次入库），其余 1024 件全为第三方素材。
> **价值不丢三件套**：① 本索引件入 git；② 实体整目录移至仓外归档（保留原结构）；③ 明确"可重建/不可重建"（见 §三）。

## 一、实体现址（2026-10-27 迁移后实测）

```
D:\multi-agent-collab-archive\reference-2026-10-24\
├─ video-teams\            8 个第三方团队包 · 43M
├─ official-cos\          5 个团队包 · 236K（.codebuddy-plugin 结构）
└─ summoned-2026-10-24\   3 个专家包 · 1.4M
合计：972 个文件 / 44M
```

## 二、来源与下载时刻（`.downloaded_at` 实测样本）

| 包 | 下载时刻（UTC） |
|---|---|
| video-teams/ai-content-creator-team | 2026-08-05T13:50:50.285Z |
| video-teams/ai-expert-studio | 2026-09-02T12:35:47.645Z |
| video-teams/humanize-ppt-team | 2026-08-05T14:07:03.070Z |
| summoned-2026-10-24/xiaoyunque-creative-team | 2026-10-24T02:00:51.585Z |
| summoned-2026-10-24/kidd-content-expert | 2026-10-24T02:03:15.407Z |
| summoned-2026-10-24/science-video-team | 2026-10-24T02:04:57.039Z |
| official-cos/* | 待补 |

> ⚠️ **待皮总补**：来源 URL / COS 对象键 / 获取方式——该信息只在决策者侧，工程师席无法代写。体量、文件数、下载时刻、现址均已代补如上。

## 三、可重建性（待皮总判定）

- 是否可从源头（市场/COS）重新下载？→ **待确认**。
- 若**不可重建**：须在本件标注「本机唯一副本」，并安排冷备（2026-10-27 实测 D 盘剩余约 76G / 已用 95%，冷备盘位需另觅）。
- 若**可重建**：本索引件即足够，实体丢失不构成史实损失。

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

直接按 §一 路径取用；若需重新纳入版本管理，优先走**独立归档仓**方案（追溯性最强），不要用 `git rm` 反向操作——历史里的 blob 不会因为后续删除而消失。
