#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SWB-BKTCLS：仓根 .collab 桶名闭集机检（MC-BUCKET-1）。
#
# 条款真源（只指路径，不复写正文）：
#   闭集名录真源 = 仓根 .collab/README.md 「20 桶名录」行（本件运行时解析对拍自证）
#   规范依据 = 皮总裁定登记件 .collab/decisions/2026-11-10-皮总裁定-候裁三件全按建议放行.md
#              §二-2 裁甲（17 桶闭集只管仓根 .collab；两包 qa 桶随批改名豁免）
#   规格票面 = .scratch/tickets/2026-11-16-SWB-BKTCLS-桶名闭集机检规格票-v1.md §二
#   扩册沿革 = 白名单 17→20（追加 claims/instances/qa 三枚）出处三件 = .collab/decisions/2026-11-20-ITER-B-C1-J1主理人自裁登记-v1.md ＋ .collab/architect/2026-11-20-ITER-BKTCLS-桶名闭集扩册-规则票-v1.md ＋ .collab/qa/2026-11-20-ITER-B-C1-审票判词-QA席-v1.md（qa 存量隐性违例清算出处）
#
# 铁律遵守（60-gates.md §〇）：本件**只输出**「严重度＋spec_id＋位置＋一句话」，
# 不决定拦不拦——拦放由路由表定。
#
# 自咬纪律（照 check-collab-lint 头注先例）：本文件内一切桶名例证一律不落反引号
# 包裹的可解析路径指针——本件虽不在 check-pointers 缺省扫描域（share 桶），
# 但按票面 §2-3 验收轮以 --target 靶检本件，反引号包径即自咬。全文零反引号包径。
#
# MC-PAIR-1（ITER-W1-T1c·收口-验收配对判据段）：
#   规格票面 = .scratch/tickets/2026-11-18-ITER-W1-T1c-判词命名与配对机检票-v1.md §三 S1 ①-⑤
#   扫描域重声明 = 同包 .collab/decisions/2026-11-18-ITER-W1-T1c-票级放行登记-v1.md §三＋§六 rev-1
#   （收口枚举域单取本包桶；判词查询域＝并集两路＝本包 audits ∪ 仓根 audits；
#    MC-BUCKET-1 本体扫描域照旧仓根 .collab，rev-1 已撤同步解析序括注）
#   生效日常量 EFFECTIVE_DATE＝2026-11-18＝本票 BUILD 笔落链当日（放行登记 §一 J-5 采甲）
#   配对段存量白名单沿革＝SWB-BG-06（ITER-E）增建 PAIR_LEGACY_EXEMPT 逐件豁免集＝缺配对判词＝历史事实不可补造＝真话入册
#
# 本件只读：不写任何文件。唯一写动作在 run-gates.sh（出口②）。
"""仓根 .collab 桶名闭集校验（MC-BUCKET-1·白名单制·单层射程）＋收口-验收配对机检（MC-PAIR-1）。

用法：
    python check-collab-buckets.py [--root <仓根>]
        [--bucket-root decisions=<收口枚举域根>] [--bucket-root audits=<判词查询域根>]...

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

# 内嵌白名单 20 项闭集（frozenset·真源同步防线见 README 对拍自证——改一漏一即红）。
# 与 .collab/README.md 「20 桶名录」行逐项同步；本处逐项裸写、不加反引号（自咬纪律）。
BUCKET_WHITELIST = frozenset({
    "decisions", "audits", "receipts", "board", "design", "research", "refs",
    "evidence", "inbox", "process", "dispatch", "drafts", "adr", "architect",
    "product", "ledger", "returns", "claims", "instances", "qa",
})

README_ANCHOR = "20 桶名录"
README_WINDOW = 5  # 名录行＝锚字样行之后首个含反引号段的行（现盘锚行下一非空行）
BACKTICK_RE = re.compile(r"`([^`\n]+)`")

# ---------- MC-PAIR-1 收口-验收配对判据段（ITER-W1-T1c） ----------
# 扫描域两路独立设定（放行登记 §三＋§六 rev-1）：收口枚举域单取本包桶；
# 判词查询域＝并集两路（本包 audits ∪ 仓根 audits）。MC-BUCKET-1 本体扫描域照旧仓根。
PAIR_SPEC_ID = "MC-PAIR-1"
# 时间效力常量（票面 S1②＋放行登记 §一 J-5 采甲）＝本票 BUILD 笔落链当日；
# 件名日期段严格小于本值者豁免＝存量不追溯。
EFFECTIVE_DATE = "2026-11-18"
# 存量归因白名单（ITER-E 族·SWB-BG-06·真话入册）：该收口登记件落笔于配对判词工序生效窗口内但 QA 判词
# 从未产出＝缺配对＝历史事实不可补造＝白名单豁免非补造；桶名径例证与件名居注释缩进面＝各闸射程纪律兑现。
PAIR_LEGACY_EXEMPT = frozenset({"2026-11-19-ITER-W2-T2e-收口登记-v1.md"})
# 本包桶根段（缺省解析序用·治理正位＝项目工作空间自家桶·拆段拼接照 run-gates 先例）
PKG_BUCKET_SEG = ("agent-experts", "baigong-" "software-team", ".collab")
# 收口登记件名形态（日期-票族-收口登记-vN·票面 S1①）
CLOSEOUT_NAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)-收口登记-v\d+\.md$")


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
    """README 对拍自证：解析「20 桶名录」行反引号段，得桶名集合。

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


