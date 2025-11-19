"""
Speech Synthesis Module
Converts text to speech using pyttsx3 text-to-speech engine
"""

import pyttsx3
import logging
from typing import Optional
from src.config import TTS_VOICE_RATE, TTS_VOICE_VOLUME

logger = logging.getLogger(__name__)


class SpeechSynthesizer:
    """Handles text-to-speech synthesis."""
    
    def __init__(self, rate: int = TTS_VOICE_RATE, volume: float = TTS_VOICE_VOLUME):
        """
        Initialize the speech synthesizer.
        
        Args:
            rate: Speech rate (default: 150 words per minute)
            volume: Volume level (0.0 to 1.0)
        """
        try:
            self.engine = pyttsx3.init()
            self.rate = rate
            self.volume = volume
            
            # Configure engine
            self.engine.setProperty('rate', self.rate)
            self.engine.setProperty('volume', self.volume)
            
            logger.info("Speech synthesizer initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize speech synthesizer: {e}")
            raise
    
    def speak(self, text: str) -> bool:
        """
        Convert text to speech and play it.
        
        Args:
            text: Text to convert to speech
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if not text:
                logger.warning("Empty text provided for speech synthesis")
                return False
            
            print(f"AI: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
            return True
            
        except Exception as e:
            logger.error(f"Error during speech synthesis: {e}")
            return False
    
    def set_rate(self, rate: int):
        """Set speech rate (words per minute)."""
        try:
            self.rate = rate
            self.engine.setProperty('rate', self.rate)
        except Exception as e:
            logger.error(f"Error setting speech rate: {e}")
    
    def set_volume(self, volume: float):
        """Set volume level (0.0 to 1.0)."""
        try:
            if 0.0 <= volume <= 1.0:
                self.volume = volume
                self.engine.setProperty('volume', self.volume)
            else:
                logger.warning(f"Volume must be between 0.0 and 1.0, got {volume}")
        except Exception as e:
            logger.error(f"Error setting volume: {e}")
    
    def stop(self):
        """Stop current speech."""
        try:
            self.engine.stop()
        except Exception as e:
            logger.error(f"Error stopping speech: {e}")
