# Antigravity Multi-Upstream Proxy · 黑曜石多上游网关 (iOS / Linux)

> 🚀 **专为 iOS 越狱（Dopamine Rootless）与 Linux 打造的端侧多上游高吞吐 AI 网关。**  
> 零第三方 pip 依赖，单文件原生 Python 3.8+ 架构，集成黑曜石修真命盘与 Liquid Glass 响应式监控看板。打通三大高价值上游生态，彻底实现 **三大上游各自用 Key 鉴权管理各自模型，物理级严格隔离**，全链路 1:1 原生纯血直通！

---

## 🌟 核心特性与架构升级

### 1. 🛡️ 三大上游 Key 与模型物理级严格隔离（2026 最新标准）
各上游各用各的专用 Key，各管各的模型池，彻底杜绝混用与跨界越权：
- **上游一：Google Antigravity 专线 (`sk-antigravity`)**
  - **31 个纯血原生模型**：独家接入官方最新 **Claude 5.5 High**（`claude-sonnet-5-5-high`、`claude-opus-5-5-high`）、Claude 4.6 深度思考（`claude-opus-4-6-thinking`、`claude-sonnet-4-6`）、Gemini 3.8 全系全档位、Gemini 3.7、Gemini 3.6、`gemini-3.1-flash-image` 原生生图等。
  - **纯血直传**：彻底铲除任何偷梁换柱与降级逻辑（请求什么模型 1:1 直送上游，绝无李鬼换李逵）。
  - **智能端点路由**：5-5 系列全自动命中 Google 生产高可用节点 `cloudcode-pa.googleapis.com`，其他模型按需自适应。
  - **权限边界**：`/v1/models` 仅吐出这 31 个模型；携带该 Key 严禁调用外部 EZ/Meta 模型（违规调用直接 403 拦截）。
- **上游二：EZComplete (Supabase Edge) 专线 (`sk-ezcomplete` / 路径 `/ez/v1`)**
  - **24 个 EZ 专线模型**：`gpt-4o-mini`、`gpt-6-sol`、`gpt-image-2.5-flare` 等。
  - **看板折叠管理**：可收纳折叠账号池、动态弹窗录入、在线剔除与实时只读嗅探余额。
  - **权限边界**：仅吐出 EZ 系列 24 个模型；严禁越权调用 Antigravity 或 Meta 模型（违规调用直接 403 拦截）。
- **上游三：Meta Model API 专线 (`sk-meta` / 路径 `/meta/v1`)**
  - **8 个 Meta 官方模型**：`muse-spark-1.3`、`muse-image-1.0`（文生图）、`muse-voice-transcribe-1.0`、`sam-3.1` 等。
  - **设备码登录**：支持 OIDC 设备码无感刷新鉴权（真机 `mlogin` 指令）。
  - **权限边界**：仅吐出 Meta 专属 8 个模型；严禁越权调用其他上游模型（违规调用直接 403 拦截）。

### 2. ⚡ 纯血直连与蜂窝网络硬件优化
- **拒绝隐式降级**：彻底清空自动模糊映射，杜绝李鬼模型替代，给开发者最原汁原味的返回。
- **蜂窝网络高可用**：自研 `CellularSafeHTTPSConnection`，12s 快速握手 + 90s 流式长连接 + 16KB 分块写入，彻底根除移动网络与代理隧道下的 `The write operation timed out` 痛点。

### 3. 🛡️ iOS 系统级脱壳看门狗 (9 秒熔断自愈)
- 系统级 LaunchDaemon (`com.gemini.antigravity.proxy.plist`) 保活。
- 看门狗静默扫描：健康态自动固化 `healthy_bak` 镜像；若遭遇进程异常或语法崩溃，9 秒内自动触发回滚并物理重启，保证服务 7x24 小时坚如磐石。

---

## 🚀 支持模型与专线接入矩阵

| 上游专线 | 专属 API Key | 推荐 Base URL | 代表可用模型 (Model ID) |
| :--- | :--- | :--- | :--- |
| **Google Antigravity** | `sk-antigravity` | `http://127.0.0.1:8088/v1` | `claude-sonnet-5-5-high`<br>`claude-opus-5-5-high`<br>`claude-opus-4-6-thinking`<br>`claude-sonnet-4-6`<br>`gemini-3.8-flash-high`<br>`gemini-3.7-flash-high`<br>`gemini-3.1-flash-image` (原生生图)<br>`gemini-pro-agent`<br>`gpt-oss-120b-medium` 等 31 个 |
| **EZComplete 专线** | `sk-ezcomplete` | `http://127.0.0.1:8088/ez/v1` | `gpt-4o-mini`<br>`gpt-6-sol`<br>`gpt-image-2.5-flare`<br>`dalle3_hd`<br>`flux-schnell` 等 24 个 |
| **Meta Model API** | `sk-meta` | `http://127.0.0.1:8088/meta/v1` | `muse-spark-1.3`<br>`muse-image-1.0`<br>`muse-voice-transcribe-1.0`<br>`sam-3.1` 等 8 个 |

---

## 🛠️ 快速启动与运维

### 1. 本地直接运行
```bash
# 零第三方库依赖，标准 Python 3.8+ 即可运行
python3 antigravity_proxy.py
```
- 控制台监听端口：`8088`
- 浏览器访问：`http://127.0.0.1:8088` 打开黑曜石修真监控仪表盘。

### 2. 客户端 (Minis / NextChat / Cherry Studio 等) 接入配置
- **添加 Antigravity 服务商**：
  - Base URL: `http://127.0.0.1:8088/v1`
  - API Key: `sk-antigravity`
- **添加 EZComplete 服务商**：
  - Base URL: `http://127.0.0.1:8088/ez/v1`
  - API Key: `sk-ezcomplete`
- **添加 Meta Model API 服务商**：
  - Base URL: `http://127.0.0.1:8088/meta/v1`
  - API Key: `sk-meta`

---

## 📱 iOS 越狱真机部署规范 (Dopamine Rootless)

1. **一键更新命令**（如已配置）：
   ```bash
   antigravity-update
   ```
2. **看门狗守护 Plist**：
   将 `com.gemini.antigravity.proxy.plist` 注入 `/var/jb/Library/LaunchDaemons/`，通过 launchctl 自启动并守护保活。
