# 2026-11-06 皮总拍板 · GWP 三拍面按建议放行＋两条跨项目新规则

- 开端实测 HEAD 读数＝`87b9acf`（登记开工 `git rev-parse --short HEAD`）。
- 呈报件＝`agent-experts/baigong-software-team/.collab/2026-11-06-GWP-呈拍简报-v1.md`（commit `ae2b13e`）。
- 被裁票面＝TK-GWP rev1（`agent-experts/baigong-software-team/.scratch/tickets/2026-11-06-GWP-guard-assembly-defects-ticket.md`，起草 `ea25d77`＋rev1 `7a98037`）。

## 一、GWP 三拍面＝全部按主理人建议拍板

1. **放行施工**：TK-GWP rev1 定稿放行。施工面＝hooks 运行链四脚本（`write-guard.py`／`lease-issuer.py`／`commit-audit.py`／`memory-neutralize.py`）；config／hooks.json／版本三同源＝禁动。
2. **守卫失效口径＝选项 A（fail-closed）**：守卫脚本未捕获异常→deny 输出＋留痕尽力＋exit 2（SystemExit 透传零扰动）。票内候裁⑩就此销账，PM 审票放行前置达成。
3. **版本排期＝选项 A**：GWP 批占 **0.1.30**（bump 随批部署段·三同源同步）；REMOTE-PUB 上架整改批顺延 **0.1.31**。
   - 0.0.1 台阶来历：REMOTE-PUB v1.2 §F 原预留 0.1.30＝上架前整改批（票面 L134–137·两次口径修正先例在册）；GWP 插队先占 0.1.30 后，上架整改批仍含自身整改内容（§B 六缺口）且版本须单调＋安装按版本寻址，故只能顺延 0.1.31＝远端上架版本比 GWP 部署后的本地预览多一档。并批同版方案（选项 B）未选。
4. **附候拍「基础设施修复票」票型＝按建议通过**：人类批准开场＋临时豁免域＋修后回归探针（P2-1 hooks 自卫死锁类将来启用）。

## 二、新增跨项目规则（皮总原话照录）

1. **代笔禁令例外条款＝派错席位写权移交**：「原则上谁写的文件谁修，除非一种情况就是主理人派错席位，这个也在实践中真实发生了，正确的席位必须可以接手对他席代笔的文件进行复核认可后接收认领，移交写权限。」
   - 操作化：唯一合法移交路径＝正确席位**复核→认可→接收认领→移交登记**；认领后该席成为新作者享续写权。除此路径，他席代笔仍违纪。
   - 本案触发实证＝GWP 票面两度派错席位（旧团席位型失败＋general-purpose 扮演架构席），后经 `software-team-architect` 席位重派合规成稿；本案无他席产物落盘，规则面向将来。
2. **主理人 memory 写权**：「主理人必须有权限写 memory。」memory 文件（工作区 `.workbuddy/memory/`、用户级 `MEMORY.md`）＝主理人合法写面，不在席位写权闭集（拍板㊻）交付面范围内。

## 三、执行路由

- 工程师席按 TK-GWP rev1 施工（票内候裁①–⑨按票面登记处置；候裁⑩已销）→ QA 席独立验证（fresh eyes）→ 部署段四段链＋bump `0.1.29 → 0.1.30`（三同源·回执附前后值实测 grep 读数）。
- REMOTE-PUB 票 §F 版本口径修正③（→0.1.31）＝作者席（arch-rpub1）续写——生产权随作者席，主理人只投递裁定。
