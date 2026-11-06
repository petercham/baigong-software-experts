# TK-GWP · 施工票：百工专家包装配态守卫装配缺陷批（缺陷票类·L2·架构席起草·0.1.29 实跑暴露批）

- 票 ID＝`TK-GWP`（代号 GWP·commit 引用形态 `TK-GWP` 命中 commit-audit `TK-` 现闭集）。
- 起草实测 HEAD＝`b47a5e6`（开工 `git rev-parse --short HEAD` 读数与主理人侧一致）；开工 ANCHOR＝开工实测 HEAD ≥ `b47a5e6`，读数附回执开端。
- 决策依据＝实跑发现（0.1.29 装配进另一项目实跑·三场景全拦）＋主理人已按真源逐条核证缺陷清单；本票只起草票面，起草席零落改（本票面即本批起草段唯一产出）。
- 被检真源闭集＝`agent-experts/baigong-software-team/skills/sop/scripts/{write-guard.py,lease-issuer.py,commit-audit.py,memory-neutralize.py}` ＋ `config/seat-permissions-hooks-map.json` ＋ `hooks/hooks.json`（后两件＝禁动面，只作取证直读）。
- 行号纪律＝票内行号全部起草实测（§十三开工复测逐位重打）；漂移以开工实测为准，锚文逐字命中后方可施工。
- 计数口径＝occurrence；判据命令落盘一律重定向至仓根 `.scratch/gwp/`（批毕即删·仓内零运行残留）；负例 exit≠0 或输出形态反转即红。
- 本票只定义施工与验收；**严禁起草段执行落改、禁改任何 scripts 真源**（本票落位＋单独 commit 即起草段全部产出）。

## 一、问题实证（起草取证·逐文件复核行号属实·回执附开工复测）

### 1.1 P1-1 探针锚冲突（最高优先·装配态零 allow 通道）

- `write-guard.py` L40–45 `pack_root()`＝脚本自身位置上溯四级＝包根；L48–63 `project_root()`＝`SWB_REPO_ROOT` 覆写缺位时**自包根位置上溯**首个含 `docs/STRUCTURE.md` 目录＝项目根（B1-C 探针锚）。
- 包自带 `agent-experts/baigong-software-team/docs/STRUCTURE.md`（起草实测存在·其 yaml 块自declare `project_root: "."` ＋ delivery_paths 六目录）——**探针自包根出发必第一眼命中包根本身**。
- 装配态后果链（实跑取证）：探针命中包根→项目根误判为包根→`normalize_path()`（write-guard.py L140–149）对 payload 项目绝对路径剥不掉项目前缀（保留盘符形态 L146–148）→租约 `path_globs`（项目根字面）永不匹配→正牌席位正常路径亦 deny＝装配零 allow 通道（实跑三场景全拦）。
- `lease-issuer.py` L32–42 `project_root()`＝同款 helper（且不读 `SWB_REPO_ROOT` 覆写），同病灶。
- 起草补强读数（cwd 语义厘清）：`hooks/hooks.json` L17/L27/L37 command＝相对路径 `"../skills/sop/scripts/…"`——旧作者形制隐含 hook 执行 cwd＝包根，该形制下「只改自 cwd 上溯」仍命中包根（cwd＝包根时），故修复规格必须含**「探针命中＝包根本身即跳过续溯」**条款方在两形制下均成立（见§3.1 行为表）。

### 1.2 P1-2 双账本错位

