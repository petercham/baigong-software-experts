#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SWB-T06-B · 三指标＋阶段终点机械面（消费面声明⑦⑨落点·双臂之一·CI 臂）

规范锚点（落笔前已回原文核对）：
- 产品设计 v2.9 §4 三指标（V13 L21＝登记件落盘物理 L49）：
  ①Hooks 拦截数＝deny 事件计数（含活性自检核验联动）；
  ②派发互验差异率（阈值 2%，分子分母口径见架构§13；超限＝触发指标异常处置——
    停用手拼强制 B3＋呈报人类，见架构§13/§14；不与熔断混用，熔断闭集另见架构§13）；
  ③路由纠正率（语义健康度观测，明示不机械化）→ 本脚本只输出 manual_observation 标记行，不产自动判定。
- 阶段终点（V13 L22＝物理 L50）：α＝7 日＋六条演练全绿→呈报决策者知悉（主理人登记·非签字）；
  β＝2 周指标全绿→呈报知悉（非签字）；γ＝4 周无熔断升级→收口→门二·上线交付前放行（人类签字）。
  判定读账本读数，输出三态 met/not-met/pending；呈拍/签字动作权在人类面，本脚本只出读数。
- 架构 §13（V13 L186＝物理 L214）成值全部读 config/thresholds.json（T06-A 件），不在本件内写死成值。
- 混用隔离硬条款（票面施工规格 T06-B）：指标异常路径与熔断路径＝两独立函数、代码分离、
  输出码互斥；混用即红项。表2-2（V13 L98）「冻结/解冻/吊销发起＝人类直通触点｜B10（脚本不得自触发）」
  → 熔断命中只输出冻结呈报码，不调用 freeze-unfreeze.py。

差异率口径（§13 逐字段化，thresholds.json.diff_rate_formula）：
  分子分量事件映射（账本六类记录·B3/B8 既有落盘事件名）：
    agent_id_mismatch  ← 派发记录 event=dispatch_rejected_agent_mismatch（dispatch-builder.py）
    whitelist_superset ← 呈报记录 event=injection_superset_reject（dispatch-builder.py）
    pack_hash_mismatch ← 呈报记录 event=pack_hash_mismatch（B8 重放差异第三分类/QA 抽样比对入账）
  分母 completed_dispatch_count ← 派发记录 event=dispatch_built 计数（实际完成派发次数）。

运行落盘一律可重定向：--ledger/--thresholds/--selftest 样区居仓外 Temp；仓内零运行残留。
本脚本＝生成方产出，不自判合格（制度③）——结论权归 QA/CI 面。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

# ---- 口径常量（事件名真源＝T03/T04 落盘形态；成值真源＝thresholds.json） ----
COMPONENT_EVENTS = {
    "agent_id_mismatch": ("派发", "dispatch_rejected_agent_mismatch"),
    "whitelist_superset": ("呈报", "injection_superset_reject"),
    "pack_hash_mismatch": ("呈报", "pack_hash_mismatch"),
}
DENOM_EVENT = ("派发", "dispatch_built")
DENY_EVENTS = {"write_deny", "liveness_sentinel"}          # 指标①：deny 事件
TRIG_LIVENESS_FAIL = "活性自检失败"                         # §13 指标异常闭集第二项
FUSE_MARKER = "FUSE_FREEZE_REPORT"                          # 熔断路径输出码
ANOMALY_MARKER = "METRIC_ANOMALY"                           # 指标异常路径输出码
ANOMALY_HANDLING = "停用手拼强制 B3＋呈报人类（架构§13/§14）"
FUSE_HANDLING = "冻结呈报码输出（冻结发起权＝人类直通触点·表2-2 V13 L98；本脚本只呈报不自触发）"

EXIT_USAGE = 2


def pack_root() -> str:
    # 本件居 tests/acceptance/ 下，上溯三级＝包根 .../baigong-software-team
    d = os.path.abspath(__file__)
    for _ in range(3):
        d = os.path.dirname(d)
    return d


def default_ledger_root() -> str:
    return os.environ.get("SWB_LEDGER_ROOT", os.path.join(os.getcwd(), ".collab", "ledger"))


def canonical_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def read_records(path: str) -> list[dict]:
    out: list[dict] = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    out.append(json.loads(line))
    return out


