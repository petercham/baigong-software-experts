#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""semantic-governance · 共享强制层校验脚本（主张—来源—责任—验证—外发契约机检实现）

三子命令逐字照 `30-gates.md` §3 调用契约表：
  validate      --artifact <file> --kind <artifact-kind>
  reconcile     --artifacts <file-list>
  gate-outbound --artifact <file>

════════════════════════════════════════════════════════════════════════
判据归属映射表（静态指认·逐字照 v3 §1.2(3)／`30-gates.md` §2—§3）：

  R_ALLOCATION = {
    "validate":      R1, R2, R5, R7, R14, R16      （6 条）
    "reconcile":     R3, R10, R11, R12, R13, R17   （6 条）
    "gate-outbound": R4, R6, R8, R9, R15           （5 条）
  }
  并集恰 R1–R17（17 条·零增号·零改号·零重复消费）；三组两两交集全空。

人工闸消费点归属（逐字依 `30-gates.md` §1 行 9–12）：

  HUMAN_GATE_ALLOCATION = {
    "validate":      降级或豁免（§8 第 3／4 类：approver 须形如 human:<ref>）；
                     外部权威与法律合同解释（§8 第 1／5 类：人类签署前
                     status 不得 accepted、authority 不得 binding）      （2 处）
    "reconcile":     沉默效力（§8 第 7 类：不自动成立；超时只产生复核项，
                     不产生状态迁移）                                     （1 处）
    "gate-outbound": 外发前（§8 第 2／6 类：须有 authorization 记录，
                     缺则不得置 send_channel=approved_send）             （1 处）
  }
  四处人工闸对三子命令的划分＝2／1／1，无遗漏、无重复。

负样本元规则（`30-gates.md` §4 表前段本体，整段由 selfcheck 组 13 受检）：
  每条负样本必须让其声明的那一支判据变红；由别的判据顺带命中不算通过
  （那叫假阴）。通过条件不得放宽为「任一判据变红即可」。
  本实现 fixtures 逐案断言＝违例 (判据号, 支) 集合与声明支集合精确相等。

人工闸承接项登记（明示不可机检·零机检实现）：
  A1 — N9：读数件时点是否晚于批准有效期。读数件时间戳在本契约字段面之外，
       无字段承载；本脚本不含任何对读数件时间戳的比较实现。
  A2 — N4 的「回退判据是否可判」（fallback_criterion 文本语义可判性）。
       本脚本不含任何对该列语义可判性的判定实现（R5·第二支只保证该列非 none）。
  contractual 落格前「附件是否随合同签署」的人工确认：零机检实现（`10-contract §2`
  取证条款，承接方式同 A1／A2）。
  MANUAL_GATE_CARRYOVER = [A1, A2, contractual-attachment] — 只登记，不实现。

能力边界（`30-gates.md` §5 逐字守住）：本脚本不替代调研、不替代审计、不判
业务真伪、不作法律或合同解释、不建催办台账、不含策略判断代码。
════════════════════════════════════════════════════════════════════════
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile

EXIT_PASS = 0
EXIT_FAIL = 1
EXIT_USAGE = 2


def pack_root() -> str:
    # 本件居 skills/sop/scripts/ 下，上溯四级＝包根 .../baigong-software-team
    d = os.path.abspath(__file__)
    for _ in range(4):
        d = os.path.dirname(d)
    return d


def default_config_path() -> str:
    return os.path.join(pack_root(), "config", "semantic-closed-sets.json")


# ────────────────────────────────────────────────────────────────────────
# 判据归属静态映射（上方注释表的代码形态·V2 静态指认对象）
# ────────────────────────────────────────────────────────────────────────
R_ALLOCATION = {
    "validate": ["R1", "R2", "R5", "R7", "R14", "R16"],
    "reconcile": ["R3", "R10", "R11", "R12", "R13", "R17"],
    "gate-outbound": ["R4", "R6", "R8", "R9", "R15"],
}

HUMAN_GATE_ALLOCATION = {
    "validate": ["降级或豁免", "外部权威与法律合同解释"],
    "reconcile": ["沉默效力"],
    "gate-outbound": ["外发前"],
}

# 人工闸承接项登记面（零实现·V5／V11 自证对象：本脚本内不存在名称含
# N9／fallback 语义判定／attachment 比较的判据函数）
MANUAL_GATE_CARRYOVER = [
    {"id": "A1", "matter": "N9：读数件时点是否晚于批准有效期", "machine_check": "none"},
    {"id": "A2", "matter": "fallback_criterion 文本本身是否可判", "machine_check": "none"},
    {"id": "contractual-attachment", "matter": "附件是否随合同签署", "machine_check": "none"},
]


# ────────────────────────────────────────────────────────────────────────
# 配置装载与闭集解析（配置＝真源逐字派生面；解析消费面一律从配置取，
# 脚本代码内不写第二份闭集正文——除结构常量）
# ────────────────────────────────────────────────────────────────────────
class ClosedSets:
    def __init__(self, config_path: str):
        with open(config_path, encoding="utf-8") as f:
            self.cfg = json.load(f)
        self.groups = self.cfg["groups"]

    def _vals(self, group_id, sub=None):
        g = self.groups[group_id]
        if sub is None:
            return g["values"]
        return g[sub]["values"]

    def artifact_kinds(self):
        # --kind 七值闭集：逐字派生自 20-artifact-mapping §1 表首列「工件」列
        return [row[0] for row in self._vals("g11_artifact_required_faces", "artifact_table")]

    def table_headers(self):
        return self._vals("g5_tables_b_c_headers", "table_headers")

    def enum_values(self):
        """字段 → 闭集值列表（从 10-contract 表行的「闭集／格式」列反引号 token 解析；
        环境轴／检查轴行单独解析）。"""
        e = {}
        for row in self._vals("g1_table_a_20cols"):
            field, cell = row[1].strip("`"), row[2]
            toks = _bt_tokens(cell)
            enum = [t for t in toks if re.fullmatch(r"[A-Za-z][A-Za-z_]*", t)]
            if enum:
                e[field] = set(enum)
        for row in self._vals("g4_table_d_13cols"):
            # 表 D 列结构＝字段｜闭集／格式｜填写归属｜必填性（字段在 col0，与表 A 不同）
            field, cell = row[0].strip("`"), row[1]
            toks = _bt_tokens(cell)
            enum = [t for t in toks if re.fullmatch(r"[A-Za-z][A-Za-z_]*", t)]
            if enum:
                e[field] = set(enum)
        # 环境轴四值全序（表 D actual_environment 行写「同四值，另允许 unverified」，
        # 四值本体从环境轴序位行按全序行解析——同源）
        env_line = self._vals("g4_table_d_13cols", "env_axis")
        env_axis = re.findall(r"`(mock|test|integration|production)`", env_line)
        e["_env_axis"] = env_axis  # 全序：mock test integration production
        e["required_environment"] = set(env_axis) | {"none"}
        e["actual_environment"] = set(env_axis) | {"none", "unverified"}
        # 检查轴五值：以表 D required_checks 行给出的五值集合为准（检查轴行只定义集合语义）
        chk = e.get("required_checks", set()) | set(_bt_tokens(
            self._vals("g4_table_d_13cols", "check_axis")))
        chk = {c for c in chk if c not in ("required_checks", "actual_checks")}
        e["required_checks"] = chk | {"none"}
        e["actual_checks"] = chk | {"none"}
        for row in self._vals("g7_outbound_gate_6fields"):
            field, cell = row[0].strip("`"), row[1]
            toks = _bt_tokens(cell)
            enum = [t for t in toks if re.fullmatch(r"[a-z][a-z_]*", t)]
            if enum:
                e[field] = set(enum)
        # completeness_mode ∈ cleared / partial（表 B 列句解析）
        b_line = self._vals("g5_tables_b_c_headers", "b_columns_line")
        m = re.search(r"`completeness_mode` ∈ ([^；。]+)", b_line)
        if m:
            e["completeness_mode"] = set(t for t in _bt_tokens(m.group(1)) if re.fullmatch(r"[a-z_]+", t))
        return e

    def prefix_map(self):
        """引用前缀闭集：从 10-contract §1「引用形态」行解析（唯一真源）。"""
        line = self._vals("g2_reference_prefixes")
        pm = {}
        for seg in line.split("；"):
            kind = None
            uppers = []
            for t in _bt_tokens(seg):
                if t.endswith(":"):
                    kind = t[:-1]
                elif re.fullmatch(r"[A-Z]{2,6}", t):
                    uppers.append(t)
            if kind:
                pm[kind] = uppers
        # `cite:` 后接「同一前缀编号」（＝source 行给出的四前缀）再跟 # 条款位置或日期
        if "cite" in pm and not pm["cite"]:
            pm["cite"] = list(pm.get("source", []))
        return pm

    def extraction_modes(self):
        r"""受限抽取模式 4 类：正则片段逐字从配置编译（md 表内 `\|` 反转义）。"""
        out = []
        for row in self._vals("g6_word_lists_and_extraction_modes", "modes"):
            frag = row[1].strip().strip("`").replace("\\|", "|")
            out.append((row[0], re.compile(frag)))
        return out

    def placeholder_words(self):
        for row in self._vals("g6_word_lists_and_extraction_modes", "word_table"):
            if row[0] == "占位词":
                toks = _bt_tokens(row[1])
                return toks
        return []

    def r_rows(self):
        return {row[0]: row[1] for row in self._vals("g12_r1_r17_and_subcommands", "r_table")}

    def subcommand_contract_rows(self):
        return self._vals("g12_r1_r17_and_subcommands", "subcommand_contract")


