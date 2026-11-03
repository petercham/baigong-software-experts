# plugin.json 跨仓 source 能力验证报告 v1（待拍②实测票）

## 【来源】帽

- 本席：产品经理席（pm-r1r2-verify，Team: _auto_15e90588-7dd0-436b-9d06-de2f2118f90f）
- 当轮三仓 HEAD 读数（2026-10-26）：`D:\multi-agent-collab-skillpack` @ `3e999ac`；`D:\multi-agent-collab-experts` @ `fa0e6d0`；`D:\multi-agent-collab-skills` @ `33739b3`
- 取证面：① 本机部署面实况（`C:\Users\peter\.workbuddy\plugins\` 注册形态）；② 平台 CLI 代码直读（`WorkBuddy\resources\app.asar.unpacked\cli\dist\codebuddy-lite-wb.mjs`，minified 但含完整 marketplace/plugin 安装逻辑，以下代码摘录均出自该文件）；③ 官方文档 WebFetch + WebSearch 外部资料；④ 静态实验（只读，未注册到真实部署面，未改三仓任何真源文件）
- 对应前序：`2026-10-26-跨平台维度耦合与装配部署补证调研报告_v1.md` 问 4（Anthropic marketplace.json「同构」未经平台验证）——本报告补上平台验证。

---

## TL;DR（三态结论 + R1/R2 建议）

1. **三态结论：不支持**（就「bundle 内组件（skills/）声明指向仓外路径／marketplace.json 式跨仓引用、注册时由平台解析装配」这一 R1 语义而言）。证据为代码级强证据，非「证据不足」。
2. **但有一个此前未记录的中间形态**：平台在 **plugin 整包粒度**支持跨仓 source（`git-subdir` 类型：指定 git 仓库 URL＋子目录 path＋可选 sha，sparse checkout 拉取）。即「跨仓」能力存在于 *marketplace.json 的 plugins[] 条目*（一个插件整体从另一仓的子目录拉取），**不存在于** *plugin.json 内 skills[]/agents[] 字段*（只接受 bundle 内相对路径）。
3. **R1/R2 终选建议：维持 R2（自研装配 publish.py --assemble）**。R1 语义（退掉装配复制步、由平台解析 bundle 内跨仓指向）在平台上无落点；装配复制步必须保留。bundle.lock 账本价值独立于 R1/R2，不受影响。

---

## 证据一：本机部署面实况（注册形态）

### 1.1 marketplace 级注册（`known_marketplaces.json`）

marketplace 本身有 source 字段，支持两类：
- `"type": "zip"`＋`url`（官方市场，从 download.codebuddy.cn 拉 zip）
- `"type": "directory"`＋本地 `path`（如 `my-experts`、`experts` 均指向 `~/.workbuddy/plugins/marketplaces/<name>` 本地目录）

→ 这是 **marketplace 粒度**的来源声明，不是 bundle 内组件粒度。

### 1.2 marketplace.json 清单（`my-experts/.codebuddy-plugin/marketplace.json`）

```json
{ "name": "my-experts",
  "plugins": [
    { "name": "hjh-software-team", "source": "./plugins/hjh-software-team", "version": "1.2.1" },
    { "name": "hjh-aigc-video-team", "source": "./plugins/hjh-aigc-video-team", "version": "1.5.0" } ] }
```

plugins[].source 为**字符串相对路径**（指向 marketplace 根内子目录）。与 Anthropic marketplace.json 同构的判断**成立**（前序报告问 4 的「同构」猜测经本机验证为真），但同构≠支持跨仓——见证据二 containment 强制。

### 1.3 plugin.json 现有字段全集（devkits 软开包 + experts 视频包 + 官方 document-skills 对照）

三方对照后，`skills`/`agents` 字段全部为 `"./skills/<dir>"`、`"./agents/<file>.md"` 形式的 **bundle 内相对路径**；无任何 source/url/registry/path 外引字段。官方市场插件（`document-skills@cb_teams_marketplace`）同样只有 `"skills": ["./skills/pdf"]`。

### 1.4 experts 仓 bundle.lock 现状（对照物）

`bundle.lock` 的 `components[].repo: "../multi-agent-collab-skills"` ＋ `ref: <commit>` 是**自研账本格式**，平台无对应解析器（代码中无 bundle.lock 字样）——它只被 devkits `publish.py --assemble` 消费，与平台注册面无关。

---

## 证据二：平台 CLI 代码直读（最强证据）

### 2.1 source 类型枚举（闭集）

```js
t.Local="local", t.Github="github", t.Url="url", t.Npm="npm", t.Pip="pip", t.GitSubdir="git-subdir"  // E 枚举
```

marketplace 级另有 `zip`/`directory`。**没有**「bundle 内组件外部引用」类型。

### 2.2 marketplace 根 containment 强制（跨仓相对路径直接抛错）

```js
function resolvePathUnderRoot(t,i,n){
  let s=resolve(t), c=resolve(s,...i);
  if(!isPathContainedInRoot(s,c,n)) throw Error(`Path escapes marketplace root: ${i.join("/")}`);
  return c }
