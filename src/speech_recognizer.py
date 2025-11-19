"""
Speech Recognition Module
Converts audio input to text using Google's Speech Recognition API
"""

import logging
from typing import Optional

# Import speech recognition after audio compatibility is set up
import speech_recognition as sr

logger = logging.getLogger(__name__)


class SpeechRecognizer:
    """Handles speech recognition from microphone input."""
    
    def __init__(self, language: str = "en-US", timeout: int = 10):
        """
        Initialize the speech recognizer.
        
        Args:
            language: Language code (default: en-US)
            timeout: Timeout for listening in seconds
        """
        self.recognizer = sr.Recognizer()
        self.language = language
        self.timeout = timeout
    
    def listen(self) -> Optional[str]:
        """
        Listen to microphone input and convert to text.
        
        Returns:
            Recognized text or None if recognition fails
        """
        try:
            with sr.Microphone() as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                print("Listening... (speak now)")
                audio = self.recognizer.listen(
                    source,
                    timeout=self.timeout,
                    phrase_time_limit=30
                )
            
            # Use Google Speech Recognition
            print("Processing speech...")
            text = self.recognizer.recognize_google(audio, language=self.language)
            print(f"You said: {text}")
            return text
            
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            print("Sorry, I couldn't understand what you said. Please try again.")
            return None
        except sr.RequestError as e:
            logger.error(f"Speech recognition error: {e}")
            print(f"Speech recognition service error: {e}")
            return None
        except sr.WaitTimeoutError:
            logger.warning("Listening timeout")
            print("No speech detected. Please try again.")
            return None
        except OSError as e:
            if "PyAudio" in str(e):
                logger.warning("PyAudio not found. Using test mode - enter text instead.")
                print("\n--- TEST MODE (PyAudio not available) ---")
                text = input("Enter your message: ").strip()
                if text:
                    print(f"You said: {text}")
                    return text
                return None
            raise
        except Exception as e:
            logger.error(f"Unexpected error during speech recognition: {e}")
            print(f"An error occurred: {e}")
            # Fallback to text input for testing
            if "PyAudio" in str(e) or "Microphone" in str(e):
                print("\n--- TEST MODE (Microphone not available) ---")
                text = input("Enter your message: ").strip()
                if text:
                    print(f"You said: {text}")
                    return text
            return None
