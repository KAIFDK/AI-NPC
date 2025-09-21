import uvicorn
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any

# --- Pydantic Models: Enforcing the API Contract ---
# These models define the exact structure of the data sent between the client and server.
# FastAPI uses these for automatic validation.

class EnvironmentContext(BaseModel):
    """Describes the NPC's immediate surroundings."""
    nearby_objects: List = Field(description="List of objects near the NPC, each with a name and description.")
    available_actions: List[str] = Field(description="List of function signatures for actions the NPC can currently perform.")

class WorldContext(BaseModel):
    """The complete package of information sent from the game client to the AI backend."""
    npc_id: str
    player_input: str
    conversation_history: List[str]
    environment: EnvironmentContext

class AIResponse(BaseModel):
    """The structured response sent from the AI backend to the game client."""
    dialogue: str
    action: str
    action_params: Dict[str, Any]
    emotion: str

# --- NPC Profile: The "Soul" of the Character ---
class NPCProfile:
    """Holds the static, authored data for an NPC's personality."""
    def __init__(self, name: str, backstory: str, personality_traits: List[str], core_knowledge: str, dialogue_style: str):
        self.name = name
        self.backstory = backstory
        self.personality_traits = ", ".join(personality_traits)
        self.core_knowledge = core_knowledge
        self.dialogue_style = dialogue_style

# --- Mock LLM Function ---
# In a real application, this would make an API call to a service like OpenAI, Anthropic, or a local model.
# For this educational example, we simulate the LLM's behavior to make the code runnable without an API key.
def mock_llm_call(prompt: str) -> str:
    """
    Simulates a call to a Large Language Model.
    It inspects the prompt for keywords to return a predictable, structured response.
    This allows us to test the end-to-end flow of the system.
    """
    print("\n--- MOCK LLM PROMPT ---")
    print(prompt)
    print("-----------------------\n")

    # Simple rule-based logic to simulate intelligent responses
    if "sword" in prompt.lower() and "give_item(item_name='Magic_Sword')" in prompt:
        return json.dumps({
            "dialogue": "Ah, you've noticed my blade. It was forged in the heart of a dying star. Perhaps it can serve you better. Take it.",
            "action": "give_item",
            "action_params": {"item_name": "Magic_Sword"},
            "emotion": "proud"
        })
    elif "door" in prompt.lower() and "unlock_door(door_name='Ancient_Door')" in prompt:
        return json.dumps({
            "dialogue": "This old door? It's been sealed for ages. Stand back, I have the key.",
            "action": "unlock_door",
            "action_params": {"door_name": "Ancient_Door"},
            "emotion": "determined"
        })
    elif "hello" in prompt.lower() or "hi" in prompt.lower():
         return json.dumps({
            "dialogue": "Hmph. What do you want?",
            "action": "idle",
            "action_params": {},
            "emotion": "grumpy"
        })
    else:
        return json.dumps({
            "dialogue": "I've got work to do. Stop bothering me.",
            "action": "idle",
            "action_params": {},
            "emotion": "annoyed"
        })

# --- Backend Application Setup ---
app = FastAPI()

# Load NPC profiles into memory on startup
NPC_DATABASE = {
    "kaelen_the_smith": NPCProfile(
        name="Kaelen",
        backstory="Kaelen is a master blacksmith, the last of a long line of artisans who once served the mountain kings. He is old, weary, and deeply saddened by the decline of his craft. He secretly possesses the key to the ancient city archives.",
        personality_traits=["grumpy", "proud", "secretly kind-hearted", "distrustful of strangers"],
        core_knowledge="Knows the location of the legendary Magic Sword and the history of the Ancient Door.",
        dialogue_style="Speaks in short, gruff sentences. Rarely uses more than two sentences at a time."
    )
}

def construct_system_prompt(profile: NPCProfile, context: WorldContext) -> str:
    """Dynamically assembles the master prompt for the LLM."""
    
    # 1. Persona Definition
    prompt = f"You are {profile.name}. Your personality is: {profile.personality_traits}. Your backstory: {profile.backstory}. Your dialogue style: {profile.dialogue_style}\n\n"
    
    # 2. Core Knowledge
    prompt += f"Relevant world knowledge you possess: {profile.core_knowledge}\n\n"

    # 3. Conversation History
    prompt += "### CONVERSATION HISTORY:\n"
    for line in context.conversation_history:
        prompt += f"- {line}\n"
    prompt += f"- Player: \"{context.player_input}\"\n\n"

    # 4. Dynamic World Context & Action Constraints
    prompt += "### CURRENT SITUATION:\n"
    prompt += f"Nearby objects of interest: {json.dumps(context.environment.nearby_objects)}\n"
    prompt += f"Based on the situation and conversation, you can perform ONLY ONE of the following actions: {json.dumps(context.environment.available_actions)}\n\n"

    # 5. Output Formatting Instructions
    prompt += "### YOUR TASK:\n"
    prompt += "Respond as the character. Your entire response MUST be a single, valid JSON object with no other text or explanation. The JSON object must contain 'dialogue' (what you say), 'action' (the chosen action from the available list), 'action_params' (a dictionary of parameters for the action), and 'emotion' (a single word describing your current emotion)."
    
    return prompt

def parse_llm_response(response_str: str) -> AIResponse:
    """
    Parses and validates the LLM's string output.
    This is a critical step for system stability.
    """
    try:
        response_data = json.loads(response_str)
        # Use Pydantic to validate the structure and types
        validated_response = AIResponse(**response_data)
        return validated_response
    except (json.JSONDecodeError, TypeError, ValueError) as e:
        print(f"Error parsing LLM response: {e}")
        print(f"Raw response was: {response_str}")
        # Fallback to a safe, default state if parsing fails
        return AIResponse(
            dialogue="I... don't know what to say.",
            action="idle",
            action_params={},
            emotion="confused"
        )

@app.post("/interact", response_model=AIResponse)
async def interact_with_npc(context: WorldContext):
    """The main API endpoint for all player-NPC interactions."""
    npc_profile = NPC_DATABASE.get(context.npc_id)
    if not npc_profile:
        raise HTTPException(status_code=404, detail="NPC not found")

    # Step 1: Construct the detailed prompt
    prompt = construct_system_prompt(npc_profile, context)
    
    # Step 2: Call the LLM (or our mock function)
    llm_output_str = mock_llm_call(prompt)
    
    # Step 3: Parse and validate the response
    ai_response = parse_llm_response(llm_output_str)
    
    return ai_response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)