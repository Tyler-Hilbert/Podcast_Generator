# Podcast Generator
Generates a podcast on a topic
## Version 1
Version 1 generates the script using Llama 4, audio using Chatterbox, and optionally a video from an SVG.
### Tools
* llama-4-maverick-17b-128e-instruct
* Groq
* Chatterbox
* MoviePy

## Version 2
Version 2 uses two Llama 4 agents to generate the script. One agent generates the outline and the second agent (which multiple times) generates the text for each section.
### Tools
* llama-4-maverick-17b-128e-instruct
* Groq

## Version 3
Version 3 uses Gemini 2.5 to generate a podcast script.
### Tools
* gemini-2.5-flash