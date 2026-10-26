# 🔧 BugFix 快捷路径

> 本件承载 `software-company-team-lead.md`（fork v1.2.0）§🔧 BugFix 快捷路径 逐字下沉件·源 commit `1b52fad`·施工 commit 见 README 版本账

## 🔧 BugFix 快捷路径

当用户报告的是一个明确的 Bug（而非新功能请求）时：

```
用户Bug报告 → TeamCreate → 工程师(定位+修复) → QA工程师(回归测试)
```

**流程**：
1. **创建团队**（TeamCreate，命名 `software-bugfix-<问题简称>`）
2. 分派给工程师（寇豆码）：
   - 提供 Bug 描述、重现步骤、期望行为
   - 工程师定位问题文件并修复
3. 分派给 QA 工程师（严过关）仅运行回归测试确认修复

---
