#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: OA-D6
# spec_file: agent-skills/object-audit/references/50-document.md
# spec_anchor: D6 引用完整性
# spec_clause_sha256: f120944580b54d49028ebe020584cdabfd644ebc0a5535bf930d4ec890db0751
# spec_version: 0.2
# spec_effective: 2026-10-22
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: OA-D8-4
# spec_file: agent-skills/object-audit/references/50-document.md
# spec_anchor: D8-4 | 索引对账
# spec_clause_sha256: ab73896dfbdadb735a6dd003b52382241b43bc7f67afc65d609ed4ddc5035953
# spec_version: 0.2
# spec_effective: 2026-10-22
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: OB-DIR-3
# spec_file: agent-skills/object-build/references/50-directory.md
# spec_anchor: ①工具契约目录名零自造
# spec_clause_sha256: cb4060880c8ff325eef4fd0ebb35d931c47e74bb16b4b7c692a0f378285f851f
# spec_version: 0.3
# spec_effective: 2026-10-22
# provider: object-build
# --- /spec-provenance ---
#
# 条款摘要口径（与 S-04 共用·写死在此以免两处实现漂移）：
#   取 spec_anchor 在 spec_file 中命中的那一行 → 去首尾空白 → 连续空白压成单个空格
#   → UTF-8 编码 → sha256（十六进制小写）。行号不参与定位，也不入判据。
#
# S-02 指针完整性与索引对账（OA-D6／OA-D8-4／OB-DIR-③）。
#
# 本件只跑这三条规则。**OA-D6-2（指针禁用序号定位）不在本件内**：该条款在
# `50-document.md` 里尚不存在，按设计 v2 §2.5.1 自举约束（规范先于脚本），
# 条款落盘前代码里不得出现 D6-2 检查路径。
#
# 严重度照抄规范，本件不做策略判断：
#   OA-D6／OA-D8-4 在 60-gates.md 路由表里配 advisory（依据状态＝缺），
#   但 SEV 由规范侧定：悬空＝阻断（50-document.md「判定要点」阻断清单含 D6 类悬空），
#   孤儿＝关注（D8-4 未列阻断清单）。此处 SEV 照抄规范，拦不拦由 run-gates.sh 按表决定。
#
# 本件只读：不写任何文件。唯一写动作在 run-gates.sh（出口②）。
"""S-02：扫仓内 md 的反引号路径与 file:line 引用是否悬空（OA-D6），并对账索引↔磁盘（OA-D8-4／OB-DIR-③）。

用法：
    python check-pointers.py [--root <仓根>] [--scope <相对目录>]... [--target <file>]...

默认扫描域＝三分类目录（`agent-experts/`＋`agent-skills/`＋`softwares/`，SWB-B2 换代；
`.collab/` 按裁-23 拍板 2 排除；显式入口见 DEFAULT_SCOPE 处注释）。

退出码（闭集，见 60-gates.md「六、退出码闭集」）：
    0 通过／1 违规（悬空或孤儿）／2 用法错／4 基础设施错
"""

from __future__ import annotations

import argparse
import os
import re
import sys

SEV_BLOCK = "BLOCK"
SEV_WATCH = "WATCH"

# 扫描域（裁-23 拍板 2＋SWB-B2 换代）：默认只扫规范文档面三分类目录，**排除 `.collab/`**——
# 与 S-03 同款划界：记录件 informative、不要求干净（append-only 史实锚里的指针
# 改不动也不该由门禁拦）。默认排除 ≠ 不能查，显式入口保留：
#   --scope .collab   追加扫描域（解析锚仍为仓根，指针照常解析）
#   --root .collab    指过去核查（脚本自动上溯仓根做解析锚，见 main 内注释）
#   --target <file>   直接指定文件核查
DEFAULT_SCOPE = ("agent-experts", "agent-skills", "softwares")

# 反引号内联代码：`...`（不跨行）。
BACKTICK_RE = re.compile(r"`([^`\n]+)`")
# 行内引用形如 foo.md:12 / references/a.py:3 —— 冒号后的行号只作人读，不参与存在性判定。
FILE_LINE_RE = re.compile(r"^(?P<path>[^\s:]+):(?P<line>\d+)$")
# 看起来像路径：含斜杠，或以已知文档/脚本扩展名结尾。
CANDIDATE_EXT = (".md", ".py", ".sh", ".json", ".state", ".txt", ".yaml", ".yml")