```

marketplace.json 里 `source: "../other-repo/..."` 类越界路径在安装时被 `Path escapes marketplace root` 拒绝。

### 2.3 安装＝整包复制到 cache，外部引用必然断链

```js
async copyPluginToCache(t,i,n){
  ...
  if(n && !this.isPathInside(c,s)) throw Error(`Plugin source path escapes marketplace root: ${t}`);
  // copyEntry 逐条复制，跳过 .git，符号链接有专门防越界检查（Unsafe ... directory / escapes plugin cache）
```

安装后插件被复制到 `plugins/cache/<marketplace>/<name>/<version>/` 独立快照；plugin.json 里若写 `"../multi-agent-collab-skills/skills/..."`，该路径在 cache 快照中不存在——**即使 schema 不报错，加载时也会找不到**（skills 加载回退逻辑就是扫 cache 内 `./skills/` 目录）。符号链接路径同样被 `escapes plugin cache` 检查拦截，symlink 逃逸这条路也封死。

### 2.4 plugin.json 内 skills[]/agents[] 无外引语义

代码中 skills 字段消费方式：读取 manifest → 相对 plugin 目录解析 → 扫 `SKILL.md`；无 skills 字段时回退扫 cache 内 `skills/` 目录（`./skills/${t}`）。全程无 URL/git/repo 解析分支。

### 2.5 git-subdir：plugin 整包粒度的跨仓能力（新发现）

```js
support(t){ return t.source===E.GitSubdir }
async install(t,i,n){
  let s=t.source; this.validateGitSha(s.sha);
  let c=s.url||s.repo, ... h=this.getValidatedSubdir(s);
  // git sparse checkout → plugins/<name>/<subdir>
}
getValidatedSubdir(t){ // path/subdir 禁绝对路径、禁盘符、禁 ".."
```

即：marketplace.json 的一个 plugin 条目可以声明 `{source:"git-subdir", url:"<git repo>", path:"workbuddy/hjh-aigc-video-team", sha:"<commit>"}`，平台 sparse-checkout 该子目录。**sha 锁定支持**（validateGitSha）——这点与 bundle.lock 的 commit 锁理念同源，但粒度是「整个插件来自某仓某子目录」，不是「插件内某组件来自另一仓」。

---

## 证据三：官方文档与外部资料

- WebFetch `https://www.workbuddy.cn/docs/workbuddy/Overview`：公开文档站无插件 manifest 规范页（无 plugin.json/marketplace.json schema 文档）。
- WebSearch 外部资料（访问日期 2026-10-26）：
  - 军舰日志《WorkBuddy 专家/专家团机制研究》：plugin.json 字段规范（源自内置 expert-manager 的 `references/plugin-json-spec.md`）——资源声明仅 `agents: string[]`、`skills: string[]`（bundle 内路径），无跨仓字段。
  - 腾讯云开发者文章《好习惯小助手从 Skill 到专家包》：明确「skills/ 整包搬进来」「唯一合法位置 `~/.workbuddy/plugins/marketplaces/my-experts/plugins/`」——社区实操与本报告代码证据一致：技能以**复制进 bundle** 方式使用。
  - 内置专家管理技能（本机 `workbuddy-builtin` 的 expert-manager）亦按「skills 在包内」建模。

## 实验说明

- 已做（只读）：三仓 plugin.json/bundle.lock 字段对照；本机注册面三本账（known_marketplaces / marketplace.json / installed_plugins）结构读取；CLI bundle 代码直读定位安装/校验路径。
- 未做（按任务边界）：真实注册实测。因代码级 containment 证据已闭环（2.2/2.3 双重抛错点），**无需**注册实测即可定论「不支持」；下列步骤仅供皮总想留一份反证记录时执行。

### 皮总侧最小实测步骤（可选反证，5 分钟）

1. 复制 `my-experts/plugins/hjh-aigc-video-team` 为临时副本包（勿动真包）。
2. 副本 plugin.json 的 skills 首项改为 `"../multi-agent-collab-skills/skills/aigc-video-governance"`。
3. 客户端插件面板刷新/重装该包。
4. 看信号：a) 面板是否报 `Path escapes marketplace root` / `escapes plugin cache`；b) 若面板无报错，则打开专家详情看五技能是否消失（cache 快照内无该路径＝加载必失败）。任一信号出现即坐实「不支持」。
5. 清理副本。

---

## R1/R2 终选建议

**终选 R2（自研装配），R1 判死。**

- **R1 不可行的落点缺失**：平台没有「bundle 内组件跨仓指向、注册时解析装配」的任何机制；反而有三重反向证据（marketplace-root containment、cache 整包复制快照、symlink 防逃逸）。Anthropic 同构的是 **marketplace.json 清单格式**，而该格式在两家都同样把跨仓限制在 marketplace 根内。
- **退不掉**：`publish.py --assemble` 装配复制步保留（它是把 skills 仓组件物化进 bundle 的唯一途径）。
- **保留（本就独立于 R1/R2）**：`bundle.lock` 账本（组件→仓→commit 锁）价值不变——平台侧无版本账本，账本只能自研；git-subdir 的 sha 锁反而佐证「锁 commit 引用外部源」是行业做法，只是 WorkBuddy 把它放在 plugin 粒度。
- **可选演进注记（不影响本次终选）**：若未来想把「技能仓」直接上架，可用 `git-subdir` 把 skills 仓的某子目录作为**独立插件**发布（用户侧装两个插件：专家包＋技能包）。但这改变产品形态（用户需分别安装、专家包 plugin.json 仍不能引用技能包内容），与「一个专家包自包含交付」现状诉求相悖，不建议现在采用。

## 附：本次取证未覆盖项（如实标注）

- 平台是否有未公开的内部 manifest 扩展字段：CLI bundle 内枚举闭集已见（2.1），未见其他；无法排除服务端市场有额外装配层，但本机 directory/zip 市场路径均走同一 containment 代码，风险低。
- WorkBuddy 版本相关：证据取自本机当前安装版 CLI（5.9.2-wb.42136757 系）。平台若后续引入组件级引用，需重验。
