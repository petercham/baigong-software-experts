#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T04-B · B5 写侧校验（消费面声明②「写侧校验规则←表2-1 不可写列」落点）

规范锚点：架构 v2.9 §9 B5 行（V13 L153–166 内）「PreToolUse stdin 直读 agent_id/agent_type
查租约[实证: buildAgentTrigger，§19；运行时完整性＝未验证:P4]」；表2-1「明确不可写」列
（V13 L70–79，经 config/seat-permissions-hooks-map.json 消费）；违纪模式表行 2
「越租约路径写入→U2＋B5 deny」。
票面纪律镜像 §10：P4 运行时读数＝inconclusive（tests/probes/results/probe-results.json）——
不把 stdin 完整性当已成立闸前提：主路（PreToolUse stdin 直读）与退路（SubagentStart 状态文件）
双形并列同交付、缺省走主路不启用退路；择路由候裁 Q-04，本脚本不自行拍板。

判据（两形同判，身份源不同）：
  身份→席位归因（seat-permissions-hooks-map.json agent_type_to_seat）；
  路径 ∈ 当席租约 path_globs（leases.jsonl 现行态）且路径 ∉ deny_globs → 放行；
  路径 ∉ 租约 path_globs ∨ 路径 ∈ deny_globs → permissionDecision deny（U2/G1）。
每次 deny：写「写入」记录（deny 留痕）＋触发「租约越界 deny」呈报码
（触发源六闭集第一项·真源＝decision-pack.py 六码）。
B10 联动：freeze-state（freeze-unfreeze.py 落盘）deny_all_writes 在位→全写 deny。
U7/诚实边界：退路形态仅状态文件读取，不声明平台阻断性能力面保证。

运行落盘一律可重定向：--ledger/--leases/--map/--freeze-state 与 SWB_LEDGER_ROOT；
验证运行请重定向至 Temp（仓内零运行残留）。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

TRIGGER_LEASE_DENY = "租约越界deny"  # 触发源六闭集第一项（真源＝decision-pack.py L40–45）

EXIT_USAGE = 2  # 与 hooks exit 2→blocking 词表一致的阻断退出码


def pack_root() -> str:
    # 本件居 skills/sop/scripts/ 下，上溯四级＝包根 .../baigong-software-team
    d = os.path.abspath(__file__)
    for _ in range(4):
        d = os.path.dirname(d)
    return d


def repo_root() -> str:
    # 交付树件上溯六级＝仓根（scripts→sop→skills→baigong→experts→deliverables→根）
    env = os.environ.get("SWB_REPO_ROOT")
    if env:
        return env
    d = pack_root()
    for _ in range(3):
        d = os.path.dirname(d)
    return d


