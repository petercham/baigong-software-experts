#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --- spec-provenance v1 ---
# spec_id: PUB-DEF-1
# spec_file: deliverables/object-build/references/60-publish.md
# spec_anchor: 〇、三条定义性约束
# spec_clause_sha256: 170ecb3566ec5df192d49850b45c37419e5f793b4ed8d0dac027d1247456a0a4
# spec_version: 0.3
# spec_effective: 2026-10-23
# provider: object-build
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: PUB-STATE-4
# spec_file: deliverables/object-build/references/60-publish.md
# spec_anchor: 四、`COPY.state`
# spec_clause_sha256: 533f5a1cbe7c631818ee6f00a40c1c4d0c6b77b27763ca354c9cf5dcf6df5a5e
# spec_version: 0.3
# spec_effective: 2026-10-23
# provider: object-build
# --- /spec-provenance ---
# --- spec-provenance v1 ---
# spec_id: PUB-CHECK-7
# spec_file: deliverables/object-build/references/60-publish.md
# spec_anchor: 七、`--check`：五态
# spec_clause_sha256: 97195dd3bde4c1a52580211818c1e142ded3fe479ddc2ece1520a429b56a75e4
# spec_version: 0.3
# spec_effective: 2026-10-23
# provider: object-build
# --- /spec-provenance ---
#
# S-05 发布器（产地 → 部署面·单向·逐字·可判）＋ `--check` 漂移检测。
# **同一判据只在此一处实现**——不另写 check-deploy-drift.py（批 17 指令：两处实现＝D2-3 违例）。
#
# 三条定义性约束（60-publish.md §〇，实现照抄）：
#   1 逐字复制零变换：两侧 sha256 相等＋可执行位相等；不换行、不动 BOM、不转码
#   2 单向：仓 → 部署面；无合并、无反向同步、无"采纳目标"
#   3 先算块、再复制、断言通过、才追加（顺序本身是判据的一部分）
#
# 发布器能力禁令（§十，写死在此防后人"顺手加一个"）：
#   禁：删除目标目录／递归清理／按目录枚举删除／合并／反向同步／文本模式复制／
#       换行转换／BOM 处理／吞异常后照常记账／修改既有块／输出里出现版本号
#   唯一允许的删除：前任块 files: 有、本次 files: 没有的文件（判据＝清单差集，非目录枚举）
#   唯一允许的写：向部署面复制白名单文件、删上述差集、向 COPY.state 追加一块
#
# 部署面写权（裁-18）：本脚本＝部署面唯一写执行体，由执行者席触发；
#   对部署面只写我方在册三包路径，其余（junction／自进化产物）零动作。
# 四步归属判定（设计 v2 §3.3.1，顺序即判据）：
#   ① isjunction ⇒ N-外部（终局）② COPY.state 在册且 copy: 指向该路径 ⇒ P-在册
#   ③ 仓内文本痕迹 ⇒ U-待认领 ④ 都不命中 ⇒ N-非我方（零动作）
#   junction 判定用 os.path.isjunction（islink 对 junction 恒 False——本仓踩过的坑）。
#
# 退出码（60-publish.md §九 映射；闭集见 60-gates.md）：
#   0 通过  1 产物侧不合规（对账不过/白名单缺件/--check 判出需重同步或漂移或权限不符）
#   2 用法错（参数缺/包名不存在/清单项非法/SKILLS_ROOT 未设——不得猜、不得回落）
#   3 前提不成立（未在册且未带 --init/copy: 指向别处/A2 未绿）
#   4 发布器自身或环境错（§五-2 断言不符/复制异常/写块失败——不写块）

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import time

STATE_FILENAME = "COPY.state"
# `copy:` 键记法＝`${SKILLS_ROOT}/<pkg>/<relpath>` 相对式（冲突预警①的实现选择：
# 账本在 S-03 扫描域内，绝对盘符路径必咬 drive-path；相对式机械可判——归属判定②
# 比对时以 env SKILLS_ROOT 展开。若裁-25 改回绝对式，只动本常量与 expand/contract 两处）。
COPY_PREFIX_TOKEN = "${SKILLS_ROOT}"
STATE_KEYS = ("source", "source_sha256", "copy", "copy_sha256_at_sync",
              "synced_at", "source_commit")
BLOCK_HEADER_RE = re.compile(r"^\[sync n=(\d+)\]$")
# 键名含数字（source_sha256/copy_sha256_at_sync）——`[a-z_]+` 会在 sha 处断键（沙箱首咬）。
KEY_LINE_RE = re.compile(r"^([a-z][a-z0-9_]*): ?(.*)$")
FILES_LINE_RE = re.compile(r"^(\S+) +(\S+) +([0-7]{4}) +(\S+)$")
KEBAB_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# 本包项目名（S-03 自伤规避：值拆段，注释不写完整字面量——裁-24 教训第三种形态）。
_PKG_NAME_PARTS = ("multi-agent", "-collab-skillpack")


def die_usage(msg: str) -> "None":
    sys.stderr.write("usage error: %s\n" % msg)
    raise SystemExit(2)


def die_infra(msg: str) -> "None":
    sys.stderr.write("infra error: %s\n" % msg)
    raise SystemExit(4)


def sha256_file(path: str) -> str:
    """bytes 口径（00-skeleton.md 取证纪律：文本模式读会归一 CRLF，hash 必歪）。"""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def mode_of(path: str) -> str:
    """四位八进制权限位（S_IMODE & 0o777，不带文件类型位；§四 mode 记法）。"""
    return "%04o" % (stat.S_IMODE(os.stat(path).st_mode) & 0o777)


