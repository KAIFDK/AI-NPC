"""
Text Generation Module
Uses Ollama for local LLM response generation
"""

import requests
import json
import logging
from typing import Optional
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL, OLLAMA_TEMPERATURE, OLLAMA_MAX_TOKENS, SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class TextGenerator:
    """Generates AI responses using Ollama local LLM."""
    
    def __init__(self, model: str = OLLAMA_MODEL, system_prompt: str = SYSTEM_PROMPT, base_url: str = OLLAMA_BASE_URL):
        """
        Initialize the text generator.
        
        Args:
            model: Ollama model to use (default: mistral)
            system_prompt: System instructions for the AI
            base_url: Ollama base URL (default: http://localhost:11434)
        """
        self.model = model
        self.system_prompt = system_prompt
        self.base_url = base_url
        self.api_endpoint = f"{base_url}/api/chat"
        self.conversation_history = []
        self._verify_connection()
    
    def _verify_connection(self) -> bool:
        """
        Verify that Ollama is running and accessible.
        
        Returns:
            True if connection is successful, False otherwise
        """
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                logger.info(f"Connected to Ollama at {self.base_url}")
                return True
            else:
                logger.error(f"Ollama returned status code {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            logger.error(f"Could not connect to Ollama at {self.base_url}. Make sure Ollama is running.")
            return False
        except Exception as e:
            logger.error(f"Error verifying Ollama connection: {e}")
            return False
    
    def generate_response(self, user_input: str) -> Optional[str]:
        """
        Generate an AI response to user input using Ollama.
        
        Args:
            user_input: The user's text input
            
        Returns:
            AI-generated response or None if generation fails
        """
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Prepare messages with system prompt
            messages = [
                {"role": "system", "content": self.system_prompt},
                *self.conversation_history
            ]
            
            # Make request to Ollama API
            payload = {
                "model": self.model,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": OLLAMA_TEMPERATURE,
                    "num_predict": OLLAMA_MAX_TOKENS
                }
            }
            
            response = requests.post(self.api_endpoint, json=payload, timeout=30)
            
            if response.status_code == 200:
                response_data = response.json()
                assistant_message = response_data.get("message", {}).get("content", "")
                
                if not assistant_message:
                    logger.warning("Ollama returned empty response")
                    return "I'm having trouble thinking right now. Please try again."
                
                # Add assistant response to history
                self.conversation_history.append({
                    "role": "assistant",
                    "content": assistant_message
                })
                
                # Keep only last 20 messages for context
                if len(self.conversation_history) > 20:
                    self.conversation_history = self.conversation_history[-20:]
                
                return assistant_message
            else:
                logger.error(f"Ollama API returned status code {response.status_code}: {response.text}")
                return "I'm having trouble connecting to the AI model. Please check if Ollama is running."
        
        except requests.exceptions.ConnectionError:
            logger.error("Connection to Ollama failed. Make sure Ollama is running.")
            return "I'm unable to connect to the AI model. Please make sure Ollama is running on your system."
        except requests.exceptions.Timeout:
            logger.error("Request to Ollama timed out")
            return "The AI model is taking too long to respond. Please try again."
        except json.JSONDecodeError:
            logger.error("Failed to decode Ollama response")
            return "I'm having trouble understanding the response. Please try again."
        except Exception as e:
            logger.error(f"Unexpected error during text generation: {e}")
            return "An unexpected error occurred while generating a response."
    
    def reset_conversation(self):
        """Clear conversation history for a fresh start."""
        self.conversation_history = []
