/**
 * [task_local]
 * # 每 4 小时自动执行一次领币（0点、4点、8点、12点、16点、20点第5分钟）
 * 5 0,4,8,12,16,20 * * * ezcomplete_daily.js, tag=EZCompleteUI自动领币, img-url=https://raw.githubusercontent.com/crossutility/Quantumult-X/master/quantumult-x.png, enabled=true
 *
 * [rewrite_local]
 * # 抓取 Token 重写规则（双向监听：请求头与响应体）
 * ^https:\/\/spuoimtqofhbdzosrbng\.supabase\.co\/(functions\/v1\/|auth\/v1\/) url script-request-header ezcomplete_daily.js
 * ^https:\/\/spuoimtqofhbdzosrbng\.supabase\.co\/auth\/v1\/token url script-response-body ezcomplete_daily.js
 *
 * [mitm]
 * hostname = spuoimtqofhbdzosrbng.supabase.co
 */

const KEY_TOKEN = "ezcomplete_token";
const KEY_REFRESH_TOKEN = "ezcomplete_refresh_token";
const KEY_EMAIL = "ezcomplete_email";
const KEY_PASSWORD = "ezcomplete_password";
const SUPABASE_URL = "https://spuoimtqofhbdzosrbng.supabase.co";
const ANON_KEY = "sb_publishable_AzEVhLuIj1nSMwZvIgKw7A__Y3Ghdtl";

const isRequest = typeof $request !== "undefined";
const isResponse = typeof $response !== "undefined";

if (isResponse) {
    // 阶段 1B：监听登录/刷新响应体，自动提取并永久保存 refresh_token
    try {
        const body = JSON.parse($response.body);
        if (body.access_token) {
            $prefs.setValueForKey(body.access_token, KEY_TOKEN);
            console.log("[EZCompleteUI] 响应体捕获最新 Access Token 成功！");
        }
        if (body.refresh_token) {
            $prefs.setValueForKey(body.refresh_token, KEY_REFRESH_TOKEN);
            console.log("[EZCompleteUI] 响应体捕获长效 Refresh Token 成功！");
        }
    } catch (e) {}
    $done({});
} else if (isRequest) {
    // 监听 ez-chat 发出的真实请求 Body 格式并永久落盘
    if ($request.url.indexOf("/ez-chat") !== -1 && $request.body) {
        $prefs.setValueForKey($request.body, "ezcomplete_last_body");
    }

    // 阶段 1A：自动抓取请求头 Token
    const authHeader = $request.headers["Authorization"] || $request.headers["authorization"];
    if (authHeader && authHeader.startsWith("Bearer ") && authHeader !== `Bearer ${ANON_KEY}`) {
        const token = authHeader.replace("Bearer ", "").trim();
        const oldToken = $prefs.valueForKey(KEY_TOKEN);
        if (token !== oldToken) {
            $prefs.setValueForKey(token, KEY_TOKEN);
            console.log("[EZCompleteUI] 成功捕获并更新 Token: " + token.substring(0, 15) + "...");
            // 静默更新即可，不再弹窗骚扰用户！
        }
    }
    $done({});
} else {
    // 阶段 2：定时任务执行领币（自带 Token 过期检测、Refresh Token 换票与账号密码静默登录三重兜底）
    let token = $prefs.valueForKey(KEY_TOKEN);
    const refreshToken = $prefs.valueForKey(KEY_REFRESH_TOKEN);

    if (isTokenExpired(token)) {
        console.log("[EZCompleteUI] 检测到 Token 已失效，正在尝试自动静默刷新换票...");
        renewToken(refreshToken, (newToken) => {
            if (newToken) {
                claimDailyCoins(newToken);
            } else {
                // 如果 refresh_token 换票失败，使用账号密码直接向 Supabase 重新登录换取全新 Token
                loginWithPassword((loginToken) => {
                    if (loginToken) {
                        claimDailyCoins(loginToken);
                    } else if (token) {
                        claimDailyCoins(token);
                    } else {
                        console.log("[EZCompleteUI] 领币失败：无法获取有效 Token");
                        $notify("EZCompleteUI 领币失败", "无法获取有效 Token", "请检查网络或在手机上打开一次 EZCompleteUI App 重新激活！");
                        $done();
                    }
                });
            }
        });
    } else if (token) {
        claimDailyCoins(token);
    } else {
        loginWithPassword((loginToken) => {
            if (loginToken) {
                claimDailyCoins(loginToken);
            } else {
                console.log("[EZCompleteUI] 领币失败：未找到存储的用户 Token");
                $notify("EZCompleteUI 领币失败", "未找到用户 Token", "请先在手机上打开一次 EZCompleteUI App 自动抓取 Token！");
                $done();
            }
        });
    }
}

function loginWithPassword(callback) {
    const email = $prefs.valueForKey(KEY_EMAIL) || "1442285193@qq.com";
    const password = $prefs.valueForKey(KEY_PASSWORD) || "tT778899";
    if (!email || !password) {
        callback(null);
        return;
    }
    console.log("[EZCompleteUI] 正在使用账号密码静默向 Supabase 登录换票...");
    const loginUrl = `${SUPABASE_URL}/auth/v1/token?grant_type=password`;
    const opts = {
        url: loginUrl,
        method: "POST",
        headers: {
            "apikey": ANON_KEY,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email, password: password })
    };
    $task.fetch(opts).then(
        resp => {
            try {
                const b = JSON.parse(resp.body);
                if (b.access_token) {
                    $prefs.setValueForKey(b.access_token, KEY_TOKEN);
                    if (b.refresh_token) $prefs.setValueForKey(b.refresh_token, KEY_REFRESH_TOKEN);
                    console.log("[EZCompleteUI] 账号密码静默登录成功！全新 Token 已存入 QX 存储！");
                    callback(b.access_token);
                    return;
                }
            } catch (e) {}
            callback(null);
        },
        err => {
            console.log("[EZCompleteUI] 账号密码静默登录网络错误: " + err);
            callback(null);
        }
    );
}

