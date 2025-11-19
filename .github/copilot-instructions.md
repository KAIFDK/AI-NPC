# AI NPC Speech Recognition & Response System

This project creates an interactive AI system that recognizes speech input and responds with synthesized speech output using **local Ollama LLM**.

## Project Setup Status

- [x] Verify that the copilot-instructions.md file in the .github directory is created.
- [x] Clarify Project Requirements - Python project for speech recognition and AI response
- [x] Scaffold the Project - Project directories and base structure created
- [x] Customize the Project - Core modules with Ollama integration implemented
- [x] Install Required Extensions - None required for this Python project
- [x] Compile the Project - Dependencies installed
- [x] Create and Run Task - Development task setup
- [ ] Launch the Project - Ready to run
- [ ] Ensure Documentation is Complete - README and instructions updated

## Project Overview

An AI NPC system with three core components:
1. **Speech Recognition**: Convert speech to text (Google Speech Recognition)
2. **Local LLM Response**: Generate intelligent responses via Ollama (runs locally)
3. **Speech Synthesis**: Convert responses to speech (pyttsx3)

## Key Changes from OpenAI to Ollama

- Removed OpenAI API dependency
- Added Ollama local LLM support via HTTP API
- No API keys required - runs completely offline after setup
- Models: Mistral, Llama2, Neural-Chat, Zephyr, etc.

## Key Files

- `src/speech_recognizer.py` - Google Speech Recognition API wrapper
- `src/text_generator.py` - Ollama local LLM integration
- `src/speech_synthesizer.py` - pyttsx3 text-to-speech engine
- `src/ai_npc.py` - Main orchestrator combining all components
- `main.py` - Application entry point

## Setup Instructions

1. Install Ollama from https://ollama.ai
2. Pull a model: `ollama pull mistral`
3. Ensure Ollama is running (default: http://localhost:11434)
4. Configure `.env` with Ollama settings
5. Run: `python main.py`
