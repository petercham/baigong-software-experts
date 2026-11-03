#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T04-D · B5 活性自检（先注入必中事件再读统计·§17 活性自检词条）

规范锚点：§17「活性自检＝先注入必中事件再读统计」；§13 指标异常闭集第二项＝「活性自检失败」
（真源＝decision-pack.py L42 TRIG_LIVENESS_FAIL）。
形态＝经 write-guard.py --sentinel 注入一条必然 deny 的哨兵写请求（哨兵路径无租约可命中→必 deny）
→ 读账本：哨兵 deny 计数 +1 且 hooks 面板（hooks.json）在册 → 断言通过；
失败 → 写「活性自检失败」呈报码（恰一条）＋ exit≠0。

hooks 在位判定（停用 hooks 场景＝判据 4 反例面）：--hooks 指向的 hooks.json 缺席，
或其 PreToolUse 段不含 write-guard 路由 → 视为 hooks 停用。
运行落盘一律可重定向：--ledger 与 SWB_LEDGER_ROOT；仓内零运行残留。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

TRIGGER_LIVENESS_FAIL = "活性自检失败"  # §13 指标异常闭集第二项（真源 decision-pack.py L42）

EXIT_SELF_CHECK_FAILED = 1


def pack_root() -> str:
    d = os.path.abspath(__file__)
    for _ in range(4):
        d = os.path.dirname(d)
    return d


def default_ledger_root() -> str:
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(os.getcwd(), ".collab", "ledger"))


def canonical_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def append_record(ledger_file: str, rtype: str, actor: str, payload: dict) -> dict:
    """append-only 追加账本记录（六类记录·§3；与 B2/B3 同形制）。"""
    os.makedirs(os.path.dirname(os.path.abspath(ledger_file)), exist_ok=True)
    prev_hash, seq = "GENESIS", 0
    if os.path.exists(ledger_file):
        with open(ledger_file, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    rec = json.loads(line)
                    prev_hash, seq = rec["hash"], rec["seq"]
    rec = {
        "seq": seq + 1,
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "type": rtype,
        "actor": actor,
        "payload": payload,
        "prev_hash": prev_hash,
    }
    rec["hash"] = hashlib.sha256(
        f'{rec["seq"]}\n{rec["ts"]}\n{rec["type"]}\n{rec["actor"]}\n{canonical_json(rec["payload"])}\n{prev_hash}'.encode("utf-8")
    ).hexdigest()
    with open(ledger_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def sentinel_count(ledger_file: str) -> int:
    """统计读数：账本中哨兵 deny 事件计数。"""
    n = 0
    if os.path.exists(ledger_file):
        with open(ledger_file, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    if r["type"] == "写入" and r["payload"].get("event") == "liveness_sentinel":
                        n += 1
    return n


def hooks_in_place(hooks_file: str) -> bool:
    """hooks 面板在位判定：文件在册且 PreToolUse 段含 write-guard 路由。"""
    if not os.path.exists(hooks_file):
        return False
    with open(hooks_file, encoding="utf-8") as f:
        try:
            h = json.load(f)
        except json.JSONDecodeError:
            return False
    blob = json.dumps(h, ensure_ascii=False)
    return "write-guard" in json.dumps(h.get("hooks", {}).get("PreToolUse", [])) or "write-guard" in blob


def run_selfcheck(ledger_file: str, hooks_file: str, write_guard: str) -> int:
    reasons: list[str] = []
    if not hooks_in_place(hooks_file):
        reasons.append(f"hooks 面板不在册或无 write-guard 路由 {hooks_file!r}")
    if not os.path.exists(write_guard):
        reasons.append(f"write-guard.py 缺席 {write_guard!r}")

    before = sentinel_count(ledger_file)
    deny_observed = False
    if not reasons:
        # 注入必中事件：哨兵 deny（无租约状态下哨兵路径必 deny）
        r = subprocess.run(
            [sys.executable, write_guard, "--sentinel", "--ledger", ledger_file,
             "--leases", os.path.join(os.path.dirname(os.path.abspath(ledger_file)), "leases.jsonl"),
             "--freeze-state", os.path.join(os.path.dirname(os.path.abspath(ledger_file)), "freeze-state.json")],
            input=json.dumps({"session_id": "liveness-selfcheck", "agent_type": "software-engineer",
                              "agent_id": "liveness-selfcheck"}),
            capture_output=True, text=True, timeout=60)
        deny_observed = '"permissionDecision":"deny"' in r.stdout
        after = sentinel_count(ledger_file)
        if not deny_observed:
            reasons.append(f"哨兵 deny 输出缺席（stdout={r.stdout[:120]!r}）")
        if after != before + 1:
            reasons.append(f"哨兵统计计数未 +1（before={before} after={after}）")

    if reasons:
        rec = append_record(ledger_file, "呈报", "liveness-selfcheck.py", {
            "event": "trigger_report", "trigger_source": TRIGGER_LIVENESS_FAIL,
            "reasons": reasons,
            "clause": "§13 指标异常闭集第二项；§17 活性自检＝先注入必中事件再读统计",
        })
        print(f"SELF-CHECK FAIL: {reasons}（呈报码「活性自检失败」入账 hash={rec['hash']}）", file=sys.stderr)
        return EXIT_SELF_CHECK_FAILED
    print(f"OK liveness-selfcheck: 哨兵 deny 注入成功且统计 +1（before={before} after={before + 1}）")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B5 活性自检（哨兵注入→统计断言·失败写呈报码）")
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    ap.add_argument("--hooks", default=os.path.join(pack_root(), "hooks", "hooks.json"))
    ap.add_argument("--write-guard", default=os.path.join(pack_root(), "skills", "sop", "scripts", "write-guard.py"))
    a = ap.parse_args(argv)
    return run_selfcheck(a.ledger, a.hooks, a.write_guard)


if __name__ == "__main__":
    sys.exit(main())
