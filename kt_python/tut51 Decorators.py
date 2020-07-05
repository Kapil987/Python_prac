# def function1():
#     print("This is function 1")

# func2 = function1       # copy is made in func2 so deleting function1 no matter
# del function1
# func2()

### Returning function by function
# def funret(num):    
#     if num == 0:
#         return print    # print and int are built-in function
#     if num == 1:
        # return int      # can be replace by sum function
# a = funret(0)
# print(a)

### Pasing function as an argument
# def executor (func):    # print is passed as argument here
#     func("This is")     # func("This is") becomes print("This is")
# executor(print)

## Decorator
def dec1(fun1): #fun1 = who_is_kapil
    def nowexec():
        print("execution now")
        fun1()
        print("executed")
    return nowexec

@dec1   # @dec1 = [ who_is_kapil = dec1(who_is_kapil) ]
def who_is_kapil():            # = nowexec
    print("Kapil is a good boy")
    # def abc():
    #     print("This is abc")

# who_is_kapil()
# who_is_kapil = dec1(who_is_kapil)
# print("address",who_is_kapil)
who_is_kapil()      #who_is_kapil = nowexec()

# print(who_is_kapil)
