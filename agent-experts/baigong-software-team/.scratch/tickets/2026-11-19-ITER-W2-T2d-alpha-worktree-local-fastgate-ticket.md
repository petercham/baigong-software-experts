# ITER-W2-T2d-α · worktree 本地快闸票（v1·架构席起草·薄票形制照 thin-ticket-template 79 行 08fb0f5b）

本票承载一件事：worktree 投递窗单笔 commit 全闸成本从主仓根回退态 8～10 分钟降到 worktree 根 60 秒内——手段＝本包新建 .githooks／ 目录承载 pre-commit＋post-commit 两枚钩子本体（动态根＝rev-parse --show-toplevel）＋主理人窗设 per-worktree 键 core.hooksPath 指入。主仓 .git／hooks／ 零触碰·share／ 全域零改动·lint 排除条款归主根域 GTFAST 票领办我方只随动。排程真源＝ITER-W1-T1e 收口登记 §八 W2 六项之「闸提速新硬需求」行＋收口族 sparse／infra 缺件归 W2-T2d 消费三处在册（现读引文见 §一）。票面形制真源＝software-orchestration references／thin-ticket-template.md（79 行 08fb0f5b 现读在位）。

模板使用说明（固定）：⟪槽：…⟫＝每票必填／必现跑槽位；未标槽段落＝预置固定行逐字照抄不改。本票纪律＝零反引号零 at；叙述面路径裸文＋全角斜杠；引用原文以 ⟦⟧；命令一律缩进段。

## 〇、分档判据读数（必填·机械入档）

- 声明闭集文件数＝当票 §三 写集具名枚数现数＝**两枚**（S1＋S2 皆新建落 .githooks／）；与计划档位行判据比对＝2≤5 成立。S3 配置动作＝非文件写（per-worktree git 配置键·归主理人投递窗执行）不入闭集计数＝登记为工序步骤；写集闭集外＝本票面一枚落 .scratch／tickets／＋取证族 .scratch／t2daarch／（均不入链面写集口径·票据桶例沿先例）。
- 入线四词命中读数＝按票级放行登记勘正词表（真源形态／文件域／席位职权／工序链）逐词预核声明闭集各面命中计数，当轮现跑：S1 体 0／0／0／0＋S2 体 0／0／0／0（写集两枚＝本票 §三 verbatim 全文含钩子本体逐词现跑·读数见 §二.8）；机械复核判据见 §四 V6（对施工笔 diff 面复跑）。
- 入档结论＝**标准档**（闭集两枚≤5＋四词预核全零命中）；错判即红条款未触发申明＝未触发。如实申报：本票议题语义涉提交链钩子载体层增建＋跨会话工序（配置动作归主理人窗·退役条款涉汇链窗）＝语义重、写集面仅两枚新文件；若施工 diff 面 V6 命中任一＝即停手升全量档呈主理人（含排程影响呈清）。
- 随登＝票面自身申明面四词命中全落 §〇 词表枚举句本体＝申明面＝沿先例口径「票面申明面四词命中不在 V6 射程」（V6 射程＝施工笔 diff 面）；票面自靶 check-pointers exit 0 现跑在册（§二.9）。

## 一、获批登记

