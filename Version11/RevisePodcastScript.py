# Utilizes GPT-5-mini and Wikipedia-MCP to fact check the initial podcast script written by Gemini.

from Config import config
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP
from pydantic_ai.messages import FunctionToolCallEvent, FunctionToolResultEvent
import asyncio
import os

server = MCPServerStreamableHTTP(config.wikipedia_mcp_url_with_key)
os.environ["OPENAI_API_KEY"] = config.openai_api_key

with open(config.initial_podcast_script_filename, 'r') as file:
    initial_podcast_script = file.read()

prompt = (
    f"You're the editor for a podcast on {config.episode_topic}. "
    f"It's your job to use Wikipedia to correct any mistakes in the script. "
    f"Use the tool `search_wikipedia` to get relevant pages. "
    f"Use the tool `get_article` to read in at least 3 Wikipedia pages. "
    f"Only include content that you can find from the `get_article` tool. "
    f"Don't include outros or intros. "
    f"Only reply with the revised podcast script. Don't include anything like [host]: or [music fades in]. "
    f"The podcast script that you need to revise is listed below: \n"
    f"{initial_podcast_script}"
)

logs = []
logs.append(f"[PROMPT]:\n{prompt}\n")

async def main():
    agent = Agent(
        name='Podcast Script Editor',
        model=config.openai_model_name,
        mcp_servers=[server]
    )

    async with agent.iter(prompt) as run:
        async for node in run:
            if Agent.is_call_tools_node(node):
                # Use tool
                async with node.stream(run.ctx) as s:
                    async for ev in s:
                        if isinstance(ev, FunctionToolCallEvent):
                            log_string = f"[MCP] Tool CALL: {ev.part.tool_name} args={ev.part.args}"
                            logs.append(log_string)
                        elif isinstance(ev, FunctionToolResultEvent):
                           log_string = f"[MCP] Tool RESULT: {ev.tool_call_id} -> {ev.result.content}"
                           logs.append(log_string)
            elif Agent.is_end_node(node):
                # Save script to file
                with open(config.revised_podcast_script_filename, "w") as f:
                    f.write(run.result.output)

    # Log
    with open(config.revised_podcast_log_filename, "w") as log_file:
        log_file.write("\n".join(logs))

if __name__ == "__main__":
    asyncio.run(main())