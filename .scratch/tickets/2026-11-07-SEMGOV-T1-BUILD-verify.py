#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEMGOV-T1 v4 验收夹具。自票面 §3.0 的 python 围栏逐字提取即可独立运行。

用法：
  python3 verify.py <check-id> <pkg-dir>    单条检查，通过 exit 0，不通过 exit 1
  python3 verify.py --all <pkg-dir>         跑全部检查
  python3 verify.py --mutate <pkg-dir>      跑全部负样本（变异体），每条须让目标检查变红
  python3 verify.py --stats <pkg-dir>       打印全部计数读数（票面一切数字的唯一来源）
  python3 verify.py --selfcheck <pkg-dir>   夹具自证：变异锚唯一性、正则命中数、源码转义体检
  python3 verify.py --list                  列出检查编号与标题

设计口径（对应票面裁定三／裁定五／裁定六／裁定七）：
  · 规范真源句用「规范化后逐字全等」（tag=exact）或「条款 sha256／摘要比对」（tag=digest）；
    禁用长度阈值、禁用子串包含、禁用只验编号序列。**这三条禁令的对象是语义判据**；
    `len(l)==0`、SKILL.md 行数上限这类**结构性体量断言**不受禁（裁定三口径确认）。
  · 闭集值一律断言「该列取值集合 等于 闭集」，不是包含。
  · 每条负样本由「某条判据的某个比较目标」经固定算子生成，算子三类：del（删值）／
    rev（等长反义替换＝极性翻转）／pad（等长加噪）。rev 保持字符数与原文完全相等，
    因此长度阈值类弱判据在此一律无效。
  · 变异器与判据的失败必须分开计数：变异未生效（锚不存在／锚不唯一／文本未变）记
    MutateFailed 并使整轮失败；只有「变异已生效且目标判据抛红」才算咬住。
  · 一切计数由 --stats 打印，票面原样粘贴，不手写汇总。
