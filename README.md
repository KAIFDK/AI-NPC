<<<<<<< HEAD
# AI NPC - Speech Recognition & Response System

An intelligent conversational AI system that recognizes speech input and responds with synthesized speech output using **local LLM via Ollama**.

## Features

- **Speech Recognition**: Convert spoken words to text using Google Speech Recognition API
- **Local LLM Responses**: Generate intelligent responses using Ollama (no API keys needed!)
- **Text-to-Speech**: Convert AI responses back to natural speech
- **Interactive Conversation**: Real-time dialogue with the AI
- **Offline Capable**: Once models are downloaded, runs completely locally

## Requirements

- **Ollama**: Download from https://ollama.ai
- A local LLM model (e.g., Mistral, Llama2, Zephyr)
- Microphone and speaker
- Python 3.8+

## Setup

### 1. Install Ollama

Download and install from https://ollama.ai

### 2. Pull a Model

Open terminal and download a model (first time only):
```bash
ollama pull mistral
```

Other available models:
```bash
ollama pull neural-chat
ollama pull llama2
ollama pull zephyr
```

### 3. Start Ollama Service

The Ollama service typically starts automatically. You can verify it's running by checking:
```bash
http://localhost:11434/api/tags
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment

Edit `.env` file:
```
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral
```

## Usage

Run the application:
```bash
python main.py
```

The system will:
1. Listen for your speech input
2. Convert speech to text
3. Generate an AI response via Ollama
4. Speak the response back to you

## Configuration

Edit `.env` to customize:

```
# Ollama API endpoint
OLLAMA_BASE_URL=http://localhost:11434

# Model selection (mistral, llama2, neural-chat, zephyr, etc.)
OLLAMA_MODEL=mistral

# Model parameters
OLLAMA_TEMPERATURE=0.7        # Lower = more focused, Higher = more creative
OLLAMA_MAX_TOKENS=150         # Max response length

# Speech settings
SPEECH_LANGUAGE=en-US
SPEECH_TIMEOUT=10
TTS_VOICE_RATE=150            # Words per minute
TTS_VOICE_VOLUME=1.0          # 0.0 to 1.0
```

## Project Structure

```
AI NPC/
├── src/
│   ├── __init__.py
│   ├── speech_recognizer.py      # Speech recognition module
│   ├── text_generator.py         # Ollama LLM integration
│   ├── speech_synthesizer.py     # Text-to-speech module
│   ├── ai_npc.py                 # Main AI NPC orchestrator
│   └── config.py                 # Configuration settings
├── tests/
├── requirements.txt
├── .env                          # Local configuration (not committed)
└── main.py                       # Entry point
```

## Dependencies

- **SpeechRecognition**: Speech to text conversion
- **pyttsx3**: Text-to-speech synthesis
- **requests**: HTTP client for Ollama API
- **python-dotenv**: Environment variable management

## Troubleshooting

### "Could not connect to Ollama"
- Make sure Ollama is running: `ollama serve`
- Check OLLAMA_BASE_URL in `.env`
- Verify http://localhost:11434 is accessible

### "Model not found"
- Pull the model: `ollama pull mistral`
- Check model name in `.env` OLLAMA_MODEL setting

### Speech Recognition Issues
- Ensure microphone is connected and working
- Check microphone permissions
- Try adjusting SPEECH_TIMEOUT in `.env`

## License

MIT License

## Support

For issues or questions, please check Ollama documentation or the repository.
=======
# AI-Driven NPC Interaction (Unreal + Python Backend)

This repo demonstrates a modular pipeline:

**Player Voice → STT → NLP → TTS → NPC Animation**

### 🔧 Quick Start
```bash
cd Backend
python -m venv .venv && . .venv/Scripts/activate  # Windows
# or: source .venv/bin/activate  (mac/linux)

pip install -r requirements.txt
cp .env.example .env   # MOCK_MODE=TRUE by default
uvicorn Backend.main:app --reload


# Unreal Integration (HTTP)

- Use **Web Request (HTTP)** nodes (or C++/Blueprint) to call:
  - `POST http://127.0.0.1:8000/stt` with `{ "audio_b64": "<base64>" }`
  - `POST http://127.0.0.1:8000/chat` with `{ "text": "hi", "context": { "npc_name": "Elder", "location": "Market" } }`
  - `POST http://127.0.0.1:8000/tts` with `{ "text": "NPC line" }` → returns `audio_b64` playable after decode.

Blueprint tip:
- Convert mic capture → WAV → Base64.
- Decode TTS `audio_b64` → write temp .wav → play on NPC Audio Component.

[ Player (Mic Input) ]
           │
           ▼
[ Speech-to-Text (Python API) ]
           │
           ▼
[ AI Response Generator (LLM/NLP Model) ]
           │
           ▼
[ Text-to-Speech Engine ]
           │
           ▼
[ Unreal Engine NPC (Voice + Animation) ]

AI-NPC/
│
├── Backend/
│   ├── main.py
│   ├── ai_response_model.py
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│   ├── config.py
│   ├── utils.py
│   ├── requirements.txt
│   └── tests/
│
├── UnrealProject/
│   └── README_Unreal_HTTP.md
│
└── README.md

#🧠 API Endpoints

| Endpoint  | Method | Description                                |
| --------- | ------ | ------------------------------------------ |
| `/health` | GET    | Checks server status                       |
| `/stt`    | POST   | Converts Base64 audio → text               |
| `/chat`   | POST   | Generates AI NPC reply from text + context |
| `/tts`    | POST   | Converts text → Base64 audio for NPC voice |

Player: "Hey, do you know where the temple is?"
NPC: "You must follow the river path eastward — the old temple awaits beyond the fog."

🧱 Future Enhancements

Multi-NPC memory and context persistence

Emotion detection from player tone

Improved TTS voices and real-time lip-sync

Integration with MetaHuman framework

Local LLM deployment for offline inference

##👨‍💻 Author & Acknowledgment

Developed by:## SAI KAIRAN AND GOLLA SUKUMAR
Course: B.Tech Computer Science (AI/ML Focus)
Project Type: AI-Driven Interactive NPC System
Tools: Unreal Engine 5, FastAPI, Python 3.10, OpenAI API

Special thanks to open-source AI communities and Unreal developers for inspiration and support.

##📜 License

This project is shared for educational and research purposes only.
You are free to use, modify, and present it in academic environments.

##🧩 Quick Recap

🎙️ Player speaks → 🧠 AI understands → 💬 NPC replies → 🔊 Voice plays → 🎮 Immersion achieved.
>>>>>>> 54d257d1aa249a80ffb8a3cb0ee6ccbc78041664
