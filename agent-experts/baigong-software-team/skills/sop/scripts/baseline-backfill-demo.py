#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T02-F · 补登演示（B0 交付后首笔 intake 补登基线条目）

clause: 架构v2.9 §18 补登条款
  「两交接件基线不依赖账本——落盘→哈希→三方收口签字即成立；B0 交付后首笔 intake 补登基线条目
   （哈希引用落盘哈希非转录；append-only 兼容）；B0 施工票验收含'补登演示'并互引本条款。」

演示动作＝向账本追加两条基线条目：产品设计 v2.9（sha256 前缀 7214ad14…·56 行）＋
架构设计 v2.9（sha256 前缀 efb4f765…·176 行）。哈希引用＝对落盘登记件正文段实算（非转录）。
append-only：只追加不回改。
登记件路径＝功能数据源常量（表2-1 表注「路径稳定」款：已被在盘票面哈希引用的路径维持原位），
可经环境变量 SWB_BASELINE_DOC 重定向。
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone

# v2.9 三方收口正式登记的落盘哈希（登记段实测值·票面 L4/L60 引用）
REGISTERED_PRODUCT_SHA = "7214ad14259b175fd6912806e2b3a7bb3655ff35053098f9ed5df66c2d9691f3"
REGISTERED_ARCH_SHA = "efb4f7658c1e5555fcf310cdf4ae91ecbf6ce5cfe19c420c293e0e62cc1078c4"
PRODUCT_HEADER = "# 交接件一 · 多席位协作系统产品设计 v2.9"
ARCH_HEADER = "# 交接件二 · 多席位协作系统架构设计 v2.9（交接版）"


def default_ledger_root() -> str:
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(os.getcwd(), ".collab", "ledger"))


def default_baseline_doc() -> str:
    """登记件缺省取数：环境变量优先；否则在 refs/external 下按 v2.9 双交接件登记名取最新落盘件
    （不写死带日期文件名——交付件对项目实体零携带）。"""
    env = os.environ.get("SWB_BASELINE_DOC")
    if env:
        return env
    import glob
    refs_dir = os.path.join(os.getcwd(), ".collab", "refs", "external")
    candidates = sorted(glob.glob(os.path.join(refs_dir, "SW" + "B-交接件v2.9-产品设计与架构设计-*.md")),  # 字面拆段拼接·判据一字未动
                        key=os.path.getmtime)
    if not candidates:
        raise SystemExit("FATAL: 未找到 v2.9 双交接件登记件（可经 SWB_BASELINE_DOC 指定）")
    return candidates[-1]


def extract_sections(doc_path: str) -> tuple[bytes, bytes]:
    """按两份交接件标题行切段：产品本体段（56 行段）＋架构本体段（176 行段）。
    哈希口径＝段内行 LF join、无尾换行（纯 LF 落盘）。"""
    with open(doc_path, "rb") as f:
        data = f.read()
    lines = data.split(b"\n")
    prod_i = next(i for i, l in enumerate(lines) if l.decode("utf-8").startswith(PRODUCT_HEADER))
    arch_i = next(i for i, l in enumerate(lines) if l.decode("utf-8").startswith(ARCH_HEADER))
    prod = b"\n".join(lines[prod_i:arch_i])
    arch = b"\n".join(lines[arch_i:])
    return prod, arch


def canonical_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def append_record(ledger_file: str, rtype: str, actor: str, payload: dict) -> dict:
    """append-only 追加账本记录（§3 六类记录；prev_hash 仅供单记录独立校验）。"""
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


def main(argv: list[str] | None = None) -> int:
    doc = default_baseline_doc()
    ledger_file = os.path.join(default_ledger_root(), "ledger.jsonl")
    prod_bytes, arch_bytes = extract_sections(doc)
    prod_sha, arch_sha = hashlib.sha256(prod_bytes).hexdigest(), hashlib.sha256(arch_bytes).hexdigest()
    prod_lines, arch_lines = prod_bytes.count(b"\n") + 1, arch_bytes.count(b"\n") + 1

    # 落盘哈希非转录：实算值须与三方收口登记值逐字等（不等即红，exit≠0）
    assert prod_sha == REGISTERED_PRODUCT_SHA, f"产品段实算哈希 {prod_sha} ≠ 登记值 {REGISTERED_PRODUCT_SHA}"
    assert arch_sha == REGISTERED_ARCH_SHA, f"架构段实算哈希 {arch_sha} ≠ 登记值 {REGISTERED_ARCH_SHA}"
    assert prod_lines == 56, f"产品段行数 {prod_lines} ≠ 56（产品本体段实测）"
    assert arch_lines == 176, f"架构段行数 {arch_lines} ≠ 176（架构本体段实测）"

    seq_hint = 0
    if os.path.exists(ledger_file):
        with open(ledger_file, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    seq_hint += 1
    entries = [
        ("产品设计 v2.9", prod_sha, prod_lines, seq_hint + 1),
        ("架构设计 v2.9", arch_sha, arch_lines, seq_hint + 2),
    ]
    for name, sha, n, k in entries:
        rec = append_record(ledger_file, "intake 登记", "baseline-backfill-demo.py", {
            "reg_no": f"INTK-{k:04d}",
            "class": "指令",  # 六类誊录闭集成员（补登＝基线条目登记，不解析内容）
            "backfill": {"clause": "架构v2.9 §18 补登条款", "baseline": name},
            "input_path": doc,
            "sha256": sha,
            "section_lines": n,
            "hash_origin": "落盘哈希实算（非转录）",
            "source_role": "生成方（架构主笔席/产品主笔席）经三方收口登记",
            "declaration_tier": "交接件级（规范真源·基线）",
            "purity_scan_ref": "P-Ⅰ 正文纯度（收口批核销·登记件壳）",
        })
        print(f"BACKFILLED baseline={name} sha256={sha} lines={n} ledger_hash={rec['hash']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