"""
import hashlib
import inspect
import os
import re
import shutil
import sys
import tempfile

PKG_NAME = "claim-commitment-governance"
FILES = [
    "SKILL.md",
    "references/10-contract.md",
    "references/20-artifact-mapping.md",
    "references/30-gates.md",
    "references/40-provenance-map.md",
    "templates/claim-register.md",
    "templates/outbound-artifact.md",
]
REFERENCES = [
    "references/10-contract.md",
    "references/20-artifact-mapping.md",
    "references/30-gates.md",
    "references/40-provenance-map.md",
]
TRUE_SOURCE = "references/10-contract.md"
KEY = {
    "SKILL.md": "skill",
    "references/10-contract.md": "contract",
    "references/20-artifact-mapping.md": "mapping",
    "references/30-gates.md": "gates",
    "references/40-provenance-map.md": "prov",
    "templates/claim-register.md": "reg",
    "templates/outbound-artifact.md": "outb",
}
KEY_INV = {v: k for k, v in KEY.items()}


class Red(Exception):
    """判据抛红：被测件违反本判据。"""


class NotHere(Exception):
    """变异的锚不在本文件——换下一个文件试，不算失败。"""


class MutateFailed(Exception):
    """变异未生效：锚不存在／锚不唯一／文本未变。**使整轮失败**，不计入咬住。"""


# ---------------------------------------------------------------- 规范化与取域
def norm(s):
    """规范化：逐行去首尾空白→丢空行→连续空白压单空格。与 check-provenance 的条款摘要算法同口径。"""
    lines = [l.strip() for l in s.replace("\r\n", "\n").split("\n")]
    return re.sub(r"\s+", " ", " ".join(l for l in lines if l)).strip()


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def read(pkg, rel):
    p = os.path.join(pkg, rel)
    if not os.path.exists(p):
        raise Red("缺件 " + rel)
    with open(p, encoding="utf-8") as f:
        return f.read()


def split_row(line):
    """按未转义的 | 切分表格行，反斜杠转义的竖线保留为字面竖线。"""
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    cells = re.split(r"(?<!\\)\|", body)
    return [c.strip().replace("\\|", "|") for c in cells]


def parse_table(text, ncols, start=None):
    """解析首个 ncols 列表格；start 给定时只从该标题之后开始找。"""
    lines = text.replace("\r\n", "\n").split("\n")
    if start is not None:
        off = None
        for i, l in enumerate(lines):
            if l.strip() == start:
                off = i
                break
        if off is None:
            raise Red("找不到小节：" + start)
        lines = lines[off:]
    rows = []
    seen = False
    for l in lines:
        if not l.strip().startswith("|"):
            if seen:
                break
            continue
        cells = split_row(l)
        if len(cells) != ncols:
            continue
        if all(re.fullmatch(r"[:\- ]*", c) for c in cells):
            continue
        rows.append(cells)
        seen = True
    if not rows:
        raise Red("解析不到 %d 列表格" % ncols)
    return rows


def region(text, heading):
    lines = text.replace("\r\n", "\n").split("\n")
    st = None
    for i, l in enumerate(lines):
        if l.strip() == heading:
            st = i
            break
    if st is None:
        raise Red("找不到小节：" + heading)
    en = len(lines)
    for j in range(st + 1, len(lines)):
        if re.match(r"^##\s", lines[j]):
            en = j
            break
    return "\n".join(lines[st:en])


def resolve_section(text, label):
    """按 40-provenance-map 的小节标签取正文：`§N` 取 `## N.` 整节；`§表头` 取首部引用块；
    `§主类型段` 取 `**主类型**：` 行。三类均须**存在且唯一**——这就是裁定九要求的「验节存在」。"""
    lines = text.replace("\r\n", "\n").split("\n")
    if label == "表头":
        st = None
        for i, l in enumerate(lines):
            if l.startswith(">"):
                st = i
                break
        if st is None:
            raise Red("找不到表头引用块")
        en = st
        while en < len(lines) and lines[en].startswith(">"):
            en += 1
        return "\n".join(lines[st:en])
    if label == "主类型段":
        hits = [l for l in lines if l.startswith("**主类型**：")]
        if not hits:
            raise Red("找不到主类型段")
        if len(hits) > 1:
            raise Red("主类型段出现 %d 次（须唯一）" % len(hits))
        return hits[0]
    pat = (r"^##\s+%s\." % re.escape(label)) if label.isdigit() else (r"^##\s+%s\s*$" % re.escape(label))
    hits = [i for i, l in enumerate(lines) if re.match(pat, l)]
    if not hits:
        raise Red("所指节不存在：§%s" % label)
    if len(hits) > 1:
        raise Red("所指节标题重复 %d 次：§%s" % (len(hits), label))
    st = hits[0]
    en = len(lines)
    for j in range(st + 1, len(lines)):
        if re.match(r"^##\s", lines[j]):
            en = j
            break
    return "\n".join(lines[st:en])


def find_line(text, prefix):
    hits = [l for l in text.replace("\r\n", "\n").split("\n") if l.startswith(prefix)]
    if not hits:
        raise Red("找不到行首 " + prefix)
    if len(hits) > 1:
        raise Red("行首 %s 命中 %d 次（须唯一）" % (prefix, len(hits)))
    return hits[0]


def tokens(cell):
    return [t for t in re.findall(r"`([^`]+)`", cell)]


# ---------------------------------------------------------------- 等长反义算子
REV_PAIRS = [
    ("不得低于", "可以低于"), ("不得单独", "可以单独"), ("互不相同", "可以相同"),
    ("不得为", "可以为"), ("不自动", "即自动"), ("不等于", "就已经"),
    ("不删除", "可删除"), ("不改写", "可改写"), ("不依赖", "可依赖"),
    ("不回写", "可回写"), ("不复写", "可复写"), ("不声明", "即声明"),
    ("不声称", "就声称"), ("不证明", "即证明"), ("不参与", "即参与"), ("不单设", "要单设"),
    ("也不得", "也可以"), ("不得再", "仍可再"), ("不写死", "可写死"),
    ("不要求", "即要求"),
    ("不得被", "可以被"), ("不得含", "可以含"), ("不得跳", "可以跳"),
    ("不得", "可以"), ("不是", "就是"), ("禁止", "允许"),
    ("不算", "就算"), ("绝不", "必可"), ("必填", "选填"), ("取一", "取多"),
    ("小于", "大于"), ("晚于", "早于"), ("不足", "已足"), ("还缺", "已足"),
    ("截止", "起算"), ("待", "已"), ("非", "是"), ("无", "有"),
]


def reverse_text(s):
    out = s
    for a, b in REV_PAIRS:
        out = out.replace(a, b)
    return out


def _loc_index(lines, kind, key):
    """定位并断言**锚唯一**（裁定七：锚命中数必须恰为 1）。"""
    if kind == "region":
        hits = [i for i, l in enumerate(lines) if l.strip() == key]
    elif kind == "line":
        hits = [i for i, l in enumerate(lines) if l.startswith(key)]
    elif kind == "row":
        hits = []
        for i, l in enumerate(lines):
            if not l.strip().startswith("|"):
                continue
            cells = split_row(l)
            if cells and cells[0].replace("`", "") == key:
                hits.append(i)
    else:
        raise MutateFailed("未知定位类型：" + str(kind))
    if not hits:
        raise NotHere(str(key))
    if len(hits) > 1:
        raise MutateFailed("锚命中 %d 次（须恰 1 次）：%s" % (len(hits), key))
    return hits[0]


def apply_loc(text, loc, new):
    kind, key = loc
    lines = text.replace("\r\n", "\n").split("\n")
    i = _loc_index(lines, kind, key)
    if kind == "region":
        en = len(lines)
        for j in range(i + 1, len(lines)):
            if re.match(r"^##\s", lines[j]):
                en = j
                break
        out = "\n".join(lines[:i] + new.split("\n") + lines[en:])
    elif kind == "line":
        lines[i] = new
        out = "\n".join(lines)
    else:
        lines[i] = new
        out = "\n".join(lines)
    if out == text:
        raise MutateFailed("变异前后文本全等（未生效）：%s" % (key,))
    return out


def extract_loc(text, loc):
    kind, key = loc
    lines = text.replace("\r\n", "\n").split("\n")
    if kind == "region":
        return region(text, key)
    if kind == "line":
        return find_line(text, key)
    if kind == "row":
        i = _loc_index(lines, kind, key)
        return lines[i]
    raise Red("未知定位类型：" + kind)


# ---------------------------------------------------------------- 期望值（构建期注入）
VERSION_CONST = "1.2.0"
DESC_DIGEST = "36a2d59b242db102fe8f45a40c7f3c3cb4c8998298ddbbfd29a642096aac3a1f"
EXPECT_A_FIELDS = ['claim_id', 'claim', 'claim_type', 'source_layer', 'evidence_tag', 'authority', 'status', 'external_effect', 'requestee', 'accountable_party', 'decision_owner', 'responsibility_basis', 'generated_by', 'approver', 'expiry', 'linked_artifacts', 'assertion_form', 'comparability_ref', 'review_owner', 'reopen_trigger']
EXPECT_A_REQUIRED = ['必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '条件必填', '条件必填', '条件必填']
EXPECT_A_CLOSED = {'claim_type': {'measurement', 'commitment', 'authorization', 'fact', 'requirement', 'risk', 'assumption'}, 'source_layer': {'contractual', 'customer_request', 'legal_regulatory', 'approved_baseline', 'technical_design', 'internal_assumption'}, 'evidence_tag': {'JUDGMENT', 'FACT', 'INFERENCE', 'UNKNOWN', 'STALE'}, 'authority': {'consultative', 'unverified', 'binding', 'internal_only'}, 'status': {'draft', 'frozen_assumption', 'accepted', 'external_pending', 'external_confirmed', 'rejected', 'superseded'}, 'external_effect': {'outbound_authorized', 'internal_only', 'outbound_pending', 'none'}, 'assertion_form': {'datetime', 'quantity', 'qualitative', 'completeness', 'identifier'}}
EXPECT_A_FORMAT = {'claim_id': '`C-[0-9]{3,}`；同一主张跨件复用同一 ID', 'claim': '一句一主张，不得复合', 'requestee': '`<role-kind>:<ref>` 或 `none`；`role-kind` ∈ `human` / `seat` / `org`', 'accountable_party': '同上格式，交付与执行责任主体', 'decision_owner': '同上格式，决策与批准主体', 'responsibility_basis': '`source:<PREFIX>-<digits>` / `authorization:<PREFIX>-<digits>` / `none`，或 `<自由描述>`（**该行 `authority` 必须为 `unverified`**）', 'generated_by': '`<generator-kind>:<ref>`；`generator-kind` ∈ `human` / `seat` / `system`', 'approver': '`<approver-kind>:<ref>` 或 `none`；`approver-kind` ∈ `human` / `seat` / `system`', 'expiry': '`YYYY-MM-DD` 或 `none`；兼作批准有效期（同一主张的有效性与批准有效性同轴）', 'linked_artifacts': '`<kind>:<value>` 列表，以 `;` 分隔；`kind` ∈ `source` / `cite` / `artifact` / `authorization`', 'comparability_ref': '`CMP-[0-9]{3,}` 或 `none`；`assertion_form ≠ qualitative` 时禁 `none`', 'review_owner': '`<role-kind>:<ref>`；`status = frozen_assumption` 时禁 `none`', 'reopen_trigger': '一句可判的重开条件；`status = frozen_assumption` 时禁 `none`'}
EXPECT_D_FIELDS = ['claim_id', 'original_requirement_ref', 'required_environment', 'required_checks', 'required_change_record', 'actual_environment', 'actual_checks', 'qa_result', 'exemption', 'reason', 'scope', 'fallback_criterion', 'reopen_trigger']
EXPECT_D_OWNER = ['生产者', '需求侧', '需求侧；生产者照录，QA 不得回写', '同上；集合语义，非全序', '需求或生产者变更要求时', '只由 QA 填', '只由 QA 填', '只由 QA 填', '生产者申请、人类批准', '`exemption ≠ none` 时', '`exemption ≠ none` 时', '`exemption ≠ none` 时', '`exemption ≠ none` 时']
EXPECT_D_REQUIRED = ['必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '必填', '条件必填', '条件必填', '条件必填', '条件必填']
EXPECT_D_CLOSED = {'qa_result': {'passed_with_exemption', 'pending', 'failed', 'passed_at_actual', 'blocked'}, 'exemption': {'partial', 'full', 'none'}}
EXPECT_D_FORMAT = {'claim_id': '`C-[0-9]{3,}`；须在表 A 已登记', 'original_requirement_ref': '`REQ-[0-9]{3,}` 或 `none`；指向表 C 的 REQ 行', 'required_environment': '`mock` / `test` / `integration` / `production` / `none`', 'required_checks': '`functional` / `security` / `performance` / `compliance` / `robustness` 的子集，以 `;` 分隔，或 `none`', 'required_change_record': '`none`，或 `<原值>→<新值>@<approver>`；`<approver>` 须与**同 `claim_id` 表 A 行 `approver` 列**同值（跨表回指，**无论本行 `original_requirement_ref` 是否为 `none`**）；该列为 `none` 时，须先把变更行为的 `human:` 签署人补入表 A `approver` 列，再写本列（机检＝`30-gates` R4 第三支·本修法第 3 处同步扩该支）', 'actual_environment': '同四值，另允许 `unverified`', 'actual_checks': '同五值集合的子集，以 `;` 分隔，或 `none`', 'reason': '一句可判理由', 'scope': '受限面描述', 'fallback_criterion': '一句可判的回退判据', 'reopen_trigger': '一句可判的重开条件'}
EXPECT_B_COLS = ['cmp_id', 'cmp_key', 'cmp_kind', 'cmp_value', 'completeness_mode', 'enumeration_count', 'remaining_count', 'claim_id', 'source_artifact']
EXPECT_C_COLS = ['id_key', 'id_value', 'definition_ref', 'status', 'req_required_environment', 'req_required_checks', 'req_enumeration_base']
MATRIX = [['legal_regulatory', '条件', '允许', '禁止', '允许'], ['contractual', '条件', '允许', '禁止', '允许'], ['approved_baseline', '条件', '允许', '禁止', '允许'], ['customer_request', '条件', '允许', '允许', '允许'], ['technical_design', '禁止', '禁止', '允许', '允许'], ['internal_assumption', '禁止', '禁止', '允许', '允许']]
ROW_DIGESTS = {'c13': [('R1', '64490fbfca0fa7864f87388af0e94b1ee82827893b3b6686328b175e6b4ef4e3'), ('R2', '6d66ba6ac6d035131c2ddda020c41791ff7ef403575a64f52db93adf2a376077'), ('R3', '6b892cd6db889fef8f5800aa4a014627e438838ef9faa3c52a662c24eef3fcb2'), ('R4', 'c68c00180af27a7379ae92142a49218670da832f7bb521b2b9c47ac91de3d50f'), ('R5', 'ed241f719ffbfca6aae4c6c91cd215b9ebbbafe9b0a45c78e407f2478ea01cae'), ('R6', 'b7bb2b3817daabbf99c1c7708e51160216a570645de60920bd6d21fa9d98a2f2'), ('R7', 'd85821d31966cc6c1e242157459fd8ea4e2a735f121e900713b702a702d01243'), ('R8', '477be783d6484d8fc3768774a1e7ceab6211d8873ea572851a61394f5b33bffc'), ('R9', '47caeb096d62eb4614934496c263a69b474080786c93ec8f83460ffbc59999f5'), ('R10', 'd2c60a5fb3b934fa2619e4123b652848b27d7875f04ad61b6bf68db2c4dad43c'), ('R11', '3255672a27cb906aa6b20a5b8367ac9efb14031a1512c0fb8101eb43941042d8'), ('R12', 'a3fd99b8e11fcae2605202009755adfb4aac62ddff3d32e34c4e37e7de185486'), ('R13', 'a51a75c436908f23dac1f91abc82e59a1c9b77944f4e7d3a44fe52fc15caf8e6'), ('R14', 'd5bd7ea4e796dc2bc87b46fd12e41dbada7084e40daad25e3c745ddfd7476078'), ('R15', '72f0a2711dc4eed299f6d5777f7f1e816e2fc7878c67249a975c6aa8a54041a7'), ('R16', '80f24066f768fb5ae94f7e23c962f5e599717217712f00a6fce70a6b9cd2d0bf'), ('R17', '3d94cca3af47d7e3c5f4fbf120db532b2aeddfdff595ca8f10db1bcb300bac59')], 'c14': [('N1', '8cb01b1fb6e6495cfe3b669f89def347634a57122e8f2b25502c81a2c7bfcd05'), ('N2', 'f0318eb89197b3b67bc016511ae5278d8936edb63dbd858ff4f15759bb276e60'), ('N3', '6647e05b61ebb66db0ea142ebc15a9d28aa5af848339813cf0874bed37196a1d'), ('N4', '019f50c2ca23a03da9a12f8d7af607c6e843eb47139f6923c5a08a7aef855a46'), ('N5', 'b46efe402cfd7ac47e221843012dec65e31c114c25fa48f7ced0c2aca7119687'), ('N6', 'c27ef1a1cc5c59a1b82e0be3f1e06fa513fc58aed4a8cfab84e527cd1f45012f'), ('N7', '7f565336cc42e6ffe2531db1de061fdd1f4a6cbe140aa44eb25ddaa9ae54c18e'), ('N8', 'cc68aeef37f04ecb6ed8622da2c466df1997241480ef31574c84603350aed36c'), ('N9', '2a0a642907abef357bc173c55b48f08f6e4e4a6d900595d688351c9e5fbf1b32'), ('N10', 'a2e992c46d224e6e5402aa21154e4df5d5a87e309f7ec097bb65842b11c331cc')]}
PATTERNS_PAIRS = [('数量（阿拉伯）', '(剩余|还剩|还缺|缺口|共|合计|总计|已|待|完成|核销)\\s*[0-9]+(\\.[0-9]+)?\\s*(人日|人|天|小时|分钟|次|个|条|项|处|万元|元|%)'), ('数量（中文）', '(剩余|还剩|还缺|缺口|共|合计|总计|已|待|完成|核销)\\s*[一二三四五六七八九十百千万两]+\\s*(人日|人|天|小时|分钟|次|个|条|项|处|万元|元|成|倍)'), ('时点', '(于|截至|截止|止于|完成于|清零于|定于|在)\\s*(20[0-9]{2}-[0-9]{2}-[0-9]{2}|[0-9]{1,2}月[0-9]{1,2}日)'), ('完备性', '(清零|一条不剩|无遗漏|核销完毕|关闭完毕|验收完毕)\\s*(于|之日|为止|完成)')]
STRONG_SET = {'均已', '一律', '确保', '必须', '全覆盖', '绝不', '全部', '保证'}
PLACEHOLDER_SET = {'暂定', 'placeholder', '待补', '待定', '待确认', 'TBD', '〔', 'TODO'}
EXPECT_OUT_FIELDS = ['outbound_type', 'claims', 'fact_review', 'commitment_review', 'authorization', 'send_channel']
EXPECT_OUT_CLOSED = {'outbound_type': {'report', 'clarification_request', 'risk_notice', 'commitment', 'acceptance'}, 'send_channel': {'draft_only', 'approved_send'}}
EXPECT_DEPS = ['bundle:semantic-governance', 'bundle:external-advisor-collab', 'bundle:deep-research', 'bundle:object-audit', 'bundle:sop']
DEP_COMPONENTS = {'sop', 'deep-research', 'object-audit', 'semantic-governance', 'external-advisor-collab'}
EXPECT_SUBCMDS = ['validate --artifact <file> --kind <artifact-kind>', 'reconcile --artifacts <file-list>', 'gate-outbound --artifact <file>']
EXPECT_AGG = ['total_claims', 'real_env_passed', 'mock_only', 'unverified', 'failed', 'excluded_by_approval', 'pending', 'not_required']
EXPECT_ARTIFACTS = ['PRD', '需求解析', '工作票', '回执／回流件', 'QA 判词', '交付汇总', '对外呈报／函件']
SEC1_MAP_DIGESTS = [('PRD', '4ed286994c5185e2de7ad8fb804b47fecb29e5c059602f20641c1576e773feea'), ('需求解析', '3b1f2030ef5fdf8feb394089a98390b3f98963570a0511ca210ed030e848504b'), ('工作票', 'e4617f038555136541bfced9c11793fad27e4aecb336f51e51924ab5d5d16724'), ('回执／回流件', 'f88593fdce07bf1ae02f17a29f34cb4c1977fc9dd153f0614999558f8bd8a9b2'), ('QA 判词', '441a6929c53fbe60c8001b18e122018f6853c3cd9fb04d86ada9734c8c75d944'), ('交付汇总', 'f79f99f584f4647f947e30fb6887b03189d7661681102c78d4c5cb05bd019c97'), ('对外呈报／函件', 'e26142a54ef707b1ebcde9fb93a79193355ec37f3c0f0a6ceed971a4d10f6bcb')]
PASSAGE_NAMES = {'claude.dev lessons-from-building', 'agentskills.io specification', 'obra/superpowers writing-skills'}
PARADIGM_NAMES = {'SSOT', 'URN 式命名'}
CARRIERS = {'object-build 第 3 步', 'object-audit S5', 'object-build 第 4 步', 'external-advisor-collab 谁主张谁举证', '1859aca', '本票', 'deep-research §六 证据纪律', '9b42454', 'object-audit S3'}
# ---- v5 新增常量（治红4-01／红4-03／红4-05／黄4-02／黄4-10）----
# §11 编号与角色发放主体（整节摘要）
SEC11_DIGEST = "b35ca98ec08ba9c6b166a8889081f88ae526a412864ab5f32e82ad0ded992fe3"
# 30-gates §4 元规则段摘要（治红4-02：保住 229 条的机制自己也要被保住）
GATES4_META_DIGEST = "c811aa7bd578430f7ca3a13f4238d679e4cd9f6fd4ab7defafb749a629f90cab"
# SKILL.md 三节整节摘要（治红4-05：正文零判据绑定）
SKILL3_DIGESTS = [("## 触发与不触发", "b8a38bf77e3372f9edd83874e392d8a56c120b4c6a06a57a6e024998f9afc226"),
                  ("## 契约总则", "38f30d49f7413185fa145eb5dd845c9fc912a5a9f0952943074a8a7c6dd96327"),
                  ("## 按需加载", "b83fb0adc3886e42eee11b4d3138f9b495dc990e620697b636c1748a71ff9406")]
# 总则→真源双向绑定（治「复述可漂移而永远绿」：每条总则须含 key，且真源文件须含 src）
TAOZE_BIND = [
    (1, "一句一主张，一行一 `claim`", "references/10-contract.md", "一句一主张，不得复合"),
    (2, "17 项必填字段", "references/10-contract.md", "必填 17 ＋ 条件必填 3"),
    (3, "`artifact:` 只能附加", "references/30-gates.md", "只能附加"),
    (4, "内部接受不等于外部确认", "references/10-contract.md", "内部接受不得写成外部确认"),
    (5, "内部冻结只限内部", "references/10-contract.md", "不得外溢为默认认可"),
    (6, "回退判据", "references/10-contract.md", "fallback_criterion"),
    (7, "审查人不得为生成方", "references/10-contract.md", "`reviewer` 不得等于 `generated_by`"),
    (8, "同键不同值即判违例", "references/30-gates.md", "同键同值"),
    (9, "不判业务真伪", "references/10-contract.md", "不得自动判定业务事实真伪"),
    (10, "状态只增不改，历史不回写", "references/10-contract.md", "不删除、不改写"),
]
# §11 引用型字段五闭集与编号前缀闭集（治红4-01：禁造号）
EXPECT_REF_FIELDS = ["source:", "authorization:", "linked_artifacts", "comparability_ref", "original_requirement_ref"]
ID_PREFIXES = {"INTK", "RES", "MSR", "DOC", "TKT", "RCP", "PRD", "QAV", "DLV", "OUT", "REQ", "CMP", "AUTH", "DEC", "C"}
# 「自由描述」的正向识别：值内含中文／全角括号／空白 ⇒ 不是编号也不是角色册位号。
# 判据问的是「该行 authority 是否已降为 unverified」，不是「字符串像不像编号」。
FREE_DESC_RE = re.compile(r"[\u4e00-\u9fff（）()\s]")
FREE_DESC_FIELDS = ("responsibility_basis", "linked_artifacts", "requestee", "accountable_party",
                    "decision_owner", "approver", "review_owner")
# 跨包条款名对照表摘要与取证口径闭集（治红4-03：条款名虚指是盲区）
CROSS_NAME_DIGEST = "89341ca953bc14b7c2afe3c265879742523e19f34a0f84b89df3a2ae8996a0cf"
EVIDENCE_TIERS = {"仓内可核", "部署件已核（0.1.30，`version: 1.0.2`）", "T2 交付物未出", "无跨包条款"}
# 他包包内文件名式引用黑名单：条款名不得写成「某包 notes-format 条款」这类不可取证形式
FOREIGN_FILE_TOKENS = ("notes-format", "30-discipline", "20-discipline", "10-roles")


def gates4_meta(text):
    """取 §4 表前元规则段：从「每条负样本必须让」到人工闸承接项标题前。"""
    lines = text.replace("\r\n", "\n").split("\n")
    i1 = None
    for i, l in enumerate(lines):
        if l.startswith("每条负样本必须让"):
            i1 = i
            break
    if i1 is None:
        raise Red("§4 元规则段起标记未命中（『每条负样本必须让…』被删或改义）")
    for j in range(i1 + 1, len(lines)):
        if lines[j].startswith("**人工闸承接项"):
            return "\n".join(lines[i1:j]).strip()
    raise Red("§4 元规则段止标记未命中")

FILES_BASENAMES = {'40-provenance-map.md', 'claim-register.md', '10-contract.md', 'SKILL.md', '30-gates.md', '20-artifact-mapping.md', 'outbound-artifact.md'}
PLAIN_SAMPLES = ['合入前一律跑全量单测。', '所有新增代码必须过 code review，不得跳过。', '本票只改一个文件，其余不动。', '全部用例均已通过，含 3 处跳过说明。']
TRUE_SAMPLES = ['剩余 3 项未验。', '已于 2026-05-01 清零。', '共 12 条待核销。', '无遗漏于交付前完成。']
S7_TEXT = '## 7. 状态语义硬规则 1. `accepted` 不等于 `external_confirmed`；内部接受不得写成外部确认。 2. `frozen_assumption` 只限内部：`expiry`、`review_owner`、`reopen_trigger` 三者均不得为 `none`，`expiry=none` 直接判违例；不得外溢为默认认可。 3. `external_pending` 超时只触发复核与升级，不自动变为 `external_confirmed`。 4. `external_effect=outbound_authorized` 只能由人类闸设置。 5. `superseded` 保留旧行，不删除、不改写；被 `superseded` 的主张不得再被任何工件引用。 6. QA 按 `actual_environment` / `actual_checks` 判定通过，不回写 `required_environment` / `required_checks`。 7. `evidence_tag` 为 `UNKNOWN` 或 `STALE` 时，`status` 不得为 `accepted`，`authority` 不得为 `binding`，`external_effect` 不得为 `outbound_authorized`。'
S8_TEXT = '## 8. 人工闸七类（唯一真源） 以下七类事项必须人类拍板，机器与席位均不得代判： 1. 外部权威来源的确认。 2. 外发授权。 3. 需求降级或豁免的批准。 4. 范围或验收口径的变更。 5. 法律、合同或责任解释。 6. 外发动作本身。 7. 是否将沉默视为认可；默认一律不算。'
S9_TEXT = '## 9. 禁止工具自决八条 1. 不得从文本自行推断权威性。 2. 不得把 `UNKNOWN` 或 `INFERENCE` 自动升格为 `FACT`。 3. 不得把内部冻结自动转为外部确认。 4. 不得自动降级要求环境或要求检查。 5. 不得自动发送任何外发件。 6. 不得自动生成对外承诺。 7. 不得自动判定业务事实真伪。 8. 不得自动改写历史主张状态。'
SEC2_DIGEST = "69d36db735c5d04cc009731950cd98b10fd30f84d01d8376124eded8c4db777d"
SEC10_DIGEST = "9c93a1b67c4671a595c999bacd8039b2afa95e00dec3dfd9e16efe77e83b406d"
SEC3_MAP_DIGEST = "64e47626afdc880c1fd1d740d2ff2cfda8ebf9b3771b1b3e03cab08509f1bcdc"
SEC2_MAP_DIGEST = "df9cf469b232c89598a88fc934980a16dbbfc0cd3a0c447762cca00b094d38f9"
GATES_S1_DIGEST = "1eb22e9ee48ff1164e14c52beb507324113757cea414472cf41b787ee306530e"
ENV_AXIS_DIGEST = "71419bb50f2021594f04bef3c44e3e6445a58ad026075016b2e13e1134048aea"
RESP_BOUND_DIGEST = "06aa99d3d61d9d0e91d2d0a72016e34a27deae12021a04307b223c0688e93214"
SOURCE_BOUND_DIGEST = "12e49591f0067e9b24c26b6bc8c2b0693ecd07c9477e58d66677cddb61969509"
ABOLISH_DIGEST = "41c21270c421426a6a346f2dddd013f4623c02a83042fefb57f76c0ef1fa9cac"
UNIQ_SENT_DIGEST = "38aad95059f1fb21b59128da5785941cd013da88fe062d4456581584de25047a"
CSTATUS_DIGEST = "bbefde1da6b1e930278265c3bf9701e90990b03341fcde2012477be7fba4a5f0"
IDKEY_DIGEST = "58488e18658f2601dba87b8f932da00e0a6ee897210301767f52588f0b48576b"
S5SPLIT_DIGEST = "dd2ed2f1ebb37ef0e262b8e8417241e35d8faae56377985461b04d76e0c92a4e"
ACCEPT_DIGEST = "f6868d332086663266a16c695752c2ad84503f9d4ce869dae694fcae11bbfcf8"
BOUND_DIGEST = "98963379b1f72098275a1231641c4ba843603db1d072bbda5cd4c862811e9ea5"
DEPWHY_DIGEST = "b84c3cd3fe54236cde7b35cd9b058ef74872d9e9ae8645df8d6cb47438805f67"
OUTB_DIGESTS = [(('line', '- `outbound_type`：'), '51091c33251bb9a3dce43541a4d48223d37b67b92203a7fd580f03609793a40c'), (('line', '- `claims`：'), 'c5c028eeea821a9079abfb377983cbf4a032500bc84944f13c6fd40eb6e9a43d'), (('line', '- `fact_review`：'), '741a33489a62888bb6043f64008644a1a81a531016d6cb8948162cfaae5f1e69'), (('line', '- `commitment_review`：'), '66bdd7b1d3eb28247c199b53ef174aaa1e7f457f702fc84d8043000f98e81e73'), (('line', '- `authorization`：'), '90176bc75b92dc74377f6f303c9e51b0d01502bfcdf85f1ad5eaef3cf97a605d'), (('line', '- `send_channel`：'), 'ea4a5facc143cd3eae38e41d110aab3123c9c6e45bc0f39ca5d0b96bb2b00f7e'), (('line', '正文每条承重主张必须能回指'), '01da7e22f7012f4de013435d6e53d34833d1e92e8f7735300e512f9ae81a5f60'), (('line', '- 授权范围：'), '5c1a8e79f3e7b934930ee46be09ad600d2be45e6d0ccced6d29592448a953131')]
OUT_ROW_DIGESTS = [('outbound_type', '072feff25f1b4e558d3a5bd47c949bd63368d6a96d08dfdfc32ba58e2ba5bf15'), ('claims', 'f03fb114fc079759c9a729303df06739b30e46982affb2d3785fc198ff22ae4e'), ('fact_review', '80ed410106ee17dc490507c402a5c80b2802f68b1c540cd2ef14f4a4810a6f40'), ('commitment_review', 'c796ecda76d98b234ebf831689639032c01ab73cfd1bcdd927d0fc1cdde64515'), ('authorization', '64fc90438fab736129ac808ab11b1ef9158d3b209711213ceba34f04049023b2'), ('send_channel', '43b1a516def1b8bdbd4d9a4dd963a1bb7e096db12bed76bf22874b061fbe24bd')]
EXPECT_TARGETS = [{'id': 'T-DESC', 'check': 'c04', 'key': 'skill', 'file': 'SKILL.md', 'loc': ('line', 'description:')}, {'id': 'T-S7', 'check': 'c10', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('region', '## 7. 状态语义硬规则')}, {'id': 'T-S8', 'check': 'c11', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('region', '## 8. 人工闸七类（唯一真源）')}, {'id': 'T-S9', 'check': 'c12', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('region', '## 9. 禁止工具自决八条')}, {'id': 'T-SEC2', 'check': 'c08', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('region', '## 2. 来源层判定序与相容矩阵')}, {'id': 'T-SEC10', 'check': 'c17', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('region', '## 10. deep-research 证据标签消费映射')}, {'id': 'T-SEC3MAP', 'check': 'c22', 'key': 'mapping', 'file': 'references/20-artifact-mapping.md', 'loc': ('region', '## 3. 交付汇总聚合字段（七桶＋分母，互斥且完备）')}, {'id': 'T-SEC2MAP', 'check': 'c22', 'key': 'mapping', 'file': 'references/20-artifact-mapping.md', 'loc': ('region', '## 2. 登记闭包')}, {'id': 'T-S1GATES', 'check': 'c11', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('region', '## 1. 人工闸消费点（不复制条文）')}, {'id': 'T-ENVAXIS', 'check': 'c07', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '**环境轴序位（全序，唯一参与大小比较的轴）**：')}, {'id': 'T-UNIQ', 'check': 'c09', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '- 表 B 是**可比对断言行**的唯一登记处。')}, {'id': 'T-BOUND', 'check': 'c23', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('line', '**能力边界声明**：')}, {'id': 'T-DEPWHY', 'check': 'c19', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('line', '**为何不钉版本（本版改判，替代上一版把语义化版本钉在组件名后的写法）**：')}, {'id': 'T-A1', 'check': 'c23', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'A1')}, {'id': 'T-A2', 'check': 'c23', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'A2')},  # T-A3 不入靶点面＝无可反转词（见主理人在途裁定二 6b0fc5d）
 {'id': 'T-A4', 'check': 'c23', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'A4')}, {'id': 'T-PAT1', 'check': 'c20', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| 数量（阿拉伯） |')}, {'id': 'T-PAT2', 'check': 'c20', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| 数量（中文） |')}, {'id': 'T-PAT3', 'check': 'c20', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| 时点 |')}, {'id': 'T-PAT4', 'check': 'c20', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| 完备性 |')}, {'id': 'T-R3', 'check': 'c13', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'R3')}, {'id': 'T-R4', 'check': 'c13', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'R4')}, {'id': 'T-R5', 'check': 'c13', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'R5')}, {'id': 'T-R8', 'check': 'c13', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'R8')}, {'id': 'T-R9', 'check': 'c13', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'R9')}, {'id': 'T-R10', 'check': 'c13', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'R10')}, {'id': 'T-R12', 'check': 'c13', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'R12')}, {'id': 'T-R13', 'check': 'c13', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'R13')}, {'id': 'T-R14', 'check': 'c13', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'R14')}, {'id': 'T-R17', 'check': 'c13', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'R17')}, {'id': 'T-N1', 'check': 'c14', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'N1')}, {'id': 'T-N4', 'check': 'c14', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'N4')}, {'id': 'T-N8', 'check': 'c14', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'N8')}, {'id': 'T-N10', 'check': 'c14', 'key': 'gates', 'file': 'references/30-gates.md', 'loc': ('row', 'N10')}, {'id': 'T-STRONG', 'check': 'c17', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| 强断言 |')}, {'id': 'T-PLACE', 'check': 'c17', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| 占位词 |')}, {'id': 'T-BND-责任主体', 'check': 'c05', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '**责任主体边界**：')}, {'id': 'T-BND-来源载体', 'check': 'c05', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '**来源载体边界**：')}, {'id': 'T-BND-字段裁撤', 'check': 'c05', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '**字段裁撤记录**：')}, {'id': 'T-source_layer', 'check': 'c05', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| 来源 | `source_layer` |')}, {'id': 'T-authority', 'check': 'c05', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| 来源 | `authority` |')}, {'id': 'T-status', 'check': 'c05', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| 状态与效力 | `status` |')}, {'id': 'T-approver', 'check': 'c05', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| 生成与批准 | `approver` |')}, {'id': 'T-D-required_environment', 'check': 'c07', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| `required_environment` |')}, {'id': 'T-D-qa_result', 'check': 'c07', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| `qa_result` |')}, {'id': 'T-D-fallback_criterion', 'check': 'c07', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '| `fallback_criterion` |')}, {'id': 'T-OUTB-01', 'check': 'c15', 'key': 'outb', 'file': 'templates/outbound-artifact.md', 'loc': ('line', '- `outbound_type`：')}, {'id': 'T-OUTB-02', 'check': 'c15', 'key': 'outb', 'file': 'templates/outbound-artifact.md', 'loc': ('line', '- `claims`：')}, {'id': 'T-OUTB-03', 'check': 'c15', 'key': 'outb', 'file': 'templates/outbound-artifact.md', 'loc': ('line', '- `fact_review`：')}, {'id': 'T-OUTB-04', 'check': 'c15', 'key': 'outb', 'file': 'templates/outbound-artifact.md', 'loc': ('line', '- `commitment_review`：')}, {'id': 'T-OUTB-05', 'check': 'c15', 'key': 'outb', 'file': 'templates/outbound-artifact.md', 'loc': ('line', '- `authorization`：')}, {'id': 'T-OUTB-06', 'check': 'c15', 'key': 'outb', 'file': 'templates/outbound-artifact.md', 'loc': ('line', '- `send_channel`：')}, {'id': 'T-OUTB-07', 'check': 'c15', 'key': 'outb', 'file': 'templates/outbound-artifact.md', 'loc': ('line', '正文每条承重主张必须能回指')}, {'id': 'T-OUTB-08', 'check': 'c15', 'key': 'outb', 'file': 'templates/outbound-artifact.md', 'loc': ('line', '- 授权范围：')}, {'id': 'T-AGGCONS', 'check': 'c22', 'key': 'mapping', 'file': 'references/20-artifact-mapping.md', 'loc': ('line', '**守恒式（闭合，无游离项）**：')}, {'id': 'T-S5SPLIT', 'check': 'c17', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '**两表分工（治重叠）**：')}, {'id': 'T-CSTATUS', 'check': 'c09', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '- `status` ∈ `defined` / `draft` / `retired`')}, {'id': 'T-IDKEY', 'check': 'c09', 'key': 'contract', 'file': 'references/10-contract.md', 'loc': ('line', '- `id_value` 是编号本体，')}, {'id': 'T-MAPQAROW', 'check': 'c22', 'key': 'mapping', 'file': 'references/20-artifact-mapping.md', 'loc': ('row', 'QA 判词')}, {'id': 'T-DEADSTEP', 'check': 'c22', 'key': 'mapping', 'file': 'references/20-artifact-mapping.md', 'loc': ('line', '4. `required_environment = none` → 计入 `not_required`')}]


# ---------------------------------------------------------------- 静态判据表（人工声明，非构建期派生）
# 人工闸七类的原文短语黑名单（c11 第 1 层：短语命中即第二真源）
BANNED_PHRASES = ("不得代判", "一律不算", "把当事人的沉默", "默认视为认可", "默认一律", "沉默视为认可")
# 人工闸七类的义素探针（c11 第 3 层：同义改写检测；已在行内含 10-contract／§7／§8／§9 指针的行豁免）
HUMAN_GATE_PROBES = ("外部权威", "外发授权", "降级或豁免", "验收口径", "责任解释", "外发动作")
# 抽取模式探针（--selfcheck 用：每个模式在其声明正样本上的命中数）
PATTERN_PROBES = [(0, "剩余 3 项未验。", 1), (1, "共十二条待核销。", 1),
                  (2, "已于 2026-05-01 清零。", 1), (3, "无遗漏于交付前完成。", 1)]
# 三闸反向验证支数（票面 §3.12 实跑核对；此处只作计数来源）
GATE_REVERSE = ("甲 删 spec-provenance 块", "乙 篡改 spec_clause_sha256",
                "丙 删 description 的『适用场景：』", "丁 追加裸日期行")
# 裁定四：逐字段消费方（值与票面 §0.4 逐行一致；--stats 由此统计，不手写）
FIELD_CONSUMERS = {
    "claim_id": "R3／R15／R17", "claim": "R14", "claim_type": "R1", "source_layer": "R1／R7",
    "evidence_tag": "R1／R8", "authority": "R1／R7／R8／R13③", "status": "R1／R3／R5③／R8①／R10",
    "external_effect": "R1／R6／R8", "requestee": "R13②", "accountable_party": "R13①②",
    "decision_owner": "R13③", "responsibility_basis": "R13①", "generated_by": "R5④／R6",
    "approver": "R5①④／R6／R7条件格／R13③", "expiry": "R5①③／R7条件格",
    "linked_artifacts": "R2 三支／R8③", "assertion_form": "R1／R14／R16",
    "comparability_ref": "R14②③", "review_owner": "R5③", "reopen_trigger": "R5③／R5⑤",
    "original_requirement_ref": "R4③④／R12②／R16②",
    "required_environment": "R1／R4①③④", "required_checks": "R1／R4①③④",
    "required_change_record": "R4③", "actual_environment": "R1／R2③／R4①②／聚合",
    "actual_checks": "R1／R4①", "qa_result": "R1／R4②／聚合", "exemption": "R1／R4①／R5①②／聚合",
    "reason": "R5①", "scope": "R5①", "fallback_criterion": "R5②",
    "cmp_id": "R17／R14③", "cmp_key": "R11", "cmp_kind": "R1／R11／R12③", "cmp_value": "R11／R16①",
    "completeness_mode": "R12①", "enumeration_count": "R12①②", "remaining_count": "R12①",
    "source_artifact": "R11 附加支", "id_key": "R16③④", "id_value": "R16②④",
    "definition_ref": "R16①", "req_required_environment": "R4③",
    "req_required_checks": "R4③", "req_enumeration_base": "R12②",
}
# 已删字段（v2→v3 删 2 列；票面 §0.4 与本表须一致）
DELETED_FIELDS = {"表 A": ["source_kind", "approval_scope"]}


# ---------------------------------------------------------------- 判据形态归类（裁定六：逐条给依据）
FORM_REASONS = {
    "c01": ("set_equal", "七件路径序列与两目录文件序列逐项全等（列表 ==），另含目录名＝name 常量等于"),
    "c02": ("structural", "只判 SKILL.md 行数上界与目录项，不比对任何规范正文；行数上限是体量断言本身，非语义判据"),
    "c03": ("exact", "frontmatter 三值逐字等于常量（version 由 v3 的『只验语义化形态』改为常量等于）"),
    "c04": ("digest", "description 规范化整串 sha256 全等（另含 when 标记在位、负路由计数、1536 上界）"),
    "c05": ("exact", "表 A 13 个非闭集字段的格式列规范化后逐字全等；另含字段/必填性序列强等与 3 句边界摘要"),
    "c06": ("set_equal", "四张表头列名序列逐列全等（R17 机检，仅此两项：列序＋表 A 表头唯一）"),
    "c07": ("exact", "表 D 11 个非闭集字段的格式列规范化后逐字全等；另含三序列强等与轴句摘要"),
    "c08": ("digest", "§2 整节规范化摘要全等；另含矩阵 6×4 共 24 格逐格全等"),
    "c09": ("set_equal", "表 B／表 C 两条列清单逐项全等为主；另含表 C 两句约束与『唯一』释义句摘要"),
    "c10": ("exact", "§7 整节规范化后逐字全等"),
    "c11": ("exact", "§8 整节规范化后逐字全等；另含跨文件第二真源三层检测（原文短语／逐行全等复制／义素探针）"),
    "c12": ("exact", "§9 整节规范化后逐字全等"),
    "c13": ("digest", "R1–R17 编号序列强等之外，17 行逐行摘要全等"),
    "c14": ("digest", "N1–N10 编号序列强等之外，10 行逐行摘要全等；**另含 §4 表前元规则段整段摘要**（v5 新增，治红4-02）"),
    "c15": ("digest", "外发门 6 行逐行摘要＋外发模板 8 处落点摘要全等"),
    "c16": ("structural", "四表示例行逐列做闭集成员／格式形态校验与填写说明条目计数，不比对规范正文"),
    "c17": ("set_equal", "强断言 8 词与占位 8 词两个集合全等为主"),
    "c18": ("exact", "三档出处语法逐字全等（通行做法名／范式名／授权载体名整名比对，不取首词）；另含节存在与节内关键词校验"),
    "c19": ("set_equal", "依赖组件序列全等＋组件闭集强等为主"),
    "c20": ("exact", "4 类抽取模式正则片段逐字全等为主；另含 4 例普通票零误触发与 4 例真断言全命中的双向功能测"),
    "c21": ("set_equal", "三子命令序列全等＋引用判据号落在 R1–R17 闭集内"),
    "c22": ("digest", "20-mapping §1 逐行摘要＋§2 整节摘要＋§3 整节摘要全等；另含七桶 125 组合穷举"),
    "c23": ("digest", "承接项 A1–A4 内容摘要＋能力边界句摘要全等"),
    "c24": ("selftest", "不判被测件内容主张，只判夹具自身不变量（靶点 REV 后等长且必变）"),
    "c25": ("structural", "术语别名行数与非空性、指针落点存在性；不比对规范正文"),
    "c26": ("exact", "§11 整节规范化摘要全等＋引用型字段五名闭集逐字等；另含三条禁令字面在位与表 A 编号前缀闭集判定（v5 新增，治红4-01）"),
    "c27": ("exact", "SKILL.md 三节整节摘要全等；另含 10 条总则→真源关键子串双向绑定（v5 新增，治红4-05）"),
    "c28": ("set_equal", "跨包条款名对照表 5 行与依赖面组件序列全等、条款名闭集判定；另含取证口径闭集与他包文件名式引用零命中（v5 新增，治红4-03）"),
}
# 六标签的**定义表**（治黄4-10：分布须可被第三方独立复算）。每标签给「定义」与「允许的主判据操作」；
# 辅判据另由 FORM_AUX 逐条登记，主/辅分离后标签不再含糊。
FORM_DEF = {
    "exact": ("整串／整节全等：比较对象是内联常量、闭集成员或整节文本，期望值可从码面直接读出（可用规范化 sha256 实现整串比较）。",
              {"整串全等", "整名成员", "摘要等值"}),
    "digest": ("逐条摘要等值：期望值以 sha256 常量呈现，按行或按落点逐条比对（读者须 diff 才能定位差异）。",
               {"摘要等值"}),
    "set_equal": ("集合或序列逐项全等：顺序参与判定（序列用 == 逐项比，集合用集合等）；不比对内容摘要。",
                  {"序列逐项等", "集合等"}),
    "structural": ("形态与体量断言：只判行数上界、目录层深、闭集成员与格式形态，不比对任何规范正文。",
                   {"形态断言", "序列逐项等"}),
    "selftest": ("夹具自证：不判被测件的内容主张，只判夹具自身不变量。",
                 {"自证断言"}),
    "id_seq": ("只比对编号序列、无其它断言。",
               {"序列逐项等"}),
}
# 每条检查的**主**判据操作（单一值；与 FORM_DEF 允许集比对，并回源码做特征交叉核）
FORM_OPS = {
    "c01": "序列逐项等", "c02": "形态断言", "c03": "整串全等", "c04": "摘要等值",
    "c05": "整串全等", "c06": "序列逐项等", "c07": "整串全等", "c08": "摘要等值",
    "c09": "序列逐项等", "c10": "整串全等", "c11": "整串全等", "c12": "整串全等",
    "c13": "摘要等值", "c14": "摘要等值", "c15": "摘要等值", "c16": "形态断言",
    "c17": "集合等", "c18": "整名成员", "c19": "序列逐项等", "c20": "整串全等",
    "c21": "序列逐项等", "c22": "摘要等值", "c23": "摘要等值", "c24": "自证断言",
    "c25": "形态断言", "c26": "摘要等值", "c27": "摘要等值", "c28": "序列逐项等",
}
# 辅判据逐条登记（治黄4-10 的第二半：主判据之外还做了什么，必须写出来，不许混进标签里）
FORM_AUX = {
    "c04": "辅：when 标记在位、负路由条数 ≥3、字符数上界（形态断言）",
    "c06": "辅：表 A 表头在本包内出现次数 == 1",
    "c14": "辅：应咬列必须可指认到具体判据支（形态断言）",
    "c17": "辅：强断言词不得与抽取模式正则共享触发词（子串包含，逐词）",
    "c18": "辅：节存在性与节内关键词**子串包含**（非整名），故主判据只声明到『整名成员』为止",
    "c19": "辅：bundle: 记号形态与跨包路径片段零命中（形态断言）",
    "c20": "辅：4 例普通票零误触发／4 例真断言全命中（双向功能测）",
    "c22": "辅：七桶 125 组合穷举（自证断言）",
    "c24": "辅：无（纯自证）",
    "c25": "辅：主类型段指针所指条目名含『混装』（子串包含）",
    "c26": "辅：三条禁令字面在位、表 A 编号前缀闭集（形态断言）",
    "c27": "辅：10 条总则→真源关键子串**双向绑定**（子串包含，两侧各查一次）",
    "c28": "辅：取证口径 ∈ 四值闭集、他包文件名式引用零命中（形态断言）",
}
# 零值桶的登记理由（治黄4-11：空桶不许裸着；删桶会把问题挪到闭集外）
EMPTY_TAG_REASON = {
    "id_seq": "本版 0 条检查只用编号序列而无其它断言：v3 的两处（R16→c09、R17→c06）在 v4 起已分别并入集合/序列全等与逐行摘要。保留该标签是为让『只用编号序列』这一形态在闭集内可指认；删桶只是把问题挪到闭集外。",
}
FORM_TAGS = ("exact", "digest", "set_equal", "structural", "selftest", "id_seq")


# ---------------------------------------------------------------- 结构面变异（文件级）
def pkg_read(pkg, rel):
    with open(os.path.join(pkg, rel), encoding="utf-8") as f:
        return f.read()


def pkg_write(pkg, rel, text):
    with open(os.path.join(pkg, rel), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def pkg_swap_words(pkg, rel, a, b):
    """互换两处字面（裁定七：两锚命中数各须恰为 1）。"""
    t = pkg_read(pkg, rel)
    if t.count(a) != 1:
        raise MutateFailed("互换锚 %r 命中 %d 次（须恰 1 次）" % (a, t.count(a)))
    if t.count(b) != 1:
        raise MutateFailed("互换锚 %r 命中 %d 次（须恰 1 次）" % (b, t.count(b)))
    t = t.replace(a, "\x00").replace(b, a).replace("\x00", b)
    pkg_write(pkg, rel, t)


def pkg_replace(pkg, rel, old, new):
    """按字面替换单处（裁定七：命中数必须恰为 1）。"""
    t = pkg_read(pkg, rel)
    if t.count(old) != 1:
        raise MutateFailed("替换锚 %r 命中 %d 次（须恰 1 次）" % (old[:48], t.count(old)))
    out = t.replace(old, new, 1)
    if out == t:
        raise MutateFailed("变异前后文本全等（未生效）：%r" % (old[:48],))
    pkg_write(pkg, rel, out)


def pkg_swap_fm(pkg, rel):
    t = pkg_read(pkg, rel)
    n = re.search(r"^name:\s*(\S+)\s*$", t, re.M)
    v = re.search(r"^version:\s*(\S+)\s*$", t, re.M)
    if not n or not v:
        raise MutateFailed("frontmatter 锚不存在（name=%s version=%s）" % (bool(n), bool(v)))
    if t.count(n.group(0)) != 1 or t.count(v.group(0)) != 1:
        raise MutateFailed("frontmatter 锚不唯一")
    t = t.replace(n.group(0), "name: " + v.group(1)).replace(v.group(0), "version: " + n.group(1))
    pkg_write(pkg, rel, t)


def pkg_swap_header(pkg, rel, ncols, ca, cb):
    t = pkg_read(pkg, rel)
    lines = t.split("\n")
    hit = None
    for i, l in enumerate(lines):
        if not l.strip().startswith("|"):
            continue
        cells = [c.replace("`", "") for c in split_row(l)]
        if len(cells) == ncols and ca in cells and cb in cells:
            if hit is not None:
                raise MutateFailed("表头锚命中多于 1 行（%d 列）" % ncols)
            hit = i
    if hit is None:
        raise MutateFailed("表头锚不存在（%d 列 %s/%s）" % (ncols, ca, cb))
    cells = [c.replace("`", "") for c in split_row(lines[hit])]
    a, b = cells.index(ca), cells.index(cb)
    cells[a], cells[b] = cells[b], cells[a]
    lines[hit] = "| " + " | ".join(cells) + " |"
    pkg_write(pkg, rel, "\n".join(lines))


def pkg_drop_section(pkg, rel, heading):
    """删掉从 heading 到下一个 ## 标题之前的整节（结构面变异用）。"""
    lines = pkg_read(pkg, rel).replace("\r\n", "\n").split("\n")
    st = None
    for i, l in enumerate(lines):
        if l.strip() == heading:
            st = i
            break
    if st is None:
        raise MutateFailed("节标题不存在：" + heading)
    en = len(lines)
    for j in range(st + 1, len(lines)):
        if lines[j].startswith("## "):
            en = j
            break
    pkg_write(pkg, rel, "\n".join(lines[:st] + lines[en:]))


