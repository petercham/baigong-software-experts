# DEBTCLN-R5 · TOKPAR 红线参数化票（v1·规格票·起草笔零施工）

- 票号：**DEBTCLN-R5**（清债批次第五票·族名锁定，勿改）
- 票名：**TOKPAR 红线参数化票**
- 票型：清债·工具参数化微票（脚本单件插入式改码·默认线值 2500 字面零变＝行为零回归）
- 起草席：架构席 arch-debt5（fresh 实例·主理人派工）
- 票面落点：.scratch／tickets／2026-11-16-DEBTCLN-R5-TOKPAR红线参数化票-v1.md
- 来源与裁定依据：工具缺口台账在册条目＝count agent tokens 脚本红线硬编码 2500（修法＝参数化不改线值）。链上在册行两处：①DEBTCLN-R4 收口登记行 49 ⟦R4 闭环候 R5 TOKPAR（count_agent_tokens.py 红线 2500 参数化·线值不动）开票⟧（收口笔 94a5ac6·链上面现读）；②SWB-B2 收口登记行 25 ⟦红线参数化旧缺口同族·执行席径修⟧（旧缺口随登在册）。线值真源＝皮总 10-25 拍板「2500 token 红线不动」；参数化目的＝可运维性，线值本身绝不改（决策者已裁起票·主理人派工在册）。
- 候裁点：**0 枚**（见 §六；两项口径自决并附论证）。

> **票面自注（防自咬体例）**：本票正文对一切路径仅叙述性提及＝裸文写＋全角斜杠（／U+FF0F），不落反引号路径指针；引用既有原文以 ⟦⟧ 标记。§二 施工命令围栏内半角径＝程序准绳（R3／R4 票同形制命令经自靶 exit 0 在册＝围栏内不入机检违例面）。本票面成文后自靶 python share/check-pointers.py --root . --target 本票面实路径 须 exit 0（读数见 §七）。

---

## 〇、开工读数（起草轮现跑·禁抄旧数）

**警示行（R3 假钉值红-1 教训在册）**：本节全部消费脚本 exit 钉值均为当轮现跑取证，禁凭记忆填值；下游各笔验收读数一律各自当轮现跑，本表只作起草态基线对照不作验收钉值本身。

