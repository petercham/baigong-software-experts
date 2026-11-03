#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T03-B · B3 注入构造（机械展开·消费面声明④「注入面←表2-3」落点）

规范锚点：架构 v2.9 §9 B3 行「dispatch-builder 机械展开」（V13 L159）；表2-3 审查注入面条款
（V13 L109：审查者看什么由 dispatch-spec 机械定义，不许自选）；§8 派发约定（V13 L152：
name 传 Agent ID 禁中文名；互验键双向比对；同源四方）；§13 差异率分子口径
｛Agent ID 不符∨包哈希不符∨白名单超集｝；违纪行 15「派发身份不符/注入包超集/串行被破」拦截面。

流程：输入票 ID → ①串行闸（活跃票非零拒绝派发＋「呈报」恰一条，复用 serial-gate）→
②按 config/dispatch-spec.json 该节点该席位 injection_faces 机械展开注入包（禁手拼路径）→
③白名单超集检测：请求注入面 ⊖ spec 声明面 ≠ ∅ → exit≠0 回显差异集 →
④Agent ID 互验键双向比对（正向：agent_id 席位前缀＝派发席位；反向：账本 agent 登记表
agent_id→seat 唯一；中文名禁）→不符计差异（§13 分子口径）并拒派发 →
⑤构造断言：注入包成品对过程痕迹词族零命中（表2-3 表注源头即纯款）→
⑥注入包哈希写账本「注入包哈希」记录类（§3 六类）。

运行落盘一律可重定向：--ledger/--states/--agents/--out 与 SWB_LEDGER_ROOT；缺省仓根类路径，
验证运行请重定向至 Temp，不得在仓内留运行残留。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

