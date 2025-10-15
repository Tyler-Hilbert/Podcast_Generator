##### Settings #####
config = {
    'groq_api_key': 'YOUR_GROQ_API_KEY',
    'model_name': 'meta-llama/llama-4-maverick-17b-128e-instruct',

    'podcast_topic': 'YOUR_EPISODE_TOPIC',
    'podcast_outline_filename': 'YOUR_EPISODE_TOPIC_Outline.txt',
    'podcast_script_filename': 'YOUR_EPISODE_TOPIC_Podcast_Script.txt'
}

from types import SimpleNamespace
config = SimpleNamespace(**config)