| 项 | 命令 | 实测读数 |
|---|---|---|
| 时点 | date '+%F %T %z' | 开工 2026-11-17 07:35:36 +0800（收尾复跑见 §七） |
| HEAD | git rev-parse --short HEAD | **94a5ac6**（＝DEBTCLN-R4 收口登记笔·链顶·与派工预期全等） |
| index.lock | ls .git／index.lock | **不存在**（NO_INDEX_LOCK） |
| tracked 脏面 | git status --porcelain | 恰一枚 M＝agent-experts／baigong-software-team／.collab／ledger／ledger.jsonl（他案脏面·禁碰禁入票） |
| untracked 全集 | 同上 | ?? 当轮值照登（开工轮计数 28 行＝2026-11-12 系列平放 md＋.collab／board／＋.collab／research／＋仓根杂散等·另有本席取证族 .scratch／debt5／ 数枚随登）——全部他案/取证面，不入声明闭集，计数照登当轮值（活体群随外案漂移·禁钉死） |
| 靶面定位（真位 Glob＋find 双式） | Glob 全仓名＝count_agent_tokens.py ＋ find 全仓排除 .git／ | **tracked 真身＝恰一枚＝share／count_agent_tokens.py**（git ls-files 恰一枚坐实）。盘上同名 .py 全量＝118 枚（find 计数当轮值·活体群禁钉死）：真身 1 枚＋取证副本 117 枚；117 枚全部居 .scratch／ 与 agent-skills／fuxi-skill／.scratch／ 两族树内（check-ignore 抽查两枚均 ignored；Glob 与 git ls-files 双式均只出一枚＝其余全部未 tracked 旁证）。 |
| 副本 hash 聚簇 | python sha256 全 118 枚 | 三簇：①**55ccdf0ecdea…**（＝真身·LF 面·恰一枚）；②9df22fc4902b… ×106（＝旧 tools／ 抬头时代快照副本·盘态 CRLF·抬头第二行注 tools 字样）；③abe98debbcf1… ×11（＝share 抬头快照·盘态 CRLF）。簇②③与真身正文逐行比对＝归一化行尾后**仅抬头行差**（簇②差第二行 tools／share 字样·簇③与真身逐字节全等仅行尾制差），三簇均携行 7 RED_LINE ＝ 2500 同码。**靶面判定＝只改真身一枚**：117 枚均为取证树/快照副本（全部未 tracked·非装配链路面）＋工具装配时自包含嵌入使用方包＝2026-11-08 皮总裁定制度性多副本存在——**禁顺手合并·零触**（§四）。 |
| 靶件基线哈希 | python sha256＋git hash-object＋git ls-files | 盘态（LF 面口径）sha256＝**55ccdf0ecdea8dcaf32d38e61fdfd3fb84390581dd8416cf60a10e41acc084e6**；blob＝**e755faef886f46b870a8a965c8029d55d527459b**（链＝盘＝工作区净态·git status 对该文件零命中·git config core.autocrlf＝true 在册而该件盘态恰 LF＝三口径注明沿用）；行数 33（wc -l）；盘态字节 1545。 |
| 硬编码 2500 定位 | grep -n "2500" 靶件＋python 全文计数 | **恰一处＝行 7 原文逐字 ⟦RED_LINE = 2500⟧**；消费点两处＝行 30 ⟦flag = 'OK ' if t <= RED_LINE else 'OVER'⟧ 与行 31 ⟦bad += t > RED_LINE⟧（经常量非字面）。脚本内其余硬编码关联值核查：CJK 区段正则＋非 CJK 除数 4（口径参数·射程外零触）；报告文案零 2500 字样（输出行不含线值）；**无其它 2500 关联硬编码面**。仓内他处 2500 字样归因照登：check-source-of-truth.py 行 52/90 注释引「2500 分轨口径」史注＋行 161 SKILL_LINE ＝ 5000（技能层另一线值·非本脚本红线常量·零触）；70-charter.md 行 47 口径引用面（零触）。 |
| 现行为基线（脚本本体） | python share／count_agent_tokens.py（缺省无参） | **exit 0·输出 7 行全 OK·OVER 0**；逐文件 token 读数按输出序照登＝1889／2462／2480／2465／2289／2496／2496（七枚·最大值 2496 贴线未过）；输出快照 sha256＝**06289e5a…**（取证族内在册）。显式 glob 臂基线：python share／count_agent_tokens.py "share／*.py" → **exit 1·14 行·OVER 10**·输出快照 sha256＝**c687abaa…**。--help 臂改前基线＝脚本无参数解析面，--help 被当 argv[1]  glob 消费→**exit 0·空输出 0 字节**（改前既有形态照登·非帮助页）。**脚本无 --selftest 类自测面**（现读坐实·无自测可跑）。 |
| 缺省指针钉值 | python share/check-pointers.py --root . 缺省扫描 grep -c BLOCK／grep -c WATCH | **BLOCK 22809／WATCH 4582**（＝R4 收口定格新态·与派工预期全等·活体面随外案摆动禁钉死）；缺省扫描 exit 1（既有基线态）。 |
| 靶件改前自靶 | python share/check-pointers.py --root . --target share／count_agent_tokens.py | **exit 0**（改前零悬空在册）。 |
| 全仓门禁基线 | bash share／run-gates.sh | **GATE PASS exit 0·发现 151502**（当轮现跑·与派工预期全等·活体面禁钉死；注＝门禁入口实体为 run-gates.sh，派工令所称 run-gates.py 仓内无此名·Glob 实证，以 .sh 现跑为准随登）。SCRIPTS 清单现读 12 项**不含本靶件**＝本脚本不在门禁调用链（消费面核查①）。 |
| 消费脚本改前基线 | check-collab-lint／check-source-of-truth 现跑 | lint **exit 1**（spec=EAC-L1 count=2006／EAC-L2 count=4097／EAC-L3 count=0·分账 EXEMPT 0／SUBSTR 1029／VIOLATION 4097）；csot **exit 0**（模式 dual｜文件 129｜BLOCK 0（新命中 0）｜基线豁免 54（WATCH）｜指针 WATCH 413）。 |
| 消费面核查 | git grep 全仓 tracked | count_agent_tokens 字样 tracked 命中面＝①check-source-of-truth.py 行 86 注释（口径同款声明·非调用·零触）；②70-charter.md 行 47 口径引用（文档引用面·零触）；③史件/登记面若干（链上史件零触）。**无任何脚本运行时调用本靶件**（run-gates.sh SCRIPTS 不含·install/钩子链不含）＝改码对全部门禁脚本输入面零变化（V3 论证根基）。 |
| 取证族零扰动实证 | 取证族（.scratch／debt5／·含改后仿真产物）落盘后复跑三扫描 | 缺省指针扫描 diff **零行**（BLOCK 22809／WATCH 4582 双不变）＋lint diff **零行**＋csot diff **零行**＝取证面自身对三机检零增量（仿真产物入扫面无新指针出账）。 |
| 仿真落笔坐实（取证族 .scratch／debt5／·用毕即拆） | 隔离副本式实跑（复制真身→§二 同款四前置断言→同款插入→全套臂复跑） | 四断言全过（MULTI-LITERAL／LIMIT-PRESENT／NOT-33-LINES／CRLF-UNEXPECTED）＋ANCHOR-MISS 反证就位；产物＝**40 行**·盘态 sha256＝**2a549d226c3704ce90296a7daa7979507faf2d4011a92eeca5fbfcecd3fd233e**·blob＝**ba4d92973501e9ea0e79f5a36791a8365be53bb8**·py_compile 通过。行为臂全套：不带参运行输出与改前基线 diff **零行**＋exit 0 全等；--limit 2500 输出与不带参 diff **零行**（显式同值＝缺省全等）；--limit 2400→exit 1·OVER 5；--limit 2496→exit 0；--limit 1889→OVER 6；--limit 1888→OVER 7；--limit 3000＋glob 臂＝OVER 8 且 **--limit 前置／后置两序输出逐字节全等**（快照 sha 6abdb53c…）＝参数位次无关性坐实；不带 --limit 的 glob 臂输出与改前 glob 基线 sha **全等**（c687abaa…）；--limit 无值→exit 1·stderr 错误行；--help 臂（不带 --limit）→exit 0·空输出＝与改前基线全等。**行 7 RED_LINE ＝ 2500 字面改后原样在场＋默认 glob 两条原样在场（逐行现读坐实）。＝参数化零自咬·零回归·零机检增量，坐实。** |