- 指令原话：⟦按薄票形制起草 T2d-α 票面一枚。写集＝agent-experts／baigong-software-team／.scratch／tickets／2026-11-19-ITER-W2-T2d-alpha-worktree-local-fastgate-ticket.md⟧＝主理人派工书（2026-11-19 当窗投递·本席新实例 arch-iter-t2da·新体例席零 git 写操作＝提交权归一裁决登记 c34f204e 口径）。
- 问题本体登记口径（主理人实测在册·本席现跑复核见 §二）：主仓钩子现势＝主仓 .git／hooks／pre-commit blob 8b785770 硬编码主仓根两行（声明闸＋exec run-gates）；worktree 每次 commit 回退吃此钩子＝全主仓面扫描＝单笔闸 8～10 分钟（主仓根 529 秒 vs worktree 根 7 秒＝派工在册值）；worktree 侧无本地钩子层＋core.hooksPath 未设＝本席现跑坐实（§二.2）。
- 排程真源逐字（ITER-W1-T1e 收口登记现读·链上 3bcb7f2b 盘面件）：⟦闸提速新硬需求（闸输出静默摘要化＋增量扫描只扫 diff 面＋sparse 存量噪声出清·目标单笔闸成本 1～2 分钟）⟧＝W2-T2d 行内；⟦sparse D 态 1018 枚照登勿处理（skip-worktree 已知存量面＝投递侧处置沿册·机理归 W2-T2d 硬消费）⟧；infra 缺件三处归 W2-T2d 消费在册（T1c 放行 §随登：⟦worktree 侧 run-gates 三处 infra／用法错…三处归 W2-T2d 扫描域界定需求项消费⟧）。本票＝T2d 拆分首发：α＝worktree 本地快闸（本票）；GTFAST＝主根域 lint 排除＋静默摘要化＋infra 缺件出清（主根会话另票·S4 禁动面预判据在册）。
- J-2 甲案条款在册随引（T1e 放行登记 dc83d847 message 现读）：⟦post-commit钩子本体本次不落另票W2-C1收口后⟧＝本票 S2 钩子本体＝该「另票」载体兑现（W2-C1 hook 漂移案型在册＝随动面见 §三 禁动与 §五 H-1）。
- 写集路径清单（仓根相对径·裸文＋全角斜杠·逐枚编号具名）：
  1. agent-experts／baigong-software-team／.githooks／pre-commit（新建·S1 verbatim）
  2. agent-experts／baigong-software-team／.githooks／post-commit（新建·S2 verbatim＝J-2 甲案钩子本体）
- 段界：本票职权属架构席＝起草票面＋两枚钩子本体设计规格 verbatim 写死（§三）＋配置动作工序登记（S3）＋退役条款（S4）；施工（两枚落盘）归工程师席 BUILD＋RECEIPT 段；配置动作与投递归主理人窗；快审归 QA 席；收口归产品席。本笔＝票面起草笔落 .scratch／tickets／，不落链（开票笔归主理人投递），链面零扰动。

## 二、当轮取证读数（现跑·禁抄旧数）

