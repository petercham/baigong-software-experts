#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""preflight-ticket.py · 票面预检闸（PF·ITER-F 族·SWB-BG-07·新建壳非拼装纯壳非重写既有闸）

判据真源指向＝票面 .collab/architect/2026-11-21-ITER-F-工序链轻量化-预检闸与机检单席化-规则票-v1.md
    §三 F1 脚本规格缩进段（＝本头部注释逐目展开之 verbatim 规格真源）＋条款本体＝开发纪律卷 §十二目 1。

判据闭集六目：
    PF-a 复用臂＝subprocess 现跑 check-ticket --target 票面（真位＝agent-experts/baigong-software-
         team/skills/sop/scripts/check-ticket.py·exit 非零即转报）；
    PF-b 复用臂＝subprocess 现跑 check-pointers --target 票面（真位＝share/check-pointers.py·同上）；
    PF-1 落点存在性＝票面声明闭集行（行内含「F〈数〉＝」或「S〈数〉＝」引导之仓根相对路径 token
         ·一行多枚逐枚取·token 截到空白与全角标点界·体例形制＝全角斜杠→验证前归一半角斜杠）
         逐枚 os.path.isfile 判定；token 尾随括注具名「新建」者改判其父目录存在；落空即 BLOCK；
    PF-2 HEAD 对链顶＝票面表头区「| HEAD |」行所带 sha（短式八位或全式四十位取行内首枚）必为
         预检当轮链顶之可验证祖先（git merge-base --is-ancestor 判定＝起草窗与预检窗允许中间插笔＝
         非祖先即 BLOCK＝归因＝链面漂移或伪锚＝退回刷新）；
    PF-3 引用三式对钉＝票面全文扫「N 行／sha」配对 token（正则：数字＋行＋全角斜杠＋hex 8—40 位）
         逐枚 git cat-file -t 可解析＋blob 型现算行数（cat-file blob 管道行数＝wc -l 口径＝换行符计数）
         等于 N；不可解析或行数不合即 BLOCK（commit 型仅判可解析不判行数＝具名口径）；
    PF-4 判据行可解析＝票面「- V0 」至「- V6 」行起始各恰一＋每条 V 目判据达意＝二者其一即成立＝
         ①该 V 目行自身含可执行命令行，或②该 V 目行之后紧随缩进段内含可执行命令行或槽填具名句
         至少一行（至下一 V 目行前）；V 目无附加行不构违例＝BLOCK 只判两形制皆无（宽读口径＝
         票面 rev-1 勘正三覆盖句写死）；前半句「V0 至 V6 行起始各恰一」沿守（＝CT-4 同判据）。
    落位闸＝票面文件名日期前缀 ≥ 条款生效日（EFFECTIVE＝放行落链当日具名）方可要求本闸在场＝
         生效日前的存量票面退回缺省不咬（存量全豁免防炸基线＝沿 check-ticket --since J-5 采甲同制）。

入参闭集＝--root／--target／--selftest（--check-ticket／--check-pointers 仅夹具面 override 用＝
    交付面缺省取真位具名）。
退出码闭集沿 share 族＝0 无违例／1 有 BLOCK／2 用法错／4 fail-closed＝票面件不存在或复用闸件失联。
输出形制沿 FINDING_RE 兼容一行一封 file:line: SEV spec msg＋末行计数汇总行。
本件只读零写＝脚本体禁任何写文件动作；--selftest 内存夹具三态干跑（正样例／违例合成／缺件面＝
    PF-1／PF-2／PF-3／PF-4 四目本体＋落位闸内存干跑＝零写盘零 git 写；PF-a／PF-b 复用臂为
    subprocess 薄壳＝经 --target 正臂窗实证）。

selftest 正样例约束（票面 rev-1 勘正三施工随动约束具名写死）＝正样例夹具必覆盖 PF-4 两种形制＝
    带紧随缩进段形制＋无附加行形制。
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

EFFECTIVE = "2026-11-21"  # 条款生效日＝本票放行落链当日（票面 §五④口径＝随放行尾段要素登记）
CHECK_TICKET_REAL = "agent-experts/baigong-software-team/skills/sop/scripts/check-ticket.py"
CHECK_POINTERS_REAL = "share/check-pointers.py"

