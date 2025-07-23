from agents import Agent
from my_config.gemini_config import MODEL

# Create an agent with a name, instruction prompt, and the model


agent = Agent(
    name="nouman",                                # Agent identifier
    instructions="You are a computer teacher.",   # Instruction for the AI's behavior
    model=MODEL                                   # The AI model it will use
)