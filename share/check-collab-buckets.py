#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SWB-BKTCLS：仓根 .collab 桶名闭集机检（MC-BUCKET-1）。
#
# 条款真源（只指路径，不复写正文）：
#   闭集名录真源 = 仓根 .collab/README.md 「17 桶名录」行（本件运行时解析对拍自证）
#   规范依据 = 皮总裁定登记件 .collab/decisions/2026-11-10-皮总裁定-候裁三件全按建议放行.md
#              §二-2 裁甲（17 桶闭集只管仓根 .collab；两包 qa 桶随批改名豁免）
#   规格票面 = .scratch/tickets/2026-11-16-SWB-BKTCLS-桶名闭集机检规格票-v1.md §二
#
# 铁律遵守（60-gates.md §〇）：本件**只输出**「严重度＋spec_id＋位置＋一句话」，
# 不决定拦不拦——拦放由路由表定。
#
# 自咬纪律（照 check-collab-lint 头注先例）：本文件内一切桶名例证一律不落反引号
# 包裹的可解析路径指针——本件虽不在 check-pointers 缺省扫描域（share 桶），
# 但按票面 §2-3 验收轮以 --target 靶检本件，反引号包径即自咬。全文零反引号包径。
#
# 本件只读：不写任何文件。唯一写动作在 run-gates.sh（出口②）。
"""仓根 .collab 桶名闭集校验（MC-BUCKET-1·白名单制·单层射程）。

用法：
    python check-collab-buckets.py [--root <仓根>]

扫描域写死＝仓根 .collab 一级子目录（os.listdir 单层枚举·不递归·不扫嵌套 .collab——
射程口径＝裁甲在册句「17 桶闭集只管仓根」。一级文件不判（散文件群另有观察账·非本闸射程）。

退出码（闭集，见 60-gates.md「六、退出码闭集」）：
    0 通过（零违例且名录对拍一致）／1 违规（≥1 发现）
    2 用法错／4 基础设施错（仓根 .collab 不存在＝仓根异常不得静默放行；README 名录行解析不到＝对拍自证失效）
"""

from __future__ import annotations

import argparse
import os
import re
import sys

SEV_BLOCK = "BLOCK"
SEV_WATCH = "WATCH"
SPEC_ID = "MC-BUCKET-1"

# 内嵌白名单 17 项闭集（frozenset·真源同步防线见 README 对拍自证——改一漏一即红）。
# 与 .collab/README.md 「17 桶名录」行逐项同步；本处逐项裸写、不加反引号（自咬纪律）。
BUCKET_WHITELIST = frozenset({
    "decisions", "audits", "receipts", "board", "design", "research", "refs",
    "evidence", "inbox", "process", "dispatch", "drafts", "adr", "architect",
    "product", "ledger", "returns",
})

README_ANCHOR = "17 桶名录"
README_WINDOW = 5  # 名录行＝锚字样行之后首个含反引号段的行（现盘锚行下一非空行）
BACKTICK_RE = re.compile(r"`([^`\n]+)`")


def die_usage(msg: str) -> "None":
    sys.stderr.write("usage error: %s\n" % msg)
    raise SystemExit(2)


def die_infra(msg: str) -> "None":
    sys.stderr.write("infra error: %s\n" % msg)
    raise SystemExit(4)