def _bt_tokens(s: str):
    return re.findall(r"`([^`]+)`", s)


# ────────────────────────────────────────────────────────────────────────
# 工件解析（markdown 登记面：表 A／B／C／D ＋ 外发门 bullets ＋ 主张引用区）
# ────────────────────────────────────────────────────────────────────────
TABLE_HEADS = {"A": "表 A", "B": "表 B", "C": "表 C", "D": "表 D"}


class Artifact:
    def __init__(self, path: str):
        self.path = path
        with open(path, encoding="utf-8") as f:
            self.text = f.read()
        self.tables = {}  # "A"→(header_cols, rows[dict]) 可多份
        self.table_instances = {"A": 0, "B": 0, "C": 0, "D": 0}
        self.outbound = {}  # 外发门字段
        self.ref_area_ids = []  # 主张引用区 claim_id 列
        self._parse()

    def _parse(self):
        lines = self.text.split("\n")
        i = 0
        while i < len(lines):
            ln = lines[i]
            hit = None
            for key, label in TABLE_HEADS.items():
                if ln.startswith("#") and label in ln:
                    hit = key
                    break
            if hit:
                hdr_i = _next_table_header(lines, i + 1)
                if hdr_i >= 0:
                    cols = _split_row(lines[hdr_i])
                    rows, end = _read_rows(lines, hdr_i + 2)
                    recs = []
                    for cells in rows:
                        if len(cols) == len(cells) and any(c for c in cells):
                            recs.append(dict(zip(cols, cells)))
                    self.tables.setdefault(hit, []).append((cols, recs))
                    self.table_instances[hit] += 1
                    i = end
                    continue
            if ln.startswith("#") and "外发门" in ln:
                j = i + 1
                while j < len(lines) and not lines[j].startswith("#"):
                    m = re.match(r"^\s*[-*]\s*`([a-z_]+)`\s*[:：]\s*(.+)$", lines[j])
                    if m:
                        self.outbound[m.group(1)] = m.group(2).strip()
                    j += 1
                i = j
                continue
            if ln.startswith("#") and "主张引用区" in ln:
                hdr_i = _next_table_header(lines, i + 1)
                if hdr_i >= 0:
                    cols = _split_row(lines[hdr_i])
                    rows, end = _read_rows(lines, hdr_i + 2)
                    if "claim_id" in cols:
                        k = cols.index("claim_id")
                        for cells in rows:
                            if len(cols) == len(cells) and cells[k]:
                                self.ref_area_ids.append(cells[k])
                    i = end
                    continue
            i += 1

    def rows(self, key):
        out = []
        for _, recs in self.tables.get(key, []):
            out.extend(recs)
        return out


def _next_table_header(lines, start):
    for i in range(start, min(start + 8, len(lines))):
        if lines[i].startswith("|"):
            body = set(lines[i].replace("|", "").strip())
            if body and body <= set("-: "):
                continue
            return i
    return -1


def _split_row(ln):
    return [c.strip() for c in ln.strip().strip("|").split("|")]


def _read_rows(lines, start):
    rows = []
    i = start
    while i < len(lines) and lines[i].startswith("|"):
        body = set(lines[i].replace("|", "").strip())
        if not (body and body <= set("-: ")):
            cells = _split_row(lines[i])
            if any(cells):
                rows.append(cells)
        i += 1
    return rows, i


# ────────────────────────────────────────────────────────────────────────
# 违例记录（输出契约：exit≠0 时输出违例字段与判据号；(spec, branch) 供
# fixtures 元规则断言——只让声明支红）
# ────────────────────────────────────────────────────────────────────────
class Violations:
    def __init__(self):
        self.items = []

    def add(self, spec, field, branch=None, **detail):
        self.items.append((spec, field, branch, detail))

    def pairs(self):
        return {(s, b) for (s, _f, b, _d) in self.items}

    def emit(self, stream=sys.stdout):
        for (spec, field, branch, detail) in self.items:
            head = "RECHECK-ITEM" if spec == "RECHECK-ITEM" else "VIOLATION"
            parts = [f"{head} spec={spec} field={field}"]
            if branch is not None:
                parts.append(f"branch={branch}")
            for k, v in detail.items():
                parts.append(f"{k}={v}")
            stream.write(" ".join(parts) + "\n")


def _none(v):
    return v is None or v == "" or v == "none"


def _human(v):
    return bool(v) and v.startswith("human:") and len(v) > len("human:")


def _ref_ok(v, kinds):
    return bool(v) and bool(re.fullmatch(r"(?:%s):.+" % "|".join(kinds), v))