- `lease-issuer.py` L45–47 `default_ledger_root()`＝`SWB_LEDGER_ROOT` 缺位时 `project_root()/.collab/ledger`（探针锚＝1.1 病灶→装配态读落包根）。
- `write-guard.py` L72–73 同名函数缺位时 `os.getcwd()/.collab/ledger`——两脚本缺省锚不同源：租约会写进包根账本、守卫读 cwd 账本，两本账非同一文件（起草旁证：包根 `.collab/` 下现盘无 ledger 面，仓根 `.collab/ledger/ledger.jsonl`＝1 行＝两锚现势各走各的）。
- 起草补强读数（错位面比任务清单更宽）：`default_ledger_root()` 全族 13 个 sop scripts＋`tests/acceptance/metrics-gate.py` 中，**仅 lease-issuer.py 用 `project_root()` 锚，其余 12 件一律 `os.getcwd()` 锚**（def 体逐件核对：baseline-backfill-demo／commit-audit／freeze-unfreeze／intake-register／liveness-selfcheck／memory-neutralize／reconcile-daily／serial-gate／shadow-replay／sign-verify／state-transition／write-guard）。本票施工面收口＝**hooks 运行链四脚本**（write-guard／lease-issuer／commit-audit／memory-neutralize）同批统一；其余 9＋1 件＝人类/主理人手调工具面（运行时 cwd 惯例＝项目根故现锚现势等效）→ P7 续票规划条（§五）。

### 1.3 P5-1 续体席位不归因

- `write-guard.py` L157–165 `seat_of()`＝agent_type 精确命中→agent_id 前缀近似两路；`config/seat-permissions-hooks-map.json` L32–38 `agent_type_to_seat` 五键闭集（`software-team-{lead,product,architect,engineer,qa}`·SCFIX 清退态）。
- 平台续体席 agent_type＝`software-team-architect-2` 类后缀型不在闭集→seat=None→L211–213 fail-closed deny。

### 1.4 P6-1 票 ID 闭集不含项目票号

- `commit-audit.py` L31–35 `TICKET_ID_PATTERNS` 四型＝`SWB-*`／`TKTn`／`TK-[A-Za-z0-9-]+`／`.collab/tickets/路径`；项目侧票号（`XXX-NNNN-WORD` 型，如实跑 `DISP-1106-REWORK` 类）不命中→L127–128 orphan 判定误拦正常提交。

### 1.5 P3-1 守卫异常＝放行（fail-open）

- hooks 阻断词表＝exit 2→blocking（`hooks.json` L18/L38 `_note`；`write-guard.py` L37 `EXIT_USAGE = 2  # 与 hooks exit 2→blocking 词表一致的阻断退出码`）。
- hooks 运行链脚本主路均无兜底异常捕获：未捕获异常（坏 `--map` JSON、账本目录不可写、payload 结构畸变等）→ Python 默认 traceback exit 1≠2→宿主放行＝守卫失效时纪律不具强制力。
- **口径级变更声明：本项改「守卫失效语义」（fail-open→fail-closed），口径写死见§3.5，单列候裁①终确认。**

### 1.6 P4-2 deny 原因 GBK 乱码

- deny/呈报输出含中文（`deny_output()` write-guard.py L186–194 `ensure_ascii=False`），Windows 中文宿主管道按 GBK 解码乱码＝审计可读性破损（阻断判定本身不受影响，reason 不可读）。
- P4-1（payload 路径 CJK→`?`）＝宿主管道编码层非包内可修＝登记不施工（§六）。

### 1.7 P7 租约模型缺口（登记·不并入本批施工面）

- `write-guard.py` L168–183 `load_leases()` 只消费 `path_globs`/`cleared` 两字段；条目 `hash` 装载但不校验；无租约时效、无按票撤销（仅 freeze 全表清租约）、`countersign` 字段写侧不核——手工伪造 jsonl 行即具现行态效力。范围大＝登记缺口＋续票规划条（§五），本票零施工。

## 二、目标（一句话）

装配态（包安装进任一含 `docs/STRUCTURE.md` 的宿主项目）下守卫链走通：正牌席位按租约有 allow、越界仍 deny、账本缺省锚四脚本同源、续体席位归因、项目票号不冤拦、守卫异常即阻断、输出编码可读——四脚本闭集内完成，配置/hooks/版本面零触。

## 三、实装规格（写死·可机械验证·行位以开工实测为准，以下为起草实测锚位）

### 3.1 落点一/六：`write-guard.py` L48–63 ＋ `lease-issuer.py` L32–42 —— `project_root()` 重写（两脚本逐字同款）

现文锚（write-guard.py L48 起 def＋docstring＋函数体整段替换；lease-issuer.py L32 起同款整段替换）替换为：

