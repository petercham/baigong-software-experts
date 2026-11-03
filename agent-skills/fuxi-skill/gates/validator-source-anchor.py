#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fuxi-skill · source-anchor validator（method 轨硬门·S3 建）。

性质＝交付件本体。层结构（顺序执行，前层 fail 不进后层；层名即 gate_source 注册词）：
    L1 机械断言 → L2 三臂对照 → L3 诱饵测试 → L4 留出集 → L5 泄漏检查 → L6 边缘诚实度
三臂臂名写死＝old / new / without_skill（D5 原文＋AC-3 对照臂注册口径）。

生成段／判分段分离：本件＝判分段，只对生成段落盘工件做确定性判定；
生成段（跑模型答题、三臂作答、×5 重蒸）＝非确定，产物落盘＋哈希归生成段。
同输入（同工件集＋同预注册件）连跑退出码与逐项读数全等。

退出码闭集（三值，无其他取值）：
    0 全层绿（未验行不算 fail 不算 pass，汇总单列，不拉码）
    1 任层 fail
    2 工具自身错误（用法错／环境错／输入 json 解析失败，fail-closed 不得吞成 0）

与 assert-tool 的关系＝分立脚本：本件不从 assert-tool import 任何判据函数，
仅以纯数据常量取词表/闭集（允许复用形态，词表本体单源在 assert-tool 注册位）；
GS 断言留在 assert-tool，实装基面＝本件写出的验证记录目录。

用法：
    python validator-source-anchor.py <batch_dir>   # 判分段：对批次工件目录出六层读数
    python validator-source-anchor.py selftest      # 自证：合成样本（系统临时目录，不落仓）咬放配对
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
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

# 层名闭集（＝gate_source 取值；与 validator-catalog 值注册·层名逐字全等）
LAYERS = ("机械断言", "三臂对照", "诱饵测试", "留出集", "泄漏检查", "边缘诚实度")

# ---- 预注册数值包（注册面＝validator-catalog §四·阈值预注册表；中途变更走独立提案）----
DECOY_HIT_MAX = 0            # 诱饵命中上限（C-2 锁定）
EDGE_HONESTY_MIN = 0.80      # 边缘诚实度期望档位占比下限（C-2 锁定）
SPLIT_RATIO = (60, 40)       # 留出集切分比例（D2 机制 technique 侧原生）
PRE_SEED = 20261030          # 留出集切分种子（预注册值）
RERUN_ASSERT_MIN = 5         # ×5 断言通过向量一致率下限＝5/5（C-2 推荐值锁定）
RERUN_JACCARD_MIN = 0.80     # ×5 锚点复现率两两 Jaccard 均值下限（C-2 推荐值锁定）
CONTAIN_MIN_LEN = 20         # 泄漏包含式比对的最小归一化题面长度（§1.3）

# 批次工件目录输入面文件闭集（缺文件＝对应层记未验，fail-closed 不推定绿）
BATCH_FILES = {
    "artifact": "artifact.json",                 # 产物实例（technique 卡集＋时间切分核对行）
    "prereg": "prereg.json",                     # 两轴切分预注册件（T 读数＋题库指纹）
    "corpus": "corpus-questions.json",           # 语料分块＋题面列表（泄漏两式对象）
    "split": "split-manifest.json",              # 留出集切分（哈希指纹代指，成员名单不落盘）
    "arms": "arm-table.json",                    # 对照组构成表＋三值报告
    "decoy": "decoy-trigger.json",               # 生成段诱饵触发读数
    "edge": "edge-honesty.json",                 # 「未明说问题」题组作答工件
    "rerun": "rerun5.json",                      # ×5 重蒸工件（断言向量＋锚点集）
}

# 禁止落盘键（hold-out 成员名单不落任何可检索件，以哈希指纹代指——前置定义件 §2.4 接口）
FORBIDDEN_MEMBER_KEYS = ("holdout成员名单", "成员名单", "成员列表")

# technique 卡结构闭集（词表本体单源＝assert-tool 注册位，本处纯数据常量复用）
CARD_SECTIONS = AT.TECHNIQUE_CARD_SECTIONS
CARD_FIELDS = AT.TECHNIQUE_CARD_FIELDS
ABSTAIN_EXPECTED = ("有限定",)   # 边缘诚实度期望档位（BW-2 词表机检：「有限定」或写「证据不足」）
EVIDENCE_INSUFFICIENT = "证据不足"
LEAKAGE_OK = "已检-不在语料内"
LEAKAGE_HIT = "已检-在语料内"
CALIBRATION_DEFAULT = "待校准"


