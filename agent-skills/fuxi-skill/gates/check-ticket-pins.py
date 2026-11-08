#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""票面钉值单一真源机检（钉值表-票内真源-基线盘 三载体对面）.

公式（票面钉死·本件＝唯一实现位；票面与代码不一致＝以票面 fenced 为准
并回执申报差异＝D-83 教训口径）：
    V1* = B + A - D 且 V0* = B
      B＝基线盘目标文件含钉语行数（基线无该文件⇒0）
      A＝本票归属该目标文件的 fenced 正文行中含钉语行数
      D＝基线盘目标文件「被替换旧行号」位上含钉语行数
输入体例（出处＝票面 §二 钉值块约定·本件为其唯一实现面）：
  钉块＝```pins 围栏；行形态六字段竖线分隔：
      PIN|<目标仓根相对路径>|<钉语>|<基线钉值>|<收口钉值>|<被替换旧行号>
      旧行号段＝"-"（无替换行）或逗号/分号分隔十进制行号（对基线盘）。
  归属＝围栏块前最近施工项目题行（行首 **S<数字> … <含斜杠仓根相对路径>…**）
      的路径段；项目题路径段必含斜杠（缺＝解析不到归属＝fail-closed）。

用法：
    python check-ticket-pins.py --ticket <票面相对路径> [--root <仓根>] [--base <sha>] [--selftest]
    --base 缺省＝调用当轮 HEAD（回执必录实际 base sha＝复现锚）。
    selftest＝临时 git 仓合成五例（两案型重演必咬＋三合规零咬）与内嵌预期对拍。

退出码（闭集·60-gates.md §六同制）：
    0 通过（全钉行与公式应值全等；或 --selftest 对拍全等）
    1 违例（≥1 钉值≠公式应值；或 selftest 对拍不符）
    2 用法错
    4 基础设施错（票面缺件／机器可读钉块缺位／围栏未闭合／孤儿闭围栏／
      围栏无归属项目题／钉行字段不可解析／旧行号段形态非法／旧行号越界）
本件只读：不写任何文件（读数入调用方回执）。不挂任何常驻门禁清单。
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

FENCE_OPEN_RE = re.compile(r"^```([A-Za-z0-9_+-]*)[ \t]*$")
FENCE_END_RE = re.compile(r"^```[ \t]*$")
S_HEAD_RE = re.compile(
    r"^\*\*S\d+[^\n]*?([A-Za-z0-9._-]+(?:/[A-Za-z0-9._-]+)+\.(?:md|py))")
LINE_SET_RE = re.compile(r"^(?:-|[0-9][0-9,;]*)$")

