#!/bin/sh
# Meta Model API 设备码登录（Muse Code 同款 OIDC 流程，走本机 8088 反代管理端点）
# 用法: muse_login.sh          发起登录并等待批准
#       muse_login.sh status   只看当前授权状态
#       muse_login.sh models   列出上游三模型
BASE="http://127.0.0.1:8088"
PY=$(command -v python3 || echo /var/jb/usr/bin/python3)

jget() { "$PY" -c "import sys,json;d=json.load(sys.stdin);print(eval(\"d$1\"))" 2>/dev/null; }

case "$1" in
  status)
    curl -s "$BASE/meta/status" | "$PY" -m json.tool
    exit 0;;
  models)
    curl -s "$BASE/v1/models" | "$PY" -c "import sys,json;print('\n'.join(m['id'] for m in json.load(sys.stdin)['data'] if m.get('owned_by')=='meta-model-api'))"
    exit 0;;
esac

RESP=$(curl -s "$BASE/meta/login")
OK=$(printf '%s' "$RESP" | jget "['ok']")
if [ "$OK" != "True" ]; then
  echo "[X] 无法发起设备码登录："
  printf '%s\n' "$RESP"
  exit 1
fi
URI=$(printf '%s' "$RESP" | jget "['verification_uri']")
CODE=$(printf '%s' "$RESP" | jget "['user_code']")
LIFE=$(printf '%s' "$RESP" | jget "['expires_in']")
echo ""
echo "  用浏览器打开： $URI"
echo "  确认这个码：   $CODE"
echo "  （$LIFE 秒内有效，反代已在后台轮询）"
echo ""
printf "  等待批准"
i=0
while [ $i -lt "$LIFE" ]; do
  sleep 5
  i=$((i + 5))
  ST=$(curl -s "$BASE/meta/status")
  AUTH=$(printf '%s' "$ST" | jget "['authorized']")
  DS=$(printf '%s' "$ST" | jget "['device_flow']['state']")
  if [ "$AUTH" = "True" ]; then
    echo ""
    echo "  [OK] 授权成功，token 已写入 meta_token.txt"
    exit 0
  fi
  case "$DS" in
    denied) echo ""; echo "  [X] 用户拒绝了授权"; exit 1;;
    expired) echo ""; echo "  [X] 设备码过期，请重跑"; exit 1;;
  esac
  printf "."
done
echo ""
echo "  [X] 超时未批准"
exit 1