## 一、案件本体与坐实

债＝工具缺口台账在册条目：token 计数脚本红线硬编码 2500（工具缺口台账口径）。现态＝红线常量以字面写死于靶件行 7（RED_LINE ＝ 2500），运维调线须改源码＝可运维性缺口；同时该线值为皮总 10-25 拍板值，任何场合不得改值。失步形态＝「值正确但不可调」：既有缺口登记两处在册（§票头来源行①②），销法＝参数化（运行时可覆盖）＋默认值保持 2500 字面不变＝语义零变、行为零回归。

靶面清单＝tracked 恰一枚（share／count_agent_tokens.py）；盘上另 117 枚同名副本＝取证树快照＋自包含嵌制度性存在（2026-11-08 皮总裁定），全数零触禁合并（§四写死）。

## 二、声明闭集（＝恰一枚施工面·插入式改码·禁酌情）

**S1 · 靶件插入 7 行块**（插入位＝行 15 注释 ⟦# 显式传 argv[1] 时按单 glob 覆盖（旧行为不变）。⟧ 之后、行 16 ⟦if len(sys.argv) > 1:⟧ 之前＝argv[1] 消费前剥离 --limit 对，参数位次无关＋默认 glob 语义原样）。插入块 verbatim（前态＝该锚注释行与 if 行之间现为空＝无此行；后态＝逐字如下 7 行）：

```python
    # DEBTCLN-R5 红线参数化：--limit 整数值运行时覆盖红线；默认＝行 7 RED_LINE＝2500（皮总 10-25 拍板值不变）。
    if '--limit' in sys.argv:
        _i = sys.argv.index('--limit')
        if _i + 1 >= len(sys.argv):
            sys.exit('count_agent_tokens: --limit 后须整数值')
        RED_LINE = int(sys.argv[_i + 1])
        del sys.argv[_i:_i + 2]
```