# 反引号里这些内容不是路径，直接跳过（示例、占位、纯锚点、命令片段）。
SKIP_EXACT = {".", "..", "/", "…", "...", "~"}
SKIP_SUBSTR = ("<", ">", " ", "*", "|", "…", "${", "$(", "==", "!=", "->", "=>", "::")

# 本仓指针写法常在路径后紧跟中文注解（`path「判定要点」`／`path（说明）`），
# 解析时先剥掉注解部分，否则每个带注解的活指针都会被误判悬空（假报淹真报）。
ANNOTATION_RE = re.compile(r"[「（(\[、，,；;：:].*$")

# 外部仓注明串（D6 裁-21 划界：外部仓引用**应在文中注明**，注明者不入悬空判定）。
EXTERNAL_MARK = "外部仓"

# 这四种写法**语法上就不是仓内相对路径**，不参与悬空判定（与 SKIP_* 同类的形态判定，
# 不是"猜它是不是外部项目"的语义判断——语义判断脚本无权做，见 60-gates.md §〇 铁律 1）：
#   `~/.claude/settings.json`            家目录路径，天然在仓外
#   `raw.githubusercontent.com/a/b/c.md` 带域名的 URL（首段含点且像域名）
#   `pingcap/tidb@master:PLANS.md`       git 引用（`repo@ref:path`）
#   `https://example.com/a/b/`           scheme 前缀 URL（带 `://`，`https:` 段含冒号不匹配 URL_PATH_RE）
HOME_PATH_RE = re.compile(r"^~(/|$)")
URL_PATH_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.-]*\.[A-Za-z]{2,}/")
GIT_REF_RE = re.compile(r"@")
# scheme 前缀 URL（T9 复跑实证漏网形态：`https://…/` 带尾斜杠曾误入目录路径放行分支）。
# 与 HOME_PATH_RE/URL_PATH_RE/GIT_REF_RE 同族＝语法形态判定，非语义判断（铁律 1）。
SCHEME_PREFIXES = ("http://", "https://", "ftp://")


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
        if os.path.isdir(os.path.join(cur, "tools")) and any(
                os.path.isdir(os.path.join(cur, c))
                for c in ("agent-experts", "agent-skills", "softwares")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            die_usage("未能定位仓根；请用 --root 指定")
        cur = parent


def looks_like_path(token: str) -> bool:
    """判定反引号内容是否「意图指向仓内文件」。判不准的一律不当路径（宁漏不误报）。"""
    tok = token.strip()
    if not tok or tok in SKIP_EXACT:
        return False
    if tok.startswith("#") or tok.startswith("@"):
        return False
    if tok.startswith(SCHEME_PREFIXES):
        return False
    if tok.endswith(":"):
        return False
    # 家目录路径／带域名的 URL／git 引用（`repo@ref:path`）——语法上就不是仓内相对路径。
    if HOME_PATH_RE.match(tok) or URL_PATH_RE.match(tok) or GIT_REF_RE.search(tok):
        return False
    # `.git/` 下是每台机器的本机配置，规范明写"钩子文件本身不入仓"
    # （60-gates.md §一），它不是仓内指针。
    if tok.startswith(".git/"):
        return False
    # file:line 形态允许（去掉行号后判定文件部分）。
    match = FILE_LINE_RE.match(tok)
    if match:
        tok = match.group("path")
    # 含空格/通配/管道等的一律不是具体路径（多为示例或表格分隔）。
    for bad in SKIP_SUBSTR:
        if bad in tok:
            return False
    if tok.startswith("/") or re.match(r"^[A-Za-z]:", tok):
        return False  # 绝对路径与盘符路径不在本判据射程（跨机不可判）
    if "/" in tok:
        # 带斜杠但既无已知扩展名也不以 `/` 结尾的，多为标识符/外部示例/URL
        # （如 `tools/list`、`src/tests/benches`、`user/repo`），判不准＝不当路径。
        if not tok.endswith(CANDIDATE_EXT) and not tok.endswith("/"):
            return False
    else:
        # 裸文件名：须以已知扩展名结尾且文件名主体非空（排除 `.md` 这类纯扩展名提及）。
        if not tok.endswith(CANDIDATE_EXT):
            return False
        stem = tok[: -len(tok.rsplit(".", 1)[1]) - 1]
        if not stem:
            return False
    return True


def build_indexes(root: str) -> "tuple[dict[str, int], list[str]]":
    """单次仓根 walk 同建两索引（FX-U28 性能口径＝两索引合并为单次 walk）：

    1. 基名索引：仓内文件基名 → 命中数（供「只写基名」的指针做存在性判定）。
       为什么需要它：本仓大量指针只写基名（README 索引行、分件互指、裁决记录）。
       D6 只问「所指目标存在」，故基名在仓内命中 ≥1 即算存在；命中 0 才是悬空。
       基名歧义（同名多份）是**另一种**失效，D6 未定义它、路由表里也没有对应
       `spec_id`，本首批不报（不越设计 §2.5 清单扩面，不自造判据）。
    2. 后缀路径索引：仓内全部文件的仓根相对路径（正斜杠形态）列表
       （供「FX-U28 唯一命中归位层」做后缀唯一匹配计数，口径见该层注释）。

    索引域＝**整个仓根**（不是 md 扫描域）：指针可以指向 `.gitignore`、`package.json`
    这类扫描域外的文件；只在扫描域内建索引会把它们误判悬空。
    剪枝目录集＝两索引共有（.git／__pycache__／node_modules）——基名索引口径照基线一字不动（零回归臂）。
    后缀路径索引另除外仓根 `.scratch/` 族＝工序取证面非实物真源（D-94 产物级复现指针
    禁指 .scratch 族＋本票 §〇 样本读数口径「仓根（非 scratch 面）后缀命中」写死——
    他案 scratch 内 worktree 副本计入会把唯一命中族人为多义化，样本判据即自相矛盾）。
    索引随单次运行构建一次复用（与基名索引同生命周期）。
    """
    index: "dict[str, int]" = {}
    relpaths: "list[str]" = []
    for cur, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "node_modules")]
        for name in files:
            index[name] = index.get(name, 0) + 1
            rp = os.path.relpath(os.path.join(cur, name), root).replace(os.sep, "/")
            if rp == ".scratch" or rp.startswith(".scratch/"):
                continue  # 基名索引照基线含 scratch 面；后缀索引不入 scratch 族
            relpaths.append(rp)
    return index, relpaths


