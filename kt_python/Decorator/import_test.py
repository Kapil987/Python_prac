# from test import repeat
import test
# from test

## ambiguity which a python should print now of file test or test2 so better use import and then use fileName.attribute name
# from test import a
# from test2 import a # this 
# print(pandas.__version__)
# print(sys.path)
# print(a)
@test.repeat
def simple():
    print('inside simple')
simple()

@test.repeat
def argu_fun(val):
    print('val is:: ',val)

argu_fun(24)