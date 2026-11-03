#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T04-H · B7 签名验证（gpg 封装·fail-closed·刻意无降级）

规范锚点：架构 v2.9 §9 B7 行「gpg，人类离线自持（验签记录居 .collab/signatures/、签名件落
.collab/human/reviews/）｜退路：刻意无降级（fail-closed）」；§11 密钥根行——密钥生成/保管＝
人类离线自持动作，不在票内；票内只交付验证侧脚本与验签记录入账。

fail-closed 语义（无降级路径）：
  gpg 不可用（--gpg 指向的实体缺席或调用失败非验签原因可归）→ exit≠0 硬失败；
  签名无效/摘要不符 → exit≠0；
  身份锚比对：验签出的 uid/keyid 须命中人类保管的身份锚文件（一行一 uid/keyid），
  锚缺席或不命中 → exit≠0（信任根平台外自持·§1 接缝合同④）。
验签通过/失败均落「签字」记录类（验签记录入账·.collab/signatures/ 语义＝记录面）。
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

EXIT_NO_GPG = 3        # gpg 缺失＝硬失败（刻意无降级）
EXIT_VERIFY_FAILED = 1  # 验签失败/身份锚不符
EXIT_USAGE = 2


def default_ledger_root() -> str:
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(os.getcwd(), ".collab", "ledger"))


def canonical_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def append_record(ledger_file: str, rtype: str, actor: str, payload: dict) -> dict:
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
        "type": rtype, "actor": actor, "payload": payload, "prev_hash": prev_hash,
    }
    rec["hash"] = hashlib.sha256(
        f'{rec["seq"]}\n{rec["ts"]}\n{rec["type"]}\n{rec["actor"]}\n{canonical_json(rec["payload"])}\n{prev_hash}'.encode("utf-8")
    ).hexdigest()
    with open(ledger_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def gpg_available(gpg: str) -> bool:
    if os.path.sep in gpg or (os.altsep and os.altsep in gpg):
        return os.path.isfile(gpg)
    from shutil import which
    return which(gpg) is not None


def verify(signed_file: str, signature_file: str, gpg: str, keyring: str | None) -> tuple[bool, str]:
    """gpg --verify 封装：返回 (验签成立?, 验签人读数)。无降级：任何异常路径均 (False, 原因)。"""
    cmd = [gpg]
    if keyring:
        cmd += ["--no-default-keyring", "--keyring", keyring]
    cmd += ["--verify", signature_file, signed_file]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except FileNotFoundError:
        return False, "gpg 实体缺席（fail-closed 硬失败，无降级）"
    except Exception as e:
        return False, f"gpg 调用异常: {e}"
    err = r.stderr or ""
    if r.returncode != 0:
        return False, f"gpg --verify 非零（rc={r.returncode}）: {err.strip()[:200]}"
    # 验签人读数：gpg stderr 中 gpg: Good signature from "<uid>"
    import re as _re
    m = _re.search(r'Good signature from "([^"]+)"', err)
    uid = m.group(1) if m else ""
    return True, uid


def check_anchor(uid: str, anchor_file: str) -> tuple[bool, str]:
    """身份锚比对：验签 uid/keyid 须命中人类保管的身份锚（信任根平台外自持·§11）。"""
    if not os.path.exists(anchor_file):
        return False, f"身份锚文件缺席 {anchor_file!r}（fail-closed）"
    with open(anchor_file, encoding="utf-8") as f:
        anchors = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    for a in anchors:
        if a and (a == uid or a in uid):
            return True, f"uid={uid!r} 命中身份锚 {a!r}"
    return False, f"uid={uid!r} 不在身份锚闭集（拒）"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B7 验签（gpg 封装·fail-closed 无降级·验签记录入账）")
    ap.add_argument("--signed", required=True, help="签名件正文（.collab/human/reviews/ 形态）")
    ap.add_argument("--signature", required=True, help="detached 签名文件（.sig）")
    ap.add_argument("--gpg", default="gpg", help="gpg 实体路径（测试可指向不存在路径验证 fail-closed）")
    ap.add_argument("--keyring", default=None, help="验签 keyring（人类公钥环·自持）")
    ap.add_argument("--identity-anchor", default=os.path.join(default_ledger_root(), "..", "signatures", "identity-anchors"),
                    help="身份锚文件（一行一 uid/keyid·人类保管）")
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    a = ap.parse_args(argv)

    if not gpg_available(a.gpg):
        # 刻意无降级：gpg 缺失＝硬失败，禁 fallback
        append_record(a.ledger, "签字", "sign-verify.py", {
            "event": "verify_fail", "reason": "gpg unavailable", "signed": a.signed,
            "clause": "§9 B7 行 fail-closed：gpg 不可用→exit≠0 硬失败，禁 fallback",
        })
        print(f"FATAL sign-verify: gpg 实体缺席（{a.gpg!r}）→ 硬失败（刻意无降级）", file=sys.stderr)
        return EXIT_NO_GPG

    ok, uid = verify(a.signed, a.signature, a.gpg, a.keyring)
    if not ok:
        append_record(a.ledger, "签字", "sign-verify.py", {
            "event": "verify_fail", "reason": uid, "signed": a.signed,
            "clause": "验签失败（伪造签名/摘要不符）→ exit≠0",
        })
        print(f"FAIL sign-verify: {uid}", file=sys.stderr)
        return EXIT_VERIFY_FAILED

    anchor_ok, anchor_why = check_anchor(uid, a.identity_anchor)
    if not anchor_ok:
        append_record(a.ledger, "签字", "sign-verify.py", {
            "event": "verify_fail", "reason": anchor_why, "signed": a.signed, "uid": uid,
            "clause": "身份锚比对失败（信任根平台外自持·§11）",
        })
        print(f"FAIL sign-verify: {anchor_why}", file=sys.stderr)
        return EXIT_VERIFY_FAILED

    append_record(a.ledger, "签字", "sign-verify.py", {
        "event": "verify_ok", "uid": uid, "signed": a.signed,
        "clause": "§9 B7 行：验签＋身份锚比对成立，验签记录入账（签名信任根本体不入仓·§11）",
    })
    print(f"OK sign-verify: uid={uid!r} 验签＋身份锚比对通过（记录入账）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