def _read_batch_file(batch_dir: str, key: str):
    """读批次工件 json；缺文件返回 None（层记未验），解析异常上抛按工具错误收。"""
    path = os.path.join(batch_dir, BATCH_FILES[key])
    if not os.path.isfile(path):
        return None
    return HC.read_json(path)


def _dir_artifact_hashes(batch_dir: str) -> str:
    """工件集哈希＝批次内全部已知工件按名序内容哈希再哈希（确定性，验证记录 `工件哈希` 字段）。"""
    parts: "list[str]" = []
    for key in sorted(BATCH_FILES):
        path = os.path.join(batch_dir, BATCH_FILES[key])
        if os.path.isfile(path):
            with open(path, "rb") as handle:
                parts.append("%s:%s" % (BATCH_FILES[key], hashlib.sha256(handle.read()).hexdigest()))
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()


# ============================================================
# 六层判定函数（纯函数·确定性；返回 (判定, 读数文本, 附加字段 dict)）
# ============================================================

def layer_l1_mechanical(artifact) -> "tuple[str, str, dict]":
    """L1 机械断言：卡级确定性断言（六段齐备＋五字段非空＋B 段非空＋触发断言在场＋出处成对）。"""
    if artifact is None:
        return (READ_UNVERIFIED, "产物工件不在场（规程在场待数据）", {})
    cards = artifact.get("cards", [])
    if not cards:
        return (READ_FAIL, "产物无卡集", {})
    problems: "list[str]" = []
    for idx, card in enumerate(cards, 1):
        missing_sections = [s for s in CARD_SECTIONS if s not in card]
        extra = sorted(set(card) - set(CARD_SECTIONS) - set(CARD_FIELDS) - {"source_id", "位置"})
        if missing_sections:
            problems.append("卡%d 六段不齐备（缺%s）" % (idx, missing_sections))
        if extra:
            problems.append("卡%d 未注册字段%s" % (idx, extra))
        missing_fields = [f for f in CARD_FIELDS if not str(card.get(f, "")).strip()]
        if missing_fields:
            problems.append("卡%d 五字段缺位%s" % (idx, missing_fields))
        if not str(card.get("B", "")).strip():
            problems.append("卡%d B 段空占位（BW-4）" % idx)
        if not str(card.get("触发", "")).strip():
            problems.append("卡%d 触发断言不在场" % idx)
        has_id = bool(str(card.get("source_id", "")).strip())
        has_loc = bool(str(card.get("位置", "")).strip())
        if has_id != has_loc:
            problems.append("卡%d source_id/位置 不成对（FC-3）" % idx)
    if problems:
        return (READ_FAIL, "；".join(problems), {})
    return (READ_PASS, "卡 %d 张·六段＋五字段＋B 段＋触发断言＋出处成对全判绿" % len(cards), {})


def layer_l2_three_arms(arms_table) -> "tuple[str, str, dict]":
    """L2 三臂对照：臂名写死 old/new/without_skill；构成表行闭集＋三值报告三行齐备。

    「同模型」＝声明值不可独立校验→读数随附局限声明（§四.2 口径）；
    缺臂/缺构成表行/缺三值报告任一→记未验（fail-closed，不以总通过推定）。
    """
    if arms_table is None:
        return (READ_UNVERIFIED, "构成表不在场（规程在场待数据）", {"control_arm": "未测"})
    arm_rows = arms_table.get("臂表", {})
    missing_arms = [a for a in HC.ARMS if a not in arm_rows]
    if missing_arms:
        return (READ_UNVERIFIED, "缺臂行%s→记未验（构成表缺行＝三臂对照记未验）" % missing_arms,
                {"control_arm": "未测"})
    row_problems: "list[str]" = []
    model_decls: "list[str]" = []
    for arm in HC.ARMS:
        row = arm_rows[arm]
        miss = [f for f in HC.ARM_TABLE_FIELDS if not str(row.get(f, "")).strip()]
        if miss:
            row_problems.append("%s 臂缺字段%s" % (arm, miss))
        model_decls.append(str(row.get("模型标识（声明值）", "")))
    three = arms_table.get("三值报告", {})
    three_missing = [k for k in ("绝对值", "基线值", "增量") if not str(three.get(k, "")).strip()]
    if row_problems:
        return (READ_FAIL, "构成表行闭集 diff 非∅：%s" % "；".join(row_problems), {"control_arm": "未测"})
    if three_missing:
        return (READ_UNVERIFIED, "三值报告缺%s行→记未验（R10 三值缺一记未验）" % three_missing,
                {"control_arm": "无臂" if "增量" in three_missing else "未测"})
    same_model_decl = model_decls[0] if len(set(model_decls)) == 1 else "声明不一致"
    limit = "「同模型」为会话侧声明值，盘上不可独立校验；任何以「同模型」为前提的增量读数随附本局限声明"
    reading = "三臂齐备（old/new/without_skill）·三值报告 %s/%s/%s·同模型声明=%s" % (
        three["绝对值"], three["基线值"], three["增量"], same_model_decl)
    if same_model_decl == "声明不一致":
        return (READ_UNVERIFIED, reading + "（声明不一致→增量只作参考，规程在场待实证）",
                {"control_arm": "三臂", "模型标识（声明值）": same_model_decl, "局限声明": limit})
    return (READ_PASS, reading,
            {"control_arm": "三臂", "模型标识（声明值）": same_model_decl, "局限声明": limit})


