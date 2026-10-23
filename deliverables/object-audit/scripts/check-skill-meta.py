#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: OA-S5
# spec_file: deliverables/object-audit/references/10-skill.md
# spec_anchor: S5 | 体量披露
# spec_clause_sha256: 6ab4da3d1a7775d1eef09829901e6311338b256f81993aed433c9a3c019778ed
# spec_version: 0.2
# spec_effective: 2026-10-22
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: OA-S2
# spec_file: deliverables/object-audit/references/10-skill.md
# spec_anchor: S2 | 触发描述
# spec_clause_sha256: 76738ff6d8b9386b3554e9586baff96f4369e11d04114a28386327f64a647cef
# spec_version: 0.2
# spec_effective: 2026-10-22
# provider: object-audit
# --- /spec-provenance ---
#
# 条款摘要口径（S-04 与本件共用同一算法·写死在此以免两处实现漂移）：
#   取 spec_anchor 在 spec_file 中命中的那一行 → 去首尾空白 → 连续空白压成单个空格
#   → UTF-8 编码 → sha256（十六进制小写）。行号不参与定位，也不入判据。
#
# S-01 体量披露与触发描述检查（OA-S5／OA-S2）。
#
# 判据来源（不复写正文，只指路径）：
#   OA-S5 → deliverables/object-audit/references/10-skill.md「S5 体量披露」
#   OA-S2 → deliverables/object-audit/references/10-skill.md「S2 触发描述」
# 严重度照抄规范：S1–S5 属「问净」，「问净」不合格＝阻断（同文件「判定要点」）。
#
# 本件只读：不写任何文件。唯一写动作在 run-gates.sh（出口②）。
# 本件不含策略判断：只输出 SEV＋spec_id＋退出码；拦不拦由 run-gates.sh 按路由表决定。
"""S-01：扫 deliverables/*/SKILL.md 的体量披露（OA-S5）与触发描述（OA-S2）。

用法：
    python check-skill-meta.py [--root <仓根>] [--project-name <名>]...

退出码（闭集，见 deliverables/multi-collab/references/60-gates.md「六、退出码闭集」）：
    0 通过（零 finding）／1 违规／2 用法错／4 基础设施错
"""

from __future__ import annotations

import argparse
import os
import re
import sys

# 严重度常量：取值域必须与 60-gates.md 路由表 on_severity 的键一致，越界即路由表 exit 4。
SEV_BLOCK = "BLOCK"

# 「什么时候用」的标记词：S2 要求 description 写 when 条件。中英双列以免漏判。
WHEN_MARKERS = ("Use when", "use when", "USE WHEN", "什么时候用", "何时使用", "适用场景")

# 主文件常驻容量红线（条数由 OA-S5 条款文本给定，此处为取值，改动须先改规范）。
MAIN_FILE_LINE_LIMIT = 200


def die_usage(msg: str) -> "None":
    """用法错：exit 2（处置人＝调用方）。"""
    sys.stderr.write("usage error: %s\n" % msg)
    raise SystemExit(2)


def find_root(explicit: str | None) -> str:
    """定位仓根：显式 --root 优先，否则自本文件向上找含 deliverables/ 的目录。"""
    if explicit:
        if not os.path.isdir(explicit):
            die_usage("--root 不存在：%s" % explicit)
        if not os.path.isdir(os.path.join(explicit, "deliverables")):
            die_usage("--root 下找不到 deliverables/：%s" % explicit)
        return os.path.abspath(explicit)
    cur = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isdir(os.path.join(cur, "deliverables")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            die_usage("未能自脚本位置向上定位到含 deliverables/ 的仓根；请用 --root 指定")
        cur = parent


def read_lines(path: str) -> "list[str]":
    """按字节安全读入并切行（文本模式统一 UTF-8，读失败即基础设施错 exit 4）。

    CRLF 先归一为 LF：本仓 `core.autocrlf=true`，检出件本身就是 CRLF；不归一则
    frontmatter 的值会带着 `\\r`（`description: xxx\\r`），触发词匹配与计数都被污染。
    """
    try:
        with open(path, "r", encoding="utf-8", newline="") as handle:
            data = handle.read().replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError) as exc:
        sys.stderr.write("infra error: 读取失败 %s: %s\n" % (path, exc))
        raise SystemExit(4)
    return data.split("\n")


