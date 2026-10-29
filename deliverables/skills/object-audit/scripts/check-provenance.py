#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: OA-D1-1
# spec_file: deliverables/object-audit/references/50-document.md
# spec_anchor: D1-1 | 归属声明随身
# spec_clause_sha256: b25fbd09c9259fc1375c4854122bc24a795f4532c36b1bfa0472a298db1108a5
# spec_version: 0.2
# spec_effective: 2026-10-22
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: ADR-2026-10-23-01
# spec_file: .collab/decisions/2026-10-22-裁决记录.md
# spec_anchor: - **拍板 3（S-04 默认域扩至 .sh·扩判据）**
# spec_clause_sha256: 3534eeb93e2d4514cf109dce4a00941ec9ada36ed51cba48f3cae83dd1756b66
# spec_version: 0.3
# spec_effective: 2026-10-23
# provider: object-audit
# --- /spec-provenance ---
#
# 条款摘要口径（本件是这条口径的**权威实现**，S-01／S-02／S-03 头注均引此）：
#   取 spec_anchor 在 spec_file 中命中的那一行 → 去首尾空白 → 连续空白压成单个空格
#   → UTF-8 编码 → sha256（十六进制小写）。行号不参与定位，也不入判据。
#   锚的定位方式：行内容 strip 后、或剥掉前导 `#`／`|` 后，以 spec_anchor **起始**。
#
# S-04 规范来源声明核验（OA-D1-1 归属声明随身 → 用到执行体上）。
#
# 判据来源（不复写正文，只指路径）：
#   P-1／P-2／P-3 与退出码归属 → deliverables/object-audit/references/70-provenance.md
#     「一、审：块在不在、字段齐不齐（P-1）」「三、审：锚还指得到吗（P-2）」「四、审：那句话还是那句话吗（P-3）」
#   退出码闭集 → deliverables/multi-collab/references/60-gates.md「六、退出码闭集」
#
# 退出码归属（照 70-provenance.md §一 与 裁-19 改判，**不照设计 v2 §2.2.4 旧配**）：
#   块整体缺失／键集合 ≠ 七键／格式不合法 → **exit 1**（声明作者欠账）
#   spec_file 不存在／锚命中 0 或 >1／条款摘要不符／provider 非现存包名 → **exit 3**（提供者欠账）
#   理由：把「作者忘了写」记进「规范没人维护」的账，正是 00-skeleton.md 记的「归属错」。
#   多类并存时取 3 优先（提供者欠账非产物方可自救，须先退提供者）。
#
# 本件只读：不写任何文件。唯一写动作在 run-gates.sh（出口②）。
"""S-04：对同目录全部 .py（含本件自身）跑 P-1／P-2／P-3 规范来源核验。

用法：
    python check-provenance.py [--root <仓根>] [--target <相对路径.py>]...
    不给 --target 时，默认扫 <仓根>/deliverables/*/scripts/*.py（含本件自身）。

退出码（闭集，见 60-gates.md「六、退出码闭集」）：
    0 通过／1 产物侧缺声明／3 规范侧失联／2 用法错／4 基础设施错
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import os
import re
import sys

SEV_BLOCK = "BLOCK"

# 七键闭集：缺一个不合格，多一个也不合格（多字段＝偷偷扩协议）。
REQUIRED_KEYS = (
    "spec_id",
    "spec_file",
    "spec_anchor",
    "spec_clause_sha256",
    "spec_version",
    "spec_effective",
    "provider",
)

# 块标记（注释载体：.py／.sh）。HTML 载体（.md）留待未来扩面，本件不猜。
# 规范件 70-provenance.md §二 的样例首尾行均带**闭合的 ` ---`**，故尾标记可选：
#   "# --- spec-provenance v1 ---" / "# --- /spec-provenance ---"
BLOCK_START_RE = re.compile(r"^[ \t]*#[ \t]*-{3,}[ \t]*spec-provenance v1[ \t]*(?:-{3,})?[ \t]*$")
BLOCK_END_RE = re.compile(r"^[ \t]*#[ \t]*-{3,}[ \t]*/spec-provenance[ \t]*(?:-{3,})?[ \t]*$")
KEY_VALUE_RE = re.compile(r"^[ \t]*#[ \t]*([A-Za-z_][A-Za-z0-9_-]*):[ \t]*(.*?)[ \t]*$")

# 格式校验（描述性字段只校格式，不与任何现值比对）。
SPEC_ID_RE = re.compile(r"^(OA|OB|MC|PUB|ADR)-[A-Za-z0-9\-.]+$")
SPEC_VERSION_RE = re.compile(r"^[0-9]+\.[0-9]+$")
SPEC_EFFECTIVE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


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
        if os.path.isdir(os.path.join(cur, "deliverables")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            die_usage("未能定位仓根；请用 --root 指定")
        cur = parent


def normalize_clause(line: str) -> str:
    """条款规范化：去首尾空白 → 连续空白压单空格（判据粒度＝一行/一表格行）。"""
    return re.sub(r"\s+", " ", line.strip())


def clause_sha256(line: str) -> str:
    return hashlib.sha256(normalize_clause(line).encode("utf-8")).hexdigest()


def read_text(path: str) -> str:
    """读文本并把 CRLF 归一为 LF。

    本仓 `core.autocrlf=true`，**检出后的文件本身就是 CRLF**；不归一则行尾 `\\r`
    会让块标记/键值的行正则失配（实测复现）。摘要口径不受影响：
    `normalize_clause` 本就把连续空白（含 `\\r`）压成单空格，两种行尾算出同一摘要。
    """
    try:
        with open(path, "r", encoding="utf-8", newline="") as handle:
            return handle.read().replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError) as exc:
        sys.stderr.write("infra error: 读取失败 %s: %s\n" % (path, exc))
        raise SystemExit(4)


# HTML 注释载体（70-provenance.md §二：`.md` 正文首块 `<!-- spec-provenance v1 … -->`）。
# 原注释"留待未来扩面"——A3 准入闸要求 SKILL.md 首块七字段（60-publish.md §六），
# 扩面即落实 §二 自己的话「一种正则三个载体通吃」；键行**不带 `#` 前缀**。
HTML_START_RE = re.compile(r"^[ \t]*<!--[ \t]*spec-provenance v1[ \t]*$")
HTML_END_RE = re.compile(r"^[ \t]*-->[ \t]*$")
HTML_KEY_VALUE_RE = re.compile(r"^[ \t]*([A-Za-z_][A-Za-z0-9_-]*):[ \t]*(.*?)[ \t]*$")


def parse_blocks(text: str) -> "list[dict[str, str]]":
    """取首尾标记之间的 key: value（一种正则通吃注释载体，不引 YAML 依赖）。
    载体二分：`#` 注释块（.py/.sh）与 HTML 注释块（.md）互斥嵌套，逐行判开闭。"""
    blocks: "list[dict[str, str]]" = []
    current: "dict[str, str] | None" = None
    html_current = False
    # 行分隔已在 read_text 归一（CRLF→LF）；此处再兜一次，防被直接传入原始文本。
    for raw in text.replace("\r\n", "\n").split("\n"):
        if BLOCK_START_RE.match(raw):
            current = {}
            html_current = False
            continue
        if HTML_START_RE.match(raw):
            current = {}
            html_current = True
            continue
        if current is not None and html_current and HTML_END_RE.match(raw):
            blocks.append(current)
            current = None
            continue
        if BLOCK_END_RE.match(raw):
            if current is not None and not html_current:
                blocks.append(current)
                current = None
            continue
        if current is not None:
            match = (HTML_KEY_VALUE_RE if html_current else KEY_VALUE_RE).match(raw)
            if match:
                current[match.group(1)] = match.group(2)
    return blocks


def resolve_anchor(spec_file_abs: str, anchor: str) -> "list[str]":
    """按锚定位：返回命中行的规范化文本列表（长度即命中数，须恰为 1）。"""
    hits: "list[str]" = []
    for raw in read_text(spec_file_abs).split("\n"):
        stripped = raw.strip()
        candidate = stripped.lstrip("#").strip()
        for probe in (stripped, candidate, candidate.lstrip("|").strip()):
            if probe.startswith(anchor):
                hits.append(normalize_clause(raw))
                break
    return hits


def existing_providers(root: str) -> "set[str]":
    # 五类子包（裁-38 Q2=A 路径适配）：deliverables/ 一层与 deliverables/skills/ 一层并集。
    providers: "set[str]" = set()
    for base in (os.path.join(root, "deliverables"),
                 os.path.join(root, "deliverables", "skills")):
        if os.path.isdir(base):
            for name in os.listdir(base):
                if os.path.isdir(os.path.join(base, name)):
                    providers.add(name)
    return providers


def check_file(root: str, path: str, providers: "set[str]") -> "tuple[list[str], int]":
    """核验单个脚本，返回 (findings, 最高优先级退出码)。0＝无问题。"""
    rel = os.path.relpath(path, root).replace(os.sep, "/")
    blocks = parse_blocks(read_text(path))
    findings: "list[str]" = []
    worst = 0

    def raise_to(code: int) -> None:
        # 3 优先于 1：提供者欠账非产物方可自救，须先退提供者。
        nonlocal worst
        if code == 3 or worst != 3:
            worst = max(worst, code)

    # ---- P-1：块在不在、键集合是否恰为七键 ----
    if not blocks:
        findings.append(
            "%s:1: %s OA-D1-1 缺 spec-provenance 块（声明作者欠账）" % (rel, SEV_BLOCK)
        )
        raise_to(1)
        return findings, worst

    for index, block in enumerate(blocks, 1):
        keys = set(block)
        missing = [k for k in REQUIRED_KEYS if k not in keys]
        extra = sorted(keys - set(REQUIRED_KEYS))
        if missing or extra:
            findings.append(
                "%s:1: %s OA-D1-1 块 %d 键集合不等于七键（缺 %s／多 %s）"
                % (rel, SEV_BLOCK, index, ",".join(missing) or "-", ",".join(extra) or "-")
            )
            raise_to(1)
            continue  # 键不全时不猜语义，后续判定对该块跳过

        spec_id = block["spec_id"]
        if not SPEC_ID_RE.match(spec_id):
            findings.append("%s:1: %s OA-D1-1 块 %d spec_id 格式不合法 %r" % (rel, SEV_BLOCK, index, spec_id))
            raise_to(1)
        if not SPEC_VERSION_RE.match(block["spec_version"]):
            findings.append(
                "%s:1: %s OA-D1-1 块 %d spec_version 格式不合法 %r（描述性字段仍须可解析）"
                % (rel, SEV_BLOCK, index, block["spec_version"])
            )
            raise_to(1)
        if not SPEC_EFFECTIVE_RE.match(block["spec_effective"]):
            findings.append(
                "%s:1: %s OA-D1-1 块 %d spec_effective 格式不合法 %r"
                % (rel, SEV_BLOCK, index, block["spec_effective"])
            )
            raise_to(1)
        if not SHA256_RE.match(block["spec_clause_sha256"]):
            findings.append(
                "%s:1: %s OA-D1-1 块 %d spec_clause_sha256 非 64 位十六进制" % (rel, SEV_BLOCK, index)
            )
            raise_to(1)

        # provider 必须是 deliverables/ 下现存包名（不是人名）——非现存＝提供者侧路由失效，exit 3。
        provider = block["provider"]
        if provider not in providers:
            findings.append(
                "%s:1: %s OA-D1-1 块 %d provider %r 不是 deliverables/ 下现存包名（规范侧失联）"
                % (rel, SEV_BLOCK, index, provider)
            )
            raise_to(3)

        # ---- P-2：锚可解析且唯一 ----
        spec_file = block["spec_file"]
        spec_abs = os.path.normpath(os.path.join(root, spec_file.replace("/", os.sep)))
        if not os.path.isfile(spec_abs) and spec_file.startswith("deliverables/") \
                and not spec_file.startswith("deliverables/skills/"):
            # 五类子包路径适配：旧式声明 `deliverables/<pkg>/…` 落空时试
            # `deliverables/skills/<pkg>/…`（纯解析双探，声明文本与 P-3 摘要不受影响）。
            nested = os.path.join(root, "deliverables", "skills",
                                  *spec_file.split("/")[1:])
            if os.path.isfile(os.path.normpath(nested)):
                spec_abs = os.path.normpath(nested)
        # 交付物包内闭环尝试（EAC-CLN·拍板㊺配套·票内预授权小改）：spec_file 为**包内
        # 相对路径**时从块所在文件的目录解析——纯解析语义扩展，P-1/P-2/P-3 判据一字未动。
        # 理由：交付物（专家/技能包）内的 provenance spec_file 只准指向包内文件
        # （指针闭集㊺）；装配面/部署面没有仓根结构，仓根语义在交付态必悬空。
        if not os.path.isfile(spec_abs):
            local = os.path.normpath(os.path.join(
                os.path.dirname(os.path.abspath(path)), spec_file.replace("/", os.sep)))
            if os.path.isfile(local):
                spec_abs = local
        if not os.path.isfile(spec_abs):
            findings.append(
                "%s:1: %s OA-D1-1 块 %d spec_file 不存在 %s（规范侧失联）"
                % (rel, SEV_BLOCK, index, spec_file)
            )
            raise_to(3)
            continue
        anchor = block["spec_anchor"]
        hits = resolve_anchor(spec_abs, anchor)
        if len(hits) != 1:
            findings.append(
                "%s:1: %s OA-D1-1 块 %d 锚 %r 在 %s 命中 %d 行（须恰 1 行；0＝锚没了，>1＝锚歧义）"
                % (rel, SEV_BLOCK, index, anchor, spec_file, len(hits))
            )
            raise_to(3)
            continue

        # ---- P-3：条款内容未变（唯一参与判定的字段）----
        actual = clause_sha256(hits[0])
        if actual != block["spec_clause_sha256"]:
            findings.append(
                "%s:1: %s OA-D1-1 块 %d 条款摘要不符：锚 %r 现值 %s… ≠ 声明 %s…（条款变了，脚本没跟上）"
                % (rel, SEV_BLOCK, index, anchor, actual[:12], block["spec_clause_sha256"][:12])
            )
            raise_to(3)

    return findings, worst


def default_targets(root: str) -> "list[str]":
    # 裁-21 拍板 3：默认域由 `*.py` 扩为 `*.py`＋`*.sh`——设计 §2.5 字面只写 .py 是
    # 当时只有 .py 的产物；现 .sh 亦带七键块，扩后「脚本自身必过 S-04」对全部执行体成立。
    # 五类子包路径适配：双域（deliverables/*/scripts/* 与 deliverables/skills/*/scripts/*）
    patterns = [os.path.join(root, "deliverables", "*", "scripts", "*"),
                os.path.join(root, "deliverables", "skills", "*", "scripts", "*")]
    hits: "set[str]" = set()
    for pattern in patterns:
        hits.update(p for p in glob.glob(pattern)
                    if p.endswith((".py", ".sh")) and os.path.isfile(p))
    return sorted(hits)


def main(argv: "list[str]") -> int:
    parser = argparse.ArgumentParser(add_help=True, description="S-04 规范来源声明核验")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    parser.add_argument(
        "--target",
        action="append",
        default=[],
        help="待核文件（相对 --root，可重复）；默认扫 deliverables/*/scripts/*.py",
    )
    args = parser.parse_args(argv)
    root = find_root(args.root)

    if args.target:
        targets = []
        for rel in args.target:
            full = os.path.normpath(os.path.join(root, rel.replace("/", os.sep)))
            if not os.path.isfile(full):
                die_usage("--target 指向不存在的文件：%s" % rel)
            targets.append(full)
    else:
        targets = default_targets(root)

    if not targets:
        sys.stderr.write("infra error: 扫描域为空（deliverables/*/scripts/*.py 不存在）\n")
        return 4

    providers = existing_providers(root)
    if not providers:
        sys.stderr.write("infra error: deliverables/ 下没有包目录，provider 无从校验\n")
        return 4

    findings: "list[str]" = []
    worst = 0
    for path in targets:
        file_findings, code = check_file(root, path, providers)
        findings.extend(file_findings)
        worst = 3 if code == 3 else max(worst, code)

    for line in findings:
        print(line)
    return worst


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed
        sys.stderr.write("infra error: %s\n" % exc)
        raise SystemExit(4)
