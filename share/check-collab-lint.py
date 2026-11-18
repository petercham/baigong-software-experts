#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: ADR-2026-10-30-01
# spec_file: agent-skills/external-advisor-collab/.scratch/tickets/2026-10-30-EAC-SK5-机检票.md
# spec_anchor: ### T1 
# spec_clause_sha256: b5cd89d8a987283e98ba20c40336c8b2973640a31573b6fa621cbdd98fbdadef
# spec_version: 1.0
# spec_effective: 2026-10-30
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: ADR-2026-10-30-02
# spec_file: agent-skills/external-advisor-collab/.scratch/tickets/2026-10-30-EAC-SK5-机检票.md
# spec_anchor: ### T2 
# spec_clause_sha256: dee69ec37a407100bec7983a54851a1fae11d6bc2aef38a37f760dde295a3725
# spec_version: 1.0
# spec_effective: 2026-10-30
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: ADR-2026-10-30-03
# spec_file: agent-skills/external-advisor-collab/.scratch/tickets/2026-10-30-EAC-SK5-机检票.md
# spec_anchor: ### T3 
# spec_clause_sha256: 61766d1e265ddb2168a79734f10818f5c3632fde3b9264799a5652721cead3f6
# spec_version: 1.0
# spec_effective: 2026-10-30
# provider: object-audit
# --- /spec-provenance ---
#
# EAC-SK5：协作纪律体裁机检（EAC-L1／EAC-L2／EAC-L3）。三检查一脚本。
#
# 条款真源（只指路径，不复写正文）：
#   EAC-L1 → external-advisor-collab/references/20-rounds.md §二/§三（收敛类必含
#            「合流与分歧清单」节）＋ 40-artifacts.md §一 收敛类注／§二 新提议登记
#   EAC-L2 → 40-artifacts.md §四之二（件性声明行＝扫描面定位判据·讨论会特有禁列）
#            ＋ multi-collab/references/20-handoff.md §二（三正面判据·通用侧）
#   EAC-L3 → 20-rounds.md §一.5 编号纪律闭集（一包一轮·已分发禁 v2）
#
# 铁律遵守（60-gates.md §〇）：本件**只输出**「严重度＋spec_id＋位置＋一句话」，
# 不决定拦不拦——拦放由路由表定。
#
# 自咬纪律（本件最重要的自我约束）：扫描器必须能引用禁模式而不被禁模式杀掉。
# 本注释与文档串内的禁模式示例一律置于反引号内；L2 对反引号段／代码围栏内的命中
# 判 SUBSTR（判非违例），对行内含豁免标记的命中判 EXEMPT——两者都不计违规。
# 教训来源：check-entity.py 头注记录的「自伤先例」（注释自咬盘符模式）。
#
# 本件只读：不写任何文件。唯一写动作在 run-gates.sh（出口②）。
"""EAC-SK5 协作纪律机检：议题包/汇总体裁（EAC-L1）＋交接件禁模式（EAC-L2）＋编号唯一性（EAC-L3）。

用法：
    python check-collab-lint.py [--root <仓根>] [--selftest] [--fixture-root <目录>]
    --selftest：对包内对拍测试件跑三检查，与内嵌预期数比对（命中数＝预期数才算绿）。

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

# ---- EAC-L1：收敛类议题包必含「合流与分歧清单」节；汇总件头部必含新提议登记字段 ----
CONVERGE_WORDS = ("收敛表态", "签字", "收口确认")
NATURE_KEY = "轮次性质"
MERGE_SECTION = "合流与分歧清单"
HEAD_WINDOW = 20  # 头部声明区窗口（汇总件/议题包的性质声明行均在头部，见票面「头部必含」）
PROPOSAL_KEY = "新提议"
PROPOSAL_ZERO_RE = re.compile(r"新提议[^。\n|]{0,16}?(?:[＝=][^。\n|]{0,6}?(?:无|零)|无新增)")

# ---- EAC-L2：交接件禁模式（五组·初版·照票面字面）----
# EAC-SK5-F 修正（报告黄-1/黄-3）：提案编号与案卷行号补边界前查——
# `\b` 在 CJK（\w）紧邻处失效（`依据P-12` 漏报），改字母负向前查；
# 案卷行号加数字前后查，`2026.md` 不再咬出 `026.md` 假命中。
L2_PATTERNS = [
    ("轮次引用", r"见第\s*\d+\s*轮"),
    ("席轮注源", r"〔[^〕]*·轮〕"),
    ("提案编号", r"(?<![A-Za-z0-9])P-\d+"),
    ("案卷行号", r"(?<!\d)\d{3}\.(?:txt|md)(?![A-Za-z0-9])"),
    ("汇总件节引", r"汇总件\s*§"),
]
# 扫描面定位判据＝件性声明行（40-artifacts.md §四之二 立该体例；此行为机检锚）
DECLARATION_RE = re.compile(r"性质\s*[＝=]\s*(?:交接件|决策件|施工输入)")
# 目录类扫描面（票面：decisions/tickets 目录件）
L2_DIR_SEGS = ("/decisions/", "/tickets/")
# 行级豁免标记（循 check-entity.py L85-89 史实锚范式）：行内含即该行判绿。
# 注：豁免注格式只认「`T-` ＋段中至少含一数字」的标记（如 `T-team-rename-01` 先例），
# 纯字母段（如提案编号 `P-1`／`T-alpha`）不算豁免注——否则豁免面吞掉禁模式自身。
# EAC-SK5-F 修正（报告红-1）：`T-` 加字母数字负向前查（check-entity:64 drive-path 同款
# 教训）——否则 `GPT-4`／`PT-1`／`QT-2024` 这类无关词触发整行豁免，吞掉该行全部禁模式。
EXEMPT_MARK_RE = re.compile(r"〔史实锚〕|〔豁免注|(?<![A-Za-z0-9])T-[A-Za-z0-9-]*\d[A-Za-z0-9-]*")
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")
FENCE_RE = re.compile(r"^[ \t]*```")

# ---- EAC-L3：.discussion/ 内议题包编号唯一性＋同轮 v2 提示 ----
# EAC-SK5-F 修正（报告红-2）：年份前缀去硬编码（原 `2026` 使 2027 起新包静默脱离
# 唯一性分组＝fail-open 时间炸弹），改 `20\d{6}` 八年式闭形态。
PKG_NO_RE = re.compile(r"^(20\d{6})-(\d{3})[.-]")
PKG_NO_RE_CASED = re.compile(r"^(20\d{6}[a-z]?)-(\d{3})[.-]")  # 案名带字母后缀形态（票面初版未列，见回报）
SAME_ROUND_V2_RE = re.compile(r"-0\d\d-.*-v[2-9]")
# 附加件不进唯一性分组：同轮 `NNN.txt`（分发主件）＋`NNN-议题包.md`（同包另一载体）
# 属正常双承载，不是「同编号多包」——不进分组否则每轮都假红（扫描面收窄主豁免口径）。
SUPPLEMENT_RE = re.compile(r"议题包|补发|交接件|质询|裁定|登记|v[2-9]")

# 扫描面排除：对拍测试件是**预期违规样本**，不得混入全仓读数（扫描面收窄＝主豁免的延伸）
FIXTURE_MARK = "/tests/fixtures/"
# `.discussion/` 段判定（首段也算——--selftest 以 fixture 根为 root 时 rel 以段起始）
DISCUSSION_RE = re.compile(r"(^|/)\.discussion/")

SCAN_EXTS = (".md", ".txt")


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
        # 仓根判定（B3a 随动·B2 收口登记候裁②）：deliverables 旧域灭，改同侪同款判定
        if os.path.isdir(os.path.join(cur, "share")) and any(
                os.path.isdir(os.path.join(cur, c)) for c in ("agent-experts", "agent-skills", "softwares")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            die_usage("未能定位仓根；请用 --root 指定")
        cur = parent


def read_lines(path: str) -> "list[str]":
    # CRLF 归一：本仓 core.autocrlf=true，检出件本身是 CRLF（与四同侪脚本同口径）
    try:
        with open(path, "r", encoding="utf-8", errors="replace", newline="") as handle:
            return handle.read().replace("\r\n", "\n").split("\n")
    except OSError as exc:
        sys.stderr.write("infra error: 读取失败 %s: %s\n" % (path, exc))
        raise SystemExit(4)


def iter_files(root: str, skip_fixtures: bool) -> "list[str]":
    # SWB-GTFAST S1-a（v2 修单）扫描域划界＝机械剪枝谓词：
    # ① 目录名为 .collab/.scratch 且相对仓根段数>=2（包内卷宗）剪；
    # ② 根 .collab 不剪照审；③ 根 .scratch 仅 tickets 子树存续，其余剪；
    # ④ .git/__pycache__ 剪枝存续；FIXTURE_MARK 臂与判据函数本体（L1/L2/L3）零动＝只换入扫文件集。
    # SWB-GTFAST S1-b 叠加：.workbuddy 目录名整词任何深度皆剪（运行时记忆面物理划界；只剪目录段恰等者）。
    out: "list[str]" = []
    root_abs = os.path.abspath(root)
    for cur, dirs, files in os.walk(root_abs):
        cur_abs = os.path.abspath(cur)
        rel_dir = os.path.relpath(cur_abs, root_abs).replace(os.sep, "/")
        keep: "list[str]" = []
        for d in dirs:
            if d in (".git", "__pycache__", ".workbuddy"):
                continue
            if d in (".collab", ".scratch"):
                if cur_abs == root_abs:
                    keep.append(d)
                    continue
                segs = (0 if rel_dir == "." else len(rel_dir.split("/"))) + 1
                if segs >= 2 and not (rel_dir == ".scratch" and d == "tickets"):
                    continue
            keep.append(d)
        if rel_dir == ".scratch":
            keep = [d for d in keep if d == "tickets"]
            files = []
        dirs[:] = keep
        if skip_fixtures and FIXTURE_MARK in "/" + rel_dir + "/":
            continue
        for name in files:
            if name.endswith(SCAN_EXTS):
                out.append(os.path.join(cur_abs, name))
    return sorted(out)


def check_l1(rel: str, lines: "list[str]") -> "list[str]":
    """议题包／汇总件体裁（扫描面＝路径含 .discussion/ 或文件名含关键词）。"""
    name = os.path.basename(rel)
    in_scope = bool(DISCUSSION_RE.search(rel)) or ("议题包" in name) or ("汇总意见报告" in name)
    if not in_scope:
        return []
    findings: "list[str]" = []
    head = lines[:HEAD_WINDOW]
    # ① 收敛类议题包必含「合流与分歧清单」节标题
    convergent = any(NATURE_KEY in ln and any(w in ln for w in CONVERGE_WORDS) for ln in head)
    if convergent and not any(MERGE_SECTION in ln for ln in lines):
        idx = next((i for i, ln in enumerate(head, 1) if NATURE_KEY in ln), 1)
        findings.append("%s:%d: %s EAC-L1 收敛类议题包缺「%s」节（新提议登记义务由该节承接）"
                        % (rel, idx, SEV_WATCH, MERGE_SECTION))
    # ② 汇总件头部必含新提议登记字段；值为零另出提示
    if "汇总意见报告" in name:
        hit = next((ln for ln in head if PROPOSAL_KEY in ln), None)
        if hit is None:
            findings.append("%s:1: %s EAC-L1 汇总件头部缺「%s登记」字段（应登记本轮有无新提议）"
                            % (rel, SEV_WATCH, PROPOSAL_KEY))
        elif PROPOSAL_ZERO_RE.search(hit):
            findings.append("%s:1: %s EAC-L1 汇总件登记「新提议＝无」——按 §四 该轮应改出议题件"
                            % (rel, SEV_WATCH))
    return findings


def check_l2(rel: str, lines: "list[str]") -> "tuple[list[str], dict[str, int]]":
    """交接件禁模式：只扫带件性声明行的件＋decisions/tickets 目录件（扫描面收窄＝主豁免）。"""
    # EAC-SK5-F（T6 配套）：`/` 前置口径——rel 首段即目录段时（--selftest 以 fixture 根
    # 为 root：rel＝`tickets/…`）也能命中段判据；与 iter_files 的 FIXTURE_MARK 段判定
    # （`"/" + rel_dir + "/"`）及 DISCUSSION_RE 的 `(^|/)` 同款。真仓 rel 恒带前导段，行为不变。
    in_scope = bool(DECLARATION_RE.search("\n".join(lines[:HEAD_WINDOW]))) or any(s in "/" + rel for s in L2_DIR_SEGS)
    findings: "list[str]" = []
    tally = {"EXEMPT": 0, "SUBSTR": 0, "VIOLATION": 0}
    if not in_scope:
        return findings, tally
    in_fence = False
    for lineno, raw in enumerate(lines, 1):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        # EAC-SK5-F 修正（报告黄-11）：反引号遮除提至行级一次算
        # （照 check-entity.mask_non_narrative 口径·原先在 match×pattern 内重复算整行）
        masked = CODE_SPAN_RE.sub(lambda m: "\x00" * len(m.group(0)), raw)
        for label, pat in L2_PATTERNS:
            for match in re.finditer(pat, raw):
                # 豁免②行级标记 → EXEMPT（绿）
                if EXEMPT_MARK_RE.search(raw):
                    tally["EXEMPT"] += 1
                    continue
                # 豁免③遮除口径：反引号段／代码围栏内的示例段 → SUBSTR（判非违例·绿）
                if in_fence or match.group(0) not in masked:
                    tally["SUBSTR"] += 1
                    continue
                tally["VIOLATION"] += 1
                findings.append("%s:%d: %s EAC-L2 交接件禁模式命中 %s＝%r（过程痕迹不入正文）"
                                % (rel, lineno, SEV_WATCH, label, match.group(0)))
    return findings, tally


def check_l3(files: "list[str]", rel_map: "dict[str, str]") -> "list[str]":
    """编号唯一性＋同轮 v2 提示（按目录分组，目录级检查）。

    EAC-SK5-F：未用形参 `root` 清理（原实现从未读它）。
    """
    findings: "list[str]" = []
    by_dir: "dict[str, dict[str, list[str]]]" = {}
    v2_seen: "set[str]" = set()
    for path in files:
        rel = rel_map[path]
        if not DISCUSSION_RE.search(rel):
            continue
        name = os.path.basename(rel)
        # ① 同轮 v2 提示（先于分组：v2 形态文件本身不再进唯一性计数）
        if SAME_ROUND_V2_RE.search(name) and name not in v2_seen:
            v2_seen.add(name)
            findings.append("%s:1: %s EAC-L3 同轮 v2 形态文件名（一包一轮·已分发禁 v2）：%s"
                            % (rel, SEV_WATCH, name))
        # ② 唯一性分组（附加件不进组，见 SUPPLEMENT_RE 注）
        m = PKG_NO_RE.match(name) or PKG_NO_RE_CASED.match(name)
        if not m or SUPPLEMENT_RE.search(name):
            continue
        key = os.path.dirname(rel) + "|" + m.group(1) + "-" + m.group(2)
        by_dir.setdefault(key, []).append(rel)
    for key, rels in sorted(by_dir.items()):
        if len(rels) > 1:
            # 落点取首个成员的真实路径（不得输出伪位置）
            findings.append("%s:1: %s EAC-L3 同一议题包编号出现在 %d 个件：%s"
                            % (rels[0], SEV_WATCH, len(rels), " / ".join(os.path.basename(r) for r in rels)))
    return findings


def scan(root: str, skip_fixtures: bool,
         targets: "list[str] | None" = None) -> "tuple[list[str], dict[str, int]]":
    files = iter_files(root, skip_fixtures)
    if targets:
        # SWB-GTFAST S2-d 靶检：既有文件枚举结果按 abspath 交集过滤
        # （判据函数本体零调用路径改动＝只换入参文件集；交集空＝零发现汇总 exit 0）。
        tset = {os.path.abspath(t) for t in targets}
        files = [p for p in files if os.path.abspath(p) in tset]
    rel_map = {p: os.path.relpath(p, root).replace(os.sep, "/") for p in files}
    findings: "list[str]" = []
    tally = {"EXEMPT": 0, "SUBSTR": 0, "VIOLATION": 0}
    for path in files:
        rel = rel_map[path]
        lines = read_lines(path)
        findings.extend(check_l1(rel, lines))
        f2, t2 = check_l2(rel, lines)
        findings.extend(f2)
        for k in tally:
            tally[k] += t2[k]
    findings.extend(check_l3(files, rel_map))
    return findings, tally


# 对拍预期（--selftest 与内嵌预期比对；改 fixture 必须同步改这里，否则对拍红）
# EAC-SK5-F：四新样件入账——fence-sample（SUBSTR+2·VIOLATION+2：GPT-4 泄漏反例＋CJK 紧邻钉死）
# ＋tickets/dir-scan-sample（VIOLATION+1·目录扫描分支钉死）；日期文件名钉死＝零新增。
EXPECTED = {"EAC-L1": 3, "EAC-L2": 6, "EAC-L3": 2,
            "EXEMPT": 3, "SUBSTR": 5, "VIOLATION": 6}


def selftest(root: str) -> int:
    # 对拍件落位（B3a 随动·B2 收口登记候裁②）：deliverables 旧域灭→三分类目录新树
    fix = os.path.join(root, "agent-skills", "object-audit",
                       "tests", "fixtures", "collab-lint")
    if not os.path.isdir(fix):
        sys.stderr.write("infra error: 对拍测试件不存在：%s\n" % fix)
        return 4
    findings, tally = scan(fix, skip_fixtures=False)
    got = {"EAC-L1": 0, "EAC-L2": 0, "EAC-L3": 0}
    for line in findings:
        for key in got:
            if " " + key + " " in line:
                got[key] += 1
    print("selftest 对拍件＝%s" % os.path.relpath(fix, root).replace(os.sep, "/"))
    for line in findings:
        print("  %s" % line)
    ok = True
    for key in ("EAC-L1", "EAC-L2", "EAC-L3"):
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
    parser = argparse.ArgumentParser(add_help=True, description="EAC-SK5 协作纪律体裁机检")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    parser.add_argument("--selftest", action="store_true", help="对包内对拍测试件跑三检查并与预期数比对")
    parser.add_argument("--target", action="append", default=[],
                        help="靶检文件（可重复；给出＝既有枚举按 abspath 交集过滤＝只换入参文件集；"
                             "交集空＝零发现汇总 exit 0；目录参数＝用法错）")
    args = parser.parse_args(argv)

    root = find_root(args.root)
    if args.selftest:
        return selftest(root)

    if args.target:
        for tgt in args.target:
            if os.path.isdir(tgt):
                die_usage("--target 只收文件，目录请走缺省扫描面：%s" % tgt)
        findings, tally = scan(root, skip_fixtures=True, targets=args.target)
    else:
        files_present = iter_files(root, skip_fixtures=True)
        if not files_present:
            sys.stderr.write("infra error: 扫描域为空（%s 下无 .md/.txt）\n" % root)
            return 4
        findings, tally = scan(root, skip_fixtures=True)
    counts = {k: sum(1 for f in findings if " " + k + " " in f) for k in ("EAC-L1", "EAC-L2", "EAC-L3")}
    for key, n in counts.items():
        print("spec=%s count=%d" % (key, n))
    print("分账：EXEMPT(豁免标记行·绿)=%d  SUBSTR(围栏/反引号内示例·判非违例)=%d  VIOLATION(扫描面真命中)=%d"
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
