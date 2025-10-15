##### Settings #####
config = {
    'gemini_api_key': 'YOUR_GEMINI_API_KEY',
    'gemini_model_name': 'gemini-2.5-pro',
    'wikipedia_mcp_url_with_key': 'https://server.smithery.ai/@Rudra-ravi/wikipedia-mcp/mcp?api_key=YOUR_SMITHERY_API_KEY',
    'openai_api_key': 'YOUR_OPENAI_API_KEY',
    'openai_model_name': 'gpt-5-mini',

    'episode_topic': 'YOUR_EPISODE_TOPIC',

    'initial_podcast_script_filename': 'YOUR_EPISODE_TOPIC_Script_Initial.txt',
    'initial_podcast_log_filename': 'YOUR_EPISODE_TOPIC_log.txt',

    'revised_podcast_script_filename': 'YOUR_EPISODE_TOPIC_Script_Revised.txt',
    'revised_podcast_log_filename': 'YOUR_EPISODE_TOPIC_revision_log.txt',

    'tts_podcast_script_filename': 'YOUR_EPISODE_TOPIC_Script_TTS.txt',

    'tts_reference_audio': 'YOUR_PROMPT.wav',
    'tts_audio_output_filename': 'YOUR_EPISODE_TOPIC_History.wav',

    'chatterbox_device': 'cpu',

    'video_thumbnail_svg': 'YOUR_EPISODE_TOPIC_Logo.svg',
    'background_music_mp3': 'YOUR_BACKGROUND_MUSIC.mp3',
    'video_output_path': 'YOUR_EPISODE_TOPIC_History.mp4'
}

from types import SimpleNamespace
config = SimpleNamespace(**config)