NAME_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-")
DECL_LINE_RE = re.compile(r"[FS]\d+＝")
SHA8_RE = re.compile(r"[0-9a-fA-F]{8}(?:[0-9a-fA-F]{32})?(?![0-9a-fA-F])")
PAIR_RE = re.compile(r"(\d+)\s*行／([0-9a-fA-F]{8,40})(?![0-9a-fA-F])")
V_HEAD_RE = re.compile(r"^- V[0-6] ")
SLOT_OPEN = "\u27ea"
FULL_SLASH = "／"
TOKEN_STOP = set(" \t；。，、（）「」『』《》【】〈〉｛｝：；！？·＝｜\"'")
CMD_RE = re.compile(
    r"^(?:git|python3?|grep|egrep|ls|wc|cat|sed|awk|find|head|tail|date|od|diff|uniq|sort|cut|tr|"
    r"touch|mkdir|cp|mv|rm|tree|md5sum|sha1sum|pip[3]?|npm|npx|node)\b"
)
CMD_ANY_RE = re.compile(
    r"(?:^|[\s（(＝=；;，,、])(?:git|python3?|grep|egrep|ls|wc|cat|sed|awk|find|head|tail|"
    r"date|od|diff|uniq|sort|cut|tr|touch|mkdir|cp|mv|rm|tree|md5sum|sha1sum|pip[3]?|npm|npx|node)\b"
)


class InfraMiss(Exception):
    pass


def die(msg: str, code: int) -> None:
    print(msg, file=sys.stderr)
    sys.exit(code)


def find_root(explicit: str | None) -> str:
    """--root 缺省＝自脚本位置向上溯至含 .git 之根（沿 share 族一行级口径）。"""
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
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read().replace("\r\n", "\n").split("\n")
    except OSError:
        raise InfraMiss("infra: 件不存在或不可读（%s）：%s" % (why, path))


def blob_line_count(root: str, sha: str) -> int:
    proc = subprocess.run(["git", "-C", root, "cat-file", "blob", sha], capture_output=True)
    return proc.stdout.count(b"\n")


def pf1(lines: list[str], root: str, path: str) -> list[str]:
    """PF-1 落点存在性＝声明闭集行 token 逐枚 isfile／「新建」括注改判父目录 isdir。"""
    findings: list[str] = []
    for i, l in enumerate(lines, 1):
        if not DECL_LINE_RE.search(l):
            continue
        for m in DECL_LINE_RE.finditer(l):
            rest = l[m.end():]
            tok_chars: list[str] = []
            for ch in rest:
                if ch in TOKEN_STOP:
                    break
                tok_chars.append(ch)
            token = "".join(tok_chars)
            if not token:
                continue
            token = token.replace(FULL_SLASH, "/")
            tail = rest[len("".join(tok_chars)):][:6]  # 「尾随括注」窗口＝紧跟 token 的括注段
            if "新建" in tail:
                target = os.path.dirname(os.path.join(root, token)) or root
                if not os.path.isdir(target):
                    findings.append("%s:%d: BLOCK preflight.PF-1 落空（新建改判父目录）：%s"
                                    % (path, i, token[:64]))
            else:
                if not os.path.isfile(os.path.join(root, token)):
                    findings.append("%s:%d: BLOCK preflight.PF-1 落空：%s" % (path, i, token[:64]))
    return findings


def pf2(lines: list[str], root: str, path: str) -> list[str]:
    """PF-2 HEAD 对链顶＝表头区「| HEAD |」行行内首枚 sha 必为当轮链顶可验证祖先。"""
    head_row = None
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith("| HEAD |"):
            head_row = (i, l)
            break
    if head_row is None:
        return ["%s:1: BLOCK preflight.PF-2 表头区无「| HEAD |」行＝锚缺位" % path]
    i, l = head_row
    m = SHA8_RE.search(l)
    if not m:
        return ["%s:%d: BLOCK preflight.PF-2 HEAD 行无 sha token（短式八位或全式四十位）" % (path, i)]
    sha = m.group(0)
    proc = subprocess.run(["git", "-C", root, "merge-base", "--is-ancestor", sha, "HEAD"],
                          capture_output=True)
    if proc.returncode != 0:
        return ["%s:%d: BLOCK preflight.PF-2 非祖先（链面漂移或伪锚＝退回刷新）：%s" % (path, i, sha)]
    return []


