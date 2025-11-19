"""
__init__.py for src package
"""

# Import audio compatibility first
from src import audio_compat

from src.speech_recognizer import SpeechRecognizer
from src.text_generator import TextGenerator
from src.speech_synthesizer import SpeechSynthesizer
from src.ai_npc import AINPC

__all__ = [
    'SpeechRecognizer',
    'TextGenerator',
    'SpeechSynthesizer',
    'AINPC'
]