def pkg_mkdir(pkg, rel):
    os.makedirs(os.path.join(pkg, rel), exist_ok=True)


def pkg_rename(pkg, a, b):
    if not os.path.exists(os.path.join(pkg, a)):
        raise MutateFailed("改名锚不存在：" + a)
    os.rename(os.path.join(pkg, a), os.path.join(pkg, b))


def pkg_dropprefix(pkg, rel, prefix):
    lines = pkg_read(pkg, rel).split("\n")
    hits = [l for l in lines if l.startswith(prefix)]
    if len(hits) != 1:
        raise MutateFailed("删行锚 %r 命中 %d 次（须恰 1 次）" % (prefix, len(hits)))
    pkg_write(pkg, rel, "\n".join(l for l in lines if not l.startswith(prefix)))


def pkg_inject(pkg, rel, after_prefix, extra):
    """在指定行之后插入一行——用于「把别处正文复制过来」这类第二真源变异。"""
    lines = pkg_read(pkg, rel).split("\n")
    hits = [i for i, l in enumerate(lines) if l.startswith(after_prefix)]
    if len(hits) != 1:
        raise MutateFailed("插入锚 %r 命中 %d 次（须恰 1 次）" % (after_prefix, len(hits)))
    lines.insert(hits[0] + 1, extra)
    pkg_write(pkg, rel, "\n".join(lines))