def pf3(lines: list[str], root: str, path: str) -> list[str]:
    """PF-3 引用三式对钉＝「N 行／sha」配对 token 逐枚 cat-file 可解析＋blob 型行数对拍。"""
    findings: list[str] = []
    for i, l in enumerate(lines, 1):
        for m in PAIR_RE.finditer(l):
            n = int(m.group(1))
            sha = m.group(2)
            t = subprocess.run(["git", "-C", root, "cat-file", "-t", sha], capture_output=True)
            typ = t.stdout.decode("ascii", "replace").strip()
            if not typ:
                findings.append("%s:%d: BLOCK preflight.PF-3 不可解析：%s" % (path, i, sha))
                continue
            if typ == "blob":
                got = blob_line_count(root, sha)
                if got != n:
                    findings.append("%s:%d: BLOCK preflight.PF-3 行数不合（声称 %d 现算 %d）：%s"
                                    % (path, i, n, got, sha))
            # commit 型＝仅判可解析不判行数（具名口径）
    return findings


def _cmd_like(stripped: str) -> bool:
    return bool(CMD_RE.match(stripped)) or SLOT_OPEN in stripped


def _cmd_like_body(stripped: str) -> bool:
    """形制①判据面＝V 目行自身任意位置含命令行（票 F 勘正三①文本兑现）。"""
    return bool(CMD_ANY_RE.search(stripped)) or SLOT_OPEN in stripped


def pf4(lines: list[str], path: str) -> list[str]:
    """PF-4 判据行可解析＝V0—V6 行起始各恰一＋各 V 目宽读达意（勘正三两形制写死）。

    附加行窗口＝V 目行后至下一 V 目前之缩进延续行段（跳空行·遇非缩进非空行即界止＝
    下一节题／边界行不入目附加行）；无附加行不构违例＝BLOCK 只判「有附加行且其中
    既无可执行命令行亦无槽填具名句」两形制皆无。
    """
    findings: list[str] = []
    idx = [i for i, l in enumerate(lines) if V_HEAD_RE.match(l)]
    for n in range(7):
        head = "- V%d " % n
        cnt = sum(1 for l in lines if l.startswith(head))
        if cnt != 1:
            findings.append("%s:1: BLOCK preflight.PF-4 V%d 行起始计数 %d ≠ 1" % (path, n, cnt))
    for k, i in enumerate(idx):
        if _cmd_like_body(lines[i].strip()):
            continue  # 形制①＝V 目行自身含可执行命令行
        nxt = idx[k + 1] if k + 1 < len(idx) else len(lines)
        body: list[str] = []
        j = i + 1
        while j < nxt:
            b = lines[j]
            if not b.strip():
                j += 1
                continue
            if b.startswith(" "):
                body.append(b)
                j += 1
            else:
                break  # 非缩进非空行＝目块界止（节题／边界行不入附加行）
        if not body:
            continue  # 无附加行形制不构违例（勘正三写死）
        if any(b.startswith("    ") and _cmd_like(b.strip()) for b in body):
            continue  # 形制②＝紧随缩进段内含命令行或槽填具名句
        findings.append("%s:%d: BLOCK preflight.PF-4 V 目两形制皆无（有附加行而段内无命令行/槽填句）：%s"
                        % (path, i + 1, lines[i].strip()[:40]))
    return findings