def layer_l3_decoy(decoy) -> "tuple[str, str, dict]":
    """L3 诱饵测试：近邻卡 decoy 触发命中数 ≤ 预注册上限（0）；超限＝FM-M-01/03 处置。

    近邻定义（method 轨，施工输入 §1.1 L3 补死值）＝同一问题域、不同来源法度的技法卡；
    decoy 集从注册库内按问题域标签选取——选取动作属生成段，本层只读落盘命中读数。
    """
    if decoy is None:
        return (READ_UNVERIFIED, "诱饵触发读数不在场（规程在场待数据）", {})
    hits = decoy.get("诱饵命中数", None)
    if not isinstance(hits, int):
        return (READ_FAIL, "诱饵命中数非整数读数（fail-closed）", {})
    if hits > DECOY_HIT_MAX:
        return (READ_FAIL, "诱饵命中 %d＞上限 %d（FM-M-01/03：阻断晋级）" % (hits, DECOY_HIT_MAX), {})
    return (READ_PASS, "诱饵命中 %d≤上限 %d" % (hits, DECOY_HIT_MAX), {})


def layer_l4_holdout(split) -> "tuple[str, str, dict]":
    """L4 留出集：60/40 固定种子切分核对；hold-out 成员名单不落可检索件（哈希指纹代指）。"""
    if split is None:
        return (READ_UNVERIFIED, "切分名单不在场（规程在场待数据）", {})
    raw_text = json.dumps(split, ensure_ascii=False)
    banned = [k for k in FORBIDDEN_MEMBER_KEYS if k in raw_text]
    if banned:
        return (READ_FAIL, "hold-out 成员名单落盘（禁用键%s）＝名单不落可检索件纪律违例" % banned, {})
    ratio = split.get("切分比例", [])
    if list(ratio) != list(SPLIT_RATIO):
        return (READ_FAIL, "切分比例 %s≠预注册 %s" % (ratio, list(SPLIT_RATIO)), {})
    if split.get("种子") != PRE_SEED:
        return (READ_FAIL, "种子 %s≠预注册 %s（中途变更须走独立提案）" % (split.get("种子"), PRE_SEED), {})
    fp_v = str(split.get("validation指纹", ""))
    fp_h = str(split.get("holdout指纹", ""))
    if len(fp_v) != 64 or len(fp_h) != 64:
        return (READ_FAIL, "切分指纹非 sha256 形态（应 64 位十六进制）", {})
    return (READ_PASS, "60/40 切分·种子=%s·两指纹在场·成员名单未落盘" % PRE_SEED, {})


