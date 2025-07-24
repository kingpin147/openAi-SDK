from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_config.groq_config import GROQ_MODEL


# Create an agent with a name, instruction prompt, and the model


gemini_agent = Agent(
    name="nouman",                                # Agent identifier
    instructions="You are a computer teacher.",   # Instruction for the AI's behavior
    model=GEMINI_MODEL                                   # The AI model it will use
)

groq_agent = Agent(
    name="Attique",                                # Agent identifier
    instructions="You are a computer teacher.",   # Instruction for the AI's behavior
    model=GROQ_MODEL                                   # The AI model it will use
)