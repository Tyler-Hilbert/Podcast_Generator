# Podcast Generator (Version 8)
Uses Gemini 2.5 to generate an initial podcast script. It then iterates over each Wikipedia page, revising the script one page at a time.
## Usage
(Note all steps need to be run within the `Version08` dir)
### Config
Add your Gemini API key to the variable `gemini_api_key` in `Config.py`
### Generate podcast script
`$python WritePodcastScript.py`