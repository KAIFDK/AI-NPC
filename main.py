"""
Main entry point for AI NPC application
"""

import sys
import logging

# Setup audio compatibility for Python 3.14+
from src import audio_compat

from src.ai_npc import AINPC

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main():
    """Main application entry point."""
    print("="*50)
    print("AI NPC - Speech Recognition & Response System")
    print("="*50)
    print()
    
    try:
        # Initialize AI NPC
        print("Initializing AI NPC system...")
        ai_npc = AINPC(language="en-US")
        
        print("System ready!\n")
        
        # Ask user how many exchanges they want
        print("How would you like to interact?")
        print("1. Single exchange (listen -> respond)")
        print("2. Multi-turn conversation (continuous)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            print("\nStarting single exchange mode...")
            ai_npc.process_speech_to_response()
        elif choice == "2":
            print("\nStarting conversation mode...")
            ai_npc.start_conversation()
        elif choice == "3":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Starting conversation mode...")
            ai_npc.start_conversation()
    
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
        sys.exit(0)
    except Exception as e:
        logging.error(f"Fatal error: {e}", exc_info=True)
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
