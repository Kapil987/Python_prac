## 1
def fun1(a, b, c, d):
    print(a, b, c, d)

# fun1("Amar","Akbar","Anthony","Amit") # unable to give 5 arguments here

## 2
## function(normal_argument, *args, **kwargs) sequence is convenstion
def fun_arg(str_class,*args,**kwargs): # args is just convention we can change this name, keep args after str_class
    # print(type(args))         # else error
    print(str_class)
    # print("args: ",args[0])
    for i in args:
        print(i)
    print("Staff\n")
    for key,value in kwargs.items():
        print(f"{key} is {value}")

list_str = ["Amar","Akbar","Anthony","Amit"]
str_class = "These are student of class 9:"
kw = {"Sohan":"Head", "Ram":"Teacher","Kapil":"Programmer"}
# fun_arg(str_class,*list_str,**kw)
fun_arg(str_class,*list_str,**kw)