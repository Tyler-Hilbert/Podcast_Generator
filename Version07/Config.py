##### Settings #####
config = {
    'gemini_api_key': 'YOUR_GEMINI_API_KEY',
    'model_name': 'gemini-2.5-flash',

    'podcast_topic': 'YOUR_PODCAST_NAME',
    'episode_topic': 'YOUR_EPISODE_TOPIC',
    'podcast_script_filename': 'YOUR_EPISODE_TOPIC_Podcast_Script.txt',
    'revised_podcast_script_filename': 'YOUR_EPISODE_TOPIC_Podcast_Script_Revised.txt',

    'wikipedia_pages': [
        'WIKIPEDIA_PAGE_RELATED_TO_YOUR_TOPIC',
        'WIKIPEDIA_PAGE_RELATED_TO_YOUR_TOPIC',
        'WIKIPEDIA_PAGE_RELATED_TO_YOUR_TOPIC',
        'WIKIPEDIA_PAGE_RELATED_TO_YOUR_TOPIC'
    ]
}

from types import SimpleNamespace
config = SimpleNamespace(**config)