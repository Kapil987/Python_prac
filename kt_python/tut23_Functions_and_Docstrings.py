## Function are used for Code re-usablility
# a = 10
# b = 20
# c = sum ((a , b)) # Built in function
# print(c)

## User define function

# def fun1():
#     print("in fun 1")

# fun1()
# fun1()
# fun1()

def fun2(a,b):
    average = (a+b)/2
    # print(average)
    return(average)
# val = fun2(5,5)
# print(val)
# print("Average =",fun2(5,5))

## function to add element in list
# list1 = []
# def add_in_list(value):
#     list1.append(value)

# add_in_list(1)
# add_in_list(10)
# print(list1)
# print(sum(list1))

## docstring
def fun3(a,b):
    """ 1st line in function with quotes is docstring: this fun2 will calculate average for two numbers,
    this function doesn't work for Three or more numbers"""
    average = (a+b)/2
    return(average)
    
print(fun3.__doc__)
