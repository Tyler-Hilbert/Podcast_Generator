##### Settings #####
config = {

'groq_api_key': 'YOUR GROQ API KEY',

'podcast_description': 'Computer History',
'episode_description': 'Python the programming language',

'initial_script_output_filename': 'Script_Python.txt',
'tts_script_output_filename': 'Script_Python_TTS.txt',

'model_name': 'meta-llama/llama-4-maverick-17b-128e-instruct',

'tts_reference_audio': 'Prompt.wav',
'tts_audio_output_filename': 'Python_Programming_Language.wav',

'chatterbox_device': 'cpu',

'video_thumbnail': 'Python.svg',
'video_output_filename': 'Python_Programming_Language.mp4'
}
from types import SimpleNamespace
config = SimpleNamespace(**config)

##### Prompts #####
prompt_system_prompt_write_podcast = f'''
You're the writer for a podcast on {config.podcast_description}.
The podcast is narrated by a single host.
The tone should be formal.
Provide background on topics where needed.
'''

prompt_write_podcast_script = f'''
Write a script for a podcast on the {config.episode_description}.
Only reply with the podcast script.
'''

def create_tts_conversion_prompt(podcast_script):
    return f'''
You'll be given the script for a podcast on {config.episode_description}.
Rewrite the script so that it can be read by TTS.
This means writing words the way they are to be pronounced, for example, 1995 as nineteen ninety five.
Remove any text that shouldn't be read out loud, such as "Host:", "(Pause)" or "(Upbeat music)".
Only reply with the text to be input into the TTS.

=== Begin Podcast Script ===
{podcast_script}
=== End Podcast Script ===
'''