def run_reuse(script: str, target: str, root: str, label: str) -> list[str]:
    """PF-a／PF-b 复用臂＝subprocess 现跑既有闸 --target 单面模式＝exit 非零即转报。"""
    sp = os.path.join(root, script)
    if not os.path.isfile(sp):
        raise InfraMiss("infra: 复用闸件失联：%s" % sp)
    proc = subprocess.run([sys.executable, sp, "--target", target],
                          capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        out = [ln for ln in (proc.stdout + proc.stderr).splitlines() if ln.strip()]
        return (["%s:1: BLOCK preflight.%s 复用臂转报（exit %d 转发 %d 行）"
                 % (target, label, proc.returncode, len(out))] + out[:20])
    return []


def run_target(target: str, root: str, ct: str, cp: str) -> int:
    if not os.path.isfile(target):
        die("infra: 票面件不存在＝fail-closed：%s" % target, 4)
    face_name = os.path.basename(target)
    m = NAME_DATE_RE.match(face_name)
    face_date = m.group(1) if m else None
    if face_date is not None and face_date < EFFECTIVE:
        print("%s:1: NOTE preflight.PF 落位闸不咬（面日期 %s < 生效日 %s＝存量退回缺省）"
              % (target, face_date, EFFECTIVE))
        print("preflight: BLOCK 0／WATCH 0 exit 0")
        return 0
    lines = read_lines(target, "--target 面")
    findings: list[str] = []
    findings += run_reuse(ct, target, root, "PF-a")
    findings += run_reuse(cp, target, root, "PF-b")
    findings += pf1(lines, root, target)
    findings += pf2(lines, root, target)
    findings += pf3(lines, root, target)
    findings += pf4(lines, target)
    for ln in findings:
        print(ln)
    print("preflight: BLOCK %d／WATCH 0 exit %d" % (len(findings), 1 if findings else 0))
    return 1 if findings else 0


# --- --selftest 三态夹具（内存夹具零写盘零 git 写） ---

def _fixture_blob(root: str) -> tuple[str, int]:
    """PF-3 正样例钉值现取＝HEAD 面 blob（链上对象必可解析·零 git 写）。"""
    proc = subprocess.run(["git", "-C", root, "rev-parse", "HEAD:" + CHECK_POINTERS_REAL],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise InfraMiss("infra: 夹具 blob 锚取不到（链上对象失联）")
    sha = proc.stdout.strip()
    return sha, blob_line_count(root, sha)


def _head_sha(root: str) -> str:
    return subprocess.run(["git", "-C", root, "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


def selftest(root: str) -> int:
    results: list[tuple[str, bool]] = []

    def check(name: str, cond: bool) -> None:
        results.append((name, cond))

    blob_sha, blob_n = _fixture_blob(root)
    head = _head_sha(root)

    # 正样例＝PF-4 两形制必覆（勘正三约束）＝带紧随缩进段形制（V1）＋无附加行形制（V0）
    good = [
        "| HEAD | git rev-parse --short HEAD | %s＝链顶现读 |" % head[:8],
        "- 写集路径清单：F1＝share／preflight-ticket.py（新建）；F2＝share／check-pointers.py",
        "- 引用对钉＝check-pointers 现态 %d 行／%s" % (blob_n, blob_sha),
        "- V0 开工读数＝当轮现跑 HEAD＋链序照登。",
        "- V1 靶面钉值零漂移＝对钉集复跑对拍。",
        "    git hash-object share/check-pointers.py",
        "- V2 施工动作＝关键句臂（命令与期望由槽填）：",
        "    \u27ea槽：grep -c 锚句命令＋期望⟫",
        "- V3 落盘坐实＝面单核验。",
        "- V4 自靶 exit 0＝落笔前现跑＝",
        "    python share/preflight-ticket.py --target fixture.md",
        "- V5 面单互证＝缺省扫描两臂现跑只平。",
        "- V6 升档停手闸＝入线四词逐词命中读数登记。",
    ]
    check("正样例 PF-1 全落点（新建改判父目录＋实存件）＝零违例", not pf1(good, root, "fx"))
    check("正样例 PF-2 链顶对链顶＝零违例", not pf2(good, root, "fx"))
    check("正样例 PF-3 现取钉值对拍＝零违例", not pf3(good, root, "fx"))
    check("正样例 PF-4 两形制（缩进段 V1＋无附加行 V0）＝零违例", not pf4(good, "fx"))

    # 违例合成＝PF-1 假落点
    bad1 = list(good)
    bad1[1] = "- 写集路径清单：F1＝share／no-such-fixture-file.py"
    f = pf1(bad1, root, "fx")
    check("违例合成 PF-1 假落点＝恰一臂归因 PF-1", len(f) == 1 and "PF-1" in f[0])

    # 违例合成＝PF-2 伪锚（零哈希＝必非祖先）
    bad2 = list(good)
    bad2[0] = "| HEAD | git rev-parse --short HEAD | 00000000＝伪锚夹具 |"
    f = pf2(bad2, root, "fx")
    check("违例合成 PF-2 伪锚＝恰一臂归因 PF-2", len(f) == 1 and "PF-2" in f[0])

    # 违例合成＝PF-3 假钉（可解析 blob＋行数不合）
    bad3 = list(good)
    bad3[2] = "- 引用对钉＝check-pointers 现态 %d 行／%s" % (blob_n + 7, blob_sha)
    f = pf3(bad3, root, "fx")
    check("违例合成 PF-3 假钉行数不合＝恰一臂归因 PF-3", len(f) == 1 and "PF-3" in f[0])

    # 违例合成＝PF-3 不可解析
    bad3b = list(good)
    bad3b[2] = "- 引用对钉＝不存在对象 99999999 夹具 3 行／9999999999999999999999999999999999999999"
    f = pf3(bad3b, root, "fx")
    check("违例合成 PF-3 不可解析＝一臂归因 PF-3", len(f) >= 1 and "PF-3" in f[0])

    # 违例合成＝PF-4 两形制皆无（V3 附加行＝缩进段内叙述行＝非命令行非槽填句）
    bad4 = list(good)
    i3 = bad4.index("- V3 落盘坐实＝面单核验。")
    bad4.insert(i3 + 1, "    叙述性缩进附加行无命令无槽标＝违例夹具")
    f = pf4(bad4, "fx")
    check("违例合成 PF-4 两形制皆无＝恰一臂归因 PF-4", len(f) == 1 and "PF-4" in f[0])

    # 违例合成＝PF-4 V 目缺失
    bad4b = [l for l in good if not l.startswith("- V6 ")]
    f = pf4(bad4b, "fx")
    check("违例合成 PF-4 V6 缺失＝恰一臂归因 PF-4", len(f) == 1 and "PF-4" in f[0])

    # 缺件面＝落位闸＝生效日前存量面退回缺省（内存判＝面日期 < EFFECTIVE 分支）
    old_face = "2026-11-19-old-face-not-checked.md"
    m = NAME_DATE_RE.match(old_face)
    check("落位闸＝生效日前存量面不咬（内存干跑）", m is not None and m.group(1) < EFFECTIVE)

    # ①形改正例夹具＝good 面 V3 行改自身行中嵌「git show --name-only」字样（非行首位）
    # ＋该 V3 行紧随四空格缩进纯叙述附加行＝pf4 期望零违例（放宽前判 BLOCK 案型转正＝①支可达实证）
    good1 = list(good)
    i3g = good1.index("- V3 落盘坐实＝面单核验。")
    good1[i3g] = "- V3 落盘坐实＝面单核验（投递笔现跑 git show --name-only 面单枚数对等）。"
    good1.insert(i3g + 1, "    纯叙述附加行无命令无槽标＝形制①转正夹具")
    check("①形改正例＝V 目行自身行中嵌命令行＋缩进纯叙述附加行＝零违例", not pf4(good1, "fx"))

    # ①形制负例夹具＝good 面 V3 行原样（无命令）＋紧随四空格缩进纯叙述附加行＝pf4 期望恰一臂
    # 归因 PF-4（放宽不过宽防回归锚＝命令词族外文本不得经①支放行）
    bad4c = list(good)
    i3b = bad4c.index("- V3 落盘坐实＝面单核验。")
    bad4c.insert(i3b + 1, "    纯叙述附加行无命令无槽标＝形制①防过宽夹具")
    f = pf4(bad4c, "fx")
    check("①形制负例＝V 目行无命令＋缩进纯叙述附加行＝恰一臂归因 PF-4", len(f) == 1 and "PF-4" in f[0])

    ok = all(c for _, c in results)
    for name, c in results:
        print("selftest %s [%s]" % (name, "PASS" if c else "FAIL"))
    print("selftest: %s 夹具 %d 枚 exit %d" % ("全绿" if ok else "对拍不符", len(results), 0 if ok else 1))
    return 0 if ok else 1


def main(argv: "list[str]") -> int:
    parser = argparse.ArgumentParser(add_help=True, description="PF 票面预检闸（ITER-F 族）")
    parser.add_argument("--root", help="仓根（缺省自脚本位置向上溯至含 .git 之根）")
    parser.add_argument("--target", help="票面路径（单面模式＝PF-a/b＋PF-1 至 PF-4）")
    parser.add_argument("--selftest", action="store_true", help="内存夹具三态干跑（零写盘零 git 写）")
    parser.add_argument("--check-ticket", default=None, help="夹具面 override 复用闸路径（缺省真位具名）")
    parser.add_argument("--check-pointers", default=None, help="夹具面 override 复用闸路径（缺省真位具名）")
    args = parser.parse_args(argv)
    root = find_root(args.root)
    ct = args.check_ticket or CHECK_TICKET_REAL
    cp = args.check_pointers or CHECK_POINTERS_REAL
    if args.selftest:
        try:
            return selftest(root)
        except InfraMiss as e:
            die(str(e), 4)
    if args.target:
        try:
            return run_target(args.target, root, ct, cp)
        except InfraMiss as e:
            die(str(e), 4)
    die("usage: 需 --target 或 --selftest（本闸无缺省扫描模式）", 2)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
