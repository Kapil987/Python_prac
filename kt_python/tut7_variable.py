# 5. Variables, Datatypes and Typecasting  
# Var cannot start with number 
# Var cannot have space
# Var can only have alphanumeric character
# Var name are case sensistive

var1 = "World"          # string
var2 = 4                # int
var3 = 35.7             # float
var4 = "Automation"
var5 = "60"
var6 = "40"
var7 = "50.5"

## Lets confirm with python
# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var5))

## Arithmetic
print(var3 + var2)
# print(var3 + var1) 
print(var1 + var4) # will concatinate ?
print(var1 + var5) # Guess ?

# print(var5 + var6) # what if i plan to add these as integer not as a string

## let me introduce typecasting
# print(int(var5) + int(var6))

## Let try this one out
# print(int(var3) + int(var7))  # Error! you want it to be integer but it became float
## solution # https://www.geeksforgeeks.org/what-is-the-meaning-of-invalid-literal-for-int-with-base/
print(int(var3) + int(float(var7))) 
# print (10 * "Hello World \n") # instead of writing it 10 times we write this way



## Get familiar with input() function , default : returns a string
# print ("Enter a number:")
# inpnum = int(input()) # input("Enter a number:")
# inpnum = 45
# print ("You have entered",type(inpnum))
# print (inpnum + 10)              # Find a solution to this problem




# Excercise 
# Make your own calculator which could take two values from user
# and perform + , - , * , /