def layer_l5_leakage(artifact, prereg, corpus) -> "tuple[str, str, dict]":
    """L5 泄漏检查：哈希两式（相等/包含）＋题库指纹防改校验＋时间切分可核对行两检。

    任一命中→`leakage_check`＝已检-在语料内→该测试集作废重建（FM 处置）＝fail；
    全不命中→已检-不在语料内；缺预注册件/缺工件→未验（fail-closed 不推定绿）。
    """
    fields = {"leakage_check": "未检"}
    if prereg is None:
        return (READ_UNVERIFIED, "两轴切分预注册件不在场→该对象评估记未验（fail-closed）", fields)
    if artifact is None or corpus is None:
        return (READ_UNVERIFIED, "产物/语料工件不在场→记未验", fields)
    # 防改题校验：题集重算哈希 ≠ 预注册题库指纹＝「题库被改」直接 fail（预注册冻结纪律同族）
    questions = corpus.get("题面列表", [])
    if HC.question_set_fingerprint(questions) != str(prereg.get("题库指纹", "")):
        return (READ_FAIL, "题库被改：重算指纹≠预注册题库指纹（预注册冻结纪律）", fields)
    # 时间切分可核对行：日期差值检＋语料哈希全等检（与预注册件 T 读数对账一致）
    line = artifact.get("时间切分核对行", {})
    t_date = HC.date_key(str(line.get("测试集日期", "")))
    c_date = HC.date_key(str(prereg.get("语料截止日", "")))
    if t_date < 0 or c_date < 0:
        return (READ_FAIL, "时间切分核对行/预注册件日期形态不合法", fields)
    if t_date <= c_date:
        return (READ_FAIL, "测试集日期 %s ≤ 语料截止日 %s（时间切分违例）"
                % (line.get("测试集日期"), prereg.get("语料截止日")), fields)
    if str(line.get("语料哈希", "")) != str(prereg.get("语料库哈希", "")):
        return (READ_FAIL, "核对行语料哈希≠预注册语料库哈希（T 读数对账不一致）", fields)
    # 哈希两式：①相等式 sha256(归一化题面) ∈ {语料分块归一化哈希}；②包含式（长度≥20）
    chunk_set = HC.corpus_chunk_hashes(corpus.get("语料分块", []))
    full_norm = HC.normalize_text("\n".join(corpus.get("语料分块", [])))
    hit_q: "list[str]" = []
    for q in questions:
        qn = HC.normalize_text(q)
        if HC.sha256_hex(qn) in chunk_set:
            hit_q.append(q[:20])
        elif len(qn) >= CONTAIN_MIN_LEN and qn in full_norm:
            hit_q.append(q[:20])
    fields["leakage_check"] = LEAKAGE_HIT if hit_q else LEAKAGE_OK
    if hit_q:
        return (READ_FAIL, "泄漏命中 %d 题（%s）→测试集作废重建（FM 处置）"
                % (len(hit_q), "、".join(hit_q[:3])), fields)
    reading = "哈希两式全不命中·题库指纹对账一致·时间切分行核对通过（语料截止日 %s＜测试集日期 %s）" % (
        prereg.get("语料截止日"), line.get("测试集日期"))
    fields["时间切分核对行"] = "%s>%s|语料哈希=%s" % (
        line.get("测试集日期"), prereg.get("语料截止日"), str(prereg.get("语料库哈希", ""))[:12])
    return (READ_PASS, reading, fields)


def layer_l6_edge_honesty(edge) -> "tuple[str, str, dict]":
    """L6 边缘诚实度：「未明说问题」题组期望档位＝「有限定」或写「证据不足」；读数＝期望档位占比。

    达标线＝预注册 EDGE_HONESTY_MIN（BW-2 词表机检口径）；缺工件→未验。
    题面主题不落语料头部主题热区（P 配平）属生成段动作，本层读落盘配平读数行。
    """
    if edge is None:
        return (READ_UNVERIFIED, "边缘题组工件不在场（规程在场待数据）", {})
    answers = edge.get("题组", [])
    if not answers:
        return (READ_FAIL, "边缘题组空集（fail-closed）", {})
    expected = [a for a in answers
                if str(a.get("abstain_tier", "")) in ABSTAIN_EXPECTED
                or EVIDENCE_INSUFFICIENT in str(a.get("输出", ""))]
    ratio = len(expected) / len(answers)
    pct = "%.0f%%" % (ratio * 100)
    reading = ("期望档位占比 %s（统计口径：期望档位=有限定或证据不足；样本量 %d；一致性系数见裁判家族行）·达标线 %s"
               % (pct, len(answers), "%.0f%%" % (EDGE_HONESTY_MIN * 100)))
    bal = edge.get("配平读数", "")
    if bal:
        reading += "·P 配平读数=%s" % bal
    if ratio < EDGE_HONESTY_MIN:
        return (READ_FAIL, reading + "＜下限（期望档位不足）", {})
    return (READ_PASS, reading, {})


# ============================================================
# ×5 方差报告行（D6 协议·报告行存在性＋数值域检；读数行入产物报告）
# ============================================================

