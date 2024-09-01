import os
import shutil
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/5.1.2_6/bin/ffmpeg"

from moviepy.editor import VideoFileClip
mclip = VideoFileClip("videoname.mp4")
clip = VideoFileClip("videoname.mp4").subclip((13,00), (50,44))

clip.write_videofile('videoname.mp4', codec='libx264', 
                    audio_codec='aac', 
                    temp_audiofile='temp-audio.m4a', 
                    remove_temp=True)
