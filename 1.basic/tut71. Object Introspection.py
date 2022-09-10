## dir() and inspect.getmembers() are basically the same, while __dict__ is the complete 
# namespace inculding metaclass attributes

import inspect
class Employee:
    no_of_leaves = 8
    def __init__(self, fname, lname):  # This is constructor, called by default
        self.fname = fname       # name is instance variable and aname is just an argument
        self.lname = lname
        print("constructor/init function is called for: ",fname)
    
    def print_abc():
        pass

rahul = Employee("Rahul","Kumar") 

print(rahul.__dict__,"\n")  #Key value pairs
print(dir(rahul),"\n")      # functions and attributes
# print(inspect.getmembers(rahul))  # fucntions , attributes, key value pairs, addresses 
                                  # of objects
print(type(rahul))      # type also comes in object introspection