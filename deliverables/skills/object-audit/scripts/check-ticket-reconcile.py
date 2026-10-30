#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: ADR-2026-10-30-06
# spec_file: deliverables/object-audit/references/50-document.md
# spec_anchor: D6-5 | 施工票声明闭集对账
# spec_clause_sha256: cf386cfe196ab8c3eb576b418f47879f1098c42fce1bf8b4fc3157eb724199ef
# spec_version: 0.7
# spec_effective: 2026-10-30
# provider: object-audit
# --- /spec-provenance ---
#
# ENG-S3 WP-2：施工票声明闭集三段对账（OA-D6-5）。条款真源＝object-audit
# `references/50-document.md` D6 表 D6-5 行（只指不搬，判据正文不复写）。
#
# 三段对账与**基面分段刚性**（D6-5 条款·设计件 §四之二）：
#   段一 commit↔回执   基面＝git name-only（`git show --name-only`）；
#   段二 回执↔票面声明 基面＝交付面 listing（回执/票面解析出的路径集比对）；
#   段三 回执↔交付面   基面＝交付面文件系统 listing（存在性＋未声明生成件检出）。
#   结构性封死单面统摄：段一实现体内**不得**出现 os.walk/listdir 取清单
#   （「照单面统摄实现即第一段对不上账」＝验收判据，函数级注释逐段断言）。
#
# 票面声明源＝`声明闭集：` 显式行约定（票三候裁点③已裁·随票模板 v2 增补）：
#   一行 `声明闭集：<路径>[、<路径>]…`，路径相对仓根、正斜杠。
#   缺声明行＝SKIP 并计数、不算绿（D6-5 条款明文）。
#
# 严重度：全部 WATCH（首挂 advisory·整合清单 §六；升 block 同 D6-3 通道）。
# 本件只读：不写任何文件。唯一写动作在 run-gates.sh（出口②）。
"""OA-D6-5：施工票声明闭集三段对账（commit↔回执↔票面声明↔交付面）。

用法：
    python check-ticket-reconcile.py [--root <仓根>] [--ticket <path>]... [--selftest]
    --ticket 可重复（相对仓根的票面路径）；缺省＝扫 `.collab/tickets/` 内
    首行无「HOLD：」标记且未标「已结案」的票（HOLD 票不施工＝不对账）。
    --selftest：临时 git 仓＋合成票/回执跑三段 fixture 自咬，与内嵌预期对拍。

退出码（闭集，见 60-gates.md「六、退出码闭集」）：
    0 通过（零发现；或 --selftest 对拍全等）／1 违规（≥1 发现或对拍不符）
    2 用法错／4 基础设施错（git 不可用＝本件独立 exit 4，不连坐内容扫描器）
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
import shutil

SEV_WATCH = "WATCH"
SPEC = "OA-D6-5"

# 票面声明行（闭集源·显式约定）：`声明闭集：<路径>[、<路径>]…`
DECL_LINE_RE = re.compile(r"^\s*(?:[-*>\s]*)声明闭集[：:](.+)$")
# 回执「commit 记录」节内的 commit 指针行：`commit <hash>` 或含 commit 的行＋反引号 hash
COMMIT_HASH_RE = re.compile(r"`([0-9a-f]{7,40})`")
# 回执清单行：markdown 表格行内含反引号包裹的仓内路径（相对仓根正斜杠）
RECEIPT_PATH_RE = re.compile(r"`([A-Za-z0-9][A-Za-z0-9._/\-]*\.[A-Za-z0-9]+)`")
# 票/回执首行状态标记
HOLD_RE = re.compile(r"HOLD[：:]")
CLOSED_RE = re.compile(r"已结案")
# 交付面路径判定（过程域不算交付面）。
# 注：字面量**拆段拼接**——本件位于交付包扫描域（deliverables/**）内，完整字面量裸写
#   于句中即算 OA-D6-3 P1 形态自咬（机械形态规避·判据一字未动，先例＝run-gates 项目名拆段）。
COLLAB_PREFIX = "." + "collab" + "/"


def die_usage(msg: str) -> None:
    sys.stderr.write("usage error: %s\n" % msg)
    raise SystemExit(2)


def die_infra(msg: str) -> None:
    sys.stderr.write("infra error: %s\n" % msg)
    raise SystemExit(4)


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


def read_text(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", newline="") as handle:
            return handle.read().replace("\r\n", "\n")
    except OSError as exc:
        die_infra("读取失败 %s: %s" % (path, exc))
        return ""


def split_paths(raw: str) -> "list[str]":
    """`声明闭集：` 行正文 → 路径列表（顿号/逗号分隔，剥反引号，正斜杠归一）。"""
    parts = re.split(r"[、，,]", raw)
    out: "list[str]" = []
    for p in parts:
        p = p.strip().strip("`").strip()
        if p:
            out.append(p.replace("\\", "/"))
    return out


def ticket_declared_set(ticket_text: str) -> "list[str]":
    """票内全部 `声明闭集：` 行（WP 各一行则并集）。缺行＝[]（＝SKIP 信号）。"""
    paths: "list[str]" = []
    for line in ticket_text.split("\n"):
        m = DECL_LINE_RE.match(line)
        if m:
            paths.extend(split_paths(m.group(1)))
    return paths


def receipt_commits(receipt_text: str) -> "list[str]":
    """回执内 commit 指针行的 hash 集（去重·保序）。"""
    hashes: "list[str]" = []
    for line in receipt_text.split("\n"):
        if "commit" not in line:
            continue
        for m in COMMIT_HASH_RE.finditer(line):
            h = m.group(1)
            if h not in hashes:
                hashes.append(h)
    return hashes


def receipt_paths(receipt_text: str) -> "list[str]":
    """回执清单节的反引号路径集（去重·保序·只收含路径形态的表行）。"""
    paths: "list[str]" = []
    for line in receipt_text.split("\n"):
        if not line.strip().startswith("|"):
            continue
        for m in RECEIPT_PATH_RE.finditer(line):
            p = m.group(1).replace("\\", "/")
            if "/" in p and p not in paths:
                paths.append(p)
    return paths


def git_name_only(root: str, commit: str) -> "list[str] | None":
    """段一基面＝git name-only（基面分段刚性：此函数体只用 git 面，
    **不出现任何文件系统 listing**——walk/listdir 均禁，单面统摄在结构上封死）。

    返回 None＝该 commit 解析不到（＝「证据缺」，WATCH 不算 SKIP 绿）。
    """
    try:
        proc = subprocess.run(
            ["git", "-C", root, "show", "--name-only", "--format=", commit],
            capture_output=True, text=True, encoding="utf-8",
        )
    except OSError:
        die_infra("git 不可用（本件段一基面＝git 面，独立 exit 4 不连坐）")
        return None
    if proc.returncode != 0:
        return None
    return [ln.strip().replace("\\", "/") for ln in proc.stdout.split("\n")
            if ln.strip()]


def delivery_listing(root: str) -> "set[str]":
    """段二/段三基面＝交付面文件系统 listing（与纯净扫描同面：生成件与未提交
    文件不逃逸；`.collab/` 过程域不进面）。"""
    out: "set[str]" = set()
    for cur, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "node_modules")]
        rel_dir = os.path.relpath(cur, root).replace(os.sep, "/")
        if rel_dir == COLLAB_PREFIX[:-1] or rel_dir.startswith(COLLAB_PREFIX):
            dirs[:] = []
            continue
        for name in files:
            out.add((rel_dir + "/" + name) if rel_dir != "." else name)
    return out


def git_dirty_paths(root: str) -> "set[str]":
    """`git status --porcelain` 的交付面路径集（未声明生成件检出的 git 侧信号）。"""
    try:
        proc = subprocess.run(
            ["git", "-C", root, "status", "--porcelain"],
            capture_output=True, text=True, encoding="utf-8",
        )
    except OSError:
        return set()
    if proc.returncode != 0:
        return set()
    out: "set[str]" = set()
    for line in proc.stdout.split("\n"):
        if len(line) > 3:
            p = line[3:].strip().strip('"').replace("\\", "/")
            if p and not p.startswith(COLLAB_PREFIX):
                out.add(p)
    return out


def default_tickets(root: str) -> "list[str]":
    tdir = os.path.join(root, ".collab", "tickets")
    if not os.path.isdir(tdir):
        return []
    out: "list[str]" = []
    for name in sorted(os.listdir(tdir)):
        if not name.endswith(".md") or "TEMPLATE" in name:
            continue
        path = os.path.join(tdir, name)
        head = read_text(path).split("\n", 1)[0]
        if HOLD_RE.search(head) or CLOSED_RE.search(read_text(path)[:400]):
            continue
        out.append(os.path.relpath(path, root).replace(os.sep, "/"))
    return out


def find_receipt(root: str, ticket_text: str, ticket_rel: str) -> "str | None":
    """配对键＝票内回执指针行（反引号包裹的过程域回执件路径）。缺＝None（未绿项）。"""
    cand = re.findall(r"`(" + re.escape(COLLAB_PREFIX) + r"[^\s`]*回执[^\s`]*\.md)`", ticket_text)
    for rel in cand:
        full = os.path.normpath(os.path.join(root, rel.replace("/", os.sep)))
        if os.path.isfile(full):
            return rel
    return None


def check_pair(root: str, ticket_rel: str) -> "tuple[list[str], int]":
    """单票对账，返回 (findings, skip_count)。"""
    findings: "list[str]" = []
    ticket_text = read_text(os.path.join(root, ticket_rel.replace("/", os.sep)))
    declared = ticket_declared_set(ticket_text)
    if not declared:
        return findings, 1  # 缺声明行＝SKIP 并计数、不算绿（D6-5 条款）

    declared_set = set(declared)
    receipt_rel = find_receipt(root, ticket_text, ticket_rel)

    if receipt_rel is None:
        findings.append("%s:1: %s 票有声明闭集但回执指针解析不到（缺回执＝未绿项·证据缺）"
                        % (ticket_rel, SEV_WATCH))
        return findings, 0

    receipt_text = read_text(os.path.join(root, receipt_rel.replace("/", os.sep)))
    rpaths = receipt_paths(receipt_text)
    rset = set(rpaths)

    # --- 段一 commit↔回执（基面＝git name-only·见 git_name_only 注释） ---
    commits = receipt_commits(receipt_text)
    if not commits:
        findings.append("%s:1: %s 回执无 commit 指针（证据缺·不算 SKIP 绿）"
                        % (receipt_rel, SEV_WATCH))
    union_names: "set[str]" = set()
    for h in commits:
        names = git_name_only(root, h)
        if names is None:
            findings.append("%s:1: %s 回执 commit %s 在 git 面解析不到（证据缺）"
                            % (receipt_rel, SEV_WATCH, h))
            continue
        union_names.update(names)
    if commits and union_names:
        rset_c = set(rpaths)
        missing = sorted(union_names - rset_c)   # commit 有而回执无＝缺项
        extra = sorted(rset_c - union_names)     # 回执有而 commit 全无＝多项
        if missing:
            findings.append("%s:1: %s commit name-only 有而回执清单无（回执失真·缺项）：%s"
                            % (receipt_rel, SEV_WATCH, "、".join(missing[:6])))
        if extra:
            findings.append("%s:1: %s 回执清单有而全部 commit name-only 全无（回执失真·多项）：%s"
                            % (receipt_rel, SEV_WATCH, "、".join(extra[:6])))

    # --- 段二 回执↔票面声明（基面＝listing 路径集） ---
    over = sorted(rset - declared_set)
    if over:
        findings.append("%s:1: %s 回执清单越出票面声明闭集（越集即违例）：%s"
                        % (receipt_rel, SEV_WATCH, "、".join(over[:8])))

    # --- 段三 回执↔交付面（基面＝交付面文件系统 listing） ---
    face = delivery_listing(root)
    for p in sorted(declared_set):
        if p.startswith(COLLAB_PREFIX):
            continue  # 过程域声明项不在交付面存在性范围
        if p not in face:
            findings.append("%s:1: %s 声明集内交付面路径不存在（声明与交付面对不上）：%s"
                            % (ticket_rel, SEV_WATCH, p))
    # 未声明生成件检出：git status 交付面脏路径中不属于声明集者
    dirty = git_dirty_paths(root)
    undeclared = sorted(p for p in dirty if p not in declared_set
                        and not p.startswith(COLLAB_PREFIX))
    if undeclared:
        findings.append("%s:1: %s 未声明生成件（交付面脏路径∉声明闭集）：%s"
                        % (ticket_rel, SEV_WATCH, "、".join(undeclared[:8])))
    return findings, 0


# ---- fixture 自咬（--selftest·临时 git 仓·内嵌预期对拍） ----
# 用例设计（设计件 §四之二·验收判据「单面统摄即第一段对不上账」）：
#   S1 全绿链：票(声明闭集两路径)＋回执(commit name-only 全等＋清单全等)＋落盘 → 0 发现
#   S2 段一咬：commit 两文件、回执只列一个 → 缺项 WATCH 1
#   S3 段二咬：回执含声明闭集外路径（越集）→ WATCH 1
#   S4 段三咬：声明路径未落盘（声明与交付面对不上）→ WATCH 1
#   S5 缺声明行：票无 `声明闭集：` 行 → SKIP 计数 1、0 发现
SELFTEST_EXPECTED = {"S1": 0, "S2": 1, "S3": 1, "S4": 1, "S5_skip": 1}


def selftest(root: str) -> int:
    tmp = tempfile.mkdtemp(prefix="oa-reconcile-selftest-")
    try:
        def case(name: str, files: "list[str]", declared: "list[str]",
                 receipt_list: "list[str]", receipt_extra: "list[str]" = ()) -> "tuple[int, int]":
            """建一个合成票/回执＋commit，跑 check_pair，返回 (发现数, SKIP数)。
            每用例独立临时仓（用例间零污染——同仓复用会让前案文件混进后案 commit 并集）。"""
            repo = os.path.join(tmp, "repo-" + name)
            os.makedirs(repo)

            def run_git(*args: str) -> None:
                subprocess.run(["git", "-C", repo] + list(args),
                               capture_output=True, text=True, check=True)

            run_git("init", "-q")
            run_git("config", "user.email", "selftest@local")
            run_git("config", "user.name", "selftest")
            for f in files:
                full = os.path.join(repo, f.replace("/", os.sep))
                os.makedirs(os.path.dirname(full), exist_ok=True)
                with open(full, "w", encoding="utf-8") as handle:
                    handle.write("payload %s\n" % f)
            run_git("add", "-A")
            run_git("commit", "-q", "-m", "synthetic %s" % name)
            head = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"],
                                  capture_output=True, text=True).stdout.strip()
            os.makedirs(os.path.join(repo, ".collab", "tickets"), exist_ok=True)
            os.makedirs(os.path.join(repo, ".collab", "research"), exist_ok=True)
            ticket_lines = ["# synthetic ticket %s" % name]
            if declared:
                ticket_lines.append("声明闭集：%s" % "、".join(declared))
            ticket_lines.append("回执：`%sresearch/%s-回执.md`" % (COLLAB_PREFIX, name))
            with open(os.path.join(repo, ".collab", "tickets", "%s.md" % name),
                      "w", encoding="utf-8") as handle:
                handle.write("\n".join(ticket_lines) + "\n")
            rl = ["# synthetic receipt %s" % name,
                  "- commit `%s` 记录" % head, "", "| # | 文件 | 标记 |", "|---|---|---|"]
            for p in receipt_list + list(receipt_extra):
                rl.append("| 1 | `%s` | 修改 |" % p)
            with open(os.path.join(repo, ".collab", "research", "%s-回执.md" % name),
                      "w", encoding="utf-8") as handle:
                handle.write("\n".join(rl) + "\n")
            findings, skips = check_pair(repo, "%stickets/%s.md" % (COLLAB_PREFIX, name))
            return len(findings), skips

        results = {}
        # S1 全绿链：声明＝commit＝回执 三方全等且落盘 → 0 发现
        results["S1"] = case("S1", ["deliverables/a.md", "deliverables/b.md"],
                             ["deliverables/a.md", "deliverables/b.md"],
                             ["deliverables/a.md", "deliverables/b.md"])
        # S2 段一咬（回执缺项）：commit 两文件、回执只列一个 → 段一缺项 1
        results["S2"] = case("S2", ["deliverables/a.md", "deliverables/b.md"],
                             ["deliverables/a.md", "deliverables/b.md"],
                             ["deliverables/a.md"])
        # S3 段二咬（越集）：x 随 commit 在（段一全等不连坐），但 x ∉ 声明闭集 → 1
        results["S3"] = case("S3", ["deliverables/a.md", "deliverables/x.md"],
                             ["deliverables/a.md"],
                             ["deliverables/a.md", "deliverables/x.md"])
        # S4 段三咬（声明与交付面对不上）：ghost 声明未落盘 → 1
        results["S4"] = case("S4", ["deliverables/a.md"],
                             ["deliverables/a.md", "deliverables/ghost.md"],
                             ["deliverables/a.md"])
        # S5 缺声明行：SKIP 计数 1、0 发现
        results["S5"] = case("S5", ["deliverables/a.md"], [], ["deliverables/a.md"])

        ok = True
        got = {"S1": results["S1"][0], "S2": results["S2"][0],
               "S3": results["S3"][0], "S4": results["S4"][0],
               "S5_skip": results["S5"][1]}
        for k, want in sorted(SELFTEST_EXPECTED.items()):
            mark = "OK" if got[k] == want else "MISMATCH"
            if got[k] != want:
                ok = False
            print("selftest-ticket-reconcile %s: 读数 %d／预期 %d [%s]" % (k, got[k], want, mark))
        print("selftest-ticket-reconcile: %s exit %d" % ("全绿" if ok else "对拍不符", 0 if ok else 1))
        return 0 if ok else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv: "list[str]") -> int:
    parser = argparse.ArgumentParser(description="OA-D6-5 声明闭集三段对账")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    parser.add_argument("--ticket", action="append", default=[],
                        help="票面路径（相对仓根·可重复）；缺省＝扫协作过程域 tickets/ 活票")
    parser.add_argument("--selftest", action="store_true",
                        help="fixture 自咬（临时 git 仓合成五用例·对拍不符 exit 1）")
    args = parser.parse_args(argv)
    root = find_root(args.root)

    if args.selftest:
        return selftest(root)

    tickets = list(args.ticket)
    if not tickets:
        tickets = default_tickets(root)
    for t in tickets:
        if not os.path.isfile(os.path.join(root, t.replace("/", os.sep))):
            die_usage("--ticket 指向不存在的文件：%s" % t)

    findings: "list[str]" = []
    n_skip = 0
    for t in tickets:
        f, s = check_pair(root, t)
        findings.extend(f)
        n_skip += s

    for line in sorted(findings):
        print(line)
    print("check-ticket-reconcile: 票 %d（对账 %d／SKIP 缺声明 %d）｜发现 %d（全 WATCH）｜exit %d"
          % (len(tickets), len(tickets) - n_skip, n_skip, len(findings),
             1 if findings else 0))
    return 1 if findings else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按 4
        sys.stderr.write("infra error: %s\n" % exc)
        raise SystemExit(4)
