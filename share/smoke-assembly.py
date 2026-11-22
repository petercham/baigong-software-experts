#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: MC-PFA-SMOKE-1
# spec_file: agent-experts/baigong-software-team/skills/software-orchestration/references/deploy-gate.md
# spec_anchor: 5. **段②行为冒烟（必跑）**
# spec_clause_sha256: 6727c208f4f9d99a379219dfb32c09a5227b8441f1acb12d256f720e2067092b
# spec_version: 1.2
# spec_effective: 2026-11-23
# provider: baigong-software-team
# --- /spec-provenance ---
#
# smoke-assembly.py · 装配面行为冒烟闸（PF-A·SWB-BG-10·share 闸族新增冒烟闸＝新建非改既有闸）
#
# 条款真源（只指路径，不复写正文）＝deploy-gate 卷 §五要点5 条款句（上方 spec-provenance
#   块锚定该行；clause sha256＝施工窗 S1 落位后现算回填，回填口径＝票面 §三 S2 一目）。
# 规格真源＝票面（只读对钉）＝本仓 .collab／board／ 下 PF-A 装配冒烟闸票面 v1 §三 S2
#   五目＋放行段落拍（J-1 甲＝A4 快照登记目＋他仓工单随登；J-2 乙向＝compile 之外补
#   subprocess 零参实跑第三臂防 __pycache__；J-3 甲＝计数锚默认钉 4 失配即红；
#   前置裁定＝两态设计）。
#
# 取的面＝--pkg 指装配面包根，两种取的面（放行段写死）＝
#   段①重装配新面（仓外 <仓>-build 面包根）＋市场源镜像同步面（宿主市场源目录下包根）。
#   对缺陷旧装配面（已出土缺陷的旧版本面＝command 串仍为旧形制）跑 exit 1＝预期红形
#   登记，非本闸缺陷＝本闸对该面如实报红正是其存在目的。
#
# 两态设计（放行段前置裁定＝闸不代裁）＝
#   装配面 hooks／hooks.json 在位 → 全臂（A1—A4）跑；
#   hooks.json 不在位（含摘除态批次）→ 输出豁免登记行（NOTE 形制·不进路由计数）
#     ＋hooks 臂计数归零→exit 0；禁对缺位面 exit 4 反向绑架段③裁量。
#   注：hooks.json 在位但不可解析＝装载态缺陷＝fail-closed exit 4 照报。
#
# 绿灯语义边界（输出行与 help 自声明·S1 条款句尾同款句）＝本闸全绿语义＝
#   「command 串可解＋被引脚本在盘＋源码可 compile＋脚本零参实跑可载入」＝
#   不含「matcher 命中→钩子 fires」语义＝matcher 词表对宿主工具名闭集核对机械判缺
#   真源（A4 只快照不判＝J-1 裁甲·他仓工单在册候真源登记后另票升级）。
#
# 判据闭集四目（票 §三 S2 四目展开）＝
#   A1 计数目＝hooks.json 可解析＋command 条目总数＝--expect-commands（默认钉 4）失配 BLOCK；
#   A2 可解目＝逐 command 串提取脚本径 token→${CODEBUDDY_PLUGIN_ROOT} 替换为包根径→
#       os.path.isfile 全真，解空即 BLOCK；
#   A3 载入目两形＝对 A2 解出各脚本源码进程内 compile 全成（语法败即 BLOCK·零写盘＝
#       禁 py_compile 缺省写字节码）＋subprocess 零参实跑各脚本（退出码 ∈ {0,2}＝可载入
#       执行形制；其余退出码或无法起进程即 BLOCK＝防运行期缺件）＝J-2 乙向第三臂；
#       实跑臂全程 env＝PYTHONDONTWRITEBYTECODE=1＋SWB_LEDGER_ROOT 重定向系统临时区＝
#       真面与夹具双侧零 __pycache__ 零账本写盘自证；
#   A4 matcher 快照登记目＝各组 matcher 现值快照输出（观察不判）。
#
# 入参闭集＝--pkg（可重复·装配面包根）／--selftest／--expect-commands（计数锚·默认 4）。
# 退出码闭集沿 share 族＝0 全过（含 hooks 缺位豁免态）／1 有 BLOCK／2 用法错／
#   4 fail-closed＝--pkg 所指包根不存在或 hooks.json 在位但不可解析。
# 输出形制沿 FINDING_RE 兼容一行一封 file:line: SEV spec msg＋末行计数汇总行；
#   豁免登记行与 A4 快照行不带 BLOCK／WATCH 词＝run-gates FINDING_RE 不匹配＝不参与路由计数。
# 本件只读零写＝脚本体对仓内与装配面禁任何写盘动作；--selftest 夹具全程落系统临时区
#   （tempfile 用毕自拆＝零残留·沿 K 双向断言先例）。
"""装配面行为冒烟闸（PF-A·部署闸段②机械冒烟目）。

用法：
    python smoke-assembly.py --pkg <装配面包根> [--pkg ...] [--expect-commands 4]
    python smoke-assembly.py --selftest

退出码（闭集）：0 全过（含豁免态）／1 有 BLOCK／2 用法错／4 fail-closed。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

EXIT_OK = 0
EXIT_BLOCK = 1
EXIT_USAGE = 2
EXIT_INFRA = 4

DEFAULT_EXPECT_COMMANDS = 4  # J-3 采甲＝默认钉 4（与 hooks 现面咬合）＝失配即红
PLUGIN_ROOT_VAR = "${CODEBUDDY_PLUGIN_ROOT}"
SEV_BLOCK = "BLOCK"
SPEC_ID = "MC-PFA-SMOKE-1"
SPEC_FILE_REL = "agent-experts/baigong-software-team/skills/software-orchestration/references/deploy-gate.md"
CLAUSE_ANCHOR = "5. **段②行为冒烟（必跑）**"

QUOTED_SEG_RE = re.compile(r'"([^"]*)"')
UNSPLIT_WS_RE = re.compile(r"\S+")
SCRIPT_EXT_RE = re.compile(r"\.(?:py|sh|js|ps1)$")


def die_usage(msg: str):
    sys.stderr.write("usage error: %s\n" % msg)
    raise SystemExit(EXIT_USAGE)


def find_repo_root() -> str:
    """仓根定位＝本件上溯找 share/（只读零副作用·沿 share 族同款）。"""
    cur = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isdir(os.path.join(cur, "share")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return ""
        cur = parent


def clause_sha256_now():
    """对 deploy-gate 卷 §五要点5 条款行现算 sha256（沿 check-provenance 规范化口径＝
    去首尾空白→连续空白压单空格→UTF-8→sha256 小写）。自证读数只读零写；不在场＝空串。"""
    root = find_repo_root()
    if not root:
        return ""
    spec_abs = os.path.join(root, SPEC_FILE_REL.replace("/", os.sep))
    if not os.path.isfile(spec_abs):
        return ""
    try:
        with open(spec_abs, encoding="utf-8", newline="") as fh:
            text = fh.read().replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError):
        return ""
    for raw in text.split("\n"):
        probe = raw.strip()
        if probe.startswith(CLAUSE_ANCHOR):
            norm = re.sub(r"\s+", " ", probe)
            return hashlib.sha256(norm.encode("utf-8")).hexdigest()
    return ""


def extract_commands(pkg_root: str):
    """读装配面 hooks／hooks.json→(cmds, matchers, err)。
    cmds＝[(event_name, entry_idx, command_str)]；matchers＝[(event_name, matcher_str)]。
    err＝fail-closed 原因；三 None＝hooks.json 不在位（两态设计走豁免登记）。"""
    hooks_path = os.path.join(pkg_root, "hooks", "hooks.json")
    if not os.path.isfile(hooks_path):
        return (None, None, None)
    try:
        with open(hooks_path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError) as exc:
        return (None, None, "hooks.json 不可解析：%s" % exc)
    hooks = data.get("hooks")
    if not isinstance(hooks, dict):
        return (None, None, "hooks.json 缺 hooks 键或类型非对象")
    cmds: "list[tuple[str, int, str]]" = []
    matchers: "list[tuple[str, str]]" = []
    for event_name, entries in hooks.items():
        if not isinstance(entries, list):
            return (None, None, "hooks.%s 类型非数组" % event_name)
        for idx, entry in enumerate(entries):
            if not isinstance(entry, dict):
                return (None, None, "hooks.%s[%d] 类型非对象" % (event_name, idx))
            matchers.append((event_name, entry.get("matcher", "")))
            inner = entry.get("hooks", [])
            if not isinstance(inner, list):
                return (None, None, "hooks.%s[%d].hooks 类型非数组" % (event_name, idx))
            for h in inner:
                if isinstance(h, dict) and h.get("type") == "command" \
                        and isinstance(h.get("command"), str):
                    cmds.append((event_name, idx, h["command"]))
    return (cmds, matchers, "")


def substitute_paths(pkg_root: str, cmd: str) -> "list[str]":
    """A2 提取＋替换＝${CODEBUDDY_PLUGIN_ROOT}→包根径后取脚本径 token；
    不含插件根锚＝解空（旧形制／缺锚＝装载态缺陷形态）。"""
    if PLUGIN_ROOT_VAR not in cmd:
        return []
    replaced = cmd.replace(PLUGIN_ROOT_VAR, pkg_root)
    # token 提取＝先取引号段、再取其余空白界 token；只留以脚本扩展名结尾者
    paths: "list[str]" = []
    rest = replaced
    for m in QUOTED_SEG_RE.finditer(replaced):
        tok = m.group(1)
        if SCRIPT_EXT_RE.search(tok):
            paths.append(tok)
        rest = rest.replace(m.group(0), " ")
    for tok in UNSPLIT_WS_RE.findall(rest):
        if SCRIPT_EXT_RE.search(tok):
            paths.append(tok)
    return paths


def run_smoke_on_pkg(pkg_root: str, expect_commands: int, ledger_tmp: str):
    """对一个装配面跑全臂→(findings, counters, infra_err)。"""
    findings: "list[str]" = []
    counters = dict(command_count=0, isfile_ok=0, isfile_fail=0,
                    compile_ok=0, compile_fail=0, exec_ok=0, exec_fail=0,
                    snapshot=0, exempt=0)
    label = os.path.normpath(pkg_root).replace(os.sep, "/")
    rel_hooks = label + "/hooks/hooks.json"

    cmds, matchers, err = extract_commands(pkg_root)
    if cmds is None and err is None:
        # 两态设计＝hooks.json 不在位（含摘除态批次）＝豁免登记行＋hooks 臂计数归零→exit 0
        print("%s:1: NOTE-EXEMPT %s hooks 臂不在位＝豁免登记（摘除态批次＝挂不挂随段③人类闸裁量·本闸不代裁）"
              % (rel_hooks, SPEC_ID))
        counters["exempt"] = 1
        return (findings, counters, "")
    if err:
        return (findings, counters, "%s（%s）" % (err, label))

    # A1 计数目
    counters["command_count"] = len(cmds)
    if len(cmds) != expect_commands:
        findings.append("%s:1: %s %s A1 计数失配＝command 条目 %d 枚不等于锚 %d 枚（增减目须同步锚）"
                        % (rel_hooks, SEV_BLOCK, SPEC_ID, len(cmds), expect_commands))

    # A4 matcher 快照登记目（观察不判＝J-1 裁甲·宿主工具名闭集真源在盘缺位）
    for event_name, matcher in matchers:
        print("%s:1: NOTE-SNAP %s A4 matcher 快照 %s＝%s（观察不判）"
              % (rel_hooks, SPEC_ID, event_name, matcher))
        counters["snapshot"] += 1

    seen_scripts: "list[str]" = []
    for event_name, idx, cmd in cmds:
        paths = substitute_paths(pkg_root, cmd)
        if not paths:
            findings.append("%s:%d: %s %s A2 解空＝command 串不含插件根锚替换形制：%s"
                            % (rel_hooks, idx + 1, SEV_BLOCK, SPEC_ID, cmd))
            continue
        for p in paths:
            if not os.path.isfile(p):
                findings.append("%s:%d: %s %s A2 被引脚本解径不在盘：%s"
                                % (rel_hooks, idx + 1, SEV_BLOCK, SPEC_ID, p))
                counters["isfile_fail"] += 1
                continue
            counters["isfile_ok"] += 1
            if p in seen_scripts:
                continue
            seen_scripts.append(p)
            # A3 载入臂甲＝进程内 compile（零写盘）
            try:
                with open(p, encoding="utf-8") as fh:
                    src = fh.read()
                compile(src, p, "exec")
                counters["compile_ok"] += 1
            except (OSError, SyntaxError, ValueError) as exc:
                findings.append("%s:%d: %s %s A3 载入臂 compile 败：%s（%s）"
                                % (rel_hooks, idx + 1, SEV_BLOCK, SPEC_ID, p, exc))
                counters["compile_fail"] += 1
            # A3 载入臂乙＝subprocess 零参实跑（J-2 乙向＝防运行期缺件；账本与字节码双零写）
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", SWB_LEDGER_ROOT=ledger_tmp)
            try:
                proc = subprocess.run([sys.executable, p], stdin=subprocess.DEVNULL,
                                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                      env=env, timeout=30)
            except (OSError, subprocess.TimeoutExpired) as exc:
                findings.append("%s:%d: %s %s A3 实跑臂无法起进程：%s（%s）"
                                % (rel_hooks, idx + 1, SEV_BLOCK, SPEC_ID, p, exc))
                counters["exec_fail"] += 1
                continue
            if proc.returncode in (0, 2):
                counters["exec_ok"] += 1
            else:
                findings.append("%s:%d: %s %s A3 实跑臂退出码 %d 不属于 {0,2}＝运行期缺件或缺依赖：%s"
                                % (rel_hooks, idx + 1, SEV_BLOCK, SPEC_ID, proc.returncode, p))
                counters["exec_fail"] += 1
    return (findings, counters, "")


def iter_pkg_surfaces(pkg_list: "list[str]") -> "list[str]":
    """面枚举＝逐枚 --pkg 展开：所指目录若为宿主层（内含多个含 hooks／plugin.json 的子包根
    且自身不是包根）则逐子包根展开；否则所指目录自身即包根。只列举零写入。"""
    surfaces: "list[str]" = []
    for pkg in pkg_list:
        pkg = os.path.abspath(pkg)
        if not os.path.isdir(pkg):
            die_usage("--pkg 不存在：%s" % pkg)
        try:
            names = sorted(os.listdir(pkg))
        except OSError as exc:
            die_usage("--pkg 不可列举：%s（%s）" % (pkg, exc))
        sub_surfaces: "list[str]" = []
        for name in names:
            d = os.path.join(pkg, name)
            if os.path.isdir(d) and (os.path.isdir(os.path.join(d, "hooks"))
                                     or os.path.isfile(os.path.join(d, "plugin.json"))):
                sub_surfaces.append(d)
        direct = (os.path.isdir(os.path.join(pkg, "hooks"))
                  or os.path.isfile(os.path.join(pkg, "plugin.json")))
        if direct:
            surfaces.append(pkg)
        elif sub_surfaces:
            surfaces.extend(sub_surfaces)
        else:
            surfaces.append(pkg)
    return surfaces


def selftest(expect_commands: int) -> int:
    """双向夹具（系统临时区·用毕自拆·零触仓内与真装配面）＝
    正夹具 exit 0 全臂读数＋负夹具缺被引一枚脚本 exit 1 形 BLOCK 行在＋零 __pycache__ 自证。"""
    tmp = tempfile.mkdtemp(prefix="smoke-assembly-selftest-")
    ledger_tmp = os.path.join(tmp, "fx_ledger")
    ok = True
    try:
        # ---- 正夹具＝合成包面（四 command 串＋三枚占位脚本在位）----
        good = os.path.join(tmp, "goodpkg")
        os.makedirs(os.path.join(good, "hooks"))
        os.makedirs(os.path.join(good, "scripts"))
        placeholder = os.path.join(good, "scripts", "placeholder.py")
        with open(placeholder, "w", encoding="utf-8") as fh:
            fh.write("import sys\nsys.exit(0)\n")
        cmd_tpl = 'python "%s"' % os.path.join(PLUGIN_ROOT_VAR, "scripts", "placeholder.py")
        hooks_body = {
            "hooks": {
                "PreToolUse": [
                    {"matcher": "Write|Edit|MultiEdit", "hooks": [{"type": "command", "command": cmd_tpl}]},
                    {"matcher": "Read|Grep", "hooks": [{"type": "command", "command": cmd_tpl}]},
                    {"matcher": "Bash", "hooks": [{"type": "command", "command": cmd_tpl}]},
                ],
                "PostToolUse": [
                    {"matcher": "Bash", "hooks": [{"type": "command", "command": cmd_tpl}]},
                ],
            }
        }
        with open(os.path.join(good, "hooks", "hooks.json"), "w", encoding="utf-8") as fh:
            json.dump(hooks_body, fh, ensure_ascii=False)
        findings, counters, infra = run_smoke_on_pkg(good, expect_commands, ledger_tmp)
        pos_green = (not findings) and (not infra) and counters["command_count"] == 4 \
            and counters["isfile_ok"] == 4 and counters["compile_ok"] == 1 \
            and counters["exec_ok"] == 1 and counters["snapshot"] == 4 \
            and ledger_tmp_is_empty(ledger_tmp)
        if not pos_green:
            ok = False
            print("SELFTEST-BAD 正夹具＝exit 0 全读数未达成 findings=%r infra=%r counters=%r"
                  % (findings, infra, counters))
        pyc = [d for d, _ds, _fs in os.walk(tmp) if "__pycache__" in d]
        if pyc:
            ok = False
            print("SELFTEST-BAD 夹具区出现 __pycache__＝实跑臂零写盘自证未达成：%r" % pyc)

        # ---- 负夹具＝缺被引一枚脚本（A2 必拦＝memory 缺位形沿 QA 演练形制）----
        bad = os.path.join(tmp, "badpkg")
        os.makedirs(os.path.join(bad, "hooks"))
        os.makedirs(os.path.join(bad, "scripts"))
        with open(os.path.join(bad, "hooks", "hooks.json"), "w", encoding="utf-8") as fh:
            json.dump(hooks_body, fh, ensure_ascii=False)
        findings_b, counters_b, infra_b = run_smoke_on_pkg(bad, expect_commands, ledger_tmp)
        neg_red = (infra_b == "") and findings_b \
            and any("A2" in f for f in findings_b) \
            and counters_b["isfile_fail"] >= 1
        if not neg_red:
            ok = False
            print("SELFTEST-BAD 负夹具＝A2 BLOCK 行未达成 findings=%r infra=%r counters=%r"
                  % (findings_b, infra_b, counters_b))
        if ok:
            print("SELFTEST-OK 正夹具四臂全绿＋负夹具 A2 缺位形 BLOCK 命中＋夹具区零 __pycache__＋账本区零写＝双向断言在册")
        return EXIT_OK if ok else EXIT_BLOCK
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def ledger_tmp_is_empty(ledger_tmp: str) -> bool:
    return (not os.path.isdir(ledger_tmp)) or (not os.listdir(ledger_tmp))


def main(argv: "list[str] | None" = None) -> int:
    ap = argparse.ArgumentParser(
        description="装配面行为冒烟闸（PF-A·部署闸段②机械冒烟目）＝A1 计数／A2 可解／A3 载入两形／A4 快照",
        epilog="取的面＝--pkg 装配面包根（段①重装配新面／市场源镜像同步面两种取的面）；"
               "对缺陷旧装配面跑 exit 1＝预期红形登记非本闸缺陷；hooks.json 不在位（含摘除态）＝"
               "豁免登记行＋exit 0（两态设计＝闸不代裁·挂不挂随段③人类闸）。"
               "绿灯语义不含「matcher 命中→钩子 fires」。")
    ap.add_argument("--pkg", "--root", dest="pkg", action="append", default=None,
                    help="装配面包根（可重复；所指目录若为宿主层＝内含多包根＝逐包根展开）"
                         "（--root＝票 §三 S2 二目 verbatim 措辞别名·同参同义）")
    ap.add_argument("--expect-commands", type=int, default=DEFAULT_EXPECT_COMMANDS,
                    help="A1 计数锚（默认钉 4＝失配即红·J-3 采甲）")
    ap.add_argument("--selftest", action="store_true",
                    help="系统临时区双向夹具干跑（用毕自拆·零触仓内与真装配面）")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest(args.expect_commands)
    if not args.pkg:
        die_usage("缺 --pkg（装配面包根）或 --selftest")

    print("# clause_sha256 现算自证 deploy-gate §五要点5 条款行＝%s（头部回填对拍用·只读零写）"
          % (clause_sha256_now() or "条款行不在场"))

    surfaces = iter_pkg_surfaces(args.pkg)
    ledger_tmp = tempfile.mkdtemp(prefix="smoke-assembly-ledger-")
    total = dict(BLOCK=0, command=0, isfile_ok=0, isfile_fail=0,
                 compile_ok=0, compile_fail=0, exec_ok=0, exec_fail=0,
                 snapshot=0, exempt=0)
    worst = EXIT_OK
    try:
        for surface in surfaces:
            findings, counters, infra = run_smoke_on_pkg(surface, args.expect_commands, ledger_tmp)
            for f in findings:
                print(f)
            if infra:
                sys.stderr.write("infra error: %s\n" % infra)
                worst = EXIT_INFRA
                continue
            total["BLOCK"] += len(findings)
            total["command"] += counters["command_count"]
            for k in ("isfile_ok", "isfile_fail", "compile_ok", "compile_fail",
                      "exec_ok", "exec_fail", "snapshot", "exempt"):
                total[k] += counters[k]
            if findings and worst != EXIT_INFRA:
                worst = EXIT_BLOCK
        print("# smoke-assembly 汇总 面 %d 枚：BLOCK %d command %d isfile %d／%d compile %d／%d exec %d／%d snap %d exempt %d"
              % (len(surfaces), total["BLOCK"], total["command"],
                 total["isfile_ok"], total["isfile_ok"] + total["isfile_fail"],
                 total["compile_ok"], total["compile_ok"] + total["compile_fail"],
                 total["exec_ok"], total["exec_ok"] + total["exec_fail"],
                 total["snapshot"], total["exempt"]))
    finally:
        shutil.rmtree(ledger_tmp, ignore_errors=True)
    return worst


if __name__ == "__main__":
    sys.exit(main())
