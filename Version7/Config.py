##### Settings #####
config = {
    'gemini_api_key': 'YOUR_GEMINI_API_KEY',
    'model_name': 'gemini-2.5-flash',

    'podcast_topic': 'Computer History',
    'episode_topic': 'History of the Amazon Web Services',
    'podcast_script_filename': 'AWS_Podcast_Script.txt',
    'revised_podcast_script_filename': 'AWS_Podcast_Script_Revised.txt',

    'wikipedia_pages': [
        'Amazon_Web_Services',
        'Amazon_(company)',
        'Web_service',
        'Cloud_computing'
    ]
}

from types import SimpleNamespace
config = SimpleNamespace(**config)