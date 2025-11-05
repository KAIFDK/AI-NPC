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
