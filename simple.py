
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

endpoint = "https://models.inference.ai.azure.com"


async def main():
    agent = Agent(
        task="Go to Reddit, search for 'browser-use', click on the first post and return the first comment.",
        llm=ChatOpenAI(base_url=endpoint, model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
