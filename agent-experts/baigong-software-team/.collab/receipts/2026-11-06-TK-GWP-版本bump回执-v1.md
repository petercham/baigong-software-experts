# TK-GWP 随批版本 bump 回执 v1（完成回流）

- 席位：工程师（eng-gwpbump）
- 票：TK-GWP 批次随批版本 bump（三同源 0.1.29 → 0.1.30 同步同值）
- 日期：2026-11-06
- 回流类型：完成

## 一、开端读数

- 开工第一步 `git rev-parse --short HEAD` = **`5c2d969`**（分支 main，≥ 票面基线要求）
- 链上取证：`git merge-base --is-ancestor` 实证施工笔 `5b8936e` 与 QA 审件 `a67dc37` 均为 HEAD 祖先＝放行链在位后方开工。
- 开工时工作区跟踪面干净（`git status --short` 无跟踪面改动，仅他案未跟踪 scratch 残留，未触碰）。

## 二、三同源实体实测路径（与票面闭集全等）

`grep -rn "0\.1\.29" agent-experts/baigong-software-team/ --include="*.json" --include="*.lock"` 实测定位三同源实体，与票面所列三路径**逐字全等**，无个别缺失：

1. `agent-experts/baigong-software-team/plugin.json`（L3）
2. `agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json`（L3）
3. `agent-experts/baigong-software-team/bundle.lock`（L5）

## 三、改前/改后 grep 读数

改前 `grep -rn "0\.1\.2[89]" agent-experts/baigong-software-team/ --include="*.json" --include="*.lock"`：

```
agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json:3:  "version": "0.1.29",
agent-experts/baigong-software-team/bundle.lock:5:    "version": "0.1.29",
agent-experts/baigong-software-team/plugin.json:3:  "version": "0.1.29",
```

＝三同源 0.1.29 在位、0.1.28 零命中（符合票面预期）。

改后（工作区＋链上 `git grep bd178a9` 双面对拍同值）：

- `grep -rn "0\.1\.2[89]"` → **零命中**（exit 1）
- `grep -rn "0\.1\.30"` → 三同源 0.1.30 同值三命中（行号 3/3/5 与改前对应）

提交 diff 内容面核验（`git show bd178a9` 仅 +/- 版本行）：

```
-  "version": "0.1.29",   +  "version": "0.1.30",   （plugin.json）
-    "version": "0.1.29", +    "version": "0.1.30", （bundle.lock）
-  "version": "0.1.29",   +  "version": "0.1.30",   （.codebuddy-plugin/plugin.json）
```

三件各恰一处改动，其余字段零动（diff --stat：3 files changed, 3 insertions(+), 3 deletions(-)）。

## 四、GATE 读数

`bash agent-skills/object-audit/scripts/run-gates.sh`（提交前、改动在工作区时跑）：

- **GATE PASS（发现 9628 条，均按路由表走②不拦提交）**
- 明细尾段照登：check-ticket-reconcile 票 97（对账 40／SKIP 缺声明 57）｜发现 178（全 WATCH）｜exit 1（均 WATCH 不拦）；check-adr 发现 0｜exit 0。
- 参考面：与票面所给现参考 GATE PASS 962x 段一致（9628 在段内）。

## 五、提交与 name-only 对账

- 提交笔：**`bd178a9`** `TK-GWP 随批版本 bump：三同源 0.1.29→0.1.30 同步同值（QA 放行 a67dc37 后随批）`
- 提交方式：只 add 三件（pathspec 逐件列出），无 `--no-verify`、无 amend、无 `git add -A`；pre-commit 门禁通过未拦截（门禁输出量大＝仓级路由表发现照登，非本笔阻断项）。
- `git show --name-only bd178a9`：

```
agent-experts/baigong-software-team/.codebuddy-plugin/plugin.json
agent-experts/baigong-software-team/bundle.lock
agent-experts/baigong-software-team/plugin.json
```

- 对账结论：name-only 三件与票面施工面闭集三件**全等**（集合相等，无多无一少）。

## 六、部署面零触声明

本票全程零装配、零注册、零复制：未触碰任何 `plugins/cache/` 或部署面目录；未运行任何装配/注册/覆盖缓存动作；工作区未留任何仓外产物（本回执件为唯一新增仓内文件，居 `.collab/receipts/`）。部署类动作留待独立部署票＋用户明示批准。

## 七、其余声明

- 除三件＋本回执件外零写入；他案未跟踪 scratch 残留（`.scratch/FX-*` 等）零触碰。
- 本回执单独 commit，前缀 `collab:`，pathspec 只落本件。