警示行（预置固定·逐字照抄）：本节全部读数＝当轮现跑，下游验收读数各自当轮现跑，本表只作起草态基线对照。

    | 项 | 命令 | 实测读数（当轮现跑） |
    |---|---|---|
    | 时点 | date 现跑 | 2026-11-19 00:08 开工窗（收尾复跑见完工回报 00:21 窗） |
    | HEAD | git rev-parse --short HEAD | 3bcb7f2b4df8aebaca5387b39a0637a3c4eb1a77＝派工预期「T1e 收口四十位」对钉全等（链顶现势） |
    | index.lock | ls 独立 gitdir／index.lock | NO_INDEX_LOCK（worktree 独立 gitdir＝主仓 .git／worktrees／baigong-software-team／现核） |
    | 脏面 | git status --porcelain | staged 零枚＋tracked M 零枚＋?? 零枚（.scratch／t2daarch／取证族居 .gitignore /**/.scratch/* 排除面＝不可见照登）＋sparse D 态 1018 枚照登勿处理投递侧处置沿册 |

本票特有靶面读数行族（命令→输出成对·禁手填）：

1. 主仓钩子现势＋blob 现算对钉：

    cat 主仓 .git/hooks/pre-commit＋python blob sha1 现算
    ＝两行实体：python3 主仓根 share/check-staged-declaration.py --root 主仓根 ‖ exec bash 主仓根 share/run-gates.sh --root 主仓根＋安装器标记行 generated-by: object-audit/scripts/install-hooks.sh；现算 blob＝8b7857701594264421832edd30dae7e401f85719＝派工钉值全等；主仓 post-commit＝absent（NO_MAIN_POST_COMMIT）；主钩行尾制式＝LF。

2. worktree 钩子层缺位三证：

    git config --get core.hooksPath → exit 1（未设坐实）
    ls 主仓 .git/worktrees/baigong-software-team/hooks/ → 目录不存在
    git rev-parse --git-path hooks → 主仓 .git/hooks（无 hooksPath 时 worktree 共享主仓钩子层＝回退机理坐实）
    git rev-parse --absolute-git-dir → 主仓 .git/worktrees/baigong-software-team

3. 全链耗时两态（worktree 根现跑 vs 主仓根派工在册值）：

    bash share/run-gates.sh --root . --no-write（worktree 根·947 文件面）＝9.6 秒 real·exit 4
    ＝派工在册 7 秒同量级（本窗含 --no-write 只读模式）；主仓根 529 秒＝派工在册转引（本席主仓路径零触碰不复跑）。
    逐闸分布（worktree 根单跑现算）＝check-collab-lint 0.6s／check-pointers 1.4s／check-pointer-closure 1.5s＝主仓根值 223s／13s／11s 转引派工在册（差异机理＝worktree 稀疏面文件数 1925（git ls-files 现跑）vs 主仓盘 198,153 含 .scratch 取证族 174,070＝派工在册）。
    本窗全链 GATE BLOCK 四枚现跑照登＝check-provenance exit 4（扫描域分类目录 scripts 缺件）＋check-source-of-truth exit 2（外案包目录缺件·sparse 射程外）＋check-collab-buckets exit 4（仓根 .collab 不存在）＋share/check-hook-health.py FX-HOOK-1 BLOCK 期望钩子不在盘＝infra 缺件三处＋钩子健康一处＝全部为 worktree 根现势既存缺件（非本票引入）＝归主根域 GTFAST 领办·α 期 ALLOW_GATE_DOWN=1 留痕口径沿用现状（§五 H-1）。

4. hooksPath per-worktree 属性实证：

    git config --get extensions.worktreeConfig → true
    主仓 .git/worktrees/baigong-software-team/config.worktree 在盘（现读＝core 段 sparseCheckout 两键）
    ＝键写侧将落 config.worktree＝per-worktree＝主仓会话读不到＝「主仓零感知」的机理面成立；git 版本 2.55.0.windows.3（hooksPath 支持面充分）。

5. H-1 靶·check-hook-health 现势单跑两态：

    python3 share/check-hook-health.py --root worktree根 → exit 1；快照行＝HOOKHEALTH-SNAPSHOT hooksPath-readings=0｜hook-file=absent；发现＝BLOCK FX-HOOK-1 期望钩子不在盘
    ＝该闸检查对象＝根参数下 .git/hooks/pre-commit 物理面＋blob 对钉 EXPECTED_HOOK_BLOB 8b785770…＋hooksPath 任意 scope 有读数即报 BLOCK（查一双态全文现读在册 §二.7）；路由表核读＝FX-HOOK-1 不在 per_spec→on_severity BLOCK→block 默认路由现读成立；60-gates 路由表 version 1 单围栏解析成立。

6. H-2 靶·声明闸 staged 语义跨 worktree 现跑：

    git rev-parse --git-path index → 主仓 .git/worktrees/baigong-software-team/index（worktree 独立 index 坐实）
    python3 share/check-staged-declaration.py --root .（空 staged）→ STAGED-DECL 汇总行 exit 0＝读数命令 git -C root diff --cached --name-only -z 于 worktree 根原生读独立 index；
    GIT_INDEX_FILE 指向不存在文件模拟 → exit 4 fail-closed（异常面不吞成 0 坐实；真实 pathspec 提交时 git 预构 next-index 天然继承＝脚本头注 §〇-2 探针定档口径现读在位）。

7. H-3 靶·sparse D 态对钩子内 git 命令扰动面：

    git status --porcelain 裸跑计时＝0.135 秒（1018 行 D 态输出面）；git show --name-only --format= HEAD 计时＝0.115 秒
    ＝本仓实测扰动可忽略，但纪律从严：S1／S2 钩子体内 git 命令闭集＝rev-parse＋show（声明闸内部＝diff --cached 定向面）＝禁 status 全扫类命令写死于 §三 规格注释；两稿 bash -n 语法核各 OK 现跑＋check-pointers --target 两稿各 exit 0（§二.9）。

8. 入线四词预核（写集两枚 verbatim 全文）＋体例自查：

    真源形态 0／文件域 0／席位职权 0／工序链 0（两枚合并逐词 python 包含式现跑）；反引号零／at 零自查在册。

9. 设计稿在位与自靶（居取证族非写集落位）：

    .scratch/t2daarch/spec-pre.sh（17 行）＋.scratch/t2daarch/spec-post.sh（30 行）＝§三 S1／S2 verbatim 同体；
    check-pointers --target spec-pre.sh exit 0＋--target spec-post.sh exit 0＋票面自靶（§四 V4 随完工回报）。

10. post-commit 本体三态真跑（非 git 写·模拟对 3bcb7f2b）：

    无声明态 → exit 0 日志行「无声明态＝非对等核验对象」；声明与 HEAD 面单同径态 → POST-COMMIT-PAIR PASS exit 0；声明 2 枚 vs 面单 1 枚模拟差集态 → stderr 醒目告警＋日志 FAIL 行 exit 0（告警不改已落链提交＝当场报语义）。反斜杠声明归一（tr 正反斜杠）后 PASS 复跑成立＝与声明闸 norm_decl 同制；证据件日志面 .collab/evidence/hooks/ 试跑后已拆（CLEANED 现跑）。

11. V5 基线锚现跑重取：

    check-pointers --root . 单跑＝exit 1·BLOCK 标记位 1863／WATCH 标记位 1009＝T1e 放行黄-3 锚全等命中；run-gates 全链输出面（本窗 .scratch/t2daarch/rungates-wt-nowrite.out）＝BLOCK 标记位 1864（含 FX-HOOK-1:1 一枚）／WATCH 标记位 3383（含 check-ticket-reconcile 154 枚 WATCH 等跨闸面）＝三口径归因沿册（单闸／全链／朴素 grep 禁混比）。

## 三、声明闭集（写集＋禁动面）

写集逐项规格（S1／S2 新建两枚·verbatim 写死＝施工席禁现场改写；落位前置条件与工序见 S3）：

- S1 agent-experts／baigong-software-team／.githooks／pre-commit＝新建 17 行·LF 制式落盘。
  落笔断言：文件不存在前置（§二.4 .githooks 目录 NO_DOTGITHOOKS 现跑）；落盘后 bash -n 语法核 exit 0＋check-pointers --target 本件 exit 0。
  本体 verbatim（缩进段＝施工照落）：

    #!/usr/bin/env bash
    # ITER-W2-T2d-α worktree 本地快闸 pre-commit 钩子本体（包内版本面·动态根）
    # 语义等态主仓现势钩子＝声明闸＋门禁全链两行；唯一改动＝根改动态取＝当轮工作树根。
    # FX_COMMIT_DECLARE 声明闸语义与 ALLOW_GATE_DOWN 口径由 share 两脚本自持＝本件零改写。
    # 只读 git 命令闭集＝rev-parse（禁 status／diff 全扫类命令·sparse D 态零扰动）。
    set -u
    ROOT_DIR="$(git rev-parse --show-toplevel | tr -d '\r')"
    SHARE_DIR="$ROOT_DIR/share"
    [ -f "$SHARE_DIR/check-staged-declaration.py" ] || { echo "infra error: 声明闸脚本缺失：$SHARE_DIR/check-staged-declaration.py" >&2; exit 4; }
    [ -f "$SHARE_DIR/run-gates.sh" ] || { echo "infra error: 门禁链脚本缺失：$SHARE_DIR/run-gates.sh" >&2; exit 4; }
    PY=""
    for cand in python3 python; do
      if command -v "$cand" >/dev/null 2>&1; then PY="$cand"; break; fi
    done
    [ -n "$PY" ] || { echo "infra error: 找不到 python3/python，门禁无法运行（不得降级为放行）" >&2; exit 4; }
    "$PY" "$SHARE_DIR/check-staged-declaration.py" --root "$ROOT_DIR" || exit $?
    exec bash "$SHARE_DIR/run-gates.sh" --root "$ROOT_DIR"

  后置断言：行总数 17；含字样 check-staged-declaration.py 恰 2／run-gates.sh 恰 2／rev-parse --show-toplevel 恰 1；硬编码主仓根字面（multi-agent-collab-devkits 完整字面）零现；反引号零／at 零。
  行尾两态口径随登：落盘 LF；链上 checkout 后 autocrlf=true 可能回 CRLF＝同制可用实证＝share/run-gates.sh 盘 CRLF 现跑可用（§二.3 全链 exit 4 为判据语义非语法错＝bash 装载正常）。
- S2 agent-experts／baigong-software-team／.githooks／post-commit＝新建 30 行·LF 制式落盘＝J-2 甲案钩子本体兑现。
  落笔断言：同 S1（前置不存在＋落盘后 bash -n exit 0＋自靶 exit 0）。
  本体 verbatim（缩进段＝施工照落）：

    #!/usr/bin/env bash
    # ITER-W2-T2d-α post-commit 钩子本体＝J-2 甲案＝HEAD 面单与声明清单对等核验
    # 只读 git 命令闭集＝rev-parse＋show（禁 status 类全扫命令）；零写链零改 index 零碰主仓面。
    # 面单读取取 -z 防转义形态（中文径与含空格径皆原样·与声明侧裸文可比）。
    # 告警日志面＝包内 .collab/evidence/hooks/（.gitignore 在位行 /**/.collab/evidence/ 覆盖＝不入链）。
    set -u
    ROOT_DIR="$(git rev-parse --show-toplevel | tr -d '\r')"
    PKG_DIR="$ROOT_DIR/agent-experts/baigong-software-team"
    LOG_DIR="$PKG_DIR/.collab/evidence/hooks"
    LOG_FILE="$LOG_DIR/post-commit.log"
    HEAD_SHORT="$(git rev-parse --short HEAD | tr -d '\r')"
    TMP_HEAD="$ROOT_DIR/.scratch/post-commit-head-list.tmp"
    TMP_DECL="$ROOT_DIR/.scratch/post-commit-decl-list.tmp"
    git -C "$ROOT_DIR" show --name-only -z --format= HEAD | tr '\0' '\n' | sed '/^[[:space:]]*$/d' | sort > "$TMP_HEAD"
    N_HEAD="$(grep -c . "$TMP_HEAD" || true)"
    printf '%s' "${FX_COMMIT_DECLARE:-}" | tr ',' '\n' | tr '\\' '/' | tr -d '\r' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//;s/^\.\///' | sed '/^[[:space:]]*$/d' | sort > "$TMP_DECL"
    N_DECL="$(grep -c . "$TMP_DECL" || true)"
    mkdir -p "$LOG_DIR" 2>/dev/null
    TS="$(date '+%Y-%m-%dT%H:%M:%S')"
    if [ "$N_DECL" -eq 0 ]; then
      printf '%s %s 无声明态＝非对等核验对象（声明闸已于提交前处置）HEAD面单=%s\n' "$TS" "$HEAD_SHORT" "$N_HEAD" >> "$LOG_FILE"
    elif cmp -s "$TMP_HEAD" "$TMP_DECL"; then
      printf '%s %s POST-COMMIT-PAIR PASS HEAD面单=%s 声明=%s\n' "$TS" "$HEAD_SHORT" "$N_HEAD" "$N_DECL" >> "$LOG_FILE"
    else
      DIFF_LIST="$(comm -3 "$TMP_HEAD" "$TMP_DECL" | tr '\n' ' ')"
      printf '%s %s POST-COMMIT-PAIR FAIL HEAD面单=%s 声明=%s 差集=%s\n' "$TS" "$HEAD_SHORT" "$N_HEAD" "$N_DECL" "$DIFF_LIST" >> "$LOG_FILE"
      printf '\n***** POST-COMMIT-PAIR 卷入告警 %s HEAD面单(%s)≠声明清单(%s) 差集=%s 日志=%s *****\n' "$HEAD_SHORT" "$N_HEAD" "$N_DECL" "$DIFF_LIST" "agent-experts/baigong-software-team/.collab/evidence/hooks/post-commit.log" >&2
    fi
    rm -f "$TMP_HEAD" "$TMP_DECL"
    exit 0

  后置断言：行总数 30；含字样 POST-COMMIT-PAIR 恰 4／git status 字样零现；三态 exit 恒 0（钩子不拦已落链＝当场报语义）；告警面＝stderr 醒目行＋仓内日志一行＝c4aad87 解一口径。
