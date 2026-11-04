# SWB-ESC1 · era 外部参照件跨仓移交微批 · 工程师回执 v1

- 回执席＝engineer-b5；票＝`.collab/2026-11-04-SWB-B批总收口登记-v1.md`（commit `3b03738`）（ESC1 票面已退役·收口见该件 ESC1 段）；清单真源＝B3 回执 §七「era 移交清单·出处二次分账」＋§五 era 计数钉口径。
- 开工 HEAD 实测（两仓各附）＝devkits `50e726a`（＝B5/B 批收口登记笔✓）·工作区 clean；experts `87199fa`·工作区 clean（仅 `.collab/`/`.workbuddy/` untracked 非本票面）。
- 计数口径＝occurrence＋`git -c core.quotepath=off`；判据自带落盘；负例 exit≠0。

## 一、两仓两笔 hash 并列

| 仓 | 笔 | hash | name-only 读数 |
|---|---|---|---|
| experts | ESC1-B 接收笔 | `29034b1` | **29** 件（全 `research/era-2026-10/**` 新增·commit message 无前缀改随该仓纪律＝中文叙事式先例） |
| devkits | ESC1-C 删源笔 | `87bf5e7` | **25** 件（tracked git rm）＋**4** 件 untracked 文件系统删补账行（dispatch R6/R7/R8＋evidence gate-01＝ignore 排除面不入 commit）＝删源面全数 29 |

落位实际行登记（票面 ESC1-D 两态口径）＝era 留置位开工实测＝仓根 `.collab/research/`（未随 B3 入项目桶）＋仓根 dispatch/evidence 四支＝「B3 先于 ESC1」正常态 ✓；experts 侧落位＝`research/era-2026-10/<原相对路径>`（该仓无 README 结构件规定 research 规范＝开工读取定案：仓 README 只放 bundle 本体＋`.dev` gitignore 条款；本接收面置仓根 `research/era-2026-10/` 层＝票面缺省落位·件名基名零改·族内相对结构保留防同名撞名〔video-team/ 与 original-5/ 与 aigc-video-team/ 三族存在同名基名 6 对〕）。experts `.gitignore` 现面无 research 排除条款＝入库条款缺省成立→**零追加**（开工读现面定案）。

## 二、handover-list 全表（29 行·钉值＝回执行数 29）

`$ESC1_TMP/handover-list.tsv` 三列（基名/原位/sha256）·sha256 列＝原位读出＝接收对账基准：

| # | 基名 | 原位（devkits 仓根相对） | sha256 | 甄别签字 |
|---|---|---|---|---|
| 1 | aigc-video-team.zip | `.collab/research/drafts-2026-10-23/` | `450e899e…9f82` | 第三方（zip 解包族头件） |
| 2 | README-返工说明.md | `…/aigc-video-team/` | `015c280f…06ac` | 说明件随族移交（件头＝批 28 返工说明·基线=my-experts 治理盘 b2933cc 态） |
| 3–9 | aigc-content-strategist / aigc-director / aigc-editor / aigc-operations / aigc-production-designer / aigc-screenwriter / aigc-video-team-lead.md | `…/aigc-video-team/` | `7761a4c9…` `06862e6c…` `0e953fef…` `84e30214…` `d43d72fd…` `547f5855…` `fc214cae…` | 第三方快照 7 席 |
| 10 | 00-撞规清单.md | `…/video-team/` | `114d86c5…d226` | 随源料族移交 |
| 11 | README-源料说明.md | `…/video-team/` | `6eff3aa8…538c` | 说明件随族移交（件头＝批 20 源料说明） |
| 12–17 | README.md＋video-content-strategist / video-director / video-editor / video-qa-operations / video-team-lead.md | `…/video-team/original-5/` | `26f4cbae…` `55ccf550…` `0ef9a598…` `af3ab547…` `7954ab91…` `e7de48af…` | 第三方源料 original-5 |
| 18–24 | video-content-strategist / video-director / video-editor / video-operations / video-production-designer / video-screenwriter / video-team-lead.md | `…/video-team/` | `f06faa55…` `8c910f26…` `31f67643…` `0bab8559…` `5064a5cc…` `77033a1d…` `803c2858…` | 第三方源料 7 件 |
| 25 | 全能AIGC视频创作团队-架构与五维优化方案.md | `.collab/research/reference-2026-10-24/` | `1425e45a…ad28` | 外部参照（主理人合成稿·reference 族 ESC1 候选＝B3 §七 在册） |
| 26–28 | 2026-10-28-R6视频团交接审读机制 / R7短剧编剧团流程剖析 / R8导演定位与策划编剧职责映射-派工书.md | `.collab/dispatch/` | `5b7ccda1…8496` `de2727d4…dbc7` `40b9087c…ee7f` | era 族留置派工书（B3 §七 二次分账在册·era 执行面随移交） |
| 29 | 2026-10-28-T-video-research-gate-01-施工回执.md | `.collab/evidence/` | `3d0a8f50…571c` | era 族留置施工回执（同上） |

