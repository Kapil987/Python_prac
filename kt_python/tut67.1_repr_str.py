# Example3: Operator Over Loading in classes
class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):  # This is constructor, called by default
        self.name = aname       # name is instance variable and aname is just an argument
        self.salary = asalary
        self.role = arole
        print("constructor/init function is called for: ",aname)
        
    def __add__(self,other):        #Dunder Method , called as Dunder add
        print("\nDunder add is called")
        return self.salary + other.salary
    
    def __truediv__(abc,other):
        print("Truediv / is called")
        return abc.salary / other.salary
    
    def print_obj(self):
        return f"\nprint_obj called \
Name is {self.name} , Salary is {self.salary} and Role is {self.role}"

    def __repr__(self):
        return f"__repr__\nEmployee ('{self.name}', {self.salary} , '{self.role}')"
        # return self.print_obj()

    # def __str__(self):
    #     return f" __str__\nName is {self.name} , Salary is {self.salary} and Role is {self.role}"

ram = Employee("vijay",100,"Tutor")
# ram.print_obj()
print(ram)
print(str(ram)) # even if str is called and str is not present repr gets called if present
# print(repr(ram)) # explicit call to repr

## Conclusion
# 1. if __str__ is not present __repr__ is called
# 2. even if explicit call is made to str and str is not present
#  repr gets called if present


