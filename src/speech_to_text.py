from typing import Optional
from .config import MOCK_MODE
from .utils import ts

def transcribe_audio(b64_wav: str, lang: Optional[str] = "en") -> str:
    """
    Accepts base64-encoded WAV/PCM audio string.
    In MOCK_MODE, returns canned text.
    """
    # Bluff: pretend to do STT
    if MOCK_MODE:
        return "hello npc, any quest for me?"
    # Real STT integration would go here (e.g., Whisper/Google), omitted.
    return f"[{ts()}] (STT placeholder)"
