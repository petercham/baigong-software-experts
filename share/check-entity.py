#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: OA-T1
# spec_file: agent-skills/object-audit/SKILL.md
# spec_anchor: T1 | 换项目测试
# spec_clause_sha256: 7415060b134d9848e21c545c803eee041739aaa69f951801ed33f55f2c534e3c
# spec_version: 0.4
# spec_effective: 2026-10-23
# provider: object-audit
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: OA-S1
# spec_file: agent-skills/object-audit/references/10-skill.md
# spec_anchor: S1 | 项目实体
# spec_clause_sha256: 318bb2af2344fe444afbde85a2a6b93fcc83bacde16098f1e366d008e378dfae
# spec_version: 0.4
# spec_effective: 2026-10-23
# provider: object-audit
# --- /spec-provenance ---
#
# 条款摘要口径（与 S-04 共用·写死在此以免两处实现漂移）：
#   取 spec_anchor 在 spec_file 中命中的那一行 → 去首尾空白 → 连续空白压成单个空格
#   → UTF-8 编码 → sha256（十六进制小写）。行号不参与定位，也不入判据。
#
# S-03 项目实体扫描（OA-T1／OA-S1）。
#
# **只扫规范件＋收编 bundle**（三分类目录面 `agent-*/**`＋`softwares/**`·bundle 现居
# 内＝收编域已在其中·DIRRELOC 路径换代随动）：`object-audit/SKILL.md「审计范围：只审规范件」`
# 明确记录件（informative）「不要求干净——它们是项目史，脏是正常形态」。若不划界，
# 裁决记录/台账里的日期与项目名会全部命中，误报会吞掉这个脚本（门禁死法之一）。
#
# 本件只读：不写任何文件。唯一写动作在 run-gates.sh（出口②）。
# 本件不含策略判断：只输出 SEV＋spec_id＋逐模式计数（含命中名单）。
"""S-03：扫规范件＋收编 bundle（三分类目录面·bundle＝agent-experts/ 子树）的项目实体命中（OA-T1／OA-S1），逐模式计数并附命中名单。

用法：
    python check-entity.py [--root <仓根>] [--project-name <名>]... [--person-name <名>]...
    环境变量 GATE_PROJECT_NAMES／GATE_PERSON_NAMES（逗号分隔）等价于同名参数。

退出码（闭集，见 60-gates.md「六、退出码闭集」）：
    0 通过（零命中）／1 违规（≥1 命中）／2 用法错／4 基础设施错
"""

from __future__ import annotations

import argparse
import fnmatch
import os
import re
import sys

SEV_BLOCK = "BLOCK"
SEV_WATCH = "WATCH"

