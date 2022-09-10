# if elif else

var1 = 10
var2 = 20

# print("Enter a value ;")
# var3 = int(input())

# Simple If else
# if var3>var2:           #Check one
#     print("Greater")
# else:
#     print("Lesser")


#Problem
# if var3>var2:           #Check one
#     print("Greater")

# if var3 == var2:        #Check two Multiple checks
#     print("Equal")
# else:
#     print("Lesser")

# Solution
# if var3>var2:           
#     print("Greater")
# elif var3 == var2:       
#     print("Equal")
# else:
#     print("Lesser")


# # Switch Case implementation using Dictionary
# switch = {0:'Zero',1:'One',2:'Two'}
# print(switch[int(input("Enter a number: "))])
# switch[0]

# if else implementation on list and Dictionary
list1 = [1, 2, 3, 4]
# print("Enter a value ;")
# var3 = int(input())

# if var3 in list1:           # in keyword
#     print("Yes in list")
# else:
#     print("Not in list")

# if var3 not in list1:     # not and in are two keywords here
#     print("Condition True")
# else:
#     print("Condition False")

# The above can be replace by print
# print(var3 not in list1)      # output is form of boolean

# One liner comes with a trade-off readability

# a = int (input("enter a \n"))
# b = int (input("enter b \n"))

# if a > b: print("a is greater")
# print("a is greater") if a < b else print("b is greater")

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

## Solution
# operator = input("Enter Operator:")
# firstNum = input("Enter 1st Num:")
# secondNum = input("Enter 2nd Num:")
# faulty_dict = {"25*3":"Error!","59+9":"Error!","22/3":"Error!"}
# expression = firstNum + operator + secondNum
# if expression in faulty_dict.keys():
#     print(faulty_dict[expression])
#     pass
# else:
#     print(eval(firstNum + operator + secondNum))