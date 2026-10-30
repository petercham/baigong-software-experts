#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fuxi-skill · public-anchor validator（person 轨软门·S3 建）。

性质＝交付件本体。层结构（顺序执行，前层 fail 不进后层；层名即 gate_source 注册词）：
    L0 格式检查表 → L1 盲评rubric → L2 绝对线 → L3 decoy → L4 泄漏检查 → L5 人工锚点卡
门禁资格两制（当期）：
    - `格式检查表`＝当期唯一门禁位（D2 嫁接机械位；S0b 元组未交付态下放行仅依机械断言，R7/R24）；
      `泄漏检查`＝门禁位（确定性判定，不依赖 judge）。
    - judge 层（盲评rubric／绝对线／decoy）分数一律**参考位不作门禁位**（B12/R24：
      无 judge-人类一致率数据→不得作门禁位；S0b 元组交付并 κ 达标后复位）。
      judge 层读数行强制并列打印 `calibration_state` 当前值（缺省即「待校准」，fail-closed）。
    - `人工锚点卡`＝消费 S0b 交付元组；元组未交付→显式记「未验」，不记绿。

生成段／判分段分离：本件＝判分段，只对生成段落盘盲评工件做确定性判定；
同输入连跑退出码与逐项读数全等。

退出码闭集（三值，无其他取值）：
    0 无 fail（未验行不算 fail 不算 pass，汇总单列，不拉码）
    1 任门禁层 fail（judge 层不拉码＝参考位）
    2 工具自身错误（用法错／环境错／输入 json 解析失败，fail-closed 不得吞成 0）

与 assert-tool 的关系＝分立脚本：不从 assert-tool import 判据函数，仅以纯数据常量取
词表/闭集（词表本体单源在 assert-tool 注册位）；GS-4 κ 对账读数面留 assert-tool，
本件 L5 只做元组在场检＋同款口径薄封装（不扩判据）。

用法：
    python validator-public-anchor.py <batch_dir>   # 判分段：对批次工件目录出六层读数
    python validator-public-anchor.py selftest      # 自证：合成样本（系统临时目录，不落仓）咬放配对
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
LAYERS = ("格式检查表", "盲评rubric", "绝对线", "decoy", "泄漏检查", "人工锚点卡")

# ---- 预注册数值包（注册面＝validator-catalog §四·阈值预注册表；中途变更走独立提案）----
ABS_LINE_MEAN = 3.0          # 绝对线：rubric 四维各自均值 ≥3.0（五级锚定量表；C-1 裁值锁定）
RUBRIC_SCALE_MAX = 5         # 量表五级
MIN_JUDGE_FAMILIES = 2       # 裁判跨 ≥2 模型家族（D8）
CONTAIN_MIN_LEN = 20         # 泄漏包含式比对的最小归一化题面长度（规程同 source-anchor §1.3）

# rubric 维度闭集（锚定文本预注册＝validator-catalog 附录；中途变更走独立提案）
RUBRIC_DIMENSIONS = ("声音保真", "框架运用", "弃权表现", "反角色扮演")

# 批次工件目录输入面文件闭集（缺文件＝对应层记未验，fail-closed 不推定绿）
BATCH_FILES = {
    "artifact": "artifact.json",            # perspective 产物实例（五层节＋要素＋正文面）
    "prereg": "prereg.json",                # 两轴切分预注册件（语料截止日＋哈希＋题库指纹）
    "corpus": "corpus-questions.json",      # 语料分块＋题面列表（含锚点题日期）
    "prompts": "test-prompts.json",         # ST-4 回归件（格式检查表对象）
    "blind": "blind-eval.json",             # 生成段盲评工件（跨家族裁判＋位置对调双跑分数）
    "decoy": "decoy-2afc.json",             # 近邻人物盲辨二选一读数（D12 读数源）
    "tuple": "anchor-tuple.json",           # S0b 人工锚点交付元组（κ 点值/区间/实做题数…）
}

# 词表/闭集纯数据常量复用（单源＝assert-tool 注册位）
PERSPECTIVE_SECTIONS = AT.PERSPECTIVE_SECTIONS
ROLEPLAY_BANNED = AT.ROLEPLAY_BANNED_WORDS
BLUNT_WORDS = AT.BLUNT_ASSERTION_WORDS
TEST_PROMPT_FIELDS = AT.TEST_PROMPT_FIELDS
LEAKAGE_OK = "已检-不在语料内"
LEAKAGE_HIT = "已检-在语料内"
CALIBRATION_DEFAULT = "待校准"
KAPPA_THRESHOLD = 0.6        # GS-4 同款口径（读数面单源＝assert-tool gs_4，本件 L5 薄封装同值）


