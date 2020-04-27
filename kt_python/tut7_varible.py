# 5. Variables, Datatypes and Typecasting 
# var1 = "Automation"     # string
# var2 = 4                # int
# var3 = 35.7             # float
# var4 = "World"
# var5 = "60"
# var6 = "40"

# Lets confirm with python
# print(type(var1))
# print(type(var2))
# print(type(var3))

# Arithmetic
# print(var3 + var2)
# #print(var3 + var1) 
# print(var1 + var4) # will concatinate ?
# print(var1 + var5) # Guess ?

# print(var5 + var6) # what if i plan to add these as integer not as a string
# let me introduce typecasting
# print(int(var5) + int(var6))
# print (10 * "Hello World \n") # instead of writing it 10 times we write this way

# input() returns string
print ("Enter a number:")
inpnum = int(input()) # input("Enter a number:")
print ("You have entered",inpnum)
print (inpnum + 10)              # Find a solution to this problem

# Excercise 
# Make your own calculator which could take two values from user
# and perform + , - , * , /