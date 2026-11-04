#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fuxi-skill · harness 非判据共用件（S3 建）。

性质＝交付件本体。本件只放两 validator 共用的**非判据**部件：
文本归一化与哈希、json/jsonl 读盘、报表行格式、字段名 diff 工具、
路径定位、集合统计工具（Jaccard）。
**不含任何判据**：无阈值、无白名单、无 pass/fail 语义（判据各归两
validator 本件与 assert-tool 注册位；闸分离的物理体现＝两 validator
分立脚本＋各自词表，本件不构成第三入口）。

确定性：无随机、无时钟参与读数、无网络；同输入连跑输出全等。

退出码：本件为库件，无独立退出码；selftest 模式仅自证部件确定性，
exit 0＝全等成立，exit 2＝部件异常（fail-closed）。

用法：
    python harness-common.py selftest
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import unicodedata

# ---- 读数闭集（验证记录 `判定` 字段三值，无其他取值；与 validator-catalog 值注册逐字全等）----
READ_PASS = "PASS"
READ_FAIL = "FAIL"
READ_UNVERIFIED = "未验"

# ---- 三臂臂名写死闭集（old／new／without_skill；AC-3 对照臂同一套定义）----
ARMS = ("old", "new", "without_skill")

# ---- 验证记录字段注册表的代码侧镜像（单源＝同目录 validator-catalog.md §二机读注册表；
#      两 validator selftest 均做「注册表↔本元组」双向 diff＝∅ 对账，未注册字段零容忍）----
REPORT_FIELDS = (
    "记录id", "产物id", "所属轨", "层名", "gate_source", "读数", "判定",
    "工件哈希", "预注册件哈希", "裁判家族", "位置对调两跑",
    "calibration_state", "evidence_grade", "control_arm", "leakage_check",
    "时间切分核对行", "run_to_run_5读数", "装载核对",
    "模型标识（声明值）", "局限声明",
)

# ---- 对照组构成表行字段闭集（代码侧镜像＝validator-catalog §三；臂行六字段齐备才出三臂读数）----
ARM_TABLE_FIELDS = ("宿主", "模型标识（声明值）", "工具面", "预算上限", "题集指纹", "臂产物哈希")

_JSON_FENCE_RE = re.compile(r"```json[ \t]*\n(.*?)\n```", re.S)


# ============================================================
# 文本归一化与哈希（泄漏比对两式的公共底座；规程语义不在此，判据在 validator）
# ============================================================

def normalize_text(text: str) -> str:
    """归一化：NFKC（含全半角折叠）＋去空白＋casefold。"""
    folded = unicodedata.normalize("NFKC", text)
    stripped = "".join(folded.split())
    return stripped.casefold()


def sha256_hex(text: str) -> str:
    """utf-8 编码 sha256 十六进制。"""
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def norm_hash(text: str) -> str:
    """归一化哈希＝sha256(归一化文本)。"""
    return sha256_hex(normalize_text(text))


def corpus_chunk_hashes(chunks: "list[str]") -> "set[str]":
    """语料分块归一化哈希集（相等式比对的右值集）。"""
    return {norm_hash(c) for c in chunks if c.strip()}


def question_set_fingerprint(question_texts: "list[str]") -> str:
    """题库指纹＝按文件序逐题归一化哈希拼接后再哈希（防改题校验的对象）。"""
    joined = "\n".join(norm_hash(t) for t in question_texts)
    return sha256_hex(joined)


# ============================================================
# json 读盘／注册表提取（机读件解析；非判据）
# ============================================================

def read_json(path: str):
    """读单个 json 文件（utf-8）；解析异常由调用方按 fail-closed 处置。"""
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: str, obj) -> None:
    """写单个 json 文件（确定性序列化：ensure_ascii=False＋键序固定 sort_keys）。"""
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(obj, handle, ensure_ascii=False, sort_keys=True, indent=2)
        handle.write("\n")


