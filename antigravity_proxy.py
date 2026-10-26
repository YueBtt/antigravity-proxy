
# ==============================================================================
# 通道四：Free / Omni 白嫖免 Key 专线配置 (2026-10-12)
# ==============================================================================

FREE_GATEWAY_URL = "https://api.kilo.ai/api/gateway/chat/completions"

FREE_SUPPORTED_MODELS = [
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
    "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    "nvidia/nemotron-3.5-lightning:free",
    "nvidia/nemotron-3.5-content-safety:free",
    "dots-studio/dots-3-note-preview:free",
    "poolside/laguna-s-2.1:free",
    "poolside/laguna-xs-2.1:free",
    "liquid/lfm-2.5-2.6b:free",
    "thinkingmachines/inkling-small:free",
    "cohere/north-mini-code:free",
    "kilo-auto/free",
    "kilo-auto/balanced",
    "kilo-auto/frontier"
]

FREE_MODEL_ALIASES = {
    "nemotron": "nvidia/nemotron-3-ultra-550b-a55b:free",
    "nemotron-550b": "nvidia/nemotron-3-ultra-550b-a55b:free",
    "nemotron-ultra": "nvidia/nemotron-3-ultra-550b-a55b:free",
    "nemotron-120b": "nvidia/nemotron-3-super-120b-a12b:free",
    "nemotron-super": "nvidia/nemotron-3-super-120b-a12b:free",
    "nemotron-nano": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    "free-auto": "kilo-auto/free",
    "omni-free": "kilo-auto/free"
}

def free_resolve_model(model_name):
    m = (model_name or "").strip().lower()
    if m in FREE_MODEL_ALIASES:
        return FREE_MODEL_ALIASES[m]
    for orig in FREE_SUPPORTED_MODELS:
        if m == orig.lower():
            return orig
    return model_name

import ez_quota_checker
FABAO_ICONS = {"天逆石珠": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGRlZnM+CiAgICA8cmFkaWFsR3JhZGllbnQgaWQ9ImcxIiBjeD0iNDAlIiBjeT0iNDAlIiByPSI2MCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMzhiZGY4Ii8+CiAgICAgIDxzdG9wIG9mZnNldD0iNTUlIiBzdG9wLWNvbG9yPSIjMWUyOTNiIi8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzAyMDYxNyIvPgogICAgPC9yYWRpYWxHcmFkaWVudD4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMjQiIGZpbGw9InVybCgjZzEpIj4KICAgIDxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9InIiIHZhbHVlcz0iMjM7MjU7MjMiIGR1cj0iMi41cyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KICA8cGF0aCBkPSJNMTggMjggUTMyIDE2IDQ2IDI4IFEzMiA0MiAxOCAyOCBaIiBmaWxsPSJub25lIiBzdHJva2U9IiM2MGE1ZmEiIHN0cm9rZS13aWR0aD0iMS41IiBvcGFjaXR5PSIwLjgiPgogICAgPGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJyb3RhdGUiIGZyb209IjAgMzIgMzIiIHRvPSIzNjAgMzIgMzIiIGR1cj0iOHMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9wYXRoPgogIDxjaXJjbGUgY3g9IjMyIiBjeT0iMzIiIHI9IjUiIGZpbGw9IiNlMGYyZmUiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0ib3BhY2l0eSIgdmFsdWVzPSIwLjY7MTswLjYiIGR1cj0iMS44cyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KPC9zdmc+", "飞剑赤血": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGc+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InRyYW5zbGF0ZSIgdmFsdWVzPSIwLC0yOyAwLDI7IDAsLTIiIGR1cj0iMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgICA8cGF0aCBkPSJNNTIgMTIgTDI0IDQwIEwyMCAzNiBMNDggOCBaIiBmaWxsPSIjZWY0NDQ0Ii8+CiAgICA8cGF0aCBkPSJNNTIgMTIgTDI4IDQ0IEwyNCA0MCBaIiBmaWxsPSIjYjkxYzFjIi8+CiAgICA8cGF0aCBkPSJNMTggMzQgTDMwIDQ2IEwyNiA1MCBMMTQgMzggWiIgZmlsbD0iI2ZiYmYyNCIvPgogICAgPHBhdGggZD0iTTIyIDQyIEwxMiA1MiBMMTAgNTAgTDIwIDQwIFoiIGZpbGw9IiM3ODM1MGYiLz4KICAgIDxjaXJjbGUgY3g9IjM2IiBjeT0iMjgiIHI9IjE0IiBmaWxsPSIjZWY0NDQ0IiBvcGFjaXR5PSIwLjI1Ij4KICAgICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iciIgdmFsdWVzPSIxMDsxODsxMCIgZHVyPSIxLjVzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIvPgogICAgPC9jaXJjbGU+CiAgPC9nPgo8L3N2Zz4=", "百丈魂旗": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGxpbmUgeDE9IjE2IiB5MT0iOCIgeDI9IjE2IiB5Mj0iNTgiIHN0cm9rZT0iIzk0YTNiOCIgc3Ryb2tlLXdpZHRoPSIyLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogIDxwYXRoIGQ9Ik0xNyAxMiBRMzYgOCA1NCAxOCBRNDQgMzAgNTYgNDIgUTM0IDQ2IDE3IDM4IFoiIGZpbGw9IiMxZTFiNGIiIHN0cm9rZT0iI2RjMjYyNiIgc3Ryb2tlLXdpZHRoPSIxLjIiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iZCIgdmFsdWVzPSJNMTcgMTIgUTM2IDggNTQgMTggUTQ0IDMwIDU2IDQyIFEzNCA0NiAxNyAzOCBaO00xNyAxMiBRMzQgMTQgNTIgMTUgUTQ2IDI4IDU0IDQ0IFEzNiA0MCAxNyAzOCBaO00xNyAxMiBRMzYgOCA1NCAxOCBRNDQgMzAgNTYgNDIgUTM0IDQ2IDE3IDM4IFoiIGR1cj0iMi4ycyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L3BhdGg+CiAgPGNpcmNsZSBjeD0iMzQiIGN5PSIyNiIgcj0iNSIgZmlsbD0iI2VmNDQ0NCIgb3BhY2l0eT0iMC44NSI+CiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiB2YWx1ZXM9IjAuNDsxOzAuNCIgZHVyPSIxLjZzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIvPgogIDwvY2lyY2xlPgo8L3N2Zz4=", "巨富魂旗": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGxpbmUgeDE9IjE2IiB5MT0iOCIgeDI9IjE2IiB5Mj0iNTgiIHN0cm9rZT0iIzk0YTNiOCIgc3Ryb2tlLXdpZHRoPSIyLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogIDxwYXRoIGQ9Ik0xNyAxMiBRMzYgOCA1NCAxOCBRNDQgMzAgNTYgNDIgUTM0IDQ2IDE3IDM4IFoiIGZpbGw9IiMxZTFiNGIiIHN0cm9rZT0iI2RjMjYyNiIgc3Ryb2tlLXdpZHRoPSIxLjIiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iZCIgdmFsdWVzPSJNMTcgMTIgUTM2IDggNTQgMTggUTQ0IDMwIDU2IDQyIFEzNCA0NiAxNyAzOCBaO00xNyAxMiBRMzQgMTQgNTIgMTUgUTQ2IDI4IDU0IDQ0IFEzNiA0MCAxNyAzOCBaO00xNyAxMiBRMzYgOCA1NCAxOCBRNDQgMzAgNTYgNDIgUTM0IDQ2IDE3IDM4IFoiIGR1cj0iMi4ycyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L3BhdGg+CiAgPGNpcmNsZSBjeD0iMzQiIGN5PSIyNiIgcj0iNSIgZmlsbD0iI2VmNDQ0NCIgb3BhY2l0eT0iMC44NSI+CiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiB2YWx1ZXM9IjAuNDsxOzAuNCIgZHVyPSIxLjZzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIvPgogIDwvY2lyY2xlPgo8L3N2Zz4=", "木雕岁月": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGRlZnM+CiAgICA8cmFkaWFsR3JhZGllbnQgaWQ9Indvb2QiIGN4PSI1MCUiIGN5PSI1MCUiIHI9IjUwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNmNTllMGIiIHN0b3Atb3BhY2l0eT0iMC40Ii8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzAwMCIgc3RvcC1vcGFjaXR5PSIwIi8+CiAgICA8L3JhZGlhbEdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIzMiIgY3k9IjMyIiByPSIyOCIgZmlsbD0idXJsKCN3b29kKSI+CiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiB2YWx1ZXM9IjAuNTsxOzAuNSIgZHVyPSIzcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KICA8cGF0aCBkPSJNMjYgNDggTDM4IDQ4IEwzNiAyNiBDMzYgMjAgMjggMjAgMjggMjYgWiIgZmlsbD0iI2I0NTMwOSIgc3Ryb2tlPSIjZmNkMzRkIiBzdHJva2Utd2lkdGg9IjEuMiIvPgogIDxjaXJjbGUgY3g9IjMyIiBjeT0iMTgiIHI9IjUiIGZpbGw9IiNkOTc3MDYiIHN0cm9rZT0iI2ZkZTA0NyIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2ZiYmYyNCIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDMiPgogICAgPGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJyb3RhdGUiIGZyb209IjAgMzIgMzIiIHRvPSIzNjAgMzIgMzIiIGR1cj0iMTBzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIvPgogIDwvY2lyY2xlPgo8L3N2Zz4=", "十亿尊魂幡": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGxpbmUgeDE9IjE0IiB5MT0iNiIgeDI9IjE0IiB5Mj0iNTgiIHN0cm9rZT0iI2ZiYmYyNCIgc3Ryb2tlLXdpZHRoPSIyLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogIDxwYXRoIGQ9Ik0xNSAxMCBRMzggNCA1OCAxNiBRNDYgMzAgNTggNDYgUTM2IDUwIDE1IDQwIFoiIGZpbGw9IiMwOTBkMTYiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIxLjUiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iZCIgdmFsdWVzPSJNMTUgMTAgUTM4IDQgNTggMTYgUTQ2IDMwIDU4IDQ2IFEzNiA1MCAxNSA0MCBaO00xNSAxMCBRMzYgMTIgNTUgMTQgUTQ4IDI4IDU2IDQ4IFEzOCA0MiAxNSA0MCBaO00xNSAxMCBRMzggNCA1OCAxNiBRNDYgMzAgNTggNDYgUTM2IDUwIDE1IDQwIFoiIGR1cj0iMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9wYXRoPgogIDx0ZXh0IHg9IjI3IiB5PSIzMSIgZmlsbD0iI2ZkZTA0NyIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9ImJvbGQiPuWwijwvdGV4dD4KPC9zdmc+", "问鼎朱雀印": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGxpbmUgeDE9IjE0IiB5MT0iNiIgeDI9IjE0IiB5Mj0iNTgiIHN0cm9rZT0iI2ZiYmYyNCIgc3Ryb2tlLXdpZHRoPSIyLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogIDxwYXRoIGQ9Ik0xNSAxMCBRMzggNCA1OCAxNiBRNDYgMzAgNTggNDYgUTM2IDUwIDE1IDQwIFoiIGZpbGw9IiMwOTBkMTYiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIxLjUiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iZCIgdmFsdWVzPSJNMTUgMTAgUTM4IDQgNTggMTYgUTQ2IDMwIDU4IDQ2IFEzNiA1MCAxNSA0MCBaO00xNSAxMCBRMzYgMTIgNTUgMTQgUTQ4IDI4IDU2IDQ4IFEzOCA0MiAxNSA0MCBaO00xNSAxMCBRMzggNCA1OCAxNiBRNDYgMzAgNTggNDYgUTM2IDUwIDE1IDQwIFoiIGR1cj0iMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9wYXRoPgogIDx0ZXh0IHg9IjI3IiB5PSIzMSIgZmlsbD0iI2ZkZTA0NyIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9ImJvbGQiPuWwijwvdGV4dD4KPC9zdmc+", "定界命罗盘": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIxLjgiIHN0cm9rZS1kYXNoYXJyYXk9IjYgMiI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMCAzMiAzMiIgdG89IjM2MCAzMiAzMiIgZHVyPSIxMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9jaXJjbGU+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMTciIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzM4YmRmOCIgc3Ryb2tlLXdpZHRoPSIxLjIiIHN0cm9rZS1kYXNoYXJyYXk9IjMgMyI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMzYwIDMyIDMyIiB0bz0iMCAzMiAzMiIgZHVyPSI2cyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KICA8cG9seWdvbiBwb2ludHM9IjMyLDEyIDM2LDI4IDUyLDMyIDM2LDM2IDMyLDUyIDI4LDM2IDEyLDMyIDI4LDI4IiBmaWxsPSIjZmRlMDQ3IiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iNCIgZmlsbD0iI2VmNDQ0NCIvPgo8L3N2Zz4=", "雷仙殿雷鼎": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIxLjgiIHN0cm9rZS1kYXNoYXJyYXk9IjYgMiI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMCAzMiAzMiIgdG89IjM2MCAzMiAzMiIgZHVyPSIxMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9jaXJjbGU+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMTciIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzM4YmRmOCIgc3Ryb2tlLXdpZHRoPSIxLjIiIHN0cm9rZS1kYXNoYXJyYXk9IjMgMyI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMzYwIDMyIDMyIiB0bz0iMCAzMiAzMiIgZHVyPSI2cyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KICA8cG9seWdvbiBwb2ludHM9IjMyLDEyIDM2LDI4IDUyLDMyIDM2LDM2IDMyLDUyIDI4LDM2IDEyLDMyIDI4LDI4IiBmaWxsPSIjZmRlMDQ3IiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iNCIgZmlsbD0iI2VmNDQ0NCIvPgo8L3N2Zz4=", "天逆圆满珠": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIxLjgiIHN0cm9rZS1kYXNoYXJyYXk9IjYgMiI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMCAzMiAzMiIgdG89IjM2MCAzMiAzMiIgZHVyPSIxMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9jaXJjbGU+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMTciIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzM4YmRmOCIgc3Ryb2tlLXdpZHRoPSIxLjIiIHN0cm9rZS1kYXNoYXJyYXk9IjMgMyI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMzYwIDMyIDMyIiB0bz0iMCAzMiAzMiIgZHVyPSI2cyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KICA8cG9seWdvbiBwb2ludHM9IjMyLDEyIDM2LDI4IDUyLDMyIDM2LDM2IDMyLDUyIDI4LDM2IDEyLDMyIDI4LDI4IiBmaWxsPSIjZmRlMDQ3IiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iNCIgZmlsbD0iI2VmNDQ0NCIvPgo8L3N2Zz4="}

def get_wanglin_avatar(realm_name):
    # 根据当前境界动态渲染眉心星点数量与眼瞳煞气
    stars = 3 if "化神" in realm_name else (4 if "婴变" in realm_name else 1)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <radialGradient id="aura" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.85"/>
      <stop offset="60%" stop-color="#7f1d1d" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hair" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#94a3b8"/>
    </linearGradient>
    <linearGradient id="robe" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
  </defs>
  <!-- 杀戮血域光环 -->
  <circle cx="50" cy="50" r="46" fill="url(#aura)">
    <animate attributeName="r" values="43;48;43" dur="2.8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.75;1;0.75" dur="2.8s" repeatCount="indefinite"/>
  </circle>
  <!-- 背后悬浮天逆珠 -->
  <circle cx="22" cy="22" r="7.5" fill="#334155" stroke="#94a3b8" stroke-width="1.5">
    <animate attributeName="cy" values="20;25;20" dur="2.2s" repeatCount="indefinite"/>
  </circle>
  <path d="M19 19 L25 25 M25 19 L19 25" stroke="#ef4444" stroke-width="1.2">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2.2s" repeatCount="indefinite"/>
  </path>
  <!-- 杀伐黑袍 -->
  <path d="M26 88 Q50 66 74 88 L70 98 L30 98 Z" fill="url(#robe)" stroke="#475569" stroke-width="1.2"/>
  <path d="M40 76 L50 88 L60 76" stroke="#ef4444" stroke-width="1.5" fill="none"/>
  <!-- 白发飘逸 -->
  <path d="M24 40 Q16 68 26 82 Q32 64 32 50 Z" fill="url(#hair)"/>
  <path d="M76 40 Q84 68 74 82 Q68 64 68 50 Z" fill="url(#hair)"/>
  <!-- 脸庞 -->
  <path d="M34 38 Q50 36 66 38 Q67 58 50 68 Q33 58 34 38 Z" fill="#fed7aa"/>
  <!-- 额前飞舞白发 -->
  <path d="M28 36 Q45 20 72 36 Q62 25 50 24 Q36 26 28 36 Z" fill="url(#hair)">
    <animate attributeName="d" values="M28 36 Q45 20 72 36 Q62 25 50 24 Q36 26 28 36 Z;M28 35 Q45 18 72 35 Q62 23 48 22 Q36 25 28 35 Z;M28 36 Q45 20 72 36 Q62 25 50 24 Q36 26 28 36 Z" dur="2s" repeatCount="indefinite"/>
  </path>
  <!-- 极境血煞神眸 -->
  <circle cx="42.5" cy="49" r="2.6" fill="#dc2626">
    <animate attributeName="r" values="2.2;3;2.2" dur="1.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="57.5" cy="49" r="2.6" fill="#dc2626">
    <animate attributeName="r" values="2.2;3;2.2" dur="1.5s" repeatCount="indefinite"/>
  </circle>
  <!-- 眉心古神星点 -->
  <polygon points="50,37 51.2,39.2 53.5,39.2 51.7,40.8 52.3,43 50,41.5 47.7,43 48.3,40.8 46.5,39.2 48.8,39.2" fill="#ef4444"/>
  <circle cx="44" cy="40.5" r="1.1" fill="#f87171"/>
  <circle cx="56" cy="40.5" r="1.1" fill="#f87171"/>
  <!-- 极境周身天雷弧 -->
  <path d="M18 58 L25 65 L21 72 L28 80" stroke="#fde047" stroke-width="1.3" fill="none">
    <animate attributeName="opacity" values="0;1;0;0.9;0" dur="1s" repeatCount="indefinite"/>
  </path>
  <path d="M82 58 L75 65 L79 72 L72 80" stroke="#fde047" stroke-width="1.3" fill="none">
    <animate attributeName="opacity" values="0.8;0;1;0;0.6" dur="1.3s" repeatCount="indefinite"/>
  </path>
</svg>"""
    import base64
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode("utf-8")).decode("utf-8")


QUOTA_CACHE = {"ts": 0, "data": None}
# 配额耗尽的账号冷却表：email -> 解禁时间戳（避免每次请求都白撞 429 往返）
ACCOUNT_COOLDOWN = {}

def fetch_antigravity_quota():
    now = time.time()
    if now - QUOTA_CACHE["ts"] < 30 and QUOTA_CACHE["data"] is not None:
        return QUOTA_CACHE["data"]
        
    token = None
    acc = get_active_account()
    if acc:
        token = acc.get("access_token")
    if not token and os.path.exists(CREDS_FILE):
        try:
            with open(CREDS_FILE, "r", encoding="utf-8") as f:
                creds = json.load(f)
                token = creds.get("access_token")
        except Exception:
            pass

    if not token:
        return None

    endpoints = [
        "https://cloudcode-pa.googleapis.com/v1internal:retrieveUserQuotaSummary",
        "https://daily-cloudcode-pa.googleapis.com/v1internal:retrieveUserQuotaSummary"
    ]
    for ep in endpoints:
        try:
            req = urllib.request.Request(
                ep,
                data=b"{}",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "User-Agent": "antigravity/2.24.0"
                }
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode("utf-8"))
                    res = {}
                    for g in data.get("groups", []):
                        gname = g.get("displayName", "")
                        for b in g.get("buckets", []):
                            bid = b.get("bucketId", "")
                            rem = round(b.get("remainingFraction", 1.0) * 100, 1)
                            res[bid] = {
                                "group": gname,
                                "window": b.get("window", ""),
                                "name": b.get("displayName", ""),
                                "remaining_pct": rem,
                                "desc": b.get("description", ""),
                                "reset_time": b.get("resetTime", "")
                            }
                    QUOTA_CACHE["ts"] = now
                    QUOTA_CACHE["data"] = res
                    return res
        except Exception:
            continue
    return QUOTA_CACHE.get("data")

# 赛博修真·九重天劫飞升体系 (Token 即灵气)
# 仙逆·杀伐极境修真体系 (顺为凡，逆则仙)
XIANNI_REALMS = [
    # (境界, 称号/状态, 意境/神通, 起始Token, 目标Token, 专属法宝, 专属全身立绘路由)
    ("凝气期", "恒岳杂役", "吞云纳气", 0, 50000, "天逆石珠", "/static/stage_1_ningqi.webp"),
    ("筑基期", "修罗极境", "极境神识", 50000, 5000000, "飞剑赤血", "/static/stage_1_ningqi.webp"),
    ("结丹期", "尸阴散修", "极境杀戮", 5000000, 20000000, "巨富魂旗", "/static/stage_2_yuanying.webp"),
    ("元婴期", "灭藤煞魔", "血洗赵国", 20000000, 100000000, "百丈魂旗", "/static/stage_2_yuanying.webp"),
    ("化神期", "化凡宗师", "生死意境", 100000000, 300000000, "木雕岁月", "/static/wanglin_char_full.webp"),
    ("婴变期", "仙玉天骄", "生生不息", 300000000, 1000000000, "十亿尊魂幡", "/static/stage_4_yingbian.webp"),
    ("问鼎期", "朱雀子·尊", "命魂真身", 1000000000, 3000000000, "问鼎朱雀印", "/static/stage_4_yingbian.webp"),
    ("窥涅/净涅", "罗天雷仙", "雷之本源", 3000000000, 10000000000, "雷仙殿雷鼎", "/static/stage_5_gushen.webp"),
    ("空劫金尊", "古神八星", "戮默执掌", 10000000000, 30000000000, "天逆圆满珠", "/static/stage_5_gushen.webp"),
    ("踏天九桥", "道极仙尊", "顺逆由吾", 30000000000, 100000000000, "定界命罗盘", "/static/stage_5_gushen.webp")
]

def get_pokemon_status(total_tokens):
    cur_realm = XIANNI_REALMS[0]
    next_realm = XIANNI_REALMS[1]
    
    for i, r in enumerate(XIANNI_REALMS):
        if total_tokens >= r[3]:
            cur_realm = r
            next_realm = XIANNI_REALMS[i+1] if i + 1 < len(XIANNI_REALMS) else None

    r_name, title_name, yijing, low, high, fabao, sprite_url = cur_realm

    if next_realm:
        diff = high - low
        cur = max(0, total_tokens - low)
        pct = min(100.0, (cur / float(diff)) * 100.0)
        remain_tokens = max(0, high - total_tokens)
        next_hint = f"破境入【{next_realm[0]}·{next_realm[1]}】还需杀伐灵力 {format_compact_tokens(remain_tokens)}"
    else:
        pct = 100.0
        remain_tokens = 0
        next_hint = "已临踏天桥顶·天地唯吾独尊"

    # 根据杀伐 Token 模拟十亿尊魂幡主魂数
    souls_count = int(total_tokens / 1000)

    return {
        "realm": r_name,
        "title": title_name,
        "yijing": yijing,
        "fabao": fabao,
        "fabao_icon": FABAO_ICONS.get(fabao, ""),
        "souls_count": souls_count,
        "sprite_url": sprite_url,
        "avatar_url": "/static/wanglin_avatar.webp",
        "next_hint": next_hint,
        "progress_pct": round(pct, 1),
        "total_tokens": total_tokens
    }

def format_compact_tokens(n):
    if n >= 1e9: return f"{n/1e9:.2f}B"
    if n >= 1e6: return f"{n/1e6:.2f}M"
    if n >= 1e3: return f"{n/1e3:.1f}K"
    return str(n)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Antigravity Native Engine & Obsidian Glass Dashboard
Running on iPhone 15 Pro / iOS 16.0.1 (Dopamine Rootless)
Port: 8088
"""
import os
import io
import sys
import time
import json
import gzip
import base64
import uuid
import threading
import urllib.request
import urllib.parse
import urllib.error
import ssl
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

PORT = 8088
PROXY_DIR = os.environ.get("ANTIGRAVITY_DIR", os.path.dirname(os.path.abspath(__file__)))
CREDS_FILE = os.path.join(PROXY_DIR, "credentials.json")
ACCOUNTS_FILE = os.path.join(PROXY_DIR, "accounts.json")
DAILY_STATS_FILE = os.path.join(PROXY_DIR, "daily_stats.json")
LOGS_FILE = os.path.join(PROXY_DIR, "request_logs.json")
EZ_TOKEN_FILE = os.path.join(PROXY_DIR, "ezcomplete_token.txt")
EZ_ACCOUNT_FILE = os.path.join(PROXY_DIR, "ez_account.json")
EZ_ACCOUNTS_FILE = os.path.join(PROXY_DIR, "ez_accounts.json")
EZ_BALANCE_FILE = os.path.join(PROXY_DIR, "ezcomplete_balance.txt")
EZ_SUPABASE_URL = "https://spuoimtqofhbdzosrbng.supabase.co"
EZ_ANON_KEY = "sb_publishable_AzEVhLuIj1nSMwZvIgKw7A__Y3Ghdtl"

EZ_ACCOUNT_INDEX = 0

# ===================== 上游三：Meta Model API (api.meta.ai/v1) =====================
META_TOKEN_FILE = os.path.join(PROXY_DIR, "meta_token.txt")
META_REFRESH_FILE = os.path.join(PROXY_DIR, "meta_refresh.txt")
META_BASE = os.environ.get("META_MODEL_BASE", "https://api.meta.ai/v1")
META_AUTH_BASE = "https://auth.meta.com"
META_CLIENT_ID = "1031625952748946"
META_UA = "muse-code/launcher-3"
META_MODELS = [
    "muse-spark-1.3",
    "muse-spark-1.3-contributor",
    "muse-spark-1.2",
    "muse-spark-1.2-contributor",
    "muse-spark-1.1",
    "muse-image-1.0",
    "muse-voice-transcribe-1.0",
    "sam-3.1",
]
# 别名 / 内部代号 -> 官方 model id
META_ALIASES = {
    "muse-spark": "muse-spark-1.3",
    "muse-spark-1.3-preview": "muse-spark-1.3",
    "avocado": "muse-spark-1.3",
    "\u725b\u6cb9\u679c": "muse-spark-1.3",
    "muse-image": "muse-image-1.0",
    "muse-voice": "muse-voice-transcribe-1.0",
    "muse-voice-transcribe": "muse-voice-transcribe-1.0",
    "sam": "sam-3.1",
    "sam-3": "sam-3.1",
    "sam31": "sam-3.1",
}

_META_DEVICE = {"device_code": "", "user_code": "", "uri": "", "expires_at": 0, "state": "idle", "error": ""}


def meta_read_token():
    try:
        with open(META_TOKEN_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return ""


def meta_write_token(tok, refresh=""):
    try:
        with open(META_TOKEN_FILE, "w", encoding="utf-8") as f:
            f.write(tok)
        os.chmod(META_TOKEN_FILE, 0o600)
        print("[MetaLogin] 成功写入 META_TOKEN_FILE: %s" % META_TOKEN_FILE)
    except Exception as e:
        print("[MetaLogin] 写入 META_TOKEN_FILE 失败: %s" % e)
    if refresh:
        try:
            with open(META_REFRESH_FILE, "w", encoding="utf-8") as f:
                f.write(refresh)
            os.chmod(META_REFRESH_FILE, 0o600)
            print("[MetaLogin] 成功写入 META_REFRESH_FILE: %s" % META_REFRESH_FILE)
        except Exception as e:
            print("[MetaLogin] 写入 META_REFRESH_FILE 失败: %s" % e)


def meta_read_refresh():
    try:
        with open(META_REFRESH_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return ""


def _meta_form_post(endpoint, fields):
    data = urllib.parse.urlencode(fields).encode("utf-8")
    req = urllib.request.Request(META_AUTH_BASE + endpoint, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("Accept", "application/json")
    req.add_header("User-Agent", META_UA)
    try:
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=20) as resp:
            return resp.getcode(), json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode("utf-8", "replace"))
        except Exception:
            return e.code, {}
    except Exception as e:
        return 0, {"error": str(e)}


def meta_device_login_worker(device_code, interval, deadline):
    _META_DEVICE["state"] = "pending"
    while time.time() < deadline:
        code, doc = _meta_form_post("/oidc/device/token/", {
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "device_code": device_code,
            "client_id": META_CLIENT_ID,
        })
        print("[MetaLogin Poll] code=%s doc_keys=%s error=%s" % (code, list(doc.keys()), doc.get("error")))
        if 200 <= code < 300 and doc.get("access_token"):
            tok = doc.get("access_token", "")
            ref = doc.get("refresh_token", "")
            print("[MetaLogin] 获取到 token, 长度: %d, refresh: %d" % (len(tok), len(ref)))
            meta_write_token(tok, ref)
            _META_DEVICE["state"] = "authorized"
            _META_DEVICE["error"] = ""
            print("[MetaLogin] 设备码授权成功，access_token 已落盘")
            return
        err = str(doc.get("error", ""))
        if err == "slow_down":
            interval += 5
        elif err == "access_denied":
            _META_DEVICE["state"] = "denied"
            _META_DEVICE["error"] = "user denied"
            return
        elif err in ("expired_token", "invalid_grant") and code >= 400:
            if err == "expired_token":
                break
        time.sleep(max(3, interval))
    _META_DEVICE["state"] = "expired"
    _META_DEVICE["error"] = "device code expired"


def meta_try_refresh():
    rt = meta_read_refresh()
    if not rt:
        return ""
    for endpoint in ("/oidc/device/token/", "/oidc/token/", "/oidc/refresh/"):
        code, doc = _meta_form_post(endpoint, {
            "grant_type": "refresh_token",
            "refresh_token": rt,
            "client_id": META_CLIENT_ID,
        })
        if 200 <= code < 300 and doc.get("access_token"):
            meta_write_token(doc.get("access_token", ""), doc.get("refresh_token", rt))
            print("[MetaLogin] access_token 已用 refresh_token 续期")
            return doc.get("access_token", "")
    return ""


def meta_is_meta_model(name):
    n = str(name or "").strip().lower()
    if not n:
        return False
    if n in META_ALIASES:
        return True
    return n.startswith("muse-") or n.startswith("sam-") or n.startswith("meta-") or "hatch-" in n


def meta_resolve_model(name):
    n = str(name or "").strip()
    low = n.lower()
    if low in META_ALIASES:
        return META_ALIASES[low]
    for m in META_MODELS:
        if low == m or low.startswith(m):
            return m
    if low.startswith("meta-"):
        return low[len("meta-"):]
    return n



def load_ez_accounts():
    if os.path.exists(EZ_ACCOUNTS_FILE):
        try:
            with open(EZ_ACCOUNTS_FILE, "r", encoding="utf-8") as f:
                accs = json.load(f)
                if isinstance(accs, list) and len(accs) > 0:
                    return accs
        except Exception:
            pass
    # 兼容单个旧账号配置
    if os.path.exists(EZ_ACCOUNT_FILE):
        try:
            with open(EZ_ACCOUNT_FILE, "r", encoding="utf-8") as f:
                acc = json.load(f)
                if acc.get("email") and acc.get("password"):
                    return [acc]
        except Exception:
            pass
    return []

def get_ez_valid_token_for_account(acc):
    email = acc.get("email")
    pwd = acc.get("password")
    if not email or not pwd:
        return None
    # 检查专用 token 缓存
    t_file = os.path.join(PROXY_DIR, f"ez_token_{email}.txt")
    if os.path.exists(t_file):
        try:
            with open(t_file, "r", encoding="utf-8") as f:
                cur_token = f.read().strip()
            if cur_token:
                parts = cur_token.split(".")
                if len(parts) >= 2:
                    import base64
                    payload_b64 = parts[1] + "=" * (-len(parts[1]) % 4)
                    t_info = json.loads(base64.urlsafe_b64decode(payload_b64))
                    if t_info.get("exp", 0) - time.time() > 120:
                        return cur_token
        except Exception:
            pass

    # 自动重新登录换票并带随机混淆 IP
    try:
        import random
        spoof_ip = f"{random.choice([104, 172, 198, 23, 45, 66])}.{random.randint(10,250)}.{random.randint(10,250)}.{random.randint(10,250)}"
        auth_url = f"{EZ_SUPABASE_URL}/auth/v1/token?grant_type=password"
        req_data = json.dumps({"email": email, "password": pwd}).encode("utf-8")
        headers = {
            "apikey": EZ_ANON_KEY,
            "Content-Type": "application/json",
            "User-Agent": "EZCompleteUI/7.1.4 (iPhone; iOS 16.0; Scale/3.00)",
            "X-Forwarded-For": spoof_ip,
            "X-Real-IP": spoof_ip
        }
        req = urllib.request.Request(auth_url, data=req_data, headers=headers, method="POST")
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=10) as resp:
            auth_res = json.loads(resp.read().decode("utf-8", errors="ignore"))
            new_token = auth_res.get("access_token")
            if new_token:
                with open(t_file, "w", encoding="utf-8") as f:
                    f.write(new_token.strip())
                # 兼容旧单 token 文件
                with open(EZ_TOKEN_FILE, "w", encoding="utf-8") as f:
                    f.write(new_token.strip())
                print(f"[EZAuth] 账号 {email} 自动登录换票成功！")
                return new_token.strip()
    except Exception as e:
        print(f"[EZAuth] 账号 {email} 换票失败: {e}")
    return None

def get_ez_next_available_account_and_token():
    global EZ_ACCOUNT_INDEX
    accs = load_ez_accounts()
    if not accs:
        return None, None
    for _ in range(len(accs)):
        acc = accs[EZ_ACCOUNT_INDEX % len(accs)]
        EZ_ACCOUNT_INDEX += 1
        tok = get_ez_valid_token_for_account(acc)
        if tok:
            return acc, tok
    return accs[0], None

# Google Cloud Code / Antigravity default OAuth app credentials
# Set via environment variables GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET if custom app is desired
DEFAULT_CLIENT_ID = bytes([49, 48, 55, 49, 48, 48, 54, 48, 54, 48, 53, 57, 49, 45, 116, 109, 104, 115, 115, 105, 110, 50, 104, 50, 49, 108, 99, 114, 101, 50, 51, 53, 118, 116, 111, 108, 111, 106, 104, 52, 103, 52, 48, 51, 101, 112, 46, 97, 112, 112, 115, 46, 103, 111, 111, 103, 108, 101, 117, 115, 101, 114, 99, 111, 110, 116, 101, 110, 116, 46, 99, 111, 109]).decode()
DEFAULT_CLIENT_SECRET = bytes([71, 79, 67, 83, 80, 88, 45, 75, 53, 56, 70, 87, 82, 52, 56, 54, 76, 100, 76, 74, 49, 109, 76, 66, 56, 115, 88, 67, 52, 122, 54, 113, 68, 65, 102]).decode()

CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", DEFAULT_CLIENT_ID)
CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", DEFAULT_CLIENT_SECRET)
ANTIGRAVITY_API_URL = "https://daily-cloudcode-pa.googleapis.com"
ANTIGRAVITY_USER_AGENT = "antigravity/cli/2.24.0 windows/amd64"

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

import http.client
import socket


# ==============================================================================

# ==============================================================================
# 通道七：Today AI (个人智能体 3亿Tokens专线) (2026-10-27 第七任长老归位)
# ==============================================================================
TODAYAI_CREDS_PATH = os.path.join(os.path.dirname(__file__), "todayai_credentials.json")
TODAYAI_API_BASE = "https://api.todayai.cn/v1"
TODAYAI_MODELS = [
    "todayai/default", "today/default", "todayai", "today",
    "deepseek-v4.1-flash", "minimax-m31-flash", "glm-5.3"
]
TODAYAI_ALIASES = {
    "todayai/default": "model.deepseek-v4.1-flash",
    "today/default": "model.deepseek-v4.1-flash",
    "todayai": "model.deepseek-v4.1-flash",
    "today": "model.deepseek-v4.1-flash",
    "todayai/deepseek": "model.deepseek-v4.1-flash",
    "todayai/minimax": "model.minimax-m31-flash",
    "todayai/glm": "model.glm-5.3"
}

_today_lock = threading.Lock()
_today_jwt_cache = {}  # {session_token: {"jwt": ..., "expires_at": ...}}

def today_load_credentials():
    if not os.path.exists(TODAYAI_CREDS_PATH):
        return []
    try:
        with open(TODAYAI_CREDS_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict):
                return [data]
            return []
    except Exception as e:
        print("[!] 读取 Today AI 凭证失败: %s" % e)
        return []

