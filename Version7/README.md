# Podcast Generator (Version 7)
Utilizes Gemini 2.5-Flash to revise a podcast script.  
Includes the contents of the Wikipedia pages listed at `Config.py` `config.wikipedia_pages' in the prompt.   
## Usage
(Note all steps need to be run within the `Version7` dir)
### Step 0 -- Config
Add your Gemini API key to the variable `gemini_api_key` in `Config.py`.  
Verify the location of `config.podcast_script_filename` in `Config.py`.  
### Step 1 -- Revise podcast script
`$python RevisePodcastScript.py`