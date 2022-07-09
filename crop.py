import os
from moviepy.editor import VideoFileClip,concatenate_videoclips
import moviepy.editor as mpy
from moviepy.video.fx.all import crop

# path of the video file to be cropped
path = '/home/lenovo/Videos/Youtube/ToCrop/'


#path of the video file to be saved after cropping
output_video = '/home/lenovo/Videos/Youtube/sample/'


for filename in os.listdir(path):

        clip = mpy.VideoFileClip(path+filename)
        (w, h) = clip.size
        cropped_clip = crop(clip, width=600, height=5000, x_center=w/2, y_center=h/2)
        cropped_clip.write_videofile(output_video+filename)





