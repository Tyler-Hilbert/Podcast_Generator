# Converts the revised script to phonetic pronunciation for TTS.

from Config import config
from pydantic_ai import Agent
import asyncio
import os

os.environ["OPENAI_API_KEY"] = config.openai_api_key
agent = Agent('openai:gpt-5')

with open(config.revised_podcast_script_filename, 'r') as file:
    revised_podcast_script = file.read()

prompt = (
    f"You'll be given the script for a podcast on {config.episode_topic}. "
    f"Rewrite the script so that it can be read by TTS. "
    f"This means writing words the way they are to be pronounced, for example, 1995 as nineteen ninety five. "
    'Remove any text that should not be read out loud, such as "Host:", "(Pause)" or "(Upbeat music)". '
    f"Only reply with the text to be input into the TTS. \n"
    f"=== Begin Podcast Script ===\n"
    f"{revised_podcast_script}\n"
    f"=== End Podcast Script ===\n"
)

async def main():
    async with agent:  
        result = await agent.run(prompt)
        with open(config.tts_podcast_script_filename, "w") as f:
            f.write(result.output)

if __name__ == "__main__":
    asyncio.run(main())