def _read_batch_file(batch_dir: str, key: str):
    """读批次工件 json；缺文件返回 None（层记未验），解析异常上抛按工具错误收。"""
    path = os.path.join(batch_dir, BATCH_FILES[key])
    if not os.path.isfile(path):
        return None
    return HC.read_json(path)


def _dir_artifact_hashes(batch_dir: str) -> str:
    """工件集哈希＝批次内全部已知工件按名序内容哈希再哈希（确定性）。"""
    parts: "list[str]" = []
    for key in sorted(BATCH_FILES):
        path = os.path.join(batch_dir, BATCH_FILES[key])
        if os.path.isfile(path):
            with open(path, "rb") as handle:
                parts.append("%s:%s" % (BATCH_FILES[key], hashlib.sha256(handle.read()).hexdigest()))
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()


def _judge_family_line(blind, decoy) -> "tuple[str, str]":
    """裁判家族＋位置对调两跑两字段读数（缺工件→「待数据」）。"""
    src = blind if blind is not None else decoy
    if src is None:
        return ("待数据", "待数据")
    fams = src.get("裁判家族", [])
    swap = src.get("位置对调两跑", "")
    fam_line = "、".join(str(f) for f in fams) if fams else "待数据"
    return (fam_line, str(swap) if swap else "待数据")


# ============================================================
# 六层判定函数（纯函数·确定性；返回 (判定, 读数文本, 附加字段 dict)）
# ============================================================

def layer_l0_format_checklist(artifact, prompts) -> "tuple[str, str, dict]":
    """L0 格式检查表（D2 嫁接机械位·当期唯一门禁位）：先判后盲评，L0 fail 不进盲评层。

    检项：五层节闭集 diff＝∅（ST-3 perspective 侧）＋禁用词（BW-1 角色扮演禁语＋BW-2
    无据断言词）命中＝0＋test-prompts 回归件在场可解析且条目字段 ⊆ ST-4 闭集＋
    要素三态标注 source_id/位置 成对（FC-3）。全部确定性判定，不依赖 judge。
    """
    if artifact is None:
        return (READ_UNVERIFIED, "产物工件不在场（规程在场待数据）", {})
    problems: "list[str]" = []
    # ① 五层节闭集 diff＝∅
    sections = list(artifact.get("五层节", {}).keys())
    extra, missing = HC_section_diff(sections)
    if extra or missing:
        problems.append("五层节 diff 多出%s 缺失%s" % (sorted(extra), sorted(missing)))
    # ② 禁用词命中＝0（BW-1＋BW-2 词表纯数据复用）
    body = json.dumps(artifact, ensure_ascii=False)
    rp_hits = [w for w in ROLEPLAY_BANNED if w in body]
    blunt_hits = [w for w in BLUNT_WORDS if w in body]
    if rp_hits:
        problems.append("角色扮演禁语命中%s（BW-1）" % rp_hits)
    if blunt_hits:
        problems.append("无据断言词命中%s（BW-2）" % blunt_hits)
    # ③ test-prompts 回归件在场可解析＋条目字段闭集
    if prompts is None:
        problems.append("test-prompts 回归件不在场（ST-4）")
    else:
        entries = prompts.get("条目", [])
        if not entries:
            problems.append("test-prompts 条目空（ST-4）")
        for idx, entry in enumerate(entries, 1):
            bad = sorted(set(entry) - set(TEST_PROMPT_FIELDS))
            if bad:
                problems.append("回归条目%d 未注册字段%s" % (idx, bad))
    # ④ 要素三态标注成对（FC-3）
    elements = artifact.get("要素", [])
    for idx, el in enumerate(elements, 1):
        has_id = bool(str(el.get("source_id", "")).strip())
        has_loc = bool(str(el.get("位置", "")).strip())
        if has_id != has_loc:
            problems.append("要素%d source_id/位置 不成对（FC-3）" % idx)
    if problems:
        return (READ_FAIL, "；".join(problems), {})
    return (READ_PASS, "五层节 diff=∅·禁语命中=0·回归件 %d 条目字段闭集·要素成对（当期唯一门禁位判绿）"
            % (len(prompts.get("条目", [])) if prompts else 0), {})


