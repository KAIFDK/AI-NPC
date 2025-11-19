"""
Configuration settings for AI NPC system
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Ollama Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
OLLAMA_TEMPERATURE = float(os.getenv("OLLAMA_TEMPERATURE", "0.7"))
OLLAMA_MAX_TOKENS = int(os.getenv("OLLAMA_MAX_TOKENS", "150"))

# Speech Recognition Configuration
SPEECH_LANGUAGE = os.getenv("SPEECH_LANGUAGE", "en-US")
SPEECH_TIMEOUT = int(os.getenv("SPEECH_TIMEOUT", "10"))
SPEECH_PHRASE_TIME_LIMIT = 30

# Text-to-Speech Configuration
TTS_VOICE_RATE = int(os.getenv("TTS_VOICE_RATE", "150"))
TTS_VOICE_VOLUME = float(os.getenv("TTS_VOICE_VOLUME", "1.0"))

# AI NPC Configuration
SYSTEM_PROMPT = """You are a helpful and friendly AI assistant. 
Respond naturally and conversationally. Keep responses concise (1-2 sentences). 
Be engaging and helpful."""

LISTENING_TIMEOUT = 10  # seconds before timeout during listening
