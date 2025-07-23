# Import configuration function to securely load environment variables from .env file
from decouple import config

# Import necessary classes from the agents library
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner

# Load API key and base URL from environment variables
key = config('GEMINI_API_KEY')
base_url = config('BASE_URL')

# Initialize an asynchronous OpenAI client (or Gemini-compatible) with the credentials
gemini_client = AsyncOpenAI(api_key=key, base_url=base_url)

# Define the language model using OpenAIChatCompletionsModel
MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",         # Specify the model to use
    openai_client=gemini_client       # Pass the client to handle requests
    # max_tokens=100                  # Optionally set max_tokens here, if supported
)

# Create an agent with a name, instruction prompt, and the model
agent = Agent(
    name="nouman",                                # Agent identifier
    instructions="You are a computer teacher.",   # Instruction for the AI's behavior
    model=MODEL                                   # The AI model it will use
)

# Run the agent synchronously with an input message
res = Runner.run_sync(
    starting_agent=agent,                 # Set the starting agent
    input="Tell me about Python"          # Input message for the agent
   
)

# Output the final response from the agent
print(res.final_output)
