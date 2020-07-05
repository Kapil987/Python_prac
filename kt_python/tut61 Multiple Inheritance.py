#Multiple Inheritance: 2 or more classes used to drive a single class (ex CoolProgrammer)
class Employee:
    no_of_leaves = 8
    var = 1
    def __init__(self, aname, asalary, arole):  # This is constructor, called by default
        self.name = aname       # name is instance variable and aname is just an argument
        self.salary = asalary
        self.role = arole
        print("\nConstructor/init function is called for: ",aname)
    
    @staticmethod
    def display(string):
        # print("\nwithout self and without class, This class is for employee only")
        # print("\nPrinting: " + string)
        
        return ("###end###")
    
    @classmethod
    def from_str(cls, string):
        params = string.split("-")
        return cls(params[0],params[1],params[2])
    
    def print_emp(self):
        print(f"\nName is {self.name} , Salary is {self.salary} and Role is {self.role}")

class Player:
    no_of_games = 4
    var = 5
    def __init__(self, cname, cgame):
        self.name = cname
        self.game = cgame
        print("\nPlayer Const is called by: ",cname)

    def print_details(self):
        print(f"Name is {self.name} and Game is {self.game}")
        return 

class CoolProgrammer(Employee,Player):
    language = "C++"
    # var = 10  #comment each var in Employee,Player and CoolProgrammer and see difference
    def print_language(self):
        print("\n Language is: ",self.language)

harry = Employee("Harry",255,"Instructor")
rohan = Employee("Rohan",455,"Student")

shubham = Player("Shubham",['Cricket'])
karan = CoolProgrammer("Karan",8999,"CoolProgrammer")
# karan = CoolProgrammer("Karan",['Tennis'])      # for Player class
# karan.print_emp()
# karan.print_language()
print(karan.var)