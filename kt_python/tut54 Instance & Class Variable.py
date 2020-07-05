class Employee:
    number_of_leaves = 8    # This is class variable
    # pass                  # this will give error if pass is provided 


kapil = Employee()      # kapil and rohan are objects of Employee
rohan = Employee()

kapil.name = "Kapil"    # name, salary and role are objects own property
kapil.salary = 2000
kapil.role = "Instructor"

rohan.name =  "rohan"
rohan.salary = 3000
rohan.role = "principal"

print(kapil.number_of_leaves)   # Accessing class variable via class object
Employee.number_of_leaves=10    # Changing class variable for all objects
print("Employee modified leaves print via kapil= ",kapil.number_of_leaves)
print("\n",rohan.__dict__,"\n")
print("\n",Employee.__dict__,"\n")
# ## Change class variable via Class objects
rohan.number_of_leaves =20
print("rohan modified leaves= ",rohan.number_of_leaves)     # Make changes only in this object properties
print("Current Employee.number_of_leaves = ",Employee.number_of_leaves) 
print("\n",rohan.__dict__,"\n")             # number of leaves attributes/variable gets 
#                                             # added to rohan object properties
# print("\n",Employee.__dict__,"\n")

## This means we cannot change Main class varibale via class objects