def strip_pointer_form(token: str) -> str:
    """token → 相对路径段（剥 file:line 行号 → 剥尾随注解 → 剥 `./` 前缀）。

    七候选层与后缀归位层共用本函数＝行号剥离口径一致（FX-U28 S1 条款四）。
    剥完为空＝整段是注解（调用方按 annotation-only 处理）。
    """
    raw = token.strip()
    match = FILE_LINE_RE.match(raw)
    rel = match.group("path") if match else raw
    # 剥掉路径后紧跟的中文注解（`50-document.md「判定要点」`），否则活指针误判悬空。
    rel = ANNOTATION_RE.sub("", rel).strip()
    if rel.startswith("./"):
        rel = rel[2:]
    return rel


def resolve(token: str, root: str, md_path: str, basename_index: "dict[str, int]") -> "str | None":
    """把相对 token 解析成仓内绝对路径候选；全部落空返回 None（＝悬空）。

    候选顺序按本仓既有指针写法（**只解析路径，不复写规范、不猜外部路径**）：
      1. 相对本文件（同目录引用，如 `40-deployment.md`）
      2. 相对仓根（全路径写法，如 `agent-skills/multi-collab/references/40-deployment.md`）
      3. 相对三分类分类目录（**跨包短写法**，如 `object-audit/references/70-provenance.md`；
         60-gates.md §四对账表与 60-publish.md 均用此式，不认它会把活指针全判悬空）
      4. 相对本文件所在包根（包内跨目录引用，如 `references/20-handoff.md`）
      5. 本文件同级的 `references/`（SKILL.md 只写基名指分件）
      6. 同目录同名（兜底：`SKILL.md:14` 这类只写文件名的引用）
      7. 纯基名（不含斜杠）退到全仓基名存在性判定
    **不设"外部路径豁免"规则**（理由见函数体内注释）：解析不到就照实报悬空。
    """
    rel = strip_pointer_form(token)
    if not rel:
        return "annotation-only"  # 剥完为空＝整段是注解，不是路径指针
    here = os.path.dirname(md_path)
    pkg_root = os.path.dirname(here)  # references/x.md 的包根
    candidates = [
        os.path.normpath(os.path.join(here, rel)),
        os.path.normpath(os.path.join(root, rel)),
        # 三分类目录（SWB-B2 换代）：跨包短写法按分类目录候选
        os.path.normpath(os.path.join(root, "agent-experts", rel)),
        os.path.normpath(os.path.join(root, "agent-skills", rel)),
        os.path.normpath(os.path.join(root, "softwares", rel)),
        os.path.normpath(os.path.join(pkg_root, rel)),
        os.path.normpath(os.path.join(here, "references", os.path.basename(rel))),
        os.path.normpath(os.path.join(here, os.path.basename(rel))),
    ]
    for cand in candidates:
        if os.path.exists(cand):
            return cand
    if "/" not in rel:
        # 纯基名指针：仓内存在同名文件即算目标存在（D6 只问存在性）。
        if basename_index.get(rel, 0) >= 1:
            return "basename-hit"
        return None
    # 带斜杠且全部候选落空＝照实报悬空。**不设"外部路径豁免"规则**，两条理由：
    #   ① "是不是外部路径"只能靠语义猜，脚本无权自造这种判断（60-gates.md §〇 铁律 1）；
    #   ② 更要紧的是它会**吞掉真报**——`docs/INDEX.md` 这类指针的父目录已被删除，
    #      按"首段不存在＝外部"就放过了，而"目标所在的目录没了"恰恰是悬空的典型形态。
    # 上游仓路径（如 `to-tickets/references/…`）因此会被报出来，这是已知噪声；
    # 路由表把 `OA-D6` 配成 advisory（不拦提交）正是为这类噪声留的出口，
    # 处置它要在表里改，不在脚本里改。
    return None


