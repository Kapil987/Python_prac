##Condition 1: when class A constructor is used to create object of class B   
# class A:
#     classvarA = "class variable A"
#     def __init__(self):
#         self.classvarA = "Instance var in class A"  #This is instance variable whoever calls it
#         print("\nClass A constructor called!!")

# class B(A):
#     # pass
#     classvarA = "classvarA of class B"
  

# b = B()
# print(b.classvarA)

# Flow for search of print(b.classvarA):
# 1.instance variable of Inherited main class, if not then
# 2. class variable with same name is present in Own/Derived (class B) class, if not
# 3. search class variable with same name in main/inherited class

##Condition 2: when class B constructor is used to create object of class B    
class A:
    # classvarA = "class variable A" 
    def __init__(self):
        # self.classvarA = "Instance var in class A"  #This is instance variable whoever calls it
        print("\nClass A constructor called!!")

class B(A):
    classvarA = "class variable: classvarA of class B"
    def __init__(self):     # Over-riding constructor of class A
        self.classvarA = "\ninstance variable of class B"
        print("\nClass B constructor called")
b = B()
print(b.classvarA)


## Flow for search of print(b.classvarA):
# 1. instance variable of own class is searched, if not then
# 2. search if class variable with same name is present in derived/own class, if not
# 3. search class variable with same name in main/inherited class
# 4. b.classvarA wont be able to access instance variable of class A as it was constructed
# with contructor of class B

## Flow for search of print(a.classvarA):
# a = A()
# print(a.classvarA)
# 1. instance variable of class A
# 2. class variable of class A
# 3. it cannot access class B variable as its not constructed by class B