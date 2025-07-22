from Config import config
from groq import Groq

def main():
    # Groq client
    client = Groq(
        api_key=config.groq_api_key,
    )
    
    # Generate outline
    generate_outline(
        topic=config.podcast_topic,
        model_name=config.model_name,
        client=client,
        podcast_outline_filename=config.podcast_outline_filename
    )

    # Generate script
    write_podcast_script(
        podcast_topic=config.podcast_topic,
        podcast_outline_filename=config.podcast_outline_filename,
        podcast_script_filename=config.podcast_script_filename,
        model_name=config.model_name,
        client=client
    )

def generate_outline(
        topic: str,
        model_name: str,
        client: Groq,
        podcast_outline_filename: str
    ):
    """
    Generates a list of section titles/outlines for the given topic.
    Saves the list to the file config.script_outline_filename.
    """

    # Prompts
    system_prompt_generate_sections = (
        f"You're part of a team that produces podcasts."
        f"It's your job to create an outline for the podcast."
    )
    user_prompt_generate_sections = (
        f"Create a list of sections that outline the topic {topic}."
        f"Format your response so that each section is on a separate line."
        f"Do not include intro or outro."
        f"Only reply with the list of sections."
    )

    # Generate outline
    chat_completion_podcast_script = client.chat.completions.create(
        messages = [
            {"role": "system", "content": system_prompt_generate_sections},
            {"role": "user", "content": user_prompt_generate_sections}
        ],
        model=model_name,
        stream=False
    )
    podcast_outline = chat_completion_podcast_script.choices[0].message.content

    # Save outline to file
    with open(podcast_outline_filename, 'w') as f:
        f.write(podcast_outline)


def write_podcast_script(
        podcast_topic: str,
        podcast_outline_filename: str,
        podcast_script_filename: str,
        model_name: str,
        client: Groq
    ):
    """
    Generates the podcast script
    """

    full_podcast_script = f'<podcast_title>{podcast_topic}<end_podcast_title>\n'
    # Generate script for each section
    with open(podcast_outline_filename, 'r') as file:
        for line in file:
            section = line.strip()
            section_script = write_podcast_section(
                section=section,
                podcast_topic=podcast_topic,
                model_name=model_name,
                client=client
            )
            full_podcast_script += f'\n<section_title>{section}<end_section_title>\n'
            full_podcast_script += section_script
            full_podcast_script += '\n'

    # Save script to file
    with open(podcast_script_filename, 'w') as f:
        f.write(full_podcast_script)

def write_podcast_section(
        section: str,
        podcast_topic: str,
        model_name: str,
        client: Groq
    ):
    """
    Generates a specific section for the podcast
    """

    # Prompts
    system_prompt_write_section = (
        f"You're part of a team producing a podcast on {podcast_topic}"
        f"It's your job to write the podcast script."
        f"You'll write the script one section at a time."
    )
    user_prompt_write_section = (
        f"Write the script for the section on {section} for the podcast {podcast_topic}."
        f"Don't include 'host:'."
        f"Don't include any intros or outros."
        f"Don't include any tags to indicate music changes or pauses."
        f"Only reply with the script."
    )

    # Generate section
    chat_completion_podcast_script = client.chat.completions.create(
        messages = [
            {"role": "system", "content": system_prompt_write_section},
            {"role": "user", "content": user_prompt_write_section}
        ],
        model=model_name,
        stream=False
    )
    section_script = chat_completion_podcast_script.choices[0].message.content
    return section_script

if __name__ == '__main__':
    main()