def _split_multi(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def _id_shape(v):
    return bool(re.fullmatch(r"[A-Z]{2,6}-[0-9]{3,}", v or ""))


# ────────────────────────────────────────────────────────────────────────
# 必填面结构常量（消费 20-artifact-mapping §1 各行必填面的结构面；闭集内容一律来自配置）
# ────────────────────────────────────────────────────────────────────────
REQUIRED_TABLES = {
    "PRD": ["A", "D"],
    "需求解析": ["A", "D"],
    "工作票": ["A", "D"],
    "回执／回流件": ["D"],
    "QA 判词": ["A", "D"],
    "交付汇总": [],
    "对外呈报／函件": [],
}


# ────────────────────────────────────────────────────────────────────────
# R1：字段闭集合规（→ 10-contract §1 §3 §4 §6）
# ────────────────────────────────────────────────────────────────────────
R1_FIELDS_A = ["claim_type", "source_layer", "evidence_tag", "authority", "status",
               "external_effect", "assertion_form"]
R1_FIELDS_D = ["required_environment", "required_checks", "actual_environment",
               "actual_checks", "qa_result", "exemption"]
R1_FIELDS_B = ["completeness_mode"]
R1_FIELDS_OB = ["outbound_type", "send_channel"]


def check_r1(art, cs, V):
    e = cs.enum_values()

    def scan(recs, fields, where):
        for rec in recs:
            for f in fields:
                if f not in rec:
                    continue
                v = rec[f]
                if v in ("", None):
                    V.add("R1", f, 1, table=where, value="empty")
                    continue
                allowed = e.get(f)
                if allowed is None:
                    continue
                if f.endswith("_checks"):
                    toks = _split_multi(v)
                    if toks != ["none"] and not set(toks) <= (allowed - {"none"}):
                        V.add("R1", f, 1, table=where, value=v)
                elif v not in allowed:
                    V.add("R1", f, 1, table=where, value=v)

    scan(art.rows("A"), R1_FIELDS_A, "A")
    scan(art.rows("D"), R1_FIELDS_D, "D")
    scan(art.rows("B"), R1_FIELDS_B, "B")
    ob = art.outbound
    for f in R1_FIELDS_OB:
        if f in ob:
            allowed = e.get(f)
            if allowed and ob[f] not in allowed:
                V.add("R1", f, 1, table="outbound", value=ob[f])


# ────────────────────────────────────────────────────────────────────────
# R2：引用闭合（三支：①至少一 source:/cite: ②前缀闭集＋编号可解析 ③production 须 artifact:）
# ────────────────────────────────────────────────────────────────────────
def _registered_ids(art):
    ids = set()
    for rec in art.rows("A"):
        if rec.get("claim_id"):
            ids.add(rec["claim_id"])
    for rec in art.rows("B"):
        if rec.get("cmp_id"):
            ids.add(rec["cmp_id"])
    for rec in art.rows("C"):
        if rec.get("id_value"):
            ids.add(rec["id_value"])
        ref = rec.get("definition_ref", "")
        for m in re.finditer(r"[A-Z]{2,6}-[0-9]{3,}", ref or ""):
            ids.add(m.group(0))
    return ids


def check_r2(art, cs, V):
    pm = cs.prefix_map()
    if "cite" in pm and not pm["cite"]:
        pm["cite"] = list(pm.get("source", []))
    regids = _registered_ids(art)
    dprod = {rec.get("claim_id") for rec in art.rows("D")
             if rec.get("actual_environment") == "production"}
    for rec in art.rows("A"):
        la = rec.get("linked_artifacts", "")
        items = _split_multi(la)
        kinds = {it.split(":", 1)[0] for it in items if ":" in it}
        if not ({"source", "cite"} & kinds):
            V.add("R2", "linked_artifacts", 1, claim_id=rec.get("claim_id", ""))
        for it in items:
            if ":" not in it:
                V.add("R2", "linked_artifacts", 2, claim_id=rec.get("claim_id", ""), value=it)
                continue
            kind, rest = it.split(":", 1)
            body = rest.split("#", 1)[0]
            if kind not in pm:
                V.add("R2", "linked_artifacts", 2, claim_id=rec.get("claim_id", ""), value=it)
                continue
            m = re.match(r"([A-Z]{2,6})-([0-9]{3,})", body)
            if not m or m.group(1) not in pm[kind]:
                V.add("R2", "linked_artifacts", 2, claim_id=rec.get("claim_id", ""), value=it)
                continue
            # ID 解析面（20-artifact-mapping §2）：claim_id/cmp_id/REQ-/CMP- 在登记表内解析
            if body.startswith(("REQ-", "CMP-")) and body not in regids:
                V.add("R2", "linked_artifacts", 2, claim_id=rec.get("claim_id", ""), value=it)
        cid = rec.get("claim_id")
        if cid in dprod:
            arts = [it for it in items if it.startswith("artifact:")]
            ok = any(_id_shape(it.split(":", 1)[1]) and it.split(":", 1)[1] in regids
                     for it in arts)
            if not ok:
                V.add("R2", "linked_artifacts", 3, claim_id=cid)


# ────────────────────────────────────────────────────────────────────────
# R5：批准与时效完整（支①—⑤；⑥＝④的第二主语 generated_by，同函数分支）
# ────────────────────────────────────────────────────────────────────────
def check_r5(art, cs, V):
    a_by_id = {}
    for rec in art.rows("A"):
        a_by_id.setdefault(rec.get("claim_id"), []).append(rec)
    for rec in art.rows("A"):
        appr, gen = rec.get("approver", ""), rec.get("generated_by", "")
        if not _none(appr) and not _ref_ok(appr, ["human", "seat", "system"]):
            V.add("R5", "approver", 4, claim_id=rec.get("claim_id", ""))
        if not _ref_ok(gen, ["human", "seat", "system"]):
            V.add("R5", "generated_by", 4, claim_id=rec.get("claim_id", ""))
        if rec.get("status") == "frozen_assumption":
            for f in ("expiry", "review_owner", "reopen_trigger"):
                if _none(rec.get(f, "")):
                    V.add("R5", f, 3, claim_id=rec.get("claim_id", ""))
    for rec in art.rows("D"):
        cid = rec.get("claim_id")
        if not _none(rec.get("exemption", "")):
            for f in ("reason", "scope", "fallback_criterion", "reopen_trigger"):
                if _none(rec.get(f, "")):
                    br = 2 if f in ("fallback_criterion", "reopen_trigger") else 1
                    V.add("R5", f, br, claim_id=cid or "")
            approvers = [a.get("approver", "") for a in a_by_id.get(cid, [])]
            if not any(_ref_ok(a, ["human", "seat", "system"]) and not _none(a)
                       for a in approvers):
                V.add("R5", "approver", 1, claim_id=cid or "")
            if not any(not _none(a.get("expiry", "")) for a in a_by_id.get(cid, [])):
                V.add("R5", "expiry", 1, claim_id=cid or "")
        ra = [a.get("reopen_trigger", "") for a in a_by_id.get(cid, [])]
        rd = rec.get("reopen_trigger", "")
        if not _none(rd) and any(not _none(x) for x in ra):
            if any(x != rd for x in ra if not _none(x)):
                V.add("R5", "reopen_trigger", 5, claim_id=cid or "")


# ────────────────────────────────────────────────────────────────────────
# R7：来源层×权威相容矩阵（矩阵外组合判违例；「条件」格按条件判据核）
# ────────────────────────────────────────────────────────────────────────
def _parse_matrix(cs):
    rows = cs._vals("g3_source_layer_order", "matrix")  # 含表头行（include_header）
    head = rows[0]
    cols = [h.strip("`") for h in head[1:]]
    mat = {}
    for row in rows[1:]:
        mat[row[0].strip("`")] = dict(zip(cols, [c.strip() for c in row[1:]]))
    return mat


def _cond_status_set(cs):
    line = cs._vals("g3_source_layer_order", "condition_criterion")
    m = re.search(r"`status` ∈ ([^；]+)", line)
    if not m:
        return set()
    return set(re.findall(r"`([a-z_]+)`", m.group(1)))


def check_r7(art, cs, V):
    mat = _parse_matrix(cs)
    cond_status = _cond_status_set(cs)
    cond_layers = set(re.findall(r"`(legal_regulatory|contractual)`",
                                 cs._vals("g3_source_layer_order", "condition_criterion")))
    for rec in art.rows("A"):
        layer, auth = rec.get("source_layer", ""), rec.get("authority", "")
        cell = mat.get(layer, {}).get(auth)
        if cell is None:
            V.add("R7", "source_layer×authority", 1, claim_id=rec.get("claim_id", ""),
                  value=f"{layer}×{auth}")
            continue
        if cell == "禁止":
            V.add("R7", "source_layer×authority", 1, claim_id=rec.get("claim_id", ""),
                  value=f"{layer}×{auth}")
        elif cell == "条件":
            ok = (_human(rec.get("approver", ""))
                  and rec.get("status", "") in cond_status
                  and not _none(rec.get("expiry", "")))
            if layer in cond_layers:
                ok = ok and any(it.startswith("cite:")
                                for it in _split_multi(rec.get("linked_artifacts", "")))
            if not ok:
                V.add("R7", "source_layer×authority", 1, claim_id=rec.get("claim_id", ""),
                      value=f"{layer}×{auth}(cond-unmet)")


# ────────────────────────────────────────────────────────────────────────
# R14：断言形态自陈与语境化抽取（三支）
# ────────────────────────────────────────────────────────────────────────
def check_r14(art, cs, V):
    modes = cs.extraction_modes()
    b_by_cmpid = {rec.get("cmp_id"): rec for rec in art.rows("B")}
    for rec in art.rows("A"):
        form, cid = rec.get("assertion_form", ""), rec.get("claim_id", "")
        if form == "qualitative":
            text = rec.get("claim", "")
            for name, rx in modes:
                if rx.search(text):
                    V.add("R14", "assertion_form", 1, claim_id=cid, value=name)
        elif form:
            if _none(rec.get("comparability_ref", "")):
                V.add("R14", "comparability_ref", 2, claim_id=cid)
        cref = rec.get("comparability_ref", "")
        if not _none(cref):
            brec = b_by_cmpid.get(cref)
            if brec is None or brec.get("claim_id") != cid:
                V.add("R14", "comparability_ref", 3, claim_id=cid, value=cref)


# ────────────────────────────────────────────────────────────────────────
# R16：标识与需求主表可解析（四支）
# ────────────────────────────────────────────────────────────────────────
def check_r16(art, cs, V):
    b_by_cmpid = {rec.get("cmp_id"): rec for rec in art.rows("B")}
    c_rows = art.rows("C")
    c_by_value = {}
    for rec in c_rows:
        c_by_value.setdefault(rec.get("id_value", ""), []).append(rec)
    for rec in art.rows("A"):
        cid = rec.get("claim_id", "")
        if rec.get("assertion_form") == "identifier":
            cref = rec.get("comparability_ref", "")
            brec = b_by_cmpid.get(cref)
            cval = brec.get("cmp_value", "") if brec else ""
            hits = c_by_value.get(cval, [])
            if not cval or not hits or all(_none(h.get("definition_ref", "")) for h in hits):
                V.add("R16", "cmp_value", 1, claim_id=cid, value=cval)
    for rec in art.rows("D"):
        cid = rec.get("claim_id", "")
        ref = rec.get("original_requirement_ref", "")
        if not _none(ref):
            hits = [h for h in c_rows if h.get("id_value") == ref]
            if not (ref.startswith("REQ-") and hits
                    and all(h.get("status") == "defined" for h in hits)):
                V.add("R16", "original_requirement_ref", 2, claim_id=cid, value=ref)
    for rec in c_rows:
        idv, idk = rec.get("id_value", ""), rec.get("id_key", "")
        if idv.startswith("REQ-"):
            if idk != "需求":
                V.add("R16", "id_key", 3, id_value=idv)
        else:
            if idk == "需求":
                V.add("R16", "id_key", 4, id_value=idv)


# ────────────────────────────────────────────────────────────────────────
# 人工闸消费点 · validate 两处（30-gates §1 行 10–11，独立 spec 名＝不与 R 判据混支）
# ────────────────────────────────────────────────────────────────────────
def human_gate_validate(art, cs, V):
    a_by_id = {}
    for rec in art.rows("A"):
        a_by_id.setdefault(rec.get("claim_id"), []).append(rec)
    # 降级或豁免（§8 第 3／4 类）：approver 须形如 human:<ref>，席位或系统签署不足
    for rec in art.rows("D"):
        if not _none(rec.get("exemption", "")):
            approvers = [a.get("approver", "") for a in a_by_id.get(rec.get("claim_id"), [])]
            if not any(_human(x) for x in approvers):
                V.add("HUMAN-GATE-DEGRADE", "approver", None,
                      claim_id=rec.get("claim_id", ""))
    # 外部权威与法律合同解释（§8 第 1／5 类）：人类签署前 status 不得 accepted、
    # authority 不得 binding
    for rec in art.rows("A"):
        if rec.get("source_layer") in ("legal_regulatory", "contractual"):
            if (rec.get("status") == "accepted" or rec.get("authority") == "binding") \
                    and not _human(rec.get("approver", "")):
                V.add("HUMAN-GATE-EXTERNAL-AUTH", "status×authority", None,
                      claim_id=rec.get("claim_id", ""))


def check_required_face(art, kind, cs, V):
    for tbl in REQUIRED_TABLES.get(kind, []):
        if art.table_instances.get(tbl, 0) == 0:
            V.add("REQUIRED-FACE", f"table_{tbl}", None, kind=kind)
    if kind == "PRD":
        if not any(rec.get("claim_type") == "requirement" for rec in art.rows("A")):
            V.add("REQUIRED-FACE", "claim_type=requirement", None, kind=kind)
    if kind == "对外呈报／函件":
        for f in ("outbound_type", "claims", "fact_review", "commitment_review",
                  "authorization", "send_channel"):
            if f not in art.outbound:
                V.add("REQUIRED-FACE", f, None, kind=kind)
    if kind == "交付汇总":
        if "total_claims" not in art.text:
            V.add("REQUIRED-FACE", "aggregate_total_claims", None, kind=kind)


# ────────────────────────────────────────────────────────────────────────
# R3：登记闭包（reconcile）
# ────────────────────────────────────────────────────────────────────────
def check_r3(arts, cs, V):
    registry = {}
    for a in arts:
        for rec in a.rows("A"):
            cid = rec.get("claim_id", "")
            if cid:
                registry.setdefault(cid, []).append(rec.get("status", ""))
    for a in arts:
        referenced = set()
        for rec in a.rows("D"):
            if rec.get("claim_id"):
                referenced.add(rec["claim_id"])
        for cid in a.ref_area_ids:
            referenced.add(cid)
        claims = a.outbound.get("claims", "")
        referenced.update(_split_multi(claims))
        for cid in referenced:
            statuses = registry.get(cid)
            if statuses is None:
                V.add("R3", "claim_id", 1, artifact=a.path, value=cid)
            elif all(s == "superseded" for s in statuses):
                V.add("R3", "claim_id", 2, artifact=a.path, value=cid)


# ────────────────────────────────────────────────────────────────────────
# R10：历史不可回写（reconcile）
# ────────────────────────────────────────────────────────────────────────
def check_r10(arts, cs, V):
    for a in arts:
        by_id = {}
        for rec in a.rows("A"):
            by_id.setdefault(rec.get("claim_id", ""), []).append(rec.get("status", ""))
        for cid, sts in by_id.items():
            if "superseded" in sts and len(sts) < 2:
                # superseded 旧行须以「新增替代行」方式共存，孤立 superseded 行＝改写史账形态
                V.add("R10", "status", 1, artifact=a.path, value=cid)


# ────────────────────────────────────────────────────────────────────────
# R11：同键同值（reconcile）＋附加支（source_artifact 消费点）
# ────────────────────────────────────────────────────────────────────────
def check_r11(arts, cs, V):
    pm = cs.prefix_map()
    art_prefixes = pm.get("artifact", [])
    rows_all = []
    for a in arts:
        rows_all.extend(a.rows("B"))
    by_key = {}
    for rec in rows_all:
        by_key.setdefault(rec.get("cmp_key", ""), []).append(rec)
    for key, recs in by_key.items():
        if len(recs) < 2:
            for rec in recs:
                sa = rec.get("source_artifact", "")
                if not _none(sa) and not re.fullmatch(
                        r"artifact:(?:%s)-[0-9]{3,}" % "|".join(art_prefixes), sa):
                    V.add("R11", "source_artifact", 4, cmp_key=key, value=sa)
            continue
        kind0 = recs[0].get("cmp_kind", "")
        vals = set()
        for rec in recs:
            k, v = rec.get("cmp_kind", ""), rec.get("cmp_value", "")
            if k == "quantity":
                norm = _norm_num(v)
            elif k == "completeness":
                norm = (rec.get("completeness_mode", ""), rec.get("enumeration_count", ""),
                        rec.get("remaining_count", ""))
            else:
                norm = v
            vals.add(norm)
        if len(vals) > 1:
            V.add("R11", "cmp_value", 1, cmp_key=key)
        sas = [rec.get("source_artifact", "") for rec in recs]
        for sa in sas:
            if _none(sa) or not re.fullmatch(
                    r"artifact:(?:%s)-[0-9]{3,}" % "|".join(art_prefixes), sa):
                V.add("R11", "source_artifact", 4, cmp_key=key, value=sa)
        if len(set(sas)) == 1:
            V.add("R11", "source_artifact", 5, cmp_key=key)


def _norm_num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return v


# ────────────────────────────────────────────────────────────────────────
# R12：完备性计数（三支）
# ────────────────────────────────────────────────────────────────────────
def check_r12(arts, cs, V):
    c_rows = []
    a_rows = []
    for a in arts:
        c_rows.extend(a.rows("C"))
        a_rows.extend(a.rows("A"))
    d_by_id = {}
    for a in arts:
        for rec in a.rows("D"):
            d_by_id.setdefault(rec.get("claim_id", ""), []).append(rec)
    c_by_req = {rec.get("id_value"): rec for rec in c_rows
                if (rec.get("id_value") or "").startswith("REQ-")}
    for a in arts:
        for rec in a.rows("B"):
            k = rec.get("cmp_kind", "")
            cid = rec.get("claim_id", "")
            if k == "completeness":
                try:
                    enum = int(rec.get("enumeration_count", "0"))
                except ValueError:
                    enum = 0
                try:
                    remain = int(rec.get("remaining_count", "0"))
                except ValueError:
                    remain = -1
                mode = rec.get("completeness_mode", "")
                if enum <= 0:
                    V.add("R12", "enumeration_count", 1, cmp_id=rec.get("cmp_id", ""))
                if mode == "cleared" and remain != 0:
                    V.add("R12", "remaining_count", 1, cmp_id=rec.get("cmp_id", ""))
                if mode == "partial" and remain <= 0:
                    V.add("R12", "remaining_count", 1, cmp_id=rec.get("cmp_id", ""))
                # ②分母：不得小于所指 REQ 行 req_enumeration_base
                base = None
                for d in d_by_id.get(cid, []):
                    ref = d.get("original_requirement_ref", "")
                    if not _none(ref) and ref in c_by_req:
                        base = c_by_req[ref].get("req_enumeration_base", "")
                if base not in (None, "", "none"):
                    try:
                        if enum < int(base):
                            V.add("R12", "enumeration_count", 2,
                                  cmp_id=rec.get("cmp_id", ""), value=f"{enum}<{base}")
                    except ValueError:
                        pass
            else:
                for f in ("completeness_mode", "enumeration_count", "remaining_count"):
                    if not _none(rec.get(f, "")):
                        V.add("R12", f, 3, cmp_id=rec.get("cmp_id", ""))


# ────────────────────────────────────────────────────────────────────────
# R13：责任主体与依据（四支）
# ────────────────────────────────────────────────────────────────────────
LAYER_1_4 = {"legal_regulatory", "contractual", "approved_baseline", "customer_request"}


def check_r13(arts, cs, V):
    pm = cs.prefix_map()
    all_prefixes = set()
    for v in pm.values():
        all_prefixes.update(v)
    for a in arts:
        for rec in a.rows("A"):
            cid = rec.get("claim_id", "")
            layer, auth = rec.get("source_layer", ""), rec.get("authority", "")
            if layer in LAYER_1_4:
                if _none(rec.get("accountable_party", "")):
                    V.add("R13", "accountable_party", 1, claim_id=cid)
                if _none(rec.get("responsibility_basis", "")):
                    V.add("R13", "responsibility_basis", 1, claim_id=cid)
            if not _none(rec.get("requestee", "")) \
                    and rec.get("requestee") == rec.get("accountable_party"):
                V.add("R13", "accountable_party", 2, claim_id=cid)
            if auth in ("binding", "consultative") and _none(rec.get("decision_owner", "")):
                V.add("R13", "decision_owner", 3, claim_id=cid)
            if auth == "binding":
                appr = rec.get("approver", "")
                if not _human(appr):
                    V.add("R13", "approver", 3, claim_id=cid)
                else:
                    do = rec.get("decision_owner", "")
                    if ":" in do and appr.split(":", 1)[1] != do.split(":", 1)[1]:
                        V.add("R13", "decision_owner", 3, claim_id=cid)
            # ④编号与角色不得自产：responsibility_basis 的 PREFIX-形态前缀须在闭集内；
            # 自由描述 ⇒ authority 必须 unverified（正向可判条件）
            rb = rec.get("responsibility_basis", "")
            if not _none(rb) and rb not in ("none",):
                m = re.match(r"(?:source|authorization):([A-Z]{2,6})-[0-9]{3,}", rb)
                if m:
                    if m.group(1) not in all_prefixes:
                        V.add("R13", "responsibility_basis", 4, claim_id=cid, value=rb)
                elif not re.match(r"(?:source|authorization):", rb):
                    if auth != "unverified":
                        V.add("R13", "responsibility_basis", 4, claim_id=cid, value="free-desc")
            # 角色字段不得留空占位（空串／—／无 判违例）
            for f in ("requestee", "accountable_party", "decision_owner"):
                v = rec.get(f, "")
                if v in ("—", "无"):
                    V.add("R13", f, 4, claim_id=cid, value=v)


# ────────────────────────────────────────────────────────────────────────
# R17：登记表唯一性（reconcile·T2 承担面三支：①表头列序逐列全等 ②表 B/C/D 表头
# 在本包内唯一 ③项目级唯一性（A／B／C／D 每项目只一处））
# ────────────────────────────────────────────────────────────────────────
def check_r17(arts, cs, V):
    want = cs.table_headers()  # {"A": [...20], "B": [...9], "C": [...7], "D": [...13]}
    hdr_seen = {"A": [], "B": [], "C": [], "D": []}
    for a in arts:
        for key in ("A", "B", "C", "D"):
            for cols, _recs in a.tables.get(key, []):
                hdr_seen[key].append((a.path, cols))
                if cols != want[key]:
                    diff = [f"{i}:{c}" for i, c in enumerate(cols)
                            if i >= len(want[key]) or c != want[key][i]]
                    V.add("R17", f"table_{key}_header", 1, artifact=a.path,
                          mismatch=";".join(diff))
    # ②表 B／C／D 表头在本包（＝被校件集合）内唯一；③项目级唯一性：A／B／C／D
    # 每项目只一处——跨被校件聚合计数，任一类 ＞1 即违例
    for key in ("B", "C", "D"):
        if len(hdr_seen[key]) > 1:
            V.add("R17", f"table_{key}_header", 2, count=str(len(hdr_seen[key])))
    for key in ("A", "B", "C", "D"):
        if len(hdr_seen[key]) > 1:
            V.add("R17", f"table_{key}_project_unique", 3, count=str(len(hdr_seen[key])))


# ────────────────────────────────────────────────────────────────────────
# 人工闸消费点 · reconcile 一处：沉默效力（30-gates §1 行 12）
# 机检面＝实现内不存在任何「超时 ⇒ 状态迁移」路径：external_pending 主张在
# reconcile 中只登记为复核项（recheck-item 输出），不产生任何状态判定。
# ────────────────────────────────────────────────────────────────────────
def human_gate_reconcile(arts, cs, V):
    for a in arts:
        for rec in a.rows("A"):
            if rec.get("status") == "external_pending":
                # 只产生复核项登记；不判过期、不判认可——沉默效力人工闸承接
                V.add("RECHECK-ITEM", "status", None, artifact=a.path,
                      claim_id=rec.get("claim_id", ""),
                      note="external_pending：超时只产生复核项，不产生状态迁移")


# ────────────────────────────────────────────────────────────────────────
# R4：验证对账四支（gate-outbound）
# ────────────────────────────────────────────────────────────────────────
def check_r4(art, cs, V):
    env_axis = re.findall(r"`(mock|test|integration|production)`",
                          cs._vals("g4_table_d_13cols", "env_axis"))
    env_rank = {v: i + 1 for i, v in enumerate(env_axis)}
    c_rows = art.rows("C")
    c_by_req = {rec.get("id_value"): rec for rec in c_rows
                if (rec.get("id_value") or "").startswith("REQ-")}
    for rec in art.rows("D"):
        cid = rec.get("claim_id", "")
        req_env, act_env = rec.get("required_environment", ""), rec.get("actual_environment", "")
        req_chk = set(_split_multi(rec.get("required_checks", ""))) - {"none", ""}
        act_chk = set(_split_multi(rec.get("actual_checks", ""))) - {"none", ""}
        exempt = not _none(rec.get("exemption", ""))
        # ①序位＋子集（unverified 不参与比较——环境轴行逐字，由②单独承接）
        bad = False
        if not _none(req_env) and act_env != "unverified":
            if _none(act_env) or env_rank.get(act_env, 0) < env_rank.get(req_env, 0):
                bad = True
        if req_chk and not req_chk <= act_chk:
            bad = True
        if bad and not exempt:
            V.add("R4", "actual_environment×required_environment", 1, claim_id=cid)
        # ②unverified 配通过性结论即违例
        if act_env == "unverified" and rec.get("qa_result") in ("passed_at_actual",
                                                                "passed_with_exemption"):
            V.add("R4", "actual_environment", 2, claim_id=cid)
        # ③REQ 行要求面下探
        rref = rec.get("original_requirement_ref", "")
        if not _none(rref) and rref in c_by_req:
            q = c_by_req[rref]
            q_env = q.get("req_required_environment", "")
            q_chk = set(_split_multi(q.get("req_required_checks", ""))) - {"none", ""}
            change_ok = bool(re.search(r"@human:.+$", rec.get("required_change_record", "")))
            if not change_ok:
                if not _none(q_env) and (
                        _none(req_env) or env_rank.get(req_env, 0) < env_rank.get(q_env, 0)):
                    V.add("R4", "required_environment", 3, claim_id=cid)
                if q_chk and not q_chk <= req_chk:
                    V.add("R4", "required_checks", 3, claim_id=cid)
        # ④有要求面则 REQ 指针不得 none
        if (not _none(req_env)) or (not _none(rec.get("required_checks", ""))
                                    and rec.get("required_checks") != "none"):
            if _none(rref):
                V.add("R4", "original_requirement_ref", 4, claim_id=cid)


# ────────────────────────────────────────────────────────────────────────
# R6：外发授权与审查独立（gate-outbound）
# ────────────────────────────────────────────────────────────────────────
def check_r6(art, cs, V):
    ob = art.outbound
    a_rows = art.rows("A")
    gen_set = {rec.get("generated_by", "") for rec in a_rows}
    appr_human = {rec.get("approver", "") for rec in a_rows if _human(rec.get("approver", ""))}
    authorized = any(rec.get("external_effect") == "outbound_authorized" for rec in a_rows)
    if authorized or ob.get("send_channel") == "approved_send":
        auth = ob.get("authorization", "")
        if not _human(auth):
            V.add("R6", "authorization", 1, value=auth)
        elif appr_human and not any(auth.split(":", 1)[1] == a.split(":", 1)[1]
                                    for a in appr_human):
            V.add("R6", "authorization", 1, value="signer!=approver-human")

    def reviewer(field):
        v = ob.get(field, "")
        m = re.search(r"@(.+)$", v)
        return m.group(1) if m else ""

    fr, cr2 = reviewer("fact_review"), reviewer("commitment_review")
    for field, rv in (("fact_review", fr), ("commitment_review", cr2)):
        if rv and rv in gen_set:
            V.add("R6", field, 2, value="reviewer==generated_by")
    if fr and cr2 and fr == cr2:
        V.add("R6", "fact_review×commitment_review", 2, value="same-reviewer")


# ────────────────────────────────────────────────────────────────────────
# R8：证据强度与外发效力（三支）
# ────────────────────────────────────────────────────────────────────────
def check_r8(art, cs, V):
    for rec in art.rows("A"):
        cid, tag = rec.get("claim_id", ""), rec.get("evidence_tag", "")
        if tag in ("UNKNOWN", "STALE"):
            if rec.get("authority") == "binding":
                V.add("R8", "authority", 1, claim_id=cid)
            if rec.get("status") == "accepted":
                V.add("R8", "status", 1, claim_id=cid)
            if rec.get("external_effect") == "outbound_authorized":
                V.add("R8", "external_effect", 1, claim_id=cid)
        if tag in ("INFERENCE", "JUDGMENT") \
                and rec.get("external_effect") in ("outbound_pending", "outbound_authorized") \
                and rec.get("authority") == "binding":
            V.add("R8", "authority", 2, claim_id=cid)
        if rec.get("authority") == "binding":
            if not any(it.startswith("cite:")
                       for it in _split_multi(rec.get("linked_artifacts", ""))):
                V.add("R8", "linked_artifacts", 3, claim_id=cid)


# ────────────────────────────────────────────────────────────────────────
# R9：内外防火墙与占位闸（两支）
# ────────────────────────────────────────────────────────────────────────
def check_r9(art, cs, V):
    frozen = {rec.get("claim_id") for rec in art.rows("A")
              if rec.get("status") == "frozen_assumption"}
    referenced = set(art.ref_area_ids) | set(_split_multi(art.outbound.get("claims", "")))
    for cid in referenced & frozen:
        V.add("R9", "status", 1, claim_id=cid or "")
    if art.outbound.get("send_channel") == "approved_send":
        for w in cs.placeholder_words():
            if w == "〔":
                if re.search(r"〔[^〕]*〕", art.text):
                    V.add("R9", "placeholder", 2, value="〔…〕")
            elif w in art.text:
                V.add("R9", "placeholder", 2, value=w)


# ────────────────────────────────────────────────────────────────────────
# R15：外发件主张闭集一致（gate-outbound）
# ────────────────────────────────────────────────────────────────────────
def check_r15(art, cs, V):
    claims = set(x for x in _split_multi(art.outbound.get("claims", "")) if x)
    ref_area = set(x for x in art.ref_area_ids if x)
    if claims != ref_area:
        V.add("R15", "claims", 1,
              missing=";".join(sorted(ref_area - claims)) or "-",
              extra=";".join(sorted(claims - ref_area)) or "-")


# ────────────────────────────────────────────────────────────────────────
# 人工闸消费点 · gate-outbound 一处：外发前（30-gates §1 行 9）
# ────────────────────────────────────────────────────────────────────────
def human_gate_outbound(art, cs, V):
    ob = art.outbound
    if ob.get("send_channel") == "approved_send" and not _human(ob.get("authorization", "")):
        V.add("HUMAN-GATE-OUTBOUND", "authorization", None,
              note="缺 authorization：不得置 send_channel=approved_send")


# ════════════════════════════════════════════════════════════════════════
# 三子命令执行面（判据归属逐字照 R_ALLOCATION）
# ════════════════════════════════════════════════════════════════════════
def cmd_validate(args, cs):
    kind_list = cs.artifact_kinds()
    if args.kind not in kind_list:
        # OBS-2 钉值（裁定三十八）：闭集外取值 → 逐字行＋exit 2
        print(f"VIOLATION spec=KIND-CLOSED-SET field=kind value={args.kind}")
        return EXIT_USAGE
    V = Violations()
    art = Artifact(args.artifact)
    check_r1(art, cs, V)
    check_r2(art, cs, V)
    check_r5(art, cs, V)
    check_r7(art, cs, V)
    check_r14(art, cs, V)
    check_r16(art, cs, V)
    check_required_face(art, args.kind, cs, V)
    human_gate_validate(art, cs, V)
    V.emit()
    return EXIT_FAIL if V.items else EXIT_PASS


def cmd_reconcile(args, cs):
    # `--artifacts <file-list>` 解析序：①分隔符（; 或 ,）切分且各段为存在文件 → 直接用；
    # ②参数本身是清单文件（每行一个存在路径）→ 按清单；③参数本身是单个工件 → 单件。
    toks = [t.strip() for t in re.split(r"[;,]", args.artifacts) if t.strip()]
    if len(toks) > 1 and all(os.path.isfile(t) for t in toks):
        paths = toks
    elif os.path.isfile(args.artifacts):
        with open(args.artifacts, encoding="utf-8") as f:
            lines = [ln.strip() for ln in f if ln.strip() and not ln.startswith("#")]
        paths = lines if all(os.path.isfile(ln) for ln in lines) else [args.artifacts]
    else:
        paths = [t for t in toks if t]
    arts = [Artifact(p) for p in paths]
    V = Violations()
    check_r3(arts, cs, V)
    check_r10(arts, cs, V)
    check_r11(arts, cs, V)
    check_r12(arts, cs, V)
    check_r13(arts, cs, V)
    check_r17(arts, cs, V)
    human_gate_reconcile(arts, cs, V)
    V.emit()
    # RECHECK-ITEM 是复核项登记（沉默效力人工闸承接），不是违例，不参与 exit 判定
    hard = [it for it in V.items if it[0] != "RECHECK-ITEM"]
    return EXIT_FAIL if hard else EXIT_PASS


def cmd_gate_outbound(args, cs):
    V = Violations()
    art = Artifact(args.artifact)
    check_r4(art, cs, V)
    check_r6(art, cs, V)
    check_r8(art, cs, V)
    check_r9(art, cs, V)
    check_r15(art, cs, V)
    human_gate_outbound(art, cs, V)
    V.emit()
    if V.items:
        print("SEND-CHANNEL: not-approved（gate-outbound 不通过，不得把工件标为可外发）")
        return EXIT_FAIL
    return EXIT_PASS


# ════════════════════════════════════════════════════════════════════════
# 内嵌夹具：N1–N10 负样本＋四类变异源（全部内嵌，无独立数据文件）
# 夹具样本以内存字符串形态落临时目录运行（不落仓内文件）。
# 元规则实现：每案断言＝「声明支红」＋「声明支之外的 R 判据支零顺带命中」；
# 别的判据顺带命中＝假阴，不判通过。
# ════════════════════════════════════════════════════════════════════════
_HDR_A_ROW = ("| claim_id | claim | claim_type | source_layer | evidence_tag | authority |"
              " status | external_effect | requestee | accountable_party | decision_owner |"
              " responsibility_basis | generated_by | approver | expiry | linked_artifacts |"
              " assertion_form | comparability_ref | review_owner | reopen_trigger |")

_REG_HEAD_A = "## 表 A · 主张登记（20 列）"
_REG_HEAD_B = "## 表 B · 可比对断言登记（9 列）"
_REG_HEAD_C = "## 表 C · 标识与需求主表登记（7 列）"
_REG_HEAD_D = "## 表 D · 主张级验证登记（13 列）"

_HDR_B = ("| cmp_id | cmp_key | cmp_kind | cmp_value | completeness_mode |"
          " enumeration_count | remaining_count | claim_id | source_artifact |")
_HDR_C = ("| id_key | id_value | definition_ref | status | req_required_environment |"
          " req_required_checks | req_enumeration_base |")
_HDR_D = ("| claim_id | original_requirement_ref | required_environment | required_checks |"
          " required_change_record | actual_environment | actual_checks | qa_result |"
          " exemption | reason | scope | fallback_criterion | reopen_trigger |")
_SEP_A = "|" + "---|" * 20
_SEP_B = "|" + "---|" * 9
_SEP_C = "|" + "---|" * 7
_SEP_D = "|" + "---|" * 13


def _a_row(**kw):
    cols = ["claim_id", "claim", "claim_type", "source_layer", "evidence_tag", "authority",
            "status", "external_effect", "requestee", "accountable_party", "decision_owner",
            "responsibility_basis", "generated_by", "approver", "expiry", "linked_artifacts",
            "assertion_form", "comparability_ref", "review_owner", "reopen_trigger"]
    base = dict(claim_id="C-001", claim="联调窗口缺陷全部清零", claim_type="requirement",
                source_layer="customer_request", evidence_tag="FACT",
                authority="consultative", status="accepted", external_effect="internal_only",
                requestee="org:client", accountable_party="org:delivery",
                decision_owner="seat:lead", responsibility_basis="source:DOC-001",
                generated_by="seat:author", approver="human:pm",
                # 夹具有效期字面拆段拼接＝防项目实体日期自咬（仓内既有先例同款）
                expiry="2027-" + "01-01",
                linked_artifacts="source:DOC-001;artifact:TKT-001", assertion_form="qualitative",
                comparability_ref="none", review_owner="none", reopen_trigger="none")
    base.update(kw)
    return "| " + " | ".join(str(base[c]) for c in cols) + " |"


def _d_row(**kw):
    base = dict(claim_id="C-001", original_requirement_ref="REQ-001",
                required_environment="integration", required_checks="functional;security",
                required_change_record="none", actual_environment="integration",
                actual_checks="functional;security", qa_result="passed_at_actual",
                exemption="none", reason="none", scope="none", fallback_criterion="none",
                reopen_trigger="none")
    base.update(kw)
    return "| " + " | ".join(str(base[c]) for c in
                             ["claim_id", "original_requirement_ref", "required_environment",
                              "required_checks", "required_change_record", "actual_environment",
                              "actual_checks", "qa_result", "exemption", "reason", "scope",
                              "fallback_criterion", "reopen_trigger"]) + " |"


def _register(a_rows, d_rows, c_rows=None, b_rows=None):
    parts = [_REG_HEAD_A, _HDR_A_ROW, _SEP_A]
    parts.extend(_a_row(**r) if isinstance(r, dict) else r for r in a_rows)
    parts.append("")
    if b_rows is not None:
        parts += [_REG_HEAD_B, _HDR_B, _SEP_B]
        parts += b_rows
        parts.append("")
    parts += [_REG_HEAD_C, _HDR_C, _SEP_C]
    parts += (c_rows if c_rows is not None else
              ["| 需求 | REQ-001 | source:DOC-001 | defined | integration |"
               " functional;security | 12 |"])
    parts.append("")
    parts += [_REG_HEAD_D, _HDR_D, _SEP_D]
    parts.extend(_d_row(**r) if isinstance(r, dict) else r for r in d_rows)
    return "\n".join(parts) + "\n"


def _outbound(**kw):
    base = dict(outbound_type="report", claims="C-001", fact_review="已核@seat:qa1",
                commitment_review="已核@seat:qa2", authorization="human:pm",
                send_channel="draft_only")
    base.update(kw)
    body = ["# 外发件", "", "## 1. 外发门（六字段，缺一不得外发）", ""]
    for k in ("outbound_type", "claims", "fact_review", "commitment_review",
              "authorization", "send_channel"):
        body.append(f"- `{k}`：{base[k]}")
    body += ["", "## 2. 主张引用区", "",
             "| claim_id | claim | evidence_tag | authority | status | external_effect |",
             "|" + "---|" * 6,
             "| C-001 | 联调窗口缺陷清零 | FACT | consultative | accepted |"
             " internal_only |", ""]
    return "\n".join(body) + "\n"


def _fx_n1():
    # 真实联调要求（REQ-001 req=integration），主张 required_environment=mock、
    # exemption=none、无 required_change_record → R4·第三支
    return {"kind": "gate-outbound",
            "text": _register([{}], [dict(required_environment="mock")]),
            "expect": {("R4", 3)}}


def _fx_n2():
    # required_checks 含 security、actual_checks 缺 security、exemption=none → R4·第一支
    return {"kind": "gate-outbound",
            "text": _register([{}], [dict(actual_checks="functional")]),
            "expect": {("R4", 1)}}


def _fx_n3():
    # approver=human:pm 在位、actual_environment=unverified、qa_result=passed_at_actual → R4·第二支
    return {"kind": "gate-outbound",
            "text": _register([{}], [dict(actual_environment="unverified")]),
            "expect": {("R4", 2)}}


def _fx_n4():
    # 降级 exemption=partial 无 fallback_criterion 无表 D reopen_trigger → R5·第二支
    # （reason/scope 在位 → R5·第一支不红；approver=human:pm → 人工闸不红）
    return {"kind": "validate",
            "text": _register([{}], [dict(exemption="partial", reason="窗口顺延",
                                          scope="security 项")]),
            "expect": {("R5", 2)}}


def _fx_n5():
    # evidence_tag=UNKNOWN 写成 authority=binding → R8·第一支
    # isolation：R8 归属 gate-outbound → 夹具按声明支所属子命令跑（表 D 默认行满足 R4、
    # 无外发门 → R6/R9/R15 零红）。validate 面隔离参考：customer_request×binding＝
    # 「条件」格，approver=human:pm＋status=accepted＋expiry 非 none＋cite: 在位→条件满足；
    # R13·③ approver human:pm 且 ref 与 decision_owner（human:pm）同值不红。
    return {"kind": "gate-outbound",
            "text": _register([dict(evidence_tag="UNKNOWN", authority="binding",
                                    decision_owner="human:pm",
                                    linked_artifacts="source:DOC-001;cite:DOC-001#3.2")],
                              [{}]),
            "expect": {("R8", 1)}}


def _fx_n6():
    # 内部 frozen_assumption 主张被外发件引作外部确认 → R9·第一支
    # （frozen 三列齐非 none → R5·③不红；引用区 claims=C-001 一致 → R15 不红；
    #  external_effect=internal_only 不配 outbound_authorized → R6 不红）
    return {"kind": "gate-outbound",
            "text": _outbound(send_channel="approved_send")
            + "\n" + _register([dict(status="frozen_assumption", review_owner="seat:lead",
                                     reopen_trigger="客户要求变更时重开")], [{}]),
            "expect": {("R9", 1)}}


def _fx_n7():
    # 完备性断言 cleared 而 remaining_count=1 → R12·第一支
    # （enumeration 12 ≥ base 12 → ②不红；assertion_form=qualitative＋文本不含
    #  语境化模式 → R14 不红；表 A comparability_ref=none → R14·③不红）
    return {"kind": "reconcile",
            "text": _register(
                [{}], [{}],
                b_rows=["| CMP-001 | 缺陷清单 | completeness | resolved | cleared | 12 | 1 |"
                        " C-001 | artifact:QAV-001 |"]),
            "expect": {("R12", 1)}}


def _fx_n8():
    # actual_environment=production 但 linked_artifacts 无 artifact: → R2·第三支
    # （R2 归属 validate → 按声明支所属子命令跑；artifact:TKT-001 去除后
    #  source: 仍在 → R2·①不红；R1/R5/R7/R14/R16 默认面不红）
    return {"kind": "validate",
            "text": _register([dict(linked_artifacts="source:DOC-001")],
                              [dict(actual_environment="production")]),
            "expect": {("R2", 3)}}


def _fx_n10():
    # completeness 断言 enumeration_count(5) < REQ-001 req_enumeration_base(12) → R12·第二支
    # （cleared＋remaining 0 → ①不红）
    return {"kind": "reconcile",
            "text": _register(
                [{}], [{}],
                b_rows=["| CMP-001 | 缺陷清单 | completeness | resolved | cleared | 5 | 0 |"
                        " C-001 | artifact:QAV-001 |"]),
            "expect": {("R12", 2)}}


NEGATIVE_SAMPLES = [
    ("N1", "R4·第三支", "表 C `req_required_environment` 比较目标", _fx_n1),
    ("N2", "R4·第一支", "集合包含比较目标", _fx_n2),
    ("N3", "R4·第二支", "环境轴 `unverified` 与 `qa_result` 的相容目标", _fx_n3),
    ("N4", "R5·第二支", "表 D 两列非 `none` 约束", _fx_n4),
    ("N5", "R8·第一支", "`evidence_tag`×`authority` 相容目标", _fx_n5),
    ("N6", "R9·第一支", "`status`×外发引用面", _fx_n6),
    ("N7", "R12·第一支", "`completeness_mode` 与 `remaining_count` 的取 0 目标", _fx_n7),
    ("N8", "R2·第三支", "`actual_environment`×`artifact:` 存在性目标", _fx_n8),
    # N9：不可机检——由人工闸 A1 承接（零机检实现，见 MANUAL_GATE_CARRYOVER）
    ("N9", "**不可机检**——由人工闸 A1 承接", "读数件时间戳在本契约管辖的字段面之外", None),
    ("N10", "R12·第二支", "表 C 枚举基数比较目标", _fx_n10),
]


def _run_on(art, kind, cs, V):
    if kind == "validate":
        check_r1(art, cs, V); check_r2(art, cs, V); check_r5(art, cs, V)
        check_r7(art, cs, V); check_r14(art, cs, V); check_r16(art, cs, V)
        human_gate_validate(art, cs, V)
    elif kind == "reconcile":
        arts = [art]
        check_r3(arts, cs, V); check_r10(arts, cs, V); check_r11(arts, cs, V)
        check_r12(arts, cs, V); check_r13(arts, cs, V); check_r17(arts, cs, V)
        human_gate_reconcile(arts, cs, V)
    else:
        check_r4(art, cs, V); check_r6(art, cs, V); check_r8(art, cs, V)
        check_r9(art, cs, V); check_r15(art, cs, V)
        human_gate_outbound(art, cs, V)


def run_fixture(name, cs, tmpdir):
    fns = {nid: fn for (nid, _b, _s, fn) in NEGATIVE_SAMPLES if fn is not None}
    if name not in fns:
        return None
    fx = fns[name]()
    p = os.path.join(tmpdir, f"fixture_{name}.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write(fx["text"])
    V = Violations()
    art = Artifact(p)
    _run_on(art, fx["kind"], cs, V)
    got = V.pairs()
    hard = {(s, b) for (s, b) in got
            if not s.startswith(("RECHECK", "HUMAN-GATE", "REQUIRED-FACE"))}
    declared = fx["expect"]
    return {"declared": sorted(declared), "got": sorted(got),
            "declared_red": declared <= got,
            "no_stray_r_violation": hard <= declared,
            "exit": EXIT_FAIL if V.items else EXIT_PASS}


def cmd_fixtures(args, cs):
    """内嵌夹具逐条实跑（V5 自证入口）。"""
    ok_all = True
    with tempfile.TemporaryDirectory() as td:
        for (nid, branch, gen, fn) in NEGATIVE_SAMPLES:
            if fn is None:
                print(f"{nid}: 不可机检·人工闸承接登记·机检实现数 0")
                continue
            r = run_fixture(nid, cs, td)
            line_ok = r["declared_red"] and r["no_stray_r_violation"] and r["exit"] != 0
            ok_all = ok_all and line_ok
            print(f"{nid} 声明支={branch} 声明支变红={r['declared_red']} "
                  f"零顺带R命中={r['no_stray_r_violation']} exit={r['exit']} "
                  f"{'PASS' if line_ok else 'FAIL'} got={r['got']}")
    return EXIT_PASS if ok_all else EXIT_FAIL


# ════════════════════════════════════════════════════════════════════════
# 同源自证（V6）：配置 ↔ 真源逐字全等／规范化摘要全等＋四类变异造红
# ════════════════════════════════════════════════════════════════════════
def _sec(lines, heading):
    try:
        h = lines.index(heading)
    except ValueError:
        return None
    nxt = None
    for i in range(h + 1, len(lines)):
        if lines[i].startswith("## ") or (lines[i].startswith("# ")
                                          and not lines[i].startswith("## ")):
            nxt = i
            break
    return lines[h + 1: nxt if nxt is not None else len(lines)]


def _find(lines, pred, start=0):
    for i in range(start, len(lines)):
        if pred(lines[i]):
            return i
    return -1


def _split_cells(ln):
    r"""单元格切分：`\|`（正则转义竖线）不是分隔符——仅在未转义 `|` 处切。"""
    tmp = ln.strip()
    if tmp.startswith("|"):
        tmp = tmp[1:]
    if tmp.endswith("|") and not tmp.endswith("\\|"):
        tmp = tmp[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", tmp)]


def _md_table(bl, header_first_cell, include_header=False):
    hi = _find(bl, lambda l: l.startswith("| " + header_first_cell + " |"))
    if hi < 0:
        return None
    rows = []
    if include_header:
        rows.append(_split_cells(bl[hi]))
    i = hi + 2
    while i < len(bl) and bl[i].startswith("|"):
        cells = _split_cells(bl[i])
        if any(cells):
            rows.append(cells)
        i += 1
    return rows


def _md_table_at(bl, header_prefix):
    hi = _find(bl, lambda l: l.startswith(header_prefix))
    if hi < 0:
        return None
    rows = []
    i = hi + 2
    while i < len(bl) and bl[i].startswith("|"):
        cells = _split_cells(bl[i])
        if any(cells):
            rows.append(cells)
        i += 1
    return rows


def _line_sw(bl, prefix):
    i = _find(bl, lambda l: l.startswith(prefix))
    return bl[i] if i >= 0 else None


def _line_ct(bl, needle):
    i = _find(bl, lambda l: needle in l)
    return bl[i] if i >= 0 else None


def _ol(bl):
    return [l for l in bl if re.match(r"^\d+\. ", l)]


def _bullets(bl):
    return [l for l in bl if l.startswith("- ")]


def _register_headers(lines):
    out = {}
    for key, heading in (("A", "## 表 A · 主张登记（20 列）"),
                         ("B", "## 表 B · 可比对断言登记（9 列）"),
                         ("C", "## 表 C · 标识与需求主表登记（7 列）"),
                         ("D", "## 表 D · 主张级验证登记（13 列）")):
        sr = _sec(lines, heading)
        if sr is None:
            return None
        hi = _find(sr, lambda l: l.startswith("|")
                   and (lambda b: bool(b) and not b <= set("-: "))(
                       set(l.replace("|", "").strip())))
        if hi < 0:
            return None
        out[key] = [x.strip() for x in sr[hi].strip().strip("|").split("|")]
    return out


def reextract(cs, src_lines):
    """按配置 extract 节从真源再抽取 → {(group_id, sub): (配置值, 再抽取值, compare)}。"""
    def do_extract(spec, lines):
        k = spec["kind"]
        bl = _sec(lines, spec["after_heading"]) if "after_heading" in spec else lines
        if bl is None:
            return None
        if k == "md_table":
            return _md_table(bl, spec["header_first_cell"],
                             include_header=bool(spec.get("include_header")))
        if k == "md_table_at":
            return _md_table_at(bl, spec["header_prefix"])
        if k == "line_startswith":
            return _line_sw(bl, spec["prefix"])
        if k == "line_contains":
            return _line_ct(bl, spec["needle"])
        if k == "ordered_list":
            return _ol(bl)
        if k == "bullet_list":
            return _bullets(bl)
        if k == "para_pair":
            return [_line_sw(bl, p) for p in spec["prefixes"]]
        if k == "register_table_headers":
            return _register_headers(lines)
        return None

    out = {}
    for gid, g in cs.groups.items():
        entries = []
        if "extract" in g:
            entries.append(("", g))
        for sub, sg in g.items():
            if isinstance(sg, dict) and "extract" in sg:
                entries.append((sub, sg))
        for sub, sg in entries:
            spec = sg["extract"]
            got = do_extract(spec, src_lines[spec["file"]])
            out[(gid, sub)] = (sg["values"], got, sg["compare"])
    return out


def _values_equal(a, b):
    return json.dumps(a, ensure_ascii=False, sort_keys=True) == \
        json.dumps(b, ensure_ascii=False, sort_keys=True)


def _norm(v):
    if isinstance(v, str):
        return re.sub(r"\s+", " ", v.replace("\\|", "|")).strip()
    if isinstance(v, list):
        return [_norm(x) for x in v]
    if isinstance(v, dict):
        return {k: _norm(x) for k, x in v.items()}
    return v


def _build_mutations(pairs):
    """四类变异（对齐 T1 夹具 c05/c13/c14/c27 同族判据）：等长反义改写／值漂移／
    常量改义／列序互换——各打一处，比对必须造红。"""
    muts = []
    # 1 等长反义改写：组 2 引用形态行内「后接」→「前连」（2 字等长反义改写）
    key2 = ("g2_reference_prefixes", "")
    cfgv, got, _ = pairs[key2]
    assert "后接" in cfgv, "变异源锚点缺失：后接"
    muts.append(("equal-length-antonym", key2, cfgv.replace("后接", "前连", 1), got))
    # 2 值漂移：组 7 外发门 outbound_type 一闭集值末字符漂移
    key7 = ("g7_outbound_gate_6fields", "")
    cfgv, got, _ = pairs[key7]
    drift = [row[:] for row in cfgv]
    assert any("risk_notice" in r[1] for r in drift), "变异源锚点缺失：risk_notice"
    drift[0][1] = drift[0][1].replace("risk_notice", "risk_noticf")
    muts.append(("value-drift", key7, drift, got))
    # 3 常量改义：组 4 环境轴全序比较符 ＜ → ≤（序语义改义）
    key4 = ("g4_table_d_13cols", "env_axis")
    cfgv, got, _ = pairs[key4]
    assert "＜" in cfgv, "变异源锚点缺失：＜"
    muts.append(("constant-resema", key4, cfgv.replace("＜", "≤"), got))
    # 4 列序互换：组 5 表 A 表头前两列互换
    key5 = ("g5_tables_b_c_headers", "table_headers")
    cfgv, got, _ = pairs[key5]
    swap = {k: list(v) for k, v in cfgv.items()}
    swap["A"][0], swap["A"][1] = swap["A"][1], swap["A"][0]
    muts.append(("column-swap", key5, swap, got))
    return muts


def cmd_selfcheck(args, cs):
    """自证入口：14 组逐组 配置值 ↔ 真源再抽取 全等；随后四类变异全数造红。"""
    src_tags = cs.cfg["_meta"]["source_files"]
    root = pack_root()
    base = os.path.dirname(os.path.dirname(root))  # 交付仓根（包根上两级）
    src_lines = {}
    for tag, rel in src_tags.items():
        p = rel if os.path.isabs(rel) else os.path.join(base, rel)
        with open(p, encoding="utf-8") as f:
            src_lines[tag] = f.read().split("\n")
    pairs = reextract(cs, src_lines)
    fail = 0
    for (gid, sub), (cfgv, got, _cmp) in sorted(pairs.items()):
        name = gid if not sub else f"{gid}.{sub}"
        equal = _values_equal(cfgv, got)
        norm_eq = _values_equal(_norm(cfgv), _norm(got))
        ok = equal or norm_eq
        if not ok:
            fail += 1
        print(f"GROUP {name}: exact={equal} normalized={norm_eq} {'OK' if ok else 'RED'}")
    print(f"SELFPROOF groups_compared={len(pairs)} red={fail}")
    muts = _build_mutations(pairs)
    red = 0
    for mname, mkey, mcfg, mgot in muts:
        hit = (not _values_equal(mcfg, mgot)) and (not _values_equal(_norm(mcfg), _norm(mgot)))
        red += 1 if hit else 0
        print(f"MUTATION {mname} target={'.'.join(mkey)}: detected={hit} "
              f"{'OK-RED' if hit else 'MISSED'}")
    print(f"SELFPROOF mutations_total={len(muts)} red={red}")
    if fail or red != len(muts):
        return EXIT_FAIL
    return EXIT_PASS


# ════════════════════════════════════════════════════════════════════════
# CLI（三子命令名称与参数逐字照 30-gates §3 调用契约表；selfcheck/fixtures/
# allocation 为自证辅助子命令，不属调用契约面）
# ════════════════════════════════════════════════════════════════════════
def main(argv=None):
    ap = argparse.ArgumentParser(prog="semantic-governance.py",
                                 description="主张—承诺契约共享强制层校验（30-gates §3）")
    ap.add_argument("--config", default=default_config_path(),
                    help="闭集配置路径（缺省＝包根 config/semantic-closed-sets.json）")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("validate")
    p1.add_argument("--artifact", required=True)
    p1.add_argument("--kind", required=True)
    p2 = sub.add_parser("reconcile")
    p2.add_argument("--artifacts", required=True)
    p3 = sub.add_parser("gate-outbound")
    p3.add_argument("--artifact", required=True)
    sub.add_parser("selfcheck")
    sub.add_parser("fixtures")
    sub.add_parser("allocation")  # 打印判据归属映射（V2 抽取面）
    args = ap.parse_args(argv)
    cs = ClosedSets(args.config)
    if args.cmd == "validate":
        return cmd_validate(args, cs)
    if args.cmd == "reconcile":
        return cmd_reconcile(args, cs)
    if args.cmd == "gate-outbound":
        return cmd_gate_outbound(args, cs)
    if args.cmd == "selfcheck":
        return cmd_selfcheck(args, cs)
    if args.cmd == "fixtures":
        return cmd_fixtures(args, cs)
    if args.cmd == "allocation":
        print(json.dumps({"R_ALLOCATION": R_ALLOCATION,
                          "HUMAN_GATE_ALLOCATION": HUMAN_GATE_ALLOCATION,
                          "MANUAL_GATE_CARRYOVER": MANUAL_GATE_CARRYOVER},
                         ensure_ascii=False, indent=2))
        return EXIT_PASS
    return EXIT_USAGE


if __name__ == "__main__":
    sys.exit(main())
