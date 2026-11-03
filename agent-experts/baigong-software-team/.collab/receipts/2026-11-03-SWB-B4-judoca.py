#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SWB-B4 判据落盘脚本（判据 6/7·回执引用位；`.scratch/` 过程域件，不入票面闭集交付面）
# 判据 6：STRUCTURE.md delivery_paths ↔ seat-permissions engineer 机械枚举行逐行相等
#         ＋ project_domain_md 逐字断言 ＋ 各项目 docs/STRUCTURE.md test -f 逐一
#         ＋ hooks-map 同源逐席全等。
# 判据 7：R⑧ 11 桶×席矩阵逐格读数（桶名真源＝B1-D 规范件 grep 引用不复写）
#         ＋ 授权桶∩deny＝∅ ＋ 旧字面 `deliverables/**` occurrence＝0（全 config 域）。
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# ROOT＝自本件位置上溯首个含 `.git` 的目录（仓根；本件住项目 .collab/receipts 桶＝层级不定）
_up = HERE
while not os.path.isdir(os.path.join(_up, ".git")) and os.path.dirname(_up) != _up:
    _up = os.path.dirname(_up)
ROOT = _up
PACK = os.path.join(ROOT, "agent-experts", "baigong-software-team")
CFG = os.path.join(PACK, "config")
SRC = os.path.join(CFG, "seat-permissions.json")
MAPF = os.path.join(CFG, "seat-permissions-hooks-map.json")


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def delivery_paths_of(structure_md_path):
    """STRUCTURE.md YAML 围栏 delivery_paths 抽取（逐行）。"""
    txt = open(structure_md_path, encoding="utf-8").read()
    m = re.search(r"delivery_paths:\n((?:[ \t]*-[ \t]*.+\n?)+)", txt)
    if not m:
        raise AssertionError("delivery_paths 抽取失败：%s" % structure_md_path)
    rows = []
    for ln in m.group(1).splitlines():
        v = ln.strip()[1:].strip().strip("`")
        if v:
            rows.append(v)
    return rows


def c6():
    d = load(SRC)
    eng = next(s for s in d["seats"] if s["seat_id"] == "engineer")
    # 机械枚举行＝write_globs 中非 .collab/ 前缀的交付面行（项目根字面）
    mech = [g for g in eng["write_globs"] if not g.startswith(".collab/")]
    paths = delivery_paths_of(os.path.join(PACK, "docs", "STRUCTURE.md"))
    rows = [p.rstrip("/") + "/**" for p in paths]
    assert rows == mech, "STRUCTURE↔engineer 行不等：%s vs %s" % (rows, mech)
    assert eng["project_domain_md"] == "docs/STRUCTURE.md", \
        "project_domain_md 现值＝%r" % eng["project_domain_md"]
    projects = []
    for cat in ("agent-experts", "agent-skills", "softwares"):
        catdir = os.path.join(ROOT, cat)
        if not os.path.isdir(catdir):
            continue
        for proj in sorted(os.listdir(catdir)):
            p = os.path.join(catdir, proj)
            if os.path.isdir(p):
                projects.append(p)
    missing = [p for p in projects
               if not os.path.isfile(os.path.join(p, "docs", "STRUCTURE.md"))]
    print("c6: delivery_paths=%s" % paths)
    print("c6: engineer 交付面枚举行=%s" % mech)
    print("c6: 逐行相等断言＝全等 OK")
    print("c6: project_domain_md＝docs/STRUCTURE.md（逐字等）OK")
    print("c6: test -f 项目 docs/STRUCTURE.md：项目数 %d／缺 %s"
          % (len(projects), missing or "none"))
    mp = load(MAPF)
    src_deny = {s["seat_id"]: s.get("deny_globs", []) for s in d["seats"]}
    for row in mp["seats"]:
        assert row["deny_globs"] == src_deny[row["seat_id"]], \
            "hooks-map 席位 %s deny_globs 与源件不一致（派生面禁改写）" % row["seat_id"]
    print("c6: hooks-map 同源逐席全等 OK")
    return 1 if missing else 0


def buckets_from_spec():
    """十一桶闭集真源＝B1-D 规范件（grep 引用不复写名录）。"""
    spec = open(os.path.join(PACK, "skills", "sop", "references",
                             "collab-fixed-structure.md"), encoding="utf-8").read()
    m = re.search(r"`(decisions/[^`]+)`", spec)
    if not m:
        raise AssertionError("十一桶闭集抽取失败")
    raw = m.group(1).split("`＋")[0]
    toks = [t.rstrip("/") for t in raw.split() if t.endswith("/")]
    if len(toks) != 11:
        raise AssertionError("桶数=%d ≠ 11: %s" % (len(toks), toks))
    return toks


def glob_hits_bucket(glob_row, bucket):
    """deny/write 行与桶的命中判据（项目根字面＝`.collab/<bucket>/…`）。"""
    return (".collab/" + bucket + "/") in glob_row


def c7():
    buckets = buckets_from_spec()
    print("c7: 桶名闭集（B1-D 真源逐字）=%s（共 %d 桶）" % (buckets, len(buckets)))
    d = load(SRC)
    seats = {s["seat_id"]: s for s in d["seats"]}
    order = ("host", "product", "architect", "qa", "engineer")
    bad = []
    print("c7: 11 桶×席矩阵（A＝write_globs 命中／D＝deny 命中／·＝两不命中）")
    for b in buckets:
        cells = []
        for sid in order:
            s = seats[sid]
            wg = [g for g in s["write_globs"] if glob_hits_bucket(g, b)]
            dg = [g for g in s.get("deny_globs", []) if glob_hits_bucket(g, b)]
            if wg and dg:
                bad.append((sid, b, "A∩D"))
            cell = "A" if wg else ("D" if dg else "·")
            cells.append("%s=%s" % (sid, cell))
        print("  %-10s %s" % (b + "/", " ".join(cells)))
    # engineer 授权子域（R⑧ 销态面）∩ deny 枚举＝∅（写侧 glob 机件实测对表在回执另一节）
    eng = seats["engineer"]
    auth = [".collab/returns/engineer/", ".collab/inbox/engineer/", ".collab/drafts/deploy/"]
    probe_bad = []
    for a in auth:
        probe = a + "x.md"
        for g in eng["deny_globs"]:
            if g.endswith("/**") and probe.startswith(g.rstrip("*").rstrip("/") + "/"):
                probe_bad.append((a, g))
    print("c7: engineer 授权子域∩deny 枚举＝%s" % (probe_bad or "∅（冲突面已消）"))
    # 旧字面 occurrence＝0 断言（全 config 域）
    occ = 0
    for name in sorted(os.listdir(CFG)):
        if not name.endswith(".json"):
            continue
        body = open(os.path.join(CFG, name), encoding="utf-8").read()
        occ += body.count("deliverables/")
    print("c7: config 域旧字面 `deliverables/` occurrence＝%d（判据＝0）" % occ)
    return 1 if (bad or probe_bad or occ) else 0


if __name__ == "__main__":
    rc = c6() | c7()
    print("b4-judoca: exit %d" % rc)
    sys.exit(rc)
