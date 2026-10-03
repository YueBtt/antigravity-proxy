#!/bin/sh
# 终极自愈看门狗：代码崩了自动回滚健康备份，绝不需要任何外部介入！

DIR="$(cd "$(dirname "$0")" && pwd)"
LOG="/var/log/antigravity_proxy.log"
ERR="/var/log/antigravity_proxy.err"
MAIN="$DIR/antigravity_proxy.py"
BAK="$DIR/antigravity_proxy.py.healthy_bak"

# 连续失败计数器
FAIL_COUNT=0

while true; do
    # 检查 8088 端口连通性
    /usr/bin/curl -s --connect-timeout 2 http://127.0.0.1:8088/api/stats > /dev/null 2>&1
    RET=$?
    
    if [ $RET -eq 0 ]; then
        # 只要当前运行正常且 8088 响应 200，立刻静默更新健康备份底座！
        FAIL_COUNT=0
        if [ -f "$MAIN" ]; then
            /usr/bin/python3 -m py_compile "$MAIN" > /dev/null 2>&1
            if [ $? -eq 0 ]; then
                cp -f "$MAIN" "$BAK"
            fi
        fi
    else
        # 异常挂掉或无法启动，开始救活
        FAIL_COUNT=$((FAIL_COUNT + 1))
        echo "$(date '+%Y-%m-%d %H:%M:%S') [Watchdog] 8088 DOWN (Fail count: $FAIL_COUNT)" >> "$LOG"

        # 如果连续失败超过 3 次（说明新改的代码有语法错误或死循环起不来），立刻自动强行回滚！
        if [ $FAIL_COUNT -ge 3 ]; then
            if [ -f "$BAK" ]; then
                echo "$(date '+%Y-%m-%d %H:%M:%S') [Watchdog] 🚨 AUTO-ROLLBACK TRIGGERED! Restoring from healthy_bak..." >> "$LOG"
                cp -f "$BAK" "$MAIN"
                FAIL_COUNT=0
            fi
        fi

        # 杀死残存进程并尝试拉起
        /usr/bin/killall -9 python3.9 python3 > /dev/null 2>&1
        sleep 1
        nohup /usr/bin/python3 "$MAIN" >> "$LOG" 2>> "$ERR" &
        echo "$(date '+%Y-%m-%d %H:%M:%S') [Watchdog] Proxy revived with PID $!" >> "$LOG"
    fi
    sleep 3
done