def default_ledger_root() -> str:
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(os.getcwd(), ".collab", "ledger"))


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
    rec["hash"] = hashlib_sha256(
        f'{rec["seq"]}\n{rec["ts"]}\n{rec["type"]}\n{rec["actor"]}\n{canonical_json(rec["payload"])}\n{prev_hash}'.encode("utf-8")
    )
    with open(ledger_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def hashlib_sha256(data: bytes) -> str:
    import hashlib
    return hashlib.sha256(data).hexdigest()


# ---- glob 匹配（表2-1 路径锚定款：仓根字面；全角括注＝源件注记，匹配前剥离） ----
def glob_match(pattern: str, rel_path: str) -> bool:
    p = re.sub(r"（[^）]*）", "", pattern).strip()
    if not p:
        return False
    # 含非机械字符（CJK 描述行如「（工作空间根∪部署路径）−受保护区」）＝非 glob 声明行，不参与机械匹配
    if re.search(r"[\u4e00-\u9fff∪−]", p):
        return False
    if p.endswith("/"):
        return rel_path.startswith(p)
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


def normalize_path(raw: str) -> str:
    """输入路径→仓根相对 posix 字面（表注路径锚定＝仓根字面）。"""
    p = str(raw).replace("\\", "/")
    root = repo_root().replace("\\", "/")
    if p.lower().startswith(root.lower() + "/"):
        p = p[len(root) + 1:]
    elif len(p) >= 2 and p[1] == ":":
        # 绝对路径落在别的盘/仓外：保留原字面小写化盘符（deny 面仍可命中仓根字面，租约面不命中即拒）
        p = p[0].lower() + p[1:]
    return p.lstrip("/")


def load_map(map_path: str) -> dict:
    with open(map_path, encoding="utf-8") as f:
        return json.load(f)


def seat_of(agent_type: str | None, agent_id: str | None, mapping: dict) -> str | None:
    """席位归因：agent_type 精确→agent_id 前缀近似（状态文件退路可能只带 agent_type）。"""
    if agent_type and agent_type in mapping:
        return mapping[agent_type]
    if agent_id:
        for k, v in mapping.items():
            if k and (str(agent_id).startswith(k) or k in str(agent_id)):
                return v
    return None


def load_leases(leases_file: str) -> list[dict]:
    """租约台账现行态（lease-issuer.py 落盘 schema：{ts, lease{ticket_id,path_globs,seat_id,hash}, countersign}）。
    freeze 清租约标记行（无 lease 键或 cleared=true）之后的租约全部失效。"""
    out: list[dict] = []
    if os.path.exists(leases_file):
        with open(leases_file, encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                e = json.loads(line)
                if e.get("cleared"):
                    out = []  # 清租约＝其后无活跃租约（B10 freeze 链）
                    continue
                if isinstance(e.get("lease"), dict):
                    out.append(e)
    return out


def deny_output(reason: str) -> str:
    """PreToolUse 决策词表（§19 V13 L224：permissionDecision deny/ask）——deny 输出。"""
    return json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }, ensure_ascii=False, separators=(",", ":"))


def decide(identity: dict, file_path: str, map_path: str, leases_file: str,
           freeze_state_file: str) -> tuple[bool, str]:
    """核心判据（主路/退路同判，identity 只换身份源）：返回 (allow?, reason)。"""
    cfg = load_map(map_path)
    seat = seat_of(identity.get("agent_type"), identity.get("agent_id"), cfg.get("agent_type_to_seat", {}))
    rel = normalize_path(file_path)

    # B10 联动：freeze 态全写 deny（§9 B10 行「全写 matcher 置 deny」）
    if os.path.exists(freeze_state_file):
        with open(freeze_state_file, encoding="utf-8") as f:
            fs = json.load(f)
        if fs.get("deny_all_writes"):
            return False, f"B10 freeze 态全写 deny（seat={seat} path={rel}）"

    if seat is None:
        # fail-closed：席位不可归因即拒（写侧校验不猜身份）
        return False, f"席位不可归因（agent_type={identity.get('agent_type')!r} agent_id={identity.get('agent_id')!r}）→ deny"

    # deny_globs 命中＝表2-1「明确不可写」列（U2/G1）
    for row in cfg.get("seats", []):
        if row.get("seat_id") == seat:
            for g in row.get("deny_globs", []):
                if glob_match(g, rel):
                    return False, f"路径∈deny_globs（表2-1 明确不可写·seat={seat} glob={g!r} path={rel}）→ deny"

    # 租约面：路径须∈当席活跃租约 path_globs
    leases = [e for e in load_leases(leases_file) if e["lease"].get("seat_id") == seat]
    for e in leases:
        for g in e["lease"].get("path_globs", []):
            if glob_match(g, rel):
                return True, f"路径∈租约（ticket={e['lease']['ticket_id']} glob={g!r}）→ allow"
    return False, f"路径∉当席租约 path_globs（越租约路径写入·违纪行2→U2＋B5 deny·seat={seat} path={rel}）→ deny"


def record_deny(ledger_file: str, seat: str | None, identity: dict, file_path: str, reason: str,
                event: str = "write_deny") -> None:
    """每次 deny：「写入」记录留痕＋「租约越界 deny」呈报码（触发源六闭集第一项）。"""
    payload = {"event": event, "path": file_path, "seat_id": seat,
               "agent_type": identity.get("agent_type"), "agent_id": identity.get("agent_id"),
               "reason": reason}
    append_record(ledger_file, "写入", "write-guard.py", payload)
    append_record(ledger_file, "呈报", "write-guard.py", {
        "event": "trigger_report", "trigger_source": TRIGGER_LEASE_DENY,
        "path": file_path, "seat_id": seat,
        "clause": "§4 触发源六闭集①租约越界 deny（真源 decision-pack.py）；§9 B5 行",
    })


