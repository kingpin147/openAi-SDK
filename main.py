# Import configuration function to securely load environment variables from .env file

# Import necessary classes from the agents library
from agents import Runner
from my_agent.teacher_agent import agent





# Run the agent synchronously with an input message
res = Runner.run_sync(
    starting_agent=agent,                 # Set the starting agent
    input="Tell me about Python"          # Input message for the agent
   
)

# Output the final response from the agent
print(res.final_output)