```python
def project_root() -> str:
    """GWP-P1-1 探针序换代：① SWB_REPO_ROOT＝项目根覆写面（测试重定向·覆写语义零动）；
    ② 自 cwd 上溯首个含 `docs/STRUCTURE.md` 且≠包根之目录＝项目根（装配态宿主项目根优先——
    包自带 docs/STRUCTURE.md＝包 bundle 自声明 project_root:"."，不得劫持宿主项目根，
    命中＝包根本身即跳过续溯）；③ 缺位回退自包根上溯（同样跳过包根自身）；
    ④ 全缺位＝落回包根（fail-safe·权限面读空即租约不命中＝deny，不开 fail-open 窗口——旧语义保持）。
    权限字面一律读作项目根相对（表2-1 路径锚定款随迁）。"""
    env = os.environ.get("SWB_REPO_ROOT")
    if env:
        return env
    pack = pack_root()
    d = os.getcwd()
    while True:
        if os.path.normcase(d) != os.path.normcase(pack) and os.path.isfile(
                os.path.join(d, "docs", "STRUCTURE.md")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    d = os.path.dirname(pack)
    while True:
        if os.path.isfile(os.path.join(d, "docs", "STRUCTURE.md")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    return pack
```

- lease-issuer.py 同款＝**逐字相同**（含 `SWB_REPO_ROOT` 覆写读取＝两脚本同源 helper 一致性补强新增；该变量缺席场景行为零变化）。
- 行为表（四场景·开工复测与验收判据据此）：

| 场景 | 旧行为 | 新行为 |
|---|---|---|
| 装配态·cwd 在宿主项目子树（宿主有 docs/STRUCTURE.md） | 命中包根→零 allow | 命中宿主项目根 ✓ 解锁 |
| 装配态·cwd＝包根（hooks.json 相对路径形制隐含） | 命中包根 | 包根命中被跳过→宿主链无 STRUCTURE 则落回包根＝与旧同不变坏；宿主经 SWB_REPO_ROOT 覆写即通（候裁⑧前置） |
| 本仓开发态（仓根无 docs/STRUCTURE.md·起草实测 Glob＝无命中） | 命中包根（包自带） | 跳过包根→仓根无 STRUCTURE→落回包根＝**与旧同·零回归** |
| `SWB_REPO_ROOT` 在场 | 直接采用 | 直接采用（零动） |

### 3.2 落点二/八/十一：`write-guard.py` L72–73 ＋ `commit-audit.py` L55–56 ＋ `memory-neutralize.py` L44–45 —— `default_ledger_root()` 缺省锚统一

三脚本 `def default_ledger_root()` 体内 `os.getcwd()` 一律替换为 `project_root()`（§3.1 修后语义），即四脚本（lease-issuer.py L45–47 现文本身不动）缺省锚统一＝`SWB_LEDGER_ROOT` 覆写 ∨ `<project_root()>/.collab/ledger`，覆写语义四脚本一致。commit-audit.py／memory-neutralize.py 需在各自 `pack_root()` 之后补入 §3.1 同款 `project_root()` helper（逐字同款＝脚本自包含分发形制保持，无跨件 import）。

### 3.3 落点三：`write-guard.py` L157–165 —— `seat_of()` 续尾剥离

现函数整块替换为：

```python
def seat_of(agent_type: str | None, agent_id: str | None, mapping: dict) -> str | None:
    """席位归因：agent_type 精确→续尾剥离（`-数字` 尾缀）→agent_id 前缀近似。
    GWP-P5-1：平台续体席 agent_type＝`software-team-<席>-<数字>` 型不在映射闭集——
    剥离尾缀 `-\\d+` 后重查；config 五键闭集零动、agent_id 近似路零动。"""
    if agent_type and agent_type in mapping:
        return mapping[agent_type]
    if agent_type:
        base = re.sub(r"-\d+$", "", agent_type)
        if base != agent_type and base in mapping:
            return mapping[base]
    if agent_id:
        for k, v in mapping.items():
            if k and (str(agent_id).startswith(k) or k in str(agent_id)):
                return v
    return None
```

