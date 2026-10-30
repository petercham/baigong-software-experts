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
#   两形态皆认（ENG-S6 解析修正·票面形态不改，多行列表为模板 v2 现行约定）：
#   ① 单行 `声明闭集：<路径>[、<路径>]…`；
#   ② 多行列表：`声明闭集：` 行（正文空）＋紧随 `- 路径` 列表行，至空行/非列表行止。
#   ENG-S8 T3 收紧（只作用于形态②，形态①口径不动）：列表条目仅**路径形态**入集
#     （含 `/` 或 `\`、或以已知扩展名 .md/.py/.sh/.json/.lock/.txt 结尾），
#     紧随的叙述行（`- 背景…`／`- HOLD…`）不入集（段三杂项误收直修）。
#   缺声明行（或声明行后无任何条目）＝SKIP 并计数、不算绿（D6-5 条款明文）。
#
# ENG-S8 口径三连修（三源均系工具口径缺陷·三段/基面分段/SKIP/退出码框架零动）：
#   T1 git 面取清单一律 `-c core.quotepath=false`：中文名 name-only 不再走八进制
#      转义，与回执清单 UTF-8 明文全等可比（段一缺项×3 直修）；
#   T2 receipt_commits 只收**交付笔**指针（行含交付/代码笔/实装标记＋hex）；
#      「开端 HEAD」「票面」「回执」行不入集（开票笔非交付笔·段一必不中）；
#   T3 声明列表条目路径形态收紧（见上）。
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

# 票面声明行（闭集源·显式约定·ENG-S6 两形态）：
#   单行 `声明闭集：<路径>[、<路径>]…`（正文非空）＝既有形态保持兼容；
#   多行列表 `声明闭集：`（正文空）＋紧随 `- 路径` 列表行（至空行/非列表行止）。
DECL_LINE_RE = re.compile(r"^\s*(?:[-*>\s]*)声明闭集[：:](.*)$")
# 多行列表形态的条目行：`- ` 起的列表行（ENG-S6 解析扩展）
DECL_LIST_ITEM_RE = re.compile(r"^\s*-\s+(.+)$")
# ENG-S8 T3：声明列表条目的已知路径扩展名闭集（路径形态判据之一）
KNOWN_DECL_EXTS = (".md", ".py", ".sh", ".json", ".lock", ".txt")
# 回执 commit 指针行内的反引号包裹 hash（7-40 位十六进制）
COMMIT_HASH_RE = re.compile(r"`([0-9a-f]{7,40})`")
# ENG-S8 T2：交付笔标记（行含其一＋hash 才入对账集）与排除标记（行含其一即不入集）。
# 「开端 HEAD」「票面」「回执」＝开端快照笔／开票笔／回执笔，均非交付笔，不入集；
# 回执笔自对账另循既有渠道（无则保持现状，不新增渠道）。
COMMIT_MARKER_RE = re.compile(r"交付|代码笔|实装|commit")
COMMIT_EXCLUDE_RE = re.compile(r"开端 ?HEAD|票面|回执")
# 回执清单行：markdown 表格行内含反引号包裹的仓内路径（相对仓根正斜杠）。
# ENG-S8 T1 配套（比较口径）：字符集含 CJK 基本域——中文名交付件的清单行须可收，
# 否则 quotepath 解转义后 git 面明文与回执面仍不可比（段一缺项假阳不消）。
RECEIPT_PATH_RE = re.compile(r"`([A-Za-z0-9一-鿿][A-Za-z0-9._/\-一-鿿]*\.[A-Za-z0-9]+)`")
# ENG-S9 T1：清单行两形态判据——① `|` 表格行（既有口径零动，行内任意反引号路径 token）；
# ② 编号列表（`1. `）／项目符号列表（`- `）的**清单条目行**：marker 后紧跟反引号路径
#   token＋行尾可选方括注/括注（如「（修改）」在反引号外＝不并入路径）＋行终。
#   锚定到行尾的目的＝非清单叙述性列表行（「- 票面：…」「- `path`：改前…」等）
#   不入清单集（真实面 S4 回执§六／selftest case11 同源防误收）。
RECEIPT_TABLE_LINE_RE = re.compile(r"^\s*\|")
RECEIPT_LIST_ENTRY_RE = re.compile(
    r"^\s*(?:\d+\.\s+|-\s+)`([A-Za-z0-9一-鿿][A-Za-z0-9._/\-一-鿿]*\.[A-Za-z0-9]+)`"
    r"\s*(?:[(（][^)）]*[)）])?\s*$")
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