- S3 配置动作（非文件写·归主理人投递窗执行·工序步骤登记）：
  时序硬约束＝**两枚钩子文件先落盘投链，配置键后设**＝反序即 hooksPath 指向缺目录＝git 静默无钩子＝fail-open 窗口（禁）。
    git config core.hooksPath agent-experts/baigong-software-team/.githooks
  ＝extensions.worktreeConfig=true 现读在位（§二.4）→键落 config.worktree＝per-worktree＝主仓零感知；键名大小写口径＝git config 读侧不区分（check-hook-health 用 --get-regexp core\.hookspath 现读在位＝S3 写侧照 core.hooksPath 标准形）。
  拆键回退口径（灰度判据失败面）＝git config --unset core.hooksPath 即整体回退现势（主仓钩子回退接管＝回退零残留）。
- S4 退役条款（辛段纪律自用·票面必载）：汇链窗若主根域 GTFAST 落地版（lint 排除＋静默摘要化＋infra 出清）优于本 α 方案→本 .githooks／ 两枚退役＋FX-HOOK-1 钉值随动重钉＝同一修复禁两侧重复维护；α 存续期间 share／ 侧判据零动＝本票只做载体层。

禁动面五行族（预置固定·逐字照抄）：

- 链上史件零回改；账本零手写；FUXI 零碰；?? 他案群照登零带入；.gitignore 零触。