### 3.4 落点七：`commit-audit.py` L31–35 —— `TICKET_ID_PATTERNS` 闭集扩第五型

列表尾部追加一行（四现有模式一字不动）：

```python
    re.compile(r"\b[A-Z][A-Z0-9]{1,9}-\d{3,4}-[A-Z][A-Z0-9]{1,14}\b"),  # GWP-P6-1 项目票号 XXX-NNNN-WORD 型（大写三段·中段三至四位数字）
```

防松约束（写死）：全大写＋三段式＋中段数字 3–4 位＝窄形制；小写／两段／纯数字尾／普通英文大写单词（无连字符三段结构）不命中；无任何票 ID 形态的提交仍 orphan 拦（负样本§八-6）。

### 3.5 落点四/九：`write-guard.py` L317–318 ＋ `commit-audit.py` L192–193 —— 入口 UTF-8 重配＋主路 fail-closed 兜底

两脚本 `if __name__ == "__main__":` 块整块替换（P3-1＋P4-2 同落点）：

write-guard.py：
```python
if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8", errors="backslashreplace")
        except Exception:
            pass
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except BaseException as _e:
        # GWP-P3-1 fail-closed：守卫异常即阻断（exit 2→blocking·§19 词表）；deny 决策照出＋留痕尽人事
        try:
            print(deny_output(f"write-guard 异常 fail-closed：{type(_e).__name__}: {_e}"))
        except Exception:
            pass
        try:
            append_record(os.path.join(default_ledger_root(), "ledger.jsonl"), "呈报",
                          "write-guard.py",
                          {"event": "guard_fail_closed", "error": f"{type(_e).__name__}: {_e}",
                           "clause": "GWP-P3-1 守卫失效语义＝fail-closed（exit 2→blocking）"})
        except Exception:
            pass
        sys.exit(EXIT_USAGE)
```

commit-audit.py（同构；阻断形态＝stderr BLOCK＋exit `EXIT_BLOCKING`，prehook/posthook 两相同一兜底口径）：
```python
if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8", errors="backslashreplace")
        except Exception:
            pass
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except BaseException as _e:
        # GWP-P3-1 fail-closed：审计异常即阻断（exit 2→blocking·§19 词表）
        try:
            print(f"BLOCK commit-audit: 异常 fail-closed {type(_e).__name__}: {_e}", file=sys.stderr)
        except Exception:
            pass
        sys.exit(EXIT_BLOCKING)
```

- 口径写死：异常→**阻断**（exit 2＋deny/BLOCK 输出＋留痕尽力），不再存在「异常＝不干预」窗口；`SystemExit`（既有 exit 2 拒签发等路径）原样透传零扰动。memory-neutralize.py 不并入（读侧标 ask 非阻断闸·诚实边界§7 对应行·候裁⑥）。

### 3.6 落点五/十：`write-guard.py` L186–194 ＋ `commit-audit.py` 输出行 —— deny/呈报 reason ASCII 安全化（P4-2 双保险）

在§3.5 入口重配之外，`deny_output()` 改为 `ensure_ascii=True` 输出（中文 reason 转 `\uXXXX` 转义＝管道任意代码页可无损还原，宿主解码端与终端显示端解耦）；`permissionDecisionReason` 值面人类可读性经宿主 JSON 解码恢复，GBK 直读乱码面消除。commit-audit.py stderr BLOCK 行保持现文（非 JSON 决策面·不进宿主解析链·候裁⑦）。

### 3.7 产出文件数汇总

修改＝**4 件**：`write-guard.py`／`lease-issuer.py`／`commit-audit.py`／`memory-neutralize.py`（均在 skills/sop/scripts/ 下）。超出即停手上报。

## 四、边界

