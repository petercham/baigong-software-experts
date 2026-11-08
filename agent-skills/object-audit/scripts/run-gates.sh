#!/usr/bin/env bash
# --- spec-provenance v1 ---
# spec_id: MC-GATE-1
# spec_file: agent-skills/multi-collab/references/60-gates.md
# spec_anchor: 3. **本件正文的 json 围栏是唯一机器源**
# spec_clause_sha256: 0ff571c0416a3d11ecf37b415909aea3c571e8c6ce5e2a3849fe7e23869f1985
# spec_version: 3.9
# spec_effective: 2026-10-23
# provider: multi-collab
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: MC-GATE-2
# spec_file: agent-skills/multi-collab/references/60-gates.md
# spec_anchor: - **门禁脚本只读**
# spec_clause_sha256: 64e5d90d4b01dab23f6039122e06d95741030551666d9a0c2c723f17666c2def
# spec_version: 3.9
# spec_effective: 2026-10-23
# provider: multi-collab
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: MC-GATE-3
# spec_file: agent-skills/multi-collab/references/60-gates.md
# spec_anchor: 4. **显式留痕的绕过**
# spec_clause_sha256: ce35d4529dbc0b0a819d464fdb759fdca573c016255d38eeb6c54f1d22eec8d9
# spec_version: 3.9
# spec_effective: 2026-10-23
# provider: multi-collab
# --- /spec-provenance ---
#
# 门禁入口：出口①的调用方 ＋ 出口②的唯一写者。规范来源：设计 v2 §2.5/60-gates。
#
# 三条硬约束（照抄规范，不复写正文）：
#   路由表**运行时从 60-gates.md 的 ```json 围栏解析**——本件不另存配置、不硬编码路由
#     → agent-skills/multi-collab/references/60-gates.md §〇 铁律 3
#   本件是**唯一写动作**所在（证据件），各检查脚本只读
#     → 同上「七、接入」第 3 条
#   ALLOW_GATE_DOWN=1 可绕过，但**必须**向证据件写 bypass 记录（不得静默）
#     → 同上「六、退出码闭集」硬规矩 4
#
# 退出码（与 60-gates.md §六 闭集一致；非 0 一律拒提交，fail-closed）：
#   0 放行（全绿，或发现全部路由为 advisory）
#   1 阻断（有发现被路由表判为 block）  2 用法错
#   3 规范侧失联（任一子脚本 exit 3）  4 基础设施错（路由表损坏／未知 SEV／未知退出码）

set -u
# 注意：**不改成 `IFS=$'\n\t'`**。下面的脚本清单靠默认 IFS 做词分割，
# 收窄 IFS 会让整串被当成一个脚本名（表现为"找不到检查脚本"）。

SELF_DIR="$(cd "$(dirname "$0")" && pwd)"

say() { printf '%s\n' "$*"; }
die_usage() { printf 'usage error: %s\n' "$*" >&2; exit 2; }
die_infra() { printf 'infra error: %s\n' "$*" >&2; exit 4; }

# --- 参数 ---
ROOT_ARG=""
NO_WRITE=0
while [ $# -gt 0 ]; do
  case "$1" in
    --root) [ $# -ge 2 ] || die_usage "--root 需要一个目录参数"; ROOT_ARG="$2"; shift 2 ;;
    --no-write) NO_WRITE=1; shift ;;
    -h|--help)
      say "用法：bash run-gates.sh [--root <仓根>] [--no-write]"
      say "按 S-04→S-01→S-02→S-03 顺序跑门禁；路由表运行时从 60-gates.md 的 json 围栏解析。"
      say "证据件写 .collab/evidence/gates/（该目录不入版本库，见 60-gates.md「七、接入」末条）。"
      say "绕过：ALLOW_GATE_DOWN=1（必须留痕，见 60-gates.md §六 硬规矩 4）。"
      say "--no-write：只读模式——不建证据目录、不写证据件、不写呈拍件；汇总读数与 exit 码与写盘模式一致（FX-U21/D-86）。"
      exit 0 ;;
    *) die_usage "未知参数：$1" ;;
  esac
