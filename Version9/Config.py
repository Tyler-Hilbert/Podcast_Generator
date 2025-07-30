##### Settings #####
config = {
    'gemini_api_key': 'YOUR_GEMINI_API_KEY',
    'model_name': 'gemini-2.5-flash',

    'podcast_topic': 'Computer History',
    'episode_topic': 'History of the Amazon Web Services',
    'podcast_script_filename_base': 'AWS_Podcast_Script',

    'main_wikipedia_page': 'Amazon_Web_Services',
    'support_wikipedia_pages': [
        'Amazon_(company)',
        'Web_service',
        'Cloud_computing'
    ]
}

config['podcast_initial_script_filename'] = config['podcast_script_filename_base'] + '_Initial.txt'

from types import SimpleNamespace
config = SimpleNamespace(**config)