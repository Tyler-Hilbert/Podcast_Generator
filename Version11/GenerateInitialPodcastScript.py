# Writes the initial podcast script using Gemini 2.5 & Wikipedia-MCP

from Config import config
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP
from pydantic_ai.messages import FunctionToolCallEvent, FunctionToolResultEvent
import asyncio
import os

server = MCPServerStreamableHTTP(config.wikipedia_mcp_url_with_key)
os.environ["GOOGLE_API_KEY"] = config.gemini_api_key

prompt = (
    f"Write a podcast on {config.episode_topic}. "
    f"Don't include outros or intros. "
    f"Use the tool `search_wikipedia` to get relevant pages. "
    f"Use the tool `get_article` to read in at least 3 Wikipedia pages. "
    f"Only include content that you can find from the `get_article` tool. "
    f"Only reply with the podcast script. Don't include anything like [host]: or [music fades in]. "
)

async def main():
    agent = Agent(config.gemini_model_name, toolsets=[server])

    logs = []

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
                with open(config.initial_podcast_script_filename, "w") as f:
                    f.write(run.result.output)

    # Log
    with open(config.initial_podcast_log_filename, "w") as log_file:
        log_file.write("\n".join(logs))

if __name__ == "__main__":
    asyncio.run(main())