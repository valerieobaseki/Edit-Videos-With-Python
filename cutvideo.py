import os
from moviepy.editor import VideoFileClip

#get your ffmpeg path
os.environ["IMAGEIO_FFMPEG_EXE"] = (
    "/opt/homebrew/Cellar/ffmpeg/5.1.2_6/bin/ffmpeg"  # noqa: E501
)
#get the current video to be cut
existingvideo = VideoFileClip("videoname.mp4").subclip((13, 00), (32, 23))

#save it as a file named updatedvideo.mp4
existingvideo.write_videofile(
    "updatedvideo.mp4",
    codec="libx264",
    audio_codec="aac",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
)