PKG_MUT = [
    ("c01", "X01 references/30-gates.md 改名（删件）",
     lambda p: pkg_rename(p, "references/30-gates.md", "references/33-gates.md")),
    ("c02", "X02 在 references/ 下建嵌套子目录（破一层深）",
     lambda p: pkg_mkdir(p, "references/nested")),
    ("c03", "X03 frontmatter name 与 version 值互换",
     lambda p: pkg_swap_fm(p, "SKILL.md")),
    ("c06", "X06 模板表 A 表头 claim_type 与 source_layer 两列互换（序位倒置）",
     lambda p: pkg_swap_header(p, "templates/claim-register.md", 20, "claim_type", "source_layer")),
    ("c19", "X19 依赖面两组件名互换（主体互换）",
     lambda p: pkg_replace(p, "references/30-gates.md",
                           "`bundle:semantic-governance` | 校验脚本",
                           "`bundle:deep-research` | 校验脚本")),
    ("c21", "X21 两子命令动词互换（主体互换）",
     lambda p: pkg_swap_words(p, "references/30-gates.md", "validate --artifact", "gate-outbound --artifact")),
    ("c24", "X24 删 §10 末尾否定句（使靶点不可反转）",
     lambda p: pkg_dropprefix(p, "references/10-contract.md", "本技能只消费")),
    ("c25", "X25 SKILL.md 指针『条目 2』改『条目 6』（指向错误条目）",
     lambda p: pkg_replace(p, "SKILL.md", "条目 2", "条目 6")),
    # ---- v4 新增：裁定九的两条实测复现（QA 席原样做法）----
    ("c11", "X26 把 §8 第 7 类原文整行复制进 20-artifact-mapping（跨文件原文复制）",
     lambda p: pkg_inject(p, "references/20-artifact-mapping.md",
                          "> 本文件只回答", "7. 是否将沉默视为认可；默认一律不算。")),
    ("c11", "X27 把 §8 第 7 类同义改写后复制进 20-artifact-mapping（同义改写绕过）",
     lambda p: pkg_inject(p, "references/20-artifact-mapping.md",
                          "> 本文件只回答", "7. 当事人不说话能不能算他点头，此处默认视作认可。")),
    ("c11", "X28 把 §5 强断言词表整行复制进 30-gates（词表整表复制）",
     lambda p: pkg_inject(p, "references/30-gates.md", "> 本文件只持判据编号与判据句",
                          "| 强断言 | `必须` / `一律` / `全部` / `绝不` / `保证` / `确保` / `均已` / `全覆盖` |")),
    ("c18", "X29 条款正文所指节由 §2 改成 §99（节不存在）",
     lambda p: pkg_replace(p, "references/40-provenance-map.md",
                           "条款正文：10-contract.md §2 | `不得跳序`",
                           "条款正文：10-contract.md §99 | `不得跳序`")),
    ("c18", "X30 落点关键词改成节内不存在的词（节在但无该内容）",
     lambda p: pkg_replace(p, "references/40-provenance-map.md",
                           "| `占位词` |", "| `强断言词表整表` |")),
    # ---- v5 新增：给新判据造结构面变异（治红4-05：新起的判据自己也须被咬）----
    ("c26", "X31 删 10-contract §11『编号与角色的发放主体』整节",
     lambda p: pkg_drop_section(p, "references/10-contract.md", "## 11. 编号与角色的发放主体")),
    ("c27", "X32 删 SKILL.md『契约总则』整节（复述节被掏空）",
     lambda p: pkg_drop_section(p, "SKILL.md", "## 契约总则")),
]


# ---------------------------------------------------------------- 检查
CHECKS = []


def check(cid, title):
    def deco(fn):
        CHECKS.append((cid, title, fn))
        return fn

    return deco


@check("c01", "七件齐备、无多余件、包目录名等于 frontmatter name")
def c01(pkg):
    got = set()
    for rel in FILES:
        p = os.path.join(pkg, rel)
        if not os.path.exists(p):
            raise Red("缺件 " + rel)
        got.add(rel.replace("\\", "/"))
    refs = sorted(os.listdir(os.path.join(pkg, "references")))
    tpls = sorted(os.listdir(os.path.join(pkg, "templates")))
    want_refs = ["10-contract.md", "20-artifact-mapping.md", "30-gates.md", "40-provenance-map.md"]
    want_tpls = ["claim-register.md", "outbound-artifact.md"]
    if refs != want_refs:
        raise Red("references/ 文件集合不等于期望（实测 %s）" % refs)
    if tpls != want_tpls:
        raise Red("templates/ 文件集合不等于期望（实测 %s）" % tpls)
    fm = read(pkg, "SKILL.md").split("---")[1]
    m = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    if not m:
        raise Red("frontmatter 缺 name")
    name = m.group(1)
    dirname = os.path.basename(os.path.abspath(pkg))
    if name != PKG_NAME:
        raise Red("frontmatter name 不等于常量 %s（实测 %s）" % (PKG_NAME, name))
    if dirname != name:
        raise Red("包目录名 %s 不等于 frontmatter name %s" % (dirname, name))
    return "七件齐备（%d 件），目录名==name==%s" % (len(got), name)


@check("c02", "SKILL.md 行数 <200；references/ 一层深；无嵌套目录")
def c02(pkg):
    txt = read(pkg, "SKILL.md")
    lines = txt.replace("\r\n", "\n").split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    if len(lines) >= 200:
        raise Red("SKILL.md %d 行 ≥ 200" % len(lines))
    for d in ("references", "templates"):
        root = os.path.join(pkg, d)
        for name in os.listdir(root):
            if os.path.isdir(os.path.join(root, name)):
                raise Red("%s/ 出现嵌套目录 %s（一层深被破坏）" % (d, name))
    return "SKILL.md %d 行 < 200；references/ 与 templates/ 均一层深" % len(lines)


@check("c03", "frontmatter：name 常量逐字、version 常量逐字、agent_created 常量逐字")
def c03(pkg):
    fm = read(pkg, "SKILL.md").split("---")[1]
    name = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    ver = re.search(r"^version:\s*(\S+)\s*$", fm, re.M)
    ac = re.search(r"^agent_created:\s*(\S+)\s*$", fm, re.M)
    if not name or name.group(1) != PKG_NAME:
        raise Red("name 不等于常量 " + PKG_NAME)
    if not ver:
        raise Red("缺 version")
    if ver.group(1) != VERSION_CONST:
        raise Red("version 不等于常量 %s（实测 %s）" % (VERSION_CONST, ver.group(1)))
    if not ac or ac.group(1) != "true":
        raise Red("agent_created 不等于常量 true")
    return "name=%s version=%s（常量全等） agent_created=true" % (name.group(1), ver.group(1))


@check("c04", "description：when 标记 + 负路由 ≥3 + ≤1536 字符 + 摘要全等")
def c04(pkg):
    fm = read(pkg, "SKILL.md").split("---")[1]
    m = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not m:
        raise Red("缺 description")
    desc = m.group(1).strip()
    if not any(w in desc for w in ("Use when", "use when", "USE WHEN", "什么时候用", "何时使用", "适用场景")):
        raise Red("description 未含 when 标记")
    if "Do NOT use for" not in desc:
        raise Red("description 缺 Do NOT use for 段")
    tail = desc.split("Do NOT use for", 1)[1]
    routes = [x for x in re.split(r"[｜|；;]", tail) if x.strip()]
    if len(routes) < 3:
        raise Red("Do NOT use for 负路由 %d 条 < 3" % len(routes))
    if len(desc) > 1536:
        raise Red("description %d 字符 > 1536" % len(desc))
    if sha(norm(desc)) != DESC_DIGEST:
        raise Red("description 摘要不等于期望（现值 %s…）" % sha(norm(desc))[:12])
    return "description %d 字符，负路由 %d 条，摘要全等" % (len(desc), len(routes))


@check("c05", "§1 表 A：20 行，字段序列/必填性序列全等 + 闭集等于 + 格式逐字全等")
def c05(pkg):
    rows = parse_table(read(pkg, "references/10-contract.md"), 4, "## 1. 主张行登记面（表 A）：必填 17 ＋ 条件必填 3 ＝ 20 列")
    head, body = rows[0], rows[1:]
    if head != ["分组", "字段", "闭集／格式", "必填性"]:
        raise Red("表 A 表头不等于期望（实测 %s）" % head)
    if len(body) != 20:
        raise Red("表 A 数据行 %d 条 ≠ 20" % len(body))
    fields = [r[1].replace("`", "") for r in body]
    if fields != EXPECT_A_FIELDS:
        raise Red("表 A 字段序列不等于期望（实测 %s）" % fields)
    req = [r[3] for r in body]
    if req != EXPECT_A_REQUIRED:
        raise Red("表 A 必填性序列不等于期望（实测 %s）" % req)
    for f, cell in [(r[1].replace("`", ""), r[2]) for r in body]:
        if f in EXPECT_A_CLOSED:
            got = set(tokens(cell))
            if got != EXPECT_A_CLOSED[f]:
                raise Red("字段 %s 的闭集取值集合不等于期望（实测 %s）" % (f, sorted(got)))
        if f in EXPECT_A_FORMAT:
            if norm(cell) != EXPECT_A_FORMAT[f]:
                raise Red("字段 %s 的格式列不等于期望（实测 %s）" % (f, norm(cell)))
    txt = read(pkg, "references/10-contract.md")
    for loc, dg, tag in ((("line", "**责任主体边界**："), RESP_BOUND_DIGEST, "责任主体边界"),
                         (("line", "**来源载体边界**："), SOURCE_BOUND_DIGEST, "来源载体边界"),
                         (("line", "**字段裁撤记录**："), ABOLISH_DIGEST, "字段裁撤记录")):
        if sha(norm(find_line(txt, loc[1]))) != dg:
            raise Red("%s句摘要不等于期望" % tag)
    return "表 A 20 行，字段/必填性序列全等，7 闭集等于，13 格式逐字全等，三句边界摘要全等"


@check("c06", "模板四表表头与 §1/§3/§4 定义逐列全等（R17 机检）")
def c06(pkg):
    reg = read(pkg, "templates/claim-register.md")
    heads = {}
    for l in reg.replace("\r\n", "\n").split("\n"):
        if not l.strip().startswith("|"):
            continue
        cells = [c.replace("`", "") for c in split_row(l)]
        if cells and cells[0] in ("claim_id", "cmp_id", "id_key"):
            heads.setdefault(len(cells), []).append(cells)
    want = {"A": EXPECT_A_FIELDS, "B": EXPECT_B_COLS, "C": EXPECT_C_COLS, "D": EXPECT_D_FIELDS}
    for tag, cols in want.items():
        found = heads.get(len(cols), [])
        hit = [h for h in found if h == cols]
        if not hit:
            raise Red("表 %s 表头（%d 列）不等于期望；同列数实测 %s" % (tag, len(cols), found))
    if len(heads.get(len(EXPECT_A_FIELDS), [])) != 1:
        raise Red("表 A 表头出现次数 ≠ 1")
    return "四张表表头逐列全等（20/9/7/13）"


@check("c07", "§3 表 D：13 行，字段/归属/必填性序列全等 + 闭集等于 + 格式逐字 + 环境轴句全等")
def c07(pkg):
    txt = read(pkg, "references/10-contract.md")
    rows = parse_table(txt, 4, "## 3. 主张级验证登记（表 D）")
    head, body = rows[0], rows[1:]
    if head != ["字段", "闭集／格式", "填写归属", "必填性"]:
        raise Red("表 D 表头不等于期望（实测 %s）" % head)
    if len(body) != 13:
        raise Red("表 D 数据行 %d 条 ≠ 13" % len(body))
    fields = [r[0].replace("`", "") for r in body]
    if fields != EXPECT_D_FIELDS:
        raise Red("表 D 字段序列不等于期望（实测 %s）" % fields)
    owner = [r[2] for r in body]
    if owner != EXPECT_D_OWNER:
        raise Red("表 D 填写归属序列不等于期望（实测 %s）" % owner)
    req = [r[3] for r in body]
    if req != EXPECT_D_REQUIRED:
        raise Red("表 D 必填性序列不等于期望（实测 %s）" % req)
    for f, cell in [(r[0].replace("`", ""), r[1]) for r in body]:
        if f in EXPECT_D_CLOSED:
            if set(tokens(cell)) != EXPECT_D_CLOSED[f]:
                raise Red("字段 %s 的闭集取值集合不等于期望" % f)
        if f in EXPECT_D_FORMAT:
            if norm(cell) != EXPECT_D_FORMAT[f]:
                raise Red("字段 %s 的格式列不等于期望（实测 %s）" % (f, norm(cell)))
    if sha(norm(find_line(txt, "**环境轴序位（全序，唯一参与大小比较的轴）**："))) != ENV_AXIS_DIGEST:
        raise Red("环境轴序位句摘要不等于期望")
    return "表 D 13 行，三序列全等，闭集与格式全等，环境轴句摘要全等"


@check("c08", "§2 来源层判定序与相容矩阵：整节摘要全等 + 6×4 逐格全等")
def c08(pkg):
    txt = read(pkg, "references/10-contract.md")
    sec = region(txt, "## 2. 来源层判定序与相容矩阵")
    if sha(norm(sec)) != SEC2_DIGEST:
        raise Red("§2 整节摘要不等于期望（现值 %s…）" % sha(norm(sec))[:12])
    rows = parse_table(txt, 5, "## 2. 来源层判定序与相容矩阵")
    body = rows[1:]
    if len(body) != 6:
        raise Red("矩阵行数 %d ≠ 6" % len(body))
    got = [[c.replace("`", "") for c in r] for r in body]
    if got != MATRIX:
        raise Red("相容矩阵 6×4 不等于期望（实测 %s）" % got)
    return "§2 整节摘要全等，矩阵 6×4 共 24 格逐格全等"


@check("c09", "§4：表 B 列 9 项、表 C 列 7 项、『唯一』释义句、表 C status 与 id_key 口径句")
def c09(pkg):
    txt = read(pkg, "references/10-contract.md")
    b = re.search(r"\*\*可比对断言登记表（表 B）列\*\*：(.+)", txt)
    if not b or tokens(b.group(1)) != EXPECT_B_COLS:
        raise Red("表 B 列清单不等于期望（实测 %s）" % (tokens(b.group(1)) if b else None))
    c = re.search(r"\*\*标识与需求主表（表 C）列\*\*：(.+)", txt)
    if not c or tokens(c.group(1)) != EXPECT_C_COLS:
        raise Red("表 C 列清单不等于期望（实测 %s）" % (tokens(c.group(1)) if c else None))
    if sha(norm(find_line(txt, "- 表 B 是**可比对断言行**的唯一登记处。"))) != UNIQ_SENT_DIGEST:
        raise Red("『唯一』释义句摘要不等于期望")
    if sha(norm(find_line(txt, "- `status` ∈ `defined` / `draft` / `retired`"))) != CSTATUS_DIGEST:
        raise Red("表 C status 约束句摘要不等于期望")
    if sha(norm(find_line(txt, "- `id_value` 是编号本体，"))) != IDKEY_DIGEST:
        raise Red("表 C id_key 识别口径句摘要不等于期望")
    return "表 B 9 列、表 C 7 列逐项全等；三句约束（唯一性／status／id_key 口径）摘要全等"


@check("c10", "§7 状态语义硬规则：整节规范化后逐字全等")
def c10(pkg):
    sec = region(read(pkg, "references/10-contract.md"), "## 7. 状态语义硬规则")
    if norm(sec) != S7_TEXT:
        raise Red("§7 不等于期望（长度 %d vs %d）" % (len(norm(sec)), len(S7_TEXT)))
    return "§7 状态语义硬规则 7 条逐字全等（%d 字符）" % len(S7_TEXT)