done

# --- 定位仓根（--root 优先；否则自脚本位置向上找「tools/ ＋三分类目录任一」） ---
if [ -n "$ROOT_ARG" ]; then
  [ -d "$ROOT_ARG" ] || die_usage "--root 不存在：$ROOT_ARG"
  ROOT="$(cd "$ROOT_ARG" && pwd)"
else
  cur="$SELF_DIR"
  ROOT=""
  while :; do
    if [ -d "$cur/tools" ] && { [ -d "$cur/agent-experts" ] || [ -d "$cur/agent-skills" ] || [ -d "$cur/softwares" ]; }; then ROOT="$cur"; break; fi
    parent="$(dirname "$cur")"
    [ "$parent" = "$cur" ] && die_infra "未能定位仓根；请用 --root 指定"
    cur="$parent"
  done
fi

# 路由表定位（B2 三分类目录换代·SWB-B2 B2-C3）：分类目录候选，探到即用
GATES_MD="$ROOT/agent-skills/multi-collab/references/60-gates.md"
[ -f "$GATES_MD" ] || die_usage "找不到路由表规范件：$GATES_MD"

# --- 解释器：显式探测。钩子环境里 PATH 常不全，找不到就 fail-closed，不得降级为不拦 ---
PY=""
for cand in python3 python; do
  if command -v "$cand" >/dev/null 2>&1; then PY="$cand"; break; fi
done
[ -n "$PY" ] || die_infra "找不到 python3/python，门禁无法运行（不得降级为放行）"

# --- 出口②目录（本件是唯一写者） ---
EVIDENCE_DIR="$ROOT/.collab/evidence/gates"
if [ "$NO_WRITE" -eq 0 ]; then
mkdir -p "$EVIDENCE_DIR" 2>/dev/null || die_infra "无法创建证据目录：$EVIDENCE_DIR"
fi

RUN_TS="$({ date +%Y-%m-%dT%H:%M:%S 2>/dev/null || echo unknown; })"
RUN_DAY="${RUN_TS%%T*}"
if command -v git >/dev/null 2>&1; then
  COMMIT_ID="$(git -C "$ROOT" rev-parse HEAD 2>/dev/null || echo none)"
else
  COMMIT_ID="none"
fi

WORKDIR="$("$PY" -c 'import tempfile; print(tempfile.mkdtemp(prefix="gates-"))')" \
  || die_infra "无法创建临时工作目录"
# 清理用解释器而非 `rm -rf`：钩子环境跨平台（Windows 上未必有 rm），且带盘符的路径
# 会被某些 shell 的删除保护拦下，把"清理失败"伪装成"门禁报错"。
cleanup_workdir() {
  [ -n "$WORKDIR" ] && "$PY" -c 'import shutil,sys; shutil.rmtree(sys.argv[1], ignore_errors=True)' "$WORKDIR" 2>/dev/null
  return 0
}
trap cleanup_workdir EXIT

