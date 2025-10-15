# Podcast Generator (Version 9)
Uses Gemini 2.5 with a main Wikipedia page to generate an initial podcast script. It then iterates over the support Wikipedia page, revising the script one page at a time.
## Usage
(Note all steps need to be run within the `Version09` dir)
### Config
Add your Gemini API key to the variable `gemini_api_key` in `Config.py`
### Generate podcast script
`$python WritePodcastScript.py`