def _load_sibling(name: str):
    """按文件路径加载同目录件（serial-gate.py 含连字符不可直接 import）。"""
    import importlib.util
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name)
    spec = importlib.util.spec_from_file_location(name.replace("-", "_").replace(".py", ""), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_gate = _load_sibling("serial-gate.py")
append_record = _gate.append_record
check_gate = _gate.check_gate
default_ledger_root = _gate.default_ledger_root
load_states = _gate.load_states

# 过程痕迹词族（§17 正文纯度款 P-Ⅰ 禁项词族·构造断言用；白名单＝指针三形态天然不含）
PURITY_FORBIDDEN_TERMS = ["修订史述", "评审表态", "审计表态", "辩解注", "开工读数", "轮次叙事", "票号叙事"]

# 退出码约定：0 放行｜2 串行闸拒（§4）｜3 白名单超集（违纪行15）｜4 Agent ID 互验不符（违纪行15）｜5 构造断言不过（纯度）
EXIT_SERIAL, EXIT_SUPERSET, EXIT_AGENT_MISMATCH, EXIT_PURITY = 2, 3, 4, 5

AGENT_ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")  # name 传 Agent ID 禁中文名（§8）


def pack_root() -> str:
    d = os.path.abspath(__file__)
    for _ in range(4):
        d = os.path.dirname(d)
    return d


def load_spec(spec_path: str) -> dict:
    with open(spec_path, encoding="utf-8") as f:
        spec = json.load(f)
    if len(spec.get("nodes", [])) != 7:
        raise SystemExit(f"FATAL: dispatch-spec 行数={len(spec.get('nodes', []))} ≠ 表2-3 七行（六节点＋维护行）")
    return spec


def canonical_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def spec_node(spec: dict, node) -> dict | None:
    for n in spec["nodes"]:
        if n["node"] == node:
            return n
    return None


def declared_face(node_cfg: dict, seat_id: str) -> list[dict]:
    """spec 声明面＝该节点该席位 injection_faces 行（机械定义，不许自选）。"""
    for face in node_cfg["injection_faces"]:
        if face["seat"] == seat_id:
            return face["entries"]
    return []


def build_injection_package(ticket_id: str, node_cfg: dict, seat_id: str,
                            entries: list[dict], out_root: str) -> dict:
    """机械展开：路径由「注入存档目录/票ID/条目名」机械拼接（禁手拼）。"""
    items = []
    for e in sorted(entries, key=lambda x: x["name"]):
        path = os.path.join(out_root, ticket_id, seat_id, e["name"] + ".md")
        items.append({"name": e["name"], "kind": e["kind"],
                      "path": path.replace("\\", "/")})
    pkg = {"ticket_id": ticket_id, "node": node_cfg["node"], "seat_id": seat_id, "items": items}
    pkg["package_hash"] = hashlib.sha256(canonical_json(
        {"ticket_id": ticket_id, "node": node_cfg["node"], "seat_id": seat_id,
         "items": [{k: it[k] for k in ("name", "kind", "path")} for it in items]}
    ).encode("utf-8")).hexdigest()
    return pkg


def purity_assertion(pkg: dict) -> list[str]:
    """构造断言：注入包成品对过程痕迹词族零命中（表2-3 表注源头即纯款）。"""
    text = canonical_json(pkg)
    return [t for t in PURITY_FORBIDDEN_TERMS if t in text]


def agent_id_crosscheck(agent_id: str, seat_id: str, agents_file: str) -> list[str]:
    """互验键双向比对（§8）：返回差异列表（空＝双向一致）。

    正向：agent_id 合法性（禁中文名）＋席位前缀＝派发席位；
    反向：账本 agent 登记表 agent_id→seat 映射与请求席位一致（一票一新鲜实例：
    同 agent_id 复派到他席即反向不一致）。
    """
    diffs: list[str] = []
    if not AGENT_ID_RE.match(agent_id or ""):
        diffs.append(f"agent_id={agent_id!r} 非法（name 传 Agent ID 禁中文名·§8）")
        return diffs
    if not agent_id.startswith(f"{seat_id}-"):
        diffs.append(f"正向比对不符：agent_id={agent_id!r} 席位前缀≠派发席位 {seat_id!r}")
    mapping: dict = {}
    if os.path.exists(agents_file):
        with open(agents_file, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    rec = json.loads(line)
                    mapping[rec["agent_id"]] = rec["seat_id"]
    if agent_id in mapping and mapping[agent_id] != seat_id:
        diffs.append(f"反向比对不符：账本登记 agent_id={agent_id!r}→席位 {mapping[agent_id]!r} ≠ 请求席位 {seat_id!r}")
    return diffs


def register_agent(agents_file: str, agent_id: str, seat_id: str, ticket_id: str) -> None:
    os.makedirs(os.path.dirname(agents_file), exist_ok=True)
    with open(agents_file, "a", encoding="utf-8") as f:
        f.write(json.dumps({"agent_id": agent_id, "seat_id": seat_id, "ticket_id": ticket_id},
                           ensure_ascii=False) + "\n")


def dispatch(ticket_meta: dict, spec: dict, ledger_file: str, states_file: str,
             agents_file: str, out_root: str) -> int:
    """按序执行：串行闸→机械展开→超集检测→Agent ID 互验→纯度断言→哈希入账＋派发记录。"""
    ticket_id = ticket_meta["ticket_id"]
    node = ticket_meta["node"]
    seat_id = ticket_meta["seat_id"]
    agent_id = ticket_meta.get("agent_id", "")
    requested = ticket_meta.get("requested_items")  # 缺省＝spec 声明面全量（机械展开）

    # ① 串行闸（§4/§9 B3：活跃票非零拒绝派发；呈报恰一条由 check_gate 写）
    n, rec = check_gate(states_file, ledger_file, ticket_id, actor="dispatch-builder.py")
    if n > 0:
        print(f"REJECT serial-gate ticket={ticket_id}: 活跃票={n} 非零，新派发被串行闸拒绝"
              f"（呈报记录 hash={rec['hash']}）", file=sys.stderr)
        return EXIT_SERIAL

    node_cfg = spec_node(spec, node)
    if node_cfg is None:
        print(f"REJECT: 节点 {node!r} 不在 dispatch-spec 七行内", file=sys.stderr)
        return EXIT_SUPERSET

    # ③ 白名单超集检测：展开请求 ⊖ spec 声明面 ≠ ∅ → exit≠0 回显差异集（违纪行15「注入包超集」）
    face = declared_face(node_cfg, seat_id)
    declared_names = {e["name"] for e in face}
    if requested is not None:
        extra = sorted(set(requested) - declared_names)
        if extra:
            append_record(ledger_file, "呈报", "dispatch-builder.py", {
                "event": "injection_superset_reject", "ticket_id": ticket_id,
                "node": node, "seat_id": seat_id, "superset_items": extra,
                "clause": "违纪行15 注入包超集·白名单超集检测（展开⊖声明面≠∅）",
            })
            print(f"REJECT superset ticket={ticket_id}: 注入面超出 spec 声明面，差异集={extra}", file=sys.stderr)
            return EXIT_SUPERSET
        entries = [e for e in face if e["name"] in set(requested)]
    else:
        entries = list(face)

    # ④ Agent ID 互验键双向比对；不符计差异（§13 分子口径）并拒派发（违纪行15 拦截面）
    diffs = agent_id_crosscheck(agent_id, seat_id, agents_file)
    if diffs:
        append_record(ledger_file, "派发", "dispatch-builder.py", {
            "event": "dispatch_rejected_agent_mismatch", "ticket_id": ticket_id,
            "seat_id": seat_id, "agent_id": agent_id, "agent_id_diffs": diffs,
            "counted_in": "差异率分子｛Agent ID 不符｝（§13）",
        })
        print(f"REJECT agent-crosscheck ticket={ticket_id}: {diffs}", file=sys.stderr)
        return EXIT_AGENT_MISMATCH

    # ② 机械展开＋⑤ 构造断言（过程痕迹词族零命中）
    pkg = build_injection_package(ticket_id, node_cfg, seat_id, entries, out_root)
    hits = purity_assertion(pkg)
    if hits:
        append_record(ledger_file, "呈报", "dispatch-builder.py", {
            "event": "injection_purity_reject", "ticket_id": ticket_id,
            "purity_term_hits": hits, "clause": "表2-3 表注构造断言（P-Ⅰ 前置）",
        })
        print(f"REJECT purity ticket={ticket_id}: 注入包成品命中过程痕迹词族 {hits}", file=sys.stderr)
        return EXIT_PURITY

    # ⑥ 注入包哈希写账本「注入包哈希」记录类（§3 六类）＋派发记录＋agent 登记（反向比对源）
    hash_rec = append_record(ledger_file, "注入包哈希", "dispatch-builder.py", {
        "ticket_id": ticket_id, "node": node, "seat_id": seat_id, "agent_id": agent_id,
        "package_hash": pkg["package_hash"], "item_count": len(pkg["items"]),
    })
    append_record(ledger_file, "派发", "dispatch-builder.py", {
        "event": "dispatch_built", "ticket_id": ticket_id, "node": node, "seat_id": seat_id,
        "agent_id": agent_id, "package_hash": pkg["package_hash"],
    })
    register_agent(agents_file, agent_id, seat_id, ticket_id)
    os.makedirs(out_root, exist_ok=True)
    manifest = os.path.join(out_root, ticket_id, f"{seat_id}-injection-manifest.json")
    os.makedirs(os.path.dirname(manifest), exist_ok=True)
    with open(manifest, "w", encoding="utf-8") as f:
        json.dump(pkg, f, ensure_ascii=False, indent=2)
    print(f"OK dispatch ticket={ticket_id} node={node} seat={seat_id} agent={agent_id} "
          f"items={len(pkg['items'])} package_hash={pkg['package_hash']} ledger_hash={hash_rec['hash']}")
    print(json.dumps(pkg, ensure_ascii=False))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B3 注入构造·机械展开＋超集检测＋Agent ID 互验＋串行闸（§9 B3）")
    ap.add_argument("--ticket", required=True, help="票ID（输入票 ID）")
    ap.add_argument("--node", required=True, help="节点（1-6 或 维护·节点1-3）")
    ap.add_argument("--seat", required=True, help="派发席位ID（seat-permissions 同源 seat_id）")
    ap.add_argument("--agent-id", required=True, help="Agent ID（禁中文名·§8 派发约定）")
    ap.add_argument("--requested-item", action="append", default=None,
                    help="请求注入条目名（可重复；缺省＝spec 声明面全量；超集→exit≠0）")
    ap.add_argument("--spec", default=os.path.join(pack_root(), "config", "dispatch-spec.json"))
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    ap.add_argument("--states", default=os.path.join(default_ledger_root(), "states.json"))
    ap.add_argument("--agents", default=os.path.join(default_ledger_root(), "agents.jsonl"))
    ap.add_argument("--out", default=os.path.join(default_ledger_root(), "injections"),
                    help="注入存档落盘根（可重定向·缺省仓根类路径）")
    a = ap.parse_args(argv)

    node = int(a.node) if a.node.isdigit() else a.node
    spec = load_spec(a.spec)
    meta = {"ticket_id": a.ticket, "node": node, "seat_id": a.seat,
            "agent_id": a.agent_id, "requested_items": a.requested_item}
    return dispatch(meta, spec, a.ledger, a.states, a.agents, a.out)


if __name__ == "__main__":
    sys.exit(main())
