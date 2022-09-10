##
# with open("demo.txt",'r') as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     # print(f.tell())
#     print("last print:",f.readline()) #no ouput ??
# x =10
# print("value:",x,end="\n")
## Let find out where is the cursor
with open("demo.txt",'r') as f:
    print(f.tell())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.tell())
    f.seek(0,2)
    # f.seek(15)
    # print(f.read()) #no ouput ??
    print(f.tell())
    print(f.readline())
    print(f.tell())
    f.seek(1)
    print(f.tell())
    f.seek(2)
    print(f.tell())
# with open("demo.txt",'r') as f:
#     i = 1
#     while(i != 28):
#         print(f.read(i))
