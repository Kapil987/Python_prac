class Employee:
    no_of_leaves = 8
    _protected = 55 # can be accessed by base and derived/inherited classes only "_" used for notation
    __private = 99  # can be accessed only withing this class "__" used for notation
    # __temp = 100
    def __init__(self, aname, asalary, arole):  # This is constructor, called by default
        self.name = aname       # name is instance variable and aname is just an argument
        self.salary = asalary
        self.role = arole
        print("constructor/init function is called for: ",aname)
        
    @classmethod            # another way of writing it
    def from_str(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def display(string):
        print("\nwithout self and without class, This class is for employee only")
        print("\nPrinting: " + string)
        return ("###end###")
class Programmer(Employee):
    temp = 10

rohan = Programmer("Rohan",543,"Programmer")
print(rohan.no_of_leaves)
print(rohan._protected)
print(rohan._Employee__private)

# kapil = Employee()  #Will not work
# kapil = Employee("Kapil",345,"Programmer")

# print(kapil._protected)
# print(kapil.__private) 

# Private variable can be accessed only with class name, Python make it little bit complicated
# so that no one access it by mistake, "_className__variableName"

# print(kapil._Employee__private) # Name handling by Python its saved this way