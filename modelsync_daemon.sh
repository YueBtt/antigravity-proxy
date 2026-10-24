#!/bin/sh
# ============================================================
# Antigravity 模型清单自动同步守护脚本
#   - 每 6 小时拉一次官方 fetchAvailableModels
#   - 发现 Argon（或任何新模型）立刻写入 models_auto.json
#   - 反代无需重启，刷新模型即生效
# 由 LaunchDaemon com.antigravity.modelsync 保活
# ============================================================

SYNC="/var/mobile/antigravity_proxy/model_sync.py"
LOG="/var/log/model_sync.log"
STATE="/var/mobile/antigravity_proxy/.argon_alerted"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] model-sync daemon started (pid $$)" >> "$LOG"

# 启动后先等 30 秒，避开开机高峰
sleep 30

while true; do
    OUT=$(python3 "$SYNC" 2>&1)
    echo "$OUT" >> "$LOG"

    # 若解锁了 Argon，且还没告警过，则留痕（只记一次）
    if echo "$OUT" | grep -q 'argon=\[.*\]'; then
        if [ ! -f "$STATE" ]; then
            touch "$STATE"
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] ★★★ Gemini 4 Argon 已解锁！可立即使用 ★★★" >> "$LOG"
        fi
    fi

    # 每 6 小时同步一次（21600 秒），分片 sleep 便于进程被杀时快速响应
    i=0
    while [ $i -lt 216 ]; do
        sleep 100
        i=$((i + 1))
    done
done