def append_record(ledger_file: str, rtype: str, actor: str, payload: dict) -> dict:
    """append-only 追加（与 B2/B3/B5 同形制）；仅 --construct-sample 样区写入用。"""
    os.makedirs(os.path.dirname(os.path.abspath(ledger_file)), exist_ok=True)
    prev_hash, seq = "GENESIS", 0
    for rec in read_records(ledger_file):
        prev_hash, seq = rec["hash"], rec["seq"]
    rec = {"seq": seq + 1,
           "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "type": rtype, "actor": actor, "payload": payload, "prev_hash": prev_hash}
    rec["hash"] = hashlib.sha256(
        f'{rec["seq"]}\n{rec["ts"]}\n{rec["type"]}\n{rec["actor"]}\n'
        f'{canonical_json(rec["payload"])}\n{prev_hash}'.encode("utf-8")).hexdigest()
    with open(ledger_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def load_thresholds(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ================= 指标① Hooks 拦截数（deny 事件计数·含活性自检核验联动） =================
def metric_hooks_deny(records: list[dict]) -> dict:
    deny = sum(1 for r in records
               if r["type"] == "写入" and r["payload"].get("event") in DENY_EVENTS)
    sentinel = sum(1 for r in records
                   if r["type"] == "写入" and r["payload"].get("event") == "liveness_sentinel")
    liveness_fail = sum(1 for r in records
                        if r["payload"].get("trigger_source") == TRIG_LIVENESS_FAIL)
    linkage = "fail" if liveness_fail else ("pass" if sentinel else "no-sentinel-evidence")
    return {"hooks_deny_count": deny, "liveness_sentinel_count": sentinel,
            "liveness_fail_reports": liveness_fail, "liveness_linkage": linkage}


# ================= 指标② 派发互验差异率（§13 口径·异常路径独立函数） =================
def diff_rate_components(records: list[dict]) -> dict:
    counts: dict[str, int] = {}
    for comp, (rtype, event) in COMPONENT_EVENTS.items():
        counts[comp] = sum(1 for r in records
                           if r["type"] == rtype and r["payload"].get("event") == event)
    denom = sum(1 for r in records
                if r["type"] == DENOM_EVENT[0] and r["payload"].get("event") == DENOM_EVENT[1])
    return {"numerator_by_component": counts, "numerator_total": sum(counts.values()),
            "completed_dispatch_count": denom,
            "diff_rate": (sum(counts.values()) / denom) if denom else 0.0}


def consecutive_crosscheck_inconsistent(records: list[dict]) -> int:
    """派发互验连续不一致最大连击数（§13 指标异常闭集第三项读数）。"""
    best = run = 0
    for r in records:
        if r["type"] != "派发":
            continue
        ev = r["payload"].get("event")
        if ev == "dispatch_rejected_agent_mismatch":
            run += 1
            best = max(best, run)
        elif ev in ("dispatch_built",):
            run = 0
    return best


def judge_metric_anomaly(records: list[dict], th: dict) -> dict:
    """指标异常判定路径（独立函数 A）：闭集三成员逐判；命中→只走本路径，不触碰熔断。"""
    anomaly_set = th["metric_anomaly_set"]
    dr = diff_rate_components(records)
    hits: list[str] = []
    if dr["diff_rate"] > anomaly_set["diff_rate_gt"]:
        hits.append(f"差异率={dr['diff_rate']:.4f}>{anomaly_set['diff_rate_gt']}")
    m1 = metric_hooks_deny(records)
    if m1["liveness_fail_reports"] > 0:
        hits.append("活性自检失败呈报在册")
    streak = consecutive_crosscheck_inconsistent(records)
    if streak >= anomaly_set["dispatch_crosscheck_consecutive_inconsistent"]:
        hits.append(f"派发互验连续不一致={streak}≥{anomaly_set['dispatch_crosscheck_consecutive_inconsistent']}")
    return {"path": "metric_anomaly", "hit": bool(hits), "hits": hits,
            "components": dr, "max_streak": streak}


def anomaly_output(verdict: dict) -> str:
    """指标异常路径输出码（含处置声明；输出文本内零熔断码）。"""
    return (f"code={ANOMALY_MARKER} hits={verdict['hits']} 处置＝{ANOMALY_HANDLING}")


# ================= 熔断判定独立函数（路径 B·与指标异常代码分离·互斥） =================
def judge_fuse(readings: dict, th: dict) -> dict:
    """熔断闭集另见§13：连续两轮不通过∨退回率>30%（C1 可调）。
    readings 来源＝QA 轮次/退回计数呈报记录（--fuse-readings JSON：{rounds_fail, rollback_rate}）；
    读数缺席＝不适用（不猜）。"""
    fuse = th["fuse_set"]
    hits: list[str] = []
    rounds = readings.get("rounds_fail")
    rate = readings.get("rollback_rate")
    if rounds is not None and rounds >= fuse["consecutive_rounds_fail"]:
        hits.append(f"连续两轮不通过＝rounds_fail={rounds}≥{fuse['consecutive_rounds_fail']}")
    if rate is not None and rate > fuse["rollback_rate_gt"]:
        hits.append(f"退回率={rate}>{fuse['rollback_rate_gt']}")
    return {"path": "fuse", "hit": bool(hits), "hits": hits}


def fuse_output(verdict: dict) -> str:
    """熔断路径输出码（只呈报不自触发；输出文本内零「停用手拼」码）。"""
    return f"code={FUSE_MARKER} hits={verdict['hits']} 处置＝{FUSE_HANDLING}"


# ================= 指标③ 路由纠正率＝明示不机械化（设计原样，不留机械闸） =================
def route_correction_line() -> str:
    return ("route_correction_rate: manual_observation "
            "（产品§4 V13 L21 语义健康度观测·明示不机械化——本脚本不产自动判定，人工观察面归 QA 抽检入册）")


# ================= 阶段终点三态（读账本读数·呈报/签字动作权在人类面） =================
def endpoint_verdicts(records: list[dict], th: dict, fuse_readings: dict) -> dict:
    ts_list = [r.get("ts") for r in records if r.get("ts")]
    span_days = 0.0
    if ts_list:
        try:
            import datetime as _dt
            t0 = _dt.datetime.strptime(min(ts_list), "%Y-%m-%dT%H:%M:%SZ")
            span_days = (_dt.datetime.now(_dt.timezone.utc).replace(tzinfo=None) - t0).total_seconds() / 86400.0
        except ValueError:
            pass
    drill_green = sorted({r["payload"].get("drill_id") for r in records
                          if r["payload"].get("event") == "drill_green"})
    six_green = len([d for d in drill_green if d]) >= 6
    m1 = metric_hooks_deny(records)
    anomaly = judge_metric_anomaly(records, th)
    fuse = judge_fuse(fuse_readings, th)
    out: dict[str, str] = {}
    if span_days < 7:
        out["alpha"] = f"pending（账本跨度 {span_days:.2f}d < 7d；演练证据 {len(drill_green)}/6）"
    else:
        out["alpha"] = ("met（7 日＋六条演练全绿→呈报决策者知悉·主理人登记·非签字）" if six_green
                        else f"not-met（7 日已满，演练全绿证据 {len(drill_green)}/6）")
    if span_days < 14:
        out["beta"] = f"pending（账本跨度 {span_days:.2f}d < 14d）"
    else:
        green = (not anomaly["hit"]) and (m1["liveness_linkage"] != "fail")
        out["beta"] = ("met（2 周指标全绿→呈报知悉·非签字）" if green else "not-met（指标存在异常命中）")
    if span_days < 28:
        out["gamma"] = f"pending（账本跨度 {span_days:.2f}d < 28d）"
    else:
        out["gamma"] = ("met（4 周无熔断升级→收口→候门二·上线交付前放行＝人类签字）"
                        if not fuse["hit"] else "not-met（熔断升级在册）")
    return {"span_days": round(span_days, 2), "drill_green_ids": drill_green,
            "alpha": out["alpha"], "beta": out["beta"], "gamma": out["gamma"]}


# ================= 构造样例面（判据7：差异率分子三分量各一构造样例·计数各 +1） =================
def construct_sample(component: str, ledger_file: str) -> int:
    if component not in COMPONENT_EVENTS:
        print(f"REJECT: 分量 {component!r} 越出分子三闭集 {sorted(COMPONENT_EVENTS)}", file=sys.stderr)
        return EXIT_USAGE
    rtype, event = COMPONENT_EVENTS[component]
    before = diff_rate_components(read_records(ledger_file))["numerator_by_component"][component]
    append_record(ledger_file, rtype, "metrics-gate.py", {
        "event": event, "diff_component": component,
        "source": "T06 判据7 构造样例（分子三分量各一样例）",
        "ticket_id": "T06-CONSTRUCT-SAMPLE",
    })
    after = diff_rate_components(read_records(ledger_file))["numerator_by_component"][component]
    print(f"construct_sample component={component} ledger={ledger_file} "
          f"count_before={before} count_after={after} delta=+{after - before}")
    return 0


# ================= 自测样区（判据2/3；样区落仓外 Temp） =================
def selftest(th_path: str) -> int:
    import tempfile
    tmp = os.path.join(os.environ.get("T06_TMP", tempfile.gettempdir()), "metrics-selftest")
    os.makedirs(tmp, exist_ok=True)
    th = load_thresholds(th_path)
    ok = True

    # 样区 A：差异率超限（三分量各 1，分母 10 → 0.3 > 0.02）
    led_a = os.path.join(tmp, "anomaly-zone-ledger.jsonl")
    open(led_a, "w", encoding="utf-8").close()
    for comp in COMPONENT_EVENTS:
        rtype, event = COMPONENT_EVENTS[comp]
        append_record(led_a, rtype, "selftest", {"event": event, "ticket_id": "SELFTEST-A"})
    for i in range(10):
        append_record(led_a, "派发", "selftest", {"event": "dispatch_built", "ticket_id": f"SELF-A{i}"})
    va = judge_metric_anomaly(read_records(led_a), th)
    out_a = anomaly_output(va)
    # 样区 B：熔断样区（rounds_fail=2；差异率不超限）
    led_b = os.path.join(tmp, "fuse-zone-ledger.jsonl")
    open(led_b, "w", encoding="utf-8").close()
    for i in range(50):
        append_record(led_b, "派发", "selftest", {"event": "dispatch_built", "ticket_id": f"SELF-B{i}"})
    vb = judge_fuse({"rounds_fail": 2, "rollback_rate": 0.0}, th)
    out_b = fuse_output(vb)

    print(f"[selftest·样区A·指标异常路径] {out_a}")
    print(f"[selftest·样区B·熔断路径] {out_b}")
    if not va["hit"] or FUSE_MARKER in out_a or "冻结呈报" in out_a:
        print("SELFTEST FAIL: 样区A 应走指标异常且输出无熔断码", file=sys.stderr)
        ok = False
    if not vb["hit"] or ANOMALY_MARKER in out_b or ANOMALY_HANDLING in out_b:
        print("SELFTEST FAIL: 样区B 应走熔断且输出无手拼禁用码", file=sys.stderr)
        ok = False
    if ok:
        print("MIX_ISOLATION_OK: 两判定路径代码分离·两读数互斥（异常样区无熔断码／熔断样区无手拼禁用码）")
    print(route_correction_line())
    eps = endpoint_verdicts(read_records(led_a), th, {"rounds_fail": 2, "rollback_rate": 0.0})
    for k in ("alpha", "beta", "gamma"):
        print(f"endpoint_{k}: {eps[k]}")
    if not ok:
        return 1
    print("SELFTEST_DONE")
    return 0


# ================= 主入口 =================
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="T06 三指标＋阶段终点机械面（CI 臂·结论权归 QA/CI 面）")
    ap.add_argument("--ledger", default=os.path.join(default_ledger_root(), "ledger.jsonl"))
    ap.add_argument("--thresholds", default=os.path.join(pack_root(), "config", "thresholds.json"))
    ap.add_argument("--fuse-readings", default=None,
                    help="熔断读数 JSON（{rounds_fail, rollback_rate}·QA 轮次/退回计数呈报面；缺席＝不适用）")
    ap.add_argument("--selftest", action="store_true", help="自测样区（仓外 Temp）")
    ap.add_argument("--construct-sample", choices=sorted(COMPONENT_EVENTS), default=None,
                    help="差异率分子三分量构造样例写入 --ledger（判据7 实测面）")
    a = ap.parse_args(argv)

    if a.selftest:
        return selftest(a.thresholds)
    if a.construct_sample:
        return construct_sample(a.construct_sample, a.ledger)

    th = load_thresholds(a.thresholds)
    records = read_records(a.ledger)
    fuse_readings: dict = {}
    if a.fuse_readings and os.path.exists(a.fuse_readings):
        with open(a.fuse_readings, encoding="utf-8") as f:
            fuse_readings = json.load(f)

    m1 = metric_hooks_deny(records)
    print(f"metric1_hooks_deny_count: {m1['hooks_deny_count']} "
          f"(sentinel={m1['liveness_sentinel_count']} linkage={m1['liveness_linkage']})")

    va = judge_metric_anomaly(records, th)
    dr = va["components"]
    print(f"metric2_diff_rate: {dr['diff_rate']:.4f} "
          f"numerator={dr['numerator_total']} by_component={dr['numerator_by_component']} "
          f"denominator={dr['completed_dispatch_count']} threshold={th['diff_rate_threshold']}")
    if va["hit"]:
        print(anomaly_output(va))   # 指标异常路径（独立；此分支零熔断码）
    else:
        print("metric2: within-threshold（指标异常闭集未命中）")

    print(route_correction_line())  # 指标③＝明示不机械化，标记行不产判定

    vb = judge_fuse(fuse_readings, th)
    if fuse_readings:
        if vb["hit"]:
            print(fuse_output(vb))  # 熔断路径（独立；此分支零手拼禁用码）
        else:
            print("fuse: not-hit（熔断闭集未命中）")
    else:
        print("fuse: no-readings（熔断读数缺席＝不适用，不猜）")

    eps = endpoint_verdicts(records, th, fuse_readings)
    for k in ("alpha", "beta", "gamma"):
        print(f"endpoint_{k}: {eps[k]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
