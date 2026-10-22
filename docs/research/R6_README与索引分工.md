# R6 研究报告：README 的职责与子目录索引文件选型

> 研究席 res-readme-index · 2026-10-22 · 只读查证，未改任何项目文件
> 等级：A=官方文档/官方风格指南原文；B=大型仓库真实实践/权威二手；C=博客/社区经验帖

## 结论（三问三答）

1. **README 做仓库根文档：对。** GitHub 官方明文定义 README 为仓库门面（A 级），且官方支持 `.github`/根/`docs` 三处放置并有优先级顺序。
2. **README 兼任"边界定义＋索引"：是业界做法，但有流派。** Google 官方风格指南明确要求包级 README 写"这个包是什么/给谁用/状态/指路链接"——即边界＋索引二合一（A 级）；多篇 README 写作指南也建议 README 首段写 scope/非目标（B/C 级）。反方（README 应极简、长文外链）同样存在（B 级，thekarel）。二合一有依据，但"边界写薄、正文外置"是共识。
3. **子包根文件：两者皆有工业化先例，本仓库场景推荐 README.md。** GitHub 浏览目录时自动渲染目录级 README（事实特性，Google 风格指南以官方口吻确认，A 级）；INDEX.md 不被 GitHub 特殊渲染，仅当普通文件。MkDocs/Docusaurus/Hugo 等静态站点器认 `index.md`/`README.md`/`_index.md`，均不认 `INDEX.md`。若仓库要"在 GitHub 上直接浏览即 landing page"，README.md 是唯一被宿主渲染的名字；若纯机检/agent 导航，INDEX.md 有专门规范先例（skissue）但零工具支持。

## 证据清单

### 1. GitHub 官方 README 定义（A）
- URL: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- 原文："You can add a README file to your repository to tell other people why your project is useful, what they can do with your project, and how they can use it."
- 原文（典型内容）："README files typically include information on: What the project does / Why the project is useful / How users can get started… / Where users can get help… / Who maintains and contributes…"
- 原文（放置与优先级）："If you put your README file in your repository's hidden `.github`, root, or `docs` directory, GitHub will recognize and automatically surface your README… the file shown is chosen from locations in the following order: the `.github` directory, then the repository's root directory, and finally the `docs` directory."
- 原文（边界侧面）："A README should only contain information necessary for developers to get started using and contributing to your project. Longer documentation is best suited for wikis."（=README 管边界、长文外置）
- **注意**：该官方页只讲仓库级 README（.github/根/docs 三处），**未把"任意子目录 README 渲染"写成正式特性**。

### 2. 目录级 README：事实特性，非 docs.github.com 正式条目（A/B）
- Google 官方风格指南（A）：https://google.github.io/styleguide/docguide/READMEs.md
  - "A README is a short summary of the contents of a directory. The contents of the file are displayed in GitHub and Gitiles when you view the contents of the containing directory."
  - "All top-level directories for a code package should have an up-to-date `README.md` file."（=每包目录一个 README 的成文规范）
  - 内容规范："Every package-level `README.md` should include or point to: 1. What is in this package or library and what's it used for. 2. Points of contact. 3. Status… 5. Links to relevant documentation."（=边界一句话＋指路，正是"边界＋索引"二合一的权威范本）
  - 命名："README files must be named `README.md`… case sensitive."
- Stack Overflow 高赞答复（B）：https://stackoverflow.com/questions/19020891/ — "GitHub already has this feature. Just put your README file in a subdirectory, and it will be displayed just like one in the root directory."
- 定性：GitHub 行为稳定存在多年、被 Google 官方指南引用，但 docs.github.com 无专页 → **事实特性（de facto feature），非文档化承诺**。

### 3. README 应含 scope/boundary 的依据（B/C）
- Google 风格指南第 2 条"Status: deprecated / not for general release"即边界声明（A，同上）。
- openresource.dev（C）："A 'Non-goals' section in your README does the same job in five lines."；引 mio 仓库 README 实例含 `## Non-goals` 节。
- omniwebkit（C）："Should the README mention what the project is NOT? For anything in a crowded space, yes."
- gruv.ai（C）："Start by structuring your README in execution order: purpose and boundaries first…"（商业博客，等级低）
- **未找到** GitHub/GitLab 官方文档明文要求 README 写"不是什么"；此点最强依据是 Google 指南的 Status 条＋社区惯例。

### 4. INDEX.md 生态（B/C）
- GitHub **不**渲染目录级 INDEX.md：GitHub Community 讨论 #34789（B）中官方答复只提 README/index.md 作为 Pages 默认页，无 INDEX.md 特殊处理；未找到任何官方来源称 GitHub 渲染 INDEX.md。
- skissue `docs/index-format.md`（B，agent 导航规范范本）："Every directory in the repo with 2 or more children must contain an INDEX.md. This file serves as the directory's table of contents, enabling agents to navigate the codebase via progressive disclosure." URL: https://github.com/midyan/skissue/blob/main/docs/index-format.md — 注意其 INDEX.md 是**纯索引**（title＋一句 purpose＋Contents 表），边界只有一行。
- llm-wiki 模式（C）：mpashka 帖："every meaningful directory gets an index.md… short. It describes the files and subdirectories nearby… tells an agent what to read before changing that part."（Karpathy llm-wiki 思路）
- rust-analyzer/zed 用 INDEX.md：**未证实**（rust-lang/rust 的 src/INDEX.md 现 404；未找到两仓 INDEX.md 的可靠路径证据）。
- 附带：GitHub 自家 docs 仓库 content/ 每目录用 `index.md`＋frontmatter `children` 列表作落地页（B，经 mintlify 镜像 https://mintlify.wiki/github/docs/site-architecture 转述，非一手）。

