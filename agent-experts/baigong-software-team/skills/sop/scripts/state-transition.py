#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T02-C · B2 状态机（状态迁移/登记/记账·零裁量）

规范锚点：架构 v2.9 §4 生命周期（节点 1 需求→2 设计→3 拆票→4 执行→5 发布→6 灰度）＋挂起态（§17）；
表2-3 六节点签字行（缺一拒迁并写「呈报」类审计事件）；§18⑩ 定级确认前置签收（P0/P1 缺陷票链
进入/离开 4 执行的迁移，定级未确认 exit≠0；定级权限归 QA 双复核＋人类终裁，本脚本只校验签收字段在位、不判级）；
§13 timeouts 缺省＝工程师票 48h／呈报 24h（未配置项＝不适用）；§9 B2 紧急停票＝人类直通入口迁「挂起」写「呈报」留痕。
触发源六闭集见 §4/§13。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

# ---- 状态集（§4＋§17 挂起）----
NODES = {1: "需求", 2: "设计", 3: "拆票", 4: "执行", 5: "发布", 6: "灰度"}
HOLD = "挂起"
DONE = "完结"
LEGAL_FORWARD = {(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, DONE)}
LEGAL_HOLD_IN = set(NODES) | {DONE}          # 任意在制/完结态可被人类直通入口迁「挂起」
LEGAL_HOLD_OUT = set(NODES)                  # 解冻仅回节点态（解冻权人类唯一·§17）

# ---- 迁移合法性表：前进迁移＝离开节点 N，须核表2-3 节点 N 签字集合（缺一拒迁）----
SIGNSETS = {
    1: ["产品交付签", "架构PRD接收签", "QA可验收性签"],
    2: ["架构交付签", "QA质量属性审计签"],
       3: ["架构生成签", "产品范围签", "QA充分性签"],
    4: ["工程师交付签", "QA审计签"],
    5: ["产品签", "release-qa签", "集成验收结论", "引用继承"],
    6: ["full-rollout（QA按声明判据单签）"],
}

# ---- 定级确认前置签收（§18⑩随动）：缺陷票链＝进入/离开 4 执行的迁移 ----
DEFECT_CHAIN = {(3, 4), (4, 5)}
DEFECT_TICKET_TYPE = "缺陷"                  # 票型八类之缺陷（§3）
GRADES_REQUIRING_CONFIRM = {"P0", "P1"}      # 定级权限归 QA 双复核＋人类终裁（表2-2），本脚本不判级

# ---- 触发源六闭集（§4/§13）----
TRIGGER_SOURCES = ["租约越界deny", "对账差≠0", "活性自检失败", "引用扫描命中", "超期", "熔断"]

# ---- 回流件四型闭集（§3）----
RETURN_TYPES = ["完成", "部分完成", "受阻", "异常"]  # §3 回流件四型闭集（V13 L113·物理 L141）

# ---- timeouts 缺省（§13；未配置项＝不适用）----
TIMEOUT_DEFAULTS = {"工程师票": 48.0, "呈报": 24.0}


def default_ledger_root() -> str:
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(os.getcwd(), ".collab", "ledger"))


def canonical_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def append_record(ledger_file: str, rtype: str, actor: str, payload: dict) -> dict:
    """append-only 追加账本记录（六类记录·§3；prev_hash 仅供单记录独立校验）。"""
    os.makedirs(os.path.dirname(ledger_file), exist_ok=True)
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