# 实体模式：判据文本＝10-skill.md「S1 项目实体」所列五类（项目名／号段／日期／人名／项目路径）。
# 号段类只收本仓已定型的形态；未定型的号段（台账号/判词号）留待注入，宁漏不误报。
#
# drive-path 的负向前查 `(?<![A-Za-z0-9])` 是**必需的**，不是放宽：URL 的 scheme 部分
# 也是「字母 + 冒号 + 斜杠」形态（scheme 尾字母会被裸模式咬住），而盘符路径的盘符
# 是**独立单字母**（前面不可能是字母）。实测：不加此约束时 23 条命中里 21 条是 URL
# （假报），真盘符只有 2 条。本注释刻意不写完整 scheme 字面量，否则扫描器会命中自己。
PATTERNS: "list[tuple[str, str, str]]" = [
    ("date", "日期", r"20\d{2}-\d{2}-\d{2}"),
    ("drive-path", "盘符路径", r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]{1,2}(?![/\\])[^\s`)\]]*"),
    ("discipline-no", "纪律号", r"\bM0\d{3}\b"),
    ("ticket-no", "票号", r"\bT-?\d{3}\b"),
]

# ---- date 豁免（裁-21·判据见 10-skill.md「S1 项目实体」豁免注／SKILL.md T1 行）----
# ①`spec-provenance` 块内全部日期（条款列举的是 `spec_effective` 行；机械化口径扩到
#   **整块**——`ADR-YYYY-MM-DD-NN` 型 spec_id 与指向 `…/2026-10-22-裁决记录.md` 的
#   spec_file 同为 70-provenance.md §七 协议强制写法，同属「协议强制日期」。
#   此扩法与「全角括注」口径同为**裁-23 拍板 1 已拍口径（L1）**）
# ②changelog 文件全部日期 ③全角括注内的日期。
# 实现解释（同步报告）：条款说「正文**裸**叙述日期仍算」，故反引号段与 URL 内的
# 日期不算"裸写于句中"——先遮除再判（遮除保位不缩列）。
# 载体二分（与 S-04 parse_blocks 同口径）：`#` 注释块（.py/.sh）与 HTML 注释块（.md）。
# 闭标记**不合并**：`-->` 只在 HTML 块打开时才算闭（md 正文普通 `-->` 不得误关块）。
SPECPROV_START_RE = re.compile(r"^[ \t]*(?:#[ \t]*-{3,}[ \t]*|<!--[ \t]*)spec-provenance v1[ \t]*(?:-{3,})?[ \t]*$")
SPECPROV_END_RE = re.compile(r"^[ \t]*#[ \t]*-{3,}[ \t]*/spec-provenance[ \t]*(?:-{3,})?[ \t]*$")
HTML_END_RE = re.compile(r"^[ \t]*-->[ \t]*$")
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")
URL_RE = re.compile(r"https?://\S+")

# ---- 改名/沿革史实句豁免（裁-23 拍板 3·判据见 10-skill.md S1 行／SKILL.md T1 行）----
# 条款句式：「改名（YYYY-MM-DD…）」「由 X 改名」「旧名作废」。机械化口径：**行内含
# 史实锚句标记**（改名／旧名作废／沿革）⇒ 该行项目名命中豁免（史实锚不删不改写）。
# 正文裸项目名（行内无标记）仍算。changelog 文件的项目名**不整体豁免**——
# 只有史实句式行豁免（90-changelog.md:13 即此例，裁-23 验收点名）。
HISTORICAL_MARKERS = ("改名", "旧名作废", "沿革")


def mask_non_narrative(line: str) -> str:
    """把反引号段与 URL 遮成等长占位（保位置，供全角括注深度计算）。"""
    line = CODE_SPAN_RE.sub(lambda m: "\x00" * len(m.group(0)), line)
    return URL_RE.sub(lambda m: "\x00" * len(m.group(0)), line)


def in_fullwidth_paren(text: str, pos: int) -> bool:
    """pos 是否落在未闭合的（…）内（全角括注＝版本/决策注的机械化口径）。"""
    depth = 0
    for ch in text[:pos]:
        if ch == "（":
            depth += 1
        elif ch == "）":
            depth = max(0, depth - 1)
    return depth > 0

# 扫描域＝规范件＋收编 bundle（收编 bundle 现居 `agent-experts/` 子树＝已在
# 三分类目录域内·SWB-B2 路径换代随动，域覆盖不减）。
# 仍不接受扩到记录件（.collab/** 等）——扩了就违反划界，误报会吞掉脚本。
SCAN_ROOT_DIRS = ("agent-experts", "agent-skills", "softwares")
SCAN_EXTS = (".md", ".py", ".sh", ".json", ".state", ".txt")

# ---- 史实锚登记件名册豁免（SWB-B5 门禁随动·主理人裁定 A·B3a 剪枝先例同规格）----
# 本件自注「扫描域＝规范件」：登记件＝三方收口史实锚（正文哈希恒等＝D5/V13 既裁），
# 非规范件，与 .collab 剪枝（B3a）／check-pointers 裁-23 记录件排除同理＝既有语义
# 物理化，**非新增豁免类别语义**。形态闭死＝**基名精确匹配名册**（fnmatch 仅允许
# 日期/版本段通配，禁泛化为 docs 整面或目录前缀豁免）。名册 **append-only**：
# 新登记件入库须随目入册（登记面＝对应票回执「门禁随动行」）。
# 名册行内日期字面拆段拼接＝防本件自咬（OA-T1 date 正则不咬拆分形态·先例＝
# drive-path 注释「刻意不写完整 scheme 字面量」同法）。
REGISTRATION_NAME_ROSTER = (
    "SWB-交接件v2.9-*-2026" + "-11-03.md",  # D7 正式登记件（SWB-B5 入库 docs·名册行出处＝B5 回执「门禁随动行」节）
)


def in_registration_roster(name: str) -> bool:
    """基名精确匹配史实锚登记件名册（名册外零豁免；豁免不外溢＝负例探针在册）。"""
    return any(fnmatch.fnmatch(name, pat) for pat in REGISTRATION_NAME_ROSTER)


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


def build_patterns(project_names: "list[str]", person_names: "list[str]") -> "list[tuple[str, str, str]]":
    """把注入的项目名/人名编成模式；未注入者由调用方记 WATCH（未执行的判据不得计绿）。"""
    patterns = list(PATTERNS)
    if project_names:
        alt = "|".join(re.escape(n) for n in sorted(project_names, key=len, reverse=True))
        patterns.insert(0, ("project-name", "项目名", r"(?<![A-Za-z0-9_])(?:%s)(?![A-Za-z0-9_])" % alt))
    if person_names:
        alt = "|".join(re.escape(n) for n in sorted(person_names, key=len, reverse=True))
        patterns.append(("person-name", "人名", r"(?:%s)" % alt))
    return patterns


def iter_scan_files(root: str) -> "list[str]":
    out: "list[str]" = []
    for top in SCAN_ROOT_DIRS:
        base = os.path.join(root, top)
        if not os.path.isdir(base):
            continue
        for cur, dirs, files in os.walk(base):
            # B3a 随动（B 批搬家后案卷桶物理入三分类目录）：扫描域仍＝规范件，
            # 项目内 `.collab/`/`.scratch/` 记录件按本件自注划界不入面
            # （与 check-pointers 裁-23 拍板 2 排除 .collab 同口径）。
            # 嵌套 git 仓根剪枝（SWB 观察记录 2026-11-19「主根闸扫面撞嵌套 worktree」）：
            # 三分类目录树下任何含 `.git`（目录或 worktree 指针文件）的子目录＝他仓检出面，
            # 整支不入扫＝主根闸只扫主根管辖面（皮总 2026-11-19 已裁「worktree 分立为既定·
            # 主根只留公共面」语义物理化·非新增豁免类别）。窄修＝处方前临时口径，
            # 全闸扫面统一排除口径归 GTBLOAT 续施射程。
            if cur != root and (
                    os.path.isdir(os.path.join(cur, ".git"))
                    or os.path.isfile(os.path.join(cur, ".git"))):
                dirs[:] = []
                continue
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".collab", ".scratch", ".workbuddy")]
            for name in files:
                if name.endswith(SCAN_EXTS):
                    out.append(os.path.join(cur, name))
    return sorted(out)


