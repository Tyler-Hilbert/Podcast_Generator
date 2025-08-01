# Uses Gemini to generate script for a podcast

from Config import config
from google import genai

# Client
client = genai.Client(api_key=config.gemini_api_key)

# Prompt
prompt = (
    f"You're the writer for a {config.podcast_topic} podcast."
    f"You're writing an episode on {config.episode_topic}."
    f"The podcast is narrated by a single host."
    f"Only reply with the script."
    f"Don't include an intro or outro."
    f"Don't include 'host:' or any indication of pauses or music."
)

# Generate podcast script
response = client.models.generate_content(
    model=config.model_name,
    contents=prompt
)
podcast_script = response.text

# Save output to file
with open(config.podcast_script_filename, 'w') as file:
    file.write(podcast_script)

