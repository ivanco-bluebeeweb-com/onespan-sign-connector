"""Extension declaration, capabilities, health check for OneSpan Sign Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "onespan-sign-connector",
    version="0.1.0",
    display_name="OneSpan Sign",
    icon="icon.svg",
    capabilities=["onespan_sign:manage"],
    description="Official Imperal connector for OneSpan Sign (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("onespan_sign_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} OneSpan Sign connection(s) configured." if count else "Not connected yet."
    }