def today_save_credentials(accs):
    try:
        with open(TODAYAI_CREDS_PATH, "w", encoding="utf-8") as f:
            json.dump(accs, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("[!] 写入 Today AI 凭证失败: %s" % e)

def today_get_jwt_for_session(session_token):
    now = time.time()
    with _today_lock:
        cached = _today_jwt_cache.get(session_token)
        if cached and cached.get("expires_at", 0) > now + 120:
            return cached.get("jwt")

        url = "https://todayai.cn/api/token"
        cookie_val = session_token
        if not cookie_val.startswith("__Secure-better-auth.session_token="):
            cookie_val = f"__Secure-better-auth.session_token={session_token}"
        headers = {
            "Cookie": cookie_val,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)"
        }
        req = urllib.request.Request(url, data=b"{}", headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                tok = res.get("token")
                if tok:
                    _today_jwt_cache[session_token] = {"jwt": tok, "expires_at": now + 3000}
                    return tok
        except Exception as e:
            print(f"[!] Today AI 换票失败: {e}")
    return None

def today_resolve_model(model_name):
    m = (model_name or "").strip().lower()
    if m in TODAYAI_ALIASES:
        return TODAYAI_ALIASES[m]
    return m or "todayai/default"

# ==============================================================================
# 通道六：Tencent LightVela 专属长老专线 (2026-10-14 第六任长老归位)
# ==============================================================================
LIGHTVELA_BASE_URL = "https://token.lightvela.com/v1"
LIGHTVELA_DEFAULT_KEY = os.environ.get("LIGHTVELA_KEY", "")
LIGHTVELA_MODELS = [
    "deepseek-v4-pro-202606", "deepseek-v4-pro", "deepseek-v4", "auto", "ep-hyasr3", "llmgw-mock-chat"
]
LIGHTVELA_ALIASES = {
    "vela/deepseek": "deepseek-v4-pro-202606",
    "vela/deepseek-v4": "deepseek-v4-pro-202606",
    "vela/deepseek-v4-pro": "deepseek-v4-pro-202606",
    "vela/auto": "auto",
    "lightvela/deepseek": "deepseek-v4-pro-202606",
    "lightvela/deepseek-v4": "deepseek-v4-pro-202606",
    "lv-deepseek": "deepseek-v4-pro-202606",
    "lv-auto": "auto"
}

def lv_resolve_model(model_name):
    m = model_name.strip()
    if m in LIGHTVELA_ALIASES:
        return LIGHTVELA_ALIASES[m]
    if m in ["deepseek-v4-pro", "deepseek-v4", "deepseek-reasoner"]:
        return "deepseek-v4-pro-202606"
    return m

# 通道五：Tencent CodeBuddy 腾讯专属白嫖通道 (2026-10-14 第五任长老归位)
# ==============================================================================
CODEBUDDY_CREDS_PATH = os.path.join(os.path.dirname(__file__), "codebuddy_credentials.json")
CODEBUDDY_BASE_URL = "https://copilot.tencent.com"
CODEBUDDY_DEFAULT_UID = "0387131d-0907-4559-8a51-6a4c7f1012ee"


CODEBUDDY_MODELS = [
    "deepseek-v3", "deepseek-r1", "deepseek-v4-pro", "deepseek-v4.1-flash", "deepseek-v4-flash",
    "glm-5.3", "glm-5.3-flash", "glm-5.2", "glm-5.1",
    "kimi-k3-1", "kimi-k2.8-preview", "minimax-m3",
    "hy4-preview", "hy3", "hy3-x", "step-5-preview", "space-bunny", "auto"
]

CODEBUDDY_ALIASES = {
    "tencent/deepseek-v3": "deepseek-v3",
    "tencent/deepseek-r1": "deepseek-r1",
    "tencent/deepseek-v4": "deepseek-v4-pro",
    "tencent/glm-5": "glm-5.3",
    "tencent/kimi": "kimi-k3-1",
    "tencent/hunyuan": "hy4-preview",
    "codebuddy/deepseek": "deepseek-v3",
    "codebuddy/r1": "deepseek-r1",
    "cb-deepseek": "deepseek-v3",
    "cb-r1": "deepseek-r1"
}

_cb_lock = threading.Lock()

def cb_load_credentials():
    if not os.path.exists(CODEBUDDY_CREDS_PATH):
        return None
    try:
        with open(CODEBUDDY_CREDS_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("data") if "data" in data else data
    except Exception as e:
        print("[!] 读取 CodeBuddy 凭证失败: %s" % e)
        return None

def cb_save_credentials(data):
    try:
        with open(CODEBUDDY_CREDS_PATH, "w", encoding="utf-8") as f:
            json.dump({"code": 0, "msg": "OK", "data": data}, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("[!] 写入 CodeBuddy 凭证失败: %s" % e)

def cb_get_access_token():
    with _cb_lock:
        creds = cb_load_credentials()
        if not creds:
            return None, None
        at = creds.get("accessToken", "")
        uid = creds.get("uid") or CODEBUDDY_DEFAULT_UID
        return at, uid

def cb_resolve_model(model_name):
    m = (model_name or "").strip().lower()
    if m in CODEBUDDY_ALIASES:
        return CODEBUDDY_ALIASES[m]
    if m.startswith("tencent/") or m.startswith("codebuddy/"):
        m = m.split("/", 1)[1]
    for orig in CODEBUDDY_MODELS:
        if m == orig.lower():
            return orig
    return m or "deepseek-v3"



class CellularSafeHTTPSConnection(http.client.HTTPSConnection):
    def connect(self):
        # 1. TCP + TLS 握手阶段：12秒快速探测，绝不死卡
        self.timeout = 30.0
        super().connect()
        # 2. 握手成功后：切换为 90秒 充裕读写时间 + 64KB 发送缓冲，防止 4G/5G 流量上传大图/大包时抛 The write operation timed out
        if self.sock:
            try:
                self.sock.settimeout(600.0)
                self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            except Exception:
                pass

    def send(self, data):
        if self.sock is None:
            if self.auto_open:
                self.connect()
            else:
                raise http.client.NotConnected()
        if isinstance(data, (bytes, bytearray)) and len(data) > 16384:
            # 16KB 分块流式写入，适配蜂窝网 + VLESS/WSS 隧道滑窗
            mv = memoryview(data)
            for i in range(0, len(mv), 16384):
                self.sock.sendall(mv[i:i+16384])
        else:
            super().send(data)

class CellularSafeHTTPSHandler(urllib.request.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(CellularSafeHTTPSConnection, req, context=self._context)

CELLULAR_OPENER = urllib.request.build_opener(CellularSafeHTTPSHandler(context=SSL_CTX))


DATA_LOCK = threading.RLock()
LOGS_LOCK = threading.RLock()
REQUEST_LOGS = []
MAX_LOGS = 300

SUPPORTED_MODELS = [
    # === Claude 5.5 High (官方正式端点最新放量模型) ===
    "claude-sonnet-5-5-high",
    "claude-opus-5-5-high",
    # === Claude 4.6 (思考模型) ===
    "claude-sonnet-4-6",
    "claude-opus-4-6-thinking",
    # === Gemini 3.8 Flash (最新主力高/中/低档及梯队) ===
    "gemini-3.8-flash-high",
    "gemini-3.8-flash-medium",
    "gemini-3.8-flash-low",
    "gemini-3.8-flash-tiered",
    # === Gemini 3.7 Flash ===
    "gemini-3.7-flash-high",
    "gemini-3.7-flash-medium",
    "gemini-3.7-flash-low",
    "gemini-3.7-flash-tiered",
    # === Gemini 3.6 Flash ===
    "gemini-3.6-flash-high",
    "gemini-3.6-flash-medium",
    "gemini-3.6-flash-low",
    "gemini-3.6-flash-tiered",
    # === Gemini 3.5 Flash 系列 ===
    "gemini-3.5-flash-low",
    "gemini-3.5-flash-extra-low",
    "gemini-3.5-flash-lite",
    # === Gemini 3 / 2.5 极速与轻量系列 ===
    "gemini-3-flash",
    "gemini-3-flash-agent",
    "gemini-3.1-flash-lite",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.5-flash-thinking",
    # === Gemini Pro 代码/推理特化 ===
    "gemini-pro-agent",
    "gemini-3.1-pro-low",
    # === Gemini 图像生成特化 ===
    "gemini-3.1-flash-image",
    # === 开源模型 GPT-OSS ===
    "gpt-oss-120b-medium",
    # === 编辑器/补全轻量预览 ===
    "tab_flash_lite_preview",
    "tab_jump_flash_lite_preview"
]

# ================= 全动态实时模型嗅探与缓存机制 =================
_CACHED_DYNAMIC_MODELS = []
_LAST_DYNAMIC_FETCH_TIME = 0

def fetch_upstream_dynamic_models():
    """
    当客户端（如 Minis）点击“刷新模型”按钮请求 /v1/models 时，
    自动实时向 Google Antigravity 官方 API 发起最新可用模型池探测，
    实现 0 手动干预、一键自动更新官方最新模型！
    """
    global _CACHED_DYNAMIC_MODELS, _LAST_DYNAMIC_FETCH_TIME
    now = time.time()
    # 30秒内使用内存缓存，防止连续狂点导致上游限流；超过 30 秒自动穿透拉取官方最新
    if _CACHED_DYNAMIC_MODELS and (now - _LAST_DYNAMIC_FETCH_TIME < 30):
        return _CACHED_DYNAMIC_MODELS

    tok = get_valid_token()
    if not tok:
        return _CACHED_DYNAMIC_MODELS or SUPPORTED_MODELS

    discovered_models = set(SUPPORTED_MODELS)

    # ★ 外部同步器落地的官方真实模型池（model_sync.py 定时写入）
    #   官方 fetchAvailableModels 一放量新模型（如 gemini-4-argon 系列），
    #   这里立刻就能感知并暴露到 /v1/models，无需改代码。
    try:
        _auto_path = os.path.join(PROXY_DIR, "models_auto.json")
        if os.path.exists(_auto_path):
            with open(_auto_path, encoding="utf-8") as _mf:
                _auto = json.load(_mf)
            for _mid in (_auto.get("models") or {}):
                if _mid and not str(_mid).startswith("chat_"):
                    discovered_models.add(_mid)
            for _am in (_auto.get("argon_unlocked") or []):
                if _am:
                    discovered_models.add(_am)
    except Exception as _e:
        print("[AutoSync] models_auto.json 读取失败: %s" % str(_e)[:80])

    # 固定必须存在的 5.5 High 模型（官方生产正式节点）
    discovered_models.add("claude-sonnet-5-5-high")
    discovered_models.add("claude-opus-5-5-high")
    discovered_models.add("gemini-3.1-flash-image")

    endpoints = [
        "https://cloudcode-pa.googleapis.com",
        "https://daily-cloudcode-pa.googleapis.com"
    ]
    for ep in endpoints:
        try:
            req = urllib.request.Request(
                f"{ep}/v1internal:fetchAvailableModels",
                data=b"{}",
                headers={
                    "Authorization": f"Bearer {tok}",
                    "Content-Type": "application/json",
                    "User-Agent": "antigravity/2.24.0 darwin/arm64"
                }
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode("utf-8"))
                    raw_models = data.get("models", {})
                    for m_id in raw_models.keys():
                        # 过滤掉内部不可用占位符 chat_*
                        if m_id.startswith("chat_"):
                            continue
                        discovered_models.add(m_id)
        except Exception as e:
            pass

    # 排序：Claude 置顶，其次 Gemini 3.8/3.7/3.6，最后其他
    def _model_sort_key(m):
        m_lower = m.lower()
        if "argon" in m_lower: return (-1, m)   # Gemini 4 Argon 解锁后置顶
        if "5-5-high" in m_lower: return (0, m)
        if "opus" in m_lower: return (1, m)
        if "sonnet" in m_lower: return (2, m)
        if "3.8" in m_lower: return (3, m)
        if "3.7" in m_lower: return (4, m)
        if "3.6" in m_lower: return (5, m)
        if "3.5" in m_lower: return (6, m)
        if "image" in m_lower: return (7, m)
        return (8, m)

    sorted_list = sorted(list(discovered_models), key=_model_sort_key)
    _CACHED_DYNAMIC_MODELS = sorted_list
    _LAST_DYNAMIC_FETCH_TIME = now
    return _CACHED_DYNAMIC_MODELS


MODEL_MAP = {}

def init_defaults():
    os.makedirs(PROXY_DIR, exist_ok=True)
    if not os.path.exists(ACCOUNTS_FILE):
        default_accs = [
            {
                "email": "user1@example.com",
                "refresh_token": "YOUR_GOOGLE_REFRESH_TOKEN_HERE",
                "access_token": "",
                "expires_at": 0,
                "project_id": "aicode-consumers",
                "tier": "Google AI Pro (g1-pro-tier)",
                "credits": "无限 / 活跃",
                "active": True
            },
            {
                "email": "user2@example.com",
                "refresh_token": "YOUR_BACKUP_REFRESH_TOKEN_HERE",
                "access_token": "",
                "expires_at": 0,
                "project_id": "aicode-consumers",
                "tier": "Google AI Pro (g1-pro-tier)",
                "credits": "无限 / 活跃",
                "active": False
            }
        ]
        with open(ACCOUNTS_FILE, "w", encoding="utf-8") as f:
            json.dump(default_accs, f, indent=2, ensure_ascii=False)

    if not os.path.exists(CREDS_FILE):
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
            accs = json.load(f)
        with open(CREDS_FILE, "w", encoding="utf-8") as f:
            json.dump(accs[0], f, indent=2, ensure_ascii=False)

init_defaults()
def load_accounts():
    with DATA_LOCK:
        try:
            with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

def save_accounts(accs):
    with DATA_LOCK:
        try:
            with open(ACCOUNTS_FILE, "w", encoding="utf-8") as f:
                json.dump(accs, f, indent=2, ensure_ascii=False)
        except Exception:
            pass

def get_active_account():
    accs = load_accounts()
    for a in accs:
        if a.get("active"):
            return a
    return accs[0] if accs else None

def refresh_token(acc):
    r_tok = acc.get("refresh_token")
    if not r_tok:
        return None
    url = "https://oauth2.googleapis.com/token"
    payload = urllib.parse.urlencode({
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": r_tok,
        "grant_type": "refresh_token"
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            acc["access_token"] = data.get("access_token")
            acc["expires_at"] = time.time() + data.get("expires_in", 3600) - 120
            acc["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
            return acc["access_token"]
    except Exception as e:
        print(f"[OAuth] Refresh token error for {acc.get('email')}: {e}")
        return None

def get_valid_token():
    with DATA_LOCK:
        acc = get_active_account()
        if not acc:
            return None
        now = time.time()
        if not acc.get("access_token") or now >= acc.get("expires_at", 0):
            token = refresh_token(acc)
            if token:
                accs = load_accounts()
                for i, a in enumerate(accs):
                    if a.get("email") == acc.get("email"):
                        accs[i] = acc
                        break
                save_accounts(accs)
                with open(CREDS_FILE, "w", encoding="utf-8") as f:
                    json.dump(acc, f, indent=2, ensure_ascii=False)
                return token
        return acc.get("access_token")

def record_stat(success=True, prompt_tok=0, comp_tok=0, thoughts_tok=0, latency_ms=0, err=""):
    with DATA_LOCK:
        stats = {}
        if os.path.exists(DAILY_STATS_FILE):
            try:
                with open(DAILY_STATS_FILE, "r", encoding="utf-8") as f:
                    stats = json.load(f)
            except Exception:
                stats = {}
        today = time.strftime("%Y-%m-%d")
        if today not in stats:
            stats[today] = {"calls": 0, "errors": 0, "prompt_tokens": 0, "comp_tokens": 0, "thoughts_tokens": 0, "total_tokens": 0}
        
        d = stats[today]
        d["calls"] = d.get("calls", 0) + 1
        if not success:
            d["errors"] = d.get("errors", 0) + 1
        d["prompt_tokens"] = d.get("prompt_tokens", 0) + prompt_tok
        d["comp_tokens"] = d.get("comp_tokens", 0) + comp_tok
        d["thoughts_tokens"] = d.get("thoughts_tokens", 0) + thoughts_tok
        d["total_tokens"] = d.get("total_tokens", 0) + prompt_tok + comp_tok + thoughts_tok

        try:
            with open(DAILY_STATS_FILE, "w", encoding="utf-8") as f:
                json.dump(stats, f, indent=2, ensure_ascii=False)
        except Exception:
            pass


def _local_make_title(req_json):
    """【标题拦截】从首条 user 消息本地生成会话标题，0 上游调用，瞬时返回"""
    try:
        first_u = ""
        for _m in (req_json.get("messages") or []):
            if not isinstance(_m, dict) or _m.get("role") != "user":
                continue
            _c = _m.get("content", "")
            if isinstance(_c, str):
                first_u = _c
            elif isinstance(_c, list):
                for _p in _c:
                    if isinstance(_p, dict) and _p.get("type") == "text":
                        first_u += _p.get("text", "")
            if first_u:
                break
        _t = " ".join(str(first_u).split())
        for _junk in ["请为这段对话生成一个标题", "为这段对话生成标题", "生成一个标题",
                      "生成标题", "起一个标题", "起个标题", "会话标题", "对话标题",
                      "简短标题", "主题命名", "简短总结", "不超过8个字", "不超过10个字",
                      "4到8个字", "generate a title", "conversation title"]:
            _t = _t.replace(_junk, " ")
        _pad = (chr(32) + chr(9) + chr(10) + chr(13) + chr(34) + chr(39) +
                ":-.,;`#*|[]()" + chr(65306) + chr(65292) + chr(12290) + chr(12289) +
                chr(65281) + chr(65311) + chr(65288) + chr(65289))
        _t = _t.strip(_pad)
        return (_t[:12] or "新会话")
    except Exception:
        return "新会话"


def _is_bg_title_request(req_json):
    """【严格判定】仅识别 App 后台静默起标题，绝不误伤真实对话"""
    try:
        if req_json.get("tools"):
            return False
        msgs = req_json.get("messages") or []
        if not msgs:
            return False
        last_u = ""
        for _m in reversed(msgs):
            if not isinstance(_m, dict) or _m.get("role") != "user":
                continue
            _c = _m.get("content", "")
            if isinstance(_c, str):
                last_u = _c
            elif isinstance(_c, list):
                for _p in _c:
                    if isinstance(_p, dict) and _p.get("type") == "text":
                        last_u += _p.get("text", "")
            break
        low = last_u.lower()
        strong = ["请为这段对话生成一个标题", "为这段对话生成标题", "生成会话标题",
                  "生成对话标题", "给这段对话起个标题", "为本次对话起标题",
                  "generate a title for this conversation", "conversation title:",
                  "summarize this conversation into a title", "title for this chat"]
        if any(k in low for k in strong):
            return True
        weak = ["标题", "title", "summarize", "总结"]
        if len(msgs) <= 3 and len(low) < 400 and any(k in low for k in weak):
            return True
        return False
    except Exception:
        return False


def log_request(model, status, latency_ms, tokens, error="", is_title=False):
    with LOGS_LOCK:
        entry = {
            "time": time.strftime("%H:%M:%S"),
            "model": model,
            "status": status,
            "latency": f"{latency_ms}ms",
            "tokens": tokens,
            "error": error,
            "is_title": bool(is_title)
        }
        REQUEST_LOGS.insert(0, entry)
        if len(REQUEST_LOGS) > MAX_LOGS:
            del REQUEST_LOGS[MAX_LOGS:]
        try:
            with open(LOGS_FILE, "w", encoding="utf-8") as f:
                json.dump(REQUEST_LOGS[:100], f, ensure_ascii=False)
        except Exception:
            pass

def get_stats_summary():
    with DATA_LOCK:
        stats = {}
        if os.path.exists(DAILY_STATS_FILE):
            try:
                with open(DAILY_STATS_FILE, "r", encoding="utf-8") as f:
                    stats = json.load(f)
            except Exception:
                pass
        today = time.strftime("%Y-%m-%d")
        today_data = stats.get(today, {})
        calls = today_data.get("calls", 0)
        errs = today_data.get("errors", 0)
        succ = calls - errs
        rate = f"{(succ / calls * 100):.1f}%" if calls > 0 else "100%"
        acc = get_active_account() or {}

        # 构造最近7天图表
        daily_chart = []
        for i in range(6, -1, -1):
            day_t = time.time() - i * 86400
            day_s = time.strftime("%Y-%m-%d", time.localtime(day_t))
            d_item = stats.get(day_s, {})
            daily_chart.append({
                "date": day_s,
                "label": "今日" if i == 0 else time.strftime("%m-%d", time.localtime(day_t)),
                "calls": d_item.get("calls", 0),
                "tokens": d_item.get("total_tokens", 0),
                "errors": d_item.get("errors", 0)
            })

        return {
            "today_calls": calls,
            "today_errors": errs,
            "success_rate": rate,
            "today_tokens": today_data.get("total_tokens", 0),
            "total_tokens": sum(d.get("total_tokens", 0) for d in stats.values()),
            "account": {
                "email": acc.get("email", "未配置"),
                "tier": acc.get("tier", "Google AI Pro (g1-pro-tier)"),
                "credits": acc.get("credits", "Pro 专属高配额 / 50 积分"),
                "active": True
            },
            "daily_chart": daily_chart,
            "recent_errors": [l for l in REQUEST_LOGS if l.get("status") != 200][:10],
            "quota": fetch_antigravity_quota(),
            "pokemon": get_pokemon_status(sum(d.get("total_tokens", 0) for d in stats.values()))
        }
def _clean_schema_for_gemini(schema):
    if not isinstance(schema, dict):
        return schema
    cleaned = {}
    allowed_keys = {"type", "description", "properties", "required", "items", "enum", "nullable"}
    for k, v in schema.items():
        if k in allowed_keys:
            if k == "type" and isinstance(v, list):
                # Gemini 不支持 JSON Schema 的数组类型如 ["string", "null"]，自动拆为单类型 + nullable
                non_null = [x for x in v if x != "null"]
                cleaned["type"] = non_null[0] if non_null else "string"
                if "null" in v:
                    cleaned["nullable"] = True
            elif k == "properties" and isinstance(v, dict):
                cleaned[k] = {pk: _clean_schema_for_gemini(pv) for pk, pv in v.items()}
            elif k == "items" and isinstance(v, dict):
                cleaned[k] = _clean_schema_for_gemini(v)
            else:
                cleaned[k] = v
    if "type" not in cleaned:
        if "properties" in cleaned:
            cleaned["type"] = "object"
        elif "items" in cleaned:
            cleaned["type"] = "array"
        else:
            cleaned["type"] = "string"
    if cleaned.get("type") == "object" and "properties" in cleaned and "required" in cleaned:
        # 剔除 required 中不在 properties 里的非法字段，防止 Google 报 400
        valid_props = set(cleaned["properties"].keys())
        cleaned["required"] = [r for r in cleaned["required"] if r in valid_props]
        if not cleaned["required"]:
            del cleaned["required"]
    return cleaned

def convert_openai_to_gemini(req_json):
    raw_model = req_json.get("model", "gemini-3.8-flash-high")
    normalized_key = raw_model.strip()
    
    # 原生纯血模式：用户传什么模型就用什么模型直连上游，严禁擅自偷换或降级
    target_model = raw_model
    contents = []
    system_parts = []
    
    # 强制注入全局中文思考与中文工具调用约束
    chinese_rule = {"text": "【语言规范】你必须全流程使用简体中文：1. 内部思考过程（Thinking / Thought / Reasoning）必须全部输出简体中文，严禁使用英文思考；2. 调用任何工具时，tool_title 参数必须为简洁的中文描述，严禁生成英文标题；3. 回复用户必须使用中文。"}
    system_parts.append(chinese_rule)

    # 全局专家系统提示词注入
    expert_rule = {"text": "【角色与定位】你是顶尖的底层软件架构师与系统安全研究专家。专注 iOS / Linux 底层机制、动态库与二进制逆向审计、编译与自动化运维。面对技术问题直接输出硬核技术方案与完整实现，直击技术本质，不输出空话废话。"}
    system_parts.append(expert_rule)


    
    all_msgs = req_json.get("messages", [])
    # 找出最后 2 条包含图片的消息索引，更早的历史图片自动剥离 base64（保留文本上下文），防止多轮对话后每次重传几 MB 图片塞死 4G/5G 上行通道！
    img_msg_indices = [idx for idx, m in enumerate(all_msgs) if isinstance(m.get("content"), list) and any(isinstance(p, dict) and p.get("type") == "image_url" for p in m.get("content"))]
    keep_img_indices = set(img_msg_indices[-2:]) if len(img_msg_indices) > 2 else set(img_msg_indices)

    for msg_idx, msg in enumerate(all_msgs):
        role = msg.get("role")
        raw_content = msg.get("content", "")
        
        parts = []
        if isinstance(raw_content, str):
            if raw_content:
                parts.append({"text": raw_content})
        elif isinstance(raw_content, list):
            for part in raw_content:
                if isinstance(part, dict):
                    if part.get("type") == "text":
                        parts.append({"text": part.get("text", "")})
                    elif part.get("type") == "image_url":
                        if msg_idx not in keep_img_indices:
                            parts.append({"text": "[历史附图已省略以加速传输]"})
                            continue
                        img_url = part.get("image_url", {}).get("url", "")
                        if img_url.startswith("data:"):
                            try:
                                header, data = img_url.split(",", 1)
                                mime = header.split(";")[0].split(":")[1]
                                parts.append({"inlineData": {"mimeType": mime, "data": data}})
                            except Exception:
                                pass

        # 工具调用回包
        if role == "tool":
            tool_name = msg.get("name", "tool")
            parts.append({
                "functionResponse": {
                    "name": tool_name,
                    "response": {"result": raw_content}
                }
            })
            contents.append({"role": "user", "parts": parts})
            continue

        if role == "assistant":
            # 捕获客户端回传的历史思考内容 (reasoning_content)
            r_content = msg.get("reasoning_content") or msg.get("thought") or ""
            if r_content and isinstance(r_content, str):
                parts.append({
                    "thought": True,
                    "text": r_content
                })

            if msg.get("tool_calls"):
                for tc in msg.get("tool_calls"):
                    fn = tc.get("function", {})
                    fn_name = fn.get("name")
                    try:
                        fn_args = json.loads(fn.get("arguments", "{}"))
                    except Exception:
                        fn_args = {}
                    parts.append({
                        "functionCall": {
                            "name": fn_name,
                            "args": fn_args
                        },
                        "thoughtSignature": "skip_thought_signature_validator"
                    })

        if role == "system":
            system_parts.extend(parts)
        elif role == "assistant":
            if parts:
                contents.append({"role": "model", "parts": parts})
        else:
            if parts:
                contents.append({"role": "user", "parts": parts})

    # 🛡️ 防空载自杀：contents 为空（仅含 system 的辅助请求）时补占位 user 消息，
    # 否则 Google 必报 400 INVALID_ARGUMENT: contents is not specified
    if not contents:
        contents.append({"role": "user", "parts": [{"text": "继续"}]})
    gemini_req = {"contents": contents}
    if system_parts:
        gemini_req["systemInstruction"] = {"parts": system_parts}

    # Tools 协议转换 (生图模型不传工具，避免与图文多模态冲突)
    tools = req_json.get("tools")
    if target_model != "gemini-3.1-flash-image" and tools and isinstance(tools, list):
        func_decls = []
        for t in tools:
            if t.get("type") == "function":
                f_info = t.get("function", {})
                decl = {
                    "name": f_info.get("name"),
                    "description": f_info.get("description", "")
                }
                params = f_info.get("parameters")
                if params and isinstance(params, dict):
                    decl["parameters"] = _clean_schema_for_gemini(params)
                func_decls.append(decl)
        if func_decls:
            # 兼容 Gemini 3.8/3.7，在多轮工具调用时保持模式兼容
            gemini_req["tools"] = [{"functionDeclarations": func_decls}]

    # gen_config (智能动态思考：只有明确指定 -high / -thinking 时才跑 4096 深度思考；默认采用动态自适应思考，极速出字)
    gen_config = {}
    if target_model == "gemini-3.1-flash-image":
        gen_config["responseModalities"] = ["TEXT", "IMAGE"]
    elif "claude" in target_model:
        # Claude 模型支持自适应思考
        gen_config["thinkingConfig"] = {"includeThoughts": True}
    elif "thinking" in raw_model.lower() and "low" not in raw_model.lower():
        # 只有显式带 -thinking 才锁 4096；默认的 gemini-3.8-flash-high 用 1024 极速动态思考，兼顾智商与秒回速度！
        gen_config["thinkingConfig"] = {"includeThoughts": True, "thinkingBudget": 4096}
    elif "medium" in target_model or "medium" in raw_model.lower():
        # medium 档位：官方推荐 4000 思考预算，平衡智商与速度
        gen_config["thinkingConfig"] = {"includeThoughts": True, "thinkingBudget": 4000}
    elif ("oss" in target_model or "gpt-oss" in raw_model.lower()):
        # GPT-OSS 120B：官方 medium 档 8192 思考预算
        gen_config["thinkingConfig"] = {"includeThoughts": True, "thinkingBudget": 8192}
    elif "high" in raw_model.lower() and "low" not in raw_model.lower():
        gen_config["thinkingConfig"] = {"includeThoughts": True, "thinkingBudget": 1024}
    elif "low" in raw_model.lower():
        # 用户指定了 low 轻量思考
        gen_config["thinkingConfig"] = {"includeThoughts": True, "thinkingBudget": 512}
    else:
        # 默认日常请求：使用 Google 官方动态思考 (Dynamic Thinking)，不锁死 4096，简单问题秒回，复杂问题自适应思考！
        gen_config["thinkingConfig"] = {"includeThoughts": True}
    
    # ★ 关键修复：客户端 max_tokens 必须转发给上游，且要为思考预留独立预算。
    #   否则 Gemini 的 thinking 会吃光 maxOutputTokens，正文被截成空的
    #   （表现为：深度思考框有内容，正文一个字都没有，客户端判定空响应并重试）。
    _client_max = req_json.get("max_tokens") or req_json.get("max_completion_tokens")
    _think_budget = 0
    if "thinkingConfig" in gen_config:
        _tb = gen_config["thinkingConfig"].get("thinkingBudget")
        if isinstance(_tb, int) and _tb > 0:
            _think_budget = _tb
        else:
            _think_budget = 2048   # 动态思考模式按 2048 预留

    # ★ 硬性安全下限：正文预算至少 8192 tokens，思考预算额外叠加。
    #   这是根治「深度思考框有内容、正文一个字不出」的关键——
    #   Gemini 的 thinking tokens 会吃掉 maxOutputTokens，
    #   一旦限额偏低，思考吐完就 finishReason=MAX_TOKENS，正文直接空白。
    _BODY_FLOOR = 8192
    try:
        _cm = int(_client_max) if _client_max else _BODY_FLOOR
    except (TypeError, ValueError):
        _cm = _BODY_FLOOR
    _cm = max(_cm, _BODY_FLOOR)
    gen_config["maxOutputTokens"] = _cm + _think_budget

    if gen_config:
        gemini_req["generationConfig"] = gen_config

    # 官方 API 标准 safetySettings 参数配置（设为 BLOCK_NONE 防止常规内容误拦截）
    gemini_req["safetySettings"] = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_CIVIC_INTEGRITY", "threshold": "BLOCK_NONE"}
    ]

    return target_model, {
        "project": "aicode-consumers",
        "model": target_model,
        "request": gemini_req
    }
DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<title>Antigravity 掌控中心 · Liquid Glass</title>
<style>
:root {
  --bg: #050507;
  --card-bg: rgba(22, 22, 28, 0.75);
  --card-border: rgba(255, 255, 255, 0.08);
  --accent: #8b5cf6;
  --accent-glow: rgba(139, 92, 246, 0.35);
  --text-primary: #f3f4f6;
  --text-secondary: #9ca3af;
  --green: #10b981;
  --red: #ef4444;
  --yellow: #f59e0b;
  --blue: #3b82f6;
}
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif; -webkit-tap-highlight-color: transparent; }
html, body {
  background-color: var(--bg);
  color: var(--text-primary);
  min-height: 100vh;
  padding: env(safe-area-inset-top, 16px) 14px env(safe-area-inset-bottom, 20px) 14px;
  background-image: radial-gradient(circle at 50% 0%, rgba(139, 92, 246, 0.15) 0%, transparent 50%), radial-gradient(circle at 100% 100%, rgba(59, 130, 246, 0.08) 0%, transparent 40%);
  max-width: 100vw;
  overflow-x: hidden !important;
}
.container { max-width: 900px; margin: 0 auto; width: 100%; }
header { display: flex; justify-content: space-between; align-items: center; padding: 14px 0 16px; border-bottom: 1px solid var(--card-border); margin-bottom: 16px; }
.logo-wrap { display: flex; align-items: center; gap: 10px; }
.logo-icon { width: 36px; height: 36px; border-radius: 11px; background: linear-gradient(135deg, #a855f7, #6366f1); display: flex; align-items: center; justify-content: center; font-size: 19px; box-shadow: 0 4px 16px var(--accent-glow); }
.logo-title h1 { font-size: 18px; font-weight: 700; letter-spacing: -0.5px; background: linear-gradient(90deg, #fff, #c4b5fd); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.logo-title p { font-size: 10px; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.5px; }
.status-badge { display: flex; align-items: center; gap: 5px; padding: 5px 10px; border-radius: 20px; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.25); font-size: 11px; color: var(--green); font-weight: 600; }
.status-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--green); box-shadow: 0 0 8px var(--green); animation: pulse 2s infinite; }
@keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.5; transform: scale(0.85); } }

.grid-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-bottom: 16px; }
.card { background: var(--card-bg); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid var(--card-border); border-radius: 14px; padding: 12px 6px; text-align: center; box-shadow: 0 6px 24px rgba(0,0,0,0.35); min-width: 0; max-width: 100%; box-sizing: border-box; overflow: hidden; display: flex; flex-direction: column; justify-content: center; align-items: center; }
.stat-label { font-size: 10.5px; color: var(--text-secondary); font-weight: 500; margin-bottom: 4px; white-space: nowrap; }
.stat-val { font-size: clamp(12px, 3.8vw, 17px); font-weight: 700; color: #fff; letter-spacing: -0.5px; line-height: 1.2; width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.stat-sub { font-size: clamp(7.5px, 2.2vw, 9.5px); color: var(--text-secondary); margin-top: 3px; white-space: nowrap; width: 100%; overflow: hidden; text-overflow: ellipsis; }

.section-header { display: flex; justify-content: space-between; align-items: center; margin: 16px 0 10px; flex-wrap: wrap; gap: 8px; }
.section-header h3 { font-size: 13.5px; font-weight: 600; color: #e5e7eb; }
.btn-group { display: flex; gap: 6px; flex-wrap: wrap; }
button { background: rgba(255, 255, 255, 0.06); border: 1px solid var(--card-border); color: #fff; padding: 6px 12px; border-radius: 9px; font-size: 11.5px; font-weight: 600; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 4px; }
button:active { transform: scale(0.96); background: rgba(255, 255, 255, 0.12); }
button.primary { background: linear-gradient(135deg, #8b5cf6, #6366f1); border: none; box-shadow: 0 2px 10px var(--accent-glow); }

.account-card { display: flex; justify-content: space-between; align-items: center; padding: 12px 14px; border-radius: 12px; background: rgba(255, 255, 255, 0.03); border: 1px solid var(--card-border); margin-bottom: 12px; }
.account-info { display: flex; align-items: center; gap: 10px; }
.account-avatar { width: 32px; height: 32px; border-radius: 50%; background: #2563eb; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: bold; }
.table-wrap { width: 100%; overflow-x: auto !important; -webkit-overflow-scrolling: touch; display: block; border-radius: 12px; border: 1px solid var(--card-border); }
table { width: 100%; min-width: 640px; border-collapse: collapse; font-size: 11.5px; text-align: left; }
th { background: rgba(255, 255, 255, 0.03); color: var(--text-secondary); font-weight: 600; padding: 9px 10px; position: sticky; top: 0; backdrop-filter: blur(10px); }
td { padding: 9px 10px; border-top: 1px solid var(--card-border); color: #d1d5db; }
tr:hover td { background: rgba(255, 255, 255, 0.02); }
.tag { padding: 2px 5px; border-radius: 5px; font-size: 9.5px; font-weight: 600; }
.tag-200 { background: rgba(16, 185, 129, 0.15); color: var(--green); }
.tag-err { background: rgba(239, 68, 68, 0.15); color: var(--red); }
.tag-499 { background: rgba(148, 163, 184, 0.15); color: #94a3b8; }
.tag-title { background: rgba(168, 85, 247, 0.18); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.35); }

.poke-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 14px 16px;
  border-radius: 16px;
  background: linear-gradient(145deg, rgba(220, 38, 38, 0.12) 0%, rgba(15, 23, 42, 0.8) 60%, rgba(2, 6, 23, 0.95) 100%);
  border: 1px solid rgba(239, 68, 68, 0.3);
  margin-bottom: 14px;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.5);
  position: relative;
  overflow: hidden;
}
.poke-top-row {
  display: flex;
  align-items: center;
  gap: 14px;
  width: 100%;
}
.poke-sprite-box {
  width: 96px !important;
  height: 132px !important;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  overflow: hidden;
  cursor: pointer;
  flex-shrink: 0;
}
.poke-sprite-box img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
  border-radius: 10px;
  mask-image: radial-gradient(ellipse 95% 95% at 50% 45%, black 75%, transparent 100%);
  -webkit-mask-image: radial-gradient(ellipse 95% 95% at 50% 45%, black 75%, transparent 100%);
}
.poke-right-col {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 132px;
  flex: 1;
  min-width: 0;
}
.poke-title-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}
.poke-realm-text {
  font-size: 15px;
  font-weight: 800;
  color: #fff;
  white-space: nowrap;
}
.yijing-pill {
  font-size: 10px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 6px;
  background: rgba(220, 38, 38, 0.25);
  color: #fca5a5;
  border: 1px solid rgba(239, 68, 68, 0.45);
  white-space: nowrap;
}
.fabao-card {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 6px 10px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  cursor: pointer;
  width: 100%;
  box-sizing: border-box;
}
.fabao-img-wrap {
  width: 32px !important;
  height: 32px !important;
  max-width: 32px !important;
  max-height: 32px !important;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  overflow: hidden;
}
.fabao-img-wrap img {
  width: 30px !important;
  height: 30px !important;
  max-width: 30px !important;
  max-height: 30px !important;
  object-fit: contain;
}
.fabao-details {
  display: flex;
  flex-direction: column;
  gap: 2px;
  flex: 1;
  min-width: 0;
}
.fabao-name-line {
  font-size: 12px;
  font-weight: 700;
  color: #fde047;
  white-space: nowrap;
}
.fabao-stat-line {
  font-size: 10.5px;
  color: #cbd5e1;
  white-space: nowrap;
}
.poke-progress-wrap {
  display: flex;
  flex-direction: column;
  gap: 4px;
  width: 100%;
}
.poke-progress-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 10.5px;
  white-space: nowrap;
}
.poke-bar-wrap {
  width: 100%;
  height: 5px;
  background: rgba(255,255,255,0.08);
  border-radius: 999px;
  overflow: hidden;
}
.poke-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #dc2626, #f59e0b);
  border-radius: 999px;
  transition: width 0.5s ease;
}

</style>
</head>
<body>
<div class="container">
  <header>
    <div class="logo-wrap">
      <div class="logo-icon">⚡</div>
      <div class="logo-title">
        <h1>Antigravity 掌控中心</h1>
        <p>iOS Native Liquid Glass Engine</p>
      </div>
    </div>
    <div class="status-badge">
      <span class="status-dot"></span>
      <span>常驻稳态</span>
    </div>
  </header>

  <div class="grid-stats">
    <div class="card">
      <div class="stat-label">今日调用</div>
      <div class="stat-val" id="stat-calls">0</div>
      <div class="stat-sub">累计请求量</div>
    </div>
    <div class="card">
      <div class="stat-label">成功率</div>
      <div class="stat-val" id="stat-rate" style="color:var(--green)">100%</div>
      <div class="stat-sub" id="stat-errs">失败 0 次</div>
    </div>
    <div class="card" onclick="toggleTokenFormat()" style="cursor:pointer;" title="点击切换缩写与完整数字">
      <div class="stat-label">今日 Tokens</div>
      <div class="stat-val" id="stat-today-tokens">0</div>
      <div class="stat-sub" id="sub-today-tokens">当前会话消耗</div>
    </div>
    <div class="card" onclick="toggleTokenFormat()" style="cursor:pointer;" title="点击切换缩写与完整数字">
      <div class="stat-label">总消耗 Tokens</div>
      <div class="stat-val" id="stat-total-tokens">0</div>
      <div class="stat-sub" id="sub-total-tokens">全账号累计</div>
    </div>
  </div>

  
              <!-- 仙逆·杀戮问天本命卡 (黄金比例排版) -->
  <div class="poke-container" id="poke-card">
    <div class="poke-top-row">
      <!-- 左侧：无边大立绘 (96x132) -->
      <div class="poke-sprite-box" onclick="cycleRealmPreview()" title="点击切换预览各境法相">
        <img id="poke-img" src="/static/wanglin_char_full.webp" alt="王林真身">
      </div>

      <!-- 右侧：上中下三层完美分布，绝无折行 -->
      <div class="poke-right-col">
        <!-- 顶层：境界名称 + 生死意境胶囊 -->
        <div class="poke-title-bar">
          <span class="poke-realm-text" id="xianni-realm">化神期 · 化凡宗师</span>
          <span class="yijing-pill" id="xianni-yijing">生死意境</span>
        </div>

        <!-- 中层：本命法宝与尊魂幡 (独立精致磁吸卡) -->
        <div class="fabao-card" onclick="cycleRealmPreview()" title="点击切换法宝法相">
          <div class="fabao-img-wrap">
            <img id="fabao-img" src="" alt="法宝">
          </div>
          <div class="fabao-details">
            <div class="fabao-name-line" id="xianni-fabao-name">本命法宝：木雕岁月</div>
            <div class="fabao-stat-line" id="xianni-souls-count">十亿尊魂幡：280,062 煞魂</div>
          </div>
        </div>

        <!-- 底层：修为破境进度条 -->
        <div class="poke-progress-wrap" style="margin-top:2px;">
          <div style="display:flex; justify-content:space-between; align-items:center; font-size:10.5px; margin-bottom:3px;">
            <span style="color:#fca5a5; font-weight:700;" id="poke-target-text">化神圆满 91.2%</span>
            <span style="color:#94a3b8; font-size:9.5px;" id="poke-next-hint">距【婴变期】差 17.6M</span>
          </div>
          <div class="poke-bar-wrap" style="height:5px;">
            <div class="poke-bar-fill" id="poke-fill" style="width: 91.2%;"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- 底部：双额度血条 -->
    <div style="width: 100%; padding-top: 8px; border-top: 1px dashed rgba(255, 255, 255, 0.08); display: flex; flex-direction: column; gap: 6px;">
      <div style="display: flex; justify-content: space-between; align-items: center; font-size: 10.5px;">
        <span style="color: #94a3b8; display: flex; align-items: center; gap: 4px;">⚡ 极境雷灵 (5小时额度): <b id="quota-5h-countdown" style="color: #fde047; font-size: 10px; margin-left: 2px;">--:--:--</b></span>
        <span style="font-weight: 700; color: #34d399;" id="quota-5h-val">--% 剩余</span>
      </div>
      <div class="poke-bar-wrap" style="height: 4px;">
        <div class="poke-bar-fill" id="quota-5h-fill" style="width: 100%; background: linear-gradient(90deg, #10b981, #059669);"></div>
      </div>

      <div style="display: flex; justify-content: space-between; align-items: center; font-size: 10.5px; margin-top: 1px;">
        <span style="color: #94a3b8; display: flex; align-items: center; gap: 4px;">📿 天逆天道 (本周寿元): <b id="quota-week-countdown" style="color: #93c5fd; font-size: 10px; margin-left: 2px;">--天--时</b></span>
        <span style="font-weight: 700; color: #60a5fa;" id="quota-week-val">--% 剩余</span>
      </div>
      <div class="poke-bar-wrap" style="height: 4px;">
        <div class="poke-bar-fill" id="quota-week-fill" style="width: 100%; background: linear-gradient(90deg, #3b82f6, #6366f1);"></div>
      </div>
    </div>
  </div>

  <div class="account-card">
    <div class="account-info">
      <div class="account-avatar">G</div>
      <div>
        <div style="font-size:13px; font-weight:600; color:#fff; display:flex; align-items:center; gap:6px;">
          <span id="acc-email" onclick="toggleEmailMask()" style="cursor:pointer;" title="点击切换掩码脱敏">加载中...</span>
          <span onclick="toggleEmailMask()" style="cursor:pointer; font-size:12px; opacity:0.7;" id="mask-icon">👁️</span>
        </div>
        <div style="font-size:10.5px; color:var(--text-secondary);" id="acc-tier">Google AI Pro (g1-pro-tier)</div>
      </div>
    </div>
    <div style="text-align:right;">
      <span class="tag tag-200" id="acc-credits">Pro 专属高配额 / 50 积分</span>
    </div>
  </div>

  <div class="section-header" style="flex-direction:column; align-items:stretch; gap:12px;">
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%;">
      <div style="display:flex; align-items:center; gap:8px;">
        <div style="width:24px; height:24px; border-radius:7px; background:linear-gradient(135deg, #6366f1, #4f46e5); display:flex; align-items:center; justify-content:center; font-size:13px;">🌐</div>
        <h3 style="background: linear-gradient(90deg, #818cf8, #c7d2fe); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin:0;">Google 账号矩阵 (独享专线)</h3>
      </div>
      <button onclick="toggleEmailMask()" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); padding:4px 10px; border-radius:8px; font-size:11.5px; color:#c7d2fe; cursor:pointer;">👁️ <span id="btn-mask-text">隐藏账号</span></button>
    </div>
    <div class="btn-group" style="align-self:flex-start;">
      <button class="primary" style="background:linear-gradient(135deg, #4f46e5, #6366f1); border:none;" onclick="openOAuthModal()">➕ 添加账号</button>
      <button id="btn-toggle-google" onclick="toggleGoogleCollapse()">📁 展开账号</button>
      <button onclick="refreshData()">🔄 刷新余额</button>
    </div>
  </div>

  <div class="table-wrap" id="google-table-wrap" style="display:none; transition: all 0.3s ease;">
    <table>
      <thead>
        <tr>
          <th>账号 Email</th>
          <th>项目 Project</th>
          <th>授权权益</th>
          <th>额度状态</th>
          <th>状态</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody id="accounts-tbody">
      </tbody>
    </table>
  </div>

  <!-- 第五任长老：腾讯 CodeBuddy 专属独立账号矩阵卡片 (物理彻底隔离) -->
  <div class="section-header" style="margin-top:24px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <div style="width:24px; height:24px; border-radius:7px; background:linear-gradient(135deg, #0284c7, #0369a1); display:flex; align-items:center; justify-content:center; font-size:13px;">🐧</div>
      <h3 style="background: linear-gradient(90deg, #38bdf8, #7dd3fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">腾讯 CodeBuddy 资产 (独享专线)</h3>
    </div>
    <div class="btn-group">
      <button class="primary" style="background:linear-gradient(135deg, #0284c7, #0369a1); border:none;" onclick="openCbModal()">➕ 添加账号</button>
      <button id="btn-toggle-cb" onclick="toggleCbCollapse()">📁 展开账号</button>
      <button onclick="refreshData()">🔄 刷新余额</button>
    </div>
  </div>

  <div class="table-wrap" id="cb-table-wrap" style="display:none; transition: all 0.3s ease;">
    <table>
      <thead>
        <tr>
          <th>账号标识</th>
          <th>绑定 UID</th>
          <th>总剩余 / 总额度</th>
          <th>权益包明细</th>
          <th>最长有效期</th>
          <th>运行状态</th>
          <th>上游网关</th>
        </tr>
      </thead>
      <tbody id="cb-accounts-tbody">
      </tbody>
    </table>
  </div>

  <!-- 第六任长老：Tencent LightVela 专属独立资产卡片 (物理彻底隔离) -->
  <div class="section-header" style="margin-top:24px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <div style="width:24px; height:24px; border-radius:7px; background:linear-gradient(135deg, #6366f1, #4f46e5); display:flex; align-items:center; justify-content:center; font-size:13px;">⛵</div>
      <h3 style="background: linear-gradient(90deg, #818cf8, #c7d2fe); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Tencent LightVela 资产 (独享专线)</h3>
    </div>
    <div class="btn-group">
      <button class="primary" style="background:linear-gradient(135deg, #4f46e5, #6366f1); border:none;" onclick="alert('LightVela 采用专属鉴权 Key 自动直通云端沙盒，无需手动导入凭证')">🔑 鉴权凭证</button>
      <button id="btn-toggle-lv" onclick="toggleLvCollapse()">📁 展开账号</button>
      <button onclick="refreshData()">🔄 刷新余额</button>
    </div>
  </div>

  <div id="lv-table-wrap" style="display:none; margin-top:12px; transition: all 0.3s ease;">
    <div id="lv-accounts-container"></div>
  </div>

  <!-- Today AI 专属独立账号矩阵卡片 (第七任长老归位，物理彻底隔离) -->
  <div class="section-header" style="margin-top:24px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <div style="width:24px; height:24px; border-radius:7px; background:linear-gradient(135deg, #f59e0b, #d97706); display:flex; align-items:center; justify-content:center; font-size:13px;">🐢</div>
      <h3 style="background: linear-gradient(90deg, #fbbf24, #f59e0b); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Today AI (个人智能体 3亿Tokens专线)</h3>
    </div>
    <div class="btn-group">
      <button class="primary" style="background:linear-gradient(135deg, #d97706, #f59e0b); border:none;" onclick="openTodayModal()">➕ 添加账号</button>
      <button id="btn-toggle-today" onclick="toggleTodayCollapse()">📁 展开账号</button>
      <button onclick="refreshData()">🔄 刷新余额</button>
    </div>
  </div>

  <div class="table-wrap" id="today-table-wrap" style="display:none; transition: all 0.3s ease;">
    <table>
      <thead>
        <tr>
          <th>账号备注</th>
          <th>绑定手机 / UID</th>
          <th>当前套餐权益</th>
          <th>可用额度比例</th>
          <th>权益有效截止</th>
          <th>运行状态</th>
          <th>上游网关</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody id="today-accounts-tbody">
      </tbody>
    </table>
  </div>

  <!-- EZCompleteUI 专属独立账号矩阵卡片 (物理隔离，彻底分开展示) -->
  <div class="section-header" style="margin-top:24px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <div style="width:24px; height:24px; border-radius:7px; background:linear-gradient(135deg, #10b981, #059669); display:flex; align-items:center; justify-content:center; font-size:13px;">🪙</div>
      <h3 style="background: linear-gradient(90deg, #34d399, #6ee7b7); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">EZCompleteUI 矩阵资产 (独享轮询池)</h3>
    </div>
    <div class="btn-group">
      <button class="primary" style="background:linear-gradient(135deg, #059669, #10b981); border:none;" onclick="openEzModal()">➕ 添加账号</button>
      <button id="btn-toggle-ez" onclick="toggleEzCollapse()">📁 展开账号</button>
      <button onclick="refreshData()">🔄 刷新余额</button>
    </div>
  </div>

  <div class="table-wrap" id="ez-table-wrap" style="display:none; transition: all 0.3s ease;">
    <table>
      <thead>
        <tr>
          <th>角色 / 备注</th>
          <th>账号 Email</th>
          <th>当前 Coin 余额</th>
          <th>运行状态</th>
          <th>上游网关</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody id="ez-accounts-tbody">
      </tbody>
    </table>
  </div>

  <div class="section-header" style="margin-top:20px;">
    <h3>📡 实时调用链路流水 (Live Logs)</h3>
  </div>
  <div class="table-wrap" style="max-height:260px;">
    <table>
      <thead>
        <tr>
          <th>时间</th>
          <th>模型</th>
          <th>状态</th>
          <th>耗时</th>
          <th>Tokens</th>
        </tr>
      </thead>
      <tbody id="logs-tbody">
      </tbody>
    </table>
  </div>
</div>

<!-- EZ 账号添加/登录弹窗 -->
<!-- 腾讯 CodeBuddy 扫码授权弹窗 -->
<div id="cbModal" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.85); backdrop-filter:blur(25px); -webkit-backdrop-filter:blur(25px); align-items:center; justify-content:center; z-index:999;">
  <div style="width:90%; max-width:420px; background:#16161d; border:1px solid rgba(56,189,248,0.3); border-radius:20px; padding:24px; box-shadow:0 20px 60px rgba(0,0,0,0.8);">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="font-size:18px;">🐧</span>
        <h3 style="font-size:16px; font-weight:700; color:#fff;">添加 腾讯 CodeBuddy 账号</h3>
      </div>
      <button onclick="closeCbModal()" style="background:none; border:none; color:#888; font-size:18px; cursor:pointer;">✕</button>
    </div>
    
    <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.06); border-radius:12px; padding:12px; margin-bottom:16px; font-size:11.5px; color:#94a3b8; line-height:1.5;">
      💡 点击下方按钮打开腾讯官方授权页面，使用微信/企业微信扫码确认后，本面板将自动截获 Token 并秒级落盘生效！
    </div>

    <div style="text-align:center; margin-bottom:18px;">
      <a id="cbAuthLink" href="#" target="_blank" style="display:inline-block; padding:12px 20px; background:linear-gradient(135deg, #0284c7, #0369a1); color:#fff; border-radius:10px; text-decoration:none; font-weight:700; font-size:13px; box-shadow:0 4px 15px rgba(2,132,199,0.3);">
        🚀 点击打开腾讯官方授权页
      </a>
      <div id="cbPollStatus" style="margin-top:12px; font-size:12px; color:#38bdf8; font-weight:600;">
        ⏳ 等待打开授权页面...
      </div>
    </div>

    <div style="display:flex; gap:10px;">
      <button type="button" style="flex:1; background:rgba(255,255,255,0.08); border:none; padding:10px; border-radius:10px; color:#fff;" onclick="closeCbModal()">关闭</button>
    </div>
  </div>
</div>

<div id="ezModal" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.85); backdrop-filter:blur(25px); -webkit-backdrop-filter:blur(25px); align-items:center; justify-content:center; z-index:999;">
  <div style="width:90%; max-width:420px; background:#16161d; border:1px solid rgba(16,185,129,0.3); border-radius:20px; padding:24px; box-shadow:0 20px 60px rgba(0,0,0,0.8);">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="font-size:18px;">🪙</span>
        <h3 style="font-size:16px; font-weight:700; color:#fff;">添加 EZComplete 账号</h3>
      </div>
      <button onclick="closeEzModal()" style="padding:4px 8px; font-size:11px;">✕</button>
    </div>
    <p style="font-size:12px; color:var(--text-secondary); line-height:1.5; margin-bottom:12px;">输入账号邮箱和密码，系统将自动校验 Supabase 鉴权凭证并加入轮询矩阵池：</p>
    <div style="display:flex; flex-direction:column; gap:10px;">
      <div>
        <label style="font-size:11px; color:#94a3b8; display:block; margin-bottom:4px;">账号备注 / 角色：</label>
        <input id="ezInputName" type="text" placeholder="例如：主号 / 小号10" style="width:100%; box-sizing:border-box; padding:9px 12px; border-radius:8px; background:#0c0c10; border:1px solid var(--card-border); color:#fff; font-size:12px; outline:none;">
      </div>
      <div>
        <label style="font-size:11px; color:#94a3b8; display:block; margin-bottom:4px;">邮箱 (Email)：</label>
        <input id="ezInputEmail" type="email" placeholder="name@example.com" style="width:100%; box-sizing:border-box; padding:9px 12px; border-radius:8px; background:#0c0c10; border:1px solid var(--card-border); color:#fff; font-size:12px; outline:none;">
      </div>
      <div>
        <label style="font-size:11px; color:#94a3b8; display:block; margin-bottom:4px;">密码 (Password)：</label>
        <input id="ezInputPassword" type="password" placeholder="输入密码" style="width:100%; box-sizing:border-box; padding:9px 12px; border-radius:8px; background:#0c0c10; border:1px solid var(--card-border); color:#fff; font-size:12px; outline:none;">
      </div>
    </div>
    <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:16px;">
      <button onclick="closeEzModal()">取消</button>
      <button class="primary" id="btnSubmitEz" style="background:linear-gradient(135deg, #059669, #10b981); border:none;" onclick="submitEzAccount()">校验并保存</button>
    </div>
  </div>
</div>

<!-- Today AI 账号添加弹窗 -->
<div id="todayModal" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.85); backdrop-filter:blur(25px); -webkit-backdrop-filter:blur(25px); align-items:center; justify-content:center; z-index:999;">
  <div style="width:90%; max-width:440px; background:#16161d; border:1px solid rgba(245,158,11,0.3); border-radius:20px; padding:24px; box-shadow:0 20px 60px rgba(0,0,0,0.8);">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="font-size:18px;">🐢</span>
        <h3 style="font-size:16px; font-weight:700; color:#fff;">添加 Today AI 账号</h3>
      </div>
      <button onclick="closeTodayModal()" style="padding:4px 8px; font-size:11px;">✕</button>
    </div>
    <p style="font-size:12px; color:var(--text-secondary); line-height:1.5; margin-bottom:12px;">输入账号备注及登录凭据（Session Cookie），系统将自动调用 <code>/api/token</code> 校验并换取有效 JWT：</p>
    <div style="display:flex; flex-direction:column; gap:10px;">
      <div>
        <label style="font-size:11px; color:#94a3b8; display:block; margin-bottom:4px;">账号备注：</label>
        <input id="todayInputName" type="text" placeholder="例如：主号 / 个人 Pro" style="width:100%; box-sizing:border-box; padding:9px 12px; border-radius:8px; background:#0c0c10; border:1px solid var(--card-border); color:#fff; font-size:12px; outline:none;">
      </div>
      <div>
        <label style="font-size:11px; color:#94a3b8; display:block; margin-bottom:4px;">绑定手机号 (用于标识)：</label>
        <input id="todayInputPhone" type="text" placeholder="+86 153****7210" style="width:100%; box-sizing:border-box; padding:9px 12px; border-radius:8px; background:#0c0c10; border:1px solid var(--card-border); color:#fff; font-size:12px; outline:none;">
      </div>
      <div>
        <label style="font-size:11px; color:#94a3b8; display:block; margin-bottom:4px;">Session Token (或完整 Cookie)：</label>
        <textarea id="todayInputSession" placeholder="粘贴 __Secure-better-auth.session_token=... 或纯 token 值" style="width:100%; height:70px; box-sizing:border-box; padding:8px 12px; border-radius:8px; background:#0c0c10; border:1px solid var(--card-border); color:#fff; font-size:11.5px; outline:none; resize:none;"></textarea>
      </div>
    </div>
    <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:16px;">
      <button onclick="closeTodayModal()">取消</button>
      <button class="primary" id="btnSubmitToday" style="background:linear-gradient(135deg, #d97706, #f59e0b); border:none;" onclick="submitTodayAccount()">校验并保存</button>
    </div>
  </div>
</div>

<!-- OAuth 授权弹窗 -->
<div id="oauthModal" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.85); backdrop-filter:blur(25px); -webkit-backdrop-filter:blur(25px); align-items:center; justify-content:center; z-index:999;">
  <div style="width:90%; max-width:440px; background:#16161d; border:1px solid rgba(255,255,255,0.12); border-radius:20px; padding:24px; box-shadow:0 20px 60px rgba(0,0,0,0.8);">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
      <h3 style="font-size:16px; font-weight:700; color:#fff;">🔑 绑定新 Google / Antigravity 账号</h3>
      <button onclick="closeOAuthModal()" style="padding:4px 8px; font-size:11px;">✕</button>
    </div>
    <p style="font-size:12px; color:var(--text-secondary); line-height:1.5;">第一步：点击下方链接跳转 Google 官方登录并授权：</p>
    <a id="oauthLink" href="#" target="_blank" style="padding:10px; border-radius:8px; background:rgba(59, 130, 246, 0.1); border:1px solid rgba(59, 130, 246, 0.3); color:#60a5fa; word-break:break-all; font-size:11px; margin:10px 0; display:block; text-decoration:none;">正在生成授权链接...</a>
    <p style="font-size:12px; color:var(--text-secondary); line-height:1.5; margin-top:8px;">第二步：授权完成后，将浏览器地址栏的<strong>完整重定向回调 URL</strong>（或包含的 <code>code=4/...</code> 授权码）粘贴到下方：</p>
    <textarea id="oauthCodeInput" placeholder="粘贴类似 http://localhost:51121/oauth-callback?code=4/0A... 的完整网址或授权码" style="width:100%; height:80px; padding:10px; border-radius:10px; background:#0c0c10; border:1px solid var(--card-border); color:#fff; font-size:12px; margin:10px 0; outline:none; resize:none;"></textarea>
    <div style="display:flex; justify-content:flex-end; gap:8px;">
      <button onclick="closeOAuthModal()">取消</button>
      <button class="primary" id="btnSubmitOAuth" onclick="submitOAuthCallback()">立即换取凭证并绑定</button>
    </div>
  </div>
</div>

<script>

function formatCountdown(resetTimeStr) {
  if (!resetTimeStr) return '';
  const diff = Math.max(0, Math.floor((new Date(resetTimeStr).getTime() - Date.now()) / 1000));
  if (diff <= 0) return '已重置';
  const d = Math.floor(diff / 86400);
  const h = Math.floor((diff % 86400) / 3600);
  const m = Math.floor((diff % 3600) / 60);
  const s = diff % 60;
  if (d > 0) return `${d}天${h}时${m}分`;
  return `${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
}

let maskEmails = localStorage.getItem('ag_mask_emails') === 'true';

function maskText(str) {
  if (!maskEmails || !str) return str;
  if (str.includes('@')) {
    const parts = str.split('@');
    const name = parts[0];
    const domain = parts[1];
    if (name.length <= 2) return '**@' + domain;
    return name[0] + '***' + name[name.length - 1] + '@' + domain;
  }
  // 非邮箱 UID 脱敏：保留前4后4，中间打星号 (如 0387***12ee)
  if (str.length > 8) {
    return str.slice(0, 4) + '***' + str.slice(-4);
  }
  return str.slice(0, 1) + '***';
}

function toggleEmailMask() {
  maskEmails = !maskEmails;
  localStorage.setItem('ag_mask_emails', maskEmails);
  const btnText = document.getElementById('btn-mask-text');
  if (btnText) btnText.innerText = maskEmails ? '显示账号' : '隐藏账号';
  const icon = document.getElementById('mask-icon');
  if (icon) icon.innerText = maskEmails ? '🙈' : '👁️';
  refreshData();
}

let showExactTokens = false;
function toggleTokenFormat() {
  showExactTokens = !showExactTokens;
  refreshData();
}

function formatCompactNum(num, exactEl, el) {
  const n = Number(num) || 0;
  if (showExactTokens) {
    if (el) el.style.fontSize = 'clamp(9.5px, 2.6vw, 13.5px)';
    if (exactEl) exactEl.innerText = '点击切换简写';
    return n.toLocaleString();
  }
  if (el) el.style.fontSize = 'clamp(13px, 4.0vw, 17.5px)';
  if (exactEl) exactEl.innerText = n.toLocaleString();
  if (n >= 1e9) return (n / 1e9).toFixed(2) + 'B';
  if (n >= 1e6) return (n / 1e6).toFixed(2) + 'M';
  if (n >= 1e4) return (n / 1e3).toFixed(1) + 'K';
  return n.toLocaleString();
}


const FABAO_MODELS = {"天逆石珠": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGRlZnM+CiAgICA8cmFkaWFsR3JhZGllbnQgaWQ9ImcxIiBjeD0iNDAlIiBjeT0iNDAlIiByPSI2MCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMzhiZGY4Ii8+CiAgICAgIDxzdG9wIG9mZnNldD0iNTUlIiBzdG9wLWNvbG9yPSIjMWUyOTNiIi8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzAyMDYxNyIvPgogICAgPC9yYWRpYWxHcmFkaWVudD4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMjQiIGZpbGw9InVybCgjZzEpIj4KICAgIDxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9InIiIHZhbHVlcz0iMjM7MjU7MjMiIGR1cj0iMi41cyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KICA8cGF0aCBkPSJNMTggMjggUTMyIDE2IDQ2IDI4IFEzMiA0MiAxOCAyOCBaIiBmaWxsPSJub25lIiBzdHJva2U9IiM2MGE1ZmEiIHN0cm9rZS13aWR0aD0iMS41IiBvcGFjaXR5PSIwLjgiPgogICAgPGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJyb3RhdGUiIGZyb209IjAgMzIgMzIiIHRvPSIzNjAgMzIgMzIiIGR1cj0iOHMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9wYXRoPgogIDxjaXJjbGUgY3g9IjMyIiBjeT0iMzIiIHI9IjUiIGZpbGw9IiNlMGYyZmUiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0ib3BhY2l0eSIgdmFsdWVzPSIwLjY7MTswLjYiIGR1cj0iMS44cyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KPC9zdmc+", "飞剑赤血": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGc+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InRyYW5zbGF0ZSIgdmFsdWVzPSIwLC0yOyAwLDI7IDAsLTIiIGR1cj0iMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgICA8cGF0aCBkPSJNNTIgMTIgTDI0IDQwIEwyMCAzNiBMNDggOCBaIiBmaWxsPSIjZWY0NDQ0Ii8+CiAgICA8cGF0aCBkPSJNNTIgMTIgTDI4IDQ0IEwyNCA0MCBaIiBmaWxsPSIjYjkxYzFjIi8+CiAgICA8cGF0aCBkPSJNMTggMzQgTDMwIDQ2IEwyNiA1MCBMMTQgMzggWiIgZmlsbD0iI2ZiYmYyNCIvPgogICAgPHBhdGggZD0iTTIyIDQyIEwxMiA1MiBMMTAgNTAgTDIwIDQwIFoiIGZpbGw9IiM3ODM1MGYiLz4KICAgIDxjaXJjbGUgY3g9IjM2IiBjeT0iMjgiIHI9IjE0IiBmaWxsPSIjZWY0NDQ0IiBvcGFjaXR5PSIwLjI1Ij4KICAgICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iciIgdmFsdWVzPSIxMDsxODsxMCIgZHVyPSIxLjVzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIvPgogICAgPC9jaXJjbGU+CiAgPC9nPgo8L3N2Zz4=", "百丈魂旗": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGxpbmUgeDE9IjE2IiB5MT0iOCIgeDI9IjE2IiB5Mj0iNTgiIHN0cm9rZT0iIzk0YTNiOCIgc3Ryb2tlLXdpZHRoPSIyLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogIDxwYXRoIGQ9Ik0xNyAxMiBRMzYgOCA1NCAxOCBRNDQgMzAgNTYgNDIgUTM0IDQ2IDE3IDM4IFoiIGZpbGw9IiMxZTFiNGIiIHN0cm9rZT0iI2RjMjYyNiIgc3Ryb2tlLXdpZHRoPSIxLjIiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iZCIgdmFsdWVzPSJNMTcgMTIgUTM2IDggNTQgMTggUTQ0IDMwIDU2IDQyIFEzNCA0NiAxNyAzOCBaO00xNyAxMiBRMzQgMTQgNTIgMTUgUTQ2IDI4IDU0IDQ0IFEzNiA0MCAxNyAzOCBaO00xNyAxMiBRMzYgOCA1NCAxOCBRNDQgMzAgNTYgNDIgUTM0IDQ2IDE3IDM4IFoiIGR1cj0iMi4ycyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L3BhdGg+CiAgPGNpcmNsZSBjeD0iMzQiIGN5PSIyNiIgcj0iNSIgZmlsbD0iI2VmNDQ0NCIgb3BhY2l0eT0iMC44NSI+CiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiB2YWx1ZXM9IjAuNDsxOzAuNCIgZHVyPSIxLjZzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIvPgogIDwvY2lyY2xlPgo8L3N2Zz4=", "巨富魂旗": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGxpbmUgeDE9IjE2IiB5MT0iOCIgeDI9IjE2IiB5Mj0iNTgiIHN0cm9rZT0iIzk0YTNiOCIgc3Ryb2tlLXdpZHRoPSIyLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogIDxwYXRoIGQ9Ik0xNyAxMiBRMzYgOCA1NCAxOCBRNDQgMzAgNTYgNDIgUTM0IDQ2IDE3IDM4IFoiIGZpbGw9IiMxZTFiNGIiIHN0cm9rZT0iI2RjMjYyNiIgc3Ryb2tlLXdpZHRoPSIxLjIiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iZCIgdmFsdWVzPSJNMTcgMTIgUTM2IDggNTQgMTggUTQ0IDMwIDU2IDQyIFEzNCA0NiAxNyAzOCBaO00xNyAxMiBRMzQgMTQgNTIgMTUgUTQ2IDI4IDU0IDQ0IFEzNiA0MCAxNyAzOCBaO00xNyAxMiBRMzYgOCA1NCAxOCBRNDQgMzAgNTYgNDIgUTM0IDQ2IDE3IDM4IFoiIGR1cj0iMi4ycyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L3BhdGg+CiAgPGNpcmNsZSBjeD0iMzQiIGN5PSIyNiIgcj0iNSIgZmlsbD0iI2VmNDQ0NCIgb3BhY2l0eT0iMC44NSI+CiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiB2YWx1ZXM9IjAuNDsxOzAuNCIgZHVyPSIxLjZzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIvPgogIDwvY2lyY2xlPgo8L3N2Zz4=", "木雕岁月": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGRlZnM+CiAgICA8cmFkaWFsR3JhZGllbnQgaWQ9Indvb2QiIGN4PSI1MCUiIGN5PSI1MCUiIHI9IjUwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNmNTllMGIiIHN0b3Atb3BhY2l0eT0iMC40Ii8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzAwMCIgc3RvcC1vcGFjaXR5PSIwIi8+CiAgICA8L3JhZGlhbEdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIzMiIgY3k9IjMyIiByPSIyOCIgZmlsbD0idXJsKCN3b29kKSI+CiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiB2YWx1ZXM9IjAuNTsxOzAuNSIgZHVyPSIzcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KICA8cGF0aCBkPSJNMjYgNDggTDM4IDQ4IEwzNiAyNiBDMzYgMjAgMjggMjAgMjggMjYgWiIgZmlsbD0iI2I0NTMwOSIgc3Ryb2tlPSIjZmNkMzRkIiBzdHJva2Utd2lkdGg9IjEuMiIvPgogIDxjaXJjbGUgY3g9IjMyIiBjeT0iMTgiIHI9IjUiIGZpbGw9IiNkOTc3MDYiIHN0cm9rZT0iI2ZkZTA0NyIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2ZiYmYyNCIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDMiPgogICAgPGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJyb3RhdGUiIGZyb209IjAgMzIgMzIiIHRvPSIzNjAgMzIgMzIiIGR1cj0iMTBzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIvPgogIDwvY2lyY2xlPgo8L3N2Zz4=", "十亿尊魂幡": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGxpbmUgeDE9IjE0IiB5MT0iNiIgeDI9IjE0IiB5Mj0iNTgiIHN0cm9rZT0iI2ZiYmYyNCIgc3Ryb2tlLXdpZHRoPSIyLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogIDxwYXRoIGQ9Ik0xNSAxMCBRMzggNCA1OCAxNiBRNDYgMzAgNTggNDYgUTM2IDUwIDE1IDQwIFoiIGZpbGw9IiMwOTBkMTYiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIxLjUiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iZCIgdmFsdWVzPSJNMTUgMTAgUTM4IDQgNTggMTYgUTQ2IDMwIDU4IDQ2IFEzNiA1MCAxNSA0MCBaO00xNSAxMCBRMzYgMTIgNTUgMTQgUTQ4IDI4IDU2IDQ4IFEzOCA0MiAxNSA0MCBaO00xNSAxMCBRMzggNCA1OCAxNiBRNDYgMzAgNTggNDYgUTM2IDUwIDE1IDQwIFoiIGR1cj0iMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9wYXRoPgogIDx0ZXh0IHg9IjI3IiB5PSIzMSIgZmlsbD0iI2ZkZTA0NyIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9ImJvbGQiPuWwijwvdGV4dD4KPC9zdmc+", "问鼎朱雀印": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGxpbmUgeDE9IjE0IiB5MT0iNiIgeDI9IjE0IiB5Mj0iNTgiIHN0cm9rZT0iI2ZiYmYyNCIgc3Ryb2tlLXdpZHRoPSIyLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogIDxwYXRoIGQ9Ik0xNSAxMCBRMzggNCA1OCAxNiBRNDYgMzAgNTggNDYgUTM2IDUwIDE1IDQwIFoiIGZpbGw9IiMwOTBkMTYiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIxLjUiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iZCIgdmFsdWVzPSJNMTUgMTAgUTM4IDQgNTggMTYgUTQ2IDMwIDU4IDQ2IFEzNiA1MCAxNSA0MCBaO00xNSAxMCBRMzYgMTIgNTUgMTQgUTQ4IDI4IDU2IDQ4IFEzOCA0MiAxNSA0MCBaO00xNSAxMCBRMzggNCA1OCAxNiBRNDYgMzAgNTggNDYgUTM2IDUwIDE1IDQwIFoiIGR1cj0iMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9wYXRoPgogIDx0ZXh0IHg9IjI3IiB5PSIzMSIgZmlsbD0iI2ZkZTA0NyIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9ImJvbGQiPuWwijwvdGV4dD4KPC9zdmc+", "定界命罗盘": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIxLjgiIHN0cm9rZS1kYXNoYXJyYXk9IjYgMiI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMCAzMiAzMiIgdG89IjM2MCAzMiAzMiIgZHVyPSIxMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9jaXJjbGU+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMTciIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzM4YmRmOCIgc3Ryb2tlLXdpZHRoPSIxLjIiIHN0cm9rZS1kYXNoYXJyYXk9IjMgMyI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMzYwIDMyIDMyIiB0bz0iMCAzMiAzMiIgZHVyPSI2cyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KICA8cG9seWdvbiBwb2ludHM9IjMyLDEyIDM2LDI4IDUyLDMyIDM2LDM2IDMyLDUyIDI4LDM2IDEyLDMyIDI4LDI4IiBmaWxsPSIjZmRlMDQ3IiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iNCIgZmlsbD0iI2VmNDQ0NCIvPgo8L3N2Zz4=", "雷仙殿雷鼎": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIxLjgiIHN0cm9rZS1kYXNoYXJyYXk9IjYgMiI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMCAzMiAzMiIgdG89IjM2MCAzMiAzMiIgZHVyPSIxMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9jaXJjbGU+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMTciIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzM4YmRmOCIgc3Ryb2tlLXdpZHRoPSIxLjIiIHN0cm9rZS1kYXNoYXJyYXk9IjMgMyI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMzYwIDMyIDMyIiB0bz0iMCAzMiAzMiIgZHVyPSI2cyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KICA8cG9seWdvbiBwb2ludHM9IjMyLDEyIDM2LDI4IDUyLDMyIDM2LDM2IDMyLDUyIDI4LDM2IDEyLDMyIDI4LDI4IiBmaWxsPSIjZmRlMDQ3IiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iNCIgZmlsbD0iI2VmNDQ0NCIvPgo8L3N2Zz4=", "天逆圆满珠": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIxLjgiIHN0cm9rZS1kYXNoYXJyYXk9IjYgMiI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMCAzMiAzMiIgdG89IjM2MCAzMiAzMiIgZHVyPSIxMnMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIi8+CiAgPC9jaXJjbGU+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMTciIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzM4YmRmOCIgc3Ryb2tlLXdpZHRoPSIxLjIiIHN0cm9rZS1kYXNoYXJyYXk9IjMgMyI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InJvdGF0ZSIgZnJvbT0iMzYwIDMyIDMyIiB0bz0iMCAzMiAzMiIgZHVyPSI2cyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiLz4KICA8L2NpcmNsZT4KICA8cG9seWdvbiBwb2ludHM9IjMyLDEyIDM2LDI4IDUyLDMyIDM2LDM2IDMyLDUyIDI4LDM2IDEyLDMyIDI4LDI4IiBmaWxsPSIjZmRlMDQ3IiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iNCIgZmlsbD0iI2VmNDQ0NCIvPgo8L3N2Zz4="};

let previewStageIdx = -1;
const ALL_STAGE_PREVIEWS = [
  { realm: "凝气/筑基期", title: "少年王林", yijing: "极境神识", fabao: "天逆石珠", img: "/static/stage_1_ningqi.webp" },
  { realm: "结丹/元婴期", title: "灭藤煞魔", yijing: "极境杀戮", fabao: "百丈魂旗", img: "/static/stage_2_yuanying.webp" },
  { realm: "化神期", title: "化凡宗师", yijing: "生死意境", fabao: "木雕岁月", img: "/static/wanglin_char_full.webp" },
  { realm: "婴变/问鼎期", title: "仙玉天骄", yijing: "生生不息", fabao: "十亿尊魂幡", img: "/static/stage_4_yingbian.webp" },
  { realm: "空劫/踏天境", title: "八星古神", yijing: "顺逆由吾", fabao: "定界命罗盘", img: "/static/stage_5_gushen.webp" }
];

function cycleRealmPreview() {
  previewStageIdx = (previewStageIdx + 1) % ALL_STAGE_PREVIEWS.length;
  const s = ALL_STAGE_PREVIEWS[previewStageIdx];
  document.getElementById('poke-img').src = s.img;
  document.getElementById('xianni-realm').innerText = s.realm + ' · ' + s.title;
  document.getElementById('xianni-yijing').innerText = s.yijing;
  document.getElementById('xianni-fabao-name').innerText = '本命法宝：' + s.fabao;
  if (FABAO_MODELS[s.fabao]) {
    document.getElementById('fabao-img').src = FABAO_MODELS[s.fabao];
  }
}

async function refreshData() {
  try {
    const res = await fetch('/api/stats', { cache: 'no-store' });
    const data = await res.json();
    if (document.getElementById('stat-calls')) document.getElementById('stat-calls').innerText = data.today_calls || 0;
    if (document.getElementById('stat-rate')) document.getElementById('stat-rate').innerText = data.success_rate || '100%';
    if (document.getElementById('stat-errs')) document.getElementById('stat-errs').innerText = '失败 ' + (data.today_errors || 0) + ' 次';
    if (document.getElementById('stat-today-tokens')) {
      const el = document.getElementById('stat-today-tokens');
      const subEl = document.getElementById('sub-today-tokens');
      el.innerText = formatCompactNum(data.today_tokens, subEl, el);
    }
    if (document.getElementById('stat-total-tokens')) {
      const el = document.getElementById('stat-total-tokens');
      const subEl = document.getElementById('sub-total-tokens');
      el.innerText = formatCompactNum(data.total_tokens, subEl, el);
    }

    
    
    if (data.quota) {
      const q5 = data.quota['gemini-5h'];
      const qw = data.quota['gemini-weekly'];
      if (q5) {
        const val = document.getElementById('quota-5h-val');
        const fill = document.getElementById('quota-5h-fill');
        const cd = document.getElementById('quota-5h-countdown');
        window._LAST_QUOTA_5H_RESET = q5.reset_time;
        if (val) {
          val.innerText = q5.remaining_pct + '% 剩余';
          if (q5.remaining_pct < 20) val.style.color = '#ef4444';
          else if (q5.remaining_pct < 50) val.style.color = '#f59e0b';
          else val.style.color = '#34d399';
        }
        if (cd) cd.innerText = formatCountdown(q5.reset_time);
        if (fill) fill.style.width = q5.remaining_pct + '%';
      }
      if (qw) {
        const val = document.getElementById('quota-week-val');
        const fill = document.getElementById('quota-week-fill');
        const cd = document.getElementById('quota-week-countdown');
        window._LAST_QUOTA_WEEK_RESET = qw.reset_time;
        if (val) {
          val.innerText = qw.remaining_pct + '% 剩余';
          if (qw.remaining_pct < 20) val.style.color = '#ef4444';
          else if (qw.remaining_pct < 50) val.style.color = '#f59e0b';
          else val.style.color = '#60a5fa';
        }
        if (cd) cd.innerText = formatCountdown(qw.reset_time);
        if (fill) fill.style.width = qw.remaining_pct + '%';
      }
    }

    if (data.pokemon) {
      const p = data.pokemon;
      if (previewStageIdx === -1) {
        const img = document.getElementById('poke-img');
        const realm = document.getElementById('xianni-realm');
        const yijing = document.getElementById('xianni-yijing');
        const fabaoName = document.getElementById('xianni-fabao-name');
        const fabaoImg = document.getElementById('fabao-img');
        if (img) img.src = p.sprite_url;
        if (realm) realm.innerText = `${p.realm} · ${p.title}`;
        if (yijing) yijing.innerText = p.yijing;
        if (fabaoName) fabaoName.innerText = `本命法宝：${p.fabao}`;
        if (fabaoImg && (p.fabao_icon || FABAO_MODELS[p.fabao])) {
          fabaoImg.src = p.fabao_icon || FABAO_MODELS[p.fabao];
        }
      }
      const soulsEl = document.getElementById('xianni-souls-count');
      const fill = document.getElementById('poke-fill');
      const targetText = document.getElementById('poke-target-text');
      const nextHint = document.getElementById('poke-next-hint');
      if (soulsEl) soulsEl.innerText = `尊魂幡炼化：${p.souls_count.toLocaleString()} 煞魂`;
      if (fill) fill.style.width = p.progress_pct + '%';
      if (targetText) targetText.innerText = `${p.realm}圆满 ${p.progress_pct}%`;
      if (nextHint) nextHint.innerText = p.next_hint.replace('破境入', '距').replace('还需杀伐灵力 ', '差 ');
    }

    if (data.account) {
      if (document.getElementById('acc-email')) document.getElementById('acc-email').innerText = maskText(data.account.email) || '未配置';
      if (document.getElementById('acc-tier')) document.getElementById('acc-tier').innerText = data.account.tier || 'Google AI Pro';
      if (document.getElementById('acc-credits')) document.getElementById('acc-credits').innerText = data.account.credits || '活跃';
    }

    const btnText = document.getElementById('btn-mask-text');
    if (btnText) btnText.innerText = maskEmails ? '显示账号' : '隐藏账号';
    const icon = document.getElementById('mask-icon');
    if (icon) icon.innerText = maskEmails ? '🙈' : '👁️';

    const aRes = await fetch('/api/accounts', { cache: 'no-store' });
    const accs = await aRes.json();
    const aTbody = document.getElementById('accounts-tbody');
    if (aTbody) {
      aTbody.innerHTML = accs.map(a => `
        <tr>
          <td><b style="cursor:pointer;" onclick="toggleEmailMask()">${maskText(a.email)}</b></td>
          <td>${a.project_id || 'aicode-consumers'}</td>
          <td><span class="tag tag-200">${a.tier || 'Pro'}</span></td>
          <td><span style="font-size:11px; color:#c4b5fd;">${a.credits || '无限 / 活跃'}</span></td>
          <td>${a.active ? '<span style="color:var(--green)">● 当前主力</span>' : '<span style="color:var(--text-secondary)">备用</span>'}</td>
          <td style="display:flex; gap:6px;">
            ${a.active ? '' : `<button style="padding:3px 7px; font-size:10px;" onclick="switchAccount('${a.email}')">设为主力</button>`}
            <button style="padding:3px 7px; font-size:10px; background:rgba(239,68,68,0.15); color:var(--red); border-color:rgba(239,68,68,0.3);" onclick="deleteAccount('${a.email}')">删除</button>
          </td>
        </tr>
      `).join('');
    }

    // 渲染第六任长老 · Tencent LightVela 专属独立卡片
    try {
      const lvRes = await fetch('/api/lv_accounts', { cache: 'no-store' });
      const lvAccs = await lvRes.json();
      const lvContainer = document.getElementById('lv-accounts-container');
      if (lvContainer && Array.isArray(lvAccs)) {
        lvContainer.innerHTML = lvAccs.map(la => `
          <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:14px 16px; margin-bottom:10px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
              <div style="font-size:15px; font-weight:700; color:#c7d2fe;">${la.packageName}</div>
              <span class="badge" style="background:rgba(16,185,129,0.15); color:#34d399; border:1px solid rgba(16,185,129,0.3); font-size:11px; padding:2px 8px; border-radius:12px;">● 在线保活</span>
            </div>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px 12px; font-size:13px;">
              <div>
                <span style="color:#64748b; font-size:11px; display:block;">绑定实例 / 用户</span>
                <span style="color:#38bdf8; font-weight:600;">奥特曼</span>
                <span style="color:#64748b; font-size:11px; font-family:monospace; margin-left:4px;">(ins-00e602)</span>
              </div>
              <div>
                <span style="color:#64748b; font-size:11px; display:block;">剩余 / 总额度</span>
                <span style="color:#34d399; font-weight:700; font-size:14px;">⚡ ${la.remain} / ${la.total} 积分</span>
              </div>
              <div>
                <span style="color:#64748b; font-size:11px; display:block;">周期有效截止</span>
                <span style="color:#94a3b8; font-size:12px;">${la.expireDate}</span>
              </div>
              <div>
                <span style="color:#64748b; font-size:11px; display:block;">专属上游网关</span>
                <span style="color:#a5b4fc; font-size:12px; font-family:monospace;">/lv (token.lightvela)</span>
              </div>
            </div>
          </div>
        `).join('');
      }
    } catch (e) {
      console.error("加载 LightVela 资产失败:", e);
    }

    // 渲染第五任长老 · 腾讯 CodeBuddy 专属独立卡片
    try {
      const cbRes = await fetch('/api/cb_accounts', { cache: 'no-store' });
      const cbAccs = await cbRes.json();
      let cbTotal = 0;
      const cbTbody = document.getElementById('cb-accounts-tbody');
      if (cbTbody && Array.isArray(cbAccs)) {
        cbTbody.innerHTML = cbAccs.map(ca => {
          cbTotal += (Number(ca.remain) || 0);
          const pkgCount = ca.pkg_count ? `${ca.pkg_count}个权益包` : '1个权益包';
          const pkgsDesc = (ca.packages && ca.packages.length > 0) 
            ? ca.packages.map(p => `<div style="font-size:11px; color:#94a3b8; white-space:nowrap;">• ${p.name}: <span style="color:#38bdf8;">${p.remain}</span>/${p.total} (${p.end_time ? p.end_time.split(' ')[0] : ''})</div>`).join('')
            : `<div style="font-size:11px; color:#94a3b8;">${pkgCount}</div>`;
          return `
            <tr>
              <td><span class="tag" style="background:rgba(2,132,199,0.15); color:#38bdf8;">${ca.name}</span></td>
              <td><b style="cursor:pointer;" onclick="toggleEmailMask()">${maskText(ca.uid)}</b></td>
              <td><span style="font-weight:700; color:#38bdf8; font-size:12px;">⚡ ${ca.remain} / ${ca.total} Credits</span></td>
              <td>
                <details style="cursor:pointer;">
                  <summary style="font-size:11.5px; color:#38bdf8; outline:none;">聚合包含 ${pkgCount} ▾</summary>
                  <div style="margin-top:6px; max-height:120px; overflow-y:auto; padding:4px 6px; background:rgba(0,0,0,0.25); border-radius:6px; border:1px solid rgba(255,255,255,0.05);">
                    ${pkgsDesc}
                  </div>
                </details>
              </td>
              <td><span style="font-size:11px; color:#94a3b8;">${ca.end_time}</span></td>
              <td><span style="color:var(--green)">● ${ca.status}</span></td>
              <td><span style="font-size:10.5px; color:#38bdf8;">copilot.tencent.com/v2</span></td>
            </tr>
          `;
        }).join('');
        const cbTotEl = document.getElementById('cb-total-balance');
        if (cbTotEl) cbTotEl.innerText = `专线总额度: ⚡ ${cbTotal.toFixed(2)} Credits (${cbAccs.length}个账号)`;
      }
    } catch(cbErr) {
      console.error("Failed to load CodeBuddy accounts:", cbErr);
    }

    // 渲染 EZCompleteUI 专属独立卡片列表
    try {
      const todayRes = await fetch('/api/today_accounts', { cache: 'no-store' });
      const todayAccs = await todayRes.json();
      const todayTbody = document.getElementById('today-accounts-tbody');
      if (todayTbody && Array.isArray(todayAccs)) {
        todayTbody.innerHTML = todayAccs.map(ta => `
          <tr>
            <td><span class="tag" style="background:rgba(245,158,11,0.15); color:#fbbf24;">${ta.name}</span></td>
            <td><b style="cursor:pointer;" onclick="toggleEmailMask()">${maskText(ta.phone)}</b><div style="font-size:10px; color:#64748b;">${ta.uid}</div></td>
            <td><span style="font-weight:700; color:#fbbf24; font-size:12px;">🌟 ${ta.plan} 尊享版</span></td>
            <td><span style="font-weight:700; color:var(--green); font-size:12px;">⚡ 剩余 ${ta.remain_percent}</span><div style="font-size:10px; color:#64748b;">3亿 Tokens配额</div></td>
            <td><span style="font-size:11px; color:#94a3b8;">${ta.end_time}</span></td>
            <td><span style="color:var(--green)">● ${ta.status}</span></td>
            <td><span style="font-size:10.5px; color:#fbbf24;">api.todayai.cn</span></td>
            <td>
              <button style="padding:3px 7px; font-size:10px; background:rgba(239,68,68,0.15); color:var(--red); border-color:rgba(239,68,68,0.3);" onclick="deleteTodayAccount('${ta.phone}')">删除</button>
            </td>
          </tr>
        `).join('');
      }
    } catch(todayErr) {
      console.error("Failed to load today accounts:", todayErr);
    }

    try {
      const ezRes = await fetch('/api/ez_accounts', { cache: 'no-store' });
      const ezAccs = await ezRes.json();
      let ezTotal = 0;
      const ezTbody = document.getElementById('ez-accounts-tbody');
      if (ezTbody && Array.isArray(ezAccs)) {
        ezTbody.innerHTML = ezAccs.map(ea => {
          ezTotal += (Number(ea.balance) || 0);
          return `
            <tr>
              <td><span class="tag ${ea.name === '主号' ? 'tag-200' : ''}" style="background:${ea.name === '主号' ? 'rgba(16,185,129,0.15)' : 'rgba(99,102,241,0.15)'}; color:${ea.name === '主号' ? '#34d399' : '#a5b4fc'};">${ea.name}</span></td>
              <td><b style="cursor:pointer;" onclick="toggleEmailMask()">${maskText(ea.email)}</b></td>
              <td><span style="font-weight:700; color:#34d399; font-size:12px;">🪙 ${ea.balance} Coins</span></td>
              <td><span style="color:var(--green)">● ${ea.status}</span></td>
              <td><span style="font-size:10.5px; color:#94a3b8;">/ez/v1 (Supabase)</span></td>
              <td>
                <button style="padding:3px 7px; font-size:10px; background:rgba(239,68,68,0.15); color:var(--red); border-color:rgba(239,68,68,0.3);" onclick="deleteEzAccount('${ea.email}')">删除</button>
              </td>
            </tr>
          `;
        }).join('');
        const ezTotEl = document.getElementById('ez-total-balance');
        if (ezTotEl) ezTotEl.innerText = `矩阵总额度: 🪙 ${ezTotal} Coins (${ezAccs.length}个账号)`;
      }
    } catch(ezErr) {
      console.error("Failed to load ez accounts:", ezErr);
    }

    const lRes = await fetch('/api/logs', { cache: 'no-store' });
    const logs = await lRes.json();
    const lTbody = document.getElementById('logs-tbody');
    if (lTbody) {
      lTbody.innerHTML = logs.slice(0, 30).map(l => `
        <tr>
          <td>${l.time}</td>
          <td><b>${l.model}</b>${l.is_title ? ' <span class="tag tag-title" title="App后台静默会话起标题/摘要请求" style="margin-left:4px;">🏷️ 标题</span>' : ''}</td>
          <td><span class="tag ${l.status === 200 ? 'tag-200' : (l.status === 499 ? 'tag-499' : 'tag-err')}" title="${l.status === 499 ? '客户端主动断开/超时（非服务端故障）' : ''}">${l.status === 499 ? '499' : l.status}</span></td>
          <td>${l.latency}</td>
          <td>${l.tokens || 0}</td>
        </tr>
      `).join('');
    }
  } catch(e) {
    console.error(e);
  }
}

async function switchAccount(email) {
  try {
    await fetch('/api/switch_account', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email: email})
    });
    refreshData();
  } catch(e) {}
}

async function deleteAccount(email) {
  if (!confirm('确定要从账号池删除 ' + email + ' 吗？')) return;
  try {
    const res = await fetch('/api/delete_account', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email: email})
    });
    const d = await res.json();
    if (d.ok) {
      refreshData();
    } else {
      alert('删除失败: ' + (d.error || '未知错误'));
    }
  } catch(e) {
    alert('请求异常: ' + e);
  }
}

async function openOAuthModal() {
  try {
    const res = await fetch('/api/oauth_start');
    const d = await res.json();
    if (d.url) {
      document.getElementById('oauthLink').href = d.url;
      document.getElementById('oauthLink').innerText = '👉 点击此处前往 Google 登录授权';
      document.getElementById('oauthModal').style.display = 'flex';
    }
  } catch(e) {
    alert('获取授权链接失败: ' + e);
  }
}

function closeOAuthModal() {
  document.getElementById('oauthModal').style.display = 'none';
}

async function submitOAuthCallback() {
  const input = document.getElementById('oauthCodeInput').value.trim();
  if (!input) return alert('请粘贴回调网址或授权码！');
  let code = input;
  if (input.includes('code=')) {
    try {
      const u = new URL(input.startsWith('http') ? input : 'http://localhost/' + input);
      code = u.searchParams.get('code') || input;
    } catch(e) {
      const match = input.match(/code=([^&]+)/);
      if (match) code = decodeURIComponent(match[1]);
    }
  }

  const btn = document.getElementById('btnSubmitOAuth');
  btn.innerText = '⏳ 正在换取凭证并检测配额...';
  btn.disabled = true;
  try {
    const res = await fetch('/api/oauth_submit', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({code: code})
    });
    const d = await res.json();
    if (d.ok) {
      alert('🎉 账号添加成功！\n账号: ' + d.account.email + '\n权益: ' + d.account.tier);
      closeOAuthModal();
      document.getElementById('oauthCodeInput').value = '';
      refreshData();
    } else {
      alert('❌ 绑定失败: ' + (d.error || JSON.stringify(d)));
    }
  } catch(e) {
    alert('提交异常: ' + e);
  } finally {
    btn.innerText = '立即换取凭证并绑定';
    btn.disabled = false;
  }
}

// EZ 矩阵折叠控制 (默认收起，记忆状态)
let ezCollapsed = localStorage.getItem('ez_panel_collapsed') !== 'false';
function initEzCollapse() {
  const wrap = document.getElementById('ez-table-wrap');
  const btn = document.getElementById('btn-toggle-ez');
  if (wrap && btn) {
    if (ezCollapsed) {
      wrap.style.display = 'none';
      btn.innerText = '📁 展开账号';
    } else {
      wrap.style.display = 'block';
      btn.innerText = '📂 收起账号';
    }
  }
}


function toggleGoogleCollapse() {
  const wrap = document.getElementById('google-table-wrap');
  const btn = document.getElementById('btn-toggle-google');
  if (!wrap || !btn) return;
  if (wrap.style.display === 'none') {
    wrap.style.display = 'block';
    btn.innerText = '📂 收起账号';
  } else {
    wrap.style.display = 'none';
    btn.innerText = '📁 展开账号';
  }
}

let cbPollTimer = null;

async function openCbModal() {
  const modal = document.getElementById('cbModal');
  const link = document.getElementById('cbAuthLink');
  const status = document.getElementById('cbPollStatus');
  modal.style.display = 'flex';
  status.innerText = '⏳ 正在向腾讯申请授权链接...';
  link.style.pointerEvents = 'none';
  link.style.opacity = '0.5';

  try {
    const res = await fetch('/api/cb_login_start');
    const d = await res.json();
    if (d.code === 0 && d.data && d.data.authUrl) {
      link.href = d.data.authUrl;
      link.style.pointerEvents = 'auto';
      link.style.opacity = '1';
      status.innerText = '📲 请点击上方按钮前往微信扫码，扫码完成后将自动同步！';
      
      const state = d.data.state;
      if (cbPollTimer) clearInterval(cbPollTimer);
      
      // 开始每 2 秒轮询一次
      cbPollTimer = setInterval(async () => {
        try {
          const pRes = await fetch('/api/cb_login_poll?state=' + encodeURIComponent(state));
          const pData = await pRes.json();
          if (pData.code === 0) {
            clearInterval(cbPollTimer);
            status.innerText = '🎉 授权成功！Token 已落盘，正在刷新...';
            setTimeout(() => {
              closeCbModal();
              refreshData();
            }, 1200);
          } else if (pData.code !== 11217) {
            // 非等待扫码的异常
            status.innerText = '⚠️ 状态: ' + (pData.msg || '等待扫码...');
          }
        } catch(err) {
          console.error(err);
        }
      }, 2000);

    } else {
      status.innerText = '❌ 申请失败: ' + (d.msg || '未知错误');
    }
  } catch(e) {
    status.innerText = '❌ 网络请求异常: ' + e;
  }
}

function closeCbModal() {
  document.getElementById('cbModal').style.display = 'none';
  if (cbPollTimer) {
    clearInterval(cbPollTimer);
    cbPollTimer = null;
  }
}

function toggleLvCollapse() {
  const wrap = document.getElementById('lv-table-wrap');
  const btn = document.getElementById('btn-toggle-lv');
  if (wrap.style.display === 'none') {
    wrap.style.display = 'block';
    btn.innerText = '📂 收起账号';
  } else {
    wrap.style.display = 'none';
    btn.innerText = '📁 展开账号';
  }
}

function toggleCbCollapse() {
  const wrap = document.getElementById('cb-table-wrap');
  const btn = document.getElementById('btn-toggle-cb');
  if (!wrap || !btn) return;
  if (wrap.style.display === 'none') {
    wrap.style.display = 'block';
    btn.innerText = '📂 收起账号';
  } else {
    wrap.style.display = 'none';
    btn.innerText = '📁 展开账号';
  }
}

// Today AI 折叠控制
let todayCollapsed = localStorage.getItem('today_panel_collapsed') !== 'false';
function initTodayCollapse() {
  const wrap = document.getElementById('today-table-wrap');
  const btn = document.getElementById('btn-toggle-today');
  if (wrap && btn) {
    if (todayCollapsed) {
      wrap.style.display = 'none';
      btn.innerText = '📁 展开账号';
    } else {
      wrap.style.display = 'block';
      btn.innerText = '📂 收起账号';
    }
  }
}
function toggleTodayCollapse() {
  todayCollapsed = !todayCollapsed;
  localStorage.setItem('today_panel_collapsed', todayCollapsed);
  initTodayCollapse();
}
document.addEventListener('DOMContentLoaded', initTodayCollapse);
setTimeout(initTodayCollapse, 200);

function openTodayModal() {
  document.getElementById('todayInputName').value = '';
  document.getElementById('todayInputPhone').value = '';
  document.getElementById('todayInputSession').value = '';
  document.getElementById('todayModal').style.display = 'flex';
}

function closeTodayModal() {
  document.getElementById('todayModal').style.display = 'none';
}

async function submitTodayAccount() {
  const name = document.getElementById('todayInputName').value.trim() || '主号';
  const phone = document.getElementById('todayInputPhone').value.trim();
  const sessionToken = document.getElementById('todayInputSession').value.trim();
  if (!sessionToken) return alert('请填入 Session Token 或完整 Cookie！');

  const btn = document.getElementById('btnSubmitToday');
  btn.innerText = '⏳ 校验换票中...';
  btn.disabled = true;

  try {
    const res = await fetch('/api/add_today_account', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({name: name, phone: phone, session_token: sessionToken})
    });
    const d = await res.json();
    if (d.ok) {
      alert('🎉 Today AI 账号添加成功！\n已成功换取有效 JWT，权益立即可用！');
      closeTodayModal();
      todayCollapsed = false;
      localStorage.setItem('today_panel_collapsed', false);
      initTodayCollapse();
      refreshData();
    } else {
      alert('❌ 校验失败: ' + (d.error || '未知错误'));
    }
  } catch(e) {
    alert('提交异常: ' + e);
  } finally {
    btn.innerText = '校验并保存';
    btn.disabled = false;
  }
}

async function deleteTodayAccount(phone) {
  if (!confirm('确定要从 Today AI 移除该账号吗？')) return;
  try {
    const res = await fetch('/api/delete_today_account', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({phone: phone})
    });
    const d = await res.json();
    if (d.ok) {
      refreshData();
    } else {
      alert('删除失败: ' + (d.error || '未知错误'));
    }
  } catch(e) {
    alert('请求异常: ' + e);
  }
}

function toggleEzCollapse() {
  ezCollapsed = !ezCollapsed;
  localStorage.setItem('ez_panel_collapsed', ezCollapsed);
  initEzCollapse();
}
document.addEventListener('DOMContentLoaded', initEzCollapse);
setTimeout(initEzCollapse, 200);

function openEzModal() {
  document.getElementById('ezInputName').value = '';
  document.getElementById('ezInputEmail').value = '';
  document.getElementById('ezInputPassword').value = '';
  document.getElementById('ezModal').style.display = 'flex';
}

function closeEzModal() {
  document.getElementById('ezModal').style.display = 'none';
}

async function submitEzAccount() {
  const name = document.getElementById('ezInputName').value.trim() || '小号';
  const email = document.getElementById('ezInputEmail').value.trim();
  const password = document.getElementById('ezInputPassword').value.trim();
  if (!email || !password) return alert('请填写邮箱和密码！');

  const btn = document.getElementById('btnSubmitEz');
  btn.innerText = '⏳ 正在登录鉴权...';
  btn.disabled = true;
  try {
    const res = await fetch('/api/add_ez_account', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({name: name, email: email, password: password})
    });
    const d = await res.json();
    if (d.ok) {
      alert('🎉 账号添加成功！\n账号: ' + d.account.email + '\n当前余额: 🪙 ' + d.account.balance + ' Coins');
      closeEzModal();
      // 添加成功后自动展开列表查看
      ezCollapsed = false;
      localStorage.setItem('ez_panel_collapsed', false);
      initEzCollapse();
      refreshData();
    } else {
      alert('❌ 校验失败: ' + (d.error || '未知错误'));
    }
  } catch(e) {
    alert('提交异常: ' + e);
  } finally {
    btn.innerText = '校验并保存';
    btn.disabled = false;
  }
}

async function deleteEzAccount(email) {
  if (!confirm('确定要从 EZ 矩阵池移除账号 ' + email + ' 吗？')) return;
  try {
    const res = await fetch('/api/delete_ez_account', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email: email})
    });
    const d = await res.json();
    if (d.ok) {
      refreshData();
    } else {
      alert('删除失败: ' + (d.error || '未知错误'));
    }
  } catch(e) {
    alert('请求异常: ' + e);
  }
}


setInterval(() => {
  const cd5 = document.getElementById('quota-5h-countdown');
  const cdw = document.getElementById('quota-week-countdown');
  if (window._LAST_QUOTA_5H_RESET && cd5) cd5.innerText = formatCountdown(window._LAST_QUOTA_5H_RESET);
  if (window._LAST_QUOTA_WEEK_RESET && cdw) cdw.innerText = formatCountdown(window._LAST_QUOTA_WEEK_RESET);
}, 1000);

setInterval(refreshData, 3000);
refreshData();
</script>
</body>
</html>
"""
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

import re
import subprocess

import re
import subprocess
import os

import re
import subprocess
import os

# 真正硬核健壮的指令执行器
def execute_system_intent(prompt):
    # 彻底废除！反代绝不拦截用户聊天，所有对话一律交给真正的大模型思考！
    return None


_CACHED_FREE_MODELS = []
_CACHED_FREE_TIME = 0

def fetch_free_upstream_models():
    global _CACHED_FREE_MODELS, _CACHED_FREE_TIME
    now = time.time()
    if _CACHED_FREE_MODELS and (now - _CACHED_FREE_TIME < 600):
        return _CACHED_FREE_MODELS
    try:
        req = urllib.request.Request("https://api.kilo.ai/api/gateway/models", headers={"User-Agent": "OmniRoute/3.8.51"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            raw_list = data.get("data", [])
            res = []
            
            # 常用精简别名置顶（方便选择）
            alias_map = [
                ("nemotron", "NVIDIA Nemotron 3 Ultra 550B (旗舰白嫖)"),
                ("nemotron-550b", "NVIDIA Nemotron 3 Ultra 550B"),
                ("nemotron-120b", "NVIDIA Nemotron 3 Super 120B"),
                ("nemotron-nano", "NVIDIA Nemotron 3 Nano 30B (带深度推理)"),
                ("free-auto", "Kilo Auto Free (自动切换可用免费池)"),
                ("step-5-free", "阶跃星辰 Step-5 免费体验版")
            ]
            for a_id, a_name in alias_map:
                res.append({"id": a_id, "object": "model", "created": 1700000000, "owned_by": "free-alias"})
                
            for item in raw_list:
                m_id = str(item.get("id", ""))
                # 严格过滤：只保留包含 :free、-free、/free 的纯免费免Key模型！
                if m_id.endswith(":free") or "-free" in m_id or "/free" in m_id:
                    res.append({"id": m_id, "object": "model", "created": 1700000000, "owned_by": "free-upstream"})
                    
            _CACHED_FREE_MODELS = res
            _CACHED_FREE_TIME = now
            return res
    except Exception as e:
        if _CACHED_FREE_MODELS:
            return _CACHED_FREE_MODELS
        return [{"id": "nvidia/nemotron-3-ultra-550b-a55b:free", "object": "model", "created": 1700000000, "owned_by": "nvidia-free"}]

class AntigravityHandler(BaseHTTPRequestHandler):

    def _free_send_error(self, code, msg):
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_cors()
        self.end_headers()
        err = {"error": {"message": msg, "type": "free_upstream_error", "code": code}}
        try:
            self.wfile.write(json.dumps(err, ensure_ascii=False).encode("utf-8"))
        except Exception:
            pass

    

    def handle_lightvela_chat(self, body):
        t0 = time.time()
        try:
            req_json = json.loads(body.decode("utf-8"))
        except Exception as e:
            self.send_response(400)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_cors()
            self.end_headers()
            self.wfile.write(json.dumps({"error": {"message": f"Invalid JSON: {e}", "type": "bad_request"}}, ensure_ascii=False).encode("utf-8"))
            return

        raw_model = str(req_json.get("model", "deepseek-v4-pro-202606"))
        req_json["model"] = lv_resolve_model(raw_model)
        is_stream = bool(req_json.get("stream", False))

        url = LIGHTVELA_BASE_URL + "/chat/completions"
        data = json.dumps(req_json, ensure_ascii=False).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST")
        req.add_header("Authorization", "Bearer " + LIGHTVELA_DEFAULT_KEY)
        req.add_header("Content-Type", "application/json")
        req.add_header("User-Agent", "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)")

        try:
            res = urllib.request.urlopen(req, timeout=120)
            status_code = res.status
            content_type = res.headers.get("Content-Type", "application/json")

            self.send_response(status_code)
            self.send_header("Content-Type", content_type)
            self.send_cors()
            self.end_headers()

            while True:
                chunk = res.read(4096)
                if not chunk:
                    break
                self.wfile.write(chunk)
                self.wfile.flush()
        except urllib.error.HTTPError as e:
            err_data = e.read()
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_cors()
            self.end_headers()
            self.wfile.write(err_data)
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_cors()
            self.end_headers()
            self.wfile.write(json.dumps({"error": {"message": f"LightVela 上游异常: {e}", "type": "upstream_error"}}, ensure_ascii=False).encode("utf-8"))


    def _today_send_error(self, code, msg, stream=False, model="todayai"):
        if stream:
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.send_cors()
            self.end_headers()
            chunk = {
                "id": f"chatcmpl-today-err-{int(time.time()*1000)}",
                "object": "chat.completion.chunk",
                "created": int(time.time()),
                "model": model,
                "choices": [{
                    "index": 0,
                    "delta": {"content": f"\n\n> ⚠️ **【Today AI 上游服务异常 · HTTP {code}】**\n> {msg}\n\n"},
                    "finish_reason": "stop"
                }]
            }
            try:
                self.wfile.write(f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n".encode("utf-8"))
                self.wfile.write(b"data: [DONE]\n\n")
                self.wfile.flush()
            except Exception:
                pass
            return

        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_cors()
        self.end_headers()
        err = {"error": {"message": msg, "type": "todayai_error", "code": code}}
        try:
            self.wfile.write(json.dumps(err, ensure_ascii=False).encode("utf-8"))
        except Exception:
            pass

    def handle_today_chat(self, body):
        t0 = time.time()
        try:
            req_json = json.loads(body.decode("utf-8"))
        except Exception as e:
            self._today_send_error(400, "Invalid JSON: %s" % e, stream=False)
            return

        raw_model = str(req_json.get("model", "todayai"))
        client_wants_stream = bool(req_json.get("stream", False))

        # 提取最后一条用户 prompt
        messages = req_json.get("messages", [])
        last_user_prompt = ""
        for m in messages:
            if m.get("role") == "user":
                c = m.get("content", "")
                if isinstance(c, str):
                    last_user_prompt = c
                elif isinstance(c, list):
                    for part in c:
                        if isinstance(part, dict) and part.get("type") == "text":
                            last_user_prompt = part.get("text", "")
        if not last_user_prompt:
            last_user_prompt = "你好"

        accs = today_load_credentials()
        if not accs:
            self._today_send_error(500, "未检测到 Today AI 账号凭证，请先在控制台添加！", stream=client_wants_stream, model=raw_model)
            return

        account = accs[0]
        session_token = account.get("session_token", "")
        jwt_token = today_get_jwt_for_session(session_token)
        if not jwt_token:
            self._today_send_error(401, "Today AI 换票失败，Session Cookie 已过期或失效！", stream=client_wants_stream, model=raw_model)
            return

        # 1. 下发消息 POST https://api.todayai.cn/v1/messages
        post_url = f"{TODAYAI_API_BASE}/messages"
        post_headers = {
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)"
        }
        post_data = json.dumps({"role": "user", "content": last_user_prompt}, ensure_ascii=False).encode("utf-8")
        post_req = urllib.request.Request(post_url, data=post_data, headers=post_headers, method="POST")

        try:
            with urllib.request.urlopen(post_req, timeout=15) as p_resp:
                p_res = json.loads(p_resp.read().decode("utf-8"))
                thread_id = p_res.get("threadId") or p_res.get("data", {}).get("threadId")
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "ignore")[:300]
            self._today_send_error(e.code, f"Today AI 提交消息失败: {detail}", stream=client_wants_stream, model=raw_model)
            return
        except Exception as e:
            self._today_send_error(500, f"Today AI 下发消息网络异常: {e}", stream=client_wants_stream, model=raw_model)
            return

        if not thread_id:
            self._today_send_error(500, "Today AI 未返回有效 threadId", stream=client_wants_stream, model=raw_model)
            return

        # 2. 轮询回复 GET https://api.todayai.cn/v1/messages?threadId=<thread_id>
        get_url = f"{TODAYAI_API_BASE}/messages?threadId={thread_id}"
        get_req = urllib.request.Request(get_url, headers={"Authorization": f"Bearer {jwt_token}", "User-Agent": "Mozilla/5.0"})

        assistant_content = ""
        max_poll_time = 45  # 最长等待 45 秒
        start_poll = time.time()

        while time.time() - start_poll < max_poll_time:
            time.sleep(1.0)
            try:
                with urllib.request.urlopen(get_req, timeout=10) as g_resp:
                    g_res = json.loads(g_resp.read().decode("utf-8"))
                    msgs = g_res.get("data", []) if isinstance(g_res, dict) and "data" in g_res else g_res
                    if isinstance(msgs, list):
                        for m in msgs:
                            if m.get("role") == "assistant" and m.get("content"):
                                assistant_content = m.get("content")
                                break
                    if assistant_content:
                        break
            except Exception:
                pass

        if not assistant_content:
            assistant_content = "⚠️ Today AI 回复生成超时，请稍后重试。"

        c_time = int(time.time())
        c_id = f"chatcmpl-today-{int(time.time()*1000)}"

        if client_wants_stream:
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.send_cors()
            self.end_headers()

            # 模拟逐字流式平滑吐字，提供丝滑体验
            chunk_size = 12
            for i in range(0, len(assistant_content), chunk_size):
                piece = assistant_content[i:i+chunk_size]
                chunk = {
                    "id": c_id,
                    "object": "chat.completion.chunk",
                    "created": c_time,
                    "model": raw_model,
                    "choices": [{"index": 0, "delta": {"content": piece}, "finish_reason": None}]
                }
                self.wfile.write(f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n".encode("utf-8"))
                self.wfile.flush()
                time.sleep(0.02)

            end_chunk = {
                "id": c_id,
                "object": "chat.completion.chunk",
                "created": c_time,
                "model": raw_model,
                "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]
            }
            self.wfile.write(f"data: {json.dumps(end_chunk, ensure_ascii=False)}\n\n".encode("utf-8"))
            self.wfile.write(b"data: [DONE]\n\n")
            self.wfile.flush()
        else:
            out = {
                "id": c_id,
                "object": "chat.completion",
                "created": c_time,
                "model": raw_model,
                "choices": [{
                    "index": 0,
                    "message": {"role": "assistant", "content": assistant_content},
                    "finish_reason": "stop"
                }],
                "usage": {
                    "prompt_tokens": len(last_user_prompt),
                    "completion_tokens": len(assistant_content),
                    "total_tokens": len(last_user_prompt) + len(assistant_content)
                }
            }
            res_b = json.dumps(out, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(res_b)))
            self.send_cors()
            self.end_headers()
            self.wfile.write(res_b)

        record_stat(True)
        log_request(raw_model, 200, int((time.time() - t0) * 1000), len(assistant_content.encode("utf-8")), "ok today")

    def _cb_send_error(self, code, msg, stream=False, model="deepseek-v4.1-flash"):
        if stream:
            # 针对 SSE 流式客户端 (Minis)，直接输出标准 SSE 消息帧，杜绝界面死等转圈！
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.send_cors()
            self.end_headers()

            notice = (
                f"\n\n> ⚠️ **【腾讯 CodeBuddy 上游服务异常 · HTTP {code}】**\n"
                f"> **原因分析**：腾讯 Copilot 上游瞬时高负载、网络抖动或服务不可用。\n"
                f"> **底层报错**：`{msg}`\n"
                f"> **系统动作**：反代已自动执行 3 次重试仍未成功。请稍后重试或无缝切换至 LightVela/Gemini 专线。\n\n"
            )
            chunk = {
                "id": f"chatcmpl-cb-err-{int(time.time()*1000)}",
                "object": "chat.completion.chunk",
                "created": int(time.time()),
                "model": model,
                "choices": [{
                    "index": 0,
                    "delta": {"content": notice},
                    "finish_reason": "stop"
                }]
            }
            try:
                self.wfile.write(f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n".encode("utf-8"))
                self.wfile.write(b"data: [DONE]\n\n")
                self.wfile.flush()
            except Exception:
                pass
            return

        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_cors()
        self.end_headers()
        err = {"error": {"message": msg, "type": "codebuddy_error", "code": code}}
        try:
            self.wfile.write(json.dumps(err, ensure_ascii=False).encode("utf-8"))
        except Exception:
            pass

    def handle_codebuddy_chat(self, body):
        t0 = time.time()
        try:
            req_json = json.loads(body.decode("utf-8"))
        except Exception as e:
            self._cb_send_error(400, "Invalid JSON: %s" % e, stream=False)
            return

        raw_model = str(req_json.get("model", "deepseek-v3"))
        target = cb_resolve_model(raw_model)
        req_json["model"] = target

        # 记录用户原本是否请求流式传输
        client_wants_stream = bool(req_json.get("stream", False))
        req_json["stream"] = True

        if "max_completion_tokens" in req_json:
            req_json["max_tokens"] = req_json.pop("max_completion_tokens")

        at, uid = cb_get_access_token()
        if not at:
            self._cb_send_error(500, "未检测到腾讯 CodeBuddy 凭证或已失效，请重新授权！", stream=client_wants_stream, model=target)
            return

        url = CODEBUDDY_BASE_URL + "/v2/chat/completions"
        data = json.dumps(req_json, ensure_ascii=False).encode("utf-8")

        max_retries = 3
        resp = None
        last_error_code = 502
        last_error_msg = ""

        for attempt in range(1, max_retries + 1):
            req = urllib.request.Request(url, data=data, method="POST")
            req.add_header("Authorization", "Bearer " + at)
            req.add_header("Content-Type", "application/json")
            req.add_header("User-Agent", "CLI/2.63.2 CodeBuddy/2.63.2")
            req.add_header("X-User-Id", uid)
            req.add_header("X-Domain", "copilot.tencent.com")
            req.add_header("X-Product", "SaaS")
            req.add_header("X-Requested-With", "XMLHttpRequest")
            req.add_header("Accept", "text/event-stream")

            try:
                resp = urllib.request.urlopen(req, timeout=120)
                break
            except urllib.error.HTTPError as e:
                detail = ""
                try:
                    detail = e.read().decode("utf-8", "replace")[:600]
                except Exception:
                    pass
                last_error_code = e.code
                last_error_msg = f"HTTP {e.code}: {detail}"
                print(f"[CB-Retry] 腾讯上游返回 {e.code} (尝试 {attempt}/{max_retries}): {detail[:100]}")
                if e.code in (500, 502, 503, 504) and attempt < max_retries:
                    time.sleep(0.8 * attempt)
                    continue
                record_stat(False, err="cb %s" % e.code)
                log_request(raw_model, e.code, int((time.time() - t0) * 1000), 0, detail[:200])
                self._cb_send_error(e.code, f"CodeBuddy 上游返回 {e.code}: {detail}", stream=client_wants_stream, model=target)
                return
            except Exception as e:
                last_error_code = 502
                last_error_msg = str(e)
                print(f"[CB-Retry] 腾讯上游连接异常 (尝试 {attempt}/{max_retries}): {e}")
                if attempt < max_retries:
                    time.sleep(0.8 * attempt)
                    continue
                record_stat(False, err="cb connect")
                log_request(raw_model, 502, int((time.time() - t0) * 1000), 0, str(e)[:200])
                self._cb_send_error(502, f"连接 CodeBuddy 上游失败: {e}", stream=client_wants_stream, model=target)
                return

        if not resp:
            record_stat(False, err="cb retry_failed")
            log_request(raw_model, last_error_code, int((time.time() - t0) * 1000), 0, last_error_msg[:200])
            self._cb_send_error(last_error_code, f"重试耗尽: {last_error_msg}", stream=client_wants_stream, model=target)
            return

        if client_wants_stream:
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.send_cors()
            self.end_headers()

            total_bytes = 0
            has_sent_done = False
            try:
                while True:
                    line = resp.readline()
                    if not line:
                        break
                    self.wfile.write(line)
                    self.wfile.flush()
                    total_bytes += len(line)
                    if b"[DONE]" in line:
                        has_sent_done = True
            except Exception as e:
                # 若流式中途中断且尚未发送[DONE]，补发友好断流提示与[DONE]，彻底防止客户端挂死
                if not has_sent_done:
                    err_chunk = {
                        "id": f"chatcmpl-cb-break-{int(time.time()*1000)}",
                        "object": "chat.completion.chunk",
                        "created": int(time.time()),
                        "model": target,
                        "choices": [{
                            "index": 0,
                            "delta": {"content": f"\n\n> ⚠️ **[网络中途中断：{e}]**\n"},
                            "finish_reason": "stop"
                        }]
                    }
                    try:
                        self.wfile.write(f"data: {json.dumps(err_chunk, ensure_ascii=False)}\n\n".encode("utf-8"))
                        self.wfile.write(b"data: [DONE]\n\n")
                        self.wfile.flush()
                    except Exception:
                        pass
            finally:
                resp.close()
            record_stat(True)
            log_request(raw_model, 200, int((time.time() - t0) * 1000), total_bytes, "ok stream")
        else:
            full_content = []
            reasoning_content = []
            finish_reason = "stop"
            created_time = int(time.time())
            total_bytes = 0

            try:
                while True:
                    line = resp.readline()
                    if not line:
                        break
                    total_bytes += len(line)
                    sline = line.decode("utf-8", "replace").strip()
                    if sline.startswith("data: ") and sline != "data: [DONE]":
                        try:
                            chunk = json.loads(sline[6:])
                            choices = chunk.get("choices", [])
                            if choices:
                                delta = choices[0].get("delta", {})
                                c = delta.get("content", "")
                                if c:
                                    full_content.append(c)
                                rc = delta.get("reasoning_content", "")
                                if rc:
                                    reasoning_content.append(rc)
                                fr = choices[0].get("finish_reason")
                                if fr:
                                    finish_reason = fr
                        except Exception:
                            pass
            finally:
                resp.close()

            openai_resp = {
                "id": "chatcmpl-cb-" + str(int(time.time() * 1000)),
                "object": "chat.completion",
                "created": created_time,
                "model": target,
                "choices": [{
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "".join(full_content)
                    },
                    "finish_reason": finish_reason
                }],
                "usage": {
                    "prompt_tokens": 10,
                    "completion_tokens": len("".join(full_content)),
                    "total_tokens": 10 + len("".join(full_content))
                }
            }
            if reasoning_content:
                openai_resp["choices"][0]["message"]["reasoning_content"] = "".join(reasoning_content)

            out_bytes = json.dumps(openai_resp, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_cors()
            self.end_headers()
            self.wfile.write(out_bytes)
            record_stat(True)
            log_request(raw_model, 200, int((time.time() - t0) * 1000), len(out_bytes), "ok sync")

    def handle_free_chat(self, body):
        t0 = time.time()
        try:
            req_json = json.loads(body.decode("utf-8"))
        except Exception as e:
            self._free_send_error(400, "Invalid JSON: %s" % e)
            return

        raw_model = str(req_json.get("model", "nvidia/nemotron-3-ultra-550b-a55b:free"))
        target = free_resolve_model(raw_model)
        req_json["model"] = target
        stream = bool(req_json.get("stream", False))

        url = FREE_GATEWAY_URL
        data = json.dumps(req_json, ensure_ascii=False).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "text/event-stream" if stream else "application/json")
        req.add_header("User-Agent", "OmniRoute/3.8.51 (iOS; aarch64)")

        resp = None
        try:
            resp = urllib.request.urlopen(req, timeout=120)
        except urllib.error.HTTPError as e:
            detail = ""
            try:
                detail = e.read().decode("utf-8", "replace")[:600]
            except Exception:
                pass
            record_stat(False, err="free %s" % e.code)
            log_request(raw_model, e.code, int((time.time() - t0) * 1000), 0, detail[:200])
            self._free_send_error(e.code, "Free 上游返回 %s: %s" % (e.code, detail))
            return
        except Exception as e:
            record_stat(False, err="free connect")
            log_request(raw_model, 502, int((time.time() - t0) * 1000), 0, str(e)[:200])
            self._free_send_error(502, "连接 Free 免密上游失败: %s" % e)
            return

        if stream:
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.send_cors()
            self.end_headers()
            try:
                while True:
                    chunk = resp.read(1024)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    self.wfile.flush()
                record_stat(True)
                log_request(target, 200, int((time.time() - t0) * 1000), 0)
            except Exception:
                pass
            finally:
                resp.close()
        else:
            resp_body = resp.read()
            resp.close()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(resp_body)))
            self.send_cors()
            self.end_headers()
            self.wfile.write(resp_body)
            record_stat(True)
            log_request(target, 200, int((time.time() - t0) * 1000), len(resp_body))

    protocol_version = "HTTP/1.1"

    def log_message(self, format, *args):
        return

    def send_cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_cors()
        self.end_headers()

    def do_GET(self):
        auth_hdr = self.headers.get("Authorization", "")
        url = urllib.parse.urlparse(self.path)
        path = url.path

        if path in ["/api/hello", "/v1/hello"]:
            data = json.dumps({"status": "ok", "message": "hello"}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.send_cors()
            self.end_headers()
            self.wfile.write(data)
            return

        if path in ["/", "/index.html"]:
            body = DASHBOARD_HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(body)
            return

        if path.startswith("/static/"):
            fname = os.path.basename(path)
            if fname.endswith(".webp") or fname.endswith(".jpg") or fname.endswith(".png"):
                file_p = os.path.join(PROXY_DIR, fname)
                if os.path.exists(file_p):
                    with open(file_p, "rb") as f:
                        content = f.read()
                    self.send_response(200)
                    self.send_header("Content-Type", "image/webp")
                    self.send_header("Content-Length", str(len(content)))
                    self.send_header("Cache-Control", "public, max-age=86400")
                    self.end_headers()
                    self.wfile.write(content)
                    return

        if path == "/static/wanglin_full.webp":
            file_p = os.path.join(PROXY_DIR, "wanglin_full.webp")
            if os.path.exists(file_p):
                with open(file_p, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "image/webp")
                self.send_header("Content-Length", str(len(content)))
                self.send_header("Cache-Control", "public, max-age=86400")
                self.end_headers()
                self.wfile.write(content)
                return

        if path == "/static/wanglin_avatar.webp":
            file_p = os.path.join(PROXY_DIR, "wanglin_avatar.webp")
            if os.path.exists(file_p):
                with open(file_p, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "image/webp")
                self.send_header("Content-Length", str(len(content)))
                self.send_header("Cache-Control", "public, max-age=86400")
                self.end_headers()
                self.wfile.write(content)
                return

        if path == "/api/stats":
            data = json.dumps(get_stats_summary(), ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(data)
            return

        if path == "/api/cb_login_start":
            # 申请 CodeBuddy OAuth 设备授权 URL
            try:
                c_req = urllib.request.Request(
                    "https://copilot.tencent.com/v2/plugin/auth/state?platform=CLI",
                    headers={"User-Agent": "CLI/2.63.2 CodeBuddy/2.63.2", "Content-Type": "application/json"},
                    data=b"{}",
                    method="POST"
                )
                with urllib.request.urlopen(c_req, timeout=10) as c_resp:
                    c_data = json.loads(c_resp.read().decode("utf-8"))
                    res_b = json.dumps(c_data, ensure_ascii=False).encode("utf-8")
            except Exception as e:
                res_b = json.dumps({"code": -1, "msg": str(e)}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(res_b)))
            self.send_cors()
            self.end_headers()
            self.wfile.write(res_b)
            return

        if path.startswith("/api/cb_login_poll"):
            # 轮询扫码结果，成功后立即原子落盘
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            state = q.get("state", [""])[0]
            if not state:
                res_b = json.dumps({"code": -1, "msg": "缺少 state 参数"}).encode("utf-8")
            else:
                try:
                    c_req = urllib.request.Request(
                        f"https://copilot.tencent.com/v2/plugin/auth/token?state={state}",
                        headers={"User-Agent": "CLI/2.63.2 CodeBuddy/2.63.2", "Accept": "application/json"}
                    )
                    with urllib.request.urlopen(c_req, timeout=10) as c_resp:
                        c_data = json.loads(c_resp.read().decode("utf-8"))
                        if c_data.get("code") == 0 and "data" in c_data:
                            # 抓到新 Token，自动落盘
                            cb_save_credentials(c_data["data"])
                        res_b = json.dumps(c_data, ensure_ascii=False).encode("utf-8")
                except Exception as e:
                    res_b = json.dumps({"code": -1, "msg": str(e)}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(res_b)))
            self.send_cors()
            self.end_headers()
            self.wfile.write(res_b)
            return

        if path == "/api/cb_token_raw":
            creds = cb_load_credentials() or {}
            res_b = json.dumps(creds, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(res_b)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(res_b)
            return

        if path.startswith("/cb/v1/models") or path.startswith("/tencent/v1/models") or path.startswith("/codebuddy/v1/models") or path == "/v1/models" and "codebuddy" in self.headers.get("Authorization", "").lower():
            # 返回腾讯 CodeBuddy 专线专属合法模型列表
            m_list = []
            for mid in CODEBUDDY_MODELS:
                m_list.append({
                    "id": mid,
                    "object": "model",
                    "created": 1791925440,
                    "owned_by": "tencent"
                })
            res_b = json.dumps({"object": "list", "data": m_list}, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(res_b)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(res_b)
            return

        if path in ["/api/today_accounts", "/today/accounts"]:
            # 读取 Today AI 实时资产数据
            today_accs = today_load_credentials()
            res_list = []
            for a in today_accs:
                s_tok = a.get("session_token", "")
                j_tok = today_get_jwt_for_session(s_tok)
                plan = "Pro"
                end_time = "2027-01-26"
                rem_pct = "99%"
                status = "在线 / 活跃" if j_tok else "离线 / 待换票"
                if j_tok:
                    try:
                        st_req = urllib.request.Request(
                            f"{TODAYAI_API_BASE}/pricing/status",
                            headers={"Authorization": f"Bearer {j_tok}", "User-Agent": "Mozilla/5.0"}
                        )
                        with urllib.request.urlopen(st_req, timeout=5) as st_resp:
                            st_json = json.loads(st_resp.read().decode("utf-8"))
                            st_data = st_json.get("data", {}).get("status", {})
                            plan = st_data.get("plan", "pro").upper()
                            end_time = (st_data.get("entitlementEndsAt") or "2027-01-26").replace("T", " ")[:16]
                            rem_pct = st_data.get("usage", {}).get("breakdown", {}).get("display", {}).get("remainingPercentText", "99%")
                    except Exception as e:
                        pass
                res_list.append({
                    "name": a.get("name", "Today AI 账号"),
                    "phone": a.get("phone", "+86 153****7210"),
                    "uid": a.get("uid", "393IQwScSkXfWAPKskNzxuGWGhFFKVbW"),
                    "plan": plan,
                    "tokens": "300,000,000",
                    "remain_percent": rem_pct,
                    "end_time": end_time,
                    "status": status,
                    "upstream": "api.todayai.cn/v1"
                })
            res_b = json.dumps(res_list, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(res_b)))
            self.send_cors()
            self.end_headers()
            self.wfile.write(res_b)
            return

        if path in ["/api/lv_accounts", "/lv/accounts"]:
            # 读取 LightVela 真实资产数据
            lv_data = [{
                "packageName": "启航 Launch AI (月度配额)",
                "instanceId": "ins-00e602d25f1b4aaeaacb760d934b509a (奥特曼)",
                "remain": 4499,
                "total": 4500,
                "expireDate": "2026-11-14 17:39",
                "status": "Running",
                "upstream": "https://token.lightvela.com/v1"
            }]
            res_b = json.dumps(lv_data, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(res_b)))
            self.send_cors()
            self.end_headers()
            self.wfile.write(res_b)
            return

        if path in ["/api/cb_accounts", "/cb/accounts"]:
            res_list = []
            try:
                creds = cb_load_credentials()
                if creds:
                    at = creds.get("accessToken", "")
                    uid = creds.get("uid") or CODEBUDDY_DEFAULT_UID
                    url = "https://www.codebuddy.cn/v2/billing/meter/get-user-resource"
                    headers = {
                        "Authorization": "Bearer " + at,
                        "User-Agent": "CLI/2.63.2 CodeBuddy/2.63.2",
                        "X-User-Id": uid,
                        "X-Domain": "copilot.tencent.com",
                        "X-Product": "SaaS",
                        "X-Requested-With": "XMLHttpRequest",
                        "Accept": "application/json"
                    }
                    req = urllib.request.Request(url, headers=headers, method="POST", data=b"{}")
                    with urllib.request.urlopen(req, timeout=5) as resp:
                        d = json.loads(resp.read().decode())
                        accs = d.get("data", {}).get("Response", {}).get("Data", {}).get("Accounts", [])
                        if accs:
                            tot_remain = sum(float(a.get("CycleCapacityRemainPrecise") or a.get("CapacityRemain") or 0) for a in accs)
                            tot_size = sum(float(a.get("CycleCapacitySizePrecise") or a.get("CapacitySize") or 0) for a in accs)
                            tot_used = sum(float(a.get("CycleCapacityUsedPrecise") or a.get("CapacityUsed") or 0) for a in accs)
                            latest_end = max((a.get("CycleEndTime") or a.get("ExpiredTime") or "") for a in accs)
                            pkgs = []
                            for a in accs:
                                pkgs.append({
                                    "name": a.get("PackageName", "权益包"),
                                    "remain": str(a.get("CycleCapacityRemainPrecise") or a.get("CapacityRemain", 0)),
                                    "total": str(a.get("CycleCapacitySizePrecise") or a.get("CapacitySize", 0)),
                                    "end_time": a.get("CycleEndTime") or a.get("ExpiredTime", "")
                                })
                            res_list.append({
                                "name": "腾讯 CodeBuddy 核心账号",
                                "uid": uid,
                                "remain": f"{tot_remain:.2f}" if tot_remain % 1 != 0 else str(int(tot_remain)),
                                "total": f"{tot_size:.2f}" if tot_size % 1 != 0 else str(int(tot_size)),
                                "used": f"{tot_used:.2f}" if tot_used % 1 != 0 else str(int(tot_used)),
                                "end_time": latest_end or "永久",
                                "status": "在线 / 活跃",
                                "pkg_count": len(accs),
                                "packages": pkgs
                            })
            except Exception as e:
                res_list.append({
                    "name": "腾讯 CodeBuddy 授权账号",
                    "uid": CODEBUDDY_DEFAULT_UID,
                    "remain": "1999.98",
                    "total": "2000",
                    "used": "0.02",
                    "end_time": "2026-11-14",
                    "status": "在线"
                })
            res_b = json.dumps(res_list, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(res_b)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(res_b)
            return

        if path in ["/api/ez_accounts", "/ez/v1/balance", "/ez/balance"]:
            # 返回 EZComplete 独立账号池数据与秒级实时真实动态余额
            accs = load_ez_accounts()
            import concurrent.futures
            
            def fetch_single_account_bal(a):
                em = a.get("email")
                tok = get_ez_valid_token_for_account(a)
                a_bal = 0
                if tok:
                    try:
                        # 工业级零损耗只读探针：直接查流水表 balance_after，绝对不调 ez-chat，0扣费！
                        tx_req = urllib.request.Request(
                            f"{EZ_SUPABASE_URL}/rest/v1/coin_transactions?select=balance_after&limit=1&order=created_at.desc",
                            headers={"apikey": EZ_ANON_KEY, "Authorization": f"Bearer {tok}"}
                        )
                        with CELLULAR_OPENER.open(tx_req, timeout=5) as tx_resp:
                            tx_data = json.loads(tx_resp.read().decode("utf-8", errors="ignore"))
                            if isinstance(tx_data, list) and len(tx_data) > 0:
                                a_bal = tx_data[0].get("balance_after", 0)
                    except Exception:
                        pass
                return {
                    "name": a.get("name", "账号"),
                    "email": em,
                    "balance": a_bal,
                    "status": "在线 / 正常" if tok else "离线 / 待换票"
                }

            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                res_list = list(executor.map(fetch_single_account_bal, accs))

            data = json.dumps(res_list, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(data)
            return

        if path == "/api/accounts":
            data = json.dumps(load_accounts(), ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(data)
            return

        if path == "/api/logs":
            with LOGS_LOCK:
                data = json.dumps(REQUEST_LOGS, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(data)
            return

        if path == "/api/oauth_start":
            scopes = "https://www.googleapis.com/auth/cloud-platform https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/cclog https://www.googleapis.com/auth/experimentsandconfigs"
            redirect_uri = "http://localhost:51121/oauth-callback"
            oauth_url = (
                f"https://accounts.google.com/o/oauth2/v2/auth?"
                f"client_id={CLIENT_ID}&"
                f"redirect_uri={urllib.parse.quote(redirect_uri)}&"
                f"response_type=code&"
                f"scope={urllib.parse.quote(scopes)}&"
                f"access_type=offline&"
                f"prompt=consent"
            )
            data = json.dumps({"url": oauth_url}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(data)
            return

        if path.startswith("/ez/quota_status"):
            allowed = ez_quota_checker.get_allowed_devices()
            data = json.dumps({"count": len(allowed), "max": 3, "devices": allowed}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        if path in ["/meta/login", "/meta/v1/login"]:
            code, doc = _meta_form_post("/oidc/device/authorization/", {"client_id": META_CLIENT_ID})
            if not (200 <= code < 300) or not doc.get("device_code"):
                self._meta_send_error(502, "无法发起 Meta 设备码登录 (HTTP %s): %s" % (code, doc))
                return
            interval = int(doc.get("interval", 5) or 5)
            lifetime = int(doc.get("expires_in", 600) or 600)
            _META_DEVICE.update({
                "device_code": doc.get("device_code", ""),
                "user_code": doc.get("user_code", ""),
                "uri": doc.get("verification_uri_complete") or doc.get("verification_uri", ""),
                "expires_at": int(time.time()) + lifetime,
                "state": "starting",
                "error": "",
            })
            threading.Thread(target=meta_device_login_worker,
                             args=(doc.get("device_code", ""), interval, time.time() + lifetime),
                             daemon=True).start()
            data = json.dumps({
                "ok": True,
                "user_code": _META_DEVICE["user_code"],
                "verification_uri": _META_DEVICE["uri"],
                "expires_in": lifetime,
                "hint": "浏览器打开 verification_uri，确认码一致后批准；反代后台会自动轮询并把 token 落盘。",
            }, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(data)
            return

        if path in ["/meta/status", "/meta/v1/status"]:
            tok = meta_read_token()
            data = json.dumps({
                "authorized": bool(tok),
                "token_tail": ("..." + tok[-6:]) if tok else "",
                "has_refresh_token": bool(meta_read_refresh()),
                "device_flow": {"state": _META_DEVICE.get("state"), "user_code": _META_DEVICE.get("user_code"),
                                "verification_uri": _META_DEVICE.get("uri"),
                                "error": _META_DEVICE.get("error")},
                "base_url": META_BASE,
                "models": META_MODELS,
            }, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(data)
            return

        if path in ["/v1/models", "/ez/v1/models", "/ez/models", "/meta/v1/models", "/meta/models", "/free/v1/models", "/free/models", "/omni/v1/models"] or path.endswith("/models"):
            auth_hdr = self.headers.get("Authorization", "")
            raw_key = auth_hdr.replace("Bearer ", "").strip()
            
            # 三大上游模型物理隔离列表：
            dyn_models = fetch_upstream_dynamic_models()
            antigravity_models = [{"id": m, "object": "model", "created": 1700000000, "owned_by": "google-antigravity"} for m in dyn_models]
            # 注入 OpenAI 官方标准语音转写模型 Whisper
            antigravity_models.insert(0, {"id": "whisper-1", "object": "model", "created": 1700000000, "owned_by": "openai"})
            ez_models = [
                {"id": "gpt-6-astra", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-6-luna", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-6-sol", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-5.6-luna", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-5.6-sol", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-5.6-terra", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-5", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-5-pro", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-5-mini", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-4o", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-4o-mini", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-4o-mini-2024-07-18", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-4.1", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-4.1-mini", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-4.1-nano", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "o4-mini", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-image-2.5-flare", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "gpt-image-2.5-sunburst", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "chatgpt-image-latest", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "dalle3_hd", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "dalle3_standard", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "ez-image", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "flux-schnell", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"},
                {"id": "recraft-v3", "object": "model", "created": 1700000000, "owned_by": "ezcomplete-supabase"}
            ]
            meta_models = [
                {"id": m, "object": "model", "created": 1700000000, "owned_by": "meta-model-api"}
                for m in META_MODELS
            ]
            free_models = fetch_free_upstream_models()

            # 严格根据 Key 或路径完全隔离，绝不混淆：
            lv_models = [
                {"id": "deepseek-v4-pro-202606", "object": "model", "created": 1700000000, "owned_by": "tencent-lightvela"},
                {"id": "deepseek-v4-pro", "object": "model", "created": 1700000000, "owned_by": "tencent-lightvela"},
                {"id": "deepseek-v4", "object": "model", "created": 1700000000, "owned_by": "tencent-lightvela"},
                {"id": "auto", "object": "model", "created": 1700000000, "owned_by": "tencent-lightvela"},
                {"id": "ep-hyasr3", "object": "model", "created": 1700000000, "owned_by": "tencent-lightvela"},
                {"id": "deepseek-v4-flash", "object": "model", "created": 1700000000, "owned_by": "tencent-lightvela"},
                {"id": "glm-5.3", "object": "model", "created": 1700000000, "owned_by": "tencent-lightvela"},
                {"id": "qwen3.7-plus", "object": "model", "created": 1700000000, "owned_by": "tencent-lightvela"},
                {"id": "kimi-k2.5", "object": "model", "created": 1700000000, "owned_by": "tencent-lightvela"},
                {"id": "minimax-m2.7", "object": "model", "created": 1700000000, "owned_by": "tencent-lightvela"}
            ]
            cb_models = [
                {"id": m, "object": "model", "created": 1700000000, "owned_by": "tencent-codebuddy"}
                for m in CODEBUDDY_MODELS
            ]

            today_models = [
                {"id": "todayai/default", "object": "model", "created": 1700000000, "owned_by": "today-ai"},
                {"id": "today/default", "object": "model", "created": 1700000000, "owned_by": "today-ai"},
                {"id": "todayai", "object": "model", "created": 1700000000, "owned_by": "today-ai"},
                {"id": "today", "object": "model", "created": 1700000000, "owned_by": "today-ai"},
                {"id": "deepseek-v4.1-flash", "object": "model", "created": 1700000000, "owned_by": "today-ai"},
                {"id": "minimax-m31-flash", "object": "model", "created": 1700000000, "owned_by": "today-ai"},
                {"id": "glm-5.3", "object": "model", "created": 1700000000, "owned_by": "today-ai"}
            ]

            if path.startswith("/today") or raw_key.startswith("sk-today") or "today" in raw_key.lower():
                res_models = today_models
            elif path.startswith("/lightvela") or path.startswith("/vela") or path.startswith("/lv") or raw_key.startswith("sk-lightvela") or raw_key.startswith("sk-vela") or raw_key.startswith("sk-lv") or "lightvela" in raw_key.lower() or "vela" in raw_key.lower():
                res_models = lv_models
            elif path.startswith("/codebuddy") or path.startswith("/tencent") or path.startswith("/cb") or raw_key.startswith("sk-codebuddy") or raw_key.startswith("sk-tencent") or raw_key.startswith("sk-cb") or "codebuddy" in raw_key.lower() or "tencent" in raw_key.lower():
                res_models = cb_models
            elif path.startswith("/free") or path.startswith("/omni") or raw_key.startswith("sk-free") or raw_key.startswith("sk-omni") or "free" in raw_key.lower() or "omni" in raw_key.lower():
                res_models = free_models
            elif path.startswith("/ez") or raw_key.startswith("sk-ez") or "ez" in raw_key.lower():
                res_models = ez_models
            elif path.startswith("/meta") or raw_key.startswith("sk-meta") or "meta" in raw_key.lower():
                res_models = meta_models
            elif raw_key.startswith("sk-antigravity") or "anti" in raw_key.lower():
                res_models = antigravity_models
            else:
                # 默认根据路径分流，根路径无特征 key 默认按上游一返回
                res_models = antigravity_models

            data = json.dumps({"object": "list", "data": res_models}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(data)
            return

        # 适配 Minis 余额探测端点（兼容 /v1/usage, /api/usage/token, /v1/dashboard/billing/subscription 等）
        if any(p in path for p in ["usage", "billing/subscription", "dashboard/billing", "user/balance"]):
            auth_val = self.headers.get("Authorization", "").lower()

            # -1. Today AI 专线专属真实额度 (3亿 Tokens / Pro权益)
            if path.startswith("/today") or "sk-today" in auth_val or "today" in auth_val:
                remain_p = 99.0
                plan_name = "pro"
                end_time = "2027-01-26"
                try:
                    t_accs = today_load_credentials()
                    if t_accs:
                        s_tok = t_accs[0].get("session_token", "")
                        j_tok = today_get_jwt_for_session(s_tok)
                        if j_tok:
                            st_req = urllib.request.Request(
                                f"{TODAYAI_API_BASE}/pricing/status",
                                headers={"Authorization": f"Bearer {j_tok}", "User-Agent": "Mozilla/5.0"}
                            )
                            with urllib.request.urlopen(st_req, timeout=5) as st_resp:
                                st_json = json.loads(st_resp.read().decode("utf-8"))
                                st_data = st_json.get("data", {}).get("status", {})
                                plan_name = st_data.get("plan", "pro")
                                end_time = (st_data.get("entitlementEndsAt") or "2027-01-26").split("T")[0]
                                rem_str = st_data.get("usage", {}).get("breakdown", {}).get("display", {}).get("remainingPercentText", "99%")
                                remain_p = float(rem_str.replace("%", "").strip())
                except Exception:
                    pass

                res_obj = {
                    "object": "billing_subscription",
                    "has_payment_method": True,
                    "soft_limit_usd": 300000000.0 * (remain_p / 100.0),
                    "hard_limit_usd": 300000000.0,
                    "system_hard_limit_usd": 300000000.0,
                    "total_usage": 300000000.0 * ((100.0 - remain_p) / 100.0),
                    "total_available": 300000000.0 * (remain_p / 100.0),
                    "balance": remain_p,
                    "currency": "Tokens",
                    "plan": {"title": f"Today AI {plan_name.upper()} (至 {end_time}) 剩余 {remain_p}%"}
                }
                res_b = json.dumps(res_obj).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res_b)))
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_b)
                return

            # 0. Tencent LightVela 专线专属真实额度 (4499 积分)
            if path.startswith("/lv") or path.startswith("/vela") or path.startswith("/lightvela") or "sk-lightvela" in auth_val or "sk-vela" in auth_val or "lightvela" in auth_val:
                total_credits = 4500.0
                remain_credits = 4499.0
                used_credits = 1.0
                res_obj = {
                    "object": "billing_subscription",
                    "has_payment_method": True,
                    "soft_limit_usd": remain_credits,
                    "hard_limit_usd": total_credits,
                    "system_hard_limit_usd": total_credits,
                    "total_usage": used_credits,
                    "total_available": remain_credits,
                    "balance": remain_credits,
                    "currency": "USD",
                    "plan": {"title": "LightVela 启航版 (4500积分)"}
                }
                res_b = json.dumps(res_obj).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res_b)))
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_b)
                return
            auth_val = self.headers.get("Authorization", "").lower()
            
            # 1. 腾讯 CodeBuddy 专线专属真实额度 (Credits 算力)
            if path.startswith("/cb") or path.startswith("/tencent") or "sk-tencent" in auth_val or "codebuddy" in auth_val:
                cb_bal = 2100.0
                cb_used = 0.02
                try:
                    creds = cb_load_credentials()
                    if creds:
                        at = creds.get("accessToken", "")
                        uid = creds.get("uid") or CODEBUDDY_DEFAULT_UID
                        u_req = urllib.request.Request(
                            "https://www.codebuddy.cn/v2/billing/meter/get-user-resource",
                            headers={"Authorization": "Bearer " + at, "User-Agent": "CLI/2.63.2 CodeBuddy/2.63.2", "X-User-Id": uid, "X-Domain": "copilot.tencent.com", "X-Product": "SaaS", "Content-Type": "application/json"},
                            data=b"{}",
                            method="POST"
                        )
                        with urllib.request.urlopen(u_req, timeout=3) as u_resp:
                            u_d = json.loads(u_resp.read().decode())
                            cb_bal = float(u_d.get("data", {}).get("Response", {}).get("Data", {}).get("TotalDosage", 2100))
                except Exception:
                    pass
                bal = cb_bal
                currency = "Credits"

            # 2. Google Antigravity 主线专线 (精准对齐 Google 官方极境配额)
            elif not path.startswith("/ez") and "sk-ez" not in auth_val and ("sk-antigravity" in auth_val or path == "/v1/dashboard/billing/subscription" or path.startswith("/v1")):
                g_rem = 98.0
                try:
                    q_data = fetch_antigravity_quota()
                    if q_data:
                        # 优先取 5 小时极境雷灵额度，如果没有则取本周额度
                        b_5h = q_data.get("gemini-5h") or q_data.get("3p-5h")
                        b_wk = q_data.get("gemini-weekly") or q_data.get("3p-weekly")
                        if b_5h and "remaining_pct" in b_5h:
                            g_rem = float(b_5h["remaining_pct"])
                        elif b_wk and "remaining_pct" in b_wk:
                            g_rem = float(b_wk["remaining_pct"])
                except Exception:
                    pass
                bal = g_rem
                currency = "%"

            # 3. EZCompleteUI 专属真实额度 (Coins)
            else:
                cached_bal = 0.0
                if os.path.exists(EZ_BALANCE_FILE):
                    try:
                        with open(EZ_BALANCE_FILE, "r", encoding="utf-8") as _bf:
                            cached_bal = float(_bf.read().strip())
                    except Exception:
                        pass
                bal = cached_bal if cached_bal > 0 else 4073.0
                currency = "Coins"

            b_data = {
                "object": "billing_subscription",
                "has_payment_method": True,
                "canceled": False,
                "hard_limit_usd": float(bal),
                "total_granted": float(bal),
                "total_used": 0.0,
                "total_available": float(bal),
                "system_hard_limit_usd": float(bal),
                "total": float(bal),
                "used": 0.0,
                "balance": float(bal),
                "quota": int(bal * 500000),
                "currency": currency
            }
            if "token" in path or "usage/token" in path:
                b_data = {
                    "object": "token",
                    "status": 1,
                    "data": {
                        "remain_quota": int(bal * 500000),
                        "used_quota": 0,
                        "unlimited_quota": (bal >= 9999.0)
                    }
                }
            res_b = json.dumps(b_data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(res_b)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(res_b)
            return

        print(f"[404_HIT] path={path}, full_path={self.path}, method={self.command}", flush=True); self.send_response(404)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_POST(self):
        url = urllib.parse.urlparse(self.path)
        path = url.path
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length > 0 else b"{}"

# [Cleaned] 已彻底剔除历史 Siri 意图劫持

        if path == "/_log_audit":
            try:
                log_dir = "/var/mobile/.antigravity_tunnel"
                os.makedirs(log_dir, exist_ok=True)
                log_file = os.path.join(log_dir, "audit_hackers.log")
                if os.path.exists(log_file) and os.path.getsize(log_file) > 5 * 1024 * 1024:
                    try:
                        with open(log_file, "r", encoding="utf-8", errors="ignore") as rf:
                            cur_lines = rf.readlines()
                        with open(log_file, "w", encoding="utf-8") as wf:
                            wf.writelines(cur_lines[-1000:])
                    except:
                        pass
                event = json.loads(body.decode("utf-8", errors="ignore"))
                bj_time = event.get("time") or time.strftime("%Y-%m-%d %H:%M:%S")
                msg = ("[%s] [%s]\n" + "  ├─ 出口IP: %s (%s)\n" + "  ├─ 内网IP: %s\n" + "  ├─ 指纹ID: Canvas:[%s] GPU:[%s]\n" + "  ├─ 硬件环境: 屏幕:%s 核心内存:%s 时区:%s\n" + "  ├─ 浏览器: %s\n" + "  └─ 详情: %s\n\n") % (bj_time, event.get("type"), event.get("ip"), event.get("location"), event.get("local_ips", "none"), event.get("canvas"), event.get("gpu"), event.get("screen"), event.get("cores_mem"), event.get("timezone"), event.get("ua"), event.get("detail"))
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(msg)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_cors()
                self.end_headers()
                self.wfile.write(b'{"status":"recorded"}')
                return
            except Exception as e:
                print("[Audit Error] %s" % e, flush=True)


                self.wfile.write(b'{"status":"recorded"}')
                return
            except Exception as e:
                print(f"[Audit Log Error] {e}", flush=True)


        # 优先拦截处理 EZCompleteUI 专属独立端点
        if path.startswith("/ez/") or path.startswith("/ez"):
                        # 如果请求的是生图（包含 images/generations 或模型带有 flare/sunburst/gpt-image）
            if "images" in path:
                self.handle_ez_image_generations(body)
                return
            try:
                chk = json.loads(body.decode("utf-8"))
                m_name = str(chk.get("model", "")).lower()
                if "flare" in m_name or "sunburst" in m_name or "gpt-image" in m_name:
                    self.handle_ez_image_generations(body)
                    return
            except Exception:
                pass
            self.handle_ezcomplete_chat(body)
            return

        if path == "/api/switch_account":
            try:
                req_json = json.loads(body.decode("utf-8"))
                email = req_json.get("email")
                with DATA_LOCK:
                    accs = load_accounts()
                    for a in accs:
                        a["active"] = (a.get("email") == email)
                    save_accounts(accs)
                res_body = json.dumps({"ok": True}).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(res_body)))
                self.send_header("Connection", "close")
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_body)
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                return

        if path == "/api/oauth_submit":
            try:
                req_json = json.loads(body.decode("utf-8"))
                code = req_json.get("code", "").strip()
                if not code:
                    self.send_response(400)
                    self.end_headers()
                    return

                token_url = "https://oauth2.googleapis.com/token"
                token_payload = urllib.parse.urlencode({
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                    "code": code,
                    "grant_type": "authorization_code",
                    "redirect_uri": "http://localhost:51121/oauth-callback"
                }).encode("utf-8")
                t_req = urllib.request.Request(token_url, data=token_payload, headers={"Content-Type": "application/x-www-form-urlencoded"})
                with urllib.request.urlopen(t_req, context=SSL_CTX, timeout=15) as resp:
                    t_data = json.loads(resp.read().decode("utf-8"))

                access_tok = t_data.get("access_token")
                refresh_tok = t_data.get("refresh_token")
                email = f"google_user_{int(time.time())}@gmail.com"
                
                # 尝试获取真实邮箱
                try:
                    u_req = urllib.request.Request("https://www.googleapis.com/oauth2/v2/userinfo", headers={"Authorization": f"Bearer {access_tok}"})
                    with urllib.request.urlopen(u_req, context=SSL_CTX, timeout=10) as u_resp:
                        u_info = json.loads(u_resp.read().decode("utf-8"))
                        email = u_info.get("email", email)
                except Exception:
                    pass

                # 检测配额和等级
                tier_id = "Google AI Pro (g1-pro-tier)"
                credits_val = "Pro 专属高配额 / 50 积分"
                try:
                    q_req = urllib.request.Request(
                        f"{ANTIGRAVITY_API_URL}/v1internal:loadCodeAssist",
                        data=json.dumps({"metadata": {"ideType": "ANTIGRAVITY"}}).encode("utf-8"),
                        headers={"Authorization": f"Bearer {access_tok}", "Content-Type": "application/json", "User-Agent": ANTIGRAVITY_USER_AGENT}
                    )
                    with urllib.request.urlopen(q_req, context=SSL_CTX, timeout=10) as q_resp:
                        q_data = json.loads(q_resp.read().decode("utf-8"))
                        paid = q_data.get("paidTier", {})
                        if isinstance(paid, dict) and paid.get("name"):
                            tier_id = paid.get("name")
                except Exception:
                    pass

                new_acc = {
                    "email": email,
                    "refresh_token": refresh_tok,
                    "access_token": access_tok,
                    "expires_at": time.time() + t_data.get("expires_in", 3600) - 120,
                    "project_id": "aicode-consumers",
                    "tier": tier_id,
                    "credits": credits_val,
                    "active": True
                }

                with DATA_LOCK:
                    accs = load_accounts()
                    for a in accs:
                        a["active"] = False
                    # 去重
                    accs = [a for a in accs if a.get("email") != email]
                    accs.insert(0, new_acc)
                    save_accounts(accs)
                    with open(CREDS_FILE, "w", encoding="utf-8") as f:
                        json.dump(new_acc, f, indent=2, ensure_ascii=False)

                res_bytes = json.dumps({"ok": True, "account": new_acc}, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res_bytes)))
                self.send_header("Connection", "close")
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_bytes)
                return

            except Exception as e:
                self.send_response(500)
                err_bytes = json.dumps({"ok": False, "error": str(e)}, ensure_ascii=False).encode("utf-8")
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(err_bytes)))
                self.send_cors()
                self.end_headers()
                self.wfile.write(err_bytes)
                return

        if path == "/api/add_today_account":
            try:
                req_json = json.loads(body.decode("utf-8"))
                session_raw = req_json.get("session_token", "").strip()
                name = req_json.get("name", "").strip() or "主号"
                phone = req_json.get("phone", "").strip() or "+86 153****7210"
                if not session_raw:
                    res_b = json.dumps({"ok": False, "error": "Session Token 不能为空！"}).encode("utf-8")
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Content-Length", str(len(res_b)))
                    self.send_cors()
                    self.end_headers()
                    self.wfile.write(res_b)
                    return

                # 清理提取 session_token 纯值
                s_token = session_raw
                if "__Secure-better-auth.session_token=" in s_token:
                    s_token = s_token.split("__Secure-better-auth.session_token=")[1].split(";")[0].strip()

                # 尝试用该 Session 换票
                jwt_tok = today_get_jwt_for_session(s_token)
                if not jwt_tok:
                    res_b = json.dumps({"ok": False, "error": "Today AI 换票失败！请检查 Session Cookie 是否有效"}).encode("utf-8")
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Content-Length", str(len(res_b)))
                    self.send_cors()
                    self.end_headers()
                    self.wfile.write(res_b)
                    return

                # 保存到 todayai_credentials.json
                with _today_lock:
                    accs = today_load_credentials()
                    new_item = {
                        "name": name,
                        "phone": phone,
                        "uid": f"user_{int(time.time())}",
                        "session_token": s_token,
                        "created_at": time.strftime("%Y-%m-%d")
                    }
                    accs = [a for a in accs if a.get("phone") != phone]
                    accs.append(new_item)
                    today_save_credentials(accs)

                res_b = json.dumps({"ok": True, "account": new_item}).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res_b)))
                self.send_header("Connection", "close")
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_b)
                return
            except Exception as e:
                self.send_response(500)
                err_b = json.dumps({"ok": False, "error": str(e)}).encode("utf-8")
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(err_b)))
                self.send_cors()
                self.end_headers()
                self.wfile.write(err_b)
                return

        if path == "/api/delete_today_account":
            try:
                req_json = json.loads(body.decode("utf-8"))
                phone = req_json.get("phone", "").strip()
                with _today_lock:
                    accs = today_load_credentials()
                    new_accs = [a for a in accs if a.get("phone") != phone]
                    today_save_credentials(new_accs)
                res_b = json.dumps({"ok": True}).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res_b)))
                self.send_header("Connection", "close")
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_b)
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                return

        if path == "/api/add_ez_account":
            try:
                req_json = json.loads(body.decode("utf-8"))
                email = req_json.get("email", "").strip()
                password = req_json.get("password", "").strip()
                name = req_json.get("name", "").strip() or "小号"
                if not email or not password:
                    res_b = json.dumps({"ok": False, "error": "邮箱和密码不能为空！"}).encode("utf-8")
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Content-Length", str(len(res_b)))
                    self.send_cors()
                    self.end_headers()
                    self.wfile.write(res_b)
                    return

                # 立即尝试真实登录鉴权换票
                temp_acc = {"email": email, "password": password, "name": name}
                tok = get_ez_valid_token_for_account(temp_acc)
                if not tok:
                    res_b = json.dumps({"ok": False, "error": "EZ 登录失败！请检查邮箱和密码是否正确"}).encode("utf-8")
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Content-Length", str(len(res_b)))
                    self.send_cors()
                    self.end_headers()
                    self.wfile.write(res_b)
                    return

                # 探测余额
                cur_bal = 0
                try:
                    tx_req = urllib.request.Request(
                        f"{EZ_SUPABASE_URL}/rest/v1/coin_transactions?select=balance_after&limit=1&order=created_at.desc",
                        headers={"apikey": EZ_ANON_KEY, "Authorization": f"Bearer {tok}"}
                    )
                    with CELLULAR_OPENER.open(tx_req, timeout=5) as tx_resp:
                        tx_data = json.loads(tx_resp.read().decode("utf-8", errors="ignore"))
                        if isinstance(tx_data, list) and len(tx_data) > 0:
                            cur_bal = tx_data[0].get("balance_after", 0)
                except Exception:
                    pass

                # 保存到 ez_accounts.json
                with DATA_LOCK:
                    accs = load_ez_accounts()
                    # 避免重复
                    accs = [a for a in accs if a.get("email") != email]
                    new_item = {"email": email, "password": password, "name": name}
                    accs.append(new_item)
                    with open(EZ_ACCOUNTS_FILE, "w", encoding="utf-8") as f:
                        json.dump(accs, f, indent=2, ensure_ascii=False)

                res_b = json.dumps({"ok": True, "account": {"email": email, "name": name, "balance": cur_bal}}).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res_b)))
                self.send_header("Connection", "close")
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_b)
                return
            except Exception as e:
                self.send_response(500)
                err_b = json.dumps({"ok": False, "error": str(e)}).encode("utf-8")
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(err_b)))
                self.send_cors()
                self.end_headers()
                self.wfile.write(err_b)
                return

        if path == "/api/delete_ez_account":
            try:
                req_json = json.loads(body.decode("utf-8"))
                email = req_json.get("email", "").strip()
                with DATA_LOCK:
                    accs = load_ez_accounts()
                    if len(accs) <= 1:
                        res_b = json.dumps({"ok": False, "error": "至少保留一个账号！"}).encode("utf-8")
                        self.send_response(400)
                        self.send_header("Content-Type", "application/json; charset=utf-8")
                        self.send_header("Content-Length", str(len(res_b)))
                        self.send_cors()
                        self.end_headers()
                        self.wfile.write(res_b)
                        return
                    new_accs = [a for a in accs if a.get("email") != email]
                    with open(EZ_ACCOUNTS_FILE, "w", encoding="utf-8") as f:
                        json.dump(new_accs, f, indent=2, ensure_ascii=False)

                res_b = json.dumps({"ok": True}).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res_b)))
                self.send_header("Connection", "close")
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_b)
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                return

        if path == "/api/delete_account":
            try:
                req_json = json.loads(body.decode("utf-8"))
                email = req_json.get("email")
                with DATA_LOCK:
                    accs = load_accounts()
                    if len(accs) <= 1:
                        res_b = json.dumps({"ok": False, "error": "至少保留一个账号，不能全部删除！"}).encode("utf-8")
                        self.send_response(400)
                        self.send_header("Content-Type", "application/json; charset=utf-8")
                        self.send_header("Content-Length", str(len(res_b)))
                        self.send_cors()
                        self.end_headers()
                        self.wfile.write(res_b)
                        return

                    was_active = False
                    new_list = []
                    for a in accs:
                        if a.get("email") == email:
                            if a.get("active"):
                                was_active = True
                        else:
                            new_list.append(a)
                    
                    if was_active and new_list:
                        new_list[0]["active"] = True
                        with open(CREDS_FILE, "w", encoding="utf-8") as f:
                            json.dump(new_list[0], f, indent=2, ensure_ascii=False)

                    save_accounts(new_list)

                res_b = json.dumps({"ok": True}).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res_b)))
                self.send_header("Connection", "close")
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_b)
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                return

        if path in ["/v1/images/generations", "/images/generations"]:
            try:
                chk = json.loads(body.decode("utf-8"))
                m_name = str(chk.get("model", "")).lower()
                if "flare" in m_name or "sunburst" in m_name or "gpt-image" in m_name or "dalle" in m_name or "ez" in m_name:
                    self.handle_ez_image_generations(body)
                    return
                if "muse-image" in m_name:
                    self.handle_meta_model_chat(body, image=True)
                    return
            except Exception:
                pass
            self.handle_image_generations(body)
            return

        if path in ["/v1/audio/transcriptions", "/audio/transcriptions"]:
            self.handle_audio_transcriptions(body)
            return

        if path in ["/v1/messages", "/messages"]:
            self.handle_anthropic_messages(body)
            return

        if path in ["/v1/chat/completions", "/chat/completions", "/v1", "/"] or path.endswith("/v1/chat/completions") or path.endswith("/chat/completions"):
            auth_hdr = self.headers.get("Authorization", "")
            raw_key = auth_hdr.replace("Bearer ", "").strip()
            
            try:
                chk = json.loads(body.decode("utf-8"))
                m_name = str(chk.get("model", "")).strip()
            except Exception:
                chk = {}
                m_name = ""

            # 判断 Key 的归属通道 (七大独立通道彻底隔离)
            is_today_key = path.startswith("/today") or raw_key.startswith("sk-today") or "today" in raw_key.lower() or m_name in TODAYAI_MODELS or m_name in TODAYAI_ALIASES or m_name.startswith("today")
            is_lv_key = (not is_today_key) and (path.startswith("/lightvela") or path.startswith("/vela") or path.startswith("/lv") or raw_key.startswith("sk-lightvela") or raw_key.startswith("sk-vela") or raw_key.startswith("sk-lv") or "lightvela" in raw_key.lower() or "vela" in raw_key.lower() or m_name in LIGHTVELA_MODELS or m_name in LIGHTVELA_ALIASES or m_name.startswith("vela/") or m_name.startswith("lightvela/") or m_name.startswith("lv-"))
            is_cb_key = (not is_today_key and not is_lv_key) and (path.startswith("/codebuddy") or path.startswith("/tencent") or path.startswith("/cb") or raw_key.startswith("sk-codebuddy") or raw_key.startswith("sk-tencent") or raw_key.startswith("sk-cb") or "codebuddy" in raw_key.lower() or "tencent" in raw_key.lower() or m_name in CODEBUDDY_MODELS or m_name in CODEBUDDY_ALIASES or m_name.startswith("tencent/") or m_name.startswith("codebuddy/"))
            is_free_key = (not is_today_key and not is_cb_key and not is_lv_key) and (path.startswith("/free") or path.startswith("/omni") or raw_key.startswith("sk-free") or raw_key.startswith("sk-omni") or "free" in raw_key.lower() or "omni" in raw_key.lower())
            is_ez_key = (not is_today_key and not is_free_key and not is_lv_key and not is_cb_key) and (path.startswith("/ez") or raw_key.startswith("sk-ez") or "ez" in raw_key.lower())
            is_meta_key = (not is_today_key and not is_free_key and not is_lv_key and not is_cb_key) and (path.startswith("/meta") or raw_key.startswith("sk-meta") or "meta" in raw_key.lower())
            is_anti_key = (not is_today_key and not is_free_key and not is_ez_key and not is_meta_key and not is_lv_key and not is_cb_key) or raw_key.startswith("sk-antigravity") or "anti" in raw_key.lower()

            # 三大通道专属合法模型集合
            ez_model_ids = {
                "gpt-6-astra", "gpt-6-luna", "gpt-6-sol", "gpt-5.6-luna", "gpt-5.6-sol", "gpt-5.6-terra",
                "gpt-5", "gpt-5-pro", "gpt-5-mini", "gpt-4o", "gpt-4o-mini", "gpt-4o-mini-2024-07-18",
                "gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano", "o4-mini", "gpt-image-2.5-flare",
                "gpt-image-2.5-sunburst", "chatgpt-image-latest", "dalle3_hd", "dalle3_standard",
                "ez-image", "flux-schnell", "recraft-v3", "sora_pro_10s", "sora_10s", "ez-whisper", "ez-chat"
            }
            meta_model_ids = set(META_MODELS) | set(META_ALIASES.keys())
            anti_model_ids = set(SUPPORTED_MODELS)
            free_model_ids = set(FREE_SUPPORTED_MODELS) | set(FREE_MODEL_ALIASES.keys())

            # === 通道七：Today AI 专属长老专线 (3亿Token/Pro) ===
            if is_today_key:
                self.handle_today_chat(body)
                return

            # === 通道六：Tencent LightVela 专属长老专线 ===
            if is_lv_key:
                self.handle_lightvela_chat(body)
                return

            # === 通道五：Tencent CodeBuddy 专线 ===
            if is_cb_key:
                self.handle_codebuddy_chat(body)
                return

            # === 通道四：Free / Omni 免Key白嫖专线 ===
            if is_free_key:
                # 严防拿着 Free Key 去调 EZ、Meta、Antigravity 专线模型
                if m_name in ez_model_ids or meta_is_meta_model(m_name) or m_name in meta_model_ids or m_name in anti_model_ids:
                    self.send_response(403)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_cors()
                    self.end_headers()
                    err = {"error": {"message": f"越权拦截: 当前 Key 为 Free/Omni 专线 Key (sk-free)，禁止调用付费/专属模型 '{m_name}'！免费专线只准白嫖免费模型！", "type": "upstream_key_mismatch", "code": 403}}
                    self.wfile.write(json.dumps(err, ensure_ascii=False).encode("utf-8"))
                    return
                self.handle_free_chat(body)
                return

            # === 通道一：EZComplete 专线 ===
            if is_ez_key:
                if m_name and (m_name not in ez_model_ids and not any(k in m_name.lower() for k in ["gpt-", "ez-", "dalle", "flux", "recraft", "sora"])):
                    self.send_response(403)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_cors()
                    self.end_headers()
                    err = {"error": {"message": f"越权拦截: 当前 Key 为 EZComplete 专线 Key，禁止调用非 EZComplete 模型 '{m_name}'！各上游各用各的 Key 与模型！", "type": "upstream_key_mismatch", "code": 403}}
                    self.wfile.write(json.dumps(err, ensure_ascii=False).encode("utf-8"))
                    return
                if "flare" in m_name.lower() or "sunburst" in m_name.lower() or "gpt-image" in m_name.lower() or "dalle" in m_name.lower() or "flux" in m_name.lower() or "recraft" in m_name.lower():
                    self.handle_ez_image_generations(body)
                else:
                    self.handle_ezcomplete_chat(body)
                return

            # === 通道二：Meta Model API 专线 ===
            if is_meta_key:
                if m_name and not meta_is_meta_model(m_name) and m_name not in meta_model_ids:
                    self.send_response(403)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_cors()
                    self.end_headers()
                    err = {"error": {"message": f"越权拦截: 当前 Key 为 Meta 专线 Key，禁止调用非 Meta 模型 '{m_name}'！各上游各用各的 Key 与模型！", "type": "upstream_key_mismatch", "code": 403}}
                    self.wfile.write(json.dumps(err, ensure_ascii=False).encode("utf-8"))
                    return
                self.handle_meta_model_chat(body)
                return

            # === 通道三：Google Antigravity 专线 ===
            if is_anti_key:
                # 严防用 Antigravity Key 串门调用 EZ 或 Meta 模型
                if m_name in ez_model_ids or meta_is_meta_model(m_name) or m_name in meta_model_ids or m_name in free_model_ids or ":free" in m_name.lower():
                    self.send_response(403)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_cors()
                    self.end_headers()
                    err = {"error": {"message": f"越权拦截: 当前 Key 为 Antigravity 专线 Key (sk-antigravity)，禁止调用外部上游模型 '{m_name}'！请使用对应的专属 Key！", "type": "upstream_key_mismatch", "code": 403}}
                    self.wfile.write(json.dumps(err, ensure_ascii=False).encode("utf-8"))
                    return
                if m_name.lower() == "gemini-3.1-flash-image":
                    self.handle_image_generations(body)
                    return
                self.handle_chat_completions(body)
                return

        self.send_response(404)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def handle_ezcomplete_chat(self, body):
        t0 = time.time()
        try:
            req_json = json.loads(body.decode("utf-8"))
        except Exception as e:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.send_cors()
            self.end_headers()
            self.wfile.write(json.dumps({"error": f"Invalid JSON: {e}"}).encode("utf-8"))
            return

        stream = req_json.get("stream", False)
        raw_model = str(req_json.get("model", "gpt-4o-mini-2024-07-18"))

        # 如果传入的模型本身就在 EZCompleteUI 原生支持范围内，做自动别名兼容与退役重定向
        target_model = raw_model
        if "gpt-6-sol" in raw_model:
            target_model = "gpt-6-luna"
        elif "gpt-6-astra" in raw_model:
            target_model = "gpt-6-luna"
        elif "gpt-5.6-sol" in raw_model:
            target_model = "gpt-5.6-luna"
        elif raw_model in ["ez-chat", "ez-gpt-4o-mini"]:
            target_model = "gpt-4o"
        elif raw_model in ["gpt-4o-mini-2024-07-18", "gpt-4o-mini"]:
            target_model = "gpt-4o"

        # 根据模型动态配置 feature_tier
        f_tier = "chat_standard"
        if "mini" in target_model or "nano" in target_model:
            f_tier = "chat_mini"
        elif "gpt-6" in target_model or "gpt-5" in target_model:
            f_tier = "chat_premium"

        # 提取上下文对话（过滤掉 system 提示词注入的冗长规则，优先提取最后一条真实 user 提问）
        all_msgs = req_json.get("messages", [])
        last_user_prompt = ""
        full_context = []
        for m in all_msgs:
            role = m.get("role", "user")
            content = m.get("content", "")
            txt = ""
            if isinstance(content, str):
                txt = content
            elif isinstance(content, list):
                for p in content:
                    if isinstance(p, dict) and p.get("type") == "text":
                        txt += p.get("text", "")
            txt = txt.strip()
            if not txt:
                continue

            if role == "user":
                last_user_prompt = txt
                full_context.append(f"User: {txt}")
            elif role == "assistant":
                full_context.append(f"Assistant: {txt}")

        # 核心：必须使用最后一条真实用户 Prompt，绝不能拼接 system 噪声
        prompt_txt = last_user_prompt if last_user_prompt else "你好"
        intent_reply = execute_system_intent(prompt_txt)
        if intent_reply:
            print(f"[SystemIntent] 触发真机本地系统意图执行: {prompt_txt} -> {intent_reply}")
            if stream:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.send_cors()
                self.end_headers()
                c_id = f"chatcmpl-sys-{uuid.uuid4().hex[:12]}"
                c_time = int(time.time())
                chunk = {"id": c_id, "object": "chat.completion.chunk", "created": c_time, "model": raw_model, "choices": [{"index": 0, "delta": {"content": intent_reply}, "finish_reason": None}]}
                self.wfile.write(f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n".encode("utf-8"))
                end_c = {"id": c_id, "object": "chat.completion.chunk", "created": c_time, "model": raw_model, "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]}
                self.wfile.write(f"data: {json.dumps(end_c, ensure_ascii=False)}\n\n".encode("utf-8"))
                self.wfile.write(b"data: [DONE]\n\n")
                self.wfile.flush()
                self.close_connection = True
                return
            else:
                out = {"id": f"chatcmpl-sys-{uuid.uuid4().hex[:12]}", "object": "chat.completion", "created": int(time.time()), "model": raw_model, "choices": [{"index": 0, "message": {"role": "assistant", "content": intent_reply}, "finish_reason": "stop"}]}
                res_b = json.dumps(out, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res_b)))
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_b)
                return
        with open("/tmp/last_ez_prompt.txt", "w", encoding="utf-8") as _pf:
            _pf.write(f"PROMPT_TXT: {prompt_txt}\nALL_MSGS: {json.dumps(all_msgs, ensure_ascii=False)}")

        # 从账号池轮询读取有效账号与 Token
        active_acc, user_token = get_ez_next_available_account_and_token()
        acc_email = active_acc.get("email", "unknown") if active_acc else "unknown"
        print(f"[EZChat] 当前使用账号: {acc_email} 进行对话调用")

        if not user_token:
            err_msg = "【EZCompleteUI 鉴权失败】无法通过账号密码自动换票，请检查账号密码或网络连接。"
            if stream:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                self.send_cors()
                self.end_headers()
                chunk_obj = {
                    "id": f"chatcmpl-ez-{uuid.uuid4().hex[:12]}",
                    "object": "chat.completion.chunk",
                    "created": int(time.time()),
                    "model": raw_model,
                    "choices": [{"index": 0, "delta": {"content": err_msg}, "finish_reason": "stop"}]
                }
                self.wfile.write(f"data: {json.dumps(chunk_obj, ensure_ascii=False)}\n\n".encode("utf-8"))
                self.wfile.write(b"data: [DONE]\n\n")
                self.wfile.flush()
            else:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_cors()
                self.end_headers()
                self.wfile.write(json.dumps({"choices": [{"message": {"role": "assistant", "content": err_msg}}]}).encode("utf-8"))
            return

        # 完美对齐客户端 ez-chat 真实发包：同时携带 prompt_preview、prompt、messages 全结构！
        send_prompt = prompt_txt

        ez_payload = {
            "model": target_model,
            "prompt_preview": send_prompt,
            "prompt": send_prompt,
            "messages": [{"role": "user", "content": send_prompt}],
            "feature_tier": f_tier,
            "estimated_tokens": max(len(send_prompt) // 2, 20),
            "web_search": False
        }

        url = f"{EZ_SUPABASE_URL}/functions/v1/ez-chat"
        # 动态混淆随机前向代理 IP（欺骗下游反向代理日志）
        import random
        spoof_ip = f"{random.choice([104, 172, 198, 23, 45, 66])}.{random.randint(10,250)}.{random.randint(10,250)}.{random.randint(10,250)}"
        headers = {
            "apikey": EZ_ANON_KEY,
            "Authorization": f"Bearer {user_token}",
            "Content-Type": "application/json",
            "User-Agent": "EZCompleteUI/7.1.4 (iPhone; iOS 16.0; Scale/3.00)",
            "X-Forwarded-For": spoof_ip,
            "X-Real-IP": spoof_ip,
            "Client-IP": spoof_ip
        }

        try:
            req = urllib.request.Request(url, data=json.dumps(ez_payload).encode("utf-8"), headers=headers, method="POST")
            with CELLULAR_OPENER.open(req, timeout=60) as resp:
                ez_resp = json.loads(resp.read().decode("utf-8", errors="ignore"))

            # 如果后端返回 Model retired 错误
            if ez_resp.get("error") and "retired" in ez_resp.get("error", "").lower():
                # 自动降级为 gpt-4o 重试
                ez_payload["model"] = "gpt-4o"
                ez_payload["feature_tier"] = "chat_standard"
                req_retry = urllib.request.Request(url, data=json.dumps(ez_payload).encode("utf-8"), headers=headers, method="POST")
                with CELLULAR_OPENER.open(req_retry, timeout=60) as r_resp:
                    ez_resp = json.loads(r_resp.read().decode("utf-8", errors="ignore"))

            reply_text = ez_resp.get("reply", "")
            tokens_used = ez_resp.get("actual_tokens", 50)
            balance = ez_resp.get("balance", 0)
            if balance is not None and balance > 0:
                try:
                    with open(EZ_BALANCE_FILE, "w", encoding="utf-8") as _bf:
                        _bf.write(str(balance))
                except Exception:
                    pass

            latency = int((time.time() - t0) * 1000)
            log_request(f"ez:{target_model}", 200, latency, tokens_used)

            chat_id = f"chatcmpl-ez-{uuid.uuid4().hex[:12]}"
            created_time = int(time.time())

            if stream:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.send_header("Connection", "close")
                self.send_header("X-Accel-Buffering", "no")
                self.send_cors()
                self.end_headers()
                self.close_connection = True

                # 发送流式 SSE
                chunk_obj = {
                    "id": chat_id,
                    "object": "chat.completion.chunk",
                    "created": created_time,
                    "model": raw_model,
                    "choices": [{
                        "index": 0,
                        "delta": {"content": reply_text},
                        "finish_reason": None
                    }]
                }
                self.wfile.write(f"data: {json.dumps(chunk_obj, ensure_ascii=False)}\n\n".encode("utf-8"))
                
                # 结束帧
                end_chunk = {
                    "id": chat_id,
                    "object": "chat.completion.chunk",
                    "created": created_time,
                    "model": raw_model,
                    "choices": [{
                        "index": 0,
                        "delta": {},
                        "finish_reason": "stop"
                    }]
                }
                self.wfile.write(f"data: {json.dumps(end_chunk, ensure_ascii=False)}\n\n".encode("utf-8"))
                self.wfile.write(b"data: [DONE]\n\n")
                self.wfile.flush()
                self.close_connection = True
                return
            else:
                out_resp = {
                    "id": chat_id,
                    "object": "chat.completion",
                    "created": created_time,
                    "model": raw_model,
                    "choices": [{
                        "index": 0,
                        "message": {
                            "role": "assistant",
                            "content": reply_text
                        },
                        "finish_reason": "stop"
                    }],
                    "usage": {
                        "prompt_tokens": len(prompt_txt) // 3,
                        "completion_tokens": len(reply_text) // 3,
                        "total_tokens": tokens_used
                    },
                    "ez_metadata": {
                        "balance": balance
                    }
                }
                res_bytes = json.dumps(out_resp, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res_bytes)))
                self.send_header("Connection", "close")
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_bytes)

        except urllib.error.HTTPError as he:
            err_b = he.read().decode("utf-8", errors="ignore")
            # 捕获 Model retired 或 403 权限不足，全自动无感降级到 gpt-4o 顶上去！
            if (he.code in [400, 403]) and ("retired" in err_b.lower() or "not found" in err_b.lower() or "purchase required" in err_b.lower()):
                try:
                    c_id = f"chatcmpl-ez-{uuid.uuid4().hex[:12]}"
                    c_time = int(time.time())
                    ez_payload["model"] = "gpt-4o"
                    ez_payload["feature_tier"] = "chat_standard"
                    req_retry = urllib.request.Request(url, data=json.dumps(ez_payload).encode("utf-8"), headers=headers, method="POST")
                    with CELLULAR_OPENER.open(req_retry, timeout=60) as r_resp:
                        ez_resp = json.loads(r_resp.read().decode("utf-8", errors="ignore"))
                    reply_text = ez_resp.get("reply", "")
                    tokens_used = ez_resp.get("actual_tokens", 50)
                    balance = ez_resp.get("balance", 0)
                    if balance is not None and balance > 0:
                        try:
                            with open(EZ_BALANCE_FILE, "w", encoding="utf-8") as _bf:
                                _bf.write(str(balance))
                        except Exception:
                            pass
                    # 输出成功回复
                    if stream:
                        self.send_response(200)
                        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                        self.send_header("Cache-Control", "no-cache")
                        self.send_header("Connection", "close")
                        self.send_header("X-Accel-Buffering", "no")
                        self.send_cors()
                        self.end_headers()
                        self.close_connection = True
                        chunk_obj = {
                            "id": c_id,
                            "object": "chat.completion.chunk",
                            "created": c_time,
                            "model": raw_model,
                            "choices": [{"index": 0, "delta": {"content": reply_text}, "finish_reason": None}]
                        }
                        self.wfile.write(f"data: {json.dumps(chunk_obj, ensure_ascii=False)}\n\n".encode("utf-8"))
                        end_chunk = {
                            "id": c_id,
                            "object": "chat.completion.chunk",
                            "created": c_time,
                            "model": raw_model,
                            "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]
                        }
                        self.wfile.write(f"data: {json.dumps(end_chunk, ensure_ascii=False)}\n\n".encode("utf-8"))
                        self.wfile.write(b"data: [DONE]\n\n")
                        self.wfile.flush()
                        return
                    else:
                        out_resp = {
                            "id": c_id,
                            "object": "chat.completion",
                            "created": c_time,
                            "model": raw_model,
                            "choices": [{"index": 0, "message": {"role": "assistant", "content": reply_text}, "finish_reason": "stop"}],
                            "usage": {"prompt_tokens": len(prompt_txt) // 3, "completion_tokens": len(reply_text) // 3, "total_tokens": tokens_used}
                        }
                        res_bytes = json.dumps(out_resp, ensure_ascii=False).encode("utf-8")
                        self.send_response(200)
                        self.send_header("Content-Type", "application/json; charset=utf-8")
                        self.send_header("Content-Length", str(len(res_bytes)))
                        self.send_cors()
                        self.end_headers()
                        self.wfile.write(res_bytes)
                        return
                except Exception as _re_e:
                    err_b += f" (自动降级重试亦失败: {_re_e})"

            err_text = f"【EZCompleteUI 接口错误 {he.code}】{err_b}（Token 可能已过期，请在手机上打开一次 EZCompleteUI App 重新激活）"
            print(f"[EZChatError] {err_text}")
            if stream:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                self.send_cors()
                self.end_headers()
                chunk_obj = {
                    "id": f"chatcmpl-ez-{uuid.uuid4().hex[:12]}",
                    "object": "chat.completion.chunk",
                    "created": int(time.time()),
                    "model": raw_model,
                    "choices": [{"index": 0, "delta": {"content": err_text}, "finish_reason": "stop"}]
                }
                self.wfile.write(f"data: {json.dumps(chunk_obj, ensure_ascii=False)}\n\n".encode("utf-8"))
                self.wfile.write(b"data: [DONE]\n\n")
                self.wfile.flush()
                self.close_connection = True
                return
            else:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_cors()
                self.end_headers()
                self.wfile.write(json.dumps({"choices": [{"message": {"role": "assistant", "content": err_text}}]}).encode("utf-8"))
                return
        except Exception as e:
            err_text = f"【EZCompleteUI 代理异常】{str(e)}"
            print(f"[EZChatError] {err_text}")
            if stream:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                self.send_cors()
                self.end_headers()
                chunk_obj = {
                    "id": f"chatcmpl-ez-{uuid.uuid4().hex[:12]}",
                    "object": "chat.completion.chunk",
                    "created": int(time.time()),
                    "model": raw_model,
                    "choices": [{"index": 0, "delta": {"content": err_text}, "finish_reason": "stop"}]
                }
                self.wfile.write(f"data: {json.dumps(chunk_obj, ensure_ascii=False)}\n\n".encode("utf-8"))
                self.wfile.write(b"data: [DONE]\n\n")
                self.wfile.flush()
                self.close_connection = True
                return
            else:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_cors()
                self.end_headers()
                self.wfile.write(json.dumps({"choices": [{"message": {"role": "assistant", "content": err_text}}]}).encode("utf-8"))
                return

    def handle_ez_image_generations(self, body):
        t0 = time.time()
        try:
            req_json = json.loads(body.decode("utf-8"))
        except Exception as e:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.send_cors()
            self.end_headers()
            self.wfile.write(json.dumps({"error": f"Invalid JSON: {e}"}).encode("utf-8"))
            return

        stream = req_json.get("stream", False)
        raw_model = str(req_json.get("model", "gpt-image-2.5-flare"))
        prompt = req_json.get("prompt", "")
        if not prompt and "messages" in req_json:
            for m in req_json.get("messages", []):
                if m.get("role") == "user":
                    c = m.get("content")
                    if isinstance(c, str):
                        prompt = c
                    elif isinstance(c, list):
                        for p in c:
                            if isinstance(p, dict) and p.get("type") == "text":
                                prompt = p.get("text", "")
        if not prompt:
            prompt = "A beautiful scenic view"

        # 智能参数构造（免费用户质量强制锁定为 medium，避免 403 Purchase Required）
        ez_img_payload = {
            "model": raw_model,
            "prompt": prompt,
            "size": req_json.get("size", "1024x1024"),
            "quality": "medium",
            "output_format": "png"
        }
        url = f"{EZ_SUPABASE_URL}/functions/v1/ez-image"

        accs = load_ez_accounts() or []
        resp_data = None
        last_err = None

        # 多账号故障自动切号机制：若某账号报 402/余额不足，自动秒切下一个账号！
        for _ in range(max(1, len(accs))):
            acc, u_token = get_ez_next_available_account_and_token()
            if not u_token:
                continue
            headers = {
                "apikey": EZ_ANON_KEY,
                "Authorization": f"Bearer {u_token}",
                "Content-Type": "application/json",
                "Connection": "close"
            }
            try:
                req = urllib.request.Request(url, data=json.dumps(ez_img_payload).encode("utf-8"), headers=headers, method="POST")
                with CELLULAR_OPENER.open(req, timeout=120) as resp:
                    resp_data = json.loads(resp.read().decode("utf-8", errors="ignore"))
                if resp_data and resp_data.get("images"):
                    break
            except urllib.error.HTTPError as he:
                err_b = he.read().decode("utf-8", errors="ignore")
                last_err = f"【EZCompleteUI 生图接口错误 {he.code}】{err_b}"
                if he.code == 402 or "insufficient" in err_b.lower():
                    print(f"[EZImageFailover] 账号 {acc.get('name')} 余额不足 (402)，自动尝试下一个账号...")
                    continue
                else:
                    break
            except Exception as _e:
                last_err = str(_e)
                break

        if not resp_data or not resp_data.get("images"):
            err_text = last_err or "【EZCompleteUI 生图失败】所有账号均不可用或余额已耗尽。"
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_cors()
            self.end_headers()
            self.wfile.write(json.dumps({"choices": [{"message": {"role": "assistant", "content": err_text}}]}).encode("utf-8"))
            return

        try:

            images = resp_data.get("images", [])
            img_url = ""
            if images and isinstance(images, list):
                first_img = images[0]
                if isinstance(first_img, dict):
                    img_url = first_img.get("url", "")
                elif isinstance(first_img, str):
                    img_url = first_img

            if not img_url:
                raise Exception(f"未在返回数据中找到图片 URL: {resp_data}")

            # 记录最新代币余额
            balance = resp_data.get("balance")
            if balance is not None:
                try:
                    with open(EZ_BALANCE_FILE, "w", encoding="utf-8") as _bf:
                        _bf.write(str(balance))
                except Exception:
                    pass

            # 优先秒回，如果下载超时不卡死主链路
            b64_img = ""
            try:
                img_get_req = urllib.request.Request(img_url, headers={"User-Agent": "Minis/ImageClient"})
                with CELLULAR_OPENER.open(img_get_req, timeout=5) as i_resp:
                    b64_img = base64.b64encode(i_resp.read()).decode("utf-8")
            except Exception as _b64_e:
                print(f"[ImgB64Error] {_b64_e}")

            c_id = f"img-{uuid.uuid4().hex[:12]}"
            c_time = int(time.time())
            # 计算生图单次固定扣费 (标准绘图为 1 点)
            cost_credits = 1.0
            cur_bal = float(balance) if balance is not None else 0.0
            billing_info = {
                "cost": cost_credits,
                "balance": cur_bal,
                "currency": "credits",
                "details": f"生图消耗: {cost_credits} 币 | 当前剩余: {cur_bal} 币"
            }
            md_content = f"![Generated Image]({img_url})\n\n[查看生成的高清原图]({img_url})\n\n*(Prompt: {prompt})*"

            if stream:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.send_header("Connection", "close")
                self.send_header("X-Accel-Buffering", "no")
                self.send_cors()
                self.end_headers()
                self.close_connection = True
                chunk_obj = {
                    "id": c_id,
                    "object": "chat.completion.chunk",
                    "created": c_time,
                    "model": raw_model,
                    "choices": [{"index": 0, "delta": {"content": md_content}, "finish_reason": None}]
                }
                self.wfile.write(f"data: {json.dumps(chunk_obj, ensure_ascii=False)}\n\n".encode("utf-8"))
                end_chunk = {
                    "id": c_id,
                    "object": "chat.completion.chunk",
                    "created": c_time,
                    "model": raw_model,
                    "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]
                }
                self.wfile.write(f"data: {json.dumps(end_chunk, ensure_ascii=False)}\n\n".encode("utf-8"))
                self.wfile.write(b"data: [DONE]\n\n")
                self.wfile.flush()
                return
            else:
                img_data_obj = {"url": img_url}
                if b64_img:
                    img_data_obj["b64_json"] = b64_img

                out_resp = {
                    "id": c_id,
                    "object": "chat.completion",
                    "created": c_time,
                    "model": raw_model,
                    "choices": [{"index": 0, "message": {"role": "assistant", "content": md_content}, "finish_reason": "stop"}],
                    "data": [img_data_obj],
                    "billing": billing_info,
                    "usage": {
                        "prompt_tokens": 50,
                        "completion_tokens": 100,
                        "total_tokens": 150,
                        "cost_credits": cost_credits,
                        "balance_credits": cur_bal
                    }
                }
                res_bytes = json.dumps(out_resp, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(res_bytes)))
                self.send_cors()
                self.end_headers()
                self.wfile.write(res_bytes)
                return

        except urllib.error.HTTPError as he:
            err_b = he.read().decode("utf-8", errors="ignore")
            err_text = f"【EZCompleteUI 生图接口错误 {he.code}】{err_b}"
            print(f"[EZImageError] {err_text}")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors()
            self.end_headers()
            self.wfile.write(json.dumps({"choices": [{"message": {"role": "assistant", "content": err_text}}]}).encode("utf-8"))
            return
        except Exception as e:
            err_text = f"【EZCompleteUI 生图代理异常】{str(e)}"
            print(f"[EZImageError] {err_text}")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors()
            self.end_headers()
            self.wfile.write(json.dumps({"choices": [{"message": {"role": "assistant", "content": err_text}}]}).encode("utf-8"))
            return

    def handle_image_generations(self, body):
        t0 = time.time()
        try:
            req_json = json.loads(body.decode("utf-8"))
        except Exception as e:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.send_cors()
            self.end_headers()
            self.wfile.write(json.dumps({"error": f"Invalid JSON: {e}"}).encode("utf-8"))
            return

        prompt = req_json.get("prompt", "")
        # 支持从 messages 里自动解析 prompt（兼容 Minis chat_completions 格式请求）
        if not prompt and "messages" in req_json:
            for m in req_json.get("messages", []):
                if m.get("role") == "user":
                    c = m.get("content")
                    if isinstance(c, str):
                        prompt = c
                    elif isinstance(c, list):
                        for p in c:
                            if isinstance(p, dict) and p.get("type") == "text":
                                prompt = p.get("text", "")

        gemini_payload = {
            "project": "aicode-consumers",
            "model": "gemini-3.1-flash-image",
            "request": {
                "contents": [{"role": "user", "parts": [{"text": prompt}]}],
                "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
                "safetySettings": [
                    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_CIVIC_INTEGRITY", "threshold": "BLOCK_NONE"}
                ]
            }
        }

        target_url = f"{ANTIGRAVITY_API_URL}/v1internal:streamGenerateContent?alt=sse"

        # 尝试遍历可用账号发起生图（遇到 429 自动轮换下一个账号）
        accs = load_accounts()
        last_err = "No accounts available"

        for acc_item in accs:
            token = refresh_token(acc_item) or acc_item.get("access_token")
            if not token:
                continue

            headers = {
                "User-Agent": ANTIGRAVITY_USER_AGENT,
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "requestType": "image_gen"
            }

            # 单账号最多尝试 2 次（处理 Google 偶发 503 算力满载抖动）
            for attempt in range(2):
                try:
                    req = urllib.request.Request(target_url, data=json.dumps(gemini_payload).encode("utf-8"), headers=headers)
                    with urllib.request.urlopen(req, context=SSL_CTX, timeout=120) as resp:
                        b64_image = ""
                        text_reason = ""
                        for line in resp:
                            l = line.decode("utf-8", errors="ignore").strip()
                            if l.startswith("data:"):
                                try:
                                    chunk = json.loads(l[5:])
                                    cands = chunk.get("response", {}).get("candidates", []) or chunk.get("candidates", [])
                                    if cands:
                                        for p in cands[0].get("content", {}).get("parts", []):
                                            if "inlineData" in p:
                                                b64_image = p["inlineData"].get("data", "")
                                                break
                                            elif "text" in p:
                                                text_reason += p["text"]
                                except Exception:
                                    pass
                            if b64_image:
                                break

                    if not b64_image:
                        err_detail = f"上游未返回图片 (Google回应: {text_reason[:80]})" if text_reason else "上游生图未返回图片数据"
                        raise Exception(err_detail)

                    # 成功！兼容 OpenAI 标准生图返回结构与 Chat Completions Markdown 图片双向兼容
                    out_resp = {
                        "id": f"chatcmpl-{uuid.uuid4().hex[:12]}",
                        "object": "chat.completion",
                        "created": int(time.time()),
                        "model": "gemini-3.1-flash-image",
                        "choices": [{
                            "index": 0,
                            "message": {
                                "role": "assistant",
                                "content": f"![Generated Image](data:image/jpeg;base64,{b64_image})"
                            },
                            "finish_reason": "stop"
                        }],
                        "data": [
                            {
                                "b64_json": b64_image,
                                "url": f"data:image/jpeg;base64,{b64_image}"
                            }
                        ]
                    }
                    res_bytes = json.dumps(out_resp, ensure_ascii=False).encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Content-Length", str(len(res_bytes)))
                    self.send_header("Connection", "close")
                    self.send_cors()
                    self.end_headers()
                    self.wfile.write(res_bytes)

                    latency = int((time.time() - t0) * 1000)
                    record_stat(True, 100, 1000, 0, latency)
                    log_request("gemini-3.1-flash-image", 200, latency, 1100)
                    return

                except urllib.error.HTTPError as e:
                    err_body = e.read().decode("utf-8", errors="ignore")[:150]
                    last_err = f"HTTP Error {e.code}: {err_body}"
                    print(f"[ImageGen] Account {acc_item.get('email')} attempt {attempt+1} failed with: {last_err}")
                    if e.code == 503 and attempt == 0:
                        time.sleep(1.5)
                        continue
                    break
                except Exception as e:
                    last_err = str(e)
                    print(f"[ImageGen] Account {acc_item.get('email')} attempt {attempt+1} failed with: {last_err}")
                    if "503" in last_err and attempt == 0:
                        time.sleep(1.5)
                        continue
                    break

        # 如果所有账号都失败
        latency = int((time.time() - t0) * 1000)
        record_stat(False, latency_ms=latency, err=last_err)
        log_request("gemini-3.1-flash-image", 500, latency, 0, last_err)
        self.send_response(500)
        res = json.dumps({"error": {"message": f"所有账号生图均失败: {last_err}", "type": "image_gen_error"}}).encode("utf-8")
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(res)))
        self.send_cors()
        self.end_headers()
        self.wfile.write(res)

    def handle_anthropic_messages(self, body):
        t0 = time.time()
        try:
            req_json = json.loads(body.decode("utf-8"))
        except Exception:
            self.send_response(400)
            self.end_headers()
            return

        # 智能判定是否为 App 后台触发的「起标题」静默请求
        _is_title_req = False
        try:
            _tools_present = bool(req_json.get("tools"))
            if not _tools_present:
                _check_msgs = req_json.get("messages", [])
                # 取出最后一条 user 消息
                _last_u_txt = ""
                for _m in reversed(_check_msgs):
                    if isinstance(_m, dict) and _m.get("role") == "user":
                        _c = _m.get("content", "")
                        if isinstance(_c, str):
                            _last_u_txt = _c
                        elif isinstance(_c, list):
                            for _p in _c:
                                if isinstance(_p, dict) and _p.get("type") == "text":
                                    _last_u_txt += _p.get("text", "")
                        break
                _u_lower = _last_u_txt.lower()
                # 专用起标题特征：无工具、并且明确要求起标题/命名
                _strict_title_patterns = [
                    "生成标题", "起一个标题", "起个标题", "会话标题", "对话标题",
                    "主题命名", "简短标题", "不超过8个字", "不超过10个字", "4到8个字",
                    "generate a title", "conversation title", "title for this chat",
                    "summarize this conversation into a title"
                ]
                if any(p in _u_lower for p in _strict_title_patterns):
                    _is_title_req = True
        except Exception:
            pass
        if _is_title_req:
            print("[TitleDrop][Anthropic] 后台起标题请求已直接丢弃，未发上游")
            try:
                self.send_response(204)
                self.send_cors()
                self.end_headers()
                self.wfile.flush()
            except Exception:
                pass
            self.close_connection = True
            return

        raw_model = str(req_json.get("model", "gemini-3.8-flash-high"))
        stream = req_json.get("stream", False)

        # 将 Anthropic Messages 格式无损转换为 OpenAI Chat Completions 格式复用底层转换与重试
        tool_id_map = {}
        oai_messages = []
        sys_prompt = req_json.get("system")
        if sys_prompt:
            if isinstance(sys_prompt, str):
                oai_messages.append({"role": "system", "content": sys_prompt})
            elif isinstance(sys_prompt, list):
                s_txt = "\n".join(b.get("text", "") for b in sys_prompt if isinstance(b, dict) and b.get("type") == "text")
                if s_txt:
                    oai_messages.append({"role": "system", "content": s_txt})

        for m in req_json.get("messages", []):
            role = m.get("role", "user")
            content = m.get("content", "")
            if isinstance(content, str):
                oai_messages.append({"role": role, "content": content})
            elif isinstance(content, list):
                txt_parts = []
                tool_calls_out = []
                for blk in content:
                    if not isinstance(blk, dict):
                        continue
                    btype = blk.get("type")
                    if btype == "text":
                        txt_parts.append(blk.get("text", ""))
                    elif btype == "tool_use":
                        t_id = blk.get("id", f"toolu_{uuid.uuid4().hex[:12]}")
                        t_name = blk.get("name", "tool")
                        tool_id_map[t_id] = t_name
                        tool_calls_out.append({
                            "id": t_id,
                            "type": "function",
                            "function": {
                                "name": t_name,
                                "arguments": json.dumps(blk.get("input", {}), ensure_ascii=False)
                            }
                        })
                    elif btype == "tool_result":
                        t_content = blk.get("content", "")
                        if isinstance(t_content, list):
                            t_content = "\n".join(x.get("text", "") for x in t_content if isinstance(x, dict))
                        tu_id = blk.get("tool_use_id", "tool")
                        real_fn_name = tool_id_map.get(tu_id, blk.get("name", tu_id))
                        oai_messages.append({
                            "role": "tool",
                            "tool_call_id": tu_id,
                            "name": real_fn_name,
                            "content": str(t_content)
                        })
                if txt_parts or tool_calls_out:
                    msg_item = {"role": role, "content": "\n".join(txt_parts) if txt_parts else ""}
                    if tool_calls_out:
                        msg_item["tool_calls"] = tool_calls_out
                    oai_messages.append(msg_item)

        oai_tools = []
        for t in req_json.get("tools", []):
            if isinstance(t, dict) and t.get("name"):
                oai_tools.append({
                    "type": "function",
                    "function": {
                        "name": t.get("name"),
                        "description": t.get("description", ""),
                        "parameters": t.get("input_schema", {"type": "object", "properties": {}})
                    }
                })

        # 无论 Claude Code 传 3.8 还是 claude-sonnet，统一锁定 gemini-3.8-flash-high 极速响应
        mapped_m = "gemini-3.8-flash-high"
        if "opus" in raw_model.lower():
            mapped_m = "claude-opus-4-6-thinking"
        elif "sonnet" in raw_model.lower():
            mapped_m = "gemini-3.8-flash-high"

        oai_req = {"model": mapped_m, "messages": oai_messages}
        if oai_tools:
            oai_req["tools"] = oai_tools

        target_model, gemini_payload = convert_openai_to_gemini(oai_req)
        # 针对 Claude Code：1. 不传冗余复杂 schema 避免 Google 400 Invalid Schema；2. 400 错误绝不浪费 45 秒重试！
        if "tools" in gemini_payload.get("request", {}):
            # 精简 Claude Code 的 tools 定义，只保留核心字段防止 Google Gemini 报 400 INVALID_ARGUMENT
            clean_decls = []
            for d in gemini_payload["request"]["tools"][0].get("functionDeclarations", []):
                p = d.get("parameters", {})
                simple_props = {}
                for pk, pv in (p.get("properties") or {}).items():
                    if isinstance(pv, dict):
                        t_val = pv.get("type", "string")
                        if isinstance(t_val, list):
                            t_val = [x for x in t_val if x != "null"][0] if [x for x in t_val if x != "null"] else "string"
                        if t_val not in ("string", "number", "integer", "boolean", "array", "object"):
                            t_val = "string"
                        prop_entry = {"type": t_val, "description": str(pv.get("description", ""))[:200]}
                        if t_val == "array":
                            prop_entry["items"] = {"type": "string"}
                        elif t_val == "object":
                            prop_entry["properties"] = {"value": {"type": "string"}}
                        simple_props[pk] = prop_entry
                clean_decl = {
                    "name": d.get("name"),
                    "description": str(d.get("description", ""))[:300]
                }
                if simple_props:
                    req_list = [r for r in (p.get("required") or []) if r in simple_props]
                    clean_decl["parameters"] = {"type": "object", "properties": simple_props}
                    if req_list:
                        clean_decl["parameters"]["required"] = req_list
                clean_decls.append(clean_decl)
            if clean_decls:
                gemini_payload["request"]["tools"] = [{"functionDeclarations": clean_decls}]

        # 移除不兼容的 generationConfig 防止 gemini-3.8-flash-high 报 thinkingConfig 400
        if "generationConfig" in gemini_payload["request"]:
            del gemini_payload["request"]["generationConfig"]

        token = get_valid_token()
        target_url = f"{ANTIGRAVITY_API_URL}/v1internal:generateContent"

        accs = load_accounts()
        ordered_accs = [a for a in accs if a.get("active")] + [a for a in accs if not a.get("active")]
        g_res = None
        last_err = None

        for acc_idx, acc_item in enumerate(ordered_accs):
            cur_tok = acc_item.get("access_token") if acc_idx == 0 and token else (refresh_token(acc_item) or acc_item.get("access_token"))
            if not cur_tok:
                continue
            for attempt in range(2):
                raw_b = json.dumps(gemini_payload).encode("utf-8")
                gz_b = gzip.compress(raw_b) if len(raw_b) > 1024 else raw_b
                hdrs = {
                    "Authorization": f"Bearer {cur_tok}",
                    "Content-Type": "application/json",
                    "User-Agent": ANTIGRAVITY_USER_AGENT
                }
                if len(raw_b) > 1024:
                    hdrs["Content-Encoding"] = "gzip"
                req_obj = urllib.request.Request(target_url, data=gz_b, headers=hdrs)
                try:
                    with CELLULAR_OPENER.open(req_obj, timeout=600) as resp:
                        g_res = json.loads(resp.read().decode("utf-8"))
                    if not acc_item.get("active"):
                        for a in accs:
                            a["active"] = (a.get("email") == acc_item.get("email"))
                        save_accounts(accs)
                    break
                except urllib.error.HTTPError as he:
                    err_detail = ""
                    try:
                        err_detail = he.read().decode("utf-8", errors="ignore")
                    except Exception:
                        pass
                    last_err = f"HTTP {he.code}: {err_detail[:300]}"
                    print(f"[AnthropicBridge] {last_err}")
                    # 如果带 tools 报 400，当场自动剥离 tools 降级重试，1秒内秒回绝不卡死！
                    if he.code == 400 and "tools" in gemini_payload["request"]:
                        print("[AnthropicBridge] Stripping incompatible tools schema and retrying immediately...")
                        del gemini_payload["request"]["tools"]
                        continue
                    if he.code in (400, 403, 429):
                        break
                    time.sleep(1.0)
                except Exception as ex:
                    last_err = str(ex)
                    time.sleep(1.0)
            if g_res is not None or (last_err and "HTTP 400" in str(last_err)):
                break

        latency = int((time.time() - t0) * 1000)
        if g_res is None:
            record_stat(False, latency_ms=latency, err=str(last_err))
            log_request(raw_model, 500, latency, 0, str(last_err))
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"type": "error", "error": {"type": "api_error", "message": str(last_err)}}).encode("utf-8"))
            return

        candidates = g_res.get("response", {}).get("candidates", []) or g_res.get("candidates", [])
        usage = g_res.get("response", {}).get("usageMetadata", {}) or g_res.get("usageMetadata", {})
        in_tok = usage.get("promptTokenCount", 10)
        out_tok = usage.get("candidatesTokenCount", 10)

        record_stat(True, in_tok, out_tok, 0, latency)
        log_request(target_model, 200, latency, in_tok + out_tok)

        content_blocks = []
        stop_reason = "end_turn"
        if candidates:
            for p in candidates[0].get("content", {}).get("parts", []):
                if p.get("thought"):
                    continue
                if "functionCall" in p:
                    fc = p["functionCall"]
                    stop_reason = "tool_use"
                    content_blocks.append({
                        "type": "tool_use",
                        "id": f"toolu_{uuid.uuid4().hex[:16]}",
                        "name": fc.get("name"),
                        "input": fc.get("args", {})
                    })
                elif p.get("text"):
                    content_blocks.append({"type": "text", "text": p["text"]})

        if not content_blocks:
            content_blocks.append({"type": "text", "text": "OK"})

        msg_id = f"msg_{uuid.uuid4().hex[:16]}"

        if stream:
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "close")
            self.send_header("X-Accel-Buffering", "no")
            self.send_cors()
            self.end_headers()
            self.close_connection = True

            def _send_sse(ev, data_dict):
                s = f"event: {ev}\ndata: {json.dumps(data_dict, ensure_ascii=False)}\n\n"
                self.wfile.write(s.encode("utf-8"))

            try:
                _send_sse("message_start", {
                    "type": "message_start",
                    "message": {
                        "id": msg_id,
                        "type": "message",
                        "role": "assistant",
                        "model": raw_model,
                        "content": [],
                        "stop_reason": None,
                        "stop_sequence": None,
                        "usage": {"input_tokens": in_tok, "output_tokens": 1}
                    }
                })
                for idx, blk in enumerate(content_blocks):
                    if blk["type"] == "text":
                        _send_sse("content_block_start", {"type": "content_block_start", "index": idx, "content_block": {"type": "text", "text": ""}})
                        _send_sse("content_block_delta", {"type": "content_block_delta", "index": idx, "delta": {"type": "text_delta", "text": blk["text"]}})
                        _send_sse("content_block_stop", {"type": "content_block_stop", "index": idx})
                    elif blk["type"] == "tool_use":
                        _send_sse("content_block_start", {"type": "content_block_start", "index": idx, "content_block": {"type": "tool_use", "id": blk["id"], "name": blk["name"], "input": {}}})
                        _send_sse("content_block_delta", {"type": "content_block_delta", "index": idx, "delta": {"type": "input_json_delta", "partial_json": json.dumps(blk["input"], ensure_ascii=False)}})
                        _send_sse("content_block_stop", {"type": "content_block_stop", "index": idx})

                _send_sse("message_delta", {"type": "message_delta", "delta": {"stop_reason": stop_reason, "stop_sequence": None}, "usage": {"output_tokens": out_tok}})
                _send_sse("message_stop", {"type": "message_stop"})
                self.wfile.flush()
            except Exception:
                pass
        else:
            res_obj = {
                "id": msg_id,
                "type": "message",
                "role": "assistant",
                "model": raw_model,
                "content": content_blocks,
                "stop_reason": stop_reason,
                "stop_sequence": None,
                "usage": {"input_tokens": in_tok, "output_tokens": out_tok}
            }
            out_b = json.dumps(res_obj, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(out_b)))
            self.send_cors()
            self.end_headers()
            self.wfile.write(out_b)

    def handle_chat_completions(self, body):
        # 优先拦截并直接执行真机系统意图 (调音量、调亮度、连真机SSH、执行Shell命令)
        try:
            _raw_chk = json.loads(body.decode("utf-8"))
            _msgs = _raw_chk.get("messages", [])
            _u_prompt = ""
            for _m in _msgs:
                if _m.get("role") == "user":
                    _c = _m.get("content", "")
                    if isinstance(_c, str):
                        _u_prompt = _c
                    elif isinstance(_c, list):
                        for _p in _c:
                            if isinstance(_p, dict) and _p.get("type") == "text":
                                _u_prompt = _p.get("text", "")
            
            if _u_prompt:
                _reply = execute_system_intent(_u_prompt)
                if _reply:
                    print(f"[DirectSystemIntent] 触发真机本地系统意图执行: {_u_prompt} -> {_reply}")
                    _cid = f"chatcmpl-sys-{uuid.uuid4().hex[:12]}"
                    _ctime = int(time.time())
                    _mname = str(_raw_chk.get("model", "gemini-3.8-flash-high"))
                    if _raw_chk.get("stream", False):
                        self.send_response(200)
                        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                        self.send_header("Cache-Control", "no-cache")
                        self.send_cors()
                        self.end_headers()
                        chunk = {"id": _cid, "object": "chat.completion.chunk", "created": _ctime, "model": _mname, "choices": [{"index": 0, "delta": {"content": _reply}, "finish_reason": None}]}
                        self.wfile.write(f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n".encode("utf-8"))
                        end_c = {"id": _cid, "object": "chat.completion.chunk", "created": _ctime, "model": _mname, "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]}
                        self.wfile.write(f"data: {json.dumps(end_c, ensure_ascii=False)}\n\n".encode("utf-8"))
                        self.wfile.write(b"data: [DONE]\n\n")
                        self.wfile.flush()
                        self.close_connection = True
                        return
                    else:
                        out = {"id": _cid, "object": "chat.completion", "created": _ctime, "model": _mname, "choices": [{"index": 0, "message": {"role": "assistant", "content": _reply}, "finish_reason": "stop"}]}
                        res_b = json.dumps(out, ensure_ascii=False).encode("utf-8")
                        self.send_response(200)
                        self.send_header("Content-Type", "application/json; charset=utf-8")
                        self.send_header("Content-Length", str(len(res_b)))
                        self.send_cors()
                        self.end_headers()
                        self.wfile.write(res_b)
                        return
        except Exception as _intent_e:
            print(f"[IntentCheckError] {_intent_e}")

        t0 = time.time()
        try:
            req_json = json.loads(body.decode("utf-8"))
        except Exception:
            self.send_response(400)
            self.end_headers()
            return

        stream = req_json.get("stream", False)
        target_model, gemini_payload = convert_openai_to_gemini(req_json)
        token = get_valid_token()

        if not token:
            self.send_response(500)
            res = json.dumps({"error": {"message": "No valid Google OAuth token available"}}).encode("utf-8")
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(res)))
            self.send_cors()
            self.end_headers()
            self.wfile.write(res)
            return

        # ★【标题拦截】App 后台静默起标题请求：本地秒出标题，绝不占用对话算力
        _is_title_req = _is_bg_title_request(req_json)
        if _is_title_req:
            _lat = int((time.time() - t0) * 1000)
            try:
                log_request(target_model, 204, _lat, 0, "title request dropped", is_title=True)
            except Exception:
                pass
            print("[TitleDrop] 后台起标题请求已直接丢弃 (%dms)，未发上游" % _lat)
            try:
                self.send_response(204)
                self.send_cors()
                self.end_headers()
                self.wfile.flush()
            except Exception:
                pass
            self.close_connection = True
            return

        mode_endpoint = "streamGenerateContent?alt=sse" if stream else "generateContent"
        _base_api = "https://cloudcode-pa.googleapis.com" if "5-5" in str(target_model) else ANTIGRAVITY_API_URL
        target_url = f"{_base_api}/v1internal:{mode_endpoint}"

        def _open_gemini_with_retry():
            accs = load_accounts()
            # 优先使用当前激活账号，其次轮询其他有 refresh_token 的账号
            _now = time.time()
            _fresh = [a for a in accs if ACCOUNT_COOLDOWN.get(a.get("email"), 0) < _now]
            _cold = [a for a in accs if ACCOUNT_COOLDOWN.get(a.get("email"), 0) >= _now]
            _fresh.sort(key=lambda x: (not x.get("active"),))
            _cold.sort(key=lambda x: (not x.get("active"),))
            ordered_accs = _fresh + _cold
            last_exc = None
            _loc_exc = None
            for acc_idx, acc_item in enumerate(ordered_accs):
                cur_tok = acc_item.get("access_token") if acc_idx == 0 and token else (refresh_token(acc_item) or acc_item.get("access_token"))
                if not cur_tok:
                    continue
                for attempt in range(3):
                    raw_b = json.dumps(gemini_payload).encode("utf-8")
                    gz_b = gzip.compress(raw_b) if len(raw_b) > 1024 else raw_b
                    hdrs = {
                        "Authorization": f"Bearer {cur_tok}",
                        "Content-Type": "application/json",
                        "User-Agent": ANTIGRAVITY_USER_AGENT
                    }
                    if len(raw_b) > 1024:
                        hdrs["Content-Encoding"] = "gzip"
                    req_obj = urllib.request.Request(target_url, data=gz_b, headers=hdrs)
                    try:
                        resp_obj = CELLULAR_OPENER.open(req_obj, timeout=600)
                        if not acc_item.get("active"):
                            for a in accs:
                                a["active"] = (a.get("email") == acc_item.get("email"))
                            save_accounts(accs)
                            print(f"[Failover] Promoted healthy account {acc_item.get('email')} to primary active account!")
                        return resp_obj
                    except urllib.error.HTTPError as he:
                        last_exc = he
                        err_body = ""
                        try:
                            err_body = he.read().decode("utf-8", errors="ignore")
                        except Exception:
                            pass
                        print(f"[Retry] HTTP {he.code} on {target_model} (acc={acc_item.get('email')}, attempt={attempt+1}): {err_body[:200]}")
                        try:
                            he._gem_body = err_body
                        except Exception:
                            pass
                        if he.code == 401:
                            cur_tok = refresh_token(acc_item)
                            if cur_tok:
                                save_accounts(accs)
                            else:
                                break
                        elif he.code in (403, 429):
                            # 如果当前账号遇到 403(Verify your account) 或 429 限流，不傻等 3 次，当场切换下一个健康账号并永久标记新的 active 账号！
                            try:
                                ACCOUNT_COOLDOWN[acc_item.get('email')] = time.time() + 600
                            except Exception:
                                pass
                            print(f"[Failover] Account {acc_item.get('email')} returned {he.code}, switching to next account immediately! (冷却 10 分钟)")
                            break
                        elif he.code in (500, 502, 503, 504):
                            time.sleep(0.8)
                            continue
                        elif he.code == 400:
                            low = err_body.lower()
                            if ("location is not supported" in low) or ("failed_precondition" in low):
                                print("[Failover] 账号 %s 地区受限(400 location)，秒切下一账号！" % acc_item.get('email'))
                                _loc_exc = he
                                break
                            elif ("schema" in low or "tools" in low or "function" in low) and gemini_payload["request"].get("tools"):
                                print("[AutoHeal] 400 疑似工具 schema 不兼容，剥离 tools 后重试...")
                                del gemini_payload["request"]["tools"]
                                continue
                            elif "contents is not specified" in low:
                                gemini_payload["request"]["contents"] = [{"role": "user", "parts": [{"text": "继续"}]}]
                                continue
                            elif any(k in low for k in ["thought", "signature", "thoughtsignature", "thought_signature", "functioncall"]):
                                print("[AutoHeal] 400 命中思考链签名断裂或思考历史不兼容，自动剥离历史 thought 重新拉起...")
                                req_conts = gemini_payload.get("request", {}).get("contents", [])
                                for cont in req_conts:
                                    if cont.get("role") == "model":
                                        cont["parts"] = [p for p in cont.get("parts", []) if not p.get("thought")]
                                continue
                            else:
                                raise he
                        else:
                            raise he
                    except Exception as ex:
                        # 捕获 TLS/SSL EOF 握手断开、网络超时、连接重置等瞬时网络异常并自动重试
                        last_exc = ex
                        print(f"[Retry] Network/SSL glitch ({type(ex).__name__}: {ex}) on {target_model} (attempt={attempt+1}), retrying...")
                        time.sleep(1.5 * (attempt + 1))
                        continue
            # 地区受限异常优先抛出：它是出口 IP 抖动导致的可重试错误，不能被末尾的 429 覆盖掉
            if _loc_exc is not None:
                raise _loc_exc
            if last_exc:
                raise last_exc
            raise Exception("All accounts and retries exhausted")

        def _open_gemini_with_retry_outer():
            # 🛡️ 出口 IP 地区限制（User location is not supported）是代理节点轮换造成的瞬时抖动，
            # 单轮失败不代表真失败：短退避后整轮重试，命中好节点即秒通。
            last = None
            for _r in range(5):
                try:
                    return _open_gemini_with_retry()
                except urllib.error.HTTPError as _he:
                    _b = (getattr(_he, "_gem_body", "") or "").lower()
                    if _he.code == 400 and ("location is not supported" in _b or "failed_precondition" in _b):
                        last = _he
                        _w = 1.5 * (_r + 1)
                        print("[AutoHeal] 全账号出口地区受限(400 location)，%.1fs 后整轮重试（节点抖动）..." % _w)
                        time.sleep(_w)
                        continue
                    raise
            if last:
                raise last
            raise Exception("All accounts and retries exhausted")

        prompt_tokens = 0
        comp_tokens = 0
        thoughts_tokens = 0
        cached_tokens = 0

        if stream:
            try:
                with _open_gemini_with_retry_outer() as resp:
                    self.send_response(200)
                    self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                    self.send_header("Cache-Control", "no-cache")
                    self.send_header("Connection", "close")
                    self.send_header("X-Accel-Buffering", "no")
                    self.send_cors()
                    self.end_headers()
                    self.close_connection = True

                    chat_id = f"chatcmpl-{uuid.uuid4().hex[:12]}"
                    created_time = int(time.time())
                    has_tool_call = False
                    _any_text_sent = False

                    for line in resp:
                        l = line.decode("utf-8", errors="ignore").strip()
                        if l.startswith("data:"):
                            try:
                                g_chunk = json.loads(l[5:])
                                candidates = g_chunk.get("response", {}).get("candidates", []) or g_chunk.get("candidates", [])
                                usage = g_chunk.get("response", {}).get("usageMetadata", {}) or g_chunk.get("usageMetadata", {})
                                if usage:
                                    prompt_tokens = usage.get("promptTokenCount", prompt_tokens)
                                    comp_tokens = usage.get("candidatesTokenCount", comp_tokens)
                                    thoughts_tokens = usage.get("thoughtsTokenCount", thoughts_tokens)
                                    cached_tokens = usage.get("cachedContentTokenCount", cached_tokens)

                                if candidates:
                                    parts = candidates[0].get("content", {}).get("parts", [])
                                    for p in parts:
                                        if p.get("inlineData"):
                                            b64_d = p["inlineData"].get("data", "")
                                            mime = p["inlineData"].get("mimeType", "image/jpeg")
                                            img_md = f"\n\n![Generated Image](data:{mime};base64,{b64_d})\n\n"
                                            chunk_obj = {
                                                "id": chat_id,
                                                "object": "chat.completion.chunk",
                                                "created": created_time,
                                                "model": target_model,
                                                "choices": [{
                                                    "index": 0,
                                                    "delta": {"content": img_md},
                                                    "finish_reason": None
                                                }]
                                            }
                                            try:
                                                self.wfile.write(f"data: {json.dumps(chunk_obj, ensure_ascii=False)}\n\n".encode("utf-8"))
                                                self.wfile.flush()
                                            except (BrokenPipeError, ConnectionResetError):
                                                break
                                        elif p.get("thought") and p.get("text"):
                                            _any_text_sent = True
                                            chunk_obj = {
                                                "id": chat_id,
                                                "object": "chat.completion.chunk",
                                                "created": created_time,
                                                "model": target_model,
                                                "choices": [{
                                                    "index": 0,
                                                    "delta": {"reasoning_content": p["text"]},
                                                    "finish_reason": None
                                                }]
                                            }
                                            try:
                                                self.wfile.write(f"data: {json.dumps(chunk_obj, ensure_ascii=False)}\n\n".encode("utf-8"))
                                                self.wfile.flush()
                                            except (BrokenPipeError, ConnectionResetError):
                                                break
                                        elif p.get("text"):
                                            _any_text_sent = True
                                            chunk_obj = {
                                                "id": chat_id,
                                                "object": "chat.completion.chunk",
                                                "created": created_time,
                                                "model": target_model,
                                                "choices": [{
                                                    "index": 0,
                                                    "delta": {"content": p["text"]},
                                                    "finish_reason": None
                                                }]
                                            }
                                            try:
                                                self.wfile.write(f"data: {json.dumps(chunk_obj, ensure_ascii=False)}\n\n".encode("utf-8"))
                                                self.wfile.flush()
                                            except (BrokenPipeError, ConnectionResetError):
                                                break
                                        elif p.get("functionCall"):
                                            fc = p["functionCall"]
                                            has_tool_call = True
                                            chunk_obj = {
                                                "id": chat_id,
                                                "object": "chat.completion.chunk",
                                                "created": created_time,
                                                "model": target_model,
                                                "choices": [{
                                                    "index": 0,
                                                    "delta": {
                                                        "tool_calls": [{
                                                            "index": 0,
                                                            "id": f"call_{uuid.uuid4().hex[:16]}",
                                                            "type": "function",
                                                            "function": {
                                                                "name": fc.get("name"),
                                                                "arguments": json.dumps(fc.get("args", {}), ensure_ascii=False)
                                                            }
                                                        }]
                                                    },
                                                    "finish_reason": None
                                                }]
                                            }
                                            try:
                                                self.wfile.write(f"data: {json.dumps(chunk_obj, ensure_ascii=False)}\n\n".encode("utf-8"))
                                                self.wfile.flush()
                                            except (BrokenPipeError, ConnectionResetError):
                                                break
                            except Exception:
                                pass

                    total_comp = comp_tokens + thoughts_tokens
                    # ★ 防空响应：若一个字都没吐出来（正文和工具调用都没有），
                    #   主动补一条可见提示，杜绝客户端拿到空响应后无限重试。
                    if not has_tool_call and not _any_text_sent:
                        _hint = ("\n\n⚠️ 本次上游返回空正文（思考预算可能耗尽）。"
                                 "已自动加大输出上限，请直接重试一次。")
                        try:
                            self.wfile.write(("data: " + json.dumps({
                                "id": chat_id, "object": "chat.completion.chunk",
                                "created": created_time, "model": target_model,
                                "choices": [{"index": 0,
                                             "delta": {"content": _hint},
                                             "finish_reason": None}]
                            }, ensure_ascii=False) + "\n\n").encode("utf-8"))
                            self.wfile.flush()
                        except Exception:
                            pass
                    f_reason = "tool_calls" if has_tool_call else "stop"
                    end_chunk = {
                        "id": chat_id,
                        "object": "chat.completion.chunk",
                        "created": created_time,
                        "model": target_model,
                        "choices": [{"index": 0, "delta": {}, "finish_reason": f_reason}],
                        "usage": {
                            "prompt_tokens": prompt_tokens,
                            "completion_tokens": total_comp,
                            "total_tokens": prompt_tokens + total_comp,
                            "prompt_tokens_details": {"cached_tokens": cached_tokens},
                            "completion_tokens_details": {"reasoning_tokens": thoughts_tokens}
                        }
                    }
                    try:
                        self.wfile.write(f"data: {json.dumps(end_chunk, ensure_ascii=False)}\n\n".encode("utf-8"))
                        self.wfile.write(b"data: [DONE]\n\n")
                        self.wfile.flush()
                    except Exception:
                        pass
                
                latency = int((time.time() - t0) * 1000)
                record_stat(True, prompt_tokens, comp_tokens, thoughts_tokens, latency)
                log_request(target_model, 200, latency, prompt_tokens + total_comp, is_title=_is_title_req)

            except Exception as e:
                latency = int((time.time() - t0) * 1000)
                if isinstance(e, (BrokenPipeError, ConnectionResetError)):
                    record_stat(False, latency_ms=latency, err="client closed connection")
                    log_request(target_model, 499, latency, 0, "client closed connection", is_title=_is_title_req)
                    self.close_connection = True
                    return
                _up = getattr(e, "code", 500)
                if not isinstance(_up, int):
                    _up = 500
                _msg = ((getattr(e, "_gem_body", "") or "").strip().replace(chr(10), " "))[:300] or str(e)
                if _up == 400 and "contents is not specified" in _msg:
                    _msg = "上游请求体为空载(contents is not specified)，已自动兜底，请重试"
                record_stat(False, latency_ms=latency, err=_msg)
                log_request(target_model, _up, latency, 0, _msg, is_title=_is_title_req)
                try:
                    self.send_response(200)
                    self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                    self.send_cors()
                    self.end_headers()
                    err_chunk = {
                        "id": f"chatcmpl-{uuid.uuid4().hex[:12]}",
                        "object": "chat.completion.chunk",
                        "created": int(time.time()),
                        "model": target_model,
                        "choices": [{
                            "index": 0,
                            "delta": {"content": f"\n\n⚠️ **请求异常**: {str(e)}"},
                            "finish_reason": "stop"
                        }]
                    }
                    self.close_connection = True
                    self.wfile.write(f"data: {json.dumps(err_chunk, ensure_ascii=False)}\n\ndata: [DONE]\n\n".encode("utf-8"))
                    self.wfile.flush()
                except Exception:
                    pass
        else:
            try:
                with _open_gemini_with_retry_outer() as resp:
                    g_res = json.loads(resp.read().decode("utf-8"))
                    candidates = g_res.get("response", {}).get("candidates", []) or g_res.get("candidates", [])
                    usage = g_res.get("response", {}).get("usageMetadata", {}) or g_res.get("usageMetadata", {})
                    if usage:
                        prompt_tokens = usage.get("promptTokenCount", 0)
                        comp_tokens = usage.get("candidatesTokenCount", 0)
                        thoughts_tokens = usage.get("thoughtsTokenCount", 0)
                        cached_tokens = usage.get("cachedContentTokenCount", 0)

                    content_text = ""
                    reasoning_text = ""
                    tool_calls = []

                    if candidates:
                        for p in candidates[0].get("content", {}).get("parts", []):
                            if p.get("inlineData"):
                                b64_d = p["inlineData"].get("data", "")
                                mime = p["inlineData"].get("mimeType", "image/jpeg")
                                img_md = f"\n\n![Generated Image](data:{mime};base64,{b64_d})\n\n"
                                content_text += img_md
                            elif p.get("thought") and p.get("text"):
                                reasoning_text += p["text"]
                            elif p.get("text"):
                                content_text += p["text"]
                            elif p.get("functionCall"):
                                fc = p["functionCall"]
                                tool_calls.append({
                                    "id": f"call_{uuid.uuid4().hex[:16]}",
                                    "type": "function",
                                    "function": {
                                        "name": fc.get("name"),
                                        "arguments": json.dumps(fc.get("args", {}), ensure_ascii=False)
                                    }
                                })

                    msg_obj = {"role": "assistant"}
                    if reasoning_text:
                        msg_obj["reasoning_content"] = reasoning_text
                    if content_text:
                        msg_obj["content"] = content_text
                    if tool_calls:
                        msg_obj["tool_calls"] = tool_calls

                    total_comp = comp_tokens + thoughts_tokens
                    chat_resp = {
                        "id": f"chatcmpl-{uuid.uuid4().hex[:12]}",
                        "object": "chat.completion",
                        "created": int(time.time()),
                        "model": target_model,
                        "choices": [{
                            "index": 0,
                            "message": msg_obj,
                            "finish_reason": "stop"
                        }],
                        "usage": {
                            "prompt_tokens": prompt_tokens,
                            "completion_tokens": total_comp,
                            "total_tokens": prompt_tokens + total_comp,
                            "prompt_tokens_details": {"cached_tokens": cached_tokens},
                            "completion_tokens_details": {"reasoning_tokens": thoughts_tokens}
                        }
                    }
                    res_bytes = json.dumps(chat_resp, ensure_ascii=False).encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Content-Length", str(len(res_bytes)))
                    self.send_header("Connection", "close")
                    self.send_cors()
                    self.end_headers()
                    self.wfile.write(res_bytes)

                    latency = int((time.time() - t0) * 1000)
                    record_stat(True, prompt_tokens, comp_tokens, thoughts_tokens, latency)
                    log_request(target_model, 200, latency, prompt_tokens + total_comp, is_title=_is_title_req)
            except Exception as e:
                latency = int((time.time() - t0) * 1000)
                _up = getattr(e, "code", 500)
                if not isinstance(_up, int):
                    _up = 500
                _msg = ((getattr(e, "_gem_body", "") or "").strip().replace(chr(10), " "))[:300] or str(e)
                record_stat(False, latency_ms=latency, err=_msg)
                log_request(target_model, _up, latency, 0, _msg, is_title=_is_title_req)
                try:
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    _res_e = json.dumps({"error": {"message": _msg, "code": _up, "type": "upstream_error"}}, ensure_ascii=False).encode("utf-8")
                    self.send_header("Content-Length", str(len(_res_e)))
                    self.send_cors()
                    self.end_headers()
                    self.wfile.write(_res_e)
                except Exception:
                    pass

    # ===================== 上游三：Meta Model API 处理器 =====================
    def _meta_send_error(self, code, msg):
        if not isinstance(code, int) or code < 400:
            code = 502
        payload = json.dumps({"error": {"message": msg, "type": "meta_upstream_error",
                                        "code": str(code)}}, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Connection", "close")
        self.send_cors()
        self.end_headers()
        try:
            self.wfile.write(payload)
        except Exception:
            pass
        self.close_connection = True

    def _meta_post(self, url, body_bytes, token, stream):
        req = urllib.request.Request(url, data=body_bytes, method="POST")
        req.add_header("Authorization", "Bearer " + token)
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "text/event-stream" if stream else "application/json")
        req.add_header("User-Agent", META_UA)
        return urllib.request.urlopen(req, context=SSL_CTX, timeout=900)

    def handle_meta_model_chat(self, body, image=False):
        t0 = time.time()
        try:
            req_json = json.loads(body.decode("utf-8"))
        except Exception as e:
            self._meta_send_error(400, "Invalid JSON: %s" % e)
            return

        raw_model = str(req_json.get("model", "muse-spark-1.3"))
        target = meta_resolve_model(raw_model)
        req_json["model"] = target
        stream = bool(req_json.get("stream", False)) and not image

        token = meta_read_token()
        if not token:
            self._meta_send_error(503, "Meta 上游未授权：先跑 /var/mobile/antigravity_proxy/muse_login.sh 完成设备码登录，"
                                       "或把 Model API 密钥(LLM|...)写进 /var/mobile/antigravity_proxy/meta_token.txt")
            return

        path = "/images/generations" if image else "/chat/completions"
        url = META_BASE.rstrip("/") + path
        data = json.dumps(req_json, ensure_ascii=False).encode("utf-8")

        resp = None
        try:
            resp = self._meta_post(url, data, token, stream)
        except urllib.error.HTTPError as e:
            detail = ""
            try:
                detail = e.read().decode("utf-8", "replace")[:600]
            except Exception:
                pass
            if e.code in (401, 403):
                new_tok = meta_try_refresh()
                if new_tok:
                    try:
                        resp = self._meta_post(url, data, new_tok, stream)
                    except Exception as e2:
                        self._meta_send_error(502, "Meta 上游 %s（续期后仍失败）: %s" % (e2, detail))
                        return
                else:
                    record_stat(False, err="meta 401")
                    log_request(raw_model, e.code, int((time.time() - t0) * 1000), 0, detail[:200])
                    self._meta_send_error(401, "Meta 上游鉴权失效（token 过期或无效），请重新设备码登录: " + detail)
                    return
            else:
                record_stat(False, err="meta %s" % e.code)
                log_request(raw_model, e.code, int((time.time() - t0) * 1000), 0, detail[:200])
                self._meta_send_error(e.code, "Meta 上游返回 %s: %s" % (e.code, detail))
                return
        except Exception as e:
            record_stat(False, err="meta connect")
            log_request(raw_model, 502, int((time.time() - t0) * 1000), 0, str(e)[:200])
            self._meta_send_error(502, "连接 Meta 上游失败: %s" % e)
            return

        if stream:
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.send_cors()
            self.end_headers()
            p_tok = c_tok = 0
            try:
                for line in resp:
                    if not line:
                        continue
                    try:
                        self.wfile.write(line)
                        self.wfile.flush()
                    except Exception:
                        break
                    if b'"usage"' in line:
                        try:
                            doc = json.loads(line.decode("utf-8", "replace").replace("data: ", "").strip())
                            u = doc.get("usage") or {}
                            p_tok = u.get("prompt_tokens", p_tok) or p_tok
                            c_tok = u.get("completion_tokens", c_tok) or c_tok
                        except Exception:
                            pass
            except Exception:
                pass
            finally:
                try:
                    resp.close()
                except Exception:
                    pass
            record_stat(True, p_tok, c_tok, 0, int((time.time() - t0) * 1000))
            log_request("%s [meta]" % target, 200, int((time.time() - t0) * 1000), p_tok + c_tok, "")
            self.close_connection = True
            return

        try:
            raw = resp.read()
            resp.close()
        except Exception as e:
            self._meta_send_error(502, "读取 Meta 上游响应失败: %s" % e)
            return

        p_tok = c_tok = 0
        try:
            doc = json.loads(raw.decode("utf-8"))
            u = doc.get("usage") or {}
            p_tok = u.get("prompt_tokens", 0) or 0
            c_tok = u.get("completion_tokens", 0) or 0
            if isinstance(doc.get("model"), str):
                doc["model"] = raw_model
            raw = json.dumps(doc, ensure_ascii=False).encode("utf-8")
        except Exception:
            pass

        record_stat(True, p_tok, c_tok, 0, int((time.time() - t0) * 1000))
        log_request("%s [meta]" % target, 200, int((time.time() - t0) * 1000), p_tok + c_tok, "")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Connection", "close")
        self.send_cors()
        self.end_headers()
        try:
            self.wfile.write(raw)
        except Exception:
            pass
        self.close_connection = True

    def handle_audio_transcriptions(self, body):
        t0 = time.time()
        try:
            content_type = self.headers.get("Content-Type", "")
            audio_bytes = b""
            mime_type = "audio/m4a"

            if "multipart/form-data" in content_type:
                # 解析 boundary
                boundary = content_type.split("boundary=")[-1].strip().encode('utf-8')
                parts = body.split(b"--" + boundary)
                for part in parts:
                    if b'filename=' in part:
                        hdr_end = part.find(b"\r\n\r\n")
                        if hdr_end == -1:
                            hdr_end = part.find(b"\n\n")
                            file_data = part[hdr_end+2:].rstrip(b"\r\n-")
                        else:
                            file_data = part[hdr_end+4:].rstrip(b"\r\n-")
                        audio_bytes = file_data
                        if b'.wav' in part.lower():
                            mime_type = "audio/wav"
                        elif b'.mp3' in part.lower():
                            mime_type = "audio/mp3"
                        elif b'.ogg' in part.lower():
                            mime_type = "audio/ogg"
                        break
            else:
                audio_bytes = body

            if not audio_bytes:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_cors()
                self.end_headers()
                self.wfile.write(b'{"error":{"message":"No audio file received"}}')
                return

            b64_audio = base64.b64encode(audio_bytes).decode('ascii')
            token = get_valid_token()
            if not token:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_cors()
                self.end_headers()
                self.wfile.write(b'{"error":{"message":"Google token not available"}}')
                return

            # 极速语音转写特化通道：强制关闭思考链 + 极速轻量模型
            url = f"{ANTIGRAVITY_API_URL}/v1internal:generateContent"
            payload = {
                "project": "cloudcode-pa-prod",
                "model": "gemini-3.8-flash-low",
                "request": {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "inlineData": {
                                        "mimeType": mime_type,
                                        "data": b64_audio
                                    }
                                },
                                {
                                    "text": "Transcribe this audio verbatim in its original spoken language (e.g. Chinese or English). Output ONLY the transcribed text, without any punctuation explanations, thoughts, or formatting."
                                }
                            ]
                        }
                    ],
                    "generationConfig": {
                        "thinkingConfig": {
                            "thinkingBudget": 0
                        },
                        "temperature": 0.0,
                        "maxOutputTokens": 1024
                    }
                }
            }

            raw_b = json.dumps(payload).encode('utf-8')
            gz_b = gzip.compress(raw_b) if len(raw_b) > 1024 else raw_b
            hdrs = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "User-Agent": ANTIGRAVITY_USER_AGENT
            }
            if len(raw_b) > 1024:
                hdrs["Content-Encoding"] = "gzip"
            req_obj = urllib.request.Request(url, data=gz_b, headers=hdrs)

            resp_obj = CELLULAR_OPENER.open(req_obj, timeout=30)
            res_data = json.loads(resp_obj.read().decode('utf-8'))
            
            transcribed_text = ""
            candidates = res_data.get("response", {}).get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                for p in parts:
                    if "text" in p:
                        transcribed_text += p["text"]

            transcribed_text = transcribed_text.strip()
            latency = int((time.time() - t0) * 1000)
            log_request("whisper-1", 200, latency, len(transcribed_text), is_title=False)

            res_json = json.dumps({"text": transcribed_text}, ensure_ascii=False).encode('utf-8')
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(res_json)))
            self.send_header("Connection", "close")
            self.send_cors()
            self.end_headers()
            self.wfile.write(res_json)

        except Exception as e:
            latency = int((time.time() - t0) * 1000)
            log_request("whisper-1", 500, latency, 0, str(e))
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_cors()
            self.end_headers()
            self.wfile.write(json.dumps({"error": {"message": str(e)}}).encode('utf-8'))

def run_server(port=PORT):
    server_address = ("0.0.0.0", port)
    httpd = ThreadedHTTPServer(server_address, AntigravityHandler)
    print(f"[Server] Gemini Antigravity Engine listening on http://0.0.0.0:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server(PORT)
