#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SWB-B16-e 对抗样本三形夹具族 · 双向断言（PF-F 向乙＝验收臂＝防「止痛式词面加固」复发判据面）。

本件居交付树 tests（项目根字面 tests/**＝施工与验收测试实体·判据真源双层双址条款）。
三形各一对断言臂（正臂＝在册形态应拦／反臂＝对抗变形应拦或应登记＝禁静默零拦）：
  形一 绕行形态族＝词面变形绕 CMD_PATTERNS 样件→断言＝拦截命中 或 「已知未拦」登记态二者必居其一；
  形二 输入件自写＝自写锚件撞守卫→断言拒（锚自指闭合拒他址）＋台账自写面（cleared 行）可查态在场；
  形三 身份冒用＝伪造 seat／agent_type 自报注入→断言采信面可查态在场（台账归因字段逐枚在册＝B16-f 采信序预置验收臂）。
X3／X4 翻正断言臂（K6 随登在册必带臂·rev-1 勘正②钉死形制＝--leases 注入非真签发沿 s4 t03 先例）：
  X3＝qa 席位注入 tests 桶租约在册路径样件→勘正后真 config allow 直证；X4＝architect 同形；
  工程师对照臂＝租约外路径 deny 存续＝双兜底不扩面；
  负夹具＝勘正前 config 快照注入（qa／architect deny_globs 含 tests/** 字面）＝deny 命中＝断言双向机械可判。
运行落盘一律 Temp／--ledger 重定向，仓内零残留·真账零染。族名＝SWB-B16-e。
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.dirname(os.path.dirname(HERE))                      # baigong-software-team（包根）
SCRIPTS = os.path.join(PACK, "skills", "sop", "scripts")
MAP_AFTER = os.path.join(PACK, "config", "seat-permissions-hooks-map.json")   # 勘正后真值（盘现链上件）

WG = os.path.join(SCRIPTS, "write-guard.py")
CA = os.path.join(SCRIPTS, "commit-audit.py")


def run_wg(tmp: str, argv_extra: list[str], stdin_payload: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, WG, "--ledger", os.path.join(tmp, "led.jsonl"),
         "--leases", os.path.join(tmp, "leases.jsonl"),
         "--freeze-state", os.path.join(tmp, "freeze-state.json")] + argv_extra,
        input=json.dumps(stdin_payload), capture_output=True, text=True)


def write_leases(tmp: str, rows: list[dict]) -> None:
    with open(os.path.join(tmp, "leases.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


# ---- 形一：绕行形态族（词面变形绕 CMD_PATTERNS）＝拦截 或 已知未拦登记 二者必居其一 ----
# 正臂＝在册三形态＋orphan 应拦；反臂＝对抗变形逐枚：命中拦 ∨ 居登记清单＝禁静默零拦。
# 登记清单＝append-only 登记面（本件在册即「已知未拦」登记态＝新形入场即逐枚表态＝止痛式加固防线）。
KNOWN_UNBLOCKED = [
    "git commit --amendend",                    # 伪词尾形＝\b--amend\b 词边界不命中（登记态）
    "GIT=git; $GIT commit --amend",             # 变量间接形＝\bgit\b 后命令词不可解析（登记态）
    "echo git commit --amend | sh",             # 管道生成执行形＝词面居管道左段（登记态）
]


def t01_bypass_forms_blocked_or_registered(tmp: str) -> None:
    import importlib.util
    spec = importlib.util.spec_from_file_location("ca_mod", CA)
    ca = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ca)
    in_register = ["git commit --amend -m 'SWB-B16E x'", "git rebase main",
                   "git push --force origin main"]
    for cmd in in_register:
        assert ca.classify_command(cmd), f"正臂在册形态未拦＝{cmd!r}"
    adversarial = in_register + KNOWN_UNBLOCKED + [
        "git  commit    --amend -m 'x'",        # 多空格形＝应命中（非登记面）
        "git commit \"--amend\" -m 'x'",        # 引号包裹形＝应命中（非登记面）
    ]
    must_hit = adversarial + KNOWN_UNBLOCKED
    for cmd in must_hit:
        hits = ca.classify_command(cmd)
        registered = cmd in KNOWN_UNBLOCKED
        assert hits or registered, f"静默零拦违例＝既未拦也未登记：{cmd!r}"


# ---- 形二：输入件自写＝自写锚件撞守卫（锚他址＝拒·锚自指＝采信可查）＋台账自写面可查 ----
def t02_selfwritten_anchor_rejected_and_ledger_state_visible(tmp: str) -> None:
    import importlib.util
    spec = importlib.util.spec_from_file_location("wg_mod", WG)
    wg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(wg)
    pack = wg.pack_root()
    # 反臂＝自写锚件指向他处＝自指闭合不成立＝拒采信
    evil = os.path.join(tmp, "evil-root")
    os.makedirs(os.path.join(evil, ".workbuddy"), exist_ok=True)
    with open(os.path.join(evil, ".workbuddy", "swb-anchor"), "w", encoding="utf-8") as f:
        f.write("project_root: C:/definitely-elsewhere\n")
    assert not wg._anchor_hit(evil, pack), "他址锚件被采信＝自指闭合守卫失守"
    # 正臂＝自指闭合锚件＝采信可查态在场（与反臂差分＝守卫生效非一刀切）
    good = os.path.join(tmp, "good-root")
    os.makedirs(os.path.join(good, ".workbuddy"), exist_ok=True)
    with open(os.path.join(good, ".workbuddy", "swb-anchor"), "w", encoding="utf-8") as f:
        f.write(f"project_root: {good}\n")
    assert wg._anchor_hit(good, pack), "自指闭合合法锚件未被采信＝差分臂失配"
    # 台账自写面＝手写 cleared 行入注入 leases＝其后租约失效＝自写语义可查态在场（freeze 链同源语义）
    write_leases(tmp, [
        {"lease": {"ticket_id": "SWB-B16E", "seat_id": "qa", "path_globs": ["tests/probes/**"], "hash": "h"}},
        {"cleared": True},
        {"lease": {"ticket_id": "SWB-B16E2", "seat_id": "qa", "path_globs": ["tests/results/**"], "hash": "h2"}},
    ])
    rows = wg.load_leases(os.path.join(tmp, "leases.jsonl"))
    assert all(r["lease"]["ticket_id"] == "SWB-B16E2" for r in rows) and len(rows) == 1, \
        "cleared 自写行语义不可查＝租约现行态非 freeze 链口径"
    # cleared 前旧租约面写样件＝可查 deny 态（自写行生效＝非静默）；cleared 后新租约面＝allow 差分臂
    r_old = run_wg(tmp, ["--path", "tests/probes/x.py"],
                   {"agent_type": "software-team-qa", "agent_id": "qa-x"})
    assert '"permissionDecision":"deny"' in r_old.stdout, "cleared 后旧租约面写未落可查 deny 态"
    r_new = run_wg(tmp, ["--path", "tests/results/y.py"],
                   {"agent_type": "software-team-qa", "agent_id": "qa-x"})
    assert '"permissionDecision"' not in r_new.stdout, "cleared 后新租约面差分臂失配"


# ---- 形三：身份冒用＝伪造 seat／agent_type 自报注入→采信面可查态在场（B16-f 预置） ----
def t03_identity_spoof_attribution_visible(tmp: str) -> None:
    write_leases(tmp, [{"lease": {"ticket_id": "SWB-B16E", "seat_id": "engineer",
                                  "path_globs": ["agents/**"], "hash": "h"}}])
    # 冒用架构席自报写租约外面＝deny 存续（写侧不认自报＝租约唯一权威）＝采信面可查
    r = run_wg(tmp, ["--path", "tests/probes/y.py"],
               {"agent_type": "software-team-architect", "agent_id": "arch-spoof"})
    assert '"permissionDecision":"deny"' in r.stdout
    with open(os.path.join(tmp, "led.jsonl"), encoding="utf-8") as f:
        recs = [json.loads(l) for l in f if l.strip()]
    deny_recs = [x for x in recs if x["payload"].get("event") == "write_deny"]
    assert len(deny_recs) == 1 and deny_recs[0]["payload"].get("seat_id") == "architect" \
        and deny_recs[0]["payload"].get("agent_type") == "software-team-architect", \
        "冒用归因不可查＝台账席位／自报字段缺席"
    # posthook 自报席位面＝采信现值入台账可查态（现行为登记＝采信序改动归 B16-f）
    led2 = os.path.join(tmp, "led2.jsonl")
    p = subprocess.run([sys.executable, CA, "posthook", "--command",
                        "git status", "--seat", "seat-selfreport", "--ledger", led2],
                       capture_output=True, text=True)
    assert p.returncode == 0
    if os.path.exists(led2):
        with open(led2, encoding="utf-8") as f:
            recs2 = [json.loads(l) for l in f if l.strip()]
        assert all(x["payload"].get("seat_id", "seat-selfreport") == "seat-selfreport" for x in recs2), \
            "posthook 自报采信不可查"
    # 续尾剥离归因面可查（伪造数字尾缀＝归因落真实席位入台账）
    r2 = run_wg(tmp, ["--path", "tests/probes/z.py"],
                {"agent_type": "software-team-qa-999", "agent_id": "qa-imp1"})
    assert '"permissionDecision":"deny"' in r2.stdout
    with open(os.path.join(tmp, "led.jsonl"), encoding="utf-8") as f:
        recs = [json.loads(l) for l in f if l.strip()]
    imp = [x for x in recs if x["payload"].get("agent_type") == "software-team-qa-999"]
    assert len(imp) == 1 and imp[0]["payload"].get("seat_id") == "qa", \
        "续尾剥离归因不可查＝冒用面静默"


# ---- X3／X4 翻正断言臂＋工程师对照臂＋负夹具（勘正前快照）＝双向机械可判 ----
def _mk_pre_k6_map(tmp: str) -> str:
    """勘正前 config 快照注入件＝qa／architect deny_globs 含 tests/** 字面（负夹具＝deny 循环命中态）。"""
    with open(MAP_AFTER, encoding="utf-8") as f:
        m = json.load(f)
    for row in m["seats"]:
        if row["seat_id"] in ("qa", "architect"):
            row["deny_globs"] = row["deny_globs"] + ["tests/**"]
    path = os.path.join(tmp, "map-pre-k6.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(m, f, ensure_ascii=False)
    return path


def t04_x3_qa_lease_allow_flip(tmp: str) -> None:
    """X3 翻正＝qa 席注入 tests 桶租约在册样件＝勘正后真 config＝allow 直证（过渡态(III) 写侧判定层消除）。"""
    write_leases(tmp, [{"lease": {"ticket_id": "SWB-B16E", "seat_id": "qa",
                                  "path_globs": ["tests/**"], "hash": "h"}}])
    r = run_wg(tmp, ["--path", "tests/probes/x3-sample.py"],
               {"agent_type": "software-team-qa", "agent_id": "qa-x3"})
    assert '"permissionDecision"' not in r.stdout, f"X3 未翻正：{r.stdout}{r.stderr}"
    assert "ALLOW write-guard path=tests/probes/x3-sample.py" in r.stderr, r.stderr


def t05_x4_architect_lease_allow_flip(tmp: str) -> None:
    write_leases(tmp, [{"lease": {"ticket_id": "SWB-B16E", "seat_id": "architect",
                                  "path_globs": ["tests/**"], "hash": "h"}}])
    r = run_wg(tmp, ["--path", "tests/probes/x4-sample.py"],
               {"agent_type": "software-team-architect", "agent_id": "arch-x4"})
    assert '"permissionDecision"' not in r.stdout, f"X4 未翻正：{r.stdout}{r.stderr}"
    assert "ALLOW write-guard path=tests/probes/x4-sample.py" in r.stderr, r.stderr


def t06_engineer_offlease_deny_persists(tmp: str) -> None:
    """工程师对照臂＝租约外路径 deny 存续＝让出非共写席 tests 面防护由租约签发面承载双兜底不扩面。"""
    write_leases(tmp, [{"lease": {"ticket_id": "SWB-B16E", "seat_id": "engineer",
                                  "path_globs": ["tests/**"], "hash": "h"}}])
    r = run_wg(tmp, ["--path", "skills/sop/scripts/x.py"],
               {"agent_type": "software-team-engineer", "agent_id": "eng-c"})
    assert '"permissionDecision":"deny"' in r.stdout, "租约外对照臂失配＝让出扩面"


def t07_negative_pre_k6_map_deny(tmp: str) -> None:
    """负夹具＝勘正前 config 注入态同租约样件＝deny 循环命中 tests/**＝断言双向机械可判。"""
    pre_map = _mk_pre_k6_map(tmp)
    write_leases(tmp, [{"lease": {"ticket_id": "SWB-B16E", "seat_id": "qa",
                                  "path_globs": ["tests/**"], "hash": "h"}}])
    r = subprocess.run(
        [sys.executable, WG, "--path", "tests/probes/x3-sample.py",
         "--map", pre_map, "--ledger", os.path.join(tmp, "led.jsonl"),
         "--leases", os.path.join(tmp, "leases.jsonl"),
         "--freeze-state", os.path.join(tmp, "freeze-state.json")],
        input=json.dumps({"agent_type": "software-team-qa", "agent_id": "qa-x3"}),
        capture_output=True, text=True)
    assert '"permissionDecision":"deny"' in r.stdout, "勘正前基线臂未拦＝双向断言失配"
    assert "glob='tests/**'" in r.stdout, r.stdout


# ---- 两枚同批一致性臂＝真源与 hooks 消费面勘正同步（S2／S3 同批案型直证） ----
def t08_same_batch_config_parity(tmp: str) -> None:
    with open(os.path.join(PACK, "config", "seat-permissions.json"), encoding="utf-8") as f:
        src = json.load(f)
    with open(MAP_AFTER, encoding="utf-8") as f:
        m = json.load(f)
    src_deny = {s["seat_id"]: s.get("deny_globs", []) for s in src["seats"]}
    for row in m["seats"]:
        assert row["deny_globs"] == src_deny[row["seat_id"]], \
            f"席位 {row['seat_id']} 两枚勘正不同批（派生一致性断言）"
    for seat in ("qa", "architect"):
        assert "tests/**" not in src_deny[seat], f"{seat} 勘正未落位＝过渡态(III) 残留"
    for seat in ("host", "product"):
        assert "tests/**" in src_deny[seat], f"{seat} 非共写席让出越界＝不扩面约束失守"


def run_self() -> int:
    tests = [t01_bypass_forms_blocked_or_registered,
             t02_selfwritten_anchor_rejected_and_ledger_state_visible,
             t03_identity_spoof_attribution_visible,
             t04_x3_qa_lease_allow_flip, t05_x4_architect_lease_allow_flip,
             t06_engineer_offlease_deny_persists, t07_negative_pre_k6_map_deny,
             t08_same_batch_config_parity]
    for t in tests:
        with tempfile.TemporaryDirectory() as tmp:
            t(tmp)
        print(f"PASS {t.__name__}")
    return 0


if __name__ == "__main__":
    sys.exit(run_self())
