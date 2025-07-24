# Import necessary classes from the agents library
from agents import Runner, set_tracing_disabled,RunConfig,set_default_openai_client,set_default_openai_api 
from my_agent.teacher_agent import gemini_agent, groq_agent 
from my_config import GEMINI_MODEL, gemini_client


set_default_openai_api("chat_completions")
set_default_openai_client(gemini_client)
set_tracing_disabled(True)


# Run the agent synchronously with an input message
res = Runner.run_sync(starting_agent=groq_agent, input="Tell me about Python", 
                      run_config=RunConfig(model=GEMINI_MODEL,
                                           model_provider=gemini_client)                                        )



# Output the final response from the agent
print(res.final_output)
