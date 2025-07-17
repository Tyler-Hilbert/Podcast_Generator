# Step 2, generating the TTS script from `WritePodcastScript` to a wav file using Chatterbox.

from Config import config
import torchaudio as ta
import torch
from chatterbox.tts import ChatterboxTTS
import re

# Load podcast TTS script and chunk into sentences
with open(config.tts_script_output_filename, "r") as file:
    podcast_script_tts = file.read()

sentences = re.split(r'(?<=[.!?])\s+|\n+', podcast_script_tts.strip())

# Generate Audio
model = ChatterboxTTS.from_pretrained(device=config.chatterbox_device)
all_audio = []
for sentence in sentences: # Generate audio for each sentence
    wav = model.generate(sentence, audio_prompt_path=config.tts_reference_audio)
    all_audio.append(wav)

# Concatenate all audio tensors and save
full_audio = torch.cat(all_audio, dim=1)
ta.save(config.tts_audio_output_filename, full_audio, model.sr)
