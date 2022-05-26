## example 1 : How to change class varibale by decorator without using self
## Constructor = to make Employee class to take argument
class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):  # cls(params[0],params[1],params[2] .This is constructor, called by default
        self.name = aname       # name is instance variable and aname is just an argument
        self.salary = asalary
        self.role = arole
        print("constructor/init function is called for: ",aname)

    @classmethod    # way to give access to class objects/instances to change class variable ie. no.of.leaves 
    def change_leaves(cls,new_leaves): # cls is just a class whic is called by class name or instance name
        cls.no_of_leaves = new_leaves

    # @classmethod
    # def from_str(cls, string):
    #     params = string.split("-")
    #     return cls(params[0],params[1],params[2] # this is passed to __init__

    @classmethod            # another way of writing it, #Alernative constructor
    def from_str(cls, string):
        return cls(*string.split("-"))

# kapil = Employee("Kapil", 5000, "Programmmer")
# rohan = Employee() # Employee("rohan",3000,"Principal")
# karan = Employee("karan-3500-Student") # error
karan = Employee.from_str("karan-3500-Student")     #constructor is also called
print(karan.salary)