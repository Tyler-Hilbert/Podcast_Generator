# Podcast Generator (Version 11)
Uses Gemini 2.5 and 3 relevant wikipedia pages to generate a podcast. The Wikipedia pages are read in using Wikipedia MCP.  
Then uses GPT-5-mini to edit any mistakes (also using 3 pages from wikipedia-mcp).  
Then GPT-5 converts the transcript to its phonetic pronunciation.  
Then generates audio using Chatterbox and video using MoviePy.  
## Usage
(Note all steps need to be run within the `Version11` dir)
### Step 0 -- Config
Add your Gemini API key to the variable `gemini_api_key` in `Config.py`.  
Update `wikipedia_mcp_url_with_key` in `Config.py` to include your API Key (you need to create a Smithery.ai account and click "Get URL with keys instead").  
Add your OpenAI API key to the variable `openai_api_key` in `Config.py`.  
### Step 1 -- Generate Podcast Script
`$python GenerateInitialPodcast.py`
### Step 2 -- Revise Podcast Script
`$python RevisePodcastScript.py`
### Step 3 -- Convert Transcript to Phonetic Pronunciation
`$python ConvertPodcastScriptToPhoneticPronunciation.py`
### Step 4 -- Generate Audio
`$python GenerateAudio.py`
### Step 5 -- Generate Video (optional)
`$python GenerateVideo.py`