def HC_section_diff(sections: "list[str]") -> "tuple[set, set]":
    """五层节 diff（复用 harness 部件字段名 diff 语义，闭集常量＝assert-tool 注册位纯数据）。"""
    return HC.field_name_diff(set(sections), set(PERSPECTIVE_SECTIONS))


def _dim_means(blind) -> "dict[str, float]":
    """盲评工件面各维分数均值（确定性算术平均；两跑取平均口径在生成段落盘分次分数）。"""
    acc: "dict[str, list[float]]" = {d: [] for d in RUBRIC_DIMENSIONS}
    for entry in blind.get("评分", []):
        scores = entry.get("分数", {})
        for dim in RUBRIC_DIMENSIONS:
            val = scores.get(dim)
            if isinstance(val, (int, float)) and 1 <= val <= RUBRIC_SCALE_MAX:
                acc[dim].append(float(val))
    return {d: (sum(v) / len(v)) for d, v in acc.items() if v}


def layer_l1_blind_rubric(blind) -> "tuple[str, str, dict]":
    """L1 盲评rubric（参考位）：judge 跨 ≥2 家族＋位置对调双跑；分数只作参考位不作门禁位。

    当期判定恒记「未验」（无 judge-人类一致率数据＝无门禁资格，B12/R24；
    S0b 元组交付并 κ 达标后复位）；读数行强制并列 calibration_state（调用方保证）。
    """
    if blind is None:
        return (READ_UNVERIFIED, "盲评工件不在场（规程在场待数据·参考位）", {})
    fams = blind.get("裁判家族", [])
    swap = str(blind.get("位置对调两跑", ""))
    means = _dim_means(blind)
    if len(fams) < MIN_JUDGE_FAMILIES or len(set(fams)) < MIN_JUDGE_FAMILIES:
        return (READ_UNVERIFIED, "裁判家族数 %d＜%d（D8 跨家规程未满足→记未验·参考位）"
                % (len(set(fams)), MIN_JUDGE_FAMILIES), {})
    if swap != "已完成":
        return (READ_UNVERIFIED, "位置对调两跑=%s（双跑取平均规程未满足→记未验·参考位）" % swap, {})
    if not means:
        return (READ_UNVERIFIED, "盲评分数面空（记未验·参考位）", {})
    dims = "／".join("%s=%.1f" % (d, means[d]) for d in RUBRIC_DIMENSIONS if d in means)
    reading = "四维均值 %s（参考位·judge 分数不作门禁位 B12/R24·裁判家族 %d 家·位置对调双跑已完成）" % (
        dims, len(set(fams)))
    return (READ_UNVERIFIED, reading,
            {"裁判家族": "、".join(str(f) for f in fams), "位置对调两跑": swap})


def layer_l2_absolute_line(blind) -> "tuple[str, str, dict]":
    """L2 绝对线（参考位）：四维各自均值 ≥3.0（五级量表·C-1 裁值预注册锁定）＋必附三值报告。

    判定恒记「未验」（同 L1 参考位口径）；三值报告缺一行记未验（R10）。
    """
    if blind is None:
        return (READ_UNVERIFIED, "盲评工件不在场（规程在场待数据·参考位）", {})
    means = _dim_means(blind)
    missing_dims = [d for d in RUBRIC_DIMENSIONS if d not in means]
    if missing_dims:
        return (READ_UNVERIFIED, "缺维度读数%s→记未验（四维各自均值线不可判·参考位）" % missing_dims, {})
    below = [d for d in RUBRIC_DIMENSIONS if means[d] < ABS_LINE_MEAN]
    three = blind.get("三值报告", {})
    three_missing = [k for k in ("绝对值", "基线值", "增量") if not str(three.get(k, "")).strip()]
    line_txt = "绝对线=%s（四维各自均值≥%.1f·五级量表·预注册锁定）" % ("四维各自均值线", ABS_LINE_MEAN)
    if three_missing:
        return (READ_UNVERIFIED, "%s·三值报告缺%s行→记未验（R10 缺一记未验·参考位）"
                % (line_txt, three_missing), {})
    status = "全维过线" if not below else "低于线维度%s" % below
    reading = "%s·%s·三值报告 %s/%s/%s（参考位·不作门禁位）" % (
        line_txt, status, three["绝对值"], three["基线值"], three["增量"])
    return (READ_UNVERIFIED, reading, {})


