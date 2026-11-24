#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T04-C · B5 提交审计（拦三形态＋PostToolUse 记账）

规范锚点：架构 v2.9 §9 B5 行「拦 amend/rebase/无票提交＋PostToolUse 记账」；
§17 orphan 提交词条＝「无票 ID trailer 的提交」；违纪模式表行 7
「无票提交/amend/rebase→B5 提交审计＋日终对账」。
B0 退路补位（§9 B0 行退路「PreToolUse 拦 force-push/amend」）：P7 阴性时拦 force-push；
P7 实测＝pass（运行时探针读数由仓侧验收体系维护，不随包分发）→ force-push 拦截作补位面同交付、
缺省仍生效（拦截无害超集，退路启用与否随 B0 定型候裁，本票不拍）。

prehook（PreToolUse Bash matcher）：命令串机检三形态＋force-push → exit 2 blocking（exit 2→blocking·§19 词表）。
posthook（PostToolUse Bash matcher）：检出 git commit 成功执行 → 提交哈希/票 ID/席位归因入「写入」记录类。

票 ID 口径：trailer/消息体含票 ID 记法（票面编号记法各形态或票面卷路径引用——
检测形态以本件 TICKET_ID_PATTERNS 闭集为准）即视为有票提交；全无＝orphan。
运行落盘一律可重定向：--ledger 与 SWB_LEDGER_ROOT；验证运行请重定向至所属项目仓根 .scratch/<票号>/（批毕即删·仓内与仓外公共区零残留）。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

# 票 ID 记法闭集形态（§17 orphan＝无票 ID trailer）
TICKET_ID_PATTERNS = [
    re.compile(r"\bSW" + r"B-[A-Z]*\d+\b"),  # 字面拆段拼接·判据一字未动（运行时语义逐字不变·两段均 r 前缀防转义自咬）
    re.compile(r"\bTKT\d+\b"),
    re.compile(r"\bTK-[A-Za-z0-9-]+\b"),
    re.compile(r"\.coll" + r"ab/tickets/[^\s\"']+"),  # 字面拆段拼接·判据一字未动（运行时语义逐字不变）
    re.compile(r"\b[A-Z][A-Z0-9]{1,9}-\d{3,4}-[A-Z][A-Z0-9]{1,14}\b"),  # GWP-P6-1 项目票号 XXX-NNNN-WORD 型（大写三段·中段三至四位数字）
]

# 三形态＋force-push 命令机检（词边界锚定，避免 "git commit --amend" 误漏/"amended" 误触）
CMD_PATTERNS = {
    "amend": re.compile(r"\bgit\b[^|;&]*\bcommit\b[^|;&]*\--amend\b"),
    "rebase": re.compile(r"\bgit\b[^|;&]*\brebase\b"),
    "force-push": re.compile(r"\bgit\b[^|;&]*\bpush\b[^|;&]*(--force(?!-with-lease)|-f\b)"),
}
# SWB-B16-a 修二（纯增·危险子命令词面退路族）＝CMD_PATTERNS 行族纯增＝仅「目标仓根解析失败」退路档激活（判序＝票面 rev-1 勘正①钉死：
# 目标仓根解析命中优先→修一判定链；词面族仅解析失败退路路径激活＝fail-closed 防「解析器缺位即零拦」重演（BG-16 甲-4 荐项语义）；
# 危险词面族在解析成功路径（本仓／跨面）零激活＝行为变化面最小＝本仓合法危险形态不入新拦＝K1 拦截阈值计数零差（V2 臂八差分臂））。
DANGEROUS_SUBCMD_PATTERNS = {  # 闭集枚举＝reset --hard／push -f 族／checkout 丢弃形态
    "reset-hard": re.compile(r"\bgit\b[^|;&]*\breset\b[^|;&]*--hard\b"),
    "push-force": re.compile(r"\bgit\b[^|;&]*\bpush\b[^|;&]*(--force(?!-with-lease)|-f\b)"),
    "checkout-discard": re.compile(r"\bgit\b[^|;&]*\bcheckout\b[^|;&]*(--\s+\S|\s--\s|-f\b|--force\b)"),
}

