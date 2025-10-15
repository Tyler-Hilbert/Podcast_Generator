# Podcast Generator
This is an podcast generator inspired by the idea of creating "Cosmos, but for computers instead of space".  

The latest — [Version 11](https://github.com/Tyler-Hilbert/Podcast_Generator/tree/main/Version11) — generates an educational podcasts by:  
1) Writing a script with Gemini-2.5 + Wikipedia MCP  
2) Fact-checking with GPT-5-mini + Wikipedia MCP  
3) Converting to phonetic text for natural narration with GPT-5  
4) Producing audio (Chatterbox) and optional video (MoviePy)  

## Version 11
[Version 11](https://github.com/Tyler-Hilbert/Podcast_Generator/tree/main/Version11) uses Gemini 2.5 and 3 relevant wikipedia pages to generate a podcast. The Wikipedia pages are read in using Wikipedia MCP.  
Then uses GPT-5-mini to edit any mistakes (also using 3 pages from wikipedia-mcp).  
Then GPT-5 converts the transcript to its phonetic pronunciation.  
Then generates audio using Chatterbox and video using MoviePy.  
### Technologies
* gemini-2.5-pro
* Wikipedia MCP
* GPT-5-mini
* GPT-5
* Chatterbox
* MoviePy

## Version 10
[Version 10](https://github.com/Tyler-Hilbert/Podcast_Generator/tree/main/Version10) uses Gemini 2.5 and 3 relevant wikipedia pages to generate a podcast. The Wikipedia pages are read in using wikipedia-mcp.
### Technologies
* gemini-2.5-pro
* Wikipedia MCP

## Version 9
[Version 9](https://github.com/Tyler-Hilbert/Podcast_Generator/tree/main/Version09) uses Gemini 2.5 with a main Wikipedia page to generate an initial podcast script.  
It then iterates over the support Wikipedia page, revising the script one page at a time.
### Technologies
* gemini-2.5-flash
* Wikipedia

## Version 8
[Version 8](https://github.com/Tyler-Hilbert/Podcast_Generator/tree/main/Version08) uses Gemini 2.5 to generate an initial podcast script.  
It then iterates over each Wikipedia page, revising the script one page at a time.
### Technologies
* gemini-2.5-flash
* Wikipedia

## Version 7
[Version 7](https://github.com/Tyler-Hilbert/Podcast_Generator/tree/main/Version07) uses Gemini 2.5 and includes the contents of relevant Wikipedia Pages to revise an existing script.
### Technologies
* gemini-2.5-flash
* Wikipedia

## Version 6
Version 6 is not available.

## Version 5
[Version 5](https://github.com/Tyler-Hilbert/Podcast_Generator/tree/main/Version05) uses Gemini 2.5 and includes the contents of relevant Wikipedia Pages in the prompt.
### Technologies
* gemini-2.5-flash
* Wikipedia

## Version 4
Version 4 is not available.

## Version 3
[Version 3](https://github.com/Tyler-Hilbert/Podcast_Generator/tree/main/Version03) uses Gemini 2.5 to generate a podcast script.
### Technologies
* gemini-2.5-flash

## Version 2
[Version 2](https://github.com/Tyler-Hilbert/Podcast_Generator/tree/main/Version02) uses two Llama 4 agents to generate the script. One agent generates the outline and the second agent (which multiple times) generates the text for each section.
### Technologies
* llama-4-maverick-17b-128e-instruct
* Groq

## Version 1
[Version 1](https://github.com/Tyler-Hilbert/Podcast_Generator/tree/main/Version01) generates the script using Llama 4, audio using `Chatterbox`, and optionally a video from an SVG.
### Technologies
* llama-4-maverick-17b-128e-instruct
* Groq
* Chatterbox
* MoviePy