# Podcast Generator (Version 1)
Utilizes Llama 4 (with Groq API) and Chatterbox to generate a podcast with option to generate a still image video.  
# Usage
(Note all steps need to be run within the `Version01` dir)
## Configure  
1) Setup a Groq account and generate an API key
2) Update the values in `Config.py`
3) Install python libraries such as `torch`, `torchaudio`, `Chatterbox`, `groq`, `PIL` and `cairosvg`
## Write Script
`$python WritePodcastScript.py`
## Generate Audio
`$python GenerateAudio.py`
## Generate Video (optional)
`$python GenerateVideo.py`