做什么：§3.1–3.6 四脚本闭集施工＋§七验收。
不做什么／禁改清单：**`config/seat-permissions-hooks-map.json`（五键闭集·deny_globs 全列）、`hooks/hooks.json`（决策词表路由面）、版本三同源（`plugin.json`／`.codebuddy-plugin/plugin.json`／`bundle.lock`——不改版本号：REMOTE-PUB 规划票 v1.2 F 段已预留 0.1.30，本批升版归属＝主理人对表后另定，本票票面先行写明）、`config/seat-permissions.json` 源件、`docs/STRUCTURE.md`（含包级自声明文件）、`tests/` 全树、P2-1 涉及的全席 deny_globs 面** 零触。其余 sop scripts（9 件）＋`tests/acceptance/metrics-gate.py` 缺省锚本批不动（§1.2 收口范围条款）。

## 五、P7 续票规划条（登记·非本批施工面）

- GWP-S2 规划条①：租约时效字段（签发含 `expires_at`，`load_leases()` 过期即滤）＋按票撤销行（`{revoked, ticket_id}` 记账行）。
- GWP-S2 规划条②：`load_leases()` 装载时重算 `lease` 三字段 canonical hash 与条目 `hash` 比对，失配＝条目作废＋呈报码（伪造行免疫）。
- GWP-S2 规划条③：`default_ledger_root()` 其余 9 scripts＋metrics-gate.py 缺省锚随 §3.2 统一（工具面批）。
- GWP-S2 规划条④：`countersign` 写侧核验面（与 B2 签发面闭环）。
规划条归属＝后续独立票，本票判据射程零含。

## 六、候裁／登记面（代码面之外·票面不自行裁决）

1. **P2-1 守卫件全席 deny_globs 死锁**：`config/**`＋`hooks/**`＋`scripts/**`（skills 域）对全部机械席位 deny＝修守卫自身无票型通道（本次实跑修复即人类手工通道）。**候裁**：增设「基础设施修复票」型＝人类显式授权+租约例外通道（人类直通＝设计语义延伸），或确认现行人工通道即终态。本票起草与后续施工均按主理人指令走人类授权通道，程序追认候此裁。
2. **P3-2 平台 hook payload 身份字段缺失**（实跑 69/199 次 agent_type/agent_id＝None）＝宿主侧问题登记，非包内可修。
3. **P4-1 payload 路径 CJK→`?`**＝宿主管道编码层登记（同 P3-2 族）。
4. **P5-2 STRUCTURE.md 自定义桶 vs 包级写域对齐程序**＝另案候批。
5. **P5-3 命名清偿机检**＝另案候批。
6. memory-neutralize.py fail-closed 化与否（读侧标 ask 语义下异常＝不标记＝漏检非放行越权，口径不同写侧）＝候裁。
7. commit-audit stderr 中文行是否 ASCII 化＝候裁（§3.6 现规格＝仅 JSON 决策面转义）。
8. hooks.json 命令改绝对化/`$CLAUDE_PROJECT_DIR` 类载体（消除 cwd＝包根隐含形制）＝候裁（触及禁动面 hooks.json，本票否动）。
9. commit-audit posthook 异常是否同样阻断（记账失败阻断工具调用＝副作用面）＝候裁（§3.5 现规格＝两相同口径阻断，若裁 posthook 降 exit 0＋呈报即回落）。
10. P3-1 口径级变更（fail-open→fail-closed）终确认＝呈主理人/人类确认（§1.5 声明在册）。

## 七、验收判据（每条可跑·重放一律落仓根 `.scratch/gwp/`·钉值来自起草实测）

预备夹具（非改动·验收工序）：`.scratch/gwp/fakeproj/` 构造假宿主项目根＝含 `docs/STRUCTURE.md`（内容含 delivery_paths 六目录 yaml 块）＋其下 `src/` 子目录；租约注入件 `.scratch/gwp/leases.jsonl`（lease-issuer 以 `SWB_REPO_ROOT=.scratch/gwp/fakeproj` 对 architect 席签 `.collab/drafts/design/` 子集租约生成）；payload 注入件 `.scratch/gwp/payload-*.json`（agent_type 字段各判据自定）。以下 `WG`／`CA`／`LI` 分别指四脚本路径全写（`agent-experts/baigong-software-team/skills/sop/scripts/…`），`FR＝SWB_REPO_ROOT=<fakeproj 绝对路径>` 前缀。

