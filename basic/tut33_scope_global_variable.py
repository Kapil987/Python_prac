## Global and local , 
## example scope of services we provide, state and central gov
# x = 10          # Global scope , center money
# def fun1():
#     x = 20      # Local scope , state money
#     print("in fun1 x is: ",x)

# fun1()
# print("in main x is: ",x)

## Look first at local and then at global
# x = 10          # Global
# def fun1():
#     x = 20      # Local
#     m = 8
#     print("in fun1 x is: ",x)

# fun1()
# print("in main x is: ",x)
# print(m)          # Error! m is local

## if not in local Program will choose global
# x = 10          # Global
# def fun1():
#     x = 20     # Local , x not in local scope so choose global
#     m = 8
#     print("in fun1 x is: ",x)

# fun1()
# print("in main x is: ",x)

##
## x as read only variable in local scope when try to change
## its value in fun1
# x = 10          # Global
# def fun1():
#     # x = 20     # Local , x not in local scope so choose global
#     m = 8
#     x = x + 20
#     print("in fun1 x is: ",x)   #30

# fun1()
# print("in main x is: ",x)       #10

## Take permission to change x by using keyword global , Problem solved
# x = 10          # Global
# def fun1():
#     global x    # Local , x not in local scope so choose global
#     m = 8
#     x = x + 20
#     print("in fun1 x is: ",x)

# fun1()
# print("in main x is: ",x)

## Question ?, there is nothing in global area

# def outer():
#     x = 20      # local variable
#     def inside():
#         global x
#         x = 88
#     print("before calling inside: ",x)  #88 #20
#     inside()
#     print("After calling inside: ",x)   #88 #20

# outer()
# print("outside: ",x)    #88

## Question
# x = 100
# def outer():
#     x = 20      # local variable
#     def inside():
#          x
#         x = 88
#     # print("before calling inside: ",x)
#     inside(global)
#     print("After calling inside: ",x)   # 20

# outer()
# print("outside: ",x)    #100


