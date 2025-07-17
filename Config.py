from groq import Groq

##### Settings #####
config = {

'groq_api_key': 'YOUR GROC API KEY',

'podcast_description': 'Computer History',
'episode_description': 'The history of Google',

'initial_script_output_filename': 'Script_Google.txt',
'tts_script_output_filename': 'Script_Google_TTS.txt',

'model_name': 'meta-llama/llama-4-maverick-17b-128e-instruct',

'tts_reference_audio': 'Prompt.wav',
'tts_audio_output_filename': 'Google_History.wav',

'chatterbox_device': 'cpu'
}
from types import SimpleNamespace
config = SimpleNamespace(**config)

##### Prompts #####
prompt_write_podcast_script = f'''
You're the writer for a podcast on {config.podcast_description}.
Write a script for a podcast on the {config.episode_description}.
The podcast is narrated by a single host.
The tone should be formal.
Provide background on topics where needed.
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

##### Groq Client #####
client = Groq(
    api_key=config.groq_api_key,
)