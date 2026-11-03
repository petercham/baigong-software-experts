#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T02-G · 转正代写（表2-1 主理人行／表注转正代写条款·V13 L79 落点）

条款本体（表2-1 表注）：转正代写＝状态机脚本将验证通过的草稿按 manifest 声明复制入 `docs/`
并附来源哈希的唯一合法写入形态；代写主体＝状态机脚本，非任何 LLM 席位。
manifest 文件由账本域保管（表2-1 主理人可写域 `.collab/manifest/`）；
校验草稿哈希＝manifest 声明哈希后方复制，不符 exit≠0。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def promote(manifest_path: str, docs_root: str) -> int:
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)
    entries = manifest.get("entries", [])
    if not entries:
        print("REJECT: manifest 无条目", file=sys.stderr)
        return 2
    # 先全量校验，全部通过后才落盘（任一不符→零写入 exit≠0）
    verified = []
    for i, e in enumerate(entries):
        draft, declared, dest = e["draft"], e["sha256"], e["dest"]
        if not os.path.isfile(draft):
            print(f"REJECT: 草稿不存在 {draft!r}", file=sys.stderr)
            return 2
        actual = sha256_file(draft)
        if actual != declared:
            print(f"REJECT: 草稿哈希不符 manifest 声明 draft={draft!r} actual={actual} declared={declared}", file=sys.stderr)
            return 2
        dest_abs = os.path.normpath(os.path.join(docs_root, dest))
        if not dest_abs.startswith(os.path.normpath(docs_root) + os.sep):
            print(f"REJECT: 目标越出 docs 根 {dest!r}", file=sys.stderr)
            return 2
        verified.append((draft, actual, dest_abs))
    for draft, actual, dest_abs in verified:
        os.makedirs(os.path.dirname(dest_abs), exist_ok=True)
        shutil.copyfile(draft, dest_abs)
        print(f"PROMOTED draft={draft} sha256={actual} dest={dest_abs}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="转正代写（manifest 校验后机械复制入 docs/）")
    ap.add_argument("--manifest", required=True, help="manifest 清单文件（账本域保管·声明草稿→docs 映射与来源哈希）")
    ap.add_argument("--docs-root", default=os.path.join(os.getcwd(), "docs"),
                    help="docs 根（缺省＝仓根 docs/；测试/冒烟可重定向）")
    a = ap.parse_args(argv)
    return promote(a.manifest, a.docs_root)


if __name__ == "__main__":
    sys.exit(main())