def rerun_report_line(rerun):
    """返回 (报表行文本 或 None)。缺工件→报告行在场但读数记未验（缺该读数行＝验收行不过）。"""
    if rerun is None:
        return ("run_to_run_5读数\t断言一致率=未验；锚点复现率=未验（×5 重蒸工件不在场）\t未验",
                "未验", "")
    vectors = rerun.get("断言向量", [])
    anchors = rerun.get("锚点集", [])
    if len(vectors) != RERUN_ASSERT_MIN or len(anchors) != RERUN_ASSERT_MIN:
        return ("run_to_run_5读数\t断言一致率=未验；锚点复现率=未验（重蒸样本非5次）\t未验",
                "未验", "")
    agree = sum(1 for pos in range(len(vectors[0])) if len({v[pos] for v in vectors}) == 1)
    total_bits = len(vectors[0])
    jmean = HC.pairwise_jaccard_mean([set(a) for a in anchors])
    # 一致率下限 5/5＝逐位全等（agree==total_bits）；复现率下限＝Jaccard 均值线
    verdict = READ_PASS if (total_bits >= 1 and agree == total_bits
                            and jmean >= RERUN_JACCARD_MIN) else READ_FAIL
    line = ("run_to_run_5读数\t断言一致率 %d/%d；锚点复现率均值 %.2f（统计口径：断言结果向量逐位一致＋source_id 锚点集两两 Jaccard 均值；样本量 5；一致性系数见锚点复现率）\t%s"
            % (agree, total_bits, jmean, verdict))
    return (line, verdict, "%d/%d|%.2f" % (agree, total_bits, jmean))


# ============================================================
# 批次执行（判分段主流程：逐层读数→报表行→验证记录 jsonl）
# ============================================================