本票特有禁动面逐项写死：

- 主仓 .git/hooks／全域零触碰（版本外共享面·T2h 归属协议预判据＝主根会话独占改；投前投后 blob 8b785770 全等归 V 系）。
- share／全域零改动（闸脚本只读红线＝lint 排除条款归主根 GTFAST 领办·check-hook-health.py EXPECTED_HOOK_BLOB 现钉 8b785770 照旧不动＝§五 H-1 采甲前提；run-gates.sh／check-staged-declaration.py blob 两态 SAME 归验收臂）。
- 主仓 .git/worktrees／baigong-software-team／config.worktree 零手改（键经 git config 命令写＝禁手改文件）；主仓 .git/config／info／exclude 零触。
- .githooks／两枚之外本包零新文件；.scratch／tickets／除本票面零增删；skills／ 全域·agents／席卡·config／ 两 json·四模板零触。
- sparse D 态 1018 枚勿处理照登（投递侧处置沿册）；钩子脚本体内禁 status 全扫类命令（写死于 S1／S2 规格注释）。

## 四、验收判据（V 系·用例唯一产出处）

V 系骨架（预置固定·命令与期望由槽填）：

- V0 开工读数＝当轮现跑 HEAD＋链序＋锁态＋脏面照登（禁扩集口径沿先例）。
  槽：开工对钉＝HEAD 3bcb7f2b4df8aebaca5387b39a0637a3c4eb1a77 或其后继（放行后以放行笔链顶为准）＋链序逐笔^相衔（现跑 3bcb7f2b←ece3b119←9be69eb7←17f8b1ba←c34f204e←f99ee505 零断）＋锁态两态照登＋脏面照登（sparse D 1018 枚照登勿处理）。
