#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check-ticket.py · 票面合规机械闸（ITER-W2-T2b 交付·票面 §三 S1 规格＋票级放行登记随正条款全覆盖）

判据单一真源＝thin 票面模板（skills/software-orchestration/references/thin-ticket-template.md）
盘面运行时动态解析；脚本体内零硬编码判据正文＝模板改闸随动（红-1 随正条款：全部判据
正文一律以 thin 盘面真源运行时解析为唯一准，禁从任何票面引用行取 verbatim）。

检查项闭集八目：
    CT-1 七节骨架＝模板七节节题各恰 1 且次序不逆；额外节题仅可现于链衔接节之后 BLOCK
    CT-2 预置固定行逐字＝具名枚举口径（红-2 随正·通用解析预置句已删禁复活）：警示行／
         禁动五行族行／候裁预置行／链衔接节体行（七子弹＋尾标闭集自校行）／模板尾行
         ＝对 thin 现势运行时解析（12 枚集＝QA 概念验证实证）；适用域＝面日期 ≥
         --since 新面（存量豁免 J-5）BLOCK
    CT-3 体例三零＝全件反引号 0／at 计数 0／非缩进段半斜杠 0（四空格及以上缩进段豁免）BLOCK
    CT-4 V 骨架全填＝"- V0 " 至 "- V6 " 行起始各恰 1 BLOCK
    CT-5 槽残留零＝U+27EA 计数 0；豁免面具名两形制头行（黄-3 随正）＝
         「使用说明（固定）」头行＋「模板使用说明（固定）」头行 BLOCK
    CT-6 链笔尾标闭集＝--since 起链上各笔 message 末行以七式之一收尾（七式运行时解析
         自模板体例行尾标括注段按全角斜杠切分）；尾标后粘文／缺尾标／闭集外尾标即违例
         （3bc1f5a5 型）；链笔日期口径＝author date（git log %aI）写死＝黄-4 BLOCK
    CT-7 件名体例＝--ticket-dir 内面日期 ≥ --since 新票文件名须以 YYYY-MM-DD- 起；
         面日期取法＝文件名日期前缀写死（黄-4）；无前缀名面日期回落＝该件 git 新增笔
         author date（历史落笔日＝存量真义·mtime 案不采＝检出制 worktree 内 mtime 全体
         现值致存量必炸）；新增日不可得＝豁免照登；缺省 --since 下存量非日期名全豁免
         （J-5 甲定格·黄-5 随登＝缺省目录硬编码包名路径，他包复用面归候补池）BLOCK
    CT-8 派生数字出处（轻臂 WATCH＝计划行 120「无出处判黄」臂最小兑现·J-1 采甲八目
         全收）＝叙述面「数字＋量词（枚／节／类／行／处）」样式行不含复算口径字样
         （现跑／复算／管道／wc／grep／ls／计数）即 WATCH；叙述面＝排缩进段／节题行／
         表行；本目同受 --since 面适用闸＝计划行 120 扫描域条款（规范生效日后新票·
         防炸基线）覆盖面判据之直译（V2 正样例 exit 0 判据随后方立＝随正后口径申明随登）

入参闭集六枚：--root／--target／--ticket-dir／--since／--template／--selftest
    --root 缺省语义＝自脚本位置向上溯至含 .git（目录或文件两态皆认）之根（黄-4 写死）
    --target 票面路径＝单面模式＝跑 CT-1 至 CT-5＋CT-8（不含 CT-6／CT-7）
    --ticket-dir 缺省＝agent-experts/baigong-software-team/.scratch/tickets
         目录模式＝跑 CT-6＋CT-7（无 --target 时即走此模式）
    --since 缺省 2026-11-20（J-5 采甲放行定格＝存量全豁免防炸基线）
    --template 缺省＝skills 包内 thin 模板盘面现件
    --selftest 内置夹具三态干跑（正样例／违例合成逐目归因／缺件面＝内存夹具零写盘零 git）