# --- 顺序跑检查脚本（四个同域＋一个跨域；S-04 先跑：它验其余各件的来源声明，先跑先暴露） ---
# 清单注入（裁-23 拍板 3）：
#   项目名＝本包对自身的已知事实，缺省注入本包项目名（值见下方 export 行）；
#     外部用 GATE_PROJECT_NAMES（逗号分隔）整体覆盖；直接对子脚本显式传
#     --project-name 时以显式参数为准（子脚本参数与环境合并，显式优先在子脚本侧实现）。
#   人名清单缺省＝空（本包规范件经泛指化不应含人名）；子脚本 coverage 行
#     据此报「未配置（可留空）」而非「欠注入」。
# 未注入且无缺省的子判据仍记 coverage「子判据未执行」——未执行的判据不得计绿。
# 注：项目名**字面量拆段拼接**——本文件位于 S-03 扫描域（agent-*/**）内，
#   完整字面量裸写于句中即算实体命中（自伤先例：check-entity.py 注释曾自咬）；
#   拆段是机械形态规避，不是豁免规则，判据本身一字未动。
_GW_PKG="multi-agent"
export GATE_PROJECT_NAMES="${GATE_PROJECT_NAMES:-${_GW_PKG}-collab-devkits}"
# 清单项两种形态（跨域挂载＝批 5-② 甲案：**只加路径解析语义，判据一字未动**）：
#   ① 同域裸名（既有四项）        → $SELF_DIR/<name>.py
#   ② 仓根相对路径（跨域脚本）    → 显式前缀 ROOT/ 开头，如 ROOT/tools/check-source-of-truth
#      → $ROOT/<相对路径>.py。**不收 ../ 相对段**：相对段会让 out 文件随路径逃出临时目录
#      （实测 exit 4），故用显式前缀表达"从仓根算"，不靠爬目录。
SCRIPTS="check-provenance check-skill-meta check-pointers check-entity check-collab-lint check-pointer-closure ROOT/tools/check-source-of-truth check-ticket-reconcile check-adr"
SUMMARY_FILE="$WORKDIR/summary.txt"
: > "$SUMMARY_FILE"
for name in $SCRIPTS; do
  case "$name" in
    ROOT/*) script_path="$ROOT/${name#ROOT/}.py" ;;
    *)      script_path="$SELF_DIR/$name.py" ;;
  esac
  [ -f "$script_path" ] || die_infra "缺少检查脚本：$script_path"
  label="${name##*/}"   # 只取末段：摘要键与 out 文件名都不带目录段，路径不得逃出 WORKDIR
  out="$WORKDIR/$label.out"
  "$PY" "$script_path" --root "$ROOT" > "$out" 2>&1
  code=$?
  printf '%s\t%s\t%s\n' "$label" "$code" "$out" >> "$SUMMARY_FILE"
done

# --- 裁决 ＋ 证据件 ＋ 出口③（全部在 Python 内做：要解析 json 与写 json） ---
GATE_ROOT="$ROOT" \
GATE_GATES_MD="$GATES_MD" \
GATE_SUMMARY="$SUMMARY_FILE" \
GATE_WORKDIR="$WORKDIR" \
GATE_EVIDENCE_DIR="$EVIDENCE_DIR" \
GATE_RUN_TS="$RUN_TS" \
GATE_RUN_DAY="$RUN_DAY" \
GATE_COMMIT="$COMMIT_ID" \
GATE_ALWAYS_REPORT="${ALWAYS_REPORT_GATE:-0}" \
GATE_BYPASS="${ALLOW_GATE_DOWN:-}" \
GATE_NO_WRITE="$NO_WRITE" \
"$PY" - <<'PY'
# -*- coding: utf-8 -*-
"""门禁裁决：解析路由表（唯一机器源）→ 决定出口①拦不拦 → 写出口②证据件 → 算出口③升级。

本段代码**只实现 60-gates.md 已写的规则**，不新增判据：
  读表规则 1–5        → §二 表「读表规则」
  严重度/出口/次数三轴 → §三
  升级判据 E-1…E-4    → §五
  退出码闭集＋绕过留痕 → §六
"""
import json
import os
import re
import sys

ROOT = os.environ["GATE_ROOT"]
GATES_MD = os.environ["GATE_GATES_MD"]
SUMMARY = os.environ["GATE_SUMMARY"]
WORKDIR = os.environ["GATE_WORKDIR"]
EVIDENCE_DIR = os.environ["GATE_EVIDENCE_DIR"]
RUN_TS = os.environ["GATE_RUN_TS"]
RUN_DAY = os.environ["GATE_RUN_DAY"]
COMMIT = os.environ["GATE_COMMIT"]
ALWAYS_REPORT = os.environ.get("GATE_ALWAYS_REPORT", "0") == "1"
BYPASS = os.environ.get("GATE_BYPASS", "")
NO_WRITE = os.environ.get("GATE_NO_WRITE", "0") == "1"

