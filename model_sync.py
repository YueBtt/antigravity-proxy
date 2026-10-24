#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Antigravity 模型清单自动同步器
--------------------------------
权威来源：POST /v1internal:fetchAvailableModels （官方账号真实可用模型池）
作用：把官方最新放量的模型（含未来解锁的 gemini-4-argon 系列）自动落到
      /var/mobile/antigravity_proxy/models_auto.json，
      反代启动/刷新模型时会读取并合并，实现 Argon 一解锁立即可用。

用法：
  python3 model_sync.py            # 同步一次
  python3 model_sync.py --print    # 顺便打印结果
退出码：0 成功 / 1 失败
"""
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

PROXY_DIR = "/var/mobile/antigravity_proxy"
PROXY_PY = os.path.join(PROXY_DIR, "antigravity_proxy.py")
ACCOUNTS = os.path.join(PROXY_DIR, "accounts.json")
OUT = os.path.join(PROXY_DIR, "models_auto.json")
LOG = "/var/log/model_sync.log"
UA = "antigravity/2.24.0 darwin/arm64"

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def log(msg):
    line = "[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), msg)
    print(line, flush=True)
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def oauth_client():
    """从反代源码里抠出 OAuth 客户端 ID/Secret（bytes 混淆存储）。"""
    code = open(PROXY_PY, encoding="utf-8", errors="ignore").read()

    def grab(name):
        m = re.search(name + r"\s*=\s*bytes\(\[([0-9,\s]+)\]\)", code)
        if not m:
            raise RuntimeError("cannot find " + name)
        return bytes(int(x) for x in m.group(1).split(",")).decode()

    return grab("DEFAULT_CLIENT_ID"), grab("DEFAULT_CLIENT_SECRET")


def refresh_token(rt, cid, csec, tries=4):
    data = urllib.parse.urlencode({
        "client_id": cid, "client_secret": csec,
        "refresh_token": rt, "grant_type": "refresh_token",
    }).encode()
    for i in range(tries):
        try:
            req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
            with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
                return json.loads(r.read().decode()).get("access_token")
        except Exception as e:
            log("token refresh try %d failed: %s" % (i + 1, str(e)[:80]))
            time.sleep(4)
    return None


def probe_model(tok, model, ua=UA):
    """直接打一发 generateContent，返回 True 表示该模型对当前账号可用。"""
    body = {"model": model, "project": "default",
            "request": {"contents": [{"role": "user", "parts": [{"text": "hi"}]}],
                        "generationConfig": {"maxOutputTokens": 4}}}
    try:
        req = urllib.request.Request(
            "https://daily-cloudcode-pa.googleapis.com/v1internal:generateContent",
            data=json.dumps(body).encode(),
            headers={"Authorization": "Bearer " + tok,
                     "Content-Type": "application/json",
                     "User-Agent": ua}, method="POST")
        with urllib.request.urlopen(req, context=CTX, timeout=35) as r:
            return r.status == 200
    except Exception:
        return False


def fetch_available(tok, tries=3):
    """调用官方权威接口，拿账号真实可用模型池。"""
    last = None
    for ep in ("https://daily-cloudcode-pa.googleapis.com",
               "https://cloudcode-pa.googleapis.com"):
        for i in range(tries):
            try:
                req = urllib.request.Request(
                    ep + "/v1internal:fetchAvailableModels",
                    data=b"{}",
                    headers={"Authorization": "Bearer " + tok,
                             "Content-Type": "application/json",
                             "User-Agent": UA},
                    method="POST")
                with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
                    if r.status == 200:
                        return json.loads(r.read().decode())
            except Exception as e:
                last = e
                time.sleep(3)
    if last:
        log("fetchAvailableModels failed: %s" % str(last)[:120])
    return None


def main():
    try:
        cid, csec = oauth_client()
    except Exception as e:
        log("oauth_client error: %s" % e)
        return 1

    try:
        accts = json.load(open(ACCOUNTS, encoding="utf-8"))
    except Exception as e:
        log("read accounts error: %s" % e)
        return 1

    # 按 active 优先，逐个账号尝试
    accts_sorted = sorted(accts, key=lambda a: (not a.get("active"), a.get("email", "")))
    merged = {}
    used = []

    for a in accts_sorted:
        rt = a.get("refresh_token")
        if not rt:
            continue
        tok = refresh_token(rt, cid, csec)
        if not tok:
            continue
        data = fetch_available(tok)
        if not data:
            continue
        ms = data.get("models", {}) or {}
        if not ms:
            continue
        used.append(a.get("email"))
        for mid, info in ms.items():
            if mid.startswith("chat_"):      # 内部占位符，不可直呼
                continue
            if mid not in merged:
                merged[mid] = {
                    "apiProvider": info.get("apiProvider"),
                    "model": info.get("model"),
                    "maxTokens": info.get("maxTokens"),
                    "quota": (info.get("quotaInfo") or {}).get("remainingFraction"),
                }
        # 一个账号拿到就够了（同一 tier 池内容一致），但继续合并以防差异
        if len(used) >= 1 and len(merged) >= 20:
            break

    if not merged:
        log("no models fetched (all accounts failed)")
        return 1

    # ★ 主动探测 Argon：fetchAvailableModels 不一定列出灰度模型，
    #   直接打一发 generateContent 才知道账号是否真被放量。
    argon = sorted([m for m in merged if "argon" in m.lower()])
    tok_probe = None
    try:
        tok_probe = refresh_token(
            next((a["refresh_token"] for a in accts_sorted if a.get("refresh_token")), ""),
            cid, csec) if not tok_probe else tok_probe
    except Exception:
        tok_probe = None

    if tok_probe:
        for cand in ("gemini-4-argon", "gemini-4-argon-high",
                     "gemini-4-argon-low", "gemini-4-argon-medium"):
            if probe_model(tok_probe, cand):
                if cand not in argon:
                    argon.append(cand)
                merged[cand] = {"apiProvider": "API_PROVIDER_GOOGLE_GEMINI",
                                "model": cand, "maxTokens": 1048576, "quota": None}
                log("★★★ ARGON UNLOCKED: %s" % cand)
    argon = sorted(argon)
    payload = {
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "updated_ts": int(time.time()),
        "accounts_used": used,
        "count": len(merged),
        "argon_unlocked": argon,
        "models": merged,
    }
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
    os.replace(tmp, OUT)

    log("synced %d models (accounts=%s) argon=%s"
        % (len(merged), ",".join(used), argon if argon else "NONE"))

    if "--print" in sys.argv:
        for m in sorted(merged):
            mark = "  <<< ARGON!" if "argon" in m.lower() else ""
            print("  %-38s %s%s" % (m, merged[m].get("apiProvider"), mark))
    return 0


if __name__ == "__main__":
    sys.exit(main())
