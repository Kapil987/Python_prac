# Static method: used when neither instance or class varibale is accessed, let say
# we need to display a info in print that this class is for only employee

class Employee:
    no_of_leaves = 8
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

# karan = Employee.from_str("karan-6000-Tutor")
karan = Employee.from_str("karan-3500-Student")  
# karan.display("Static Method")
# print(karan.display("Static Method"))
Employee.display("Class Employee") 

