from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional, Dict
from .config import PROJECT_NAME, VERSION
from .ai_response_model import generate_reply
from .speech_to_text import transcribe_audio
from .text_to_speech import synthesize_voice

app = FastAPI(title=PROJECT_NAME, version=VERSION)

class STTRequest(BaseModel):
    audio_b64: str = Field(..., description="Base64 WAV/PCM")
    lang: Optional[str] = "en"

class ChatRequest(BaseModel):
    text: str
    context: Dict = Field(default_factory=dict)

class TTSRequest(BaseModel):
    text: str
    voice: Optional[str] = "female_hero"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/stt")
def stt(req: STTRequest):
    text = transcribe_audio(req.audio_b64, req.lang)
    return {"text": text}

@app.post("/chat")
def chat(req: ChatRequest):
    reply = generate_reply(req.text, req.context)
    return {"reply": reply}

@app.post("/tts")
def tts(req: TTSRequest):
    audio_b64 = synthesize_voice(req.text, req.voice)
    return {"audio_b64": audio_b64}

# Run: uvicorn Backend.main:app --reload
