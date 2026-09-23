# Google Antigravity Proxy (iOS / Linux)

> High-performance OAuth Reverse Proxy & Obsidian Glass Dashboard for Google Antigravity & Daily CloudCode Internal API.
> Seamlessly bridges OpenAI API format with Google Antigravity Internal Protocol, supporting Deep Thinking (Reasoning), Tool Calls (Function Calling), Multimodal Image Generation, Multi-Account Pooling, and System-Level Daemon Watchdogs.

---

## 🌟 Key Features

- **OpenAI ↔ Antigravity Protocol Bridge**: Full compatibility with `/v1/chat/completions` and `/v1/models`.
- **Deep Thinking & Reasoning Output**: Native support for Google's `thinkingBudget` and `includeThoughts`, streaming thought chains in standard `reasoning_content` chunks.
- **Tools & Function Calling**: Automatic injection of `skip_thought_signature_validator` to bypass upstream thought signature restrictions.
- **Multimodal Image Generation**: Automatically intercepts image generation models (e.g. `gemini-3.1-flash-image`), strips incompatible tool schemas, and formats returned images into clean Markdown.
- **Obsidian Glass Web Dashboard**: Built-in responsive web dashboard (iOS Safari & desktop optimized) with real-time stats, latency, quota tracking, and multi-account OAuth management.
- **Multi-Account Failover Pool**: Automatic account rotation with 429/403 rate-limit backoff.
- **Unchained Watchdog Daemon**: Zero-dependency detached watchdog process designed to survive iOS Jetsam / LaunchDaemon memory limits.

---

## 🚀 Supported Models

| Model Alias | Upstream Antigravity Target | Capabilities |
| :--- | :--- | :--- |
| `gemini-3.7-flash-high` | `gemini-2.5-flash` / Antigravity Internal | Thinking, Tools, Streaming |
| `gemini-3.8-flash-high` | `gemini-2.5-flash` / Antigravity Internal | Fast Inference, Tools |
| `gemini-pro-agent` | `gemini-2.5-pro` / Antigravity Internal | Complex Reasoning, Tools |
| `claude-sonnet-4-6` | `claude-3-5-sonnet` (Antigravity Virtual Mapping) | Full Reasoning, Coding |
| `claude-opus-4-6-thinking`| `claude-3-opus` (Antigravity Virtual Mapping) | Deep Thinking Chains |
| `gemini-3.1-flash-image` | Antigravity Multimodal Image Pipeline | Native Image Generation |

---

## 🛠️ Architecture & Files

```text
├── antigravity_proxy.py           # Core proxy service & Web dashboard
├── watchdog.sh                    # Detached watchdog daemon
├── com.gemini.antigravity.proxy.plist # iOS LaunchDaemon plist
├── credentials.json.template      # OAuth credentials template
├── accounts.json.template         # Multi-account configuration template
├── README.md                      # Documentation
└── .gitignore                     # Sensitive data exclusion rules
```

---

## 📦 Quick Start

### 1. Requirements
- Python 3.8+ (Standard Library only — zero 3rd-party dependencies required!)
- OpenSSL (Built into Python `ssl` module)

### 2. Launching Service
```bash
python3 antigravity_proxy.py
```
Default port: `8088`. Open `http://localhost:8088` in your browser to access the Obsidian Glass Dashboard.

### 3. Using with OpenAI-Compatible Clients
- **Base URL**: `http://127.0.0.1:8088/v1`
- **API Key**: Any string (e.g. `sk-antigravity`)
- **Model**: `gemini-3.7-flash-high` / `gemini-3.1-flash-image`

---

## 🛡️ License

MIT License. Designed for research and private experimentation.
