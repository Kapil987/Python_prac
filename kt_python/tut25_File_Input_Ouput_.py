## File I/O Basics
"""
"r" - Open file for reading
"w" - Open file for writing
"x" - Create file if not exist
"a" - Add more content to a file
"t" - Open file in text mode
"b" - Binary mode
"+" - Read and Write
"""
## To read a file will need a file pointer
# open("demo.txt") # no use of this open so will file pointer
# f = open("demo.txt")
# content = f.read()
# print(content)
# f.close()       # Close like we close our fridge after use, Good Practice

## Let specify modes
# f = open("demo.txt","rt")   #Change different modes
# content = f.read()
# print(content)
# f.close()       # Close like we close our fridge after use, Good Practice

## Reading Character by charater
# f = open("demo.txt","rt")   
# content = f.read(3)
# print(content)
# content = f.read(3)     
# print(content)
# f.close()      

## No output for last print
# f = open("demo.txt","rt")   
# content = f.read(344)
# print("1=",content)
# content = f.read(456)    
# print("2=",content)
# f.close()      

## using for loop Char by Char
# f = open("demo.txt","rt")   
# content = f.read()
# for line in content:
#     print(line)
# f.close()      

## using loop with file descritor
# f = open("demo.txt","rt")   
# # content = f.read()
# for line in f:
#     print(line,end='')
# f.close()      

## using readline function
# f = open("demo.txt","rt")   
# print(f.readline())
# print(f.readline())
# f.close()      

## using readlines function
# f = open("demo.txt","rt")   
# print(f.readlines())
# f.close()      

## Openig a file and writing it into f.write