def load_states(states_file: str) -> dict:
    if os.path.exists(states_file):
        with open(states_file, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_states(states_file: str, states: dict) -> None:
    os.makedirs(os.path.dirname(states_file), exist_ok=True)
    with open(states_file, "w", encoding="utf-8") as f:
        json.dump(states, f, ensure_ascii=False, indent=2)


def load_timeouts(timeouts_file: str | None) -> dict:
    cfg = dict(TIMEOUT_DEFAULTS)
    if timeouts_file and os.path.exists(timeouts_file):
        with open(timeouts_file, encoding="utf-8") as f:
            cfg.update(json.load(f))
    return cfg


def transition(ticket_id: str, src, dst, *, kind: str, signs: list[str],
               ticket_type: str | None, severity: str | None, severity_confirmed: bool,
               human_direct: bool, ledger_file: str, states_file: str,
               trigger_source: str | None = None,
               return_type: str | None = None) -> int:
    """合法迁移→写对应记录类（派发/签字）并回显；非法迁移→写「呈报」类审计事件并 exit≠0。"""
    states = load_states(states_file)
    timeouts = load_timeouts(os.environ.get("SWB_TIMEOUTS_FILE"))
    current = states.get(ticket_id)

    # 无状态票：仅允许「建立于节点 1 需求」（首次派发），其余按当前态核
    if current is None:
        if src == 1 and dst == 1:
            states[ticket_id] = {"state": 1, "ticket_type": ticket_type}
            save_states(states_file, states)
            rec = append_record(ledger_file, "派发", "state-transition.py",
                                {"event": "ticket_established", "ticket_id": ticket_id,
                                 "state": 1, "ticket_type": ticket_type,
                                 "timeout_hours": timeouts.get(ticket_type if ticket_type in timeouts else "工程师票")})
            print(f"OK established ticket={ticket_id} state=1(需求) ledger_hash={rec['hash']}")
            return 0
        return _reject(ledger_file, ticket_id, src, dst, "未知票据无当前状态（仅允许建立于节点1）", trigger_source)

    cur_state = current["state"]
    if cur_state != src:
        return _reject(ledger_file, ticket_id, src, dst, f"当前态={cur_state} 与请求离开态={src} 不符", trigger_source)

    # 挂起/解冻（§9 B2 紧急停票＝人类直通入口；解冻权人类唯一·§17）
    if dst == HOLD:
        if cur_state not in LEGAL_HOLD_IN:
            return _reject(ledger_file, ticket_id, src, dst, f"{cur_state}→挂起 不在合法性表", trigger_source)
        if not human_direct:
            return _reject(ledger_file, ticket_id, src, dst, "迁挂起仅人类直通入口可触发（脚本不得自触发）", trigger_source)
        states[ticket_id] = {"state": HOLD, "held_from": cur_state, "ticket_type": current.get("ticket_type")}
        save_states(states_file, states)
        rec = append_record(ledger_file, "呈报", "state-transition.py",
                            {"event": "emergency_hold", "ticket_id": ticket_id,
                             "from": cur_state, "to": HOLD, "note": "人类指令留痕，不入触发源闭集（§9 B2）"})
        print(f"OK held ticket={ticket_id} ledger_hash={rec['hash']}")
        return 0
    if cur_state == HOLD:
        if not human_direct:
            return _reject(ledger_file, ticket_id, src, dst, "挂起解冻权人类唯一（§17）", trigger_source)
        if dst not in LEGAL_HOLD_OUT:
            return _reject(ledger_file, ticket_id, src, dst, f"挂起→{dst} 不在合法性表", trigger_source)
        states[ticket_id] = {"state": dst, "ticket_type": current.get("ticket_type")}
        save_states(states_file, states)
        rec = append_record(ledger_file, "签字", "state-transition.py",
                            {"event": "unfreeze", "ticket_id": ticket_id, "from": HOLD, "to": dst})
        print(f"OK unfrozen ticket={ticket_id} state={dst} ledger_hash={rec['hash']}")
        return 0

    # 定级确认前置签收（§18⑩）：缺陷票链迁移且 P0/P1 定级未确认→拒
    if ticket_type == DEFECT_TICKET_TYPE and (src, dst) in DEFECT_CHAIN \
            and (severity or "") in GRADES_REQUIRING_CONFIRM and not severity_confirmed:
        return _reject(ledger_file, ticket_id, src, dst,
                       f"定级确认前置签收缺席：{severity} 级缺陷票链迁移 {src}→{dst} 候「定级确认」签收（定级权＝QA双复核＋人类终裁，本脚本不判级）",
                       trigger_source)

    # 前进迁移合法性＋签字集合校验（表2-3 离开节点 N 的签字行）
    if (src, dst) not in LEGAL_FORWARD:
        return _reject(ledger_file, ticket_id, src, dst, f"迁移 {src}→{dst} 不在合法性表（前进链单向）", trigger_source)
    required = SIGNSETS.get(src, [])
    missing = [s for s in required if s not in signs]
    if missing:
        return _reject(ledger_file, ticket_id, src, dst, f"签字集合缺席：{missing}", trigger_source)

    # 回流四型标签校验（§3 闭集机械化·SWB-T07-C）：4→5 必填、非回流迁移禁挂
    if (src, dst) == (4, 5) and return_type is None:
        return _reject(ledger_file, ticket_id, src, dst,
                       "4→5 回流迁移缺 return_type（回流四型闭集 {完成,部分完成,受阻,异常}·§3）", trigger_source)
    if (src, dst) != (4, 5) and return_type is not None:
        return _reject(ledger_file, ticket_id, src, dst,
                       "return_type 只许挂 4→5 回流迁移（防误挂·回流四型闭集 {完成,部分完成,受阻,异常}·§3）", trigger_source)

    states[ticket_id] = {"state": dst, "ticket_type": current.get("ticket_type")}
    save_states(states_file, states)
    rtype = "签字" if kind == "signoff" else "派发"
    rec = append_record(ledger_file, rtype, "state-transition.py",
                        {"event": "transition", "ticket_id": ticket_id, "from": src, "to": dst,
                         "kind": kind, "signs": signs,
                         "return_type": return_type if (src, dst) == (4, 5) else None,
                         "grade_confirm": (severity or "") if (ticket_type == DEFECT_TICKET_TYPE and (src, dst) in DEFECT_CHAIN) else None,
                         "severity_confirmed": severity_confirmed if (ticket_type == DEFECT_TICKET_TYPE and (src, dst) in DEFECT_CHAIN) else None})
    print(f"OK transition ticket={ticket_id} {src}({NODES.get(src, src)})→{dst}({NODES.get(dst, dst)}) record_type={rtype} ledger_hash={rec['hash']}")
    return 0


def _reject(ledger_file: str, ticket_id: str, src, dst, reason: str, trigger_source: str | None) -> int:
    payload = {"event": "audit_transition_rejected", "ticket_id": ticket_id, "from": src, "to": dst,
               "reject_reason": reason}
    if trigger_source is not None:
        if trigger_source not in TRIGGER_SOURCES:
            print(f"REJECT: 触发源越出六闭集 {TRIGGER_SOURCES}", file=sys.stderr)
            return 3
        payload["trigger_source"] = trigger_source
    append_record(ledger_file, "呈报", "state-transition.py", payload)
    print(f"REJECT ticket={ticket_id} {src}→{dst}: {reason}", file=sys.stderr)
    return 2


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="B2 状态迁移（零裁量·非法迁移 exit≠0＋呈报留痕）")
    ap.add_argument("--ticket", required=True)
    ap.add_argument("--from", dest="src", required=True, help="离开态（1-6/挂起）")
    ap.add_argument("--to", dest="dst", required=True, help="目标态（1-6/挂起/完结）")
    ap.add_argument("--kind", choices=["dispatch", "signoff"], default="dispatch")
    ap.add_argument("--sign", action="append", default=[], help="签字名（可重复；按表2-3 签字集合核）")
    ap.add_argument("--ticket-type", default=None, help="票型八类之一（§3）")
    ap.add_argument("--severity", default=None, help="缺陷定级（P0/P1/P2…）——本脚本不判级，只读签收字段")
    ap.add_argument("--severity-confirmed", action="store_true", help="定级确认前置签收字段在位（§18⑩）")
    ap.add_argument("--human-direct", action="store_true", help="人类直通入口标记（挂起/解冻专用）")
    ap.add_argument("--trigger-source", default=None, help="审计事件触发源（六闭集内）")
    ap.add_argument("--return-type", default=None, choices=RETURN_TYPES, help="回流四型标签（4→5 必填·§3 闭集）")
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    ap.add_argument("--states", default=os.path.join(default_ledger_root(), "states.json"))
    a = ap.parse_args(argv)

    def norm(v: str):
        return int(v) if v.isdigit() else v

    return transition(a.ticket, norm(a.src), norm(a.dst), kind=a.kind, signs=a.sign,
                      ticket_type=a.ticket_type, severity=a.severity,
                      severity_confirmed=a.severity_confirmed, human_direct=a.human_direct,
                      ledger_file=a.ledger, states_file=a.states, trigger_source=a.trigger_source,
                      return_type=a.return_type)


if __name__ == "__main__":
    sys.exit(main())