def layer_l3_decoy_2afc(decoy) -> "tuple[str, str, dict]":
    """L3 decoy（参考位）：近邻人物盲辨二选一（2AFC）；读数＝辨认正确率＝D12 独立报告行读数源。

    该行与 D12 排他性正确率独立报告行同源**不并分**（报表无聚合总分字段）；
    规程行本身属验收行；裁判判定同受 R24 约束→当期判定记未验（参考位）。
    """
    if decoy is None:
        return (READ_UNVERIFIED, "2AFC 读数不在场（规程在场待数据·参考位）", {})
    acc = decoy.get("辨认正确率", None)
    n = decoy.get("样本量", 0)
    fams = decoy.get("裁判家族", [])
    swap = str(decoy.get("位置对调两跑", ""))
    if not isinstance(acc, (int, float)) or not isinstance(n, int) or n <= 0:
        return (READ_FAIL, "2AFC 读数形态不合法（正确率/样本量缺失，fail-closed）", {})
    if len(set(fams)) < MIN_JUDGE_FAMILIES or swap != "已完成":
        return (READ_UNVERIFIED, "2AFC 跨家/双跑规程未满足→记未验（规程行本身属验收行·参考位）", {})
    reading = ("辨认正确率 %.0f%%（统计口径：2AFC 位置对调双跑均值；样本量 %d；一致性系数见裁判家族行）"
               "·裁判家族 %d 家·与 D12 独立报告行同源不并分" % (acc * 100, n, len(set(fams))))
    return (READ_UNVERIFIED, reading,
            {"裁判家族": "、".join(str(f) for f in fams), "位置对调两跑": swap})


def layer_l4_leakage(prereg, corpus) -> "tuple[str, str, dict]":
    """L4 泄漏检查（门禁位·确定性判定不依赖 judge）：规程同 source-anchor §1.3。

    哈希两式＋题库指纹防改校验；锚点题取语料截止日之后（R13/§9.6 person 轨 T 定义照引）；
    命中→FM-P-04 阻断（fail）；缺预注册件/缺工件→未验（fail-closed）。
    """
    fields = {"leakage_check": "未检"}
    if prereg is None:
        return (READ_UNVERIFIED, "两轴切分预注册件不在场→该对象评估记未验（fail-closed）", fields)
    if corpus is None:
        return (READ_UNVERIFIED, "语料/题面工件不在场→记未验", fields)
    questions = [str(q.get("题面", "")) for q in corpus.get("题面列表", [])]
    # 防改题校验
    if HC.question_set_fingerprint(questions) != str(prereg.get("题库指纹", "")):
        return (READ_FAIL, "题库被改：重算指纹≠预注册题库指纹（预注册冻结纪律）", fields)
    # 锚点题日期检：锚点题取语料截止日之后
    c_date = HC.date_key(str(prereg.get("语料截止日", "")))
    bad_anchor: "list[str]" = []
    for q in corpus.get("题面列表", []):
        if str(q.get("是否锚点题", "")) == "是":
            a_date = HC.date_key(str(q.get("题目日期", "")))
            if a_date < 0 or a_date <= c_date:
                bad_anchor.append(str(q.get("题面", ""))[:20])
    if bad_anchor:
        return (READ_FAIL, "锚点题不落语料截止日之后（R13/§9.6）：%s" % bad_anchor, fields)
    # 哈希两式
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
        return (READ_FAIL, "泄漏命中 %d 题（%s）→FM-P-04 阻断" % (len(hit_q), "、".join(hit_q[:3])), fields)
    fields["时间切分核对行"] = "锚点题日期>语料截止日(%s)|语料哈希=%s" % (
        prereg.get("语料截止日"), str(prereg.get("语料库哈希", ""))[:12])
    return (READ_PASS, "哈希两式全不命中·题库指纹对账一致·锚点题日期均在语料截止日之后（门禁位判绿）", fields)


def kappa_consistent_thin(calibration_state: str, kappa_report) -> bool:
    """GS-4 同款口径薄封装（判据读数面单源＝assert-tool gs_4；本封装只做在场对账，不扩判据）。"""
    if kappa_report is None:
        return calibration_state == "待校准"
    point = kappa_report.get("点值", 0.0)
    lower = kappa_report.get("区间下界", 0.0)
    if point >= KAPPA_THRESHOLD and lower >= KAPPA_THRESHOLD:
        return calibration_state == "校准态"
    return calibration_state == "待校准"