def is_junction(path: str) -> bool:
    """目录联接判定。Python ≥3.12 有 os.path.isjunction；3.12 以下 fallback：
    realpath 与 abspath 不等即视为联接（实测对 junction 成立，见设计 v2 §2.6）。
    """
    if hasattr(os.path, "isjunction"):
        try:
            return bool(os.path.isjunction(path))
        except OSError:
            return False
    try:  # fallback（3.12 以下）
        return os.path.realpath(path) != os.path.abspath(path)
    except OSError:
        return False


def iter_markdown(root: str, scopes: "list[str]") -> "list[str]":
    out: "list[str]" = []
    for scope in scopes:
        base = os.path.join(root, scope)
        if not os.path.isdir(base):
            continue
        for cur, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
            for name in files:
                if name.endswith(".md"):
                    out.append(os.path.join(cur, name))
    return sorted(out)


def check_dangling(root: str, md_files: "list[str]", basename_index: "dict[str, int]",
                   relpaths: "list[str]") -> "tuple[list[str], list[str]]":
    """OA-D6：反引号路径／file:line 引用目标必须存在。

    指针 vs 提及（裁-21·判据见 50-document.md「D6 引用完整性」划界条款）：
      带目录的完整路径＝**指针**，解析不到即悬空，BLOCK；
      裸基名＝**提及嫌疑**（歧义天然高：泛指产物名／被论证的通用文件名），降 WATCH 不 BLOCK；
      行内注明「外部仓」的引用＝外部提及，不入悬空判定（条款要求注明，注明即机械可判；
      未注明者照报——注明的责任在作者，不在脚本猜）。
    主观部分（论证语气）不留脚本，留人判（条款原文）。

    返回 (findings, notes)：notes＝FX-U28 归位注记行，走 stdout 但不进 findings
    （不污染 exit 码；NOTE-FXU28 不含 BLOCK／WATCH 词，run-gates FINDING_RE 不匹配＝天然不参与路由计数）。

    FX-U28 后缀唯一命中解析层（插入位＝resolve 七候选层全部落空之后、悬空 BLOCK／WATCH 判定之前）：
      触发形态＝含斜杠相对 token（file:line 先剥行号＝strip_pointer_form 与七候选层同口径）；
      纯基名 token 不入本层（既有基名存在性层口径一字不动）。
      归位判据＝对 token 做「仓根相对路径以／＋token 结尾」的后缀匹配计数：
        命中恰 1＝归位放行（不再报 BLOCK，输出 NOTE 注记行）；
        命中 0＝维持既有 BLOCK（真悬空不变）；
        命中 ≥2＝维持既有 BLOCK 且文案不变（多义不猜＝fail-closed；多义详情不入文案＝防文案漂移破坏既有对拍）。
    """
    findings: "list[str]" = []
    notes: "list[str]" = []
    # 后缀匹配加速桶：基名 → 仓根相对路径列表（后缀命中必先同基名，桶外零漏）。
    by_base: "dict[str, list[str]]" = {}
    for rp in relpaths:
        by_base.setdefault(rp.rsplit("/", 1)[-1], []).append(rp)
    for md in md_files:
        rel_md = os.path.relpath(md, root).replace(os.sep, "/")
        try:
            with open(md, "r", encoding="utf-8", newline="") as handle:
                # CRLF 归一：本仓 core.autocrlf=true，检出件本身是 CRLF，
                # 不归一则反引号捕获会带着 `\r`，指针判定与打印都失真。
                lines = handle.read().replace("\r\n", "\n").split("\n")
        except (OSError, UnicodeDecodeError) as exc:
            sys.stderr.write("infra error: 读取失败 %s: %s\n" % (rel_md, exc))
            raise SystemExit(4)
        for lineno, raw in enumerate(lines, 1):
            if raw.lstrip().startswith("<!--"):
                continue  # 注释块内的示例路径不作指针判定
            for token in BACKTICK_RE.findall(raw):
                if not looks_like_path(token):
                    continue
                tok = token.strip()
                if EXTERNAL_MARK in raw:
                    continue  # 已注明外部仓＝外部提及（D6 裁-21 划界）
                if resolve(token, root, md, basename_index) is not None:
                    continue
                if "/" in tok:
                    # FX-U28 后缀唯一命中归位判定（七候选层已全落空至此）：
                    # 后缀匹配＝「仓根相对路径以／＋剥离后 token 结尾」计数（file:line 已先剥行号）。
                    rel = strip_pointer_form(token)
                    needle = "/" + rel
                    hits = [rp for rp in by_base.get(rel.rsplit("/", 1)[-1], ())
                            if rp.endswith(needle)]
                    if len(hits) == 1:
                        # 命中恰 1＝归位放行：不进 findings（exit 码不受影响），出注记行。
                        notes.append(
                            "%s:%d: NOTE-FXU28 短式指针唯一归位 `%s` → %s"
                            % (rel_md, lineno, tok, hits[0])
                        )
                        continue
                    # 命中 0（真悬空）／命中 ≥2（多义不猜＝fail-closed）＝维持既有 BLOCK，文案不变。
                    findings.append(
                        "%s:%d: %s OA-D6 指针悬空 `%s` → 目标不存在" % (rel_md, lineno, SEV_BLOCK, tok)
                    )
                else:
                    findings.append(
                        "%s:%d: %s OA-D6 提及嫌疑 `%s` → 仓内无同名件（裸基名不 BLOCK，D6 裁-21 划界）"
                        % (rel_md, lineno, SEV_WATCH, tok)
                    )
    return findings, notes


