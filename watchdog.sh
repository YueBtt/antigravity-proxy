#!/bin/sh
# Antigravity Proxy 独立守护看门狗 (脱壳保活架构)
# 作用: 作为超轻量 Shell 常驻，监控 Python 反代，彻底脱离 launchd 的内存锁链

DIR="$(cd "$(dirname "$0")" && pwd)"
LOG="/var/log/antigravity_proxy.log"
ERR="/var/log/antigravity_proxy.err"

while true; do
    # 检查 8088 端口连通性
    /usr/bin/curl -s --connect-timeout 2 http://127.0.0.1:8088/api/stats > /dev/null 2>&1
    RET=$?
    if [ $RET -ne 0 ]; then
        # 异常挂掉或端口未通，强制清理并释放端口
        /usr/bin/killall -9 python3 > /dev/null 2>&1
        sleep 1
        # 后台无拘无束脱壳拉起
        nohup /usr/bin/python3 "$DIR/antigravity_proxy.py" >> "$LOG" 2>> "$ERR" &
        echo "$(date '+%Y-%m-%d %H:%M:%S') [Watchdog] Proxy revived with PID $!" >> "$LOG"
    fi
    sleep 3
done