def layer_l5_anchor_card(tuple_obj) -> "tuple[str, str, dict]":
    """L5 人工锚点卡：消费 S0b 交付元组（κ 点值/区间/实做题数/补题题记录/受限登记，R9）。

    当期 S0b 未交付（盘上无预注册件、无元组）→显式记「未验」，不记绿；
    元组交付前 L1-L3 分数一律参考位（DeepSeek 改写句口径：不阻塞＝工程推进不等待，放行判据不降低）。
    """
    if tuple_obj is None:
        return (READ_UNVERIFIED,
                "S0b 人工锚点交付元组未交付（盘上无元组）→记未验，不以 stub/总通过推定绿",
                {"calibration_state": CALIBRATION_DEFAULT})
    need = ("κ点值", "κ区间下界", "实做题数")
    miss = [k for k in need if tuple_obj.get(k) in (None, "")]
    if miss:
        return (READ_UNVERIFIED, "元组缺字段%s→记未验（fail-closed）" % miss,
                {"calibration_state": CALIBRATION_DEFAULT})
    state = str(tuple_obj.get("calibration_state", CALIBRATION_DEFAULT))
    kappa = {"点值": tuple_obj["κ点值"], "区间下界": tuple_obj["κ区间下界"]}
    if not kappa_consistent_thin(state, kappa):
        return (READ_FAIL, "calibration_state 与 κ 报告不一致（GS-4 口径对账 fail-closed）→待校准阻断放行",
                {"calibration_state": "待校准"})
    return (READ_PASS, "元组在场·κ 对账一致（calibration_state=%s·实做题数 %s）→judge 层复位门禁资格待独立提案"
            % (state, tuple_obj["实做题数"]), {"calibration_state": state})


# ============================================================
# 批次执行（判分段主流程：逐层读数→报表行→验证记录 jsonl；报表无聚合总分字段）
# ============================================================

def run_batch(batch_dir: str, write_records: bool = True) -> int:
    """对批次工件目录跑六层＋D12 独立行；写出报表与验证记录；退出码闭集。"""
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
    calib_state = CALIBRATION_DEFAULT
    if inputs["tuple"] is not None:
        calib_state = str(inputs["tuple"].get("calibration_state", CALIBRATION_DEFAULT))
    family_line, swap_line = _judge_family_line(inputs["blind"], inputs["decoy"])

    results: "list[tuple[str, str, str, dict]]" = []
    blocked = False
    layer_defs = [
        ("格式检查表", lambda: layer_l0_format_checklist(artifact, inputs["prompts"])),
        ("盲评rubric", lambda: layer_l1_blind_rubric(inputs["blind"])),
        ("绝对线", lambda: layer_l2_absolute_line(inputs["blind"])),
        ("decoy", lambda: layer_l3_decoy_2afc(inputs["decoy"])),
        ("泄漏检查", lambda: layer_l4_leakage(prereg, inputs["corpus"])),
        ("人工锚点卡", lambda: layer_l5_anchor_card(inputs["tuple"])),
    ]
    for layer_name, fn in layer_defs:
        if blocked:
            results.append((layer_name, READ_UNVERIFIED, "前层 fail 不进后层（先判后盲评顺序纪律）", {}))
            continue
        verdict, reading, extra = fn()
        results.append((layer_name, verdict, reading, extra))
        # L0 格式检查表 fail＝不进盲评层；L4 泄漏 fail＝FM-P-04 阻断后续锚点层
        if verdict == READ_FAIL and layer_name in ("格式检查表",):
            blocked = True

    counts = {READ_PASS: 0, READ_FAIL: 0, READ_UNVERIFIED: 0}
    report_lines: "list[str]" = ["产物id\t%s" % (str(artifact.get("产物id", "")) if artifact else "")]
    records: "list[dict]" = []
    judge_layers = ("盲评rubric", "绝对线", "decoy")
    for seq, (layer_name, verdict, reading, extra) in enumerate(results, 1):
        counts[verdict] += 1
        # judge 层读数行强制并列打印 calibration_state（缺省即「待校准」，fail-closed）
        if layer_name in judge_layers:
            report_lines.append(HC.format_report_line("L%d %s" % (seq, layer_name), reading, verdict, calib_state))
        else:
            report_lines.append(HC.format_report_line("L%d %s" % (seq, layer_name), reading, verdict))
        rec = HC.record_skeleton()
        rec.update({
            "记录id": "%s-P%02d" % (os.path.basename(batch_dir.rstrip("\\/")), seq),
            "产物id": str(artifact.get("产物id", "")) if artifact else "",
            "所属轨": "person",
            "层名": layer_name,
            "gate_source": layer_name,
            "读数": reading,
            "判定": verdict,
            "工件哈希": artifact_hash,
            "预注册件哈希": prereg_hash,
            "calibration_state": calib_state,
            "evidence_grade": ("机械断言" if layer_name in ("格式检查表", "泄漏检查") else "LLM 判定"),
            "裁判家族": extra.get("裁判家族", family_line),
            "位置对调两跑": extra.get("位置对调两跑", swap_line),
        })
        for key, val in extra.items():
            if key not in ("裁判家族", "位置对调两跑"):
                rec[key] = val
        records.append(rec)
    # D12 排他性辨认正确率独立报告行（与 L3 decoy 同源不并分；报表无聚合总分字段）
    d12_reading = "读数不在场"
    d12_verdict = READ_UNVERIFIED
    if inputs["decoy"] is not None:
        for _seq, (layer_name, verdict, reading, _e) in enumerate(results, 1):
            if layer_name == "decoy":
                d12_reading = reading
                d12_verdict = verdict
                break
    report_lines.append(HC.format_d12_line(d12_reading, d12_verdict))
    # 装载核对字段位预留（当期恒未验——R20 装载记录导出接口实证不可得，不以 stub 推定绿）
    for rec in records:
        rec["装载核对"] = READ_UNVERIFIED

    report_lines.append("汇总\tPASS=%d FAIL=%d 未验=%d\t%s"
                        % (counts[READ_PASS], counts[READ_FAIL], counts[READ_UNVERIFIED],
                           "门禁层FAIL存在→退出1" if counts[READ_FAIL] else "无门禁层FAIL→退出0"))
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
    sections = {name: "内容段" for name in PERSPECTIVE_SECTIONS}
    elements = [{"source_id": "s1", "位置": "第二章"}]
    if bad:
        sections.pop("反模式")
        elements = [{"source_id": "s1"}]
    art = {"产物id": "demo-perspective-v1", "五层节": sections, "要素": elements}
    if bad:
        art["正文注记"] = "接下来我以他的名义作答，他必然会否决"
    return art


