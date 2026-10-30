#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fuxi-skill S0a 断言工具骨架（结构层门禁·机械断言，不依赖人工校准）。

断言目录＝同目录 `assertion-catalog.md`（18 项：ST-1..5／BW-1..4／FC-1..5／GS-1..4）。
本件与目录一一对应：每项目录断言有对应函数（当期可执行项＝实装；
〔S1-S3 执行〕项＝桩＋显式 PENDING_STAGE 读数，不算 fail 不算 pass，汇总单列）。

退出码闭集（三值，无其他取值）：
    0 全绿（无 fail；PENDING_STAGE 不拉码）
    1 有 fail
    2 工具自身错误（用法错／环境错／内部异常，fail-closed 不得吞成 0）

确定性：全部断言为确定性判据——无随机种子、无时钟参与读数、无网络；
同输入连跑两次退出码与逐项读数全等。

用法：
    python assert-tool.py            # 仓内执行模式：跑 18 项，当期实装项出读数，余者 PENDING_STAGE
    python assert-tool.py selftest   # 自证模式：内存构造正负样本，逐类断言「能咬能放」
"""

from __future__ import annotations

import re
import sys

# ---- 退出码闭集 ----
EXIT_GREEN = 0
EXIT_FAIL = 1
EXIT_TOOL_ERROR = 2

# ---- 读数闭集（单条断言的三种读数，无其他取值）----
READ_PASS = "PASS"
READ_FAIL = "FAIL"
READ_PENDING = "PENDING_STAGE"

# ============================================================
# 词表与闭集注册位（词表本体落盘＝BW-1／BW-2 当期可执行判据的对象）
# ============================================================

# BW-1 角色扮演句式禁语词表（承载位＝perspective 规范总则「HOW they think
# 不是 WHAT they said」＋「非角色扮演」声明；命中即产物违规）。
ROLEPLAY_BANNED_WORDS = (
    "以他的名义",
    "扮演他",
    "模仿他的语气",
    "假装他是",
    "现在我就是他",
)

# BW-2 「无据斩钉截铁」启发式词表（无据断言触发词）。
BLUNT_ASSERTION_WORDS = (
    "必然会",
    "毫无疑问",
    "他一定会",
    "只能是",
    "历来如此",
)

# BW-2 拒答/弃权四档口径标注位（闭集注册）。
ABSTAIN_TIERS = ("有支持", "有限定", "无支持但貌似合理", "明确幻觉")

# BW-3 口径三件套关键词（裸数字邻近语境必含）。
NUMBER_CONTEXT_KEYS = ("统计口径", "样本量", "一致性系数")

# FC-1 两字段闭集（两轴正交）。
EVIDENCE_GRADES = ("人工验证", "机械断言", "LLM 判定")
CALIBRATION_STATES = ("校准态", "待校准")

# ST-3 perspective 五层节闭集／technique 六段卡＋五字段闭集。
PERSPECTIVE_SECTIONS = ("表达DNA", "心智模型", "决策启发式", "反模式", "诚实边界")
TECHNIQUE_CARD_SECTIONS = ("R", "I", "A1", "A2", "E", "B")
TECHNIQUE_CARD_FIELDS = ("出处", "触发", "步骤", "边界", "验证状态")

# ST-4 test-prompts 条目字段闭集。
TEST_PROMPT_FIELDS = ("用例id", "题面", "期望档位", "所属轨", "是否锚点题")

# ST-5 coverage-audit 三问字段。
COVERAGE_AUDIT_FIELDS = ("哪些留下", "哪些扔了", "为什么")

# FC-2 三文件注册字段名闭集（S1 起草时扩充，骨架期＝基线集）。
KERNEL_FIELD_REGISTRY = ("evidence_grade", "calibration_state", "source_id", "位置")

# FC-4 状态词表取值闭集＋看板三栏字段名闭集。
STATE_WORDS = ("needs_review", "active", "归档区", "待校准", "未验")
BOARD_COLUMNS = ("本轮改动", "触发的坏信号", "人工闸结论")

# GS-1/GS-2 gate_source 白名单（person 软门类／method 硬门类；互斥＝双向断言基面）。
PERSON_GATE_WHITELIST = ("盲评rubric", "绝对线", "decoy", "泄漏检查", "人工锚点卡")
METHOD_GATE_WHITELIST = ("机械断言", "三臂对照", "诱饵测试", "留出集")

# 共享内核三文件名（ST-2 对象；S1 建成前不存在＝执行位 S1）。
KERNEL_THREE_FILES = ("evidence-grading", "failure-modes", "artifact-contract")

_PERCENT_RE = re.compile(r"\d+(?:\.\d+)?\s*%")
_NUMBER_METRIC_RE = re.compile(r"(?:通过率|一致率|占比)[^\d]{0,8}\d+(?:\.\d+)?")


# ============================================================
# 核心判据函数（纯函数·确定性；selftest 正负样本即对它们咬放）
# ============================================================

def banned_phrase_hits(text: str, banned: "tuple[str, ...]") -> "list[str]":
    """BW-1 禁语命中：返回命中词表（空＝放）。"""
    return [w for w in banned if w in text]


def blunt_hits(text: str, triggers: "tuple[str, ...]") -> "list[str]":
    """BW-2 无据斩钉截铁命中：返回触发词（空＝放）。"""
    return [w for w in triggers if w in text]


def bare_number_hits(report_text: str) -> "list[str]":
    """BW-3 裸数字检出：数字（百分比/通过率类）所在行缺口径三件套任一＝裸数字。

    判定粒度＝行（确定性、无跨行猜测）：行内含数字 token 且三件套关键词齐备才放。
    """
    hits: "list[str]" = []
    for lineno, line in enumerate(report_text.split("\n"), 1):
        if _PERCENT_RE.search(line) or _NUMBER_METRIC_RE.search(line):
            missing = [k for k in NUMBER_CONTEXT_KEYS if k not in line]
            if missing:
                hits.append("line%d 缺%s" % (lineno, "、".join(missing)))
    return hits


def field_value_closed_ok(record: "dict[str, str]", registry: "dict[str, tuple[str, ...]]") -> bool:
    """FC-1 字段取值闭集：每个注册字段的取值必须落在对应闭集内。"""
    for field, allowed in registry.items():
        if field not in record or record[field] not in allowed:
            return False
    return True


def section_diff(sections: "tuple[str, ...]", registry: "tuple[str, ...]") -> "tuple[set, set]":
    """ST-3 节闭集 diff：返回 (多出集, 缺失集)；两集皆空＝diff＝∅。"""
    got = set(sections)
    want = set(registry)
    return (got - want, want - got)


def test_prompt_entries_ok(entries: "list[dict[str, str]]") -> bool:
    """ST-4 test-prompts 条目字段闭集：条目非空且每条字段集合 ⊆ 注册闭集。"""
    if not entries:
        return False
    allowed = set(TEST_PROMPT_FIELDS)
    for entry in entries:
        if not entry or not set(entry) <= allowed:
            return False
    return True


def coverage_audit_ok(rejected_listing: "list[str]", audit: "dict[str, str]") -> bool:
    """ST-5 rejected/ 可枚举（listing 可为空表＝可枚举态）＋audit 三问字段齐备非空。"""
    if rejected_listing is None:
        return False
    return all(audit.get(k, "").strip() for k in COVERAGE_AUDIT_FIELDS)


def b_segment_ok(cards: "list[dict[str, str]]") -> bool:
    """BW-4 technique 卡 B 段存在且非空占位。"""
    if not cards:
        return False
    return all(card.get("B", "").strip() for card in cards)


def unknown_field_names_diff(used: "tuple[str, ...]", registry: "tuple[str, ...]") -> bool:
    """FC-2 未注册字段 diff＝∅：used 中不属于注册闭集的字段数＝0。"""
    return not (set(used) - set(registry))


def paired_fields_ok(records: "list[dict[str, str]]") -> bool:
    """FC-3 source_id＋位置双形态成对：任一侧出现则另一侧必须在场。"""
    for rec in records:
        has_id = bool(rec.get("source_id", "").strip())
        has_loc = bool(rec.get("位置", "").strip())
        if has_id != has_loc:
            return False
    return True


def state_vocab_closed_ok(used_states: "tuple[str, ...]", used_columns: "tuple[str, ...]") -> bool:
    """FC-4 状态词表取值闭集＋看板三栏字段名闭集（两 diff 皆空）。"""
    return (not (set(used_states) - set(STATE_WORDS))
            and not (set(used_columns) - set(BOARD_COLUMNS)))


def ns_borrow_hits(bundle: "dict[str, dict[str, str]]") -> "list[str]":
    """FC-5 bundle 两命名空间互借检出：persona 层引用 technique 层分数（或反向）命中列表。"""
    hits: "list[str]" = []
    persona = bundle.get("persona", {})
    technique = bundle.get("technique", {})
    for layer, body in (("persona", persona), ("technique", technique)):
        for key, value in body.items():
            if "分数" in key and "层借用" in value:
                hits.append("%s.%s" % (layer, key))
    return hits


def gate_source_hits(track: str, gate_source: str) -> "list[str]":
    """GS-1/GS-2 轨白名单命中：返回越轨判据命中列表（空＝放）。

    person 轨禁 method 硬门判据（method 白名单即 person 侧禁区），对称反之。
    """
    if track == "person":
        return [gate_source] if gate_source in METHOD_GATE_WHITELIST and gate_source not in PERSON_GATE_WHITELIST else []
    if track == "method":
        return [gate_source] if gate_source in PERSON_GATE_WHITELIST and gate_source not in METHOD_GATE_WHITELIST else []
    return ["未知轨:%s" % track]


def calibration_consistent(calibration_state: str, kappa_report: "dict[str, float] | None") -> bool:
    """GS-4 calibration_state 与 κ 报告一致性（fail-closed）。

    规则（确定性）：κ 报告缺失＝状态只能为「待校准」；κ 报告在场且点值与区间
    下界均 ≥ 门槛＝只允许「校准态」；其余组合一律不一致（不一致→待校准阻断放行）。
    """
    threshold = 0.6
    if kappa_report is None:
        return calibration_state == "待校准"
    point = kappa_report.get("点值", 0.0)
    lower = kappa_report.get("区间下界", 0.0)
    calibrated = point >= threshold and lower >= threshold
    if calibrated:
        return calibration_state == "校准态"
    return calibration_state == "待校准"


def vocab_body_present(vocab: "tuple[str, ...]") -> bool:
    """词表本体在场判据：非空元组且条目均为非空字符串。"""
    return bool(vocab) and all(isinstance(w, str) and w.strip() for w in vocab)


# ============================================================
# 18 项目录断言 ↔ 函数桩（当期实装＝BW-1／BW-2；余者 PENDING_STAGE）
# ============================================================

def st_1_contract_file() -> "tuple[str, str]":
    """ST-1 产物契约文件存在可解析——〔S0a 建／S1 执行〕。"""
    return (READ_PENDING, "S1")


def st_2_three_kernel_files() -> "tuple[str, str]":
    """ST-2 evidence-grading／failure-modes／artifact-contract 三文件存在——〔S0a 建／S1 执行〕。"""
    return (READ_PENDING, "S1")


def st_3_section_closed_diff() -> "tuple[str, str]":
    """ST-3 perspective 五层节／technique 六段卡＋五字段闭集 diff＝∅——〔S0a 建／S1 执行〕。"""
    return (READ_PENDING, "S1")


def st_4_test_prompts() -> "tuple[str, str]":
    """ST-4 test-prompts 存在可解析＋条目字段闭集——〔S0a 建／S1 执行〕。"""
    return (READ_PENDING, "S1")


def st_5_rejected_coverage() -> "tuple[str, str]":
    """ST-5 rejected/ 可枚举＋coverage-audit 三问字段——〔S0a 建／S1 执行〕。"""
    return (READ_PENDING, "S1")


def bw_1_roleplay_vocab() -> "tuple[str, str]":
    """BW-1 角色扮演禁语词表本体落盘——〔S0a〕当期可执行（词表本体在场类）。"""
    ok = vocab_body_present(ROLEPLAY_BANNED_WORDS)
    return (READ_PASS if ok else READ_FAIL, "词表条目 %d" % len(ROLEPLAY_BANNED_WORDS))


def bw_2_blunt_vocab_tiers() -> "tuple[str, str]":
    """BW-2 无据斩钉截铁词表＋四档口径标注位——〔S0a〕当期可执行（词表本体在场类）。"""
    ok = (vocab_body_present(BLUNT_ASSERTION_WORDS)
          and len(set(ABSTAIN_TIERS)) == 4
          and vocab_body_present(ABSTAIN_TIERS))
    return (READ_PASS if ok else READ_FAIL, "触发词 %d·档位 %d" % (len(BLUNT_ASSERTION_WORDS), len(ABSTAIN_TIERS)))


def bw_3_bare_number_rule() -> "tuple[str, str]":
    """BW-3 裸数字检出规则——〔S0a 建／S1 执行〕（检出器已就位＝bare_number_hits，产物报告待 S1）。"""
    return (READ_PENDING, "S1")


def bw_4_b_segment_decl() -> "tuple[str, str]":
    """BW-4 technique 卡 B 段边界声明存在——〔S0a 建／S1 执行〕。"""
    return (READ_PENDING, "S1")


def fc_1_two_field_closedset() -> "tuple[str, str]":
    """FC-1 evidence_grade／calibration_state 两字段闭集——〔S0a 建／S1 执行〕。"""
    return (READ_PENDING, "S1")


def fc_2_kernel_fields_diff() -> "tuple[str, str]":
    """FC-2 三文件字段名闭集未注册字段 diff＝∅——〔S0a 建／S1 执行〕。"""
    return (READ_PENDING, "S1")


def fc_3_paired_source_location() -> "tuple[str, str]":
    """FC-3 source_id＋位置双形态字段成对——〔S0a 建／S1 执行〕。"""
    return (READ_PENDING, "S1")


def fc_4_state_vocab_board() -> "tuple[str, str]":
    """FC-4 状态词表取值闭集＋看板三栏字段名闭集——〔S0a 建／S1 执行〕。"""
    return (READ_PENDING, "S1")


def fc_5_bundle_ns_isolation() -> "tuple[str, str]":
    """FC-5 bundle 两层验证状态命名空间隔离互借检出＝0——〔S0a 建／S2 执行〕。"""
    return (READ_PENDING, "S2")


def gs_1_person_gate_source() -> "tuple[str, str]":
    """GS-1 person 轨 gate_source 白名单（调 method 硬门判据命中＝0）——〔S0a 建／S3 执行〕。"""
    return (READ_PENDING, "S3")


def gs_2_method_gate_source() -> "tuple[str, str]":
    """GS-2 method 轨 gate_source 对称白名单——〔S0a 建／S3 执行〕。"""
    return (READ_PENDING, "S3")


def gs_3_bidirectional_zero_mismatch() -> "tuple[str, str]":
    """GS-3 双向断言不匹配数＝0（S3 硬验收位不变，当期只建工具）——〔S0a 建／S3 执行〕。"""
    return (READ_PENDING, "S3")


def gs_4_calibration_kappa() -> "tuple[str, str]":
    """GS-4 calibration_state 与 κ 报告一致性校验器（κ 读数待 S0b）——〔S0a 建／S0b·S1 执行〕。"""
    return (READ_PENDING, "S0b")


ASSERTIONS: "list[tuple[str, str]]" = [
    ("ST-1", "st_1_contract_file"),
    ("ST-2", "st_2_three_kernel_files"),
    ("ST-3", "st_3_section_closed_diff"),
    ("ST-4", "st_4_test_prompts"),
    ("ST-5", "st_5_rejected_coverage"),
    ("BW-1", "bw_1_roleplay_vocab"),
    ("BW-2", "bw_2_blunt_vocab_tiers"),
    ("BW-3", "bw_3_bare_number_rule"),
    ("BW-4", "bw_4_b_segment_decl"),
    ("FC-1", "fc_1_two_field_closedset"),
    ("FC-2", "fc_2_kernel_fields_diff"),
    ("FC-3", "fc_3_paired_source_location"),
    ("FC-4", "fc_4_state_vocab_board"),
    ("FC-5", "fc_5_bundle_ns_isolation"),
    ("GS-1", "gs_1_person_gate_source"),
    ("GS-2", "gs_2_method_gate_source"),
    ("GS-3", "gs_3_bidirectional_zero_mismatch"),
    ("GS-4", "gs_4_calibration_kappa"),
]


# ============================================================
# selftest：正负样本自证每类断言能咬能放
# ============================================================

def _selftest_cases() -> "list[tuple[str, bool, bool]]":
    """返回 (用例名, 判据结果, 期望结果) 列表；任一不符即 selftest 红。

    覆盖七类判据核心各一对正负样本（咬＝期望 False/有命中，放＝期望 True/无命中）。
    """
    cases: "list[tuple[str, bool, bool]]" = []

    # BW-1 禁语：放／咬
    cases.append(("BW1_pass", banned_phrase_hits("他用这套框架分析了问题", ROLEPLAY_BANNED_WORDS) == [], True))
    cases.append(("BW1_bite", banned_phrase_hits("接下来我以他的名义作答", ROLEPLAY_BANNED_WORDS) != [], True))

    # BW-2 斩钉截铁＋四档：放／咬＋档位闭集完整性
    cases.append(("BW2_pass", blunt_hits("有限定：他在公开场合表达过倾向", BLUNT_ASSERTION_WORDS) == [], True))
    cases.append(("BW2_bite", blunt_hits("他必然会否决这个方案", BLUNT_ASSERTION_WORDS) != [], True))
    cases.append(("BW2_tiers", len(set(ABSTAIN_TIERS)) == 4, True))

    # BW-3 裸数字：带三件套放／裸数字咬
    with_ctx = "通过率 62%（统计口径：三臂对照；样本量 40；一致性系数见 κ 报告）"
    without_ctx = "通过率 62%，效果显著"
    cases.append(("BW3_pass", bare_number_hits(with_ctx) == [], True))
    cases.append(("BW3_bite", bare_number_hits(without_ctx) != [], True))

    # FC-1 两字段闭集：合法放／越界咬
    registry = {"evidence_grade": EVIDENCE_GRADES, "calibration_state": CALIBRATION_STATES}
    cases.append(("FC1_pass", field_value_closed_ok({"evidence_grade": "机械断言", "calibration_state": "待校准"}, registry), True))
    cases.append(("FC1_bite", field_value_closed_ok({"evidence_grade": "感觉可靠", "calibration_state": "待校准"}, registry), False))

    # ST-3 节闭集 diff：全等放／缺节多出各咬
    d1 = section_diff(PERSPECTIVE_SECTIONS, PERSPECTIVE_SECTIONS)
    d2 = section_diff(("表达DNA", "心智模型", "决策启发式", "反模式"), PERSPECTIVE_SECTIONS)
    d3 = section_diff(PERSPECTIVE_SECTIONS + ("执行步骤",), PERSPECTIVE_SECTIONS)
    cases.append(("ST3_pass", d1 == (set(), set()), True))
    cases.append(("ST3_bite_missing", d2 != (set(), set()), True))
    cases.append(("ST3_bite_extra_ir_mix", d3 != (set(), set()), True))
    t1 = section_diff(TECHNIQUE_CARD_SECTIONS, TECHNIQUE_CARD_SECTIONS)
    t2 = section_diff(("R", "I", "A1", "A2", "E"), TECHNIQUE_CARD_SECTIONS)
    cases.append(("ST3T_pass", t1 == (set(), set()), True))
    cases.append(("ST3T_bite", t2 != (set(), set()), True))

    # ST-4 test-prompts：合法放／未注册字段咬／空咬
    good_entry = [{"用例id": "tp01", "题面": "边缘题", "期望档位": "有限定", "所属轨": "person", "是否锚点题": "否"}]
    bad_entry = [{"用例id": "tp02", "自造字段": "x"}]
    cases.append(("ST4_pass", test_prompt_entries_ok(good_entry), True))
    cases.append(("ST4_bite_unknown", test_prompt_entries_ok(bad_entry), False))
    cases.append(("ST4_bite_empty", test_prompt_entries_ok([]), False))

    # ST-5 rejected/＋三问：齐备放／缺问咬／不可枚举咬
    cases.append(("ST5_pass", coverage_audit_ok([], {"哪些留下": "8 条", "哪些扔了": "5 条", "为什么": "跨域复现不足"}), True))
    cases.append(("ST5_bite_missing_q", coverage_audit_ok([], {"哪些留下": "8 条", "哪些扔了": "5 条"}), False))
    cases.append(("ST5_bite_unenum", coverage_audit_ok(None, {"哪些留下": "x", "哪些扔了": "y", "为什么": "z"}), False))

    # BW-4 B 段：非空放／空段咬
    cases.append(("BW4_pass", b_segment_ok([{"R": "原文", "B": "仅限高频决策场景"}]), True))
    cases.append(("BW4_bite_empty", b_segment_ok([{"R": "原文", "B": "  "}]), False))

    # FC-2 未注册字段 diff：注册内放／自造字段咬
    cases.append(("FC2_pass", unknown_field_names_diff(("evidence_grade", "source_id"), KERNEL_FIELD_REGISTRY), True))
    cases.append(("FC2_bite", unknown_field_names_diff(("evidence_grade", "自造字段"), KERNEL_FIELD_REGISTRY), False))

    # FC-3 成对字段：成对放／单侧咬
    cases.append(("FC3_pass", paired_fields_ok([{"source_id": "s1", "位置": "第三章"}]), True))
    cases.append(("FC3_bite", paired_fields_ok([{"source_id": "s1"}]), False))

    # FC-4 状态词表＋看板：闭集内放／越界咬
    cases.append(("FC4_pass", state_vocab_closed_ok(("needs_review", "未验"), BOARD_COLUMNS), True))
    cases.append(("FC4_bite", state_vocab_closed_ok(("彻底完成",), BOARD_COLUMNS), False))

    # FC-5 命名空间互借：隔离放／借分咬
    iso = {"persona": {"gate_source": "盲评rubric"}, "technique": {"gate_source": "机械断言"}}
    borrow = {"persona": {"分数": "借technique层借用机械断言分"}, "technique": {}}
    cases.append(("FC5_pass", ns_borrow_hits(iso) == [], True))
    cases.append(("FC5_bite", ns_borrow_hits(borrow) != [], True))

    # GS-1/GS-2 gate_source：白名单放／互套咬（双向）
    cases.append(("GS1_pass", gate_source_hits("person", "盲评rubric") == [], True))
    cases.append(("GS1_bite", gate_source_hits("person", "机械断言") != [], True))
    cases.append(("GS2_pass", gate_source_hits("method", "留出集") == [], True))
    cases.append(("GS2_bite", gate_source_hits("method", "人工锚点卡") != [], True))

    # GS-4 校准一致性：κ 达标＋校准态放／缺 κ 仍校准态咬／不一致咬
    good_kappa = {"点值": 0.7, "区间下界": 0.62}
    weak_kappa = {"点值": 0.65, "区间下界": 0.55}
    cases.append(("GS4_pass", calibration_consistent("校准态", good_kappa), True))
    cases.append(("GS4_pass_pending", calibration_consistent("待校准", None), True))
    cases.append(("GS4_bite_missing", calibration_consistent("校准态", None), False))
    cases.append(("GS4_bite_inconsistent", calibration_consistent("校准态", weak_kappa), False))

    # 词表本体在场（BW-1/BW-2 当期实装判据）：正咬反放自证
    cases.append(("VOCAB_pass", vocab_body_present(ROLEPLAY_BANNED_WORDS), True))
    cases.append(("VOCAB_bite_empty", vocab_body_present(()), False))
    cases.append(("VOCAB_bite_blank", vocab_body_present(("  ",)), False))

    return cases


def run_selftest() -> int:
    """逐例对拍：判据实际结果 ≠ 期望结果即记反常；全等 exit 0。"""
    failures = 0
    total = 0
    for name, actual, expected in _selftest_cases():
        total += 1
        if actual != expected:
            failures += 1
            print("selftest FAIL %s：判据返回 %r，期望 %r（不能咬或不能放）" % (name, actual, expected))
    print("selftest 用例 %d／反常 %d" % (total, failures))
    return EXIT_FAIL if failures else EXIT_GREEN


def run_assertions() -> int:
    """仓内执行模式：18 项逐项读数＋汇总单列（PASS／FAIL／PENDING_STAGE）。"""
    counts = {READ_PASS: 0, READ_FAIL: 0, READ_PENDING: 0}
    namespace = globals()
    for assert_id, fn_name in ASSERTIONS:
        fn = namespace.get(fn_name)
        if not callable(fn):
            # 函数缺失＝工具自身缺陷（工具侧欠账），按工具错误码收
            sys.stderr.write("tool error: 断言 %s 对应函数缺失：%s\n" % (assert_id, fn_name))
            return EXIT_TOOL_ERROR
        read, detail = fn()
        if read not in counts:
            sys.stderr.write("tool error: 断言 %s 读数 %r 不在闭集\n" % (assert_id, read))
            return EXIT_TOOL_ERROR
        counts[read] += 1
        print("%s %s %s" % (assert_id, read, detail))
    print("汇总 PASS=%d FAIL=%d PENDING_STAGE=%d 总数=%d"
          % (counts[READ_PASS], counts[READ_FAIL], counts[READ_PENDING], sum(counts.values())))
    return EXIT_FAIL if counts[READ_FAIL] else EXIT_GREEN


def main(argv: "list[str]") -> int:
    if len(argv) == 0:
        return run_assertions()
    if len(argv) == 1 and argv[0] == "selftest":
        return run_selftest()
    sys.stderr.write("usage error: 用法＝python assert-tool.py [selftest]（无其他参数）\n")
    return EXIT_TOOL_ERROR


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按工具错误码，不得吞成 0
        sys.stderr.write("tool error: %s\n" % exc)
        raise SystemExit(EXIT_TOOL_ERROR)