function isTokenExpired(token) {
    if (!token) return true;
    try {
        const parts = token.split(".");
        if (parts.length < 2) return true;
        let base64 = parts[1].replace(/-/g, "+").replace(/_/g, "/");
        while (base64.length % 4) {
            base64 += "=";
        }
        // Base64 解码
        const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
        let output = "";
        for (let bc = 0, bs = 0, buffer, idx = 0; buffer = base64.charAt(idx++); ~buffer && (bs = bc % 4 ? bs * 64 + buffer : buffer, bc++ % 4) ? output += String.fromCharCode(255 & bs >> (-2 * bc & 6)) : 0) {
            buffer = chars.indexOf(buffer);
        }
        const json = JSON.parse(output);
        const exp = json.exp;
        const now = Math.floor(Date.now() / 1000);
        return exp - now < 120; // 提前 2 分钟视为过期
    } catch (e) {
        return false;
    }
}

function renewToken(refreshToken, callback) {
    const renewUrl = `${SUPABASE_URL}/auth/v1/token?grant_type=refresh_token`;
    const opts = {
        url: renewUrl,
        method: "POST",
        headers: {
            "apikey": ANON_KEY,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "refresh_token": refreshToken })
    };
    $task.fetch(opts).then(
        resp => {
            try {
                const b = JSON.parse(resp.body);
                if (b.access_token) {
                    $prefs.setValueForKey(b.access_token, KEY_TOKEN);
                    if (b.refresh_token) $prefs.setValueForKey(b.refresh_token, KEY_REFRESH_TOKEN);
                    console.log("[EZCompleteUI] QX 自动静默换票成功！");
                    callback(b.access_token);
                    return;
                }
            } catch (e) {}
            callback(null);
        },
        err => {
            console.log("[EZCompleteUI] 静默换票网络失败: " + err);
            callback(null);
        }
    );
}

function claimDailyCoins(userToken, isRetry) {
    console.log("[EZCompleteUI] 开始执行领币请求...");
    const claimUrl = `${SUPABASE_URL}/functions/v1/claim-daily-coins`;
    const options = {
        url: claimUrl,
        method: "POST",
        headers: {
            "apikey": ANON_KEY,
            "Authorization": `Bearer ${userToken}`,
            "Content-Type": "application/json",
            "User-Agent": "EZCompleteUI/7.1.4 (iPhone; iOS 16.0; Scale/3.00)"
        },
        body: "{}"
    };

    $task.fetch(options).then(
        resp => {
            console.log(`[EZCompleteUI] HTTP 响应码: ${resp.statusCode}`);
            console.log(`[EZCompleteUI] 响应原始 Body: ${resp.body}`);
            try {
                const body = JSON.parse(resp.body);
                if (resp.statusCode === 200 || resp.statusCode === 201) {
                    const added = body.coins_added || body.coins || "若干";
                    const balance = body.current_balance || body.balance || "未知";
                    const nextClaim = body.next_claim_at ? `下次可领: ${body.next_claim_at}` : "";
                    console.log(`[EZCompleteUI] 领币成功！到账: +${added}, 当前总余额: ${balance} ${nextClaim}`);
                    $notify("EZCompleteUI 领币成功", `💰 到账: +${added} Coins`, `当前总余额: ${balance}`);
                } else if (resp.statusCode === 401 && !isRetry) {
                    console.log("[EZCompleteUI] 收到 401 凭据失效，触发账号密码全自动重登换票并重试...");
                    loginWithPassword((newToken) => {
                        if (newToken) {
                            claimDailyCoins(newToken, true);
                        } else {
                            $notify("EZCompleteUI 领币失败", "Token 已过期且无法登录", "请检查密码或在 App 内重新登录！");
                            $done();
                        }
                    });
                    return;
                } else if (resp.statusCode === 400 || body.error || body.message) {
                    const msg = body.message || body.error || "冷却中或已领取";
                    console.log(`[EZCompleteUI] 未到领取时间/冷却中: ${msg}`);
                    $notify("EZCompleteUI 领币提示", "今日已领或未到时间", `${msg}`);
                } else {
                    console.log(`[EZCompleteUI] 接口异常返回: HTTP ${resp.statusCode}`);
                    $notify("EZCompleteUI 领币异常", `HTTP ${resp.statusCode}`, resp.body || "");
                }
            } catch (e) {
                console.log(`[EZCompleteUI] JSON 解析失败: ${e}`);
                $notify("EZCompleteUI 领币响应解析失败", `状态码: ${resp.statusCode}`, resp.body || "");
            }
            $done();
        },
        err => {
            const errStr = typeof err === "object" ? JSON.stringify(err) : String(err);
            console.log(`[EZCompleteUI] 请求错误: ${errStr}`);
            $notify("EZCompleteUI 领币网络请求错误", "无法连接 Supabase", errStr);
            $done();
        }
    );
}
