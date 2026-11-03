#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fuxi-skill · S0b 人工锚点测量工具（判分段·确定性·S0b 建）。

性质＝交付件本体。消费批次标注工件（人工标注＝生成段落盘件，本件只判分）出
判据行读数与交付元组。判据行闭集（四行族）：
    ①软门κ／硬门κ 各一行：点值＋bootstrap 下界双条件 ≥0.6（R4；两套标注独立、
      两个 κ 各自计算不合一，R12；两两读数按档位分列不互充）；
    ②硬门侧「断言结果 vs 人工金标」一致率行（Wilson 单侧 95% 下界）＋FP/FN 分解行
      （读数承接硬门判定语义；报表标注「不替代两 κ 义务」；达标线未注册→当期判定记未验）；
    ③题数检行：实做题数＜下限→对应 κ 行转「题量受限」登记读数（R2，记未验不记绿）；
      加题累计越上限或标注读数越预算上限→超限检行如实报超限（FAIL，咬不静默）；
    ④增量保留口径行（R15 定稿）：κ 在旧∪新标注并集上重算、旧标注不作废（代码路径单义）；
      作废重标唯一触发＝标注规范哈希变更（并在读数行注明）。
交付元组产出（R9 五字段＋calibration_state）：calibration_state 由 κ 双条件自动驱动
（校准态／待校准），不得人工填写（R11）→落批次工件目录 anchor-tuple-soft.json／
anchor-tuple-hard.json（软/硬两元组分文件；落盘路径注册＝同目录 validator-catalog §三）。

结构体例＝两 validator 同款：非判据共用件＝同目录 `harness-common.py`（复用）；
词表/闭集纯数据常量 import 同目录 `assert-tool.py` 注册位（单源，不复制）。
生成段／判分段分离：本件＝判分段，只对落盘标注工件做确定性判定。

预注册数值包常量（九个；注册面＝validator-catalog §四表 S0b 行；一经注册不得变更，
中途变更走独立提案）：
    QUESTIONS_PER_OBJ_PER_TRACK=8（每对象每轨起步题数）／MIN_QUESTIONS=5（题数下限）／
    ADDQ_CAP=30（每对象累计加题上限）／BUDGET_CAP=128（标注读数预算上限）／
    OBJECTS=2（预算测算前提恒 2）／KAPPA_THRESHOLD=0.6（达标线，import 自 assert-tool 不复制）／
    ONE_SIDED_Z=1.645（单侧 95%）／BOOT_ITERS=5000（bootstrap 百分位迭代数）／
    BOOT_SEED=20261031（bootstrap 种子预注册值，确定性可复跑）。

确定性：无时钟参与读数、无网络；随机＝bootstrap 仅用预注册种子；同输入连跑输出逐字节全等。

退出码闭集（三值，无其他取值）：
    0 无 fail（未验行不算 fail 不算 pass，汇总单列，不拉码）
    1 任一判据行 FAIL（超限/κ 未达标/元组对账不一致等如实咬）
    2 工具自身错误（用法错／环境错／输入 json 解析失败，fail-closed 不得吞成 0）

用法：
    python s0b-kappa.py <batch_dir>   # 判分段：对批次标注工件目录出判据行＋写交付元组
    python s0b-kappa.py selftest      # 自证：内存配对＋系统临时目录合成批次（不落仓）咬放配对
