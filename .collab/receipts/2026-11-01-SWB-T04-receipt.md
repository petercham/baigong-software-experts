# SWB-T04 回执 · 强制机制群 B5＋B7＋B8＋B10＋B11

- 票面：`agent-experts/baigong-software-team/.scratch/tickets/2026-11-01-SWB-T04-enforcement-hooks-b5-b7-b8-b10-b11.md`
- 开端 HEAD 实测：`2765c3f`（`git log --oneline -1` 读数原文：`2765c3f collab: tickets/README 状态行随批登记（主理人手续）：T03 转已收口＋T04 候开工消费面注记`）——与预期一致。
- 环境注记执行：测试临时目录＝`D:/t04-tmp/`（全域一致路径，用毕已清理）；全部脚本缺省路径支持 `SWB_LEDGER_ROOT`／`--ledger`/`--leases`/`--freeze-state` 重定向；运行与自测全程重定向至 Temp，仓内零运行残留（收尾 `git status --short` 仅闭集文件＋本回执）。

## 完整写入/修改文件清单（11 件＝声明闭集 10＋回执）

1. `deliverables/experts/baigong-software-team/hooks/hooks.json`（T04-A）
2. `deliverables/experts/baigong-software-team/skills/sop/scripts/write-guard.py`（T04-B）
3. `deliverables/experts/baigong-software-team/skills/sop/scripts/commit-audit.py`（T04-C）
4. `deliverables/experts/baigong-software-team/skills/sop/scripts/liveness-selfcheck.py`（T04-D）
5. `deliverables/experts/baigong-software-team/skills/sop/scripts/freeze-unfreeze.py`（T04-E）
6. `deliverables/experts/baigong-software-team/skills/sop/scripts/memory-neutralize.py`（T04-F）
7. `deliverables/experts/baigong-software-team/skills/sop/scripts/shadow-replay.py`（T04-G）
8. `deliverables/experts/baigong-software-team/skills/sop/scripts/sign-verify.py`（T04-H）
9. `deliverables/experts/baigong-software-team/config/seat-permissions-hooks-map.json`（T04-I）
10. `deliverables/experts/baigong-software-team/tests/s4/test_enforcement.py`
11. `.collab/receipts/2026-11-01-SWB-T04-receipt.md`（本件）

## 判据 1–9 实测读数

### 判据 1（hooks.json 结构）— PASS
命令：`python -c "import json;h=json.load(open('deliverables/experts/baigong-software-team/hooks/hooks.json'));assert h"` → `c1 exit=0`。
grep 读数（PreToolUse/PostToolUse 两键在盘）：
```
11:    "PreToolUse": [
43:    "PostToolUse": [
```

### 判据 2（deny 冒烟）— PASS
无租约状态下样例写请求（agent_type=software-engineer，path=docs/foo.md）经 write-guard，stdout 读数原文：
```
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"路径∈deny_globs（表2-1 明确不可写·seat=engineer glob='docs/**' path=docs/foo.md）→ deny"}}
```
含 `"permissionDecision":"deny"`；deny 留痕「写入」记录＋「租约越界deny」呈报码各恰一（账本尾两行读数在案，seq=3 写入/seq=4 呈报）。

### 判据 3（orphan／amend／rebase 三读数）— PASS
```
orphan exit=2   （git commit -m 'plain message no ticket' → BLOCK 形态=['orphan']）
amend exit=2    （git commit --amend -m 'SWB-T04 x' → BLOCK 形态=['amend']）
rebase exit=2   （git rebase main → BLOCK 形态=['rebase']）
```
附：force-push 补位面 `git push --force origin main` → exit=2（B0 退路补位·T04-C）。

### 判据 4（活性自检正反两态）— PASS
正态：`python .../liveness-selfcheck.py` → `OK liveness-selfcheck: 哨兵 deny 注入成功且统计 +1（before=0 after=1）`，`c4-pass exit=0`；账本「活性自检失败」计数 `0`（无新增）。
反态（停用 hooks：PreToolUse 空路由面板）→ `c4-off exit=1`，stderr：
```
SELF-CHECK FAIL: ["hooks 面板不在册或无 write-guard 路由 'D:/t04-tmp/run/hooks-off.json'"]（呈报码「活性自检失败」入账 hash=715eeba2...）
```
账本「活性自检失败」计数 0→1（新增恰 1 条）。