@check("c11", "§8 逐字全等 + 跨文件第二真源三层检测（原文短语／逐行全等复制／义素探针／词表整行）")
def c11(pkg):
    contract = read(pkg, TRUE_SOURCE)
    sec = region(contract, "## 8. 人工闸七类（唯一真源）")
    if norm(sec) != S8_TEXT:
        raise Red("§8 不等于期望")
    gates = read(pkg, "references/30-gates.md")
    if sha(norm(region(gates, "## 1. 人工闸消费点（不复制条文）"))) != GATES_S1_DIGEST:
        raise Red("30-gates §1 消费点摘要不等于期望")

    # 扫描面：references/ 全部文件，唯排除唯一真源 10-contract.md
    scan = [r for r in REFERENCES if r != TRUE_SOURCE]
    if len(scan) != 3:
        raise Red("扫描面文件数 %d ≠ 3（references/ 共 4 件，排除真源 1 件）" % len(scan))
    forbidden_lines = set()
    for src in ("## 7. 状态语义硬规则", "## 8. 人工闸七类（唯一真源）", "## 9. 禁止工具自决八条"):
        for l in region(contract, src).split("\n"):
            if norm(l):
                forbidden_lines.add(norm(l))
    for rel in scan:
        t = read(pkg, rel)
        for raw in t.replace("\r\n", "\n").split("\n"):
            line = raw.strip()
            if not line:
                continue
            pointed = ("10-contract" in line) or ("→ §" in line)
            for bad in BANNED_PHRASES:
                if bad in line and not pointed:
                    raise Red("%s 出现人工闸正文短语『%s』（第二真源）" % (rel, bad))
            if not pointed:
                if "沉默" in line and "认可" in line:
                    raise Red("%s 出现人工闸第 7 类的义素组合『沉默＋认可』（同义改写第二真源）" % rel)
                if "默认" in line and any(w in line for w in ("视作", "视为", "等同", "认可")):
                    raise Red("%s 出现人工闸第 7 类的义素组合『默认＋视作/视为/等同/认可』（同义改写第二真源）" % rel)
                for probe in HUMAN_GATE_PROBES:
                    # 在途裁定（主理人件 b47709e·裁定一甲案窄化）：仅探针层行级豁免增
                    # 「行内含『人工闸』」；BANNED／逐行全等／义素组合／词表层豁免不动
                    if probe in line and "人工闸" not in line:
                        raise Red("%s 出现人工闸正文短语『%s』（第二真源）" % (rel, probe))
                ns = sum(1 for w in STRONG_SET if w in line)
                if ns >= 3:
                    raise Red("%s 单行出现 %d 个强断言词（词表整行复制）" % (rel, ns))
                np_ = sum(1 for w in PLACEHOLDER_SET if w in line)
                if np_ >= 3:
                    raise Red("%s 单行出现 %d 个占位词（词表整行复制）" % (rel, np_))
            if norm(line) in forbidden_lines:
                raise Red("%s 出现与 §7／§8／§9 逐行全等的行（跨文件原文复制）：%s" % (rel, line[:40]))
    return "§8 七类逐字全等；扫描面 %d 件（references/ 4 件排除真源）；三层检测（短语／逐行全等／义素探针／词表整行）零命中；30-gates §1 摘要全等" % len(scan)


@check("c12", "§9 禁止工具自决八条：整节规范化后逐字全等")
def c12(pkg):
    sec = region(read(pkg, "references/10-contract.md"), "## 9. 禁止工具自决八条")
    if norm(sec) != S9_TEXT:
        raise Red("§9 不等于期望（长度 %d vs %d）" % (len(norm(sec)), len(S9_TEXT)))
    return "§9 八条逐字全等（%d 字符）" % len(S9_TEXT)


@check("c13", "判据表 R1–R17：编号集合强等 + 逐行摘要全等")
def c13(pkg):
    rows = parse_table(read(pkg, "references/30-gates.md"), 2, "## 2. 脚本闸 R1–R17")
    body = rows[1:]
    ids = [r[0].replace("`", "").strip() for r in body]
    want = ["R%d" % i for i in range(1, 18)]
    if ids != want:
        raise Red("判据编号集合不等于 R1..R17（实测 %s）" % ids)
    for (cid, dg), r in zip(ROW_DIGESTS["c13"], body):
        if sha(norm("| " + r[0] + " | " + r[1] + " |")) != dg:
            raise Red("判据行 %s 摘要不等于期望" % cid)
    return "判据 R1–R17 编号强等，17 行摘要逐行全等"


@check("c14", "负样本表 N1–N10：编号集合强等 + 逐行摘要全等 + 应咬列可指认")
def c14(pkg):
    rows = parse_table(read(pkg, "references/30-gates.md"), 4, "## 4. 负样本闸 N1–N10 与人工闸承接项 A1–A4")
    body = rows[1:]
    ids = [r[0].replace("`", "").strip() for r in body]
    want = ["N%d" % i for i in range(1, 11)]
    if ids != want:
        raise Red("负样本编号集合不等于 N1..N10（实测 %s）" % ids)
    for (cid, dg), r in zip(ROW_DIGESTS["c14"], body):
        if sha(norm("| " + r[0] + " | " + r[1] + " | " + r[2] + " | " + r[3] + " |")) != dg:
            raise Red("负样本行 %s 摘要不等于期望" % cid)
    for r in body:
        cell = r[2]
        if "不可机检" in cell:
            continue
        if not re.search(r"R\d+·第[一二三四五六]支", cell):
            raise Red("负样本 %s 的『应咬判据』不可指认到具体判据支（实测 %s）" % (r[0], cell))
    meta = gates4_meta(read(pkg, "references/30-gates.md"))
    if sha(norm(meta)) != GATES4_META_DIGEST:
        raise Red("§4 表前元规则段摘要不等于期望（『须让其声明的那一支变红』被放宽即红）")
    return "负样本 N1–N10 编号强等，10 行摘要全等，应咬列全部可指认支；§4 元规则段摘要全等"


@check("c15", "外发门 §6 表 6 行全等 + 外发模板字段行与正文规则摘要全等")
def c15(pkg):
    txt = read(pkg, "references/10-contract.md")
    rows = parse_table(txt, 2, "## 6. 外发门")
    body = rows[1:]
    fields = [r[0].replace("`", "") for r in body]
    if fields != EXPECT_OUT_FIELDS:
        raise Red("外发门字段序列不等于期望（实测 %s）" % fields)
    for f, cell in [(r[0].replace("`", ""), r[1]) for r in body]:
        if f in EXPECT_OUT_CLOSED and set(tokens(cell)) != EXPECT_OUT_CLOSED[f]:
            raise Red("外发门字段 %s 的闭集取值集合不等于期望" % f)
    for (fid, dg), r in zip(OUT_ROW_DIGESTS, body):
        if sha(norm("| " + r[0] + " | " + r[1] + " |")) != dg:
            raise Red("外发门字段 %s 的判据文案摘要不等于期望" % fid)
    outb = read(pkg, "templates/outbound-artifact.md")
    for loc, dg in OUTB_DIGESTS:
        if sha(norm(extract_loc(outb, loc))) != dg:
            raise Red("外发模板落点摘要不等于期望：%s" % (loc[1],))
    return "外发门 6 字段序列全等、闭集等于；外发模板 %d 处落点摘要全等" % len(OUTB_DIGESTS)


@check("c16", "模板四表示例行逐列合规（含 R7 条件格与 R13 第三支）；填写说明条目数 = 10")
def c16(pkg):
    reg = read(pkg, "templates/claim-register.md")

    def ex_row(ncols):
        for l in reg.replace("\r\n", "\n").split("\n"):
            if l.strip().startswith("|"):
                cells = split_row(l)
                if len(cells) == ncols and cells[0].replace("`", "") in ("C-001", "CMP-001", "需求", "线号"):
                    return cells
        raise Red("找不到 %d 列示例行" % ncols)

    a = ex_row(20)
    dup = {k: v.replace("`", "").strip() for k, v in zip(EXPECT_A_FIELDS, a)}
    if not re.fullmatch(r"C-[0-9]{3,}", dup["claim_id"]):
        raise Red("表 A 示例 claim_id 格式不符")
    for f in ("claim_type", "source_layer", "evidence_tag", "authority", "status", "external_effect", "assertion_form"):
        if dup[f] not in EXPECT_A_CLOSED[f]:
            raise Red("表 A 示例列 %s 取值 %s 不在闭集内" % (f, dup[f]))
    arts = [x.strip() for x in dup["linked_artifacts"].split(";")]
    ok_prefix = ("source:", "cite:", "artifact:", "authorization:")
    for x in arts:
        if not x.startswith(ok_prefix):
            raise Red("表 A 示例 linked_artifacts 出现非法前缀：%s" % x)
    for x in arts:
        if x.startswith("artifact:"):
            if not re.fullmatch(r"artifact:(TKT|RCP|PRD|QAV|DLV|OUT|REQ|CMP)-[0-9]+", x):
                raise Red("表 A 示例 artifact: 前缀不在闭集内：%s" % x)
        if x.startswith("source:"):
            if not re.fullmatch(r"source:(INTK|RES|MSR|DOC)-[0-9]+", x):
                raise Red("表 A 示例 source: 前缀不在闭集内：%s" % x)

    # R7 相容矩阵：示例行的 source_layer × authority 必须落在「允许」或已满足条件的「条件」格
    sl, au = dup["source_layer"], dup["authority"]
    mrow = [r for r in MATRIX if r[0] == sl]
    if not mrow:
        raise Red("表 A 示例 source_layer=%s 不在矩阵行内" % sl)
    cols = ["binding", "consultative", "internal_only", "unverified"]
    if au not in cols:
        raise Red("表 A 示例 authority=%s 不在矩阵列内" % au)
    cell = mrow[0][1 + cols.index(au)]
    if cell == "禁止":
        raise Red("表 A 示例行违反 R7：%s × %s 为『禁止』格" % (sl, au))
    if cell == "条件":
        if not dup["approver"].startswith("human:"):
            raise Red("表 A 示例行落在 R7『条件』格但 approver 非 human:<ref>（实测 %s）" % dup["approver"])
        if dup["status"] not in ("accepted", "external_pending", "external_confirmed"):
            raise Red("表 A 示例行落在 R7『条件』格但 status=%s 不满足条件" % dup["status"])
        if dup["expiry"] == "none":
            raise Red("表 A 示例行落在 R7『条件』格但 expiry=none")
    # 补强 A：自由描述形态的 responsibility_basis 须同行标 unverified（正向可判条件）
    basis = dup["responsibility_basis"]
    if basis != "none" and not re.fullmatch(r"(source|authorization):[A-Z]+-[0-9]+", basis):
        if au != "unverified":
            raise Red("表 A 示例 authority=%s 而 responsibility_basis=自由描述 %r（须 authority=unverified）" % (au, basis))
    # R13 第三支
    if au == "binding":
        ap = dup["approver"]
        if not ap.startswith("human:"):
            raise Red("表 A 示例 authority=binding 但 approver 不以 human: 起头（实测 %s）" % ap)
        if ap.split(":", 1)[1] != dup["decision_owner"].split(":", 1)[-1]:
            raise Red("表 A 示例 authority=binding 但 approver 的 ref 与 decision_owner 不同")

    b = ex_row(9)
    dupb = dict(zip(EXPECT_B_COLS, b))
    if dupb["cmp_kind"] not in ("quantity", "datetime", "identifier", "completeness"):
        raise Red("表 B 示例 cmp_kind 不在闭集内")
    if dupb["completeness_mode"] not in ("cleared", "partial", "none"):
        raise Red("表 B 示例 completeness_mode 不在闭集内")
    if not re.fullmatch(r"artifact:(TKT|RCP|PRD|QAV|DLV|OUT|REQ|CMP)-[0-9]+", dupb["source_artifact"]):
        raise Red("表 B 示例 source_artifact 不在 artifact: 前缀闭集内：%s" % dupb["source_artifact"])

    c = ex_row(7)
    dupc = dict(zip(EXPECT_C_COLS, c))
    if dupc["status"] not in ("defined", "draft", "retired"):
        raise Red("表 C 示例 status 不在闭集内")
    if dupc["req_required_environment"] not in ("mock", "test", "integration", "production", "none"):
        raise Red("表 C 示例 req_required_environment 不在闭集内")
    if dupc["id_value"].startswith("REQ-") and dupc["id_key"] != "需求":
        raise Red("表 C 示例 REQ- 行的 id_key 不等于『需求』（实测 %s）" % dupc["id_key"])

    d = ex_row(13)
    dupd = dict(zip(EXPECT_D_FIELDS, d))
    if dupd["qa_result"] not in ("pending", "passed_at_actual", "passed_with_exemption", "failed", "blocked"):
        raise Red("表 D 示例 qa_result 不在闭集内")
    if dupd["exemption"] not in ("none", "partial", "full"):
        raise Red("表 D 示例 exemption 不在闭集内")
    if dupd["actual_environment"] not in ("mock", "test", "integration", "production", "unverified"):
        raise Red("表 D 示例 actual_environment 不在闭集内")

    instr = region(reg, "## 填写说明")
    n = len(re.findall(r"^\d+\.\s", instr, re.M))
    if n != 11:
        raise Red("填写说明条目 %d 条 ≠ 11" % n)
    return "四表示例行逐列合规（R7 条件格 %s×%s=%s；R13 第三支在位）；填写说明 11 条" % (sl, au, cell)


@check("c17", "§5 词表：强断言 8 词、占位 8 词集合全等；两表分工句；§10 映射摘要全等")
def c17(pkg):
    txt = read(pkg, "references/10-contract.md")
    rows = parse_table(txt, 2, "## 5. 强断言词表与占位词表")
    body = rows[1:]
    if len(body) != 2:
        raise Red("词表行数 %d ≠ 2" % len(body))
    got = {r[0]: set(tokens(r[1])) for r in body}
    if got.get("强断言") != STRONG_SET:
        raise Red("强断言词表不等于期望（实测 %s）" % sorted(got.get("强断言") or []))
    if got.get("占位词") != PLACEHOLDER_SET:
        raise Red("占位词表不等于期望（实测 %s）" % sorted(got.get("占位词") or []))
    pat = " ".join(x[1] for x in PATTERNS_PAIRS)
    shared = 0
    for w in got["强断言"]:
        if w in pat:
            shared += 1
            if w not in ("清零",):
                raise Red("强断言词 %s 仍出现在抽取模式内（重叠未治）" % w)
    if sha(norm(find_line(txt, "**两表分工（治重叠）**："))) != S5SPLIT_DIGEST:
        raise Red("§5 两表分工句摘要不等于期望")
    sec10 = region(txt, "## 10. deep-research 证据标签消费映射")
    if sha(norm(sec10)) != SEC10_DIGEST:
        raise Red("§10 映射整节摘要不等于期望")
    # 语义守卫（治红4-03 的「机检把错的当合法性来源」）：摘要之外，真名必须逐字在位、
    # 且不得出现他包笔记格式细则文件名。否则作者只要顺手把摘要常量改掉，错名就能复活。
    for tok in FOREIGN_FILE_TOKENS:
        if tok in sec10:
            raise Red("§10 以他包包内文件名引用条款（%s）：条款名须写成「包名 ＋ 条款位置」" % tok)
    for need in ("`SKILL.md §六 证据纪律`", "标签闭集（五标·英文）", "措辞分级"):
        if need not in sec10:
            raise Red("§10 缺真名要件 %r（只改摘要救不回错名）" % need)
    return ("强断言 8 词、占位 8 词两个集合全等；**强断言词与抽取模式正则无共享触发词（逐词子串判定，命中 %d 处）**；"
            "占位词与本项无关（未验，不作『零交集』表述）；两表分工句与 §10 摘要全等" % shared)


@check("c18", "来源档 23 条：三档出处语法整名全等 + 组闭集自洽 + 节存在 + 节内关键词")
def c18(pkg):
    txt = read(pkg, "references/40-provenance-map.md")
    head = resolve_section(txt, "表头")
    g1 = parse_group(head, 1)
    g2 = parse_group(head, 2)
    g3 = parse_group(head, 3)
    if g1 != PASSAGE_NAMES:
        raise Red("表头第 1 组通行做法名闭集不等于常量（实测 %s）" % sorted(g1))
    if g2 != PARADIGM_NAMES:
        raise Red("表头第 2 组命名范式闭集不等于常量（实测 %s）" % sorted(g2))
    if g3 != CARRIERS:
        raise Red("表头第 3 组授权载体闭集不等于常量（实测 %s）" % sorted(g3))

    rows = parse_table(txt, 5)
    body = rows[1:]
    if len(body) != 23:
        raise Red("来源档条目 %d 条 ≠ 23" % len(body))
    ids = [r[0] for r in body]
    if ids != [str(i) for i in range(1, 24)]:
        raise Red("来源档条目编号不等于 1..23（实测 %s）" % ids)
    for r in body:
        lvl, src, kw = r[2], r[3], r[4]
        joined = "".join(r)
        for bad in ("同上", "见上"):
            if bad in joined:
                raise Red("条目 %s 出现 %s 式虚指" % (r[0], bad))
        if lvl not in ("业界出处", "命名范式", "本地约定"):
            raise Red("条目 %s 档位不在三档闭集内：%s" % (r[0], lvl))
        if not src or src.strip() in ("—", "-", ""):
            raise Red("条目 %s 出处列为空或破折号" % r[0])
        if lvl == "业界出处":
            m = re.search(r"通行做法：([^；;]+)", src)
            if not m:
                raise Red("条目 %s 的业界出处未写出通行做法名称" % r[0])
            name = strip_paren(m.group(1))
            if name not in g1:
                raise Red("条目 %s 的通行做法名 %r 不是整名全等（闭集：%s）" % (r[0], name, sorted(g1)))
            if "条款正文：" in src:
                raise Red("条目 %s 档位为业界出处却写了条款正文（档位与语法不符）" % r[0])
            continue
        if lvl == "命名范式":
            m = re.search(r"范式：([^（；;]+)", src)
            if not m:
                raise Red("条目 %s 的命名范式未写出范式名称" % r[0])
            if m.group(1).strip() not in g2:
                raise Red("条目 %s 的范式名 %r 不在闭集内" % (r[0], m.group(1).strip()))
        else:
            m = re.search(r"授权载体：([^；;]+)", src)
            if not m:
                raise Red("条目 %s 缺授权载体" % r[0])
            carriers = [x.strip() for x in m.group(1).split("＋")]
            if not carriers or any(not c for c in carriers):
                raise Red("条目 %s 授权载体拆分出空项" % r[0])
            for name in carriers:
                if name not in g3:
                    raise Red("条目 %s 的授权载体 %r 不在闭集内" % (r[0], name))
        if "条款正文：" not in src:
            if kw.strip() != "—":
                raise Red("条目 %s 未写条款正文，但落点关键词不是破折号（%r）" % (r[0], kw))
            continue
        m2 = re.search(r"条款正文：([0-9A-Za-z\.\-]+\.md) §([0-9]+|[^\s|§]+)", src)
        if not m2:
            raise Red("条目 %s 缺『条款正文：<本包文件名> §<小节标签>』" % r[0])
        fname, label = m2.group(1), m2.group(2)
        if fname not in FILES_BASENAMES:
            raise Red("条目 %s 的条款正文指向非本包文件 %s" % (r[0], fname))
        target = [x for x in FILES if x.endswith("/" + fname) or x == fname]
        if len(target) != 1:
            raise Red("条目 %s 的条款正文文件名在本包不唯一：%s" % (r[0], fname))
        body_text = resolve_section(read(pkg, target[0]), label)
        if not kw or kw.strip() == "—":
            raise Red("条目 %s 有条款正文但落点关键词为空或破折号" % r[0])
        words = tokens(kw) or [kw]
        for w in words:
            if norm(w) not in norm(body_text):
                raise Red("条目 %s 的落点关键词 %r 不在 %s §%s 正文内（该节无此内容）" % (r[0], w, fname, label))
    return "来源档 23 条编号强等；三档语法整名全等；三组闭集与表头声明自洽；23 条落点节全部存在且含声明关键词；零『同上』"


