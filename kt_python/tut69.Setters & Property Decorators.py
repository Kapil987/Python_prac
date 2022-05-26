
# ## Example 1:
# class Employee:
#     abc = 10
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#         self.email = f"{fname}.{lname}@company_name.com"
    
#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"

#     def print_email(self):
#         pass

# alya = Employee("Alya","Bhatt")
# nikil = Employee("Nikhil","Sharma")
# # print(nikil.abc)
# print(alya.email)
# alya.lname = "Kapoor"   #why didn't last name changed ??

#Conclusion: lname is not changed because constructor was called at the time of object 
# creation at that time lname was Bhatt, then we printed alya.email and then we  
# we changed the last name so no effect, so what's the solution 

## Example 2: Solution
# class Employee:
#     abc = 10
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f"{fname}.{lname}@company_name.com"
    
#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"
    
#     @property   #email = email(email)
#     def email(self):
#         return f"{self.fname}.{self.lname}@company_name.com" #remove self and see effect

# alya = Employee("Alya","Bhatt")
# # print(alya.abc)
# # print(alya.email())
# alya.lname = "Kapoor" 
# # print(alya.email()) 

## once decorator @porperty is used you can't use alya.email() as a function call
# will be using as a normal variable call -- alya.email 
## What if i dont want to run email() function ?
## i want to give email as a attribute, answer: use decorator propertly at email
# print(alya.email)   

## let say i want to give input as email and it change first and last name
## Example 3: Solution is Setter

class Employee:
    abc = 10
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@company_name.com"
    
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    @property   #email = email(email)
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set.Please set it using setter"
        return f"{self.fname}.{self.lname}@company_name.com" #remove self and see effect
    
    @email.setter
    def email(self,string):
        print("Setting now...")
        names = string.split("@") [0]
        self.fname = names.split(".") [0]
        self.lname = names.split(".") [1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

alya = Employee("Alya","Bhatt")
alya.email = "Alya.Kapoor@company_name.com" # error! if @email.setter is commented 
                                    # to resolve this we need setter
print(alya.fname)
print(alya.lname)
print(alya.email)

## Now i want to delete alya.email
del alya.email ## error! as its searching for deleter, Solution is to make deleter decorator
print(alya.email)   # now i dont want none.none@company_name.com
## Solution add these to @property  if self.fname == None or self.lname == None:
#                                   return "Email is not set"