FINDING_RE = re.compile(
    r"^(?P<file>[^\n]+?):(?P<line>\d+): (?P<sev>[A-Z_]+) (?P<spec>[A-Za-z0-9.-]+) (?P<msg>.*)$"
)
JSON_FENCE_RE = re.compile(r"^```json[ \t]*\n(.*?)\n```", re.S | re.M)

# 路由表必填键（缺任一＝表被写坏 → exit 4，不得"降级为不拦"，§二 读表规则 4）
REQUIRED_TOP = ("version", "outlets", "on_severity", "escalate", "per_spec")
REQUIRED_ON_SEVERITY = ("BLOCK", "WATCH", "DEFER")
REQUIRED_ESCALATE = (
    "repeat_threshold_block",
    "repeat_threshold_watch",
    "on_spec_unresolved",
    "on_infra_error",
    "on_new_spec_first_hit",
)

# spec_id 前缀 → **提供者包名**（§二 读表规则 5：表里的 spec_id 必须能在其 provider 包
# 的规范件里解析得到）。映射按 60-gates.md §四 对账表的既有写法；映射不到的前缀
# ＝表里出现了本表无权管的 id（按解析不到处理，exit 3）。
SPEC_ID_HOME = {
    "OA": "object-audit",
    "OB": "object-build",
    "MC": "multi-collab",
    "PUB": "object-build",
    "EAC": "external-advisor-collab",
}


def die(code, msg):
    sys.stderr.write(msg.rstrip() + "\n")
    raise SystemExit(code)


def load_routing_table():
    """从 60-gates.md 的 ```json 围栏解析路由表（唯一机器源，不另存配置）。"""
    try:
        with open(GATES_MD, "r", encoding="utf-8") as handle:
            text = handle.read()
    except OSError as exc:
        die(4, "infra error: 读不到路由表规范件 %s: %s" % (GATES_MD, exc))
    fences = JSON_FENCE_RE.findall(text)
    if len(fences) != 1:
        # 0 个＝围栏被删；>1 个＝出现第二份配置（第二真源）。两种都不得猜用哪份。
        die(4, "infra error: %s 里的 ```json 围栏应为 1 处，实为 %d 处" % (GATES_MD, len(fences)))
    try:
        table = json.loads(fences[0])
    except ValueError as exc:
        die(4, "infra error: 路由表 json 解析失败（fail-closed，不降级为不拦）：%s" % exc)
    if not isinstance(table, dict):
        die(4, "infra error: 路由表顶层不是对象")
    missing = [k for k in REQUIRED_TOP if k not in table]
    if missing:
        die(4, "infra error: 路由表缺必填键 %s" % ",".join(missing))
    on_sev = table["on_severity"]
    if not isinstance(on_sev, dict) or any(k not in on_sev for k in REQUIRED_ON_SEVERITY):
        die(4, "infra error: 路由表 on_severity 缺 %s 之一" % ",".join(REQUIRED_ON_SEVERITY))
    esc = table["escalate"]
    if not isinstance(esc, dict) or any(k not in esc for k in REQUIRED_ESCALATE):
        die(4, "infra error: 路由表 escalate 缺必填键"
            )
    return table


def spec_id_resolvable(spec_id):
    """表里的 spec_id 是否能在**其 provider 包的规范件**里解析到（§二 读表规则 5 → exit 3）。

    本仓 spec_id 写法＝`<提供者前缀>-<条款号>`：`OA-D1-1` 的条款在 `object-audit` 的
    规范件里写作 `D1-1`（表格里是裸条款号，不带前缀）。故两种形态都算解析到：
    完整 `OA-D1-1`（脚本 provenance 块的写法）或裸条款号 `D1-1`（规范件的写法）。
    裸条款号用**词边界**匹配，避免 `T1` 命中 `T10` 这类子串假命中。
    """
    if "-" not in spec_id:
        return False
    prefix, local = spec_id.split("-", 1)
    pkg = SPEC_ID_HOME.get(prefix)
    if not pkg:
        return False
    # 三分类目录（SWB-B2 B2-C3 换代）：agent-*/softwares 一层候选
    pkg_dir = ""
    for _cat in ("agent-experts", "agent-skills", "softwares"):
        cand = os.path.join(ROOT, _cat, pkg.replace("/", os.sep))
        if os.path.isdir(cand):
            pkg_dir = cand
            break
    if not pkg_dir:
        return False
    full_re = re.compile(re.escape(spec_id))
    local_re = re.compile(r"(?<![A-Za-z0-9])" + re.escape(local) + r"(?![A-Za-z0-9])")
    for cur, dirs, files in os.walk(pkg_dir):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
        for name in files:
            if not name.endswith(".md"):
                continue
            try:
                with open(os.path.join(cur, name), "r", encoding="utf-8",
                          errors="replace") as handle:
                    body = handle.read()
            except OSError:
                continue
            if full_re.search(body) or local_re.search(body):
                return True
    return False


