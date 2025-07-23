from decouple import config

from agents import AsyncOpenAI, OpenAIChatCompletionsModel


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