from agents.lwc_ai_agent import analyseLWC
import asyncio 
import sys 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(analyseLWC(prompt=prompt))