退出码闭集（fail-closed·沿 share 族不取 3＝无外部路由表依赖）：
    0 无违例／1 有 BLOCK 或 WATCH 发现／2 用法错／
    4 fail-closed＝--target 件不存在／--template 件不存在／模板预置行集或尾标闭集解析
      为空＝判据真源失联必 fail-closed 不得降级为放行

输出形制＝一行一封 file:line: BLOCK 或 WATCH check-ticket.CT-n 短msg（run-gates
FINDING_RE 兼容）＋末行计数汇总行。本件只读零写＝脚本体禁任何写文件动作（证据件归
调用方窗·run-gates 出口②口径）。

头部注释＝判据真源指向（thin 模板路径＋本票票号 ITER-W2-T2b）＋检查项闭集八目一览。
注释与文档面禁写入线四词字面＝V6 前置保证条款。
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

SLOT_OPEN = "\u27ea"  # U+27EA＝槽标首字符（使用说明行所示槽位标记）
DEFAULT_TICKET_DIR = "agent-experts/baigong-software-team/.scratch/tickets"
DEFAULT_TEMPLATE = ("agent-experts/baigong-software-team/skills/"
                    "software-orchestration/references/thin-ticket-template.md")
DEFAULT_SINCE = "2026-11-20"  # J-5 采甲放行定格
CT8_QUANT = "枚|节|类|行|处"  # 票面 §三.4 五集口径
CT8_CALIBER = ("现跑", "复算", "管道", "wc", "grep", "ls", "计数")
CT8_STYLE_RE = re.compile(r"[0-9０-９]+\s*(%s)" % CT8_QUANT)
NAME_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-")
TRAILER_TOK_RE = re.compile(r"-[A-Z][A-Z-]*$")
SEC_RE = re.compile(r"^## ")


def die(msg: str, code: int) -> None:
    print(msg, file=sys.stderr)
    sys.exit(code)


