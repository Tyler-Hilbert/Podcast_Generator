# Writes the script for a podcast using the settings in `Config.py`

from Config import config, client, prompt_write_podcast_script, create_tts_conversion_prompt

# Generate podcast script
chat_completion_podcast_script = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt_write_podcast_script,
        }
    ],
    model=config.model_name,
    stream=False,
)
podcast_script = chat_completion_podcast_script.choices[0].message.content

# Save podcast script to file (for debugging and reference)
with open(config.initial_script_output_filename, 'w') as f:
    f.write(podcast_script)

# Process text for TTS
chat_completion_podcast_tts = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": create_tts_conversion_prompt(podcast_script),
        }
    ],
    model=config.model_name,
    stream=False,
)
podcast_script_tts = chat_completion_podcast_tts.choices[0].message.content

# Save Podcast TTS to file
with open(config.tts_script_output_filename, 'w') as f:
    f.write(podcast_script_tts)