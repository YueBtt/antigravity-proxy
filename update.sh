#!/bin/sh
# Antigravity Proxy 一键极速更新与热重载脚本

DIR="$(cd "$(dirname "$0")" && pwd)"
MAIN="$DIR/antigravity_proxy.py"
DOG="$DIR/watchdog.sh"

echo "🚀 开始从 GitHub 检查并拉取最新反代核心..."

# 1. 尝试直接通过 Git 更新（如果是 git 仓库）
if [ -d "$DIR/.git" ]; then
    git -C "$DIR" pull --rebase
else
    # 2. 否则走 Raw CDN 极速直灌下载
    curl -fsSL https://raw.githubusercontent.com/YueBtt/antigravity-proxy/main/antigravity_proxy.py -o "$MAIN.tmp"
    if [ $? -eq 0 ] && [ -s "$MAIN.tmp" ]; then
        python3 -m py_compile "$MAIN.tmp" > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            mv -f "$MAIN.tmp" "$MAIN"
            echo "✅ antigravity_proxy.py 更新完成并通过语法验证！"
        else
            echo "❌ 语法校验失败，放弃更新！"
            rm -f "$MAIN.tmp"
            exit 1
        fi
    fi

    # 同步更新看门狗
    curl -fsSL https://raw.githubusercontent.com/YueBtt/antigravity-proxy/main/watchdog.sh -o "$DOG.tmp"
    if [ $? -eq 0 ] && [ -s "$DOG.tmp" ]; then
        mv -f "$DOG.tmp" "$DOG"
        chmod +x "$DOG"
        echo "✅ watchdog.sh 看门狗更新完成！"
    fi
fi

# 3. 杀掉旧进程，由看门狗秒级无缝热拉起
echo "🔄 重启反代服务..."
killall -9 python3 python3.9 2>/dev/null
sleep 1

# 4. 健康检查
curl -s --connect-timeout 3 http://127.0.0.1:8088/api/stats > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "🎉 反代服务已满血复活，最新版本部署成功！"
else
    echo "⚠️ 正在等待看门狗拉起，请稍候访问 http://127.0.0.1:8088 验证！"
fi