def parse_frontmatter(lines: "list[str]") -> "dict[str, str]":
    """inline 解析 frontmatter（零第三方依赖：不引 pyyaml）。

    只取 `key: value` 顶层标量；值可折行（缩进续行拼回）。解析不出 description
    不报错——「缺字段」是产物违规，由调用方按 finding 处理。
    """
    if not lines or lines[0].strip() != "---":
        return {}
    fields: "dict[str, str]" = {}
    key = None
    for raw in lines[1:]:
        stripped = raw.strip()
        if stripped == "---":
            break
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", raw)
        if match:
            key = match.group(1)
            fields[key] = match.group(2).strip()
        elif key and (raw.startswith(" ") or raw.startswith("\t")):
            fields[key] = (fields.get(key, "") + " " + stripped).strip()
    return fields


def check_one(root: str, skill_md: str, project_names: "list[str]") -> "list[str]":
    """对单个 SKILL.md 跑 OA-S5 与 OA-S2，返回 finding 行（不含策略判断）。"""
    rel = os.path.relpath(skill_md, root).replace(os.sep, "/")
    lines = read_lines(skill_md)
    pkg_dir = os.path.dirname(skill_md)
    findings: "list[str]" = []

    # ---- OA-S5：主文件＜200 行 ＋ references/ 渐进披露存在 ----
    body = [ln for ln in lines]
    total = len(body)
    # 末行常为空串（文件以换行收尾），不计入行数，否则 200 行的件会被判 201。
    if body and body[-1] == "":
        total -= 1
    if total >= MAIN_FILE_LINE_LIMIT:
        findings.append(
            "%s:1: %s OA-S5 主文件 %d 行 ≥ %d 行容量红线（细则应进 references/）"
            % (rel, SEV_BLOCK, total, MAIN_FILE_LINE_LIMIT)
        )
    if not os.path.isdir(os.path.join(pkg_dir, "references")):
        findings.append(
            "%s:1: %s OA-S5 无 references/ 渐进披露层（细则无处可放）" % (rel, SEV_BLOCK)
        )

    # ---- OA-S2：description 含 when；不含项目名 ----
    fields = parse_frontmatter(lines)
    desc = fields.get("description", "")
    if not desc:
        findings.append("%s:1: %s OA-S2 frontmatter 缺 description 字段" % (rel, SEV_BLOCK))
    else:
        if not any(marker in desc for marker in WHEN_MARKERS):
            findings.append(
                "%s:1: %s OA-S2 description 未含 when 条件（缺「什么时候用」，该用法永不加载）"
                % (rel, SEV_BLOCK)
            )
        for name in project_names:
            if name and name in desc:
                findings.append(
                    "%s:1: %s OA-S2 description 含项目名「%s」（应写场景不写项目）"
                    % (rel, SEV_BLOCK, name)
                )
    return findings


def main(argv: "list[str]") -> int:
    parser = argparse.ArgumentParser(add_help=True, description="S-01 体量披露与触发描述检查")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    parser.add_argument(
        "--project-name",
        action="append",
        default=[],
        help="项目名（可重复）；亦可用环境变量 GATE_PROJECT_NAMES 逗号分隔注入",
    )
    args = parser.parse_args(argv)

    root = find_root(args.root)
    names = list(args.project_name)
    env_names = os.environ.get("GATE_PROJECT_NAMES", "")
    if env_names.strip():
        names.extend(n.strip() for n in env_names.split(",") if n.strip())

    deliverables = os.path.join(root, "deliverables")
    try:
        packages = sorted(
            name for name in os.listdir(deliverables)
            if os.path.isfile(os.path.join(deliverables, name, "SKILL.md"))
        )
    except OSError as exc:
        sys.stderr.write("infra error: 无法列 deliverables/: %s\n" % exc)
        return 4

    if not packages:
        sys.stderr.write("infra error: deliverables/ 下没有任何 SKILL.md（扫描域为空）\n")
        return 4

    findings: "list[str]" = []
    for name in packages:
        findings.extend(check_one(root, os.path.join(deliverables, name, "SKILL.md"), names))

    if not names:
        # 项目名子判据未执行 ⇒ 不静默，但也不是 finding：与 S-03 同口径（裁-21），
        # 「清单没注入」是**配置问题**不是产物违规，记成 OA-S2 违规＝归属错；
        # 每次运行打 coverage 行（非 finding 格式，run-gates 原样透传显示）。
        # 修单②（裁-21 复核）：不再输出字面 glob 位置——coverage 行本就无单件落点。
        print("coverage: OA-S2「不含项目名」子判据未执行（--project-name 或 GATE_PROJECT_NAMES 未注入）")

    for line in findings:
        print(line)
    return 1 if findings else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # 未预期异常＝基础设施错，不得吞成 0（fail-closed）
        sys.stderr.write("infra error: %s\n" % exc)
        raise SystemExit(4)
