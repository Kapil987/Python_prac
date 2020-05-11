## Simple example
# try:
#     print(a)
# except NameError:                       # NameError is a keyword here
#     print("Variable x is not defined")
# except:                               # Default Except it must be last
#     print("Something else wen wrong")

## With else
# try:
#     print("Hello")
# except:
#     print("erro in string")
# else:                           # if try doesn't gets error then else block is also executed 
#     print("All good")

## finally (keyword) will be executed regardless if the try block raises and error or not
# try:
#     # print(b)
#     print("Hello")
# except:
#     print("some error")
# finally:
#     print("This will printed for sure")



## Using as Exceptiona and as

# num1 = input("Enter num1: ")
# num2 = input("Enter num2: ")
# print("sum =",num1+num2)

# Lets try entering alphbetic value first for num1 and then for num2 see the line number will change, 
# Error, Problem ?

# print("This line is very important")    # This line doesn't print if above is error

## Solution
# try:
#     print("sum =",int(num1 )+ int(num2))
# except Exception as e:      # Error is catched in e
#     print(e)

# print("This line is very important")

## Practical use-case for finally
# try:
#     f = open("abc.txt")
#     f.write("did file opened")
# except:
#     print("somethin might have went wrong")
# finally:
#     f.close()

## Using raise: raise an error and stop the program if count if less than 0
# count = -1

# if count < 0:
#     print("worked till here")
#     raise Exception("unable to consider count below 0")

## Excercise
# Using raise with TypeError

