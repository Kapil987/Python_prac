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
# shutil.rmtree() deletes a directory and all its contents. # import shutil for this to work

# os.mkdir("temp_folder")
# os.chdir("C:\\Users\kk186085\Desktop")
# print(os.getcwd())
# print(os.listdir())
# os.rename("delete","ndel")

##
# print(os.environ.get('Path')) # for linux use PATH

##
print(os.path.join("c:\\","demo.txt"))
print(os.path.exists("c:\\"))
print(os.path.isfile("C:\Kapil\My Stuff\Videos\Python\Part 07-Module 01-Lesson 01_Why Python Programming\index.html"))
# os.path.isdir("path to dir")

## delete shows error
# direc = "delete"
# full_path = os.path.join(location,direc)
# os.remove(full_path)
# os.remove("temp_folder")

"""
#!/usr/bin/env python
import os
import sys
import datetime
old_stdout = sys.stdout
log_file = open('message.log','a+')
sys.stdout = log_file

local_time = datetime.datetime.now().strftime("%Y-%m-%d--%H:%M:%S")
print('\n')
print ("Script Started at : ",local_time)
print('\n')

d = '/root/py_scripts/'

for f in os.listdir(d):
    if os.path.isfile(d + f):
        print(f)


print ('Script End \n')

sys.stdout = old_stdout
log_file.close()


"""

""" 
#!/usr/bin/env python
import logging

#now we will Create and configure logger
logging.basicConfig(filename="std.log",
                                        format='%(asctime)s %(message)s',
                                        filemode='w')

#Let us Create an object
logger=logging.getLogger()

#Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#some messages to test
logger.debug("This is just a harmless debug message")
logger.info("This is just an information for you")
logger.warning("OOPS!!!Its a Warning")
logger.error("Have you try to divide a number by zero")
logger.critical("The Internet is not working....")
"""