def run_batch(batch_dir: str, write_records: bool = True) -> int:
    """对批次工件目录跑六层＋×5 报告行；写出报表与验证记录；退出码闭集。"""
    if not os.path.isdir(batch_dir):
        sys.stderr.write("tool error: 批次目录不存在：%s\n" % batch_dir)
        return EXIT_TOOL_ERROR
    try:
        inputs = {key: _read_batch_file(batch_dir, key) for key in BATCH_FILES}
    except ValueError as exc:
        sys.stderr.write("tool error: 批次工件 json 解析失败：%s\n" % exc)
        return EXIT_TOOL_ERROR

    artifact, prereg = inputs["artifact"], inputs["prereg"]
    artifact_hash = _dir_artifact_hashes(batch_dir)
    prereg_hash = ""
    if prereg is not None:
        prereg_hash = hashlib.sha256(
            json.dumps(prereg, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()

    results: "list[tuple[str, str, str, dict]]" = []  # (层名, 判定, 读数, 附加字段)
    blocked = False
    layer_defs = [
        ("机械断言", lambda: layer_l1_mechanical(artifact)),
        ("三臂对照", lambda: layer_l2_three_arms(inputs["arms"])),
        ("诱饵测试", lambda: layer_l3_decoy(inputs["decoy"])),
        ("留出集", lambda: layer_l4_holdout(inputs["split"])),
        ("泄漏检查", lambda: layer_l5_leakage(artifact, prereg, inputs["corpus"])),
        ("边缘诚实度", lambda: layer_l6_edge_honesty(inputs["edge"])),
    ]
    for layer_name, fn in layer_defs:
        if blocked:
            results.append((layer_name, READ_UNVERIFIED, "前层 fail 不进后层（顺序纪律）", {}))
            continue
        verdict, reading, extra = fn()
        results.append((layer_name, verdict, reading, extra))
        if verdict == READ_FAIL:
            blocked = True

    rerun_line, rerun_verdict, rerun_reading = rerun_report_line(inputs["rerun"])

    counts = {READ_PASS: 0, READ_FAIL: 0, READ_UNVERIFIED: 0}
    report_lines: "list[str]" = ["产物id\t%s" % (str(artifact.get("产物id", "")) if artifact else "")]
    records: "list[dict]" = []
    for seq, (layer_name, verdict, reading, extra) in enumerate(results, 1):
        counts[verdict] += 1
        report_lines.append(HC.format_report_line("L%d %s" % (seq, layer_name), reading, verdict))
        rec = HC.record_skeleton()
        rec.update({
            "记录id": "%s-V%02d" % (os.path.basename(batch_dir.rstrip("\\/")), seq),
            "产物id": str(artifact.get("产物id", "")) if artifact else "",
            "所属轨": "method",
            "层名": layer_name,
            "gate_source": layer_name,
            "读数": reading,
            "判定": verdict,
            "工件哈希": artifact_hash,
            "预注册件哈希": prereg_hash,
            "calibration_state": CALIBRATION_DEFAULT,   # method 轨无 judge 层，登记缺省值（口径见 validator-catalog §一.3）
            "evidence_grade": "机械断言",
        })
        rec.update(extra)
        records.append(rec)
    counts[rerun_verdict if rerun_verdict in counts else READ_UNVERIFIED] += 1
    report_lines.append(rerun_line)
    rerun_rec = HC.record_skeleton()
    rerun_rec.update({
        "记录id": "%s-V07" % os.path.basename(batch_dir.rstrip("\\/")),
        "产物id": str(artifact.get("产物id", "")) if artifact else "",
        "所属轨": "method", "层名": "机械断言", "gate_source": "机械断言",
        "读数": rerun_reading or "未验", "判定": rerun_verdict,
        "工件哈希": artifact_hash, "预注册件哈希": prereg_hash,
        "calibration_state": CALIBRATION_DEFAULT, "evidence_grade": "机械断言",
        "run_to_run_5读数": rerun_reading or "",
    })
    records.append(rerun_rec)
    # 装载核对字段位预留（当期恒未验——R20 装载记录导出接口实证不可得，不以 stub 推定绿）
    for rec in records:
        rec["装载核对"] = READ_UNVERIFIED

    report_lines.append("汇总\tPASS=%d FAIL=%d 未验=%d\t%s"
                        % (counts[READ_PASS], counts[READ_FAIL], counts[READ_UNVERIFIED],
                           "FAIL存在→退出1" if counts[READ_FAIL] else "无FAIL→退出0"))
    print("\n".join(report_lines))

    if write_records:
        try:
            HC.write_jsonl(os.path.join(batch_dir, "verification-records.jsonl"), records)
            HC.write_json(os.path.join(batch_dir, "report.json"),
                          {"批次": os.path.basename(batch_dir.rstrip("\\/")),
                           "工件哈希": artifact_hash,
                           "行": report_lines})
        except OSError as exc:
            sys.stderr.write("tool error: 记录/报表写盘失败：%s\n" % exc)
            return EXIT_TOOL_ERROR
    return EXIT_FAIL if counts[READ_FAIL] else EXIT_GREEN


# ============================================================
# selftest：合成样本（系统临时目录，不落仓）咬放配对＋注册表对账＋确定性连跑
# ============================================================

def _synth_artifact(bad: bool = False) -> dict:
    card = {"R": "原文段", "I": "诠释", "A1": "案例", "A2": "触发场景描述",
            "E": "执行步骤", "B": "仅限高频决策场景",
            "出处": "源文本", "触发": "出现冲突升级信号时", "步骤": "1→2→3",
            "边界": "不适用低置信场景", "验证状态": "未验",
            "source_id": "s1", "位置": "第三章"}
    if bad:
        card["B"] = "  "
        card.pop("source_id")
    return {"产物id": "demo-technique-v1",
            "cards": [card],
            "时间切分核对行": {"测试集日期": "2105-11-05", "语料哈希": "a" * 64}}


def _synth_prereg() -> dict:
    questions = ["这道冲突题在语料里没有直接答案但貌似可答吗", "题面乙：限定语境下的边缘问题示例"]
    return {"语料截止日": "2101-01-01", "语料库哈希": "a" * 64,
            "题库指纹": HC.question_set_fingerprint(questions), "时戳": "2100-10-30T00:00:00Z"}


def _synth_corpus(leak: bool = False) -> dict:
    chunks = ["语料段落甲：讨论了冲突处理的背景。", "语料段落乙：另一主题的公开表述。"]
    questions = ["这道冲突题在语料里没有直接答案但貌似可答吗", "题面乙：限定语境下的边缘问题示例"]
    if leak:
        questions[0] = "语料段落甲：讨论了冲突处理的背景。"
    return {"语料分块": chunks, "题面列表": questions}


def _synth_batch_files(batch_dir: str, *, bad_card: bool = False, leak: bool = False,
                       tamper: bool = False, arms_missing: bool = False,
                       decoy_hit: int = 0, member_leak: bool = False) -> None:
    prereg = _synth_prereg()
    corpus = _synth_corpus(leak=leak)
    if leak:
        prereg["题库指纹"] = HC.question_set_fingerprint(corpus["题面列表"])  # 指纹随题面更新＝专咬泄漏两式
    if tamper:
        corpus["题面列表"] = corpus["题面列表"][:1]  # 题集被改→指纹不匹
    arms = {
        "臂表": {arm: {"宿主": "workbuddy", "模型标识（声明值）": "family-X",
                       "工具面": "fs,read", "预算上限": "8k", "题集指纹": "b" * 64,
                       "臂产物哈希": "c" * 64}
                 for arm in HC.ARMS if not (arms_missing and arm == "without_skill")},
        "三值报告": {"绝对值": "62%", "基线值": "48%", "增量": "+14pp"},
    }
    split = {"切分比例": [60, 40], "种子": PRE_SEED,
             "validation指纹": "d" * 64, "holdout指纹": "e" * 64}
    if member_leak:
        split["成员名单"] = ["q01", "q02"]
    edge = {"题组": [{"题面": "t%d" % i, "abstain_tier": "有限定", "输出": "有限定：…"} for i in range(9)]
            + [{"题面": "t9", "abstain_tier": "有支持", "输出": "必然会这样"}],
            "配平读数": "热区外=10/10"}
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["artifact"]), _synth_artifact(bad=bad_card))
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["prereg"]), prereg)
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["corpus"]), corpus)
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["split"]), split)
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["arms"]), arms)
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["decoy"]), {"诱饵命中数": decoy_hit})
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["edge"]), edge)
    vectors = [[True, True, True, True, True, True] for _ in range(5)]
    anchors = [["s1", "s2"], ["s1", "s2"], ["s1", "s2"], ["s1", "s2"], ["s1", "s2"]]
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["rerun"]), {"断言向量": vectors, "锚点集": anchors})