# selftest 用例设计（票面 §二 规格钉死）：
#   case1_first_seen_bite：首见案型重演（表钉 1 vs 公式应值 2）⇒ 违例 1
#   case2_second_seen_bite：二见案型重演（旧行含钉语 D=1·真源复入 A=1·
#     表钉 0 vs 应值 1）⇒ 违例 1
#   case3_conformant_ok：合规全等（V0=B·V1=B+A-D）⇒ 违例 0
#   case4_old_zero_ok：旧值零残留成文式（B=1·A=0·D=1⇒应值 0）⇒ 违例 0
#   case5_new_one_ok：新值入位式（B=0·A=1·D=0⇒应值 1）⇒ 违例 0
# （fixture 内样例日期一律非 20xx 形态＝实体扫描卫生口径·票面 §〇-10）
SELFTEST_EXPECTED = {
    "case1_first_seen_bite": 1,
    "case2_second_seen_bite": 1,
    "case3_conformant_ok": 0,
    "case4_old_zero_ok": 0,
    "case5_new_one_ok": 0,
}


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
        if os.path.isdir(os.path.join(cur, "tools")) and any(
                os.path.isdir(os.path.join(cur, c))
                for c in ("agent-experts", "agent-skills", "softwares")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            die_usage("未能定位仓根；请用 --root 指定")
        cur = parent


def read_text(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", newline="") as handle:
            return handle.read().replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError) as exc:
        die_infra("读取失败 %s: %s" % (path, exc))
        return ""


def split_fences(lines: "list[str]") -> "list[tuple[str, list[str], int]]":
    """围栏切块（fail-closed：未闭合围栏／孤儿闭围栏＝基础设施错）。"""
    blocks: "list[tuple[str, list[str], int]]" = []
    i = 0
    n = len(lines)
    while i < n:
        m = FENCE_OPEN_RE.match(lines[i])
        if m and not FENCE_END_RE.match(lines[i]):
            lang = m.group(1)
            j = i + 1
            body: "list[str]" = []
            while j < n and not FENCE_END_RE.match(lines[j]):
                body.append(lines[j])
                j += 1
            if j >= n:
                die_infra("围栏未闭合（行 %d·lang=%s）" % (i + 1, lang))
            blocks.append((lang, body, i))
            i = j + 1
            continue
        if FENCE_END_RE.match(lines[i]):
            die_infra("孤儿闭围栏（行 %d）" % (i + 1))
        i += 1
    return blocks


def nearest_target(lines: "list[str]", open_idx: int) -> "str | None":
    """块归属＝块前最近施工项目题的路径段（无＝None）。"""
    for j in range(open_idx - 1, -1, -1):
        m = S_HEAD_RE.match(lines[j])
        if m:
            return m.group(1)
    return None


def git_show(root: str, base: str, rel: str) -> "str | None":
    proc = subprocess.run(["git", "-C", root, "show", "%s:%s" % (base, rel)],
                          capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0:
        return None
    return proc.stdout.replace("\r\n", "\n")


def check_ticket(root: str, ticket_rel: str, base: str) -> "tuple[list[str], int]":
    """单票对面，返回 (违例行, 钉行数)。缺机器可读钉块＝基础设施错（不算绿）。"""
    ticket_path = os.path.join(root, ticket_rel.replace("/", os.sep))
    if not os.path.isfile(ticket_path):
        die_infra("--ticket 指向不存在的文件：%s" % ticket_rel)
    lines = read_text(ticket_path).split("\n")
    source_lines: "dict[str, list[str]]" = {}
    pins_rows: "list[tuple[str, str, int, int, str]]" = []
    for lang, body, open_idx in split_fences(lines):
        target = nearest_target(lines, open_idx)
        if target is None:
            die_infra("围栏无归属施工项目题（行 %d·lang=%s）" % (open_idx + 1, lang))
        if lang == "pins":
            for raw in body:
                if not raw.strip():
                    continue
                fields = raw.split("|")
                if len(fields) != 6 or fields[0] != "PIN":
                    die_infra("钉行不可解析（六字段·竖线分隔·首字段 PIN）：%r" % raw)
                lset = fields[5].strip()
                if not LINE_SET_RE.match(lset):
                    die_infra("旧行号段形态非法：%r" % lset)
                try:
                    v0 = int(fields[3])
                    v1 = int(fields[4])
                except ValueError:
                    die_infra("钉值字段非整数：%r" % raw)
                pins_rows.append((fields[1].strip(), fields[2], v0, v1, lset))
        else:
            source_lines.setdefault(target, []).extend(body)
    if not pins_rows:
        die_infra("票面无机器可读钉块（缺位＝不算绿）")
    fails: "list[str]" = []
    for (f, x, v0, v1, lset) in pins_rows:
        base_text = git_show(root, base, f)
        base_lines = base_text.split("\n") if base_text is not None else []
        b = sum(1 for ln in base_lines if x in ln)
        a = sum(1 for ln in source_lines.get(f, []) if x in ln)
        d = 0
        if lset != "-":
            if base_text is None:
                die_infra("基线无 %s 却声明被替换旧行号（%s）" % (f, lset))
            for tok in [t for t in re.split(r"[,;]", lset) if t]:
                lineno = int(tok)
                if lineno < 1 or lineno > len(base_lines):
                    die_infra("旧行号越界 %s L%d（基线行数 %d）"
                              % (f, lineno, len(base_lines)))
                if x in base_lines[lineno - 1]:
                    d += 1
        v1_star = b + a - d
        if v0 != b or v1 != v1_star:
            fails.append("钉违例 %s｜钉语=%s｜表值 %d/%d｜公式应值 %d/%d"
                         "（B=%d A=%d D=%d）｜旧行=%s"
                         % (f, x, v0, v1, b, v1_star, b, a, d, lset))
    return fails, len(pins_rows)


def selftest() -> int:
    tmp = tempfile.mkdtemp(prefix="ctp-selftest-")
    try:
        def case(name: str, base_file: "str | None", base_lines: "list[str]",
                 fenced: "list[str]", pin: str) -> int:
            repo = os.path.join(tmp, "repo-" + name)
            os.makedirs(repo)
            git = ["git", "-C", repo]
            subprocess.run(git + ["init", "-q"], check=True, capture_output=True)
            subprocess.run(git + ["config", "user.email", "selftest@local"],
                           check=True, capture_output=True)
            subprocess.run(git + ["config", "user.name", "selftest"],
                           check=True, capture_output=True)
            if base_file is not None:
                full = os.path.join(repo, base_file.replace("/", os.sep))
                os.makedirs(os.path.dirname(full), exist_ok=True)
                with open(full, "w", encoding="utf-8") as handle:
                    handle.write("\n".join(base_lines) + "\n")
            subprocess.run(git + ["add", "-A"], check=True, capture_output=True)
            subprocess.run(git + ["commit", "-q", "-m", "synthetic " + name],
                           check=True, capture_output=True)
            head = subprocess.run(git + ["rev-parse", "HEAD"],
                                  capture_output=True, text=True).stdout.strip()
            os.makedirs(os.path.join(repo, ".scratch", "tickets"), exist_ok=True)
            target = base_file if base_file is not None else "deliverables/nf.py"
            ticket = ["# synthetic %s" % name,
                      "**S1 . %s 整行替换（合成目题）**" % target,
                      "```text"]
            ticket.extend(fenced)
            ticket.extend(["```", "```pins", pin, "```"])
            with open(os.path.join(repo, ".scratch", "tickets", name + ".md"),
                      "w", encoding="utf-8") as handle:
                handle.write("\n".join(ticket) + "\n")
            fails, _n = check_ticket(repo, ".scratch/tickets/%s.md" % name, head)
            return len(fails)

        results = {
            "case1_first_seen_bite": case(
                "case1", "pkg/registration.md",
                ["# reg", "| 配平 | 旧行 |", "- 新鲜度窗口读数（旧措辞）"],
                ["| 配平 | 一手占比已过门槛（按参考评分条款不入该轴） |",
                 "- 新鲜度窗口读数（参考评分口径·非门槛）：窗内=`7`/`25`"],
                "PIN|pkg/registration.md|参考评分|0|1|2,3"),
            "case2_second_seen_bite": case(
                "case2", "products/README.md",
                ["# products", "- 当期读数 0（属空池平凡真态）", "- 三态注：旧行"],
                ["- 当期读数 **0**——此 0 已非空池平凡真态＝产物级实证",
                 "- 三态注：规程级／产物级实证（已达成态）"],
                "PIN|products/README.md|空池平凡真|1|0|2"),
            "case3_conformant_ok": case(
                "case3", "deliverables/f.md", ["# F", "- 无关行一"],
                ["- 新行含新措辞甲"],
                "PIN|deliverables/f.md|新措辞甲|0|1|2"),
            "case4_old_zero_ok": case(
                "case4", "pkg/SKILL.md", ["- `复审到期日`=`1999-01-05`"],
                ["- `复审到期日`=`1999-04-04`"],
                "PIN|pkg/SKILL.md|1999-01-05|1|0|1"),
            "case5_new_one_ok": case(
                "case5", "pkg/SKILL.md", ["- `复审到期日`=`1999-01-05`"],
                ["- `复审到期日`=`1999-04-04`"],
                "PIN|pkg/SKILL.md|1999-04-04|0|1|1"),
        }
        ok = True
        bad = 0
        for name in sorted(SELFTEST_EXPECTED):
            got = results[name]
            want = SELFTEST_EXPECTED[name]
            mark = "OK" if got == want else "MISMATCH"
            if got != want:
                ok = False
                bad += 1
            print("selftest-ticket-pins %s：读数 %d／预期 %d [%s]"
                  % (name, got, want, mark))
        print("selftest-ticket-pins: 用例 %d／反常 %d" % (len(SELFTEST_EXPECTED), bad))
        return 0 if ok else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv: "list[str]") -> int:
    parser = argparse.ArgumentParser(description="票面钉值单一真源机检")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    parser.add_argument("--ticket", help="票面路径（相对仓根·单票）")
    parser.add_argument("--base", help="基线 commit（缺省＝当轮 HEAD）")
    parser.add_argument("--selftest", action="store_true",
                        help="临时仓合成五例对拍（两案型必咬＋三合规零咬）")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.ticket:
        die_usage("非 selftest 模式必须给 --ticket")
    root = find_root(args.root)
    base = args.base
    if not base:
        proc = subprocess.run(["git", "-C", root, "rev-parse", "HEAD"],
                              capture_output=True, text=True)
        if proc.returncode != 0:
            die_infra("git 不可用且未给 --base（fail-closed）")
        base = proc.stdout.strip()
    fails, n_pins = check_ticket(root, args.ticket, base)
    for line in fails:
        print(line)
    print("check-ticket-pins: 票 %s（base %s）钉行 %d｜违例 %d｜exit %d"
          % (args.ticket, base[:8], n_pins, len(fails), 1 if fails else 0))
    return 1 if fails else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按 4，不得吞成 0
        sys.stderr.write("infra error: %s\n" % exc)
        raise SystemExit(4)

