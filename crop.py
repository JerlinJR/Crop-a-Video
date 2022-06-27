import moviepy.editor as mpy
from moviepy.video.fx.all import crop

clip = mpy.VideoFileClip("/Path to the video/")
(w, h) = clip.size
cropped_clip = crop(clip, width=600, height=5000, x_center=w/2, y_center=h/2)
cropped_clip.write_videofile('/Path of video to be saved/')