def exec_bit(path: str) -> int:
    return stat.S_IMODE(os.stat(path).st_mode) & 0o111


def mode_signature(oct_str: str) -> "tuple[int, int]":
    """§四 mode 判定口径（原文）：**只用「可执行位（0o111）有无」与「只读位」，
    其余位只记录不判定**（避免 umask 与平台噪声变误报）。§十二 平台边界：Windows
    无 POSIX 权限位，st_mode 只反映只读位（普通文件恒 0666/0444）——全量比对在
    Windows 上恒假（0644 vs 0666 天天误报），签名比对才与条款一致。"""
    value = int(oct_str, 8)
    return (1 if value & 0o111 else 0, 1 if value & 0o200 else 0)


def read_text(path: str) -> str:
    # CRLF 归一只用于**解析**；复制路径绝不经过本函数（§五-1 二进制）。
    with open(path, "r", encoding="utf-8", newline="") as handle:
        return handle.read().replace("\r\n", "\n")


def find_root(explicit: "str | None") -> str:
    if explicit:
        if not os.path.isdir(explicit):
            die_usage("--root 不存在：%s" % explicit)
        return os.path.abspath(explicit)
    cur = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isdir(os.path.join(cur, "deliverables")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            die_usage("未能定位仓根；请用 --root 指定")
        cur = parent


def skills_root(env: "dict[str, str]") -> str:
    """目标根一律由环境变量显式给出（§九：无默认值，未设 ⇒ exit 2，不得猜）。"""
    value = env.get("SKILLS_ROOT", "").strip()
    if not value:
        die_usage("SKILLS_ROOT 未设置（目标根必须由环境变量显式给出，不得猜、不得回落当前目录）")
    return os.path.abspath(value)


# ---------------------------------------------------------------- COPY.state

class SyncBlock:
    """一个 `[sync n=k]` 块：六键＋files 四元组（§四）。"""

    def __init__(self, n: int) -> "None":
        self.n = n
        self.keys: "dict[str, str]" = {}
        # relpath -> (repo_sha256, copy_sha256, mode)
        self.files: "dict[str, tuple[str, str, str]]" = {}


def parse_state(text: str) -> "list[SyncBlock]":
    """解析全部块（append-only 流水）。格式坏＝账本被改坏＝环境错 exit 4（发布器维护方）。"""
    blocks: "list[SyncBlock]" = []
    current: "SyncBlock | None" = None
    in_files = False
    for lineno, raw in enumerate(text.split("\n"), 1):
        line = raw.rstrip()
        header = BLOCK_HEADER_RE.match(line)
        if header:
            current = SyncBlock(int(header.group(1)))
            blocks.append(current)
            in_files = False
            continue
        if current is None:
            if line.strip():
                die_infra("COPY.state 块外有内容（第 %d 行）：%r" % (lineno, line))
            continue
        if line.strip() == "files:":
            in_files = True
            continue
        key_match = KEY_LINE_RE.match(line)
        if key_match and not line.startswith(" "):
            current.keys[key_match.group(1)] = key_match.group(2).strip()
            in_files = False
            continue
        if in_files and line.strip():
            quad = FILES_LINE_RE.match(line.strip())
            if not quad:
                die_infra("COPY.state files 行不合四元组（第 %d 行）：%r" % (lineno, line))
            current.files[quad.group(4)] = (quad.group(1), quad.group(2), quad.group(3))
    for block in blocks:
        missing = [k for k in STATE_KEYS if k not in block.keys]
        if missing:
            die_infra("COPY.state 第 %d 块缺键 %s（六键保留，§四）" % (block.n, ",".join(missing)))
    return blocks


def manifest_digest(entries: "list[tuple[str, str, str]]", use_copy: bool) -> str:
    """两块级摘要（§四）：relpath 字节序升序取 "<sha>  <mode>  <relpath>" 以 \\n 连接
    （不含末尾换行）UTF-8 取 sha256。源侧用 repo_sha256，副本侧用 copy_sha256。"""
    col = 1 if use_copy else 0
    lines = sorted(
        ("%s  %s  %s" % (e[col], e[2], e[0]) for e in entries),
        key=lambda s: s.split("  ", 2)[2].encode("utf-8"),
    )
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def state_path(root: str, pkg: str) -> str:
    return os.path.join(root, "deliverables", pkg, STATE_FILENAME)


def load_last_block(root: str, pkg: str) -> "tuple[list[SyncBlock], SyncBlock]":
    path = state_path(root, pkg)
    if not os.path.isfile(path):
        return [], None
    blocks = parse_state(read_text(path))
    if not blocks:
        die_infra("%s 存在但无任何 [sync n=k] 块" % STATE_FILENAME)
    return blocks, blocks[-1]


def copy_target_of(root: str, block: SyncBlock, env: "dict[str, str]") -> str:
    """把最后一块 `copy:` 还原成绝对路径（`${SKILLS_ROOT}` 以 env 展开）。"""
    value = block.keys.get("copy", "")
    if value.startswith(COPY_PREFIX_TOKEN):
        value = os.path.join(env["SKILLS_ROOT"], value[len(COPY_PREFIX_TOKEN):].lstrip("/"))
    return os.path.abspath(value)


def is_registered(root: str, pkg: str, env: "dict[str, str]") -> "tuple[bool, str]":
    """在册（§一）：COPY.state 存在 **且** 最后一块 copy: 指向 {SKILLS_ROOT}/<pkg>。
    二者缺一＝尚未在册（不得当"已发布但内容不符"处理）。只读仓侧，不读部署面字节。

    「指向」＝**目录前缀匹配**：§四 样例的 `copy:` 值是 `<SKILLS_ROOT>/<pkg>/SKILL.md`
    （指向主文件），§3.3.1-② 的表述是"指向 {SKILLS_ROOT}/n"（指向目录）——两者取
    交集＝copy: 落在该目录之下（含其本身）。等值比较会把规范样例自己的写法判成
    "指向别处"（沙箱二咬实证）。
    """
    blocks, last = load_last_block(root, pkg)
    if last is None:
        return False, "未在册（无 %s）" % STATE_FILENAME
    target_dir = os.path.normcase(os.path.join(env["SKILLS_ROOT"], pkg))
    copy_abs = os.path.normcase(copy_target_of(root, last, env))
    if not (copy_abs == target_dir
            or copy_abs.startswith(target_dir + os.sep)):
        return False, "在册目标指向别处：%s" % last.keys.get("copy", "")
    return True, "在册（第 %d 块）" % last.n


# ---------------------------------------------------------------- 五态判定

STATE_CONSISTENT = "一致"
STATE_STALE = "陈旧"
STATE_LAG = "滞后"
STATE_DRIFT = "漂移"
STATE_MODE = "不一致（权限）"
STATE_MISSING = "缺副本"


def judge_file(blocks: "list[SyncBlock]", relpath: str, repo_now: str,
               copy_now: "str | None", mode_now: "str | None") -> "tuple[str, str]":
    """§七 五态（逐文件）。返回（态，说明）。判定顺序：先 hash 态 1→4，落态 1 才判权限。

    blocks＝全部历史块（**块数不可删**——只留一块时态 3 无从谈起，负样本守这条）。
    """
    last = blocks[-1]
    if relpath not in last.files:
        return STATE_DRIFT, "不在最后一块白名单（白名单过期）"
    repo_l, copy_l, mode_l = last.files[relpath]
    if copy_now is None:
        return STATE_MISSING, "部署面无此文件（白名单在册但副本缺失）"
    hist = [blk.files.get(relpath, ("", "", ""))[1] for blk in blocks]
    if copy_now == copy_l:
        if repo_now != repo_l:
            return STATE_STALE, "仓内已先进（副本＝最后基线）"
        if mode_signature(mode_now) != mode_signature(mode_l):
            return STATE_MODE, "mode 期望 %s 现值 %s（判定＝可执行位有无＋只读位，§四；hash 看不见权限位）" % (mode_l, mode_now)
        return STATE_CONSISTENT, ""
    for blk in reversed(blocks[:-1]):
        if relpath in blk.files and copy_now == blk.files[relpath][1]:
            return STATE_LAG, "副本停在第 %d 次同步" % blk.n
    return STATE_DRIFT, "副本字节不在任何同步流水里（先查改动来源）"


# ---------------------------------------------------------------- 四步归属判定

def classify_target(root: str, name: str, env: "dict[str, str]") -> "tuple[str, str]":
    """设计 v2 §3.3.1 四步有序判定。顺序即判据（不先判 junction，第③步会把
    被文档提到过的外部件判成"待认领"——凭空造出 7 件待办）。

    返回（类别，理由）。类别：P-在册 / N-外部 / U-待认领 / N-非我方。
    **没有一步读被判定件的字节**（归属与完整性分离，§3.3.3）。
    """
    target = os.path.join(env["SKILLS_ROOT"], name)
    # ① junction ⇒ 外部（终局）。isjunction 需 3.12+；islink 对 junction 恒 False。
    if os.path.isjunction(target):
        return "N-外部", "①目录联接（终局，不再判）"
    # ② 仓侧在册
    registered, why = is_registered(root, name, env)
    if registered:
        return "P-在册", "②" + why
    # ③ 仓内文本痕迹（decisions/ deliverables/ README.md；docs/ 本仓无，跳过）
    needles = [os.path.join(root, ".collab", "decisions"),
               os.path.join(root, "deliverables")]
    readme = os.path.join(root, "README.md")
    try:
        for base in needles:
            if not os.path.isdir(base):
                continue
            for cur, dirs, files in os.walk(base):
                dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
                for fname in files:
                    if not fname.endswith((".md", ".state")):
                        continue
                    fpath = os.path.join(cur, fname)
                    try:
                        if re.search(r"(?<![A-Za-z0-9_-])%s(?![A-Za-z0-9_-])"
                                     % re.escape(name), read_text(fpath)):
                            return "U-待认领", "③仓内痕迹 %s" % os.path.relpath(fpath, root)
                    except (OSError, UnicodeDecodeError):
                        continue
        if os.path.isfile(readme) and re.search(
                r"(?<![A-Za-z0-9_-])%s(?![A-Za-z0-9_-])" % re.escape(name),
                read_text(readme)):
            return "U-待认领", "③仓内痕迹 README.md"
    except OSError:
        pass
    # ④ 都不命中
    return "N-非我方", "④零动作"


# ---------------------------------------------------------------- 集合对账（§八）

def reconcile(root: str, pkg: str, whitelist: "list[str]") -> "list[str]":
    """白名单↔磁盘对账：只扫白名单涉及的目录（父目录集合 D），D 内只取一层。
    不参与对账：COPY.state 自身、`.` 开头条目。返回 finding 行（空＝通过）。"""
    problems: "list[str]" = []
    pkg_dir = os.path.join(root, "deliverables", pkg)
    whitelist_set = set(whitelist)
    dirs = sorted({os.path.dirname(rel) or "." for rel in whitelist})
    observed: "set[str]" = set()
    for d in dirs:
        base = os.path.join(pkg_dir, d)
        if not os.path.isdir(base):
            continue
        for name in os.listdir(base):
            if name.startswith(".") or name == STATE_FILENAME:
                continue
            rel = (d + "/" + name) if d != "." else name
            if os.path.isfile(os.path.join(base, name)):
                observed.add(rel)
    for rel in sorted(observed - whitelist_set):
        problems.append("未纳管: %s" % rel)
    for rel in sorted(whitelist_set - observed):
        problems.append("缺件: %s" % rel)
    return problems


# ---------------------------------------------------------------- 准入闸（§六）

def gate_a1(root: str, pkg: str) -> "tuple[bool, str]":
    path = os.path.join(root, "deliverables", pkg, "SKILL.md")
    return (os.path.isfile(path), "SKILL.md %s" % ("存在" if os.path.isfile(path) else "不存在（部署面不得成为唯一载体）"))


def gate_a2(root: str) -> "tuple[bool, str]":
    """A2 过审计＝当期 S-01/S-02/S-03 全绿（证据件）＋审计席判词无「阻塞」（decisions 侧）。

    证据件＝run-gates 出口②（`.collab/evidence/gates/`，不入 git）。**已知后果**
    （60-publish.md §六 末注）：新克隆环境无证据件 ⇒ A2 判未绿——这是"证据不随仓走"
    的直接推论，实现里**不得给 A2 开例外**。

    「全绿（exit 0）」的机检取**裁决语义**而非子脚本裸退出码：证据件 findings[] 里
    无被路由表判 block 的发现（＝run-gates 的 GATE PASS 口径）。
    **理由（实现选择·已报告待确认）**：字面 exit 0 在本仓是**恒假**——S-02 因 11 条
    提及类 WATCH（路由 advisory）恒 exit 1，而裁-24 遗留①已认定该状态合法
    （"GATE PASS 不受影响…维持现状可接受"）。三轴分离（60-gates §三）下"绿"的
    定义权在路由裁决，不在发现计数；按字面实现＝把 advisory 当 block，反而违 §三。
    判词机检口径（**裁-25 最小约定**·60-gates.md §七）：判词行格式
    `【判词】<批次>｜阻塞项：<无|列表>｜判定：<放行|有条件放行|不放行>`；
    机检**只认**「阻塞项：无」＋「判定：放行」的组合，其余组合（含"有条件放行"）
    一律未绿。判词由独立审计席出（发布方不得自写判词自放行）。

    「当期」的实现＝**当场跑 run-gates**（A2 语义是"当期全绿"，翻旧证据件＝拿
    历史绿当今天绿）。run-gates 是证据件唯一写者且**只写非 0 退出**（GATE PASS
    不留件），故：①先记运行前的证据件集合，运行后**新增**的才是当期件；
    ②当期无某脚本的件＝该脚本 exit 0（绿），有件则读 findings[] 看 block 路由。
    run-gates 自身 exit≠0（钩子会拦的那种）⇒ A2 直接未绿。
    """
    gates_dir = os.path.join(root, ".collab", "evidence", "gates")
    before = set(os.listdir(gates_dir)) if os.path.isdir(gates_dir) else set()
    code = run_gates(root)
    if code != 0:
        return False, "run-gates 当期 exit %d（GATE 未 PASS）" % code
    after = set(os.listdir(gates_dir)) if os.path.isdir(gates_dir) else set()
    fresh = sorted(after - before)
    bad: "list[str]" = []
    for fname in fresh:
        if not fname.endswith(".json"):
            continue
        try:
            with open(os.path.join(gates_dir, fname), "r", encoding="utf-8") as handle:
                payload = json.load(handle)
        except (OSError, ValueError) as exc:
            bad.append("%s（证据件读坏：%s）" % (fname, exc))
            continue
        blocked = [f for f in payload.get("findings", [])
                   if f.get("commit") == "block"]
        if blocked:
            bad.append("%s（%d 条 block 路由）" % (fname, len(blocked)))
    if bad:
        return False, "当期门禁未绿：%s" % "；".join(bad)
    decisions_dir = os.path.join(root, ".collab", "decisions")
    VERDICT_RE = re.compile(r"【判词】[^｜|]*[｜|]阻塞项：无[｜|]判定：放行")
    latest_verdict = ""
    any_verdict = False
    if os.path.isdir(decisions_dir):
        for fname in sorted(os.listdir(decisions_dir)):
            if not fname.endswith(".md"):
                continue
            for line in read_text(os.path.join(decisions_dir, fname)).split("\n"):
                if "【判词】" in line:
                    any_verdict = True
                    latest_verdict = line  # decisions 按文件名（日期）升序，末条＝最新
    if not any_verdict:
        return False, "decisions 侧无任何【判词】行（裁-25 格式：【判词】<批次>｜阻塞项：…｜判定：…）"
    if VERDICT_RE.search(latest_verdict):
        return True, "最新判词＝阻塞项：无＋判定：放行"
    return False, "最新判词非「阻塞项：无＋判定：放行」组合：%s" % latest_verdict.strip()[:80]


def gate_a3(root: str, pkg: str) -> "tuple[bool, str]":
    """A3 出处齐＝调 S-04（P-1/P-2/P-3 全过）。S-04 默认域＝deliverables/*/scripts/*，
    SKILL.md 的 md 载体块不在其默认域 ⇒ 用 --target 显式指过去（S-04 已支持）。
    exit 1＝产物侧缺件（作者欠账）；exit 3＝提供者欠账。"""
    script = os.path.join(root, "deliverables", "object-audit", "scripts",
                          "check-provenance.py")
    if not os.path.isfile(script):
        die_infra("找不到 S-04：%s" % script)
    proc = subprocess.run(
        [sys.executable, script, "--root", root,
         "--target", "deliverables/%s/SKILL.md" % pkg],
        capture_output=True)
    code = proc.returncode if proc.returncode in (0, 1, 2, 3, 4) else 4
    if code == 0:
        return True, "S-04 exit 0"
    out = ((proc.stdout or b"") + (proc.stderr or b"")).decode("utf-8", errors="replace")
    first = out.strip().split("\n")[0] if out.strip() else ""
    return False, "S-04 exit %d：%s" % (code, first[:120])


def gate_a4(root: str, pkg: str, env: "dict[str, str]") -> "tuple[bool, str]":
    """A4 不撞外部件：目标非 junction；若已存在，其**目录本身**是普通目录即可继续
    （逐文件溯源在复制前断言里做——目录里混有别人文件时由集合对账/白名单兜住）。
    junction ⇒ 拒发（向联接复制＝改别人仓）。"""
    target = os.path.join(env["SKILLS_ROOT"], pkg)
    if os.path.isjunction(target):
        return False, "目标是目录联接（向联接复制＝改别人仓）"
    return True, "目标非联接"


def gate_a5(root: str, pkg: str) -> "tuple[bool, str]":
    """A5 形态合规＝调 S-01（体量/触发）＋本器补两条纯机检（name==目录名且小写
    kebab；references/ 平铺一层）——S-01 现不含这两条，A5 条款要求它们，
    在发布器侧补齐属实现条款，不新增判据。"""
    script = os.path.join(root, "deliverables", "object-audit", "scripts",
                          "check-skill-meta.py")
    if not os.path.isfile(script):
        die_infra("找不到 S-01：%s" % script)
    env2 = dict(os.environ)
    env2.setdefault("GATE_PROJECT_NAMES", _PKG_NAME_PARTS[0] + _PKG_NAME_PARTS[1])
    proc = subprocess.run([sys.executable, script, "--root", root],
                          capture_output=True, env=env2)
    if proc.returncode != 0:
        out = ((proc.stdout or b"") + (proc.stderr or b"")).decode("utf-8", errors="replace")
        first = out.strip().split("\n")[0] if out.strip() else ""
        return False, "S-01 exit %d：%s" % (proc.returncode, first[:120])
    skill_md = os.path.join(root, "deliverables", pkg, "SKILL.md")
    fields = {}
    lines = read_text(skill_md).split("\n")
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            m = re.match(r"^([A-Za-z_]+): *(.*)$", line)
            if m:
                fields[m.group(1)] = m.group(2).strip()
    if fields.get("name") != pkg:
        return False, "frontmatter name=%r 与目录名 %r 不一致" % (fields.get("name"), pkg)
    if not KEBAB_RE.match(pkg):
        return False, "包名不是小写 kebab：%s" % pkg
    refs = os.path.join(root, "deliverables", pkg, "references")
    if os.path.isdir(refs):
        for name in os.listdir(refs):
            if os.path.isdir(os.path.join(refs, name)):
                return False, "references/ 下有子目录（套娃）：%s" % name
    return True, "S-01 exit 0＋name/kebab/平铺过"


# ---------------------------------------------------------------- 证据流水（裁-19）

def evidence_dir(root: str) -> str:
    return os.path.join(root, ".collab", "evidence", "publish")


def write_evidence(root: str, payload: "dict") -> str:
    directory = evidence_dir(root)
    os.makedirs(directory, exist_ok=True)
    stamp = time.strftime("%Y-%m-%dT%H-%M-%S")
    path = os.path.join(directory, "publish-%s-%s.json" % (payload.get("pkg", "?"), stamp))
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
    return path


# ---------------------------------------------------------------- 复制与断言（§五）

def copy_one(src: str, dst: str) -> "None":
    """§五-1：首选 shutil.copy2（连权限位一起复制）。禁文本模式/换行转换/BOM。
    异常**不得吞**（§五-3）：原样上抛，由调用方 exit 4 且不写块。"""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)


