##### Settings #####
config = {
    'gemini_api_key': 'YOUR_GEMINI_API_KEY',
    'model_name': 'gemini-2.5-flash',

    'podcast_topic': 'YOUR_PODCAST_NAME',
    'episode_topic': 'YOUR_EPISODE_TOPIC',
    'podcast_script_filename_base': 'YOUR_EPISODE_TOPIC_Podcast_Script',

    'main_wikipedia_page': 'WIKIPEDIA_PAGE_FOR_YOUR_TOPIC',
    'support_wikipedia_pages': [
        'WIKIPEDIA_PAGE_RELATED_TO_YOUR_TOPIC',
        'WIKIPEDIA_PAGE_RELATED_TO_YOUR_TOPIC',
        'WIKIPEDIA_PAGE_RELATED_TO_YOUR_TOPIC'
    ]
}

config['podcast_initial_script_filename'] = config['podcast_script_filename_base'] + '_Initial.txt'

from types import SimpleNamespace
config = SimpleNamespace(**config)