| # | 判据 | 命令口径 | 钉值 |
|---|---|---|---|
| 1a | 语法闸×4 | `python -m py_compile` 四脚本逐一 | 四件 exit 0 |
| 2a | P1-1 装配态 allow | 假项目根＋租约在册＋payload（agent_type＝software-team-architect，写目标＝fakeproj 内 `.collab/drafts/design/x.md` 绝对路径，cwd＝fakeproj） | stdout deny JSON 缺席＋stderr 含 `ALLOW`＋exit 0 |
| 2b | P1-1 装配态 deny（负样本） | 同 2a 但写目标＝fakeproj 内 `docs/ARCHITECTURE.md`（租约外） | stdout deny JSON 在场＋exit 0（deny 决策面）＋ledger deny 留痕 |
| 2c | P1-1 本仓开发态零回归 | 无 SWB_REPO_ROOT·cwd＝本仓根·跑 write-guard --sentinel | 哨兵 deny 照旧（与修前同形态） |
| 3a | P1-2 缺省锚对拍 | 四脚本各跑一行 `python -c "import importlib.util,…;print(default_ledger_root())"`（注入面：四脚本各 exec 取 default_ledger_root）·cwd 统一＝fakeproj·无 SWB_LEDGER_ROOT | 四读数**逐字一致**（＝fakeproj/.collab/ledger） |
| 3b | P1-2 覆写一致 | 同 3a 加 `SWB_LEDGER_ROOT` 指 `.scratch/gwp/led` | 四读数＝覆写值 |
| 4a | P5-1 续体归因 | payload agent_type＝`software-team-architect-2` 写租约内路径 | allow（＝归因 architect） |
| 4b | P5-1 非法型仍 None（负样本） | payload agent_type＝`software-team-architect-x` 写同路径 | deny「席位不可归因」 |
| 5a | P6-1 项目票号不冤拦 | `CA prehook --command "git commit -m 'fix: TK-GWP 修复'"` 与 `--command "git commit -m 'feat: DISP-1106-REWORK 随正'"` | 两跑 exit 0 无 orphan |
| 5b | P6-1 无票仍拦（负样本） | `CA prehook --command "git commit -m 'fix something'"` | exit 2＋BLOCK orphan |
| 5c | P6-1 现有四型零回归 | 现四型各一提交串（SWB-B1/TKT12/TK-X1/含 .collab/tickets/ 路径） | 四跑全 exit 0 |
| 6a | P3-1 注入异常 fail-closed（write-guard） | `WG --map <坏JSON件> --path <任意>` stdin 喂合法 payload | **exit 2**＋stdout deny JSON（fail-closed 字样） |
| 6b | P3-1 注入异常（commit-audit） | `CA prehook --input <坏JSON件>`（--input 指向非法 JSON 文件→json.load 抛异常） | **exit 2**＋stderr BLOCK fail-closed |
| 7a | P4-2 deny JSON ASCII | 任一 deny 场景 stdout | JSON 可 `json.loads` 且全 ASCII（`\uXXXX` 转义还原＝原中文） |
| 7b | P4-2 中文路径场景不炸链 | cwd＝含中文目录名夹具·deny 跑通 | exit 0＋deny JSON 完好 |
| 8 | 禁动面哈希不变 | `git diff --name-only HEAD` 修批后 | 恰＝四脚本（config/hooks/plugin/bundle.lock/tests 零入列） |
| 9 | 租约签发链走通 | `FR LI --ticket TK-GWP-TEST --seat architect --countersign architect:qa --path-glob .collab/drafts/design/ --leases <夹具>` | exit 0＋四字段 JSON＋账本落夹具文件 |

**残留纪律**：判据跑毕 `rm -rf .scratch/gwp/`，`git status --porcelain` 对 `.scratch/gwp` 零命中＝「仓内零运行残留」读数。

## 八、负样本判读（每条配一句）

