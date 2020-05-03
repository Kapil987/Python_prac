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