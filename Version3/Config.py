##### Settings #####
config = {
    'gemini_api_key': 'YOUR_GEMINI_API_KEY',
    'model_name': 'gemini-2.5-flash',

    'podcast_topic': 'Computer History',
    'episode_topic': 'History of the company IBM',
    'podcast_script_filename': 'IBM_Podcast_Script.txt'
}

from types import SimpleNamespace
config = SimpleNamespace(**config)