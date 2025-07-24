from decouple import config

from agents import AsyncOpenAI, OpenAIChatCompletionsModel


# Load API key and base URL from environment variables

key = config('GROQ_API_KEY')
base_url = config('BASE_URL_GROQ')

# Initialize an asynchronous OpenAI client (or Gemini-compatible) with the credentials
groq_client = AsyncOpenAI(api_key=key, base_url=base_url)

# Define the language model using OpenAIChatCompletionsModel
GROQ_MODEL = OpenAIChatCompletionsModel(
    model="llama-3.3-70b-versatile",         # Specify the model to use
    openai_client=groq_client       # Pass the client to handle requests
    # max_tokens=100                  # Optionally set max_tokens here, if supported
)