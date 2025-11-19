"""
Main AI NPC Module
Orchestrates speech recognition, text generation, and speech synthesis
"""

import logging
from typing import Optional
from src.speech_recognizer import SpeechRecognizer
from src.text_generator import TextGenerator
from src.speech_synthesizer import SpeechSynthesizer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AINPC:
    """Main AI NPC system that combines all modules."""
    
    def __init__(self, language: str = "en-US"):
        """
        Initialize the AI NPC system.
        
        Args:
            language: Language for speech recognition
        """
        try:
            self.speech_recognizer = SpeechRecognizer(language=language)
            self.text_generator = TextGenerator()
            self.speech_synthesizer = SpeechSynthesizer()
            self.is_running = False
            logger.info("AI NPC system initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize AI NPC: {e}")
            raise
    
    def process_speech_to_response(self) -> Optional[str]:
        """
        Complete pipeline: listen -> generate -> speak.
        
        Returns:
            The generated response or None if any step fails
        """
        try:
            # Step 1: Listen to user input
            user_input = self.speech_recognizer.listen()
            if not user_input:
                return None
            
            # Step 2: Generate AI response
            response = self.text_generator.generate_response(user_input)
            if not response:
                return None
            
            # Step 3: Speak the response
            self.speech_synthesizer.speak(response)
            
            return response
            
        except Exception as e:
            logger.error(f"Error in speech-to-response pipeline: {e}")
            return None
    
    def start_conversation(self, max_exchanges: Optional[int] = None):
        """
        Start an interactive conversation loop.
        
        Args:
            max_exchanges: Maximum number of exchanges (None for infinite)
        """
        self.is_running = True
        exchange_count = 0
        
        print("\n" + "="*50)
        print("AI NPC System Started")
        print("Say 'exit', 'quit', or 'bye' to end the conversation")
        print("="*50 + "\n")
        
        try:
            while self.is_running:
                if max_exchanges and exchange_count >= max_exchanges:
                    print("Maximum exchanges reached. Ending conversation.")
                    break
                
                exchange_count += 1
                print(f"\n--- Exchange {exchange_count} ---")
                
                response = self.process_speech_to_response()
                
                if response and any(word in response.lower() for word in ['exit', 'quit', 'bye']):
                    print("\nEnding conversation...")
                    break
        
        except KeyboardInterrupt:
            print("\n\nConversation interrupted by user.")
        except Exception as e:
            logger.error(f"Error during conversation: {e}")
            print(f"An error occurred: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """Stop the AI NPC system."""
        self.is_running = False
        self.text_generator.reset_conversation()
        self.speech_synthesizer.stop()
        logger.info("AI NPC system stopped")
