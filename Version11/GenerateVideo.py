# Generates a video with TTS audio + background music from SVG image.

from Config import config
from moviepy.editor import *
from moviepy.video.fx.all import resize
from moviepy.audio.fx import all as afx
from PIL import Image
import os
import cairosvg

# Load the main audio
main_audio = AudioFileClip(config.tts_audio_output_filename)
duration = main_audio.duration

# Load and loop background music to match duration
bg_audio = AudioFileClip(config.background_music_mp3)
bg_audio = bg_audio.fx(afx.audio_loop, duration=duration).volumex(0.2)

# Mix main audio and background audio
composite_audio = CompositeAudioClip([bg_audio, main_audio])

# Convert SVG to high-resolution PNG using cairosvg
png_image_path = "temp_logo.png"
cairosvg.svg2png(url=config.video_thumbnail_svg, write_to=png_image_path, output_width=1600, output_height=1600)

# Load and resize the image
image_clip = ImageClip(png_image_path, transparent=True)
image_clip = resize(image_clip, height=800)
image_clip = image_clip.set_position("center").set_duration(duration)

# Create background
background = ColorClip(size=(1920, 1080), color=(255,255,255), duration=duration)

# Composite video
video = CompositeVideoClip([background, image_clip])
video = video.set_audio(composite_audio)

# Export
video.write_videofile(config.video_output_path, fps=24, codec='libx264', audio_codec='aac')

# Clean up
os.remove(png_image_path)
print("Video created successfully as", config.video_output_path)