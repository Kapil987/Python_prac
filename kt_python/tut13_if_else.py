# if elif else

# var1 = 10
# var2 = 20

# print("Enter a value ;")
# var3 = int(input())

# if var3>var2:           #Check one
#     print("Greater")
# if var3 == var2:        #Check two
#     print("Equal")
# else:
#     print("Lesser")

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
# if var3 in list1:
#     print("Yes in list")
# else:
#     print("Not in list")

# if var3 not in list1:     # not and in are two keywords here
#     print("True")
# else:
#     print("False")
# The above can be replace by print
# print(var3 not in list1)      # output is form of boolean

inp_var = int(input("Enter a value to be searched: "))
if inp_var not in list:             # in and not are different keywords
    print("Present in list")
else:
    print("Not present in list")


# Quiz
# print("What is your age?")
# age = int(input())
# if age<18:
#     print("You cannot drive")
# elif age == 18:
#     print("We will think about you")
# else:
#     print("You can drive")

# but if you enter 7777 it will say you can drive this is Problem!!!

#Exercise
# Design a calulator which solves the problem for all except the following
# 25 * 3 = 75, 59 + 9 =77, 22/3 = 7.0
