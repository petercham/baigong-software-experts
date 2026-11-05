#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: OA-E-ADR-1
# spec_file: agent-skills/object-audit/references/50-document.md
# spec_anchor: E-ADR-1″ 头块断言：适用面＝`docs/adr/*.md`（项目内）；头 12 行内必含
# spec_clause_sha256: 991f1f4798839c5e7be24b2a7c3d3951bc917b7fd073baed4da4f9b8070f3257
# spec_version: 0.9
# spec_effective: 2026-11-05
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: OA-E-ADR-2
# spec_file: agent-skills/object-audit/references/50-document.md
# spec_anchor: E-ADR-2‴ 编号正断言＋唯一＋递增（v3.1 修）：
# spec_clause_sha256: 3b840421c581f7c671bdc1ca166fea42f8afb43bdaa8e9aba5512c0ee941a877
# spec_version: 0.9
# spec_effective: 2026-11-05
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: OA-E-ADR-3
# spec_file: agent-skills/object-audit/references/50-document.md
# spec_anchor: E-ADR-3″ 双向 supersede 全向校验（适用域＝docs/adr/ 集）：
# spec_clause_sha256: 8373d976034fc6e0b2b3c4b265aaa7b9da551a5d1961e5d9ae67a2366677128a
# spec_version: 0.9
# spec_effective: 2026-11-05
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: OA-E-ADR-4
# spec_file: agent-skills/object-audit/references/50-document.md
# spec_anchor: E-ADR-4″ accepted 不可变：适用域＝docs/adr 族限定（`docs/adr/*.md` 目录族——限定语义＝「只辖 ADR 族，不辖裁定登记族史实注记」）；
# spec_clause_sha256: 1a6bc3d2d2e56a0406ed393d4f0785642e76d5177d7d87d5cde2c66b86888e27
# spec_version: 0.9
# spec_effective: 2026-11-05
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: OA-E-ADR-5
# spec_file: agent-skills/object-audit/references/50-document.md
# spec_anchor: E-ADR-5‴ 三面对账（v3.1 修·桶互斥）：
# spec_clause_sha256: 4775ecbf0a6ef07cb28a03ac31f76b7160176fbed1691f6ce6fcf9e472ab1beb
# spec_version: 0.9
# spec_effective: 2026-11-05
# provider: object-audit
# --- /spec-provenance ---
#
# E-ADR 族校验器（ADR-L0 批实装·条款真源＝50-document.md「E-ADR ADR 族机检断言（docs/adr 面）」节，
# ES 定标终态 v2 A.3＋v3 §一-B＋v3.1 三修点逐字迁入；spec_id 进表形态＝OA-E-ADR-1…5（修订笔 R-1 换代）。
#
# 根锚定位闭集四序（ADR-L0 修订笔 黄-3 定死·fail-closed 不降级不计绿）：
#   ① --bundle-root 显式覆写
#   ② --root 参数目录内含 bundle.lock 即直用（该目录＝bundle 根）
#   ③ 缺省挂载态（run-gates 固定传 --root＝仓根）：自该根解 agent-experts/*/bundle.lock
#     （恰一处）读其 bundle.path 字段定为 bundle 根
#   ④ 四序皆空＝infra error exit 4（不降级不计绿——挂载态对仓根真空真之「摆设」路径被封）
# 四断言（含 E-ADR-5 三面对账）一律按 bundle 根算。仓根 .collab/decisions/（治理层搬家批
# 所设七件面）不在 E-ADR-5 射程——ES 定标与 ADR 工序链以 bundle 项目根为锚（候裁③射程裁量不变）。
#
# E-ADR-4/E-ADR-5 的 diff 面实现＝pre-commit 上下文取 `git diff --cached -- docs/adr/`
#   （run-gates 钩子环境内 staged 非空即在该上下文）；非该上下文跳过并在 coverage 行申报
#   「未执行」＝族件「未执行判据不得计绿」口径。
#
# 本件只读：不写任何文件（git 只跑只读子命令）。唯一写动作在 run-gates.sh（出口②）。
"""E-ADR 族校验：docs/adr 头块（E-ADR-1″）＋编号（E-ADR-2‴）＋双向 supersede（E-ADR-3″）
＋accepted 不可变（E-ADR-4″）＋三面对账（E-ADR-5‴）。

用法：
    python check-adr.py [--bundle-root <bundle根>] [--root <仓根|bundle根>]

退出码（闭集，见 60-gates.md「六、退出码闭集」）：
    0 通过（含 docs/adr 真空真）／1 违规／2 用法错／4 基础设施错（根锚四序皆空等）
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

SEV_BLOCK = "BLOCK"
SEV_WATCH = "WATCH"

ADR_SUBDIR = "docs/adr"
DECISIONS_SUBDIR = ".collab/decisions"
VERDICTS_REL = os.path.join(".collab", "decisions", "verdicts.md")

# E-ADR-2‴(0)：文件名正断言（四位制·NNNN-slug.md）
NAME_OK_RE = re.compile(r"^(\d{4})-[A-Za-z0-9._-]+\.md$")
NUM_PREFIX_RE = re.compile(r"^(\d{4})-")

# E-ADR-1″：头 12 行五行闭集（Date 行匹配前遮反引号——协议强制日期载体合法）
STATUS_RE = re.compile(r"^- Status：(Proposed|Accepted|Rejected|Deprecated|Superseded by .+)$")
DATE_RE = re.compile(r"^- Date：(YYYY|[0-9]{4})-[0-9]{2}-[0-9]{2}")
HEADER_LINES = ("^- Deciders：", "^- Author：", "^- Registrar：")
SUPERSEDES_RE = re.compile(r"^- Supersedes：(.*)$")

# E-ADR-3″ 补偿断言：adr 件内 .collab/… 案卷活引用（advisory 起步＝WATCH）
LIVE_REF_RE = re.compile(r"\.collab/[a-z]+/[^ )`\"']*\.md")

# E-ADR-4″ 注记引用式三式闭集（v3.1 黄-3）
NOTE_DATE_RE = re.compile(r"YYYY-MM-DD|[0-9]{4}-[0-9]{2}-[0-9]{2}")
REF_NNNN_RE = re.compile(r"^\d{4}-")
REF_LEGACY_RE = re.compile(r"ADR-\d{3}")
REF_CASEPATH_RE = re.compile(r"(?:^|\s)(?:\.collab/|docs/)\S+")


def die_usage(msg: str) -> None:
    sys.stderr.write("usage error: %s\n" % msg)
    raise SystemExit(2)


def die_infra(msg: str) -> None:
    sys.stderr.write("infra error: %s\n" % msg)
    raise SystemExit(4)


def read_text(path: str) -> str:
    """读文本并把 CRLF 归一为 LF（本仓 autocrlf=true，检出文件本身 CRLF）。"""
    try:
        with open(path, "r", encoding="utf-8", newline="") as handle:
            return handle.read().replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError) as exc:
        die_infra("读取失败 %s: %s" % (path, exc))


def resolve_bundle_root(bundle_root_arg: str | None, root_arg: str | None) -> str:
    """根锚四序（头注在册）：①--bundle-root ②--root 含 bundle.lock ③自解 bundle.lock
    ④皆空 fail-closed exit 4。"""
    # ① 显式覆写
    if bundle_root_arg:
        if not os.path.isdir(bundle_root_arg):
            die_usage("--bundle-root 不存在：%s" % bundle_root_arg)
        return os.path.abspath(bundle_root_arg)
    # ② --root 目录内含 bundle.lock 即直用
    if root_arg:
        if not os.path.isdir(root_arg):
            die_usage("--root 不存在：%s" % root_arg)
        root_abs = os.path.abspath(root_arg)
        if os.path.isfile(os.path.join(root_abs, "bundle.lock")):
            return root_abs
        # ③ 挂载态：自该根解 agent-experts/*/bundle.lock（恰一处）读 bundle.path
        locks = sorted(glob.glob(os.path.join(root_abs, "agent-experts", "*", "bundle.lock")))
        if len(locks) == 1:
            try:
                lock = json.loads(read_text(locks[0]))
            except ValueError as exc:
                die_infra("bundle.lock 解析失败 %s: %s" % (locks[0], exc))
            try:
                bpath = lock["bundle"]["path"]
            except (KeyError, TypeError):
                die_infra("bundle.lock 缺 bundle.path 字段：%s" % locks[0])
            bundle_root = os.path.normpath(os.path.join(root_abs, bpath))
            if not os.path.isdir(bundle_root):
                die_infra("bundle.path 指向目录不存在：%s" % bundle_root)
            return bundle_root
        if len(locks) > 1:
            die_infra("bundle.lock 多于一处（%d），不得猜用哪份：%s"
                      % (len(locks), ", ".join(os.path.relpath(x, root_abs).replace(os.sep, "/") for x in locks)))
    # ④ 四序皆空＝fail-closed
    die_infra("根锚四序皆空：无 --bundle-root、--root 不含 bundle.lock、自解 bundle.lock 无果（不降级不计绿）")


def git_lines(bundle_root: str, args: "list[str]") -> "list[str]":
    """git 只读子命令（-C bundle_root·-c core.quotepath=false）。失败＝infra exit 4。"""
    cmd = ["git", "-c", "core.quotepath=false", "-C", bundle_root] + args
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    except OSError as exc:
        die_infra("git 不可用：%s" % exc)
    if proc.returncode != 0:
        die_infra("git %s 失败（rc=%d）：%s" % (" ".join(args), proc.returncode, proc.stderr.strip()))
    return [l for l in proc.stdout.split("\n") if l.strip()]


def mask_backticks(line: str) -> str:
    """遮反引号段：反引号包裹内容保留文本但用于 Date 匹配前消去反引号字符本身。"""
    return line.replace("`", "")


def adr_files_on_disk(bundle_root: str) -> "list[str]":
    d = os.path.join(bundle_root, "docs", "adr")
    if not os.path.isdir(d):
        return []
    return sorted(n for n in os.listdir(d) if n.endswith(".md"))


def check_files(bundle_root: str, findings: "list[str]") -> "dict[int, str]":
    """E-ADR-1″/2‴/3″（＋3″ 补偿断言 WATCH）对盘上 docs/adr/*.md 全族。"""
    names = adr_files_on_disk(bundle_root)
    rel = lambda n: (ADR_SUBDIR + "/" + n)
    # --- E-ADR-2‴ (0) 正断言 ---
    bad_names = [n for n in names if not NAME_OK_RE.match(n)]
    for n in bad_names:
        findings.append("%s:1: %s OA-E-ADR-2 文件名不符正断言 ^(\\d{4})-[A-Za-z0-9._-]+\\.md$：%s"
                        % (rel(n), SEV_BLOCK, n))
    good = [n for n in names if NAME_OK_RE.match(n)]
    # --- E-ADR-2‴ (1) 提取集唯一 (2) 递增（对账集＝正断言通过者）---
    nums = [int(NUM_PREFIX_RE.match(n).group(1)) for n in good]
    seen: "dict[int, int]" = {}
    for n in nums:
        seen[n] = seen.get(n, 0) + 1
    for n, c in sorted(seen.items()):
        if c > 1:
            findings.append("%s:1: %s OA-E-ADR-2 编号 %04d 重复 occurrence=%d" % (ADR_SUBDIR, SEV_BLOCK, n, c))
    if seen and sorted(seen) != list(range(min(seen), max(seen) + 1)):
        findings.append("%s:1: %s OA-E-ADR-2 编号集不连续（跳号）：%s"
                        % (ADR_SUBDIR, SEV_BLOCK, ",".join("%04d" % x for x in sorted(seen))))
    # --- 逐件读头块 ---
    headers: "dict[str, dict[str, str]]" = {}
    for n in good:
        path = os.path.join(bundle_root, "docs", "adr", n)
        lines = read_text(path).split("\n")[:12]
        headers[n] = {}
        masked = [mask_backticks(l) for l in lines]
        if not any(STATUS_RE.match(m) for m in masked):
            findings.append("%s:1: %s OA-E-ADR-1 头 12 行缺 Status 闭集行" % (rel(n), SEV_BLOCK))
        date_hit = any(DATE_RE.match(m) for m in masked)
        if not date_hit:
            findings.append("%s:1: %s OA-E-ADR-1 头 12 行缺 Date：YYYY-MM-DD 行（遮反引号后匹配）" % (rel(n), SEV_BLOCK))
        for pref in HEADER_LINES:
            key = pref[len("^- "):pref.index("：")]
            if not any(m.startswith("- %s：" % key) for m in masked):
                findings.append("%s:1: %s OA-E-ADR-1 头 12 行缺 %s：行" % (rel(n), SEV_BLOCK, key))
        status_line = next((m for m in masked if STATUS_RE.match(m)), "")
        supersedes_line = next((m for m in masked if SUPERSEDES_RE.match(m)), "")
        headers[n]["status"] = status_line
        headers[n]["supersedes"] = supersedes_line
    # --- E-ADR-3″ 双向 supersede 全向校验（图节点身份＝四位编号）---
    num_of_file = {n: NUM_PREFIX_RE.match(n).group(1) for n in good}
    file_of_num = {v: k for k, v in num_of_file.items()}

    def num_in_ref(ref: str) -> str:
        m = re.search(r"\d{4}", ref)
        return m.group(0) if m else ""

    for n in good:
        own = num_of_file[n]
        st = headers[n].get("status", "")
        m = re.search(r"Superseded by (.+)$", st)
        if m:
            tgt = file_of_num.get(num_in_ref(m.group(1)), "")
            if not tgt:
                findings.append("%s:1: %s OA-E-ADR-3 悬空 supersede：Status 指 %r 不在盘" % (rel(n), SEV_BLOCK, m.group(1)))
            else:
                ts = headers[tgt].get("supersedes", "")
                if not ts or own not in ts:
                    findings.append("%s:1: %s OA-E-ADR-3 新→旧回指缺边：%s 无指回本案（%s）的 Supersedes 行"
                                    % (rel(n), SEV_BLOCK, tgt, own))
        sup = headers[n].get("supersedes", "")
        sm = SUPERSEDES_RE.match(sup) if sup else None
        if sm and sm.group(1).strip():
            tgt = file_of_num.get(num_in_ref(sm.group(1)), "")
            if not tgt:
                findings.append("%s:1: %s OA-E-ADR-3 Supersedes 指 %r 不在盘" % (rel(n), SEV_BLOCK, sm.group(1)))
            else:
                tstatus = headers[tgt].get("status", "")
                if own not in tstatus:
                    findings.append("%s:1: %s OA-E-ADR-3 旧→新向缺边：%s Status 未含本案引用（%s）" % (rel(n), SEV_BLOCK, tgt, own))
    # --- E-ADR-3″ 补偿断言（advisory 起步＝WATCH）---
    for n in good:
        body = read_text(os.path.join(bundle_root, "docs", "adr", n))
        for ref in LIVE_REF_RE.findall(body):
            # 案卷引用按 bundle 根解析（ES 锚 bundle 项目根·候裁③射程口径）
            if not os.path.isfile(os.path.join(bundle_root, ref.replace("/", os.sep))):
                findings.append("%s:1: %s OA-E-ADR-3 adr 内案卷活引用解析不到（补偿断言·advisory）：%s"
                                % (rel(n), SEV_WATCH, ref))
    return headers


def check_diff_surface(bundle_root: str, findings: "list[str]") -> "tuple[bool, str]":
    """E-ADR-4″ diff 白名单＋E-ADR-5‴ 删除行断言——pre-commit 上下文（staged 非空）内执行。
    返回 (是否执行, 未执行原因)。"""
    try:
        proc = subprocess.run(
            ["git", "-c", "core.quotepath=false", "-C", bundle_root, "diff", "--cached", "--name-only"],
            capture_output=True, text=True, encoding="utf-8")
    except OSError:
        return False, "git 不可用"
    if proc.returncode != 0:
        return False, "git diff --cached 不可读（非 pre-commit 上下文）"
    if not [l for l in proc.stdout.split("\n") if l.strip()]:
        return False, "staged 为空（非 pre-commit 上下文）"
    ns = git_lines(bundle_root, ["diff", "--cached", "--name-status", "--", ADR_SUBDIR])
    for row in ns:
        parts = row.split("\t")
        if len(parts) < 2:
            continue
        state, path = parts[0], parts[-1]
        name = path.rsplit("/", 1)[-1]
        if state.startswith("D"):
            findings.append("%s:1: %s OA-E-ADR-5 删除行 BLOCK 断言：docs/adr 族出现 %s 删除（%s）"
                            % (path, SEV_BLOCK, state, name))
            continue
        if state.startswith("A") and name not in adr_files_on_disk(bundle_root):
            findings.append("%s:1: %s OA-E-ADR-1 staged 新增 adr 件不在盘：%s" % (path, SEV_BLOCK, name))
            continue
        if state.startswith("M"):
            # E-ADR-4″：修改面白名单＝Status 行＋Supersedes 行＋文末追加注记行
            diff = git_lines(bundle_root, ["diff", "--cached", "--", path])
            removed = [l[1:] for l in diff if l.startswith("-") and not l.startswith("---")]
            added = [l[1:] for l in diff if l.startswith("+") and not l.startswith("+++")]
            def is_whitelisted(line: str) -> bool:
                s = line.strip()
                if s.startswith("- Supersedes："):
                    return True
                sm = STATUS_RE.match(mask_backticks(s))
                if sm:
                    return True
                # 文末追加注记行：必含日期戳＋触发件引用三式闭集
                if NOTE_DATE_RE.search(s) and (REF_NNNN_RE.search(s) or REF_LEGACY_RE.search(s)
                                               or REF_CASEPATH_RE.search(s)):
                    return True
                return False
            for l in removed:
                if not is_whitelisted(mask_backticks(l)):
                    findings.append("%s:1: %s OA-E-ADR-4 accepted 不可变：删除/改写白名单外行：%s"
                                    % (path, SEV_BLOCK, l[:80]))
            # 追加行须为注记行或 Status/Supersedes 替换（追加＝新增行 only 的行级判定）
            removed_norm = {mask_backticks(x).strip() for x in removed}
            for l in added:
                s = mask_backticks(l).strip()
                if s in removed_norm:
                    continue  # 替换对（Status/Supersedes 行改写）——白名单内已核
                if not is_whitelisted(s):
                    findings.append("%s:1: %s OA-E-ADR-4 accepted 不可变：追加白名单外行：%s"
                                    % (path, SEV_BLOCK, l[:80]))
        # staged 新增件全族一致性由 check_files 盘上断言覆盖
    # E-ADR-5‴ 删除行断言·decisions 桶
    ns2 = git_lines(bundle_root, ["diff", "--cached", "--name-status", "--", DECISIONS_SUBDIR])
    for row in ns2:
        parts = row.split("\t")
        if len(parts) >= 2 and parts[0].startswith("D"):
            findings.append("%s:1: %s OA-E-ADR-5 删除行 BLOCK 断言：decisions 族出现 %s 删除（%s）"
                            % (parts[-1], SEV_BLOCK, parts[0], parts[-1].rsplit("/", 1)[-1]))
    return True, ""


def check_sum(bundle_root: str, findings: "list[str]") -> "tuple[int, int, int]":
    """E-ADR-5‴ 三面对账（桶互斥和式）——对账集＝git ls-files（tracked 面）。"""
    b1 = git_lines(bundle_root, ["ls-files", ADR_SUBDIR + "/"])
    b2_all = git_lines(bundle_root, ["ls-files", DECISIONS_SUBDIR + "/"])
    b2 = [p for p in b2_all if not re.search(r"decisions/verdicts\.md$", p)]
    b3 = [p for p in b2_all if re.search(r"decisions/verdicts\.md$", p)]
    for p in b1:
        if not os.path.isfile(os.path.join(bundle_root, p.replace("/", os.sep))):
            findings.append("%s:1: %s OA-E-ADR-5 桶1 缺名在盘断言：tracked 而不在盘 %s" % (p, SEV_BLOCK, p))
    for p in b2:
        if not os.path.isfile(os.path.join(bundle_root, p.replace("/", os.sep))):
            findings.append("%s:1: %s OA-E-ADR-5 桶2 逐名清单对账：tracked 而不在盘 %s" % (p, SEV_BLOCK, p))
    if len(b3) > 1:
        findings.append("%s:1: %s OA-E-ADR-5 桶3 verdicts.md 应恰单件，tracked=%d" % (VERDICTS_REL, SEV_BLOCK, len(b3)))
    if b3 and not os.path.isfile(os.path.join(bundle_root, VERDICTS_REL)):
        findings.append("%s:1: %s OA-E-ADR-5 桶3 verdicts.md tracked 而不在盘" % (VERDICTS_REL, SEV_BLOCK))
    total = git_lines(bundle_root, ["ls-files", ADR_SUBDIR + "/", DECISIONS_SUBDIR + "/"])
    if len(b1) + len(b2) + len(b3) != len(total):
        findings.append("%s:1: %s OA-E-ADR-5 和式断言不符：桶1+桶2+桶3=%d+%d+%d≠和式=%d"
                        % (ADR_SUBDIR, SEV_BLOCK, len(b1), len(b2), len(b3), len(total)))
    return len(b1), len(b2), len(b3)


def main() -> int:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--bundle-root", default=None, help="bundle 根显式覆写（四序①）")
    parser.add_argument("--root", default=None, help="仓根或 bundle 根（四序②③入口；run-gates 缺省传仓根）")
    args = parser.parse_args()

    bundle_root = resolve_bundle_root(args.bundle_root, args.root)

    findings: "list[str]" = []
    check_files(bundle_root, findings)
    diff_ran, diff_skip_reason = check_diff_surface(bundle_root, findings)
    b1, b2, b3 = check_sum(bundle_root, findings)

    for line in findings:
        print(line)
    print("check-adr: bundle 根＝%s｜docs/adr 盘上件=%d｜桶1=%d 桶2=%d 桶3=%d｜发现 %d｜exit %d"
          % (bundle_root.replace(os.sep, "/"), len(adr_files_on_disk(bundle_root)),
             b1, b2, b3, len(findings), 1 if findings else 0))
    if not diff_ran:
        print("check-adr coverage: E-ADR-4″ 本次未执行（%s）——未执行判据不得计绿" % diff_skip_reason)
    return 1 if findings else 0


try:
    raise SystemExit(main())
except SystemExit:
    raise
except Exception as exc:  # fail-closed：未预期异常按 4，不得吞成 0
    sys.stderr.write("infra error: %s\n" % exc)
    raise SystemExit(4)
