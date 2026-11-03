#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S4 施工测试实体 · 强制机制群（B5/B7/B8/B10/B11）——三段式（表2-2）。

本件居交付树 tests（deliverables/**/tests/**＝施工与验收测试实体·判据真源双层双址条款）。
覆盖票面判据：1 hooks 两键结构；2 deny 冒烟（无租约写→permissionDecision deny）；
3 orphan/amend/rebase 三形态 exit=2；4 活性自检正反两态；5 freeze 动作链三步＋≤60s；
6 B11 引用扫描命中；7 sign-verify fail-closed 两读数；9 派生一致性断言
（seat-permissions-hooks-map deny_globs 席位集 ⊆ seat-permissions 席位集且每席位非空）。
运行落盘一律 Temp 重定向，仓内零残留。
"""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.dirname(os.path.dirname(HERE))                       # baigong-software-team
SCRIPTS = os.path.join(PACK, "skills", "sop", "scripts")
CONFIG = os.path.join(PACK, "config")
HOOKS = os.path.join(PACK, "hooks", "hooks.json")


def load_script(name: str):
    path = os.path.join(SCRIPTS, name)
    spec = importlib.util.spec_from_file_location(name.replace("-", "_").replace(".py", ""), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


wg = load_script("write-guard.py")
ca = load_script("commit-audit.py")
mn = load_script("memory-neutralize.py")


def read_ledger(path: str) -> list[dict]:
    out = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    out.append(json.loads(line))
    return out


# ---- 判据 1：hooks.json 结构（PreToolUse/PostToolUse 两键） ----
def t01_hooks_two_keys(tmp: str) -> None:
    with open(HOOKS, encoding="utf-8") as f:
        h = json.load(f)
    assert h, "hooks.json 非法 JSON 或空"
    hb = h.get("hooks", h)
    assert "PreToolUse" in hb and "PostToolUse" in hb


# ---- 判据 2：无租约状态样例写请求 → deny 输出 ----
def t02_deny_smoke_no_lease(tmp: str) -> None:
    led, leases = os.path.join(tmp, "led.jsonl"), os.path.join(tmp, "leases.jsonl")
    r = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, "write-guard.py"),
         "--path", "docs/should-not-write.md", "--ledger", led, "--leases", leases,
         "--freeze-state", os.path.join(tmp, "freeze-state.json")],
        input=json.dumps({"agent_type": "software-engineer", "agent_id": "eng-x",
                          "tool_input": {"file_path": "docs/should-not-write.md"}}),
        capture_output=True, text=True)
    assert '"permissionDecision":"deny"' in r.stdout, r.stdout + r.stderr
    deny_recs = [x for x in read_ledger(led) if x["payload"].get("event") == "write_deny"]
    report_recs = [x for x in read_ledger(led)
                   if x["payload"].get("trigger_source") == "租约越界deny"]
    assert len(deny_recs) == 1 and len(report_recs) == 1  # deny 留痕＋呈报码各恰一


def t03_lease_allow_and_deny_globs(tmp: str) -> None:
    """租约内路径放行＋deny_globs 命中拒（表2-1 不可写列消费面）。"""
    led, leases = os.path.join(tmp, "led.jsonl"), os.path.join(tmp, "leases.jsonl")
    os.makedirs(os.path.dirname(leases), exist_ok=True)
    with open(leases, "w", encoding="utf-8") as f:
        f.write(json.dumps({"ts": "t", "lease": {"ticket_id": "SWB-T99", "seat_id": "engineer",
                                                 "path_globs": ["deliverables/**"], "hash": "h"}},
                            ensure_ascii=False) + "\n")
    env_in = json.dumps({"agent_type": "software-engineer", "agent_id": "eng-x"})
    r_allow = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, "write-guard.py"),
         "--path", "deliverables/experts/baigong-software-team/x.py",
         "--ledger", led, "--leases", leases,
         "--freeze-state", os.path.join(tmp, "freeze-state.json")],
        input=env_in, capture_output=True, text=True)
    assert '"permissionDecision"' not in r_allow.stdout  # 放行＝不干预
    r_deny = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, "write-guard.py"),
         "--path", "tests/root-judgement-truth.py",  # 仓根 tests/∈engineer deny_globs
         "--ledger", led, "--leases", leases,
         "--freeze-state", os.path.join(tmp, "freeze-state.json")],
        input=env_in, capture_output=True, text=True)
    assert '"permissionDecision":"deny"' in r_deny.stdout


def t04_statefile_fallback_same_decision(tmp: str) -> None:
    """退路形态（SubagentStart 状态文件）同判据交付——缺省不启用，显式参数可选（候裁 Q-04 双形）。"""
    led, leases = os.path.join(tmp, "led.jsonl"), os.path.join(tmp, "leases.jsonl")
    sf = os.path.join(tmp, "subagent-state.json")
    with open(sf, "w", encoding="utf-8") as f:
        json.dump({"sess-1": {"agent_id": "eng-1", "agent_type": "software-engineer"}}, f)
    r = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, "write-guard.py"),
         "--identity-source", "statefile", "--state-file", sf,
         "--path", "docs/x.md", "--ledger", led, "--leases", leases,
         "--freeze-state", os.path.join(tmp, "freeze-state.json")],
        input=json.dumps({"session_id": "sess-1"}), capture_output=True, text=True)
    assert '"permissionDecision":"deny"' in r.stdout, r.stdout + r.stderr


# ---- 判据 3：orphan／amend／rebase 各 exit=2 ----
def t05_orphan_amend_rebase_exit2(tmp: str) -> None:
    led = os.path.join(tmp, "led.jsonl")
    cases = [
        "git commit -m 'plain message without any ticket id'",           # orphan
        "git commit --amend -m 'SWB-T04 fix'",                            # amend
        "git rebase -i main",                                             # rebase
    ]
    for cmd in cases:
        rc = ca.main(["prehook", "--command", cmd, "--ledger", led])
        assert rc == 2, f"cmd={cmd!r} rc={rc} ≠ 2"
    blocks = [x for x in read_ledger(led) if x["payload"].get("event") == "commit_audit_block"]
    assert len(blocks) == 3
    # 合法提交命令不误拦
    assert ca.main(["prehook", "--command", "git commit -m 'collab: SWB-T04 smoke'", "--ledger", led]) == 0


def t06_force_push_blocked(tmp: str) -> None:
    """B0 退路补位面：force-push 命令拦截（P7 pass 下同交付补位）。"""
    led = os.path.join(tmp, "led.jsonl")
    rc = ca.main(["prehook", "--command", "git push --force origin main", "--ledger", led])
    assert rc == 2


# ---- 判据 4：活性自检正反两态 ----
def t07_liveness_pass_and_fail(tmp: str) -> None:
    led = os.path.join(tmp, "led.jsonl")
    hooks_off = os.path.join(tmp, "hooks-disabled.json")
    r_pass = subprocess.run([sys.executable, os.path.join(SCRIPTS, "liveness-selfcheck.py"),
                             "--ledger", led, "--hooks", HOOKS], capture_output=True, text=True)
    assert r_pass.returncode == 0, r_pass.stdout + r_pass.stderr
    fails_before = len([x for x in read_ledger(led)
                        if x["payload"].get("trigger_source") == "活性自检失败"])
    with open(hooks_off, "w", encoding="utf-8") as f:
        json.dump({"hooks": {"PreToolUse": []}}, f)  # 停用＝write-guard 路由不在册
    r_fail = subprocess.run([sys.executable, os.path.join(SCRIPTS, "liveness-selfcheck.py"),
                             "--ledger", led, "--hooks", hooks_off], capture_output=True, text=True)
    assert r_fail.returncode != 0
    fails_after = [x for x in read_ledger(led)
                   if x["payload"].get("trigger_source") == "活性自检失败"]
    assert len(fails_after) == fails_before + 1  # 新增恰 1 条


# ---- 判据 5：freeze 动作链三步＋自计时≤60s ----
def t08_freeze_chain_within_60s(tmp: str) -> None:
    led = os.path.join(tmp, "led.jsonl")
    leases = os.path.join(tmp, "leases.jsonl")
    fs = os.path.join(tmp, "freeze-state.json")
    with open(leases, "w", encoding="utf-8") as f:
        f.write(json.dumps({"lease": {"ticket_id": "SWB-T99", "seat_id": "engineer",
                                      "path_globs": ["deliverables/**"], "hash": "h"}}, ensure_ascii=False) + "\n")
    r = subprocess.run([sys.executable, os.path.join(SCRIPTS, "freeze-unfreeze.py"), "freeze",
                        "--ledger", led, "--leases", leases, "--freeze-state", fs],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "elapsed=" in r.stdout and "OK ≤时限" in r.stdout  # 自计时回显
    with open(fs, encoding="utf-8") as f:
        st = json.load(f)
    assert st["frozen"] and st["deny_all_writes"]
    cleared = [json.loads(l) for l in open(leases, encoding="utf-8") if l.strip()]
    assert any(c.get("cleared") for c in cleared)  # ①清租约
    # freeze 联动：写侧全 deny
    w = subprocess.run([sys.executable, os.path.join(SCRIPTS, "write-guard.py"),
                        "--path", "deliverables/experts/baigong-software-team/a.py",
                        "--ledger", led, "--leases", leases, "--freeze-state", fs],
                       input=json.dumps({"agent_type": "software-engineer"}),
                       capture_output=True, text=True)
    assert '"permissionDecision":"deny"' in w.stdout
    # 解冻无人类令牌→拒（脚本不得自触发·表2-2 V13 L98）
    u = subprocess.run([sys.executable, os.path.join(SCRIPTS, "freeze-unfreeze.py"), "unfreeze",
                        "--ledger", led, "--leases", leases, "--freeze-state", fs,
                        "--token-anchor", os.path.join(tmp, "no-anchor")],
                       capture_output=True, text=True)
    assert u.returncode != 0


def t09_unfreeze_with_human_token(tmp: str) -> None:
    led, leases, fs = (os.path.join(tmp, "led.jsonl"), os.path.join(tmp, "leases.jsonl"),
                       os.path.join(tmp, "freeze-state.json"))
    anchor = os.path.join(tmp, "anchors")
    import hashlib as _h
    token = "human-token-xyz"
    with open(anchor, "w", encoding="utf-8") as f:
        f.write(_h.sha256(token.encode()).hexdigest() + "\n")
    subprocess.run([sys.executable, os.path.join(SCRIPTS, "freeze-unfreeze.py"), "freeze",
                    "--ledger", led, "--leases", leases, "--freeze-state", fs], check=True,
                   capture_output=True)
    u = subprocess.run([sys.executable, os.path.join(SCRIPTS, "freeze-unfreeze.py"), "unfreeze",
                        "--human-token", token, "--token-anchor", anchor,
                        "--ledger", led, "--leases", leases, "--freeze-state", fs],
                       capture_output=True, text=True)
    assert u.returncode == 0, u.stdout + u.stderr
    with open(fs, encoding="utf-8") as f:
        assert json.load(f)["deny_all_writes"] is False


# ---- 判据 6：B11 下游件含记忆路径引用 → 命中码回显 ----
def t10_memory_ref_scan_hit(tmp: str) -> None:
    led = os.path.join(tmp, "led.jsonl")
    victim = os.path.join(tmp, "downstream-note.md")
    with open(victim, "w", encoding="utf-8") as f:
        f.write("# 下游件\n\n依据 memory/session-recap.md 的既有结论继续。\n")
    r = subprocess.run([sys.executable, os.path.join(SCRIPTS, "memory-neutralize.py"), "scan",
                        "--files", victim, "--ledger", led], capture_output=True, text=True)
    assert "引用扫描命中" in r.stdout, r.stdout + r.stderr
    hits = [x for x in read_ledger(led) if x["payload"].get("trigger_source") == "引用扫描命中"]
    assert len(hits) == 1


def t11_memory_read_flag(tmp: str) -> None:
    """面①：记忆读取→ask 标（§19 词表既有值；不声明阻断保证）。"""
    led = os.path.join(tmp, "led.jsonl")
    r = subprocess.run([sys.executable, os.path.join(SCRIPTS, "memory-neutralize.py"), "prehook",
                        "--path", "memory/session-recap.md", "--ledger", led],
                       input="{}", capture_output=True, text=True)
    assert '"permissionDecision":"ask"' in r.stdout


# ---- 判据 7：sign-verify fail-closed 两读数 ----
def t12_sign_verify_fail_closed(tmp: str) -> None:
    led = os.path.join(tmp, "led.jsonl")
    signed, sig = os.path.join(tmp, "review.md"), os.path.join(tmp, "review.md.sig")
    with open(signed, "w", encoding="utf-8") as f:
        f.write("人类评审件样例\n")
    with open(sig, "w", encoding="utf-8") as f:
        f.write("not a real signature\n")
    # 读数①：伪造签名 → exit≠0
    r1 = subprocess.run([sys.executable, os.path.join(SCRIPTS, "sign-verify.py"),
                         "--signed", signed, "--signature", sig,
                         "--identity-anchor", os.path.join(tmp, "anchor"), "--ledger", led],
                        capture_output=True, text=True)
    assert r1.returncode != 0
    # 读数②：gpg 缺失环境 → exit≠0 硬失败
    fake_missing = os.path.join(tmp, "definitely-not-gpg.exe")
    r2 = subprocess.run([sys.executable, os.path.join(SCRIPTS, "sign-verify.py"),
                         "--signed", signed, "--signature", sig, "--gpg", fake_missing,
                         "--ledger", led], capture_output=True, text=True)
    assert r2.returncode != 0 and "硬失败" in (r2.stderr + r2.stdout)
    fails = [x for x in read_ledger(led) if x["payload"].get("event") == "verify_fail"]
    assert len(fails) == 2  # 两读数均落验签记录


# ---- 判据 9：派生一致性断言 ----
def t13_derived_consistency(tmp: str) -> None:
    with open(os.path.join(CONFIG, "seat-permissions.json"), encoding="utf-8") as f:
        src = json.load(f)
    with open(os.path.join(CONFIG, "seat-permissions-hooks-map.json"), encoding="utf-8") as f:
        m = json.load(f)
    src_seats = {s["seat_id"] for s in src["seats"]}
    map_seats = {s["seat_id"] for s in m["seats"]}
    assert map_seats <= src_seats, f"席位集 {map_seats} ⊄ 源席位集 {src_seats}"
    src_deny = {s["seat_id"]: s.get("deny_globs", []) for s in src["seats"]}
    for row in m["seats"]:
        assert row["deny_globs"], f"席位 {row['seat_id']} deny_globs 为空"
        assert row["deny_globs"] == src_deny[row["seat_id"]], \
            f"席位 {row['seat_id']} deny_globs 与源件不一致（派生面禁改写）"
    assert m.get("derived_from", "").startswith("seat-permissions.json"), "头部 derived_from 注缺席"


def run_self() -> int:
    tests = [t01_hooks_two_keys, t02_deny_smoke_no_lease, t03_lease_allow_and_deny_globs,
             t04_statefile_fallback_same_decision, t05_orphan_amend_rebase_exit2,
             t06_force_push_blocked, t07_liveness_pass_and_fail, t08_freeze_chain_within_60s,
             t09_unfreeze_with_human_token, t10_memory_ref_scan_hit, t11_memory_read_flag,
             t12_sign_verify_fail_closed, t13_derived_consistency]
    for t in tests:
        with tempfile.TemporaryDirectory() as tmp:
            t(tmp)
        print(f"PASS {t.__name__}")
    return 0


def main() -> int:
    return run_self()


if __name__ == "__main__":
    sys.exit(main())
