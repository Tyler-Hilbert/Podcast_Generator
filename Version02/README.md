# Podcast Generator (Version 2)
Utilizes Llama 4 (with Groq API) to generate a podcast script.  
One agent generates an outline while a second agent generates each section from the outline.  
## Usage
(Note all steps need to be run within the `Version02` dir)
### Step 0 -- Config
Add your GROQ API key to the variable `groq_api_key` in `Config.py`
### Step 1 -- Generate podcast script
`$python WritePodcastScript.py`
## Results
The multi-agent script generation produces longer and more in-depth scripts. The sections don't always follow a linear chronological order and sometimes bounce around.  