import os
from moviepy.editor import VideoFileClip, concatenate_videoclips


# path of folder with videos
path = '/home/lenovo/Videos/Youtube/ToMerge/'

# path of the output video to be saved
output_video = "/home/lenovo/Videos/Youtube/ToCrop/"

#merge video to the end of the output video
merge_video_to_end = "/home/lenovo/Videos/Youtube/Subscribe screen YT/subscreen.mp4"


for filename in os.listdir(path):
    print(filename)
    video1 = VideoFileClip(path+filename)
    video2 = VideoFileClip(merge_video_to_end)

    final_video = concatenate_videoclips([video1,video2],method='compose')
    final_video.write_videofile(output_video+filename)