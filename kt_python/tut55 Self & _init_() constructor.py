## Example 1
# class Employee:
#     no_of_leaves = 8
#                         # self means object in picture ie kapil or rohan, remove self and 
#     def display(self):  # see the error that shows on argunment is auto passed print(kapil.display())
#         return f"Name is {self.name} Salary is {self.salary} and Role is {self.role}"

# kapil = Employee()
# rohan = Employee()

# kapil.name = "kapil"
# kapil.salary = "2000"
# kapil.role  = "programmer"

# rohan.name = "rohan"
# rohan.salary = "3000"
# rohan.role   = "principal"

# print(kapil.display())
# print(rohan.no_of_leaves)   # class variable can be accessed by objects

## Conclusion: 
# Self is a convention and not a real python keyword
# self is parameter in function and user can use another parameter name in place of it.
# But it is advisable to use self because it increase the readability of code.

# self represents the instance of the class. By using the “self” keyword we can access 
# the attributes and methods of the class in python. It binds the attributes with the given 
# arguments.


## example 2
## Constructor = to make Employee class to take argument
class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname       # name is instance variable and aname is just an argument
        self.salary = asalary
        self.role = arole
        print("\nEmp Const is called by: ",aname)  
    
    # def __init__(self):
    #     print("this is sample constructor") 

# both objects have different self which contain their attributes 
# kapil = Employee("Kapil", 5000, "Programmmer")  # if init func is commented this give error
rohan = Employee() 
# rohan = Employee("rohan",3000,"Principal")

# print(kapil.salary)