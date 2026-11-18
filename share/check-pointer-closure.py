#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: ADR-2026-10-30-04
# spec_file: agent-skills/object-audit/references/50-document.md
# spec_anchor: D6-3 | 交付包指针闭集
# spec_clause_sha256: 2ffcbacb3c9b07b60576f0d99409eb5c889f81ce88ac3f3607422d66a010dee2
# spec_version: 0.6
# spec_effective: 2026-10-30
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: ADR-2026-10-30-05
# spec_file: agent-skills/object-audit/references/50-document.md
# spec_anchor: D6-4 | 交付包内指针可达性
# spec_clause_sha256: 7baa37b870148da0b90f21093fd1431346c88984fb71dd30672a830a10a07892
# spec_version: 0.6
# spec_effective: 2026-10-30
# provider: object-audit
# --- /spec-provenance ---
#
# ENG-G2 WP-3：交付包引用可达性机检（OA-D6-3 指针闭集／OA-D6-4 包内可达性）。
#
# 条款真源（只指路径，不复写正文）：
#   OA-D6-3 → object-audit/references/50-document.md D6 表 D6-3 行（交付包指针闭集）
#   OA-D6-4 → 同上 D6-4 行（包内反引号相对指针以包根解析可达）
#
# 扫描面（缺省＝两包面，裁③＋SWB-B2 换代）：agent-skills/external-advisor-collab/ ＋ agent-experts/（软开 bundle）。
# `--pkg <dir>`（可重复）＝显式指入其他交付态包面（跨仓组件包/装配预览面），给出即取代缺省。
# `.collab/**` 与其余规范件不进扫描面（扫描面收窄＝主豁免）。
#
# 铁律遵守：本件**只输出**「严重度＋spec_id＋位置＋一句话」，不决定拦不拦——拦放由路由表定。
# 豁免三范式（循 check-collab-lint 成文号）：
#   ①扫描面收窄（主豁免）；②行级豁免标记〔史实锚〕/〔豁免注…/T-<名>-<n> → EXEMPT；
#   ③反引号段与代码围栏内示例 → SUBSTR（禁模式引用不被禁模式杀掉·自咬反例必测）。
#
# 本件只读：不写任何文件。唯一写动作在 run-gates.sh（出口②）。
"""ENG-G2 交付包指针闭集与可达性机检（OA-D6-3／OA-D6-4）。

用法：
    python check-pointer-closure.py [--root <仓根>] [--pkg <包目录>]... [--selftest]
    --pkg 可重复；给出时扫描面＝所列包面（相对 --root 或绝对），缺省＝两包面。
    --selftest：对包内对拍测试件跑两检查，与内嵌预期数比对（命中数＝预期数才算绿）。

退出码（闭集，见 60-gates.md「六、退出码闭集」）：
    0 通过（零发现；或 --selftest 对拍全等）／1 违规（≥1 发现或对拍不符）
    2 用法错／4 基础设施错
"""

from __future__ import annotations

import argparse
import os
import re
import sys

SEV_WATCH = "WATCH"

# ---- OA-D6-3 四模式（设计稿 §2.3·案卷组不重叠以免双计，见注）----
# 案卷标识拆三条互斥子模式：日期段-序号（含 a/b 后缀形态）／案卷卷号 txt／复盘案引用目录名。
# 不取「-0\d\d」独立子式：其为日期段子集，并行会双计同串（初版探针实测双计）。
PATTERNS = [
    ("P1 出包案面路径", r"\.collab/"),
    ("P2 盘符路径", r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]"),  # 前缀形态即判（较 check-entity 更宽：交付态任何盘符前缀都违例）
    ("P3 宿主家目录", r"(?:~/|\.workbuddy/)"),
    ("P4 案卷标识", r"(?:2026\d{4}[a-z]?-\d{3}|\d{3}\.txt|reference-2026)"),
]
# 行级豁免标记（照 check-collab-lint EXEMPT_MARK_RE 成文号：T- 带左界防 GPT-4 类泄漏）
EXEMPT_MARK_RE = re.compile(r"〔史实锚〕|〔豁免注|(?<![A-Za-z0-9])T-[A-Za-z0-9-]*\d[A-Za-z0-9-]*")
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")
FENCE_RE = re.compile(r"^[ \t]*```")

# ---- OA-D6-4 可达性：反引号内带目录段的 .md/.py 相对指针（裸基名＝提及嫌疑不判，循裁-21）----
POINTER_RE = re.compile(r"`([A-Za-z0-9_\-./\u4e00-\u9fff]+\.(?:md|py))`")

# 缺省扫描面＝两包面（裁③：其余包 `--pkg` 逐包扩面）
DEFAULT_PKG_FACES = ("agent-skills/external-advisor-collab", "agent-experts")
SCAN_EXTS = (".md", ".txt", ".py", ".sh", ".json", ".lock", ".state")