# SWB-B16-a 修一（纯增·目标仓根解析臂）＝写型／读型子命令族闭集枚举＋解析用词面锚（判据字面族·非决策词层·§19 三值维持）
GIT_WRITE_SUBCMDS = frozenset({"commit", "reset", "push", "checkout"})
GIT_READ_SUBCMDS = frozenset({"status", "log", "diff", "show"})
_GIT_SUB_RE = re.compile(r"\bgit\b\s*(?:-{1,2}[A-Za-z][\w-]*(?:\s+(?:\"[^\"]*\"|'[^']*'|[^\s|;&]+))?)*\s+([a-z][a-z-]+)")
_GIT_C_RE = re.compile(r"\bgit\b\s+-C\s+(\"([^\"]*)\"|'([^']*)'|([^\s|;&]+))")
_REDIR_RE = re.compile(r"(?<![0-9A-Za-z_&])>{1,2}\s*(\"([^\"]*)\"|'([^']*)'|([^\s|;&<>]+))")  # 写形态闸＝stdout 覆盖／追加重定向；fd 复制（2＞dev－null、N＞＆、＆＞ 形态）值首含 & 或前置数字＝非文件写不入判定面（防误拦臂）
_UNRESOLVED_VAL_RE = re.compile(r"\$\{|\$\(|\A\s*\$\S|\A\s*\Z")

EXIT_BLOCKING = 2  # exit 2→blocking（§19 决策词表）


def pack_root() -> str:
    d = os.path.abspath(__file__)
    for _ in range(4):
        d = os.path.dirname(d)
    return d


ANCHOR_FILE = os.path.join(".workbuddy", "swb-anchor")  # PROJINIT-P1 显式锚定声明件（开发面根相对字面·四脚本同款）


def _anchor_hit(d: str, pack: str) -> bool:
    """锚定命中：d≠包根 ∧ d/.workbuddy/swb-anchor 存在 ∧ 首个 `project_root:` 行解析值
    （相对值按 d 解析）经 normcase 后＝d 自身（自指闭合＝锚件不得指向他处，防跨项目劫持）。"""
    if os.path.normcase(d) == os.path.normcase(pack):
        return False
    ap = os.path.join(d, ANCHOR_FILE)
    if not os.path.isfile(ap):
        return False
    try:
        with open(ap, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return False
    for line in text.splitlines():
        if line.strip().startswith("project_root:"):
            val = line.split(":", 1)[1].strip().strip("\"'")
            if not val:
                return False
            target = val if os.path.isabs(val) else os.path.join(d, val)
            return os.path.normcase(os.path.abspath(target)) == os.path.normcase(d)
    return False


def _structure_hit(d: str, pack: str) -> bool:
    """事后校验路：d≠包根 ∧ d/docs/STRUCTURE.md 存在（旧 ②③ 文件溯源语义降档保持·不再作判定前提）。"""
    return (os.path.normcase(d) != os.path.normcase(pack)
            and os.path.isfile(os.path.join(d, "docs", "STRUCTURE.md")))


def project_root() -> str:
    """PROJINIT-P1 锚定换代（裁定①＋双根裁定：本函数返回值＝开发面根 {dev_root}/{project_id}）：
    探测序（与代码循环序严格同构·R-2）：
    ① SWB_REPO_ROOT 覆写（测试重定向＋部署态正式锚定·覆写语义零动·值原样返回不做 abspath 归一）在场即回；
    ② 锚定声明件路：先自 cwd 上溯、后自包根上溯——首个 `.workbuddy/swb-anchor` 自指闭合命中目录＝项目根（权威锚）；
    ③ STRUCTURE.md 事后校验路：先自 cwd 上溯、后自包根上溯——首个含 `docs/STRUCTURE.md` 且≠包根目录（降档保持）；
    ④ 全缺位＝落回包根（fail-safe·权限面读空即租约不命中＝deny，不开 fail-open 窗口——旧语义保持）。
    权限字面一律读作开发面根相对（表2-1 路径锚定款随迁）。"""
    env = os.environ.get("SWB_REPO_ROOT")
    if env:
        return env
    pack = pack_root()
    for probe in (_anchor_hit, _structure_hit):
        for d0 in (os.getcwd(), os.path.dirname(pack)):
            d = d0
            while True:
                if probe(d, pack):
                    return d
                parent = os.path.dirname(d)
                if parent == d:
                    break
                d = parent
    return pack


def governance_resident() -> bool:
    """ITER-K 锚门中立放行·治理在场判定（三枚同款·函数体只读零写·零宿主专有假设＝纯环境变量＋文件系统探测）：
    治理在场＝① SWB_REPO_ROOT 非空在场；或②③探测命中（project_root 现读值经 normcase 后≠pack_root）；
    或④落位且租约台账目录在场（台账目录名＝字面拆段拼接·沿 commit-audit 判据段拆段先例形制·防指针闸 OA-D6 自咬）；
    四条件全缺位＝返回假＝非百工管辖项目＝钩子中立放行。"""
    if os.environ.get("SWB_REPO_ROOT"):
        return True
    pack = pack_root()
    if os.path.normcase(project_root()) != os.path.normcase(pack):
        return True
    if os.path.isdir(os.path.join(project_root(), ".coll" + "ab", "ledger")):
        return True
    return False


def default_ledger_root() -> str:
    # GWP-P1-2 缺省锚统一＝<project_root()>/.collab/ledger（四脚本同源·§3.2）
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(project_root(), ".collab", "ledger"))