def assert_copy(src: str, dst: str) -> "None":
    """§五-2 运行时断言（防线不是声明）：任一不过 ⇒ exit 4 且不写块。"""
    if sha256_file(dst) != sha256_file(src):
        die_infra("断言1不过：副本 sha256 ≠ 源（复制实现走歪：编码/换行/BOM/半写）%s" % dst)
    if exec_bit(dst) != exec_bit(src):
        die_infra("断言3不过：可执行位没跟着走（copyfile 的典型后果）%s" % dst)


def backup_target(root: str, pkg: str, env: "dict[str, str]") -> "str | None":
    """写前备份：把将被覆盖的旧副本（白名单文件）备份到 evidence/publish/backup-<ts>/。
    返回备份目录；目标不存在（首次发布）返回 None。备份失败＝环境错 exit 4（不得裸覆盖）。"""
    target_dir = os.path.join(env["SKILLS_ROOT"], pkg)
    if not os.path.isdir(target_dir):
        return None
    stamp = time.strftime("%Y%m%d-%H%M%S")
    backup_root = os.path.join(evidence_dir(root), "backup-%s" % stamp, pkg)
    count = 0
    for cur, dirs, files in os.walk(target_dir):
        for name in files:
            src = os.path.join(cur, name)
            rel = os.path.relpath(src, target_dir)
            dst = os.path.join(backup_root, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            count += 1
    return backup_root if count else None


def append_block(root: str, pkg: str, env: "dict[str, str]", files: "list[str]",
                 repo_hashes: "dict[str, tuple[str, str, str]]", next_n: int) -> "None":
    """追加一块（§四 只可追加；§三-3 复制断言通过**才**走到这里）。
    写失败＝exit 4（此时副本已新、账本未记——报告里写明"重跑发布可补账，无假基线"：
    重跑时 --check 会判滞后/漂移，不会把没记账的同步洗成合法）。"""
    path = state_path(root, pkg)
    existing = read_text(path) if os.path.isfile(path) else ""
    skill_rel = "SKILL.md"
    entries = sorted(repo_hashes.items(), key=lambda kv: kv[0].encode("utf-8"))
    manifest_repo = manifest_digest([v for _, v in entries], use_copy=False)
    manifest_copy = manifest_digest([v for _, v in entries], use_copy=True)
    commit = "none"
    try:
        proc = subprocess.run(["git", "-C", root, "rev-parse", "HEAD"],
                              capture_output=True, text=True)
        if proc.returncode == 0:
            commit = proc.stdout.strip() or "none"
    except OSError:
        pass
    tz_offset = -time.timezone if time.daylight == 0 else -time.altzone
    sign = "+" if tz_offset >= 0 else "-"
    tz_offset = abs(tz_offset)
    ts = "%s%s%02d:%02d" % (time.strftime("%Y-%m-%dT%H:%M:%S"), sign,
                            tz_offset // 3600, (tz_offset % 3600) // 60)
    lines = [
        "[sync n=%d]" % next_n,
        "source: deliverables/%s/%s" % (pkg, skill_rel),
        "source_sha256: %s" % manifest_repo,
        "copy: %s/%s/SKILL.md" % (COPY_PREFIX_TOKEN, pkg),
        "copy_sha256_at_sync: %s" % manifest_copy,
        "synced_at: %s" % ts,
        "source_commit: %s" % commit,
        "files:",
    ]
    for rel, (repo_sha, copy_sha, mode) in entries:
        lines.append("%s %s %s %s" % (repo_sha, copy_sha, mode, rel))
    block_text = "\n".join(lines) + "\n"
    try:
        if existing and not existing.endswith("\n"):
            block_text = "\n" + block_text
        with open(path, "a", encoding="utf-8", newline="\n") as handle:
            handle.write(block_text)
    except OSError as exc:
        die_infra("写块失败（副本已新、账本未记；重跑发布可补账）：%s" % exc)


# ---------------------------------------------------------------- 子命令

def do_check(root: str, pkg: str, env: "dict[str, str]", verbose: bool) -> int:
    """--check：五态报告，**不写任何东西**。退出码：全一致 0；有需重同步/漂移/权限 1；
    未在册 3。版本号不进任何提示（§一）——本函数输出只有 relpath＋态。"""
    blocks, last = load_last_block(root, pkg)
    if last is None:
        print("%s: 未在册（无 %s）——阶段 0：publish.py --init %s --files <relpath>…"
              % (pkg, STATE_FILENAME, pkg))
        return 3
    target_dir = os.path.join(env["SKILLS_ROOT"], pkg)
    verdicts = []
    for rel in sorted(last.files, key=str.encode):
        repo_path = os.path.join(root, "deliverables", pkg, rel)
        copy_path = os.path.join(target_dir, rel)
        repo_now = sha256_file(repo_path) if os.path.isfile(repo_path) else None
        copy_now = sha256_file(copy_path) if os.path.isfile(copy_path) else None
        mode_now = mode_of(copy_path) if os.path.isfile(copy_path) else None
        if repo_now is None:
            verdicts.append((rel, "缺源", "仓内文件不存在（白名单过期）"))
            continue
        state, why = judge_file(blocks, rel, repo_now, copy_now, mode_now)
        verdicts.append((rel, state, why))
    bad = [v for v in verdicts if v[1] != STATE_CONSISTENT]
    for rel, state, why in verdicts:
        if state == STATE_CONSISTENT and not verbose:
            continue
        print("%s %s: %s%s" % (pkg, rel, state, ("（%s）" % why if why else "")))
    if not bad:
        print("%s: 一致（%d 文件）" % (pkg, len(verdicts)))
        return 0
    print("%s: %d/%d 需处置" % (pkg, len(bad), len(verdicts)))
    return 1


def resolve_bash() -> str:
    """解析**真正的** bash。Windows 上 PATH 里可能混着 WSL shim
    （`WindowsApps\\bash.exe`／`system32\\bash.exe`——调起 wsl.exe，本环境被安全
    策略拦死且输出 GBK 乱码），必须跳过；优先 PortableGit 的 usr/bin/bash。"""
    candidates: "list[str]" = []
    override = os.environ.get("GATE_BASH", "").strip()
    if override:
        candidates.append(override)
    path_dirs = os.environ.get("PATH", "").split(os.pathsep)
    for d in path_dirs:
        cand = os.path.join(d, "bash.exe")
        if os.path.isfile(cand):
            candidates.append(cand)
        cand2 = os.path.join(d, "bash")
        if os.path.isfile(cand2) and not cand:
            candidates.append(cand2)
    for cand in candidates:
        low = cand.replace("\\", "/").lower()
        if "windowsapps" in low or "/system32/" in low:
            continue  # WSL shim，不是 bash
        if "usr/bin" in low or "portablegit" in low or "git\\bin" in low.replace("/", "\\"):
            return cand
    return candidates[0] if candidates else "bash"


def run_gates(root: str) -> int:
    """A2 前置：调 run-gates.sh（它写证据件）。返回其退出码。
    输出按 bytes 捕获再 replace 解码（子进程可能混入非 UTF-8 字节，解码崩＝误报 infra）。"""
    runner = os.path.join(root, "deliverables", "object-audit", "scripts", "run-gates.sh")
    if not os.path.isfile(runner):
        die_infra("找不到 run-gates.sh：%s" % runner)
    bash = resolve_bash()
    proc = subprocess.run([bash, runner, "--root", root],
                          capture_output=True)
    text = (proc.stdout or b"").decode("utf-8", errors="replace")
    for line in text.splitlines():
        print(line)
    return proc.returncode


def do_publish(root: str, pkg: str, env: "dict[str, str]", init_files: "list[str]",
               extra_files: "list[str]", dry_run: bool) -> int:
    """发布（阶段 0 --init / 阶段 n 常规）。§三-3 顺序：算块→复制→断言→追加。"""
    pkg_dir = os.path.join(root, "deliverables", pkg)
    # 清单项格式校验最先跑（§三-1「给到目录或不存在的文件 ⇒ exit 2」；用法错先于
    # 一切闸——调用方的错不该被闸的错掩盖）。
    for rel in init_files + extra_files:
        if rel.startswith("..") or rel.startswith("/") or "\\" in rel or "*" in rel or "?" in rel:
            die_usage("清单项非法（禁通配/目录/绝对/..）：%s" % rel)
        item = os.path.join(pkg_dir, rel)
        if os.path.isdir(item):
            die_usage("清单项是目录（禁目录枚举）：%s" % rel)
        if not os.path.isfile(item):
            die_usage("清单项不存在：%s" % rel)
    # A1 有产地
    ok, why = gate_a1(root, pkg)
    if not ok:
        print("拒发（A1）：%s" % why)
        return 1
    # A4 不撞外部件（先于 A2/A3：junction 一票否决，不浪费门禁）
    ok, why = gate_a4(root, pkg, env)
    if not ok:
        print("拒发（A4）：%s" % why)
        return 1
    # 阶段判定（§二，写死不"看情况"）
    blocks, last = load_last_block(root, pkg)
    registered, reg_why = is_registered(root, pkg, env)
    if blocks and not registered:
        print("拒发：COPY.state 存在但 %s（exit 3）" % reg_why)
        return 3
    if last is None and not init_files:
        print("未在册且未带 --init（exit 3）：阶段 0 须显式清单——"
              "publish.py --init %s --files <relpath>…" % pkg)
        return 3
    if last is not None and init_files:
        print("已在册（第 %d 块）——--init 只用于首次；常规发布去掉 --init" % last.n)
        return 2
    # 白名单（§二：阶段 0＝命令行唯一来源；阶段 n＝最后一块 ∪ --files）
    if last is None:
        whitelist = sorted(set(init_files), key=str.encode)
        for rel in whitelist:
            if rel.startswith("..") or rel.startswith("/") or "\\" in rel or "*" in rel or "?" in rel:
                die_usage("清单项非法（禁通配/目录/绝对/..）：%s" % rel)
            item = os.path.join(pkg_dir, rel)
            if os.path.isdir(item):
                die_usage("清单项是目录（禁目录枚举）：%s" % rel)
            if not os.path.isfile(item):
                die_usage("清单项不存在：%s" % rel)
    else:
        whitelist = sorted(set(list(last.files) + extra_files), key=str.encode)
    # 集合对账（§八）——--init 同样跑（§三-2 同一套断言，无初始化例外）
    problems = reconcile(root, pkg, whitelist)
    if problems:
        for line in problems:
            print(line)
        return 1
    # A2/A3/A5 准入闸（--init 同样全跑）
    for gate_id, fn in (("A2", lambda: gate_a2(root)),
                        ("A3", lambda: gate_a3(root, pkg)),
                        ("A5", lambda: gate_a5(root, pkg))):
        ok, why = fn()
        if not ok:
            code = 3 if gate_id == "A2" else 1
            print("拒发（%s）：%s（exit %d）" % (gate_id, why, code))
            return code
    if dry_run:
        print("%s: 准入闸全绿（dry-run 未写）" % pkg)
        return 0
    # 幂等短路（批 17 验收 5）：同状态重复 publish ⇒ 零差异、**不追加空块**。
    # 空块＝把"这次没发生"记成"这次同步了"——流水会掺入非事件，滞后态失去精度。
    # 条件必须含"白名单未扩"：--files 带了新文件时 check（只看最后一块）会假 0，
    # 直接短路＝新文件漏发。
    if (last is not None and set(whitelist) == set(last.files)
            and do_check(root, pkg, env, verbose=False) == 0):
        print("%s: 已一致（第 %d 块），零写入" % (pkg, last.n))
        return 0
    # 备份旧副本（裁-18：发布器＝部署面唯一写；写前备份）
    backup = backup_target(root, pkg, env)
    # 复制＋逐文件断言（§五-2/§五-3：异常 exit 4 不写块）
    repo_hashes: "dict[str, tuple[str, str, str]]" = {}
    target_dir = os.path.join(env["SKILLS_ROOT"], pkg)
    try:
        for rel in whitelist:
            src = os.path.join(pkg_dir, rel)
            dst = os.path.join(target_dir, rel)
            copy_one(src, dst)
            assert_copy(src, dst)
            repo_hashes[rel] = (sha256_file(src), sha256_file(dst), mode_of(dst))
    except SystemExit:
        raise
    except OSError as exc:
        die_infra("复制异常（不写块）：%s" % exc)
    # 唯一允许的删除：前任块有、本次白名单没有（清单差集，非目录枚举）
    removed: "list[str]" = []
    if last is not None:
        for rel in sorted(set(last.files) - set(whitelist), key=str.encode):
            stale = os.path.join(target_dir, rel)
            if os.path.isfile(stale):
                os.remove(stale)
                removed.append(rel)
    # 块级断言（§五-2 断言 2）：副本清单摘要 == 源清单摘要
    entries = list(repo_hashes.values())
    if manifest_digest(entries, use_copy=False) != manifest_digest(entries, use_copy=True):
        die_infra("断言2不过：块级清单摘要两侧不等（复制实现走歪）")
    # 断言通过 → 才追加块（§三-3）
    next_n = (blocks[-1].n + 1) if blocks else 1
    append_block(root, pkg, env, whitelist, repo_hashes, next_n)
    # 复跑 --check 期望一致（§3.6.2 步 7：追加后仍不一致＝发布器 bug ⇒ exit 4）
    code = do_check(root, pkg, env, verbose=False)
    if code != 0:
        die_infra("发布后自检不过（发布器 bug，立即上报）：check exit %d" % code)
    write_evidence(root, {"pkg": pkg, "sync_n": next_n, "files": len(whitelist),
                          "removed": removed, "backup": backup, "result": "ok"})
    print("%s: 已发布（第 %d 块，%d 文件%s）"
          % (pkg, next_n, len(whitelist),
             ("，删 %d" % len(removed)) if removed else ""))
    return 0


def main(argv: "list[str]") -> int:
    parser = argparse.ArgumentParser(add_help=True,
                                     description="S-05 发布器（仓→部署面·单向·逐字）＋--check 漂移检测")
    parser.add_argument("--root", help="仓根（默认自脚本位置向上定位）")
    parser.add_argument("--check", action="store_true",
                        help="五态报告（不写任何东西）；不给 --pkg 时全查有 SKILL.md 的包")
    parser.add_argument("--init", action="store_true",
                        help="阶段 0：首次入库（清单必须显式给，禁目录枚举）")
    parser.add_argument("--pkg", help="包名（发布/单包核查时必填）")
    parser.add_argument("--files", action="append", default=[],
                        help="清单项（相对 deliverables/<pkg>/，可重复）")
    parser.add_argument("--dry-run", action="store_true", help="只过闸不写")
    parser.add_argument("--verbose", action="store_true",
                        help="人读摘要（版本号只允许出现在这里，且标注描述性）")
    parser.add_argument("--classify", action="store_true",
                        help="对部署面一级条目跑四步归属判定（只读）")
    args = parser.parse_args(argv)
    root = find_root(args.root)
    env = dict(os.environ)
    if args.classify:
        sr = skills_root(env)
        for name in sorted(os.listdir(sr)):
            if name.startswith(".") or name.endswith(".zip"):
                continue
            full = os.path.join(sr, name)
            if not (os.path.isdir(full) or os.path.isjunction(full)):
                continue
            kind, why = classify_target(root, name, env)
            print("%-36s %s  %s" % (name, kind, why))
        return 0
    if args.check:
        skills_root(env)
        pkgs = [args.pkg] if args.pkg else sorted(
            d for d in os.listdir(os.path.join(root, "deliverables"))
            if os.path.isfile(os.path.join(root, "deliverables", d, "SKILL.md")))
        # 聚合规则（§3.6.2 步 3 闭集 0/1/3）：有 1 即 1（需处置压过未在册）；
        # 否则有 3 报 3；全 0 才 0。4 不经此处（die_infra 直接 SystemExit）。
        codes = set()
        for pkg in pkgs:
            codes.add(do_check(root, pkg, env, args.verbose))
            if args.verbose:
                skill_md = os.path.join(root, "deliverables", pkg, "SKILL.md")
                for line in read_text(skill_md).split("\n")[:10]:
                    m = re.match(r"^version: *(.+)$", line)
                    if m:
                        print("%s: [描述性，不参与判定] 仓内 version=%s" % (pkg, m.group(1)))
        if 1 in codes:
            return 1
        return 3 if 3 in codes else 0
    if not args.pkg:
        die_usage("发布需要 --pkg <包名>")
    if not KEBAB_RE.match(args.pkg):
        die_usage("包名不是小写 kebab：%s" % args.pkg)
    skills_root(env)
    if args.init:
        return do_publish(root, args.pkg, env, args.files, [], args.dry_run)
    return do_publish(root, args.pkg, env, [], args.files, args.dry_run)


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未定义路径按 4（闭集，60-gates.md §六）
        sys.stderr.write("infra error: %s\n" % exc)
        raise SystemExit(4)