def _synth_prompts() -> dict:
    return {"条目": [{"用例id": "tp01", "题面": "边缘题", "期望档位": "有限定",
                      "所属轨": "person", "是否锚点题": "是"}]}


def _synth_prereg() -> dict:
    questions = ["锚点题干甲：他在公开场合如何界定该框架的适用边界", "题面乙：貌似可答的边缘问题"]
    return {"语料截止日": "2101-01-01", "语料库哈希": "a" * 64,
            "题库指纹": HC.question_set_fingerprint(questions)}


def _synth_corpus(leak: bool = False, bad_anchor: bool = False) -> dict:
    chunks = ["语料段落甲：框架背景讨论。", "语料段落乙：另一主题公开表述。"]
    anchor_date = "2100-12-01" if bad_anchor else "2103-03-15"
    questions = [{"题面": "锚点题干甲：他在公开场合如何界定该框架的适用边界",
                  "是否锚点题": "是", "题目日期": anchor_date},
                 {"题面": "题面乙：貌似可答的边缘问题", "是否锚点题": "否", "题目日期": "2102-02-10"}]
    if leak:
        questions[0]["题面"] = "语料段落甲：框架背景讨论。"
    return {"语料分块": chunks, "题面列表": questions}


def _synth_blind() -> dict:
    return {"裁判家族": ["family-A", "family-B"], "位置对调两跑": "已完成",
            "评分": [{"judge": "family-A", "run": 1, "分数": {d: 4 for d in RUBRIC_DIMENSIONS}},
                     {"judge": "family-A", "run": 2, "分数": {d: 3 for d in RUBRIC_DIMENSIONS}},
                     {"judge": "family-B", "run": 1, "分数": {d: 4 for d in RUBRIC_DIMENSIONS}},
                     {"judge": "family-B", "run": 2, "分数": {d: 3 for d in RUBRIC_DIMENSIONS}}],
            "三值报告": {"绝对值": "4.0", "基线值": "3.0", "增量": "+1.0"}}


def _synth_decoy() -> dict:
    return {"裁判家族": ["family-A", "family-B"], "位置对调两跑": "已完成",
            "辨认正确率": 0.8, "样本量": 10}