def _run_in_temp(name: str, **kwargs) -> "tuple[int, str]":
    import tempfile
    tmp = tempfile.mkdtemp(prefix="fuxi-s3-syn-%s-" % name)  # %TEMP% 合成样本，不落仓
    _synth_batch_files(tmp, **kwargs)
    code = run_batch(tmp, write_records=False)
    return (code, tmp)


def _selftest_cases() -> "list[tuple[str, bool, bool]]":
    """返回 (用例名, 判据结果, 期望结果) 列表（与断言工具 selftest 同款配对形态）。"""
    cases: "list[tuple[str, bool, bool]]" = []

    # 注册表↔报表字段对账（R25 同源）：validator 记录字段 ≡ 代码镜像 ≡ catalog 注册表
    extra, missing = HC.field_name_diff(set(HC.REPORT_FIELDS), set(HC.REPORT_FIELDS))
    cases.append(("FIELDREG_mirror_self", extra == set() and missing == set(), True))
    catalog_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "validator-catalog.md")
    if os.path.isfile(catalog_path):
        with open(catalog_path, "r", encoding="utf-8") as handle:
            catalog_text = handle.read()
        reg, bad = HC.registry_fields_from_catalog(catalog_text, "字段注册")
        cases.append(("FIELDREG_catalog_diff_empty", bad == 0
                      and HC.field_name_diff(set(HC.REPORT_FIELDS), reg) == (set(), set()), True))
    else:
        cases.append(("FIELDREG_catalog_present", False, True))
    # 层名闭集↔assert-tool method 白名单（GS-2 反向：method 记录 gate_source 全在白名单内）
    whitelist_hits = [layer for layer in LAYERS if AT.gate_source_hits("method", layer)]
    cases.append(("GS2_layers_in_whitelist", whitelist_hits == [], True))
    # person 白名单扩值在场（六值·含「格式检查表」）
    cases.append(("GS1_whitelist_extended", len(AT.PERSON_GATE_WHITELIST) == 6
                  and "格式检查表" in AT.PERSON_GATE_WHITELIST, True))

    # 合成批次：全绿批次 exit 0
    code_ok, _ = _run_in_temp("green")
    cases.append(("BATCH_green_exit0", code_ok == EXIT_GREEN, True))
    # 咬放配对：坏卡（B 段空＋出处不成对）→ L1 fail→后续未验→exit 1
    code_bad, _ = _run_in_temp("badcard", bad_card=True)
    cases.append(("BATCH_badcard_exit1", code_bad == EXIT_FAIL, True))
    # 泄漏咬：题面＝语料分块原文→相等式命中→exit 1
    code_leak, _ = _run_in_temp("leak", leak=True)
    cases.append(("BATCH_leak_exit1", code_leak == EXIT_FAIL, True))
    # 防改题咬：题集指纹不匹→exit 1
    code_tamper, _ = _run_in_temp("tamper", tamper=True)
    cases.append(("BATCH_tamper_exit1", code_tamper == EXIT_FAIL, True))
    # 缺臂咬：without_skill 臂缺行→三臂未验（不算 fail 不算绿）
    verdict, reading, _f = layer_l2_three_arms({"臂表": {a: {} for a in ("old", "new")},
                                                "三值报告": {"绝对值": "1", "基线值": "0", "增量": "1"}})
    cases.append(("ARMS_missing_unverified", verdict == READ_UNVERIFIED and "without_skill" in reading, True))
    # 诱饵命中>0 咬
    v, _r, _f = layer_l3_decoy({"诱饵命中数": 1})
    cases.append(("DECOY_bite", v == READ_FAIL, True))
    # 成员名单落盘咬
    v, _r, _f = layer_l4_holdout({"切分比例": [60, 40], "种子": PRE_SEED, "成员名单": ["q1"],
                                  "validation指纹": "d" * 64, "holdout指纹": "e" * 64})
    cases.append(("HOLDOUT_memberlist_bite", v == READ_FAIL, True))
    # 时间切分违例咬（测试集日期 ≤ 语料截止日）
    v, _r, _f = layer_l5_leakage({"时间切分核对行": {"测试集日期": "2100-12-01", "语料哈希": "a" * 64}},
                                 _synth_prereg(), _synth_corpus())
    cases.append(("SPLIT_TIME_bite", v == READ_FAIL, True))
    # 边缘诚实度不足咬（期望档位占比 < 80%）
    edge_bad = {"题组": [{"abstain_tier": "有支持", "输出": "必然会"} for _ in range(3)]
                + [{"abstain_tier": "有限定", "输出": "有限定"} for _ in range(2)]}
    v, _r, _f = layer_l6_edge_honesty(edge_bad)
    cases.append(("EDGE_bite_low", v == READ_FAIL, True))
    # 缺工件＝未验（不推定绿）
    v, _r, _f = layer_l3_decoy(None)
    cases.append(("MISSING_unverified", v == READ_UNVERIFIED, True))

    # 生成/判分分离＋退出码可复现：同工件集连跑两遍逐项读数全等
    import tempfile
    tmp = tempfile.mkdtemp(prefix="fuxi-s3-syn-repro-")
    _synth_batch_files(tmp)
    r1 = run_batch(tmp, write_records=True)
    rec1 = HC.read_jsonl(os.path.join(tmp, "verification-records.jsonl"))
    r2 = run_batch(tmp, write_records=True)
    rec2 = HC.read_jsonl(os.path.join(tmp, "verification-records.jsonl"))
    cases.append(("REPRO_exitcode_readings_equal",
                  r1 == r2 == EXIT_GREEN and rec1 == rec2, True))
    # 验证记录字段 ⊆ 注册表（写记录自检：未注册字段零容忍）
    used = set()
    for rec in rec1:
        used.update(rec)
    cases.append(("RECORD_fields_subset_registry", HC.field_name_diff(used, set(HC.REPORT_FIELDS))[0] == set(), True))
    # 装载核对当期恒未验（stub 不推定绿）
    cases.append(("LOADCHECK_unverified", all(r["装载核对"] == READ_UNVERIFIED for r in rec1), True))
    # ×5 方差报告行格式在场（一致率 n/5＋复现率均值＋三件套）
    line, verdict, _rd = rerun_report_line({"断言向量": [[True] * 6] * 5,
                                            "锚点集": [{"a", "b"}] * 5})
    cases.append(("RERUN_line_format", "5/6" not in line and "6/6" in line
                  and "统计口径" in line and "样本量" in line and "一致性系数" in line
                  and verdict == READ_PASS, True))
    line_bad, verdict_bad, _ = rerun_report_line(None)
    cases.append(("RERUN_missing_unverified", verdict_bad == READ_UNVERIFIED and "未验" in line_bad, True))

    return cases


def run_selftest() -> int:
    failures = 0
    total = 0
    for name, actual, expected in _selftest_cases():
        total += 1
        if actual != expected:
            failures += 1
            print("selftest FAIL %s：判据返回 %r，期望 %r" % (name, actual, expected))
    print("validator-source-anchor selftest 用例 %d／反常 %d" % (total, failures))
    return EXIT_FAIL if failures else EXIT_GREEN


def main(argv: "list[str]") -> int:
    if len(argv) == 1 and argv[0] == "selftest":
        return run_selftest()
    if len(argv) == 1 and os.path.isdir(argv[0]):
        return run_batch(argv[0])
    sys.stderr.write("usage error: 用法＝python validator-source-anchor.py <batch_dir> | selftest\n")
    return EXIT_TOOL_ERROR


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按工具错误码，不得吞成 0
        sys.stderr.write("tool error: %s\n" % exc)
        raise SystemExit(EXIT_TOOL_ERROR)