- V1 靶面钉值零漂移＝开工对钉值与下游验收复跑对拍；漂移即停手回报。
  槽：对钉项＝主仓钩子 blob 8b7857701594264421832edd30dae7e401f85719（开工现算全等）＋check-hook-health.py EXPECTED_HOOK_BLOB 字面现读 8b785770（share 零改动面）＋core.hooksPath 开工 exit 1 空读数＋.githooks／ 开工 absent（NO_DOTGITHOOKS）＋主仓根 run-gates 529 秒／逐闸 223s-13s-11s＝派工在册转引标注不冒充本席现跑＋check-pointers 单跑锚 1863／1009 现跑全等。
- V2 施工动作＝施工步骤命令 verbatim＋断言＋程序化动作读数。
  槽：步骤一 BUILD 落两枚（路径＝§三 S1／S2）→各 bash -n exit 0＋自靶 exit 0＋后置断言逐枚（行总数 17／30＋字样计数＋主仓根字面零现）；步骤二 投链后主理人窗 S3 设键→git config --get core.hooksPath 回读＝agent-experts/baigong-software-team/.githooks＋config.worktree 面单现读该键在位＋主仓 git config --get core.hooksPath（-C 主仓根）＝空 exit 1＝主仓零感知键面坐实。
- V3 落盘坐实＝面单核验（git show --numstat／--name-only 于施工笔）。
  槽：BUILD 笔面单恰两枚＝S1 A 17／0＋S2 A 30／0；零越界（对照 §三 闭集两枚）。