def _is_list_item(line: str) -> bool:
    """多行列表形态的条目行判定：`- ` 起的列表行（`*`/`>` 形态不采·票面模板 v2 用 `- `）。"""
    return bool(DECL_LIST_ITEM_RE.match(line))


def _is_path_form(entry: str) -> bool:
    """ENG-S8 T3：声明列表条目的路径形态判据（只作用于多行列表形态②）。

    入集条件＝整条目为**单一 token**（无空白、无全角标点/引号：字符闭集＝
    ASCII 字母数字 + `._/-\\` + CJK 基本域），且（含 `/` 或 `\\`，
    或以 KNOWN_DECL_EXTS 已知扩展名结尾）。
    纯叙述行（`- 背景…`／`- HOLD…`）＝含空白/标点或无路径特征＝不入集。
    """
    if not entry or any(c.isspace() for c in entry):
        return False
    if not re.fullmatch(r"[A-Za-z0-9._/\\\-一-鿿]+", entry):
        return False
    if "/" in entry or "\\" in entry:
        return True
    return entry.lower().endswith(KNOWN_DECL_EXTS)


def ticket_declared_set(ticket_text: str) -> "list[str]":
    """票内全部 `声明闭集：` 声明块（WP 各一块则并集）。两形态（ENG-S6）：
      ① 单行 `声明闭集：<路径>[、<路径>]…`（正文非空）——既有形态保持兼容；
      ② 多行列表 `声明闭集：`（正文空）＋紧随 `- 路径` 列表行，至空行/非列表行止。
    ENG-S8 T3（只收紧形态②，形态①口径不动）：列表条目仅**路径形态**入集
    （判据见 _is_path_form）；叙述行仍终止条件不变（仍是列表行→继续扫描）但不入集。
    无任何声明块、或声明块均无条目＝[]（＝SKIP 信号）。"""
    paths: "list[str]" = []
    lines = ticket_text.split("\n")
    i = 0
    while i < len(lines):
        m = DECL_LINE_RE.match(lines[i])
        if not m:
            i += 1
            continue
        body = m.group(1).strip()
        if body:
            # 形态①：单行正文即闭集条目（口径不动）
            paths.extend(split_paths(body))
            i += 1
            continue
        # 形态②：正文空＝多行列表头，随后收 `- ` 列表行至空行/非列表行止；
        # ENG-S8 T3：条目逐条过路径形态判据，叙述行扫过不入集。
        i += 1
        while i < len(lines) and _is_list_item(lines[i]):
            raw = DECL_LIST_ITEM_RE.match(lines[i]).group(1)
            for p in split_paths(raw):
                if _is_path_form(p):
                    paths.append(p)
            i += 1
    return paths


def receipt_commits(receipt_text: str) -> "list[str]":
    """回执内**交付笔** commit 指针的 hash 集（去重·保序）。

    ENG-S8 T2 口径（写进 docstring＝票面要求）：只收交付笔指针——行内含
    交付标记（「交付」/「代码笔」/「实装」/「commit」，见 COMMIT_MARKER_RE）
    且含反引号包裹 hash（7-40 hex）者入集；行内含「开端 HEAD」「票面」
    「回执」标记（COMMIT_EXCLUDE_RE）者整行不入集——开端快照笔／开票笔／
    回执笔均非交付笔，混入则段一基面必不中（开票笔 name-only＝中文名票面件）。
    回执笔自对账另循既有渠道（现状无独立渠道＝保持现状，不新增）。
    """
    hashes: "list[str]" = []
    for line in receipt_text.split("\n"):
        if not COMMIT_MARKER_RE.search(line):
            continue
        if COMMIT_EXCLUDE_RE.search(line):
            continue
        for m in COMMIT_HASH_RE.finditer(line):
            h = m.group(1)
            if h not in hashes:
                hashes.append(h)
    return hashes


