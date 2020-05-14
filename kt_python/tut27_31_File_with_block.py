

# try:
#     f = open("demo.txt",'r')    # Try with demo1.txt
#     print(f.readline())
# except:
#     print("File not found Error!")
# finally:                        # comment for demo1.txt
#     f.close()                   # comment for demo1.txt

## File handling with 'with' block , There is no need to call f.close in case of with, it take care of it
# with open("demo.txt",'r') as f:
#     print(f.readline())

# Question of the day
# with open("demo.txt",'r') as f:
#     print(f.readline())
# f = open("demo.txt",'r')
# print(f.readline())
# f.close()

# Options
# a) a line will print
# b) all lines in the file will print
# c) No lines will print
# d) there will an error