块全文 sha256（UTF-8·含行尾 LF 面口径）＝**c2e49c06383fb4da9c1395c269319e2365561761733ab783264782aee3e67abe**（块字符数 316·七行逐行 sha256 前缀钉＝77bc232f／a7f427fa／e5d5e92a／332cac5f／ef708572／7db57d09／f30c539d·起草轮仿真实算钉版·V2 复算）。

**施工手段规格（唯一准绳·两步·块先钉哈希再插入·四重前置断言防手误）**：

第一步＝块落盘（heredoc 逐字·禁手敲增删）：

```bash
mkdir -p .scratch/debt5/b1 && cat > .scratch/debt5/b1/block.txt <<'BLOCKEOF'
    # DEBTCLN-R5 红线参数化：--limit 整数值运行时覆盖红线；默认＝行 7 RED_LINE＝2500（皮总 10-25 拍板值不变）。
    if '--limit' in sys.argv:
        _i = sys.argv.index('--limit')
        if _i + 1 >= len(sys.argv):
            sys.exit('count_agent_tokens: --limit 后须整数值')
        RED_LINE = int(sys.argv[_i + 1])
        del sys.argv[_i:_i + 2]
BLOCKEOF
```

第二步＝断言＋插入（程序化·一次落盘）：

```bash
python - <<'PYEOF'
import hashlib
p='share/count_agent_tokens.py'
s=open(p,encoding='utf-8',newline='').read()
assert s.count('RED_LINE = 2500')==1,'MULTI-LITERAL'
assert '--limit' not in s,'LIMIT-PRESENT'
assert s.count(chr(10))==33,'NOT-33-LINES'
assert chr(13) not in s,'CRLF-UNEXPECTED'
blk=open('.scratch/debt5/b1/block.txt',encoding='utf-8',newline='').read()
assert hashlib.sha256(blk.encode('utf-8')).hexdigest()=='c2e49c06383fb4da9c1395c269319e2365561761733ab783264782aee3e67abe','BLOCK-HASH-MISMATCH'
anchor='    # 显式传 argv[1] 时按单 glob 覆盖（旧行为不变）。'+chr(10)
assert s.count(anchor)==1,'ANCHOR-MISS'
open(p,'w',encoding='utf-8',newline='').write(s.replace(anchor,anchor+blk,1))
print('INSERTED-7-LINES')
PYEOF
```

（断言＝行 7 字面值唯一否则拒改／--limit 零先例否则拒改／基线恰 33 行否则拒改／盘态零 CR 否则拒改（行尾制随动断言系本件 LF 实测态所定·§〇 行尾制在册）／块哈希对钉否则拒改／锚行唯一否则拒改。产物＝同文件 40 行·既有 33 行 byte 零扰动＋7 行插入＋无删除；工程师用其它手段须同等过 V1／V2。）

**改后靶件预期态（仿真钉版·复算基准非验收钉值）**：40 行；盘态 sha256＝**2a549d226c3704ce90296a7daa7979507faf2d4011a92eeca5fbfcecd3fd233e**（LF 面口径）；blob＝**ba4d92973501e9ea0e79f5a36791a8365be53bb8**；行 7 仍＝RED_LINE = 2500 字面（V1 前置）；默认 glob 两条仍在场。

**已申报差量面（非基线臂·显式申报非回归）**：①--limit 无值＝改前被当 glob 消费（exit 0 空扫）→改后 fail-fast exit 1 带错误行；②--limit 非整数值＝改后 ValueError 栈 exit 1（错误文案称整数值·非整输入走异常面仍非零 exit·运维面语义一致）。两臂均非既有使用形态（无任何调用方传 --limit·§〇 消费面核查），申报在册防误读。

### 禁动面（写死）

