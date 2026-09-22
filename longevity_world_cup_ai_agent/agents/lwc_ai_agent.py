from pydantic_ai import Agent 
from dotenv import load_dotenv 
from tools.lwc_tools import getLongeivityWorldCup, getLongeivityWorldCupPersons, getImageBaseURL, writeHTML
from prompts.lwc_prompt import SYSTEM_PROMPT

load_dotenv()

agent = Agent(
    tools = [getLongeivityWorldCup, getLongeivityWorldCupPersons, getImageBaseURL, writeHTML],
    system_prompt = SYSTEM_PROMPT,
    model = 'openai:gpt-5.2'
)

async def analyseLWC(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')