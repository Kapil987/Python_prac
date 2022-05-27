# Decorator 
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs): # caller can provide either 0 or any number of arguments
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

# Decorator 2 with advance usage
def twice_out(fun):
    def twice_inner(*abc,**gfh):
        print('twice inner: ', twice_inner.__name__)
        for i in abc:
            print(i)
        fun(*abc, **gfh)
    return twice_inner