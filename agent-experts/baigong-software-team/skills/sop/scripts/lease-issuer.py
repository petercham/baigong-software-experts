#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T02-D · B2 租约签发（消费面声明①「租约段实例化←表2-1」落点）

规范锚点：架构 v2.9 §9 B2 行（输出{票ID·路径集·席位ID·哈希}入账；租约段自表2-1 实例化）／
§17 租约词条＋租约段词条（经架构签注由 B2 实例化）／§7 架构纪律「租约签注唯一生产权」。
实例化源＝config/seat-permissions.json 逐席位行（行集＝表2-1 v2.9 版六席位行逐行转录）。
签发输出＝{ticket_id, path_globs, seat_id, hash} 四字段 JSON 入账；countersign（架构签注）必填——
未签注件签发请求 exit≠0。deny_globs 由 seat-permissions 供 T04 B5 消费（校验实体在 T04）。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

LEASE_KEYS = ["ticket_id", "path_globs", "seat_id", "hash"]  # §17 租约词条四字段
COUNTERSIGN_SIGNER = "architect"  # §7 架构纪律：租约签注唯一生产权＝架构席


def pack_root() -> str:
    # 本件居 skills/sop/scripts/ 下，上溯四级＝包根 .../baigong-software-team
    d = os.path.abspath(__file__)
    for _ in range(4):
        d = os.path.dirname(d)
    return d


def project_root() -> str:
    """SWB-B4 B4-B 两级锚换代＝项目根锚（与 write-guard.py 同款 helper）：
    自包根上溯首个含 `docs/STRUCTURE.md` 的目录＝项目根；探针缺位退回落包根（fail-safe）。"""
    d = pack_root()
    while True:
        if os.path.isfile(os.path.join(d, "docs", "STRUCTURE.md")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return pack_root()
        d = parent


def default_ledger_root() -> str:
    # 账本根缺省＝<项目根>/.collab/ledger（SWB_LEDGER_ROOT 覆写语义零动）
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(project_root(), ".collab", "ledger"))


def load_seats(config_path: str) -> list[dict]:
    with open(config_path, encoding="utf-8") as f:
        data = json.load(f)
    seats = data["seats"]
    if len(seats) != 6:
        raise SystemExit(f"FATAL: seat-permissions 席位行数={len(seats)} ≠ 表2-1 六席位行")
    return seats


def canonical_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def issue_lease(ticket_id: str, seat_id: str, countersign: str | None, config_path: str,
                leases_file: str, requested_globs: list[str] | None = None) -> dict:
    """实例化＝从 seat-permissions 该席位行取写域 path_globs；架构签注缺席→exit≠0。"""
    if not countersign or not countersign.strip():
        print(f"REJECT: 租约未签注（countersign 缺席）——租约段经架构签注由 B2 实例化（§17/§7），拒签发 ticket={ticket_id}", file=sys.stderr)
        raise SystemExit(2)
    if not countersign.startswith(f"{COUNTERSIGN_SIGNER}:") or len(countersign.split(":", 1)[1].strip()) == 0:
        print("REJECT: countersign 签注人非架构席或签注值空（租约签注唯一生产权＝架构席·§7）", file=sys.stderr)
        raise SystemExit(2)

    seats = load_seats(config_path)
    seat = next((s for s in seats if s["seat_id"] == seat_id), None)
    if seat is None:
        print(f"REJECT: 席位 {seat_id!r} 不在表2-1 六席位行内", file=sys.stderr)
        raise SystemExit(2)

    domain = seat["write_globs"]
    if requested_globs is None:
        path_globs = list(domain)
    else:
        # 零裁量子集校验：请求路径集每一项须命中该席位写域行（项目根字面锚定·表注路径锚定款
        # 随 SWB-B4 B4-B 两级锚换代；行为零变化款：描述行在旧式 `d in g` 比对下亦恒不命中）
        for g in requested_globs:
            if not any(g == d or g.startswith(d.rstrip("/")) or d in g for d in domain):
                print(f"REJECT: 请求路径 {g!r} 越出席位 {seat_id} 写域行（表2-1 实例化源），拒签发", file=sys.stderr)
                raise SystemExit(2)
        path_globs = list(requested_globs)

    lease = {"ticket_id": ticket_id, "path_globs": path_globs, "seat_id": seat_id}
    lease["hash"] = hashlib.sha256(canonical_json(
        {"ticket_id": lease["ticket_id"], "path_globs": lease["path_globs"], "seat_id": lease["seat_id"]}
    ).encode("utf-8")).hexdigest()

    os.makedirs(os.path.dirname(leases_file), exist_ok=True)
    entry = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "lease": lease,                       # 四字段本体（§17 租约词条）
        "countersign": countersign,           # 架构签注字段（必填·§7）
        "instantiated_from": os.path.relpath(config_path, pack_root()).replace("\\", "/"),
    }
    with open(leases_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return lease


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B2 租约签发（租约段←表2-1 实例化·架构签注必填）")
    ap.add_argument("--ticket", required=True, help="票ID")
    ap.add_argument("--seat", required=True, help="席位ID（host/product/architect/qa/engineer/human）")
    ap.add_argument("--countersign", default=None,
                    help="架构签注字段，形如 architect:<sig>（缺席或非架构席→exit≠0·§7）")
    ap.add_argument("--path-glob", action="append", default=None,
                    help="请求路径集（可重复；缺省＝该席位写域全行；须为写域子集）")
    ap.add_argument("--config", default=os.path.join(pack_root(), "config", "seat-permissions.json"))
    ap.add_argument("--leases", default=os.path.join(default_ledger_root(), "leases.jsonl"))
    a = ap.parse_args(argv)
    lease = issue_lease(a.ticket, a.seat, a.countersign, a.config, a.leases, a.path_glob)
    print(json.dumps(lease, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