- **默认线值 2500 字面值禁改＝语义零变**：行 7 ⟦RED_LINE = 2500⟧ 一个 byte 不动（＝皮总 10-25 拍板值面·10-25「2500 token 红线不动」）；仓内他处 2500 字样（70-charter 口径行／check-source-of-truth 注释与 SKILL_LINE ＝ 5000 技能层线值）全部零触。
- 靶件其余面零触：头注四要素声明（行 1-4）、CJK 正则与 tokens 函数（行 6-10，口径 script-v1 真源面）、默认 glob 两条（行 19-20 现位）、exit 语义（行 33 现位）。
- 取证快照与自包含副本 117 枚全部零触·禁顺手合并（2026-11-08 皮总裁定制度性多副本）；agent-skills／fuxi-skill／.scratch／ 树内全部副本零触（FUXI 零碰）。
- 他案脏面零带入：ledger.jsonl 之 M 态＋?? 当轮全集＝禁碰禁入库。
- 链上史件零回改；账本面零手写；.gitignore 零触。

## 三、验收判据（全机械·命令＋钉值·禁凭记忆填值）

- **V0 开工读数**：施工轮现跑 HEAD＝94a5ac6 链上本票落链后最新值如实照登；git status 他案脏面形态与 §〇 一致（ledger 一枚 M＋?? 当轮值照登——禁扩集口径沿 R1-R4 先例；本票落链后本票面转 tracked，?? 不含本票）；index.lock 不存在坐实。
- **V1 参数化后缺省行为零回归**：
  1. python -m py_compile 靶件 → exit 0。
  2. 不带参运行靶件 → **exit 0**＋输出与施工笔前态快照 diff **零行**（施工轮改前自备快照＝基线面·活体外仓 agents 禁跨轮钉死）；§〇 基线读数复对＝7 行全 OK·OVER 0·token 钉值 1889・2462・2480・2465・2289・2496・2496 在场（外仓活体面若他案漂移＝如实照登＋归因禁遮掩）。
  3. 行 7 字面在场唯一：grep -c "RED_LINE = 2500" 靶件 ＝ **1**；改前行面（git show 施工笔父面）同式＝1（前态恰 1 复证·非 0→1 型）。
  4. 默认 glob 两条未动：git show 施工笔 diff 面单核验＝删除行集 **空**（纯插入型·见 V2）。
- **V2 插入块逐字对钉（INSERT-EQUAL 式）**：git show --numstat 于施工笔＝**7／0**（纯插入零删除）；逐行对拍改行集＝**[]（既有 33 行零改动）**＋行数 33→40＋块哈希对钉：

```bash
python -c "import subprocess,hashlib;b=open('share/count_agent_tokens.py',encoding='utf-8',newline='').read();a=subprocess.run(['git','show','HEAD^:share/count_agent_tokens.py'],capture_output=True).stdout.decode('utf-8',newline='');blk=''.join(l+chr(10) for l in b.splitlines(True)[15:22]);d=[i+1 for i,(x,y) in enumerate(zip(a.splitlines(True),b.splitlines(True))) if x!=y];import hashlib as h;print('CHANGED',d,'LEN',len(a.splitlines()),len(b.splitlines()),'BLK',h.sha256(blk.encode('utf-8')).hexdigest(),'DISK',h.sha256(open('share/count_agent_tokens.py','rb').read()).hexdigest());raise SystemExit(0 if d==[] and len(a.splitlines())==33 and len(b.splitlines())==40 and h.sha256(blk.encode('utf-8')).hexdigest()=='c2e49c06383fb4da9c1395c269319e2365561761733ab783264782aee3e67abe and h.sha256(open('share/count_agent_tokens.py','rb').read()).hexdigest()=='2a549d226c3704ce90296a7daa7979507faf2d4011a92eeca5fbfcecd3fd233e' else 1)"
```

→ **exit 0** 且打印 CHANGED [] LEN 33 40＋BLK c2e49c06…＋DISK 2a549d22…（基线以施工笔父笔链上态为准；HEAD^ 写法按实际父笔 sha 置换并照登；盘态 LF 口径注明三口径纪律沿用）。
- **V3 参数生效实证（带参臂·仿真已钉·验收复跑）**：
  1. --limit 2500（不带 glob）输出与不带参 diff **零行**＋exit 码全等（显式同值＝缺省）。
  2. --limit 2400 → **exit 1·OVER 5**；--limit 2496 → **exit 0**；--limit 1889 → OVER 6；--limit 1888 → OVER 7（外仓活体 token 值若漂移＝按当轮不带参读数重推导 OVER 数随动＋归因照登，禁跨轮死钉）。
  3. glob 臂＋参数位次：python share／count_agent_tokens.py "share／*.py" --limit 3000 与 --limit 3000 前置式，两输出逐字节全等＋OVER ＝ 8（§〇 仿真钉 6abdb53c 同构复对）。
  4. 不带 --limit 的 glob 臂输出与改前同臂快照 diff **零行**（旧行为不变条不破坏）。
  5. 已申报差量两臂复现：--limit 无值 → exit 1；--limit abc → exit 非零（§二 申报面复证·禁误计回归）。
