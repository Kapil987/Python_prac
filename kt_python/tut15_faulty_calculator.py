# Faulty Calculator
# list1 = list(range(1,6))
# print(list1)
# Design a calulator which solves the problem for all except the following
# 25 * 3 = 75, 59 + 9 =77, 22/3 = 7.0
# or (oper == "/" and (var1 != 22 and var2 !=3))
# or (oper == "*" and (var1 != 25 and var2 !=3)
var1 = int(input("Enter 1st number: "))
var2 = int(input("Enter 2nd number: "))
oper = (input("Enter + ,  *, /: "))
# di_cal = { "ADD" : "+" ,  "MUL" : "*", "DIV" : "/"}

if (oper == "+" and (var1 == 59 and var2 == 9)) or (oper == "*" and (var1 == 25 and var2 == 3)) or (oper == "/" and (var1 == 22 and var2 == 3)):
    print("Error!")
elif (oper == "+"):
    print("Result of is ADD : ",var1+var2)
elif (oper == "*"):
    print("Result of is MUL : ",var1*var2)
elif (oper == "/"):
    print("Result of is DIV : ",var1/var2)
else:
    print("Wrong input ")






    """
    operator = input("Enter Operator:")
firstNum = input("Enter 1st Num:")
secondNum = input("Enter 2nd Num:")
faulty_dict = {"25*3":"Error!","59+9":"Error!","22/3":"Error!"}
expression = firstNum + operator + secondNum
if expression in faulty_dict.keys():
    print(faulty_dict[expression])
    pass
else:
    print(eval(firstNum + operator + secondNum))
    """