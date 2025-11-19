import base64
from typing import Optional
from .config import MOCK_MODE
from .utils import ts

def synthesize_voice(text: str, voice: Optional[str] = "female_hero") -> str:
    """
    Returns base64 WAV audio. In MOCK_MODE, returns a tiny silent wav header.
    """
    if MOCK_MODE:
        # 44-byte WAV header for 1-second silence @8kHz mono, super tiny demo
        silent_wav = (
            b"RIFF$\x80\x00\x00WAVEfmt "
            b"\x10\x00\x00\x00\x01\x00\x01\x00@\x1f\x00\x00@\x1f\x00\x00"
            b"\x01\x00\x08\x00data\x00\x80\x00\x00" + b"\x80"*0x800
        )
        return base64.b64encode(silent_wav).decode("utf-8")
    # Real TTS (e.g., Polly/ElevenLabs) would go here; omitted for repo.
    return base64.b64encode(f"[{ts()}] {text}".encode()).decode()
