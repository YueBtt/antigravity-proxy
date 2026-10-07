# Antigravity Multi-Upstream Proxy · 黑曜石网关 (iOS / Linux)

> 🚀 **专为 iOS 越狱（Dopamine Rootless）与 Linux 打造的端侧多上游大模型聚合网关。**  
> 零第三方 pip 依赖，单文件原生 Python 实现，集成修真主题 Liquid Glass 响应式看板，打通三大高价值上游，无缝输出标准 OpenAI API。

---

## 🌟 核心特性与架构亮点

### 1. 三上游物理隔离与智能路由
- **上游一：Google Antigravity (Daily CloudCode)**
  - 核心接入：Google 内部协议 ↔ OpenAI 双向转换，支持思维链推理（`reasoning_content`）流式透传。
  - 协议优化：自动注入 `skip_thought_signature_validator`，规避 Google 上游工具调用签名风控。
  - 多账号容灾：内置 Multi-Account 轮询池与权重调度，遇 429 毫秒级静默切号。
- **上游二：EZCompleteUI (Supabase Edge Gateway)**
  - 路由挂载点：`/ez/v1/chat/completions`、`/ez/v1/models`、`/ez/v1/balance`。
  - 独立账号池：多账号负载均衡矩阵，支持 Coin 余额实时只读嗅探与 0 损耗验票。
  - **最新看板能力**：
    - 📁 **可收纳折叠**：默认折叠账号列表，展示矩阵总额度与总账号数，避免卡片过长刷屏。
    - ➕ **动态录入弹窗**：支持通过 Web 弹窗一键录入账号密码，底层自动发起 Supabase 鉴权并热加载入池。
    - 🗑️ **在线剔除管理**：列表直接支持废号剔除与状态监控。
- **上游三：Meta Model API (api.meta.ai)**
  - 挂载官方 Muse 家族（`muse-spark-1.3`、`muse-image-1.0` 等）及 SAM 3.1 视觉分割接口。
  - 支持 OIDC 设备码登录机制（真机 `mlogin` 助手）。

### 2. 蜂窝网络自适应与高可用传输
- 自研 `CellularSafeHTTPSConnection`：12s 快速握手 + 90s 流式长连接 + 16KB 分块写入，彻底解决移动蜂窝网络或 VLESS/WSS 隧道上传大包时抛出 `The write operation timed out` 的顽疾。

### 3. iOS 系统级脱壳看门狗 (9秒熔断自愈)
- 系统级 LaunchDaemon 保活守护。
- 看门狗静默扫描：健康态自动更新 `healthy_bak` 镜像；若遭遇进程异常或语法崩溃，9 秒内自动触发回滚并物理重启，保证服务 7x24 小时不掉线。

---

## 🚀 支持模型与路由映射

客户端统一配置 Base URL 即可直接调用（支持 OpenAI SDK / NextChat / Cherry Studio / Minis）：

| 路由入口 | 模型代号 (Model ID) | 上游归属 | 核心特性 |
| :--- | :--- | :--- | :--- |
| `/v1` | `gemini-3.8-flash-high` | Google Antigravity | 最新一代满血架构，超高响应速度 |
| `/v1` | `gemini-3.7-flash-high` | Google Antigravity | 官方满血旗舰，超长思维链推理 + 工具调用 |
| `/v1` | `claude-sonnet-4-6` | Antigravity 宿主 | 顶级代码架构与长文本逆向分析 |
| `/v1` | `claude-opus-4-6-thinking` | Antigravity 宿主 | 究极脑力深度推理，带 Thinking 细节 |
| `/v1` | `gemini-3.1-flash-image` | Antigravity 生图 | 原生文生图通道，自动输出 Markdown 图片 |
| `/ez/v1` | `gpt-4o-mini` / `ez-chat` | EZComplete 专线 | 轻量高并发、稳定可用 |
| `/ez/v1` | `gpt-image-2.5-flare` | EZComplete 生图 | 极速生图与改图通道 |
| `/v1` | `muse-spark-1.3` | Meta Model API | 1M 上下文、多模态原生理解 |

---

## 🛠️ 快速启动与使用

### 1. 本地启动
```bash
# 零依赖，原生 Python 3.8+ 直接跑
python3 antigravity_proxy.py
```
- 控制台监听端口：`8088`
- 浏览器访问：`http://127.0.0.1:8088` 打开黑曜石 Liquid Glass 仪表盘

### 2. 客户端接入配置
- **上游一 / 全局入口**：
  - Base URL: `http://127.0.0.1:8088/v1`
  - API Key: `sk-antigravity`
- **上游二 (EZComplete) 专线**：
  - Base URL: `http://127.0.0.1:8088/ez/v1`
  - API Key: `sk-ezcomplete`

---

## 📱 iPhone 越狱常驻部署 (iOS 16+ / Dopamine)

1. **部署代码**：
   ```bash
   mkdir -p /var/mobile/antigravity_proxy
   cp antigravity_proxy.py watchdog.sh /var/mobile/antigravity_proxy/
   chmod +x /var/mobile/antigravity_proxy/watchdog.sh
   ```

2. **激活 LaunchDaemon 系统守护**：
   ```bash
   cp com.gemini.antigravity.proxy.plist /var/jb/Library/LaunchDaemons/
   launchctl bootstrap system /var/jb/Library/LaunchDaemons/com.gemini.antigravity.proxy.plist
   ```

---

## 📂 仓库结构说明

```text
├── antigravity_proxy.py               # 核心源码：双向代理 + 三上游路由 + Liquid Glass 看板
├── watchdog.sh                        # 9秒熔断自愈与健康看门狗
├── com.gemini.antigravity.proxy.plist # iOS LaunchDaemon 保活配置
├── credentials.json.template          # Google OAuth 单账号模板
├── accounts.json.template             # Google 多账号池配置模板
├── ez_accounts.json.template          # EZComplete 账号矩阵模板
├── README.md                          # 项目工程文档
└── .gitignore                         # 严格凭据脱敏防泄露规则
```

---

## 🛡️ 安全规范说明

- 仓库严格配置了 `.gitignore`，严禁提交任何真实的 `credentials.json`、`accounts.json`、`ez_accounts.json`、`ez_token_*.txt` 等凭据。
- 部署新环境请使用提供的 `.template` 模板重命名并填写账号信息，或直接通过面板 Web 弹窗在线录入。
