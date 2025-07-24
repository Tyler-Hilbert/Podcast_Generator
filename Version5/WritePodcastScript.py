# Uses Gemini to generate script for a podcast.
# Includes Wikipedia pages in the prompt.

from Config import config
from google import genai
import requests

def main():
    # Load Wikipedia data
    wikipedia_prompt_data = ''
    for page_title in config.wikipedia_pages:
        wikipedia_prompt_data += f'||Begin {page_title} page||\n'
        wikipedia_prompt_data += load_wikipedia_page(page_title)
        wikipedia_prompt_data += f'\n||End {page_title} page||\n\n'

    # Client
    client = genai.Client(api_key=config.gemini_api_key)

    # Prompt
    prompt = (
        f"You're the writer for a {config.podcast_topic} podcast."
        f"You're writing an episode on {config.episode_topic}."
        f"You'll be given several Wikipedia pages at the end of this prompt."
        f"Focus on the main points and avoid listing specific dates unless it is important to do so."
        f"The podcast is narrated by a single host."
        f"Only reply with the script."
        f"Don't include an intro or outro."
        f"Don't include 'host:' or any indication of pauses or music."
        f"\n{wikipedia_prompt_data}"
    )

    # Generate podcast script
    response = client.models.generate_content(
        model=config.model_name,
        contents=prompt
    )
    podcast_script = response.text

    # Save output to file
    with open(config.podcast_script_filename, 'w') as file:
        file.write(podcast_script)

# Returns string of page contents of page title (must be the same as the Wikipedia URL)
#   or quits if exception
def load_wikipedia_page(page_title):
    api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={page_title}&prop=extracts&explaintext=true&format=json"
    try:
        response = requests.get(api_url)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        data = response.json()

        # Navigate through the JSON structure to find the 'extract'
        # The structure is often: data -> query -> pages -> (page_id) -> extract
        page_id = next(iter(data['query']['pages'])) # Get the first (and usually only) page ID
        plain_text_content = data['query']['pages'][page_id]['extract']

        return plain_text_content

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        exit()
    except KeyError:
        print(f"Could not find 'extract' or 'pages' in the API response for '{page_title}'. The page might not exist or the API structure has changed.")
        exit()

if __name__ == '__main__':
    main()