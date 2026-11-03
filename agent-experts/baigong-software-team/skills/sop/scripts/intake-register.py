#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T02-B · B1 intake 登记（誊录登记脚本·零裁量）

规范锚点：架构 v2.9 §9 B1 行／表2-2「人类输入誊录与路由」行（六类誊录闭集＋
外部输入件登记四字段 source_role／declaration_tier／sha256／purity_scan_ref，不做业务解析）。
账本六类记录之「intake 登记」（§3）。

闭集六类誊录类型（B1 六类闭集·不做业务解析）：
  产品需求／审查审计／规则意见／SOP变更／询问／指令
脚本零裁量：不做任何业务解析，只登记与编号；登记号回显。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

# 六类誊录闭集（闭集＝成员判定，非成员拒登；内容一律不解析）
TRANSCRIPTION_CLASSES = ["产品需求", "审查审计", "规则意见", "SOP变更", "询问", "指令"]

RECORD_TYPES = ["派发", "写入", "签字", "注入包哈希", "intake 登记", "呈报"]  # 账本六类（§3）


def default_ledger_root() -> str:
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(os.getcwd(), ".collab", "ledger"))


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_json(obj: dict) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def append_record(ledger_file: str, rtype: str, actor: str, payload: dict) -> dict:
    """append-only 追加一条账本记录（前向哈希链 prev_hash→hash·§3/§17：主信任锚＝git 原生链，
    记录级 prev_hash 仅供单记录独立校验）。"""
    os.makedirs(os.path.dirname(ledger_file), exist_ok=True)
    prev_hash = "GENESIS"
    seq = 0
    if os.path.exists(ledger_file):
        with open(ledger_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    rec = json.loads(line)
                    prev_hash = rec["hash"]
                    seq = rec["seq"]
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


def register_intake(input_path: str, tclass: str, ledger_file: str,
                    source_role: str | None = None, declaration_tier: str | None = None,
                    purity_scan_ref: str | None = None) -> dict:
    """输入＝人类输入原文件路径；输出＝intake 登记记录入账＋登记号。零裁量：不读内容语义，仅取哈希。"""
    if tclass not in TRANSCRIPTION_CLASSES:
        raise SystemExit(f"REJECT: 誊录类型越出六类闭集 {TRANSCRIPTION_CLASSES}，收到＝{tclass!r}")
    if not os.path.isfile(input_path):
        raise SystemExit(f"REJECT: 输入原文件不存在 {input_path!r}")
    file_hash = sha256_file(input_path)
    seq_hint = 0
    if os.path.exists(ledger_file):
        with open(ledger_file, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    seq_hint += 1
    reg_no = f"INTK-{seq_hint + 1:04d}"
    payload = {
        "reg_no": reg_no,
        "class": tclass,               # 六类誊录闭集成员
        "input_path": input_path,
        "sha256": file_hash,           # 四字段之 sha256（落盘哈希非转录）
        "source_role": source_role if source_role is not None else "unspecified",
        "declaration_tier": declaration_tier if declaration_tier is not None else "unspecified",
        "purity_scan_ref": purity_scan_ref if purity_scan_ref is not None else "unspecified",
    }
    return append_record(ledger_file, "intake 登记", "intake-register.py", payload)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B1 intake 登记（零裁量·只登记与编号）")
    ap.add_argument("input_path", help="人类输入原文件路径")
    ap.add_argument("--class", dest="tclass", required=True,
                    help="誊录类型（六类闭集：产品需求／审查审计／规则意见／SOP变更／询问／指令）")
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    ap.add_argument("--source-role", default=None, help="外部输入件四字段·source_role")
    ap.add_argument("--declaration-tier", default=None, help="外部输入件四字段·declaration_tier")
    ap.add_argument("--purity-scan-ref", default=None, help="外部输入件四字段·purity_scan_ref")
    args = ap.parse_args(argv)
    rec = register_intake(args.input_path, args.tclass, args.ledger,
                          args.source_role, args.declaration_tier, args.purity_scan_ref)
    print(f"REGISTERED reg_no={rec['payload']['reg_no']} class={rec['payload']['class']} sha256={rec['payload']['sha256']} hash={rec['hash']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
