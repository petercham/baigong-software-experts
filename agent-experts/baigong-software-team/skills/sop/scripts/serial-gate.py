#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T03-C · B3 串行闸（消费面声明⑤「串行/派发←表2-2/§4」落点）

规范锚点：架构 v2.9 §4「执行期全系统一票活跃，新派发被串行闸拒绝」；
§9 B3 行「活跃票非零拒绝派发」；表2-2「票内工作：工程师，一票一新鲜实例，票间串行」。
读数源＝账本活跃票计数（states 登记面：节点 1–6 为活跃态；挂起/完结非活跃——挂起＝治理级停态·§17）。
活跃≠0 时任何派发请求 exit≠0 且写「呈报」类审计事件（恰一条，供 dispatch-builder 复用本函数不重复写）。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

# 活跃态集＝六节点在制态（§4）；挂起/完结不计活跃
NODE_STATES = {1, 2, 3, 4, 5, 6}


def default_ledger_root() -> str:
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(os.getcwd(), ".collab", "ledger"))


def canonical_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def append_record(ledger_file: str, rtype: str, actor: str, payload: dict) -> dict:
    """append-only 追加账本记录（六类记录·§3；与 B2 同形制，prev_hash 仅供单记录独立校验）。"""
    os.makedirs(os.path.dirname(ledger_file), exist_ok=True)
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


def load_states(states_file: str) -> dict:
    if os.path.exists(states_file):
        with open(states_file, encoding="utf-8") as f:
            return json.load(f)
    return {}


def active_tickets(states_file: str) -> list[str]:
    """活跃票计数读数源：states 中处于节点 1–6 在制态的票 ID 列表。"""
    states = load_states(states_file)
    return sorted(tid for tid, info in states.items()
                  if isinstance(info, dict) and info.get("state") in NODE_STATES)


def check_gate(states_file: str, ledger_file: str, request_ticket: str,
               actor: str = "serial-gate.py") -> tuple[int, dict | None]:
    """串行闸判定：活跃≠0 → 写「呈报」类审计事件恰一条并返回 (活跃数, 记录)；活跃=0 → (0, None)。

    调用方（dispatch-builder）负责 exit≠0；本函数保证呈报留痕恰一次，不重复写。
    """
    actives = active_tickets(states_file)
    if not actives:
        return 0, None
    rec = append_record(ledger_file, "呈报", actor, {
        "event": "serial_gate_reject",
        "request_ticket": request_ticket,
        "active_tickets": actives,
        "active_count": len(actives),
        "clause": "§4 执行期全系统一票活跃，新派发被串行闸拒绝（B3）",
    })
    return len(actives), rec


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B3 串行闸（活跃票非零拒绝派发·§4/§9 B3）")
    ap.add_argument("--ticket", required=True, help="请求派发的票ID")
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    ap.add_argument("--states", default=os.path.join(default_ledger_root(), "states.json"))
    a = ap.parse_args(argv)

    n, rec = check_gate(a.states, a.ledger, a.ticket)
    if n > 0:
        print(f"REJECT serial-gate ticket={a.ticket}: 活跃票={n} 非零，新派发被串行闸拒绝"
              + (f"（呈报记录 hash={rec['hash']}）" if rec else ""), file=sys.stderr)
        return 2
    print(f"OK serial-gate ticket={a.ticket}: 活跃票=0，串行闸放行")
    return 0


if __name__ == "__main__":
    sys.exit(main())
