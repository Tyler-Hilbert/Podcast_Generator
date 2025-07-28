# Uses Gemini to generate script for a podcast.
# Loops over included resources to revise the script.

from Config import config
from google import genai
import requests

def main():
    # Client
    client = genai.Client(api_key=config.gemini_api_key)

    # Generate initial podcast script
    generate_initial_script(client)

    # Refine podcast script
    for revision_num, wikipedia_page_title in enumerate(config.wikipedia_pages):
        revise_podcast_script(revision_num, client, wikipedia_page_title)

# Generates the initial podcast script and saves it to config.podcast_initial_script_filename
def generate_initial_script(client):
    # Prompt for initial script generation
    prompt = (
        f"You're the writer for a {config.podcast_topic} podcast. "
        f"You're writing an episode on {config.episode_topic}. "
        f"The podcast is narrated by a single host. "
        f"Only reply with the script. "
        f"Don't include an intro or outro. "
        f"Don't include 'host:' or any indication of pauses or music. "
    )

    # Generate podcast script
    response = client.models.generate_content(
        model=config.model_name,
       contents=prompt
    )
    podcast_script = response.text

    # Save initial script
    with open(config.podcast_initial_script_filename, 'w') as file:
        file.write(podcast_script)

# Reads the previous script from a file,
#   revises the previous script using Wikipedia,
#   saves the revised script to a file.
def revise_podcast_script(revision_num, client, wikipedia_page_title):
    if revision_num == 0: # This is the first revision
        read_filename = config.podcast_initial_script_filename
    else: # This is not the first revision
        read_filename = config.podcast_script_filename_base + '_Revision' + str(revision_num) + '.txt'
    write_filename = config.podcast_script_filename_base + '_Revision' + str(revision_num+1) + '.txt'
    
    # Load current podcast script
    podcast_script_prompt_data = load_podcast_script(read_filename)
    
    # Load Wikipedia Data
    wikipedia_prompt_data = load_wikipedia_page(wikipedia_page_title)

    # Revision Prompt
    prompt = (
        f"You're an editor for a {config.podcast_topic} podcast. "
        f"You're revising an episode on {config.episode_topic}. "
        f"You'll be given the current podcast script. "
        f"You'll be given several Wikipedia pages at the end of this prompt. "
        f"Revise the podcast script to correct any incorrect facts. "
        f"The podcast is narrated by a single host. "
        f"Only reply with the script. "
        f"Don't include an intro or outro. "
        f"Don't include 'host:' or any indication of pauses or music. "
        f"\n{podcast_script_prompt_data}"
        f"\n{wikipedia_prompt_data}"
    )

    # Generate podcast script
    response = client.models.generate_content(
        model=config.model_name,
        contents=prompt
    )
    revised_podcast_script = response.text

    # Save revised podcast script
    with open(write_filename, 'w') as file:
        file.write(revised_podcast_script)

# Loads the podcast script and surrounds it with begin and end tags.
def load_podcast_script(filename):
    with open(filename, "r") as file:
        podcast_script = file.read()

    podcast_script_prompt_data = (
        f"||Begin Podcast Script||\n"
        f"{podcast_script}\n"
        f"||End Podcast Script||\n"
    )

    return podcast_script_prompt_data

# Returns string of page contents of page title (must be the same as the Wikipedia URL)
#   or quits if exception
def load_wikipedia_page(page_title):
    plain_text_content = f'\n||Begin Wikipedia Page {page_title}||\n'
    api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={page_title}&prop=extracts&explaintext=true&format=json"
    try:
        response = requests.get(api_url)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        data = response.json()

        # Navigate through the JSON structure to find the 'extract'
        # The structure is often: data -> query -> pages -> (page_id) -> extract
        page_id = next(iter(data['query']['pages'])) # Get the first (and usually only) page ID
        plain_text_content += data['query']['pages'][page_id]['extract']

        plain_text_content += f'\n||End Wikipedia Page {page_title}||'
        return plain_text_content

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        exit()
    except KeyError:
        print(f"Could not find 'extract' or 'pages' in the API response for '{page_title}'. The page might not exist or the API structure has changed.")
        exit()

if __name__ == '__main__':
    main()