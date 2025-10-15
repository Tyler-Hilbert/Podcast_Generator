# Podcast Generator (Version 10)
Uses Gemini 2.5 and 3 relevant wikipedia pages to generate a podcast. The Wikipedia pages are read in using Wikipedia MCP.
## Usage
(Note all steps need to be run within the `Version10` dir)
### Config
Add your Gemini API key to the variable `gemini_api_key` in `Config.py`.  
Update `wikipedia_mcp_url_with_key` in `Config.py` to include your API Key (you need to create a Smithery.ai account and click "Get URL with keys instead").  
### Generate podcast script
`$python GenerateInitialPodcast.py`