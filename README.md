# Podcast Generator
Utilizes Llama 4 (with Groq API) and Chatterbox to generate a podcast.  
An example is [here](https://www.youtube.com/watch?v=-oJIJmt62U4).  
# Usage
## Step 0 -- Configure  
1) Setup a Groq account and generate an API key
2) Update the values in `Config.py`
3) Install python libraries such as `torch`, `torchaudio`, `Chatterbox`, `groq`, `PIL` and `cairosvg`
## Step 1 -- Write Script
`$python WritePodcastScript.py`  
(you will need to uncomment the TTS section if you plan on generating audio).  
## Step 2 -- Generate Audio (optional)
`$python GenerateAudio.py`
## Step 3 -- Generate Video (optional)
`$python GenerateVideo.py`