#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T04-F · B11 记忆中立化（两面扫描）

规范锚点：架构 v2.9 §9 B11 行「Read/Grep matcher 扫描＋下游件引用扫描」；对应 U6/G1-G2、
违纪模式表行 1（B11 面）与行 6「检索自救→U7＋B11 读侧扫描（P3 能力面未验证，只作辅助面不作假设）」、
行 11「过程件被用作引用目标→B8 引用可达性扫描＋B11 下游件引用扫描」。
诚实边界（当票面明示）：U7 保证＝「P3[未验证]＋G5 辅助面」（§7 对应行）——
本脚本只实现读侧检出面，不声明阻断性能力面保证。

两面：
  ①prehook（Read/Grep matcher）：扫描记忆文件读取请求 → 命中记忆路径 → 拦/标
    （permissionDecision deny 或 ask 属 §19 词表既有值；缺省 ask＝标，deny 可配）；
  ②scan：下游件引用扫描——新增/修改件文本出现记忆文件路径引用 → 报「引用扫描命中」
    呈报码（触发源六闭集第四项·真源 decision-pack.py L43）。
记忆路径集＝缺省六族形态（memory/、.memory、MEMORY.md、memories/、记忆文件族），
可经 --memory-globs 配置闭包扩展。
运行落盘一律可重定向：--ledger 与 SWB_LEDGER_ROOT；仓内零运行残留。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

TRIGGER_REF_SCAN_HIT = "引用扫描命中"  # 触发源六闭集第四项（真源 decision-pack.py L43）

# 记忆路径族（缺省闭包；配置可扩展）
DEFAULT_MEMORY_GLOBS = ["memory/**", ".memory/**", "memories/**", "MEMORY.md",
                        "**/memory/**", "**/.memory/**", "**/MEMORY.md"]


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


def glob_match(pattern: str, rel_path: str) -> bool:
    p = pattern.replace("\\", "/")
    parts, i = [], 0
    while i < len(p):
        if p.startswith("**", i):
            parts.append(".*")
            i += 2
            if i < len(p) and p[i] == "/":
                i += 1
        elif p[i] == "*":
            parts.append("[^/]*")
            i += 1
        elif p[i] == "?":
            parts.append("[^/]")
            i += 1
        else:
            parts.append(re.escape(p[i]))
            i += 1
    return re.fullmatch("".join(parts), rel_path) is not None


def memory_hit(path: str, globs: list[str]) -> str | None:
    """读取目标命中记忆路径族判定：glob 匹配∨路径段含记忆族主干。"""
    norm = str(path).replace("\\", "/")
    segs = set(norm.split("/"))
    for g in globs:
        if glob_match(g, norm):
            return g
        stem = g.replace("**", "").strip("/")
        if stem and (stem in segs or norm.endswith("/" + stem) or norm == stem):
            return g
    return None


def prehook(a: argparse.Namespace, payload: dict) -> int:
    """面①：Read/Grep matcher——记忆文件读取→引用记忆作流程状态即拦/标（缺省 ask＝标）。"""
    ti = payload.get("tool_input") or {}
    target = a.path or ti.get("file_path") or ti.get("path") or ti.get("pattern") or ""
    if not target:
        return 0
    hit = memory_hit(target, a.memory_globs)
    if hit is None:
        return 0
    rec = append_record(a.ledger, "呈报", "memory-neutralize.py", {
        "event": "memory_read_flagged", "target": target, "matched_glob": hit,
        "decision": a.read_decision,
        "clause": "§9 B11 行读侧扫描；诚实边界＝只实现读侧检出面，不声明阻断性能力面保证（§7 对应行）",
    })
    decision = json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": a.read_decision,  # §19 词表既有值 deny/ask（不自造）
            "permissionDecisionReason": f"B11 记忆中立化：读取目标命中记忆路径族（glob={hit!r}）→ 标（ask）",
        }
    }, ensure_ascii=False, separators=(",", ":"))
    print(decision)
    print(f"FLAG memory-neutralize: target={target} glob={hit} decision={a.read_decision} ledger_hash={rec['hash']}", file=sys.stderr)
    return 0


def scan(a: argparse.Namespace) -> int:
    """面②：下游件引用扫描——件文本出现记忆路径引用→「引用扫描命中」呈报码。"""
    hits: list[dict] = []
    for path in a.files:
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
        for g in a.memory_globs:
            # 引用形态＝glob 的字面主干出现在件文本中（路径引用字面命中）
            stem = g.replace("**", "").rstrip("/")
            if not stem:
                continue
            for m in re.finditer(re.escape(stem), text):
                hits.append({"file": path, "memory_ref": stem, "offset_line": text[:m.start()].count("\n") + 1})
                break
    if hits:
        rec = append_record(a.ledger, "呈报", "memory-neutralize.py", {
            "event": "trigger_report", "trigger_source": TRIGGER_REF_SCAN_HIT,
            "hits": hits,
            "clause": "§9 B11 行下游件引用扫描；违纪行 11（过程件/记忆被用作引用目标）",
        })
        print(f"HIT ref-scan: {len(hits)} 处记忆路径引用命中，呈报码「引用扫描命中」入账 hash={rec['hash']}")
        for h in hits:
            print(f"  {h['file']}:{h['offset_line']} -> {h['memory_ref']}")
        return 1  # 命中即非零回显（呈报码已落账）
    print("OK ref-scan: 零记忆路径引用命中")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B11 记忆中立化（读侧标/拦＋下游件引用扫描）")
    ap.add_argument("phase", choices=["prehook", "scan"])
    ap.add_argument("--input", default=None, help="PreToolUse payload JSON 文件（测试注入面）")
    ap.add_argument("--path", default=None, help="读取目标注入面（prehook 优先于 payload.tool_input）")
    ap.add_argument("--files", nargs="*", default=[], help="下游件清单（scan 面）")
    ap.add_argument("--read-decision", choices=["ask", "deny"], default="ask",
                    help="读侧命中决策（§19 词表既有值；缺省 ask＝标，不声明阻断保证）")
    ap.add_argument("--memory-globs", nargs="*", default=DEFAULT_MEMORY_GLOBS)
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    a = ap.parse_args(argv)

    if a.phase == "prehook":
        if not governance_resident():
            print("NEUTRAL memory-neutralize: project-root 探测全缺位且租约台账缺位＝非百工管辖项目→钩子惰性放行（ITER-K 锚门中立放行）", file=sys.stderr)
            return 0
        payload: dict = {}
        if a.input:
            with open(a.input, encoding="utf-8") as f:
                payload = json.load(f)
        elif not a.path and not sys.stdin.isatty():
            raw = sys.stdin.read().strip()
            if raw:
                try:
                    payload = json.loads(raw)
                except json.JSONDecodeError:
                    payload = {}
        return prehook(a, payload)
    return scan(a)


if __name__ == "__main__":
    sys.exit(main())
