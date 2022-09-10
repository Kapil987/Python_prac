"""
# for undersatnding pasting ORGINAL do_twice deco definition
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
"""
"""
# Import type
1) import decorator: In general this is best practice
    @decorator.do_twice
2) from decorator import do_twice:
    @dotwice

"""

# import decorator
from decorator import do_twice
 
# @decorator.do_twice
@do_twice
def say_hi():
    print("This is",say_hi.__name__) # this will print @do_twice inner function name, if not decorated then will print say_hi
say_hi()                             # as function name
 
def your_name(name, name2, name3):
    print(f"Your name is: {name} {name2} {name3}")

your_name("Kapil",'karan','Koshanl') # TypeError: wrapper_do_twice() takes 0 positional arguments but 1 was given

"""
Two possible solution here:
1)  Change the wrapper_do_twice() definition to such as it accepts an argument. example: wrapper_do_twice(name)
    this solution will solve your_name("Kapil") but creates problem when you call: say_hi()
    
    say_hi()
    TypeError: wrapper_do_twice() missing 1 required positional argument: 'name'

2)  The bettor solution to this problem is to use *args,**kwrgs in the inner wrapper function. 
    Then it will accept an arbitrary number of positional and keyword arguments

MODIFIED do_twice Decoraor Definition
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func()
        func()
    return wrapper_do_twice
"""

"""

# """
# import decorator
# deco twice_out caller function
from decorator import twice_out
@twice_out 
def new(*var,**accept):
    print('new from var: ' + str(var) + str(accept.items()))

new('aft','night',name = 'Morning')