- V4 自靶 exit 0＝落笔前各靶件 check-pointers --target 现跑。
  槽：--target S1 件 exit 0＋--target S2 件 exit 0＋--target 本票面 exit 0（三跑期望全 exit 0；起草窗两稿同体已 exit 0 现跑在册 §二.9）。
- V5 面单互证＝声明闭集 vs 实测 numstat 对等（零越档）＋缺省扫描对施工前基线只平或降、非零逐枚归因禁遮掩。
  槽：改前基线＝§二.11 两口径照登（单闸 1863／1009＋全链 1864／3383）；改后复跑对锚只平或降；新增 FX-HOOK-1 hooksPath 读数面 BLOCK（查一）预期＝＋1 枚＝逐枚归因＝钩子健康闸对 per-worktree 键的现存语义（§五 H-1 采甲在册缺件族）＝禁遮掩禁无锚比平。
- V6 升档停手闸＝入线四词（词表以票级放行登记勘正表为准）grep 于施工笔 diff 面→命中 0；命中任一＝停手呈主理人升全量档，禁自行继续。
  槽：四词逐词对 diff 面复跑读数（期望 0／0／0／0；起草窗预核含两枚 verbatim 已全零见 §二.8）。

α 效能判据（本票特有·归 QA 验收臂现跑）：
- A-1 单笔 commit 全闸实测 ≤60 秒＝负样例＝α 落地后一笔真实投递掐表读数入回执（开工→commit 返回全程；预期量级＝§二.3 全链 9.6 秒＋声明闸亚秒）。
- A-2 主仓零感知坐实＝主仓钩子 blob 投前投后现算全等 8b785770＋主仓链面零新笔归我方＋主仓 config 键面空（V2 步骤二回读）。
- A-3 声明闸照常拦截（dry 面禁真投）＝worktree 根 unset FX_COMMIT_DECLARE 与 ALLOW_GATE_DOWN 后 python3 share/check-staged-declaration.py --root worktree根 于 staged 非空模拟面应 exit 1（现势空 staged 面 exit 0 对照在册 §二.6；测试笔禁真投＝用 dry 直接调脚本面）。
- A-4 post-commit 在岗两态自洽＝三态真跑（无声明／PASS／FAIL 告警）各 exit 0＋日志行形态对 §二.10 对拍；条件式兜底文案兼容两态＝thin 71 行 08fb0f5b「（钩子在岗时）」口径（钩子在岗后语义现势化）。

对抗臂（验收席自定为本票下限）：臂①两枚落盘与票面 verbatim 逐字对拍（改动外零扰动＝新建件全文件对票面缩进段剥缩进全串等值）；臂②禁动面 blob 两态 SAME 逐枚（主仓钩子＋share 全域＋席卡＋config 两 json）；臂③钩子体语义核验＝S1 无主仓根硬编码字面＋S2 无 status 全扫命令＋S2 exit 恒 0 不拦已落链；臂④回退演练＝--unset 后主仓钩子回退接管一笔（可选臂·灰度回退面可测性）；臂⑤钩子装载实证＝一次真投递窗钩子确实触发（证据＝post-commit 日志行新增＋声明闸 STAGED-DECL 输出入 commit 输出重定向件）。

## 五、候裁单列（必有节·可 0 枚）

预置固定行：批次编排类不上楼＝不自列候裁。