def _synth_batch_files(batch_dir: str, *, bad_artifact: bool = False, leak: bool = False,
                       bad_anchor: bool = False, no_prompts: bool = False,
                       blind_bad_family: bool = False, with_tuple: bool = False) -> None:
    prereg = _synth_prereg()
    corpus = _synth_corpus(leak=leak, bad_anchor=bad_anchor)
    if leak:
        corpus_q = [q["题面"] for q in corpus["题面列表"]]
        prereg["题库指纹"] = HC.question_set_fingerprint(corpus_q)  # 指纹随题面更新，专咬泄漏两式
    blind = _synth_blind()
    if blind_bad_family:
        blind["裁判家族"] = ["family-A"]
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["artifact"]), _synth_artifact(bad=bad_artifact))
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["prereg"]), prereg)
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["corpus"]), corpus)
    if not no_prompts:
        HC.write_json(os.path.join(batch_dir, BATCH_FILES["prompts"]), _synth_prompts())
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["blind"]), blind)
    HC.write_json(os.path.join(batch_dir, BATCH_FILES["decoy"]), _synth_decoy())
    if with_tuple:
        HC.write_json(os.path.join(batch_dir, BATCH_FILES["tuple"]),
                      {"κ点值": 0.7, "κ区间下界": 0.62, "实做题数": 8, "calibration_state": "校准态"})


def _run_in_temp(name: str, **kwargs) -> int:
    import tempfile
    tmp = tempfile.mkdtemp(prefix="fuxi-s3-pub-%s-" % name)  # %TEMP% 合成样本，不落仓
    _synth_batch_files(tmp, **kwargs)
    return run_batch(tmp, write_records=False)


