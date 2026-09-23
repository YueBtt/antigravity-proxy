# Google Antigravity 原生反向代理与黑曜石看板 (iOS / Linux)

> 🚀 **专为 iPhone 越狱环境（iOS 16+ / Dopamine Rootless）与 Linux 打造的高性能 Google Antigravity & Daily CloudCode 内部协议反代服务。**  
> 完美的 OpenAI 协议中继桥梁，支持深度思考链（Reasoning / Thinking）、工具调用（Tool Calls / Function Calling）、多模态生图渲染、多账号无缝轮换容灾，以及 iOS 系统级脱壳保活守护。

---

## 🌟 核心特性与亮点

- **🔄 双向协议无缝转换**：全量兼容 OpenAI `/v1/chat/completions` 与 `/v1/models` 标准端点，所有支持 OpenAI 接口的客户端（如 Minis、NextChat、ChatBox、LobeChat、Cherry Studio 等）即插即用。
- **🧠 原生深度思考链（Thinking / Reasoning）**：打通 Google 上游 `thinkingBudget` 与 `includeThoughts` 参数，将思考过程以标准的 `reasoning_content` 流式块完整下发，思考细节分毫毕现。
- **🛠️ 智能函数与工具调用（Function Calling / Tools）**：内置自动注入 `skip_thought_signature_validator`，完美绕过 Google 上游对思考签名的严苛校验，工具链多轮调用稳如老狗。
- **🎨 多模态生图自动分流**：智能拦截生图模型（如 `gemini-3.1-flash-image`），自动剥离不兼容的 tools 声明，并把上游返回的图片 Base64 自动排版为 Markdown 格式秒级渲染。
- **💎 黑曜石毛玻璃 Web 仪表盘**：内置纯自研响应式 Web 看板（专为手机端 Safari 与桌面端优化），实时展示每日请求量、Token 吞吐、延迟分布、账号状态，支持扫码/点击一键绑定 Google OAuth 账号。
- **🛡️ 多账号池自动容灾与轮换**：支持挂载多个 Google 账号，遭遇 429（限流）或 403 异常时毫秒级自动切换可用账号重试，保障业务永不断流。
- **⚡ 独创脱壳看门狗（Unchained Watchdog）**：纯 Shell 极轻常驻进程，彻底摆脱 iOS LaunchDaemon 对后台守护进程 6MB 的 Jetsam 内存杀后台限制。

---

## 🚀 支持模型与映射列表

在任何 OpenAI 兼容客户端中，你可以直接请求以下模型：

| 模型代号（请求参数） | 上游真实 Antigravity 模型 | 核心能力与特性 |
| :--- | :--- | :--- |
| `gemini-3.7-flash-high` | `gemini-2.5-flash` / Antigravity Internal | 支持深度思维链思考、工具调用、高并发极速流式 |
| `gemini-3.8-flash-high` | `gemini-2.5-flash` / Antigravity Internal | 毫秒级极速响应、日常会话与自动化指令 |
| `gemini-pro-agent` | `gemini-2.5-pro` / Antigravity Internal | 复杂长文本逻辑推理、代码深度重构、工具链编排 |
| `claude-sonnet-4-6` | `claude-3-5-sonnet` (Antigravity 虚拟映射) | 超强代码与工程架构能力、高精准度格式输出 |
| `claude-opus-4-6-thinking` | `claude-3-opus` (Antigravity 虚拟映射) | 顶级思考链深度推理、长流程决策规划 |
| `gemini-3.1-flash-image` | Antigravity Multimodal Image Pipeline | 原生 AI 图像生成通道，直出高清图像 Markdown |

*注：反代内置智能模糊别名映射，传入 `gemini-3.7-flash`、`gemini-3.1-pro`、`claude-sonnet`、`imagen-3`、`dall-e-3` 等常用名称均会自动路由到最佳可用模型。*

---

## 📂 仓库项目结构

```text
├── antigravity_proxy.py           # 反代服务核心源码 & 黑曜石 Web 看板（零三方依赖）
├── watchdog.sh                    # 独立脱壳常驻看门狗脚本
├── com.gemini.antigravity.proxy.plist # iOS LaunchDaemon 系统级自启动配置文件
├── credentials.json.template      # 单账号 OAuth 凭据模板
├── accounts.json.template         # 多账号池配置模板
├── README.md                      # 中文项目完全指南
└── .gitignore                     # 敏感凭据防泄漏规则
```

---

## 🛠️ 快速上手与部署指南

### 1. 运行环境要求
- **Python 3.8+**（全部基于 Python 原生标准库开发，无需通过 pip 安装任何第三方依赖库，极度干净纯粹）
- **OpenSSL**（Python 内置 ssl 模块支持）

### 2. 本地直接运行
```bash
python3 antigravity_proxy.py
```
- 服务默认监听端口：`8088`。
- 打开浏览器访问：`http://localhost:8088`（或局域网 IP 如 `http://192.168.x.x:8088`）进入黑曜石管理看板。

### 3. 配置客户端接入（以 Minis / NextChat 为例）
- **接口地址 (Base URL)**: `http://127.0.0.1:8088/v1`
- **API 密钥 (API Key)**: 任意非空字符串（如 `sk-antigravity`）
- **模型名称 (Model)**: `gemini-3.7-flash-high` 或 `gemini-3.1-flash-image`

---

## 📱 iPhone 越狱环境常驻部署 (iOS 16+ Dopamine)

1. **部署源码到指定目录**：
   ```bash
   mkdir -p /var/mobile/antigravity_proxy
   cp antigravity_proxy.py watchdog.sh /var/mobile/antigravity_proxy/
   chmod +x /var/mobile/antigravity_proxy/watchdog.sh
   ```

2. **安装并激活 LaunchDaemon 系统守护**：
   ```bash
   cp com.gemini.antigravity.proxy.plist /var/jb/Library/LaunchDaemons/
   launchctl bootstrap system /var/jb/Library/LaunchDaemons/com.gemini.antigravity.proxy.plist
   ```
   *即使设备注销、桌面崩溃或重启，系统级看门狗都会在 3 秒内秒级自愈并拉起反代！*

---

## 🛡️ 安全规范说明

- 仓库内预置了严格的 `.gitignore` 规则，**严禁将真实的 `credentials.json`、`accounts.json`、`*.env` 等包含 Google OAuth Refresh Token 的凭据文件提交至公共版本库**。
- 部署时请基于提供的 `.template` 模板文件重命名并填入自己的配置。

---

## 📄 开源许可

本项目遵循 MIT 协议开源。仅供技术研究、内部测试与学习交流使用。
