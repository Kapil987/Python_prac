from moviepy.editor import AudioFileClip
import os

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

file_name = get_Title()
def extract_audio():
    audio = AudioFileClip(file_name)
    audio.write_audiofile(file_name + '_audio.mp3',44100)

if __name__ == '__main__':
    extract_audio()