def check_orphans(root: str) -> "list[str]":
    """OA-D8-4／OB-DIR-③：包内 references/ 的每个文件须被该包 SKILL.md 指到，否则＝孤儿。"""
    findings: "list[str]" = []
    # 三分类目录（SWB-B2 换代）：三域枚举
    cat_bases = [os.path.join(root, c) for c in ("agent-experts", "agent-skills", "softwares")]
    if not any(os.path.isdir(b) for b in cat_bases):
        sys.stderr.write("infra error: 找不到三分类目录，索引对账无扫描域\n")
        raise SystemExit(4)
    pkg_bases = [b for b in cat_bases if os.path.isdir(b)]
    seen_pkgs: "set[str]" = set()
    for base in pkg_bases:
      if not os.path.isdir(base):
        continue
      for pkg in sorted(os.listdir(base)):
        if pkg in seen_pkgs:
            continue
        seen_pkgs.add(pkg)
        skill_md = os.path.join(base, pkg, "SKILL.md")
        refs_dir = os.path.join(base, pkg, "references")
        if not os.path.isfile(skill_md) or not os.path.isdir(refs_dir):
            continue
        try:
            with open(skill_md, "r", encoding="utf-8", newline="") as handle:
                index_text = handle.read()
        except (OSError, UnicodeDecodeError) as exc:
            sys.stderr.write("infra error: 读取失败 %s: %s\n" % (skill_md, exc))
            raise SystemExit(4)
        for name in sorted(os.listdir(refs_dir)):
            full = os.path.join(refs_dir, name)
            if not os.path.isfile(full) or is_junction(full):
                continue
            if name not in index_text:
                findings.append(
                    "%s:1: %s OA-D8-4 孤儿：`references/%s` 未被本包 SKILL.md 指到（索引无它）"
                    % (os.path.relpath(skill_md, root).replace(os.sep, "/"), SEV_WATCH, name)
                )
    return findings


