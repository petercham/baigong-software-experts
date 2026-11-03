#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T04-E · B10 停刀（freeze/unfreeze/revoke·人类直通触点专用）

规范锚点：架构 v2.9 §9 B10 行逐字动作链「freeze 清租约 → 全写 matcher 置 deny → 终止实例」；
表2-2（V13 L98）「冻结/解冻/吊销发起＝人类直通触点｜B10（脚本不得自触发）」——本脚本无自动
触发路径，unfreeze/revoke 入口带人类令牌校验（校验锚缺席＝fail-closed 拒）；
§13（V13 L186）成值时限「停刀时限＝deny−freeze≤60s（缺省，C1 可调）」——缺省 60，可配；
§4/§17 紧急直通三通道之首＝一键冻结→B10。

P6（deny 跨席位一致性）读数＝inconclusive（tests/probes/results/probe-results.json）——
票面纪律镜像 §10：主路（全局 freeze-state 单点 deny）与退路（逐席显式 deny 列表配置面）
双形并列同交付、缺省走主路；退路启用候裁 Q-05，本脚本不自行拍板。

动作链落盘形态：
  ①清租约＝租约台账追加 cleared 行（write-guard 消费时其后租约全失效）；
  ②全写 deny＝freeze-state.json deny_all_writes=true（write-guard 消费联动）＋
    退路配置面 per_seat_deny 列表（双形并列，缺省主路生效）；
  ③终止实例＝对活跃席位逐一落「实例终止请求」记录（有 --instance-state 且记录 pid 时
    best-effort os.kill，失败如实登记不假称终止）。
运行落盘一律可重定向：--ledger/--leases/--freeze-state 与 SWB_LEDGER_ROOT；仓内零运行残留。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import signal
import sys
import time
from datetime import datetime, timezone

DEFAULT_DENY_DEADLINE_S = 60.0  # §13 V13 L186：deny−freeze≤60s（缺省，可配但缺省即 60）

EXIT_HUMAN_TOKEN_INVALID = 2  # 人类令牌校验失败/缺席（表2-2 脚本不得自触发→fail-closed）
EXIT_DEADLINE_EXCEEDED = 3   # deny−freeze 超时限（成值时限违约如实登记）


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


def load_json(path: str | None, default):
    if path and os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def active_seats(map_path: str) -> list[str]:
    cfg = load_json(map_path, {})
    return [row["seat_id"] for row in cfg.get("seats", [])]


def verify_human_token(token: str | None, token_anchor: str) -> tuple[bool, str]:
    """人类令牌校验：--human-token 的 sha256 须命中人类保管的校验锚文件（锚内一行一 sha256）。
    锚缺席/令牌缺席/不命中 → fail-closed 拒（解冻/吊销仅人类直通触点触发·表2-2 V13 L98）。"""
    if not token or not token.strip():
        return False, "人类令牌缺席（unfreeze/revoke 仅人类直通触点触发，脚本不得自触发）"
    if not os.path.exists(token_anchor):
        return False, f"人类令牌校验锚缺席 {token_anchor!r}（fail-closed 拒）"
    with open(token_anchor, encoding="utf-8") as f:
        anchors = {l.strip().lower() for l in f if l.strip()}
    digest = hashlib.sha256(token.encode("utf-8")).hexdigest()
    if digest not in anchors:
        return False, "人类令牌与校验锚不命中（拒）"
    return True, "人类令牌校验通过（人类直通触点）"


