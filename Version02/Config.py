##### Settings #####
config = {
    'groq_api_key': 'YOUR_GROQ_API_KEY',
    'model_name': 'meta-llama/llama-4-maverick-17b-128e-instruct',

    'podcast_topic': 'History of IBM',
    'podcast_outline_filename': 'IBM_Outline.txt',
    'podcast_script_filename': 'IBM_Podcast_Script.txt'
}

from types import SimpleNamespace
config = SimpleNamespace(**config)