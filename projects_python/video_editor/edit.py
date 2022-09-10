import moviepy.editor as mpy
import os
from os.path import splitext
vcodec = "libx264"

videoquality = '24'
compression = 'slow'

source_dir = "E:/Programming/Python Programs/Python_prac/projects_python/video_edit"
input_format = ['.mp4']

# Searching for a single file that is of .mp4 format
def get_Title():
    with os.scandir(source_dir) as entries:
        for entry in entries:
            val = entry.name
            for i in input_format:
                if val.endswith(i):
                    return(val)

# title = get_Title()

loadtitle = get_Title()
filename, extension = splitext(loadtitle)
savetitle = filename + '_output' + extension
# print('savetitle',savetitle)

cuts = [('00:00:00.00','00:00:22.00'),('00:00:27.00','00:01:51.00'),
        ('00:01:58.00','00:03:13.00'),('00:03:19.00','00:05:48.00'),
        ('00:05:55.00','00:06:48.00')]#('00:07:17.00','00:09:05.00'),
        # ('00:09:11.00','00:10:38.00'),('00:10:44.00','00:12:40.00'),
        # ('00:12:46.00','00:13:29.00')]#('00:08:16.00','00:08:59.00')]

def edit_video(loadtitle, savetitle, cuts):
    #load file
    video = mpy.VideoFileClip(loadtitle)

    #cut file
    clips = []
    for cut in cuts:
        clip = video.subclip(cut[0],cut[1])
        clips.append(clip)
    
    final_clip = mpy.concatenate_videoclips(clips)

    final_clip.write_videofile(savetitle,
                                threads=4,fps=24,codec=vcodec,
                                preset=compression,ffmpeg_params=["-crf",
                                videoquality])
    video.close()

if __name__ == '__main__':
    edit_video(loadtitle, savetitle, cuts)