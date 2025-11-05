import os
from dotenv import load_dotenv

load_dotenv()

MOCK_MODE = os.getenv("MOCK_MODE", "TRUE").upper() == "TRUE"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
PROJECT_NAME = "AI-Driven NPC Backend"
VERSION = "1.0.0"
