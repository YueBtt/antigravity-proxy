# Antigravity Multi-Upstream Proxy · 天道宗门多上游网关 (iOS / Linux)

> 🚀 **专为 iOS 越狱（Dopamine Rootless）与 Linux 打造的端侧多上游高吞吐 AI 网关。**  
> 零第三方 pip 依赖，单文件原生 Python 3.8+ 架构，集成黑曜石修真命盘与 Liquid Glass 响应式监控看板。打通全球六大高价值上游生态，彻底实现 **各大专线上游各用各的专用 Key 与路径鉴权，物理级严格隔离**，全链路 1:1 原生纯血直通！

---

## 🌟 核心特性与架构升级

### 1. 🛡️ 六大上游 Key 与模型物理级严格隔离（2026 最新标准）
各上游各用各的专用 Key，各管各的模型池，彻底杜绝混用与跨界越权：
- **专线一：Google Antigravity 专线 (`sk-antigravity`)**
  - **纯血原生模型**：独家接入官方最新 **Claude 5.5 High**（`claude-sonnet-5-5-high`、`claude-opus-5-5-high`）、Claude 4.6 深度思考（`claude-opus-4-6-thinking`、`claude-sonnet-4-6`）、Gemini 3.8 全系全档位、Gemini 3.7、`gemini-3.1-flash-image` 原生生图等。
  - **纯血直传**：彻底铲除任何偷梁换柱与降级逻辑（请求什么模型 1:1 直送上游，绝无李鬼换李逵）。
  - **智能端点路由**：5-5 系列全自动命中 Google 生产高可用节点，自动注入 `skip_thought_signature_validator` 绕过校验。
  - **权限边界**：`/v1/models` 仅吐出专属模型；携带该 Key 严禁调用外部模型（违规调用直接 403 拦截）。
- **专线二：EZComplete (Supabase Edge) 专线 (`sk-ezcomplete` / 路径 `/ez/v1`)**
  - **24 个 EZ 专线模型**：`gpt-4o-mini`、`gpt-6-sol`、`gpt-image-2.5-flare`、`flux-schnell` 等。
  - **看板折叠管理**：可收纳折叠账号池、动态弹窗录入、在线剔除与实时只读嗅探余额。
- **专线三：Meta Model API 专线 (`sk-meta` / 路径 `/meta/v1`)**
  - **8 个 Meta 官方模型**：`muse-spark-1.3`、`muse-image-1.0`（文生图）、`muse-voice-transcribe-1.0`、`sam-3.1` 等。
  - **设备码登录**：支持 OIDC 设备码无感刷新鉴权（真机 `muse_login.sh` 指令）。
- **专线四：Kilo Free 免费专线 (`sk-kilo` / 路径 `/kilo/v1`)**
  - **纯白嫖无门槛模型**：`nvidia-nemotron-70b`、`nemotron-550b` 等纯免费高算力推理。
- **专线五：Tencent CodeBuddy 腾讯专线 (`sk-tencent` / 路径 `/cb/v1`)**
  - **18 个腾讯全血大模型**：`deepseek-v4.1`、`deepseek-v4`、`glm-5.3`、`kimi-k3-1`、`hy4-preview` 等。
  - **出站强制 stream 处理**：原生完美兼容流式与非流式调用，多账号扫码入册。
- **专线六：Tencent LightVela 腾讯算力专线 (`sk-lightvela` / 路径 `/lv/v1`)**
  - **深度求索满血长推理版**：`deepseek-v4-pro-202606`、`auto` 等。
  - **沙盒算力直通**：每月白送 4500 算力积分，0 损耗直连满血 DeepSeek 推理。

### 2. ⚡ 起标题直接丢弃优化 (HTTP 204 No Content)
- 智能识别客户端后台静默触发的“给对话起标题”小请求；
- **0ms 秒级直接返回 HTTP 204** 并断开连接，彻底不发往上游，杜绝并发排队与卡顿！

### 3. ⚡ 纯血直连与蜂窝网络硬件优化
- **拒绝隐式降级**：彻底清空自动模糊映射，杜绝李鬼模型替代，给开发者最原汁原味的返回。
- **蜂窝网络高可用**：自研 `CellularSafeHTTPSConnection`，12s 快速握手 + 90s 流式长连接 + 16KB 分块写入，彻底根除移动网络与代理隧道下的 `The write operation timed out` 痛点。

### 4. 🛡️ iOS 系统级脱壳看门狗 (9 秒熔断自愈)
- 系统级 LaunchDaemon (`com.gemini.antigravity.proxy.plist`) 保活。
- 看门狗静默扫描：健康态自动固化 `healthy_bak` 镜像；若遭遇进程异常或语法崩溃，9 秒内自动触发回滚并物理重启，保证服务 7x24 小时坚如磐石。

---

## 🚀 支持模型与专线接入矩阵

| 上游专线 | 专属 API Key | 推荐 Base URL | 代表可用模型 (Model ID) |
| :--- | :--- | :--- | :--- |
| **Google Antigravity** | `sk-antigravity` | `http://127.0.0.1:8088/v1` | `claude-sonnet-5-5-high`<br>`claude-opus-5-5-high`<br>`claude-opus-4-6-thinking`<br>`claude-sonnet-4-6`<br>`gemini-3.8-flash-high`<br>`gemini-3.7-flash-high`<br>`gemini-3.1-flash-image` (原生生图) 等 |
| **EZComplete 专线** | `sk-ezcomplete` | `http://127.0.0.1:8088/ez/v1` | `gpt-4o-mini`<br>`gpt-6-sol`<br>`gpt-image-2.5-flare`<br>`flux-schnell` 等 24 个 |
| **Meta Model API** | `sk-meta` | `http://127.0.0.1:8088/meta/v1` | `muse-spark-1.3`<br>`muse-image-1.0`<br>`muse-voice-transcribe-1.0`<br>`sam-3.1` 等 8 个 |
| **Kilo Free 专线** | `sk-kilo` | `http://127.0.0.1:8088/kilo/v1` | `nemotron-550b`<br>`nvidia-nemotron-70b` 等免费模型 |
| **Tencent CodeBuddy** | `sk-tencent` | `http://127.0.0.1:8088/cb/v1` | `deepseek-v4.1`<br>`deepseek-v4`<br>`glm-5.3`<br>`kimi-k3-1`<br>`hy4-preview` 等 18 个 |
| **Tencent LightVela** | `sk-lightvela` | `http://127.0.0.1:8088/lv/v1` | `deepseek-v4-pro-202606`<br>`auto` 等 |

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
- **添加 Tencent CodeBuddy 服务商**：
  - Base URL: `http://127.0.0.1:8088/cb/v1`
  - API Key: `sk-tencent`
- **添加 Tencent LightVela 服务商**：
  - Base URL: `http://127.0.0.1:8088/lv/v1`
  - API Key: `sk-lightvela`
