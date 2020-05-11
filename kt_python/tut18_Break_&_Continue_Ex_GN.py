
i=0
# while(True):
#     print(i+1,end='')
#     i=i+1
#     if(i==30):
#         break

# print greater than 5 ans less than 45
# while(True):
#     if(i < 5):
#         i=i+1
#         continue
#     print(i,end=' ')
#     i=i+1
#     if(i == 45):
#         break

# # Print congrate if number is greater than 100 and Try again continously number is less than 100
# while(True):
#     inp = int(input("Enter a Number"))
#     if inp > 100:
#         print("Congrats you have entered Greater than 100")
#         break
#     else:
#         print("Try again!\n")
#         continue

# Name of the program is Guess the number: 
# Hide a number in your program and continously allow user to guess that number 



# l = 20;
# def fun():
#     # global l 
#     l = 100
#     l = l + 10
#     print("inside fun l=",l)

# fun()
# print("outside fun l=",l)

## Nested Functions

# x = 200
# def foo():
#     x = 20      #Local variable is preffered
#     def fun2():
#         global x      # take this variable in global space and then understand
#         x = 200
# print("Before calling fun2",x)
# # fun2()
# print("after calling fun2",x)

# foo()
# print(hex(id(foo)))