### 判据 5（freeze 冒烟）— PASS
先置一条活跃租约再 freeze，脚本自计时回显读数原文：
```
FREEZE chain readout:
  1-清租约: ok=True
  2-全写deny: ok=True
  3-终止实例: ok=True
deny−freeze elapsed=0.005s deadline=60.0s -> OK ≤时限
c5 exit=0
```
三步读数齐且 ≤60s；freeze 后写侧联动 deny（test t08 内断言：租约内路径亦 deny）；解冻无人类令牌 exit≠0（表2-2「脚本不得自触发」）。

### 判据 6（B11 冒烟）— PASS
样例下游件含 `memory/session-notes.md` 与 `MEMORY.md` 引用，memory-neutralize scan 回显：
```
HIT ref-scan: 2 处记忆路径引用命中，呈报码「引用扫描命中」入账 hash=68463064d1ee7e73989f8812d4aa18cb7df942bd54929048bd3d4cad858f820e
  D:/t04-tmp/run/downstream.md:3 -> memory
  D:/t04-tmp/run/downstream.md:3 -> MEMORY.md
```

### 判据 7（sign-verify fail-closed 两读数）— PASS
读数①伪造签名：`FAIL sign-verify: gpg --verify 非零（rc=2）: gpg: no valid OpenPGP data found.` → `c7-fake exit=1`。
读数②gpg 缺失环境（--gpg 指向不存在实体）：`FATAL sign-verify: gpg 实体缺席（'D:/t04-tmp/run/no-such-gpg.exe'）→ 硬失败（刻意无降级）` → `c7-nogpg exit=3`。
两读数均落「签字」记录类 verify_fail（test t12 断言恰 2 条）。

### 判据 8（测试件退出 0）— PASS
`python deliverables/experts/baigong-software-team/tests/s4/test_enforcement.py` →
13 项全 PASS（t01–t13），`c8 exit=0`。

### 判据 9（派生一致性断言）— PASS（测试内断言 t13_derived_consistency）
读数：seat-permissions-hooks-map.json 席位集 `{host, product, architect, qa, engineer}` ⊆ seat-permissions.json 六席位集；每席位 deny_globs 非空且与源件逐席位全等（派生面禁改写）；头部 `derived_from: "seat-permissions.json (表2-1)"` 在位。人类席位不入 hooks 映射＝设计语义（表2-2 人类直通触点＝人类直通，hooks 强制面不作用人类），映射件内已注。

### 附：B8 影子重放冒烟（判据外补充读数）
样例存档件含过程痕迹词族＋不可达引用 → `HIT shadow-replay: 词族命中=2 引用命中=1 -> exit≠0`；差异三分类 JSON 落盘（missing_in_replay=[]／missing_in_ledger＝账本未归属提交集／mismatch=[]）。白名单指针三形态（设计锚/哈希/治理域路径）豁免面在 t 面生效。

## 候裁点单列（不自行拍）

- **Q-04**：P4 运行时读数＝inconclusive（probe-results.json 实测读数 `"P4": {"status": "inconclusive"}`）→ write-guard 主路（stdin 直读）与退路（SubagentStart 状态文件）**双形并列同交付、缺省走主路不启用退路**；退路是否启用候裁 Q-04。
- **Q-05**：P6 读数＝inconclusive → freeze 退路「逐席显式 deny 列表」配置面已实现（freeze-state.json `per_seat_deny` 键），`fallback_enabled: false` 缺省走主路；是否启用候裁 Q-05。
- **B7 密钥根生成/轮换**：人类离线自持动作，票内只交付验证侧脚本与验签记录入账，未代拍。

## 异常路由登记

- 本次无门禁真拦（commit 前 pre-commit/run-gates 正常通过，未使用 --no-verify）。
- 施工期自纠两处（非闸拦，属开发期缺陷自闭合）：①commit-audit/memory-neutralize CLI 注入面在场时仍读 stdin 导致测试阻塞→改为注入参数在场不读 stdin；②freeze-unfreeze `load_json(None)` TypeError→签名放宽 `str | None`。
- 呈核项：`tests/probes/results/probe-results.json` 读数 P4/P5/P6/P8＝inconclusive 与本票双形并列口径一致，无冲突。

## commit 对账口径

单独一笔，`collab:` 前缀，`git show --name-only` 应含且仅含上列 11 件。