"""

from __future__ import annotations

import importlib.util
import json
import math
import os
import random
import sys

# ---- 退出码闭集 ----
EXIT_GREEN = 0
EXIT_FAIL = 1
EXIT_TOOL_ERROR = 2


def _load_sibling(mod_name: str, filename: str):
    """按文件位置装载同目录兄弟件（kebab 文件名非合法模块名，走 importlib）。"""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    spec = importlib.util.spec_from_file_location(mod_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


HC = _load_sibling("fuxi_harness_common", "harness-common.py")
AT = _load_sibling("fuxi_assert_tool", "assert-tool.py")

READ_PASS = HC.READ_PASS
READ_FAIL = HC.READ_FAIL
READ_UNVERIFIED = HC.READ_UNVERIFIED

# ---- 预注册数值包常量（九个；注册面＝validator-catalog §四表 S0b 行）----
QUESTIONS_PER_OBJ_PER_TRACK = 8   # 每对象每轨起步题数
MIN_QUESTIONS = 5                 # 题数下限（不足转「题量受限」登记读数）
ADDQ_CAP = 30                     # 每对象累计加题上限
BUDGET_CAP = 128                  # 标注读数预算上限
OBJECTS = 2                       # 预算测算前提恒 2（两轨×两对象口径）
KAPPA_THRESHOLD = AT.KAPPA_THRESHOLD   # 达标线单源＝assert-tool 注册位（不复制）
ONE_SIDED_Z = 1.645               # 单侧 95% 置信水平 z 值
BOOT_ITERS = 5000                 # κ bootstrap 百分位迭代数
BOOT_SEED = 20261031              # bootstrap 种子（预注册值，确定性可复跑）

# ---- 批次标注工件目录输入面文件闭集（缺文件＝对应读数记未验，fail-closed 不推定绿）----
BATCH_FILES = {
    "labels_soft": "anchor-labels-soft.json",   # 软门两套标注（R12 独立·两 κ 不合一）
    "labels_hard": "anchor-labels-hard.json",   # 硬门两套标注（同上）
    "gold": "gold-assertions.json",             # 人工金标 vs 断言结果对（硬门侧增量行对象）
    "tuple_out": "anchor-tuple-out.json",       # 可选件：已存在则对账（缺位＝合法）
}

CALIBRATION_STATES = AT.CALIBRATION_STATES   # 词表单源＝assert-tool 注册位（不复制）
CALIBRATED = CALIBRATION_STATES[0]           # 校准态
PENDING_CAL = CALIBRATION_STATES[1]          # 待校准

TUPLE_OUT_FILES = {"labels_soft": "anchor-tuple-soft.json",
                   "labels_hard": "anchor-tuple-hard.json"}


# ============================================================
# 统计部件（纯函数·确定性）
# ============================================================

def wilson_lower(k: int, n: int, z: float = ONE_SIDED_Z) -> float:
    """比例的单侧 95% Wilson 置信下限（n≤0 返回 0.0，fail-closed）。"""
    if n <= 0:
        return 0.0
    p = float(k) / float(n)
    z2 = z * z
    centre = p + z2 / (2.0 * n)
    margin = z * math.sqrt(p * (1.0 - p) / float(n) + z2 / (4.0 * float(n) * float(n)))
    return (centre - margin) / (1.0 + z2 / float(n))


def cohens_kappa(labels_a: "list[str]", labels_b: "list[str]") -> float:
    """Cohen's kappa（名义类别两标注一致性）。长度不等或为空＝0.0（fail-closed）。
    退化情形（pe≥1，两标注恒同常数）：po≥1 记 1.0，否则记 0.0。
    """
    if not labels_a or not labels_b or len(labels_a) != len(labels_b):
        return 0.0
    n = float(len(labels_a))
    agree = sum(1 for a, b in zip(labels_a, labels_b) if a == b)
    po = agree / n
    pa: "dict[str, int]" = {}
    pb: "dict[str, int]" = {}
    for a in labels_a:
        pa[a] = pa.get(a, 0) + 1
    for b in labels_b:
        pb[b] = pb.get(b, 0) + 1
    pe = sum((pa.get(c, 0) / n) * (pb.get(c, 0) / n) for c in set(pa) | set(pb))
    if pe >= 1.0:
        return 1.0 if po >= 1.0 else 0.0
    return (po - pe) / (1.0 - pe)


def bootstrap_kappa_lower(labels_a: "list[str]", labels_b: "list[str]",
                          iters: int = BOOT_ITERS, seed: int = BOOT_SEED) -> float:
    """κ 的单侧 95% 置信下限＝bootstrap 百分位法（预注册种子·有放回重采样·取下侧 5% 分位）。
    确定性：同输入＋同种子连跑逐值全等；样本＜2 返回 0.0（fail-closed）。
    """
    n = len(labels_a)
    if n < 2 or n != len(labels_b):
        return 0.0
    rng = random.Random(seed)
    values: "list[float]" = []
    for _ in range(iters):
        idxs = [rng.randrange(n) for _ in range(n)]
        values.append(cohens_kappa([labels_a[i] for i in idxs], [labels_b[i] for i in idxs]))
    values.sort()
    rank = min(int(0.05 * iters), iters - 1)
    return values[rank]


def retest_kappa(old_pairs: "list[tuple[str, str]]", new_pairs: "list[tuple[str, str]]") -> float:
    """增量保留口径（R15 定稿）：κ 在旧∪新标注并集上重算，旧标注不作废（代码路径单义）。
    入参＝(标注甲, 标注乙) 题对列表；并集＝旧在前、新在后顺序拼接后整体计算。
    """
    union = list(old_pairs) + list(new_pairs)
    return cohens_kappa([p[0] for p in union], [p[1] for p in union])


# ============================================================
# 标注工件解析与并集（纯函数·确定性）
# ============================================================

def label_pairs_from_unit(unit: "dict") -> "list[tuple[str, str, str]]":
    """标注单元（{"标注者甲": {题目id: 档位}, "标注者乙": {...}}）
    → 按题目 id 排序对齐的 (甲档位, 乙档位, 题目id) 列表；两标注者未共题不入列（不猜测）。
    """
    mine = unit.get("标注者甲", {})
    other = unit.get("标注者乙", {})
    if not isinstance(mine, dict) or not isinstance(other, dict):
        return []
    out: "list[tuple[str, str, str]]" = []
    for q in sorted(mine):
        if q in other:
            out.append((str(mine[q]), str(other[q]), str(q)))
    return out


def merge_history(data: dict) -> "tuple[list, str, bool]":
    """当前标注＋历史标注并集（增量保留口径：规范哈希一致才并入历史；
    哈希不一致＝唯一作废重标触发，旧标注不入并集并在读数行注明）。
    返回 (并集题对列表, 当前规范哈希, 历史是否因规范哈希变更作废)。
    """
    spec = str(data.get("规范哈希", ""))
    pairs = label_pairs_from_unit(data.get("标注单元", {}))
    voided = False
    for block in data.get("历史标注", []):
        if str(block.get("规范哈希", "")) == spec:
            pairs = label_pairs_from_unit(block.get("标注单元", {})) + pairs
        else:
            voided = True
    return (pairs, spec, voided)


def kappa_track(data, track_name: str) -> "tuple[str, str, list, str, str, str, float, float]":
    """单轨（软门/硬门）标注工件 → 判据行①读数。

    三态：缺工件＝未验；配对为空＝未验；题数＜下限＝未验＋「题量受限」登记读数（R2）；
    题数达标＝κ 点值＋bootstrap 下界双条件 ≥ 达标线→校准态（PASS），否则待校准（FAIL 如实显示）。
    返回 (判定, 读数, 并集题对, 受限登记, calibration_state, 轨道名, κ点值, κ下界)；
    κ 未产出时点值/下界以 float('nan') 表示（元组落盘置 null）。
    """
    nan = float("nan")
    if data is None:
        return (READ_UNVERIFIED, "%s标注工件不在场（规程在场待数据·fail-closed）" % track_name,
                [], "", PENDING_CAL, track_name, nan, nan)
    pairs, _spec, voided = merge_history(data)
    if not pairs:
        return (READ_UNVERIFIED, "%s标注配对为空（两标注者无共题）" % track_name,
                [], "", PENDING_CAL, track_name, nan, nan)
    n = len(pairs)
    if n < MIN_QUESTIONS:
        tag = "题量受限（实做 %d＜下限 %d·登记读数）" % (n, MIN_QUESTIONS)
        return (READ_UNVERIFIED, "%s%s·κ 读数不产出（元组 κ 字段置 null）" % (track_name, tag),
                pairs, tag, PENDING_CAL, track_name, nan, nan)
    la = [p[0] for p in pairs]
    lb = [p[1] for p in pairs]
    point = cohens_kappa(la, lb)
    lower = bootstrap_kappa_lower(la, lb)
    calibrated = point >= KAPPA_THRESHOLD and lower >= KAPPA_THRESHOLD
    state = CALIBRATED if calibrated else PENDING_CAL
    note = "·历史标注因规范哈希变更作废不入并集（唯一作废触发·独立提案留痕）" if voided else ""
    reading = ("%sκ点值 %.4f·bootstrap 下界 %.4f（统计口径：百分位 %d 次·种子 %d·单侧 95%%；"
               "样本量 %d；一致性系数见本行）·双条件≥%.1f→%s%s"
               % (track_name, point, lower, BOOT_ITERS, BOOT_SEED, n, KAPPA_THRESHOLD,
                  "校准态" if calibrated else "待校准", note))
    return (READ_PASS if calibrated else READ_FAIL, reading, pairs, "", state, track_name, point, lower)


def gold_agreement_row(gold) -> "tuple[str, str]":
    """判据行②：硬门侧「断言结果 vs 人工金标」一致率（Wilson 单侧 95% 下界）＋FP/FN 分解行。

    该读数承接硬门判定语义，报表标注「不替代两 κ 义务」（两 κ 本体零触动）；
    一致率达标线未注册→当期判定记未验（不假绿）。
    """
    if gold is None:
        return (READ_UNVERIFIED, "金标对工件不在场（规程在场待数据·fail-closed）")
    pairs = gold.get("配对", [])
    if not pairs:
        return (READ_UNVERIFIED, "金标配对为空（记未验）")
    n = len(pairs)
    agree = 0
    fp = 0
    fn = 0
    for rec in pairs:
        want = str(rec.get("人工金标", ""))
        got = str(rec.get("断言结果", ""))
        if want == got:
            agree += 1
        elif got == "PASS" and want == "FAIL":
            fp += 1
        elif got == "FAIL" and want == "PASS":
            fn += 1
    rate = agree / float(n)
    lower = wilson_lower(agree, n)
    return (READ_UNVERIFIED,
            "金标一致率 %.0f%%（统计口径：断言结果与人工金标逐题对拍；样本量 %d；"
            "一致性系数 Wilson 单侧95%%下界 %.4f）·FP=%d FN=%d·承接硬门判定语义·不替代两 κ 义务"
            % (rate * 100, n, lower, fp, fn))


def limits_row(bundle: "dict") -> "tuple[str, str]":
    """判据行③（超限侧）：逐轨加题累计对上限检＋两轨标注读数合计对预算上限检；越线如实报超限（咬，不静默）。"""
    present = [k for k in ("labels_soft", "labels_hard") if bundle.get(k) is not None]
    if not present:
        return (READ_UNVERIFIED, "两套标注工件均不在场（超限检不可判·fail-closed）")
    addq_total = 0
    reads_total = 0
    detail: "list[str]" = []
    for key in present:
        data = bundle[key]
        addq = int(data.get("加题数", 0) or 0)
        reads = int(data.get("标注读数数", 0) or 0)
        addq_total += addq
        reads_total += reads
        detail.append("%s 加题%d·读数%d" % ("软门" if key == "labels_soft" else "硬门", addq, reads))
    problems: "list[str]" = []
    if addq_total > ADDQ_CAP:
        problems.append("加题累计 %d＞上限 %d（每对象累计）" % (addq_total, ADDQ_CAP))
    if reads_total > BUDGET_CAP:
        problems.append("标注读数合计 %d＞预算上限 %d" % (reads_total, BUDGET_CAP))
    reading = "%s·加题累计 %d≤%d·标注读数 %d≤%d" % ("／".join(detail), addq_total, ADDQ_CAP,
                                                    reads_total, BUDGET_CAP)
    if problems:
        return (READ_FAIL, "超限咬：%s（应≤预注册上限·不静默）" % "；".join(problems))
    return (READ_PASS, reading)


def questions_row(bundle: "dict") -> "tuple[str, str, str]":
    """判据行③（题数侧）·题数检登记行：逐轨实做题数对起步值/下限读数（受限转径由 κ 行承载）。"""
    parts: "list[str]" = []
    for key, name in (("labels_soft", "软门"), ("labels_hard", "硬门")):
        data = bundle.get(key)
        if data is None:
            parts.append("%s 工件缺位" % name)
            continue
        n = len(merge_history(data)[0])
        tag = "达标" if n >= MIN_QUESTIONS else "转题量受限"
        parts.append("%s 实做 %d（起步 %d·下限 %d）%s" % (name, n, QUESTIONS_PER_OBJ_PER_TRACK, MIN_QUESTIONS, tag))
    return (READ_UNVERIFIED, "题数检登记行：%s（登记读数·不作门禁判定）" % "／".join(parts), "")


def retest_row(bundle: "dict") -> "tuple[str, str]":
    """判据行④·增量保留口径登记行（R15）：并集重算路径单义在场；作废重标唯一触发注明。"""
    voided = False
    seen = False
    for key in ("labels_soft", "labels_hard"):
        data = bundle.get(key)
        if data is None:
            continue
        seen = True
        if merge_history(data)[2]:
            voided = True
    if not seen:
        return (READ_UNVERIFIED, "标注工件缺位（增量保留路径读数待数据）")
    note = "·本批存在规范哈希变更→旧标注作废不入并集（唯一作废触发）" if voided else "·本批无规范哈希变更（旧标注不作废）"
    return (READ_UNVERIFIED,
            "增量保留口径：κ 在旧∪新标注并集重算·旧标注不作废；作废重标唯一触发＝标注规范哈希变更（走独立提案留痕）%s（登记行·不作门禁判定）" % note)


def tuple_out_recon(bundle: "dict", computed: "dict") -> "tuple[str, str]":
    """可选件 anchor-tuple-out.json 对账：已存在则与本次产出元组逐字段对账（不一致＝FAIL 咬）。"""
    out = bundle.get("tuple_out")
    if out is None:
        return (READ_PASS, "可选对账件不在场（缺位合法·不记未验不记咬）")
    entries = out if isinstance(out, list) else [out]
    problems: "list[str]" = []
    for idx, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            problems.append("对账条目%d 非对象" % idx)
            continue
        key = "labels_hard" if str(entry.get("轨道", "")) == "硬门" else "labels_soft"
        ours = computed.get(key)
        if ours is None:
            problems.append("对账条目%d 对应轨道本次无产出（无可对账）" % idx)
            continue
        for field in ("κ点值", "κ区间下界", "实做题数", "calibration_state"):
            if str(entry.get(field, "")) != str(ours.get(field, "")):
                problems.append("对账条目%d 字段%s 落盘%s≠本次%s" % (idx, field, entry.get(field), ours.get(field)))
    if problems:
        return (READ_FAIL, "元组对账不一致：%s" % "；".join(problems))
    return (READ_PASS, "可选对账件在场·逐字段对账全等（%d 条）" % len(entries))


def build_tuple(track_result: "tuple", data) -> "dict":
    """交付元组装配（R9 五字段＋calibration_state 自动驱动；κ 未产出＝null＋受限登记）。"""
    _verdict, _reading, pairs, limited, state, track_name, point, lower = track_result
    nan = float("nan")
    return {
        "轨道": track_name,
        "κ点值": None if math.isnan(point) else round(point, 6),
        "κ区间下界": None if math.isnan(lower) else round(lower, 6),
        "实做题数": len(pairs),
        "补题记录": list((data or {}).get("补题记录", [])),
        "受限登记": limited,
        "calibration_state": state,
    }


# ============================================================
# 批次执行（判分段主流程：判据行读数→写交付元组；汇总单列三态）
# ============================================================

def _read_batch_file(batch_dir: str, key: str):
    """读批次标注工件 json；缺文件返回 None（读数记未验），解析异常上抛按工具错误收。"""
    path = os.path.join(batch_dir, BATCH_FILES[key])
    if not os.path.isfile(path):
        return None
    return HC.read_json(path)


def run_batch(batch_dir: str, write_outputs: bool = True) -> "tuple[int, list[str]]":
    """对批次标注工件目录跑判据行；写软/硬两交付元组；返回 (退出码, 读数行列表)。"""
    if not os.path.isdir(batch_dir):
        sys.stderr.write("tool error: 批次目录不存在：%s\n" % batch_dir)
        raise SystemExit(EXIT_TOOL_ERROR)
    try:
        bundle = {key: _read_batch_file(batch_dir, key) for key in BATCH_FILES}
    except ValueError as exc:
        sys.stderr.write("tool error: 批次标注工件 json 解析失败：%s\n" % exc)
        raise SystemExit(EXIT_TOOL_ERROR)

    rows: "list[tuple[str, str, str]]" = []
    soft = kappa_track(bundle["labels_soft"], "软门")
    hard = kappa_track(bundle["labels_hard"], "硬门")
    rows.append(("软门κ", soft[1], soft[0]))
    rows.append(("硬门κ", hard[1], hard[0]))
    gold_verdict, gold_reading = gold_agreement_row(bundle["gold"])
    rows.append(("金标一致率＋FP/FN", gold_reading, gold_verdict))
    lim_verdict, lim_reading = limits_row(bundle)
    rows.append(("超限检（加题/预算）", lim_reading, lim_verdict))
    q_verdict, q_reading, _ = questions_row(bundle)
    rows.append(("题数检", q_reading, q_verdict))
    r_verdict, r_reading = retest_row(bundle)
    rows.append(("增量保留口径", r_reading, r_verdict))

    computed: "dict[str, dict]" = {}
    if bundle["labels_soft"] is not None:
        computed["labels_soft"] = build_tuple(soft, bundle["labels_soft"])
    if bundle["labels_hard"] is not None:
        computed["labels_hard"] = build_tuple(hard, bundle["labels_hard"])
    t_verdict, t_reading = tuple_out_recon(bundle, computed)
    rows.append(("元组对账（可选件）", t_reading, t_verdict))

    counts = {READ_PASS: 0, READ_FAIL: 0, READ_UNVERIFIED: 0}
    out_lines: "list[str]" = ["批次\t%s" % os.path.basename(batch_dir.rstrip("\\/"))]
    for name, reading, verdict in rows:
        counts[verdict] += 1
        out_lines.append("%s\t%s\t%s" % (name, reading, verdict))
    out_lines.append("汇总\tPASS=%d FAIL=%d 未验=%d\t%s"
                     % (counts[READ_PASS], counts[READ_FAIL], counts[READ_UNVERIFIED],
                        "有FAIL→退出1" if counts[READ_FAIL] else "无FAIL→退出0"))
    print("\n".join(out_lines))

    if write_outputs:
        try:
            for key, fname in TUPLE_OUT_FILES.items():
                if key in computed:
                    HC.write_json(os.path.join(batch_dir, fname), computed[key])
        except OSError as exc:
            sys.stderr.write("tool error: 交付元组写盘失败：%s\n" % exc)
            raise SystemExit(EXIT_TOOL_ERROR)
    return (EXIT_FAIL if counts[READ_FAIL] else EXIT_GREEN, out_lines)


# ============================================================
# selftest：内存配对＋临时目录合成批次（不落仓）咬放配对
# ============================================================

def _synth_labels(spec: str, pairs: "list[tuple[str, str]]", addq: int = 0,
                  reads: int = 0, history: "list[dict] | None" = None,
                  addq_records: "list[dict] | None" = None) -> dict:
    unit: "dict[str, dict[str, str]]" = {"标注者甲": {}, "标注者乙": {}}
    for idx, (a, b) in enumerate(pairs, 1):
        unit["标注者甲"]["q%02d" % idx] = a
        unit["标注者乙"]["q%02d" % idx] = b
    data: "dict" = {"规范哈希": spec, "标注单元": unit,
                    "加题数": addq, "标注读数数": reads, "补题记录": addq_records or []}
    if history:
        data["历史标注"] = history
    return data


def _perfect_pairs(n: int = 8) -> "list[tuple[str, str]]":
    classes = ("X", "Y", "Z")
    return [(classes[i % 3], classes[i % 3]) for i in range(n)]


def _weak_lower_pairs() -> "list[tuple[str, str]]":
    """κ 点值 ≥0.6（≈0.619）但 n=8 样本下 bootstrap 下界必不足——专咬「下界不足」。"""
    la = ["X", "X", "X", "Y", "Y", "Y", "Z", "Z"]
    lb = ["X", "X", "X", "Y", "Y", "Z", "Z", "Y"]
    return list(zip(la, lb))


def _synth_batch(batch_dir: str, *, soft_pairs: "list[tuple[str, str]] | None" = None,
                 hard_pairs: "list[tuple[str, str]] | None" = None,
                 addq: int = 0, reads: int = 0, with_gold: bool = True,
                 tuple_out_mismatch: bool = False) -> None:
    """合成批次标注工件（系统临时目录，不落仓）。"""
    soft = _synth_labels("spec-a", soft_pairs if soft_pairs is not None else _perfect_pairs(8),
                         addq=addq, reads=reads)
    hard = _synth_labels("spec-b", hard_pairs if hard_pairs is not None else _perfect_pairs(8),
                         addq=addq, reads=reads)
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["labels_soft"]), soft)
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["labels_hard"]), hard)
    if with_gold:
        HC.write_json(os.path.join(batch_dir, BATCH_FILES["gold"]),
                      {"配对": [{"题id": "q01", "人工金标": "PASS", "断言结果": "PASS"},
                                {"题id": "q02", "人工金标": "FAIL", "断言结果": "PASS"},
                                {"题id": "q03", "人工金标": "PASS", "断言结果": "PASS"}]})
    if tuple_out_mismatch:
        HC.write_json(os.path.join(batch_dir, BATCH_FILES["tuple_out"]),
                      {"轨道": "软门", "κ点值": 0.111, "κ区间下界": 0.222,
                       "实做题数": 8, "calibration_state": "待校准"})


def _run_in_temp(name: str, **kwargs) -> "tuple[int, list[str]]":
    import tempfile
    base = tempfile.mkdtemp(prefix="fuxi-s0b-%s-" % name)  # %TEMP% 合成样本，不落仓
    tmp = os.path.join(base, "batch")  # 批次目录名定值（读数行含批次名→连跑逐字节全等可判）
    os.makedirs(tmp)
    _synth_batch(tmp, **kwargs)
    return run_batch(tmp, write_outputs=False)


def _selftest_cases() -> "list[tuple[str, bool, bool]]":
    """返回 (用例名, 判据结果, 期望结果) 列表（与两 validator selftest 同款配对形态）。"""
    cases: "list[tuple[str, bool, bool]]" = []

    # Wilson 两定值锚（n=8：k=7 不过线／k=8 过线；锚值 0.589／0.747 容差 ±0.001）
    w7 = wilson_lower(7, 8)
    w8 = wilson_lower(8, 8)
    cases.append(("WILSON_anchor_k7", abs(w7 - 0.589) <= 0.001, True))
    cases.append(("WILSON_anchor_k8", abs(w8 - 0.747) <= 0.001, True))
    cases.append(("WILSON_k7_below_line", w7 < KAPPA_THRESHOLD, True))
    cases.append(("WILSON_k8_over_line", w8 >= KAPPA_THRESHOLD, True))
    cases.append(("WILSON_empty_failclosed", wilson_lower(0, 0) == 0.0, True))

    # cohens_kappa：全一致＝1／全错位低值／长度不等 fail-closed
    cases.append(("KAPPA_perfect", cohens_kappa(["X", "Y", "Z"], ["X", "Y", "Z"]) == 1.0, True))
    cases.append(("KAPPA_mismatch_low", cohens_kappa(["X", "X", "Y", "Y"], ["Y", "Y", "X", "X"]) < 0.0, True))
    cases.append(("KAPPA_len_mismatch_zero", cohens_kappa(["X"], ["X", "Y"]) == 0.0, True))
    cases.append(("KAPPA_constant_degenerate", cohens_kappa(["X", "X"], ["X", "X"]) == 1.0, True))

    # bootstrap 种子确定性：同输入两跑逐值全等；样本＜2 fail-closed
    pa = [p[0] for p in _perfect_pairs(8)]
    pb = [p[1] for p in _perfect_pairs(8)]
    cases.append(("BOOT_seed_deterministic",
                  bootstrap_kappa_lower(pa, pb) == bootstrap_kappa_lower(pa, pb), True))
    cases.append(("BOOT_small_sample_zero", bootstrap_kappa_lower(["X"], ["X"]) == 0.0, True))

    # 判据行①配对：κ 达标放（校准态）／下界不足咬（待校准如实显示）／缺工件未验
    v1, r1, _p1, _l1, s1, _t1, _pt1, _lo1 = kappa_track(_synth_labels("s", _perfect_pairs(8)), "软门")
    cases.append(("KTRACK_pass_calibrated", v1 == READ_PASS and s1 == CALIBRATED, True))
    v2, r2, _p2, _l2, s2, _t2, pt2, lo2 = kappa_track(_synth_labels("s", _weak_lower_pairs()), "软门")
    cases.append(("KTRACK_bite_lower_short", v2 == READ_FAIL and s2 == PENDING_CAL and pt2 >= KAPPA_THRESHOLD and lo2 < KAPPA_THRESHOLD, True))
    v3, _r3, _p3, _l3, s3, _t3, _pt3, _lo3 = kappa_track(None, "硬门")
    cases.append(("KTRACK_missing_unverified", v3 == READ_UNVERIFIED and s3 == PENDING_CAL, True))

    # 判据行③受限转径：题数 4＜下限→未验＋受限登记（κ 字段置 null）
    v4, r4, _p4, lim4, s4, _t4, pt4, lo4 = kappa_track(_synth_labels("s", _perfect_pairs(4)), "软门")
    tup4 = build_tuple((v4, r4, _p4, lim4, s4, "软门", pt4, lo4), _synth_labels("s", _perfect_pairs(4)))
    cases.append(("QCOUNT_limited_tag", v4 == READ_UNVERIFIED and "题量受限" in lim4, True))
    cases.append(("QCOUNT_tuple_null_kappa", tup4["κ点值"] is None and tup4["κ区间下界"] is None
                  and tup4["实做题数"] == 4 and tup4["受限登记"] != "", True))

    # 判据行③超限咬：加题 31＞30 咬／读数 129＞128 咬／限内放
    over_addq = {"labels_soft": _synth_labels("s", _perfect_pairs(8), addq=31, reads=64), "labels_hard": None}
    over_budget = {"labels_soft": _synth_labels("s", _perfect_pairs(8), addq=2, reads=129), "labels_hard": None}
    in_limits = {"labels_soft": _synth_labels("s", _perfect_pairs(8), addq=2, reads=64), "labels_hard": None}
    cases.append(("LIMITS_bite_addq", limits_row(over_addq)[0] == READ_FAIL, True))
    cases.append(("LIMITS_bite_budget", limits_row(over_budget)[0] == READ_FAIL, True))
    cases.append(("LIMITS_pass", limits_row(in_limits)[0] == READ_PASS, True))
    cases.append(("LIMITS_missing_unverified", limits_row({"labels_soft": None, "labels_hard": None})[0] == READ_UNVERIFIED, True))

    # 判据行②金标行：在场记未验（不假绿）＋FP/FN 分解对＋缺工件未验
    gv, greading = gold_agreement_row({"配对": [{"人工金标": "PASS", "断言结果": "PASS"},
                                                {"人工金标": "FAIL", "断言结果": "PASS"}]})
    cases.append(("GOLD_unverified_with_fp", gv == READ_UNVERIFIED and "FP=1" in greading and "FN=0" in greading, True))
    gv2, greading2 = gold_agreement_row({"配对": [{"人工金标": "PASS", "断言结果": "FAIL"}]})
    cases.append(("GOLD_fn_split", "FP=0" in greading2 and "FN=1" in greading2, True))
    cases.append(("GOLD_missing_unverified", gold_agreement_row(None)[0] == READ_UNVERIFIED, True))

    # 判据行④增量保留口径（R15）：并集重算例＋规范哈希一致并历史／变更作废并注明
    old = [("X", "X"), ("Y", "Y"), ("X", "Y")]
    new = [("Z", "Z"), ("X", "X")]
    union_expected = cohens_kappa([p[0] for p in old + new], [p[1] for p in old + new])
    cases.append(("RETEST_union_equals_recompute", retest_kappa(old, new) == union_expected, True))
    hist_same = _synth_labels("s", new, history=[{"规范哈希": "s", "标注单元": {
        "标注者甲": {"h1": "X", "h2": "Y"}, "标注者乙": {"h1": "X", "h2": "Y"}}}])
    hist_changed = _synth_labels("s", new, history=[{"规范哈希": "s-old", "标注单元": {
        "标注者甲": {"h1": "X", "h2": "Y"}, "标注者乙": {"h1": "X", "h2": "Y"}}}])
    u_same = merge_history(hist_same)[0]
    u_changed = merge_history(hist_changed)
    cases.append(("R15_history_same_spec_merged", len(u_same) == 4, True))
    cases.append(("R15_spec_change_voids_history", len(u_changed[0]) == 2 and u_changed[2] is True, True))

    # 可选对账件：缺位放／在场全等放／数值不一致咬
    comp = {"labels_soft": {"κ点值": 0.5, "κ区间下界": 0.4, "实做题数": 8, "calibration_state": "待校准"}}
    ok_out = {"tuple_out": {"轨道": "软门", "κ点值": 0.5, "κ区间下界": 0.4,
                            "实做题数": 8, "calibration_state": "待校准"}}
    bad_out = {"tuple_out": {"轨道": "软门", "κ点值": 0.9, "κ区间下界": 0.4,
                             "实做题数": 8, "calibration_state": "待校准"}}
    cases.append(("TUPRECON_absent_pass", tuple_out_recon({"tuple_out": None}, comp)[0] == READ_PASS, True))
    cases.append(("TUPRECON_match_pass", tuple_out_recon(ok_out, comp)[0] == READ_PASS, True))
    cases.append(("TUPRECON_mismatch_bite", tuple_out_recon(bad_out, comp)[0] == READ_FAIL, True))

    # 词表常量复用对账：calibration_state 词表与 assert-tool 注册位逐字全等（不复制自检）
    cases.append(("VOCAB_single_source", CALIBRATION_STATES == AT.CALIBRATION_STATES
                  and list(CALIBRATION_STATES) == ["校准态", "待校准"], True))
    cases.append(("THRESH_single_source", KAPPA_THRESHOLD == AT.KAPPA_THRESHOLD, True))

    # 合成批次全链：达标批次 exit 0（金标行未验不拉码）
    code, _lines = _run_in_temp("green")
    cases.append(("BATCH_green_exit0", code == EXIT_GREEN, True))
    # 下界不足批次→硬门/软门行 FAIL→exit 1（真咬）
    code2, _l2 = _run_in_temp("weak", soft_pairs=_weak_lower_pairs())
    cases.append(("BATCH_weakkappa_exit1", code2 == EXIT_FAIL, True))
    # 超限批次（加题 31）→exit 1
    code3, _l3 = _run_in_temp("overaddq", addq=31)
    cases.append(("BATCH_overaddq_exit1", code3 == EXIT_FAIL, True))
    # 对账不一致批次→exit 1
    code4, _l4 = _run_in_temp("reconbad", tuple_out_mismatch=True)
    cases.append(("BATCH_reconbad_exit1", code4 == EXIT_FAIL, True))
    # 空目录（无任何标注工件）＝全未验 exit 0（fail-closed 不假绿）
    import tempfile
    empty_base = tempfile.mkdtemp(prefix="fuxi-s0b-empty-")
    empty = os.path.join(empty_base, "batch")  # 批次目录名定值（连跑逐字节全等可判）
    os.makedirs(empty)
    code5, _l5 = run_batch(empty, write_outputs=False)
    cases.append(("BATCH_empty_allunverified_exit0", code5 == EXIT_GREEN, True))

    # 确定性连跑：同批次两跑读数行逐字节全等＋落盘元组两跑全等
    import tempfile
    repro_base = tempfile.mkdtemp(prefix="fuxi-s0b-repro-")
    tmp = os.path.join(repro_base, "batch")  # 批次目录名定值（连跑逐字节全等可判）
    os.makedirs(tmp)
    _synth_batch(tmp, soft_pairs=_weak_lower_pairs())
    c1, lines1 = run_batch(tmp, write_outputs=True)
    tup1_soft = HC.read_json(os.path.join(tmp, TUPLE_OUT_FILES["labels_soft"]))
    tup1_hard = HC.read_json(os.path.join(tmp, TUPLE_OUT_FILES["labels_hard"]))
    c2, lines2 = run_batch(tmp, write_outputs=True)
    tup2_soft = HC.read_json(os.path.join(tmp, TUPLE_OUT_FILES["labels_soft"]))
    cases.append(("REPRO_lines_bytes_equal",
                  c1 == c2 and "\n".join(lines1).encode("utf-8") == "\n".join(lines2).encode("utf-8"), True))
    cases.append(("REPRO_tuple_files_equal", tup1_soft == tup2_soft, True))
    cases.append(("TUPLE_two_files_split", tup1_hard["轨道"] == "硬门" and tup1_soft["轨道"] == "软门", True))
    cases.append(("TUPLE_five_fields_plus_state",
                  set(tup1_soft) == {"轨道", "κ点值", "κ区间下界", "实做题数", "补题记录", "受限登记", "calibration_state"}, True))

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
    print("s0b-kappa selftest 用例 %d／反常 %d" % (total, failures))
    return EXIT_FAIL if failures else EXIT_GREEN


def main(argv: "list[str]") -> int:
    if len(argv) == 1 and argv[0] == "selftest":
        return run_selftest()
    if len(argv) == 1 and os.path.isdir(argv[0]):
        code, _lines = run_batch(argv[0])
        return code
    sys.stderr.write("usage error: 用法＝python s0b-kappa.py <batch_dir> | selftest\n")
    return EXIT_TOOL_ERROR


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按工具错误码，不得吞成 0
        sys.stderr.write("tool error: %s\n" % exc)
        raise SystemExit(EXIT_TOOL_ERROR)