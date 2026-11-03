#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S2 施工测试实体 · 租约实例化（B2 租约签发←表2-1 实例化·消费面①）——三段式（表2-2）。

覆盖：租约四字段闭集＝{ticket_id,path_globs,seat_id,hash}；架构签注必填（§7 唯一生产权）；
seat-permissions 六席位行＝表2-1 行数；工程师行「明确不可写」含仓根 tests/ 真源域条款转录；
deny_globs 数组在位（T04 B5 消费数据源）；promote-manifest 哈希校验形态。
"""
from __future__ import annotations

import importlib.util
import json
import os
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.dirname(os.path.dirname(HERE))
SCRIPTS = os.path.join(PACK, "skills", "sop", "scripts")
CONFIG = os.path.join(PACK, "config", "seat-permissions.json")


def load_script(name: str):
    path = os.path.join(SCRIPTS, name)
    spec = importlib.util.spec_from_file_location(name.replace("-", "_").replace(".py", ""), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lease_mod = load_script("lease-issuer.py")
promote_mod = load_script("promote-manifest.py")


def t01_lease_four_keys_exact(tmp: str) -> None:
    leases = os.path.join(tmp, "leases.jsonl")
    lease = lease_mod.issue_lease("TKT-S1", "engineer", "architect:sig-001", CONFIG, leases)
    assert sorted(lease.keys()) == sorted(["ticket_id", "path_globs", "seat_id", "hash"]), \
        f"租约四键闭集不符：{sorted(lease.keys())}"
    with open(leases, encoding="utf-8") as f:
        entry = json.loads(f.readline())
    assert entry["countersign"] == "architect:sig-001"
    assert entry["lease"] == lease


def t02_missing_countersign_rejected(tmp: str) -> None:
    leases = os.path.join(tmp, "leases2.jsonl")
    try:
        lease_mod.issue_lease("TKT-S2", "engineer", None, CONFIG, leases)
        raise AssertionError("未签注件签发未被拒")
    except SystemExit as e:
        assert e.code != 0
    assert not os.path.exists(leases) or os.path.getsize(leases) == 0


def t03_non_architect_countersign_rejected(tmp: str) -> None:
    leases = os.path.join(tmp, "leases3.jsonl")
    try:
        lease_mod.issue_lease("TKT-S3", "engineer", "qa:sig-002", CONFIG, leases)
        raise AssertionError("非架构席签注未被拒（§7 租约签注唯一生产权）")
    except SystemExit as e:
        assert e.code != 0


def t04_six_seats_match_table21(tmp: str) -> None:
    with open(CONFIG, encoding="utf-8") as f:
        d = json.load(f)
    assert len(d["seats"]) == 6
    assert d["derived_from"] == "表2-1"
    names = [s["seat"] for s in d["seats"]]
    assert names == ["主理人", "产品", "架构", "QA", "工程师", "人类"]


def t05_engineer_row_transcription(tmp: str) -> None:
    with open(CONFIG, encoding="utf-8") as f:
        d = json.load(f)
    eng = next(s for s in d["seats"] if s["seat"] == "工程师")
    # v2.9 表2-1 工程师行「明确不可写」列随转录（含仓根 tests/ 真源域括注）
    assert any("仓根 tests/" in x and "架构/QA 共写域" in x for x in eng["explicitly_not_writable"])
    assert isinstance(eng["deny_globs"], list) and len(eng["deny_globs"]) >= 1  # T04 B5 消费面数据源
    # 双层双址条款在头部表注
    assert "判据真源双层双址" in d["table_notes"]
    assert "deliverables/**/tests/**" in d["table_notes"]["判据真源双层双址"]


def t06_path_subset_gate(tmp: str) -> None:
    leases = os.path.join(tmp, "leases6.jsonl")
    # 请求越出席位写域 → 拒（零裁量子集判定）
    try:
        lease_mod.issue_lease("TKT-S6", "product", "architect:sig-006", CONFIG, leases,
                              requested_globs=["docs/xxx"])
        raise AssertionError("越写域路径集未被拒")
    except SystemExit as e:
        assert e.code != 0
    lease = lease_mod.issue_lease("TKT-S6", "product", "architect:sig-006", CONFIG, leases,
                                  requested_globs=[".collab/drafts/prd/"])
    assert lease["path_globs"] == [".collab/drafts/prd/"]


def t07_promote_manifest_hash_gate(tmp: str) -> None:
    draft = os.path.join(tmp, "draft.md")
    with open(draft, "w", encoding="utf-8") as f:
        f.write("验证通过的草稿\n")
    real = promote_mod.sha256_file(draft)
    docs = os.path.join(tmp, "docs")
    man_ok = os.path.join(tmp, "manifest_ok.json")
    with open(man_ok, "w", encoding="utf-8") as f:
        json.dump({"entries": [{"draft": draft, "sha256": real, "dest": "final.md"}]}, f, ensure_ascii=False)
    assert promote_mod.promote(man_ok, docs) == 0
    assert os.path.isfile(os.path.join(docs, "final.md"))
    # 篡改草稿 → exit≠0 且 docs 无新增
    with open(draft, "a", encoding="utf-8") as f:
        f.write("篡改\n")
    docs_before = sorted(os.listdir(docs))
    man_bad = os.path.join(tmp, "manifest_bad.json")
    with open(man_bad, "w", encoding="utf-8") as f:
        json.dump({"entries": [{"draft": draft, "sha256": real, "dest": "final2.md"}]}, f, ensure_ascii=False)
    rc = promote_mod.promote(man_bad, docs)
    assert rc != 0
    assert sorted(os.listdir(docs)) == docs_before


def run_self() -> int:
    tests = [t01_lease_four_keys_exact, t02_missing_countersign_rejected,
             t03_non_architect_countersign_rejected, t04_six_seats_match_table21,
             t05_engineer_row_transcription, t06_path_subset_gate,
             t07_promote_manifest_hash_gate]
    for t in tests:
        with tempfile.TemporaryDirectory() as tmp:
            t(tmp)
        print(f"PASS {t.__name__}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_self())
