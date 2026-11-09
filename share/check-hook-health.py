#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: MC-GATE-2
# spec_file: agent-skills/multi-collab/references/60-gates.md
# spec_anchor: - **门禁脚本只读**
# spec_clause_sha256: 64e5d90d4b01dab23f6039122e06d95741030551666d9a0c2c723f17666c2def
# spec_version: 3.9
# spec_effective: 2026-10-23
# provider: multi-collab
# --- /spec-provenance ---
"""门禁载体层健康哨兵（FX-U34／D-102：闸挂钩子而钩子健康无机械哨兵＝fail-open 面无哨兵）。

三查一快照（全部只读零写盘＝MC-GATE-2 口径）：
  查一＝core.hooksPath 任意 scope 出现读数即异常报出（键在盘＝缺省钩子整体失效＝
        D-102 机理＝误序读取意图写键即静默解除全仓钩子）；
  查二＝期望钩子文件在盘；可执行位仅 POSIX 平台判（Windows 权限位不具区分力＝
        读数登记不判，承 install-hooks.sh「不依赖可执行位」口径）；
  查三＝钩子内容健康＝安装器标记行 MARKER 在场＋调用行含两枚在册门禁实体后缀＋
        钩子 blob 对钉期望常量全等；
  快照＝hooksPath 现值逐读数（带 origin）＋钩子 blob sha＋mode 读数，每次必出＝
        0ac1d08 类污染窗口的未来即时可见面（不再需要事后逐笔伴随戳对钉追证）。

发现行形态＝run-gates.sh FINDING_RE 一行一封；SEV＝BLOCK（fail-closed 承提交闸
升硬拦同向＝起草席定形，BLOCK/WARN 候裁呈放行批）。快照行不匹配 FINDING_RE＝
非发现（真盘健康时门禁零 BLOCK 族新增）。spec_id 不入路由表 per_spec＝按
on_severity 默认路由（BLOCK→block），免触 60-gates.md 零扩张。

退出码（闭集·60-gates.md §六同制）：
  0 健康（三查全过）  1 有发现（任一查失配＝BLOCK 发现入路由）
  2 用法错  4 基础设施错（git config 读数命令异常退出＝不得降级为不查）
本件只读：不写任何文件（读数入 stdout 与出口②证据件）。
"""

from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import sys

SEV_BLOCK = "BLOCK"
SPEC_ID = "FX-HOOK-1"
MARKER = "generated-by: object-audit/scripts/install-hooks.sh"
EXPECTED_CALL_TARGETS = ("share/check-staged-declaration.py", "share/run-gates.sh")
EXPECTED_HOOK_BLOB = "8b7857701594264421832edd30dae7e401f85719"


def die_usage(msg: str) -> None:
    sys.stderr.write("usage error: %s\n" % msg)
    raise SystemExit(2)


def die_infra(msg: str) -> None:
    sys.stderr.write("infra error: %s\n" % msg)
    raise SystemExit(4)


def find_root(explicit):
    if explicit:
        if not os.path.isdir(explicit):
            die_usage("--root 不存在：%s" % explicit)
        return os.path.abspath(explicit)
    cur = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isdir(os.path.join(cur, "share")) and any(
                os.path.isdir(os.path.join(cur, c))
                for c in ("agent-experts", "agent-skills", "softwares")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            die_usage("未能定位仓根；请用 --root 指定（钩子面判据不猜根）")
        cur = parent


def read_hookspath_readings(root):
    """core.hooksPath 全 scope 读数（带 origin）。返回 (读数行列表, 命令异常否)。"""
    proc = subprocess.run(
        ["git", "-C", root, "config", "--show-origin", "--get-regexp",
         r"core\.hookspath"],
        capture_output=True, text=True, encoding="utf-8")
    if proc.returncode not in (0, 1):
        return [], True
    lines = [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]
    return lines, False


def blob_sha1(path):
    with open(path, "rb") as handle:
        data = handle.read()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def report(msg):
    print("share/check-hook-health.py:1: %s %s %s" % (SEV_BLOCK, SPEC_ID, msg))


def main(argv):
    parser = argparse.ArgumentParser(description="门禁载体层健康哨兵（只读）")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    args = parser.parse_args(argv)
    root = find_root(args.root)

    findings = 0
    readings, cmd_bad = read_hookspath_readings(root)
    if cmd_bad:
        die_infra("git config 读数命令异常退出（fail-closed，不得降级为不查）")

    # --- 快照行（非发现形态·每次必出＝污染未来即时可见面） ---
    snap_kv = "hooksPath-readings=%d" % len(readings)
    for ln in readings:
        snap_kv += "｜%s" % ln.replace(" ", "=")

    hook = os.path.join(root, ".git", "hooks", "pre-commit")
    on_disk = os.path.isfile(hook)
    if on_disk:
        blob = blob_sha1(hook)
        mode = oct(os.stat(hook).st_mode & 0o111)
        snap_kv += "｜hook-blob=%s｜hook-mode=%s" % (blob, mode)
    else:
        snap_kv += "｜hook-file=absent"
    print("HOOKHEALTH-SNAPSHOT %s" % snap_kv)

    # --- 查一 hooksPath 污染读数（有读数即异常） ---
    for ln in readings:
        findings += 1
        report("hooksPath 污染读数（键在盘＝缺省钩子整体失效）：%s" % ln)

    # --- 查二 期望钩子在盘＋exec 态（exec 仅 POSIX 判） ---
    if not on_disk:
        findings += 1
        report("期望钩子不在盘：%s" % ".git/hooks/pre-commit")
    else:
        if os.name == "posix" and not (os.stat(hook).st_mode & 0o111):
            findings += 1
            report("期望钩子缺可执行位（POSIX 面判）：%s" % ".git/hooks/pre-commit")

        # --- 查三 钩子内容健康（MARKER＋调用行后缀含判＋blob 对钉） ---
        with open(hook, "r", encoding="utf-8", errors="replace") as handle:
            body = handle.read()
        body_lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
        if not any(MARKER in ln for ln in body_lines):
            findings += 1
            report("钩子缺安装器标记行（非本器装的或被改写）：%s" % MARKER)
        for suffix in EXPECTED_CALL_TARGETS:
            if not any(suffix in ln for ln in body_lines):
                findings += 1
                report("钩子调用行缺期望门禁实体（后缀含判）：%s" % suffix)
        if blob != EXPECTED_HOOK_BLOB:
            findings += 1
            report("钩子 blob 对钉失配（本体被改或安装器更新未随正钉值）：现值=%s 期望=%s"
                   % (blob, EXPECTED_HOOK_BLOB))

    return 1 if findings else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按 4，不得吞成 0
        sys.stderr.write("infra error: %s\n" % exc)
        raise SystemExit(4)