def read_jsonl(path: str) -> "list[dict]":
    """读 jsonl（每行一记录）；空行跳过，非 dict 行由调用方处置。"""
    records: "list[dict]" = []
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def write_jsonl(path: str, records: "list[dict]") -> None:
    """写 jsonl（确定性序列化）。"""
    with open(path, "w", encoding="utf-8") as handle:
        for rec in records:
            handle.write(json.dumps(rec, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


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


def registry_fields_from_catalog(catalog_text: str, want_key: str) -> "tuple[set[str], int]":
    """从 validator-catalog 文本抽 {"字段注册": [...]} 块的指定键列表（返回 (字段集, 失败块数)）。

    want_key＝"字段注册" 时取各块该键并集；供「注册表↔代码镜像」双向 diff 对账部件使用。
    """
    blocks, bad = md_json_blocks(catalog_text)
    names: "set[str]" = set()
    for block in blocks:
        decl = block.get(want_key)
        if isinstance(decl, list):
            names.update(str(n) for n in decl)
    return names, bad


# ============================================================
# 字段名 diff 工具（FC-2 同款双向 diff 的机械对账部件；不内置任何注册表＝判据在外）
# ============================================================

def field_name_diff(used: "set[str]", registry: "set[str]") -> "tuple[set, set]":
    """返回 (实例侧未注册多出集, 注册表未使用缺失集)；两集皆空＝diff＝∅。"""
    return (used - registry, registry - used)


# ============================================================
# 报表行格式（产物报表/验证记录行的统一格式；无聚合总分概念——报表无总分字段）
# ============================================================

def format_report_line(layer: str, reading: str, judgment: str,
                       calibration_state: str = "") -> str:
    """统一报表行：`层名 <TAB> 读数 <TAB> 判定 [<TAB> calibration_state=…]`。

    judge 层调用时强制随附 calibration_state 当前值（fail-closed 并列打印口径由调用方保证）。
    """
    if calibration_state:
        return "%s\t%s\t%s\tcalibration_state=%s" % (layer, reading, judgment, calibration_state)
    return "%s\t%s\t%s" % (layer, reading, judgment)


def format_d12_line(reading: str, judgment: str) -> str:
    """D12 排他性辨认正确率独立报告行（该行只进报表行，不并入任何层 fail/pass 判定）。"""
    return "D12排他性辨认正确率\t%s\t%s" % (reading, judgment)


def record_skeleton() -> "dict[str, str]":
    """验证记录字段骨架（REPORT_FIELDS 全集、缺省值在场；validator 写记录时先取骨架再覆值）。"""
    return {field: "" for field in REPORT_FIELDS}


# ============================================================
# 路径定位（过程域证据面＝验证记录与对照组构成表落盘路径；注册面见 validator-catalog）
# ============================================================

def evidence_harness_dir(base_dir: str = "") -> str:
    """验证记录与对照组构成表落盘路径定位＝<仓根>/.collab/evidence/harness/。

    base_dir 缺省＝自本件位置静态上溯三级（交付面 gates/→fuxi-skill→agent-skills→仓根）。
    """
    if base_dir:
        return os.path.join(base_dir, ".collab", "evidence", "harness")
    here = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.normpath(os.path.join(here, os.pardir, os.pardir, os.pardir))
    return os.path.join(repo_root, ".collab", "evidence", "harness")


# ============================================================
# 集合统计部件（×5 锚点复现率两两 Jaccard 均值；无阈值＝统计口径不在此判）
# ============================================================

def jaccard(a: "set[str]", b: "set[str]") -> float:
    """两集合 Jaccard 系数；双空集约定为 1.0。"""
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b)


def pairwise_jaccard_mean(sets: "list[set[str]]") -> float:
    """集合列表两两 Jaccard 均值（样本＜2 返回 0.0，由调用方记未验）。"""
    if len(sets) < 2:
        return 0.0
    vals = [jaccard(a, b) for i, a in enumerate(sets) for b in sets[i + 1:]]
    return sum(vals) / len(vals)


def date_key(iso_date: str) -> int:
    """ISO 日期（YYYY-MM-DD）→ 单调日期键（确定性，无时钟参与读数）。格式不合法返回 -1。"""
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", iso_date.strip())
    if not m:
        return -1
    y, mo, d = (int(g) for g in m.groups())
    if not (1 <= mo <= 12 and 1 <= d <= 31):
        return -1
    return y * 372 + mo * 31 + d


# ============================================================
# selftest（部件自证：确定性＋归一化/哈希/指纹/行格式/路径定位基本活性）
# ============================================================

def _selftest_cases() -> "list[tuple[str, bool, bool]]":
    """返回 (用例名, 判据结果, 期望结果) 列表（与断言工具 selftest 同款配对形态）。"""
    cases: "list[tuple[str, bool, bool]]" = []

    # 归一化：全半角折叠＋去空白＋casefold 放／差异文本不归同
    cases.append(("NORM_fullwidth_fold", normalize_text("Ｈｅｌｌｏ Ｗｏｒｌｄ") == normalize_text("hello world"), True))
    cases.append(("NORM_keep_distinct", normalize_text("甲案") != normalize_text("乙案"), True))

    # 归一化哈希稳定＋指纹可复现
    h1 = norm_hash(" 测试 题目 Alpha ")
    h2 = norm_hash("测试题目alpha")
    cases.append(("HASH_norm_stable", h1 == h2, True))
    fp1 = question_set_fingerprint(["题一", "题二"])
    fp2 = question_set_fingerprint(["题一", "题二"])
    fp3 = question_set_fingerprint(["题一", "题二改"])
    cases.append(("FINGERPRINT_reproducible", fp1 == fp2, True))
    cases.append(("FINGERPRINT_changed_differs", fp1 != fp3, True))

    # 分块哈希集：等值分块同哈希
    ch = corpus_chunk_hashes(["段落 甲", "段落乙"])
    cases.append(("CHUNK_norm_hit", norm_hash("段落甲") in ch, True))

    # 字段注册表提取＋双向 diff 部件
    sample = ('```json\n{"字段注册": ["a", "b", "c"]}\n```\n```json\n{"字段注册": ["c", "d"]}\n```')
    got, bad = registry_fields_from_catalog(sample, "字段注册")
    cases.append(("REGISTRY_extract", got == {"a", "b", "c", "d"} and bad == 0, True))
    d1 = field_name_diff({"a", "b", "c", "d"}, {"a", "b", "c", "d"})
    d2 = field_name_diff({"a", "自造"}, {"a", "b"})
    cases.append(("REGDIFF_pass", d1 == (set(), set()), True))
    cases.append(("REGDIFF_bite", d2 != (set(), set()), True))

    # REPORT_FIELDS 骨架字段全集在场
    sk = record_skeleton()
    cases.append(("SKELETON_fields", set(sk) == set(REPORT_FIELDS), True))

    # 报表行格式：judge 行带 calibration_state、普通行不带；无总分字段
    line_j = format_report_line("盲评rubric", "四维均值 3.6/5", "PASS", "待校准")
    line_p = format_report_line("格式检查表", "禁语命中=0", "PASS")
    cases.append(("LINE_calib_pair", "calibration_state=待校准" in line_j, True))
    cases.append(("LINE_plain", line_p == "格式检查表\t禁语命中=0\tPASS", True))
    cases.append(("D12_line_indep", format_d12_line("辨认正确率 80%（统计口径：2AFC 双跑均值；样本量 10；一致性系数 0.81）", "未验").startswith("D12排他性辨认正确率"), True))

    # 统计部件：Jaccard＋日期键
    cases.append(("JACCARD", jaccard({"a", "b"}, {"b", "c"}) == 1 / 3 and pairwise_jaccard_mean([{"a"}, {"a"}, {"b"}]) > 0, True))
    cases.append(("DATEKEY", date_key("2100-10-30") > date_key("2100-01-01") and date_key("bad") == -1, True))

    # json/jsonl 读盘确定性序列化往返（内存对象→tmp 路径由调用方负责，此处验字符串确定性）
    s1 = json.dumps({"b": 1, "a": "甲"}, ensure_ascii=False, sort_keys=True)
    s2 = json.dumps({"a": "甲", "b": 1}, ensure_ascii=False, sort_keys=True)
    cases.append(("JSON_deterministic", s1 == s2, True))

    return cases


def run_selftest() -> int:
    failures = 0
    total = 0
    for name, actual, expected in _selftest_cases():
        total += 1
        if actual != expected:
            failures += 1
            print("selftest FAIL %s：判据返回 %r，期望 %r" % (name, actual, expected))
    print("harness-common selftest 用例 %d／反常 %d" % (total, failures))
    return 2 if failures else 0


def main(argv: "list[str]") -> int:
    if len(argv) == 1 and argv[0] == "selftest":
        return run_selftest()
    sys.stderr.write("usage error: 用法＝python harness-common.py selftest（库件，无其他参数）\n")
    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按工具错误码，不得吞成 0
        sys.stderr.write("tool error: %s\n" % exc)
        raise SystemExit(2)