def do_freeze(a: argparse.Namespace) -> int:
    t0 = time.monotonic()
    steps: list[dict] = []

    # ① freeze 清租约（§9 B10 行逐字第一步）
    cleared = 0
    if os.path.exists(a.leases):
        with open(a.leases, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    e = json.loads(line)
                    if isinstance(e.get("lease"), dict) and not e.get("cleared"):
                        cleared += 1
    os.makedirs(os.path.dirname(os.path.abspath(a.leases)), exist_ok=True)
    with open(a.leases, "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                            "cleared": True, "cleared_count_prior": cleared,
                            "by": "freeze-unfreeze.py freeze"}, ensure_ascii=False) + "\n")
    steps.append({"step": "1-清租约", "cleared_lease_records": cleared, "ok": True})

    # ② 全写 matcher 置 deny（主路＝全局 freeze-state；退路＝逐席显式 deny 列表·候裁 Q-05 双形并列）
    seats = active_seats(a.map)
    state = {
        "frozen": True,
        "deny_all_writes": True,                      # 主路配置面（write-guard 消费）
        "per_seat_deny": {s: True for s in seats},     # 退路配置面（逐席显式 deny 列表·缺省不生效）
        "fallback_enabled": False,                    # 候裁 Q-05：缺省不启用退路
        "frozen_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "action_chain": "freeze 清租约 → 全写 matcher 置 deny → 终止实例（§9 B10 行逐字）",
    }
    os.makedirs(os.path.dirname(os.path.abspath(a.freeze_state)), exist_ok=True)
    with open(a.freeze_state, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    steps.append({"step": "2-全写deny", "deny_all_writes": True,
                  "seats_in_per_seat_list": seats, "ok": True})

    # ③ 终止实例（best-effort：有实例台账则 kill 并如实登记，无台账则落终止请求记录）
    inst = load_json(a.instance_state, {})
    kills: list[dict] = []
    for seat, pid in sorted(inst.items()):
        try:
            os.kill(int(pid), signal.SIGTERM)
            kills.append({"seat": seat, "pid": pid, "result": "SIGTERM sent"})
        except Exception as e:
            kills.append({"seat": seat, "pid": pid, "result": f"failed: {e}"})
    append_record(a.ledger, "呈报", "freeze-unfreeze.py", {
        "event": "b10_freeze", "steps": steps, "instance_terminations": kills,
        "clause": "§9 B10 行动作链＋表2-2 人类直通触点发起（一键冻结＝紧急直通三通道之首）",
    })
    steps.append({"step": "3-终止实例", "terminations": kills,
                  "note": "实例台账缺席时＝终止请求已落账，平台实例终止属 L0 能力面" if not kills else "ok",
                  "ok": True})

    elapsed = time.monotonic() - t0
    ok_deadline = elapsed <= a.deny_deadline_s
    print("FREEZE chain readout:")
    for s in steps:
        print(f"  {s['step']}: ok={s['ok']}")
    print(f"deny−freeze elapsed={elapsed:.3f}s deadline={a.deny_deadline_s}s -> {'OK ≤时限' if ok_deadline else 'EXCEEDED'}")
    if not ok_deadline:
        append_record(a.ledger, "呈报", "freeze-unfreeze.py", {
            "event": "freeze_deadline_exceeded", "elapsed_s": round(elapsed, 3),
            "deadline_s": a.deny_deadline_s, "clause": "§13 V13 L186 停刀时限 deny−freeze≤60s",
        })
        return EXIT_DEADLINE_EXCEEDED
    return 0


def do_unfreeze(a: argparse.Namespace) -> int:
    ok, why = verify_human_token(a.human_token, a.token_anchor)
    if not ok:
        print(f"REJECT unfreeze: {why}", file=sys.stderr)
        return EXIT_HUMAN_TOKEN_INVALID
    state = load_json(a.freeze_state, {})
    if not state.get("frozen"):
        print("REJECT unfreeze: 当前非冻结态（无可解冻）", file=sys.stderr)
        return 1
    state["frozen"] = False
    state["deny_all_writes"] = False
    state["unfrozen_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(a.freeze_state, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    append_record(a.ledger, "签字", "freeze-unfreeze.py", {
        "event": "b10_unfreeze", "human_direct": True,
        "clause": "解冻仅人类直通触点（表2-2 V13 L98）；令牌校验通过留痕",
    })
    print("OK unfreeze: freeze-state 解除，写侧 deny 联动撤销（人类直通触点）")
    return 0


def do_revoke(a: argparse.Namespace) -> int:
    ok, why = verify_human_token(a.human_token, a.token_anchor)
    if not ok:
        print(f"REJECT revoke: {why}", file=sys.stderr)
        return EXIT_HUMAN_TOKEN_INVALID
    state = load_json(a.freeze_state, {})
    state["revoked"] = True
    state["revoked_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(a.freeze_state, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    append_record(a.ledger, "呈报", "freeze-unfreeze.py", {
        "event": "b10_revoke", "human_direct": True,
        "clause": "吊销仅人类直通触点（表2-2 V13 L98）",
    })
    print("OK revoke: 冻结态吊销入账（人类直通触点）")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B10 停刀（freeze 动作链＋人类令牌门禁解冻/吊销·主退双形）")
    ap.add_argument("action", choices=["freeze", "unfreeze", "revoke"])
    ap.add_argument("--human-token", default=None, help="人类令牌（unfreeze/revoke 必填·表2-2 人类直通触点）")
    ap.add_argument("--token-anchor", default=os.path.join(default_ledger_root(), "..", "human", "b10-token-anchors"),
                    help="令牌校验锚文件（人类保管·一行一 sha256；缺席＝fail-closed）")
    ap.add_argument("--deny-deadline-s", type=float, default=DEFAULT_DENY_DEADLINE_S,
                    help="成值时限（§13 V13 L186 缺省 60s，C1 可调）")
    ap.add_argument("--map", default=os.path.join(pack_root(), "config", "seat-permissions-hooks-map.json"))
    ap.add_argument("--leases", default=os.path.join(default_ledger_root(), "leases.jsonl"))
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    ap.add_argument("--freeze-state", default=os.path.join(default_ledger_root(), "freeze-state.json"))
    ap.add_argument("--instance-state", default=None, help="席位→实例 pid 台账 JSON（终止实例 best-effort 读数源）")
    a = ap.parse_args(argv)
    if a.action == "freeze":
        return do_freeze(a)
    if a.action == "unfreeze":
        return do_unfreeze(a)
    return do_revoke(a)


if __name__ == "__main__":
    sys.exit(main())
