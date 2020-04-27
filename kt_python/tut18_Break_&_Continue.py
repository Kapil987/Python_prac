
# l = 20;
# def fun():
#     # global l 
#     l = 100
#     l = l + 10
#     print("inside fun l=",l)

# fun()
# print("outside fun l=",l)

## Nested Functions

x = 200
def foo():
    x = 20      #Local variable is preffered
    def fun2():
        global x      # take this variable in global space and then understand
        x = 200
print("Before calling fun2",x)
# fun2()
print("after calling fun2",x)

foo()
print(hex(id(foo)))