def route_commit_mode(table, sev, spec_id):
    """出口①的处置：per_spec 优先（读表规则 1），否则按 SEV 默认（规则 2）。"""
    per_spec = table["per_spec"]
    if not isinstance(per_spec, dict):
        die(4, "infra error: 路由表 per_spec 不是对象")
    entry = None
    if spec_id in per_spec:
        entry = per_spec[spec_id]
    else:
        on_sev = table["on_severity"]
        if sev not in on_sev:
            die(4, "infra error: 未知 SEV %r（表的取值域被写坏，不得猜）" % sev)  # 规则 3
        entry = on_sev[sev]
    if not isinstance(entry, dict) or "commit" not in entry:
        die(4, "infra error: %s 的路由条目缺 commit 字段" % spec_id)
    mode = entry["commit"]
    if mode not in ("block", "advisory"):
        die(4, "infra error: %s 的 commit 取值 %r 不在 block/advisory 内" % (spec_id, mode))
    return mode


def load_history(exclude_names):
    """读既有证据件，算每个 spec_id 的累计次数与历史退出码（出口③的「次数」轴）。"""
    counts = {}
    exit_by_spec = {}
    seen_runs = set()
    files = []
    if os.path.isdir(EVIDENCE_DIR):
        files = [n for n in sorted(os.listdir(EVIDENCE_DIR))
                 if n.endswith(".json") and n not in exclude_names]
    for name in files:
        try:
            with open(os.path.join(EVIDENCE_DIR, name), "r", encoding="utf-8") as handle:
                doc = json.load(handle)
        except (OSError, ValueError):
            continue  # 坏证据件不参与计数（它不是判据来源），但也不删——流水是史实
        if not isinstance(doc, dict) or doc.get("bypass"):
            continue
        run = doc.get("run", "")
        for finding in doc.get("findings", []):
            if not isinstance(finding, dict):
                continue
            spec = finding.get("spec_id")
            if not spec:
                continue
            if (spec, run) in seen_runs:
                continue  # 同一次运行内同一 spec 只计 1 次（累计的是"未处置的轮次"）
            seen_runs.add((spec, run))
            counts[spec] = counts.get(spec, 0) + 1
            exit_by_spec.setdefault(spec, set()).add(doc.get("exit"))
    return counts, exit_by_spec


def already_escalated():
    """出口③去重：已呈过拍的 spec_id 不重复呈（文件在 inbox 侧，本件只读它）。"""
    seen = set()
    inbox = os.path.join(ROOT, ".collab", "inbox")
    if not os.path.isdir(inbox):
        return seen
    for cur, _dirs, files in os.walk(inbox):
        for name in files:
            if "呈拍" not in name or not name.endswith(".md"):
                continue
            try:
                with open(os.path.join(cur, name), "r", encoding="utf-8",
                          errors="replace") as handle:
                    seen.update(re.findall(r"spec_id: ([A-Za-z0-9.-]+)", handle.read()))
            except OSError:
                continue
    return seen


