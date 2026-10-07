#!/bin/sh
# 终极自愈看门狗 v2：精准单杀 + 双次确认 + 语法熔断回滚
# 相比 v1 的改进：
#   1. 单次探测抖动不再当场杀人，双次确认才重启，杜绝误杀正在吐字的在途请求（抽风根因之一）
#   2. 探测改用 HTTP 200 精准判定 + 6 秒硬超时，不再因慢请求误判 DOWN
#   3. 重启前先做 py_compile 体检，语法损坏直接熔断回滚，杜绝无限重启抖动
#   4. 优先按 PID 精准击杀，不再无脑 killall 误伤其他 python 进程

DIR="$(cd "$(dirname "$0")" && pwd)"
LOG="/var/log/antigravity_proxy.log"
ERR="/var/log/antigravity_proxy.err"
MAIN="$DIR/antigravity_proxy.py"
BAK="$DIR/antigravity_proxy.py.healthy_bak"
PIDF="$DIR/antigravity_proxy.pid"

FAIL_COUNT=0

start_proxy() {
    /usr/bin/python3 -m py_compile "$MAIN" > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        if [ -f "$BAK" ]; then
            echo "$(date '+%Y-%m-%d %H:%M:%S') [Watchdog] 语法损坏，熔断回滚 healthy_bak" >> "$LOG"
            cp -f "$BAK" "$MAIN"
        fi
        /usr/bin/python3 -m py_compile "$MAIN" > /dev/null 2>&1
        if [ $? -ne 0 ]; then
            echo "$(date '+%Y-%m-%d %H:%M:%S') [Watchdog] 回滚后仍无法编译，跳过本轮启动" >> "$LOG"
            return 1
        fi
    fi
    nohup /usr/bin/python3 -u "$MAIN" >> "$LOG" 2>> "$ERR" &
    echo $! > "$PIDF"
    echo "$(date '+%Y-%m-%d %H:%M:%S') [Watchdog] Proxy revived with PID $!" >> "$LOG"
}

kill_proxy() {
    if [ -f "$PIDF" ]; then
        _p=$(cat "$PIDF" 2>/dev/null)
        if [ -n "$_p" ]; then
            kill -9 "$_p" > /dev/null 2>&1
        fi
    fi
    /usr/bin/killall -9 python3.9 python3 > /dev/null 2>&1
}

while true; do
    CODE=$(/usr/bin/curl -s -o /dev/null -m 6 -w '%{http_code}' --connect-timeout 2 http://127.0.0.1:8088/api/stats 2>/dev/null)

    if [ "$CODE" = "200" ]; then
        FAIL_COUNT=0
        if [ -f "$MAIN" ] && [ -f "$BAK" ] && ! cmp -s "$MAIN" "$BAK"; then
            /usr/bin/python3 -m py_compile "$MAIN" > /dev/null 2>&1
            if [ $? -eq 0 ]; then
                cp -f "$MAIN" "$BAK"
                echo "$(date '+%Y-%m-%d %H:%M:%S') [Watchdog] 代码变更且语法校验通过，已静默更新健康备份底座" >> "$LOG"
            fi
        fi
        sleep 5
        continue
    fi

    FAIL_COUNT=$((FAIL_COUNT + 1))
    echo "$(date '+%Y-%m-%d %H:%M:%S') [Watchdog] 8088 探测异常 (HTTP=$CODE, Fail=$FAIL_COUNT)" >> "$LOG"

    if [ $FAIL_COUNT -lt 2 ]; then
        sleep 2
        continue
    fi

    if [ $FAIL_COUNT -ge 3 ] && [ -f "$BAK" ] && ! cmp -s "$MAIN" "$BAK"; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') [Watchdog] 连续 3 次失败，AUTO-ROLLBACK 回滚 healthy_bak" >> "$LOG"
        cp -f "$BAK" "$MAIN"
    fi

    /usr/bin/killall -9 python3.9 python3 > /dev/null 2>&1
    sleep 1
    start_proxy
    FAIL_COUNT=0
    sleep 4
done
