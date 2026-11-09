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
#
# 本件＝提交钩子链上的暂存面对照环节（FX-U30 排产票 S1）。判据来源（不复写正文，只指路径）：
#   卷入案型本体与条款防线 → `agent-skills/fuxi-skill/.collab/defects/2026-11-07-FUXI-缺陷台账归因复盘-v1.md`（D-58 行）
#   退出码闭集 → agent-skills/multi-collab/references/60-gates.md「六、退出码闭集」
#   行为规格唯一真源 → 本票票面 S1 fenced 块（tickets 桶内 FX-U30 排产施工票）
#
# 调用位置：由 pre-commit 钩子在 run-gates 链之前直接调起（fail-fast：咬住即拒提不再跑全链）；
#   本件不进 run-gates.sh 清单。亦可独立手跑。
# 探针定档（票面 §〇-2）：钩子环境内跑 git diff --cached --name-only -z 天然继承
#   GIT_INDEX_FILE——pathspec 提交只见 next-index 子集视图（天然零误拦）；
#   无 pathspec 提交见全共享 staged 面（含窗口期他席插入件＝卷入必咬）。
#
# 退出码（闭集·与检查脚本闭集对齐但不含 3）：
#   0 放行（staged⊆声明；或 BYPASS 全转警告）
#   1 卷入 BLOCK（存在 staged 件 ∉ 声明闭集，或无声明且 staged 非空——均 fail-closed）
#   2 用法错  4 基础设施错（git 不可用／声明文件不存在／staged 读数命令失败）
# 未预期异常按 4（不得吞成 0）。
# 本件只读：零写盘——不建目录、不写证据件、不碰 index（BYPASS 留痕归 run-gates 出口②职责）。
"""FX-U30 暂存声明闸

用法：
    python check-staged-declaration.py [--root <仓根>] [--declare <声明文件>]
    其余参数一律用法错 exit 2（不猜）。

声明源闭集（两种·环境变量优先）：
  1) 环境变量 FX_COMMIT_DECLARE：换行或逗号分隔的仓根相对路径清单；
  2) --declare 指向的文件：每行一路径（空行跳过）。
  两者皆缺＝无声明场景（staged 非空即硬拦＝皮总 2026-11-09 裁定「提交闸：升」FX-U32 升格在册；唯一豁免通道＝ALLOW_GATE_DOWN=1 全转警告留痕·灰度期豁免不另设）。
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys

SUMMARY_FMT = "STAGED-DECL: staged %d｜声明 %d｜超额 %d"


def die_usage(msg: str) -> "None":
    sys.stderr.write("usage error: %s\n" % msg)
    raise SystemExit(2)


def die_infra(msg: str) -> "None":
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


def norm_decl(p: str) -> str:
    """声明侧归一：去首尾空白→反斜杠归正斜杠→剥去 ./ 前缀（比对只认全路径相等）。"""
    p = p.strip().replace("\\", "/")
    while p.startswith("./"):
        p = p[2:]
    return p


def read_declared(root: str, declare_path: str | None) -> "list[str] | None":
    """声明源闭集两形态·环境变量优先。皆缺＝None（无声明场景）。"""
    env = os.environ.get("FX_COMMIT_DECLARE")
    if env is not None:
        raw_items: "list[str]" = []
        for chunk in env.replace(",", "\n").split("\n"):
            item = norm_decl(chunk)
            if item:
                raw_items.append(item)
        return raw_items
    if declare_path is not None:
        target = declare_path
        if not os.path.isfile(target):
            # 允许相对仓根的写法（钩子 cwd 不保证）；两处都落空＝基础设施错
            cand = os.path.join(root, declare_path.replace("/", os.sep))
            if os.path.isfile(cand):
                target = cand
            else:
                die_infra("--declare 指向不存在的文件：%s" % declare_path)
        raw_items = []
        try:
            with open(target, "r", encoding="utf-8", newline="") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError) as exc:
            die_infra("读取声明文件失败 %s: %s" % (target, exc))
        for chunk in text.replace("\r\n", "\n").split("\n"):
            item = norm_decl(chunk)
            if item:
                raw_items.append(item)
        return raw_items
    return None


def read_staged(root: str) -> "list[str]":
    """staged 面读数＝当轮 git diff --cached --name-only -z（NUL 分隔防转义歧义）。

    不显式覆盖 GIT_INDEX_FILE：钩子环境里它天然指向 next-index（pathspec 提交）
    或共享 index（无 pathspec 提交）——两种视图语义即票面 §〇-2 探针定档。
    命令失败＝基础设施错（fail-closed，不得当空面放行）。
    """
    try:
        proc = subprocess.run(
            ["git", "-C", root, "diff", "--cached", "--name-only", "-z"],
            capture_output=True, text=True, encoding="utf-8")
    except OSError as exc:
        die_infra("git 不可用：%s" % exc)
        return []
    if proc.returncode != 0:
        die_infra("staged 读数命令失败（git diff --cached --name-only -z exit %d）：%s"
                  % (proc.returncode, (proc.stderr or "").strip()))
    return [p for p in proc.stdout.split("\0") if p]


def main(argv: "list[str]") -> int:
    parser = argparse.ArgumentParser(description="暂存声明闸（staged⊆声明闭集）")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    parser.add_argument("--declare", help="声明文件路径（每行一仓根相对路径）")
    args = parser.parse_args(argv)  # 未知参数 argparse 默认 exit 2＝用法错闭集内

    root = find_root(args.root)
    declared = read_declared(root, args.declare)
    staged = read_staged(root)
    bypass = os.environ.get("ALLOW_GATE_DOWN", "") == "1"

    if declared is None:
        # 三③' 无声明场景＝fail-closed 硬拦（FX-U32·承皮总裁定点②；灰度反例两枚在册 TR26 575fbba／TR27 67fc6b4）
        if staged:
            view = "next-index" if "next-index" in os.path.basename(os.environ.get("GIT_INDEX_FILE", "")) else "shared-index"
            print("STAGED-DECL-VIEW %s（GIT_INDEX_FILE 读数视图·提交侧对照可见化）" % view)
            if bypass:
                print("BYPASS STAGED-DECL-BLOCK 本次提交无声明闭集：staged %d 件全部入账（卷入风险面·见 D-58）" % len(staged))
                print("BYPASS STAGED-DECL-BLOCK 声明指引：提交前设环境变量 FX_COMMIT_DECLARE=仓根相对路径清单（逗号或换行分隔）或传 --declare 声明文件；add 与 commit 紧邻无窗口·pathspec 须 add/commit 两端齐带")
                print("BYPASS " + SUMMARY_FMT % (len(staged), 0, len(staged)))
                return 0
            print("STAGED-DECL-BLOCK 本次提交无声明闭集：staged %d 件全部入账（卷入风险面·见 D-58）" % len(staged))
            print("STAGED-DECL-BLOCK 声明指引：提交前设环境变量 FX_COMMIT_DECLARE=仓根相对路径清单（逗号或换行分隔）或传 --declare 声明文件；add 与 commit 紧邻无窗口·pathspec 须 add/commit 两端齐带")
            print(SUMMARY_FMT % (len(staged), 0, len(staged)) + "｜exit 1")
            return 1
        return 0

    decl_set = set(declared)
    # 七、比对＝全路径相等，不做后缀匹配（防多义放行）
    excess = [p for p in staged if p not in decl_set]

    if not excess:
        # 三① 有声明且 staged⊆声明 → exit 0（仅汇总行）
        print(SUMMARY_FMT % (len(staged), len(decl_set), 0))
        return 0

    # 三② 有声明且存在 staged 件 ∉ 声明闭集 → BLOCK（fail-closed）
    if bypass:
        # 四、绕过口径：全部转警告·前缀 BYPASS·exit 0；本闸不写证据件（留痕归 run-gates 出口②）
        for p in excess:
            print("BYPASS STAGED-DECL-BLOCK %s 不在声明闭集内" % p)
        print("BYPASS " + SUMMARY_FMT % (len(staged), len(decl_set), len(excess)))
        return 0
    for p in excess:
        print("STAGED-DECL-BLOCK %s 不在声明闭集内" % p)
    print(SUMMARY_FMT % (len(staged), len(decl_set), len(excess)) + "｜exit 1")
    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按 4，不得吞成 0
        sys.stderr.write("infra error: %s\n" % exc)
        raise SystemExit(4)