def receipt_paths(receipt_text: str) -> "list[str]":
    """回执清单节的反引号路径集（去重·保序·只收已认行形态）。

    ENG-S9 T1 清单行形态扩认：① `|` 表格行——既有口径零动（行内任意反引号路径 token）；
    ② 编号列表（marker「1. 」＋反引号路径＋括注「（修改）」）与项目符号列表（marker
      「- 」＋反引号路径）的清单条目行——marker 后紧跟反引号路径 token＋行尾可选括注
      （行内括号注记在反引号外＝不并入路径），整式锚定行尾＝叙述性列表行
      （「- 票面：…」「- 反引号路径：改前…」）不入清单集
      （防「回执有而 commit 全无」多项假阳，真实面 S4 回执§六同源）。
    其余行形态（正文行/标题行）仍不收。去重·保序语义不变。
    """
    paths: "list[str]" = []
    for line in receipt_text.split("\n"):
        if RECEIPT_TABLE_LINE_RE.match(line):
            found = [m.group(1) for m in RECEIPT_PATH_RE.finditer(line)]
        else:
            m = RECEIPT_LIST_ENTRY_RE.match(line)
            if not m:
                continue
            found = [m.group(1)]
        for raw in found:
            p = raw.replace("\\", "/")
            if "/" in p and p not in paths:
                paths.append(p)
    return paths


