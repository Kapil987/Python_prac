# Customized for windows
import os
from os.path import splitext, exists, join
import time
from watchdog.observers import Observer
from shutil import move
from watchdog.events import FileSystemEventHandler

source_dir = "C:/Users/Kapil/Downloads/"
destination_dir_video = "C:/Users/Kapil/Videos/files"

# """
video_extension = ['.mp4']


def make_unique(path):
    filename, extension = splitext(path)
    counter = 1
    while exists(path):
        path = f'{filename} ({counter}){extension}'
        counter += 1
    print('make_unique: ', path)
    return path

def move_file(dest, name):
    print(f'dest: {dest}, this is name: {name}')
    destination_file_check = (f'{dest}/{name}')
    change_name = os.path.join(source_dir, name)
    if exists(destination_file_check):
        unique_name = make_unique(destination_file_check)
        time.sleep(1) # two other process accessing the file error may occur
        # rename(change_name,unique_name)
        print(f'\n Renaming and moving file name: {change_name} to {unique_name}')
        move(change_name,unique_name)
        print('Going back')
        return
    
    print(f'\nmoving file name: {change_name} \ndestination: {dest}')
    time.sleep(1) # PermissionError: [Errno 13] Permission denied: 'C:/Users/Kapil/Downloads/docker - Copy.mp4' might occuer
    move(change_name, dest)

class moveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_video_file(name)

    def check_video_file(self, name):
        for video in video_extension:
            if name.endswith(video) or name.endswith(video.upper()):
                move_file(destination_dir_video, name)


if __name__ == "__main__":
    path = source_dir
    event_handler = moveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# """
