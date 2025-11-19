from typing import Dict
from .config import MOCK_MODE, OPENAI_API_KEY, MODEL_NAME
from .utils import ts

# Optional: real API (won't run in MOCK_MODE)
try:
    from openai import OpenAI
    _client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
except Exception:
    _client = None

SYSTEM_PROMPT = (
    "You are an in-game NPC. Keep replies short (1-2 lines), "
    "context-aware, and friendly."
)

def generate_reply(user_text: str, npc_context: Dict) -> str:
    if MOCK_MODE or not OPENAI_API_KEY or _client is None:
        # Simple rule-based mock so demo always works
        name = npc_context.get("npc_name", "NPC")
        loc = npc_context.get("location", "village square")
        if "hello" in user_text.lower():
            return f"{name}: Hello, traveler! It's {ts()} at the {loc}."
        if "quest" in user_text.lower():
            return f"{name}: I have a small task—find 3 herbs near the river."
        if "bye" in user_text.lower():
            return f"{name}: Farewell! May your path be clear."
        return f"{name}: I heard rumors about bandits near the old bridge."
    # Real call (if keys present and MOCK_MODE=False)
    msg = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Context:{npc_context}\nPlayer:{user_text}"},
    ]
    try:
        resp = _client.chat.completions.create(
            model=MODEL_NAME,
            messages=msg,
            temperature=0.7,
            max_tokens=80,
        )
        return resp.choices[0].message.content.strip()
    except Exception:
        return "NPC: (whispers) The winds are quiet…"