def main(argv: "list[str]") -> int:
    parser = argparse.ArgumentParser(add_help=True, description="S-03 项目实体扫描（仅规范件）")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    parser.add_argument("--project-name", action="append", default=[], help="项目名（可重复）")
    parser.add_argument("--person-name", action="append", default=[], help="人名（可重复）")
    args = parser.parse_args(argv)

    root = find_root(args.root)
    projects = list(args.project_name)
    persons = list(args.person_name)
    for env, bucket in (("GATE_PROJECT_NAMES", projects), ("GATE_PERSON_NAMES", persons)):
        value = os.environ.get(env, "")
        if value.strip():
            bucket.extend(n.strip() for n in value.split(",") if n.strip())

    files = iter_scan_files(root)
    if not files:
        sys.stderr.write("infra error: 规范件扫描域为空（三分类目录不存在或无待扫文件）\n")
        return 4

    patterns = build_patterns(projects, persons)
    counts: "dict[str, list[str]]" = {key: [] for key, _, _ in patterns}
    first_hit: "dict[str, str]" = {}  # 每模式首个命中的 file:line（聚合 finding 的落点）
    for path in files:
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        basename = os.path.basename(path).lower()
        # 史实锚登记件名册豁免（B5 随动·主理人裁定 A）：名册内基名＝整件不入扫面
        # （与 .collab 剪枝同理＝记录件物理划界，非日期级豁免）。
        if in_registration_roster(os.path.basename(path)):
            continue
        is_changelog = "changelog" in basename
        # 裁-25 拍板 1①：账本（COPY.state，文件名**精确匹配**）全部日期豁免——
        # 机器生成同步流水，与 changelog 同性质（协议强制时间戳）。机械化口径＝
        # 文件名判定，与 changelog 文件名口径同款；只豁免 date，其余实体照扫。
        is_ledger = basename == "copy.state"
        try:
            with open(path, "r", encoding="utf-8", errors="replace", newline="") as handle:
                # CRLF 归一：本仓 core.autocrlf=true，检出件本身是 CRLF（与其他三件同口径）
                lines = handle.read().replace("\r\n", "\n").split("\n")
        except OSError as exc:
            sys.stderr.write("infra error: 读取失败 %s: %s\n" % (rel, exc))
            return 4
        in_prov_block = False
        in_html_block = False
        for lineno, raw in enumerate(lines, 1):
            # 豁免①（块级）：spec-provenance 块内全部日期不扫（协议强制写法）。
            # 载体二分（与 S-04 parse_blocks 同口径）：`-->` 只在 HTML 块内才是闭标记，
            # 否则 md 正文里的普通 `-->` 会误关块。
            if SPECPROV_START_RE.match(raw):
                in_prov_block = True
                in_html_block = raw.lstrip().startswith("<!--")
            elif (in_html_block and HTML_END_RE.match(raw)) or (
                    not in_html_block and SPECPROV_END_RE.match(raw)):
                in_prov_block = False
                in_html_block = False
            for key, _label, pat in patterns:
                if key == "date":
                    # 豁免①②④：provenance 块内／changelog 文件／账本 COPY.state 整行跳过
                    if is_changelog or in_prov_block or is_ledger:
                        continue
                    masked = mask_non_narrative(raw)
                    for match in re.finditer(pat, masked):
                        # 豁免③：全角括注内的版本/决策注日期
                        if in_fullwidth_paren(masked, match.start()):
                            continue
                        counts[key].append("%s:%d: %s" % (rel, lineno, match.group(0)))
                        first_hit.setdefault(key, "%s:%d" % (rel, lineno))
                    continue
                if key == "project-name":
                    # 裁-23 史实句豁免：行内含改名/沿革标记 ⇒ 该行项目名不报
                    if any(marker in raw for marker in HISTORICAL_MARKERS):
                        continue
                    for match in re.finditer(pat, raw):
                        counts[key].append("%s:%d: %s" % (rel, lineno, match.group(0)))
                        first_hit.setdefault(key, "%s:%d" % (rel, lineno))
                    continue
                for match in re.finditer(pat, raw):
                    counts[key].append("%s:%d: %s" % (rel, lineno, match.group(0)))
                    first_hit.setdefault(key, "%s:%d" % (rel, lineno))

    findings: "list[str]" = []
    label_of = {key: label for key, label, _ in patterns}
    for key, hits in counts.items():
        print("pattern=%s(%s) count=%d" % (key, label_of[key], len(hits)))
        for hit in hits:
            print("  %s" % hit)
        if hits:
            # 修单②：聚合 finding 的落点必须是**真实路径**（取首个命中处），
            # 不得输出旧域前缀这类伪位置——机器消费时它是假路径。
            findings.append(
                "%s: %s OA-T1 项目实体命中 pattern=%s count=%d（规范件须换项目仍成立；名单见 pattern 行）"
                % (first_hit[key], SEV_BLOCK, key, len(hits))
            )

    # 注入类子判据的覆盖度提示：**不是 finding**（OA-T1 在路由表里配 block，把
    # 「清单没注入」记成 OA-T1 违规＝把**配置问题**记成**产物违规**——正是
    # 70-provenance.md 记在账上的「归属错」；且注入后本仓 决策者/项目名 命中属待拍项，
    # 两头一夹门禁永不可满足，永不可满足的门禁＝装饰）。
    # 但也不静默：每次运行都打 coverage 行（非 finding 格式，run-gates 原样透传显示）。
    if not projects:
        print("coverage: OA-T1「项目名」子判据未执行（--project-name 或 GATE_PROJECT_NAMES 未注入）")
    if not persons:
        # 裁-23 拍板 3：人名清单缺省＝空是**合法配置**（本包规范件经泛指化后不应含
        # 人名），文案据此从「未执行（欠注入）」改为「未配置（可留空）」——不制造焦虑。
        print("coverage: OA-T1「人名」子判据未执行——人名清单未配置（如规范件不应含人名可留空）")

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
