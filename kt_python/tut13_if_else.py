# if elif else

# var1 = 10
# var2 = 20

# print("Enter a value ;")
# var3 = int(input())

# if var3>var1:
#     print("Greater")
# elif var3==var1:
#     print("equal")
# else:
#     print("Lesser")

# # Switch Case implementation using Dictionary
switch = {0:'Zero',1:'One',2:'Two'}
# print(switch[int(input("Enter a number: "))])

# if else implementation on list and Dictionary
list = [1, 2, 3, 4]
inp_var = int(input("Enter a value to be searched: "))
if inp_var not in list:             # in and not are different keywords
    print("Present in list")
else:
    print("Not present in list")