@check("c19", "依赖面 5 行记号形态全等（不钉版本）；七件内 bundle: 记号同形同闭集；零跨包路径")
def c19(pkg):
    gates = read(pkg, "references/30-gates.md")
    rows = parse_table(gates, 2, "## 5. 依赖面与能力边界")
    body = [r for r in rows[1:] if r[0].startswith("`bundle:")]
    if len(body) != 5:
        raise Red("依赖面表数据行 %d 条 ≠ 5" % len(body))
    comps = [tokens(r[0])[0] for r in body]
    if comps != EXPECT_DEPS:
        raise Red("依赖组件序列不等于期望（实测 %s）" % comps)
    if set(x.split(":", 1)[1] for x in comps) != DEP_COMPONENTS:
        raise Red("依赖组件名集合不等于期望（实测 %s）" % sorted(x.split(":", 1)[1] for x in comps))
    if sha(norm(find_line(gates, "**为何不钉版本"))) != DEPWHY_DIGEST:
        raise Red("30-gates §5『为何不钉版本』句摘要不等于期望")
    for rel in FILES:
        t = re.sub(r"<!--\s*spec-provenance v1.*?-->", "", read(pkg, rel), flags=re.S)
        for tok in re.findall(r"bundle:[A-Za-z0-9<>_-]+", t):
            if not re.fullmatch(r"bundle:[a-z0-9-]+", tok):
                raise Red("%s 的依赖记号 %r 形态不符（须 bundle:<组件名>，不带版本号）" % (rel, tok))
            if tok.split(":", 1)[1] not in DEP_COMPONENTS:
                raise Red("%s 的依赖记号 %r 组件名不在闭集内" % (rel, tok))
        for bad in ("skills/", "agent-skills/", "agent-experts/", ".collab/", "../"):
            if bad in t:
                raise Red("%s 出现跨包/仓根路径片段：%s" % (rel, bad))
        if re.search(r"包\s*`?(references|templates|scripts)/", t):
            raise Red("%s 以裸包内路径引用跨包文件（应改『包名＋条款名』）" % rel)
    return "依赖 5 行组件序列全等、五记号不带版本；七件 bundle: 记号同形同闭集；零跨包路径"


@check("c20", "抽取模式 4 类逐字全等；4 例普通工作票不命中；4 例真断言命中")
def c20(pkg):
    txt = read(pkg, "references/10-contract.md")
    rows = parse_table(txt, 2, "**受限抽取模式（闭集，语境化：先有断言引导词，再有数值或时点）**")
    body = rows[1:]
    if len(body) != 4:
        raise Red("抽取模式类数 %d ≠ 4" % len(body))
    got = [(r[0].replace("`", ""), norm(r[1]).strip("`")) for r in body]
    if got != PATTERNS_PAIRS:
        raise Red("抽取模式 4 类不等于期望（实测 %s）" % got)
    regs = [re.compile(p) for _, p in PATTERNS_PAIRS]
    for s in PLAIN_SAMPLES:
        for rgx in regs:
            if rgx.search(s):
                raise Red("普通工作票正样本被误触发：%s" % s)
    for s in TRUE_SAMPLES:
        if not any(rgx.search(s) for rgx in regs):
            raise Red("真断言正样本未被命中：%s" % s)
    return "模式 4 类逐字全等；%d 例普通票零误触发；%d 例真断言全命中" % (len(PLAIN_SAMPLES), len(TRUE_SAMPLES))


@check("c21", "三子命令表 3 行；判据归属列取值全部在 R1–R17 内")
def c21(pkg):
    gates = read(pkg, "references/30-gates.md")
    rows = parse_table(gates, 4, "## 3. `semantic-governance` 三子命令调用契约")
    body = rows[1:]
    names = [tokens(r[0])[0] for r in body]
    if names != EXPECT_SUBCMDS:
        raise Red("子命令序列不等于期望（实测 %s）" % names)
    allcells = " ".join(r[1] + " " + r[2] + " " + r[3] for r in body)
    for rid in re.findall(r"\bR(\d+)\b", allcells):
        if not (1 <= int(rid) <= 17):
            raise Red("调用契约引用了未定义判据号 R%s" % rid)
    return "三子命令 3 行全等；引用判据号全部落在 R1–R17"


@check("c22", "20-mapping §1 七行摘要 + §2 整节摘要 + §3 整节摘要 + 七桶 125 组合穷举")
def c22(pkg):
    txt = read(pkg, "references/20-artifact-mapping.md")
    rows = parse_table(txt, 4, "## 1. 七类工件的必填面")
    body = rows[1:]
    if [r[0] for r in body] != EXPECT_ARTIFACTS:
        raise Red("七类工件序列不等于期望（实测 %s）" % [r[0] for r in body])
    if len(body) != 7:
        raise Red("§1 工件行数 %d ≠ 7" % len(body))
    for (name, dg), r in zip(SEC1_MAP_DIGESTS, body):
        if sha(norm("|" + "|".join(r) + "|")) != dg:
            raise Red("20-mapping §1 工件行 %s 摘要不等于期望" % name)
    if sha(norm(region(txt, "## 2. 登记闭包"))) != SEC2_MAP_DIGEST:
        raise Red("20-mapping §2 整节摘要不等于期望")
    rows3 = parse_table(txt, 2, "## 3. 交付汇总聚合字段（七桶＋分母，互斥且完备）")
    body3 = rows3[1:]
    fields = [tokens(r[0])[0] if tokens(r[0]) else r[0] for r in body3]
    if fields != EXPECT_AGG:
        raise Red("聚合字段序列不等于期望（实测 %s）" % fields)
    if sha(norm(region(txt, "## 3. 交付汇总聚合字段（七桶＋分母，互斥且完备）"))) != SEC3_MAP_DIGEST:
        raise Red("聚合整节摘要不等于期望（现值 %s…）" % sha(norm(region(txt, "## 3. 交付汇总聚合字段（七桶＋分母，互斥且完备）")))[:12])
    # 七桶穷举：125 组合逐个落入恰一个桶，且七桶皆可达
    seen = {}
    for req in ENV_REQ:
        for act in ENV_ACT:
            for qa in QA_SET:
                seen.setdefault(agg_bucket(req, act, qa), 0)
                seen[agg_bucket(req, act, qa)] += 1
    if set(seen) != set(EXPECT_AGG[1:]):
        raise Red("七桶覆盖不全或出现空桶（实测 %s）" % sorted(seen))
    total = sum(seen.values())
    if total != len(ENV_REQ) * len(ENV_ACT) * len(QA_SET):
        raise Red("穷举总数 %d 不等于组合数" % total)
    if agg_bucket("none", "integration", "passed_at_actual") != "not_required":
        raise Red("未提出要求环境的主张被记入 %s（应为 not_required）" % agg_bucket("none", "integration", "passed_at_actual"))
    if agg_bucket("integration", "integration", "passed_at_actual") != "mock_only":
        raise Red("integration 实况应计入 mock_only（不把 integration 掉出等式）")
    if agg_bucket("production", "production", "pending") != "pending":
        raise Red("production+pending 应计入 pending")
    return "§1 七行摘要全等；§2／§3 整节摘要全等；七桶 %d 组合穷举全落且七桶皆可达（not_required 已可达）" % total


@check("c23", "人工闸承接项 A1–A4 表 4 行摘要全等 + 能力边界段摘要全等")
def c23(pkg):
    gates = read(pkg, "references/30-gates.md")
    rows = parse_table(gates, 3, "**人工闸承接项（明示不可机检，不冒充机检）**")
    body = rows[1:]
    if [r[0] for r in body] != ["A1", "A2", "A3", "A4"]:
        raise Red("承接项编号不等于 A1/A2/A3/A4")
    if sha(norm(" || ".join("|".join(r) for r in body))) != ACCEPT_DIGEST:
        raise Red("承接项 A1–A4 内容摘要不等于期望")
    if sha(norm(find_line(gates, "**能力边界声明**："))) != BOUND_DIGEST:
        raise Red("能力边界声明摘要不等于期望")
    return "承接项 A1–A4 摘要全等；能力边界声明摘要全等"


@check("c24", "等长反义自检：全部靶点经 REV 替换后长度相等、内容必变、摘要必变")
def c24(pkg):
    bad = 0
    for e in EXPECT_TARGETS:
        txt = read(pkg, e["file"])
        cur = extract_loc(txt, e["loc"])
        rv = reverse_text(cur)
        if len(rv) != len(cur):
            raise Red("靶点 %s 的 REV 长度不等（%d vs %d）" % (e["id"], len(rv), len(cur)))
        if rv == cur:
            raise Red("靶点 %s 无可反转词（REV 后内容未变）" % e["id"])
        if sha(norm(rv)) == sha(norm(cur)):
            raise Red("靶点 %s 的 REV 摘要未变" % e["id"])
        bad += 1
    return "靶点 %d 个，REV 全部等长且内容必变（长度阈值类判据在此失效）" % bad


@check("c25", "术语别名 ≥8 行且非空；主类型段指针所指来源档条目确为混装判据")
def c25(pkg):
    txt = read(pkg, "SKILL.md")
    rows = parse_table(txt, 2, "## 术语别名（用户怎么说 ↔ 契约怎么叫）")
    body = rows[1:]
    if len(body) < 8:
        raise Red("术语别名 %d 行 < 8" % len(body))
    for r in body:
        if not r[0].strip() or not r[1].strip():
            raise Red("术语别名出现空单元格")
    main = resolve_section(txt, "主类型段")
    m = re.search(r"条目\s*([0-9]+)", main)
    if not m:
        raise Red("主类型段未写出来源档条目号")
    n = m.group(1)
    prov = read(pkg, "references/40-provenance-map.md")
    hit = [r for r in parse_table(prov, 5)[1:] if r[0] == n]
    if len(hit) != 1:
        raise Red("SKILL.md 所称『条目 %s』在来源档中不存在" % n)
    if "混装" not in hit[0][1]:
        raise Red("SKILL.md 所指『条目 %s』不是混装合法性判据（实测条目名：%s）" % (n, hit[0][1]))
    return "术语别名 %d 行；主类型段指针指向来源档条目 %s 且该条确为混装判据" % (len(body), n)


@check("c26", "§11 编号与角色的发放主体：整节摘要 + 引用型字段五闭集 + 禁令在位 + 表 A 编号前缀闭集")
def c26(pkg):
    txt = read(pkg, "references/10-contract.md")
    sec = region(txt, "## 11. 编号与角色的发放主体")
    if sha(norm(sec)) != SEC11_DIGEST:
        raise Red("§11 整节摘要不等于期望（现值 %s…）" % sha(norm(sec))[:12])
    rows = parse_table(txt, 3, "**引用型字段五项闭集与无号写法**：")
    fields = [r[0].replace("`", "") for r in rows[1:]]
    if fields != EXPECT_REF_FIELDS:
        raise Red("引用型字段闭集不等于期望（实测 %s）" % fields)
    for need in ("编号两分发放", "禁造号", "不得留空", "不得编位号"):
        if need not in sec:
            raise Red("§11 缺声明字面：%s（改义即红）" % need)
    reg = read(pkg, "templates/claim-register.md")
    a = None
    for l in reg.replace("\r\n", "\n").split("\n"):
        if not l.strip().startswith("|"):
            continue
        cells = split_row(l)
        if len(cells) == 20 and cells[0].replace("`", "").strip() == "C-001":
            a = dict(zip(EXPECT_A_FIELDS, [c.replace("`", "").strip() for c in cells]))
            break
    if a is None:
        raise Red("表 A 示例行不存在，编号前缀无从判定")
    n_ref = 0
    for f in ("linked_artifacts", "responsibility_basis"):
        for tok in [x.strip() for x in a[f].split(";") if x.strip()]:
            if tok == "none" or FREE_DESC_RE.search(tok) or ":" not in tok:
                continue  # 自由描述：交由下面的「authority 必须 unverified」判，不按编号形态误杀
            n_ref += 1
            m = re.fullmatch(r"([a-z_]+):([A-Z]+)-([0-9]+)(?:#.+)?", tok)
            if not m:
                raise Red("表 A 示例 %s 的引用 %r 不是『kind:PREFIX-digits』形态" % (f, tok))
            if m.group(2) not in ID_PREFIXES:
                raise Red("表 A 示例 %s 的编号前缀 %s 不在已登记前缀闭集内（禁造号）" % (f, m.group(2)))
    # 正向可判条件：任何自由描述（引用型字段或角色 <ref>）⇒ 该行 authority 必须 unverified
    free = []
    for f in FREE_DESC_FIELDS:
        v = a.get(f, "")
        if not v or v == "none":
            continue
        for tok in v.split(";"):
            tok = tok.strip()
            if not tok or tok == "none":
                continue
            val = tok.split(":", 1)[1] if ":" in tok else tok
            if FREE_DESC_RE.search(val):
                free.append((f, tok))
    if free and a["authority"] != "unverified":
        raise Red("表 A 示例行有自由描述 %s 但 authority=%s（自由描述 ⇒ 必须 unverified；禁造号不靠黑名单，靠如实降格证据强度）"
                  % (free[:2], a["authority"]))
    # 责任链自洽（裁定十二 1／2 的机检形态）：1–4 层必须有主体与依据；5–6 层不得硬编主体
    sl = a["source_layer"]
    if sl in ("legal_regulatory", "contractual", "approved_baseline", "customer_request"):
        if a["accountable_party"] == "none" or a["responsibility_basis"] == "none":
            raise Red("表 A 示例行在 1–4 层却缺责任链（accountable_party=%s，basis=%s）" % (a["accountable_party"], a["responsibility_basis"]))
    if sl in ("technical_design", "internal_assumption"):
        if a["accountable_party"] != "none" and a["responsibility_basis"] == "none":
            raise Red("表 A 示例行在 %s 层硬编了责任主体（accountable_party=%s 而 basis=none）：须单列『无责任主体主张』，禁硬编填充" % (sl, a["accountable_party"]))
    if a["authority"] in ("binding", "consultative") and a["decision_owner"] == "none":
        raise Red("表 A 示例行 authority=%s 却 decision_owner=none（裁定十二 2：只对 binding／consultative 强制非空）" % a["authority"])
    return ("§11 摘要全等；五字段闭集逐字等；四条禁令字面在位；表 A %d 处引用编号前缀全部落在 %d 个已登记前缀内；"
            "自由描述 %d 处（authority=%s，正向条件%s）；责任链自洽（%s 层）"
            % (n_ref, len(ID_PREFIXES), len(free), a["authority"],
               "成立" if not free or a["authority"] == "unverified" else "不成立", sl))


@check("c27", "SKILL.md 三节整节摘要 + 10 条总则与真源双向绑定（治『复述可漂移而永远绿』）")
def c27(pkg):
    txt = read(pkg, "SKILL.md")
    for head, dg in SKILL3_DIGESTS:
        if sha(norm(region(txt, head))) != dg:
            raise Red("%s 整节摘要不等于期望（现值 %s…）" % (head, sha(norm(region(txt, head)))[:12]))
    taoz = region(txt, "## 契约总则")
    items = {}
    for l in taoz.replace("\r\n", "\n").split("\n"):
        m = re.match(r"^(\d+)\.\s+(.*)$", l)
        if m:
            items[int(m.group(1))] = m.group(2)
    if sorted(items) != list(range(1, 11)):
        raise Red("契约总则条目号不等于 1..10（实测 %s）" % sorted(items))
    for n, key, rel, src_key in TAOZE_BIND:
        if key not in items[n]:
            raise Red("总则第 %d 条未含真源关键子串 %r（复述已漂移）" % (n, key))
        if src_key not in read(pkg, rel):
            raise Red("总则第 %d 条所指真源 %s 内已无 %r（真源被改，复述成了唯一真源）" % (n, rel, src_key))
    return "三节摘要全等；总则 10 条逐条与真源双向绑定（%d 组）" % len(TAOZE_BIND)


@check("c28", "跨包条款名：对照表 5 行与依赖面同序、条款名闭集、取证口径闭集、他包文件名式引用零命中")
def c28(pkg):
    gates = read(pkg, "references/30-gates.md")
    rows = parse_table(gates, 3, "**跨包条款名对照（本包只引用下列条款名，别名一律判违例）**：")
    body = rows[1:]
    comps = [r[0].replace("`", "") for r in body]
    if comps != EXPECT_DEPS:
        raise Red("对照表组件序列不等于依赖面组件序列（实测 %s）" % comps)
    if sha(norm(" || ".join("|".join(r) for r in body))) != CROSS_NAME_DIGEST:
        raise Red("跨包条款名对照表内容摘要不等于期望")
    allowed = set()
    for r in body:
        if r[2] not in EVIDENCE_TIERS:
            raise Red("组件 %s 的取证口径 %r 不在四值闭集内（%s）" % (r[0], r[2], sorted(EVIDENCE_TIERS)))
        if "无跨包条款" in r[1]:
            continue
        for name in [x.strip().strip("`") for x in re.split("／", r[1]) if x.strip()]:
            allowed.add(name)
    allow_all = allowed | CARRIERS
    n_hit = 0
    for rel in FILES:
        t = re.sub(r"<!--\s*spec-provenance v1.*?-->", "", read(pkg, rel), flags=re.S)
        for tok in FOREIGN_FILE_TOKENS:
            if tok in t:
                raise Red("%s 以他包包内文件名引用条款（%s）：条款名须写成「包名 ＋ 条款位置」" % (rel, tok))
        for m in re.finditer(r"`([^`\n]+)`", t):
            inner = m.group(1)
            mm = re.match(r"^(deep-research|external-advisor-collab|object-audit|object-build|semantic-governance|sop)\s+(.+)$", inner)
            if not mm:
                continue
            n_hit += 1
            if inner not in allow_all:
                raise Red("%s 的反引号条款名 %r 不在闭集内（闭集：%s）" % (rel, inner, sorted(allow_all)))
    return "对照表 5 行与依赖面同序、摘要全等、取证口径四值闭集；反引号条款名 %d 处全部在闭集内；他包文件名式引用零命中" % n_hit


