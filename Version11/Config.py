##### Settings #####
config = {
    'gemini_api_key': 'YOUR_GEMINI_API_KEY',
    'gemini_model_name': 'gemini-2.5-pro',
    'wikipedia_mcp_url_with_key': 'https://server.smithery.ai/@Rudra-ravi/wikipedia-mcp/mcp?api_key=YOUR_SMITHERY_API_KEY',
    'openai_api_key': 'YOUR_OPENAI_API_KEY',
    'openai_model_name': 'gpt-5-mini',

    'episode_topic': 'the history of the Amazon Web Services',

    'initial_podcast_script_filename': 'AWS_Script_Initial.txt',
    'initial_podcast_log_filename': 'AWS_log.txt',

    'revised_podcast_script_filename': 'AWS_Script_Revised.txt',
    'revised_podcast_log_filename': 'AWS_revision_log.txt',

    'tts_podcast_script_filename': 'AWS_Script_TTS.txt',

    'tts_reference_audio': 'Prompt.wav',
    'tts_audio_output_filename': 'AWS_History.wav',

    'chatterbox_device': 'cpu',

    'video_thumbnail_svg': 'Amazon_Web_Services_Logo.svg',
    'background_music_mp3': 'Mesmerizing Galaxy Loop.mp3',
    'video_output_path': 'AWS_History.mp4'
}

from types import SimpleNamespace
config = SimpleNamespace(**config)