def die_usage(msg: str) -> "None":
    sys.stderr.write("usage error: %s\n" % msg)
    raise SystemExit(2)


def find_root(explicit: str | None) -> str:
    if explicit:
        if not os.path.isdir(explicit):
            die_usage("--root 不存在：%s" % explicit)
        return os.path.abspath(explicit)
    cur = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isdir(os.path.join(cur, "share")) and any(
                os.path.isdir(os.path.join(cur, c)) for c in ("agent-experts", "agent-skills", "softwares")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            die_usage("未能定位仓根；请用 --root 指定")
        cur = parent


def read_lines(path: str) -> "list[str]":
    # CRLF 归一：本仓 core.autocrlf=true，检出件本身是 CRLF（与同侪脚本同口径）
    try:
        with open(path, "r", encoding="utf-8", errors="replace", newline="") as handle:
            return handle.read().replace("\r\n", "\n").split("\n")
    except OSError as exc:
        sys.stderr.write("infra error: 读取失败 %s: %s\n" % (path, exc))
        raise SystemExit(4)


def resolve_faces(root: str, pkgs: "list[str]") -> "list[str]":
    faces: "list[str]" = []
    for p in pkgs or list(DEFAULT_PKG_FACES):
        abs_p = p if os.path.isabs(p) else os.path.join(root, p.replace("/", os.sep))
        if not os.path.isdir(abs_p):
            die_usage("包面不存在：%s" % p)
        faces.append(os.path.abspath(abs_p))
    return faces


def iter_files(faces: "list[str]") -> "list[str]":
    out: "list[str]" = []
    for face in faces:
        for cur, dirs, files in os.walk(face):
            # SWB-GTFAST S1-b：.workbuddy 目录名整词划界（任何深度皆剪＝运行时记忆面不入扫描域；只剪目录段恰等者）
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".workbuddy")]
            for name in files:
                if name.endswith(SCAN_EXTS):
                    out.append(os.path.join(cur, name))
    return sorted(out)


def check_closure(rel: str, lines: "list[str]") -> "tuple[list[str], dict[str, int]]":
    """OA-D6-3：四模式逐行扫（豁免②行级→EXEMPT；豁免③遮除→SUBSTR）。"""
    findings: "list[str]" = []
    tally = {"EXEMPT": 0, "SUBSTR": 0, "VIOLATION": 0}
    in_fence = False
    for lineno, raw in enumerate(lines, 1):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        # 遮除行级一次算（循 check-entity mask 口径）
        masked = CODE_SPAN_RE.sub(lambda m: "\x00" * len(m.group(0)), raw)
        for label, pat in PATTERNS:
            for match in re.finditer(pat, raw):
                if EXEMPT_MARK_RE.search(raw):
                    tally["EXEMPT"] += 1
                    continue
                if in_fence or match.group(0) not in masked:
                    tally["SUBSTR"] += 1
                    continue
                tally["VIOLATION"] += 1
                findings.append("%s:%d: %s OA-D6-3 交付包面出包指针命中 %s＝%r（指针只准包内闭环）"
                                % (rel, lineno, SEV_WATCH, label, match.group(0)[:60]))
    return findings, tally


def check_reach(rel: str, path: str, face_root: str) -> "list[str]":
    """OA-D6-4：反引号带目录段 .md/.py 相对指针可达性。

    解析口径＝从所在文件目录**逐级上溯至包面根**（bundle 面内嵌多技能包，
    合法包内指针可在 bundle 根解析；越过包面根即出包——出包形态交 D6-3 模式面）。
    全程落空＝违例。
    """
    findings: "list[str]" = []
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError as exc:
        sys.stderr.write("infra error: 读取失败 %s: %s\n" % (rel, exc))
        raise SystemExit(4)
    face_abs = os.path.abspath(face_root)
    cur_dir = os.path.dirname(os.path.abspath(path))
    for match in POINTER_RE.finditer(text):
        tok = match.group(1)
        if "/" not in tok or tok.startswith("/") or "<" in tok or ":" in tok:
            continue  # 裸基名＝提及嫌疑（裁-21）；占位/绝对/盘符交 D6-3 模式面处理
        if any(re.search(pat, tok) for _label, pat in PATTERNS):
            continue  # token 本身即出包形态（案面/案卷号）＝交 OA-D6-3 模式面处理，不双计
        relp = tok.replace("/", os.sep)
        resolved = False
        d = cur_dir
        while len(d) >= len(face_abs) and d.startswith(face_abs):
            if os.path.isfile(os.path.join(d, relp)):
                resolved = True
                break
            parent = os.path.dirname(d)
            if parent == d:
                break
            d = parent
        if resolved:
            continue
        lineno = text.count("\n", 0, match.start()) + 1
        findings.append("%s:%d: %s OA-D6-4 包内指针不可达（所在目录上溯至包面根全程解析落空）：%r"
                        % (rel, lineno, SEV_WATCH, tok))
    return findings


