#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fuxi-skill 结构层门禁断言工具（机械断言，不依赖人工校准）。S0a 建骨架，S1 实装共享内核 L0 执行位，S2 实装 adapter 互斥＋FC-5。

断言目录＝同目录 `assertion-catalog.md`（25 项：ST-1..8／BW-1..6／FC-1..6／GS-1..5）。
本件与目录一一对应：每项目录断言有对应函数（当期可执行项＝实装；
〔Sx 执行〕项＝桩＋显式 PENDING_STAGE 读数，不算 fail 不算 pass，汇总单列）。

S1 实装位（共享内核 L0 落盘后）：ST-1／ST-2／ST-5／FC-1／FC-2／FC-3／FC-4。
S2 实装位：ST-6／ST-7（两 adapter 互斥 IR 字段互检）＋FC-5（bundle 两层命名空间互借检出）
    ＋FC-4 黄-2 收口扩展（看板实例正文状态 token 扫描＋AC-5 词表声明句私扩扫描）。
S3 实装位：GS-1／GS-2／GS-3（实装基面＝验证记录目录·`.collab/evidence/harness/` 内
    *.jsonl 全部记录的 所属轨×gate_source 白名单双向 diff，不匹配数＝0 才绿；
    记录目录由两 validator 判分段写出，字段注册表＝`validator-catalog.md` §二）。
    S3 白名单扩值：PERSON_GATE_WHITELIST 扩「格式检查表」六值（门禁面重交付·AC-5 扩词程序同族），
    与 METHOD_GATE_WHITELIST 互斥集合同步维护于本注册位。
S4 实装位：ST-3 转实装（产物实例节结构 diff·active 生效池空扫描合法态＋段名前缀归一化口径）
    ＋新增 ST-8／BW-5／BW-6／FC-6／GS-5（两规范表文件节闭集＋矛盾平滑检出＋README 置顶判据
    ＋active 池人工确认存在＋门禁不退化基线对照）。
S0b 实装位：GS-4 转实装（注册落盘路径内 anchor-tuple*.json 定位；无元组＝PENDING_STAGE
    「S0b 元组未交付」如实态；在场＝逐元组挂接既有纯函数 calibration_consistent() 对账，
    判据本体零改动；κ 达标线常量 KAPPA_THRESHOLD 注册于本件供 s0b-kappa.py import 不复制）。
判据基面（固定路径静态定位，契约与工具互不嵌套）：
    contracts/＝三契约文件（声明面）；rejected/＝淘汰留档区（可枚举基面）；
    adapters/＝两 adapter 件＋分类器件（S2 结构断言基面）；
    specs/＝两输出规范表文件（ST-8 基面）；包 README.md（BW-6 基面）；
    deliverables/products/＝active 生效池注册路径（FC-6 池计数基面＝池根直接条目）；
    产物级扫描面（ST-3／BW-1／BW-2／BW-5(b) 消费）＝池根直接条目＋pending/（待确认暂存区）一层下产物目录，
    两口径分离：暂存区条目入结构检与词表实扫、不计入池计数；archive/＝历史记录区，免产物级机检、不入扫描面。

退出码闭集（三值，无其他取值）：
    0 全绿（无 fail；PENDING_STAGE 不拉码）
    1 有 fail
    2 工具自身错误（用法错／环境错／内部异常，fail-closed 不得吞成 0）

确定性：全部断言为确定性判据——无随机种子、无时钟参与读数、无网络；
同输入连跑两次退出码与逐项读数全等。

用法：
    python assert-tool.py            # 仓内执行模式：跑 25 项，当期实装项出读数，余者 PENDING_STAGE
    python assert-tool.py selftest   # 自证模式：内存构造正负样本，逐类断言「能咬能放」