def find_root(explicit: str | None) -> str:
    """--root 缺省＝自脚本位置向上溯至含 .git 之根（黄-4 一行级写死）。"""
    if explicit:
        if not os.path.isdir(explicit):
            die("usage: --root 不存在：%s" % explicit, 2)
        return os.path.abspath(explicit)
    cur = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.exists(os.path.join(cur, ".git")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            die("infra: 未能定位仓根；请用 --root 指定", 4)
        cur = parent


def read_lines(path: str, why: str) -> list[str]:
    """只读取面；件不存在＝判据真源失联＝exit 4（fail-closed）。"""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read().replace("\r\n", "\n").split("\n")
    except OSError:
        raise InfraMiss("infra: 件不存在或不可读（%s）：%s" % (why, path))


class InfraMiss(Exception):
    pass


# --- 模板真源运行时解析（脚本体内零硬编码判据正文） ---

def parse_template(lines: list[str]) -> tuple[list[str], dict[str, list[str]], list[str]]:
    """自 thin 盘面解析：七节节题闭集／具名枚举预置行集（红-2 随正 12 枚口径）／尾标闭集七式。"""
    sec_titles = [l for l in lines if SEC_RE.match(l)]
    if not sec_titles:
        raise InfraMiss("infra: 模板节题解析为空＝判据真源失联")

    sections: list[tuple[str, list[str]]] = []
    cur: list[str] = []
    for l in lines:
        if SEC_RE.match(l):
            if cur:
                sections.append((cur[0], cur[1:]))
            cur = [l]
        elif cur:
            cur.append(l)
    if cur:
        sections.append((cur[0], cur[1:]))

    preset: dict[str, list[str]] = {}

    # 警示行＝具名头「警示行」起之行
    preset["警示行"] = [l for _, ls in sections for l in ls if l.startswith("警示行")]

    # 禁动五行族行＝「禁动面五行族」引导行之后首个非空行（列表行本体）
    fam: list[str] = []
    for _, ls in sections:
        for i, l in enumerate(ls):
            if l.startswith("禁动面五行族"):
                for m in ls[i + 1:]:
                    if m.strip():
                        if m.lstrip().startswith("-"):
                            fam.append(m)
                        break
    preset["禁动五行族行"] = fam

    # 候裁预置行＝「预置固定行：」头起之行
    preset["候裁预置行"] = [l for _, ls in sections for l in ls if l.startswith("预置固定行：")]

    # 链衔接节体行＝节题含「链衔接」之节全部非空体行（七子弹＋尾标闭集自校行＝8 枚）；
    # 模板尾行剔除＝防与「模板尾行」目双计（具名枚举 12 枚集对齐口径）
    six: list[str] = []
    for t, ls in sections:
        if "链衔接" in t:
            six = [l for l in ls if l.strip() and not l.startswith("（模板尾")]
    preset["链衔接节体行"] = six

    # 模板尾行＝全角括号头「（模板尾」锚
    preset["模板尾行"] = [l for l in lines if l.startswith("（模板尾")]

    flat = [l for v in preset.values() for l in v]
    if not flat:
        raise InfraMiss("infra: 模板预置行集解析为空＝判据真源失联")

    # 尾标闭集七式＝体例行「尾标闭集（…」括注段按全角斜杠切分（末项尾随空格 strip 一行级口径）
    forms: list[str] = []
    for l in lines:
        m = re.search("尾标闭集（(.*?)）", l)
        if m:
            for seg in m.group(1).split("／"):
                # 段首 token 提取口径（末段含「照段别取用…」尾随叙述＝一行级切分口径）
                t = re.match(r"\s*(-[A-Z][A-Z-]*)", seg)
                if t:
                    forms.append(t.group(1))
            break
    if not forms:
        raise InfraMiss("infra: 尾标闭集解析为空＝判据真源失联")
    return sec_titles, preset, forms


# --- 面日期取法（黄-4 写死＝文件名日期前缀） ---

def face_date(lines: list[str], path: str) -> str | None:
    m = NAME_DATE_RE.match(os.path.basename(path))
    return m.group(1) if m else None


def in_scope(face_dt: str | None, since: str) -> bool:
    """面适用闸＝面日期 ≥ --since；无前缀名面在 V2 单面模式无法定日＝豁免照登（存量面默认不咬）。"""
    return face_dt is not None and face_dt >= since


# --- 面判据 CT-1／CT-2／CT-3／CT-4／CT-5／CT-8 ---

def ct1(sec_titles: list[str], lines: list[str], path: str) -> list[str]:
    findings: list[str] = []
    got = [l for l in lines if SEC_RE.match(l)]
    six_idx = max((i for i, l in enumerate(got) if "链衔接" in l), default=-1)
    for t in sec_titles:
        n = got.count(t)
        if n == 0:
            findings.append("%s:1: BLOCK check-ticket.CT-1 缺节题行：%s" % (path, t[:24]))
        elif n > 1:
            findings.append("%s:1: BLOCK check-ticket.CT-1 节题行重复 %d 枚：%s" % (path, n, t[:24]))
    seq = [sec_titles.index(g) for g in got if g in sec_titles]
    if seq != sorted(seq):
        findings.append("%s:1: BLOCK check-ticket.CT-1 节题次序逆序" % path)
    for i, l in enumerate(got):
        if l not in sec_titles and six_idx >= 0 and i < six_idx:
            findings.append("%s:%d: BLOCK check-ticket.CT-1 额外节题现于链衔接节之前：%s" % (path, i + 1, l[:24]))
    return findings


def ct2(preset: dict[str, list[str]], lines: list[str], path: str) -> list[str]:
    findings: list[str] = []
    face = set(lines)
    for name, rows in preset.items():
        for r in rows:
            if r not in face:
                findings.append("%s:1: BLOCK check-ticket.CT-2 预置行缺失（%s）：%s" % (path, name, r[:36]))
    return findings


def ct3(lines: list[str], path: str) -> list[str]:
    findings: list[str] = []
    bt = sum(l.count("`") for l in lines)
    at = sum(l.count("@") for l in lines)
    if bt:
        findings.append("%s:1: BLOCK check-ticket.CT-3 反引号计数 %d ≠ 0" % (path, bt))
    if at:
        findings.append("%s:1: BLOCK check-ticket.CT-3 at 计数 %d ≠ 0" % (path, at))
    for i, l in enumerate(lines, 1):
        if "/" in l and not l.startswith("    "):
            findings.append("%s:%d: BLOCK check-ticket.CT-3 非缩进段半斜杠" % (path, i))
    return findings


def ct4(lines: list[str], path: str) -> list[str]:
    findings: list[str] = []
    for n in range(7):
        head = "- V%d " % n
        cnt = sum(1 for l in lines if l.startswith(head))
        if cnt != 1:
            findings.append("%s:1: BLOCK check-ticket.CT-4 V%d 行起始计数 %d ≠ 1" % (path, n, cnt))
    return findings


def ct5(lines: list[str], path: str) -> list[str]:
    # 豁免面具名两形制头行（黄-3 随正）
    hits = [i + 1 for i, l in enumerate(lines)
            if SLOT_OPEN in l
            and not l.lstrip().startswith(("使用说明（固定）", "模板使用说明（固定）"))]
    return ["%s:%d: BLOCK check-ticket.CT-5 槽标残留 U+27EA" % (path, ln) for ln in hits]


def ct8(lines: list[str], path: str) -> list[str]:
    findings: list[str] = []
    for i, l in enumerate(lines, 1):
        if not CT8_STYLE_RE.search(l):
            continue
        if l[:1].isspace() or l.startswith("#") or l.lstrip().startswith("|"):
            continue  # 叙述面＝排缩进段／节题行／表行
        if any(k in l for k in CT8_CALIBER):
            continue
        findings.append("%s:%d: WATCH check-ticket.CT-8 派生数字无复算口径：%s" % (path, i, l.strip()[:36]))
    return findings


def run_face(path: str, since: str, ctx: tuple) -> list[str]:
    sec_titles, preset, _ = ctx
    lines = read_lines(path, "--target 面")
    findings = ct1(sec_titles, lines, path) + ct3(lines, path) + ct4(lines, path) + ct5(lines, path)
    fdt = face_date(lines, path)
    if in_scope(fdt, since):
        findings += ct2(preset, lines, path)
        findings += ct8(lines, path)
    return findings


# --- 链判据 CT-6／CT-7 ---

def check_trailer(last_line: str, forms: list[str]) -> str | None:
    """纯函数：message 末行 → None＝合规／否则违例归因串。"""
    if not last_line.strip():
        return "缺尾标（末行空）"
    m = TRAILER_TOK_RE.search(last_line.rstrip())
    if not m:
        return "缺尾标或尾标后粘文（末行不以大写连字符尾标收尾）"
    if m.group(0) not in forms:
        return "闭集外尾标 %s" % m.group(0)
    return None


def run_ct6(root: str, since: str, forms: list[str]) -> list[str]:
    """--since 起链上各笔（日期口径＝author date %aI 写死·黄-4）末行尾标核。"""
    try:
        proc = subprocess.run(
            ["git", "-C", root, "log", "--format=%h\x1f%aI\x1f%B\x1e"],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    except (OSError, subprocess.TimeoutExpired):
        raise InfraMiss("infra: git log 不可达＝链判据失联")
    if proc.returncode != 0:
        raise InfraMiss("infra: git log 失败：%s" % proc.stderr.strip()[:120])
    findings: list[str] = []
    for rec in proc.stdout.split("\x1e"):
        rec = rec.strip("\n")
        if not rec.strip():
            continue
        parts = rec.split("\x1f")
        if len(parts) < 3:
            continue
        sha, author_iso, msg = parts[0], parts[1], parts[2]
        if author_iso[:10] < since:
            continue  # 链笔日期闸＝author date 口径
        msg_lines = [l for l in msg.split("\n") if l.strip()]
        last = msg_lines[-1] if msg_lines else ""
        bad = check_trailer(last, forms)
        if bad:
            findings.append("%s:1: BLOCK check-ticket.CT-6 %s（链笔 %s·author %s）" % (sha, bad, sha, author_iso[:10]))
    return findings


def git_added_date(root: str, rel_path: str) -> str | None:
    try:
        proc = subprocess.run(
            ["git", "-C", root, "log", "--diff-filter=A", "--format=%aI", "-1", "--", rel_path],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None
    out = proc.stdout.strip().splitlines()
    return out[0][:10] if out else None


def run_ct7(root: str, ticket_dir: str, since: str) -> list[str]:
    """--ticket-dir 内面日期 ≥ --since 件名须 YYYY-MM-DD- 前缀；无前缀名回落 git 新增笔日期。"""
    if not os.path.isdir(ticket_dir):
        raise InfraMiss("infra: --ticket-dir 不存在：%s" % ticket_dir)
    findings: list[str] = []
    for name in sorted(os.listdir(ticket_dir)):
        p = os.path.join(ticket_dir, name)
        if not os.path.isfile(p):
            continue
        if NAME_DATE_RE.match(name):
            continue  # 前缀合规（面适用性由前缀日期自证·合规名零违例）
        fdt = git_added_date(root, os.path.relpath(p, root).replace(os.sep, "/"))
        if fdt is None:
            continue  # 新增日不可得＝豁免照登
        if fdt >= since:
            findings.append("%s:1: BLOCK check-ticket.CT-7 件名非日期前缀（新增日 %s ≥ --since）：%s" % (p, fdt, name[:48]))
    return findings


# --- --selftest 三态夹具（内存夹具零写盘零 git） ---

def build_pos_fixture(template_lines: list[str]) -> list[str]:
    """正样例夹具＝thin 盘面去槽标线（使用说明行两形制保留＝豁免面）＝全预置面。"""
    keep = []
    for l in template_lines:
        if SLOT_OPEN in l and not l.lstrip().startswith(("使用说明（固定）", "模板使用说明（固定）")):
            continue
        keep.append(l)
    return keep


def selftest(root: str, ctx: tuple, template_lines: list[str]) -> int:
    sec_titles, preset, forms = ctx
    results: list[tuple[str, bool]] = []
    pos = build_pos_fixture(template_lines)

    def face_findings(fx_lines: list[str], name: str) -> list[str]:
        f = ct1(sec_titles, fx_lines, name) + ct3(fx_lines, name) + ct4(fx_lines, name) + ct5(fx_lines, name)
        f += ct2(preset, fx_lines, name)  # 夹具面日期 2999 全入扫描域＝预置核必跑
        f += ct8(fx_lines, name)
        return f

    def has(ftype: str, fs: list[str]) -> bool:
        return any(ftype in x for x in fs)

    # 态一·正样例（全预置面）＝零发现
    f_pos = face_findings(pos, "2999-01-01-selftest-pos.md")
    results.append(("正样例夹具（全预置面）exit 0 期望＝零发现 实得 %d" % len(f_pos), not f_pos))

    # 态二·违例合成逐目归因
    fx = list(pos)
    fx = [l for l in fx if not SEC_RE.match(l) or "候裁单列" not in l]
    results.append(("缺节面→CT-1 归因", has("CT-1", face_findings(fx, "2999-01-01-syn-missing-sec.md"))))

    fx = [l for l in pos if not l.startswith("警示行")]
    results.append(("预置行缺失面→CT-2 归因", has("CT-2", face_findings(fx, "2999-01-01-syn-preset.md"))))

    fx = list(pos)
    fx[1] = fx[1] + "含反引号样本"
    fx.insert(2, "带`反引号叙述行")
    results.append(("反引号入线面→CT-3 归因", has("CT-3", face_findings(fx, "2999-01-01-syn-btick.md"))))

    fx = list(pos)
    fx.insert(2, "叙述段残留槽位⟪槽：未填⟫残留 5 枚")
    results.append(("槽残留面→CT-5 归因", has("CT-5", face_findings(fx, "2999-01-01-syn-slot.md"))))

    fx = [l for l in pos if not l.startswith("- V2 ")]
    results.append(("V骨架缺行面→CT-4 归因", has("CT-4", face_findings(fx, "2999-01-01-syn-v4.md"))))

    fx = list(pos)
    fx.insert(2, "本面合计 1234 枚无出处样本")
    results.append(("无口径数字叙述面→CT-8 WATCH 归因", has("CT-8", face_findings(fx, "2999-01-01-syn-ct8.md"))))

    # CT-6 三态纯函数归因（3bc1f5a5 型复刻＝尾标后粘文）
    results.append(("尾标后粘文（3bc1f5a5 型）→CT-6 归因",
                    check_trailer("正文若干 -QA-REV 后粘迁位随登长文", forms) is not None))
    results.append(("缺尾标→CT-6 归因", check_trailer("正文无尾标收尾", forms) is not None))
    results.append(("闭集外尾标→CT-6 归因", check_trailer("正文 -CLOSEOUT", forms) is not None))
    good = [check_trailer("正文 %s" % fm, forms) is None for fm in forms]
    results.append(("七式闭集全合规（动态解析 %d 枚）" % len(forms), all(good)))

    # CT-7 名核纯函数归因
    ok_name = bool(NAME_DATE_RE.match("2999-01-01-样例票.md"))
    bad_name = not NAME_DATE_RE.match("BAD-非日期名票.md")
    results.append(("CT-7 前缀正例＋非日期名反例", ok_name and bad_name))

    # 态三·缺件面＝exit 4 语义（InfraMiss 路径）
    got4 = False
    try:
        read_lines(os.path.join(root, ".selftest-nonexistent-face.md"), "缺件夹具")
    except InfraMiss:
        got4 = True
    results.append(("缺件面→exit 4 语义（InfraMiss 抛出）", got4))
    got4t = False
    try:
        parse_template(["not a template at all"])
    except InfraMiss:
        got4t = True
    results.append(("模板真源失联面→exit 4 语义（解析为空）", got4t))

    ok = all(p for _, p in results)
    for msg, p in results:
        print("selftest %s [%s]" % (msg, "PASS" if p else "FAIL"))
    print("selftest: %s 夹具 %d 枚 exit %d" % ("全绿" if ok else "对拍不符", len(results), 0 if ok else 1))
    return 0 if ok else 1


# --- 出口 ---

def main() -> int:
    parser = argparse.ArgumentParser(add_help=True, description="票面合规机械闸（判据真源＝thin 模板运行时解析）")
    parser.add_argument("--root", help="仓根（缺省自脚本位置向上溯至含 .git 之根）")
    parser.add_argument("--target", help="票面路径（单面模式＝CT-1 至 CT-5＋CT-8）")
    parser.add_argument("--ticket-dir", help="票面目录（缺省＝%s·目录模式跑 CT-6＋CT-7）" % DEFAULT_TICKET_DIR)
    parser.add_argument("--since", default=DEFAULT_SINCE, help="扫描域日期闸（缺省 %s＝J-5 定格）" % DEFAULT_SINCE)
    parser.add_argument("--template", help="thin 模板路径（缺省＝包内 thin 盘面现件）")
    parser.add_argument("--selftest", action="store_true", help="内置夹具三态干跑")
    args = parser.parse_args()

    if args.since and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.since):
        die("usage: --since 须为 YYYY-MM-DD：%s" % args.since, 2)

    root = find_root(args.root)
    template = args.template or os.path.join(root, DEFAULT_TEMPLATE)

    findings: list[str] = []
    try:
        template_lines = read_lines(template, "--template 判据真源")
        ctx = parse_template(template_lines)
        if args.selftest:
            return selftest(root, ctx, template_lines)
        if args.target:
            findings = run_face(args.target, args.since, ctx)
        else:
            _, _, forms = ctx
            tdir = args.ticket_dir or os.path.join(root, DEFAULT_TICKET_DIR)
            findings = run_ct6(root, args.since, forms) + run_ct7(root, tdir, args.since)
    except InfraMiss as e:
        print(str(e), file=sys.stderr)
        return 4

    for f in findings:
        print(f)
    n_block = sum(1 for f in findings if ": BLOCK " in f)
    n_watch = sum(1 for f in findings if ": WATCH " in f)
    print("check-ticket: BLOCK %d／WATCH %d exit %d" % (n_block, n_watch, 1 if findings else 0))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