- H-1 FX-HOOK-1 钩子健康闸适配（真岔·呈方案＋推荐）：议题＝hooksPath 切换后 check-hook-health 在 worktree 根 run-gates 内的语义——现钉 EXPECTED_HOOK_BLOB 8b785770 钉的是主仓钩子；share 零改动红线下两案。甲案＝share 零改动·现钉照旧：实证链＝①主仓面（他案在用·主仓钩子调 run-gates --root 主仓根）查一查二查三全过＝现钉照旧通过零影响（per-worktree 键主仓不可见 §二.4）；②worktree 面本票落地后查一新增 hooksPath 读数 BLOCK＋查二 hook-file=absent BLOCK（worktree .git 为文件无 hooks 子目录）＝两枚 BLOCK 与现存 infra 三枚同族＝均为「主根域待清缺件」＝α 期 ALLOW_GATE_DOWN=1 留痕口径沿用现状（W2-C1 hook 漂移在册·非静默·声明闸在钩子直调层照常先行）；代价＝worktree 面 FX-HOOK-1 哨兵语义失真持续（其「钩子在岗」断言对 worktree 失效）＝GTFAST／W2-C1 收口时统一重定形（含「worktree 钩子在位」断言增否归该票设计权）。乙案＝本票动 share 增 worktree 感知＝违 share 零改动红线＋写集越界＝评估不可行侧呈清。建议采纳＝甲（V5 已按＋1 归因入册＝失真面显账不隐）。
- H-2 声明闸 staged 语义跨 worktree 核验（实证结论·非候裁）：现跑坐实＝worktree 独立 index（--git-path index 现读）＋脚本 git -C root diff --cached 原生读当轮 index＋钩子环境 GIT_INDEX_FILE 天然继承＋异常面 exit 4 fail-closed＝**原生正确零适配需求**；登记为取证结案不入候裁。
- H-3 sparse D 态扰动面（实证结论·非候裁）：本仓裸 status 仅 0.135 秒＝扰动可忽略；处置＝纪律从严写死钩子体 git 命令闭集（S1／S2 规格注释＋对抗臂③）＝设计约束已入 §三 非真岔；登记结案。
- J-1 post-commit 告警日志落位：议题＝仓内日志一行落哪。甲案＝包内 .collab/evidence/hooks/post-commit.log（.gitignore 在位行 /**/.collab/evidence/ 覆盖＝不入链＝零 .gitignore 改动·S2 verbatim 已按此写死；代价＝日志面不入链＝证据效力＝盘面临时面沿 run-gates 证据件同制）。乙案＝落 .scratch/hooks/（同样 ignore·语义不如 evidence 贴）。建议采纳＝甲（已在 S2 verbatim 内＝随裁确认）。
- J-2 α 与主根 GTFAST 的闸链双活窗口：议题＝S3 设键后主仓钩子对 worktree 不再触发，主根会话钩子仍主仓根全扫——汇链窗（本包链 merge 回主仓）主仓面闸成本依旧 8～10 分钟，α 不改善主仓面。甲案＝接受（本票射程＝worktree 投递窗；主仓面提速＝GTFAST 本体＝S4 退役条款已预置防双维护）。乙案＝本票扩面改主仓钩子＝违 S4 禁动面＋T2h 归属预判据＝不可行侧呈清。建议采纳＝甲。

## 六、链衔接纪律（预置固定·不重写）

- 开工现跑 HEAD＋链序照登；单 pathspec add 紧邻 commit＋FX_COMMIT_DECLARE 挂 commit 命令侧＝仓根相对路径（两端皆为声明侧卫生纪律·缩小卷入命中面·非拦截机制——c4aad87 三实验坐实提交侧拦不住他席 staged 注入）；卷入防线＝（钩子在岗时）post-commit 比对真实树当场报（HEAD 面单与声明清单对等核验·不符即醒目告警＋仓内日志一行）；commit 前先跑自靶 exit 0。
- message 用 -F 文件承载（防引号与中断·先例在册）＝message 文件落仓根 .scratch／ 取证族·用毕即拆 ls 坐实。
- 落链硬口径＝-F 承载＋commit 输出重定向落盘＋后台执行（中断教训先例在册）；commit 类命令 timeout 600000。
- 体例＝裸文＋全角斜杠·零 at 零反引号·命令缩进段；尾标闭集（-TICKET／-BUILD／-RECEIPT／-QA-REV／-QAV／-GCLOSE 照段别取用）；族名随 message 内嵌。
- 禁 add -A／禁 amend／禁 --no-verify；message 以 collab: 起头·零 at 零反引号·＝号串联关键读数。
- 撞锁两态口径＝lock 在飞等待自然消退、实证陈旧按先例删锁留证；他案脏面照登零带入。
- 临时工作物落仓根 .scratch／；取证族用毕即拆 ls 坐实随完工回报。

（模板尾·固定形制：append-only 票面后续修订在票尾续 rev 段，rev 段间互不回改）
