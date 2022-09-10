# print(a)
## Simple example, Generalising all exceptions
# a = 10
# try:
#     print(a)
# except:                           # default executes everytime
#     print("Something went wrong")

## Capturing specific errors
# a = 10
# try:
#     print(a)
# except SyntaxError:                       # SyntaxError consider change to NameError is a keyword here
#     print("Variable a is not defined")
# except:                               # Default Except it must be last
#     print("Something else went wrong")

## With else
# str1 = "hello"
# try:
#     print(str1)
# except:
#     print("ERROR in string")
# else:                           # if try gets error then else block will not executed 
#     print("All good")

## finally (keyword) will be executed regardless if the try block raises and error or not
# str1 = "hello"
# try:
#     print(str1)
# except:
#     print("some error with the try block")
# finally:
#     print("This is important and will printed for sure")



## Using as Exception and as

# num1 = int(input("Enter num1: "))
# num2 = input("Enter num2: ")
# print("sum =",num1+num2)

# Lets try entering alphbetic value first for num1 and then for num2 see the line number will change, 
# Error, Problem ?

# print("This line is very important")    # This line doesn't print if above is error

## Solution
# try:
#     num1 = int(input("Enter num1: "))
#     num2 = input("Enter num2: ")
#     # print("sum =",int(num1) + int(num2))
#     print("sum =",(num1 + num2))
# except Exception as e:      # Error is catched in e
#     print(e)

# print("This line is very important")



## Using raise: raise an error and stop the program if count if less than 0
# count = 1

# if count < 0:
#     print("worked till here")
#     raise Exception("unable to consider count below 0")
# print("did i got printed!")


## Excercise
# Using raise with TypeError

