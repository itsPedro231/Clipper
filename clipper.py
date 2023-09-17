from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *

# Script to clip videos.

def clipper(PATH, clip_length):
  clip = VideoFileClip(PATH)
  duration = int(clip.duration)
  print("Video length:", duration/60, "min\n")
  
  time0 = 0
  clipCounter = 1

  for time1 in range(clip_length, duration+1, clip_length):
    target = "PATH/FILENAME{}.mp4".format(clipCounter)
    ffmpeg_extract_subclip(PATH, time0, time1, targetname = target)
    time0 = time1
    clipCounter += 1

clipper(PATH="PATH TO VIDEO", clip_length=5)