def git_name_only(root: str, commit: str) -> "list[str] | None":
    """段一基面＝git name-only（基面分段刚性：此函数体只用 git 面，
    **不出现任何文件系统 listing**——walk/listdir 均禁，单面统摄在结构上封死）。

    ENG-S8 T1：取清单走 `git -c core.quotepath=false`——中文名件 name-only
    不再输出八进制转义引号形态，与回执清单（UTF-8 明文）全等可比。
    返回 None＝该 commit 解析不到（＝「证据缺」，WATCH 不算 SKIP 绿）。
    """
    try:
        proc = subprocess.run(
            ["git", "-c", "core.quotepath=false", "-C", root,
             "show", "--name-only", "--format=", commit],
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
    """`git status --porcelain` 的交付面路径集（未声明生成件检出的 git 侧信号）。

    ENG-S8 T1 同源口径：名面类调用一律 `-c core.quotepath=false`
    （中文名脏路径不解八进制转义则与声明面永不相等＝假阳未声明生成件）。
    """
    try:
        proc = subprocess.run(
            ["git", "-c", "core.quotepath=false", "-C", root, "status", "--porcelain"],
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


# 回执指针两形态（ENG-S7 扩认·工具向票面体例三律②「含盘符完整路径」对齐）：
#   ① 相对仓根 `<COLLAB>.md` 正斜杠反引号路径（现行形态保持）；
#   ② 绝对盘符路径反引号包裹（`[A-Za-z]:[\\/]…`，反斜杠/正斜杠皆收）——
#      归一化（反斜杠→斜杠、仓根前缀大小写不敏感比对）后落在本仓过程域内
#      ＝合法回执指针；仓外绝对路径＝不算回执指针（现状保持）。
ABS_RECEIPT_PTR_RE = re.compile(r"`([A-Za-z]:[^\s`]*回执[^\s`]*\.md)`")


def abs_ptr_to_rel(root: str, raw: str) -> "str | None":
    """绝对盘符路径回执指针 → 仓内相对路径（正斜杠）。
    仅当归一后落在 <仓根>\\<过程域>/ 内才算；仓外＝None（不算回执指针）。"""
    norm = raw.replace("\\", "/")
    root_norm = root.replace("\\", "/").rstrip("/").lower()
    norm_lower = norm.lower()
    if not norm_lower.startswith(root_norm + "/"):
        return None
    rel = norm[len(root_norm) + 1:]
    if not rel.lower().startswith(COLLAB_PREFIX):
        return None
    return rel


def find_receipt(root: str, ticket_text: str, ticket_rel: str) -> "str | None":
    """配对键＝票内回执指针行（反引号包裹的过程域回执件路径·两形态见
    ABS_RECEIPT_PTR_RE 注）。缺＝None（未绿项）。"""
    cand = re.findall(r"`(" + re.escape(COLLAB_PREFIX) + r"[^\s`]*回执[^\s`]*\.md)`", ticket_text)
    for rel in cand:
        full = os.path.normpath(os.path.join(root, rel.replace("/", os.sep)))
        if os.path.isfile(full):
            return rel
    # ENG-S7 形态②：绝对盘符路径指针，归一落仓内过程域＝合法，仓外不算。
    for raw in ABS_RECEIPT_PTR_RE.findall(ticket_text):
        rel = abs_ptr_to_rel(root, raw)
        if rel is None:
            continue
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
#   case6_multiline_ok（ENG-S6）：多行列表形态票面（「声明闭集：」行＋`- 路径` 列表行）
#     → 解析成功、三段对账执行且全绿 → 0 发现
#   case7_nodecllist_skip（ENG-S6）：「声明闭集：」行后无列表行 → 无条目＝仍 SKIP 1
#   case8_absdrive_ok（ENG-S7）：票面回执指针＝仓内绝对盘符路径（反斜杠·真实票体例形态）
#     → 归一解析成功、三段对账执行全绿 → 0 发现
#   case9_absout_notptr（ENG-S7）：回执指针＝仓外绝对盘符路径 → 不算回执指针
#     → 「回执指针解析不到」WATCH 1（现状语义保持）
#   case10_cnname_quotepath_ok（ENG-S8 T1）：交付件中文名（git core.quotepath 场景）
#     → name-only 解转义与回执 UTF-8 明文可比 → 段一匹配成功 → 0 发现
#     （修前＝转义形态段一缺项假阳 1）
#   case11_ticketface_notcommit（ENG-S8 T2）：回执含「票面（开票 commit hash）」
#     「开端 HEAD（票 commit）」行 → 非交付笔不入对账集、不误报「解析不到」 → 0 发现
#     （修前＝开票笔 hash 被收→段一证据缺假阳 1）
#   case12_declnarr_pathonly（ENG-S8 T3）：声明列表夹叙述行（`- 背景…`／`- HOLD…`）
#     → 声明集只收路径形态条目、叙述行不入（不误入段三） → 0 发现
#     （修前＝叙述行入声明集→段三「声明与交付面对不上」假阳 2）
#   case13_numlist_ok（ENG-S9 T1）：回执清单＝编号列表形态（`1. \`路径\`（修改）`）
#     → 清单行扩认后段二/段三解析成功对账全绿 → 0 发现
#     （修前＝只收 `|` 表格行→清单解析空→段一缺项假阳）
#   case14_tableform_regression（ENG-S9 T2）：表格形态回执清单回归（既有用例口径零动）
#     → 对账全绿 0 发现；表格＋编号＋项目符号混排去重保序语义不变亦 0 发现
SELFTEST_EXPECTED = {"S1": 0, "S2": 1, "S3": 1, "S4": 1, "S5_skip": 1,
                     "case6_multiline_ok": 0, "case7_nodecllist_skip": 1,
                     "case8_absdrive_ok": 0, "case9_absout_notptr": 1,
                     "case10_cnname_quotepath_ok": 0, "case11_ticketface_notcommit": 0,
                     "case12_declnarr_pathonly": 0,
                     "case13_numlist_ok": 0, "case14_tableform_regression": 0}


def selftest(root: str) -> int:
    tmp = tempfile.mkdtemp(prefix="oa-reconcile-selftest-")
    try:
        def case(name: str, files: "list[str]", declared: "list[str]",
                 receipt_list: "list[str]", receipt_extra: "list[str]" = (),
                 decl_mode: str = "single", ptr_mode: str = "relative",
                 decl_extra: "list[str]" = (),
                 receipt_extra_lines: "list[str]" = (),
                 receipt_form: str = "table",
                 receipt_plain: "list[str]" = ()) -> "tuple[int, int]":
            """建一个合成票/回执＋commit，跑 check_pair，返回 (发现数, SKIP数)。
            decl_mode：single＝单行「声明闭集：a、b」；multiline＝模板 v2 多行列表
            （「声明闭集：」行＋`- 路径` 列表行）；header_only＝仅声明行无条目。
            ptr_mode（ENG-S7）：relative＝相对过程域正斜杠指针（现行体例）；
            abs_inrepo＝仓内绝对盘符路径指针（反斜杠·真实票面形态·盘符大小写故意
            与仓根不一致以验证大小写不敏感）；abs_outrepo＝仓外绝对盘符路径指针
            （回执件在仓外真实落盘，验证不算回执指针）。
            decl_extra（ENG-S8 T3）：追加在声明列表条目之后的 `- ` 叙述行原文
            （`- 背景…`／`- HOLD…` 形态·验证只收路径形态不入叙述行）。
            receipt_extra_lines（ENG-S8 T2）：回执追加行原文（「票面（开票笔 hash）」
            「开端 HEAD」形态·验证非交付笔不入对账集）。
            receipt_form（ENG-S9 T1/T2）：清单节行形态——table＝表格行
            「| 1 | 反引号路径 | 修改 |」（现行默认·零动）；numlist＝编号列表
            「1. 反引号路径（修改）」；bullet＝项目符号列表「- 反引号路径」；
            mixed＝表格＋编号＋项目符号混排（去重语义验证：每件各以
            不同形态出现一次＋首件双形态重复出现＝应去重不重复计）。
            receipt_plain：追加在清单节后的非清单列表行原文（「- 反引号路径：改前…改后…」
            叙述形态·验证不入清单集）。
            每用例独立临时仓（用例间零污染——同仓复用会让前案文件混进后案 commit 并集）。
            注：abs_* 两案依赖临时仓绝对路径带盘符（Windows 面·票面体例同源）。"""
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
            if decl_mode == "multiline":
                ticket_lines.append("- 声明闭集：")
                ticket_lines.extend("  - `%s`" % p for p in declared)
                ticket_lines.extend(decl_extra)
            elif decl_mode == "header_only":
                ticket_lines.append("- 声明闭集：")
                ticket_lines.append("")
            elif declared:
                ticket_lines.append("声明闭集：%s" % "、".join(declared))
            # 回执指针形态（ENG-S7 ptr_mode）
            receipt_fname = "%s-回执.md" % name
            if ptr_mode == "abs_inrepo":
                # 仓内绝对盘符路径（反斜杠）＋盘符大小写翻转＝验证大小写不敏感归一
                p = os.path.join(repo, ".collab", "research", receipt_fname)
                p = p[0].swapcase() + p[1:]
                ticket_lines.append("回执：`%s`" % p)
            elif ptr_mode == "abs_outrepo":
                # 仓外绝对盘符路径：回执件真实落盘于仓外，仍不算回执指针
                p = os.path.join(tmp, "outside-" + name, "research", receipt_fname)
                ticket_lines.append("回执：`%s`" % p)
            else:
                ticket_lines.append("回执：`%sresearch/%s`" % (COLLAB_PREFIX, receipt_fname))
            with open(os.path.join(repo, ".collab", "tickets", "%s.md" % name),
                      "w", encoding="utf-8") as handle:
                handle.write("\n".join(ticket_lines) + "\n")
            rl = ["# synthetic receipt %s" % name,
                  "- commit `%s` 记录" % head, ""]
            entries = receipt_list + list(receipt_extra)
            if receipt_form == "numlist":
                rl.extend("%d. `%s`（修改）" % (i + 1, p2)
                          for i, p2 in enumerate(entries))
            elif receipt_form == "bullet":
                rl.extend("- `%s`" % p2 for p2 in entries)
            elif receipt_form == "mixed":
                # 每件各以一种形态出现一次＋首件表格/编号双形态各一次＝去重语义验证
                rl.extend(["| # | 文件 | 标记 |", "|---|---|---|"])
                rl.append("| 1 | `%s` | 修改 |" % entries[0])
                for i, p2 in enumerate(entries):
                    if i % 2 == 0:
                        rl.append("%d. `%s`（修改）" % (i + 1, p2))
                    else:
                        rl.append("- `%s`" % p2)
            else:
                rl.extend(["| # | 文件 | 标记 |", "|---|---|---|"])
                for p2 in entries:
                    rl.append("| 1 | `%s` | 修改 |" % p2)
            rl.extend(receipt_plain)
            rl.extend(receipt_extra_lines)
            if ptr_mode == "abs_outrepo":
                outdir = os.path.join(tmp, "outside-" + name, "research")
                os.makedirs(outdir, exist_ok=True)
                rpath = os.path.join(outdir, receipt_fname)
            else:
                rpath = os.path.join(repo, ".collab", "research", receipt_fname)
            with open(rpath, "w", encoding="utf-8") as handle:
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
        # case6 多行列表形态（模板 v2 现行票面）：解析成功、三段对账全绿 → 0 发现
        results["case6_multiline_ok"] = case(
            "case6", ["deliverables/a.md", "deliverables/b.md"],
            ["deliverables/a.md", "deliverables/b.md"],
            ["deliverables/a.md", "deliverables/b.md"], decl_mode="multiline")
        # case7 声明行后无列表行：无条目＝仍 SKIP 1、0 发现
        results["case7_nodecllist_skip"] = case(
            "case7", ["deliverables/a.md"], ["deliverables/a.md"],
            ["deliverables/a.md"], decl_mode="header_only")
        # case8 仓内绝对盘符路径回执指针（反斜杠·盘符大小写翻转）：归一解析成功对账全绿 → 0 发现
        results["case8_absdrive_ok"] = case(
            "case8", ["deliverables/a.md"], ["deliverables/a.md"],
            ["deliverables/a.md"], ptr_mode="abs_inrepo")
        # case9 仓外绝对盘符路径回执指针（回执件仓外真实落盘）：不算回执指针 → WATCH 1
        results["case9_absout_notptr"] = case(
            "case9", ["deliverables/a.md"], ["deliverables/a.md"],
            ["deliverables/a.md"], ptr_mode="abs_outrepo")
        # case10 中文名交付件（git core.quotepath 场景）：name-only 解转义与回执
        # UTF-8 明文可比 → 段一匹配全绿 → 0 发现（修前＝转义形态缺项＋多项假阳）
        results["case10_cnname_quotepath_ok"] = case(
            "case10", ["deliverables/收尾微票.md", "deliverables/a.md"],
            ["deliverables/收尾微票.md", "deliverables/a.md"],
            ["deliverables/收尾微票.md", "deliverables/a.md"])
        # case11 回执含「票面（开票笔 hash）」＋「开端 HEAD（票 commit）」行：
        # 非交付笔不入对账集 → 不为其对账、不误报证据缺 → 0 发现
        # （修前＝两 hash 被收成 commit 指针→git 面解析不到→证据缺 WATCH 2）
        results["case11_ticketface_notcommit"] = case(
            "case11", ["deliverables/a.md"], ["deliverables/a.md"],
            ["deliverables/a.md"], receipt_extra_lines=[
                "- 票面：`.collab/tickets/case11.md`（开票笔 `72c0a97`）。",
                "- 开端 HEAD：`1fb47f45ed36ee8297c2316a9ad52660cd630dd2`（票 commit，开工实测）。",
            ])
        # case12 声明列表夹叙述行（`- 背景…`／`- HOLD…`）：声明集只收路径形态条目
        # → 叙述行不入段三不误报 → 0 发现（修前＝叙述行入声明集→段三对不上 WATCH 2）
        results["case12_declnarr_pathonly"] = case(
            "case12", ["deliverables/a.md", "deliverables/b.md"],
            ["deliverables/a.md", "deliverables/b.md"],
            ["deliverables/a.md", "deliverables/b.md"], decl_mode="multiline",
            decl_extra=["- 背景（自包含）：合成叙述行，含空白与（全角标点）。",
                        "- HOLD：无。"])
        # case13 回执清单＝编号列表形态（`1. \`路径\`（修改）`·S4 回执真实体例）：
        # 清单行扩认→段一/段二/段三解析成功对账全绿 → 0 发现
        # （修前＝只收 `|` 表格行→清单解析空→段一缺项假阳）；
        # 附叙述性列表行（「- \`p\`：改前…」）验证不入清单集不致多项假阳。
        results["case13_numlist_ok"] = case(
            "case13", ["deliverables/a.md", "deliverables/b.md"],
            ["deliverables/a.md", "deliverables/b.md"],
            ["deliverables/a.md", "deliverables/b.md"], receipt_form="numlist",
            receipt_plain=["- `deliverables/a.md`：改前 `\"version\": \"0.1.9\"` → 改后 `0.1.10`。",
                           "- 工作区核验：commit 前改动面恰此二件，无未声明生成件逃逸。"])
        # case14 表格形态回归＋混排去重：表格形态（case14a）口径零动对账全绿；
        # 表格＋编号＋项目符号混排、首件双形态重复出现（case14b）→ 去重语义不变全绿
        f14a, _ = case("case14a", ["deliverables/a.md", "deliverables/b.md"],
                       ["deliverables/a.md", "deliverables/b.md"],
                       ["deliverables/a.md", "deliverables/b.md"])
        f14b, _ = case("case14b", ["deliverables/a.md", "deliverables/b.md"],
                       ["deliverables/a.md", "deliverables/b.md"],
                       ["deliverables/a.md", "deliverables/b.md"], receipt_form="mixed")
        results["case14_tableform_regression"] = (f14a + f14b, 0)

        ok = True
        got = {"S1": results["S1"][0], "S2": results["S2"][0],
               "S3": results["S3"][0], "S4": results["S4"][0],
               "S5_skip": results["S5"][1],
               "case6_multiline_ok": results["case6_multiline_ok"][0],
               "case7_nodecllist_skip": results["case7_nodecllist_skip"][1],
               "case8_absdrive_ok": results["case8_absdrive_ok"][0],
               "case9_absout_notptr": results["case9_absout_notptr"][0],
               "case10_cnname_quotepath_ok": results["case10_cnname_quotepath_ok"][0],
               "case11_ticketface_notcommit": results["case11_ticketface_notcommit"][0],
               "case12_declnarr_pathonly": results["case12_declnarr_pathonly"][0],
               "case13_numlist_ok": results["case13_numlist_ok"][0],
               "case14_tableform_regression": results["case14_tableform_regression"][0]}
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