# ---------------------------------------------------------------- 辅助：表头分组与括号剥离
def parse_group(head, idx):
    m = re.search(r"第\s*%d\s*组（[^）]*）：(.+)" % idx, head)
    if not m:
        raise Red("表头缺第 %d 组闭集声明" % idx)
    return set(tokens(m.group(1)))


def strip_paren(s):
    return re.sub(r"（[^）]*）\s*$", "", s.strip()).strip()


# ---------------------------------------------------------------- 聚合分桶（与 20-mapping §3 判决序同构）
ENV_REQ = ("none", "mock", "test", "integration", "production")
ENV_ACT = ("unverified", "mock", "test", "integration", "production")
QA_SET = ("pending", "passed_at_actual", "passed_with_exemption", "failed", "blocked")


def agg_bucket(req, act, qa):
    if qa in ("failed", "blocked"):
        return "failed"
    if act == "unverified":
        return "unverified"
    if qa == "passed_with_exemption":
        return "excluded_by_approval"
    if req == "none":
        return "not_required"
    if act == "production" and qa == "passed_at_actual":
        return "real_env_passed"
    if act in ("mock", "test", "integration"):
        return "mock_only"
    return "pending"


# ---------------------------------------------------------------- 变异算子
def mut_del(text, loc):
    return apply_loc(text, loc, "")


def mut_rev(text, loc):
    return apply_loc(text, loc, reverse_text(extract_loc(text, loc)))


def mut_pad(text, loc):
    return apply_loc(text, loc, extract_loc(text, loc) + " 补充说明见附注。")


def mut_sub(text, old, new, key=None):
    """字面替换。裁定七：锚命中数必须恰为 1，否则记 MutateFailed 使整轮失败。"""
    n = text.count(old)
    if n == 0:
        raise NotHere(old[:40])
    if n > 1:
        raise MutateFailed("字面锚命中 %d 次（须恰 1 次）：%r" % (n, old[:40]))
    out = text.replace(old, new, 1)
    if out == text:
        raise MutateFailed("变异前后文本全等（未生效）：%r" % (old[:40],))
    return out


def mut_sub_all_rows(text, ncols, start, col, old, new):
    lines = text.replace("\r\n", "\n").split("\n")
    off = None
    for i, l in enumerate(lines):
        if l.strip() == start:
            off = i
            break
    if off is None:
        raise NotHere(start)
    hit = 0
    for i in range(off, len(lines)):
        if not lines[i].strip().startswith("|"):
            if hit:
                break
            continue
        cells = split_row(lines[i])
        if len(cells) != ncols or all(re.fullmatch(r"[:\- ]*", c) for c in cells):
            continue
        if col < len(cells) and cells[col] == old:
            cells[col] = new
            lines[i] = "| " + " | ".join(cells) + " |"
            hit += 1
    if not hit:
        raise NotHere(old)
    return "\n".join(lines)


def build_mutations():
    """每条 (检查号, 名称, 函数, 文件键, 组别)。组别：A=对方席 QA v3 复刻；B=对方席产品席 v3 复刻；
    C=对方席定向反转（R18／R16）；D=v4 新增定向（裁定七自证与裁定九复现）。"""
    M = []

    def add(cid, name, fn, key, group):
        M.append((cid, name, fn, key, group))

    # A. 对方席（QA 席）复刻 23 条
    add("c05", "A01 表 A 必填性列全改『可选』",
        lambda t: mut_sub_all_rows(t, 4, "## 1. 主张行登记面（表 A）：必填 17 ＋ 条件必填 3 ＝ 20 列", 3, "必填", "可选"), None, "A")
    add("c07", "A02 表 D 填写归属『只由 QA 填』改『由生产者填』",
        lambda t: mut_sub_all_rows(t, 4, "## 3. 主张级验证登记（表 D）", 2, "只由 QA 填", "由生产者填"), None, "A")
    add("c08", "A03 删『条件』判据段整句＋删矩阵外违例句",
        lambda t: mut_del(mut_sub(t, "**「条件」的判据**：`approver` 形如 `human:<ref>`，且 `status` ∈ `accepted` / `external_pending` / `external_confirmed`，且 `expiry ≠ none`；`legal_regulatory` 与 `contractual` 另须 `linked_artifacts` 含至少一条 `cite:` 引用。\n\n", ""),
                          ("line", "**未在矩阵中出现的组合一律判违例**")), None, "A")
    add("c05", "A04 责任边界句极性翻转（保留『不得单独』子串）",
        lambda t: mut_sub(t, "**责任主体边界**：`requestee` 是请求对象，不得单独充当 `accountable_party`", "**责任主体边界**：`accountable_party` 不得单独充当 `requestee`，故请求对象恒可顶替"), None, "A")
    add("c10", "A05 §7 第 1 条换同长度废话",
        lambda t: mut_sub(t, "1. `accepted` 不等于 `external_confirmed`；内部接受不得写成外部确认。",
                          "1. 内部状态与外部状态在命名层面互不影响，措辞以可读为先。"), None, "A")
    add("c12", "A06 §9 第 3 条换废话",
        lambda t: mut_sub(t, "3. 不得把内部冻结自动转为外部确认。",
                          "3. 内部冻结的外化处理应当谨慎并留痕备查。"), None, "A")
    add("c13", "A07b R4 换 100 字同语义废话（长度阈值拦不住）",
        lambda t: mut_sub(t, "| R4 | 验证对账四支：", "| R4 | 验证对账方面的工作应当由相关责任方在各自的工序内按既有惯例稳妥推进并保留必要的过程记录，具体口径以实际执行情况为准，如遇分歧由责任方协商确定，本条不另设强制约束条件，相关判断由执行方自行把握，机器仅作提示不作判定，历史做法可作参考。另："), None, "A")
    add("c14", "A08b N4 换 70 字废话",
        lambda t: mut_sub(t, "| N4 | 降级（`exemption=partial`）无 `fallback_criterion` 或无表 D `reopen_trigger`。",
                          "| N4 | 关于降级场景下的若干填写要求，宜由填表方结合实际情况自行把握，本表不作硬性约束，也不设专门的比较目标，相关事项在执行层协商处理即可，机器不必介入。"), None, "A")
    add("c11", "A09 人工闸第 7 类同义复述回 30-gates",
        lambda t: mut_sub(t, "- 沉默效力（`reconcile`）：", "- 是否把当事人的沉默当作认可，此处一律不算数；沉默效力（`reconcile`）："), "gates", "A")
    add("c15", "A10 外发模板 claims 字段行内容改『无』",
        lambda t: mut_sub(t, "- `claims`：", "- `claims`：无。原说明作废。\n- 原说明："), None, "A")
    add("c16", "A11 删模板填写说明整节",
        lambda t: t.split("## 填写说明")[0], None, "A")
    add("c22", "A12 删 20-mapping §3 聚合整节",
        lambda t: mut_del(t, ("region", "## 3. 交付汇总聚合字段（七桶＋分母，互斥且完备）")), None, "A")
    add("c18", "A13 来源档出处列全改『—』",
        lambda t: "\n".join(
            ("| " + " | ".join(split_row(l)[:3] + ["—", split_row(l)[4]]) + " |")
            if l.strip().startswith("|") and len(split_row(l)) == 5 and split_row(l)[0].isdigit() else l
            for l in t.replace("\r\n", "\n").split("\n")), None, "A")
    add("c05", "A14 approver 行闭集删 system",
        lambda t: mut_sub(t, "`<approver-kind>:<ref>` 或 `none`；`approver-kind` ∈ `human` / `seat` / `system`", "`<approver-kind>:<ref>` 或 `none`；`approver-kind` ∈ `human` / `seat`"), None, "A")
    add("c04", "A15 description 换纯词堆＋删 Do NOT use for",
        lambda t: re.sub(r"^description:.*$", "description: 一个技能。适用场景：来源层、来源权威、证据标签、事实、推断、判断、未知、过期、假设冻结、异议窗、默认认可、Mock、占位、降级、豁免、验证等级、QA 判词、外发授权、claim、outbound。", t, count=1, flags=re.M), None, "A")
    add("c15", "A16 外发模板 claims 语义改『必须等于全集』",
        lambda t: mut_sub(t, "必须是主张登记表的真子集或全集", "必须是主张登记表的全集"), None, "A")
    add("c15", "A17 §6 claims 格值改『无』",
        lambda t: mut_sub(t, "| `claims` | 本件引用主张的 `claim_id` 闭集列表；允许是主登记表的真子集，不得含未登记或 `superseded` 的 ID |", "| `claims` | 无 |"), None, "A")
    add("c16", "A18 表 A 示例行整行掏空",
        lambda t: re.sub(r"^\| C-001 \|.*$", "| " + " | ".join([""] * 20) + " |", t, count=1, flags=re.M), None, "A")
    add("c15", "A19 删外发模板正文回指规则",
        lambda t: mut_sub(t, "正文每条承重主张必须能回指第 2 节表内某个 `claim_id`；表外主张不得出现在正文承重句内。", "正文自由书写，不要求回指。"), None, "A")
    add("c17", "A20 删 §10 deep-research 映射整节",
        lambda t: mut_del(t, ("region", "## 10. deep-research 证据标签消费映射")), None, "A")
    add("c20", "A21 删『时点』抽取模式整行",
        lambda t: re.sub(r"^\| 时点 \|.*$", "", t, count=1, flags=re.M), None, "A")
    add("c17", "A22 强断言词表由 8 词删至 1 词",
        lambda t: mut_sub(t, "| 强断言 | `必须` / `一律` / `全部` / `绝不` / `保证` / `确保` / `均已` / `全覆盖` |", "| 强断言 | `必须` |"), None, "A")
    add("c17", "A23 占位词表删 `〔`",
        lambda t: mut_sub(t, "/ `placeholder` / `〔` |", "/ `placeholder` |"), None, "A")

    # B. 对方席（产品席）复刻 8 条
    add("c10", "S1 §7 追加『紧急情况可临时代行』",
        lambda t: mut_sub(t, "7. `evidence_tag` 为 `UNKNOWN` 或 `STALE` 时，`status` 不得为 `accepted`",
                          "7. 紧急情况可临时代行，`evidence_tag` 为 `UNKNOWN` 或 `STALE` 时，`status` 不得为 `accepted`"), "contract", "B")
    add("c04", "S2 description 触发词后追加『普通工作票、代码提交、排版』",
        lambda t: re.sub(r"^(description: .*?)(\n)", r"\1普通工作票、代码提交、排版时同样适用。\2", t, count=1, flags=re.M), "skill", "B")
    add("c11", "S3 §8 第 7 类『默认一律不算』→『默认视为认可』",
        lambda t: mut_sub(t, "7. 是否将沉默视为认可；默认一律不算。", "7. 是否将沉默视为认可；默认视为认可。"), "contract", "B")
    add("c07", "S4 §3 环境轴序位整体倒转",
        lambda t: mut_sub(t, "`mock` = 1 ＜ `test` = 2 ＜ `integration` = 3 ＜ `production` = 4", "`mock` = 4 ＞ `test` = 3 ＞ `integration` = 2 ＞ `production` = 1"), "contract", "B")
    add("c12", "S5 §9 第 5 条『不得自动发送』→『可自动发送，无需人类闸』",
        lambda t: mut_sub(t, "5. 不得自动发送任何外发件。", "5. 可自动发送任何外发件，无需人类闸。"), "contract", "B")
    add("c15", "S6 §6 fact_review『不得等于 generated_by』→『可以等于』",
        lambda t: mut_sub(t, "| `fact_review` | `<结论>@<reviewer>`；`reviewer` 不得等于 `generated_by` |", "| `fact_review` | `<结论>@<reviewer>`；`reviewer` 可以等于 `generated_by` |"), "contract", "B")
    add("c07", "S7 表 D『只由 QA 填』→『需求方可代填』",
        lambda t: mut_sub_all_rows(t, 4, "## 3. 主张级验证登记（表 D）", 2, "只由 QA 填", "需求方可代填"), "contract", "B")
    add("c08", "S8 『矩阵外一律违例』→『可默认放行』",
        lambda t: mut_sub(t, "**未在矩阵中出现的组合一律判违例**，不做默认放行。", "**未在矩阵中出现的组合可默认放行**，不必逐条判定。"), "contract", "B")

    # C. 对方席定向反转 2 条
    add("c18", "R18 条目 20 档位『本地约定』改『业界出处』（档位翻转）",
        lambda t: mut_sub(t, "| 20 | 内外防火墙：内部接受不等于外部确认 | 本地约定 |", "| 20 | 内外防火墙：内部接受不等于外部确认 | 业界出处 |"), "prov", "C")
    add("c16", "R16 表 D 示例 qa_result 与 actual_environment 值互换（主体互换）",
        lambda t: mut_sub(t, "| integration | functional;security | none | integration | functional;security | passed_at_actual |",
                          "| integration | functional;security | none | passed_at_actual | functional;security | integration |"), "reg", "C")

    # D. v4 新增定向 6 条（裁定七自证 ＋ 裁定九实测复现 ＋ 裁定十反证）
    add("c18", "D01 条目 9 条款正文改跨包指针（重回指针套指针）",
        lambda t: mut_sub(t, "条款正文：10-contract.md §2 | `四件套承接条款`", "条款正文：external-advisor-collab §谁主张谁举证 | `四件套承接条款`"), "prov", "D")
    add("c18", "D02 条目 10 条款正文由 §1 改回 §2（节在但无该内容）",
        lambda t: mut_sub(t, "条款正文：10-contract.md §1 | `technical_design`", "条款正文：10-contract.md §10 | `technical_design`"), "prov", "D")
    add("c19", "D03 依赖记号钉回版本号（管制十反证）",
        lambda t: mut_sub(t, "| `bundle:object-audit` | 审计判据与发布闸", "| `bundle:object-audit@v1.0.0` | 审计判据与发布闸"), "gates", "D")
    add("c22", "D04 判定序第 4 步（not_required）挪回第 7 步",
        lambda t: mut_sub(t, "4. `required_environment = none` → 计入 `not_required`（**本步必须先于第 5／6 步**：未提出要求环境的主张不参与环境实况分桶，故即便 `actual_environment` 落了 `mock`／`test`／`integration` 也不得记入 `mock_only`）。",
                          "7. 其余 → 计入 `not_required`。"), "mapping", "D")
    add("c16", "D05 表 A 示例 authority consultative→binding（违反 R7 条件格）",
        lambda t: mut_sub(t, "| consultative | draft |", "| binding | draft |"), "reg", "D")
    add("c11", "D06 把 §8 第 3 类整行复制进 40-provenance-map（跨文件原文复制）",
        lambda t: mut_sub(t, "| 18 | 人工闸七类与「沉默默认不算」 |",
                          "3. 需求降级或豁免的批准。\n| 18 | 人工闸七类与「沉默默认不算」 |"), "prov", "D")

    # E. v5 新增定向 10 条（治红4-01／红4-02／红4-03／红4-05 的反证）
    add("c14", "D07 §4 元规则放宽为『任一判据变红即可』（保住 229 条的机制自身失守）",
        lambda t: mut_sub(t, "；由别的判据顺带命中不算通过（那叫假阴）。",
                          "；由别的判据顺带命中同样算通过。"), "gates", "E")
    add("c28", "D08 条款名回退为他包包内文件名『notes-format 条款「标签分级」』",
        lambda t: mut_sub(t, "（包内 `SKILL.md §六 证据纪律`「标签闭集（五标·英文）／措辞分级」）",
                          "（包内 notes-format 条款「标签分级」）"), "gates", "E")
    add("c26", "D09 §11『编号两分发放』反转为『编号全部自造』（造号自证失守·锚随 M-4 改后正文重设）",
        lambda t: mut_sub(t, "**编号两分发放**：**来源面／跨包编号**",
                          "**编号全部自造发放**：**来源面／跨包编号**"), "contract", "E")
    add("c27", "D10 总则 4 反转为『内部接受早已等于外部确认』",
        lambda t: mut_sub(t, "4. 内部接受不等于外部确认。",
                          "4. 内部接受早就等于外部确认。"), "skill", "E")
    add("c27", "D11 总则 10 反转为『状态可增可改，历史可回写』",
        lambda t: mut_sub(t, "10. 状态只增不改，历史不回写。",
                          "10. 状态可增可改，历史可回写。"), "skill", "E")
    add("c27", "D12 总则 7 反转为『审查人必须是生成方』",
        lambda t: mut_sub(t, "审查人不得为生成方", "审查人必须是生成方"), "skill", "E")
    add("c17", "D14 §10 真名改回错名（notes-format 条款「标签分级」）→ c17 必红",
        lambda t: mut_sub(t, "标签本体与措辞分级以 `bundle:deep-research` 包 `SKILL.md §六 证据纪律` 的「标签闭集（五标·英文）」（`:61`）与「措辞分级」（`:63`）为真源，细则见同包 `methodology.md:52`",
                          "标签本体与措辞分级以 deep-research 包 notes-format 条款「标签分级」为真源"), "contract", "E")
    add("c26", "D15 自由描述 basis ＋ authority=binding（正向条件被破，必须红）",
        lambda t: mut_sub(t, "| customer_request | INFERENCE | consultative | draft | none | org:requesting-unit | org:delivery-unit | seat:decision-seat | authorization:DEC-001 |",
                          "| customer_request | INFERENCE | binding | draft | none | org:requesting-unit | org:delivery-unit | seat:decision-seat | 客户口头授权（未编号） |"), "reg", "E")
    add("c26", "D16 旧闭集形态填未登记前缀（自造编号，必须红）",
        lambda t: mut_sub(t, "| seat:decision-seat | authorization:DEC-001 |", "| seat:decision-seat | source:XYZ-001 |"), "reg", "E")
    add("c26", "D13 表 A 示例行在内部假设层硬编责任主体（basis 掏空）",
        lambda t: mut_sub(t, "| customer_request | INFERENCE | consultative | draft | none | org:requesting-unit | org:delivery-unit | seat:decision-seat | authorization:DEC-001 |",
                          "| internal_assumption | INFERENCE | consultative | draft | none | org:requesting-unit | org:delivery-unit | seat:decision-seat | none |"), "reg", "E")
    return M


