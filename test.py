import time
import asyncio
from rasa.core.agent import Agent
from rasa.utils.endpoints import EndpointConfig
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook",type="http")
agent = Agent.load("api-rasa/models/20240101-155929-vibrato-gravel.tar.gz", action_endpoint= action_endpoint)
async def main():
    # Load the Rasa agent model
    
    while 1:
        message = input("AI: ")
    # Send a message to the loaded agent and receive a response
        start = time.time()
        message = await agent.handle_text(message)

    # Print the response
        print(message)
        print("time: ", time.time()-start)
    

# Run the asynchronous main function
asyncio.run(main())