- **V4 门禁四件套改前后零变化**：python share/check-pointers.py 缺省扫描 grep -c BLOCK／grep -c WATCH → 预期 **BLOCK 22809／WATCH 4582 双零变化**（插入块零反引号零路径 token＝零指针增量·仿真在册；改前后 diff 零行＋**指针差量归因口径**＝靶件头注行 2 自引路径零动＝既有计数面该件出账零变化；若差量非零＝逐行归因禁遮掩）；bash share／run-gates.sh → **GATE PASS exit 0**，发现数照登（基线 151502·活体面禁钉死·变化归因照登·禁总数增减类伪钉值；SCRIPTS 不含靶件＝输入面先验零变化）；check-collab-lint 现跑 **exit 1 与本施工轮改前基线 exit 全等**＋计数照登（EAC-L1 2006／EAC-L2 4097／EAC-L3 0·VIOLATION 4097）＋改前改后输出 diff **零行**；check-source-of-truth 现跑 **exit 0 与基线全等**＋计数照登（BLOCK 0／豁免 54／指针 WATCH 413／文件 129）。四件套 exit 钉值全部当轮现跑（R3 假钉值红-1 教训）。
- **V5 自靶**：python share/check-pointers.py --root . --target 施工后靶件实路径 → **exit 0**（改前基线 exit 0 在册 §〇；插入块零路径 token＝零增量）；本票面（链上现文）同式 exit 0 复证；回执面同式 exit 0。
- **V6 commit 面单核验口径**：照 R2 收口登记 §四 终版＝核验时点 git diff --cached --name-only 实测 staged 恰靶件一枚（BUILD 笔）或恰回执一枚（RECEIPT 笔）＋钩子 STAGED-DECL 互证为准；commit 树面并发窗裹入他案＝归因在册不构成施工违例；禁写总数增减类伪钉值。

## 四、观察行（随登·不立项不候裁）

- 117 枚取证/快照副本与真身将呈内容差（真身携 --limit 块·副本不携）＝制度性多副本面的预期分叉（自包含嵌裁定在册）；若后续「装配嵌入版本账」类缺口另案在册候排，本票零处置防 scope 扩面。
- check-source-of-truth.py 行 86 注释「同款实现」口径声明＝注释面引用，参数化不改口径本体（tokens 函数零触），工具注释零改观察行。
- 靶件盘态 LF 而 core.autocrlf＝true 并存＝既有现状（§〇 三口径纪律注明）；断言 CRLF-UNEXPECTED 保改后同制。
- 脚本无 --selftest 自测面＝既有形态照登（§〇），补自测非本票射程（YAGNI）。
- 门禁入口实体名 run-gates.sh 与派工令所称 .py 出入＝以仓内实体现跑为准随登（§〇 在册）。

## 五、排程（串行两笔施工段）

链第 1 步＝本票起草笔（架构席·本笔）。第 2 步＝双席快审（产品席＋QA 席 fresh eyes：审 S1 块可照抄性·V 系完备性·已申报差量两臂取舍·靶面单枚判定论证）。第 3 步＝放行登记（主理人）。第 4 步＝工程师施工一笔（靶件一枚·§二 两步命令）＋**回执一笔**（落 .collab／receipts／ 桶·R1 勘正口径）。第 5 步＝fresh QA 按 §三 V 系独立验收判词。第 6 步＝收口登记（主理人）。

**排程红线**：工程师一笔 BUILD＋一笔 RECEIPT 串行；fresh QA 独立验收照 V 系；各笔面单恰枚＋STAGED-DECL 互证。