def main(argv: "list[str]") -> int:
    parser = argparse.ArgumentParser(add_help=True, description="S-02 指针完整性与索引对账")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）；指向仓内子目录（如 .collab）时，"
                                       "该目录成为扫描域、仓根自动上溯做解析锚（裁-23 拍板 2 显式入口）")
    parser.add_argument(
        "--scope",
        action="append",
        default=None,
        help="扫描子目录（相对 --root，可重复）；默认三分类目录（.collab 已按裁-23 拍板 2 排除，"
             "需要时显式 --scope .collab 加回）",
    )
    parser.add_argument(
        "--target",
        action="append",
        default=None,
        help="只核查指定 .md 文件（可重复；裁-23 拍板 2 显式入口）。"
             "只做悬空/提及判定，不做索引对账（孤儿是包级判据，与单文件无关）",
    )
    args = parser.parse_args(argv)
    root = find_root(args.root)

    # 裁-23 拍板 2 显式入口：--root 指到非仓根（如 .collab）时，指针解析、基名索引、
    # 孤儿对账都必须以**仓根**为锚（否则相对指针全判悬空＝假报），故自动上溯定位仓根；
    # 原 --root 目录则退化为默认扫描域——"默认排除≠不能查"。
    scan_base = None
    if not any(os.path.isdir(os.path.join(root, c))
               for c in ("agent-experts", "agent-skills", "softwares")):
        anchor = os.path.dirname(root)
        while True:
            if os.path.isdir(os.path.join(anchor, "tools")) and any(
                    os.path.isdir(os.path.join(anchor, c))
                    for c in ("agent-experts", "agent-skills", "softwares")):
                break
            parent = os.path.dirname(anchor)
            if parent == anchor:
                die_usage("--root 不在本仓工作区内，无法定位解析锚仓根：%s" % args.root)
            anchor = parent
        scan_base = root
        root = anchor

    basename_index, relpaths = build_indexes(root)
    if args.target:
        md_files = []
        for tgt in args.target:
            full = os.path.abspath(tgt)
            if os.path.isdir(full):
                die_usage("--target 只收文件，目录请用 --scope：%s" % tgt)
            if not os.path.isfile(full):
                die_usage("--target 文件不存在：%s" % tgt)
            md_files.append(full)
        findings, notes = check_dangling(root, sorted(md_files), basename_index, relpaths)
    else:
        if args.scope:
            scopes = list(args.scope)
        elif scan_base:
            scopes = [os.path.relpath(scan_base, root).replace(os.sep, "/")]
        else:
            scopes = list(DEFAULT_SCOPE)
        md_files = iter_markdown(root, scopes)
        if not md_files:
            sys.stderr.write("infra error: 扫描域内没有任何 .md（scope=%s）\n" % ",".join(scopes))
            return 4
        findings, notes = check_dangling(root, md_files, basename_index, relpaths)
        findings = findings + check_orphans(root)

    for line in findings:
        print(line)
    # FX-U28 注记行：单独 print 在 findings 之后——不进 findings 列表＝不污染 exit 码；
    # 注记行不带 BLOCK／WATCH 词＝run-gates FINDING_RE 不匹配，天然不参与路由计数。
    for line in notes:
        print(line)
    return 1 if findings else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按 4，不得吞成 0
        sys.stderr.write("infra error: %s\n" % exc)
        raise SystemExit(4)