自产件二次甄别＝**争议留置 0 件**；本仓自产不外移清单＝`2026-10-23-视频团队本体审计_v1.md` 1 支（审计对象指针在件头＝判词依据·B3 §七 缺省留仓根桶）。#2/#10/#11 说明件定性＝era 案卷内说明面随其源料族整体移交（B3 §七 计数口径 24 含之·拆离反致族不完整）＝签字认可非争议。

## 三、逐件 sha256 接收断言对账表

接收断言＝`sha256sum <experts research/era-2026-10/…>` 对 handover-list 第三列逐行比对：**MATCH 29／MISMATCH 0**（exit 0）。异字节负例探针＝接收件副本追加 `x` 一字节→对账＝不等 exit 1 ✓＝断言机械有效。

## 四、判据 1–5 读数

1. **三值计数全等**：handover-list 行数＝**29**＝experts 接收 commit name-only＝**29**＝devkits 删源 commit name-only 25＋untracked 文件系统删补账 4＝**29** ✓。
2. **逐件 sha256 全等** exit 0（29/29）＋异字节负例 exit 1 ✓（§三）。
3. **devkits era 留置位清单族清零**：`find .collab/research -type f | grep -cE 'drafts-2026-10-23|reference-2026-10-24'`＝**0** ✓；dispatch/evidence 清单族＝**0** ✓；research 现面余自产审计件 1 支＝清单外留置非违例 ✓。
4. **自产件未外移**：experts 接收 name-only ∩ 自产清单（`视频团队本体审计`）＝**∅** ✓。
5. **无誊写违规**：复制全程逐件 `cp`（命令读数＝循环内 `cp -- "$src" "$dst"` 29/29 成功计数＝29 入回执）＝零 Agent 全文重输出自察声明 ✓。

era 计数随账（B3 §五 口径）：`git ls-files .collab/research | grep -cE '视频|video|短剧|导演|编剧'` 删源后复跑＝0＋自产 1＝1（原 26＝25 移交〔24＋reference 1〕＋自产 1）✓ 分解闭合；era 族 research 外 4 支清零 ✓。

## 五、ESC1-D 随动定案＋禁动面自察

- devkits gitignore 三桶 ignore 行（B5 映射表在册）＝**零改**（删源后残留无害）✓；仓根 README era 索引行＝不回头改（「已移交·ESC1 回执指针」＝B 批收口登记级＝主理人侧）✓。
- 禁动面自察：清单外件零触碰（含相邻自产研究件）；experts 既有件内容零触碰（接收笔 name-only 29 全＝新增）；两仓版本账零动 ✓。
- ESC1-A 清单锁定笔＝devkits 只读（`$ESC1_TMP` 落盘不入 git）＝无独立 commit 可落＝如实登记（票面「先行单独笔」在 TMP 面）。
- 全程禁 `--no-verify`、禁 amend；每 commit 门禁族集全跑（删源笔 GATE PASS 8790）。

## 六、候裁／异常

无红项。一处登记级＝experts 仓 commit message 无 `collab:` 前缀＝票面「前缀随该仓纪律」＝该仓先例＝中文叙事式（`feat(rename):`/裸中文），照随。

——engineer-b5 · SWB-ESC1 回执（施工本体全程字节级＝cp/删·誊写禁令 f5a0d96 辖域内自察）。