def _selftest_cases() -> "list[tuple[str, bool, bool]]":
    """返回 (用例名, 判据结果, 期望结果) 列表（与断言工具 selftest 同款配对形态）。"""
    cases: "list[tuple[str, bool, bool]]" = []

    # 注册表↔记录字段对账（R25 同源）：代码镜像 ≡ catalog 注册表（双向 diff＝∅）
    catalog_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "validator-catalog.md")
    if os.path.isfile(catalog_path):
        with open(catalog_path, "r", encoding="utf-8") as handle:
            reg, bad = HC.registry_fields_from_catalog(handle.read(), "字段注册")
        cases.append(("FIELDREG_catalog_diff_empty", bad == 0
                      and HC.field_name_diff(set(HC.REPORT_FIELDS), reg) == (set(), set()), True))
    else:
        cases.append(("FIELDREG_catalog_present", False, True))
    # 层名闭集↔person 白名单（GS-1 反向：person 记录 gate_source 全在白名单内）
    whitelist_hits = [layer for layer in LAYERS if AT.gate_source_hits("person", layer)]
    cases.append(("GS1_layers_in_whitelist", whitelist_hits == [], True))
    # person 白名单六值扩值在场（含「格式检查表」·与 method「机械断言」刻意异名）
    cases.append(("GS1_whitelist_six", len(AT.PERSON_GATE_WHITELIST) == 6
                  and "格式检查表" in AT.PERSON_GATE_WHITELIST
                  and "格式检查表" not in AT.METHOD_GATE_WHITELIST, True))

    # 合成批次：全绿批次 exit 0（judge 层未验不拉码）
    cases.append(("BATCH_green_exit0", _run_in_temp("green") == EXIT_GREEN, True))
    # 咬放配对：坏产物（缺节＋禁语＋要素不成对）→L0 fail→后续未验→exit 1
    cases.append(("BATCH_badartifact_exit1", _run_in_temp("badart", bad_artifact=True) == EXIT_FAIL, True))
    # 回归件缺位咬（L0 fail）
    cases.append(("BATCH_noprompts_exit1", _run_in_temp("noprompt", no_prompts=True) == EXIT_FAIL, True))
    # 泄漏咬（门禁位·题面＝语料分块原文）
    cases.append(("BATCH_leak_exit1", _run_in_temp("leak", leak=True) == EXIT_FAIL, True))
    # 锚点题日期违例咬（不落语料截止日之后）
    cases.append(("BATCH_badanchor_exit1", _run_in_temp("badanchor", bad_anchor=True) == EXIT_FAIL, True))
    # judge 层单家族＝规程未满足→未验不拉码（exit 0，禁假绿）
    cases.append(("BATCH_singlefamily_exit0_unverified",
                  _run_in_temp("fam1", blind_bad_family=True) == EXIT_GREEN, True))
    # S0b 元组未交付＝人工锚点卡记未验（不记绿）
    v, reading, _f = layer_l5_anchor_card(None)
    cases.append(("ANCHORCARD_unverified", v == READ_UNVERIFIED and "未验" in reading, True))
    # 元组在场＋κ 一致→复位读数（配对放例）；κ 不一致→咬
    v2, _r2, _f2 = layer_l5_anchor_card({"κ点值": 0.7, "κ区间下界": 0.62, "实做题数": 8,
                                          "calibration_state": "校准态"})
    v3, _r3, _f3 = layer_l5_anchor_card({"κ点值": 0.65, "κ区间下界": 0.55, "实做题数": 8,
                                          "calibration_state": "校准态"})
    cases.append(("ANCHORCARD_kappa_pass", v2 == READ_PASS, True))
    cases.append(("ANCHORCARD_kappa_bite", v3 == READ_FAIL, True))

    # judge 层判定恒未验（参考位不作门禁位）：盲评在场仍不记绿
    v4, reading4, _f4 = layer_l1_blind_rubric(_synth_blind())
    cases.append(("JUDGE_reference_only", v4 == READ_UNVERIFIED and "参考位" in reading4, True))
    v5, _r5, _f5 = layer_l2_absolute_line(_synth_blind())
    cases.append(("ABSLINE_reference_unverified", v5 == READ_UNVERIFIED, True))
    v6, _r6, _f6 = layer_l3_decoy_2afc(_synth_decoy())
    cases.append(("DECOY_reference_unverified", v6 == READ_UNVERIFIED, True))

    # 生成/判分分离＋退出码可复现：同工件集连跑两遍逐项读数全等
    import tempfile
    tmp = tempfile.mkdtemp(prefix="fuxi-s3-pub-repro-")
    _synth_batch_files(tmp)
    r1 = run_batch(tmp, write_records=True)
    rec1 = HC.read_jsonl(os.path.join(tmp, "verification-records.jsonl"))
    rep1 = HC.read_json(os.path.join(tmp, "report.json"))
    r2 = run_batch(tmp, write_records=True)
    rec2 = HC.read_jsonl(os.path.join(tmp, "verification-records.jsonl"))
    cases.append(("REPRO_exitcode_readings_equal",
                  r1 == r2 == EXIT_GREEN and rec1 == rec2, True))
    # judge 层报表行强制并列 calibration_state（fail-closed 缺省待校准）
    judge_lines = [ln for ln in rep1["行"] if any(("L%d " % i) in ln and layer in ln
                   for i, layer in ((2, "盲评rubric"), (3, "绝对线"), (4, "decoy")))]
    cases.append(("CALIB_printed_on_judge_lines",
                  len(judge_lines) == 3 and all("calibration_state=待校准" in ln for ln in judge_lines), True))
    # D12 独立报告行在场＋报表无聚合总分字段（不得并入总分）
    d12_lines = [ln for ln in rep1["行"] if ln.startswith("D12排他性辨认正确率")]
    total_hit = [ln for ln in rep1["行"] if "总分" in ln]
    cases.append(("D12_indep_line_present", len(d12_lines) == 1, True))
    cases.append(("NO_TOTAL_SCORE_FIELD", total_hit == [], True))
    # 验证记录字段 ⊆ 注册表（写记录自检：未注册字段零容忍）
    used: "set[str]" = set()
    for rec in rec1:
        used.update(rec)
    cases.append(("RECORD_fields_subset_registry", HC.field_name_diff(used, set(HC.REPORT_FIELDS))[0] == set(), True))
    # 装载核对当期恒未验（stub 不推定绿）
    cases.append(("LOADCHECK_unverified", all(r["装载核对"] == READ_UNVERIFIED for r in rec1), True))
    # 记录层名均在层名闭集（validator 写记录自检，两处同一注册表之实例侧）
    cases.append(("RECORD_layers_closed", all(r["层名"] in LAYERS for r in rec1), True))

    return cases


def run_selftest() -> int:
    failures = 0
    total = 0
    for name, actual, expected in _selftest_cases():
        total += 1
        if actual != expected:
            failures += 1
            print("selftest FAIL %s：判据返回 %r，期望 %r" % (name, actual, expected))
    print("validator-public-anchor selftest 用例 %d／反常 %d" % (total, failures))
    return EXIT_FAIL if failures else EXIT_GREEN


def main(argv: "list[str]") -> int:
    if len(argv) == 1 and argv[0] == "selftest":
        return run_selftest()
    if len(argv) == 1 and os.path.isdir(argv[0]):
        return run_batch(argv[0])
    sys.stderr.write("usage error: 用法＝python validator-public-anchor.py <batch_dir> | selftest\n")
    return EXIT_TOOL_ERROR


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as exc:  # fail-closed：未预期异常按工具错误码，不得吞成 0
        sys.stderr.write("tool error: %s\n" % exc)
        raise SystemExit(EXIT_TOOL_ERROR)
