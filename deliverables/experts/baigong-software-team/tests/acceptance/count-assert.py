#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SWB-T06-C · 制度④「计数即断言」机检器（违纪模式表行 10 落点）

规范锚点：产品 §4 违纪模式表行 10「计数/数字声明失实（含完备性断言失实）→ 制度④计数即断言＋
制度⑥完备即断言」（V13 L39＝物理 L67）；架构 §16 制度④「计数即断言——数字声明与事实断言同纪律」
（V13 L199＝物理 L227）；§7 验收核验「无裸纪律」（V13 L141＝物理 L169）。
票包总览 §七 申报「交叉验第二实现＝T06 交付后由其 count-assert.py 模式1/3 重跑同一断言」。

三模式：
  模式1 票面闭集解析：定位 `- 声明闭集：` 锚行→计数其后连续 `- <路径>` 裸路径条目行→
        与票面申报数 N（--expect，或从票清单表反查）比对，不符 exit≠0；缺声明＝SKIP 不算绿。
  模式2 无裸纪律计数：扫描席位卡纪律段纪律行（`- ` 起行），缺 `G[1-5]` 标注即计裸纪律，非零 exit≠0。
  模式3 总览映射表行数比对：票清单表申报闭集件数 vs 各票实物锚行条目数，两实现交叉验
        （实现A＝状态机逐行；实现B＝锚段正则整段提取）；行数断言（消费面10/构件12/违纪16/候裁7）同检。

