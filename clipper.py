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
    target = "C:/Users/pedro/OneDrive/Documentos/Codes/yt/clips/V{}.mp4".format(clipCounter)
    ffmpeg_extract_subclip(PATH, time0, time1, targetname = target)
    time0 = time1
    clipCounter += 1

clipper(PATH="C:/Users/pedro/OneDrive/Documentos/Codes/yt/video1.mp4", clip_length=5)
