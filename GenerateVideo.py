# Step 3, generate video

from Config import config
from moviepy.editor import *
from moviepy.video.fx.all import resize
from PIL import Image
import os
import cairosvg

# Convert SVG to PNG
png_image_path = "temp_thumbnail.png"
cairosvg.svg2png(url=config.video_thumbnail, write_to=png_image_path, output_width=1600, output_height=1600)

# Load audio
audio = AudioFileClip(config.tts_audio_output_filename)
duration = audio.duration

# Load and resize the image to fit YouTube resolution (1920x1080)
image_clip = ImageClip(png_image_path, transparent=True)
image_clip = resize(image_clip, height=800)
image_clip = image_clip.set_position("center").set_duration(duration)

# Create background
background = ColorClip(size=(1920, 1080), color=(255,255,255), duration=duration)

# Composite the image on top of the background
video = CompositeVideoClip([background, image_clip])
video = video.set_audio(audio)

# Write the result to a video file
video.write_videofile(config.video_output_filename, fps=24, codec='libx264', audio_codec='aac')

# Delete temporary image file
os.remove(png_image_path)