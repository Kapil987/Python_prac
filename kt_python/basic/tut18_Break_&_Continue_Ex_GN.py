i=0
# while(True):
    # print(i+1,end=' ')
    # i=i+1
    # if(i==30):
    #     break

# print greater than 4 and less than 45 , i = 0
# while(True):
#     if(i < 5):
#         i=i+1     # first i = 1, i = 2,3,4 
#         continue
#     print(i,end=' ')    # i = 5, 6
#     i=i+1               # i = 6, 7
#     if(i == 45):
#         break

# # Print congrats if number is greater than 100 and Try again continously if user enters
# number is less than 100
while(True):
    inp = int(input("Enter a Number btw 1 to 100: "))
    if inp > 100:
        print("Congrats you have entered Greater than 100")
        break
    else:
        print("Try again!\n")
        continue

# Name of the program is Guess the number: 
# Hide a number in your program and continously allow user to guess that number. if user
# guess is correct then exit the program



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