def scan_pair(root: str, bucket_args: "list[str] | None") -> "tuple[list[str], int, int]":
    """MC-PAIR-1 配对判据段：收口登记件必引本票族 QA独立验收判词件全名。

    返回（违例行列表，在判收口枚数，判词件命中枚数）。

    扫描域两路解析序（放行登记 §三＋§六 rev-1）：
    ① 显式 --bucket-root（可重复·key=value：decisions= 单路／audits= 可多枚成并集）优先；
    ② 缺省自 --root 下探本包桶根（在场即用）：收口枚举域＝其 decisions；
       判词查询域＝并集两路＝其 audits ∪ 仓根 .collab/audits（兼容存量跨域链史·rev-1 采变体二）；
    ③ 任一路解析不到＝空面 fail-closed＝基础设施错 exit 4（两路均缺＝§三③ 写死案型；
       单路缺同按空面处置，不得静默放行——照本件既有 fail-closed 先例从严）。

    时间效力条款（票面 S1②）：件名日期段严格小于 EFFECTIVE_DATE 者不判＝存量全豁免。
    本段零写（只读铁律·票面 S1④）。
    """
    dec_dir = None
    aud_dirs: "list[str]" = []
    for spec in (bucket_args or []):
        key, sep, val = spec.partition("=")
        if not sep or not val:
            die_usage("--bucket-root 须为 key=value 形态（decisions=／audits=）：%s" % spec)
        if not os.path.isdir(val):
            die_usage("--bucket-root 目录不存在：%s" % val)
        if key == "decisions":
            dec_dir = os.path.abspath(val)
        elif key == "audits":
            ap = os.path.abspath(val)
            if ap not in aud_dirs:
                aud_dirs.append(ap)
        else:
            die_usage("--bucket-root 的 key 只认 decisions／audits：%s" % spec)

    pkg_collab = os.path.join(root, *PKG_BUCKET_SEG)
    if dec_dir is None:
        cand = os.path.join(pkg_collab, "decisions")
        if os.path.isdir(cand):
            dec_dir = cand
    if not aud_dirs:
        # 并集两路候选＝本包 audits ∪ 仓根 audits；linked worktree 下仓根＝git 链面真源位，
        # 自仓根 .git 文件内 gitdir 行回溯（sparse 域仓根桶不落盘＝既有案型，链面仍在主仓）。
        cands = [os.path.join(pkg_collab, "audits"),
                 os.path.join(root, ".collab", "audits")]
        git_marker = os.path.join(root, ".git")
        if os.path.isfile(git_marker):
            try:
                with open(git_marker, "r", encoding="utf-8", errors="replace") as handle:
                    marker = handle.read().strip()
                if marker.startswith("gitdir:"):
                    gdir = marker.split(":", 1)[1].strip().replace("\\", "/")
                    if "/worktrees/" in gdir:
                        common_dir = gdir.split("/worktrees/")[0]
                        cands.append(os.path.join(os.path.dirname(common_dir),
                                                  ".collab", "audits"))
            except OSError:
                pass  # 第二路按在场即用处置；两路均缺仍由下方 fail-closed 拦，不得静默放行
        for cand in cands:
            ap = os.path.abspath(cand)
            if os.path.isdir(ap) and ap not in aud_dirs:
                aud_dirs.append(ap)
    if dec_dir is None or not aud_dirs:
        die_infra("配对段两路桶根解析不到（收口枚举域 %s｜判词查询域在场 %d 路）＝空面 fail-closed"
                  % (dec_dir if dec_dir else "缺", len(aud_dirs)))

    try:
        names = sorted(os.listdir(dec_dir))
    except OSError as exc:
        die_infra("读取收口枚举域失败 %s: %s" % (dec_dir, exc))
    aud_names: "list[str]" = []
    for d in aud_dirs:
        try:
            aud_names.extend(os.listdir(d))
        except OSError as exc:
            die_infra("读取判词查询域失败 %s: %s" % (d, exc))

    findings: "list[str]" = []
    n_close = 0
    n_hit = 0
    for name in names:
        m = CLOSEOUT_NAME_RE.match(name)
        if not m:
            continue
        date_seg, fam = m.group(1), m.group(2)
        if date_seg < EFFECTIVE_DATE:
            continue  # 存量不追溯（票面 S1②·严格小于才豁免）
        if name in PAIR_LEGACY_EXEMPT:
            continue  # 存量白名单（SWB-BG-06·不可补造案型·真话入册）
        n_close += 1
        verdict_re = re.compile(r"^\d{4}-\d{2}-\d{2}-%s-QA独立验收判词-v\d+\.md$"
                                % re.escape(fam))
        verdicts = sorted({n for n in aud_names if verdict_re.match(n)})
        if not verdicts:
            findings.append("%s:1: %s %s 收口登记件缺配对验收判词件（票族 %s 于判词查询域零命中）"
                            % (name, SEV_BLOCK, PAIR_SPEC_ID, fam))
            continue
        n_hit += len(verdicts)
        try:
            with open(os.path.join(dec_dir, name), "r", encoding="utf-8",
                      errors="replace", newline="") as handle:
                body = handle.read()
        except OSError as exc:
            die_infra("读取收口登记件失败 %s: %s" % (os.path.join(dec_dir, name), exc))
        if not any(v in body for v in verdicts):
            findings.append("%s:1: %s %s 收口登记件正文未引用配对验收判词件全名（票族 %s）"
                            % (name, SEV_BLOCK, PAIR_SPEC_ID, fam))
    return findings, n_close, n_hit


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
    parser = argparse.ArgumentParser(add_help=True,
                                     description="仓根 .collab 桶名闭集校验（MC-BUCKET-1）＋收口-验收配对机检（MC-PAIR-1）")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    parser.add_argument("--bucket-root", action="append", metavar="KEY=路径",
                        help="配对段扫描域显式指认（可重复）：decisions=收口枚举域根·audits=判词查询域根（多枚成并集）")
    parser.add_argument("--seg", choices=("all", "bucket", "pair"), default="all",
                        help="段选择：all 两段全跑（缺省·run-gates 挂载形态）／bucket 仅桶名闭集面／pair 仅配对面"
                             "（worktree sparse 域仓根桶不落盘＝放行登记 §六 rev-1 在册案型，配对段须可独立取读数）")
    args = parser.parse_args(argv)

    root = find_root(args.root)
    pair_findings: "list[str]" = []
    findings: "list[str]" = []
    watches: "list[str]" = []
    # 配对段先行输出：MC-BUCKET-1 本体面在 worktree sparse 域按既有 fail-closed 语义
    # exit 4（放行登记 §六 rev-1 在册案型）＝配对段读数不得被后段 die 吞掉，先输出后跑本体。
    if args.seg in ("all", "pair"):
        pair_findings, n_close, n_verdict = scan_pair(root, args.bucket_root)
        for line in pair_findings:
            print(line)
        print("配对段：生效日 %s｜收口件在判 %d 枚｜判词件命中 %d 枚｜配对违例 %d"
              % (EFFECTIVE_DATE, n_close, n_verdict, len(pair_findings)))
    if args.seg in ("all", "bucket"):
        findings, watches = scan(root)
        for line in findings:
            print(line)
        for line in watches:
            print(line)
        n_dir = len([n for n in os.listdir(os.path.join(root, ".collab"))
                     if os.path.isdir(os.path.join(root, ".collab", n))])
        print("check-collab-buckets：一级目录判 %d 枚｜违例 %d｜名录对拍 %s"
              % (n_dir, len(findings), "一致" if not watches else "漂移"))
    return 1 if (findings or pair_findings or watches) else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed
        sys.stderr.write("infra error: %s\n" % exc)
        raise SystemExit(4)
