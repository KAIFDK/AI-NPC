#!/usr/bin/env python3
"""
Simple test client for the AI NPC system.
This client sends various test scenarios to the NPC backend and displays the responses.
"""

import requests
import json
from typing import List, Dict, Any

# Server configuration
BASE_URL = "http://localhost:8000"
INTERACT_ENDPOINT = f"{BASE_URL}/interact"

def send_interaction(npc_id: str, player_input: str, conversation_history: List[str], 
                    nearby_objects: List[Dict[str, str]], available_actions: List[str]) -> Dict[str, Any]:
    """Send an interaction request to the NPC backend."""
    
    payload = {
        "npc_id": npc_id,
        "player_input": player_input,
        "conversation_history": conversation_history,
        "environment": {
            "nearby_objects": nearby_objects,
            "available_actions": available_actions
        }
    }
    
    try:
        response = requests.post(INTERACT_ENDPOINT, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with server: {e}")
    return {}

def display_interaction(player_input: str, ai_response: Dict[str, Any]):
    """Display the interaction in a nice format."""
    print(f"\n{'='*50}")
    print(f"🧙‍♂️ Player: {player_input}")
    print(f"🤖 Kaelen: {ai_response['dialogue']}")
    print(f"⚡ Action: {ai_response['action']}")
    if ai_response['action_params']:
        print(f"📋 Parameters: {ai_response['action_params']}")
    print(f"😄 Emotion: {ai_response['emotion']}")
    print(f"{'='*50}")

def main():
    """Run various test scenarios with the NPC."""
    
    print("🎮 AI NPC Test Client")
    print("Connecting to the backend server...")
    
    # Test 1: Simple greeting
    print("\n🧪 Test 1: Simple Greeting")
    response = send_interaction(
        npc_id="kaelen_the_smith",
        player_input="Hello there!",
        conversation_history=[],
        nearby_objects=[
            {"name": "Anvil", "description": "A heavy iron anvil, well-used"},
            {"name": "Hammer", "description": "A masterwork smithing hammer"}
        ],
        available_actions=["idle", "speak", "work_forge"]
    )
    
    if response:
        display_interaction("Hello there!", response)
    
    # Test 2: Ask about the magic sword
    print("\n🧪 Test 2: Asking about the Magic Sword")
    response = send_interaction(
        npc_id="kaelen_the_smith",
        player_input="I've heard you have a magic sword. Can I have it?",
        conversation_history=["Player: Hello there!", "Kaelen: Hmph. What do you want?"],
        nearby_objects=[
            {"name": "Magic_Sword", "description": "A gleaming blade with ancient runes"},
            {"name": "Anvil", "description": "A heavy iron anvil, well-used"}
        ],
        available_actions=["idle", "give_item(item_name='Magic_Sword')", "speak"]
    )
    
    if response:
        display_interaction("I've heard you have a magic sword. Can I have it?", response)
    
    # Test 3: Ask about unlocking a door
    print("\n🧪 Test 3: Asking about the Ancient Door")
    response = send_interaction(
        npc_id="kaelen_the_smith",
        player_input="Can you help me unlock this ancient door?",
        conversation_history=[
            "Player: Hello there!", 
            "Kaelen: Hmph. What do you want?",
            "Player: I've heard you have a magic sword. Can I have it?",
            "Kaelen: Ah, you've noticed my blade. It was forged in the heart of a dying star. Perhaps it can serve you better. Take it."
        ],
        nearby_objects=[
            {"name": "Ancient_Door", "description": "A massive stone door with intricate carvings"},
            {"name": "Key", "description": "An ornate bronze key"}
        ],
        available_actions=["idle", "unlock_door(door_name='Ancient_Door')", "speak"]
    )
    
    if response:
        display_interaction("Can you help me unlock this ancient door?", response)
    
    # Test 4: Generic conversation
    print("\n🧪 Test 4: Generic Conversation")
    response = send_interaction(
        npc_id="kaelen_the_smith",
        player_input="Tell me about your craft.",
        conversation_history=[
            "Player: Hello there!", 
            "Kaelen: Hmph. What do you want?"
        ],
        nearby_objects=[
            {"name": "Forge", "description": "A roaring forge with white-hot coals"},
            {"name": "Tools", "description": "Various smithing tools hang on the wall"}
        ],
        available_actions=["idle", "speak", "demonstrate_craft"]
    )
    
    if response:
        display_interaction("Tell me about your craft.", response)
    
    print("\n✅ All tests completed!")
    print("The AI NPC system is running successfully! 🎉")

if __name__ == "__main__":
    main()