def read_identity(args: argparse.Namespace, payload: dict) -> dict:
    """身份源双形并列（P4 inconclusive·镜像 §10）：
    主路＝PreToolUse stdin 直读 agent_id/agent_type（缺省）；
    退路＝SubagentStart 状态文件按 session_id 查表（候裁 Q-04，缺省不启用）。"""
    if args.identity_source == "stdin":
        return {"agent_id": payload.get("agent_id"), "agent_type": payload.get("agent_type")}
    # 退路：状态文件形态（§9 B5 行「P4 阴性→SubagentStart 状态文件，人类拍板启用」）
    sid = str(payload.get("session_id", ""))
    state = {}
    if args.state_file and os.path.exists(args.state_file):
        with open(args.state_file, encoding="utf-8") as f:
            state = json.load(f)
    entry = state.get(sid, {})
    return {"agent_id": entry.get("agent_id"), "agent_type": entry.get("agent_type")}


def read_target(args: argparse.Namespace, payload: dict) -> str:
    ti = payload.get("tool_input") or {}
    return args.path or ti.get("file_path") or ti.get("path") or ti.get("target_file") or ""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B5 写侧校验（PreToolUse deny·主路/退路双形并列缺省主路）")
    ap.add_argument("--input", default=None, help="stdin 不可用时的 PreToolUse payload JSON 文件（测试注入面）")
    ap.add_argument("--path", default=None, help="样例写路径（测试注入面，优先于 payload.tool_input）")
    ap.add_argument("--identity-source", choices=["stdin", "statefile"], default="stdin",
                    help="身份源：stdin＝主路（缺省）；statefile＝退路（候裁 Q-04，须 --state-file）")
    ap.add_argument("--state-file", default=None, help="退路 SubagentStart 状态文件（{session_id:{agent_id,agent_type}}）")
    ap.add_argument("--sentinel", action="store_true",
                    help="活性哨兵注入（liveness-selfcheck.py 专用）：构造必然 deny 并按哨兵事件留痕，仍输出 deny 决策")
    ap.add_argument("--map", default=os.path.join(pack_root(), "config", "seat-permissions-hooks-map.json"))
    ap.add_argument("--leases", default=os.path.join(default_ledger_root(), "leases.jsonl"))
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    ap.add_argument("--freeze-state", default=os.path.join(default_ledger_root(), "freeze-state.json"))
    a = ap.parse_args(argv)

    payload: dict = {}
    if a.input:
        with open(a.input, encoding="utf-8") as f:
            payload = json.load(f)
    elif not sys.stdin.isatty():
        raw = sys.stdin.read().strip()
        if raw:
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                payload = {}

    identity = read_identity(a, payload)
    target = read_target(a, payload)
    if a.sentinel and not target:
        target = ".collab/liveness/sentinel-write"  # 必中事件：哨兵路径无租约可命中→必 deny

    if not target:
        print("REJECT: 写目标路径缺席（fail-closed）", file=sys.stderr)
        print(deny_output("写目标路径缺席→deny"))
        return 0

    allow, reason = decide(identity, target, a.map, a.leases, a.freeze_state)
    if allow:
        # 词表内不自造 allow 输出：无决策输出＝不干预
        print(f"ALLOW write-guard path={normalize_path(target)}: {reason}", file=sys.stderr)
        return 0

    event = "liveness_sentinel" if a.sentinel else "write_deny"
    seat = seat_of(identity.get("agent_type"), identity.get("agent_id"),
                   load_map(a.map).get("agent_type_to_seat", {}))
    record_deny(a.ledger, seat, identity, target, reason, event=event)
    print(deny_output(reason))
    return 0


if __name__ == "__main__":
    sys.exit(main())