## 六、候裁面（必有节·**候裁 0 枚**）

- **自决① · 参数形态＝--limit 整数值·argv 全文检索＋消费前剥离（位次无关）**：候选比较＝a）argparse 完整帮助页——否：靶件现为无解析极简形态（33 行自包含工具），argparse 引入帮助页输出面改变 --help 改前基线（空扫→帮助页），违反 V1 零回归红线且超出缺口最小修法；b）仅认 argv[1] 位——否：位次歧义运维面踩坑（glob 与参先后不定），仿真位次无关仅两行成本；c）环境变量——否：不可显式审计·与仓内脚本参数化惯例（--root／--target 式）不合。取 b 形态＝最小插入块＋fail-fast 无值断言（位次无关已并入 b 判据）。先例口径＝仓内脚本参数化惯例（check-pointers --root／--target 同款 flag＋value 形态）。
- **自决② · 无值／非整值 --limit＝fail-fast 申报差量（非基线臂）**：改前该形态为无语义空扫（exit 0 空输出），属既有基线外形态；不申报差量而保持静默＝调线拼错时静默假绿（运维缺口反增），故取 exit 非零显式失败＋§二 申报面在册。双席若裁须保持旧静默形态或补 try/except 整值守卫＝随其裁落另出 rev，不预判。

批次编排类不上楼＝不自列候裁；两项均属票内口径归起草席位闭合。

## 七、起草笔自证（落笔后、commit 前实跑）

- 开工读数＝§〇 全表（当轮现跑·HEAD 94a5ac6·收尾时点见完工回报）。
- 本票面自靶＝python share/check-pointers.py --root . --target .scratch／tickets／2026-11-16-DEBTCLN-R5-TOKPAR红线参数化票-v1.md → **exit 0**（实跑坐实·读数见完工回报）。
- 防自咬体例取证在册（.scratch／debt5／ 取证族·用毕即拆口径见回报）：§〇 仿真落笔全套读数在册（§〇 末行·隔离副本式＋四断言反证＋九行为臂）；本票笔成文时点靶件仍＝改前净态（修票不施工·git status 对靶件零命中在册）；取证族落盘对三机检 diff 零行实证在册（§〇 零扰动行）。
- 靶件基线双哈希＋行尾制＝§〇 在册（盘 sha256 55ccdf0e…LF 面／blob e755faef…／33 行／CR 零枚）；V2 基线以本票落链后链上笔为准（本票笔不触靶件，HEAD 态靶件哈希不变）。
- 本笔面＝恰票面一件；其余全程零触碰；他案脏面零带入。

## 八、链衔接纪律段（各笔共守·写死）

- 单件／本笔面 pathspec 两端齐带（add 与 commit 各带本笔面路径）；add 紧邻 commit 零窗口；commit 前 git diff --cached --name-only 坐实仅自笔面。
- FX_COMMIT_DECLARE＝仓根相对纯路径清单（逗号或换行分隔）**挂 commit 命令侧**（挂 add 侧会被 STAGED-DECL-BLOCK 拦）。
- 禁 add -A／禁 amend／禁 --no-verify；message 以 collab: 起头·零 at 符号·零反引号；尾标置 message 最末位。**本票各笔尾标闭集**：本票笔 -TICKET／QA 快审笔 -QA-REV／产品快审笔 -PM-REV／放行登记笔 -PM-RELEASE／工程师施工笔 -BUILD／工程师回执笔 -RECEIPT／QA 验收笔 -QAV／收口登记笔 -GCLOSE（族名 DEBTCLN-R5 随尾标内嵌）。
- 一票一 commit 增量落盘；commit 类命令 timeout 600000ms；撞 index.lock 先 tasklist 坐实 git.exe＝0 枚再按有证删锁先例处置（R3／R4 案型在册），案型如实登记不 amend。
- 防自咬体例＝票面／回执正文路径裸文＋全角斜杠叙述形态；引文 ⟦⟧；票面与回执自身须过 check-pointers --target exit 0 后才可落链。
- 临时工作物只落仓根 .scratch／debt5／ 族；本席起草笔只写票面这一件。

---

（v1 尾·append-only：后续修订在此处续 rev 段，rev 段间互不回改）