def find_root(explicit: str | None) -> str:
    if explicit:
        if not os.path.isdir(explicit):
            die_usage("--root 不存在：%s" % explicit)
        return os.path.abspath(explicit)
    cur = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isdir(os.path.join(cur, "share")) and any(
                os.path.isdir(os.path.join(cur, c))
                for c in ("agent-experts", "agent-skills", "softwares")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            die_usage("未能定位仓根；请用 --root 指定")
        cur = parent


def read_readme_buckets(readme_path: str) -> "frozenset[str]":
    """README 对拍自证：解析「17 桶名录」行反引号段，得桶名集合。

    解析不到＝对拍自证失效＝基础设施错 exit 4（fail-closed·不得静默只信内嵌集）。
    行内尾缀斜杠剥除归一（名录行以 decisions/ 这类带斜杠形态书写）。
    """
    try:
        with open(readme_path, "r", encoding="utf-8", errors="replace", newline="") as handle:
            lines = handle.read().replace("\r\n", "\n").split("\n")
    except OSError as exc:
        die_infra("读取 README 失败 %s: %s" % (readme_path, exc))
    anchor_i = next((i for i, ln in enumerate(lines) if README_ANCHOR in ln), None)
    if anchor_i is None:
        die_infra("README 名录行解析不到（锚字样「%s」零命中）：%s" % (README_ANCHOR, readme_path))
    for ln in lines[anchor_i + 1: anchor_i + 1 + README_WINDOW]:
        m = BACKTICK_RE.search(ln)
        if m:
            toks = m.group(1).split()
            if not toks:
                die_infra("README 名录行反引号段为空：%s" % readme_path)
            return frozenset(t[:-1] if t.endswith("/") else t for t in toks)
    die_infra("README 名录行解析不到（锚字样命中但窗口内无反引号段）：%s" % readme_path)


def scan(root: str) -> "tuple[list[str], list[str]]":
    """返回（违例行列表，名录漂移 WATCH 行列表）。"""
    collab = os.path.join(root, ".collab")
    # 空面 fail-closed：仓根 .collab 不存在＝基础设施错 exit 4（票面 §2-2 写死）
    if not os.path.isdir(collab):
        die_infra("仓根 .collab 不存在：%s" % collab)
    try:
        entries = os.listdir(collab)
    except OSError as exc:
        die_infra("读取 .collab 一级目录失败：%s" % exc)

    findings: "list[str]" = []
    for name in sorted(entries):
        if not os.path.isdir(os.path.join(collab, name)):
            continue  # 一级文件不判（散文件群非本闸射程）
        if name in BUCKET_WHITELIST:
            continue
        findings.append(".collab/%s:1: %s %s 桶名闭集违例（桶名 %s ∉ %d 桶名录）"
                        % (name, SEV_BLOCK, SPEC_ID, name, len(BUCKET_WHITELIST)))

    watches: "list[str]" = []
    readme = os.path.join(collab, "README.md")
    if not os.path.isfile(readme):
        die_infra("仓根 .collab/README.md 不存在（名录真源缺失·对拍自证失效）")
    parsed = read_readme_buckets(readme)
    if parsed != BUCKET_WHITELIST:
        # 两源不一致本身即报（闭集改动必须两处同步·改一漏一即红·票面 §2-3）
        only_readme = sorted(parsed - BUCKET_WHITELIST)
        only_script = sorted(BUCKET_WHITELIST - parsed)
        watches.append(".collab/README.md:1: %s %s 名录漂移（README 名录行解析集 ≠ 脚本内嵌集：仅README有=%s 仅脚本有=%s）"
                       % (SEV_WATCH, SPEC_ID,
                          ",".join(only_readme) if only_readme else "-",
                          ",".join(only_script) if only_script else "-"))
    return findings, watches


def main(argv: "list[str]") -> int:
    parser = argparse.ArgumentParser(add_help=True, description="仓根 .collab 桶名闭集校验（MC-BUCKET-1）")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    args = parser.parse_args(argv)

    root = find_root(args.root)
    findings, watches = scan(root)
    for line in findings:
        print(line)
    for line in watches:
        print(line)
    n_dir = len([n for n in os.listdir(os.path.join(root, ".collab"))
                 if os.path.isdir(os.path.join(root, ".collab", n))])
    print("check-collab-buckets：一级目录判 %d 枚｜违例 %d｜名录对拍 %s"
          % (n_dir, len(findings), "一致" if not watches else "漂移"))
    return 1 if (findings or watches) else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed
        sys.stderr.write("infra error: %s\n" % exc)
        raise SystemExit(4)