### 5. 静态站点生成器的 index 机制（A）——"目录索引文件"的工业化先例
- MkDocs（A）https://www.mkdocs.org/user-guide/writing-your-docs/ ：
  - "MkDocs will allow you to name your index pages as `README.md` instead of `index.md`… when MkDocs renders your site, the file will be renamed to `index.html`."
  - "If both an `index.md` file and a `README.md` file are found in the same directory, then the `index.md` file is used and the `README.md` file is ignored."
- Docusaurus（A）https://docusaurus.io/docs/sidebar/autogenerated ：
  - "A category index document is a document following one of those filename conventions: Named as `index`… Named as `README`… Same name as parent folder."
  - 官方 tips 直接回答本题："Naming your introductory document `README.md` makes it show up when browsing the folder using the GitHub interface, while using `index.md` makes the behavior more in line with how HTML files are served."
- Hugo（A）https://gohugo.io/content-management/organization/ ："`_index.md` has a special role in Hugo. It allows you to add front matter and content to `home`, `section`, `taxonomy`, and `term` pages."
- 三家均不识别 `INDEX.md`（大写）为特殊文件。

### 6. Diátaxis 对索引/导航的说法（A，间接）
- URL: https://diataxis.fr/reference/（diataxis.fr 无独立 navigation 章节，/navigation/ 404）
- "the structure of the documentation should mirror the structure of the product"（目录结构镜像产品结构→目录级索引页与产品结构同构，符合"一级子包根＝索引"）
- "Reference material is useful when it is consistent. Standard patterns are what allow us to use reference material effectively."（索引页应标准化、同构）
- Diátaxis 未直接规定"索引页与解释内容是否同页"；其"不要混写（mixed-up）"原则针对四大类内容，索引/导航不在四象限内。**查无"索引页不得含边界说明"的明文**；reference 章的" austere / describe only"精神倾向索引页薄写。

### 7. 反方声音（B/C）
- thekarel best practices（B）："By default, I'd avoid adding separate READMEs to the individual workspace modules."＋"Write as little as possible… The less you write, the less will become obsolete tomorrow."——明确反对每模块一个 README、主张 README 极简。
- README rot 讨论（C）：datadef.io/guides/en/readme-rot（"A README is the most-read document in a repository and usually the least maintained"；腐烂顺序：setup→badges→截图→架构节）；paelladoc.com/blog/living-documentation（"Docs rot because they're a second copy of the truth"）。→ 反对的是**README 里写易腐事实**，不是反对目录级 README 本身；对"边界写薄"是支持论据。
- **未找到**权威来源系统性反对"每目录一个 README"作为反模式（Google 指南立场恰好相反）。

## 对比表：README.md vs INDEX.md 作子包根文件

| 维度 | README.md | INDEX.md |
|---|---|---|
| GitHub 仓库浏览渲染 | ✅ 目录级自动渲染（事实特性，Google 指南确认） | ❌ 普通文件，不渲染 |
| GitHub 仓库根渲染 | ✅ 官方特性（.github/根/docs） | ❌ |
| MkDocs | ✅ 可替代 index.md，构建为 index.html | ❌ 不识别 |
| Docusaurus | ✅ category index 三惯例之一 | ❌ 不识别 |
| Hugo | ➖ 认 `_index.md`（README 需 alias） | ❌ 不识别 |
| 语义惯例 | "面向人的门面/入口"，Google 定义＝目录摘要 | 无统一惯例；agent 导航圈（skissue/llm-wiki）新兴用法 |
| 机检可行性 | 高（名字固定，可查"每子包恰一个"） | 同样高，且因无宿主渲染副作用，纯机读语义更干净 |
| 冲突风险 | 与 MkDocs 同目录 index.md 共存时被忽略 | 与站点生成器无冲突 |

## 查不到的清单
1. docs.github.com 上关于"子目录 README 渲染"的正式文档页——不存在（只有仓库级 README 页）。
2. GitHub 官方对 INDEX.md 的任何特殊处理说明——不存在。
3. rust-analyzer / zed 仓库使用 INDEX.md 的一手路径证据——未找到（rust-lang/rust src/INDEX.md 已 404）。
4. Diátaxis 关于"索引页与解释性内容是否同页"的明文——无此章节（/navigation/ 404）。
5. GitHub/GitLab 官方"README 应写 non-goals/boundary"的明文——无；最强为 Google 指南 Status 条＋社区实践。
6. 权威（官方/大厂）系统性反对"每目录一个 README"的成文观点——未找到，仅个人经验帖（thkarel）。