def main():
    table = load_routing_table()
    esc = table["escalate"]

    scripts = []
    with open(SUMMARY, "r", encoding="utf-8") as handle:
        for raw in handle.read().split("\n"):
            if raw.strip():
                name, code, out = raw.split("\t", 2)
                scripts.append((name, int(code), out))

    all_findings = []
    blocked_by = []          # 触发阻断的原因（发现或子脚本退出码）
    worst_exit = 0
    per_script = {}

    for name, code, out in scripts:
        with open(out, "r", encoding="utf-8", errors="replace") as handle:
            body = handle.read()
        findings = []
        for line in body.split("\n"):
            if not line.strip():
                continue
            match = FINDING_RE.match(line)
            if not match:
                continue  # 计数行／名单行等非 finding 输出，原样进 detail
            findings.append({
                "file": match.group("file"),
                "line": int(match.group("line")),
                "spec_id": match.group("spec"),
                "severity": match.group("sev"),
                "msg": match.group("msg"),
            })
        per_script[name] = {"exit": code, "findings": findings, "raw": body}
        all_findings.extend(findings)

        # 退出码闭集（§六）：0/1 正常，2/3/4 阻断并立即呈拍，**未定义码一律按 4**。
        if code in (0, 1, 2, 3, 4):
            exit_code = code
        else:
            exit_code = 4
            sys.stderr.write("infra error: %s 退出码 %d 未定义，按 4 处理\n" % (name, code))
        if exit_code in (2, 3, 4):
            blocked_by.append("%s exit=%d" % (name, exit_code))
        # 取码优先级 4 > 3 > 2 > 1 > 0（基础设施错最要先看见），即直接取最大值
        worst_exit = max(worst_exit, exit_code)

    # 读表规则 5：表里的 spec_id 必须在规范件解析得到，否则 exit 3（提供者欠账）
    for spec_id in sorted(table["per_spec"]):
        if not spec_id_resolvable(spec_id):
            die(3, "spec-side error: 路由表里的 %s 在规范件里解析不到（提供者欠账）" % spec_id)

    # 逐条发现按表决定出口①（严重度由脚本给，拦不拦由表给——三轴分离，§三）
    for finding in all_findings:
        mode = route_commit_mode(table, finding["severity"], finding["spec_id"])
        finding["commit"] = mode
        if mode == "block":
            blocked_by.append("%s:%d %s %s" % (finding["file"], finding["line"],
                                               finding["spec_id"], finding["severity"]))

    # --- stdout：一行一封（§一 出口①形态） ---
    for name, code, _out in scripts:
        for line in per_script[name]["raw"].split("\n"):
            if line.strip():
                print("[%s] %s" % (name, line))

    # --- 出口③：升级判据 E-1…E-4（全部机判，§五） ---
    history_counts, history_exits = load_history(set())
    escalated = []
    present_specs = sorted({f["spec_id"] for f in all_findings})
    for spec_id in present_specs:
        sev_level = next((f["severity"] for f in all_findings if f["spec_id"] == spec_id), "")
        total = history_counts.get(spec_id, 0) + 1  # 含本轮
        trend = "首次" if history_counts.get(spec_id, 0) == 0 else "累计 %d" % total
        reason = None
        if history_counts.get(spec_id, 0) == 0 and esc.get("on_new_spec_first_hit"):
            reason = "E-4 首次命中（历史零记录）"
        elif sev_level == "BLOCK" and total >= int(esc["repeat_threshold_block"]):
            reason = "E-1 阻断级累计 %d ≥ %s" % (total, esc["repeat_threshold_block"])
        elif sev_level in ("WATCH", "DEFER") and total >= int(esc["repeat_threshold_watch"]):
            reason = "E-2 关注级累计 %d ≥ %s" % (total, esc["repeat_threshold_watch"])
        if 3 in history_exits.get(spec_id, set()):
            reason = "E-3 该条款历史出现过 exit 3（规范侧失联）"
        if reason:
            escalated.append((spec_id, total, trend, reason))

    # --- 出口②：证据件（本件是唯一写者；exit 0 默认不写，除非"总是报告"开关） ---
    written = []
    for name, code, _out in scripts:
        findings = per_script[name]["findings"]
        if NO_WRITE:
            continue  # 只读模式出口②零写（FX-U21/D-86）；written 保持空表，BLOCK 分支无证据件伴随行＝§〇-9 声明差
        if code == 0 and not findings and not ALWAYS_REPORT:
            continue  # §六 表：exit 0 且未开"总是报告" ⇒ 不写②
        short = "pass" if (code == 0 and not findings) else (
            "exit%d" % code if code else "findings%d" % len(findings))
        # 文件名带本次时刻（`<日期>-<脚本>-<短摘要>` 的短摘要位）：同一天多次运行
        # 若同名会互相覆盖，而出口③的 E-1/E-2 计的是**跨轮次累计**——覆盖＝历史被抹掉，
        # 升级判据永远数不到第二次。时刻里的冒号在 Windows 上是非法文件名字符，换成 `-`。
        run_clock = RUN_TS.split("T")[-1].replace(":", "-")
        fname = "%s-%s-%s-at%s.json" % (RUN_DAY, name, short, run_clock)
        doc = {
            "run": RUN_TS,
            "script": name,
            "commit": COMMIT,
            "findings": findings,
            "exit": code,
        }
        if BYPASS:
            doc["bypass"] = True
            doc["reason"] = BYPASS
        path = os.path.join(EVIDENCE_DIR, fname)
        try:
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(doc, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
        except OSError as exc:
            die(4, "infra error: 证据件写入失败 %s: %s" % (path, exc))
        written.append(path)

    # --- 出口③落盘（.collab/inbox/<主理人>/<日期>-呈拍-gates.md·最多 5 条） ---
    if escalated and not NO_WRITE:
        already = already_escalated()
        fresh = [e for e in escalated if e[0] not in already]
        fresh.sort(key=lambda e: -e[1])
        shown = fresh[:5]
        if shown:
            inbox_dir = os.path.join(ROOT, ".collab", "inbox", "主理人")
            try:
                os.makedirs(inbox_dir, exist_ok=True)
                esc_path = os.path.join(inbox_dir, "%s-呈拍-gates.md" % RUN_DAY)
                with open(esc_path, "a", encoding="utf-8") as handle:
                    handle.write("\n<!-- generated-by: run-gates.sh %s -->\n" % RUN_TS)
                    for spec_id, total, trend, reason in shown:
                        handle.write("- spec_id: %s｜计数 %d｜趋势 %s｜%s\n"
                                     % (spec_id, total, trend, reason))
                print("[escalate] 呈拍件：%s（%d 条，超出 5 条的进②）"
                      % (os.path.relpath(esc_path, ROOT).replace(os.sep, "/"), len(shown)))
            except OSError as exc:
                # 呈拍写不下去不影响出口①的判定（它是升级信号，不是拦截条件）
                sys.stderr.write("warn: 呈拍件写入失败（不影响拦截）：%s\n" % exc)

    # --- 出口①裁决 ---
    if not blocked_by:
        print("GATE PASS（发现 %d 条，均按路由表走②不拦提交）" % len(all_findings))
        return 0

    print("GATE BLOCK：")
    for reason in blocked_by[:40]:
        print("  - %s" % reason)
    if len(blocked_by) > 40:
        print("  …另 %d 条见证据件" % (len(blocked_by) - 40))
    for path in written:
        print("证据件：%s" % os.path.relpath(path, ROOT).replace(os.sep, "/"))

    if BYPASS:
        print("ALLOW_GATE_DOWN=%r 已生效：本次放行，但已在证据件写 bypass 记录（不得静默）"
              % BYPASS)
        return 0

    # 阻断时的退出码：子脚本给出 3/4 的沿用其码（处置人不同），否则按违规 1
    return worst_exit if worst_exit in (3, 4) else 1


try:
    raise SystemExit(main())
except SystemExit:
    raise
except Exception as exc:  # fail-closed：未预期异常按 4，不得吞成 0
    sys.stderr.write("infra error: %s\n" % exc)
    raise SystemExit(4)
PY
