import os
import moviepy.editor as mpy
from moviepy.video.fx.all import crop

# Specify the path correctly
path = '/home/lenovo/Videos/Edit/'
# path = '123/'
print("Starting....")

for filename in os.listdir(path):
        clip = mpy.VideoFileClip(path+filename)
        (w, h) = clip.size
        cropped_clip = crop(clip, width=600, height=5000, x_center=w/2, y_center=h/2)
        cropped_clip.write_videofile('/home/lenovo/Videos/sample/'+filename)