1. 判据 2a 不过（仍 deny）→ 探针换代未命中宿主根（cwd 链或跳过包根条款写错）＝P1-1 未修通。
2. 判据 2b 不过（越界被 allow）→ 探针换代顺带放开了租约面（path_globs 匹配逻辑被误动）＝越权放行，重大红。
3. 判据 2c 不过（本仓形态变化）→ 开发态回归破坏（跳过包根后回退路径写错）。
4. 判据 3a/3b 不过 → 缺省锚仍不同源或覆写只通一脚本＝P1-2 未闭合。
5. 判据 4b 不过（非法后缀被归因）→ 续尾剥离过宽（`-\d+` 写成了任意尾缀剥离）＝归因面放宽过度。
6. 判据 5b 不过（无票提交放过）→ 第五型正则松化到吞并普通文案＝orphan 判据失效，重大红。
7. 判据 5c 不过 → 现有闭集被改写＝判据一字未动纪律破坏。
8. 判据 6a/6b 不过（exit 1 或无 deny 输出）→ fail-closed 兜底未生效＝口径级变更未落地。
9. 判据 7a 不过（JSON 含裸中文或不可 loads）→ 转义面写错＝P4-2 未修。
10. 判据 8 不过 → 越界改动＝触及禁动面，停手上报。
11. 判据 9 不过 → 租约签发链自身被 P1 换代改坏＝B2 面回归红。

## 九、停止条件（遇此停手上报，不自行处理）

歧义：开工复测任一行号/锚文与§一/§三不符（他席已先行改动真源）→ 停手上报；越界：需触禁改清单任何一件；依赖缺失：hooks 宿主对 `ensure_ascii=True` 决策 JSON 消费形态存疑（判据 7a 实跑与宿主行为不符）→ 停手上报呈候裁；同席多实例并发＝立即停手报告（席位守则）。

## 十、回滚

git 层面：本批＝四脚本单 commit（或按主理人拆笔），`git revert <本批笔>` 全撤。数据层面：`.scratch/gwp/` 夹具＝批毕即删＝无数据回滚面；账本无 schema 变更（新事件类型 `guard_fail_closed` 追加型记录，旧 reader 兼容）＝无不可回滚步骤。租约模型零 schema 变更（P7 未施工）＝回滚无对账断层。

## 十一、预算

改文件＝4｜改行（增删合计）≤170（write-guard ≈60：project_root 换代＋seat_of＋deny_output 转义＋__main__ 兜底／lease-issuer ≈30：同款 helper 换代／commit-audit ≈60：helper 新增＋票型一行＋锚统一＋__main__ 兜底／memory-neutralize ≈45：helper 新增＋锚统一）｜步骤≤10（复测→四件施工→py_compile→夹具→判据 2/3/4→判据 5/6→判据 7/9→哈希对面→删夹具→回执）。

## 十二、候裁清单汇总

§六 1–10 条为候裁/登记全集（其中候裁⑩＝P3-1 口径级变更终确认＝本批放行前置）。票面自行裁决项（起草席职权内）：P1-1 采「cwd 上溯优先＋包根自跳过＋包根回退」三段式（非仅任务草案两段＝补 hooks 相对路径形制免疫）；P5-1 采尾缀 `-数字` 剥离（映射文件零动）；P6-1 采闭集扩第五窄型（非全局放宽）；P4-2 采「入口 UTF-8 重配＋决策 JSON ensure_ascii 转义」双保险；P3-1 采 __main__ 外层 BaseException 兜底（不动 main 内部结构）。

## 十三、开工复测清单（回执开端必附）

1. `git rev-parse --short HEAD`（≥`b47a5e6`）。
2. write-guard.py L48/L72/L157/L186/L317、lease-issuer.py L32/L45、commit-audit.py L31/L55/L192、memory-neutralize.py L44 现文逐字命中§三锚文（任一漂移＝停止条件）。
3. 包自带 `docs/STRUCTURE.md` 存在＋本仓根 `docs/STRUCTURE.md` 缺席（Glob 空）两读数复测（§3.1 行为表前提）。
4. §1.2 全族 13 件 def 体 grep 读数复测（收口范围四件核实）。
5. 版本三同源现值 `0.1.29` 读数在案（禁动面基线）。