计数口径声明：occurrence 口径（逐条目计数，非 grep -c 行数口径）；本脚本输出逐项读数供回执引用。
本脚本＝生成方产出，不自判合格（制度③）——结论权归 QA/CI 面。
"""
from __future__ import annotations

import argparse
import os
import re
import sys

ANCHOR = "- 声明闭集："
EXIT_MISMATCH = 1
EXIT_NO_DECLARATION = 2  # SKIP 面：缺声明不算绿（非零 exit 如实呈现）


def entry_line(line: str) -> bool:
    """裸路径条目行判定：`- ` 起行且其后为非空单段路径字面（无表格竖线、无中文冒号断言）。"""
    s = line.strip()
    if not s.startswith("- "):
        return False
    body = s[2:].strip()
    if not body or body.startswith(("#", "|", ">")):
        return False
    # 路径条目＝可解析为相对路径字面：以字母/点起始，不含全角冒号「：」
    return bool(re.match(r"^[A-Za-z.][^\uFF1A|]*$", body))


# ---- 实现A：状态机逐行扫描 ----
def closure_entries_impl_a(text: str) -> list[str] | None:
    lines = text.splitlines()
    idx = [i for i, l in enumerate(lines) if l.strip() == ANCHOR]
    if not idx:
        return None
    entries: list[str] = []
    for l in lines[idx[0] + 1:]:
        if entry_line(l):
            entries.append(l.strip()[2:].strip())
        elif not l.strip():
            continue  # 空行不中断条目段
        else:
            break
    return entries


# ---- 实现B：锚段正则整段提取（与实现A独立路径·交叉验用） ----
def closure_entries_impl_b(text: str) -> list[str] | None:
    m = re.search(re.escape(ANCHOR) + r"\n((?:- [^\n]*\n?|\n)+)", text)
    if not m:
        return None
    out: list[str] = []
    for l in m.group(1).splitlines():
        if l.strip() and entry_line(l):
            out.append(l.strip()[2:].strip())
    return out


def table_body_rows(text: str, header_pat: str) -> list[list[str]]:
    """markdown 表体行提取（header_pat 命中标题后的首个表：跳过 |---| 分隔行）。"""
    lines = text.splitlines()
    hi = next((i for i, l in enumerate(lines) if re.search(header_pat, l)), None)
    if hi is None:
        return []
    rows: list[list[str]] = []
    started = False
    for l in lines[hi + 1:]:
        s = l.strip()
        if s.startswith("|"):
            if re.match(r"^\|[ :_|-]+\|$", s):
                started = True
                continue
            if started:
                rows.append([c.strip() for c in s.strip("|").split("|")])
        elif started:
            break
    return rows


def mode1(ticket_path: str, expect: int | None) -> int:
    with open(ticket_path, encoding="utf-8") as f:
        text = f.read()
    ea = closure_entries_impl_a(text)
    if ea is None:
        print(f"SKIP mode1 {ticket_path}: 锚行 {ANCHOR!r} 缺席（缺声明＝SKIP 不算绿）", file=sys.stderr)
        return EXIT_NO_DECLARATION
    n = len(ea)
    if expect is None:
        print(f"mode1 {ticket_path}: 实数={n}；申报数缺席（--expect 未给）→ SKIP 不算绿", file=sys.stderr)
        return EXIT_NO_DECLARATION
    eb = closure_entries_impl_b(text)
    cross = (eb is not None and len(eb) == n)
    print(f"mode1 {ticket_path}: 申报={expect} 实数(实现A)={n} 交叉(实现B)={len(eb) if eb is not None else 'MISS'} "
          f"cross_ok={cross}")
    if not cross:
        print("FAIL mode1: 两实现计数不一致（计数双实现交叉验失败）", file=sys.stderr)
        return EXIT_MISMATCH
    if expect != n:
        print(f"FAIL mode1: 申报 {expect} ≠ 实数 {n}（计数即断言·违纪行10）", file=sys.stderr)
        return EXIT_MISMATCH
    print("PASS mode1: 申报＝实数（occurrence 口径）")
    return 0


def mode2(cards: list[str]) -> int:
    bare_total = 0
    for card in cards:
        with open(card, encoding="utf-8") as f:
            lines = f.read().splitlines()
        in_disc = False
        total = 0
        bare: list[str] = []
        for l in lines:
            if re.match(r"^##+ .*(纪律|红线|铁律)", l):
                in_disc = True
                continue
            if re.match(r"^##+ ", l):
                in_disc = False
                continue
            if in_disc and l.strip().startswith("- "):
                total += 1
                if not re.search(r"G[1-5]", l):
                    bare.append(l.strip()[:60])
        bare_total += len(bare)
        print(f"mode2 {os.path.basename(card)}: 纪律行={total} 裸纪律={len(bare)}")
        for b in bare:
            print(f"  BARE: {b}")
    if bare_total:
        print(f"FAIL mode2: 裸纪律总数={bare_total}（§7「无裸纪律」验收·违纪行8）", file=sys.stderr)
        return EXIT_MISMATCH
    print("PASS mode2: 裸纪律总数=0（occurrence 口径）")
    return 0


def mode3(overview_path: str, tickets_dir: str) -> int:
    with open(overview_path, encoding="utf-8") as f:
        text = f.read()
    ok = True
    # (a) 四映射表行数断言（总览 §七 申报值＝对照基准）
    expected_rows = [("消费面声明十项", r"消费面声明十项", 10),
                     ("§9 十构件", r"十构件（B0–B11", 12),
                     ("违纪模式闭集表", r"违纪模式闭集表", 16),
                     ("候裁点清单", r"候裁点清单", 7)]
    for name, pat, exp in expected_rows:
        rows = table_body_rows(text, pat)
        verdict = "OK" if len(rows) == exp else "FAIL"
        if verdict == "FAIL":
            ok = False
        print(f"mode3(a) {name}: 映射表体行数={len(rows)} 申报={exp} -> {verdict}")
    # (b) 票清单申报件数 vs 各票实物锚行条目数（两实现交叉验）
    trows = table_body_rows(text, r"^\| 票号 \| 文件名")
    trows = [r for r in trows if re.match(r"^T\d{2}$", r[0])]
    if len(trows) != 6:
        print(f"mode3(b) FAIL: 票清单表体行数={len(trows)} ≠ 6", file=sys.stderr)
        ok = False
    for row in trows:
        tid, fname, declared = row[0], row[1], int(row[3])
        path = os.path.join(tickets_dir, fname)
        if not os.path.isfile(path):
            print(f"mode3(b) {tid}: FAIL 实物缺席 {path}", file=sys.stderr)
            ok = False
            continue
        with open(path, encoding="utf-8") as f:
            ttxt = f.read()
        ea = closure_entries_impl_a(ttxt)
        eb = closure_entries_impl_b(ttxt)
        na = len(ea) if ea is not None else -1
        nb = len(eb) if eb is not None else -1
        verdict = "OK" if (na == declared == nb) else "FAIL"
        if verdict == "FAIL":
            ok = False
        print(f"mode3(b) {tid}: 申报={declared} 实物(实现A)={na} 实物(实现B)={nb} -> {verdict}")
    # (c) 总件数断言
    total_decl = sum(int(r[3]) for r in trows if re.match(r"^T\d{2}$", r[0]) and r[3].isdigit())
    total_actual = 0
    for row in trows:
        path = os.path.join(tickets_dir, row[1])
        if os.path.isfile(path):
            with open(path, encoding="utf-8") as f:
                ea = closure_entries_impl_a(f.read())
            total_actual += len(ea) if ea is not None else 0
    verdict = "OK" if total_decl == total_actual == 65 else "FAIL"
    if verdict == "FAIL":
        ok = False
    print(f"mode3(c) 闭集总件数: 申报={total_decl} 实物={total_actual} 对照基准=65 -> {verdict}")
    if not ok:
        print("FAIL mode3: 映射表行数/实物计数存在不符（计数即断言·违纪行10）", file=sys.stderr)
        return EXIT_MISMATCH
    print("PASS mode3: 行数与实物计数全部相符（两实现交叉验通过·occurrence 口径）")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="制度④计数即断言机检器（模式1/2/3）")
    ap.add_argument("--mode1", default=None, help="票面闭集解析：票据路径")
    ap.add_argument("--expect", type=int, default=None, help="模式1 票面申报数 N")
    ap.add_argument("--mode2", nargs="*", default=None, help="无裸纪律计数：席位卡路径集（缺省＝五席位卡）")
    ap.add_argument("--mode3", default=None, help="总览映射表行数比对：总览件路径")
    a = ap.parse_args(argv)
    rc = 0
    if a.mode1:
        rc |= main1(a)
    if a.mode2 is not None:
        cards = a.mode2 or default_cards()
        rc |= mode2(cards)
    if a.mode3:
        root = repo_root()
        rc |= mode3(a.mode3, os.path.join(root, ".collab", "tickets"))
    if rc == 0 and not (a.mode1 or a.mode2 is not None or a.mode3):
        ap.print_help()
        return EXIT_USAGE_OK
    return rc


def main1(a: argparse.Namespace) -> int:
    return mode1(a.mode1, a.expect)


def default_cards() -> list[str]:
    root = os.path.join(pack_root(), "agents")
    return [os.path.join(root, n) for n in
            ("software-team-lead.md", "software-team-product.md", "software-team-architect.md",
             "software-team-qa.md", "software-team-engineer.md")]


EXIT_USAGE_OK = 0  # 无模式参数＝打印帮助（不算红）


def pack_root() -> str:
    d = os.path.abspath(__file__)
    for _ in range(3):
        d = os.path.dirname(d)
    return d


def repo_root() -> str:
    env = os.environ.get("SWB_REPO_ROOT")
    if env:
        return env
    d = pack_root()
    for _ in range(3):
        d = os.path.dirname(d)
    return d


if __name__ == "__main__":
    sys.exit(main())
