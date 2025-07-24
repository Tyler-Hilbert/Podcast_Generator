# Podcast Generator (Version 5)
Utilizes Gemini 2.5-Flash to generate a podcast script.  
Includes the contents of the Wikipedia pages listed at `Config.py` `config.wikipedia_pages' in the prompt.   
## Usage
(Note all steps need to be run within the `Version5` dir)
### Step 0 -- Config
Add your Gemini API key to the variable `gemini_api_key` in `Config.py`
### Step 1 -- Generate podcast script
`$python WritePodcastScript.py`