def face_of(path: str, faces: "list[str]") -> str:
    ap = os.path.abspath(path)
    for face in faces:
        if ap.startswith(face + os.sep):
            return face
    return os.path.dirname(ap)


def scan(root: str, faces: "list[str]",
         targets: "list[str] | None" = None) -> "tuple[list[str], dict[str, int]]":
    files = iter_files(faces)
    if targets:
        # SWB-GTFAST S2-d 靶检：既有文件枚举结果按 abspath 交集过滤
        # （判据函数本体零调用路径改动＝只换入参文件集；交集空＝零发现汇总 exit 0）。
        tset = {os.path.abspath(t) for t in targets}
        files = [p for p in files if os.path.abspath(p) in tset]
    findings: "list[str]" = []
    tally = {"EXEMPT": 0, "SUBSTR": 0, "VIOLATION": 0}
    for path in files:
        face = face_of(path, faces)
        rel = os.path.relpath(path, face).replace(os.sep, "/")
        lines = read_lines(path)
        f3, t3 = check_closure(rel, lines)
        findings.extend(f3)
        for k in tally:
            tally[k] += t3[k]
        if path.endswith(".md"):
            findings.extend(check_reach(rel, path, face))
    return findings, tally


# 对拍预期（--selftest 与内嵌预期比对；改 fixture 必须同步改这里，否则对拍红）
EXPECTED = {"OA-D6-3": 4, "OA-D6-4": 1,
            "EXEMPT": 2, "SUBSTR": 4, "VIOLATION": 4}


def selftest(root: str) -> int:
    fix = os.path.join(root, "agent-skills", "object-audit",
                       "tests", "fixtures", "pointer-closure")
    if not os.path.isdir(fix):
        sys.stderr.write("infra error: 对拍测试件不存在：%s\n" % fix)
        return 4
    faces = [os.path.abspath(fix)]
    findings, tally = scan(root, faces)
    got = {"OA-D6-3": 0, "OA-D6-4": 0}
    for line in findings:
        for key in got:
            if " " + key + " " in line:
                got[key] += 1
    print("selftest 对拍件＝%s" % os.path.relpath(fix, root).replace(os.sep, "/"))
    for line in findings:
        print("  %s" % line)
    ok = True
    for key in ("OA-D6-3", "OA-D6-4"):
        mark = "MATCH" if got[key] == EXPECTED[key] else "MISMATCH"
        print("  分账 %s＝%d（预期 %d）%s" % (key, got[key], EXPECTED[key], mark))
        ok = ok and got[key] == EXPECTED[key]
    for key in ("EXEMPT", "SUBSTR", "VIOLATION"):
        mark = "MATCH" if tally[key] == EXPECTED[key] else "MISMATCH"
        print("  三态 %s＝%d（预期 %d）%s" % (key, tally[key], EXPECTED[key], mark))
        ok = ok and tally[key] == EXPECTED[key]
    print("selftest %s" % ("PASS（自咬反例判绿：EXEMPT/SUBSTR 均不计违规）" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv: "list[str]") -> int:
    parser = argparse.ArgumentParser(add_help=True, description="ENG-G2 交付包指针闭集与可达性机检")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    parser.add_argument("--pkg", action="append", default=[],
                        help="交付包面（可重复；给出即取代缺省两包面）")
    parser.add_argument("--selftest", action="store_true", help="对包内对拍测试件跑两检查并与预期数比对")
    parser.add_argument("--target", action="append", default=[],
                        help="靶检文件（可重复；给出＝既有枚举按 abspath 交集过滤＝只换入参文件集；"
                             "交集空＝零发现汇总 exit 0；目录参数＝用法错）")
    args = parser.parse_args(argv)

    root = find_root(args.root)
    if args.selftest:
        return selftest(root)

    faces = resolve_faces(root, args.pkg)
    if args.target:
        for tgt in args.target:
            if os.path.isdir(tgt):
                die_usage("--target 只收文件，目录请走 --pkg 扩面：%s" % tgt)
        findings, tally = scan(root, faces, targets=args.target)
    else:
        files = iter_files(faces)
        if not files:
            sys.stderr.write("infra error: 扫描域为空（包面下无待扫文件）\n")
            return 4
        findings, tally = scan(root, faces)
    counts = {k: sum(1 for f in findings if " " + k + " " in f) for k in ("OA-D6-3", "OA-D6-4")}
    for key, n in counts.items():
        print("spec=%s count=%d" % (key, n))
    print("分账：EXEMPT(豁免标记行·绿)=%d  SUBSTR(围栏/反引号内示例·判非违例)=%d  VIOLATION(包面真命中)=%d"
          % (tally["EXEMPT"], tally["SUBSTR"], tally["VIOLATION"]))
    for line in findings:
        print(line)
    return 1 if findings else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed
        sys.stderr.write("infra error: %s\n" % exc)
        raise SystemExit(4)
