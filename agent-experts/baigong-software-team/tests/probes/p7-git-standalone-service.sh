#!/usr/bin/env bash
# P7 git 独立服务可建性（架构设计 v2.9 §10 L196 词条原句摘录·SWB-T01 T01-A）
# 核验方式（票面钉死·§19「git 原生能力」行）：仅验可建性——本地建裸仓＋保护分支/拒非快进配置可达；
# 不验远端服务运维（属 §11 人类侧外置物）。
# 退出码约定：0＝探针完整跑完且产出合法状态行；非0＝探针执行失败。
set -u
EVID_DIR="${EVID_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/swb-t01-p7-XXXXXX")}"
OUT="$EVID_DIR/p7.out"
SCRATCH="$EVID_DIR/gitsvc"

{
  echo "P7 git 独立服务可建性 实测 $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  git --version
  mkdir -p "$SCRATCH"
  echo "--- ① 本地裸仓可建 ---"
  git init --bare -q "$SCRATCH/remote.git" && echo "bare-init=OK" || echo "bare-init=FAIL"
  echo "--- ② 工作仓推送/拉取闭环（file:// 协议＝独立服务最小形态）---"
  git init -q -b main "$SCRATCH/work"
  (
    cd "$SCRATCH/work"
    git -c user.email=probe@local -c user.name=probe commit -q --allow-empty -m t01-probe-base
    git remote remove origin 2>/dev/null
    git remote add origin "$SCRATCH/remote.git"
    git push -q -u origin main
  ) && echo "push-loop=OK" || echo "push-loop=FAIL"
  echo "--- ③ 拒非快进（non-fast-forward rejection）可达 ---"
  nf=FAIL
  (
    cd "$SCRATCH/work"
    git -c user.name=probe -c user.email=probe commit -q --allow-empty -m t01-probe-c2
    git push -q origin main
    git reset -q --hard HEAD~1
    git -c user.name=probe -c user.email=probe commit -q --allow-empty -m t01-probe-c2b
    git push -q origin main 2>/dev/null
    git reset -q --hard HEAD~1
    git -c user.name=probe -c user.email=probe commit -q --allow-empty -m t01-probe-diverge
    git push origin main 2>/dev/null
  )
  rc=$?
  if [ $rc -ne 0 ]; then nf=OK; fi
  echo "non-ff-rejection=$nf (push rc=$rc)"
  echo "--- ④ 保护分支配置可达（receive.denyNonFastforwards＋分支级拒绝样例）---"
  git -C "$SCRATCH/remote.git" config receive.denyNonFastforwards true && echo "denyNFF-config=OK"
  git -C "$SCRATCH/remote.git" config --get receive.denyNonFastforwards
  # 服务端钩子拒绝指定分支＝保护分支最小原生实现可达性
  printf '#!/bin/sh\nwhile read old new ref; do case "$ref" in refs/heads/main) echo "protected: $ref" >&2; exit 1;; esac; done\nexit 0\n' > "$SCRATCH/remote.git/hooks/pre-receive"
  chmod +x "$SCRATCH/remote.git/hooks/pre-receive"
  prot=FAIL
  (
    cd "$SCRATCH/work"
    git -c user.name=probe -c user.email=probe commit -q --allow-empty -m t01-probe-prot
    git push origin main 2>/dev/null
  )
  prc=$?
  [ $prc -ne 0 ] && prot=OK
  echo "pre-receive-branch-guard=$prot (push rc=$prc)"
  if git init --bare -q "$SCRATCH/remote2.git" 2>/dev/null && [ $nf = OK ]; then
    echo "VERDICT: pass"
  else
    echo "VERDICT: negative"
  fi
} > "$OUT" 2>&1
status=$(grep -o 'VERDICT: [a-z]*' "$OUT" | tail -1 | cut -d' ' -f2)
case "$status" in pass|negative|inconclusive) : ;; *) status=inconclusive ;; esac
cat "$OUT"
echo "STATUS: $status"
exit 0