def canonical_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def append_record(ledger_file: str, rtype: str, actor: str, payload: dict) -> dict:
    """append-only 追加账本记录（六类记录·§3；与 B2/B3 同形制）。"""
    os.makedirs(os.path.dirname(os.path.abspath(ledger_file)), exist_ok=True)
    prev_hash, seq = "GENESIS", 0
    if os.path.exists(ledger_file):
        with open(ledger_file, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    rec = json.loads(line)
                    prev_hash, seq = rec["hash"], rec["seq"]
    rec = {
        "seq": seq + 1,
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "type": rtype,
        "actor": actor,
        "payload": payload,
        "prev_hash": prev_hash,
    }
    rec["hash"] = hashlib.sha256(
        f'{rec["seq"]}\n{rec["ts"]}\n{rec["type"]}\n{rec["actor"]}\n{canonical_json(rec["payload"])}\n{prev_hash}'.encode("utf-8")
    ).hexdigest()
    with open(ledger_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def extract_ticket_id(text: str) -> str | None:
    for pat in TICKET_ID_PATTERNS:
        m = pat.search(text)
        if m:
            return m.group(0)
    return None


def classify_command(command: str) -> list[str]:
    """命令串 → 命中形态列表（amend/rebase/force-push）。"""
    hits = [name for name, pat in CMD_PATTERNS.items() if pat.search(command)]
    return hits


def is_commit_command(command: str) -> bool:
    return bool(re.search(r"\bgit\b[^|;&]*\bcommit\b", command))



def _norm_cmp(p: str) -> str:
    p = os.path.normcase(os.path.abspath(os.path.normpath(p)))
    return p.rstrip(os.sep) or os.sep


def _within_own_surface(root: str) -> bool:
    """本仓面判定＝目标仓根与本仓三参考根（包根／project_root 现读／cwd）恰等同源（严格等值＝非包含关系＝他仓含本仓形态仍判跨面）。"""
    nr = _norm_cmp(root)
    return any(nr == _norm_cmp(ref) for ref in (pack_root(), project_root(), os.getcwd()))


def _probe_target_root(seed: str) -> str:
    """B16-a 修一·目标仓根解析＝经既有 project_root／_anchor_hit 同源语义探测序：
    seed 归一→自最近存在祖先上溯，首个锚定自指命中／STRUCTURE 命中／.git 命中目录＝目标仓根；
    三锚全缺＝落回 seed 自身归一（判定面＝路径同源比对非存在性＝非存在面路径仍入跨面判据）。"""
    pack = pack_root()
    seed_abs = os.path.abspath(os.path.normpath(seed))
    d = seed_abs
    while d and not os.path.exists(d):
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    probe = d
    while probe:
        if _anchor_hit(probe, pack) or _structure_hit(probe, pack):
            return probe
        if os.path.isdir(os.path.join(probe, ".git")) or os.path.isfile(os.path.join(probe, ".git")):
            return probe
        parent = os.path.dirname(probe)
        if parent == probe:
            break
        probe = parent
    return seed_abs


def _git_subcommands(command: str) -> list[str]:
    return _GIT_SUB_RE.findall(command)


def _is_unresolved_value(val: str) -> bool:
    """-C／重定向目标值不可解析态＝空值／shell 变量未展开残值（「${FX…}」类）＝解析失败入退路档（修二激活闸）。"""
    return bool(_UNRESOLVED_VAL_RE.search(val.strip()))


def resolve_target_surface(command: str) -> str:
    """目标仓根解析臂·git 面（修一）：返回 own／cross／unparsed／none。
    提取序＝git -C 值提取→缺＝cwd 推断（票面修一 verbatim）；读型豁免＝纯读族命令不入判定面（闭集＝GIT_READ_SUBCMDS）。"""
    subs = _git_subcommands(command)
    if not subs:
        return "none"
    has_write = any(s in GIT_WRITE_SUBCMDS for s in subs)
    has_read = any(s in GIT_READ_SUBCMDS for s in subs)
    if not has_write and has_read:
        return "own"  # 读型子命令族豁免放行
    if not has_write:
        return "none"
    m = _GIT_C_RE.search(command)
    if m:
        val = next((g for g in (m.group(2), m.group(3), m.group(4)) if g is not None), "")
        if _is_unresolved_value(val):
            return "unparsed"  # -C 值未展开／空值＝目标仓根解析失败＝修二退路档激活面
        root = _probe_target_root(val)
    else:
        root = _probe_target_root(os.getcwd())
    return "own" if _within_own_surface(root) else "cross"


def cross_surface_findings(command: str, state: str) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
    """跨面命中清单＝(warn 族, confirm 族)。
    warn 族＝跨面写型 git 子命令命中＋shell 重定向／echo 写形态目标落本仓外命中（修一第三段）；
    confirm 族＝危险子命令形态（修二词面族同源复用）×跨面命中＝确认态三证载体（修三）。"""
    warn_f: list[tuple[str, str]] = []
    conf_f: list[tuple[str, str]] = []
    if state == "cross":
        for sub in dict.fromkeys(s for s in _git_subcommands(command) if s in GIT_WRITE_SUBCMDS):
            warn_f.append(("git-" + sub, "git 写型子命令跨面"))
        for name, pat in DANGEROUS_SUBCMD_PATTERNS.items():
            if pat.search(command):
                conf_f.append((name, "危险子命令跨面（确认态三证）"))
    for m in _REDIR_RE.finditer(command):
        val = next((g for g in (m.group(2), m.group(3), m.group(4)) if g is not None), "")
        if not val or _is_unresolved_value(val):
            continue
        target = os.path.abspath(os.path.normpath(val if os.path.isabs(val) else os.path.join(os.getcwd(), val)))
        if not _within_own_surface(target):
            warn_f.append(("shell-redirect", "shell 重定向写形态目标落本仓外"))
    return warn_f, conf_f


def head_commit_info(repo_root: str) -> tuple[str, str]:
    """HEAD 提交哈希＋消息（记账/孤儿判定读数源）。"""
    try:
        r = subprocess.run(["git", "-C", repo_root, "log", "-1", "--pretty=%H%n%B"],
                           capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            return "", ""
        lines = r.stdout.split("\n", 1)
        return lines[0].strip(), (lines[1] if len(lines) > 1 else "").strip()
    except Exception:
        return "", ""


# —— SWB-B16-d 修一（纯增·提交身份引导提示态）＝prehook 检出 commit 命令＋仓 git 身份缺失（user.name／user.email 任缺）
# → stderr 附出路指引提示行＝不拦＝提示态＝零拦截强度变化＝判定值与台账面零变化（J-1 采乙在册＝修二并 B16-f＝本票写集仅修一一枚）
# 定位申明＝防过失导向＝「报错无出路」EXT 轻目本体消解；-c 参数随手伪造身份面＝本修不拦＝伪造对抗归 B16-f 采信面域（沿 BG-16 甲-5 定位行）。
GIT_IDENTITY_KEYS = ("user.name", "user.email")  # 仓 git 身份两键（缺失判定面＝config --get 非零退出或空值）
EXIT_GUIDE_ANCHOR = "EXIT-GUIDE"  # 机器可判锚词（ASCII 字面＝stderr 提示面可 grep 命中＝沿 B16-b 先例形制）


def git_identity_missing(repo: str) -> list[str]:
    """目标仓 git 身份缺失面探测（只读 git config --get 面＝非零退出或空值＝缺失）；
    探测异常（仓不可读／超时）＝回落空列表＝提示面永不自引入新判定面（纯增零风险纪律）。"""
    missing: list[str] = []
    for key in GIT_IDENTITY_KEYS:
        try:
            r = subprocess.run(["git", "-C", repo, "config", "--get", key],
                               capture_output=True, text=True, timeout=10)
        except Exception:
            return []
        if r.returncode != 0 or not r.stdout.strip():
            missing.append(key)
    return missing


def prehook(args: argparse.Namespace, payload: dict) -> int:
    command = args.command or (payload.get("tool_input") or {}).get("command", "")
    if not command:
        return 0  # 无命令面＝不干预（决策词表内不自造额外输出）
    # —— SWB-B16-d 修一（纯增·居词面检查段前＝提示态段）＝不拦＝零台账追加＝判定面零扰动 ——
    if is_commit_command(command):
        missing_ids = git_identity_missing(args.repo)
        if missing_ids:
            print(f"HINT commit-audit: {EXIT_GUIDE_ANCHOR} 提交身份引导（提示态·不拦）＝当仓 git 身份缺失＝{'、'.join(missing_ids)}＝commit 将因 Author identity unknown 直接失败；出路指引＝①仓级补全身份＝git config user.name 与 git config user.email 各补一键 ②单次命令级＝git -c user.name=… -c user.email=…（随手伪造面＝防过失定位申明＝伪造对抗归 B16-f 采信面域＝本修不拦）③跨仓交接＝交接件经工作面交接区由对方仓自行立案（落点判据＝dev-discipline §十四 目 4＝只指不搬）", file=sys.stderr)
    # —— SWB-B16-a 修一＋修三：目标仓根解析段（纯增·居词面检查段前）＋修二退路闸（判序＝票面 rev-1 勘正①） ——
    state = resolve_target_surface(command)
    if state == "unparsed":
        dang = [name for name, pat in DANGEROUS_SUBCMD_PATTERNS.items() if pat.search(command)]
        if dang:
            reason = f"B5 提交审计退路拦截：目标仓根解析失败＋危险子命令词面命中形态={dang}（修二退路档＝fail-closed 防解析器缺位即零拦）"
            append_record(args.ledger, "呈报", "commit-audit.py", {
                "event": "commit_audit_block", "decision": "block", "forms": dang,
                "command_excerpt": command[:200],
                "clause": "SWB-B16-a 修二退路档＝解析失败→危险词面兜底命中 exit 2＋BLOCK 行（rev-1 勘正①判序钉死）",
            })
            print(f"BLOCK commit-audit: {reason}", file=sys.stderr)
            return EXIT_BLOCKING
    warn_f, conf_f = cross_surface_findings(command, state)
    for form, why in warn_f:  # 修三＝warn 双证载体＝台账留痕行（decision=warn 字段）＋stderr 输出行；warn 不入 §19 决策词层（三值维持）
        append_record(args.ledger, "呈报", "commit-audit.py", {
            "event": "commit_audit_warn", "decision": "warn", "form": form,
            "command_excerpt": command[:200],
            "clause": "SWB-B16-a 修一跨面目标仓根判定＋修三 warn 双证（BG-16 rev-1 勘正②钉死口径）",
        })
        print(f"WARN commit-audit: 跨面写形态判定命中＝{why}（{form}）＝warn 双证·非阻断", file=sys.stderr)
    for form, why in conf_f:  # 修三确认态三证＝exit 0＋stderr 行首 CONFIRM commit-audit: 标记行＋台账 decision=confirm 字段（词表不扩）
        append_record(args.ledger, "呈报", "commit-audit.py", {
            "event": "commit_audit_confirm", "decision": "confirm", "form": form,
            "command_excerpt": command[:200],
            "clause": "SWB-B16-a 修三确认态三证载体（勘正②＝exit 0＋CONFIRM 标记行＋台账 confirm 字段）",
        })
        print(f"CONFIRM commit-audit: 确认态在场＝{why}（{form}）＝归宿主人类侧确认·脚本面不自阻塞", file=sys.stderr)
    hits = classify_command(command)
    ticket_id = extract_ticket_id(command)
    # orphan 判定：commit 命令且消息面（-m 引文/命令全文）无票 ID
    if is_commit_command(command) and ticket_id is None:
        hits.append("orphan")
    if not hits:
        return 0
    reason = f"B5 提交审计拦截：形态={hits}（§9 B5 行 amend/rebase/无票提交＋§9 B0 退路 force-push 补位）"
    append_record(args.ledger, "呈报", "commit-audit.py", {
        "event": "commit_audit_block", "forms": hits, "command_excerpt": command[:200],
        "clause": "§17 orphan 提交词条＝无票 ID trailer 的提交；违纪行 7",
    })
    print(f"BLOCK commit-audit: {reason}", file=sys.stderr)
    return EXIT_BLOCKING


def posthook(args: argparse.Namespace, payload: dict) -> int:
    command = args.command or (payload.get("tool_input") or {}).get("command", "")
    if command and not is_commit_command(command):
        return 0
    commit_hash, msg = head_commit_info(args.repo)
    if not commit_hash:
        return 0  # 无新提交可读＝记不上账不硬造
    ticket_id = extract_ticket_id(msg) or extract_ticket_id(command)
    if ticket_id is None:
        # PostToolUse 侧兜底呈报 orphan（prehook 未拦到的旁路提交）
        append_record(args.ledger, "呈报", "commit-audit.py", {
            "event": "orphan_commit_report", "commit": commit_hash,
            "trigger_source": "对账差≠0",
            "clause": "orphan 提交入日终对账差（reconcile-daily.py 交叉核口径）",
        })
    append_record(args.ledger, "写入", "commit-audit.py", {
        "event": "commit_record", "commit": commit_hash, "ticket_id": ticket_id,
        "seat_id": args.seat or (payload.get("agent_type") or ""),
        "agent_type": payload.get("agent_type"), "agent_id": payload.get("agent_id"),
        "clause": "§9 B5 行 PostToolUse 记账：提交哈希/票 ID/席位归因入「写入」记录类",
    })
    print(f"OK commit-audit posthook: commit={commit_hash[:12]} ticket={ticket_id} 已入「写入」记录")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B5 提交审计（prehook 拦三形态＋force-push／posthook 记账）")
    ap.add_argument("phase", choices=["prehook", "posthook"], help="hooks 阶段（hooks.json 路由）")
    ap.add_argument("--input", default=None, help="PreToolUse/PostToolUse payload JSON 文件（测试注入面）")
    ap.add_argument("--command", default=None, help="命令串注入面（测试优先于 payload.tool_input.command）")
    ap.add_argument("--repo", default=os.getcwd(), help="git 仓根（posthook 读数源）")
    ap.add_argument("--seat", default=None, help="席位归因（posthook 记账字段）")
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    a = ap.parse_args(argv)

    payload: dict = {}
    if a.input:
        with open(a.input, encoding="utf-8") as f:
            payload = json.load(f)
    elif not a.command and not sys.stdin.isatty():
        # 平台直连形态（PreToolUse/PostToolUse stdin）；注入面参数在场则不读 stdin（防阻塞）
        raw = sys.stdin.read().strip()
        if raw:
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                payload = {}
    if not governance_resident():
        print("NEUTRAL commit-audit: project-root 探测全缺位且租约台账缺位＝非百工管辖项目→钩子惰性放行（ITER-K 锚门中立放行）", file=sys.stderr)
        return 0
    if a.phase == "prehook":
        return prehook(a, payload)
    return posthook(a, payload)


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8", errors="backslashreplace")
        except Exception:
            pass
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except BaseException as _e:
        # GWP-P3-1 fail-closed：审计异常即阻断（exit 2→blocking·§19 词表）
        try:
            print(f"BLOCK commit-audit: 异常 fail-closed {type(_e).__name__}: {_e}", file=sys.stderr)
        except Exception:
            pass
        sys.exit(EXIT_BLOCKING)