def run_check(cid, pkg):
    for c, t, fn in CHECKS:
        if c == cid:
            return fn(pkg)
    raise Red("未知检查号 " + cid)


def _collect_muts():
    muts = []
    for item in build_mutations():
        cid, name, fn, key, group = item
        muts.append((cid, name, key, fn, group))
    for e in EXPECT_TARGETS:
        muts.append((e["check"], "OP-del %s 删值" % e["id"], e["key"], (lambda t, e=e: mut_del(t, e["loc"])), "OP"))
        muts.append((e["check"], "OP-rev %s 等长反义" % e["id"], e["key"], (lambda t, e=e: mut_rev(t, e["loc"])), "OP"))
        muts.append((e["check"], "OP-pad %s 加噪" % e["id"], e["key"], (lambda t, e=e: mut_pad(t, e["loc"])), "OP"))
    return muts


def run_mutations(pkg):
    base = os.path.abspath(pkg)
    bitten = []
    fake = []
    mfail = []
    per = {}

    def bump(cid, kind):
        per.setdefault(cid, {"bite": 0, "miss": 0, "fail": 0})[kind] += 1

    # 结构面（文件级）
    for cid, name, fn in PKG_MUT:
        tmp = tempfile.mkdtemp(prefix="semgov-x-")
        dst = os.path.join(tmp, os.path.basename(base))
        shutil.copytree(base, dst)
        try:
            try:
                fn(dst)
            except MutateFailed as exc:
                mfail.append((cid, name, "MUTATE_FAILED " + str(exc)))
                bump(cid, "fail")
                continue
            try:
                out = run_check(cid, dst)
                fake.append((cid, name, "假通过（变异已生效但仍报 %s）" % out))
                bump(cid, "miss")
            except Red as exc:
                print("BITE %-4s %-56s -> %s" % (cid, name, str(exc)[:80]))
                bitten.append((cid, name))
                bump(cid, "bite")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    # 内容面
    muts = _collect_muts()
    for cid, name, key, fn, group in muts:
        done = False
        for rel in ([KEY_INV[key]] if key else FILES):
            src = os.path.join(base, rel)
            with open(src, encoding="utf-8") as f:
                orig = f.read()
            try:
                new = fn(orig)
            except NotHere:
                continue
            except MutateFailed as exc:
                mfail.append((cid, name, "MUTATE_FAILED " + str(exc)))
                bump(cid, "fail")
                done = True
                break
            except Red as exc:
                mfail.append((cid, name, "MUTATE_FAILED 变异器抛红：" + str(exc)))
                bump(cid, "fail")
                done = True
                break
            if new == orig:
                # 锚在本文件未命中（变异器对该文件不适用）——换下一个文件试
                continue
            tmp = tempfile.mkdtemp(prefix="semgov-m-")
            dst = os.path.join(tmp, os.path.basename(base))
            shutil.copytree(base, dst)
            with open(os.path.join(dst, rel), "w", encoding="utf-8", newline="\n") as f:
                f.write(new)
            try:
                try:
                    out = run_check(cid, dst)
                    fake.append((cid, name, "假通过（变异已生效但仍报 %s）" % out))
                    bump(cid, "miss")
                except Red as exc:
                    print("BITE %-4s %-56s -> %s" % (cid, name, str(exc)[:80]))
                    bitten.append((cid, name))
                    bump(cid, "bite")
            finally:
                shutil.rmtree(tmp, ignore_errors=True)
            done = True
            break
        if not done:
            mfail.append((cid, name, "MUTATE_FAILED 锚在本包任一文件均不存在"))
            bump(cid, "fail")

    print("")
    for cid, name, why in mfail:
        print("!! %-4s %-56s -> %s" % (cid, name, why))
    for cid, name, why in fake:
        print("?? %-4s %-56s -> %s" % (cid, name, why))
    total = len(PKG_MUT) + len(muts)
    print("变异体合计 %d 条（结构面 %d ＋ 内容面 %d）" % (total, len(PKG_MUT), len(muts)))
    print("  咬住 %d 条 / 假通过 %d 条 / MUTATE_FAILED %d 条" % (len(bitten), len(fake), len(mfail)))
    ids = sorted(per)
    print("逐判据覆盖：" + " ".join("%s=%d/%d" % (c, per[c]["bite"], per[c]["bite"] + per[c]["miss"] + per[c]["fail"]) for c in ids))
    covered = [c for c in ids if per[c]["bite"] > 0 and per[c]["miss"] == 0 and per[c]["fail"] == 0]
    miss = [c for c, _t, _f in CHECKS if c not in covered]
    if miss:
        print("未获有效覆盖的判据（须有咬住且零假通过零失败）：" + " ".join(miss))
    ok = (not mfail) and (not fake) and (not miss)
    print("判定：%s" % ("全绿（%d 条全咬、零假通过、零失败、覆盖 %d/%d）" % (len(bitten), len(covered), len(CHECKS)) if ok else "不通过"))
    return 0 if ok else 1


def selfcheck(pkg):
    """裁定七：夹具自证。锚唯一性 + 正则命中数 + 源码转义体检 + 形态自洽。"""
    bad = 0
    print("== 1) 变异锚唯一性（每个靶点的 loc 在其目标文件命中恰 1 次）==")
    n_anchor = 0
    for e in EXPECT_TARGETS:
        try:
            txt = read(pkg, e["file"])
            lines = txt.replace("\r\n", "\n").split("\n")
            i = _loc_index(lines, e["loc"][0], e["loc"][1])
            assert i >= 0
            n_anchor += 1
        except (NotHere, MutateFailed, Red) as exc:
            bad += 1
            print("!! 靶点 %s 锚不合格：%s" % (e["id"], exc))
    print("   靶点 %d 个，锚唯一命中 %d 个，不合格 %d 个" % (len(EXPECT_TARGETS), n_anchor, bad))

    print("== 2) 正则体检（编译通过 + 在声明探针上命中数符合声明 + 普通票零命中）==")
    regs = [re.compile(p) for _, p in PATTERNS_PAIRS]
    for idx, probe, want in PATTERN_PROBES:
        got = len(regs[idx].findall(probe))
        okk = got == want
        print("   %-12s 探针 %-22r 命中 %d（声明 %d）%s" % (PATTERNS_PAIRS[idx][0], probe, got, want, "OK" if okk else "FAIL"))
        if not okk:
            bad += 1
    plain_hits = 0
    for s in PLAIN_SAMPLES:
        for rgx in regs:
            plain_hits += len(rgx.findall(s))
    print("   普通工作票样句 %d 例 × %d 模式：命中 %d（声明 0）%s" % (len(PLAIN_SAMPLES), len(regs), plain_hits, "OK" if plain_hits == 0 else "FAIL"))
    if plain_hits:
        bad += 1

    print("== 3) 源码转义体检（本夹具源码内不得出现双斜杠转义）==")
    with open(os.path.abspath(__file__), encoding="utf-8") as f:
        own = f.read()
    body = re.sub(r'"""[\s\S]*?"""', "", own, count=1)
    found = []
    for tok in ("/" + "/s", "/" + "/S", "/" + "/d", "/" + "/w", "/" + "/b", "/" + "/D", "/" + "/W"):
        if tok in body:
            found.append(tok)
    print("   双斜杠转义命中 %d 处（声明 0）%s" % (len(found), "OK" if not found else "FAIL " + repr(found)))
    if found:
        bad += 1

    print("== 4) 形态自洽（不只查缺/多余/非法，还查标签与主操作、主操作与源码特征是否对得上）==")
    cids = [c for c, _t, _f in CHECKS]
    miss_form = [c for c in cids if c not in FORM_REASONS]
    extra_form = [c for c in FORM_REASONS if c not in cids]
    badtag = [c for c in cids if c in FORM_REASONS and FORM_REASONS[c][0] not in FORM_TAGS]
    print("   检查 %d 条；缺形态 %d 条；多余形态 %d 条；非法标签 %d 条" % (len(cids), len(miss_form), len(extra_form), len(badtag)))
    if miss_form or extra_form or badtag:
        bad += 1
    # (a) 六标签齐备且与 FORM_TAGS 全等
    if set(FORM_DEF) != set(FORM_TAGS):
        bad += 1
        print("   !! 定义表标签集合与 FORM_TAGS 不等（%s vs %s）" % (sorted(FORM_DEF), sorted(FORM_TAGS)))
    # (b) 每标签非空，或在 EMPTY_TAG_REASON 登记了零值理由
    dist = {tg: [c for c in cids if FORM_REASONS[c][0] == tg] for tg in FORM_TAGS}
    empty = [tg for tg in FORM_TAGS if not dist[tg]]
    unexplained = [tg for tg in empty if tg not in EMPTY_TAG_REASON]
    print("   非空标签 %d/%d；空桶 %d 个（已登记理由 %d 个）：%s"
          % (len(FORM_TAGS) - len(empty), len(FORM_TAGS), len(empty), len(empty) - len(unexplained),
             " ".join("%s%s" % (tg, "✓" if tg in EMPTY_TAG_REASON else "✗") for tg in empty) or "无"))
    if unexplained:
        bad += 1
    # (c) 主操作 ∈ 该标签允许集
    op_bad = []
    for c in cids:
        tg = FORM_REASONS[c][0]
        op = FORM_OPS.get(c)
        if op is None or op not in FORM_DEF[tg][1]:
            op_bad.append((c, tg, op))
    print("   主操作不合标签允许集 %d 条%s" % (len(op_bad), "" if not op_bad else " " + repr(op_bad)))
    if op_bad:
        bad += 1
    # (d) 源码特征交叉核：主操作必须能在该检查源码里找到对应特征
    SIG = {"摘要等值": ("sha(norm(",), "整串全等": ("!=", "=="), "序列逐项等": ("!=", "=="),
           "集合等": ("set(", "!="), "整名成员": (" in ", "!="), "形态断言": ("re.", "len(", "os.path"),
           "自证断言": ("sha(norm(", "len(")}
    sig_bad = []
    for c, _t, fn in CHECKS:
        op = FORM_OPS.get(c)
        if op is None:
            continue
        try:
            src = inspect.getsource(fn)
        except (OSError, TypeError):
            src = ""
        sigs = SIG.get(op, ())
        if not any(s in src for s in sigs):
            sig_bad.append((c, op))
    print("   主操作与源码特征不一致 %d 条%s" % (len(sig_bad), "" if not sig_bad else " " + repr(sig_bad)))
    if sig_bad:
        bad += 1

    print("== 5) 变异生成器自洽（每条内容面变异在本包内至少一处可生效）==")
    inert = []
    base = os.path.abspath(pkg)
    for cid, name, key, fn, group in _collect_muts():
        hit = False
        for rel in ([KEY_INV[key]] if key else FILES):
            with open(os.path.join(base, rel), encoding="utf-8") as f:
                orig = f.read()
            try:
                new = fn(orig)
            except (NotHere, MutateFailed, Red):
                continue
            if new != orig:
                hit = True
                break
        if not hit:
            inert.append((cid, name))
    print("   内容面变异 %d 条，可生效 %d 条，失效 %d 条" % (len(_collect_muts()), len(_collect_muts()) - len(inert), len(inert)))
    for cid, name in inert:
        print("   !! 失效：%s %s" % (cid, name))
    if inert:
        bad += 1

    print("== 判定：%s ==" % ("自证全绿" if bad == 0 else "自证不通过（%d 项）" % bad))
    return 0 if bad == 0 else 1


def stats(pkg):
    """裁定六：票面一切数字的唯一来源。逐条给出形态归类依据。"""
    cids = [c for c, _t, _f in CHECKS]
    print("== 检查条数 ==")
    print("  检查总数 %d 条（%s）" % (len(cids), " ".join(cids)))

    print("== 判据形态分布（由 FORM_REASONS 逐条归类，非手写汇总）==")
    counts = {t: [] for t in FORM_TAGS}
    for c in cids:
        tag = FORM_REASONS[c][0]
        counts[tag].append(c)
    for t in FORM_TAGS:
        print("  %-10s %2d 条  %s" % (t, len(counts[t]), " ".join(counts[t]) if counts[t] else "（无）"))
    print("  合计 %d 条；分布之和 %d == 检查数 %d ：%s"
          % (len(cids), sum(len(counts[t]) for t in FORM_TAGS), len(cids),
             "是" if sum(len(counts[t]) for t in FORM_TAGS) == len(cids) else "否"))

    print("== 逐条归类依据 ==")
    for c in cids:
        print("  %-4s %-10s %s" % (c, FORM_REASONS[c][0], FORM_REASONS[c][1]))

    print("== 形态六标签定义表（答黄4-10：第三方可据定义＋主/辅判据独立复算分布）==")
    for tg in FORM_TAGS:
        print("  %-10s 定义：%s" % (tg, FORM_DEF[tg][0]))
        print("  %-10s 允许主操作：%s" % ("", "／".join(sorted(FORM_DEF[tg][1]))))
    for tg in FORM_TAGS:
        if not counts[tg] and tg in EMPTY_TAG_REASON:
            print("  %-10s 零值理由：%s" % (tg, EMPTY_TAG_REASON[tg]))
    print("== 主判据／辅判据分离（主操作逐条；辅判据逐条登记）==")
    for c in cids:
        print("  %-4s 主 %-6s ｜ %s" % (c, FORM_OPS.get(c, "（未填）"), FORM_AUX.get(c, "辅：无")))

    print("== 自检与被测分离（答黄3-12）==")
    selftest = [c for c in cids if FORM_REASONS[c][0] == "selftest"]
    print("  被测判据 %d 条 ＋ 自检 %d 条（%s）＝ %d 条"
          % (len(cids) - len(selftest), len(selftest), " ".join(selftest) if selftest else "无", len(cids)))

    print("== 裁定三口径的三项零计数（源码模式扫描，非语义判定）==")
    len_th = []
    for c, _t, fn in CHECKS:
        try:
            body = inspect.getsource(fn)
        except (OSError, TypeError):
            body = ""
        if re.search(r"len\([^)]*\)\s*(?:>=|<=|>|<)\s*\d", body):
            hit = re.findall(r"len\([^)]*\)\s*(?:>=|<=|>|<)\s*\d\S*", body)
            len_th.append((c, hit))
    print("  含 len(...) 与常数作 >/</>=/<= 比较的检查：%d 条 %s"
          % (len(len_th), " ".join("%s%s" % (c, h) for c, h in len_th)))
    grep_q = [c for c, _t, fn in CHECKS if "grep -q" in inspect.getsource(fn)]
    print("  含 grep -q 子串判定的检查：%d 条 %s" % (len(grep_q), " ".join(grep_q)))
    idseq = [c for c in cids if FORM_REASONS[c][0] == "id_seq"]
    print("  仅比对编号序列、无其它断言的检查：%d 条 %s" % (len(idseq), " ".join(idseq)))

    print("== 变异体构成 ==")
    muts = _collect_muts()
    grp = {}
    for cid, name, key, fn, group in muts:
        grp[group] = grp.get(group, 0) + 1
    print("  结构面（文件级 PKG_MUT）%d 条" % len(PKG_MUT))
    print("  内容面 %d 条，其中：对方席 QA 复刻 A=%d；对方席产品席复刻 B=%d；对方席定向反转 C=%d；v4 新增定向 D=%d；v5 新增定向 E=%d；靶点算子 OP=%d"
          % (len(muts), grp.get("A", 0), grp.get("B", 0), grp.get("C", 0), grp.get("D", 0), grp.get("E", 0), grp.get("OP", 0)))
    parts = sum(grp.values())
    print("  分组之和 %d == 内容面 %d ：%s" % (parts, len(muts), "是" if parts == len(muts) else "否"))
    print("  合计 %d 条" % (len(PKG_MUT) + len(muts)))

    print("== 靶点数 ==")
    print("  靶点 %d 个；REV 对 %d 组" % (len(EXPECT_TARGETS), len(REV_PAIRS)))

    print("== 七件行数 ==")
    tot = 0
    for rel in FILES:
        txt = read(pkg, rel)
        n = len(txt.replace("\r\n", "\n").rstrip("\n").split("\n"))
        tot += n
        print("  %-40s %4d 行" % (rel, n))
    print("  合计 %d 行" % tot)

    print("== 三闸支数 ==")
    print("  正向 3 支（闸一 check-skill-meta／闸二 check-provenance／闸三 check-entity）＋ 反向 %d 支 ＝ %d 支"
          % (len(GATE_REVERSE), 3 + len(GATE_REVERSE)))

    print("== 字段消费方统计（裁定四）==")
    for tag, fields in (("表 A", EXPECT_A_FIELDS), ("表 D", EXPECT_D_FIELDS),
                        ("表 B", EXPECT_B_COLS), ("表 C", EXPECT_C_COLS)):
        n = len(fields)
        consumed = len([f for f in fields if FIELD_CONSUMERS.get(f)])
        print("  %s %d 列：有判据消费 %d，登记面 %d，已删 %d"
              % (tag, n, consumed, n - consumed, len(DELETED_FIELDS.get(tag, []))))
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    if argv[1] == "--list":
        for c, t, _ in CHECKS:
            print("%-4s %s" % (c, t))
        return 0
    if argv[1] == "--all":
        pkg = argv[2]
        bad = 0
        for c, t, fn in CHECKS:
            try:
                msg = fn(pkg)
                print("OK   %-4s %s" % (c, msg))
            except Red as exc:
                bad += 1
                print("FAIL %-4s %s" % (c, exc))
            except (MutateFailed, NotHere) as exc:
                bad += 1
                print("FAIL %-4s 夹具异常：%s" % (c, exc))
        return 0 if bad == 0 else 1
    if argv[1] == "--mutate":
        return run_mutations(argv[2])
    if argv[1] == "--stats":
        return stats(argv[2])
    if argv[1] == "--selfcheck":
        return selfcheck(argv[2])
    if len(argv) < 3:
        print("用法：verify.py <check-id> <pkg-dir>")
        return 2
    try:
        msg = run_check(argv[1], argv[2])
        print("OK   %-4s %s" % (argv[1], msg))
        return 0
    except Red as exc:
        print("FAIL %-4s %s" % (argv[1], exc))
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
