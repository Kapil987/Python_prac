# f = open("demo.txt",'w')            # opened in write mode
# count = f.write("\nlife is an adventurer")
# print(count)
# f.close()                       # Garbage collector does close it but still is a good practice


# f = open("demo.txt",'a')            # opened in append mode
# count = f.write("\nlife is an adventurer")
# print(count)
# f.close()                       # Garbage collector does close it but still is a good practice

## with read and write mode together
# f = open("demo.txt",'r+')
# print(f.read())
# f.write("\nThank You!")
# print(f.read())
# f.close()

## f.tell() : where is file pointer
# f = open("demo.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()

## f.seek() : reset file pointer
# f = open("demo.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.seek(0)         # 0 , 10, 15 etc
# print(f.readline())
# f.close()

