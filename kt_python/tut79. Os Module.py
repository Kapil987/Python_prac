import os

## EX-1
# print (dir(os))
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# # f = open("test.py")
# # f.close()
# ## \\ to avoid escape sequence
# os.chdir("c:\\Users\kk186085\OneDrive - Teradata\My Learnings\Python Prog\kt_python") 
# f = open("test.py")
# f.close()
# print(os.getcwd())

##EX-2
# print(os.listdir("c://"))
# print(type(os.listdir("c://")))

## EX-3 delete a emply folder
# os.remove() removes a file.
# os.rmdir() removes an empty directory.
# shutil.rmtree() deletes a directory and all its contents. 

# os.mkdir("temp_folder")
# os.chdir("C:\\Users\kk186085\Desktop")
# print(os.getcwd())
# print(os.listdir())
# os.rename("delete","ndel")

##
# print(os.environ.get('Path'))

##
print(os.path.join("c:\\","demo.txt"))
print(os.path.exists("c:\\"))
print(os.path.isfile("C:\Kapil\My Stuff\Videos\Python\Part 07-Module 01-Lesson 01_Why Python Programming\index.html"))

## delete shows error
# direc = "delete"
# full_path = os.path.join(location,direc)
# os.remove(full_path)
# os.remove("temp_folder")

