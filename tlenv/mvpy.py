from moviepy.editor import VideoFileClip

def get_video_duration(filename):
    clip = VideoFileClip(filename)
    return clip.duration