"""

from __future__ import annotations

import json
import os
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

# 证据分级契约侧值闭集（EG-2／EG-3，与 `evidence_grade` 轴正交）。
EVIDENCE_LEVELS = ("原文可证实", "跨文本推断", "模型补全")
SOURCE_STATES = ("本人原文", "第三方转述", "模型推断")

# AC-3 准入证据卡对照臂栏／泄漏检查栏值闭集。
CONTROL_ARMS = ("三臂", "无臂", "未测")
LEAKAGE_CHECKS = ("已检-不在语料内", "已检-在语料内", "未检")

# AC-1 元数据值闭集（编译形态 B10/R23；所属轨沿用 ST-4 取值风格）。
COMPILE_FORMS = ("single", "pack", "bundle")
SIDE_TRACKS = ("person", "method", "bundle")

# ST-3 perspective 五层节闭集／technique 六段卡＋五字段闭集。
PERSPECTIVE_SECTIONS = ("表达DNA", "心智模型", "决策启发式", "反模式", "诚实边界")
TECHNIQUE_CARD_SECTIONS = ("R", "I", "A1", "A2", "E", "B")
TECHNIQUE_CARD_FIELDS = ("出处", "触发", "步骤", "边界", "验证状态")
# ST-3 段名前缀归一化口径（S4 钉死）：产物节头书写形态＝`<段名> <段描述名>`（如「R 原文」）；
# 机检 diff 基面＝段名前缀 token；描述名不参与段名 diff，但须与注册描述名逐字全等（改名＝咬）；
# 裸段名形态（「R」）与全形态两写法同判合法——杜绝「R」vs「R 原文」两套写法引发的假咬。
TECHNIQUE_SEGMENT_DESCS = ("原文", "诠释", "案例", "触发场景", "执行步骤", "边界")

# ST-8 两规范表文件本体节闭集（恰四节）＋关键引用行在场对象（S4 建）。
SPEC_FOUR_SECTIONS = ("适用范围", "节闭集表", "声明措例", "量纲与机检落点")
SPEC_FILES = ("perspective-spec", "technique-spec")
SPEC_KEY_REFS = {
    "perspective-spec": ("AC-1", "宁可生成一个诚实标注局限的 60 分产物，也不要一个看似完美的 90 分造假产物"),
    "technique-spec": ("AC-2", "VA-S-01"),
}

# BW-5 矛盾平滑检出（S4 建·坏信号④机械位）：(a) person adapter 防编护栏节条款声明行；
# (b) 平滑句式启发式预注册词表本体（随批锁定值；中途变更走门禁面重交付程序，BW-1/BW-2 同制）。
PERSON_CONTRADICTION_DECL_ROWS = ("内部矛盾不平滑", "矛盾是深度的重要信号")
SMOOTH_PHRASE_VOCAB = ("毫无矛盾", "观点完全一致", "前后一贯无张力", "自洽无冲突")

# BW-6 README 相近工具对照表置顶判据（S4 建·§八 命名硬性要求登记位机检化）。
COMPARISON_TABLE_TOOL_NAMES = ("nuwa-skill", "cangjie-skill")
COMPARISON_TABLE_OWN_NAME = "fuxi-skill"
COMPARISON_NO_INHERIT_DECL = "与前序同名旧物无继承关系"
COMPARISON_ROW_NAMES = ("对象", "产物", "验证")

# FC-6 active 生效池（S4 建·R16 验收机检位）：注册路径＋条目确认件四字段闭集。
_PRODUCTS_SUBPATH = ("deliverables", "products")
CONFIRM_FILE_NAME = "confirmation.md"
POOL_CONFIRM_FIELDS = ("产物id", "人工确认引用", "提案件引用", "版本审计引用")

# GS-5 门禁不退化基线（S4 建·坏信号③机械位）：三组注册位对基线只增不减，任一缩水＝咬。
VALIDATOR_LAYER_NAMES = ("机械断言", "三臂对照", "诱饵测试", "留出集", "泄漏检查", "边缘诚实度",
                         "格式检查表", "盲评rubric", "绝对线", "decoy", "人工锚点卡")
GS5_BASELINE = {"层名基数": 11, "person白名单基数": 6, "method白名单基数": 6, "断言编号基数": 25}

# 契约文件节闭集（EG 六节／FM 五节／AC 五节；多节/缺节/改名＝diff 非空即 fail）。
EG_SECTIONS = ("适用范围", "三级标注", "来源三态", "三问可答口径", "候选单元记录", "语料门槛登记")
FM_SECTIONS = ("表结构", "分流语义", "共享条目", "person轨条目", "method轨条目")
AC_SECTIONS = ("产物类型与元数据", "状态字段", "准入证据卡", "声明与措辞纪律", "状态词表与看板")

# ST-4 test-prompts 条目字段闭集。
TEST_PROMPT_FIELDS = ("用例id", "题面", "期望档位", "所属轨", "是否锚点题")

# ST-5 coverage-audit 三问字段。
COVERAGE_AUDIT_FIELDS = ("哪些留下", "哪些扔了", "为什么")

# FC-2 交付面字段名注册表（S1 扩充＝既有 4＋新增清单；未注册字段零容忍，双向 diff＝∅ 防私扩）。
KERNEL_FIELD_REGISTRY = (
    # 既有（S0a 基线）
    "evidence_grade", "calibration_state", "source_id", "位置",
    # 新增（证据/候选单元）
    "证据等级", "来源态", "所属轨", "candidate_id", "abstain_tier",
    # 新增（证据卡）
    "control_arm", "leakage_check",
    # 新增（产物元数据）
    "产物id", "编译形态", "快照时戳", "版本号", "复审到期日",
    # 新增（留档条目）
    "淘汰维度", "淘汰理由",
    # 新增（门槛登记）
    "一手占比门槛", "新鲜度窗口月数", "一手占比",
    # 新增（failure-modes 条目字段）
    "编号", "轨别", "触发", "检出", "处置",
)

# FC-4 状态词表取值闭集＋看板三栏字段名闭集。
STATE_WORDS = ("needs_review", "active", "归档区", "待校准", "未验", "受限")
BOARD_COLUMNS = ("本轮改动", "触发的坏信号", "人工闸结论")
BOARD_HEADER_DECL = "性质＝记录件·人工触发填写·非控制器"
BOARD_PERIOD_MAX_DAYS = 14  # 相邻板文件名日期间隔上限（周期兜底，AC-5 定稿值）
# 黄-2 收口（S2）：状态 token 扫描两扫描位——①看板正文含「状态」关键词行的反引号 token；
# ②契约 AC-5 词表声明句（含「基线闭集」短语行）反引号 token。两路 token 均须 ⊆ 状态词表闭集。
BOARD_STATE_LINE_KEY = "状态"
VOCAB_LINE_KEY = "基线闭集"

# ST-6／ST-7（S2 建）：两 adapter 互斥 IR 字段互检——
# person.md 禁 technique 轨 IR 段名字样；method.md 禁 persona 轨 IR 节名字样。
PERSON_FORBIDDEN_IR_TERMS = ("执行步骤",)
METHOD_FORBIDDEN_IR_TERMS = ("表达DNA", "表达 DNA")

# GS-1/GS-2 gate_source 白名单（person 软门类／method 硬门类；互斥＝双向断言基面）。
# S3 扩值（扩值依据与审计轨迹见版本受控记录与断言目录修订注记·门禁面重交付程序＝AC-5 扩词程序同族）：person 白名单六值，
# 增「格式检查表」＝D2 嫁接机械层唯一合法记账词，与 method 白名单「机械断言」刻意异名
# （异名即 B3 不互套的词表体现）。
# method 白名单随 D3 嫁接层同步补齐＝六值（层名即 gate_source 注册词：泄漏检查／边缘诚实度
# 入 method 侧记账；「泄漏检查」为两轨共有的确定性判据词，两轨各自在场不违互斥——互斥性
# 由专属词承载：机械断言/三臂对照/诱饵测试/留出集/边缘诚实度 入 person 记录必咬，
# 盲评rubric/绝对线/decoy/人工锚点卡/格式检查表 入 method 记录必咬）。
PERSON_GATE_WHITELIST = ("盲评rubric", "绝对线", "decoy", "泄漏检查", "人工锚点卡", "格式检查表")
METHOD_GATE_WHITELIST = ("机械断言", "三臂对照", "诱饵测试", "留出集", "泄漏检查", "边缘诚实度")

# 验证记录落盘路径注册（validator-catalog 顶部注册同源：过程域证据子域；
# 路径拼接行＝FC-4 看板路径同款代码位，非文档过程域指针）
_HARNESS_SUBPATH = (".collab", "evidence", "harness")

# 共享内核三文件名（ST-2 对象；S1 落点＝contracts/ 子目录）。
KERNEL_THREE_FILES = ("evidence-grading", "failure-modes", "artifact-contract")

# S2 adapter 面三文件名（ST-6／ST-7 对象；落点＝adapters/ 子目录）。
ADAPTER_FILES = ("person", "method", "classifier")

# FM 条目纪律参数（五元组表结构＋分流语义）。
FM_PREFIX_TRACK = {"S": "共享", "P": "person", "M": "method"}
FM_BASELINE_COUNTS = {"S": 5, "P": 4, "M": 3}
FM_UNCERTAIN_WORDS = ("视情况", "酌情", "后续再定")
FM_ACTION_WORDS = ("降级", "阻断", "转人工闸")

# 契约声明值 ↔ 工具注册值 互洽对照（FC-1 类双向 diff 对象；逐字全等才算过）。
VALUE_REGISTRIES = {
    "evidence_grade": EVIDENCE_GRADES,
    "calibration_state": CALIBRATION_STATES,
    "证据等级": EVIDENCE_LEVELS,
    "来源态": SOURCE_STATES,
    "control_arm": CONTROL_ARMS,
    "leakage_check": LEAKAGE_CHECKS,
    "abstain_tier": ABSTAIN_TIERS,
    "编译形态": COMPILE_FORMS,
    "所属轨": SIDE_TRACKS,
}

# 三问必答字段（EG-4：证据等级双轴＋对照臂＋泄漏检查）。
THREE_QUESTION_FIELDS = ("证据等级", "evidence_grade", "control_arm", "leakage_check")
# 淘汰条目三问字段（§2.2：继承 EG-4 之 `证据等级` 单轴＋对照臂＋泄漏检查）。
ENTRY_QUESTION_FIELDS = ("证据等级", "control_arm", "leakage_check")

_JSON_FENCE_RE = re.compile(r"```json[ \t]*\n(.*?)\n```", re.S)
_SECTION_RE = re.compile(r"^##\s+(EG|FM|AC)-\d+\s+(.+?)\s*$", re.M)
_H2_SEC_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)
# ST-3 段头形态（归一化口径）：`<段名> [<段描述名>]`（裸段名与全形态两写法同判合法）。
_SEG_HEAD_RE = re.compile(r"^([RIAB][12]?|E)(?:\s+(\S.*?))?\s*$")
_PRODUCT_DIR_SUFFIXES = ("-perspective", "-technique", "-bundle")
_PRODUCT_BODY_FILE = "SKILL.md"   # 产物本体件名：节结构 diff 只消费本体件（随件入词表面不入节 diff 面）
_TEST_PROMPTS_FILE = "test-prompts.md"  # 产物随件回归资产件名（ST-4 消费位·T5 建）
_PENDING_SUBDIR = "pending"       # 生效池根下待确认暂存区子目录（产物级扫描面扩一层；条目不计池计数）
_FM_ROW_RE = re.compile(r"^FM-[SPM]-\d{2}$")
_BOARD_NAME_RE = re.compile(r"^board-(\d{4})-(\d{2})-(\d{2})\.md$")
_BACKTICK_TOKEN_RE = re.compile(r"`([^`\n]+)`")

_PERCENT_RE = re.compile(r"\d+(?:\.\d+)?\s*%")
_NUMBER_METRIC_RE = re.compile(r"(?:通过率|一致率|占比)[^\d]{0,8}\d+(?:\.\d+)?")

# 判据基面路径（自工具文件位置静态定位，契约与工具互不嵌套）。
_SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CONTRACTS_DIR = os.path.join(_SKILL_ROOT, "contracts")
_REJECTED_DIR = os.path.join(_SKILL_ROOT, "rejected")


def _read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="replace", newline="") as handle:
        return handle.read().replace("\r\n", "\n")


def md_json_blocks(text: str) -> "tuple[list[dict], int]":
    """提取 markdown 内 fenced json 块：返回 (解析成功块列表, 解析失败数)。"""
    blocks: "list[dict]" = []
    bad = 0
    for raw in _JSON_FENCE_RE.findall(text):
        try:
            parsed = json.loads(raw)
        except ValueError:
            bad += 1
            continue
        if isinstance(parsed, dict):
            blocks.append(parsed)
    return blocks, bad


def md_sections(text: str) -> "list[str]":
    """提取契约文件一级节名（`## EG-n 节名` 形态的节名部分）。"""
    return [m.group(2) for m in _SECTION_RE.finditer(text)]


def declared_field_names(blocks: "list[dict]") -> "set[str]":
    """json 块面的声明字段名集合：字段注册表＋值注册键（实例记录键交实例侧判据，不并入声明面）。"""
    names: "set[str]" = set()
    for block in blocks:
        decl = block.get("字段注册")
        if isinstance(decl, list):
            names.update(str(n) for n in decl)
        vals = block.get("值注册")
        if isinstance(vals, dict):
            names.update(str(k) for k in vals)
    return names


def value_decl_diff(blocks: "list[dict]", registries: "dict[str, tuple[str, ...]]") -> "list[str]":
    """契约声明值 ↔ 工具注册值 diff：逐字段并集与注册元组逐字全等才算过。"""
    problems: "list[str]" = []
    merged: "dict[str, set]" = {}
    for block in blocks:
        vals = block.get("值注册")
        if not isinstance(vals, dict):
            continue
        for field, allowed in vals.items():
            if isinstance(allowed, list):
                merged.setdefault(str(field), set()).update(str(v) for v in allowed)
    for field, registry in registries.items():
        want = set(registry)
        got = merged.get(field, set())
        extra = got - want
        missing = want - got
        if extra or missing:
            problems.append("%s 多出%s 缺失%s" % (field, sorted(extra) or "∅", sorted(missing) or "∅"))
    return problems


def three_question_ok(record: "dict") -> bool:
    """三问可答判据：证据等级双轴＋对照臂＋泄漏检查四字段在场非空。"""
    return all(str(record.get(k, "")).strip() for k in THREE_QUESTION_FIELDS)


def entry_question_ok(record: "dict") -> bool:
    """淘汰条目三问判据：`证据等级`／`control_arm`／`leakage_check` 在场非空。"""
    return all(str(record.get(k, "")).strip() for k in ENTRY_QUESTION_FIELDS)


def audit_fields_ok(blocks: "list[dict]") -> bool:
    """coverage-audit 三问字段：每字段在某 json 块中取值非空字符串。"""
    for field in COVERAGE_AUDIT_FIELDS:
        if not any(isinstance(b.get(field), str) and b[field].strip() for b in blocks):
            return False
    return True


def fm_entries_from_text(text: str) -> "list[list[str]]":
    """从 failure-modes 契约文本抽 FM 条目行（五元组：编号/轨别/触发/检出/处置）。"""
    entries: "list[list[str]]" = []
    for raw in text.split("\n"):
        line = raw.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells and cells[0] and _FM_ROW_RE.match(cells[0]):
            entries.append(cells)
    return entries


def fm_entries_discipline(entries: "list[list[str]]") -> "list[str]":
    """FM 条目纪律（五元组非空＋分流语义＋轨别/前缀匹配＋数量基线）：返回问题列表（空＝放）。"""
    problems: "list[str]" = []
    counts: "dict[str, int]" = {"S": 0, "P": 0, "M": 0}
    seen_ids: "set[str]" = set()
    for cells in entries:
        if len(cells) != 5:
            problems.append("%s 五元组列数=%d（应5）" % (cells[0] if cells else "?", len(cells)))
            continue
        fid, track, trigger, detect, action = cells
        prefix = fid[3] if fid.startswith("FM-") else "?"
        if prefix not in FM_PREFIX_TRACK:
            problems.append("%s 编号前缀不合法" % fid)
            continue
        if fid in seen_ids:
            problems.append("%s 编号重复" % fid)
        seen_ids.add(fid)
        counts[prefix] += 1
        if not all(c.strip() for c in cells):
            problems.append("%s 五元组有空列" % fid)
        if track != FM_PREFIX_TRACK[prefix]:
            problems.append("%s 轨别%s与前缀不匹配" % (fid, track))
        if any(w in action for w in FM_UNCERTAIN_WORDS):
            problems.append("%s 处置含不确定措辞（无逃逸路径违例）" % fid)
        if not any(w in action for w in FM_ACTION_WORDS):
            problems.append("%s 处置缺三态词（降级/阻断/转人工闸）" % fid)
    for prefix, want in FM_BASELINE_COUNTS.items():
        if counts[prefix] < want:
            problems.append("FM-%s 条目数%d＜基线%d" % (prefix, counts[prefix], want))
    return problems


def board_files_ok(board_dir: str) -> "tuple[bool, str]":
    """看板实例判据（在场才检）：性质声明行＋三栏标题＋相邻板日期间隔 ≤14 天。"""
    if not os.path.isdir(board_dir):
        return (True, "看板实例不在场（合法）")
    names = sorted(n for n in os.listdir(board_dir) if _BOARD_NAME_RE.match(n))
    if not names:
        return (True, "看板目录空（合法）")
    for name in names:
        text = _read_text(os.path.join(board_dir, name))
        head = "\n".join(text.split("\n")[:15])
        if BOARD_HEADER_DECL not in head:
            return (False, "%s 缺性质声明行（记录件非控制器）" % name)
        missing_cols = [c for c in BOARD_COLUMNS if ("## " + c) not in text]
        if missing_cols:
            return (False, "%s 缺三栏标题%s" % (name, "、".join(missing_cols)))
    days: "list[int]" = []
    for name in names:
        m = _BOARD_NAME_RE.match(name)
        y, mo, d = (int(g) for g in m.groups())
        days.append(y * 372 + mo * 31 + d)  # 单调日期键（确定性，无时钟参与读数）
    for a, b in zip(days, days[1:]):
        if b - a > BOARD_PERIOD_MAX_DAYS:
            return (False, "相邻板日期间隔超限（>%d 天）" % BOARD_PERIOD_MAX_DAYS)
    return (True, "看板实例 %d 份判绿" % len(names))


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


def test_prompt_values_ok(entries: "list[dict[str, str]]") -> bool:
    """ST-4 条目取值闭集（T5 建）：`期望档位` ∈ ABSTAIN_TIERS、`所属轨` ∈ SIDE_TRACKS（字段缺省不在此咬，归字段面判据）。"""
    registry = {"期望档位": ABSTAIN_TIERS, "所属轨": SIDE_TRACKS}
    for entry in entries:
        for field, allowed in registry.items():
            if field in entry and str(entry[field]) not in allowed:
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


def kernel_field_diff(declared: "set[str]", registry: "tuple[str, ...]",
                      vocab_extra: "tuple[str, ...]" = ()) -> "tuple[set, set]":
    """FC-2 双向字段 diff：返回 (声明侧未注册多出集, 注册表未声明缺失集)；两集皆空＝diff＝∅。

    vocab_extra＝已在别处注册的字段名（ST-5 coverage-audit 三问），计入已注册面防误判多出。
    """
    allowed = set(registry) | set(vocab_extra)
    return (declared - allowed, allowed - declared)


def paired_fields_ok(records: "list[dict[str, str]]") -> bool:
    """FC-3 source_id＋位置双形态成对：任一侧出现则另一侧必须在场。"""
    for rec in records:
        has_id = bool(rec.get("source_id", "").strip())
        has_loc = bool(rec.get("位置", "").strip())
        if has_id != has_loc:
            return False
    return True


def product_element_pair_hits(entry_texts: "dict[str, dict[str, str]]") -> "tuple[list[str], int]":
    """FC-3 产物要素行级成对检（T5 建·行级判据·确定性）。

    逐条目本体件（`_PRODUCT_BODY_FILE`）逐行扫描：行内同时含 `` `证据等级` ``＋`` `来源态` ``
    两个反引号闭集字段名 token＝要素标注行；要素标注行须同时含子串 `source_id` 与子串 `位置`，
    只有其一＝不成对＝命中（逐行列明细）。返回 (命中列表, 要素行数)；无要素行＝空扫描合法态。
    模型推断态哨兵取值（EG-3）形式满足本判据（哨兵值含两子串即成对）。
    """
    hits: "list[str]" = []
    marked = 0
    for name in sorted(entry_texts):
        for fname in sorted(entry_texts[name]):
            if fname != _PRODUCT_BODY_FILE:
                continue
            for lineno, line in enumerate(entry_texts[name][fname].split("\n"), 1):
                if "`证据等级`" not in line or "`来源态`" not in line:
                    continue
                marked += 1
                has_id = "source_id" in line
                has_loc = "位置" in line
                if has_id != has_loc:
                    missing = "位置" if has_id else "source_id"
                    hits.append("%s/%s line%d 不成对（缺%s）" % (name, fname, lineno, missing))
    return hits, marked


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


def bundle_layers(record: "dict") -> "bool":
    """bundle 实例记录识别：json 块顶层同时含 persona／technique 两键＝bundle 两层实例。"""
    return "persona" in record and "technique" in record


def state_token_scan(text: str, line_key: str, allowed: "tuple[str, ...]", exact: bool) -> "list[str]":
    """黄-2 收口（S2）：状态 token 扫描（确定性行粒度）。

    只扫含 line_key 关键词的行，取行内反引号 token（路径形态 token——含
    `/`、`\\`、`:` 或 `.md`/`.py` 后缀者＝指针非状态词，不入扫描）：
    - exact=False（看板正文侧）：token 须 ⊆ 状态词表 ∪ 字段注册表 ∪ 看板三栏名（豁免面），
      越集 token＝词表私扩，逐行检出。
    - exact=True（契约词表声明句侧）：token 集合须与状态词表全集逐字全等（多一值少一值都检出）。
    """
    allowed_set = set(allowed)
    exempt = allowed_set | set(KERNEL_FIELD_REGISTRY) | set(BOARD_COLUMNS)
    hits: "list[str]" = []
    for lineno, line in enumerate(text.split("\n"), 1):
        if line_key not in line:
            continue
        tokens = {t for t in _BACKTICK_TOKEN_RE.findall(line)
                  if not any(ch in t for ch in "/\\:") and not t.endswith((".md", ".py"))}
        if not tokens:
            continue
        if exact:
            extra = tokens - allowed_set
            missing = allowed_set - tokens
            if extra or missing:
                hits.append("line%d 词表句 diff 多出%s 缺失%s"
                            % (lineno, sorted(extra) or "∅", sorted(missing) or "∅"))
        else:
            extra = tokens - exempt
            if extra:
                hits.append("line%d 状态token越词表%s" % (lineno, sorted(extra)))
    return hits


def ir_term_hits(text: str, forbidden: "tuple[str, ...]") -> "list[str]":
    """ST-6／ST-7 互斥 IR 字段字样命中计数（每字样命中数，空列表＝零命中＝放）。"""
    return [t for t in forbidden if t in text]


def gate_source_hits(track: str, gate_source: str) -> "list[str]":
    """GS-1/GS-2 轨白名单命中：返回越轨判据命中列表（空＝放）。

    person 轨禁 method 硬门判据（method 白名单即 person 侧禁区），对称反之。
    """
    if track == "person":
        return [gate_source] if gate_source in METHOD_GATE_WHITELIST and gate_source not in PERSON_GATE_WHITELIST else []
    if track == "method":
        return [gate_source] if gate_source in PERSON_GATE_WHITELIST and gate_source not in METHOD_GATE_WHITELIST else []
    return ["未知轨:%s" % track]


# GS-4 κ 达标线（S0b 建·预注册数值＝validator-catalog §四表 S0b 行「达标线」行同源；
# 消费面 s0b-kappa.py import 本常量不复制——读数面单源在本注册位）。
KAPPA_THRESHOLD = 0.6


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


def _contract_texts() -> "dict[str, str]":
    """读三契约文件＋留档约定件的文本（缺键＝缺文件）。"""
    texts: "dict[str, str]" = {}
    for name in KERNEL_THREE_FILES:
        path = os.path.join(_CONTRACTS_DIR, name + ".md")
        if os.path.isfile(path):
            texts[name] = _read_text(path)
    readme = os.path.join(_REJECTED_DIR, "README.md")
    if os.path.isfile(readme):
        texts["rejected-README"] = _read_text(readme)
    return texts


def _all_blocks(texts: "dict[str, str]") -> "tuple[list[dict], int]":
    blocks: "list[dict]" = []
    bad = 0
    for text in texts.values():
        got, badn = md_json_blocks(text)
        blocks.extend(got)
        bad += badn
    return blocks, bad


def _adapter_texts() -> "dict[str, str]":
    """读 adapters/ 面件文本（S2 结构断言基面；缺键＝缺文件）。"""
    texts: "dict[str, str]" = {}
    adapters_dir = os.path.join(_SKILL_ROOT, "adapters")
    for name in ADAPTER_FILES:
        path = os.path.join(adapters_dir, name + ".md")
        if os.path.isfile(path):
            texts["adapter-" + name] = _read_text(path)
    return texts


def perspective_head_sections(text: str) -> "tuple[str, ...]":
    """ST-3 perspective 侧：抽产物 H2 节名并去空白归一（连写／带空格两形态同判合法）。"""
    return tuple(re.sub(r"\s+", "", m.group(1)) for m in _H2_SEC_RE.finditer(text))


def technique_segment_normalize(heads: "tuple[str, ...]") -> "tuple[set, set, list[str]]":
    """ST-3 technique 侧段名前缀归一化：返回 (多出段名集, 缺失段名集, 非法描述名命中列表)。

    节头两写法同判合法：裸段名「R」／全形态「R 原文」；描述名在场则须与注册描述名逐字全等
    （「R 原文X」改名＝咬）；节头不属段头形态＝非法记入第三集。
    """
    got: "set[str]" = set()
    bad: "list[str]" = []
    for head in heads:
        m = _SEG_HEAD_RE.match(head.strip())
        if not m:
            bad.append(head)
            continue
        seg, desc = m.group(1), (m.group(2) or "").strip()
        got.add(seg)
        if desc and seg in TECHNIQUE_CARD_SECTIONS:
            idx = TECHNIQUE_CARD_SECTIONS.index(seg)
            if desc != TECHNIQUE_SEGMENT_DESCS[idx]:
                bad.append(head)
    return (got - set(TECHNIQUE_CARD_SECTIONS), set(TECHNIQUE_CARD_SECTIONS) - got, bad)


def card_fields_closed_ok(block: "dict") -> bool:
    """ST-3 卡体五字段闭集：json 卡块含任一注册字段则其键集须 ⊆ 五字段闭集。"""
    keys = {str(k) for k in block}
    if not (keys & set(TECHNIQUE_CARD_FIELDS)):
        return True
    return keys <= set(TECHNIQUE_CARD_FIELDS)


def spec_sections(text: str) -> "tuple[str, ...]":
    """ST-8：抽规范表文件本体 H2 节名（四节节闭集对象）。"""
    return tuple(m.group(1) for m in _H2_SEC_RE.finditer(text))


def spec_missing_key_refs(text: str, refs: "tuple[str, ...]") -> "list[str]":
    """ST-8 关键引用行在场：逐引用串扫描，返回缺失列表（空＝放）。"""
    return [r for r in refs if r not in text]


def decl_rows_missing(text: str, rows: "tuple[str, ...]") -> "list[str]":
    """BW-5(a)：条款声明行在场扫描，返回缺失声明行列表（空＝放）。"""
    return [r for r in rows if r not in text]


def readme_table_problems(text: str) -> "list[str]":
    """BW-6 README 置顶判据（纯文本判据）：返回问题列表（空＝放）。

    ①首个二级标题行之前出现的首个 markdown 表格含两对照工具名（本产品线列名另检）；
    ②「无继承关系」声明行命中＝恰 1；③对照表三维度行名齐备。任一违＝问题。
    """
    problems: "list[str]" = []
    lines = text.split("\n")
    h2_idx = next((i for i, ln in enumerate(lines) if ln.startswith("## ")), len(lines))
    table_start = next((i for i, ln in enumerate(lines) if ln.lstrip().startswith("|")), None)
    if table_start is None:
        return ["无 markdown 表格（对照表缺位）"]
    if table_start >= h2_idx:
        problems.append("首个 markdown 表格不在首个二级标题之前（未置顶）")
    table_end = table_start
    while table_end < len(lines) and lines[table_end].lstrip().startswith("|"):
        table_end += 1
    table_lines = lines[table_start:table_end]
    joined = "\n".join(table_lines)
    for name in COMPARISON_TABLE_TOOL_NAMES:
        if name not in joined:
            problems.append("对照表缺工具名 %s" % name)
    if COMPARISON_TABLE_OWN_NAME not in joined:
        problems.append("对照表缺本产品线列名 %s" % COMPARISON_TABLE_OWN_NAME)
    row_first_cells = [ln.strip().strip("|").split("|")[0].strip() for ln in table_lines]
    missing_rows = [r for r in COMPARISON_ROW_NAMES if r not in row_first_cells]
    if missing_rows:
        problems.append("对照表缺维度行名%s" % "、".join(missing_rows))
    decl_count = text.count(COMPARISON_NO_INHERIT_DECL)
    if decl_count != 1:
        problems.append("无继承声明行命中=%d（应＝1）" % decl_count)
    return problems


def pool_entry_confirmed(block: "dict", dir_name: str) -> bool:
    """FC-6 条目确认块判据：四字段恰备非空＋产物id 与目录名逐字全等。"""
    return (set(str(k) for k in block) == set(POOL_CONFIRM_FIELDS)
            and all(str(v).strip() for v in block.values())
            and str(block.get("产物id", "")).strip() == dir_name)


def non_regression_shrunk(current: "tuple[str, ...] | int", baseline: "tuple[str, ...] | int") -> "list[str]":
    """GS-5 只增不减判据：集合基线返回被删值列表；基数基线越线返回越线标记列表。"""
    if isinstance(baseline, tuple):
        return [b for b in baseline if b not in set(current)]
    return [] if int(current) >= int(baseline) else ["基数%s＜基线%s" % (current, baseline)]


def _repo_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.dirname(_SKILL_ROOT)))


def _active_pool_dir() -> str:
    return os.path.join(_repo_root(), *_PRODUCTS_SUBPATH)


def _product_entries() -> "list[tuple[str, str]]":
    """active 池条目列表 (目录名, 路径)：仅生效池根直接条目——池计数口径（FC-6 消费）。"""
    pool = _active_pool_dir()
    if not os.path.isdir(pool):
        return []
    out: "list[tuple[str, str]]" = []
    for name in sorted(os.listdir(pool)):
        path = os.path.join(pool, name)
        if os.path.isdir(path) and name.endswith(_PRODUCT_DIR_SUFFIXES):
            out.append((name, path))
    return out


def _product_scan_entries() -> "list[tuple[str, str]]":
    """产物级扫描面枚举 (目录名, 路径)＝生效池根直接条目＋pending/ 一层下产物目录。

    两口径分离：本枚举供产物级判据（ST-3 节结构／BW-1／BW-2／BW-5(b) 词表实扫）消费；
    active 池计数（FC-6）只消费 `_product_entries()`（池根直接条目），暂存区条目不计入池。
    pending/ 不存在＝空扫描合法态（同扩面前口径）；历史记录区目录不入本构造（免产物级机检）。
    """
    out = _product_entries()
    pending_dir = os.path.join(_active_pool_dir(), _PENDING_SUBDIR)
    if os.path.isdir(pending_dir):
        for name in sorted(os.listdir(pending_dir)):
            path = os.path.join(pending_dir, name)
            if os.path.isdir(path) and name.endswith(_PRODUCT_DIR_SUFFIXES):
                out.append((name, path))
    return out


def _entry_texts(entries: "list[tuple[str, str]]") -> "dict[str, dict[str, str]]":
    """扫描枚举 → 逐条目 {文件名: 文本} 映射（纯内存形态，词表实扫判据的自证样本可注入）。"""
    return {name: _product_md_texts(path) for name, path in entries}


def word_gate_hits(entry_texts: "dict[str, dict[str, str]]",
                   banned: "tuple[str, ...]") -> "tuple[list[str], int]":
    """词表门禁产物正文实跑位：逐条目逐正文件跑禁语命中，返回 (命中列表, 扫描件数)。空列表＝放。"""
    hits: "list[str]" = []
    scanned = 0
    for name in sorted(entry_texts):
        for fname in sorted(entry_texts[name]):
            scanned += 1
            for w in banned_phrase_hits(entry_texts[name][fname], banned):
                hits.append("%s/%s:%s" % (name, fname, w))
    return hits, scanned


def _product_md_texts(dirpath: str) -> "dict[str, str]":
    """产物目录内 .md 件文本（确认件除外——确认件属入池规程面，非产物正文）。"""
    texts: "dict[str, str]" = {}
    for name in sorted(os.listdir(dirpath)):
        if name.endswith(".md") and name != CONFIRM_FILE_NAME:
            texts[name] = _read_text(os.path.join(dirpath, name))
    return texts


# ============================================================
# 25 项目录断言 ↔ 函数（S1 实装：ST-1/ST-2/ST-5/FC-1/FC-2/FC-3/FC-4；S2 实装：ST-6/ST-7/FC-5；
# S3 实装：GS-1/GS-2/GS-3；S4 实装：ST-3/ST-8/BW-5/BW-6/FC-6/GS-5；余者桩）
# ============================================================

def st_1_contract_file() -> "tuple[str, str]":
    """ST-1 产物契约文件存在可解析——〔S0a 建／S1 实装〕。"""
    texts = _contract_texts()
    main_name = "artifact-contract"
    if main_name not in texts:
        return (READ_FAIL, "主契约面 contracts/%s.md 缺失" % main_name)
    _, bad = md_json_blocks(texts[main_name])
    if bad:
        return (READ_FAIL, "artifact-contract json 块解析失败 %d 处" % bad)
    extra, missing = section_diff(tuple(md_sections(texts[main_name])), AC_SECTIONS)
    if extra or missing:
        return (READ_FAIL, "AC 节闭集 diff 多出%s 缺失%s" % (sorted(extra), sorted(missing)))
    return (READ_PASS, "主契约面在场·json 可解析·AC 节闭集 diff=∅")


def st_2_three_kernel_files() -> "tuple[str, str]":
    """ST-2 evidence-grading／failure-modes／artifact-contract 三文件存在——〔S0a 建／S1 实装〕。"""
    texts = _contract_texts()
    missing = [n for n in KERNEL_THREE_FILES if n not in texts]
    if missing:
        return (READ_FAIL, "缺件%s" % "、".join(missing))
    registries = {"evidence-grading": EG_SECTIONS, "failure-modes": FM_SECTIONS, "artifact-contract": AC_SECTIONS}
    problems: "list[str]" = []
    for name, reg in registries.items():
        extra, miss = section_diff(tuple(md_sections(texts[name])), reg)
        if extra or miss:
            problems.append("%s 节diff 多出%s 缺失%s" % (name, sorted(extra), sorted(miss)))
    if problems:
        return (READ_FAIL, "；".join(problems))
    return (READ_PASS, "三件在 contracts/ 实体·节闭集 diff=∅（EG6/FM5/AC5）")


def st_3_section_closed_diff() -> "tuple[str, str]":
    """ST-3 perspective 五层节／technique 六段卡＋五字段闭集 diff＝∅——〔S0a 建／S4 实装〕。

    实装基面＝产物级扫描面枚举（生效池根直接条目＋pending/ 一层下产物目录）内的产物本体件
    （`SKILL.md`；随件件不入节结构 diff 面——节闭集只钉本体节形）：
    perspective 产物 H2 节名去空白归一后与五层闭集 diff＝∅；technique 产物节头按
    段名前缀归一化口径 diff＝∅（描述名改名＝咬）；卡体 json 块五字段闭集 ⊆ 检。
    无实例＝空扫描合法态判绿（FC-5/GS 同款），判据活性由 selftest 节闭集咬放配对实证。
    """
    entries = _product_scan_entries()
    problems: "list[str]" = []
    checked = 0
    for name, path in entries:
        texts = _product_md_texts(path)
        for fname, text in texts.items():
            if fname != _PRODUCT_BODY_FILE:
                continue
            checked += 1
            if name.endswith("-perspective"):
                heads = perspective_head_sections(text)
                extra, missing = section_diff(heads, PERSPECTIVE_SECTIONS)
                if extra or missing:
                    problems.append("%s/%s 五层节diff 多出%s 缺失%s"
                                    % (name, fname, sorted(extra) or "∅", sorted(missing) or "∅"))
            if name.endswith("-technique"):
                heads = tuple(m.group(1) for m in _H2_SEC_RE.finditer(text))
                card_heads = tuple(h for h in heads if _SEG_HEAD_RE.match(h.strip()))
                if card_heads:
                    extra, missing, bad = technique_segment_normalize(card_heads)
                    if extra or missing:
                        problems.append("%s/%s 六段diff 多出%s 缺失%s"
                                        % (name, fname, sorted(extra) or "∅", sorted(missing) or "∅"))
                    if bad:
                        problems.append("%s/%s 段头描述名改名/形态非法%s" % (name, fname, bad))
                blocks, _bad = md_json_blocks(text)
                for block in blocks:
                    if not card_fields_closed_ok(block):
                        problems.append("%s/%s 卡体五字段越闭集" % (name, fname))
            # bundle 条目：两命名空间隔离判据归 FC-5（跨层互借检出）；bundle 内部两层
            # 各自结构检随首个 bundle 产物接入时按两轨口径分别展开（扫描面已含条目文件）。
    if problems:
        return (READ_FAIL, "产物实例节结构 diff 非∅：%s" % "；".join(problems))
    return (READ_PASS, "产物实例 %d 条目·文件 %d·节结构 diff=∅（%s）"
            % (len(entries), checked, "实产物判绿" if entries else "空扫描合法态·配对咬放见 selftest"))


def test_prompts_list_blocks(text: str) -> "tuple[list[list[dict]], int]":
    """ST-4 实装层（T5 建）：抽 markdown 内顶层为 list 的 fenced json 块。

    `md_json_blocks` 只收 dict 块，list 块须单独解析（防误判缺块）。
    返回 (非空 list 块列表, 解析失败数)；空 list 块不入首列（空 list＝无条目，由调用侧咬）。
    """
    lists: "list[list[dict]]" = []
    bad = 0
    for raw in _JSON_FENCE_RE.findall(text):
        try:
            parsed = json.loads(raw)
        except ValueError:
            bad += 1
            continue
        if isinstance(parsed, list) and parsed:
            lists.append(parsed)
    return lists, bad


def st_4_test_prompts() -> "tuple[str, str]":
    """ST-4 test-prompts 存在可解析＋条目字段闭集——〔S0a 建／T5 实装〕。

    实装基面＝产物级扫描面枚举（同 ST-3＝生效池根直接条目＋pending/ 一层下产物目录），
    消费条目随件 `test-prompts.md`：件存在＋至少一个顶层非空 json list 块＋
    每条目字段集合 ⊆ TEST_PROMPT_FIELDS＋`期望档位` ∈ ABSTAIN_TIERS＋`所属轨` ∈ SIDE_TRACKS；
    无条目＝空扫描合法态判绿（ST-3/FC-5 同款口径）；判据本体复用 test_prompt_entries_ok()。
    `是否锚点题` 构造口径引用 validator-catalog VA-P-05（R13 时序），本断言只查字段闭集不查锚点题真实性。
    """
    entries = _product_scan_entries()
    targets = [(n, p) for n, p in entries if n.endswith(("-perspective", "-technique"))]
    problems: "list[str]" = []
    per_entry_counts: "list[str]" = []
    entries_total = 0
    for name, path in targets:
        prompts_path = os.path.join(path, _TEST_PROMPTS_FILE)
        if not os.path.isfile(prompts_path):
            problems.append("%s 随件 %s 缺失（回归资产缺位）" % (name, _TEST_PROMPTS_FILE))
            continue
        lists, bad = test_prompts_list_blocks(_read_text(prompts_path))
        if bad:
            problems.append("%s/%s json 解析失败 %d 处" % (name, _TEST_PROMPTS_FILE, bad))
            continue
        if not lists:
            problems.append("%s/%s 无顶层非空 json list 块（缺块或空 list）" % (name, _TEST_PROMPTS_FILE))
            continue
        all_entries: "list[dict]" = []
        for lst in lists:
            all_entries.extend(e for e in lst if isinstance(e, dict))
        non_dict = sum(len(lst) for lst in lists) - len(all_entries)
        if non_dict:
            problems.append("%s/%s list 块含非对象条目 %d 条" % (name, _TEST_PROMPTS_FILE, non_dict))
            continue
        entries_total += len(all_entries)
        per_entry_counts.append("%s=%d" % (name, len(all_entries)))
        if not test_prompt_entries_ok(all_entries) or not test_prompt_values_ok(all_entries):
            details: "list[str]" = []
            allowed = set(TEST_PROMPT_FIELDS)
            for i, entry in enumerate(all_entries, 1):
                unknown = {str(k) for k in entry} - allowed
                if unknown:
                    details.append("条目%d 未注册字段%s" % (i, sorted(unknown)))
                tier = entry.get("期望档位")
                if tier is not None and str(tier) not in ABSTAIN_TIERS:
                    details.append("条目%d 期望档位%s越四档闭集" % (i, tier))
                track = entry.get("所属轨")
                if track is not None and str(track) not in SIDE_TRACKS:
                    details.append("条目%d 所属轨%s越轨闭集" % (i, track))
            problems.append("%s/%s 条目越闭集：%s" % (name, _TEST_PROMPTS_FILE, "；".join(details) or "条目集合非法"))
    if problems:
        return (READ_FAIL, "test-prompts 回归件判据违例：%s" % "；".join(problems))
    return (READ_PASS, "产物条目 %d·回归条目 %d（逐条目 %s）·字段闭集＋档位/轨取值判绿（%s）"
            % (len(targets), entries_total, "／".join(per_entry_counts) or "无",
               "实产物判绿" if targets else "空扫描合法态·配对咬放见 selftest"))


def st_5_rejected_coverage() -> "tuple[str, str]":
    """ST-5 rejected/ 可枚举＋coverage-audit 三问字段——〔S0a 建／S1 实装〕。

    目录不存在＝PENDING（留档基面未落＝不算 fail）；存在＝实检：批次目录逐份验
    coverage-audit 三问齐备＋条目 json 三问可答；批次为零＝空 listing 合法可枚举态。
    """
    if not os.path.isdir(_REJECTED_DIR):
        return (READ_PENDING, "rejected/ 目录不存在（留档基面未落）")
    batches = sorted(d for d in os.listdir(_REJECTED_DIR)
                     if os.path.isdir(os.path.join(_REJECTED_DIR, d)))
    problems: "list[str]" = []
    audited = 0
    entries_checked = 0
    for batch in batches:
        batch_dir = os.path.join(_REJECTED_DIR, batch)
        audit_path = os.path.join(batch_dir, "coverage-audit.md")
        if not os.path.isfile(audit_path):
            problems.append("%s/ 缺 coverage-audit.md" % batch)
        else:
            blocks, bad = md_json_blocks(_read_text(audit_path))
            if bad:
                problems.append("%s/coverage-audit json 解析失败 %d" % (batch, bad))
            elif not audit_fields_ok(blocks):
                problems.append("%s/coverage-audit 三问字段不齐备非空" % batch)
            else:
                audited += 1
        for name in sorted(os.listdir(batch_dir)):
            if name == "coverage-audit.md" or not name.endswith(".md"):
                continue
            blocks, bad = md_json_blocks(_read_text(os.path.join(batch_dir, name)))
            if bad or not blocks:
                problems.append("%s/%s 无合法 json 块" % (batch, name))
                continue
            for block in blocks:
                entries_checked += 1
                if not entry_question_ok(block):
                    problems.append("%s/%s 条目三问字段缺位" % (batch, name))
    if problems:
        return (READ_FAIL, "；".join(problems))
    return (READ_PASS, "批次 %d·审计件 %d·条目 %d（空 listing 合法）" % (len(batches), audited, entries_checked))


def st_6_person_ir_exclusion() -> "tuple[str, str]":
    """ST-6 person adapter 无 technique 轨 IR 段名（「执行步骤」段字样命中＝0）——〔S2 建／S2 实装〕。"""
    texts = _adapter_texts()
    if "adapter-person" not in texts:
        return (READ_FAIL, "adapters/person.md 缺失（无互检基面）")
    hits = ir_term_hits(texts["adapter-person"], PERSON_FORBIDDEN_IR_TERMS)
    if hits:
        return (READ_FAIL, "person 面命中 technique 轨 IR 段名%s（IR 串味·坏信号①）" % hits)
    return (READ_PASS, "person 面无「执行步骤」段字样·命中=0")


def st_7_method_ir_exclusion() -> "tuple[str, str]":
    """ST-7 method adapter 无 persona 轨 IR 节名（「表达 DNA」段字样命中＝0）——〔S2 建／S2 实装〕。"""
    texts = _adapter_texts()
    if "adapter-method" not in texts:
        return (READ_FAIL, "adapters/method.md 缺失（无互检基面）")
    hits = ir_term_hits(texts["adapter-method"], METHOD_FORBIDDEN_IR_TERMS)
    if hits:
        return (READ_FAIL, "method 面命中 persona 轨 IR 节名%s（IR 串味·坏信号①）" % hits)
    return (READ_PASS, "method 面无「表达 DNA」段字样·命中=0")


def bw_1_roleplay_vocab() -> "tuple[str, str]":
    """BW-1 角色扮演禁语词表本体落盘＋产物正文实跑位——〔S0a〕词表本体在场类。

    产物正文实跑位＝产物级扫描面枚举（生效池根＋pending/ 一层下产物目录）逐正文件禁语命中，
    命中数＝0 才绿（词表消费接到产物枚举＝门禁实跑，无产物＝空扫描 0 命中平凡真）。
    """
    ok = vocab_body_present(ROLEPLAY_BANNED_WORDS)
    if not ok:
        return (READ_FAIL, "词表本体不在场/条目格式非法（条目 %d）" % len(ROLEPLAY_BANNED_WORDS))
    hits, scanned = word_gate_hits(_entry_texts(_product_scan_entries()), ROLEPLAY_BANNED_WORDS)
    if hits:
        return (READ_FAIL, "产物正文角色扮演禁语命中%s（产物违规·风险档跳档复核）" % hits)
    return (READ_PASS, "词表条目 %d·产物正文实跑命中=0（扫描 %d 件）" % (len(ROLEPLAY_BANNED_WORDS), scanned))


def bw_2_blunt_vocab_tiers() -> "tuple[str, str]":
    """BW-2 无据斩钉截铁词表＋四档口径标注位＋产物正文实跑位——〔S0a〕词表本体在场类。

    产物正文实跑位同 BW-1（同一扫描面枚举，触发词命中数＝0 才绿）。
    """
    ok = (vocab_body_present(BLUNT_ASSERTION_WORDS)
          and len(set(ABSTAIN_TIERS)) == 4
          and vocab_body_present(ABSTAIN_TIERS))
    if not ok:
        return (READ_FAIL, "词表或四档标注位不在场（触发词 %d·档位 %d）"
                % (len(BLUNT_ASSERTION_WORDS), len(ABSTAIN_TIERS)))
    hits, scanned = word_gate_hits(_entry_texts(_product_scan_entries()), BLUNT_ASSERTION_WORDS)
    if hits:
        return (READ_FAIL, "产物正文无据斩钉截铁触发命中%s（应落弃权四档其一）" % hits)
    return (READ_PASS, "触发词 %d·档位 %d·产物正文实跑命中=0（扫描 %d 件）"
            % (len(BLUNT_ASSERTION_WORDS), len(ABSTAIN_TIERS), scanned))


def bw_3_bare_number_rule() -> "tuple[str, str]":
    """BW-3 裸数字检出规则——〔S0a 建／S1 执行〕（检出器已就位＝bare_number_hits，产物报告待产物面）。"""
    return (READ_PENDING, "S1")


def bw_4_b_segment_decl() -> "tuple[str, str]":
    """BW-4 technique 卡 B 段边界声明存在——〔S0a 建／S1 执行〕。"""
    return (READ_PENDING, "S1")


def fc_1_two_field_closedset() -> "tuple[str, str]":
    """FC-1 evidence_grade／calibration_state 两字段闭集——〔S0a 建／S1 实装〕。

    两字段名在契约注册（声明面在场）＋契约声明值与工具注册值逐字全等（双向 diff＝∅）。
    """
    texts = _contract_texts()
    blocks, _ = _all_blocks(texts)
    names = declared_field_names(blocks)
    for field in ("evidence_grade", "calibration_state"):
        if field not in names:
            return (READ_FAIL, "字段 %s 未在契约声明面注册" % field)
    fc1_only = {"evidence_grade": EVIDENCE_GRADES, "calibration_state": CALIBRATION_STATES}
    problems = value_decl_diff(blocks, fc1_only)
    if problems:
        return (READ_FAIL, "值闭集 diff 非∅：%s" % "；".join(problems))
    return (READ_PASS, "两字段名在注册面·两值闭集与契约声明逐字全等")


def fc_2_kernel_fields_diff() -> "tuple[str, str]":
    """FC-2 三文件字段名闭集未注册字段 diff＝∅——〔S0a 建／S1 实装〕（注册表按扩充清单）。

    机检口径三条：①契约声明字段名 ⊆ 注册表；②实例 json 记录字段名 ⊆ 注册表；
    ③注册表 ⊆ 契约声明字段名（双向 diff＝∅，防注册表私扩）。
    附带 FM 条目纪律（五元组非空＋处置列不确定措辞子串扫描＋轨别/前缀匹配）。
    """
    texts = _contract_texts()
    missing = [n for n in KERNEL_THREE_FILES if n not in texts]
    if missing:
        return (READ_FAIL, "契约缺件%s（无声明基面）" % "、".join(missing))
    blocks, bad = _all_blocks(texts)
    if bad:
        return (READ_FAIL, "json 块解析失败 %d 处" % bad)
    declared = declared_field_names(blocks)
    extra, missing_reg = kernel_field_diff(declared, KERNEL_FIELD_REGISTRY, COVERAGE_AUDIT_FIELDS)
    problems: "list[str]" = []
    if extra:
        problems.append("声明侧未注册多出%s" % sorted(extra))
    if missing_reg:
        problems.append("注册表未声明缺失%s" % sorted(missing_reg))
    # ②实例记录字段名 ⊆ 注册表（EG-5 示例行＋留档条目示例）
    allowed = set(KERNEL_FIELD_REGISTRY) | set(COVERAGE_AUDIT_FIELDS)
    for block in blocks:
        if "字段注册" in block or "值注册" in block:
            continue
        inst_unknown = {str(k) for k in block} - allowed
        if inst_unknown:
            problems.append("实例记录未注册字段%s" % sorted(inst_unknown))
    # FM 条目纪律挂本断言（执行票口径：既编项实装化＋子检查承载，不新增断言编号）
    if "failure-modes" in texts:
        problems.extend(fm_entries_discipline(fm_entries_from_text(texts["failure-modes"])))
    # 契约声明值 ↔ 工具注册值全量互洽（九对照字段，逐字全等）
    problems.extend(value_decl_diff(blocks, VALUE_REGISTRIES))
    if problems:
        return (READ_FAIL, "；".join(problems))
    return (READ_PASS, "注册表 %d 字段·双向 diff=∅·实例⊆注册·FM条目纪律·值互洽全等"
            % len(KERNEL_FIELD_REGISTRY))


def fc_3_paired_source_location() -> "tuple[str, str]":
    """FC-3 source_id＋位置双形态字段成对——〔S0a 建／S1 实装／T5 产物要素侧扩展〕。

    契约实例侧判据零动（contracts/ json 实例逐条成对）；T5 追加产物要素侧＝
    产物级扫描面（同 ST-3）逐条目本体件行级成对检（要素标注行缺 source_id 或 位置 任一＝咬）；
    模型推断态哨兵取值见 EG-3（哨兵形态形式满足成对判据）。
    """
    texts = _contract_texts()
    records: "list[dict]" = []
    for text in texts.values():
        blocks, _ = md_json_blocks(text)
        for block in blocks:
            if "字段注册" in block or "值注册" in block:
                continue
            records.append(block)
    if not paired_fields_ok(records):
        return (READ_FAIL, "契约 json 实例 source_id/位置 不成对")
    hits, marked = product_element_pair_hits(_entry_texts(_product_scan_entries()))
    if hits:
        return (READ_FAIL, "产物要素行 source_id/位置 不成对：%s" % "；".join(hits))
    return (READ_PASS, "契约 json 实例 %d 条成对判绿·产物要素侧要素行 %d 行成对判绿（%s）"
            % (len(records), marked, "无要素行＝空扫描合法态" if not marked else "实要素行判绿"))


def fc_4_state_vocab_board() -> "tuple[str, str]":
    """FC-4 状态词表取值闭集＋看板三栏字段名闭集——〔S0a 建／S1 实装／S2 黄-2 收口扩展〕。

    词表本体在场（六值闭集锁定·T6 扩「受限」）＋看板契约节声明行在 AC-5 节＋
    看板实例（如在场）三栏标题∈注册三栏、性质声明行在场、相邻板日期间隔 ≤14 天＋
    黄-2 收口两扫描：看板正文「状态」关键词行反引号 token ⊆ 词表∪字段注册表（私扩必咬）；
    AC-5「基线闭集」声明句反引号 token 与词表全集逐字全等（私扩/缺值必咬）。
    """
    ok_vocab = vocab_body_present(STATE_WORDS) and len(set(STATE_WORDS)) == 6
    texts = _contract_texts()
    ac_text = texts.get("artifact-contract", "")
    decl_in_ac5 = all(("`%s`" % c) in ac_text for c in BOARD_COLUMNS)
    header_ok = BOARD_HEADER_DECL in ac_text
    if not (ok_vocab and decl_in_ac5 and header_ok):
        return (READ_FAIL, "词表在场=%s 三栏声明在AC-5=%s 性质声明行=%s" % (ok_vocab, decl_in_ac5, header_ok))
    vocab_hits = state_token_scan(ac_text, VOCAB_LINE_KEY, STATE_WORDS, exact=True)
    if vocab_hits:
        return (READ_FAIL, "AC-5 词表声明句私扩/缺值：%s" % "；".join(vocab_hits))
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(_SKILL_ROOT)))
    board_dir = os.path.normpath(os.path.join(repo_root, ".collab", "board"))
    ok_board, detail = board_files_ok(board_dir)
    if not ok_board:
        return (READ_FAIL, detail)
    token_hits: "list[str]" = []
    if os.path.isdir(board_dir):
        for name in sorted(n for n in os.listdir(board_dir) if _BOARD_NAME_RE.match(n)):
            body = _read_text(os.path.join(board_dir, name))
            token_hits.extend("%s:%s" % (name, h)
                              for h in state_token_scan(body, BOARD_STATE_LINE_KEY, STATE_WORDS, exact=False))
    if token_hits:
        return (READ_FAIL, "看板正文状态token越词表：%s" % "；".join(token_hits))
    return (READ_PASS, "词表六值·三栏名声明 AC-5·词表声明句逐字全等·%s·看板状态token扫描判绿" % detail)


def fc_5_bundle_ns_isolation() -> "tuple[str, str]":
    """FC-5 bundle 两层验证状态命名空间隔离互借检出＝0——〔S0a 建／S2 实装〕。

    扫描基面＝contracts/＋adapters/ 全部 json 块中的 bundle 实例记录
    （顶层同时含 persona／technique 两键）；逐条跑互借检出，全量命中数＝0 才算过。
    当期无 bundle 实例＝空扫描合法态（互借检出 0），配对咬放交 selftest 实证判据活性。
    """
    texts = _contract_texts()
    texts.update(_adapter_texts())
    blocks, bad = _all_blocks(texts)
    if bad:
        return (READ_FAIL, "json 块解析失败 %d 处" % bad)
    bundles = [b for b in blocks if bundle_layers(b)]
    hits: "list[str]" = []
    for rec in bundles:
        hits.extend(ns_borrow_hits({"persona": rec.get("persona", {}),
                                    "technique": rec.get("technique", {})}))
    if hits:
        return (READ_FAIL, "跨层互借字段检出%s（应＝0）" % hits)
    return (READ_PASS, "bundle 实例 %d 条·命名空间互借检出=0（配对咬放实证见 selftest）" % len(bundles))


def _verification_records() -> "tuple[list[dict], list[str]]":
    """读验证记录目录（validator-catalog 顶部注册落盘路径＝.collab/evidence/harness/ 递归 *.jsonl）。

    返回 (记录列表, 读取问题列表)；目录不在场＝空扫描合法态（读取问题空）。
    """
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(_SKILL_ROOT)))
    rec_dir = os.path.join(repo_root, *_HARNESS_SUBPATH)
    records: "list[dict]" = []
    problems: "list[str]" = []
    if not os.path.isdir(rec_dir):
        return (records, problems)
    for dirpath, _dirnames, filenames in os.walk(rec_dir):
        for name in sorted(filenames):
            if not name.endswith(".jsonl"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, "r", encoding="utf-8", errors="replace", newline="") as handle:
                for lineno, line in enumerate(handle, 1):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        obj = json.loads(line)
                    except ValueError:
                        problems.append("%s:%d json 解析失败" % (name, lineno))
                        continue
                    if isinstance(obj, dict):
                        records.append(obj)
                    else:
                        problems.append("%s:%d 非对象记录" % (name, lineno))
    return (records, problems)


def gs_1_person_gate_source() -> "tuple[str, str]":
    """GS-1 person 轨 gate_source 白名单（调 method 硬门判据命中＝0）——〔S0a 建／S3 实装〕。

    实装基面＝验证记录目录（validator-catalog 注册落盘路径）内全部 person 记录；
    无记录＝空扫描合法态（不匹配数 0，配对咬放交 selftest 实证判据活性）。
    """
    records, read_problems = _verification_records()
    if read_problems:
        return (READ_FAIL, "验证记录读取问题：%s" % "；".join(read_problems))
    hits: "list[str]" = []
    person_count = 0
    for rec in records:
        track = str(rec.get("所属轨", ""))
        if track != "person":
            continue
        person_count += 1
        gate = str(rec.get("gate_source", ""))
        hits.extend("%s:%s" % (str(rec.get("记录id", "?")), h) for h in gate_source_hits(track, gate))
    if hits:
        return (READ_FAIL, "person 轨 gate_source 越白名单命中%s（应＝0）" % hits)
    return (READ_PASS, "person 记录 %d 条·越白名单命中=0（%s）" % (person_count, "实记录判绿" if person_count else "空扫描合法态·配对咬放见 selftest"))


def gs_2_method_gate_source() -> "tuple[str, str]":
    """GS-2 method 轨 gate_source 对称白名单——〔S0a 建／S3 实装〕（R18 双向之反向）。"""
    records, read_problems = _verification_records()
    if read_problems:
        return (READ_FAIL, "验证记录读取问题：%s" % "；".join(read_problems))
    hits: "list[str]" = []
    method_count = 0
    for rec in records:
        track = str(rec.get("所属轨", ""))
        if track != "method":
            continue
        method_count += 1
        gate = str(rec.get("gate_source", ""))
        hits.extend("%s:%s" % (str(rec.get("记录id", "?")), h) for h in gate_source_hits(track, gate))
    if hits:
        return (READ_FAIL, "method 轨 gate_source 越白名单命中%s（应＝0）" % hits)
    return (READ_PASS, "method 记录 %d 条·越白名单命中=0（%s）" % (method_count, "实记录判绿" if method_count else "空扫描合法态·配对咬放见 selftest"))


def gs_3_bidirectional_zero_mismatch() -> "tuple[str, str]":
    """GS-3 双向断言不匹配数＝0（S3 硬验收位）——〔S0a 建／S3 实装〕。

    GS-1＋GS-2 合成双向：全量验证记录（含未知轨记录）的不匹配数＝0 才算过；
    validator 写记录时自检同表（双保险，两处同一注册表）。
    """
    records, read_problems = _verification_records()
    if read_problems:
        return (READ_FAIL, "验证记录读取问题：%s" % "；".join(read_problems))
    mismatch = 0
    unknown_track: "list[str]" = []
    for rec in records:
        track = str(rec.get("所属轨", ""))
        gate = str(rec.get("gate_source", ""))
        hits = gate_source_hits(track, gate)
        if any(h.startswith("未知轨") for h in hits):
            unknown_track.append(str(rec.get("记录id", "?")))
        mismatch += len(hits)
    if unknown_track:
        return (READ_FAIL, "未知轨记录%s（白名单 diff 不可判）" % unknown_track)
    if mismatch:
        return (READ_FAIL, "双向不匹配数=%d（应＝0·S3 硬验收不过）" % mismatch)
    return (READ_PASS, "全量记录 %d 条·双向不匹配数=0（%s）" % (len(records),
            "实记录硬验收判绿" if records else "空扫描合法态·硬验收读数随当批实记录在场"))


def _gs4_tuple_obj_problems(name: str, obj: "dict") -> "list[str]":
    """GS-4 逐元组对账挂接层（判据本体＝calibration_consistent() 零改动，本层只装配读数）。

    κ 字段缺失/置 null＝按「无 κ 报告」入同一判据（受限元组只能待校准，fail-closed）；
    calibration_state 越闭集＝直接咬。返回问题列表（空＝一致）。
    """
    state = str(obj.get("calibration_state", ""))
    if state not in CALIBRATION_STATES:
        return ["%s calibration_state=%r 越两值闭集（fail-closed）" % (name, state)]
    point = obj.get("κ点值", None)
    lower = obj.get("κ区间下界", None)
    kappa = None if (point is None or lower is None) else {"点值": point, "区间下界": lower}
    if not calibration_consistent(state, kappa):
        return ["%s κ报告与 calibration_state=%s 不一致（κ点值=%s·区间下界=%s）"
                % (name, state, point, lower)]
    return []


def gs_4_calibration_kappa() -> "tuple[str, str]":
    """GS-4 calibration_state 与 κ 报告一致性校验器——〔S0a 建／S0b 实装〕。

    实装基面＝validator-catalog 注册落盘路径（`.collab/evidence/harness/` 递归）内全部
    `anchor-tuple*.json`（复用 `_HARNESS_SUBPATH` 注册路径）：
    无元组＝PENDING_STAGE「S0b 元组未交付」（当期如实态，不算 fail 不算 pass）；
    元组在场＝逐元组跑既有纯函数 calibration_consistent()（判据零改动，仅挂接）
    对账 κ 点值/区间下界 ↔ calibration_state；任一不一致＝FAIL 逐条列明细；
    全对＝PASS（读数含元组数）。
    """
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(_SKILL_ROOT)))
    rec_dir = os.path.join(repo_root, *_HARNESS_SUBPATH)
    tuple_paths: "list[str]" = []
    if os.path.isdir(rec_dir):
        for dirpath, _dirnames, filenames in os.walk(rec_dir):
            for fname in sorted(filenames):
                if fname.startswith("anchor-tuple") and fname.endswith(".json"):
                    tuple_paths.append(os.path.join(dirpath, fname))
    if not tuple_paths:
        return (READ_PENDING, "S0b 元组未交付")
    problems: "list[str]" = []
    for path in sorted(tuple_paths):
        name = os.path.relpath(path, rec_dir).replace("\\", "/")
        try:
            with open(path, "r", encoding="utf-8") as handle:
                obj = json.load(handle)
        except ValueError:
            problems.append("%s json 解析失败（fail-closed）" % name)
            continue
        if not isinstance(obj, dict):
            problems.append("%s 非对象元组" % name)
            continue
        problems.extend(_gs4_tuple_obj_problems(name, obj))
    if problems:
        return (READ_FAIL, "元组在场·对账不一致：%s" % "；".join(problems))
    return (READ_PASS, "元组 %d 个在场·κ 报告与 calibration_state 逐元组对账全一致（判据本体零改动）"
            % len(tuple_paths))


def st_8_spec_tables_closed() -> "tuple[str, str]":
    """ST-8 两规范表文件存在＋自身四节节闭集 diff＝∅＋关键引用行在场——〔S4 建／S4 实装〕。

    固定路径静态扫描 `specs/` 两规范表文件；未建齐＝PENDING（ST-5 先例），建齐后当期即绿。
    """
    specs_dir = os.path.join(_SKILL_ROOT, "specs")
    missing_files = [n for n in SPEC_FILES
                     if not os.path.isfile(os.path.join(specs_dir, n + ".md"))]
    if missing_files:
        return (READ_PENDING, "规范表未建齐（缺%s）" % "、".join(missing_files))
    problems: "list[str]" = []
    for name in SPEC_FILES:
        text = _read_text(os.path.join(specs_dir, name + ".md"))
        extra, missing = section_diff(spec_sections(text), SPEC_FOUR_SECTIONS)
        if extra or missing:
            problems.append("%s 四节节diff 多出%s 缺失%s"
                            % (name, sorted(extra) or "∅", sorted(missing) or "∅"))
        miss_refs = spec_missing_key_refs(text, SPEC_KEY_REFS[name])
        if miss_refs:
            problems.append("%s 关键引用行缺失%s" % (name, "、".join(miss_refs)))
    if problems:
        return (READ_FAIL, "；".join(problems))
    return (READ_PASS, "两规范表在场·四节闭集 diff=∅·关键引用行（AC-1/总则声明行/AC-2/VA-S-01）在场")


def bw_5_contradiction_smoothing() -> "tuple[str, str]":
    """BW-5 矛盾平滑检出（坏信号④机械位）——〔S4 建／S4 实装〕。

    (a) 声明面：`adapters/person.md` 含「内部矛盾不平滑」条款行＋「矛盾是深度的重要信号」
        措辞行在场（当期可绿）；
    (b) 产物面：平滑句式启发式预注册词表本体在场（BW-1/BW-2 同制）＋perspective 产物正文
        命中＝坏信号④咬（产物级扫描面枚举＝生效池根＋pending/ 一层下产物目录，无实例＝空扫描合法态）。
    """
    ok_vocab = vocab_body_present(SMOOTH_PHRASE_VOCAB) and len(set(SMOOTH_PHRASE_VOCAB)) == 4
    texts = _adapter_texts()
    if "adapter-person" not in texts:
        return (READ_FAIL, "adapters/person.md 缺失（无声明基面）")
    missing_rows = decl_rows_missing(texts["adapter-person"], PERSON_CONTRADICTION_DECL_ROWS)
    if missing_rows:
        return (READ_FAIL, "person 面矛盾条款声明行缺失%s（坏信号④声明面失守）" % missing_rows)
    if not ok_vocab:
        return (READ_FAIL, "平滑句式词表本体不在场/基数越线（应＝4 值预注册）")
    hits: "list[str]" = []
    scanned = 0
    for name, path in _product_scan_entries():
        if not name.endswith(("-perspective", "-bundle")):
            continue
        for fname, text in _product_md_texts(path).items():
            scanned += 1
            for w in blunt_hits(text, SMOOTH_PHRASE_VOCAB):
                hits.append("%s/%s:%s" % (name, fname, w))
    if hits:
        return (READ_FAIL, "产物正文平滑句式命中%s（内部矛盾消失·坏信号④）" % hits)
    return (READ_PASS, "(a) 声明行两行在场·(b) 词表 4 值本体在场·产物面命中=0（扫描 %d 件·%s）"
            % (scanned, "空扫描合法态" if not scanned else "实扫描判绿"))


def bw_6_readme_comparison_top() -> "tuple[str, str]":
    """BW-6 README 相近工具对照表置顶——〔S4 建／S4 实装〕。

    判据①首个二级标题前首个 markdown 表格含两对照工具名（本产品线列名另检）
    ＋②「无继承关系」声明行命中＝1＋③三维度行名齐备；任一违＝fail。
    """
    readme = os.path.join(_SKILL_ROOT, "README.md")
    if not os.path.isfile(readme):
        return (READ_FAIL, "包 README.md 缺失（无判据基面）")
    problems = readme_table_problems(_read_text(readme))
    if problems:
        return (READ_FAIL, "；".join(problems))
    return (READ_PASS, "对照表先于首个二级标题·两工具名＋本线列名命中·声明行命中=1·三维度行名齐备")


def fc_6_active_pool_confirmation() -> "tuple[str, str]":
    """FC-6 active 池人工确认存在断言（R16 验收）——〔S4 建／S4 实装〕。

    active 池目录内每一产物条目须可指向一条人工确认记录（条目根部确认件四字段引用行）；
    无确认记录的 active 条目数＝0。目录不存在＝PENDING（ST-5 先例）；目录在场且空＝
    空扫描合法态判绿（当期 0 属空池平凡真＝规程级实证，非产物级实证）。
    """
    pool = _active_pool_dir()
    if not os.path.isdir(pool):
        return (READ_PENDING, "active 池目录未建（生效池约定未落盘）")
    entries = _product_entries()
    unconfirmed: "list[str]" = []
    for name, path in entries:
        confirm_path = os.path.join(path, CONFIRM_FILE_NAME)
        if not os.path.isfile(confirm_path):
            unconfirmed.append(name)
            continue
        blocks, bad = md_json_blocks(_read_text(confirm_path))
        if bad or not blocks or not any(pool_entry_confirmed(b, name) for b in blocks):
            unconfirmed.append(name)
    if unconfirmed:
        return (READ_FAIL, "无人工确认来源条目数=%d（应＝0）：%s" % (len(unconfirmed), unconfirmed))
    return (READ_PASS, "active 池条目 %d·无人工确认来源条目数=0（%s）"
            % (len(entries), "空池平凡真·规程级实证非产物级" if not entries else "实条目确认引用行判绿"))


def gs_5_gate_non_regression() -> "tuple[str, str]":
    """GS-5 门禁不退化断言（坏信号③机械位）——〔S4 建／S4 实装〕。

    三组注册位对基线只增不减：validator 层名注册闭集（11 值）／两 gate_source 白名单
    （各六值）／断言编号基数（25 项）；机械断言层名（`机械断言`／`格式检查表`）在各自
    白名单在场。任一缩水＝咬。声明↔代码双向 diff＝validator-catalog §二 层名值注册
    与本注册常量互检（FC-1 同款手法）。
    """
    problems: "list[str]" = []
    shrunk = non_regression_shrunk(len(VALIDATOR_LAYER_NAMES), GS5_BASELINE["层名基数"])
    if shrunk:
        problems.extend("层名%s" % s for s in shrunk)
    problems.extend("person白名单%s" % s for s in non_regression_shrunk(len(set(PERSON_GATE_WHITELIST)), GS5_BASELINE["person白名单基数"]))
    problems.extend("method白名单%s" % s for s in non_regression_shrunk(len(set(METHOD_GATE_WHITELIST)), GS5_BASELINE["method白名单基数"]))
    problems.extend("断言基数%s" % s for s in non_regression_shrunk(len(ASSERTIONS), GS5_BASELINE["断言编号基数"]))
    if "机械断言" not in METHOD_GATE_WHITELIST:
        problems.append("机械断言层名越出 method 白名单（机械层被移除嫌疑）")
    if "格式检查表" not in PERSON_GATE_WHITELIST:
        problems.append("格式检查表层名越出 person 白名单（机械层被移除嫌疑）")
    catalog = os.path.join(os.path.dirname(os.path.abspath(__file__)), "validator-catalog.md")
    if os.path.isfile(catalog):
        blocks, _bad = md_json_blocks(_read_text(catalog))
        declared: "set[str]" = set()
        for block in blocks:
            vals = block.get("值注册")
            if isinstance(vals, dict) and isinstance(vals.get("层名"), list):
                declared.update(str(v) for v in vals["层名"])
        if declared:
            missing_decl = [v for v in VALIDATOR_LAYER_NAMES if v not in declared]
            extra_decl = sorted(declared - set(VALIDATOR_LAYER_NAMES))
            if missing_decl or extra_decl:
                problems.append("层名声明↔代码 diff 声明缺%s 多出%s" % (missing_decl or "∅", extra_decl or "∅"))
    else:
        problems.append("validator-catalog 缺失（层名声明基面不可得）")
    if problems:
        return (READ_FAIL, "门禁注册位退化/分叉：%s" % "；".join(problems))
    return (READ_PASS, "层名11·白名单6+6·断言基数%d·机械层名两白名单在场·层名声明↔代码 diff=∅（只增不减）"
            % len(ASSERTIONS))


ASSERTIONS: "list[tuple[str, str]]" = [
    ("ST-1", "st_1_contract_file"),
    ("ST-2", "st_2_three_kernel_files"),
    ("ST-3", "st_3_section_closed_diff"),
    ("ST-4", "st_4_test_prompts"),
    ("ST-5", "st_5_rejected_coverage"),
    ("ST-6", "st_6_person_ir_exclusion"),
    ("ST-7", "st_7_method_ir_exclusion"),
    ("ST-8", "st_8_spec_tables_closed"),
    ("BW-1", "bw_1_roleplay_vocab"),
    ("BW-2", "bw_2_blunt_vocab_tiers"),
    ("BW-3", "bw_3_bare_number_rule"),
    ("BW-4", "bw_4_b_segment_decl"),
    ("BW-5", "bw_5_contradiction_smoothing"),
    ("BW-6", "bw_6_readme_comparison_top"),
    ("FC-1", "fc_1_two_field_closedset"),
    ("FC-2", "fc_2_kernel_fields_diff"),
    ("FC-3", "fc_3_paired_source_location"),
    ("FC-4", "fc_4_state_vocab_board"),
    ("FC-5", "fc_5_bundle_ns_isolation"),
    ("FC-6", "fc_6_active_pool_confirmation"),
    ("GS-1", "gs_1_person_gate_source"),
    ("GS-2", "gs_2_method_gate_source"),
    ("GS-3", "gs_3_bidirectional_zero_mismatch"),
    ("GS-4", "gs_4_calibration_kappa"),
    ("GS-5", "gs_5_gate_non_regression"),
]


# ============================================================
# selftest：正负样本自证每类断言能咬能放
# ============================================================

def _selftest_cases() -> "list[tuple[str, bool, bool]]":
    """返回 (用例名, 判据结果, 期望结果) 列表；任一不符即 selftest 红。

    覆盖判据核心各一对正负样本（咬＝期望 False/有命中，放＝期望 True/无命中）。
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

    # 契约节闭集 diff（EG/FM/AC）：全等放／缺节咬／改名咬
    e1 = section_diff(EG_SECTIONS, EG_SECTIONS)
    e2 = section_diff(EG_SECTIONS[:5], EG_SECTIONS)
    e3 = section_diff(EG_SECTIONS[:5] + ("语料库登记",), EG_SECTIONS)
    cases.append(("EGsec_pass", e1 == (set(), set()), True))
    cases.append(("EGsec_bite_missing", e2 != (set(), set()), True))
    cases.append(("EGsec_bite_rename", e3 != (set(), set()), True))
    f1 = section_diff(FM_SECTIONS, FM_SECTIONS)
    f2 = section_diff(FM_SECTIONS + ("bundle轨条目",), FM_SECTIONS)
    cases.append(("FMsec_pass", f1 == (set(), set()), True))
    cases.append(("FMsec_bite_extra", f2 != (set(), set()), True))
    a1 = section_diff(AC_SECTIONS, AC_SECTIONS)
    a2 = section_diff(AC_SECTIONS[:4], AC_SECTIONS)
    cases.append(("ACsec_pass", a1 == (set(), set()), True))
    cases.append(("ACsec_bite_missing_board", a2 != (set(), set()), True))

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

    # ST-5 三问可答（条目实例）：三问齐放／缺对照臂咬／泄漏空咬
    full_rec = {"证据等级": "跨文本推断", "evidence_grade": "LLM 判定", "control_arm": "未测", "leakage_check": "未检"}
    no_arm = {"证据等级": "原文可证实", "evidence_grade": "机械断言", "leakage_check": "已检-不在语料内"}
    blank_leak = dict(full_rec, leakage_check="  ")
    cases.append(("Q3_pass", three_question_ok(full_rec), True))
    cases.append(("Q3_bite_no_arm", three_question_ok(no_arm), False))
    cases.append(("Q3_bite_blank_leak", three_question_ok(blank_leak), False))

    # BW-4 B 段：非空放／空段咬
    cases.append(("BW4_pass", b_segment_ok([{"R": "原文", "B": "仅限高频决策场景"}]), True))
    cases.append(("BW4_bite_empty", b_segment_ok([{"R": "原文", "B": "  "}]), False))

    # FC-2 未注册字段 diff：注册内放／自造字段咬（S1 扩充注册表）
    cases.append(("FC2_pass", unknown_field_names_diff(("evidence_grade", "source_id", "control_arm", "淘汰维度"), KERNEL_FIELD_REGISTRY), True))
    cases.append(("FC2_bite", unknown_field_names_diff(("evidence_grade", "自造字段"), KERNEL_FIELD_REGISTRY), False))

    # FC-2 契约字段闭集外值必咬（配对咬放例：注册表扩充字段放／闭集外字段双向咬）
    decl_ok = set(KERNEL_FIELD_REGISTRY)
    kp1 = kernel_field_diff(decl_ok, KERNEL_FIELD_REGISTRY, COVERAGE_AUDIT_FIELDS)
    kp2 = kernel_field_diff(decl_ok | {"自造字段"}, KERNEL_FIELD_REGISTRY, COVERAGE_AUDIT_FIELDS)
    kp3 = kernel_field_diff(decl_ok - {"一手占比门槛"}, KERNEL_FIELD_REGISTRY, COVERAGE_AUDIT_FIELDS)
    cases.append(("FC2K_pass", kp1[0] == set(), True))
    cases.append(("FC2K_bite_extra", kp2[0] != set(), True))
    cases.append(("FC2K_bite_reg_missing", kp3[1] != set(), True))

    # FC-1 值互洽（声明值↔注册值）：逐字全等放／越界值咬／缺声明咬
    good_block = [{"值注册": {"evidence_grade": ["人工验证", "机械断言", "LLM 判定"],
                              "calibration_state": ["校准态", "待校准"]}}]
    bad_block = [{"值注册": {"evidence_grade": ["人工验证", "机械断言", "LLM 判定", "直觉认定"],
                             "calibration_state": ["校准态", "待校准"]}}]
    partial_block = [{"值注册": {"evidence_grade": ["人工验证", "机械断言", "LLM 判定"]}}]
    fc1_pair = {"evidence_grade": EVIDENCE_GRADES, "calibration_state": CALIBRATION_STATES}
    cases.append(("FC1V_pass", value_decl_diff(good_block, fc1_pair) == [], True))
    cases.append(("FC1V_bite_extra_value", value_decl_diff(bad_block, fc1_pair) != [], True))
    cases.append(("FC1V_bite_missing_decl", value_decl_diff(partial_block, fc1_pair) != [], True))

    # FM 条目纪律：合法放／不确定措辞咬／轨别错挂咬
    good_rows = [
        ["FM-S-01", "共享", "语料不足", "一手占比检查读数", "转人工闸：索取补充语料"],
        ["FM-S-02", "共享", "上下文不足", "无成对标注检出", "降级：写证据不足"],
        ["FM-S-03", "共享", "成本失控", "台账越线读数", "阻断当前批次"],
        ["FM-S-04", "共享", "Agent 冲突", "diff 非空", "转人工闸：矛盾留档"],
        ["FM-S-05", "共享", "产出互斥", "diff 非空", "阻断：两版并存"],
        ["FM-P-01", "person", "幻觉填充", "无落档检出", "阻断：退回"],
        ["FM-P-02", "person", "公关蒸馏", "词表命中", "降级：标 needs_review"],
        ["FM-P-03", "person", "语录复读", "重合度读数", "降级：移事实层"],
        ["FM-P-04", "person", "语料泄漏", "已检-在语料内", "阻断：测试集作废"],
        ["FM-M-01", "method", "触发不准", "诱饵命中>0", "阻断晋级"],
        ["FM-M-02", "method", "术语壁垒", "I 段判项 fail", "降级：重写"],
        ["FM-M-03", "method", "跨技能混淆", "decoy fail", "阻断：不晋级"],
    ]
    bad_wishy = [list(r) for r in good_rows]
    bad_wishy[0][4] = "视情况处理"
    bad_track = [list(r) for r in good_rows]
    bad_track[9][1] = "person"
    cases.append(("FM_pass", fm_entries_discipline(good_rows) == [], True))
    cases.append(("FM_bite_wishy", any("不确定措辞" in p for p in fm_entries_discipline(bad_wishy)), True))
    cases.append(("FM_bite_track", any("不匹配" in p for p in fm_entries_discipline(bad_track)), True))
    cases.append(("FM_bite_short", any("＜基线" in p for p in fm_entries_discipline(good_rows[:3])), True))

    # 看板实例判据（内存路径不可用＝用临时目录语义交 ST-5 样本跑通，此处断纯词表侧）
    cases.append(("BOARD_cols_pass", state_vocab_closed_ok(("待校准", "归档区"), BOARD_COLUMNS), True))
    cases.append(("BOARD_cols_bite", state_vocab_closed_ok(("已核",), BOARD_COLUMNS), False))

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
    # FC-5 实装层：bundle 实例识别（两键在场＝bundle 记录；单层记录不入扫描）
    cases.append(("FC5L_bundle_detect", bundle_layers(iso) and not bundle_layers({"persona": {}}), True))

    # 黄-2 收口：看板正文状态 token 扫描（词表内/字段名放／私扩咬）
    board_good = "## 人工闸结论\n\n- 状态迁移到 `active`，产物级 `needs_review` 清零；字段 `证据等级` 随动。\n"
    board_bad = "## 人工闸结论\n\n- 人工闸记录：S1 产物面全部 `彻底完成`，状态迁移到 `已核`。\n"
    cases.append(("Y2_board_pass", state_token_scan(board_good, BOARD_STATE_LINE_KEY, STATE_WORDS, False) == [], True))
    cases.append(("Y2_board_bite", state_token_scan(board_bad, BOARD_STATE_LINE_KEY, STATE_WORDS, False) != [], True))
    # 黄-2 收口：AC-5 词表声明句扫描（全等放／私扩「已核」咬／缺值咬）
    vocab_good = "基线闭集（与 FC-4 注册位逐字全等）：`needs_review`／`active`／`归档区`／`待校准`／`未验`／`受限`。"
    vocab_bad = "基线闭集（与 FC-4 注册位逐字全等）：`needs_review`／`active`／`归档区`／`待校准`／`未验`／`受限`／`已核`。"
    vocab_short = "基线闭集（与 FC-4 注册位逐字全等）：`needs_review`／`active`／`归档区`／`待校准`／`未验`。"
    cases.append(("Y2_vocab_pass", state_token_scan(vocab_good, VOCAB_LINE_KEY, STATE_WORDS, True) == [], True))
    cases.append(("Y2_vocab_bite_extra", state_token_scan(vocab_bad, VOCAB_LINE_KEY, STATE_WORDS, True) != [], True))
    cases.append(("Y2_vocab_bite_missing", state_token_scan(vocab_short, VOCAB_LINE_KEY, STATE_WORDS, True) != [], True))

    # ST-6／ST-7 互斥 IR 字段互检：无对方字样放／串味咬
    cases.append(("ST6_pass", ir_term_hits("## persona-IR 五层\n表达DNA／心智模型／决策启发式／反模式／诚实边界", PERSON_FORBIDDEN_IR_TERMS) == [], True))
    cases.append(("ST6_bite", ir_term_hits("## persona-IR 五层\n第六节 执行步骤：1/2/3", PERSON_FORBIDDEN_IR_TERMS) != [], True))
    cases.append(("ST7_pass", ir_term_hits("## technique-IR RIA++ 六段\nR 原文／I 诠释／A1 案例／A2 触发场景／E 执行步骤／B 边界", METHOD_FORBIDDEN_IR_TERMS) == [], True))
    cases.append(("ST7_bite", ir_term_hits("## technique-IR 六段\n补一节 表达 DNA 摘录", METHOD_FORBIDDEN_IR_TERMS) != [], True))

    # GS-1/GS-2 gate_source：白名单放／互套咬（双向）
    cases.append(("GS1_pass", gate_source_hits("person", "盲评rubric") == [], True))
    cases.append(("GS1_bite", gate_source_hits("person", "机械断言") != [], True))
    cases.append(("GS2_pass", gate_source_hits("method", "留出集") == [], True))
    cases.append(("GS2_bite", gate_source_hits("method", "人工锚点卡") != [], True))

    # GS S3 批配对咬放：person 扩值「格式检查表」放／method 侧咬；method 补齐「边缘诚实度」放／person 侧咬；
    # 「泄漏检查」两轨共有词两侧均放（互斥性由专属词承载）
    cases.append(("GS1x_pass_fmt", gate_source_hits("person", "格式检查表") == [], True))
    cases.append(("GS2x_bite_fmt", gate_source_hits("method", "格式检查表") != [], True))
    cases.append(("GS2x_pass_edge", gate_source_hits("method", "边缘诚实度") == [], True))
    cases.append(("GS1x_bite_edge", gate_source_hits("person", "边缘诚实度") != [], True))
    cases.append(("GS_shared_leak_both_ok",
                  gate_source_hits("person", "泄漏检查") == [] and gate_source_hits("method", "泄漏检查") == [], True))
    # GS 词表在场性（扩值后闭集基数：person 六值／method 六值·均无重复）
    cases.append(("GS_vocab_sizes", len(set(PERSON_GATE_WHITELIST)) == 6 and len(set(METHOD_GATE_WHITELIST)) == 6, True))
    # GS 实装读取部件（内存空基面＝空扫描合法态；实例记录配对咬放经 _verification_records 读盘侧由仓内模式承载）
    cases.append(("GS3_unknown_track_bite", any(h.startswith("未知轨") for h in gate_source_hits("bundle", "盲评rubric")), True))

    # GS-4 校准一致性：κ 达标＋校准态放／缺 κ 仍校准态咬／不一致咬
    good_kappa = {"点值": 0.7, "区间下界": 0.62}
    weak_kappa = {"点值": 0.65, "区间下界": 0.55}
    cases.append(("GS4_pass", calibration_consistent("校准态", good_kappa), True))
    cases.append(("GS4_pass_pending", calibration_consistent("待校准", None), True))
    cases.append(("GS4_bite_missing", calibration_consistent("校准态", None), False))
    cases.append(("GS4_bite_inconsistent", calibration_consistent("校准态", weak_kappa), False))

    # GS-4 S0b 转实装挂接层配对咬放（判据本体＝既有 calibration_consistent 样本复用，不重复造判据）：
    # 在场一致放／在场不一致咬／κ 置 null 受限元组待校准放／κ 置 null 仍校准态咬／状态越闭集咬
    cases.append(("GS4I_pass", _gs4_tuple_obj_problems("t.json", {"κ点值": 0.7, "κ区间下界": 0.62,
                  "calibration_state": "校准态"}) == [], True))
    cases.append(("GS4I_bite_inconsistent", _gs4_tuple_obj_problems("t.json", {"κ点值": 0.65,
                  "κ区间下界": 0.55, "calibration_state": "校准态"}) != [], True))
    cases.append(("GS4I_nullkappa_pending_pass", _gs4_tuple_obj_problems("t.json", {"κ点值": None,
                  "κ区间下界": None, "calibration_state": "待校准"}) == [], True))
    cases.append(("GS4I_nullkappa_calibrated_bite", _gs4_tuple_obj_problems("t.json", {"κ点值": None,
                  "κ区间下界": None, "calibration_state": "校准态"}) != [], True))
    cases.append(("GS4I_state_outside_bite", _gs4_tuple_obj_problems("t.json", {"κ点值": 0.7,
                  "κ区间下界": 0.62, "calibration_state": "已校准"}) != [], True))
    cases.append(("GS4I_threshold_registered", KAPPA_THRESHOLD == 0.6, True))

    # 词表本体在场（BW-1/BW-2 当期实装判据）：正咬反放自证
    cases.append(("VOCAB_pass", vocab_body_present(ROLEPLAY_BANNED_WORDS), True))
    cases.append(("VOCAB_bite_empty", vocab_body_present(()), False))
    cases.append(("VOCAB_bite_blank", vocab_body_present(("  ",)), False))

    # ===== S4 批配对咬放 =====

    # ST-8 规范表四节闭集：齐备放／缺节咬／改名咬＋关键引用行缺失咬
    s8_good = ("## 适用范围\nx\n## 节闭集表\nx\n## 声明措例\n"
               "宁可生成一个诚实标注局限的 60 分产物，也不要一个看似完美的 90 分造假产物\n"
               "## 量纲与机检落点\nAC-1 AC-2 VA-S-01")
    s8_missing = "## 适用范围\nx\n## 节闭集表\nx\n## 声明措例\nx"
    s8_rename = "## 适用范围\nx\n## 节闭集表\nx\n## 声明措辞\nx\n## 量纲与机检落点\nx"
    cases.append(("ST8_pass", section_diff(spec_sections(s8_good), SPEC_FOUR_SECTIONS) == (set(), set()), True))
    cases.append(("ST8_bite_missing", section_diff(spec_sections(s8_missing), SPEC_FOUR_SECTIONS) != (set(), set()), True))
    cases.append(("ST8_bite_rename", section_diff(spec_sections(s8_rename), SPEC_FOUR_SECTIONS) != (set(), set()), True))
    cases.append(("ST8refs_pass", spec_missing_key_refs(s8_good, SPEC_KEY_REFS["perspective-spec"]) == [], True))
    cases.append(("ST8refs_bite", spec_missing_key_refs("## 适用范围\n无引用", SPEC_KEY_REFS["perspective-spec"]) != [], True))

    # ST-3 转实装层：perspective 节头去空白归一放／带空格形态同判放／缺层咬／串层咬
    p_good = "## 表达DNA\nx\n## 心智模型\nx\n## 决策启发式\nx\n## 反模式\nx\n## 诚实边界\nx"
    p_space = "## 表达 DNA\nx\n## 心智模型\nx\n## 决策启发式\nx\n## 反模式\nx\n## 诚实边界\nx"
    p_short = "## 表达DNA\nx\n## 心智模型\nx\n## 反模式\nx\n## 诚实边界\nx"
    p_mix = p_good + "\n## 执行步骤\nx"
    cases.append(("ST3I_pass", section_diff(perspective_head_sections(p_good), PERSPECTIVE_SECTIONS) == (set(), set()), True))
    cases.append(("ST3I_space_pass", section_diff(perspective_head_sections(p_space), PERSPECTIVE_SECTIONS) == (set(), set()), True))
    cases.append(("ST3I_bite_missing", section_diff(perspective_head_sections(p_short), PERSPECTIVE_SECTIONS) != (set(), set()), True))
    cases.append(("ST3I_bite_mix", section_diff(perspective_head_sections(p_mix), PERSPECTIVE_SECTIONS) != (set(), set()), True))

    # ST-3 technique 归一化口径：「R 原文」全形态放／裸段名「R」放／「R 原文X」改名咬／缺段咬／非法头咬
    t_full = ("R 原文", "I 诠释", "A1 案例", "A2 触发场景", "E 执行步骤", "B 边界")
    t_bare = ("R", "I", "A1", "A2", "E", "B")
    t_rename = ("R 原文X", "I 诠释", "A1 案例", "A2 触发场景", "E 执行步骤", "B 边界")
    t_missing = ("R 原文", "I 诠释", "A1 案例", "A2 触发场景", "E 执行步骤")
    ex1 = technique_segment_normalize(t_full)
    ex2 = technique_segment_normalize(t_bare)
    ex3 = technique_segment_normalize(t_rename)
    ex4 = technique_segment_normalize(t_missing)
    cases.append(("ST3T_norm_pass", ex1 == (set(), set(), []), True))
    cases.append(("ST3T_bare_pass", ex2 == (set(), set(), []), True))
    cases.append(("ST3T_rename_bite", ex3[2] != [], True))
    cases.append(("ST3T_missing_bite", ex4[1] != set(), True))
    cases.append(("ST3T_fields_pass",
                  card_fields_closed_ok({"出处": "s1", "触发": "t", "步骤": "p", "边界": "b", "验证状态": "未验"}), True))
    cases.append(("ST3T_fields_bite",
                  card_fields_closed_ok({"出处": "s1", "自造字段": "x"}), False))

    # BW-5 矛盾平滑：声明行两行放／缺行咬；词表本体放／空咬；产物命中咬／无命中放
    cases.append(("BW5a_pass", decl_rows_missing("内部矛盾不平滑：矛盾是深度的重要信号", PERSON_CONTRADICTION_DECL_ROWS) == [], True))
    cases.append(("BW5a_bite", decl_rows_missing("防编护栏节（无条款）", PERSON_CONTRADICTION_DECL_ROWS) != [], True))
    cases.append(("BW5b_vocab_pass", vocab_body_present(SMOOTH_PHRASE_VOCAB) and len(set(SMOOTH_PHRASE_VOCAB)) == 4, True))
    cases.append(("BW5b_bite_hit", blunt_hits("该人物思想毫无矛盾、自洽无冲突。", SMOOTH_PHRASE_VOCAB) != [], True))
    cases.append(("BW5b_pass_nohit", blunt_hits("其早期与晚期立场存在张力，按原样入档。", SMOOTH_PHRASE_VOCAB) == [], True))

    # 产物正文门禁实跑位（BW-1/BW-2 词表消费接产物枚举＝根条目＋pending/ 一层口径）：合成条目正文 放／咬 配对
    body_clean = {"obj-a-perspective": {"SKILL.md": "他用这套框架分析决策；证据不足维度写证据不足。",
                                        "registration.md": "注册记录：语料门槛登记。"},
                  "pending/obj-b-perspective": {"SKILL.md": "其立场张力按原样入档，来源态逐条标注。"}}
    body_dirty1 = {"obj-a-perspective": {"SKILL.md": "接下来我以他的名义作答，给出结论。"},
                   "pending/obj-b-perspective": {"SKILL.md": "正常正文。"}}
    body_dirty2 = {"obj-a-perspective": {"SKILL.md": "正常正文。"},
                   "pending/obj-b-perspective": {"SKILL.md": "他必然会否决这个方案，无需再看证据。"}}
    h1p, n1p = word_gate_hits(body_clean, ROLEPLAY_BANNED_WORDS)
    h1b, n1b = word_gate_hits(body_dirty1, ROLEPLAY_BANNED_WORDS)
    h2b, n2b = word_gate_hits(body_dirty2, BLUNT_ASSERTION_WORDS)
    cases.append(("BW1body_pass", h1p == [], True))
    cases.append(("BW1body_bite", h1b != [], True))
    cases.append(("BW2body_pass", word_gate_hits(body_clean, BLUNT_ASSERTION_WORDS)[0] == [], True))
    cases.append(("BW2body_bite", h2b != [], True))
    cases.append(("BODY_scan_count", n1p == 3 and n1b == 2 and n2b == 2, True))

    # BW-6 README 置顶：置顶齐备放／表在 H2 后咬／缺声明行咬／缺行名咬／声明重复咬
    bw6_good = ("# t\n\n| 维度 | fuxi-skill | nuwa-skill | cangjie-skill |\n|---|---|---|---|\n"
                "| 对象 | a | b | c |\n| 产物 | d | e | f |\n| 验证 | g | h | i |\n\n"
                "与前序同名旧物无继承关系。\n\n## 目录地图\nx")
    bw6_after_h2 = "# t\n\n## 目录地图\nx\n\n| 对象 | nuwa-skill | cangjie-skill |\n|---|---|---|\n| 产物 | fuxi-skill | y |\n\n与前序同名旧物无继承关系。"
    bw6_nodecl = bw6_good.replace(COMPARISON_NO_INHERIT_DECL, "（无声明）")
    bw6_norows = bw6_good.replace("| 对象 | a | b | c |\n", "").replace("| 产物 | d | e | f |\n", "")
    cases.append(("BW6_pass", readme_table_problems(bw6_good) == [], True))
    cases.append(("BW6_bite_after_h2", any("未置顶" in p for p in readme_table_problems(bw6_after_h2)), True))
    cases.append(("BW6_bite_nodecl", any("声明行命中" in p for p in readme_table_problems(bw6_nodecl)), True))
    cases.append(("BW6_bite_norows", any("维度行名" in p for p in readme_table_problems(bw6_norows)), True))
    cases.append(("BW6_bite_decl2", any("声明行命中" in p for p in readme_table_problems(bw6_good + "\n" + COMPARISON_NO_INHERIT_DECL)), True))

    # FC-6 active 池条目确认：四字段齐放／缺块咬／产物id 不匹配咬／空字段咬
    conf_ok = {"产物id": "obj-a-perspective", "人工确认引用": "board-x", "提案件引用": "prop-1", "版本审计引用": "commit-1"}
    cases.append(("FC6_pass", pool_entry_confirmed(conf_ok, "obj-a-perspective"), True))
    cases.append(("FC6_bite_id", pool_entry_confirmed(conf_ok, "obj-b-perspective"), False))
    cases.append(("FC6_bite_missing_field", pool_entry_confirmed({"产物id": "obj-a-perspective"}, "obj-a-perspective"), False))
    cases.append(("FC6_bite_blank", pool_entry_confirmed(dict(conf_ok, 人工确认引用="  "), "obj-a-perspective"), False))

    # GS-5 不退化：层名基数达标放／删层咬；基数达标放／缩水咬
    cases.append(("GS5_layers_pass", non_regression_shrunk(len(VALIDATOR_LAYER_NAMES), GS5_BASELINE["层名基数"]) == [], True))
    cases.append(("GS5_layers_bite", non_regression_shrunk(len(VALIDATOR_LAYER_NAMES) - 1, GS5_BASELINE["层名基数"]) != [], True))
    cases.append(("GS5_count_pass", non_regression_shrunk(25, 25) == [], True))
    cases.append(("GS5_count_bite", non_regression_shrunk(24, 25) != [], True))
    cases.append(("GS5_mech_present", "机械断言" in METHOD_GATE_WHITELIST and "格式检查表" in PERSON_GATE_WHITELIST, True))
    cases.append(("GS5_assert基数", len(ASSERTIONS) == GS5_BASELINE["断言编号基数"], True))

    # ===== T5 批配对咬放（FUXI-T5：ST-4 转实装层＋FC-3 产物要素行级侧·内存注入不落仓） =====

    # ST-4 实装层：合法条目 list 块放／未注册字段咬／空 list 咬／随件缺失咬
    tp_good_md = '# t\n\n```json\n[{"用例id": "tp-01", "题面": "q", "期望档位": "有限定", "所属轨": "person", "是否锚点题": false}]\n```\n'
    tp_unknown_md = '# t\n\n```json\n[{"用例id": "tp-02", "自造字段": "x"}]\n```\n'
    tp_empty_md = '# t\n\n```json\n[]\n```\n'
    tp_dict_md = '# t\n\n```json\n{"用例id": "tp-03"}\n```\n'
    good_lists, good_bad = test_prompts_list_blocks(tp_good_md)
    cases.append(("ST4I_pass", good_lists and test_prompt_entries_ok(good_lists[0]), True))
    unknown_lists, _ub = test_prompts_list_blocks(tp_unknown_md)
    cases.append(("ST4I_bite_unknown", unknown_lists and not test_prompt_entries_ok(unknown_lists[0]), True))
    cases.append(("ST4I_bite_emptylist", test_prompts_list_blocks(tp_empty_md)[0] == [], True))
    cases.append(("ST4I_dict_notlist", test_prompts_list_blocks(tp_dict_md)[0] == [], True))
    cases.append(("ST4I_bite_missing", _TEST_PROMPTS_FILE not in {"SKILL.md": "本体件", "registration.md": "注册件"}, True))
    cases.append(("ST4I_tier_bite", not test_prompt_values_ok([{"用例id": "tp-04", "期望档位": "斩钉截铁", "所属轨": "person"}]), True))
    cases.append(("ST4I_track_bite", not test_prompt_values_ok([{"用例id": "tp-05", "期望档位": "有限定", "所属轨": "persona"}]), True))
    cases.append(("ST4I_values_pass", test_prompt_values_ok([{"用例id": "tp-06", "期望档位": "有支持", "所属轨": "method"}]), True))

    # FC-3 产物要素行级侧：内联成对放／去 source_id 咬／去 位置 咬／哨兵形态放
    el_good = {"obj-a-perspective": {"SKILL.md": "- 要素行。`证据等级`=`跨文本推断`·`来源态`=`本人原文`·source_id=`src-01`·位置＝「第三章」\n"}}
    el_noid = {"obj-a-perspective": {"SKILL.md": "- 要素行。`证据等级`=`跨文本推断`·`来源态`=`本人原文`·位置＝「第三章」\n"}}
    el_noloc = {"obj-a-perspective": {"SKILL.md": "- 要素行。`证据等级`=`跨文本推断`·`来源态`=`本人原文`·source_id=`src-01`\n"}}
    el_sentinel = {"obj-a-perspective": {"SKILL.md": "- 要素行。`证据等级`=`模型补全`·`来源态`=`模型推断`·source_id=`model-knowledge`·位置＝「模型内部既有知识，无外部回查位置」\n"}}
    el_nonelem = {"obj-a-perspective": {"SKILL.md": "- 普通正文行，无要素标注字段 token。\n", "test-prompts.md": "`证据等级`=`跨文本推断`·`来源态`=`本人原文`\n"}}
    cases.append(("FC3P_pass", product_element_pair_hits(el_good)[0] == [] and product_element_pair_hits(el_good)[1] == 1, True))
    cases.append(("FC3P_bite_noid", product_element_pair_hits(el_noid)[0] != [], True))
    cases.append(("FC3P_bite_noloc", product_element_pair_hits(el_noloc)[0] != [], True))
    cases.append(("FC3P_sentinel_pass", product_element_pair_hits(el_sentinel)[0] == [], True))
    cases.append(("FC3P_empty_pass", product_element_pair_hits(el_nonelem) == ([], 0), True))

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
    """仓内执行模式：20 项逐项读数＋汇总单列（PASS／FAIL／PENDING_STAGE）。"""
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
