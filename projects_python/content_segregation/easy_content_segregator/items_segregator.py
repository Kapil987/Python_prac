# Os independent Segregator
import os
import platform
# print(platform.uname())
# os.mkdir('newfolder')
# print(os.getcwd(),'\n')

current_folder = os.getcwd()
print(os.walk(current_folder))

for dirpath,dirname,filenames in os.walk(current_folder):
    print('\n',dirpath,'\n')