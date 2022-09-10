## Inheritance: qualities from parents to child

class Employee:
    no_of_leaves = 8
    no_of_holiday = 100
    def __init__(self, aname, asalary, arole, atemp):  # This is constructor, called by default
        self.name = aname       # name is instance variable and aname is just an argument
        self.salary = asalary
        self.role = arole
        print("constructor of Employee function is called for: ",aname)
    
    @staticmethod
    def display(string):
        print("\nwithout self and without class, This class is for employee only")
        print("\nPrinting: " + string)
        return ("###end###")

class Programmer(Employee): # Employee is inherited to programmer child
    # no_of_holiday = 60    # first search here then upper class
    def __init__(self, bname, bsalary, brole, languages):
        self.name = bname  
        self.salary = bsalary
        self.role = brole
        self.languages = languages
        print("\nConstructor for Programmer class called by: ",bname)
#   def __init__(self):
#       pass
    def dis_prog(self):
        return f"\nProgrmmer's name is {self.name} Salary is {self.salary}, role is {self.role} and languages are {self.languages}"

vinod = Programmer("vinod", 7000, "Programmer","Python")
# vinod = Programmer()
# vikas = Programmer("vikas", 6500, "Programmer",['Java', 'Cpp'])

# vinod.dis_prog()
# print(vinod.dis_prog())
# print(vinod.display("from vinod"))    #display is employee method we can use here as inherited
# print(vikas.dis_prog())
print(vinod.no_of_holiday)