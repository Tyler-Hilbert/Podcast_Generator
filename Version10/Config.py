##### Settings #####
config = {
    'gemini_api_key': "YOUR_GEMINI_API_KEY",
    'model_name': "gemini-2.5-pro",
    'wikipedia_mcp_url_with_key': 'https://server.smithery.ai/@Rudra-ravi/wikipedia-mcp/mcp?api_key=YOUR_SMITHERY_API_KEY',

    'episode_topic': 'YOUR_EPISODE_TOPIC',

    'initial_podcast_script_filename': 'YOUR_EPISODE_TOPIC_Script_Initial.txt',
    'log_filename': 'YOUR_EPISODE_TOPIC_log.txt'
}

from types import SimpleNamespace
config = SimpleNamespace(**config)